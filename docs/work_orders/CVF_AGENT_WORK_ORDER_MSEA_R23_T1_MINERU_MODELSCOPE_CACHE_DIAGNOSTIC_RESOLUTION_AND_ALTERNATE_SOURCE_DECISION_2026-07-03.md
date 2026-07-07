# CVF Agent Work Order - MSEA-R23-T1 MinerU ModelScope Cache Diagnostic Resolution And Alternate Source Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R23_T1

Dispatch base head: d0d4f120

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_DECISION_WORKER_RETURN_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R23_T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_DECISION_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker must capture `git rev-parse --short HEAD` before edits.

Current-time notes: artifact date is 2026-07-03; use current repository state, accepted R22 closure evidence, and the pinned MinerU source mirror.

Do-not-misread notes: this packet authorizes only R22 diagnostic inspection, reuse of the ignored R22 venv, R23 config/log redirection, and one ModelScope pipeline cache resume/retry. It does not authorize parser/OCR/VLM/API/router/Gradio/Docker/WSL execution, local service startup, document body read, extraction outputs, public-sync, alternate model-source command execution, schema/writer/adapter/checker implementation, legal advice, current-law, runtime smoke, production, or workflow-chain claims.

Required first actions: read startup files, guard orientation, literal gotchas, this work order, the paired GC-018 baseline, source references, and checker source listed in the Checker Source Read-Ahead Block before writing worker outputs.

Return contract: create the worker return and companion readiness matrix, run required gates, leave governed changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute the bounded R23 diagnostic-resolution lane: carry forward the accepted R22 timeout evidence, verify the R22 ignored venv and command are still available, inspect secret-safe local cache/config/log metadata, and run exactly one ModelScope pipeline cache resume/retry with R23 config redirection if prerequisites are satisfied. Success means the worker can classify whether cache/config readiness is now enough to author a later runtime-smoke work order, whether ModelScope remains held for more diagnostics, or whether an alternate model-source decision should be opened.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R23-T1 --title "MinerU ModelScope Cache Diagnostic Resolution And Alternate Source Decision" --date 2026-07-03 --base d0d4f120 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed scaffold fields, set DISPATCH_READY, added R22 dependency release, source-verified retry/cache/config facts, local runtime mutation envelope, worker-output shape mandate, route tokens, and allowed command sequence. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; and worker-output checker token summaries for worker-return, structural, Delta, external-intake, rescan, corpus, finding, and epistemic gates. |
| docOnlyNewFields | selectedRouteToken; retryCommandDisposition; r22DiagnosticCarryForward; r23ConfigWritebackReceipt; modelCacheCompletionReceipt; alternateSourceDecision; runtimeSmokeGateDisposition |
| claimBoundary | Dispatch authoring provenance only; no parser/OCR/VLM/API/Docker/service/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the literal required shape. Worker should return to orchestrator only for a source contradiction, missing R22 venv or command, active cache-prep process that makes retry unsafe, failed network/download diagnostic that cannot be classified safely, forbidden-scope need, or missing authority that makes completion impossible.

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition |
| --- | --- | --- | --- |
| MSEA-R22-T1 accepted ModelScope download diagnostic | `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | `7b105700` | SATISFIED - selected `HOLD_PENDING_MODELSCOPE_DOWNLOAD_DIAGNOSTIC` after local package activation succeeded but ModelScope cache prep timed out |
| Session next-move freshness | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V34_2026-07-03.md` | `d0d4f120` | SATISFIED - next allowed move permits fresh diagnostic-aware ModelScope cache resume/retry or alternate model-source decision |
| Operator authorization | current operator instruction in this session | N/A | SATISFIED - operator said to continue using R22 material commit `7b105700` and prior proposal |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | Worker output checker read-ahead is mandatory; provider-local authority is excluded; cache retry remains isolated to ignored local runtime paths; cache completion is not parser runtime readiness. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; ADIF resolver query exactness; Dependency Release Evidence; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields; Worker Return Packet Shape Contract fields; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; Delta block field labels; Agent Operation Trace labels; worker output section names Target / Source, Scope / Methodology, Findings / Position, Risk / Corrective Action, External Knowledge Intake Routing, Rescan Intelligence Hardening, Corpus Completeness And Report Integrity, Finding-To-Governance Learning Disposition, and Epistemic Process Block. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm this work order's dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this work order and paired baseline only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R23-T1 must re-read current CVF-governed sources, accepted R22 artifacts, pinned MinerU source mirror docs/source, and local ignored runtime metadata before any retry command.

