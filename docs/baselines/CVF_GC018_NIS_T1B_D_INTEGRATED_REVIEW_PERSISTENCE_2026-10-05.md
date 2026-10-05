# CVF GC-018 Baseline - NIS T1B Integrated Review Persistence

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-NIS-T1B-D

dispatchBaseHead: 5e42818cb4e88a618b0b612528fc351635ca23ea
providerExecutionAuthority: FORBIDDEN
Date: 2026-10-05

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator; delegated Local dispatcher

Reviewer owner: Local reviewer/closer

Worker target: distinct INTERNAL_AGENT implementation worker

## Purpose

Complete the existing app_builder_complete Intent-to-Spec review consumer with request-owned save/readback and an explicitly admitted private single-host storage profile. Reuse the checkpointed A/B/C contracts; close their actual UI/API and transaction-proof gaps as one bounded implementation, not another port-only completion. The target is saved content confirmation, not build-ready acceptance or BUILD authority.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NIS-T1B-D --title "NIS T1B Integrated Review Persistence" --date 2026-10-05 --base cc98c79657f86890624fc3a60becd0f2e8adfda3 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --stdout --include-worker-return-skeleton` |
| generatedProfile | web-ui-dashboard plus WORKER_MUST_NOT_COMMIT |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Source-verified consumer scope, checked source checkpoint 5e42818cb4e88a618b0b612528fc351635ca23ea, actor/profile/transaction acceptance, role graph, exact evidence and bounded helper families replaced generated stubs. |
| checkerReadAheadConfirmation | governance/compat/check_baseline_update_compat.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_artifacts.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_task_governance_route.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_markdown_structural_completeness.py |
| docOnlyNewFields | knownForeignDirtyPaths; seedEvidenceDisposition; profileAdmissionDisposition; no new machine enum or checker rule |
| claimBoundary | Dispatch admission only; implementation, independent probe and acceptance remain pending. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`reviewer`, role=`reviewer`, lifecyclePhase=`review`.
Command: `python -B governance/compat/run_adif_defect_resolver.py --task-class reviewer --role reviewer --lifecycle-phase review --json`.
Returned defects: NONE_RETURNED.
Actual resolver executed on 2026-10-05; totalCandidates=0, truncated=false. Worker resolves its own execution role before authoring return; no registry mutation.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_baseline_update_compat.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_artifacts.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_task_governance_route.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_markdown_structural_completeness.py |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; DISPATCH_READY; acceptance-ledger-json; Gate-To-Role Closeability Contract; High-Risk Local Transaction Proof Applicability; Returned defects: NONE_RETURNED; rawMemoryReleased=false |
| gateRunPurpose | Confirm source-verified bounded dispatch and role closeability before release; no implementation proof. |
| claimBoundary | Read-ahead concerns authoring and evidence shapes; never certifies runtime/security outcomes. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Current review and source revision | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts | synchronizeIntentSpecReview; buildReviewedDraftPacket | synchronizeIntentSpecReview; buildReviewedDraftPacket | existing Web consumer | ACCEPT |
| Portable byte-bound candidate | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-confirmation.ts | createSpecConfirmationCandidate; verifySpecConfirmationReadback | createSpecConfirmationCandidate; verifySpecConfirmationReadback | existing Web consumer | ACCEPT |
| Request actor owner | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-actor.ts | resolveIntentSpecActor; assertCurrentIntentSpecActor | resolveIntentSpecActor; assertCurrentIntentSpecActor | existing Web consumer | ACCEPT |
| Canonical admission and exact store-port readback | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-acceptance.ts | prepareIntentSpecAcceptance; commitIntentSpecAcceptanceCandidate | prepareIntentSpecAcceptance; commitIntentSpecAcceptanceCandidate | existing Web consumer | ACCEPT |
| Concrete immutable publication preimage | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-file-store.ts | FileIntentSpecAcceptanceStore | FileIntentSpecAcceptanceStore | existing Web consumer | ACCEPT |
| Actual request Auth.js integration | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts | verifySessionCookie | verifySessionCookie | existing Web consumer | ACCEPT |
| Existing review consumer | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/IntentSpecReview.tsx | IntentSpecReview | IntentSpecReview | existing Web consumer | ACCEPT |
| Existing confirmation consumer | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/IntentSpecConfirmation.tsx | IntentSpecConfirmation | IntentSpecConfirmation | existing Web consumer | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| New NIS-T1B-D paths | Exact new pair, input manifest and skeleton did not exist before authoring | ACCEPT |
| Token search | `rg -n "NIS.T1B.D|Integrated Review Persistence" docs CVF_SESSION` before authoring: no matches | ACCEPT |
| Collision decision | One new bounded integration dispatch; existing A/B/C remain preimage admissions, not closed dependencies | ACCEPT |

## Web/UI Claim Boundary (trigger stub)

Read DESIGN.md before implementation. Retain the existing bilingual operational design. Synthetic UI tests establish structure and content binding only; no AI governance, live identity, deployment or production readiness claim.

## Claim Boundary

rawMemoryReleased=false. Operator-authorized local source implementation and synthetic isolated filesystem/security fixtures only. No real project data/root configuration, provider/login call, BUILD authority, public export or reopening parked lanes. Independent probe and final acceptance belong to Local, not the worker.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation and review; no public-sync authorization.

## Scope / Target / Owner Boundary

One bounded implementation assignment governed by `docs/work_orders/CVF_AGENT_WORK_ORDER_NIS_T1B_D_INTEGRATED_REVIEW_PERSISTENCE_2026-10-05.md`. Worker owns only its listed Web NIS consumer/probe families and exact return/evidence artifacts. Local owns dispatch, independent review, commits and continuity. Read profile and transaction acceptance together; source checkpoint is not runtime acceptance.

## Decision / Baseline / Proposed Tranche

Operator authorizes Local orchestration/review and manually relayed internal implementation. NIS-T1B-D joins UI/API plus private-profile transaction proof. Build-ready remains the later target, not a grant in this assignment. No new module tree, engine, roadmap, dependency or real runtime/provider activation.

## Evidence / Verification Requirements

Bound full pre-dispatch/pre-implementation autorun, worker-return fast, requirement-linked focused tests and production-path transaction/security fixtures, then independent Local probe and review. Normal local commits; material and continuity separated; final clean nonempty committed closure before any acceptance claim.

## Epistemic Process Block

Expected Result / Prediction: source-owned current content can be privately saved/read without stale or cross-actor confirmation.
Evidence Comparison: checkpointed A/B/C synthetic proof exists; integration and independent security/profile acceptance pending.
Contradiction Or Gap Disposition: unsupported profile/proof blocks acceptance; do not weaken standard.
Claim Update: dispatch admission only, no complete T1B/S1 or build-ready claim.

## Current Runtime Freshness Verification

N/A_WITH_REASON - source-pinned dispatch with synthetic local tests only; no live identity/provider/deployment claim. Read actual source and host capabilities before implementation; do not infer runtime activation from source existence.

