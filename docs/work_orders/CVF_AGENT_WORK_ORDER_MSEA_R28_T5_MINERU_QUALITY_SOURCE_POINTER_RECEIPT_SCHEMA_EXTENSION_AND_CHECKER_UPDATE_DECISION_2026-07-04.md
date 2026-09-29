# CVF Agent Work Order - MSEA-R28-T5 MinerU Quality Source Pointer Receipt Schema Extension And Checker Update Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T5-QUALITY-SOURCE-POINTER-RECEIPT-SCHEMA-EXTENSION

rawMemoryReleased: false

dispatchBaseHead: 1443bf09

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_WORKER_RETURN_2026-07-04.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T5.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. R28-T4 closure at material
commit `0c81b7bc` accepted the checker and released only fresh R28-T5 packet
authoring for quality/source-pointer schema/checker work.

Do-not-misread notes: this packet authorizes only bounded metadata receipt
schema-helper changes, matching writer tests, existing checker/test updates,
conditional registry metadata update, and a worker return. It does not
authorize MinerU runtime execution, private/generated content read, Candidate
Group A import, memory/RAG write, provider/live proof, public-sync, standalone
app work, legal/use-case deep dive, extraction accuracy, document truth, legal
quality, current-law correctness, workflow-chain release claim, worker stage,
worker commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the Source
Verification Block, and checker source for worker-created outputs before
editing any file.

