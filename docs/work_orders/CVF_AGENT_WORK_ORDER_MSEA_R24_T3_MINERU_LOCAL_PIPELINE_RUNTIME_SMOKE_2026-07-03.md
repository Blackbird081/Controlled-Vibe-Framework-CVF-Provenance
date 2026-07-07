# CVF Agent Work Order - MSEA-R24-T3 MinerU Local Pipeline Runtime Smoke

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-03

Batch ID: MSEA-R24-T3

Dispatch base head: 71737425

Commit mode: WORKER_MUST_NOT_COMMIT

Worker return path: `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md`

Companion reference path: `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md`

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R24-T3.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-03.

Do-not-misread notes: this packet authorizes at most one local MinerU CLI smoke
using the accepted T2A config/cache receipt and one authorized Candidate Group A
DOCX file. It forbids model download, a second smoke, manual document body
inspection, content quotation in committed artifacts, external export,
provider API proof, extraction-accuracy/legal-quality/current-law claims,
workflow-chain completion, release-readiness claims, stage, commit, or push.

Required first actions: read this work order, paired baseline, accepted T2A
worker return and readiness matrix, R17 private-test intake ledger, MinerU
CLI/config source, checker source read-ahead files, and literal-format gotchas
before creating worker outputs or running the command.

Return contract: create the worker return artifact and companion readiness
matrix, run required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Run one bounded local MinerU CLI runtime smoke, if preflight confirms the
accepted config receipt, local venv command, and one Candidate Group A input
are present. The worker must record either a smoke receipt or a diagnostic hold
without rerunning or expanding scope.

## Scope

| Field | Value |
|---|---|
| Allowed scope | one local MinerU CLI smoke plus ignored runtime output/log/receipt evidence and two governed worker outputs |
| Forbidden scope | second smoke command, model download/cache mutation, manual document body read, content quote, public-sync, provider/live proof, RAG/S3, schema/writer/adapter/checker implementation, production claim |
| Target | ignored `.cvf/runtime` smoke output/log evidence and governed worker return/reference outputs |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | Operator asked Codex to continue the approved T1-T4 MinerU chain after T2A accepted config/cache evidence. |
| scope classification | Bounded single-tranche work order: one local smoke command, two governed worker outputs, and ignored `.cvf/runtime` receipts only. |
| risk sensitivity | Sensitive private Candidate Group A legal-policy input, local runtime process, provider/live/public-sync and production-readiness risks all remain constrained by this packet. |
| selected role route | routeMode=`MULTI_AGENT_SINGLE_ROLE`; dispatcher creates packet, worker executes no-commit smoke, reviewer/closer owns material commit and session-sync. |
| role separation basis | Worker must not commit; reviewer/closer conversion preserves separate execution and acceptance accountability. |
| escalation condition | Hold or stop on missing CLI/config/input, hash or size mismatch, command timeout/failure, teardown uncertainty, second-command need, or checker failure. |
| routingBoundary | MinerU source mirror, accepted T2A config/cache receipt, and R17 private-test ledger only. |

## Authority Chain

| Authority | Path or commit | Disposition |
|---|---|---|
| Operator instruction | current session request to continue T1-T4 through governed dependency gates | ACCEPT |
| R24 roadmap | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | ACCEPT |
| T2A accepted worker return | `docs/reviews/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_WORKER_RETURN_2026-07-03.md` | ACCEPT |
| T2A readiness matrix | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | ACCEPT |
| Candidate Group A private-test boundary | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | ACCEPT |
| MinerU source mirror | `.private_reference/source_mirrors/opendatalab__MinerU/` | ACCEPT |

## Agent Roles

| Role | Responsibility | Commit authority |
|---|---|---|
| Dispatcher | author baseline and work order | may commit dispatch after gates |
| Worker | run at most one allowed local smoke and create two uncommitted outputs | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | repair, review, commit accepted worker outputs, and sync session | owns closure commit |

## Required First Reads

