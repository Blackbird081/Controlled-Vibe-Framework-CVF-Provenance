# CVF External Source Mirrors

Memory class: PRIVATE_REFERENCE_CONTROL_PLANE

Status: ACTIVE_REFERENCE

docType: private_reference_index

Date: 2026-06-29

## Purpose

This folder is the local parking area for cloned upstream repositories used as
source reference during external absorption.

It exists to prevent a recurring absorption blind spot: an external-agent pack
or summary may be useful, but it is not the upstream source of truth when the
original repository can be cloned and pinned.

## Storage Rule

Clone upstream repositories under this folder only as local reference inputs.
Repository payloads are intentionally ignored by git. Track only:

- `.private_reference/source_mirrors/README.md`
- `.private_reference/source_mirrors/INDEX.md`
- `.private_reference/source_mirrors/.gitignore`

Do not track cloned source contents, dependency installs, generated indexes,
runtime outputs, package caches, or third-party repository `.git` data.

## Naming Convention

Use a stable owner/repo slug and pin the commit in the index:

```text
.private_reference/source_mirrors/<owner>__<repo>/
```

Example:

```text
.private_reference/source_mirrors/addyosmani__agent-skills/
```

The clone folder may contain the upstream git repository locally, but the
governed authority record is the matching row in `INDEX.md`.

## Authority Boundary

Source mirrors are reference inputs only. They are not CVF-owned source, not
runtime dependencies, not package roots, not provider proof, not public-sync
artifacts, and not production-readiness evidence.

External-agent absorption packs remain secondary artifacts. When both an
upstream repository and a derived external-agent pack exist, source-verification
for repo facts must prefer the pinned upstream source mirror or a live upstream
URL/commit record over the derived pack.

## Required Metadata

Every cloned source mirror must have a row in `INDEX.md` with:

- upstream repository URL;
- local mirror path;
- pinned commit SHA or `PENDING_CLONE`;
- clone or verification date;
- related external-agent pack or absorption folder;
- current absorption lane;
- source authority disposition;
- runtime boundary.

## Claim Boundary

This folder does not authorize cloning by itself, runtime install, dependency
installation, hook execution, provider calls, public export, package activation,
or direct import. Any absorption, package promotion, checker, or runtime work
still requires the normal CVF governed chain.
