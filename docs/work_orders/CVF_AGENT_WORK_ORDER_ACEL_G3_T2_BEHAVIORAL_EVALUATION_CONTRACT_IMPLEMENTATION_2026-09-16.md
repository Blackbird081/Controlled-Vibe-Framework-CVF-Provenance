# CVF Agent Work Order - ACEL G3 T2 Behavioral Evaluation Contract Implementation

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

## Dispatch Prompt Envelope

Batch ID: ACEL-G3-T2-BEHAVIORAL-EVALUATION-CONTRACT-IMPLEMENTATION

Dispatch base head: `01a854f7b7ed80c35ab77ba02c7ffd273ae61658`

dispatchBaseHead: `01a854f7b7ed80c35ab77ba02c7ffd273ae61658`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_TO_SET

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Worker: INTERNAL_AGENT implementation and evidence worker.

Role: INTERNAL_AGENT offline contract implementer; never reviewer or closer.

Reviewer/closer: Local reviewer/orchestrator.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_2026-09-16.md`

Worker return path: `docs/reviews/CVF_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_WORKER_RETURN_2026-09-16.md`

Current-time notes: Local selected the separate G3 implementation successor at
clean continuity HEAD `01a854f7b7ed80c35ab77ba02c7ffd273ae61658`.

Do-not-misread notes: implement and test an offline generic contract only. Do
not run real skills, provider/live calls, or mutate package/lifecycle state.

Required first actions: read `AGENTS.md`, startup front doors, guard orientation,
literal gotchas, the paired baseline, this packet, the accepted G3 T1 design,
and applicable checker sources; capture exact HEAD/status; run
pre-implementation before editing.

Return contract: create exactly seven declared outputs, leave them uncommitted
and unstaged, then return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement the accepted G3 generic behavioral-evaluation contract as a
normative reference, pure TypeScript types/grader plus adversarial tests, and a
read-only Python evidence checker plus focused tests. Produce an implementation
audit and a full worker-return packet for Local review.

## Authority Chain

1. `ECOSYSTEM/doctrine/` and `ECOSYSTEM/operating-model/`.
2. `AGENTS.md`, canonical standards, and current continuity.
3. Operator instruction on 2026-09-16 to continue and let Local issue the order.
4. Accepted G3 T1 design completion and machine manifest.
5. Paired GC-018 baseline and this work order.

The relayed Claude worker is `INTERNAL_AGENT` in the shared workspace. Local
owns private-CVF review, bounded repair, terminal disposition, and commits.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| G3 T1 accepted design | `docs/reviews/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md`, SHA-256 `175598c620caf4e106d4dd3b1a68522cc39a6412186109bb64f092d53b765148`, terminal `CLOSED_PASS_BOUNDED_DESIGN_READY` | exact predecessor is accepted and no design blocker remains | RELEASED |
| machine successor manifest | `docs/audits/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json`, SHA-256 `0af2a46edec9e31b879812c0beabead5582e00944db9cf616a904141d640c93e` | four planned paths exist only as approved future manifest | RELEASED |

## Scope / Methodology

Implement only pure offline behavior. Treat fixtures, traces, repeats, baseline
pairs, grader output, and evidence references as immutable data. The grader is
a pure function and must not trust a runner-declared verdict. The Python
checker is read-only and validates supplied package/evidence documents without
editing them.

The four approved successor paths remain unchanged. Add one focused Python
test companion because a new checker without a direct negative suite is not
closeable. This is a test-only closeability correction, not owner expansion.

## Normative Implementation Contract

The reference and TypeScript contract must define:

- fixture identity, canonical input bytes, deterministic/stochastic policy,
  positive/negative class, outcome assertions, process assertions, and an
  explicit allowed-transition table;
- trace provenance, source commit/hash, capture mode (`OFFLINE_SYNTHETIC`,
  `MOCK_REPLAY`, or `LIVE_REFERENCE_ONLY`), expiry, ordered tool/action events,
  and output observations;
- separately invokable trace producer interface and grader, with no shared
  mutable state and no grader consumption of a self-declared pass token;
- immutable result carrying a terminal status, defects, repeat evidence,
  fixture/source hashes, and claim boundary;
- exact result/defect values: `PASS_WITH_EVIDENCE`, `FAIL_WITH_DEFECTS`,
  `INCOMPLETE_TRACE`, `UNDECLARED_TOOL_USE`,
  `STALE_REPLAY_PROVENANCE`, `NONEQUIVALENT_BASELINE_PAIR`, and
  `INSUFFICIENT_REPEAT_EVIDENCE`;
- one passing repeat for deterministic skills and three consecutive passing
  repeats for stochastic skills;
- byte-identical input fixture control for WITH/WITHOUT comparison;
- source-hash invalidation and mock/replay provenance/expiry enforcement;
- no automatic certification and no mutation of input values.

Unknown modes, tokens, transitions, missing fields, invalid dates, inconsistent
hashes, nonconsecutive repeats, or malformed evidence must fail closed.

## Required Negative Tests

At minimum, focused tests must reject:

1. self-grading or reliance on a runner-declared `PASS`;
2. missing required trace event or output observation;
3. undeclared tool/action or forbidden event transition;
4. stale, expired, provenance-free, or source-hash-mismatched replay;
5. unequal WITH/WITHOUT canonical input bytes;
6. fewer than three consecutive passing stochastic repeats.

Also prove a complete positive deterministic case, a complete positive
stochastic case, deterministic replay of grading, input non-mutation, correct
outcome obtained through forbidden process still fails, and source changes
invalidate prior evidence.

## Python Evidence Checker Contract

`check_assf_behavioral_evaluation_evidence.py` must expose a reusable read-only
function and a CLI. Given explicit package/evidence paths or test-injected
roots, it must fail when `uatState: PASSED` declares this behavioral contract
but no existing governed result proves `PASS_WITH_EVIDENCE`; fail on stale
source/fixture hash, absent artifact, malformed/unknown result, insufficient
repeat evidence, non-equivalent baseline, or mock/live overclaim. It must not
require all existing packages to adopt the new contract and must not rewrite
package entries, the generated index, certification state, or evidence files.

The focused Python suite must construct hermetic temporary fixtures and cover
one passing case plus each fail-closed class relevant to evidence admission.
No repository data mutation is permitted.

## Roadmap-To-Work-Order Trace Matrix

| Upstream requirement | Work-order control | Disposition |
|---|---|---|
| G3 design accepted | exact predecessor hash and owner contract | RELEASED_TO_IMPLEMENTATION |
| four exact successor paths | first four worker outputs | BINDING |
| checker requires direct proof | fifth focused test companion | CLOSEABILITY_CORRECTION |
| independent grading | pure separate interfaces and self-grade rejection | BINDING |
| no state-token-as-quality | checker validates evidence only; no certification write | BINDING |
| separate operator checkpoint | worker returns uncommitted; Local reviews | PRESERVED |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G3-T2-BEHAVIORAL-EVALUATION-CONTRACT-IMPLEMENTATION
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
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

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g3-behavioral-evaluation-owner-composition","chainMode":"SUCCESSOR","chainOrdinal":1,"predecessor":{"path":"docs/reviews/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md","sha256":"175598c620caf4e106d4dd3b1a68522cc39a6412186109bb64f092d53b765148"},"blockerDelta":{"prior":["g3_generic_behavioral_owner_not_composed"],"resolved":[],"retained":["g3_generic_behavioral_owner_not_composed"],"new":[],"reopened":[],"current":["g3_generic_behavioral_owner_not_composed"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":1,"nonDecreasingBlockerTransitions":1},"claims":[{"claimId":"ACEL-G3-T2-IMPLEMENTATION-DISPATCH","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_2026-09-16.md"}],"requiredDisposition":"READY_WITH_EXECUTABLE_PROOF","successorScope":"EXECUTABLE_IMPLEMENTATION"}
```

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G3-T2-BEHAVIORAL-EVALUATION-CONTRACT-IMPLEMENTATION","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"NEW_INTERFACE"},"pathFamilies":["docs/baselines/","docs/reference/agent_system_skills/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/","governance/compat/","docs/audits/","docs/reviews/"],"claims":["pure offline contract and checker can implement the accepted G3 design"],"requiredProof":["TypeScript focused tests","TypeScript typecheck","Python checker tests","implementation audit","worker-return fast gate","Local review"],"operatorCheckpoints":["Local closure","provider/live","runtime wiring","public sync","deployment"],"forbiddenEffects":["skill-state mutation","generated-index mutation","provider call","credential access","network effect","runtime action","worker commit","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json","completenessClaimChanged":false}}
```

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| intake summary | operator-selected implementation successor to accepted G3 T1 design |
| scope classification | bounded pure local implementation with documentation and tests |
| risk sensitivity | P2 because evidence may later support UAT, while this tranche cannot mutate state |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` implementation; Local reviews and closes |
| role separation basis | worker creates seven uncommitted outputs; Local independently accepts or rejects |
| escalation condition | source contradiction, forbidden-path need, external effect, or uncloseable gate |

