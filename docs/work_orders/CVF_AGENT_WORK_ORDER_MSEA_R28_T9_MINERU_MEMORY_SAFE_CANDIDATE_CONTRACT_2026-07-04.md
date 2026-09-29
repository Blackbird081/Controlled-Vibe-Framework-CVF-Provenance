# CVF Agent Work Order - MSEA-R28-T9 MinerU Memory Safe Candidate Contract

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T9-MINERU-MEMORY-SAFE-CANDIDATE-CONTRACT

rawMemoryReleased: false

dispatchBaseHead: c4fed412

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_WORKER_RETURN_2026-07-04.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T9.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. R28-T8 material commit
`cba22bc8` accepted the downstream-use and memory-route release decision
matrix, and session-sync commit `c4fed412` routes the next allowed move to T9
packet authoring for a metadata-only memory-safe candidate contract while
preserving the memory/RAG write hold.

Do-not-misread notes: this packet authorizes only deterministic local
source/test implementation and a worker return. It does not authorize MinerU
runtime execution, private/generated content read, Candidate Group A import,
memory/RAG write, provider/live proof, public-sync, checker/hook edits,
standalone app work, legal/use-case deep dive, extraction accuracy, document
truth, legal quality, current-law correctness, workflow-chain production claim,
worker stage, worker commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the
Source Verification Block, and checker source for worker-created outputs before
writing any file.

