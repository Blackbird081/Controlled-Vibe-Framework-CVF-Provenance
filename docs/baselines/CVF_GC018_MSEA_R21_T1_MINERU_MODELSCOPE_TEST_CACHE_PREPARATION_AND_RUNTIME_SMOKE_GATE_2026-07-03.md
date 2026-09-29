# CVF GC-018 Baseline - MSEA-R21-T1 MinerU ModelScope Test Cache Preparation And Runtime Smoke Gate

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R21_T1

Dispatch base head: bd322a8d

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Purpose

Open the bounded post-R20 tranche for a test-only MinerU ModelScope model-cache
preparation gate. The worker may attempt a single ModelScope pipeline model
cache/download command only if the command already exists locally, while
capturing secret-safe config/cache evidence and preserving a hard stop before
any document parsing, OCR, VLM, API, Docker, service startup, package install,
source import, public-sync, production, or workflow-chain claim.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R21_T1 --title "MinerU ModelScope Test Cache Preparation And Runtime Smoke Gate" --date 2026-07-03 --base bd322a8d --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed scaffold fields, set DISPATCH_READY, added R20 dependency release, source-verified ModelScope/model-download/config-writeback facts, and narrowed worker scope to command-exists-gated ModelScope pipeline cache preparation only. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py`. |
| docOnlyNewFields | selectedRouteToken; modelSourceRoute; downloadCommandStatus; modelCachePrepDisposition; configWritebackReceipt; runtimeSmokeGateDisposition; installAuthorizationStatus |
| claimBoundary | Dispatch authoring provenance only; no parser/OCR/VLM/API/Docker/service/provider/live/public/Web/MCP/model-router behavior claim. |

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition |
| --- | --- | --- | --- |
| MSEA-R20-T1 accepted operator model-source checkpoint | `docs/reviews/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | `df5b71fa` | SATISFIED - selected route token `HOLD_PENDING_OPERATOR_MODEL_SOURCE_CHOICE` explicitly allowed operator selection among local, modelscope, huggingface, auto/config write-back, or defer |
| Session continuity after R20 acceptance | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V34_2026-07-03.md` | `bd322a8d` | SATISFIED - next allowed move names modelscope remote download permission as a release option before runtime smoke work-order authoring |
| Operator model-source choice | current operator instruction in this session | N/A | SATISFIED - operator accepted the ModelScope recommendation for test-first use and deferred deeper project-specific model selection |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | This baseline excludes provider-local authority, keeps worker-output checker read-ahead mandatory, separates command-exists-gated cache preparation from parser runtime, and blocks package install if the download command is missing. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; ADIF resolver query exactness; Dependency Release Evidence; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields; Worker Return Packet Shape Contract fields; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; Delta block field labels; Agent Operation Trace labels. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm this baseline's dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this baseline and paired work order only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MinerU source mirror remains the current upstream authority for this lane. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | line 35 | `opendatalab__MinerU` | source mirror index | ACCEPT |
| R20 selected a hold pending operator model-source choice before runtime smoke. | VALUE_SET | VALUE_SET | `docs/reviews/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_WORKER_RETURN_2026-07-03.md` | `## Reviewer Decision / Closure Disposition` | `HOLD_PENDING_OPERATOR_MODEL_SOURCE_CHOICE` | MSEA-R20-T1 worker return | ACCEPT |
| R20 matrix names modelscope download permission as a release option. | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | lines 62-67 | `modelscope` | MSEA-R20-T1 readiness matrix | ACCEPT |
| MinerU supports `MINERU_MODEL_SOURCE=modelscope`. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | lines 12-14 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| MinerU quick usage says users can switch from huggingface to modelscope through the environment variable. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md` | lines 4-6 | `MINERU_MODEL_SOURCE` | quick usage documentation | ACCEPT |
| MinerU built-in model download generates `mineru.json` and may update config. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md` | line 122 | `mineru-models-download` | quick usage documentation | ACCEPT |
| MinerU model download writes path and actual source to `mineru.json`. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 44 | `mineru.json` | model source documentation | ACCEPT |
| MinerU download command supports remote source and model type choices. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 91-105 | `--source`; `--model_type` | `download_models` | ACCEPT |
| MinerU download command supports pipeline or VLM models from ModelScope or HuggingFace. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 114-117 | `download_models` | `download_models` | ACCEPT |
| MinerU project exposes `mineru-models-download` as a console script. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | line 133 | `mineru-models-download` | project scripts | ACCEPT |
| MinerU config path can be set with `MINERU_TOOLS_CONFIG_JSON` or defaults to `mineru.json` in the user home directory. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 23-28 | `get_tools_config_file_path` | config path helper | ACCEPT |
| Pipeline backend is the lower-risk first smoke target because it can run CPU or GPU. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 74 | `pipeline` | upstream README backend comparison | ACCEPT |
| MinerU CLI parser runtime can automatically start a local temporary service without API URL. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 146 | `mineru` | upstream README | ACCEPT |
| VLM MinerU2.5 model exists on HuggingFace and ModelScope but is not selected for this first test gate. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/changelog.md` | line 112 | `opendatalab/MinerU2.5-2509-1.2B` | changelog | ACCEPT |

## New Doc-Only Fields

| Field | Meaning | Disposition |
| --- | --- | --- |
| selectedRouteToken | Worker-selected next route for reviewer/closer consideration | DOC_ONLY_NEW |
| modelSourceRoute | Records that the operator selected ModelScope for test-first preparation | DOC_ONLY_NEW |
| downloadCommandStatus | Worker classification of whether `mineru-models-download` exists locally | DOC_ONLY_NEW |
| modelCachePrepDisposition | Worker classification of command result, cache/config evidence, or blocker | DOC_ONLY_NEW |
| configWritebackReceipt | Secret-safe before/after `mineru.json` metadata and diff summary | DOC_ONLY_NEW |
| runtimeSmokeGateDisposition | Whether a later parser smoke work order can be authored | DOC_ONLY_NEW |
| installAuthorizationStatus | Records that package install remains unauthorized in this tranche | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R21 artifact path check | `Test-Path` for planned baseline, work order, worker return, and companion reference returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| R21 token search | `rg -n "MSEA_R21_T1|MSEA-R21-T1|MODELSCOPE_TEST_CACHE_PREPARATION|ModelScope Test Cache Preparation" docs CVF_SESSION AGENT_HANDOFF_V34_2026-07-03.md .private_reference/source_mirrors/INDEX.md` returned no matches before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | MSEA-R21-T1 is a new child tranche released by accepted MSEA-R20-T1 and operator ModelScope test choice | SAFE_TO_CREATE |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| modelDownloadAuthorized | CONDITIONAL_YES_MODELSCOPE_PIPELINE_ONLY |
| packageInstallAuthorized | NO |
| freshnessVerificationMode | SOURCE_VERIFIED_CONDITIONAL_DOWNLOAD_ONLY |
| reason | This dispatch authorizes only a command-exists-gated ModelScope pipeline model cache/download attempt; it does not authorize parser runtime, service startup, OCR, VLM, Docker, provider/live proof, or package install. |
| requiredFutureAction | If command exists and cache preparation succeeds, author a separate parser smoke work order; if command is missing, return a package-install authorization blocker. |

## Source-Intake Decision Packet Fields

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | source-mirror absorption follow-on planning |
| Negative search performed | Yes - see Negative Search And Collision Discipline |
| Disposition | RUNTIME_CANDIDATE |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R20 operator model-source hold route | `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | ENRICH_EXISTING | converts operator ModelScope choice into a bounded command-exists cache-prep gate | execute R21 worker |
| MinerU model-source and config write-back facts | `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | ENRICH_EXISTING | sharpens ModelScope test route and config receipt requirements | source-verify and classify |
| MinerU package install | `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | REJECT_DIRECT_IMPORT | package lifecycle remains unauthorized in this tranche | forbid install |
| MinerU parser runtime | `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | REJECT_DIRECT_IMPORT | parser runtime remains unauthorized until a later work order | forbid execution |

## Baseline Decision

MSEA-R21-T1 is authorized as a test-only ModelScope pipeline cache preparation
gate. The worker may create a no-commit worker return and companion readiness
matrix. If `mineru-models-download` is available, the worker may run exactly
one command using explicit source and model type:

```powershell
mineru-models-download --source modelscope --model_type pipeline
```

If the command is missing, the worker must not install packages or run `pip`,
`uv`, `conda`, Docker, WSL, parser, OCR, VLM, API, router, Gradio, or service
commands. The worker must return a blocker route that preserves the need for a
fresh package-install or environment-prep work order.

## Planned Artifact Manifest

| Artifact | Owner | Disposition |
| --- | --- | --- |
| `docs/reviews/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_WORKER_RETURN_2026-07-03.md` | worker | create uncommitted |
| `docs/reference/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_READINESS_MATRIX_2026-07-03.md` | worker | create uncommitted |

## Verification Evidence

| Evidence | Command or source | Result |
| --- | --- | --- |
| Startup base | `git rev-parse --short HEAD` | `bd322a8d` |
| Worktree cleanliness | `git status --short` | no output before authoring |
| R20 dependency | `git log --oneline -8` | material `df5b71fa`, sync `bd322a8d` |
| Negative search | R21 title and token search across governed docs, session state, active handoff, and mirror index | no matches before authoring |
| Path existence | `Test-Path` for planned baseline, work order, worker return, and companion reference | all returned `False` before authoring |
| ADIF disclosure | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` | 10 returned defects disclosed |
| Checker read-ahead | targeted reads of listed `governance/compat/check_*.py` files | literal shape controls copied into this packet |

## Claim Boundary

This baseline authorizes dispatch and no-commit worker execution for a
ModelScope pipeline model-cache preparation gate only. It does not authorize
MinerU package installation, source import, parser/OCR/VLM/hybrid/API/router/
Gradio/Docker execution, local temporary service startup, document body read,
extraction outputs, provider/live proof, S3/RAG, schema/writer/adapter/checker
implementation, public-sync, benchmark, document-truth, extraction-accuracy,
legal advice quality, current-law correctness, production readiness, action
authority, or workflow-chain completion claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Candidate Group A source documents and any future derived outputs are
authorized only for local private CVF testing unless the operator separately
approves fuller inclusion or public export.
