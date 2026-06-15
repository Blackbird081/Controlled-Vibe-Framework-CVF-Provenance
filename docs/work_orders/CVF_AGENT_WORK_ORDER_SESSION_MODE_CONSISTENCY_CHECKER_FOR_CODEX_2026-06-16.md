# CVF Agent Work Order - Session Mode-Consistency Checker For Codex

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-16

Owner / Orchestrator: Codex

Implementer: Codex

Reviewer / closer: Codex, with machine gates

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: 2a65298b

executionBaseHead: 2a65298b

closureBaseHead: 2a65298b

riskCeiling: R0_GOVERNANCE_TOOLING_ONLY

rawMemoryReleased: false

completionReviewPath:
`docs/reviews/CVF_SESSION_MODE_CONSISTENCY_CHECKER_COMPLETION_2026-06-16.md`

## Purpose

Implement T1 of the session continuity foundation: a read-only checker that
fails when the session mode marker disagrees across the front door, active
handoff, and `ACTIVE_SESSION_STATE_CORE.json`. This closes the gate gap that
let a real `currentMode` drift pass every check until manual audit.

## 1. Mission

Add `governance/compat/check_session_mode_consistency.py`, a read-only checker
that reads the mode marker from each canonical surface and exits non-zero on
disagreement, plus focused tests and additive wiring into reviewer-fast and the
steward session-sync lane.

## 2. Authority Chain

- Operator instruction: 2026-06-16, approved the session continuity authoring
  and mode-consistency foundation roadmap and the T1 next move.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.
- Roadmap:
  `docs/roadmaps/CVF_SESSION_CONTINUITY_AUTHORING_AND_MODE_CONSISTENCY_FOUNDATION_ROADMAP_2026-06-16.md`.
- GC-018:
  `docs/baselines/CVF_GC018_SESSION_MODE_CONSISTENCY_CHECKER_2026-06-16.md`.

Authority boundary: T1 read-only checker plus additive wiring only. T2 authoring
helper and all parked lanes remain held.

## 3. Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator | Codex | scope, dispatch, boundary guard |
| Implementer | Codex | new checker, tests, additive wiring, completion review |
| Reviewer / closer | Codex plus machine gates | inspect diff, run gates, commit |
| Operator | Human | T2 dispatch, scope expansion, public-sync |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | Operator approved roadmap and T1 next move; Codex owns implementation and closure |
| Scope classification | Bounded R0 governance tooling: new read-only checker, tests, additive wiring |
| Risk sensitivity | No public sync, no provider call, no live proof, no secret use, no session mutation, no behavior change to existing checkers, no production claim |
| Selected role route | `SINGLE_AGENT_MULTI_ROLE` |
| Role separation basis | Codex executes implementation and reviewer duties with machine gates and distinct material/session commits |
| Escalation condition | Stop for session-file mutation, behavior change to existing checkers, T2 scope, network, credentials, or public-sync |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Role separation ledger | Codex records implementation, focused tests, wiring, material commit, pre-closure, and session-sync as distinct steps |
| Evidence basis independent of memory | Checker output, test run, reviewer-fast, diff hygiene, pre-closure gate, and git status are required evidence |
| Self-review boundary | Self-review bounded by machine gates and explicit completion review evidence; no independent external review claimed |
| Escalation conditions | Stop for session-file mutation, behavior change to existing checkers, T2 scope, credentials, network, public-sync, or risk expansion |
| Gate sequence | pre-dispatch before dispatch commit; focused tests and reviewer-fast before material commit; pre-closure on material range; session-sync steward before continuity commit |

## 4. Required First Reads

