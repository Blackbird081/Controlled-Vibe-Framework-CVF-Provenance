# CVF GC-018 ADIF Continuous Execution Authorization

Memory class: FULL_RECORD

Status: AUTHORIZED_CONTINUOUS_EXECUTION_HARDENED_T3_T5

Date: 2026-06-22

docType: gc018_baseline

dispatchBaseHead: 60751daf

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_MUST_CAPTURE_AT_CLOSURE

Commit mode: `WORKER_MAY_COMMIT`

## Purpose

Authorize Claude to execute the Agent Defect Intelligence Foundation sequence
continuously as `T0 -> T1 -> T2 -> (T3 || T4) -> T5`, then return the complete
private commit chain to Codex for independent review and closure.

## Decision / Baseline / Proposed Tranche

Decision: authorize one continuous private ADIF execution chain with committed
dependency checkpoints and final Codex review. Baseline: roadmap commit
`d86f49e9`, MPI-T6 closure `14f8e5f9`, and dispatch-authoring base
`60751daf`. Proposed tranche: the complete T0-T5 sequence in this packet.

## Operator Authorization

The operator explicitly selected every ADIF tranche on 2026-06-22 and selected
this optimized execution order. This removes repeated operator-selection pauses
inside the authorized claim boundary. It does not waive source verification,
dependency evidence, child GC-018/work-order packets, gates, scope boundaries,
or Codex final review.

## Continuous Execution Decision

| Stage | Release condition | Execution disposition |
|---|---|---|
| T0 | this authorization and dispatch commit exist | READY_FIRST |
| T1 | T0 checkpoint commit, child completion evidence, and tranche gates pass | AUTO_RELEASE_WITH_EVIDENCE |
| T2 | T1 checkpoint commit, child completion evidence, and tranche gates pass | AUTO_RELEASE_WITH_EVIDENCE |
| T3 | T2 checkpoint commit and child packet gates pass | PARALLEL_RELEASE_A |
| T4 | same T2 checkpoint commit and child packet gates pass | PARALLEL_RELEASE_B |
| T5 | T3 and T4 checkpoint commits are integrated and both child gates pass | CONVERGENCE_RELEASE |
| Final review | T5 commit, final worker return, clean worktree, full manifest | CODEX_REVIEW_REQUIRED |

