# CVF Agent Work Order - MSEA R41 T1 MinerU File Backed Persistence Release Authority Decision

Memory class: governed-work-order

Status: DISPATCH_READY

Created: 2026-07-06

rawMemoryReleased: false

## Dispatch Prompt Envelope

dispatchId: MSEA-R41-T1-MINERU-FILE-BACKED-PERSISTENCE-RELEASE-AUTHORITY-DECISION

route: WORKER_MUST_NOT_COMMIT

taskClass: Work-order execution / authority decision

role: worker

dispatchBaseHead: `1559f6461`

executionBaseHead: WORKER_CAPTURE_AT_START

closureBaseHead: REVIEWER_SET_AT_CLOSURE

Commit mode: WORKER_MUST_NOT_COMMIT

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_2026-07-06.md`

Current-time notes: Artifact date is 2026-07-06. The operator selected the
file-backed persistence authority lane after R40-T1 bounded provider/live
proof closure.

Do-not-misread notes: This packet authorizes a docs-only authority decision.
It does not authorize file-backed persistence invocation, MinerU runtime,
private/generated output reads, production Memory/RAG release, retrieval,
vectorization, public-sync, worker commit, push, public claim, extraction
accuracy, document truth, legal quality, current-law correctness, or any
hosted/public/production release claim.

Required first actions: read this work order, paired GC-018 baseline,
mandatory startup files, guard orientation, and literal gotchas. Recompute
source anchors before writing either output artifact.

Return contract: create the decision matrix and worker-return artifact, record
final `git status --short --untracked-files=all`, run worker-return fast gate
and pre-implementation autorun gate, and stop for reviewer closure. Do not
commit.

workerTargetPaths:

- `docs/reference/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md`

workerReturnPath:

- `docs/reviews/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-06.md`

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py` read as the required helper surface; packet was manually authored for R41-T1 |
| generatedProfile | work order / source-verified dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Manual source-verified authoring for MinerU file-backed persistence release authority decision |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| docOnlyNewFields | `Scaffold Provenance Block` |
| claimBoundary | Dispatch scaffold provenance only; no runtime, private-output read, production release, public-sync, worker commit, push, or public claim |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| intake summary | Operator asked to create the next work order for the file-backed persistence authority lane |
| scope classification | Docs-only source-verified release authority decision |
| risk sensitivity | High: persistence release can be misread as production Memory/RAG or durable-store invocation authority |
| selected role route | routeMode: MULTI_AGENT_SINGLE_ROLE |
| role separation basis | Dispatcher authors GC-018/work order; worker creates decision matrix and worker return without commit; reviewer/closer owns closure and material commit; session-sync steward owns continuity update |
| escalation condition | Return to orchestrator if the decision would require source/test edits, file-backed persistence invocation, MinerU runtime, private/generated output reads, production release, public-sync, or raw secret handling |

## Worker Autonomy / No-Question Rule

The worker may proceed without wording or preference questions. The worker
must repair allowed-scope checker failures directly by reading the failing
checker source and matching the literal required shape.

The worker must stop and return `BLOCKED_WITH_REASON` if the decision cannot
be source-verified or if it would need to cross any forbidden scope.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Dispatcher | Authored this GC-018/source-verified R41-T1 work order and paired baseline |
| Worker | Creates the decision matrix, writes worker return, runs gates, and does not commit |
| Reviewer/closer | Reviews output, verifies gates, repairs only within scope if needed, and owns material closure commit |
| Session-sync steward | Updates session surfaces only after accepted reviewer closure changes current mode or next allowed move |

## Purpose

Decide whether MinerU file-backed persistence can be released, must remain
held, or requires a narrower implementation packet. The decision must be
source-verified against current durable-memory store source, current
system-chain route behavior, and accepted R38/R39/R40 evidence.

## Authority Chain

| Authority | Role in R41-T1 |
| --- | --- |
| Operator instruction on 2026-07-06 | Selects the file-backed persistence authority decision lane |
| Paired GC-018 baseline | Authorizes docs-only dispatch |
| R38 T4 release-gate decision | Names file-backed persistence as a held authority lane requiring a fresh packet |
| R39 T1 authority decision | Confirms production Memory/RAG route release remains held pending authority gaps |
| R40 T1 provider-live proof closure | Confirms only bounded provider-live proof is complete, not persistence release |
| Current durable-memory store source | Provides in-process and file-backed store factories plus receipt invariants |
| Current system-chain route candidate source | Shows file-backed persistence requests still fail closed |
| ADIF-0024 | Requires final command rerun and workspace hygiene disclosure |