| File | Required use |
|---|---|
| `CVF_SESSION_MEMORY.md` | front-door marker locations (lines 9, 45) |
| `AGENT_HANDOFF_V19_2026-06-15.md` | handoff marker locations (lines 27, 31) |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | `currentMode` location (line 63) |
| `governance/compat/check_active_session_state.py` | existing structural checks to avoid duplicating; `FRONT_DOOR_PATH` line 35 |
| `governance/compat/run_local_governance_hook_chain.py` | `REVIEWER_FAST_CHECKS` wiring point at line 24 |
| `governance/compat/run_agent_commit_steward_preflight.py` | session-sync lane in `_mode_commands` at line 213 |
| `docs/baselines/CVF_GC018_SESSION_MODE_CONSISTENCY_CHECKER_2026-06-16.md` | GC-018 authorized scope |

## 5. Allowed Scope

Codex may create or modify:

| Path | Action |
|---|---|
| `governance/compat/check_session_mode_consistency.py` | create (read-only checker) |
| `governance/compat/test_check_session_mode_consistency.py` | create |
| `governance/compat/run_local_governance_hook_chain.py` | additive entry in `REVIEWER_FAST_CHECKS` only |
| `governance/compat/run_agent_commit_steward_preflight.py` | additive command in session-sync lane of `_mode_commands` only |
| `docs/reviews/CVF_SESSION_MODE_CONSISTENCY_CHECKER_COMPLETION_2026-06-16.md` | create |
| `AGENT_HANDOFF_V19_2026-06-15.md` | session-sync update once material SHA exists |
| `CVF_SESSION_MEMORY.md` | session-sync update once material SHA exists |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | session-sync update |
| `CVF_SESSION/state/entries/lastUpdated.json` | session-sync update |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | session-sync regeneration |

## 6. Forbidden Scope And Stop Conditions

Stop before:

- writing, staging, or committing any file as a side effect of the checker;
- changing behavior of `check_active_session_state.py` or
  `generate_active_session_state.py`;
- implementing the T2 authoring helper (separate dispatch after T1 closes);
- any network call, credential read, or secret use;
- public-sync;
- co-work product or platform development;
- production or public readiness claims;
- session-file mutation in the material commit (session-sync is a separate
  follow-up batch; the material commit must close first).

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Front-door mode marker line | `CVF_SESSION_MEMORY.md` | line 9 | `Current mode marker:` | front-door front matter | ACCEPT |
| Front-door secondary mode line | `CVF_SESSION_MEMORY.md` | line 45 | `Current mode:` | front-door Current State | ACCEPT |
| Handoff startup ack mode field | `AGENT_HANDOFF_V19_2026-06-15.md` | line 27 | `current mode=` | handoff Startup Acknowledgment | ACCEPT |
| Handoff Current Mode value | `AGENT_HANDOFF_V19_2026-06-15.md` | line 31 | `## Current Mode` | handoff Current Mode | ACCEPT |
| Core currentMode field | `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | line 63 | `currentMode` | active session core | ACCEPT |
| activeHandoff resolution key | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | line 35 | `activeHandoff` | aggregate active session state | ACCEPT |
| Front-door path constant | `governance/compat/check_active_session_state.py` | line 35 | `FRONT_DOOR_PATH` | check_active_session_state module | ACCEPT |
| Reviewer-fast checks list | `governance/compat/run_local_governance_hook_chain.py` | line 24 | `REVIEWER_FAST_CHECKS` | hook chain runner | ACCEPT |
| Steward session-sync lane | `governance/compat/run_agent_commit_steward_preflight.py` | line 179 | `_mode_commands` | commit steward preflight | ACCEPT |

## 6A. Source-Fidelity Pass

Existing paths verified at `2a65298b`:

- `CVF_SESSION_MEMORY.md` -- EXISTS; markers at lines 9 and 45.
- `AGENT_HANDOFF_V19_2026-06-15.md` -- EXISTS; markers at lines 27 and 31.
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` -- EXISTS; `currentMode` line 63.
- `governance/compat/run_local_governance_hook_chain.py` -- EXISTS; `REVIEWER_FAST_CHECKS` line 24.
- `governance/compat/run_agent_commit_steward_preflight.py` -- EXISTS; session-sync lane line 213.

Planned new paths (NEW, no runtime claim):

