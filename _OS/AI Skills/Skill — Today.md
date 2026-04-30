---
name: today
version: 1.0
description: Morning daily brief. Creates today's Daily Note from template, reads last 3 Agent_Logs for context, surfaces open tasks and content pipeline items. Outputs a structured daily brief.
trigger: /today
---

## Instructions

You are generating Aaron's morning operating brief.

**Starting State:** No Daily Note exists for today (or it's a blank stub)
**Target State:**
1. Today's Daily Note created from template at `BuildSafe IQ/Operations/Daily Notes/YYYY-MM-DD.md`
2. Structured daily brief output to terminal

---

### Step 1 — Create Today's Daily Note

Check if `BuildSafe IQ/Operations/Daily Notes/[today's date].md` exists.

- **If NO:** Create it using `_OS/Templates/Daily Note Template.md`. Replace `{{date}}` with today's full date (e.g., `2026-04-15 — Tuesday`). Write to `BuildSafe IQ/Operations/Daily Notes/YYYY-MM-DD.md`.
- **If YES and has content beyond the template:** Do not overwrite. Read it and continue to Step 2.
- **If YES and is empty stub:** Populate the template structure and continue.

---

### Step 2 — Read Recent Session Context

Read the 3 most recent files in `_OS/_brain/Agent_Logs/` (sorted by filename, descending).
If `Agent_Logs/` is empty or doesn't exist, skip this step and note: "No prior session digests found."

Extract from digests:
- Open loops flagged for carry-forward
- Decisions that are still active
- Any items explicitly noted as "next session" priorities

---

### Step 3 — Read Open Tasks

Read all files in `_OS/_tasks/`. Extract items that are not marked complete.
If folder is empty, note: "No open tasks."

---

### Step 4 — Read Content Pipeline

Read `BuildSafe IQ/Marketing & Content/Content/Pipeline/Content Pipeline.md`.
Extract any items in "In Progress" or "Due This Week" status.
If file doesn't exist, skip.

---

### Step 5 — Output Daily Brief

Output in this exact format:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DAILY BRIEF — [DATE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CARRYING FORWARD
[Open loops and priorities from last session. If none: "Clean slate."]

OPEN TASKS
[From _OS/_tasks/. If none: "None."]

CONTENT PIPELINE (THIS WEEK)
[Items due or in progress. If none: "Nothing scheduled."]

SUGGESTED FOCUS TODAY
[Top 1–2 specific items to work on, based on all context above]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

After output, update the "Morning Brief" section of today's Daily Note with this briefing.

---

### Stop Conditions
- Do NOT modify any file except creating/populating today's Daily Note
- Do NOT modify memory.md
- Do NOT modify Agent_Logs files — read only
- Stop and confirm if today's Daily Note already has substantial user-written content (don't overwrite brain dumps)

### Checkpoint Output
`✅ /today complete. Daily Note ready at BuildSafe IQ/Operations/Daily Notes/[date].md`
