# CVF GC-018 Baseline - MSEA-R24-T3A MinerU Path Quoting Safe Local Pipeline Rerun

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-04

Batch ID: MSEA-R24-T3A

Dispatch base head: 5a43cebe

Commit mode: WORKER_MUST_NOT_COMMIT

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Purpose

Dispatch one bounded rerun of the MSEA-R24-T3 local MinerU pipeline smoke after
accepted T3 evidence selected `SMOKE_FAIL_DIAGNOSTIC_RECORDED` for a Windows
path-quoting wrapper failure. This baseline releases only a quoting-safe rerun
packet and does not claim parser success, extraction accuracy, document truth,
legal advice quality, current-law correctness, workflow-chain completion,
public readiness, or production readiness.

## Scope

| Field | Value |
|---|---|
| In scope | MSEA-R24-T3A dispatch packet for one path-quoting-safe local MinerU CLI rerun using the accepted T2A config/cache receipt and the same authorized Candidate Group A DOCX |
| Out of scope | second rerun, model download/cache mutation, ModelScope, VLM/hybrid/http-client/router/Gradio/Docker/WSL, service outside the single CLI process, document body read by agent, content quote, public-sync, provider/live proof, RAG/S3, schema/writer/adapter/checker/package/Web/MCP/model-router/action-authority work, benchmark, workflow-chain claim, production claim |
| Owner | dispatcher for packet authoring; worker for future uncommitted runtime evidence; reviewer/closer for material acceptance and session-sync |

## Decision / Baseline / Proposed Tranche

| Field | Value |
|---|---|
| Decision | Dispatch T3A only because T3 failed before document processing due local invocation argument quoting |
| Baseline | accepted T3 diagnostic closure, accepted T2A config/cache receipt, R22 ignored MinerU venv, MinerU CLI/config source, and R17 Candidate Group A private-test authorization |
| Proposed tranche | MSEA-R24-T3A MinerU path-quoting-safe local pipeline rerun |
| Dispatch route | WORKER_MUST_NOT_COMMIT |

## Evidence / Verification

