# CVF Agent Work Order - MSEA-R24-T2 MinerU HuggingFace Cache Completion Recovery

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-03

Batch ID: MSEA-R24-T2

Dispatch base head: 2356c27c

Commit mode: WORKER_MUST_NOT_COMMIT

Worker return path: `docs/reviews/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_WORKER_RETURN_2026-07-03.md`

Companion reference path: `docs/reference/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_READINESS_MATRIX_2026-07-03.md`

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R24-T2.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-03.

Do-not-misread notes: this packet authorizes exactly one HuggingFace pipeline
cache-completion command using the existing ignored R22 venv. It does not
authorize parser/OCR/VLM/API/router/Gradio/Docker/WSL execution, local service
startup beyond the command process itself, document body read, extraction
output, public-sync, provider/live proof, runtime smoke, or production claim.

Required first actions: read this work order, paired baseline, T1 decision
matrix, R22 readiness matrix, checker source read-ahead files, and cited MinerU
source lines before creating worker outputs or running the command.

Return contract: create the worker return artifact and companion readiness
matrix, run required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Run one bounded HuggingFace MinerU pipeline cache-completion command and record
whether it creates the expected ignored config/cache receipt. If it fails,
classify the failure once and do not rerun.

## Scope

| Field | Value |
|---|---|
| Allowed scope | one HuggingFace pipeline cache-completion command plus receipt/diagnostic artifacts |
| Forbidden scope | any runtime smoke, parser/OCR/VLM/API/router/Gradio/Docker/WSL execution, public-sync, provider/live proof, production claim |
| Target | local ignored `.cvf/runtime` receipt and governed worker return/reference outputs |

## Authority Chain

| Authority | Path or commit | Disposition |
|---|---|---|
| Operator instruction | current session request to complete T1-T4 through governed dependency gates | ACCEPT |
| R24 roadmap | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | ACCEPT |
| T1 decision | `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md` | ACCEPT |
| R22 readiness | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | ACCEPT |
| MinerU source mirror | `.private_reference/source_mirrors/opendatalab__MinerU/` | ACCEPT |

## Agent Roles

| Role | Responsibility | Commit authority |
|---|---|---|
| Dispatcher | author baseline and work order | may commit dispatch after gates |
| Worker | run exactly one allowed command and create two uncommitted outputs | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | repair, review, commit accepted worker outputs, and sync session | owns closure commit |

## Required First Reads

1. `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_2026-07-03.md`
2. `docs/baselines/CVF_GC018_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_2026-07-03.md`
3. `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md`
4. `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md`
5. `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py`
6. `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md`
7. `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py`
8. Checker files listed in the Checker Source Read-Ahead Block.

## Pre-Flight Checks

| Check | Required evidence |
|---|---|
| Capture base | `git rev-parse --short HEAD` recorded as executionBaseHead |
| Worktree status | `git status --short --untracked-files=all` before command |
| Output absence | planned worker return and companion reference are absent before creation |
| Command presence | `.cvf/runtime/msea-r22-mineru-venv/Scripts/mineru-models-download.exe` exists |
| Config target | `.cvf/runtime/msea-r24-huggingface-mineru.json` is the process-local config receipt path |

## Write Ownership

| Path class | Worker permission |
|---|---|
| Worker return path | create only, leave uncommitted |
| Companion reference path | create only, leave uncommitted |
| `.cvf/runtime/` log/config/cache receipts | may write ignored local runtime evidence |
| Repository source, checkers, session state, public-sync, package files | forbidden |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Capture `executionBaseHead` and initial `git status --short --untracked-files=all`. | worker return |
| 2 | Confirm planned worker outputs are absent. | worker return |
| 3 | Confirm venv-local `mineru-models-download.exe` exists. | command evidence |
| 4 | Set process-local `MINERU_TOOLS_CONFIG_JSON=.cvf/runtime/msea-r24-huggingface-mineru.json`. | command evidence |
| 5 | Run exactly one command: `.\\.cvf\\runtime\\msea-r22-mineru-venv\\Scripts\\mineru-models-download.exe --source huggingface --model_type pipeline`. | log file and worker return |
| 6 | Check for `.cvf/runtime/msea-r24-huggingface-mineru.json` and cache metadata. | readiness matrix |
| 7 | Select exactly one result token. | worker return and readiness matrix |
| 8 | Run worker-return fast gate and pre-implementation autorun. | gate evidence |

