# CVF Agent Work Order - MSEA-R22-T1 MinerU Package Install Activation And ModelScope Pipeline Cache Preparation

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R22_T1

Dispatch base head: 242927cc

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R22_T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker must capture `git rev-parse --short HEAD` before edits.

Current-time notes: artifact date is 2026-07-03; use current repository state, pinned MinerU source mirror, and the operator's authorization to open the R22 package install/activation prerequisite step.

Do-not-misread notes: this packet authorizes only ignored local runtime venv creation/reuse, MinerU install from the pinned source mirror, local config redirection, and ModelScope pipeline cache preparation. It does not authorize parser/OCR/VLM/API/router/Gradio/Docker/WSL execution, local service startup, document body read, extraction outputs, public-sync, schema/writer/adapter/checker implementation, legal advice, current-law, production, or workflow-chain claims.

Required first actions: read startup files, guard orientation, literal gotchas, this work order, the paired GC-018 baseline, source references, and checker source listed in the Checker Source Read-Ahead Block before writing worker outputs.

Return contract: create the worker return and companion readiness matrix, run required gates, leave governed changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute the bounded R22 prerequisite lane: create or reuse a local ignored MinerU virtual environment, install/activate MinerU from the pinned source mirror with pipeline support, verify `mineru-models-download`, redirect MinerU config to `.cvf/runtime/msea-r22-mineru.json`, and attempt ModelScope pipeline model cache preparation. Success means the worker can classify package install, command activation, config writeback, and cache-prep readiness without running any document parser.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R22-T1 --title "MinerU Package Install Activation And ModelScope Pipeline Cache Preparation" --date 2026-07-03 --base 242927cc --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed scaffold fields, set DISPATCH_READY, added R21 dependency release, source-verified install/cache/config facts, local runtime mutation envelope, worker-output shape mandate, route tokens, and allowed command sequence. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py`. |
| docOnlyNewFields | selectedRouteToken; packageInstallDisposition; activationCommandStatus; modelCachePrepDisposition; configWritebackReceipt; runtimeSmokeGateDisposition; localRuntimeMutationEnvelope |
| claimBoundary | Dispatch authoring provenance only; no parser/OCR/VLM/API/Docker/service/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the literal required shape. Worker should return to orchestrator only for a source contradiction, missing MinerU source mirror, package install failure that cannot be classified safely, failed network or download diagnostic that cannot be classified safely, forbidden-scope need, or missing authority that makes completion impossible.

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition |
| --- | --- | --- | --- |
| MSEA-R21-T1 accepted package-install blocker | `docs/reviews/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_READINESS_MATRIX_2026-07-03.md` | `c859ffb1` | SATISFIED - selected `HOLD_PENDING_MINERU_PACKAGE_INSTALL_AUTHORIZATION` after local CLI was missing |
| Session next-move freshness | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V34_2026-07-03.md` | `242927cc` | SATISFIED - next allowed move permits fresh MSEA-R22 package install/activation authorization if operator proceeds |
| Operator authorization | current operator instruction in this session | N/A | SATISFIED - operator agreed to process the full R22 path proposed after R21 |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | Worker output checker read-ahead is mandatory; provider-local authority is excluded; package install remains isolated to ignored local runtime paths; ModelScope cache preparation is not parser runtime readiness. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; ADIF resolver query exactness; Dependency Release Evidence; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields; Worker Return Packet Shape Contract fields; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; Delta block field labels; Agent Operation Trace labels. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm this work order's dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this work order and paired baseline only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R22-T1 must re-read current CVF-governed sources, accepted R21 artifacts, pinned MinerU source mirror docs/source, and local environment metadata before running install/cache commands.

unicodePathHandling: Use LiteralPath and UTF-8-safe command output for local paths; do not normalize or rewrite filenames.

