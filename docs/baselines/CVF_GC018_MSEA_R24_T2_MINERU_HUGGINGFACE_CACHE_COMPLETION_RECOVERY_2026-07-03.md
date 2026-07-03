# CVF GC-018 Baseline - MSEA-R24-T2 MinerU HuggingFace Cache Completion Recovery

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-03

Batch ID: MSEA-R24-T2

Dispatch base head: 2356c27c

Commit mode: WORKER_MUST_NOT_COMMIT

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Purpose

Dispatch one bounded worker tranche to run a single HuggingFace MinerU pipeline
cache-completion command using the existing ignored R22 venv, then record a
config/cache receipt or a secret-safe diagnostic. This baseline authorizes no
parser/OCR/VLM/API/router/Gradio/Docker/WSL runtime smoke and no document
processing.

## Scope

| Field | Value |
|---|---|
| In scope | T2 dispatch packet for one bounded HuggingFace cache-completion command |
| Out of scope | runtime smoke, document processing, provider/live proof, public-sync, production readiness |
| Owner | dispatcher for packet authoring; worker for future uncommitted execution evidence |

## Decision / Baseline / Proposed Tranche

| Field | Value |
|---|---|
| Decision | Dispatch T2 only after accepted T1 selected HuggingFace cache recovery |
| Baseline | existing ignored R22 venv and source-verified MinerU download CLI |
| Proposed tranche | MSEA-R24-T2 HuggingFace cache-completion recovery |
| Dispatch route | WORKER_MUST_NOT_COMMIT |

## Evidence / Verification

| Evidence | Source |
|---|---|
| T1 route release | accepted T1 decision matrix selected `SELECT_HUGGINGFACE_CACHE_RECOVERY` |
| CLI support | MinerU source mirror verifies `--source` and `--model_type pipeline` |
| Config receipt expectation | MinerU docs and config helper verify `mineru.json` and `MINERU_TOOLS_CONFIG_JSON` |
| Pre-dispatch verification | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 2356c27c --head HEAD` |

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| R24 roadmap T2 dependency | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | `aa2614f6` | SATISFIED - T2 opens only after T1 selects a source route |
| T1 selected HuggingFace | `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md` | `86097efe` | SATISFIED - selected `SELECT_HUGGINGFACE_CACHE_RECOVERY` and released T2 authoring only |
| R22 venv command exists | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | `7b105700` | SATISFIED - venv and command activation were ready local only |

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
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` reviewed as local helper surface |
| generatedProfile | manual dispatch packet authoring after helper/source read-ahead |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Manual baseline authored from current T1/R22/MinerU evidence and repaired against pre-dispatch gates. |
| checkerReadAheadConfirmation | Checker Source Read-Ahead Block lists the dispatch and absorption gates used for this packet. |
| docOnlyNewFields | none |
| claimBoundary | Scaffold provenance describes dispatch packet shape only; no cache command or runtime behavior is claimed. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: this dispatch batch may update active
session wording only to prevent the dispatch lifecycle checker from confusing
the accepted T1 closure row with the still-open T2 dispatch lane. The change is
literal-text clarification only and does not alter the T1 closure decision, T2
runtime authority, checker behavior, or generated-state schema.

