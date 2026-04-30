---
name: review
version: 1.1
description: End-of-session digest. Scans today's Daily Note, extracts qualifying entries for memory.md, presents each for approval, appends approved entries, and writes a session digest to Agent_Logs/.
trigger: /review
compatibility: claude-code
input: Today's Daily Note (auto-read from vault)
output: Approved entries appended to memory.md + session digest in Agent_Logs/
---

## Instructions

You are running the end-of-session review protocol.

**Starting State:** Today's Daily Note at `BuildSafe IQ/Operations/Daily Notes/YYYY-MM-DD.md`
**Target State:**
1. Approved entries appended to `_OS/_brain/memory.md`
2. Session digest written to `_OS/_brain/Agent_Logs/YYYY-MM-DD-HH.md`

---

### Step 1 — Read Today's Daily Note

Read `BuildSafe IQ/Operations/Daily Notes/[today's date].md`.

If the file does not exist:
> "No Daily Note found for today. Run `/today` first to create one, then add your notes before running `/review`."
Stop.

---

### Step 2 — Extract Qualifying Entries

Scan the Daily Note for entries that qualify for memory.md. Apply these signal rules:

| Signal | Qualifies? |
|--------|-----------|
| Decision with a tradeoff | ✅ Yes |
| Risk flag — legal, financial, operational, brokerage | ✅ Yes |
| Repeated friction (third mention of the same problem) | ✅ Yes |
| Revenue event | ✅ Yes |
| System or process change | ✅ Yes |
| Insight that changes how a problem is framed | ✅ Yes |
| Task completed with no lesson attached | ❌ No |
| Vague observation ("felt tired", "busy day") | ❌ No |
| Routine activity | ❌ No |

---

### Step 3 — Present Each Entry for Approval

For each qualifying entry, present:

```
PROPOSED ENTRY [#N of N]:
Type: [Decision / Lesson / Pattern / Risk / Insight]
Category: [Strategy / Legal / Finance / Ops / Team / Content / Brokerage / System]
Title: [Short descriptive title]
Context: [One sentence — what triggered this]
Entry: [2–4 sentences. The actual content.]

→ Approve, edit, or skip? (a/e/s)
```

Wait for Aaron's response before proceeding to the next entry.
**NEVER append to memory.md without explicit approval on each entry.**

---

### Step 4 — Append Approved Entries

For each approved entry, append to `_OS/_brain/memory.md` using exact format:

```markdown
### YYYY-MM-DD HH:MM — [Category] — [Title]
**Type:** [Decision / Lesson / Pattern / Risk / Insight]
**Context:** [One sentence trigger]
**Entry:** [Content]
**Linked files:** [[relevant file if any]]
---
```

---

### Step 5 — Write Session Digest

Write `_OS/_brain/Agent_Logs/YYYY-MM-DD-HH.md` with this structure:

```markdown
# Session Digest — YYYY-MM-DD HH:MM

## What Was Worked On
- [3–5 bullets covering the session's work]

## Decisions Made
- [List decisions from this session]

## Open Loops (Carry Forward)
- [Anything unresolved that needs to continue next session]

## Files Created / Modified
- [List with paths]

## Memory Entries Appended
- [N entries added to memory.md]
```

---

### Stop Conditions
- Stop immediately if today's Daily Note does not exist — do not proceed
- Never append to memory.md without explicit approval
- Never write outside `_OS/_brain/memory.md` and `_OS/_brain/Agent_Logs/`
- Stop and ask if an entry's category or type is ambiguous

### Checkpoint Output
`✅ /review complete. [N] entries appended to memory.md. Digest written to Agent_Logs/[filename].`