## Worker Autonomy / No-Question Rule

The worker must proceed without asking the operator for preferences when the
answer is source-verifiable from this packet, the paired baseline, cited MinerU
source, current worktree state, or checker output. If the single allowed command
fails, times out, or produces no receipt, the worker records the diagnostic and
returns `HOLD_PENDING_CACHE_NETWORK_DIAGNOSTIC` or another allowed token rather
than rerunning or expanding scope.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | operator request is to continue the dependency-gated T1-T4 sequence, with T2 limited to the cache-completion recovery lane released by T1 |
| scope classification | bounded allowed scope: one command plus two governed worker outputs and ignored local receipt/log evidence |
| risk sensitivity | secret-safe local runtime evidence only; no public-sync, provider/live proof, legal-quality claim, production readiness, or document body processing |
| selected role route | role route mode: MULTI_AGENT_SINGLE_ROLE |
| role separation basis | dispatcher authors packet; worker executes and returns uncommitted outputs; reviewer/closer owns material commit and session-sync |
| escalation condition | stop, hold, or return to orchestrator if the command path is missing, a second command would be needed, HuggingFace requires unavailable credentials, or gates require out-of-scope repair |
| commitMode | WORKER_MUST_NOT_COMMIT |

## Allowed Command

The only authorized cache command is:

```powershell
$env:MINERU_TOOLS_CONFIG_JSON = ".cvf/runtime/msea-r24-huggingface-mineru.json"
.\.cvf\runtime\msea-r22-mineru-venv\Scripts\mineru-models-download.exe --source huggingface --model_type pipeline
```

The worker must capture stdout/stderr or a summarized log in ignored runtime
space, preferably `.cvf/runtime/msea-r24-huggingface-cache.log`. If the command
hangs or fails, classify the failure and do not rerun.

## Allowed Result Tokens

Worker must select exactly one:

| Token | Meaning |
|---|---|
| CACHE_CONFIG_RECEIPT_READY | Config/cache receipt exists and is sufficient to author T3 runtime-smoke work order. |
| HOLD_PENDING_CACHE_NETWORK_DIAGNOSTIC | HuggingFace command failed, timed out, or produced no config/cache receipt; diagnostic recorded. |
| HOLD_PENDING_LOCAL_MODEL_PATH | Command evidence shows a local-model-path prep route is needed instead. |
| HOLD_ALL_RUNTIME_LANES | No T3 runtime lane may open. |

## Forbidden Scope

Worker must not run any second cache command, ModelScope retry, `auto` probe,
local model parsing, parser/OCR/VLM/API/router/Gradio/Docker/WSL execution,
local service startup beyond the one command process, source document
copy/import, document body read, extraction output, provider/live proof,
public-sync, RAG/S3, schema/writer/adapter/checker implementation, package
reinstall, Web/MCP/model-router/action-authority work, benchmark,
document-truth, extraction-accuracy, legal advice quality, current-law
correctness, runtime smoke, workflow-chain completion, production readiness,
stage, commit, or push.

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| T1 selected HuggingFace | `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md` | `86097efe` | SATISFIED |
| R22 venv command exists | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | `7b105700` | SATISFIED |
| T2 fresh dispatch | paired GC-018 baseline | current batch | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` reviewed as local helper surface |
| generatedProfile | manual work-order authoring after helper/source read-ahead |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Manual work order authored from current T1/R22/MinerU evidence and repaired against pre-dispatch gates. |
| checkerReadAheadConfirmation | Checker Source Read-Ahead Block lists dispatch, worker-return, and absorption gates used for this packet. |
| docOnlyNewFields | none |
| claimBoundary | Scaffold provenance describes dispatch packet shape only; no cache command or runtime behavior is claimed. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: this dispatch batch may update active
session wording only to prevent the dispatch lifecycle checker from confusing
the accepted T1 closure row with the still-open T2 dispatch lane. The change is
literal-text clarification only and does not alter the T1 closure decision, T2
runtime authority, checker behavior, or generated-state schema.

Protected paths:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/entries/mseaR24T1MineruModelSourceFallbackDecisionClosure20260703.json`
- `CVF_SESSION_MEMORY.md`