Return contract: modify only the named source/test files, create only the
worker return path, run focused pytest, worker-return fast gate, and
pre-implementation autorun, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | operator requested completion of T7-T10 from accepted R28-T8 closure evidence and next-route recommendation |
| Intake role | worker implements deterministic local metadata-only memory-safe candidate contract helper plus tests |
| Scope classification | bounded source/test implementation; no runtime/provider/public/private-content/memory-write behavior |
| Reviewer role | reviewer/closer validates source/test diff, worker return, gates, no-commit discipline, and memory hold |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; source/test changes remain pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require MinerU runtime execution, private/generated content read, memory/RAG write, provider/live proof, public-sync, standalone app work, legal/use-case deep dive, checker/hook edits, session-sync by worker, AGENTS.md edit, active handoff edit, dependency install, destructive command, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Implement a deterministic metadata-only helper that builds a memory-safe
candidate contract from existing MinerU receipt metadata and source-verified
quality/source-pointer refs. The helper must carry downstream-use status and
claim boundary for later T10 route selection while keeping direct memory/RAG
write unauthorized.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | implement named source/test changes and create worker return only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker artifacts, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator asked to complete T7-T10 after R28-T8 was accepted | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` and `CVF_SESSION/ACTIVE_SESSION_STATE.json` route next allowed move to R28-T9 packet authoring only | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V36_2026-07-04.md` names the same next allowed move and parked checkpoints | ACCEPT |
| R28-T8 closure | material commit `cba22bc8` accepted the decision matrix and preserved memory write hold | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_2026-07-04.md` | ACCEPT |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T8 material closure | `docs/reviews/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_WORKER_RETURN_2026-07-04.md` and `docs/reference/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md` at commit `cba22bc8` | ACCEPT |
| R28-T8 session-sync routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at commit `c4fed412` | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `c4fed412` before authoring | ACCEPT |
| Worker execution release | R28-T9 dispatch artifacts and gates must exist before worker begins; this packet supplies that release after commit | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- create `docs/reviews/CVF_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_WORKER_RETURN_2026-07-04.md`;
- add a deterministic metadata-only candidate contract dataclass or helper that uses existing receipt metadata, `quality_report_ref`, `source_pointer`, downstream-use status, and claim boundary;
- prove helper output is stable, omits content fields, preserves held downstream status, and can be derived from a `MineruMetadataReceipt` or its payload without reading files;
- run focused pytest, worker-return fast gate, pre-implementation autorun, and no-commit evidence commands.

Forbidden scope:

- no MinerU command, model/cache mutation, ModelScope, VLM, OCR, parser,
  router, Gradio, Docker, WSL, or runtime smoke;
- no private source document body read and no generated output content read,
  quotation, copy, import, stage, or commit;
- no checker edit, hook wiring, registry aggregate edit, runtime receipt
  instance, memory-layer write, RAG write, adapter implementation, S3, Web,
  MCP, model-router, package lifecycle, action-authority, public-sync,
  provider/live proof, standalone PDF app, legal/use-case deep dive,
  extraction-accuracy claim, document-truth claim, legal advice quality claim,
  current-law correctness claim, production workflow-chain claim, worker stage,
  worker commit, or push;
- no active session state, active handoff, root startup file, AGENTS.md,
  public-sync clone, dependency install, or unrelated documentation edit.

Risk ceiling: R1 deterministic local source/test implementation; no runtime/provider/private-data/public action.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| receipt writer source | worker may modify listed file only | WORKER_MUST_NOT_COMMIT |
| receipt writer focused tests | worker may modify listed file only | WORKER_MUST_NOT_COMMIT |
| worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| checker/hook/source outside listed file/test/registry files | not worker-owned in R28-T9 | forbidden |
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
| checker source for worker return and touched source/test gates | READ_BEFORE_WRITING_OUTPUTS |

## Preflight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Capture execution base | `git rev-parse --short HEAD` | record in worker return |
| Confirm worktree status | `git status --short --untracked-files=all` | record exact pending paths |
| Confirm planned worker return path | `Test-Path docs/reviews/CVF_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_WORKER_RETURN_2026-07-04.md` | no conflicting existing R28-T9 worker artifact |
| Read checker/output source | direct file reads of applicable review, source/test, trace, delta, public-export, worker-return, and dispatch-quality checkers | record exact headings/tokens before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm worktree state | worker return trace |
| 2 | Read worker-output checker source and all Source Verification Block files before editing | Checker Source Read-Ahead Block in worker return |
| 3 | Add deterministic metadata-only memory-safe candidate contract helper in receipt writer source | source diff and focused tests |
| 4 | Add tests proving stable helper output, receipt compatibility, unsafe-marker rejection, no content fields, no memory write, and held downstream route | focused pytest |
| 5 | Create worker return summarizing implementation, changed files, tests, gates, no-commit status, and T10 recommendation | worker return |
| 6 | Run focused pytest, worker-return fast gate, and pre-implementation autorun on the worker changed range | command evidence |
| 7 | Leave changes uncommitted and return for reviewer closure | `git status --short --untracked-files=all` and HEAD unchanged |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T9 --title "MinerU Memory Safe Candidate Contract" --date 2026-07-04 --base c4fed412 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled source verification, deterministic metadata-only contract helper scope, worker output manifest, checker-output read-ahead mandate, handoff control, and held memory-write boundary |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `MEMORY_SAFE_CANDIDATE_CONTRACT`; `MEMORY_SAFE_CANDIDATE_CONTRACT_IMPLEMENTED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T9_DISPATCH`; `T10_ROUTE_SELECTION_RECOMMENDED` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker/test failures directly by reading the
failing source and matching the required shape. Worker should return to
orchestrator only for a source contradiction, forbidden-scope need, live/
provider/public/private-content requirement, checker/hook/session edit
requirement, dependency install, destructive action, or missing authority that
makes completion impossible.

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
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; New Implementation Symbols; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created return requires its own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session state releases R28-T9 packet authoring from accepted R28-T8 evidence and preserves the memory-write hold. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| R28-T8 closure accepted the memory-safe candidate contract recommendation and preserved memory write hold. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T8DownstreamUseAndMemoryRouteReleaseDecisionClosure20260704.json` | lines 5 and 15-24 | `MEMORY_SAFE_CANDIDATE_CONTRACT_RECOMMENDED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T8` | active session state entry | ACCEPT |
| R28-T8 companion matrix selected memory-safe candidate contract first and rejected direct memory/RAG write. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md` | lines 50-63 | `MEMORY_SAFE_CANDIDATE_CONTRACT_RECOMMENDED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T8` | MSEA-R28-T8 decision matrix | ACCEPT |
| Receipt writer declares current receipt version. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | line 17 | `RECEIPT_VERSION` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer keeps downstream release held. | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 19 and 81 | `DOWNSTREAM_RELEASE_HELD`; `downstream_release` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer owns the receipt dataclass, quality/source-pointer dataclass, quality/source-pointer helper, and receipt builder. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 69, 87, 143, and 201 | `MineruMetadataReceipt`; `MineruQualityReportSourcePointer`; `build_mineru_quality_report_source_pointer`; `build_mineru_metadata_receipt` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer validates bounded identifiers and rejects raw-content markers. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 53-57, 98-103, and 125-140 | `_SAFE_ID_RE`; `_UNSAFE_TEXT_MARKERS`; `_validate_quality_source_pointer` | MinerU metadata receipt writer validation | ACCEPT |
| Receipt payload emits quality report, source pointer, downstream, content-read, and claim-boundary metadata fields. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 258-270 | `mineru_metadata_receipt_payload`; `claimBoundary`; `downstreamRelease`; `outputContentRead`; `qualityReportRef`; `sourcePointer` | MinerU metadata receipt writer payload | ACCEPT |
| Receipt checker requires quality report and source pointer fields. | RUNTIME_BEHAVIOR | `governance/compat/check_mineru_receipt_boundary.py` | lines 37-48 and 307-320 | `qualityReportRef`; `sourcePointer`; `QUALITY_OR_SOURCE_POINTER_MISSING` | MinerU receipt boundary checker | ACCEPT |
| Receipt checker keeps committed private output content unread. | RUNTIME_BEHAVIOR | `governance/compat/check_mineru_receipt_boundary.py` | lines 235-250 | `privateOutputDisposition`; `outputContentRead` | MinerU receipt boundary checker | ACCEPT |
| R27 requires receipt, quality, source pointer, downstream-use status, claim boundary, and fresh memory owner work order before memory write. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 74 and 85-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED`; `NOT_AUTHORIZED_BY_R27` | MSEA-R27 decision ledger | ACCEPT |
| R24-T4 private-output policy permits metadata-only receipt evidence while keeping generated output content private. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 53-65 and 212 | `outputContentRead`; `privateOutputDisposition`; `RECEIPT_METADATA_ALLOWED` | MSEA-R24-T4 private-output policy | ACCEPT |
| Focused tests already cover receipt payload fields, deterministic quality/source-pointer helper, fail-closed metadata validation, and held downstream lanes. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 47-66, 110-151, 174-238, and 241-249 | `test_receipt_payload_contains_required_r24_r26_metadata_fields`; `test_quality_report_source_pointer_helper_is_deterministic_and_receipt_compatible`; `test_quality_report_source_pointer_helper_fails_closed`; `test_downstream_lanes_remain_held_for_future_packets` | MinerU metadata receipt writer tests | ACCEPT |