| Evidence item | Verification |
|---|---|
| Dispatch base | `5a43cebe` captured after MSEA-R24-T3 diagnostic session-sync |
| Pre-dispatch target | this baseline and paired work order only |
| Runtime execution | NOT_RUN_BY_DISPATCHER |
| Verification status | pending pre-dispatch autorun after this packet is authored |

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| MSEA-R24-T3 accepted diagnostic closure | `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md` selected `SMOKE_FAIL_DIAGNOSTIC_RECORDED` and recorded `LOCAL_INVOCATION_ARGUMENT_QUOTING` | `4fe1b044` | SATISFIED |
| T3 readiness matrix held T4 | `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md` records no output receipt and `NOT_RELEASED_WITH_REASON` for T4 | `4fe1b044` | SATISFIED |
| T3 session sync routes T3A authoring | `CVF_SESSION/ACTIVE_SESSION_STATE.json` and `AGENT_HANDOFF_V35_2026-07-03.md` route next move to fresh T3A work-order authoring | `5a43cebe` | SATISFIED |
| T2A accepted config/cache receipt | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` records config/cache receipt ready | `b53786d9` | SATISFIED |
| Candidate Group A private-test boundary | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` permits local private testing with metadata/redaction/excerpt-minimal committed evidence only | `eb127b7f` | SATISFIED |

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
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R24-T3A --title "MinerU Path Quoting Safe Local Pipeline Rerun" --date 2026-07-04 --base 5a43cebe --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R24-T3 diagnostic closure at 4fe1b044 selected SMOKE_FAIL_DIAGNOSTIC_RECORDED" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled dependency release evidence, source verification, quoting-safe rerun boundary, Candidate Group A privacy boundary, and worker-output contract. |
| checkerReadAheadConfirmation | Checker Source Read-Ahead Block lists dispatch and worker-output gates used for this packet. |
| docOnlyNewFields | `pathQuotingSafeInvocationDisposition`; `t3aRuntimeSmokeReceiptDisposition`; `t3aCandidateGroupASmokeInput` |
| claimBoundary | Dispatch authoring provenance only; no runtime smoke has been run by this baseline. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; Dependency Release Evidence; Negative Search And Collision Discipline; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; External Knowledge Intake Routing row labels; External Absorption Core row labels; External Absorption Value Conversion Matrix columns; Overlap And Novelty Classification dispositions; ledger_terminal=; Corpus verdict bullet; Public Export Disposition |
| gateRunPurpose | Confirmation evidence after checker source read-ahead; gates confirm this baseline and paired work order shape. |
| claimBoundary | Read-ahead covers this dispatch packet; worker output artifacts require their own checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T3 selected diagnostic failure rather than smoke pass. | VALUE_SET | `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md` | Decision / Disposition | `SMOKE_FAIL_DIAGNOSTIC_RECORDED` | T3 worker return | ACCEPT |
| T3 failure class was local invocation argument quoting before document processing. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md` | Diagnostic Classification | `LOCAL_INVOCATION_ARGUMENT_QUOTING` | T3 readiness matrix | ACCEPT |
| T3 did not release T4. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md` | Route Decision Matrix | `NOT_RELEASED_WITH_REASON` | T3 readiness matrix | ACCEPT |
| T3A authoring is the next allowed move. | VALUE_SET | `CVF_SESSION/state/entries/nextAllowedMove.json` | value | `MSEA-R24-T3A` | active session state source | ACCEPT |
| T2A config/cache receipt remains the prerequisite local model/config basis. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | Readiness Findings | `CONFIG_CACHE_RECEIPT_READY` | T2A readiness matrix | ACCEPT |
| MinerU command-line parsing supports input path and output directory. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md` | lines 11-19 | `mineru -p <input_path> -o <output_path>` | MinerU usage docs | ACCEPT |
| MinerU CLI exposes `--path`, `--output`, `--backend`, `--method`, `--formula`, and `--table`. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/client.py` | lines 1040-1185 | `main` | MinerU CLI client | ACCEPT |
| MinerU backend choices include `pipeline`. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | lines 3-14 | `BACKEND_PIPELINE` | backend options | ACCEPT |
| MinerU config reader honors `MINERU_TOOLS_CONFIG_JSON`. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/config_reader.py` | lines 14-17 | `MINERU_TOOLS_CONFIG_JSON` | config reader | ACCEPT |
| MinerU local model source resolves to configured models directory. | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 211-291 | `resolve_model_source`; `get_local_models_dir` | model download utility | ACCEPT |
| Candidate Group A is authorized for local private CVF testing only with metadata/redaction/excerpt-minimal committed evidence. | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | Operator Authorization Boundary | `Candidate Group A` | R17 intake ledger | ACCEPT |
| T3A direct call-operator invocation form is a new packet instruction derived from the T3 quoting diagnostic, not a pre-existing MinerU source fact. | DOC_ONLY_NEW | `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md` | Risk / Corrective Action | `pathQuotingSafeInvocationDisposition` | T3A dispatch packet | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned T3A baseline path absence | `Test-Path` returned `False` before authoring for the planned T3A baseline path | SAFE_TO_CREATE |
| Planned T3A work order path absence | `Test-Path` returned `False` before authoring for the planned T3A work order path | SAFE_TO_CREATE |
| Token search | `rg -n "MSEA_R24_T3A|MSEA-R24-T3A|PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN|Path Quoting Safe Local Pipeline Rerun" docs CVF_SESSION AGENT_HANDOFF_V35_2026-07-03.md` found only current next-move/session references before new files | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | T3A is a dependent child of accepted T3 diagnostic closure and current next-move surfaces | SAFE_TO_CREATE |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | This baseline is dispatch authoring only. The future worker may run one local MinerU CLI rerun only after this packet is committed and session-sync routes execution. |
| requiredFutureAction | Worker must capture executionBaseHead, run the single allowed quoting-safe command or an allowed preflight hold, and create uncommitted worker return plus companion readiness matrix. |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned MinerU source mirror plus accepted T2A receipt plus accepted T3 diagnostic plus R17 private-test boundary -> T3A quoting-safe rerun dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this baseline and paired work order |
| Disposition | ADAPT: convert accepted local quoting diagnostic into one bounded private local rerun work order |
| Claim boundary | dispatch only; no parser result, extraction quality, public-sync, provider/live proof, or production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA owner surfaces |
| Enumeration command | filesystem-backed direct reads of cited T2A/T3/R17/MinerU source files |
| Manifest artifact or inline manifest | inline table: Source Verification Block |
| Processing ledger artifact or inline ledger | inline table: Dependency Release Evidence and paired work order |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | R24 roadmap, T2A accepted artifacts, T3 accepted diagnostic artifacts, R17 private-test ledger, pinned MinerU CLI/config source |
| Unresolved items | actual T3A smoke result, runtime diagnostic, output receipt, T4 release |
| Completion claim boundary | dispatch only; no runtime smoke executed by dispatcher |

ledger_terminal=READ for cited source evidence; ledger_terminal=ADAPTED for T3A dispatch; ledger_terminal=DEFERRED for worker result and T4; ledger_terminal=REJECTED for direct workflow-chain completion from dispatch.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| T3 diagnostic closure | path quoting wrapper failure before processing | RUNTIME_CANDIDATE | T3A work order | dispatch one corrected invocation attempt | one command only |
| MinerU CLI docs/source | local input/output and pipeline backend command surface | DOCTRINE_ADAPTED | T3A work order | source-verified worker command | no API/router/gradio lane |
| T2A config source | local model path receipt exists | RUNTIME_CANDIDATE | T3A worker preflight | reuse process-local env vars | no model download |
| R17 private-test ledger | Candidate Group A local private authorization | DOCTRINE_ADAPTED | T3A privacy boundary | use same smaller file as private input | no source copy/import |
| R22/R24 local MinerU venv | existing ignored local CLI package surface | PACKAGE_CANDIDATE | T3A worker preflight | verify command presence only | no package mutation |
| T4 workflow-chain policy | requires successful T3/T3A smoke evidence | CHECKER_CANDIDATE | future T4 | defer | no checker implementation |
| Direct workflow-chain completion | unsupported by dispatch-only evidence | REJECT_DIRECT_IMPORT | future T4 | reject until accepted smoke receipt | no workflow-chain claim |
| Public export | not authorized | NO_PACKAGE_OR_RUNTIME_VALUE | private provenance only | none | no public-sync |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| T2A config/cache receipt | `docs/reference/CVF_MSEA_R24_T2A_MINERU_ABSOLUTE_CONFIG_PATH_AND_LOCAL_CACHE_BINDING_READINESS_MATRIX_2026-07-03.md` | CONFIRMED_EXISTING | prerequisite remains accepted | cite |
| T3 failed smoke diagnostic | `docs/reviews/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_WORKER_RETURN_2026-07-03.md` | ENRICH_EXISTING | releases only quoting-safe rerun authoring | adapt |
| MinerU CLI runtime command | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/client.py` | CONFIRMED_EXISTING | command options are unchanged | cite |
| Candidate Group A private input | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | CONFIRMED_EXISTING | reused without content quotation | cite |
| Workflow-chain completion | `docs/reference/CVF_MSEA_R24_T3_MINERU_LOCAL_PIPELINE_RUNTIME_SMOKE_READINESS_MATRIX_2026-07-03.md` | REJECT_DIRECT_IMPORT | T4 still held | defer |

