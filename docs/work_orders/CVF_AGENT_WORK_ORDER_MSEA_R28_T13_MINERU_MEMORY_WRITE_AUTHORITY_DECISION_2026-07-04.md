# CVF Agent Work Order - MSEA R28 T13 MinerU Memory Write Authority Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T13-MINERU-MEMORY-WRITE-AUTHORITY-DECISION

rawMemoryReleased: false

dispatchBaseHead: 4cd04307

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T13.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. R28-T12 material commit
`91cc1422` accepted a deterministic metadata-only admission readout helper,
and session-sync commit `4cd04307` permits fresh memory-write authority
work-order authoring if the operator selects that lane. The operator selected
the T13-T16 sequence in this session.

Do-not-misread notes: this packet authorizes only docs-only decision matrix
authoring and a worker return. It does not authorize source/test
implementation, checker/hook edits, MinerU runtime execution, private/generated
content read, Candidate Group A import, memory/RAG write, provider proof,
external sync, standalone app work, legal/use-case deep dive, extraction
accuracy, document truth, legal quality, current-law correctness,
workflow-chain release claim, session-sync by worker, worker stage, worker
commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the
Source Verification Block, and checker source for worker-created outputs before
writing any file.

Return contract: create only the named decision matrix and worker return, run
worker-return fast gate and pre-implementation autorun, leave changes
uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | accepted R28-T12 closure evidence and current operator T13-T16 selection |
| Intake role | worker authors docs-only source-verified decision matrix |
| Scope classification | bounded decision artifact; no runtime/provider/public/private-content/memory-write behavior |
| Reviewer role | reviewer/closer validates decision matrix, worker return, gates, no-commit discipline, and memory hold |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; docs-only worker changes remain pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require source/test implementation, checker/hook/session edit, MinerU runtime execution, private/generated content read, memory/RAG write, provider/live proof, public-sync, standalone app work, legal/use-case deep dive, dependency install, destructive command, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Create a T13 memory-write authority decision matrix that selects whether T14
may implement a deterministic metadata-only memory-record candidate builder.
T13 must keep actual memory/RAG write unauthorized and must separate
candidate-building authority from store-write authority.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | create named matrix and worker return only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker artifacts, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator asked to proceed from T13-T16 using accepted T12 closure evidence | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` and `CVF_SESSION/state/entries/nextAllowedMove.json` route next allowed move to fresh memory-write authority work-order authoring if selected | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V36_2026-07-04.md` names the same next allowed move and parked checkpoints | ACCEPT |
| R28-T12 closure | material commit `91cc1422` accepted the admission readout and preserved memory-write hold | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_2026-07-04.md` | ACCEPT |

## Operator Checkpoint

| Checkpoint | Resolution |
| --- | --- |
| Operator selected T13-T16 | ACCEPT - begin with T13 authority decision because actual write remains held |
| Scope ceiling | ACCEPT - T13 is docs-only decision matrix and worker return |
| Parked lanes | HELD - actual memory/RAG write, runtime, private/generated content read, provider/live proof, public-sync, checker/hook edit, app, legal/use-case, and production workflow-chain claims remain unauthorized |
| Return route | ACCEPT - worker returns uncommitted artifacts for reviewer/closer closure |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T12 material closure | `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` and material commit `91cc1422` | ACCEPT |
| R28-T12 closure state entry | `CVF_SESSION/state/entries/mseaR28T12MineruMemoryOwnerAdmissionReadoutImplementationClosure20260704.json` records `MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTED` and `FUTURE_MEMORY_WRITE_WORK_ORDER_REQUIRED` | ACCEPT |
| R28-T12 session-sync routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at session-sync commit `4cd04307` | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `4cd04307` before authoring | ACCEPT |
| Worker execution release | R28-T13 dispatch artifacts and gates must exist before worker begins; this packet supplies that release after commit | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md`;
- create `docs/reviews/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`;
- source-verify T13 decision rows against current T12 evidence and current source symbols;
- select exactly one route token:
  `MEMORY_RECORD_CANDIDATE_BUILDER_READY`,
  `MEMORY_WRITE_AUTHORITY_HELD_PENDING_SOURCE`,
  or `MEMORY_WRITE_AUTHORITY_PARKED`;
