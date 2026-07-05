# CVF Agent Work Order - MSEA R28 T14 MinerU Memory Record Candidate Builder

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T14-MINERU-MEMORY-RECORD-CANDIDATE-BUILDER

rawMemoryReleased: false

dispatchBaseHead: ef99f417

closureBaseHead: REVIEWER_TO_SET

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T14.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T14_MINERU_MEMORY_RECORD_CANDIDATE_BUILDER_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. T13 material commit
`0002de2d` selected `MEMORY_RECORD_CANDIDATE_BUILDER_READY` and session-sync
commit `ef99f417` permits T14 work-order authoring only. This dispatch releases
worker execution only after it is committed and pre-dispatch gates pass.

Do-not-misread notes: this packet authorizes only local metadata-only
source/test implementation and a worker return. It does not authorize actual
memory/RAG write, memory-store adapter, vectorization, retrieval, checker/hook
edits, MinerU runtime execution, private/generated content read, Candidate
Group A import, provider proof, public-sync, standalone app work, legal/use-case
deep dive, extraction accuracy, document truth, legal quality,
current-law correctness, workflow-chain release claim, session-sync by worker,
worker stage, worker commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the
Source Verification Block, and checker source for worker-created outputs before
writing any file.

Return contract: implement only the named source/test helper scope and worker
return, run focused pytest, worker-return fast gate, and pre-implementation
autorun, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T14_MINERU_MEMORY_RECORD_CANDIDATE_BUILDER_WORKER_RETURN_2026-07-04.md`

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | accepted R28-T13 closure evidence and operator T13-T16 selection |
| Intake role | worker implements bounded source/test helper |
| Scope classification | deterministic metadata-only source/test implementation; no runtime/provider/public/private-content/memory-write behavior |
| Reviewer role | reviewer/closer validates source/test diff, worker return, gates, no-commit discipline, and memory hold |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; worker changes remain pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require memory/RAG write, store adapter, checker/hook/session edit, MinerU runtime, private/generated content read, provider/live proof, public-sync, dependency install, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Implement a deterministic metadata-only memory-record candidate builder from
the accepted T12 admission readout. The candidate is review material for a
future memory owner/store decision; it is not a memory/RAG write.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | edit only allowed source/test paths and create worker return | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker artifacts, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator asked to proceed from T13-T16 using accepted T13 evidence | ACCEPT |
| Active session state | bootstrap and nextAllowedMove route next move to T14 work-order authoring only | ACCEPT |
| R28-T13 closure | material commit `0002de2d` selected future metadata-only candidate-builder work | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T14_MINERU_MEMORY_RECORD_CANDIDATE_BUILDER_2026-07-04.md` | ACCEPT |

## Operator Checkpoint

| Checkpoint | Resolution |
| --- | --- |
| Operator selected T13-T16 | ACCEPT - T14 proceeds only because T13 selected candidate-builder readiness |
| Scope ceiling | ACCEPT - T14 is local metadata-only source/test helper and worker return |
| Parked lanes | HELD - actual memory/RAG write, runtime, private/generated content read, provider/live proof, public-sync, checker/hook edit, app, legal/use-case, and production workflow-chain claims remain unauthorized |
| Return route | ACCEPT - worker returns uncommitted artifacts for reviewer/closer closure |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T13 material closure | `docs/reviews/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md` and material commit `0002de2d` | ACCEPT |
| R28-T13 selected route | `docs/reference/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` selected `MEMORY_RECORD_CANDIDATE_BUILDER_READY` | ACCEPT |
| R28-T13 closure state entry | `CVF_SESSION/state/entries/mseaR28T13MineruMemoryWriteAuthorityDecisionClosure20260704.json` records T14 work-order authoring release and T16 write hold | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `ef99f417` before authoring | ACCEPT |
| Worker execution release | T14 dispatch artifacts and gates must exist before worker begins; this packet supplies that release after commit | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- edit `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- edit `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- create `docs/reviews/CVF_MSEA_R28_T14_MINERU_MEMORY_RECORD_CANDIDATE_BUILDER_WORKER_RETURN_2026-07-04.md`;
- add deterministic metadata-only candidate dataclass, builder, payload, and
  focused tests;
- keep memory/RAG write unauthorized.

Forbidden scope:

- no checker/hook/session/handoff/AGENTS.md edit by worker;
- no memory/RAG write, store adapter, vectorization, retrieval, provider/live
  proof, MinerU runtime execution, private/generated content read, Candidate
  Group A import, public-sync, Web/MCP/model-router work, dependency install,
  standalone app, legal/use-case deep dive, extraction-accuracy claim,
  document-truth claim, legal-quality claim, current-law correctness claim,
  production workflow-chain claim, worker stage, worker commit, or push.

