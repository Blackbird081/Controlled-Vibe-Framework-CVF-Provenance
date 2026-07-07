# CVF GC-018 Baseline - MSEA-R28-T9 MinerU Memory Safe Candidate Contract

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T9-MINERU-MEMORY-SAFE-CANDIDATE-CONTRACT

rawMemoryReleased: false

dispatchBaseHead: c4fed412

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: worker role, not a specific provider name

## Purpose

Authorize one bounded no-commit source/test worker tranche to add a
metadata-only memory-safe candidate contract helper to the existing MinerU
metadata receipt writer. The helper may package source-verified receipt
metadata, quality/source-pointer refs, allowed downstream-use status, and claim
boundary into a deterministic candidate contract for later route selection.

This baseline does not authorize MinerU runtime execution, private or generated
content reads, Candidate Group A import, memory/RAG writes, provider/live proof,
public-sync, checker/hook edits, standalone app work, legal/use-case deep dive,
extraction accuracy, document truth, legal quality, current-law correctness,
workflow-chain production readiness, worker stage, worker commit, or push.

## Scope / Target / Owner Boundary

Allowed worker output paths:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`
- `docs/reviews/CVF_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_WORKER_RETURN_2026-07-04.md`

Allowed worker actions:

- read startup/state/handoff, this baseline, paired work order, source
  verification files, and worker-output checker source before editing;
- add a small metadata-only candidate contract dataclass or helper in the
  existing receipt writer source;
- use only caller-supplied metadata and existing receipt payload fields;
- keep `outputContentRead` false, `DOWNSTREAM_RELEASE_HELD`, private-output
  disposition, and no raw-content markers intact;
- add focused tests proving determinism, receipt compatibility, fail-closed
  unsafe-marker rejection, and no memory/RAG write authorization;
- create the worker return and leave all changes uncommitted.

Forbidden paths and actions: no edits to active session state, active handoff,
root startup files, AGENTS.md, checker/hook source, registry aggregates,
public-sync clone, private source documents, generated MinerU output content,
runtime receipt instances, memory/RAG owner, adapter code, Web/UI, MCP, CLI,
provider/live proof, dependency install, worker stage, worker commit, or push.

## Baseline Decision

| Field | Value |
| --- | --- |
| selectedRoute | `MEMORY_SAFE_CANDIDATE_CONTRACT` |
| releaseBasis | R28-T8 material commit `cba22bc8` accepted a docs-only decision matrix recommending `MEMORY_SAFE_CANDIDATE_CONTRACT_RECOMMENDED`; session-sync commit `c4fed412` routes the next allowed move to T9 packet authoring. |
| workerBoundary | bounded source/test helper plus worker return |
| expectedDecisionPressure | define a deterministic metadata-only contract that can support T10 route selection without writing memory |
| memoryWriteDisposition | `MEMORY_WRITE_NOT_AUTHORIZED_BY_T9_DISPATCH` |
| runtimeDisposition | no MinerU runtime execution, no private/generated content read, no extraction accuracy or document-truth claim |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T9 --title "MinerU Memory Safe Candidate Contract" --date 2026-07-04 --base c4fed412 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled R28-T9 metadata-only source/test helper scope, dependency release evidence, source verification, worker manifest, handoff controls, and no-memory-write boundaries |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `MEMORY_SAFE_CANDIDATE_CONTRACT`; `MEMORY_SAFE_CANDIDATE_CONTRACT_IMPLEMENTED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T9_DISPATCH`; `T10_ROUTE_SELECTION_RECOMMENDED` |
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
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define worker implementation content. |
| claimBoundary | This read-ahead covers the R28-T9 dispatch packet only; worker-created return and source/test edits require their own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session state routes the next allowed move to T9 metadata-only memory-safe candidate contract work-order authoring. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| R28-T8 closure accepted the memory-safe candidate contract recommendation and preserved memory write hold. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T8DownstreamUseAndMemoryRouteReleaseDecisionClosure20260704.json` | lines 5 and 15-24 | `MEMORY_SAFE_CANDIDATE_CONTRACT_RECOMMENDED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T8` | active session state entry | ACCEPT |
| R28-T8 companion matrix selected memory-safe candidate contract first and rejected direct memory/RAG write. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md` | lines 50-63 | `MEMORY_SAFE_CANDIDATE_CONTRACT_RECOMMENDED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T8` | MSEA-R28-T8 decision matrix | ACCEPT |
| Current receipt writer keeps downstream release held by default. | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 19 and 81 | `DOWNSTREAM_RELEASE_HELD`; `downstream_release` | MinerU metadata receipt writer | ACCEPT |
| Current receipt writer owns receipt and quality/source-pointer metadata helper symbols. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 69, 87, 143, and 201 | `MineruMetadataReceipt`; `MineruQualityReportSourcePointer`; `build_mineru_quality_report_source_pointer`; `build_mineru_metadata_receipt` | MinerU metadata receipt writer | ACCEPT |
| Current receipt writer validates bounded metadata identifiers and rejects raw-content markers. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 53-57, 98-103, and 125-140 | `_SAFE_ID_RE`; `_UNSAFE_TEXT_MARKERS`; `_validate_quality_source_pointer` | MinerU metadata receipt writer validation | ACCEPT |
| Receipt payload emits downstream, content-read, quality-report, source-pointer, and claim-boundary metadata fields. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 258-270 | `claimBoundary`; `downstreamRelease`; `outputContentRead`; `qualityReportRef`; `sourcePointer` | MinerU metadata receipt writer payload | ACCEPT |
| Receipt checker requires quality/source-pointer and private-output metadata fields while keeping output content unread. | RUNTIME_BEHAVIOR | `governance/compat/check_mineru_receipt_boundary.py` | lines 37-48, 235-250, and 307-320 | `REQUIRED_FIELDS`; `privateOutputDisposition`; `outputContentRead`; `qualityReportRef`; `sourcePointer` | MinerU receipt boundary checker | ACCEPT |
| R27 requires receipt, quality, source pointer, downstream-use status, claim boundary, and fresh memory owner work order before memory write. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 74 and 85-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED`; `NOT_AUTHORIZED_BY_R27` | MSEA-R27 decision ledger | ACCEPT |
| R24-T4 permits metadata-only receipt evidence and forbids generated output content inspection for committed private evidence. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 53-65 and 212 | `outputContentRead`; `privateOutputDisposition`; `RECEIPT_METADATA_ALLOWED` | MSEA-R24-T4 private-output policy | ACCEPT |
| Focused receipt writer tests already cover receipt payload fields, deterministic quality/source-pointer helper, fail-closed validation, and held downstream lanes. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 47-66, 110-151, 174-238, and 241-249 | `test_receipt_payload_contains_required_r24_r26_metadata_fields`; `test_quality_report_source_pointer_helper_is_deterministic_and_receipt_compatible`; `test_quality_report_source_pointer_helper_fails_closed`; `test_downstream_lanes_remain_held_for_future_packets` | MinerU metadata receipt writer tests | ACCEPT |

