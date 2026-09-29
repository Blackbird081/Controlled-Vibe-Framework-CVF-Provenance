# CVF Agent Work Order - MSEA-R28-T8 MinerU Downstream Use And Memory Route Release Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T8-DOWNSTREAM-USE-AND-MEMORY-ROUTE-RELEASE-DECISION

rawMemoryReleased: false

dispatchBaseHead: 5d396bc8

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_WORKER_RETURN_2026-07-04.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T8.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. R28-T7 material commit
`67b98170` accepted deterministic metadata-only quality-report/source-pointer
helper evidence, and session-sync commit `5d396bc8` routes the next allowed move
to T8 downstream-use and memory-route release decision work-order authoring.

Do-not-misread notes: this packet authorizes only docs-only decision matrix and
worker-return authoring. It does not authorize MinerU runtime execution,
private/generated content read, Candidate Group A import, source/test edit,
checker/hook edit, memory/RAG write, provider/live proof, public-sync,
standalone app work, legal/use-case deep dive, extraction accuracy, document
truth, legal quality, current-law correctness, workflow-chain release claim,
worker stage, worker commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the Source
Verification Block, and checker source for worker-created outputs before
writing any file.

Return contract: create only the named companion matrix and worker return, run
worker-return fast gate and pre-implementation autorun, leave changes
uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | operator requested completion of T7-T10; accepted T7 closure evidence and active session route next move to T8 |
| Intake role | worker authors docs-only downstream-use and memory-route release decision matrix |
| Scope classification | bounded docs-only decision; no runtime/provider/public/private-content/memory-release behavior |
| Reviewer role | reviewer/closer validates matrix, worker return, gates, no-commit discipline, and memory hold |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; docs-only changes remain pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require MinerU runtime execution, private/generated content read, memory/RAG write, provider/live proof, public-sync, standalone app work, legal/use-case deep dive, source/test/checker/hook/session edit, AGENTS.md edit, active handoff edit, dependency install, destructive command, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Create a source-verified decision matrix that evaluates whether R28-T7 evidence
is enough to release a downstream-use and memory-route implementation lane.
The worker must decide among direct memory-route release, memory-safe candidate
contract first, or continued full hold, and must keep memory/RAG writes
unauthorized unless a future packet supplies fresh owner authority.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | create named companion matrix and worker return only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker artifacts, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator asked to complete T7-T10 after R28-T7 closure | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` and `CVF_SESSION/ACTIVE_SESSION_STATE.json` route next allowed move to R28-T8 packet authoring | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V36_2026-07-04.md` names the same next allowed move and parked checkpoints | ACCEPT |
| R28-T7 closure | material commit `67b98170` accepted deterministic metadata-only helper evidence and preserved memory hold | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_2026-07-04.md` | ACCEPT |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T7 material closure | `docs/reviews/CVF_MSEA_R28_T7_MINERU_ACTUAL_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` and state entry at commit `67b98170` | ACCEPT |
| R28-T7 session-sync routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at commit `5d396bc8` | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `5d396bc8` before authoring | ACCEPT |
| Worker execution release | R28-T8 dispatch artifacts and gates must exist before worker begins; this packet supplies that release after commit | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md`;
- create `docs/reviews/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_WORKER_RETURN_2026-07-04.md`;
- evaluate direct memory-route release, memory-safe candidate contract first,
  and continued full hold against R28-T7, R28-T6, R27, and R24-T4 evidence;
- select a bounded next route for T9/T10 without executing that route;
- run worker-return fast gate, pre-implementation autorun, and no-commit
  evidence commands.

Forbidden scope:

- no MinerU command, model/cache mutation, ModelScope, VLM, OCR, parser, router,
  Gradio, Docker, WSL, or runtime smoke;
- no private source document body read and no generated output content read,
  quotation, copy, import, stage, or commit;