unicodePathHandling: Use LiteralPath and UTF-8-safe command output for local paths; do not normalize or rewrite filenames.

extractedTextAuthority: N/A with reason

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` |
| priorVerificationAnchor | `selectedRouteToken: HOLD_PENDING_MODELSCOPE_DOWNLOAD_DIAGNOSTIC` |
| recomputeReason | R23-T1 must re-read current CVF-governed sources, accepted R22 artifacts, pinned MinerU source mirror docs/source, and local ignored runtime metadata before any retry command |
| freshRecomputeRequired | true for R22 venv status, active process status, command availability, R22 log/config/cache metadata, R23 config path, retry command result, and diagnostics; no document body read and no parser extraction |
| unicodePathHandling | Use `-LiteralPath` and UTF-8-safe command output for local paths; do not normalize or rewrite filenames |
| extractedTextAuthority | N/A with reason |

## Operator Authorization And Privacy Boundary

The operator authorized continuing from the R22 diagnostic hold for local private CVF testing only. Candidate Group A source documents remain private and must not be public-synced or redistributed. R23 may create metadata/redacted evidence about cache diagnostics and a retry command but must not copy source documents into the repository, read source document body content, create parser outputs, or include sensitive personal/legal details in committed artifacts.

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MinerU source mirror remains the current upstream authority for this lane. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | line 35 | `opendatalab__MinerU` | source mirror index | ACCEPT |
| R22 selected a ModelScope download diagnostic hold. | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | line 11 | `HOLD_PENDING_MODELSCOPE_DOWNLOAD_DIAGNOSTIC` | R22 readiness matrix | ACCEPT |
| R22 package install succeeded in the ignored venv. | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | line 57 | `.cvf/runtime/msea-r22-mineru-venv` | R22 readiness matrix | ACCEPT |
| R22 command activation succeeded. | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | line 58 | `mineru-models-download.exe` | R22 readiness matrix | ACCEPT |
| R22 cache prep timed out and did not write config. | VALUE_SET | VALUE_SET | `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md` | lines 173-176 | `TIMEOUT_PARTIAL` | R22 worker return | ACCEPT |
| MinerU project exposes `mineru-models-download` as a console script. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | line 133 | `mineru-models-download` | project scripts | ACCEPT |
| MinerU supports ModelScope through `MINERU_MODEL_SOURCE`. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | lines 12-20 | `MINERU_MODEL_SOURCE` | model-source documentation | ACCEPT |
| MinerU completed downloads write model path and model source to config. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | lines 37-49 | `mineru-models-download` | model-source documentation | ACCEPT |
| MinerU model updates can be incrementally updated if the local model folder has not been moved. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 48 | `mineru-models-download` | model-source documentation | ACCEPT |
| MinerU download CLI supports source and model-type options. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 96-114 | `download_models` | model download CLI | ACCEPT |
| MinerU pipeline model download enumerates pipeline model paths and writes configuration. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 36-52 | `download_pipeline_models` | model download CLI | ACCEPT |
| MinerU config path can be redirected by `MINERU_TOOLS_CONFIG_JSON`. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 23-25 | `get_tools_config_file_path` | config path helper | ACCEPT |
| MinerU ModelScope download uses snapshot download and pipeline root resolution helpers. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 254-279 | `_snapshot_download_cached` | model download utility | ACCEPT |
| Local `.cvf/runtime` is ignored and suitable for R23 config/log side effects. | VALUE_SET | VALUE_SET | `.gitignore` | lines 49-51 | `.cvf/runtime/` | repository ignore policy | ACCEPT |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R22 ModelScope download diagnostic | `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | ENRICH_EXISTING | R23 narrows the hold into one diagnostic-aware resume/retry and route decision. | ADAPT |
| MinerU source mirror facts | `.private_reference/source_mirrors/INDEX.md` plus R22/R23 Source Verification Blocks | CONFIRMED_EXISTING | Source mirror authority is reused without source import. | NO_NEW_OWNER |
| R23 config receipt | `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_DECISION_2026-07-03.md` | NEW_FINDING | R23 writes a separate config path to avoid confusing R22 absence evidence with a later retry receipt. | ABSORB_AS_BOUNDARY |
| Parser/runtime smoke | `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json` | REJECT_DIRECT_IMPORT | Runtime smoke remains outside R23. | DEFER |
| Alternate model source | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | R23 may recommend a future alternate-source decision only; it may not execute alternate-source download. | DEFER |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | Pinned MinerU source mirror is used as the external upstream input for a governed local cache diagnostic dispatch. |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and the paired R23 baseline |
| Disposition | ROUTED_TO_GOVERNED_WORK_ORDER_WITH_LOCAL_RUNTIME_DIAGNOSTIC |
| Claim boundary | Source mirror evidence supports only this cache diagnostic dispatch; no source import, parser runtime, public-sync, or production claim. |