## Worker Autonomy / No-Question Rule

Proceed autonomously within the seven paths. Repair allowed-scope failures by
reading the relevant checker or compiler output. Stop only for a source
contradiction, need to edit a forbidden path, or missing authority that makes a
truthful terminal result impossible.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | selected the G3 implementation successor |
| Local dispatcher/reviewer | froze scope; later reviews, repairs, closes, commits |
| Claude worker | implements seven uncommitted outputs and returns evidence |

## Required First Reads

- `AGENTS.md`, bootstrap/front door, and active handoff.
- guard orientation README and governed-artifact literal gotchas.
- paired baseline, this work order, accepted G3 T1 audit, completion, and manifest.
- ASSF lifecycle/package contracts and implementation/test patterns in Source Verification.
- checker sources named in Checker Source Read-Ahead Block.

## Pre-Flight Checks

Capture full `git rev-parse HEAD` and `git status --short`; require the dispatch
artifacts to be committed and no unrelated changes. Run pre-implementation
against the captured full hash before editing. Confirm all seven output paths
are absent and all forbidden paths remain read-only.

## Write Ownership

Worker owns exactly seven create-only paths in Required Artifact Manifest.
Every other path is read-only. The worker must not stage, commit, delete,
rename, generate aggregates, install dependencies, or edit continuity.

