# CVF Agent Work Order - Session-Sync Authoring Helper For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-16

Owner / Orchestrator: Codex

Implementer: Codex

Reviewer / closer: Codex, with machine gates

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: f424d8b4

executionBaseHead: f424d8b4

closureBaseHead: f424d8b4

riskCeiling: R0_GOVERNANCE_TOOLING_ONLY

rawMemoryReleased: false

completionReviewPath:
`docs/reviews/CVF_SESSION_SYNC_AUTHORING_HELPER_COMPLETION_2026-06-16.md`

## Purpose

Implement T2 of the session continuity foundation: a read-only authoring mode in
`build_session_sync_pack.py` that emits paste-ready session-sync content (a
skeleton state entry with the next `stateOrder`, a `nextAllowedMove` update
template, and the three-surface mode marker block) to cut the manual
session-sync authoring overhead that is 49 percent of recent commits.

## 1. Mission

Add an additive `--author-entry` read-only mode to
`governance/compat/build_session_sync_pack.py` that prints a skeleton state
entry, a `nextAllowedMove` update template, and the three-surface mode marker
block, plus focused tests. The mode must not write, stage, or commit, and must
not change the existing `--suggest`/`--enforce`/`--plan-only` behavior.

## 2. Authority Chain

- Operator instruction: 2026-06-16, approved the session continuity foundation
  roadmap and the T2 next move after T1 closure.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.
- Roadmap:
  `docs/roadmaps/CVF_SESSION_CONTINUITY_AUTHORING_AND_MODE_CONSISTENCY_FOUNDATION_ROADMAP_2026-06-16.md`.
- GC-018:
  `docs/baselines/CVF_GC018_SESSION_SYNC_AUTHORING_HELPER_2026-06-16.md`.

Authority boundary: T2 read-only authoring helper plus additive tests only. All
parked lanes remain held.

## 3. Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator | Codex | scope, dispatch, boundary guard |
| Implementer | Codex | additive helper mode, tests, completion review |
| Reviewer / closer | Codex plus machine gates | inspect diff, run gates, commit |
| Operator | Human | scope expansion, public-sync |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | Operator approved roadmap and T2 next move; Codex owns implementation and closure |
| Scope classification | Bounded R0 governance tooling: additive read-only helper mode plus tests |
| Risk sensitivity | No public sync, no provider call, no live proof, no secret use, no session mutation, no behavior change to existing modes, no production claim |
| Selected role route | `SINGLE_AGENT_MULTI_ROLE` |
| Role separation basis | Codex executes implementation and reviewer duties with machine gates and distinct material/session commits |
| Escalation condition | Stop for session-file mutation, behavior change to existing modes, scope expansion, network, credentials, or public-sync |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Role separation ledger | Codex records implementation, focused tests, material commit, pre-closure, and session-sync as distinct steps |
| Evidence basis independent of memory | Helper output, test run, reviewer-fast, diff hygiene, pre-closure gate, and git status are required evidence |
| Self-review boundary | Self-review bounded by machine gates and explicit completion review evidence; no independent external review claimed |
| Escalation conditions | Stop for session-file mutation, behavior change to existing modes, credentials, network, public-sync, or risk expansion |
| Gate sequence | pre-dispatch before dispatch commit; focused tests and reviewer-fast before material commit; pre-closure on material range; session-sync steward before continuity commit |

## 4. Required First Reads

| File | Required use |
|---|---|
| `CVF_SESSION_MEMORY.md` | front-door marker surfaces |
| `AGENT_HANDOFF_V19_2026-06-15.md` | handoff marker surfaces |
| `governance/compat/build_session_sync_pack.py` | argparse mode group at lines 207-261; existing read-only structure |
| `governance/compat/generate_active_session_state.py` | `source_entry` line 32; `entry_filename` line 21 |
| `governance/compat/check_session_mode_consistency.py` | canonical five marker surfaces to emit in the marker block |
| `docs/baselines/CVF_GC018_SESSION_SYNC_AUTHORING_HELPER_2026-06-16.md` | GC-018 authorized scope |

