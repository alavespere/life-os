# memory.md — Decisions, Lessons & Patterns
_Append-only. Never delete. Claude writes here via `/log` and `/review`. Aaron writes manually._
_Last entry: 2026-04-06_

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
**Entry:** Brokerage will be a separate entity from BuildSafe IQ Inc. Key facts: (1) Delaware C-Corp is purely the SaaS platform — no brokerage. (2) Wyoming LLC not yet registered — future vehicle for brokerage. (3) Current pitch deck v.3.30.26 presents BuildSafe IQ as AI/tech SaaS only — no brokerage mention. (4) Investors do not want brokerage combined with the SaaS platform. Brokerage is a parallel business, not a revenue engine of BuildSafe IQ. Legal and entity work still needed: Wyoming LLC registration, NH agency license, E&O coverage.
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

### 2026-05-08 — BD — Hubble Pre-Seed Investor List Processed
**Type:** Update
**Context:** Mobile Drop processed from 2026-05-07 session — 36 pre-seed investors sourced from Hubble platform.
**Entry:** 36 investors logged. Check sizes $25K–$5M. None contacted yet. 3 flagged as NEW to platform: Alexi Sevastopoulos (Santa Cruz Ventures), Brent Fulfer (TB Ventures), Tobias Bauer (TB Ventures). Next steps: run Investor Intelligence batch research tool on all 36 → tier by relevance → draft personalized cold outreach starting with the 3 new ones → track in Capital_Raising_Contacts.xlsx. Fold into 5 daily outreach touches. Saved to: `BuildSafe IQ/Operations/Daily Notes/2026-05-08 — Hubble Pre-Seed Investor List.md`
**Linked files:** [[2026-05-08 — Hubble Pre-Seed Investor List]]
---

### 2026-05-08 — Knowledge Base — Holland Construction Law Book Fully Processed
**Type:** Decision
**Context:** Aaron photographed all ~175 pages of "Construction Law & Risk Management Case Notes and Articles" (J. Kent Holland Jr., Arch Insurance Group) across 4 sessions May 6-7, 2026.
**Entry:** Full 27-chapter book processed and saved to vault. Covers: Differing Site Conditions, Contractor Licensing, Disputes, Scope, Design-Build, Professional Liability, Environmental, Bidding, Changes, Pay When Paid/Pay If Paid, Consequential Damages, Joint Ventures, Construction Defects, Delay, Insurance (CGL coverage analysis, exclusions, 11 key cases), Limitation of Liability, Scheduling (Measured Mile, Constructive Acceleration, CPM pitfalls), Site Safety (7-factor test, OSHA/A/E, 9 key cases), Statute of Limitations, Statute of Repose, Waiver of Subrogation, Substantial Completion, Surety (Miller Act, SDI vs. bonds), Debarment, Termination, Warranties. Output includes: full chapter notes, 35+ key case citations, Risk Scoring Model inputs table (25 factors), CGL/E&O/Surety underwriting checklists, 15-item content pipeline. Saved to: `BuildSafe IQ/Marketing & Content/Research_Base/2026-05-08 — Construction Law & Risk Management — Holland — Full Notes.md`
**Linked files:** [[2026-05-08 — Construction Law & Risk Management — Holland — Full Notes]]
---

### 2026-05-08 — Market Intel — Burns & Wilcox P&C Q2 2026
**Type:** Insight
**Context:** Mobile Drop processed — Burns & Wilcox P&C Report Q2 2026 Outlook reviewed on mobile.
**Entry:** Key signals: (1) B&W explicitly validating AI/API platforms for binding authority — BSIQ pitch aligns directly. (2) Contractor GL softening — submission quality is the differentiator. (3) SAM coverage demand spiking for GCs at schools/healthcare/municipalities — new line to pursue via B&W. (4) CPL soft with new entrants — good placement opportunity. (5) Social inflation dominant theme across all lines — plays into BSIQ risk scoring. Key contact: Chris Siegel, VP/MD Orlando — construction, property, environmental specialist. Saved to: `BuildSafe IQ/Marketing & Content/Research_Base/2026-05-07 — Burns & Wilcox P&C Q2 2026 Intel.md`
**Linked files:** [[2026-05-07 — Burns & Wilcox P&C Q2 2026 Intel]]
---

### 2026-05-07 — System — Mobile Inbox + Connect to Brain Protocol Established
**Type:** Decision
**Context:** Aaron works across desktop (Claude Code) and mobile (claude.ai) — mobile sessions were not persisting to the vault, causing lost work on investor lists, book processing, and other tasks.
**Entry:** Mobile workflow system established. Three components: (1) `_OS/AI Skills/connect-to-brain.md` — a full context prompt Aaron pastes at the start of any mobile Claude session, loading all business context so mobile Claude can process intelligently. (2) `_Mobile Inbox` folder created in Google Drive (ID: 1Xtv9uG4kXylgnawFxwIlfC--rr5VjZ-R) — landing zone for mobile session outputs. (3) Gmail bridge — at end of any mobile session, Claude generates a structured Mobile Drop Note and Aaron emails it to aaron@buildsafeiq.com with subject `[Mobile Drop] - [Topic]`. Desktop Claude picks these up via Gmail MCP and routes them into the vault. Protocol: search Gmail for `[Mobile Drop]` subject at start of any session where mobile processing is expected.
**Linked files:** [[connect-to-brain.md]], [[_Mobile Inbox (Drive)]]
---

