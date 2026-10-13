# CVF GC-018 Baseline - NCR Result Export Feedback

Memory class: governed-dispatch-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-13
Batch ID: CVF-NCR-RESULT-EXPORT-FEEDBACK-20261013
Inspection base: `5c8bd0a5f3aa88edbaf14eab019d25b2ec36af13`
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Select one finite NCR R1 result-recovery gap: PDF and Word exports currently catch failures in `ResultViewer` and log them, without showing the user an actionable failure. Add accessible English/Vietnamese failure feedback and a same-run retry while preserving the result, run, receipt, and successful export behavior. This is a private offline UI contribution, not full R1/R2 completion or an NCR pilot exit.

## Decision / Proposed Tranche

One internal no-commit, 60-minute implementation tranche follows a materially bound dispatch. Root retains reviewer/closer and all authority/continuity decisions. This document remains a draft hold until binding.

## Evidence

Source inspection at the stated HEAD confirms the two logging-only catch paths and existing deferred isolation tests; exact symbols and lines appear below. No test or export behavior is claimed by this packet.

## Scope / Target / Owner Boundary

The released worker may modify the v1.6 `ResultViewer.tsx` and its two existing sibling tests, and may add one `ResultExportControls.tsx` helper plus one focused `ResultViewer.export-feedback.test.tsx` regression file within the same component family. Worker evidence and return paths are fixed in the paired order. The worker must not stage or commit. Local reviewer/closer owns dispatch release, independent review, any GC-051 new-test registry source item and regeneration, material commit, and dedicated current-SHA continuity. No product route, API, storage, dependency, provider, send, clipboard, Markdown export, or broad result refactor is admitted.

## Design Control Gate

For each selected export, a failure belongs only to the mounted run and the newest export token. Keep the failure visible after the menu closes, provide the affected format and a direct retry action, and expose it via an accessible live alert. A retry clears only its own failure at start. A stale A completion after B mounts, or an older same-run completion after a newer export, must not set or clear B/current failure or busy state. Never display raw exception details. Existing output, receipt, run actions, successful download and analytics behavior remain intact. Reuse the existing export language preference for EN/VI text. PDF and Word have distinct failure controls; clipboard and Markdown are outside this tranche.

## Acceptance Criteria

| ID | Observable requirement |
|---|---|
| REQ-FAILURE | A forced PDF or Word save failure produces a localized, accessible, format-specific message with direct retry; raw exception text is absent; result and receipt remain present. |
| REQ-RETRY | Same-run retry clears its own failure and a successful save completes with existing success behavior; the other format's failure is not cleared incidentally. |
| REQ-ISOLATION | Deferred failure from run A after mounting B, and older same-run completion after a newer export, cannot change current failure or busy state. Include a competing same-run completion negative control. |
| REQ-MAINTAINABILITY | Proactively extract a cohesive export controls/labels region into the named helper so `ResultViewer.tsx` is at least 50 lines shorter than the 941-line inspection base; no behavior changes outside selected export feedback. |
| REQ-RETURN | Red baseline then green focused tests, type check, scoped lint, truthful proof IDs, changed-set reconciliation and worker return fast gate; zero provider calls. |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Run-keyed body and export sequence | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.tsx` | 69-92 | `ResultViewerBody`, `exportSeq` | ResultViewer | ACCEPT |
| PDF failure and menu finalization | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.tsx` | 283-381 | PDF export catch/finally | ResultViewer | ACCEPT |
| Word failure and menu finalization | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.tsx` | 383-522 | Word export catch/finally | ResultViewer | ACCEPT |
| Existing error tests assert console only | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.test.tsx` | 413-423; 477-487 | PDF/Word error tests | component tests | ACCEPT |
| Existing deferred run isolation tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.isolation.test.tsx` | 228; 331-397 | deferred Word export suite | component isolation tests | ACCEPT |
| R1 remains partial | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | 19-29; 88-90 | R1 journey and current continuation | NCR roadmap | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | Checker Source Read-Ahead Block; acceptance-ledger-json; gateId, mustPassBy, repairOwner, mutationSurface; dispatchKind INITIAL |
| gateRunPurpose | Draft shape confirmation before Root material binding and bound dispatch; no gate PASS asserted. |
| claimBoundary | Read-ahead confirms listed predicates only; Root must complete full pre-dispatch read/gate. |

## Epistemic Process Block

- Expected Result / Prediction: visible format-specific failure and retry will let a user recover from a failed local export without losing the result.
- Evidence Comparison: current catch paths log; existing tests assert console calls and no visible recovery.
- Contradiction Or Gap Disposition: selected source has no visible failure control; negative races require new focused tests.
- Claim Update: proposal and source pin only; no implementation result yet.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`dispatch`
Resolver command: `python -B governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase dispatch`
Returned defect count: 0
Returned defects: NONE_RETURNED
Dispatch impact: preserve scoped checks and truthful evidence.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-RESULT-EXPORT-FEEDBACK-20261013 --title "NCR Result Export Feedback" --date 2026-10-13 --base 5c8bd0a5f3aa88edbaf14eab019d25b2ec36af13 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key ncr-result-export-feedback --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | web-ui-dashboard, internal no-commit INITIAL |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Bound source facts, selected R1 failure/retry design, finite tests and maintainability extraction. |
| checkerReadAheadConfirmation | Four checker sources above inspected for applicable literal tokens. |
| docOnlyNewFields | None. |
| claimBoundary | Dispatch drafting only. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local INTERNAL_AGENT orchestrator/reviewer dispatch owner |
| Provider or surface | shared private workspace |
| Session or invocation | ncr-result-export-feedback-packet-20261013 |
| Working directory | repository root |
| Command or tool surface | targeted source/standards reads; scaffold; draft authoring |
| Target paths | `docs/baselines/CVF_GC018_NCR_RESULT_EXPORT_FEEDBACK_2026-10-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_RESULT_EXPORT_FEEDBACK_2026-10-13.md`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | operator NCR continuation and Root bounded selection |
| Before status evidence | inspection HEAD `5c8bd0a5f3aa88edbaf14eab019d25b2ec36af13`; clean at intake |
| After status evidence | exact8 packet/source-generated material admission; final actual-SHA continuity and bound release follow |
| Diff evidence | `git diff --name-status` at handoff |
| Approval boundary | offline UI, zero provider budget |
| Claim boundary | packet draft, no execution proof |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-result-export-feedback-packet-20261013 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_RESULT_EXPORT_FEEDBACK_2026-10-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_RESULT_EXPORT_FEEDBACK_2026-10-13.md`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_RESULT_EXPORT_FEEDBACK_2026-10-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_RESULT_EXPORT_FEEDBACK_2026-10-13.md`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH exact8 required before commit |
| Deletion or rename disposition | N/A with reason: none planned |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private NCR UI dispatch preparation.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Root dispatch/closure material projection and dedicated actual-SHA exact-six continuity; worker has no authority to edit these protected paths.
Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
Operator authorization: 2026-10-13 NCR continuation with Root Local dispatch/review/closure ownership.
Rollback boundary: this packet and future bounded continuity only; preserve accepted NCR evidence and parked effects.

## Claim Boundary

R1/R2 remain partial, R3/R4 open, R5/R6 deferred. Real-data writer/custody/business acceptance, send/B2, P11, public and deployment stay parked. No live-governance claim or provider budget follows from this packet.