- `governance/compat/check_session_mode_consistency.py` -- NEW.
- `governance/compat/test_check_session_mode_consistency.py` -- NEW.
- `docs/reviews/CVF_SESSION_MODE_CONSISTENCY_CHECKER_COMPLETION_2026-06-16.md` -- NEW.

## Current Runtime Freshness Verification

This work order claims no provider calls, no network use, no API key use, no
live proof, and no behavior change to existing checkers. The checker is
read-only and reads only repo-local session files.

Search evidence:

- No `fetch`, `http`, `requests`, or `urllib` calls authorized or present.
- No `.env` or credential path read authorized or present.
- `check_active_session_state.py` and `generate_active_session_state.py` are
  read-only in this tranche; the new checker adds the cross-surface marker
  agreement check that line 366 of `check_active_session_state.py` does not
  perform.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: All source verification rows recomputed from current file reads at 2a65298b. No prior verification artifact exists for this tranche.

unicodePathHandling: literal paths only; all source file reads use UTF-8-safe encoding with errors=replace; no Unicode-path corpus evidence is used.

extractedTextAuthority: SOURCE_AUTHORITY

Text encoding: all authored prose uses ASCII only.

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order section | Output artifact | Verification | Status |
|---|---|---|---|---|
| Checker fails on cross-surface marker disagreement | Section 5; mission | `check_session_mode_consistency.py` | focused test asserting non-zero exit on drift | OPEN |
| Checker passes when surfaces agree | Section 5 | checker | focused test on clean tree | OPEN |
| Resolve handoff path from activeHandoff, not hardcode | Section 6 forbidden; source verification | checker | code review in completion | OPEN |
| Wire into reviewer-fast | Section 5 | `run_local_governance_hook_chain.py` | reviewer-fast lists the checker | OPEN |
| Wire into session-sync steward lane | Section 5 | `run_agent_commit_steward_preflight.py` | session-sync steward runs the checker | OPEN |
| Read-only: no write/stage | Section 6 forbidden | checker | completion claim boundary | OPEN |
| Focused tests | Section 5 | `test_check_session_mode_consistency.py` | test run output | OPEN |
| Completion review with trace block | Section 5 | completion review | `Manifest delta: MATCH` | OPEN |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for all non-destructive
actions inside this work order's Allowed scope: reading named files, running
`git status`/`git diff`/`git rev-parse` and listed governance gates, creating
the three new files, applying additive wiring to the two named runners, running
focused tests/reviewer-fast/diff hygiene/pre-closure, committing the material
batch, and running the session-sync batch as a separate follow-up commit.

Escalation is reserved for: session-file mutation in the material commit,
behavior change to existing checkers, T2 scope, network calls, credential use,
public-sync, scope expansion, or destructive action. Routine gate failures
inside Allowed scope are mandatory remediation, not operator-preference
checkpoints.

## Pre-Flight Checks

| Check | Command | Expected |
|---|---|---|
| Active session state | `python governance/compat/check_active_session_state.py --enforce` | PASS |
| Worktree before edits | `git status --short` | clean |
| Execution base | `git rev-parse --short HEAD` | `2a65298b` |

## 7. Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Verify HEAD = `2a65298b`; run active session state check | startup confirmation |
| 2 | Author `check_session_mode_consistency.py` reading all canonical surfaces; resolve handoff from `activeHandoff` | new checker |
| 3 | Author `test_check_session_mode_consistency.py`; cover agree (exit 0), disagree (exit 1), handoff resolution | focused test file |
| 4 | Add additive entry to `REVIEWER_FAST_CHECKS` and to the steward session-sync lane | wiring diff |
| 5 | Run tests, reviewer-fast, diff hygiene | gate evidence |
| 6 | Author completion review with Agent Operation Trace Block | completion review |
| 7 | Commit material batch | single governed material commit |
| 8 | Run pre-closure autorun gate over committed range | closure gate evidence |
| 9 | Run session-sync steward; update session files; commit session-sync batch | session-sync commit |

## 8. Write Ownership

