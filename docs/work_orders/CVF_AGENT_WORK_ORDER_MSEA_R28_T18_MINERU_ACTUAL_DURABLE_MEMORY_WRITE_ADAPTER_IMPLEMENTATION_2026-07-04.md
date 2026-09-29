# CVF Agent Work Order - MSEA R28 T18 MinerU Actual Durable Memory Write Adapter Implementation

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T18-MINERU-ACTUAL-DURABLE-MEMORY-WRITE-ADAPTER-IMPLEMENTATION

rawMemoryReleased: false

dispatchBaseHead: 7374b059

closureBaseHead: REVIEWER_TO_SET

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T18.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. T17 material commit
`5166a624` accepted the durable-memory write authority decision and selected
T18 adapter implementation as the next candidate route. Session-sync commit
`7374b059` routes the next move to T18 work-order authoring.

Do-not-misread notes: this packet authorizes only a deterministic
Extraction Foundation source/test adapter candidate and T18 worker return. It
does not authorize actual memory/RAG write, durable-store invocation,
vectorization, retrieval, Learning Plane source edits, checker/hook edits,
session/handoff edits, MinerU runtime execution, private/generated content
read, Candidate Group A import, provider proof, public-sync, standalone app
work, legal/use-case deep dive, extraction accuracy, document truth, legal
quality, current-law correctness, workflow-chain production-readiness claim,
worker stage, worker commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the
Source Verification Block, current target source/test files, and checker
source for worker-created outputs before writing any file.