extractedTextAuthority: N/A with reason

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reference/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_READINESS_MATRIX_2026-07-03.md` |
| priorVerificationAnchor | `selectedRouteToken: HOLD_PENDING_MINERU_PACKAGE_INSTALL_AUTHORIZATION` |
| recomputeReason | R22-T1 must re-read current CVF-governed sources, accepted R21 artifacts, pinned MinerU source mirror docs/source, and local environment metadata before running install/cache commands |
| freshRecomputeRequired | true for source facts, Python/uv/pip availability, venv status, package install, command activation, config evidence, cache evidence, and diagnostics; no document body read and no parser extraction |
| unicodePathHandling | Use `-LiteralPath` and UTF-8-safe command output for local paths; do not normalize or rewrite filenames |
| extractedTextAuthority | N/A with reason |

## Operator Authorization And Privacy Boundary

The operator authorized this R22 package install/activation and ModelScope cache-prep prerequisite lane for local private CVF testing only. Candidate Group A source documents remain private and must not be public-synced or redistributed. This tranche may create metadata/redacted evidence about local package/cache preparation but must not copy source documents into the repository, read source document body content, create parser outputs, or include sensitive personal/legal details in committed artifacts.

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MinerU source mirror remains the current upstream authority for this lane. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | line 35 | `opendatalab__MinerU` | source mirror index | ACCEPT |
| R21 selected a package-install authorization blocker. | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_READINESS_MATRIX_2026-07-03.md` | selectedRouteToken line | `HOLD_PENDING_MINERU_PACKAGE_INSTALL_AUTHORIZATION` | R21 readiness matrix | ACCEPT |
| MinerU supports source-code installation using uv editable install. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/quick_start/index.md` | lines 115-120 | `uv pip install -e .[all]` | quick start install docs | ACCEPT |
| MinerU project requires Python 3.10 through below 3.14. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | line 12 | `requires-python` | project metadata | ACCEPT |
| MinerU project exposes pipeline optional dependencies. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | lines 93-103 | `pipeline` | project optional dependencies | ACCEPT |
| MinerU project exposes `mineru-models-download` as a console script. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | line 133 | `mineru-models-download` | project scripts | ACCEPT |
| MinerU model-source docs support ModelScope and environment control. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | lines 11-23 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| MinerU model download writes model path and source to config after completion. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | lines 35-49 | `mineru-models-download` | model source documentation | ACCEPT |
| MinerU download CLI supports source and model-type options. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 93-117 | `download_models` | model download CLI | ACCEPT |
| MinerU pipeline model download enumerates pipeline model paths and writes configuration. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 21-52 | `download_pipeline_models` | model download CLI | ACCEPT |
| MinerU config path can be redirected by `MINERU_TOOLS_CONFIG_JSON`. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 23-28 | `get_tools_config_file_path` | config path helper | ACCEPT |
| MinerU ModelScope download uses ModelScope snapshot download and persists config. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 253-275 | `_snapshot_download_cached` | model download utility | ACCEPT |
| Pipeline cache root resolution checks existing config before new download. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 279-324 | `auto_download_and_get_model_root_path` | model download utility | ACCEPT |
| Local `.cvf/runtime` is ignored and suitable for untracked runtime artifacts. | VALUE_SET | VALUE_SET | `.gitignore` | lines 49-52 | `.cvf/runtime/` | repository ignore policy | ACCEPT |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| MinerU install/cache facts | `docs/reference/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_READINESS_MATRIX_2026-07-03.md` and this R22 work order | ENRICH_EXISTING | R22 converts the R21 package-install blocker into a concrete prerequisite execution lane. | ADAPT |
| MinerU source mirror package metadata | `.private_reference/source_mirrors/INDEX.md` plus R22 Source Verification Block | CONFIRMED_EXISTING | Source mirror authority already exists and is reused without source import. | NO_NEW_OWNER |
| Local ignored runtime envelope | `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_2026-07-03.md` | NEW_FINDING | The venv/config side-effect boundary is new and specific to R22. | ABSORB_AS_BOUNDARY |
| Parser/runtime smoke | OWNER_SURFACE_NOT_FOUND | REJECT_DIRECT_IMPORT | Runtime extraction remains outside R22. | DEFER |

## New Doc-Only Fields

| Field | Meaning | Disposition |
| --- | --- | --- |
| selectedRouteToken | Worker-selected next route for reviewer/closer consideration | DOC_ONLY_NEW |
| packageInstallDisposition | Worker classification of venv creation and package install result | DOC_ONLY_NEW |
| activationCommandStatus | Worker classification of `mineru-models-download` availability inside the venv | DOC_ONLY_NEW |
| modelCachePrepDisposition | Worker classification of command result, cache/config evidence, or blocker | DOC_ONLY_NEW |
| configWritebackReceipt | Secret-safe before/after config metadata and JSON key summary | DOC_ONLY_NEW |
| runtimeSmokeGateDisposition | Whether a later parser smoke work order can be authored | DOC_ONLY_NEW |
| localRuntimeMutationEnvelope | Records allowed ignored local side-effect paths | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R22 artifact path check | `Test-Path` for planned baseline, work order, worker return, and companion reference returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| R22 token search | `rg -n "MSEA_R22_T1|MSEA-R22-T1|MINERU_PACKAGE_INSTALL_ACTIVATION|Package Install Activation And ModelScope Pipeline Cache" docs CVF_SESSION AGENT_HANDOFF_V34_2026-07-03.md .private_reference\source_mirrors\INDEX.md` returned no matches before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | MSEA-R22-T1 is a new child tranche released by accepted MSEA-R21-T1 and operator authorization | SAFE_TO_CREATE |

## Authority Chain

- Operator instruction: agreed to process the proposed R22 package install/activation and ModelScope cache-prep prerequisite lane.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V34_2026-07-03.md`.
- Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_2026-07-03.md`.
- Accepted R21 blocker and readiness matrix.
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
| Operator | operator | owns package-install, parser-runtime, document-body, public-sync, and production decisions |
| Dispatcher | dispatcher role | authors this GC-018/work order and runs pre-dispatch gates |
| Worker | delegated worker role | executes allowed local package/cache commands and creates only the named worker return and companion readiness matrix, without commit |
| Reviewer/closer | reviewer/closer | reviews returned artifacts, repairs allowed-scope shape defects if needed, commits material if accepted |
| Session-sync steward | reviewer/closer once material is accepted | updates active session state once accepted material exists |

## Pre-Flight Checks

Required before worker execution:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path 'docs\reviews\CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md'
Test-Path 'docs\reference\CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected result: clean worktree at execution start, planned worker outputs absent before writing, and pre-implementation gate passing after worker output authoring and allowed-scope repairs.

## Write Ownership

| Path family | Worker permission |
| --- | --- |
| `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md` | CREATE_ONLY_UNCOMMITTED |
| `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | CREATE_ONLY_UNCOMMITTED |
| `.cvf/runtime/msea-r22-mineru-venv/` | CREATE_OR_REUSE_LOCAL_IGNORED_RUNTIME_VENV |
| `.cvf/runtime/msea-r22-mineru.json` | CREATE_OR_UPDATE_LOCAL_IGNORED_MINERU_CONFIG |
| model cache created or reused by the MinerU download command | LOCAL_SIDE_EFFECT_ALLOWED_UNTRACKED |
| session-state, front-door, and active-handoff surfaces | FORBIDDEN |
| `.private_reference/source_mirrors/**` | READ_ONLY source authority; install may reference the pinned mirror path but must not edit it |
| public-sync, Web, MCP, model-router, checker, adapter, schema/writer, runtime source implementation paths | FORBIDDEN |

