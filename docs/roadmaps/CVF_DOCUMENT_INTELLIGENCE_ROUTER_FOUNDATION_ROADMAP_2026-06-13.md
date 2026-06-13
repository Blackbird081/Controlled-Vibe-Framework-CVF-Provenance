# CVF Document Intelligence Router Foundation Roadmap

Memory class: FULL_RECORD

Status: DRAFT_FOR_CLAUDE_REBUTTAL

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
4. Claude should rebut this draft before the final roadmap is closed.

This draft authorizes planning and critique only. It does not authorize
runtime implementation, external repository edits, dependency installation,
OCR execution, provider/API-key use, document ingestion, public-sync,
production readiness, public readiness, or cost/quality claims.

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

Source authority for this draft is limited to:

- operator instruction in this session;
- `docs/roadmaps/CVF_DOCUMENT_TRANSLATOR_CONTROL_ADAPTATION_ROADMAP_2026-06-13.md`;
- `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md`;
- `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md`;
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
3. Separate document profile and intent from raw document content.
4. Make review/operator actions first-class outputs.
5. Treat Policy_Local and Document Translator as adapter consumers, not router
   owners.
6. Make provider/OCR/cost routes advisory or blocked until separately
   authorized live-proof work orders exist.

Rejected design:

- direct external Document Translator code import;
- immediate runtime adapter wiring;
- provider/OCR execution inside the router;
- replacing `ScanOutcomeReport` with a second operator-report surface;
- allowing use-case apps to define foundation document semantics;
- mixing Policy_Local legal/current-status constraints into a generic router;
- claiming cost/quality/readiness from external README or CLAUDE docs.

## Proposed Router Concepts

The future router should distinguish these contract families.

| Contract family | Proposed purpose | Raw content allowed? | Initial status |
| --- | --- | --- | --- |
| `DocumentProfile` | source type, language hints, page count, artifact role, domain hints, declared downstream use | no | PROPOSED |
| `DocumentIntent` | translation, policy evidence review, corpus scan, summarization, citation extraction, operator review | no | PROPOSED |
| `DocumentStructureSignals` | table density, image/formula presence, section/heading signals, page continuity, layout-risk flags | no | PROPOSED |
| `DocumentIntelligenceRouteDecision` | allowed next path, blocked path, required review, downstream adapter eligibility | no | PROPOSED |
| `DocumentIntelligenceReviewPacket` | operator-visible reasons, evidence metrics, unresolved risks, next action | no raw text by default | PROPOSED |

All names above are proposed doc-only fields until a later source-verified work
order accepts or revises them. They must not be cited as existing runtime fields
before implementation.

## Proposed Tranche Plan

| Tranche | Deliverable | Dependency | Status |
| --- | --- | --- | --- |
| DIR-T0 | Foundation owner reconciliation and source-authority map | Claude rebuttal incorporated, fresh GC-018/work order | HOLD_PENDING_REBUTTAL_AND_AUTH |
| DIR-T1 | Document profile and intent taxonomy contract | DIR-T0 closure | HOLD_PENDING_T0 |
| DIR-T2 | Document structure signal contract and scan-layer mapping | DIR-T1 closure | HOLD_PENDING_T1 |
| DIR-T3 | Router decision contract that composes EXA-T2 `ScanRouteDecision` | DIR-T2 closure | HOLD_PENDING_T2 |
| DIR-T4 | Operator-visible document-intelligence review packet | DIR-T3 closure | HOLD_PENDING_T3 |
| DIR-T5 | Downstream adapter readiness matrix for Policy_Local and Document Translator | DIR-T4 closure | HOLD_PENDING_T4 |
| DIR-T6 | Later deterministic local source implementation and focused tests | DIR-T5 closure plus explicit implementation authorization | HOLD_PENDING_IMPLEMENTATION_AUTH |
| DIR-T7 | Later runtime pilot, if any, over bounded samples | DIR-T6 closure plus operator sample corpus and live-proof authorization | HOLD_PENDING_RUNTIME_AUTH |

## Tranche Detail

### DIR-T0 - Owner Reconciliation And Source Authority

Purpose: prevent duplicate abstractions before adding a router.

Deliverables:

- source map of current extraction foundation owners;
- accepted/rejected owner boundaries for profile, intent, structure, route,
  report, review, and downstream adapter concepts;
