# CVF GC-018 Baseline - MSEA-R28-T3 MinerU Receipt Boundary Checker Candidate Design

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA-R28-T3-CHECKER-CANDIDATE-DESIGN

rawMemoryReleased: false

Dispatch base head: 606043f5

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: worker role, not a specific provider name

## Purpose

Authorize one bounded docs-only worker tranche to design the MinerU receipt
boundary checker candidate. The worker must turn accepted R26 criteria,
R28-T1 metadata receipt source behavior, and R28-T2 route-selection evidence
into a concise checker-candidate design matrix without implementing checker
code, hook wiring, runtime execution, memory writes, or use-case/product depth.

## Scope / Target / Owner Boundary

Allowed target: docs-only checker-candidate design evidence.

Allowed worker output paths:

- `docs/reviews/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_WORKER_RETURN_2026-07-04.md`
- `docs/reference/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_MATRIX_2026-07-04.md`

Forbidden paths and actions: no checker implementation, hook wiring,
`governance/compat` mutation, hook catalog mutation, source/test edit, MinerU
runtime execution, model/cache mutation, private document body read, generated
output content read or quotation, Candidate Group A source or generated output
import, public-sync, provider/live proof, memory-layer write, RAG write,
adapter implementation, S3, Web, MCP, model-router, action-authority,
standalone PDF app, legal/use-case deep dive, package lifecycle mutation,
production-readiness claim, worker stage, worker commit, or push.

## Owner / Source

This baseline is owned by the accepted R28-T2 route-selection closure,
R28-T1 metadata receipt writer source and tests, R26 checker-candidate
reference, R27 scan-to-memory route matrix, R24 private-output policy, and
current session state. It releases only design-candidate documentation.

## Protocol / Contract / Requirements

The worker must:

- re-read startup front door, active state, active handoff, guard orientation,
  literal-format gotchas, this baseline, and paired work order;
- read checker source for the worker return and companion reference before
  writing either output artifact;
- verify current R28-T1 writer source and tests for held downstream release and
  output-content-read rejection;
- derive a candidate checker design from R26 and R28-T2, including fields,
  failure classes, evidence inputs, and non-goals;
- keep the result design-only and explicitly defer checker implementation or
  hook wiring to a future fresh GC-018 if the reviewer accepts this design;
- leave memory-route release held pending an actual checker and quality/source
  pointer prerequisites.

## Baseline Decision