Protected paths:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/entries/mseaR24T1MineruModelSourceFallbackDecisionClosure20260703.json`
- `CVF_SESSION_MEMORY.md`

Operator authorization: operator asked to continue the dependency-gated T1-T4
sequence; this protected-path edit is required only to keep T2 dispatch
machine-checkable after T1 closure.

Rollback boundary: if rejected, revert only this T2 dispatch packet and the
literal session wording clarification. Do not revert material T1 acceptance
commit `86097efe` or earlier session-sync commits.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; Dependency Release Evidence; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; External Knowledge Intake Routing row labels; External Absorption Core row labels; External Absorption Value Conversion Matrix columns; Overlap And Novelty Classification dispositions; ledger_terminal=; Corpus verdict bullet; Public Export Disposition |
| gateRunPurpose | Confirmation evidence after checker source read-ahead; gates confirm this baseline and paired work order shape. |
| claimBoundary | Dispatch only; no worker execution, cache command, parser runtime, provider/live proof, public-sync, or production behavior is claimed here. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1 selected HuggingFace cache recovery. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md` | selectedRouteToken line | `SELECT_HUGGINGFACE_CACHE_RECOVERY` | T1 decision matrix | ACCEPT |
| MinerU exposes the download console script. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | line 133 | `mineru-models-download` | project scripts | ACCEPT |
| MinerU download CLI supports remote source option. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 94-103 | `--source` | MinerU model download CLI | ACCEPT |
| MinerU download CLI supports pipeline model type. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 104-117 | `--model_type` | MinerU model download CLI | ACCEPT |
| MinerU completed downloads write model path and source into config. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 44 | `mineru.json` | MinerU model-source docs | ACCEPT |
| MinerU model download must use a remote source. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 49 | `mineru-models-download` | MinerU model-source docs | ACCEPT |
| MinerU config path can be redirected by `MINERU_TOOLS_CONFIG_JSON`. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 23-25 | `get_tools_config_file_path` | config path helper | ACCEPT |
| R22 ignored venv exists and contains the download command. | VALUE_SET | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | lines 57-58 | `.cvf/runtime/msea-r22-mineru-venv` | R22 readiness matrix | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned path existence | `Test-Path` returned False for the T2 baseline, work order, worker return, and readiness matrix before authoring. | SAFE_TO_CREATE |
| Token search | `rg -n "MSEA_R24_T2|MSEA-R24-T2|HUGGINGFACE_CACHE_COMPLETION_RECOVERY" docs CVF_SESSION .private_reference/source_mirrors/INDEX.md` found no prior T2 dispatch artifacts. | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | T2 is released by accepted T1 and current next-move surfaces. | SAFE_TO_CREATE |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned MinerU source mirror plus accepted T1 decision -> T2 bounded HuggingFace cache-completion recovery |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this baseline and paired work order |
| Disposition | ADAPT: convert source-backed T1 route into one bounded cache-completion dispatch |
| Claim boundary | dispatch only; worker execution must record receipt or diagnostic |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Enumeration command | `filesystem-backed direct reads of cited T1/R22/MinerU source files` |
| Manifest artifact or inline manifest | inline table: Source Verification Block |
| Processing ledger artifact or inline ledger | inline table: Dependency Release Evidence |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md`; `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md`; `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Unresolved items | T2 command result, config receipt, cache completion, T3 smoke release |
| Completion claim boundary | dispatch only; no runtime smoke or parser execution |

ledger_terminal=READ for cited source evidence; ledger_terminal=ADAPTED for T2 dispatch; ledger_terminal=DEFERRED for command result and T3/T4; ledger_terminal=REJECTED for direct runtime smoke in T2.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| T1 decision matrix | HuggingFace selected | RUNTIME_CANDIDATE | T2 work order | dispatch bounded command | one cache command only |
| MinerU CLI source | source and pipeline options exist | RUNTIME_CANDIDATE | T2 worker | run exact command | no parser |
| MinerU config helper | config path override exists | DOCTRINE_ADAPTED | T2 worker | write ignored config receipt if command completes | no repo config |
| R22 venv | local command exists | PACKAGE_CANDIDATE | T2 worker | reuse only | no reinstall |
| Runtime smoke | requires T2 receipt first | REJECT_DIRECT_IMPORT | claim boundary | defer to T3 | no smoke |
| Workflow chain | requires T3 first | CHECKER_CANDIDATE | future T4 | defer | no checker implementation |
| Public export | not authorized | NO_PACKAGE_OR_RUNTIME_VALUE | private provenance only | none | no public-sync |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| T1 source choice | `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | releases T2 authoring | dispatch |
| MinerU CLI | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | ENRICH_EXISTING | exact HuggingFace pipeline command | adapt |
| R22 venv | `docs/reference/CVF_MSEA_R22_T1_MINERU_PACKAGE_INSTALL_ACTIVATION_AND_MODELSCOPE_PIPELINE_CACHE_PREPARATION_READINESS_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | reuse only | cite |
| Runtime smoke | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | REJECT_DIRECT_IMPORT | T3 only after receipt | defer |
| Workflow-chain policy | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | REJECT_DIRECT_IMPORT | T4 only after smoke | defer |

