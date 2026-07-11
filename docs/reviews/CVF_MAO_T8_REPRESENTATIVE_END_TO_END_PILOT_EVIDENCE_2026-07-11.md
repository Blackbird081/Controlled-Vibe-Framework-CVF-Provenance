# CVF MAO-T8 Representative End-To-End Pilot Evidence

Memory class: FULL_RECORD

docType: review

Status: EVIDENCE_RECORDED

Date: 2026-07-11

Batch ID: MAO-T8

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_2026-07-11.md`

executionBaseHead: `9450f77fd`

## Purpose

Record command-backed receipts and the proof boundary for the selected
pilot task `MAO-T8-LOCAL-STALE-READOUT-REPAIR`, per
`docs/reviews/CVF_MAO_T8_REPRESENTATIVE_PILOT_SELECTION_CHECKPOINT_2026-07-11.md`.
This packet is evidence for the worker return, not a substitute for it.

## Target / Source

Target: one new execution-plane pilot harness module
(`representative.pilot.contract.ts`) that composes the accepted MAO-T1
through T7 contracts into one worker/reviewer/revision/closer chain plus
five negative scenarios, without redefining any of their semantics.

Source: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_2026-07-11.md`;
`docs/baselines/CVF_GC018_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_2026-07-11.md`;
`docs/reviews/CVF_MAO_T8_REPRESENTATIVE_PILOT_SELECTION_CHECKPOINT_2026-07-11.md`;
the Source Verification Block entries in the work order/baseline
(`compileTaskGraph`'s `PILOT_MAX_CONCURRENT_ROLES`, `checkSelfApproval`,
`classifyReadoutFreshness`, `checkRevisionCeiling`, `checkCloserIdentity`,
`detectTimeout`), each re-read fresh at this execution base.

## Scope / Methodology

Read the pilot selection checkpoint's task/proof-class decision and required
negative scenarios, the GC-018 baseline's Source Verification Block, and the
work order. Re-read the six cited MAO-T1/T4/T5/T6/T7 source files at this
execution base to confirm every cited symbol still exists with the claimed
behavior before writing any orchestration code. Implemented one harness
module exposing a `runPilotChain` orchestration function plus five standalone
negative-scenario functions, then one test file exercising the chain and
every negative. Ran TypeScript typecheck and the focused Vitest target.

## Command-Backed Receipts

### TypeScript typecheck

