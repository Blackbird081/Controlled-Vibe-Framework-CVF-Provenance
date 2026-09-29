# CVF Agent Work Order - MSEA-R24-T1 MinerU Model Source Fallback Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-03

Batch ID: MSEA-R24-T1

Dispatch base head: 225228d9

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_WORKER_RETURN_2026-07-03.md`

Companion reference path: `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R24-T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-03.

Do-not-misread notes: this packet authorizes only source verification and route selection for model-source fallback. It does not authorize any cache command, model download, alternate-source execution, parser runtime, document body read, extraction output, public-sync, or production claim.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, R24 roadmap, R23 readiness matrix, MinerU source files named in Source Verification, and all checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create the worker return artifact and companion decision matrix, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Perform a bounded source-verified decision pass that selects or holds the next MinerU model-source route after R23 left cache/config readiness unproven. The worker must choose exactly one allowed route token and must not run a download or parser command.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Capture `executionBaseHead` and initial `git status --short`. | Worker return trace |
| 2 | Read startup, guard, baseline, work order, roadmap, R23 matrix, and checker source. | Source Inventory and Checker Source Read-Ahead Block |
| 3 | Source-verify MinerU model-source options from pinned mirror docs and CLI/helper files. | Source Verification Block |
| 4 | Compare `huggingface`, `modelscope`, `auto`, and `local` against R23 blocker evidence and local-private boundaries. | Companion decision matrix |
| 5 | Select exactly one route token. | `selectedRouteToken` in both worker outputs |
| 6 | Run worker-return fast gate and pre-implementation autorun. | Gate Evidence |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R24-T1 --title "MinerU Model Source Fallback Decision" --date 2026-07-03 --base 225228d9 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders, normalized paths, added R24 dependency release, route tokens, source verification, external absorption blocks, handoff contract, reviewer conversion, and output shape requirements. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| docOnlyNewFields | selectedRouteToken; sourceChoiceDisposition; t2ReleaseDisposition; cacheCommandAuthorization; runtimeSmokeGateDisposition |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the literal required shape. Worker should return to orchestrator only for a source contradiction, forbidden-scope need, or missing authority that makes completion impossible.

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
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; Dependency Release Evidence; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Output Checker Read-Ahead Mandate; Worker Return Packet Shape Contract; External Knowledge Intake Routing row labels; External Absorption Core row labels; Overlap And Novelty Classification dispositions; ledger_terminal=; Corpus verdict bullet; Public Export Disposition |
| gateRunPurpose | Confirmation evidence after checker source read-ahead; gates confirm this work order shape. |
| claimBoundary | Read-ahead covers this work order and paired baseline only; worker must perform separate output-artifact checker read-ahead before writing return/matrix. |

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| R24 roadmap ready | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | `aa2614f6` | SATISFIED - roadmap opens T1 work-order authoring |
| R23 diagnostic acceptance | `docs/reference/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_READINESS_MATRIX_2026-07-03.md` | `e9baa312` | SATISFIED - cache/config readiness remains blocked and needs T1 route decision |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeType | source-verified model-source route decision |
| selected role route | SINGLE_AGENT_MULTI_ROLE route mode for one local agent performing dispatch, worker, reviewer/closer, and session-sync roles in separate phases |
| scope classification | DECISION_ONLY_NO_RUNTIME_EXECUTION |
| risk sensitivity | MEDIUM because T1 gates later cache/runtime work but does not run commands |
| workerRole | delegated worker performs source verification and route selection, then writes uncommitted outputs |
| reviewerRole | reviewer/closer reviews worker outputs and owns material commit if accepted |
| escalation condition | operator checkpoint required if T1 needs cache/download/runtime execution, local model path authority not already available, document processing, public-sync, or production/workflow-chain claim |
| claimBoundary | role routing only; no cache/parser/runtime/public/provider/live/production claim |

## Single-Agent Multi-Role Control Block

