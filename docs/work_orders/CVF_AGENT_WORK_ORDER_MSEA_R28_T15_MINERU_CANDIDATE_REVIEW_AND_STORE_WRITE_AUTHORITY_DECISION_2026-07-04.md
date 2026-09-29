# CVF Agent Work Order - MSEA R28 T15 MinerU Candidate Review And Store Write Authority Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T15-MINERU-CANDIDATE-REVIEW-AND-STORE-WRITE-AUTHORITY-DECISION

rawMemoryReleased: false

dispatchBaseHead: 13b22b94

closureBaseHead: REVIEWER_TO_SET

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T15.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. T14 material commit
`1b367302` accepted a deterministic metadata-only memory-record candidate
builder and session-sync commit `13b22b94` permits T15 work-order authoring
only. This dispatch releases worker execution only after it is committed and
pre-dispatch gates pass.

Do-not-misread notes: this packet authorizes only docs-only candidate review,
store-write authority decision matrix, and worker return. It does not authorize
actual memory/RAG write, memory-store adapter implementation, vectorization,
retrieval, checker/hook edits, MinerU runtime execution, private/generated
content read, Candidate Group A import, provider proof, public-sync,
standalone app work, legal/use-case deep dive, extraction accuracy, document
truth, legal quality, current-law correctness, workflow-chain release claim,
session-sync by worker, worker stage, worker commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the
Source Verification Block, and checker source for worker-created outputs before
writing any file.

Return contract: create only the T15 decision matrix and worker return, run
worker-return fast gate and pre-implementation autorun, leave changes
uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | accepted R28-T14 closure evidence and operator T13-T16 selection |
| Intake role | worker performs docs-only authority decision |
| Scope classification | deterministic docs-only candidate review and store-write authority decision; no runtime/provider/public/private-content/memory-write behavior |
| Reviewer role | reviewer/closer validates decision matrix, worker return, gates, no-commit discipline, and memory hold/release boundary |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; worker changes remain pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require memory/RAG write, store adapter implementation, checker/hook/session edit, MinerU runtime, private/generated content read, provider/live proof, public-sync, dependency install, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Decide whether the accepted T14 metadata-only memory-record candidate and
source-verified durable memory-store owner surfaces are sufficient to release
future T16 work-order authoring for actual memory-store write, or whether T16
must remain held pending an adapter/mapping packet.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | create T15 decision matrix and worker return only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker artifacts, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator asked to proceed from T13-T16 using accepted T14 evidence | ACCEPT |
| Active session state | bootstrap and nextAllowedMove route next move to T15 work-order authoring only | ACCEPT |
| R28-T14 closure | material commit `1b367302` selected candidate ready for review and future store authority requirement | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_2026-07-04.md` | ACCEPT |

## Operator Checkpoint

| Checkpoint | Resolution |
| --- | --- |
| Operator selected T13-T16 | ACCEPT - T15 proceeds only because T14 closed candidate-builder scope |
| Scope ceiling | ACCEPT - T15 is docs-only decision matrix and worker return |
| Parked lanes | HELD - actual memory/RAG write, runtime, private/generated content read, provider/live proof, public-sync, checker/hook edit, app, legal/use-case, and production workflow-chain claims remain unauthorized |
| Return route | ACCEPT - worker returns uncommitted artifacts for reviewer/closer closure |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T14 material closure | `docs/reviews/CVF_MSEA_R28_T14_MINERU_MEMORY_RECORD_CANDIDATE_BUILDER_WORKER_RETURN_2026-07-04.md` and material commit `1b367302` | ACCEPT |
| R28-T14 selected candidate | `CVF_SESSION/state/entries/mseaR28T14MineruMemoryRecordCandidateBuilderClosure20260704.json` records `MEMORY_RECORD_CANDIDATE_READY_FOR_REVIEW` | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `13b22b94` before authoring | ACCEPT |
| Worker execution release | T15 dispatch artifacts and gates must exist before worker begins; this packet supplies that release after commit | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md`;
- create `docs/reviews/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`;
- decide whether future T16 work-order authoring is released or held;
- keep memory/RAG write unauthorized in T15 itself.

Forbidden scope:

- no source/test/checker/hook/session/handoff/AGENTS.md edit by worker;
- no memory/RAG write, store adapter implementation, vectorization, retrieval,
  provider/live proof, MinerU runtime execution, private/generated content
  read, Candidate Group A import, public-sync, Web/MCP/model-router work,
  dependency install, standalone app, legal/use-case deep dive,
  extraction-accuracy claim, document-truth claim, legal-quality claim,
  current-law correctness claim, production workflow-chain claim, worker stage,
  worker commit, or push.