## New Doc-Only Fields

| Field | Meaning | Disposition |
| --- | --- | --- |
| selectedRouteToken | Worker-selected next route for reviewer/closer consideration | DOC_ONLY_NEW |
| retryCommandDisposition | Worker classification of the single R23 retry command | DOC_ONLY_NEW |
| r22DiagnosticCarryForward | Worker summary of accepted R22 timeout/config/cache evidence | DOC_ONLY_NEW |
| r23ConfigWritebackReceipt | Secret-safe metadata for `.cvf/runtime/msea-r23-mineru.json` if created | DOC_ONLY_NEW |
| modelCacheCompletionReceipt | Secret-safe cache/root evidence if cache completion occurs | DOC_ONLY_NEW |
| alternateSourceDecision | Whether a future alternate-source decision work order is recommended | DOC_ONLY_NEW |
| runtimeSmokeGateDisposition | Whether a later parser smoke work order can be authored | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R23 artifact path check | `Test-Path` for planned baseline, work order, worker return, and companion reference returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| R23 token search | `rg -n "MSEA_R23_T1|MSEA-R23-T1|MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION|ModelScope Cache Diagnostic Resolution And Alternate Source Decision" docs CVF_SESSION AGENT_HANDOFF_V34_2026-07-03.md .private_reference\source_mirrors\INDEX.md` returned no matches before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | MSEA-R23-T1 is a new child tranche released by accepted MSEA-R22-T1 and operator authorization | SAFE_TO_CREATE |

## Authority Chain

- Operator instruction: continue after R22 diagnostic hold.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V34_2026-07-03.md`.
- Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_DECISION_2026-07-03.md`.
- Accepted R22 diagnostic and readiness matrix.
- Candidate Group A private intake remains the privacy boundary; no document-body reads are authorized.
- MinerU source authority: `.private_reference/source_mirrors/opendatalab__MinerU/`.

Authority boundary: if any source contradicts this packet, stop and return `BLOCKED_WITH_REASON`. The worker may not upgrade cache-prep language into parser runtime, service startup, extraction accuracy, legal-quality, public, workflow-chain, or production authority.

## Required First Reads

