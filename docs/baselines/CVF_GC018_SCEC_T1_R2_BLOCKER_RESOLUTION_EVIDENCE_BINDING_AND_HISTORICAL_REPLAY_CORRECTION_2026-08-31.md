# CVF GC-018 SCEC-T1-R2 Blocker Resolution Evidence Binding And Historical Replay Correction Baseline

Memory class: governed-baseline

- Status: `READY_FOR_DISPATCH`
- Date: `2026-08-31`
- Execution base: `9e27af8db7b34b3f2f7212f48365e0c5c4940a34`
- Task ID: `SCEC-T1-R2`
- Problem key: `scec-blocker-resolution-evidence-binding`
- Governing work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_T1_R2_BLOCKER_RESOLUTION_EVIDENCE_BINDING_AND_HISTORICAL_REPLAY_CORRECTION_2026-08-31.md`
- Commit authority: orchestrator/reviewer only
- Worker commit authority: none

## Purpose

Harden the SCEC foundation after its first historical effectiveness test found
that valid set algebra can still label an unresolved blocker `resolved`
without binding that transition to inspectable accepted evidence. Correct the
GC010 replay in the same integrated tranche. This is foundation work only;
GC010 product/runtime remains parked.

## Root Problem

SCEC-E1 proved the stop rule works, but independent review found the replay and
dispatch seed dropped `T1J_BLOCKER_ROUTE_ORDER_AND_PAYLOAD_PROVENANCE_UNDECIDED`.
Accepted R3 evidence retained that blocker. Therefore the correct R2-to-R3
transition is 3 to 4, not 3 to 3. The current checker validates blocker set
algebra but has no per-resolved-blocker evidence binding, allowing unsupported
resolution laundering to remain structurally valid.

## Accepted Authority

| Authority | Accepted fact |
|---|---|
| `docs/assessments/CVF_SCEC_E1_GC010_T1J_R1_R3_EFFECTIVENESS_RECONCILIATION_2026-08-31.md` | Reviewer-corrected E1 verdict is `EFFECTIVE_WITH_HARDENING_REQUIRED`; R2-to-R3 is 3 to 4. |
| `docs/reviews/CVF_SCEC_E1_GC010_T1J_R1_R3_EFFECTIVENESS_RECONCILIATION_WORKER_RETURN_2026-08-31.md` | The route-order/payload blocker was reopened by independent review and STOP/NO_SUCCESSOR still holds. |
| `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | SCEC controls declared evidence shape and does not decide semantic truth. |
| `governance/compat/check_semantic_convergence_control.py` | Existing validation binds predecessor hashes and set algebra but does not bind `resolved` IDs to evidence. |
| `governance/compat/fixtures/semantic_convergence_control/gc010_t1j_r1_r3_replay.json` | R3 reviewer node currently marks the route-order/payload blocker resolved contrary to accepted R3 evidence. |

## Decision / Baseline

