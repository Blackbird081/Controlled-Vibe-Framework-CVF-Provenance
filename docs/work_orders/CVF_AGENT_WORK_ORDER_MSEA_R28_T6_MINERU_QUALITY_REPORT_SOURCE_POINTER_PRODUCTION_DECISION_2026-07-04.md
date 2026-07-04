# CVF Agent Work Order - MSEA-R28-T6 MinerU Quality Report Source Pointer Production Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T6-QUALITY-REPORT-SOURCE-POINTER-PRODUCTION-DECISION

rawMemoryReleased: false

dispatchBaseHead: facb2714

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_WORKER_RETURN_2026-07-04.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T6.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. R28-T5 closure at material
commit `4a824e6d` accepted receipt-side quality/source-pointer fields and
checker validation. Session-sync commit `facb2714` routes the next allowed move
to fresh R28-T6 packet authoring for actual quality-report/source-pointer
production decision while preserving the memory-route hold.

Do-not-misread notes: this packet authorizes only docs-only source-verified
decision work that creates a worker return and companion matrix. It does not
authorize source/test edits, checker edits, MinerU runtime execution,
private/generated content read, Candidate Group A import, memory/RAG write,
provider/live proof, public-sync, standalone app work, legal/use-case deep dive,
extraction accuracy, document truth, legal quality, current-law correctness, no
workflow-chain release claim, worker stage, worker commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the Source
Verification Block, and checker source for worker-created outputs before
writing any file.

Return contract: create only the worker return and companion matrix paths,
run worker-return fast gate and pre-implementation autorun, leave changes
uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Companion matrix path: `docs/reference/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_MATRIX_2026-07-04.md`

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | operator request to write the next-tranche work order from accepted R28-T5 closure evidence |
| Intake role | worker produces docs-only production decision for actual quality report and source pointer |
| Scope classification | bounded decision artifact work; no runtime/provider/public/private-content/source-edit/memory-release behavior |
| Reviewer role | reviewer/closer validates source evidence, worker return, companion matrix, no-commit discipline, and memory hold |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; decision artifacts remain pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require MinerU runtime execution, private/generated content read, memory/RAG write, provider/live proof, public-sync, standalone app work, legal/use-case deep dive, source/test edits, checker edits, session-sync by worker, AGENTS.md edit, active handoff edit, dependency install, destructive command, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Produce the R28-T6 source-backed production decision for how CVF should later
produce an actual MinerU quality report and source pointer for a committed
metadata receipt. The worker must create a decision matrix that distinguishes
receipt-side references from actual referenced-quality/source-pointer evidence,
preserves R24-T4 private-output boundaries, and keeps the memory route held
unless a future memory-owner work order explicitly releases it.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | create worker return and companion decision matrix only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker artifacts, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator asked to create the next work order after R28-T5 worker execution completed | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` and `CVF_SESSION/ACTIVE_SESSION_STATE.json` route next allowed move to R28-T6 packet authoring only | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V36_2026-07-04.md` names the same next allowed move and parked checkpoints | ACCEPT |
| R28-T5 closure | material commit `4a824e6d` accepted receipt-side quality/source-pointer fields and checker validation while holding memory route | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_2026-07-04.md` | ACCEPT |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T5 material closure | `docs/reviews/CVF_MSEA_R28_T5_MINERU_QUALITY_SOURCE_POINTER_RECEIPT_SCHEMA_EXTENSION_AND_CHECKER_UPDATE_DECISION_WORKER_RETURN_2026-07-04.md` at commit `4a824e6d` | ACCEPT |
| R28-T5 session-sync routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at commit `facb2714` | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `facb2714` before authoring | ACCEPT |
| Worker execution release | R28-T6 dispatch artifacts and gates must exist before worker begins; this packet supplies that release after commit | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reviews/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_WORKER_RETURN_2026-07-04.md`;
- create `docs/reference/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_MATRIX_2026-07-04.md`;
- decide whether the next tranche should implement actual quality-report/source-pointer production, hold it, or split it into smaller source-verified tranches;
- map R28-T5 receipt fields to Extraction Foundation quality/storage owner surfaces without editing those sources;
- state exact memory-route hold and future release prerequisites;
- run worker-return fast gate, pre-implementation autorun, and no-commit evidence commands.

Forbidden scope:

- no MinerU command, model/cache mutation, ModelScope, VLM, OCR, parser, router, Gradio, Docker, WSL, or runtime smoke;
- no private source document body read and no generated output content read, quotation, copy, import, stage, or commit;
- no source/test/checker edit, committed runtime receipt instance, memory-layer write, RAG write, adapter implementation, S3, Web, MCP, model-router, package lifecycle, action-authority, public-sync, provider/live proof, standalone PDF app, legal/use-case deep dive, extraction-accuracy claim, document-truth claim, legal advice quality claim, current-law correctness claim, production workflow-chain claim, worker stage, worker commit, or push;
- no active session state, active handoff, root startup file, AGENTS.md, public-sync clone, or unrelated documentation edit.

