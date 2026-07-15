# CVF Agent Work Order - System Chain UC-04B R3R2 Reviewer Auth Projection Repair

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-15

Work Order ID: `SCLP-UC04B-R3R2`

dispatchBaseHead: `a06265e49`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC04B_R3R2_REVIEWER_AUTH_PROJECTION_REPAIR_2026-07-15.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: R3R1 closed blocked at `0856e090d`; session routing is
anchored at `8785005e5`. Browser and business execution remain unauthorized.

Do-not-misread notes: implement only the server initial projection, extracted
client component, and deterministic tests. Do not run Playwright, submit a Web
job, edit the retained proof, or tune timeouts.

Required first actions: read the companion baseline, R3R1 completion, reopened
GAP, ADIF-0034 through ADIF-0037, current source/test, `DESIGN.md`, guard
orientation, and literal gotchas; then run the stated pre-implementation gate.

Return contract: `COMPLETE_PENDING_REVIEW` only with executionBaseHead, exact
four-path manifest, 34/34 focused PASS, typecheck PASS, zero live counters,
unstaged status, and unchanged HEAD; otherwise `BLOCKED_WITH_REASON`.

## Purpose

Implement the bounded server-to-client reviewer projection repair and prove it
with deterministic local tests before any new UC-04B browser business run.

## Target / Source

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC04B_R3R2_REVIEWER_AUTH_PROJECTION_REPAIR_2026-07-15.md`.

Companion baseline:
`docs/baselines/CVF_GC018_SYSTEM_CHAIN_UC04B_R3R2_REVIEWER_AUTH_PROJECTION_REPAIR_2026-07-15.md`.

## Authority Chain

Operator continuation -> active handoff V44 -> R3R1 completion/GAP reopen ->
R3R2 GC-018 -> this work order -> no-commit worker -> reviewer/closer.

## Agent Roles

- Dispatcher: owns source fidelity, allowed scope, and dispatch commit.
- Worker: owns only the fulfillment manifest and must not commit.
- Reviewer/closer: reconciles tests/diff and owns material closure.
- Session-sync steward: updates continuity only after material closure.

## Required First Reads

Read the companion baseline, R3R1 completion, reopened GAP entry, ADIF-0034
through ADIF-0037, current Operations page/test, ambient session adapter,
auth-me route, root `DESIGN.md`, guard orientation, and literal gotchas before
editing.

## Scope / Target / Owner Boundary

Writable paths are exactly the three source/test paths in the fulfillment
manifest plus the worker return. The retained R3R1 proof, auth API and adapter,
shell hook, job route/runtime, audit store, checker owners, GAP/roadmap, session,
and public surfaces are read-only.

## Source Inventory

1. R3R2 GC-018 baseline.
2. R3R1 completion and diagnostic.
3. Reopened auth-projection GAP entry.
4. ADIF-0034 through ADIF-0037.
5. Current Operations page and page test.
6. `middleware-auth.ts`, `/api/auth/me`, `ClientProviders.tsx`, and shell
   `useAuth.ts` as read-only projection inventory.
7. Root `DESIGN.md`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| current page owns all client logic | `canonical-contract:cvf-web-operations-page-source` | line 1; lines 127-160 | `GovernanceOperationsPage` | App Router page | EXISTS | ACCEPT |
| current initial role is anonymous | `canonical-contract:cvf-web-operations-page-source` | line 128 | `role` | component state | VALUE_SET | ACCEPT |
| current client refresh endpoint | `canonical-contract:cvf-web-operations-page-source` | line 152 | `/api/auth/me` | mount effect | LITERAL_INVARIANT | ACCEPT |
| ambient server session resolution exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | lines 96-122 | `verifySessionCookie` | session adapter | RUNTIME_BEHAVIOR | ACCEPT |
| role response fields exist | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/auth/me/route.ts` | `GET` response | `role`; `user`; `authenticated` | auth API | EXISTS | ACCEPT |
| existing client tests mock auth and jobs | `canonical-contract:cvf-web-operations-page-test-source` | `setupFetch`; suite | `fetchMock` | focused component test | EXISTS | ACCEPT |
| direct session and Operations diverged | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3R1_NEGATIVE_LOCATOR_RECOVERY_COMPLETION_2026-07-15.md` | Findings / Position | `SCLP-UC04B-R3R1` | reviewer closure | VALUE_SET | ACCEPT |
| next action requires deterministic regression | `docs/reference/system_chain/gaps/entries/web_nextauth_application_projection_split.json` | `actionOwner`; `closeCondition` | `cvf.asc.gap.web_nextauth_application_projection_split.v1` | GAP registry | VALUE_SET | ACCEPT |

## New Doc-Only Fields

| Field | Owner after implementation | Meaning |
|---|---|---|
| `initialRole` | new `OperationsClient` props | raw ambient session role used for initial mapped Operations state |
| `initialUser` | new `OperationsClient` props | ambient display identity used before client refresh |

## Current Runtime Freshness Verification

Fresh inspection at `a06265e49` confirmed all Source Verification rows. The
current provider registry exists at
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` with
`PROVIDER_CAPABILITY_REGISTRY`; it is read-only and irrelevant to this
provider-free projection repair. No provider-registry absence or hardcoded
provider claim is made. R3R1 trace evidence is retained without rerun.

