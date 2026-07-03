# CVF GC-018 Baseline - MSEA-R22-T1 MinerU Package Install Activation And ModelScope Pipeline Cache Preparation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R22_T1

Dispatch base head: 242927cc

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Purpose

Authorize the next bounded MinerU prerequisite step after MSEA-R21-T1 selected `HOLD_PENDING_MINERU_PACKAGE_INSTALL_AUTHORIZATION`: create an ignored local runtime virtual environment, install/activate MinerU from the pinned source mirror only for local private testing, and attempt ModelScope pipeline cache preparation. This baseline does not authorize parser execution, document-body reads, extraction outputs, public-sync, legal-quality evaluation, or production/workflow-chain claims.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R22-T1 --title "MinerU Package Install Activation And ModelScope Pipeline Cache Preparation" --date 2026-07-03 --base 242927cc --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed scaffold fields, set DISPATCH_READY, added R21 dependency release, source-verified install/cache/config facts, bounded local runtime mutation envelope, worker output manifest, route tokens, and pre-dispatch gate plan. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py`. |
| docOnlyNewFields | selectedRouteToken; packageInstallDisposition; activationCommandStatus; modelCachePrepDisposition; configWritebackReceipt; runtimeSmokeGateDisposition; localRuntimeMutationEnvelope |
| claimBoundary | Dispatch authoring provenance only; no parser/OCR/VLM/API/Docker/service/provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | Source facts are recomputed from CVF surfaces and the pinned mirror; provider-local authority is excluded; worker output checker read-ahead is mandatory; package install is allowed only inside the local ignored runtime envelope. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; ADIF resolver query exactness; Dependency Release Evidence; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields; Worker Return Packet Shape Contract fields; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; Delta block field labels; Agent Operation Trace labels; source-not-found disposition spelling; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this baseline and paired work order only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition |
| --- | --- | --- | --- |
| MSEA-R21-T1 accepted package-install blocker | `docs/reviews/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_READINESS_MATRIX_2026-07-03.md` | `c859ffb1` | SATISFIED - selected `HOLD_PENDING_MINERU_PACKAGE_INSTALL_AUTHORIZATION` after local CLI was missing |
| Session next-move freshness | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V34_2026-07-03.md` | `242927cc` | SATISFIED - next allowed move permits fresh MSEA-R22 package install/activation authorization if operator proceeds |
| Operator authorization | current operator instruction in this session | N/A | SATISFIED - operator agreed to process the full R22 path proposed after R21 |

## Decision / Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Decision | OPEN_MSEA_R22_T1_LOCAL_PACKAGE_INSTALL_AND_CACHE_PREP |
| Baseline | R21 proved the source route exists but local CLI activation is missing; R22 opens only the package/install prerequisite step. |
| Proposed tranche | Create a local ignored venv, install MinerU from the pinned mirror, redirect config to `.cvf/runtime`, and attempt ModelScope pipeline cache preparation. |
| Stop condition | Any need for parser execution, document body read, source document import, public-sync, or production/workflow-chain claim stops the tranche. |

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MinerU source mirror is the current upstream authority for this lane. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | line 35 | `opendatalab__MinerU` | source mirror index | ACCEPT |
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
| MinerU install/cache facts | `docs/reference/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_READINESS_MATRIX_2026-07-03.md` and this R22 baseline | ENRICH_EXISTING | R22 narrows the R21 blocker into a local package activation prerequisite lane. | ADAPT |
| MinerU source mirror package metadata | `.private_reference/source_mirrors/INDEX.md` plus R22 Source Verification Block | CONFIRMED_EXISTING | Source mirror authority already exists and is reused without source import. | NO_NEW_OWNER |
| Local ignored runtime envelope | `docs/baselines/CVF_GC018_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_2026-07-03.md` | NEW_FINDING | The concrete ignored local venv/config boundary is new to R22. | ABSORB_AS_BOUNDARY |
| Parser/runtime smoke | OWNER_SURFACE_NOT_FOUND | REJECT_DIRECT_IMPORT | Runtime extraction remains outside R22. | DEFER |

## Evidence / Verification

| Evidence class | Required evidence |
| --- | --- |
| Source verification | R22 Source Verification Block rows must cite current CVF surfaces or pinned MinerU mirror paths. |
| Dispatch gates | Pre-dispatch autorun and dispatch steward must pass before worker execution. |
| Worker evidence | Worker return must record package install, command activation, config/cache receipt, selected route, and no-parser boundary. |
| Claim boundary | No runtime parser, document extraction, public-sync, legal-quality, workflow-chain, or production claim may be inferred from package/cache prep. |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R22 artifact path check | `Test-Path` for planned baseline, work order, worker return, and companion reference returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| R22 token search | `rg -n "MSEA_R22_T1|MSEA-R22-T1|MINERU_PACKAGE_INSTALL_ACTIVATION|Package Install Activation And ModelScope Pipeline Cache" docs CVF_SESSION AGENT_HANDOFF_V34_2026-07-03.md .private_reference\source_mirrors\INDEX.md` returned no matches before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | MSEA-R22-T1 is a new child tranche released by accepted MSEA-R21-T1 and operator authorization | SAFE_TO_CREATE |

## Local Runtime Mutation Envelope

| Surface | Authorized disposition |
| --- | --- |
| `.cvf/runtime/msea-r22-mineru-venv/` | CREATE_OR_REUSE_LOCAL_IGNORED_RUNTIME_VENV |
| `.cvf/runtime/msea-r22-mineru.json` | CREATE_OR_UPDATE_LOCAL_IGNORED_MINERU_CONFIG |
| package install source | pinned mirror `.private_reference/source_mirrors/opendatalab__MinerU` only |
| package dependency install | allowed only inside the R22 virtual environment |
| model cache | allowed only as created by `mineru-models-download --source modelscope --model_type pipeline`; no model files may be committed |
| repo material paths | dispatch artifacts and later worker return/reference only |

## Claim Boundary

This baseline authorizes only local package install/activation and ModelScope pipeline cache-preparation prerequisites for a later runtime smoke tranche. It does not authorize parser/OCR/VLM/hybrid/API/router/Gradio/Docker/WSL execution, local service startup, document body read, extraction outputs, source document import, public-sync, schema/writer/adapter/checker implementation, provider/live proof, legal advice quality, current-law correctness, benchmark, workflow-chain completion, or production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R22 concerns private local package/cache preparation and contains no public-sync export.