### 2026-05-05 — BD — John Hession Investor Outreach Status
**Type:** Update
**Context:** Reviewed full John Hession email thread and sent him a comprehensive update per his request.
**Entry:** John is in Colorado until May 10-11 visiting family. Still actively working for BSIQ from the road — made the Leader Bank intro while traveling. Three VC conversations to date: (1) B Capital (Patrick Harmon) — expressed interest, can't lead, connecting to pre-seed funds; (2) Grid Capital (Jackie DiMonte) — paused in late April due to father's health, conversation was positive before that; (3) TipTop VC (Nick) — was evaluating with leads in mind, in follow-up mode. Consonant Ventures (via Keith at CK Team) — deck and pro formas sent April 30, very early. Leader Bank (Summer Hutchison, Vitaliy Schafer, Alex Guinta) — John intro'd May 4, Summer replied same day, call scheduled May 6. Joe Caruso (Bantam Group) — most active referral; had call April 24, Joe working on intros to Josh Kanner (Smartvid.io), Raghi Iyengar (Manufacton), Liberty Mutual Ventures; meetings scheduled later in May. Sent John a fresh standalone email (per his iPad formatting requirement) with: VC firm names, full Referral List status, and his current intro paragraph.
**Linked files:** [[none]]
---

### 2026-05-14 — Strategy — Positioning Pivot: AI Platform → Tech-Enabled Service Provider
**Type:** Decision
**Context:** Josh Kanner (Oracle/Newmetrix) challenged the pitch deck and pushed for a fundamental reframe.
**Entry:** Decided to reposition BuildSafe IQ from "AI platform" to "tech-enabled construction risk advisory service." AI is the engine, not the product. Service delivery (QBRs, certified risk professionals) moves from Addendum A to the core of the pitch. The trigger: Josh built Newmetrix (sold to Oracle 2022) — same space — and said the current framing sounds like a copied platform. The tradeoff: the service model is less sexy to SaaS investors but more defensible, stickier, and validated by General Catalyst's $13.8M seed in Zero RFI (same thesis, different buyer). New one-liner: "BuildSafe IQ is a tech-enabled construction risk advisory service — we use AI to score subcontractor and project risk across seven validated signals, then deliver the insight through certified risk professionals so GCs can act before the loss happens."
**Linked files:** [[2026-05-14 — Josh Kanner — Pitch Deck Revision Notes]]
---

### 2026-05-14 — BD — Josh Kanner Relationship Status
**Type:** Update
**Context:** First meeting with Josh Kanner today, intro via Joe Caruso (Bantam Group).
**Entry:** Josh Kanner is Senior Director of Product & Strategy at Oracle Construction & Engineering. Previously co-founded Vela Systems (sold to Autodesk 2012) and Newmetrix (AI risk intel, sold to Oracle 2022). One of the most credible domain experts Aaron could meet. He challenged the pitch on four fronts: TAM sourcing, boiling the ocean, platform vs. service positioning, and no AI/data science depth. Joe Caruso agreed with all of it. Josh agreed to continue the conversation after the pitch is refined. Follow-up email sent same day — acknowledged feedback, attached current deck + TAM report, asked for 20-minute reconnect once refined. Goal: make Josh an advisor, not push for investment. Advisor ask is reserved for the follow-up session, not email. Note: Oracle is listed as an M&A acquirer in the deck — Josh is aware of this context.
**Linked files:** [[2026-05-14 — Josh Kanner — Pitch Deck Revision Notes]], [[Joe Caruso — Bantam Group]]
---

### 2026-05-14 — Market Intel — Competitive Landscape Updates
**Type:** Insight
**Context:** Josh Kanner and research surfaced three competitive developments that need to be addressed in the pitch deck.
**Entry:** (1) Procore acquired Datagrid (January 2026) — workflow AI for submittal automation, RFI drafting, and data connectivity. NOT risk intelligence. Their buyer is the project manager. BSIQ's buyer is the risk manager, CFO, and insurance team. Different problem, different stakeholder. (2) Document Crunch — Josh called it a risk management platform. Correct reframe: Document Crunch analyzes contract language and flags risky clauses. BSIQ scores whether the contractor can actually perform. Contract document review vs. predictive risk intelligence. Trimble acquisition validates the market. (3) Zero RFI — $13.8M seed from General Catalyst (March 2026). AI-enabled owner's rep firm. Serves building owners and developers, not GCs. Same tech-enabled service thesis as BSIQ's pivot — different buyer. General Catalyst's investment is a validation signal for the model. All three updates to be incorporated into Slide 8 (competitive landscape) and Slide 15 (Why Now) in pitch deck v5.
**Linked files:** [[2026-05-14 — Josh Kanner — Pitch Deck Revision Notes]]
---

### 2026-04-07 00:30 — Ops — Master Folder Routed to Vault
**Type:** Decision
**Context:** Processed Project Performance Accelerator Initiative master folder (129 files).
**Entry:** Key documents extracted and routed: Contacts.md (6 CFMA contacts) → CRM; Vision/Mission/Values, BuildSafe IQ Story → Brand; Deal Teaser (archived, older raise numbers) → GTM/Archive; Working IR Doc, Beta GC One-Pager → GTM; Service Offerings WIP → Product; Signals for Delays → Knowledge Base; Meeting Notes (Karen 2/5/25, Risk Management Synopsis) → Daily Operations/Meeting Notes. Contractor agreements (Deon/Arshdeep) noted and legal tracker updated. Remaining ~100 files in master folder (PDFs, resumes, older pitch decks, spreadsheets) not yet routed — categorization plan pending.
**Linked files:** [[Legal Tracker]]
---
