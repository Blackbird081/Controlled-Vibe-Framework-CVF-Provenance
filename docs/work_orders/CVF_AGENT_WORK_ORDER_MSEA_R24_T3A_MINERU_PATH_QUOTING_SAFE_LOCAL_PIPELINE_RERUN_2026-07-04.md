# CVF Agent Work Order - MSEA-R24-T3A MinerU Path Quoting Safe Local Pipeline Rerun

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-04

Batch ID: MSEA-R24-T3A

Dispatch base head: 5a43cebe

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R24-T3A.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04.

Do-not-misread notes: this packet authorizes at most one local MinerU CLI
rerun using a PowerShell call-operator invocation pattern that preserves
Windows paths with spaces. It forbids model download, a second rerun, manual
document body inspection, content quotation in committed artifacts, external
export, provider API proof, extraction-accuracy/legal-quality/current-law
claims, workflow-chain completion, release-readiness claims, stage, commit, or
push.

Required first actions: read this work order, paired baseline, accepted T3
worker return and readiness matrix, accepted T2A readiness matrix, R17 private
test ledger, MinerU CLI/config source, checker source read-ahead files, and
literal-format gotchas before creating worker outputs or running the command.

Return contract: create the worker return artifact and companion readiness
matrix, run required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Worker return path: `docs/reviews/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_WORKER_RETURN_2026-07-04.md`

Companion reference path: `docs/reference/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_READINESS_MATRIX_2026-07-04.md`

Completion review path: `docs/reviews/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_COMPLETION_2026-07-04.md`

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Purpose

Run one bounded path-quoting-safe local MinerU CLI pipeline rerun, if preflight
confirms the accepted config receipt, local venv command, and one Candidate
Group A input are present. The worker must record either a smoke receipt or a
diagnostic hold without rerunning or expanding scope.

## Scope

| Field | Value |
|---|---|
| Allowed scope | one local MinerU CLI rerun using a direct PowerShell call operator plus ignored runtime output/log/receipt evidence and two governed worker outputs |
| Forbidden scope | second rerun, model download/cache mutation, ModelScope, VLM/hybrid/http-client/router/Gradio/Docker/WSL, service outside the single CLI process, manual document body read, content quote, public-sync, provider/live proof, RAG/S3, schema/writer/adapter/checker implementation, production claim |
| Target | ignored `.cvf/runtime` T3A smoke output/log/receipt evidence and governed worker return/reference outputs |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | Operator asked Codex to continue the T1-T4 MinerU chain after T3 recorded a quoting diagnostic and held T4. |
| scope classification | Bounded single-tranche work order: one local rerun command, two governed worker outputs, and ignored `.cvf/runtime` receipts only. |
| risk sensitivity | Sensitive private Candidate Group A legal-policy input, local runtime process, provider/live/public-sync and production-readiness risks all remain constrained by this packet. |
| selected role route | routeMode=`MULTI_AGENT_SINGLE_ROLE`; dispatcher creates packet, worker executes no-commit rerun, reviewer/closer owns material commit and session-sync. |
| role separation basis | Worker must not commit; reviewer/closer conversion preserves separate execution and acceptance accountability. |
| escalation condition | Hold or stop on missing CLI/config/input, hash or size mismatch, command timeout/failure, teardown uncertainty, second-command need, or checker failure. |
| routingBoundary | MinerU source mirror, accepted T2A config/cache receipt, accepted T3 diagnostic closure, and R17 private-test ledger only. |

## Authority Chain

| Authority | Path or commit | Disposition |
|---|---|---|
| Operator instruction | current session request to continue after T3 diagnostic closure | ACCEPT |
| T3 accepted diagnostic closure | `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md` at `4fe1b044` | ACCEPT |
| T3 readiness matrix | `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md` at `4fe1b044` | ACCEPT |
| T3 session sync | `CVF_SESSION/ACTIVE_SESSION_STATE.json` at `5a43cebe` | ACCEPT |
| T2A readiness matrix | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | ACCEPT |
| Candidate Group A private-test boundary | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | ACCEPT |
| MinerU source mirror | `.private_reference/source_mirrors/opendatalab__MinerU/` | ACCEPT |