Risk ceiling: docs-only authority decision and review packet only.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| T15 decision matrix | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| T15 worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| source/test/checker/hook/session/public/runtime paths | not worker-owned in R28-T15 | forbidden |
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
| Confirm planned worker output paths | `Test-Path` for T15 matrix and worker return | no conflicting existing R28-T15 worker artifacts |
| Read checker/output source | direct file reads of applicable worker-return and governance checkers | record exact headings/tokens before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm worktree state | worker return trace |
| 2 | Read worker-output checker source and all Source Verification Block files before editing | Checker Source Read-Ahead Block |
| 3 | Create T15 decision matrix with Source Verification Block and selected T16 disposition | matrix diff |
| 4 | Create worker return summarizing source verification, decision, changed files, gates, no-commit status, and next recommendation | worker return |
| 5 | Run worker-return fast gate and pre-implementation autorun | command evidence |
| 6 | Leave changes uncommitted and return for reviewer closure | `git status --short --untracked-files=all` and HEAD unchanged |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker, formatting, source-verification, or
packet-shape failures directly by reading the failing checker and matching the
required shape. Worker should return to orchestrator only for a source
contradiction, forbidden-scope need, live/provider/public/private-content
requirement, checker/hook/session edit requirement, dependency install,
destructive action, or missing authority that makes completion impossible.

## Return-To-Orchestrator Conditions

| Condition | Required worker response |
| --- | --- |
| Matrix and worker return completed inside allowed scope with gates passing | return `COMPLETE_PENDING_REVIEW` and leave changes uncommitted |
| Source contradiction blocks decision | return `BLOCKED_WITH_REASON` with exact source conflict |
| Any needed action is outside allowed scope | return `BLOCKED_WITH_REASON`; do not expand into runtime, memory, public, checker, session, private-output, or provider work |
| Gate failure inside allowed scope | repair by reading the failing checker/test and rerun the gate before returning |
| Worker accidentally stages or commits | stop and return `BLOCKED_WITH_REASON`; reviewer/closer owns recovery |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T15 --title "MinerU Candidate Review And Store Write Authority Decision" --date 2026-07-04 --base 13b22b94 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | docs-only WORKER_MUST_NOT_COMMIT authority decision tranche |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T15 source verification, dependency release, docs-only decision scope, no-memory-write boundary, worker manifest, checker-output read-ahead mandate, handoff control, and held T16 boundary |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `storeWriteAuthorityDecision`; `selectedT16Disposition`; `MEMORY_STORE_WRITE_WORK_ORDER_AUTHORING_READY`; `MEMORY_STORE_WRITE_HELD_PENDING_ADAPTER_MAPPING` |
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
| T14 closed with candidate ready for review and future store authority required. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T14MineruMemoryRecordCandidateBuilderClosure20260704.json` | fields `candidateDisposition`; `futureAuthorityRequired`; `t15Disposition`; `t16Disposition` | `MEMORY_RECORD_CANDIDATE_READY_FOR_REVIEW`; `FUTURE_MEMORY_STORE_WRITE_AUTHORITY_REQUIRED` | active session state entry | ACCEPT |
| T14 source exposes a metadata-only record candidate dataclass, builder, and payload. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 143, 509, and 591 | `MineruMemoryRecordCandidate`; `build_mineru_memory_record_candidate`; `mineru_memory_record_candidate_payload` | MinerU metadata receipt writer | ACCEPT |
| T14 source keeps memory write unauthorized for the candidate. | VALUE_SET | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 25 and 157-159 | `MEMORY_WRITE_NOT_AUTHORIZED_BY_T14`; `future_authority_required` | MinerU metadata receipt writer | ACCEPT |
| Durable memory store exposes write/read interfaces and durable write input/receipt types. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 33-63 and 89-93 | `DurableMemoryReceipt`; `DurableMemoryWriteInput`; `DurableMemoryStore.write` | Learning Plane durable memory store | ACCEPT |
| Durable memory store write path rejects raw payloads and requires policy authorization. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 134-142, 191-230, and 232-291 | `hasRawPayload`; `policyDecision`; `actorAuthorized`; `raw_memory_payload_rejected`; `durable_memory_write_authorized` | Learning Plane durable memory store | ACCEPT |
| Durable memory receipt remains summary-only with no raw release or reinjection. | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 33-49 and 169-174 | `summaryOnly`; `canReinject`; `rawMemoryReleased` | Learning Plane durable memory receipt | ACCEPT |
| R27 scan-to-memory route requires receipt, quality, source pointer, downstream-use status, and claim boundary before future memory write. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 74-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | R27 decision ledger | ACCEPT |
| R24-T4 private-output policy keeps private/generated output content out of successor routing. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 44-54 and 212 | `sourceInputSlot`; `privateOutputDisposition`; policy claim boundary | R24-T4 policy reference | ACCEPT |
| T13 kept T16 held unless later source-backed store-write authority exists. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | lines 67-73 | `T16 Hold Conditions` | T13 decision matrix | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Source status |
| --- | --- | --- |
| `storeWriteAuthorityDecision` | T15 docs-only decision on whether future T16 work-order authoring is released or held | DOC_ONLY_NEW |
| `selectedT16Disposition` | T15 selected route for future T16 authoring or hold | DOC_ONLY_NEW |
| `MEMORY_STORE_WRITE_WORK_ORDER_AUTHORING_READY` | possible T15 decision token if source-backed authority is sufficient | DOC_ONLY_NEW |
| `MEMORY_STORE_WRITE_HELD_PENDING_ADAPTER_MAPPING` | possible T15 decision token if mapping remains insufficient | DOC_ONLY_NEW |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | create docs-only decision matrix with selected T16 disposition |
| `docs/reviews/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md` | create worker return with command evidence and no-commit statement |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; worker returns uncommitted docs-only decision artifacts; reviewer/closer commits accepted material; session-sync steward updates continuity |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=13b22b94; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch changes are paired GC-018 and work order only; worker changes are T15 decision matrix and T15 worker return only |
| traceScope(phase, actor) | dispatcher trace in this work order and baseline; worker trace in worker return; reviewer trace through commit steward and gate evidence; session-sync trace in active handoff/front door/state |
| commitOwner(phase) | dispatch author may commit dispatch; WORKER_MUST_NOT_COMMIT; reviewer/closer commits accepted material; session-sync steward commits protected continuity |
| crossBatchIsolation | MSEA-R28-T15 only; do not mix T15 with runtime/provider/live/private-output/public-sync/checker/hook/session changes or another tranche |
| nextMoveSurfaces | once accepted T15 material commit exists, session-sync steward must update `CVF_SESSION_MEMORY.md`, active state sources, generated active state, bootstrap read model, and active handoff |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return per governed artifact gotcha 30 |
| reviewerOwnedClosurePaths | T15 decision matrix; T15 worker return |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`
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
| worker-return fast gate | `python governance/compat/run_worker_return_fast_gate.py` |
| pre-implementation autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` |
| no-commit discipline | worker return states HEAD unchanged and changes uncommitted |

## Verification Commands

| Phase | Command | Required result |
| --- | --- | --- |
| worker fast gate | `python governance/compat/run_worker_return_fast_gate.py` | PASS before reviewer acceptance |
| worker autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` | PASS before reviewer acceptance |
| reviewer steward | `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce` | PASS before material commit |
| material hook | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | PASS before material commit |

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker changes only T15 matrix and T15 worker return | `git status --short --untracked-files=all` |
| AC2 | Matrix source-verifies T14 candidate and durable memory-store authority surfaces | matrix Source Verification Block |
| AC3 | Matrix selects exactly one future T16 disposition | matrix decision section |
| AC4 | T15 itself does not write memory/RAG or edit runtime/source/test/session/checker files | worker return and git status |
| AC5 | Actual memory/RAG write remains unauthorized until a future accepted T16 packet | matrix claim boundary |

