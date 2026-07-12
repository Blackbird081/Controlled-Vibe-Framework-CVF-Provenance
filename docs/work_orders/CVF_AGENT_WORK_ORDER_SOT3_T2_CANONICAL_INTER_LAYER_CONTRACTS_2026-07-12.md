# CVF Agent Work Order - SOT3-T2 Canonical Inter-Layer Contracts

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-12

Work order ID: SOT3-T2

dispatchBaseHead: `cc64c8e07`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

## Dispatch Prompt Envelope

Role: documentation-contract worker. Dispatcher and reviewer/closer remain separate.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T2_CANONICAL_INTER_LAYER_CONTRACTS_2026-07-12.md`.

Commit mode: WORKER_MUST_NOT_COMMIT

Base: capture executionBaseHead with `git rev-parse --short HEAD` before edits.

Current-time notes: T0R topology and T1 owners are accepted; this tranche
creates documentation contracts only.

Do-not-misread notes: do not create TypeScript, JSON Schema, tests, runtime,
guards, checkers, packages, provider calls, or public artifacts.

Required first actions: read startup surfaces, roadmap, paired baseline, this
work order, T0R/T1 accepted evidence, TKG-T1, skill truth-packet standard, and
retained contract sources; capture HEAD/status and verify dependencies.

Return contract: `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON`, exactly
five outputs, gate evidence, actual changed set, and unchanged HEAD.

## Purpose

Create one CVF-owned documentation contract family for the complete
Refinery-to-Kernel-to-Flow chain, with explicit authority, field minimums,
status transitions, compatibility, and fail-closed negative cases.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-T2 --title "Canonical Inter-Layer Contracts" --date 2026-07-12 --base cc64c8e07 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | no-commit documentation-contract worker |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Filled authority, dependency, new fields, contract inventory, invariants, exact paths, handoff, verification, acceptance, and claim boundaries. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_truth_foundation_claim_guard.py` |
| docOnlyNewFields | SourceEnvelope; RefineryPacket; KernelEvaluationRequest; KernelDecision; TruthReceipt; TruthReference; DistributionPackage; FeedbackProposal |
| claimBoundary | Documentation contract creation only; no runtime or implementation proof. |

## Authority Chain

- Operator instruction: continue after accepted SOT3-T1.
- Roadmap: `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md`.
- Baseline: `docs/baselines/CVF_GC018_SOT3_T2_CANONICAL_INTER_LAYER_CONTRACTS_2026-07-12.md`.
- T1 material closure: `520ffb4cc`.
- T1 completion: `docs/reviews/CVF_SOT3_T1_COMPLETION_REVIEW_2026-07-12.md`.
- Upstream doctrine: `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`.

## Agent Roles

- Operator: owns future runtime/implementation authorization.
- Dispatcher: authors and validates this packet.
- Worker: creates the five documentation/review outputs without commit.
- Reviewer/closer: independently validates contract semantics and commits accepted material.

## Scope / Target / Owner Boundary

Allowed worker writes are exactly the five paths in Planned Worker Fulfillment
Manifest. The first three create the new CAP-01 documentation owner family;
the fourth reconciles sources/collisions; the fifth is the worker return.

Forbidden: every other path, including TypeScript, JSON/YAML schemas, tests,
guards, checkers, package files, generated state, roadmap/session, retained
source, provider/live, public-sync, stage, commit, or push.

Risk ceiling: HIGH_DOC_CONTRACT_ONLY.

## Worker Autonomy / No-Question Rule