## Agent Roles

| Role | Responsibility | Commit authority |
|---|---|---|
| Dispatcher | author baseline and work order | may commit dispatch after gates |
| Worker | run at most one allowed local rerun and create two uncommitted outputs | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | repair, review, commit accepted worker outputs, and sync session | owns closure commit |

## Required First Reads

1. `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_2026-07-04.md`
2. `docs/baselines/CVF_GC018_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_2026-07-04.md`
3. `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md`
4. `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md`
5. `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md`
6. `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md`
7. `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md`
8. `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/cli_tools.md`
9. `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/client.py`
10. `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/config_reader.py`
11. `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py`
12. Checker files listed in the Checker Source Read-Ahead Block.

## Pre-Flight Checks

| Check | Required evidence |
|---|---|
| Capture base | `git rev-parse --short HEAD` recorded as executionBaseHead |
| Worktree status | `git status --short --untracked-files=all` before command |
| Output absence | planned worker return and companion reference are absent before creation |
| MinerU CLI presence | `.cvf/runtime/msea-r22-mineru-venv/Scripts/mineru.exe` exists |
| Accepted config presence | `.cvf/runtime/msea-r24-t2a-huggingface-mineru.json` exists |
| Config safe metadata | config includes `models-dir.pipeline` and that local path exists |
| Candidate input presence | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\148_2025_QH15_675262.docx` exists and hash/size match R17 evidence |
| Output parent | `.cvf/runtime` exists before command |

If any preflight check fails, do not run the smoke command; select
`HOLD_PENDING_RUNTIME_ENV_FIX` or `HOLD_ALL_RUNTIME_LANES` with diagnostic.

## Write Ownership

| Path class | Worker permission |
|---|---|
| Worker return path | create only, leave uncommitted |
| Companion reference path | create only, leave uncommitted |
| `.cvf/runtime/msea-r24-t3a-*` log/output/receipt evidence | may write ignored local runtime evidence |
| Candidate Group A original DOCX files | may be read only by the single MinerU command; do not copy/import/stage/commit |
| Repository source, checkers, session state, public-sync, package files | forbidden |

## Candidate Group A Privacy Boundary

| Field | Value |
|---|---|
| Input chosen for rerun | `148_2025_QH15_675262.docx` because it is the smaller authorized Candidate Group A file in R17 metadata and was the T3 input |
| Source location | operator-local CVF-Workspace sibling path named in Pre-Flight Checks |
| Worker artifact rule | committed artifacts may include only metadata, hash/size, command status, output file names/counts, and excerpt-minimal or redacted evidence if unavoidable |
| Forbidden evidence | no source document copy/import, no original file commit, no full extraction output commit, no sensitive legal/personal detail quotation, no public-sync |

## Allowed Command

The only authorized smoke command is one PowerShell script block that invokes
`mineru.exe` exactly once by direct call operator. Do not use `Start-Process`
or a single shell string that can split paths with spaces.

```powershell
$env:MINERU_TOOLS_CONFIG_JSON = "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\.cvf\runtime\msea-r24-t2a-huggingface-mineru.json"
$env:MINERU_MODEL_SOURCE = "local"
$env:MINERU_DEVICE_MODE = "cpu"
$env:MINERU_API_OUTPUT_ROOT = "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\.cvf\runtime\msea-r24-t3a-api-output"
$env:MINERU_LOCAL_API_STARTUP_TIMEOUT_SECONDS = "300"
$env:MINERU_TASK_RESULT_TIMEOUT_SECONDS = "900"
$mineru = ".\.cvf\runtime\msea-r22-mineru-venv\Scripts\mineru.exe"
$inputPath = "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\148_2025_QH15_675262.docx"
$outputPath = ".\.cvf\runtime\msea-r24-t3a-output"
$stdoutLog = ".\.cvf\runtime\msea-r24-t3a-runtime-smoke.log"
$stderrLog = ".\.cvf\runtime\msea-r24-t3a-runtime-smoke.err.log"
& $mineru -p $inputPath -o $outputPath -b pipeline -m auto -f false -t false > $stdoutLog 2> $stderrLog
$exitCode = $LASTEXITCODE
```

The worker may create `.cvf/runtime/msea-r24-t3a-runtime-smoke-receipt.json`
after this single invocation to record exit code, duration, output directory
metadata, log paths, and process teardown. If the CLI launches a temporary
local `mineru-api`, that process is authorized only as part of this single
command and must be verified stopped or diagnosed after the command exits or
times out.

## Allowed Result Tokens

Worker must select exactly one:

| Token | Meaning |
|---|---|
| SMOKE_PASS_BOUNDED | One rerun exited 0, expected output directory exists, and only metadata-safe output receipt is recorded. |
| SMOKE_FAIL_DIAGNOSTIC_RECORDED | One rerun ran and failed or timed out; diagnostic is recorded and no rerun happened. |
| HOLD_PENDING_RUNTIME_ENV_FIX | Preflight or command evidence shows a missing path, missing dependency, lingering process, or local environment issue that needs a later fix. |
| HOLD_ALL_RUNTIME_LANES | No T4 workflow-chain lane may open. |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Capture `executionBaseHead` and initial `git status --short --untracked-files=all`. | worker return |
| 2 | Create short worker-return skeleton using helper before long prose. | worker return gate evidence |
| 3 | Confirm planned worker outputs are absent. | worker return |
| 4 | Confirm MinerU CLI, T2A config, configured pipeline path, Candidate Group A input, and output parent exist. | worker return and matrix |
| 5 | Run exactly one allowed direct-call command, or hold before command if preflight fails. | log file and worker return |
| 6 | Capture exit code, duration, log path, output directory file-name inventory, and process teardown evidence. | readiness matrix |
| 7 | Select exactly one allowed result token and state whether T4 remains held. | worker return and readiness matrix |
| 8 | Run worker-return fast gate and pre-implementation autorun. | gate evidence |

## Worker Autonomy / No-Question Rule

The worker must proceed without asking the operator for preferences when the
answer is source-verifiable from this packet, the paired baseline, cited MinerU
source, current worktree state, or checker output. If the single allowed rerun
fails, times out, or cannot start because of preflight, the worker records the
diagnostic and returns an allowed hold token rather than rerunning, changing
input, downloading models, or expanding scope.

## Forbidden Scope

Worker must not run a second rerun command, rerun after failure, run model
download/cache mutation, use ModelScope, use VLM/hybrid/http-client/router/
Gradio/Docker/WSL, start a service outside the single CLI process, manually
open or quote document body content, copy/import Candidate Group A files into
this repository, commit extraction outputs, public-sync, call a provider/live
API, perform RAG/S3/schema/writer/adapter/checker/package/Web/MCP/model-router/
action-authority work, benchmark, claim document truth, claim extraction
accuracy, claim legal advice quality, claim current-law correctness, claim
workflow-chain completion, claim production readiness, stage, commit, or push.

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| T3 accepted diagnostic closure | `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md` selected `SMOKE_FAIL_DIAGNOSTIC_RECORDED` | `4fe1b044` | SATISFIED |
| T3 readiness matrix | `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md` recorded `LOCAL_INVOCATION_ARGUMENT_QUOTING` and no T4 release | `4fe1b044` | SATISFIED |
| T3 session sync | `CVF_SESSION/ACTIVE_SESSION_STATE.json` routes next move to T3A authoring | `5a43cebe` | SATISFIED |
| T2A readiness matrix | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` records config/cache receipt ready | `b53786d9` | SATISFIED |
| Candidate Group A private-test boundary | R17 intake ledger | `eb127b7f` | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | N/A with reason: resolver returned no defects for this dispatcher pre-dispatch query |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R24-T3A --title "MinerU Path Quoting Safe Local Pipeline Rerun" --date 2026-07-04 --base 5a43cebe --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R24-T3 diagnostic closure at 4fe1b044 selected SMOKE_FAIL_DIAGNOSTIC_RECORDED" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled dispatch prompt envelope, authority chain, allowed command, source verification, dependency release evidence, worker packet-shape contract, and privacy boundary. |
| checkerReadAheadConfirmation | Checker Source Read-Ahead Block lists dispatch, worker-return, and absorption gates used for this packet. |
| docOnlyNewFields | `pathQuotingSafeInvocationDisposition`; `t3aRuntimeSmokeReceiptDisposition`; `t3aCandidateGroupASmokeInput` |
| claimBoundary | Scaffold provenance describes dispatch packet shape only; no command has been run by dispatch. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; Dependency Release Evidence; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; External Knowledge Intake Routing row labels; External Absorption Core row labels; ledger_terminal=; Corpus verdict bullet; Allowed Result Tokens; Allowed Command; Public Export Disposition |
| gateRunPurpose | Confirmation evidence after checker source read-ahead; gates confirm this work order shape. |
| claimBoundary | Read-ahead covers this dispatch packet; worker output artifacts require their own checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T3 selected diagnostic failure rather than smoke pass. | VALUE_SET | `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md` | Decision / Disposition | `SMOKE_FAIL_DIAGNOSTIC_RECORDED` | T3 worker return | ACCEPT |
| T3 failure class was local invocation argument quoting before document processing. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md` | Diagnostic Classification | `LOCAL_INVOCATION_ARGUMENT_QUOTING` | T3 readiness matrix | ACCEPT |
| T3 did not release T4. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md` | Route Decision Matrix | `NOT_RELEASED_WITH_REASON` | T3 readiness matrix | ACCEPT |
| T3A authoring is the next allowed move. | VALUE_SET | `CVF_SESSION/state/entries/nextAllowedMove.json` | value | `MSEA-R24-T3A` | active session state source | ACCEPT |
| T2A config/cache receipt remains the prerequisite local model/config basis. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | Readiness Findings | `CONFIG_CACHE_RECEIPT_READY` | T2A readiness matrix | ACCEPT |
| MinerU command-line parsing supports input path and output directory. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md` | lines 11-19 | `mineru -p <input_path> -o <output_path>` | MinerU usage docs | ACCEPT |
| MinerU CLI exposes `--path`, `--output`, `--backend`, `--method`, `--formula`, and `--table`. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/client.py` | lines 1040-1185 | `main` | MinerU CLI client | ACCEPT |
| MinerU backend choices include `pipeline`. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | lines 3-14 | `BACKEND_PIPELINE` | backend options | ACCEPT |
| MinerU config reader honors `MINERU_TOOLS_CONFIG_JSON`. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/config_reader.py` | lines 14-17 | `MINERU_TOOLS_CONFIG_JSON` | config reader | ACCEPT |
| MinerU local model source resolves to configured models directory. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 211-291 | `resolve_model_source`; `get_local_models_dir` | model download utility | ACCEPT |
| Candidate Group A is authorized for local private CVF testing only with metadata/redaction/excerpt-minimal committed evidence. | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | Operator Authorization Boundary | `Candidate Group A` | R17 intake ledger | ACCEPT |
| T3A direct call-operator invocation form is a new packet instruction derived from the T3 quoting diagnostic, not a pre-existing MinerU source fact. | DOC_ONLY_NEW | `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md` | Risk / Corrective Action | `pathQuotingSafeInvocationDisposition` | T3A dispatch packet | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned T3A baseline path absence | `Test-Path` returned `False` before authoring for the planned T3A baseline path | SAFE_TO_CREATE |
| Planned T3A work order path absence | `Test-Path` returned `False` before authoring for the planned T3A work order path | SAFE_TO_CREATE |
| Token search | `rg -n "MSEA_R24_T3A|MSEA-R24-T3A|PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN|Path Quoting Safe Local Pipeline Rerun" docs CVF_SESSION AGENT_HANDOFF_V35_2026-07-03.md` found only current next-move/session references before new files | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | T3A is a dependent child of accepted T3 diagnostic closure and current next-move surfaces | SAFE_TO_CREATE |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
|---|---|
| worker return under reviews | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| companion reference under reference | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

Literal-shape reminders: do not list required headings with heading prefix
syntax before the real section; avoid `after closure` wording unless a
dependency-release row cites the accepted artifact path and commit.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_WORKER_RETURN_2026-07-04.md` | create uncommitted worker return with selected result token, command evidence, gate evidence, and no-commit statement |
| `docs/reference/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_READINESS_MATRIX_2026-07-04.md` | create uncommitted readiness matrix with metadata-only receipt disposition, T4 release decision, and diagnostic or pass matrix |
| ignored `.cvf/runtime/msea-r24-t3a-*` files | may create local output/log/receipt evidence only; do not stage or commit |

