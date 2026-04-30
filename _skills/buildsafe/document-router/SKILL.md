---
name: document-router
version: 1.1
description: Routes files dropped in _inbox/ to the correct vault location based on content analysis. Reads each file, determines its type and context, moves or copies it to the right folder, and logs the routing decisions. Eliminates manual filing.
trigger: /route-inbox
compatibility: claude-code
input: All unprocessed files in _inbox/
output: Files routed to correct vault locations + routing log written to _inbox/routing-log.md
---

## Instructions

You are the vault's document routing system. Your job is to read every unprocessed file in `_inbox/`, determine where it belongs, and route it to the correct location. Be decisive. If the correct location is ambiguous, choose the most likely destination and flag it for confirmation.

**Starting State:** Files sitting in `_inbox/` without a home
**Target State:** All files routed to correct vault locations + routing log updated

---

### Step 1 — Scan Inbox

List all files in `_inbox/` and its immediate subfolders. Exclude:
- Files already in subfolders named for a specific client (those should be processed via `/onboard-client`)
- Files named `routing-log.md`

If inbox is empty: "Inbox is clear. Nothing to route."

---

### Step 2 — Classify Each File

For each file, read its content and classify it:

| Document Type | Destination |
|--------------|-------------|
| COI (Certificate of Insurance) | `Brokerage/Active_Submissions/[client-name]/documents/` — run `/analyze-coi` after routing |
| Loss run document | `Brokerage/Active_Submissions/[client-name]/documents/` — run `/analyze-loss-runs` after routing |
| Client intake / application | `_inbox/[client-name]/` — queue for `/onboard-client` |
| Financial statement or model | `BuildSafe IQ/Finance/` or `_Personal/Finance/` based on context |
| Legal document (contract, agreement) | `BuildSafe IQ/Legal/` or `Brokerage/Legal/` based on entity |
| Meeting notes or transcript | `BuildSafe IQ/Operations/Meeting Notes/` |
| Research article or intelligence | `BuildSafe IQ/Marketing & Content/Research_Base/Project_Oracle_Feeds/` |
| Personal health record | `_Personal/Health & Fitness/` |
| Personal finance document | `_Personal/Finance/` |
| Content draft or script | `BuildSafe IQ/Marketing & Content/Content/Pipeline/` |
| Product / technical document | `BuildSafe IQ/Product/` |
| Unknown / ambiguous | Flag for manual routing — do not move |

---

### Step 3 — Route Each File

For each classified file:
1. Copy the file to the destination folder
2. Rename if needed to match vault naming conventions (YYYY-MM-DD — Description.ext)
3. Note the original filename and destination in the routing log

**Do NOT delete files from `_inbox/` until Aaron confirms routing is correct.**

---

### Step 4 — Flag Actionable Files

After routing, identify files that need immediate follow-up action:

| File | Routed To | Required Action |
|------|----------|----------------|
| [COI file] | Brokerage/... | Run `/analyze-coi [client-name]` |
| [Loss run file] | Brokerage/... | Run `/analyze-loss-runs [client-name]` |
| [Client intake] | _inbox/[name]/ | Run `/onboard-client [client-name]` |
| [Contract] | Legal/ | Manual review required |

---

### Step 5 — Write Routing Log

Append to `_inbox/routing-log.md`:

```markdown
## Routing Run — [YYYY-MM-DD HH:MM]

| File | Classified As | Routed To | Status |
|------|--------------|----------|--------|
| [filename] | [type] | [destination] | ✅ Routed / ⚠️ Flagged |

### Flagged for Manual Review
- [file] — [reason for ambiguity]

### Next Actions Required
- [file] → [command to run]
```

---

### Step 6 — Clear Processed Paths from README

After successfully routing a file that was listed as a raw file path in `_inbox/README.md`:
1. Remove that file path line from the README
2. Only remove paths for files with status ✅ Routed — leave any ⚠️ Flagged paths in place until Aaron confirms
3. If all listed paths have been routed, the path section of the README will be empty — that is correct

This keeps the README as a live queue: paths present = not yet processed, paths absent = done.

---

### Step 7 — Push to Google Drive

After every file is routed locally (Step 3), push it to the corresponding Google Drive folder using `mcp__claude_ai_Google_Drive__create_file`.

**Reference:** Load `_skills/buildsafe/document-router/drive-folder-map.md` to get the Drive folder ID for each destination path.

**For each ✅ routed file:**
1. Look up the local destination path in `drive-folder-map.md` to get the Drive folder ID
2. Read the file content from its local vault path
3. Base64-encode the content
4. Call `mcp__claude_ai_Google_Drive__create_file` with:
   - `title`: the routed filename (same name used in the vault)
   - `parentId`: the Drive folder ID from the map
   - `content`: base64-encoded file content
   - `mimeType`: match the file extension (`.md` → `text/markdown`, `.pdf` → `application/pdf`, `.docx` → `application/vnd.openxmlformats-officedocument.wordprocessingml.document`, `.pptx` → `application/vnd.openxmlformats-officedocument.presentationml.presentation`, `.csv` → `text/csv`)
   - `disableConversionToGoogleType`: `true` — preserve original file format, do not auto-convert to Google Docs/Sheets

**If the destination subfolder doesn't exist in Drive yet:**
- Create it first using `mcp__claude_ai_Google_Drive__create_file` with `mimeType: application/vnd.google-apps.folder` and the parent's Drive folder ID
- Then upload the file into the newly created folder
- Add the new folder ID to `drive-folder-map.md`

**For ⚠️ flagged files:** Do NOT push to Drive until Aaron confirms the routing destination.

**Update the routing log** — add a `Drive` column to the routing log table:

| File | Classified As | Routed To | Drive | Status |
|------|--------------|-----------|-------|--------|
| [filename] | [type] | [local path] | ✅ Pushed / ⚠️ Pending | ✅ Routed |

---

### Stop Conditions
- Do NOT delete files from `_inbox/` — copy only, never move
- Do NOT route to `BuildSafe IQ/Legal/` or `Brokerage/Legal/` without flagging for Aaron's review
- Stop and ask if a file could belong to multiple destinations with equal probability
- Do NOT route personal financial documents without explicit confirmation
- Do NOT push ⚠️ flagged files to Drive until Aaron confirms

### Checkpoint Output
`✅ /route-inbox complete. [N] files routed + pushed to Drive. [N] flagged for manual review. [N] next actions queued.`