## Roadmap-To-Work-Order Trace Matrix

| Driver | Work-order requirement | Disposition |
| --- | --- | --- |
| R38 selected stop after foundation/internal system-chain audit | Do not open broad implementation or use-case work | SATISFIED_BY_DOCS_ONLY_AUTHORITY_DECISION |
| R39 held production Memory/RAG route release pending authority gaps | Decide persistence authority before production route work | SATISFIED_BY_THIS_PACKET |
| R40 completed only bounded provider-live proof | Do not treat live proof as persistence release | SATISFIED_BY_THIS_PACKET |
| Operator requested next work order | Author fresh source-verified R41-T1 dispatch | SATISFIED_BY_THIS_PACKET |

## Operator Checkpoint

Operator checkpoint is satisfied for this packet only: the operator asked to
create the R41-T1 work order for the next roadmap lane.

Any implementation, file-backed invocation, production Memory/RAG route
release, private-output policy release, public-sync, or use-case/legal
workflow still requires a separate fresh packet.

## Pre-flight Checks

| Check | Required worker evidence |
| --- | --- |
| Worktree before edits | `git status --short --untracked-files=all` from the provenance workspace |
| Dispatch base capture | `git rev-parse --short HEAD` at worker start |
| Source-anchor recompute | Fresh `rg -n` or equivalent source reads for each runtime/source symbol cited in this packet |
| Provider-local hygiene | Inspect and disclose provider-local or IDE side-channel files; do not create, stage, or rely on them as authority |
| Negative scope check | Confirm no MinerU runtime, private-output read, source/test edit, file-backed invocation, provider/live call, or public-sync is needed |

## Write Ownership

| Surface | Owner |
| --- | --- |
| R41-T1 decision matrix | Worker may create |
| R41-T1 worker return | Worker may create |
| Existing source and tests | Worker may read only; do not edit |
| Session state, active handoff, session memory | Not worker-owned |
| Public-sync clone or public catalog | Not worker-owned |
| Provider-local configuration or memory files | Not worker-owned; do not create, stage, or rely on them as authority |

## Required First Reads