Dispatch one integrated implementation tranche. It must add a machine-checked,
per-resolved-blocker evidence-binding contract; update all active scaffold
producers and focused tests; correct the historical replay and its expected
outcomes; add an unsupported-resolution negative regression; update ADIF-0055;
and return one no-commit review packet. No separate design tranche is allowed.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Set reconciliation permits `resolved` arrays without evidence mapping | `governance/compat/check_semantic_convergence_control.py` | `_validate_top_shape`; `_validate_set_reconciliation` | `REQUIRED_BLOCKER_DELTA_FIELDS` | SCEC checker | `ACCEPT` |
| Standard currently describes set algebra but no resolution evidence owner | `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | `Machine-Readable Block Schema`; invariants 3 and 4 | `cvf.semanticConvergenceControl.v1` | SCEC standard | `ACCEPT` |
| Replay resolves an actually retained blocker | `governance/compat/fixtures/semantic_convergence_control/gc010_t1j_r1_r3_replay.json` | T1J-R3 reviewer correction node | `T1J_BLOCKER_ROUTE_ORDER_AND_PAYLOAD_PROVENANCE_UNDECIDED` | replay fixture | `ACCEPT` |
| Accepted R3 correction keeps approval ordering and payload provenance open | `docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md` | Independent Reviewer Correction | R3 reviewer evidence | historical accepted review | `ACCEPT_AS_REGRESSION_EVIDENCE` |
| E1 independently corrected the transition to 3 to 4 | `docs/reviews/CVF_SCEC_E1_GC010_T1J_R1_R3_EFFECTIVENESS_RECONCILIATION_WORKER_RETURN_2026-08-31.md` | Independent Reviewer Correction | `EFFECTIVE_WITH_HARDENING_REQUIRED` | E1 accepted review | `ACCEPT` |

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "scec-blocker-resolution-evidence-binding",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [
      "SCEC_RESOLVED_BLOCKER_HAS_NO_BOUND_EVIDENCE",
      "SCEC_GC010_REPLAY_DROPS_UNRESOLVED_ROUTE_PAYLOAD_BLOCKER"
    ],
    "reopened": [],
    "current": [
      "SCEC_RESOLVED_BLOCKER_HAS_NO_BOUND_EVIDENCE",
      "SCEC_GC010_REPLAY_DROPS_UNRESOLVED_ROUTE_PAYLOAD_BLOCKER"
    ]
  },
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "SCEC-T1-R2-FOUNDATION-GAP",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/reviews/CVF_SCEC_E1_GC010_T1J_R1_R3_EFFECTIVENESS_RECONCILIATION_WORKER_RETURN_2026-08-31.md"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Required Control Semantics

1. Every blocker ID in `blockerDelta.resolved` must have exactly one explicit
   resolution-evidence record; no missing, duplicate, or extra record passes.
2. Each record must bind an evidence class, normalized repository-relative
   evidence path, immutable SHA-256, and a precise evidence locator or claim
   link. The checker verifies shape, path safety, existence, hash equality,
   and exact blocker-ID coverage.
3. Executable-proof resolution must link to a declared claim whose proof class
   satisfies the existing claim-to-proof mapping. Accepted-review resolution
   remains reviewer-semantic authority; the checker must not pretend to score
   whether prose is true.
4. Empty `resolved` requires an empty evidence map and scaffold generators emit
   that safe default.
5. The corrected R3 reviewer node retains all three R2 blockers, adds the
   rejected exactly-once barrier, and has current count 4. STOP/NO_SUCCESSOR
   and two non-decreasing transitions remain unchanged.
6. Existing unchanged historical artifacts are not retroactively reopened;
   changed/new active blocks and direct validator tests use the hardened shape.

## Acceptance Strategy

- negative test: a blocker moved to `resolved` with no binding fails closed;
- negative tests: wrong blocker ID, extra binding, unsafe/unreadable path,
  hash mismatch, missing locator, and invalid claim link fail closed;
- positive tests: accepted-review binding and executable-claim binding pass;
- replay assertions prove R2-to-R3 3 to 4 and STOP/NO_SUCCESSOR;
- both scaffold producers and their golden/focused tests emit the safe field;
- all existing focused SCEC tests pass with no product/runtime changes.

## Evidence / Verification

Dispatch evidence is the accepted E1 correction, direct standard/checker/
fixture source reads, exact work-order manifest, and passing pre-dispatch gate.
Implementation evidence is deferred to the no-commit worker return and must
include pre-fix reproduction, focused tests, direct checker, and final status.

## Dual Agent Surface Matrix

| Surface | Contract state | Implemented state | Evidence | Disposition | Owner |
|---|---|---|---|---|---|
| Internal dispatcher/reviewer | Integrated hardening packet defined | Pending worker implementation | this baseline and work order | `CONTRACT_ONLY` | orchestrator/reviewer |
| External worker surface | Exact manifest and no-commit return defined | Pending operator-mediated execution | governing work order | `CONTRACT_ONLY` | worker |

## ADIF Defect Registry Disclosure

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json`
- Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
- Applied entries: `ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`, `ADIF-0020`, `ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`, `ADIF-0044`, `ADIF-0055`
- Disposition: `APPLIED`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | `READY_FOR_DISPATCH`; `WORKER_MUST_NOT_COMMIT`; `Source Verification Block`; `Semantic Convergence Outcome`; active schema field; protected-path authorization labels |
| gateRunPurpose | Confirm the packet shape after source read-ahead, not discover required structure. |
| claimBoundary | Structural preparation only; no implementation or semantic-truth proof. |

## Scaffold Provenance Block

- scaffoldHelperCommand: `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id SCEC-T1-R2 --title "Blocker Resolution Evidence Binding And Historical Replay Correction" --date 2026-08-31 --base 9e27af8db7b34b3f2f7212f48365e0c5c4940a34 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --include-worker-return-skeleton --stdout`
- generatedProfile: `protected-governance-path`
- generatedSkeletonStatus: `GENERATED_BUT_REPLACED`
- manualEditsAfterScaffold: `YES - bounded foundation authority and exact proof contract replaced generic placeholders`
- checkerReadAheadConfirmation: `COMPLETE`
- docOnlyNewFields: `resolution-evidence contract remains pending implementation`
- claimBoundary: `dispatch authority only`

## Claim Boundary

This baseline authorizes only SCEC foundation hardening and historical replay
correction. It does not authorize GC010 product/runtime work, a same-problem
T1J-R4 successor, provider/live activity, public sync, deployment, production,
or automated semantic-truth scoring.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: private provenance dispatch authority, not public release material.
