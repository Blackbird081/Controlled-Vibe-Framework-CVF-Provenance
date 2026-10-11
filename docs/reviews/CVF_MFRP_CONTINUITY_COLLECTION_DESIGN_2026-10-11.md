# MFRP Material Continuity Collection Design - Proposal

Memory class: governed-design

docType: review

Status: DESIGN_PROPOSAL_PENDING_LOCAL_REVIEW

Date: 2026-10-11

Batch ID: CVF-MFRP-CONTINUITY-COLLECTION-DESIGN-20261011

Dispatch base head: 0e5de48d040c44a76cd729565d9780b8c50207d1

executionBaseHead: 2575d3e5d0497c1fb392c313fb35038c6fa6c1c9

Commit mode: WORKER_MUST_NOT_COMMIT

rawMemoryReleased=false

Companion evidence: `docs/reviews/evidence/mfrp-continuity-collection-design-worker-20261011.json`

## Purpose

Decide whether the existing MFRP P2 producer, P4-C1 collector and material/continuity fingerprint owners can safely recover collection for the real S2-R3 case, in which a reviewed material commit was skipped with `SKIPPED_NO_COMMITTED_EVIDENCE`. The design keeps the fail-closed fingerprint behaviour, selects one disposition, and lists the owner changes that a future decision would need. It is not an implementation, not a receipt rewrite, not a sample promotion, and not a model benchmark.

## Target / Source

| Item | Source and identity |
|---|---|
| Material commit | `0ab461e2b807a33984a4f8357140f5d28988fd23`; parent `6ed5646236858413f0696bdd10169e6cb135118b` |
| Continuity commit | `0e5de48d040c44a76cd729565d9780b8c50207d1` |
| Frozen case | `docs/reviews/evidence/mfrp-continuity-collection-design-dispatch-case-20261011.json` (raw sha `6cec4aa6...`) |
| Committed-evidence contract | `docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md` (sha `57ee1b05...`) |
| Fingerprint helper | `governance/compat/committed_evidence_fingerprint.py` (sha `39feb312...`) |
| Producer | `governance/compat/run_agent_autorun_workflow_gate.py` (sha `8d28ac30...`) |
| Collector | `governance/compat/mfrp_shadow_canary_autocollect.py` (sha `7002f9e0...`) |
| Canonical receipt reader | `governance/compat/agent_automation_machine_verification_readout.py` (sha `ff6088bf...`) |
| Bounded retry owner | `docs/reviews/CVF_MFRP_P4_C1_BOUNDED_RETRY_RECOVERY_COMPLETION_2026-09-27.md` (sha `f4194852...`) |
| Semantic acceptance of the material | `docs/reviews/CVF_MODEL_SELECTION_S2_R3_PROJECTION_COMPLETION_2026-10-11.md` (sha `8f5dc02e...`) |

Each claim below names the artifact that supplies it. Pin matches are identity checks only; they do not establish that a source was read in full.

## Scope / Methodology

Startup order was followed. The work order, the committed-evidence contract, the retry completion and the frozen case were read in full. The fingerprint helper's verification and identity functions, the readout reader, the collector's receipt validation, candidate and retry selection, and the producer's committed-evidence branch were read as named bodies. Roadmap, completion and collection-ledger sections were located and read as targeted sections. The pre-implementation gate passed at the execution base before any output existed.

Method: (1) validate the two frozen raw receipts with the canonical reader on disposable copies, without changing the frozen case; (2) reconcile the three overlapping paths against their committed blobs; (3) run four isolated Git fixture probes through the real helper with explicit SHAs and an explicit working directory; (4) compare three options against feasibility, authority, fraud negatives, marginal value, rollback and cost.

Probe results and their source are recorded in the companion evidence. No probe touched the source repository, its Git configuration, the journal, the safety marker or any receipt.

## Findings / Position

Finding 1 - the fail-closed behaviour is correct. The historical material target is refused at the current worktree because later commits changed three overlapping paths. Real-repo verification of `6ed5646..0ab461e` returns false with the reason `worktree content at 'CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json' does not match 0ab461e2b...'s committed blob`. The contract's guard 3 is the source of this refusal.

