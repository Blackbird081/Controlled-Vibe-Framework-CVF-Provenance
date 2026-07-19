# CVF Agent Work Order - CVF Web UX T3 Home Onboarding Chrome And Density

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-WEB-UX-T3

Dispatch base head: `6b0bd77dd`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated implementation worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_UX_T3_WORKER_RETURN_2026-07-19.md`

## Dispatch Prompt Envelope

Role: implement bounded current-source Home, onboarding, chrome, and density remediation.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T3_HOME_ONBOARDING_CHROME_AND_DENSITY_2026-07-19.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: require the operator-provided final packet/session-sync HEAD before any edit.

Current-time notes: T1, T1P, and T2 are closed. T4 and every hosted/deploy/public/provider/production/projection lane remain parked.

Do-not-misread notes: T3 changes presentation and local first-run state composition only. It must not change APIs, auth, roles, stores, providers, dependencies, deployment, or public-sync.

Required first actions: confirm clean worktree and supplied HEAD; read startup surfaces, guard orientation, literal gotchas, `DESIGN.md`, paired baseline, this work order, and every source named below; run pre-implementation before editing.

Return contract: run current source on localhost, capture durable first-run and returning-user desktop/mobile evidence, run provider-free verification, leave everything uncommitted and unstaged, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Let a new user see CVF's task-first value immediately. Shorten the blocking
introduction, prevent a second automatic tour, reduce repeated Home explanation,
move settings/version controls into secondary disclosure, and remove horizontal
document overflow without weakening warnings at the point of action.

## Authority Chain

Operator instruction -> accepted T0 audit -> active UX roadmap -> accepted T1,
T1P, and T2 reviews -> paired T3 baseline -> this source-verified work order.

## Agent Roles

- Worker: bounded frontend implementer; must not commit.
- Reviewer/closer: recomputes source, tests, build, evidence, and owns closure.
- Session-sync steward: updates protected continuity only after acceptance.

## Write Ownership

Worker owns only worker-editable Allowed Scope paths. Reviewer owns the roadmap,
completion review, bounded repairs, and commits. Session state is forbidden.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| T1 | `docs/reviews/CVF_WEB_UX_T1_COMPLETION_2026-07-19.md` | `d4e6e48a0` | `CLOSED_PASS_BOUNDED` |
| T1P | `docs/reviews/CVF_WEB_UX_T1P_COMPLETION_2026-07-19.md` | `45d505836` | `CLOSED_PASS_BOUNDED` |
| T2 | `docs/reviews/CVF_WEB_UX_T2_COMPLETION_2026-07-19.md` | `bb1418554` | `CLOSED_PASS_BOUNDED`; T3 released |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T3 --title "CVF Web UX T3 Home Onboarding Chrome And Density" --date 2026-07-19 --base 6b0bd77dd --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit Web/UI profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added roadmap trace, exact source/test/evidence scope, line-count reduction, browser states, overflow metric, and provider-free exclusions |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_governed_file_size.py` |
| docOnlyNewFields | none |
| claimBoundary | packet provenance only; no implementation claim |

## Worker Autonomy / No-Question Rule