| Field | Value |
|---|---|
| selected route mode | SINGLE_AGENT_MULTI_ROLE |
| dispatch role | dispatch author owns GC-018/work-order material commit |
| worker role | worker owns only the two uncommitted output artifacts |
| reviewer role | reviewer/closer owns acceptance, allowed-scope repair, material commit, and session-sync |
| phase separation | dispatch, worker, review, and session-sync must be evidenced as separate phases |
| evidence basis independent of memory | R24 roadmap path, R23 readiness matrix path, pinned MinerU source mirror paths, and command-backed gates; provider memory or chat history is not source authority |
| gate sequence | pre-dispatch before commit; worker-return fast gate and pre-implementation autorun before worker handoff; reviewer-return steward before material commit; session-sync steward after material commit |
| role separation ledger | dispatcher owns this baseline/work order; worker owns only planned uncommitted outputs; reviewer/closer owns material acceptance and session-sync |
| self-review boundary | any same-agent reviewer/closer phase must re-run gates and may repair only allowed-scope evidence/shape defects; broader scope returns to operator |
| commit boundary | worker must not stage, commit, or push |
| escalation conditions | operator escalation for cache/download/runtime execution, local model path authority gap, parser/service/document-body action, public-sync, or production/workflow-chain claim |
| claim boundary | role-control only; no cache/runtime/provider/public/package behavior claim |

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator request | operator approved R24 direction and asked Codex to handle T1-T4 with governed dependencies | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` at `aa2614f6` | ACCEPT |
| Baseline | `docs/baselines/CVF_GC018_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_2026-07-03.md` | ACCEPT |
| Work order | this packet | ACCEPT |

## Agent Roles

| Role | Responsibility |
|---|---|
| Dispatcher | owns baseline/work-order authoring and pre-dispatch gates |
| Worker | creates only the named worker return and companion decision matrix, without commit |
| Reviewer/closer | reviews worker outputs, repairs allowed-scope shape defects, commits material if accepted, then performs session-sync |

## Required First Reads

| Path | Purpose |
|---|---|
| `CVF_SESSION_MEMORY.md` | startup front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | compact current state |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | canonical current state |
| `AGENT_HANDOFF_V34_2026-07-03.md` | active handoff |
| `docs/reference/guard_orientation/README.md` | guard routing |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | literal-format traps |
| paired baseline and this work order | governing dispatch packet |
| R24 roadmap and R23 readiness matrix | dependency and route evidence |
| MinerU source files in Source Verification Block | model-source facts |

## Pre-Flight Checks

| Check | Required evidence |
|---|---|
| Capture execution base | `git rev-parse --short HEAD` before edits |
| Confirm worktree | `git status --short --untracked-files=all` before edits |
| Confirm no output collision | planned worker return and companion reference absent before writing |
| Read output checkers | worker records checker-source read-ahead for both output artifacts |

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reviews/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_WORKER_RETURN_2026-07-03.md` | worker | allowed |
| `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md` | worker | allowed |
| Any other governed path | reviewer/dispatcher only through fresh authorization | forbidden to worker |
| Git stage/commit/push | reviewer/closer only | forbidden to worker |

## Evidence Requirements

| Requirement | Evidence |
|---|---|
| Source option comparison | companion matrix compares `huggingface`, `modelscope`, `auto`, and `local` |
| Route selection | one allowed route token appears in both outputs |
| T2 release or hold | worker records `t2ReleaseDisposition` with reason |
| No command execution | command evidence shows no cache/download/parser command run |
| No commit | `git status --short --untracked-files=all` shows untracked worker outputs only |
| Gates | worker-return fast gate and pre-implementation autorun evidence |

## Acceptance Criteria

| Criterion | Evidence | Status |
|---|---|---|
| Worker selected exactly one route token | worker return and companion matrix | REQUIRED |
| No cache/runtime command was run | command evidence and claim boundary | REQUIRED |
| Source verification is current | Source Verification Block in worker outputs | REQUIRED |
| T2 dependency is explicit | selected route and t2 release disposition | REQUIRED |
| Worker did not commit | git status evidence | REQUIRED |

## Review Gate

Reviewer/closer must run `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBase> --head HEAD --enforce` before material commit. If the worker selects a T2-opening token, reviewer/closer must ensure the next move says fresh T2 GC-018/work-order authoring, not direct cache execution.

