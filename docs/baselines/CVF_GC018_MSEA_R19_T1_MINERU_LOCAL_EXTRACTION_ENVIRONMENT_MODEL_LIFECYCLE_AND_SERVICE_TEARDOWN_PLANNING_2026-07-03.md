# CVF GC-018 Baseline - MSEA-R19-T1 MinerU Local Extraction Environment Model Lifecycle And Service Teardown Planning

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R19_T1

Dispatch base head: add7eda4

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Purpose

Open a bounded planning tranche after accepted MSEA-R18-T1 selected
`HOLD_RUNTIME_PENDING_ENVIRONMENT_OR_MODEL_PLAN`. The worker must source-verify
MinerU environment/model/source/service facts, perform only read-only local
environment inventory, and produce a readiness matrix for a later local runtime
pilot without installing MinerU, downloading models, starting services, or
running parser/OCR/VLM/hybrid/API/router/Gradio/Docker paths.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R19_T1 --title "MinerU Local Extraction Environment Model Lifecycle And Service Teardown Planning" --date 2026-07-03 --base add7eda4 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed scaffold fields, set DISPATCH_READY, added R18 dependency release, source-verified MinerU model-source/environment/service facts, and narrowed worker scope to planning plus read-only inventory only. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`. |
| docOnlyNewFields | selectedRouteToken; environmentInventoryMode; modelLifecyclePlan; temporaryServiceTeardownPlan; runtimeSmokePilotReadiness; outputQuarantineDisposition |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition |
| --- | --- | --- | --- |
| MSEA-R18-T1 local extraction pilot plan and receipt readiness selection accepted | `docs/reviews/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | `d40e21c8` | SATISFIED - selected route token `HOLD_RUNTIME_PENDING_ENVIRONMENT_OR_MODEL_PLAN` opens this planning-only tranche |
| Session continuity after R18 acceptance | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V34_2026-07-03.md` | `add7eda4` | SATISFIED - next allowed move names fresh GC-018/source-verified work order or roadmap for environment/model/service planning |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | This baseline avoids provider-local authority, keeps runtime candidates held, mandates worker-output checker read-ahead, separates doc-only fields from source facts, and keeps symbol cells to real symbols or sections. |

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
| R18 accepted route holds runtime pending environment or model plan | VALUE_SET | VALUE_SET | `docs/reviews/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_WORKER_RETURN_2026-07-03.md` | `## Reviewer Decision / Closure Disposition` | `HOLD_RUNTIME_PENDING_ENVIRONMENT_OR_MODEL_PLAN` | MSEA-R18-T1 worker return | ACCEPT |
| R18 matrix marks Environment Plan, Model Lifecycle, and Temporary Service as unresolved | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | `## Runtime Prerequisite Disposition` | Runtime Prerequisite Disposition | MSEA-R18-T1 readiness matrix | ACCEPT |
| R18 command envelope is future-only and not executed | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | `## Pilot Command Envelope` | Pilot Command Envelope | MSEA-R18-T1 readiness matrix | ACCEPT |
| R17 accepted Candidate Group A only for local private CVF testing | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | `## Claim Boundary` | Candidate Group A | MSEA-R17-T1 intake ledger | ACCEPT |
| R12 local parser runtime pilot requires fresh GC-018 authorization | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | runtime pilot gating table | Local parser runtime pilot | MSEA-R12-T1 policy reference | ACCEPT |
| MinerU pinned mirror is the upstream authority for this lane | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `opendatalab__MinerU` | source mirror index | ACCEPT |
| MinerU CLI entry point is available as a project script | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | project scripts section | `mineru` | project scripts | ACCEPT |
| MinerU model download command is available as a project script but remains forbidden here | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | project scripts section | `mineru-models-download` | project scripts | ACCEPT |
| MinerU README says the pipeline backend runs on CPU or GPU | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 74 | `pipeline` | upstream README | ACCEPT |
| MinerU README states `mineru` can automatically start a local temporary service when no API URL is provided | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 146 | `mineru` | upstream README | ACCEPT |
| MinerU README states pure CPU execution is supported and GPU/MPS acceleration also exists | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 184 | pure CPU environment | upstream README | ACCEPT |
| MinerU README cautions that non-mainline environments are not guaranteed | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 216 | non-mainline environments | upstream README | ACCEPT |
| MinerU README shows pipeline command envelope for CPU use | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | lines 334-336 | `mineru -p <input_path> -o <output_path> -b pipeline` | upstream README | ACCEPT |
| MinerU model-source docs define `MINERU_MODEL_SOURCE` accepted values | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 12 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| MinerU model-source docs say unset variable allows automatic source selection | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 12 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| MinerU model-source docs say the config write-back records the actual source after first auto probe | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 26 | `model-source` | model source documentation | ACCEPT |
| MinerU model-source docs say model download writes model path and source to `mineru.json` | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 44 | `mineru.json` | model source documentation | ACCEPT |
| MinerU model-source docs say local models can be enabled through environment variables | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | lines 53-55 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| MinerU Docker docs restrict Docker deployment to Linux and Windows with WSL2 | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/quick_start/docker_deployment.md` | line 6 | Docker deployment | Docker deployment documentation | ACCEPT |
| MinerU Docker docs warn GPU memory pre-allocation can block multiple vLLM services | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/quick_start/docker_deployment.md` | line 54 | vLLM service | Docker deployment documentation | ACCEPT |