1. `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_2026-07-03.md`
2. `docs/baselines/CVF_GC018_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_2026-07-03.md`
3. `docs/reviews/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_WORKER_RETURN_2026-07-03.md`
4. `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md`
5. `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md`
6. `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md`
7. `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/cli_tools.md`
8. `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/client.py`
9. `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/config_reader.py`
10. `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py`
11. Checker files listed in the Checker Source Read-Ahead Block.

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
| `.cvf/runtime/msea-r24-t3-*` log/output/receipt evidence | may write ignored local runtime evidence |
| Candidate Group A original DOCX files | may be read only by the single MinerU command; do not copy/import/stage/commit |
| Repository source, checkers, session state, public-sync, package files | forbidden |

## Candidate Group A Privacy Boundary

| Field | Value |
|---|---|
| Input chosen for smoke | `148_2025_QH15_675262.docx` because it is the smaller authorized Candidate Group A file in R17 metadata |
| Source location | operator-local CVF-Workspace sibling path named in Pre-Flight Checks |
| Worker artifact rule | committed artifacts may include only metadata, hash/size, command status, output file names/counts, and excerpt-minimal or redacted evidence if unavoidable |
| Forbidden evidence | no source document copy/import, no original file commit, no full extraction output commit, no sensitive legal/personal detail quotation, no public-sync |

## Allowed Command

The only authorized smoke command is the local MinerU CLI invocation below,
with process-local environment variables and output under ignored `.cvf/runtime`:

```powershell
$env:MINERU_TOOLS_CONFIG_JSON = "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\.cvf\runtime\msea-r24-t2a-huggingface-mineru.json"
$env:MINERU_MODEL_SOURCE = "local"
$env:MINERU_DEVICE_MODE = "cpu"
$env:MINERU_API_OUTPUT_ROOT = "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\.cvf\runtime\msea-r24-t3-api-output"
$env:MINERU_LOCAL_API_STARTUP_TIMEOUT_SECONDS = "300"
$env:MINERU_TASK_RESULT_TIMEOUT_SECONDS = "900"
.\.cvf\runtime\msea-r22-mineru-venv\Scripts\mineru.exe -p "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\148_2025_QH15_675262.docx" -o ".\.cvf\runtime\msea-r24-t3-output" -b pipeline -m auto -f false -t false
```

The worker may redirect stdout/stderr to
`.cvf/runtime/msea-r24-t3-runtime-smoke.log` as part of this single command
attempt. If the CLI launches a temporary local `mineru-api`, that process is
authorized only as part of this single command and must be verified stopped or
diagnosed after the command exits or times out.

## Allowed Result Tokens

Worker must select exactly one:

| Token | Meaning |
|---|---|
| SMOKE_PASS_BOUNDED | One command exited 0, expected output directory exists, and only metadata-safe output receipt is recorded. |
| SMOKE_FAIL_DIAGNOSTIC_RECORDED | One command ran and failed or timed out; diagnostic is recorded and no rerun happened. |
| HOLD_PENDING_RUNTIME_ENV_FIX | Preflight or command evidence shows a missing path, missing dependency, lingering process, or local environment issue that needs a later fix. |
| HOLD_ALL_RUNTIME_LANES | No T4 workflow-chain lane may open. |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Capture `executionBaseHead` and initial `git status --short --untracked-files=all`. | worker return |
| 2 | Create short worker-return skeleton using helper before long prose. | worker return gate evidence |
| 3 | Confirm planned worker outputs are absent. | worker return |
| 4 | Confirm MinerU CLI, T2A config, configured pipeline path, Candidate Group A input, and output parent exist. | worker return and matrix |
| 5 | Run exactly one allowed command, or hold before command if preflight fails. | log file and worker return |
| 6 | Capture exit code, duration, log path, output directory file-name inventory, and process teardown evidence. | readiness matrix |
| 7 | Select exactly one allowed result token. | worker return and readiness matrix |
| 8 | Run worker-return fast gate and pre-implementation autorun. | gate evidence |

