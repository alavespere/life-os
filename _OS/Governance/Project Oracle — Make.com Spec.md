# Project Oracle — Make.com Automation Spec
_Two trigger paths: Feedly (primary) + Gmail/Google Alerts (secondary)_
_Build this in Make.com (formerly Integromat). ~45 min setup._

---

## Pipeline Overview

**Path A — Feedly (Categories 1–6 and 9: industry RSS feeds)**
```
Feedly Board (Oracle — Curated)
    ↓  [trigger: new saved article]
Perplexity API
    ↓  [synthesize + identify risk implication]
GitHub API
    ↓  [create .md file in vault repo]
Obsidian Git Plugin
    ↓  [auto-pull on next sync]
Research_Base/Project_Oracle_Feeds/
```

**Path B — Gmail (Categories 7–8: Google Alerts for regional markets)**
```
Google Alerts (email delivery → aaron@buildsafeiq.com)
    ↓  [Gmail label filter: "Oracle — Google Alerts"]
Gmail Trigger (Make.com watches label)
    ↓  [extract alert subject + body + links]
Perplexity API
    ↓  [synthesize + identify risk implication]
GitHub API
    ↓  [create .md file in vault repo]
Obsidian Git Plugin
    ↓  [auto-pull on next sync]
Research_Base/Project_Oracle_Feeds/
```

> **Why two paths?** Google Alerts no longer offers RSS feeds on most accounts. Feedly handles structured industry RSS (trade publications, gov data). Gmail handles Google Alerts keyword monitoring for regional market intel. Both feed the same downstream pipeline.

---

## Prerequisites

Before building:
- [ ] Feedly Enterprise account with API access enabled
- [ ] Perplexity Pro account (API key from `perplexity.ai/settings/api`)
- [ ] Private GitHub repo connected to your Obsidian vault (via Obsidian Git plugin)
- [ ] Make.com account (free tier is sufficient to start)
- [ ] Google Alerts configured for regional keywords, set to email delivery → `aaron@buildsafeiq.com`
- [ ] Gmail filter created: `from:googlealerts-noreply@google.com` → apply label `Oracle — Google Alerts`

