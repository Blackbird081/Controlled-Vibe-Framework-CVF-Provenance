# CVF GC-018 Baseline - MSEA-R24-T2A MinerU Absolute Config Path And Local Cache Binding

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-03

Batch ID: MSEA-R24-T2A

Dispatch base head: 9a24c3b6

Commit mode: WORKER_MUST_NOT_COMMIT

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Purpose

Dispatch one bounded recovery worker tranche after accepted MSEA-R24-T2. T2
proved the HuggingFace pipeline snapshot exists locally, but did not write a
MinerU config receipt because the relative `MINERU_TOOLS_CONFIG_JSON` value
resolved under the user home and its parent directory was absent. T2A
authorizes only one follow-up HuggingFace pipeline command using an absolute
config path under ignored `.cvf/runtime` so the worker can record whether the
local cache can be bound into a config receipt.

## Scope

| Field | Value |
|---|---|
| In scope | T2A dispatch packet for absolute config path and local HuggingFace cache binding receipt recovery |
| Out of scope | runtime smoke, document processing, parser/OCR/VLM/API/router/Gradio/Docker/WSL execution, provider/live proof, public-sync, package reinstall, production readiness |
| Owner | dispatcher for packet authoring; worker for future uncommitted command evidence; reviewer/closer for material acceptance |

## Decision / Baseline / Proposed Tranche

| Field | Value |
|---|---|
| Decision | Dispatch T2A only after accepted T2 selected `HOLD_PENDING_LOCAL_MODEL_PATH` and recorded `CONFIG_NOT_WRITTEN_PARENT_DIRECTORY_MISSING` |
| Baseline | existing ignored R22 venv, existing HuggingFace snapshot evidence, and source-verified MinerU absolute config path behavior |
| Proposed tranche | MSEA-R24-T2A MinerU absolute config path and local cache binding |
| Dispatch route | WORKER_MUST_NOT_COMMIT |

## Evidence / Verification