| Source | Required action |
| --- | --- |
| active session front door named by root agent instructions | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V34_2026-07-03.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| paired GC-018 baseline | READ |
| this work order | READ |
| source files listed in Source Verification Block | READ |
| checker source listed in Checker Source Read-Ahead Block | READ |

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Operator | operator | owns retry, alternate-source, parser-runtime, document-body, public-sync, and production decisions |
| Dispatcher | dispatcher role | authors this GC-018/work order and runs pre-dispatch gates |
| Worker | delegated worker role | executes allowed local cache diagnostic and one retry command, creates only the named worker return and companion readiness matrix, without commit |
| Reviewer/closer | reviewer/closer | reviews returned artifacts, repairs allowed-scope shape defects if needed, commits material if accepted |
| Session-sync steward | reviewer/closer once material is accepted | updates active session state once accepted material exists |

## Pre-Flight Checks

Required before worker execution:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path 'docs\reviews\CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_DECISION_WORKER_RETURN_2026-07-03.md'
Test-Path 'docs\reference\CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_READINESS_MATRIX_2026-07-03.md'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected result: clean worktree at execution start, planned worker outputs absent before writing, and pre-implementation gate passing after worker output authoring and allowed-scope repairs.

## Write Ownership

| Path family | Worker permission |
| --- | --- |
| `docs/reviews/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_DECISION_WORKER_RETURN_2026-07-03.md` | CREATE_ONLY_UNCOMMITTED |
| `docs/reference/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_READINESS_MATRIX_2026-07-03.md` | CREATE_ONLY_UNCOMMITTED |
| `.cvf/runtime/msea-r22-mineru-venv/` | READ_OR_REUSE_LOCAL_IGNORED_RUNTIME_VENV |
| `.cvf/runtime/msea-r23-mineru.json` | CREATE_OR_UPDATE_LOCAL_IGNORED_MINERU_CONFIG |
| `.cvf/runtime/msea-r23-cache-resume.log` | CREATE_OR_UPDATE_LOCAL_IGNORED_DIAGNOSTIC_LOG |
| model cache created or resumed by the MinerU download command | LOCAL_SIDE_EFFECT_ALLOWED_UNTRACKED |
| session-state, front-door, and active-handoff surfaces | FORBIDDEN |
| `.private_reference/source_mirrors/**` | READ_ONLY source authority; no source edits |
| public-sync, Web, MCP, model-router, checker, adapter, schema/writer, runtime source implementation paths | FORBIDDEN |

## Allowed / Forbidden Scope

| Scope item | Disposition |
| --- | --- |
| Inspect R22 venv, command, config, log, cache metadata, and active process status | ALLOWED |
| Reuse R22 venv if present and command exists | ALLOWED |
| Redirect MinerU config to `.cvf/runtime/msea-r23-mineru.json` for the retry | ALLOWED |
| Run one ModelScope pipeline cache resume/retry command | ALLOWED |
| Create the two named worker output artifacts | ALLOWED |
| Reinstall MinerU outside the R22 venv | FORBIDDEN |
| Run alternate-source download commands such as HuggingFace or local source | FORBIDDEN |
| Parser/OCR/VLM/API/router/Gradio/Docker/WSL execution | FORBIDDEN |
| Local service startup | FORBIDDEN |
| Source document copy/import or document body read | FORBIDDEN |
| Extraction outputs, public-sync, schema/writer/adapter/checker implementation | FORBIDDEN |
| Legal advice quality, current-law correctness, runtime smoke, workflow-chain completion, production readiness | FORBIDDEN |

## Execution Plan

