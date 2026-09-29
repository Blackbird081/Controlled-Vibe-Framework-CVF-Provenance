# CVF Agent Work Order - MSEA R44 T1 MinerU File Backed Persistence Release Recheck Or Stop

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

rawMemoryReleased=false

Batch ID: MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP

Dispatch base head: baf6f098a

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: Codex reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_WORKER_RETURN_2026-07-06.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_2026-07-06.md`

Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_2026-07-06.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-06.

Do-not-misread notes: this packet authorizes a docs-only/source-verified release recheck or stop decision. It does not authorize runtime, private-output read, real file-backed persistence invocation, source/test edit, production Memory/RAG route release, provider/live proof, public-sync, worker commit, push, or use-case/legal workflow.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, the R43-T2 worker return, the current source/test files named in the Source Verification Block, and all checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create the decision matrix and worker return artifact, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Produce a source-verified decision on whether the MinerU file-backed persistence lane can now move from held authority to a future narrow invocation implementation packet, based on R43-T2 actor-role authority wiring and current source evidence. The worker must distinguish "ready to author a narrow invocation packet" from "runtime invocation is already released"; R44-T1 can only decide the next authorized packet, not run or wire persistence itself.

## Authority Chain

| Authority source | Role in this dispatch |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | Current front-door continuity and next-move context |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Canonical active mode, active handoff, and session state |
| `AGENT_HANDOFF_V37_2026-07-06.md` | Active handoff named by the state registry |
| `docs/reference/guard_orientation/README.md` | Guard routing for governed dispatch and worker execution |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Literal-format guardrails for artifact authoring |
| `docs/reviews/CVF_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` | Accepted predecessor evidence for actor-role authority wiring |
| Current source files named in Source Verification Block | Runtime/source evidence for release recheck |

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | Author GC-018 baseline and work order | May commit dispatch artifacts if gates pass |
| Worker | Create R44-T1 decision matrix and worker return only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | Review worker return, run closure gates, decide acceptance, and own any material/session-sync commits | Reviewer-owned |
| Operator | Owns policy checkpoints and any future release decision beyond this packet | N/A |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP --title "MSEA R44 T1 MinerU File Backed Persistence Release Recheck Or Stop" --date 2026-07-06 --base baf6f098a --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled R44-T1 purpose, dependency evidence, source verification, ADIF disclosure, handoff control, required artifact manifest, decision options, and claim boundaries |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| docOnlyNewFields | R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_READY_FOR_NARROW_INVOCATION_PACKET; R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_HELD_PENDING_REMAINING_AUTHORITY_GAPS; R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_REJECTED_STOP |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the literal required shape. Worker should return to orchestrator only for a source contradiction, forbidden-scope need, or missing authority that makes completion impossible.

## Dependency Release Evidence

| Dependency | Required evidence | Refreshed evidence | Disposition |
| --- | --- | --- | --- |
| R43-T2 actor-role authority implementation | Accepted material closure before R44-T1 release recheck | R43-T2 worker return records `ACCEPTED_FOR_MATERIAL_COMMIT` at `docs/reviews/CVF_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md`; material closure commit `db2599f49`; session sync commit `baf6f098a` | SATISFIED |
| Operator policy clarification | R44-T1 must preserve that CVF controls evidence and route-boundary authority, not agent internal operation | R43-T2 worker return records route-boundary authority/evidence/traceability language and forbids agent-operation intervention claims | SATISFIED |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap or predecessor decision | Required next action | R44-T1 handling |
| --- | --- | --- |
| R41-T1 held file-backed persistence release pending authority gaps | Recheck release only after a fresh authority source exists | R43-T2 supplied actor-role authority wiring, so R44-T1 rechecks the lane source-verified |
| R43-T1 selected Option B for actor-role authority wiring design | Use implementation evidence before deciding whether to widen invocation | R44-T1 reads accepted R43-T2 implementation evidence and current source |
| Operator instruction to avoid latching onto use-case/legal workflow | Keep system-chain foundation decision bounded | R44-T1 forbids use-case/legal workflow and public/production claims |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 11 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006 |
| Dispatch impact | Packet uses exact source verification rows, explicit no-commit ownership, checker read-ahead, dependency release evidence, no provider-local authority, and bounded decision language |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Source Verification Block; ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; WORKER_MUST_NOT_COMMIT; DISPATCH_READY; ACCEPT; VALUE_SET; EXISTS; DOC_ONLY_NEW; N/A with reason |
| gateRunPurpose | Confirmation after source-read authoring; gate runs are not the first discovery pass for packet shape |
| claimBoundary | Read-ahead covers dispatch artifact shape and required control blocks only; it does not prove runtime behavior or release readiness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R43-T2 accepted worker return records actor-role authority wiring and reviewer acceptance | VALUE_SET | `docs/reviews/CVF_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` | lines 27 and 137 | `ACCEPTED_FOR_MATERIAL_COMMIT` | R43-T2 worker return | ACCEPT |
| R43-T2 worker return preserves no-production-release and no-real-persistence-invocation boundaries | VALUE_SET | `docs/reviews/CVF_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` | lines 199 and 218 | `file-backed persistence invocation` | R43-T2 worker return claim boundary | ACCEPT |
| Route candidate imports the runtime actor-role type | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 15 | `RuntimeMemoryActorRole` | MinerU system-chain route candidate | ACCEPT |
| Route candidate defines a dedicated actor-role fail-closed token | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 35-36 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_ACTOR_ROLE_NOT_AUTHORIZED` | MinerU system-chain route candidate | ACCEPT |
| Route candidate defines a file-backed persistence actor-role allowlist | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 44 | `FILE_BACKED_PERSISTENCE_ACTOR_ROLE_ALLOWLIST` | MinerU system-chain route candidate | ACCEPT |
| Route authority contains explicit file-backed request and actor-role fields | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 52-60 | `fileBackedPersistenceRequested`; `fileBackedPersistenceActorRole` | `MineruSystemChainRouteAuthority` | ACCEPT |
| Current persistence mode type remains restricted to in-process-only | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 46 | `MineruSystemChainPersistenceMode` | MinerU system-chain route candidate | ACCEPT |
| Current route still fails closed when file-backed persistence is requested after actor-role authorization | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 125-142 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | `evaluateMineruSystemChainRouteCandidate` | ACCEPT |
| Current result paths keep production route unauthorized | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 179 and 191 | `productionRouteAuthorized` | MinerU system-chain route candidate result | ACCEPT |
| R43-T2 tests prove authorized OPERATOR and GOVERNOR still hit the bounded cap | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | lines 249-285 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | MinerU system-chain route candidate tests | ACCEPT |
| R43-T2 tests prove missing and unauthorized roles fail the actor-role gate | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | lines 292-358 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_ACTOR_ROLE_NOT_AUTHORIZED` | MinerU system-chain route candidate tests | ACCEPT |
| Durable memory store has a file-backed store constructor but receipt invariants keep raw release false | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 47-48 and 106-110 | `createFileBackedDurableMemoryStore`; `rawMemoryReleased` | Durable memory store | ACCEPT |
| Runtime actor role vocabulary includes OPERATOR and GOVERNOR | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 12-14 | `RuntimeMemoryActorRole` | Runtime memory hierarchy | ACCEPT |

## New Doc-Only Fields

| Field | Owner artifact | Purpose | Runtime/source status |
| --- | --- | --- | --- |
| `R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_READY_FOR_NARROW_INVOCATION_PACKET` | R44-T1 decision matrix | Decision token for authorizing a future narrow invocation packet | DOC_ONLY_NEW |
| `R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_HELD_PENDING_REMAINING_AUTHORITY_GAPS` | R44-T1 decision matrix | Decision token for holding the lane with named remaining gaps | DOC_ONLY_NEW |
| `R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_REJECTED_STOP` | R44-T1 decision matrix | Decision token for stopping this lane until a new operator checkpoint | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R44-T1 baseline before authoring | `Test-Path docs/baselines/CVF_GC018_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_2026-07-06.md` returned `False` before authoring | ACCEPT |
| Path existence for R44-T1 work order before authoring | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_2026-07-06.md` returned `False` before authoring | ACCEPT |
| Token search before authoring | `rg -n "MSEA-R44-T1|MSEA_R44_T1|CVF_MSEA_R44_T1" docs CVF_SESSION EXTENSIONS` returned no matches before authoring | ACCEPT |
| Collision decision | No existing R44-T1 packet or output path was present | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated worker performs docs-only source-verified decision; reviewer/closer owns acceptance, commits, and session sync |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=baf6f098a; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker may create only the two R44-T1 worker-owned artifacts listed in Work-Order Fulfillment Manifest |
| traceScope(phase, actor) | Worker return must include Agent Operation Trace Block with before/after status, diff evidence, manifest match, and no-commit evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | R44-T1 must not modify R43 artifacts, source/test files, session state, public-sync files, provider-local files, or unrelated roadmap files |
| nextMoveSurfaces | Worker does not update next-move surfaces; reviewer/closer owns any accepted session state and handoff updates |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_COMPLETION_2026-07-06.md` |
| reviewerOwnedClosurePaths | completion review if needed; active session state source fragments; generated active session state; active handoff; session memory front door |
| closureOwner | Codex reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| routeMode | SINGLE_AGENT_SINGLE_ROLE |
| intakeSummary | User request asks to create the next work order after R43-T2; R44-T1 is an internal CVF release recheck using current source and accepted R43-T2 evidence. |
| scopeClassification | Bounded docs-only authority decision; worker may create only the R44-T1 decision matrix and worker return. |
| riskSensitivity | Medium governance risk because the packet concerns memory/persistence authority, but no runtime, provider/live, private-output, public-sync, or source/test edit is allowed. |
| selectedRoleRoute | routeMode SINGLE_AGENT_SINGLE_ROLE; delegated worker creates docs-only outputs and reviewer/closer owns acceptance and commits. |
| roleSeparationBasis | Worker must not commit; reviewer/closer owns closure decision and any session-sync. |
| dispatcherRole | dispatcher role |
| workerRole | delegated worker |
| reviewerRole | reviewer/closer role |
| authorityCheckpoint | SATISFIED: R43-T2 actor-role authority implementation is accepted and current source preserves the bounded cap. |
| escalationCondition | Stop and return BLOCKED if completion needs source/test edits, runtime invocation, durable-store write, live/provider proof, private output, public-sync, production release, use-case/legal workflow, or agent-operation intervention. |
| claimBoundary | Role routing only; no external knowledge intake, provider-specific assignment, provider-local authority, live provider behavior, public-sync, or agent-operation intervention claim. |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: R44-T1 uses only CVF-governed source files and accepted CVF review artifacts |
| Matching local-view guard | N/A with reason: no external knowledge intake event occurred |
| Owner surface | This work order and paired GC-018 baseline |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external source is promoted to CVF authority |
| Claim boundary | This section is routing evidence only and does not authorize outside-source absorption |

## Required First Reads

| Required read | Purpose |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | Session front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Compact state read |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Canonical current mode and handoff routing |
| active handoff named by the state registry | Current governed continuity |
| `docs/reference/guard_orientation/README.md` | Guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Literal-format failure prevention |
| this work order and paired GC-018 baseline | Dispatch authority |
| `docs/reviews/CVF_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` | Accepted predecessor implementation evidence |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | Current route candidate source |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | Current route candidate tests |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | Durable store and receipt evidence |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | Actor role source vocabulary |
| checker files listed in Checker Source Read-Ahead Block | Output-shape authority |

## Allowed Scope

- Create `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md`.
- Create `docs/reviews/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_WORKER_RETURN_2026-07-06.md`.
- Read source and governed artifacts needed to verify the Source Verification Block.
- Run docs/governance gates required by this work order.
- Decide exactly one R44-T1 disposition token from the Decision Options section.

## Forbidden Scope

- Do not edit source files, tests, runtime files, hook wiring, session state, handoffs, public-sync files, provider-local files, or unrelated docs.
- Do not run MinerU runtime, read private/generated MinerU output, invoke real file-backed persistence, write durable memory records, or run provider/live proof.
- Do not widen `MineruSystemChainPersistenceMode`, remove `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED`, or alter the actor-role allowlist.
- Do not claim production Memory/RAG release, production readiness, extraction accuracy, document truth, legal quality, current-law correctness, workflow-chain production readiness, public export, or hosted release.
- Do not enter use-case/legal workflow design.
- Do not commit, push, stage unrelated files, or leave provider-local stray files such as `.qwen/settings.json`.

## Pre-Flight Checks

| Check | Required worker evidence |
| --- | --- |
| Execution base | Record `git rev-parse --short HEAD` before writing |
| Clean worktree | Record `git status --short --untracked-files=all` before writing |
| Required reads | List read-first artifacts and source files actually read |
| Scope confirmation | Confirm only the two worker-owned output paths are created |
| Provider-local hygiene | Confirm no provider-local stray files or IDE config changes were created |

## Write Ownership

| Path | Worker permission | Notes |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md` | CREATE | Worker-owned decision matrix |
| `docs/reviews/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_WORKER_RETURN_2026-07-06.md` | CREATE | Worker-owned return packet |
| Any other path | FORBIDDEN | Return `BLOCKED_WITH_REASON` if completion requires another path |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| `docs/reviews/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_WORKER_RETURN_2026-07-06.md` | Derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, no-commit evidence shape, and public disposition shape before writing |
| `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md` | Derive exact reference headings, source verification labels, decision/disposition language, trace language, and claim-boundary labels before writing |