## Evidence Requirements

| Requirement | Required evidence |
|---|---|
| command count | exactly one MinerU CLI invocation or no invocation if preflight holds |
| command form | worker return records direct call-operator command form and absence of `Start-Process` |
| private input boundary | metadata/hash/size only; no source content quote or copied document |
| output disposition | metadata-only output inventory or diagnostic receipt under ignored runtime path |
| T4 decision | explicit `NOT_RELEASED_WITH_REASON` unless `SMOKE_PASS_BOUNDED` is selected and reviewer accepts it |
| no-commit behavior | `git status --short --untracked-files=all` and no HEAD change by worker |

## Acceptance Criteria

| Criterion | Pass condition |
|---|---|
| preflight is source-backed | CLI/config/input/output parent checks are recorded |
| single invocation boundary holds | no second rerun, no alternate backend, no model download |
| result token is exact | one allowed result token is selected in both worker outputs |
| privacy boundary holds | committed artifacts contain only metadata-safe evidence |
| gates pass | worker-return fast gate and pre-implementation autorun pass or failure is returned with diagnostic |

## Review Gate

Reviewer/closer must verify the worker did not commit, did not run a second
rerun, did not quote source content, and did not claim T4/workflow-chain release
without a successful accepted smoke receipt.

## Closure Checklist