## Execution Plan

1. Perform required reads, base/status capture, path checks, and pre-flight.
2. Author the normative reference before code so types follow accepted rules.
3. Implement immutable TypeScript contracts and a pure grader.
4. Add focused TypeScript positive/negative/adversarial tests and typecheck.
5. Implement the read-only Python checker/CLI and hermetic unit tests.
6. Reconcile contract dimensions to tests and results in the implementation audit.
7. Create the full worker return, run gates, confirm empty staging and unchanged HEAD.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | one INTERNAL_AGENT implements docs, TypeScript, Python, tests, audit, return; never reviews/closes |
| phase | implementation pending Local review |
| baseHeadFor(phase) | dispatchBaseHead=`01a854f7b7ed80c35ab77ba02c7ffd273ae61658`; executionBaseHead=worker capture; closureBaseHead=Local sets |
| changedSetScope(phase) | exact seven worker-owned paths |
| traceScope(phase, actor) | worker records commands, tests, status, exact changed set |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; Local is sole commit owner |
| crossBatchIsolation | no edits outside exact manifest |
| nextMoveSurfaces | worker return to Local only; no automatic successor |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT implementation worker

laneOwnedPaths: exact seven Required Artifact Manifest paths

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return with empty staging and exact changed set

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | one worker authors docs, TypeScript, Python, tests, audit, and return |
| actor | INTERNAL_AGENT worker |
| role set | contract author, implementer, test author, evidence producer; never reviewer/closer |
| Role separation ledger | worker self-checks owned outputs; Local independently accepts/rejects |
| Evidence basis independent of memory | governed predecessor, source files, focused tests, hashes, and gates |
| Gate sequence | pre-implementation; focused tests/typecheck; worker-return fast; Local review |
| Self-review boundary | worker may repair owned paths but cannot close or commit |
| escalation condition | missing authority, source contradiction, forbidden path, or external effect |

