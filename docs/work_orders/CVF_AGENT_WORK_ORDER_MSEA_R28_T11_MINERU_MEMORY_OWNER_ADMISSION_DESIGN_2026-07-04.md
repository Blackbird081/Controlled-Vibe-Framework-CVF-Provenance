# CVF Agent Work Order - MSEA R28 T11 MinerU Memory Owner Admission Design

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T11-MINERU-MEMORY-OWNER-ADMISSION-DESIGN

rawMemoryReleased: false

dispatchBaseHead: c870adac

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_WORKER_RETURN_2026-07-04.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T11.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. R28-T10 material commit
`528f8255` accepted future memory-owner review readiness, and session-sync
commit `c870adac` permits a fresh memory-owner work order if the operator
selects that lane. The operator requested continuation, selecting that next
lane.

Do-not-misread notes: this packet authorizes only docs-only admission-design
matrix and worker return creation. It does not authorize MinerU runtime
execution, private/generated content read, Candidate Group A import,
source/test/checker/hook edits, memory/RAG write, provider/live proof,
public-sync, standalone app work, legal/use-case deep dive, extraction
accuracy, document truth, legal quality, current-law correctness,
workflow-chain production-readiness claim, worker stage, worker commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the
Source Verification Block, and checker source for worker-created outputs before
writing any file.

Return contract: create only the companion matrix and worker return, run
worker-return fast gate and pre-implementation autorun, leave changes
uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | accepted R28-T10 closure evidence and current operator continuation |
| Intake role | docs-only worker creates admission-design matrix and worker return |
| Scope classification | bounded documentation design; no runtime/provider/public/private-content/memory-write behavior |
| Reviewer role | reviewer/closer validates matrix, worker return, gates, no-commit discipline, and memory hold |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; docs-only changes remain pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require MinerU runtime execution, private/generated content read, memory/RAG write, provider/live proof, public-sync, standalone app work, legal/use-case deep dive, checker/hook edits, source/test edits, session-sync by worker, AGENTS.md edit, active handoff edit, dependency install, destructive command, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Create a source-verified T11 matrix that designs the memory-owner admission
decision boundary after accepted T10 evidence. The expected decision space is:
design-only admission criteria for future implementation, continue full hold,
or return blocked for missing source authority. Direct memory/RAG write remains
unauthorized in this tranche.

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
| Operator instruction | operator requested continuation after T7-T10 closure, selecting the permitted next lane | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` and `CVF_SESSION/state/entries/nextAllowedMove.json` allow fresh memory-owner work-order authoring if selected | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V36_2026-07-04.md` names the same next allowed move and parked checkpoints | ACCEPT |
| R28-T10 closure | material commit `528f8255` accepted future memory-owner review readiness and preserved memory-write hold | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_2026-07-04.md` | ACCEPT |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T10 material closure | `docs/reviews/CVF_MSEA_R28_T10_MINERU_MEMORY_ROUTE_SELECTION_AFTER_CANDIDATE_CONTRACT_WORKER_RETURN_2026-07-04.md` and material commit `528f8255` | ACCEPT |
| R28-T10 session-sync routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at session-sync commit `c870adac` | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `c870adac` before authoring | ACCEPT |
| Worker execution release | R28-T11 dispatch artifacts and gates must exist before worker begins; this packet supplies that release after commit | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md`;
- create `docs/reviews/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_WORKER_RETURN_2026-07-04.md`;
- define docs-only admission design criteria, source prerequisites, rejection conditions, and future implementation prerequisites for a memory-owner lane;
- preserve direct memory/RAG write hold and require a later fresh implementation packet before any write.

Forbidden scope:

- no MinerU command, model/cache mutation, ModelScope, VLM, OCR, parser,
  router, Gradio, Docker, WSL, or runtime smoke;
- no private source document body read and no generated output content read,
  quotation, copy, import, stage, or commit;
- no source/test/checker/hook edit, registry aggregate edit, runtime receipt
  instance, memory-layer write, RAG write, adapter implementation, S3, Web,
  MCP, model-router, package lifecycle, action-authority, public-sync,
  provider/live proof, standalone PDF app, legal/use-case deep dive,
  extraction-accuracy claim, document-truth claim, legal advice quality claim,
  current-law correctness claim, production workflow-chain claim, worker stage,
  worker commit, or push;
- no active session state, active handoff, root startup file, AGENTS.md,
  public-sync clone, dependency install, or unrelated documentation edit.