Finding 2 - the continuity binding is genuine. The frozen continuity receipt declares a `committedEvidence` object whose fingerprint `3aaa07f9...` recomputes exactly from the Git objects of `0ab461e..0e5de48`. Its raw bytes match the frozen raw hash, and the canonical reader accepts it.

Finding 3 - the three overlapping paths are real and their raw blob identities match the case. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, `CVF_SESSION/ACTIVE_SESSION_STATE.json` and `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` are changed by both the material range and the continuity range. The material closure receipt (`6ed5646..0ab461e`) declares no binding, and the frozen case does not record why.

Finding 4 - the gap is structural for session-sync materials. The collector regenerates a receipt for a trusted commit at the next disclosure, so the gate reads the bytes of that later worktree. Guard 3 then cannot admit the material's historical target whenever the next session-sync commit changes any path the material also changed. The existing owner already names this mismatch: the retry completion's finding `HISTORICAL_REPLAY_MISMATCH` selects only replayable items and leaves unreplayable evidence visible and unconsumed.

Finding 5 - the generated receipt is still a PASS for the requested range. Guard 3 denies provenance, but it does not stop the gate from producing a legacy PASS receipt that names `base..head` while reading later bytes. The collector treats that receipt as a legacy skip, so the risk is contained today. It is recorded as a standing risk, not changed here.

Finding 6 - continuity admissibility is time-dependent. The case captured the continuity target as true at `0e5de48d0`. At the current HEAD `2575d3e5d`, the same check returns false, because the packet commits `9afd2165a` and `2575d3e5d` changed the same continuity files. A current-HEAD check cannot demonstrate continuity admissibility for an older range.

Position: the existing machinery already does what the work order asks of a safe design. It refuses the wrong target, keeps the unreplayable item visible and unconsumed, and does not consume a retry it cannot replay. No small contract change is needed to make this case collectable without weakening a guard, and the only candidate that would collect it re-executes history. The recommendation below follows from that.

## Option Comparison

| Option | Feasibility | Authority and conflicts | Fraud negatives | Marginal collection value | Cost and rollback | Verdict |
|---|---|---|---|---|---|---|
| 1. Retain explicit skip (`SKIPPED_NO_COMMITTED_EVIDENCE`) | implemented; retryable class; not replayable now | no authority change; matches the accepted retry design (unreplayable items stay visible and unconsumed) | none new | zero new rows for this material; the material's acceptance is already recorded in its completion | no cost; no rollback needed | SELECTED for this case |
| 2. Inspect exact historical material in an isolated target | possible with a clean isolated checkout of `6ed5646..0ab461e`, but the collector would then run the whole pre-closure bundle again in a new environment | a re-executed bundle is a new attempt, not the original closure execution; needs a new admission class and conflicts with the no-historical-replay rule | selection bias: a re-run could pass where the original did not, unless every attempt is recorded | adds one row for one material; no evidence that the re-run matches the original execution | repeated full bundle per material; rollback removes the isolated path only | DEFERRED_WITH_REASON |
| 3a. Reuse a closure-time receipt that already carries a valid binding for the exact trusted range | works only if the material's own closure receipt carries a binding | does not help this case (Finding 3: that receipt has none); reopens the existing rule that stale phase files do not compete | stale or replayed receipts, forged bindings, receipts from a dirty tree | prevents future systematic skips for materials that closed clean | small owner change; rollback is removal of the reuse branch | DEFERRED_WITH_REASON, future candidate |
| 3b. Record the material's immutable range identity beside the continuity binding without a producer-issued binding | computable from Git objects | not allowed: the contract's producer admission condition requires the gate to have run against the committed target | proves bytes existed, not that the gate ran against them | misleading if read as collected evidence | none | REJECTED |
| 4. Relax guard 3 so a later session-sync commit does not break an earlier target | feasible in code | forbidden by the contract's target guard | creates the exact false-admission class the guard was added to prevent | would collect rows that do not match their range | none | REJECTED |

## Selected Disposition

Selected: RETAIN_EXPLICIT_SKIP_FOR_THIS_MATERIAL and DEFER_STRUCTURAL_COLLECTION_CHANGE.

