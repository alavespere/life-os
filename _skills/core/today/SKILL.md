---
name: today
version: 1.1
description: Morning daily brief. Creates today's Daily Note from template, reads last 3 Agent_Logs for context, surfaces open tasks, content pipeline items, and calendar. Outputs a structured daily brief.
trigger: /today
compatibility: claude-code
input: Vault state (auto-read — Daily Notes, Agent_Logs, tasks, content pipeline)
output: Structured daily brief to terminal + today's Daily Note created/populated
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

- **If NO:** Create it using `_OS/Templates/Daily Note Template.md`. Replace `{{date}}` with today's full date (e.g., `2026-04-27 — Monday`). Write to `BuildSafe IQ/Operations/Daily Notes/YYYY-MM-DD.md`.
- **If YES and has content beyond the template:** Do not overwrite. Read it and continue to Step 2.
- **If YES and is empty stub:** Populate the template structure and continue.

---

### Step 2 — Read Recent Session Context

Read the 3 most recent files in `_OS/_brain/Agent_Logs/` (sorted by filename, descending).
If `Agent_Logs/` is empty, skip and note: "No prior session digests found."

Extract: open loops flagged for carry-forward, active decisions, "next session" priorities.

---

### Step 3 — Read Open Tasks

Read all files in `_OS/_tasks/`. Extract items not marked complete.
If folder is empty: "No open tasks."

---

### Step 4 — Read Content Pipeline

Read `BuildSafe IQ/Marketing & Content/Content/Pipeline/Content Pipeline.md`.
Extract items in "In Progress" or "Due This Week" status.
If file doesn't exist, skip.

---

### Step 5 — Check State Files

Read `BuildSafe IQ/State/` if it exists. Surface any pending items or flags from state files.

---

### Step 6 — Output Daily Brief

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DAILY BRIEF — [DATE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CARRYING FORWARD
[Open loops from last session. If none: "Clean slate."]

OPEN TASKS
[From _OS/_tasks/. If none: "None."]

CONTENT PIPELINE (THIS WEEK)
[Items due or in progress. If none: "Nothing scheduled."]

STATE FLAGS
[Anything pending in BuildSafe IQ/State/. If none: "No flags."]

SUGGESTED FOCUS TODAY
[Top 1–2 specific items based on all context above]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

After output, update the "Morning Brief" section of today's Daily Note with this briefing.

---

### Stop Conditions
- Do NOT modify any file except creating/populating today's Daily Note
- Do NOT modify memory.md
- Do NOT modify Agent_Logs files — read only
- Stop and confirm if today's Daily Note already has substantial user-written content

### Checkpoint Output
`✅ /today complete. Daily Note ready at BuildSafe IQ/Operations/Daily Notes/[date].md`