## Pre-Flight Checks

Before edits:

```powershell
git rev-parse HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base a06265e49 --head HEAD
```

Require HEAD ancestry at or after `a06265e49`, clean status, and PASS. Re-read
all source-verification owners. Stop on contradiction.

## Execution Instructions

1. Capture `executionBaseHead`, clean status, and relevant source snippets.
2. Create `OperationsClient.tsx` beside the current page. Move the current
   client implementation into it without visual, job, audit, role-mapping, or
   copy changes. Export it with optional `initialRole` and `initialUser` props.
3. Initialize role with the existing `mapRole(initialRole)` behavior and user
   with `initialUser` or the current local fallback. Retain the existing mount
   `/api/auth/me` fetch and jobs load as a refresh path.
4. Replace `page.tsx` with an async server wrapper. Call ambient
   `verifySessionCookie()` with no request argument and pass `session?.role`
   and `session?.user` to `OperationsClient`. An unauthenticated null session
   must preserve anonymous-local behavior.
5. Update `page.test.tsx` without removing its three existing behavior cases.
   Add exactly two deterministic cases:
   - server wrapper passes reviewer role/user from mocked ambient session;
   - client renders reviewer before a deferred auth refresh resolves and the
     fetch ledger contains `/api/auth/me`.
6. Run the exact five-file focused suite from the Web package and require
   34/34 PASS:
   `npx vitest run "src/app/(dashboard)/governance/operations/page.test.tsx" src/app/api/system/jobs/route.test.ts src/lib/server/web-governance-jobs.test.ts src/lib/middleware-auth.test.ts src/app/api/auth/me/route.test.ts --reporter=dot`.
7. Run `npx tsc --noEmit` and require PASS.
8. Confirm zero diff in the retained proof spec and every read-only owner.
9. Create the no-commit worker return, run worker-return fast and commit-steward
   reviewer-return preflight, then leave all files unstaged.

## Planned Worker Fulfillment Manifest