- [x] Dispatch packet includes dependency release evidence.
- [x] Dispatch packet includes source verification.
- [x] Dispatch packet includes worker output shape contract.
- [x] Dispatch packet keeps T4 held until accepted smoke evidence exists.
- [x] Dispatch packet preserves Candidate Group A privacy boundary.

## Return-To-Orchestrator Conditions

Worker returns `COMPLETE_PENDING_REVIEW` only after creating the planned
uncommitted worker return and readiness matrix and running required gates.
Worker returns `BLOCKED_WITH_REASON` if source facts contradict this packet,
preflight cannot be satisfied, a second command would be required, or forbidden
scope would be needed.

## Operator Checkpoint

No operator checkpoint is required before T3A worker execution. Operator
checkpoint is required before T4 dispatch, public-sync, provider/live proof,
source/package/checker mutation, or use-case/product expansion.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_WORKER_RETURN_2026-07-04.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without heading prefix syntax. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or recovery requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T3/T3A requires config/cache receipt | Dependency Release Evidence | T2A selected route and receipt fields | pre-dispatch gate | PASS |
| T3 failure requires fresh authority before rerun | Dependency Release Evidence | T3 diagnostic closure commit and token | pre-dispatch gate | PASS |
| Rerun must be bounded | Allowed Command | command count and log path | worker return | PASS |
| T4 remains gated | Claim Boundary | t3aRuntimeSmokeReceiptDisposition | reviewer check | PASS |
| Privacy boundary survives runtime smoke | Candidate Group A Boundary | metadata-only committed evidence | reviewer check | PASS |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher creates packet; worker returns uncommitted outputs; reviewer/closer owns material commit and session-sync |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=5a43cebe; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | baseline and work order only for dispatch; worker may create only two planned outputs plus ignored runtime receipts |
| traceScope(phase, actor) | dispatcher trace in this packet; worker trace in return/matrix; reviewer trace in closure/session-sync |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | MSEA-R24-T3A only; T4 requires separate accepted T3A evidence and work order |
| nextMoveSurfaces | reviewer/closer updates session surfaces only after accepting worker return |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_COMPLETION_2026-07-04.md` |
| reviewerOwnedClosurePaths | worker return, companion readiness matrix, and session state/handoff/front-door updates after material acceptance |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git status --short --untracked-files=all
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned MinerU source mirror plus accepted T2A receipt plus accepted T3 diagnostic plus R17 private-test boundary -> T3A quoting-safe rerun dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this work order and paired baseline |
| Disposition | ADAPT: convert accepted local quoting diagnostic into one bounded private local rerun work order |
| Claim boundary | dispatch only; no parser result, extraction quality, public-sync, provider/live proof, or production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA owner surfaces |
| Enumeration command | filesystem-backed direct reads of cited T2A/T3/R17/MinerU source files |
| Manifest artifact or inline manifest | inline table: Source Verification Block |
| Processing ledger artifact or inline ledger | inline table: Dependency Release Evidence |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | R24 roadmap, T2A accepted artifacts, T3 accepted diagnostic artifacts, R17 private-test ledger, pinned MinerU CLI/config source |
| Unresolved items | actual T3A smoke result, runtime diagnostic, output receipt, T4 release |
| Completion claim boundary | dispatch only; no runtime smoke executed by dispatcher |

ledger_terminal=READ for cited source evidence; ledger_terminal=ADAPTED for T3A dispatch; ledger_terminal=DEFERRED for worker result and T4; ledger_terminal=REJECTED for direct workflow-chain completion from dispatch.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| T3 diagnostic closure | path quoting wrapper failure before processing | RUNTIME_CANDIDATE | T3A work order | dispatch one corrected invocation attempt | one command only |
| MinerU CLI docs/source | local input/output and pipeline backend command surface | DOCTRINE_ADAPTED | T3A work order | source-verified worker command | no API/router/gradio lane |
| T2A config source | local model path receipt exists | RUNTIME_CANDIDATE | T3A worker preflight | reuse process-local env vars | no model download |
| R17 private-test ledger | Candidate Group A local private authorization | DOCTRINE_ADAPTED | T3A privacy boundary | use same smaller file as private input | no source copy/import |
| R22/R24 local MinerU venv | existing ignored local CLI package surface | PACKAGE_CANDIDATE | T3A worker preflight | verify command presence only | no package mutation |
| T4 workflow-chain policy | requires successful T3/T3A smoke evidence | CHECKER_CANDIDATE | future T4 | defer | no checker implementation |
| Direct workflow-chain completion | unsupported by dispatch-only evidence | REJECT_DIRECT_IMPORT | future T4 | reject until accepted smoke receipt | no workflow-chain claim |
| Public export | not authorized | NO_PACKAGE_OR_RUNTIME_VALUE | private provenance only | none | no public-sync |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| T2A config/cache receipt | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | prerequisite remains accepted | cite |
| T3 failed smoke diagnostic | `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md` | ENRICH_EXISTING | releases only quoting-safe rerun authoring | adapt |
| MinerU CLI runtime command | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/client.py` | CONFIRMED_EXISTING | command options are unchanged | cite |
| Candidate Group A private input | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | CONFIRMED_EXISTING | reused without content quotation | cite |
| Workflow-chain completion | `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md` | REJECT_DIRECT_IMPORT | T4 still held | defer |