## Worker Autonomy / No-Question Rule

The worker must proceed without asking the operator for preferences when the
answer is source-verifiable from this packet, the paired baseline, cited MinerU
source, current worktree state, or checker output. If the single allowed smoke
fails, times out, or cannot start because of preflight, the worker records the
diagnostic and returns an allowed hold token rather than rerunning, changing
input, downloading models, or expanding scope.

## Forbidden Scope

Worker must not run a second smoke command, rerun after failure, run model
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
| T2A accepted worker return | `docs/reviews/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_WORKER_RETURN_2026-07-03.md` | `b53786d9` | SATISFIED |
| T2A readiness matrix | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | `b53786d9` | SATISFIED |
| T2A session sync | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `71b10f74` | SATISFIED |
| T2A handoff/session lifecycle wording | `AGENT_HANDOFF_V35_2026-07-03.md` and active session generated state | `5af0d29f`; `71737425` | SATISFIED |
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
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R24-T3 --title "MinerU Local Pipeline Runtime Smoke" --date 2026-07-03 --base a6d08fd5 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| finalDispatchBaseAdjustment | Updated dispatch base to `71737425` after separate lifecycle session-wording and handoff-marker hygiene commits. |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled dispatch prompt envelope, authority chain, allowed command, source verification, dependency release evidence, worker packet-shape contract, and privacy boundary. |
| checkerReadAheadConfirmation | Checker Source Read-Ahead Block lists dispatch, worker-return, and absorption gates used for this packet. |
| docOnlyNewFields | `runtimeSmokeReceiptDisposition`; `runtimeSmokeOutputBoundary`; `candidateGroupASmokeInput` |
| claimBoundary | Scaffold provenance describes dispatch packet shape only; no command has been run by dispatch. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; Dependency Release Evidence; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; External Knowledge Intake Routing row labels; External Absorption Core row labels; ledger_terminal=; Corpus verdict bullet; Allowed Result Tokens; Allowed Command; Public Export Disposition |
| gateRunPurpose | Confirmation evidence after checker source read-ahead; gates confirm this work order shape. |
| claimBoundary | Read-ahead covers this dispatch packet; worker output artifacts require their own checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R24 roadmap allows T3 only after config/cache receipt. | VALUE_SET | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | T1-T4 Dependency Contract | `MSEA-R24-T3` | R24 roadmap | ACCEPT |
| T2A selected config/cache receipt ready. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | top route fields | `CONFIG_CACHE_RECEIPT_READY` | T2A readiness matrix | ACCEPT |
| T2A config writeback receipt is absolute-path written. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | top receipt fields | `CONFIG_WRITTEN_ABSOLUTE_PATH` | T2A readiness matrix | ACCEPT |
| MinerU command-line parsing supports input path and output directory. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md` | Quick Usage via Command Line | `mineru -p <input_path> -o <output_path>` | MinerU usage docs | ACCEPT |
| MinerU CLI starts a temporary local API when `--api-url` is omitted. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md` | Quick Usage via Command Line tip | `--api-url` omitted | MinerU usage docs | ACCEPT |
| MinerU CLI exposes local input, output, backend, method, start, and end options. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/client.py` | lines 1037-1147 | `main` click options | MinerU CLI client | ACCEPT |
| MinerU backend choices include `pipeline`. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | top constants | `BACKEND_PIPELINE` | backend options | ACCEPT |
| MinerU config reader honors `MINERU_TOOLS_CONFIG_JSON`. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/config_reader.py` | top config constant and `read_config` | `MINERU_TOOLS_CONFIG_JSON` | config reader | ACCEPT |
| MinerU local model source resolves to configured `models-dir`. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 211-249 and 288-295 | `resolve_model_source`; `get_local_models_dir` | model download utility | ACCEPT |
| Candidate Group A permits local private testing only with metadata/redaction/excerpt-minimal committed evidence. | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | Operator Authorization Boundary | `Candidate Group A` | R17 intake ledger | ACCEPT |

