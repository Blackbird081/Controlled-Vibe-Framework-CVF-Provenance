# CVF GC-018 Baseline - SOT3-T2 Canonical Inter-Layer Contracts

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-12

Baseline ID: GC018-SOT3-T2

Risk ceiling: HIGH_DOC_CONTRACT_ONLY

## Purpose

Authorize one no-commit worker to create the CVF-owned documentation contract
family for the accepted three-layer SOT architecture without implementing any
package, runtime, schema, test, guard, checker, provider, or public behavior.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind gc018-baseline --batch-id SOT3-T2 --title "Canonical Inter-Layer Contracts" --date 2026-07-12 --base cc64c8e07 --stdout` |
| generatedProfile | GC-018 documentation-contract authoring |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Added T1 dependency, owner namespace, contract chain, fail-closed invariants, exact outputs, and no-runtime boundary. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_truth_foundation_claim_guard.py` |
| docOnlyNewFields | SourceEnvelope; RefineryPacket; KernelEvaluationRequest; KernelDecision; TruthReceipt; TruthReference; DistributionPackage; FeedbackProposal |
| claimBoundary | Documentation contract family only; no runtime, schema, test, guard, or readiness proof. |

## Target / Source

- T0R architecture acceptance: `docs/reviews/CVF_SOT3_T0R_COMPLETION_REVIEW_2026-07-12.md`.
- T1 owner acceptance: `docs/reviews/CVF_SOT3_T1_COMPLETION_REVIEW_2026-07-12.md`.
- T1 owner map: `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md`.
- TKG-T1 upstream doctrine: `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`.
- Retained source specifications remain read-only evidence.

## Scope / Target / Owner Boundary

Allowed: create a new documentation-only owner namespace under
`docs/reference/sot_three_layer/`, define one canonical contract chain, map
producers/consumers, declare fail-closed invariants and negative cases, and
return source reconciliation evidence.

Forbidden: TypeScript/JSON Schema/runtime/test/guard/checker implementation,
package activation, direct import, mutation of TKG-T1 or skill truth-packet
owners, provider/live proof, public-sync, commit, release, or readiness claim.

## Findings / Position

The canonical chain is:

```text
SourceEnvelope
  -> RefineryPacket
  -> KernelEvaluationRequest
  -> KernelDecision + TruthReceipt
  -> TruthReference
  -> DistributionPackage
  -> FeedbackProposal
```

Refinery prepares but never declares truth. Kernel alone evaluates trust and
issues decision/receipt/reference authority. Flow consumes Kernel proof and
owns distribution/lifecycle only. Feedback proposes change but cannot mutate
truth, evidence, or source score directly.

## Baseline Decision