- no source/test edit, checker edit, hook wiring, registry aggregate edit,
  runtime receipt instance, memory-layer write, RAG write, adapter
  implementation, S3, Web, MCP, model-router, package lifecycle,
  action-authority, public-sync, provider/live proof, standalone PDF app,
  legal/use-case deep dive, extraction-accuracy claim, document-truth claim,
  legal advice quality claim, current-law correctness claim, production
  workflow-chain claim, worker stage, worker commit, or push;
- no active session state, active handoff, root startup file, AGENTS.md,
  public-sync clone, dependency install, or unrelated documentation edit.

Risk ceiling: R1 docs-only decision; no runtime/provider/private-data/public action.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| companion T8 decision matrix | worker may create listed file only | WORKER_MUST_NOT_COMMIT |
| worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| source/test/checker/hook files | not worker-owned in R28-T8 | forbidden |
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
| checker source for worker return and companion matrix gates | READ_BEFORE_WRITING_OUTPUTS |

## Preflight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Capture execution base | `git rev-parse --short HEAD` | record in worker return |
| Confirm worktree status | `git status --short --untracked-files=all` | record exact pending paths |
| Confirm planned worker paths | `Test-Path` for the T8 companion matrix and worker return | no conflicting existing R28-T8 worker artifact |
| Read checker/output source | direct file reads of applicable review, reference, trace, delta, public-export, worker-return, and dispatch-quality checkers | record exact headings/tokens before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm worktree state | worker return trace |
| 2 | Read worker-output checker source and all Source Verification Block files before editing | Checker Source Read-Ahead Block in worker return |
| 3 | Create companion decision matrix comparing direct memory-route release, memory-safe candidate contract first, and continued full hold | companion matrix |
| 4 | Select exactly one downstream-use and memory-route disposition with T9/T10 recommendation boundaries | companion matrix and worker return |
| 5 | Create worker return summarizing decision, changed files, gates, no-commit status, and next recommended tranche | worker return |
| 6 | Run worker-return fast gate and pre-implementation autorun on the worker changed range | command evidence |
| 7 | Leave changes uncommitted and return for reviewer closure | `git status --short --untracked-files=all` and HEAD unchanged |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T8 --title "MinerU Downstream Use And Memory Route Release Decision" --date 2026-07-04 --base 5d396bc8 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled source verification, docs-only decision scope, worker output manifest, checker-output read-ahead mandate, handoff control, and held-lane boundaries |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION`; `MEMORY_ROUTE_RELEASE_DECISION_MATRIX_READY`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T8_DISPATCH`; `MEMORY_SAFE_CANDIDATE_CONTRACT_RECOMMENDED` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
live/provider/public/private-content requirement, source/test/checker/hook/
session edit requirement, dependency install, destructive action, or missing
authority that makes completion impossible.

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
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define worker decision content. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created return and matrix require their own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session state routes the next allowed move to T8 downstream-use and memory-route release decision authoring. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| R28-T7 closure accepted deterministic metadata-only quality/source-pointer helper evidence. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T7ActualQualityReportSourcePointerProductionImplementationClosure20260704.json` | lines 5 and 17-23 | `CLOSED_PASS_BOUNDED`; `QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTED` | active session state entry | ACCEPT |
| R28-T7 worker return keeps the memory route held pending downstream-use and memory-owner decision. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T7_MINERU_ACTUAL_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` | lines 62-63 | `MEMORY_ROUTE_HELD_PENDING_ALLOWED_DOWNSTREAM_USE_AND_MEMORY_OWNER_DECISION` | MSEA-R28-T7 worker return | ACCEPT |
| Receipt writer keeps downstream release held by default. | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 19 and 81 | `DOWNSTREAM_RELEASE_HELD`; `downstream_release` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer owns metadata-only quality/source-pointer helper symbols. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 87 and 143 | `MineruQualityReportSourcePointer`; `build_mineru_quality_report_source_pointer` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer keeps committed private output content unread. | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 79-80 and 226-229 | `private_output_disposition`; `output_content_read` | MinerU metadata receipt writer | ACCEPT |
| Receipt payload emits downstream, content-read, quality-report, and source-pointer metadata fields. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 260, 262, 266, and 270 | `downstreamRelease`; `outputContentRead`; `qualityReportRef`; `sourcePointer` | MinerU metadata receipt writer payload | ACCEPT |
| Receipt checker requires quality/source-pointer and private-output metadata fields. | RUNTIME_BEHAVIOR | `governance/compat/check_mineru_receipt_boundary.py` | lines 37-48, 215, 235-250, and 307-320 | `REQUIRED_FIELDS`; `privateOutputDisposition`; `outputContentRead`; `qualityReportRef`; `sourcePointer` | MinerU receipt boundary checker | ACCEPT |
| R28-T6 matrix holds direct memory/RAG release and points to future memory-owner authorization. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T6_MINERU_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_DECISION_MATRIX_2026-07-04.md` | lines 71, 88-91, and 97-99 | `MEMORY_WRITE_AUTHORIZED`; `HELD_PENDING_ACTUAL_PRODUCTION_IMPLEMENTATION`; `HELD_PENDING_SOURCE_POINTER_PRODUCTION_CONTRACT` | MSEA-R28-T6 decision matrix | ACCEPT |
| R27 ledger requires receipt, quality, source pointer, downstream-use status, claim boundary, and fresh memory owner work order before memory write. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 74 and 85-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED`; `NOT_AUTHORIZED_BY_R27` | MSEA-R27 decision ledger | ACCEPT |
| R24-T4 private-output policy permits metadata-only receipt evidence and requires generated output content to remain unread. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 53-65 and 212 | `outputContentRead`; `privateOutputDisposition`; `RECEIPT_METADATA_ALLOWED` | MSEA-R24-T4 private-output policy | ACCEPT |