Risk ceiling: local deterministic metadata helper and focused tests only.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| allowed receipt writer source | worker edits, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| allowed focused receipt writer test | worker edits, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| T14 worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| checker/hook/session/public/runtime paths | not worker-owned in R28-T14 | forbidden |
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
| Confirm planned worker output path | `Test-Path` for T14 worker return | no conflicting existing R28-T14 worker artifact |
| Read checker/output source | direct file reads of applicable worker-return and governance checkers | record exact headings/tokens before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm worktree state | worker return trace |
| 2 | Read worker-output checker source and all Source Verification Block files before editing | Checker Source Read-Ahead Block |
| 3 | Add metadata-only candidate dataclass, builder, and payload in the allowed receipt writer source | source diff |
| 4 | Add focused tests for determinism, metadata-only payload, memory-write hold, source-pointer sensitivity, and unsafe readout rejection | test diff |
| 5 | Create worker return summarizing source verification, changed files, gates, no-commit status, and next recommendation | worker return |
| 6 | Run focused pytest, worker-return fast gate, and pre-implementation autorun | command evidence |
| 7 | Leave changes uncommitted and return for reviewer closure | `git status --short --untracked-files=all` and HEAD unchanged |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker, source, test, formatting, or
packet-shape failures directly by reading the failing checker/test and matching
the required shape. Worker should return to orchestrator only for a source
contradiction, forbidden-scope need, live/provider/public/private-content
requirement, checker/hook/session edit requirement, dependency install,
destructive action, or missing authority that makes completion impossible.

## Return-To-Orchestrator Conditions

| Condition | Required worker response |
| --- | --- |
| Source/test implementation and worker return completed inside allowed scope with gates passing | return `COMPLETE_PENDING_REVIEW` and leave changes uncommitted |
| Source contradiction blocks helper implementation | return `BLOCKED_WITH_REASON` with exact source conflict |
| Any needed action is outside allowed scope | return `BLOCKED_WITH_REASON`; do not expand into runtime, memory, public, checker, session, private-output, or provider work |
| Gate failure inside allowed scope | repair by reading the failing checker/test and rerun the gate before returning |
| Worker accidentally stages or commits | stop and return `BLOCKED_WITH_REASON`; reviewer/closer owns recovery |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T14 --title "MinerU Memory Record Candidate Builder" --date 2026-07-04 --base ef99f417 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | source/test WORKER_MUST_NOT_COMMIT implementation tranche |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T14 source verification, dependency release, helper/test scope, no-memory-write boundary, worker manifest, checker-output read-ahead mandate, handoff control, and held memory-write boundary |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `MineruMemoryRecordCandidate`; `build_mineru_memory_record_candidate`; `mineru_memory_record_candidate_payload`; `MEMORY_RECORD_CANDIDATE_READY_FOR_REVIEW`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T14_CANDIDATE_ONLY` |
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
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; New Source Symbols; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created return requires its own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T13 selected the metadata-only memory-record candidate builder route. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | lines 49-53 | `selectedRoute`; `t14Disposition` | T13 decision matrix | ACCEPT |
| T13 closure keeps actual memory/RAG write held and T16 blocked pending store-write authority. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T13MineruMemoryWriteAuthorityDecisionClosure20260704.json` | `selectedRoute`; `t16Disposition` fields | `MEMORY_RECORD_CANDIDATE_BUILDER_READY`; `T16_ACTUAL_MEMORY_RAG_WRITE_HELD_PENDING_SOURCE_BACKED_STORE_WRITE_AUTHORITY` | active session state entry | ACCEPT |
| Receipt writer exposes the T12 admission readout dataclass consumed by T14. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 120-136 | `MineruMemoryOwnerAdmissionReadout` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer exposes the T12 readout builder and payload renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 403 and 462-482 | `build_mineru_memory_owner_admission_readout`; `mineru_memory_owner_admission_readout_payload` | MinerU metadata receipt writer | ACCEPT |
| Existing T12 readout keeps output content unread and memory write unauthorized. | VALUE_SET | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 131-135 | `output_content_read`; `memory_write_authorized`; `memory_write_disposition`; `future_authority_required` | MinerU metadata receipt writer | ACCEPT |
| Focused receipt-writer tests already cover deterministic metadata-only admission readout behavior and unsafe candidate failures. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 343-367 and 449-456 | `test_memory_owner_admission_readout_is_deterministic_and_metadata_only`; `test_memory_owner_admission_readout_fails_closed_for_unsafe_candidates` | MinerU receipt writer tests | ACCEPT |

## New Source Symbols

