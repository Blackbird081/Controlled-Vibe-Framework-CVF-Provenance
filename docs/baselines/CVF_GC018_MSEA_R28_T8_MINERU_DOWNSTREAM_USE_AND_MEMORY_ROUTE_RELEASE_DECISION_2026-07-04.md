# CVF GC-018 Baseline - MSEA-R28-T8 MinerU Downstream Use And Memory Route Release Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T8-DOWNSTREAM-USE-AND-MEMORY-ROUTE-RELEASE-DECISION

rawMemoryReleased: false

dispatchBaseHead: 5d396bc8

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: worker role, not a specific provider name

## Purpose

Authorize one bounded no-commit docs-only worker tranche to decide whether the
accepted R28-T7 quality-report/source-pointer helper is sufficient to release a
downstream-use and memory-route implementation lane, or whether the memory route
must remain held behind a narrower memory-safe candidate contract.

This baseline does not authorize MinerU runtime execution, private or generated
content reads, Candidate Group A import, memory/RAG writes, provider/live proof,
public-sync, source/test/checker/hook edits, standalone app work, legal/use-case
deep dive, extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain production readiness, worker stage, worker commit,
or push.

## Scope / Target / Owner Boundary

Allowed worker output paths:

- `docs/reference/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md`
- `docs/reviews/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_WORKER_RETURN_2026-07-04.md`

Allowed worker actions:

- read the required startup/state/handoff surfaces, this baseline, paired work
  order, and all Source Verification Block files;
- create a docs-only companion decision matrix comparing direct memory-route
  release, memory-safe candidate contract, and full hold options;
- create a worker return with the selected downstream-use and memory-route
  disposition;
- run worker-return fast gate and pre-implementation autorun;
- leave all changes uncommitted for reviewer closure.

Forbidden paths and actions: no edits to active session state, active handoff,
root startup files, AGENTS.md, source code, tests, checker/hook source, registry
aggregates, public-sync clone, private source documents, generated MinerU output
content, runtime receipt instances, memory/RAG owner, adapter code, Web/UI, MCP,
CLI, provider/live proof, dependency install, worker stage, worker commit, or
push.

## Baseline Decision

| Field | Value |
| --- | --- |
| selectedRoute | `DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION` |
| releaseBasis | R28-T7 material commit `67b98170` accepted deterministic metadata-only quality-report/source-pointer helper evidence; session-sync commit `5d396bc8` routes the next allowed move to T8 work-order authoring. |
| workerBoundary | docs-only decision matrix plus worker return |
| expectedDecisionPressure | decide whether to release a downstream memory implementation lane or keep memory held behind a memory-safe candidate contract |
| memoryWriteDisposition | `MEMORY_WRITE_NOT_AUTHORIZED_BY_T8_DISPATCH` |
| runtimeDisposition | no MinerU runtime execution, no private/generated content read, no extraction accuracy or document-truth claim |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T8 --title "MinerU Downstream Use And Memory Route Release Decision" --date 2026-07-04 --base 5d396bc8 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled R28-T8 docs-only decision scope, dependency release evidence, source verification, worker manifest, handoff controls, and held-lane boundaries |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION`; `MEMORY_ROUTE_RELEASE_DECISION_MATRIX_READY`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T8_DISPATCH`; `MEMORY_SAFE_CANDIDATE_CONTRACT_RECOMMENDED` |
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
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; Resolver query; Returned defects: NONE_RETURNED; Public Export Disposition; Delta Execution Claim Boundary Control Block; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define worker decision content. |
| claimBoundary | This read-ahead covers the R28-T8 dispatch packet only; worker-created return and matrix require their own source and checker read-ahead before writing. |

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
| R28-T7 accepted quality/source-pointer helper evidence | material commit `67b98170`; T7 worker return and state entry | worker must decide whether this evidence satisfies downstream-use release prerequisites |
| R27 requires receipt, quality, source pointer, downstream-use status, and claim boundary before memory-safe candidate | R27 ledger rows above | worker must compare release options against those prerequisites |
| R24-T4 keeps generated output content private | R24-T4 policy row above | worker must reject any option requiring private/generated content read |
| R28-T6 held memory/RAG route behind future memory-owner authorization | R28-T6 matrix rows above | worker must not authorize memory/RAG write directly |

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
| nextMoveSurfaces | reviewer/session-sync steward updates front door, generated state, and active handoff only after T8 closure |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_WORKER_RETURN_2026-07-04.md` |
| reviewerOwnedClosurePaths | reviewer may repair/accept the worker return and companion matrix only if needed; session-sync steward owns continuity paths after material closure |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_WORKER_RETURN_2026-07-04.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Guard owner | `governance/compat/check_foundation_storage_layout.py` |
| Trigger reason | this baseline authorizes one companion reference under `docs/reference/` and one worker return under `docs/reviews/` |
| Stable location decision | companion decision matrix belongs in `docs/reference/` because it is successor decision evidence for T9/T10 routing |
| Index or front-door decision | N/A with reason: no new stable reference front door is introduced |
| Archive or rotation decision | N/A with reason: no existing durable governance file is split, moved, archived, or rotated in this dispatch |
| Generated aggregate decision | no generated aggregate edit is authorized |
| Claim boundary | storage-layout evidence only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

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

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T8 dispatch baseline for downstream-use and memory-route release decision |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata receipt source and checker evidence are cited, but this baseline creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this baseline runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local file reads, source verification, scaffold generation, and governance dispatch gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | dispatch authoring for docs-only downstream-use and memory-route release decision |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior or memory write without fresh source-verified authorization. |

## Evidence / Verification

| Evidence item | Required result | Current dispatch evidence |
| --- | --- | --- |
| Source verification | ACCEPT rows cite CVF-governed surfaces or current runtime source | Source Verification Block in this baseline and paired work order |
| Prior decision release | R28-T7 accepted deterministic metadata helper while preserving memory hold | T7 worker return, state entry, material commit `67b98170`, and session-sync commit `5d396bc8` |
| Dispatch gates | pre-dispatch autorun must pass before worker execution begins | pending gate evidence in dispatcher final report |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T8 dispatch is private provenance work only. No public-sync export,
public repository commit, or public catalog claim is included.

## Claim Boundary

This baseline authorizes only a docs-only no-commit R28-T8 downstream-use and
memory-route release decision worker. It does not authorize source/test edits,
checker/hook edits, MinerU runtime execution, private/generated content reads,
Candidate Group A import, memory/RAG write, provider/live proof, public-sync,
standalone app work, legal/use-case deep dive, extraction accuracy, document
truth, legal quality, current-law correctness, workflow-chain production
readiness, worker stage, worker commit, or push.
