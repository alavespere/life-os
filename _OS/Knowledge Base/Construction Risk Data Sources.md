# Construction Risk Data Sources — Free & Public
_Research reference — Last updated: 2026-04-06_

---

## 1. Government & Regulatory Sources

| Source | What to Pull | Use Case |
|--------|-------------|----------|
| OSHA | Violation records, incident reports, citations, NAICS codes | Safety benchmarking, subcontractor prequal risk scoring |
| Census Bureau — Building Permits Survey | Monthly permit data by county, state, metro | Regional demand trends, backlog analysis, labor strain |
| BLS (Bureau of Labor Statistics) | Construction employment, wage, productivity, injury rates | Regional labor availability, project planning, wage risk |
| EEOC | Construction-related discrimination/harassment claims | Company reputation monitoring |
| Department of Labor (WHD Enforcement) | Wage/hour violations by employer | Reputation/litigation risk scoring |
| FMCSA (for fleets) | Truck safety scores, driver violations | Fleet risk profiling for self-performing GCs |
| NOAA / NWS | Weather events, historic & forecast | Weather delay prediction by zip code |

---

## 2. Legal & Litigation Databases

| Source | What to Pull | Use Case |
|--------|-------------|----------|
| PACER (via CourtListener RECAP API) | Federal court filings involving construction firms | Predictive litigation risk, delay patterns, contract types |
| State-level court sites | Local civil case filings, liens, judgments | Sub-level litigation trend mapping |
| LCP Tracker | Prevailing wage compliance on public projects | Labor compliance audit history |

---

## 3. Industry News & Permit Feeds

| Source | What to Pull | Use Case |
|--------|-------------|----------|
| Dodge Data & Analytics (free briefs) | Construction starts, delays, project types | Permit-based backlog monitoring |
| ENR (Engineering News-Record) | Legal disputes, M&A, market instability | Risk alerts for partners and GCs |
| Building departments (city/county) | Inspection failures, stop work orders | Local enforcement trends |
| Union sites / NLRB | Strike announcements, labor disputes | Schedule/labor risk prediction |

---

## 4. Social & Review Platforms

| Source | What to Pull | Use Case |
|--------|-------------|----------|
| Glassdoor / Indeed | Employee reviews of construction firms | Culture/stability scoring |
| Reddit / Contractor forums | Sub chatter, payment issues, delays | Risk signals from project-level conversation |
| Better Business Bureau (BBB) | Complaints filed against contractors | Prequal risk layer |

---

## 5. Corporate & Financial Data

| Source | What to Pull | Use Case |
|--------|-------------|----------|
| OpenCorporates / SEC EDGAR | Incorporation, ownership, litigation disclosures | Company integrity scoring |
| State contractor licensing boards | License suspensions, revocations, complaints | Prequalification data enhancement |
| SAM.gov | Federal contractor history | Prime/sub partnership viability |

---

## Derived Risk Signals
Raw data is step one. The value is in derived signals:

- **Safety score:** OSHA violations per $1M in revenue (normalized)
- **Litigation density:** Court filings per active project
- **Labor stability index:** BLS regional employment trend + union activity
- **Weather delay probability:** NOAA historical + forecast by project zip code
- **Financial stability proxy:** Licensing status + BBB + court judgments + payment disputes
- **Schedule risk indicator:** Permit pull rate vs. inspection pass rate by jurisdiction
