Status: ACTIVE_AUTHORIZATION
Memory class: POINTER_RECORD

# CVF GitHub Workspace CI Debt Repair Authorization

## Target / Source

Target: GitHub CI and local workspace debt on the provenance PR branch.
Source: GitHub PR #22 CI logs, `.gitignore`, workflow files, and active session
state checker source.

## Purpose

Authorize a narrow GitHub/workspace debt repair for the already-open provenance
PR branch. The repair is limited to CI reproducibility and local-only path
handling discovered after pushing the R72 governance rebalance branch to
GitHub.

## Scope / Methodology

Method: inspect failing CI logs, patch only the workflow/checker paths needed for
reproducible PR execution, run focused local checks, and keep public-sync
untouched.

## Scope / Target / Owner Boundary

Owner: Codex acting as provenance PR cleanup implementer after operator
authorization.

Scope: provenance GitHub/workspace cleanup only.

Out of scope: public-sync mutation, public repository push, product runtime
behavior, provider live proof, PR merge, or roadmap execution.

## Claim Boundary

Claim: this artifact authorizes the protected checker/test edits needed to make
GitHub CI evaluate PR branch state without requiring ignored local-only
materials.

Final verification boundary: local gates and GitHub PR checks after push.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update the active session state checker so
missing `requiredFirstReads` paths that are intentionally ignored by Git, such
as `.private_reference/` local-only evidence, do not fail GitHub CI clones while
normal tracked startup paths still fail when missing. Add focused unit coverage
for that behavior.

Protected paths changed:

- `governance/compat/check_active_session_state.py`
- `governance/compat/test_check_active_session_state.py`

Operator authorization: 2026-07-08 operator requested cleaning GitHub/workspace
debt before continuing the roadmap.

Rollback boundary: revert this authorization artifact and the two protected
checker/test edits if the GitHub PR still fails because missing ignored
`requiredFirstReads` paths should remain hard-blocking in CI.

## CI Repair Scope

Allowed non-protected paths:

- `.github/workflows/ci.yml`
- `.github/workflows/cvf-static-ci.yml`
- `.gitignore`
- guard contract lockfile tracked for CI dependency installation

Boundary: no public-sync mutation, no runtime provider proof, no product feature
change, no merge authorization, and no push to the public repository.

## Checker Source Read-Ahead Block

| field | value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_closure_packaging_preflight.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `Core Guard Self-Protection Authorization`; `Protected paths`; `Operator authorization`; `Rollback boundary`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `Memory class`; `Claim Boundary` |
| gateRunPurpose | Confirmation/evidence run after the artifact shape was known; not first discovery. |
| claimBoundary | Read-ahead evidence is limited to this authorization artifact and the protected checker/test edits in this repair. |

## Findings / Position

Position: the CI failures are infrastructure/workspace debt, not evidence that
R72 governance rebalance content is unsafe.

## Risk / Corrective Action

Risk: allowing ignored local-only paths too broadly could hide a missing tracked
startup document.

Corrective action: the checker exemption is limited to Git-ignored
`requiredFirstReads`; required startup guards and tracked first reads remain
hard-blocking when absent.

## Decision / Recommendation / Disposition

Disposition: APPROVE_BOUNDED_CI_DEBT_REPAIR.

Recommendation: push this repair to PR #22, then re-evaluate GitHub checks
before any merge decision.