**Set up Gmail filter:**
1. In Gmail → Settings → Filters and Blocked Addresses → Create new filter
2. From: `googlealerts-noreply@google.com`
3. Apply label: `Oracle — Google Alerts` (create the label first if it doesn't exist)
4. Skip inbox: optional (recommended to keep inbox clean)

---

## Scenario: Oracle Feed Processor

**Scenario name:** `Oracle — Feedly to Obsidian`

---

### Module 1: Trigger — Feedly Watch Board

**App:** Feedly
**Trigger:** Watch for New Articles Saved to Board
**Board:** `Oracle — Curated`
**Poll interval:** Every 15 minutes

**Output variables:**
- `title` — article title
- `url` — article URL
- `source` — publication name
- `published_date` — date published
- `summary` — Feedly's extracted summary (if available)

---

### Module 2: Action — Perplexity API Synthesis

**App:** HTTP (Make.com built-in)
**Method:** POST
**URL:** `https://api.perplexity.ai/chat/completions`

**Headers:**
```
Authorization: Bearer {{PERPLEXITY_API_KEY}}
Content-Type: application/json
```

**Body:**
```json
{
  "model": "sonar-pro",
  "messages": [
    {
      "role": "system",
      "content": "You are a senior construction risk analyst. You synthesize industry intelligence for a commercial insurance brokerage founder and construction risk SME building a personal brand. Be direct. No filler. Cite sources precisely."
    },
    {
      "role": "user",
      "content": "Synthesize this article in exactly 3 paragraphs:\n\n1. What happened / what the article says (key data points only, cite the source)\n2. Why it matters for commercial construction risk management specifically\n3. The non-obvious implication — what most people in the industry will miss about this\n\nArticle URL: {{url}}\nArticle title: {{title}}\nSource: {{source}}"
    }
  ],
  "max_tokens": 600,
  "temperature": 0.3
}
```

**Output:** Parse `choices[0].message.content` → store as `synthesis`

---

### Module 3: Action — Generate Filename

**App:** Tools (Make.com built-in — Set Variable)

**Logic:**
```
filename = {{formatDate(published_date, "YYYY-MM-DD")}} — {{replace(title, " ", "-")}} — Oracle.md
```

Truncate title to 60 characters max. Remove special characters.

---

### Module 4: Action — Build Markdown File Content

**App:** Tools (Make.com built-in — Set Variable)

**Content template:**
```
---
title: {{title}}
source: {{source}}
url: {{url}}
date: {{formatDate(published_date, "YYYY-MM-DD")}}
type: Oracle Feed
pillar: [assign manually in Obsidian]
tags: [construction-risk, oracle]
---

# {{title}}

**Source:** [{{source}}]({{url}})
**Date:** {{formatDate(published_date, "YYYY-MM-DD")}}

---

## Synthesis

{{synthesis}}

---

## Raw Summary
{{summary}}

---

*Processed by Project Oracle — Make.com automation*
```

---

### Module 5: Action — Create File in GitHub

**App:** GitHub
**Action:** Create a File

**Repository:** `[your-vault-repo-name]`
**Branch:** `main`
**File path:** `BuildSafe IQ/Marketing & Content/Research_Base/Project_Oracle_Feeds/{{filename}}`
**Content:** `{{markdown_content}}` (Base64 encoded — Make.com handles this automatically)
**Commit message:** `Oracle: {{title}}`

---

### Module 6: Obsidian Git Auto-Pull

The Obsidian Git plugin (set to auto-pull every 1 minute) will pick up the new file on the next sync cycle. No additional configuration needed once the plugin is installed.

---

---

## Scenario B: Oracle Gmail Processor (Google Alerts)

**Scenario name:** `Oracle — Google Alerts to Obsidian`

This scenario watches for Google Alert emails and processes them through the same Perplexity → GitHub pipeline.

---

### Module 1B: Trigger — Gmail Watch Label

**App:** Gmail
**Trigger:** Watch Emails in Label
**Label:** `Oracle — Google Alerts`
**Poll interval:** Every 15 minutes

**Output variables:**
- `subject` — alert subject (contains keyword + top result headline)
- `body_text` — plain text body of the alert email
- `date` — email received date

---

### Module 2B: Action — Parse Alert Content

**App:** Tools (Make.com built-in — Text Parser)

Google Alert emails contain multiple links. Extract the top result:

**Regex to extract first article title and URL from body:**
```
Pattern 1 (title): (?<=\n)[A-Z][^\n]{20,120}(?=\n)
Pattern 2 (url): https?://[^\s"]+(?=\s)
```

Set variables:
- `alert_keyword` — extract from subject (format: "Google Alert - [keyword]")
- `article_title` — first extracted title from body
- `article_url` — first extracted URL from body
- `alert_date` — `{{formatDate(date, "YYYY-MM-DD")}}`

> **Note:** Google Alerts often contain multiple results per email. This spec processes the top result. To process all results, add an iterator over the parsed links.

---

### Module 3B: Action — Perplexity API Synthesis

Same as Module 2 (Feedly path) with modified prompt:

**Body:**
```json
{
  "model": "sonar-pro",
  "messages": [
    {
      "role": "system",
      "content": "You are a senior construction risk analyst specializing in regional market intelligence. Synthesize industry news for a commercial insurance brokerage founder monitoring regional construction risk. Be direct. No filler. Cite sources precisely."
    },
    {
      "role": "user",
      "content": "This is a Google Alert for the keyword: {{alert_keyword}}\n\nSynthesize this in exactly 3 paragraphs:\n\n1. What happened / what was reported (key data points only, cite the source)\n2. Why it matters for regional construction risk in this market specifically\n3. The non-obvious implication — what most people will miss\n\nArticle URL: {{article_url}}\nArticle title: {{article_title}}\nAlert keyword: {{alert_keyword}}"
    }
  ],
  "max_tokens": 600,
  "temperature": 0.3
}
```

---

### Module 4B: Action — Generate Filename

```
filename = {{alert_date}} — {{replace(alert_keyword, " ", "-")}} — Alert — {{replace(truncate(article_title, 40), " ", "-")}}.md
```

---

### Module 5B: Action — Build Markdown File Content

```
---
title: {{article_title}}
source: Google Alert — {{alert_keyword}}
url: {{article_url}}
date: {{alert_date}}
type: Oracle Feed
trigger: google-alert
keyword: {{alert_keyword}}
tags: [construction-risk, oracle, google-alert, regional]
---

# {{article_title}}

**Source:** Google Alert — `{{alert_keyword}}`
**Date:** {{alert_date}}
**URL:** {{article_url}}

---

## Synthesis

{{synthesis}}

---

## Raw Alert Excerpt
{{truncate(body_text, 500)}}

---

*Processed by Project Oracle — Gmail pipeline*
```

---

### Module 6B: Action — Create File in GitHub

Same as Module 5 (Feedly path):

**File path:** `BuildSafe IQ/Marketing & Content/Research_Base/Project_Oracle_Feeds/{{filename}}`
**Commit message:** `Oracle (Alert): {{alert_keyword}} — {{article_title}}`

---

### Module 7B: Mark Email as Processed

**App:** Gmail
**Action:** Add Label to Email
**Label:** `Oracle — Processed`

This prevents reprocessing on the next poll cycle. Create this label in Gmail first.

---

## Error Handling

Add a Router after Module 2 with two paths:

**Path A — Success:** Perplexity returned a synthesis → continue to Module 3
**Path B — Error:** Perplexity failed → send fallback email to `aaron@buildsafeiq.com` with article URL and title. Subject: `[Oracle] Failed to process: {{title}}`

---

## Research Base Index Update (Manual Step)

After articles accumulate, periodically run:

```
/ingest latest
```

Claude will scan new files in `Project_Oracle_Feeds/` that aren't yet in `Research_Base/index.md` and add them to the appropriate pillar section.

Target: run `/ingest latest` weekly as part of the Friday `/weekly-review` workflow.

---

## Cost Estimate

| Tool | Usage | Monthly Cost |
|------|-------|-------------|
| Feedly Enterprise | 200+ sources, board feature | ~$18/mo |
| Perplexity Pro API | ~200 articles/mo × $0.001 per request | ~$0.20/mo |
| Make.com | ~300 operations/mo — free tier covers this | $0 |
| GitHub | Private repo | $0 |
| Google Alerts | Email delivery to Gmail | $0 |

**Total incremental cost: ~$18/mo**

---

## Setup Sequence

### Phase 1 — Foundation
1. Install Obsidian Git plugin → connect to private GitHub repo
2. Create Feedly Enterprise account → set up 9 collections from `Project Oracle — Feedly Config.md`
3. Create Make.com account

### Phase 2 — Feedly Pipeline (Categories 1–6, 9)
4. Build Scenario A: `Oracle — Feedly to Obsidian` following Modules 1–6
5. Test with one saved Feedly article → verify file appears in vault within 2 minutes

### Phase 3 — Gmail Pipeline (Categories 7–8: Regional Alerts)
6. Set up Google Alerts for regional keywords (see Feedly Config categories 7–8 for keywords)
   - Delivery: Email to `aaron@buildsafeiq.com`
   - Frequency: As-it-happens
7. Create Gmail labels: `Oracle — Google Alerts`, `Oracle — Processed`
8. Create Gmail filter: `from:googlealerts-noreply@google.com` → apply `Oracle — Google Alerts`
9. Build Scenario B: `Oracle — Google Alerts to Obsidian` following Modules 1B–7B
10. Test with a live Google Alert email → verify file appears in vault

### Phase 4 — Verify End-to-End
11. Confirm Obsidian Git pulls all new files within 2 minutes of GitHub commit
12. Run `/ingest latest` to add first Oracle entries to `Research_Base/index.md`
13. Run `/weekly-brief` — confirm it reads Oracle feed files correctly
