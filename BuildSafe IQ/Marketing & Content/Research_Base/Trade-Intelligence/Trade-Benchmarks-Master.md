# Trade-Intelligence: Master Benchmarks Reference
_Structured extraction for use in Risk Scoring Model, Subcontractor Prequal Module, and Underwriting Tool._
_Sources: BLS Table 1 (2024), ABC STEP (2025), NCCI, CFMA 2024, LumberFi EMR Guide (2025)_
_Last updated: 2026-05-12_

---

## How to Use This File
- **Risk Scoring Model:** Use EMR and TRIR scoring tables (Part III) for trade-adjusted scoring inputs
- **Subcontractor Prequal Module:** Use Parts I–IV for benchmark lookup by NAICS code
- **Underwriting / Brokerage:** Use WC loss cost rates (Part II) and GL risk tier (Part IV)
- **Content Engine:** Use Part V for counterintuitive data points

---

## Part I: Safety Benchmarks by Trade (BLS 2024 / ABC STEP 2025)

| Trade | NAICS | TRIR | DART | DAFW | ABC Gold Max | ABC Diamond Max | EMR Industry Avg | EMR Acceptable | EMR Red Flag |
|---|---|---|---|---|---|---|---|---|---|
| Framing | 238130 | **4.6** | **3.4** | 2.1 | 5.5 | 2.75 | 1.05–1.25 | ≤ 1.10 | > 1.40 |
| Siding | 238170 | **3.2** | **2.5** | 2.2 | 5.8 | 2.90 | 1.00–1.15 | ≤ 1.05 | > 1.35 |
| HVAC/Plumbing | 238220 | 2.9 | 1.7 | 1.1 | 2.9 | 1.45 | 0.92–1.03 | ≤ 1.00 | > 1.15 |
| Drywall/Insulation | 238310 | 2.9 | 2.0 | 1.2 | 3.6 | 1.80 | 0.95–1.10 | ≤ 1.00 | > 1.25 |
| Concrete | 238110 | 2.8 | 2.0 | 1.3 | 2.8 | 1.40 | 0.95–1.10 | ≤ 1.00 | > 1.20 |
| Steel/Precast | 238120 | 2.8 | 1.3 | 0.8 | 3.6 | 1.80 | 0.90–1.05 | ≤ 1.00 | > 1.15 |
| Glass/Glazing | 238150 | 2.7 | 1.5 | 0.7 | 2.5 | 1.25 | 0.90–1.05 | ≤ 1.00 | > 1.20 |
| Roofing | 238160 | 2.4 | 1.7 | 1.1 | 3.2 | 1.60 | **1.08–1.22** | ≤ 1.10 | > 1.40 |
| Tile/Terrazzo | 238340 | 2.4 | 1.6 | 1.2 | 1.5 | 0.75 | 0.88–1.00 | ≤ 1.00 | > 1.20 |
| **All Specialty (238)** | — | **2.3** | **1.4** | **1.0** | — | — | — | — | — |
| Flooring | 238330 | 2.0 | 0.7 | 0.6 | 2.4 | 1.20 | 0.88–1.00 | ≤ 1.00 | > 1.20 |
| Masonry | 238140 | 1.9 | 1.5 | 1.2 | 2.7 | 1.35 | 0.88–1.00 | ≤ 1.00 | > 1.20 |
| Electrical | 238210 | **1.8** | 1.1 | 0.7 | 2.0 | 1.00 | 0.82–0.93 | ≤ 1.00 | > 1.15 |
| Painting | 238320 | **1.6** | 1.1 | 1.0 | 1.6 | 0.80 | 0.85–0.95 | ≤ 1.00 | > 1.15 |
| Site Prep | 238910 | **1.5** | 1.0 | 0.7 | 1.9 | 0.95 | 0.88–1.00 | ≤ 1.00 | > 1.20 |

**TRIR = Total Recordable Incident Rate | DART = Days Away, Restricted, or Transferred | DAFW = Days Away from Work**
**EMR = Experience Modification Rate (1.0 = industry average for that trade)**

---

## Part II: Workers' Compensation Profile by Trade

