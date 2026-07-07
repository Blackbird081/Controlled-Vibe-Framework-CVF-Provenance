# CVF GC-018 Baseline - MSEA-R20-T1 MinerU Model Cache Local Source And Teardown Prep

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R20_T1

Dispatch base head: a093405d

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Purpose

Open the bounded post-R19 planning tranche for MinerU model-cache, local-source,
and temporary-service teardown readiness. The worker must turn the accepted
R19 route into a source-verified prep matrix for a later private runtime smoke
pilot, without running MinerU, importing MinerU, installing packages,
downloading models, starting services, reading document body content, or
creating extraction outputs.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R20_T1 --title "MinerU Model Cache Local Source And Service Teardown Prep Planning" --date 2026-07-03 --base a093405d --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed scaffold fields, set DISPATCH_READY, added R19 dependency release, source-verified MinerU model-source/cache/service facts, and narrowed worker scope to planning plus read-only local metadata checks only. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`. |
| docOnlyNewFields | selectedRouteToken; modelSourceChoiceStatus; localModelPathStatus; mineruConfigWritebackRisk; temporaryServiceTeardownReceipt; runtimeSmokePilotReadiness |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition |
| --- | --- | --- | --- |
| MSEA-R19-T1 accepted route selection | `docs/reviews/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` | `707953bc` | SATISFIED - selected route token `OPEN_MODEL_CACHE_AND_LOCAL_SOURCE_PREP_WORK_ORDER_FIRST` opens this prep tranche |
| Session continuity after R19 acceptance | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V34_2026-07-03.md` | `a093405d` | SATISFIED - next allowed move names fresh GC-018/source-verified work order for model cache, local-source preparation, and temporary-service teardown receipt planning |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | This baseline excludes provider-local authority, keeps runtime candidates parked, separates doc-only fields from source facts, and requires worker-output checker source read-ahead before writing. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; ADIF resolver query exactness; Dependency Release Evidence; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields; Worker Return Packet Shape Contract fields; Source-Intake Decision Packet Fields; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; Target / Source; Scope / Applies To; Rescan Intelligence Hardening; ledger terminal marker; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; Delta block field labels; Agent Operation Trace labels. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm this baseline's dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this baseline and paired work order only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R19 accepted route opens model cache and local-source prep before runtime smoke | VALUE_SET | VALUE_SET | `docs/reviews/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_WORKER_RETURN_2026-07-03.md` | `## Reviewer Decision / Closure Disposition` | `OPEN_MODEL_CACHE_AND_LOCAL_SOURCE_PREP_WORK_ORDER_FIRST` | MSEA-R19-T1 worker return | ACCEPT |
| R19 readiness matrix selected the same model-cache/local-source prep route | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` | `## Route Decision Menu Selection` | `OPEN_MODEL_CACHE_AND_LOCAL_SOURCE_PREP_WORK_ORDER_FIRST` | MSEA-R19-T1 readiness matrix | ACCEPT |
| Candidate Group A remains private local CVF testing only | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | `## Claim Boundary` | Candidate Group A | MSEA-R17-T1 intake ledger | ACCEPT |
| MinerU source mirror remains the upstream authority for this lane | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `opendatalab__MinerU` | source mirror index | ACCEPT |
| MinerU can automatically start a local temporary service when no API URL is provided | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 146 | `mineru` | upstream README | ACCEPT |
| MinerU CLI supports a pipeline command envelope for local input and output paths | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | lines 332-336 | `mineru -p <input_path> -o <output_path> -b pipeline` | upstream README | ACCEPT |
| MinerU input may be local files or directories through supported surfaces | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 339 | local files or directories | upstream README | ACCEPT |
| MinerU model source uses accepted environment values and environment priority | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 12 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| MinerU unset model source reads `model-source` and may write back resolved source | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 26 | `model-source` | model source documentation | ACCEPT |
| MinerU model download writes model path and source to `mineru.json` | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 44 | `mineru.json` | model source documentation | ACCEPT |
| MinerU model updates can redownload to default location and update config | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 48 | `mineru-models-download` | model source documentation | ACCEPT |
| MinerU model download command must use a remote source and ignores local mode for that invocation | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 49 | `mineru-models-download` | model source documentation | ACCEPT |
| MinerU local model mode can be requested through the environment variable | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | lines 53-56 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| Docker deployment is limited to Linux and Windows with WSL2 | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/quick_start/docker_deployment.md` | line 6 | Docker deployment | Docker deployment documentation | ACCEPT |

## New Doc-Only Fields

| Field | Meaning | Disposition |
| --- | --- | --- |
| selectedRouteToken | Worker-selected next-route token for reviewer/closer consideration | DOC_ONLY_NEW |
| modelSourceChoiceStatus | Worker classification of whether operator has chosen `huggingface`, `modelscope`, `local`, or held auto mode | DOC_ONLY_NEW |
| localModelPathStatus | Worker classification of whether local model path proof exists | DOC_ONLY_NEW |
| mineruConfigWritebackRisk | Worker classification of config mutation risk for later runtime work | DOC_ONLY_NEW |
| temporaryServiceTeardownReceipt | Worker-defined future receipt fields for service detection and cleanup | DOC_ONLY_NEW |
| runtimeSmokePilotReadiness | Worker classification of whether later runtime smoke dispatch is ready | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Existing MSEA-R20 artifacts | negative search for `MSEA_R20_T1`, `MSEA-R20-T1`, `MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP`, and `Model Cache Local Source And Teardown Prep` across governed docs, session state, governance, and the source mirror index returned no matches before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Dispatch packet path check | Planned baseline, work order, worker return, and companion reference paths all returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| Collision decision | MSEA-R20-T1 is a new child tranche after accepted MSEA-R19-T1 route selection | SAFE_TO_CREATE |

## Source-Intake Decision Packet Fields

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | source-mirror absorption follow-on planning |
| Negative search performed | Yes - see Negative Search And Collision Discipline |
| Disposition | ADAPT |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R19 model/cache/local-source route | `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` | ENRICH_EXISTING | converts route selection into a worker-owned prep matrix | author R20 dispatch |
| MinerU model-source and config write-back facts | `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` | ENRICH_EXISTING | sharpens model-cache and local-source readiness before runtime | source-verify and classify |
| MinerU runtime execution | `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | REJECT_DIRECT_IMPORT | runtime remains unauthorized in this tranche | forbid execution |

