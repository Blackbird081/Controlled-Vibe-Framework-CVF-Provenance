# CVF Agent Work Order - CVF Web UX T4 Browser Acceptance And Roadmap Closure

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-WEB-UX-T4

Dispatch base head: `5be9d3490`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated browser-audit worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_UX_T4_WORKER_RETURN_2026-07-19.md`

## Dispatch Prompt Envelope

Role: audit the accepted T1-T3 current-source UX in a real localhost browser.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_BROWSER_ACCEPTANCE_AND_ROADMAP_CLOSURE_2026-07-19.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: require the operator-provided final packet/session-sync HEAD before any action.

Current-time notes: T1 through T3 are closed bounded. T4 is the final roadmap acceptance audit, not source-repair authority.

Do-not-misread notes: start current-source Web and use browser automation with a visible rendered page. Do not use hosted screenshots, stale temp images, mocks, provider calls, or source edits.

Required first actions: confirm a clean worktree and supplied HEAD; read startup surfaces, guard orientation, literal gotchas, `DESIGN.md`, paired baseline, this order, and named source; run pre-implementation before starting Web.

Return contract: save durable localhost evidence and a terminal matrix; stop every server you started; return `COMPLETE_PENDING_REVIEW` only if all required rows pass, otherwise `BLOCKED_WITH_REASON` without source repair.

## Purpose

Determine whether the accepted task-first UX is coherent across desktop,
tablet, mobile, dark, light, and a non-default accent, while preserving route
reachability, keyboard focus, primary-action priority, state honesty, and
ordinary-versus-advanced audience disclosure.

## Authority Chain

Operator instruction -> accepted T0 audit -> active UX roadmap -> accepted
T1-T3 reviews -> paired T4 baseline -> this source-verified work order.

## Agent Roles

- Worker: current-source browser auditor; no source mutation and no commit.
- Reviewer/closer: recomputes evidence, decides roadmap closure, and commits.
- Session-sync steward: updates protected continuity only after acceptance.

## Write Ownership

Worker owns only the audit matrix, durable screenshots, and worker return.
Reviewer owns completion review, roadmap closure, bounded redispatch decisions,
and commits. Source, session state, deployment, and public-sync are forbidden.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| T1 | `docs/reviews/CVF_WEB_UX_T1_COMPLETION_2026-07-19.md` | `d4e6e48a0` | `CLOSED_PASS_BOUNDED` |
| T1P | `docs/reviews/CVF_WEB_UX_T1P_COMPLETION_2026-07-19.md` | `45d505836` | `CLOSED_PASS_BOUNDED`; hosted mutation parked |
| T2 | `docs/reviews/CVF_WEB_UX_T2_COMPLETION_2026-07-19.md` | `bb1418554` | `CLOSED_PASS_BOUNDED` |
| T3 | `docs/reviews/CVF_WEB_UX_T3_COMPLETION_2026-07-19.md` | `114daa54a` | `CLOSED_PASS_BOUNDED`; T4 released |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T4 --title "CVF Web UX T4 Browser Acceptance And Roadmap Closure" --date 2026-07-19 --base 5be9d3490 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus read-only Web/browser audit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added route-anchor evidence rule, viewport/theme/accent matrix, state coverage, failure route, and roadmap closure boundary |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| docOnlyNewFields | browser matrix fields below |
| claimBoundary | packet provenance only; no browser acceptance claim |

## Worker Autonomy / No-Question Rule

Repair audit-document and evidence-path gate failures directly. Do not repair
Web source. A reproducible UI defect, unavailable real browser, missing route,
or forbidden-path need returns `BLOCKED_WITH_REASON` with evidence.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-browser-audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-browser-audit" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | exact route identity and visible-anchor evidence are mandatory because T3 exposed mislabeled captures |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status; dependency rows; Source Verification; handoff route; worker-return shape; no-commit evidence |
| gateRunPurpose | confirm dispatch shape after current source and design reads |
| claimBoundary | checker compliance confirms packet shape only |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Worker instruction | Evidence required | Fail condition |
|---|---|---|---|
| desktop/tablet/mobile | use 1440x900, 820x1180, and 390x844 viewports | named PNGs and dimensions | any viewport class absent |
| dark/light/accent | desktop dark, tablet light, mobile non-default accent | visible preference selections plus rendered pages | appearance only inferred from storage |
| navigation and focus | exercise desktop/sidebar/mobile overlay and keyboard focus | matrix rows with action and visible result | route unreachable or focus invisible/trapped |
| primary actions and density | inspect Home plus knowledge journey | whole-viewport PNGs and visible anchors | explanation hides primary action |
| loading/empty/error honesty | record naturally available states without API/provider mutation | row per observed or N/A with exact source/runtime reason | fabricated state or blanket PASS |
| advanced disclosure | open Workspace technical details intentionally | closed/open images and visible anchor | internals dominate ordinary view or become unreachable |
| hosted boundary | use localhost current source only | URL `http://localhost:3000/...` in each row | hosted URL or stale image used |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Home route owner | EXISTS | canonical contract: direct current-source read of the dashboard Home page | line 85 | `HomePage` | dashboard Home route | ACCEPT |
| Workspace ordinary/advanced owner | RUNTIME_BEHAVIOR | canonical contract: direct current-source read of the dashboard Workspace page | lines 122-167 | `WorkspacePage`; `advanced-detail` | Workspace route | ACCEPT |
| Help owner | EXISTS | canonical contract: direct current-source read of the dashboard Help page | line 13 | `HelpPage` | Help route | ACCEPT |
| Knowledge governance owner | EXISTS | canonical contract: direct current-source read of the dashboard Knowledge page | line 90 | `KnowledgeGovernancePage` | Knowledge route | ACCEPT |
| Intake owner | EXISTS | canonical contract: direct current-source read of the dashboard Intake page | line 86 | `KnowledgeIntakePage` | Intake route | ACCEPT |
| Artifacts owner | EXISTS | canonical contract: direct current-source read of the dashboard Artifacts page | line 68 | `ArtifactsPage` | Artifacts route | ACCEPT |
| Transfer owner | EXISTS | canonical contract: direct current-source read of the dashboard Transfer page | line 120 | `WorkTransferPage` | Transfer route | ACCEPT |
| Sidebar advanced group | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | lines 49 and 222 | `Sidebar`; `advanced-operations` | dashboard navigation | ACCEPT |
| Theme/accent/preferences owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | lines 67-265 | `CompactHeader`; `setTheme`; `updateTweaks` | compact header | ACCEPT |
| Visual contract | LITERAL_INVARIANT | canonical contract: `DESIGN.md` | sections 4, 7, 8, 9, 14.6 | responsive priority; visible focus; progressive disclosure | CVF design contract | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime claim boundary |
|---|---|---|
| captureId | stable matrix-to-image identity | audit metadata only |
| exactUrl | proves route identity | localhost URL only |
| visibleRouteAnchor | proves visible page identity | rendered text, not authority |
| viewportThemeAccent | records tested presentation state | no hosted equivalence claim |
| widthMetric | records document/body versus client width | measurement from audited page only |