Exact owners retained unchanged: `committed_evidence_fingerprint.verify_worktree_matches_committed_target` (guard 3), `mfrp_shadow_canary_autocollect.validate_and_reconcile_receipt` (the `SKIPPED_NO_COMMITTED_EVIDENCE` branch), `mfrp_shadow_canary_autocollect.find_receipt_candidate` (no stale-receipt competition), and the bounded retry owner (one retry per trusted commit, replayable only).

Authority granted by this design: none. No owner changes, no receipt or journal changes, no sample promotion, no safety-marker change.

Proof: the four isolated probes and the real-repo reconciliation in the companion evidence.

Rollback: nothing to roll back. The recommendation is a documented retained disposition.

## Future Admission Requirements (Not Granted)

Option 3a may be reconsidered only through a separate design that proves all of the following:

1. The reused receipt's `base..head` equals the exact trusted range, and its `committedEvidence` recomputes from Git objects.
2. The canonical receipt reader accepts the receipt, including its digest.
3. The binding was produced when HEAD equalled the trusted commit with a clean worktree. This timing must be recorded in the receipt, not inferred.
4. Hostile negatives: an old PASS receipt for another range; a receipt with a forged or one-sided binding; a receipt produced from a dirty tree; a receipt whose disclosure ordering is not proven.
5. Guard 3 is unchanged, and one bounded retry per trusted commit is preserved.
6. Opportunity, attempt and sample counts stay separate.

Option 2 may be reconsidered only through a separate design that defines isolated re-execution as its own admission class, records every attempt including failures, and proves that the isolated environment reproduces the original gate inputs.

## Risk / Corrective Action

Risk 1 - systematic skips for session-sync materials. Materials whose overlapping paths are updated by the next session-sync commit will not bind. Corrective action: none in this design. Local should decide whether to accept this as a known limit or to open a separate design under Option 3a.

Risk 2 - misleading legacy PASS receipts (Finding 5). The generated receipt names the requested range but reads later bytes. Corrective action: recorded as a standing risk. A future design should make the gate refuse a PASS receipt when the worktree does not match the range, or label it explicitly.

Risk 3 - time-dependent continuity admissibility (Finding 6). Corrective action: any continuity claim must name the HEAD at which it was checked.

Risk 4 - unknown closure cause for the material's own receipt (Finding 3). The frozen case does not record why that receipt has no binding. Corrective action: Local should consult the closure-time runtime log if it still exists before any future decision.

## Retry And Attempt Accounting

The case records one collector attempt for trusted commit `0ab461e2b`: outcome `SKIPPED_NO_COMMITTED_EVIDENCE`, not a historical diagnostic, with no retry marker. `SKIPPED_NO_COMMITTED_EVIDENCE` is a retryable outcome in the observability owner. The retry is consumed only if the trusted target is replayable; it is not, so no retry is consumed by this design.

Opportunity count for this material: one trusted commit evaluated at one disclosure. Attempts: one. Collected samples: none. No count was inflated by the design work, which made no collector call.

## Finding-To-Governance Learning Disposition

Defect class: MACHINE_GATE_GAP
Learning lane: GOVERNANCE_CONTROL_PLANE
Disposition: MACHINE_CHECK_CANDIDATE
Next action: Local decides whether to open a separate design for the closure-time reuse option (3a) with anti-replay negatives, or to accept the standing risk that a generated receipt can report PASS for bytes it did not match. This design adds no check.
Runtime/provider/cost learning: N/A_WITH_REASON - no runtime, provider or cost finding; no experiment or measured comparison was selected.