## 5. Allowed Scope

Codex may modify or create:

| Path | Action |
|---|---|
| `docs/roadmaps/CVF_SESSION_CONTINUITY_AUTHORING_AND_MODE_CONSISTENCY_FOUNDATION_ROADMAP_2026-06-16.md` | closure status update only |
| `docs/baselines/CVF_GC018_SESSION_SYNC_AUTHORING_HELPER_2026-06-16.md` | source-scope and trace correction |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_SYNC_AUTHORING_HELPER_FOR_CODEX_2026-06-16.md` | closure update |
| `governance/compat/build_session_sync_pack.py` | additive read-only `--author-entry` mode only |
| `governance/compat/test_build_session_sync_pack.py` | additive tests |
| `docs/reviews/CVF_SESSION_SYNC_AUTHORING_HELPER_COMPLETION_2026-06-16.md` | create |
| `AGENT_HANDOFF_V19_2026-06-15.md` | session-sync update once material SHA exists |
| `CVF_SESSION_MEMORY.md` | session-sync update once material SHA exists |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | session-sync mode marker update |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | session-sync update |
| `CVF_SESSION/state/entries/lastUpdated.json` | session-sync update |
| `CVF_SESSION/state/entries/sessionSyncAuthoringHelperClosure20260616.json` | session-sync closure entry |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | session-sync regeneration |

## 6. Forbidden Scope And Stop Conditions

Stop before:

- writing, staging, or committing any file as a side effect of the helper;
- changing behavior of the existing `--suggest`/`--enforce`/`--plan-only` modes;
- changing behavior of `generate_active_session_state.py` or
  `check_session_mode_consistency.py`;
- any network call, credential read, or secret use;
- public-sync;
- co-work product or platform development;
- production or public readiness claims;
- session-file mutation in the material commit (session-sync is a separate
  follow-up batch; the material commit must close first).

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Helper argparse mode group | `governance/compat/build_session_sync_pack.py` | line 207 | `main` | build_session_sync_pack module | ACCEPT |
| Existing manifest printer | `governance/compat/build_session_sync_pack.py` | line 111 | `_print_manifest` | build_session_sync_pack module | ACCEPT |
| State entry schema builder | `governance/compat/generate_active_session_state.py` | line 32 | `source_entry` | generate_active_session_state module | ACCEPT |
| Entry filename builder | `governance/compat/generate_active_session_state.py` | line 21 | `entry_filename` | generate_active_session_state module | ACCEPT |
| Source-only entry fields set | `governance/compat/generate_active_session_state.py` | line 19 | `SOURCE_ONLY_ENTRY_FIELDS` | generate_active_session_state module | ACCEPT |
| Marker surfaces to emit | `governance/compat/check_session_mode_consistency.py` | line 35 | `FRONT_DOOR_MARKER_RE` | check_session_mode_consistency module | ACCEPT |

## 6A. Source-Fidelity Pass

Existing paths verified at `f424d8b4`:

- `governance/compat/build_session_sync_pack.py` -- EXISTS; argparse mode group lines 207-261.
- `governance/compat/generate_active_session_state.py` -- EXISTS; `source_entry` line 32, `entry_filename` line 21.
- `governance/compat/check_session_mode_consistency.py` -- EXISTS; marker surfaces.

Planned new path (NEW, no runtime claim):

- `docs/reviews/CVF_SESSION_SYNC_AUTHORING_HELPER_COMPLETION_2026-06-16.md` -- NEW.

## Current Runtime Freshness Verification

This work order claims no provider calls, no network use, no API key use, no
live proof, and no behavior change to existing modes or checkers. The helper is
read-only and prints generated content to stdout.

Search evidence:

- No `fetch`, `http`, `requests`, or `urllib` calls authorized or present.
- No `.env` or credential path read authorized or present.
- The existing `--suggest`/`--enforce`/`--plan-only` modes and
  `generate_active_session_state.py`/`check_session_mode_consistency.py` are
  unchanged; the helper adds a new additive mode only.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: All source verification rows recomputed from current file reads at f424d8b4. No prior verification artifact exists for this tranche.

unicodePathHandling: literal paths only; all source file reads use UTF-8-safe encoding with errors=replace; no Unicode-path corpus evidence is used.

extractedTextAuthority: SOURCE_AUTHORITY

Text encoding: all authored prose uses ASCII only.

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order section | Output artifact | Verification | Status |
|---|---|---|---|---|
| Emit skeleton state entry with next stateOrder | Section 5; mission | `--author-entry` mode | test asserting next-order skeleton | PASS |
| Emit nextAllowedMove update template | Section 5 | helper output | test asserting template present | PASS |
| Emit three-surface mode marker block | Section 5 | helper output | test asserting all five canonical occurrences | PASS |
| Reuse source_entry/entry_filename, do not duplicate | Section 6 forbidden; source verification | helper | code review in completion | PASS |
| Read-only: no write/stage | Section 6 forbidden | helper | completion claim boundary | PASS |
| Existing modes unchanged | Section 6 forbidden | helper | existing tests still pass | PASS |
| Focused tests | Section 5 | `test_build_session_sync_pack.py` | test run output | PASS |
| Completion review with trace block | Section 5 | completion review | `Manifest delta: MATCH` | PASS |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for all non-destructive
actions inside this work order's Allowed scope: reading named files, running
`git status`/`git diff`/`git rev-parse` and listed governance gates, adding the
additive helper mode and tests, running focused tests/reviewer-fast/diff
hygiene/pre-closure, committing the material batch, and running the session-sync
batch as a separate follow-up commit.

Escalation is reserved for: session-file mutation in the material commit,
behavior change to existing modes or checkers, network calls, credential use,
public-sync, scope expansion, or destructive action. Routine gate failures
inside Allowed scope are mandatory remediation, not operator-preference
checkpoints.

## Pre-Flight Checks

| Check | Command | Expected |
|---|---|---|
| Active session state | `python governance/compat/check_active_session_state.py --enforce` | PASS |
| Mode consistency | `python governance/compat/check_session_mode_consistency.py --enforce` | PASS |
| Worktree before edits | `git status --short` | clean |
| Execution base | `git rev-parse --short HEAD` | `f424d8b4` |

## 7. Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Verify HEAD = `f424d8b4`; run pre-flight checks | startup confirmation |
| 2 | Add `--author-entry` mode computing next stateOrder and emitting skeleton entry, nextAllowedMove template, and marker block | helper diff |
| 3 | Add focused tests covering all three emitted blocks, next-order computation, and read-only behavior | test diff |
| 4 | Run tests (new and existing), reviewer-fast, diff hygiene | gate evidence |
| 5 | Author completion review with Agent Operation Trace Block | completion review |
| 6 | Commit material batch | single governed material commit |
| 7 | Run pre-closure autorun gate over committed range | closure gate evidence |
| 8 | Run session-sync steward; update session files; commit session-sync batch | session-sync commit |

## 8. Write Ownership

Codex may write only the allowed files in Section 5. Session-file updates must
be a separate session-sync commit after material closure.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one additive read-only authoring mode to
`build_session_sync_pack.py` plus focused tests. This scope does not authorize
session-file mutation in the material commit, behavior change in existing modes
or checkers, runtime behavior, external repository work, public-sync, or
production readiness claims.

Protected paths:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/lastUpdated.json`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `governance/compat/build_session_sync_pack.py`
- `governance/compat/test_build_session_sync_pack.py`
- `docs/roadmaps/CVF_SESSION_CONTINUITY_AUTHORING_AND_MODE_CONSISTENCY_FOUNDATION_ROADMAP_2026-06-16.md`
- `docs/baselines/CVF_GC018_SESSION_SYNC_AUTHORING_HELPER_2026-06-16.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_SYNC_AUTHORING_HELPER_FOR_CODEX_2026-06-16.md`
- `docs/reviews/CVF_SESSION_SYNC_AUTHORING_HELPER_COMPLETION_2026-06-16.md`