Repair allowed-scope source, test, browser, and checker failures directly.
Return only for a verified source contradiction, required forbidden path, or
missing authority/capability that prevents truthful execution.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-implementation" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | standard UI, browser evidence, maintainability, and no-commit controls apply |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status; dependency rows; Source Verification; handoff route; Worker Return Packet Shape Contract; no-commit and changed-set evidence |
| gateRunPurpose | confirm dispatch shape after current source and design reads |
| claimBoundary | checker compliance confirms packet shape only |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Worker instruction | Evidence required | Fail condition |
|---|---|---|---|
| shorten first-run onboarding | replace five-step blocker with at most two concise decisions and an immediate skip | first-run tests plus browser images | value remains hidden behind three or more steps |
| expose Home value immediately | put outcome choices and one primary next action above secondary education | returning-user Home images and copy assertions | hero/repeated explanation precedes useful choices |
| demote settings/version controls | place version and visual preferences behind one accessible secondary control; keep language reachable | header tests and mobile/desktop images | version/Tweaks/theme dominate primary chrome |
| reduce card/prose density | remove or consolidate repeated explanation while retaining action-point warnings | component tests and reviewer image comparison | same claim repeated in separate cards without distinct action |
| mobile fit | eliminate document-level horizontal overflow at 390px | measured scrollWidth/clientWidth evidence | document/body overflow is greater than zero |
| maintainability | extract same-domain Home presentation from the 951-line route | line counts and file-size gate | Home stays at or grows above 951 lines |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Home hierarchy and secondary tour | RUNTIME_BEHAVIOR | canonical contract: direct current-source read of the dashboard Home page | lines 84-948 | `HomePage`; `workflowState`; `OnboardingTour` | Home route | ACCEPT |
| Blocking five-step onboarding | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OnboardingWizard.tsx` | lines 20-166 | `STEPS`; `OnboardingWizard`; `onComplete` | `OnboardingWizardProps` | ACCEPT |
| Delayed four-step Home tour | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OnboardingTour.tsx` | lines 6-145 | `STORAGE_KEY`; `TOUR_STEPS`; `OnboardingTour` | contextual tour | ACCEPT |
| Completion state and starter transition | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useModals.ts` | lines 16-34 | `showOnboarding`; `handleOnboardingComplete` | `useModals` | ACCEPT |
| Header primary controls | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | lines 66-175 | `CompactHeader`; `versionBadge`; `tweaksButton` | header component | ACCEPT |
| Dashboard shell composition and main offset | RUNTIME_BEHAVIOR | canonical contract: direct current-source read of the dashboard route-group layout | lines 201-280 | `DashboardLayoutInner`; `CompactHeader`; `Sidebar` | dashboard layout | ACCEPT |
| UI contract | LITERAL_INVARIANT | canonical contract: `DESIGN.md` | sections 4, 7, 8, 9, 14.6 | progressive disclosure; responsive priority; natural language | CVF design contract | ACCEPT |

## New Source Paths

| Proposed path | Purpose | Boundary |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/home/HomeBrowseExperience.tsx` | extracted Home browse/value presentation | presentation only; route behavior remains in Home page |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/home/HomeBrowseExperience.test.tsx` | hierarchy, action, language, and density regression | provider-free unit test |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.test.tsx` | secondary-control, accessibility, and responsive regression | provider-free unit test |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.test.tsx` | Home composition and first-visible-value regression | provider-free unit test |

## Required First Reads

Read `DESIGN.md`, the paired baseline, this work order, all Source Verification
files, existing tests, and checker sources before implementation.

## Pre-Flight Checks

- require clean worktree and exact operator-provided `executionBaseHead`;
- verify existing paths and proposed-path collisions;
- capture starting line counts and run pre-implementation before editing;
- do not run a provider-calling benchmark or any live/provider suite.

## Implementation Requirements

1. Make first-run onboarding no more than two concise screens/decisions. The
   first screen must state the outcome-level value and offer a visible skip.
2. Do not auto-launch a second tour after onboarding. Preserve an accessible,
   user-invoked help path if the contextual content remains valuable.
3. On returning Home, show task/outcome choices and one primary next action
   before promotional hero copy, stats, setup education, or repeated cards.
4. Consolidate repeated explanatory surfaces. Keep risk, missing-key, review,
   and claim-boundary warnings at the exact action where they matter.
5. Replace the top row of version/Tweaks/language/theme controls with compact
   primary chrome and one accessible secondary preferences disclosure. Language
   must remain reachable without opening the sidebar.
6. At 390px and 1440px, `document.documentElement.scrollWidth` and
   `document.body.scrollWidth` must not exceed their client widths. Fix the
   owning component; do not hide overflow globally as a substitute.
7. Extract same-domain Home presentation so `home/page.tsx` is materially
   shorter than 951 lines. Do not compress logic or prose to evade the guard.
8. Preserve routes, localStorage completion semantics, starter transition,
   API events, auth, role checks, template selection, and warnings.
9. Add focused provider-free tests for Vietnamese and English, keyboard/ARIA,
   first-run/returning states, secondary settings, density, and overflow-prone
   responsive classes.
10. Run current source on `localhost:3000`; save first-run Home, returning Home,
    and secondary-preferences desktop/mobile PNGs in the durable evidence path.
    Evidence must show the whole viewport and current source, not hosted output.
11. Run focused tests, explicit provider-free suite excluding
    `src/**/*.live.test.ts` and `src/app/api/execute/pvv.nc.benchmark.test.ts`,
    `npm run check`, production build, file-size guard, and worker-return gate.
    Stop the server and disclose console or API errors without rerunning live.

## Allowed Scope

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OnboardingWizard.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OnboardingWizard.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OnboardingTour.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OnboardingTour.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/home/HomeBrowseExperience.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/home/HomeBrowseExperience.test.tsx`
- `docs/reviews/evidence/CVF_WEB_UX_T3_LOCALHOST_2026-07-19/`
- `docs/reviews/CVF_WEB_UX_T3_WORKER_RETURN_2026-07-19.md`

## Forbidden Scope

All other paths, especially dependencies and lockfiles, component barrels,
global overflow hiding, APIs, auth, roles, stores, providers, live tests,
deployment configuration, generated aggregates, session state, roadmap,
public-sync, production, and projection automation.