The design repeats a known class (unreplayable historical target, `HISTORICAL_REPLAY_MISMATCH`) that the retry owner already handled. The new facts are that the material closure receipt lacks a binding for an unrecorded reason, and that the collector's regenerated receipt can report PASS for bytes it did not match. Both belong to the owner that generates receipts and are recorded as risks in this design.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_truth_foundation_claim_guard.py`; `governance/compat/check_independent_review_probe_admission.py`. Named for gate application; their constants were not re-read line by line in this lane. |
| literalTokensReviewed | Checker Source Read-Ahead Block; Agent Operation Trace Block; Epistemic Process Block; Finding-To-Governance Learning Disposition; Rescan Intelligence Hardening; Expected Result / Prediction; Evidence Comparison; Contradiction Or Gap Disposition; Defect class; Learning lane; Disposition; Next action |
| gateRunPurpose | confirmation and evidence of the fast gate on final bytes; the gate verifies the required structure and does not replace the owner probes |
| claimBoundary | covers the named owner bodies and the probes in the companion evidence; other applicable checkers are exercised by the fast gate and were not read line by line; no corpus claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Haiku-family INTERNAL_AGENT worker, operator-started shared-workspace seat |
| Provider or surface | private shared workspace, no provider or network call |
| Session or invocation | mfrp-continuity-collection-design-worker-20261011 |
| Working directory | repository root; probe fixtures under the ignored runtime folder |
| Command or tool surface | file reads, git read-only commands, canonical receipt reader on copies, real-repo read-only owner calls, isolated fixture probes |
| Target paths | `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`; companion evidence; return |
| Allowed scope source | work order Write Ownership table |
| Before status evidence | HEAD 2575d3e5d; clean worktree; staged empty |
| After status evidence | three untracked owned files; no tracked file modified |
| Diff evidence | `git status --short` shows the owned untracked files only |
| Approval boundary | operator-started worker after bound pre-implementation PASS; no commit or nested agent |
| Claim boundary | offline design and owner probes; no runtime or collection claim |
| Agent type | INTERNAL_AGENT |
| Invocation ID | mfrp-continuity-collection-design-worker-20261011 |
| Expected manifest | `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_COMPLETION_2026-10-11.md`; `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`; `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_WORKER_RETURN_2026-10-11.md`; `docs/reviews/evidence/mfrp-continuity-collection-design-worker-20261011.json`; `docs/reviews/evidence/mfrp-continuity-collection-design-local-20261011.json`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`; `docs/baselines/CVF_GC018_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`; `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json`; `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_COMPLETION_2026-10-11.md`; `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`; `docs/reviews/CVF_MFRP_CONTINUITY_COLLECTION_DESIGN_WORKER_RETURN_2026-10-11.md`; `docs/reviews/evidence/mfrp-continuity-collection-design-worker-20261011.json`; `docs/reviews/evidence/mfrp-continuity-collection-design-local-20261011.json`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`; `docs/baselines/CVF_GC018_MFRP_CONTINUITY_COLLECTION_DESIGN_2026-10-11.md`; `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json`; `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Epistemic Process Block

Expected Result / Prediction: the existing owners refuse the historical target and keep the unreplayable item visible and unconsumed, so a safe recovery needs either an explicit admission change or a retained skip.
Evidence Comparison: four isolated probes match their expected results, including the no-op control; the two frozen raw receipts validate; the continuity range identity recomputes exactly; the real-repo historical target is refused at the current HEAD.
Contradiction Or Gap Disposition: the continuity check was true in the case and false at the current HEAD; this is time-dependent and is reported, not resolved. The material closure receipt's missing binding is unexplained by the case and is recorded as a limit.
Claim Update: retained explicit skip proposed for this material; structural change deferred with reasons; no collection or effectiveness claim.

## Rescan Intelligence Hardening

- N/A with reason: this design is a documentary owner analysis; no intake refresh, delta ledger, routing matrix or source reassessment was produced.

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

## Public Export Disposition

DEFERRED_PRIVATE_ONLY. Private design and evidence only; no public-sync authorization.

## Claim Boundary

One source-derived design. It names the existing owners, records one retained disposition with reasons, and lists the future admission requirements without granting them. It makes no claim about runtime collection, collector recovery, model ranking, live AI governance, cost, or the truth of any receipt's execution. `independentProbeDisposition: PENDING_REVIEWER_EXECUTION`. Historical semantics, actual target bytes and current authority are kept separate throughout.

## Local Closure Trace Conversion

Local expanded only the two trace manifest rows to the reviewer-authorized twelve-path material. Original submitted design bytes/SHA and worker proof/return are preserved in Local evidence. This closure metadata correction does not enlarge worker execution authority or erase its three-path return.
