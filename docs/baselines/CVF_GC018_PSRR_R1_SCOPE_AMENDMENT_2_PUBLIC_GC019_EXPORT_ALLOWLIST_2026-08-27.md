# CVF GC-018 Baseline - PSRR-R1 Scope Amendment 2 Public GC-019 Export Allowlist

Memory class: governed-scope-amendment

Status: APPROVED_FOR_REVIEWER_REPAIR

Batch ID: PSRR-R1-SA2

Date: 2026-08-27

Decision owner: operator authority exercised by the orchestrator/reviewer under the standing full-authority instruction.

## Purpose

Authorize exactly two same-roadmap public-surface allowlist entries after hosted
runs at public SHA `01d27608` proved that the required PSRR GC-019 artifact is
also blocked by the public-surface policy solely because it lives under the
normally private `docs/reviews` family, and the first local rerun proved the
valid generated `USR-048_claude_design_handoff.gov.md` name collides with the
broad private-handoff glob. This is one closure repair, not a successor tranche.

## Decision / Baseline / Proposed Tranche

Decision: approve two exact-path manifest entries. Baseline: public SHA
`01d27608f1a1151bf642de24baf2ead8960331e7`, Documentation & Testing run
`33052498416`, Static CI run `33052498419`, and Public Surface run
`33052498450`. Proposed tranche: none; PSRR-R1-SA2 is a same-roadmap amendment.

## Target / Source

- Target: two exact entries in `governance/public-surface-manifest.json` for the already committed PSRR GC-019 artifact and generated USR-048 record.
- Source: `scripts/check_public_surface.py`, `governance/public-surface-manifest.json`, and the hosted failures above.

## Scope / Applies To

Reviewer may add only the two named exact paths with public-safe reasons,
commit and push it, run local public-surface/foundational/preflight checks, and
obtain fresh exact-SHA hosted proof. The artifact, generator, registry records,
validator, workflows, product source, and all other allowlist entries are
read-only.

## Evidence / Verification

The public-surface checker must pass with the exact entry while the
foundational guard continues to recognize the required GC-019 artifact. Fresh
hosted proof must distinguish any remaining AGT failure from this repaired
export-boundary defect.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| the public surface blocks the GC-019 artifact by family | hosted finding | canonical public-sync source at SHA `01d27608` | `BLOCKED_GLOBS`; run `33052498419` | `BLOCKED_GLOBS` | public-surface checker | ACCEPT |
| exact public exceptions are manifest-owned | checker contract | canonical public-sync source at SHA `01d27608` | `allowlist` | `allowlist` | public-surface policy manifest | ACCEPT |
| USR-048 is blocked only by a filename glob collision | local checker finding | canonical public-sync source at SHA `01d27608` | first SA2 rerun | `USR-048_claude_design_handoff.gov.md` | public-surface checker | ACCEPT |
| GC-019 remains required for the material commit range | hosted finding | `governance/compat/check_foundational_guard_surfaces.py` | structural change audit guard | `_check_structural_change_audit_guard` | foundational guard | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `scripts/check_public_surface.py`; `governance/compat/check_foundational_guard_surfaces.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Decision / Baseline / Proposed Tranche`; `Source Verification Block`; `Checker Source Read-Ahead Block`; `Public Export Disposition`; `Claim Boundary` |
| gateRunPurpose | authorize one exact public-boundary repair from hosted evidence |
| claimBoundary | authorization only; no repaired or green claim before fresh proof |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent orchestrator/reviewer acting under standing operator authority |
| Provider or surface | private provenance and public GitHub Actions evidence |
| Session or invocation | PSRR-R1-SA2 closure repair, 2026-08-27 |
| Working directory | private root; public sibling read-only before amendment commit |
| Command or tool surface | hosted job inspection, checker and manifest source read, governed amendment authoring |
| Target paths | this amendment only before public repair |
| Allowed scope source | standing operator authority plus exact hosted blocker |
| Before status evidence | private clean at `80a79500e`; public clean at `01d27608` |
| After status evidence | one committed private amendment before public manifest repair |
| Diff evidence | `git diff --name-status` |
| Approval boundary | two exact manifest entries; no AGT repair, workflow change, merge, or deploy |
| Claim boundary | scope authorization only, not repair success |
| Agent type | orchestrator/reviewer |
| Invocation ID | `psrr-r1-sa2-public-allowlist-2026-08-27` |
| Expected manifest | this one private amendment |
| Actual changed set | this one private amendment |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this private amendment is authority evidence; only the exact public
manifest entry is intended for export.

## Claim Boundary

This amendment authorizes two exact public manifest entries and their
reviewer-owned commit, push, and proof. It authorizes no broader private-review
export, validator weakening, workflow/source-skill/AGT/product change, merge,
deployment, secret or provider use, or successor roadmap.
