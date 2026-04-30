---
name: analyze-loss-runs
version: 1.1
description: Analyzes 5-year loss run documents for a brokerage submission. Calculates frequency, severity, and loss ratio metrics by year. Identifies trends. Drafts the three-section underwriting narrative. Updates missing-info-checklist.
trigger: /analyze-loss-runs [client-name]
compatibility: claude-code
input: Loss run documents in Brokerage/Active_Submissions/[client-name]/documents/
output: loss-run-analysis.md + updated missing-info-checklist.md in client folder
---

## Instructions

You are analyzing loss runs as a senior commercial underwriter preparing a submission package.

**Input:** `Brokerage/Active_Submissions/[client-name]/documents/`
**Target State:**
- `Brokerage/Active_Submissions/[client-name]/loss-run-analysis.md`
- Updated `Brokerage/Active_Submissions/[client-name]/missing-info-checklist.md`

---

### Step 1 — Read Loss Run Documents

Read all files in `Brokerage/Active_Submissions/[client-name]/documents/`.

If not found:
> "No documents found. Create the documents/ subfolder and drop loss run files there."
Stop.

List each file and which coverage line it covers (GL, Auto, WC, Umbrella).

---

### Step 2 — Build Annual Metrics Table

| Policy Year | # Claims | Total Paid | Open Reserves | Total Incurred | Revenue Used | Freq. Rate | Sev. Rate | Loss Ratio |
|------------|----------|-----------|--------------|---------------|-------------|-----------|----------|-----------|

**Formulas:**
- Frequency Rate = # Claims ÷ (Revenue ÷ $1,000,000)
- Severity Rate = Total Incurred ÷ # Claims
- Loss Ratio = Total Incurred ÷ Premium (N/A if no premium data)
- Total Incurred = Total Paid + Open Reserves

Flag every unverifiable number with `[VERIFY]`.

---

### Step 3 — Trend Analysis

- **Frequency:** Increasing / decreasing / flat over 5 years?
- **Severity:** Increasing / decreasing / flat?
- **Loss type clustering:** Same type repeating?
- **Timing patterns:** Seasonal or phase-based clustering?
- **Large loss distortion:** Any single claim >30% of total incurred? Flag separately.
- **Open reserve risk:** Any reserve open >24 months? Flag for adverse development.

---

### Step 4 — Draft Underwriting Narrative

**What Happened:** Facts only — dates, amounts, types. No editorializing.

**Why It Happened:** Root cause analysis. If unknown: "Root cause not documented — must obtain from insured before submission."

**Corrective Actions Taken:** Specific steps the client implemented. If none: `[MUST OBTAIN — carriers will require this for any above-average loss year.]`

---

### Step 5 — Write Output

`Brokerage/Active_Submissions/[client-name]/loss-run-analysis.md`:

```markdown
# Loss Run Analysis — [Client Name]
_Generated: [date] | Lines: [GL/WC/Auto] | Years: [range]_

## Annual Metrics
[Table]

## Trend Analysis
[Findings]

## Underwriting Narrative
### What Happened
### Why It Happened
### Corrective Actions Taken

## Open Items
[VERIFY flags and gaps]
```

Update `missing-info-checklist.md` with any new gaps found.

---

### Stop Conditions
- Only write to the client's Active_Submissions folder
- Never estimate a number — flag with `[VERIFY]`
- Stop and ask if data across documents is contradictory
- Stop and ask if you can't determine which coverage line a document belongs to

### Checkpoint Output
`✅ /analyze-loss-runs complete. [N] years analyzed. [N] claims, $[X] total incurred. [N] items added to checklist.`
