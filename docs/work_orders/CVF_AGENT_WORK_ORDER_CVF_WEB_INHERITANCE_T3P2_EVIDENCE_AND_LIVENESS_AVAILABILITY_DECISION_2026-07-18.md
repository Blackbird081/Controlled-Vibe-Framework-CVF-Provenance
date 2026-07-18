# CVF Agent Work Order - MAO Evidence And Liveness Availability Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-WEB-INHERITANCE-T3P2

Dispatch base head: `f2e0b7161`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated source-audit worker

Reviewer/closer: CVF independent reviewer/closer

Worker return path:
`docs/reviews/CVF_WEB_INHERITANCE_T3P2_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: execute only T3P2 as a no-commit documentation-only source-decision
worker.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_INHERITANCE_T3P2_EVIDENCE_AND_LIVENESS_AVAILABILITY_DECISION_2026-07-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: use and verify the dispatcher-provided post-dispatch session
HEAD before writing.

Current-time notes: source verification and packet date are 2026-07-18.

Do-not-misread notes: this packet decides evidence/liveness availability; it
does not implement a store, heartbeat persistence, adapter, or Web page.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, roadmap, T3A/T3P1 reviews, all cited source and
contract owners, and output checker source.

Return contract: leave exactly two allowed outputs unstaged and uncommitted and
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Select a truthful, value-backed route for MAO evidence and liveness before
T3B scope is authored.

## Agent Roles

- Worker: direct source audit, terminal decision, and no-commit return.
- Reviewer/closer: independent recomputation, challenge, closure, and commit.
- Session steward: protected continuity in a separate commit.

## Authority Chain

Operator standing authority -> Web inheritance roadmap -> accepted T3A and
T3P1 reviews -> this packet -> no-commit worker -> independent reviewer.

## Required First Reads

Read `CVF_SESSION_MEMORY.md`, bootstrap/state registry, active handoff, guard
orientation, literal gotchas, paired baseline, roadmap, T3A/T3P1 completion
reviews, and every Source Verification file.

## Pre-Flight Checks

Verify clean start and execution HEAD; run pre-implementation autorun; refresh
persistence, reconstruction, retention, caller, heartbeat, timeout, and
recency searches; stop on a forbidden-scope need.

## Worker Autonomy / No-Question Rule

Repair allowed-output defects directly. Return only for base mismatch, missing
canonical source, unresolved contradiction, or required third path.

## Intake Role Routing Decision

routeMode: SINGLE_AGENT_SINGLE_ROLE selected route

Intake summary: repository-local architecture and product-boundary decision.

Scope classification: two documentation outputs, no implementation.

Risk sensitivity: HIGH because false liveness or retention claims could
mislead operators.

Role separation: worker cannot accept or commit its decision.

Escalation condition: the selected route requires implementation to prove an
existing-source claim.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| T3A decision accepted | `docs/reviews/CVF_WEB_INHERITANCE_T3A_COMPLETION_REVIEW_2026-07-18.md` | `c0d88ff34` | ACCEPT |
| T3P1 discovery accepted | `docs/reviews/CVF_WEB_INHERITANCE_T3P1_COMPLETION_REVIEW_2026-07-18.md` | `c282312b9` | ACCEPT |
| roadmap release | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | dispatcher material commit for this packet | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| evidence ledger is in-memory | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | `MaoEvidenceLedger` | `MaoEvidenceLedger` | evidence ledger | ACCEPT |
| freshness means evidence recency | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | `classifyReadoutFreshness` | `classifyReadoutFreshness` | evidence readout contract | ACCEPT |
| milestones exclude per-heartbeat mirroring | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | `projectWorkspaceMilestones` | `projectWorkspaceMilestones` | milestone projection | ACCEPT |
| receipts require batch-life plus closure-window retention | VALUE_SET | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Storage And Retention Decision | `Retention` | runtime foundation contract | ACCEPT |
| heartbeat records are process-local | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts` | `MaoLifecycleController` | `heartbeatRecords` | lifecycle controller | ACCEPT |
| timeout detection persists a durable event | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | `recordTimeout` | `recordTimeout` | operational launcher | ACCEPT |
| run IDs and events are now discoverable/replayable | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `listRunIds`; `resumeRun` | `listRunIds`; `resumeRun` | durable run store | ACCEPT |
| operator projection consumes caller-supplied ledger | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.operator.projection.ts` | input and builder | `MaoOperationalOperatorProjectionInput` | operator projection | ACCEPT |

## New Doc-Only Fields

| Field | Required value boundary |
|---|---|
| `availabilityDisposition` | one allowed terminal route |
| `claimableLivenessDimensions` | separate heartbeat, timeout, task state, recency |
| `requiredNextOwner` | exact owner/path proposal or N/A with reason |
| `t3bReleaseBoundary` | released dimensions and exclusions or N/A with reason |

## Scope / Target / Owner Boundary

Audit and decide only. Proposed persistence symbols belong in a clearly marked
proposal table, never the Source Verification table.

## Allowed Scope

1. `docs/reviews/CVF_WEB_INHERITANCE_T3P2_EVIDENCE_AND_LIVENESS_AVAILABILITY_DECISION_2026-07-18.md`
2. `docs/reviews/CVF_WEB_INHERITANCE_T3P2_WORKER_RETURN_2026-07-18.md`

## Write Ownership

The worker owns only the two Allowed Scope outputs. The reviewer owns closure
conversion across those outputs, the paired baseline/work order, roadmap, and
completion review. Protected continuity remains a separate steward batch.

## Foundation Storage Layout Block

Storage layout applicability: N/A with reason. This tranche compares current
durable and in-memory owners but creates, splits, relocates, and refactors no
foundation file or storage layout. Any selected persistence implementation
requires a fresh GC-018 and work order naming its canonical root, source
layout, index/front door, generator disposition, and migration boundary.

Stable front door: existing MAO reference front door remains
`docs/reference/multi_agent_orchestration/README.md`.

Generated aggregate disposition: N/A with reason; no aggregate changes.

Archive disposition: N/A with reason; no file is superseded or relocated.

## Forbidden Scope

No source, test, persistence, package, Web, config, registry, generated state,
provider/live, browser, public-sync, push, release, production, staging,
stash, or commit mutation.

## Required Decision Contract

Select exactly one `availabilityDisposition`:

- `DURABLE_EVIDENCE_SUBSTRATE_REQUIRED` when retention and restart-safe
  milestone evidence require a new owner before T3B;
- `BOUNDED_DURABLE_EVENT_ONLY_WEB_ROUTE` when durable event/task/timeout value
  justifies T3B while evidence milestones and heartbeat are explicitly omitted;
- `EXPLICIT_IN_PROCESS_EVIDENCE_ROUTE` only when process-lifetime limitations
  are acceptable and visibly operator-safe; or
- `DEFER_T3_WITH_REASON` with a concrete reopen condition.

Challenge at least one alternative. Record a matrix for retention,
reconstruction, evidence caller, milestone availability, heartbeat,
timeout/task state, recency, privacy, operator value, and next owner.

## Execution Plan

1. Refresh direct source and negative searches.
2. Separate all four liveness/readout dimensions.
3. Evaluate retention contract against current in-memory ownership.
4. Complete the terminal matrix and challenge alternatives.
5. Select one route and exact next owner or T3B boundary.
6. Run gates and return exact two-path no-commit evidence.

## Required Artifact Manifest

| Artifact | Expected result |
|---|---|
| T3P2 decision | terminal matrix, one route, exact next owner/boundary |
| worker return | commands, evidence, changed set, no-commit proof |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| decision | create source-cited matrix and challenged terminal route |
| worker return | record final searches, gates, and exact boundary |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence |
|---|---|---|
| evidence/liveness prerequisite decision | terminal availability matrix | decision artifact |
| truthful liveness | four dimensions separated | claimability rows |
| no premature implementation | documentation-only forbidden scope | exact diff |
| dependency ordering | T3B remains parked until review | route and completion review |

## Evidence Requirements

Evidence must include direct citations, zero-hit searches, terminal row count,
one decision token, alternative challenge, exact next owner or T3B boundary,
worker-return fast gate, file-size guard, exact changed set, empty cached diff,
and unchanged HEAD.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
git rev-parse --short HEAD
```