Risk ceiling: R1 deterministic local documentation design; no runtime/provider/private-data/public action.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| T11 companion matrix | worker may create listed file only | WORKER_MUST_NOT_COMMIT |
| T11 worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| source/test/checker/hook/session files | not worker-owned in R28-T11 | forbidden |
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
| Confirm planned worker paths | `Test-Path` for matrix and worker return paths | no conflicting existing R28-T11 worker artifact |
| Read checker/output source | direct file reads of applicable review, reference, trace, delta, public-export, worker-return, and dispatch-quality checkers | record exact headings/tokens before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm worktree state | worker return trace |
| 2 | Read worker-output checker source and all Source Verification Block files before editing | Checker Source Read-Ahead Block in worker return |
| 3 | Create companion memory-owner admission design matrix from T10/R27/R24 evidence | matrix diff |
| 4 | Define design-only admission prerequisites, rejection conditions, and future implementation prerequisites | matrix and worker return |
| 5 | Create worker return summarizing changed files, gates, no-commit status, and design disposition | worker return |
| 6 | Run worker-return fast gate and pre-implementation autorun on the worker changed range | command evidence |
| 7 | Leave changes uncommitted and return for reviewer closure | `git status --short --untracked-files=all` and HEAD unchanged |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T11 --title "MinerU Memory Owner Admission Design" --date 2026-07-04 --base c870adac --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled source verification, dependency release, docs-only admission-design scope, worker output manifest, checker-output read-ahead mandate, handoff control, and held memory-write boundary |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `MEMORY_OWNER_ADMISSION_DESIGN_MATRIX`; `MEMORY_OWNER_ADMISSION_DESIGN_ONLY`; `MEMORY_WRITE_STILL_NOT_AUTHORIZED_BY_T11_DISPATCH`; `FUTURE_MEMORY_OWNER_IMPLEMENTATION_WORK_ORDER_REQUIRED` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router/memory behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing source and matching the required shape. Worker should return to
orchestrator only for a source contradiction, forbidden-scope need, live/
provider/public/private-content requirement, checker/hook/session edit
requirement, dependency install, destructive action, or missing authority that
makes completion impossible.

## Return-To-Orchestrator Conditions

