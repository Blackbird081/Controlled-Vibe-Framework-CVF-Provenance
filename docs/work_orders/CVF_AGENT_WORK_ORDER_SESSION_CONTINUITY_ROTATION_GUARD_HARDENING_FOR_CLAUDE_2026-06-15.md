# CVF Agent Work Order - Session Continuity Rotation Guard Hardening For Claude - 2026-06-15

Memory class: AGENT_WORK_ORDER_PACKET

Status: DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT

Assigned agent: Claude
Reviewer/committer: Codex
dispatchBaseHead: c7d3d955
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
closureBaseHead: CODEX_REVIEWER_SETS_AFTER_WORKER_RETURN
Roadmap: `docs/roadmaps/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_ROADMAP_2026-06-15.md`
GC-018: `docs/baselines/CVF_GC018_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_2026-06-15.md`

## Objective

Harden the active-session guard so future handoff rotations cannot leave stale
root `AGENT_HANDOFF*.md` files behind. Any root handoff file other than the
active handoff named by `CVF_SESSION/ACTIVE_SESSION_STATE.json` must be reported
as a guard violation, regardless of whether its status is ARCHIVED,
SUPERSEDED, or any other non-active wording.

## Purpose

Move a repeated reviewer cleanup risk into a reusable active-session machine
guard so all future agents follow the same handoff-rotation control.

## Authority Chain

| Authority | Path |
|---|---|
| Operator request | Current session request: audit worker return, write next roadmap, and create Claude work order |
| Roadmap | `docs/roadmaps/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_ROADMAP_2026-06-15.md` |
| GC-018 | `docs/baselines/CVF_GC018_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_2026-06-15.md` |
| Canonical guard | `governance/compat/check_active_session_state.py` |
| Test owner | `governance/compat/test_check_active_session_state.py` |

## Agent Roles

| Role | Agent | Boundary |
|---|---|---|
| Orchestrator | Codex | Authored roadmap, GC-018, and this work order |
| Worker | Claude | Implements allowed-scope guard/test changes and worker return |
| Reviewer/committer | Codex | Reviews worker return, runs closure gates, commits if passing |

## Commit Mode

Commit mode: WORKER_MUST_NOT_COMMIT

Claude may edit only the allowed files below and must return
`COMPLETE_PENDING_REVIEW` with evidence. Codex reviews and commits.

## Required First Reads

Claude must read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `docs/roadmaps/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_ROADMAP_2026-06-15.md`
- `docs/baselines/CVF_GC018_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_2026-06-15.md`
- `governance/compat/check_active_session_state.py`
- `governance/compat/test_check_active_session_state.py`

## Pre-Flight Checks

- Confirm `git rev-parse --short HEAD` and record it as `executionBaseHead`.
- Confirm no unexpected modified files outside the allowed scope block.
- Confirm the source verification items still exist before editing.
- Allowed-scope machine failures remain worker-owned and must be resolved before return.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | Operator requested audit, next foundation roadmap, and Claude implementation work order |
| Scope classification | Bounded governance-control guard and focused test hardening |
| Risk sensitivity | Low runtime risk; no provider, live, secret, public-sync, or production surface |
| Selected route mode | MULTI_AGENT_MULTI_ROLE |
| Selected role route | Codex orchestrator; Claude worker; Codex reviewer/committer |
| Role separation basis | Worker must not commit; independent reviewer owns closure |
| Escalation condition | Stop and return BLOCKED if work requires session state, runtime, provider, live proof, public-sync, legacy reads, credentials, or destructive action |

## Write Ownership

Claude owns only the implementation files and worker return named in Allowed
Scope. Codex owns completion review and commit packaging.

## Allowed Scope

Implementation:

1. `governance/compat/check_active_session_state.py`
2. `governance/compat/test_check_active_session_state.py`

Worker return:

3. `docs/reviews/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_WORKER_RETURN_2026-06-15.md`

No other path is authorized.

## Forbidden Scope