1. Capture `executionBaseHead` and current worktree status.
2. Complete Required First Reads and worker-output checker-source read-ahead.
3. Recompute source facts from R22 and the pinned MinerU mirror.
4. Run read-only local metadata commands for R22 venv, R22 command path, R22/R23 config files, R22 cache log, partial cache evidence, and active MinerU/python cache-prep processes.
5. If the R22 venv or command is missing, stop with `BLOCKED_WITH_REASON`.
6. Set process-local `MINERU_MODEL_SOURCE=modelscope` and absolute `MINERU_TOOLS_CONFIG_JSON` pointing to `.cvf/runtime/msea-r23-mineru.json`.
7. Run exactly one ModelScope pipeline cache resume/retry command if no active prior cache-prep process exists.
8. Record secret-safe before/after config/cache metadata, command exit status, elapsed time, timeout class if any, and retryability.
9. Select exactly one route token.
10. Author the worker return and companion readiness matrix.
11. Run worker-return fast gate and pre-implementation autorun.
12. Leave governed changes uncommitted and return the status token.

## Allowed Command Sequence

Worker may run only the following cache mutation command, plus read-only metadata and gate commands:

```powershell
$env:MINERU_MODEL_SOURCE='modelscope'
$env:MINERU_TOOLS_CONFIG_JSON=(Resolve-Path '.cvf\runtime').Path + '\msea-r23-mineru.json'
.\.cvf\runtime\msea-r22-mineru-venv\Scripts\mineru-models-download.exe --source modelscope --model_type pipeline
```

If an executable has a `.cmd` or script suffix instead of `.exe`, worker may use the equivalent file inside the same R22 venv scripts directory and must record the exact path. Worker must stop before parser or service execution even if cache preparation succeeds. Worker must not run a second retry in the same tranche.

## Live Run Diagnostic Discipline

The retry command is a local model-cache prerequisite command, not CVF provider/live governance proof. If it fails, times out, produces empty output, or needs a rerun, the worker must classify the failure before any further action with stage, class, retryability, user action, command path, elapsed time, safe message, and whether config/cache evidence changed. Repeating the same unclear command is forbidden in R23.

## Route Tokens

Worker must select exactly one:

| Route token | Meaning |
| --- | --- |
| OPEN_MSEA_R24_LOCAL_PIPELINE_RUNTIME_SMOKE_WORK_ORDER | R23 cache retry completed with sufficient config/cache receipt to author a later parser smoke work order; worker still must not run parser smoke |
| HOLD_PENDING_MODELSCOPE_RETRY_OR_NETWORK_DIAGNOSTIC | retry failed, timed out, or remained incomplete, and diagnostic is recorded |
| OPEN_ALTERNATE_MODEL_SOURCE_DECISION_WORK_ORDER | ModelScope remains too slow or unstable and a future HuggingFace/local-source decision should be evaluated through fresh source-verified dispatch |
| HOLD_PENDING_CONFIG_WRITEBACK_REVIEW | command appears successful but config/cache receipt is ambiguous |
| HOLD_ALL_MINERU_RUNTIME_LANES | operator or environment blocks further package/cache work |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intakeType | local cache diagnostic resolution using accepted R22 timeout evidence |
| selected role route | SINGLE_AGENT_MULTI_ROLE route mode for one local agent performing dispatch, worker, reviewer/closer, and session-sync roles in separate phases |
| workerRole | delegated worker performs allowed local metadata checks and one cache retry command, then writes uncommitted outputs |
| reviewerRole | reviewer/closer reviews worker outputs and owns material commit if accepted |
| escalation condition | operator checkpoint required if retry requires broader scope than the allowed command sequence, if alternate source must be executed, or if parser/document/runtime execution is requested |
| claimBoundary | role routing only; no parser/runtime/public/provider/live/production claim |

## Single-Agent Multi-Role Control Block