## Execution Plan

1. Capture base/status and pre-implementation evidence.
2. Extract Home presentation and simplify first-visible hierarchy.
3. Simplify onboarding/tour and compact the global header.
4. Add focused tests and run provider-free verification.
5. Run localhost browser proof, record width metrics, and save durable images.
6. Write the worker return, run worker-fast, verify exact changed set, stop Web.

## Evidence Requirements

- exact before/after HEAD, status, staged status, and changed manifest;
- focused and provider-free test counts, TypeScript check, build, file-size, and
  worker-return gate outputs;
- six durable localhost PNGs and a 390px/1440px scroll-width matrix;
- initial/final line counts for Home and every touched source/test file;
- current-source server start/ready/stop evidence and secret-safe console log.

## Verification Commands

Run from the cvf-web package unless a repository-root command is shown:

1. focused Vitest targets for every changed component and route;
2. `npx vitest run --exclude "src/**/*.live.test.ts" --exclude "src/app/api/execute/pvv.nc.benchmark.test.ts"`;
3. `npm run check`;
4. `npm run build`;
5. repository root: `python governance/compat/check_governed_file_size.py --enforce`;
6. repository root: `python governance/compat/run_worker_return_fast_gate.py --base <executionBaseHead> --head HEAD`.

The worker must not replace the required fast gate with individual checkers.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | active roadmap plus accepted T0-T2 evidence and direct source |
| Scope classification | bounded Web frontend implementation |
| Intake role | worker implements source, tests, and browser evidence |
| Reviewer role | independent reviewer/closer validates and commits |
| Routing decision | `WORKER_MUST_NOT_COMMIT` |
| Public route | `DEFERRED_PRIVATE_ONLY` |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer closure conversion |
| escalation condition | verified contradiction, forbidden-path need, or missing browser capability |
| risk sensitivity | MEDIUM: shared first-run and shell presentation |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no external knowledge artifact is promoted |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T3 work order and independent completion review |
| Disposition | NOT_APPLICABLE_WITH_REASON: T3 uses accepted CVF reviews and direct source only |
| Claim boundary | external agent or provider memory is not CVF authority |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated implementation worker to independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=6b0bd77dd; executionBaseHead=OPERATOR_PROVIDED_FINAL_SESSION_SYNC_HEAD; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact worker-owned Allowed Scope |
| traceScope(phase, actor) | source, tests, images, width metrics, commands, and return manifest |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | T4 and hosted/deploy/public/provider/production/projection lanes parked |
| nextMoveSurfaces | reviewer updates roadmap; session-sync steward updates protected continuity after acceptance |

## Dual Agent Surface Matrix

| Surface | Interface | Authority / risk boundary | Required evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | repository worker route | exact Allowed Scope; no commit | tests, build, localhost PNGs, width metrics, git evidence | current filesystem/tooling | IMPLEMENT_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | external CLI/MCP worker | same work order and no-commit boundary | same machine and visual evidence | operator-provided CLI/MCP adapter only | CONTRACT_ONLY |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_WEB_UX_T3_COMPLETION_2026-07-19.md` |
| reviewerOwnedClosurePaths | active UX roadmap; completion review; bounded repairs; material commit |
| conversionRule | worker `COMPLETE_PENDING_REVIEW` is not closure; reviewer recomputes all material and browser evidence |
| failureRoute | return bounded defects to worker or record `BLOCKED_WITH_REASON` |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --base <executionBaseHead> --head HEAD`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Worker return must contain Purpose; Target / Source; Scope / Methodology;
Findings / Position; Risk / Corrective Action; Claim Boundary; Checker Source
Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary
Control Block; Public Export Disposition; executionBaseHead; exact `git status
--short`; initial/final line counts; focused/provider-free/check/build/file-size
results; browser matrix and width measurements; console findings; server-stop
evidence; and N/A with reason for conditional governed sections.

## Agent Operation Trace Block