| Path | Ownership | Required disposition |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/operations/page.tsx` | worker | async ambient-session wrapper only |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/operations/OperationsClient.tsx` | worker | extracted client implementation with two initial props |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/operations/page.test.tsx` | worker | retain three cases and add exactly two projection cases |
| `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3R2_REVIEWER_AUTH_PROJECTION_REPAIR_WORKER_RETURN_2026-07-15.md` | worker | no-commit return |

## Write Ownership

The worker may write only the four manifest paths above. New imports inside
those files may reference current read-only owners. Any required mutation to an
auth API, session adapter, shell hook, job route, proof spec, config, checker,
roadmap, GAP, or session surface returns to the orchestrator.

## Evidence Requirements

Return source snippets for server call/props, client initialization/refresh,
test names, focused 34/34 output, typecheck, proof-spec zero diff, exact command
ledger, actual changed set, unstaged status, and unchanged HEAD. Browser,
business, checker-job, retry, and provider counters must each be zero.

## Acceptance Criteria

- AC-01: clean execution base and current sources.
- AC-02: exact four-path manifest only.
- AC-03: server wrapper uses ambient `verifySessionCookie()`.
- AC-04: reviewer initial props map to reviewer before refresh.
- AC-05: client still emits `/api/auth/me` and retains jobs refresh.
- AC-06: anonymous null-session behavior remains.
- AC-07: existing markup, job logic, role logic, and copy are unchanged.
- AC-08: focused suite passes exactly 34/34.
- AC-09: TypeScript passes.
- AC-10: zero Playwright, Web submission, checker-job, retry, and provider call.
- AC-11: retained proof and read-only owners have zero diff.
- AC-12: worker does not stage or commit.

## Fail Conditions

Dirty start, stale source, wider diff, shell/auth/job/proof mutation, new auth
mechanism, visual change, removed refresh, missing test, count other than 34/34,
typecheck failure, browser or business invocation, provider call, unexpected
path, staging, commit, or broader claim returns `BLOCKED_WITH_REASON`.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only if every AC is evidenced. Otherwise stop
without live retry and name the exact source/test contradiction. Routine
in-manifest type or test defects must be repaired and rerun locally.

## Worker Autonomy / No-Question Rule

Proceed autonomously inside the exact manifest. Repair routine in-scope type,
import, and focused-test defects without asking the operator. Stop for a source
contradiction, wider owner requirement, browser execution, or claim expansion.

## Execution Plan

Execute in order: source freeze, client extraction, server wrapper, two focused
projection tests, exact five-file suite, typecheck, read-only diff audit,
worker-return gates, and unstaged handoff. Do not parallelize source mutation
with verification.

## Review Gate

Reviewer independently checks manifest fidelity, ambient-session call, initial
reviewer props, retained client refresh, five named page tests, exact 34/34,
typecheck, zero proof/live/provider action, unstaged status, and unchanged HEAD.
Reviewer must not run Playwright to promote this local repair.

## Operator Checkpoint

No operator choice is needed inside the exact manifest. Return control only if
the source requires a wider auth/shell owner, browser execution, provider use,
public-sync, or claim expansion.

## Closure Checklist

| Closure item | Worker disposition |
|---|---|
| clean base | required |
| server/client split | required |
| initial reviewer projection | required |
| client refresh emission | required |
| focused 34/34 | required |
| typecheck | required |
| zero proof/live/provider action | required |
| no staging/commit | required |
| GAP/roadmap/session projection | reviewer-owned |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Output artifact or field | Verification | Status |
|---|---|---|---|---|
| repair projection before browser rerun | server bootstrap | page and client source | focused tests | READY |
| prove request emission locally | deferred-fetch case | fetch ledger | page test | READY |
| retain prior business evidence | proof read-only | zero diff | git diff | READY |
| bounded cost | no browser/business/provider | command ledger | worker return | READY |

## Cost And Retry Control

Planned Playwright/browser invocations: zero. Planned Web submissions: zero.
Planned selected checker job executions: zero. Retries: zero. Provider calls:
zero. Local focused tests may be rerun only to repair in-manifest code defects.

## Agent Handoff Contract Control Block

Contract stable front door: `docs/reference/agent_handoff/README.md`.

Contract source archive-qualified exception for lifecycle parsing:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> worker -> reviewer/closer -> session-sync steward |
| phase | R3R2 reviewer auth-projection local repair |
| baseHeadFor(phase) | dispatchBaseHead=`a06265e49`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | exact Planned Worker Fulfillment Manifest |
| traceScope(phase, actor) | worker records source, split, tests, commands, zero-live counters, diff, status, and HEAD; reviewer owns closure |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns material commit |
| commitMode | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | R3R2 manifest only; session sync separate |
| nextMoveSurfaces | reviewer updates GAP, roadmap, coverage, and session only after accepted evidence |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3R2_REVIEWER_AUTH_PROJECTION_REPAIR_COMPLETION_2026-07-15.md`