SOT3-T2 documentation contract authoring is authorized. Runtime and all
implementation remain `NOT_AUTHORIZED`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`canonical inter-layer contract authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "canonical inter-layer contract authoring" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs/work_orders --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| three-layer topology accepted | VALUE_SET | `docs/reviews/CVF_SOT3_T0R_COMPLETION_REVIEW_2026-07-12.md` | Disposition | `REVIEWER_ACCEPTED_BOUNDED` | T0R review | ACCEPT |
| CAP-01 requires a new architecture owner | VALUE_SET | `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md` | Owner-Decision Token Summary | `CAP-01` | T1 owner map | ACCEPT |
| TKG-T1 remains upstream doctrine owner | VALUE_SET | `docs/reviews/CVF_SOT3_T1_COMPLETION_REVIEW_2026-07-12.md` | Findings / Position | `CAP-04` | T1 review | ACCEPT |
| T2 roadmap objective is canonical inter-layer contracts | VALUE_SET | `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md` | Tranche Plan | `SOT3-T2` | SOT3 roadmap | ACCEPT |
| implementation remains unauthorized | LITERAL_INVARIANT | `docs/reviews/CVF_SOT3_T1_COMPLETION_REVIEW_2026-07-12.md` | Implementation Boundary | `NOT_AUTHORIZED` | T1 review | ACCEPT |

## New Doc-Only Fields

| New item | Intended documentation owner | Existing-runtime claim |
|---|---|---|
| `SourceEnvelope` | SOT three-layer contract chain | NONE |
| `RefineryPacket` | SOT three-layer contract chain | NONE |
| `KernelEvaluationRequest` | SOT three-layer contract chain | NONE |
| `KernelDecision` | SOT three-layer contract chain | NONE |
| `TruthReceipt` | SOT three-layer contract chain, aligned with TKG-T1 doctrine | NONE |
| `TruthReference` | SOT three-layer contract chain | NONE |
| `DistributionPackage` | SOT three-layer contract chain | NONE |
| `FeedbackProposal` | SOT three-layer contract chain | NONE |

## Negative Search And Collision Discipline

| Search token | Exact search command or query | Search roots | Same-token collision result | Disposition |
|---|---|---|---|---|
| contract family namespace | `rg -n "sot_three_layer|SOT Three-Layer" docs/reference EXTENSIONS governance` | current CVF roots | no current owner namespace at dispatch | NEW_DOCUMENTATION_OWNER_CANDIDATE |
| receipt binding | `rg -n "TruthReceipt|truth receipt|receipt binding" docs/reference EXTENSIONS governance` | current CVF roots | skill receipt phrase and Guard workflow receipt are not truth-evaluation contracts | COLLISION_REVIEWED_NOT_SAME_OWNER |

## Contract Invariants

1. Source identity exists before normalization and persists by reference/hash.
2. Duplicate grouping precedes conflict evaluation.
3. Zero executed Refinery stages cannot produce Kernel-ready status.
4. Empty evidence or verification results cannot pass Kernel evaluation.
5. Receipt binds evaluated packet hash, policy/rule versions, evidence,
   obligations, verification results, decision, and predecessor hash.
6. Only Kernel creates `TruthReference`.
7. Flow cannot publish from caller-supplied approval booleans.
8. Distribution requires a valid, non-expired Kernel receipt/reference.
9. Feedback is proposal-only and cannot mutate authority directly.
10. Direct import of retained competing packet/runtime shapes is forbidden.

## Verification / Evidence

- exact eight-contract inventory and producer/consumer map;
- field minimums, status vocabularies, and lifecycle transitions;
- TKG-T1 alignment and collision ledger;
- at least twelve negative cases covering empty, mismatch, replay, expiry,
  invalid transition, and direct-mutation scenarios;
- exactly five worker outputs and unchanged HEAD.

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_truth_foundation_claim_guard.py` |
| literalTokensReviewed | DISPATCH_READY; Source Verification Block; New Doc-Only Fields; NOT_AUTHORIZED; Public Export Disposition |
| gateRunPurpose | confirm documentation-contract dispatch shape after source and checker review |
| claimBoundary | gates do not prove contract correctness or runtime behavior |

## Acceptance Criteria

- [ ] all eight contracts have one canonical producer and consumer set;
- [ ] no duplicate packet or lifecycle authority remains;
- [ ] Kernel-only trust/receipt/reference authority is explicit;
- [ ] Refinery no-AI/no-truth boundary is explicit;
- [ ] Flow post-Kernel-only boundary is explicit;
- [ ] fail-closed invariants and negative cases are complete;
- [ ] TKG-T1 and skill truth-packet compatibility is mapped;
- [ ] no runtime/schema/test/guard/checker mutation or worker commit.

## Fail Conditions

- multiple canonical packet shapes;
- Flow or Refinery issues Kernel authority artifacts;
- empty collections can satisfy required stages/evidence;
- receipt hash excludes evaluated content or decision context;
- feedback mutates authoritative state directly;
- runtime/readiness claim or forbidden path mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private retained evidence and internal contract design.

## Claim Boundary

This baseline authorizes documentation-only contract authoring. It does not
authorize runtime, schemas, tests, guards, checkers, packages, provider/live
proof, public-sync, release, or production readiness.
