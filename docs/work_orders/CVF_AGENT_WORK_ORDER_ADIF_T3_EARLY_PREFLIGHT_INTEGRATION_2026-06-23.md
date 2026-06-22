# CVF Agent Work Order - ADIF-T3 Early Preflight Integration

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

Date: 2026-06-23

docType: work_order

closureBaseHead: NOT_EXECUTED_YET

## Dispatch Prompt Envelope

Role: Claude continuous-execution orchestrator/worker, executing the T3
evidence branch of the joint ADIF-T3/T4 dispatch, forked from the
handoff-sync bridge HEAD.

Canonical packet:
`docs/baselines/CVF_GC018_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md`

Commit mode: `WORKER_MAY_COMMIT`

dispatchBaseHead: `617b041f` (the ADIF-T3/T4 joint dispatch handoff-sync
bridge HEAD).

executionBaseHead: `617b041f` (confirmed via `git rev-parse --short HEAD`
before any edit in this branch).

Current-time notes: this is the T3 evidence branch only. Real OS-level
worktree isolation was attempted via `EnterWorktree` and failed on this
machine (Windows path-length limit triggered by an existing long governed
checker filename already in the repository, unrelated to ADIF). The
operator authorized serialized execution in the single working directory
in place of literal worktree isolation, since T3 and T4 declare fully
disjoint write ownership and the disjointness guarantee holds regardless
of whether isolation is enforced by the filesystem or by write-ownership
discipline.

Do-not-misread notes: this checkpoint covers only the two T3 paths listed
below. It does not touch any T4 path, any autorun command list, or any
session/handoff file beyond what the joint dispatch and its own bridge
already cover.

Required first actions: none beyond the joint dispatch's Required First
Reads, already completed before this branch began.

Return contract: this branch returns `COMPLETE_PENDING_REVIEW`; per the
operator's continuous-execution instruction, Claude continues directly
into the T4 branch without a Codex pause.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one read-only ADIF preflight
readout helper plus its focused test under `governance/compat/`, per the
ADIF-T3/T4 joint GC-018 baseline's Allowed scope (ADIF-T3 branch).

Protected paths (every changed guard/control path is listed):

- `governance/compat/run_adif_preflight_readout.py`
- `governance/compat/test_run_adif_preflight_readout.py`

Operator authorization: the operator pre-selected the T0-T5 continuous
sequence and instructed Claude to execute T3->T4->T5 continuously without
a Codex pause, per the joint GC-018 baseline and the Continuous Execution
Handoff-Sync Bridge Standard.

Rollback boundary: if this T3 branch is rejected, remove only the two
named paths above and this work order. Do not revert the ADIF-T3/T4 joint
dispatch commit (`af56db7c`) or its handoff-sync bridge (`617b041f`).

Scope boundary: this authorization does not extend to existing guard
behavior, active session files, root handoff files, runtime/product
source, public-sync, provider/live proof, direct-interception tooling, or
any CLI/MCP adapter.

## Scope / Owner Boundary

Allowed scope: create `governance/compat/run_adif_preflight_readout.py`
and `governance/compat/test_run_adif_preflight_readout.py` only, per the
joint GC-018 baseline's T3 Allowed scope. Forbidden scope is identical to
the joint baseline's Forbidden scope for ADIF-T3/T4.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `governance/compat/run_adif_preflight_readout.py` | Claude (T3 branch) | create |
| `governance/compat/test_run_adif_preflight_readout.py` | Claude (T3 branch) | create |
| this work order | Claude (T3 branch) | create, commit |

## Mission

Implement the ADIF-T3 read-only preflight defect-packet readout module and
its focused tests, per the joint GC-018 baseline.

## Purpose

Give agents a bounded, human-readable readout of relevant ADIF entries
during pre-implementation context, without duplicating the ADIF-T2
resolver's matching/ordering logic and without creating a competing
autorun process.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority; pre-selected the T0-T5 continuous sequence |
| Dispatcher | Claude authored the joint T3/T4 GC-018 baseline and this T3 branch packet |
| Orchestrator/worker | Claude |
| Reviewer/closer | Codex, once after the complete T0-T5 graph returns |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Claude orchestrates and executes the T3 branch under `WORKER_MAY_COMMIT`; Codex reviews and closes the complete T0-T5 chain once after T5 |
| phase | EXECUTION |
| baseHeadFor(phase) | `executionBaseHead=617b041f` (joint dispatch handoff-sync bridge HEAD) |
| changedSetScope(phase) | T3 branch = readout module, readout test, this work order |
| traceScope(phase, actor) | one trace covers this T3 branch checkpoint |
| commitOwner(phase) | Claude commits this T3 checkpoint under `WORKER_MAY_COMMIT` |
| crossBatchIsolation | T3 declares zero shared paths with T4; both converge into the same branch without overlap |
| nextMoveSurfaces | Claude continues directly into the T4 branch without a Codex pause |
| Closer designation | Codex |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Joint ADIF-T3/T4 GC-018 baseline | `docs/baselines/CVF_GC018_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md` | ACCEPT |
| Joint ADIF-T3/T4 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md` | ACCEPT |
| Handoff-sync bridge after joint dispatch | `617b041f` | ACCEPT |
| Continuous Execution Handoff-Sync Bridge Standard | `docs/reference/CVF_CONTINUOUS_EXECUTION_HANDOFF_SYNC_BRIDGE_STANDARD_2026-06-23.md` | ACCEPT |

## Required First Reads

Inherited in full from the joint ADIF-T3/T4 GC-018 baseline's Required
First Reads, already completed before this branch began:
`docs/baselines/CVF_GC018_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md`.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python -m pytest governance/compat/test_run_adif_preflight_readout.py -v
```

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | one new sibling `governance/compat/run_adif_preflight_readout.py` module plus matching test file, following existing flat-import compat conventions |
| Storage decision | one readout module, one test module; no generated aggregate; no relocation or refactor of any existing file |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | read-only local function calls over the existing ADIF-T2 resolver; no runtime memory store, no CLI/MCP surface |

