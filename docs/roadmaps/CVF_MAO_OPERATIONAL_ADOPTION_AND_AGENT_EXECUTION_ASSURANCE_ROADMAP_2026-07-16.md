# CVF MAO Operational Adoption And Agent Execution Assurance Roadmap

Memory class: FULL_RECORD

docType: roadmap

Date: 2026-07-16

Status: MAO_OA_T3_DISPATCHED_WORKER_NEXT

Roadmap ID: MAO-OA

## Purpose

Move the closed deterministic MAO foundation toward governed operational
adoption for real agent project execution without recreating its contracts.
The roadmap begins with a source-verified audit of the current ownership and
wiring gap, then admits implementation only in dependency-released tranches.

## Authorization / Decision

The active session next move authorizes this roadmap and its required
source-verified packet. SOT3-APP-T0B closed at material commit `577237cba`.
The earlier MAO foundation closed at `29c55ca36`, and its bounded live value
pilot closed `REVIEWER_ACCEPTED_VALUE_NOT_PROVEN` at `75f5c0b90`.

Decision: `MAO_OA_T3_DISPATCHED_WORKER_NEXT`.

T0 remains accepted as a documentation/evidence closure. MAO-OA-T1 is
independently accepted after one reviewer-owned GC-051 registry repair. The
operator checkpoint on 2026-07-16 released one source-verified MAO-OA-T2
dispatch for a bounded execution-plane durable run store, deterministic replay,
fail-closed recovery, and idempotent resume. T2 is independently accepted after
two reviewer-owned malformed-snapshot fail-closed guards and matching tests.
The operator checkpoint on 2026-07-17 releases one source-verified MAO-OA-T3
dispatch for a bounded execution-plane launcher composing the accepted durable
store, fake/local provider-neutral adapter, and deterministic lifecycle
controller. MAO-OA-T4 through T7 remain parked.

## Scope / Target / Owner Boundary

Target: an orchestrator-owned, durable, evidence-convergent execution path for
bounded CVF agent projects.

Owner boundaries:

- control plane owns risk, role admission, approval, and authority decisions;
- execution plane owns accepted task-graph lifecycle and durable execution
  evidence;
- provider adapters execute only explicit admitted tasks and do not own policy;
- independent reviewer evidence remains separate from worker conclusions;
- exactly one designated closer owns integration and commit conversion;
- session state and workspace state remain governed projections, not runtime
  queues or execution truth.

MAO-OA-T0 owns source inspection and an owner/gap matrix only. It may not edit
runtime, tests, package roots, session state, or public surfaces.

## Non-Goals

- no Agent OS, autonomous general scheduler, hosted platform, or production
  readiness claim;
- no unbounded fan-out, automatic commit, worker self-approval, or implicit
  scope expansion;
- no recreation of the existing MAO task graph, ledger, role resolver,
  delegation, reviewer isolation, closer, lifecycle, or evidence contracts;
- no provider call, live proof, build, typecheck, or test in MAO-OA-T0;
- no SOT3-APP-T1 or other absorption before this roadmap reaches governed
  closure;
- no public-sync or push.

## Design Control Gate

Each tranche requires a fresh GC-018 and source-verified work order. T1 and
later work stays `HOLD` until the preceding completion review is accepted and
the next packet cites its material commit, final disposition, refreshed base
anchors, exact allowed paths, and pre-dispatch PASS evidence.

Any implementation packet must reuse the existing MAO foundation owners and
prove a specific missing connection. A packet that proposes a parallel task
graph, role policy, reviewer contract, closer contract, or evidence truth is
blocked.

## Dependency Release Evidence

