# CVF GC-018 Baseline - MAO-T1 Task Graph And State Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-07-11

Batch ID: MAO-T1-DISPATCH

dispatchBaseHead: `329f4a985`

executionBaseHead: `c1089bf2a`

closureBaseHead: `c1089bf2a`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Authorize a bounded MAO-T1 implementation of the task graph, immutable authority
binding, append-only state/event ledger, deterministic read model, and focused
tests under a dedicated execution-plane module. No provider, queue, scheduler,
UI, public, or role-resolver implementation is authorized.

## Scope / Target / Owner Boundary

The execution plane owns task-graph/state mechanics. A future control-plane
resolver owns admission policy. AHB remains authority for route/closer/commit;
workspace generated state remains projection only. Root execution-plane index
and monolithic root tests are read-only in this tranche.

## Decision / Baseline / Proposed Tranche

Implement MAO-T1 in a dedicated `src/mao/` module with dedicated tests. Do not
wire the root barrel, provider router, workspace state, queue, or runtime caller.
This produces an internally testable foundation, not a production invocation.

## Evidence / Verification

Evidence requires focused TypeScript tests, package typecheck, deterministic
replay comparison, table-driven corruption/transition negatives, exact six-path
manifest, workspace runtime-boundary pass, file-size pass, worker-return fast
gate, and autorun on the real execution range.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T0 closure | `docs/reviews/CVF_MAO_T0_SOURCE_INVENTORY_ARCHITECTURE_DECISIONS_AND_SCHEMAS_COMPLETION_2026-07-11.md`; commit `dbe963b03` | reviewer accepted T0 contract/schema foundation | SATISFIED |
| Protected closure sync | commit `329f4a985`; mode `mao_t0_closed` | active next move must release T1 packet authoring | SATISFIED |
| Runtime schema authority | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json` | valid Draft 2020-12 schema | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T1-DISPATCH --title "MAO-T1 Task Graph And State Contract" --date 2026-07-11 --base 329f4a985 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all placeholders with source-backed T1 scope, paths, controls, and evidence |
| checkerReadAheadConfirmation | dispatch-quality, AHB, workspace, runtime-boundary, file-size, ADIF, and foundation-layout checkers read |
| docOnlyNewFields | none; implementation consumes T0 schema vocabulary |
| claimBoundary | dispatch authoring only; no runtime behavior proven |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| MAO task/event/read-model schema | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json` | definitions and root properties | `taskGraph`, `eventLedgerEntry`, `maoReadModel` | T0 JSON Schema | ACCEPT |
| lifecycle and propagation semantics | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Task Lifecycle and Terminal Outcome Propagation | task state transition tables | MAO contract | ACCEPT |
| existing coordination module is shallow historical overlap | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/execution.multi.agent.coordination.contract.ts` | class definition | `MultiAgentCoordinationContract` | execution plane | ACCEPT |
| execution plane root index exports W2-T9 contracts | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | W2-T9 export block, lines 399-421 | `MultiAgentCoordinationContract` | execution-plane root barrel | ACCEPT |
| root index and root test are large governed files | VALUE_SET | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | registered exceptions | execution-plane root index/test paths | file-size guard | ACCEPT |
| workspace state is projection, not task execution truth | LITERAL_INVARIANT | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | Topology Decision | `ACTIVE_AGENT_WORKSPACE_STATE.json` | workspace topology | ACCEPT |

## Current Runtime Freshness Verification

Verified at `329f4a985`: T0 contract/schema exist; historical coordination source
and W2-T9 root exports exist; no `src/mao/` implementation path exists; workspace
runtime boundary remains queue-skeleton/read-model only.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-contract`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class runtime-contract --role dispatcher --lifecycle-phase pre-dispatch --surface-selector multi_agent_orchestration --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Disclosed defectIds | N/A with reason: NONE_RETURNED |
| Dispatch impact | retain T0 threat/failure caveats and require negative tests |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/check_agent_workspace_runtime_boundary.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; source verification; AHB control; workspace design; runtime expansion; worker return profile |
| gateRunPurpose | confirmation and evidence after source-backed packet authoring; not first discovery |
| claimBoundary | packet shape and source fidelity only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

Intake summary: bounded execution-plane task-graph/state foundation.

Scope classification: RUNTIME_FOUNDATION_LOCAL_NO_INTEGRATION.

Risk sensitivity: HIGH because state transitions and authority hashes become
load-bearing for later orchestration.

Escalation condition: source/schema contradiction, required root-barrel change,
forbidden integration need, or inability to preserve deterministic semantics.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime-foundation dispatch. Any later public work
requires a separate packet in the sibling public-sync clone.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired work order | CLOSED_PASS_BOUNDED | PASS |
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

This baseline authorizes only MAO-T1 local task-graph/state foundation source,
tests, and worker return. It does not authorize provider/live behavior, role
resolver, delegation adapter, queue/scheduler, root-barrel integration, UI,
workspace/session state, public-sync, ASC admission, or production readiness.
