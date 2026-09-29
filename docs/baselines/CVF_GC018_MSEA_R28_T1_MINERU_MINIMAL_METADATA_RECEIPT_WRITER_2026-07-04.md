# CVF GC-018 Baseline - MSEA-R28-T1 MinerU Minimal Metadata Receipt Writer

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA-R28-T1

rawMemoryReleased: false

Dispatch base head: 0892f634

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: worker role, not a specific provider name

## Purpose

Authorize one bounded implementation tranche for a deterministic
metadata-only MinerU receipt writer in Extraction Foundation. The writer may
turn caller-supplied private-test metadata into a governed receipt object or
payload, but it must not execute MinerU, read source documents, read generated
output content, write memory, write RAG, or claim product/app readiness.

## Scope / Target / Owner Boundary

Allowed target: a small local helper under Extraction Foundation plus focused
tests and a worker return.

Allowed implementation paths:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`
- `docs/reviews/CVF_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_WORKER_RETURN_2026-07-04.md`

Forbidden paths and actions: no MinerU runtime execution, model/cache mutation,
private document body read, generated output content read or quotation,
Candidate Group A source or generated output import, public-sync,
provider/live proof, checker implementation, memory-layer or RAG write,
adapter implementation, S3, Web, MCP, model-router, action-authority,
standalone PDF app, legal/use-case deep dive, package lifecycle mutation,
production-readiness claim, stage by worker, commit by worker, or push.

## Owner / Source

This baseline is owned by the R28 route selection and accepted MSEA owner
surfaces. It releases only the first implementation step selected by R28:
`MINIMAL_METADATA_RECEIPT_WRITER`.

## Protocol / Contract / Requirements

The worker must implement a deterministic local metadata writer that:

- accepts caller-supplied receipt metadata only;
- validates required R24/R26 fields;
- keeps `outputContentRead` false for this tranche;
- permits safe MinerU output filename-family metadata only;
- emits an explicit claim boundary and held downstream-release status;
- returns or renders stable data suitable for future checker work;
- includes focused tests proving privacy, required-field, filename, and
  downstream-release boundaries.

## Baseline Decision

| Field | Value |
| --- | --- |
| selectedRoute | `MINIMAL_METADATA_RECEIPT_WRITER` |
| releaseBasis | R28 selection commit `e2bb6b61` selected the writer-first lane and current session state at `0892f634` routes the next allowed move to this dispatch. |
| implementationBoundary | source/test/worker-return only, under WORKER_MUST_NOT_COMMIT |
| heldLanes | checker, memory-safe candidate, memory write, RAG write, runtime workflow, standalone app, and legal/use-case deep dive |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T1 --title "MinerU Minimal Metadata Receipt Writer" --date 2026-07-04 --base 0892f634 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with R28/R27/R26/R24 source verification, narrow implementation scope, worker manifest, and gate list |
| checkerReadAheadConfirmation | dispatch-quality, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, and structural-completeness checker sources were read before authoring |
| docOnlyNewFields | none; new implementation symbols are assigned to worker allowed scope, not source-verified as existing fields |
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
| Dispatch impact | No ADIF-specific extra instruction is required beyond the active guard orientation and literal-format gotchas. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; claimBoundary; Resolver query; Returned defects: NONE_RETURNED; Public Export Disposition; Delta Execution Claim Boundary Control Block; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates must confirm dispatch shape and must not be used as first discovery. |
| claimBoundary | This read-ahead covers the R28-T1 dispatch packet only; worker-created outputs must perform their own checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R28 selected the minimal metadata receipt writer as the first implementation sequence item. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_FOUNDATION_IMPLEMENTATION_SEQUENCE_AUDIT_AND_SELECTION_2026-07-04.md` | Decision / Disposition and R28 Selection Matrix | `SELECT_MINIMAL_METADATA_RECEIPT_WRITER_FIRST`; `MINIMAL_METADATA_RECEIPT_WRITER` | MSEA-R28 selection review | ACCEPT |
| R27 lists receipt writer implementation as a candidate next packet and keeps checker, memory, runtime, and app lanes sequenced or held. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | implementation sequence matrix | `Receipt writer implementation`; `Receipt checker implementation`; `Memory write adapter`; `MinerU runtime workflow` | MSEA-R27 decision ledger | ACCEPT |
| R26 defines the metadata-only receipt fields and keeps writer/checker implementation unauthorized until fresh GC-018. | VALUE_SET | `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | Receipt Schema Draft and Writer Contract Draft | `receiptId`; `outputContentRead`; `privateOutputDisposition`; `downstreamRelease`; `NOT_AUTHORIZED_BY_R26` | MSEA-R26 receipt contract | ACCEPT |
| R24-T4 defines the receipt envelope and private output classes for committed metadata only. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | Receipt Envelope and Private Output Class Matrix | `PRIVATE_INPUT_ONLY`; `PRIVATE_RUNTIME_COPY`; `PRIVATE_GENERATED_OUTPUT`; `RECEIPT_METADATA_ALLOWED`; `EXCERPT_MINIMAL_SEPARATE_AUTHORITY` | MSEA-R24-T4 private-output policy | ACCEPT |
| MinerU source mirror documents safe output filename families that can be used as metadata-only names. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | output file sections and summary list | `layout.pdf`; `span.pdf`; `model.json`; `middle.json`; `content_list.json`; `content_list_v2.json`; `*.md` | MinerU source mirror output docs | ACCEPT |
| Extraction Foundation has deterministic scan-route owner logic and no OCR/provider execution in that owner. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | module contract and route function | `decide_scan_route`; `ScanRouteDecision`; `DocumentScanSignals` | Extraction Foundation scan route | ACCEPT |
| Extraction Foundation has private-safe metadata evidence records and raw-content pointer rejection. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py` | record/evaluation helpers | `MetadataEvidenceRecord`; `evaluate_metadata_evidence`; `RAW_CONTENT_FORBIDDEN` | Extraction Foundation metadata evidence | ACCEPT |
| Extraction Foundation has bounded scan-outcome report rendering and file writing helpers. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | report dataclass and renderer helpers | `ScanOutcomeReport`; `build_scan_outcome_report`; `write_scan_outcome_report_files` | Extraction Foundation scan outcome report | ACCEPT |
| Extraction Foundation has quality, chunk, and storage-boundary primitives, but no MinerU metadata receipt writer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | extraction pipeline dataclasses and builders | `ExtractionQualityReport`; `ExtractionChunk`; `ExtractionStorageBoundary`; `build_extraction_storage_boundary` | Extraction Foundation pipeline | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned dispatch artifact paths absent before authoring | `Test-Path` returned `False` for the planned GC-018, work order, and worker return paths. | PASS |
| Token search for R28-T1 writer lane before authoring | `rg -n "MSEA-R28-T1\|MINERU_MINIMAL_METADATA_RECEIPT_WRITER\|Minimal Metadata Receipt Writer\|mineru_metadata_receipt_writer" docs CVF_SESSION EXTENSIONS\CVF_EXTRACTION_FOUNDATION` returned only existing R28 next-move continuity references, not an existing dispatch or implementation. | PASS |
| Collision decision | No existing R28-T1 artifact or writer implementation exists; dispatch can create the first packet. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor route item | Source evidence | R28-T1 handling |
| --- | --- | --- |
| Receipt writer implementation | R27 future sequence and R28 selection | release one narrow writer implementation work order |
| Receipt checker implementation | R26 checker candidate and R28 sequence | held for R28-T2 |
| Memory-safe candidate and memory write | R27 scan-to-memory matrix | held until receipt/checker path exists |
| Runtime workflow | R27 and R28 held route | forbidden in R28-T1 |
| Standalone app/legal use case | R27/R28 held or rejected route | forbidden in R28-T1 |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Extraction Foundation helper to be implemented by worker | metadata-only local helper; no file read, runtime run, memory write, or action authority | R24/R26/R27/R28 source verification in this baseline | internal-only helper; no external adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP/API adapter in R28-T1 | external ingress, auth, approval, mutation, raw-data release, and public claims are out of scope | this baseline forbids adapter and public-sync work | deferred adapter owner requires future GC-018 | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted MinerU source mirror and MSEA owner surfaces -> R27 plane route -> R28 selection -> R28-T1 metadata writer dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | this GC-018 baseline and paired work order |
| Disposition | ADAPT: turn accepted receipt-policy and filename-family evidence into a bounded implementation dispatch |
| Claim boundary | no source import, runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, or product-app claim |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R24/R26 receipt fields | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md`; `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | CONFIRMED_EXISTING | implementation is newly authorized only by this dispatch | implement narrowly |
| MinerU filename families | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md`; `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | CONFIRMED_EXISTING | writer may validate safe names as metadata | implement validation |
| Extraction Foundation report/quality owners | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`; `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | ENRICH_EXISTING | writer should align with existing local deterministic style | implement adjacent helper |
| Checker, memory, RAG, runtime, app lanes | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md`; `docs/reviews/CVF_MSEA_R28_FOUNDATION_IMPLEMENTATION_SEQUENCE_AUDIT_AND_SELECTION_2026-07-04.md` | REJECT_DIRECT_IMPORT | not released by R28-T1 | defer |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_FOUNDATION_IMPLEMENTATION_SEQUENCE_AUDIT_AND_SELECTION_2026-07-04.md`

