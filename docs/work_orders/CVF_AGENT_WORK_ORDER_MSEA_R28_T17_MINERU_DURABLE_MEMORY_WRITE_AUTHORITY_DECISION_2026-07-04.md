# CVF Agent Work Order - MSEA R28 T17 MinerU Durable Memory Write Authority Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T17-MINERU-DURABLE-MEMORY-WRITE-AUTHORITY-DECISION

rawMemoryReleased: false

dispatchBaseHead: f0800b95

closureBaseHead: REVIEWER_TO_SET

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T17.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. T16 material commit
`0bf81a68` accepted the summary-only durable-memory write-input candidate
mapper and kept actual memory/RAG write unauthorized. Session-sync commit
`f0800b95` routes the next move to T17 work-order authoring.

Do-not-misread notes: this packet authorizes only docs-only decision matrix and
worker return authoring. It does not authorize actual memory/RAG write,
durable-store invocation, vectorization, retrieval, source/test/checker/hook
edits, MinerU runtime execution, private/generated content read, Candidate
Group A import, provider proof, public-sync, standalone app work,
legal/use-case deep dive, extraction accuracy, document truth, legal quality,
current-law correctness, workflow-chain release claim, session-sync by worker,
worker stage, worker commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the
Source Verification Block, and checker source for worker-created outputs before
writing any file.

Return contract: create only the companion decision matrix and T17 worker
return, run worker-return fast gate and pre-implementation autorun, leave
changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | accepted R28-T16 closure evidence and operator T16-T20 sequence selection |
| Intake role | worker performs bounded docs-only durable-memory write authority decision |
| Scope classification | decision matrix and worker return only; no runtime/provider/public/private-content/memory-write behavior |
| Reviewer role | reviewer/closer validates decision evidence, gates, no-commit discipline, and memory-write hold boundary |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; worker changes remain pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require durable-store invocation, memory/RAG write, source/test/checker/hook/session edit, MinerU runtime, private/generated content read, provider/live proof, public-sync, dependency install, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Create the T17 source-verified durable-memory write authority decision matrix
that determines whether a later T18 packet may implement actual durable-memory
write behavior from the accepted T16 summary-only write-input candidate.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | author companion decision matrix and worker return only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker artifacts, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | operator selected the T16-T20 system-chain continuation | ACCEPT |
| Active session state | bootstrap and nextAllowedMove route next move to T17 work-order authoring only | ACCEPT |
| R28-T16 closure | material commit `0bf81a68` selected T17 authority-decision work-order authoring while keeping memory write unauthorized | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_2026-07-04.md` | ACCEPT |

## Operator Checkpoint

| Checkpoint | Resolution |
| --- | --- |
| Operator selected T16-T20 sequence | ACCEPT - T17 proceeds only because T16 closed mapping-only release |
| Scope ceiling | ACCEPT - T17 is decision matrix and worker return only |
| Parked lanes | HELD - actual memory/RAG write, runtime, private/generated content read, provider/live proof, public-sync, checker/hook edit, app, legal/use-case, and production workflow-chain claims remain unauthorized |
| Return route | ACCEPT - worker returns uncommitted artifacts for reviewer/closer closure |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T16 material closure | `docs/reviews/CVF_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` and material commit `0bf81a68` | ACCEPT |
| R28-T16 selected T17 route | `CVF_SESSION/state/entries/mseaR28T16MineruMemoryStoreAdapterMappingImplementationClosure20260704.json` records the T17 authoring route | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `f0800b95` before authoring | ACCEPT |
| Worker execution release | T17 dispatch artifacts and gates must exist before worker begins; this packet supplies that release after commit | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md`;
- create `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`;
- decide whether future T18 actual durable-memory write implementation is
  source-backed, still held, or blocked;
- document policyDecision, actorAuthorized, provenanceScore, raw-payload,
  receipt, and actor-role prerequisites for any future write packet.

Forbidden scope:

- no source/test/checker/hook/session/handoff/AGENTS.md edits by worker;
- no durable memory-store invocation, memory/RAG write, vectorization,
  retrieval, provider/live proof, MinerU runtime execution, private/generated
  content read, Candidate Group A import, public-sync, Web/MCP/model-router
  work, dependency install, standalone app, legal/use-case deep dive,
  extraction-accuracy claim, document-truth claim, legal-quality claim,
  current-law correctness claim, production workflow-chain claim, worker stage,
  worker commit, or push.

