# CVF GC-018 Baseline - CVF Web UX T1 Task-First Navigation And Workspace Audience Separation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-WEB-UX-T1

Dispatch base head: `c02691201`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: delegated frontend implementation worker

## Purpose

Authorize a bounded T1 implementation that reorganizes existing CVF Web routes
around user jobs and separates ordinary `/workspace` summaries from advanced
technical continuity detail.

## Decision / Baseline / Proposed Tranche

Decision: release only CVF-WEB-UX-T1. Baseline: current sidebar, translation,
workspace presentation, and test owners at dispatch HEAD. Proposed tranche:
task-first regrouping plus workspace audience separation without data-owner or
deployment mutation.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-WEB-UX-T1 --title "CVF Web Task-First Navigation And Workspace Audience Separation" --date 2026-07-19 --base b9717a7f7 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CVF-WEB-UX-T0 pass at 93c2663a6" --include-worker-return-skeleton --stdout` |
| generatedProfile | web-ui-dashboard plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced skeleton fields with current roadmap, source symbols, exact scope, tests, browser proof, and closure ownership |
| checkerReadAheadConfirmation | dispatch-quality, ADIF disclosure, handoff-boundary, scaffold-provenance, structural, and file-size checker sources read |
| docOnlyNewFields | audienceSummary; advancedDetailDisclosure are implementation requirements, not claimed existing runtime fields |
| claimBoundary | dispatch provenance only; no implementation or readiness claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| CVF-WEB-UX-T0 audit | `docs/reviews/CVF_WEB_UX_CLARITY_T0_COMPLETION_2026-07-19.md`; closure `93c2663a6` | bounded audit accepted | PASS |
| UX remediation roadmap | `docs/roadmaps/CVF_WEB_TASK_FIRST_UX_AND_AUDIENCE_CLARITY_REMEDIATION_ROADMAP_2026-07-19.md`; commit `479e31701` | T1 dispatch authorized | PASS |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-dashboard`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-dashboard" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF-specific control beyond canonical Web, handoff, and worker-return gates |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | dispatch status; source verification dispositions; dependency rows; no-commit route; public disposition |
| gateRunPurpose | confirm packet shape after direct source verification and before dispatch |
| claimBoundary | checkers validate dispatch structure; source files and accepted audit support implementation facts |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Sidebar owns grouped route navigation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | `Sidebar` nav render, lines 145-275 | `Sidebar` | `Sidebar` component | ACCEPT |
| Sidebar group supports collapsible grouping | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/sidebar/SidebarNavGroup.tsx` | component definition | `SidebarNavGroup` | `SidebarNavGroup` component | ACCEPT |
| Translation dictionaries own nav labels | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n.tsx` | translation import and `t` resolver | `translations` | `LanguageProvider` | ACCEPT |
| Workspace data remains read-only | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | `getCvfWorkspaceReadModel` | `getCvfWorkspaceReadModel` | server read model | ACCEPT |
| Canonical Web design requirements | LITERAL_INVARIANT | canonical contract: `DESIGN.md` | Layout and Navigation; Accessibility and Language; Agent Prompt Guide | `DESIGN.md` | CVF design contract | ACCEPT |

## New Doc-Only Fields

| Field | Meaning | Runtime status |
|---|---|---|
| audienceSummary | acceptance label for ordinary-user workspace presentation | DOC_ONLY_NEW |
| advancedDetailDisclosure | acceptance label for explicit technical-detail access | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Packet paths | both target packet paths returned `False` before authoring | PASS |
| Batch token search | existing matches only in session queue surfaces | PASS |
| Collision decision | create fresh T1 packet; do not reuse closed T0 packet | PASS |

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | confirmed before packet authoring |
| UI claim boundary | local source implementation and browser evidence only; no hosted, production, deployment, or public readiness claim |

## Scope / Target / Owner Boundary

The worker may edit only the eight paths named by the paired work order. The
server read model, APIs, routes, auth, permissions, provider paths, generated
state, deployment configuration, and public repository are forbidden.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| route loss during regrouping | preserve every current href/state target and test representative groups |
| technical truth hidden | advanced disclosure retains exact values and source paths |
| language drift | update both dictionaries and i18n key coverage |
| local-only visual assumption | capture localhost browser evidence at desktop and mobile widths |

## Evidence / Verification

The worker must provide focused tests, TypeScript, production build, localhost
desktop/mobile screenshots, file-size result, exact changed set, empty staged
diff, and unchanged execution HEAD.

## Claim Boundary

This baseline authorizes the paired no-commit T1 worker only. It does not prove
implementation, hosted freshness, responsive completeness, deployment, public
export, provider behavior, or production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T1 is private source implementation pending independent review and
later browser/deployment/public tranches.