| Condition | Required worker response |
| --- | --- |
| Matrix and worker return completed inside allowed scope with gates passing | return `COMPLETE_PENDING_REVIEW` and leave changes uncommitted |
| Source contradiction blocks admission design | return `BLOCKED_WITH_REASON` with exact source conflict |
| Any needed action is outside allowed scope | return `BLOCKED_WITH_REASON`; do not expand into runtime, memory, public, checker, source, or session work |
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
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define admission design content. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created matrix and return require their own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session state allows a fresh memory-owner work order only after operator selection and keeps memory write unauthorized. | VALUE_SET | `CVF_SESSION/state/entries/nextAllowedMove.json` | line 4 | `nextAllowedMove` | active session state entry | ACCEPT |
| T10 closure accepted the route-selection worker return and selected future memory-owner review readiness. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T10MemoryRouteSelectionAfterCandidateContractClosure20260704.json` | lines 5-19 | `MEMORY_SAFE_CANDIDATE_READY_FOR_MEMORY_OWNER_REVIEW`; `FUTURE_MEMORY_OWNER_WORK_ORDER_REQUIRED` | active session state entry | ACCEPT |
| T10 matrix selected future memory-owner review and kept private output unreleased. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T10_MINERU_MEMORY_ROUTE_SELECTION_AFTER_CANDIDATE_CONTRACT_MATRIX_2026-07-04.md` | lines 43-47 | `selectedRouteDisposition`; `privateOutputDisposition` | T10 route-selection matrix | ACCEPT |
| T10 worker return states the same selected route, memory hold, and future authority requirement. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T10_MINERU_MEMORY_ROUTE_SELECTION_AFTER_CANDIDATE_CONTRACT_WORKER_RETURN_2026-07-04.md` | lines 59-63 | `selectedNextRoute`; `futureAuthorityRequired` | T10 worker return | ACCEPT |
| R27 requires memory-safe candidates to have receipt, quality, source pointer, downstream-use status, and claim boundary before memory admission. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 74-75 and 86-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | R27 decision ledger | ACCEPT |
| R24-T4 policy keeps private/generated content out of design and route evidence. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 17, 104, 114-115, and 210-218 | `private-output`; `Claim Boundary`; `Public Export Disposition` | R24-T4 private-output policy | ACCEPT |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned T11 paths absent before authoring | `Test-Path` returned `False` for planned T11 baseline, work order, worker return, and matrix paths. | PASS |
| Token search for T11 before authoring | `rg -n "MSEA-R28-T11|MEMORY_OWNER_ADMISSION|Memory Owner Admission|MEMORY_ADMISSION" docs CVF_SESSION governance EXTENSIONS` returned no matches before authoring. | PASS |
| Freshness disposition | Current source has accepted T10 future memory-owner review evidence; no T11 admission design matrix exists yet. | PASS |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Exact search roots | `docs`, `CVF_SESSION`, `governance`, and `EXTENSIONS` | PASS |
| Exact search command or query | `rg -n "MSEA-R28-T11|MEMORY_OWNER_ADMISSION|Memory Owner Admission|MEMORY_ADMISSION" docs CVF_SESSION governance EXTENSIONS` | PASS |
| Coverage across source/tests/docs/JSON/evidence | The search included governed docs, generated session JSON, governance code, and Extraction Foundation surfaces. | PASS |
| Same-token collision result | No dedicated T11 baseline, work order, worker return, or companion matrix existed before authoring. | PASS |
| Absent-versus-collision disposition | T10 future-authority references are predecessor evidence only; T11 may dispatch as a new docs-only admission-design worker packet. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor requirement | Source evidence | R28-T11 handling |
| --- | --- | --- |
| T10 selects future memory-owner review readiness | T10 matrix lines 43-47 and worker return lines 59-63 | authorize docs-only admission design matrix |
| R27 requires future memory owner authority before write | R27 ledger lines 86-87 | direct memory/RAG write remains unauthorized |
| R27 lists memory-safe candidate prerequisites | R27 ledger lines 74-75 | worker designs admission criteria around receipt, quality, source pointer, downstream-use status, and claim boundary |
| R24-T4 preserves private-output limits | R24-T4 policy rows above | worker must not read or quote private/generated content |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | governed docs-only memory-owner admission design matrix and worker return | internal worker may create documentation evidence under WORKER_MUST_NOT_COMMIT; reviewer must accept before closure | this work order, paired GC-018, source verification, worker return, governance gates | docs-only contract boundary; no memory adapter or runtime action | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP or external adapter owner in R28-T11 | external ingress, authentication, approval, receipt, raw-data, mutation, and public boundaries remain out of scope | no source-verified external adapter authority in R28-T11 | adapter deferred; no CLI/MCP surface implemented or claimed | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | extraction/source evidence -> T10 memory-owner review readiness -> fresh GC-018/work order -> T11 admission design evidence |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired R28-T11 GC-018 and this work order |
| Disposition | ADAPT accepted T10 evidence into a bounded memory-owner admission design dispatch; no external source becomes authority by itself |
| Claim boundary | routing evidence only; no external repository absorption, private/generated content read, MinerU runtime, provider/live proof, public-sync, app, memory write, or production claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Guard owner | `governance/compat/check_foundation_storage_layout.py` |
| Trigger reason | this work order authorizes a worker return under reviews and a bounded companion matrix under reference |
| Stable location decision | companion matrix belongs under `docs/reference/` because it is selected source-verified design evidence |
| Index or front-door decision | N/A with reason: no new stable reference family or generated aggregate is introduced |
| Archive or rotation decision | N/A with reason: no existing durable governance file is split, moved, archived, or rotated in this dispatch |
| Generated aggregate decision | no generated aggregate edit is authorized |
| Claim boundary | storage-layout evidence only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## Worker Output Checker Read-Ahead Mandate

Before writing worker-owned output artifacts, read checker source for their
docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| companion matrix under reference | derive exact reference/trace/delta/public-export/external-intake/corpus/rescan/claim-boundary labels before writing |
| worker return under reviews | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, public-export terms, and no-commit evidence shape before writing |

Literal-shape reminders: when listing required section names, write section
names without heading prefixes. Keep exact source path verification in this
work order and avoid repeating unnecessary extension path literals in worker
review artifacts.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit worker -> reviewer/closer -> session-sync steward |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=c870adac; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | worker may create only the named companion matrix and named worker return |
| traceScope(phase, actor) | worker records executionBaseHead, changed files, worker-return gate, autorun evidence, admission-design disposition, and no-commit statement; reviewer records closure evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit if accepted |
| crossBatchIsolation | do not mix R28-T11 with memory-route write, runtime, provider/live, public-sync, app/use-case/legal, checker/hook edits, source/test edits, or session-sync work |
| nextMoveSurfaces | session-sync steward updates front door, active state, and active handoff only when material closure evidence exists |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return unless reviewer needs a separate closure packet |
| reviewerOwnedClosurePaths | worker return plus named companion matrix |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md` | create source-verified memory-owner admission design matrix and design-only disposition |
| `docs/reviews/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_WORKER_RETURN_2026-07-04.md` | create no-commit evidence packet with changed files, gates, design disposition, and no-memory-write boundary |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_WORKER_RETURN_2026-07-04.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| companion matrix | exact path, selected design-only disposition, source-backed rationale, and no-memory-write boundary |
| worker return | exact path, executionBaseHead, changed files, no-commit evidence, and selected disposition |
| worker-return fast gate | exact command and pass result |
| pre-implementation autorun | exact command and pass result |
| no-commit evidence | `git status --short --untracked-files=all` and HEAD unchanged |
| claim-boundary evidence | explicit no-runtime/no-private-content/no-memory-release/no-public statement |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Admission design matrix | source-verified matrix defines design-only memory-owner admission criteria after T10 evidence |
| Memory hold | direct memory/RAG write remains unauthorized |
| Future authority | any memory write or memory-owner implementation is explicitly deferred to a future fresh GC-018/work order |
| Privacy boundary | no private/generated output content is read, quoted, copied, imported, staged, committed, or encoded |
| Scope | no source/test/checker/hook/session/public/runtime/provider/app/legal/deep-quality claim |
| Worker mode | worker leaves all changes uncommitted |

