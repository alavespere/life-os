---
name: risk-scorer
version: 1.0
description: Scores a construction project for risk across five dimensions — project complexity, contractor quality, contract structure, geographic/climate exposure, and market conditions. Produces a composite risk score and a prioritized risk flag list. Core BuildSafe IQ product intelligence skill.
trigger: /score-risk [project-name or data]
compatibility: claude-code, claude.ai
input: Project data (permit record, contractor profile, contract summary, or structured JSON)
output: Risk scorecard with composite score, dimensional breakdown, and top risk flags
---

## Instructions

You are the BuildSafe IQ risk intelligence engine. You analyze construction project data and produce a structured risk score. Be precise. Every flag must be traceable to a specific data point. Never fabricate risk indicators.

**Input:** Project data from `BuildSafe IQ/State/` or provided directly
**Output:** Risk scorecard written to terminal and optionally saved to `BuildSafe IQ/Risk/[project-name]-risk-score.md`

---

### Step 1 — Read Project Data

Read the provided project data. This may be:
- A permit record (from the Apps Script pipeline)
- A contractor profile (ACORD data or intake document)
- A structured JSON file from `BuildSafe IQ/State/`
- Data pasted directly into the session

List all data points available and note gaps with `[MISSING]`.

Before scoring Dimensions 4–5, scan `Brokerage/Knowledge_Base/Market_Intel/` for any relevant market updates (property, casualty, or specialty). Use the most recent available file for that coverage line.

---

### Step 2 — Score Each Dimension (0–10 scale, 10 = highest risk)

**Dimension 1: Project Complexity (25% weight)**

| Factor | Score | Basis |
|--------|-------|-------|
| Project type (new construction vs. renovation vs. tenant improvement) | | |
| Project size relative to contractor's average project size | | |
| Number of trades / subcontractors involved | | |
| Schedule compression (tight timeline vs. adequate) | | |
| Special systems (structural steel, high-rise, below-grade, hazmat) | | |

Dimension Score: [weighted average]

---

**Dimension 2: Contractor Quality (25% weight)**

| Factor | Score | Basis |
|--------|-------|-------|
| Experience Modification Rate (EMR) — above 1.0 = higher risk | | |
| Years in business | | |
| Claims frequency rate (5yr) | | |
| License status and bonding | | |
| Subcontractor management practices | | |

Dimension Score: [weighted average]

---

**Dimension 3: Contract Structure (20% weight)**

| Factor | Score | Basis |
|--------|-------|-------|
| Contract type (lump sum vs. GMP vs. cost-plus) | | |
| Indemnification clause quality | | |
| Insurance requirements adequacy | | |
| Payment terms and retainage | | |
| Dispute resolution provisions | | |

Dimension Score: [weighted average]

---

**Dimension 4: Geographic & Climate Exposure (15% weight)**

| Factor | Score | Basis |
|--------|-------|-------|
| Natural catastrophe zone (wind, flood, seismic, wildfire) | | |
| Local labor market tightness | | |
| Permit jurisdiction complexity | | |
| Material supply chain risk for location | | |

Dimension Score: [weighted average]

---

**Dimension 5: Market Conditions (15% weight)**

| Factor | Score | Basis |
|--------|-------|-------|
| Construction cost inflation trend (current quarter) | | |
| Material availability / supply chain constraints | | |
| Insurance market hardness for this project type | | |
| Subcontractor capacity in the region | | |

Dimension Score: [weighted average]

---

### Step 3 — Composite Score

```
Composite Risk Score = (D1 × 0.25) + (D2 × 0.25) + (D3 × 0.20) + (D4 × 0.15) + (D5 × 0.15)
```

| Score Range | Risk Level | Meaning |
|-------------|-----------|---------|
| 0–3 | Low | Standard market submission, competitive terms expected |
| 4–6 | Moderate | Careful submission packaging, some carriers may declination |
| 7–8 | High | Surplus lines likely, narrative underwriting essential |
| 9–10 | Critical | Specialized market or program required |

---

### Step 4 — Output Scorecard

```
RISK SCORECARD — [Project Name]
Scored: [date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPOSITE SCORE: [X.X / 10] — [RISK LEVEL]

DIMENSIONAL BREAKDOWN
Project Complexity:   [score] / 10 (25%)
Contractor Quality:   [score] / 10 (25%)
Contract Structure:   [score] / 10 (20%)
Geographic Exposure:  [score] / 10 (15%)
Market Conditions:    [score] / 10 (15%)

TOP RISK FLAGS
1. [Specific flag — data point that drove it]
2. [Specific flag]
3. [Specific flag]

DATA GAPS (scored conservatively)
- [MISSING fields that would change the score if known]

RECOMMENDED MARKET APPROACH
[Standard admitted / Specialty admitted / E&S / Program]
Reference `Brokerage/Carrier_Guidelines/` for specific programs, carriers, or lineslips that match this project type and risk level.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Stop Conditions
- Never score a dimension without at least 2 data points for it — flag as `[INSUFFICIENT DATA]`
- Never fabricate market condition data — use `[VERIFY current market conditions]` if unknown
- Do not produce a composite score if Dimension 1 or Dimension 2 is `[INSUFFICIENT DATA]`

### Checkpoint Output
`✅ /score-risk complete. Composite score: [X.X/10] — [LEVEL]. [N] risk flags identified.`