Before writing, read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- active handoff named by session state
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_2026-07-06.md`
- this work order
- `docs/reference/CVF_MSEA_R38_T4_MINERU_TO_MEMORY_SCANLAYER_RELEASE_GATE_DECISION_2026-07-06.md`
- `docs/reference/CVF_MSEA_R39_T1_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md`
- `docs/reviews/CVF_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_COMPLETION_2026-07-06.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts`

## Mission

Create a source-verified decision matrix that selects exactly one disposition:

- `R41_T1_FILE_BACKED_PERSISTENCE_RELEASE_READY_FOR_NARROW_IMPLEMENTATION_PACKET`
- `R41_T1_FILE_BACKED_PERSISTENCE_RELEASE_HELD_PENDING_AUTHORITY_GAPS`
- `R41_T1_FILE_BACKED_PERSISTENCE_RELEASE_REJECTED_STOP`

The matrix must explain why the selected disposition follows from current
source and accepted governed evidence. It must preserve all boundaries if the
answer is held or rejected, and it must require a separate implementation
packet if the answer is "ready for narrow implementation packet."

## Allowed Scope

You may create only:

- `docs/reference/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md`
- `docs/reviews/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-06.md`

You may run:

- source reads and `rg -n` commands
- worker-return and pre-implementation gates required by the current workflow

## Forbidden Scope

Do not:

- edit source files, existing tests, generated JSON aggregates, session state,
  active handoff, public-sync files, or provider-local files;
- run MinerU runtime or read, quote, summarize, copy, import, stage, or commit
  private/generated MinerU output content;
- invoke file-backed persistence, production durable store, production
  Memory/RAG route, retrieval, vectorization, or reinjection;
- run provider/live proof or rely on live output as authority;
- claim extraction accuracy, document truth, legal quality, current-law
  correctness, hosted readiness, public readiness, or production readiness;
- create a public claim, public-sync batch, worker commit, or push.

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Capture execution base and worktree status | `git rev-parse --short HEAD`; `git status --short --untracked-files=all` |
| 2 | Read startup, baseline, work order, R38/R39/R40 evidence, and current source files | Source Inventory in worker return |
| 3 | Recompute source anchors | fresh `rg -n` or equivalent read evidence |
| 4 | Create decision matrix | target path under `docs/reference` |
| 5 | Create worker return | target path under `docs/reviews` |
| 6 | Run worker-return fast gate and pre-implementation gate | command output |
| 7 | Stop without committing | final `git status --short --untracked-files=all` showing only allowed paths |

## Verification Commands

Worker must run these commands after final edits and record exact output
summaries in the worker return:

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Durable memory store exposes a file-backed factory | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 106-110 | `createFileBackedDurableMemoryStore` | durable memory store | EXISTS | ACCEPT |
| Durable memory receipt records durable persistence and keeps summary-only/non-reinject/raw-release invariants | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 36-44 | `DurableMemoryReceipt` | durable memory store | EXISTS | ACCEPT |
| File-backed store reads and writes JSON records through a file-backed class | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 415-450 | `FileBackedDurableMemoryStore` | durable memory store | EXISTS | ACCEPT |
| Memory/RAG route helper remains a bounded candidate and does not authorize production persistence | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 1-13 and 33-34 | `MEMORY_RAG_ROUTE_RELEASE_NOT_PRODUCTION_AUTHORIZED_BY_T22` | MinerU Memory/RAG route release candidate | VALUE_SET | ACCEPT |
| Memory/RAG route result keeps productionRouteAuthorized false | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 64 and 231 | `productionRouteAuthorized` | MinerU Memory/RAG route release candidate | VALUE_SET | ACCEPT |
| System-chain route candidate explicitly models file-backed persistence requests | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 34-43 | `MineruSystemChainRouteAuthority` | MinerU system-chain route candidate | EXISTS | ACCEPT |
| System-chain route candidate fails closed when file-backed persistence is requested | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 105-110 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | MinerU system-chain route candidate | VALUE_SET | ACCEPT |
| System-chain route candidate accepts only in-process persistence in the accepted candidate path | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 156-158 | `persistenceMode` | MinerU system-chain route candidate | VALUE_SET | ACCEPT |
| R38 T4 preserved file-backed persistence as a held authority lane needing a fresh packet | `docs/reference/CVF_MSEA_R38_T4_MINERU_TO_MEMORY_SCANLAYER_RELEASE_GATE_DECISION_2026-07-06.md` | lines 60-64 | `file-backed persistence` | R38 release-gate decision | VALUE_SET | ACCEPT |
| R39 T1 held production Memory/RAG route release pending authority gaps | `docs/reference/CVF_MSEA_R39_T1_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` | lines 53 and 89 | `R39_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_HELD_PENDING_AUTHORITY_GAPS` | R39-T1 authority decision matrix | VALUE_SET | ACCEPT |
| R40 T1 completed only bounded provider-live proof and did not release file-backed persistence | `docs/reviews/CVF_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_COMPLETION_2026-07-06.md` | lines 55 and 103-105 | `R40_T1_PROVIDER_LIVE_PROOF_COMPLETE_BOUNDED_PRIVATE` | R40-T1 completion review | VALUE_SET | ACCEPT |
| Active session routes the next move to fresh source-verified packet selection or stop | `CVF_SESSION_MEMORY.md` | Next Allowed Move section | `msea_r40_t1_mineru_system_chain_provider_live_proof_closed_pending_next_roadmap_selection_or_stop` | active session front door | VALUE_SET | ACCEPT |

## Planned Worker Fulfillment Manifest

| Planned artifact | Type | Owner | Required proof literal |
| --- | --- | --- | --- |
| `docs/reference/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` | decision matrix | worker | one selected R41-T1 disposition token |
| `docs/reviews/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-06.md` | worker return | worker | `COMPLETE_PENDING_REVIEW` |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must include these literal sections:

- Purpose
- Target / Source
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Decision / Disposition
- Source Inventory
- Source Verification Block
- ADIF Defect Registry Disclosure
- Checker Source Read-Ahead Block
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- External Knowledge Intake Routing
- Public Export Disposition
- Claim Boundary

It must also include `executionBaseHead`, command evidence, final
`git status --short --untracked-files=all`, and an explicit no-commit
statement.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R41-T1 dispatch authoring, 2026-07-06 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `Get-Content`; `rg`; `python governance/compat/run_adif_defect_resolver.py`; `apply_patch`; governance dispatch checks |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_2026-07-06.md` |
| Allowed scope source | operator selected file-backed persistence authority decision lane with R40-T1 completion evidence at `docs/reviews/CVF_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_COMPLETION_2026-07-06.md` and current base commit `1559f6461` |
| Before status evidence | HEAD `1559f6461`; worktree clean before R41-T1 dispatch artifact authoring |
| After status evidence | R41-T1 dispatch packet pending pre-dispatch gates |
| Diff evidence | `git diff --name-status 1559f6461..HEAD` |
| Approval boundary | dispatch authoring only |
| Claim boundary | no persistence release or invocation has been run by the dispatch packet itself |
| Agent type | dispatcher |
| Invocation ID | `msea-r41-t1-mineru-file-backed-persistence-release-authority-decision-dispatch-2026-07-06` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_2026-07-06.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_2026-07-06.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | non-active-handoff central core; archive exception not applicable: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher -> worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`1559f6461`; executionBaseHead=worker-captured start HEAD; closureBaseHead=reviewer-set at closure |
| changedSetScope(phase) | dispatch authoring changes only paired GC-018/work order; worker may create only decision matrix and worker return; reviewer owns closure artifacts; session-sync steward owns session surfaces |
| traceScope(phase, actor) | dispatch trace in this work order; worker trace in worker return; reviewer trace in completion review; session-sync trace in active handoff if next move changes |
| commitOwner(phase) | dispatcher owns dispatch commit; worker must not commit; reviewer/closer owns material closure commit; session-sync steward owns session-sync commit |
| crossBatchIsolation | do not mix with implementation, file-backed invocation, production Memory/RAG release, private-output policy, public-sync, or session-sync |
| nextMoveSurfaces | reviewer/session-sync steward updates only after accepted reviewer closure decision changes current mode or next allowed move |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-06.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-06.md`
- this work order status and closure package if accepted

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver query:

`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

