# PRD — BuildSafe IQ Second Brain
_Claude Code + Obsidian Integration_
**Owner:** Aaron | **Company:** BuildSafe IQ Inc.
**Version:** 1.0 | **Created:** 2026-04-02 | **Status:** Phase 1 Complete

---

See full PRD in source document. This file is the vault-resident copy for reference during implementation.

## Phase Status

| Phase | Focus | Built | Status |
|-------|-------|-------|--------|
| Phase 1 | Memory layer foundation | Week 1–2 | ✅ Complete |
| Phase 2 | Daily logging + lesson extraction | 2026-04-15 | ✅ Complete |
| Phase 3 | Brokerage engine + command library | 2026-04-15 | ✅ Complete |
| Phase 4 | Project Oracle (Feedly + Make.com automation) | Spec built — setup pending | 🔧 In Progress |
| Phase 5 | `/recall` + semantic search | TBD | 🔲 Future |
| Phase 6 | `/emerge` pattern intelligence | TBD | 🔲 Future |

## Phase 1 Acceptance Criteria
- [ ] Claude opens a fresh session and responds "Context loaded. Ready." without being told anything
- [ ] Claude correctly identifies Aaron's company, team members, and current bottlenecks when asked
- [ ] Claude refuses to write to any file outside the designated write zones
- [ ] `memory.md` has at least 7 entries (one per day, Week 1)

## Phase 2 Acceptance Criteria
- [ ] `/review` runs end-to-end in under 3 minutes
- [ ] At least 80% of extracted entries are genuinely useful (Aaron's judgment)
- [ ] Zero entries appended without Aaron's approval
- [ ] `memory.md` grows by 3–7 entries per day of use

## Phase 3 Acceptance Criteria
- [ ] `/today` produces a complete daily brief in under 60 seconds with zero manual input
- [ ] `/emerge` surfaces at least one non-obvious pattern per week
- [ ] `/skill [name]` produces output consistent with Aaron's voice without session context
- [ ] Updating `user.md` once propagates correctly to all Skills
- [ ] `memory.md` is legible as a standalone decision log
