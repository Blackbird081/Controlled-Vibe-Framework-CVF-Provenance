# CVF GC-018 Baseline - MSEA-R24-T1 MinerU Model Source Fallback Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-03

Batch ID: MSEA-R24-T1

Dispatch base head: 225228d9

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role, not a provider-specific agent

## Purpose

Dispatch a source-verified, decision-only worker tranche to choose the next MinerU model-source route after R23 held runtime smoke for absent config/cache receipt. This baseline authorizes no cache command or parser execution; it only authorizes evidence review and route selection for T2.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R24-T1 --title "MinerU Model Source Fallback Decision" --date 2026-07-03 --base 225228d9 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders, normalized output paths, added R24 roadmap dependency release, source verification, external absorption blocks, and route tokens. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| docOnlyNewFields | selectedRouteToken; sourceChoiceDisposition; t2ReleaseDisposition; cacheCommandAuthorization; runtimeSmokeGateDisposition |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | Still apply scaffold-first, checker read-ahead, literal gotchas, and worker-output shape mandates from active guard orientation. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; Dependency Release Evidence; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; External Knowledge Intake Routing row labels; External Absorption Core row labels; Overlap And Novelty Classification dispositions; ledger_terminal=; Corpus verdict bullet; Public Export Disposition |
| gateRunPurpose | Confirmation evidence after checker source read-ahead; gates confirm this dispatch packet shape. |
| claimBoundary | Read-ahead covers this baseline and paired work order only; no worker output, cache command, runtime, public-sync, or production behavior is claimed. |

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| R24 roadmap ready | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | `aa2614f6` | SATISFIED - roadmap status is `ROADMAP_READY_FOR_MSEA_R24_T1_GC018_AND_WORK_ORDER_AUTHORING` |
| R23 diagnostic acceptance | `docs/reference/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_READINESS_MATRIX_2026-07-03.md` | `e9baa312` | SATISFIED - selected `HOLD_PENDING_MODELSCOPE_RETRY_OR_NETWORK_DIAGNOSTIC` and kept runtime smoke blocked |
| Session next-move freshness | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V34_2026-07-03.md` | `225228d9` | SATISFIED - next move routes to MSEA-R24-T1 work-order authoring only |

## Decision / Baseline / Proposed Tranche

| Field | Value |
|---|---|
| Decision | Dispatch MSEA-R24-T1 as a decision-only no-commit worker tranche |
| Baseline | R24 roadmap plus R23 cache/config blocker evidence |
| Proposed tranche | Worker creates one worker return and one companion decision matrix, selects exactly one allowed route token, and does not run cache/runtime commands |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R24 roadmap opens T1 model-source fallback decision only. | VALUE_SET | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | line 5 and lines 132-143 | `ROADMAP_READY_FOR_MSEA_R24_T1_GC018_AND_WORK_ORDER_AUTHORING` | R24 roadmap | ACCEPT |
| R23 selected diagnostic hold and kept cache/config not ready. | VALUE_SET | `docs/reference/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_READINESS_MATRIX_2026-07-03.md` | lines 9-17 | `HOLD_PENDING_MODELSCOPE_RETRY_OR_NETWORK_DIAGNOSTIC` | R23 readiness matrix | ACCEPT |
| MinerU supports HuggingFace, ModelScope, and local model-source choices. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 3 and line 12 | `MINERU_MODEL_SOURCE` | MinerU model-source documentation | ACCEPT |
| MinerU docs say environment value `auto` should not be set directly. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 12 | `auto` | MinerU model-source documentation | ACCEPT |
| MinerU completed download writes model path and source into config. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 44 | `mineru.json` | MinerU model-source documentation | ACCEPT |
| MinerU download CLI supports pipeline model type and source option. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 94-117 | `download_models` | MinerU model download CLI | ACCEPT |
| MinerU utility defines remote sources as HuggingFace and ModelScope. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | line 20 | `REMOTE_MODEL_SOURCES` | MinerU model download utility | ACCEPT |
| MinerU utility can resolve local source. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 233-234 | `resolve_model_source` | MinerU model download utility | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned output path existence | `Test-Path` returned False for the T1 baseline, work order, worker return, and companion decision matrix before authoring. | SAFE_TO_CREATE |
| Token search | `rg -n "MSEA_R24_T1|MSEA-R24-T1|MODEL_SOURCE_FALLBACK_DECISION|MinerU Model Source Fallback Decision" docs CVF_SESSION AGENT_HANDOFF_V34_2026-07-03.md .private_reference/source_mirrors/INDEX.md` found only roadmap/session route mentions, no prior T1 dispatch artifacts. | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | MSEA-R24-T1 is released by accepted R24 roadmap and current next-move surfaces. | SAFE_TO_CREATE |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned MinerU source mirror plus accepted R23 diagnostic evidence -> T1 model-source fallback decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this baseline and paired work order |
| Disposition | ROUTED_TO_GOVERNED_DECISION_ONLY_WORK_ORDER |
| Claim boundary | source verification and route decision only; no cache command, alternate-source download, parser runtime, public-sync, or production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Enumeration command | `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU docs/reviews docs/reference docs/roadmaps` plus targeted `rg -n` source-verification queries |
| Manifest artifact or inline manifest | Source Verification Block in this baseline and paired work order |
| Processing ledger artifact or inline ledger | paired worker return and companion decision matrix to be created by worker |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | R24 roadmap, R23 readiness matrix, pinned MinerU source mirror |
| Unresolved items | source route selection and T2 release decision |
| Completion claim boundary | decision-only dispatch; no runtime, download, parser, document-body, extraction, source import, provider/live proof, public-sync, schema/writer/adapter/checker work |

ledger_terminal=READ for R24/R23/MinerU source evidence; ledger_terminal=DEFERRED for T2/T3/T4 execution; ledger_terminal=REJECTED for direct runtime or workflow-chain claims in T1.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| R24 roadmap | T1 must decide model-source route first | DOCTRINE_ADAPTED | T1 work order | dispatch worker | no cache command |
| R23 readiness matrix | no config/cache receipt | DOCTRINE_ADAPTED | T1 decision matrix | preserve blocker | no runtime smoke |
| MinerU model-source docs | supported source values and config writeback boundary | RUNTIME_CANDIDATE | T1 decision matrix | choose route or hold | no download in T1 |
| R22 venv evidence | package activation may support later T2 | PACKAGE_CANDIDATE | T2 candidate only | defer | no reinstall |
| Worker output gates | decision matrix must carry exact route token and non-claims | CHECKER_CANDIDATE | worker return/matrix | run fast gates | no checker implementation |
| Direct alternate-source execution | out of T1 scope | REJECT_DIRECT_IMPORT | claim boundary | reject | no HuggingFace/local command |
| Already-owned R21 package blocker | superseded by R22/R23 evidence | NO_PACKAGE_OR_RUNTIME_VALUE | predecessor surfaces | cite only | no new package value |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| R24 T1 release | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | CONFIRMED_EXISTING | roadmap already opens T1 | dispatch |
| R23 cache blocker | `docs/reference/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_READINESS_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | no new runtime evidence | cite |
| MinerU source options | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | ENRICH_EXISTING | T1 compares options for next route | adapt |
| Cache command execution | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | REJECT_DIRECT_IMPORT | T2 owns command execution only if released | defer |
| Runtime smoke | `docs/reference/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_READINESS_MATRIX_2026-07-03.md` | REJECT_DIRECT_IMPORT | T3 remains blocked | defer |