## New Doc-Only Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `MEMORY_SAFE_CANDIDATE_CONTRACT` | selected R28-T9 route for metadata-only helper implementation | DOC_ONLY_NEW | use in dispatch, worker return, and helper naming only |
| `MEMORY_SAFE_CANDIDATE_CONTRACT_IMPLEMENTED` | expected material result token if worker implementation is accepted | DOC_ONLY_NEW | use only with tests/gate evidence |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T9_DISPATCH` | hard boundary that T9 does not authorize memory write | DOC_ONLY_NEW | preserve in worker return and tests |
| `T10_ROUTE_SELECTION_RECOMMENDED` | next-route recommendation after accepted T9 evidence | DOC_ONLY_NEW | use only as recommendation, not execution authority |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact:
`docs/reviews/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_WORKER_RETURN_2026-07-04.md`

recomputeReason: R28-T9 implements deterministic local source/test behavior and
must source-map current owner surfaces directly instead of relying on prior
review prose.

unicodePathHandling: literal UTF-8-safe repository paths only.

extractedTextAuthority: N/A with reason

No sample document text, OCR output, private source document body, or generated
MinerU output content is authorized.

Evidence reuse is limited to CVF-governed predecessor artifacts and current
runtime source. Memory summaries and chat reports are not source authority for
runtime fields.

## New Implementation Symbols

| Proposed symbol | Target file | Required purpose | Worker rule |
| --- | --- | --- | --- |
| `MineruMemorySafeCandidateContract` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | immutable metadata-only value object carrying bounded receipt id, quality/source-pointer refs, downstream status, claim boundary, and memory-write authorization token | add only if it keeps source simple and tests focused |
| `build_mineru_memory_safe_candidate_contract` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | deterministic helper that derives a metadata-only candidate contract from a receipt without reading content or writing memory | add and cover with tests |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned R28-T9 dispatch paths absent before authoring | `Test-Path` returned `False` for planned R28-T9 baseline, work order, and worker return paths. | PASS |
| Token search for R28-T9 before authoring | `rg -n "MSEA-R28-T9|MEMORY_SAFE_CANDIDATE_CONTRACT|memory safe candidate contract" docs CVF_SESSION governance EXTENSIONS` returned predecessor next-move/recommendation references and no existing R28-T9 dispatch artifact before this packet was created. | PASS |
| Current receipt source check | `rg -n "MineruMetadataReceipt|MineruQualityReportSourcePointer|build_mineru_quality_report_source_pointer|DOWNSTREAM_RELEASE_HELD|claimBoundary|qualityReportRef|sourcePointer" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py governance/compat/check_mineru_receipt_boundary.py EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests` confirmed current receipt/helper fields and tests exist. | PASS |
| Freshness disposition | Current source has receipt references and quality/source-pointer helper evidence, but no metadata-only memory-safe candidate contract helper; R28-T9 may dispatch implementation. | PASS |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Exact search roots | `docs`, `CVF_SESSION`, `governance`, and `EXTENSIONS` | PASS |
| Exact search command or query | `rg -n "MSEA-R28-T9|MEMORY_SAFE_CANDIDATE_CONTRACT|memory safe candidate contract" docs CVF_SESSION governance EXTENSIONS` | PASS |
| Coverage across source/tests/docs/JSON/evidence | The search included governed docs, generated session JSON, governance code, and Extraction Foundation source/test surfaces. | PASS |
| Same-token collision result | Current occurrences before authoring were session next-move and T8 recommendation references, not an existing R28-T9 dispatch artifact or implementation. | PASS |
| Absent-versus-collision disposition | No dedicated R28-T9 baseline, work order, worker return, source helper, or focused T9 tests existed before authoring; session references are routing evidence only. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor requirement | Source evidence | R28-T9 handling |
| --- | --- | --- |
| R28-T8 recommends memory-safe candidate contract next | material commit `cba22bc8`; R28-T8 worker return and matrix | authorize deterministic local source/test implementation |
| Receipt writer already accepts `qualityReportRef` and `sourcePointer` metadata | writer and checker source rows above | worker adds candidate contract helper rather than changing receipt schema |
| R24-T4 requires no private/generated output content read | R24-T4 policy row above | helper must use caller-supplied receipt metadata only |
| R27 memory write requires future memory-owner work order | R27 row above | memory/RAG write remains unauthorized; any T10 route-selection dispatch must cite the accepted T9 worker return path, material commit, and session-sync routing evidence before execution |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Extraction Foundation local Python helper and focused tests | internal worker may implement deterministic local metadata helper under WORKER_MUST_NOT_COMMIT; reviewer must accept before closure | this work order, paired GC-018, source verification, worker return, focused pytest | local helper only; no runtime adapter or memory write | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP or external adapter owner in R28-T9 | external ingress, authentication, approval, receipt, raw-data, mutation, and public boundaries remain out of scope | no source-verified external adapter authority in R28-T9 | adapter deferred; no CLI/MCP surface implemented or claimed | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Corpus scan or extraction intake |
| Chain map route | extraction/source evidence -> CVF-owned references and runtime source verification -> fresh GC-018/work order -> autorun pre-dispatch gates |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired R28-T9 GC-018 and this work order |
| Disposition | ADAPT accepted R28-T8 decision evidence into a bounded implementation dispatch; no external source becomes authority by itself |
| Claim boundary | routing evidence only; no external repository absorption, private/generated content read, MinerU runtime, provider/live proof, public-sync, app, memory write, or production claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Guard owner | `governance/compat/check_foundation_storage_layout.py` |
| Trigger reason | this work order authorizes a worker return under reviews and bounded source/test edits under an existing extension |
| Stable location decision | no new stable reference family or generated aggregate is created |
| Index or front-door decision | N/A with reason: no new stable reference front door is introduced |
| Archive or rotation decision | N/A with reason: no existing durable governance file is split, moved, archived, or rotated in this dispatch |
| Generated aggregate decision | no generated aggregate edit is authorized |
| Claim boundary | storage-layout evidence only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker-owned output artifact, read checker source for its
docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under reviews | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, public-export terms, and no-commit evidence shape before writing |

Literal-shape reminders: when listing required section names, write section
names without heading prefixes. If a Findings row exists, use a real
defect-class enum token in the learning disposition. Keep exact source path
verification in this work order and avoid repeating unnecessary extension path
literals in the worker review packet.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit worker -> reviewer/closer -> session-sync steward |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=c4fed412; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | worker may touch only the named receipt writer source, named focused receipt writer test, and worker return path |
| traceScope(phase, actor) | worker records executionBaseHead, changed files, focused pytest, worker-return gate, autorun evidence, and no-commit statement; reviewer records closure evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit if accepted |
| crossBatchIsolation | do not mix R28-T9 with memory-route write, runtime, provider/live, public-sync, app/use-case/legal, checker/hook edits, T10 execution, or session-sync work |
| nextMoveSurfaces | session-sync steward updates front door, active state, and active handoff only when material closure evidence exists |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return unless reviewer needs a separate closure packet |
| reviewerOwnedClosurePaths | worker return plus named source/test implementation diff |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | add deterministic metadata-only memory-safe candidate contract helper and keep receipt/downstream/private-output invariants intact |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | add focused tests for helper determinism, receipt compatibility, unsafe-marker rejection, no content fields, no memory write, and held downstream release |
| `docs/reviews/CVF_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_WORKER_RETURN_2026-07-04.md` | create no-commit evidence packet with changed files, focused tests, gates, selected disposition, and T10 recommendation |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_WORKER_RETURN_2026-07-04.md`

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
| source implementation | exact path, added symbol(s), no content-read behavior, and compatibility with existing receipt builder |
| focused tests | exact pytest command and pass result for receipt writer tests |
| worker return | exact path, executionBaseHead, changed files, no-commit evidence, and selected disposition |
| worker-return fast gate | exact command and pass result |
| pre-implementation autorun | exact command and pass result |
| no-commit evidence | `git status --short --untracked-files=all` and HEAD unchanged |
| claim-boundary evidence | explicit no-runtime/no-private-content/no-memory-release/no-public statement |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Helper implementation | deterministic metadata-only helper produces a bounded candidate contract from receipt metadata and quality/source-pointer refs |
| Receipt compatibility | helper output is derived from `MineruMetadataReceipt` or its payload and preserves receipt metadata invariants |
| Privacy boundary | tests show no private/generated output content is read, quoted, copied, imported, staged, committed, or encoded into helper output |
| Held downstream route | contract output keeps `outputContentRead` false and `DOWNSTREAM_RELEASE_HELD` |
| Memory hold | helper and worker return state memory/RAG write remains unauthorized pending future memory-owner work order |
| Scope | no checker/hook/session/public/runtime/provider/app/legal/deep-quality claim |
| Worker mode | worker leaves all changes uncommitted |