## Corpus Completeness And Report Integrity

- Corpus task class: T3A dispatch for one bounded local MinerU runtime rerun.
- Corpus root: accepted T2A artifacts, accepted T3 diagnostic artifacts, R17 private-test authorization, and pinned MinerU CLI/config source.
- Snapshot time: 2026-07-04 dispatch authoring.
- Enumeration command: filesystem-backed direct reads of cited source files and negative-search commands above.
- Manifest artifact or inline manifest: Source Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded dispatch source set, not a new corpus snapshot.
- Processing ledger artifact or inline ledger: Dependency Release Evidence and paired work order.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=T2A/T3/R17/MinerU source evidence; ledger_terminal=READ/ADAPTED/DEFERRED/REJECTED; exclusions=manual document body read, content quotes, second runtime command, public-sync, provider/live proof, production claims; unresolved=0 for dispatch authoring.
- Unresolved files: none for dispatch authoring.
- Declared exclusions: runtime execution by dispatcher, second rerun, model download, document-body quotation, public-sync, provider/live proof, production readiness.
- Unreadable or unsupported files: none identified for dispatch authoring.
- Aggregation check: PASS - accepted owner surfaces are cited.
- Drift check: PASS - current next-move surfaces route T3A authoring after T3 diagnostic closure.
- Output traceability: paired T3A work order names worker return and readiness matrix.
- Adversarial verification: direct T4 workflow-chain completion and legal/extraction-quality claims are rejected.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or recovery requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T3/T3A requires config/cache receipt | Dependency Release Evidence | T2A selected route and receipt fields | pre-dispatch gate | PASS |
| T3 failure requires fresh authority before rerun | Dependency Release Evidence | T3 diagnostic closure commit and token | pre-dispatch gate | PASS |
| Rerun must be bounded | Allowed Command in work order | command count and log path | worker return | PASS |
| T4 remains gated | Claim Boundary | t3aRuntimeSmokeReceiptDisposition | reviewer check | PASS |
| Privacy boundary survives runtime smoke | Candidate Group A Boundary in work order | metadata-only committed evidence | reviewer check | PASS |

## Claim Boundary

This baseline authorizes only dispatch of the paired T3A no-commit work order.
It does not run MinerU, inspect document content, produce extraction output,
release T4, update public-sync, mutate packages/checkers/source/session state,
or claim parser success, workflow-chain completion, legal-quality, or
production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T3A is private provenance runtime-smoke dispatch using private Candidate
Group A inputs and ignored local runtime evidence only.
