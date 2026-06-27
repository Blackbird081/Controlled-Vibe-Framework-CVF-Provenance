# CVF GC-018 - DIR-T0 Document Intelligence Router Contract Matrix

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `51cd1ded`

sourceAuthority:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md`

parentRoadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

## Purpose

Authorize DIR-T0 as a bounded documentation-only contract matrix tranche for
the Document Intelligence Router foundation. The worker may reconcile current
EXA-T2 and EX-T9 owner surfaces, define three doc-only contract tables, create
an adapter eligibility matrix, and specify machine-check candidates for a later
implementation tranche.

This tranche does not authorize runtime implementation, source code changes,
OCR execution, provider/API use, retrieval changes, corpus ingestion, external
Document Translator or Policy_Local tree inspection, public-sync, readiness,
cost, quality, memory reinjection, high-risk promotion, or autonomous mutation.

## Scope / Target / Owner Boundary

Target: DIR-T0 contract matrix and worker-return review artifacts only.

Owner boundary: Codex owns dispatch, review, commit, and session state. Claude
owns worker implementation artifacts under `WORKER_MUST_NOT_COMMIT` and must
return them uncommitted for Codex review.

## Decision / Baseline / Proposed Tranche

Decision: open DIR-T0 from the finalized Document Intelligence Router roadmap
after Claude rebuttal incorporation and session-state synchronization.

Baseline:

- DIR roadmap finalization material commit: `075679f3`.
- DIR Claude rebuttal commit: `fc79fcdf`.
- DIR final roadmap session-sync commit: `51cd1ded`.
- Current scan-route owner surface remains
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`.
- Current extraction quality and scan-outcome owner surfaces remain
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` and
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`.

Authorized tranche:

- add a DIR contract matrix under `docs/reference/`;
- add a DIR-T0 worker-return packet under `docs/reviews/`;
- classify every proposed symbol or field as existing, proposed doc-only, or
  rejected;
- keep use-case names in adapter rows only, not in foundation capability
  enums;
