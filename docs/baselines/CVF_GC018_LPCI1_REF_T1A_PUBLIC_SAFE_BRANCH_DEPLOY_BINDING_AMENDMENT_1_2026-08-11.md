# CVF GC-018 Baseline - LPCI1-REF T1A Public-Safe Branch Deploy Binding Amendment 1

Memory class: governed-dispatch-baseline

Status: APPROVED_FOR_EXECUTION

Date: 2026-08-11

Batch ID: LPCI1-REF-T1A-PUBLIC-SAFE-BRANCH-DEPLOY-BINDING-AMENDMENT-1

Dispatch base head: `5d9a718032ed1ca3bfcae8f0287f549209157cf5`

Target base head: `2103a38fda01ee827e9fc6c3be38a824fa5d54ad`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Amend the blocked exact-23 projection into the exact transitive 41-path
accepted candidate by adding 18 prerequisite-lineage paths.

## Scope / Target / Owner Boundary

Target: the existing local `lpci1-ref-staging` worktree. The worker preserves
the inherited 23 byte-equal paths, projects the exact 18-path amendment from
`e82ab11dc`, and returns without commit. Reviewer owns acceptance and closure.

## Source / Predecessor Evidence

Canonical inputs are the Amendment 1 source verification, original GC-018
baseline, committed blocked worker return, accepted lineage commits
`db580830f`, `5c86f6d77`, `e82ab11dc`, and final byte tree `e82ab11dc`.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | approved status, exact delta, inherited changed set, no-commit boundary, public disposition |
| gateRunPurpose | confirm amendment baseline shape |
| claimBoundary | authority only; no candidate acceptance or external action |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| Inherited projection | committed blocked return plus fresh exact-23 status/hash verification | SATISFIED_PENDING_WORKER_REFRESH |
| Accepted transitive lineage | union of `EXTENSIONS/` changed sets at `db580830f`, `5c86f6d77`, `e82ab11dc` | SATISFIED |
| Final byte owner | `e82ab11dc0c3b7af46b330c6eedf10049231d7de` | SATISFIED |
| Public target | local branch HEAD remains `2103a38f...`, staging empty | SATISFIED |
| Push/deploy authority | excluded | DEFERRED_TO_LATER_REVIEWER_TRANCHE |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI1-REF public-safe prerequisite lineage amendment`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Inherited Exact 23-Path Manifest

The exact ordered manifest under `## Exact Public-Safe Projection Manifest` in
`docs/baselines/CVF_GC018_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_2026-08-11.md`
is incorporated without change. The worker must freshly prove all 23 paths
equal `e82ab11dc` before amendment and again in the final 41-path ledger.

## Exact 18-Path Amendment Manifest

1. `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts`
2. `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
3. `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`
4. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/credential-boundary.test.ts`
5. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/p4b-b-dry-run-gate.test.ts`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.test.tsx`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.governance.test.ts`
11. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.test.ts`
12. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.ts`
13. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.test.ts`
14. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts`
15. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/query-conformance.test.ts`
16. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/query-conformance.ts`
17. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.test.ts`
18. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts`

Final required public changed set: exact union of inherited 23 plus amendment
18, total 41, with no deletion or rename and staging index empty.

## Forbidden Scope

- Every public path outside the exact union 41 and every Core path except the
  Amendment 1 worker return.
- Manual redesign, source normalization, package-version authoring, dependency
  fetch, or network install. Exact package/lockfile byte projection is allowed.
- Secret reads; commit, tag, merge, push, pull request, Netlify action, browser
  smoke, provider/store request, rollback, production, or `main` change.

## Verification Contract

- Require inherited candidate branch/HEAD/status and exact 23-byte fidelity.
- Project exact 18 final bytes from `e82ab11dc`.
- Prove 41/41 source-target SHA-256 equality and exact changed-set union.
- Run Model Gateway tests/typecheck and cvf-web lineage/release tests,
  typecheck, scoped lint, and production build with installed offline tooling.
- If local dependency materialization requires network access, do not fetch;
  return a precise blocker after preserving exact repository bytes.

## Acceptance Criteria

1. Exact 41-path byte equality and zero manifest delta.
2. All required deterministic tests, typechecks, lint, and build pass.
3. No external action, secret read, repository commit, or staging mutation.
4. Amendment worker return passes its fast gate.

## Decision / Baseline / Proposed Tranche

`APPROVED_FOR_EXECUTION`: exact local no-commit repair only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: independent acceptance must precede any public commit or push.

## Claim Boundary

This baseline can authorize a locally buildable candidate; it cannot prove or
authorize Netlify, hosted, provider/store, public export, or production state.
