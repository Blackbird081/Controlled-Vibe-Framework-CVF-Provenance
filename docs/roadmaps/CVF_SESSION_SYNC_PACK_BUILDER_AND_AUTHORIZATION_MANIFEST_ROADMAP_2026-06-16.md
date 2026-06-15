# CVF Session-Sync Pack Builder And Authorization Manifest Roadmap

Memory class: FULL_RECORD

rawMemoryReleased: false

Date: 2026-06-16

Status: ROADMAP_READY_FOR_GC018

Owner: Codex orchestrator

Worker target: Claude

## Purpose

Every material commit in CVF currently requires an agent to manually assemble
the correct session-sync packet: updating `CVF_SESSION_MEMORY.md`, regenerating
`ACTIVE_SESSION_STATE.json`, verifying state entries, confirming the active
handoff has the right HEAD/material-parent marker, and ensuring that any
protected-path mutation has a matching Core Guard Self-Protection Authorization.

The commit-steward preflight hardening (closed at `d709071c`) moved the
authorization check earlier in the flow. This roadmap takes the next step:
give every agent a machine-generated manifest of exactly which protected paths
must be authorized before the session-sync commit begins, and a drift check
that catches stale state between `ACTIVE_SESSION_STATE.json` and the
`CVF_SESSION/state/**` entry files before the agent edits anything.

## Audit Position

The repeating failure pattern: agents complete a material tranche, then
session-sync silently drifts because the protected-path manifest existed only
in the active handoff and had to be hand-read and hand-matched. The
closure-packaging preflight (`check_closure_packaging_preflight.py`) already
catches missing authorization post-hoc. This tool generates the authorization
manifest pre-emptively, so the agent has the exact block to paste before
writing the session-sync commit.

Commit steward preflight is the hook. Session-sync pack builder is the
pre-hook helper that ensures the agent never reaches the hook with an
incomplete or stale packet.

## Authorization / Decision

Decision: proceed to GC-018 and Claude work order for T1. Operator approved
this roadmap after commit-steward preflight hardening closure.

## Scope

T1 covers authoring-time tooling only:

- A Python helper script (`governance/compat/build_session_sync_pack.py`) that:
  - reads the changed-path plan from `run_agent_commit_steward_preflight.py`
    build_path_plan logic (import, not duplicate);
  - reads `CVF_SESSION/ACTIVE_SESSION_STATE.json` and all `CVF_SESSION/state/**`
    entry files;
  - emits the exact protected-path authorization manifest block an agent must
    include in the active handoff before a session-sync commit;
  - reports drift between the aggregate `ACTIVE_SESSION_STATE.json` and the
    individual entry files under `CVF_SESSION/state/entries/`;
  - accepts `--suggest` (print manifest block only, no exit code change) and
    `--enforce` (non-zero exit if drift or missing authorization detected);
  - never auto-claims closure, never bypasses a hook, never writes session files.
- A `--plan-only` path that outputs the manifest without running gates, usable
  inside dispatch prompt envelopes as a pre-read step.
- Focused unit tests under `governance/compat/tests/test_build_session_sync_pack.py`.
- A completion review with Agent Operation Trace Block.

The script must import `build_path_plan` from `run_agent_commit_steward_preflight`
rather than duplicating the protected-path classification logic.

## Non-Goals

- Auto-writing session files or handoff mutations;
- bypassing or replacing `check_closure_packaging_preflight.py` or
  `check_active_session_state.py`;
- live provider, runtime, or public-sync changes;
- wiring into the pre-commit hook (the commit steward calls this as a helper,
  the hook calls the commit steward - no new hook dependency);
- co-work product development;
- production or public readiness claims.

## Design Boundary

The pack builder is a read-only diagnostic and manifest generator. It may read
repo files and git status output; it must not write any governed file. All
writes remain the agent's responsibility after reviewing the manifest.