| Trade | Primary NCCI Code | Code Description | Loss Cost (per $100 payroll) | WC Risk Tier | Multiple vs. Electrical (5190) |
|---|---|---|---|---|---|
| Steel Erection (high-rise) | **5069** | Iron/Steel Erection, not over 2 stories | **~$60.61** | Extreme | **11.0x** |
| Steel Erection (1–2 story) | **5059** | Iron/Steel Frame Structure | **~$35.15** | Very High | **6.4x** |
| Bridge/Industrial Painting | **5037** | Painting Metal Bridges | **~$29.65** | Very High | **5.4x** |
| Roofing NOC | **5545** | Roofing NOC | **~$25.15** | Very High | **4.6x** |
| Roofing Felt/Pitch | **5547** | Roofing/Comm/Felt & Pitch | **~$23.01** | Very High | **4.2x** |
| Concrete | **5213** | Concrete Construction | **~$16.58** | High | **3.0x** |
| Masonry | **5022** | Masonry | **~$14.85** | High | **2.7x** |
| Framing (commercial) | **5403** | Carpentry NOC | **~$13.09** | High | **2.4x** |
| Line Work Electrical | **7538** | Electrical Light/Power Line | **~$13.51** | High | **2.5x** |
| Drywall | **5221** | Drywall/Pkg Area | **~$10.99** | Moderate-High | **2.0x** |
| Painting (3 stories or less) | **5040** | Painting, 3 Stories or Less | **~$10.48** | Moderate | **1.9x** |
| Roofing (sheet metal flat) | **5538** | Roofing/Comm/Sht Mtl Flat | **~$9.48** | Moderate | **1.7x** |
| Framing (residential) | **5651** | Carpentry, Residential ≤3 Stories | **~$8.77** | Moderate | **1.6x** |
| Plumbing | **5183** | Plumbing | **~$7.57** | Moderate | **1.4x** |
| Insulation | **5479** | Insulation Work NOC | **~$7.61** | Moderate | **1.4x** |
| HVAC | **5536** | Air Conditioning | **~$7.41** | Moderate | **1.3x** |
| Electrical (within building) | **5190** | Electrical Work Within Building | **~$5.49** | Lower | **1.0x (baseline)** |
| Fire Suppression | **5188** | Fire Suppression Systems | **~$4.51** | Lower | **0.8x** |

*Loss costs are estimates and vary by state and carrier. Use for relative comparison and risk tiering only.*

---

## Part III: Trade-Adjusted Scoring Tables (Risk Scoring Model)

### EMR Scoring — Trade-Calibrated

| Score | Label | Electrical / Painting | HVAC / Plumbing / Masonry | Concrete / Steel / Drywall | Roofing / Framing / Siding |
|---|---|---|---|---|---|
| **5** | Excellent | < 0.70 | < 0.75 | < 0.80 | < 0.85 |
| **4** | Good | 0.70–0.85 | 0.75–0.90 | 0.80–0.95 | 0.85–1.00 |
| **3** | Acceptable | 0.85–1.00 | 0.90–1.05 | 0.95–1.10 | 1.00–1.15 |
| **2** | Marginal | 1.00–1.15 | 1.05–1.20 | 1.10–1.25 | 1.15–1.30 |
| **1** | Unacceptable | > 1.15 | > 1.20 | > 1.25 | > 1.35 |

### TRIR Scoring — Trade-Calibrated

| Score | Label | Electrical / Painting | HVAC / Plumbing | Concrete / Masonry | Roofing / Framing |
|---|---|---|---|---|---|
| **5** | Excellent | < 0.9 | < 1.5 | < 1.4 | < 1.6 |
| **4** | Good | 0.9–1.5 | 1.5–2.0 | 1.4–2.0 | 1.6–2.5 |
| **3** | Acceptable | 1.5–2.0 | 2.0–2.9 | 2.0–2.8 | 2.5–3.5 |
| **2** | Marginal | 2.0–2.5 | 2.9–3.5 | 2.8–3.5 | 3.5–4.5 |
| **1** | Unacceptable | > 2.5 | > 3.5 | > 3.5 | > 4.5 |

---

## Part IV: Financial Benchmarks by Trade

