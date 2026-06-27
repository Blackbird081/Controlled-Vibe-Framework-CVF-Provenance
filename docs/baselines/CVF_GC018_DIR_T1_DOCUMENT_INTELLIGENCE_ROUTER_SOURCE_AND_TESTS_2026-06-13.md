# CVF GC-018 - DIR-T1 Document Intelligence Router Source And Tests

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-13

Owner: Claude (orchestrator for this tranche)

Assigned worker: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `e426d983`

sourceAuthority:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_FOR_CODEX_2026-06-13.md`

parentRoadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

predecessorTranche:
`docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`

## Purpose

Authorize DIR-T1 as a bounded deterministic local source implementation tranche
for the Document Intelligence Router foundation. The worker may implement a
small deterministic router module plus focused tests that compose the existing
EXA-T2 scan-route contracts exactly as specified in the DIR-T0 contract matrix.

This tranche does not authorize OCR execution, provider/API use, retrieval
changes, corpus ingestion, external Document Translator or Policy_Local tree
inspection, public-sync, readiness, cost, quality, memory reinjection,
high-risk promotion, or autonomous mutation.

## Scope / Target / Owner Boundary

Target: one new deterministic router source module, its focused test file, and
one governance checker that proves the router authorization gate does not
overlap scan dispositions, plus the two worker-return review artifacts.

Owner boundary: Claude owns this tranche's orchestration, review, closure, and
session-state sync. Codex owns worker implementation artifacts under
`WORKER_MUST_NOT_COMMIT` and must return them uncommitted for Claude review.

Role inversion note: in DIR-T0 Codex was orchestrator and Claude was worker.
For DIR-T1 the roles invert: Claude orchestrates and reviews; Codex implements.
This is an authorized intentional role swap, not a governance drift.

## Decision / Baseline / Proposed Tranche

Decision: open DIR-T1 from the finalized Document Intelligence Router roadmap
after the DIR-T0 contract matrix reached its bounded-pass closure (status
recorded in the DIR-T0 contract matrix header and Dependency Release Evidence).

Baseline:

- DIR final roadmap session-sync commit: `51cd1ded`.
- DIR-T0 dispatch commit: `e19d725d`.
- DIR-T0 closure commit: `082b02ff`.
- DIR-T0 closure session-sync commit: `e426d983` (current dispatch base).
- DIR-T0 contract matrix status: closed bounded-pass (see Dependency Release
  Evidence row for the exact status token).
- Current scan-route owner surface remains
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`.
- Current extraction quality and scan-outcome owner surfaces remain
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` and
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`.

Authorized tranche:

- add `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py`;
- add `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py`;
- add `governance/compat/check_dir_disposition_no_scan_overlap.py`;
- add a DIR-T1 worker-return packet under `docs/reviews/`;
- update the parent roadmap DIR-T1 row only to mark worker-return status, not
  final closure;
- return uncommitted artifacts to Claude for review and commit.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| DIR-T0 contract matrix closed | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`; status `CLOSED_PASS_BOUNDED`; closure commit `082b02ff` | ACCEPT |
| DIR-T0 worker return accepted | `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`; status `WORKER_RETURN_ACCEPTED_BY_CODEX` | ACCEPT |
| Final roadmap holds DIR-T1 behind fresh GC-018 | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`; DIR-T1 status `AWAITING_FRESH_AUTHORIZATION` | ACCEPT |
| Session state synchronized DIR-T0 closure | current HEAD before dispatch `e426d983` | ACCEPT |
| Fresh DIR-T1 authorization | this GC-018 baseline and the paired Codex work order | ACCEPT |

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | DIR-T1 builds only on the closed DIR-T0 contract matrix and source-verified EXA-T2/EX-T9 surfaces | COMPLETE |
| Detailed source files read | scan route, extraction pipeline, scan outcome report, and DIR-T0 contract matrix are source-verified below | COMPLETE |
| Current owner surfaces checked | Source Verification Block separates existing source from the new router module | COMPLETE |
| Accept/defer/reject dispositions recorded | Source Verification and Authorized Artifact Set tables below | COMPLETE |
| Adversarial role review applied | DIR-T0 contract matrix already incorporated Claude rebuttal B1-B4; DIR-T1 implements exactly those resolved contracts | COMPLETE |
| Blind-spot delta | no external tree scan, OCR/provider action, retrieval change, or downstream use-case edit is authorized | COMPLETE |

