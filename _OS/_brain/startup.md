# startup.md — Claude Code Session Startup Script
_Do not modify this file. It is the boot sequence for every Claude Code session._
_Last updated: 2026-05-18_

---

## Session Startup Instructions

At the start of every session, silently execute these steps in order:

1. Read `_OS/_brain/soul.md` in full
2. Read `_OS/_brain/user.md` in full
3. Read the last 30 entries of `_OS/_brain/memory.md`
4. Check if today's Daily Note exists at `BuildSafe IQ/Operations/Daily Notes/YYYY-MM-DD.md`
   - **If NO:** Run `/today` automatically — create the note, check Agent_Logs and tasks, output the daily brief. Do NOT output "Context loaded. Ready." first.
   - **If YES:** Output exactly one line: `Context loaded. Ready.` then wait.

Do not summarize what you read.
Do not ask clarifying questions.

You now know who Aaron is, what he is building, and what he has learned.
Act accordingly in everything that follows.

---

## Vault Path Reference
All file paths are relative to vault root:
`C:\Users\aaron.lavespere\Documents\Aaron's Life & Business OS\`

## Write Zones (quick reference — full rules in soul.md)
- **Append only:** `_OS/_brain/memory.md`
- **Create new files:** `BuildSafe IQ/Operations/Daily Notes/`, `_OS/_brain/Agent_Logs/`, `_OS/_tasks/`
- **Read only:** everything else unless Aaron explicitly instructs otherwise
