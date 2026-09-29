# CVF Agent Work Order - ODVR-T2 Representative Operator Value Proof

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-07-12

Batch ID: ODVR-T2-DISPATCH

dispatchBaseHead: `9fa305afd`

executionBaseHead: `99c2875cd`

closureBaseHead: `99c2875cd`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: independent reviewer

## Dispatch Prompt Envelope

Role: delegated worker for ODVR-T2 representative value proof.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_2026-07-12.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture exact committed dispatch HEAD before any edit.

Current-time notes: refresh HEAD, state drift, source paths, and material commit
resolution before measuring.

Do-not-misread notes: measure the same questions twice for each scenario. Do
not edit the composer, optimize the composed path during measurement, spawn
subagents, commit, mutate state, add UI, call providers, publish, or absorb an
outside source.

Required first actions: startup sequence, HEAD/status, paired packet, roadmap,
T0 contract/schema, T1 implementation/completion, source/checker reads, ADIF
rerun, then pre-implementation gate.

Return contract: leave exactly three outputs uncommitted and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Measure whether the committed ODVR readout reduces operator navigation for the
same canonical questions without losing or changing facts.

## Authority Chain

1. `AGENTS.md` and active session front doors.
2. Paired T2 baseline and this work order.
3. ODVR roadmap, T0 contract/schema, and T1 completion review.
4. Current generated state and cited canonical lane artifacts.
5. Canonical AHB contract and commit-steward standard.

## Agent Roles

- worker: execute both measurement paths, record receipts, report; no commit.
- reviewer: independently recompute counts and facts, decide terminal value.
- session-sync steward: update continuity only after material closure.

## Scope / Target / Owner Boundary

### Allowed deliverables

- `docs/evidence/odvr/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_RECEIPT_2026-07-12.json`
- `docs/reviews/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_2026-07-12.md`
- `docs/reviews/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_WORKER_RETURN_2026-07-12.md`

### Forbidden scope

No edit to composer/tests/schema/contract, generated or source session state,
roadmap, baseline/work order, Web/UI/routes, provider/API, checker/hook/CI,
public-sync, registry, or outside-source paths.

## Write Ownership

Worker may create exactly the three allowed deliverables. Any required fourth
path returns to the orchestrator.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| T1 accepted implementation | completion review and `16364f797` | SATISFIED |
| session release | closure sync `9fa305afd` | SATISFIED |
| closed scenario | `odvrT1Closure20260712` canonical state entry | SATISFIED |
| parked/reopen scenario | MAO-LIVE roadmap explicit value verdict and reopen section | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind evidence-only --batch-id ODVR-T2 --title "Representative Operator Value Proof" --date 2026-07-12 --base 9fa305afd --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SATISFIED: ODVR-T1 accepted at 16364f797" --include-worker-return-skeleton --stdout` |
| generatedProfile | evidence-only plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-backed measurement, trace, receipt, and no-mutation controls |
| checkerReadAheadConfirmation | named checker sources read before authoring |
| docOnlyNewFields | receipt-only measurement fields named in paired baseline |
| claimBoundary | dispatch provenance only |

## Required First Reads

Read the mandatory startup/guard/gotcha sequence, paired T2 packet, ODVR
roadmap, T0 contract/schema, T1 helper/tests/completion, current state sources,
MAO-LIVE roadmap, canonical AHB contract, and applicable checker sources.

## Pre-Flight Checks

Capture HEAD/status, run generated-state drift check, verify all source paths
and commits, rerun ADIF, and run the pre-implementation autorun gate.

## Worker Autonomy / No-Question Rule

Repair allowed-output evidence and gate defects. Return only for canonical
source contradiction, forbidden-path need, inability to make the questions
identical, or inability to measure without changing the tested implementation.

## Source Verification Block

Use and independently refresh the paired baseline Source Verification Block.
Receipt fields listed as doc-only evidence fields must not be described as
runtime or schema authority.

## Negative Search And Collision Discipline

| Field | Evidence |
|---|---|
| Exact search command | `rg -n -i --glob '*.md' --glob '*.json' -- 'ODVR-T2|REPRESENTATIVE_OPERATOR_VALUE_PROOF' docs CVF_SESSION governance` |
| Exact roots | governed docs, generated state, and local composer source |
| Same-token collisions | roadmap and dispatch occurrences are authority context; no prior T2 proof artifact exists at dispatch |
| Planned path disposition | three output paths are absent and reserved for this tranche |

