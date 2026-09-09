# CVF Agents Critical Repository Boundary

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-06-23

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This file
records one rotated AGENTS.md rule; it does not enumerate, map, or project
CVF state as a generated aggregate.

**Applies to:** any agent reading `AGENTS.md` who needs the repository
boundary rule rotated out of that file under the Governed File Size Guard
(GC-023).

## Purpose

Rotate the "Critical Repository Boundary - 2026-05-09" rule out of
`AGENTS.md` to keep that file under its governed line-count threshold,
without losing the rule itself. `AGENTS.md` retains a one-line pointer to
this file.

## Critical Repository Boundary - 2026-05-09

This workspace is the private provenance/archive repository:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git`

It contains full historical development material, evidence records, handoffs,
reviews, and internal continuity files. Treat it as locked for private audit and
deep review. Do not use this workspace as the public CVF product front door.

The only GitHub repository intended for public/external CVF information is:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Public-facing architecture, README, contributor, setup, governance, provider,
cost, or evidence-summary changes must be prepared and pushed from the sibling
public-sync clone:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Before any push that is meant for the public repository, run `git remote -v`.
If the current working directory is this provenance workspace or `origin`
contains `Controlled-Vibe-Framework-CVF-Provenance`, stop and switch to the
public-sync clone. Do not push the full provenance tree into the public repo.

## Operator-Authorized Provenance Push Route - 2026-09-09

When the operator says to push CVF, this workspace, or the current work to the
provenance GitHub repository, that statement is the per-invocation push
authorization. The agent must not ask the operator to repeat the authorization
or instruct the operator to unlock the remote manually.

The canonical route is
`powershell -ExecutionPolicy Bypass -File scripts\cvf-provenance-push.ps1
-Branch main`. The script must start with the provenance push URL locked, run
the full pre-push governance chain before unlocking, set the push URL only to
`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git`,
push the requested branch, and restore
`DISABLED_PROVENANCE_ARCHIVE_DO_NOT_PUSH_FROM_THIS_WORKSPACE` in its `finally`
path. Direct `git remote set-url`, an explicit-URL `git push`, and bypassing a
failed guard are not approved alternatives.

Before execution, verify the worktree is clean, the current branch is the
intended branch, and fetch/reconcile the tracked remote without destructive
history rewriting. After execution, verify `HEAD` equals the remote branch,
ahead/behind is `0/0`, the worktree is clean, and the push URL is locked again.
If a guard fails, repair only an authorized in-scope defect, rerun the canonical
route, and report a real blocker only when safe repair is not authorized.

## Claim Boundary

This file records the rotated repository-boundary rule and the operator-approved
safe provenance-push route. It does not authorize public-sync execution,
force-push, history rewriting, guard bypass, remote substitution, credential
disclosure, or pushing private provenance content to the public repository.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: describes the private provenance workspace's own boundary rule
relative to the public repository; not itself eligible for public-sync
export.
