# CVF Document Intelligence Router Foundation Roadmap

Memory class: FULL_RECORD

Status: DIR_T0_CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-13

Owner: Codex

## Authorization / Decision

Decision: `DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_BEFORE_USE_CASE_RUNTIME`.

Operator direction:

1. CVF foundation quality remains priority one.
2. Document Translator is a downstream CVF use case, similar to Policy_Local.
3. The next foundation step should be a Document Intelligence Router roadmap
   that reuses the EXA-T2 scan-route contracts and supports the scan layer.
4. Claude rebutted the draft at commit `fc79fcdf`; Codex accepted the four
   blocker fixes and incorporated them into this final roadmap.

This final roadmap authorizes only the next planning move: DIR-T0 may be
opened later through fresh GC-018 and a source-verified work order. It does not
authorize runtime implementation, external repository edits, dependency
installation, OCR execution, provider/API-key use, document ingestion,
public-sync, production readiness, public readiness, or cost/quality claims.

## Purpose

Define a CVF-owned Document Intelligence Router foundation layer above the
existing extraction scan layer.

The scan layer answers:

`Given supplied scan/extraction signals, is local extraction usable, OCR
eligible, blocked, or operator-review required?`

The proposed Document Intelligence Router answers:

`Given a document artifact, intended downstream use, structural profile, scan
route decision, confidence limits, and governance boundaries, what controlled
document-intelligence path is allowed next?`

This is useful for CVF foundation because it turns document workflows into
governed routing decisions before downstream use cases such as Policy_Local,
Document Translator, corpus intelligence, retrieval packs, or operator review
consume the document.

## Scope / Target / Owner Boundary

In scope:

- create a foundation roadmap for a CVF-owned Document Intelligence Router;
- reuse EXA-T2 `DocumentScanSignals`, `ScanRouteDecision`, and
  `decide_scan_route()` rather than replacing them;
- define the boundary between scan-layer signals and document-level
  intelligence routing;
- plan a document profile, intent, structure, confidence, and review packet
  contract;
- keep Policy_Local and Document Translator as downstream use-case adapters;
- identify which tranches are documentation-only, source-contract, or later
  runtime candidates.

Out of scope:

- editing `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Document_Translator`;
- editing external Policy_Local files;
- copying third-party code into CVF;
- installing or executing OCR, vision, provider, translation, retrieval,
  vector, WebSocket, or API-runtime dependencies;
- changing existing retrieval behavior;
- ingesting corpus records or storing raw document content;
- public-sync, production readiness, public readiness, cost, speed, accuracy,
  layout-preservation, provider-quality, or release claims.

Target owner surface: CVF private provenance planning under `docs/roadmaps/`.

Future implementation owner surface, if authorized later:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/` for document-intelligence contracts
  adjacent to the scan layer;
- `docs/reference/` for standards/contracts;
- `docs/work_orders/` and `docs/baselines/` for source-verified tranche
  dispatch.

## Non-Goals

This roadmap does not:

- reimplement the extraction pipeline;
- replace EXA-T2 scan routing;
- turn CVF into a translation app;
- unlock Policy_Local PL-S1;
- unlock Document Translator runtime adaptation;
- activate EC, retrieval, T12, OCR, provider calls, or public-sync;
- prove any external repository README/CLAUDE performance or production claim;
- authorize autonomous mutation, memory reinjection, or high-risk promotion.

## Source Authority

Source authority for this roadmap is limited to:

- operator instruction in this session;
- `docs/roadmaps/CVF_DOCUMENT_TRANSLATOR_CONTROL_ADAPTATION_ROADMAP_2026-06-13.md`;
- `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md`;
- `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md`;
- `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`;
- current CVF extraction foundation source files named in the Source
  Verification table.

`Thong_tin.md` and external repository claims remain operator/source
observations only. They are not runtime proof, provider proof, production proof,
or cost/quality evidence.

## Authority Chain

| Authority | Path or source | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-13 chat: create detailed roadmap and let Claude rebut before final | ACCEPT |
| Document Translator control adaptation roadmap | `docs/roadmaps/CVF_DOCUMENT_TRANSLATOR_CONTROL_ADAPTATION_ROADMAP_2026-06-13.md` | ACCEPT_AS_DOWNSTREAM_USE_CASE_CONTEXT |
| EXA parent roadmap | `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md` | ACCEPT_AS_SCAN_LAYER_PARENT_CONTEXT |
| EXA-T2 completion | `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md` | ACCEPT_AS_CURRENT_SCAN_ROUTE_FOUNDATION |
| Claude rebuttal | `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md` at commit `fc79fcdf` | ACCEPT_WITH_BLOCKER_FIXES |
| Extraction source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/` | ACCEPT_AS_CURRENT_OWNER_SURFACE |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: scan route version | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 20 | `SCAN_ROUTE_DECISION_VERSION` | EXA-T2 scan route module | ACCEPT |
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