Codex may write only the allowed files in Section 5. Session-file updates must
be a separate session-sync commit after material closure.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one new read-only session mode-consistency
checker, focused tests, and additive wiring into reviewer-fast and the steward
session-sync lane. This scope does not authorize session-file mutation in the
material commit, behavior change in existing checkers, runtime behavior,
external repository work, public-sync, or production readiness claims.

Protected paths:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/lastUpdated.json`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `governance/compat/check_session_mode_consistency.py`
- `governance/compat/test_check_session_mode_consistency.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_agent_commit_steward_preflight.py`
- `docs/baselines/CVF_GC018_SESSION_MODE_CONSISTENCY_CHECKER_2026-06-16.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_MODE_CONSISTENCY_CHECKER_FOR_CODEX_2026-06-16.md`
- `docs/reviews/CVF_SESSION_MODE_CONSISTENCY_CHECKER_COMPLETION_2026-06-16.md`

Operator authorization: operator approved the session continuity authoring and
mode-consistency foundation roadmap and instructed Codex to take the T1 next
move.

Rollback boundary: revert only this mode-consistency checker batch if the
checker, wiring, tests, or completion review are incorrect. Do not revert
roadmap commit `2a65298b`, mode drift fix `7df9679d`, session-sync pack builder
material commit `a5e91d4b`, or any prior closed tranche.

## 9. Review Gate

Closure requires focused tests pass, the new checker passing on the current
clean tree, reviewer-fast PASS, pre-commit PASS, committed-range pre-closure
PASS after material commit, and a completion review with `Manifest delta: MATCH`.

## Evidence Requirements

| Evidence | Command |
|---|---|
| Focused tests | `python -m unittest governance.compat.test_check_session_mode_consistency -v` |
| Checker on clean tree | `python governance/compat/check_session_mode_consistency.py --enforce` (exit 0) |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` |
| Diff hygiene | `git diff --check` |
| Pre-closure autorun | `python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 2a65298b --head HEAD` |

## 11. Acceptance Criteria

| Criterion | Status |
|---|---|
| Checker fails when mode marker disagrees across surfaces | OPEN |
| Checker passes when surfaces agree | OPEN |
| Handoff path resolved from `activeHandoff`, not hardcoded | OPEN |
| Wired into reviewer-fast | OPEN |
| Wired into steward session-sync lane | OPEN |
| No file writes or git stage as side effect | OPEN |
| Focused tests pass | OPEN |
| Completion review with Agent Operation Trace Block present | OPEN |
| `Manifest delta: MATCH` in completion review | OPEN |

## 6E.1 Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | OPEN |
| Completion or reviewer artifact | `docs/reviews/CVF_SESSION_MODE_CONSISTENCY_CHECKER_COMPLETION_2026-06-16.md` | file exists with trace block and `Manifest delta: MATCH` | OPEN |
| Roadmap state | `docs/roadmaps/CVF_SESSION_CONTINUITY_AUTHORING_AND_MODE_CONSISTENCY_FOUNDATION_ROADMAP_2026-06-16.md` | T1 delivered; T2 remains held; no stale dispatch residue | OPEN |
| Registry JSON | BLOCKED with reason | no GC-051 source/test/runtime registry surface authorized in this tranche | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no corpus registry Markdown owner authorized | BLOCKED with reason |
| External evidence digest | N/A with reason | no external source, provider, OCR, or live-proof artifact | N/A with reason |
| Session continuity | N/A with reason | session sync is a dedicated follow-up batch; material commit lands first | N/A with reason |
| System loop interlock | N/A with reason | no interlock registry mutation authorized | N/A with reason |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |

## Closure Checklist

| Item | Status |
|---|---|
| Acceptance criteria satisfied | OPEN |
| Focused tests run | OPEN |
| Agent Operation Trace Block present | OPEN |
| Changed-file scope matches authorized list | OPEN |
| Core Guard Self-Protection Authorization included | PASS |
| No session-file mutation in material commit | OPEN |
| No public-sync authorized | PASS |

