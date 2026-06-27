# CVF Agent Work Order - ADIF Continuous Execution T0-T5 For Claude

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: work_order

Commit mode: `WORKER_MAY_COMMIT`

dispatchBaseHead: 60751daf

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: c08f810e

## Dispatch Prompt Envelope

Role: Claude continuous execution orchestrator/worker. Claude may use isolated
T3/T4 workers. Codex is the designated final reviewer/closer.

Canonical packet:
`docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md`

Commit mode: `WORKER_MAY_COMMIT`

executionBaseHead: capture with `git rev-parse --short HEAD` before edits.

Current-time notes: the operator preselected the exact sequence
`T0 -> T1 -> T2 -> (T3 || T4) -> T5`; child evidence still controls each
release.

Do-not-misread notes: continuous does not mean gate-free. Parallel means
isolated worktrees with an identical post-T2 bridge base and disjoint manifests,
otherwise serialize. Do not push. The only permitted continuity edit is the
root-handoff-only bridge defined by the 2026-06-23 hardening standard.

Required first actions: read the canonical packet and Required First Reads,
capture HEAD/status, run pre-implementation, and author the T0 child packet.

Return contract: return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`
with the complete evidence graph. Codex reviews after T5.

## Mission

Execute ADIF continuously in the order `T0 -> T1 -> T2 -> (T3 || T4) -> T5`
under the canonical authorization packet below. Produce private checkpoint
commits and return the whole batch to Codex for final review. Do not push.

## Purpose

Translate the operator's continuous-execution selection into a dependency-safe
Claude dispatch while preserving child source verification and Codex final
review.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator sequence decision | `T0 -> T1 -> T2 -> (T3 || T4) -> T5`, 2026-06-22 | ACCEPT |
| Canonical authorization | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | ACCEPT |
| ADIF roadmap | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Handoff contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACCEPT |
| T2 accepted checkpoint review | `docs/reviews/CVF_ADIF_T2_TASK_ROLE_PHASE_DEFECT_PACKET_RESOLVER_CHECKPOINT_REVIEW_2026-06-23.md`; commit `07000fd6` | ACCEPT |
| Continuous bridge standard | `docs/reference/CVF_CONTINUOUS_EXECUTION_HANDOFF_SYNC_BRIDGE_STANDARD_2026-06-23.md` | ACCEPT - binding T3-T5 addendum |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | human operator; sequence and boundary authority |
| Dispatcher | Codex for this master packet; Claude for source-verified child packets |
| Orchestrator/worker | Claude |
| Parallel T3/T4 workers | Claude-isolated agents/worktrees, if disjointness is proven |
| Reviewer/closer | Codex, explicitly designated |
| Session-sync steward | Codex following accepted closure |
| Handoff-sync bridge steward | Claude orchestrator for T3-T5 only, root active handoff only |

## Required First Reads

- `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md`
- `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`
- `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`
- `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md`
- `docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md`
- `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`
- `docs/reference/CVF_CONTINUOUS_EXECUTION_HANDOFF_SYNC_BRIDGE_STANDARD_2026-06-23.md`
- `docs/reviews/CVF_ADIF_T2_TASK_ROLE_PHASE_DEFECT_PACKET_RESOLVER_CHECKPOINT_REVIEW_2026-06-23.md`

## Pre-Flight Checks

- confirm current HEAD contains the committed dispatch packet;
- confirm `git status --short` is clean;
- capture `executionBaseHead`;
- run pre-implementation with a real range;
- verify T0 child packet source facts before implementation;
- verify no public-sync, provider/live, secret/quota, or session path is in the
  execution manifest.

## Canonical Packet

`docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md`

Roadmap:
`docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`

## Required First Actions

1. Read the canonical packet and roadmap completely.
2. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
3. Confirm the worktree is clean and the dispatch commit contains this packet.
4. Run pre-implementation with the captured base and real HEAD.
5. Author and gate a fresh T0 child GC-018/work order before T0 implementation.

## Execution Contract

| Sequence | Claude action | Required evidence before continuing |
|---|---|---|
| T0 | owner reconciliation and taxonomy contract | committed child packet, output, focused checks, checkpoint review |
| T1 | schema, compact source layout, seed dictionary | T0 checkpoint commit plus refreshed source verification and gates |
| T2 | deterministic bounded resolver and tests | T1 checkpoint commit plus refreshed source verification and gates |
| T3/T4 | execute in isolated worktrees from identical T2 HEAD | disjoint manifests, branch-local tests/gates, separate checkpoint commits |
| integration | combine T3/T4 without losing evidence commits | integration tests/gates and clean convergence ledger |
| T5 | lifecycle/drift/quality guard | integrated T3/T4 evidence plus fresh child packet and gate placement proof |
| return | complete batch handoff | final manifest, graph, gates, clean status, no push |

## Allowed Scope

- author fresh child GC-018/work orders and worker checkpoint evidence; no
  intermediate Codex review artifact is required for T3 or T4;
- create the ADIF reference family, compact entry sources, template, seed
  entries, bounded resolver, focused tests, T3 integration, T4 intake bridge,
  and T5 integrity guard only as source-verified by each child packet;
- update this roadmap's tranche/checkpoint rows during execution;
- create local private commits and isolated T3/T4 worktrees/branches;
- make allowed-scope gate repairs and rerun gates.
- create dedicated root-active-handoff-only bridge commits between T3-T5
  material transitions when required by GC-020.

## Write Ownership

This master packet owns no implementation filenames beyond its dispatch
artifacts. Each child packet must declare exact write paths before that tranche
starts. Claude owns those child-declared paths and private execution commits.
T3/T4 workers must own disjoint paths. Claude owns only the root handoff during
an authorized bridge commit. Codex owns final completion/status and all other
session-sync paths.

## Forbidden Scope

- active session state, session front door, review queue, or generated
  active-session aggregate; active handoff is forbidden except for the exact
  root-handoff-only bridge commit authorized by the hardening standard;
- public-sync clone, remote push, remote changes, or public claims;
- provider/live calls, secrets/quota, runtime/product behavior, model routing,
  memory reinjection, arbitrary command execution, or direct interception;
- changing canonical F2G/FPRC/INDEX/Guard Orientation semantics without a
  source-owner decision that stops the batch for Codex review;
- broad historical migration or full-dictionary prompt injection;
- claiming comprehension, effectiveness, readiness, or final closure.

## Source Verification Block

The master source facts are the eleven `ACCEPT` rows in the canonical packet.
They are incorporated here by exact path and section. This master work order
does not claim that future ADIF files or symbols already exist.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Continuous sequence is operator-authorized | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | Continuous Execution Decision | `T0`; `T1`; `T2`; `T3`; `T4`; `T5` | ADIF authorization | VALUE_SET | ACCEPT |
| Tranche definitions exist in roadmap | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | Tranche Sequence | `ADIF-T0`; `ADIF-T1`; `ADIF-T2`; `ADIF-T3`; `ADIF-T4`; `ADIF-T5` | ADIF roadmap | EXISTS | ACCEPT |
| Dependency release evidence is mandatory | `docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md` | Required Dependency Release Evidence | `Dependency Release Evidence` | dependency release standard | VALUE_SET | ACCEPT |
| Commit ownership and parallel isolation are governed | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | CF-07; CF-08 | `commitOwner(phase)`; `crossBatchIsolation` | Agent Handoff Contract | VALUE_SET | ACCEPT |

Every child packet must add its own full Source Verification Block. Missing or
rejected source facts stop that child; this master packet cannot convert them
to `ACCEPT`.

## Execution Plan

1. Execute and commit T0 from a fresh child packet.
2. Release, execute, and commit T1 from T0 checkpoint evidence.
3. Release, execute, and commit T2 from T1 checkpoint evidence.
4. Jointly author/gate T3/T4 child packets, commit, bridge, then fork identical
   bridge HEAD into isolated worktrees when manifests are disjoint.
5. Execute both branches with `CHECKPOINT_PASS_PENDING_FINAL_REVIEW`; do not
   pause for Codex.
6. Integrate branch one, bridge; integrate branch two, bridge; run combined
   tests/gates without squashing evidence.
7. Author/gate T5, bridge its dispatch commit, execute/commit T5.
8. Produce the final worker return and stop once for Codex review.

## Evidence Requirements

Each tranche must record child packet path, execution base, checkpoint commit,
changed manifest, focused tests, autorun commands/results, findings, and claim
boundary. The final return adds T3/T4 fork/convergence evidence, combined test
results, graph evidence, and clean worktree status.

## Acceptance Criteria

| Criterion | Required disposition |
|---|---|
| T0-T2 order preserved | PASS |
| T3/T4 share exact T2 base and have disjoint manifests or serialize | PASS |
| T5 begins only after both branches integrate and pass | PASS |
| every child has fresh GC-018, work order, source verification, and gates | PASS |
| F2G/FPRC/INDEX ownership preserved | PASS |
| no provider/live/public/session scope entered | PASS |
| final return is review-pending, not closed | PASS |

## Review Gate

Codex reviews the complete committed graph after T5, recomputes source facts,
runs focused/integration tests and closure gates, then accepts, repairs,
partially accepts, or rejects each tranche. Claude must not pre-write Codex's
final completion review.

## Closure Checklist

- [x] Operator selected the continuous sequence.
- [x] Canonical authorization and master work order exist.
- [x] Initial roadmap dependency is released.
- [x] Codex is designated final closer.
- [x] Public/provider/runtime/session boundaries are explicit.
- [x] Later tranche release requires committed child evidence.

## Return-To-Orchestrator Conditions

Return success only as `COMPLETE_PENDING_REVIEW`. Return
`BLOCKED_WITH_REASON` for any Stop Condition in the canonical packet. Do not
continue past a missing dependency artifact, failed out-of-scope gate, or
unsafe parallel overlap.

## Operator Checkpoint

The operator has preselected T0-T5 inside this exact sequence. No repeated
operator question is required for compliant child transitions. A new operator
checkpoint is required for scope/risk/claim expansion, public/provider/live or
secret/quota work, destructive action, canonical-owner semantic change, or a
different execution order.

## New Doc-Only Fields

The five orchestration labels in the canonical packet are `DOC_ONLY_NEW` and
remain local to this execution chain. Child implementation must not encode them
as runtime or canonical governance enums.

## Dependency Release Evidence

| Prerequisite artifact | Closure or dispatch commit | Disposition | Gate evidence |
|---|---|---|---|
| ADIF roadmap | `d86f49e9` | ACCEPT | roadmap gates and commit evidence recorded in session state |
| MPI-T6 decision closure before ADIF selection | `14f8e5f9` | ACCEPT | committed-range pre-closure PASS |
| Operator continuous-selection decision | this authorization packet | ACCEPT | dispatch gates required before Claude starts |
| ADIF-T2 accepted checkpoint | `07000fd6` | ACCEPT | 13 focused tests, reviewer-fast, and pre-commit PASS; handoff bridge `4527c55a` |
| T3-T5 choreography hardening | this changed master packet and bridge standard | ACCEPT | real-range pre-dispatch and pre-commit required before release |

Later tranche dependencies are not claimed released by this table. Claude must
append source-backed checkpoint rows to the matching child packet before each
transition.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Evidence owner |
|---|---|---|
| preserve F2G/FPRC ownership | child Source Verification and T0 contract | T0/T1 |
| category remains orthogonal | schema contract and tests | T0/T1 |
| bounded task packet | deterministic resolver/max-count tests | T2 |
| no comprehension claim | child claim boundaries | all tranches |
| generated aggregate discipline | compact sources plus generator/check if aggregate exists | T1/T5 |
| early preflight without competing autorun | source-verified AAF/owner integration | T3 |
| governed finding intake | F2G/FPRC-preserving outcomes | T4 |
| honest machine enforcement | integrity tests and justified gate placement | T5 |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator-originated ADIF continuous-execution selection |
| intake summary | private T0-T5 foundation chain with evidence-gated transitions |
| scope classification | governed foundation implementation; no runtime/provider/public behavior |
| risk sensitivity | R2 governance foundation with protected checker wiring possible only in source-verified child scope |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Claude orchestrates sequential work; isolated T3/T4 workers may run in parallel; Codex is final reviewer/closer |
| Commit mode | `WORKER_MAY_COMMIT` |
| escalation condition | scope/risk/claim expansion, overlapping parallel writes, forbidden paths, provider/live, public-sync, secrets/quota, destructive action, or canonical-owner semantic change |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | sequential Claude orchestrator/worker; parallel isolated T3/T4 workers; Codex final reviewer/closer |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=60751daf`; Claude captures execution bases; Codex captures closure base |
| changedSetScope(phase) | dispatch=three dispatch artifacts; execution=child-declared paths; closure=reviewer-owned conversion paths; session-sync=continuity only |
| traceScope(phase, actor) | one trace per dispatch/execution branch/closure/session-sync actor-phase |
| commitOwner(phase) | Codex dispatch; Claude execution; Claude root-handoff-only bridge for T3-T5; Codex closure and session sync |
| crossBatchIsolation | T0/T1/T2 sequential; T3/T4 separate clean worktrees from identical T2 HEAD; T5 after integration |
| Before status evidence | clean worktree before dispatch authoring at base `60751daf`; current pending set is exactly the three dispatch artifacts and must be committed before Claude starts |
| nextMoveSurfaces | Claude does not edit mode/state/front door/next move; only the root handoff bridge ledger is permitted before final Codex sync |
| Closer designation | Codex |