## Allowed / Forbidden Scope

| Scope item | Disposition |
| --- | --- |
| Create/reuse R22 venv under `.cvf/runtime` | ALLOWED |
| Install MinerU from pinned source mirror inside the R22 venv | ALLOWED |
| Redirect MinerU config to `.cvf/runtime/msea-r22-mineru.json` | ALLOWED |
| Run one ModelScope pipeline cache-prep command | ALLOWED |
| Create the two named worker output artifacts | ALLOWED |
| Parser/OCR/VLM/API/router/Gradio/Docker/WSL execution | FORBIDDEN |
| Local service startup | FORBIDDEN |
| Source document copy/import or document body read | FORBIDDEN |
| Extraction outputs, public-sync, schema/writer/adapter/checker implementation | FORBIDDEN |
| Legal advice quality, current-law correctness, workflow-chain completion, production readiness | FORBIDDEN |

## Execution Plan

1. Capture `executionBaseHead` and current worktree status.
2. Complete Required First Reads and worker-output checker-source read-ahead.
3. Recompute source facts from R21 and the pinned MinerU mirror.
4. Run read-only local metadata commands to identify Python, uv, pip, current command availability, existing R22 venv/config status, and environment variables.
5. Create or reuse `.cvf/runtime/msea-r22-mineru-venv/`.
6. Install/activate MinerU from `.private_reference/source_mirrors/opendatalab__MinerU` with pipeline support inside the R22 venv.
7. Verify `mineru-models-download` inside the R22 venv.
8. Set process-local `MINERU_MODEL_SOURCE=modelscope` and absolute `MINERU_TOOLS_CONFIG_JSON` pointing to `.cvf/runtime/msea-r22-mineru.json`.
9. Run exactly one ModelScope pipeline cache-prep command if install and command activation succeeded.
10. Record secret-safe before/after config/cache metadata, command exit status, and diagnostic classification.
11. Author the worker return and companion readiness matrix.
12. Run worker-return fast gate and pre-implementation autorun.
13. Leave governed changes uncommitted and return the status token.

