# CVF LPCI1 Legal Policy Corpus Intelligence Product MVP Roadmap

Memory class: FULL_RECORD

Status: ACTIVE

docType: roadmap

Date: 2026-06-03

executionBaseHead: `c0ebfd9c`

## Purpose

Define the governed implementation tranches for the LPCI1 Legal/Policy
Corpus Intelligence chatbot MVP. This roadmap converts CI2 corpus enforcement
readiness into a staged product implementation plan.

This roadmap authorizes LPCI1 tranches in sequence. Each tranche must open a
fresh work order with source verification. This document is planning
authorization only — it does not implement LPCI.

## Scope / Applies To

Applies to: all LPCI1 implementation tranches (T1–T7).

Owner surface: CVF governance layer; LPCI1 product tranche owners.

This roadmap is bounded by:

- `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md`
- `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md`
- `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json`

---

## Non-Goals

- Implement any LPCI runtime artifact (UI, API, vector DB, embedding, provider call).
- Provide legal advice or production compliance certification.
- Build public SaaS, multi-tenant hosting, or autonomous legal decisioning.
- Perform broad legacy corpus re-scan beyond the two registered CI1 pilot roots.
- Claim legal answer correctness or production readiness.
- Replace an LLM provider or search engine with a general-purpose corpus.

---

## Evidence Inheritance (from CI2)

| CI2 artifact | LPCI1 consumption |
| --- | --- |
| CI2-T4 pilot pack (`CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json`) | Schema proof for T1 intake architecture; not a production corpus |
| CI2-T3 enforced index model (`CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL.json`) | Field schema for all LPCI corpus packets |
| CI2-T2 checkers (NR-04, NR-05, NR-11) | Structurally enforced on all LPCI corpus packets |
| CI1-T7 LPCI intake bridge | Primary inputs, gap acknowledgment obligations, claim boundary inheritance |
| CI1-T5 sampling results | T5 PASSED_SAMPLING_WITH_GAPS — not runtime accuracy proof |

Inherited gaps from CI2-T4 that LPCI must carry forward:

| Gap | Field | Impact on LPCI |
| --- | --- | --- |
| G1 per-file hash | `sourceHash` | LPCI ingest must declare per-file hash or accepted manifest proxy per NR-04 |
| G2 T2 ownerSurface alias | `ownerSurface` | pilot pack only; LPCI real corpus must use canonical enum |
| G3 legal/policy fields absent | legalPolicy domain extensions | LPCI T2 must populate these when a real legal corpus is ingested |

---

## Tranche Plan

| Tranche | Goal | Primary outputs | Status | Dependency |
| --- | --- | --- | --- | --- |
| LPCI1-T1 | Product Intake and Architecture | architecture document, corpus intake spec, LPCI GC-018 T1 supplement | HOLD_PENDING_CI2_T5_COMMIT — work order exists | LPCI1 GC-018 plus CI2-T5 closure commit |
| LPCI1-T2 | Domain Classification | legal/policy classification ledger aligned with GC-050, NR-11 alias enforcement | PROPOSED | T1 architecture reviewed |
| LPCI1-T3 | Search and Filter Index | faceted index schema, query filter contract, negative search evidence format | PROPOSED | T2 classification closed |
| LPCI1-T4 | Retrieval Boundary | citation-first retrieval receipt, freshness/conflict warning, abstention rules | PROPOSED | T3 index closed |
| LPCI1-T5 | Chatbot Prototype | local UI/API with operator-provided LLM API key, citations, answer class, audit receipt | PROPOSED | T4 retrieval reviewed |
| LPCI1-T6 | Adversarial Evaluation | 5-10 source-sampled checks per corpus class, false-direct-answer audit | PROPOSED | T5 prototype |
| LPCI1-T7 | Template Packaging | downstream workspace guide, corpus intake template, readiness checklist | PROPOSED | T6 evaluation reviewed |

---

## T1 Scope (immediate next tranche)

LPCI1-T1 covers product intake and architecture only. Outputs must include:

1. Architecture document naming:
   - corpus intake pipeline design (local file import, manifest, hash);
   - classification pipeline design (GC-050 aligned, CI2 field schema);
   - retrieval and answer boundary design (citation-first, abstention);
   - API / UI surface sketch (no implementation).

2. T1 GC-018 supplement that acknowledges NR-04/NR-05/NR-11 gaps per
   CI1-T7 obligations.

3. Corpus intake spec citing CI2-T4 inherited gaps and stating whether
   per-file hash or manifest proxy is adopted for LPCI.

LPCI1-T1 does not implement any code. Runtime artifacts (routes, components,
vector DB, provider calls) remain blocked until T1 architecture review passes.

---

## Work Plan

