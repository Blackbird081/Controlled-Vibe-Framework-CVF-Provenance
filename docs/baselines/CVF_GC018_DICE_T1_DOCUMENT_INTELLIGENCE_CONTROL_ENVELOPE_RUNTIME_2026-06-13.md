# CVF GC-018 - DICE-T1 Document Intelligence Control Envelope Runtime

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `579962d7`

sourceAuthority:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_FOR_CLAUDE_2026-06-13.md`

parentRoadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`

predecessorTranche:
`docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`

## Purpose

Authorize DICE-T1 as a bounded local deterministic CVF foundation tranche.
Claude must implement a Document Intelligence Control Envelope module and
focused tests that compose existing EXA-T2 scan-route, scan outcome report,
and DIR route-decision owner surfaces without redefining their semantics.

## Scope / Target / Owner Boundary

Target: one runtime source module, one focused test module, and one worker
return packet.

Owner boundary: Codex owns orchestration, dispatch, review, commit, and later
session-state sync. Claude owns only the DICE-T1 allowed artifacts under
`WORKER_MUST_NOT_COMMIT`.

## Decision / Baseline / Proposed Tranche

Decision: open DICE-T1 after DICE-T0 closed `CLOSED_PASS_BOUNDED` and after
Codex promoted the DICE-T0 orchestrator findings into dispatch-quality
hardening.

Baseline:

- current dispatch base: `579962d7`;
- DICE-T0 material closure commit: `a355cd7a`;
- DICE-T0 session-sync commit: `bd3c9f7c`;
- DICE-T0 finding-promotion hardening commit: `dbe3ddca`;
- handoff sync after hardening: `579962d7`;
- parent roadmap:
  `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`.

Proposed tranche:

- create `document_intelligence_control_envelope.py`;
- create focused tests for the envelope contract and DICE-MC-01 through
  DICE-MC-10;
- create a DICE-T1 worker-return packet;
- return uncommitted artifacts for Codex review.

## Runtime Authorization

Authorized runtime scope: local deterministic source and tests only under
`EXTENSIONS/CVF_EXTRACTION_FOUNDATION`.

This baseline authorizes no OCR execution, provider/API call, retrieval
execution, app execution, sample document processing, external repo access,
public-sync, or live-proof command.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| DICE-T0 closed | `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`; material closure commit `a355cd7a` | ACCEPT |
| DICE-T0 session state synchronized | session-sync commit `bd3c9f7c` | ACCEPT |
| DICE-T0 finding promotion completed | source-anchor hardening commit `dbe3ddca`; handoff sync `579962d7` | ACCEPT |
| Operator selected next work order | 2026-06-13 operator instruction to continue and create Claude work order | ACCEPT |
| Fresh DICE-T1 work order exists | paired DICE-T1 Claude work order | ACCEPT |

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | DICE-T1 builds on DICE-T0 contract matrix and current extraction foundation source | COMPLETE |
| Detailed source files read | source verification below covers router, scan route, extraction quality, and scan outcome surfaces | COMPLETE |
| Current owner surfaces checked | DICE-T1 must compose existing owner surfaces and must not redefine their literal values | COMPLETE |
| Accept/defer/reject dispositions recorded | paired work order requires DICE-MC proof rows and negative evidence | COMPLETE |
| Adversarial role review applied | paired work order requires use-case drift, provider/OCR drift, and DICE-MC-08 passthrough checks | COMPLETE |
| Blind-spot delta | no external app tree, provider service, OCR service, sample document, retrieval, or public-sync is in scope | COMPLETE |

Verdict: `COMPLETE_WITH_DECLARED_BOUNDARIES`.

## Rescan Intelligence Hardening

- Original source artifact: closed DICE-T0 matrix and current extraction
  foundation source, not the external Document Translator repo.
- Predecessor intake artifact:
  `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`.
- Delta ledger status: DISPATCH_DECLARED_LIMITS - DICE-T1 is released only as
  local deterministic source, tests, and worker-return packet.
- Routing matrix status: DISPATCH_DECLARED_LIMITS - OCR/provider, retrieval,
  external use-case repos, public-sync, and readiness claims remain out of
  scope.
- Semantic sampling status: DISPATCH_DECLARED_LIMITS - worker must compose
  current owner surfaces and reject duplicate confidence/route/provider
  ownership.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| sampleId | Delta category | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| DICE-T1-GC018-D1 | NEW_FINDING | DICE-T0 matrix | DICE-MC-01 through DICE-MC-10 are candidates | DICE-T1 implements focused local proofs | Could this become broad runtime governance? | PASS |
| DICE-T1-GC018-D2 | CHANGED_DISPOSITION | DICE-T0 closure | DICE-MC-08 needs passthrough handling | DICE-T1 fixtures must preserve existing DIR invariant | Could the checker reject current behavior? | PASS |
| DICE-T1-GC018-D3 | UNCHANGED_FROM_INTAKE | DT-CVF boundary | Document Translator remains downstream | external tree access forbidden | Could app claims leak into foundation proof? | PASS |
| DICE-T1-GC018-D4 | REMOVED_OR_REJECTED | runtime/provider pressure | OCR/provider/cost routes need separate authorization | DICE-T1 local only | Could Claude run provider/OCR proof? | PASS |

### Follow-Up Routing Matrix

