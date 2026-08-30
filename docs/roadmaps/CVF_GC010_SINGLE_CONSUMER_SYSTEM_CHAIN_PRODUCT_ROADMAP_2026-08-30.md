# CVF GC-010 Single-Consumer System Chain Product Roadmap

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

Roadmap ID: GC010-SCR-R1

Date: 2026-08-30

Owner: operator and orchestrator/reviewer

## Purpose

Create one real CVF-owned, non-test consumer for `AgentExecutionRuntime` and
connect it to an existing governed execution channel without duplicating guard
evaluation, approval settlement, provider-attempt admission, provider calls,
or durable evidence. This is a product-development roadmap requested by the
operator, not a retroactive claim that the historical GC-010 reopen condition
is already satisfied.

## Decision And Value Case

Proceed because the repository now contains materially stronger foundation
source than at the July value-park decision: `AgentExecutionRuntime` composes
the approval bridge; the approval bridge has exactly-once settlement and is
package-exported; GC-009 has an accepted Web caller; and `/api/execute` now
wraps each provider call with provider-attempt admission and reconciliation.

The remaining value-bearing gap is narrow: select and implement one consumer
boundary that composes these owners instead of leaving them as independent
planes. Broad multi-plane integration, a new UI, an MCP launcher, and
historical-only cleanup do not justify their current cost and are excluded.

## Historical Boundary

The closed July roadmap and GC010-AER-T2 completion remain historical evidence.
Their four-fact reopen condition is not declared satisfied at roadmap start.
This roadmap is separately authorized product work intended to create the
missing source facts. The paired gap may be reclassified only after current
source and accepted proof demonstrate all four together:

1. direct import or construction of `AgentExecutionRuntime`;
2. a concrete registered production invocation trigger;
3. real `GuardRuntimeEngine` and `ExecutionProvider` wiring;
4. a durable receipt or audit consumer on the invoked path.

## Target Chain

```text
existing CVF-owned trigger
  -> one composition owner
  -> one guard decision
  -> approval bridge when required
  -> one provider-attempt admission per actual provider call
  -> one actual provider call per admitted attempt
  -> one reconciled result and durable audit/receipt projection
  -> caller response
```

## Design Control Gate

### Scope boundary

- One named non-test trigger and the smallest cooperating path set.
- Existing `AgentExecutionRuntime`, `ApprovalExecutionBridge`, GC-009 gateway,
  Web provider-attempt admission, and durable evidence owners are reused where
  source-compatible.
- T0 is documentation-only. Runtime edits begin only through a fresh T1 work
  order after independent T0 acceptance.

### Non-goals

- no universal channel coverage;
- no arbitrary external-agent launch, interception, or control;
- no new UI, deployment, public release, or production-readiness claim;
- no Learning Plane, vector runtime, DEAR P4/P5, or unrelated roadmap work;
- no provider/live call before the separately parked T5 checkpoint.

### Mandatory invariants

- Guard evaluation occurs exactly once for each admitted logical execution.
- Provider-attempt admission occurs exactly once before each actual provider
  call, including retries.
- A denied attempt starts zero provider calls.
- An admitted attempt starts at most one provider call.
- Approval settlement is exactly once and preserves timeout/abort cleanup.
- Durable receipt/audit projection is reconciled for success, denial, thrown
  or rejected invocation, retry exhaustion, timeout, and cancellation.
- No adapter is accepted merely because it exports or constructs the runtime.

### Source-verification plan

T0 compares five candidate families against current committed source:

1. package-native composition adapter consumed by `cvf-web`;
2. direct `cvf-web` caller;
3. Execution Plane or MAO caller;
4. CLI or MCP caller;
5. remain parked with an exact missing-fact condition.

For each candidate, T0 must name the trigger, construction/import owner,
engine owner, provider adapter owner, approval path, attempt-admission owner,
durable receipt consumer, response mapper, failure path, duplication risk,
and smallest future manifest.

### Claim boundary

T0 can prove only a current-source architecture decision. T1-T4 can later
prove bounded local composition and deterministic behavior if released. A
real-provider governance claim requires the separate T5 checkpoint and the
repository live-proof standard.

## Scope

The scope is the one-consumer GC-010 product chain and the minimum cooperating
owners needed to preserve existing GC-009, approval, provider-attempt, and
durable-evidence behavior. T0 is limited to the paired architecture audit and
worker return.

## Non-Goals

The non-goals listed inside the Design Control Gate are binding: no universal
channel, new UI, external-agent control, Learning Plane, vector runtime, DEAR,
provider use, deployment, public release, or production-readiness work.

## Tranches

| Tranche | Scope | State | Release condition |
| --- | --- | --- | --- |
| T0 | Current-source single-consumer and invocation-boundary decision | CLOSED_PASS_BOUNDED | independently accepted `NO_VIABLE_CONSUMER_RETAIN_PARKED` |
| T1 | Minimal export/composition and one non-test consumer | PARKED_NO_VIABLE_CONSUMER | fresh source must satisfy the historical four-fact reopen condition before a new packet is considered |
| T2 | Deterministic positive, fail-closed, concurrency, throw/reject, timeout, cancellation, and retry proof | HOLD_DEPENDENCY | accepted T1 material commit |
| T3 | Durable receipt/audit projection through an existing operator surface | HOLD_DEPENDENCY | accepted T2 evidence |
| T4 | Value, latency, failure, rollback, and system-chain map reconciliation | HOLD_DEPENDENCY | accepted T3 evidence |
| T5 | Optional bounded real-provider proof | PARKED_OPERATOR_CHECKPOINT | explicit fresh operator grant after T4; live standard applies |