## Fail Conditions

- source facts conflict with the Source Verification Block;
- design requires reading private source documents or generated output content;
- design requires running MinerU, provider/live proof, memory/RAG, public-sync, app work, source/test/checker/hook edits, or dependency installs;
- matrix claims direct memory write authorization or actual memory admission implementation;
- worker edits session state, active handoff, AGENTS.md, public-sync, checker/hook source, registry aggregates, source/test files, or unrelated docs;
- worker stages, commits, or pushes;
- command evidence is missing, stale, or ambiguous.

## Review Gate

Reviewer must inspect the matrix, worker return, source verification,
worker-return fast gate, pre-implementation autorun, no-commit statement, and
memory-write hold. Reviewer may repair allowed-scope defects but must return to
orchestrator if acceptance requires runtime/private/provider/public/memory/
checker/session/source scope expansion.

## Closure Checklist

| Item | Closure disposition |
| --- | --- |
| Source verification still accurate | checked, or BLOCKED with return action |
| Matrix/return diff inside allowed scope | checked, or BLOCKED with return action |
| Worker-return fast gate passes | checked, or BLOCKED with command evidence |
| Pre-implementation autorun passes | checked, or BLOCKED with command evidence |
| No forbidden runtime/private/provider/public/memory/checker/session/source action | checked, or BLOCKED with return action |
| Memory-write hold preserved | checked, or BLOCKED with return action |
| Next allowed move stated | checked after review decision |
| Session sync | reviewer/steward only when material closure exists |

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base c870adac --head HEAD
git status --short --untracked-files=all
```

If the changed range differs from `c870adac..HEAD` during worker execution,
capture the worker's executionBaseHead and run gates over the real worker
changed range.

## Operator Checkpoint

operator.checkpoint.waiver: Operator requested continuation after T7-T10
closure. This dispatch interprets that as selecting the only concrete permitted
next lane: memory-owner admission design. Any memory write remains held for a
future implementation work order.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T11 MinerU Memory Owner Admission Design, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, scaffold helper, apply_patch, governance gates |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_2026-07-04.md` |
| Allowed scope source | active session state nextAllowedMove and operator request |
| Before status evidence | clean worktree evidence: `git status --short` returned no output before authoring |
| After status evidence | dispatcher pre-dispatch gates to be recorded before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator requested continuation; this dispatch authorizes only T11 docs-only worker packet |
| Claim boundary | dispatch authoring only; no worker execution, runtime, memory/RAG, public-sync, provider/live, private/generated content read, checker/hook/source edit, or production claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t11-dispatch-2026-07-04` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_2026-07-04.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_2026-07-04.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename performed |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T11 docs-only memory-owner admission design work order |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata/helper and decision evidence are cited, but this work order creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this work order runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local source verification, docs-only admission-design matrix, worker return, and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | docs-only admission-design worker dispatch and bounded evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior, checker/hook/source edit, or memory write without fresh source-verified authorization. |

## Claim Boundary

This work order authorizes a no-commit worker to create a source-verified
docs-only memory-owner admission design matrix and worker return after accepted
T10 route-selection evidence. It does not authorize MinerU runtime execution,
private/generated content read, runtime receipt creation, source/test/checker/
hook edits, memory/RAG release, adapter work, provider/live proof, public-sync,
app work, legal/use-case deep dive, extraction accuracy, document truth, legal
quality, current-law correctness, workflow-chain production claim, worker
commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T11 is private provenance implementation-dispatch work and does not
change the public-sync repository or public catalog.