Return contract: update only the allowed source/test paths, create the T18
worker return, run focused pytest, worker-return fast gate, and
pre-implementation autorun, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | accepted R28-T17 closure evidence and operator T16-T20 system-chain continuation |
| Intake role | worker performs bounded source/test durable-memory write adapter candidate implementation |
| Scope classification | Extraction Foundation source/test adapter candidate and worker return only; no runtime/provider/public/private-content/memory-write behavior |
| Reviewer role | reviewer/closer validates source/test diff, gates, no-commit discipline, and durable-store no-invocation boundary |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; worker changes remain pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require durable-store invocation, actual memory/RAG write, Learning Plane source edit, checker/hook/session/handoff edit, MinerU runtime, private/generated content read, provider/live proof, public-sync, dependency install, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Implement a deterministic metadata-only durable-memory write adapter candidate
for MinerU receipt metadata, using the accepted T16 write-input candidate and
the T17 authority prerequisites. The result should make a future reviewer able
to inspect a policy/actor/provenance-gated adapter payload without performing
any durable-store invocation or memory write in T18.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | implement allowed source/test adapter candidate and worker return only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker artifacts, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator asked to continue T16-T20 system-chain sequence and then write the work order after T17 completion | ACCEPT |
| Active session state | bootstrap and nextAllowedMove route next move to T18 work-order authoring only | ACCEPT |
| R28-T17 closure | material commit `5166a624` selected T18 adapter implementation route while keeping memory write unauthorized by T17 | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_2026-07-04.md` | ACCEPT |

## Operator Checkpoint

| Checkpoint | Resolution |
| --- | --- |
| Operator selected T16-T20 sequence | ACCEPT - T18 proceeds only because T17 selected the adapter implementation route |
| Scope ceiling | ACCEPT - T18 is source/test adapter candidate implementation and worker return only |
| Parked lanes | HELD - actual memory/RAG write, durable-store invocation, runtime, private/generated content read, provider/live proof, public-sync, checker/hook/session/handoff edit by worker, app, legal/use-case, and production workflow-chain claims remain unauthorized |
| Return route | ACCEPT - worker returns uncommitted artifacts for reviewer/closer closure |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T17 material closure | `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md` and material commit `5166a624` | ACCEPT |
| R28-T17 selected T18 route | `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` records `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE` | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `7374b059` before authoring | ACCEPT |
| Worker execution release | T18 dispatch artifacts and gates must exist before worker begins; this packet supplies that release after commit | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- update `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- update `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- create `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`;
- implement source-backed, deterministic, metadata-only adapter candidate
  structures and tests for the T16 durable write-input candidate.

Forbidden scope:

- no edits to Learning Plane TypeScript source, durable store source, runtime
  memory hierarchy source, checker/hook/session/handoff/AGENTS.md/public-sync
  paths by worker;
- no durable memory-store invocation, actual memory/RAG write, vectorization,
  retrieval, provider/live proof, MinerU runtime execution, private/generated
  content read, Candidate Group A import, dependency install, standalone app,
  legal/use-case deep dive, extraction-accuracy claim, document-truth claim,
  legal-quality claim, current-law correctness claim, production workflow-chain
  claim, worker stage, worker commit, or push.

Risk ceiling: local deterministic Python adapter candidate implementation and
focused unit tests only.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| allowed Extraction Foundation source and focused test | worker edits, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| T18 worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| Learning Plane source, durable-store invocation, checker/hook/session/handoff/public/runtime paths | not worker-owned in R28-T18 | forbidden |
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
| target source and test files | READ_BEFORE_EDITING |
| checker source for worker return and governed source/test gates | READ_BEFORE_WRITING_OUTPUTS |

## Preflight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Capture execution base | `git rev-parse --short HEAD` | record in worker return |
| Confirm worktree status | `git status --short --untracked-files=all` | record exact pending paths |
| Confirm planned worker-return path | `Test-Path` for T18 worker return | no conflicting existing R28-T18 worker return |
| Read target source/test | direct file reads of the two allowed Extraction Foundation files | record source/test surfaces inspected |
| Read checker/output source | direct file reads of applicable worker-return, dispatch, and governance checkers | record exact headings/tokens before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm worktree state | worker return trace |
| 2 | Read target source/test, worker-output checker source, and all Source Verification Block files before editing | Checker Source Read-Ahead Block |
| 3 | Add a deterministic adapter candidate dataclass or equivalent structure in the existing MinerU metadata receipt writer module | source diff |
| 4 | Add a builder that accepts a T16 durable write-input candidate and explicit policyDecision, actorAuthorized, actor role, target durable tier, provenanceScore, R27 prerequisite booleans, and claim-boundary metadata | source diff |
| 5 | Fail closed for policy denial, actor authorization failure, low provenance, unauthorized actor role, missing R27 prerequisite, output-content read, memory-write already authorized, or raw/private payload exposure | tests |
| 6 | Add a deterministic payload renderer that keeps summaryOnly true, canReinject false, rawMemoryReleased false, metadata-only fields, and no durable-store invocation token | tests |
| 7 | Extend focused tests for happy path, deterministic payload, actor-tier differences, and each fail-closed condition | pytest evidence |
| 8 | Create worker return summarizing changed files, gates, no-commit status, and remaining durable-store no-invocation hold | worker return |
| 9 | Run focused pytest, worker-return fast gate, and pre-implementation autorun | command evidence |
| 10 | Leave changes uncommitted and return for reviewer closure | `git status --short --untracked-files=all` and HEAD unchanged |

## Implementation Guidance

The worker may choose exact internal implementation details if tests and source
verification remain satisfied, but the preferred shape is:

- introduce a T18 adapter candidate object that references the existing
  `MineruDurableMemoryWriteInputCandidate`;
- expose a builder named close to
  `build_mineru_durable_memory_write_adapter_candidate`;
- expose a payload renderer named close to
  `mineru_durable_memory_write_adapter_candidate_payload`;
- include a disposition token equivalent to
  `DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE_READY`;
- include a hold token equivalent to
  `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T18`;
- preserve T16 `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16_MAPPING_ONLY` as source
  evidence, not as a persistence release.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker, formatting, source-verification,
unit-test, worker-return, or packet-shape failures directly by reading the
failing checker/test and matching the required shape. Worker should return to
orchestrator only for a source contradiction, forbidden-scope need,
live/provider/public/private-content requirement, Learning Plane source edit
requirement, checker/hook/session/handoff edit requirement, dependency install,
destructive action, or missing authority that makes completion impossible.

## Return-To-Orchestrator Conditions

| Condition | Required worker response |
| --- | --- |
| Source/test adapter candidate and worker return completed inside allowed scope with gates passing | return `COMPLETE_PENDING_REVIEW` and leave changes uncommitted |
| Source contradiction blocks adapter implementation | return `BLOCKED_WITH_REASON` with exact source conflict |
| Any needed action is outside allowed scope | return `BLOCKED_WITH_REASON`; do not expand into runtime, durable-store invocation, memory write, public, checker, session, private-output, provider, or Learning Plane edit work |
| Gate failure inside allowed scope | repair by reading the failing checker/test and rerun before returning |
| Worker accidentally stages or commits | stop and return `BLOCKED_WITH_REASON`; reviewer/closer owns recovery |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T18 --title "MinerU Actual Durable Memory Write Adapter Implementation" --date 2026-07-04 --base 7374b059 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile, adapted to bounded source/test adapter implementation |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T18 source verification, dependency release, source/test adapter scope, durable-store no-invocation boundary, worker manifest, checker-output read-ahead mandate, handoff control, and adapter-only claim boundary |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, ADIF-disclosure, public-export, autorun workflow, commit-steward, and governed-file-size checker source surfaces were read before authoring |
| docOnlyNewFields | `MineruDurableMemoryWriteAdapterCandidate`; `build_mineru_durable_memory_write_adapter_candidate`; `mineru_durable_memory_write_adapter_candidate_payload`; `DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE_READY`; `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T18` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router/memory persistence behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, source verification, checker read-ahead, and no-commit discipline. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Dual Agent Surface Matrix; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created source/test changes and worker return require their own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T17 selected T18 adapter implementation while keeping memory write unauthorized by T17. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | lines 56-60 | `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T17_DECISION_ONLY` | T17 decision matrix | ACCEPT |
| T17 worker return states T18 is a candidate route and no write action is released by T17. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md` | lines 57, 66-71, and 89-91 | `t18ReadinessStatus`; `memoryWriteDisposition`; `nextRecommendation` | T17 worker return | ACCEPT |
| T16 source exposes the durable write-input candidate, builder, and payload renderer that T18 may consume. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 167, 635, and 711 | `MineruDurableMemoryWriteInputCandidate`; `build_mineru_durable_memory_write_input_candidate`; `mineru_durable_memory_write_input_candidate_payload` | MinerU metadata receipt writer | ACCEPT |
| T16 mapper keeps memory write unauthorized and source output content unread. | VALUE_SET | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 27, 167-179 | `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16`; `memory_write_disposition`; `output_content_read`; `memory_write_authorized` | MinerU metadata receipt writer | ACCEPT |
| Existing tests cover deterministic durable write-input candidate payload and unsafe-input failure cases. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 602-629, 640-654, and 747-753 | `test_durable_memory_write_input_candidate_is_deterministic_and_metadata_only`; `test_durable_memory_write_input_candidate_changes_with_scope_or_actor`; `test_durable_memory_write_input_candidate_fails_closed_for_unsafe_inputs` | MinerU metadata receipt writer tests | ACCEPT |
| Durable memory store write input names the policy, actor, and provenance fields the adapter must prepare. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 52-63 | `DurableMemoryWriteInput`; `policyDecision`; `actorAuthorized`; `provenanceScore` | Learning Plane durable memory store | ACCEPT |
| Durable memory store denies writes without actor authorization and allow policy. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 195-206 | `write`; `durable_memory_policy_denied`; `actorAuthorized`; `policyDecision` | Learning Plane durable memory store | ACCEPT |
| Durable memory store rejects raw payload-like fields and low provenance before persistence. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 98, 137-143, and 249-263 | `MIN_PROVENANCE_SCORE`; `hasRawPayload`; `raw_memory_payload_rejected`; `low_provenance_score` | Learning Plane durable memory store | ACCEPT |
| Durable memory receipt remains summary-only with no raw release or reinjection. | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 46-48 and 173-175 | `summaryOnly`; `canReinject`; `rawMemoryReleased` | Learning Plane durable memory store | ACCEPT |
| Runtime memory hierarchy defines actor-role values and durable actor authorization lanes. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 12-19 values `OPERATOR`, `GOVERNOR`, `HUMAN`, `BUILDER`, `AI_AGENT`, `REVIEWER`, `SERVICE_AGENT`, `OBSERVER`, `ANALYST`, `unknown`; lines 171-204 durable lanes; lines 273-274 actor membership branch | `RuntimeMemoryActorRole`; `allowedActors`; `durablePersistenceAllowed` | Runtime memory hierarchy | ACCEPT |
| R27 scan-to-memory route requires receipt, quality, source pointer, downstream-use status, and claim boundary before future memory write. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 71-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | R27 decision ledger | ACCEPT |
| R24-T4 private-output policy keeps private/generated output content out of successor routing. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 54-64 and 212 | `privateOutputDisposition`; `PRIVATE_GENERATED_OUTPUT`; policy claim boundary | R24-T4 policy reference | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Source status |
| --- | --- | --- |
| `MineruDurableMemoryWriteAdapterCandidate` | proposed Python dataclass name for T18 worker implementation | DOC_ONLY_NEW |
| `build_mineru_durable_memory_write_adapter_candidate` | proposed Python builder name for T18 worker implementation | DOC_ONLY_NEW |
| `mineru_durable_memory_write_adapter_candidate_payload` | proposed deterministic payload renderer name for T18 worker implementation | DOC_ONLY_NEW |
| `DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE_READY` | proposed adapter-ready disposition token for T18 worker implementation | DOC_ONLY_NEW |
| `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T18` | proposed hold token confirming no durable-store invocation in T18 | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`
priorVerificationAnchor: `5166a624`
freshRecomputeRequired: true
recomputeReason: T18 authorizes source/test implementation, so T16 writer, durable-store, runtime hierarchy, R27, and R24-T4 evidence must be source-verified against current HEAD.
unicodePathHandling: use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames.
extractedTextAuthority: N/A with reason
extractedTextAuthorityReason: no extracted text, private/generated output text, or document body is source authority for T18.

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Dispatch base | `git rev-parse --short HEAD` returned `7374b059` before authoring | ACCEPT |
| Worktree state | `git status --short` was empty before T18 authoring | ACCEPT |
| Existing T18 artifact collision | planned worker-return path was absent before authoring | ACCEPT |
| Existing T18 token search | narrowed governed-artifact/state `rg` returned only current next-move/T17 route mentions before authoring | ACCEPT |
| Runtime execution | No MinerU/provider/live/runtime/memory-store command is authorized by this work order | NOT_APPLICABLE_WITH_REASON |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T18 source/test adapter candidate and worker return | internal reviewer/worker implementation evidence only; no memory write authority | this work order and paired GC-018 | adapter candidate emits metadata-only payload and no durable-store invocation | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external CLI/MCP surface in T18 | external agents receive no actionable write interface from this private packet | public export is deferred | DEFERRED_WITH_REASON: any external adapter requires fresh public-safe contract and authorization | DEFERRED_WITH_REASON |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | update with deterministic durable-memory write adapter candidate implementation only |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | update focused tests for adapter candidate happy path, determinism, actor/provenance/policy gates, privacy, and no-invocation hold |
| `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` | create worker return with command evidence and no-commit statement |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; worker returns uncommitted source/test and worker-return artifacts; reviewer/closer commits accepted material; session-sync steward updates continuity |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=7374b059; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch changes are paired GC-018 and work order only; worker changes are the two allowed Extraction Foundation files and T18 worker return only |
| traceScope(phase, actor) | dispatcher trace in this work order and baseline; worker trace in worker return; reviewer trace through commit steward and gate evidence; session-sync trace in active handoff/front door/state |
| commitOwner(phase) | dispatch author may commit dispatch; WORKER_MUST_NOT_COMMIT; reviewer/closer commits accepted material; session-sync steward commits protected continuity |
| crossBatchIsolation | MSEA-R28-T18 only; do not mix T18 with runtime/provider/live/private-output/public-sync/checker/hook/session/handoff/Learning Plane changes or another tranche |
| nextMoveSurfaces | once accepted T18 material commit exists, session-sync steward must update `CVF_SESSION_MEMORY.md`, active state sources, generated active state, bootstrap read model, and active handoff |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return per governed artifact gotcha 30 |
| reviewerOwnedClosurePaths | allowed Extraction Foundation source/test files and T18 worker return |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without heading prefixes. The worker return must include Purpose,
Target / Source, Scope / Methodology, Findings / Position, Risk / Corrective
Action, Checker Source Read-Ahead Block, Agent Operation Trace Block, Delta
Execution Claim Boundary Control Block, Public Export Disposition, External
Knowledge Intake Routing, Rescan Intelligence Hardening, Corpus Completeness
And Report Integrity, Finding-To-Governance Learning Disposition, Epistemic
Process Block, Claim Boundary, git status --short, Changed Files, Command
Evidence, Worker Experience Retrospective, and No-Commit Statement.

## Evidence Requirements

| Evidence | Required command or artifact |
| --- | --- |
| execution base | `git rev-parse --short HEAD` recorded in worker return |
| worktree status | `git status --short --untracked-files=all` recorded in worker return |
| focused pytest | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py -q` |
| worker-return fast gate | `python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` |
| pre-implementation autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` |
| no-commit discipline | worker return states HEAD unchanged and changes uncommitted |

## Verification Commands

| Phase | Command | Required result |
| --- | --- | --- |
| focused unit test | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py -q` | PASS before reviewer acceptance |
| worker fast gate | `python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | PASS before reviewer acceptance |
| worker autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` | PASS before reviewer acceptance |
| reviewer steward | `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce` | PASS before material commit |
| material hook | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | PASS before material commit |

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker changes only the two allowed Extraction Foundation files and T18 worker return | `git status --short --untracked-files=all` |
| AC2 | Adapter candidate builder consumes the existing T16 durable write-input candidate rather than bypassing it | source diff and tests |
| AC3 | Adapter candidate fails closed unless policyDecision is allow, actorAuthorized is true, provenanceScore is at least 0.7, actor role is allowed for the selected durable tier, and R27 prerequisite booleans are satisfied | source diff and tests |
| AC4 | Adapter payload is deterministic, metadata-only, summaryOnly true, canReinject false, rawMemoryReleased false, output_content_read false, and contains no raw/private output content fields | source diff and tests |
| AC5 | T18 does not call durable store, write memory/RAG, vectorize, retrieve, run MinerU, edit Learning Plane/checker/hook/session/public paths, or claim persistence | worker return and git status |
| AC6 | Actual durable-store invocation and memory/RAG write remain held after T18 unless reviewer closure explicitly releases only a future T19 work-order authoring route | worker return claim boundary |