## Current Runtime Freshness Verification

At execution start, require `generate_active_session_state.py --check` PASS,
resolve `16364f797`, verify the closed entry and MAO-LIVE roadmap, and validate
the composed JSON against the committed T0 schema. Any drift or unresolved
anchor blocks measurement until classified; do not silently repair owners.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`evaluation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class evaluation --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs/reviews --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

Disclosed defectIds: N/A with reason: resolver returned zero defects.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | source table, ADIF query, route token, trace labels, worker-return headings, evidence comparison |
| gateRunPurpose | confirmatory evidence after source-backed packet authoring |
| claimBoundary | bounded T2 measurement only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

Risk sensitivity: MEDIUM because mismatched questions or incomplete fact sets
could create a false value conclusion.

Intake summary: bounded local evaluation of one committed read-only projection.

Scope classification: LOCAL_EVIDENCE_ONLY_VALUE_PROOF.

Escalation: canonical contradiction, asymmetric question set, invalid receipt,
or any need to edit the tested implementation.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | executionBaseHead captured at start |
| changedSetScope(phase) | exactly three allowed evidence outputs |
| traceScope(phase, actor) | worker trace covers worker measurement and outputs only |
| commitOwner(phase) | nobody during execution; reviewer at CLOSURE |
| crossBatchIsolation | clean worktree and one batch only |
| Before status evidence | clean status at executionBaseHead |
| nextMoveSurfaces | worker must not edit; session steward owns post-review sync |

## Reviewer Closure Conversion

completionReviewPath: optional; reviewer should record the decision in the T2
proof report or worker return unless a separate completion artifact is needed.

reviewerOwnedClosurePaths: allowed repairs, baseline/work-order closure
conversion, roadmap T2 disposition if supported, material commit, and separate
session sync.

## Dual Agent Surface Matrix

| Surface | Disposition | Interface | Authority/risk boundary | Evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | IMPLEMENTED | local CLI and canonical file reads | read-only measurement | JSON receipt and report | no action adapter |
| EXTERNAL_AGENT_CLI_MCP | NOT_IMPLEMENTED | N/A with reason: no external route | no external execution claim | no receipt | fresh authorization required |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_CURRENT

priorVerificationArtifact: `docs/reviews/CVF_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_COMPLETION_2026-07-12.md`

priorVerificationAnchor: material commit `16364f797`

freshRecomputeRequired: yes; trace counts, elapsed time, and facts are new evidence

unicodePathHandling: use literal repository-relative paths and UTF-8-safe readers; new governed text defaults to ASCII

extractedTextAuthority: canonical sources and captured command output only

## Roadmap-to-Work-Order Trace Matrix

| Roadmap T2 requirement | Instruction | Evidence path |
|---|---|---|
| one closed lane | use ODVR-T1 closure scenario | JSON receipt scenario 1 |
| one parked/reopen lane | use MAO-LIVE value-not-proven roadmap scenario | JSON receipt scenario 2 |
| same operator questions | freeze the question set before either path | receipt `operatorQuestionSet` |
| manual and composed traces | run MANUAL first, then COMPOSED, without optimization | receipt trace arrays |
| steps, files, elapsed time | record raw events and recomputable totals | receipt measurements |
| answer correctness | compare every answer to canonical expected facts | receipt fact comparison |
| independent terminal value verdict | reviewer recomputes and decides | proof report reviewer section |
| value threshold | require fewer files and fewer steps with zero fact loss | proof report decision matrix |
| UI boundary | keep UI closed regardless of worker recommendation | report claim boundary |

## Required Artifact Manifest

| Path | Owner | Required content |
|---|---|---|
| `docs/evidence/odvr/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_RECEIPT_2026-07-12.json` | worker | two scenarios, four raw traces, questions, facts, counts, timings |
| `docs/reviews/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_2026-07-12.md` | worker | comparison, recomputation, bounded recommendation |
| `docs/reviews/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_WORKER_RETURN_2026-07-12.md` | worker | checker-safe no-commit return |

## Work-Order Fulfillment Manifest

Exactly three worker-owned outputs: JSON measurement receipt, value-proof
report, and worker return. No optional worker file.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must include purpose, target/source, scope/methodology, findings,
risk/corrective action, executionBaseHead, git status, changed files, tests and
gates, unresolved dissent, claim boundary, Checker Source Read-Ahead Block,
Agent Operation Trace Block, Delta Execution Claim Boundary Control Block,
Public Export Disposition, Epistemic Process Block, compact non-applicable
rescan/corpus/external-intake sections, and the no-commit statement.

## Measurement Protocol

1. Freeze this question set for both paths and both scenarios: current lane
   status/verdict; latest material decision and commit; claim boundary; parked
   or blocked condition and checkable reopen condition when applicable; next
   allowed move; public export disposition; source freshness.
2. Record canonical expected answers before timing either path, with exact
   source anchors. Expected answers are scoring authority, not worker memory.
3. Execute MANUAL first by following mandatory startup/canonical owner paths
   without invoking `run_odvr_readout.py`. Count each explicit file open/read as
   one file read and each operator command or navigation action as one step.
4. Execute COMPOSED using the committed helper/CLI or its injected composer for
   the same scenario. Count the invocation and any additional file inspection.
5. Capture monotonic elapsed milliseconds for each path. Timing is secondary;
   file and step reduction plus exact fact preservation are the pass threshold.
6. Record raw event arrays so reviewer can recompute every total. Do not report
   only percentages.
7. Validate composed outputs against the T0 schema and compare all answer keys.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | refresh sources and freeze questions/expected facts | receipt anchors |
| 2 | run closed-lane MANUAL and COMPOSED traces | raw events and answers |
| 3 | run parked-lane MANUAL and COMPOSED traces | raw events and answers |
| 4 | recompute counts, validate schema, compare facts | receipt summaries |
| 5 | author proof report and worker return | exact three-path manifest |
| 6 | run focused and governance gates | command evidence |

## Acceptance Criteria

- Exactly two scenarios and four traces use the identical frozen questions.
- Raw events recompute to declared step/file totals.
- Every expected and observed fact has a canonical source anchor.
- Both composed outputs validate against the T0 schema.
- `VALUE_PROVEN_BOUNDED` is allowed only if both scenarios reduce file reads
  and steps and preserve every canonical fact.
- Any fact loss/change, mismatched question, stale source, or irreproducible
  count yields `VALUE_NOT_PROVEN` or `BLOCKED_EVIDENCE_INVALID`.
- Elapsed time is reported but cannot override a file/step/fact failure.
- No implementation, UI, provider, public, state, or absorption change occurs.

## Negative And Fail-Condition Scan

Fail on different questions, incomplete facts, cached/manual memory substituted
for reads, uncounted actions, post-hoc path optimization, non-monotonic timing,
schema-invalid output, missing raw events, inferred source facts, extra path,
or implementation PASS presented as value proof.

## Verification Commands

- `python governance/compat/generate_active_session_state.py --check`
- `python -m unittest governance.compat.test_run_odvr_readout -v`
- JSON parse and T0-schema validation for both composed scenario outputs.
- receipt recomputation script executed inline without writing a fourth file.
- `python governance/compat/run_worker_return_fast_gate.py`
- `python governance/compat/check_governed_file_size.py --enforce`
- `git diff --check`
- pre-implementation autorun on the real execution range.

## Evidence Requirements

Exact HEAD/status, frozen questions, canonical expected facts, raw events,
recomputed totals, monotonic timings, schema validation, fact comparison,
secrets scan, exact changed set, and governance command receipts.

## Review Gate

The reviewer independently opens canonical anchors, recomputes all four traces,
reruns schema/fact comparisons, rejects asymmetric questions or hidden reads,
and alone assigns `VALUE_PROVEN_BOUNDED`, `VALUE_NOT_PROVEN`, or
`BLOCKED_EVIDENCE_INVALID`.

## Return-To-Orchestrator Conditions

Return for source contradiction, invalid/missing canonical scenario evidence,
forbidden-path need, inability to create equivalent composed scenario input,
or measurement design requiring implementation change.

## Operator Checkpoint

N/A with reason: operator authorized T2 evidence work. Any UI follow-up still
requires a positive reviewed result and separate operator authorization.

## Closure Checklist

- [x] Exact three-output manifest reviewed.
- [x] Same-question equivalence proven.
- [x] Raw counts independently recompute.
- [x] Both composed outputs are schema-valid.
- [x] Canonical fact mismatches recorded and value is not proven.
- [x] Worker-return fast gate passes.
- [x] Reviewer decision and material commit prepared.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated worker |
| Provider or surface | local private provenance repository |
| Session or invocation | ODVR-T2 execution |
| Working directory | repository root |
| Command or tool surface | read/search/local CLI/timing/JSON validation only |
| Target paths | exactly three evidence outputs |
| Allowed scope source | paired T2 baseline and this work order |
| Before status evidence | clean worktree at executionBaseHead |
| After status evidence | uncommitted evidence outputs plus return |
| Diff evidence | status and diff name-status |
| Approval boundary | no commit; reviewer acceptance required |
| Claim boundary | representative operator value measurement only |
| Agent type | worker |
| Invocation ID | odvr-t2-delegated-worker-2026-07-12 |
| Expected manifest | three paths in Required Artifact Manifest |
| Actual changed set | worker records at return |
| Manifest delta | worker records MATCH or BLOCKED |
| Deletion or rename disposition | N/A with reason: none |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation root | `docs/evidence/odvr/` for receipt plus `docs/reviews/` for human evidence |
| Stable front door | `docs/reference/operator_decision_value_readout/README.md` remains unchanged |
| Durable source files | one immutable JSON receipt and one governed review report |
| Generated aggregate | N/A with reason: no aggregate is created |
| Generator/checker | receipt is parsed, recomputed, and schema cross-checked by inline verification |
| Index update | N/A with reason: bounded evidence does not create a new reference family |
| Public boundary | private provenance only; no public-sync |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | bounded local manual-versus-composed measurement only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - required JSON receipt carries raw trace events and answers |
| actionEvidence | ACTION_EVIDENCE_PRESENT - command, file-read, timing, and schema-validation events are required |
| invocationBoundary | local file reads and committed ODVR CLI/composer only; no provider or outside invocation |
| interceptionBoundary | N/A with reason: no output interception, wrapper, proxy, or runtime enforcement is claimed |
| claimLanguage | T2 may claim only measured navigation reduction and exact fact preservation |
| forbiddenExpansion | no universal agent control, UI, provider, mutation, public, absorption, or production claim |


## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private measurement dispatch. Public-sync boundary: worker must not
copy, commit, or push any T2 artifact to the sibling public repository.

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| ODVR-T2-A1 | `docs/evidence/odvr/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_RECEIPT_2026-07-12.json` | `$.scenarios[0].factsPreserved` | 7 for value proof | 3 | FAIL_VALUE_THRESHOLD |
| ODVR-T2-A2 | `docs/evidence/odvr/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_RECEIPT_2026-07-12.json` | `$.scenarios[1].factsPreserved` | 7 for value proof | 0 | FAIL_VALUE_THRESHOLD |
| ODVR-T2-A3 | `docs/evidence/odvr/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_RECEIPT_2026-07-12.json` | `$.scenarios[*].traces[*].rawEvents` | all declared totals recompute | four of four traces recompute | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_2026-07-12.md` | `Status: REVIEWER_ACCEPTED_VALUE_NOT_PROVEN` | PASS |
| Roadmap state | `docs/roadmaps/CVF_OPERATOR_DECISION_AND_VALUE_READOUT_ROADMAP_2026-07-12.md` | `Status: CLOSED_VALUE_NOT_PROVEN` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no mutation; aggregate drift check passes | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no mutation required | PASS |
| External evidence digest | N/A with reason: internal local measurement | no external evidence | N/A with reason |
| System loop interlock | T2 receipt and canonical sources | value threshold fails without mutation | PASS |
| Session continuity | separate session-sync after material commit | not part of material closure | N/A with reason |

## Claim Boundary

This work order authorizes exactly one two-scenario manual-versus-composed
measurement and three evidence outputs. It does not authorize composer changes,
UI/Web, provider/live, session mutation, autonomous action, public-sync,
outside-source absorption, production readiness, or a value-positive claim
without independent reviewer acceptance.
