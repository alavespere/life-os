# Skill Library — Index
_All skills in this vault. Loaded via `.claude/settings.json` → `skillsPath: ./_skills`_
_Last updated: 2026-04-27_

---

## Core Skills (claude-code)

| Skill | Trigger | Description |
|-------|---------|-------------|
| `review` | `/review` | End-of-session digest → memory.md + Agent_Logs/ |
| `today` | `/today` | Morning brief + create today's Daily Note |
| `weekly-review` | `/weekly-review` | Friday review across all contexts → _Personal/Goals/Reviews/ |

---

## Brokerage Skills (claude-code)

| Skill | Trigger | Description |
|-------|---------|-------------|
| `onboard-client` | `/onboard-client [name]` | Client intake → ACORD mapping → Active_Submissions/ |
| `analyze-loss-runs` | `/analyze-loss-runs [name]` | 5-year loss metrics + underwriting narrative |
| `coi-analyzer` | `/analyze-coi [name]` | COI compliance check → coverage gaps + verdict |

---

## BuildSafe IQ Skills (claude-code + claude.ai)

| Skill | Trigger | Description |
|-------|---------|-------------|
| `risk-scorer` | `/score-risk [project]` | 5-dimension project risk score + flag list |
| `document-router` | `/route-inbox` | Auto-route _inbox/ files to correct vault locations |
| `weekly-brief` | `/weekly-brief` | Newsletter draft from Oracle feeds → Pipeline/ |
| `email` | `/email [type] [name]` | Draft emails in Aaron's voice — 5 types: investor-cold, investor-follow, investor-bump, partner-intro, client-cold |

---

## Compatibility Tiers

| Tier | Where It Runs | Skills |
|------|-------------|--------|
| **Tier 1 — Universal** | claude-code + claude.ai | `coi-analyzer`, `risk-scorer`, `weekly-brief`, `email` |
| **Tier 2 — Claude Code only** | Requires VS Code + vault | `review`, `today`, `weekly-review`, `onboard-client`, `analyze-loss-runs`, `document-router` |
| **Tier 3 — Claude.ai + MCP** | Requires Drive/Gmail connectors | *(planned: email-follow-up-tracker, drive-report-pusher)* |

---

## Agent Personas (separate from skills — activate by phrase)

These live in `_OS/AI Skills/` and are activated by telling Claude "Act as my [role]":

| Phrase | File | Role |
|--------|------|------|
| "Act as my BDR" | `Agent — BDR.md` | Outbound prospecting |
| "Act as my CRO" | `Agent — CRO.md` | Revenue strategy |
| "Act as my CFO" | `Agent — CFO.md` | Financial modeling |
| "Act as my CMO" | `Agent — CMO.md` | Marketing strategy |
| "Act as my COO" | `Agent — COO.md` | Operations |
| "Act as my legal counsel" | `Agent — Legal Counsel.md` | Legal analysis |
| "Act as my CBO" | `Agent — CBO (Brokerage).md` | Brokerage strategy |

---

## Community Skills (installed at `~/.claude/skills/`)

| Skill | Repository | Purpose |
|-------|-----------|---------|
| `prompt-master` | `nidhinjs/prompt-master` | Optimizes prompts for any AI tool |

**To install additional community skills:**
```
npx skills add coreyhaines31/marketingskills
npx skills add pbakaus/impeccable
npx skills add anthropics/skills
```