Verdict: `COMPLETE_WITH_DECLARED_BOUNDARIES`.

## Rescan Intelligence Hardening

- Original source artifact: closed DIR-T0 contract matrix and current EXA-T2/
  EX-T9 extraction foundation source, not the external Document Translator repo.
- Predecessor intake artifact:
  `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`
  and
  `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`.
- Delta ledger status: DISPATCH_DECLARED_LIMITS - T1 is released only as a
  deterministic local source module, focused tests, and one overlap checker.
- Routing matrix status: DISPATCH_DECLARED_LIMITS - OCR/provider, retrieval,
  external use-case repos, public-sync, and readiness claims remain out of scope.
- Semantic sampling status: DISPATCH_DECLARED_LIMITS - worker must source-verify
  EXA-T2 values instead of retyping them, and prove gate/disposition disjointness.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| sampleId | Delta category | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| DIR-T1-GC018-D1 | UNCHANGED_FROM_INTAKE | roadmap DIR-T1 detail | DIR-T1 requires fresh GC-018 and source-verified work order | this baseline plus paired work order | Did dispatch skip release evidence? | PASS |
| DIR-T1-GC018-D2 | CHANGED_DISPOSITION | roadmap tranche plan | DIR-T1 was awaiting fresh authorization | status moves to dispatch only | Did dispatch claim closure before worker return? | PASS |
| DIR-T1-GC018-D3 | NEW_FINDING | DIR-T0 contract matrix MC-1 | router gate must be disjoint from scan disposition | work order requires overlap checker plus disjoint test | Could the router retype scan dispositions? | PASS |
| DIR-T1-GC018-D4 | REMOVED_OR_REJECTED | external-tree boundary | no Document Translator or Policy_Local tree inspection | forbidden scope retained | Could the router import external use-case code? | PASS |

### Follow-Up Routing Matrix

