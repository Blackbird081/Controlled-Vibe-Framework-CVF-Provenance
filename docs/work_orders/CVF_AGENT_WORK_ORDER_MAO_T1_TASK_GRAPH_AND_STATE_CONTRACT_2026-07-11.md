# CVF Agent Work Order - MAO-T1 Task Graph And State Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-07-11

Batch ID: MAO-T1-DISPATCH

dispatchBaseHead: `329f4a985`

executionBaseHead: `c1089bf2a`

closureBaseHead: `c1089bf2a`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: independent reviewer

## Dispatch Prompt Envelope

Role: delegated worker for MAO-T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T1_TASK_GRAPH_AND_STATE_CONTRACT_2026-07-11.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture actual clean HEAD at start.

Current-time notes: artifact date is 2026-07-11.

Do-not-misread notes: local task-graph/state implementation only; no provider,
resolver, adapter, queue, UI, public, workspace/session, or root-barrel work.

Required first actions: startup reads; capture HEAD/status; read paired baseline,
T0 front door/contract/schema/inventory, checker sources, existing execution
coordination source, and local package/test conventions before editing.

Return contract: produce the exact fulfillment manifest, run required tests and
gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Implement and test the deterministic MAO task graph, immutable authority
binding, append-only event/state ledger, terminal propagation, and generated
read model specified by MAO-T0.

## Authority Chain

1. `AGENTS.md` and active session front doors.
2. Paired GC-018 and this work order.
3. MAO roadmap and accepted T0 completion review.
4. MAO reference front door, contract, schema, and inventory.
5. Active AHB/workspace contracts.
6. Existing execution-plane source only for verified conventions.

## Agent Roles

- delegated worker: implement, test, document evidence, return without commit;
- independent reviewer/designated closer: recompute evidence, repair or reject,
  author completion review, and own accepted material commit;
- session-sync steward: separate phase after material closure.

## Scope / Target / Owner Boundary

### Allowed worker paths

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.task.graph.state.contract.test.ts`
- `docs/reviews/CVF_MAO_T1_TASK_GRAPH_AND_STATE_CONTRACT_WORKER_RETURN_2026-07-11.md`

### Forbidden paths and behavior

No root `src/index.ts`, root `tests/index.test.ts`, historical coordination
source, provider router, role resolver, adapter, queue, scheduler, Web/UI,
workspace state, session state, checker/hook/CI, roadmap, registry, public-sync,
ASC/R91, L4, R84, or R73F change. No provider call or subagent spawn.

## Write Ownership

Exactly six worker paths. Any seventh path or required root export returns to
orchestrator. Worker must not commit.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| MAO-T0 contract/schema closure | completion review at commit `dbe963b03` | SATISFIED |
| T0 closure continuity | state/handoff sync `329f4a985` | SATISFIED |
| Dedicated module layout | planned `src/mao/` paths absent; root monoliths read-only | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T1-DISPATCH --title "MAO-T1 Task Graph And State Contract" --date 2026-07-11 --base 329f4a985 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | all placeholders replaced with source-backed T1 scope and controls |
| checkerReadAheadConfirmation | listed checker sources read before authoring |
| docOnlyNewFields | none; consume T0 schema vocabulary |
| claimBoundary | dispatch provenance only |

## Required First Reads

Mandatory startup files; paired baseline/work order; MAO front door, contract,
schema, inventory, T0 completion; AHB ratification; workspace topology/runtime
expansion contract; existing execution coordination source; execution-plane
package/tsconfig/test conventions; all checker sources in read-ahead block.

## Pre-Flight Checks

Capture actual HEAD and empty `git status --short`; confirm six paths do not
exist; run collision searches; confirm no unrelated worktree batch.

## Worker Autonomy / No-Question Rule

Repair allowed-scope failures directly. Return only for source contradiction,
required forbidden path, missing authority, or architecture choice outside T0.

## Source Verification Block

Use the paired baseline table. Implementation must map every exported type and
transition to T0 schema/contract. No new field or enum may be invented silently;
return `BLOCKED_WITH_REASON` if T0 is insufficient.

## Current Runtime Freshness Verification

Re-run path/symbol searches at execution start. Confirm dedicated `src/mao/`
paths remain absent, historical W2-T9 source is unchanged, root monoliths remain
read-only, and no runtime caller/integration is claimed.

## Negative Search And Collision Discipline

Use `Test-Path` on six outputs and `rg --files --hidden --no-ignore` plus exact
symbol searches for proposed MAO class/type names. Record collisions in return.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-contract`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class runtime-contract --role dispatcher --lifecycle-phase pre-dispatch --surface-selector multi_agent_orchestration --risk-ceiling HIGH --max-results 20 --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/check_agent_workspace_runtime_boundary.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | ready status; no-commit route; source verification; runtime/workspace boundaries; worker return contract; foundation storage |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | dispatch compatibility only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

