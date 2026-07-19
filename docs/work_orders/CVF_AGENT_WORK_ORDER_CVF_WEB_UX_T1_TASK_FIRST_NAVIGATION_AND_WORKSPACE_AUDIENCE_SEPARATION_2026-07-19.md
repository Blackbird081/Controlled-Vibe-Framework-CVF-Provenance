# CVF Agent Work Order - CVF Web UX T1 Task-First Navigation And Workspace Audience Separation

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Batch ID: CVF-WEB-UX-T1

Dispatch base head: `c02691201`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated frontend implementation worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_UX_T1_WORKER_RETURN_2026-07-19.md`

## Dispatch Prompt Envelope

Role: implement the bounded T1 CVF Web navigation and workspace audience split.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T1_TASK_FIRST_NAVIGATION_AND_WORKSPACE_AUDIENCE_SEPARATION_2026-07-19.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: require the exact committed dispatch/session-sync HEAD named
in the operator prompt before any edit.

Current-time notes: packet authored 2026-07-19 from current source at dispatch
HEAD `c02691201`; hosted state is outside this tranche.

Do-not-misread notes: preserve every existing route and exact technical truth.
Do not change the workspace read model, API, auth, provider, deployment, public
surface, or session state. Do not use hosted screenshots as current-source
proof.

Required first actions: read startup state, guard orientation, literal gotchas,
`DESIGN.md`, the paired baseline, this packet, all Source Verification files,
and worker-output checkers before writing.

Return contract: leave all changes uncommitted and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Make navigation understandable by user job and make `/workspace` useful to an
ordinary user before progressively disclosing exact reviewer/operator detail.

## Authority Chain

Operator instruction -> closed T0 audit -> UX remediation roadmap at
`479e31701` -> paired GC-018 baseline -> this T1 work order.

## Agent Roles

- Worker: bounded frontend implementer; no commit.
- Reviewer/closer: recomputes source, tests, build, and browser evidence;
  repairs within scope; owns material commit.
- Session-sync steward: updates next-move surfaces only after reviewer decision.

## Required First Reads

1. `CVF_SESSION_MEMORY.md` and active state/handoff.
2. `docs/reference/guard_orientation/README.md` and literal gotchas.
3. `DESIGN.md`.
4. Paired baseline, this work order, and every Source Verification source.
5. Worker-return and relevant frontend/file-size checker sources.

## Pre-Flight Checks

- confirm clean worktree and exact operator-provided execution base HEAD;
- run pre-implementation autorun before the first edit;
- confirm all eight Allowed Scope paths and no forbidden-path need;
- read current sidebar, translations, workspace page, and tests directly.

## Write Ownership

Worker owns exactly the Allowed Scope paths. Reviewer owns optional completion
and browser-evidence paths declared by Reviewer Closure Conversion. Session
surfaces and Git commits remain reviewer/session-steward owned.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-WEB-UX-T1 --title "CVF Web Task-First Navigation And Workspace Audience Separation" --date 2026-07-19 --base b9717a7f7 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CVF-WEB-UX-T0 pass at 93c2663a6" --include-worker-return-skeleton --stdout` |
| generatedProfile | web-ui-dashboard plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced skeleton fields with exact source facts, allowed paths, tests, browser proof, and closure conversion |
| checkerReadAheadConfirmation | dispatch-quality, ADIF disclosure, handoff-boundary, scaffold-provenance, worker-return, and structural checker sources read |
| docOnlyNewFields | audienceSummary; advancedDetailDisclosure |
| claimBoundary | dispatch provenance only; no implementation or readiness claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T0 audit closure | `docs/reviews/CVF_WEB_UX_CLARITY_T0_COMPLETION_2026-07-19.md`; `93c2663a6` | accepted bounded | PASS |
| T1 roadmap authority | `docs/roadmaps/CVF_WEB_TASK_FIRST_UX_AND_AUDIENCE_CLARITY_REMEDIATION_ROADMAP_2026-07-19.md`; `479e31701` | T1 dispatch authorized | PASS |
| paired baseline | `docs/baselines/CVF_GC018_CVF_WEB_UX_T1_TASK_FIRST_NAVIGATION_AND_WORKSPACE_AUDIENCE_SEPARATION_2026-07-19.md` | dispatch-ready and source verified | PASS |