## Worker Autonomy / No-Question Rule

Claude repairs and reruns all allowed-scope gate failures without asking the
operator. Claude asks or stops only for the explicit escalation conditions in
the Intake Role Routing Decision.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | new stable ADIF reference/source family chosen by T0/T1 child packet |
| Storage decision | compact per-entry sources; stable front door; no hand-edited large aggregate |
| Existing aggregate impact | N/A until a child packet proves an aggregate is required |
| Generated state impact | active session generated state is forbidden during Claude execution |
| Durable governance boundary | private source-backed defect intelligence only; no runtime memory store |

## Return Contract

Return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` with all evidence
required by the canonical packet. A successful worker return is not closure.

## Worker Pending-Return Gate

Before return, run focused child tests, reviewer-fast, pre-commit, and the
appropriate real-range autorun gates. Record command, base, head, result, and
any diagnostic. Do not rerun unclear live/provider failures; live/provider work
is forbidden here.

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_ADIF_CONTINUOUS_EXECUTION_T0_T5_COMPLETION_2026-06-22.md`

reviewerOwnedClosurePaths:

- the completion review above;
- this work order and canonical authorization status conversion;
- roadmap final tranche and claim-boundary conversion;
- allowed reviewer repairs to Claude-owned files;
- session continuity only in a separate post-closure commit.

