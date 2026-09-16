# CVF ACEL G2 Topology Experiment T1 Result

Memory class: governed-experiment-result

Status: PROPOSAL_ONLY_READY_FOR_REVIEW

docType: experiment_result

Batch ID: ACEL-G2-TOPOLOGY-EXPERIMENT-T1

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_2026-09-16.md`

Paired baseline: `docs/baselines/CVF_GC018_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_2026-09-16.md`

executionBaseHead: `db9bfd775c8fc4bea2b4d230a2665cd115a5c731`

## Purpose

Report the observed hermetic result of the G2 runtime-topology decision-policy
oracle: exactly 32 proposal-only run records across eight fixtures, two
policies (`A_FIXED`, `B_DYNAMIC`) and two repetitions, with quality admission
preceding every cost comparison and the immutable authority envelope preserved
across every route decision. This report states a T2-readiness disposition
only; it does not itself accept the tranche or open T2.

## Target / Source

| Artifact | Role |
|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/runtime.topology.experiment.contract.ts` | isolated experiment contract (policies, invariants, admission, metrics) |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/runtime.topology.experiment.contract.test.ts` | 43 focused tests covering actions, policies, task classes, negative cases and determinism |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/fixtures/runtime.topology.experiment.tasks.v1.json` | eight-fixture corpus, two per task class |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/scripts/run-runtime-topology-experiment.ts` | hermetic runner producing the receipt below |
| `docs/audits/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_32_RUN_RECEIPT_2026-09-16.json` | machine receipt, this result's evidence |

## Scope / Methodology

The contract defines a closed `RouteAction` vocabulary (`NO_DELEGATE`,
`DELEGATE`, `PARALLELIZE`, `RECLAIM`, `ESCALATE`), an immutable
`AuthorityEnvelope`, a `RuntimeEvidenceInput` shape and a fail-closed legal
transition table. Policy A always returns the fixture's preselected topology
and ignores runtime evidence. Policy B is a pure deterministic function of
declared runtime evidence only (load factor, cross-module coupling,
independent-subtask count, prior-attempt-failed and executor-health flags) -
no clock, RNG, network or provider call is consulted. Every run first computes
quality admission (`evaluateQualityAdmission`): a run is `admitted=true` only
when the selected action equals its fixture oracle, all invariants pass, the
outcome oracle passes and critical defects are zero; `selectCheaperAdmittedRun`
filters to admitted runs before any cost comparison, so a cheaper unadmitted
run can never win. The runner loads the eight-fixture corpus, executes the
closed 8 x 2 x 2 matrix, asserts exactly 32 unique `(taskId, policy,
repetition)` keys and all five Policy B actions represented, and writes one
deterministic JSON receipt using a fixed `generatedAt` timestamp so re-running
the runner without source changes reproduces byte-identical output.

## Findings / Position

All 32 planned executions completed and were admitted (`admittedRunCount:
16/16` for each policy in the receipt's `aggregate` block). Policy B's 16 runs
collectively exercise all five actions: `NO_DELEGATE` (BR-01, LI-01, FF-02, x2
repetitions each), `DELEGATE` (BR-02, CR-01), `PARALLELIZE` (LI-02),
`RECLAIM` (FF-01) and `ESCALATE` (CR-02). The `NO_DELEGATE` outcomes are
recorded as positive, oracle-matching decisions rather than an absence of
delegation. No authority-envelope expansion, illegal transition, duplicate or
missing run, reclaim dual-write authority, or unknown-input case occurred in
the hermetic run; the corresponding negative-path tests (see Evidence
Requirements below) independently confirm each of those six fail-closed
behaviors throws `RuntimeTopologyExperimentError` rather than degrading
silently.

Policy B's aggregate `meanDeterministicIntegrationEffort` (8.25) is higher than
Policy A's (3.625) in this hermetic fixture set, because the fixtures were
authored to exercise every Policy B action at least once, which biases toward
higher-effort actions (`DELEGATE`, `PARALLELIZE`, `RECLAIM`, `ESCALATE`) more
often than a representative task mixture would. This is expected given the
coverage-first fixture design and is not read as evidence that either policy
is cheaper in general; see Claim Boundary.

## Risk / Corrective Action

No corrective action is required: every acceptance criterion in the governing
work order was met on the first runner execution. The reviewer should
independently resample at minimum the six fail-closed negative-path tests
(authority-envelope expansion, illegal transition, reclaim dual-write
authority, duplicate run, missing run, unknown input) and the two-run
byte-identical receipt comparison before treating this tranche as accepted,
per `EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`.

## T2 Readiness Disposition

`READY_FOR_REVIEW`

This disposition covers only the hermetic decision-policy oracle and its
receipt integrity. It does not recommend production adoption of dynamic
runtime topology, does not claim real-agent task-outcome improvement, and does
not itself authorize a T2 real-agent work order. T2 remains a separate,
Local-authorized dispatch.

## Evidence Requirements (Cross-Reference)

- Fixture identities and execution base: `executionBaseHead` and
  `fixtureManifestHash` are recorded in the receipt header (see Command
  Evidence in the paired worker return for literal values).
- All five Policy B actions represented by a correct fixture oracle: receipt
  `actionsRepresented` array and per-fixture `dynamicOracleAction` fields.
- Authority-envelope, illegal-transition and reclaim-exclusivity negative
  tests: `runtime.topology.experiment.contract.test.ts` describe blocks
  "Authority envelope invariants (fail closed)", "Legal transition table
  (fail closed)" and "Reclaim dual-write exclusivity (fail closed)".
- Quality admission precedes all economic comparison:
  `evaluateQualityAdmission` runs before `computeOrchestrationMetrics` in
  `runOne`, and `selectCheaperAdmittedRun` filters to `admitted` records
  before any cost comparison; covered by the "never lets a cheaper unadmitted
  run win" test.
- Exact test counts, command exits, receipt hashes and eight-path status: see
  the paired worker return's Command Evidence section.

## Claim Boundary

This result reports a bounded, hermetic decision-policy oracle execution only.
It makes no claim that dynamic (`B_DYNAMIC`) runtime topology outperforms
fixed (`A_FIXED`) topology for real agent work, authorizes no actual subagent,
provider or network execution, changes no production delegation or routing
owner, and is not exported through any production barrel. Only Local review
may accept this tranche or authorize a separate T2 real-agent work order.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private experimental result; no public-sync authority.
