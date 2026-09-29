# CVF MSEA R82 Workspace Distribution And Update Release Roadmap

Memory class: FULL_RECORD

Status: RC_PASS_BOUNDED_AND_PUBLIC_SYNCED

docType: roadmap

Date: 2026-07-10

Owner: Codex

## Authorization / Decision

Operator authorized completion of R82A through R82F after R81 reached
`RC_PASS_BOUNDED`.

R82 converts the proven local Windows workspace flow into a bounded,
public-safe distribution and update surface. One integrated dispatch may
execute all six tranches without separate operator pauses, provided every
public/private boundary check remains clean.

## Purpose

Prove that a user can install, select a public-safe profile, update, recover
from an interrupted or invalid update, and receive the same bounded workspace
surface from the public repository.

## Scope

In scope:

- a versioned public workspace distribution manifest;
- a standalone Windows installer that clones only the public repository;
- public-free and paid-user-safe profile materialization;
- repeatable update and backup restoration using the existing reconciler;
- clean-room proof under Windows PowerShell 5.1 and PowerShell 7 when present;
- bounded public-sync export and GitHub push after all local gates pass.

Out of scope:

- `operator-local` or provenance continuity distribution;
- `Policy_Local` application changes;
- non-Windows support, hosted service, provider/live proof, Memory/RAG,
  retrieval, vectorization, legal workflow, or production SLA claims;
- checker, hook, Fast Lane, or broad governance refactoring.

## Non-Goals

R82 does not create an MSI, package manager, entitlement server, licensing
system, auto-updater daemon, or cross-platform installer. It establishes the
smallest supportable Windows distribution contract.

## Product Boundary

| Surface | R82 rule |
|---|---|
| Provenance | owns source, private evidence, and distribution authoring |
| Public core | receives only public-safe scripts, manifest, and guidance |
| Local workspace | contains a hidden public clone, generated wrappers, selected public profile, and secret-free receipt |
| Operator-local | remains private and is never selectable by the public installer |

## Design Control Gate

R82 preserves source verification, public/private separation, command-backed
closure, and reviewer decision evidence. Distribution convenience may not
weaken remote validation, path containment, profile allowlisting, or rollback.

## Roadmap Tranches

| Tranche | Objective | Required evidence | Status |
|---|---|---|---|
| R82A | Distribution/version contract | manifest and source-backed public boundary | PASS |
| R82B | Public-safe installer and profile materializer | parser, path, and deny-token checks | PASS |
| R82C | Clean-room install proof | PowerShell 5.1 and PowerShell 7 results | PASS |
| R82D | Update and rollback proof | successful refresh plus invalid-update restoration | PASS |
| R82E | Profile delivery proof | public-free and paid-user-safe manifests; operator-local rejection | PASS |
| R82F | Public-sync and release decision | remote, changed-set, CI/gate, push, and final decision | PASS |

## Work Plan

1. Author and gate the integrated dispatch pair.
2. Add the public distribution manifest, installer, profile materializer, and
   root-guide/update integration.
3. Run local clean-room install, profile, update, and rollback proof.
4. Sync only the bounded public-safe changed set to the sibling public clone.
5. Run public checks, commit/push only when clean, then close R82 from evidence.

## Acceptance Criteria

- installer accepts only `public-free` and `paid-user-safe`;
- installer verifies the exact public remote before using an existing core;
- receipt contains no secret or provenance-only path;
- selected public packs contain no private continuity token;
- update succeeds and a forced invalid replacement restores the prior core;
- PowerShell 5.1 and PowerShell 7 proof pass when both executables are present;
- public-sync changed set contains no baseline, review, roadmap, session, or
  private artifact;
- R82F records exact public and provenance commits or returns a blocker.

## Verification / Evidence

| Evidence | Required result |
|---|---|
| Script parser | all changed PowerShell files parse in both available shells |
| Package build | deterministic manifest inputs and SHA-256 output |
| Install | hidden public core, wrappers, profile, and receipt created |
| Update/restore | refresh succeeds and failed replacement restores prior HEAD |
| Public boundary | exact public remote and no private token/path in exported set |
| Git | clean worktrees and pushed SHAs match remotes |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `Status: INTEGRATED_EXECUTION_AUTHORIZED`; section name: Authorization / Decision; section name: Purpose; section name: Scope; section name: Non-Goals; section name: Work Plan; section name: Acceptance Criteria; section name: Public Export Disposition |
| gateRunPurpose | confirmation before integrated dispatch and later closure |
| claimBoundary | R82 Windows workspace distribution and update only |

## Public Export Disposition

EXPORTED

Public remote: `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Public commit: `a4d5dba915f9ca8acea251a3a479ca9e1420d1fc`

Exported front door:
`docs/reference/workspace_distribution/README.md`

The roadmap and private execution evidence remain provenance-only. The public
commit contains the bounded distribution scripts, manifest, public guidance,
and workspace templates only.

## Machine Closure Package

| Closure item | Evidence | Final status |
|---|---|---|
| Roadmap state | This file has `Status: RC_PASS_BOUNDED_AND_PUBLIC_SYNCED`. | PASS |
| R82A-R82B product source | Provenance material commit `4939e59d0`; manifest version `0.1.0-rc1`. | PASS |
| R82C clean installs | Windows PowerShell 5.1 `public-free` and PowerShell 7 `paid-user-safe` targets. | PASS |
| R82D update and restore | successful update plus forced invalid-replacement restoration to the prior HEAD and remote | PASS |
| R82E profile boundary | 7-artifact and 9-artifact public profiles passed; `operator-local` was rejected | PASS |
| R82F public release | public commit `a4d5dba915f9ca8acea251a3a479ca9e1420d1fc`; public static CI 8/8 | PASS |
| Completion review | `docs/reviews/CVF_MSEA_R82_WORKSPACE_DISTRIBUTION_AND_UPDATE_RELEASE_COMPLETION_REVIEW_2026-07-10.md` | PASS |

## Claim Boundary

This roadmap authorizes bounded Windows workspace distribution proof and a
public-sync decision. It does not claim hosted, paid-user production,
cross-platform, provider, or downstream application readiness.