Operator authorization: operator approved the session continuity foundation
roadmap and instructed Codex to take the T2 next move after T1 closure.

Rollback boundary: revert only this authoring-helper batch if the helper mode,
tests, or completion review are incorrect. Do not revert T1 material commit
`e022c872`, T1 session-sync `f424d8b4`, roadmap commit `2a65298b`, or any prior
closed tranche.

## 9. Review Gate

Closure requires focused tests pass, existing tests still pass, the helper
running read-only on the current tree, reviewer-fast PASS, pre-commit PASS,
committed-range pre-closure PASS after material commit, and a completion review
with `Manifest delta: MATCH`.

## Evidence Requirements

| Evidence | Command |
|---|---|
| Focused tests | `python -m unittest governance.compat.test_build_session_sync_pack -v` |
| Helper author mode | `python governance/compat/build_session_sync_pack.py --author-entry --state-key exampleClosure20260616` |
| Existing modes unchanged | `python governance/compat/build_session_sync_pack.py --suggest` |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` |
| Diff hygiene | `git diff --check` |
| Pre-closure autorun | `python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base f424d8b4 --head HEAD` |

## 11. Acceptance Criteria

| Criterion | Status |
|---|---|
| Helper emits skeleton entry with next stateOrder | PASS |
| Helper emits nextAllowedMove update template | PASS |
| Helper emits three-surface mode marker block | PASS |
| Reuses source_entry/entry_filename, no duplication | PASS |
| Read-only: no write/stage as side effect | PASS |
| Existing modes unchanged; existing tests pass | PASS |
| Focused tests pass | PASS |
| Completion review with Agent Operation Trace Block present | PASS |
| `Manifest delta: MATCH` in completion review | PASS |

## 6E.1 Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SESSION_SYNC_AUTHORING_HELPER_COMPLETION_2026-06-16.md` | file exists with trace block and `Manifest delta: MATCH` | PASS |
| Roadmap state | `docs/roadmaps/CVF_SESSION_CONTINUITY_AUTHORING_AND_MODE_CONSISTENCY_FOUNDATION_ROADMAP_2026-06-16.md` | T2 delivered; roadmap fully delivered; no stale dispatch residue | PASS |
| Registry JSON | BLOCKED with reason | no GC-051 source/test/runtime registry surface authorized in this tranche | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no corpus registry Markdown owner authorized | BLOCKED with reason |
| External evidence digest | N/A with reason | no external source, provider, OCR, or live-proof artifact | N/A with reason |
| System loop interlock | N/A with reason | no interlock registry mutation authorized | N/A with reason |
| Session continuity | N/A with reason | session sync is a dedicated follow-up batch; material commit lands first | N/A with reason |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |

## Closure Checklist

| Item | Status |
|---|---|
| Acceptance criteria satisfied | PASS |
| Focused tests run | PASS |
| Agent Operation Trace Block present | PASS |
| Changed-file scope matches authorized list | PASS |
| Core Guard Self-Protection Authorization included | PASS |
| No session-file mutation in material commit | PASS |
| No public-sync authorized | PASS |

## Return-To-Orchestrator Conditions

Return to operator only if a required gate fails outside Allowed scope, the
additive mode requires a behavior change to an existing mode or checker, or the
skeleton entry cannot reuse `source_entry`/`entry_filename` without modifying
`generate_active_session_state.py`.

## Operator Checkpoint

No operator checkpoint remains inside T2. With T2 closed the session continuity
foundation roadmap is fully delivered; further session-sync automation remains a
separate operator decision.

## Dispatch Prompt Envelope

```text
Role: Codex implementer + reviewer + closer
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_SYNC_AUTHORING_HELPER_FOR_CODEX_2026-06-16.md
Commit mode: WORKER_MAY_COMMIT
executionBaseHead: f424d8b4
Current-time notes:
  - Additive read-only mode only. Do NOT mutate CVF_SESSION/** in the material
    commit, and do NOT change the existing --suggest/--enforce/--plan-only
    behavior.
  - Reuse source_entry and entry_filename from generate_active_session_state.py
    for the skeleton entry; do not duplicate the schema.
  - Compute next stateOrder as max existing entry order + 1.
  - The three-surface marker block must list all five canonical occurrences the
    mode-consistency checker enforces (front door x2, handoff x2, core).
  - Session-sync is a SEPARATE follow-up commit after material closure.
Do-not-misread notes:
  - The helper is READ-ONLY. It prints to stdout; it must not write, stage, or
    commit any file.
  - --author-entry needs a --state-key input; the helper must not invent closure
    prose, only the skeleton structure.
Required first actions:
  1. git rev-parse --short HEAD  ->  must equal f424d8b4
  2. python governance/compat/check_active_session_state.py --enforce  ->  PASS
  3. python governance/compat/check_session_mode_consistency.py --enforce -> PASS
  4. Read build_session_sync_pack.py lines 138-215 and
     generate_active_session_state.py lines 19-48
Return contract: COMPLETE_PENDING_REVIEW
  Evidence required: focused test run (new and existing), --author-entry sample,
  --suggest unchanged sample, reviewer-fast PASS, diff hygiene PASS, completion
  review with Agent Operation Trace Block and Manifest delta: MATCH.
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 session-sync authoring helper work order authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch, governance gates |
| Target paths | GC-018, this work order |
| Allowed scope source | operator approved roadmap and T2 next move |
| Before status evidence | T1 closed `e022c872`; mode consistent `f424d8b4` |
| After status evidence | Codex T2 implementation complete with read-only helper and focused tests |
| Diff evidence | T2 closure range from `f424d8b4` |
| Approval boundary | T2 read-only helper implementation, closure review, and roadmap closure only |
| Claim boundary | no runtime/provider/public/production claim |
| Agent type | Codex orchestrator |
| Invocation ID | `work-order-session-sync-authoring-helper-2026-06-16` |
| Expected manifest | `docs/roadmaps/CVF_SESSION_CONTINUITY_AUTHORING_AND_MODE_CONSISTENCY_FOUNDATION_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_SESSION_SYNC_AUTHORING_HELPER_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_SYNC_AUTHORING_HELPER_FOR_CODEX_2026-06-16.md`; `governance/compat/build_session_sync_pack.py`; `governance/compat/test_build_session_sync_pack.py`; `docs/reviews/CVF_SESSION_SYNC_AUTHORING_HELPER_COMPLETION_2026-06-16.md` |
| Actual changed set | `docs/roadmaps/CVF_SESSION_CONTINUITY_AUTHORING_AND_MODE_CONSISTENCY_FOUNDATION_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_SESSION_SYNC_AUTHORING_HELPER_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_SYNC_AUTHORING_HELPER_FOR_CODEX_2026-06-16.md`; `governance/compat/build_session_sync_pack.py`; `governance/compat/test_build_session_sync_pack.py`; `docs/reviews/CVF_SESSION_SYNC_AUTHORING_HELPER_COMPLETION_2026-06-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order authorizes one bounded read-only authoring-helper tranche plus
additive tests. It does not authorize session-file mutation, behavior change in
existing modes or checkers, runtime behavior, external repository work,
public-sync, co-work product development, production readiness, or public
readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control tooling. Public-sync is not
authorized.

rawMemoryReleased: false
