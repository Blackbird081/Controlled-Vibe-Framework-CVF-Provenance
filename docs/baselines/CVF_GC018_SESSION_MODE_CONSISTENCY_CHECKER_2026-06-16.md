# GC-018 Session Mode-Consistency Checker

Memory class: FULL_RECORD

rawMemoryReleased: false

Baseline ID: GC018-SESSION-MODE-CONSISTENCY-CHECKER-2026-06-16

Date: 2026-06-16

Status: AUTHORIZED_SESSION_MODE_CONSISTENCY_CHECKER

dispatchBaseHead: 2a65298b

## Purpose

Authorize T1 of the Session Continuity Authoring And Mode-Consistency
Foundation roadmap: a checker that fails when the session mode marker disagrees
across its canonical surfaces (front door, active handoff, and
`ACTIVE_SESSION_STATE_CORE.json`).

## Decision

Proceed with T1 read-only checker plus wiring:

- `governance/compat/check_session_mode_consistency.py`;
- `governance/compat/test_check_session_mode_consistency.py`;
- additive wiring into reviewer-fast and the steward session-sync lane;
- completion review.

## Source / Predecessor Evidence

A real `currentMode` drift was introduced during the session-sync pack builder
session-sync and passed all 16 reviewer-fast checks, pre-commit, and the
session-sync steward. It was caught only by manual audit and repaired in commit
`7df9679d`.

Root cause: `governance/compat/check_active_session_state.py` line 366 only
validates that `currentMode` is a non-empty string. It never compares
`currentMode` against the front-door `Current mode marker:` line or the handoff
`## Current Mode` value. The surfaces can diverge silently.

Canonical marker surfaces verified at `2a65298b`:

- front door `CVF_SESSION_MEMORY.md`: `Current mode marker:` (line 9) and
  `Current mode:` (line 45);
- active handoff (resolved from `ACTIVE_SESSION_STATE.json` `activeHandoff`):
  `## Current Mode` value (line 31) and startup acknowledgment
  `current mode=` field (line 27);
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`: `currentMode` (line 63).

## Authorized Scope

Codex may create or modify:

- `governance/compat/check_session_mode_consistency.py` (new, read-only);
- `governance/compat/test_check_session_mode_consistency.py` (new);
- `governance/compat/run_local_governance_hook_chain.py` (additive entry in
  `REVIEWER_FAST_CHECKS` only);
- `governance/compat/run_agent_commit_steward_preflight.py` (additive command
  in the session-sync lane of `_mode_commands` only);
- `docs/reviews/CVF_SESSION_MODE_CONSISTENCY_CHECKER_COMPLETION_2026-06-16.md`.

## Not Authorized

- Writing, staging, or committing any session file from the checker;
- behavior change to `check_active_session_state.py` or
  `generate_active_session_state.py`;
- T2 session-sync authoring helper (separate dispatch after T1 closes);
- live API calls or credential use;
- public-sync;
- co-work product development;
- source edits outside the authorized paths;
- production or public readiness claims.

## Guard Requirements

`check_session_mode_consistency.py` must:

- resolve the active handoff path from `ACTIVE_SESSION_STATE.json`
  `activeHandoff`, not hardcode it;
- read the mode marker from each canonical surface and fail with a clear
  message when any surface disagrees;
- be read-only: no file write, no git stage, no git commit;
- support `--enforce` to exit non-zero on disagreement.

## Evidence / Verification

Codex must return focused test output, reviewer-fast output, session-sync
steward output, diff hygiene, and a completion review proving no session
mutation, runtime, provider, live, public-sync, or production scope was
touched.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 mode-consistency checker authorization |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | apply_patch, source inspection, governance gates |
| Target paths | this GC-018, Codex work order |
| Allowed scope source | operator approved session continuity authoring and mode-consistency foundation roadmap |
| Before status evidence | roadmap `ROADMAP_READY_FOR_GC018` at `2a65298b`; mode drift fixed `7df9679d` |
| After status evidence | Codex T1 implementation packet authorized |
| Diff evidence | GC-018/work order authoring range from `2a65298b` |
| Approval boundary | T1 read-only checker plus additive wiring only |
| Claim boundary | no runtime/provider/public/production claim |
| Agent type | Codex orchestrator |
| Invocation ID | `gc018-session-mode-consistency-checker-2026-06-16` |
| Expected manifest | `docs/baselines/CVF_GC018_SESSION_MODE_CONSISTENCY_CHECKER_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_MODE_CONSISTENCY_CHECKER_FOR_CODEX_2026-06-16.md`; `AGENT_HANDOFF_V19_2026-06-15.md` |
| Actual changed set | `docs/baselines/CVF_GC018_SESSION_MODE_CONSISTENCY_CHECKER_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_MODE_CONSISTENCY_CHECKER_FOR_CODEX_2026-06-16.md`; `AGENT_HANDOFF_V19_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance baseline. No public-sync batch is
authorized.

## Claim Boundary

This baseline authorizes one bounded read-only checker tranche. It does not
authorize session-file mutation, runtime behavior, provider calls, public-sync,
co-work product development, production readiness, or public readiness.
