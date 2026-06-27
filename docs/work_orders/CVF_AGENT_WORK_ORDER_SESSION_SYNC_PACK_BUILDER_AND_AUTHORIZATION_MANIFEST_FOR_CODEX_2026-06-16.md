# CVF Agent Work Order - Session-Sync Pack Builder And Authorization Manifest For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-16

Owner / Orchestrator: Codex

Implementer: Codex

Reviewer / closer: Codex, with machine gates

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: 6bf59f37

executionBaseHead: 6bf59f37

closureBaseHead: 6bf59f37

riskCeiling: R0_GOVERNANCE_TOOLING_ONLY

rawMemoryReleased: false

completionReviewPath:
`docs/reviews/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_COMPLETION_2026-06-16.md`

## Purpose

Implement a bounded read-only Python helper that generates the protected-path
authorization manifest and detects session-state drift before any session-sync
commit. This is a governance tooling tranche; no runtime, provider, or
public-sync work is authorized.

## 1. Mission

Implement a read-only Python helper (`build_session_sync_pack.py`) that:

- generates the exact protected-path authorization manifest an agent must
  include in the active handoff before any session-sync commit;
- detects drift between `ACTIVE_SESSION_STATE.json` and the
  `CVF_SESSION/state/` source files before the agent writes anything.

This removes the most common manual step in every material tranche: assembling
the correct protected-path list and verifying aggregate state has not drifted.

## 2. Authority Chain

- Operator instruction: 2026-06-16, authorized session-sync pack builder
  roadmap after commit-steward preflight hardening closure.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.
- Roadmap:
  `docs/roadmaps/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_ROADMAP_2026-06-16.md`.
- GC-018:
  `docs/baselines/CVF_GC018_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_2026-06-16.md`.

Authority boundary: read-only diagnostic tooling only. No session-file
mutation, no hook-chain wiring, no behavior change in existing checkers.

## 3. Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator | Codex | scope, dispatch, boundary guard |
| Implementer | Codex | new script, tests, completion review only |
| Reviewer / closer | Codex plus machine gates | inspect diff, run gates, commit |
| Operator | Human | any scope expansion, hook wiring, public-sync |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | Operator authorized session-sync pack builder roadmap; Codex owns implementation and closure |
| Scope classification | Bounded R0 governance tooling: new read-only Python script plus focused tests |
| Risk sensitivity | No public sync, no provider call, no live proof, no secret use, no session mutation, no hook wiring, no production claim |
| Selected role route | `SINGLE_AGENT_MULTI_ROLE` |
| Role separation basis | Codex executes implementation and reviewer duties with machine gates and distinct material/session commits |
| Escalation condition | Stop for session-file mutation, hook-chain behavior change, scope expansion, network, credentials, or public-sync |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Role separation ledger | Codex records implementation, focused tests, material commit, pre-closure, and session-sync as distinct steps |
| Evidence basis independent of memory | Script output sample, test run, reviewer-fast, diff hygiene, pre-closure gate, and git status are required evidence |
| Self-review boundary | Self-review bounded by machine gates and explicit completion review evidence; no independent external review claimed |
| Escalation conditions | Stop for session-file mutation, hook-chain wiring, behavior change to existing checkers, credentials, network, public-sync, or risk expansion |
| Gate sequence | pre-dispatch before dispatch commit; focused tests and reviewer-fast before material commit; pre-closure on material range; session-sync steward before continuity commit |

## 4. Required First Reads

| File | Required use |
|---|---|
| `CVF_SESSION_MEMORY.md` | active front door and current mode |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable state |
| `AGENT_HANDOFF_V19_2026-06-15.md` | active handoff and parked lanes |
| `governance/compat/run_agent_commit_steward_preflight.py` | `build_path_plan` source at line 125; `SESSION_PREFIXES` at line 21 |
| `governance/compat/generate_active_session_state.py` | `validate_aggregate_matches_sources` source at line 137; `ENTRIES_DIR` at line 18 |
| `docs/baselines/CVF_GC018_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_2026-06-16.md` | GC-018 authorized scope |

