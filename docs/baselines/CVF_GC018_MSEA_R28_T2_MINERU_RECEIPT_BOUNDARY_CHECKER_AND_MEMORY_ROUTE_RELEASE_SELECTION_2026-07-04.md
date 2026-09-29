# CVF GC-018 Baseline - MSEA-R28-T2 MinerU Receipt Boundary Checker And Memory Route Release Selection

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA-R28-T2-ROUTE-SELECTION

rawMemoryReleased: false

Dispatch base head: 95734097

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: worker role, not a specific provider name

## Purpose

Authorize one bounded route-selection tranche following the accepted R28-T1
metadata receipt writer. The worker must source-verify whether the next useful CVF-foundation
move is a receipt-boundary checker-candidate design, and must decide whether
memory-route release remains held until receipt, quality, and checker
preconditions are satisfied.

## Scope / Target / Owner Boundary

Allowed target: docs-only source-verified decision work.

Allowed worker output paths:

- `docs/reviews/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_WORKER_RETURN_2026-07-04.md`
- `docs/reference/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md`

Forbidden paths and actions: no MinerU runtime execution, model/cache
mutation, private document body read, generated output content read or
quotation, Candidate Group A source or generated output import, public-sync,
provider/live proof, checker implementation, hook wiring, memory-layer write,
RAG write, adapter implementation, S3, Web, MCP, model-router,
action-authority, standalone PDF app, legal/use-case deep dive, package
lifecycle mutation, production-readiness claim, worker stage, worker commit, or
push.

## Owner / Source

This baseline is owned by the R28 closed writer tranche, R27 plane integration
ledger, R26 receipt contract, R24 private-output policy, and current session
state. It releases only route-selection and design-readiness classification.

## Protocol / Contract / Requirements

The worker must:

- re-read the startup front door, active state, active handoff, guard
  orientation, literal-format gotchas, this baseline, and paired work order;
- read checker source before writing the worker return or companion reference;
- verify R28-T1 writer output boundaries from current source and worker return;
- classify receipt-boundary checker candidate value using R28-T1 writer
  closure evidence;
- classify memory-safe candidate, memory write, runtime, and standalone app
  lanes as open or held using source-backed conditions;
- produce a companion decision matrix with route token, evidence, novelty,
  prerequisites, and forbidden expansion for each lane;
- leave all implementation lanes held unless source-backed release conditions
  exist inside CVF-governed surfaces.

## Baseline Decision