## New Doc-Only Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION` | selected R28-T8 route for docs-only release decision | DOC_ONLY_NEW | use in dispatch and worker return only |
| `MEMORY_ROUTE_RELEASE_DECISION_MATRIX_READY` | expected companion matrix result token | DOC_ONLY_NEW | use only with matrix and gate evidence |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T8_DISPATCH` | hard boundary that dispatch does not authorize memory write | DOC_ONLY_NEW | preserve in matrix and worker return |
| `MEMORY_SAFE_CANDIDATE_CONTRACT_RECOMMENDED` | possible T8-selected next route if direct memory release remains premature | DOC_ONLY_NEW | use only as a recommendation, not implementation authority |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact:
`docs/reviews/CVF_MSEA_R28_T7_MINERU_ACTUAL_QUALITY_REPORT_SOURCE_POINTER_PRODUCTION_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`

recomputeReason: R28-T8 decides downstream-use and memory-route release from
current owner surfaces and must re-check current route/source evidence instead
of relying on prior chat or memory summaries.

encodingDiscipline: ASCII-only authored artifact; no private/generated content
quote; no long literal path lists inside review output beyond allowed Source
Inventory and Source Verification evidence.

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned R28-T8 paths absent before authoring | `Test-Path` returned `False` for planned R28-T8 baseline, work order, and worker return paths. | PASS |
| R27 scan-to-memory route source resolved | `rg --files docs/reference docs/roadmaps docs/reviews | rg "MSEA_R27|MSEA-R27|SCAN_TO_MEMORY|scan.*memory|memory.*route"` returned the R27 roadmap, decision ledger, and completion review; no separate R27 scan-to-memory route matrix file exists. | PASS |
| Current receipt/source helper check | `rg -n "build_mineru_quality_report_source_pointer|MineruQualityReportSourcePointer|qualityReportRef|sourcePointer|DOWNSTREAM_RELEASE_HELD" ...` confirmed current helper and receipt fields. | PASS |
| Freshness disposition | Current source has metadata helper evidence, but no memory write authority or memory-safe candidate contract; R28-T8 may dispatch docs-only release decision. | PASS |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Exact search roots | `docs`, `CVF_SESSION`, `governance`, and `EXTENSIONS` | PASS |
| Exact search command or query | `Test-Path` checks for planned T8 baseline, work order, and worker return paths returned `False` before authoring. | PASS |
| Same-token collision result | No dedicated R28-T8 baseline, work order, worker return, or companion decision matrix existed before authoring. | PASS |
| Absent-versus-collision disposition | Existing T8 mentions were future-routing text only; this packet creates the first R28-T8 dispatch artifacts. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor requirement | Source evidence | R28-T8 handling |
| --- | --- | --- |
| R28-T7 accepted quality/source-pointer helper evidence | material commit `67b98170`; T7 worker return and state entry | authorize docs-only downstream-use and memory-route decision |
| R27 requires receipt, quality, source pointer, downstream-use status, and claim boundary before memory-safe candidate | R27 ledger rows above | worker must compare release options against those prerequisites |
| R24-T4 requires no private/generated output content read | R24-T4 policy row above | worker must reject any option requiring private/generated content read |
| R28-T6 held memory/RAG route behind future memory-owner authorization | R28-T6 matrix rows above | worker must not authorize memory/RAG write directly |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md` | create companion decision matrix with source inventory, option matrix, selected disposition, next-route recommendation, and claim boundary |
| `docs/reviews/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_WORKER_RETURN_2026-07-04.md` | create worker return with evidence, changed files, command results, no-commit statement, and reviewer action needed |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_WORKER_RETURN_2026-07-04.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet, delegated worker creates docs-only matrix/return, reviewer closes, session-sync steward updates state |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=5d396bc8; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch may add only the paired R28-T8 GC-018 baseline and work order; worker may add only the matrix and worker return |
| traceScope(phase, actor) | dispatcher trace in this baseline/work order; worker trace in worker return; reviewer trace in closure commit and session-sync |
| commitOwner(phase) | dispatcher may commit dispatch after gates; worker is WORKER_MUST_NOT_COMMIT; reviewer owns material closure; session-sync steward owns continuity sync |
| crossBatchIsolation | no T9/T10 execution, memory write, source/test/checker edit, runtime, public-sync, or provider/live proof inside T8 |
| nextMoveSurfaces | reviewer/session-sync steward updates front door, generated state, and active handoff only when accepted T8 material closure evidence exists |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return unless reviewer needs a separate closure packet |
| reviewerOwnedClosurePaths | reviewer may repair/accept the worker return and companion matrix only if needed; session-sync steward owns continuity paths when material closure is accepted |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under `docs/reviews/` | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| companion reference under `docs/reference/` | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