## Required First Reads

Read `DESIGN.md`, the paired baseline, this work order, all Source Verification
files, accepted T1-T3 reviews, browser skill/instructions available to the
worker, and checker sources before starting Web.

## Pre-Flight Checks

- require clean worktree and exact operator-provided `executionBaseHead`;
- run pre-implementation before starting the server;
- verify port 3000 availability and record any pre-existing owner before action;
- verify evidence directory is absent or empty; never reuse a temp or hosted image;
- load no provider key and invoke no API/provider governance proof.

## Execution Plan

1. Start current-source Next Web from the cvf-web package on localhost:3000 and wait for Ready.
2. Use a real rendered browser; prefer browser subagent when available, otherwise Playwright is acceptable with the fallback disclosed.
3. Establish onboarding/returning state explicitly and record it without changing source.
4. Execute the required viewport/theme/accent, route, navigation, focus, width, state, and audience matrix.
5. Save original PNGs to the durable evidence directory and write the audit matrix.
6. Run provider-free focused checks needed to prove unchanged source behavior, then worker-fast.
7. Stop all server/browser processes started by this tranche and verify no listener remains.
8. Return without staging or committing.

## Browser Acceptance Matrix

At minimum capture these twelve durable states:

| captureId | Viewport | Appearance | Route/state | Required visible anchor |
|---|---|---|---|---|
| desktop-dark-home | 1440x900 | dark | `/home`, returning | outcome/task choice heading |
| desktop-dark-workspace | 1440x900 | dark | `/workspace`, ordinary | ordinary status summary |
| desktop-dark-workspace-advanced | 1440x900 | dark | `/workspace`, advanced open | exact technical detail anchor |
| tablet-light-home | 820x1180 | light | `/home`, returning | outcome/task choice heading |
| tablet-light-sidebar | 820x1180 | light | sidebar open | all task groups reachable |
| tablet-light-journey | 820x1180 | light | knowledge journey route | current step and next route |
| mobile-accent-home | 390x844 | non-default accent | `/home`, returning | outcome/task choice heading |
| mobile-accent-sidebar | 390x844 | non-default accent | sidebar open | navigation overlay and close control |
| mobile-accent-help | 390x844 | non-default accent | `/help` | help outcome heading |
| mobile-accent-intake | 390x844 | non-default accent | `/knowledge/intake` | intake action heading |
| mobile-accent-artifacts | 390x844 | non-default accent | `/artifacts` | review/export heading |
| mobile-accent-transfer | 390x844 | non-default accent | `/work-transfer` | transfer check heading |

