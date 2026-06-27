# CVF GC-018 - DICE-T0 Document Intelligence Control Envelope Contract Matrix

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `bea8e1f1`

sourceAuthority:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md`

parentRoadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`

predecessorTranche:
`docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md`

## Purpose

Authorize DICE-T0 as a doc-only CVF foundation tranche. Claude must create a
Document Intelligence Control Envelope contract matrix that maps current
extraction foundation and DIR owner surfaces into a reusable document-control
envelope without implementing runtime behavior.

## Scope / Target / Owner Boundary

Target: one reference contract matrix and one worker-return packet.

Owner boundary: Codex owns orchestration, dispatch, review, commit, and later
session-state sync. Claude owns only the DICE-T0 worker artifacts under
`WORKER_MUST_NOT_COMMIT`.

## Decision / Baseline / Proposed Tranche

Decision: open DICE-T0 after DIR-T2 closure because the next foundation need is
not another use-case lane. It is a reusable control envelope that prevents
downstream document workflows from redefining route, confidence, provider/OCR,
operator-review, or cost boundaries.

Baseline:

- current dispatch base: `bea8e1f1`;
- DIR-T2 material closure commit: `e3395acc`;
- DIR-T2 session-sync commit: `bea8e1f1`;
- parent roadmap:
  `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`.

Proposed tranche:

- create a DICE-T0 contract matrix under `docs/reference/`;
- create a DICE-T0 worker-return packet under `docs/reviews/`;
- return uncommitted artifacts for Codex review.

## Runtime Authorization

Authorized runtime scope: none.

