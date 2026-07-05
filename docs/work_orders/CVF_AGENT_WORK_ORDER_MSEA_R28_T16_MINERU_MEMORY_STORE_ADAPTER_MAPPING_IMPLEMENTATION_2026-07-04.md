# CVF Agent Work Order - MSEA R28 T16 MinerU Memory Store Adapter Mapping Implementation

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T16-MINERU-MEMORY-STORE-ADAPTER-MAPPING-IMPLEMENTATION

rawMemoryReleased: false

dispatchBaseHead: c9528ec8

closureBaseHead: REVIEWER_TO_SET

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T16.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. T15 material commit
`50afaa0f` selected `MEMORY_STORE_WRITE_WORK_ORDER_AUTHORING_READY` for T16
authoring only. Session-sync commit `c9528ec8` routes the next move to T16
work-order authoring.

Do-not-misread notes: this packet authorizes only a deterministic source/test
mapping helper and worker return. It does not authorize actual memory/RAG
write, durable-store invocation, vectorization, retrieval, checker/hook edits,
MinerU runtime execution, private/generated content read, Candidate Group A
import, provider proof, public-sync, standalone app work, legal/use-case deep
dive, extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain release claim, session-sync by worker, worker
stage, worker commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the
Source Verification Block, and checker source for worker-created outputs before
writing any file.