Proceed autonomously for allowed reads, five-output authoring, and owned-output
gate repair. Return blocked for source drift, authority conflict that cannot be
resolved without operator choice, forbidden-path need, or scope expansion.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`canonical inter-layer contract authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "canonical inter-layer contract authoring" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs/work_orders --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Required First Reads

1. startup/session/handoff and guard-orientation surfaces;
2. paired roadmap and baseline;
3. this work order;
4. T0R completion, recommendation, and semantic matrix;
5. T1 completion, owner map, and conversion ledger;
6. TKG-T1 truth-foundation contract;
7. skill truth-packet standard and Guard Contract receipt-binding source;
8. retained Refinery/Kernel/Flow README, TREEVIEW where present, and contract specs.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
git cat-file -e 520ffb4cc^{commit}
python governance/compat/generate_active_session_state.py --check
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1 owner reconciliation accepted | VALUE_SET | `docs/reviews/CVF_SOT3_T1_COMPLETION_REVIEW_2026-07-12.md` | Disposition | `REVIEWER_ACCEPTED_BOUNDED` | T1 review | ACCEPT |
| CAP-01 is new architecture owner candidate | VALUE_SET | `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md` | Owner-Decision Token Summary | `CAP-01` | T1 owner map | ACCEPT |
| CAP-04 and CAP-09 enrich TKG-T1 | VALUE_SET | `docs/reviews/CVF_SOT3_T1_COMPLETION_REVIEW_2026-07-12.md` | Repair Verification | `CAP-04` | T1 review | ACCEPT |
| retained runtime direct import rejected | VALUE_SET | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | Source Conversion Matrix | `Truth Kernel strict-mode package code` | TKG-T1 | ACCEPT |
| T2 is canonical contract tranche | VALUE_SET | `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md` | Tranche Plan | `SOT3-T2` | SOT3 roadmap | ACCEPT |

## New Doc-Only Fields

| New item | Required minimum |
|---|---|
| `SourceEnvelope` | identity, source type, owner, capture time, scope, purpose, confidentiality, content hash, raw reference |
| `RefineryPacket` | source references, normalized records, duplicate/conflict sets, findings, integrity, lineage, rule manifest, status, failures |
| `KernelEvaluationRequest` | packet hash/reference, policy/rule versions, evidence, obligations, verification mode, requested decision context |
| `KernelDecision` | ACCEPT, REJECT, ESCALATE, REQUIRE_ADDITIONAL_EVIDENCE plus reasons and failed obligations |
| `TruthReceipt` | evaluated content hash, decision, evidence/obligation/result bindings, versions, timestamps, predecessor hash, receipt hash |
| `TruthReference` | receipt-bound stable reference, scope, version, validity, supersession, revocation state |
| `DistributionPackage` | recipient/role/task/phase, truth references, dose, restrictions, expiry, routing decision, acknowledgement |
| `FeedbackProposal` | observation, target reference, proposed change, evidence, proposer, review status, no-direct-mutation flag |

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| T0R architecture | `docs/reviews/CVF_SOT3_T0R_COMPLETION_REVIEW_2026-07-12.md` | `ae7d53385` | REVIEWER_ACCEPTED_BOUNDED |
| T1 ownership | `docs/reviews/CVF_SOT3_T1_COMPLETION_REVIEW_2026-07-12.md` | `520ffb4cc` | REVIEWER_ACCEPTED_BOUNDED |
| continuity release | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `cc64c8e07` | T2 packet authoring next |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output | Verification | Status |
|---|---|---|---|---|
| canonical inter-layer contracts | New Doc-Only Fields | contract-chain reference | eight-contract inventory | PASS |
| no duplicate authority | Contract Authority Matrix | architecture front door | producer/consumer uniqueness | PASS |
| fail-closed behavior | Contract Invariants | invariant/negative-case reference | negative-case count and coverage | PASS |
| no implementation | Scope | all outputs | changed-set inspection | PASS |

## Contract Authority Matrix

| Artifact | Sole producer | Allowed consumers | Forbidden producer |
|---|---|---|---|
| SourceEnvelope | governed intake adapter | Refinery | Flow, Kernel |
| RefineryPacket | Refinery | Kernel | Flow |
| KernelDecision | Kernel | Refinery adapter, Flow, governance | Refinery, Flow |
| TruthReceipt | Kernel | Flow, guards, consumers | Refinery, Flow, caller |
| TruthReference | Kernel | Flow and governed consumers | Refinery, Flow |
| DistributionPackage | Flow | governed recipient | Kernel, Refinery |
| FeedbackProposal | Flow/consumer under policy | governed reviewer/owner | direct authority store mutation |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | accepted T0R/T1 evidence, current CVF doctrine, retained contract specifications |
| Scope classification | LEGACY_EXTERNAL_ABSORPTION_DOCUMENTATION_CONTRACT_AUTHORING |
| Intake role | no-commit documentation-contract worker |
| Provider surface | operator-selected local worker; no provider authority |
| Reviewer role | CVF reviewer validates and commits accepted documentation contracts |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Escalation condition | unresolved authority conflict, source drift, forbidden-path need, operator-only semantic choice, or scope expansion |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| selected role route | dispatcher -> documentation-contract worker -> CVF reviewer/closer |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit documentation-contract worker -> CVF reviewer/closer |
| phase | SOT3-T2 documentation contract authoring |
| baseHeadFor(phase) | dispatchBaseHead=`cc64c8e07`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_MUST_CAPTURE_AT_CLOSURE` |
| changedSetScope(phase) | exactly five planned outputs |
| traceScope(phase, actor) | reads, source mappings, contract decisions, gates, changed set, no-commit evidence |
| commitOwner(phase) | worker=WORKER_MUST_NOT_COMMIT; reviewer owns accepted commit |
| crossBatchIsolation | no runtime/schema/test/guard/checker/package/session/public paths |
| nextMoveSurfaces | worker does not edit continuity; reviewer decides after acceptance |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md`

reviewerOwnedClosurePaths: this work order; five outputs; roadmap/continuity only after acceptance.

pendingStatusTokensAllowedBeforeReview: COMPLETE_PENDING_REVIEW, COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW, DRAFT, HOLD_*

forbiddenClosedEquivalentResidue: pending worker status or runtime/readiness claim

predecessorClosureFactSource: T1 material commit `520ffb4cc`

## Planned Worker Fulfillment Manifest

| Artifact | Required action |
|---|---|
| `docs/reference/sot_three_layer/README.md` | create compact canonical front door and owner/authority map |
| `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` | define all eight field/status/producer/consumer contracts |
| `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | define fail-closed invariants and at least 12 negative cases |
| `docs/reviews/CVF_SOT3_T2_CONTRACT_SOURCE_RECONCILIATION_2026-07-12.md` | map every absorbed field/rule to retained and current sources, with collisions/exclusions |
| `docs/reviews/CVF_SOT3_T2_WORKER_RETURN_2026-07-12.md` | checker-safe pending-review return |