- Runtime source outside `governance/compat/`.
- Model Gateway code or tests.
- `CVF_SESSION/**`, `AGENT_HANDOFF*.md`, or `CVF_SESSION_MEMORY.md`.
- Provider/API/live proof.
- Public-sync.
- `.private_reference/legacy/**`.
- Broad refactors of active-session state logic.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this work order is not legacy-adjacent despite
being foundation control-plane work. It hardens an existing current-source
machine guard and must not read `.private_reference/legacy/**`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Root handoff discovery | `governance/compat/check_active_session_state.py` | lines 272-273 | `_root_handoff_paths` | Active session state guard | ACCEPT |
| Handoff status parser | `governance/compat/check_active_session_state.py` | lines 290-296 | `_handoff_status` | Active session state guard | ACCEPT |
| Active root handoff detector | `governance/compat/check_active_session_state.py` | lines 299-305 | `_active_handoffs` | Active session state guard | ACCEPT |
| Exact-one-ACTIVE enforcement | `governance/compat/check_active_session_state.py` | lines 507-512 | `active_handoffs` | `_classify` | ACCEPT |
| Registry mismatch enforcement | `governance/compat/check_active_session_state.py` | lines 513-516 | `active_handoff` | `_classify` | ACCEPT |
| Current stale-root enforcement is status-limited to ARCHIVED | `governance/compat/check_active_session_state.py` | lines 517-526 | `handoff_violations` | `_classify` | ACCEPT |
| Existing archived-root test coverage | `governance/compat/test_check_active_session_state.py` | lines 238-250 | `test_unregistered_archived_root_handoff_fails` | Active session state tests | ACCEPT |

## Implementation Instructions

1. Update `check_active_session_state.py` so every root `AGENT_HANDOFF*.md`
   whose relative path is not `active_handoff` produces a handoff violation.
2. Keep the existing `expected exactly one root AGENT_HANDOFF*.md with
   Status: ACTIVE` check.
3. Keep the existing `active handoff registry mismatch` check.
4. Replace or generalize the current ARCHIVED-only root stale message. The new
   message must tell the operator that a non-active root handoff remains at the
   repository root and must be archived or removed.
5. Preserve archive-qualified references under `CVF_SESSION/handoffs/archive/`;
   this work order is about root files only.
6. Add tests for:
   - root SUPERSEDED handoff fails;
   - root non-active handoff with unexpected status wording fails;
   - the existing archived-root test remains meaningful.
7. Do not modify session state, active handoff, root handoff files, or
   `CVF_SESSION_MEMORY.md`.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Capture execution base and status | `git rev-parse --short HEAD`; `git status --short` |
| 2 | Implement root stale handoff guard generalization | diff in `check_active_session_state.py` |
| 3 | Add focused tests | diff in `test_check_active_session_state.py` |
| 4 | Run focused pytest | command output |
| 5 | Run fast return gate | command output |
| 6 | Author worker return | review artifact |

## Required Tests And Gates

Run:

```bash
python -m pytest governance/compat/test_check_active_session_state.py
```

Then run one fast return gate:

```bash
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_active_session_state.py
```

If the second command is not compatible with this repo's current pytest target
format, run `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`
and record the incompatibility reason in the worker return.

## Evidence Requirements

The worker return must include:

- changed file set;
- focused test output;
- fast gate output;
- no-commit evidence;
- actual changed set;
- Agent Operation Trace Block with all required labels;
- explicit N/A reason for live proof, public-sync, and legacy absorption.

## Review Gate

Codex must not commit until the worker return exists, focused tests pass, and
reviewer gates are rerun on the actual changed set.

## Closure Checklist

- [ ] Source verification rechecked
- [ ] Guard implementation complete
- [ ] SUPERSEDED root handoff test added
- [ ] Unexpected non-active root handoff test added
- [ ] Existing archived-root test still passes
- [ ] Focused pytest passes
- [ ] Fast return gate or reviewer-fast passes
- [ ] Worker return authored
- [ ] Worker did not commit

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all checklist items are satisfied.
Return `BLOCKED` only if a required action exceeds declared write ownership.

## Operator Checkpoint

No human authorization pause applies to the declared three-file worker set.
Additional authorization is required only if runtime, provider, public-sync,
legacy, credential, destructive action, or session-state mutation becomes
necessary.

## Worker Autonomy / No-Question Rule