- state whether T14 may proceed and what T16 remains blocked from doing.

Forbidden scope:

- no source/test implementation, checker/hook edit, session edit, active
  handoff edit, AGENTS.md edit, runtime adapter, Web, MCP, model-router,
  package lifecycle, public-sync clone, dependency install, or unrelated
  documentation edit;
- no MinerU command, model/cache mutation, parser/OCR/VLM/API/router/Gradio/
  Docker/WSL execution, local service startup, runtime smoke, or provider/live
  proof;
- no private source document body read and no generated output content read,
  quotation, copy, import, stage, or commit;
- no Candidate Group A import, committed runtime receipt instance, memory-layer
  write, RAG write, extraction-accuracy claim, document-truth claim, legal
  advice quality claim, current-law correctness claim, production workflow-chain
  claim, worker stage, worker commit, or push.

Risk ceiling: R0/R1 documentation-only decision work; no runtime/provider/private-data/public action.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| T13 decision matrix | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| T13 worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| source/test/checker/hook/session paths | not worker-owned in R28-T13 | forbidden |
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
| checker source for worker return and reference matrix gates | READ_BEFORE_WRITING_OUTPUTS |

## Preflight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Capture execution base | `git rev-parse --short HEAD` | record in worker return |
| Confirm worktree status | `git status --short --untracked-files=all` | record exact pending paths |
| Confirm planned worker output paths | `Test-Path` for the T13 matrix and worker return | no conflicting existing R28-T13 worker artifact |
| Read checker/output source | direct file reads of applicable reference, review, trace, delta, public-export, worker-return, and dispatch-quality checkers | record exact headings/tokens before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm worktree state | worker return trace |
| 2 | Read worker-output checker source and all Source Verification Block files before editing | Checker Source Read-Ahead Block in worker return and matrix |
| 3 | Create the T13 memory-write authority decision matrix with one route token | matrix |
| 4 | Create worker return summarizing source verification, route decision, changed files, gates, no-commit status, and next recommendation | worker return |
| 5 | Run worker-return fast gate and pre-implementation autorun on the worker changed range | command evidence |
| 6 | Leave changes uncommitted and return for reviewer closure | `git status --short --untracked-files=all` and HEAD unchanged |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker or packet-shape failures directly by
reading the failing checker and matching the required artifact shape. Worker
should return to orchestrator only for a source contradiction, forbidden-scope
need, live/provider/public/private-content requirement, source/test/checker/
hook/session edit requirement, dependency install, destructive action, or
missing authority that makes completion impossible.

## Return-To-Orchestrator Conditions

