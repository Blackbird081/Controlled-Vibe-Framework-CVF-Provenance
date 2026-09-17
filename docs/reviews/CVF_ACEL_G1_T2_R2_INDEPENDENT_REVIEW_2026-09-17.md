# CVF ACEL G1 T2 R2 Independent Review

Memory class: FULL_RECORD

Status: REVIEW_REJECTED_PARKED_REDESIGN_REQUIRED

docType: review

Date: 2026-09-17

Batch ID: ACEL-G1-T2-R2-INDEPENDENT-REVIEW

Reviewer: Local orchestrator/reviewer

Review base: `85b60e9e7`

## Purpose

Record the terminal Local review of Claude's R2 consolidated return for
`ACEL-G1-T2-TASK-CLASS-CALIBRATION-OWNER-IMPLEMENTATION`. The review consumes
the returned 88/88 TypeScript and 73/73 Python evidence, but independently
checks the design-to-code identity and integrity edges that those tests claim
to prove. It does not implement a third repair, accept the seven worker paths,
or open runtime, provider/live, real calibration, G4, public-sync, or
deployment work.

## Startup And Role Routing Acknowledgment

Current mode is `multi_repo_absorption_acel_g1_t2_implementation_dispatched`;
active handoff is `AGENT_HANDOFF_V61_2026-09-16.md`; the allowed move was Local
review of the exact seven-path offline return. Claude and any provider-native
helpers in the shared workspace are `INTERNAL_AGENT` workers. Final technical
disposition remains Local. External research is advisory only and did not
supply proof for this review. G4 and all live/runtime checkpoints remain
parked.

## Scope / Target / Owner Boundary

- the accepted G1 T1 design manifest and its required held-out, preference,
  provenance, and regression semantics;
- the seven uncommitted G1 T2 paths declared by the work order;
- the R2 worker-return claims and negative-case matrix;
- focused source inspection plus one read-only in-memory TypeScript probe;
- repository status and commit boundary.

No worker path was edited, staged, or committed by this review.

## Scope / Methodology

The reviewer consumed the returned test/gate evidence rather than broadly
recreating it, read the accepted manifest and the exact implementation edges
named by R2, and ran one bounded contradiction probe because the source showed
a specific information gap. The expected information gain was whether the
actual decision function rejected cross-candidate admission and mismatched
authority/provenance identities; the probe completed locally in seconds.

## Target / Source

The target is the exact seven-path worker return governed by
`docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md`.
The controlling semantic source is
`docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json`;
current implementation, tests, checker, audit, contract, and worker return are
the evidence under review.

## Independent Review Disposition

`REVIEW_REJECTED_PARKED_REDESIGN_REQUIRED`

The R2 return does not satisfy design-to-code parity. Its passing suites prove
the cases encoded by the worker, but the positive fixture helper itself
normalizes a cross-candidate positive/negative pool that is weaker than the
accepted design. Two additional integrity edges also remain unbound. These are
acceptance-blocking contract defects, not documentation-only discrepancies.

This is the third Local disposition boundary on the same implementation
tranche after R1 and R2 repair. No automatic R3 dispatch is authorized. The
seven worker paths remain uncommitted and parked pending a fresh owner/schema
decision that can represent candidate-scoped required fixture coverage and a
complete provenance preimage.

## Findings / Position

| ID | Severity | Finding | Direct source evidence | Independent observation | Disposition |
|---|---|---|---|---|---|
| R2-RV-F1 | CRITICAL | Round-level fixture admission is pooled across all candidates, so one candidate's negative fixture can satisfy another candidate's positive/negative admission requirement. The preferred candidate is not required to have bound `PASS_WITH_EVIDENCE` for all required held-out fixtures. | accepted manifest lines 169-182; implementation lines 492-507 and 683-725; test helpers lines 285-374 | The R2 helper appends an intentionally failing negative companion candidate. The ordinary positive candidate still becomes `preferred`; therefore the negative requirement is satisfied by evidence that does not attest the preferred candidate. | BLOCKING_SCHEMA_AND_BINDING_GAP |
| R2-RV-F2 | HIGH | GC-026 validates the attestation content hash and winner task/config, but does not require the outer `promotionRecordRef` and `promotedAt` to equal the hashed inner record. | implementation lines 216-221 and 835-848; checker lines 293-413 | Changing outer promotion reference to `different-record` and outer time to `2030-01-01T00:00:00Z` while retaining the original hashed inner record still returns `ACCEPTED_PREFERRED` and emits a CURRENT binding. | BLOCKING_CROSS_RECORD_INTEGRITY_GAP |
| R2-RV-F3 | HIGH | The provenance preimage omits the accepted design's `preferencePolicyHash` and does not bind actual trace identity/capture mode or producer receipt identity. | accepted manifest line 211; implementation lines 660-715 and 886-904 | Changing a supplied G3 trace ID to an unbound value remains accepted and produces the same provenance. Changing the winning GC-026 score from 42 to 999 also leaves provenance unchanged. | BLOCKING_PROVENANCE_GAP |
| R2-RV-F4 | MEDIUM | The Python checker mirrors the incomplete GC-026 binding and checks provenance shape rather than recomputing the accepted design formula. | checker lines 293-430 and 424-487 | A machine PASS from this checker cannot close F2 or F3 because those equality/preimage edges are absent from the checker itself. | DEPENDENT_TEST_AND_CHECKER_GAP |

