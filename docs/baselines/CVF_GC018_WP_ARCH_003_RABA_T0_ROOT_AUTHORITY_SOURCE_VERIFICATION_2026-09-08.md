# CVF GC-018 Baseline - WP-ARCH-003 RABA-T0 Root Authority Source Verification

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-09-08

Batch ID: WP-ARCH-003-RABA-T0-ROOT-AUTHORITY-SOURCE-VERIFICATION

Dispatch base head: `dbf0f1bcc77286fe3429bf582d46df7d1f9edbd2`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one fresh, documentation-only source-verification tranche under
`WP-ARCH-003-RABA`. The worker must determine whether current governed source
supports a truthful approval-authority root and a trusted principal-to-task-to-
file-scope binding that reaches a real runtime consumer. The independent
reviewer owns semantic acceptance and every commit.

## Accepted Authority

- The operator authorized RABA-T0 packet authoring on 2026-09-08.
- The RABA roadmap at commit `cd56ac953d411f6781758d2fe625ea88a9545644`
  is the fresh parent authority and requires evidence-first owner selection.
- The AR1 R1 completion review at commit
  `8ab5a361cbacacbc5f9c1d9e78590342a1173a23` is accepted only for its terminal
  rejection and root-defect facts. Rejected worker prose is not architecture
  authority.
- The accepted bounded `ARCH-ABS-021` consumer correction is reusable and must
  not be re-reviewed without a named contradiction.
- P4-C1 remains active at `b9bdba712`; this tranche creates no MFRP sample,
  receipt, readout, checkpoint or implementation evidence.

## Scope / Target / Owner Boundary

The worker may create exactly two governed artifacts: the assessment and its
worker return named below. Current TypeScript, tests, roadmaps, baselines, work
orders, reviews, checkers, continuity, registries, and the rejected AR1
artifacts are read-only.

The assessment must answer RABA-Q01 through RABA-Q06 as one trust chain:

`authority issuer -> approval receipt -> receipt verifier -> task/principal scope binding -> guard composition -> runtime action decision`

An input supplied by the same caller requesting permission is request evidence,
not proof of approval, identity, owned scope, or freshness. A deterministic
content hash is integrity evidence only and must not be promoted to issuer
provenance.

## Source / Predecessor Evidence