## 5. Allowed Scope

Codex may create:

| Path | Action |
|---|---|
| `governance/compat/build_session_sync_pack.py` | create (read-only tool) |
| `governance/compat/test_build_session_sync_pack.py` | create |
| `docs/reviews/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_COMPLETION_2026-06-16.md` | create |
| `AGENT_HANDOFF_V19_2026-06-15.md` | session-sync update once material SHA exists |
| `CVF_SESSION_MEMORY.md` | session-sync update once material SHA exists |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | session-sync update |
| `CVF_SESSION/state/entries/lastUpdated.json` | session-sync update |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | session-sync regeneration |

Codex may apply a minimal read-path change (no behavior change):

| Path | Allowed change |
|---|---|
| `governance/compat/run_agent_commit_steward_preflight.py` | add `if __name__ == "__main__"` guard or minimal `__all__` to expose `build_path_plan` for import; no logic change |
| `governance/compat/generate_active_session_state.py` | import `validate_aggregate_matches_sources` only; no modification needed if already importable |

## 6. Forbidden Scope And Stop Conditions

Stop before:

- writing, staging, or committing any file as a side effect of
  `build_session_sync_pack.py` itself;
- modifying `check_closure_packaging_preflight.py` or
  `check_active_session_state.py` behavior;
- adding new entries to `governance/compat/run_local_governance_hook_chain.py`
  or `governance/compat/run_agent_autorun_workflow_gate.py`;
- any network call, credential read, or secret use;
- public-sync;
- co-work product or platform development;
- production or public readiness claims;
- session-file mutation in the material commit (session-sync is a separate
  follow-up batch; the material commit must close first).

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| `build_path_plan` function definition | `governance/compat/run_agent_commit_steward_preflight.py` | line 123 | `build_path_plan` | `run_agent_commit_steward_preflight` module | ACCEPT |
| `SESSION_PREFIXES` protected-path classifier | `governance/compat/run_agent_commit_steward_preflight.py` | line 21 | `SESSION_PREFIXES` | `run_agent_commit_steward_preflight` module | ACCEPT |
| `HANDOFF_PREFIXES` protected-path classifier | `governance/compat/run_agent_commit_steward_preflight.py` | line 25 | `HANDOFF_PREFIXES` | `run_agent_commit_steward_preflight` module | ACCEPT |
| `_is_protected_session_path` classification function | `governance/compat/run_agent_commit_steward_preflight.py` | line 107 | `_is_protected_session_path` | `run_agent_commit_steward_preflight` module | ACCEPT |
| `validate_aggregate_matches_sources` drift detector | `governance/compat/generate_active_session_state.py` | line 135 | `validate_aggregate_matches_sources` | `generate_active_session_state` module | ACCEPT |
| `ENTRIES_DIR` points to `CVF_SESSION/state/entries` | `governance/compat/generate_active_session_state.py` | line 18 | `ENTRIES_DIR` | `generate_active_session_state` module | ACCEPT |
| `SOURCE_DIR` root for state files | `governance/compat/generate_active_session_state.py` | line 16 | `SOURCE_DIR` | `generate_active_session_state` module | ACCEPT |
| `STATE_PATH` aggregate output path | `governance/compat/check_active_session_state.py` | line 36 | `STATE_PATH` | `check_active_session_state` module | ACCEPT |
| `AUTH_MARKER` post-hoc authorization check token | `governance/compat/check_closure_packaging_preflight.py` | line 24 | `AUTH_MARKER` | `check_closure_packaging_preflight` module | ACCEPT |

## 6A. Source-Fidelity Pass

Existing paths verified:

- `governance/compat/run_agent_commit_steward_preflight.py` -- EXISTS, 337 lines.
- `governance/compat/generate_active_session_state.py` -- EXISTS.
- `governance/compat/check_active_session_state.py` -- EXISTS.
- `governance/compat/check_closure_packaging_preflight.py` -- EXISTS.
- `CVF_SESSION/state/entries/` -- EXISTS, contains multiple `.json` entry files.