| Dependency | Current evidence | Release decision |
|---|---|---|
| SOT3-APP-T0B independent closure | `docs/reviews/CVF_SOT3_APP_T0B_COMPLETION_2026-07-16.md`; material commit `577237cba` | SATISFIED |
| MAO deterministic foundation closure | `docs/reviews/CVF_MAO_T9_INDEPENDENT_CRITIQUE_RECONCILIATION_AND_CLOSURE_COMPLETION_2026-07-12.md`; material commit `29c55ca36` | SATISFIED |
| MAO live value-pilot stop rule | `docs/reviews/CVF_MAO_LIVE_T1_PROVIDER_ADAPTER_VALUE_PILOT_COMPLETION_2026-07-12.md`; material commit `75f5c0b90` | SATISFIED_WITH_BOUNDARY: do not repeat the easy comparison task |
| Active next-move authority | `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/state/entries/sot3AppT0BClosure20260716.json` | SATISFIED for roadmap and T0 audit only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Existing immutable task-graph compiler | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | lines 273-357 | `compileTaskGraph` | execution-plane MAO task graph | ACCEPT |
| Existing in-memory append-only execution ledger | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | lines 149-160 | `MaoEventLedger` | execution-plane MAO event ledger | ACCEPT |
| Existing fake/local delegation adapter has no queue or runtime caller wiring | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | lines 1-14 and 137-168 | `MaoDelegationAdapter` | execution-plane MAO delegation adapter | ACCEPT |
| Existing lifecycle controller has deterministic clock and no durable storage | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts` | lines 232-250 | `MaoLifecycleController` | execution-plane MAO lifecycle controller | ACCEPT |
| Existing control-plane role resolver is pure and has no runtime caller | LITERAL_INVARIANT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | lines 1-11 and 158-188 | `resolveRole` | control-plane MAO role resolver | ACCEPT |
| Existing representative chain is a local deterministic pilot | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/representative.pilot.contract.ts` | lines 1-14 and 341-425 | `runPilotChain` | execution-plane representative pilot | ACCEPT |
| Existing live bridge composes one fixed comparison lane through Model Gateway | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts` | lines 1-18 and 502-630 | `runMaoLane` | MAO live-provider value pilot | ACCEPT |
| Exactly one closer and separate session sync remain upstream invariants | DOC_CONTRACT | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | CF-07 and C3 | `commitOwner(CLOSURE)` | Agent Handoff Contract | ACCEPT |

## Current Runtime Freshness Verification

Verified at dispatch base `c137986c6` on 2026-07-16.

| Check | Current result | Disposition |
|---|---|---|
| MAO local barrel statement | `src/mao/index.ts` lines 3-7 says it is not imported by root and has no queue, scheduler, UI, or runtime caller | GAP_CANDIDATE_FOR_T0_AUDIT |
| Execution-plane root search | `rg -n "mao|Mao|MAO" EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` returned no match | GAP_CANDIDATE_FOR_T0_AUDIT |
| Control-plane root search | `rg -n "mao|Mao|MAO" EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/index.ts` returned no match | GAP_CANDIDATE_FOR_T0_AUDIT |
| Caller search | current non-test hits are MAO-local composition and the dedicated live pilot; test hits dominate contract use | RECOMPUTE_AND_CLASSIFY_IN_T0 |
| Durable-state source | current event ledger and lifecycle controller explicitly use in-memory collections and no durable storage | RECOMPUTE_AND_CLASSIFY_IN_T0 |

These are source-visible gap candidates, not proof that every possible dynamic
or external caller is absent. T0 must search all governed source roots and
preserve `UNRESOLVED_INVOCATION` where a caller edge cannot be proven.

## Work Plan And Dependencies

| Tranche | Scope | Dependency | Status |
|---|---|---|---|
| MAO-OA-T0 | current owner, entrypoint, caller, durable-state, liveness, evidence, reviewer, closer, and operator-route audit | dependencies above | PASS_BOUNDED_WITH_REVIEWER_REPAIRS |
| MAO-OA-T1 | root/package adoption seam and orchestrator contract | accepted T0 owner/gap matrix plus fresh GC-018 and work order | PASS_BOUNDED_WITH_REVIEWER_REPAIR |
| MAO-OA-T2 | durable run store, replay, recovery, and idempotent resume | accepted T1 contract `1bb5ff7f3`, operator checkpoint, canonical execution-plane append-only storage authority, and independent T2 completion review | PASS_BOUNDED_WITH_REVIEWER_REPAIR |
| MAO-OA-T3 | governed worker launcher, heartbeat, timeout, cancellation, and provider-neutral adapter wiring | accepted T2 closure `042abf44b`, explicit operator checkpoint, and current-source verification | DISPATCHED_WORKER_NEXT |
| MAO-OA-T4 | independent evidence collection, review repair, dissent, closer convergence, and commit/session interlock | accepted T3 | HOLD |
| MAO-OA-T5 | operator readout and bounded workspace/session projection | accepted T4 | HOLD |
| MAO-OA-T6 | materially harder representative agent-project proof with predeclared value hypothesis | accepted T5 plus explicit live/provider authority | HOLD |
| MAO-OA-T7 | independent critique, closure diff, architecture/public disposition, and roadmap closure | accepted T6 | HOLD |

## MAO-OA-T0 Required Output

The worker creates exactly:

- `docs/reviews/CVF_MAO_OA_T0_OPERATIONAL_ADOPTION_OWNER_AND_GAP_MATRIX_2026-07-16.md`
- `docs/reviews/CVF_MAO_OA_T0_WORKER_RETURN_2026-07-16.md`

The matrix must terminally classify:

- every MAO source module and its tested/public/root/caller status;
- current orchestration entrypoints and invocation edges;
- task graph compilation and admission ownership;
- event/evidence durability and replay ownership;
- worker launch, heartbeat, cancel, timeout, retry, and orphan ownership;
- reviewer source isolation and evidence recomputation;
- closer, commit steward, material/session split, and next-move ownership;
- operator readout and workspace projection;
- live-provider bridge and value-proof limits;
- the smallest source-verified T1 implementation boundary.

Every row ends in `REUSE_AS_IS`, `WIRE_EXISTING`, `EXTEND_EXISTING`,
`NEW_OWNER_REQUIRED`, `DEFER_VALUE_NOT_PROVEN`, `REJECT_DUPLICATE`, or
`UNRESOLVED_INVOCATION`.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Owning work order | Closure evidence |
|---|---|---|
| Recompute all current MAO owners/callers | MAO-OA-T0 | terminal owner/gap matrix plus exact commands |
| Preserve ambiguity for unproven invocation edges | MAO-OA-T0 | `UNRESOLVED_INVOCATION` rows with search evidence |
| Prevent duplicate foundation owners | MAO-OA-T0 | overlap decision per concern and T1 boundary |
| Root/package adoption seam | MAO-OA-T1 | source/test implementation and negatives |
| Durable progress and recovery | MAO-OA-T2 | durable replay/recovery receipts and fault tests |
| Governed worker execution/liveness | MAO-OA-T3 | source wiring, focused tests, diagnostics |
| Independent review and closer convergence | MAO-OA-T4 | isolated evidence and one-closer negative proof |
| Operator readout/projection | MAO-OA-T5 | deterministic read model and drift checks |
| Harder value proof | MAO-OA-T6 | real provider evidence and declared quality hypothesis |
| Final critique/closure | MAO-OA-T7 | independent review and machine closure package |

## Acceptance Criteria

- T0 produces a complete source-backed owner/gap matrix with no silent owner
  family and no implementation mutation.
- T1 is not released until T0 names one exact minimal adoption seam and its
  current owners, callers, tests, failure cases, and forbidden duplicates.
- T2-T5 prove durable progress, liveness, review independence, one-closer
  convergence, and operator visibility before live value proof.
- T6 uses a materially harder task and predeclared quality-gain hypothesis;
  repeating the closed easy comparison is forbidden.
- T7 reconciles every roadmap row, public disposition, architecture admission,
  and remaining limitation before closure.

## Verification And Evidence

Each tranche must use a real changed range, direct current-source evidence,
the phase-matching agent autorun gate, and an independently recomputed closure
decision. T0 evidence is limited to repository reads and documentation gates;
it does not establish runtime, provider, live, or public behavior.

## MAO-OA-T0 Closure Evidence

- accepted matrix: 18/18 terminal rows with 16 current-owner concerns, two
  explicit ownerless concerns, and one unresolved external-dynamic-invocation
  boundary;
- disposition reconciliation: 2 reuse, 6 wire, 6 defer-value-not-proven, 3
  new-owner-required, and 1 unresolved invocation;
- current source manifest: 13 MAO source files, 9 MAO tests, and one dedicated
  live-pilot script;
- root/caller result: neither package root exports MAO; no tracked
  non-test/non-MAO-local caller of the audited symbols was found;
- accepted T1 packet boundary: package-root re-exports plus one pure
  orchestration composition contract reusing `compileTaskGraph` and
  `resolveRole`; no worker/provider launch or durable storage;
- reviewer decision: accepted after one consolidated repair round; no worker
  repair turn, provider call, runtime command, source mutation, or public work.
- completion review: `docs/reviews/CVF_MAO_OA_T0_COMPLETION_REVIEW_2026-07-16.md`.

## MAO-OA-T1 Dispatch Evidence

- paired baseline:
  `docs/baselines/CVF_GC018_MAO_OA_T1_PACKAGE_ROOT_AND_ORCHESTRATION_COMPOSITION_CONTRACT_2026-07-16.md`;
- canonical work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T1_PACKAGE_ROOT_AND_ORCHESTRATION_COMPOSITION_CONTRACT_2026-07-16.md`;
- route: `WORKER_MUST_NOT_COMMIT` implementation worker followed by independent
  reviewer/closer and separate session-sync steward;