The drift check compares `CVF_SESSION/ACTIVE_SESSION_STATE.json` top-level keys
against the union of entry files in `CVF_SESSION/state/entries/`. A key present
in the aggregate but absent from any entry file, or vice versa for governed
entry keys, is reported as drift. The check does not re-implement the full
generate_active_session_state logic - it reads the existing outputs and flags
inconsistency.

## Design Control Gate

The script must not write, commit, or stage any file. `--enforce` mode may exit
non-zero to block an agent workflow; it must not take any mutating side effect.

## Recommended Tranche

T1: Session-Sync Pack Builder And Authorization Manifest Foundation.

Claude should:

- author `governance/compat/build_session_sync_pack.py` with `--suggest`,
  `--enforce`, and `--plan-only` modes;
- implement `build_protected_path_manifest()` (imports `build_path_plan` from
  commit steward preflight), `check_state_drift()`, and a `main()` CLI;
- add focused tests;
- author a completion review.

## Work Plan

| Step | Work | Owner |
|---|---|---|
| 1 | Author `build_session_sync_pack.py` with all three modes | Claude |
| 2 | Add `test_build_session_sync_pack.py` with focused tests | Claude |
| 3 | Author completion review with Agent Operation Trace Block | Claude |
| 4 | Review and commit if accepted | Codex |

## Value Rationale

This improves CVF core for all agents (Claude, Codex, future workers), not a
single use case. The manifest generation removes the most common manual step
in every material tranche: "which protected paths need authorization, and do
they match what the handoff already authorizes?" The drift check surfaces the
second most common defect: `ACTIVE_SESSION_STATE.json` carrying stale keys
that no longer match the `state/entries/` source files.

These two catches together reduce the latency between tranche closure and a
clean session-sync commit, regardless of which agent or model is executing.

## Scope Guard

Allowed:

- `governance/compat/build_session_sync_pack.py` (new file, read-only tool);
- `governance/compat/tests/test_build_session_sync_pack.py` (new test file);
- completion review document;
- no mutation of existing governance scripts or session files.

Forbidden:

- auto-writing session files, handoff mutations, or staged changes;
- modifying `run_agent_commit_steward_preflight.py` scope beyond importing
  `build_path_plan` (if import requires minimal refactor, scope is limited to
  exposing that one function - no behavior change);
- live API calls;
- co-work product or platform development;
- public-sync;
- production or public readiness claims.

## Acceptance Criteria

The tranche is complete when:

1. `python governance/compat/build_session_sync_pack.py --suggest` prints a
   protected-path manifest block for the current working-tree state without
   error;
2. `--enforce` exits non-zero when drift is present and zero when clean;
3. focused tests pass;
4. completion review with Agent Operation Trace Block is present and
   `Manifest delta: MATCH`.

## Verification / Evidence

Required evidence: script output sample (`--suggest` and `--enforce` on a
clean tree), focused test run, diff hygiene, and completion review.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 next-roadmap selection after commit-steward hardening |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, governance gates |
| Target paths | roadmap only |
| Allowed scope source | operator requested session-sync pack builder roadmap after commit-steward preflight hardening |
| Before status evidence | commit-steward hardening material commit `d709071c`; active handoff `AGENT_HANDOFF_V19_2026-06-15.md` |
| After status evidence | roadmap ready for GC-018 |
| Diff evidence | roadmap authoring session 2026-06-16 |
| Approval boundary | roadmap authoring only; no source mutation |
| Claim boundary | no runtime/provider/public/production claim |
| Agent type | Codex orchestrator |
| Invocation ID | `session-sync-pack-builder-roadmap-2026-06-16` |
| Expected manifest | `docs/roadmaps/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_ROADMAP_2026-06-16.md` |
| Actual changed set | `docs/roadmaps/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_ROADMAP_2026-06-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation planning. No public-sync batch is
authorized.

## Claim Boundary

This roadmap selects a governance/control-plane tooling tranche. It does not
prove implementation, runtime behavior, provider behavior, live governance
behavior, public readiness, production readiness, or co-work product
capability.
