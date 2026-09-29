# CVF GC-018 Baseline - MSEA-R24-T4 MinerU Workflow Chain Receipt Policy And Private Output Handling

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-04

Batch ID: MSEA-R24-T4

Dispatch base head: e6d1d3d2

Commit mode: WORKER_MUST_NOT_COMMIT

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Purpose

Dispatch one bounded docs-only worker tranche to convert the accepted MSEA-R24-T3A smoke receipt into a private workflow-chain receipt policy. This baseline authorizes no MinerU rerun, no generated-output content inspection, no schema/writer/adapter/checker implementation, no public-sync, and no production workflow-chain claim.

## Scope

| Field | Value |
|---|---|
| In scope | MSEA-R24-T4 dispatch packet for policy wording, private output handling rules, and successor-roadmap release criteria |
| Out of scope | MinerU command execution, output-content read/quote, Candidate Group A source copy/import, runtime/provider/live proof, public-sync, RAG/S3, schema/writer/adapter/checker/package/Web/MCP/model-router/action-authority work, legal-quality or current-law claim, production claim |
| Owner | dispatcher for packet authoring; worker for uncommitted policy/reference outputs; reviewer/closer for material acceptance and session-sync |

## Decision / Baseline / Proposed Tranche

| Field | Value |
|---|---|
| Decision | Dispatch T4 because T3A smoke receipt was accepted by reviewer/closer at material commit `04b99044` |
| Baseline | accepted R24 roadmap, accepted T3A worker return and readiness matrix, R17 private-test boundary, and MinerU output-file documentation |
| Proposed tranche | MSEA-R24-T4 MinerU workflow-chain receipt policy and private output handling |
| Dispatch route | WORKER_MUST_NOT_COMMIT |

## Evidence / Verification