| Route lane | Target | Disposition | Evidence | Next action |
| --- | --- | --- | --- |
| DO_NOW | DICE-T1 local source, tests, worker return | ACCEPT | this GC-018 plus paired work order | Claude executes allowed artifacts |
| SEPARATE_RUNTIME_TRANCHE | OCR/provider/API, retrieval, live proof, app route wiring | DEFER | runtime authorization boundary | fresh operator authorization required |
| STRATEGIC_OPERATOR_DECISION | DT-CVF-T0, Policy_Local PL-S1, public-sync, readiness, cost, quality | DEFER | active parked checkpoints | operator decision later |
| OUT_OF_SCOPE | external Document Translator and Policy_Local tree operations | REJECT | forbidden path manifest | no read, list, hash, modify, or import |
| RESOLVED_BY_DESIGN | worker commits | REJECT | `WORKER_MUST_NOT_COMMIT` | Codex reviews and commits |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- |
| DICE-T1-GC018-S1 | extraction pipeline | extraction quality owns confidence fields | envelope must not add a second confidence threshold | Could DICE invent confidence semantics? | PASS |
| DICE-T1-GC018-S2 | scan route source | EXA-T2 owns scan route disposition | envelope must consume, not duplicate | Could DICE reissue scan route values? | PASS |
| DICE-T1-GC018-S3 | DIR router source | DIR owns authorization gate and downstream capability | envelope must consume DIR gates | Could DICE bypass operator review gates? | PASS |
| DICE-T1-GC018-S4 | scan outcome report | scan report owns operator-visible scan findings | envelope must preserve findings and review requirement | Could DICE suppress operator action? | PASS |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: DICE-T0 matrix closed | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md` | Status line | `CLOSED_PASS_BOUNDED` | DICE-T0 matrix | ACCEPT |
| EXISTS: DICE-T0 completion closed | `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md` | Status line | `CLOSED_PASS_BOUNDED` | DICE-T0 completion review | ACCEPT |
| EXISTS: DIR authorization gate | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 35 | `AuthorizationGate` | DIR router module | ACCEPT |
| EXISTS: DIR downstream capability | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 43 | `DownstreamCapability` | DIR router module | ACCEPT |
| EXISTS: DIR route decision | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 105 | `DocumentIntelligenceRouteDecision` | DIR router module | ACCEPT |
| EXISTS: DIR decision version field | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 108 | `decision_version` | DocumentIntelligenceRouteDecision | ACCEPT |
| EXISTS: DIR downstream eligibility field | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 111 | `downstream_eligibility` | DocumentIntelligenceRouteDecision | ACCEPT |
| EXISTS: DIR scan digest field | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 113 | `scan_decision_digest` | DocumentIntelligenceRouteDecision | ACCEPT |
| EXISTS: DIR eligibility derivation function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 120 | `_derive_downstream_eligibility` | DIR router module | ACCEPT |
| EXISTS: DIR route function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 137 | `decide_document_intelligence_route` | DIR router module | ACCEPT |
| EXISTS: EXA-T2 scan disposition | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 31 | `ScanRouteDisposition` | EXA-T2 scan-route module | ACCEPT |
| EXISTS: EXA-T2 scan route decision | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 58 | `ScanRouteDecision` | EXA-T2 scan-route module | ACCEPT |
| EXISTS: EXA-T2 scan route function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 69 | `decide_scan_route` | EXA-T2 scan-route module | ACCEPT |
| EXISTS: extraction quality owner field | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 111 | `mean_ocr_confidence` | ExtractionQualityReport | ACCEPT |
| EXISTS: operator scan outcome report | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 43 | `ScanOutcomeReport` | scan outcome report module | ACCEPT |
| EXISTS: scan review requirement field | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 51 | `operator_review_required` | ScanOutcomeReport | ACCEPT |
| EXISTS: scan findings field | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 54 | `findings` | ScanOutcomeReport | ACCEPT |
| EXISTS: scan outcome report builder | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 129 | `build_scan_outcome_report` | scan outcome report module | ACCEPT |

## Authorized Artifact Set

Claude may create or update only:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py`;
- `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md`;
- the paired work order only if adding worker-return evidence is necessary.

## Required Runtime Contents

The DICE-T1 implementation must:

- compose `decide_document_intelligence_route` and existing scan outcome
  report surfaces;
- expose a deterministic envelope result that carries route decision,
  scan-review requirement, findings, downstream handoff allowance, and claim
  boundary;
- block downstream handoff for `OCR_REQUIRES_SEPARATE_AUTH`,
  `PROVIDER_REQUIRES_SEPARATE_AUTH`, `OPERATOR_REVIEW_REQUIRED`, and
  `BLOCKED` unless the result explicitly surfaces operator review/block
  status;
- preserve `decision_version` and `scan_decision_digest`;
- preserve `ScanOutcomeReport.findings` without filtering;
- avoid introducing any new OCR/provider execution path, confidence threshold,
  scan disposition literal, authorization gate literal, or downstream
  capability literal.

## Evidence / Verification

Required dispatch verification:

- work-order dispatch quality checker passes on the dispatch package;
- pre-dispatch autorun gate passes on the real changed range;
- pre-commit governance chain passes before Codex commits.

Required worker verification is defined in the paired work order.

## Claim Boundary

This GC-018 authorizes local deterministic DICE-T1 source and tests only. It
does not authorize provider/OCR execution, external app tree inspection,
retrieval behavior change, route/API wiring, corpus ingestion, public-sync,
document correctness claims, extraction accuracy claims, provider quality
claims, readiness claims, cost claims, memory reinjection, high-risk
promotion, or autonomous mutation.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dispatch baseline. No public-sync
artifact or public catalog claim is authorized.