## Review Gate

Reviewer/closer must verify that the worker did not run MinerU, did not read
private/generated content, did not write memory/RAG, did not invoke durable
memory store, did not edit Learning Plane source, did not edit
checker/hook/session/handoff/public surfaces, and did not create optional
completion review unless required. Reviewer/closer must run focused tests,
worker-return fast gate, reviewer-return commit steward, and pre-commit before
material closure.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T18 MinerU Actual Durable Memory Write Adapter Implementation dispatch, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell (`git`, `rg`, `python governance/compat/*`), apply_patch |
| Target paths | this work order and paired GC-018 baseline |
| Allowed scope source | operator T16-T20 sequence; T17 closure selected T18 adapter implementation while keeping actual write held |
| Before status evidence | clean worktree at HEAD `7374b059`; `git status --short` returned empty output before dispatch authoring |
| After status evidence | two untracked dispatch artifacts only; HEAD unchanged at `7374b059` before dispatch commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only |
| Claim boundary | T18 source/test adapter candidate dispatch; no runtime/private-output/memory-write/public/provider/checker/session/Learning Plane implementation claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t18-dispatch-2026-07-04` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Allowed source/test adapter candidate implemented | PASS or BLOCKED with reason |
| Worker return present and gate-clean | PASS or BLOCKED with reason |
| No forbidden runtime/memory/public/provider/session/checker/Learning Plane path touched by worker | PASS or BLOCKED with reason |
| Durable-store invocation and actual memory/RAG write remain held in T18 unless explicitly released as future T19 authoring only by accepted closure evidence | PASS or BLOCKED with reason |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| storageAction | DOCUMENTATION_ONLY_WITH_REASON |
| storageRoot | N/A with reason: T18 dispatch creates no storage root and writes no memory/RAG store |
| indexUpdate | N/A with reason: no file-storage index is modified |
| claimBoundary | no storage adapter invocation, memory store write, RAG store, S3, public-sync, or runtime persistence behavior is authorized by dispatch |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> T16 adapter mapping -> T17 authority decision -> T18 adapter implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired GC-018 baseline |
| Disposition | ADAPT accepted T17 authority decision into bounded source/test adapter implementation dispatch |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session/handoff edit, Learning Plane edit, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T18 work order for durable-memory write adapter candidate implementation |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store invocation, memory/RAG write, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime or memory-store receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, or external action is executed or observed. |
| invocationBoundary | source/test adapter candidate dispatch and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | work-order dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory persistence behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T18 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.

## Claim Boundary

This work order authorizes only a bounded source/test durable-memory write
adapter candidate implementation and worker return. It does not authorize
actual memory/RAG write, durable-store invocation, vectorization, retrieval,
Learning Plane source edits, checker/hook edits, session/handoff edits by
worker, MinerU runtime execution, private/generated content read, Candidate
Group A import, provider/live proof, public-sync, standalone app work,
legal/use-case deep dive, extraction accuracy, document truth, legal quality,
current-law correctness, workflow-chain production readiness, session-sync by
worker, worker stage, worker commit, or push.