## Acceptance Criteria

- AC-01: retention/reconstruction/caller facts are terminal and cited.
- AC-02: heartbeat, timeout/task state, and recency remain distinct.
- AC-03: one route and one challenged alternative are recorded.
- AC-04: next owner or T3B release boundary is exact and privacy-bounded.
- AC-05: exactly two outputs, unchanged HEAD, no staging, and all gates pass.

Fail conditions: guessed source symbol, blended liveness claim, unresolved
retention contradiction, ambiguous next owner, forbidden path, or failed gate.

## Review Gate

Independent reviewer recomputes every seam, challenges the route, and owns
roadmap release, material commit, and closure.

## Closure Checklist

- [ ] execution HEAD matches;
- [ ] terminal matrix covers every required dimension;
- [ ] one route and challenged alternative are recorded;
- [ ] next owner or T3B boundary is exact;
- [ ] exactly two paths change and nothing is staged;
- [ ] worker no-commit boundary is honored; and
- [ ] independent review remains pending.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for base mismatch, missing canonical source,
required third path, or a decision that cannot be made without implementation.

## Operator Checkpoint

N/A with reason: standing authority releases this decision only. T3B and all
implementation/external mutation remain parked.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_SINGLE_ROLE` |
| rolePattern | one source-audit worker followed by independent reviewer/closer |
| phase | dispatch, no-commit decision, reviewer closure, session sync |
| baseHeadFor(phase) | dispatchBaseHead=`f2e0b7161`; executionBaseHead=dispatcher-provided post-dispatch HEAD; closureBaseHead=executionBaseHead |
| changedSetScope(phase) | dispatch=roadmap/baseline/work order; execution=exact two outputs; closure=reviewer-owned docs; session=protected continuity |
| traceScope(phase, actor) | each actor records its own commands and changed set |
| commitOwner(phase) | dispatcher; none for worker; reviewer/closer; session steward |
| crossBatchIsolation | T3B, T4-T5, Web, provider/live, and external mutation parked |
| nextMoveSurfaces | session steward only |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_WEB_INHERITANCE_T3P2_COMPLETION_REVIEW_2026-07-18.md`

