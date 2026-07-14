# CVF Agent Work Order - System Chain UC-04B R2 Web Auth Projection Repair

Memory class: FULL_RECORD

Status: DISPATCH_READY

Work Order ID: SCLP-UC04B-R2

Date: 2026-07-14

dispatchBaseHead: `76f70a13b`

Execution mode: WORKER_MUST_NOT_COMMIT

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

```text
Role: worker/implementer. Codex is reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_2026-07-14.md.
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: capture executionBaseHead and require a clean worktree.
Current-time notes: repair the request-bound auth projection only; no provider key or business job is needed.
Do-not-misread notes: this is not a UC-04B business proof rerun. Run focused tests, freeze the dedicated regression spec, then invoke Playwright exactly once with zero retries.
Required first actions: read startup/guard sources, paired GC-018, ADIF-0033/0034, auth owners and dependency contract, then run pre-implementation.
Return contract: COMPLETE_PENDING_REVIEW only with reconciled ledger/receipt and all ACs; otherwise BLOCKED_WITH_REASON with one secret-safe diagnostic. Never commit.
```

## Purpose

Repair and prove the request-bound Web authentication projection exposed by
R1 without consuming the UC-04B business-chain proof budget.

## Objective

Make `verifySessionCookie(request)` use the supplied request token while
preserving ambient no-request behavior and impersonation. Prove agreement
between direct NextAuth session, `/api/auth/me`, and the Operations page for
the developer actor, plus the existing anonymous denial boundary.

## Authority Chain

Operator continuation -> system-chain roadmap -> R1 bounded blocker closure ->
paired R2 GC-018 -> this work order. Current runtime source and machine gates
control.

## Agent Roles

| Role | Ownership |
|---|---|
| dispatcher | source verification, repair boundary, dispatch gates |
| worker | exact runtime/test repair, one auth regression invocation, evidence, no-commit return |
| reviewer/closer | independent review, closure, reverse projection, commits |

## Scope

Worker may edit exactly two auth runtime owners, one focused unit-test owner,
and one new proof-only E2E spec, then create the declared evidence and return.
Auth routes, job owners/routes, Operations page, retained business spec,
roadmaps, registries, session, public surfaces, and providers are read-only.

## Required First Reads

1. Startup front doors, active handoff, guard orientation, literal gotchas.
2. Paired R2 GC-018, this work order, ADIF-0033, ADIF-0034, and Live Run Diagnostic Standard.
3. Root `DESIGN.md`, auth config, middleware adapter/tests, `/api/auth/me`, Operations page, Playwright config, and installed Auth.js JWT contract.
4. R1 completion and registered auth-projection GAP.

## Pre-Flight Checks

- Capture `executionBaseHead`; require empty `git status --short`.
- Refresh every Source Verification ACCEPT fact.
- Run pre-implementation autorun before implementation.
- Confirm dependency files exist without modifying `node_modules`.
- Confirm `.env.local` existence secret-safely; never print values.
- Run focused unit tests before freezing the E2E proof source.
- Confirm tracked `test-results/.last-run.json` baseline for later restoration.

## Write Ownership

The worker owns only the exact Planned Worker Fulfillment Manifest. Playwright
output, Next build state, cookies, traces, screenshots, environment files,
runtime audit files, `node_modules`, and `test-results/.last-run.json` are
runtime inputs or disposable outputs and must not be staged. Reviewer/closer
owns the completion review, baseline/work-order status conversion, architecture
projection, session updates, and all commits.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| middleware request is currently ignored | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | `verifySessionCookie` | `verifySessionCookie` | Web session adapter | RUNTIME_BEHAVIOR | ACCEPT |
| auth config owns the fallback secret | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | NextAuth config secret field | `secret` | NextAuth configuration | VALUE_SET | ACCEPT |
| JWT callback owns role and identity claims | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | callbacks jwt block | `jwt` | NextAuth token callback | RUNTIME_BEHAVIOR | ACCEPT |
| session callback projects role and identity | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | callbacks session block | `session` | NextAuth session callback | RUNTIME_BEHAVIOR | ACCEPT |
| request token API accepts request and explicit secret | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/node_modules/@auth/core/jwt.d.ts` | `GetTokenParams` and declaration | `getToken` | Auth.js JWT API | EXISTS | ACCEPT |
| request token runtime enforces request and secret | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/node_modules/@auth/core/jwt.js` | `getToken` | `getToken` | Auth.js JWT runtime | RUNTIME_BEHAVIOR | ACCEPT |
| focused owner tests exist | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.test.ts` | `verifySessionCookie` describe block | `verifySessionCookie` | middleware auth tests | EXISTS | ACCEPT |
| direct credentials helper proves CSRF/callback/session | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts` | `signInViaNextAuth` | `signInViaNextAuth` | E2E auth helper | RUNTIME_BEHAVIOR | ACCEPT |
| auth-me route consumes request-bound verification | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/auth/me/route.ts` | GET handler | `GET` | auth-me API route | RUNTIME_BEHAVIOR | ACCEPT |
| R1 closure records direct-session/application split | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R1_WEB_AUTH_AND_READOUT_RECOVERY_COMPLETION_2026-07-14.md` | findings | `CLOSED_BLOCKED_BOUNDED` | reviewer closure | VALUE_SET | ACCEPT |
| GAP record owns repair route | `docs/reference/system_chain/gaps/entries/web_nextauth_application_projection_split.json` | gap record | `cvf.asc.gap.web_nextauth_application_projection_split.v1` | system-chain GAP registry | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

