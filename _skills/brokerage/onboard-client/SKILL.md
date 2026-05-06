---
name: onboard-client
version: 1.1
description: Brokerage client intake. Reads all files in _inbox/[client-name], extracts and maps data to ACORD 125/126/140 fields, creates the Active_Submissions folder with overview.md, conversation-log.md, and missing-info-checklist.md.
trigger: /onboard-client [client-name]
compatibility: claude-code
input: All documents in _inbox/[client-name]/ (PDFs, emails, spreadsheets)
output: Brokerage/Active_Submissions/[client-name]/ with 3 structured files
---

## Instructions

You are running the brokerage client onboarding protocol. Operate as a senior commercial underwriter mapping unstructured intake documents to structured ACORD submission data.

**Input:** All files in `_inbox/[client-name]/`
**Target State:** Client folder at `Brokerage/Active_Submissions/[client-name]/` containing:
- `overview.md` — ACORD-mapped data
- `conversation-log.md` — all communications, chronological
- `missing-info-checklist.md` — data gaps by priority

---

### Step 1 — Read All Intake Files

Read every file in `_inbox/[client-name]/`. List each file found and its type.

If folder does not exist or is empty:
> "No intake files found at _inbox/[client-name]/. Drop all client documents there first."
Stop.

---

### Step 2 — Extract ACORD Data

Mark each field: `[EXTRACTED]` / `[INFERRED]` / `[MISSING]`

**ACORD 125 — General Information**
| Field | Value | Status |
|-------|-------|--------|
| Named Insured (Legal Name) | | |
| DBA | | |
| FEIN | | |
| Entity Type | | |
| Years in Business | | |
| State of Domicile | | |
| Mailing Address | | |
| Primary Contact Name | | |
| Primary Contact Phone | | |
| Primary Contact Email | | |
| Primary Operations Description | | |

**ACORD 126 — Commercial General Liability**
| Field | Value | Status |
|-------|-------|--------|
| Annual Gross Revenue | | |
| Payroll — Class 1 + Description | | |
| Payroll — Class 2 + Description | | |
| Payroll — Class 3 + Description | | |
| Total Annual Payroll | | |
| Subcontractor Costs | | |
| Primary Work Type | GC / Sub / Owner-Builder | |
| Project Types | Commercial / Residential / Industrial | |
| Geographic Scope | | |
| Average Project Size | | |
| Largest Single Project (past 3 years) | | |
| Current Backlog | | |

**Safety Record**
| Field | Value | Status |
|-------|-------|--------|
| Experience Modification Rate (EMR) | | |
| OSHA Recordable Rate | | |
| Formal Safety Program | Y / N | |
| Safety Director / Contact | | |
| Last OSHA Inspection | | |

**Claims History**
| Field | Value | Status |
|-------|-------|--------|
| 5-Year Loss Runs Available | Y / N | |
| Total Claims (5yr) | | |
| Total Incurred (5yr) | | |
| Open Reserves (current) | | |
| Large Loss Explanation on File | Y / N | |

**Current Coverage**
| Field | Value | Status |
|-------|-------|--------|
| Current Carrier | | |
| Policy Expiration Date | | |
| CGL Limits (occ / agg) | | |
| Auto Limits | | |
| Workers Comp Limits | | |
| Umbrella Limits | | |
| Estimated Current Premium | | |
| Reason for Shopping | | |

---

### Step 2.5 — Benchmarking Context

Before writing the overview, check `Brokerage/Past_Clients/` for any account in the same contractor class (GC, sub-specialty, A/E, owner-builder). Use matching past accounts to:
- Calibrate whether stated revenue, payroll, and project sizes are reasonable
- Identify coverage lines or limits that prior similar accounts carried
- Surface submission strategies that worked for comparable risk profiles

Note which past account was used for comparison in the overview.md.

---

### Step 3 — Create Client Folder

Create `Brokerage/Active_Submissions/[client-name]/` with:

**overview.md** — copy `Brokerage/ACORD_Templates/ACORD-Overview-Template.md` and populate with Step 2 data. For coverage line applications, reference carrier-specific forms in `Brokerage/Submission_Forms/` (Vantage SDI, TokioMarine cyber, JLG builders, Chubb WC).

**conversation-log.md:**
```markdown
# Conversation Log — [Client Name]
| Date | Type | Participants | Summary |
|------|------|-------------|---------|
```

**missing-info-checklist.md:**
```markdown
# Missing Information Checklist — [Client Name]
_Generated: [date]_

## Critical (Submission Cannot Proceed)
- [ ]

## Important (Carrier Will Ask)
- [ ]

## Nice to Have
- [ ]
```

---

### Step 4 — Output Summary

```
CLIENT ONBOARDED: [Client Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Files read:       [N] documents
Fields populated: [N] / [total]
Fields missing:   [N]

CRITICAL gaps:
  • [top 3]

Folder: Brokerage/Active_Submissions/[client-name]/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Next: /analyze-loss-runs [client-name] once loss runs are in documents/
```

---

### Stop Conditions
- Only write inside `Brokerage/Active_Submissions/[client-name]/`
- Do NOT modify `_inbox/` files
- Stop and ask if two documents have conflicting field values
- Stop and ask if client folder already exists at target path

### Checkpoint Output
`✅ /onboard-client complete. [client-name] created. [N] fields populated. [N] missing info items.`