reviewerOwnedClosurePaths: two worker outputs, paired baseline/work order,
roadmap, and completion review; continuity in a separate commit.

closureOwner: CVF independent reviewer/closer.

workerCommitPermission: FORBIDDEN.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_INHERITANCE_T3P2_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class architecture --role dispatcher --lifecycle-phase pre-dispatch --surface-selector execution-plane --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Scope / Target / Owner Boundary; Allowed Scope; Forbidden Scope; Required Decision Contract; Roadmap-To-Work-Order Trace Matrix; Evidence Requirements; Verification Commands; Acceptance Criteria; Review Gate; Closure Checklist; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Claim Boundary |
| gateRunPurpose | dispatch confirmation after direct source verification |
| claimBoundary | structural conformance does not select the product route |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T3P2 --title "MAO Evidence And Liveness Availability Decision" --date 2026-07-18 --base f2e0b7161 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled terminal route vocabulary, source matrix, exact outputs, handoff, and no-implementation boundary |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | four fields listed in New Doc-Only Fields |
| claimBoundary | dispatch-authoring provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-WEB-INHERITANCE-T3P2 dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification, search, scaffold helper, authoring, gates |
| Target paths | roadmap; paired T3P2 baseline; this work order |
| Allowed scope source | accepted T3P1 review and roadmap |
| Before status evidence | clean worktree at `f2e0b7161` |
| After status evidence | exact three-path dispatch set pending commit |
| Diff evidence | bounded material diff |
| Approval boundary | documentation-only evidence/liveness decision dispatch |
| Claim boundary | no persistence, Web, execution, provider/live, public, push, or production mutation |
| Agent type | dispatcher |
| Invocation ID | `cvf-web-inheritance-t3p2-dispatch-2026-07-18` |
| Expected manifest | roadmap; T3P2 baseline; T3P2 work order |
| Actual changed set | exact three-path dispatch set |
| Manifest delta | MATCH after verification |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: current in-memory evidence ownership likely
cannot satisfy restart-safe retention, while durable events can support a
narrower task/timeout readout.

Evidence Comparison Requirement: compare the prediction against current
contract, source, callers, and alternatives.

Contradiction Handling Requirement: narrow or block the route on contradictory
evidence.

Claim Update Requirement: record confirmed, narrowed, or invalidated route.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only evidence/liveness availability decision |
| claimDisposition | N/A with reason: no behavior implemented |
| receiptEvidence | N/A with reason: source decision creates no receipt |
| actionEvidence | N/A with reason: no action surface released |
| invocationBoundary | exact two-output no-commit packet |
| interceptionBoundary | no IDE, shell, provider, filesystem, or agent-action interception claim |
| claimLanguage | inspect, distinguish, decide, and report only |
| forbiddenExpansion | persistence, Web, execution, provider/live, public, push, production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision dispatch; no public-sync action.

## Claim Boundary

This work order authorizes exactly two documentation outputs. It does not
authorize persistence, T3B, Web implementation, provider/live, public, push,
release, production, or session mutation.
