# memory.md — Decisions, Lessons & Patterns
_Append-only. Never delete. Claude writes here via `/log` and `/review`. Aaron writes manually._
_Last entry: 2026-05-05_

---

## Entry Format

```
### YYYY-MM-DD HH:MM — [Category] — [Title]
**Type:** Decision | Lesson | Pattern | Risk | Insight
**Context:** One sentence on what triggered this entry.
**Entry:** The actual content.
**Linked files:** [[relevant note if any]]
---
```

---

## Log

### 2026-04-06 13:00 — System — Second Brain Initialized
**Type:** Decision
**Context:** Aaron decided to build a Claude Code + Obsidian Second Brain to eliminate context re-explanation overhead.
**Entry:** System initialized. soul.md, user.md, memory.md, and startup.md created. Architecture defined: read-only vault folders + controlled write zones. Phase 1 complete. Phase 2 target: `/review` command running daily by end of Week 5.
**Linked files:** [[BuildSafe IQ Second Brain PRD]]
---

### 2026-04-06 20:30 — Strategy — Brokerage May Run Separate from BuildSafe IQ
**Type:** Decision (in progress)
**Context:** Investor feedback — potential investors do not like the brokerage combined with the BuildSafe IQ tech platform.
**Entry:** Brokerage will be a separate entity from BuildSafe IQ Inc. Key facts: (1) Delaware C-Corp is purely the SaaS platform — no brokerage. (2) Wyoming LLC not yet registered — future vehicle for brokerage. (3) Current pitch deck v.3.30.26 presents BuildSafe IQ as AI/tech SaaS only — type no brokerage mention. (4) Investors do not want brokerage combined with the SaaS platform. Brokerage is a parallel business, not a revenue engine of BuildSafe IQ. Legal and entity work still needed: Wyoming LLC registration, NH agency license, E&O coverage.
**Linked files:** [[Pitch Deck — v.3.30.26]], [[Go-to-Market Strategy]]
---

### 2026-04-06 20:45 — Legal — Cap Table Needs to Be Established & Backdated
**Type:** Decision
**Context:** Aaron identifying legal items that need to be completed before fundraising close.
**Entry:** Cap table needs to be formalized and backdated to date of Delaware C-Corp registration. Known allocations: Ev Jordan = 15%. Still TBD: advisor pool size, employee option pool (ESOP) size. IP Assignment agreement is also unsigned (both parties listed as TBD). All of this needs to go through Morse Barnes-Brown & Pendleton before any investor due diligence.
**Linked files:** [[Capital Raising Checklist]], [[4. Brokerage Operations/Legal/]]
---

### 2026-04-06 21:00 — Finance — Financial Model v2 Key Numbers Confirmed
**Type:** Insight
**Context:** Read BSIQ_Financial_RM_v2_2026-03-24.xlsx in full.
**Entry:** Pre-money $10M, post-money $12.5M, investor 20%, Aaron post-seed 68%, Ev 12%. Y2 cash runway is only 8 months — highest operational risk in the model. Grant Robbins listed in pitch deck but model LD-32 says no equity, not on team — discrepancy must be resolved before due diligence. Brokerage revenue = $0 across all 5 years in model, consistent with separate entity decision.
**Linked files:** [[Financial Model Summary — v2 2026-03-24]]
---

### 2026-04-06 21:15 — Legal — Full Legal Checklist Established (19 Items)
**Type:** Decision
**Context:** Aaron asked what was missing for investor due diligence — full legal picture mapped out.
**Entry:** 19 legal items identified across 4 priority tiers. Critical path: (1) investment instrument decision with Hession — SAFE vs. note vs. priced round — this unlocks everything else. (2) Cap table formalized and backdated. (3) IP Assignment executed. (4) Founder vesting schedules for Aaron and Ev. MSA template and data privacy policy needed before first client contract. 409A required before any options can be granted. Deon and Arshdeep contractor agreements need confirmation. Full tracker: `4. Brokerage Operations/Legal/Legal Tracker.md`
**Linked files:** [[Legal Tracker]]
---

### 2026-04-07 — Legal — Brittany Gilchrist Exit Resolved
**Type:** Decision
**Context:** Brittany exited BuildSafe IQ. Written confirmation in hand. Aaron considers resolved.
**Entry:** Brittany is out. Written confirmation of exit exists. Cap table is Aaron 85% / Ev 15% pre-raise. Do not reference any prior cap table showing different numbers — it is stale and superseded. Hession to review written documentation during cap table formalization call as a diligence confirmation step only.
**Linked files:** [[Legal Tracker]]
---

### 2026-04-07 00:15 — Legal — Contractor Agreements Confirmed (Expired Feb 2026)
**Type:** Update
**Context:** Extracted contractor agreements from master folder zip.
**Entry:** Deon Gracias: $375/month contractor agreement, Aug 2025 – Feb 2026, IP assigned to company, confidentiality included. Arshdeep Kaur: $225/month internship offer letter, Aug 2025 – Feb 2026, IP assigned to company, confidentiality included. Both agreements expired ~Feb 2026. Hession needs to confirm whether expired agreements still bind IP already created, and whether renewals are needed if work is ongoing. Legal Tracker item 13 updated from Unknown to Confirmed (with renewal action item).
**Linked files:** [[Legal Tracker]]
---

