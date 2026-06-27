# CVF GC-018 Agent Commit Steward Protocol Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-15

Owner: Codex Orchestrator

---

## Purpose

Authorize a bounded governance-control batch that standardizes faster governed
commit preparation across agents without weakening guard coverage.

## Scope

Allowed scope:

- add an agent-neutral commit steward protocol standard;
- add a steward preflight wrapper;
- add focused tests for path classification and commit-shape risk detection;
- add a pointer in `AGENTS.md` so future agents use the same flow.

Forbidden scope:

- disabling, weakening, or bypassing existing hooks;
- authorizing `--no-verify`;
- changing runtime/provider/live/public behavior;
- granting worker commit rights;
- changing unrelated governance gates.

## Source / Predecessor Evidence

| Source | Use in this baseline |
| --- | --- |
| `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | Existing phase-gate authority retained. |
| `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | Existing material/session split lesson retained. |
| `docs/reference/CVF_SINGLE_AGENT_MULTI_ROLE_CONTROL_STANDARD_2026-06-11.md` | Single-agent multi-role boundary retained. |
| `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | Exact changed-set conflict handled by commit-shape planning. |
| Operator instruction 2026-06-15 | Requested faster total governed commit workflow with guards preserved. |

## Decision / Baseline / Proposed Tranche

Decision: approve bounded commit steward protocol hardening now.

Baseline: existing autorun phase gates and git hooks remain authoritative and
are not weakened.

Proposed tranche: add an agent-neutral preflight wrapper and standard so agents
run the correct phase gate once, catch commit-shape conflicts early, and split
material/session-sync commits when required.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add the commit steward protocol and wrapper
so future agents reduce total elapsed commit time by running the correct phase
preflight early and by splitting material/session-sync commits when needed.

Protected paths:

- `AGENTS.md`
- `governance/compat/run_agent_commit_steward_preflight.py`
- `governance/compat/test_run_agent_commit_steward_preflight.py`

Operator authorization: 2026-06-15 operator instruction requested foundation
hardening for faster total governed commit time while preserving guards and
supporting any agent, including single-agent multi-role execution.

Rollback boundary: revert this baseline, the new standard, the steward
script/test, and the AGENTS.md pointer only. Do not revert Model Gateway C-02
P2 dispatch commit `eea131ec` or session sync commit `91b94856`.

## Evidence / Verification

Required verification before material commit:

| Gate | Command | Expected result |
| --- | --- | --- |
| Focused tests | `python -m pytest governance/compat/test_run_agent_commit_steward_preflight.py` | PASS |
| Steward preflight | `python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 91b94856 --head HEAD --enforce` | PASS |
| Markdown structure | `python governance/compat/check_markdown_structural_completeness.py --base 91b94856 --head HEAD --enforce` | PASS |
| Diff hygiene | `git diff --check` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control hardening. Public-sync is not
authorized by this baseline.

## Claim Boundary

This baseline authorizes only the bounded commit steward control-plane
hardening. It does not claim runtime behavior, provider readiness, live proof,
public readiness, production readiness, or a reduction in the number of
mandatory guard checks. The expected value is fewer failed commit attempts and
less repeated agent latency.
