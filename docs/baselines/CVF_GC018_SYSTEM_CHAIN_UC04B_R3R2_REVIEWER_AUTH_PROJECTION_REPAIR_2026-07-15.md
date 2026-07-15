# CVF GC-018 System Chain UC-04B R3R2 Reviewer Auth Projection Repair

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-07-15

GC-018 ID: `SCLP-UC04B-R3R2-GC018`

dispatchBaseHead: `a06265e49`

## Purpose

Repair the bounded reviewer projection edge before another UC-04B browser
business proof. Replace the Operations page's client-only anonymous bootstrap
with a server-derived initial session projection while retaining client refresh.

## Proposed Tranche / Decision

Dispatch one no-commit worker for a provider-free source and test repair only.
No Playwright, browser business invocation, Web job submission, checker job,
provider call, public-sync, or session-state mutation is authorized.

## Scope / Target / Owner Boundary

Owned source is the Operations server entry, a new client component extracted
from the current page, and the existing focused page test. `middleware-auth.ts`,
`/api/auth/me`, shell `useAuth`, the R3R1 proof spec, job route/runtime, audit
store, checker owners, and all session/governance owners remain read-only.

## Design Control Gate

- Root `DESIGN.md` was read.
- No visual redesign or copy change is authorized.
- Existing markup, test IDs, role mapping, job behavior, and audit behavior
  remain unchanged.
- Server bootstrap adds no new visible surface; it removes the initial false
  anonymous projection for authenticated requests.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Operations page is client-only | `canonical-contract:cvf-web-operations-page-source` | line 1 and line 127 | `GovernanceOperationsPage` | App Router page | EXISTS | ACCEPT |
| role initializes anonymous | `canonical-contract:cvf-web-operations-page-source` | line 128 | `role` | component state | VALUE_SET | ACCEPT |
| client auth refresh owner | `canonical-contract:cvf-web-operations-page-source` | lines 148-160 | `load` | mount effect | RUNTIME_BEHAVIOR | ACCEPT |
| developer maps to operator | `canonical-contract:cvf-web-operations-page-source` | lines 97-101 | `mapRole` | Operations role projection | RUNTIME_BEHAVIOR | ACCEPT |
| requestless ambient session owner exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | lines 96-110 and 118-122 | `verifySessionCookie` | session adapter | RUNTIME_BEHAVIOR | ACCEPT |
| auth route uses request-bound owner | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/auth/me/route.ts` | lines 4-7 | `GET` | auth projection API | RUNTIME_BEHAVIOR | ACCEPT |
| current component test mocks client fetch | `canonical-contract:cvf-web-operations-page-test-source` | `setupFetch`; `GovernanceOperationsPage` suite | `fetchMock` | focused UI regression | EXISTS | ACCEPT |
| R3R1 found no client request | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3R1_NEGATIVE_LOCATOR_RECOVERY_COMPLETION_2026-07-15.md` | Evidence Reconciliation | `/api/auth/me` | reviewer closure | VALUE_SET | ACCEPT |
| existing projection GAP reopened | `docs/reference/system_chain/gaps/entries/web_nextauth_application_projection_split.json` | `currentStatus`; `actionOwner` | `cvf.asc.gap.web_nextauth_application_projection_split.v1` | GAP registry | VALUE_SET | ACCEPT |

## New Implementation Items

| Item | Exact authorized shape | Existing-source claim |
|---|---|---|
| `OperationsClient.tsx` | extracted current client implementation with `initialRole?: string` and `initialUser?: string` props; initial state uses existing `mapRole`; current `/api/auth/me` refresh remains | DOC_ONLY_NEW |
| server page wrapper | async page calls ambient `verifySessionCookie()` and passes session role/user to the client component | DOC_ONLY_NEW |
| deterministic projection tests | server wrapper passes reviewer props; client renders reviewer before refresh resolves and emits `/api/auth/me` | DOC_ONLY_NEW |

## Current Runtime Freshness Verification

