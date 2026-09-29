# CVF ACEL G2 T2 Real-Agent Experiment Design

Memory class: governed-experiment-design

docType: experiment_design

Status: BLOCKED_NO_QUALIFIED_CANDIDATE

Batch ID: ACEL-G2-T2-REAL-AGENT-EXPERIMENT-DESIGN

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_2026-09-16.md`

Paired baseline: `docs/baselines/CVF_GC018_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_2026-09-16.md`

Machine manifest: `docs/audits/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_MANIFEST_2026-09-16.json`

executionBaseHead: `6c81c575957d0a7eba416eaa5c8a442e0891e443`

## Purpose

Produce a source-backed, execution-ready design for a bounded ACEL G2 T2
fixed-versus-dynamic real-agent topology experiment without executing it, per
the governing work order. Determine whether an accepted harder task and a
truthful current composition seam exist. This design does not itself
execute anything, call a provider, invoke an agent/subagent, or access a
credential; it reports zero external effects.

## Target / Source

Nine source artifacts were fully read and terminally accounted (see the
machine manifest's `sourceLedger` for exact SHA-256 hashes and byte counts):

| # | Path | Role |
|---|---|---|
| 1 | `docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_COMPLETION_2026-09-16.md` | T1 acceptance and claim ceiling |
| 2 | `docs/audits/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_RESULT_2026-09-16.md` | T1 result and T2-readiness disposition boundary |
| 3 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/runtime.topology.experiment.contract.ts` | T1 executable decision contract |
| 4 | `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md` | prior live comparison roadmap and reopen conditions |
| 5 | `docs/reviews/CVF_MAO_LIVE_T1_PROVIDER_ADAPTER_VALUE_PILOT_COMPLETION_2026-07-12.md` | prior live comparison result (VALUE_NOT_PROVEN) |
| 6 | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts` | existing live comparison bridge |
| 7 | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | existing durable operational launcher |
| 8 | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | existing Model Gateway live-call harness |
| 9 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | existing provider-execution grant evaluator |

Nine-source reconciliation: `manifestCount=9; ledgerTerminalCount=9;
exclusions=0; unresolved=0`. No fact in this design relies on provider-local
memory, chat history, or external synthesis; every claim below cites one of
the nine rows or is marked source-not-found.

## Scope / Methodology

Read-only source and evidence audit followed by one bounded design decision.
For each of the ten required design questions in the work order, the
governing fact and its source row are stated below. No source, test,
runtime, package, checker, or session-state file was modified. No agent,
subagent, or provider was invoked; no credential or `.env.local` was read.

## Findings / Position

### 1. Real execution owner

No current source symbol consumes the T1 `RouteAction` decision output.
`rg`-equivalent search across all TypeScript files below `EXTENSIONS` for
`RouteAction|decideRouteAction|runtime.topology.experiment.contract` returns
exactly three files: the T1 contract itself, its own test file, and its own
runner script (source row 3). The contract is not exported through
`src/index.ts` or any `*.barrel.ts` in Control Plane Foundation. **Disposition:
GAP - no execution owner exists.**

### 2/3. Control policy (`A_FIXED`) and treatment policy (`B_DYNAMIC`)

Both policies are well-defined at the decision-contract level (source row 3):
`A_FIXED` always returns the fixture's preselected topology; `B_DYNAMIC` is a
pure deterministic function of declared runtime evidence with zero clock/RNG/
network/provider dependency, and `AuthorityEnvelope.providerExecutionAuthority`
is typed to always equal `"FORBIDDEN"`. Both policies are designable without
authority expansion. **Disposition: DESIGNABLE, but see Composition Gap below
- no execution owner currently reads either policy's output.**

### 4. Candidate task

**No accepted candidate in the bounded nine-source corpus satisfies the
admission rule.** The one source-backed task in that corpus was reviewed
against the canonical rule (accepted local direct-lane evidence at most
80/100 or one explicit rubric-defined material defect):

- `MAO-LIVE-T1` prime-number task (source rows 4, 5): both lanes scored
  100/100. This is the closed easy task the work order and roadmap explicitly
  forbid reusing. **EXCLUDED_DUPLICATE.**
The exact-path corpus contains no accepted harder-candidate receipt. This is a
bounded corpus conclusion, not a claim that every historical CVF artifact was
searched. Under the work order, missing admitted evidence is sufficient to
stop rather than widen the corpus or manufacture readiness. **Disposition:
BLOCKED_NO_QUALIFIED_CANDIDATE.**

### 5. Independent grading

Design-only (no candidate to grade). The existing pattern to reuse is
`scoreAgainstRubric` in `live.provider.value.pilot.ts` (source row 6): a
deterministic local rubric recomputed from received response text, never a
second live judge call and never worker self-report. This pattern satisfies
the work order's grader-independence requirement and should be reused, not
reinvented, if a qualified candidate is later admitted.

### 6. Randomization/order control

Design-only. Predeclare lane order (`A_FIXED` first, then `B_DYNAMIC`, or a
fixed seed) before any future call; freeze task prompt, rubric, authority,
model/provider lane, temperature/options and budgets; no adaptive prompt
tuning after observing either lane. No execution occurred to control.

### 7. Cost accounting

Design-only ceiling, reusing the existing `MaoLiveCallLedger` pattern (source
row 6): maximum four provider calls, maximum one treatment revision,
input/output token evidence required per call (unknown is never recorded as
zero), wall-clock latency per lane plus orchestration-only overhead, and a
50-percent latency-overhead ceiling.

### 8. Five-action owner/disposition table

| Action | Owner | Disposition |
|---|---|---|
| `NO_DELEGATE` | none | GAP - would map to the direct lane in `live.provider.value.pilot.ts` if wired, but no wiring exists |
| `DELEGATE` | none | GAP - would map to `runMaoLane`'s single worker call if wired, but no wiring exists |
| `PARALLELIZE` | none | EXCLUDED_WITH_REASON - neither MAO call surface exposes concurrent multi-executor fan-out; `operational.worker.launcher.ts` delegation reservation is sequential parent/child capacity accounting, not parallel execution |
| `RECLAIM` | none | EXCLUDED_WITH_REASON - `operational.worker.launcher.ts`'s `reconcileDelegation` recovers a durable reservation after a crash, a different semantic from T1's dual-write-exclusive mid-run executor handoff; treating them as equivalent would be an unsupported inference |
| `ESCALATE` | none | GAP - would map to `runMaoLane`'s one-revision repair path if wired, but no wiring exists, and no action may expand risk ceiling, sandbox, provider grant, or call ceiling in any case |

Silence is not used for any action; every row states an owner or an explicit
exclusion with reason, per the work order's requirement.

### 9. What stops the run / what evidence may never be interpreted as success

Hard stops (design-only, reusing the roadmap's existing stop rules from
source row 4): grant denial, secret exposure, authority drift, incomplete
receipt, ambiguous grader output, retryable failure without diagnosis, or any
required fifth call. No repeat solely to obtain a preferred result. A tie or
a loss on the independent rubric is never interpreted as `B_DYNAMIC` value,
matching the precedent already set by `decideValueVerdict` in source row 6
(`VALUE_PROVEN` requires a strictly higher MAO-lane score, not a tie).

### 10. Exact paths a later implementation/execution packet would own

Not applicable. No next-manifest paths are proposed because
`DESIGN_READY_FOR_SEPARATE_EXECUTION_WORK_ORDER` requires all dependency and
admission rows to pass, and candidate admission fails. Proposing execution
paths without an admitted candidate would be exactly the kind of "invented
readiness" the work order's Epistemic Process Block forbids.

## Composition Graph

`T1_POLICY_DECISION -> TOPOLOGY_ACTION_CONSUMER`: **GAP** (no consumer of
`RouteAction`/`decideRouteAction` exists outside T1's own three files).

`TOPOLOGY_ACTION_CONSUMER -> MAO_LAUNCHER_OR_LIVE_BRIDGE`: **GAP** (no
consumer exists to name; the two candidate MAO call surfaces -
`operational.worker.launcher.ts`'s `MaoOperationalAdapterPort.invoke` and
`live.provider.value.pilot.ts`'s `runDirectLane`/`runMaoLane` calling
`runLiveProof` - are structurally distinct with no shared topology-action
parameter).

`MAO_LAUNCHER_OR_LIVE_BRIDGE -> MODEL_GATEWAY (runLiveProof)`:
**PRESENT_FOR_LIVE_BRIDGE_ONLY** (only `live.provider.value.pilot.ts` calls
`runLiveProof`; the operational launcher calls a separate adapter port).

`MODEL_GATEWAY -> GRADER`: **PRESENT** (`scoreAgainstRubric` is deterministic
and independent of the worker under test).

`GRADER -> RECEIPT -> LOCAL_REVIEW`: **PRESENT** for the closed MAO-LIVE-T1
precedent (source row 5), whose accepted Local review carries a secret-safe
machine receipt.

No edge is inferred from source existence alone. The full graph with cited
evidence per edge is in the machine manifest's `compositionGraph` object.

## Risk / Corrective Action

The principal risk this design guards against is exactly the one the
governing baseline named: collapsing "T1 can decide an action" and "the
operational launcher has durable behavior" into "a real-agent topology
experiment can run today." Both are true in isolation; neither implies the
other is wired to it. This design does not make that inference. A secondary
risk - reusing the MAO-LIVE-T1 100/100 task to manufacture false candidate
readiness - is explicitly rejected in the Candidate Admission section above.

No corrective action is available inside this tranche: reopening requires a
fresh, separately authorized candidate-qualification pass (see Next Allowed
Move below), which is outside this work order's read-only design scope and
would itself require a live provider call this tranche is forbidden from
making.

## Terminal Disposition

**`BLOCKED_NO_QUALIFIED_CANDIDATE`**

This is the correct one of the four allowed terminal dispositions because:
`DESIGN_READY_FOR_SEPARATE_EXECUTION_WORK_ORDER` requires all dependency and
admission rows to pass, and candidate admission fails (Findings item 4);
`REJECT_DUPLICATE_MAO_LIVE_T1` does not apply because this design does not
attempt to reuse or reopen the MAO-LIVE-T1 task, it correctly excludes it;
`BLOCKED_RUNTIME_COMPOSITION_GAP` is a real, independently true finding (see
Composition Graph) but is not the controlling blocker, because even a fully
composed runtime seam would still have no qualified task to run it against.
Candidate admission is the harder, prior-in-sequence blocker and is named as
the terminal disposition.

## Next Allowed Move

Reopen requires, in this order: (1) a fresh, separately operator-authorized
candidate-qualification pass that produces one accepted local direct-lane
score at or below 80/100, or one predeclared rubric-defined material defect,
with evidence sufficient for independent rescoring; (2) only after such a
candidate is accepted, a separate design/implementation packet that also
resolves the `BLOCKED_RUNTIME_COMPOSITION_GAP` finding by naming and building
the exact callable seam between the T1 decision contract and one MAO call
surface. Neither step is authorized by this tranche.

## Claim Boundary

This design reports a bounded, read-only source audit and one terminal
parked disposition. It makes no claim that dynamic topology improves
real-agent outcomes, that any current MAO/Model Gateway owner is composed
with the T1 decision contract, or that a qualified candidate task exists. It
authorizes no agent/subagent execution, provider/live call, credential
access, runtime/production mutation, or public sync. Only Local review may
change this disposition, and only after new accepted evidence is created
through a separately governed work order.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private G2-T2 experiment design; no public-safe artifact is authorized.
