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

## Mandatory Upstream Freshness Preflight

Operator-authorized on 2026-09-14. Before starting a new repository audit or
absorption batch, including reuse of an existing mirror, the dispatcher must
observe the canonical upstream again before freezing the source manifest.
An old clone date, local remote-tracking ref, or earlier receipt is insufficient.

1. Verify repository identity and resolve the live default branch and full HEAD
   SHA with `git ls-remote --symref <canonical-url> HEAD`, or an authoritative
   repository API. Record UTC observation time, URL, command/result, branch,
   observed SHA, existing analysis pin, and the selected next analysis pin.
2. If the source is absent or the selected pin differs, acquire the complete
   selected source tree through the authorized clone/fetch scope. Default to
   the freshly observed default-branch HEAD. A release/tag or historical target
   requires an explicit audit-purpose reason and an immutable resolved SHA;
   latest HEAD is not automatically the latest stable release.
3. For an existing mirror, compare the previous pin with the observed upstream:
   record ancestry/divergence, changed paths, and impact on selected mechanisms,
   consumers, tests and retained adverse findings. Reuse unchanged blob evidence;
   read affected deltas before carrying findings forward to the new pin.
4. Verify the acquired commit, clean checkout, license and manifest; update the
   source index and linked acquisition receipt before dispatch. If HEAD moves
   during acquisition, record the new observation and reconcile it before the
   manifest freeze. Do not silently substitute a branch name for the chosen SHA.
5. Freeze that pin for worker execution. Never pull/reset or replace a checkout
   in use by another worker; prepare a separate pinned checkout within authorized
   scope or defer the update. At the next decision boundary, check freshness
   again and assess relevant deltas without restarting unchanged evidence work.

If upstream observation or acquisition fails, record the concrete blocker and
do not claim current-upstream coverage. Historical-pin work may proceed only
when its governing scope explicitly permits it. This preflight does not itself
authorize source execution, dependency installation or additional repositories.

Operator exception: the already-dispatched QM-RUNTIME-VALUE-R2 investigation
retains `51bf455ea414a58f70274284ce212142518e556a`; do not reopen or repin that
batch under this rule. This exception does not extend to other repositories or
future QM batches and makes no current-upstream completion claim.

### Lightweight Receipt Check

Before dispatch, run `python governance/compat/check_upstream_freshness_receipt.py
--receipt <acquisition-receipt.json>` and retain its exit status with the packet.
The command exits 1 for missing, malformed or inconsistent evidence. Automatic
enforcement also runs inside `check_external_knowledge_intake_routing.py`, which
is already called by pre-dispatch, reviewer-fast, pre-commit and pre-push gates.
No extra network call or hook process is added.

New work orders containing a named source-mirror path or `source-intake` must
include exactly one `## Upstream Freshness Preflight` section with one JSON
array of receipts. Supply one receipt per named mirror; each selected pin must
also appear in the work-order scope outside that section. Empty arrays, missing
mirrors, duplicate repositories and invalid receipts block the gate. New,
not-yet-committed work orders also require observation within the last 24 hours
at gate execution, preventing reuse of an old receipt for a new dispatch.

Work orders unchanged from activation baseline
`7dc3dc51238b4f5092d0482624750f1b555380fc` retain their frozen contract, including
QM R2. Modified or newly authored packets must satisfy the new binding. This
does not rescan historical packets outside the gate's changed-path set.
Status-only closure of a pre-activation dispatch may append its Machine Closure
Package without a fresh observation; changing its source scope still requires
the receipt. Closure is not a new audit dispatch.

The JSON object has exactly these string fields:

| Field | Value |
|---|---|
| `schemaVersion` | `cvf.upstream-freshness.v1` |
| `sourceUrl` | Canonical credential-free HTTPS repository URL |
| `observedAt` | Actual remote-observation UTC timestamp |
| `manifestFrozenAt` | Actual manifest-freeze UTC timestamp, after observation and not in the future |
| `defaultBranch` | Full `refs/heads/...` reference |
| `observedHead` | Full lowercase 40-character observed Git SHA |
| `selectedPin` | Full lowercase 40-character analysis SHA |
| `previousPin` | Prior full SHA, or `NONE` for first acquisition |
| `selectionReason` | Required nonempty audit-purpose reason when selected pin differs from observed HEAD; otherwise empty allowed |
| `deltaSummary` | Required nonempty changed-path and scope-impact summary when prior pin differs from upstream; otherwise empty allowed |
| `lsRemoteOutput` | Captured output of the live symbolic-HEAD lookup, binding branch and observed SHA |

Observation must occur in the current preflight, at most 24 hours before the
manifest freeze. A delayed freeze requires another observation. Historical
receipts remain reproducible against their recorded freeze time; a previous
batch's receipt is not permission to skip a new observation. API-based
acquisition remains supported procedurally, but this lightweight checker needs
the additional symbolic-HEAD Git observation in its receipt.

The checker validates structure, timestamp order, captured HEAD consistency
and required delta/selection explanations. It cannot authenticate a supplied
receipt, prove the remote remains current, verify acquisition or judge semantic
delta quality. The reviewer still verifies provenance, the acquired pin and
manifest through the source evidence. It performs no network or source execution.

## Claim Boundary

This folder does not authorize cloning by itself, runtime install, dependency
installation, hook execution, provider calls, public export, package activation,
or direct import. Any absorption, package promotion, checker, or runtime work
still requires the normal CVF governed chain.
