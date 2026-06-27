# CVF GC-018 Commit Closure Latency Control Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-15

Owner: Codex Orchestrator

---

## Purpose

Authorize a bounded CVF governance-control batch that reduces total
commit/closure latency by separating the final active-handoff-only sync lane
from broader session-state synchronization.

This responds to the operator finding that the P3/P4A closure took too long
because material review, closure review, session sync, and final handoff sync
were still too easy to collapse into repeated full-gate attempts.

## Scope

Allowed scope:

- add a narrow `handoff-sync` mode to the commit steward preflight;
- make the steward print the recommended lane for the observed changed set;
- add focused tests for handoff-only fast-lane acceptance and mixed-session
  rejection;
- update the commit steward standard and `AGENTS.md` pointer guidance;
- author this baseline and completion review for bounded closure.

Forbidden scope:

- disabling, weakening, bypassing, or removing existing hooks or autorun gates;
- authorizing `--no-verify`;
- granting worker commit rights;
- changing provider/live/public/runtime behavior;
- changing Model Gateway P4B, EPF wiring, strategy layer, or AI Gateway scope.

## Source / Predecessor Evidence

| Source | Use in this baseline |
| --- | --- |
| `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | Existing steward protocol extended with handoff-only lane. |
| `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | Existing material/session/handoff split rule retained. |
| `governance/compat/check_active_session_state.py` | Already accepts parent-present-for-sync-commit for dedicated session/handoff sync commits. |
| Operator instruction 2026-06-15 | Requested CVF foundation hardening after 18m29s commit/closure latency finding. |

## Decision / Baseline / Proposed Tranche

Decision: approve a bounded commit-closure latency control hardening tranche.

Baseline: full phase gates remain authoritative. The new lane only narrows the
preflight used when the changed set is root active-handoff-only.

Proposed tranche: add `handoff-sync` to `run_agent_commit_steward_preflight.py`
so agents use `session-sync` for generated/front-door state changes and
`handoff-sync` for final active-handoff-only continuity commits.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update the commit steward preflight,
focused tests, steward standard, and `AGENTS.md` guidance so future agents can
select the narrowest safe commit lane and avoid rerunning unrelated generated
state checks for handoff-only commits.

Protected paths:

- `AGENTS.md`
- `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`
- `governance/compat/run_agent_commit_steward_preflight.py`
- `governance/compat/test_run_agent_commit_steward_preflight.py`

Governance artifacts in this batch:

- `docs/baselines/CVF_GC018_COMMIT_CLOSURE_LATENCY_CONTROL_HARDENING_2026-06-15.md`
- `docs/reviews/CVF_COMMIT_CLOSURE_LATENCY_CONTROL_HARDENING_COMPLETION_2026-06-15.md`

Operator authorization: 2026-06-15 operator instruction "Nang nen CVF di" after
the explicit latency finding and Codex recommendation for commit/closure latency
control.

Rollback boundary: revert exactly this baseline, the completion review, the
steward script/test changes, the steward standard addendum, and the AGENTS.md
guidance. Do not revert Model Gateway P3/P4A material commit `5d46bc62`,
closure/sync commit `21c8a9e2`, or handoff-sync commit `9df57da0`.

## Evidence / Verification

Required verification before material commit:

| Gate | Command | Expected result |
| --- | --- | --- |
| Focused steward tests | `python -m pytest governance/compat/test_run_agent_commit_steward_preflight.py -q` | PASS |
| Handoff-sync plan check | `python governance/compat/run_agent_commit_steward_preflight.py --mode handoff-sync --base HEAD~1 --head HEAD --enforce --plan-only` | PASS on a handoff-only range |
| Agent trace | `python governance/compat/check_agent_operation_trace.py --base 9df57da0 --head HEAD --enforce` | PASS |
| Diff hygiene | `git diff --check` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control hardening. Public-sync is not
authorized by this baseline.

## Claim Boundary

This baseline authorizes only control-plane latency hardening for commit
steward preflight selection. It does not reduce mandatory guard coverage,
change runtime/provider behavior, run live proof, authorize public-sync, claim
production readiness, or open Model Gateway P4B.
