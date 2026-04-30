import os
import re
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import csv

BASE = Path(__file__).resolve().parent

def clean_num(s):
    if s is None:
        return None
    s = str(s).strip()
    if s == "":
        return None
    s = s.replace('"', '').replace("\u00a0", "")
    s = re.sub(r"[^0-9.\-]", "", s)
    try:
        return float(s)
    except:
        return None


def read_row_value(csv_path, key_pattern):
    # find a row where first column matches key_pattern (case-insensitive contains)
    with open(csv_path, newline='', encoding='utf-8', errors='replace') as f:
        reader = csv.reader(f)
        headers = next(reader, None)
        # find year columns indices (headers like Y1 2026 or Y1)
        years_idx = []
        year_labels = []
        if headers:
            for i,h in enumerate(headers):
                if h and re.search(r'Y\d|20\d{2}', h):
                    years_idx.append(i)
                    year_labels.append(h)
        for row in reader:
            if len(row) == 0:
                continue
            first = row[0].strip().lower()
            if key_pattern.lower() in first:
                vals = []
                for i in years_idx:
                    v = row[i] if i < len(row) else ''
                    vals.append(clean_num(v))
                return year_labels, vals
    return year_labels, [None]*len(year_labels)


if __name__ == '__main__':
    # files
    pl = BASE / 'P&L Summary (Annual).csv'
    rev_detail = BASE / 'Revenue Detail.csv'
    jv = BASE / 'JV Partner Illustration.csv'

    # read revenue and ebitda from P&L
    years_rev, revenue = read_row_value(pl, 'TOTAL REVENUE')
    years_ebitda, ebitda = read_row_value(pl, 'EBITDA')

    # read JV revenue
    years_jv, jv_revenue = read_row_value(jv, "aaron's total jv revenue")
    if not any(jv_revenue):
        # fallback search in revenue_detail
        years_jv, jv_revenue = read_row_value(rev_detail, "aaron's jv revenue")

    # use years from revenue if available
    years = years_rev or years_ebitda or years_jv
    # normalize labels
    def normalize_years(hdrs):
        out = []
        for h in hdrs:
            if not h:
                out.append('')
            else:
                m = re.search(r'20\d{2}', h)
                if m:
                    out.append(m.group(0))
                else:
                    out.append(h)
        return out

    years = normalize_years(years)

    # Prepare data arrays (convert None to nan) and handle empty/mismatched lengths
    import numpy as np
    def ensure_array(arr, target_len):
        # arr may be list of numbers or empty
        if not arr:
            return np.array([np.nan] * target_len, dtype=float)
        # convert None -> nan
        vals = [v if v is not None else np.nan for v in arr]
        if len(vals) < target_len:
            vals = vals + [np.nan] * (target_len - len(vals))
        return np.array(vals[:target_len], dtype=float)

    target_len = max(1, len(years))
    revenue = ensure_array(revenue, target_len)
    ebitda = ensure_array(ebitda, target_len)
    jv_revenue = ensure_array(jv_revenue, target_len)

    # Create PDF page
    out_pdf = BASE / 'JV_onepager.pdf'
    plt.rcParams.update({'font.size': 10})
    fig = plt.figure(figsize=(8.5, 11))

    # Title
    fig.suptitle('JV One-Page Summary — Financial Brokerage', fontsize=16, y=0.95)

    # Left: bullets (text box)
    ax_text = fig.add_axes([0.05, 0.45, 0.55, 0.45])
    ax_text.axis('off')

    bullets = [
        'Purpose: Discuss JV pilot (80/20 split) and pilot scope.',
        f'Revenue (Model): {int(revenue[0]) if not np.isnan(revenue[0]) else "-"} → {int(revenue[-1]) if not np.isnan(revenue[-1]) else "-"}',
        f'EBITDA: {int(ebitda[0]) if not np.isnan(ebitda[0]) else "-"} → {int(ebitda[-1]) if not np.isnan(ebitda[-1]) else "-"}',
        f"Aaron's JV Rev: {int(jv_revenue[0]) if not np.isnan(jv_revenue[0]) else '-'} → {int(jv_revenue[-1]) if not np.isnan(jv_revenue[-1]) else '-'}",
        'Key assumptions: 1 partner Y1 → 6+ partners Y3+, contingent income at $500K NWP.',
        'Risks: partner recruitment/onboarding, early dependence on Aaron production.',
        'Ask: confirm partner pipeline, pilot timeline, payment cadence, reporting.',
    ]

    text = '\n'.join(['• ' + b for b in bullets])
    ax_text.text(0, 1, text, va='top')

    # Right: three charts stacked
    ax1 = fig.add_axes([0.65, 0.65, 0.3, 0.28])
    ax2 = fig.add_axes([0.65, 0.36, 0.3, 0.28])
    ax3 = fig.add_axes([0.65, 0.07, 0.3, 0.28])

    x = list(range(len(years)))

    if revenue.size and not np.all(np.isnan(revenue)):
        ax1.plot(x, revenue/1e6, marker='o')
        ax1.set_title('Revenue (M)')
        ax1.set_xticks(x); ax1.set_xticklabels(years, rotation=45)
    else:
        ax1.text(0.5,0.5,'No revenue data',ha='center')

    if ebitda.size and not np.all(np.isnan(ebitda)):
        ax2.plot(x, ebitda/1e6, marker='o', color='green')
        ax2.set_title('EBITDA (M)')
        ax2.set_xticks(x); ax2.set_xticklabels(years, rotation=45)
    else:
        ax2.text(0.5,0.5,'No EBITDA data',ha='center')

    if jv_revenue.size and not np.all(np.isnan(jv_revenue)):
        ax3.plot(x, jv_revenue/1e6, marker='o', color='orange')
        ax3.set_title("Aaron's JV Revenue (M)")
        ax3.set_xticks(x); ax3.set_xticklabels(years, rotation=45)
    else:
        ax3.text(0.5,0.5,'No JV revenue data',ha='center')

    # Footer small note
    fig.text(0.05, 0.03, 'Source: Financial_Brokerage_v8_2026-04-07.xlsx — generated CSVs in this folder', fontsize=8)

    pp = PdfPages(out_pdf)
    pp.savefig(fig, bbox_inches='tight')
    pp.close()
    print(f'Created {out_pdf}')