## New Doc-Only Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `MEMORY_SAFE_CANDIDATE_CONTRACT` | selected R28-T9 route for metadata-only helper implementation | DOC_ONLY_NEW | use in dispatch, worker return, and helper naming only |
| `MEMORY_SAFE_CANDIDATE_CONTRACT_IMPLEMENTED` | expected material result token if worker implementation is accepted | DOC_ONLY_NEW | use only with tests/gate evidence |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T9_DISPATCH` | hard boundary that T9 does not authorize memory write | DOC_ONLY_NEW | preserve in worker return and tests |
| `T10_ROUTE_SELECTION_RECOMMENDED` | next-route recommendation after accepted T9 evidence | DOC_ONLY_NEW | use only as recommendation, not execution authority |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned R28-T9 paths absent before authoring | `Test-Path` returned `False` for planned R28-T9 baseline, work order, and worker return paths. | PASS |
| Current receipt/source helper check | `rg -n "MineruMetadataReceipt|MineruQualityReportSourcePointer|build_mineru_quality_report_source_pointer|DOWNSTREAM_RELEASE_HELD|claimBoundary|qualityReportRef|sourcePointer" ...` confirmed current helper, receipt fields, and tests exist. | PASS |
| R28-T8 dependency release check | T8 closure state entry and companion matrix rows above confirm `MEMORY_SAFE_CANDIDATE_CONTRACT_RECOMMENDED` and memory write not authorized. | PASS |
| Freshness disposition | Current source has receipt references and quality/source-pointer helper evidence, but no memory-safe candidate contract helper; R28-T9 may dispatch bounded source/test implementation. | PASS |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Exact search roots | `docs`, `CVF_SESSION`, `governance`, and `EXTENSIONS` | PASS |
| Exact search command or query | `rg -n "MSEA-R28-T9|MEMORY_SAFE_CANDIDATE_CONTRACT|memory safe candidate contract" docs CVF_SESSION governance EXTENSIONS` before authoring showed only predecessor next-move/recommendation references and no T9 dispatch artifact. | PASS |
| Same-token collision result | No dedicated R28-T9 baseline, work order, worker return, or source helper existed before authoring. | PASS |
| Absent-versus-collision disposition | Existing T9 mentions were routing evidence only; this packet creates the first R28-T9 dispatch artifacts. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor requirement | Source evidence | R28-T9 handling |
| --- | --- | --- |
| R28-T8 recommends metadata-only memory-safe candidate contract | material commit `cba22bc8`; T8 matrix and state entry | authorize bounded source/test helper implementation |
| R27 requires downstream-use status and claim boundary before memory-safe candidate | R27 ledger rows above | helper must include metadata-only status and claim-boundary fields |
| R24-T4 keeps generated output content private | R24-T4 policy row above | helper must use receipt metadata only |
| T8 forbids memory/RAG write | T8 matrix and state rows above | helper must not create memory records or memory write authority |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit worker -> reviewer/closer -> session-sync steward |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=c4fed412; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch may add only the paired R28-T9 GC-018 baseline and work order; worker may touch only the named receipt writer source, named focused receipt writer test, and worker return path |
| traceScope(phase, actor) | dispatcher trace in this baseline/work order; worker trace in worker return; reviewer trace in closure commit and session-sync |
| commitOwner(phase) | dispatcher may commit dispatch after gates; worker is WORKER_MUST_NOT_COMMIT; reviewer owns material closure; session-sync steward owns continuity sync |
| crossBatchIsolation | no T10 execution, memory write, runtime, provider/live, public-sync, app/use-case/legal, checker/hook edit, or session-sync work inside worker scope |
| nextMoveSurfaces | reviewer/session-sync steward updates front door, generated state, and active handoff only after T9 closure |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return unless reviewer needs a separate closure packet |
| reviewerOwnedClosurePaths | worker return plus named source/test implementation diff |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_WORKER_RETURN_2026-07-04.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Guard owner | `governance/compat/check_foundation_storage_layout.py` |
| Trigger reason | this baseline authorizes a worker return under reviews and bounded source/test edits under an existing extension |
| Stable location decision | no new stable reference family or generated aggregate is created |
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
| Owner surface | paired R28-T9 GC-018 and work order |
| Disposition | ADAPT accepted R28-T8 decision evidence into a bounded source/test implementation dispatch; no external source becomes authority by itself |
| Claim boundary | routing evidence only; no external repository absorption, private/generated content read, MinerU runtime, provider/live proof, public-sync, app, memory write, or production claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T9 dispatch baseline for metadata-only memory-safe candidate contract helper |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata receipt source and checker evidence are cited, but this baseline creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this baseline runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local file reads, source verification, scaffold generation, and governance dispatch gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | dispatch authoring for metadata-only memory-safe candidate contract helper |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior or memory write without fresh source-verified authorization. |

## Evidence / Verification

| Evidence item | Required result | Current dispatch evidence |
| --- | --- | --- |
| Source verification | ACCEPT rows cite CVF-governed surfaces or current runtime source | Source Verification Block in this baseline and paired work order |
| Prior decision release | R28-T8 accepted metadata-only memory-safe candidate contract recommendation while preserving memory hold | T8 matrix, state entry, material commit `cba22bc8`, and session-sync commit `c4fed412` |
| Dispatch gates | pre-dispatch autorun must pass before worker execution begins | pending gate evidence in dispatcher final report |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T9 dispatch is private provenance work only. No public-sync export,
public repository commit, or public catalog claim is included.

## Claim Boundary

This baseline authorizes only a no-commit R28-T9 metadata-only memory-safe
candidate contract helper and focused tests. It does not authorize checker/hook
edits, MinerU runtime execution, private/generated content reads, Candidate
Group A import, memory/RAG write, provider/live proof, public-sync, standalone
app work, legal/use-case deep dive, extraction accuracy, document truth, legal
quality, current-law correctness, workflow-chain production readiness, worker
stage, worker commit, or push.