| Field | Value |
| --- | --- |
| selectedRoute | `RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION` |
| releaseBasis | Current session state at `95734097` routes next allowed work to R28-T2 with R28-T1 writer material commit `23177f27` as predecessor evidence. |
| implementationBoundary | docs-only worker return and decision matrix, under WORKER_MUST_NOT_COMMIT |
| heldLanes | checker code, hook wiring, memory-safe candidate contract, memory write, RAG write, runtime workflow, standalone app, legal/use-case deep dive, provider/live proof, public-sync |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T2 --title "MinerU Receipt Boundary Checker And Memory Route Release Selection" --date 2026-07-04 --base 95734097 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled R28-T2 route-selection purpose, source verification, no-commit handoff control, worker manifest, checker-output read-ahead mandate, and CVF-foundation boundaries |
| checkerReadAheadConfirmation | dispatch-quality, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, structural-completeness, and protected-guard-scope checker surfaces were read or compared through the R28-T1 accepted packet pattern before authoring |
| docOnlyNewFields | `SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY`; `HOLD_MEMORY_ROUTE_RELEASE_PENDING_RECEIPT_CHECKER_AND_QUALITY`; `HOLD_RUNTIME_AND_APP_LANES_FOR_CVF_FOUNDATION_ONLY` |
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
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, and worker-output checker read-ahead. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; claimBoundary; Resolver query; Returned defects: NONE_RETURNED; Public Export Disposition; Delta Execution Claim Boundary Control Block; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers the R28-T2 dispatch packet only; worker-created outputs require their own checker-source read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Current session state releases R28-T2 route-selection with R28-T1 writer closure evidence. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `MSEA-R28-T2` | active session bootstrap read model | ACCEPT |
| R28 selection names receipt boundary checker second and memory-safe candidate after receipt and checker. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_FOUNDATION_IMPLEMENTATION_SEQUENCE_AUDIT_AND_SELECTION_2026-07-04.md` | R28 Selection Matrix | `RECEIPT_BOUNDARY_CHECKER`; `NEXT_AFTER_WRITER`; `NEXT_AFTER_RECEIPT_AND_CHECKER` | MSEA-R28 selection review | ACCEPT |
| R28-T1 writer return records downstream release as held pending receipt checker and memory route. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_WORKER_RETURN_2026-07-04.md` | worker boundary and downstream release rows | `HELD_PENDING_RECEIPT_CHECKER_AND_MEMORY_ROUTE` | MSEA-R28-T1 worker return | ACCEPT |
| R27 implementation sequence treats receipt checker and memory-safe candidate as candidate next packets while holding memory write and runtime workflow. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | implementation sequence matrix | `Receipt checker implementation`; `Memory-safe candidate contract`; `Memory write adapter`; `MinerU runtime workflow` | MSEA-R27 decision ledger | ACCEPT |
| R26 records checker candidate status and criteria but does not authorize checker implementation. | VALUE_SET | `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | Checker Candidate Design | `checkerCandidateStatus`; `CHECKER_CANDIDATE`; `NOT_AUTHORIZED_BY_R26` | MSEA-R26 receipt contract | ACCEPT |
| R24-T4 defines the receipt envelope and private output classes that any checker candidate must protect. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | Receipt Envelope and Private Output Class Matrix | `outputContentRead`; `downstreamRelease`; `PRIVATE_INPUT_ONLY`; `PRIVATE_RUNTIME_COPY`; `PRIVATE_GENERATED_OUTPUT` | MSEA-R24-T4 private-output policy | ACCEPT |
| R28-T1 writer source exposes a held downstream-release constant and rejects output-content-read true. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | constants and builder validation | `DOWNSTREAM_RELEASE_HELD`; `OUTPUT_CONTENT_READ_FORBIDDEN`; `build_mineru_metadata_receipt` | Extraction Foundation metadata receipt writer | ACCEPT |
| R28-T1 writer tests prove stable payload, held downstream release, and false output-content-read behavior. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | writer tests | `render_mineru_metadata_receipt_json`; `output_content_read`; `DOWNSTREAM_RELEASE_HELD` | Extraction Foundation metadata receipt writer tests | ACCEPT |
| Extraction Foundation pipeline owns quality and chunk primitives, so memory-route release must account for quality and source pointers before any memory write. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | dataclasses and builders | `ExtractionQualityReport`; `ExtractionChunk`; `ExtractionStorageBoundary` | Extraction Foundation pipeline | ACCEPT |

## New Doc-Only Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY` | possible R28-T2 selected route token | DOC_ONLY_NEW | may select only docs/design readiness, not checker code |
| `HOLD_MEMORY_ROUTE_RELEASE_PENDING_RECEIPT_CHECKER_AND_QUALITY` | possible R28-T2 memory-route hold token | DOC_ONLY_NEW | use when memory candidate/write release lacks checker and quality proof |
| `HOLD_RUNTIME_AND_APP_LANES_FOR_CVF_FOUNDATION_ONLY` | possible R28-T2 runtime/app boundary token | DOC_ONLY_NEW | use to preserve CVF-plane focus and prevent standalone app drift |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact paths absent before authoring | `Test-Path` returned `False` for the planned GC-018, work order, worker return, and companion decision matrix paths. | PASS |
| Token search for R28-T2 lane before authoring | `rg -n "MSEA-R28-T2\|MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE\|SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY\|HOLD_MEMORY_ROUTE_RELEASE_PENDING_RECEIPT_CHECKER_AND_QUALITY" docs CVF_SESSION EXTENSIONS governance` returned only current session next-move references, not an existing R28-T2 packet. | PASS |
| Collision decision | No existing R28-T2 dispatch or output artifact exists; this baseline may create the first packet. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor route item | Source evidence | R28-T2 handling |
| --- | --- | --- |
| Receipt writer implementation | R28-T1 material commit `23177f27` and worker return | accepted as predecessor evidence |
| Receipt checker implementation | R27 future sequence and R28 selection | classify design readiness only |
| Memory-safe candidate contract | R27 sequence and R28 selection | classify release prerequisites and likely hold until checker and quality proof |
| Memory write adapter | R27 held lane | keep held unless source-backed release evidence exists |
| Runtime workflow and standalone app | R27/R28 held route and operator CVF-foundation instruction | keep held |