## Closure Checklist

| Item | Required disposition |
|---|---|
| Worker return reviewed | PASS or BLOCKED with reason |
| Companion matrix reviewed | PASS or BLOCKED with reason |
| No forbidden command | PASS or BLOCKED with reason |
| Route token accepted | PASS or BLOCKED with reason |
| Material commit | reviewer/closer only |
| Session-sync | after material commit if next move changes |

## Operator Checkpoint

Operator checkpoint is required before any T2 work order that runs a cache command if T1 selects local model path prep, requires broader network/download scope than one bounded command, or requires any parser/document/runtime execution. T1 itself does not require another operator checkpoint unless source evidence contradicts the roadmap.

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

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T1 must choose model-source route before T2 | Execution Plan; Allowed Route Tokens | `selectedRouteToken` | worker-return fast gate plus reviewer check | PASS |
| T1 must not run cache command | Forbidden Scope; Claim Boundary | `cacheCommandAuthorization` | worker return command evidence | PASS |
| T2 remains dependent | Allowed Route Tokens; Reviewer Closure Conversion | `t2ReleaseDisposition` | reviewer/closer checks route token | PASS |
| Runtime smoke remains blocked | Forbidden Scope; Claim Boundary | `runtimeSmokeGateDisposition` | pre-implementation autorun | PASS |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned output path existence | `Test-Path` returned False for the T1 baseline, work order, worker return, and companion decision matrix before authoring. | SAFE_TO_CREATE |
| Token search | `rg -n "MSEA_R24_T1|MSEA-R24-T1|MODEL_SOURCE_FALLBACK_DECISION|MinerU Model Source Fallback Decision" docs CVF_SESSION AGENT_HANDOFF_V34_2026-07-03.md .private_reference/source_mirrors/INDEX.md` found only roadmap/session route mentions, no prior T1 dispatch artifacts. | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | MSEA-R24-T1 is released by accepted R24 roadmap and current next-move surfaces. | SAFE_TO_CREATE |

## Allowed Route Tokens

Worker must select exactly one:

| Token | Meaning |
|---|---|
| SELECT_HUGGINGFACE_CACHE_RECOVERY | Source evidence supports opening T2 for one bounded HuggingFace cache-completion command. |
| SELECT_MODELSCOPE_SUPERVISED_RETRY | Source evidence supports opening T2 for one better-supervised ModelScope retry. |
| SELECT_AUTO_SOURCE_PROBE | Source evidence supports opening T2 for an auto probe without setting `MINERU_MODEL_SOURCE=auto`. |
| SELECT_LOCAL_MODEL_PATH_PREP | Source evidence supports opening a local-model-path prep tranche before cache/runtime work. |
| HOLD_ALL_CACHE_RECOVERY | No source route is ready or permitted. |

## Forbidden Scope