Every other worker path is forbidden.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | compact front door plus two canonical contract references and two dated review artifacts |
| Storage decision | new `docs/reference/sot_three_layer/` owner family authorized by T1 CAP-01 decision |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | documentation owner only; runtime owners remain future candidates |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Contract Invariants

Carry all ten baseline invariants. Each invariant must map to at least one
negative case and one contract field/status rule. Undefined or empty required
collections fail closed; version/hash/reference mismatches reject or escalate;
expired/revoked proof cannot distribute; feedback never mutates authority.

## Verification Commands

```powershell
python governance/compat/generate_active_session_state.py --check
python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_truth_foundation_claim_guard.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
git rev-parse --short HEAD
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_truth_foundation_claim_guard.py` |
| literalTokensReviewed | DISPATCH_READY; New Doc-Only Fields; Planned Worker Fulfillment Manifest; WORKER_MUST_NOT_COMMIT; NOT_AUTHORIZED |
| gateRunPurpose | confirm contract-dispatch and worker-output shape after checker review |
| claimBoundary | checker conformance does not prove contract or runtime behavior |

## Execution Plan

1. Verify clean execution base and accepted T0R/T1 dependencies.
2. Read current doctrine and retained contract sources.
3. Create the compact owner front door and authority map.
4. Define the eight contracts, field minimums, statuses, and transitions.
5. Map ten invariants to at least twelve negative cases.
6. Produce field/source reconciliation with collision and exclusion decisions.
7. Run gates and return exactly five files without staging or committing.

## Write Ownership

Worker owns only the five manifest paths, create-only then modify-listed for
gate repair. Worker must not stage or commit.

## Evidence Requirements