Planned new paths (NEW, no runtime claim):

- `governance/compat/build_session_sync_pack.py` -- NEW.
- `governance/compat/test_build_session_sync_pack.py` -- NEW.
- `docs/reviews/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_COMPLETION_2026-06-16.md` -- NEW.

## Current Runtime Freshness Verification

This work order claims no provider calls, no network use, no API key use, no
live proof, and no runtime source edits outside the three new allowed files.

Search evidence:

- No `fetch`, `http`, `requests`, or `urllib` calls authorized or present in
  the new script (behavioral constraint; enforced by forbidden scope).
- No `.env` or credential path read authorized or present.
- Existing checker files (`check_closure_packaging_preflight.py`,
  `check_active_session_state.py`, `run_local_governance_hook_chain.py`,
  `run_agent_autorun_workflow_gate.py`) are read-only in this tranche.
- `run_agent_commit_steward_preflight.py` may receive only a minimal
  `if __name__ == "__main__"` guard or `__all__` -- verified at 337 lines,
  no behavior change authorized.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: All source verification rows recomputed from current file reads in this session. No prior verification artifact exists for this tranche.

unicodePathHandling: literal paths only; all source file reads use UTF-8-safe encoding with errors=replace; no Unicode-path corpus evidence is used.

extractedTextAuthority: SOURCE_AUTHORITY

Text encoding: all authored prose uses ASCII only. No non-ASCII characters are
introduced by this work order file. Em-dash characters in referenced source
files are pre-existing and not authored by this work order.

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order section | Output artifact | Verification | Status |
|---|---|---|---|---|
| Import `build_path_plan`, do not duplicate | Section 5 allowed scope; forbidden scope | `build_session_sync_pack.py` | code review in completion | PASS |
| `--suggest` prints manifest block | Section 7 execution plan step 2 | script output sample | `--suggest` run evidence | PASS |
| `--enforce` exits non-zero on drift | Section 7 execution plan step 2 | script exit code | `--enforce` run evidence | PASS |
| `--plan-only` prints manifest without drift | Section 7 execution plan step 2 | script output | `--plan-only` run evidence | PASS |
| Read-only: no file write, no git stage | Section 6 forbidden scope | N/A -- behavioral constraint | completion review claim boundary | PASS |
| Focused unit tests | Section 5 allowed scope | `test_build_session_sync_pack.py` | test run output | PASS |
| Completion review with Agent Operation Trace Block | Section 5 allowed scope | completion review | `Manifest delta: MATCH` | PASS |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for all non-destructive
actions inside this work order's Allowed scope.

Proceed autonomously with:

- reading files named by this work order;
- running `git status`, `git diff`, `git rev-parse`, and listed governance
  gates;
- creating the three new allowed files;
- applying a minimal `if __name__ == "__main__"` guard to the commit steward
  preflight script if needed for clean import;
- running focused tests, reviewer-fast, diff hygiene, and pre-closure gate;
- committing the material batch;
- running the session-sync batch as a separate follow-up commit.

Escalation is reserved for: session-file mutation in the material commit,
hook-chain behavior change, modification of existing checker behavior, network
calls, credential use, public-sync, scope expansion, or destructive action.

Routine gate failures inside Allowed scope are mandatory remediation, not
operator-preference checkpoints.

## Pre-Flight Checks

| Check | Command | Expected |
|---|---|---|
| Active session state | `python governance/compat/check_active_session_state.py --enforce` | PASS |
| Worktree before edits | `git status --short` | clean |
| Execution base | `git rev-parse --short HEAD` | `6bf59f37` |