Risk ceiling: R1 docs-only decision dispatch; no runtime/provider/private-data/source-edit action.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| companion decision matrix | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| writer/checker/source/test/registry files | not worker-owned in R28-T6 | forbidden |
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
| checker source for worker return and companion matrix | READ_BEFORE_WRITING_OUTPUTS |

## Preflight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Capture execution base | `git rev-parse --short HEAD` | record in worker return |
| Confirm worktree status | `git status --short --untracked-files=all` | record exact pending paths |
| Confirm planned worker paths | `Test-Path` for worker return and companion matrix paths | no conflicting existing R28-T6 worker artifacts |
| Read checker/output source | direct file reads of applicable review, reference, trace, delta, public-export, worker-return, and dispatch-quality checkers | record exact headings/tokens before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm worktree state | worker return trace |
| 2 | Read worker-output checker source and all Source Verification Block files before writing | Checker Source Read-Ahead Block in worker return and matrix |
| 3 | Create companion matrix mapping actual quality-report/source-pointer production prerequisites, owner surfaces, and held lanes | companion matrix |
| 4 | Create worker return summarizing decision, evidence, no-commit status, and next recommended tranche | worker return |
| 5 | Run worker-return fast gate and pre-implementation autorun on the worker changed range | command evidence |
| 6 | Leave changes uncommitted and return for reviewer closure | `git status --short --untracked-files=all` and HEAD unchanged |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T6 --title "MinerU Quality Report Source Pointer Production Decision" --date 2026-07-04 --base facb2714 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled source verification, decision-only scope, worker output manifest, checker-output read-ahead mandate, handoff control, and held-lane boundaries |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_ONLY`; `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_MATRIX_READY`; `MEMORY_ROUTE_STILL_HELD_PENDING_ACTUAL_PRODUCTION_AND_MEMORY_OWNER_DECISION` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
live/provider/public/private-content requirement, source/test edit requirement,
dependency install, destructive action, or missing authority that makes
completion impossible.

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
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created return and matrix require their own source and checker read-ahead before writing. |

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
| `INTERNAL_AGENT` | worker return and companion decision matrix | internal worker may decide future production contract under WORKER_MUST_NOT_COMMIT; reviewer must accept before closure | this work order, paired GC-018, source verification, worker return, matrix | docs-only decision; no runtime adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP or external adapter owner in R28-T6 | external ingress, authentication, approval, receipt, raw-data, mutation, and public boundaries remain out of scope | no source-verified external adapter authority in R28-T6 | adapter deferred; no CLI/MCP surface implemented or claimed | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Corpus scan or extraction intake |
| Chain map route | extraction/source evidence -> CVF-owned references and runtime source verification -> fresh GC-018/work order -> autorun pre-dispatch gates |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired R28-T6 GC-018 and this work order |
| Disposition | ADAPT prior R27/R28 and Extraction Foundation evidence into a bounded production-decision dispatch; no external source becomes authority by itself |
| Claim boundary | routing evidence only; no external repository absorption, private/generated content read, runtime/provider/live proof, public-sync, app, or production claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Guard owner | `governance/compat/check_foundation_storage_layout.py` |
| Trigger reason | this work order authorizes a new durable reference matrix under `docs/reference/` |
| Stable location decision | one companion matrix is allowed under the existing flat `docs/reference/` governed artifact family for MSEA execution evidence |
| Index or front-door decision | N/A with reason: this is a dated execution matrix, not a new stable reference family |
| Archive or rotation decision | N/A with reason: no existing durable governance file is split, moved, archived, or rotated in this dispatch |
| Generated aggregate decision | no generated aggregate edit is authorized |
| Claim boundary | storage-layout evidence only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under reviews | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, public-export terms, and no-commit evidence shape before writing |
| companion matrix under reference | derive exact reference/matrix headings, source verification columns, GC-051 path-literal boundaries, trace needs, and no-content claim language before writing |

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
| baseHeadFor(phase) | dispatchBaseHead=facb2714; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | worker may touch only the worker return and companion matrix paths |
| traceScope(phase, actor) | worker records executionBaseHead, changed files, command evidence, and no-commit statement; reviewer records closure evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit if accepted |
| crossBatchIsolation | do not mix R28-T6 with implementation, memory-route release, runtime, provider/live, public-sync, app/use-case/legal, or session-sync work |
| nextMoveSurfaces | session-sync steward updates front door, active state, and active handoff only when material closure evidence exists |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return unless reviewer needs a separate closure packet |
| reviewerOwnedClosurePaths | worker return plus companion decision matrix |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_WORKER_RETURN_2026-07-04.md` | create no-commit evidence packet with selected disposition and next recommendation |
| `docs/reference/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_MATRIX_2026-07-04.md` | create companion decision matrix with source-backed prerequisites, held lanes, fail conditions, and future implementation split if recommended |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_WORKER_RETURN_2026-07-04.md`

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
| companion matrix | exact path, selected disposition, source verification block, and held-lane matrix |
| worker return | exact path, executionBaseHead, changed files, no-commit evidence, and selected disposition |
| worker-return fast gate | exact command and pass result |
| pre-implementation autorun | exact command and pass result |
| no-commit evidence | `git status --short --untracked-files=all` and HEAD unchanged |
| claim-boundary evidence | explicit no-runtime/no-private-content/no-source-edit/no-memory-release statement |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Decision matrix | maps actual quality-report/source-pointer production prerequisites to source-backed owner surfaces |
| Source boundaries | cites R28-T5 source, R28-T5 return, R28-T3 matrix, R27 ledger, R24-T4 policy, and Extraction Foundation owner surfaces |
| Privacy boundary | no private or generated output content is read, quoted, copied, imported, staged, or committed |
| Memory hold | downstream memory route remains held pending actual production evidence and memory-owner decision |
| Scope | no source/test/checker edit and no runtime/provider/live/public/app/legal/deep-quality claim |
| Worker mode | worker leaves all changes uncommitted |

## Fail Conditions

- source facts conflict with the Source Verification Block;
- decision requires reading private source documents or generated output content;
- decision requires running MinerU, provider/live proof, memory/RAG, public-sync, app work, or source/test edits;
- matrix claims actual quality report or source-pointer production without committed evidence;
- worker edits session state, active handoff, AGENTS.md, public-sync, source, tests, checker, registry, or unrelated docs;
- worker stages, commits, or pushes;
- command evidence is missing, stale, or ambiguous.

## Review Gate

Reviewer must inspect the worker return, companion matrix, source verification,
worker-return fast gate, pre-implementation autorun, no-commit statement, and
memory-route hold. Reviewer may repair allowed-scope documentation defects but
must return to orchestrator if acceptance requires runtime/private/provider/
public/memory/source-edit scope expansion.

## Closure Checklist

| Item | Closure disposition |
| --- | --- |
| Source verification still accurate | checked, or BLOCKED with return action |
| Companion matrix complete | checked, or BLOCKED with return action |
| Worker-return fast gate passes | checked, or BLOCKED with command evidence |
| Pre-implementation autorun passes | checked, or BLOCKED with command evidence |
| No forbidden runtime/private/provider/public/memory/source-edit action | checked, or BLOCKED with return action |
| Memory-route hold preserved | checked, or BLOCKED with return action |
| Next allowed move stated | checked after review decision |
| Session sync | reviewer/steward only when material closure exists |

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base facb2714 --head HEAD
git status --short --untracked-files=all
```