## Worker Autonomy / No-Question Rule

Repair allowed-scope defects directly. Return only for a source contradiction,
forbidden-path need, or missing authority that makes truthful completion
impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-dashboard`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-dashboard" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | canonical Web, handoff, source, and worker-return controls apply |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | dispatch envelope; source table; roadmap trace; fulfillment manifest; handoff fields; worker return profile |
| gateRunPurpose | confirm exact dispatch contract after source verification |
| claimBoundary | checker compliance is packet evidence, not UI completion evidence |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Grouped navigation owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | nav render, lines 145-275 | `Sidebar` | `Sidebar` component | ACCEPT |
| Navigation group primitive | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/sidebar/SidebarNavGroup.tsx` | component definition | `SidebarNavGroup` | `SidebarNavGroup` component | ACCEPT |
| Translation resolver | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n.tsx` | imports and `t` | `translations` | `LanguageProvider` | ACCEPT |
| Vietnamese dictionary | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n/vi.json` | navigation keys | `nav` | translation dictionary | ACCEPT |
| English dictionary | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n/en.json` | navigation keys | `nav` | translation dictionary | ACCEPT |
| Workspace data owner remains unchanged | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | `getCvfWorkspaceReadModel` | `getCvfWorkspaceReadModel` | server read model | ACCEPT |
| Design contract | LITERAL_INVARIANT | canonical contract: `DESIGN.md` | sections 4, 7, 8, 9, and 14.6 | `DESIGN.md` | canonical visual contract | ACCEPT |

## New Doc-Only Fields

| Field | Meaning | Disposition |
|---|---|---|
| audienceSummary | acceptance concept for ordinary-user view | DOC_ONLY_NEW |
| advancedDetailDisclosure | acceptance concept for explicit technical disclosure | DOC_ONLY_NEW |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap T1 requirement | Worker instruction | Evidence |
|---|---|---|
| task-oriented navigation | regroup existing routes into clear user-job sections | sidebar tests plus browser screenshot |
| preserve all routes | keep every existing href/state target reachable | route manifest assertions |
| ordinary workspace summary | lead with plain-language status and next action | workspace component test |
| advanced exact detail | disclose mode, handoff, dispatch, lanes, paths, and sources explicitly | test closed/open disclosure state |
| no deployment work | forbid deployment and hosted-readiness claims | exact changed set and worker return |

## Implementation Requirements

1. Reorganize navigation into understandable groups equivalent to Home,
   AI work, Knowledge and review, Advanced operations, and Account/settings.
2. Preserve every existing route target and permission condition.
3. Use both translation dictionaries for new group and action labels.
4. Make `/workspace` lead with a Vietnamese-first plain-language operational
   summary, current next action, and recovery state.
5. Put raw mode, previous mode, handoff filename, commit, dispatch, lane IDs,
   source paths, and boundary text inside an explicit accessible advanced
   disclosure; do not delete or alter those values.
6. Do not modify the server read model or fabricate missing/current state.
7. Add focused tests for navigation route preservation, group labels, ordinary
   workspace summary, disclosure state, and absence of mutation controls.
8. Run localhost and capture desktop plus mobile screenshots of `/home` sidebar
   and `/workspace` with advanced detail closed and open.

## Execution Plan

1. Preserve a route/permission manifest from the current Sidebar.
2. Implement translated task groups and focused Sidebar tests.
3. Recompose workspace presentation without changing its model.
4. Extend workspace tests for summary, disclosure, and no-mutation behavior.
5. Run focused tests, TypeScript, build, localhost browser proof, and governed
   gates; repair allowed-scope failures; return uncommitted.

## Allowed Scope

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n/vi.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n/en.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n-keys.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.test.tsx`
- `docs/reviews/CVF_WEB_UX_T1_WORKER_RETURN_2026-07-19.md`

## Forbidden Scope