| Step | Tranche | Primary action | Dependency | Output status |
| --- | --- | --- | --- | --- |
| W1 | LPCI1-T1 | Product intake and architecture | CI2-T5 closure + operator commit | HOLD until dependency-release refresh after CI2-T5 commit |
| W2 | LPCI1-T2 | Domain classification | T1 architecture review closed | PROPOSED |
| W3 | LPCI1-T3 | Search and filter index | T2 classification closed | PROPOSED |
| W4 | LPCI1-T4 | Retrieval boundary | T3 index closed | PROPOSED |
| W5 | LPCI1-T5 | Chatbot prototype | T4 retrieval reviewed | PROPOSED |
| W6 | LPCI1-T6 | Adversarial evaluation | T5 prototype | PROPOSED |
| W7 | LPCI1-T7 | Template packaging | T6 evaluation reviewed | PROPOSED |

---

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| LPCI1-T1 architecture reviewed | architecture document, corpus intake spec, and T1 GC-018 supplement closed |
| No runtime before T1 gate | zero UI/API/vector/provider files created before T1 passes |
| Legal corpus GC-051 registered | target corpus in registry before T2 scan |
| CI2 checkers pass for all LPCI packets | NR-04/NR-05/NR-11 autorun gates COMPLIANT for every LPCI corpus packet |
| Claim boundary preserved per tranche | no tranche claims beyond its accepted answer classes |
| Adversarial evaluation present (T6) | at least 5 source-sampled checks per corpus class |

---

## Blocked Scope (all tranches)

| Blocked work | Blocking condition |
| --- | --- |
| Runtime UI/API/route | T1 architecture review + fresh work order |
| Vector DB schema or embedding pipeline | T3 index design + fresh work order |
| Live provider query | T4 retrieval boundary + fresh work order |
| New corpus beyond pilot roots | GC-051 registration per corpus |
| Legal advice claims | OUT OF SCOPE permanently |
| Public-sync | Separate authorization per CVF public-sync rule |

---

## Domain Extension Fields (for LPCI corpus packets)

LPCI extends the CI2 enforced common fields with legal/policy domain fields.
These must be populated when a real legal corpus is ingested (T2 onwards):

| Field | Purpose |
| --- | --- |
| `jurisdiction` | country, state, company, org scope |
| `authorityLevel` | hierarchy or internal rank |
| `issuingBody` | ministry, department, company function, owner team |
| `effectiveDate` | date the rule starts applying |
| `status` | effective, draft, amended, superseded, repealed, obsolete, unknown |
| `documentType` | law, decree, circular, policy, notice, decision, SOP, contract, other |

These fields are inherited from the `legalPolicy` domain extension group
defined in `docs/corpus-intelligence/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL.json`.

---

## Decision

Authorize LPCI1 tranches T1–T7 in sequence per this roadmap. Each tranche
requires a separate work order. No tranche may begin before the prior tranche's
completion review is closed.

First dependency-gated dispatch candidate: LPCI1-T1 via
`docs/work_orders/CVF_WO_LPCI1_T1_PRODUCT_INTAKE_AND_ARCHITECTURE_2026-06-02.md`.

---

## Alternatives

| Alternative | Reason not chosen |
| --- | --- |
| Skip architecture review (T1) and start chatbot implementation directly | Rejected — no-runtime-until-T1 gate in GC-018 baseline |
| Use a single large work order for all LPCI | Rejected — tranche separation enforces claim boundary at each stage |
| Treat CI2-T4 pilot pack as the production corpus | Rejected — pilot pack is governance proof only; a real legal corpus must be separately registered |

---

## Consequences

| Consequence | Effect |
| --- | --- |
| LPCI1-T1 work order exists but remains dependency-gated | Architecture intake may begin only after CI2-T5 closure is committed and the T1 work order is released with closure-commit evidence |
| T2–T7 are blocked until prior tranche reviews close | Staged gate prevents premature implementation claims |
| Legal corpus intake requires GC-051 registration | No ad-hoc corpus expansion |
| CI2 checkers enforce all LPCI corpus packets | NR-04/NR-05/NR-11 violations will block autorun workflow gates |

---

## Claim Boundary

This roadmap authorizes planning and staged architecture intake. It does NOT:

- implement any LPCI runtime artifact;
- claim legal answer correctness or production readiness;
- authorize vector database, embedding, or provider calls;
- claim public or hosted readiness.

---

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP` — no LPCI1 MVP roadmap existed to convert CI2
enforcement readiness into staged implementation authorization

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `RULE_ADDED` — LPCI1 MVP roadmap establishes 7-tranche
implementation plan with dependencies, blocked scope, domain extension
fields, and T1 dispatch authorization

Next control action: `OPEN` — LPCI1-T1 dependency-release refresh is the immediate next move

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: this roadmap is a governance planning artifact only.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: roadmap references internal governance chain details and private
corpus pilot evidence; not suitable for the public CVF repository at this stage.

Public-sync boundary: no artifacts from this batch are queued for public-sync.
Next public-sync action: a public-facing LPCI product overview could be
prepared separately after T1 architecture review.