Literal-shape reminders: do not list required headings as backticked heading
strings before the real section; write source-not-found disposition spelling
instead of the exact blocked enum in literalTokensReviewed; avoid stale
dependency-placeholder wording unless a dependency-release row cites the
accepted artifact path and commit.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Corpus scan or extraction intake |
| Chain map route | extraction/source evidence -> CVF-owned references and runtime source verification -> fresh GC-018/work order -> autorun pre-dispatch gates |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired R28-T8 GC-018 and work order |
| Disposition | ADAPT accepted R28-T7 implementation evidence into a bounded release-decision dispatch; no external source becomes authority by itself |
| Claim boundary | routing evidence only; no external repository absorption, private/generated content read, MinerU runtime, provider/live proof, public-sync, app, memory write, or production claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Guard owner | `governance/compat/check_foundation_storage_layout.py` |
| Trigger reason | this work order authorizes one companion reference under `docs/reference/` and one worker return under `docs/reviews/` |
| Stable location decision | companion decision matrix belongs in `docs/reference/` because it is successor decision evidence for T9/T10 routing |
| Index or front-door decision | N/A with reason: no new stable reference front door is introduced |
| Archive or rotation decision | N/A with reason: no existing durable governance file is split, moved, archived, or rotated in this dispatch |
| Generated aggregate decision | no generated aggregate edit is authorized |
| Claim boundary | storage-layout evidence only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| companion matrix created | matrix exists at the authorized path and selects exactly one memory-route disposition |
| direct memory write boundary | matrix and worker return state memory/RAG write remains unauthorized in T8 |
| option comparison | direct release, memory-safe candidate contract, and full hold are compared against source-verified prerequisites |
| no forbidden reads/actions | no MinerU runtime, private/generated content read, Candidate Group A import, provider/live proof, public-sync, source/test/checker edit, or memory write |
| gates | worker-return fast gate and pre-implementation autorun pass on the worker changed range |
| no-commit discipline | worker leaves changes uncommitted for reviewer closure |