Every audit row must record `captureId`, exact localhost URL, visible route
anchor, viewport, theme/accent, interaction, result, width metric, screenshot
path, console/API diagnostic, and terminal verdict. A filename is not route
proof. Inspect original-resolution images after saving them.

## State And Accessibility Requirements

- Use keyboard Tab/Shift+Tab/Enter/Escape on preferences, sidebar, primary
  Home action, Workspace advanced details, and one journey navigation action.
- Record visible focus, logical order, close behavior, and absence of traps.
- Measure document/body `scrollWidth` and `clientWidth` on every captured route.
- Record loading, empty, unavailable, warning, or error states that naturally
  appear. Use `N/A with reason` for a state that cannot be reached without
  forbidden API/provider/data mutation; do not fabricate it.
- Disclose every console error, hydration warning, failed request, and 4xx/5xx
  response with route and whether it affects acceptance.

## Allowed Scope

- `docs/reviews/CVF_WEB_UX_T4_BROWSER_ACCEPTANCE_MATRIX_2026-07-19.md`
- `docs/reviews/CVF_WEB_UX_T4_WORKER_RETURN_2026-07-19.md`
- `docs/reviews/evidence/CVF_WEB_UX_T4_LOCALHOST_2026-07-19/`

## Forbidden Scope

Every other path, including all Web source/tests, dependencies, lockfiles,
scripts, generated aggregates, session state, roadmap, prior evidence, hosted
configuration, deployment, public-sync, provider/live, production, and
continuous-projection surfaces.

## Evidence Requirements

- exact before/after HEAD, status, staged state, and changed manifest;
- server start/Ready URL, process ownership, stop, and no-listener evidence;
- twelve or more original-resolution PNGs matching the matrix;
- exact URL and visible route anchor for every PNG;
- width, keyboard/focus, navigation, console/API, and natural-state results;
- provider-free verification and governed worker-return gate output;
- no source/test change and no commit.

## Verification Commands

