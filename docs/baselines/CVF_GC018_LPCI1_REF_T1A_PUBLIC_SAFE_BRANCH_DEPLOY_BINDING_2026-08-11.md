# CVF GC-018 Baseline - LPCI1-REF T1A Public-Safe Branch Deploy Binding

Memory class: governed-dispatch-baseline

Status: APPROVED_FOR_EXECUTION

Date: 2026-08-11

Batch ID: LPCI1-REF-T1A-PUBLIC-SAFE-BRANCH-DEPLOY-BINDING

Dispatch base head: `a2687471b8869dc6391273aa442b012fd287970b`

Target base head: `2103a38fda01ee827e9fc6c3be38a824fa5d54ad`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Authorize an exact, reviewable public-safe projection of the accepted LPCI1
runtime onto a local public-sync staging branch. This baseline does not
authorize push, deploy, live proof, provider use, or production mutation.

## Scope / Target / Owner Boundary

Target: exact 23-path local projection in the public-sync clone. The delegated
worker owns uncommitted preparation; the independent reviewer owns acceptance,
commit, and any later push. Production and external runtime actions are out of
scope.

## Source / Predecessor Evidence

The paired source-verification review, accepted release-hardening completion,
private material commit `e82ab11dc`, public base `2103a38f...`, and operator
Netlify Save confirmation are the complete predecessor set.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch status, exact manifest, no-commit boundary, public disposition, and claim tokens |
| gateRunPurpose | confirm dispatch baseline after authoring |
| claimBoundary | authority definition only; no public or hosted action |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| Deterministic LPCI1 hardening | accepted material commit `e82ab11dc` and accepted completion review | SATISFIED |
| Public-sync clone | clean `main@2103a38fda01ee827e9fc6c3be38a824fa5d54ad` with correct public remote | SATISFIED |
| Netlify branch context | operator saved `lpci1-ref-staging` as an additional branch deploy | SATISFIED_AS_OPERATOR_EXTERNAL_STATE |
| Push/deploy authority | deliberately excluded from this worker tranche | DEFERRED_TO_REVIEWER |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI1-REF public-safe branch deploy binding`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Exact Public-Safe Projection Manifest

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.test.ts`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-policy.ts`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-policy.test.ts`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-audit.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-audit.test.ts`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-health.ts`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-health.test.ts`
11. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts`
12. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.test.ts`
13. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/system-health.ts`
14. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/system-health.test.ts`
15. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.example`
16. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts`
17. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.test.ts`
18. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts`
19. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.test.ts`
20. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts`
21. `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts`
22. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-execution-bridge.test.ts`
23. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts`

Worker return path in private Core:
`docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_WORKER_RETURN_2026-08-11.md`.

## Forbidden Scope

- `docs/guides/CVF_LPCI1_WEB_UC01_RELEASE_OPERATIONS_RUNBOOK.md` and every
  other private governance, session, review, baseline, work-order, secret, or
  private-reference path.
- Package/dependency/lockfile mutation.
- Reading `.env`, `.env.local`, Netlify secrets, or any real credential value.
- Commit, tag, merge, push, pull request, Netlify trigger, browser smoke,
  provider/API request, Redis request, rollback, production, or `main` change.
- Any file outside the exact 23 public paths plus the one private worker return.

## Verification Contract

- Target branch is local `lpci1-ref-staging`, created from exact public target
  base if absent; an existing conflicting branch is a stop condition.
- Every projected target byte must equal `e82ab11dc:<path>` from private Core.
- Run Model Gateway focused tests and TypeScript check.
- Run cvf-web exact LPCI1/release suites, TypeScript, scoped lint, and build.
- Reconcile expected 23 public changes plus one private return; staging empty;
  both repository HEADs unchanged.

## Acceptance Criteria

1. Exact 23-path byte equality against the accepted material tree.
2. No unexpected public path and no public governance/private artifact.
3. All deterministic tests, typechecks, lint, and build pass.
4. No secrets, external runtime request, commit, push, or deployment occurs.
5. Worker return states `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Decision / Baseline / Proposed Tranche

`APPROVED_FOR_EXECUTION`: exact local staging preparation only, with all
commit, push, deploy, live, provider, store, and production effects deferred.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: staging content is only prepared locally; reviewer acceptance and a
separate reviewer-owned push are required before branch deployment.

## Claim Boundary

Passing this baseline proves only local byte projection and deterministic
verification. It proves no hosted endpoint, external store, provider, Netlify
deployment, public availability, or production readiness.
