# CVF GC-018 Baseline - MSEA-R28-T5 MinerU Quality Source Pointer Receipt Schema Extension And Checker Update Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T5-QUALITY-SOURCE-POINTER-RECEIPT-SCHEMA-EXTENSION

rawMemoryReleased: false

dispatchBaseHead: 1443bf09

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: worker role, not a specific provider name

## Purpose

Authorize one bounded worker tranche to extend the MinerU metadata receipt
schema with metadata-only quality/source-pointer references and update the
existing MinerU receipt-boundary checker and focused tests to enforce those
fields.

This baseline does not authorize MinerU runtime execution, private or generated
content reads, Candidate Group A import, memory/RAG writes, provider/live proof,
public-sync, standalone app work, legal/use-case deep dive, extraction accuracy,
document truth, legal quality, current-law correctness, workflow-chain
production readiness, worker stage, worker commit, or push.

## Scope / Target / Owner Boundary

Allowed worker target: schema-helper extension in the existing metadata receipt
writer, matching writer tests, existing receipt-boundary checker update,
matching checker tests, and a no-commit worker return.

Allowed worker output paths:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`
- `governance/compat/check_mineru_receipt_boundary.py`
- `governance/compat/test_check_mineru_receipt_boundary.py`
- `docs/reviews/CVF_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_WORKER_RETURN_2026-07-04.md`
- `docs/corpus-intelligence/registry/entries/msea-r28-t1-mineru-metadata-receipt-writer-source.json` only if GC-051 requires metadata update for the changed writer source
- `docs/corpus-intelligence/registry/entries/msea-r28-t1-mineru-metadata-receipt-writer-tests.json` only if GC-051 requires metadata update for the changed writer tests
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only when regenerated from source entries by the existing registry generator

Forbidden paths and actions: no edits to active session state, active handoff,
root startup files, AGENTS.md, public-sync clone, product runtime, Web/UI,
MCP/CLI adapter, memory/RAG owner, Candidate Group A source or generated output,
private source documents, generated MinerU output content, or runtime receipt
instances.

## Baseline Decision

| Field | Value |
| --- | --- |
| selectedRoute | `QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION` |
| releaseBasis | R28-T4 material commit `0c81b7bc` accepted the local receipt-boundary checker and kept the quality/source-pointer prerequisite held. |
| implementationBoundary | writer schema helper, writer tests, existing checker update, checker tests, conditional registry metadata update, and worker return |
| memoryRouteDisposition | `MEMORY_ROUTE_STILL_HELD_AFTER_CHECKER_IMPLEMENTATION`; this tranche may add quality/source-pointer receipt fields but does not authorize memory writes. |
| runtimeDisposition | no MinerU runtime execution, no private/generated content read, no extraction accuracy or document-truth claim |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T5 --title "MinerU Quality Source Pointer Receipt Schema Extension And Checker Update Decision" --date 2026-07-04 --base 1443bf09 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile, with protected governance path trigger active |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled R28-T5 purpose, source verification, proposed field table, protected-path authorization, worker output manifest, handoff controls, and memory-route hold boundaries |
| checkerReadAheadConfirmation | dispatch-quality, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, corpus-scan-registry, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `qualityReportRef`; `sourcePointer`; `QUALITY_OR_SOURCE_POINTER_MISSING`; `QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION`; `MEMORY_ROUTE_STILL_HELD_AFTER_QUALITY_SOURCE_POINTER_SCHEMA_EXTENSION` |
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
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, scaffold output, source verification, protected-path authorization, and worker-output checker read-ahead. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Core Guard Self-Protection Authorization; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; Resolver query; Returned defects: NONE_RETURNED; Public Export Disposition; Delta Execution Claim Boundary Control Block; protected paths; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers the R28-T5 dispatch packet only; worker-created source, tests, registry entries, and worker return require their own source and checker read-ahead before editing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session state releases R28-T5 packet authoring from accepted R28-T4 checker evidence. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `MSEA-R28-T5`; `0c81b7bc` | active session bootstrap read model | ACCEPT |
| R28-T4 closure accepts the checker and keeps the memory route held. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T4MineruReceiptBoundaryCheckerImplementationClosure20260704.json` | value fields | `selectedImplementationDisposition`; `memoryRouteDisposition`; `nextRecommendedMove` | active session state entry | ACCEPT |
| R28-T4 worker return recommends a future R28-T5 quality/source-pointer field tranche and states the checker alone does not satisfy memory prerequisites. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_WORKER_RETURN_2026-07-04.md` | lines 135-147 and 259-267 | `MEMORY_ROUTE_STILL_HELD_AFTER_CHECKER_IMPLEMENTATION`; `quality/source-pointer field` | R28-T4 worker return | ACCEPT |
| R28-T3 design matrix names the quality/source-pointer prerequisite as a future field absent from the R28-T1 receipt shape. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_MATRIX_2026-07-04.md` | lines 68 and 76 | `QUALITY_OR_SOURCE_POINTER_MISSING`; `Quality/source-pointer field` | R28-T3 design matrix | ACCEPT |
| R27 requires receipt, quality, source pointer, allowed downstream use, and claim boundary before memory-safe candidate readiness. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 73-86 | `QUALITY_DISPOSITION_READY`; `MEMORY_SAFE_CANDIDATE_READY` | R27 decision ledger | ACCEPT |
| Extraction Foundation pipeline owns quality, chunk, and storage-boundary primitives a future memory-safe route would consume. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | lines 101, 117, 152, and 424-438 | `ExtractionQualityReport`; `ExtractionChunk`; `ExtractionStorageBoundary`; `build_extraction_storage_boundary` | Extraction Foundation pipeline | ACCEPT |
| R28-T1 writer currently owns the metadata receipt dataclass, builder, payload renderer, and JSON renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 16-18, 66-77, 112, 159, 178 | `RECEIPT_VERSION`; `DOWNSTREAM_RELEASE_HELD`; `MineruMetadataReceipt`; `build_mineru_metadata_receipt`; `mineru_metadata_receipt_payload`; `render_mineru_metadata_receipt_json` | Extraction Foundation metadata receipt writer | ACCEPT |
| R28-T1 writer tests currently assert existing metadata receipt payload fields and held downstream release. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 46-59 and 137 | `sourceInputSlot`; `inputSha256`; `privateOutputDisposition`; `DOWNSTREAM_RELEASE_HELD` | Extraction Foundation metadata receipt writer tests | ACCEPT |
| R28-T4 checker currently owns receipt required-field checks and validation dispatch. | EXISTS | `governance/compat/check_mineru_receipt_boundary.py` | lines 36-47 and 209-238 | `REQUIRED_FIELDS`; `_validate_receipt`; `INVALID_PRIVATE_OUTPUT_DISPOSITION` | MinerU receipt boundary checker | ACCEPT |
| R28-T4 checker tests currently own focused validation coverage for required fields and held downstream release. | EXISTS | `governance/compat/test_check_mineru_receipt_boundary.py` | lines 85, 115, 121, and 127 | `INVALID_PRIVATE_OUTPUT_DISPOSITION`; `DOWNSTREAM_RELEASE_CLAIMS_UNAUTHORIZED_ROUTE`; `SOURCE_SLOT_EXPOSES_SENSITIVE_DETAIL` | MinerU receipt boundary checker tests | ACCEPT |