| Field | Value |
| --- | --- |
| selectedRoute | `RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY` |
| releaseBasis | Current session state at `606043f5` routes next allowed work to R28-T3 packet authoring after accepted R28-T2 material commit `3e230445`. |
| implementationBoundary | docs-only worker return and checker-candidate design matrix, under WORKER_MUST_NOT_COMMIT |
| heldLanes | checker code, hook wiring, memory-safe candidate implementation, memory write, RAG write, runtime workflow, standalone app, legal/use-case deep dive, provider/live proof, public-sync |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T3 --title "MinerU Receipt Boundary Checker Candidate Design" --date 2026-07-04 --base 606043f5 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled R28-T3 design-only purpose, source verification, no-commit handoff control, worker manifest, checker-output read-ahead mandate, and no-implementation boundaries |
| checkerReadAheadConfirmation | dispatch-quality, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, structural-completeness, and protected-guard-scope checker surfaces were read or compared before authoring |
| docOnlyNewFields | `RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY`; `CHECKER_IMPLEMENTATION_HELD_PENDING_ACCEPTED_DESIGN`; `MEMORY_ROUTE_HELD_PENDING_ACTUAL_CHECKER_AND_QUALITY` |
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
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, scaffold output, and worker-output checker read-ahead. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; claimBoundary; Resolver query; Returned defects: NONE_RETURNED; Public Export Disposition; Delta Execution Claim Boundary Control Block; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers the R28-T3 dispatch packet only; worker-created output artifacts require their own checker-source read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Current session state releases R28-T3 packet authoring after accepted R28-T2 route selection. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `MSEA-R28-T3`; `SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY` | active session bootstrap read model | ACCEPT |
| R28-T2 selected a bounded checker-candidate design route and held memory release pending checker plus quality/source-pointer prerequisites. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_WORKER_RETURN_2026-07-04.md` | Decision / Disposition | `SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY`; `HOLD_MEMORY_ROUTE_RELEASE_PENDING_RECEIPT_CHECKER_AND_QUALITY` | MSEA-R28-T2 worker return | ACCEPT |
| R28-T2 companion matrix marks receipt-boundary checker candidate design as selected and memory-route release as held. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md` | Route Decision Matrix | `SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY`; `HOLD_MEMORY_ROUTE_RELEASE_PENDING_RECEIPT_CHECKER_AND_QUALITY` | MSEA-R28-T2 decision matrix | ACCEPT |
| R26 records checker candidate status and criteria without authorizing checker implementation. | VALUE_SET | `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | Checker Candidate Design | `checkerCandidateStatus`; `CHECKER_CANDIDATE`; `NOT_AUTHORIZED_BY_R26` | MSEA-R26 receipt contract | ACCEPT |
| R24-T4 defines private receipt envelope fields and private output class vocabulary that the design must protect. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | Receipt Envelope and Private Output Class Matrix | `outputContentRead`; `downstreamRelease`; `PRIVATE_INPUT_ONLY`; `PRIVATE_RUNTIME_COPY`; `PRIVATE_GENERATED_OUTPUT` | MSEA-R24-T4 private-output policy | ACCEPT |
| R28-T1 writer source exposes a held downstream-release constant and rejects output-content-read true. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 18, 66-76, 112-138, 160-178 | `DOWNSTREAM_RELEASE_HELD`; `MineruMetadataReceipt`; `build_mineru_metadata_receipt`; `render_mineru_metadata_receipt_json` | Extraction Foundation metadata receipt writer | ACCEPT |
| R28-T1 writer tests prove stable payload, held downstream release, and false output-content-read behavior. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 59, 63-64, 90-112 | `render_mineru_metadata_receipt_json`; `output_content_read`; `DOWNSTREAM_RELEASE_HELD` | Extraction Foundation metadata receipt writer tests | ACCEPT |
| R27 scan-to-memory route matrix requires receipt, quality, source pointer, allowed downstream use, and claim boundary before memory-safe candidate readiness. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | Scan-To-Memory Intake Route Matrix | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED`; `NOT_AUTHORIZED_BY_R27` | MSEA-R27 decision ledger | ACCEPT |
| Extraction Foundation pipeline owns quality, chunk, source-hash, and storage-boundary primitives for future memory-safe routing. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | lines 101-157 and 372-489 | `ExtractionQualityReport`; `ExtractionChunk`; `ExtractionStorageBoundary` | Extraction Foundation pipeline | ACCEPT |

## New Doc-Only Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY` | selected R28-T3 route token | DOC_ONLY_NEW | use for design readiness only, not checker code |
| `CHECKER_IMPLEMENTATION_HELD_PENDING_ACCEPTED_DESIGN` | downstream implementation hold token | DOC_ONLY_NEW | use if design is complete but implementation remains unauthorized |
| `MEMORY_ROUTE_HELD_PENDING_ACTUAL_CHECKER_AND_QUALITY` | memory route hold token for R28-T3 | DOC_ONLY_NEW | preserve R28-T2 memory hold until actual checker and quality/source-pointer prerequisites exist |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact paths absent before authoring | `Test-Path` returned `False` for the planned GC-018, work order, worker return, and companion design matrix paths. | PASS |
| Token search for R28-T3 lane before authoring | `rg -n "MSEA-R28-T3\|R28_T3\|RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN\|CHECKER_CANDIDATE_DESIGN_ONLY" docs CVF_SESSION EXTENSIONS governance` returned only current session next-move references and no existing R28-T3 packet. | PASS |
| Collision decision | No existing R28-T3 dispatch or output artifact exists; this baseline may create the first packet. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor route item | Source evidence | R28-T3 handling |
| --- | --- | --- |
| Receipt writer implementation | R28-T1 material commit `23177f27` and source/tests | accept as concrete receipt-shape evidence |
| Receipt checker candidate design | R28-T2 material commit `3e230445`; R26 checker candidate reference | design candidate matrix only |
| Memory-safe candidate contract | R27 sequence and R28-T2 held memory route | keep held until actual checker and quality/source-pointer prerequisites exist |
| Memory write adapter | R27 held lane | keep held |
| Runtime workflow and standalone app | R27/R28 held route and operator CVF-foundation instruction | keep held |

