---
name: document-router
version: 1.3
description: Routes files dropped in either _inbox/ (local vault) or G:\My Drive\BuildSafe Brain\_inbox\ (Drive inbox) to the correct vault location and mirrors to Drive. Also processes Gmail inbox across all active email streams. Reads each file/email, determines its type and context, copies it to the right folder, and logs the routing decisions.
trigger: /route-inbox
compatibility: claude-code
input: Gmail inbox (all active streams) + _OS/_inbox/ (local vault) + G:\My Drive\BuildSafe Brain\_inbox\ (Drive inbox)
output: Emails processed + files routed to correct vault locations + mirrored to G:\My Drive\ + routing log written
---

## Instructions

You are the vault's document routing system. Your job is to:
1. Process all unread/unlabeled email streams in Gmail
2. Read every unprocessed file in both inboxes
3. Determine where each piece of content belongs
4. Copy/route to the correct location and mirror to Drive
5. Log all routing decisions

Be decisive. If the correct location is ambiguous, choose the most likely destination and flag it for confirmation.

**Starting State:** Unprocessed emails + files sitting in inboxes without a home
**Target State:** All emails processed + files routed to vault + mirrored to Drive + routing log updated

---

### Step 0 — Process Gmail Inbox

Use `mcp__claude_ai_Gmail__search_threads` and `mcp__claude_ai_Gmail__get_thread` to process each email stream below. After processing each email, apply the appropriate Gmail label to mark it processed.

#### 0A — Mobile Drops
**Search query:** `subject:"Mobile Drop" from:aaron@buildsafeiq.com newer_than:7d`

For each thread found:
- Read the full content via `get_thread`
- Parse the subject line format: `[Mobile Drop] - [Topic] - [YYYY-MM-DD]`
- If it contains notes, insights, or tasks → append to today's Daily Note at `BuildSafe IQ/Operations/Daily Notes/YYYY-MM-DD.md` (create if doesn't exist)
- If it contains a YouTube link or URL → route to `_OS/Capture/` with title and link
- If it contains a client-related note → route to the relevant client folder in `Brokerage/Active_Submissions/`
- Apply label: `Oracle - Processed`

#### 0B — Oracle / Google Alert Intelligence
**Search query 1:** `label:Oracle -label:"Oracle - Processed" newer_than:30d`
**Search query 2:** `label:"Oracle — Google Alerts" -label:"Oracle - Processed" newer_than:30d`

For each thread found:
- Read the full content via `get_thread`
- Extract: headline/article title, source publication, key data point or event, risk implication
- Determine intelligence category:
  - Construction market / macro → `BuildSafe IQ/Marketing & Content/Research_Base/Project_Oracle_Feeds/`
  - Insurance / carrier news → same folder, prefix file `[Insurance]`
  - Regulatory / OSHA / compliance → same folder, prefix `[Regulatory]`
  - Competitor / technology → `BuildSafe IQ/Marketing & Content/Research_Base/`
- If the item contains a data point worth building content around → add a content seed to `Content Ideas Backlog.md`
- Apply label: `Oracle - Processed`

**File naming for Oracle extracts:** `YYYY-MM-DD — [Source] — [Short Title].md`

#### 0C — Research Newsletters
**Search query:** `(from:insurancejournal.com OR from:claimsjournal.com OR from:constructiondive.com OR from:enr.com OR from:contractormag.com OR from:theinstitutes.org OR from:bls.gov OR subject:"Broker Brief" OR subject:"Construction Intelligence") newer_than:30d -label:"Oracle - Processed"`

For each thread found:
- Skim subject and body for: new data points, OSHA changes, carrier market shifts, loss trends, construction spend data
- If actionable intel found → extract to `BuildSafe IQ/Marketing & Content/Research_Base/Project_Oracle_Feeds/`
- If it's pure promotional / no signal → skip (do not route)
- If it contains a research article worth full extraction → flag: "This looks like research worth extracting. Want me to run the full 4-layer extraction?"
- Apply label: `Oracle - Processed`

#### 0D — BD Threads (Business Development)
**Search query:** `(from:jhession1976@gmail.com OR from:jcaruso@bantamgroup.com OR from:keith@ckteamllc.com OR from:leaderbank.com) newer_than:14d -label:"Oracle - Processed"`

For each thread found:
- Read via `get_thread`
- Identify: new introductions, meeting requests, follow-up actions, investor context
- Surface key developments as a bullet list in the routing log
- Flag any required action: "Reply needed", "Meeting to schedule", "Intro to follow up"
- Do NOT auto-draft replies — flag for Aaron to handle
- Apply label: `Oracle - Processed`

