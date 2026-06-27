# Large-Scope Change Authorization — Archive Hygiene Batch 2026-06-10

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-10

## Purpose

Authorize the large-scope archive hygiene commit that moves 162 stale dated
docs (LHW12-19, WCE, EL1-3, DELTA-D1-D3, PM, PD1-2, etc.) from active
paths to their respective `archive/` subdirectories. This is a pure
file-move batch with no content changes.

## Scope / Target / Owner Boundary

Target: all stale dated docs identified by
`scripts/cvf_active_archive.py --execute` on 2026-06-10 as exceeding the
10-doc actionable threshold. Owner boundary: this authorization covers only
file-move operations within this batch; it does not authorize content changes,
core guard changes, or protected-path changes.

## Source / Predecessor Evidence

Predecessor: prior archive hygiene batch at commits `52ee4fc2` / `4cc74195` /
`dd15ba39` (2026-06-03) archived 91 docs. This batch clears the remaining 162
stale actionable docs accumulated since 2026-05-29 cutoff.

Archive script: `scripts/cvf_active_archive.py`. Archive baseline:
`governance/compat/CVF_ACTIVE_ARCHIVE_BASELINE.json`.

## Decision / Baseline / Proposed Tranche

Decision: execute archive hygiene now to unblock the pre-push gate and allow
98 local commits to be pushed to origin.

Baseline: `check_active_archive_hygiene.py` reports 0 actionable stale docs
after this batch (down from 163).

## Evidence / Verification

`check_active_archive_hygiene.py` output after script execution:
`Stale actionable: 0 (threshold 10)` — `COMPLIANT`.

## Large-Scope Change Authorization

Authorized scope: archive hygiene batch executed by
`scripts/cvf_active_archive.py --execute` on 2026-06-10.

Changed-file ceiling: 230 (162 moved docs + archive index updates + baseline
and reference link rewrites; actual: 222).

Rename/delete ceiling: 165 (162 source deletes + a few reference updates;
actual: 161).

Operator authorization: operator instructed on 2026-06-10 to run archive
hygiene and clear all pre-push blockers so the branch can be pushed.

Rollback boundary: revert only the archive moves and archive index updates
committed in this batch. Do not revert DSCP, LPCI2, DESIGN.md, or any prior
governance work.

## Claim Boundary

This is a scope authorization record for the archive hygiene file-move batch
only. It does not authorize future large-scope changes, core guard changes,
protected path changes, or any content modification to governed artifacts.
