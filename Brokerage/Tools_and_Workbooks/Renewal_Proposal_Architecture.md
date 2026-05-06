# Renewal Proposal Workbook — Architecture & Schema
_Based on: LJA Renewal Proposal 8.1.2023-2024 (Greyling/EPIC)_
_Status: Reference template for all commercial renewals_

---

## Overview

A 46-sheet macro-enabled Excel workbook that generates a complete renewal proposal package for a commercial insurance client. All data flows from a single **Input** sheet outward to print-ready coverage detail sheets and executive summary sheets.

**The document is a one-input-many-output system.**
Enter data once in Input → every coverage sheet, summary, and comparison auto-populates.

---

## Sheet Index

### Front Matter (print-ready, client-facing)
| Sheet | Purpose |
|-------|---------|
| Cover | Title page — named insured, renewal date, broker team |
| Schedule Named | Master policy schedule — all lines, carriers, limits, premiums |
| Renewal Strategy | Narrative strategy memo (text, non-formula) |
| Renewal Strategy (2) | Extended strategy with market narrative |
| Insurers Approached (PL) | Market submissions log — PL lines only |
| Insurers Approached | Market submissions log — all P&C lines |
| Explanation Renewal Comparisons | Footnote legend for comparison methodology |

### Analysis Engine
| Sheet | Purpose |
|-------|---------|
| Input | **Master data hub.** Every carrier, premium, exposure, limit, deductible enters here. ~1,200+ rows organized in ~40-row blocks per coverage line. |
| Renewal Summary (Incumbent) | Side-by-side: Expiring vs. Renewal (incumbent only). Pulls 100% from Input. |
| Renewal Summary (Market) | Side-by-side: Expiring vs. Incumbent vs. Alternative market. Pulls 100% from Input. The primary deliverable. |

### Coverage Detail Sheets (one per line, print-ready)
| Sheet | Coverage Line |
|-------|--------------|
| Professional Liability | E&O — revenue-based, surplus lines |
| Right of Way | Right of Way acquisition PL — revenue-based |
| CPL | Contractors Pollution Liability |
| Excess Professional Liability | First excess layer over PL |
| Excess Professional Liability 2 | Second excess layer |
| General Liab. | CGL — payroll/revenue-based |
| Workers Comp (AOS) | WC — All Other States |
| Workers Comp (CA) | WC — California (separate rating) |
| Business Auto | BAP — scheduled autos |
| Auto Symbols | Auto coverage symbol reference |
| Umbrella Liability | Primary umbrella — follows form |
| Excess Umbrella | Excess over umbrella |
| Property | Commercial property — TIV-based |
| IM | Inland Marine (detailed scheduled items) |
| Inland Marine | Inland Marine (summary) |
| Excess Property | Excess property layer |
| Package - Property | Package deal property component |
| Package - Inland Marine | Package deal IM component |
| Property Coverage by Location | Location-by-location TIV schedule |
| Watercraft | Watercraft/hull |
| BTA | Business Travel Accident |
| Foreign Package | International coverage |
| DBA | Defense Base Act |
| Executive Liability | D&O + EPL + Fiduciary + Crime (shared limits) |
| Crime | Standalone crime / fidelity |
| Cyber Liability | Cyber — revenue-based, SL taxes |
| Kidnap & Ransom | K&R — multi-year policy |
| Tech Liability | Technology E&O |
| Drone | Drone liability + hull |

### Administrative (client-facing service pages)
| Sheet | Purpose |
|-------|---------|
| Subjectivities | Carrier subjectivities and outstanding items |
| When to Call | Claim reporting contacts by line |
| CoC | Certificate of Insurance instructions |
| Reporting Claims | Step-by-step claims reporting guide |
| Payment Options | Premium finance and payment instructions |
| Greyling Service Team | Broker team contacts (replace with your team) |
| Final Page | Back cover / disclaimer |

---

## Input Sheet Schema — Row Block Structure

Each coverage line occupies a block of ~40 rows in the Input sheet, with this repeating pattern:

```
[Line name header row]
  Status / submission tracker
  Description of coverage
  Expiring Policy Number
  Renewal Policy Number
  --- Column headers ---
  | Field               | Expiring Program | Expiring Adjusted | Option I | Option II | Bound |
  |---------------------|-----------------|-------------------|----------|-----------|-------|
  | Insurer             |                 |                   |          |           |       |
  | Writing Company     |                 |                   |          |           |       |
  | AM Best Rating      |                 |                   |          |           |       |
  | Premium             | annualized      | adj formula       | manual   | manual    |       |
  | Rate per $100 exp.  | formula         | formula           | formula  | formula   |       |
  | % Change vs Adj     |                 |                   | formula  | formula   |       |
  | Surplus Lines Tax % |                 |                   |          |           |       |
  | Stamping Fee %      |                 |                   |          |           |       |
  | Policy Fee          |                 |                   |          |           |       |
  | Total w/ Taxes      | formula         | formula           | formula  | formula   |       |
  | Commission %        |                 |                   |          |           |       |
  --- Exposure Block ---
  | Exposure Base Label |
  | Expiring Exposure   | value           |                   |          |           |       |
  | Renewal Exposure    |                 |                   | value    |           |       |
  | % Change Exposure   |                 |                   | formula  |           |       |
  --- Limits Block ---
  | Policy Limits (each occurrence, aggregate, SIR/retention, maintenance) |
  --- Deductibles Block ---
```

---

## Key Formula Patterns

