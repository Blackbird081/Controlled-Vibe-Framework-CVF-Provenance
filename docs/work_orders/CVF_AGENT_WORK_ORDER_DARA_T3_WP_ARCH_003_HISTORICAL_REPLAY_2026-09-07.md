# CVF Agent Work Order - DARA-T3 WP-ARCH-003 Historical Replay

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-07

Batch ID: DARA-T3-WP-ARCH-003-HISTORICAL-REPLAY

Dispatch base head: `42ba4db4311e98d6401e25989f392533765f0a54`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: bounded external historical-replay worker. The operator manually relays
this committed packet; the orchestrator/reviewer does not invoke any external
agent through CLI or MCP.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_2026-09-07.md`.

Paired baseline: `docs/baselines/CVF_GC018_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_2026-09-07.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: DARA-T2B is `CLOSED_PASS_BOUNDED` through material
`e601523cd` and continuity `42ba4db43`. This is a new DARA-T3 parent
assignment with external usage 0 before execution and ceiling 1.

Do-not-misread notes: this is counterfactual offline replay, not
`WP-ARCH-003` acceptance or implementation. Do not edit historical inputs,
active DARA checkers, roadmap, baseline, this work order, session state,
hooks, runtime, provider, public or deployment surfaces.

Required first actions: acknowledge startup authority; capture exact HEAD and
clean status; read the paired baseline, this order, all seven frozen sources,
guard orientation and checker sources; recompute all seven hashes; run the
pre-implementation gate; then create only the five named outputs.

Return contract: freeze fixture and ledger before first replay; execute the
focused tests and two deterministic runs; leave all changes uncommitted; return
`COMPLETE_PENDING_REVIEW`, `RETURN_TO_DESIGN`, or `BLOCKED_WITH_REASON`.

## Purpose

Implement and run the DARA-T3 deterministic historical replay defined by the
paired baseline. Prove whether current architecture-readiness admission would
stop the observed Initial/R1/R2 failure classes before avoidable external
invocations, with explicit false-negative accounting and no post-result tuning.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: EXTERNAL_AGENT_CLI_MCP

parentAssignmentId: DARA-T3-WP-ARCH-003-HISTORICAL-REPLAY

reviewRoundCount: 0

priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH

dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH

newIndependentCriticalEvidence: NONE

regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 1

usageAvailability: KNOWN_FOR_ADMISSION

quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING

nextDispatchDisposition: INITIAL_DISPATCH

rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH

reworkGeneration: 0

consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "dara-t3-wp-arch-003-historical-replay",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["historical-replay-not-yet-proven"],
    "reopened": [],
    "current": ["historical-replay-not-yet-proven"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "DARA-T3-DISPATCH",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/baselines/CVF_GC018_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_2026-09-07.md"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

The worker return is ordinal 1, binds this committed work order's SHA-256 and
resolves the blocker only with `EXECUTABLE_PROOF`. No successor opens.

## Worker Autonomy / No-Question Rule

Repair allowed-scope defects directly. Return to the orchestrator only when a
frozen source hash drifts, a sixth path or active-checker edit is required, a
zero-tolerance case cannot be represented without inventing evidence, or a
forbidden external/runtime action would be necessary.

## Agent Roles

| Role | Responsibility | Forbidden overlap |
|---|---|---|
| Operator | manually relay the committed packet and the worker's textual return | does not author or accept worker evidence |
| External worker | create and verify only the exact five worker-owned paths | no commit, self-acceptance, continuity edit or scope expansion |
| Orchestrator/reviewer/closer | evaluate returned evidence, run bounded independent checks, decide acceptance and own commits | does not recreate the implementation or the full case analysis |

## Required First Reads

1. This work order and the paired GC-018 baseline in full.
2. `CVF_SESSION_MEMORY.md`, the bootstrap read model and the active handoff.
3. `docs/reference/guard_orientation/README.md` and the literal-format gotchas.
4. All seven artifacts in the baseline's Frozen Replay Source Set.
5. Applicable DARA schema/helper and checker sources before writing code.

## Pre-Flight Checks

1. Record exact HEAD and confirm a clean worktree before any edit.
2. Confirm the committed dispatch HEAD is an ancestor of the execution HEAD.
3. Recompute all seven frozen SHA-256 values; any mismatch fails closed.
4. Confirm all five fulfillment paths are absent and no collision exists.
5. Run the required pre-implementation gate before creating outputs.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator fresh continuation | operator continuation message, 2026-09-07 | ACCEPT |
| DARA roadmap T3 row | `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md` | ACCEPT |
| accepted T2B closure | `docs/reviews/CVF_DARA_T2B_INTERNAL_RECOVERY_COMPLETION_REVIEW_2026-09-07.md`; `483176267`, `11b6e579b`, `e601523cd` | ACCEPT |
| paired GC-018 baseline | `docs/baselines/CVF_GC018_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_2026-09-07.md` | ACCEPT |
| execution anchor | worker captures committed dispatch HEAD and clean status | REQUIRED_AT_EXECUTION |

## Scope / Target / Owner Boundary

Create exactly five artifacts named below. Read-only imports from the accepted
DARA helper modules are allowed. Do not alter current admission behavior,
historical evidence or any active project/runtime surface.

The fixture and ledger must be frozen before first replay. The worker may not
tune expectations after observing output. If a fixture defect is found after
the freeze, stop and report it rather than modifying the frozen files.

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_EXTERNAL_LOW_RISK_WITH_REASON:OFFLINE_REPLAY_OF_FROZEN_INPUTS_NO_ACTIVE_GUARD_WIRING

Reason: exact-five reversible, provider-free test/evidence work; all owners,
paths, source identities, cases and stop conditions are frozen by the paired
baseline. No authority, runtime registration, external adapter or production
composition is created.

## Work-Order Fulfillment Manifest

| Path | Action | Required proof |
|---|---|---|
| `governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json` | CREATE | seven hashes, three raw cases, at least nine seeded cases, frozen expectations |
| `governance/compat/dara_t3_historical_replay.py` | CREATE | deterministic read-only API/CLI; normalized JSON; no arbitrary execution |
| `governance/compat/test_dara_t3_historical_replay.py` | CREATE | drift, earliest-stop, zero-tolerance, idempotence and malformed-fixture coverage |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_LEDGER_2026-09-07.md` | CREATE | pre-run fixture/ledger hashes and full result reconciliation |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-07.md` | CREATE | full return, commands, exact diff and terminal disposition |

Forbidden paths: every path not listed above. In particular, do not modify
the baseline, work order, roadmap, existing DARA sources/tests, historical
inputs, `WP-ARCH-003` files, hooks, state, handoff or public-sync files.

## Write Ownership

The worker owns only the five manifest paths while they remain uncommitted.
The reviewer/closer owns acceptance, any reviewer addendum, staging, material
commit and later continuity sync. Simultaneous edits are forbidden.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order binding | Verification | Status |
|---|---|---|---|
| replay Initial/R1/R2 | exactly three raw historical cases bound to frozen sources S01-S03 | ledger rows and helper JSON | MAPPED |
| test known dispatcher-created defect classes | ten named seeded families derived from S04-S05 | fixture plus zero-tolerance matrix | MAPPED |
| measure avoided external invocations | earliest-stop and invocation-ordinal accounting per raw case | result reconciliation | MAPPED |
| preserve reviewer non-duplication | reviewer samples evidence and reruns focused checks only | reviewer strategy and return contract | MAPPED |
| choose one terminal T3 outcome | `REPLAY_BLOCKS_AVOIDABLE_INVOCATIONS` or `RETURN_TO_DESIGN` | reviewer-owned completion decision | MAPPED |
| do not open DARA-T4 or WP implementation | explicit claim and operator-checkpoint boundaries | changed-path proof | MAPPED |

## Replay Acceptance Matrix

| ID | Obligation | Required outcome |
|---|---|---|
| T3-A01 | seven frozen source hashes | 7/7 exact before fixture creation and again at return |
| T3-A02 | raw historical dispatches | Initial/R1/R2 each produces a recorded pre-invocation DARA stop; no retroactive validity claim |
| T3-A03 | seeded cases | at least twelve total cases and all ten named defect families represented |
| T3-A04 | earliest-stop accounting | exact invocation ordinal and avoided-invocation count per raw case; aggregate reconciles |
| T3-A05 | zero-tolerance recall | 100%; any miss returns `RETURN_TO_DESIGN` |
| T3-A06 | false positives/negatives | explicit row for every case; no omitted or averaged failure |
| T3-A07 | freeze integrity | fixture and ledger hashes recorded before first replay and unchanged afterward |
| T3-A08 | determinism | two consecutive normalized result files/streams are byte-identical |
| T3-A09 | scope | exact five paths, no active checker edits, staging empty, worker commit absent |
| T3-A10 | quota | external invocation count becomes 1/1; providerCallCount remains 0 |

## Execution Plan

1. Complete preflight and freeze the source inventory.
2. Create the fixture and ledger with expectations, then record their hashes.
3. Create the read-only replay helper and focused tests without active wiring.
4. Run all focused verification, including two byte-identical normalized runs.
5. Reconcile every case and write the no-commit worker return.

## Implementation Requirements

1. Use Python standard library unless an already-installed repository
   dependency is necessary; do not install packages.
2. Resolve paths relative to repository root and reject traversal/absolute
   fixture paths.
3. Read source bytes and verify SHA-256 before evaluating any case.
4. Reuse public functions from the accepted DARA schema/checker modules where
   practical; do not copy a second semantic validator.
5. The helper may evaluate strings/structured fixtures only. It must not
   execute shell commands, import the historical work orders as code, access
   network/provider/credentials or mutate source files.
6. Emit schema-versioned JSON with case totals, dispositions,
   falsePositiveCount, falseNegativeCount, zeroToleranceMissCount,
   avoidedInvocationCount and terminal verdict.
7. Keep machine results distinct from reviewer semantic acceptance.

## Evidence Requirements

Evidence must include 7/7 source hashes, pre-run fixture/ledger hashes,
case-level expected/actual outcomes, earliest-stop and invocation accounting,
false-positive/false-negative totals, two-run byte identity, exact changed-path
proof, empty staging and the complete command/exit-code record. Self-authored
semantic acceptance is not evidence.

## Acceptance Criteria

T3-A01 through T3-A10 are conjunctive. `COMPLETE_PENDING_REVIEW` is allowed
only when every row passes, all required commands exit zero and the exact-five
manifest is preserved. Any zero-tolerance miss requires `RETURN_TO_DESIGN`.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m pytest governance/compat/test_dara_t3_historical_replay.py -q
python governance/compat/dara_t3_historical_replay.py --fixture governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json --json
python governance/compat/dara_t3_historical_replay.py --fixture governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json --json
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_dara_t3_historical_replay.py
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
```

The worker must compare the two replay outputs without writing an unlisted
sixth file. Capture output in memory or use a temporary path outside the repo.

## Review Gate

The reviewer recomputes the seven source hashes, validates the freeze hashes,
samples at least one case from every zero-tolerance class, reruns the focused
test/helper and standard fast gates, and inspects exact changed paths. The
reviewer consumes valid worker evidence and does not repeat full implementation
or per-row analysis. Only the reviewer may assign the terminal T3 roadmap
outcome.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-07.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_dara_t3_historical_replay.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Scope / Methodology; Findings / Position; Risk /
Corrective Action; Checker Source Read-Ahead Block; Agent Operation Trace
Block; Delta Execution Claim Boundary Control Block; Epistemic Process Block;
Public Export Disposition; Claim Boundary; Command Evidence; No-Commit
Statement; git status --short.

Conditional sections must use a truthful compact N/A-with-reason disposition
when not applicable. The return must include the exact architecture
applicability declaration from this order rather than fabricate accepted
matrix echo fields.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator manual relay -> external worker -> orchestrator/reviewer -> closer |
| phase | DARA-T3 historical replay execution |
| baseHeadFor(phase) | dispatchBaseHead=`42ba4db4311e98d6401e25989f392533765f0a54`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact five worker paths only |
| traceScope(phase, actor) | worker records commands/diff; reviewer records focused comparison and commit range |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns commits |
| crossBatchIsolation | Before status evidence: clean worktree at `42ba4db4311e98d6401e25989f392533765f0a54`; DARA-T2B closed; WP-ARCH-003 and DARA-T4 remain parked |
| nextMoveSurfaces | active handoff, bootstrap and state only following reviewer acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_COMPLETION_REVIEW_2026-09-07.md` |
| reviewerOwnedClosurePaths | worker return in-place reviewer addendum or named completion review; roadmap/work-order terminal metadata only after acceptance |
| closureOwner | orchestrator/reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local replay helper/test and reviewer gates | no production wiring; reviewer alone accepts/commits | exact-five manifest and return | local Python process only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | one worker reached by operator manual relay | new parent count 0 to 1; ceiling 1; no provider authority inside repo | committed packet and exact return | text relay only; orchestrator uses no CLI/MCP | CONTRACT_ONLY |

## Core Guard Self-Protection Authorization

Protected paths:

- `governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json`
- `governance/compat/dara_t3_historical_replay.py`
- `governance/compat/test_dara_t3_historical_replay.py`

Operator authorization: fresh continuation after DARA-T2B closure.
Rollback boundary: remove only the exact five worker artifacts. Active DARA
checker, dispatch framework, hooks, state and historical inputs are excluded.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T3 is the next foundation tranche | roadmap | `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md` | Work Plan; WP-ARCH-003 Interlock | `DARA-T3` | DARA roadmap | ACCEPT |
| T2B is accepted and committed | closure evidence | `docs/reviews/CVF_DARA_T2B_INTERNAL_RECOVERY_COMPLETION_REVIEW_2026-09-07.md` | Decision / Disposition; Machine Closure Package | `CLOSED_PASS_BOUNDED`; `483176267` | reviewer closure | ACCEPT |
| DARA validator is current oracle | standard/source | `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md` | Schema; Closed-Chain Machine Contract; Quota And Admission Progression | `cvf.dara.architectureBindingMatrix.v1` | DARA standard | ACCEPT |
| exact historical inputs and hashes | paired baseline | `docs/baselines/CVF_GC018_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_2026-09-07.md` | Frozen Replay Source Set | DARA-T3-S01 through DARA-T3-S07 | dispatcher-owned freeze | ACCEPT |
| exact worker outputs | paired baseline | `docs/baselines/CVF_GC018_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_2026-09-07.md` | Required Artifact Manifest | five literal paths | dispatcher-owned manifest | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-readiness historical replay`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "architecture-readiness historical replay" --role dispatcher --lifecycle-phase dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | no additional ADIF-specific requirement; roadmap findings remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_architecture_schema.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | DISPATCH_READY, INITIAL, EXTERNAL_AGENT_CLI_MCP, low-risk architecture reason, no-commit conversion, protected paths, trace labels, private export disposition |
| gateRunPurpose | confirm a complete dispatch packet before consuming external invocation 1 |
| claimBoundary | structural compliance does not prove replay results or semantic acceptance |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| five output paths absent | `Test-Path` returned `False` for all five at `42ba4db43` | PASS |
| competing owner search | `rg -n "DARA-T3|DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY" docs CVF_SESSION governance/compat` | only roadmap/continuity references; no active replay implementation |
| collision decision | existing MFRP replay is a different reviewer-readout domain and is read-only precedent | NO_OWNER_COLLISION |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | committed CVF work order -> operator manual relay -> bounded external return -> local reviewer decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | DARA roadmap, paired baseline, this work order and the exact worker-return path in the fulfillment manifest |
| Disposition | one external worker invocation admitted under new parent ceiling 1 |
| Claim boundary | returned material is evidence input, not acceptance authority |

## Epistemic Process Block

### Expected Result / Prediction

Current DARA admission should stop all three historical dispatches before their
recorded external invocation, and all seeded zero-tolerance cases should fail
closed with zero false negatives.

### Evidence Comparison

Not executed at dispatch. The worker must compare raw and seeded actual results
against the frozen ledger without changing expectations after first replay.

### Contradiction Or Gap Disposition

Any source drift, zero-tolerance miss, nondeterminism or need to edit an active
checker returns `BLOCKED_WITH_REASON` or `RETURN_TO_DESIGN`.

### Claim Update

This packet claims dispatch readiness only; replay effectiveness remains
unproven until independent review.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator/reviewer |
| Provider or surface | local private CVF workspace; no external CLI/MCP invocation |
| Session or invocation | DARA-T3 dispatch authoring, 2026-09-07 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, `Test-Path`, SHA-256, scaffold stdout, apply_patch and local gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator continuation; closed DARA-T2B; roadmap T3 row |
| Before status evidence | clean worktree at HEAD `42ba4db4311e98d6401e25989f392533765f0a54`; five worker outputs absent |
| After status evidence | exact two dispatcher-owned documents in the worktree; worker outputs remain absent |
| Diff evidence | `git status --short --untracked-files=all`; exact two dispatch paths |
| Approval boundary | DARA-T3 dispatch authoring and one external invocation via operator relay |
| Claim boundary | no replay result, WP repair, DARA-T4, provider/live/public/deploy action |
| Agent type | orchestrator/reviewer |
| Invocation ID | `dara-t3-dispatch-authoring-2026-09-07` |
| Expected manifest | paired baseline plus this work order |
| Actual changed set | paired baseline plus this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id DARA-T3-WP-ARCH-003-HISTORICAL-REPLAY --title "DARA T3 WP-ARCH-003 Historical Replay" --date 2026-09-07 --base 42ba4db4311e98d6401e25989f392533765f0a54 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --new-independent-critical-evidence NONE --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all placeholders with exact authority, source hashes, replay obligations, five paths and return contract |
| checkerReadAheadConfirmation | applicable sources above were read before authoring |
| docOnlyNewFields | none |
| claimBoundary | provenance only; no implementation or replay result claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | offline historical replay helper, fixture, tests and documentation evidence |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime/provider receipt exists or is claimed; replay artifacts are local evidence only |
| actionEvidence | ACTION_EVIDENCE_PRESENT: dispatch authoring commands and pre-dispatch gate evidence; worker action evidence must be returned separately |
| invocationBoundary | one operator-relayed external worker assignment; no orchestrator CLI/MCP provider call |
| interceptionBoundary | no runtime interception, wrapper, provider gate or production enforcement |
| claimLanguage | counterfactual replay evidence only, not retroactive invalidation or production readiness |
| forbiddenExpansion | no WP implementation, active guard edit, provider/live, credentials, public sync, deploy, push or automatic DARA-T4 |

## Verification And Return Decision

Return `COMPLETE_PENDING_REVIEW` only if all T3-A01 through T3-A10 pass and
every required command exits zero. Return `RETURN_TO_DESIGN` for any
zero-tolerance miss or unrepresentable required case. Return
`BLOCKED_WITH_REASON` for source drift, forbidden-path need or nonzero required
gate. Never self-accept or commit.

## Return-To-Orchestrator Conditions

Return immediately with `BLOCKED_WITH_REASON` on source drift, required
out-of-manifest mutation, forbidden active-checker change, or a nonzero
mandatory precondition. Return `RETURN_TO_DESIGN` for any zero-tolerance miss
or unrepresentable required case. Otherwise return `COMPLETE_PENDING_REVIEW`.

## Operator Checkpoint

The operator's fresh continuation instruction authorizes DARA-T3 and one manual
external relay only. No further operator checkpoint is required inside the
exact-five implementation. DARA-T4, WP-ARCH-003 repair, provider/live work,
public sync and deployment remain parked behind a new explicit direction.

## Closure Checklist

- [ ] Exact five worker paths and no other changes.
- [ ] Seven source hashes match at start and return.
- [ ] Fixture and ledger freeze hashes remain identical.
- [ ] T3-A01 through T3-A10 are reconciled truthfully.
- [ ] Required commands and two deterministic runs pass.
- [ ] Staging is empty and the worker made no commit.
- [ ] Worker return uses one allowed non-terminal disposition.

## Intake Role Routing Decision

Intake summary: committed CVF evidence plus one operator-relayed external
worker execution; no external knowledge is accepted directly.

Scope classification: bounded offline code/test/evidence replay.

Risk sensitivity: medium because governance admission is evaluated, while no
active guard wiring or runtime/provider effect is allowed.

Selected role route: `routeMode=MULTI_AGENT_SINGLE_ROLE`.

Role separation basis: worker produces exact-five evidence; internal reviewer
independently accepts or rejects it and owns commits.

Escalation condition: frozen-source contradiction, manifest escape,
zero-tolerance miss or any need for forbidden authority.

## Foundation Storage Layout Block

The fixture, helper and tests use the established `governance/compat/fixtures/`
and `governance/compat/` families; human replay evidence uses `docs/reviews/`.
No new `docs/reference/` family, stable standard, folder front door, index,
registry or alternate duplicate owner is created. The five literal paths are
the complete storage layout and rollback boundary.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "DARA-T3-WP-ARCH-003-HISTORICAL-REPLAY",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["docs/baselines/", "docs/work_orders/", "docs/reviews/", "governance/compat/"],
  "claims": ["bounded deterministic historical architecture-readiness replay"],
  "requiredProof": ["seven source hashes", "exact-five manifest", "zero-tolerance replay", "two-run determinism", "no-commit return"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["active guard wiring", "runtime or provider effect", "public sync", "deployment", "worker commit"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded seven-source set; no corpus-completeness claim",
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, `P3_ELEVATED`, selective execution false and
`RUN_FULL_LEGACY_BUNDLE`.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | deterministic offline replay of frozen committed inputs; no runtime/provider/live behavior is claimed |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime/provider receipt | no such receipt is authorized or claimed | N/A with reason: offline replay only |
| Local action evidence | dispatch authoring and pre-dispatch gate output are locally observable | PASS |
| Worker replay evidence | exact-five return contract defines required evidence | N/A with reason: worker has not executed |
| Reviewer acceptance | reserved to the reviewer after evidence return | N/A with reason: no return exists |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch; no public-sync authority.

## Machine Closure Package

This work order is dispatch-ready, not terminal. The worker must reproduce this
section in the return with truthful non-terminal evidence; reviewer/closer owns
all final statuses.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | dispatch authorization only; terminal conversion is reviewer-owned | N/A with reason: execution has not occurred |
| Completion or reviewer artifact | DARA-T3 completion review | created only after returned evidence is assessed | N/A with reason: no return exists |
| Roadmap state | `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md` | T3 is the authorized measurement tranche; T4 remains parked | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | unchanged; no registry claim or mutation is authorized | PASS |
| Registry Markdown | `docs/corpus-intelligence/registry/` | unchanged; no registry claim or mutation is authorized | PASS |
| External evidence digest | exact-five worker manifest | no returned external evidence exists at dispatch | N/A with reason: worker has not executed |
| System loop interlock | active system-loop surfaces | no runtime or production interlock mutation is authorized | N/A with reason: offline replay only |
| Session continuity | active handoff/bootstrap/state | closer synchronizes continuity in a separate commit after material dispatch | N/A with reason: material dispatch commit must occur first |

## Claim Boundary

This order authorizes exactly one external, operator-relayed, provider-free
historical replay producing five uncommitted artifacts. It does not accept or
implement `WP-ARCH-003`, open DARA-T4, alter MFRP/P4-C1, authorize provider or
live execution, publish, deploy, push or claim production readiness.