Risk ceiling: docs-only authority decision and matrix authoring.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| T17 companion decision matrix | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| T17 worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| source/test/checker/hook/session/public/runtime/durable-store invocation paths | not worker-owned in R28-T17 | forbidden |
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
| Confirm planned output paths | `Test-Path` for T17 matrix and worker return | no conflicting existing R28-T17 outputs |
| Read checker/output source | direct file reads of applicable worker-return, reference, and governance checkers | record exact headings/tokens before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm worktree state | worker return trace |
| 2 | Read worker-output checker source and all Source Verification Block files before editing | Checker Source Read-Ahead Block |
| 3 | Author the companion decision matrix with a source-verified decision summary and route-selection table | matrix diff |
| 4 | Evaluate policyDecision, actorAuthorized, provenanceScore, raw-payload, receipt, actor-role, privacy, and R27 prerequisite rows | matrix evidence rows |
| 5 | Create worker return summarizing decision, changed files, gates, no-commit status, and remaining actual-write hold | worker return |
| 6 | Run worker-return fast gate and pre-implementation autorun | command evidence |
| 7 | Leave changes uncommitted and return for reviewer closure | `git status --short --untracked-files=all` and HEAD unchanged |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker, formatting, source-verification,
matrix-shape, or packet-shape failures directly by reading the failing
checker/test and matching the required shape. Worker should return to
orchestrator only for a source contradiction, forbidden-scope need,
live/provider/public/private-content requirement, source/test/checker/hook/
session edit requirement, dependency install, destructive action, or missing
authority that makes completion impossible.

## Return-To-Orchestrator Conditions

