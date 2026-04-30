# Project Oracle — Feedly Intelligence Configuration
_3-folder RSS matrix for construction risk intelligence gathering (Feedly free tier)_
_~40 RSS sources across 3 folders. Category 7 (Regional) handled via Gmail/Google Alerts._

---

## Free Tier Constraints

Feedly free allows **3 folders max**. The original 9-category design is consolidated below into 3 folders that map to your existing setup. Do not create new folders — add feeds to existing ones.

| Folder | Categories Covered | Sources |
|--------|--------------------|---------|
| `Curated` | Save-to-trigger only — no feeds | 0 |
| `Labor` | Categories 3, 4, 5, 6 — Risk Signals | ~18 feeds |
| `Phase Intelligence` | Categories 1, 2, 8, 9 — Industry Reading | ~22 feeds |
| *(Gmail pipeline)* | Category 7 — Regional (Google Alerts) | n/a |

---

## Setup Instructions

1. **`Curated` folder** — keep empty of feeds. Use it only as a manual save destination. Any article you read in Feedly and save here triggers the Make.com automation.
2. **`Labor` folder** — add all feeds from Categories 3, 4, 5, and 6 below
3. **`Phase Intelligence` folder** — add all feeds from Categories 1, 2, 8, and 9 below
4. **Mute Filters** (Feedly → Preferences → Mute Filters) — add: `press release`, `product launch`, `sponsored`, `webinar`
5. Make.com → Perplexity synthesis → GitHub → Obsidian (see `Project Oracle — Make.com Spec.md`)

---

## FOLDER: Phase Intelligence
_Add Categories 1, 2, 8, and 9 to this folder._

---

## Category 1: Construction Industry Core

**Add to folder:** `Phase Intelligence`

| Source | RSS Feed |
|--------|---------|
| Engineering News-Record (ENR) | `https://www.enr.com/rss/news` |
| Construction Dive | `https://www.constructiondive.com/feeds/news/` |
| Building Design+Construction | `https://www.bdcnetwork.com/rss/articles.xml` |
| Constructor Magazine (AGC) | `https://www.constructormagazine.com/feed/` |
| Construction Executive | `https://constructionexec.com/feed` |
| For Construction Pros | `https://www.forconstructionpros.com/rss/all` |
| Constructech Magazine | `https://www.constructech.com/feed/` |
| ProBuilder | `https://www.probuilder.com/rss.xml` |
| Contractor Magazine | `https://www.contractormag.com/rss/all` |
| Jobsite News (Procore) | `https://jobsite.procore.com/feed/` |

---

## Category 2: Phase-Based Intelligence

**Add to folder:** `Phase Intelligence` _(already configured — verify feeds are present)_

**Pre-Construction & Design**
| Source | RSS Feed |
|--------|---------|
| AIA News | `https://www.aia.org/rss/news` |
| Design-Build Institute of America | `https://dbia.org/feed/` |
| Dodge Construction Network | `https://www.construction.com/feed/` |

**Construction & Execution**
| Source | RSS Feed |
|--------|---------|
| Equipment World | `https://www.equipmentworld.com/rss/all` |

**Post-Construction & FM**
| Source | RSS Feed |
|--------|---------|
| FacilitiesNet | `https://www.facilitiesnet.com/rss/` |
| BOMA International | `https://www.boma.org/rss` |

---

## FOLDER: Labor
_Add Categories 3, 4, 5, and 6 to this folder._

---

## Category 3: Labor & Workforce

**Add to folder:** `Labor` _(already configured — verify feeds are present)_

| Source | RSS Feed |
|--------|---------|
| OSHA News Releases | `https://www.osha.gov/news/newsreleases.xml` |
| NLRB Press Releases | `https://www.nlrb.gov/news-outreach/news-story/rss` |
| Building Trades News (NABTU) | `https://nabtu.org/feed/` |
| BLS Construction Data | `https://www.bls.gov/feed/` |

---

## Category 4: Supply Chain & Materials

**Add to folder:** `Labor`

| Source | RSS Feed |
|--------|---------|
| Steel Market Update | `https://www.steelmarketupdate.com/feed/` |
| Random Lengths (Lumber) | `https://www.randomlengths.com/feed/` |
| Supply Chain Dive | `https://www.supplychaindive.com/feeds/news/` |
| FreightWaves | `https://www.freightwaves.com/feed` |

---

## Category 5: Legal, Regulatory & Compliance

**Add to folder:** `Labor`

