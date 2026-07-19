# CVF GC-018 Baseline - CVF Web UX T2 Language And Guided Knowledge Journey

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-WEB-UX-T2

Dispatch base head: `409099f63`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: delegated implementation worker

## Purpose

Pin the current five-route Web language and journey seams before T2 replaces
mixed internal vocabulary with outcome-first copy and adds a visible,
route-preserving knowledge-to-review-to-handoff journey.

## Decision/Baseline/Proposed Tranche

- Decision: release bounded T2 current-source Web implementation.
- Baseline: five existing routes, their current copy owners, and their runtime
  behavior seams at dispatch base `409099f63`.
- Proposed tranche: CVF-WEB-UX-T2 only; T3-T4 and all hosted/deployment/public
  lanes remain parked.

## Evidence/Verification

Direct source reads verified each page owner, copy object, API call site,
validator seam, export component, and the canonical design contract. Worker
must recompute these invariants before editing and reviewer must recompute them
again before closure.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition |
|---|---|---|---|
| T1 source UX | `docs/reviews/CVF_WEB_UX_T1_COMPLETION_2026-07-19.md` | `d4e6e48a0` | `CLOSED_PASS_BOUNDED` |
| T1P hosted/current diagnosis | `docs/reviews/CVF_WEB_UX_T1P_COMPLETION_2026-07-19.md` | `45d505836` | `CLOSED_PASS_BOUNDED`; deployment remains parked |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T2 --title "CVF Web UX T2 Language And Guided Knowledge Journey" --date 2026-07-19 --base 409099f63 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit Web/UI profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added dependency release, direct source manifest, exact scope, design boundary, and browser-evidence requirements |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py` |
| docOnlyNewFields | none |
| claimBoundary | scaffold provenance only; no implementation, browser acceptance, hosted, or deployment claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`web-ui-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "web-ui-implementation" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | standard UI, evidence, and no-commit controls apply |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status; dependency evidence; source verification columns; no-commit conversion; ADIF literal; scaffold command; changed-set boundary |
| gateRunPurpose | confirm dispatch structure after direct source and design-contract reads |
| claimBoundary | checker compliance confirms packet shape only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Help route derives visible cards and steps from bilingual content | RUNTIME_BEHAVIOR | canonical contract: direct current-source read of help `page.tsx` under the dashboard route group | lines 12-30 | `HelpPage` | `HELP_CONTENT` consumer | ACCEPT |
| Help bilingual content exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/help-content.ts` | line 41 onward | `HELP_CONTENT` | `Record<Lang, HelpContent>` | ACCEPT |
| Knowledge governance route owns mixed bilingual labels | EXISTS | canonical contract: direct current-source read of governance knowledge `page.tsx` under the dashboard route group | lines 44-87 | `LABELS`; `KnowledgeGovernancePage` | page-local label contract | ACCEPT |
| Governance route calls three existing lifecycle APIs plus ingest | RUNTIME_BEHAVIOR | canonical contract: same direct governance knowledge page read | lines 129, 162, 181, 193 | `fetch` call sites | current route handlers | ACCEPT |
| Intake route owns bilingual copy and submits collections | RUNTIME_BEHAVIOR | canonical contract: direct current-source read of knowledge intake `page.tsx` under the dashboard route group | lines 8-120 | `COPY`; `KnowledgeIntakePage`; collection fetch | page-local copy and submit handler | ACCEPT |
| Intake links to review packet export | LITERAL_INVARIANT | canonical contract: same direct knowledge intake page read | line 183 | `/artifacts` | Next Link | ACCEPT |
| Artifact route owns bilingual review-packet copy | EXISTS | canonical contract: direct current-source read of artifacts `page.tsx` under the dashboard route group | lines 8-117 | `COPY`; `ArtifactsPage`; `ArtifactExportPanel` | page plus existing export component | ACCEPT |
| Transfer route owns bilingual copy and handoff validation | RUNTIME_BEHAVIOR | canonical contract: direct current-source read of work-transfer `page.tsx` under the dashboard route group | lines 11-140 | `COPY`; `WorkTransferPage`; `validateHandoff` | existing handoff validator and audit fetch | ACCEPT |
| Canonical UI language and journey rules exist | LITERAL_INVARIANT | canonical contract: `DESIGN.md` | sections 4, 7, 8, 9, 14.6 | form workflow order; responsive priority; natural Vietnamese; protected routes | CVF design contract | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Baseline path | `Test-Path` returned false before authoring | ADD |
| Work-order path | `Test-Path` returned false before authoring | ADD |
| Worker-return path | `Test-Path` returned false before authoring | ADD |
| Completion path | `Test-Path` returned false before authoring | ADD |
| Collision decision | no existing T2 packet family was found | SAFE_TO_AUTHOR |

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | complete direct read before packet authoring |
| UI claim boundary | current-source copy, navigation, tests, and localhost evidence only; no hosted freshness or production-readiness claim |

## Claim Boundary

This baseline authorizes T2 packet dispatch only. It does not authorize API,
store, parser, role, provider, deployment, public-sync, production, or
continuous-projection mutation.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired T2 work order | `DISPATCH_READY` with dependency and source evidence | PASS |
| Completion or reviewer artifact | future T2 completion review | N/A with reason: worker execution has not started | N/A with reason |
| Roadmap state | active UX roadmap | `ACTIVE_T2_PACKET_AUTHORIZED` | PASS |
| Registry JSON | corpus registry aggregate | current drift check | PASS |
| Registry Markdown | paired registry surface | existing governed surface | PASS |
| External evidence digest | future localhost evidence | N/A with reason: produced during worker execution | N/A with reason |
| System loop interlock | no system-loop change | N/A with reason: Web presentation dispatch | N/A with reason |
| Session continuity | active front door and handoff | N/A with reason: final dispatch sync follows packet commit | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T2 is private current-source Web remediation pending independent review.