Codex may accept, repair within scope, partially accept, or reject individual
tranches. Claude checkpoint commits do not constrain Codex's final disposition.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Disposition |
|---|---|---|---|---|
| `INTERNAL_AGENT` | local continuous orchestrator, child workers, resolver, and bridge steward | machine-gated private commits; root handoff bridge only; Codex retains review/closure | bridge standard and hardened execution plan | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | no execution adapter in T3-T5 | ingress, authentication, approval, receipt, raw-data, mutation, runtime, and public boundaries remain outside scope | Forbidden Scope and T2 review | `DEFERRED_WITH_REASON` - future adapter requires separate authorization |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| ADIF governed artifact | committed implementation and final-review acceptance | PASS |
| GC-051 corpus registration | generated JSON aggregate and retained human companion | PASS |
| Runtime/provider receipt | N/A with reason: no runtime/provider/live claim | N/A with reason |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | current ADIF governed source, tests, and final-review diff |
| Provider registry surfaces | not changed or claimed by this bounded foundation batch |
| Freshness disposition | PASS - no runtime, provider, live-proof, or external-adapter behavior is claimed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance execution only. No public-sync or remote push is
authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | private governed ADIF foundation execution |
| claimDisposition | N/A with reason: no Delta execution-control behavior is implemented or claimed |
| receiptEvidence | N/A with reason: no Delta receipt |
| actionEvidence | N/A with reason: dispatch packet only; Claude evidence follows in child commits |
| invocationBoundary | local repository work, tests, gates, commits, and isolated worktrees |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | evidence-gated ADIF implementation only |
| forbiddenExpansion | runtime/provider/live, public-sync, arbitrary action execution, readiness, universal control |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | local workspace |
| Session or invocation | ADIF continuous execution dispatch, 2026-06-22 |
| Working directory | repository root |
| Command or tool surface | governed source reads, apply_patch, dispatch gates, git commit |
| Target paths | canonical authorization; this work order; roadmap status update |
| Allowed scope source | operator instruction selecting continuous T0-T5 execution |
| Before status evidence | clean worktree at HEAD `60751daf` before authoring; current pending set is exactly the three dispatch artifacts; ADIF was parked pending T0 selection |
| After status evidence | continuous chain dispatch-ready pending Claude start |
| Diff evidence | dispatch range name-status and gate output |
| Approval boundary | dispatch only; no ADIF implementation in this batch |
| Claim boundary | conditional execution chain with evidence gates; no runtime/public/provider expansion |
| Agent type | dispatch author / future reviewer-closer |
| Invocation ID | `adif-continuous-execution-dispatch-2026-06-22` |
| Expected manifest | canonical authorization; this work order; ADIF roadmap |
| Actual changed set | canonical authorization; this work order; ADIF roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | ADIF continuous authorization | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | final ADIF completion review | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | ADIF roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | ADIF-T0-T5 entry generated from registry source | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | human companion retained; no quick-lookup delta required | PASS |
| External evidence digest | N/A | no external evidence intake | N/A with reason |
| Session continuity | active session surfaces | separate post-closure sync follows | N/A with reason |
| System loop interlock | N/A | no runtime loop changed | N/A with reason |

## Claim Boundary

This master work order authorizes orchestration, child packet authoring, and
execution only under refreshed child evidence. It does not make unknown source
facts true, release a failed dependency, authorize public/provider/runtime
behavior, or replace Codex final review.