| Field | Value |
| --- | --- |
| routeToken | SINGLE_AGENT_MULTI_ROLE |
| role route | single local agent may perform multiple roles only with separated dispatch, worker, reviewer/closer, and session-sync evidence |
| dispatchRole | dispatcher authored baseline and work order before worker execution |
| workerRole | worker must capture executionBaseHead, execute only allowed commands, create only named outputs, and not commit |
| reviewerCloserRole | reviewer/closer may repair allowed-scope evidence shape and commit material if accepted |
| sessionSyncRole | session-sync steward updates protected session surfaces only after material commit |
| cleanWorktreeRequirement | Before status evidence must record clean worktree at worker start |
| escalation conditions | operator escalation for alternate source execution, parser/service/document-body action, public-sync, or production/workflow-chain claim |
| evidence basis independent of memory | source verification rows, command receipts, git diff/status, and governance gates; provider memory and chat are not CVF authority |
| gate sequence | pre-dispatch before dispatch commit; pre-implementation after worker output; reviewer-fast/steward before material commit; session-sync steward before protected state commit |
| role separation ledger | dispatcher writes packet; worker writes uncommitted outputs; reviewer/closer commits material; session-sync steward updates protected session files |
| self-review boundary | single-agent multi-role does not claim independent review; allowed-scope repairs are evidence-based and gate-checked |
| crossBatchIsolation | MSEA-R23-T1 only; no parser smoke or public/runtime expansion |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_DECISION_WORKER_RETURN_2026-07-03.md` | CREATE with command receipts, route token, gates, no-commit evidence |
| `docs/reference/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_READINESS_MATRIX_2026-07-03.md` | CREATE with cache/config readiness matrix and next-route decision |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_DECISION_WORKER_RETURN_2026-07-03.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section names without the heading prefix. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under reviews | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| companion reference under reference | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

Literal-shape reminders: do not list required headings as backticked heading strings before the real section; write source-not-found disposition spelling instead of the exact blocked enum in literalTokensReviewed; avoid broad dependency-placeholder wording unless the row cites the accepted artifact path and commit.

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| Base and worktree status | `executionBaseHead`, `git status --short`, and actual changed file list |
| Source verification | Source Inventory plus Source Verification Block in worker outputs |
| R22 diagnostic carry-forward | accepted R22 selected route, venv command status, timeout/config/cache evidence |
| Active process safety | process check before retry; stop if an existing cache-prep process is active |
| Allowed retry command | exact command, exit code, elapsed time, stdout/stderr summary, and timeout/failure classification |
| R23 config write-back | secret-safe before/after metadata for `.cvf/runtime/msea-r23-mineru.json`; no raw secrets printed |
| Cache evidence | model path/cache root evidence only if created or reported by the command; no model files committed |
| Runtime non-execution | explicit statement that no parser/OCR/VLM/API/router/Gradio/Docker/WSL/service/document-body action occurred |
| Route decision | exactly one `selectedRouteToken` in both worker return and companion matrix |
| Gates | worker-return fast gate and pre-implementation autorun output |

## Acceptance Criteria

| Criterion | Acceptance evidence |
| --- | --- |
| R22 diagnostic classified | worker return records R22 selected route, timeout, config absence, and partial cache evidence |
| R22 venv and command availability classified | worker return records command path or blocker |
| Retry command classified | worker return records exact command, result, elapsed time, and diagnostic class if failed |
| Config/cache evidence classified | readiness matrix records before/after config metadata and cache completion or blocker |
| Forbidden scope preserved | worker return explicitly states no parser/runtime/document-body/public/production action occurred |
| Gates pass | worker-return fast gate and pre-implementation autorun pass before reviewer acceptance |

## Review Gate

Reviewer/closer must run:

```powershell
python governance\compat\run_worker_return_fast_gate.py
python governance\compat\run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce
python governance\compat\run_local_governance_hook_chain.py --hook pre-commit --parallel
```

Reviewer may repair only allowed-scope evidence or literal-shape defects inside the named worker outputs. Any broader runtime, parser, package distribution, source import, public-sync, alternate source execution, or production request returns to operator.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Worker commit mode honored | PASS or BLOCKED with reason |
| Material changed set limited to named outputs | PASS or BLOCKED with reason |
| Ignored local runtime side effects recorded | PASS or BLOCKED with reason |
| No forbidden parser/document/public action | PASS or BLOCKED with reason |
| Session-sync surfaces updated after material commit | PASS or BLOCKED with reason |

## Operator Checkpoint

Operator checkpoint is required before any of the following: reinstalling outside the R22 venv, using HuggingFace/local/other source for a real download, downloading VLM or all model families, running parser/OCR/VLM/API/router/Gradio/Docker/WSL/service commands, reading any private document body, committing generated extraction outputs, or claiming runtime-smoke/production/workflow-chain readiness.

## Verification Commands

```powershell
python governance\compat\run_worker_return_fast_gate.py
python governance\compat\run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance\compat\run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce
git status --short
```

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | dispatcher authors packet; worker executes without commit; reviewer/closer accepts material; session-sync steward updates front door and state after material commit |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=d0d4f120; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch may add paired baseline/work order only; worker may add the two named output artifacts and ignored local runtime side effects only; reviewer may commit material outputs; session-sync steward updates only session surfaces |
| traceScope(phase, actor) | each role records Agent Operation Trace Block in its owned artifact or handoff/session-sync surface |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit; session-sync steward owns protected session commit |
| crossBatchIsolation | MSEA-R23-T1 only; no parser smoke, source document processing, public-sync, alternate source execution, schema/writer/adapter/checker implementation, or production chain |
| nextMoveSurfaces | session-sync steward updates `CVF_SESSION_MEMORY.md`, generated active session state, and active handoff only after material acceptance |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_DECISION_COMPLETION_2026-07-03.md` (optional; prefer repairing evidence in the worker return per literal-format gotcha 30) |
| reviewerOwnedClosurePaths | worker return and companion readiness matrix if accepted; no optional completion review unless worker return cannot carry reviewer decision |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R23 cache diagnostic resolution dispatch only |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: dispatch packet plus later worker return command receipts only; no Delta runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: cache retry command is allowed only as a local prerequisite action; no CVF action-authority claim |
| invocationBoundary | Manual local worker invocation inside this repository and ignored local runtime paths |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | local cache prerequisite evidence only, not runtime governance behavior |
| forbiddenExpansion | Do not expand into parser/runtime/provider/live/public/package distribution/Web/MCP/model-router/action-authority behavior without fresh source-verified authorization |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R23 is private local cache diagnostic work with ignored runtime side effects and no public-sync export.