## Evidence Requirements

| Evidence item | Required evidence |
| --- | --- |
| companion matrix | matrix includes source inventory, option comparison, selected disposition, next-route recommendation, and claim boundary |
| selected route | exactly one selected downstream-use and memory-route disposition is stated |
| no memory write | worker return and matrix explicitly state memory/RAG write remains unauthorized by T8 |
| command evidence | worker-return fast gate and pre-implementation autorun results are recorded |
| no-commit evidence | `git status --short --untracked-files=all` and HEAD evidence are recorded in worker return |

## Review Gate

Reviewer must reject or repair the worker return if it claims memory/RAG write
authority, source/test implementation, private/generated content access, runtime
proof, provider/live behavior, public-sync, legal/use-case quality, extraction
accuracy, document truth, current-law correctness, workflow-chain production
readiness, worker commit, or push.

## Closure Checklist

- [x] Dispatch is source-verified and dependency-release evidence cites T7 closure.
- [x] Worker output paths are bounded to one companion matrix and one worker return.
- [x] Agent Handoff Contract Control Block and Reviewer Closure Conversion are present.
- [x] ADIF Defect Registry Disclosure is present.
- [x] Source Verification Block uses current CVF-governed source surfaces.
- [x] Public Export Disposition is private-only.
- [x] Memory/RAG write remains unauthorized by this dispatch.

## Verification Commands

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 5d396bc8 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 5d396bc8 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 5d396bc8 --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
```

## Operator Checkpoint

No further operator checkpoint is required before dispatch because the operator
requested completion of T7-T10 and T7 closure plus active session state release
T8 work-order authoring. Worker must return `BLOCKED_WITH_REASON` if any
decision option requires a forbidden runtime, private/generated content, memory,
public, provider/live, source/test/checker, or production-readiness action.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T8 MinerU Downstream Use And Memory Route Release Decision dispatch, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell (`rg`, `Test-Path`, `python governance/compat/*`), apply_patch |
| Target paths | paired R28-T8 GC-018 baseline and work order |
| Allowed scope source | active session next allowed move backed by R28-T7 material commit `67b98170` and session-sync commit `5d396bc8` |
| Before status evidence | HEAD `5d396bc8`; worktree clean before authoring |
| After status evidence | two added dispatch artifacts before dispatch commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatcher dispatch authoring only |
| Claim boundary | docs-only decision dispatch; no runtime/private-output/memory/public/provider claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t8-dispatch-2026-07-04` |
| Expected manifest | paired R28-T8 baseline and work order |
| Actual changed set | paired R28-T8 baseline and work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T8 dispatch for downstream-use and memory-route release decision |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata receipt source and checker evidence are cited, but this work order creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this work order runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local file reads, source verification, scaffold generation, and governance dispatch gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | dispatch authoring for docs-only downstream-use and memory-route release decision |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior or memory write without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T8 dispatch is private provenance work only. No public-sync export,
public repository commit, or public catalog claim is included.

## Claim Boundary

This work order authorizes only a docs-only no-commit R28-T8 downstream-use and
memory-route release decision worker. It does not authorize source/test edits,
checker/hook edits, MinerU runtime execution, private/generated content reads,
Candidate Group A import, memory/RAG write, provider/live proof, public-sync,
standalone app work, legal/use-case deep dive, extraction accuracy, document
truth, legal quality, current-law correctness, workflow-chain production
readiness, worker stage, worker commit, or push.
