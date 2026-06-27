# CVF Document Intelligence Control Envelope Roadmap

Memory class: FULL_RECORD

Status: DICE_T1_PASS_BOUNDED

docType: roadmap

Date: 2026-06-13

Owner: Codex

rawMemoryReleased=false

## Purpose

Define the next CVF foundation lane after DIR-T2: a Document Intelligence
Control Envelope (DICE) that coordinates document profile, scan route,
authorization gate, confidence/review signal ownership, and provider/OCR cost
boundaries before any downstream use-case repo consumes document intelligence.

DICE is a reusable CVF foundation layer. It is not a Document Translator
implementation, not a Policy_Local implementation, and not a provider/OCR
runtime lane.

## Operator Decision

The operator selected continued CVF foundation hardening after DIR-T2 closure.
The selected direction is to open a new roadmap and work order for Claude,
with CVF foundation quality remaining priority one and downstream document
translation kept as a separate use case.

## Authorization

Authorized move: DICE-T1 closure as bounded local deterministic foundation
source and tests after Codex review of Claude's uncommitted worker return.

Not authorized: DICE-T2 operator packet sample, DICE-T3 provider/OCR
authorization design, DT-CVF-T0, Policy_Local PL-S1, public-sync, live proof,
external repo access, OCR/provider execution, retrieval route wiring, corpus
ingestion, or readiness/cost/quality claims.

## Decision

Proceed with DICE-T0 as the next CVF foundation lane. This decision keeps the
router foundation closed and moves one layer upward into reusable control
envelope design.

## Background

DIR-T0 through DIR-T2 closed a bounded deterministic Document Intelligence
Router foundation:

- DIR-T0 created the doc-only router contract matrix.
- DIR-T1 implemented the deterministic local router source and tests.
- DIR-T2 proved the router over synthetic metadata-only fixture cases.

DIR deliberately stays narrow. It composes EXA-T2 scan-route decisions and
emits authorization gates, but it does not define the broader control envelope
needed by downstream document workflows: who owns profile evidence, which
signals may become operator-visible review items, when provider/OCR/cost routes
remain blocked, and how use-case adapters must consume foundation outputs
without re-creating route semantics.

## Scope

DICE may define:

- a reusable document-control envelope above DIR and EXA-T2;
- ownership tables for profile, scan, route, review, confidence, provider/OCR,
  cost, and downstream adapter boundaries;
- a bounded artifact contract for operator-visible document control packets;
- machine-check candidates that keep use cases from bypassing DIR gates;
- release rules for later runtime work only after fresh authorization.

DICE must not:

- read, list, hash, or modify the external Document Translator clone;
- mutate Policy_Local, retrieval, corpus ingestion, route/API, OCR, provider,
  or public-sync surfaces;
- execute provider/API calls or OCR;
- claim production readiness, public readiness, cost savings, provider quality,
  document correctness, translation quality, or extraction accuracy;
- authorize memory reinjection, high-risk promotion, or autonomous mutation.

## Non-Goals

- Implement DICE-T2/T3 runtime/provider/OCR authorization design.
- Add route/API wiring, generated aggregates, or public-sync surfaces.
- Inspect or modify the external Document Translator clone.
- Inspect or modify Policy_Local.
- Execute OCR, providers, retrieval, or live governance proof.
- Make readiness, cost, quality, production, public, or release claims.

## Relationship To DIR

| Layer | Current owner | DICE stance |
| --- | --- | --- |
| Extraction quality | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | consume only; do not redefine confidence or quality flags |
| Scan route | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | consume only; do not duplicate scan dispositions |
| Operator scan report | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | reuse as one operator-visible evidence source |
| Document Intelligence Router | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | compose as required foundation route authority |
| Downstream use cases | future adapter-specific lanes | consume DICE/DIR outputs without claiming readiness |

## Work Plan

| Tranche | Goal | Prerequisite | Status |
| --- | --- | --- | --- |
| DICE-T0 | Doc-only control-envelope contract matrix and owner-source map | this roadmap plus fresh GC-018/work order | CLOSED_PASS_BOUNDED |
| DICE-T1 | Deterministic local envelope contract/test harness, if T0 proves source owner | DICE-T0 closure plus fresh GC-018 | CLOSED_PASS_BOUNDED |
| DICE-T2 | Operator-visible document control packet sample, if T1 proves stable contract | DICE-T1 closure plus fresh GC-018 | ELIGIBLE_FOR_FRESH_GC018 |
| DICE-T3 | Runtime/provider/OCR authorization design, if still needed | DICE-T2 closure plus explicit live-proof/key/quota authorization | HOLD_PENDING_RUNTIME_AUTH |

## DICE-T0 Detail

DICE-T0 is doc-only. Claude must produce a contract matrix that:

- maps existing source-owned fields and functions to DICE envelope roles;
- records accepted, deferred, and rejected ownership boundaries;
- defines no runtime symbols as already existing unless source-verified;
- separates provider/OCR/cost authorization from local deterministic routing;
- defines machine-check candidates for later enforcement;
- records a worker-return packet for Codex review.

Allowed artifacts for DICE-T0:

- `docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md`;
- `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`.

## Design Control Gate

| Control question | Required DICE-T0 answer |
| --- | --- |
| Does DICE duplicate DIR scan/authorization semantics? | It must reject duplication and consume DIR outputs. |
| Does DICE redefine extraction confidence? | It must reject redefinition and cite extraction owner surfaces. |
| Does DICE unlock provider/OCR execution? | It must keep provider/OCR blocked pending separate authorization. |
| Does DICE become Document Translator implementation work? | It must keep Document Translator as a downstream adapter lane only. |
| Does DICE claim runtime readiness? | It must not claim runtime, production, public, cost, or quality readiness. |