No tranche self-authorizes its successor.

## Work Plan

1. T0 recomputes source and selects or rejects one consumer boundary.
2. The reviewer independently accepts, repairs, or parks the result.
3. A fresh packet may release T1 only if its value and exact manifest are
   accepted.
4. T2 through T4 remain sequential proof and reconciliation tranches.
5. T5 remains a separately parked operator checkpoint.

## T0 Terminal Tokens

T0 must select exactly one:

- `READY_FOR_T1_SINGLE_CONSUMER_COMPOSITION`
- `PARTIAL_READY_REQUIRES_INTERFACE_CHANGE`
- `NO_VIABLE_CONSUMER_RETAIN_PARKED`
- `BLOCKED_SOURCE_CONTRADICTION`

The first two tokens authorize reviewer consideration and possible T1 packet
authoring only. They do not authorize implementation.

## Acceptance Criteria

- Current committed source is used, not working-tree or historical inference.
- All five candidate families and all mandatory invariants are reconciled.
- Exactly one caller file/symbol or one exact proposed path set is selected,
  or the missing facts are stated precisely.
- The design prevents duplicate guard evaluation and duplicate provider
  admission/invocation by construction.
- A smallest T1 write manifest and focused test manifest are named.
- T0 changes only its audit and worker-return paths, makes zero provider calls,
  and leaves commit ownership to the reviewer.

## Verification / Evidence

T0 evidence is the exact architecture audit, the full worker return, current
Git/source searches, the pre-implementation autorun result, the worker-return
fast gate, unchanged worker HEAD, empty staged diff, and exact two-path status.
No local documentation evidence is treated as runtime invocation proof.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current private runtime source verification and independent CVF review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this private roadmap |
| Disposition | `BLOCKED_UNTIL_CVF_PROOF` for caller, runtime, or readiness claims |
| Claim boundary | The delegated execution surface does not convert worker opinion into CVF authority; independent review remains required. |

## Risk And Rollback

The highest architectural risk is wrapping the existing Web route with a
second execution pipeline, which could double-evaluate policy or double-call a
provider. T0 must reject any candidate that cannot assign a single owner to
each boundary. T1 rollback, if later released, must be a small Git-reversible
composition removal that restores the accepted pre-T1 route behavior.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Status`, `Design-Control Gate`, `Acceptance Criteria`, `Public Export Disposition`, dispatch-ready and claim-boundary terms |
| gateRunPurpose | Confirmation evidence after reading checker source, not first discovery of artifact requirements. |
| claimBoundary | Read-ahead confirms document shape only; it does not prove consumer viability or runtime behavior. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap is private provenance planning. Public export would add
no runtime proof and is not required to execute T0. No public-sync boundary,
public repository mutation, push, or deployment is authorized by this closure.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R1_T0_SINGLE_CONSUMER_BOUNDARY_DECISION_2026-08-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GC010_SCR_R1_T0_SINGLE_CONSUMER_BOUNDARY_DECISION_WORKER_RETURN_2026-08-30.md` | Independent Reviewer Addendum accepts `NO_VIABLE_CONSUMER_RETAIN_PARKED` | PASS |
| Roadmap state | this roadmap | `Status: CLOSED_PASS_BOUNDED`; T0 closed; T1 parked | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | exact baseline/work-order hashes regenerated from canonical state sources | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V59_2026-08-11.md` | separate continuity commit owns closed-mode narrative | BLOCKED with reason: material closure precedes continuity synchronization |
| External evidence digest | N/A with reason: no external evidence was consumed | zero provider/live/network/browser/credential calls | N/A with reason: local private-source decision only |
| System loop interlock | tranche table and terminal token | T1-T5 do not self-open; historical four-fact reopen condition remains binding | PASS |
| Session continuity | bootstrap/state/front door/handoff | exact authority hashes aligned; closed-mode synchronization follows material commit | N/A with reason: separate continuity commit required by commit choreography |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| Runtime receipt evidence | N/A with reason: documentation-only T0 creates no runtime receipt | N/A_WITH_REASON |
| Query acceptance evidence | N/A with reason: T0 performs no runtime query admission | N/A_WITH_REASON |
| Worker-return acceptance | Independent Reviewer Addendum accepts the parked decision after bounded repair | PASS |
| Closure claim | `CLOSED_PASS_BOUNDED` for the current-source architecture decision only | PASS |

## Claim Boundary

This roadmap records T0 as `CLOSED_PASS_BOUNDED` with terminal token
`NO_VIABLE_CONSUMER_RETAIN_PARKED`. It does not claim that GC-010 is invoked
by a production consumer, close the paired gap, authorize T1, modify runtime
source, permit provider use, or establish live, deployment, public, or
production readiness.