priorVerificationAnchor: R28 selected route plus R24/R26/R27 source owner surfaces

freshRecomputeRequired: yes, worker must re-read the work order, GC-018, and current source files before implementation

unicodePathHandling: use literal UTF-8 paths and PowerShell-safe commands; do not normalize or rewrite source-mirror paths

extractedTextAuthority: no extracted document text authority exists in R28-T1; document text and generated output content remain forbidden

## Acceptance Criteria

| Criterion | Required evidence |
| --- | --- |
| Writer exists and is deterministic | source file plus focused tests |
| Writer is metadata-only | tests show no source document body or generated output content is required or accepted |
| Required R24/R26 fields are preserved | tests cover required field presence and stable rendering |
| Privacy defaults are fail-closed | tests keep `outputContentRead` false and reject unsafe source slots or output names |
| Downstream lanes remain held | receipt payload contains a held downstream-release status and boundary text |
| Worker obeys no-commit mode | worker return records uncommitted changed set and `git status --short` |

## Verification

Required worker gates are listed in the paired work order. Dispatch author must
run pre-dispatch autorun before handing this packet to the worker.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | MSEA-R28-T1 GC-018 dispatch for metadata-only receipt writer |
| claimDisposition | CLAIM_REJECTED: no runtime, execution-control, direct-interception, provider, public, memory, RAG, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: dispatch creates no runtime or writer receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: dispatcher creates governed dispatch artifacts only |
| invocationBoundary | governed markdown dispatch authoring |
| interceptionBoundary | no wrapper/proxy, runtime gate, provider call, memory store, RAG index, adapter, or production enforcement behavior |
| claimLanguage | GC-018 baseline is dispatch-ready for worker execution; implementation result is not claimed here |
| forbiddenExpansion | no MinerU runtime, checker, adapter, memory/RAG, public-sync, provider/live, app, legal/use-case, Web, MCP, model-router, package lifecycle, action-authority, production, stage by worker, commit by worker, or push |

## Claim Boundary

This baseline authorizes only MSEA-R28-T1 dispatch for a deterministic
metadata-only receipt writer helper and focused tests. It does not claim or
authorize MinerU runtime execution, checker implementation, private document
read, generated output content read or quotation, source import, public-sync,
provider/live proof, memory ingestion, RAG write, adapter implementation,
standalone PDF app, legal-quality analysis, extraction accuracy, current-law
correctness, workflow-chain production readiness, action authority, stage by
worker, commit by worker, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T1 uses private provenance MSEA planning and source-mirror evidence.
No public-sync export is authorized.