If the changed range differs from `facb2714..HEAD` during worker execution,
capture the worker's executionBaseHead and run gates over the real worker
changed range.

## Operator Checkpoint

operator.checkpoint.waiver: Operator already requested the next-tranche work
order using accepted R28-T5 closure evidence; worker execution remains bounded
by this source-verified work order and returns uncommitted for reviewer closure.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T6 MinerU Quality Report Source Pointer Production Decision, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, scaffold helper, apply_patch, governance gates |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_2026-07-04.md` |
| Allowed scope source | active session state nextAllowedMove and operator request |
| Before status evidence | clean worktree evidence: `git status --short` returned no output before authoring |
| After status evidence | dispatcher pre-dispatch gates to be recorded before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator requested next-tranche work-order authoring after R28-T5 |
| Claim boundary | dispatch authoring only; no worker execution, runtime, memory/RAG, public-sync, provider/live, private/generated content read, source/test edit, or production claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t6-dispatch-2026-07-04` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_2026-07-04.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_2026-07-04.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename performed |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T6 quality-report/source-pointer production decision work order |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata receipt source and checker evidence are cited, but this work order creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this work order runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local source verification, docs-only decision artifacts, governance gates, and worker return only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | docs-only production decision and bounded worker evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior, source/test edit, or memory write without fresh source-verified authorization. |

## Claim Boundary

This work order authorizes a no-commit worker to create a docs-only
quality-report/source-pointer production decision matrix and worker return. It
does not authorize MinerU runtime execution, private/generated content read,
runtime receipt creation, source/test/checker edits, memory/RAG release,
adapter work, provider/live proof, public-sync, app work, legal/use-case deep
dive, extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain release claim, worker commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T6 is private provenance decision-dispatch work and does not change
the public-sync repository or public catalog.