## Core Guard Self-Protection Authorization

| Field | Value |
| --- | --- |
| Authorized guard-maintenance scope | none |
| Protected paths | no `governance/compat/*.py`, hook catalog, autorun catalog, AGENTS.md, or session-state path is authorized for worker edits |
| Operator authorization | operator authorized next work-order creation for design-only checker-candidate packet, not checker implementation |
| Rollback boundary | if design evidence requires checker source changes, return BLOCKED_WITH_REASON instead of editing protected paths |
| Not authorized | no checker implementation, hook wiring, generated-state mutation, protected governance mutation, or session-sync by worker |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 writer and R28-T2 route selection -> R28-T3 checker-candidate design |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | this GC-018 baseline and paired work order |
| Disposition | ADAPT: convert accepted receipt and route evidence into a bounded checker-candidate design packet |
| Claim boundary | no source import, runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker implementation, or product-app claim |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R28-T1 metadata writer | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`; R28-T1 tests | CONFIRMED_EXISTING | concrete receipt shape and validation behavior | use as candidate-design input |
| R26 checker candidate criteria | R26 receipt contract reference | ENRICH_EXISTING | R28-T3 can organize criteria into a design matrix | design only |
| R28-T2 selected route | R28-T2 worker return and companion matrix | ENRICH_EXISTING | turns route decision into worker-dispatchable design work | dispatch design packet |
| Memory-safe candidate route | R27 decision ledger and Extraction Foundation quality owners | CONFIRMED_EXISTING | no new release evidence yet | keep held |
| Runtime, app, use-case, memory-write lanes | R27/R28 held surfaces and operator instruction | REJECT_DIRECT_IMPORT | useful later but outside current CVF-foundation step | keep held |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_WORKER_RETURN_2026-07-04.md`

priorVerificationAnchor: R28-T2 selected checker-candidate design route and held memory-route evidence

freshRecomputeRequired: yes, worker must re-read the work order, GC-018,
current writer source/tests, and current R24/R26/R27/R28 owner surfaces before
writing outputs.

unicodePathHandling: ASCII-only artifact paths in this dispatch.

extractedTextAuthority: no private document text or generated output content is
authorized.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit worker -> reviewer/closer -> session-sync steward |
| phase | pre-dispatch |
| baseHeadFor(phase) | dispatchBaseHead=606043f5; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatcher owns this GC-018 and paired work order; worker owns only worker return and companion design matrix; reviewer owns closure repairs and material commit; steward owns session-sync when closure exists |
| traceScope(phase, actor) | each actor records before status, after status, diff evidence, and no-commit or commit ownership evidence |
| commitOwner(phase) | dispatcher may commit dispatch; worker is WORKER_MUST_NOT_COMMIT; reviewer/closer may commit accepted worker outputs; session-sync steward may commit continuity updates only when material closure exists |
| crossBatchIsolation | R28-T3 must not edit source/tests, checker code, hook catalogs, R27/R26/R24 owner surfaces, runtime outputs, private source documents, generated output content, public-sync clone, protected governance code, or generated session state |
| nextMoveSurfaces | reviewer/closer and session-sync steward update next allowed move only when accepted R28-T3 closure exists |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_COMPLETION_2026-07-04.md` |
| reviewerOwnedClosurePaths | worker return, companion design matrix, and allowed reviewer repairs inside those artifacts only |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T3 docs-only dispatch baseline |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no new runtime receipt is created or consumed by this baseline. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this baseline. |
| invocationBoundary | local file reads, searches, scaffold generation, and governance dispatch gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | checker-candidate design dispatch baseline only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without fresh source-verified authorization. |

## Claim Boundary

This baseline authorizes a docs-only checker-candidate design worker tranche.
It does not authorize checker code, hook wiring, MinerU runtime, private content
read, generated output read, memory/RAG write, adapter work, public-sync,
provider/live proof, standalone app work, legal/use-case deep dive, or
production workflow-chain claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T3 is private provenance dispatch work and does not change the
public-sync repository or public catalog.