## Execution Plan

1. Confirm `executionBaseHead` and clean worktree.
2. Implement `run_adif_preflight_readout.py` calling the existing
   `resolve_defect_packet` function.
3. Implement `test_run_adif_preflight_readout.py` with focused coverage.
4. Run focused tests; confirm all pass.
5. Confirm no autorun wiring via `grep`.
6. Run real-range pre-implementation gate; repair and rerun until clean.
7. Commit the T3 branch checkpoint; continue directly into the T4 branch.

## Evidence Requirements

- `python -m pytest governance/compat/test_run_adif_preflight_readout.py -v`
  result with all 7 tests passing;
- `grep -n "run_adif_preflight_readout" governance/compat/run_agent_autorun_workflow_gate.py`
  returns no match, confirming no autorun wiring;
- exact claim boundary and public export disposition.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | Readout calls the existing resolver and formats output without duplicating matching logic | `test_does_not_duplicate_resolver_matching_logic` |
| AC2 | No filesystem mutation | `test_human_text_includes_claim_boundary_and_does_not_mutate_filesystem` |
| AC3 | Bounded by `max_results` | `test_readout_is_bounded_by_max_results` |
| AC4 | No competing autorun process created | `grep` against `run_agent_autorun_workflow_gate.py` |
| AC5 | Focused tests pass | `pytest` run: 7/7 |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| `EnterWorktree` failed on this machine due to a pre-existing long governed-checker filename hitting the Windows path-length limit | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_CANDIDATE | route a future separate tranche to evaluate `core.longpaths` or filename shortening for the offending checker; not in ADIF-T3 scope |

Runtime/provider/cost learning lane: N/A_WITH_REASON - the worktree failure
is a local filesystem/git-config condition, not provider/cost behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-implementation work. No public-sync
repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude continuous-execution orchestrator/worker |
| Provider or surface | local workspace |
| Session or invocation | ADIF-T3 branch execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | file write tool, pytest, governance gates, git commit |
| Target paths | this work order; readout module; readout test |
| Allowed scope source | joint ADIF-T3/T4 GC-018 baseline's T3 Allowed scope |
| Before status evidence | executionBaseHead `617b041f`; clean worktree confirmed |
| After status evidence | T3 branch checkpoint committed; execution continues directly into the T4 branch |
| Diff evidence | T3-branch-only name-status and committed diff |
| Approval boundary | ADIF-T3 branch scope only |
| Claim boundary | read-only readout helper; no runtime/public/provider/external-adapter expansion |
| Agent type | continuous-execution orchestrator/worker |
| Invocation ID | `adif-t3-branch-execution-2026-06-23` |
| Expected manifest | this work order; readout module; readout test |
| Actual changed set | this work order; readout module; readout test |
| Manifest delta | MATCH |

## Review Gate

Codex reviews the T3 branch as part of the complete T0-T5 graph review
once after T5. No per-branch reviewer pause is required, per this turn's
explicit instruction and the Continuous Execution Handoff-Sync Bridge
Standard.

## Closure Checklist

- [x] T3 readout module and test created inside Allowed scope only.
- [x] Focused tests pass (7/7).
- [x] No autorun wiring confirmed via `grep`.
- [x] Core Guard Self-Protection Authorization block present for both
      protected paths.
- [ ] Codex review of the complete T0-T5 graph after T5 (pending; not
      owned by this branch packet).

## Return-To-Orchestrator Conditions

Return success as `COMPLETE_PENDING_REVIEW` for this T3 branch and
continue directly into the T4 branch. Return `BLOCKED_WITH_REASON` for any
Stop Condition in the canonical authorization or the bridge standard.

## Operator Checkpoint

The human principal pre-selected the entire continuous sequence and this
turn separately instructed Claude to run T3->T4->T5 continuously without a
Codex pause. A fresh pause applies only to scope/risk/claim expansion,
runtime/provider/live/public work, secrets/quota, destructive action,
canonical-owner semantic change, write ownership overlap that cannot be
safely serialized, or a different execution order than the one named
above.

## Claim Boundary

This work order records only the ADIF-T3 branch checkpoint. It does not
authorize ADIF-T4 or T5 implementation, any CLI/MCP adapter, or final
closure. Codex remains the designated final reviewer/closer for the
complete T0-T5 chain.
