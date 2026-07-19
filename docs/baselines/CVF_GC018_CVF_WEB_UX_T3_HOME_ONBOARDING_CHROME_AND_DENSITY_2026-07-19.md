# CVF GC-018 Baseline - CVF Web UX T3 Home Onboarding Chrome And Density

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-WEB-UX-T3

Dispatch base head: `6b0bd77dd`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: delegated implementation worker

## Purpose

Pin the current Home, first-run onboarding, global header, and dashboard layout
owners before T3 makes the product value visible sooner, reduces repeated
explanation, moves secondary controls out of primary attention, and removes
document-level mobile overflow.

## Decision/Baseline/Proposed Tranche

- Decision: release bounded T3 current-source Web implementation.
- Baseline: the current five-step blocking wizard, four-step delayed Home tour,
  951-line Home page, always-visible version/Tweaks/language/theme controls, and
  dashboard shell at dispatch base `6b0bd77dd`.
- Proposed tranche: T3 only. T4 and all hosted, deployment, public, provider,
  production, and continuous-projection lanes remain parked.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| T1 task-first navigation | `docs/reviews/CVF_WEB_UX_T1_COMPLETION_2026-07-19.md` | `d4e6e48a0` | `CLOSED_PASS_BOUNDED` |
| T1P hosted/current diagnosis | `docs/reviews/CVF_WEB_UX_T1P_COMPLETION_2026-07-19.md` | `45d505836` | `CLOSED_PASS_BOUNDED`; mutation remains parked |
| T2 guided knowledge journey | `docs/reviews/CVF_WEB_UX_T2_COMPLETION_2026-07-19.md` | `bb1418554` | `CLOSED_PASS_BOUNDED`; T3 packet authoring released |

## Evidence/Verification

Direct reads verified the Home, onboarding, header, modal-state, and dashboard
layout owners. The worker must recompute these facts before editing; the
reviewer must recompute implementation, test, build, and browser evidence.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T3 --title "CVF Web UX T3 Home Onboarding Chrome And Density" --date 2026-07-19 --base 6b0bd77dd --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit Web/UI profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added released dependencies, direct source owners, line-count constraint, exact browser states, and provider-free test boundary |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_file_size.py` |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no UI or browser acceptance claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-implementation" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | standard UI, evidence, maintainability, and no-commit controls apply |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | ready status; dependency evidence; source verification columns; ADIF query; no-commit conversion; exact changed-set boundary |
| gateRunPurpose | confirm dispatch shape after current source and design-contract reads |
| claimBoundary | checker compliance confirms packet shape only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Home owns browse/value hierarchy and renders the secondary tour | RUNTIME_BEHAVIOR | canonical contract: direct current-source read of the dashboard Home page | lines 84-948 | `HomePage`; `workflowState`; `OnboardingTour` | Home route component | ACCEPT |
| Home is above the frontend advisory threshold | VALUE_SET | canonical contract: direct current-source read of the dashboard Home page | current file length | `HomePage` | governed file-size policy | ACCEPT |
| Blocking onboarding contains five steps and opens starter mode | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OnboardingWizard.tsx` | lines 20-166 | `STEPS`; `OnboardingWizard`; `onComplete` | `OnboardingWizardProps` | ACCEPT |
| A second delayed four-step Home tour uses a separate storage key | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OnboardingTour.tsx` | lines 6-145 | `STORAGE_KEY`; `TOUR_STEPS`; `OnboardingTour` | Home contextual tour | ACCEPT |
| Global shell owns first-run display and preserves completion state | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useModals.ts` | lines 16-34 | `showOnboarding`; `handleOnboardingComplete` | `useModals` | ACCEPT |
| Header exposes version, Tweaks, language, and theme in primary chrome | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | lines 66-175 | `CompactHeader`; `versionBadge`; `tweaksButton` | `CompactHeaderProps` | ACCEPT |
| Dashboard layout composes onboarding, header, sidebar, and main offset | RUNTIME_BEHAVIOR | canonical contract: direct current-source read of the dashboard route-group layout | lines 201-280 | `DashboardLayoutInner`; `CompactHeader`; `Sidebar` | dashboard route-group layout | ACCEPT |
| Canonical responsive, language, hierarchy, and progressive-disclosure rules exist | LITERAL_INVARIANT | canonical contract: `DESIGN.md` | sections 4, 7, 8, 9, 14.6 | responsive priority; natural Vietnamese; protected routes | CVF design contract | ACCEPT |

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | complete direct read before packet authoring |
| UI claim boundary | current-source Home/shell presentation, tests, and localhost evidence only |

## Claim Boundary

This baseline authorizes T3 dispatch only. It does not authorize API, auth,
store, provider, dependency, deployment, public-sync, production, or projection
mutation and does not claim hosted freshness.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired T3 work order | `DISPATCH_READY` with source evidence | PASS |
| Completion or reviewer artifact | future T3 completion review | N/A with reason: worker execution has not started | N/A with reason |
| Roadmap state | active UX roadmap | `ACTIVE_T3_DISPATCH_READY` | PASS |
| Registry JSON | corpus registry aggregate | current drift check | PASS |
| Registry Markdown | paired registry surface | existing governed surface | PASS |
| External evidence digest | future localhost evidence | N/A with reason: produced during worker execution | N/A with reason |
| System loop interlock | no system-loop change | N/A with reason: Web presentation dispatch | N/A with reason |
| Session continuity | active front door and handoff | N/A with reason: dispatch sync follows material commit | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T3 is private current-source Web remediation pending independent review.
