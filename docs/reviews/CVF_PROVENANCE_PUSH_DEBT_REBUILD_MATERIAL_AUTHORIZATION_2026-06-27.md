# CVF Provenance Push Debt Rebuild Material Authorization

Memory class: REVIEW_ARTIFACT

Status: ACTIVE_AUTHORIZATION

Date: 2026-06-27

docType: authorization_record

## Purpose

Authorize a one-time material rebuild commit from pushed base `75fcad20` so the
already-reviewed FPC-SCG, FPC-DSD, FPC-UAP, and push-debt standardization
material state can be republished as a clean range before a separate
session-sync commit.

## Target / Source

| Target | Source |
|---|---|
| Rebuild material range | local backup branch `backup/provenance-push-debt-after-standardization-20260627-e1caa9d5` |
| Pushed provenance base | `origin/codex/p1-p5-small-debt-remediation` at `75fcad20` before rebuild |
| Active rebuild branch | `codex/provenance-push-rebuild-20260627` |
| Excluded session paths | `AGENTS.md`, root `AGENT_HANDOFF*.md`, `CVF_SESSION/`, and `CVF_SESSION_MEMORY.md` |
| Protected guard/checker paths | protected path list in this authorization |

## Scope / Methodology

The rebuild commit is allowed to restore material paths from local backup HEAD
`e1caa9d5` while excluding `AGENTS.md`, root `AGENT_HANDOFF*.md`,
`CVF_SESSION/`, and `CVF_SESSION_MEMORY.md`. Those protected session and
handoff paths must remain for a second dedicated session-sync commit.

## Findings / Position

The original local branch accumulated 28 commits ahead of upstream. Rebuilding
from pushed base `75fcad20` with one material commit and one session-sync commit
keeps the upstream ahead count within the new push-readiness limit and preserves
a recoverable backup branch:

`backup/provenance-push-debt-after-standardization-20260627-e1caa9d5`

## Risk / Corrective Action

Risk: the rebuild material commit changes more than 40 files.

Corrective action: this artifact provides explicit `Large-Scope Change
Authorization` for the one-time rebuild range and records the rollback boundary.

Risk: the rebuild material commit changes multiple protected Python guard files.

Corrective action: this artifact provides `Core Guard Self-Protection
Authorization` listing every protected path in the material rebuild range.

## Decision / Disposition

Disposition: ACTIVE_AUTHORIZATION for the rebuild material commit only.

## Large-Scope Change Authorization

Authorized large-scope scope: one-time material rebuild from pushed base
`75fcad20` to the already-reviewed local material state at `e1caa9d5`, excluding
active session and handoff paths.

Changed-file ceiling: 90 files.

Rename/delete ceiling: 10 files.

Operator authorization: the operator instructed the agent to process the
provenance push-debt issue and standardize the lesson before returning to next
tranche work.

Rollback boundary: if the rebuild material commit is rejected, abandon only
branch `codex/provenance-push-rebuild-20260627` and return to backup branch
`backup/provenance-push-debt-after-standardization-20260627-e1caa9d5`. Do not
delete or rewrite the backup branch.

## Core Guard Self-Protection Authorization - Rebuild Material Commit

Authorized guard-maintenance scope: restore the already-reviewed guard/checker
material state from backup HEAD `e1caa9d5` into a clean material rebuild commit.

Protected paths:

- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/check_dice_machine_candidates.py`
- `governance/compat/check_fpc_system_chain_acceptance_ledger.py`
- `governance/compat/check_raw_memory_release_invariant.py`
- `governance/compat/check_system_loop_interlock.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/run_agent_push_readiness_preview.py`
- `governance/compat/run_worker_return_fast_gate.py`
- `governance/compat/test_check_dice_machine_candidates.py`
- `governance/compat/test_check_fpc_system_chain_acceptance_ledger.py`
- `governance/compat/test_check_raw_memory_release_invariant.py`
- `governance/compat/test_check_system_loop_interlock.py`
- `governance/compat/test_run_agent_push_readiness_preview.py`
- `governance/compat/test_run_worker_return_fast_gate.py`

Operator authorization: the operator approved handling the push-debt repair and
required the prevention lesson to be standardized so future agents cannot
repeat it.

Rollback boundary: if this guard-maintenance rebuild is rejected, abandon only
the rebuild branch and preserve both backup branches. Do not revert previously
pushed commit `75fcad20` or public-sync commit
`04d88109317c780ceb2062a257c0e863e2379276`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance rebuild authorization. No public-sync repository
work or public catalog claim is authorized by this artifact.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | provenance push debt rebuild, 2026-06-27 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | git branch backup, git switch, git restore, apply_patch, governance gates |
| Target paths | material rebuild paths from `75fcad20..e1caa9d5`, excluding active session and handoff paths |
| Allowed scope source | operator instruction to repair provenance push debt and prevent repeat agent behavior |
| Before status evidence | upstream branch at `75fcad20`; backup branch at `e1caa9d5`; rebuild branch created from `75fcad20` |
| After status evidence | material rebuild commit validation pending |
| Diff evidence | `git diff --name-status` on rebuild material worktree |
| Approval boundary | one material rebuild commit only |
| Claim boundary | no session-sync commit, branch push, public-sync, runtime/provider/live behavior, MPI-T6 reopen, adapter implementation, or package activation |
| Agent type | reviewer/closer |
| Invocation ID | provenance-push-debt-rebuild-material-authorization-2026-06-27 |
| Expected manifest | this authorization plus material rebuild paths restored from backup |
| Actual changed set | material rebuild worktree before commit |
| Manifest delta | MATCH |

## Claim Boundary

This artifact authorizes only the material rebuild commit on
`codex/provenance-push-rebuild-20260627`. It does not authorize rewriting the
backup branches, pushing public repository content, or reopening any parked
runtime/provider/live/MPI-T6 lane.
