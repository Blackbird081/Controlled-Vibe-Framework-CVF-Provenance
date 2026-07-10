# CVF MSEA R82 Workspace Distribution And Update Release Roadmap

Memory class: FULL_RECORD

Status: INTEGRATED_EXECUTION_AUTHORIZED

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
| R82A | Distribution/version contract | manifest and source-backed public boundary | AUTHORIZED |
| R82B | Public-safe installer and profile materializer | parser, path, and deny-token checks | AUTHORIZED |
| R82C | Clean-room install proof | PowerShell 5.1 and PowerShell 7 results | AUTHORIZED |
| R82D | Update and rollback proof | successful refresh plus invalid-update restoration | AUTHORIZED |
| R82E | Profile delivery proof | public-free and paid-user-safe manifests; operator-local rejection | AUTHORIZED |
| R82F | Public-sync and release decision | remote, changed-set, CI/gate, push, and final decision | AUTHORIZED |

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

DEFERRED_PRIVATE_ONLY

Reason: roadmap and execution evidence stay in provenance. Only separately
allowlisted public-safe product files may be exported during R82F.

## Claim Boundary

This roadmap authorizes bounded Windows workspace distribution proof and a
public-sync decision. It does not claim hosted, paid-user production,
cross-platform, provider, or downstream application readiness.