## Required Worker Outputs

| Path | Required status |
|---|---|
| `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md` | create, uncommitted |
| `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md` | create, uncommitted |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | Optional; prefer repairing evidence in the worker return per gotcha 30. |
| reviewerOwnedClosurePaths | worker return and companion readiness matrix |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Worker output checker read-ahead mandate:

- The worker must read the checker files named in this work order as applied to the review worker return and the reference companion before writing the first substantive output section.
- The worker return must include section name: Target / Source; section name: Scope / Methodology; section name: Findings / Position; section name: Risk / Corrective Action; section name: Decision / Disposition; section name: External Knowledge Intake Routing; section name: Rescan Intelligence Hardening; section name: Corpus Completeness And Report Integrity; section name: Finding-To-Governance Learning Disposition; section name: Epistemic Process Block; section name: Agent Operation Trace Block; section name: Delta Execution Claim Boundary Control Block; section name: Public Export Disposition; section name: git status --short; section name: Changed Files; section name: No-Commit Statement.
- The companion reference must include section name: Scope / Applies To, `ledger_terminal=` marker, and a terminal selected route token.
- The worker must run `python governance/compat/run_worker_return_fast_gate.py` after creating a short skeleton and again after filling content.
- Individual checker substitution is forbidden unless the full fast gate itself is also run.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned MinerU source mirror plus accepted T2A local receipt plus R17 private-test boundary -> T3 local runtime-smoke dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this work order and paired baseline |
| Disposition | ADAPT: dispatch one bounded private local runtime-smoke command |
| Claim boundary | dispatch only; no parser result, extraction quality, public-sync, or production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA owner surfaces |
| Enumeration command | filesystem-backed direct reads of cited T2A/R17/MinerU source files |
| Manifest artifact or inline manifest | inline table: Source Verification Block |
| Processing ledger artifact or inline ledger | inline table: Execution Plan and Allowed Result Tokens |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | R24 roadmap, T2A accepted artifacts, R17 private-test ledger, pinned MinerU CLI/config source |
| Unresolved items | smoke result, runtime diagnostic, output receipt, T4 release |
| Completion claim boundary | dispatch only; no runtime smoke executed by dispatcher |

