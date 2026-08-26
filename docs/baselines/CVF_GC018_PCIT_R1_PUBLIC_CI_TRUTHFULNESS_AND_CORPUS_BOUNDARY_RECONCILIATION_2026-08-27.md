# CVF GC-018 Baseline - PCIT-R1 Public CI Truthfulness And Corpus Boundary Reconciliation

Memory class: governed-dispatch-baseline

Status: APPROVED_FOR_EXECUTION

providerExecutionAuthority: FORBIDDEN

Batch ID: PCIT-R1

Dispatch base head: `eb60e89d3e53c8ae11bab36d1767ff43ff81430d`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent orchestrator/reviewer

Worker target: worker role

## Purpose

Authorize one bounded public CI workflow/runner reconciliation return against
the exact published public SHA, without product-source repair or external
effects.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id PCIT-R1 --title "Public CI Truthfulness And Corpus Boundary Reconciliation" --date 2026-08-27 --base 56c77c42416adee59752b285add6f66dad8458d4 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | public-sync plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact run evidence, scope, stop conditions and proof |
| checkerReadAheadConfirmation | dispatch, task-route, handoff, public-disposition and artifact-shape checker sources |
| docOnlyNewFields | failure classification vocabulary and single-tranche value table |
| claimBoundary | dispatch authoring provenance only |

## Authorization / Decision

Proceed with one PCIT-R1 worker. The worker may prepare a local public-sync
candidate but may not commit, push, deploy, access secrets, call providers, or
edit product/runtime/dependency source.

## Decision / Baseline / Proposed Tranche

Baseline: public SHA `a0ef5923d100b02c43294815ac9d01d8db20e8b8`
has green public-sync/public-surface checks and red general CI workflows.
Proposed tranche: exactly PCIT-R1, one no-commit workflow/runner candidate.
Decision: approved within the exact allowlist and stop conditions below.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| generic public CI invokes the private pre-commit hook | runtime workflow | `.github/workflows/ci.yml` | Web UI Tests / Governance Hook Chain | `run_local_governance_hook_chain.py --hook pre-commit` | GitHub Actions workflow | ACCEPT |
| public-safe sync preflight exists | runtime workflow | `.github/workflows/public-sync-preflight.yml` | Validate public candidate | `check_cvf_public_sync_candidate.py` | GitHub Actions workflow | ACCEPT |
| static CI runner mixes build checks with private continuity/governance checks | source behavior | `scripts/run_cvf_static_ci_gate.py` | `run_checks` | `check_continuation_chain` | static runner | ACCEPT |
| exact public SHA and public preflight success are retained in the terminal release packet | governed receipt | `docs/reviews/CVF_LPCI1_WEB_R3_FINAL_AUTH_BUILD_PUBLIC_RELEASE_COMPLETION_2026-08-27.md` | Verification And Evidence | `a0ef5923d100b02c43294815ac9d01d8db20e8b8` | terminal LPCI1 Web R3 review | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| artifact path collision | three target paths returned false from `Test-Path` before authoring | ACCEPT |
| token collision | `rg -n "PUBLIC_CI_TRUTHFULNESS|PCIT-R1|Public CI Truthfulness" docs CVF_SESSION` returned no prior authority | ACCEPT |
| owner collision | WSR1 concerns workspace-kit publication, not current GitHub Actions truthfulness | REJECT as owner for this lane |

## Scope / Target / Owner Boundary

Allowed public-sync writes are exactly the four workflow paths and static
runner/test paths named by the roadmap. Allowed private write is exactly
`docs/reviews/CVF_PCIT_R1_PUBLIC_CI_TRUTHFULNESS_AND_CORPUS_BOUNDARY_RECONCILIATION_WORKER_RETURN_2026-08-27.md`.

## Stop Conditions

Stop on required product/runtime source, dependency/lockfile mutation,
threshold weakening, hidden genuine failure, private corpus export, secret or
provider use, commit/push/deploy need, dirty starting worktree, or any path
outside the exact allowlist.

## Evidence / Verification

The worker must provide refreshed GitHub run/job receipts, a per-job
classification and coverage matrix, exact local diffs, focused runner proof if
changed, workflow/YAML validation, public-sync preflight, and dual-repository
HEAD/status/staging evidence.

## Public/Provenance Boundary

| Field | Value |
| --- | --- |
| Provenance repo | current private workspace; never push it to public |
| Public-sync clone | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync` |
| Verified public remote | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` |
| Worker effect boundary | local reversible edits only; no commit or push |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Public sync`, role=`dispatcher`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Public sync" --role dispatcher --lifecycle-phase pre-implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | retain exact dual-repository and no-commit controls |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status, source table columns, handoff fields, public disposition, task manifest heading |
| gateRunPurpose | confirm dispatch shape after evidence collection |
| claimBoundary | checker pass does not prove public CI success |

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: worker candidate and independent public commit/push evidence do not yet
exist.

## Claim Boundary

This baseline authorizes one no-commit workflow/runner candidate only. It
authorizes no public write, runtime/product repair, dependency upgrade, secret
access, provider/live action, CI suppression, or successor tranche.
