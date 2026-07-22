# ADIF-0046 - Broad Projection Revives Superseded Public Claim

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0046
title: Broad projection revives superseded public claim
defectCategory: SOURCE_FIDELITY
defectClass: MACHINE_GATE_GAP
defectRole: session-sync steward
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Public-sync; Reviewer-return review; Closure
roles: reviewer; closer; session-sync steward
lifecyclePhases: pre-closure; pre-push
surfaceSelectors: public README, Architecture, provider-readiness, limitations, provider guide, and evidence-index projections
detectionSignals: a later projection restores a claim rejected or downgraded by a reviewed decision; certified status conflicts with limitations; cited public evidence index is absent
enforcementLevel: GUIDANCE_ONLY
checkerBindings: NOT_APPLICABLE_WITH_REASON: no current checker compares cross-surface semantic dispositions and superseding review decisions before projection
promotionState: MACHINE_CHECK_CANDIDATE
supersedes: NONE
lastVerifiedCommit: b542a06da
roadmapSeedId: NONE
```

## Purpose

Prevent a broad public projection, curated front-door restore, or repository
sync from reviving a claim that a later governed review explicitly downgraded,
rejected, or held.

## Scope / Applies To

Applies when public-sync copies or restores README, Architecture, readiness
matrices, limitations, provider guides, catalogs, badges, or evidence indexes
from multiple source snapshots. It is especially relevant when a later receipt
projection changes evidence availability but does not include authority to
reverse an earlier semantic disposition.

## Bad Example

Copy a historical provider matrix after a reviewer has selected a bounded
non-certified option. Restore `CERTIFIED` because receipt files now exist, keep
a conflicting limitation, and cite an index path that the public repository
does not contain.

## Good Example

Before public export, compare each strong claim across the current reviewed
decision, readiness matrix, limitation register, provider guide, README,
Architecture, and cited evidence paths. Keep the later reviewed disposition
unless a fresh governed promotion explicitly changes it. Treat receipt
presence as evidence, not automatic promotion authority.

## Canonical Sources

- `docs/reference/CVF_MSEA_R65C_PUBLIC_SYNC_PUBLISH_OR_HOLD_AND_PROVIDER_RECEIPT_LINK_INTEGRITY_DECISION_MATRIX_2026-07-07.md`, R65 Option B evidence.
- `docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md`, L-007 provider boundary.
- `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md`, current public disposition and claim boundary.
- `docs/reviews/CVF_PUBLIC_SEVEN_STEP_AND_PROVIDER_CLAIM_RECONCILIATION_CLOSURE_2026-07-23.md`, regression evidence and repair.

## Remediation

Build a semantic projection manifest before public export. For every strong
claim, record the latest reviewed disposition, all public projection surfaces,
the exact evidence paths, and whether the export is allowed to promote,
preserve, downgrade, or remove the claim. Block export when a certified/badge
claim conflicts with a limitation or cites a missing evidence path. Checker
implementation requires a separate authorized batch.

## Epistemic Process Block

### Expected Result / Prediction

Once R65 selected Option B, later public projections should preserve OpenAI as
non-certified unless a fresh governed promotion explicitly reverses it.

### Evidence Comparison

Public `main` again contained an OpenAI `CERTIFIED` matrix row and a missing
OpenAI canary index link while the limitations register and provider guide
retained the R65 non-certified boundary.

### Contradiction Or Gap Disposition

The projection copied historical evidence and stale claim text without
carrying forward the later semantic decision. Existing link and phrase checks
did not prevent this cross-surface regression.

### Claim Update

R65's correction was locally valid but not durable across later broad
projection. A cross-surface semantic projection check is a machine-check
candidate; no prevention effectiveness is claimed yet.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local private provenance workspace and sibling public-sync clone |
| Session or invocation | public seven-step and provider-claim reconciliation, 2026-07-23 |
| Working directory | repository root |
| Command or tool surface | local Git history, rg, PowerShell source reads, apply_patch, public static/documentation gates |
| Target paths | ADIF-0046 and entries README row |
| Allowed scope source | operator requested reviewer handling, public/provenance documentation reconciliation, and learning capture for material findings |
| Before status evidence | R65 Option B existed, but public matrix at `c1076dc4b` restored OpenAI `CERTIFIED` and a missing index link |
| After status evidence | public commit `6ce1cf00c` restores the bounded provider disposition; defect is resolver-discoverable |
| Diff evidence | provenance material closure changed set includes this entry and README row |
| Approval boundary | governance learning and documentation repair only; no checker, runtime, provider, CLI/MCP, badge, or UI implementation |
| Claim boundary | guidance and machine-check candidate only; no automated prevention claim |
| Agent type | reviewer/closer |
| Invocation ID | `public-projection-regression-adif-0046-2026-07-23` |
| Expected manifest | ADIF-0046 and entries README row inside the documentation reconciliation closure batch |
| Actual changed set | ADIF-0046 and entries README row inside the documentation reconciliation closure batch |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance learning. The public documentation repair is
exported separately; this ADIF entry is not part of the public projection.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | cross-surface public projection regression guidance only |
| claimDisposition | CLAIM_REJECTED: no automatic semantic projection checker exists |
| receiptEvidence | `CLAIM_REJECTED_NO_RECEIPT`: source and Git evidence support the defect; no runtime receipt is used |
| actionEvidence | ACTION_EVIDENCE_PRESENT: R65 decision, conflicting public files, repaired public commit, and link verification |
| invocationBoundary | local reviewer inspection, documentation repair, and Git public export |
| interceptionBoundary | no provider, CLI/MCP adapter, browser, runtime, badge/UI, or production interception |
| claimLanguage | preserve later reviewed public dispositions across broad projection |
| forbiddenExpansion | no checker implementation, OpenAI promotion, provider parity, live proof, runtime, hosted, deployment, or production claim |

## Claim Boundary

This entry records a recurring semantic projection defect and a bounded
checker candidate. It does not claim that current gates automatically detect
the pattern or authorize provider-certification, UI, runtime, or public-export
implementation.