Return contract: implement only the allowed source/test mapping helper and
T16 worker return, run focused pytest, worker-return fast gate, and
pre-implementation autorun, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | accepted R28-T15 closure evidence and operator T13-T16 selection |
| Intake role | worker performs bounded source/test mapping implementation |
| Scope classification | deterministic source/test mapping helper; no runtime/provider/public/private-content/memory-write behavior |
| Reviewer role | reviewer/closer validates implementation, tests, worker return, gates, no-commit discipline, and memory-write hold boundary |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; worker changes remain pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require durable-store invocation, memory/RAG write, checker/hook/session edit, MinerU runtime, private/generated content read, provider/live proof, public-sync, dependency install, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Implement the T16 summary-only adapter mapping helper that converts a T14
MinerU memory-record candidate into a durable-memory write-input candidate
payload without calling the durable memory store or writing memory/RAG.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | implement allowed source/test mapping helper and worker return only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker artifacts, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator asked to proceed from T13-T16 | ACCEPT |
| Active session state | bootstrap and nextAllowedMove route next move to T16 work-order authoring only | ACCEPT |
| R28-T15 closure | material commit `50afaa0f` selected T16 authoring-ready route with mapping required before any write | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_2026-07-04.md` | ACCEPT |

## Operator Checkpoint

| Checkpoint | Resolution |
| --- | --- |
| Operator selected T13-T16 | ACCEPT - T16 proceeds only because T15 closed source-backed authoring release |
| Scope ceiling | ACCEPT - T16 is source/test mapping helper and worker return only |
| Parked lanes | HELD - actual memory/RAG write, runtime, private/generated content read, provider/live proof, public-sync, checker/hook edit, app, legal/use-case, and production workflow-chain claims remain unauthorized |
| Return route | ACCEPT - worker returns uncommitted artifacts for reviewer/closer closure |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T15 material closure | `docs/reference/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md`, worker return, and material commit `50afaa0f` | ACCEPT |
| R28-T15 selected route | `CVF_SESSION/state/entries/mseaR28T15MineruCandidateReviewAndStoreWriteAuthorityDecisionClosure20260704.json` records `MEMORY_STORE_WRITE_WORK_ORDER_AUTHORING_READY` | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `c9528ec8` before authoring | ACCEPT |
| Worker execution release | T16 dispatch artifacts and gates must exist before worker begins; this packet supplies that release after commit | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- create `docs/reviews/CVF_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`;
- implement deterministic constants, dataclass, builder, and payload renderer
  for summary-only durable-memory write-input candidate mapping;
- add focused tests for deterministic mapping, metadata-only behavior,
  fail-closed unsafe candidate inputs, and no durable-store invocation.

Forbidden scope:

- no durable memory-store invocation, memory/RAG write, vectorization,
  retrieval, provider/live proof, MinerU runtime execution, private/generated
  content read, Candidate Group A import, public-sync, Web/MCP/model-router
  work, dependency install, standalone app, legal/use-case deep dive,
  extraction-accuracy claim, document-truth claim, legal-quality claim,
  current-law correctness claim, production workflow-chain claim, checker/hook/
  session/handoff/AGENTS.md edit by worker, worker stage, worker commit, or
  push.

Risk ceiling: local deterministic mapping helper/test behavior and worker
return only.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| receipt-writer source and focused tests | worker creates changes, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| T16 worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| checker/hook/session/public/runtime/durable-store invocation paths | not worker-owned in R28-T16 | forbidden |
| any other path | not worker-owned | forbidden unless a revised work order authorizes it |

## Required First Reads

| Source | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V36_2026-07-04.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| this work order and paired GC-018 | READ |
| all source files in the Source Verification Block | SOURCE_VERIFIED |
| checker source for worker return | READ_BEFORE_WRITING_OUTPUTS |

## Preflight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Capture execution base | `git rev-parse --short HEAD` | record in worker return |
| Confirm worktree status | `git status --short --untracked-files=all` | record exact pending paths |
| Confirm planned worker return path | `Test-Path` for T16 worker return | no conflicting existing R28-T16 worker return |
| Read checker/output source | direct file reads of applicable worker-return and governance checkers | record exact headings/tokens before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm worktree state | worker return trace |
| 2 | Read worker-output checker source and all Source Verification Block files before editing | Checker Source Read-Ahead Block |
| 3 | Add T16 constants, dataclass, deterministic builder, and camelCase payload renderer to the allowed receipt-writer source | source diff |
| 4 | Add focused tests for mapping determinism, no raw/private/generated content fields, fail-closed policy, and no durable-store invocation | pytest evidence |
| 5 | Create worker return summarizing implementation, changed files, gates, no-commit status, and remaining actual-write hold | worker return |
| 6 | Run focused pytest, worker-return fast gate, and pre-implementation autorun | command evidence |
| 7 | Leave changes uncommitted and return for reviewer closure | `git status --short --untracked-files=all` and HEAD unchanged |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker, formatting, source-verification,
test, or packet-shape failures directly by reading the failing checker/test and
matching the required shape. Worker should return to orchestrator only for a
source contradiction, forbidden-scope need, live/provider/public/private-content
requirement, checker/hook/session edit requirement, dependency install,
destructive action, or missing authority that makes completion impossible.

## Return-To-Orchestrator Conditions

| Condition | Required worker response |
| --- | --- |
| Mapping helper, focused tests, and worker return completed inside allowed scope with gates passing | return `COMPLETE_PENDING_REVIEW` and leave changes uncommitted |
| Source contradiction blocks implementation | return `BLOCKED_WITH_REASON` with exact source conflict |
| Any needed action is outside allowed scope | return `BLOCKED_WITH_REASON`; do not expand into runtime, memory write, public, checker, session, private-output, or provider work |
| Gate/test failure inside allowed scope | repair by reading the failing checker/test and rerun before returning |
| Worker accidentally stages or commits | stop and return `BLOCKED_WITH_REASON`; reviewer/closer owns recovery |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T16 --title "MinerU Memory Store Adapter Mapping Implementation" --date 2026-07-04 --base c9528ec8 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | source/test WORKER_MUST_NOT_COMMIT mapping implementation tranche |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T16 source verification, dependency release, source/test mapping scope, no-memory-write boundary, worker manifest, checker-output read-ahead mandate, handoff control, and actual-write hold |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16_MAPPING_ONLY`; `MineruDurableMemoryWriteInputCandidate`; `build_mineru_durable_memory_write_input_candidate`; `mineru_durable_memory_write_input_candidate_payload` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router/memory behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, source verification, checker read-ahead, and no-commit discipline. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created return requires its own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T15 selected T16 authoring-ready route while keeping actual write unauthorized. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | Decision Summary | `MEMORY_STORE_WRITE_WORK_ORDER_AUTHORING_READY`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T15_DECISION_ONLY` | T15 decision matrix | ACCEPT |
| T14 source exposes a metadata-only memory-record candidate and payload renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 143, 509, and 591-602 | `MineruMemoryRecordCandidate`; `build_mineru_memory_record_candidate`; `mineru_memory_record_candidate_payload` | MinerU metadata receipt writer | ACCEPT |
| T14 source keeps downstream release held and memory write unauthorized. | VALUE_SET | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 22, 25, 157-159, and 535 | `DOWNSTREAM_RELEASE_HELD`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T14`; `future_authority_required` | MinerU metadata receipt writer | ACCEPT |
| T14 tests cover deterministic metadata-only candidate behavior and fail-closed unsafe readouts. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 470-587 | `test_memory_record_candidate_is_deterministic_and_metadata_only`; `test_memory_record_candidate_fails_closed_for_unsafe_readouts` | MinerU receipt writer tests | ACCEPT |
| Durable memory store write input requires id, scope, actor, actor role, summary, optional policy decision, authorization, and provenance score. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 52-63 and 195-203 | `DurableMemoryWriteInput`; `policyDecision`; `actorAuthorized`; `provenanceScore` | Learning Plane durable memory store | ACCEPT |
| Durable memory store rejects raw payload-like fields and low provenance before persistence. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 98, 137-143, and 252-263 | `MIN_PROVENANCE_SCORE`; `hasRawPayload`; `raw_memory_payload_rejected`; `low_provenance_score` | Learning Plane durable memory store | ACCEPT |
| Durable memory receipt remains summary-only with no raw release or reinjection. | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 35-49 and 160-175 | `summaryOnly`; `canReinject`; `rawMemoryReleased` | Learning Plane durable memory receipt | ACCEPT |
| Runtime memory hierarchy defines actor-role values and durable actor authorization lanes. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 10-18 values `OPERATOR`, `GOVERNOR`, `HUMAN`, `BUILDER`, `AI_AGENT`, `REVIEWER`, `SERVICE_AGENT`, `OBSERVER`, `ANALYST`, `unknown`; lines 173-204 durable actor lanes and `m1_durable_cross_session` | `RuntimeMemoryActorRole`; `allowedActors`; `m1_durable_cross_session` | Runtime memory hierarchy | ACCEPT |
| R27 scan-to-memory route requires receipt, quality, source pointer, downstream-use status, and claim boundary before future memory write. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 71-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | R27 decision ledger | ACCEPT |
| R24-T4 private-output policy keeps private/generated output content out of successor routing. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 43-56 and 212 | `sourceInputSlot`; `privateOutputDisposition`; policy claim boundary | R24-T4 policy reference | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Source status |
| --- | --- | --- |
| `MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTED` | proposed T16 implementation disposition token | DOC_ONLY_NEW |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16_MAPPING_ONLY` | proposed T16 memory-write hold token | DOC_ONLY_NEW |
| `MineruDurableMemoryWriteInputCandidate` | proposed Python dataclass for summary-only durable write input candidate | DOC_ONLY_NEW |
| `build_mineru_durable_memory_write_input_candidate` | proposed Python builder from T14 candidate to durable write input candidate | DOC_ONLY_NEW |
| `mineru_durable_memory_write_input_candidate_payload` | proposed Python payload renderer for stable camelCase output | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reference/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md`
priorVerificationAnchor: `50afaa0f`
freshRecomputeRequired: true
recomputeReason: T16 authorizes source/test implementation, so consumed symbols and durable-store owner surfaces must be source-verified against current HEAD.
unicodePathHandling: use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames.
extractedTextAuthority: N/A with reason
extractedTextAuthorityReason: no extracted text, private/generated output text, or document body is source authority for T16.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | add mapping constants, dataclass, deterministic builder, and payload renderer |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | add focused tests for T16 mapping and fail-closed boundaries |
| `docs/reviews/CVF_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` | create worker return with command evidence and no-commit statement |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; worker returns uncommitted source/test and worker-return artifacts; reviewer/closer commits accepted material; session-sync steward updates continuity |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=c9528ec8; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch changes are paired GC-018 and work order only; worker changes are allowed receipt-writer source, focused test, and T16 worker return only |
| traceScope(phase, actor) | dispatcher trace in this work order and baseline; worker trace in worker return; reviewer trace through commit steward and gate evidence; session-sync trace in active handoff/front door/state |
| commitOwner(phase) | dispatch author may commit dispatch; WORKER_MUST_NOT_COMMIT; reviewer/closer commits accepted material; session-sync steward commits protected continuity |
| crossBatchIsolation | MSEA-R28-T16 only; do not mix T16 with runtime/provider/live/private-output/public-sync/checker/hook/session changes or another tranche |
| nextMoveSurfaces | once accepted T16 material commit exists, session-sync steward must update `CVF_SESSION_MEMORY.md`, active state sources, generated active state, bootstrap read model, and active handoff |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return per governed artifact gotcha 30 |
| reviewerOwnedClosurePaths | allowed receipt-writer source; focused receipt-writer test; T16 worker return |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without heading prefixes. The worker return must include Purpose,
Target / Source, Scope / Methodology, Findings / Position, Risk / Corrective
Action, Checker Source Read-Ahead Block, Agent Operation Trace Block, Delta
Execution Claim Boundary Control Block, Public Export Disposition, External
Knowledge Intake Routing, Rescan Intelligence Hardening, Corpus Completeness
And Report Integrity, Finding-To-Governance Learning Disposition, Epistemic
Process Block, Claim Boundary, git status --short, Changed Files, Command
Evidence, Worker Experience Retrospective, and No-Commit Statement.

