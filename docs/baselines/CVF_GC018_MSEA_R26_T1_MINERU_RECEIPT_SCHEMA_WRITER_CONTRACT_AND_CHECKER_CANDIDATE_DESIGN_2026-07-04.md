# CVF GC-018 Baseline - MSEA R26 T1 MinerU Receipt Schema Writer Contract And Checker Candidate Design

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: MSEA-R26-T1

Dispatch base head: b8b8412e

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: Codex/reviewer-closer

Worker target: delegated worker

## Purpose

Authorize one bounded post-MSEA-R25 documentation tranche that turns the accepted MinerU private-output receipt policy into a source-backed schema/writer contract draft and checker-candidate decision surface.

## Scope

This baseline applies only to MSEA-R26-T1 dispatch authoring and delegated worker execution. It does not authorize schema writer implementation, checker implementation, adapter implementation, runtime execution, source import, memory ingestion, public-sync, provider/live proof, package mutation, production workflow-chain claims, or legal-quality claims.

## Source And Predecessor Evidence

| Evidence item | Source | Verified line/section | Disposition |
| --- | --- | --- | --- |
| R25 selected schema/writer contract draft and checker candidate only | `docs/reference/CVF_MSEA_R25_MINERU_WORKFLOW_CHAIN_SYSTEMIZATION_DECISION_LEDGER_2026-07-04.md` | lines 46, 61, 94, 142 | ACCEPT |
| T4 defines the minimal private receipt envelope and output classes | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 39-66, 116 | ACCEPT |
| MinerU names output file families used for metadata-only receipt classification | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | lines 17-19, 35-40, 62-64, 109-111, 292-298, 396-402, 675, 730-742 | ACCEPT |
| Post-R25 session state allows exactly one selected post-R25 route with fresh GC-018/work order | `CVF_SESSION/ACTIVE_SESSION_STATE.json` and `AGENT_HANDOFF_V35_2026-07-03.md` | active state and handoff read before authoring | ACCEPT |

## Decision

Dispatch MSEA-R26-T1 as a no-commit worker tranche. The worker must create a worker return and a companion reference contract only, leaving review and commit ownership to the reviewer/closer.

## Proposed Tranche