## Fail Conditions

- source facts conflict with the Source Verification Block;
- implementation requires reading private source documents or generated output content;
- implementation requires running MinerU, provider/live proof, memory/RAG, public-sync, app work, checker/hook edits, or dependency installs;
- helper output includes raw-content markers, private full paths, generated output content, extracted text, OCR text, document body text, memory record body, vector content, or memory/RAG write authority;
- worker edits session state, active handoff, AGENTS.md, public-sync, checker/hook source, registry aggregates, or unrelated docs;
- worker stages, commits, or pushes;
- command evidence is missing, stale, or ambiguous.

## Review Gate

Reviewer must inspect the source/test diff, worker return, source verification,
focused pytest, worker-return fast gate, pre-implementation autorun, no-commit
statement, and memory-write hold. Reviewer may repair allowed-scope defects but
must return to orchestrator if acceptance requires runtime/private/provider/
public/memory/checker/session scope expansion.

## Closure Checklist

| Item | Closure disposition |
| --- | --- |
| Source verification still accurate | checked, or BLOCKED with return action |
| Source/test diff inside allowed scope | checked, or BLOCKED with return action |
| Focused pytest passes | checked, or BLOCKED with command evidence |
| Worker-return fast gate passes | checked, or BLOCKED with command evidence |
| Pre-implementation autorun passes | checked, or BLOCKED with command evidence |
| No forbidden runtime/private/provider/public/memory/checker/session action | checked, or BLOCKED with return action |
| Memory-write hold preserved | checked, or BLOCKED with return action |
| Next allowed move stated | checked after review decision |
| Session sync | reviewer/steward only when material closure exists |

