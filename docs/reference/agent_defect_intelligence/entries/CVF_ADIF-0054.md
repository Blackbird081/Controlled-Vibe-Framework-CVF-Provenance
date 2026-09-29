# ADIF-0054 - Serial Public Projection Repair Before Push

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0054
title: Serial public projection repair before push
defectCategory: GATE_TRIGGER_FRICTION
defectClass: PHASE_GATE_PLACEMENT_GAP
defectRole: dispatcher; worker; reviewer; closer
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Public-sync; Reviewer-return review
roles: dispatcher; worker; reviewer; closer; session-sync steward
lifecyclePhases: pre-implementation; pre-closure; pre-push
surfaceSelectors: scripts/cvf-public-sync.ps1; public-sync pending candidate; relative TypeScript and JavaScript dependency edges
detectionSignals: private hook run against public clone; stale range-pinned profile; serial reviewer repair rounds; generated runtime residue; missing relative import or export target; full or live-named suite run in real public worktree
enforcementLevel: PARTIAL_CHECK
checkerBindings: governance/compat/check_review_cost_control.py
promotionState: STANDARD_ADDED_AND_MACHINE_GATE_PLACED
supersedes: NONE
lastVerifiedCommit: PENDING_CURRENT_HARDENING_COMMIT
roadmapSeedId: NONE
```

## Purpose

Make serial public-projection repair discoverable to future agents and bind it
to the earliest candidate preflight that can prevent recurrence.

## Scope / Applies To

Applies to CVF public-sync preparation and review of its pending candidate.
The entry does not authorize public writes, provider/live tests, or cleanup of
unrelated baseline debt.

## Bad Example

Run a private hook or stale policy profile against the public clone, hand the
partial projection to review, repair each missing dependency separately, run a
full suite in the real worktree, and discover runtime residue only at staging.

## Good Example

Build the complete candidate once, run the current-candidate public preflight,
return all ownership, residue, diff, and dependency-closure violations
together, then verify broader suites only in a disposable clean worktree.

## Canonical Sources

- `docs/reference/CVF_PUBLIC_SYNC_ONE_SHOT_PREFLIGHT_STANDARD_2026-08-24.md`
- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md`
- `scripts/cvf-public-sync.ps1`
- `scripts/check_cvf_public_sync_candidate.py`

## Remediation

Use only the public-sync-specific candidate preflight. Require the exact-SHA
GitHub status through protected `main`, including for admins. Consolidate its full
violation set before review. Reject unowned or generated pending paths and
missing relative dependencies before `-NoCommit`, staging, commit, or push.
Use a disposable exact-candidate worktree for broader tests and require fresh
authority before selecting any live/provider test.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker and governance maintainer |
| Provider or surface | local private provenance and sibling public-sync worktrees |
| Session or invocation | public-sync latency learning, 2026-08-24 |
| Working directory | repository root |
| Command or tool surface | git evidence inspection, exporter source read, focused pytest |
| Target paths | entry, one-shot standard, exporter, preflight, focused tests, local pre-push hook, GitHub Actions gate |
| Allowed scope source | operator instruction to convert the incident into learning and prevent recurrence |
| Before status evidence | public sync required serial dependency repairs and runtime residue cleanup before an approximately eight-second push |
| After status evidence | exporter invokes one consolidated fail-closed preflight before review or staging |
| Diff evidence | current material batch git diff and focused test result |
| Approval boundary | local governance learning and public-sync preparation only; no public write or live call |
| Claim boundary | partial machine prevention of named projection defects; no universal semantic-completeness claim |
| Agent type | worker |
| Invocation ID | `public-sync-one-shot-learning-2026-08-24` |
| Expected manifest | `.github/workflows/public-sync-preflight.yml`; `docs/reference/CVF_PUBLIC_SYNC_ONE_SHOT_PREFLIGHT_STANDARD_2026-08-24.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0054.md`; `scripts/check_cvf_public_sync_candidate.py`; `scripts/cvf-public-pre-push-hook.sh`; `scripts/cvf-public-sync.ps1`; `scripts/test_check_cvf_public_sync_candidate.py` |
| Actual changed set | `.github/workflows/public-sync-preflight.yml`; `docs/reference/CVF_PUBLIC_SYNC_ONE_SHOT_PREFLIGHT_STANDARD_2026-08-24.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0054.md`; `scripts/check_cvf_public_sync_candidate.py`; `scripts/cvf-public-pre-push-hook.sh`; `scripts/cvf-public-sync.ps1`; `scripts/test_check_cvf_public_sync_candidate.py` |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance defect intelligence and public-sync control detail.

## Claim Boundary

This entry records a reusable defect and its partial enforcement. The existing
review-cost checker covers serial review signals; the exporter-local machine
preflight covers candidate ownership, residue, diff hygiene, and relative
dependency closure. It does not claim all semantic or live behavior is checked.