- exact eight-contract inventory;
- field-level source and collision reconciliation;
- producer/consumer and authority uniqueness;
- status and transition tables;
- TKG-T1 and skill truth-packet compatibility;
- at least 12 negative cases with expected fail-closed outcome;
- exactly five changed files and unchanged HEAD.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one chain can preserve TKG-T1 doctrine while
adding the missing three-module boundaries without duplicate authority.

Evidence Comparison Requirement: compare every field/invariant against T0R,
T1, TKG-T1, skill truth packet, Guard receipt collision, and retained specs.

Contradiction Handling Requirement: unresolved authority or field conflict
blocks the affected contract and remains explicit.

Claim Update Requirement: mark every proposed field/rule absorbed, adapted,
new doc-only, rejected, deferred, or blocked.

## Review Gate

Reviewer independently checks authority uniqueness, field/source fidelity,
negative-case coverage, TKG-T1 compatibility, and forbidden runtime claims.

## Closure Checklist

- [ ] exactly five outputs;
- [ ] eight contracts complete;
- [ ] one canonical producer/consumer chain;
- [ ] ten invariants mapped;
- [ ] at least 12 negative cases;
- [ ] source reconciliation complete;
- [ ] no runtime/schema/test/guard/checker mutation;
- [ ] worker HEAD unchanged.

## Return-To-Orchestrator Conditions

Return blocked for source drift, unresolved authority conflict, forbidden-path
need, materially new operator choice, or scope expansion.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC-01 | exactly eight canonical contract types | inventory |
| AC-02 | unique authority and producer/consumer mapping | authority matrix |
| AC-03 | SourceEnvelope-first persistent lineage | fields/invariants |
| AC-04 | Refinery deterministic no-AI/no-truth | boundary rules |
| AC-05 | Kernel-only decision/receipt/reference | authority rules |
| AC-06 | Flow post-Kernel-only and receipt-bound | distribution rules |
| AC-07 | feedback proposal cannot mutate authority | lifecycle rules |
| AC-08 | empty/mismatch/replay/expiry cases fail closed | 12+ negative cases |
| AC-09 | no runtime claim or forbidden change | status/diff evidence |

## Fail Conditions

| Failure | Action |
|---|---|
| duplicate canonical type or producer | revise before return |
| guessed existing runtime field | mark new doc-only or block |
| empty required collection passes | reject contract draft |
| receipt not content/context bound | reject contract draft |
| direct feedback mutation | reject transition |
| extra path, stage, or commit | reviewer rejects return |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-T2 dispatch authoring, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | reads, rg, governance gates, apply_patch, git |
| Target paths | roadmap, paired baseline, this work order |
| Allowed scope source | operator instructed continuation after T1 acceptance |
| Before status evidence | base `cc64c8e07`; clean worktree |
| After status evidence | T2 packet pending validation |
| Diff evidence | git status and staged diff before commit |
| Approval boundary | documentation-contract dispatch only |
| Claim boundary | no runtime/schema/test/guard/checker/package/provider/public/readiness claim |
| Agent type | dispatcher |
| Invocation ID | `sot3-t2-dispatch-2026-07-12` |
| Expected manifest | roadmap; T2 baseline; T2 work order |
| Actual changed set | roadmap; T2 baseline; T2 work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | SOT3-T2 documentation contract dispatch only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - T0R/T1 accepted reviews |
| actionEvidence | ACTION_EVIDENCE_PRESENT - roadmap, baseline, work order |
| invocationBoundary | local documentation authoring only |
| interceptionBoundary | no runtime/provider/filesystem interception claim |
| claimLanguage | bounded documentation contract creation |
| forbiddenExpansion | runtime, schemas, tests, guards, checkers, packages, provider/live, public-sync, release, readiness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal contract design based on private retained evidence.

## Claim Boundary

This work order authorizes exactly five no-commit documentation/review outputs.
It does not authorize runtime, schemas, tests, guards, checkers, packages,
provider/live proof, public-sync, release, or production readiness.

## Operator Checkpoint

SATISFIED_FOR_SOT3_T2_DOCUMENTATION_CONTRACTS. The operator instructed
continuation after T1 acceptance. All implementation remains outside scope.