## Verification Commands

```powershell
python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base c4fed412 --head HEAD
git status --short --untracked-files=all
```

If the changed range differs from `c4fed412..HEAD` during worker execution,
capture the worker's executionBaseHead and run gates over the real worker
changed range.

## Operator Checkpoint

operator.checkpoint.waiver: Operator requested completion of T7-T10; T9 worker
execution remains bounded by this source-verified work order and returns
uncommitted for reviewer closure. T10 work still requires fresh dependency
release evidence once T9 artifact and commit evidence is accepted.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T9 MinerU Memory Safe Candidate Contract, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, scaffold helper, apply_patch, governance gates |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_2026-07-04.md` |
| Allowed scope source | active session state nextAllowedMove and operator request |
| Before status evidence | clean worktree evidence: `git status --short` returned no output before authoring |
| After status evidence | dispatcher pre-dispatch gates to be recorded before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator requested T7-T10 completion; this dispatch authorizes only T9 implementation packet |
| Claim boundary | dispatch authoring only; no worker execution, runtime, memory/RAG, public-sync, provider/live, private/generated content read, checker/hook edit, or production claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t9-dispatch-2026-07-04` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_2026-07-04.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_2026-07-04.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename performed |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T9 deterministic metadata-only memory-safe candidate contract work order |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata receipt source and checker evidence are cited, but this work order creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this work order runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local source verification, deterministic helper implementation, focused tests, governance gates, and worker return only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | deterministic local metadata-only candidate contract helper implementation and bounded worker evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior, checker/hook edit, or memory write without fresh source-verified authorization. |

## Claim Boundary

This work order authorizes a no-commit worker to implement a deterministic
metadata-only memory-safe candidate contract helper and focused tests. It does
not authorize MinerU runtime execution, private/generated content read, runtime
receipt creation, checker/hook edits, memory/RAG release, adapter work,
provider/live proof, public-sync, app work, legal/use-case deep dive,
extraction accuracy, document truth, legal quality, current-law correctness,
workflow-chain production claim, worker commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T9 is private provenance implementation-dispatch work and does not
change the public-sync repository or public catalog.
