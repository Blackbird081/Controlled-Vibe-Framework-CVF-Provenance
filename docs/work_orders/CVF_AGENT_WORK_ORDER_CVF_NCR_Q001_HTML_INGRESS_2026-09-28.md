# CVF Work Order - NCR Q001 HTML Ingress Repair

Memory class: governed-work-order

docType: work_order

Status: ACTIVE_BOUNDED

Batch ID: CVF-NCR-Q001-HTML-INGRESS

executionBaseHead: `97abcecc50b8f734376cec015b7e96b1126479d1`

workerReturnPath: `docs/reviews/CVF_CVF_NCR_Q001_HTML_INGRESS_RETURN_2026-09-28.md`

## Purpose

Execute the operator-authorized Q001 repair under `docs/baselines/CVF_GC018_CVF_NCR_Q001_HTML_INGRESS_2026-09-28.md` and roadmap D015/Q001. Local is the INTERNAL_AGENT source verifier, implementer and final technical decision owner; external Web is advisory only.

## Authority Chain

Operator instruction on 2026-09-28, NCR roadmap Q001/D015, paired GC-018 baseline, active handoff V63, then this bounded order. This order does not transfer the operator's effect/data/cost authority.

## Agent Roles

Local INTERNAL_AGENT implements and returns source evidence; a distinct Local reviewer/closer evaluates before material commit. EXTERNAL_AGENT_CLI_MCP is advisory with no invocation in this tranche. Operator owns pilot admission.

## Allowed / Forbidden Scope

Allowed: exact source/test/doc paths listed in this order. Forbidden: live provider/effect, external runtime, deployment, public-sync, P11, broad scan and unapproved configuration/data access.

## Required First Reads

Read active bootstrap, front door and handoff; external-local role owners; guard orientation and literal gotchas; accepted NCR W00-W02 source packets; DESIGN.md; targeted route/helper/panel and tests.

## Pre-Flight Checks

Confirm base HEAD and clean starting status; read applicable checker source and exact owner files; preserve P11 and the 52-deferred lane. Use the accepted source evidence without duplicate survey.

## Write Ownership

Worker owns the existing export route/helper, panel, focused tests, browser fixture and pending return. Dispatcher owns baseline/work order; Local reviewer owns roadmap disposition and closure. Worker does not commit.

## Source Verification Block

| Decision | Source | Verified fact |
|---|---|---|
| ACCEPT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | Current route coerces memoryClass, scans sourceContent only, and returns success independently of receipt decision. |
| ACCEPT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | Receipt helper defaults missing decision to ALLOW. |
| ACCEPT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | Present receipt badge says Governed for any returned decision. |
| ACCEPT | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | Q001 keeps P06/P08/profile/walkthrough open; D015 selects no external runtime for this HTML slice. |

## Allowed Work

Edit the named route, helper, panel and focused tests. Reject malformed input before effect, make receipt parsing fail closed, mark preview as draft/unaccepted, and show decision without claiming final acceptance. Record secret-safe profile limits and verification. Use synthetic inputs only.

## Forbidden Work

No provider/live call, P11, OMP/OMC/AKI/QM adapter, deployment, public export, raw environment value, ledger inspection or automatic Q001 closure. Operator owns pilot effect/data/cost checkpoint.

## Acceptance

Negative fixtures for invalid type/size/secret metadata and malformed/denied receipts; valid HTML remains usable as a draft; component presents missing/DENY distinctly. Offline checks and source review do not constitute live governance proof.

## Acceptance Criteria

The focused negative/positive fixtures pass, the synthetic browser shows draft state, and the implementation preserves no-final-acceptance semantics. Reviewer assesses exact changed set and source evidence before any commit.

## Execution Plan

Repair validation and receipt interpretation, update UI state, run focused tests/typecheck/mock browser, return bounded evidence, then submit to distinct Local review.

## Evidence Requirements

Record exact changed paths, focused test/typecheck/browser results, receipt shape source, secret-safe profile presence, open deployment unknowns and no-live claim.

## Review Gate

Run worker-return and reviewer-fast gates; reviewer evaluates evidence rather than recreating implementation. Any unclosed gate blocks commit.

## Closure Checklist

Only after reviewer acceptance: update roadmap disposition, run commit steward preflight, commit material paths, then separately sync active continuity if the next move changes.

## Return-To-Orchestrator Conditions

Return COMPLETE_PENDING_REVIEW with code/tests/evidence; if source contradiction or authorization gap arises, return a named blocker without widening scope.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gc018_stop_boundary_semantics.py`; `governance/compat/check_independent_review_probe_admission.py` |
| literalTokensReviewed | `Authority Chain`, `Agent Roles`, `Review-Dispatch Convergence Control: REQUIRED`, `independentProbeRequired`, `Public Export Disposition` |
| gateRunPurpose | Confirmation of authored work-order evidence, not first discovery of required shape. |
| claimBoundary | Source read-ahead does not prove dispatch or live run readiness. |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-Q001-HTML-INGRESS
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-q001-html-ingress","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Independent Review Probe Admission Contract

independentProbeRequired: NOT_APPLICABLE_WITH_REASON: focused offline tests and synthetic browser evidence are source-repair checks, while live governance proof remains explicitly unclaimed and parked.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | bounded Q001 source repair; no P11, provider/live or public action |

## Agent Handoff Contract Control Block

Contract source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

dispatchBaseHead: `97abcecc50b8f734376cec015b7e96b1126479d1`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one internal worker followed by distinct Local reviewer/closer |
| phase | bounded Q001 implementation pending review |
| baseHeadFor(phase) | executionBaseHead=`97abcecc50b8f734376cec015b7e96b1126479d1`; closureBaseHead=reviewer capture |
| changedSetScope(phase) | named source/test/doc files only |
| traceScope(phase, actor) | worker return records source and verification; Local reviewer evaluates |
| commitOwner(phase) | worker forbidden; Local closer after acceptance |
| crossBatchIsolation | P11 and external runtime lanes parked; no stash/reset/clean |
| nextMoveSurfaces | pending return then reviewer decision; active continuity only if next move changes |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | CVF-NCR-Q001-HTML-INGRESS, 2026-09-28 |
| Working directory | repository root |
| Command or tool surface | governed reads, Git and focused local checks |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator instruction, roadmap Q001/D015 and paired baseline |
| Before status evidence | clean worktree at `97abcecc5` |
| After status evidence | exact bounded delta staged pending review |
| Diff evidence | source/test/doc changed set in pending return |
| Approval boundary | no pilot effect, cost, provider/live or public-sync |
| Claim boundary | local source repair and synthetic proof only |
| Agent type | dispatcher |
| Invocation ID | cvf-ncr-q001-html-ingress-20260928 |
| Expected manifest | N/A with reason: dispatch trace does not enumerate future worker outputs; the bounded worker paths are declared above. |
| Actual changed set | N/A with reason: the dispatch trace does not claim to be the worker return's final changed-set ledger. |
| Manifest delta | N/A with reason: compare the worker's actual changed set at the review phase. |

## Claim Boundary

This work order is a bounded source repair, not a pilot or release-quality proof.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Operator Checkpoint

The operator retains decisions on actual pilot data, where it travels, retention, expense limits and any real service invocation. This document records a bounded local coding task. The later pilot decision needs a concrete deployment profile and a separately reviewable evidence package before it can proceed.

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - this source repair does not authorize operating-system security mutation, cross-process locking, durable transaction migration or rollback tooling.