| Condition | Required worker response |
| --- | --- |
| Decision matrix and worker return completed inside allowed scope with gates passing | return `COMPLETE_PENDING_REVIEW` and leave changes uncommitted |
| Source contradiction blocks a decision route | return `BLOCKED_WITH_REASON` with exact source conflict |
| Any needed action is outside allowed scope | return `BLOCKED_WITH_REASON`; do not expand into runtime, memory, public, checker, session, source, test, or private-output work |
| Gate failure inside allowed scope | repair by reading the failing checker and rerun the gate before returning |
| Worker accidentally stages or commits | stop and return `BLOCKED_WITH_REASON`; reviewer/closer owns recovery |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T13 --title "MinerU Memory Write Authority Decision" --date 2026-07-04 --base 4cd04307 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T13 source verification, dependency release, docs-only matrix scope, no-memory-write boundary, worker manifest, checker-output read-ahead mandate, handoff control, and held memory-write boundary |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `MEMORY_WRITE_AUTHORITY_DECISION`; `MEMORY_RECORD_CANDIDATE_BUILDER_READY`; `MEMORY_WRITE_STILL_NOT_AUTHORIZED_BY_T13`; `FUTURE_MEMORY_RECORD_CANDIDATE_WORK_ORDER_REQUIRED` |
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
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created matrix and return require their own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Current session routing allows a fresh memory-write authority work order if selected, while memory/RAG write remains held. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| T12 closure recorded accepted admission readout implementation and future memory-write work-order requirement. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T12MineruMemoryOwnerAdmissionReadoutImplementationClosure20260704.json` | lines 20-25 | `selectedImplementationDisposition`; `futureAuthorityRequired` | active session state entry | ACCEPT |
| T12 worker return states future memory write still requires a separate fresh authority packet. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` | lines 68-73 and 87-90 | `FUTURE_MEMORY_WRITE_WORK_ORDER_REQUIRED` | T12 worker return | ACCEPT |
| Receipt writer owns the accepted T12 readout dataclass and payload renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 120 and 462 | `MineruMemoryOwnerAdmissionReadout`; `mineru_memory_owner_admission_readout_payload` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer keeps T12 memory write unauthorized through a stable token. | VALUE_SET | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 23 and 133 | `MEMORY_WRITE_NOT_AUTHORIZED_BY_T12`; `memory_write_disposition` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer exposes `future_authority_required` on the T12 readout. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 135 and 472 | `future_authority_required`; `futureAuthorityRequired` | MinerU metadata receipt writer | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime/source status |
| --- | --- | --- |
| `MEMORY_WRITE_AUTHORITY_DECISION` | T13 decision-matrix classification field | DOC_ONLY_NEW |
| `MEMORY_RECORD_CANDIDATE_BUILDER_READY` | selected route if T13 releases T14 metadata-only candidate-builder work | DOC_ONLY_NEW |
| `MEMORY_WRITE_STILL_NOT_AUTHORIZED_BY_T13` | explicit T13 hold on actual memory/RAG write | DOC_ONLY_NEW |
| `FUTURE_MEMORY_RECORD_CANDIDATE_WORK_ORDER_REQUIRED` | future authority requirement for T14 if T13 selects the candidate-builder route | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`
priorVerificationAnchor: `91cc1422`
freshRecomputeRequired: true
recomputeReason: T13 creates a new decision matrix, so source facts and dependency release evidence must be recomputed against current HEAD.
unicodePathHandling: Use literal paths and UTF-8-safe command output for local paths; do not normalize or rewrite filenames.
extractedTextAuthority: AUXILIARY_ONLY

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` |
| priorVerificationAnchor | `91cc1422` |
| freshRecomputeRequired | true |
| recomputeReason | T13 creates a new decision matrix, so source facts and dependency release evidence must be recomputed against current HEAD |
| unicodePathHandling | Use literal paths and UTF-8-safe command output for local paths; do not normalize or rewrite filenames |
| extractedTextAuthority | AUXILIARY_ONLY |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact path existence | `Test-Path` returned false for T13 baseline, work order, matrix, and worker-return paths before authoring | ACCEPT |
| Token search for T13 packet title | `rg -n "MSEA-R28-T13|MEMORY_WRITE_AUTHORITY_DECISION|MinerU Memory Write Authority Decision" docs CVF_SESSION AGENT_HANDOFF_V36_2026-07-04.md CVF_SESSION_MEMORY.md` was run before authoring; no existing T13 artifact collision was found | ACCEPT |
| Collision decision | No existing T13 dispatch, decision matrix, or worker-return artifact was present before authoring | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; worker returns uncommitted matrix/review artifacts; reviewer/closer commits accepted material; session-sync steward updates continuity |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=4cd04307; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch changes are paired GC-018 and work order only; worker changes are named matrix and worker return only |
| traceScope(phase, actor) | dispatcher trace in this work order and baseline; worker trace in worker return; reviewer trace through commit steward and gate evidence; session-sync trace in active handoff/front door/state |
| commitOwner(phase) | dispatch author may commit dispatch; WORKER_MUST_NOT_COMMIT; reviewer/closer commits accepted material; session-sync steward commits protected continuity |
| crossBatchIsolation | MSEA-R28-T13 only; do not mix T13 with runtime/provider/live/private-output/public-sync/source/test/checker/hook/session changes or another tranche |
| nextMoveSurfaces | once accepted T13 material commit exists, session-sync steward must update `CVF_SESSION_MEMORY.md`, active state sources, generated active state, bootstrap read model, and active handoff |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return per governed artifact gotcha 30 |
| reviewerOwnedClosurePaths | worker return plus T13 decision matrix if accepted |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| T13 decision matrix under the reference area | derive reference structural headings, trace labels if applicable, public-export disposition, external-intake routing, and claim-boundary tokens before writing |
| worker return under the reviews area | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |

Literal-shape reminders: do not list required worker-output sections as
backticked heading strings before the real section; write source-not-found
disposition spelling instead of the exact blocked enum in literalTokensReviewed;
avoid broad dependency-placeholder wording unless the row cites the accepted
artifact path and commit.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | create docs-only source-verified decision matrix selecting one route token |
| `docs/reviews/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md` | create worker return with command evidence and no-commit statement |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`
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
| decision route | T13 matrix contains exactly one selected route token |
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
| AC1 | Worker creates the T13 decision matrix and worker return only | `git status --short --untracked-files=all` |
| AC2 | Decision matrix selects exactly one route token and preserves actual memory/RAG write hold | matrix and worker return |
| AC3 | Decision matrix explicitly releases or holds T14 metadata-only memory-record candidate builder scope | matrix |
| AC4 | T16 actual memory/RAG write remains held unless later source-backed store authority exists | matrix claim boundary |
| AC5 | Worker-return fast gate, pre-implementation autorun, reviewer steward, and material pre-commit hook pass before closure | command evidence |

## Review Gate

Reviewer/closer must verify that the worker did not implement source/test
changes, did not write memory/RAG, did not edit checker/hook/session surfaces,
and did not create optional completion review unless required. Reviewer/closer
must run reviewer-return commit steward and pre-commit before material closure.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T13 MinerU Memory Write Authority Decision dispatch, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell (`git`, `rg`, `python governance/compat/*`), apply_patch |
| Target paths | this work order and paired GC-018 baseline |
| Allowed scope source | operator requested T13-T16 sequence using accepted T12 closure evidence; active session next move permits fresh memory-write authority work-order authoring if selected |
| Before status evidence | clean worktree at HEAD `4cd04307`; `git status --short --untracked-files=all` returned empty output before dispatch authoring |
| After status evidence | two untracked dispatch artifacts only; HEAD unchanged at `4cd04307` before dispatch commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only |
| Claim boundary | docs-only T13 decision dispatch; no runtime/private-output/memory/public/provider/source/test/checker/session implementation claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t13-dispatch-2026-07-04` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| T13 matrix present and source-verified | PASS or BLOCKED with reason |
| Worker return present and gate-clean | PASS or BLOCKED with reason |
| No forbidden source/test/runtime/memory/public/provider/session path touched by worker | PASS or BLOCKED with reason |
| T14 next authority selected or held | PASS or BLOCKED with reason |
| Actual memory/RAG write remains held in T13 | PASS or BLOCKED with reason |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| storageAction | DOCUMENTATION_ONLY_WITH_REASON |
| storageRoot | N/A with reason: T13 creates governed reference/review artifacts only |
| indexUpdate | N/A with reason: no file-storage index is modified |
| claimBoundary | no storage adapter, memory store, RAG store, S3, public-sync, or runtime persistence behavior is authorized |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> R28-T13 memory-write authority decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired GC-018 baseline |
| Disposition | ADAPT: convert accepted T12 admission readout evidence into a bounded decision matrix for future memory-record candidate work |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session edit, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T13 work order for memory-write authority decision |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, or external action is executed or observed. |
| invocationBoundary | local document authoring and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | work-order dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T13 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.

## Claim Boundary

This work order authorizes only a docs-only T13 authority decision matrix and
worker return. It does not authorize source/test implementation, checker/hook
edits, MinerU runtime execution, private/generated content read, Candidate
Group A import, memory/RAG write, provider/live proof, public-sync, standalone
app work, legal/use-case deep dive, extraction accuracy, document truth, legal
quality, current-law correctness, workflow-chain production readiness,
session-sync by worker, worker stage, worker commit, or push.