- implementation boundary: execution/control package-root exports plus one pure
  deterministic composition contract reusing `compileTaskGraph` and
  `resolveRole`;
- forbidden boundary: no durable storage, worker/provider launch, lifecycle,
  reviewer/closer execution, UI, CLI/MCP, live proof, public-sync, or push.

## MAO-OA-T1 Closure Evidence

- execution package root forwards the existing MAO barrel once; control package
  root forwards one MAO domain barrel;
- `composeOrchestrationPlan` reuses `compileTaskGraph` and `resolveRole`, returns
  compile failures with null role resolution, and preserves resolver rejection
  and operator-approval-required receipts;
- reviewer reruns passed 3/3 execution tests, 11/11 control tests, and both
  TypeScript checks;
- execution root is 1,418 lines against the approved 1,450-line ceiling;
- the worker preserved `WORKER_MUST_NOT_COMMIT` at base `77e6c3a64`;
- reviewer reproduced the sole 61/62 fast-gate gap, added one generated-source
  registry entry covering the three missing new paths plus the changed control
  root cited by staged closure evidence, regenerated the GC-051 aggregate, and
  obtained 62/62 reviewer-fast PASS; and
- completion review:
  `docs/reviews/CVF_MAO_OA_T1_COMPLETION_REVIEW_2026-07-16.md`.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | current deterministic MAO foundation plus proposed T1 composition boundary | T0 closure is static evidence only; T1 needs fresh source-verified authority | accepted T0 matrix and reviewer recomputation | internal composition only; worker/provider launch remains T3 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no current MAO CLI/MCP owner | no ingress, authentication, approval, receipt, raw-data, mutation, or public behavior is authorized | OA-18 tracked-source search with dynamic ambiguity retained | external adapter remains parked under a later separate tranche | `N/A_WITH_REASON` |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Memory class; docType; Status; Purpose; Authorization / Decision; Scope / Target / Owner Boundary; Non-Goals; Design Control Gate; Source Verification Block; Current Runtime Freshness Verification; Work Plan And Dependencies; Roadmap-To-Work-Order Trace Matrix; Dual Agent Surface Matrix; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm source-backed roadmap and T0 dispatch structure before material commit |