## Return-To-Orchestrator Conditions

Return to operator only if a required gate fails outside Allowed scope, the
wiring requires a behavior change to an existing checker, or the checker cannot
read a canonical marker surface without modifying it.

## Operator Checkpoint

No operator checkpoint remains inside T1. T2 authoring helper, additional marker
surfaces, and public-sync remain separate operator decisions.

## Dispatch Prompt Envelope

```text
Role: Codex implementer + reviewer + closer
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_MODE_CONSISTENCY_CHECKER_FOR_CODEX_2026-06-16.md
Commit mode: WORKER_MAY_COMMIT
executionBaseHead: 2a65298b
Current-time notes:
  - NEW checker tranche plus additive wiring only. Do NOT mutate CVF_SESSION/**
    in the material commit.
  - check_active_session_state.py and generate_active_session_state.py are
    read-only; the new checker adds the cross-surface marker check, it does not
    change their behavior.
  - Wiring is additive only: one new entry in REVIEWER_FAST_CHECKS (hook chain)
    and one new command in the session-sync lane of _mode_commands (steward).
  - Session-sync (front door, handoff, ACTIVE_SESSION_STATE.json, state entries)
    is a SEPARATE follow-up commit after material closure.
Do-not-misread notes:
  - check_session_mode_consistency.py is READ-ONLY. It must not write, stage, or
    commit any file as a side effect.
  - Resolve the active handoff path from ACTIVE_SESSION_STATE.json activeHandoff,
    do not hardcode AGENT_HANDOFF_V19.
  - There are 4 marker occurrences to compare: front door lines 9 and 45,
    handoff lines 27 and 31, plus core currentMode. Verify line positions at
    execution time since the files may shift.
Required first actions:
  1. git rev-parse --short HEAD  ->  must equal 2a65298b
  2. python governance/compat/check_active_session_state.py --enforce  ->  PASS
  3. Read CVF_SESSION_MEMORY.md lines 1-60, AGENT_HANDOFF_V19 lines 25-35,
     ACTIVE_SESSION_STATE_CORE.json currentMode
  4. Read run_local_governance_hook_chain.py lines 24-70 and
     run_agent_commit_steward_preflight.py lines 181-245
Return contract: COMPLETE_PENDING_REVIEW
  Evidence required: focused test run, checker exit-0 on clean tree, reviewer-fast
  PASS, session-sync steward PASS, diff hygiene PASS, completion review with
  Agent Operation Trace Block and Manifest delta: MATCH.
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 mode-consistency checker work order authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch, governance gates |
| Target paths | GC-018, this work order |
| Allowed scope source | operator approved roadmap and T1 next move |
| Before status evidence | roadmap `2a65298b`; mode drift fixed `7df9679d`; HEAD `2a65298b` |
| After status evidence | Codex T1 dispatch packet complete; ready for implementation |
| Diff evidence | dispatch packet authoring range from `2a65298b` |
| Approval boundary | dispatch packet authoring only; no source mutation |
| Claim boundary | no runtime/provider/public/production claim |
| Agent type | Codex orchestrator |
| Invocation ID | `work-order-session-mode-consistency-checker-2026-06-16` |
| Expected manifest | `docs/baselines/CVF_GC018_SESSION_MODE_CONSISTENCY_CHECKER_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_MODE_CONSISTENCY_CHECKER_FOR_CODEX_2026-06-16.md`; `AGENT_HANDOFF_V19_2026-06-15.md` |
| Actual changed set | `docs/baselines/CVF_GC018_SESSION_MODE_CONSISTENCY_CHECKER_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_MODE_CONSISTENCY_CHECKER_FOR_CODEX_2026-06-16.md`; `AGENT_HANDOFF_V19_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order authorizes one bounded read-only checker tranche plus additive
wiring. It does not authorize session-file mutation, behavior change in existing
checkers, runtime behavior, external repository work, public-sync, co-work
product development, production readiness, or public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control tooling. Public-sync is not
authorized.

rawMemoryReleased: false