Operator authorization: operator asked to continue the dependency-gated T1-T4
sequence; this protected-path edit is required only to keep T2 dispatch
machine-checkable after T1 closure.

Rollback boundary: if rejected, revert only this T2 dispatch packet and the
literal session wording clarification. Do not revert material T1 acceptance
commit `86097efe` or earlier session-sync commits.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; Dependency Release Evidence; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; External Knowledge Intake Routing row labels; External Absorption Core row labels; ledger_terminal=; Corpus verdict bullet; Allowed Result Tokens; Allowed Command; Public Export Disposition |
| gateRunPurpose | Confirmation evidence after checker source read-ahead; gates confirm this work order shape. |
| claimBoundary | Read-ahead covers this dispatch packet only; worker output artifacts require their own checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1 selected HuggingFace cache recovery. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md` | selectedRouteToken line | `SELECT_HUGGINGFACE_CACHE_RECOVERY` | T1 decision matrix | ACCEPT |
| MinerU exposes the download console script. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | line 133 | `mineru-models-download` | project scripts | ACCEPT |
| MinerU download CLI supports remote source option. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 94-103 | `--source` | MinerU model download CLI | ACCEPT |
| MinerU download CLI supports pipeline model type. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 104-117 | `--model_type` | MinerU model download CLI | ACCEPT |
| MinerU completed downloads write model path and source into config. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 44 | `mineru.json` | MinerU model-source docs | ACCEPT |
| MinerU config path can be redirected by `MINERU_TOOLS_CONFIG_JSON`. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 23-25 | `get_tools_config_file_path` | config path helper | ACCEPT |
| R22 ignored venv exists and contains the download command. | VALUE_SET | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | lines 57-58 | `.cvf/runtime/msea-r22-mineru-venv` | R22 readiness matrix | ACCEPT |

## Required Worker Outputs

| Path | Required status |
|---|---|
| `docs/reviews/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_WORKER_RETURN_2026-07-03.md` | create, uncommitted |
| `docs/reference/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_READINESS_MATRIX_2026-07-03.md` | create, uncommitted |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | Optional; prefer repairing evidence in the worker return per gotcha 30. |
| reviewerOwnedClosurePaths | worker return and companion readiness matrix |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_WORKER_RETURN_2026-07-03.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned MinerU source mirror plus accepted T1 decision -> T2 bounded HuggingFace cache-completion recovery |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this work order and paired baseline |
| Disposition | ADAPT: dispatch one bounded cache-completion command |
| Claim boundary | dispatch only; no parser runtime, public-sync, or production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Enumeration command | `filesystem-backed direct reads of cited T1/R22/MinerU source files` |
| Manifest artifact or inline manifest | inline table: Source Verification Block |
| Processing ledger artifact or inline ledger | inline table: Execution Plan and Allowed Result Tokens |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md`; `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md`; `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Unresolved items | command result, config/cache receipt, T3 release |
| Completion claim boundary | dispatch only; no runtime smoke or parser execution |

ledger_terminal=READ for cited source evidence; ledger_terminal=ADAPTED for T2 dispatch; ledger_terminal=DEFERRED for worker result and T3/T4; ledger_terminal=REJECTED for direct runtime smoke in T2.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| T1 decision matrix | HuggingFace selected | RUNTIME_CANDIDATE | T2 worker | run one bounded command | no parser |
| MinerU CLI source | source and pipeline options exist | RUNTIME_CANDIDATE | T2 worker | exact command only | no second command |
| MinerU config helper | config override exists | DOCTRINE_ADAPTED | T2 receipt | use ignored config path | no repo config |
| R22 venv | command exists | PACKAGE_CANDIDATE | T2 worker | reuse only | no reinstall |
| Runtime smoke | T3 dependency | REJECT_DIRECT_IMPORT | claim boundary | defer | no smoke |
| Workflow-chain policy | T4 dependency | CHECKER_CANDIDATE | future T4 | defer | no checker implementation |
| Public export | not authorized | NO_PACKAGE_OR_RUNTIME_VALUE | private provenance only | none | no public-sync |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| T1 route | `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | releases T2 authoring | dispatch |
| MinerU CLI | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | ENRICH_EXISTING | exact HuggingFace pipeline command | adapt |
| R22 venv | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | reuse only | cite |
| Runtime smoke | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | REJECT_DIRECT_IMPORT | T3 only after receipt | defer |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T2 requires T1 route release | Dependency Release Evidence | selected route token | pre-dispatch gate | PASS |
| T2 may run one bounded command | Allowed Command | command evidence | worker return | PASS |
| T3 remains gated | Forbidden Scope | runtimeSmokeGateDisposition | reviewer check | PASS |
| T4 remains gated | Forbidden Scope | workflow-chain disposition | reviewer check | PASS |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher creates packet; worker returns uncommitted outputs; reviewer/closer owns material commit and session-sync |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=2356c27c; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | baseline and work order only for dispatch; worker may create only two planned outputs and ignored runtime receipts |
| traceScope(phase, actor) | dispatcher trace in this packet; worker trace in return/matrix; reviewer trace in closure/session-sync |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | MSEA-R24-T2 only; T3/T4 require separate release evidence and work orders |
| nextMoveSurfaces | reviewer/closer updates session surfaces only after accepting worker return |