## 7. Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Verify HEAD = `6bf59f37`; run `check_active_session_state.py --enforce` | startup confirmation |
| 2 | Author `build_session_sync_pack.py` with `--suggest`, `--enforce`, `--plan-only` modes; import `build_path_plan` and `validate_aggregate_matches_sources` | new script |
| 3 | Author `test_build_session_sync_pack.py`; cover `--suggest` output, `--enforce` exit-0 on clean tree, `--enforce` exit-1 on drift, `--plan-only` output | focused test file |
| 4 | Run tests; capture output | test run evidence |
| 5 | Run `build_session_sync_pack.py --suggest` and `--enforce` on clean tree | sample output evidence |
| 6 | Run reviewer-fast and diff hygiene | gate pass evidence |
| 7 | Author completion review with Agent Operation Trace Block | completion review |
| 8 | Commit material batch (new script + tests + completion review only) | single governed material commit |
| 9 | Run pre-closure autorun gate over committed range | closure gate evidence |
| 10 | Run session-sync steward; update session files; commit session-sync batch | session-sync commit |

## 8. Write Ownership

Codex may write only the allowed files listed in Section 5. The session-file
update (`CVF_SESSION_MEMORY.md`, `ACTIVE_SESSION_STATE.json`, active handoff)
must be a separate session-sync commit after material closure.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one new read-only session-sync manifest
helper script, focused tests, and a completion review. This scope does not
authorize session-file mutation, hook-chain wiring, behavior change in existing
checkers, runtime behavior, external repository work, public-sync, or production
readiness claims.

Protected paths:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/lastUpdated.json`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `governance/compat/build_session_sync_pack.py`
- `governance/compat/test_build_session_sync_pack.py`
- `docs/roadmaps/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_ROADMAP_2026-06-16.md`
- `docs/baselines/CVF_GC018_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_2026-06-16.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_FOR_CODEX_2026-06-16.md`
- `docs/reviews/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_COMPLETION_2026-06-16.md`

Operator authorization: operator approved session-sync pack builder roadmap
2026-06-16 after commit-steward session-sync preflight hardening closure at
`d709071c`.

Rollback boundary: revert only this session-sync pack builder material batch
if the script, tests, or completion review are incorrect. Do not revert
commit-steward hardening material commit `d709071c`, dispatch envelope material
commit `b2654e2e`, or any prior closed tranche.

## 9. Review Gate

Closure requires:

- focused tests pass;
- `build_session_sync_pack.py --enforce` exits 0 on clean tree;
- reviewer-fast PASS;
- pre-commit PASS;
- committed-range pre-closure autorun gate PASS after material commit;
- completion review with `Manifest delta: MATCH`.

## Evidence Requirements

| Evidence | Command |
|---|---|
| Focused tests | `python -m unittest governance.compat.test_build_session_sync_pack -v` |
| `--suggest` sample | `python governance/compat/build_session_sync_pack.py --suggest` |
| `--enforce` clean exit | `python governance/compat/build_session_sync_pack.py --enforce` (exit 0) |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` |
| Diff hygiene | `git diff --check` |
| Pre-closure autorun | `python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 6bf59f37 --head HEAD` |

## 11. Acceptance Criteria

| Criterion | Status |
|---|---|
| `--suggest` prints protected-path manifest without error | PASS |
| `--enforce` exits 0 on clean tree | PASS |
| `--enforce` exits 1 when drift is present | PASS |
| `build_path_plan` imported, not duplicated | PASS |
| `validate_aggregate_matches_sources` imported, not duplicated | PASS |
| No file writes or git stage as side effect of the script | PASS |
| Focused tests pass | PASS |
| Completion review with Agent Operation Trace Block present | PASS |
| `Manifest delta: MATCH` in completion review | PASS |

## 6E.1 Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_COMPLETION_2026-06-16.md` | file exists with trace block and `Manifest delta: MATCH` | PASS |
| Roadmap state | `docs/roadmaps/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_ROADMAP_2026-06-16.md` | tranche delivered; roadmap remains `ROADMAP_READY_FOR_GC018` as the planning record, no stale dispatch residue | PASS |
| Registry JSON | BLOCKED with reason | no GC-051 source/test/runtime registry surface authorized in this tranche | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no corpus registry Markdown owner authorized | BLOCKED with reason |
| External evidence digest | N/A with reason | no external source, provider, OCR, or live-proof artifact | N/A with reason |
| Session continuity | N/A with reason | session sync is a dedicated follow-up batch; material commit must land first | N/A with reason |
| System loop interlock | N/A with reason | no interlock registry mutation authorized | N/A with reason |
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

