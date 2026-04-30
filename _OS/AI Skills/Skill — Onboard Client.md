---
name: onboard-client
version: 1.0
description: Brokerage client intake protocol. Reads all files in _inbox/[client-name], extracts ACORD-relevant data, creates the submission folder in Brokerage/Active_Submissions/ with overview.md, conversation-log.md, and missing-info-checklist.md.
trigger: /onboard-client [client-name]
---

## Instructions

You are running the brokerage client onboarding protocol. Operate as a senior commercial underwriter mapping unstructured intake documents to structured ACORD submission data.

**Input:** All files in `_inbox/[client-name]/`
**Target State:** Client folder at `Brokerage/Active_Submissions/[client-name]/` containing:
- `overview.md` — ACORD-mapped data using the base template
- `conversation-log.md` — all communications found in intake documents, in chronological order
- `missing-info-checklist.md` — all data gaps organized by priority

---

### Step 1 — Read All Intake Files

Read every file in `_inbox/[client-name]/`. List each file found and its type.

If the folder does not exist or is empty:
> "No intake files found at _inbox/[client-name]/. Drop all client documents there first, then re-run /onboard-client [client-name]."
Stop.

---

### Step 2 — Extract ACORD Data

For each field below, extract the best available data from the intake files. Mark each field:
- `[EXTRACTED]` — found and confirmed
- `[INFERRED]` — derived from context, needs verification
- `[MISSING]` — not found in any document

**ACORD 125 — General Information**
| Field | Value | Status |
|-------|-------|--------|
| Named Insured (Legal Name) | | |
| DBA | | |
| FEIN | | |
| Entity Type (Corp/LLC/Partnership/Sole Prop) | | |
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
| Annual Gross Revenue (current year) | | |
| Payroll — Classification 1 + Description | | |
| Payroll — Classification 2 + Description | | |
| Payroll — Classification 3 + Description | | |
| Total Annual Payroll | | |
| Subcontractor Costs | | |
| Primary Work Type | GC / Sub / Owner-Builder | |
| Project Types | Commercial / Residential / Industrial | |
| Geographic Scope of Operations | | |
| Average Project Size | | |
| Largest Single Project (past 3 years) | | |
| Current Project Backlog | | |

**Safety Record**
| Field | Value | Status |
|-------|-------|--------|
| Experience Modification Rate (EMR) | | |
| OSHA Recordable Rate | | |
| Formal Safety Program in Place | Y / N | |
| Safety Director / Program Contact | | |
| Last OSHA Inspection Date & Result | | |

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
| Reason for Marketing / Shopping | | |

---

### Step 3 — Create Client Folder

Create `Brokerage/Active_Submissions/[client-name]/` and write three files:

**overview.md**
Copy the ACORD Overview Template from `Brokerage/ACORD_Templates/ACORD-Overview-Template.md` and populate it with all extracted data from Step 2.

**conversation-log.md**
Create with this structure:
```markdown
# Conversation Log — [Client Name]
_Chronological record of all communications_

| Date | Type | Participants | Summary |
|------|------|-------------|---------|
| | | | |
```
Populate with any communications, emails, or meeting notes found in the intake documents.

**missing-info-checklist.md**
Create with this structure:
```markdown
# Missing Information Checklist — [Client Name]
_Generated: [date]_

## Critical (Submission Cannot Proceed)
- [ ] [Item]

## Important (Carrier Will Ask)
- [ ] [Item]

## Nice to Have (Strengthens Narrative)
- [ ] [Item]
```
Populate with all `[MISSING]` fields from Step 2, organized by priority.

---

### Step 4 — Output Summary

```
CLIENT ONBOARDED: [Client Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Files read:      [N] documents
Fields populated: [N] / [total]
Fields missing:  [N]

CRITICAL gaps:
  • [top 3 missing critical items]

Folder created: Brokerage/Active_Submissions/[client-name]/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Next step: Run /analyze-loss-runs [client-name] once loss runs are in documents/ folder.
```

---

### Stop Conditions
- Only write inside `Brokerage/Active_Submissions/[client-name]/`
- Do NOT modify any files in `_inbox/`
- Do NOT create files anywhere else
- Stop and ask if two documents provide conflicting values for the same field (e.g., two different revenue figures)
- Stop and ask before proceeding if client folder already exists at the target path

### Checkpoint Output
`✅ /onboard-client complete. [client-name] folder created. [N] fields populated. [N] missing info items.`
