# CVF GC-018 - DIR-T2 Document Intelligence Router Foundation Pilot

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-06-13

Owner: Codex (orchestrator)

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `30e6d174`

sourceAuthority:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_FOR_CLAUDE_2026-06-13.md`

parentRoadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

predecessorTranche:
`docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md`

## Purpose

Authorize DIR-T2 as a bounded CVF foundation pilot for the deterministic
Document Intelligence Router. The pilot must validate current DIR-T1 behavior
over a small operator-approved, synthetic, metadata-only sample corpus that
represents document-shape cases without reading or importing external
Document Translator files.

This tranche is foundation hardening. Document Translator remains only a
downstream use-case context and must not become the implementation target.

## Scope / Target / Owner Boundary

Target: one local deterministic pilot harness, focused tests, and a worker
return packet proving that DIR-T1 composes EXA-T2 scan-route outputs across a
bounded fixture corpus while preserving claim boundaries.

Owner boundary: Codex owns orchestration, dispatch, review, closure, and
session-state sync. Claude owns worker implementation artifacts under
`WORKER_MUST_NOT_COMMIT` and must return them uncommitted for Codex review.

## Decision / Baseline / Proposed Tranche

Decision: open DIR-T2 only as a CVF foundation pilot. The authorized pilot is
test-only and synthetic-fixture based.

Baseline:

- current dispatch base: `30e6d174`;
- DIR-T0 closure commit: `082b02ff`;
- DIR-T1 closure commit: `4bf991f3`;
- current router source:
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py`;
- current scan route source:
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`.

Proposed tranche:

- create a focused DIR-T2 foundation pilot test file;
- create a worker-return packet;
- return uncommitted artifacts for Codex review and commit.

## Runtime Authorization

Authorized runtime scope: local deterministic Python execution only, using
in-repo fixture metadata and existing EXA-T2/DIR-T1 source.

Not authorized: OCR execution, provider/API calls, external service calls,
retrieval runtime, Document Translator source reads, Policy_Local mutation,
corpus ingestion, public-sync, readiness, cost, or quality claims.

If Claude determines that a real file, OCR, provider, retrieval, or external
repository step is needed, Claude must stop and return `BLOCKED_SCOPE_EXPANSION`.

## Operator-Approved Sample Corpus Boundary

The operator instruction for this batch authorizes a bounded sample corpus only
as synthetic metadata fixtures inside the CVF provenance repo. The sample
corpus must contain no raw document text, no copied document bytes, no OCR
output, no provider response, and no external Document Translator file path.

Minimum fixture cases:

| sampleId | Intent | Required scan disposition coverage |
| --- | --- | --- |
| DIR-T2-S1 | digital-native structured text handoff | `LOCAL_TEXT_EXTRACTION_RECOMMENDED` |
| DIR-T2-S2 | scanned or image-heavy document requiring operator/OCR authorization | `OCR_ELIGIBLE_OPERATOR_REVIEW_REQUIRED` |
| DIR-T2-S3 | ambiguous/low-confidence document requiring operator review | `ESCALATE_OR_ABSTAIN` |
| DIR-T2-S4 | unsupported source blocked by scan layer | `BLOCKED_UNSUPPORTED` |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| DIR-T0 contract matrix closed | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` at closure commit `082b02ff` | ACCEPT |
| DIR-T1 source and tests closed | `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md` at closure commit `4bf991f3` | ACCEPT |
| DIR-T1 router source exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | ACCEPT |
| Active next move authorizes DIR-T2 only through fresh GC-018, sample corpus, and runtime authorization | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Fresh DIR-T2 authorization | this GC-018 baseline and paired Claude work order | ACCEPT |

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | DIR-T2 builds only on closed DIR-T0/T1 artifacts and current EXA-T2/DIR-T1 source | COMPLETE |
| Detailed source files read | source verification below covers router, scan-route, tests, roadmap, and session boundary | COMPLETE |
| Current owner surfaces checked | EXA-T2 owns scan route; DIR owns authorization gate; downstream adapters remain separate | COMPLETE |
| Accept/defer/reject dispositions recorded | source verification, runtime authorization, and forbidden scope blocks are recorded | COMPLETE |
| Adversarial role review applied | this pilot blocks real file/OCR/provider/retrieval and use-case implementation drift | COMPLETE |
| Blind-spot delta | semantic correctness of document content remains unproven and out of scope | COMPLETE |

Verdict: `COMPLETE_WITH_DECLARED_BOUNDARIES`.

## Rescan Intelligence Hardening

- Original source artifact: closed DIR-T0 contract matrix, DIR-T1 completion
  review, and current EXA-T2/DIR-T1 source, not the external Document
  Translator repo.
- Predecessor intake artifact:
  `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md`.
- Delta ledger status: DISPATCH_DECLARED_LIMITS - T2 is released only as a
  local deterministic pilot harness and worker-return packet.
- Routing matrix status: DISPATCH_DECLARED_LIMITS - OCR/provider, retrieval,
  external use-case repos, public-sync, and readiness claims remain out of
  scope.
- Semantic sampling status: DISPATCH_DECLARED_LIMITS - worker must cover all
  current scan dispositions through synthetic metadata fixtures.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| sampleId | Delta category | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| DIR-T2-GC018-D1 | UNCHANGED_FROM_INTAKE | roadmap DIR-T2 detail | DIR-T2 requires bounded sample corpus and runtime authorization | synthetic metadata-only corpus plus local runtime tests | Did dispatch skip the sample boundary? | PASS |
