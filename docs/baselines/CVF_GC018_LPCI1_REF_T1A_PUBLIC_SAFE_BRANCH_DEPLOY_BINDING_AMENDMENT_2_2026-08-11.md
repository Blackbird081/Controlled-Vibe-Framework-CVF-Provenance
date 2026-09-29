# CVF GC-018 Baseline - LPCI1-REF T1A Public-Safe Branch Deploy Binding Amendment 2

Memory class: governed-dispatch-baseline

Status: APPROVED_FOR_EXECUTION

Date: 2026-08-11

Batch ID: LPCI1-REF-T1A-PUBLIC-SAFE-BRANCH-DEPLOY-BINDING-AMENDMENT-2

Dispatch base head: `99a99ee2548f6ef76f18d014ac422abfbe7ff98c`

Public target head: `2103a38fda01ee827e9fc6c3be38a824fa5d54ad`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Authorize a source-first one-path test repair and exact same-path public mirror
without changing current release authorization behavior.

## Scope / Target / Owner Boundary

Worker may modify exactly one private source path and the identical public
candidate path, then create one private Amendment 2 return. Reviewer owns
acceptance and commits. All other tracked paths and external actions are out.

## Source / Predecessor Evidence

Amendment 2 source verification, committed Amendment 1 blocked return, exact
union-41 public candidate, and current route/policy/auth helper sources.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | exact paths, source-first order, no-commit boundary, public disposition |
| gateRunPurpose | confirm Amendment 2 baseline |
| claimBoundary | authority only |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| Union-41 bytes | 41/41 hashes; missing/extra/mismatch zero | SATISFIED |
| Offline dependency link | cvf-web TypeScript PASS without network | SATISFIED |
| Actual blocker | three focused failures isolated to one test | SATISFIED |
| Runtime policy | actual 403 is policy-correct and must remain unchanged | FROZEN |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI1-REF source-first route governance test repair`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Exact Repair Manifest

Private source owner:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.governance.test.ts`

Public mirror:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.governance.test.ts`

Private return:
`docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_2_WORKER_RETURN_2026-08-11.md`.

## Required Semantic Delta

- Import and use `deriveServiceTokenIdentity` and `digestReleaseIdentity`.
- In test setup, set `LPCI_QUERY_SERVICE_ACTOR_ALLOWLIST` to the digest of the
  derived `test-service-token` service actor.
- Delete that environment variable during teardown.
- Preserve all production route, policy, auth and union-41 files unchanged.
- After the private edit, copy identical bytes to the public same-path mirror.

## Forbidden Scope

Runtime route/policy/auth edits, assertion weakening to 403, path widening,
dependency/network installation, secrets, commit, push, deploy, browser,
provider/store, production, and public `main`.

## Verification Contract

Prove private/public repaired-path equality; public changed set remains exact
union 41; staging zero. Use an offline sibling junction when needed. Run the
focused 15-file set, Model Gateway full suite/typecheck, cvf-web typecheck,
scoped lint, production build, and `git diff --check`.

## Acceptance Criteria

1. One private source path changed; public remains exact union 41.
2. Repaired private/public path hashes match.
3. All required tests, types, lint, and build pass offline.
4. Both HEADs and staging indexes remain unchanged by worker.

## Decision / Baseline / Proposed Tranche

`APPROVED_FOR_EXECUTION`: one-path source-first test repair only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: independent acceptance and reviewer-owned commits are required.

## Claim Boundary

Passing proves a local deterministic candidate only, not public export,
Netlify, provider/store, hosted runtime, or production readiness.