Machine-gate failures inside declared paths are worker-owned and must pass
before return. Escalate only when the required action would change
scope, risk, credentials, public-sync, live proof, or session state.

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_COMPLETION_2026-06-15.md`
- `AGENT_HANDOFF_V19_2026-06-15.md` only if post-commit session synchronization is required
- `CVF_SESSION_MEMORY.md` only if post-commit next-move synchronization is required
- generated active state source/aggregate only if post-commit synchronization is required

Codex runs pre-closure gates on the real worker range, inspects the actual diff,
authors the completion review, and commits. Claude does not author the
completion review.

## Worker Return Requirements

Create:

`docs/reviews/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_WORKER_RETURN_2026-06-15.md`

Required sections:

- Purpose
- Scope And Methodology
- Changed File Set
- Source Verification Result
- Implementation Summary
- Acceptance Criteria Evidence
- Gate Results
- Public Export Disposition (`DEFERRED_PRIVATE_ONLY`)
- Legacy Absorption Coverage Index Disposition (`NOT_APPLICABLE_WITH_REASON`)
- Finding-To-Governance Learning Disposition
- Negative Search And Collision Discipline
- Agent Operation Trace Block
- Claim Boundary
- No-Commit Evidence

## Roadmap-To-Work-Order Trace Matrix

| Roadmap deliverable | Work order instruction | Status |
|---|---|---|
| D3 Guard implementation | Implementation Instructions 1-5 | DISPATCHED |
| D4 Focused unit tests | Implementation Instructions 6 | DISPATCHED |
| D5 Worker return | Worker Return Requirements | DISPATCHED |
| D6 Completion review and commit | Codex reviewer | REQUIRED_AFTER_WORKER_RETURN |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC-1 | Root SUPERSEDED handoff fails | Focused test name and output |
| AC-2 | Root non-active unexpected status handoff fails | Focused test name and output |
| AC-3 | Existing archived-root stale handoff coverage remains | Focused test output |
| AC-4 | Active-session guard tests pass | Command output |
| AC-5 | Fast return gate or reviewer-fast passes | Command output |
| AC-6 | No unauthorized files changed | `git diff --name-status` and `git status --short` |

## Worker Expected Manifest

Claude's implementation return is expected to change only:

- `governance/compat/check_active_session_state.py`
- `governance/compat/test_check_active_session_state.py`
- `docs/reviews/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_WORKER_RETURN_2026-06-15.md`

## Agent Operation Trace Block

| Label | Value |
|---|---|
| Actor | Codex orchestrator dispatching Claude worker |
| Provider or surface | Codex local filesystem |
| Session or invocation | 2026-06-15 guard-hardening dispatch |
| Working directory | d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF |
| Command or tool surface | apply_patch, PowerShell, local governance gates |
| Target paths | `governance/compat/check_active_session_state.py`; `governance/compat/test_check_active_session_state.py`; worker return path |
| Allowed scope source | GC-018 and this work order |
| Before status evidence | Reviewer finding from session front-door compaction closure |
| After status evidence | Dispatch packet authored; worker implementation not yet returned |
| Diff evidence | Current dispatch batch changed set in this trace block |
| Approval boundary | Operator requested next roadmap and Claude work order; no live/public/legacy authorization |
| Claim boundary | Stale root handoff guard/test hardening only |
| Agent type | Codex orchestrator; Claude worker assigned |
| Invocation ID | 2026-06-15 dispatch packet |
| Expected manifest | `AGENT_HANDOFF_V19_2026-06-15.md`; `AGENTS.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`; `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/lastUpdated.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION_MEMORY.md`; `docs/baselines/CVF_GC018_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_2026-06-15.md`; `docs/baselines/CVF_GC018_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_2026-06-15.md`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/session-front-door-v19.json`; `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_COMPLETION_2026-06-15.md`; `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_WORKER_RETURN_2026-06-15.md`; `docs/roadmaps/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_ROADMAP_2026-06-15.md`; `docs/roadmaps/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_ROADMAP_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_FOR_CLAUDE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_FOR_CLAUDE_2026-06-15.md` |
| Actual changed set | `AGENT_HANDOFF_V19_2026-06-15.md`; `AGENTS.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`; `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/lastUpdated.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION_MEMORY.md`; `docs/baselines/CVF_GC018_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_2026-06-15.md`; `docs/baselines/CVF_GC018_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_2026-06-15.md`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/session-front-door-v19.json`; `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_COMPLETION_2026-06-15.md`; `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_WORKER_RETURN_2026-06-15.md`; `docs/roadmaps/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_ROADMAP_2026-06-15.md`; `docs/roadmaps/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_ROADMAP_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_FOR_CLAUDE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_FOR_CLAUDE_2026-06-15.md` |
| Manifest delta | MATCH; root V18 deletion recorded by deletion disposition in the completion review |
| Deletion or rename disposition | No delete or rename authorized |

## Claim Boundary

This work order authorizes only guard hardening for stale root handoff detection.
It does not authorize session rotation, state mutation, Model Gateway work,
provider wiring, legacy absorption, public-sync, or live proof.