### 1. Premium Annualization
Converts a short-period premium to a 12-month equivalent for apples-to-apples comparison.
```
=(actual_premium / actual_days) * 365
```
**Example (PL):** `=(846438/334)*365`

### 2. Blended Rate per $100 of Exposure
```
= premium / (exposure / 100)
```
Where exposure is typically 12-month revenue (gross minus direct reimbursables).

### 3. Expiring Adjusted Premium
Applies the exposure percentage change to the expiring annualized premium.
```
= expiring_annualized + expiring_annualized * exposure_pct_change
```

### 4. Percentage Change (Expiring Adjusted vs. Renewal)
```
= -(expiring_adjusted - renewal) / expiring_adjusted
```
Positive = rate increase. Negative = rate decrease.

### 5. Total Premium with Surplus Lines Taxes & Fees
```
= net_premium * (1 + surplus_lines_tax_pct + stamping_fee_pct)
```
**Texas SL Tax:** 4.85% | **TX Stamping Fee:** 0.075%

### 6. Exposure Change
```
= -(old_exposure - new_exposure) / old_exposure
```

---

## Comparison Column Structure

Every coverage line uses the same 5-column comparison:

| Column | Label | How Populated |
|--------|-------|---------------|
| B | Expiring Program | Annualized from actual short-period premium |
| C | Expiring Adjusted | Expiring × (1 + exposure change) — normalizes for growth |
| D | Renewal Option I | Incumbent carrier renewal quote (manual entry) |
| E | Renewal Option II | Alternative market quote (manual entry) |
| F | Bound | Final bound premium (filled after binding) |

---

## Renewal Summary Logic

**Renewal Summary (Market)** — the primary client deliverable — is structured in three macro-sections:

### Section 1: Total Professional Liability Cost (rows ~6–40)
Subtotals: PL + Right of Way + CPL + Excess PL + Excess PL 2
Grand Total row (row ~40): `=SUM(all PL line total premiums)`

### Section 2: Total P&C Cost (rows ~48–109)
Subtotals by captive vs. non-captive grouping (GL/WC/Auto in one block)
Grand Total row (row ~109): `=SUM(all P&C total premiums)`

### Section 3: Total All Other Insurance (rows ~116–182)
DBA, Executive Liability, Crime, Cyber, K&R, Tech, Drone, BTA, Foreign
Grand Total row (row ~182)

### Grand Total — All Lines (row ~184)
```
= Total_PL_Cost + Total_PC_Cost + Total_Other_Cost
```

---

## How to Use for a New Proposal

### Step 1 — Open the template
Open `Renewal_Proposal_Template.xlsm` from `Brokerage/Tools_and_Workbooks/`.

### Step 2 — Populate the Input sheet (only ever touch Input)
Fill in these fields per coverage line:
- Named insured, address, renewal date
- Policy numbers (expiring and renewal)
- Carrier names and AM Best ratings
- Expiring premium (actual, not annualized — the formula annualizes it)
- Actual policy period in days (for the annualization denominator)
- Renewal Option I and II premiums (manual quotes from markets)
- Surplus lines tax rates (state-specific)
- Exposure base values (revenue, TIV, payroll)
- Limits and retentions

### Step 3 — Do not touch the summary/detail sheets
All downstream sheets auto-populate from Input. They are read-only for data entry purposes.

### Step 4 — Customize service pages
Replace Greyling team contacts with your team in the `Greyling Service Team` sheet.
Update CoC holder, payment instructions, and When to Call contacts.

### Step 5 — Select print areas and export
Each coverage sheet has a defined print area. Use the print/PDF function per sheet.
The `Renewal Summary (Market)` sheet is typically the first deliverable sent.

---

## Template Population Checklist

**Per coverage line (repeat for each active line):**
- [ ] Coverage line name and description
- [ ] Expiring policy number
- [ ] Insurer name (all 4 columns)
- [ ] Writing company (all 4 columns)
- [ ] AM Best rating (all 4 columns)
- [ ] Actual expiring premium (raw, not annualized)
- [ ] Actual policy period days (denominator for annualization)
- [ ] Surplus lines tax rate (if applicable)
- [ ] Stamping fee rate (if applicable)
- [ ] Policy fee (if applicable)
- [ ] Commission % (if applicable)
- [ ] Exposure base — expiring and renewal values
- [ ] Policy limits — each occurrence, aggregate, SIR
- [ ] Renewal Option I premium
- [ ] Renewal Option II premium

**Document-level:**
- [ ] Named insured and address on Cover sheet
- [ ] Renewal date
- [ ] Insurers Approached log (carriers approached + dates)
- [ ] Renewal Strategy narrative
- [ ] Subjectivities list
- [ ] Service team contacts updated
- [ ] When to Call contacts updated

---

## Coverage Lines Not Applicable

If a coverage line does not apply to the client, hide the row in the Renewal Summary sheets (do not delete — the sheet indexing relies on the row structure).

---

## Notes on Special Lines

**Kidnap & Ransom:** Often a 3-year policy. Input stores 3-year premium; use annualized ÷ 3 for comparison row. The notes section calls this out.

**Executive Liability:** D&O + EPL + Fiduciary + Crime often share a single aggregate limit. The template tracks each sublimit separately but rolls up to one total premium.

**WC (CA vs. AOS):** California workers comp is rated and reported separately from all other states. Keep as two separate rows in Input.

**Captive programs:** The template has a "Sub-Total Captive vs. Non-Captive" row in the P&C section of the Renewal Summary. If the client is in or considering a captive, this row separates captive-participant lines for side-by-side cost comparison.