## Allowed Command Sequence

Worker may run only the following package/cache mutation commands, plus read-only metadata and gate commands:

```powershell
python -m venv .cvf\runtime\msea-r22-mineru-venv
.\.cvf\runtime\msea-r22-mineru-venv\Scripts\python.exe -m pip install --upgrade pip
.\.cvf\runtime\msea-r22-mineru-venv\Scripts\python.exe -m pip install -e ".private_reference\source_mirrors\opendatalab__MinerU[pipeline]"
$env:MINERU_MODEL_SOURCE='modelscope'
$env:MINERU_TOOLS_CONFIG_JSON=(Resolve-Path '.cvf\runtime').Path + '\msea-r22-mineru.json'
.\.cvf\runtime\msea-r22-mineru-venv\Scripts\mineru-models-download.exe --source modelscope --model_type pipeline
```

If an executable has a `.cmd` or script suffix instead of `.exe`, worker may use the equivalent file inside the same R22 venv scripts directory and must record the exact path. Worker must stop before parser or service execution even if cache preparation succeeds.

## Route Tokens

Worker must select exactly one:

| Route token | Meaning |
| --- | --- |
| OPEN_MSEA_R23_LOCAL_PIPELINE_RUNTIME_SMOKE_WORK_ORDER | package install/activation and ModelScope pipeline cache prep completed with sufficient receipt for a later parser smoke work order |
| HOLD_PENDING_PACKAGE_INSTALL_DIAGNOSTIC | venv/package install failed or dependency resolver failed and diagnostic is recorded |
| HOLD_PENDING_MODELSCOPE_DOWNLOAD_DIAGNOSTIC | package activation succeeded but ModelScope pipeline cache-prep command failed and diagnostic is recorded |
| HOLD_PENDING_CONFIG_WRITEBACK_REVIEW | download appears successful but config/cache receipt is ambiguous |
| HOLD_ALL_MINERU_RUNTIME_LANES | operator or environment blocks further package/cache work |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intakeType | local package/cache prerequisite after accepted R21 blocker |
| selected role route | SINGLE_AGENT_MULTI_ROLE route mode for one local agent performing dispatch, worker, reviewer/closer, and session-sync roles in separate phases |
| workerRole | delegated worker performs allowed local install/cache commands and writes uncommitted outputs |
| reviewerRole | reviewer/closer reviews worker outputs and owns material commit if accepted |
| escalation condition | operator checkpoint required if package/cache commands require broader scope than the allowed command sequence, if package install needs a different source, or if parser/document/runtime execution is requested |
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
| escalation conditions | operator escalation for broader install source, non-pipeline model family, parser/service/document-body action, public-sync, or production/workflow-chain claim |
| evidence basis independent of memory | source verification rows, command receipts, git diff/status, and governance gates; provider memory and chat are not CVF authority |
| gate sequence | pre-dispatch before dispatch commit; pre-implementation after worker output; reviewer-fast/steward before material commit; session-sync steward before protected state commit |
| role separation ledger | dispatcher writes packet; worker writes uncommitted outputs; reviewer/closer commits material; session-sync steward updates protected session files |
| self-review boundary | single-agent multi-role does not claim independent review; allowed-scope repairs are evidence-based and gate-checked |
| crossBatchIsolation | MSEA-R22-T1 only; no parser smoke or public/runtime expansion |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md` | CREATE with command receipts, route token, gates, no-commit evidence |
| `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | CREATE with install/cache/config readiness matrix and next-route decision |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md`
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
| Python/uv/pip environment | command output with versions and paths |
| Venv install | command, exit code, elapsed time, package version when available |
| Command activation | `Get-Command` or direct path evidence for venv-local `mineru-models-download` |
| Allowed cache-prep command | exact command and exit code for `--source modelscope --model_type pipeline` |
| Config write-back | secret-safe before/after metadata for `.cvf/runtime/msea-r22-mineru.json`; no raw secrets printed |
| Cache evidence | model path/cache root evidence only if created or reported by the command; no model files committed |
| Runtime non-execution | explicit statement that no parser/OCR/VLM/API/router/Gradio/Docker/WSL/service/document-body action occurred |
| Route decision | exactly one `selectedRouteToken` in both worker return and companion matrix |
| Gates | worker-return fast gate and pre-implementation autorun output |

## Acceptance Criteria

| Criterion | Acceptance evidence |
| --- | --- |
| Package install classified | worker return records command, exit code, and install disposition |
| CLI activation classified | worker return records venv-local `mineru-models-download` path or failure diagnostic |
| Cache-prep classified | worker return records selected route and ModelScope pipeline command result if run |
| Config evidence classified | readiness matrix records before/after config metadata or clear blocker |
| Forbidden scope preserved | worker return explicitly states no parser/runtime/document-body/public/production action occurred |
| Gates pass | worker-return fast gate and pre-implementation autorun pass before reviewer acceptance |

## Review Gate

Reviewer/closer must run:

```powershell
python governance\compat\run_worker_return_fast_gate.py
python governance\compat\run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce
python governance\compat\run_local_governance_hook_chain.py --hook pre-commit --parallel
```

Reviewer may repair only allowed-scope evidence or literal-shape defects inside the named worker outputs. Any broader runtime, parser, package distribution, source import, public-sync, or production request returns to operator.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Worker commit mode honored | PASS or BLOCKED with reason |
| Material changed set limited to named outputs | PASS or BLOCKED with reason |
| Ignored local runtime side effects recorded | PASS or BLOCKED with reason |
| No forbidden parser/document/public action | PASS or BLOCKED with reason |
| Session-sync surfaces updated after material commit | PASS or BLOCKED with reason |

## Operator Checkpoint

Operator checkpoint is required before any of the following: installing outside the R22 venv, using a different package source, downloading VLM or all model families, running parser/OCR/VLM/API/router/Gradio/Docker/WSL/service commands, reading any private document body, committing generated extraction outputs, or claiming production/workflow-chain readiness.

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
| baseHeadFor(phase) | dispatchBaseHead=242927cc; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch may add paired baseline/work order only; worker may add the two named output artifacts and ignored local runtime side effects only; reviewer may commit material outputs; session-sync steward updates only session surfaces |
| traceScope(phase, actor) | each role records Agent Operation Trace Block in its owned artifact or handoff/session-sync surface |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit; session-sync steward owns protected session commit |
| crossBatchIsolation | MSEA-R22-T1 only; no parser smoke, source document processing, public-sync, schema/writer/adapter/checker implementation, or production chain |
| nextMoveSurfaces | session-sync steward updates `CVF_SESSION_MEMORY.md`, generated active session state, and active handoff only after material acceptance |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_COMPLETION_2026-07-03.md` (optional; prefer repairing evidence in the worker return per literal-format gotcha 30) |
| reviewerOwnedClosurePaths | worker return and companion readiness matrix if accepted; no optional completion review unless worker return cannot carry reviewer decision |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R22 package/cache prerequisite dispatch only |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: dispatch packet plus later worker return command receipts only; no Delta runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: package/cache commands are allowed only as local prerequisite actions; no CVF action-authority claim |
| invocationBoundary | Manual local worker invocation inside this repository and ignored local runtime paths |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | local prerequisite evidence only, not runtime governance behavior |
| forbiddenExpansion | Do not expand into parser/runtime/provider/live/public/package distribution/Web/MCP/model-router/action-authority behavior without fresh source-verified authorization |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R22 is private local package/cache preparation with ignored runtime side effects and no public-sync export.