Command: `npx tsc -p tsconfig.json --noEmit` (run from
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION`)

Result: PASS (clean exit, no errors).

### Focused test execution

Command: `npx vitest run --config vitest.config.ts tests/mao.representative.pilot.contract.test.ts`

Result: PASS. 24/24 tests pass across 10 describe blocks (11ms test
duration). First run surfaced 2 failing assertions from miscalibrated test
timestamps (a revision-and-second-review window that itself exceeded the
60-second staleness ceiling, contradicting the intended "revision repairs
staleness" scenario); repaired by moving the revised-readout and
second-review timestamps to within the freshness window of the seeded
receipts. Second run: 24/24 PASS.

### Governed file size guard

Command: `python governance/compat/check_governed_file_size.py`

Result: COMPLIANT (0 violations; 7729 governed files checked).

### Git diff whitespace check

Command: `git diff --check`

Result: PASS. One harmless LF/CRLF advisory on `index.ts`, consistent with
the same class of advisory recorded in every prior MAO worker return.

## Findings / Position

### Representative chain proof

| Chain step | Contract used | Evidence |
|---|---|---|
| Task graph compiled | MAO-T1 `compileTaskGraph` | `compilePilotGraph` test: 2 tasks, worker depends-on none, reviewer depends-on worker |
| Worker produces readout from seeded receipts | MAO-T7 `MaoEvidenceLedger`/`buildEvidenceReadout` | `runWorkerPhase` test: 3 receipts ingested in order, `totalReceipts=3` |
| Reviewer independently recomputes freshness (never trusts worker's readout content) | MAO-T7 `classifyReadoutFreshness` recomputed against the same ledger at the reviewer's own evaluation time | `runReviewerPhase` STALE/CURRENT tests |
| Reviewer isolation | MAO-T4 `buildIsolatedSourcePacket` excludes `pilot/readout.json` | isolated-packet test asserts excluded path present |
| One classified revision | MAO-T4 `checkRevisionCeiling`/`recordReviewInLedger` (ceiling=1) | `runPilotChain` revision test: `revisionCount=1` after exactly one `REQUEST_REPAIR` |
| Closer accepts only a consistent terminal chain | MAO-T5 `checkCloserIdentity`/`makeIntegrationDecision` | closer test: `receipt.decision=ACCEPT`, `closerActorId` matches designated closer |

### Negative scenario proof

| Scenario | Required result | Evidence |
|---|---|---|
| self-approval | rejected | `runReviewerPhase` with equal worker/reviewer identity returns `outcome: null`, error contains "self-approval is forbidden" (MAO-T4 `checkSelfApproval`) |
| duplicate execution/admission | rejected without duplicate side effect | `runDuplicateAdmissionNegative`: second `claim()` on the same key returns `false`; the guard's `seen()` stays `true` (MAO-T6 `createIdempotencyGuard`) |
| timeout | terminal classified result, never inferred success | `runTimeoutNegative`: `timedOut` is a classified boolean from `detectTimeout`; `inferredSuccess` is the literal `false` in every case (MAO-T6 `detectTimeout`) |
| cancel | no new child starts after accepted cancellation | `runCancelNegative`: after `acceptCancel`, `mayStartNewChild` returns `false` (MAO-T6 cancel lifecycle) |
| budget ceiling | graph/invocation rejected before over-budget execution | `runBudgetCeilingNegative`: `maxConcurrentRoles=4` is rejected at compile time with `BUDGET_CONCURRENCY_EXCEEDS_CEILING`, before any task runs (MAO-T1 `compileTaskGraph`) |

## Proof Boundary

This pilot proves deterministic local composition of existing MAO-T1
through T7 contracts under one representative task, plus fail-closed
behavior for the five required negative scenarios. It does not prove:
real provider behavior, network transport, a durable/persistent queue, a
UI, concurrent multi-process execution, production throughput, or
public-sync readiness. `PILOT_MAX_CONCURRENT_ROLES` (task graph contract,
private module constant, value `3`) was verified present and enforced via
its rejection behavior (`compilePilotGraph(4)` fails,
`compilePilotGraph(3)` succeeds) rather than imported directly, since the
constant is not exported by its owning module.

## Risk / Corrective Action

No repair was required to the pilot harness source itself. The test-file
timestamp miscalibration described under Command-Backed Receipts was
corrected before the second (passing) run. Risk for reviewer attention: the
pilot harness's `runPilotChain` throws (rather than returning a typed
failure) when a review phase call returns `outcome: null` unexpectedly,
since that path is reserved for programming-contract violations (e.g. a
malformed revision ledger state) rather than an expected pilot-flow branch;
this is intentional fail-fast behavior for a deterministic local harness,
not a runtime error-handling gap, but the reviewer should confirm this
matches the intended pilot proof boundary.

## Decision / Recommendation / Disposition

Disposition: EVIDENCE_RECORDED. Recommend the reviewer treat this packet as
command-backed evidence supporting the worker return's Findings / Position
section, and independently rerun the focused test target plus typecheck
before accepting closure.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`,
role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | review-docType heading groups (target/source, scope/methodology, findings/position, risk/corrective action, decision/recommendation/disposition); full Agent Operation Trace Block label set; Epistemic Process Block four subsections |
| gateRunPurpose | confirmation ahead of worker-return fast gate |
| claimBoundary | pilot evidence record only; no runtime, provider, or production claim |

## Epistemic Process Block

### Expected Result / Prediction

A deliberately stale initial readout would be independently detected by the
reviewer's own recomputation (not by trusting the worker's readout), trigger
exactly one classified revision, and the revised readout would then be
accepted, producing one consistent terminal integration receipt. All five
negative scenarios would fail closed without executing any forbidden
side effect.

### Evidence Comparison

Confirmed on the second test run (24/24 PASS): `initialFreshness=STALE`,
`firstReview.terminal.decision=REQUEST_REPAIR`, `revisionCount=1`,
`revisedFreshness=CURRENT`, `secondReview.terminal.decision=ACCEPT`,
`closeOutcome.receipt.decision=ACCEPT`. All five negative scenarios
returned their required rejected/blocked/never-inferred-success result.

### Contradiction Or Gap Disposition

The first test run contradicted the prediction only due to a test-harness
timestamp defect (the revision/second-review window itself fell outside the
freshness ceiling), not a pilot-harness source defect. Repaired by
recalibrating test timestamps; no source-contract change was needed.

### Claim Update

The representative chain and all five negative scenarios are proven at the
bounded local deterministic level described in Proof Boundary above.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker |
| Provider or surface | private workspace |
| Session or invocation | MAO-T8 pilot evidence recording 2026-07-11 |
| Working directory | repository root/package |
| Command or tool surface | file writes, Vitest, tsc, governance gates |
| Target paths | this evidence packet |
| Allowed scope source | MAO-T8 work order Work-Order Fulfillment Manifest |
| Before status evidence | clean execution HEAD `9450f77fd` |
| After status evidence | 24/24 tests and typecheck PASS |
| Diff evidence | `git diff --name-status` |
| Approval boundary | T8 evidence recording only |
| Claim boundary | deterministic local pilot proof only; no provider/production claim |
| Agent type | worker |
| Invocation ID | `mao-t8-pilot-evidence-2026-07-11` |
| Expected manifest | this evidence packet |
| Actual changed set | this evidence packet |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This packet records command-backed pilot evidence only. It does not claim
provider behavior, network transport, durable queue readiness, UI,
production orchestration readiness, or public-sync readiness. Reviewer
independent verification is required before acceptance.
