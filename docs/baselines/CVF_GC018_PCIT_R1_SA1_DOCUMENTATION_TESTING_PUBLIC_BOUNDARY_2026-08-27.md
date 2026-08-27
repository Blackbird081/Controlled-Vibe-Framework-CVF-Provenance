# CVF GC-018 Baseline - PCIT-R1-SA1 Documentation Testing Public Boundary

Memory class: governed-dispatch-baseline

Status: APPROVED_FOR_EXECUTION

Batch ID: PCIT-R1-SA1

Dispatch base head: `2c9f7d3b2`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent orchestrator/reviewer

Worker target: one no-commit workflow worker

## Purpose

Release one bounded amendment inside PCIT-R1 for the public
`Documentation & Testing` workflow exposed by PR run `33036642522`. Reconcile
private-corpus jobs, stale bootstrap and false-green summary behavior without
opening a new roadmap or changing product/dependency surfaces.

## Decision / Baseline

Decision: release one owner-only no-commit amendment. Baseline: public branch
commit `910665e62`, unmerged PR `#4`, hosted finding run `33036642522`, and
private reviewer evidence commit `92ae3460a`.

## Evidence / Verification

Reviewer must require the bounded job/coverage matrix, YAML validation, exact
two-path worker manifest, public-sync preflight and a new exact-SHA hosted run
before merge. Current evidence proves the need and boundary, not the repair.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id PCIT-R1-SA1 --title "Documentation Testing Public Boundary Scope Amendment" --date 2026-08-27 --base 2c9f7d3b2 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | public-sync plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-backed PCIT-R1-SA1 authority, exact ownership and proof |
| checkerReadAheadConfirmation | dispatch-quality, governed-artifact, task-route, public-disposition and scaffold-provenance checkers |
| docOnlyNewFields | amendment character; PR evidence boundary |
| claimBoundary | authoring provenance only; no public execution claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| parent PCIT-R1 authority and blocked review | parent roadmap/baseline/work order; reviewer evidence commit `92ae3460a` | operator explicitly approves one owner-only amendment | RELEASED_BY_OPERATOR |
| public candidate | branch commit `910665e62`; PR `#4` unmerged | retain prior five-path candidate read-only | RELEASED_READ_ONLY |
| hosted finding | PR run `33036642522` | amendment limited to its owning workflow | RELEASED_BOUNDED |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| PR workflow invokes private-corpus checkers | repository-boundary mismatch | `.github/workflows/documentation-testing.yml` | jobs list | jobs | GitHub Actions | ACCEPT |
| Python job installs a non-package directory | bootstrap drift | `.github/workflows/documentation-testing.yml` | `test` / Install dependencies | test | GitHub Actions | ACCEPT |
| summary can pass over failed dependencies | false-green orchestration | `.github/workflows/documentation-testing.yml` | `status-check` | status-check | GitHub Actions | ACCEPT |

## Negative Search And Collision Discipline

Artifact paths were absent before authoring. Token search found only the
session checkpoint authorizing PCIT-R1-SA1; no competing baseline or work order
exists. Disposition: create one paired amendment packet without R2.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Public sync`, role=`dispatcher`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | source table columns, dispatch status, ownership, public disposition and scaffold fields |
| gateRunPurpose | confirm amendment packet after source review |
| claimBoundary | checker conformance does not prove hosted success |

## Public/Provenance Boundary

Private provenance owns authority/evidence. The sibling public-sync clone owns
the one workflow candidate. Worker public writes are local and reversible;
commit, push, merge and deployment remain reviewer-only.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: amendment implementation and accepted exact-SHA hosted proof do not yet
exist; PR `#4` remains unmerged.

## Claim Boundary

This baseline authorizes one no-commit amendment for one public workflow. It
does not authorize other owners, product source, packages, dependencies,
secrets, providers, Netlify configuration, branch-policy bypass, merge or R2.