## Claim Boundary

This work order authorizes only local ignored venv creation/reuse, MinerU install/activation from the pinned mirror, local config redirection, ModelScope pipeline cache-prep attempt, and two governed worker output artifacts. It does not authorize parser/OCR/VLM/hybrid/API/router/Gradio/Docker/WSL execution, local service startup, document body read, extraction outputs, source document import, public-sync, schema/writer/adapter/checker implementation, provider/live proof, legal advice quality, current-law correctness, benchmark, workflow-chain completion, or production readiness.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R22-T1 dispatch authoring, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, `Get-Content`, `build_dispatch_packet_scaffold.py`, `apply_patch`, pre-dispatch gates |
| Target paths | paired R22 baseline and work order |
| Allowed scope source | operator approved R22 using accepted MSEA-R21-T1 material commit `c859ffb1`; dispatch base `242927cc` |
| Before status evidence | clean worktree: `git rev-parse --short HEAD` returned `242927cc`; `git status --short` was empty before authoring |
| After status evidence | paired R22 baseline and work order are uncommitted pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only; worker execution follows after dispatch commit |
| Claim boundary | source-verified package/cache prerequisite dispatch only; no parser/runtime/public/provider/live/production claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r22-t1-dispatch-authoring-2026-07-03` |
| Expected manifest | R22 baseline and work order |
| Actual changed set | R22 baseline and work order |
| Manifest delta | MATCH |