## Current Runtime Freshness Verification

This roadmap makes no current runtime freshness claim.

| Runtime surface | Freshness claim | Verification state | Disposition |
| --- | --- | --- | --- |
| DIR source implementation | not implemented | N/A with reason: no source file is authorized by this roadmap | PASS |
| OCR/provider execution | not authorized | N/A with reason: no OCR/provider runtime was run or claimed | PASS |
| External Document Translator repo | not read for finalization | N/A with reason: adapter matrix must use published contract names only | PASS |
| External Policy_Local tree | not read for finalization | N/A with reason: PL-S remains separately held | PASS |
| Retrieval behavior | not changed | N/A with reason: DIR routes to later owners and does not wire retrieval | PASS |

## Foundation Relationship To EXA-T2

The Document Intelligence Router must compose EXA-T2 rather than duplicate it.

| Layer | Existing or proposed owner | Responsibility |
| --- | --- | --- |
| Extraction pipeline | existing `extraction_pipeline.py` | extract text/OCR through explicit adapter boundaries and evaluate quality |
| Scan route decision | existing `scan_route_decision.py` | turn supplied scan signals into local/OCR/escalate/block decisions |
| Operator scan outcome report | existing `scan_outcome_report.py` | show bounded extraction findings and operator actions without raw content release |
| Document Intelligence Router | proposed future CVF owner | combine document profile, document intent, structure signals, scan route, confidence, review, and downstream adapter eligibility |

The scan layer remains the source of truth for scan and extraction status.
The router may consume the scan decision but must not rewrite scan quality,
execute OCR, call providers, or create a parallel extraction confidence stack.

## Design Control Gate

Selected design:

1. Keep EXA-T2 as the local scan-route primitive.
2. Add a higher-level document router only after source-verifying existing
   owners.
3. Collapse intent into a capability-shaped field on `DocumentProfile`; do not
   create a standalone foundation `DocumentIntent` enum with use-case names.
4. Make review/operator actions first-class outputs.
5. Treat Policy_Local and Document Translator as adapter consumers, not router
   owners.
6. Make provider/OCR/cost routes blocked until separately authorized
   live-proof work orders exist; do not make them permanent advisory claims.
7. Keep `DocumentStructureSignals` separate for now because the current scan
   layer has extraction quality/coverage fields but no intrinsic document-shape
   fields.

Rejected design:

- direct external Document Translator code import;
- immediate runtime adapter wiring;
- provider/OCR execution inside the router;
- replacing `ScanOutcomeReport` with a second operator-report surface;
- allowing use-case apps to define foundation document semantics;
- use-case-named foundation intent values such as translation or legal-policy
  review;
- a flat router disposition enum that re-encodes EXA-T2 scan dispositions;
- mixing Policy_Local legal/current-status constraints into a generic router;
- claiming cost/quality/readiness from external README or CLAUDE docs.

## Claude Rebuttal Incorporation Ledger

| Rebuttal item | Codex disposition | Roadmap correction |
| --- | --- | --- |
| B1 - router disposition enum re-encodes scan layer | ACCEPT | replace flat router disposition with 3-axis composition: scan route passthrough, authorization gate, downstream capability eligibility |
| B2 - use-case names in foundation intent enum | ACCEPT | remove standalone use-case `DocumentIntent`; use `DownstreamCapability` and adapter matrix rows |
| B3 - 8-tranche / 5-contract speculative stack | ACCEPT | collapse roadmap to DIR-T0 doc-only contracts/matrix, DIR-T1 source/test, DIR-T2 pilot |
| B4 - external-tree read boundary under-stated | ACCEPT | state that adapter matrix must not read, list, hash, or modify Document Translator or Policy_Local source trees |
| I1 - semantic chunking | ACCEPT | keep semantic chunking out of DIR; DIR routes to later chunk/context owners |
| I2 - cost/provider routing | ACCEPT | provider/OCR routing is blocked until live-proof authorization, not advisory forever |
| I3 - machine-checkability | ACCEPT_AS_CANDIDATE | DIR-T1 should include an overlap check proving router authority gates do not duplicate scan dispositions |
| I4 - package owner | ACCEPT | future source implementation should live in `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/` unless DIR-T0 source map proves otherwise |

