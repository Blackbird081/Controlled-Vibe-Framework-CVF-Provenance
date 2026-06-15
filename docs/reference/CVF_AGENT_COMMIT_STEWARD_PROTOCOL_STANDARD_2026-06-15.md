# CVF Agent Commit Steward Protocol Standard

Memory class: FULL_RECORD

Status: ACTIVE_STANDARD

docType: reference

Date: 2026-06-15

Authority: operator request after Model Gateway C-02 P2 dispatch commit latency

---

## Purpose

Reduce total agent commit latency without weakening CVF guard coverage.

The protocol is agent-neutral. It applies whether Codex, Claude, another agent,
or one agent in multiple roles prepares the commit. The optimization target is
elapsed workflow time, not convenience for a specific provider.

## Scope

This standard applies to any governed CVF batch that:

- commits or prepares a commit for work orders, roadmaps, baselines, reviews,
  standards, guards, source, tests, session state, or handoff files;
- uses `WORKER_MUST_NOT_COMMIT` or `WORKER_MAY_COMMIT`;
- uses single-agent multi-role execution;
- changes active session front-door or generated state files;
- includes an Agent Operation Trace Block;
- runs autorun workflow gates.

## Core Principle

Keep guard coverage intact, but move failure discovery earlier and split commits
so one gate family does not invalidate another.

Do not use `--no-verify` as the normal speed path. Faster CVF commits come from:

- capturing the correct base before edits;
- running the phase-appropriate steward preflight before commit;
- avoiding duplicate fast/full gate runs unless the phase requires both;
- separating material artifacts from session/handoff sync;
- resolving manifest and protected-path conflicts before invoking `git commit`.

## Required Steward Command

Before a governed commit or worker return handoff, run the steward preflight for
the matching mode:

```powershell
python governance/compat/run_agent_commit_steward_preflight.py --mode <mode> --base <baseHead> --head HEAD --enforce
```

Allowed modes:

| Mode | Use when | Primary gate |
| --- | --- | --- |
| `dispatch` | Releasing a roadmap/work order/baseline to a worker | autorun `pre-dispatch` |
| `implementation` | Worker starts or validates implementation scope | autorun `pre-implementation` |
| `reviewer-return` | Reviewer inspects uncommitted worker artifacts | `reviewer-fast` |
| `closure` | Reviewer/committer validates committed closure range | autorun `pre-closure` |
| `push` | Preparing public or remote push | autorun `pre-push` |
| `session-sync` | Updating only session front-door/state/handoff continuity | active session and generated-state checks |

`--enforce` fails high-risk commit-shape conflicts. Without `--enforce`, the
script reports the same diagnostics but exits successfully unless a commanded
gate fails.

## Commit Split Rule

Material artifacts and session/handoff sync should be separate commits.

Default sequence:

1. Material commit: source, tests, work order, baseline, review, standard,
   guard, or registry artifacts owned by the work.