## DICE-T1 Detail

DICE-T1 is a bounded local deterministic implementation tranche. Claude must
create a source module and focused tests that compose existing EXA-T2 scan,
scan outcome report, and DIR route decision surfaces into a document-control
envelope without changing OCR/provider/retrieval behavior or downstream
adapter semantics.

Allowed artifacts for DICE-T1:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py`;
- `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md`.

DICE-T1 must carry forward DICE-MC-01 through DICE-MC-10 and must specifically
handle DICE-MC-08 without rejecting the current DIR passthrough invariant for
`LOCAL_DETERMINISTIC_ALLOWED`.

## Acceptance Criteria

DICE-T1 closure is acceptable only if:

- a fresh GC-018 baseline exists;
- a source-verified Claude work order exists and is closed bounded;
- focused DICE-T1 tests and combined DIR/scan-outcome/DICE tests pass;
- reviewer-fast and closure gates pass on a real changed range;
- the worker scope remains local deterministic source and tests only;
- external Document Translator, Policy_Local, OCR/provider, retrieval,
  public-sync, and readiness/cost/quality claims remain blocked.

## Verification

Dispatch verification included:

- `python governance/compat/check_work_order_dispatch_quality.py --base 579962d7 --head HEAD --enforce`;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 579962d7 --head HEAD`;
- local pre-commit governance chain before Codex dispatch commit.

Closure verification must include:

- `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py -v`;
- `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_outcome_report.py EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py -v`;
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 0fd52604 --head HEAD`;
- local pre-commit governance chain before Codex material closure commit.

## Evidence

Evidence for this roadmap is limited to current in-repo source, governed docs,
DIR-T2 closure evidence, and operator instruction. No external app tree,
provider service, OCR service, sample document, or public-sync evidence is
used.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| DIR-T2 closure | `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md`; material closure commit `e3395acc`; session-sync commit `bea8e1f1` | ACCEPT |
| Operator selected foundation lane | 2026-06-13 operator instruction to continue opening CVF foundation roadmap and Claude work order | ACCEPT |
| Document Translator use-case boundary | `docs/roadmaps/CVF_DOCUMENT_TRANSLATOR_CONTROL_ADAPTATION_ROADMAP_2026-06-13.md` keeps DT-CVF-T0 separate | ACCEPT |
| Current DIR source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | ACCEPT |
| Current EXA-T2 source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | ACCEPT |

## Corpus Completeness And Report Integrity

- Corpus task class: ROADMAP_SOURCE_AUTHORITY_SCOPE

- Corpus root: `d:/UNG DUNG AI/TOOL AI 2026/Controlled-Vibe-Framework-CVF`

- Snapshot time: 2026-06-13T00:00:00+07:00

- Enumeration command: filesystem-backed inline manifest from current repo
  paths; no external enumeration.

- Manifest artifact or inline manifest:

| Path or source | Status | Reason |
| --- | --- | --- |
| `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md` | READ | predecessor closure evidence |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | READ | current DIR owner source |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | READ | current EXA-T2 owner source |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | READ | current extraction quality owner source |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | READ | current operator scan report owner source |
| `docs/roadmaps/CVF_DOCUMENT_TRANSLATOR_CONTROL_ADAPTATION_ROADMAP_2026-06-13.md` | READ | downstream use-case boundary |
| external Document Translator clone | SKIPPED_WITH_REASON | explicitly out of scope for foundation roadmap |
| Policy_Local tree | SKIPPED_WITH_REASON | explicitly out of scope |
| OCR/provider/live services | DEFERRED | separate authorization required |
| public-sync repository | SKIPPED_WITH_REASON | no public export authorized |

- Manifest hash: N/A_WITH_REASON - inline manifest only; no external corpus
  snapshot generated.

- Processing ledger artifact or inline ledger: inline manifest above.

- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.

- Reconciliation: manifest=inline; ledger_terminal=allowed; exclusions=declared; unresolved=0.

- Unresolved files: 0

- Declared exclusions: external Document Translator clone, Policy_Local tree,
  OCR/provider/live services, sample documents, and public-sync repository.

- Unreadable or unsupported files: none.

- Aggregation check: PASS - no aggregated file count is claimed.

- Drift check: PASS - DICE-T0 work order source-verifies current line anchors
  before dispatch.

- Output traceability: roadmap sections map to the paired GC-018 and work
  order.

- Adversarial verification: external app/runtime evidence is excluded to
  prevent use-case drift.

- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | DIR-T0/T1/T2 closure artifacts and current extraction foundation source are the source authority | COMPLETE |
| Detailed source files checked | DICE-T0 work order source-verifies router, scan route, extraction quality, and scan outcome surfaces | COMPLETE |
| Accept/defer/reject dispositions required | DICE-T0 matrix must include owner boundary tables | COMPLETE |
| Adversarial review required | DICE-T0 must test for use-case drift, provider/OCR drift, and confidence redefinition | COMPLETE |
| Blind-spot delta | external app/runtime proof remains excluded until separate authorization | COMPLETE |

## Claim Boundary

This roadmap has closed DICE-T1 as a bounded local deterministic foundation
source and test tranche. It does not prove document intelligence runtime
behavior against real documents, document content correctness, extraction
accuracy, OCR quality, provider behavior, retrieval quality, Document
Translator readiness,
Policy_Local readiness, production readiness, public readiness, release
readiness, cost savings, quality improvement, memory reinjection, high-risk
promotion, or autonomous mutation.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation roadmap; no public-sync batch or public
catalog claim is authorized.

This is a private provenance roadmap. No public-sync batch or public catalog
claim is authorized.
