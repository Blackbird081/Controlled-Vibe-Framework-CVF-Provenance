# GC-018 Session-Sync Pack Builder And Authorization Manifest

Memory class: FULL_RECORD

rawMemoryReleased: false

Baseline ID: GC018-SESSION-SYNC-PACK-BUILDER-AND-AUTHORIZATION-MANIFEST-2026-06-16

Date: 2026-06-16

Status: AUTHORIZED_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST

dispatchBaseHead: 6bf59f37

## Purpose

Authorize a bounded CVF foundation tranche that delivers a read-only diagnostic
helper (`build_session_sync_pack.py`) that generates the exact protected-path
authorization manifest an agent needs before any session-sync commit, and
detects drift between `ACTIVE_SESSION_STATE.json` and the `CVF_SESSION/state/`
source files before any edits begin.

## Decision

Proceed with T1 read-only tooling foundation:

- `governance/compat/build_session_sync_pack.py` with `--suggest`, `--enforce`,
  and `--plan-only` modes;
- `governance/compat/tests/test_build_session_sync_pack.py` with focused tests;
- completion review.

## Source / Predecessor Evidence

Commit-steward preflight hardening (closed `d709071c`) moved the authorization
check earlier in the flow. The remaining manual step is generating the exact
authorization manifest block before the agent writes the session-sync commit.

Existing CVF control surfaces that this tranche builds on:

- `run_agent_commit_steward_preflight.py` already classifies changed paths into
  material vs protected via `build_path_plan()` (line 125);
- `generate_active_session_state.py` already exposes `validate_aggregate_matches_sources()`
  (line 137) to detect aggregate-vs-source drift;
- `check_closure_packaging_preflight.py` already catches missing authorization
  post-hoc; this tool generates the manifest pre-emptively.

The repeating defect pattern: agents arrive at the session-sync commit with an
incomplete authorization manifest because the protected-path list existed only
in the active handoff and had to be hand-read and hand-matched.

## Authorized Scope

Codex may create:

- `governance/compat/build_session_sync_pack.py`;
- `governance/compat/tests/test_build_session_sync_pack.py`;
- `docs/reviews/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_COMPLETION_2026-06-16.md`.

Codex may read but must not modify behavior of:

- `governance/compat/run_agent_commit_steward_preflight.py` - import
  `build_path_plan` only; if a minimal `__all__` or module-level guard is needed
  to expose the function cleanly, that minimal change is authorized;
- `governance/compat/generate_active_session_state.py` - import
  `validate_aggregate_matches_sources` only.

## Not Authorized

- Auto-writing session files, handoff mutations, or staged changes;
- modifying `check_closure_packaging_preflight.py` or
  `check_active_session_state.py` behavior;
- wiring into the pre-commit hook (the commit steward calls this as a helper;
  no new hook dependency in this tranche);
- live API calls or credential use;
- public-sync;
- co-work product development;
- source edits outside the authorized paths;
- production or public readiness claims.

## Guard Requirements

`build_session_sync_pack.py` must:

- be read-only: no file write, no git stage, no git commit side effect;
- import `build_path_plan` from `run_agent_commit_steward_preflight` rather
  than duplicating protected-path classification logic;
- `--suggest`: print the protected-path authorization manifest block; exit 0
  regardless of drift;
- `--enforce`: exit non-zero if drift detected or if any protected path in the
  plan lacks a matching authorization token;
- `--plan-only`: print manifest only; equivalent to `--suggest` without drift
  analysis overhead.

## Evidence / Verification

Codex must return:

- focused test run output (`python -m pytest governance/compat/tests/test_build_session_sync_pack.py`
  or equivalent unittest);
- `build_session_sync_pack.py --suggest` output sample on a clean tree;
- `build_session_sync_pack.py --enforce` exit-code sample on a clean tree (must
  exit 0);
- diff hygiene (`git diff --check`);
- completion review with Agent Operation Trace Block and `Manifest delta: MATCH`.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 session-sync pack builder GC-018 authorization |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch, governance gates |
| Target paths | roadmap, this GC-018, Codex work order |
| Allowed scope source | operator authorized session-sync pack builder after commit-steward hardening |
| Before status evidence | commit-steward hardening material commit `d709071c`; roadmap authored 2026-06-16 |
| After status evidence | Codex implementation packet authorized |
| Diff evidence | GC-018 and work order authoring range from `6bf59f37` |
| Approval boundary | read-only diagnostic tooling only; no session mutation |
| Claim boundary | no runtime/provider/public/production claim |
| Agent type | Codex orchestrator |
| Invocation ID | `gc018-session-sync-pack-builder-2026-06-16` |
| Expected manifest | `docs/roadmaps/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_FOR_CODEX_2026-06-16.md` |
| Actual changed set | `docs/roadmaps/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_FOR_CODEX_2026-06-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance baseline. No public-sync batch is
authorized.

## Claim Boundary

This baseline authorizes one bounded read-only tooling tranche. It does not
authorize session-file mutation, runtime behavior, provider calls, public-sync,
co-work product development, production readiness, or public readiness.