## Required Artifact Manifest

Work-Order Fulfillment Manifest: REQUIRED_EXACT_SEVEN_PATHS

| Artifact | Required worker action |
|---|---|
| `docs/reference/agent_system_skills/CVF_ASSF_BEHAVIORAL_EVALUATION_CONTRACT.md` | create normative human contract with owner/dependency/claim boundaries |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts` | create pure immutable TypeScript contract and grader |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/assf.behavioral.evaluation.contract.test.ts` | create focused positive, negative, adversarial tests |
| `governance/compat/check_assf_behavioral_evaluation_evidence.py` | create standalone read-only fail-closed checker and CLI |
| `governance/compat/test_check_assf_behavioral_evaluation_evidence.py` | create hermetic focused checker tests |
| `docs/audits/CVF_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_2026-09-16.md` | create source/result ledger, contract-to-test map, command evidence, limitations |
| `docs/reviews/CVF_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_WORKER_RETURN_2026-09-16.md` | create full no-commit worker return |

No other file may be created, modified, deleted, renamed, staged, or committed.

## Evidence Requirements

- captured full execution base, before/after status, and exact seven-path diff;
- contract-to-source-symbol and contract-to-test mapping;
- concise pass/fail output and exit code for each required command;
- negative-case ledger for all six accepted defect classes;
- evidence that inputs remain unchanged and grading is deterministic;
- proof Python tests use temporary roots and do not mutate repository data;
- explicit zero counts for provider, agent, credential, network, runtime,
  certification/index, public, deployment, stage, and commit effects.

## Acceptance Criteria

- exactly seven worker paths exist and no other path changes;
- normative reference, TypeScript implementation, tests, Python checker, and
  Python tests agree on values, repeat policy, hashes, and fail-closed behavior;
- focused Vitest, `npm run check`, Python unittest, checker help smoke,
  pre-implementation, worker-return fast, and `git diff --check` pass;