| Field | Value |
| --- | --- |
| trancheId | MSEA-R26-T1 |
| routeToken | `SELECT_SCHEMA_WRITER_CONTRACT_DRAFT` plus `SELECT_CHECKER_CANDIDATE_ONLY` |
| workerCommitMode | WORKER_MUST_NOT_COMMIT |
| authorizedOutputs | worker return under `docs/reviews/`; companion reference under `docs/reference/` |
| implementationAuthority | NOT_AUTHORIZED |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R26-T1 --title "MinerU Receipt Schema Writer Contract And Checker Candidate Design" --date 2026-07-04 --base b8b8412e --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R25 closure at 1e58d75a selected SELECT_SCHEMA_WRITER_CONTRACT_DRAFT plus SELECT_CHECKER_CANDIDATE_ONLY" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled source evidence, route selection, output contract, external routing, overlap, AHB, AOT, delta, and verification blocks. |
| checkerReadAheadConfirmation | Dispatch author read `governance/compat/check_work_order_dispatch_quality.py`, `governance/compat/check_agent_packet_authority_and_encoding.py`, `governance/compat/check_governed_artifact_checker_read_ahead.py`, `governance/compat/check_adif_defect_registry_disclosure.py`, `governance/compat/check_agent_handoff_boundary.py`, `governance/compat/check_external_knowledge_intake_routing.py`, `governance/compat/check_external_absorption_core.py`, `governance/compat/check_external_absorption_value_conversion.py`, `governance/compat/check_external_absorption_overlap_discipline.py`, `governance/compat/check_source_mirror_migration.py`, `governance/compat/check_corpus_completeness_report_integrity.py`, `governance/compat/check_rescan_intelligence_hardening.py`, `governance/compat/check_agent_operation_trace.py`, `governance/compat/check_delta_execution_claim_boundary.py`, `governance/compat/check_worker_return_quality_gate.py`, and `governance/compat/check_markdown_structural_completeness.py`. |
| docOnlyNewFields | Listed in New Doc-Only Fields. |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| MSEA-R25 route selection | Material commit `1e58d75a` closed MSEA-R25; R25 ledger line 61 selected contract drafting and checker candidate only. | Fresh GC-018 and source-verified work order required before any next tranche. | SATISFIED_FOR_DISPATCH |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF defect packet applied to this dispatch query; literal-format and checker-read-ahead safeguards remain mandatory from canonical references. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | Checker Source Read-Ahead Block; Source Verification Block; Negative Search And Collision Discipline; ADIF Defect Registry Disclosure; ACCEPT; REJECT; DOC_ONLY_NEW; DISPATCH_READY; WORKER_MUST_NOT_COMMIT; SINGLE_AGENT_SINGLE_ROLE; CLAIM_REJECTED_NO_RECEIPT; CLAIM_REJECTED_NO_ACTION; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Confirmation/evidence before dispatch, not discovery after authoring. |
| claimBoundary | Read-ahead confirms packet-shape obligations for this baseline only; it does not validate future worker output content. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R25 allows contract draft and checker candidate route | VALUE_SET | `docs/reference/CVF_MSEA_R25_MINERU_WORKFLOW_CHAIN_SYSTEMIZATION_DECISION_LEDGER_2026-07-04.md` | lines 46, 61, 94, 142 | `SELECT_SCHEMA_WRITER_CONTRACT_DRAFT`; `SELECT_CHECKER_CANDIDATE_ONLY` | MSEA-R25 decision ledger | ACCEPT |
| Minimal receipt fields already accepted | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 39-56 | `receiptId`; `inputSha256`; `outputContentRead`; `privateOutputDisposition`; `downstreamRelease` | T4 receipt envelope | ACCEPT |
| Private output disposition vocabulary already accepted | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 62-66 | `PRIVATE_INPUT_ONLY`; `PRIVATE_RUNTIME_COPY`; `PRIVATE_GENERATED_OUTPUT`; `RECEIPT_METADATA_ALLOWED`; `EXCERPT_MINIMAL_SEPARATE_AUTHORITY` | T4 private output class matrix | ACCEPT |
| MinerU output file families are documented upstream | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | lines 17-19, 35-40, 62-64, 109-111, 292-298, 396-402, 675, 730-742 | `layout.pdf`; `span.pdf`; `model.json`; `middle.json`; `content_list.json`; `content_list_v2.json` | MinerU output documentation | ACCEPT |
| R25 denies implementation and runtime expansion | LITERAL_INVARIANT | `docs/reference/CVF_MSEA_R25_MINERU_WORKFLOW_CHAIN_SYSTEMIZATION_DECISION_LEDGER_2026-07-04.md` | lines 114, 128, 209-215 | `implementation remains future work` | MSEA-R25 claim boundary | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Source fact type | Dispatch disposition |
| --- | --- | --- | --- |
| sourceInputSlot | Metadata-only local slot label for private inputs without naming sensitive documents. | DOC_ONLY_NEW | Allowed in R26 reference draft only. |
| inputSizeBytes | Metadata-only size field for future receipt envelope. | DOC_ONLY_NEW | Allowed in R26 reference draft only. |
| executionBaseHead | Git base field copied from governed worker practice. | DOC_ONLY_NEW | Allowed as documentation contract field, not runtime behavior. |
| commandAttemptCount | Future receipt metadata field. | DOC_ONLY_NEW | Allowed as documentation contract field, not runtime behavior. |
| exitCode | Future receipt metadata field. | DOC_ONLY_NEW | Allowed as documentation contract field, not runtime behavior. |
| durationSeconds | Future receipt metadata field. | DOC_ONLY_NEW | Allowed as documentation contract field, not runtime behavior. |
| outputFileCount | Metadata-only output count field. | DOC_ONLY_NEW | Allowed as documentation contract field, not output-content read authority. |
| outputFileNames | Metadata-only output family names. | DOC_ONLY_NEW | Allowed only for filenames/classes, not generated content. |
| claimBoundary | Receipt statement field preserving no-production/no-legal-quality boundaries. | DOC_ONLY_NEW | Allowed in R26 reference draft only. |
| writerContractStatus | Documentation-only route token for future writer readiness. | DOC_ONLY_NEW | No writer implementation. |
| checkerCandidateStatus | Documentation-only route token for future checker consideration. | DOC_ONLY_NEW | No checker implementation. |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned baseline path did not exist before authoring | `Test-Path docs/baselines/CVF_GC018_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` returned `False`. | NO_COLLISION |
| Planned work order path did not exist before authoring | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` returned `False`. | NO_COLLISION |
| Prior artifact token search | `rg -n "MSEA_R26_T1|MSEA-R26-T1|RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN|Receipt Schema Writer Contract And Checker Candidate Design" docs/roadmaps docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION AGENT_HANDOFF_V35_2026-07-03.md` returned exit code 1 with no matches. | NO_PRIOR_ARTIFACT |
| Collision decision | R26-T1 is a new post-R25 tranche. | PROCEED |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | SOURCE_MIRROR_LOCAL_REFERENCE_ONLY |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MSEA-R25 ledger plus T4 receipt policy; MinerU source mirror used as upstream documentation authority for output filenames only. |
| Disposition | ROUTED_TO_REFERENCE_CONTRACT_DRAFT |
| Claim boundary | This route consumes already mirrored documentation and does not import source, execute MinerU, or make runtime claims. |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| T4 receipt envelope fields | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | CONFIRMED_EXISTING | R26 may reorganize into a draft schema/writer contract but cannot replace T4 policy. | ENRICH_EXISTING_REFERENCE |
| MinerU output filename families | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` and R25 ledger | ENRICH_EXISTING | R26 can map names to metadata-only output family slots. | ADD_DOC_ONLY_CONTRACT_MAPPING |
| Future checker enforcement | `docs/reference/CVF_MSEA_R25_MINERU_WORKFLOW_CHAIN_SYSTEMIZATION_DECISION_LEDGER_2026-07-04.md` line 142 and `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` line 116 | CONFIRMED_EXISTING | Existing status is checker candidate only. | KEEP_CHECKER_CANDIDATE_ONLY |
| Runtime writer implementation | `docs/reference/CVF_MSEA_R25_MINERU_WORKFLOW_CHAIN_SYSTEMIZATION_DECISION_LEDGER_2026-07-04.md` claim boundary lines 114 and 209-215 | REJECT_DIRECT_IMPORT | No implementation authority exists in this baseline. | HOLD_FOR_FRESH_AUTHORITY |

