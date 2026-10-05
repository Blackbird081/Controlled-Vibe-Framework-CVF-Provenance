# CVF GC-018 Baseline - NIS T1B Integrated Review Persistence

Memory class: governed-dispatch-baseline

Status: HOLD_OPERATOR_CHECKPOINT

Batch ID: CVF-NIS-T1B-D

dispatchBaseHead: 5e42818cb4e88a618b0b612528fc351635ca23ea
providerExecutionAuthority: FORBIDDEN
Date: 2026-10-05

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator; delegated Local dispatcher

Reviewer owner: Local reviewer/closer

Worker target: distinct INTERNAL_AGENT implementation worker

## Consolidated Rework Admission

reworkAdmissionStatus: HOLD_OPERATOR_CHECKPOINT
priorFindingSetDigest: 8cd7769b5b2ed9c2e899ec9b54bce7150f929d74f94954acf29d82991eae62f3
Evidence: `docs/reviews/evidence/cvf-nis-t1b-d-rework-admission-2026-10-05.json`. This amendment controls rework round 1 of the same CVF-NIS-T1B-D assignment. The original worker checkout and frozen R0 return remain untouched and unaccepted. Do not execute or redispatch from this held packet.

| Finding | Owner / minimum outcome | Targeted evidence |
|---|---|---|
| F1 HIGH | Worker makes hardening initialization exception-safe, including ambiguous subprocess failure after ACL mutation and restoration failure | Actual production helper regression before rollback handle return; real semantic rollback/readback and subsequent peer acquisition |
| F2 HIGH | Worker binds save/reopen display and late receipts to the canonical authenticated session lifecycle, including A-B-A | Session switch/logout/loading/expiry regressions plus existing review/language/reviewer generation checks; no protected auth-owner edits |
| F3 MEDIUM | Local registry owner registers exactly the five returned probe files by source entry and generator | Direct coverage assertion for every exact path, including mjs and ps1; worker remains forbidden to edit registry/checkers |
| F4 LOW | Worker binds the actual saved gate-log bytes and freezes a new R1 return around the final required gate | Raw file SHA256; preserve R0 return and receipt as historical evidence |
| B1 BLOCKER | Local reviewer owns real WRONG_OWNER fixture proof after the named authority checkpoint | Actual differing owner, independent complete semantic PRE/POST plus content/existence; no synthetic security success or waived field |

Independent structural diagnostic verified 20 numeric pins and reproduced F1; it does not fulfill the real-security independent proof. Original test receipts are consumed, not broadly rerun. Full contract/schema/path/authority/test/range/commit-plan dependency audit is bound in the evidence JSON before any repair. The expected pending worker preimage is pinned there; a dirty tree must not be called clean.

Checkpoint NIS-T1B-D-WRONG-OWNER-FIXTURE requests one Local elevated Windows helper solely on a marked, caller-created, private OS-temp fixture: assign namespace owner to S-1-5-32-544, let the ordinary unprivileged production probe measure/refuse the actual mismatch and compare semantic PRE=POST plus exact content/existence, then restore the captured original owner. Validate containment and every ancestor against reparse points. No account creation or real store/configuration change. Failed restoration retains the isolated fixture and diagnostics. No privileged operation is authorized by this held proposal.

After checkpoint resolution, Local materializes `docs/corpus-intelligence/registry/entries/nis-t1b-d-private-profile-probes.json` and regenerates the registry, then updates the role graph and actual evidence/pins before release. Do not remove HRLTP fields, lower the claim contract, or rename files as a coverage workaround. Worker R1 outputs use distinct return/evidence paths; original R0 bytes stay frozen. Rework release requires committed pair, matched continuity, exact source/fixture preimage pins, full pre-dispatch PASS and a new bound pre-implementation PASS. No worker staging/commit; no main/worker implementation merge now.

## Purpose

Complete the existing app_builder_complete Intent-to-Spec review consumer with request-owned save/readback and an explicitly admitted private single-host storage profile. Reuse the checkpointed A/B/C contracts; close their actual UI/API and transaction-proof gaps as one bounded implementation, not another port-only completion. The target is saved content confirmation, not build-ready acceptance or BUILD authority.

## Scaffold Provenance Block

Initial scaffold retained from committed packet b2016e35a4b11043524ac51c26a49121309391cc; current manual amendment is a held consolidated rework admission, not initial dispatch or completed repair.

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NIS-T1B-D --title "NIS T1B Integrated Review Persistence" --date 2026-10-05 --base cc98c79657f86890624fc3a60becd0f2e8adfda3 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --stdout --include-worker-return-skeleton` |
| generatedProfile | web-ui-dashboard plus WORKER_MUST_NOT_COMMIT |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Source-verified consumer scope, checked source checkpoint 5e42818cb4e88a618b0b612528fc351635ca23ea, actor/profile/transaction acceptance, role graph, exact evidence and bounded helper families replaced generated stubs. |
| checkerReadAheadConfirmation | governance/compat/check_baseline_update_compat.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_artifacts.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_task_governance_route.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_review_cost_control.py; governance/compat/check_changed_corpus_registry_coverage.py; governance/compat/check_corpus_scan_registry.py |
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
| applicableCheckersRead | governance/compat/check_baseline_update_compat.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_artifacts.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_task_governance_route.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_review_cost_control.py; governance/compat/check_changed_corpus_registry_coverage.py; governance/compat/check_corpus_scan_registry.py |
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

