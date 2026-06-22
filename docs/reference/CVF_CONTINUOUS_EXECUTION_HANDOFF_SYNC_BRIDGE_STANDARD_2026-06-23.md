# CVF Continuous Execution Handoff-Sync Bridge Standard

Memory class: FULL_RECORD

Status: ACTIVE_STANDARD

Date: 2026-06-23

docType: reference_standard

## Purpose

Preserve genuine continuous multi-tranche execution when GC-020 requires the
active handoff to recognize each new material HEAD, without converting every
checkpoint into a reviewer pause.

## Scope / Applies To

Applies to explicitly authorized `WORKER_MAY_COMMIT` multi-tranche sequences
whose intermediate material commits must satisfy GC-020 before the next local
machine gate. It does not apply to ordinary worker returns, final closure,
public-sync, provider/live execution, or any sequence without a named terminal
reviewer checkpoint.

## Core Distinction

A handoff-sync bridge is continuity bookkeeping, not review, acceptance,
closure, dependency judgment, or session-state ownership.

The allowed sequence is:

`material commit -> root-handoff-only bridge commit -> next machine gate`

The bridge records the material parent SHA so the active-state compatibility
checker can accept the dedicated handoff-only child commit. It does not release
work by human judgment; the governing continuous authorization and machine
dependency evidence do that.

## Eligibility

This bridge may be used only when all conditions hold:

- an explicit operator-approved continuous sequence exists;
- the authorization names the stages and terminal reviewer checkpoint;
- `WORKER_MAY_COMMIT` applies;
- the current material commit is inside a source-verified child scope;
- the next transition is already machine-authorized;
- no scope, risk, claim, runtime/provider/live/public, secret/quota, or
  destructive boundary changes.

Otherwise the normal reviewer/session-sync route applies.

## Exact Write Boundary

The bridge may edit exactly one file:

- the root active handoff named by `CVF_SESSION/ACTIVE_SESSION_STATE.json`.

It must not edit:

- `CVF_SESSION_MEMORY.md`;
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` or its generated sources;
- the review queue;
- roadmaps, work orders, baselines, implementation, tests, or public files.

The handoff edit may only append or refresh a bounded continuous-execution
bridge ledger row naming stage, material HEAD, evidence status, next
machine-authorized move, and stop-boundary statement. It must not change
current mode, canonical next move, acceptance, closure, or final disposition.

## Required Command And Commit Shape

After each material/dispatch/integration commit that must precede another gate:

1. capture the material HEAD;
2. update only the active handoff bridge ledger;
3. run
   `python governance/compat/run_agent_commit_steward_preflight.py --mode handoff-sync --base <materialHead> --head HEAD --enforce`;
4. run the normal pre-commit hook;
5. commit only the active handoff;
6. continue from the bridge commit without reviewer pause.

The bridge status token is `HANDOFF_SYNC_BRIDGE_PASS`. A child material packet
may use `CHECKPOINT_PASS_PENDING_FINAL_REVIEW`; neither token is a closed or
review-accepted status.

## Parallel Fork And Convergence

For parallel branches:

- author and gate both child packets before the common fork;
- create one handoff-sync bridge after the joint dispatch commit;
- fork both worktrees from that identical bridge HEAD;
- keep branch manifests disjoint;
- integrate one evidence branch, bridge its material HEAD, integrate the other,
  then bridge the convergence HEAD;
- do not squash or rewrite branch evidence;
- run combined tests/gates before the convergence-dependent tranche.

This bridge sequencing avoids stale-HEAD hook failures while preserving final
independent review of the complete graph.

## Stop Conditions

Stop rather than bridge when:

- the material checkpoint or required focused gate failed;
- the next dependency is not already authorized;
- the handoff edit would need any second file;
- the bridge would make an acceptance/closure claim;
- parallel manifests overlap without safe serialization;
- any forbidden expansion or operator checkpoint is triggered.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| handoff-sync is a dedicated root-active-handoff-only steward lane | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | handoff-sync mode and command | `handoff-sync` | commit steward protocol | VALUE_SET | ACCEPT |
| active handoff must recognize current HEAD or the parent of a dedicated continuity commit | `governance/compat/check_active_session_state.py` | GC-020 HEAD compatibility validation | active handoff HEAD check | active session checker | RUNTIME_BEHAVIOR | ACCEPT |
| phase-specific commit ownership may be assigned by the handoff contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | CF-07 and commit owner fields | `commitOwner(phase)` | Agent Handoff Contract | VALUE_SET | ACCEPT |
| continuous ADIF sequence already has machine-gated transitions and final Codex review | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | Continuous Execution Decision; Return Contract | `AUTO_RELEASE_WITH_EVIDENCE` | ADIF authorization | VALUE_SET | ACCEPT |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Disposition |
|---|---|---|---|---|
| `INTERNAL_AGENT` | local git/handoff steward lane | root-handoff-only continuity commit; no review or closure authority | commit steward `handoff-sync` mode | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | no external bridge interface | no ingress, authentication, approval, receipt, raw-data, mutation, or public behavior is authorized | exact write boundary | `N/A_WITH_REASON` - repository-local continuity operation only |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| reviewer-owned session sync after every worker commit turned continuous execution into micro-review | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_ADDED | use the root-handoff-only bridge for eligible continuous chains |

Runtime/provider/cost learning lane: N/A_WITH_REASON - no runtime/provider/cost
behavior changes.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance execution-control standard; no public-sync is
authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | repository-local handoff continuity bridge |
| claimDisposition | N/A with reason: no Delta execution-control behavior |
| receiptEvidence | N/A with reason: no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exact one-file git commit shape and steward gate |
| invocationBoundary | local governed continuous-execution sequence |
| interceptionBoundary | no IDE/shell/filesystem/provider interception claim |
| claimLanguage | continuity bridge only, not review or acceptance |
| forbiddenExpansion | session state, runtime/provider/live, public-sync, external adapter, readiness, universal control |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex governance hardening author |
| Provider or surface | local workspace |
| Session or invocation | ADIF T3-T5 continuous-execution hardening, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | governed reads, apply_patch, governance gates, git commit |
| Target paths | this standard; ADIF authorization; master work order; roadmap |
| Allowed scope source | operator instruction to harden T3-T5 continuous execution after T2 review |
| Before status evidence | T2 accepted at `07000fd6`; prior pattern paused at every tranche |
| After status evidence | reusable root-handoff-only bridge contract |
| Diff evidence | governed material diff and gate output |
| Approval boundary | governance choreography only; no T3-T5 implementation |
| Claim boundary | no external/runtime/public expansion |
| Agent type | dispatch/governance author |
| Invocation ID | `continuous-handoff-sync-bridge-hardening-2026-06-23` |
| Expected manifest | this standard; ADIF authorization; master work order; ADIF roadmap |
| Actual changed set | this standard; ADIF authorization; master work order; ADIF roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This standard authorizes only explicitly assigned root-handoff-only bridge
commits inside an already approved continuous sequence. It does not authorize
self-review, self-closure, session-state mutation, or scope expansion.