Return to operator only if:

- a required gate fails outside Allowed scope;
- `build_path_plan` import requires a logic change to the commit steward
  preflight script (escalate; do not proceed);
- `validate_aggregate_matches_sources` import requires a modification to
  `generate_active_session_state.py` (escalate; do not proceed).

## Operator Checkpoint

No operator checkpoint remains inside T1. Hook-chain wiring, additional
reviewer-fast checks, and public-sync remain separate operator decisions.

## Dispatch Prompt Envelope

```text
Role: Codex implementer + reviewer + closer
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_FOR_CODEX_2026-06-16.md
Commit mode: WORKER_MAY_COMMIT
executionBaseHead: 6bf59f37
Current-time notes:
  - NEW file tranche only. Do NOT mutate CVF_SESSION/** in the material commit.
  - run_agent_commit_steward_preflight.py may receive a minimal __name__ guard
    or __all__ to expose build_path_plan cleanly; no logic change allowed.
  - generate_active_session_state.py: import only; do not modify.
  - Session-sync (CVF_SESSION_MEMORY.md, ACTIVE_SESSION_STATE.json,
    AGENT_HANDOFF_V19) is a SEPARATE follow-up commit after material closure.
Do-not-misread notes:
  - build_session_sync_pack.py is READ-ONLY. It must not write, stage, or
    commit any file as a side effect of its own execution.
  - --enforce exits non-zero on drift or missing authorization; it does NOT
    auto-repair anything.
  - Tests live flat in governance/compat/ as test_<module>.py (62 existing
    test files follow this convention; there is no tests/ subdir).
Required first actions:
  1. git rev-parse --short HEAD  ->  must equal 6bf59f37
  2. python governance/compat/check_active_session_state.py --enforce  ->  PASS
  3. Read governance/compat/run_agent_commit_steward_preflight.py lines 1-145
  4. Read governance/compat/generate_active_session_state.py lines 1-155
Return contract: COMPLETE_PENDING_REVIEW
  Evidence required: focused test run output, --suggest sample, --enforce
  exit-0 sample, reviewer-fast PASS, diff hygiene PASS, completion review
  with Agent Operation Trace Block and Manifest delta: MATCH.
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 session-sync pack builder work order authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch, governance gates |
| Target paths | roadmap, GC-018, this work order |
| Allowed scope source | operator authorized session-sync pack builder roadmap 2026-06-16 |
| Before status evidence | commit-steward hardening material commit `d709071c`; HEAD `6bf59f37` |
| After status evidence | Codex implemented the tool and tests; tranche committed as one material batch |
| Diff evidence | tranche material range from `6bf59f37` |
| Approval boundary | bounded read-only tooling tranche; no session mutation |
| Claim boundary | no runtime/provider/public/production claim |
| Agent type | Codex orchestrator and implementer (single-agent multi-role) |
| Invocation ID | `work-order-session-sync-pack-builder-2026-06-16` |
| Expected manifest | `docs/baselines/CVF_GC018_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_2026-06-16.md`; `docs/roadmaps/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_COMPLETION_2026-06-16.md`; `governance/compat/build_session_sync_pack.py`; `governance/compat/test_build_session_sync_pack.py` |
| Actual changed set | `docs/baselines/CVF_GC018_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_2026-06-16.md`; `docs/roadmaps/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_SESSION_SYNC_PACK_BUILDER_AND_AUTHORIZATION_MANIFEST_COMPLETION_2026-06-16.md`; `governance/compat/build_session_sync_pack.py`; `governance/compat/test_build_session_sync_pack.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order authorizes one bounded read-only tooling tranche. It does not
authorize session-file mutation, hook-chain wiring, behavior change in existing
checkers, runtime behavior, external repository work, public-sync, co-work
product development, production readiness, or public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control tooling. Public-sync is not
authorized.

rawMemoryReleased: false