- no package/index/lifecycle state or wiring is changed;
- staging is empty and HEAD equals execution base;
- return is truthful `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Findings / Position

Dispatch position: the accepted G3 owner can now be implemented locally. The
additional Python test companion is required because checker behavior must be
directly testable before Local can accept it.

## Review Gate

Local reviews exact outputs and consumes valid focused evidence. Acceptance
requires semantic agreement across docs, TypeScript, Python, and tests; a green
gate alone does not prove the contract is correct.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every criterion is met. Return
`BLOCKED_WITH_REASON` with exact evidence for a source contradiction,
toolchain failure, or need for any forbidden path or authority.

## Operator Checkpoint

The operator already selected this implementation tranche. Stop after the
uncommitted return. Local/operator selection remains required before real
evaluation, UAT/certification mutation, integration, provider/live, runtime,
public sync, deployment, or production.

## Worker Output Checker Read-Ahead Mandate

Before authoring the reference, audit, or return, read the checker sources for
their path family and conditional content. The worker return must derive exact
review headings, trace fields, Delta boundary, public disposition, no-commit
evidence, corpus/value/rescan N/A tokens, and gate evidence from current
checkers rather than copying stale prose.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| Mandatory evidence | Producing role/path | Executing role | Reviewing role | Closeable without forbidden authority |
|---|---|---|---|---|
| normative contract | worker/reference path | worker | Local | YES |
| TypeScript behavior | worker/source and focused test | worker | Local | YES |
| Python checker behavior | worker/checker and focused test | worker | Local | YES |
| implementation ledger | worker/audit path | worker | Local | YES |
| full return and no-commit proof | worker/return path | worker | Local | YES |

No mandatory gate depends on provider/live, credentials, network, runtime,
protected-path mutation, operator action during execution, or worker commit.

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | AGENT_HANDOFF_V60_2026-09-08.md material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | TypeScript/Python source and focused tests | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | audit and worker return disclosures | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact seven worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| focused_typescript | WORKER_RETURN | worker | IMPLEMENTATION | TypeScript source and test | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| focused_python | WORKER_RETURN | worker | IMPLEMENTATION | Python checker and test | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_typescript |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact seven worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_python |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker paths plus optional closure | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer completion path | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Verification Commands

Run from repository root unless a command explicitly changes directory:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
Push-Location EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npx vitest run --config vitest.config.ts tests/assf.behavioral.evaluation.contract.test.ts
npm run check
Pop-Location
python -m unittest governance.compat.test_check_assf_behavioral_evaluation_evidence
python governance/compat/check_assf_behavioral_evaluation_evidence.py --help
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

Do not run the full release bundle: this tranche neither needs nor authorizes
provider/live proof. Record exact exit codes and concise outputs in the audit
and return.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_WORKER_RETURN_2026-09-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk /
Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution
Claim Boundary Control Block; Public Export Disposition; executionBaseHead;
git status --short; Changed Files; Command Evidence; No-Commit Statement.

Conditional blocks must appear with accurate `N/A with reason` dispositions:
External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus
Completeness And Report Integrity; Finding-To-Governance Learning Disposition;
Epistemic Process Block; Machine Closure Package.

The return must use terminal `COMPLETE_PENDING_REVIEW` only if all seven paths
exist, all focused gates pass, changed-set manifest matches, staging is empty,
and HEAD equals captured execution base. Otherwise use `BLOCKED_WITH_REASON`.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_COMPLETION_2026-09-16.md` (Local-owned only if needed) |
| reviewerOwnedClosurePaths | work-order status, optional completion review, continuity exact-hash projection if accepted |
| closureOwner | Local reviewer/orchestrator |
| workerCommitPermission | FORBIDDEN |