## Review Gate

Reviewer/closer must verify that the worker did not run MinerU, did not read
private/generated content, did not write memory/RAG, did not edit checker/hook/
session/source/test surfaces, and did not create optional completion review
unless required. Reviewer/closer must run reviewer-return commit steward and
pre-commit before material closure.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T15 MinerU Candidate Review And Store Write Authority Decision dispatch, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell (`git`, `rg`, `python governance/compat/*`), apply_patch |
| Target paths | this work order and paired GC-018 baseline |
| Allowed scope source | operator requested T13-T16 sequence; T14 closure selected candidate ready for review and future store authority requirement |
| Before status evidence | clean worktree at HEAD `13b22b94`; `git status --short` returned empty output before dispatch authoring |
| After status evidence | two untracked dispatch artifacts only; HEAD unchanged at `13b22b94` before dispatch commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only |
| Claim boundary | T15 docs-only authority decision dispatch; no runtime/private-output/memory/public/provider/checker/session/source implementation claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t15-dispatch-2026-07-04` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| T15 decision matrix present and source-verified | PASS or BLOCKED with reason |
| Worker return present and gate-clean | PASS or BLOCKED with reason |
| No forbidden runtime/memory/public/provider/session/source/test/checker path touched by worker | PASS or BLOCKED with reason |
| T15 selected T16 authoring-ready or held disposition | PASS or BLOCKED with reason |
| Actual memory/RAG write remains held in T15 | PASS or BLOCKED with reason |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| storageAction | DOCUMENTATION_ONLY_WITH_REASON |
| storageRoot | N/A with reason: T15 creates no storage root and writes no memory/RAG store |
| indexUpdate | N/A with reason: no file-storage index is modified |
| claimBoundary | no storage adapter, memory store, RAG store, S3, public-sync, or runtime persistence behavior is authorized |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> T14 candidate builder -> T15 store-write authority decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired GC-018 baseline |
| Disposition | ADAPT accepted T14 candidate into a bounded source-backed store-write authority decision |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session/source edit, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T15 work order for candidate review and store-write authority decision |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store write, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime or memory-store receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, or external action is executed or observed. |
| invocationBoundary | docs-only authority decision and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | work-order dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T15 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.

## Claim Boundary

This work order authorizes only a docs-only candidate review and store-write
authority decision matrix plus worker return. It does not authorize actual
memory/RAG write, store adapter implementation, checker/hook edits, MinerU
runtime execution, private/generated content read, Candidate Group A import,
provider/live proof, public-sync, standalone app work, legal/use-case deep
dive, extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain production readiness, session-sync by worker,
worker stage, worker commit, or push.
