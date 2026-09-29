# CVF GC-018 Baseline - MSEA-R23-T1 MinerU ModelScope Cache Diagnostic Resolution And Alternate Source Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R23_T1

Dispatch base head: d0d4f120

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Purpose

Authorize the next bounded MinerU prerequisite step after MSEA-R22-T1 selected
`HOLD_PENDING_MODELSCOPE_DOWNLOAD_DIAGNOSTIC`: inspect the R22 timeout evidence,
reuse the ignored R22 venv only if present, and perform one diagnostic-aware
ModelScope pipeline cache resume/retry with a separate R23 config receipt. This
baseline does not authorize parser execution, document-body reads, extraction
outputs, public-sync, legal-quality evaluation, runtime smoke, workflow-chain
completion, or production claims.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R23-T1 --title "MinerU ModelScope Cache Diagnostic Resolution And Alternate Source Decision" --date 2026-07-03 --base d0d4f120 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed scaffold fields, set DISPATCH_READY, added R22 dependency release, source-verified ModelScope/config/cache facts, bounded retry envelope, worker-output shape mandate, route tokens, and pre-dispatch gate plan. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; and worker-output checker token summaries for worker-return, structural, Delta, external-intake, rescan, corpus, finding, and epistemic gates. |
| docOnlyNewFields | selectedRouteToken; retryCommandDisposition; r22DiagnosticCarryForward; r23ConfigWritebackReceipt; modelCacheCompletionReceipt; alternateSourceDecision; runtimeSmokeGateDisposition |
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
| Dispatch impact | R23 source facts are recomputed from CVF-governed surfaces and the pinned mirror; provider-local authority is excluded; worker output checker read-ahead is mandatory; cache retry remains isolated to ignored local runtime and user cache metadata. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; ADIF resolver query exactness; Dependency Release Evidence; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields; Worker Return Packet Shape Contract fields; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; Delta block field labels; Agent Operation Trace labels; source-not-found disposition spelling; worker output section names Target / Source, Scope / Methodology, Findings / Position, Risk / Corrective Action, External Knowledge Intake Routing, Rescan Intelligence Hardening, Corpus Completeness And Report Integrity, Finding-To-Governance Learning Disposition, and Epistemic Process Block. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this baseline and paired work order only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition |
| --- | --- | --- | --- |
| MSEA-R22-T1 accepted ModelScope download diagnostic | `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | `7b105700` | SATISFIED - selected `HOLD_PENDING_MODELSCOPE_DOWNLOAD_DIAGNOSTIC` after package activation succeeded but cache prep timed out |
| Session next-move freshness | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V34_2026-07-03.md` | `d0d4f120` | SATISFIED - next allowed move permits fresh R23 cache resume/retry or alternate-source authoring |
| Operator authorization | current operator instruction in this session | N/A | SATISFIED - operator said to continue using R22 material commit `7b105700` and prior proposal |

## Decision / Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Decision | OPEN_MSEA_R23_T1_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION |
| Baseline | R22 proved the local package and venv command exist, but the ModelScope pipeline cache-prep command timed out and no R22 config file was written. |
| Proposed tranche | Inspect R22 logs/cache/config metadata, then run exactly one resume/retry of `mineru-models-download --source modelscope --model_type pipeline` from the R22 venv with R23 config redirection. |
| Stop condition | Any need for parser execution, document body read, source document import, public-sync, alternate model-source command execution, or production/workflow-chain claim stops the tranche. |

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MinerU source mirror is the current upstream authority for this lane. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | line 35 | `opendatalab__MinerU` | source mirror index | ACCEPT |
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
| MinerU ModelScope/config facts | `.private_reference/source_mirrors/opendatalab__MinerU/`; `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | Current source facts remain in upstream mirror. | NO_NEW_OWNER |
| R23 config receipt | `docs/baselines/CVF_GC018_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_DECISION_2026-07-03.md` | NEW_FINDING | R23 uses `.cvf/runtime/msea-r23-mineru.json` to avoid overwriting R22 evidence. | ABSORB_AS_BOUNDARY |
| Parser/runtime smoke | `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json` | REJECT_DIRECT_IMPORT | Cache completion can only open a later work order; it does not execute runtime smoke. | DEFER |
| Alternate model source | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | R23 may recommend an alternate-source decision but may not execute alternate source commands. | DEFER |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | Pinned MinerU source mirror is used as the external upstream input for a governed local cache diagnostic dispatch. |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline and the paired R23 work order |
| Disposition | ROUTED_TO_GOVERNED_DISPATCH_WITH_LOCAL_RUNTIME_DIAGNOSTIC |
| Claim boundary | Source mirror evidence supports only this cache diagnostic dispatch; no source import, parser runtime, public-sync, or production claim. |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_WORKER_RETURN_2026-07-03.md`
- Predecessor intake artifact: `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md`
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS
- Routing matrix status: COMPLETE_WITH_DELTA_ROUTING_SAMPLE
- Semantic sampling status: COMPLETE_WITH_DELTA_ROUTING_SAMPLE
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Source claim | R23 check | Disposition |
| --- | --- | --- | --- |
| UNCHANGED_FROM_INTAKE | R22 selected ModelScope as the cache-prep route. | R23 keeps ModelScope for one bounded retry. | retained |
| CHANGED_DISPOSITION | R22 held on timeout and absent config. | R23 authorizes one retry with separate config receipt. | changed to retry decision |
| NEW_FINDING | R23 uses a new config path to separate retry evidence. | `.cvf/runtime/msea-r23-mineru.json` is the planned receipt path. | new boundary |
| REMOVED_OR_REJECTED | Runtime smoke can follow immediately from R22. | R23 still blocks parser runtime until cache/config evidence completes. | rejected |