`AUTO_RELEASE_WITH_EVIDENCE` is not a gate bypass. Before each transition,
Claude must author a fresh child GC-018 and source-verified child work order,
record the predecessor artifact and commit, run pre-dispatch and
pre-implementation gates with a real range, then commit the child packet before
implementation.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ADIF sequence and tranche purposes | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | `## Tranche Sequence` | `ADIF-T0`; `ADIF-T1`; `ADIF-T2`; `ADIF-T3`; `ADIF-T4`; `ADIF-T5` | ADIF roadmap | VALUE_SET | ACCEPT |
| F2G owns canonical defect classes and promotion direction | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | `## Minimum defect classes`; protocol sections | `Finding-To-Governance Learning Disposition` | F2G standard | VALUE_SET | ACCEPT |
| FPRC owns root-cause role values | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | `## Defect Role Field` | `defectRole` | FPRC standard | VALUE_SET | ACCEPT |
| Guard Orientation owns task-first control routing | `docs/reference/guard_orientation/README.md` | `## Task Class Guard Map` | `Task Class Guard Map` | guard orientation front door | EXISTS | ACCEPT |
| INDEX cannot replace canonical authority | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | Core Distinction; Required Metadata | `INDEX_ARTIFACT` | INDEX classification standard | LITERAL_INVARIANT | ACCEPT |
| Generated aggregates require compact sources and generator discipline | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | generated source layout discipline | `generated source layout` | generated aggregate standard | RUNTIME_BEHAVIOR | ACCEPT |
| AAF is an existing early diagnostic integration candidate | `governance/compat/run_agent_automation_assist.py` | module diagnostic assembly; `build_report` | `build_report` | AAF helper | EXISTS | ACCEPT |
| Autorun common and pre-implementation bundles exist | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands`; `_pre_implementation_commands` | `_common_commands`; `_pre_implementation_commands` | autorun workflow gate | EXISTS | ACCEPT |
| Reviewer-fast registry exists | `governance/compat/run_local_governance_hook_chain.py` | `REVIEWER_FAST_CHECKS` | `REVIEWER_FAST_CHECKS` | local governance hook chain | EXISTS | ACCEPT |
| Dependency release needs artifact, commit, disposition, anchors, and gates | `docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md` | Required Dependency Release Evidence; Dependency Release Workflow | `Dependency Release Evidence` | dependency release standard | VALUE_SET | ACCEPT |
| Four canonical handoff routes and phase-specific commit ownership exist | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | CF-01 through CF-08 | `MULTI_AGENT_MULTI_ROLE`; `commitOwner(phase)` | Agent Handoff Contract | VALUE_SET | ACCEPT |
| Root-active-handoff-only bridge lane and stop boundaries | `docs/reference/CVF_CONTINUOUS_EXECUTION_HANDOFF_SYNC_BRIDGE_STANDARD_2026-06-23.md` | Exact Write Boundary; Required Command And Commit Shape | `HANDOFF_SYNC_BRIDGE_PASS` | continuous bridge standard | VALUE_SET | ACCEPT |
| ADIF-T2 checkpoint is accepted after resolver hardening | `docs/reviews/CVF_ADIF_T2_TASK_ROLE_PHASE_DEFECT_PACKET_RESOLVER_CHECKPOINT_REVIEW_2026-06-23.md` | Findings / Position; Gate Evidence | `ACCEPTED_FOR_CONTINUATION_PENDING_FINAL_REVIEW` | T2 checkpoint review | VALUE_SET | ACCEPT |

## New Doc-Only Fields

| Field | Owner | Disposition |
|---|---|---|
| `AUTO_RELEASE_WITH_EVIDENCE` | this authorization only | DOC_ONLY_NEW |
| `PARALLEL_RELEASE_A` | this authorization only | DOC_ONLY_NEW |
| `PARALLEL_RELEASE_B` | this authorization only | DOC_ONLY_NEW |
| `CONVERGENCE_RELEASE` | this authorization only | DOC_ONLY_NEW |
| `PASS_FOR_CONTINUATION_PENDING_CODEX_REVIEW` | child checkpoint evidence only | DOC_ONLY_NEW |

These values are orchestration labels, not runtime enums and not substitutes
for canonical work-order or closure statuses.

## Intake Role Routing Decision

route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: Claude is the continuous execution orchestrator and tranche
worker; Claude may use two isolated subagents/worktrees for T3 and T4; Codex is
the designated independent reviewer and sole final closer.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | sequential Claude orchestrator/worker, three-or-more-agent parallel fork at T3/T4, Codex final reviewer/closer |
| phase | DISPATCH_AUTHORING -> EXECUTION -> CLOSURE -> SESSION_SYNC |
| baseHeadFor(DISPATCH_AUTHORING) | `60751daf` |
| baseHeadFor(EXECUTION) | Claude captures dispatch HEAD before the first edit and records each child execution base |
| baseHeadFor(CLOSURE) | Codex captures final Claude HEAD before review |
| changedSetScope(DISPATCH_AUTHORING) | this baseline, master work order, and roadmap dispatch-state update |
| changedSetScope(EXECUTION) | only paths authorized by each fresh child packet |
| changedSetScope(CLOSURE) | Codex completion review, allowed repairs, status conversion, and accepted material |
| traceScope(phase, actor) | one trace per Claude tranche/subagent branch; one Codex closure trace |
| commitOwner(DISPATCH_AUTHORING) | Codex |
| commitOwner(EXECUTION) | Claude and explicitly named T3/T4 branch workers under `WORKER_MAY_COMMIT` |
| commitOwner(CLOSURE) | Codex only |
| commitOwner(SESSION_SYNC) | Codex only |
| commitOwner(HANDOFF_SYNC_BRIDGE) | continuous orchestrator for T3-T5 under the 2026-06-23 bridge standard; root active handoff only |
| crossBatchIsolation | T0/T1/T2 sequential on execution branch; T3 and T4 use separate worktrees from identical T2 HEAD; T5 starts only after integration |
| nextMoveSurfaces | active state/front door remain Codex-owned; T3-T5 orchestrator may edit only the root active handoff in a dedicated bridge commit; Codex owns final session sync |

Designated closer: Codex.

## T3-T5 Continuous Execution Hardening - 2026-06-23

`docs/reference/CVF_CONTINUOUS_EXECUTION_HANDOFF_SYNC_BRIDGE_STANDARD_2026-06-23.md`
is incorporated as a binding addendum and supersedes any earlier instruction
that would pause for Codex between T3, T4, integration, and T5.

- T3/T4 child success status: `CHECKPOINT_PASS_PENDING_FINAL_REVIEW`.
- Machine evidence releases continuation; Codex does not accept/review either
  child before T5.
- After a material, dispatch, or integration commit that precedes another
  gate, the orchestrator may create a dedicated root-handoff-only
  `HANDOFF_SYNC_BRIDGE_PASS` commit.
- The bridge cannot edit session state/front door/review queue, change current
  mode/next move, or claim review/closure.
- Stop for Codex only after T5 final return or an existing Stop Condition.

## Parallel Fork And Convergence Protocol

1. Author and gate both T3/T4 child packets in one joint dispatch batch after
   accepted T2 evidence, commit it, then create one handoff-sync bridge.
2. Create two isolated worktrees/branches from that identical bridge HEAD.
3. T3 and T4 child packets must declare disjoint write ownership. If paths
   overlap, parallel execution is forbidden and Claude must serialize them.
4. Each branch runs focused tests, worker-return fast checks, and pre-commit
   gates before its checkpoint commit.
5. Integrate the first evidence branch without rewriting/squashing, create a
   handoff-sync bridge, then integrate the second evidence branch.
6. Create a convergence handoff-sync bridge and run combined tests/gates.
7. Author/gate the T5 child packet, bridge its dispatch commit, execute T5,
   commit the final return, and stop for Codex final review.

## Commit And Push Boundary

Claude may create private local commits required for dependency release,
parallel convergence, and the root-handoff-only bridge defined above. Claude
must not push, public-sync, force-push, rebase published history, alter remotes,
or edit other session continuity. Codex reviews the complete graph after T5 and
owns final closure, final session sync, and any later push.

## Stop Conditions

Claude stops and returns `BLOCKED_WITH_REASON` if:

- a child packet cannot source-verify an existing path, symbol, enum, or owner;
- a dependency checkpoint lacks a committed artifact or gate evidence;
- T3/T4 write ownership overlaps and safe serialization is not possible inside
  the child scope;
- any repair requires runtime/provider/live/public work, secrets/quota,
  destructive action, new authority semantics, or scope expansion;
- a child gate fails outside that child's allowed scope;
- T5 would need hook placement not justified by repeated-use evidence.

Allowed-scope gate failures must be repaired and rerun without asking the
operator.

## Return Contract

Claude returns exactly one final batch packet with:

- status `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`;
- dispatch HEAD, every child execution/checkpoint HEAD, T2 fork HEAD, T3/T4
  branch heads, integration HEAD, and final T5 HEAD;
- per-tranche changed-file manifests and tests/gates;
- dependency release ledger for every transition;
- T3/T4 disjointness and convergence evidence;
- final `git status --short` and `git log --graph --oneline` excerpt;
- unresolved findings routed by RSE/F2G;
- no claim of closure, effectiveness, provider behavior, or public readiness.

## Evidence / Verification

Dispatch evidence requires reviewer-fast, dispatch-quality, pre-dispatch,
commit-steward dispatch mode, and pre-commit checks over the real dispatch
range. Execution evidence is tranche-local: child source verification,
focused tests, real-range autorun gates, committed dependency anchors, and the
final graph/manifest return. Codex recomputes closure evidence after T5.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Disposition |
|---|---|---|---|---|
| `INTERNAL_AGENT` | local child packets, resolver, isolated worktrees, and root-handoff-only bridges | private machine-gated commits; no self-review or final closure authority | T0-T2 commits/reviews and bridge standard | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | no adapter authorized in this sequence | no ingress, authentication, approval, receipt, raw-data, mutation, runtime, or public claim | forbidden scope and T2 contract | `DEFERRED_WITH_REASON` - separate source-verified authorization required |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this authorization governs private provenance execution. No public
artifact, public-sync clone mutation, remote push, or public catalog claim is
authorized.

## Claim Boundary

This packet authorizes a governed private execution chain and local checkpoint
commits only. It does not pre-approve unknown child source facts, waive child
packets or gates, authorize runtime/provider/live/public behavior, prove agent
comprehension or defect prevention, or close any ADIF tranche before Codex
final review.