Worker must not run model download, cache retry, alternate-source command, parser/OCR/VLM/API/router/Gradio/Docker/WSL execution, local service startup, source document copy/import, document body read, extraction output, provider/live proof, public-sync, RAG/S3, schema/writer/adapter/checker implementation, package reinstall, Web/MCP/model-router/action-authority work, benchmark, document-truth, extraction-accuracy, legal advice quality, current-law correctness, runtime smoke, workflow-chain completion, production readiness, stage, commit, or push.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_WORKER_RETURN_2026-07-03.md` | Create worker return with selected route, evidence, gates, no-commit status, and exact changed set. |
| `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md` | Create companion decision matrix comparing `huggingface`, `modelscope`, `auto`, and `local` against R23 blocker evidence and route tokens. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher creates packet; worker returns uncommitted outputs; reviewer/closer owns material commit and session-sync |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=225228d9; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | baseline and work order only for dispatch; worker may create only the two planned outputs |
| traceScope(phase, actor) | dispatcher trace in this packet; worker trace in return and matrix; reviewer trace in closure/session-sync |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | MSEA-R24-T1 only; T2/T3/T4 require separate release evidence and work orders |
| nextMoveSurfaces | reviewer/closer updates session surfaces only after accepting worker return |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | Optional; prefer repairing evidence in the worker return per gotcha 30. |
| reviewerOwnedClosurePaths | worker return and companion decision matrix |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
|---|---|
| worker return under reviews | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| companion reference under reference | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_WORKER_RETURN_2026-07-03.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section names without the heading prefix. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned MinerU source mirror plus accepted R23 diagnostic evidence -> T1 model-source fallback decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this work order and paired baseline |
| Disposition | ROUTED_TO_GOVERNED_DECISION_ONLY_WORK_ORDER |
| Claim boundary | source verification and route decision only; no cache command, alternate-source download, parser runtime, public-sync, or production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Enumeration command | `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU docs/reviews docs/reference docs/roadmaps` plus targeted `rg -n` source-verification queries |
| Manifest artifact or inline manifest | Source Verification Block |
| Processing ledger artifact or inline ledger | worker return and companion decision matrix |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | R24 roadmap, R23 readiness matrix, pinned MinerU source mirror |
| Unresolved items | source route selection and T2 release decision |
| Completion claim boundary | decision-only dispatch; no runtime, download, parser, document-body, extraction, source import, provider/live proof, public-sync, schema/writer/adapter/checker work |

ledger_terminal=READ for R24/R23/MinerU source evidence; ledger_terminal=DEFERRED for T2/T3/T4 execution; ledger_terminal=REJECTED for direct runtime or workflow-chain claims in T1.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| R24 T1 release | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | CONFIRMED_EXISTING | roadmap already opens T1 | dispatch |
| R23 cache blocker | `docs/reference/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_READINESS_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | no new runtime evidence | cite |
| MinerU source options | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | ENRICH_EXISTING | T1 compares options for next route | adapt |
| Cache command execution | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | REJECT_DIRECT_IMPORT | T2 owns command execution only if released | defer |
| Runtime smoke | `docs/reference/CVF_MSEA_R23_T1_MINERU_MODELSCOPE_CACHE_DIAGNOSTIC_RESOLUTION_AND_ALTERNATE_SOURCE_READINESS_MATRIX_2026-07-03.md` | REJECT_DIRECT_IMPORT | T3 remains blocked | defer |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationStorageAction | N/A with reason: this work order does not create, split, relocate, or refactor durable governance foundation files |
| generatedAggregateDisposition | N/A with reason: no generated aggregate is edited by this material dispatch |
| storageLayoutBoundary | dispatch packet and worker-owned outputs only |
| claimBoundary | no storage layout, registry topology, or foundation refactor claim |

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git status --short --untracked-files=all
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R24-T1 MinerU Model Source Fallback Decision dispatch, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, source reads, dispatch scaffold helper, `apply_patch`, governance gates |
| Target paths | this work order and paired GC-018 baseline |
| Allowed scope source | R24 roadmap material commit `aa2614f6`; session-sync commit `225228d9` |
| Before status evidence | clean worktree before dispatch authoring: `git status --short --untracked-files=all` returned empty; planned T1 paths absent |
| After status evidence | baseline and work order pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no cache/runtime/provider/public/package behavior |
| Agent type | dispatcher |
| Invocation ID | `msea-r24-t1-model-source-fallback-decision-dispatch-2026-07-03` |
| Expected manifest | this work order and paired baseline |
| Actual changed set | this work order and paired baseline |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | MSEA-R24-T1 decision-only source-route dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed. |
| invocationBoundary | local governed dispatch authoring only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | dispatch packet and future worker decision evidence only |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router/cache execution/parser/document behavior without fresh source-verified authorization |

## Claim Boundary

This work order authorizes only source verification and route selection for MSEA-R24-T1. It does not authorize cache mutation, model download, alternate-source command execution, parser/OCR/VLM/API/router/Gradio/Docker/WSL execution, local service startup, source document copy/import, document body read, extraction output, provider/live proof, public-sync, schema/writer/adapter/checker implementation, runtime smoke, workflow-chain completion, production readiness, stage, commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet; no public-sync export is authorized.