ledger_terminal=READ for cited source evidence; ledger_terminal=ADAPTED for T3 dispatch; ledger_terminal=DEFERRED for worker result and T4; ledger_terminal=REJECTED for direct workflow-chain completion from T3 dispatch.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| T2A readiness matrix | config/cache receipt exists | RUNTIME_CANDIDATE | T3 worker | run one bounded smoke | one command only |
| MinerU CLI docs/source | `mineru -p ... -o ... -b pipeline` command surface | DOCTRINE_ADAPTED | T3 worker | source-verified command | no API/router/gradio lane |
| MinerU config source | local model source reads configured `models-dir` | RUNTIME_CANDIDATE | T3 worker | set process-local env vars | no model download |
| R17 private-test ledger | Candidate Group A local private authorization | DOCTRINE_ADAPTED | T3 privacy boundary | use one smaller file as private input | no source copy/import |
| T4 workflow-chain policy | requires T3 smoke evidence | CHECKER_CANDIDATE | future T4 | defer | no checker implementation |
| MinerU package state | local ignored venv already exists from prior accepted work | PACKAGE_CANDIDATE | T3 worker preflight | verify command presence only | no package mutation |
| Direct workflow-chain completion | not supported by dispatch-only evidence | REJECT_DIRECT_IMPORT | future T4 | reject until accepted smoke receipt | no workflow-chain claim |
| Public export | not authorized | NO_PACKAGE_OR_RUNTIME_VALUE | private provenance only | none | no public-sync |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| T2A config/cache receipt | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | releases T3 authoring | dispatch |
| MinerU CLI runtime command | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/client.py` | ENRICH_EXISTING | exact local command surface for smoke | adapt |
| Candidate Group A private input | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | CONFIRMED_EXISTING | reused as one private smoke input without content quotation | cite |
| Workflow-chain completion | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | REJECT_DIRECT_IMPORT | T4 only after accepted T3 evidence | defer |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or recovery requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T3 requires config/cache receipt | Dependency Release Evidence | T2A selected route and receipt fields | pre-dispatch gate | PASS |
| T3 may run one bounded local smoke | Allowed Command | command evidence | worker return | PASS |
| T4 remains gated | Forbidden Scope | runtimeSmokeReceiptDisposition | reviewer check | PASS |
| Privacy boundary survives smoke | Candidate Group A Privacy Boundary | metadata-only committed evidence | reviewer check | PASS |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher creates packet; worker returns uncommitted outputs; reviewer/closer owns material commit and session-sync |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=71737425; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | baseline and work order only for dispatch; worker may create only two planned outputs and ignored runtime receipts |
| traceScope(phase, actor) | dispatcher trace in this packet; worker trace in return/matrix; reviewer trace in closure/session-sync |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | MSEA-R24-T3 only; T4 requires separate release evidence and work order |
| nextMoveSurfaces | reviewer/closer updates session surfaces only after accepting worker return |

## Corpus Completeness And Report Integrity

- Corpus task class: T3 work-order dispatch for one bounded local MinerU runtime smoke.
- Corpus root: accepted T2A artifacts, R17 private-test authorization, and pinned MinerU CLI/config source.
- Snapshot time: 2026-07-03 dispatch authoring.
- Enumeration command: filesystem-backed direct reads of cited source files and negative-search commands recorded in the paired baseline.
- Manifest artifact or inline manifest: Source Verification Block in this work order.
- Manifest hash: N/A with reason: bounded dispatch source set, not a new corpus snapshot.
- Processing ledger artifact or inline ledger: Execution Plan and Allowed Result Tokens.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=T2A/R17/MinerU source evidence; ledger_terminal=READ/ADAPTED/DEFERRED/REJECTED; exclusions=manual document body read, content quotes, second runtime command, public-sync, provider/live proof, production claims; unresolved=0 for dispatch authoring.
- Unresolved files: none for dispatch authoring.
- Declared exclusions: runtime execution by dispatcher, second smoke command, model download, document-body quotation, public-sync, provider/live proof, production readiness.
- Unreadable or unsupported files: none identified for dispatch authoring.
- Aggregation check: PASS - accepted owner surfaces are cited.
- Drift check: PASS - current next-move surfaces route T3 authoring after T2A.
- Output traceability: worker return and readiness matrix are named.
- Adversarial verification: direct T4 workflow-chain completion and legal/extraction-quality claims are rejected.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Verification Commands

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md --title "CVF MSEA-R24-T3 MinerU Local Pipeline Runtime Smoke Worker Return"
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git status --short --untracked-files=all
```

## Evidence Requirements

| Requirement | Evidence |
|---|---|
| Single command proof | command line, environment keys without secrets, exit code or timeout class, duration, and log path |
| Preflight proof | MinerU CLI path, config path, configured pipeline path, Candidate Group A input hash/size, output parent |
| Smoke output proof | metadata-only output directory inventory and expected receipt file names/counts if created |
| Teardown proof | no lingering MinerU local API process attributable to this smoke, or diagnostic if unknown |
| Failure proof | diagnostic class, stage, retryability, safe message, and no-rerun statement |
| Boundary proof | final `git status --short --untracked-files=all` and changed path list |
| Gate proof | worker-return fast gate and pre-implementation autorun output summary |

## Acceptance Criteria

| Criterion | Required disposition |
|---|---|
| Exactly one allowed command attempted or a preflight hold recorded | PASS or BLOCKED_WITH_REASON |
| Worker output paths created | PASS or BLOCKED_WITH_REASON |
| Result token selected from allowed set | PASS |
| No forbidden content quotation/public/provider/package/checker work | PASS |
| Gates run with real executionBaseHead | PASS or diagnostic if blocked |