- explicit collision check against EXA-T2 and EX-T9;
- decision on whether router contracts belong in
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION` or a new foundation package.

Allowed scope:

- docs/reference and docs/reviews artifacts only;
- no source implementation unless the work order explicitly authorizes it.

Exit criteria:

- every proposed field or symbol is labeled as existing, proposed doc-only, or
  rejected;
- Claude rebuttal findings are accepted/deferred/rejected with reasons;
- no runtime/OCR/provider/app edit is performed.

### DIR-T1 - Document Profile And Intent Taxonomy

Purpose: define the minimal metadata needed before route decisions.

Candidate profile signals:

- source type and source artifact ID;
- language hints;
- page count;
- source hash;
- declared artifact role;
- downstream intent;
- domain hint such as generic, legal-policy, translation, corpus-intelligence,
  or operator-review.

Candidate intent values:

- `TRANSLATION_PREP`;
- `POLICY_EVIDENCE_REVIEW`;
- `CORPUS_INTELLIGENCE_SCAN`;
- `CITATION_OR_METADATA_EXTRACTION`;
- `OPERATOR_READABILITY_REVIEW`;
- `ABSTAIN_OR_BLOCK`.

Acceptance boundary:

- no raw document text;
- no provider choice;
- no domain-specific legal finding;
- no production/readiness claim.

### DIR-T2 - Document Structure Signal Contract

Purpose: give downstream controllers a stable way to reason about structure
without storing raw content.

Candidate structure signals:

- heading/section presence;
- table density;
- image density;
- formula or symbol density;
- page continuity risk;
- scanned-page ratio when supplied by scan layer;
- layout-preservation risk;
- citation/evidence-marker presence as a boolean or count;
- missing-page or low-coverage flags from extraction quality.

Required relationship to scan layer:

- reuse `ExtractionQualityReport` and `DocumentScanSignals` where possible;
- avoid duplicate coverage/confidence thresholds;
- keep layout-risk advisory separate from OCR/provider execution.

### DIR-T3 - Router Decision Contract

Purpose: produce a bounded, deterministic decision about the next allowed
document-intelligence path.

Candidate outputs:

- decision version;
- route disposition;
- allowed next path;
- blocked path reason;
- required operator action;
- downstream adapter eligibility;
- scan route decision digest;
- claim boundary.

Candidate dispositions:

- `PROCEED_LOCAL_DOCUMENT_INTELLIGENCE`;
- `PROCEED_AFTER_OPERATOR_REVIEW`;
- `OCR_ELIGIBLE_BUT_NOT_AUTHORIZED`;
- `PROVIDER_ELIGIBLE_BUT_NOT_AUTHORIZED`;
- `BLOCKED_UNSUPPORTED_SOURCE`;
- `ABSTAIN_INSUFFICIENT_EVIDENCE`.

Required composition:

- consume EXA-T2 `ScanRouteDecision`;
- preserve EXA-T2 `BLOCKED_UNSUPPORTED` and `ESCALATE_OR_ABSTAIN` semantics;
- do not downgrade operator-review requirements;
- do not execute any downstream adapter.

### DIR-T4 - Operator-Visible Review Packet

Purpose: make the router decision inspectable by a non-coder operator.

Candidate packet sections:

- source artifact summary;
- profile summary;
- structure signal summary;
- scan route digest;
- router decision;
- required operator action;
- blocked or deferred capabilities;
- downstream adapter eligibility;
- claim boundary and public export disposition.

Required relationship:

- reuse `ScanOutcomeReport` findings where scan/extraction quality caused the
  route;
- add document-intelligence findings only when they are not scan-quality
  duplicates;
- preserve raw-content release prohibition by default.

### DIR-T5 - Downstream Adapter Readiness Matrix

Purpose: make use-case readiness explicit without unlocking the use cases.

Rows should cover at least:

- Policy_Local PL-S lane;
- Document Translator DT-CVF lane;
- corpus intelligence scan layer;
- memory/retrieval pack handoff;
- operator review only.

Each row must state:

- required router inputs;
- allowed outputs;
- forbidden outputs;
- required operator checkpoint;
- live-proof requirement if provider/OCR/runtime behavior is claimed;
- current readiness state.

### DIR-T6 - Later Deterministic Source Implementation

Purpose: implement only after the contracts survive rebuttal and T0-T5 closure.

Candidate source:

- a small Python module adjacent to EXA-T2, if source ownership confirms that
  extraction foundation is the right package;
- focused tests for invalid signals, blocked source types, operator-review
  propagation, no-raw-content fields, and downstream adapter boundaries.

This tranche must be separately authorized by fresh GC-018 and source-verified
work order. It is not authorized by this draft.

### DIR-T7 - Later Runtime Pilot

Purpose: run a bounded live/local pilot only after contracts and source are
closed.

This is held until:

- operator supplies a bounded sample corpus;
- live-provider/OCR/runtime scope is explicitly authorized if needed;
- diagnostics and receipts are defined;
- release-quality governance proof rules are satisfied when governance behavior
  is claimed.

## Work Plan

1. Send this draft to Claude for adversarial rebuttal.
2. Require Claude to classify each critique as blocker, improvement, or
   non-blocking disagreement.
3. Codex incorporates or rejects rebuttal points in a final roadmap revision.
4. Only after final roadmap acceptance may DIR-T0 be opened with fresh GC-018
   and a source-verified work order.
5. Keep Document Translator DT-CVF-T0 and Policy_Local PL-S1 separate unless a
   later operator decision explicitly sequences them after DIR.

## Dispatch Boundary

This draft is not a dispatch packet.

No worker may implement the router from this draft alone. A future work order
must include:

- Source Verification Block;
- Roadmap-to-Work-Order Trace Matrix;
- dependency-release evidence from this final roadmap;
- explicit allowed file paths;
- explicit no-runtime/no-provider/no-OCR boundary unless later authorized;
- required proof commands;
- worker commit mode.

## Claude Rebuttal Gate

Claude should rebut this roadmap before finalization.

Required rebuttal questions:

1. Does the proposed router duplicate EXA-T2 scan routing instead of composing
   it?
2. Are `DocumentProfile`, `DocumentIntent`, and `DocumentStructureSignals`
   scoped too broadly for a foundation tranche?
3. Which tranche should remain doc-only, and which should become source/test
   implementation?
4. Does any language accidentally authorize OCR, provider, retrieval, external
   repo edits, or Policy_Local mutation?
5. Are Policy_Local and Document Translator sufficiently isolated as downstream
   adapters?
6. Are any current CVF owner surfaces missing from the Source Verification
   table?
7. Should semantic chunking/context handoff be earlier, later, or out of DIR
   scope?
8. Should cost/provider routing be advisory-only forever, or just blocked until
   live-proof authorization?
9. Are the acceptance criteria machine-checkable enough?
10. What is the smallest useful DIR-T0 that reduces risk without creating a
    speculative abstraction stack?

Claude's output should include:

- `ACCEPT`, `DEFER`, or `REJECT` disposition for the roadmap structure;
- blocker list, if any;
- proposed tranche changes;
- missing source-owner checks;
- claim-boundary risks;
- recommended final-roadmap edits.

## Acceptance Criteria

This draft is acceptable for Claude rebuttal only if:

1. It keeps EXA-T2 as the scan-route owner.
2. It separates scan-layer decisions from document-intelligence routing.
3. It keeps Document Translator and Policy_Local downstream and separately
   gated.
4. It forbids runtime/OCR/provider/external repo edits until later authorized
   work orders.
5. It records proposed doc-only fields as proposed, not existing runtime facts.
6. It includes a Claude rebuttal gate before finalization.
7. It includes public export disposition and claim boundary.

## Verification / Evidence

Drafting evidence:

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

Required before finalizing this roadmap:

- Claude rebuttal artifact under `docs/reviews/`;
- Codex final incorporation decision;
- reviewer-fast or applicable governance hook pass;
- no untracked external use-case edit included in the roadmap commit.

## Governed Work Lifecycle

`INTAKE -> DRAFT -> REBUTTAL -> FINAL_ROADMAP -> GC-018 -> WORK_ORDER -> BUILD -> REVIEW -> FREEZE`

- INTAKE: operator identified DIR as a foundation step that helps CVF and scan
  layer.
- DRAFT: this artifact proposes the route architecture and questions.
- REBUTTAL: Claude challenges duplication, scope, owner boundaries, and claim
  safety.
- FINAL_ROADMAP: Codex incorporates accepted critique.
- GC-018: DIR-T0 receives a fresh baseline only after finalization.
- WORK_ORDER: implementation or doc closure requires source verification.
- BUILD: no build is authorized yet.
- REVIEW: Codex reviews worker returns before commit.
- FREEZE: readiness claims require closed artifacts and applicable gates.

## Claim Boundary

This draft proposes a foundation roadmap for critique. It does not prove
document intelligence behavior, extraction accuracy, OCR quality, provider
behavior, routing correctness, retrieval quality, Policy_Local readiness,
Document Translator readiness, public readiness, production readiness, release
readiness, cost savings, memory reinjection, high-risk promotion, or
autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance draft for Claude rebuttal; no public-sync batch is
authorized.