## Corpus Completeness And Report Integrity

- Corpus task class: T2 work-order dispatch for bounded cache-completion recovery.
- Corpus root: T1 decision matrix, R22 readiness matrix, and pinned MinerU CLI/config docs.
- Snapshot time: 2026-07-03 dispatch authoring.
- Enumeration command: filesystem-backed direct reads of cited source files.
- Manifest artifact or inline manifest: Source Verification Block in this work order.
- Manifest hash: N/A with reason: bounded dispatch source set, not a new corpus snapshot.
- Processing ledger artifact or inline ledger: Execution Plan and Allowed Result Tokens.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=T1/R22/MinerU source evidence; ledger_terminal=READ/ADAPTED/DEFERRED/REJECTED; exclusions=parser runtime, document processing, public-sync, provider/live proof, production claims; unresolved=0 for dispatch authoring.
- Unresolved files: none for dispatch authoring.
- Declared exclusions: runtime smoke, parser execution, document body read, extraction outputs, public-sync, provider/live proof, production readiness.
- Unreadable or unsupported files: none identified.
- Aggregation check: PASS - accepted owner surfaces are cited.
- Drift check: PASS - T1 selected HuggingFace route.
- Output traceability: worker return and readiness matrix are named.
- Adversarial verification: direct runtime smoke and workflow-chain completion are rejected for T2.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git status --short --untracked-files=all
```

## Evidence Requirements

| Requirement | Evidence |
|---|---|
| Single command proof | command line, exit code or timeout class, and log path |
| Receipt proof | existence and safe summary of `.cvf/runtime/msea-r24-huggingface-mineru.json` if created |
| Failure proof | diagnostic class, stage, retryability, and no-rerun statement |
| Boundary proof | final `git status --short --untracked-files=all` and changed path list |
| Gate proof | worker-return fast gate and pre-implementation autorun output summary |

## Acceptance Criteria

| Criterion | Required disposition |
|---|---|
| Exactly one allowed command attempted | PASS or BLOCKED_WITH_REASON |
| Worker output paths created | PASS or BLOCKED_WITH_REASON |
| Result token selected from allowed set | PASS |
| No forbidden runtime/document/public/provider/package work | PASS |
| Gates run with real executionBaseHead | PASS or diagnostic if blocked |

## Review Gate

Reviewer must confirm worker outputs satisfy the Worker Return Packet Shape
Contract, command count is exactly one, ignored runtime receipt/log evidence is
secret-safe, and no T3/T4 release is claimed unless the selected T2 token and
receipt evidence support it.

## Closure Checklist

| Item | Required resolution |
|---|---|
| Worker return reviewed | checked, N/A with reason, or BLOCKED |
| Companion readiness matrix reviewed | checked, N/A with reason, or BLOCKED |
| Gate evidence verified | checked, N/A with reason, or BLOCKED |
| T3 release decision recorded | checked, N/A with reason, or BLOCKED |
| Session sync updated after accepted material commit | checked, N/A with reason, or BLOCKED |

## Return-To-Orchestrator Conditions

Return to orchestrator if the allowed command path is missing, a second command
would be required, source facts contradict this packet, HuggingFace access
requires credentials not already available, or gates reveal an out-of-scope
repair need.

## Operator Checkpoint

No operator checkpoint is required before the single T2 command because the
operator authorized the full dependency-gated T1-T4 sequence. A new operator
checkpoint is required before any command outside the Allowed Command section or
before T3/T4 execution without fresh release evidence.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R24-T2 HuggingFace cache-completion recovery dispatch, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, source reads, `apply_patch`, governance gates |
| Target paths | this work order and paired baseline |
| Allowed scope source | T1 material commit `86097efe`; session-sync commit `dc1c8392`; handoff marker `c1b8079b`; dispatch wording clarification `eb4ecd4f`; handoff marker `2356c27c` |
| Before status evidence | clean worktree before dispatch authoring |
| After status evidence | baseline and work order pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no cache command executed by dispatch; no runtime smoke |
| Agent type | dispatcher |
| Invocation ID | `msea-r24-t2-huggingface-cache-work-order-dispatch-2026-07-03` |
| Expected manifest | this work order and paired baseline |
| Actual changed set | this work order and paired baseline |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R24-T2 work order for one bounded HuggingFace cache command |
| claimDisposition | CLAIM_REJECTED: dispatch does not execute the command or claim runtime readiness |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker must create receipt or diagnostic |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no command action in dispatch |
| invocationBoundary | local governed dispatch authoring only |
| interceptionBoundary | no provider, parser, Web, MCP, adapter, or production route interception claim |
| claimLanguage | work-order dispatch and future worker receipt only |
| forbiddenExpansion | no parser/OCR/VLM/API/router/Gradio/Docker/WSL execution, document processing, provider/live proof, public-sync, runtime smoke, workflow-chain completion, or production-readiness claim |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationStorageImpact | N/A with reason: this work order does not create, split, relocate, or refactor durable governance foundation files. |
| stablePathDecision | N/A with reason: only dated dispatch/worker artifacts are authorized. |
| indexUpdateDecision | N/A with reason: no stable foundation family or README index is changed. |
| claimBoundary | This block is included because the artifact cites `docs/reference/` owner surfaces; it does not authorize foundation storage changes. |

## Claim Boundary

This work order authorizes exactly one HuggingFace pipeline cache-completion
command under worker control and no other runtime action. It does not authorize
parser smoke, document processing, provider/live proof, public-sync,
production readiness, stage, commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet; no public-sync export is authorized.