reviewerOwnedClosurePaths: paired baseline/work-order status; completion review;
coverage, roadmap, GAP/front doors, and session only after evidence acceptance.

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3R2_REVIEWER_AUTH_PROJECTION_REPAIR_WORKER_RETURN_2026-07-15.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Skeleton command: `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3R2_REVIEWER_AUTH_PROJECTION_REPAIR_WORKER_RETURN_2026-07-15.md --title "CVF System Chain UC-04B R3R2 Reviewer Auth Projection Repair Worker Return" --profile WORKER_RETURN_FULL_GATE_V1`

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| intake summary | continue the reviewer projection GAP after accepted R3R1 blocked closure |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| selected route | dispatcher -> no-commit worker -> reviewer/closer |
| scope | local Web auth projection repair |
| risk sensitivity | R1 provider-free source/test repair with no browser or business action |
| escalation | source contradiction or wider owner requirement |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator continuation routes current CVF repair only; no external artifact absorbed |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | internal execution packet; governed source remains authority |
| Claim boundary | no external repository, corpus, or provider-readiness claim |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: current runtime repair; no legacy/external intake.

## Provider Memory Authority Boundary

Provider-local memory and chat are not evidence. Use only governed source,
R3R1 closure/evidence, GAP entry, commands, tests, and worker return.

## UI / Web Design Control Block

| Field | Value |
|---|---|
| designContract | root `DESIGN.md` read |
| UIChangeAuthorized | NO visual or copy change |
| retainedSurface | current Operations markup and test IDs |
| authorized structural change | server wrapper plus extracted client component |
| boundary | no redesign, token, accessibility, or responsive claim |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | deterministic local reviewer projection repair |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE only after focused tests and typecheck |
| receiptEvidence | N/A with reason: no live or business action is authorized |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no browser denial action in R3R2 |
| invocationBoundary | zero browser, Web submission, checker job, retry, provider call |
| interceptionBoundary | no IDE, provider, MCP, public, production, or universal interception |
| claimLanguage | local projection source and regression only |
| forbiddenExpansion | no reviewer browser denial, full UC-04B, unified inventory, provider, public, production, scale, certification, or user value |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Web UI/dashboard`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cvf-web`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Web UI/dashboard" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --max-results 20 --json`

Returned defects: NONE_RETURNED

Applicable changed-range defects: `ADIF-0034`; `ADIF-0035`; `ADIF-0036`;
`ADIF-0037`. The packet separates server session, client initial projection,
client refresh, and later business proof.

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce
git diff --check
git status --short
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Source Verification Block`; `Planned Worker Fulfillment Manifest`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Public Export Disposition` |
| gateRunPurpose | confirm server/client owners, exact manifest, deterministic proof, and no-live boundary before dispatch |
| claimBoundary | local repair dispatch only |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id SCLP-UC04B-R3R2 --title "System Chain UC-04B R3R2 Reviewer Auth Projection Repair" --date 2026-07-15 --base a06265e49 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | Web/UI no-commit repair |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, server bootstrap, client extraction, deterministic tests, zero-live controls, and handoff contract |
| checkerReadAheadConfirmation | current checker sources and literal gotchas read |
| docOnlyNewFields | `initialRole`; `initialUser`; dated R3R2 return labels |
| claimBoundary | dispatch only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair packet; no public-sync authority.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer |
| Provider or surface | private provenance repository; no provider call |
| Session or invocation | SCLP-UC04B-R3R2 packet authoring, 2026-07-15 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, trace reconciliation, apply_patch, resolver, dispatch gates |
| Target paths | paired R3R2 baseline and work order |
| Allowed scope source | active nextAllowedMove at `a06265e49` |
| Before status evidence | clean worktree at `a06265e49` |
| After status evidence | source-verified local-only R3R2 dispatch packet |
| Diff evidence | paired dispatch files only before commit |
| Approval boundary | packet authoring and later no-commit worker; no browser or implementation in authoring batch |
| Claim boundary | dispatch authority only |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc04b-r3r2-dispatch-2026-07-15 |
| Expected manifest | paired R3R2 baseline and work order |
| Actual changed set | paired R3R2 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

A PASS may prove only local source wiring and deterministic reviewer initial
projection/request emission. It cannot close reviewer browser denial, full
UC-04B, unified inventory, provider governance, public or production readiness,
scale, certification, or user value.
