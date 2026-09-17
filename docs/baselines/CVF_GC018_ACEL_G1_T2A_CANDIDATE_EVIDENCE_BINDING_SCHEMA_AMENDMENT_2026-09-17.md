# CVF GC-018 Baseline - ACEL G1 T2A Candidate Evidence Binding Schema Amendment

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-09-17

Batch ID: ACEL-G1-T2A-CANDIDATE-EVIDENCE-BINDING-SCHEMA-AMENDMENT

Dispatch base head: `a9813bb3e4fbc53ffc245ec19a0f3808ef16f93e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local orchestrator/reviewer

Worker target: shared-workspace `INTERNAL_AGENT` design worker

## Purpose

Authorize one documentation-only schema amendment that resolves the four
acceptance blockers recorded by the G1 T2 R2 independent review before any new
implementation attempt. This is a fresh root-contract design tranche, not R3
repair of the seven rejected worker paths.

## Scope / Target / Owner Boundary

The worker may create exactly one human design audit, one machine-readable
design manifest and one worker return. Local owns review and commit. The seven
rejected G1 T2 paths already present as untracked files are frozen read-only
inputs: hash them before and after, but do not edit, stage, delete or commit
them. No provider/live, runtime, configuration, G4, public or deployment
authority is released.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| R2 independent review | `docs/reviews/CVF_ACEL_G1_T2_R2_INDEPENDENT_REVIEW_2026-09-17.md`, SHA-256 `c29cf63ff0aed8c294e61f3286e98ac18242b30b4a3f16445dc1a7310eba175f`, committed at `0862d3610` | may open a fresh reviewed schema amendment; no automatic R3 | RELEASED_FOR_DESIGN_ONLY |
| accepted G1 T1 design | manifest SHA-256 `c8c1f6899e50513141e69113b8ac9faf37669b1fcd785bc2df3b88d8e894505b` | remains source authority unless amendment names and justifies an exact changed clause | RELEASED_WITH_RECONCILIATION_REQUIRED |
| rejected implementation | seven untracked paths, not accepted or committed | evidence may be inspected; bytes must remain unchanged | FROZEN_REJECTED_INPUT |

## Source / Predecessor Evidence

The accepted T1 manifest remains design authority; the T2 R2 independent
review is defect and disposition authority; the rejected seven-path return is
read-only diagnostic evidence. Exact paths and hashes are carried by the
paired work order and must be reconciled by the worker.

## Proposed Tranche

One documentation-only schema amendment defining candidate-scoped evidence,
GC-026 equality, the canonical provenance preimage and independent checker
recomputation. Any implementation is a later, separately reviewed tranche.

## Required Design Outcomes

1. Define candidate-scoped required fixture-set membership and prove every
   required held-out fixture has a result bound to the same candidate.
2. Choose one GC-026 record topology: eliminate redundant outer fields or
   require exact equality with the hashed inner record.
3. Define a complete canonical provenance preimage that binds preference
   policy, evidence-envelope identity, producer receipt and trace identity plus
   capture mode with deterministic ordering.
4. Define independent checker recomputation and negative cases for every edge.
5. Produce an explicit migration/replacement disposition for the seven
   rejected paths without modifying them.

## Evidence / Verification Boundary

The worker must reconcile the accepted design, the R2 rejection and current
rejected source/checker bytes. Source facts require exact paths, symbols and
SHA-256 values. A design result may be `DESIGN_READY_FOR_SEPARATE_IMPLEMENTATION_WORK_ORDER`
or `BLOCKED_WITH_REASON`; it cannot claim implementation readiness, empirical
calibration or runtime enforcement.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| paired dispatch paths | absent before authoring | NO_COLLISION |
| three worker output paths | absent before authoring | NO_COLLISION |
| rejected seven paths | present as untracked worker return | FROZEN_INPUT_NOT_OUTPUT |
| batch identifier | no prior governed artifact hit | NEW_BATCH |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T2A-CANDIDATE-EVIDENCE-BINDING-SCHEMA-AMENDMENT --title "ACEL G1 T2A Candidate Evidence Binding Schema Amendment" --date 2026-09-17 --base a9813bb3e4fbc53ffc245ec19a0f3808ef16f93e --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_ACEL_G1_T2_R2_INDEPENDENT_REVIEW_2026-09-17.md --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key acel-g1-empirical-calibration-owner-composition --scec-chain-mode SUCCESSOR --scec-chain-ordinal 2 --scec-predecessor-path docs/reviews/CVF_ACEL_G1_T2_R2_INDEPENDENT_REVIEW_2026-09-17.md --scec-predecessor-sha256 c29cf63ff0aed8c294e61f3286e98ac18242b30b4a3f16445dc1a7310eba175f --scec-required-disposition ROOT_CONTRACT_REQUIRED --scec-successor-scope INTEGRATED_ROOT_CONTRACT --stdout` |
| generatedProfile | generic worker, internal agent, no commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact G1 design outcomes, frozen rejected-input boundary, three-path output manifest |
| checkerReadAheadConfirmation | dispatch quality, semantic convergence, closeability, structural, trace, claim-boundary and session guards |
| docOnlyNewFields | candidate evidence-set topology; GC-026 equality topology; canonical provenance preimage; rejected-path migration disposition |
| claimBoundary | dispatch baseline only; no implementation/runtime claim |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | ready status; first-section dispatch envelope; dependency release; exact paths; no-commit boundary; convergence and closeability fields |
| gateRunPurpose | confirmation after source and schema review, not first discovery |
| claimBoundary | checker conformance cannot establish semantic correctness |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044; 10 returned from 24
candidates. The dispatch avoids exhaustive-corpus claims, provider-local
authority, hidden protected writes, unchecked aggregation and child timeout.

## Claim Boundary

This baseline authorizes three uncommitted design/evidence outputs only. It
does not accept or mutate the rejected implementation, authorize R3, select an
operating point, prove empirical value, or open provider/live/runtime/G4 work.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only G1 root-contract amendment dispatch baseline |
| claimDisposition | CLAIM_REJECTED: no implemented execution-control or calibration capability claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no provider/runtime/calibration receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: Local source review, hashes and dispatch gates only |
| invocationBoundary | local documentation and read-only verification |
| interceptionBoundary | no direct interception, wrapper, runtime gate or model-router action |
| claimLanguage | schema recovery dispatched pending worker and Local review |
| forbiddenExpansion | rejected-path edit, R3 repair, implementation, G4, provider/live, runtime, public, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design-recovery dispatch; no public artifact requested.