| Condition | Required worker response |
| --- | --- |
| Matrix and worker return completed inside allowed scope with gates passing | return `COMPLETE_PENDING_REVIEW` and leave changes uncommitted |
| Source contradiction blocks decision | return `BLOCKED_WITH_REASON` with exact source conflict |
| Any needed action is outside allowed scope | return `BLOCKED_WITH_REASON`; do not expand into runtime, memory write, public, source/test, checker, session, private-output, or provider work |
| Gate failure inside allowed scope | repair by reading the failing checker/test and rerun before returning |
| Worker accidentally stages or commits | stop and return `BLOCKED_WITH_REASON`; reviewer/closer owns recovery |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T17 --title "MinerU Durable Memory Write Authority Decision" --date 2026-07-04 --base f0800b95 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile, adapted to docs-only authority decision tranche |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T17 source verification, dependency release, docs-only matrix scope, no-memory-write boundary, worker manifest, checker-output read-ahead mandate, handoff control, and actual-write hold |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX`; `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T17_DECISION_ONLY` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router/memory behavior claim. |

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
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; Dual Agent Surface Matrix; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created return and matrix require their own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T16 closure accepted mapper-only behavior and released T17 authoring while keeping memory write unauthorized. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T16MineruMemoryStoreAdapterMappingImplementationClosure20260704.json` | lines 19-22 | `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16_MAPPING_ONLY`; `AUTHOR_MSEA_R28_T17_GC018_AND_SOURCE_VERIFIED_WORK_ORDER_FOR_ACTUAL_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION` | active session state source entry | ACCEPT |
| T16 source exposes durable write-input candidate dataclass, builder, and payload renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 167, 635, and 711 | `MineruDurableMemoryWriteInputCandidate`; `build_mineru_durable_memory_write_input_candidate`; `mineru_durable_memory_write_input_candidate_payload` | MinerU metadata receipt writer | ACCEPT |
| T16 mapper keeps memory write unauthorized and output content unread. | VALUE_SET | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 27, 167-179, and 663-669 | `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16`; `output_content_read`; `memory_write_authorized` | MinerU metadata receipt writer | ACCEPT |
| Durable memory store write input names the policy, actor, and provenance fields a future write packet must decide. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 52-63 | `DurableMemoryWriteInput`; `policyDecision`; `actorAuthorized`; `provenanceScore` | Learning Plane durable memory store | ACCEPT |
| Durable memory store denies writes without actor authorization and allow policy. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 195-206 | `write`; `durable_memory_policy_denied`; `actorAuthorized`; `policyDecision` | Learning Plane durable memory store | ACCEPT |
| Durable memory store rejects raw payload-like fields and low provenance before persistence. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 98, 137-143, and 249-263 | `MIN_PROVENANCE_SCORE`; `hasRawPayload`; `raw_memory_payload_rejected`; `low_provenance_score` | Learning Plane durable memory store | ACCEPT |
| Durable memory receipt remains summary-only with no raw release or reinjection. | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 46-48 and 173-175 | `summaryOnly`; `canReinject`; `rawMemoryReleased` | Learning Plane durable memory store | ACCEPT |
| Runtime memory hierarchy defines actor-role values and durable actor authorization lanes. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 10-18 values `OPERATOR`, `GOVERNOR`, `HUMAN`, `BUILDER`, `AI_AGENT`, `REVIEWER`, `SERVICE_AGENT`, `OBSERVER`, `ANALYST`, `unknown`; lines 173-204 durable lanes; lines 273-276 actor-denial branch | `RuntimeMemoryActorRole`; `allowedActors`; `m1_durable_cross_session`; `actor_not_allowed_for_memory_tier` | Runtime memory hierarchy | ACCEPT |
| R27 scan-to-memory route requires receipt, quality, source pointer, downstream-use status, and claim boundary before future memory write. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 71-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | R27 decision ledger | ACCEPT |
| R24-T4 private-output policy keeps private/generated output content out of successor routing. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 54-64 and 212 | `privateOutputDisposition`; `PRIVATE_GENERATED_OUTPUT`; policy claim boundary | R24-T4 policy reference | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Source status |
| --- | --- | --- |
| `DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX` | proposed T17 companion matrix disposition family | DOC_ONLY_NEW |
| `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE` | proposed future route token if source evidence supports T18 authoring | DOC_ONLY_NEW |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T17_DECISION_ONLY` | proposed T17 hold token confirming no actual write in T17 | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`
priorVerificationAnchor: `0bf81a68`
freshRecomputeRequired: true
recomputeReason: T17 evaluates actual write authority prerequisites, so durable-store and runtime actor gates must be source-verified against current HEAD.
unicodePathHandling: use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames.
extractedTextAuthority: N/A with reason
extractedTextAuthorityReason: no extracted text, private/generated output text, or document body is source authority for T17.

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Dispatch base | `git rev-parse --short HEAD` returned `f0800b95` before authoring | ACCEPT |
| Worktree state | `git status --short` was empty before T17 authoring | ACCEPT |
| Existing T17 artifact collision | planned matrix and worker-return paths were absent before authoring | ACCEPT |
| Existing Extraction Foundation mapper | `rg` found only T16 mapper and tests under Extraction Foundation; no actual durable-store invocation is authorized by this work order | ACCEPT |
| Runtime execution | No MinerU/provider/live/runtime/memory-store command is authorized by this work order | NOT_APPLICABLE_WITH_REASON |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T17 decision matrix and worker return | internal reviewer/worker decision evidence only; no memory write authority | this work order and paired GC-018 | N/A with reason: no runtime adapter in T17 | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external CLI/MCP surface in T17 | external agents receive no actionable write interface from this private packet | public export is deferred | DEFERRED_WITH_REASON: any external adapter requires fresh public-safe contract and authorization | DEFERRED_WITH_REASON |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | create source-verified decision matrix selecting future T18 route, hold, or block |
| `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md` | create worker return with command evidence and no-commit statement |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; worker returns uncommitted matrix and worker-return artifacts; reviewer/closer commits accepted material; session-sync steward updates continuity |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=f0800b95; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch changes are paired GC-018 and work order only; worker changes are T17 companion matrix and T17 worker return only |
| traceScope(phase, actor) | dispatcher trace in this work order and baseline; worker trace in worker return; reviewer trace through commit steward and gate evidence; session-sync trace in active handoff/front door/state |
| commitOwner(phase) | dispatch author may commit dispatch; WORKER_MUST_NOT_COMMIT; reviewer/closer commits accepted material; session-sync steward commits protected continuity |
| crossBatchIsolation | MSEA-R28-T17 only; do not mix T17 with runtime/provider/live/private-output/public-sync/source/test/checker/hook/session changes or another tranche |
| nextMoveSurfaces | once accepted T17 material commit exists, session-sync steward must update `CVF_SESSION_MEMORY.md`, active state sources, generated active state, bootstrap read model, and active handoff |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_COMPLETION_2026-07-04.md` optional; prefer repairing evidence in the worker return per governed artifact gotcha 30 |
| reviewerOwnedClosurePaths | T17 companion decision matrix; T17 worker return |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
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
| worker-return fast gate | `python governance/compat/run_worker_return_fast_gate.py` |
| pre-implementation autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` |
| no-commit discipline | worker return states HEAD unchanged and changes uncommitted |