Fresh inspection at `a06265e49` confirmed the client-only anonymous initial
state, ambient session adapter, request-bound auth API, and existing mocked
component test. Retained R3R1 trace contained all page chunks with HTTP 200 but
zero `/api/auth/me`, zero `/api/system/jobs`, zero console errors, and zero page
errors. This packet does not claim a proven browser-engine root cause.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| R3R1 bounded closure | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3R1_NEGATIVE_LOCATOR_RECOVERY_COMPLETION_2026-07-15.md` | `0856e090d` | SATISFIED |
| projection GAP reopen | `docs/reference/system_chain/gaps/entries/web_nextauth_application_projection_split.json` | `0856e090d` | SATISFIED |
| active route | `AGENT_HANDOFF_V44_2026-07-15.md` | `a06265e49` | SATISFIED |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Packet control | Evidence target | Status |
|---|---|---|---|
| repair reviewer projection before rerun | server-derived initial props | focused server/client tests | READY |
| preserve client refresh | retain `/api/auth/me` mount fetch | request-emission test | READY |
| avoid live cost | zero Playwright/business/provider | command ledger in return | READY |
| retain prior evidence | proof spec read-only | zero diff | READY |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Web UI/dashboard`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cvf-web`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Web UI/dashboard" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --max-results 20 --json`

Returned defects: NONE_RETURNED

Changed-range applicability: `ADIF-0034`; `ADIF-0035`; `ADIF-0036`;
`ADIF-0037`. This packet performs deterministic local repair before any later
browser proof and does not use a timeout increase as repair evidence.

## Cost And Retry Control

Browser invocations, Web submissions, selected checker executions, retries,
and provider calls are all exactly zero. Local Vitest and TypeScript commands
are deterministic verification, not business invocations.

## Acceptance Criteria

- Current Operations markup and business behavior are preserved.
- Server wrapper passes ambient authenticated role and user to the client.
- Client renders mapped reviewer immediately from initial props.
- Client still emits `/api/auth/me` and applies a successful refresh.
- Existing three page tests remain; exactly two projection tests are added.
- Focused five-file suite passes 34/34 and typecheck passes.
- No proof spec, auth owner, shell hook, job route/runtime, audit, checker,
  browser output, provider, roadmap, GAP, or session owner changes.

## Evidence / Verification

The worker must return source-diff evidence, two named deterministic projection
tests, exact focused 34/34 output, clean TypeScript output, zero diff for every
read-only owner, zero browser/business/provider counters, unchanged HEAD, and
unstaged status. Reviewer closure may accept local repair only; a later packet
owns browser proof.

## Fail Conditions

Source contradiction, wider owner edit, new auth mechanism, swallowed server
error without explicit anonymous fallback, removal of client refresh, markup or
business behavior change, fewer than 34 focused PASS results, typecheck failure,
browser invocation, Web submission, checker job, retry, provider call, staging,
commit, or expanded claim blocks the worker return.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair dispatch; no public-sync authority.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `New Implementation Items`; `Dependency Release Evidence`; `Roadmap-To-Work-Order Trace Matrix`; `Public Export Disposition` |
| gateRunPurpose | confirm current projection owners, bounded repair, and zero-live boundary before dispatch |
| claimBoundary | dispatch authorization only; no implementation or browser claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id SCLP-UC04B-R3R2 --title "System Chain UC-04B R3R2 Reviewer Auth Projection Repair" --date 2026-07-15 --base a06265e49 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | Web/UI no-commit repair |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, server/client split, deterministic tests, zero-browser boundary, and handoff controls |
| checkerReadAheadConfirmation | applicable sources and literal gotchas read |
| docOnlyNewFields | new component props and dated R3R2 evidence labels only |
| claimBoundary | dispatch authoring provenance only |

## Claim Boundary

This baseline authorizes a bounded local projection repair. It does not prove
browser hydration, reviewer denial, full UC-04B, unified inventory, provider
governance, public or production readiness, scale, certification, or user value.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | SCLP-UC04B-R3R2 | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3R2_REVIEWER_AUTH_PROJECTION_REPAIR_COMPLETION_2026-07-15.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Worker return | declared R3R2 return | `COMPLETE_PENDING_REVIEW` accepted | PASS |
| Deterministic regression | five focused files | 34/34 PASS and typecheck PASS | PASS |
| Registry JSON | coverage and generated GAP index | local repair accepted; browser proof pending | PASS |
| Registry Markdown | system-chain front door | R3R3 negative proof next | PASS |
| System loop interlock | local request-emission regression | browser invocation remains zero | PASS |
| Roadmap state | system-chain roadmap | R3R3 negative proof packet next | PASS |
| External evidence digest | N/A with reason: repository evidence only | no external input | N/A with reason |
| Session continuity | active session | separate post-material sync | N/A with reason |
| Public export | this baseline | `DEFERRED_PRIVATE_ONLY` | PASS |
