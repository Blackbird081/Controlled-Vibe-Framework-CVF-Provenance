# CVF Agent Work Order - LSC-T5/T7 Learning Plane Bridge And Latency Guard

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-21

docType: work_order

dispatchBaseHead: 749dc791

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_FOR_WORKER_2026-06-21.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: LSC-T5/T7 is the next Learning Signal Chain roadmap area
after LSC-T6 closure. The mission is to define bridge alignment from LSC signal
records to existing RT2/RT3 and MLW3/MLW5/MLW6 proposal-only Learning Plane
surfaces, and to define/implement only a narrow read-only helper/test latency
fast-path if required by the contract.

Do-not-misread notes: do not mutate the Learning Plane runtime, edit RT2/RT3
runtime source, create a ledger store, generator, drift checker, durable store,
CLI/MCP adapter, MCP tool, provider route, public-sync artifact, queue/daemon,
watcher, direct-interception wrapper, runtime readiness proof, or public
catalog claim. Do not edit session state, active handoff, root startup routers,
public-sync, `.github/**`, dependency manifests, web UI routes, MCP packages,
or `EXTENSIONS/**`. Do not reopen AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, or
MLW8.

Required first actions: read this work order, read the LSC-T5/T7 GC-018
baseline, read the LSC-T0 roadmap, read the LSC reference front door, read the
LSC-T1/T3/T4/T6 contracts, read the Learning Signal Intake bridge, read RT2
and RT3 source surfaces, read MLW3/5/6 reference contracts, inspect the AAF
helper and focused tests, confirm actual `executionBaseHead`, and inspect
current `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only the required
uncommitted artifacts, actual `executionBaseHead`, actual `git status --short`,
source inventory, scan-depth ledger, gate evidence, and no commit. If blocked,
return `BLOCKED_WITH_REASON` and name the exact source or gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Purpose

Dispatch a bounded LSC-T5/T7 worker task to create the Learning Plane bridge
and latency guard reference contract, update the LSC front door, and optionally
add only a narrow read-only AAF helper/test fast-path if the contract requires
it.

This work order preserves the LSC claim boundary: proposal-only Learning Plane
routing, no autonomous mutation, fast capture, governed promotion, no provider
or public proof, and no actual CLI/MCP adapter behavior.

## Agent Roles

| Role | Owner | Commitment boundary |
|---|---|---|
| Dispatcher | Codex/orchestrator | creates GC-018 baseline and this worker packet |
| Worker | external worker/Claude | edits only Required Deliverables and returns uncommitted |
| Reviewer/closer | Codex/orchestrator after worker return | validates, repairs allowed-scope packet defects, commits accepted material, and performs session sync if needed |
| Operator | human operator | checkpoint only for scope expansion, parked-lane reopening, provider/live/public/runtime work, secrets, or destructive action |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator roadmap order | `LSC-T2 -> LSC-T4 -> LSC-T3 -> LSC-T6 -> LSC-T5/T7` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| LSC-T5/T7 GC-018 baseline | `docs/baselines/CVF_GC018_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_2026-06-21.md` | ACCEPT |
| LSC-T0 roadmap | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | ACCEPT |
| LSC reference front door | `docs/reference/learning_signal_chain/README.md` | ACCEPT |
| LSC-T1/T3/T4/T6 contracts | `docs/reference/learning_signal_chain/` | ACCEPT |
| RT2/RT3 Learning Plane source surfaces | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/finding-to-learning-bridge.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/learning-plane/readout/route.ts` | SOURCE_AUTHORITY |
| MLW3/MLW5/MLW6 reference contracts | `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md`; `docs/reference/CVF_MLW5_AUDIT_FEEDBACK_VALIDATION_LANE_2026-06-05.md`; `docs/reference/CVF_MLW6_SIMULATION_FAILURE_GATE_2026-06-05.md` | ACCEPT |
| AAF helper source and focused tests | `governance/compat/run_agent_automation_assist.py`; `governance/compat/test_run_agent_automation_assist.py` | SOURCE_AUTHORITY_FOR_OPTIONAL_HELPER_SCOPE |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatcher creates packet; worker authors reference/front-door/helper/test/return artifacts; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=749dc791`; `executionBaseHead` confirmed by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending LSC-T5/T7 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix LSC-T5/T7 with AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7/8, runtime/provider/live, MCP adapter behavior, public-sync, queue/daemon, direct-interception, ledger/generator implementation, or Learning Plane runtime mutation |
| Before status evidence | clean worktree at committed dispatch base `749dc791` before LSC-T5/T7 dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_COMPLETION_2026-06-21.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted LSC reference-front-door and LSC-T5/T7 contract updates; accepted AAF helper/test updates if any; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: allow the LSC-T5/T7 worker to update only
the AAF helper and focused helper tests named below if needed to implement a
read-only latency/bridge fast-path. This authorization is limited to
`governance/compat/run_agent_automation_assist.py` and
`governance/compat/test_run_agent_automation_assist.py` and does not authorize
other `governance/compat/**` files, hook wiring, guard registry changes,
runtime Learning Plane mutation, provider/live proof, public-sync, CLI/MCP
adapter behavior, direct interception, queue/daemon, watcher, readiness, cost
optimization, or universal control.

Protected paths:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`
- `docs/baselines/CVF_GC018_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_2026-06-21.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_FOR_WORKER_2026-06-21.md`

Operator authorization: the operator selected the roadmap order
`LSC-T2 -> LSC-T4 -> LSC-T3 -> LSC-T6 -> LSC-T5/T7` and requested continuing
with work-order creation after LSC-T6 closure.

Rollback boundary: revert only the eventual LSC-T5/T7 worker/reviewer material
commit if rejected. Do not revert LSC-T6 closure commit `65af6db3`,
continuity commit `749dc791`, or earlier LSC closure commits.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator roadmap order, LSC-T0 roadmap, closed LSC-T1/T3/T4/T6 reference contracts, RT2/RT3 source, MLW3/5/6 contracts |
| Intake role | worker authors bounded bridge/latency reference contract and optional read-only helper/test fast-path |
| Reviewer role | reviewer/closer validates source fidelity, claim boundary, gate evidence, and commit eligibility |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; bridge-alignment plus latency-guard reference/helper work |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if runtime Learning Plane mutation, RT2/RT3 runtime edits, MCP/provider/live/public-sync/session-sync/parked-lane expansion is required |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | LSC-T5/T7 is derived from the current LSC roadmap and accepted LSC reference contracts, not a raw `.private_reference/legacy` corpus scan or LHW wave. |
| Coverage evidence used instead | LSC-T0 roadmap, LSC reference front door, LSC-T1/T3/T4/T6 contracts, RT2/RT3 source surfaces, MLW3/5/6 contracts, and AAF helper signal readout source. |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and role-neutrality rule |
| `docs/baselines/CVF_GC018_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_2026-06-21.md` | GC-018 authorization and claim boundary |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_FOR_WORKER_2026-06-21.md` | current work order and packet shape |
| `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | LSC roadmap, LSC-T5/T7 rows, design-control gate |
| `docs/reference/learning_signal_chain/README.md` | LSC reference front door to update |
| `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | intake ownership and de-dup/root-cause policy |
| `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md` | current helper readout shape and future LSC-T7 relationship |
| `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | promotion outcomes, blocker rules, LSC-T5/T7 relationship |
| `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | external signal IO and no-runtime latency boundary |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | intake fields and autonomous mutation invariant |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/finding-to-learning-bridge.ts` | RT2 bridge source shape |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/learning-plane/readout/route.ts` | RT3 readout route source shape |
| `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md` | proposal-only learning signal pipeline |
| `docs/reference/CVF_MLW5_AUDIT_FEEDBACK_VALIDATION_LANE_2026-06-05.md` | audit-feedback validation lane |
| `docs/reference/CVF_MLW6_SIMULATION_FAILURE_GATE_2026-06-05.md` | simulation/failure gate for high-risk promotion |
| `governance/compat/run_agent_automation_assist.py` | current AAF helper `signalReadout` source |
| `governance/compat/test_run_agent_automation_assist.py` | focused AAF helper tests |

## Pre-Flight Checks

The worker must run or record these checks before returning:

```powershell
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_run_agent_automation_assist
python governance/compat/run_agent_automation_assist.py --base 749dc791 --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_agent_automation_assist.py
```

The worker-return artifact must record command results or a
`BLOCKED_WITH_REASON` if a required command cannot run.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-gate, helper smoke,
packet-shape, source-fidelity, ASCII, and focused-test defects and rerun the
required checks before returning. Do not ask the operator whether to fix
allowed-scope defects.

Ask or return `BLOCKED_WITH_REASON` only when the repair would exceed Allowed
scope, change the claim boundary, require session/handoff/public-sync,
provider/live, RT2/RT3 runtime source, Learning Plane runtime mutation,
dependency install, destructive action, parked-lane reopening, or access to
secrets/quota.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `docs/reference/learning_signal_chain/README.md` | worker | may update only to add the LSC-T5/T7 row |
| `docs/reference/learning_signal_chain/CVF_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD.md` | worker | create |
| `governance/compat/run_agent_automation_assist.py` | worker | optional narrow read-only helper/latency fast-path edit only |
| `governance/compat/test_run_agent_automation_assist.py` | worker | optional focused tests for the helper/latency fast path only |
| `docs/reviews/CVF_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_WORKER_RETURN_2026-06-21.md` | worker | create |
| `docs/baselines/CVF_GC018_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_2026-06-21.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_FOR_WORKER_2026-06-21.md` | reviewer/closer | no worker edit |
| session state, active handoff, public-sync, RT2/RT3 runtime routes, Learning Plane runtime source, MCP packages, dependency manifests, `.github/**` | out of worker scope | forbidden |

## Scope / Target / Owner Boundary

Allowed scope:

- update `docs/reference/learning_signal_chain/README.md` to list LSC-T5/T7;
- create `docs/reference/learning_signal_chain/CVF_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD.md`;
- update `governance/compat/run_agent_automation_assist.py` only if needed for
  a read-only helper/latency fast-path output that remains advisory and
  non-mutating;
- update `governance/compat/test_run_agent_automation_assist.py` only for
  focused tests tied to the helper/latency fast-path output;
- create `docs/reviews/CVF_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_WORKER_RETURN_2026-06-21.md`;
- define bridge eligibility, proposal-only Learning Plane routing, `EVALUATED`
  mapping to MLW5/MLW6, latency guard rules, fast-path no-blocker behavior,
  and mutation boundary.
- update `docs/baselines/CVF_GC018_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_2026-06-21.md`
  status and closure evidence as reviewer/closer only;
- update this work order status and closure evidence as reviewer/closer only;
- create `docs/reviews/CVF_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_COMPLETION_2026-06-21.md`
  as reviewer/closer only.

Reviewer/closer closure scope:

- update this work order status and closure evidence;
- update the LSC-T5/T7 GC-018 baseline status;
- create the LSC-T5/T7 completion review;
- repair allowed-scope reference/front-door/helper/test/return wording,
  manifests, or packet-shape defects required by machine gates before commit.

Forbidden scope:

- no edits to `EXTENSIONS/**`, RT2/RT3 runtime source, MLW reference artifacts,
  session state, active handoff, root startup routers, public-sync, `.github/**`,
  dependency manifests, web UI routes, MCP packages, runtime provider routes, or
  Learning Plane runtime source;
- no ledger source directory, generated aggregate, generator, drift checker,
  durable store, runtime Learning Plane mutation, provider/live proof,
  dependency install, queue, daemon, watcher, wrapper/proxy enforcement, direct
  IDE/shell/git/filesystem interception, arbitrary command execution, or
  EDIT/COMMIT execution;
- no actual CLI/MCP adapter behavior, MCP tool implementation, shell bridge,
  adapter invocation, read-receipt enforcement, public catalog update,
  production/readiness claim, full-hook equivalence, cost optimization, speed
  claim, or universal governed-coding-control claim;
- no implementation of AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, or MLW8.

Risk ceiling: R1/R2 bounded reference and local helper/test work.

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Confirm `git status --short` before editing.
3. Read all Required First Reads.
4. Create the LSC-T5/T7 reference contract at the stable path.
5. Update the LSC reference front door with a bounded LSC-T5/T7 row.
6. If the reference contract requires helper visibility, update only AAF helper
   readout code and focused tests; otherwise leave helper/test files unchanged
   and record `N/A_WITH_REASON`.
7. Create the worker-return artifact with actual changed-set status and gate
   evidence.
8. Run required checks.
9. Return `COMPLETE_PENDING_REVIEW` uncommitted, or `BLOCKED_WITH_REASON` with
   exact blocker evidence.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order requirement | Disposition |
|---|---|---|
| LSC-T5 aligns signal ledger entries with RT2/RT3 and MLW3 proposal-only pipeline | Required Contract bridge-aligned and evaluated-bounded sections | ACCEPT |
| LSC-T5 maps `EVALUATED` to MLW5/MLW6 validators | Required Contract evaluated-bounded section | ACCEPT |
| LSC-T5 has no autonomous mutation and no new evaluator | Mutation boundary and forbidden scope | ACCEPT |
| LSC-T7 enforces capture-fast/promotion-slow budget | Required Contract latency-bounded and fast-path sections | ACCEPT |
| LSC-T7 avoids retrospective overburden | helper/test changes limited to read-only fast-path or N/A | ACCEPT |
| LSC-T0 future work orders preserve parked lanes and source verification | Authority chain, Source Verification Block, parked scope | ACCEPT |
| LSC-T0 acceptance requires no provider/live/public/direct-interception scope unless separately authorized | Forbidden scope and Claim Boundary | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| LSC-T0 design gate requires existing-chain mapping, latency budget, intake extension, mutation boundary, source authority, and runtime boundary | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 237-245 | Design Control Gate | LSC-T0 roadmap | VALUE_SET | ACCEPT |
| LSC-T0 defines LSC-T5 Learning Plane Bridge Alignment | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | line 256 | `LSC-T5` | LSC-T0 roadmap | VALUE_SET | ACCEPT |
| LSC-T0 defines LSC-T7 Latency Guard And Fast Path | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | line 258 | `LSC-T7` | LSC-T0 roadmap | VALUE_SET | ACCEPT |
| LSC-T0 maps `EVALUATED` to MLW5/MLW6 and preserves `autonomousMutationAuthorized=false` through LSC-T7 | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 282-285 | `EVALUATED`; `autonomousMutationAuthorized` | LSC-T0 roadmap | VALUE_SET | ACCEPT |
| Future LSC work orders must cite AAF, Finding-To-Governance, RT2/RT3, MLW3, MLW5, and MLW6 and keep capture fast/promotion governed | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 301-318 | Acceptance Criteria For Future Work Orders | LSC-T0 roadmap | VALUE_SET | ACCEPT |
| Learning Signal Intake owns lane, defectClass, severity, disposition, evidenceBasis, and autonomous mutation invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | lines 35-65, 107-171 | `LearningSignalIntakeInput`; `LearningSignalIntakeRecord` | LPF intake bridge | EXISTS | ACCEPT |
| RT2 bridge defines finding input, finding record, and build function | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/finding-to-learning-bridge.ts` | lines 35-100 | `FindingToLearningInput`; `FindingToLearningRecord`; `buildFindingToLearningRecord` | cvf-web finding bridge | EXISTS | ACCEPT |
| RT2 bridge declares and assigns autonomous mutation as false | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/finding-to-learning-bridge.ts` | lines 61-62, 99-100 | `autonomousMutationAuthorized` | `FindingToLearningRecord` | LITERAL_INVARIANT | ACCEPT |
| RT3 readout route calls RT2 bridge and returns `findingToLearningReadout` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/learning-plane/readout/route.ts` | lines 1-128 | `/api/learning-plane/readout`; `findingToLearningReadout` | RT3 readout route | EXISTS | ACCEPT |
| MLW3 defines proposal-only learning signal pipeline and routes high-risk proposals to MLW6 | `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md` | lines 15-23, 55-70, 80-86, 104-106 | `proposalAction`; `autonomousMutationAuthorized`; `MLW6` | MLW3 reference contract | VALUE_SET | ACCEPT |
| MLW5 defines audit feedback validation without direct mutation and routes high-risk candidates to MLW6 | `docs/reference/CVF_MLW5_AUDIT_FEEDBACK_VALIDATION_LANE_2026-06-05.md` | lines 15-22, 51-67, 74-83, 101-103 | `requiresSimulation`; `mutationAuthorized`; `BLOCK_PROMOTION` | MLW5 reference contract | VALUE_SET | ACCEPT |
| MLW6 defines simulation/failure gate and no automatic promotion | `docs/reference/CVF_MLW6_SIMULATION_FAILURE_GATE_2026-06-05.md` | lines 15-21, 50-77, 92-94, 112-114 | `promotionVerdict`; `Never promote automatically` | MLW6 reference contract | VALUE_SET | ACCEPT |
| LSC-T3 defines current helper `signalReadout` shape, advisory non-blocking default, and future LSC-T7 relationship | `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md` | lines 52-55, 72-77, 111-128, 177-179 | `signalReadout`; `blocking`; `LSC-T7` | LSC-T3 contract | VALUE_SET | ACCEPT |
| LSC-T4 defines promotion outcomes, closure-blocker conditions, de-dup policy, and LSC-T5/T7 relationship | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | lines 51-57, 68-74, 113-120, 138-141, 208-210, 226 | `READOUT_ONLY`; `CLOSURE_BLOCKER`; `rootCauseGroupId`; `LSC-T5`; `LSC-T7` | LSC-T4 policy | VALUE_SET | ACCEPT |
| LSC-T6 defines external-agent contract boundary and keeps LSC-T5/T7 parked until separately authorized | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | lines 337-341, 348-349, 355 | `Latency Boundary`; `LSC-T5`; `LSC-T7`; `CLI/MCP adapter implementation` | LSC-T6 contract | VALUE_SET | ACCEPT |
| AAF helper currently exposes `SignalReadoutItem`, JSON `signalReadout`, and human readout output | `governance/compat/run_agent_automation_assist.py` | lines 459-642, 736-750, 801-809 | `SignalReadoutItem`; `_build_signal_readout`; `signalReadout` | AAF helper | EXISTS | ACCEPT |
| Focused helper tests currently cover `signalReadout` JSON/human output, non-blocking default, and LSC-T4 vocabulary | `governance/compat/test_run_agent_automation_assist.py` | lines 628-728 | `SignalReadoutTests` | AAF helper tests | EXISTS | ACCEPT |

## New Doc-Only Terms

| Proposed term | Owner in LSC-T5/T7 | Runtime status | Reason |
|---|---|---|---|
| `learningPlaneBridgeCandidate` | LSC-T5/T7 reference contract | DOC_ONLY_NEW | proposal-only mapping from LSC signal to RT2/RT3/MLW3 path |
| `bridgeEligibility` | LSC-T5/T7 reference contract | DOC_ONLY_NEW | states whether a signal may be routed to proposal-only Learning Plane surfaces |
| `evaluationRoute` | LSC-T5/T7 reference contract | DOC_ONLY_NEW | maps `EVALUATED` to MLW5/MLW6 without defining a new evaluator |
| `latencyGuardDisposition` | LSC-T5/T7 reference contract and optional helper readout | DOC_ONLY_NEW | classifies whether a signal stays fast-path readout or needs governed promotion |
| `fastPathNoBlocker` | LSC-T5/T7 reference contract | DOC_ONLY_NEW | asserts routine readout-only signals must not block closure or add gate cost |

## Required LSC-T5/T7 Contract

The worker must produce a reference contract that includes:

- Bridge Alignment: exact mapping from LSC signal/intake fields to RT2/RT3 and
  MLW3 proposal-only fields.
- Bridge Eligibility Matrix: which LSC-T4 outcomes remain readout-only, which
  become proposal candidates, and which require work-order or blocker handling.
- `EVALUATED` Route: reuse MLW5 audit feedback validation and MLW6 simulation/
  failure gate for high-risk promotion; define no new evaluator.
- Latency Guard Rules: capture stays cheap/local, readout-only signals do not
  add gate latency, and promotion/validation is batched or governed.
- Fast Path Rule: routine `READOUT_ONLY` signals must keep `blocking=false`;
  only source-backed LSC-T4 `CLOSURE_BLOCKER` conditions may block closure.
- Optional Helper/Test Implementation: if edited, AAF helper output must stay
  read-only, deterministic, and focused; tests must verify no mutation, no
  runtime Learning Plane call, and no blocker inflation for routine signals.
- Mutation Boundary: `autonomousMutationAuthorized=false` remains invariant.
- Claim Boundary: no ledger store, generator, drift checker, runtime Learning
  Plane mutation, provider/live proof, CLI/MCP adapter behavior, public-sync,
  readiness, full-hook equivalence, cost optimization, or universal control.

## Worker Return Packet Shape Contract

The worker-return artifact must include these required terms and sections:

| Required item | Required value |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| executionBaseHead | actual `git rev-parse --short HEAD` captured at worker start |
| git status | actual `git status --short` after worker edits |
| Source Inventory | all files read and edited |
| Scan Depth Ledger | source-read depth and any unreadable/deferred files |
| Gate Evidence | required command results |
| Changed Files | exact pending changed paths |
| Purpose | worker-return purpose section |
| Scope / Methodology | worker-return scope and methodology section |
| Findings / Position | worker-return findings and final position section |
| Risk / Corrective Action | worker-return risk and corrective action section |
| Claim Boundary | no forbidden runtime/provider/public/adapter/ledger scope |
| Agent Operation Trace Block | worker role trace |
| Delta Execution Claim Boundary Control Block | N/A rows for execution-control claims |
| Public Export Disposition | `DEFERRED_PRIVATE_ONLY` |
| WORKER_EXPERIENCE_RETRO | structured block or exact N/A token |

Conditional sections must be present or marked `N/A with reason`:

- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| LSC-T5/T7 reference contract exists | stable reference file created |
| LSC front door updated | LSC-T5/T7 row present and bounded |
| Bridge alignment is source-verified | RT2/RT3/MLW3/5/6 and intake bridge cited |
| Latency guard preserves fast path | routine readout-only signals do not become blockers or deep gates |
| Optional helper edits are focused | only AAF helper/test files touched for read-only behavior |
| Required checks pass | commands in Pre-Flight Checks pass or block with reason |
| Worker does not commit | changed set remains uncommitted for reviewer |
| Forbidden scope untouched | no protected/runtime/public/provider/adapter paths beyond allowed helper/test files |

## Closure Checklist

Reviewer/closer closure evidence must resolve these items:

- Required deliverables exist.
- No forbidden paths changed.
- Source Verification claims remain current.
- Bridge remains proposal-only and mutation-bounded.
- Latency guard remains read-only/fast-path unless separately authorized.
- README row states no runtime/public/provider/adapter behavior.
- Worker-return packet includes required sections and token.
- Reviewer-fast or stricter gate passes.
- Commit ownership remains reviewer/closer only.
- Session-sync is performed only if mode or next-move surfaces change.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_FOR_WORKER_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer/closer patch | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer/closer patch | PASS |
| Worker return | `docs/reviews/CVF_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_WORKER_RETURN_2026-06-21.md` | `Status: COMPLETE_PENDING_REVIEW`; accepted by reviewer/closer | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_COMPLETION_2026-06-21.md` | reviewer-owned final disposition `CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | roadmap top `Status: LSC_T1_DISPATCH_READY`; roadmap remains governing LSC-T0 plan | PASS |
| Reference front door | `docs/reference/learning_signal_chain/README.md` | LSC-T5/T7 row present | PASS |
| Reference contract | `docs/reference/learning_signal_chain/CVF_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Helper implementation | `governance/compat/run_agent_automation_assist.py` | read-only `latencyGuardDisposition` helper field accepted | PASS |
| Focused tests | `governance/compat/test_run_agent_automation_assist.py` | focused tests pass: 53/53 | PASS |
| Session continuity | active session front-door/state/handoff after material commit | session-sync follows material closure commit | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | unchanged; `python governance/compat/generate_corpus_scan_registry.py --check` PASS | PASS |
| Registry Markdown | `docs/corpus-intelligence/registry/` | unchanged; no per-entry registry source changed in LSC-T5/T7 | PASS |
| External evidence digest | N/A with reason: no external benchmark/provider/live digest created | reference/helper closure only | N/A with reason |
| System loop interlock | N/A with reason: no runtime/source interlock changed by dispatch | no runtime/source mutation by dispatch | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: LSC-T5/T7 dispatch creates no runtime receipt | N/A_WITH_REASON |
| Query acceptance evidence | N/A with reason: LSC-T5/T7 dispatch performs no query acceptance | N/A_WITH_REASON |
| Worker-return acceptance | worker return present and accepted by reviewer/closer | PASS |
| Closure claim | `CLOSED_PASS_BOUNDED` bridge/latency reference and read-only helper closure | PASS |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all Required Deliverables are created
and required gate evidence is recorded. Return `BLOCKED_WITH_REASON` if the task
requires forbidden paths, runtime Learning Plane mutation, RT2/RT3 runtime
edits, provider/live proof, public-sync, MCP/CLI adapter behavior, dependency
install, destructive actions, or parked-lane reopening.

## Current Runtime Freshness Verification

| Claim | Freshness evidence | Disposition |
|---|---|---|
| LSC-T5/T7 contract path does not already exist | `Get-ChildItem docs/reference/learning_signal_chain -Filter '*LSC_T5*'`; `Get-ChildItem docs/reference/learning_signal_chain -Filter '*LSC_T7*'` returned no existing file before dispatch authoring | ACCEPT |
| LSC-T5/T7 work order and baseline paths do not already exist | `Get-ChildItem docs/work_orders -Filter '*LSC_T5*'`; `Get-ChildItem docs/baselines -Filter '*LSC_T5*'`; matching T7 queries returned no existing file before dispatch authoring | ACCEPT |
| Current helper exposes read-only `signalReadout` | `governance/compat/run_agent_automation_assist.py` lines 459-642, 736-750, 801-809 | ACCEPT |
| Runtime Learning Plane mutation is not authorized | Allowed and Forbidden scope in this work order | N/A_WITH_REASON |
| CLI/MCP adapter behavior is not authorized | Forbidden scope and Claim Boundary | N/A_WITH_REASON |
| Provider/live proof is not authorized | Forbidden scope and Claim Boundary | N/A_WITH_REASON |
| Public-sync is not authorized | Public route and Public Export Disposition | N/A_WITH_REASON |

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`.
- Predecessor intake artifact: `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md`.
- Predecessor readout artifact: `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md`.
- Predecessor promotion artifact: `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md`.
- Predecessor external-agent artifact: `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because LSC-T5/T7 moves from
  roadmap next-move into dispatch-ready bridge/latency work.
- Routing matrix status: `DO_NOW` for bridge/latency reference and optional
  read-only helper/test fast path; `SEPARATE_RUNTIME_TRANCHE` for ledger store,
  generator, drift checker, runtime Learning Plane mutation, public-sync, live
  proof, or CLI/MCP adapter implementation; `STRATEGIC_OPERATOR_DECISION` for
  AAF-T6/T7, CGE-T3, ACE-R1, MLW7/8 after this tranche; `OUT_OF_SCOPE` for
  provider/live/direct-interception/readiness claims.
- Semantic sampling status: sampled LSC-T0 LSC-T5/T7 rows, LSC-T1 intake
  ownership, LSC-T3 readout shape, LSC-T4 blocker policy, LSC-T6 latency
  boundary, RT2/RT3 bridge/readout, MLW3/5/6 proposal and validation contracts,
  and AAF helper readout source.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | LSC remains capture-fast, promotion-slow, proposal-only, and mutation-bounded. |
| CHANGED_DISPOSITION | LSC-T5/T7 bridge and latency guard moved from roadmap next-move to dispatch requirements. |
| NEW_FINDING | Combined T5/T7 needs one bridge/latency boundary so helper changes do not imply Learning Plane runtime mutation. |
| REMOVED_OR_REJECTED | runtime/provider/live/public-sync/direct-interception/CLI-MCP adapter behavior remains rejected for this dispatch. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | LSC-T5/T7 reference contract, README row, optional AAF helper/test fast-path, and worker-return packet. |
| SEPARATE_RUNTIME_TRANCHE | ledger store, generator, drift checker, Learning Plane runtime mutation, provider/live proof, public-sync, CLI/MCP adapter implementation. |
| STRATEGIC_OPERATOR_DECISION | AAF-T6/T7, CGE-T3, ACE-R1, MLW7/8 remain parked unless separately authorized. |
| OUT_OF_SCOPE | provider/live, public-sync, direct interception, readiness, universal control. |
| RESOLVED_BY_DESIGN | reuse RT2/RT3/MLW3/MLW5/MLW6 proposal-only chain instead of inventing a new evaluator. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LSC-T5T7-WO-S1 | LSC-T0 work plan | LSC-T5 aligns bridge; LSC-T7 owns latency guard | mapped into Required Deliverables | Could the worker implement runtime mutation under bridge wording? | PASS_BOUNDARY |
| LSC-T5T7-WO-S2 | LPF intake bridge | autonomous mutation remains false | Required Contract mutation boundary | Could bridge alignment authorize mutation? | PASS_NO_MUTATION |
| LSC-T5T7-WO-S3 | RT2/RT3 source | bridge/readout already exist as advisory surfaces | Source Verification | Could the worker edit RT2/RT3 runtime source? | PASS_FORBIDDEN |
| LSC-T5T7-WO-S4 | LSC-T4 policy | only closure-blocker conditions can pause closure | latency guard requirement | Could readout-only signals block closure? | PASS_NO_BLOCKER |
| LSC-T5T7-WO-S5 | MLW5/MLW6 contracts | high-risk proposals require validation and no auto-promotion | evaluated-bounded requirement | Could LSC-T5 define a new evaluator? | PASS_NO_NEW_EVALUATOR |

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - LSC-T5/T7 dispatch is a
  bounded bridge/latency work order, not a corpus enumeration or legacy scan.
- Corpus root: NOT_APPLICABLE_WITH_REASON - no corpus root is assigned.
- Snapshot time: NOT_APPLICABLE_WITH_REASON - no corpus snapshot is taken.
- Enumeration command: filesystem-backed direct file reads listed in Source
  Verification Block and Required First Reads; no corpus enumeration command is
  authorized.
- Manifest artifact or inline manifest: inline Source Verification Block above.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is
  created.
- Processing ledger artifact or inline ledger: inline Source Verification Block
  and semantic sampling tables above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=corpus enumeration and legacy scan surfaces out of scope; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: corpus scan, legacy source-family enumeration,
  public-sync copy, runtime/provider/live proof, CLI/MCP adapter, and parked lanes.
- Unreadable or unsupported files: 0.
- Aggregation check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate is
  created.
- Drift check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate or generated
  corpus registry is changed.
- Output traceability: Required Deliverables and Source Verification Block
  define all worker output traceability.
- Adversarial verification: reviewer/closer must run reviewer-fast or stricter
  applicable gate before acceptance.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output or LSC-T6 external signal event to finding classification to governed LSC signal to proposal-only bridge candidate |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | LSC-T5/T7 Learning Plane Bridge And Latency Guard |
| Disposition | ADAPT as CVF-owned bridge/latency reference and optional local helper fast-path |
| Claim boundary | external-agent returns remain input only until classified and promoted through governed CVF artifacts; LSC-T5/T7 does not implement external-agent CLI/MCP adapter behavior |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T5/T7 bridge/latency worker dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation/reference and optional read-only local helper/test work only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | Learning Plane bridge alignment, proposal-only routing, latency guard, fast-path readout boundary, and mutation boundary only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, CLI/MCP adapter behavior, runtime Learning Plane mutation, cost optimization, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| LSC signals need a source-verified bridge to existing Learning Plane proposal surfaces | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T5/T7 must define proposal-only bridge alignment | handled by this dispatch |
| Routine readout-only signals must not inflate latency or block closure | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | LSC-T7 must preserve capture-fast/promotion-slow rules | handled by this dispatch |
| Actual Learning Plane mutation remains out of scope | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime mutation implementation in this tranche | handled |
| Public-facing export remains out of scope | RUNTIME_SIGNAL_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | public-sync requires separate authorization | handled |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch for Learning Signal Chain bridge/latency
work. No public-sync remote, public commit, public artifact path, or public
claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | LSC-T5/T7 dispatch authoring, 2026-06-21 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification reads, apply_patch edits, dispatch gates |
| Target paths | `docs/baselines/CVF_GC018_LSC_T5_T7_LEARNING_PLANE_BRIDGE_LATENCY_GUARD_2026-06-21.md`; this work order |
| Allowed scope source | operator-selected LSC roadmap order and active session next allowed move |
| Before status evidence | HEAD `749dc791`; clean worktree before dispatch authoring |
| After status evidence | dispatch packet created for worker |
| Diff evidence | pre-dispatch gates required before commit |
| Approval boundary | dispatch only; no worker execution, runtime mutation, provider/live, public-sync, or CLI/MCP adapter behavior |
| Claim boundary | worker dispatch packet only |
| Agent type | dispatcher |
| Invocation ID | `lsc-t5-t7-bridge-latency-guard-dispatch-2026-06-21` |
| Expected manifest | this work order and paired GC-018 baseline |
| Actual changed set | checked by dispatch gates before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch packet |

## Claim Boundary

This work order dispatches only LSC-T5/T7 Learning Plane bridge alignment,
latency guard/fast-path reference work, optional read-only AAF helper/test
changes inside the named worker scope, and worker-return evidence. It does not
authorize a ledger store, source directory, generator, drift checker, durable
store, runtime Learning Plane mutation, provider/live proof, actual CLI/MCP
adapter behavior, public-sync, direct interception, wrapper/proxy enforcement,
queue/daemon, watcher, readiness, cost optimization, full-hook equivalence, or
universal governed-coding control.

## Evidence Requirements

The worker return must include command-backed evidence for:

- `git rev-parse --short HEAD`;
- `git status --short`;
- `python -m unittest governance.compat.test_run_agent_automation_assist`;
- `python governance/compat/run_agent_automation_assist.py --base 749dc791 --head HEAD --json --enforce`;
- `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_agent_automation_assist.py`.

If any command cannot run, the worker return must use `BLOCKED_WITH_REASON` and
record the exact command, failure stage, and whether the blocker is inside or
outside Allowed scope.

## Review Gate

Reviewer/closer must not accept the worker return until:

- all changed files are inside Allowed scope;
- source verification remains current;
- forbidden runtime/provider/public/adapter/session scope is untouched;
- helper/test edits, if any, are read-only and focused;
- worker-return packet shape and `WORKER_EXPERIENCE_RETRO` requirements pass;
- reviewer-fast or stricter local governance gate passes before commit.

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order.

Operator checkpoint is required before any runtime Learning Plane mutation,
RT2/RT3 runtime edit, provider/live proof, public-sync, dependency install,
session/handoff edit by the worker, CLI/MCP adapter behavior, direct
interception, queue/daemon/watcher/readiness claim, parked-lane reopening,
secrets/quota use, destructive action, or broader claim boundary change.