## Corpus Completeness And Report Integrity

- Corpus task class: T3A dispatch for one bounded local MinerU runtime rerun.
- Corpus root: accepted T2A artifacts, accepted T3 diagnostic artifacts, R17 private-test authorization, and pinned MinerU CLI/config source.
- Snapshot time: 2026-07-04 dispatch authoring.
- Enumeration command: filesystem-backed direct reads of cited source files and negative-search commands above.
- Manifest artifact or inline manifest: Source Verification Block in this work order.
- Manifest hash: N/A with reason: bounded dispatch source set, not a new corpus snapshot.
- Processing ledger artifact or inline ledger: Dependency Release Evidence.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=T2A/T3/R17/MinerU source evidence; ledger_terminal=READ/ADAPTED/DEFERRED/REJECTED; exclusions=manual document body read, content quotes, second runtime command, public-sync, provider/live proof, production claims; unresolved=0 for dispatch authoring.
- Unresolved files: none for dispatch authoring.
- Declared exclusions: runtime execution by dispatcher, second rerun, model download, document-body quotation, public-sync, provider/live proof, production readiness.
- Unreadable or unsupported files: none identified for dispatch authoring.
- Aggregation check: PASS - accepted owner surfaces are cited.
- Drift check: PASS - current next-move surfaces route T3A authoring after T3 diagnostic closure.
- Output traceability: this work order names worker return and readiness matrix.
- Adversarial verification: direct T4 workflow-chain completion and legal/extraction-quality claims are rejected.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local repo authoring |
| Session or invocation | MSEA-R24-T3A dispatch authoring, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads; `rg`; scaffold helper; ADIF resolver; governance gates |
| Target paths | this work order and paired GC-018 baseline |
| Allowed scope source | active state next allowed move and accepted T3 diagnostic closure |
| Before status evidence | `git rev-parse --short HEAD` = `5a43cebe`; worktree clean before authoring; planned paths absent |
| After status evidence | pre-dispatch gates required before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator asked to continue after T3 diagnostic; this dispatch authorizes only T3A worker execution |
| Claim boundary | dispatch packet only; no runtime command run by dispatcher |
| Agent type | dispatcher |
| Invocation ID | `msea-r24-t3a-dispatch-2026-07-04` |
| Expected manifest | T3A GC-018 baseline and T3A work order |
| Actual changed set | to be confirmed by pre-dispatch gate |
| Manifest delta | no extra files expected |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | MSEA-R24-T3A dispatch for one bounded path-quoting-safe local MinerU rerun work order |
| claimDisposition | CLAIM_REJECTED: dispatch does not execute the rerun command or claim runtime success |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker must create smoke receipt or diagnostic |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action in dispatch |
| invocationBoundary | future worker may run exactly one local MinerU CLI invocation after dispatch |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, provider call, or agent coding control is authorized |
| claimLanguage | dispatch-only rerun authorization |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router behavior outside this packet |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationStorageChange | NOT_APPLICABLE_WITH_REASON |
| durableGovernanceFileMutation | NO |
| generatedAggregateMutation | NO |
| reason | This work order creates dispatch artifacts only and does not create, split, relocate, or refactor durable governance foundation files. |

## Claim Boundary

This work order authorizes only a no-commit worker to perform one local
path-quoting-safe MinerU CLI rerun and produce metadata-safe private evidence.
It does not authorize T4 dispatch, public-sync, provider/live proof, model
download/cache mutation, package/checker/source mutation, document-content
quotation, extraction-quality claims, legal/current-law claims, workflow-chain
completion, production readiness, stage, commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T3A is private provenance runtime-smoke dispatch using private Candidate
Group A inputs and ignored local runtime evidence only.
