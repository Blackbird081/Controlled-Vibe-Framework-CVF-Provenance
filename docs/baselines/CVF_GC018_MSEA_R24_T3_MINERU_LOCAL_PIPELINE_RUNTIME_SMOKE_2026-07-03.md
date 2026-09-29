# CVF GC-018 Baseline - MSEA-R24-T3 MinerU Local Pipeline Runtime Smoke

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-03

Batch ID: MSEA-R24-T3

Dispatch base head: 71737425

Commit mode: WORKER_MUST_NOT_COMMIT

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Purpose

Dispatch one bounded local MinerU CLI runtime smoke after accepted MSEA-R24-T2A
recorded `CONFIG_CACHE_RECEIPT_READY` and `CONFIG_WRITTEN_ABSOLUTE_PATH`.
This baseline releases only a one-input, private, local runtime smoke and
receipt/diagnostic capture; it does not claim extraction accuracy, document
truth, legal advice quality, current-law correctness, workflow-chain
completion, public readiness, or production readiness.

## Scope

| Field | Value |
|---|---|
| In scope | MSEA-R24-T3 dispatch packet for one local MinerU CLI smoke using the accepted T2A config/cache receipt and one authorized Candidate Group A DOCX |
| Out of scope | second smoke command, model download/cache mutation, public-sync, provider/live proof, RAG/S3, schema/writer/adapter/checker implementation, benchmark, extraction-accuracy, legal-quality, workflow-chain, production claim |
| Owner | dispatcher for packet authoring; worker for future uncommitted runtime smoke evidence; reviewer/closer for material acceptance |

## Decision / Baseline / Proposed Tranche

| Field | Value |
|---|---|
| Decision | Dispatch T3 only after T2A selected `CONFIG_CACHE_RECEIPT_READY` and `CONFIG_WRITTEN_ABSOLUTE_PATH` |
| Baseline | accepted T2A config/cache receipt, R22 ignored MinerU venv, MinerU CLI source/docs, and R17 Candidate Group A private-test authorization |
| Proposed tranche | MSEA-R24-T3 MinerU local pipeline runtime smoke |
| Dispatch route | WORKER_MUST_NOT_COMMIT |

## Evidence / Verification