| Evidence | Source | Accepted fact | Disposition |
|---|---|---|---|
| fresh parent | `docs/roadmaps/CVF_WP_ARCH_003_ROOT_AUTHORITY_AND_PRINCIPAL_SCOPE_ARCHITECTURE_REASSESSMENT_ROADMAP_2026-09-08.md` | RABA-T0 must verify six root questions and terminate with one exact decision | ACCEPT |
| terminal predecessor fact | `docs/reviews/CVF_WP_ARCH_003_AR1_R1_CANONICAL_OWNER_RUNTIME_PATH_DESIGN_REWORK_COMPLETION_2026-09-08.md` | AR1 R1 is rejected; trustworthy approval provenance and principal-scope binding remain unresolved | ACCEPT |
| authority envelope | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | `MaoAuthorityEnvelopeInput`, `buildAuthorityEnvelope`, and `verifyAuthorityEnvelope` bind caller-provided checkpoint content to a deterministic hash | ACCEPT |
| role receipt | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | `MaoRoleResolutionReceipt` binds a role decision to the task graph but is not itself a principal-scope proof | ACCEPT |
| guard context | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | `GuardRequestContext` carries role, agent and target-file request data | ACCEPT |
| current MCP seam | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | `buildContext` feeds `cvf_evaluate_full` and the guard engine from tool arguments | ACCEPT |
| delegated-write evaluator | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts` | `evaluateDelegatedWriteBoundary` denies outside a declared boundary but does not issue authority expansion | ACCEPT |

## Decision / Baseline

Decision: `AUTHOR_RABA_T0_SOURCE_VERIFICATION_PENDING_REVIEW`.

The dispatch admits current source facts, not a successful root contract. The
worker must either source every required edge and identify one owner per
responsibility or park the design. A proposal-shaped answer cannot substitute
for current evidence, and structural gate success cannot establish authority.

## Required Artifact Manifest

| Path | Action | Owner | Required result |
|---|---|---|---|
| `docs/assessments/CVF_WP_ARCH_003_RABA_T0_ROOT_AUTHORITY_SOURCE_VERIFICATION_2026-09-08.md` | CREATE | worker | exact source ledger, trust-chain and owner decision for RABA-Q01 through RABA-Q06 |
| `docs/reviews/CVF_WP_ARCH_003_RABA_T0_ROOT_AUTHORITY_SOURCE_VERIFICATION_WORKER_RETURN_2026-09-08.md` | CREATE | worker | pending-review commands, changed-set, hashes and no-commit receipt |

## Acceptance Contract

1. All six root questions have exact current-source answers or an explicit
   fail-closed reason.
2. Approval provenance is distinguished from content integrity.
3. Principal/task/file-scope binding is not self-attested by the requester.
4. Authenticity, expiry or sequence, replay, forgery, mismatch and omission
   behavior are covered.
5. One exact producer-to-verifier-to-non-test-consumer path is named, or the
   design parks.
6. One canonical package and symbol owner is selected per responsibility, with
   rejected-alternative rationale.
7. Current and proposed symbols are labeled separately; absent paths are never
   cited as current authority.
8. `ARCH-ABS-021` is reused without duplicate review unless a contradiction is
   recorded.
9. The terminal decision is exactly
   `PROCEED_TO_INTEGRATED_ROOT_CONTRACT_DESIGN` or
   `PARK_NO_TRUTHFUL_AUTHORITY_ROOT`.
10. Exactly two output paths are created, unstaged and uncommitted; all other
    repository bytes remain unchanged.

## Review Strategy

The reviewer will consume the returned source ledger, search evidence, path
hashes and command receipts. The six questions are reviewed as one dependency
class. Routine review is limited to the returned evidence and targeted checks
for decision-changing claims; no broad duplicate run or worker-analysis
recreation is allowed without a named contradiction, expected information gain
and cost reason.

## Evidence / Verification

Dispatch evidence consists of the committed RABA roadmap, immutable completion-
review identity, current source table, exact manifest, negative collision
receipt, ADIF result and successful dispatch gates. Worker evidence must be
returned through the paired work order and remains non-authoritative until an
independent completion review.

## Negative Search And Collision Discipline

| Check | Exact evidence | Disposition |
|---|---|---|
| artifact paths | `Test-Path` over the baseline, work order, assessment and worker-return targets returned False before authoring | PASS_NO_COLLISION |
| batch token | exact `rg` query for `WP-ARCH-003-RABA-T0-ROOT-AUTHORITY-SOURCE-VERIFICATION` under `docs` and `CVF_SESSION` returned no match before authoring | PASS_NO_COLLISION |
| rejected AR1 evidence | old names remain occurrences by design; they are read-only historical evidence and are not reused as RABA outputs | PASS_PRESERVE_HISTORY |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: EXTERNAL_AGENT_CLI_MCP

parentAssignmentId: WP-ARCH-003-RABA-T0-ROOT-AUTHORITY-SOURCE-VERIFICATION

reviewRoundCount: 0

priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH

dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH

newIndependentCriticalEvidence: NONE

regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 1

usageAvailability: KNOWN_FOR_ADMISSION

quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING

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

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | committed baseline, work order and later reviewer completion | source-verification governance only; no runtime or source mutation | source ledger, exact manifest and reviewer decision | N/A with reason: internal review has no runtime adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | operator-relayed worker packet | one invocation, exact-two outputs, no commit and no self-acceptance | execution base, operation trace, hashes and return gate | prompt transport only; no runtime/MCP adapter is created | CONTRACT_ONLY |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`root authority source verification`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_architecture_schema.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | dispatch-ready status, exact source columns and dispositions, no-commit anchors, initial convergence counters, external invocation ceiling, worker-return profile, dual-agent dispositions, trace labels and private export token |
| gateRunPurpose | confirm packet structure after source-bound authoring; not discover or accept root-authority semantics |
| claimBoundary | checker success cannot prove a trusted issuer, principal binding, verifier or runtime consumer |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id WP-ARCH-003-RABA-T0-ROOT-AUTHORITY-SOURCE-VERIFICATION --title "WP-ARCH-003 RABA-T0 Root Authority Source Verification" --date 2026-09-08 --base dbf0f1bcc77286fe3429bf582d46df7d1f9edbd2 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/roadmaps/CVF_WP_ARCH_003_ROOT_AUTHORITY_AND_PRINCIPAL_SCOPE_ARCHITECTURE_REASSESSMENT_ROADMAP_2026-09-08.md --stdout --include-worker-return-skeleton --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --scec-problem-key WP_ARCH_003_ROOT_AUTHORITY_PRINCIPAL_SCOPE --scec-chain-mode INITIAL --scec-chain-ordinal 1 --scec-required-disposition ROOT_CONTRACT_REQUIRED --scec-successor-scope INTEGRATED_ROOT_CONTRACT` |
| generatedProfile | generic no-commit external initial dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | corrected INITIAL chain ordinal to zero and replaced placeholders with exact RABA source, trust-chain, terminal-decision and exact-two controls |
| checkerReadAheadConfirmation | all listed dispatch, convergence, return, trace and export checker sources were read before authoring |
| docOnlyNewFields | none |
| claimBoundary | provenance only; no root-contract, runtime or provider acceptance claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch evidence; no public-sync authority.

## Claim Boundary

This baseline authorizes one operator-relayed, external-worker, exact-two,
documentation-only RABA-T0 source-verification return after the packet is
committed and the operator explicitly relays it. It does not execute that
worker, accept a root contract, repair AR1, change source/tests, open RABA-T1 or
DARA-T5, mutate MFRP, call a provider, expose credentials, stage or commit
worker files, publish, push, deploy, or claim runtime or production readiness.