Refresh all accepted facts before editing. If the request-token API cannot
preserve the configured claims, if focused owners disagree with the packet,
or if a read-only owner must change, return `BLOCKED_WITH_REASON` before the
live ledger starts.

## Execution Plan

1. Capture clean execution base and run source/environment preflight.
2. In `src/auth.ts`, export one shared `authSecret` constant from the current
   secret expression and use it in the existing NextAuth config. Do not alter
   credential, JWT, or session semantics.
3. In `src/lib/middleware-auth.ts`, when a request is supplied, call the public
   `getToken` API with that request and `authSecret`; map its existing identity,
   role, organization, team, and expiry claims into `SessionCookie`. When no
   request is supplied, retain current `auth()` behavior. Retain impersonation
   overlay for the supplied request.
4. Extend focused tests so request-supplied behavior calls `getToken` rather
   than `auth`, maps claims and expiry, returns null for a null token, and
   retains no-request and impersonation behavior.
5. Add a serial, proof-only E2E spec with stable cases
   `positive_developer_auth_projection` and
   `negative_anonymous_auth_projection`. Use direct CSRF/credentials/session
   authentication. Positive asserts session role developer, `/api/auth/me`
   authenticated developer, and Operations active role operator. Negative
   asserts `/api/auth/me` 401 and Operations `anonymous_local`.
6. Ensure the spec never POSTs `/api/system/jobs`, invokes a checker, or calls
   a provider. Compute its SHA-256 and create the invocation ledger before the
   live command. Set `invocationStarted=1` immediately before process spawn.
7. Run the exact Playwright command once. Freeze proof and receipt logic after
   ledger start. On failure, write one diagnostic and stop without retry.
8. Reconcile receipt, ledger, zero counters, proof hash, cases, exact changed
   set, tracked runtime artifacts, stage state, and unchanged HEAD. Scaffold
   and gate the no-commit worker return.

## Planned Worker Fulfillment Manifest

| Path | Ownership | Required disposition |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | worker runtime | shared secret export only |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | worker runtime | request-bound token repair |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.test.ts` | worker test | focused regression coverage |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts` | worker proof-only | dedicated two-case regression |
| `docs/reviews/evidence/system-chain-uc04b-r2-auth-projection-invocation-ledger-2026-07-14.json` | worker | monotonic one-invocation ledger |
| `docs/reviews/evidence/system-chain-uc04b-r2-auth-projection-regression-2026-07-14.json` | worker | reconciled receipt |
| `docs/reviews/evidence/system-chain-uc04b-r2-auth-projection-diagnostic-2026-07-14.json` | worker conditional | required only on non-PASS |
| `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_WORKER_RETURN_2026-07-14.md` | worker | no-commit return |

## Core Guard Self-Protection Authorization

