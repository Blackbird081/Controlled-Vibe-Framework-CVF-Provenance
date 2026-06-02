# CVF CI1 Corpus Intelligence Operationalization Roadmap

Memory class: SUMMARY_RECORD

Status: T1_COMPLETE_T2_REVIEWED_T3_CLOSED_PASS_BOUNDED_T4_COMPLETE_PENDING_REVIEW

docType: roadmap

Date: 2026-06-02

GC-018: `docs/baselines/CVF_GC018_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_2026-06-02.md`

## Purpose

Turn CVF corpus intelligence from a set of standards and guards into an
operational workflow that future agents can execute across arbitrary corpora.

CI1 is the bridge between the now-closed Memory plane and the next practical
corpus work: legacy deep rescans, user project corpora, source-doc search,
company policy corpora, and the LPCI legal/policy chatbot product.

## Authorization / Decision

Authority:

- operator direction on 2026-06-02 to continue Corpus Intelligence after Memory
  plane closure;
- `docs/baselines/CVF_GC018_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_2026-06-02.md`;
- `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`;
- `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`;
- active GC-047, GC-048, GC-049, and GC-050 guard chain.

Decision: begin with CI1-T1, a readiness packet template and dispatch workflow.
Do not start another broad legacy scan until this operating packet exists.

## Scope / Target / Owner Boundary

Target:

- a repeatable CVF workflow for corpus discovery, search/filter readiness,
  knowledge-map reconciliation, intelligence classification, and adversarial
  sampling.

CVF owns:

- standards, packet templates, dispatch rules, guard wiring, evidence blocks,
  and closure criteria.

Corpus owners own:

- source corpus truth, domain judgment, semantic correctness review, and
  authority/currentness decisions.

Out of scope:

- broad legacy rescan execution;
- vector database or retrieval runtime implementation;
- LPCI product implementation;
- public-sync;
- production readiness or legal advice claims.

## Non-Goals

- do not reopen Memory plane implementation;
- do not scan `.private_reference/legacy/` in CI1-T1;
- do not create a vector database, embedding pipeline, or runtime retrieval
  route;
- do not implement the LPCI legal/policy chatbot product in this roadmap;
- do not claim semantic correctness from machine gates;
- do not change public-sync or public README surfaces;
- do not claim production, hosted, or public readiness.

## Current State