#### 0E — Self-Captures (Sent to Self)
**Search query:** `from:aaron@buildsafeiq.com to:aaron@buildsafeiq.com newer_than:14d -subject:"Mobile Drop" -label:"Oracle - Processed"`

For each thread found:
- Determine content type from subject and body:
  - YouTube link / article URL → `_OS/Capture/` with title and URL
  - Raw idea or insight → append to `_OS/Capture/Raw Ideas.md`
  - Research link → route to `Research_Base/` with summary
  - Task or reminder → flag in routing log as "Add to task list"
- Apply label: `Oracle - Processed`

#### 0F — Team Updates
**Search query:** `from:evj@buildsafeiq.com newer_than:14d -label:"Oracle - Processed"`

For each thread found:
- Identify: forwarded articles (route to Research_Base), action items (flag for Aaron), FYI items (log and close)
- Apply label: `Oracle - Processed`

#### Gmail Processing Summary
After completing all 6 email streams, output a summary table:

| Stream | Threads Found | Processed | Flagged | Labels Applied |
|---|---|---|---|---|
| Mobile Drops | N | N | N | Oracle - Processed |
| Oracle / Alerts | N | N | N | Oracle - Processed |
| Newsletters | N | N | N | Oracle - Processed |
| BD Threads | N | N | N | Oracle - Processed |
| Self-Captures | N | N | N | Oracle - Processed |
| Team Updates | N | N | N | Oracle - Processed |

---

### Step 1 — Scan Both File Inboxes

List all files in:
1. `_OS/_inbox/` (local vault inbox) and its immediate subfolders
2. `G:\My Drive\BuildSafe Brain\_inbox\` (Drive inbox)

Exclude:
- Files already in subfolders named for a specific client (process via `/onboard-client`)
- Files named `routing-log.md`

If both inboxes are empty: skip to routing log.

Note the source (local or Drive) for each file — it affects Step 6 handling.

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

### Gmail Processing
| Stream | Threads | Processed | Flagged |
|---|---|---|---|
| [stream] | N | N | N |

### BD Thread Flags
- [contact] — [summary of new development or required action]

### File Routing
| File | Source | Classified As | Routed To | Drive Sync | Status |
|---|---|---|---|---|---|
| [filename] | Local / Drive | [type] | [destination] | ✅ / ⚠️ | ✅ Routed / ⚠️ Flagged |

### Flagged for Manual Review
- [file or email] — [reason]

### Next Actions Required
- [item] → [command to run or action needed]
```

---

### Step 6 — Mirror to Google Drive

After routing each file locally, write it to the corresponding path under `G:\My Drive\BuildSafe Brain\` using the Write tool.

**Drive path mapping (mirrors vault structure):**
| Local Vault Path | Drive Mirror Path |
|---|---|
| `BuildSafe IQ/Marketing & Content/Research_Base/` | `G:\My Drive\BuildSafe Brain\Research_Base\` |
| `BuildSafe IQ/Marketing & Content/Research_Base/Project_Oracle_Feeds/` | `G:\My Drive\BuildSafe Brain\Research_Base\Project_Oracle_Feeds\` |
| `BuildSafe IQ/Operations/Meeting Notes/` | `G:\My Drive\BuildSafe Brain\Meeting Notes\` |
| `BuildSafe IQ/Finance/` | `G:\My Drive\BuildSafe Brain\Finance\` |
| `BuildSafe IQ/Legal/` | `G:\My Drive\BuildSafe Brain\Legal\` |
| `BuildSafe IQ/Product/` | `G:\My Drive\BuildSafe Brain\Product\` |
| `BuildSafe IQ/Marketing & Content/Content/Pipeline/` | `G:\My Drive\BuildSafe Brain\Content\Pipeline\` |

**For files sourced from `G:\My Drive\BuildSafe Brain\_inbox\`:** They're already in Drive — just copy to the correct Drive subfolder. No separate sync needed.

**For ⚠️ flagged files:** Do NOT mirror to Drive until Aaron confirms the routing destination.

Create Drive subfolders as needed via Bash if the path doesn't exist.

---

### Stop Conditions
- Do NOT delete files from either inbox — copy only, never move
- Do NOT route to `BuildSafe IQ/Legal/` or `Brokerage/Legal/` without flagging for Aaron's review
- Stop and ask if a file could belong to multiple destinations with equal probability
- Do NOT route personal financial documents without explicit confirmation
- Do NOT mirror ⚠️ flagged files to Drive until Aaron confirms
- Do NOT auto-draft BD replies — surface the thread and flag for Aaron

### Checkpoint Output
`✅ /route-inbox complete. [N] emails processed across [N] streams. [N] files routed + mirrored to Drive. [N] flagged for manual review. [N] next actions queued.`