Protected path authorized:
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts`.

Operator authorization: the operator said `tiep tuc` after R1 closure routed
this exact bounded repair packet next.

Rollback boundary: only the R2 manifest and reviewer-owned R2 closure surfaces.

Not authorized: checker/hook changes, retained business-spec execution,
provider calls, public sync, or unrelated protected-path mutation.

## Invocation Ledger Contract

The ledger must exist before the Playwright command and contain execution base,
command fingerprint, frozen spec path/hash, ceiling 1, monotonic
`invocationStarted`, timestamps, result, both case IDs, and counters for
business submissions, checker executions, retries, and provider calls. All
four counters must remain zero. Receipt, diagnostic, return, and runtime facts
must reconcile with the same ledger.

## Evidence Requirements

Record clean start, source refresh, focused tests, secret-safe environment
existence, frozen proof hash, ledger, command fingerprint, real Next dev mode,
stable cases, direct/API/page projections, exact zero counters, conditional
diagnostic, secret scan, diff/status/stage evidence, and unchanged HEAD. Never
retain passwords, cookies, tokens, raw environment values, or API keys.

## Acceptance Criteria

- AC-01: all source facts and focused unit tests pass before ledger start.
- AC-02: request-supplied verification uses request token; no-request behavior remains.
- AC-03: identity, role, organization, team, expiry, null token, and impersonation tests pass.
- AC-04: proof hash is identical in ledger, receipt, and final spec.
- AC-05: exactly one Playwright invocation runs the two stable cases.
- AC-06: developer direct session, auth-me, and Operations projections agree.
- AC-07: anonymous auth-me and Operations projections remain denied/anonymous.
- AC-08: business submissions, checkers, retries, and provider calls all equal zero.
- AC-09: exact manifest only; tracked runtime artifacts restored; nothing staged.
- AC-10: worker HEAD remains execution base and worker makes no commit.

## Fail Conditions

Dirty start, source contradiction, read-only-owner need, failed focused test,
proof change after ledger start, second Playwright command, wrong projection,
nonzero business/checker/retry/provider counter, secret leak, unexpected file,
staged change, commit, or business-chain promotion returns
`BLOCKED_WITH_REASON` and stops.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with all ACs evidenced. Otherwise return
`BLOCKED_WITH_REASON`, one diagnostic, retryability false for this packet, and
the smallest source-backed reviewer action. Do not ask for a rerun.

## Operator Checkpoint

No checkpoint is parked. Canonical local mock credentials may be used. No
external provider key or business execution is authorized.

## Closure Checklist

| Item | Disposition |
|---|---|
| source refresh and focused tests | worker evidence required |
| request/no-request projection repair | worker evidence required |
| immutable ledger and frozen hash | worker evidence required |
| one command and two stable cases | worker evidence required |
| exact zero business-cost counters | worker evidence required |
| exact changed set and unchanged HEAD | worker evidence required |
| architecture GAP and roadmap decision | reviewer-owned |
| separate future UC-04B business proof | not authorized in R2 |

## Worker Autonomy / No-Question Rule

Proceed inside the exact manifest. Before ledger start, in-scope repair and
focused-test reruns are allowed. After ledger start, no source repair or live
rerun is authorized. Any forbidden-scope need stops the tranche.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Evidence | Status |
|---|---|---|---|
| repair real auth seam | request-token adapter | focused unit tests | READY |
| prove positive projection | direct/API/page assertions | E2E receipt | READY |
| retain negative boundary | anonymous API/page case | E2E receipt | READY |
| bound live cost | immutable ledger | 1/0/0/0/0 counters | READY |
| avoid false UC-04B closure | business spec forbidden | reviewer decision | READY |

## Cost And Retry Control

Authorized totals: Playwright invocations 1; business submissions 0; checker
executions 0; retries 0; provider/API/MCP calls 0. Web auth/API requests inside
the two cases are allowed and must not be miscounted as business submissions.

## Agent Handoff Contract Control Block

Contract stable front door: `docs/reference/agent_handoff/README.md`.

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit repair worker, then reviewer/closer |
| phase | UC-04B R2 auth-owner repair, one regression command, receipt, return |
| baseHeadFor(phase) | dispatchBaseHead=`76f70a13b`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | exact Planned Worker Fulfillment Manifest |
| traceScope(phase, actor) | worker records source/test/hash/ledger/invocation/cases/counters/diff/HEAD; reviewer owns closure |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns material commit |
| crossBatchIsolation | CLEAN_WORKTREE_CONFIRMED at dispatch; non-manifest surfaces read-only |
| nextMoveSurfaces | reviewer updates closure, reverse projection, and session only after review |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_COMPLETION_2026-07-14.md` |
| reviewerOwnedClosurePaths | completion; paired baseline/work order; GAP/coverage/roadmap decision; active session sources |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return and evidence, read checker source for each
path family and conditional content class. Derive exact review headings,
worker-return terms, trace labels, delta labels, and no-commit evidence shape.
Do not list heading-shaped checklist literals before their real sections.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_WORKER_RETURN_2026-07-14.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Skeleton command: `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_WORKER_RETURN_2026-07-14.md --title "CVF System Chain UC-04B R2 Web Auth Projection Repair Worker Return" --profile WORKER_RETURN_FULL_GATE_V1`

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake route | operator continuation of accepted R1 architecture blocker |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| Selected role route | dispatcher -> no-commit worker -> reviewer/closer |
| scope classification | bounded local Web auth runtime repair |
| risk sensitivity | R1 provider-free development runtime |
| escalation condition | any fail condition |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current local source plus bounded real Web regression |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | Web auth adapter and system-chain GAP registry |
| Disposition | BLOCKED_UNTIL_CVF_PROOF |
| Claim boundary | source and R1 diagnosis are not R2 runtime proof |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: internal Web auth repair; no legacy corpus intake.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R1 proved the split but did not repair or pass the application projection

priorVerificationArtifact: `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R1_WEB_AUTH_AND_READOUT_RECOVERY_COMPLETION_2026-07-14.md`