| claimBoundary | checker conformance does not prove runtime adoption, provider behavior, or user value |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: current MAO modules are strong deterministic
contracts but lack a proven orchestrator-owned durable project execution path.

Evidence Comparison Requirement: each tranche compares direct source/runtime
evidence with this prediction and narrows or rejects it where contradicted.

Contradiction Handling Requirement: contradictory caller, durability, or
integration evidence must be recorded, not forced into the predicted gap.

Claim Update Requirement: every completion review records confirmed, revised,
narrowed, or invalidated adoption claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap and current-source mapping. Public export is
not authorized.

## Next Allowed Move

Execute only
`docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T3_OPERATIONAL_WORKER_LAUNCHER_AND_LIVENESS_WIRING_2026-07-17.md`
under `WORKER_MUST_NOT_COMMIT`. MAO-OA-T4 through T7, SOT3-APP-T1, other
absorption, real provider/network/process/queue execution, reviewer/closer
execution, operator projection, live expansion, public-sync, and push remain
parked.

## Claim Boundary

This roadmap records a reviewer-accepted documentation-only T0 owner/gap audit,
a reviewer-accepted bounded T1 package-root and pure-composition seam, and a
reviewer-accepted bounded T2 local durable-store and replay component, and one
dispatched T3 fake/local operational-launcher packet. Dispatch is not
implementation or provider proof and does not release T4 or later. The roadmap
defines a future governed path toward operational adoption but does not claim
distributed concurrency, real provider launch,
liveness, provider control,
automatic review, automatic commit, public readiness, production readiness,
scale, certification, shipment, or demonstrated user value.
