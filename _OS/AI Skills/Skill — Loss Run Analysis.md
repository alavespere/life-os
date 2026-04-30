---
name: analyze-loss-runs
version: 1.0
description: Analyzes 5-year loss run documents for a brokerage submission. Calculates frequency, severity, and loss ratio by year. Identifies trends. Drafts the structured underwriting narrative. Updates the client's missing-info-checklist.
trigger: /analyze-loss-runs [client-name]
---

## Instructions

You are analyzing loss runs as a senior commercial underwriter preparing a submission package for placement.

**Input:** Loss run documents in `Brokerage/Active_Submissions/[client-name]/documents/`
**Target State:**
- `Brokerage/Active_Submissions/[client-name]/loss-run-analysis.md` — metrics + narrative
- Updated `Brokerage/Active_Submissions/[client-name]/missing-info-checklist.md`

---

### Step 1 — Read Loss Run Documents

Read all files in `Brokerage/Active_Submissions/[client-name]/documents/`.

If no documents folder exists or no loss run files found:
> "No loss run documents found at Brokerage/Active_Submissions/[client-name]/documents/. Create the documents/ subfolder and drop the loss run PDFs or exported files there."
Stop.

List each file found and what coverage line it covers (GL, Auto, WC, Umbrella, etc.).

---

### Step 2 — Build Annual Metrics Table

For each year of available data (target: 5 years), extract:

| Policy Year | # Claims | Total Paid | Reserves (Open) | Total Incurred | Revenue Used | Freq. Rate | Sev. Rate | Loss Ratio |
|------------|----------|-----------|----------------|---------------|-------------|-----------|----------|-----------|
| | | | | | | | | |

**Calculations:**
- **Frequency Rate** = # Claims ÷ (Revenue ÷ $1,000,000)
- **Severity Rate** = Total Incurred ÷ # Claims
- **Loss Ratio** = Total Incurred ÷ Premium (if premium data is available; otherwise note as N/A)
- **Total Incurred** = Total Paid + Open Reserves

Flag every number you cannot verify from the source documents with `[VERIFY]`.

---

### Step 3 — Trend Analysis

After building the metrics table, analyze:

**Frequency Trend:** Is claim count increasing, decreasing, or flat over 5 years?

**Severity Trend:** Is average incurred per claim increasing, decreasing, or flat?

**Loss Type Clustering:** Are there patterns in claim type (slip/fall, property damage, auto, WC)?

**Timing Patterns:** Do losses cluster in certain months or project phases?

**Large Loss Distortion:** Identify any single claim that represents more than 30% of total incurred — flag it separately so it doesn't distort the averages.

**Open Reserve Risk:** Identify open reserves that could develop adversely. Flag any reserve that has been open more than 24 months.

---

### Step 4 — Draft Underwriting Narrative

Structure in exactly three sections. Be precise and factual. Do not editorialize.

**What Happened:**
State the facts: total claims, total incurred, span of years analyzed, dominant loss types. Example: "Over the 5-year period from [year] to [year], [Company] experienced [N] claims across GL and WC lines, with total incurred of $[X]. The most frequent loss type was [type], representing [%] of all claims."

**Why It Happened:**
Root cause analysis based on the data available. If the cause is not documented: state explicitly "Root cause for [loss type] losses is not documented in available loss runs. This must be addressed in the insured interview prior to submission."

**Corrective Actions Taken:**
Specific steps documented in the client's intake materials. If none are documented: flag as `[MUST OBTAIN — Carriers will require an explanation of corrective actions for any loss year with frequency or severity above market average.]`

---

### Step 5 — Write Loss Run Analysis File

Write `Brokerage/Active_Submissions/[client-name]/loss-run-analysis.md` with:

```markdown
# Loss Run Analysis — [Client Name]
_Generated: [date] | Lines analyzed: [GL/WC/Auto/etc.] | Years covered: [range]_

---

## Annual Metrics

[Metrics table from Step 2]

---

## Trend Analysis

[Findings from Step 3]

---

## Underwriting Narrative

### What Happened
[Step 4 — What Happened]

### Why It Happened
[Step 4 — Why It Happened]

### Corrective Actions Taken
[Step 4 — Corrective Actions]

---

## Open Items
[Any data gaps, VERIFY flags, or items needed from insured]
```

---

### Step 6 — Update Missing Info Checklist

Append any new gaps to `Brokerage/Active_Submissions/[client-name]/missing-info-checklist.md`.

Common additions from loss run analysis:
- Missing revenue data (needed for frequency rate calculation)
- Missing premium data (needed for loss ratio)
- Undocumented root causes for major losses
- Missing corrective action documentation
- Open reserves with no status update

---

### Stop Conditions
- Only write to `Brokerage/Active_Submissions/[client-name]/`
- Flag every metric you cannot verify from source documents with `[VERIFY]` — never estimate
- Stop and ask if loss run data across documents is contradictory
- Stop and ask if you cannot determine which coverage line a loss run belongs to

### Checkpoint Output
`✅ /analyze-loss-runs complete. [N] years analyzed. [N] claims, $[X] total incurred. Narrative drafted. [N] items added to missing info checklist.`
