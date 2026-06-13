# CVF Agent Work Order - DICE-T1 Document Intelligence Control Envelope Runtime

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-13

Owner: Codex (orchestrator)

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `579962d7`

executionBaseHead: `579962d7`

closureBaseHead: `WORKER_MUST_NOT_SET`

sourceAuthority:
`docs/baselines/CVF_GC018_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_2026-06-13.md`

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:
`docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_COMPLETION_2026-06-13.md`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/state/**`;
`CVF_SESSION_MEMORY.md`;
`AGENT_HANDOFF_V18_2026-06-12.md`

GC-018:
`docs/baselines/CVF_GC018_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`

Predecessor tranche:
`docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`

## Purpose

Implement a bounded local deterministic DICE-T1 Document Intelligence Control
Envelope source module plus focused tests. Claude must compose existing
EXA-T2 scan-route, scan outcome report, and DIR route-decision owner surfaces
without redefining scan dispositions, authorization gates, downstream
capabilities, OCR confidence, provider/OCR execution, retrieval behavior, or
downstream use-case readiness.

This work order is CVF foundation hardening. It is not Document Translator
implementation work.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator request | operator asked Codex to continue and create the Claude work order after DICE-T0 closure and hardening | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md` | ACCEPT |
| DICE-T0 completion | `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md` | ACCEPT |
| DICE-T0 contract matrix | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_2026-06-13.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatches roadmap update, fresh GC-018, and this work order |
| Worker | Claude | authors allowed-scope source, tests, and worker-return packet only |
| Reviewer / closer | Codex | reviews, fixes reviewer-owned issues, runs closure gates, commits |

## Intake Role Routing Decision

Intake summary: DICE-T0 closed and recorded DICE-MC-01 through DICE-MC-10.
The operator asked Codex to continue with a Claude work order. The selected
lane is DICE-T1, a local deterministic foundation implementation and test
harness.

Scope classification: bounded local source plus focused tests plus one
worker-return packet.

Risk sensitivity: medium governance risk because DICE-T1 creates runtime
symbols, but risk remains bounded by local deterministic execution only, no
provider/API/OCR/retrieval action, no external repo access, no public-sync,
and no readiness/cost/quality claim.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Claude acts as worker under `WORKER_MUST_NOT_COMMIT`;
Codex remains reviewer, closer, and committer.

Escalation condition: return `BLOCKED_SCOPE_EXPANSION` if Claude needs real
documents, external Document Translator files, Policy_Local files, OCR,
provider/API calls, retrieval runtime, corpus ingestion, public-sync,
session-state edits, generated aggregate edits, governance-checker edits, or a
claim that exceeds local deterministic foundation proof.

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`
5. `docs/baselines/CVF_GC018_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_2026-06-13.md`
6. `docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md`
7. `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`
8. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py`
9. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`
10. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`
11. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`
12. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py`
13. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_outcome_report.py`
14. this work order

## Startup Acknowledgment Required

Claude must begin with:

`Startup acknowledged: current mode=dice_t1_document_intelligence_control_envelope_runtime_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=DICE-T1; next allowed move=Claude implements allowed-scope DICE-T1 local deterministic envelope source and tests under WORKER_MUST_NOT_COMMIT and returns uncommitted artifacts; parked checkpoint=DT-CVF-T0, Policy_Local PL-S1, external Document Translator repo, OCR/provider/retrieval, corpus ingestion, public-sync, T12, readiness/cost/quality claims remain parked.`

## Commit Mode And Base-Anchor Lifecycle

| Anchor | Value | Owner | Disposition |
| --- | --- | --- | --- |
| dispatchBaseHead | `579962d7` | Codex | ACCEPT |
| executionBaseHead | `579962d7` | Claude | ACCEPT |
| closureBaseHead | `WORKER_MUST_NOT_SET` | Codex reviewer | ACCEPT |
| Commit mode | `WORKER_MUST_NOT_COMMIT` | Codex | ACCEPT |

Claude must not commit. Claude must record worker-return base/head and
`git status --short` output in the worker-return packet.

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_FOR_CLAUDE_2026-06-13.md`
- `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_COMPLETION_2026-06-13.md`
- `docs/baselines/CVF_GC018_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_2026-06-13.md`
- `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/**`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

pendingStatusTokensAllowedBeforeReview: `WORKER_RETURN_SUBMITTED_UNCOMMITTED`,
`DRAFT`, `HOLD_*`

forbiddenClosedEquivalentResidue: `COMPLETE_PENDING_REVIEW`,
`NOT_EXECUTED_YET`, `WORKER_RETURNS_PENDING`, `PRE_CLOSURE_NOT_RUN`,
`FAIL_EXPECTED_PENDING_FINALITY`, `DISPATCHED` as current status

predecessorClosureFactSource:
`docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`

## Dependency Release Evidence

| Dependency | Required evidence | Disposition |
| --- | --- | --- |
| DICE-T0 closed | `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md` at material closure commit `a355cd7a` | ACCEPT |
| DICE-T0 session synchronized | session-sync commit `bd3c9f7c` | ACCEPT |
| DICE-T0 finding promotion completed | hardening commit `dbe3ddca` plus handoff sync `579962d7` | ACCEPT |
| Operator selected DICE-T1 work order | 2026-06-13 operator instruction in chat | ACCEPT |
| Fresh DICE-T1 baseline | `docs/baselines/CVF_GC018_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_2026-06-13.md` | ACCEPT |

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

## Current Runtime Freshness Verification

| Source fact | Verification command or evidence | Disposition |
| --- | --- | --- |
| DIR route symbols and DICE-MC-08 source | `rg -n "AuthorizationGate|DownstreamCapability|DocumentIntelligenceRouteDecision|downstream_eligibility|_derive_downstream_eligibility|decide_document_intelligence_route" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | ACCEPT |
| EXA-T2 scan symbols | `rg -n "ScanRouteDisposition|ScanRouteDecision|decide_scan_route" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | ACCEPT |
| Scan outcome symbols | `rg -n "ScanOutcomeReport|operator_review_required|findings|build_scan_outcome_report" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | ACCEPT |
| Extraction confidence owner | `rg -n "ExtractionQualityReport|mean_ocr_confidence" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | ACCEPT |
| Prior line-anchor defect | `build_scan_outcome_report` is cited at definition line 131, not a continuation line | ACCEPT |

## New Runtime Symbols Authorized

The following labels may be introduced only in the new DICE-T1 source module
and tests. They must not be represented as pre-existing source facts.

| New runtime symbol | Required purpose | Boundary |
| --- | --- | --- |
| `DocumentIntelligenceControlEnvelopeInput` | local deterministic envelope input | new DICE-T1 module only |
| `DocumentIntelligenceControlEnvelopeResult` | local deterministic envelope result | new DICE-T1 module only |
| `EnvelopeAdapterHandoff` | local downstream handoff decision record | must not bypass DIR gate |
| `build_document_intelligence_control_envelope` | local deterministic composer function | must not call OCR/provider/retrieval |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Roadmap evidence | Work-order section | Verification |
| --- | --- | --- | --- |
| DICE-T1 local deterministic runtime | roadmap DICE-T1 Detail | Purpose; Allowed Implementation Scope | focused tests pass |
| compose existing owner surfaces | roadmap Relationship To DIR | Source Verification Block; Deliverables | source imports and tests |
| preserve DICE-MC candidates | DICE-T0 matrix Machine-Check Candidates | Required DICE-MC Proofs | test names and assertions |
| handle DICE-MC-08 passthrough | DICE-T0 completion finding DICE-T0-F4 | DICE-MC-08 requirement | targeted test fixture |
| keep use cases downstream | roadmap Scope and Non-Goals | Forbidden Path Manifest | worker return negative evidence |
| keep provider/OCR/retrieval blocked | roadmap Authorization | Forbidden Path Manifest; Claim Boundary | no provider/OCR/retrieval calls |

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope gate failures without asking the operator.
Claude must return `BLOCKED_SCOPE_EXPANSION` only if the repair would touch
forbidden paths, alter the claim boundary, require external repo access, run
OCR/provider/API, mutate retrieval/corpus/session state, edit governance
checkers/generated aggregates, use public-sync, or make readiness/cost/quality
claims.

## Pre-Flight Checks

Before implementation, Claude must:

1. Read every Required First Reads path.
2. Confirm `git rev-parse --short HEAD`.
3. Confirm `git status --short`.
4. Confirm the external Document Translator and Policy_Local trees are not
   read, listed, hashed, modified, or imported.
5. Use current source files over memory or prior summaries for every source
   fact.

## Single-Agent Multi-Role Control Block

| Control item | Requirement | Disposition |
| --- | --- | --- |
| Role separation ledger | Codex=orchestrator/reviewer/closer; Claude=worker only | ACCEPT |
| Evidence basis independent of memory | closure must rely on git diff, source files, tests, worker return, reviewer-fast, pre-closure, and pre-push evidence | ACCEPT |
| Self-review boundary | Claude worker return is not independent review; Codex review is required | ACCEPT |
| Escalation conditions | any need for external files, OCR/provider/API, retrieval, session mutation, public-sync, governance checker edit, generated aggregate edit, or widened claim returns blocked | ACCEPT |
| Gate sequence | Codex dispatch uses pre-dispatch; Claude worker uses required proofs; Codex review uses reviewer-fast and closure gates | ACCEPT |
| Raw memory boundary | rawMemoryReleased=false | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact:
`docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`

recomputeReason: DICE-T1 creates local deterministic runtime symbols and must
source-map current owner surfaces directly.

unicodePathHandling: literal UTF-8-safe repository paths only.

extractedTextAuthority: N/A with reason - no sample document text or OCR output
is authorized.

Evidence reuse is limited to source-verified contracts and current runtime
source. Memory summaries and chat reports are not source authority for runtime
fields.

## Allowed Implementation Scope

Claude may create or update:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py`;
- `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/__init__.py` only if needed to
  expose the new local module without changing existing behavior;
- this work order only to add worker-return evidence if needed.

Reviewer-owned closure may update this work order, the paired GC-018, the
parent roadmap, the worker return, the completion review, and active session
continuity files.

## Allowed / Forbidden Scope

Allowed scope:

- create the DICE-T1 local deterministic envelope module;
- create the DICE-T1 focused tests;
- create the DICE-T1 worker-return packet;
- run local deterministic tests and governance checkers listed in the Required
  Proof Manifest;
- cite current in-repo source files and current governed docs.

Forbidden scope:

- external Document Translator source access;
- Policy_Local source access or mutation;
- OCR/provider/API/service execution;
- retrieval runtime or corpus ingestion;
- route/API wiring;
- governance checker edits;
- generated aggregate edits;
- session-state, handoff, or front-door mutation by Claude;
- public-sync;
- readiness, cost, quality, hosted, production, release, or public claims.

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `D:/UNG DUNG AI/TOOL AI 2026/CVF-Workspace/Document_Translator` | do not read, list, hash, import, or modify |
| external Policy_Local tree | do not read, list, hash, import, or modify |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | consume only; do not modify DIR owner source |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | consume only; do not modify EXA-T2 scan owner source |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | consume only; do not modify scan report owner source |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | consume only; do not modify extraction confidence owner source |
| `governance/compat/**` | do not create or modify checkers |
| `CVF_SESSION/**` | worker session-state mutation not authorized |
| `CVF_SESSION_MEMORY.md` | worker front-door mutation not authorized |
| `AGENT_HANDOFF*.md` | worker handoff mutation not authorized |
| public-sync repository | not authorized |
| provider key files and environment files | not authorized |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `D:/UNG DUNG AI/TOOL AI 2026/CVF-Workspace/Document_Translator` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Do not read, list, hash, import, or modify |
| external Policy_Local tree | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Do not read, list, hash, import, or modify |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Consume only; do not modify |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Consume only; do not modify |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Consume only; do not modify |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Consume only; do not modify |
| `governance/compat/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Do not edit checkers |
| `CVF_SESSION/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Codex reviewer owns session sync |
| `CVF_SESSION_MEMORY.md` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Codex reviewer owns front-door sync |
| `AGENT_HANDOFF*.md` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Codex reviewer owns handoff sync |
| public-sync repository | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Do not access |
| provider key files and environment files | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Do not access |

## Deliverables

Claude must create:

1. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py`
2. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py`
3. `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md`

The source module must include:

- deterministic dataclasses or typed records for envelope input, result, and
  downstream handoff decision;
- a composer function named `build_document_intelligence_control_envelope`;
- explicit claim boundary text;
- no OCR/provider/retrieval imports or calls;
- no redefinition of `ScanRouteDisposition`, `AuthorizationGate`, or
  `DownstreamCapability` literal values.

The test module must include:

- focused tests for DICE-MC-01 through DICE-MC-10;
- a DICE-MC-08 test that preserves the existing DIR passthrough invariant for
  `LOCAL_DETERMINISTIC_ALLOWED`;
- negative tests proving blocked/provider/OCR/operator-review gates do not
  produce an unqualified downstream handoff;
- tests proving scan findings and operator-review requirement are preserved;
- tests proving no second OCR confidence threshold is introduced.

The worker-return packet must include:

- files created or modified;
- `git status --short`;
- proof manifest results;
- DICE-MC proof table;
- negative evidence for external tree access, OCR/provider/API, retrieval,
  corpus ingestion, public-sync, generated aggregate edits, governance checker
  edits, readiness, cost, and quality claims;
- worker disposition `WORKER_RETURN_SUBMITTED_UNCOMMITTED`.

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | Yes | DICE-T1 local deterministic envelope source |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | Yes | DICE-T1 focused test harness |
| `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md` | Yes | worker return, evidence, findings, and claim boundary |

## Work-Order Fulfillment Manifest

Claude must report each Required Artifact Manifest row as created, updated, or
blocked. Claude must also report each Forbidden Path Manifest row as untouched
or blocked.

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| envelope source symbol | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | `build_document_intelligence_control_envelope` | Yes |
| envelope source result | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | `DocumentIntelligenceControlEnvelopeResult` | Yes |
| DICE-MC-08 regression | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | `DICE-MC-08` | Yes |
| blocked handoff regression | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | `DICE_MUST_NOT_FORWARD_BLOCKED_HANDOFF` | Yes |
| worker return disposition | `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md` | `WORKER_RETURN_SUBMITTED_UNCOMMITTED` | Yes |

## Required DICE-MC Proofs

| Candidate ID | Required worker proof |
| --- | --- |
| DICE-MC-01 | test or static assertion that DICE does not define a new `ScanRouteDisposition` literal owner |
| DICE-MC-02 | test or static assertion that DICE does not define a new `AuthorizationGate` literal owner |
| DICE-MC-03 | test or static assertion that DICE does not define a new `DownstreamCapability` literal owner |
| DICE-MC-04 | blocked/provider/OCR gates do not produce unqualified downstream handoff |
| DICE-MC-05 | operator review required is surfaced in the envelope result |
| DICE-MC-06 | `scan_decision_digest` is preserved |
| DICE-MC-07 | `decision_version` is preserved |
| DICE-MC-08 | downstream eligibility is not widened beyond DIR output while preserving existing DIR passthrough behavior |
| DICE-MC-09 | no new OCR confidence threshold is introduced |
| DICE-MC-10 | scan findings are preserved without filtering or suppression |

## Execution Plan

1. Create the DICE-T1 local deterministic envelope source module.
2. Import and compose existing DIR, EXA-T2 scan-route, and scan outcome report
   owner surfaces.
3. Add focused tests for DICE-MC-01 through DICE-MC-10.
4. Add the DICE-MC-08 passthrough invariant fixture.
5. Run the Required Commands and record outcomes.
6. Create the worker-return packet with evidence, negative scope proof, and
   findings.

## Evidence Requirements

Claude's worker-return packet must include:

- `WORKER_MUST_NOT_COMMIT observed`;
- `rawMemoryReleased=false`;
- changed-file list from `git status --short`;
- proof command summaries;
- DICE-MC proof table;
- explicit statement that no external Document Translator tree, Policy_Local
  tree, public-sync, OCR/provider/API, retrieval runtime, corpus ingestion,
  generated aggregate, governance checker, or session-state mutation was used;
- Finding-To-Governance Learning Disposition, using `N/A_WITH_REASON` only if
  no reusable finding appears.

## Acceptance Criteria

| Criterion | Evidence |
| --- | --- |
| DICE-T1 source module exists and exposes required symbols | Required Proof Manifest |
| Focused tests cover DICE-MC-01 through DICE-MC-10 | test names and assertions |
| DICE-MC-08 preserves current DIR passthrough invariant | targeted test fixture |
| Blocked/OCR/provider/operator-review gates do not create unqualified handoff | tests |
| Scan findings and operator-review requirement are preserved | tests |
| No external files or services are used | worker-return negative evidence |
| Worker does not commit | `git status --short` and return packet |

## Required Commands

Claude must run, at minimum:

- `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py`
- `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_outcome_report.py EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py`
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`

Claude must not run provider/OCR/live-proof commands.

## Review Gate

Codex reviewer must verify:

- Claude honored `WORKER_MUST_NOT_COMMIT`;
- all Required Artifact Manifest rows are present or explicitly blocked;
- Required Proof Manifest commands pass or have safe diagnostics;
- DICE-MC-01 through DICE-MC-10 are addressed;
- DICE-MC-08 does not reject current DIR passthrough behavior;
- no forbidden path, external repo, provider/OCR service, retrieval runtime,
  generated aggregate, governance checker, public-sync, or session-state
  mutation was used by Claude;
- claim boundary remains foundation-only.

## Closure Checklist

| Item | Required closure disposition |
| --- | --- |
| Worker return reviewed | PASS, BLOCKED, or N/A with reason |
| Required artifacts reviewed | PASS, BLOCKED, or N/A with reason |
| Required proofs reviewed | PASS, BLOCKED, or N/A with reason |
| DICE-MC coverage reviewed | PASS, BLOCKED, or N/A with reason |
| Forbidden scope checked | PASS, BLOCKED, or N/A with reason |
| Finding-To-Governance disposition reviewed | PASS, BLOCKED, or N/A with reason |
| Session continuity updated by reviewer | PASS, BLOCKED, or N/A with reason |

## Return-To-Orchestrator Conditions

Return `BLOCKED_SCOPE_EXPANSION` if any required result needs:

- real document files;
- external Document Translator or Policy_Local access;
- OCR/provider/API execution;
- retrieval runtime or corpus ingestion;
- public-sync;
- governance checker edits;
- generated aggregate edits;
- session-state mutation by Claude;
- readiness, cost, quality, hosted, production, release, or public claims.

## Operator Checkpoint

No operator checkpoint is required for local deterministic DICE-T1 source and
tests. Operator checkpoint is required if Claude or Codex needs real
documents, external Document Translator access, Policy_Local access,
OCR/provider/API execution, retrieval runtime, corpus ingestion, public-sync,
or readiness/cost/quality claims.

## Write Ownership

| Path | Owner | Boundary |
| --- | --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | Claude | create/update allowed |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | Claude | create/update allowed |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/__init__.py` | Claude | optional export-only update if needed |
| `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md` | Claude | create/update allowed |
| completion review artifact | Codex | reviewer-owned closure only |

## Mandatory Gate-Failure Remediation Protocol

If an allowed-scope gate fails, Claude must repair and rerun it before
returning. Claude must not ask the operator whether to fix allowed-scope
failures. Claude must stop only when a fix would exceed Allowed scope or touch
forbidden paths.

## Self-Reported Gate Evidence Consistency

Worker-return PASS claims must include command names and outcomes. A handwritten
PASS claim without command evidence is not closure evidence for Codex.

## Pending Artifact Evidence Finality

No required artifact may be left as pending in the worker return. If an
artifact cannot be created, return `BLOCKED_SCOPE_EXPANSION` with the exact
blocking reason.

## Export Surface Decision

Public export is not authorized. This DICE-T1 tranche remains private
provenance until a separate public-sync work order is created.

## Claim Boundary

DICE-T1 is local deterministic CVF foundation source and tests only. It does
not authorize OCR/provider/API execution, external app tree access, retrieval
behavior changes, route/API wiring, corpus ingestion, public-sync, document
correctness claims, extraction accuracy claims, provider quality claims,
readiness claims, cost claims, memory reinjection, high-risk promotion, or
autonomous mutation.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dispatch work order. No public-sync
artifact or public catalog claim is authorized.