Local applies `EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`: inspect
the seven outputs and consume valid test evidence. A rerun requires a named
contradiction, expected information gain, or safety reason.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0007, ADIF-0016,
ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049 and
ADIF-0006.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | ready status, first prompt section, source columns, successor convergence fields, route enums, exact return contract, closeability graph, trace fields, and forbidden provider authority |
| gateRunPurpose | confirm packet evidence and literal shape before dispatch |
| claimBoundary | checker compliance does not prove implementation correctness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| G3 implementation is explicitly the next separate checkpoint | DEPENDENCY | `docs/reviews/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md` | Terminal Decision and Acceptance Matrix | exact successor boundary | Local completion | ACCEPT |
| accepted behavioral dimensions and negative cases | CONTRACT | `docs/audits/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json` | `behavioralContract`; `negativeCases`; `evidenceFlow` | G3 machine design | design manifest | ACCEPT |
| lifecycle remains certification/UAT authority | AUTHORITY | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `certificationState`; `uatState` | lifecycle contract | ACCEPT |
| package fields are existing schema | SCHEMA | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `acceptanceEvidence`; `evidenceRequirements`; `uatState` | package contract | ACCEPT |
| direct pure TypeScript pattern exists | IMPLEMENTATION_PATTERN | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/g2.t2.discriminating.task.contract.ts` | exported parser/evaluator | pure fail-closed contract | G2 T2 source | ACCEPT |
| focused Vitest pattern exists | TEST_PATTERN | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/g2.t2.discriminating.task.contract.test.ts` | test suites | adversarial offline fixtures | G2 T2 tests | ACCEPT |
| read-only checker and hermetic unittest pattern exists | CHECKER_PATTERN | `governance/compat/check_assf_certified_metadata_admission.py` | `check` and CLI; paired test file | injected roots and violations | ASSF admission checker | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| seven exact worker paths | each returned `False` under `Test-Path` before authoring | NO_COLLISION |
| existing generic behavioral owner | accepted T1 bounded search found none | IMPLEMENT_ACCEPTED_OWNER |
| adjacent lifecycle/admission/release/provider owners | accepted T1 overlap matrix | COMPOSE; DO_NOT_DUPLICATE |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G3-T2-BEHAVIORAL-EVALUATION-CONTRACT-IMPLEMENTATION --title "ACEL G3 T2 Behavioral Evaluation Contract Implementation" --date 2026-09-16 --base 01a854f7b7ed80c35ab77ba02c7ffd273ae61658 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key acel-g3-behavioral-evaluation-owner-composition --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/reviews/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md --scec-predecessor-sha256 175598c620caf4e106d4dd3b1a68522cc39a6412186109bb64f092d53b765148 --scec-required-disposition READY_WITH_EXECUTABLE_PROOF --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | generic no-commit successor dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact contract, closeability test companion, seven-path manifest, focused gates, and forbidden boundaries |
| checkerReadAheadConfirmation | dispatch/convergence/routing/closeability/trace/handoff/provider/Delta families |
| docOnlyNewFields | normativeImplementationContract; pythonEvidenceCheckerContract |
| claimBoundary | dispatch only; no implementation pass is claimed |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer/orchestrator acting as dispatcher |
| Provider or surface | private CVF workspace only |
| Session or invocation | ACEL G3 T2 implementation dispatch, 2026-09-16 |
| Working directory | repository root |
| Command or tool surface | startup/source reads, current searches, hashes, ADIF resolver, scaffold stdout, apply_patch, dispatch gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator instruction to continue after accepted G3 T1 closure |
| Before status evidence | clean worktree at HEAD `01a854f7b7ed80c35ab77ba02c7ffd273ae61658` |
| After status evidence | exact two dispatch artifacts pending dispatcher commit |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | internal offline implementation dispatch only |
| Claim boundary | no implementation result, provider/live, runtime, public, or deployment claim |
| Agent type | dispatcher |
| Invocation ID | `acel-g3-t2-behavioral-contract-implementation-dispatch-20260916` |
| Expected manifest | paired baseline and work order |
| Actual changed set | same two paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | offline contract/checker implementation dispatch |
| claimDisposition | CLAIM_REJECTED: no implementation behavior is claimed before worker evidence and Local review |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no evaluator, agent, provider, or runtime receipt exists |
| actionEvidence | ACTION_EVIDENCE_PRESENT: accepted predecessor hashes, path absence, and dispatch gates only |
| invocationBoundary | local reads, hashes, document edits, and governance gates |
| interceptionBoundary | no direct interception, wrapper, runtime gate, provider call, or agent action |
| claimLanguage | authorized for implementation, never implemented or behaviorally proven |
| forbiddenExpansion | certification/index mutation, provider/live, runtime, public, deploy, production |

## Finding-To-Governance Learning Disposition

Do not add a global rule, hook, or catalog entry. The Python test companion is
the only closeability correction. Any reusable defect is recorded in the audit
for Local disposition. Runtime/provider/cost learning is `N/A_WITH_REASON`.

## Epistemic Process Block

Epistemic Process Applicability: BOUNDED_GOVERNANCE_IMPLEMENTATION

Expected Result / Prediction: the accepted owner design can be represented as
pure immutable contracts with fail-closed graders and a read-only evidence
admission checker without changing lifecycle authority.

Evidence Comparison Requirement: focused TypeScript/Python tests map every
contract dimension and negative class to observed pass/fail behavior.

Contradiction Handling Requirement: block on authority or model mismatch;
never weaken a negative case or mutate a forbidden path to obtain green tests.

