# CVF GC-018 Baseline - MSEA-R28-T6 MinerU Quality Report Source Pointer Production Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T6-QUALITY-REPORT-SOURCE-POINTER-PRODUCTION-DECISION

rawMemoryReleased: false

dispatchBaseHead: facb2714

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: worker role, not a specific provider name

## Purpose

Authorize one bounded no-commit worker tranche to decide the source-backed
production contract for an actual MinerU quality report and source pointer
paired to a committed metadata receipt. The worker may produce a worker return
and companion decision matrix only.

This baseline does not authorize MinerU runtime execution, private or generated
content reads, Candidate Group A import, source/test edits, checker edits,
memory/RAG writes, provider/live proof, public-sync, standalone app work,
legal/use-case deep dive, extraction accuracy, document truth, legal quality,
current-law correctness, workflow-chain production readiness, worker stage,
worker commit, or push.

## Scope / Target / Owner Boundary

Allowed worker target: docs-only production-decision analysis for actual quality
report and source-pointer requirements, grounded in accepted R28-T5 evidence,
R28-T5 writer/checker source, R28-T3 design evidence, R27 memory route
requirements, R24-T4 private-output policy, and Extraction Foundation
quality/storage owner surfaces.

Allowed worker output paths:

- `docs/reviews/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_WORKER_RETURN_2026-07-04.md`
- `docs/reference/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_MATRIX_2026-07-04.md`

Forbidden paths and actions: no edits to active session state, active handoff,
root startup files, AGENTS.md, public-sync clone, product runtime, Web/UI,
MCP/CLI adapter, memory/RAG owner, Candidate Group A source or generated output,
private source documents, generated MinerU output content, runtime receipt
instances, writer source, checker source, tests, or registry aggregates.

## Baseline Decision