## Proposed Router Concepts

The future router should distinguish only the minimum contract families needed
to compose the scan layer.

| Contract family | Proposed purpose | Raw content allowed? | Initial status |
| --- | --- | --- | --- |
| `DocumentProfile` | source type, source artifact ID, source hash, language hints, page count, artifact role, domain hint, requested capability | no | PROPOSED |
| `DocumentStructureSignals` | intrinsic document-shape signals such as tables, images, formulas, layout risk, section/heading presence | no | PROPOSED |
| `DocumentIntelligenceRouteDecision` | scan route passthrough, authorization gate, downstream eligibility, operator action, scan decision digest | no | PROPOSED |

Supporting proposed type:

`DownstreamCapability = STRUCTURED_TEXT_HANDOFF | EVIDENCE_CITATION_HANDOFF |
CORPUS_SCAN_HANDOFF | OPERATOR_REVIEW_ONLY | ABSTAIN_OR_BLOCK`

Use-case mapping lives in the adapter matrix, not in a foundation intent enum:

| Use-case lane | Required capability | Defined where |
| --- | --- | --- |
| Document Translator DT-CVF | `STRUCTURED_TEXT_HANDOFF` | adapter matrix |
| Policy_Local PL-S | `EVIDENCE_CITATION_HANDOFF` | adapter matrix |
| Corpus intelligence | `CORPUS_SCAN_HANDOFF` | adapter matrix |
| Operator review only | `OPERATOR_REVIEW_ONLY` | adapter matrix |

All names above are proposed doc-only fields until a later source-verified work
order accepts or revises them. They must not be cited as existing runtime fields
before implementation.

## Router Composition Model

The router must not define a flat disposition enum that overlaps scan route
values. It composes three independent axes:

1. `scan_route`: passthrough from EXA-T2 `ScanRouteDisposition`;
2. `authorization_gate`: the router-owned authority axis;
3. `downstream_eligibility`: capability names that may receive a handoff.

Proposed authorization gate values:

- `LOCAL_DETERMINISTIC_ALLOWED`;
- `OCR_REQUIRES_SEPARATE_AUTH`;
- `PROVIDER_REQUIRES_SEPARATE_AUTH`;
- `OPERATOR_REVIEW_REQUIRED`;
- `BLOCKED`.

Deterministic mapping from scan route to authorization gate:

| Source `scan_route` | Derived `authorization_gate` |
| --- | --- |
| `LOCAL_TEXT_EXTRACTION_RECOMMENDED` | `LOCAL_DETERMINISTIC_ALLOWED` |
| `OCR_ELIGIBLE_OPERATOR_REVIEW_REQUIRED` | `OCR_REQUIRES_SEPARATE_AUTH` |
| `ESCALATE_OR_ABSTAIN` | `OPERATOR_REVIEW_REQUIRED` |
| `BLOCKED_UNSUPPORTED` | `BLOCKED` |

The router may add `PROVIDER_REQUIRES_SEPARATE_AUTH` only when a later
source-verified work order defines a provider-need signal and the corresponding
live-proof boundary. This roadmap does not authorize that signal.

Machine-check candidate for DIR-T1:

- fail if any router `AuthorizationGate` value duplicates a
  `ScanRouteDisposition` value;
- fail if a foundation `DownstreamCapability` enum contains use-case names
  such as Document Translator, Policy_Local, translation, or legal policy;
- fail if route decisions include raw text, OCR output, provider response, or
  downstream app state.

## Proposed Tranche Plan