| Trade | Gross Margin | Net Margin | Current Ratio | Quick Ratio | Days in AR | Rev/Employee | Key Financial Risk |
|---|---|---|---|---|---|---|---|
| Electrical | 28–35% | 4–8% | 1.4–1.8 | 1.0–1.4 | 45–60 days | $250–325K | Material float, copper price volatility |
| HVAC/Plumbing | 28–35% | 4–7% | 1.4–1.9 | — | 45–65 days | $200–300K | Equipment cost, refrigerant |
| Roofing | 20–30% | 3–6% | 1.3–1.8 | — | 50–70 days | $175–250K | Warranty reserve, weather |
| Concrete | 18–25% | 2–5% | 1.3–1.7 | — | 45–60 days | $150–225K | Equipment leverage |
| Steel/Precast | 20–28% | 3–6% | 1.3–1.7 | — | — | $200–275K | Crane costs, WC premium burden |
| Framing | 15–22% | 2–4% | 1.2–1.6 | — | — | $150–200K | Lumber price volatility |
| Masonry | 18–25% | 2–5% | 1.3–1.7 | — | — | $150–200K | Material cost, labor availability |
| Drywall/Insulation | 18–25% | 2–5% | 1.3–1.7 | — | — | $150–200K | Material cost |
| Painting | 20–28% | 3–6% | 1.3–1.8 | — | — | $150–225K | Material, CPL exposure |
| Site Prep | 20–28% | 3–6% | 1.3–1.7 | — | — | $175–250K | Equipment depreciation |
| Flooring | 22–30% | 3–6% | 1.3–1.8 | — | — | $150–225K | Adhesive/material cost |

---

## Part V: Surety Bonding Profile by Trade

| Trade | Bondability | Single Project Limit | Aggregate Limit | Key Surety Concerns |
|---|---|---|---|---|
| Electrical | High | 8–12x working capital | 12–18x WC | License, material procurement, backlog concentration |
| HVAC/Plumbing | High | 8–12x working capital | 12–18x WC | Equipment ownership, change order management |
| Concrete | Moderate-High | 8–10x working capital | 12–15x WC | Equipment schedule, formwork ownership |
| Steel/Precast | Moderate | 7–10x working capital | 10–15x WC | Crane ownership, WC premium burden |
| Roofing | Moderate | 7–10x working capital | 10–15x WC | Warranty exposure, insurance placement |
| Framing | Moderate | 7–10x working capital | 10–15x WC | Lumber price risk, thin margins |
| Masonry | Moderate | 8–10x working capital | 12–15x WC | Silica compliance, material cost |
| Painting | Moderate | 8–12x working capital | 12–18x WC | Environmental liability, completed ops |
| Site Prep | Moderate | 8–10x working capital | 12–15x WC | Environmental liability, equipment |

---

## Part VI: General Liability Risk Tier by Trade

| Trade | GL Risk Tier | Monthly GL Cost (Small Sub) | Primary Loss Driver |
|---|---|---|---|
| Roofing | **Extreme** | $150–$300 | Completed ops, water intrusion, hot work |
| Steel Erection | **Extreme** | $200–$500+ | Catastrophic property damage, crane |
| Fire Sprinkler | **Very High** | $150–$350 | Water damage, system impairment |
| HVAC/Plumbing | **High** | $75–$140 | Water damage, completed ops |
| Concrete | **High** | $100–$200 | Formwork failure, pump operations |
| Masonry | **High** | $100–$200 | Silica, scaffold, completed ops |
| Electrical | **Moderate-High** | $85–$150 | Fire, completed ops, arc flash |
| Drywall/Insulation | **Moderate** | $75–$125 | Scaffold, completed ops |
| Painting | **Moderate** | $75–$125 | VOC/chemical, completed ops |
| Site Preparation | **Moderate** | $100–$200 | Environmental, utility strikes |
| Flooring | **Lower** | $60–$100 | Chemical adhesives |

---

## Part VII: NAICS Code Quick Reference

| NAICS | Trade | Primary WC Code |
|---|---|---|
| 238110 | Poured Concrete | 5213 |
| 238120 | Structural Steel & Precast | 5069 / 5059 |
| 238130 | Framing | 5403 / 5651 |
| 238140 | Masonry | 5022 |
| 238150 | Glass & Glazing | — |
| 238160 | Roofing | 5545 / 5547 / 5538 |
| 238170 | Siding | — |
| 238210 | Electrical | 5190 / 7538 |
| 238220 | Plumbing, HVAC | 5183 / 5536 |
| 238310 | Drywall & Insulation | 5221 / 5479 |
| 238320 | Painting | 5040 / 5037 |
| 238330 | Flooring | — |
| 238340 | Tile & Terrazzo | — |
| 238910 | Site Preparation | — |
