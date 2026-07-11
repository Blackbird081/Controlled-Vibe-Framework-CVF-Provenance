# CVF MAO-T8 Representative End-To-End Pilot Worker Return

Memory class: FULL_RECORD

docType: review

Status: COMPLETE_PENDING_REVIEW

Date: 2026-07-11

Batch ID: MAO-T8

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_2026-07-11.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_2026-07-11.md`

dispatchBaseHead: `47ed44b12`

executionBaseHead: `9450f77fd`

closureBaseHead: TO_BE_CAPTURED_BY_REVIEWER_AT_CLOSURE

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Return the MAO-T8 representative end-to-end pilot for the selected task
`MAO-T8-LOCAL-STALE-READOUT-REPAIR`: one local deterministic task graph in
which a worker produces an operator evidence readout from seeded receipts,
an independent reviewer detects a deliberately stale readout by
recomputing freshness itself (never trusting the worker's readout content),
one classified revision regenerates the readout, and one designated closer
accepts only the resulting consistent terminal receipt chain. All five
required negative scenarios (self-approval, duplicate execution/admission,
timeout, cancel, budget ceiling) are proven to fail closed. No provider
call, network request, durable queue, UI, commit, workspace/session state
mutation, or MAO-T9 work was performed.

## Target / Source

Target: one new execution-plane MAO module
(`representative.pilot.contract.ts`), one focused test file
(`mao.representative.pilot.contract.test.ts`), a bounded barrel extension
(`src/mao/index.ts`), one pilot evidence packet, and this worker return.
Exactly five worker paths; no commit.

Source authority: paired work order
(`docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_2026-07-11.md`),
the GC-018 baseline
(`docs/baselines/CVF_GC018_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_2026-07-11.md`),
and the pilot selection checkpoint
(`docs/reviews/CVF_MAO_T8_REPRESENTATIVE_PILOT_SELECTION_CHECKPOINT_2026-07-11.md`).
The six cited MAO-T1/T4/T5/T6/T7 source files
(`task.graph.contract.ts`, `reviewer.isolation.contract.ts`,
`dissent.revision.contract.ts`, `closer.interlock.contract.ts`,
`lifecycle.controller.contract.ts`, `evidence.readout.contract.ts`) were
re-read fresh at this execution base; `evidence.readout.contract.ts` and
its test file were found already modified since T7 dispatch with an added
`TASK_GRAPH_ID_MISMATCH` rejection reason (T7 closure repair), which this
pilot's `runWorkerPhase` respects by always passing a matching
`taskGraphId`.

## Scope / Methodology

Read the mandatory startup sequence, the pilot selection checkpoint, the
GC-018 baseline's Source Verification Block, and the work order. Verified
MAO-T1 through T7 are accepted (dependency release evidence in both the
baseline and work order) and confirmed the T7 evidence/readout contract's
current state directly rather than relying on the prior T7 worker-return
snapshot, since the system noted it had been modified since that session.
Implemented one harness module composing existing contracts (no
reimplementation of any cited contract's semantics), one test file (24
cases across 10 describe blocks), a barrel extension, one evidence packet,
and this return. Ran TypeScript typecheck (PASS), focused Vitest (24/24
PASS after one test-timestamp repair), the governed file size guard
(COMPLIANT), and `git diff --check` (PASS with one harmless CRLF advisory).

## Exact Changed Set

4 code/evidence paths (plus this return, not yet written):

```
M  EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/representative.pilot.contract.ts
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.representative.pilot.contract.test.ts
?? docs/reviews/CVF_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_EVIDENCE_2026-07-11.md
```

Plus this worker return at:
`docs/reviews/CVF_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_WORKER_RETURN_2026-07-11.md`

## Verification Commands And Results

### TypeScript typecheck

Command: `npx tsc -p tsconfig.json --noEmit`

Result: PASS (no errors, clean exit, first run).

### Focused test execution

Command: `npx vitest run --config vitest.config.ts tests/mao.representative.pilot.contract.test.ts`

Result: PASS on second run. 24/24 tests pass across 10 describe blocks
(11ms test duration). First run failed 2 assertions due to a test-harness
timestamp defect (the intended stale-then-repaired scenario's revision and
second-review timestamps fell outside the 60-second freshness ceiling used
by the recomputed check, so the "repaired" readout still classified STALE);
repaired by moving those three timestamps closer to the seeded receipts'
`recordedAt` values. Full detail and the corrected timestamps are recorded
in the pilot evidence packet's Command-Backed Receipts section.

### Governed file size guard

Command: `python governance/compat/check_governed_file_size.py`

Result: COMPLIANT (0 violations; new T8 files do not appear in the
advisory list; 7729 governed files checked).

### Git diff whitespace check

Command: `git diff --check`

Result: PASS. Only a harmless LF/CRLF advisory for `index.ts` (same class
of advisory recorded in every prior MAO worker return).

## Test Coverage

The test file (`mao.representative.pilot.contract.test.ts`, 10 describe
blocks, 24 cases) covers:

### compilePilotGraph
- Compiles successfully at the pilot concurrency ceiling (3)
- Rejects a graph above the ceiling (4) with `BUDGET_CONCURRENCY_EXCEEDS_CEILING`

### runWorkerPhase
- Seeds the ledger in order and builds a readout
- Produces a deliberately stale readout when `generatedAt` is far past the last receipt

### runReviewerPhase
- Rejects self-approval when reviewer identity equals worker identity
- Excludes the worker output path from the isolated source packet
- Independently classifies STALE and requests repair
- Independently classifies CURRENT and accepts

### runCloserPhase
- Rejects an actor that is not the designated closer
- Rejects closing with zero review receipts

### Negative: self-approval
- Rejected end to end via `runReviewerPhase`

### Negative: duplicate execution/admission
- Second claim of the same idempotency key rejected without duplicate side effect
- Different keys are independent and both succeed

### Negative: timeout
- Classifies a terminal timed-out result and never infers success
- Does not time out under the ceiling, and still never infers success

### Negative: cancel
- Blocks new child admission once cancellation is accepted

### Negative: budget ceiling
- Rejects an over-ceiling graph before any task executes
- Does not reject a graph at the ceiling

### runPilotChain (full representative end-to-end chain)
- Compiles the graph successfully
- Detects the deliberately stale initial readout, requests exactly one repair
- Regenerates a fresh readout; second review accepts it
- Closes with a consistent terminal integration receipt only after acceptance
- Closes immediately with no revision when the initial readout is already fresh
- Deterministic replay: two independent chain runs produce the same closure receiptId

## Source Inventory

| File | Lines | Purpose |
|---|---|---|
| `src/mao/representative.pilot.contract.ts` | 315 | Pilot task graph, worker/reviewer/closer phases, five negative-scenario functions, full-chain orchestration |
| `tests/mao.representative.pilot.contract.test.ts` | 258 | Focused tests across 10 describe blocks, 24 cases |
| `src/mao/index.ts` | +33 lines | Bounded barrel exports for T8 module |
| `docs/reviews/CVF_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_EVIDENCE_2026-07-11.md` | new | Command-backed receipts and proof boundary |

## Delta Boundary

Only the four named worker paths (plus this return) were created or
modified. No provider/network call, real wall-clock, durable queue, UI,
workspace/session state, public-sync, root barrel, checker/hook, roadmap,
git mutation, MAO-T9, commit, push, or live proof was performed.

## Findings / Position

### Finding 1: Test-harness timestamp miscalibration (self-corrected)

The first draft of `runPilotChain` test invocations placed the revised
readout and second review far past the seeded receipts' `recordedAt`
values, so the recomputed freshness check classified the "repaired"
readout as still STALE - the test asserted a positive outcome the
timestamps themselves contradicted. This was a test-authoring defect, not
a `representative.pilot.contract.ts` source defect: the freshness
recomputation behaved correctly (STALE is the correct classification for
those timestamps). Repaired by recalibrating three timestamps to fall
within the freshness window.

Learning lane: GOVERNANCE_CONTROL_PLANE
Defect class: WORKER_EXECUTION_ERROR
Repair owner: worker (self-corrected before return)

### Finding 2: `PILOT_MAX_CONCURRENT_ROLES` is not exported by its owning module

The work order and baseline's Source Verification Block cite
`PILOT_MAX_CONCURRENT_ROLES` as a `LITERAL_INVARIANT` in
`task.graph.contract.ts`. This constant exists (value `3`, line 111 at
this execution base) but is a private module-scope constant, not exported.
The pilot harness therefore verifies the ceiling through
`compileTaskGraph`'s rejection behavior (`compilePilotGraph(4)` fails with
`BUDGET_CONCURRENCY_EXCEEDS_CEILING`; `compilePilotGraph(3)` succeeds)
rather than importing the constant directly. This satisfies the cited
invariant's behavioral claim without requiring an export-surface change to
an accepted T1 contract, which is out of this pilot's bounded scope.

Learning lane: GOVERNANCE_CONTROL_PLANE
Defect class: N/A_WITH_REASON
Repair owner: N/A with reason: behavioral verification is sufficient; no
source-contract export change is in scope for this pilot

### Finding 3: GC-051 corpus scan registry coverage gap (anticipated)

Following the pattern established in the MAO-T6 and MAO-T7 worker returns,
the new test file `mao.representative.pilot.contract.test.ts` is expected
to require a GC-051 registry source entry. Per the work order's Reviewer
Closure Conversion block (`reviewerOwnedClosurePaths: pilot packet,
evidence reconciliation, completion review`), this is reviewer-owned, not
worker-owned.

Learning lane: GOVERNANCE_CONTROL_PLANE
Defect class: ORCHESTRATOR_PACKET_GAP
Repair owner: reviewer

## Closure Diff Gate

| Requirement | Handling | Status |
|---|---|---|
| One worker-reviewer-revision-closer proof lane | `runPilotChain` orchestrates all four phases over existing T1/T4/T5/T7 contracts | IMPLEMENTED |
| Independent reviewer recomputation (not trusting worker readout) | `runReviewerPhase` recomputes `classifyReadoutFreshness` from the ledger, ignoring the passed-in readout's own content | IMPLEMENTED |
| Exactly one classified revision ceiling | MAO-T4 `checkRevisionCeiling` with `PILOT_MAX_REVISION_DEPTH=1` | IMPLEMENTED |
| Designated closer accepts only consistent terminal chain | MAO-T5 `checkCloserIdentity`/`makeIntegrationDecision`; non-terminal reviews block integration | IMPLEMENTED |
| Self-approval rejected | MAO-T4 `checkSelfApproval` via `runReviewerPhase` | IMPLEMENTED |
| Duplicate execution/admission rejected without duplicate side effect | MAO-T6 `createIdempotencyGuard`; second claim returns false | IMPLEMENTED |
| Timeout is terminal classified, never inferred success | MAO-T6 `detectTimeout`; `inferredSuccess` is always literal `false` | IMPLEMENTED |
| Cancel blocks new children once accepted | MAO-T6 cancel lifecycle | IMPLEMENTED |
| Budget ceiling rejected before over-budget execution | MAO-T1 `compileTaskGraph` `BUDGET_CONCURRENCY_EXCEEDS_CEILING` | IMPLEMENTED |
| Focused tests and typecheck pass | tsc clean; 24/24 Vitest pass | IMPLEMENTED |
| Exactly five paths, no commit | 4 code/evidence + 1 return, uncommitted | CONFIRMED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`,
role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Finding-To-Governance Learning Disposition