All other paths, especially workspace read-model source/tests, APIs, auth,
permissions, providers, package dependencies, deployment config, public-sync,
session state, generated aggregates, governance checkers, and Git history.

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | Yes | task-first navigation implementation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.test.tsx` | Yes | route, group, and permission preservation proof |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n/vi.json` | Yes | Vietnamese group labels |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n/en.json` | Yes | English group labels |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx` | Yes | ordinary and advanced audience separation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.test.tsx` | Yes | audience and jargon-leak regression proof |
| `docs/reviews/CVF_WEB_UX_T1_WORKER_RETURN_2026-07-19.md` | Yes | worker and R1 evidence return |
| `docs/reviews/evidence/CVF_WEB_UX_T1_R1_LOCALHOST_2026-07-19` | Yes | durable desktop/mobile localhost images |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| seven Web source/test paths | modify or create only as required; every omission explained |
| worker return | create full gated return with screenshot locators and exact changed set |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one frontend worker, then independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=`c02691201`; executionBaseHead=operator-provided committed dispatch/session-sync HEAD; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exactly the eight Allowed Scope paths |
| traceScope(phase, actor) | worker records commands, screenshots, status, and manifest; reviewer recomputes evidence |
| commitOwner(phase) | worker forbidden; reviewer/closer owns material commit |
| crossBatchIsolation | T1P-T4 and all public/deploy/provider/projection lanes remain parked |
| nextMoveSurfaces | reviewer/session-sync steward updates only following reviewer acceptance |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator instruction plus closed UX audit |
| Scope classification | bounded Web frontend implementation |
| Intake role | worker implements navigation and workspace presentation |
| Reviewer role | independent reviewer/closer validates and commits accepted material |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; worker returns uncommitted artifacts |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer conversion |
| escalation condition | return blocked for source contradiction or forbidden-path need |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_WEB_UX_T1_COMPLETION_2026-07-19.md` |
| reviewerOwnedClosurePaths | eight worker paths plus optional conventional completion review and separately authorized browser evidence directory |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_UX_T1_WORKER_RETURN_2026-07-19.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
Set-Location 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web'
npx vitest run src/components/Sidebar.test.tsx 'src/app/(dashboard)/workspace/page.test.tsx' src/lib/i18n-keys.test.ts
npx tsc --noEmit
npm run build
Set-Location ../../../..
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --name-status
git diff --cached --name-status
git status --short
git rev-parse --short HEAD
```

Browser evidence must come from current source on `http://localhost:3000`, not
the hosted site. Pure UI structure proof needs no provider call.

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | REQUIRED before implementation |
| UI claim boundary | local navigation/workspace clarity only; no hosted, deployment, provider, public, or production readiness claim |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | current Sidebar, i18n, workspace page, read model, and tests cited above |
| Runtime behavior claimed | bounded current-source presentation ownership only |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - source symbols verified on 2026-07-19; hosted freshness belongs to T1P |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing cvf-web frontend component, dictionaries, and tests |
| Storage decision | reuse existing owners; one same-domain Sidebar test may be created |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | N/A with reason: no governance foundation or index is created, moved, or refactored |

## Dual Agent Surface Matrix

| Surface class | Intended user | Interface | Authority/risk boundary | Required evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | reviewer/operator | advanced workspace detail | read-only exact values | component tests and browser evidence | existing read model |
| EXTERNAL_AGENT_CLI_MCP | outside technical consumer | not implemented in T1 | no CLI/MCP or runtime authority | N/A with reason: Web-only tranche | DOCUMENTATION_ONLY_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside artifact is absorbed |
| Matching local-view guard | N/A with reason: current source and accepted CVF audit are authority |
| Owner surface | paired roadmap and current Web source |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | external-agent disposition does not authorize an adapter |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch steward |
| Provider or surface | private provenance workspace |
| Session or invocation | CVF-WEB-UX-T1 packet authoring, 2026-07-19 |
| Working directory | repository root |
| Command or tool surface | source reads, scaffold preview, resolver, patch, dispatch gates |
| Target paths | paired baseline and work order |
| Allowed scope source | operator continuation plus roadmap commit `479e31701` |
| Before status evidence | clean worktree at HEAD `c02691201` before packet authoring |
| After status evidence | paired source-verified dispatch artifacts pending commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | T1 dispatch only |
| Claim boundary | no implementation, provider, deploy, public, or production action |
| Agent type | dispatcher |
| Invocation ID | `cvf-web-ux-t1-dispatch-2026-07-19` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local Web presentation changes and tests |
| claimDisposition | CLAIM_REJECTED: no execution-control or governance-enforcement behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: browser screenshots are UI evidence only |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source edits, tests, build, and localhost browser inspection only |
| invocationBoundary | no provider or governed product workflow invocation |
| interceptionBoundary | no wrapper, proxy, runtime gate, or coding control |
| claimLanguage | implemented locally only after evidence; never hosted-ready without T1P |
| forbiddenExpansion | no read model, API, auth, provider, deploy, public, session, or projection mutation |

