# Project Oracle — Feedly Intelligence Configuration
_9-category RSS matrix for automated construction risk intelligence gathering_
_Configure in Feedly Enterprise. Target: 200+ sources across all 9 categories._

---

## Setup Instructions

1. Create a Feedly Board called **"Oracle — Curated"** — this is your high-signal save target
2. Set up each category below as a Feedly Collection
3. Any article you save to "Oracle — Curated" board triggers the Make.com automation
4. Make.com → Perplexity synthesis → GitHub → Obsidian (see `Project Oracle — Make.com Spec.md`)

---

## Category 1: Construction Industry Core

**Collection Name:** `Oracle — Construction Core`

| Source | RSS Feed |
|--------|---------|
| Engineering News-Record (ENR) | `https://www.enr.com/rss/news` |
| Construction Dive | `://www.constructiondive.com/feeds/news/` |
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

**Collection Name:** `Oracle — Phase Intelligence`

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
https
---

## Category 3: Labor & Workforce

**Collection Name:** `Oracle — Labor`

| Source | RSS Feed |
|--------|---------|
| OSHA News Releases | `https://www.osha.gov/news/newsreleases.xml` |
| NLRB Press Releases | `https://www.nlrb.gov/news-outreach/news-story/rss` |
| Building Trades News (NABTU) | `https://nabtu.org/feed/` |
| BLS Construction Data | `https://www.bls.gov/feed/` |

---

## Category 4: Supply Chain & Materials

**Collection Name:** `Oracle — Supply Chain`

| Source | RSS Feed |
|--------|---------|
| Steel Market Update | `https://www.steelmarketupdate.com/feed/` |
| Random Lengths (Lumber) | `https://www.randomlengths.com/feed/` |
| Supply Chain Dive | `https://www.supplychaindive.com/feeds/news/` |
| FreightWaves | `https://www.freightwaves.com/feed` |

---

## Category 5: Legal, Regulatory & Compliance

**Collection Name:** `Oracle — Legal & Regulatory`

| Source | RSS Feed |
|--------|---------|
| Construction Law Musings | `https://constructionlawva.com/feed/` |
| Lexology (Construction) | `https://www.lexology.com/feed/` |
| EPA Press Releases | `https://www.epa.gov/newsreleases/search/rss` |
| Federal Register (Construction) | `https://www.federalregister.gov/api/v1/documents.rss?conditions%5Bterm%5D=construction` |

---

## Category 6: Insurance & Risk Transfer

**Collection Name:** `Oracle — Insurance Markets`

| Source | RSS Feed |
|--------|---------|
| Business Insurance | `https://www.businessinsurance.com/rss/all` |
| Risk & Insurance | `https://www.riskandinsurance.com/feed/` |
| Insurance Journal | `https://insurancejournal.com/feed/` |
| PropertyCasualty360 | `https://www.propertycasualty360.com/rss/` |
| IRMI (Construction) | `https://www.irmi.com/rss` |
| Surety & Fidelity Association | `https://www.surety.org/feed/` |

---

## Category 7: Regional Market Indicators

**Collection Name:** `Oracle — Regional Matrix`

Set up Google Alerts for each metro and convert to RSS. Go to `google.com/alerts`, create the alert, then click the RSS icon.

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
| New Hampshire / New England | `"New Hampshire" AND ("construction" OR "commercial real estate" OR "development")` |

---

## Category 8: Macro-Economic & Global Risk

**Collection Name:** `Oracle — Macro`

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

**Collection Name:** `Oracle — Research`

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