| Field | Value |
| --- | --- |
| selectedRoute | `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_ONLY` |
| releaseBasis | R28-T5 material commit `4a824e6d` accepted receipt-side quality/source-pointer fields and checker validation while preserving the memory-route hold. |
| implementationBoundary | worker return plus companion decision matrix only |
| memoryRouteDisposition | `MEMORY_ROUTE_STILL_HELD_PENDING_ACTUAL_PRODUCTION_AND_MEMORY_OWNER_DECISION` |
| runtimeDisposition | no MinerU runtime execution, no private/generated content read, no extraction accuracy or document-truth claim |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T6 --title "MinerU Quality Report Source Pointer Production Decision" --date 2026-07-04 --base facb2714 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled R28-T6 decision-only purpose, source verification, worker output manifest, handoff controls, and held-lane boundaries |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_ONLY`; `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_MATRIX_READY`; `MEMORY_ROUTE_STILL_HELD_PENDING_ACTUAL_PRODUCTION_AND_MEMORY_OWNER_DECISION` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, scaffold output, source verification, checker read-ahead, and no-commit discipline. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; Resolver query; Returned defects: NONE_RETURNED; Public Export Disposition; Delta Execution Claim Boundary Control Block; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define worker scope. |
| claimBoundary | This read-ahead covers the R28-T6 dispatch packet only; worker-created return and matrix require their own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session state releases R28-T6 packet authoring from accepted R28-T5 evidence and preserves the memory-route hold. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| R28-T5 worker return states receipt-side quality/source-pointer references now exist but actual quality report production, source-pointer resolution, and memory release remain unsatisfied. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_WORKER_RETURN_2026-07-04.md` | lines 103-119, 130, 138, and 146-148 | `MEMORY_ROUTE_STILL_HELD_AFTER_QUALITY_SOURCE_POINTER_SCHEMA_EXTENSION`; `qualityReportRef`; `sourcePointer` | R28-T5 worker return | ACCEPT |
| R28-T5 writer source owns metadata-only quality/source-pointer receipt fields and keeps downstream release held. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 16, 18, 49, 67, 74-80, 133, 185, 198, and 202 | `RECEIPT_VERSION`; `DOWNSTREAM_RELEASE_HELD`; `QUALITY_OR_SOURCE_POINTER_MISSING`; `MineruMetadataReceipt`; `build_mineru_metadata_receipt`; `mineru_metadata_receipt_payload` | Extraction Foundation metadata receipt writer | ACCEPT |
| R28-T5 checker requires quality/source-pointer fields and validates missing or invalid values with the dedicated failure token. | RUNTIME_BEHAVIOR | `governance/compat/check_mineru_receipt_boundary.py` | lines 37, 47-48, 212, 215, and 307-320 | `REQUIRED_FIELDS`; `_validate_receipt`; `QUALITY_OR_SOURCE_POINTER_MISSING` | MinerU receipt boundary checker | ACCEPT |
| R28-T3 design matrix records the quality/source-pointer prerequisite and keeps memory write held until actual checker, quality/source-pointer, and memory adapter prerequisites exist. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_MATRIX_2026-07-04.md` | lines 45, 68, 77, 114, and 132 | `QUALITY_OR_SOURCE_POINTER_MISSING`; `MEMORY_ROUTE_HELD_PENDING_ACTUAL_CHECKER_AND_QUALITY` | R28-T3 design matrix | ACCEPT |
| R27 memory-safe candidate readiness requires receipt, quality, source pointer, downstream use, claim boundary, and later memory-owner work. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 39, 85, 86, and 263-264 | `QUALITY_DISPOSITION_READY`; `MEMORY_SAFE_CANDIDATE_READY` | R27 decision ledger | ACCEPT |
| R24-T4 private-output policy allows metadata-only receipts and requires output-content read to remain false for private committed evidence. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 44, 51-54, 62-65, 134, 141, and 148 | `outputContentRead`; `privateOutputDisposition`; `PRIVATE_GENERATED_OUTPUT`; `RECEIPT_METADATA_ALLOWED` | MSEA-R24-T4 private-output policy | ACCEPT |
| Extraction Foundation owns quality report and storage-boundary primitives that a future implementation may connect without making this dispatch a runtime claim. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | lines 101, 105, 152, 156, 235, 424, 426, and 436-438 | `ExtractionQualityReport`; `ExtractionStorageBoundary`; `evaluate_extraction_quality`; `build_extraction_storage_boundary` | Extraction Foundation pipeline | ACCEPT |

## New Doc-Only Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_ONLY` | selected R28-T6 disposition for docs-only production-contract decision | DOC_ONLY_NEW | use only in worker return and companion matrix |
| `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_MATRIX_READY` | accepted matrix-ready result token if the worker completes without implementation | DOC_ONLY_NEW | use only if all source evidence and held-lane boundaries are satisfied |
| `MEMORY_ROUTE_STILL_HELD_PENDING_ACTUAL_PRODUCTION_AND_MEMORY_OWNER_DECISION` | memory-route disposition after R28-T6 docs-only decision | DOC_ONLY_NEW | preserve memory hold even if the matrix is accepted |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned R28-T6 dispatch paths absent before authoring | `Test-Path` returned `False` for planned R28-T6 baseline, work order, worker return, and companion matrix paths. | PASS |
| Token search for R28-T6 before authoring | `rg -n "MSEA-R28-T6|QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION|QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_MATRIX_READY|quality report source pointer production" docs CVF_SESSION governance EXTENSIONS` returned only active session next-move references before this packet was created. | PASS |
| Current receipt source check | `rg -n "qualityReportRef|sourcePointer|QUALITY_OR_SOURCE_POINTER_MISSING|RECEIPT_VERSION|DOWNSTREAM_RELEASE_HELD" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py governance/compat/check_mineru_receipt_boundary.py` confirmed R28-T5 receipt-side fields and checker token exist. | PASS |
| Freshness disposition | Current source has receipt-side references but no source-backed actual quality-report/source-pointer production decision packet; R28-T6 may dispatch a docs-only worker to produce that decision. | PASS |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Exact search roots | `docs`, `CVF_SESSION`, `governance`, and `EXTENSIONS` | PASS |
| Exact search command or query | `rg -n "MSEA-R28-T6|QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION|QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_MATRIX_READY|quality report source pointer production" docs CVF_SESSION governance EXTENSIONS` | PASS |
| Coverage across source/tests/docs/JSON/external evidence | The search included governed docs, generated session JSON, governance code, and Extraction Foundation source surfaces. | PASS |
| Same-token collision result | Current occurrences before authoring were session next-move references, not an existing R28-T6 dispatch artifact. | PASS |
| Absent-versus-collision disposition | No dedicated R28-T6 baseline, work order, worker return, or matrix existed before authoring; session references are routing evidence only. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor requirement | Source evidence | R28-T6 handling |
| --- | --- | --- |
| R28-T5 added receipt-side quality/source-pointer references but did not produce the referenced quality report or source pointer | material commit `4a824e6d`; R28-T5 worker return lines 103-119 and 146-148 | authorize docs-only production-decision matrix |
| R28-T3 required a paired quality report/source pointer before memory readiness | design matrix line 68 | define source-backed criteria for a future implementation packet |
| R27 memory-safe candidate requires quality, source pointer, downstream use, claim boundary, and memory-owner decision | R27 ledger lines 85-86 | keep memory route held |
| R24-T4 forbids generated-output content reads for private committed evidence | R24-T4 policy lines 51-65 and 134-148 | require metadata-only evidence and no content read |
| Extraction Foundation owns quality/storage primitives | extraction pipeline lines 101-156 and 424-438 | map owner surfaces without implementation |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | worker return and companion decision matrix | internal worker may decide future production contract under WORKER_MUST_NOT_COMMIT; reviewer must accept before closure | this GC-018, paired work order, source verification, worker return, matrix | docs-only decision; no runtime adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP or external adapter owner in R28-T6 | external ingress, authentication, approval, receipt, raw-data, mutation, and public boundaries remain out of scope | no source-verified external adapter authority in R28-T6 | adapter deferred; no CLI/MCP surface implemented or claimed | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Corpus scan or extraction intake |
| Chain map route | extraction/source evidence -> CVF-owned references and runtime source verification -> fresh GC-018/work order -> autorun pre-dispatch gates |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired R28-T6 GC-018 and work order |
| Disposition | ADAPT prior R27/R28 and Extraction Foundation evidence into a bounded production-decision dispatch; no external source becomes authority by itself |
| Claim boundary | routing evidence only; no external repository absorption, private/generated content read, runtime/provider/live proof, public-sync, app, or production claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Guard owner | `governance/compat/check_foundation_storage_layout.py` |
| Trigger reason | this baseline authorizes a new durable reference matrix under `docs/reference/` |
| Stable location decision | one companion matrix is allowed under the existing flat `docs/reference/` governed artifact family for MSEA execution evidence |
| Index or front-door decision | N/A with reason: this is a dated execution matrix, not a new stable reference family |
| Archive or rotation decision | N/A with reason: no existing durable governance file is split, moved, archived, or rotated in this dispatch |
| Generated aggregate decision | no generated aggregate edit is authorized |
| Claim boundary | storage-layout evidence only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T6 dispatch baseline for quality-report/source-pointer production decision |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata receipt source and checker evidence are cited, but this baseline creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this baseline runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local file reads, source verification, scaffold generation, and governance dispatch gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | dispatch authoring for a docs-only production-decision tranche |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior or memory write without fresh source-verified authorization. |

## Evidence / Verification

| Evidence item | Required result | Current dispatch evidence |
| --- | --- | --- |
| Source verification | ACCEPT rows cite CVF-governed surfaces or current runtime source | Source Verification Block in this baseline and paired work order |
| Prior implementation release | R28-T5 accepted receipt-side fields and checker validation | R28-T5 worker return, material commit `4a824e6d`, and session-sync commit `facb2714` |
| Dispatch gates | pre-dispatch autorun must pass before worker execution begins | pending gate evidence in dispatcher final report |
| Worker decision evidence | worker return and companion decision matrix | required by paired work order; not produced by this baseline |
| Claim exclusions | no runtime/provider/live/public/private-content/app/legal/deep-quality claim | Claim Boundary and Public Export Disposition in this baseline |

## Claim Boundary

This baseline authorizes dispatch of a no-commit worker to create a docs-only
quality-report/source-pointer production decision packet and companion matrix.
It does not release memory/RAG, run MinerU, read private/generated content,
create a runtime receipt, edit writer/checker/tests, make public or provider
claims, build an app, or claim extraction accuracy, document truth, legal
quality, current-law correctness, workflow-chain production readiness, worker
commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T6 is private provenance dispatch work and does not change the
public-sync repository or public catalog.
