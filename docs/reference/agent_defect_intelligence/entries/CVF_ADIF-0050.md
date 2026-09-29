# ADIF-0050 - Public Repository Used As Governed Authoring Source

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0050
title: Public repository used as governed authoring source
defectCategory: AUTHORITY_BOUNDARY
defectClass: PROCESS_NONCOMPLIANCE
defectRole: worker
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Worker execution (WORKER_MUST_NOT_COMMIT); Reviewer-return review; Public-sync; Closure
roles: operator; dispatcher; worker; reviewer; closer; session-sync steward
lifecyclePhases: pre-implementation; pre-closure; pre-push
surfaceSelectors: private provenance repository and sibling public-sync repository
detectionSignals: governed implementation or review commits appear on public main before a matching provenance commit; public-only mapped filenames are treated as provenance authority; internal work-order or review evidence is published
enforcementLevel: GUIDANCE_ONLY
checkerBindings: NOT_APPLICABLE_WITH_REASON: current local gates cannot prevent a separate machine or agent from authoring and pushing directly in the public clone
promotionState: DESIGN_REVIEW_REQUIRED
supersedes: NONE
lastVerifiedCommit: e26253e25
roadmapSeedId: NONE
```

## Purpose

Prevent the curated public-sync repository from becoming the authoring source
for governed CVF learning, implementation, review, or closure work.

## Scope / Applies To

Applies whenever work can touch both the private provenance repository and the
sibling public-sync clone, including work performed on another computer before
the repositories have been synchronized.

## Bad Example

Implement and review a new bootstrap tranche in the public clone, push it to
public `main`, and only later discover that provenance lacks the learning,
source, review evidence, and mapped-filename context.

## Good Example

Author and accept governed work in provenance first. Classify every changed
path for public export, use the canonical mapper into a clean sibling
public-sync clone, run the public pre-push gates, then push the public commit
and record both receipts.

## Canonical Sources

- `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md`
- `scripts/cvf-public-sync.ps1`
- `docs/reviews/CVF_PUBLIC_FIRST_GOLDEN_DOWNSTREAM_BOOTSTRAP_RECOVERY_2026-07-23.md`
- `docs/reference/agent_defect_intelligence/README.md`

## Remediation

1. Freeze further public-first edits.
2. Fetch the exact public incident range into provenance without rewriting
   either history.
3. Import with no-commit operations, reconcile mapped filenames against the
   canonical projection script, and run provenance tests.
4. Commit and push provenance before making a forward public correction.
5. Remove private execution evidence from public, retain only reviewed
   public-safe surfaces, run public gates, and push normally.
6. Record both commit receipts and keep the learning private unless a separate
   export decision authorizes it.

## Epistemic Process Block

### Expected Result / Prediction

A public-only authoring flow should be recoverable by copying its commits into
provenance without semantic changes if both repositories are equivalent.

### Evidence Comparison

The four public commits imported without textual conflicts, but the dedicated
test failed immediately because the public-authored harness assumed
public-only mapped filenames existed in provenance. Nine Markdown artifacts
also lacked required provenance structure, and five internal evidence files
had been unnecessarily published.

### Contradiction Or Gap Disposition

The repositories are deliberately not equivalent. Public is a projection with
mapped aliases and a narrower evidence surface, so public-first authoring
bypasses both authority order and path classification.

### Claim Update

Recovery must reconcile semantic repository roles, not merely copy commits.
No automatic cross-machine prevention exists yet.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local private provenance workspace and sibling public-sync clone |
| Session or invocation | golden downstream public-first recovery, 2026-07-23 |
| Working directory | repository root |
| Command or tool surface | Git source inspection, no-commit import, PowerShell harness, governance gates, apply_patch |
| Target paths | ADIF-0050 and entries README row |
| Allowed scope source | operator instruction to process the misplaced learning and synchronize both repositories under CVF rules |
| Before status evidence | public `571cb21b7` contained four unmatched public-first commits |
| After status evidence | entry is resolver-discoverable after the provenance material commit |
| Diff evidence | new entry and entries README row |
| Approval boundary | learning and repository recovery only; no provider, CLI/MCP agent, deployment, branch protection, or history rewrite |
| Claim boundary | guidance only; no automatic prevention claim |
| Agent type | reviewer/closer |
| Invocation ID | `public-first-authority-boundary-adif-0050-20260723` |
| Expected manifest | ADIF-0050 and entries README row |
| Actual changed set | ADIF-0050 and entries README row |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no ADIF entry is deleted or renamed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance defect intelligence. The public corrective
projection is recorded separately.

## Claim Boundary

This entry records a recurring authority-boundary risk and its bounded recovery
sequence. It does not implement a cross-machine checker, prevent direct public
pushes, or authorize provider, runtime, deployment, or public export work.
