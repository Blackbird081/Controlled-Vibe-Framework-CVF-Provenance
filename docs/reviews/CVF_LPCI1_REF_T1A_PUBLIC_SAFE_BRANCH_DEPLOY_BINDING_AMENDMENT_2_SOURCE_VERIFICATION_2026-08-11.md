# CVF LPCI1-REF T1A Public-Safe Branch Deploy Binding Amendment 2 Source Verification

Memory class: FULL_RECORD

Status: ACCEPTED_FOR_DISPATCH

Date: 2026-08-11

docType: review

Batch ID: LPCI1-REF-T1A-PUBLIC-SAFE-BRANCH-DEPLOY-BINDING-AMENDMENT-2

## Purpose

Verify the single source-owned repair needed after Amendment 1 independent
review exposed stale route-governance test setup.

## Scope / Methodology

Read-only inspection of the committed blocker, route authorization flow,
release role policy, service-token identity helper, test setup, exact union-41
state, and offline deterministic commands. No secret or external action.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | concrete sources, dispatch status, exact ownership, trace, no-commit and public disposition |
| gateRunPurpose | confirm Amendment 2 source and packet shape |
| claimBoundary | local source verification only |

## Authority And Base

| Item | Evidence | Disposition |
| --- | --- | --- |
| Operator | delegated orchestrator/reviewer authority and `next` | ACCEPT |
| Core dispatch base | clean `main@99a99ee2548f6ef76f18d014ac422abfbe7ff98c` | ACCEPT |
| Amendment 1 blocker | `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_1_WORKER_RETURN_2026-08-11.md`; commit `7c0a1982b` | ACCEPT |
| Public candidate | exact union 41 at local `lpci1-ref-staging@2103a38f...`; staged zero | ACCEPT_FOR_REPAIR |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Three stale status assertions | TEST_CONTRACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.governance.test.ts` | validation cases at expectations 400 | `beforeEach`, `makeRequest`, three tests | route governance test owner | ACCEPT |
| Service requests require release allowlist | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | post-auth role decision | `parseLpciServiceActorAllowlist` call | LPCI query route | ACCEPT |
| Canonical allowlist value is a service identity digest | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/release-policy.ts` | service-token branch | `digestReleaseIdentity`, `evaluateReleaseRolePolicy` | release role policy | ACCEPT |
| Token maps to opaque service actor ID | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | identity helper | `deriveServiceTokenIdentity` | service-token auth | ACCEPT |
| Offline package link is sufficient | EXECUTION_EVIDENCE | `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_1_WORKER_RETURN_2026-08-11.md` | Tests And Build Evidence | cvf-web TypeScript PASS | committed independent review | ACCEPT |

## Current Runtime Freshness Verification

At public union 41, Model Gateway TypeScript and 30 files / 231 tests pass;
cvf-web TypeScript passes with a temporary offline sibling junction; focused
cvf-web tests pass 14 files / 215 tests and fail three assertions in only
`route.governance.test.ts`. Actual 403 matches current release policy; expected
400 requires the test service actor to be explicitly allowlisted.

## Exact Repair Decision

Modify only the private provenance copy of
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.governance.test.ts`
to derive the test service actor with `deriveServiceTokenIdentity`, digest it
with `digestReleaseIdentity('service', ...)`, set
`LPCI_QUERY_SERVICE_ACTOR_ALLOWLIST` in `beforeEach`, and delete it in
`afterEach`. Then copy that exact repaired byte to the same public candidate
path. Runtime route behavior must not change.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI1-REF source-first route governance test repair`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Findings / Position

The repair is test setup alignment, not a runtime-policy relaxation. One
source path and its same-path public mirror are sufficient.

## Risk / Corrective Action

Risk is accidentally weakening authorization or diverging source/public
bytes. Prohibit route/runtime edits; require focused negative/auth tests,
source-public hash equality, full mandatory checks, and independent review.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/reviewer |
| Provider or surface | private Core and read-only public-sync |
| Session or invocation | `lpci1-ref-t1a-amendment-2-source-verification-20260811` |
| Working directory | Core plus public-sync clone |
| Command or tool surface | local Git, source inspection, offline TypeScript/tests, authority authoring |
| Target paths | exact three Amendment 2 authority paths |
| Allowed scope source | delegated operator authority and committed blocker |
| Before status evidence | Core clean worktree at `99a99ee2548f6ef76f18d014ac422abfbe7ff98c`; public exact union 41, staged zero |
| After status evidence | authority pending commit; runtime/public bytes untouched |
| Diff evidence | `git diff --name-status` must show exact three authority files |
| Approval boundary | Amendment 2 dispatch only |
| Claim boundary | no implementation, commit of runtime, push, deploy, provider/store, or production action |
| Agent type | orchestrator/dispatcher/reviewer |
| Invocation ID | `lpci1-ref-t1a-amendment-2-source-verification-20260811` |
| Expected manifest | source verification, baseline, work order |
| Actual changed set | reviewer reconciles before authority commit |
| Manifest delta | must be zero |
| Deletion or rename disposition | N/A with reason: new authority files only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local one-path test-repair authority |
| claimDisposition | CLAIM_REJECTED: no repaired or hosted behavior claimed yet |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no hosted receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local deterministic failure and source inspection |
| invocationBoundary | zero runtime/public mutation, commit, push, deploy, provider/store, or production invocation |
| interceptionBoundary | local repositories only |
| claimLanguage | accepted for one-path source-first test repair dispatch |
| forbiddenExpansion | runtime policy changes, network fetch, push, deploy, secrets, provider/store, production, `main` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: source repair and independent review precede export.

## Claim Boundary

This verifies the repair design only; it proves no passing implementation,
public export, hosted deployment, external runtime, or production readiness.