## New Proposed Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `qualityReportRef` | metadata-only pointer to an authorized quality report or quality disposition record | DOC_ONLY_NEW | implement only if source-safe, bounded, and no content read is required |
| `sourcePointer` | metadata-only source pointer identifier for downstream traceability | DOC_ONLY_NEW | implement as bounded metadata, not a source document path/body quote |
| `QUALITY_OR_SOURCE_POINTER_MISSING` | checker failure token for absent or invalid quality/source-pointer references | DOC_ONLY_NEW | add to checker only with focused tests |
| `MEMORY_ROUTE_STILL_HELD_AFTER_QUALITY_SOURCE_POINTER_SCHEMA_EXTENSION` | R28-T5 held-lane token | DOC_ONLY_NEW | preserve memory hold even if schema/checker update passes |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned R28-T5 dispatch paths absent before authoring | `Test-Path` returned `False` for the planned R28-T5 GC-018, work order, and worker return paths. | PASS |
| Existing quality/source-pointer implementation search | `rg -n "qualityReportRef|sourcePointer|sourcePointerRef|qualityReportRef|QUALITY_OR_SOURCE_POINTER_MISSING" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests governance/compat docs/reference docs/reviews` returned only the R28-T3 design matrix prerequisite row before authoring. | PASS |
| Existing checker owner check | `rg -n "REQUIRED_FIELDS|def _validate_receipt|INVALID_PRIVATE_OUTPUT_DISPOSITION" governance/compat/check_mineru_receipt_boundary.py` confirmed the current checker owner surface. | PASS |
| Freshness disposition | No current writer or checker implementation owns `qualityReportRef`, `sourcePointer`, or `QUALITY_OR_SOURCE_POINTER_MISSING`; R28-T5 may dispatch a bounded worker to add them. | PASS |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact paths absent before authoring | `Test-Path` returned `False` for the planned R28-T5 GC-018, work order, and worker return paths. | PASS |
| Token search for R28-T5 lane before authoring | `rg -n --fixed-strings "MSEA-R28-T5" docs CVF_SESSION governance EXTENSIONS` returned only current session next-move references before this packet was created. | PASS |
| Collision decision | No existing R28-T5 dispatch or worker return exists; this baseline may create the first dispatch packet. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor requirement | Source evidence | R28-T5 handling |
| --- | --- | --- |
| R28-T4 accepted checker but held memory route | material commit `0c81b7bc`; worker return and state entry | allow one quality/source-pointer schema/checker update tranche |
| R28-T3 named quality/source-pointer as future field | design matrix lines 68 and 76 | create bounded fields and checker validation |
| R27 memory-safe candidate requires receipt, quality, source pointer, downstream use, and claim boundary | decision ledger lines 73-86 | keep memory route held; no memory write or RAG release |
| R28-T1 writer owns current receipt schema | writer source/tests | update writer source/tests only within allowed scope |
| R28-T4 checker owns receipt-boundary gate | checker source/tests | update checker source/tests only within allowed scope |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | writer helper plus local governance checker | internal worker may extend metadata schema and checker under WORKER_MUST_NOT_COMMIT; reviewer must accept before closure | this GC-018, paired work order, source verification, focused tests, worker return | internal-only Python helper/checker; no external adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP or external adapter owner in R28-T5 | external ingress, authentication, approval, receipt, raw-data, mutation, and public boundaries remain out of scope | no source-verified external adapter authority in R28-T5 | adapter deferred; no CLI/MCP surface implemented or claimed | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Corpus scan or extraction intake |
| Chain map route | extraction/source evidence -> CVF-owned references and runtime source verification -> fresh GC-018/work order -> autorun pre-dispatch gates |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired R28-T5 GC-018 and work order |
| Disposition | ADAPT prior R27/R28 evidence into a bounded quality/source-pointer schema/checker dispatch; no external source becomes authority by itself |
| Claim boundary | routing evidence only; no external repository absorption, private/generated content read, runtime/provider/live proof, public-sync, app, or production claim |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update the existing MinerU receipt-boundary
checker and focused tests only as needed to enforce the new metadata-only
quality/source-pointer receipt fields.