Returned defects:

- ADIF-0001
- ADIF-0002
- ADIF-0014
- ADIF-0015
- ADIF-0020
- ADIF-0021
- ADIF-0007
- ADIF-0016
- ADIF-0017
- ADIF-0024
- ADIF-0006

Disclosed defectIds:

- ADIF-0001
- ADIF-0002
- ADIF-0014
- ADIF-0015
- ADIF-0020
- ADIF-0021
- ADIF-0007
- ADIF-0016
- ADIF-0017
- ADIF-0024
- ADIF-0006

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dispatch Prompt Envelope; Source Verification Block; ADIF Defect Registry Disclosure; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Planned Worker Fulfillment Manifest; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation evidence before dispatch; gates confirm packet shape after source and checker read-ahead |
| claimBoundary | checker read-ahead evidence only; no private-output read, production Memory/RAG release, retrieval, vectorization, file-backed production persistence, public-sync, worker commit, push, or public claim |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | N/A with reason: R41-T1 is not absorbing external knowledge; it is dispatching a docs-only authority decision over current CVF-owned source and governed artifacts |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired GC-018 baseline |
| Disposition | DEFERRED_EXTERNAL_ABSORPTION_NOT_IN_SCOPE |
| Claim boundary | No external knowledge is promoted to CVF authority |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | Docs-only authority decision for MinerU file-backed persistence release |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, production route release, memory-store write, RAG, provider behavior, or public runtime behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatcher authored docs-only dispatch artifacts and did not execute runtime action |
| invocationBoundary | no file-backed persistence invocation, MinerU runtime, private-output read, provider/live proof, public-sync, retrieval, vectorization, or production Memory/RAG route invocation occurs in this dispatch |
| interceptionBoundary | no direct interception, mandatory wrapper, provider routing, or runtime enforcement is claimed |
| claimLanguage | bounded authority-decision dispatch language only: decide, hold, release-to-narrow-packet, or stop |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router/use-case/private-output/production behavior is executed or authorized beyond this docs-only dispatch |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| storageChangeScope | N/A with reason: no docs/reference foundation file, generated aggregate, index, split, relocation, or refactor is authorized |
| durableFoundationFiles | N/A with reason: this packet creates only a work order, paired baseline, one decision matrix, and one worker return |
| indexOrFrontDoorImpact | N/A with reason: no foundation index or front-door update is authorized in worker scope |
| rotationOrSplitPlan | N/A with reason: no touched file is a foundation file requiring rotation or split |
| claimBoundary | Foundation storage layout block is present for guard compatibility only; no durable foundation storage change is authorized |