## Risk / Corrective Action

The immediate risk is false certification: a candidate can be promoted using
another candidate's fixture-class coverage, a promotion reference inconsistent
with its hashed record, and provenance that does not change when relevant
evidence/policy identity changes. The corrective action is to keep all seven
paths uncommitted, park the tranche, and require the schema-level reopen
decision specified below. No local patch is applied because candidate-scoped
fixture collections change the contract shape rather than one isolated branch.

## Probe Evidence

The reviewer reused the worker's own builders in memory and loaded the actual
TypeScript implementation through the repository-local TypeScript compiler.
The probe made no file change, network call, provider call, benchmark run, or
configuration mutation.

| Probe | Mutation | Observed result |
|---|---|---|
| baseline | worker's positive candidate plus its negative companion | `ACCEPTED_PREFERRED`; companion is `insufficient_evidence` |
| GC-026 outer/inner mismatch | outer record/time changed; hashed inner record unchanged | `ACCEPTED_PREFERRED`; CURRENT regression binding emitted |
| trace identity mismatch | actual `g3Traces[0].traceId` changed without changing declared `traceIds` | `ACCEPTED_PREFERRED`; provenance identical to baseline |
| preference value mutation | winning value changed from 42 to 999 | `ACCEPTED_PREFERRED`; provenance identical to baseline |

The SEARCH-partition variant failed closed, which confirms the contamination
branch works for the narrow declared key case. It does not cure the distinct
candidate-scoped fixture-coverage gap in F1.

## Returned Evidence Evaluation

| Returned claim | Review result |
|---|---|
| 88/88 TypeScript tests | ACCEPT_AS_EXECUTION_EVIDENCE; REJECT_AS_DESIGN_PARITY_PROOF because the happy path encodes the cross-candidate companion pattern |
| 73/73 Python tests | ACCEPT_AS_EXECUTION_EVIDENCE; REJECT_AS_INTEGRITY_COMPLETENESS_PROOF because the checker omits the same equality/preimage edges |
| source 974 lines, test 1178 lines | ACCEPT; governed file-size repair is not disputed |
| WORKER_MUST_NOT_COMMIT | PASS; HEAD was unchanged by the worker and staging remained empty |
| three unrelated discussion-file gate failures | RESOLVED_SEPARATELY at material commit `8d54351f35993f04d661bcacd458b31956081295`; not charged to the seven worker paths |
| no unresolved risk blocks `COMPLETE_PENDING_REVIEW` | REJECT; F1-F3 are unresolved acceptance blockers |

## Acceptance Resolution

| Work-order acceptance item | Resolution |
|---|---|
| exact seven create-only worker paths | PASS |
| no provider/live/runtime/configuration effect | PASS |
| worker made no commit | PASS |
| candidate/config/comparability recomputation | PASS_BOUNDED |
| all required held-out G3 fixtures bound to the preferred candidate | FAIL_R2_RV_F1 |
| independently verifiable preference authority | FAIL_R2_RV_F2 |
| provenance binds accepted design inputs | FAIL_R2_RV_F3 |
| checker proves persisted evidence integrity | FAIL_R2_RV_F4 |
| Local terminal acceptance | REJECTED_AND_PARKED |

## Review Cost Telemetry And Stop Disposition

| Field | Value |
|---|---|
| reviewRoundCount | 3 |
| workerRepairTurnCount | 2 |
| newRootCauseCountThisRound | 1 |
| dependentFindingCountThisRound | 3 |
| elapsedReviewMinutes | `NOT_AVAILABLE_WITH_REASON: cross-turn elapsed time is not exposed reliably` |
| providerCallCount | 0 |
| tokenOrQuotaUsage | `NOT_AVAILABLE_WITH_REASON: provider-neutral quota telemetry is unavailable in repository evidence` |
| valueDelta | Prevented a cross-candidate evidence pool and incomplete authority/provenance binding from being committed as the G1 operating-point owner contract. |
| stopDisposition | REVIEW_COST_ESCALATION_REQUIRED |
| preRepairAuditDisposition | COMPLETE_BEFORE_REPAIR |
| materialCommitCount | 1 |
| continuityCommitCount | 1 |
| commitPlanDisposition | WITHIN_DEFAULT_BUDGET |
| latencyDisposition | `LATENCY_BUDGET_EXCEEDED_WITH_REASON: R2 semantic verification crossed chat turns and required a focused contradiction probe` |
| avoidableDelayClass | SEQUENTIAL_FINDING_DISCOVERY |