This is a doc-only contract and source-map tranche. It authorizes no OCR,
provider/API call, retrieval execution, app execution, sample document
processing, external repo access, public-sync, or live-proof command.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| DIR-T2 foundation pilot closed | `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md`; material closure commit `e3395acc` | ACCEPT |
| DIR-T2 session state synchronized | current dispatch base `bea8e1f1` | ACCEPT |
| Operator selected foundation lane | 2026-06-13 operator instruction to open next CVF foundation roadmap and Claude work order | ACCEPT |
| Fresh DICE roadmap exists | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md` | ACCEPT |
| Fresh work order exists | paired DICE-T0 Claude work order | ACCEPT |

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | DICE-T0 builds on closed DIR-T0/T1/T2 artifacts and current extraction foundation source | COMPLETE |
| Detailed source files read | source verification below covers router, scan route, extraction quality, and scan outcome surfaces | COMPLETE |
| Current owner surfaces checked | DICE-T0 must separate extraction quality, scan route, DIR authorization, and operator report ownership | COMPLETE |
| Accept/defer/reject dispositions recorded | required in the paired work order's worker deliverables | COMPLETE |
| Adversarial role review applied | paired work order requires use-case drift, provider/OCR drift, and confidence redefinition checks | COMPLETE |
| Blind-spot delta | no external app tree, provider service, OCR service, or sample document is in scope | COMPLETE |

Verdict: `COMPLETE_WITH_DECLARED_BOUNDARIES`.

## Rescan Intelligence Hardening

- Original source artifact: closed DIR-T0/T1/T2 artifacts and current
  extraction foundation source, not the external Document Translator repo.
- Predecessor intake artifact:
  `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md`.
- Delta ledger status: DISPATCH_DECLARED_LIMITS - DICE-T0 is released only as
  a doc-only contract matrix and worker-return packet.
- Routing matrix status: DISPATCH_DECLARED_LIMITS - OCR/provider, retrieval,
  external use-case repos, public-sync, and readiness claims remain out of
  scope.
- Semantic sampling status: DISPATCH_DECLARED_LIMITS - worker must source-map
  current owner surfaces and reject duplicate confidence/route/provider
  ownership.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| sampleId | Delta category | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| DICE-T0-GC018-D1 | NEW_FINDING | DIR-T2 completion | DIR foundation pilot is closed | DICE opens one envelope layer above DIR | Could this reopen DIR source? | PASS |
| DICE-T0-GC018-D2 | CHANGED_DISPOSITION | active next move | operator may select another foundation lane | DICE-T0 selected and bounded | Could this become DT-CVF-T0? | PASS |
| DICE-T0-GC018-D3 | UNCHANGED_FROM_INTAKE | DT-CVF roadmap boundary | Document Translator remains downstream | external tree access forbidden | Could app claims leak into foundation proof? | PASS |
| DICE-T0-GC018-D4 | REMOVED_OR_REJECTED | runtime/provider pressure | OCR/provider/cost routes need separate authorization | DICE-T0 doc-only matrix | Could Claude run provider/OCR proof? | PASS |

### Follow-Up Routing Matrix

| Route lane | Target | Disposition | Evidence | Next action |
| --- | --- | --- | --- | --- |
| DO_NOW | DICE-T0 doc-only contract matrix and worker return | ACCEPT | this GC-018 plus paired work order | Claude executes allowed artifacts |
| SEPARATE_RUNTIME_TRANCHE | runtime source, OCR, provider/API, retrieval, live proof | DEFER | runtime authorization boundary | fresh operator authorization required |
| STRATEGIC_OPERATOR_DECISION | DT-CVF-T0, Policy_Local PL-S1, public-sync, readiness, cost, quality | DEFER | active parked checkpoints | operator decision later |
| OUT_OF_SCOPE | external Document Translator and Policy_Local tree operations | REJECT | forbidden path manifest | no read, list, hash, modify, or import |
| RESOLVED_BY_DESIGN | worker commits | REJECT | `WORKER_MUST_NOT_COMMIT` | Codex reviews and commits |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| DICE-T0-GC018-S1 | extraction pipeline | extraction quality owns confidence fields | matrix must reject confidence redefinition | Could DICE invent new confidence semantics? | PASS |
| DICE-T0-GC018-S2 | scan route source | EXA-T2 owns scan route disposition | matrix must consume, not duplicate | Could DICE reissue scan route values? | PASS |
| DICE-T0-GC018-S3 | DIR router source | DIR owns authorization gate | matrix must consume DIR gates | Could DICE bypass operator review gates? | PASS |
| DICE-T0-GC018-S4 | scan outcome report | scan report owns current operator-visible scan outcome | matrix must map rather than replace | Could DICE obscure operator action? | PASS |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: DIR route version | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 25 | `DOCUMENT_INTELLIGENCE_ROUTE_VERSION` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR claim boundary | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 27 | `CLAIM_BOUNDARY` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR authorization gate | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 35 | `AuthorizationGate` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR downstream capability | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 43 | `DownstreamCapability` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR document profile | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 68 | `DocumentProfile` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR structure signals | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 86 | `DocumentStructureSignals` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR route decision | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 105 | `DocumentIntelligenceRouteDecision` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR route function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 139 | `decide_document_intelligence_route` | DIR-T1 router module | ACCEPT |
| EXISTS: EXA-T2 scan route version | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 20 | `SCAN_ROUTE_DECISION_VERSION` | EXA-T2 scan-route module | ACCEPT |
| EXISTS: EXA-T2 scan disposition | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 31 | `ScanRouteDisposition` | EXA-T2 scan-route module | ACCEPT |
| EXISTS: EXA-T2 scan signals | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 40 | `DocumentScanSignals` | EXA-T2 scan-route module | ACCEPT |
| EXISTS: EXA-T2 scan function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 71 | `decide_scan_route` | EXA-T2 scan-route module | ACCEPT |
| EXISTS: extraction quality report | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 101 | `ExtractionQualityReport` | extraction pipeline | ACCEPT |
| EXISTS: OCR confidence owner field | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 111 | `mean_ocr_confidence` | extraction quality report | ACCEPT |
| EXISTS: extraction quality evaluator | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 235 | `evaluate_extraction_quality` | extraction pipeline | ACCEPT |
| EXISTS: operator scan outcome report | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 43 | `ScanOutcomeReport` | scan outcome report module | ACCEPT |
| EXISTS: operator scan report renderer | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 217 | `render_scan_outcome_report_markdown` | scan outcome report module | ACCEPT |
| EXISTS: DIR-T2 completion | `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md` | Status line | `CLOSED_PASS_BOUNDED` | DIR-T2 completion review | ACCEPT |

## Authorized Artifact Set

Claude may create or update only:

- `docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md`;
- `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`;
- the paired work order only if adding worker-return evidence is necessary.

## Required Contract Matrix Contents

The DICE-T0 matrix must include:

- source-owned envelope role map;
- accepted, deferred, and rejected boundary table;
- provider/OCR/cost authorization boundary;
- operator-visible review packet boundary;
- downstream adapter consumption boundary for Document Translator and
  Policy_Local without reading either tree;
- machine-check candidate table for DICE-T1;
- finding-to-governance learning disposition;
- public export disposition;
- claim boundary.

## Evidence / Verification

Required dispatch verification:

- work-order dispatch quality checker passes on the dispatch package;
- pre-dispatch autorun gate passes on the real changed range;
- pre-commit governance chain passes before Codex commits.

Required worker verification is defined in the paired work order.

## Claim Boundary

This GC-018 authorizes doc-only DICE-T0 contract matrix work. It does not
authorize runtime implementation, provider/OCR execution, external app tree
inspection, retrieval behavior change, corpus ingestion, public-sync, document
correctness claims, extraction accuracy claims, provider quality claims,
readiness claims, cost claims, memory reinjection, high-risk promotion, or
autonomous mutation.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This is a private provenance dispatch baseline. No public-sync artifact or
public catalog claim is authorized.
