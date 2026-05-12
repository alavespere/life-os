---
name: document-router
version: 1.2
description: Routes files dropped in either _inbox/ (local vault) or G:\My Drive\BuildSafe Brain\_inbox\ (Drive inbox) to the correct vault location and mirrors to Drive. Reads each file, determines its type and context, copies it to the right folder, and logs the routing decisions.
trigger: /route-inbox
compatibility: claude-code
input: All unprocessed files in _OS/_inbox/ AND G:\My Drive\BuildSafe Brain\_inbox\
output: Files routed to correct vault locations + mirrored to G:\My Drive\ + routing log written
---

## Instructions

You are the vault's document routing system. Your job is to read every unprocessed file in both inboxes, determine where each belongs, copy it to the correct location, and mirror it to Drive. Be decisive. If the correct location is ambiguous, choose the most likely destination and flag it for confirmation.

**Starting State:** Files sitting in either inbox without a home
**Target State:** All files routed to vault + mirrored to G:\My Drive\ + routing log updated

---

### Step 1 — Scan Both Inboxes

List all files in:
1. `_OS/_inbox/` (local vault inbox) and its immediate subfolders
2. `G:\My Drive\BuildSafe Brain\_inbox\` (Drive inbox)

Exclude:
- Files already in subfolders named for a specific client (process via `/onboard-client`)
- Files named `routing-log.md`

If both inboxes are empty: "Both inboxes are clear. Nothing to route."

Note the source (local or Drive) for each file — it affects Step 7 handling.

---

### Step 2 — Classify Each File

For each file, read its content and classify it:

| Document Type | Local Vault Destination | Notes |
|---|---|---|
| COI (Certificate of Insurance) | `Brokerage/Active_Submissions/[client-name]/documents/` | Run `/analyze-coi` after routing |
| Loss run document | `Brokerage/Active_Submissions/[client-name]/documents/` | Run `/analyze-loss-runs` after routing |
| Client intake / application | `_OS/_inbox/[client-name]/` | Queue for `/onboard-client` |
| Financial statement or model | `BuildSafe IQ/Finance/` or `_Personal/Finance/` based on context | |
| Legal document (contract, agreement) | `BuildSafe IQ/Legal/` or `Brokerage/Legal/` | Flag for Aaron review before routing |
| Meeting notes or transcript | `BuildSafe IQ/Operations/Meeting Notes/` | |
| Research article, intelligence, or industry report | `BuildSafe IQ/Marketing & Content/Research_Base/` | Flag for 4-layer extraction (see Note below) |
| Personal health record | `_Personal/Health & Fitness/` | |
| Personal finance document | `_Personal/Finance/` | |
| Content draft or script | `BuildSafe IQ/Marketing & Content/Content/Pipeline/` | |
| Product / technical document | `BuildSafe IQ/Product/` | |
| Unknown / ambiguous | Flag for manual routing | Do not move |

**Note on Research Documents:** Any research article, industry report, or intelligence document should be flagged as a candidate for 4-layer extraction (Archive → Structured Extractions → Model Inputs → Content Seeds). After routing to Research_Base, ask Aaron: "This looks like research worth extracting. Want me to run the full extraction?"

---

### Step 3 — Route Each File

For each classified file:
1. Copy the file to the destination folder
2. Rename if needed to match vault naming conventions: `YYYY-MM-DD — Description.ext`
3. Note the original filename, source inbox, and destination in the routing log

**Do NOT delete files from either inbox until Aaron confirms routing is correct.**

---

### Step 4 — Flag Actionable Files

After routing, identify files that need immediate follow-up:

| File | Routed To | Required Action |
|---|---|---|
| [COI file] | Brokerage/... | Run `/analyze-coi [client-name]` |
| [Loss run] | Brokerage/... | Run `/analyze-loss-runs [client-name]` |
| [Client intake] | _inbox/[name]/ | Run `/onboard-client [client-name]` |
| [Contract] | Legal/ | Manual review required |
| [Research doc] | Research_Base/ | Offer 4-layer extraction |

---

### Step 5 — Write Routing Log

Append to `_OS/_inbox/routing-log.md`:

```markdown
## Routing Run — [YYYY-MM-DD HH:MM]

| File | Source | Classified As | Routed To | Drive Sync | Status |
|---|---|---|---|---|---|
| [filename] | Local / Drive | [type] | [destination] | ✅ / ⚠️ | ✅ Routed / ⚠️ Flagged |

### Flagged for Manual Review
- [file] — [reason]

### Next Actions Required
- [file] → [command to run or action needed]
```

---

### Step 6 — Mirror to Google Drive

After routing each file locally, write it to the corresponding path under `G:\My Drive\BuildSafe Brain\` using the Write tool.

**Drive path mapping (mirrors vault structure):**
| Local Vault Path | Drive Mirror Path |
|---|---|
| `BuildSafe IQ/Marketing & Content/Research_Base/` | `G:\My Drive\BuildSafe Brain\Research_Base\` |
| `BuildSafe IQ/Operations/Meeting Notes/` | `G:\My Drive\BuildSafe Brain\Meeting Notes\` |
| `BuildSafe IQ/Finance/` | `G:\My Drive\BuildSafe Brain\Finance\` |
| `BuildSafe IQ/Legal/` | `G:\My Drive\BuildSafe Brain\Legal\` |
| `BuildSafe IQ/Product/` | `G:\My Drive\BuildSafe Brain\Product\` |
| `BuildSafe IQ/Marketing & Content/Content/Pipeline/` | `G:\My Drive\BuildSafe Brain\Content\Pipeline\` |

**For files sourced from `G:\My Drive\BuildSafe Brain\_inbox\`:** They're already in Drive — just copy to the correct Drive subfolder. No separate sync needed.

**For ⚠️ flagged files:** Do NOT mirror to Drive until Aaron confirms the routing destination.

Create Drive subfolders as needed — `mkdir -p` via Bash if the path doesn't exist.

---

### Stop Conditions
- Do NOT delete files from either inbox — copy only, never move
- Do NOT route to `BuildSafe IQ/Legal/` or `Brokerage/Legal/` without flagging for Aaron's review
- Stop and ask if a file could belong to multiple destinations with equal probability
- Do NOT route personal financial documents without explicit confirmation
- Do NOT mirror ⚠️ flagged files to Drive until Aaron confirms

### Checkpoint Output
`✅ /route-inbox complete. [N] files routed + mirrored to Drive. [N] flagged for manual review. [N] next actions queued.`