## Evidence Requirements

| Evidence | Required command or artifact |
| --- | --- |
| execution base | `git rev-parse --short HEAD` recorded in worker return |
| worktree status | `git status --short --untracked-files=all` recorded in worker return |
| focused pytest | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py -q` |
| worker-return fast gate | `python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` |
| pre-implementation autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` |
| no-commit discipline | worker return states HEAD unchanged and changes uncommitted |

## Verification Commands

| Phase | Command | Required result |
| --- | --- | --- |
| focused pytest | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py -q` | PASS before worker return |
| worker fast gate | `python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | PASS before reviewer acceptance |
| worker autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` | PASS before reviewer acceptance |
| reviewer steward | `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce` | PASS before material commit |
| material hook | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | PASS before material commit |

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker changes only allowed receipt-writer source, focused receipt-writer test, and T16 worker return | `git status --short --untracked-files=all` |
| AC2 | Implementation creates deterministic summary-only durable write-input candidate mapping from `MineruMemoryRecordCandidate` | source diff and focused tests |
| AC3 | Candidate payload has no raw OCR, extracted text, document body, private/generated output content, vector content, or durable-store receipt fields | focused tests |
| AC4 | T16 itself does not call durable store, write memory/RAG, vectorize, retrieve, run MinerU, or edit session/checker/hook/public paths | worker return and git status |
| AC5 | Actual memory/RAG write remains unauthorized after T16 mapping unless reviewer closure explicitly creates a later release condition | worker return claim boundary |

## Review Gate

Reviewer/closer must verify that the worker did not run MinerU, did not read
private/generated content, did not write memory/RAG, did not invoke durable
memory store, did not edit checker/hook/session/public surfaces, and did not
create optional completion review unless required. Reviewer/closer must run
reviewer-return commit steward and pre-commit before material closure.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T16 MinerU Memory Store Adapter Mapping Implementation dispatch, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell (`git`, `rg`, `python governance/compat/*`), apply_patch |
| Target paths | this work order and paired GC-018 baseline |
| Allowed scope source | operator requested T13-T16 sequence; T15 closure selected T16 authoring-ready with mapping required before any write |
| Before status evidence | clean worktree at HEAD `c9528ec8`; `git status --short` returned empty output before dispatch authoring |
| After status evidence | two untracked dispatch artifacts only; HEAD unchanged at `c9528ec8` before dispatch commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only |
| Claim boundary | T16 source/test mapping implementation dispatch; no runtime/private-output/memory-write/public/provider/checker/session implementation claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t16-dispatch-2026-07-04` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| T16 mapping source/test changes present and focused tests pass | PASS or BLOCKED with reason |
| Worker return present and gate-clean | PASS or BLOCKED with reason |
| No forbidden runtime/memory/public/provider/session/checker path touched by worker | PASS or BLOCKED with reason |
| Actual memory/RAG write remains held in T16 unless explicitly released by accepted closure evidence | PASS or BLOCKED with reason |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| storageAction | DOCUMENTATION_ONLY_WITH_REASON |
| storageRoot | N/A with reason: T16 dispatch creates no storage root and writes no memory/RAG store |
| indexUpdate | N/A with reason: no file-storage index is modified |
| claimBoundary | no storage adapter invocation, memory store write, RAG store, S3, public-sync, or runtime persistence behavior is authorized by dispatch |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> T15 store-write authority decision -> T16 adapter mapping |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired GC-018 baseline |
| Disposition | ADAPT accepted T15 authoring-ready route into a bounded source/test mapping implementation dispatch |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session edit, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T16 work order for memory-store adapter mapping implementation |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store write, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime or memory-store receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, or external action is executed or observed. |
| invocationBoundary | source/test mapping implementation dispatch and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | work-order dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T16 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.

## Claim Boundary

This work order authorizes only a bounded source/test implementation of a
deterministic summary-only durable-memory write-input candidate mapper plus
worker return. It does not authorize actual memory/RAG write, durable-store
invocation, vectorization, retrieval, checker/hook edits, MinerU runtime
execution, private/generated content read, Candidate Group A import,
provider/live proof, public-sync, standalone app work, legal/use-case deep
dive, extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain production readiness, session-sync by worker,
worker stage, worker commit, or push.