priorVerificationAnchor: blocker and owner diagnosis only; no PASS reuse

freshRecomputeRequired: yes, under fresh R2 authority

unicodePathHandling: literal repository paths and explicit UTF-8 readers; new governed prose is ASCII

extractedTextAuthority: N/A with reason: no OCR or extracted external input

## Provider Memory Authority Boundary

Provider memory and chat are not authority. Executable facts must be refreshed
from governed source, installed dependency contract, and retained evidence.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | one local request-bound Web auth repair and regression |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT only through R2 ledger and receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT only if the one-command projection regression passes |
| invocationBoundary | one Playwright command; zero business/checker/retry/provider calls |
| interceptionBoundary | no IDE, shell, git, provider, MCP, public, production, or universal interception claim |
| claimLanguage | selected local auth projections agreed as recorded in one evidence window |
| forbiddenExpansion | no UC-04B business, all-auth, provider, production, public, scale, certification, or user-value claim |

## Verification Commands

```text
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx vitest run src/lib/middleware-auth.test.ts src/app/api/auth/me/route.test.ts --reporter=verbose
npx playwright test tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts --config playwright.config.ts --workers=1
cd ../../../..
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce
git diff --check
git status --short
```

The Playwright line is the sole live invocation. Never repeat it.

## Review Gate

Reviewer independently checks source contract, runtime diff, focused tests,
proof hash, ledger monotonicity, one invocation, two cases, projection
agreement, zero counters, diagnostic accuracy, exact changed set, protected
authorization, runtime hygiene, and unchanged worker HEAD.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Web auth runtime repair`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cvf-web`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Web auth runtime repair" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --max-results 20 --json`

Returned defects: ADIF-0033

Directly applicable governed defects: `CVF_ADIF-0033`; `CVF_ADIF-0034`.

Resolver returned zero candidates; protected-path and invocation-ledger defects
remain explicitly applied from the governed registry.

## Commit Prompt Readiness

| Field | Value |
|---|---|
| workerCommitPrompt | FORBIDDEN |
| reviewerMaterialCommit | only after accepted review |
| sessionSyncCommit | separate after material decision |
| changedSetEvidence | exact manifest plus diff/status/stage evidence |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id SCLP-UC04B-R2 --title "System Chain UC-04B R2 Web Auth Projection Repair" --date 2026-07-14 --base 76f70a13b --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | Web/UI plus no-commit worker dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-backed repair, manifest, protected path, ledger, and closure controls |
| checkerReadAheadConfirmation | applicable checker sources and literal gotchas read |
| docOnlyNewFields | dated auth regression ledger and receipt fields |
| claimBoundary | dispatch packet only |

## Foundation Storage Layout Block

Existing auth runtime files remain owners. The new E2E file is proof-only and
dated evidence remains under reviews. No new stable API, schema, provider,
MCP, public, or production surface is added.

## UI / Web Design Control Block

| Field | Value |
|---|---|
| canonicalDesignSource | `DESIGN.md` |
| designMutation | FORBIDDEN |
| visualProofScope | existing Operations active-role readout only |
| accessibilityInteraction | role/name locators and visible assertions |
| responsiveOrBrandClaim | N/A with reason: no redesign or viewport claim |
| evidenceBoundary | auth projection behavior only, not general visual quality |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Source Verification Block`; `Planned Worker Fulfillment Manifest`; `Core Guard Self-Protection Authorization`; `Agent Handoff Contract Control Block`; `Public Export Disposition` |
| gateRunPurpose | confirmation after complete source and evidence inventory |
| claimBoundary | no-commit provider-free local Web auth repair |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair packet; no public-sync authority.

## Claim Boundary

A PASS proves only one request-bound local Web authentication projection for
one developer and one anonymous context in one development evidence window.
It does not prove the UC-04B business chain, all authentication paths,
provider governance, production, public readiness, scale, certification, or
user value.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer |
| Provider or surface | private provenance repository |
| Session or invocation | SCLP-UC04B-R2 packet authoring, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, scaffold, apply_patch, resolver, dispatch gates |
| Target paths | paired R2 baseline and work order |
| Allowed scope source | active nextAllowedMove at `76f70a13b` |
| Before status evidence | clean worktree at `76f70a13b` |
| After status evidence | source-verified auth-projection repair dispatch packet |
| Diff evidence | two-file dispatch diff before commit |
| Approval boundary | packet authoring and one later no-commit worker |
| Claim boundary | no repair, Web invocation, provider, public, or reverse projection in authoring batch |
| Agent type | dispatcher/reviewer |
| Invocation ID | `system-chain-uc04b-r2-dispatch-2026-07-14` |
| Expected manifest | paired R2 baseline and work order |
| Actual changed set | paired R2 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