## Core Guard Self-Protection Authorization

| Field | Value |
| --- | --- |
| Authorized guard-maintenance scope | none |
| Protected paths | no `governance/compat/*.py`, hook catalog, autorun catalog, AGENTS.md, or session-state path is authorized for worker edits |
| Operator authorization | operator authorized next work-order creation and CVF-foundation audit, not checker implementation |
| Rollback boundary | if route-selection evidence requires checker source changes, return BLOCKED_WITH_REASON instead of editing protected paths |
| Not authorized | no checker implementation, hook wiring, generated-state mutation, protected governance mutation, or session-sync by worker |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | source mirror and MSEA owner surfaces -> R27 plane route -> R28 writer closure -> R28-T2 route-selection |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | this GC-018 baseline and paired work order |
| Disposition | ADAPT: convert accepted receipt and route evidence into a bounded CVF-foundation decision packet |
| Claim boundary | no source import, runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T2 docs-only dispatch baseline |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no new runtime receipt is created or consumed by this baseline. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this baseline. |
| invocationBoundary | local file reads, searches, scaffold generation, and governance dispatch gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | route-selection dispatch baseline only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without fresh source-verified authorization. |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R28-T1 metadata writer | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`; R28-T1 worker return | CONFIRMED_EXISTING | newly available concrete receipt shape | use as predecessor evidence |
| Receipt checker candidate | R26 contract and R28 selection | ENRICH_EXISTING | route-selection can sharpen design readiness | classify, do not implement |
| Memory-safe candidate route | R27 decision ledger and Extraction Foundation quality owners | ENRICH_EXISTING | route-selection can state release prerequisites | classify and hold unless released |
| Runtime, app, use-case, memory-write lanes | R27/R28 held surfaces and operator instruction | REJECT_DIRECT_IMPORT | useful later but outside current CVF-foundation step | keep held |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_WORKER_RETURN_2026-07-04.md`

priorVerificationAnchor: R28-T1 writer source and held downstream-release evidence

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
| baseHeadFor(phase) | dispatchBaseHead=95734097; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatcher owns this GC-018 and paired work order; worker owns only worker return and companion decision matrix; reviewer owns closure repairs and material commit; steward owns session-sync when closure exists |
| traceScope(phase, actor) | each actor records before status, after status, diff evidence, and no-commit or commit ownership evidence |
| commitOwner(phase) | dispatcher may commit dispatch; worker is WORKER_MUST_NOT_COMMIT; reviewer/closer may commit accepted worker outputs; session-sync steward may commit continuity updates only when material closure exists |
| crossBatchIsolation | R28-T2 must not edit R28-T1 source/tests, R27/R26/R24 owner surfaces, runtime outputs, private source documents, generated output content, public-sync clone, protected governance code, or generated session state |
| nextMoveSurfaces | reviewer/closer and session-sync steward update next allowed move only when accepted R28-T2 closure exists |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_WORKER_RETURN_2026-07-04.md` |
| reviewerOwnedClosurePaths | worker return, companion decision matrix, and allowed reviewer repairs inside those artifacts only |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Claim Boundary

This baseline authorizes a docs-only route-selection worker tranche. It does
not authorize checker code, hook wiring, MinerU runtime, private content read,
generated output read, memory/RAG write, adapter work, public-sync,
provider/live proof, standalone app work, legal/use-case deep dive, or
production workflow-chain claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T2 is private provenance dispatch work and does not change the
public-sync repository or public catalog.
