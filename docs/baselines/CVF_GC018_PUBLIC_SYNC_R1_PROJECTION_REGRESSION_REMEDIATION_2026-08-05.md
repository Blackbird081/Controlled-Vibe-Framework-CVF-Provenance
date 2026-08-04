# CVF GC-018 Baseline - Public Sync R1 Projection Regression Remediation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: PUBLIC-SYNC-R1

dispatchBaseHead: `85ffba891`

rawMemoryReleased: false

## Purpose

Authorize one bounded remediation before another public export attempt: prevent
five previously removed private bootstrap evidence files from being projected,
restore projection-policy parity, and align the Guard Contract package-boundary
test with the already accepted `mandatory-gateway` export.

## Baseline Decision

Decision: `PUBLIC_SYNC_R1_REMEDIATION_AUTHORIZED_BOUNDED`

The operator explicitly requested continuation to the public repository. The
2026-08-05 dry candidate is rejected as an export artifact because it
reintroduced five private files and the full cvf-web suite reported 19 failures.
This baseline releases only the narrow projection/test repair. It does not
authorize repairing those 19 failures, a broad public export, or any live run.

## Scope / Applies To

Allowed provenance paths:

- `scripts/cvf-public-sync.ps1`
- `scripts/cvf_projection_policy.json`
- `scripts/test_get_cvf_projection_map.ps1`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/package.boundary.test.ts`
- `docs/reviews/CVF_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_WORKER_RETURN_2026-08-05.md`

The sibling public-sync clone is read-only for verification in this tranche.

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator instruction | `next`, following the blocked public-sync report on 2026-08-05 |
| Repository boundary | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` |
| Corrective public precedent | `docs/reviews/CVF_PUBLIC_FIRST_GOLDEN_DOWNSTREAM_BOOTSTRAP_RECOVERY_2026-07-23.md` |
| Public export rule | `docs/reference/archive/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md` |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id CVF-PUBLIC-SYNC-R1 --title "Public Sync Projection Regression Remediation" --date 2026-08-05 --base 85ffba891 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | public-sync plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with bounded authority, verified sources, exact paths, stop conditions, and offline verification. |
| checkerReadAheadConfirmation | Work-order dispatch, handoff boundary, ADIF disclosure, public export, and governed artifact read-ahead checkers reviewed. |
| docOnlyNewFields | `PUBLIC_SYNC_R1_REMEDIATION_AUTHORIZED_BOUNDED` |
| claimBoundary | Dispatch authority only; no public export or runtime claim. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Public export must use the sibling clone | VALUE_SET | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | Critical Repository Boundary | `Controlled-Vibe-Framework-CVF-public-sync` | repository boundary | ACCEPT |
| Five bootstrap evidence files were removed from public | VALUE_SET | `docs/reviews/CVF_PUBLIC_FIRST_GOLDEN_DOWNSTREAM_BOOTSTRAP_RECOVERY_2026-07-23.md` | public private-evidence removal row | `27137db4d` | corrective review | ACCEPT |
| Sync filtering is owned by deny patterns | EXISTS | `scripts/cvf-public-sync.ps1` | denylist and `Test-Denied` | `DENY_PATTERNS` | public sync script | ACCEPT |
| Mapper policy must match sync filtering | VALUE_SET | `scripts/cvf_projection_policy.json` | `sourceOfTruth` and `denyPatterns` | `denyPatterns` | projection policy | ACCEPT |
| Guard package exports mandatory gateway | VALUE_SET | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` | `exports` and `files` | `./runtime/mandatory-gateway` | package manifest | ACCEPT |
| Boundary test omits mandatory gateway | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/package.boundary.test.ts` | package boundary assertions | `packageJson` | Vitest boundary test | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact paths | `Test-Path` returned false for baseline, work order, and worker return before authoring | ACCEPT |
| Batch token search | `rg -n "PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION" docs CVF_SESSION` returned no collision | ACCEPT |
| Existing public candidate | Both provenance and public-sync worktrees were clean before this packet | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039,
ADIF-0043, ADIF-0049, ADIF-0006.

Disclosure count: 20

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Status, Source Verification Block, ADIF Defect Registry Disclosure, Public Export Disposition, Agent Handoff Contract Control Block, Reviewer Closure Conversion |
| gateRunPurpose | Confirm dispatch shape before implementation. |
| claimBoundary | Checker-shape evidence only; no implementation or export claim. |

## Acceptance Criteria

| Criterion | Required evidence |
| --- | --- |
| Five files classify as denied | focused mapper test and read-only mapper result |
| Script/policy parity remains exact | projection mapper policy-parity PASS |
| Package boundary aligns with manifest | focused Vitest PASS with provider keys cleared |
| Public-sync remains unchanged | public `git status --short` clean and HEAD unchanged |
| No provider use | all provider key variables cleared for tests; no live test command |

## Stop Conditions

- Any required change outside the five allowed provenance paths.
- Any attempt to repair the 19 cvf-web failures in this tranche.
- Any provider key, live test, public commit, or public push.
- Any public candidate containing a deferred/private artifact.

## Evidence / Verification

Required evidence is the focused mapper test, projection-policy JSON parse,
offline package-boundary Vitest, Guard Contract typecheck, exact changed-set
status, public-sync clean status, and worker-return fast gate. Full cvf-web
suite success is not an acceptance criterion; its known 19 failures are a stop
condition for any later broad public export.

## Claim Boundary

Projection safety and stale boundary-test remediation only. No application
runtime behavior, provider behavior, public export, production readiness,
governance-latency L0, downstream edit, or broad cvf-web repair is authorized.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this dispatch packet authorizes private provenance remediation only;
a later independently reviewed export batch must provide public commit evidence.