| Field | Required worker evidence |
|---|---|
| Actor | delegated implementation worker |
| Provider or surface | local repository and localhost browser |
| Agent type | implementation worker |
| Session or invocation | worker execution session |
| Invocation ID | worker records local invocation identifier or N/A with reason |
| Working directory | repository root and cvf-web package |
| Command or tool surface | git, Vitest, TypeScript, Next build/dev, browser automation, governance gates |
| Intent | T3 outcome-first Home and shell remediation |
| Inputs | work order, baseline, DESIGN.md, direct source |
| Target paths | exact Allowed Scope |
| Allowed scope source | this work order |
| Expected manifest | allowed modified/new paths actually needed |
| Before status evidence | clean worktree at HEAD `6b0bd77dd` before packet authoring; worker must independently confirm clean execution base |
| Actions | exact edits, tests, build, browser proof |
| Outputs | source/tests, durable PNGs, worker return |
| Evidence | commands, counts, width metrics, git manifests |
| After status evidence | final `git status --short` and staged-state output |
| Actual changed set | exact final manifest |
| Manifest delta | NONE or explained allowed-path subset |
| Approval boundary | no commit, live, deploy, public, production, or projection authority |
| Diff evidence | `git diff --name-status`; cached diff; HEAD before/after |
| Claim boundary | current-source localhost UI only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic local Web presentation implementation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no provider or governed execution receipt is authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT through source diff, tests, build, localhost images, and width measurements |
| invocationBoundary | local Next server and provider-free browser/test process only |
| interceptionBoundary | no provider, API gateway, production, or external-service interception |
| claimLanguage | current source renders the reviewed first-run and returning-user states on localhost |
| forbiddenExpansion | hosted freshness, live governance, provider, deployment, public, or production readiness |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: T3 extracts a Web presentation component inside the
existing cvf-web source tree; it does not create, move, or refactor a durable
governance foundation, index, registry, or generated aggregate.

## Acceptance Criteria

- [ ] First-run value is visible within at most two onboarding decisions.
- [ ] No second automatic tour follows onboarding.
- [ ] Returning Home exposes outcomes and primary action before education.
- [ ] Secondary controls no longer dominate desktop or mobile chrome.
- [ ] Document/body horizontal overflow is zero at 390px and 1440px.
- [ ] Home page is materially shorter than 951 lines through extraction.
- [ ] Focused, provider-free, check, build, file-size, browser, and worker gates pass.
- [ ] Exact Allowed Scope only; nothing staged; HEAD unchanged.

## Review Gate

Reviewer must recompute changed scope, focused/provider-free checks, production
build, line reduction, six images, width measurements, visible language,
keyboard access, console findings, server stop, and no-commit evidence. Any
obscured screenshot or measurement without current-source server evidence fails.

## Closure Checklist

- [ ] Every acceptance item is recomputed by the reviewer.
- [ ] Work order and roadmap statuses match the review decision.
- [ ] Closure Diff Gate reconciles roadmap, packet, artifacts, and claims.
- [ ] Material commit contains no protected session-sync path.
- [ ] T4 remains parked unless T3 closes with dependency evidence.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only after all worker-owned evidence passes.
Return `BLOCKED_WITH_REASON` before unauthorized edits when a source
contradiction, forbidden owner path, or unavailable browser capability blocks
truthful completion. Do not commit under either result.

## Operator Checkpoint

No mid-worker preference checkpoint is required. T4, hosted mutation,
deployment, public-sync, provider/live, production, and projection work require
later authorization and remain parked.

## Current Runtime Freshness Verification

| Claim | Current source evidence | Freshness disposition |
|---|---|---|
| first-run owner | `OnboardingWizard` plus `useModals` direct reads at dispatch base | VERIFIED_CURRENT |
| contextual Home tour | `OnboardingTour` render in `HomePage` at dispatch base | VERIFIED_CURRENT |
| header controls | `CompactHeader` direct read at dispatch base | VERIFIED_CURRENT |
| absent new test/component paths | `Test-Path` checks before packet authoring | VERIFIED_CURRENT |

This table establishes dispatch-time source freshness only. The worker must
recompute it at the supplied execution base.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `DISPATCH_READY` | PASS |
| Completion or reviewer artifact | T3 completion review | N/A with reason: implementation has not started | N/A with reason |
| Roadmap state | active UX roadmap | T3 packet authorization is current | PASS |
| Registry JSON | corpus registry aggregate | current drift check; no source-registration mutation required | PASS |
| Registry Markdown | paired registry surface | current governed surface; no source-registration mutation required | PASS |
| External evidence digest | durable T3 evidence directory | N/A with reason: worker creates evidence during execution | N/A with reason |
| System loop interlock | no system-loop change | N/A with reason: Web presentation only | N/A with reason |
| Session continuity | active state and handoff | N/A with reason: session-sync-steward owned | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Dispatch receipt | source-verified ready packet | this paired baseline/work-order family at base `6b0bd77dd` | PASS |
| Execution receipt | worker return and durable browser evidence | N/A with reason: execution has not started | N/A with reason |
| Provider receipt | none | N/A with reason: provider/live work is forbidden | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T3 is private current-source remediation pending review and later T4 acceptance.

## Claim Boundary

This packet authorizes only T3 current-source presentation work. It does not
authorize T4, hosted mutation, deploy, public-sync, provider/live calls,
production action, or continuous-projection execution.