| Evidence item | Verification |
|---|---|
| Dispatch base | `e6d1d3d2` captured after MSEA-R24-T3A acceptance session-sync |
| Pre-dispatch target | this baseline and paired work order only |
| Runtime execution | NOT_RUN_BY_DISPATCHER |
| Verification status | pending pre-dispatch autorun after this packet is authored |

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| MSEA-R24 roadmap T4 dependency | roadmap states T4 opens after T3 records smoke evidence and uses workflow-chain receipt policy | `4065bb0e` | SATISFIED |
| T3A smoke receipt accepted | worker return selected `SMOKE_PASS_BOUNDED`; reviewer accepted material commit | `04b99044` | SATISFIED |
| T3A readiness matrix | matrix records exit code `0`, output file count `6`, metadata-only inventory, and no workflow-chain claim | `04b99044` | SATISFIED |
| T3A session sync releases T4 authoring | active session state and handoff route next move to fresh T4 GC-018/work-order authoring only | `e6d1d3d2` | SATISFIED |
| Candidate Group A private-test boundary | R17 permits local private testing only with metadata/redaction/excerpt-minimal committed evidence | `eb127b7f` | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | N/A with reason: resolver returned no defects for this dispatcher pre-dispatch query |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R24-T4 --title "MinerU Workflow Chain Receipt Policy And Private Output Handling" --date 2026-07-04 --base e6d1d3d2 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R24-T3A smoke receipt accepted at 04b99044 selected SMOKE_PASS_BOUNDED" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled dependency release evidence, source verification, private-output policy boundary, worker-output contract, and successor roadmap release boundary. |
| checkerReadAheadConfirmation | Checker Source Read-Ahead Block lists dispatch and worker-output gates used for this packet. |
| docOnlyNewFields | `workflowReceiptPolicyDisposition`; `privateOutputHandlingDisposition`; `workflowChainSystemizationRoadmapReleaseDisposition` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

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
| R24-T4 opens after smoke evidence and writes workflow-chain receipt policy. | VALUE_SET | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | T1-T4 Dependency Contract | `MSEA-R24-T4` | R24 roadmap | ACCEPT |
| T3A selected bounded smoke pass. | VALUE_SET | `docs/reviews/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_WORKER_RETURN_2026-07-04.md` | Decision / Disposition | `SMOKE_PASS_BOUNDED` | T3A worker return | ACCEPT |
| T3A recorded metadata-only output file count. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_READINESS_MATRIX_2026-07-04.md` | Runtime Receipt Matrix | `outputFileCount` | T3A readiness matrix | ACCEPT |
| T3A output inventory includes generated json, markdown, and origin-copy file names under ignored runtime output. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_READINESS_MATRIX_2026-07-04.md` | Output Inventory | `148_2025_QH15_675262_*` | T3A readiness matrix | ACCEPT |
| Candidate Group A committed evidence must remain metadata/redaction/excerpt-minimal and private. | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | Permission And Privacy Disposition | `Candidate Group A` | R17 intake ledger | ACCEPT |
| MinerU documents expected output file classes including model, middle, content list, layout, and span outputs. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | output file reference sections | `model.json`; `middle.json`; `content_list.json`; `content_list_v2.json`; `layout.pdf`; `span.pdf` | MinerU output docs | ACCEPT |
| This T4 policy field is new doc-only governance wording, not an existing runtime field. | DOC_ONLY_NEW | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | T1-T4 Dependency Contract | `workflowReceiptPolicyDisposition` | T4 dispatch packet | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned T4 baseline path absence | `Test-Path` returned `False` before authoring for the planned T4 baseline path | SAFE_TO_CREATE |
| Planned T4 work order path absence | `Test-Path` returned `False` before authoring for the planned T4 work order path | SAFE_TO_CREATE |
| Token search | `rg -n "MSEA_R24_T4|MSEA-R24-T4|WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING|Workflow Chain Receipt Policy And Private Output Handling" docs CVF_SESSION AGENT_HANDOFF_V35_2026-07-03.md` found only roadmap/session next-move references before new files | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | T4 is a dependent child of accepted T3A smoke closure and current next-move surfaces | SAFE_TO_CREATE |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | This baseline is dispatch authoring for a docs-only policy tranche. No MinerU command or generated output content inspection is authorized. |
| requiredFutureAction | Worker must create uncommitted policy/reference outputs from accepted metadata-only owner surfaces and run worker-output gates. |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned MinerU source mirror plus accepted T3A smoke receipt plus R17 private-test boundary -> T4 policy dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this baseline and paired work order |
| Disposition | ADAPT: convert accepted smoke metadata into private workflow-chain receipt policy |
| Claim boundary | dispatch only; no parser result, extraction quality, public-sync, provider/live proof, or production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA owner surfaces |
| Enumeration command | filesystem-backed direct reads of cited R24/T3A/R17/MinerU source files |
| Manifest artifact or inline manifest | inline table: Source Verification Block |
| Processing ledger artifact or inline ledger | inline table: Dependency Release Evidence and paired work order |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md`; `docs/reviews/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_WORKER_RETURN_2026-07-04.md`; `docs/reference/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_READINESS_MATRIX_2026-07-04.md`; `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md`; inline table: Source Verification Block |
| Unresolved items | worker-selected T4 policy token and successor R25 roadmap authoring |
| Completion claim boundary | dispatch only; no runtime smoke executed by dispatcher |

ledger_terminal=READ for cited source evidence; ledger_terminal=ADAPTED for T4 dispatch; ledger_terminal=DEFERRED for R25 implementation lanes; ledger_terminal=REJECTED for direct production/workflow-chain claims.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| T3A smoke receipt | process-level smoke passed with metadata-only output inventory | DOCTRINE_ADAPTED | T4 policy | define receipt policy | no rerun |
| T3A runtime receipt | ignored local receipt exists as accepted source evidence | RUNTIME_CANDIDATE | T4 policy | reuse metadata only | no new runtime |
| MinerU output docs | named output artifact classes | DOCTRINE_ADAPTED | T4 policy | map privacy classes | no output read |
| R17 privacy boundary | local private testing and committed metadata limits | DOCTRINE_ADAPTED | T4 policy | preserve private handling | no public-sync |
| Future receipt checker | possible later enforcement | CHECKER_CANDIDATE | R25 roadmap | defer to fresh work order | no checker implementation |
| Existing MinerU package surface | package already used by T3A but irrelevant to T4 policy | PACKAGE_CANDIDATE | pending owner: no T4 package owner surface needed | cite only | no package mutation |
| Direct production workflow | unsupported by T4 policy alone | REJECT_DIRECT_IMPORT | claim boundary | reject | no production claim |
| Runtime/package mutation | outside T4 | NO_PACKAGE_OR_RUNTIME_VALUE | none | none | no mutation |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| R24 roadmap T4 route | `docs/roadmaps/CVF_MSEA_R24_MINERU_MODEL_SOURCE_FALLBACK_AND_CACHE_COMPLETION_RECOVERY_ROADMAP_2026-07-03.md` | CONFIRMED_EXISTING | dependency satisfied by accepted T3A | cite |
| T3A metadata receipt | `docs/reviews/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_WORKER_RETURN_2026-07-04.md`; `docs/reference/CVF_MSEA_R24_T3A_MINERU_PATH_QUOTING_SAFE_LOCAL_PIPELINE_RERUN_READINESS_MATRIX_2026-07-04.md` | ENRICH_EXISTING | enables policy, not production | adapt |
| MinerU output classes | inline table: Source Verification Block | ENRICH_EXISTING | sharpens private output taxonomy | adapt |
| Candidate Group A privacy | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | CONFIRMED_EXISTING | remains binding | cite |
| Direct schema/writer/checker implementation | OWNER_SURFACE_NOT_FOUND | REJECT_DIRECT_IMPORT | future R25 only | defer |

## Corpus Completeness And Report Integrity

- Corpus task class: T4 dispatch for private workflow-chain receipt policy.
- Corpus root: R24 roadmap, accepted T3A artifacts, R17 private-test ledger, and pinned MinerU output documentation.
- Snapshot time: 2026-07-04 dispatch authoring.
- Enumeration command: filesystem-backed direct reads of cited source files and negative-search commands above.
- Manifest artifact or inline manifest: Source Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded dispatch source set, not a new corpus snapshot.
- Processing ledger artifact or inline ledger: Dependency Release Evidence and paired work order.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=R24/T3A/R17/MinerU source evidence; ledger_terminal=READ/ADAPTED/DEFERRED/REJECTED/NO_NEW_VALUE; exclusions=runtime rerun, generated-output content read, public-sync, implementation work, production claims; unresolved=0 for dispatch authoring.
- Unresolved files: none for dispatch authoring.
- Declared exclusions: runtime execution, output-content quotation, schema/writer/adapter/checker work, public-sync, provider/live proof, production readiness.
- Unreadable or unsupported files: none identified for dispatch authoring.
- Aggregation check: PASS - accepted owner surfaces are cited.
- Drift check: PASS - current next-move surfaces route T4 authoring after T3A acceptance.
- Output traceability: paired T4 work order names worker return and policy artifact.
- Adversarial verification: direct workflow-chain completion and legal/extraction-quality claims are rejected.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or recovery requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T4 opens only after smoke evidence | Dependency Release Evidence | T3A accepted receipt commit | pre-dispatch gate | PASS |
| T4 writes receipt policy | Purpose and Worker Fulfillment Manifest | policy artifact | worker return | PASS |
| Privacy boundary survives output handling | Private Output Handling Boundary | metadata-only and no-content-read rules | reviewer check | PASS |
| Workflow-chain claim remains bounded | Claim Boundary | workflowReceiptPolicyDisposition | reviewer check | PASS |
| R25 requires fresh roadmap/work order | Claim Boundary | successor release disposition | reviewer check | PASS |

## Claim Boundary

This baseline authorizes only dispatch of the paired T4 no-commit work order. It does not run MinerU, inspect document content, produce extraction output, update public-sync, mutate packages/checkers/source/session state, implement schemas or adapters, or claim extraction accuracy, workflow-chain production readiness, legal quality, or current-law correctness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T4 is private provenance policy work over local private MinerU smoke evidence and Candidate Group A privacy constraints. No public-sync export is authorized.