| Tranche | Deliverable | Dependency | Status |
| --- | --- | --- | --- |
| DIR-T0 | Doc-only owner reconciliation, 3 contract tables, adapter matrix, and machine-check candidate spec | Final roadmap plus fresh GC-018/work order | CLOSED_PASS_BOUNDED |
| DIR-T1 | Deterministic local source implementation and focused tests | DIR-T0 closure plus fresh GC-018/work order | CLOSED_PASS_BOUNDED |
| DIR-T2 | Bounded pilot over operator-approved samples, if any | DIR-T1 closure plus sample corpus and runtime/live-proof authorization when applicable | HOLD_PENDING_T1_AND_RUNTIME_AUTH |

## Tranche Detail

### DIR-T0 - Doc-Only Contract And Adapter Matrix

Purpose: prevent duplicate abstractions before adding source code.

Deliverables:

- source map of current extraction foundation owners;
- accepted/rejected owner boundaries for profile, structure, route, review, and
  downstream adapter concepts;
- explicit collision check against EXA-T2 and EX-T9;
- final doc-only tables for `DocumentProfile`, `DocumentStructureSignals`, and
  `DocumentIntelligenceRouteDecision`;
- adapter eligibility matrix that maps use-case lanes to
  `DownstreamCapability`;
- machine-check candidate for scan-disposition overlap and use-case name leaks;
- source-owner decision for a later module under
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/`, unless source evidence blocks
  that placement.

Allowed scope:

- docs/reference and docs/reviews artifacts only;
- no source implementation;
- no runtime, OCR, provider, retrieval, external use-case repo, or corpus
  operation.

Exit criteria:

- every proposed field or symbol is labeled as existing, proposed doc-only, or
  rejected;
- the adapter matrix uses capability names, not use-case names inside a
  foundation enum;
- the matrix does not read, list, hash, or modify any file under
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Document_Translator` or any
  external Policy_Local source tree;
- missing published adapter contracts are recorded as
  `ADAPTER_CONTRACT_NOT_YET_PUBLISHED`, not inferred from source;
- no runtime/OCR/provider/app edit is performed.

### DIR-T1 - Deterministic Source Contract And Tests

Purpose: implement the minimal deterministic router only after DIR-T0 closes.

Candidate source:

- a small `document_intelligence_router.py` module adjacent to EXA-T2, if
  DIR-T0 confirms `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/` ownership;
- focused tests in `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/`;
- a governance checker or focused test proving router authority gates do not
  overlap scan dispositions.

Required behavior:

- import or otherwise source-verify EXA-T2 scan route values instead of
  retyping them;
- preserve `BLOCKED_UNSUPPORTED` and `ESCALATE_OR_ABSTAIN` semantics;
- never downgrade operator-review requirements;
- keep provider/OCR actions blocked unless a separate work order authorizes
  them;
- keep `DocumentStructureSignals` separate at implementation start, with a
  documented `KEEP_SEPARATE_BUT_COLLAPSIBLE_AT_T1` decision if tests prove the
  structure contract has no independent variation.

Acceptance boundary:

- no raw document text;
- no provider call or OCR execution;
- no domain-specific legal finding;
- no production/readiness claim.

This tranche must be separately authorized by fresh GC-018 and a
source-verified work order. It is not authorized by this roadmap.

### DIR-T2 - Later Bounded Pilot

Purpose: run a bounded live/local pilot only after contracts and source are
closed.

This is held until:

- operator supplies a bounded sample corpus;
- live-provider/OCR/runtime scope is explicitly authorized if needed;
- diagnostics and receipts are defined;
- release-quality governance proof rules are satisfied when governance behavior
  is claimed.

## Work Plan

1. Preserve Claude rebuttal at
   `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`.
2. Record Codex incorporation decision in a review artifact.
3. Only after this final roadmap acceptance may DIR-T0 be opened with fresh GC-018
   and a source-verified work order.
4. Keep Document Translator DT-CVF-T0 and Policy_Local PL-S1 separate unless a
   later operator decision explicitly sequences them after DIR.

## Dispatch Boundary

This roadmap is not a dispatch packet.

No worker may implement the router from this roadmap alone. A future work order
must include:

- Source Verification Block;
- Roadmap-to-Work-Order Trace Matrix;
- dependency-release evidence from this final roadmap;
- explicit allowed file paths;
- explicit no-runtime/no-provider/no-OCR boundary unless later authorized;
- required proof commands;
- worker commit mode.