## Baseline Decision

MSEA-R20-T1 is authorized for model-cache/local-source and temporary-service
teardown prep planning only. The worker may create a no-commit worker return
and companion readiness matrix that determine whether a later MSEA-R21 runtime
smoke pilot work order can be authored or must hold for operator model-source
choice, local model path proof, config write-back risk, or teardown receipt
conditions.

## Planned Artifact Manifest

| Artifact | Owner | Disposition |
| --- | --- | --- |
| `docs/reviews/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_WORKER_RETURN_2026-07-03.md` | worker | create uncommitted |
| `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | worker | create uncommitted |

## Verification Evidence

| Evidence | Command or source | Result |
| --- | --- | --- |
| Startup base | `git rev-parse --short HEAD` | `a093405d` |
| R19 acceptance dependency | `git log --oneline -6` | material `707953bc`, sync `a093405d` |
| Negative search | searched R20 IDs and title tokens across governed docs, session state, governance, and source mirror index | no matches before authoring |
| Path existence | `Test-Path` for planned baseline, work order, worker return, and companion reference | all returned `False` before authoring |
| ADIF disclosure | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` | 10 returned defects disclosed |
| Checker read-ahead | targeted reads of listed `governance/compat/check_*.py` files and R19 accepted packet shape | literal shape controls copied into this packet |

## Claim Boundary

This baseline authorizes only dispatch and no-commit worker planning for a
future private local MinerU runtime smoke pilot. It does not authorize MinerU
install, import, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker
execution, local temporary service startup, provider/live proof, S3/RAG,
source document copy/import, document body read, fuller content quotation,
schema/writer/adapter/checker implementation, package activation, public-sync,
benchmark, document-truth, extraction-accuracy, legal advice quality,
current-law correctness, production readiness, action authority, or
workflow-chain completion claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Candidate Group A source documents and future derived outputs are
authorized only for local private CVF testing unless the operator separately
approves fuller inclusion or public export.
