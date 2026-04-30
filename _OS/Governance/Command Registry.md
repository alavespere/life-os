# Command Registry
_Source of truth for all Claude Code commands in this vault._
_Last updated: 2026-04-15_

---

## Phase 1 — Live ✅

| Command | Skill File | Purpose | Status |
|---------|-----------|---------|--------|
| Session startup | _(auto — CLAUDE.md)_ | Load brain files on session open | ✅ Live |
| `/log [type]: [text]` | _(inline)_ | Manually append entry to memory.md | ✅ Live |

---

## Phase 2 — Live ✅ (built 2026-04-15)

| Command | Skill File | Purpose | Status |
|---------|-----------|---------|--------|
| `/today` | `Skill — Today.md` | Morning daily brief + create today's Daily Note | ✅ Built |
| `/review` | `Skill — Review.md` | End-of-session digest → memory.md + Agent_Logs/ | ✅ Built |
| `/weekly-review` | `Skill — Weekly Review.md` | Friday review → _Personal/Goals/Reviews/ | ✅ Built |

---

## Phase 3 — Live ✅ (built 2026-04-15)

| Command | Skill File | Purpose | Status |
|---------|-----------|---------|--------|
| `/onboard-client [name]` | `Skill — Onboard Client.md` | Brokerage intake → Active_Submissions/ | ✅ Built |
| `/analyze-loss-runs [name]` | `Skill — Loss Run Analysis.md` | Loss run metrics + underwriting narrative | ✅ Built |

---

## Phase 4 — Pending Setup (infrastructure required)

| Command | Purpose | Dependency |
|---------|---------|-----------|
| `/ingest [topic or "latest"]` | Add new Oracle feeds to Research_Base/index.md | Feedly + Make.com running |
| `/status` | Full business pulse — CRM, brokerage, pipeline, content | Needs content pipeline + CRM populated |

---

## Future

| Command | Purpose | Status |
|---------|---------|--------|
| `/recall [topic]` | Semantic search across memory archives | 🔲 Future |
| `/emerge` | Surface non-obvious patterns across vault | 🔲 Future |

---

## `/log` Usage

```
/log Decision: [text]
/log Lesson: [text]
/log Pattern: [text]
/log Risk: [text]
/log Insight: [text]
```

Claude will format your input into the memory.md schema, show you the entry, and append on confirmation.

---

## Agent Skills (Separate from Commands)

Activate by telling Claude to "Act as my [role]":

| Activation Phrase | File | Role |
|------------------|------|------|
| "Act as my BDR" | `Agent — BDR.md` | Outbound sales / prospecting |
| "Act as my CRO" | `Agent — CRO.md` | Revenue strategy |
| "Act as my CFO" | `Agent — CFO.md` | Financial modeling and analysis |
| "Act as my CMO" | `Agent — CMO.md` | Marketing and brand strategy |
| "Act as my COO" | `Agent — COO.md` | Operations and execution |
| "Act as my legal counsel" | `Agent — Legal Counsel.md` | Legal analysis and review |
| "Act as my CBO" | `Agent — CBO (Brokerage).md` | Brokerage strategy |

---

## How to Execute a Command

1. In your Claude Code terminal session, type the command
2. Claude reads the relevant Skill file from `_OS/AI Skills/`
3. Claude follows the skill protocol exactly — no deviation
4. All writes are within the declared write zones for that skill

**Note:** Skill files use prompt-master's ReAct + Stop Conditions architecture. Every skill has explicit starting state, target state, allowed actions, stop conditions, and checkpoint output.