| Defect | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| Test-harness timestamp miscalibration | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | worker self-corrects before return (already applied) |
| GC-051 closure metadata | ORCHESTRATOR_PACKET_GAP | DOCUMENTATION_ONLY_LEARNING; runtime learning lane N/A with reason: metadata only | RULE_EXISTS | reviewer adds entry |

## Acceptance Receipt Assertion Matrix

| Assertion | Evidence |
|---|---|
| Reviewer never trusts worker readout content as freshness authority | `runReviewerPhase` recomputes `classifyReadoutFreshness` from the ledger at its own evaluation time, independent of the `readout` parameter's `generatedAt` |
| Exactly one revision occurs, never more | `runPilotChain` revision test: `revisionCount=1`; `PILOT_MAX_REVISION_DEPTH=1` bounds `checkRevisionCeiling` |
| Closer never accepts an unresolved chain | `runCloserPhase`/`makeIntegrationDecision` rejects non-terminal (`REQUEST_REPAIR`/`ESCALATE`) review decisions |
| Self-approval always rejected | equal worker/reviewer identity test |
| Duplicate admission never produces a second side effect | idempotency guard `seen()`/`claim()` sequence test |
| Timeout never infers success | `inferredSuccess` literal `false` assertion in both timed-out and not-timed-out cases |
| Cancel blocks children only after acceptance, not just request | tracker state `ACCEPTED` plus `mayStartAfterAccept=false` test |
| Budget ceiling enforced before execution | `compilePilotGraph(4)` rejected at compile time, before any task phase runs |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | local MAO-T8 representative pilot harness, tests, and evidence packet |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: local pure functions and in-memory contract composition only |
| actionEvidence | ACTION_EVIDENCE_PRESENT: 24/24 tests and typecheck PASS |
| invocationBoundary | local in-process contract calls only |
| interceptionBoundary | no provider, IDE, MCP, Web, wrapper, proxy, or runtime interception |
| claimLanguage | one representative deterministic local contract-composition proof only |
| forbiddenExpansion | real provider, network, durable queue, UI, public-sync, production readiness, MAO-T9 |