Intake summary: high-risk local state-machine foundation with independent review.

Scope classification: RUNTIME_FOUNDATION_LOCAL_NO_INTEGRATION.

Risk sensitivity: HIGH.

Escalation condition: schema contradiction, nondeterministic semantics, required
integration/root export, forbidden path, or unbounded state behavior.

## Agent Handoff Contract Control Block

Contract source, active and not archive:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | actual executionBaseHead captured at start |
| changedSetScope(phase) | exactly six allowed worker paths |
| traceScope(phase, actor) | worker execution trace only |
| commitOwner(phase) | nobody in execution; independent closer at closure |
| crossBatchIsolation | one batch; clean worktree required |
| Before status evidence | `git status --short` empty at execution start |
| nextMoveSurfaces | worker must not edit; separate session sync after reviewer acceptance |

## Agent Workspace Design Control Block

Contract sources, active and not archive:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` and
`docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`.

| Field | Value |
|---|---|
| Workspace purpose | MAO execution state only; workspace remains projection |
| Contract source | MAO T0 contract plus active AHB/workspace contracts |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | in-memory deterministic contract for T1 tests; no durable queue |
| Handoff fields | authority hash, route, phase, changed set, trace, commit owner |
| State ownership | MAO event ledger owns local execution truth; workspace state unchanged |
| Guard owner | existing workspace design/runtime-boundary guards |
| Build boundary | dedicated runtime source/tests only; no provider proof, public-sync, registry edits, queue, UI, workspace generated state, or session state |

## Runtime Expansion Control Block

| Field | Value |
|---|---|
| runtimeMode | RUNTIME_IMPLEMENTATION_REQUESTED |
| contractSource | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` |
| frontDoor | `docs/reference/agent_workspace/README.md` |
| requestedScope | dedicated local task-graph/state modules and focused tests |
| forbiddenExpansion | provider/live, queue/scheduler, UI, public-sync, workspace/session state, registry edits |
| evidenceRequired | deterministic unit tests, negative corruption/transition tests, exact changed set |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MAO_T1_TASK_GRAPH_AND_STATE_CONTRACT_COMPLETION_2026-07-11.md`

reviewerOwnedClosurePaths: completion review, baseline/work-order closure
conversion, allowed repairs to the six worker paths, and the minimum GC-051
registry source/aggregate coverage required for the five new execution-plane
source/test paths. Session sync is separate. Registry coverage is reviewer-only
closure metadata; the worker prohibition remains enforced.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap T1 requirement | Required output/evidence |
|---|---|
| deterministic graph compiler/validator | `task.graph.contract.ts` plus tests |
| dependency and parent/child evidence | graph node/edge validation and lineage tests |
| terminal/blocked propagation | state transition implementation and table-driven tests |
| immutable authority binding | authority hash mismatch rejection tests |
| append-only event ledger | ledger contract and mutation/ordering negatives |
| deterministic read model | read-model reducer and replay-equality tests |
| corruption tests | cycle, missing dependency, duplicate ID/event, invalid transition, stale authority tests |

## Work-Order Fulfillment Manifest

Exactly five implementation/test files plus one worker return. No optional path.

## Required Artifact Manifest

| Artifact | Owner | Required disposition |
|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | worker | REQUIRED |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | worker | REQUIRED |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts` | worker | REQUIRED |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | worker | REQUIRED |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.task.graph.state.contract.test.ts` | worker | REQUIRED |
| `docs/reviews/CVF_MAO_T1_TASK_GRAPH_AND_STATE_CONTRACT_WORKER_RETURN_2026-07-11.md` | worker | REQUIRED |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Worker return must record execution base, six-path manifest, commands/results,
test counts, source mapping, dissent, and `WORKER_MUST_NOT_COMMIT` confirmation.

## Execution Plan

1. Map T0 schema types/states to TypeScript without adding vocabulary.
2. Implement immutable graph compile/validate and deterministic identifiers.
3. Implement append-only event ledger and transition/propagation rules.
4. Implement deterministic read-model replay.
5. Add table-driven positive and adversarial tests.
6. Run gates and return uncommitted material.

## Verification Commands

- focused project test command for the dedicated MAO test file;
- TypeScript typecheck using the execution-plane package configuration;
- deterministic replay repeated-run comparison;
- negative tests for cycles, duplicates, missing dependencies, invalid terminal
  transitions, authority mismatch, duplicate event, and out-of-order event;
- `python governance/compat/check_agent_workspace_runtime_boundary.py --enforce`;
- `python governance/compat/check_governed_file_size.py --enforce`;
- `git diff --check`;
- worker-return fast and applicable autorun gate on real range.
- `python governance/compat/run_worker_return_fast_gate.py`.

## Acceptance Criteria

- Six-path manifest matches exactly.
- T0 state/enum/field vocabulary is implemented without silent additions.
- Graph compilation, lineage, cycle/missing dependency, terminal propagation,
  authority binding, append-only ordering, duplicate protection, and deterministic
  replay have positive and negative proof.
- No root barrel/test monolith, provider, resolver, adapter, queue, UI, public,
  workspace/session, checker/hook, registry, roadmap, or catalog change.
- No production invocation or provider-readiness claim.

## Evidence Requirements

Exact commands, test counts, typecheck results, repeated-run hashes or equality,
changed-set proof, and explicit N/A with reason for non-applicable evidence.

## Negative And Fail-Condition Scan

Fail on cycles accepted, missing dependency accepted, duplicate task/event
accepted, invalid terminal transition, authority rewrite, nondeterministic replay,
mutable historical event, provider hardcoding, second execution truth, root
monolith edit, extra path, implicit commit, or production claim.

## Review Gate

Independent reviewer re-runs all focused tests and typecheck, samples transition
semantics against T0, validates exact manifest, and alone accepts/commits.

## Closure Checklist

- [x] Six worker paths reviewed.
- [x] T0 vocabulary mapping verified.
- [x] Positive and negative tests pass.
- [x] Deterministic replay proven.
- [x] No forbidden path or claim.
- [x] Worker-return fast gate passes after reviewer-owned GC-051 coverage.

## Return-To-Orchestrator Conditions

Return for source/schema contradiction, required forbidden path/root export,
unresolved state semantics, or maintainability boundary that cannot be solved
inside the six-path manifest.

## Operator Checkpoint

N/A with reason: operator authorized the next governed work-order step; provider,
public, irreversible, and high-risk external effects remain excluded.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated worker |
| Provider or surface | local private provenance repository |
| Session or invocation | MAO-T1 execution |
| Working directory | repository root |
| Command or tool surface | source edit, local test/typecheck, read-only governance gates |
| Target paths | six allowed paths |
| Allowed scope source | this work order and paired GC-018 |
| Before status evidence | clean worktree; `git status --short` empty at execution start |
| After status evidence | six uncommitted worker outputs |
| Diff evidence | exact name-status and test evidence in worker return |
| Approval boundary | no worker commit; reviewer/closer accepts |
| Claim boundary | local T1 task-graph/state foundation only |
| Agent type | worker |
| Invocation ID | mao-t1-delegated-worker-2026-07-11 |
| Expected manifest | six allowed paths |
| Actual changed set | worker records at return |
| Manifest delta | worker records MATCH or BLOCKED |
| Deletion or rename disposition | N/A with reason: none authorized |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation root | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/` |
| Stable local front door | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` |
| Durable source files | task graph, event ledger, read model contracts |
| Generated aggregate | N/A with reason: T1 read model is runtime output, not committed aggregate |
| Generator/checker | N/A with reason: local TypeScript contracts/tests only |
| Root index update | forbidden; future integration requires separate bounded packet |
| Test location | dedicated MAO test file; root test monolith unchanged |
| Public boundary | provenance only; no public-sync |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime foundation. Any later public export requires
a separate packet and sibling public-sync clone.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | T0 completion review | REVIEWER_ACCEPTED_BOUNDED | PASS |
| Roadmap state | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` | PROPOSED | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | current; no T1 registration required | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | current companion | PASS |
| External evidence digest | T0 critique reconciliation | sha256 `E7392BC13A7F56E8647E94D091B5F76BB8EA3D67ACCF4245EE0E150A5354726D` | PASS |
| System loop interlock | R91/ASC freshness | CURRENT | PASS |
| Session continuity | active front doors | T0 closed, T1 authoring released | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | Evidence field | Required value | Observed value | Status |
|---|---|---|---|---|---|
| MAO-T1-Q1 | T0 completion | verdict | REVIEWER_ACCEPTED_BOUNDED | REVIEWER_ACCEPTED_BOUNDED | PASS |

## Claim Boundary

This work order authorizes one no-commit worker to implement/test the local
MAO-T1 task-graph/state foundation only. It does not authorize provider calls,
role resolver, delegation adapter, queue/scheduler, root integration, UI,
workspace/session state, public-sync, ASC admission, or production readiness.
