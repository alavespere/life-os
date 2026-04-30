# Skill — Process Capture
_Trigger: `/process-capture`_
_Last updated: 2026-04-08_

---

## Purpose
Read everything Aaron has dropped into the capture zones, categorize each entry,
route it to the correct vault location, and clear processed content.
This is the bridge between raw thought and organized second brain.

---

## Capture Zones (Read These First)

1. `_OS/Capture/Quick Capture.md` — typed thoughts, brain dumps, loose notes
2. `_OS/Capture/Meeting Transcripts/` — any new files not yet processed
3. `_OS/_inbox/` — any files dropped for intake

If all zones are empty, report that and stop.

---

## Execution Steps

### Step 1 — Read All Capture Zones
Read every entry in `Quick Capture.md`. List any files present in `Meeting Transcripts/` and `_inbox/`. Report the full inventory before doing anything else.

### Step 2 — Categorize Each Entry
Classify each item using the routing table below. A single capture entry may produce multiple routed outputs (e.g., a meeting note can yield both a daily note AND a task).

### Step 3 — Route (Write-Zone-Safe Items First)
Execute all writes to safe zones automatically. Flag everything else for Aaron's confirmation before writing.

### Step 4 — Report
Present a routing summary: what was written where, what is pending Aaron's confirmation.

### Step 5 — Archive Processed Entries
After Aaron confirms (or declines) flagged items, move processed entries from `Quick Capture.md` into a dated archive section at the bottom of the file under `## Archived — YYYY-MM-DD`. Do not delete them.

---

## Routing Table

| Signal in Entry | Category | Destination | Write Zone |
|---|---|---|---|
| Meeting / call / spoke with / transcript | Meeting Note | `BuildSafe IQ/Operations/Daily Notes/YYYY-MM-DD — [Topic].md` | ✅ Auto-write |
| TODO / need to / follow up / action item / by [date] | Task | `_OS/_tasks/TASK — [title].md` | ✅ Auto-write |
| Decided / decision / going with / we're not doing | Decision | Append to `_OS/_brain/memory.md` | ✅ Auto-write |
| Risk / legal / Hession / contract / license / compliance | Legal/Risk Flag | Append to `_OS/_brain/memory.md` as Risk type | ✅ Auto-write |
| Lesson / pattern / keep doing / stop doing / mistake | Lesson/Pattern | Append to `_OS/_brain/memory.md` | ✅ Auto-write |
| Idea for content / LinkedIn / post / article / script | Content Idea | Flag → confirm → `BuildSafe IQ/Marketing & Content/` | ⚠️ Confirm first |
| Lead / prospect / intro / broker / GC / subcontractor | Sales/CRM | Flag → confirm → `BuildSafe IQ/Sales & CRM/` | ⚠️ Confirm first |
| Investor / pitch / term sheet / VC / raise | Fundraising | Flag → confirm → `BuildSafe IQ/Operations/` | ⚠️ Confirm first |
| Product / feature / build / fix / user feedback | Product | Flag → confirm → `BuildSafe IQ/Product/` | ⚠️ Confirm first |
| Personal / health / family / fitness / goals / money | Personal | Flag → confirm → `_Personal/` | ⚠️ Confirm first |
| General thought / brain dump (no clear category) | Daily Brain Dump | `BuildSafe IQ/Operations/Daily Notes/YYYY-MM-DD — Brain Dump.md` | ✅ Auto-write |

---

## memory.md Entry Format (for auto-writes)

```
### YYYY-MM-DD HH:MM — [Category] — [Title]
**Type:** Decision | Lesson | Pattern | Risk | Insight
**Context:** One sentence on what triggered this entry.
**Entry:** The actual content.
**Linked files:** (if applicable)
---
```

## Task File Format (for auto-writes)

```
# TASK — [Title]
**Created:** YYYY-MM-DD
**Status:** Open
**Priority:** High / Medium / Low
**Due:** (if mentioned)
**Context:** (source entry summary)

## Action Items
- [ ] ...
```

---

## What This Skill Does NOT Do
- Modify existing files outside the write zones
- Delete content from `Quick Capture.md` (archive only)
- Route to `BuildSafe IQ/Legal/`, `BuildSafe IQ/Finance/`, or `BuildSafe IQ/HR & Team/` without explicit instruction
- Make judgment calls on ambiguous entries — ask Aaron when unclear