| Evidence item | Verification |
|---|---|
| Dispatch base | `71737425` captured after separate session-wording and handoff-marker hygiene commits |
| Pre-dispatch target | this baseline and paired work order only |
| Runtime execution | NOT_RUN_BY_DISPATCHER |
| Verification status | pending pre-dispatch autorun rerun after allowed-scope repairs |

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| R24 roadmap T3 dependency | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | `aa2614f6` | SATISFIED - T3 opens only after config/cache receipt |
| T2A accepted config/cache receipt | `docs/reviews/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_WORKER_RETURN_2026-07-03.md` | `b53786d9` | SATISFIED - selected `CONFIG_CACHE_RECEIPT_READY` |
| T2A readiness matrix | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | `b53786d9` | SATISFIED - config writeback receipt is `CONFIG_WRITTEN_ABSOLUTE_PATH` |
| Session sync | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `71b10f74` | SATISFIED - next allowed move routes to T3 work-order authoring |
| Handoff/session lifecycle wording | `AGENT_HANDOFF_V35_2026-07-03.md` and active session generated state | `5af0d29f`; `71737425` | SATISFIED - lifecycle wording repair prevents closed T2A from being read as closed T3 and handoff marker records the repair head |
| Candidate Group A private-test boundary | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | `eb127b7f` | SATISFIED - local private testing only; committed evidence must be metadata/excerpt-minimal |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | N/A with reason: resolver returned no defects for this dispatcher pre-dispatch query |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R24-T3 --title "MinerU Local Pipeline Runtime Smoke" --date 2026-07-03 --base a6d08fd5 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| finalDispatchBaseAdjustment | Updated dispatch base to `71737425` after separate lifecycle session-wording and handoff-marker hygiene commits. |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled T3 dependency release evidence, source verification, runtime-smoke boundary, Candidate Group A privacy boundary, and worker-output contract. |
| checkerReadAheadConfirmation | Checker Source Read-Ahead Block lists dispatch, worker-output, absorption, operation-trace, and delta-claim checkers. |
| docOnlyNewFields | `runtimeSmokeReceiptDisposition`; `runtimeSmokeOutputBoundary`; `candidateGroupASmokeInput` |
| claimBoundary | Dispatch authoring provenance only; no runtime smoke has been run by this baseline. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; Dependency Release Evidence; Negative Search And Collision Discipline; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; External Knowledge Intake Routing row labels; External Absorption Core row labels; External Absorption Value Conversion Matrix columns; Overlap And Novelty Classification dispositions; ledger_terminal=; Corpus verdict bullet; Current Runtime Freshness Verification; Public Export Disposition |
| gateRunPurpose | Confirmation evidence after checker source read-ahead; gates confirm this baseline and paired work order shape. |
| claimBoundary | Read-ahead covers this dispatch packet; worker output artifacts require their own checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R24 roadmap allows T3 only after config/cache receipt. | VALUE_SET | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | T1-T4 Dependency Contract | `MSEA-R24-T3` | R24 roadmap | ACCEPT |
| T2A selected config/cache receipt ready. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | top route fields | `CONFIG_CACHE_RECEIPT_READY` | T2A readiness matrix | ACCEPT |
| T2A config writeback receipt is absolute-path written. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | top receipt fields | `CONFIG_WRITTEN_ABSOLUTE_PATH` | T2A readiness matrix | ACCEPT |
| MinerU command-line parsing supports input path and output directory. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md` | Quick Usage via Command Line | `mineru -p <input_path> -o <output_path>` | MinerU usage docs | ACCEPT |
| MinerU CLI launches a temporary local API when `--api-url` is omitted. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md` | Quick Usage via Command Line tip | `--api-url` omitted | MinerU usage docs | ACCEPT |
| MinerU CLI exposes `--path`, `--output`, `--backend`, `--method`, `--start`, and `--end`. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/client.py` | lines 1037-1147 | `main` click options | MinerU CLI client | ACCEPT |
| MinerU backend choices include `pipeline`. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | top constants | `BACKEND_PIPELINE` | backend options | ACCEPT |
| MinerU config reader honors `MINERU_TOOLS_CONFIG_JSON`. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/config_reader.py` | top config constant and `read_config` | `MINERU_TOOLS_CONFIG_JSON` | config reader | ACCEPT |
| MinerU local model source resolves to configured `models-dir`. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 211-249 and 288-295 | `resolve_model_source`; `get_local_models_dir` | model download utility | ACCEPT |
| Candidate Group A is authorized for local private CVF testing only with metadata/redaction/excerpt-minimal committed evidence. | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | Operator Authorization Boundary | `Candidate Group A` | R17 intake ledger | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned T3 baseline path absence | `Test-Path docs\baselines\CVF_GC018_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_2026-07-03.md` returned `False` before authoring | SAFE_TO_CREATE |
| Planned T3 work order path absence | `Test-Path docs\work_orders\CVF_AGENT_WORK_ORDER_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_2026-07-03.md` returned `False` before authoring | SAFE_TO_CREATE |
| Token search | `rg -n "MSEA_R24_T3|MSEA-R24-T3|LOCAL_PIPELINE_RUNTIME_SMOKE|pipeline runtime smoke" docs CVF_SESSION AGENT_HANDOFF_V35_2026-07-03.md` found only roadmap/session next-move references and predecessor seeds, no prior T3 dispatch artifact | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | T3 is a dependent child of accepted T2A and current next-move surfaces | SAFE_TO_CREATE |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | This baseline is dispatch authoring only. The future worker may run one local MinerU CLI smoke only after this packet is committed and session-sync routes execution. |
| requiredFutureAction | Worker must capture executionBaseHead, run the single allowed command or an allowed preflight hold, and create uncommitted worker return plus companion readiness matrix. |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned MinerU source mirror plus accepted T2A local receipt plus R17 private-test boundary -> T3 local runtime-smoke dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this baseline and paired work order |
| Disposition | ADAPT: convert accepted config/cache receipt into one bounded private local runtime-smoke work order |
| Claim boundary | dispatch only; no parser result, extraction quality, public-sync, or production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA owner surfaces |
| Enumeration command | filesystem-backed direct reads of cited T2A/R17/MinerU source files |
| Manifest artifact or inline manifest | inline table: Source Verification Block |
| Processing ledger artifact or inline ledger | inline table: Dependency Release Evidence and paired work order |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | R24 roadmap, T2A accepted artifacts, R17 private-test ledger, pinned MinerU CLI/config source |
| Unresolved items | actual smoke result, runtime diagnostic, output receipt, T4 release |
| Completion claim boundary | dispatch only; no runtime smoke executed by dispatcher |

