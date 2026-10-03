# CVF Downstream Gate Profile Migration And Upgrade Contract

Memory class: FULL_RECORD

Status: ACTIVE_STANDARD

docType: reference

Date: 2026-10-03

Batch ID: CVF-DGIP-T1

## Purpose

Define how projects receive, pin, upgrade and migrate to
`cvf.downstreamGateProfile@1.0.0` without rewriting history or project-owned content.

## Scope / Applies To

Applies to fresh bootstrap, repeated bootstrap, pre-existing governed projects
and explicit profile upgrades performed through `scripts/new-cvf-workspace.ps1`
and the runner `install` subcommand.

## Bootstrap Modes

| Mode | Condition | Result |
|---|---|---|
| FRESH | no continuity surface exists | profile, lock, workflow and continuity truth generated |
| EXISTING | a lock already exists | verified; `ALREADY_INSTALLED` with no file change, or `DRIFT_PRESERVED` (no overwrite) which fails bootstrap |
| EXPLICIT | operator passes `-InstallGateProfile` | tooling is installed; project-owned content is untouched |
| SKIP | pre-existing project without a lock | `MIGRATION_REQUIRED_SKIPPED`; the doctor reports `GATE_PROFILE_NOT_INSTALLED` and claims no coverage |

## Existing-Project Migration Steps

1. Inventory: run the doctor; a legacy project shows the migration gap.
2. Install the tooling explicitly with `-InstallGateProfile` (collisions with
   project-owned files in `scripts/cvf_gates/` stop with `BLOCKED_COLLISION`).
3. Adopt the continuity contract deliberately: add `continuityContract` to the
   state file and a `## Current Truth` block to `CVF_SESSION_MEMORY.md`. Until
   then CVF-DG-CONT-01 reports `BLOCKED_MIGRATION_REQUIRED` with locators. No
   automatic or heuristic alignment is performed.
4. Work orders: a candidate with a non-conforming `Status` line is corrected by
   its owner; unchanged historical work orders are not migrated.
5. CI: an existing project-owned workflow is preserved and reported as
   `PROJECT_OWNED_PRESERVED`; the PR phase stays unverified until it carries the
   pinned runner command.

## Upgrade

A new profile version is a new `profileId`. `install --upgrade` replaces the
inherited files and rewrites the lock only on explicit operator action; the old
lock is never edited in place by bootstrap. The Core doctor reports a project
whose copy differs from the Core source as `TRUSTED_MISMATCH`.

## Rollout Evidence

Real adoption in a downstream project, a hosted PR run and public export are
separate external-effect admissions and remain `DEFERRED_PRIVATE_ONLY`.

## Claim Boundary

Migration rules only. They do not assert that any real project has migrated or
that any hosted CI has run.