### 2026-04-07 — Team — Deon Exited, Arshdeep Continuing
**Type:** Update
**Context:** Aaron clarified team status.
**Entry:** Deon Gracias exited — conflict with full-time job. No longer on team. IP built under original agreement should be confirmed as vested in company (ask Hession during cap table call). Arshdeep Kaur continuing on contract until project complete — needs a new agreement drafted. Legal Tracker item 13 updated.
**Linked files:** [[Legal Tracker]]
---

### 2026-04-07 — Legal — Brittany Exit Considered Resolved
**Type:** Update
**Context:** Aaron clarified written confirmation is sufficient — no separate attorney action needed.
**Entry:** Aaron has written confirmation of Brittany's exit and considers the matter resolved. Share the documentation with Hession during cap table formalization (item 2) to confirm it holds in diligence. No standalone call needed for Brittany. Legal Tracker item 0 downgraded to resolved.
**Linked files:** [[Legal Tracker]]
---

### 2026-05-04 — Legal — Brittany Gilchrist — No Claim, No Involvement
**Type:** Decision
**Context:** Aaron confirmed Brittany has no claim on the company and has not been involved in over a year.
**Entry:** Brittany Gilchrist is not a shareholder and has no claim on BuildSafe IQ Inc. Aaron has a text trail confirming she wants nothing from the company. She signed no documents. No formal exit paperwork needed. Cap table is Aaron 85% / Ev 15% pre-raise. Do not reference Brittany in any active legal items, risk flags, or ownership discussions. All prior references in vault updated to reflect this.
**Linked files:** [[Legal Tracker]], [[Cap Table — Pre-Raise (Informal).csv]]
---

### 2026-05-04 — Team — Deon Exited; Arshdeep Month-to-Month
**Type:** Update
**Context:** Aaron clarified current contractor status during routing run.
**Entry:** Deon Gracias is no longer working with BuildSafe IQ — exited due to conflict with full-time job. No active engagement. IP from original agreement should be confirmed as vested in company (Hession). Arshdeep Kaur is continuing on a month-to-month basis — not tied to project completion. Formal contractor renewal agreement still needed.
**Linked files:** [[Legal Tracker]]
---

### 2026-05-05 — BD — John Hession Investor Outreach Status
**Type:** Update
**Context:** Reviewed full John Hession email thread and sent him a comprehensive update per his request.
**Entry:** John is in Colorado until May 10-11 visiting family. Still actively working for BSIQ from the road — made the Leader Bank intro while traveling. Three VC conversations to date: (1) B Capital (Patrick Harmon) — expressed interest, can't lead, connecting to pre-seed funds; (2) Grid Capital (Jackie DiMonte) — paused in late April due to father's health, conversation was positive before that; (3) TipTop VC (Nick) — was evaluating with leads in mind, in follow-up mode. Consonant Ventures (via Keith at CK Team) — deck and pro formas sent April 30, very early. Leader Bank (Summer Hutchison, Vitaliy Schafer, Alex Guinta) — John intro'd May 4, Summer replied same day, call scheduled May 6. Joe Caruso (Bantam Group) — most active referral; had call April 24, Joe working on intros to Josh Kanner (Smartvid.io), Raghi Iyengar (Manufacton), Liberty Mutual Ventures; meetings scheduled later in May. Sent John a fresh standalone email (per his iPad formatting requirement) with: VC firm names, full Referral List status, and his current intro paragraph.
**Linked files:** [[none]]
---

### 2026-04-07 00:30 — Ops — Master Folder Routed to Vault
**Type:** Decision
**Context:** Processed Project Performance Accelerator Initiative master folder (129 files).
**Entry:** Key documents extracted and routed: Contacts.md (6 CFMA contacts) → CRM; Vision/Mission/Values, BuildSafe IQ Story → Brand; Deal Teaser (archived, older raise numbers) → GTM/Archive; Working IR Doc, Beta GC One-Pager → GTM; Service Offerings WIP → Product; Signals for Delays → Knowledge Base; Meeting Notes (Karen 2/5/25, Risk Management Synopsis) → Daily Operations/Meeting Notes. Contractor agreements (Deon/Arshdeep) noted and legal tracker updated. Remaining ~100 files in master folder (PDFs, resumes, older pitch decks, spreadsheets) not yet routed — categorization plan pending.
**Linked files:** [[Legal Tracker]]
---

### 2026-05-05 21:00 — Product — COI Automation Feature Set Added to Roadmap
**Type:** Decision
**Context:** LinkedIn message from a competitor (Cara AI) described four insurance workflow automation features worth building into BuildSafe IQ.
**Entry:** Four features identified for internal build — do not partner or respond to sender. (1) COI Generation: AMS-connected, contract-driven, email delivery, ~30K COIs/yr scale signal. (2) Coverage Comparison & Proposal Generation: side-by-side with citations, branded output. (3) Knowledge Base ("Veteran in a Box"): upload carrier guidelines/SOPs/OSHA data → natural language search — makes 25-yr veteran knowledge accessible on day one. (4) Email AI: forward thread → get ACORD/COI/coverage summary back, zero new tab/login. Build order: Knowledge Base first (feeds all others) → Email AI → COI Generation → Coverage Comparison. Stack: AWS Textract + Claude Vision (per OCR report v1.1) + Google Apps Script email layer. Task created for tomorrow: open VS Code, begin Knowledge Base architecture.
**Linked files:** [[Feature Spec — COI Automation & Insurance AI Layer]], [[TASK — Begin COI Automation Build — 2026-05-06]]
---