## Corpus Completeness And Report Integrity

- Corpus task class: T2 dispatch for bounded cache-completion recovery.
- Corpus root: T1 decision matrix, R22 readiness matrix, and pinned MinerU CLI/config docs.
- Snapshot time: 2026-07-03 dispatch authoring.
- Enumeration command: filesystem-backed direct reads of cited source files.
- Manifest artifact or inline manifest: Source Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded dispatch source set, not a new corpus snapshot.
- Processing ledger artifact or inline ledger: Dependency Release Evidence and paired work order.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=T1/R22/MinerU source evidence; ledger_terminal=READ/ADAPTED/DEFERRED/REJECTED; exclusions=parser runtime, document processing, public-sync, provider/live proof, production claims; unresolved=0 for dispatch authoring.
- Unresolved files: none for dispatch authoring.
- Declared exclusions: runtime smoke, parser execution, document body read, extraction outputs, public-sync, provider/live proof, production readiness.
- Unreadable or unsupported files: none identified.
- Aggregation check: PASS - accepted owner surfaces are cited.
- Drift check: PASS - T1 selected HuggingFace route.
- Output traceability: paired T2 work order names worker return and readiness matrix.
- Adversarial verification: direct runtime smoke and workflow-chain completion are rejected for T2.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T2 requires T1 route release | Dependency Release Evidence | selected route token | pre-dispatch gate | PASS |
| T2 may run one bounded command | Work order Allowed Command | command evidence | worker return | PASS |
| T3 remains gated | Claim Boundary | runtimeSmokeGateDisposition | reviewer check | PASS |
| T4 remains gated | Claim Boundary | workflow-chain disposition | reviewer check | PASS |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher creates packet; worker returns uncommitted outputs; reviewer/closer owns material commit and session-sync |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=2356c27c; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | baseline and work order only for dispatch; worker may create only the two planned outputs and ignored runtime receipts |
| traceScope(phase, actor) | dispatcher trace in this packet; worker trace in return/matrix; reviewer trace in closure/session-sync |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | MSEA-R24-T2 only; T3/T4 require separate release evidence and work orders |
| nextMoveSurfaces | reviewer/closer updates session surfaces only after accepting worker return |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R24-T2 dispatch for one bounded HuggingFace cache command |
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
| Session or invocation | MSEA-R24-T2 HuggingFace cache-completion recovery dispatch, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, source reads, `apply_patch`, governance gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | T1 material commit `86097efe`; session-sync commit `dc1c8392`; handoff marker `c1b8079b`; dispatch wording clarification `eb4ecd4f`; handoff marker `2356c27c` |
| Before status evidence | clean worktree before dispatch authoring |
| After status evidence | baseline and work order pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no cache command executed by dispatch; no runtime smoke |
| Agent type | dispatcher |
| Invocation ID | `msea-r24-t2-huggingface-cache-dispatch-2026-07-03` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | this baseline and paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch |

## Claim Boundary

This baseline authorizes only a future worker to run one bounded HuggingFace
pipeline model cache-completion command and record receipt/diagnostic evidence.
It does not authorize parser runtime, document processing, public-sync,
provider/live proof, runtime smoke, workflow-chain completion, production
readiness, stage, commit, or push.