## Risk / Corrective Action

No repair to `representative.pilot.contract.ts` itself was required; the
one repair applied was to test-file timestamps, described in Finding 1.
Risk for reviewer attention: `runPilotChain` throws (rather than returning
a typed failure) if a review phase call unexpectedly returns
`outcome: null`, since that branch represents a programming-contract
violation (a malformed revision ledger or a first-review error the pilot
does not intend to reach) rather than an expected flow branch in a
deterministic local harness. The reviewer should confirm this fail-fast
behavior is acceptable for a pilot proof rather than expecting a typed
error result on every possible internal path.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_worker_experience_retrospective.py` |
| literalTokensReviewed | `REQUIRED_HEADINGS`, `SELF_DECLARE_MARKER`, `RESPONDS_MARKER`, `AOT_FIELDS`, `DELTA_FIELDS`, `PUBLIC_EXPORT_TOKENS`, `DELTA_RECEIPT_TOKENS`, `DELTA_ACTION_TOKENS`, `PREVENTIVE_CONTROL_CANDIDATES` enum, authority-reference full-path citation requirement |
| gateRunPurpose | reviewer confirmation |
| claimBoundary | local T8 pilot evidence only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker |
| Provider or surface | private workspace |
| Session or invocation | MAO-T8 representative pilot worker execution 2026-07-11 |
| Working directory | repository root/package |
| Command or tool surface | file writes, Vitest, tsc, governance gates |
| Target paths | four worker outputs plus this return |
| Allowed scope source | MAO-T8 work order |
| Before status evidence | clean execution HEAD `9450f77fd` |
| After status evidence | 24/24 tests and typecheck PASS |
| Diff evidence | `git diff --name-status` |
| Approval boundary | T8 only |
| Claim boundary | deterministic local pilot-composition mechanics only |
| Agent type | worker |
| Invocation ID | `mao-t8-representative-pilot-worker-2026-07-11` |
| Expected manifest | five worker paths (four code/evidence plus this return) |
| Actual changed set | same |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no external input |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | reviewer/closer |
| Disposition | no absorption |
| Claim boundary | CVF source only |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: no rescan/intake.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus completeness claim.

## Epistemic Process Block

### Expected Result / Prediction

The pilot chain would compile, exercise a stale-then-repaired readout
through independent review, close via one designated closer, and every
negative scenario would fail closed on the first correctly-calibrated test
run.

### Evidence Comparison

The chain, closer, and negative-scenario predictions were confirmed exactly
as expected. The stale-then-repaired timing prediction required one
timestamp correction (Finding 1) before the evidence matched the
prediction; the underlying contract behavior did not need correction.

### Contradiction Or Gap Disposition

The one contradiction (first test run) traced to test-harness timestamp
authoring, not to a defect in `representative.pilot.contract.ts` or any
cited T1-T7 contract. No gap in the underlying contracts was found.

### Claim Update

The representative worker-reviewer-revision-closer chain and all five
required negative scenarios are proven at the bounded deterministic local
level. Reviewer independent verification is required before broader claims.

## git status --short

```
 M EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/representative.pilot.contract.ts
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.representative.pilot.contract.test.ts
?? docs/reviews/CVF_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_EVIDENCE_2026-07-11.md
?? docs/reviews/CVF_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_WORKER_RETURN_2026-07-11.md
```

## Changed Files

Exactly five worker paths listed above; reviewer adds GC-051 coverage,
evidence reconciliation, and completion review per the work order's
Reviewer Closure Conversion block.

## Command Evidence

- Focused Vitest 24/24 PASS (second run, after timestamp repair).
- Typecheck PASS (first run).
- Governed file size guard COMPLIANT (0 violations).
- `git diff --check` PASS (one harmless CRLF advisory on `index.ts`).
- Worker-return fast gate: run and repaired to the reviewer-owned GC-051
  boundary, consistent with the MAO-T6/T7 precedent.

WORKER_EXPERIENCE_RETRO:

- frictionLevel: LOW
- frictionType: SCOPE_AMBIGUITY
- observedStep: first pilot-chain test run (timestamp calibration for the
  stale-then-repaired scenario)
- preventiveControlCandidate: NONE

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. Reviewer/designated closer owns closure
commit.

## Claim Boundary

This return claims deterministic local composition of the accepted MAO-T1
through T7 contracts into one representative pilot chain, plus fail-closed
behavior for five required negative scenarios. It does not prove real
provider behavior, network transport, durable queue behavior, UI,
concurrent multi-process execution, production orchestration readiness, or
public-sync readiness. Reviewer independent verification is required before
any of those broader claims may be made.