## Claude Rebuttal Gate

Status: `SATISFIED`.

Claude rebuttal artifact:

`docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`

Commit: `fc79fcdf`.

Result: Claude accepted the draft architecture with four blockers. Codex
accepted B1-B4 and I1-I4 into this roadmap. DIR-T0 remains blocked until a
fresh GC-018 and source-verified work order are opened.

## Acceptance Criteria

This roadmap is acceptable for DIR-T0 authorization only if:

1. It keeps EXA-T2 as the scan-route owner.
2. It separates scan-layer decisions from document-intelligence routing.
3. It keeps Document Translator and Policy_Local downstream and separately
   gated.
4. It forbids runtime/OCR/provider/external repo edits until later authorized
   work orders.
5. It records proposed doc-only fields as proposed, not existing runtime facts.
6. It records Claude rebuttal incorporation before finalization.
7. It includes public export disposition and claim boundary.
8. It collapses speculative tranches to DIR-T0/T1/T2.
9. It avoids use-case names in foundation capability enums.
10. It requires scan-disposition overlap protection before source
    implementation.

## Verification / Evidence

Finalization evidence:

- `docs/roadmaps/CVF_DOCUMENT_TRANSLATOR_CONTROL_ADAPTATION_ROADMAP_2026-06-13.md`
  was read for the downstream use-case boundary.
- `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md`
  was read for EXA absorption context.
- `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md`
  was read for scan-route closure status.
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`,
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`, and
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` were read
  for owner-surface verification.
- `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`
  was read and incorporated.

Required before opening DIR-T0:

- fresh GC-018 baseline;
- source-verified work order;
- pre-dispatch autorun gate over the real changed range;
- no untracked external use-case edit included in the dispatch commit.

Status: `SATISFIED_BY_DIR_T0_DISPATCH`.

Dispatch package:

- GC-018:
  `docs/baselines/CVF_GC018_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md`
- dispatchBaseHead: `51cd1ded`
- worker commit mode: `WORKER_MUST_NOT_COMMIT`
- worker boundary: contract-matrix documentation and worker-return packet only;
  no runtime/source, external Document Translator or Policy_Local tree
  operation, OCR/provider, retrieval, corpus, public-sync, readiness, cost, or
  quality claim is authorized.

DIR-T0 closure package:

- completion:
  `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`
- contract matrix:
  `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`
- worker return:
  `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_COMPLETION_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this file | `Status: DIR_T0_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | no GC-051 registry update authorized for DIR-T0 closure | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no GC-051 registry update authorized for DIR-T0 closure | BLOCKED with reason |
| External evidence digest | N/A with reason | no external corpus/provider evidence used | N/A with reason |
| System loop interlock | N/A with reason | no runtime loop mutation authorized | N/A with reason |
| Session continuity | active state/front door/handoff | separate session-sync commit follows material closure when required | N/A with reason |

## Governed Work Lifecycle

`INTAKE -> DRAFT -> REBUTTAL -> FINAL_ROADMAP -> GC-018 -> WORK_ORDER -> BUILD -> REVIEW -> FREEZE`

- INTAKE: operator identified DIR as a foundation step that helps CVF and scan
  layer.
- DRAFT: this artifact proposes the route architecture and questions.
- REBUTTAL: Claude challenges duplication, scope, owner boundaries, and claim
  safety.
- FINAL_ROADMAP: this revision incorporates accepted critique.
- GC-018: DIR-T0 may receive a fresh baseline only after this finalization.
- WORK_ORDER: implementation or doc closure requires source verification.
- BUILD: no build is authorized yet.
- REVIEW: Codex reviews worker returns before commit.
- FREEZE: readiness claims require closed artifacts and applicable gates.

## Claim Boundary

This final roadmap authorizes only later DIR-T0 planning through fresh GC-018
and source-verified work order. It does not prove document intelligence
behavior, extraction accuracy, OCR quality, provider behavior, routing
correctness, retrieval quality, Policy_Local readiness, Document Translator
readiness, public readiness, production readiness, release readiness, cost
savings, memory reinjection, high-risk promotion, or autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation roadmap; no public-sync batch is
authorized.