### Follow-Up Routing Matrix

| Routing lane | Candidate | Disposition |
| --- | --- | --- |
| DO_NOW | worker performs R22 metadata check and one ModelScope retry | allowed |
| SEPARATE_RUNTIME_TRANCHE | parser smoke after completed cache/config receipt | held |
| STRATEGIC_OPERATOR_DECISION | alternate source if ModelScope remains too slow | possible |
| OUT_OF_SCOPE | parser runtime, public-sync, legal quality, production chain | rejected |
| RESOLVED_BY_DESIGN | no document body read in cache diagnostic work | resolved |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| R23-B1 | R22 readiness matrix | package activation succeeded but cache did not complete | retry only | Could R23 jump directly to runtime smoke? | NO; runtime smoke needs a later work order |
| R23-B2 | MinerU model-source docs | completed downloads write config | config receipt | Could an incomplete cache file count as readiness? | NO; config/cache receipt is required |
| R23-B3 | R23 claim boundary | alternate source may be recommended only | alternate-source decision | Could worker run a HuggingFace command now? | NO; alternate-source execution is forbidden |

## Evidence / Verification

| Evidence class | Required evidence |
| --- | --- |
| Source verification | R23 Source Verification Block rows cite current CVF surfaces or pinned MinerU mirror paths. |
| Dispatch gates | Pre-dispatch autorun and dispatch steward must pass before worker execution. |
| Worker evidence | Worker return must record R22 diagnostic carry-forward, process check, config/cache metadata, exactly one retry command if prerequisites hold, route token, and no-parser boundary. |
| Claim boundary | No runtime parser, document extraction, public-sync, legal-quality, workflow-chain, production, or runtime smoke claim may be inferred from cache retry. |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R23 artifact path check | `Test-Path` for planned baseline, work order, worker return, and companion reference returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| R23 token search | `rg -n "MSEA_R23_T1|MSEA-R23-T1|MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION|ModelScope Cache Diagnostic Resolution And Alternate Source Decision" docs CVF_SESSION AGENT_HANDOFF_V34_2026-07-03.md .private_reference\source_mirrors\INDEX.md` returned no matches before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | MSEA-R23-T1 is a new child tranche released by accepted MSEA-R22-T1 and operator authorization | SAFE_TO_CREATE |

## Local Runtime Mutation Envelope

| Surface | Authorized disposition |
| --- | --- |
| `.cvf/runtime/msea-r22-mineru-venv/` | READ_OR_REUSE_LOCAL_IGNORED_RUNTIME_VENV |
| `.cvf/runtime/msea-r23-mineru.json` | CREATE_OR_UPDATE_LOCAL_IGNORED_MINERU_CONFIG |
| `.cvf/runtime/msea-r23-cache-resume.log` | CREATE_OR_UPDATE_LOCAL_IGNORED_DIAGNOSTIC_LOG |
| package install source | no reinstall authorized unless the R22 venv is missing or unusable; if missing, worker returns `BLOCKED_WITH_REASON` |
| model cache | allowed only as created or resumed by `mineru-models-download --source modelscope --model_type pipeline`; no model files may be committed |
| repo material paths | dispatch artifacts and later worker return/reference only |

## Claim Boundary

This baseline authorizes only R22 diagnostic inspection, one ModelScope pipeline
cache resume/retry using the R22 venv, R23 config/log metadata, and two governed
worker output artifacts. It does not authorize package reinstall outside the
R22 venv, parser/OCR/VLM/hybrid/API/router/Gradio/Docker/WSL execution, local
service startup, document body read, extraction outputs, source document import,
public-sync, schema/writer/adapter/checker implementation, provider/live proof,
legal advice quality, current-law correctness, benchmark, runtime smoke,
workflow-chain completion, or production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R23 concerns private local cache diagnostics with ignored runtime side
effects and contains no public-sync export.