1. repository root: pre-implementation autorun using the actual execution base;
2. cvf-web package: targeted provider-free tests for Home, Workspace, sidebar, header, and T2 journey owners;
3. repository root: `python governance/compat/check_governed_file_size.py --enforce`;
4. repository root: `python governance/compat/run_worker_return_fast_gate.py`;
5. final `git status --short`, `git diff --name-status`, `git diff --cached --name-status`, HEAD, and port-listener checks.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | active roadmap, accepted T1-T3 reviews, direct source |
| Scope classification | read-only current-source Web browser audit |
| Intake role | worker captures and classifies browser evidence |
| Reviewer role | independent reviewer/closer recomputes and decides roadmap closure |
| Routing decision | `WORKER_MUST_NOT_COMMIT` |
| Public route | `DEFERRED_PRIVATE_ONLY` |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer closure conversion |
| escalation condition | reproducible UI defect, forbidden source repair, or unavailable real browser |
| risk sensitivity | MEDIUM: final UX roadmap acceptance evidence |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside artifact is promoted |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T4 audit and independent completion review |
| Disposition | NOT_APPLICABLE_WITH_REASON: accepted CVF source and localhost browser control |
| Claim boundary | browser evidence is not external authority or hosted equivalence proof |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated browser-audit worker to independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=5be9d3490; executionBaseHead=OPERATOR_PROVIDED_FINAL_SESSION_SYNC_HEAD; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact three-output Allowed Scope |
| traceScope(phase, actor) | browser, process, images, matrix, diagnostics, commands, and return manifest |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | source repair and all hosted/deploy/public/provider/production/projection lanes parked |
| nextMoveSurfaces | reviewer decides roadmap closure; session-sync steward updates continuity after acceptance |

## Dual Agent Surface Matrix

