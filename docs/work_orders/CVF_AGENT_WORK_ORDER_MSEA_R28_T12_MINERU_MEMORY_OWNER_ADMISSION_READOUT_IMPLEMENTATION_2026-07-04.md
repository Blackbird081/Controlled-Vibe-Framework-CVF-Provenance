# CVF Agent Work Order - MSEA R28 T12 MinerU Memory Owner Admission Readout Implementation

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T12-MINERU-MEMORY-OWNER-ADMISSION-READOUT-IMPLEMENTATION

rawMemoryReleased: false

dispatchBaseHead: 89c356a4

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T12.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. R28-T11 material commit
`dec53037` accepted memory-owner admission design criteria, and session-sync
commit `89c356a4` permits fresh T12 work-order authoring if the operator
selects that lane. The operator selected T12 completion in this session.

Do-not-misread notes: this packet authorizes only deterministic local
metadata-only source/test implementation and a worker return. It does not
authorize MinerU runtime execution, private/generated content read, Candidate
Group A import, memory/RAG write, provider/live proof, public-sync,
standalone app work, legal/use-case deep dive, extraction accuracy, document
truth, legal quality, current-law correctness, workflow-chain production
readiness, checker/hook edits, session-sync by worker, worker stage, worker
commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the
Source Verification Block, and checker source for worker-created outputs before
writing any file.

Return contract: modify only the named source/test files, create only the
worker return path, run focused pytest, worker-return fast gate, and
pre-implementation autorun, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | accepted R28-T11 closure evidence and current operator T12 selection |
| Intake role | worker implements deterministic local metadata-only memory-owner admission readout helper plus tests |
| Scope classification | bounded source/test implementation; no runtime/provider/public/private-content/memory-write behavior |
| Reviewer role | reviewer/closer validates source/test diff, worker return, gates, no-commit discipline, and memory hold |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; source/test changes remain pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require MinerU runtime execution, private/generated content read, memory/RAG write, provider/live proof, public-sync, standalone app work, legal/use-case deep dive, checker/hook edits, session-sync by worker, AGENTS.md edit, active handoff edit, dependency install, destructive command, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Implement a deterministic metadata-only helper that builds a memory-owner
admission readout from an existing `MineruMemorySafeCandidateContract`. The
helper must verify the T11 admission criteria using metadata-only fields and
must keep direct memory/RAG write unauthorized.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | implement named source/test changes and create worker return only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker artifacts, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator asked to complete MSEA-R28-T12 using accepted T11 closure evidence at material commit `dec53037` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` and `CVF_SESSION/state/entries/nextAllowedMove.json` route next allowed move to T12 work-order authoring if selected | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V36_2026-07-04.md` names the same next allowed move and parked checkpoints | ACCEPT |
| R28-T11 closure | material commit `dec53037` accepted the admission design matrix and preserved memory-write hold | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_2026-07-04.md` | ACCEPT |

## Operator Checkpoint

| Checkpoint | Resolution |
| --- | --- |
| Operator selected T12 | ACCEPT - operator asked the reviewer/closer to complete MSEA-R28-T12 in this session |
| Scope ceiling | ACCEPT - T12 is limited to deterministic metadata-only source/test implementation and worker return |
| Parked lanes | HELD - memory/RAG write, runtime, private/generated content read, provider/live proof, public-sync, checker/hook edit, app, legal/use-case, and production workflow-chain claims remain unauthorized |
| Return route | ACCEPT - worker returns uncommitted artifacts for reviewer/closer closure |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T11 material closure | `docs/reviews/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_WORKER_RETURN_2026-07-04.md` and material commit `dec53037` | ACCEPT |
| R28-T11 companion design matrix | `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md` at accepted closure commit `dec53037` | ACCEPT |
| R28-T11 session-sync routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at session-sync commit `89c356a4` | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `89c356a4` before authoring | ACCEPT |
| Worker execution release | R28-T12 dispatch artifacts and gates must exist before worker begins; this packet supplies that release after commit | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- create `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`;
- add a deterministic metadata-only admission readout dataclass or helper that
  uses existing candidate metadata, receipt id, input digest, quality report
  ref, source pointer, downstream-use status, and claim boundary;
- prove helper output is stable, omits content fields, preserves no memory
  write, and can be derived from `MineruMemorySafeCandidateContract` without
  reading files;
- run focused pytest, worker-return fast gate, pre-implementation autorun, and
  no-commit evidence commands.

Forbidden scope:

- no MinerU command, model/cache mutation, ModelScope, VLM, OCR, parser,
  router, Gradio, Docker, WSL, runtime smoke, or provider/live proof;
- no private source document body read and no generated output content read,
  quotation, copy, import, stage, or commit;
- no Candidate Group A import, checker edit, hook wiring, registry aggregate
  edit, runtime receipt instance, memory-layer write, RAG write, adapter
  implementation, S3, Web, MCP, model-router, package lifecycle,
  action-authority, public-sync, standalone PDF app, legal/use-case deep dive,
  extraction-accuracy claim, document-truth claim, legal advice quality claim,
  current-law correctness claim, production workflow-chain claim, worker stage,
  worker commit, or push;
- no active session state, active handoff, root startup file, AGENTS.md,
  public-sync clone, dependency install, or unrelated documentation edit.

Risk ceiling: R1 deterministic local source/test implementation; no runtime/provider/private-data/public action.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| receipt writer source | worker may modify listed file only | WORKER_MUST_NOT_COMMIT |
| receipt writer focused tests | worker may modify listed file only | WORKER_MUST_NOT_COMMIT |
| worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| checker/hook/source outside listed file/test files | not worker-owned in R28-T12 | forbidden |
| session state, front door, and active handoff | session-sync steward | forbidden to worker |
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
| checker source for worker return and touched source/test gates | READ_BEFORE_WRITING_OUTPUTS |

## Preflight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Capture execution base | `git rev-parse --short HEAD` | record in worker return |
| Confirm worktree status | `git status --short --untracked-files=all` | record exact pending paths |
| Confirm planned worker return path | `Test-Path docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` | no conflicting existing R28-T12 worker artifact |
| Read checker/output source | direct file reads of applicable review, source/test, trace, delta, public-export, worker-return, and dispatch-quality checkers | record exact headings/tokens before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm worktree state | worker return trace |
| 2 | Read worker-output checker source and all Source Verification Block files before editing | Checker Source Read-Ahead Block in worker return |
| 3 | Add deterministic metadata-only memory-owner admission readout helper in receipt writer source | source diff and focused tests |
| 4 | Add tests proving stable helper output, candidate compatibility, unsafe candidate rejection, no content fields, no memory write, and future-authority boundary | focused pytest |
| 5 | Create worker return summarizing implementation, changed files, tests, gates, no-commit status, and next recommendation | worker return |
| 6 | Run focused pytest, worker-return fast gate, and pre-implementation autorun on the worker changed range | command evidence |
| 7 | Leave changes uncommitted and return for reviewer closure | `git status --short --untracked-files=all` and HEAD unchanged |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T12 --title "MinerU Memory Owner Admission Readout Implementation" --date 2026-07-04 --base 89c356a4 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled source verification, deterministic metadata-only admission readout helper scope, worker output manifest, checker-output read-ahead mandate, handoff control, and held memory-write boundary |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `MEMORY_OWNER_ADMISSION_READOUT`; `MEMORY_OWNER_ADMISSION_READY_FOR_REVIEW`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T12_DISPATCH`; `FUTURE_MEMORY_WRITE_WORK_ORDER_REQUIRED` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router/memory behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker/test failures directly by reading the
failing source and matching the required shape. Worker should return to
orchestrator only for a source contradiction, forbidden-scope need, live/
provider/public/private-content requirement, checker/hook/session edit
requirement, dependency install, destructive action, or missing authority that
makes completion impossible.