## Verification Commands

| Phase | Command | Required result |
| --- | --- | --- |
| worker fast gate | `python governance/compat/run_worker_return_fast_gate.py` | PASS before reviewer acceptance |
| worker autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` | PASS before reviewer acceptance |
| reviewer steward | `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce` | PASS before material commit |
| material hook | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | PASS before material commit |

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker changes only T17 companion matrix and T17 worker return | `git status --short --untracked-files=all` |
| AC2 | Matrix source-verifies durable-store write policy, actor authorization, provenance score, raw-payload rejection, summary-only receipt, R27 prerequisites, and R24-T4 privacy boundary | matrix Source Verification Block |
| AC3 | Matrix selects exactly one future-route disposition and keeps T17 memory write unauthorized | matrix Decision Summary and worker return |
| AC4 | T17 itself does not call durable store, write memory/RAG, vectorize, retrieve, run MinerU, or edit source/test/checker/hook/session/public paths | worker return and git status |
| AC5 | Actual memory/RAG write remains unauthorized after T17 unless reviewer closure explicitly releases only a future T18 work-order authoring route | worker return claim boundary |

## Review Gate

Reviewer/closer must verify that the worker did not run MinerU, did not read
private/generated content, did not write memory/RAG, did not invoke durable
memory store, did not edit source/test/checker/hook/session/public surfaces,
and did not create optional completion review unless required. Reviewer/closer
must run reviewer-return commit steward and pre-commit before material closure.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T17 MinerU Durable Memory Write Authority Decision dispatch, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell (`git`, `rg`, `python governance/compat/*`), apply_patch |
| Target paths | this work order and paired GC-018 baseline |
| Allowed scope source | operator selected T16-T20 sequence; T16 closure selected T17 authority-decision authoring while keeping actual write held |
| Before status evidence | clean worktree at HEAD `f0800b95`; `git status --short` returned empty output before dispatch authoring |
| After status evidence | two untracked dispatch artifacts only; HEAD unchanged at `f0800b95` before dispatch commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only |
| Claim boundary | T17 docs-only authority decision dispatch; no runtime/private-output/memory-write/public/provider/source/test/checker/session implementation claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t17-dispatch-2026-07-04` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| T17 companion matrix present and source-verified | PASS or BLOCKED with reason |
| Worker return present and gate-clean | PASS or BLOCKED with reason |
| No forbidden runtime/memory/public/provider/session/checker/source/test path touched by worker | PASS or BLOCKED with reason |
| Actual memory/RAG write remains held in T17 unless explicitly released as future T18 authoring only by accepted closure evidence | PASS or BLOCKED with reason |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| storageAction | DOCUMENTATION_ONLY_WITH_REASON |
| storageRoot | N/A with reason: T17 dispatch creates no storage root and writes no memory/RAG store |
| indexUpdate | N/A with reason: no file-storage index is modified |
| claimBoundary | no storage adapter invocation, memory store write, RAG store, S3, public-sync, or runtime persistence behavior is authorized by dispatch |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> T16 adapter mapping -> T17 write authority decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired GC-018 baseline |
| Disposition | ADAPT accepted T16 mapping closure into a bounded docs-only authority decision dispatch |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session edit, source/test edit, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T17 work order for durable-memory write authority decision |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store write, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime or memory-store receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, or external action is executed or observed. |
| invocationBoundary | docs-only authority decision dispatch and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | work-order dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T17 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.

## Claim Boundary

This work order authorizes only a bounded docs-only durable-memory write
authority decision matrix and worker return. It does not authorize actual
memory/RAG write, durable-store invocation, vectorization, retrieval,
source/test/checker/hook edits by worker, MinerU runtime execution,
private/generated content read, Candidate Group A import, provider/live proof,
public-sync, standalone app work, legal/use-case deep dive, extraction
accuracy, document truth, legal quality, current-law correctness,
workflow-chain production readiness, session-sync by worker, worker stage,
worker commit, or push.