Return contract: create or modify only the allowed worker-owned paths, run
focused tests and required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | operator request to write the next-tranche work order from accepted R28-T4 checker closure evidence |
| Intake role | worker extends metadata-only receipt schema and updates the existing checker/tests |
| Scope classification | bounded source/checker/test implementation; no runtime/provider/public/private-content/memory-release behavior |
| Reviewer role | reviewer/closer validates source evidence, focused tests, worker return, memory hold, and no-commit discipline |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; implementation remains pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require MinerU runtime execution, private/generated content read, memory/RAG write, provider/live proof, public-sync, standalone app work, legal/use-case deep dive, session-sync by worker, AGENTS.md edit, active handoff edit, source/test edits outside owned paths, dependency install, destructive command, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Implement the R28-T5 quality/source-pointer receipt schema tranche. The worker
must extend the existing MinerU metadata receipt writer with bounded
metadata-only quality/source-pointer references, update focused writer tests,
update the existing receipt-boundary checker to require and validate those
references, update focused checker tests, and return uncommitted evidence.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | implement writer/checker/test updates and worker return | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker return, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator asked to write the next-tranche work order after accepting R28-T4 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` and `CVF_SESSION/ACTIVE_SESSION_STATE.json` route next allowed move to R28-T5 packet authoring only | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V36_2026-07-04.md` names the same next allowed move and parked checkpoints | ACCEPT |
| R28-T4 closure | material commit `0c81b7bc` accepted the checker and held memory route | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_2026-07-04.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` only to add bounded metadata-only `qualityReportRef` and `sourcePointer` receipt fields, validation, payload rendering, and receipt-version update if required;
- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` only for focused coverage of those receipt fields and existing privacy/held-route boundaries;
- modify `governance/compat/check_mineru_receipt_boundary.py` only to add required-field and bounded-value validation for `qualityReportRef`, `sourcePointer`, and `QUALITY_OR_SOURCE_POINTER_MISSING`;
- modify `governance/compat/test_check_mineru_receipt_boundary.py` only for focused checker coverage of these fields and no-content/no-runtime boundaries;
- update existing GC-051 registry source entries and regenerate `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only if a gate requires metadata refresh for changed registered source/test paths;
- create the worker return path named above;
- run focused writer/checker tests, worker-return fast gate, and pre-implementation autorun;
- record exact `executionBaseHead`, changed files, command evidence, and no-commit statement.

Forbidden scope:

- no MinerU command, model/cache mutation, ModelScope, VLM, OCR, parser, router, Gradio, Docker, WSL, or runtime smoke;
- no private source document body read and no generated output content read, quotation, copy, import, stage, or commit;
- no committed runtime receipt instance, memory-layer write, RAG write, adapter implementation, S3, Web, MCP, model-router, package lifecycle, action-authority, public-sync, provider/live proof, standalone PDF app, legal/use-case deep dive, extraction-accuracy claim, document-truth claim, legal advice quality claim, current-law correctness claim, production workflow-chain claim, worker stage, worker commit, or push;
- no active session state, active handoff, root startup file, AGENTS.md, public-sync clone, or unrelated source/test edit.

Risk ceiling: R2 bounded source/checker/test update; no runtime/provider/private-data action.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| writer source and writer tests | worker modifies only for metadata-only quality/source-pointer fields | allowed |
| receipt-boundary checker and focused checker tests | worker modifies only for quality/source-pointer validation | allowed |
| existing R28-T1 registry source/test entries and generated aggregate | worker modifies only if GC-051 requires metadata refresh | conditional allowed |
| worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| session state, front door, and active handoff | session-sync steward | forbidden to worker |
| any other path | not worker-owned | forbidden unless a revised work order authorizes it |

## Required First Reads

| Source | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V36_2026-07-04.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| this work order and paired GC-018 | READ |
| all source files in the Source Verification Block | SOURCE_VERIFIED |
| checker source for worker return, writer source/tests, checker source/tests, and conditional registry output | READ_BEFORE_WRITING_OUTPUTS |

## Preflight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Capture execution base | `git rev-parse --short HEAD` | record in worker return |
| Confirm worktree status | `git status --short --untracked-files=all` | record exact pending paths |
| Confirm planned worker return path | `Test-Path` for worker return path | no conflicting existing R28-T5 worker return |
| Read checker/output source | direct file reads of applicable output, trace, delta, corpus, worker-return, writer, checker, and hook/catalog checkers | record exact headings/tokens in worker return before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm clean or declared worktree state | worker return trace |
| 2 | Read worker-output checker source and current writer/checker source before editing | Checker Source Read-Ahead Block |
| 3 | Add metadata-only `qualityReportRef` and `sourcePointer` fields to the writer dataclass, builder, validation, and payload renderer | writer source and focused tests |
| 4 | Keep `downstreamRelease` held and preserve no-content-read validation | writer tests and checker tests |
| 5 | Add checker required-field/value validation and `QUALITY_OR_SOURCE_POINTER_MISSING` failure coverage | checker source and focused tests |
| 6 | Refresh existing registry metadata only if a gate requires it | registry drift check, if applicable |
| 7 | Create worker return with no-commit evidence and run required gates | worker return and command evidence |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T5 --title "MinerU Quality Source Pointer Receipt Schema Extension And Checker Update Decision" --date 2026-07-04 --base 1443bf09 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile, with protected governance path trigger active |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled source verification, proposed field table, implementation scope, worker output manifest, checker-output read-ahead mandate, handoff control, and R28 held-lane boundaries |
| checkerReadAheadConfirmation | dispatch-quality, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, corpus-scan-registry, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `qualityReportRef`; `sourcePointer`; `QUALITY_OR_SOURCE_POINTER_MISSING`; `QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION`; `MEMORY_ROUTE_STILL_HELD_AFTER_QUALITY_SOURCE_POINTER_SCHEMA_EXTENSION` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
live/provider/public/private-content requirement, dependency install,
destructive action, or missing authority that makes completion impossible.

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
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Core Guard Self-Protection Authorization; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; protected paths; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created writer/checker source, tests, registry entries, and worker return require their own source and checker read-ahead before editing. |

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
| Collision decision | No existing R28-T5 dispatch or worker return exists; this work order may create the first dispatch packet. | PASS |

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
| `INTERNAL_AGENT` | writer helper plus local governance checker | internal worker may extend metadata schema and checker under WORKER_MUST_NOT_COMMIT; reviewer must accept before closure | this work order, paired GC-018, source verification, focused tests, worker return | internal-only Python helper/checker; no external adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP or external adapter owner in R28-T5 | external ingress, authentication, approval, receipt, raw-data, mutation, and public boundaries remain out of scope | no source-verified external adapter authority in R28-T5 | adapter deferred; no CLI/MCP surface implemented or claimed | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Corpus scan or extraction intake |
| Chain map route | extraction/source evidence -> CVF-owned references and runtime source verification -> fresh GC-018/work order -> autorun pre-dispatch gates |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired R28-T5 GC-018 and this work order |
| Disposition | ADAPT prior R27/R28 evidence into a bounded quality/source-pointer schema/checker dispatch; no external source becomes authority by itself |
| Claim boundary | routing evidence only; no external repository absorption, private/generated content read, runtime/provider/live proof, public-sync, app, or production claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Guard owner | `governance/compat/check_foundation_storage_layout.py` |
| Trigger reason | this work order modifies durable governance checker source under `governance/compat/` and extraction foundation source under `EXTENSIONS/` |
| Stable location decision | existing writer/checker/test files stay in their current source families; no new stable reference folder is created |
| Index or front-door decision | no new `docs/reference/` family, front door, or stable reference folder is created |
| Archive or rotation decision | N/A with reason: no existing durable governance file is split, moved, archived, or rotated in this dispatch |
| Generated aggregate decision | registry aggregate may change only if GC-051 requires source-entry metadata refresh and only through the existing generator |
| Claim boundary | storage-layout evidence only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

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

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under reviews | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| writer source and tests | derive existing dataclass/builder/payload/test conventions and no-content/no-runtime boundary before editing |
| checker source and tests | derive existing range-aware CLI pattern, required-field validation, diagnostics, and focused unittest style before editing |
| optional registry entries | derive generated-source discipline from GC-051 checker and registry generator before editing any aggregate |

Literal-shape reminders: when listing required section names, write section
names without heading prefixes. Do not write never-created optional artifact
paths as parseable path tokens inside negative evidence rows. If a Findings row
exists, use a real defect-class enum token in the learning disposition.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit worker -> reviewer/closer -> session-sync steward |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=1443bf09; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | worker may touch only allowed writer/checker/test/conditional-registry/worker-return paths |
| traceScope(phase, actor) | worker records executionBaseHead, changed files, command evidence, and no-commit statement; reviewer records closure evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit if accepted |
| crossBatchIsolation | do not mix R28-T5 with memory-route release, runtime, provider/live, public-sync, app/use-case/legal, or session-sync work |
| nextMoveSurfaces | session-sync steward updates front door, active state, and active handoff only when material closure evidence exists |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return unless reviewer needs a separate closure packet |
| reviewerOwnedClosurePaths | worker return plus accepted writer/checker/test/conditional-registry artifacts |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | add bounded metadata-only `qualityReportRef` and `sourcePointer` receipt support |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | add focused writer tests for new fields and preserved hold/no-content boundaries |
| `governance/compat/check_mineru_receipt_boundary.py` | add required-field/value checks and `QUALITY_OR_SOURCE_POINTER_MISSING` |
| `governance/compat/test_check_mineru_receipt_boundary.py` | add focused checker tests for missing/invalid new fields |
| worker return | create no-commit evidence packet |
| existing registry entries and aggregate | update only if a gate requires metadata refresh |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_WORKER_RETURN_2026-07-04.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| focused writer tests | exact command and pass count |
| focused checker tests | exact command and pass count |
| receipt-boundary checker smoke | exact command with base/head and pass result |
| worker-return fast gate | exact command and pass result |
| pre-implementation autorun | exact command and pass result |
| no-commit evidence | `git status --short --untracked-files=all` and HEAD unchanged |
| claim-boundary evidence | explicit no-runtime/no-private-content/no-memory-release statement |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Writer schema | metadata-only quality/source-pointer fields are rendered deterministically without content reads |
| Writer tests | focused tests cover field rendering and preserved no-content/held-route behavior |
| Checker | checker fails missing or invalid quality/source-pointer references with `QUALITY_OR_SOURCE_POINTER_MISSING` |
| Checker tests | focused tests cover positive and negative cases |
| Memory hold | downstream release remains held and memory route is not released |
| Scope | no runtime/provider/live/private-content/public/app/legal/deep-quality claim |
| Worker mode | worker leaves all changes uncommitted |

## Fail Conditions

- source facts conflict with the Source Verification Block;
- implementation requires reading private source documents or generated output content;
- implementation requires running MinerU, provider/live proof, memory/RAG, public-sync, or app work;
- checker cannot validate the new fields without opening referenced files;
- worker edits session state, active handoff, AGENTS.md, public-sync, or unrelated source paths;
- worker stages, commits, or pushes;
- command evidence is missing, stale, or ambiguous.

## Review Gate

Reviewer must inspect the worker return, changed writer/checker/test diffs,
focused tests, worker-return fast gate, pre-implementation autorun, no-commit
statement, and memory-route hold. Reviewer may repair allowed-scope defects but
must return to orchestrator if acceptance requires runtime/private/provider/
public/memory scope expansion.

## Closure Checklist

| Item | Closure disposition |
| --- | --- |
| Source verification still accurate | checked, or BLOCKED with return action |
| Focused tests pass | checked, or BLOCKED with command evidence |
| Worker-return fast gate passes | checked, or BLOCKED with command evidence |
| Pre-implementation autorun passes | checked, or BLOCKED with command evidence |
| No forbidden runtime/private/provider/public/memory action | checked, or BLOCKED with return action |
| Memory-route hold preserved | checked, or BLOCKED with return action |
| Next allowed move stated | checked after review decision |
| Session sync | reviewer/steward only when material closure exists |

## Verification Commands

```powershell
python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py governance/compat/test_check_mineru_receipt_boundary.py -q
python governance/compat/check_mineru_receipt_boundary.py --base 1443bf09 --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 1443bf09 --head HEAD
git status --short --untracked-files=all
```

If the focused test invocation changes during implementation, use the matching
repo-local unittest or pytest command and record the exact command.

## Operator Checkpoint

operator.checkpoint.waiver: Operator already requested the next-tranche work
order using accepted R28-T4 closure evidence; worker implementation remains bounded by this
source-verified work order and returns uncommitted for reviewer closure.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T5 MinerU Quality Source Pointer Receipt Schema Extension And Checker Update Decision, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, scaffold helper, apply_patch, governance gates |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_2026-07-04.md` |
| Allowed scope source | active session state nextAllowedMove and operator request |
| Before status evidence | clean worktree evidence: `git status --short` returned no output before authoring |
| After status evidence | dispatcher pre-dispatch gates to be recorded before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator requested next-tranche work-order authoring after R28-T4 |
| Claim boundary | dispatch authoring only; no worker execution, runtime, memory/RAG, public-sync, provider/live, private/generated content read, or production claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t5-dispatch-2026-07-04` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_2026-07-04.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_2026-07-04.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename performed |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T5 metadata-only schema/checker update work order |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata receipt writer/checker evidence is cited, but this work order creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this work order runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local source verification, metadata-only writer/checker updates, focused tests, governance gates, and worker return only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | local schema/checker implementation and bounded tests only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior or memory write without fresh source-verified authorization. |

## Claim Boundary

This work order authorizes a no-commit worker to extend metadata-only quality
and source-pointer receipt fields in the existing writer, update the existing
receipt-boundary checker and focused tests, and create a worker return. It does
not authorize MinerU runtime execution, private/generated content read, runtime
receipt creation, memory/RAG release, adapter work, provider/live proof,
public-sync, app work, legal/use-case deep dive, extraction accuracy, document
truth, legal quality, current-law correctness, workflow-chain production
readiness, worker commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T5 is private provenance schema/checker dispatch work and does not
change the public-sync repository or public catalog.
