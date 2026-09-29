# CVF GC-018 Baseline - MSEA-R28-T7 MinerU Actual Quality Report Source Pointer Production Implementation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T7-ACTUAL-QUALITY-REPORT-SOURCE-POINTER-PRODUCTION-IMPLEMENTATION

rawMemoryReleased: false

dispatchBaseHead: 75802a8d

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: worker role, not a specific provider name

## Purpose

Authorize one bounded no-commit worker tranche to implement deterministic local
metadata production for MinerU `qualityReportRef` and `sourcePointer` values
that can be supplied to the existing metadata receipt writer. The worker may
modify only the named Extraction Foundation source/test surfaces and create the
named worker return.

This baseline does not authorize MinerU runtime execution, private or generated
content reads, Candidate Group A import, memory/RAG writes, provider/live
proof, public-sync, standalone app work, legal/use-case deep dive, extraction
accuracy, document truth, legal quality, current-law correctness, workflow-chain
production readiness, worker stage, worker commit, or push.

## Scope / Target / Owner Boundary

Allowed worker target: deterministic metadata-only helper implementation that
connects current Extraction Foundation quality/storage owner surfaces to the
current receipt writer's bounded `qualityReportRef` and `sourcePointer` fields.

Allowed worker output paths:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`
- `docs/reviews/CVF_MSEA_R28_T7_MINERU_ACTUAL_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`

Forbidden paths and actions: no edits to active session state, active handoff,
root startup files, AGENTS.md, public-sync clone, product runtime outside the
named Extraction Foundation source/test files, Web/UI, MCP/CLI adapter,
memory/RAG owner, Candidate Group A source or generated output, private source
documents, generated MinerU output content, runtime receipt instances,
checker/hook source, registry aggregates, or unrelated documentation.

## Baseline Decision

| Field | Value |
| --- | --- |
| selectedRoute | `ACTUAL_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTATION` |
| releaseBasis | R28-T6 material commit `6bad1865` accepted the production-decision matrix and kept memory route held. Session-sync commit `75802a8d` routes the next allowed move to T7 packet authoring only. |
| implementationBoundary | deterministic local metadata helper plus focused tests plus worker return |
| memoryRouteDisposition | `MEMORY_ROUTE_HELD_PENDING_ALLOWED_DOWNSTREAM_USE_AND_MEMORY_OWNER_DECISION` |
| runtimeDisposition | no MinerU runtime execution, no private/generated content read, no extraction accuracy or document-truth claim |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T7 --title "MinerU Actual Quality Report Source Pointer Production Implementation" --date 2026-07-04 --base 75802a8d --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled R28-T7 implementation purpose, source verification, source/test ownership, worker output manifest, handoff controls, and held-lane boundaries |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `ACTUAL_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTATION`; `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTED`; `MEMORY_ROUTE_HELD_PENDING_ALLOWED_DOWNSTREAM_USE_AND_MEMORY_OWNER_DECISION` |
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
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define worker implementation content. |
| claimBoundary | This read-ahead covers the R28-T7 dispatch packet only; worker-created return requires its own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session state releases R28-T7 packet authoring from accepted R28-T6 evidence and preserves the memory-route hold. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| R28-T6 worker return selects a decision-only route and recommends fresh R28-T7 implementation authorization. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_WORKER_RETURN_2026-07-04.md` | Decision / Disposition section | `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_MATRIX_READY`; `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_ONLY` | MSEA-R28-T6 worker return | ACCEPT |
| R28-T6 companion matrix separates receipt-reference shape from actual quality-report and source-pointer production. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_MATRIX_2026-07-04.md` | Decision Matrix section | `HELD_PENDING_ACTUAL_PRODUCTION_IMPLEMENTATION`; `HELD_PENDING_SOURCE_POINTER_PRODUCTION_CONTRACT` | MSEA-R28-T6 decision matrix | ACCEPT |
| Receipt writer declares current receipt version. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | line 16 | `RECEIPT_VERSION` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer keeps downstream release held. | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | line 18 | `DOWNSTREAM_RELEASE_HELD` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer exposes the quality/source-pointer missing token. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | line 49 | `QUALITY_OR_SOURCE_POINTER_MISSING` | MinerU metadata receipt writer validation | ACCEPT |
| Receipt writer owns the receipt dataclass and receipt builder. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 67 and 133 | `MineruMetadataReceipt`; `build_mineru_metadata_receipt` | MinerU metadata receipt writer | ACCEPT |
| Receipt payload emits quality report and source pointer metadata fields. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 185, 198, and 202 | `mineru_metadata_receipt_payload`; `qualityReportRef`; `sourcePointer` | MinerU metadata receipt writer payload | ACCEPT |
| Receipt checker requires quality report and source pointer fields. | RUNTIME_BEHAVIOR | `governance/compat/check_mineru_receipt_boundary.py` | lines 47-48 and 307-320 | `qualityReportRef`; `sourcePointer`; `QUALITY_OR_SOURCE_POINTER_MISSING` | MinerU receipt boundary checker | ACCEPT |
| Extraction Foundation owns a quality report dataclass. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 101 | `ExtractionQualityReport` | Extraction Foundation pipeline | ACCEPT |
| Extraction Foundation owns storage-boundary quality state. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 152 | `ExtractionStorageBoundary` | Extraction Foundation pipeline | ACCEPT |
| Extraction Foundation owns quality evaluation logic. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 233 | `evaluate_extraction_quality` | Extraction Foundation pipeline | ACCEPT |
| Extraction Foundation owns storage-boundary construction. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 422 | `build_extraction_storage_boundary` | Extraction Foundation pipeline | ACCEPT |
| Focused tests already cover receipt payload fields and fail-closed metadata validation. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 47-65 and 109-145 | `test_receipt_payload_contains_required_r24_r26_metadata_fields`; `test_invalid_metadata_fails_closed` | MinerU metadata receipt writer tests | ACCEPT |
| Focused tests already cover storage-boundary determinism and quality report ownership. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_pipeline.py` | lines 330-359 | `test_extraction_storage_boundary_is_deterministic_and_counts_chunks` | Extraction pipeline tests | ACCEPT |
| R24-T4 policy permits metadata-only receipt evidence while keeping generated output content private. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | private-output policy rows | `outputContentRead`; `privateOutputDisposition`; `RECEIPT_METADATA_ALLOWED` | MSEA-R24-T4 private-output policy | ACCEPT |
| R27 leaves memory write unauthorized until quality/source pointer, downstream use, and memory-owner prerequisites are met. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | route readiness rows | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED`; `NOT_AUTHORIZED_BY_R27` | MSEA-R27 decision ledger | ACCEPT |

## New Doc-Only Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `ACTUAL_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTATION` | selected R28-T7 route for deterministic helper implementation | DOC_ONLY_NEW | use in dispatch and worker return only |
| `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTED` | expected worker result token if source/test implementation passes | DOC_ONLY_NEW | use only with focused test and gate evidence |
| `MEMORY_ROUTE_HELD_PENDING_ALLOWED_DOWNSTREAM_USE_AND_MEMORY_OWNER_DECISION` | memory-route disposition after T7 implementation | DOC_ONLY_NEW | preserve memory hold even if helper implementation is accepted |

## New Implementation Symbols

| Proposed symbol | Target file | Required purpose | Source-verification status |
| --- | --- | --- | --- |
| `MineruQualityReportSourcePointer` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | immutable metadata-only value object carrying bounded `quality_report_ref` and `source_pointer` strings | new implementation symbol authorized by this baseline |
| `build_mineru_quality_report_source_pointer` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | deterministic helper that derives bounded metadata identifiers from caller-supplied quality/storage metadata without reading content | new implementation symbol authorized by this baseline |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned R28-T7 dispatch paths absent before authoring | `Test-Path` returned `False` for planned R28-T7 baseline, work order, and worker return paths. | PASS |
| Token search for R28-T7 before authoring | `rg -n "MSEA-R28-T7|ACTUAL_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTATION|QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTED|quality report source pointer production implementation" docs CVF_SESSION governance EXTENSIONS` returned only active session next-move references before this packet was created. | PASS |
| Current receipt source check | `rg -n "qualityReportRef|sourcePointer|QUALITY_OR_SOURCE_POINTER_MISSING|RECEIPT_VERSION|DOWNSTREAM_RELEASE_HELD" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py governance/compat/check_mineru_receipt_boundary.py EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests` confirmed R28-T5 receipt-side fields, checker token, and tests exist. | PASS |
| Current quality/storage owner check | `rg -n "ExtractionQualityReport|ExtractionStorageBoundary|evaluate_extraction_quality|build_extraction_storage_boundary|quality_report|source_hash" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests` confirmed quality/storage primitives and tests exist. | PASS |
| Freshness disposition | Current source has receipt references and quality/storage owner surfaces, but no helper that produces the bounded receipt references from quality/storage metadata; R28-T7 may dispatch implementation. | PASS |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Exact search roots | `docs`, `CVF_SESSION`, `governance`, and `EXTENSIONS` | PASS |
| Exact search command or query | `rg -n "MSEA-R28-T7|ACTUAL_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTATION|QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTED|quality report source pointer production implementation" docs CVF_SESSION governance EXTENSIONS` | PASS |
| Coverage across source/tests/docs/JSON/external evidence | The search included governed docs, generated session JSON, governance code, and Extraction Foundation source/test surfaces. | PASS |
| Same-token collision result | Current occurrences before authoring were session next-move references, not an existing R28-T7 dispatch artifact or implementation. | PASS |
| Absent-versus-collision disposition | No dedicated R28-T7 baseline, work order, worker return, source helper, or focused T7 tests existed before authoring; session references are routing evidence only. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor requirement | Source evidence | R28-T7 handling |
| --- | --- | --- |
| R28-T6 decided actual quality/source-pointer production should be implemented next | material commit `6bad1865`; R28-T6 worker return and matrix | authorize deterministic local source/test implementation |
| Receipt writer already accepts `qualityReportRef` and `sourcePointer` metadata | writer and checker source rows above | worker adds production helper rather than changing receipt schema |
| R24-T4 requires no private/generated output content read | R24-T4 policy row above | helper must use caller-supplied metadata only |
| R27 memory-safe candidate still requires downstream and memory-owner decisions | R27 row above | memory route remains held after T7 |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Extraction Foundation local Python helper and focused tests | internal worker may implement deterministic local metadata helper under WORKER_MUST_NOT_COMMIT; reviewer must accept before closure | this GC-018, paired work order, source verification, worker return, focused pytest | local helper only; no runtime adapter or memory write | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP or external adapter owner in R28-T7 | external ingress, authentication, approval, receipt, raw-data, mutation, and public boundaries remain out of scope | no source-verified external adapter authority in R28-T7 | adapter deferred; no CLI/MCP surface implemented or claimed | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Corpus scan or extraction intake |
| Chain map route | extraction/source evidence -> CVF-owned references and runtime source verification -> fresh GC-018/work order -> autorun pre-dispatch gates |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired R28-T7 GC-018 and work order |
| Disposition | ADAPT accepted R28-T6 decision evidence into a bounded implementation dispatch; no external source becomes authority by itself |
| Claim boundary | routing evidence only; no external repository absorption, private/generated content read, MinerU runtime, provider/live proof, public-sync, app, or production claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Guard owner | `governance/compat/check_foundation_storage_layout.py` |
| Trigger reason | this baseline authorizes a worker return under `docs/reviews/` and bounded source/test edits under an existing extension |
| Stable location decision | no new stable reference family or generated aggregate is created |
| Index or front-door decision | N/A with reason: no new stable reference front door is introduced |
| Archive or rotation decision | N/A with reason: no existing durable governance file is split, moved, archived, or rotated in this dispatch |
| Generated aggregate decision | no generated aggregate edit is authorized |
| Claim boundary | storage-layout evidence only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T7 dispatch baseline for deterministic quality-report/source-pointer metadata production helper |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata receipt source and checker evidence are cited, but this baseline creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this baseline runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local file reads, source verification, scaffold generation, and governance dispatch gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | dispatch authoring for deterministic local metadata helper implementation |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior or memory write without fresh source-verified authorization. |

## Evidence / Verification

| Evidence item | Required result | Current dispatch evidence |
| --- | --- | --- |
| Source verification | ACCEPT rows cite CVF-governed surfaces or current runtime source | Source Verification Block in this baseline and paired work order |
| Prior decision release | R28-T6 accepted production-decision matrix | R28-T6 worker return, companion matrix, material commit `6bad1865`, and session-sync commit `75802a8d` |
| Dispatch gates | pre-dispatch autorun must pass before worker execution begins | pending gate evidence in dispatcher final report |
| Worker implementation evidence | worker return, focused pytest, worker-return fast gate, pre-implementation autorun | required by paired work order; not produced by this baseline |
| Claim exclusions | no runtime/provider/live/public/private-content/app/legal/deep-quality claim | Claim Boundary and Public Export Disposition in this baseline |

## Claim Boundary

This baseline authorizes dispatch of a no-commit worker to implement a
deterministic local metadata helper and focused tests for MinerU
quality-report/source-pointer production. It does not release memory/RAG, run
MinerU, read private/generated content, create a runtime receipt, edit checker
or hook catalogs, make public or provider claims, build an app, or claim
extraction accuracy, document truth, legal quality, current-law correctness,
workflow-chain production readiness, worker commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T7 is private provenance dispatch work and does not change the
public-sync repository or public catalog.
