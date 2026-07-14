# CVF GC-018 System Chain UC-04B R2 Web Auth Projection Repair

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018_baseline

Date: 2026-07-14

Risk classification: R1

## Purpose

Authorize one bounded repair of the request-bound Web authentication projection
exposed by SCLP-UC04B-R1. This tranche repairs and proves authentication only;
it does not execute the UC-04B business job, a checker, or a provider.

## Proposed Tranche / Decision

Authorize `SCLP-UC04B-R2` for one no-commit worker. The worker may export the
existing shared auth secret, make `verifySessionCookie(request)` decode the
request token, extend focused unit tests, and add one protected proof-only E2E
spec. Reviewer/closer owns acceptance, closure, and commits.

## Design Control Gate

| Control | Decision |
|---|---|
| repair seam | NextAuth config plus request-bound middleware adapter |
| retained path | no-request `auth()` projection remains supported |
| positive actor | mock user `dev`, expected role `developer`, Operations projection `operator` |
| negative actor | fresh anonymous context, expected API 401 and page `anonymous_local` |
| proof source | new dedicated auth-projection regression spec |
| live ceiling | one Playwright command, zero business submissions/checkers/providers/retries |
| excluded proof | retained UC-04B business spec is not invoked |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| current middleware accepts but ignores request | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | `verifySessionCookie` | `verifySessionCookie` | Web session adapter | RUNTIME_BEHAVIOR | ACCEPT |
| current auth config owns fallback secret | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | NextAuth config secret field | `secret` | NextAuth configuration | VALUE_SET | ACCEPT |
| JWT callback owns projected identity and role claims | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | callbacks jwt block | `jwt` | NextAuth token callback | RUNTIME_BEHAVIOR | ACCEPT |
| installed request-token API accepts request and secret | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/node_modules/@auth/core/jwt.d.ts` | `GetTokenParams` and export declaration | `getToken` | Auth.js JWT API | EXISTS | ACCEPT |
| request-token runtime rejects missing request or secret | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/node_modules/@auth/core/jwt.js` | `getToken` | `getToken` | Auth.js JWT runtime | RUNTIME_BEHAVIOR | ACCEPT |
| installed dependency is NextAuth v5 beta line | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies | `next-auth` | Web dependency manifest | VALUE_SET | ACCEPT |
| focused tests currently cover only auth-context projection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.test.ts` | `verifySessionCookie` describe block | `verifySessionCookie` | middleware auth test owner | EXISTS | ACCEPT |
| R1 observed session/application projection split | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R1_WEB_AUTH_AND_READOUT_RECOVERY_COMPLETION_2026-07-14.md` | final disposition and findings | `CLOSED_BLOCKED_BOUNDED` | reviewer closure | VALUE_SET | ACCEPT |
| architecture GAP records the same owner seam | `docs/reference/system_chain/gaps/entries/web_nextauth_application_projection_split.json` | gap record | `cvf.asc.gap.web_nextauth_application_projection_split.v1` | system-chain GAP registry | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

Fresh reads at dispatch base `76f70a13b` confirm all accepted facts. The worker
must refresh them before editing. A dependency-contract contradiction or need
to change the auth route, jobs route, Operations page, or business proof stops
the tranche.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| R1 bounded blocker accepted | material closure commit `eebc3f8ce` | SATISFIED |
| repair packet is current next move | session commit `76f70a13b` | SATISFIED |
| architecture owner gap registered | governed GAP entry at dispatch base | SATISFIED |
| dispatch start clean | empty status at `76f70a13b` | SATISFIED |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | R2 control | Evidence | Disposition |
|---|---|---|---|
| repair real auth boundary | request-bound token projection | focused tests | READY |
| prove positive application projection | direct credentials session plus `/api/auth/me` and Operations | one E2E case | READY |
| retain negative boundary | anonymous API and Operations assertions | one E2E case | READY |
| prevent value/cost drift | one immutable invocation ledger | exact zero business counters | READY |
| keep UC-04B claim stale | business spec excluded | reviewer closure | READY |

## Core Guard Self-Protection Authorization

Protected path authorized:
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts`.

Operator authorization: the operator said `tiep tuc` after accepting the R1
bounded blocker and its source-backed repair route.

Rollback boundary: revert only the R2 auth-owner, focused-test, proof-spec, and
dated evidence batch if rejected. Do not revert R1 closure or session commits.

Not authorized: checker/hook changes, business-job execution, provider calls,
public sync, production claim, or mutation outside the R2 manifest.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Web auth runtime repair`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cvf-web`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Web auth runtime repair" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --max-results 20 --json`

Returned defects: ADIF-0033

Directly applicable governed defects: `CVF_ADIF-0033`; `CVF_ADIF-0034`.

Resolver returned zero candidates; ADIF-0033 is disclosed because the exact
new E2E path is protected, and ADIF-0034 controls the live invocation ledger.

## Cost And Retry Control

One Playwright command, zero business submissions, zero checker executions,
zero provider calls, and zero retries. Any failure produces one diagnostic and
stops. Unit-test commands before the ledger are not live invocations.

## Acceptance Criteria

- Request-bound identity is decoded from the supplied request, not ambient context.
- No-request behavior and impersonation overlay remain covered.
- Positive direct session, `/api/auth/me`, and Operations role projections agree.
- Anonymous API and Operations projections remain denied/local-anonymous.
- One command and exact zero business/checker/provider/retry counters reconcile.
- No UC-04B business proof or coverage promotion is claimed.

## Evidence / Verification

Required evidence includes execution base, source refresh, focused tests,
frozen proof hash, monotonic invocation ledger, exact command fingerprint,
two stable cases, projection assertions, zero counters, conditional diagnostic,
secret scan, exact diff/status/stage evidence, and unchanged worker HEAD.

## Fail Conditions

Source contradiction, focused-test failure, second Playwright command, proof
edit after ledger start, incorrect projection, nonzero business/checker/provider
counter, retry, secret leak, unexpected file, commit, or stronger claim blocks.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair packet; no public-sync scope.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Dependency Release Evidence`; `Core Guard Self-Protection Authorization`; `Public Export Disposition` |
| gateRunPurpose | confirmation after source inventory, not first discovery |
| claimBoundary | dispatch authorization only; no repair or Web invocation in this batch |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id SCLP-UC04B-R2 --title "System Chain UC-04B R2 Web Auth Projection Repair" --date 2026-07-14 --base 76f70a13b --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | Web/UI plus no-commit worker dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-backed auth repair, protected-path, live-cost, and closure controls |
| checkerReadAheadConfirmation | guard orientation, literal gotchas, and applicable checker contracts read |
| docOnlyNewFields | dated invocation ledger and regression receipt fields only |
| claimBoundary | packet authorization only |

## Claim Boundary

This baseline authorizes one local auth-projection repair and one bounded real
Next development regression command. It does not prove the UC-04B business
chain, all authentication paths, provider governance, production, public
readiness, scale, certification, or user value.