Protected paths:

- `governance/compat/check_mineru_receipt_boundary.py`
- `governance/compat/test_check_mineru_receipt_boundary.py`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only when regenerated from source entries

Operator authorization: operator asked to write the next-tranche work order
after accepting R28-T4.

Rollback boundary: revert only R28-T5 worker changes if rejected; do not revert
R28-T4 material commit `0c81b7bc` or older MSEA history.

Not authorized: no session-state edit by worker, AGENTS.md edit, active handoff
edit, MinerU runtime execution, private/generated content read, memory/RAG
write, provider/live proof, public-sync, external adapter, standalone app,
legal/use-case deep dive, extraction accuracy, document truth, current-law
correctness, workflow-chain production readiness, worker stage, worker commit,
or push.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T5 dispatch baseline for metadata-only quality/source-pointer receipt schema and checker update |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor writer/checker evidence is cited, but this baseline creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this baseline runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local file reads, source verification, scaffold generation, and governance dispatch gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | dispatch authoring for a local schema/checker tranche only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior or memory write without fresh source-verified authorization. |

## Evidence / Verification

| Evidence item | Required result | Current dispatch evidence |
| --- | --- | --- |
| Source verification | ACCEPT rows cite CVF-governed surfaces or current runtime source | Source Verification Block in this baseline and paired work order |
| Prior implementation release | R28-T4 accepted checker and held memory route | R28-T4 worker return, active session state entry, and material commit `0c81b7bc` |
| Dispatch gates | pre-dispatch autorun must pass before worker implementation begins | pending gate evidence in dispatcher final report |
| Worker implementation evidence | focused tests, writer/checker diff, worker return, and no-commit proof | required by paired work order; not produced by this baseline |
| Claim exclusions | no runtime/provider/live/public/private-content/app/legal/deep-quality claim | Claim Boundary and Public Export Disposition in this baseline |

## Claim Boundary

This baseline authorizes dispatch of a no-commit worker to extend metadata-only
receipt schema fields for quality/source-pointer references and update the
existing receipt-boundary checker/tests. It does not release memory/RAG, run
MinerU, read private/generated content, create a runtime receipt, make public or
provider claims, build an app, or claim extraction accuracy, document truth,
legal quality, current-law correctness, workflow-chain production readiness,
worker commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T5 is private provenance schema/checker dispatch work and does not
change the public-sync repository or public catalog.