## Worker Output Quality Controls

| Control | Requirement |
| --- | --- |
| Final rerun | Rerun worker-return fast gate and pre-implementation gate after final edits |
| Static diagnostics | Disclose any observed Pylance, TypeScript, markdown, or governance diagnostic in touched paths |
| Provider-local hygiene | Do not leave `.qwen`, IDE side-channel, or provider-local config files; disclose final status with untracked files |
| Negative edge cases | Decision matrix must explicitly reject interpreting file-backed source existence as release authority |
| Path-literal discipline | Avoid unnecessary literal source paths in review prose beyond required evidence tables |

## Acceptance Criteria

| ID | Criterion | Evidence |
| --- | --- | --- |
| AC1 | Decision matrix exists at the allowed path | git status and file path |
| AC2 | Worker return exists at the allowed path | git status and file path |
| AC3 | Matrix selects exactly one R41-T1 disposition token | decision matrix |
| AC4 | Decision is source-verified against current durable store and route candidate source | Source Verification Block |
| AC5 | Decision distinguishes file-backed source existence from release authority | matrix findings and claim boundary |
| AC6 | No forbidden runtime/private/public/provider/use-case scope is crossed | worker return claim boundary and final status |
| AC7 | Worker honors WORKER_MUST_NOT_COMMIT | final git status and no-commit statement |

## Evidence Requirements

| Evidence item | Required disposition |
| --- | --- |
| Execution base | Worker records `git rev-parse --short HEAD` at start |
| Source anchors | Worker recomputes anchors for durable-memory store, Memory/RAG route, system-chain route, R38/R39/R40 evidence, and current next move |
| Decision matrix | Worker records selected disposition and non-selected alternatives |
| Worktree status | Worker records final `git status --short --untracked-files=all` |
| Scope boundary | Worker records no source/test edit, no private-output read, no MinerU runtime, no file-backed invocation, no production release, no public-sync, and no worker commit |

## Review Gate

Reviewer must verify that the allowed changed set is limited to the decision
matrix and worker return, all source facts are recomputed from current files,
the selected disposition is one of the three allowed R41-T1 tokens, no file-
backed persistence invocation occurred, and the worker did not commit.

## Closure Checklist

- [x] Work order includes Source Verification Block.
- [x] Work order includes ADIF Defect Registry Disclosure.
- [x] Work order includes Agent Handoff Contract Control Block.
- [x] Work order includes Reviewer Closure Conversion.
- [x] Work order includes External Knowledge Intake Routing.
- [x] Work order includes Delta Execution Claim Boundary Control Block.
- [x] Work order includes Foundation Storage Layout Block.
- [x] Work order includes Scaffold Provenance Block.
- [x] Work order includes Public Export Disposition and Claim Boundary.

## Fail Conditions

- Source facts cannot be verified from current source or accepted governed artifacts.
- Decision matrix selects more than one disposition or no disposition.
- Worker edits source/tests or generated state.
- Worker invokes file-backed persistence, MinerU runtime, production Memory/RAG, retrieval, vectorization, provider/live proof, public-sync, or push.
- Worker reads, quotes, summarizes, copies, imports, stages, or commits private/generated MinerU output content.
- Worker claims production readiness, hosted readiness, public readiness, extraction accuracy, document truth, legal quality, current-law correctness, or use-case/legal workflow readiness.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: R41-T1 is a private provenance authority-decision packet. It does
not update public catalog content or make a public product-readiness claim.

## Claim Boundary

This work order authorizes only a docs-only source-verified decision on
MinerU file-backed persistence release authority. It does not authorize
MinerU runtime execution, private/generated output content reads, production
Memory/RAG route release, production durable-store invocation, file-backed
production persistence, retrieval, vectorization, public-sync, use-case/legal
workflow, extraction-truth claims, current-law claims, public readiness,
production readiness, worker commit, or push.