| Symbol | Purpose | Source status |
| --- | --- | --- |
| `MineruMemoryRecordCandidate` | metadata-only candidate record for future memory-owner/store review | DOC_ONLY_NEW |
| `build_mineru_memory_record_candidate` | deterministic builder from T12 admission readout | DOC_ONLY_NEW |
| `mineru_memory_record_candidate_payload` | stable camelCase payload renderer | DOC_ONLY_NEW |
| `MEMORY_RECORD_CANDIDATE_READY_FOR_REVIEW` | candidate disposition token | DOC_ONLY_NEW |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T14_CANDIDATE_ONLY` | explicit T14 hold on actual memory/RAG write | DOC_ONLY_NEW |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | add deterministic metadata-only candidate dataclass, builder, and payload |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | add focused tests for deterministic candidate behavior and fail-closed holds |
| `docs/reviews/CVF_MSEA_R28_T14_MINERU_MEMORY_RECORD_CANDIDATE_BUILDER_WORKER_RETURN_2026-07-04.md` | create worker return with command evidence and no-commit statement |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; worker returns uncommitted source/test/review artifacts; reviewer/closer commits accepted material; session-sync steward updates continuity |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=ef99f417; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch changes are paired GC-018 and work order only; worker changes are allowed receipt writer source, allowed focused test, and T14 worker return only |
| traceScope(phase, actor) | dispatcher trace in this work order and baseline; worker trace in worker return; reviewer trace through commit steward and gate evidence; session-sync trace in active handoff/front door/state |
| commitOwner(phase) | dispatch author may commit dispatch; WORKER_MUST_NOT_COMMIT; reviewer/closer commits accepted material; session-sync steward commits protected continuity |
| crossBatchIsolation | MSEA-R28-T14 only; do not mix T14 with runtime/provider/live/private-output/public-sync/checker/hook/session changes or another tranche |
| nextMoveSurfaces | once accepted T14 material commit exists, session-sync steward must update `CVF_SESSION_MEMORY.md`, active state sources, generated active state, bootstrap read model, and active handoff |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T14_MINERU_MEMORY_RECORD_CANDIDATE_BUILDER_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return per governed artifact gotcha 30 |
| reviewerOwnedClosurePaths | allowed receipt writer source; allowed focused receipt writer test; T14 worker return |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T14_MINERU_MEMORY_RECORD_CANDIDATE_BUILDER_WORKER_RETURN_2026-07-04.md`
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
| focused pytest | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py -q` | PASS before reviewer acceptance |
| worker fast gate | `python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | PASS before reviewer acceptance |
| worker autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` | PASS before reviewer acceptance |
| reviewer steward | `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce` | PASS before material commit |
| material hook | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | PASS before material commit |

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker changes only allowed source/test files and T14 worker return | `git status --short --untracked-files=all` |
| AC2 | Candidate builder is deterministic and metadata-only | source diff and focused tests |
| AC3 | Candidate payload omits output file names and content-bearing fields | focused tests |
| AC4 | Actual memory/RAG write remains unauthorized | source constants, payload, tests, worker return |
| AC5 | T16 actual memory/RAG write remains held unless future source-backed store-write authority exists | worker return claim boundary |

## Review Gate

Reviewer/closer must verify that the worker did not run MinerU, did not read
private/generated content, did not write memory/RAG, did not edit checker/hook/
session surfaces, and did not create optional completion review unless
required. Reviewer/closer must run reviewer-return commit steward and
pre-commit before material closure.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T14 MinerU Memory Record Candidate Builder dispatch, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell (`git`, `rg`, `python governance/compat/*`), apply_patch |
| Target paths | this work order and paired GC-018 baseline |
| Allowed scope source | operator requested T13-T16 sequence; T13 closure selected metadata-only candidate-builder route |
| Before status evidence | clean worktree at HEAD `ef99f417`; `git status --short --untracked-files=all` returned empty output before dispatch authoring |
| After status evidence | two untracked dispatch artifacts only; HEAD unchanged at `ef99f417` before dispatch commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only |
| Claim boundary | T14 metadata-only implementation dispatch; no runtime/private-output/memory/public/provider/checker/session implementation claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t14-dispatch-2026-07-04` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| T14 source/test implementation present and source-verified | PASS or BLOCKED with reason |
| Worker return present and gate-clean | PASS or BLOCKED with reason |
| No forbidden runtime/memory/public/provider/session path touched by worker | PASS or BLOCKED with reason |
| Actual memory/RAG write remains held in T14 | PASS or BLOCKED with reason |
| T15 next authority is selected or held | PASS or BLOCKED with reason |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| storageAction | DOCUMENTATION_ONLY_WITH_REASON |
| storageRoot | N/A with reason: T14 creates no storage root and writes no memory/RAG store |
| indexUpdate | N/A with reason: no file-storage index is modified |
| claimBoundary | no storage adapter, memory store, RAG store, S3, public-sync, or runtime persistence behavior is authorized |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> T13 decision -> T14 metadata-only candidate builder |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired GC-018 baseline |
| Disposition | ADAPT accepted T13 evidence into a bounded metadata-only candidate-builder implementation |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session edit, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T14 work order for metadata-only memory-record candidate builder |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, or external action is executed or observed. |
| invocationBoundary | local source/test implementation and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | work-order dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T14 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.

## Claim Boundary

This work order authorizes only a local deterministic metadata-only
candidate-builder implementation, focused tests, and a worker return. It does
not authorize actual memory/RAG write, checker/hook edits, MinerU runtime
execution, private/generated content read, Candidate Group A import,
provider/live proof, public-sync, standalone app work, legal/use-case deep
dive, extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain production readiness, session-sync by worker,
worker stage, worker commit, or push.
