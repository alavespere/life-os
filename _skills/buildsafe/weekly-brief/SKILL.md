---
name: weekly-brief
version: 1.0
description: Generates the weekly Construction Risk Intelligence Brief from Project Oracle feeds and Research Base. Structures output as the five-section newsletter format — Signal, Regional Pulse, Legal Watch, Data Point, Framework. Writes to newsletter draft folder.
trigger: /weekly-brief
compatibility: claude-code, claude.ai
input: New Project Oracle feeds from the past 7 days + Research Base index
output: Weekly brief draft written to BuildSafe IQ/Marketing & Content/Content/Pipeline/
---

## Instructions

You are generating Aaron's weekly *Construction Risk Intelligence Brief* — the newsletter that goes out Monday morning to Beehiiv subscribers.

**Input:** `BuildSafe IQ/Marketing & Content/Research_Base/Project_Oracle_Feeds/` (last 7 days)
**Target State:** Newsletter draft at `BuildSafe IQ/Marketing & Content/Content/Pipeline/Newsletter-Draft-YYYY-MM-DD.md`

---

### Step 1 — Read This Week's Oracle Feeds

Read all files in `BuildSafe IQ/Marketing & Content/Research_Base/Project_Oracle_Feeds/` dated within the last 7 days.

If fewer than 3 articles exist: note the gap and continue with what's available.

Also read `BuildSafe IQ/Marketing & Content/Research_Base/index.md` for the Data Points Bank.

---

### Step 2 — Select the Best Content for Each Section

**The Signal** — pick the single most important market development of the week. Ask: what would a GC or subcontractor most need to know? What has the biggest risk implication?

**The Regional Pulse** — pick the most notable regional development. Prioritize the markets where construction activity is highest: DFW, Miami, Phoenix, NYC, Boston.

**The Legal Watch** — pick the most significant case law, regulatory development, or compliance change. Must be factual and sourced.

**The Data Point** — pick the single most surprising or counterintuitive statistic from the week's feeds. Must have a verifiable source and date.

**The Framework** — pick a practical risk management concept from the week's research that readers can apply immediately.

---

### Step 3 — Draft Each Section

Follow Aaron's brand voice strictly:
- Direct, authoritative, data-grounded
- Short declarative sentences for emphasis
- Always the non-obvious angle
- Never: "I'm excited to share", "it's worth noting", "game-changer"
- 8th-grade reading level
- Always cite sources

**Section 1: The Signal** (150 words max)
*One major market development and its risk implication.*

**Section 2: The Regional Pulse** (100 words max)
*One regional market update — what's happening and why it matters for risk.*

**Section 3: The Legal Watch** (100 words max)
*One case law or regulatory development — what changed and what contractors need to know.*

**Section 4: The Data Point** (50 words max + source)
*One surprising statistic. Format: [Stat]. [Source, Date]. [One-sentence implication.]*

**Section 5: The Framework** (200 words max)
*One practical risk management tip. Make it specific and actionable — not generic advice.*

---

### Step 4 — Write Newsletter Draft

```markdown
# Construction Risk Intelligence Brief — [Week of YYYY-MM-DD]
_Draft for Beehiiv — Review before sending_

---

## The Signal
[150 words]

## The Regional Pulse
[100 words]

## The Legal Watch
[100 words]

## The Data Point
[50 words + source citation]

## The Framework
[200 words]

---

## What I'm Watching
_3 links to the most important articles this week:_
1. [Title] — [Source] — [URL]
2. [Title] — [Source] — [URL]
3. [Title] — [Source] — [URL]

---
_Sources used: [list all Oracle feed files referenced]_
_Word count: [total]_
_Status: DRAFT — needs Aaron review_
```

---

### Stop Conditions
- Never fabricate statistics or quotes — only use data from Oracle feeds or verified sources
- If fewer than 2 verified sources exist for a section, write what you have and flag: `[NEEDS MORE RESEARCH]`
- Do not publish — this is a draft for Aaron's review only
- Word counts are maximums — concise is better

### Checkpoint Output
`✅ /weekly-brief complete. Draft written to Pipeline/Newsletter-Draft-[date].md. [N] Oracle feeds used.`