- return uncommitted artifacts to Codex for review and commit.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| Claude rebuttal exists | `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`; commit `fc79fcdf`; status `REBUTTAL_FOR_CODEX_REVIEW` | ACCEPT |
| Codex finalization review accepted blockers | `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CODEX_FINALIZATION_REVIEW_2026-06-13.md`; status `CLOSED_PASS_BOUNDED` | ACCEPT |
| Final roadmap released DIR-T0 only through fresh GC-018 | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`; status before this dispatch `FINAL_ROADMAP_AWAITING_DIR_T0_AUTHORIZATION` | ACCEPT |
| Session state synchronized final roadmap | current HEAD before dispatch `51cd1ded` | ACCEPT |
| Fresh DIR-T0 authorization | this GC-018 baseline and the paired Claude work order | ACCEPT |

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | DIR roadmap cites EXA parent, EXA-T2 completion, Document Translator context, and Claude rebuttal | COMPLETE |
| Detailed source files read | scan route, extraction pipeline, and scan outcome report anchors are source-verified below | COMPLETE |
| Current owner surfaces checked | Source Verification Block separates existing source from proposed doc-only contracts | COMPLETE |
| Accept/defer/reject dispositions recorded | Source Verification and New Doc-Only Fields Authorized tables below | COMPLETE |
| Adversarial role review applied | Claude rebuttal B1-B4 and I1-I4 were incorporated before dispatch | COMPLETE |
| Blind-spot delta | no external tree scan, runtime/OCR/provider action, or downstream use-case edit is authorized | COMPLETE |

Verdict: `COMPLETE_WITH_DECLARED_BOUNDARIES`.

## Rescan Intelligence Hardening

- Original source artifact: finalized DIR roadmap and current EXA-T2/EX-T9
  extraction foundation source, not the external Document Translator repo.
- Predecessor intake artifact:
  `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`
  and
  `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CODEX_FINALIZATION_REVIEW_2026-06-13.md`.
- Delta ledger status: DISPATCH_DECLARED_LIMITS - T0 is released only as
  doc-only owner reconciliation and contract matrix work.
- Routing matrix status: DISPATCH_DECLARED_LIMITS - runtime implementation,
  OCR/provider, retrieval, external use-case repos, public-sync, and readiness
  claims remain out of scope.
- Semantic sampling status: DISPATCH_DECLARED_LIMITS - worker must include
  source-owner collision rows and adapter-boundary rows in the contract matrix.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| sampleId | Delta category | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| DIR-T0-GC018-D1 | UNCHANGED_FROM_INTAKE | roadmap dispatch boundary | DIR-T0 requires fresh GC-018 and source-verified work order | this baseline plus paired work order | Did dispatch skip release evidence? | PASS |
| DIR-T0-GC018-D2 | CHANGED_DISPOSITION | roadmap tranche plan | DIR-T0 was awaiting fresh authorization | status moves to dispatch only | Did dispatch claim closure before worker return? | PASS |
| DIR-T0-GC018-D3 | NEW_FINDING | Claude rebuttal B1-B4 | flat disposition and use-case enum risks must be blocked | work order requires axis separation and adapter-only use-case rows | Could T0 recreate the criticized overlap? | PASS |
| DIR-T0-GC018-D4 | REMOVED_OR_REJECTED | external-tree boundary | no Document Translator or Policy_Local tree inspection | forbidden scope retained | Could adapter matrix infer unpublished contracts from source? | PASS |

### Follow-Up Routing Matrix

| Route lane | Target | Disposition | Evidence | Next action |
| --- | --- | --- | --- | --- |
| DO_NOW | DIR-T0 contract matrix and worker return | ACCEPT | final roadmap DIR-T0 detail | Claude implements allowed artifacts |
| SEPARATE_RUNTIME_TRANCHE | source implementation, tests, OCR, provider, or live proof | DEFER | roadmap DIR-T1 and claim boundary | fresh authorization after T0 closure |
| STRATEGIC_OPERATOR_DECISION | DT-CVF-T0, Policy_Local PL-S1, sample corpus, public-sync, readiness, cost, or quality claim | DEFER | active session parked checkpoint | operator decision later |
| OUT_OF_SCOPE | external Document Translator and Policy_Local tree operations | REJECT | roadmap external-tree boundary | no read, list, hash, modify, or import |
| RESOLVED_BY_DESIGN | worker commits | REJECT | `WORKER_MUST_NOT_COMMIT` | Codex reviews and commits |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| DIR-T0-GC018-S1 | scan route source | `ScanRouteDecision` already owns scan route decisions | source verification cites source lines | Could DIR duplicate scan dispositions? | PASS |
| DIR-T0-GC018-S2 | final roadmap | `DownstreamCapability` keeps capability names generic | new doc-only table boundary | Could use-case names enter foundation enum? | PASS |
| DIR-T0-GC018-S3 | final roadmap | missing adapter contracts must be labeled, not inferred | work order requires `ADAPTER_CONTRACT_NOT_YET_PUBLISHED` | Could external repos be inspected for convenience? | PASS |
| DIR-T0-GC018-S4 | final roadmap | DIR-T1 is held behind T0 closure | dependency release table keeps T1 held | Could dispatch authorize code work? | PASS |

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
| EXISTS: storage boundary | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 152 | `ExtractionStorageBoundary` | extraction pipeline | ACCEPT |
| EXISTS: OCR language mapping owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 162 | `map_ocr_language_codes` | extraction pipeline | ACCEPT |
| EXISTS: extraction quality evaluator | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 235 | `evaluate_extraction_quality` | extraction pipeline | ACCEPT |
| EXISTS: scan outcome report | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 43 | `ScanOutcomeReport` | EX-T9 scan outcome report module | ACCEPT |
| EXISTS: scan outcome report builder | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 131 | `build_scan_outcome_report` | EX-T9 scan outcome report module | ACCEPT |
| DIR-T0 scope is doc-only contract and adapter matrix work | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | lines 285-333 | `DIR-T0` | DIR roadmap | ACCEPT |
| DIR-T0 must not inspect external use-case source trees | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | lines 318-323 | `Document_Translator`, `Policy_Local` | DIR roadmap | ACCEPT |
| DIR-T0 opening requires fresh GC-018 and source-verified work order | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | lines 455-459 | `Required before opening DIR-T0` | DIR roadmap | ACCEPT |
| Claude rebuttal blockers were incorporated before dispatch | `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CODEX_FINALIZATION_REVIEW_2026-06-13.md` | lines 68-97 | `B1`, `B2`, `B3`, `B4`, `I1`, `I2`, `I3`, `I4` | Codex finalization review | ACCEPT |

## New Doc-Only Fields Authorized

These names are authorized only for DIR-T0 documentation contracts. They are
not claimed as current runtime/source symbols.

| New doc-only field or symbol | Roadmap source | Target contract path | Boundary |
| --- | --- | --- | --- |
| `DocumentProfile` | roadmap lines 224 and 305 | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | doc-only contract table, not runtime class |
| `DocumentStructureSignals` | roadmap lines 225 and 305 | same | doc-only contract table, not runtime class |
| `DocumentIntelligenceRouteDecision` | roadmap lines 226 and 306 | same | doc-only contract table, not runtime class |
| `DownstreamCapability` | roadmap lines 230-232 and 308 | same | capability enum proposal, not use-case enum |
| `authorization_gate` | roadmap lines 246-276 | same | router authority axis, not scan disposition |
| `downstream_eligibility` | roadmap lines 246-276 | same | downstream capability axis, not app state |
| `scan_decision_digest` | roadmap lines 224-226 and 305-310 | same | reference digest only, no raw text/OCR/provider output |
| `ADAPTER_CONTRACT_NOT_YET_PUBLISHED` | roadmap lines 324-326 | same | adapter-matrix label for missing published contracts |

## Authorized Artifact Set

Claude may create or update only:

- `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`;
- `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`;
- the paired work order only if adding worker-return evidence is necessary;
- the parent roadmap row only to mark worker-return status, not final closure.

## Evidence / Verification

Required dispatch verification:

- work-order dispatch quality checker passes on the dispatch package;
- pre-dispatch autorun gate passes on the real changed range;
- reviewer-fast and pre-commit gates pass before Codex commits.

Required worker verification is defined in the paired work order.

## Claim Boundary

This GC-018 authorizes bounded DIR-T0 contract-matrix work only. It does not
claim document intelligence behavior exists, router source code is implemented,
scan/extraction accuracy is improved, OCR/provider behavior is available,
retrieval behavior changed, Policy_Local is ready, Document Translator is
ready, public catalog export exists, release proof exists, memory reinjection
is authorized, high-risk promotion is authorized, or autonomous mutation is
authorized.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This is a private provenance dispatch baseline. No public-sync artifact or
public catalog claim is authorized by this tranche.