Claim Update Requirement: report implementation-ready pending Local review, or
a precise blocker; never claim real-skill behavioral quality.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external research or repository intake |
| Matching local-view guard | N/A with reason: no external input is being absorbed |
| Owner surface | Local reviewer/orchestrator |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external knowledge enters this tranche |
| Claim boundary | Claude is an INTERNAL_AGENT because it works in the shared private workspace |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/reviews/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md"}
```

## Foundation Storage Layout Block

The seven outputs are flat governed reference, source, test, audit, and review
files. No durable store, queue, runtime state, registry, generated aggregate,
rebuild pipeline, relocation, or directory split is created. The fifth path is
the direct test companion to its fourth-path checker.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: new contract and checker behavior must be proved by fresh
focused TypeScript and Python tests at the worker execution base.

unicodePathHandling: USE_REPOSITORY_ROOT_AND_LITERAL_PATHS_WITHOUT_RELOCATION

extractedTextAuthority: N/A with reason

Reuse only the exact accepted G3 T1 completion, audit, and JSON manifest at the
recorded hashes; re-read current ASSF and implementation-pattern sources rather
than copying historical conclusions. All new text/code uses UTF-8 and ASCII
identifiers/tokens. The workspace Unicode path is handled by normal repository-
root commands; no path relocation, byte conversion, or extracted-text proxy is
authorized. Reused evidence proves design authority only, never implementation
PASS.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO_NEW_RUNTIME_CLAIM |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | clean HEAD, predecessor hashes, current source reads, exact path checks, and focused offline gates |
| reason | accepted design is current, while evaluator/runtime integration remains unimplemented and forbidden |
| requiredFutureAction | Local review plus a separate work order before real evaluation or runtime wiring |

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: offline behavioral evidence contract implementation.

Target lifecycle state: unchanged; no package or skill transition.

Prior phase evidence: accepted G3 T1 owner-composition design.

Next forbidden skip: no UAT update, certification, activation, runtime,
provider, or production promotion in this tranche.

Runtime/provider proof: N/A with reason: explicitly forbidden.

Claim boundary: the checker can validate supplied evidence but cannot mutate or
admit a real package in this work order.

## Closure Checklist

- [ ] Worker captured exact execution base and clean dispatch status.
- [ ] Exactly seven worker-owned paths exist; every other path is unchanged.
- [ ] TypeScript focused tests and typecheck pass.
- [ ] Python checker tests and help smoke pass.
- [ ] Contract/test/defect ledger is complete and consistent.
- [ ] Pre-implementation and worker-return fast gates pass.
- [ ] Staging is empty, HEAD unchanged, and no commit occurred.
- [ ] Local reviewer records the terminal disposition.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `DISPATCH_READY` is the required pre-execution state | PASS |
| Completion or reviewer artifact | Local-owned future completion | N/A with reason: implementation has not run | N/A with reason |
| Roadmap state | active ACEL continuity | G3 T2 is operator-selected and intentionally open | PASS |
| Registry JSON | `docs/corpus-intelligence/registry/entries/acel-g3-t1-behavioral-evaluation-owner-composition-design.json` | GC-051 already covers the declared successor paths; mutation forbidden | PASS |
| Registry Markdown | `docs/audits/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_2026-09-16.md` | accepted human design and successor manifest | PASS |
| External evidence digest | N/A with reason: no external evidence | zero external inputs | N/A with reason |
| System loop interlock | no runtime consumer | runtime forbidden | N/A with reason |
| Session continuity | active handoff/front doors | N/A with reason: Local projects dispatch commit after these gates | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| predecessor | accepted G3 T1 exact hash | completion and manifest hashes match | PASS |
| worker scope | exact seven create-only paths | seven paths declared; all absent before dispatch | PASS |
| closeability | checker has focused test owner | fifth companion path explicitly authorized | PASS |
| provider authority | forbidden | zero calls and ceiling zero | PASS |
| state mutation | forbidden | package/index/lifecycle paths excluded | PASS |
| worker commit | forbidden | Local remains sole commit owner | PASS |

## Claim Boundary

This work order authorizes exactly seven uncommitted offline implementation and
evidence outputs. It does not authorize real evaluator runs, skill/package or
certification/index mutation, provider/live/network/credential access, runtime
wiring, hook/CI/release integration, public sync, deployment, production, or an
automatic successor tranche.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private offline implementation dispatch; public-sync is outside scope.