Literal-shape reminders: when listing required worker-output sections, write section names without the `##` prefix. Reserve actual heading syntax for real sections so structural checkers do not treat checklist text as artifact body.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md` | Create source-verified decision matrix with one selected disposition token and named evidence for release/hold/stop |
| `docs/reviews/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_WORKER_RETURN_2026-07-06.md` | Create worker return with source inventory, findings, command evidence, no-commit statement, and exact changed-set manifest |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| foundationStorageChange | N/A with reason: R44-T1 does not create, split, relocate, refactor, or modify durable governance foundation storage files |
| durableStoreRuntimeChange | FORBIDDEN: no durable-store write, file-backed invocation, or persistence-mode widening is authorized |
| indexOrCatalogChange | N/A with reason: no index, catalog, public-sync, or storage-layout update is authorized |
| claimBoundary | The packet references durable memory source evidence only for release authority recheck; it does not change storage layout |

## Decision Options

| Disposition token | Meaning |
| --- | --- |
| `R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_READY_FOR_NARROW_INVOCATION_PACKET` | Current evidence is sufficient to authorize a future source/test implementation packet that deliberately widens the route candidate enough to invoke file-backed persistence under the existing actor-role authority gate |
| `R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_HELD_PENDING_REMAINING_AUTHORITY_GAPS` | The lane remains held because named authority gaps remain after R43-T2, and the worker must name those gaps precisely |
| `R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_REJECTED_STOP` | The file-backed persistence lane is not worth continuing now and should be stopped until a new operator checkpoint reopens it |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_WORKER_RETURN_2026-07-06.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section names without the `##` prefix. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git status --short --untracked-files=all
```

Worker must record exact command outcomes in the worker return. If pre-implementation fails only because of dispatcher-owned artifacts outside worker Write Ownership, record the exact failure and return for reviewer/closer decision instead of editing forbidden paths.

## Execution Plan

1. Capture execution base and clean worktree evidence.
2. Read the mandatory startup, guard, dispatch, predecessor, source, and checker files.
3. Create the R44-T1 decision matrix using the Source Verification Block and New Doc-Only Fields table.
4. Select exactly one disposition token and explain release/hold/stop consequences.
5. Create the worker return with source inventory, command evidence, trace evidence, delta boundary, public disposition, and no-commit statement.
6. Run required gates and record exact outcomes.
7. Leave changes uncommitted and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| Source verification | Table rows citing source file, line or section, symbol, owning interface/function/schema, claim type, and disposition |
| Decision evidence | One selected R44-T1 disposition token with consequence explanation |
| Command evidence | Exact command names and pass/fail summaries |
| Changed-set evidence | `git diff --name-status` plus `git status --short --untracked-files=all` |
| No-commit evidence | Explicit statement that worker did not commit, stage unrelated files, push, or public-sync |
| Claim boundary | Explicit no-runtime, no-private-output, no-real-persistence, no-production-release, no-public claim boundary |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated worker role |
| Provider or surface | local workspace |
| Session or invocation | MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP worker execution, 2026-07-06 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | File read/edit tools; `git rev-parse`; `git status`; `git diff --name-status`; required Python gates |
| Target paths | `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md`; `docs/reviews/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_WORKER_RETURN_2026-07-06.md` |
| Allowed scope source | This work order Write Ownership and Work-Order Fulfillment Manifest |
| Before status evidence | clean worktree: `git rev-parse --short HEAD` returned `baf6f098a`; `git status --short --untracked-files=all` was empty before authoring. |
| After status evidence | Worker must capture `git status --short --untracked-files=all` after writing |
| Diff evidence | `git diff --name-status` |
| Approval boundary | Operator-approved R44-T1 dispatch only |
| Claim boundary | Docs-only release recheck or stop decision; no runtime, source/test edit, or production release claim |
| Agent type | worker |
| Invocation ID | `msea_r44_t1_mineru_file_backed_persistence_release_recheck_or_stop-2026-07-06` |
| Expected manifest | The two worker-owned artifacts listed in Work-Order Fulfillment Manifest |
| Actual changed set | Worker must list actual changed paths |
| Manifest delta | MATCH or describe mismatch and return blocked |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R44-T1 docs-only file-backed persistence release recheck or stop decision |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed by this dispatch |
| receiptEvidence | N/A with reason: no runtime or persistence receipt is authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT: governed artifact creation and command evidence only |
| invocationBoundary | No MinerU runtime, durable-store write, provider/live call, private-output read, or file-backed persistence invocation |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | CVF records route-boundary authority, evidence, and traceability; it does not intervene in or direct agent internal operation |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without a fresh source-verified authorization |

## Acceptance Criteria

- Decision matrix selects exactly one R44-T1 disposition token.
- Decision matrix explains whether R43-T2 actor-role authority closes the previously named authority gap and names any remaining gap.
- Decision matrix clearly separates "future narrow invocation packet may be authored" from "runtime invocation is already released".
- Worker return includes source inventory, source verification, findings, risk/corrective action, decision/disposition, trace block, delta claim boundary, public disposition, command evidence, and no-commit evidence.
- Worker changed set matches Work-Order Fulfillment Manifest.
- Required gates are run and outcomes are recorded.

## Fail Conditions

- Worker edits any source/test/runtime/session/public/provider-local path.
- Worker runs runtime, private-output read, real persistence invocation, durable-store write, provider/live proof, public-sync, or use-case/legal workflow.
- Worker claims production Memory/RAG release or production readiness.
- Worker uses provider-local memory as canonical source authority.
- Worker omits source verification, ADIF disclosure, trace evidence, or no-commit evidence.
- Worker leaves stray provider-local files or IDE/provider config changes.

## Review Gate

Reviewer/closer must verify the worker changed set, run the worker-return fast gate, run the relevant autorun gate on the proper execution range, and decide whether to accept, repair within reviewer-owned paths, or return blocked. Reviewer/closer owns any material commit and session-sync commit.

## Closure Checklist

| Item | Required closure handling |
| --- | --- |
| Worker changed-set manifest | Must match Work-Order Fulfillment Manifest or return blocked |
| Worker return fast gate | Must pass or cite reviewer-owned repair |
| Autorun gate | Must run on proper execution range and be dispositioned |
| Commit ownership | Worker must not commit; reviewer/closer owns accepted material commit |
| Session sync | Reviewer/closer updates next-move surfaces only after acceptance |
| Public export | Must remain private-only unless a future public-sync packet authorizes export |

## Operator Checkpoint

| Field | Value |
| --- | --- |
| Current checkpoint | Operator approved creation of this R44-T1 work order |
| Worker checkpoint need | N/A with reason: worker can complete the docs-only decision within the authorized scope |
| Future checkpoint | Required before any real file-backed persistence invocation, source/test implementation, provider/live proof, production Memory/RAG release, public-sync, or use-case/legal workflow |

## Claim Boundary

This work order authorizes only a docs-only, source-verified release recheck and worker return. It does not authorize source/test edits, persistence-mode widening, MinerU runtime execution, private/generated output reads, real file-backed persistence invocation, durable-store writes, production Memory/RAG route release, retrieval, vectorization, provider/live proof, Web/UI work, public-sync, use-case/legal workflow, extraction accuracy claims, document truth claims, legal quality claims, current-law correctness claims, workflow-chain production readiness claims, worker commit, push, or public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance work order for bounded release authority recheck. No public-sync artifact, public catalog update, public remote proof, or exported public path is authorized by this packet.