## Claim Boundary

This work order authorizes only R22 diagnostic inspection, reuse of the ignored R22 venv, R23 config/log metadata, one ModelScope pipeline cache resume/retry command, and two governed worker output artifacts. It does not authorize package reinstall outside the R22 venv, alternate-source download execution, parser/OCR/VLM/hybrid/API/router/Gradio/Docker/WSL execution, local service startup, document body read, extraction outputs, source document import, public-sync, schema/writer/adapter/checker implementation, provider/live proof, legal advice quality, current-law correctness, benchmark, runtime smoke, workflow-chain completion, or production readiness.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R23-T1 dispatch authoring, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, `Get-Content`, `build_dispatch_packet_scaffold.py`, `apply_patch`, pre-dispatch gates |
| Target paths | paired R23 baseline and work order |
| Allowed scope source | operator continued using accepted MSEA-R22-T1 material commit `7b105700`; dispatch base `d0d4f120` |
| Before status evidence | clean worktree: `git rev-parse --short HEAD` returned `d0d4f120`; `git status --short` was empty before authoring |
| After status evidence | paired R23 baseline and work order are uncommitted pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only; worker execution follows after dispatch commit |
| Claim boundary | source-verified cache diagnostic resolution dispatch only; no parser/runtime/public/provider/live/production claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r23-t1-dispatch-authoring-2026-07-03` |
| Expected manifest | R23 baseline and work order |
| Actual changed set | R23 baseline and work order |
| Manifest delta | MATCH |
