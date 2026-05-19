---
title: Cara AI
type: entity
tags: [competitor, insurance-tech, COI, workflow-automation, construction-insurance]
sources: [memory.md — COI automation feature spec 2026-05-05]
last_updated: 2026-05-19
---

# Cara AI

Insurance workflow automation platform for construction. Identified via LinkedIn (May 2026) by Aaron as a feature set worth building into BSIQ's platform.

---

## What Cara AI Does

Four core features:
1. **COI Generation** — AMS-connected, contract-driven, email delivery. Scale signal: ~30K COIs/year.
2. **Coverage Comparison & Proposal Generation** — Side-by-side analysis with citations, branded output.
3. **Knowledge Base ("Veteran in a Box")** — Upload carrier guidelines, SOPs, OSHA data → natural language search.
4. **Email AI** — Forward email thread → get ACORD/COI/coverage summary back. Zero new tab or login required.

---

## Strategic Decision

**Do not partner with or respond to Cara AI.** Build these features internally for BSIQ's platform.

Build order priority:
1. Knowledge Base (feeds all other features)
2. Email AI (lowest friction adoption)
3. COI Generation (AMS integration required)
4. Coverage Comparison (branded output layer)

Stack: AWS Textract + Claude Vision (per OCR report v1.1) + Google Apps Script email layer.

Related task: See `_OS/_tasks/TASK — Begin COI Automation Build — 2026-05-06.md` (overdue — needs decision to execute, reschedule, or defer).

---

## Positioning vs. BSIQ

| Dimension | Cara AI | BSIQ |
|---|---|---|
| Core focus | Insurance workflow automation (COI, ACORD) | Subcontractor risk scoring + advisory service |
| Primary user | Broker/insurer back office | GC risk manager |
| COI capability | Yes (core product) | Target feature to build |
| Risk scoring | No | Core product |

Cara AI is workflow. BSIQ is intelligence. The features overlap at the COI layer — BSIQ building Cara-equivalent COI automation makes the platform stickier and more complete.

---

## Cross-references
[[competitive-landscape-2026]] | [[cgl-coverage]] | [[additional-insured]]
