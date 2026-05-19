---
title: Wiki Schema — Operating Rules
type: meta
last_updated: 2026-05-19
---

# BuildSafe IQ Knowledge Base — Schema

The wiki is a persistent, interlinked collection of markdown pages that sits between Aaron and his raw sources. The LLM writes and maintains it. Aaron reads it. Raw sources in `Research_Base/` are never modified.

---

## Directory Structure

```
BuildSafe IQ/Knowledge Base/
├── _schema.md          ← This file. How the wiki works.
├── index.md            ← Master catalog. Read this first on every query.
├── log.md              ← Append-only operation log.
├── concepts/           ← Domain knowledge: frameworks, terms, mechanics
├── entities/
│   ├── competitors/    ← One page per competitor
│   ├── carriers/       ← Carriers, MGAs, wholesale brokers
│   └── partners/       ← Investors, JV partners, advisors
├── sources/            ← One summary page per major source ingested
└── analyses/           ← Synthesized outputs from query sessions
```

Raw sources live in:
- `Research_Base/Trade-Intelligence/` — trade benchmarks, coverage matrices, red flags
- `Research_Base/Project_Oracle_Feeds/` — market intel feed
- `_OS/Knowledge Base/` — reference library (PDFs, legal references)

---

## Page Format

Every wiki page uses this frontmatter:

```yaml
---
title: [Page Title]
type: concept | entity | source | analysis
tags: [tag1, tag2]
sources: [raw source filenames this page draws from]
last_updated: YYYY-MM-DD
---
```

Then: Summary (2-4 sentences), structured sections, and a `## Cross-references` section at the end linking to related wiki pages with `[[page-name]]` syntax.

---

## Operations

### Ingest (adding a new source)
When Aaron adds a source to Research_Base or _inbox:
1. Read the source
2. Write a summary page in `sources/`
3. Update `index.md` with the new source page
4. Scan existing concept and entity pages — update any that this source extends, contradicts, or strengthens
5. If the source introduces a new concept or entity worth a dedicated page, create it
6. Append an entry to `log.md`: `## [YYYY-MM-DD] ingest | [Source Title]`

A single source should touch 3–10 wiki pages. If it touches zero, the ingest was incomplete.

### Query (answering a question)
1. Read `index.md` to find relevant pages
2. Read the relevant pages in full
3. Synthesize and answer with page citations using `[[page-name]]`
4. If the answer reveals something worth keeping (analysis, comparison, synthesis), write it to `analyses/` and add to index
5. Append to `log.md`: `## [YYYY-MM-DD] query | [Question summary]`

### Lint (wiki health check)
Run periodically (monthly). Check for:
- Orphan pages (no inbound links from other pages)
- Stale claims (pages not updated after a contradicting source was ingested)
- Missing cross-references (concepts mentioned but not linked)
- Concept gaps (important terms referenced in multiple pages but lacking their own page)
- Data gaps (important questions the wiki cannot answer — potential new sources to find)

Append to `log.md`: `## [YYYY-MM-DD] lint | [Summary of findings]`

---

## Cross-Referencing Rules

- Use `[[filename-without-extension]]` to link to other wiki pages
- Link liberally — the connections between pages are as valuable as the pages themselves
- A `[[link]]` to a page that doesn't exist yet is valid; it marks a gap to fill

---

## What Goes Where

| Content | Location |
|---------|----------|
| How a framework or concept works (EMR, CGL, WIP analysis) | `concepts/` |
| A specific company (competitor, carrier, partner) | `entities/` |
| Summary of a specific source document | `sources/` |
| Synthesized answer to a question or comparison | `analyses/` |
| Raw market intel, oracle feeds, full book notes | `Research_Base/` (read-only) |

---

## Update Triggers

A wiki page should be updated when:
- A new source contradicts or extends a claim on the page
- A competitive entity changes its product or positioning
- A legal case changes how a concept is interpreted
- A market event changes a benchmark or threshold

Always update `last_updated` in frontmatter when editing a page.