| Evidence | Source |
|---|---|
| T2 accepted diagnostic | `docs/reviews/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_WORKER_RETURN_2026-07-03.md` |
| T2 selected hold token | `docs/reference/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_READINESS_MATRIX_2026-07-03.md` |
| Absolute config path behavior | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` |
| Config writeback behavior | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` |
| Pre-dispatch verification | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 9a24c3b6 --head HEAD` |

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| R24 roadmap T2/T3 dependency | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | `aa2614f6` | SATISFIED - T3 remains gated until config/cache receipt is accepted |
| T2 accepted diagnostic | `docs/reviews/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_WORKER_RETURN_2026-07-03.md` | `561eedc3` | SATISFIED - selected `HOLD_PENDING_LOCAL_MODEL_PATH` and released only T2A work-order authoring |
| T2 session sync | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `5ad392b6` | SATISFIED - next allowed move routes to T2A authoring |
| T2 handoff marker | `AGENT_HANDOFF_V35_2026-07-03.md` | `9a24c3b6` | SATISFIED - active handoff names T2A as next allowed move |
| R22 venv command exists | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | `7b105700` | SATISFIED - venv-local command was accepted earlier and still exists by pre-dispatch `Test-Path` |

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
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` reviewed before authoring |
| generatedProfile | compact manual dispatch using T2 shape plus current source verification |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Manual baseline keeps the helper-required blocks and narrows the command to absolute-path recovery. |
| checkerReadAheadConfirmation | Checker Source Read-Ahead Block lists dispatch, worker-output, and absorption checkers. |
| docOnlyNewFields | T2A result tokens are doc-only route-selection fields for worker/reviewer disposition. |
| claimBoundary | Scaffold provenance describes dispatch packet shape only; no command has been run by this baseline. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; Dependency Release Evidence; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; External Knowledge Intake Routing row labels; External Absorption Core row labels; External Absorption Value Conversion Matrix columns; Overlap And Novelty Classification dispositions; ledger_terminal=; Corpus verdict bullet; Public Export Disposition |
| gateRunPurpose | Confirmation evidence after checker source read-ahead; gates confirm this baseline and paired work order shape. |
| claimBoundary | Dispatch only; worker output artifacts require their own checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T2 selected local model or config-path recovery. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_READINESS_MATRIX_2026-07-03.md` | line 9 | `HOLD_PENDING_LOCAL_MODEL_PATH` | T2 readiness matrix | ACCEPT |
| T2 config receipt was not written because parent directory was missing. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_READINESS_MATRIX_2026-07-03.md` | line 13 | `CONFIG_NOT_WRITTEN_PARENT_DIRECTORY_MISSING` | T2 readiness matrix | ACCEPT |
| MinerU uses `MINERU_TOOLS_CONFIG_JSON` to choose the tools config file. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | line 25 | `MINERU_TOOLS_CONFIG_JSON` | `get_tools_config_file_path` | ACCEPT |
| MinerU returns an absolute config path unchanged. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | line 21 definition; body lines 26-27 | `get_tools_config_file_path` | `get_tools_config_file_path` | ACCEPT |
| MinerU joins relative config paths under the user home. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | line 21 definition; body line 28 | `get_tools_config_file_path` | `get_tools_config_file_path` | ACCEPT |
| MinerU writes the modified config file with `open(local_filename, 'w')`. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 83-84 | `download_and_modify_json` | config writeback helper | ACCEPT |
| MinerU pipeline download calls `configure_model` after downloading pipeline models. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 36-52 | `download_pipeline_models` | MinerU model download CLI | ACCEPT |
| `configure_model` writes `models-dir.pipeline` and `model-source` to the selected config file. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 21-32 | `configure_model` | MinerU model download CLI | ACCEPT |
| R22 ignored venv exists and contains the download command. | VALUE_SET | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | lines 57-58 | `.cvf/runtime/msea-r22-mineru-venv` | R22 readiness matrix | ACCEPT |
| Local HuggingFace pipeline snapshot exists from T2. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_READINESS_MATRIX_2026-07-03.md` | line 127 | `HuggingFace snapshot path` | T2 readiness matrix | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned path existence | `Get-ChildItem` found no T2A baseline or work order before authoring. | SAFE_TO_CREATE |
| Token search | `rg -n "MSEA_R24_T2A|MSEA-R24-T2A|ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING" docs CVF_SESSION` found no prior T2A dispatch artifact before authoring. | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | T2A is a recovery child of accepted T2 and current next-move surfaces. | SAFE_TO_CREATE |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned MinerU source mirror plus accepted T2 diagnostic -> T2A absolute config path recovery |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this baseline and paired work order |
| Disposition | ADAPT: convert source-backed T2 failure into one bounded absolute-path recovery command |
| Claim boundary | dispatch only; worker execution must record receipt or diagnostic |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Enumeration command | `filesystem-backed direct reads of cited T2/R22/MinerU source files` |
| Manifest artifact or inline manifest | inline table: Source Verification Block |
| Processing ledger artifact or inline ledger | inline table: Dependency Release Evidence |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | `docs/reviews/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_READINESS_MATRIX_2026-07-03.md`; `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md`; `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Unresolved items | T2A command result, absolute config receipt, T3 runtime-smoke release |
| Completion claim boundary | dispatch only; no runtime smoke or parser execution |

