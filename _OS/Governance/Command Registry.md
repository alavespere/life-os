# Command Registry
_Source of truth for all Claude Code commands in this vault._
_Last updated: 2026-05-18_

---

## Core Commands

| Command | Skill Path | Purpose | Status |
|---------|-----------|---------|--------|
| Session startup | _(auto — CLAUDE.md + soul.md)_ | Load brain files, check daily note, run `/today` if none exists | ✅ Live |
| `/log [type]: [text]` | _(inline)_ | Manually append entry to memory.md | ✅ Live |

---

## Core Skills

| Command | Skill Path | Purpose | Status |
|---------|-----------|---------|--------|
| `/today` | `_skills/core/today/SKILL.md` | Morning brief + create today's Daily Note | ✅ Live |
| `/review` | `_skills/core/review/SKILL.md` | End-of-session digest → memory.md + Agent_Logs/ | ✅ Live |
| `/weekly-review` | `_skills/core/weekly-review/SKILL.md` | Friday review → _Personal/Goals/Reviews/ | ✅ Live |

---

## Brokerage Skills

| Command | Skill Path | Purpose | Status |
|---------|-----------|---------|--------|
| `/onboard-client [name]` | `_skills/brokerage/onboard-client/SKILL.md` | Client intake → ACORD mapping → Active_Submissions/ | ✅ Live |
| `/analyze-loss-runs [name]` | `_skills/brokerage/analyze-loss-runs/SKILL.md` | 5-year loss metrics + underwriting narrative | ✅ Live |
| `/analyze-coi [name]` | `_skills/brokerage/coi-analyzer/SKILL.md` | COI compliance check → coverage gaps + verdict | ✅ Live |

---

## BuildSafe IQ Skills

| Command | Skill Path | Purpose | Status |
|---------|-----------|---------|--------|
| `/score-risk [project]` | `_skills/buildsafe/risk-scorer/SKILL.md` | 5-dimension project risk score + flag list | ✅ Live |
| `/route-inbox` | `_skills/buildsafe/document-router/SKILL.md` | Auto-route _inbox/ files to correct vault locations | ✅ Live |
| `/weekly-brief` | `_skills/buildsafe/weekly-brief/SKILL.md` | Newsletter draft from Oracle feeds → Pipeline/ | ✅ Live |
| `/email [type or context]` | `_skills/buildsafe/email/SKILL.md` | Draft any email in Aaron's voice — paste thread, describe situation, or name recipient | ✅ Live |

---

## Agent Personas (separate from skills — activate by phrase)

These live in `_OS/AI Skills/` and are activated by telling Claude "Act as my [role]":

| Activation Phrase | File | Role |
|------------------|------|------|
| "Act as my BDR" | `Agent — BDR.md` | Outbound prospecting |
| "Act as my CRO" | `Agent — CRO.md` | Revenue strategy |
| "Act as my CFO" | `Agent — CFO.md` | Financial modeling |
| "Act as my CMO" | `Agent — CMO.md` | Marketing strategy |
| "Act as my COO" | `Agent — COO.md` | Operations |
| "Act as my legal counsel" | `Agent — Legal Counsel.md` | Legal analysis |
| "Act as my CBO" | `Agent — CBO (Brokerage).md` | Brokerage strategy |

---

## `/log` Usage

```
/log Decision: [text]
/log Lesson: [text]
/log Pattern: [text]
/log Risk: [text]
/log Insight: [text]
```

Claude formats input into the memory.md schema, shows you the entry, and appends on confirmation.

---

## Planned / Future

| Command | Purpose | Status |
|---------|---------|--------|
| `/ingest [topic]` | Add new Oracle feeds to Research_Base/ | 🔲 Requires Feedly + Make.com running |
| `/status` | Full business pulse — CRM, brokerage, pipeline, content | 🔲 Requires CRM populated |
| `/recall [topic]` | Semantic search across memory archives | 🔲 Future |

---

## How to Execute a Command

1. Type the command in Claude Code terminal
2. Claude reads the SKILL.md from `_skills/[category]/[skill]/`
3. Claude follows the skill protocol exactly — no deviation
4. All writes are within the declared write zones for that skill

**Note:** All skills live in `_skills/`. The `_OS/AI Skills/Skill — *.md` files are legacy references and are superseded by `_skills/`.