The material and continuity counts above refer only to the separately requested
orchestration-discussion preservation, commits `8d54351f3` and `85b60e9e7`.
The rejected G1 implementation has zero material or continuity commits.

## Required Reopen Decision

Reopen only through a fresh reviewed design/schema amendment that answers all
of the following together:

1. whether a candidate envelope contains a fixture-result collection or
   references one candidate-scoped admitted fixture-set evaluation;
2. how every required held-out fixture is bound to the same candidate and must
   independently yield `PASS_WITH_EVIDENCE`;
3. which outer GC-026 fields are redundant and removed, or which exact equality
   constraints bind them to hashed record content;
4. the complete canonical provenance preimage, including preference policy,
   evidence-envelope identity, receipt identity, trace identity/capture mode,
   and deterministic ordering;
5. how the Python checker independently recomputes those edges.

Do not issue a narrow R3 patch against the current one-fixture-per-candidate
shape. F1 requires an owner/schema choice, and F2-F4 must be closed in the same
dependency graph before another implementation dispatch.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this is a private provenance review of rejected, uncommitted offline
implementation evidence. No public artifact, public-sync remote, or export
authority is in scope.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | independent offline review of seven uncommitted G1 T2 paths |
| claimDisposition | CLAIM_REJECTED: worker readiness and implementation acceptance are not established |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no provider, benchmark, real calibration, or runtime receipt was requested or produced |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source inspection, repository status, accepted-design comparison, and one hermetic in-memory contradiction probe |
| invocationBoundary | local read-only source/test loading and deterministic TypeScript execution only |
| interceptionBoundary | no runtime wrapper, dispatcher, provider, network, configuration, or deployment interception |
| claimLanguage | R2 execution evidence is real but insufficient for design parity; implementation remains uncommitted and parked |
| forbiddenExpansion | no R3 auto-dispatch, G4, real calibration, provider/live, runtime, configuration mutation, public sync, or deployment |

## Claim Boundary

Final disposition is limited to rejection and parking of this uncommitted R2
return. Verification proves the four named contradictions against current
local source; it does not prove that a future schema design is correct, that a
real operating point exists, or that any runtime/provider behavior is ready.
Passing returned tests remain valid execution evidence but cannot override
the accepted design or the independently reproduced counterexamples.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_task_class_calibration_owner_evidence.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | review structural headings; `## Checker Source Read-Ahead Block`; four required read-ahead fields; exact eight-field Delta block; `REVIEW_COST_ESCALATION_REQUIRED`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirmation of the recorded review shape and bounded disposition after semantic inspection; machine gates are evidence, not first discovery of implementation correctness |
| claimBoundary | read-ahead and gate success prove artifact conformance only; they do not cure F1-F4 or accept the rejected worker implementation |

## Epistemic Process Block

### Expected Result / Prediction

If R2 fully closed the accepted design, fixture-set admission would be
candidate-scoped, promotion identity would be consistent across outer and
hashed records, and every invalidation-relevant preference/evidence identity
would alter provenance or fail closed.

### Evidence Comparison

R2 materially improved recomputation and attestation structure, and its tests
execute successfully. Direct source inspection and the bounded probe show that
the three named integrity expectations still fail on the actual implementation
path.

### Contradiction Or Gap Disposition

Local repository authority overrides the worker return's readiness claim. The
contradictions are recorded rather than reconciled by assuming that a
round-level mixed-candidate pool, outer-only promotion reference, or omitted
policy/evidence identities are equivalent to the accepted design.

### Claim Update

The R2 worker return is rejected and the G1 T2 implementation is parked for a
fresh schema-level decision. No implementation or runtime capability is
accepted by this review.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF shared workspace |
| Session or invocation | ACEL G1 T2 R2 independent review, 2026-09-17 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, `git status`, local Node/TypeScript in-memory probe, `apply_patch` for this reviewer record only |
| Target paths | accepted design manifest, exact seven worker outputs, this review |
| Allowed scope source | G1 T2 work order Review Gate and operator instruction to handle Claude's return |
| Before status evidence | worker self-declared `COMPLETE_PENDING_REVIEW` with 88/88 and 73/73 |
| After status evidence | three implementation blockers and one dependent checker/test blocker independently evidenced |
| Diff evidence | worker seven paths remain untracked; this reviewer record is the only G1 review-owned addition |
| Approval boundary | Local disposition only; no repair or successor authority exercised |
| Claim boundary | offline review; no provider/live, empirical calibration, runtime, G4, public, or deployment claim |
| Agent type | reviewer/closer |
| Invocation ID | `acel-g1-t2-r2-independent-review-2026-09-17` |
| Expected manifest | exact seven worker paths plus one reviewer-owned disposition record |
| Actual changed set | exact seven worker paths plus this reviewer-owned disposition record |
| Manifest delta | MATCH |