| Source | RSS Feed |
|--------|---------|
| Construction Law Musings | `https://constructionlawva.com/feed/` |
| Lexology (Construction) | `https://www.lexology.com/feed/` |
| EPA Press Releases | `https://www.epa.gov/newsreleases/search/rss` |
| Federal Register (Construction) | `https://www.federalregister.gov/api/v1/documents.rss?conditions%5Bterm%5D=construction` |

---

## Category 6: Insurance & Risk Transfer

**Add to folder:** `Labor`

| Source | RSS Feed |
|--------|---------|
| Business Insurance | `https://www.businessinsurance.com/rss/all` |
| Risk & Insurance | `https://www.riskandinsurance.com/feed/` |
| Insurance Journal | `https://insurancejournal.com/feed/` |
| PropertyCasualty360 | `https://www.propertycasualty360.com/rss/` |
| IRMI (Construction) | `https://www.irmi.com/rss` |
| Surety & Fidelity Association | `https://www.surety.org/feed/` |

---

## FOLDER: None — Gmail Pipeline Only
_Category 7 does not use a Feedly folder. Configure Google Alerts to email delivery only._

---

## Category 7: Regional Market Indicators

**Handled via:** Gmail pipeline → Make.com (see `Project Oracle — Make.com Spec.md` → Scenario B)

Google Alerts no longer offers RSS on most accounts. Set each alert to email delivery → `aaron@buildsafeiq.com`. Gmail filter (`from:googlealerts-noreply@google.com` → label `Oracle — Google Alerts`) feeds the Make.com automation.

Do NOT add these to Feedly.

| Metro | Alert Query |
|-------|------------|
| Boston | `"Boston" AND ("commercial real estate" OR "construction starts" OR "biotech development")` |
| New York City | `"NYC" AND ("commercial real estate" OR "construction starts" OR "zoning changes")` |
| Chicago | `"Chicago" AND ("commercial real estate" OR "construction starts" OR "logistics development")` |
| Los Angeles | `"Los Angeles" AND ("commercial real estate" OR "construction starts" OR "infrastructure")` |
| Dallas/Fort Worth | `"DFW" AND ("commercial real estate" OR "construction starts" OR "corporate relocation")` |
| Miami/South Florida | `"Miami" AND ("commercial real estate" OR "construction starts" OR "climate risk")` |
| Atlanta | `"Atlanta" AND ("commercial real estate" OR "construction starts" OR "industrial development")` |
| Seattle | `"Seattle" AND ("commercial real estate" OR "construction starts" OR "tech development")` |
| Denver | `"Denver" AND ("commercial real estate" OR "construction starts" OR "population growth")` |
| Phoenix | `"Phoenix" AND ("commercial real estate" OR "construction starts" OR "water risk")` |
| Detroit | `"Detroit" AND ("commercial real estate" OR "construction starts" OR "automotive development")` |
| Minneapolis | `"Minneapolis" AND ("commercial real estate" OR "construction starts" OR "industrial development")` |

---

## FOLDER: Phase Intelligence (continued)

---

## Category 8: Macro-Economic & Global Risk

**Add to folder:** `Phase Intelligence`

| Source | RSS Feed |
|--------|---------|
| Wall Street Journal (Economy) | `https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml` |
| Federal Reserve News | `https://www.federalreserve.gov/feeds/press_all.xml` |
| Mortgage Bankers Association | `https://www.mba.org/rss` |
| Council on Foreign Relations | `https://www.cfr.org/rss/all` |
| NOAA News | `https://www.noaa.gov/rss` |
| Swiss Re Institute | `https://www.swissre.com/rss` |
| Munich Re | `https://www.munichre.com/rss` |
| Climate Central | `https://www.climatecentral.org/rss` |
| World Economic Forum | `https://www.weforum.org/rss` |

---

## Category 9: Academic & Research

**Add to folder:** `Phase Intelligence`

| Source | RSS Feed |
|--------|---------|
| RAND Corporation | `https://www.rand.org/rss/research_reports.xml` |
| McKinsey Global Institute | `https://www.mckinsey.com/rss` |
| Deloitte Insights | `https://www2.deloitte.com/rss` |
| Journal of Construction Engineering | `https://ascelibrary.org/action/showFeed?type=etoc&feed=rss&jc=jcemd4` |

---

## Curation Protocol

Not every article in every feed needs to be processed. Be selective:

**Save to "Oracle — Curated" board (triggers Make.com) when:**
- The article contains a data point usable in content
- It signals a market shift relevant to construction risk
- It has legal or regulatory implications for GCs or subs
- It would surprise your target audience

**Skip when:**
- Company press releases with no data
- Gear reviews or product announcements
- Duplicate coverage of the same story

**Target:** 3–7 articles per day saved to Curated. Quality over volume.