## New Doc-Only Fields

| Field | Meaning | Disposition |
| --- | --- | --- |
| selectedRouteToken | Worker-selected next-route token for reviewer/closer consideration | DOC_ONLY_NEW |
| environmentInventoryMode | Read-only local inventory mode, not installation or runtime execution | DOC_ONLY_NEW |
| modelLifecyclePlan | Documentation-only model source/cache/download/local-mode plan for a later tranche | DOC_ONLY_NEW |
| temporaryServiceTeardownPlan | Documentation-only local service detection and teardown checklist for a later tranche | DOC_ONLY_NEW |
| runtimeSmokePilotReadiness | Worker classification of whether a future runtime pilot can be authored | DOC_ONLY_NEW |
| outputQuarantineDisposition | Worker classification of private output root and no-public/no-commit handling | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Existing MSEA-R19 artifacts | negative search for `MSEA_R19_T1`, `MSEA-R19-T1`, `LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN`, and `Local Extraction Environment Model Lifecycle And Service Teardown` across governed docs and active session surfaces returned no matches before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Dispatch packet path check | No existing baseline or work order with these exact R19 names existed before this add operation | ABSENT_BEFORE_AUTHORING |
| Collision decision | MSEA-R19-T1 is a new child tranche after accepted MSEA-R18-T1 planning route selection | SAFE_TO_CREATE |

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
| R18 environment/model/service hold | `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | ENRICH_EXISTING | converts unresolved prerequisites into a worker-owned readiness matrix | author MSEA-R19-T1 dispatch |
| MinerU model-source and local-service facts | `.private_reference/source_mirrors/opendatalab__MinerU/`; R18 matrix | ENRICH_EXISTING | adds model-source/cache/config write-back and service teardown planning surface | source-verify and classify |
| MinerU runtime execution | R12/R18 held-lane surfaces | REJECT_DIRECT_IMPORT | runtime remains unauthorized in this tranche | forbid execution and keep route selection only |

## Baseline Decision

MSEA-R19-T1 is authorized for environment/model/service lifecycle planning and
read-only local inventory only. The worker may author a worker return and a
companion readiness matrix that decide whether a later MSEA-R20 local runtime
smoke pilot work order can be authored, or whether model-cache, service
teardown, operator environment choice, or output-quarantine conditions remain
held. This GC-018 does not authorize runtime execution.

## Planned Artifact Manifest

| Artifact | Owner | Disposition |
| --- | --- | --- |
| `docs/reviews/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_WORKER_RETURN_2026-07-03.md` | worker | create uncommitted |
| `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` | worker | create uncommitted |

## Verification Evidence

| Evidence | Command or source | Result |
| --- | --- | --- |
| Startup base | `git rev-parse --short HEAD` | `add7eda4` |
| R18 acceptance dependency | `git log --oneline -2` | material `d40e21c8`, sync `add7eda4` |
| Negative search | searched `MSEA_R19_T1`, `MSEA-R19-T1`, `LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN`, and `Local Extraction Environment Model Lifecycle And Service Teardown` across governed docs and active session surfaces | no matches before authoring |
| ADIF disclosure | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` | 10 returned defects disclosed |
| Checker read-ahead | targeted reads of listed `governance/compat/check_*.py` files | literal shape controls copied into this packet |

## Claim Boundary

This baseline authorizes only dispatch and no-commit worker planning for a
future private local MinerU runtime smoke pilot. It does not authorize MinerU
install, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker
execution, local temporary service startup, provider/live proof, S3/RAG,
source document copy/import, fuller content quotation, schema/writer/adapter/
checker implementation, package activation, public-sync, benchmark,
document-truth, extraction-accuracy, legal advice quality, current-law
correctness, production readiness, action authority, or workflow-chain
completion claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Candidate Group A source documents and any future derived outputs are
authorized only for local private CVF testing unless the operator separately
approves fuller inclusion or public export.