| Layer | Artifact | Status |
| --- | --- | --- |
| Source corpus completeness | GC-047 standard and checker | ACTIVE |
| Knowledge-map reconciliation | GC-048 standard and checker | ACTIVE |
| Core guard self-protection | GC-049 guard and checker | ACTIVE |
| Intelligence classification | GC-050 standard, guard, and checker | ACTIVE |
| Search/filter readiness | `CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | ACTIVE STANDARD |
| Memory/KGR/MKE substrate | MKG7, KGR1, MKE1 | CLOSED_PASS_BOUNDED |
| LPCI product target | LPCI roadmap | PROPOSED PRODUCT ROADMAP |

## Tranche Plan

| Tranche | Goal | Primary outputs | Status |
| --- | --- | --- | --- |
| CI1-T1 | Readiness Packet Template | canonical packet template, dispatch checklist, work order | CLOSED_PASS_BOUNDED |
| CI1-T2 | Legacy Rescan Pilot — Graphify | apply CI1-T1 packet to `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/` (5 files) | COMPLETE_PENDING_REVIEW |
| CI1-T3 | Legacy Rescan Pilot 2 - Graph Governance | apply CI1 workflow to `.private_reference/legacy/CVF ADD/code-review-graph/` (7 files) and route findings through GC-051/GC-052 | CLOSED_PASS_BOUNDED |
| CI1-T4 | Cross-Corpus Index Model | normalize search/filter facets across at least two real CI1 scan packets | COMPLETE_PENDING_REVIEW |
| CI1-T5 | Classification Sampling Protocol | adversarial sampling protocol over the T4 model with accepted/deferred/rejected/zero-result rows | HOLD_UNTIL_T4_CLOSED |
| CI1-T6 | Checker Decision | decide whether T5 findings justify a structural machine checker | HOLD_UNTIL_T5_CLOSED |
| CI1-T7 | LPCI Intake Bridge | map the T4/T5/T6 corpus-intelligence chain into LPCI-T1 product intake | HOLD_UNTIL_T6_DECIDED |

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| C1.0 | Open CI1 GC-018 | baseline | DONE |
| C1.1 | Dispatch CI1-T1 | work order | DONE |
| C1.2 | Create packet template | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | DONE — committed `662b673b` |
| C1.3 | Open CI1-T2 GC-018 for Graphify pilot | `docs/baselines/CVF_GC018_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_2026-06-02.md` | DONE |
| C1.4 | Dispatch CI1-T2 work order | `docs/work_orders/CVF_WO_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_2026-06-02.md` | DISPATCHED |
| C1.5 | Worker executes CI1-T2 — fills packet + completion review | readiness packet + review | COMPLETE_PENDING_REVIEW |
| C1.6 | Review CI1-T2 output and select CI1-T3 scope | selected `CVF ADD/code-review-graph/` after count correction to 7 files | DONE |
| C1.7 | Open CI1-T3 GC-018 | `docs/baselines/CVF_GC018_CI1_T3_GRAPH_GOVERNANCE_CORPUS_DEEP_SCAN_2026-06-02.md` | DONE |
| C1.8 | Dispatch CI1-T3 work order | `docs/work_orders/CVF_WO_CI1_T3_GRAPH_GOVERNANCE_CORPUS_DEEP_SCAN_2026-06-02.md` | DONE |
| C1.9 | Worker executes CI1-T3 — fills packet, finding packet, registry, completion review | readiness packet + review + GC-051 entry | CLOSED_PASS_BOUNDED |
| C1.10 | Reviewer commits CI1-T3 and runs committed-range closure | `7c068eeb` + handoff-sync `b0d0249c` | DONE |
| C1.11 | Open CI1-T4 GC-018 | `docs/baselines/CVF_GC018_CI1_T4_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md` | DONE |
| C1.12 | Dispatch CI1-T4 work order | `docs/work_orders/CVF_WO_CI1_T4_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md` | DONE |

## CI1-T1 Expected Packet Shape

CI1-T1 must create a reusable packet template containing:

- source corpus boundary;
- filesystem discovery index;
- GC-047 corpus completeness block;
- GC-048 knowledge-map reconciliation block;
- corpus search/filter readiness block;
- GC-050 corpus intelligence classification block;
- negative search evidence table;
- derived trace table;
- query receipt model;
- adversarial sampling plan;
- acceptance/defer/reject disposition matrix;
- claim/final/verification boundary.

## Acceptance Criteria

- CI1-T1 produces a template that future workers can fill without inventing
  section names.
- The template names required commands and evidence for GC-047, GC-048, and
  GC-050.
- The template requires negative search evidence before any "not found" claim.
- The template separates generic search/filter fields from domain extensions.
- The template states that semantic correctness remains review/adversarial
  sampling, not machine-gate proof.
- No CI1 artifact claims legacy scan completion, LPCI implementation,
  production readiness, or public readiness.

## Verification / Evidence

CI1-T1 must run:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_core_guard_self_protection.py --enforce
```

If a future T2 pilot reads an actual corpus, it must also run:

```powershell
python governance/compat/check_corpus_completeness_report_integrity.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base <baseHead> --head HEAD --enforce
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI1 is private governance and corpus-intelligence operating workflow
work. No public-sync remote, public repository commit, public artifact path,
hosted proof, or public README claim is included.

## Claim Boundary

CI1 creates the operating discipline for future corpus intelligence work. It
does not perform a new legacy rescan, certify semantic correctness, build a
runtime retrieval index, implement LPCI, or claim production/public readiness.

## Dependency Lock

- CI1-T5 may be dispatched only after CI1-T4 produces the JSON cross-corpus
  index model and completion review.
- CI1-T6 may be dispatched only after CI1-T5 closes with reviewed sampling
  evidence.
- CI1-T7 may be dispatched only after CI1-T6 completes and returns an explicit
  checker decision.
- LPCI-T1 may not dispatch until CI1-T7 closes.