## Return-To-Orchestrator Conditions

| Condition | Required worker response |
| --- | --- |
| Source/test implementation and worker return completed inside allowed scope with gates passing | return `COMPLETE_PENDING_REVIEW` and leave changes uncommitted |
| Source contradiction blocks admission readout implementation | return `BLOCKED_WITH_REASON` with exact source conflict |
| Any needed action is outside allowed scope | return `BLOCKED_WITH_REASON`; do not expand into runtime, memory, public, checker, session, or private-output work |
| Gate failure inside allowed scope | repair by reading the failing checker and rerun the gate before returning |
| Worker accidentally stages or commits | stop and return `BLOCKED_WITH_REASON`; reviewer/closer owns recovery |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, scaffold output, source verification, checker read-ahead, and no-commit discipline. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; New Implementation Symbols; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created return requires its own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session state releases T12 packet authoring from accepted T11 evidence and preserves the memory-write hold. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| T11 matrix defines admission criteria for receipt, quality, source pointer, downstream-use status, claim boundary, private-output boundary, memory-write authority, and candidate readiness. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md` | lines 40-47 | `Admission Design Matrix` | MSEA-R28-T11 admission design matrix | ACCEPT |
| T11 selected design-only disposition and requires future memory-owner implementation authority. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md` | lines 53-56 | `MEMORY_OWNER_ADMISSION_DESIGN_ONLY`; `FUTURE_MEMORY_OWNER_IMPLEMENTATION_WORK_ORDER_REQUIRED` | MSEA-R28-T11 selected disposition | ACCEPT |
| R27 requires memory-safe candidates to carry receipt, quality, source pointer, downstream-use status, and claim boundary before memory admission. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 74 and 86-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | MSEA-R27 decision ledger | ACCEPT |
| Receipt writer owns the memory-safe candidate contract dataclass and existing payload renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 98 and 358 | `MineruMemorySafeCandidateContract`; `mineru_memory_safe_candidate_contract_payload` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer validates bounded identifiers, source pointers, held downstream release, and memory-safe candidate contracts. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 119-155 and 295-352 | `_validate_safe_id`; `_validate_quality_source_pointer`; `build_mineru_memory_safe_candidate_contract` | MinerU metadata receipt writer validation | ACCEPT |
| Current focused tests cover deterministic memory-safe candidate contracts and unsafe receipt rejection. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 255-333 | `test_memory_safe_candidate_contract_is_deterministic_and_metadata_only`; `test_memory_safe_candidate_contract_fails_closed_for_unsafe_receipts` | MinerU metadata receipt writer tests | ACCEPT |