## Review Gate

Reviewer must confirm worker outputs satisfy the Worker Return Packet Shape
Contract, command count is at most one, ignored runtime receipt/log evidence is
private and metadata-safe, Candidate Group A content is not quoted, and no T4
workflow-chain release is claimed unless the selected T3 token and smoke
receipt support a fresh T4 work order.

## Closure Checklist

| Item | Required resolution |
|---|---|
| Worker return reviewed | checked, N/A with reason, or BLOCKED |
| Companion readiness matrix reviewed | checked, N/A with reason, or BLOCKED |
| Gate evidence verified | checked, N/A with reason, or BLOCKED |
| T4 release decision recorded | checked, N/A with reason, or BLOCKED |
| Session sync updated after accepted material commit | checked, N/A with reason, or BLOCKED |

## Return-To-Orchestrator Conditions

Return to orchestrator if the allowed command path is missing, the Candidate
Group A input is unavailable or hash/size mismatches R17, a second command would
be required, local API teardown cannot be safely assessed, source facts
contradict this packet, or gates reveal an out-of-scope repair need.

## Operator Checkpoint

No operator checkpoint is required before the single T3 smoke because the
operator authorized the dependency-gated T1-T4 sequence and Candidate Group A is
already authorized for local private testing only. A new operator checkpoint is
required before any fuller content inclusion, public-sync, Candidate Group B
use, second smoke, nonlocal provider route, or T4 execution without fresh
release evidence.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R24-T3 local pipeline runtime smoke dispatch, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, source reads, scaffold helper, apply_patch, governance gates |
| Target paths | this work order and paired baseline |
| Allowed scope source | T2A material commit `b53786d9`; session-sync commit `71b10f74`; handoff marker `a6d08fd5`; lifecycle wording commit `5af0d29f`; handoff marker commit `71737425` |
| Before status evidence | clean worktree at `71737425` before final dispatch gate rerun |
| After status evidence | baseline and work order pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no runtime smoke executed by dispatch |
| Agent type | dispatcher |
| Invocation ID | `msea-r24-t3-local-pipeline-runtime-smoke-work-order-dispatch-2026-07-03` |
| Expected manifest | this work order and paired baseline |
| Actual changed set | this work order and paired baseline |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R24-T3 work order for one bounded local MinerU runtime-smoke command |
| claimDisposition | CLAIM_REJECTED: dispatch does not execute the command or claim smoke success |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker must create smoke receipt or diagnostic |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no command action in dispatch |
| invocationBoundary | local governed dispatch authoring only |
| interceptionBoundary | no provider, Web, MCP, adapter, model-router, action-authority, or production route interception claim |
| claimLanguage | work-order dispatch and future worker receipt only |
| forbiddenExpansion | no second smoke, model download, public-sync, provider/live proof, RAG/S3, schema/writer/adapter/checker implementation, benchmark, extraction-accuracy, legal-quality, workflow-chain completion, or production-readiness claim |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationStorageImpact | N/A with reason: this work order does not create, split, relocate, or refactor durable governance foundation files. |
| stablePathDecision | N/A with reason: only dated dispatch/worker artifacts are authorized. |
| indexUpdateDecision | N/A with reason: no stable foundation family or README index is changed. |
| claimBoundary | This block is included because the artifact cites `docs/reference` owner surfaces; it does not authorize foundation storage changes. |

## Claim Boundary

This work order authorizes exactly one local MinerU CLI runtime-smoke attempt
under worker control and no other runtime action. It does not authorize a
second command, cache mutation, model download, manual document body read,
content quotation, public-sync, provider/live proof, extraction accuracy
claim, legal-quality claim, workflow-chain completion, production readiness,
stage, commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet for local Candidate Group A smoke;
no public-sync export is authorized.