| Surface | Interface | Authority / risk boundary | Required evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | repository/browser worker | exact Allowed Scope; read-only source; no commit | localhost matrix, images, diagnostics, git/process evidence | current filesystem and browser tooling | AUDIT_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | external CLI/MCP worker | same packet and no-commit boundary | same direct rendered-browser evidence | operator-provided browser/CLI adapter only | CONTRACT_ONLY |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-19.md` |
| reviewerOwnedClosurePaths | active UX roadmap; completion review; material commit |
| conversionRule | worker `COMPLETE_PENDING_REVIEW` is not closure; reviewer recomputes matrix, images, diagnostics, ports, and exact scope |
| failureRoute | accept truthful block and author a separate source-repair packet; worker must not mutate source |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must contain every full-gate heading and scalar token, exact
execution base, actual changed set, browser matrix summary, URL/anchor proof,
width and focus results, diagnostics, process stop proof, conditional-control
N/A blocks in checker shape, and no-commit evidence.

## Agent Operation Trace Block

| Field | Required worker evidence |
|---|---|
| Actor | delegated browser-audit worker |
| Provider or surface | local repository and current-source localhost browser |
| Agent type | audit worker |
| Session or invocation | T4 worker session |
| Invocation ID | worker records identifier or N/A with reason |
| Working directory | repository root and cvf-web package |
| Command or tool surface | git, Next dev, browser automation, provider-free tests, governance gates |
| Intent | final multi-viewport UX browser acceptance audit |
| Inputs | work order, baseline, DESIGN.md, accepted reviews, direct source |
| Target paths | exact Allowed Scope |
| Allowed scope source | this work order |
| Expected manifest | matrix, worker return, and durable evidence directory |
| Before status evidence | clean worktree and supplied HEAD |
| Actions | start current Web, interact, measure, capture, classify, stop |
| Outputs | audit matrix, PNGs, worker return |
| Evidence | URLs, visible anchors, images, metrics, diagnostics, commands |
| After status evidence | final status, staged state, HEAD, and port listeners |
| Actual changed set | exact final manifest |
| Manifest delta | NONE or explained allowed evidence subset |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |
| Approval boundary | no source repair, commit, live, deploy, public, production, or projection authority |
| Diff evidence | `git diff --name-status`; cached diff; HEAD before/after |
| Claim boundary | current-source localhost browser audit only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic current-source localhost browser audit |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no provider or governed execution receipt is authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT through browser interactions, images, measurements, and process evidence |
| invocationBoundary | local Next server and provider-free browser/test process only |
| interceptionBoundary | no provider, API gateway, production, hosted, or external-service interception |
| claimLanguage | current source rendered the exact audited states on localhost |
| forbiddenExpansion | source repair, hosted freshness, live governance, deployment, public, provider, or production readiness |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: T4 creates bounded review evidence in the existing
reviews tree and no durable governance foundation, registry, or aggregate.

## Acceptance Criteria

- [ ] Desktop, tablet, and mobile evidence is complete.
- [ ] Dark, light, and non-default accent states are visibly proven.
- [ ] Every screenshot row records exact localhost URL and visible route anchor.
- [ ] Navigation, keyboard focus, Escape/close, and advanced disclosure pass.
- [ ] Document/body overflow measurements are terminal for every captured route.
- [ ] Primary actions precede repeated explanation on ordinary-user surfaces.
- [ ] Natural loading/empty/error/warning states are classified without fabrication.
- [ ] Console/API diagnostics are disclosed and acceptance impact classified.
- [ ] Exactly Allowed Scope changed; no source/test mutation, staging, or commit.
- [ ] Worker-fast and process teardown checks pass.

## Review Gate

Reviewer must reopen original-resolution images, reproduce representative
desktop/tablet/mobile states, validate URL/anchor identity, inspect the full
matrix, recompute width/focus/diagnostic/port evidence, and compare all roadmap
criteria. Missing or mislabeled evidence blocks roadmap closure.

## Closure Checklist

- [ ] Every acceptance item is independently recomputed.
- [ ] Closure Diff Gate reconciles roadmap, packet, matrix, images, and claims.
- [ ] Any defect is routed to a separate source-repair packet, not silently repaired here.
- [ ] Roadmap status changes only after reviewer acceptance.
- [ ] Material commit contains no protected session-sync path.
- [ ] Hosted/deploy/public/provider/production/projection lanes remain parked.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all required audit rows are terminal
PASS or justified non-blocking N/A. Return `BLOCKED_WITH_REASON` for a
reproducible acceptance defect, unavailable real browser, missing route, or
forbidden repair need. Never edit source or commit.

## Operator Checkpoint

No mid-worker preference checkpoint is required. Roadmap closure is reviewer
owned. Hosted mutation, deployment, public-sync, provider/live, production,
and continuous-projection execution require separate authorization.

## Current Runtime Freshness Verification

| Claim | Current source evidence | Freshness disposition |
|---|---|---|
| task-first Home | `HomePage` direct read at dispatch base | VERIFIED_CURRENT |
| ordinary/advanced Workspace | `WorkspacePage`; `advanced-detail` | VERIFIED_CURRENT |
| knowledge journey routes | Help, Knowledge, Intake, Artifacts, Transfer route owners | VERIFIED_CURRENT |
| responsive navigation | `Sidebar`; `advanced-operations` | VERIFIED_CURRENT |
| appearance controls | `CompactHeader`; `setTheme`; `updateTweaks` | VERIFIED_CURRENT |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `DISPATCH_READY` | PASS |
| Completion or reviewer artifact | T4 completion review | N/A with reason: audit has not started | N/A with reason |
| Roadmap state | active UX roadmap | T4 packet authorized | PASS |
| Registry JSON | corpus registry aggregate | current drift check | PASS |
| Registry Markdown | paired registry surface | no mutation required unless coverage gate reports a gap | PASS |
| External evidence digest | durable T4 evidence directory | N/A with reason: repository-local evidence produced during audit | N/A with reason |
| System loop interlock | no system-loop mutation | N/A with reason: browser audit only | N/A with reason |
| Session continuity | active state and handoff | N/A with reason: session-sync-steward owned | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Dispatch receipt | source-verified ready packet | paired baseline/work-order at `5be9d3490` | PASS |
| Browser receipt | matrix plus durable current-source evidence | N/A with reason: audit has not started | N/A with reason |
| Provider receipt | none | N/A with reason: provider/live work is forbidden | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T4 audits private current source. Hosted deployment and public-sync remain separate.

## Claim Boundary

This packet authorizes only T4 read-only current-source localhost browser
acceptance. It does not authorize source repair, hosted mutation, deploy,
public-sync, provider/live calls, production action, or continuous projection.