## Acceptance Criteria

- [x] exactly the Allowed Scope changed set;
- [x] every existing route target remains represented;
- [x] new groups have both Vietnamese and English labels;
- [x] `/workspace` ordinary summary appears before internal detail;
- [x] advanced disclosure retains exact technical values;
- [x] focused tests, TypeScript, build, file-size, and worker-return gates pass;
- [x] localhost desktop and mobile evidence is recorded;
- [x] nothing staged and worker HEAD unchanged.

## Evidence Requirements

- exact route/permission preservation assertions;
- focused test counts and commands;
- TypeScript and production-build results;
- localhost screenshot paths for required desktop/mobile states;
- actual `git diff --name-status`, cached diff, status, and HEAD.

## Review Gate

Reviewer must inspect the changed UI source, rerun focused tests and build,
open localhost in a graphical browser, verify labels and disclosure states, and
run reviewer-fast plus pre-closure gates before acceptance.

## Closure Checklist

- [x] All roadmap trace rows are satisfied or blocked explicitly.
- [x] Allowed changed set is exact; no forbidden path changed.
- [x] Route and permission preservation evidence passes.
- [x] Ordinary summary and advanced exact detail both pass.
- [x] Focused tests, TypeScript, build, browser proof, and governed gates pass.
- [x] Worker made no commit and reviewer owns closure.

## Closure Diff Gate

| Requirement | Final evidence | Disposition |
|---|---|---|
| navigation regroup | five task-first groups with route/permission tests | PASS |
| audience separation | plain-language summary plus exact advanced disclosure | PASS |
| responsive proof | durable desktop/mobile localhost images | PASS |
| source quality | focused tests 152/152, TypeScript, production build | PASS |
| scope boundary | exact material set; temporary helper removed | PASS |
| public/deploy boundary | no hosted, provider, deploy, or public mutation | PASS |

## Closure Decision

`CLOSED_PASS_BOUNDED`

Accepted by the independent reviewer/closer with a bounded two-file reviewer
repair and fresh R1 localhost evidence. T1P packet authoring is released;
later implementation, deployment, public, provider, and projection lanes
remain parked.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | top status and checked acceptance/closure lists | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WEB_UX_T1_COMPLETION_2026-07-19.md` | reviewer decision `CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_WEB_TASK_FIRST_UX_AND_AUDIENCE_CLARITY_REMEDIATION_ROADMAP_2026-07-19.md` | T1 accepted; T1P is the next separately governed move | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | changed-path coverage and aggregate drift checks pass | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | paired registry surface exists; no mutation required by the coverage gate | PASS |
| External evidence digest | repository-local R1 evidence | N/A with reason: evidence is committed inside this repository | N/A with reason |
| System loop interlock | no system-loop mutation authorized | N/A with reason: presentation-only Web tranche | N/A with reason |
| Session continuity | active session front door and handoff | N/A with reason: protected session-sync follows material commit | N/A with reason |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with all required evidence and no staged
files. Return `BLOCKED_WITH_REASON` before scope expansion when a forbidden path
or source contradiction is unavoidable.

## Operator Checkpoint

T1 implementation is authorized. T1P-T4, deployment, hosted repair,
public-sync, provider/live activity, production action, and projection
execution remain parked until independent T1 closure.

## Claim Boundary

This work order authorizes only the bounded no-commit T1 implementation. It
does not authorize T1P-T4, deployment, hosted claims, provider calls, public
export, production action, session mutation, or projection execution.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private implementation dispatch pending independent review and later
deployment/public authorization.