## Evidence Reuse And Encoding Plan

| Field | Value |
| --- | --- |
| priorVerificationMode | REUSE_PRIOR_VERIFICATION plus targeted line refresh with `Select-String` |
| unicodePathHandling | Use repo-local paths exactly as cited; preserve spaces in working directory only in command context. |
| extractedTextAuthority | Source mirror documentation and governed CVF references only; provider-local memories are not authority. |
| recomputeBoundary | Worker must refresh cited source lines if any referenced artifact changed after dispatch. |
| encodingBoundary | ASCII only for new governed markdown unless an explicit exception is added. |

## Evidence And Verification

Dispatch verification must use pre-dispatch autorun over `b8b8412e..HEAD` before material commit. Worker verification must use pre-implementation autorun and worker-return fast gate from the worker execution base.

## Claim Boundary

This baseline authorizes only MSEA-R26-T1 dispatch and no-commit worker documentation outputs. It does not authorize runtime/provider/live/public/package/Web/MCP/model-router/action-authority behavior, schema writer code, checker code, adapter work, source import, private output content inspection, memory ingestion, production workflow-chain readiness, document-truth, extraction-accuracy, current-law, or legal-quality claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R26-T1 is private provenance work based partly on private testing policy and a local source mirror; no public-sync export is authorized.