2. Session-sync commit: `CVF_SESSION_MEMORY.md`,
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION/state/**`, active
   handoff, and related continuity pointers.

Do not mix material artifacts with active handoff/session sync when an Agent
Operation Trace Block requires an exact `Actual changed set`, unless the
artifact explicitly authorizes the mixed protected-path manifest and the machine
gate accepts the exact observed paths.

## Single-Agent Multi-Role Rule

A single agent may execute multiple roles only if the evidence is separated by
phase and commit shape:

- role changes must be stated in the artifact;
- base heads must be captured per phase;
- material and session-sync commits remain separate when both are needed;
- worker evidence, reviewer evidence, and committer evidence must not be
collapsed into a single unqualified PASS claim;
- committed-range `pre-closure` remains reviewer/committer evidence even if the
same agent authored the worker artifacts.

## `WORKER_MUST_NOT_COMMIT` Rule

For `WORKER_MUST_NOT_COMMIT`, the worker leaves artifacts uncommitted and may
run `reviewer-return` or focused tests. The reviewer/committer owns:

- final material commit;
- committed-range `pre-closure`;
- session-sync commit if state changes;
- final clean-worktree claim.

The worker must not claim committed-range closure from uncommitted artifacts.

## Latency Discipline

Run only the gate set that matches the phase:

- dispatch packets: steward `dispatch`; do not also run `reviewer-fast` unless
  a no-commit worker return is being reviewed;
- worker returns: steward `reviewer-return`; do not claim closure from it;
- closure: steward `closure` after material commit; do not use `--base HEAD
  --head HEAD`;
- session sync: steward `session-sync` instead of the full phase gate when no
  material artifact is changing.

The git hook remains the final local confirmation layer. The steward preflight
exists to reduce repeated failed commits, not to replace hooks.

## Evidence Requirements

Commit or closure evidence should record:

- steward mode;
- base head and head;
- changed-path summary;
- material paths;
- protected session paths;
- split recommendation or `N/A with reason`;
- gate result;
- whether `--enforce` was used.

## Failure Conditions

The steward preflight must block or return to orchestrator when:

- the selected mode does not match the work phase;
- `closure` or `push` uses an empty committed range;
- an Agent Operation Trace exact-manifest artifact is mixed with active
  session/handoff sync in a way that would change the observed set;
- generated active session state is edited without source JSON alignment;
- protected session files are changed without an authorized session-sync
  boundary;
- a worker in `WORKER_MUST_NOT_COMMIT` tries to commit or claim committed-range
  closure.

## Related Artifacts

- `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`
- `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`
- `docs/reference/CVF_SINGLE_AGENT_MULTI_ROLE_CONTROL_STANDARD_2026-06-11.md`
- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`
- `governance/compat/run_agent_commit_steward_preflight.py`

## Core Guard Self-Protection Authorization

This batch is authorized as bounded governance control-plane hardening in
response to the operator request on 2026-06-15 to reduce total governed commit
latency while keeping guard coverage.

Protected paths authorized in this batch:

- `AGENTS.md`
- `governance/compat/run_agent_commit_steward_preflight.py`
- `governance/compat/test_run_agent_commit_steward_preflight.py`

Allowed changes:

- add the agent-neutral commit steward protocol to active agent instructions;
- add the steward preflight wrapper;
- add focused tests for path classification and high-risk commit-shape
  detection.

Forbidden changes:

- disabling, weakening, or removing existing hooks;
- authorizing `--no-verify`;
- granting worker commit rights;
- changing provider/live/public behavior;
- changing unrelated governance gates.

Rollback boundary: revert this standard, the steward script/test, and the
AGENTS.md pointer only. Do not revert Model Gateway C-02 P2 dispatch commit
`eea131ec` or session sync commit `91b94856`.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex |
| Provider or surface | Codex CLI |
| Session or invocation | Commit steward foundation hardening from HEAD `91b94856` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read current autorun/hook/commit choreography files; create GC-018 authorization baseline; create standard; create steward preflight script; create focused tests; update AGENTS.md pointer |
| Target paths | `AGENTS.md`; `docs/baselines/CVF_GC018_AGENT_COMMIT_STEWARD_PROTOCOL_HARDENING_2026-06-15.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/test_run_agent_commit_steward_preflight.py` |
| Allowed scope source | Operator instruction 2026-06-15: "nang nen" for faster total governed commit time while keeping guards and supporting any agent or single-agent multi-role |
| Before status evidence | HEAD `91b94856`; worktree clean before this hardening batch |
| After status evidence | `git status --short` shows exactly the five target paths before material commit |
| Diff evidence | `git diff --check` and steward preflight expected PASS before commit |
| Approval boundary | Operator authorized foundation hardening; no runtime/provider/live/public behavior authorized |
| Claim boundary | Repo-local trace only; no OS telemetry, provider-internal log, public readiness, production readiness, or runtime behavior claim |
| Agent type | Single agent acting as orchestrator/implementer/reviewer for a governance-control batch |
| Invocation ID | Commit steward hardening session from HEAD `91b94856` |
| Expected manifest | `AGENTS.md`; `docs/baselines/CVF_GC018_AGENT_COMMIT_STEWARD_PROTOCOL_HARDENING_2026-06-15.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/test_run_agent_commit_steward_preflight.py` |
| Actual changed set | `AGENTS.md`; `docs/baselines/CVF_GC018_AGENT_COMMIT_STEWARD_PROTOCOL_HARDENING_2026-06-15.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/test_run_agent_commit_steward_preflight.py` |
| Manifest delta | MATCH |

## Claim Boundary

This standard does not reduce required governance coverage, authorize
`--no-verify`, bypass git hooks, grant worker commit rights, authorize public
push, or claim production readiness. It standardizes the fastest governed path
by making the correct preflight, split, and evidence sequence repeatable across
agents.