| Route lane | Target | Disposition | Evidence | Next action |
| --- | --- | --- | --- | --- |
| DO_NOW | DIR-T1 router module, focused tests, overlap checker, worker return | ACCEPT | DIR-T0 contract matrix and roadmap DIR-T1 detail | Codex implements allowed artifacts |
| SEPARATE_RUNTIME_TRANCHE | OCR, provider, retrieval, or live proof | DEFER | roadmap DIR-T2 and claim boundary | fresh authorization after T1 closure |
| STRATEGIC_OPERATOR_DECISION | DT-CVF-T0, Policy_Local PL-S1, sample corpus, public-sync, readiness, cost, or quality claim | DEFER | active session parked checkpoint | operator decision later |
| OUT_OF_SCOPE | external Document Translator and Policy_Local tree operations | REJECT | roadmap external-tree boundary | no read, list, hash, modify, or import |
| RESOLVED_BY_DESIGN | worker commits | REJECT | `WORKER_MUST_NOT_COMMIT` | Claude reviews and commits |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| DIR-T1-GC018-S1 | scan route source | `ScanRouteDisposition` already owns scan route values | work order requires import, not retype | Could DIR retype scan dispositions? | PASS |
| DIR-T1-GC018-S2 | DIR-T0 contract matrix | `AuthorizationGate` must be disjoint from scan disposition | overlap checker required | Could a gate value collide with a scan value? | PASS |
| DIR-T1-GC018-S3 | DIR-T0 contract matrix | `DocumentStructureSignals` stays separate at T1 start | work order keeps structure separate unless tests prove no variation | Could structure be silently folded? | PASS |
| DIR-T1-GC018-S4 | roadmap DIR-T1 acceptance boundary | no raw text, OCR, provider, or readiness claim | claim boundary plus test boundary | Could the module execute OCR or providers? | PASS |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: scan route version | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 20 | `SCAN_ROUTE_DECISION_VERSION` | EXA-T2 scan route module | ACCEPT |
| EXISTS: scan route disposition owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 31 | `ScanRouteDisposition` | EXA-T2 scan route module | ACCEPT |
| EXISTS: scan signal contract | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 40 | `DocumentScanSignals` | EXA-T2 scan route module | ACCEPT |
| EXISTS: scan route decision contract | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 58 | `ScanRouteDecision` | EXA-T2 scan route module | ACCEPT |
| EXISTS: route decision function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 71 | `decide_scan_route` | EXA-T2 scan route module | ACCEPT |
| EXISTS: extraction status owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 27 | `ExtractionStatus` | extraction pipeline | ACCEPT |
| EXISTS: extraction quality report | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 101 | `ExtractionQualityReport` | extraction pipeline | ACCEPT |
| EXISTS: test import pattern | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py` | lines 5-18 | `sys.path.insert` plus bare module import | EXA-T2 test convention | ACCEPT |
| EXISTS: DIR-T0 contract matrix closed | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | Status line | `CLOSED_PASS_BOUNDED` | DIR-T0 contract matrix | ACCEPT |
| PROPOSED: router authorization gate | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | AuthorizationGate table | `AuthorizationGate` | DIR-T0 contract matrix Contract 3 | ACCEPT_AS_DOC_ONLY_TO_IMPLEMENT |
| PROPOSED: gate derivation map | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | AuthorizationGate Derivation Table | total map from 4 scan values | DIR-T0 contract matrix Contract 3 | ACCEPT_AS_DOC_ONLY_TO_IMPLEMENT |

## New Source And Test Symbols Authorized

These names are authorized for DIR-T1 runtime implementation, sourced from the
closed DIR-T0 contract matrix. They become runtime symbols in this tranche.

| New symbol | DIR-T0 contract source | Target file | Boundary |
| --- | --- | --- | --- |
| `DOCUMENT_INTELLIGENCE_ROUTE_VERSION` | matrix Contract 3 `decision_version` | `document_intelligence_router.py` | router contract version constant, distinct from scan route version |
| `AuthorizationGate` | matrix Contract 3 AuthorizationGate table | `document_intelligence_router.py` | router-owned Literal; must be disjoint from `ScanRouteDisposition` |
| `DownstreamCapability` | matrix Contract 4 | `document_intelligence_router.py` | capability-shaped Literal; no use-case name values |
| `DocumentProfile` | matrix Contract 1 | `document_intelligence_router.py` | frozen dataclass; no raw text fields |
| `DocumentStructureSignals` | matrix Contract 2 | `document_intelligence_router.py` | frozen dataclass kept separate at T1 start |
| `DocumentIntelligenceRouteDecision` | matrix Contract 3 | `document_intelligence_router.py` | frozen dataclass; scan route passthrough plus authorization gate |
| `decide_document_intelligence_route` | matrix Contract 3 derivation table | `document_intelligence_router.py` | deterministic function composing `decide_scan_route` or a supplied `ScanRouteDecision` |

## Authorized Artifact Set

Codex may create or update only:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py`;
- `governance/compat/check_dir_disposition_no_scan_overlap.py`;
- `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_WORKER_RETURN_2026-06-13.md`;
- the paired work order only if adding worker-return evidence is necessary;
- the parent roadmap DIR-T1 row only to mark worker-return status, not final
  closure.

## Evidence / Verification

Required dispatch verification:

- work-order dispatch quality checker passes on the dispatch package;
- pre-dispatch autorun gate passes on the real changed range;
- reviewer-fast and pre-commit gates pass before Claude commits.

Required worker verification is defined in the paired work order.

## Claim Boundary

This GC-018 authorizes bounded DIR-T1 deterministic source and test work only.
It does not claim document intelligence behavior is validated against real
documents, scan/extraction accuracy is improved, OCR/provider behavior is
available, retrieval behavior changed, Policy_Local is ready, Document
Translator is ready, public catalog export exists, release proof exists, memory
reinjection is authorized, high-risk promotion is authorized, or autonomous
mutation is authorized.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This is a private provenance dispatch baseline. No public-sync artifact or
public catalog claim is authorized by this tranche.
