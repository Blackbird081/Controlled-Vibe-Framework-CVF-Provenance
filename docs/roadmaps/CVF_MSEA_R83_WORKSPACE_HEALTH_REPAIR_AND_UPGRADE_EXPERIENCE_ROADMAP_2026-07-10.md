# CVF MSEA R83 Workspace Health Repair And Upgrade Experience Roadmap

Memory class: FULL_RECORD

Status: RC_PASS_BOUNDED_AND_PUBLIC_SYNCED

docType: roadmap

Date: 2026-07-10

Owner: Codex

## Authorization / Decision

The operator authorized complete R83 execution after R82 reached
`RC_PASS_BOUNDED_AND_PUBLIC_SYNCED`.

## Purpose

Turn the R82 Windows distribution candidate into an operable workspace that
can report its health, identify available updates, repair generated artifacts
without changing the selected profile, and guide one bounded upgrade flow.

## Scope

In scope:

- a machine-readable workspace status contract;
- read-only local and optional remote update checks;
- bounded wrapper/profile repair without core replacement;
- one root management command for status, update, and repair;
- stale-core, missing-artifact, and profile-drift migration proof;
- bounded public-sync and release decision.

Out of scope:

- MSI, package manager, daemon, silent/background update, entitlement,
  licensing, cross-platform support, hosted service, provider/live proof,
  `Policy_Local`, operator-local distribution, or downstream use-case work;
- checker, hook, Fast Lane, Memory/RAG, retrieval, or legal workflow changes.

## Non-Goals

R83 does not optimize repository size, add automatic scheduling, create a new
profile tier, or certify general-availability support. It solves observable
workspace health and bounded recovery only.

## Product Boundary

Status is read-only. Repair may regenerate public wrappers, guides, and the
currently selected public profile, but may not update the hidden core or select
a different profile. Update continues through the existing backup/rollback
reconciler. All public operations require the exact public repository remote.

## Design Control Gate

Status must remain read-only. Repair must preserve hidden-core HEAD and active
profile. Update must retain exact-remote validation and rollback. Any violation
blocks public release.

## Roadmap Tranches

| Tranche | Objective | Required evidence | Status |
|---|---|---|---|
| R83A | Workspace status contract | deterministic verdict and machine-readable output | PASS |
| R83B | Doctor and repair | missing/drifted generated artifacts restored without profile change | PASS |
| R83C | Unified upgrade UX | root status/update/repair command and guides | PASS |
| R83D | Migration proof | stale core, missing wrapper, drift, update, and rollback cases | PASS |
| R83E | Public release | exact diff, public checks, push, and bounded closure | PASS |

## Work Plan

1. Gate and commit the integrated dispatch packet.
2. Implement the public commands and wrapper/manifest wiring.
3. Run disposable health, drift, repair, update, and rollback proof.
4. Export and gate an exact public-safe bundle.
5. Close, push, and session-sync from final evidence.

## Acceptance Criteria

- status returns only `CURRENT`, `UPDATE_AVAILABLE`, `DRIFTED`, or
  `REPAIR_REQUIRED`;
- local status does not mutate the workspace;
- optional remote status detects a newer public `main` revision;
- repair preserves the active profile and hidden-core HEAD;
- update retains the R82 backup/rollback behavior;
- public projection contains no private session, roadmap, baseline, review, or
  operator-local artifact;
- exact public and provenance commits are recorded at closure.

## Verification / Evidence

Use disposable Windows workspaces for clean, stale, missing-wrapper,
profile-drift, repair, valid-update, and forced-invalid-update cases. Record
PowerShell parser results, JSON output, before/after hashes and commits, remote
URLs, changed sets, public static checks, and post-push equality.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `Status: INTEGRATED_EXECUTION_AUTHORIZED`; section name: Authorization / Decision; section name: Purpose; section name: Scope; section name: Acceptance Criteria; section name: Public Export Disposition |
| gateRunPurpose | confirmation before integrated dispatch and closure |
| claimBoundary | R83 Windows workspace health, repair, and upgrade experience only |

## Public Export Disposition

EXPORTED

Public remote: `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Public product commit: `3d6a8500864227bfbb620cba137efd5c541e5c99`

Public compatibility fix commit: `fbb6c4d493182bc50fe04fd9c74fc8bc09d4a348`

Exported front door: `docs/reference/workspace_distribution/README.md`

The roadmap and private evidence remain provenance-only.

## Machine Closure Package

| Closure item | Evidence | Final status |
|---|---|---|
| Roadmap state | This file has `Status: RC_PASS_BOUNDED_AND_PUBLIC_SYNCED`. | PASS |
| R83A status | four verdicts and JSON output proven on disposable workspaces | PASS |
| R83B repair | core HEAD/profile preserved and drift removed | PASS |
| R83C management | generated root command routes status, update, and repair | PASS |
| R83D migration | R82 commit upgraded to R83; forced failure restored exact state | PASS |
| R83E public release | public commits `3d6a85008` and `fbb6c4d49`; static CI 8/8 | PASS |
| Completion review | `docs/reviews/CVF_MSEA_R83_WORKSPACE_HEALTH_REPAIR_AND_UPGRADE_EXPERIENCE_COMPLETION_REVIEW_2026-07-10.md` | PASS |

## Claim Boundary

This roadmap authorizes bounded Windows workspace operability work. It does
not authorize production, cross-platform, hosted, entitlement, or use-case
claims.
