# Project Oracle — Complete Workflow
_Every step from "article appears in Feedly" to "processed note lands in Obsidian vault"_
_Designed for Feedly free tier._

---

## The Problem With the Original Plan

The original spec called for a "Feedly Board" called `Oracle — Curated` where Aaron saves individual articles. **Boards are a Feedly Pro feature.** On free tier, you can only create folders for organizing RSS feed sources — not save individual articles to a custom destination.

This doc replaces that approach with two paths that work on free Feedly:

- **Path A — Automatic:** Make.com watches key RSS feeds directly, processes all new articles on a schedule. No manual action required.
- **Path B — Manual queue:** Aaron reads in Feedly, pastes URLs of best articles into a Google Sheet. Make.com watches the sheet and processes on demand.

Use both together: Path A for volume (catch everything from top feeds), Path B for priority pieces you want processed immediately or with a custom note.

---

## What Feedly Free Actually Supports

| Feature | Free | Pro |
|---------|------|-----|
| Folders (collections) | 3 max | Unlimited |
| RSS feeds per folder | Unlimited | Unlimited |
| Save individual articles to Boards | No | Yes |
| AI Priority Signals | No | Yes |
| Mute filters (keyword hide) | Yes | Yes |
| API access for Make.com | Limited | Full |
| Share article via email/link | Yes | Yes |
| Read Later (basic save) | Yes | Yes |

**Bottom line:** Feedly free is a reading interface. The automation trigger must come from somewhere else — either direct RSS watching in Make.com (Path A) or a Google Sheet queue (Path B).

---

## Complete Workflow — Step by Step

### Step 1: Reading (Daily — in Feedly)

1. Open Feedly → go to **Phase Intelligence** folder
2. Scan headlines — look for:
   - Data points you can use in content
   - Market shifts relevant to construction risk
   - Legal/regulatory changes affecting GCs or subs
   - Anything that would surprise your audience
3. Click to read promising articles
4. Repeat in **Labor** folder

**Time target:** 15–20 minutes per day

---

### Step 2: Curation Decision

For each article you read, make one of three calls:

| Decision | Action |
|----------|--------|
| **Strong signal** — worth a full Perplexity synthesis | Copy URL → paste into Oracle Queue sheet (Path B, immediate processing) |
| **Decent signal** — let the automation catch it | Leave it. If it's in a feed on the Path A watch list, it'll be auto-processed |
| **Skip** — press release, gear review, noise | Move on |

**Target:** 3–7 articles/day manually queued (Path B). Path A handles the rest.

---

### Step 3: Path A — Automatic RSS Processing (Make.com)

Make.com watches a curated shortlist of your highest-signal RSS feeds directly — bypassing Feedly entirely. New articles trigger the pipeline automatically.

**Feeds Make.com watches directly (Path A shortlist):**

| Feed | Why |
|------|-----|
| Engineering News-Record | Highest signal construction news |
| Construction Dive | Best daily construction intel |
| Insurance Journal | Insurance market moves |
| OSHA News Releases | Compliance/regulatory |
| Supply Chain Dive | Material cost signals |
| Federal Register (Construction) | Regulatory changes |
| Federal Reserve News | Macro rate signals |

Make.com checks these every 15–30 minutes. Every new article is sent to Perplexity for synthesis and written to your vault.

**Result:** Your vault fills automatically with processed intel from top feeds. No action required from you.

---

### Step 4: Path B — Manual Queue (Google Sheets)

When you find a strong article in Feedly that you want processed immediately (or with a personal note attached), you add it to the Oracle Queue sheet.

**Setup (one time):**

Create a Google Sheet called **"Oracle Queue"** with these columns:

| Column | Purpose |
|--------|---------|
| A: URL | Paste the article URL here |
| B: Title | Optional — copy the headline |
| C: Note | Optional — your context ("use for DFW section") |
| D: Status | Leave blank — Make.com writes "Processed" here when done |

Make.com trigger: **Google Sheets → Watch New Rows** — fires when you add a new row to column A.

**Your action:** Find a good article in Feedly → copy URL → paste in column A of the sheet → done.

---

### Step 5: Make.com Processing (both paths)

Both Path A and Path B feed into the same Make.com processing pipeline:

```
RSS feed (Path A) or Google Sheet row (Path B)
    ↓
Extract: title, URL, source, date
    ↓
Perplexity API — 3-paragraph synthesis
    (What happened / Why it matters / Non-obvious implication)
    ↓
Build .md file with YAML frontmatter
    ↓
GitHub API — create file in vault repo
    ↓
Obsidian Git auto-pull (every 1 min)
    ↓
File lands in: BuildSafe IQ/Marketing & Content/Research_Base/Project_Oracle_Feeds/
```

See `Project Oracle — Make.com Spec.md` for the exact module-by-module build instructions.

---

### Step 6: Vault Review (Weekly)

New files accumulate in `Research_Base/Project_Oracle_Feeds/` throughout the week.

**Weekly trigger (part of `/weekly-review`):**

1. Run `/ingest latest` — Claude scans new Oracle files, adds them to `Research_Base/index.md` under the correct pillar
2. Run `/weekly-brief` — Claude drafts the newsletter from that week's Oracle files
3. Aaron reviews and publishes the newsletter draft

---

## Daily Habit Loop

```
Morning (15 min):
  Open Feedly → read Phase Intelligence + Labor
  Strong articles → paste URL into Oracle Queue sheet
  Automation handles the rest

Weekly (Friday):
  /ingest latest → updates Research Base index
  /weekly-brief → drafts newsletter from Oracle feeds
  Review draft → publish to Beehiiv
```

---

## Setup Checklist

### Feedly (you are here)
- [x] Phase Intelligence folder — feeds added
- [x] Labor folder — feeds added
- [ ] Curated folder — repurpose: delete it OR rename to "Reading Queue" (optional aesthetic choice — it's not used in automation)
- [ ] Add mute filters: `press release`, `product launch`, `sponsored`, `webinar`

### Google Sheet (next step)
- [ ] Create "Oracle Queue" sheet with columns: URL, Title, Note, Status
- [ ] Copy the sheet URL — you'll need it for Make.com

### Google Alerts (next step)
- [ ] Create 11 regional alerts (see Feedly Config → Category 7 for queries)
- [ ] Set delivery: email to `aaron@buildsafeiq.com`
- [ ] Create Gmail filter: `from:googlealerts-noreply@google.com` → label `Oracle — Google Alerts`
- [ ] Create second Gmail label: `Oracle — Processed`

### Obsidian Git (before Make.com)
- [ ] Install Obsidian Git plugin
- [ ] Connect to private GitHub repo
- [ ] Set auto-pull interval: 1 minute

### Make.com (last step)
- [ ] Build Scenario A: Direct RSS watcher → Perplexity → GitHub
- [ ] Build Scenario B: Google Sheet queue → Perplexity → GitHub
- [ ] Build Scenario C: Gmail Google Alerts → Perplexity → GitHub
- [ ] Test all three paths end-to-end

---

## Where Things Land in the Vault

```
BuildSafe IQ/Marketing & Content/Research_Base/
├── Project_Oracle_Feeds/
│   ├── 2026-04-30 — ENR Article Title — Oracle.md
│   ├── 2026-04-30 — Construction Dive Article — Oracle.md
│   └── ...
└── index.md  ← updated weekly by /ingest latest
```

Each file has:
- YAML frontmatter (title, source, URL, date, type, pillar, tags)
- Perplexity synthesis (3 paragraphs)
- Raw summary from feed
