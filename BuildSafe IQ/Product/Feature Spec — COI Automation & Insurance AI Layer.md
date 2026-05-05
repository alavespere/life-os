# Feature Spec — COI Automation & Insurance AI Layer
_Created: 2026-05-05 | Source: LinkedIn competitor message (Cara AI / similar product)_
_Status: Roadmap — Build in VS Code_

---

## Overview

A LinkedIn message outlined a competing product ("Cara") with four AI-powered insurance workflow features. These features are directly applicable to BuildSafe IQ's risk intelligence platform and brokerage layer. Build them ourselves — do not partner or respond.

---

## Features to Build

### 1. COI Generation (Automated)
- Reads directly from AMS (Agency Management System)
- Handles complex contract-driven COI requests
- Delivers completed COI via email without leaving the inbox
- **Scale signal:** Some agencies generate ~30,000 COIs/year; the 10% requiring manual review is their biggest time sink
- **BuildSafe IQ angle:** GCs and subcontractors deal with COI requests constantly. Automate the full loop — request → AMS read → generate → email delivery

### 2. Coverage Comparison & Proposal Generation
- Side-by-side coverage analysis with citations
- Branded output
- No manual assembly required
- **BuildSafe IQ angle:** Risk scoring layer can feed directly into proposal generation. Compare subcontractor coverage against contract requirements automatically.

### 3. Knowledge Base ("Veteran in a Box")
- Upload: carrier risk appetite guides, employee manuals, SOPs, binding checklists
- Train and customize AI to your agency
- Enable natural language search across all uploaded content
- **Goal:** Make a 25-year veteran's knowledge available to someone who started 3 weeks ago
- **BuildSafe IQ angle:** Seed with OSHA enforcement data, subcontractor risk profiles, surety bond guidelines, construction-specific carrier appetite. This IS the risk intelligence layer.

### 4. Email AI (Zero-Friction Entry Point)
- Forward an email thread → get back a completed ACORD, COI, or coverage summary
- No new tab, no new login required
- **BuildSafe IQ angle:** Lowest-friction adoption path. Users don't need to learn a new tool — they just forward emails. Output plugs into existing workflows.

---

## Architecture Notes

The underlying stack for all four features:
- **Document ingestion:** AWS Textract + Claude Vision hybrid (per OCR report v1.1)
- **AI reasoning layer:** Claude (not Mistral — Mistral scoped for Phase 3 cost reduction on structured extraction only)
- **Email layer:** Gmail API or Google Apps Script for email forwarding/delivery
- **AMS integration:** To be scoped — depends on which AMS platforms target clients use

---

## Roadmap Position

| Feature | Priority | Complexity | Notes |
|---------|----------|------------|-------|
| Knowledge Base | High | Medium | Build first — feeds all other features |
| Email AI | High | Medium | Highest adoption leverage — zero friction |
| COI Generation | High | High | Needs AMS integration scoped first |
| Coverage Comparison | Medium | Medium | Depends on knowledge base being live |

---

## Next Action
- [ ] Open VS Code and begin architecture for Knowledge Base feature
- [ ] Research AMS platforms used by target GC clients
- [ ] Identify "Cara" company (Google the product name) — track their funding and roadmap
- [ ] Map email AI flow using existing Google Apps Script infrastructure

---

_Linked memory entry: 2026-05-05 — Product — COI Automation Feature Set Added to Roadmap_