## New Implementation Symbols

| Symbol | Type | Purpose | Source status |
| --- | --- | --- | --- |
| `MEMORY_OWNER_ADMISSION_READOUT_VERSION` | constant | stable readout version for T12 metadata-only admission payloads | NEW_IMPLEMENTATION_SYMBOL |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T12` | constant | stable T12 memory-write hold token | NEW_IMPLEMENTATION_SYMBOL |
| `MineruMemoryOwnerAdmissionReadout` | dataclass | metadata-only admission readout derived from a memory-safe candidate contract | NEW_IMPLEMENTATION_SYMBOL |
| `build_mineru_memory_owner_admission_readout` | helper function | verify T11 admission criteria from existing candidate contract metadata | NEW_IMPLEMENTATION_SYMBOL |
| `mineru_memory_owner_admission_readout_payload` | helper function | render stable camelCase readout payload without content-bearing fields | NEW_IMPLEMENTATION_SYMBOL |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md`
priorVerificationAnchor: `dec53037`
freshRecomputeRequired: true
recomputeReason: T12 changes source/test behavior, so source facts and focused tests must be recomputed against current HEAD.
unicodePathHandling: Use literal paths and UTF-8-safe command output for local paths; do not normalize or rewrite filenames.
extractedTextAuthority: AUXILIARY_ONLY

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md` |
| priorVerificationAnchor | `dec53037` |
| freshRecomputeRequired | true |
| recomputeReason | T12 changes source/test behavior, so source facts and focused tests must be recomputed against current HEAD |
| unicodePathHandling | Use literal paths and UTF-8-safe command output for local paths; do not normalize or rewrite filenames |
| extractedTextAuthority | AUXILIARY_ONLY |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact path existence | `Test-Path` returned false for T12 baseline, work order, and worker-return paths before authoring | ACCEPT |
| Token search for T12 packet title | `rg -n "MSEA-R28-T12|MEMORY_OWNER_ADMISSION_READOUT|MinerU Memory Owner Admission Readout Implementation" docs CVF_SESSION AGENT_HANDOFF_V36_2026-07-04.md CVF_SESSION_MEMORY.md` was run before authoring; no existing T12 artifact collision was found | ACCEPT |
| Collision decision | No existing T12 dispatch, implementation, or worker-return artifact was present before authoring | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; worker returns uncommitted source/test/review artifacts; reviewer/closer commits accepted material; session-sync steward updates continuity |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=89c356a4; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch changes are paired GC-018 and work order only; worker changes are allowed receipt writer source, focused receipt writer test, and named worker return only |
| traceScope(phase, actor) | dispatcher trace in this work order and baseline; worker trace in worker return; reviewer trace through commit steward and gate evidence; session-sync trace in active handoff/front door/state |
| commitOwner(phase) | dispatch author may commit dispatch; WORKER_MUST_NOT_COMMIT; reviewer/closer commits accepted material; session-sync steward commits protected continuity |
| crossBatchIsolation | MSEA-R28-T12 only; do not mix T12 with runtime/provider/live/private-output/public-sync/checker/hook/session changes or another tranche |
| nextMoveSurfaces | once accepted T12 material commit exists, session-sync steward must update `CVF_SESSION_MEMORY.md`, active state sources, generated active state, bootstrap read model, and active handoff |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return per governed artifact gotcha 30 |
| reviewerOwnedClosurePaths | worker return plus allowed source/test paths if accepted |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under the reviews area | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |

Literal-shape reminders: do not list required headings as backticked heading
strings before the real section; write source-not-found disposition spelling
instead of the exact blocked enum in literalTokensReviewed; avoid broad
dependency-placeholder wording unless the row cites the accepted artifact path
and commit.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | add metadata-only T12 admission readout helper and payload renderer |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | add focused tests for deterministic output, no content fields, no memory write, unsafe candidate rejection, and stable payload |
| `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` | create worker return with command evidence and no-commit statement |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Dispatch base | `git rev-parse --short HEAD` returned `89c356a4` before authoring | ACCEPT |
| Worktree state | `git status --short --untracked-files=all` was empty before dispatch authoring | ACCEPT |
| T12 path collision | planned T12 baseline, work order, and worker return did not exist before authoring | ACCEPT |
| Runtime execution | No MinerU/provider/live/runtime command is authorized by this work order | NOT_APPLICABLE_WITH_REASON |

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| Focused pytest | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` |
| Worker-return fast gate | `python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` |
| Pre-implementation autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` |
| No-commit evidence | `git rev-parse --short HEAD` unchanged from execution base while worker changes are pending |
| Changed files | `git diff --name-status` and `git status --short --untracked-files=all` |

## Verification Commands

```powershell
python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py
python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git status --short --untracked-files=all
```

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker adds deterministic memory-owner admission readout helper and payload renderer in the allowed receipt writer source only | source diff and focused tests |
| AC2 | Readout verifies metadata-only T11 gates: candidate id, receipt id, input digest, quality report ref, source pointer, downstream-use status, claim boundary, output-content-read false, and memory-write authorization false | focused tests |
| AC3 | Readout payload omits content-bearing fields such as extracted text, OCR text, document body, memory record body, vector content, and output file names | focused tests |
| AC4 | Worker creates the named worker return and leaves changes uncommitted | worker return, git status, and HEAD evidence |
| AC5 | Focused pytest, worker-return fast gate, pre-implementation autorun, reviewer steward, and material pre-commit hook pass before closure | command evidence |

## Review Gate

Reviewer/closer must run reviewer-return commit steward on the worker changed
range before staging material closure. Reviewer may repair only allowed-scope
defects in the worker return, source, or focused test files. Any scope
expansion returns to the operator.

## Closure Checklist

| Item | Required resolution |
| --- | --- |
| Source/test diff inside allowed paths | checked before material commit |
| Worker return path present and complete | checked before material commit |
| Focused pytest passed | checked before material commit |
| Worker-return fast gate passed | checked before material commit |
| Pre-implementation autorun passed on worker range | checked before material commit |
| Reviewer-return steward passed | checked before material commit |
| Material pre-commit hook passed | checked before material commit |
| Session-sync completed once accepted material commit exists | session-sync steward task for the accepted material commit |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> R28-T12 memory-owner admission readout implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired GC-018 baseline |
| Disposition | ADAPT: convert accepted T11 admission design evidence into a bounded metadata-only admission readout helper |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session edit, or product-app claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Storage scope | NOT_APPLICABLE_WITH_REASON |
| Reason | T12 does not add storage directories, corpus output, memory store, RAG index, or runtime receipt instance. |
| Claim boundary | deterministic source/test helper only; no storage layout or persistence behavior claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T12 MinerU Memory Owner Admission Readout Implementation dispatch, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, scaffold helper, rg, Test-Path, apply_patch, governance gates |
| Target paths | paired T12 GC-018 baseline and this work order |
| Allowed scope source | operator selected T12 from active next allowed move using accepted T11 closure evidence at material commit `dec53037` |
| Before status evidence | HEAD `89c356a4`; worktree clean before dispatch authoring |
| After status evidence | paired T12 dispatch artifacts pending gates |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only; worker implementation waits until dispatch commit and gates pass |
| Claim boundary | T12 dispatch packet only; no runtime/private-output/memory/public/provider/source implementation claim before worker execution |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t12-dispatch-2026-07-04` |
| Expected manifest | paired T12 GC-018 baseline and this work order |
| Actual changed set | paired T12 GC-018 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T12 dispatch authoring for deterministic metadata-only admission readout implementation |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, or external action is executed or observed. |
| invocationBoundary | local document authoring and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | dispatch packet evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory behavior without fresh source-verified authorization. |

## Claim Boundary

This work order authorizes only deterministic local metadata-only admission
readout source/test implementation and a worker return after dispatch gates
pass. It does not authorize MinerU runtime execution, private/generated content
read, Candidate Group A import, memory/RAG write, provider/live proof,
public-sync, standalone app work, legal/use-case deep dive, extraction
accuracy, document truth, legal quality, current-law correctness,
workflow-chain production readiness, checker/hook edit, session-sync by
worker, worker stage, worker commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T12 work order is private provenance governance material only. No
public-sync export, public repository commit, or public catalog claim is
included.