| DIR-T2-GC018-D2 | CHANGED_DISPOSITION | active session next move | DIR-T2 was held until fresh authorization | this baseline releases only local deterministic pilot scope | Did dispatch authorize OCR/provider or external repo work? | PASS |
| DIR-T2-GC018-D3 | NEW_FINDING | DIR-T1 completion residual | DIR-T1 was deterministic-only and not validated over samples | focused pilot harness now assigned | Could validation become a use-case readiness claim? | PASS |
| DIR-T2-GC018-D4 | REMOVED_OR_REJECTED | Document Translator use-case context | downstream app should remain separate from foundation router | external tree access forbidden | Could Claude inspect or modify the app repo? | PASS |

### Follow-Up Routing Matrix

| Route lane | Target | Disposition | Evidence | Next action |
| --- | --- | --- | --- | --- |
| DO_NOW | local deterministic DIR-T2 fixture pilot and worker return | ACCEPT | this GC-018 plus paired work order | Claude executes allowed artifacts |
| SEPARATE_RUNTIME_TRANCHE | OCR, provider/API, retrieval runtime, or real document execution | DEFER | runtime authorization boundary | fresh operator authorization required |
| STRATEGIC_OPERATOR_DECISION | DT-CVF-T0, Policy_Local PL-S1, public-sync, readiness, cost, or quality claim | DEFER | active parked checkpoints | operator decision later |
| OUT_OF_SCOPE | external Document Translator and Policy_Local tree operations | REJECT | forbidden path manifest | no read, list, hash, modify, or import |
| RESOLVED_BY_DESIGN | worker commits | REJECT | `WORKER_MUST_NOT_COMMIT` | Codex reviews and commits |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| DIR-T2-GC018-S1 | scan route source | EXA-T2 owns `ScanRouteDisposition` | worker must cover all current scan routes | Could DIR re-encode scan route semantics? | PASS |
| DIR-T2-GC018-S2 | router source | DIR owns `AuthorizationGate` and downstream eligibility | tests assert gate/action/eligibility per sample | Could gate downgrade operator review? | PASS |
| DIR-T2-GC018-S3 | roadmap DIR-T2 | sample corpus is bounded and operator approved | synthetic metadata-only fixtures | Could real documents leak into the pilot? | PASS |
| DIR-T2-GC018-S4 | claim boundary | no app readiness or provider/OCR behavior is claimed | worker return must state negative evidence | Could foundation proof become Document Translator proof? | PASS |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: DIR route version | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 25 | `DOCUMENT_INTELLIGENCE_ROUTE_VERSION` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR authorization gate | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 35 | `AuthorizationGate` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR downstream capability | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 43 | `DownstreamCapability` | DIR-T1 router module | ACCEPT |
| EXISTS: scan-to-gate map | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 51 | `SCAN_ROUTE_TO_AUTHORIZATION_GATE` | DIR-T1 router module | ACCEPT |
| EXISTS: document profile | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 68 | `DocumentProfile` | DIR-T1 router module | ACCEPT |
| EXISTS: structure signals | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 86 | `DocumentStructureSignals` | DIR-T1 router module | ACCEPT |
| EXISTS: route decision | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 105 | `DocumentIntelligenceRouteDecision` | DIR-T1 router module | ACCEPT |
| EXISTS: route function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 139 | `decide_document_intelligence_route` | DIR-T1 router module | ACCEPT |
| EXISTS: EXA-T2 scan route version | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 20 | `SCAN_ROUTE_DECISION_VERSION` | EXA-T2 scan route module | ACCEPT |
| EXISTS: EXA-T2 scan disposition | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 31 | `ScanRouteDisposition` | EXA-T2 scan route module | ACCEPT |
| EXISTS: EXA-T2 scan signals | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 40 | `DocumentScanSignals` | EXA-T2 scan route module | ACCEPT |
| EXISTS: EXA-T2 scan function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 71 | `decide_scan_route` | EXA-T2 scan route module | ACCEPT |
| EXISTS: DIR-T1 focused tests | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py` | lines 71, 98, 150, 172, 224 | `test_*` | DIR-T1 test suite | ACCEPT |
| EXISTS: DIR-T2 roadmap gate | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | lines 368-388 | `DIR-T2` | parent roadmap | ACCEPT |

## Authorized Artifact Set

Claude may create or update only:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py`;
- `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_WORKER_RETURN_2026-06-13.md`;
- the paired work order only if adding worker-return evidence is necessary.

## Evidence / Verification

Required dispatch verification:

- dispatch-quality checker passes on this GC-018 and paired work order;
- pre-dispatch autorun gate passes on the real changed range before dispatch;
- pre-commit governance chain passes before Codex commits.

Required worker verification is defined in the paired work order.

## Claim Boundary

This GC-018 authorizes local deterministic foundation pilot proof only. It
does not claim document understanding, extraction accuracy, OCR quality,
provider behavior, retrieval quality, Document Translator readiness,
Policy_Local readiness, public readiness, production readiness, hosted
readiness, memory reinjection, high-risk promotion, or autonomous mutation.

rawMemoryReleased=false