## Corpus Completeness And Report Integrity

- Corpus task class: decision-only model-source fallback work-order dispatch.
- Corpus root: R24 roadmap, R23 readiness matrix, and pinned MinerU model-source files.
- Snapshot time: 2026-07-03 dispatch authoring.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU docs/reviews docs/reference docs/roadmaps` plus targeted `rg -n` source-verification queries.
- Manifest artifact or inline manifest: Source Verification Block in this baseline and paired work order.
- Manifest hash: N/A with reason: this dispatch consumes governed artifacts and pinned source files, not a new file corpus.
- Processing ledger artifact or inline ledger: worker return and companion decision matrix required by paired work order.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE, ADAPTED, REJECTED, NO_NEW_VALUE.
- Reconciliation: manifest=R24/R23/MinerU source evidence; ledger_terminal=READ/ADAPTED/DEFERRED/REJECTED/NO_NEW_VALUE for dispatch scope; exclusions=cache command, runtime smoke, document body, extraction output, public-sync, production claims; unresolved=0 for dispatch authoring.
- Unresolved files: none for dispatch authoring scope.
- Declared exclusions: cache command, alternate-source download, runtime smoke, document body, extraction output, public-sync, provider/live proof, production claims.
- Unreadable or unsupported files: none identified for this dispatch authoring.
- Aggregation check: PASS - accepted owner surfaces are cited instead of regenerated into a new corpus aggregate.
- Drift check: PASS - R23 accepted matrix still records absent config/cache receipt.
- Output traceability: worker return and companion decision matrix are named in the paired work order.
- Adversarial verification: direct runtime smoke, direct cache command, and workflow-chain completion are rejected for T1.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Evidence / Verification

| Evidence item | Result |
|---|---|
| Dispatch base head | `225228d9` |
| Planned path absence | baseline, work order, worker return, and companion decision matrix were absent before authoring |
| ADIF resolver | returned zero entries and disclosed `NONE_RETURNED` |
| Pre-dispatch target | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 225228d9 --head HEAD` |

## Claim Boundary

This baseline authorizes only a source-verified decision worker for MSEA-R24-T1. It does not authorize cache mutation, model download, alternate-source command execution, parser/OCR/VLM/API/router/Gradio/Docker/WSL execution, local service startup, source document copy/import, document body read, extraction output, provider/live proof, public-sync, schema/writer/adapter/checker implementation, runtime smoke, workflow-chain completion, or production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet; no public-sync export is authorized.
