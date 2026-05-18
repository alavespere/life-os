# TASK — Begin COI Automation & Insurance AI Build
_Created: 2026-05-05 | Original Due: 2026-05-06 | Status: OVERDUE — needs decision | Last reviewed: 2026-05-18_

---

## Task
Open VS Code and begin architecture for the COI Automation + Insurance AI Layer feature set.

## Context
Identified a competing product (Cara AI) via LinkedIn with four insurance workflow automation features worth building into BuildSafe IQ. Full feature spec saved to:
`BuildSafe IQ/Product/Feature Spec — COI Automation & Insurance AI Layer.md`

## Starting Point — Build in This Order
1. **Knowledge Base** — Upload carrier risk appetite guides, SOPs, OSHA data → natural language search. Feeds everything else.
2. **Email AI** — Forward thread → get ACORD/COI/coverage summary back. Zero friction adoption.
3. **COI Generation** — AMS integration + contract-driven generation + email delivery.
4. **Coverage Comparison** — Side-by-side analysis with citations, branded output.

## First Session Goal (Tomorrow)
- Open VS Code
- Sketch the Knowledge Base architecture: ingestion pipeline, storage, retrieval layer
- Reference: `BuildSafe IQ/Product/Feature Spec — COI Automation & Insurance AI Layer.md`
- Stack: AWS Textract + Claude Vision (per OCR report v1.1) + Google Apps Script for email layer

## Done When
- [ ] Knowledge Base architecture diagrammed in VS Code
- [ ] Ingestion pipeline decision made (file types, storage, chunking strategy)
- [ ] First prototype or scaffold started

---
_Linked files: [[Feature Spec — COI Automation & Insurance AI Layer]]_