ledger_terminal=READ for cited source evidence; ledger_terminal=ADAPTED for T3 dispatch; ledger_terminal=DEFERRED for worker result and T4; ledger_terminal=REJECTED for direct workflow-chain completion from T3 dispatch.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| T2A readiness matrix | config/cache receipt exists | RUNTIME_CANDIDATE | T3 work order | dispatch one bounded smoke | one command only |
| MinerU CLI docs/source | `mineru -p ... -o ... -b pipeline` command surface | DOCTRINE_ADAPTED | T3 work order | source-verified worker command | no API/router/gradio lane |
| MinerU config source | local model source reads configured `models-dir` | RUNTIME_CANDIDATE | T3 worker | set process-local env vars | no model download |
| R17 private-test ledger | Candidate Group A local private authorization | DOCTRINE_ADAPTED | T3 privacy boundary | use one smaller file as private input | no source copy/import |
| T4 workflow-chain policy | requires T3 smoke evidence | CHECKER_CANDIDATE | future T4 | defer | no checker implementation |
| MinerU package state | local ignored venv already exists from prior accepted work | PACKAGE_CANDIDATE | T3 worker preflight | verify command presence only | no package mutation |
| Direct workflow-chain completion | not supported by dispatch-only evidence | REJECT_DIRECT_IMPORT | future T4 | reject until accepted smoke receipt | no workflow-chain claim |
| Public export | not authorized | NO_PACKAGE_OR_RUNTIME_VALUE | private provenance only | none | no public-sync |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| T2A config/cache receipt | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | releases T3 authoring | dispatch |
| MinerU CLI runtime command | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/client.py` | ENRICH_EXISTING | exact local command surface for smoke | adapt |
| Candidate Group A private input | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | CONFIRMED_EXISTING | reused as one private smoke input without content quotation | cite |
| Workflow-chain completion | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | REJECT_DIRECT_IMPORT | T4 only after accepted T3 evidence | defer |

## Corpus Completeness And Report Integrity

- Corpus task class: T3 dispatch for one bounded local MinerU runtime smoke.
- Corpus root: accepted T2A artifacts, R17 private-test authorization, and pinned MinerU CLI/config source.
- Snapshot time: 2026-07-03 dispatch authoring.
- Enumeration command: filesystem-backed direct reads of cited source files and negative-search commands above.
- Manifest artifact or inline manifest: Source Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded dispatch source set, not a new corpus snapshot.
- Processing ledger artifact or inline ledger: Dependency Release Evidence and paired work order.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=T2A/R17/MinerU source evidence; ledger_terminal=READ/ADAPTED/DEFERRED/REJECTED; exclusions=manual document body read, content quotes, second runtime command, public-sync, provider/live proof, production claims; unresolved=0 for dispatch authoring.
- Unresolved files: none for dispatch authoring.
- Declared exclusions: runtime execution by dispatcher, second smoke command, model download, document-body quotation, public-sync, provider/live proof, production readiness.
- Unreadable or unsupported files: none identified for dispatch authoring.
- Aggregation check: PASS - accepted owner surfaces are cited.
- Drift check: PASS - current next-move surfaces route T3 authoring after T2A.
- Output traceability: paired T3 work order names worker return and readiness matrix.
- Adversarial verification: direct T4 workflow-chain completion and legal/extraction-quality claims are rejected.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or recovery requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T3 requires config/cache receipt | Dependency Release Evidence | T2A selected route and receipt fields | pre-dispatch gate | PASS |
| T3 local runtime smoke must be bounded | Allowed Command in work order | command count and log path | worker return | PASS |
| T4 remains gated | Claim Boundary | runtimeSmokeReceiptDisposition | reviewer check | PASS |
| Privacy boundary survives smoke | Candidate Group A Boundary in work order | metadata-only committed evidence | reviewer check | PASS |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher creates packet; worker returns uncommitted outputs; reviewer/closer owns material commit and session-sync |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=71737425; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | baseline and work order only for dispatch; worker may create only two planned outputs plus ignored runtime receipts |
| traceScope(phase, actor) | dispatcher trace in this packet; worker trace in return/matrix; reviewer trace in closure/session-sync |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | MSEA-R24-T3 only; T4 requires separate accepted T3 evidence and work order |
| nextMoveSurfaces | reviewer/closer updates session surfaces only after accepting worker return |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R24-T3 dispatch for one bounded local MinerU runtime-smoke work order |
| claimDisposition | CLAIM_REJECTED: dispatch does not execute the smoke command or claim runtime success |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker must create smoke receipt or diagnostic |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action in dispatch |
| invocationBoundary | local governed dispatch authoring only |
| interceptionBoundary | no provider, Web, MCP, adapter, model-router, action-authority, or production route interception claim |
| claimLanguage | work-order dispatch and future worker receipt only |
| forbiddenExpansion | no second smoke, model download, public-sync, provider/live proof, RAG/S3, schema/writer/adapter/checker implementation, benchmark, extraction-accuracy, legal-quality, workflow-chain completion, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet for local Candidate Group A smoke;
no public-sync export is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R24-T3 local pipeline runtime smoke dispatch, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, source reads, scaffold helper, apply_patch, governance gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | T2A material commit `b53786d9`; session-sync commit `71b10f74`; handoff marker `a6d08fd5`; lifecycle wording commit `5af0d29f`; handoff marker commit `71737425` |
| Before status evidence | clean worktree at `71737425` before final dispatch gate rerun |
| After status evidence | baseline and work order pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no runtime smoke executed by dispatch |
| Agent type | dispatcher |
| Invocation ID | `msea-r24-t3-local-pipeline-runtime-smoke-dispatch-2026-07-03` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | this baseline and paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch |

## Claim Boundary

This baseline authorizes only a future worker to run one bounded local MinerU
CLI smoke using accepted config/cache evidence and one authorized private test
input, then record receipt or diagnostic evidence. It does not authorize a
second command, cache mutation, model download, public-sync, provider/live
proof, RAG/S3, schema/writer/adapter/checker implementation, document-truth
claim, extraction-accuracy claim, legal advice quality claim, current-law
correctness claim, workflow-chain completion, production readiness, stage,
commit, or push.
