# CVF GC-018 Baseline - CVF Web UX T4 Browser Acceptance And Roadmap Closure

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-WEB-UX-T4

Dispatch base head: `5be9d3490`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: delegated browser-audit worker

## Purpose

Pin the accepted T1-T3 current-source UX and the exact browser evidence needed
for a final multi-viewport, theme, accent, navigation, focus, overflow,
primary-action, state, and audience-disclosure audit before bounded roadmap
closure can be considered.

## Decision/Baseline/Proposed Tranche

- Decision: release read-only T4 localhost browser acceptance.
- Baseline: T1, T1P, T2, and T3 are independently closed bounded; T3 material
  closure is `114daa54a` and its session sync is `5be9d3490`.
- Proposed tranche: current-source audit outputs only. Source repair, hosted
  mutation, deployment, public-sync, provider/live, production, and continuous
  projection remain parked.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| T1 | `docs/reviews/CVF_WEB_UX_T1_COMPLETION_2026-07-19.md` | `d4e6e48a0` | `CLOSED_PASS_BOUNDED` |
| T1P | `docs/reviews/CVF_WEB_UX_T1P_COMPLETION_2026-07-19.md` | `45d505836` | `CLOSED_PASS_BOUNDED`; hosted mechanism unresolved |
| T2 | `docs/reviews/CVF_WEB_UX_T2_COMPLETION_2026-07-19.md` | `bb1418554` | `CLOSED_PASS_BOUNDED` |
| T3 | `docs/reviews/CVF_WEB_UX_T3_COMPLETION_2026-07-19.md` | `114daa54a` | `CLOSED_PASS_BOUNDED`; T4 packet authoring released |

## Evidence/Verification

Direct source reads verified the Home, Workspace, knowledge journey, sidebar,
theme, accent, and preferences owners at dispatch base. The worker must run the
current source, capture original browser evidence, and leave source unchanged.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T4 --title "CVF Web UX T4 Browser Acceptance And Roadmap Closure" --date 2026-07-19 --base 5be9d3490 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus read-only Web/browser audit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added accepted dependencies, route-anchor evidence rule, viewport/theme matrix, read-only failure route, and hosted boundary |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py` |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no browser acceptance or roadmap closure claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-browser-audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-browser-audit" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | exact route identity, visible anchors, durable screenshots, and no-source-mutation controls are explicit |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | ready status; dependency evidence; source verification columns; ADIF query; no-commit conversion; exact changed-set boundary |
| gateRunPurpose | confirm dispatch shape after current source and design-contract reads |
| claimBoundary | checker compliance confirms packet shape only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Home route owns the task-first landing state | EXISTS | canonical contract: direct current-source read of the dashboard Home page | line 85 | `HomePage` | dashboard Home route | ACCEPT |
| Workspace owns ordinary and advanced disclosure | RUNTIME_BEHAVIOR | canonical contract: direct current-source read of the dashboard Workspace page | lines 122-167 | `WorkspacePage`; `advanced-detail` | Workspace route | ACCEPT |
| Help route exists | EXISTS | canonical contract: direct current-source read of the dashboard Help page | line 13 | `HelpPage` | Help route | ACCEPT |
| Knowledge governance route exists | EXISTS | canonical contract: direct current-source read of the dashboard Knowledge page | line 90 | `KnowledgeGovernancePage` | Knowledge route | ACCEPT |
| Knowledge intake route exists | EXISTS | canonical contract: direct current-source read of the dashboard Intake page | line 86 | `KnowledgeIntakePage` | Intake route | ACCEPT |
| Review artifact route exists | EXISTS | canonical contract: direct current-source read of the dashboard Artifacts page | line 68 | `ArtifactsPage` | Artifacts route | ACCEPT |
| Work transfer route exists | EXISTS | canonical contract: direct current-source read of the dashboard Transfer page | line 120 | `WorkTransferPage` | Transfer route | ACCEPT |
| Sidebar owns advanced operations disclosure | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | lines 49 and 222 | `Sidebar`; `advanced-operations` | dashboard navigation | ACCEPT |
| Header owns theme, accent, and preferences | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/CompactHeader.tsx` | lines 67-265 | `CompactHeader`; `setTheme`; `updateTweaks` | compact header | ACCEPT |
| Canonical visual acceptance rules exist | LITERAL_INVARIANT | canonical contract: `DESIGN.md` | sections 4, 7, 8, 9, 14.6 | responsive priority; visible focus; progressive disclosure | CVF design contract | ACCEPT |

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | complete direct read before packet authoring |
| UI claim boundary | current-source localhost browser audit only |

## Claim Boundary

This baseline authorizes T4 read-only browser audit outputs. It does not
authorize source repair, hosted mutation, deployment, public-sync, provider or
live calls, production action, or continuous-projection execution.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired T4 work order | `DISPATCH_READY` with source evidence | PASS |
| Completion or reviewer artifact | future T4 completion review | N/A with reason: audit has not started | N/A with reason |
| Roadmap state | active UX roadmap | `ACTIVE_T4_PACKET_AUTHORIZED` | PASS |
| Registry JSON | corpus registry aggregate | current drift check | PASS |
| Registry Markdown | paired registry surface | existing governed surface | PASS |
| External evidence digest | future localhost evidence | N/A with reason: repository-local evidence produced during audit | N/A with reason |
| System loop interlock | no system-loop change | N/A with reason: browser audit dispatch | N/A with reason |
| Session continuity | active front door and handoff | N/A with reason: dispatch sync follows material commit | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T4 audits private current source; hosted deployment and public export remain separate.