ledger_terminal=READ for cited source evidence; ledger_terminal=ADAPTED for T2A dispatch; ledger_terminal=DEFERRED for command result and T3/T4; ledger_terminal=REJECTED for direct runtime smoke in T2A.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| T2 readiness matrix | local config-path recovery needed | RUNTIME_CANDIDATE | T2A work order | dispatch bounded recovery command | one command only |
| MinerU config helper | absolute paths are accepted unchanged | DOCTRINE_ADAPTED | T2A worker | use absolute ignored config path | no repo config |
| MinerU writeback helper | parent directory must exist for target write | RUNTIME_CANDIDATE | T2A worker | use existing `.cvf/runtime` parent | no source patch |
| R22 venv | command exists | PACKAGE_CANDIDATE | T2A worker | reuse only | no reinstall |
| Runtime smoke | requires accepted T2A receipt first | REJECT_DIRECT_IMPORT | claim boundary | defer to T3 | no smoke |
| Workflow-chain policy | requires T3 first | CHECKER_CANDIDATE | future T4 | defer | no checker implementation |
| Public export | not authorized | NO_PACKAGE_OR_RUNTIME_VALUE | private provenance only | none | no public-sync |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| T2 failure diagnostic | `docs/reference/CVF_MSEA_R24_T2_MINERU_HUGGINGFACE_CACHE_COMPLETION_RECOVERY_READINESS_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | releases T2A recovery authoring | dispatch |
| MinerU config helper | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | ENRICH_EXISTING | absolute path explanation narrows recovery command | adapt |
| R22 venv | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | reuse only | cite |
| Runtime smoke | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | REJECT_DIRECT_IMPORT | T3 only after receipt | defer |
| Workflow-chain policy | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | REJECT_DIRECT_IMPORT | T4 only after smoke | defer |

## Corpus Completeness And Report Integrity

- Corpus task class: T2A dispatch for bounded absolute config path recovery.
- Corpus root: accepted T2 artifacts, R22 readiness matrix, and pinned MinerU config/download source.
- Snapshot time: 2026-07-03 dispatch authoring.
- Enumeration command: filesystem-backed direct reads of cited source files.
- Manifest artifact or inline manifest: Source Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded dispatch source set, not a new corpus snapshot.
- Processing ledger artifact or inline ledger: Dependency Release Evidence and paired work order.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=T2/R22/MinerU source evidence; ledger_terminal=READ/ADAPTED/DEFERRED/REJECTED; exclusions=parser runtime, document processing, public-sync, provider/live proof, production claims; unresolved=0 for dispatch authoring.
- Unresolved files: none for dispatch authoring.
- Declared exclusions: runtime smoke, parser execution, document body read, extraction outputs, public-sync, provider/live proof, production readiness.
- Unreadable or unsupported files: none identified.
- Aggregation check: PASS - accepted owner surfaces are cited.
- Drift check: PASS - T2 selected local config-path recovery.
- Output traceability: paired T2A work order names worker return and readiness matrix.
- Adversarial verification: direct runtime smoke and workflow-chain completion are rejected for T2A.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or recovery requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T2 requires config/cache receipt before T3 | Dependency Release Evidence | selected T2 route and config receipt absence | pre-dispatch gate | PASS |
| T2A may run one recovery command only | Work order Allowed Command | command evidence | worker return | PASS |
| T3 remains gated | Claim Boundary | runtimeSmokeGateDisposition | reviewer check | PASS |
| T4 remains gated | Claim Boundary | workflow-chain disposition | reviewer check | PASS |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher creates packet; worker returns uncommitted outputs; reviewer/closer owns material commit and session-sync |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=9a24c3b6; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | baseline and work order only for dispatch; worker may create only the two planned outputs and ignored runtime receipts |
| traceScope(phase, actor) | dispatcher trace in this packet; worker trace in return/matrix; reviewer trace in closure/session-sync |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | MSEA-R24-T2A only; T3/T4 require separate release evidence and work orders |
| nextMoveSurfaces | reviewer/closer updates session surfaces only after accepting worker return |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R24-T2A dispatch for one absolute config path cache-binding recovery command |
| claimDisposition | CLAIM_REJECTED: dispatch does not execute the command or claim runtime readiness |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker must create receipt or diagnostic |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no command action in dispatch |
| invocationBoundary | local governed dispatch authoring only |
| interceptionBoundary | no provider, parser, Web, MCP, adapter, or production route interception claim |
| claimLanguage | work-order dispatch and future worker receipt only |
| forbiddenExpansion | no parser/OCR/VLM/API/router/Gradio/Docker/WSL execution, document processing, provider/live proof, public-sync, runtime smoke, workflow-chain completion, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet; no public-sync export is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R24-T2A absolute config path recovery dispatch, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, source reads, apply_patch, governance gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | T2 material commit `561eedc3`; session-sync commit `5ad392b6`; handoff marker `9a24c3b6` |
| Before status evidence | clean worktree at `9a24c3b6` before dispatch authoring |
| After status evidence | baseline and work order pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no cache command executed by dispatch; no runtime smoke |
| Agent type | dispatcher |
| Invocation ID | `msea-r24-t2a-absolute-config-path-dispatch-2026-07-03` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | this baseline and paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch |

## Claim Boundary

This baseline authorizes only a future worker to run one bounded HuggingFace
pipeline cache-binding command with an absolute ignored config path and record
receipt/diagnostic evidence. It does not authorize parser runtime, document
processing, public-sync, provider/live proof, runtime smoke, workflow-chain
completion, production readiness, stage, commit, or push.
