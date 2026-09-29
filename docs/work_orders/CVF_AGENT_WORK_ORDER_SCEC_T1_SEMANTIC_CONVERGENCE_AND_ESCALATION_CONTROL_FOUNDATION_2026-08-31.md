# CVF Agent Work Order - SCEC-T1 Semantic Convergence And Escalation Control Foundation

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION

Dispatch base head: `9bdc372a43f91be54a1302f6d1a1493ab1ad8793`

dispatchBaseHead: `9bdc372a43f91be54a1302f6d1a1493ab1ad8793`

closureBaseHead: reviewer captures after accepted worker return

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: one delegated governance implementation worker

Reviewer/closer: orchestrator/reviewer

Worker return path: `docs/reviews/CVF_SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION_WORKER_RETURN_2026-08-31.md`

## Dispatch Prompt Envelope

Role: delegated governance implementation worker for `SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION`.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION_2026-08-31.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture full `git rev-parse HEAD` before edits; stop if it differs from the committed dispatch HEAD supplied by the operator.

Current-time notes: artifact date is 2026-08-31; re-verify current source and checker behavior at execution time.

Do-not-misread notes: this is one integrated governance-foundation implementation. It does not authorize GC-010 product/runtime edits, a T1J-R4 decision, semantic truth scoring, reasoning-trace inspection, provider/live work, public sync, deployment, or production claims.

Required first actions: read `AGENTS.md`, session bootstrap/front door, guard orientation, literal gotchas, paired GC-018 baseline, this packet, every authority and checker source named below; run the pre-implementation gate before editing.

Return contract: implement exactly the Required Artifact Manifest, run focused and repository gates, leave all changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` at the named worker-return path.

providerExecutionAuthority: FORBIDDEN

## Purpose

Implement one forward-only Semantic Convergence And Escalation Control (SCEC)
foundation. The system must constrain whether a problem chain may progress; it
must not prescribe or inspect how agents reason. Use the historical GC-010
T1J-R1-through-R3 chain as a negative replay and make later tranches emit and
validate the control state by default.

This work order is intentionally one integrated implementation tranche. Do not
split it into separate standard, checker, scaffold, or gate-placement tranches.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: EXTERNAL_AGENT_CLI_MCP
parentAssignmentId: SCEC-T1
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 2
usageAvailability: KNOWN_FOR_ADMISSION
quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

## Scope / Target / Owner Boundary

The worker owns the bounded docs/checker/scaffold/catalog/test implementation
listed in the exact artifact manifest. The worker may make in-scope repairs
until all required gates pass. The reviewer independently verifies semantics,
repairs only if necessary, commits material, closes the tranche, and updates
continuity. The operator transports this committed packet to the worker.

No product or runtime source is in scope. GC-010 T1J-R4 remains parked until
this foundation is reviewed, committed, and continuity is closed.

## Authority Chain

1. Operator instruction on 2026-08-31 authorizes raising the CVF foundation,
   then using subsequent tranches as effectiveness tests.
2. `AGENTS.md` requires repeated agent mistakes to become a written rule,
   machine check, and earliest applicable autorun phase gate.
3. The paired GC-018 baseline defines the root defect and accepted semantics.
4. This work order controls the worker implementation and return.

## Agent Roles

- Worker: implement the exact governed change set, tests, and worker return;
  no staging or commit.
- Reviewer/closer: independently inspect source and diff, require corrections,
  run closure gates, and own all commits and continuity changes.
- Operator: transport the packet/return and authorize any scope expansion.

## Required First Reads

- `AGENTS.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION_MEMORY.md`
- active handoff named by the bootstrap read model
- `docs/baselines/CVF_GC018_SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION_2026-08-31.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`
- `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`
- `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`
- `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`
- `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`
- `governance/toolkit/05_OPERATION/CVF_GUARD_REGISTRY_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_GUARD_AUTHORING_STANDARD_GUARD.md`
- every source named by the Source Verification and Checker Source Read-Ahead blocks

## Pre-Flight Checks

1. Capture full `git rev-parse HEAD` and
   `git status --short --untracked-files=all` before edits.
2. Stop if HEAD differs from the committed dispatch head supplied by the
   operator or if pre-existing drift is not exactly operator-disclosed.
3. Confirm the new required paths do not already exist.
4. Run `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation`.
5. Re-run the source searches underlying the baseline instead of trusting
   historical line numbers.
6. Read every checker/catalog/scaffold file before changing it.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "SCEC-T1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "CREATES_OR_CHANGES_AUTHORITY",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "NEW_AUTHORITY"
  },
  "pathFamilies": [
    "docs/baselines",
    "docs/work_orders",
    "docs/reference",
    "docs/reviews",
    "governance/compat"
  ],
  "claims": [
    "forward-only problem-chain progression invariant",
    "machine-enforced escalation and claim-to-proof declaration"
  ],
  "requiredProof": [
    "canonical standard",
    "fail-closed checker",
    "historical replay fixture",
    "focused positive and negative tests",
    "pre-dispatch and local-hook binding",
    "scaffold regression proof",
    "independent reviewer closure"
  ],
  "operatorCheckpoints": [
    "scope expansion",
    "semantic truth scoring",
    "provider or live execution",
    "public sync",
    "deployment",
    "destructive action"
  ],
  "forbiddenEffects": [
    "reasoning trace inspection",
    "automatic semantic truth scoring",
    "product or runtime edits",
    "provider network or live execution",
    "public sync or deployment",
    "worker staging or commit"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Intake Role Routing Decision

routeMode: MULTI_AGENT_MULTI_ROLE

intakeSummary: one integrated local governance-standard, checker, scaffold, and phase-gate implementation

scopeClassification: PROTECTED_GOVERNANCE_IMPLEMENTATION_NO_EXTERNAL_EFFECT_NO_COMMIT

riskSensitivity: high because this change creates active authority and a fail-closed checker on dispatch progression

escalationCondition: any required extra path, semantic-truth scoring, existing-guard weakening, source contradiction, provider/live need, or dirty overlap

The selected role route is one operator-mediated external governance worker
followed by independent local orchestrator/reviewer closure. The requested
profile is `P3_ELEVATED_PROTECTED_GOVERNANCE_PATH`; no mixed-role self-closure
is allowed.

## Semantic Convergence Control Contract

The new canonical standard and checker must define a machine-readable block
with at least these fields:

- `schemaVersion`
- stable `problemKey`
- `chainMode` and integer `chainOrdinal`
- predecessor artifact path plus SHA-256 content hash, or an initial sentinel
- blocker delta sets: `prior`, `resolved`, `retained`, `new`, `reopened`,
  and `current`
- counters for partial-ready closures, reviewer scope expansions,
  same-claim corrections, and non-decreasing blocker transitions
- claim records containing claim ID, claim class, proof class, and evidence
  reference
- required progression disposition and successor scope

The checker must enforce:

1. stable problem identity and monotonic ordinal across successors;
2. exact predecessor path/hash evidence;
3. set reconciliation:
   `prior = resolved union retained` and
   `current = retained union new union reopened`;
4. valid disjointness and no silent blocker disappearance;
5. `ROOT_CONTRACT_REQUIRED` after two partial-ready closures, one reviewer
   scope expansion, or a repeated same-claim correction;
6. `STOP_REASSESS_ARCHITECTURE` after two consecutive non-decreasing blocker
   transitions;
7. no narrow successor token after escalation;
8. no runtime readiness from documentation-only proof;
9. claim-to-proof minimums from the paired baseline;
10. forward-only activation: unchanged historical artifacts are not reopened;
11. quoted/example marker text cannot trigger false positives;
12. fail-closed behavior for malformed or incomplete active blocks.

The checker must only validate observable declarations and evidence shape. It
must not inspect chain-of-thought, score prose quality, or claim to determine
semantic truth.

## Historical Regression Replay

Create the exact JSON fixture named in the artifact manifest. It must encode
the corrected GC-010 T1J-R1/R2/R3 history sufficiently to prove:

- the stable problem chain;
- R2's stated single remaining gap;
- reviewer scope expansion in R2;
- the R3 exactly-once claim and reviewer correction;
- why a narrow R3-style continuation is rejected under the new rule;
- why the required next shape is one integrated root contract rather than
  another single-gap decision.

This fixture is regression evidence, not a rewrite or activation of historical
work orders.

## Claim-To-Proof Mapping

Implement these minimum mappings exactly:

| Claim class | Required minimum proof class |
|---|---|
| `CONCURRENCY_EXACTLY_ONCE` | `EXECUTABLE_ADVERSARIAL_CONCURRENCY_TEST` |
| `CRASH_RECOVERY` | `EXECUTABLE_STATE_TRANSITION_CRASH_TEST` |
| `ORDERING` | `EXECUTABLE_SEQUENCE_ASSERTION` |
| `SCHEMA_COMPATIBILITY` | `EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST` |
| `DOCUMENTATION_ONLY` | `PROPOSAL_ONLY_NO_RUNTIME_READINESS` |
| `OTHER` | `NAMED_OBSERVABLE_PROOF` |

Allowed progression dispositions:

- `CONTINUE_BOUNDED`
- `ROOT_CONTRACT_REQUIRED`
- `STOP_REASSESS_ARCHITECTURE`
- `READY_WITH_EXECUTABLE_PROOF`

Allowed successor scopes:

- `INITIAL_BOUNDED`
- `INTEGRATED_ROOT_CONTRACT`
- `NO_SUCCESSOR`
- `EXECUTABLE_IMPLEMENTATION`

Do not add an allowed narrow-gap successor token after escalation.

## Write Ownership

The worker may create or modify only the paths in the Required Artifact
Manifest. Existing changes on those paths must be disclosed before edits.
All other paths are forbidden.

The paired baseline and this work order are immutable worker input. The worker
must not edit, stage, or commit them.

## Required Artifact Manifest

Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reference/semantic_convergence_control/README.md` | CREATE |
| `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | CREATE |
| `docs/reference/work_order_template/README.md` | MODIFY |
| `docs/reference/guard_orientation/README.md` | MODIFY |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0055.md` | CREATE |
| `docs/reference/agent_defect_intelligence/entries/README.md` | MODIFY |
| `governance/compat/check_semantic_convergence_control.py` | CREATE |
| `governance/compat/test_check_semantic_convergence_control.py` | CREATE |
| `governance/compat/fixtures/semantic_convergence_control/gc010_t1j_r1_r3_replay.json` | CREATE |
| `governance/compat/agent_autorun_command_catalog.py` | MODIFY |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | MODIFY |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | MODIFY |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | MODIFY |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | MODIFY |
| `governance/compat/build_dispatch_packet_scaffold.py` | MODIFY |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | MODIFY |
| `governance/compat/run_worker_return_scaffold.py` | MODIFY |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | MODIFY |
| `governance/compat/test_run_worker_return_scaffold.py` | MODIFY |
| `governance/compat/fixtures/woas_r3_worker_return_skeleton_golden.md` | MODIFY |
| `docs/reviews/CVF_SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION_WORKER_RETURN_2026-08-31.md` | CREATE |

No implicit support file is authorized. If an additional path is materially
necessary, stop with `BLOCKED_WITH_REASON` and name it; do not expand scope.

## Forbidden Path Manifest

Forbidden paths include, without limitation:

- `EXTENSIONS/**`
- product source, runtime source, routes, package exports, provider adapters,
  and product tests
- `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, and handoffs
- `AGENTS.md`, doctrine, operating model, roadmaps, and active baselines/work
  orders
- release/deployment/public-sync paths
- git index, commits, tags, branches, and remotes

## Execution Plan

1. Re-verify source and record the exact clean execution base.
2. Author the canonical SCEC standard with scope, schema, activation,
   invariants, escalation, proof mappings, claim boundary, and adoption rules.
3. Implement a fail-closed checker with a reusable pure validation core.
4. Add the historical regression fixture and exhaustive focused tests.
5. Bind the checker exactly once in common autorun and each named local hook
   catalog at the earliest applicable phase without disabling any existing
   command.
6. Extend dispatch and worker-return scaffolds so new governed chains emit the
   control and outcome blocks by default.
7. Update scaffold tests and golden fixture.
8. Add ADIF-0055 and index it.
9. Update orientation/router docs without duplicating canonical semantics.
10. Create the full worker return, run all gates after final edits, and stop
    without staging or commit.

## Required Tests

At minimum, focused tests must cover:

1. valid initial-chain block;
2. missing block on a newly changed governed work order;
3. stable problem-key mismatch;
4. predecessor hash mismatch;
5. blocker set-algebra mismatch and silent disappearance;
6. one reviewer scope expansion requiring an integrated root contract;
7. two partial-ready closures requiring an integrated root contract;
8. two non-decreasing transitions requiring stop/reassessment;
9. historical T1J R2-to-R3 narrow replay rejection;
10. documentation-only proof prohibited from runtime readiness;
11. every claim-to-proof mapping;
12. quoted/example markers ignored;
13. unchanged historical files excluded from forward-only activation;
14. dispatch and worker-return scaffolds emitting required blocks;
15. checker present exactly once in common autorun and all three hook catalogs;
16. no existing gate selectively removed or suppressed.

Use temporary repositories/directories for file-state tests. Do not mutate the
real workspace as test setup.

## Evidence Requirements

- Standard clauses must map to checker functions and focused tests.
- Every escalation outcome must have at least one positive and one negative
  machine test.
- Historical replay must cite current local source paths and expected failure.
- Catalog changes must prove exact-once inclusion and preservation of all prior
  commands.
- Scaffold examples must parse as valid initial/successor blocks and must not
  fabricate readiness evidence.
- Final command evidence must be captured after the last worker edit.

## Earliest Gate Placement

Add the checker to `_common_commands` in
`governance/compat/agent_autorun_command_catalog.py` so pre-implementation and
later phases receive it according to the existing catalog model. Also add it
exactly once to reviewer-fast, pre-commit, and pre-push local catalogs. Preserve
all existing commands and ordering constraints unless current source requires
a documented equivalent placement.

## Scaffold Requirements

The dispatch scaffold must support emitting a valid initial or successor SCEC
block from explicit arguments. The worker-return skeleton and runner must emit
an outcome block suitable for reviewer correction and successor reconciliation.

Defaults may be conservative, but must never fabricate predecessor hashes,
proof evidence, or readiness. Missing successor facts must fail or generate an
explicit unresolved sentinel rejected before dispatch. Update focused tests and
the golden worker-return fixture accordingly.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: implement and bind the SCEC checker and its
direct scaffold/catalog regression tests only.

Protected paths:

- `governance/compat/check_semantic_convergence_control.py`
- `governance/compat/test_check_semantic_convergence_control.py`
- `governance/compat/fixtures/semantic_convergence_control/gc010_t1j_r1_r3_replay.json`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`
- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `governance/compat/fixtures/woas_r3_worker_return_skeleton_golden.md`

Operator authorization: the operator explicitly authorized raising the CVF
foundation on 2026-08-31, then validating it through subsequent tranches.

Rollback boundary: all changes are local, uncommitted, and limited to the exact
manifest. The reviewer may reject the entire worker diff. The worker must not
delete, weaken, bypass, skip, or conditionally suppress any existing guard.

## System Loop Interlock Routing

- Governance plane: `SEMANTIC_PROGRESSION_CONTROL`
- Existing neighboring plane: `REVIEW_COST_CONTROL`
- Boundary: review-cost controls invocation economics; SCEC controls declared
  problem-chain progression and evidence shape.
- Duplicate-control prohibition: do not add risk/value classification to SCEC
  and do not add semantic progression logic to TPGR or review-cost schemas.
- Runtime interlock: none; this tranche cannot invoke or alter product runtime.

## Finding-To-Governance Disposition

| Defect class | Governance lane | Required disposition |
|---|---|---|
| `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | `STANDARD_ADDED` |
| `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_ADDED` |
| `PHASE_GATE_PLACEMENT_GAP` | `GOVERNANCE_CONTROL_PLANE` | `EARLIEST_APPLICABLE_GATE_ADDED` |

The worker return must reconcile every class to implemented path/test evidence.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Repeated defect promotion order | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | repeated-error and promotion sections | canonical document | learning philosophy | `ACCEPT` |
| Review-cost semantic boundary | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | scope and machine enforcement | canonical document | review-cost standard | `ACCEPT` |
| Historical R2 narrowing and reviewer expansion | `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md` | worker findings and reviewer correction | T1J-R2 packet | worker/reviewer evidence | `ACCEPT` |
| Historical R3 exactly-once claim and correction | `docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md` | worker evidence and reviewer correction | T1J-R3 packet | worker/reviewer evidence | `ACCEPT` |
| Shared early autorun catalog | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` | command catalog | autorun workflow | `ACCEPT` |
| Three local hook catalogs | `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py` | command lists | local catalogs | local hook gates | `ACCEPT` |
| Dispatch scaffold builder | `governance/compat/build_dispatch_packet_scaffold.py` | `build_work_order` | scaffold builder | dispatch scaffolding | `ACCEPT` |
| Worker-return skeleton builder | `governance/compat/build_worker_return_skeleton_scaffold.py` | `build_worker_return_skeleton` | skeleton builder | return scaffolding | `ACCEPT` |
| Worker-return runner | `governance/compat/run_worker_return_scaffold.py` | section list and `main` | scaffold runner | return validation | `ACCEPT` |

The worker must refresh line/symbol evidence against its execution base and
return `BLOCKED_WITH_REASON` for a contradiction; do not invent compatibility.

## Evidence Reuse Control

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md`; `docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md`

priorVerificationAnchor: `b3589ee23e2f2712ab709bba697c403727cf64d2`

freshRecomputeRequired: yes

unicodePathHandling: literal repository paths and UTF-8-safe readers

extractedTextAuthority: current local CVF-governed source only; provider memory or extracted external text is not authority

## Dual Agent Surface Matrix

| Surface | Contract state | Implemented state | Evidence | Disposition | Owner |
|---|---|---|---|---|---|
| Local Codex dispatcher/reviewer | committed packet defines exact SCEC-T1 contract and review gate | implementation absent at dispatch | baseline and this work order | `CONTRACT_ONLY` | orchestrator/reviewer |
| External Claude worker | operator-mediated file transfer conveys the committed packet; return requires local gate evidence | no hidden runtime/MCP capability is claimed | worker return at exact path | `CONTRACT_ONLY` | external worker |

The external surface is a file-transfer execution adapter, not evidence of MCP,
runtime, provider, or automatic cross-agent memory support.

## ADIF Defect Registry Disclosure

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json`
- Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
- Applied entries: `ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`, `ADIF-0020`, `ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`, `ADIF-0044`
- Resolver truncation: `true`; displayed matching set applied, no claim of complete registry scan
- Planned new entry: `ADIF-0055`
- Disposition: `APPLIED`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Commit mode: WORKER_MUST_NOT_COMMIT`; prompt-envelope fields; source-verification columns and dispositions; `Work-Order Fulfillment Manifest`; core-authorization tokens; route JSON; INITIAL review-cost sentinels; worker-return profile literals |
| gateRunPurpose | Gates confirm compliance after source read-ahead; they are not used as the first discovery of packet requirements. |
| claimBoundary | Structural checker preparation does not prove the worker's future implementation or semantic correctness. |

The worker must read the applicable sources again at its actual execution base.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id SCEC-T1 --title "Semantic Convergence And Escalation Control Foundation" --date 2026-08-31 --base 9bdc372a43f91be54a1302f6d1a1493ab1ad8793 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --include-worker-return-skeleton --stdout` |
| generatedProfile | `protected-governance-path` |
| generatedSkeletonStatus | `GENERATED_BUT_REPLACED` |
| manualEditsAfterScaffold | Replaced generic skeleton with bounded SCEC schema, exact manifests, proof matrix, tests, and self-protection authorization. |
| checkerReadAheadConfirmation | Applicable checker sources were read before authoring. |
| docOnlyNewFields | The SCEC block is dispatch authority until worker implementation passes review. |
| claimBoundary | No implemented control or product readiness is claimed by this work order. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | one operator-mediated external governance worker; independent local orchestrator/reviewer/closer |
| phase | committed dispatch to uncommitted worker return |
| baseHeadFor(phase) | dispatchBaseHead=`9bdc372a43f91be54a1302f6d1a1493ab1ad8793`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact 21-path Required Artifact Manifest |
| traceScope(phase, actor) | worker records commands/status/manifest/no-commit evidence; reviewer records independent closure |
| commitOwner(phase) | reviewer/closer; worker commit forbidden |
| crossBatchIsolation | clean worktree at dispatch; no unrelated edits, staging, commits, or residual files |
| nextMoveSurfaces | reviewer updates active handoff/session state only after accepted material commit |

## Reviewer Closure Conversion

Worker completion is not closure. The reviewer must independently verify:

1. the standard does not claim semantic-truth scoring;
2. checker behavior, historical replay, and every negative boundary;
3. exact protected-path diff and no disabled pre-existing command;
4. scaffold output and golden fixture;
5. direct, reviewer-fast, pre-commit, and pre-closure gates;
6. worker HEAD unchanged and no commit;
7. material commit before a separate continuity commit.

Reviewer correction must be explicit and supersede conflicting worker claims.
The worker must not self-approve or convert its return to closed status.

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION_COMPLETION_2026-08-31.md` (optional; reviewer creates only if necessary) |
| reviewerOwnedClosurePaths | worker return and optional completion review; continuity paths only in a separate reviewer commit |
| closureOwner | orchestrator/reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION_WORKER_RETURN_2026-08-31.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

scopeClassification: PROTECTED_GOVERNANCE_IMPLEMENTATION_NO_EXTERNAL_EFFECT_NO_COMMIT

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

publicSyncDisposition: FORBIDDEN

liveRuntimeDisposition: FORBIDDEN

workerSelfSelection: FORBIDDEN

The return must contain:

- exact execution base and final HEAD;
- startup acknowledgment;
- exact changed-path manifest and forbidden-path negative check;
- implementation summary by contract invariant;
- refreshed Source Verification Block;
- Semantic Convergence Outcome block for problem key
  `cvf-semantic-convergence-and-escalation-control`;
- historical replay results;
- claim-to-proof test ledger;
- guard placement and no-suppression evidence;
- scaffold/golden regression evidence;
- Core Guard Self-Protection reconciliation;
- Agent Operation Trace Block;
- Delta Execution Claim Boundary Control Block;
- gate commands and complete exit results;
- risks/corrective actions;
- terminal `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`;
- explicit no-stage/no-commit statement.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator/dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SCEC-T1 dispatch authoring, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | governed reads, source searches, ADIF resolver, scaffold helper, apply_patch, gates, git |
| Target paths | paired SCEC-T1 baseline and work order |
| Allowed scope source | operator instruction to raise the CVF foundation and validate it through successor tranches |
| Before status evidence | HEAD `9bdc372a43f91be54a1302f6d1a1493ab1ad8793`; clean worktree |
| After status evidence | exact two dispatch documents pending orchestrator commit |
| Diff evidence | `git diff --check`; `git status --short --untracked-files=all` |
| Approval boundary | governance dispatch authoring only |
| Claim boundary | repo-local trace only; no implemented SCEC, provider identity, or runtime behavior claim |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `scec-t1-dispatch-2026-08-31` |
| Expected manifest | exact paired baseline and work order |
| Actual changed set | exact paired baseline and work order |
| Manifest delta | MATCH |

The future worker return must also list chronological material actions without
private reasoning or chain-of-thought.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | bounded SCEC-T1 governance foundation dispatch and exact worker manifest |
| claimDisposition | `BOUNDED_CLAIM_WITH_EVIDENCE`: local uncommitted implementation and test evidence only |
| receiptEvidence | `CVF_RECEIPT_PRESENT`: captured base/status, source verification, resolver output, scaffold provenance, and required gates |
| actionEvidence | `ACTION_EVIDENCE_PRESENT`: exact two-file dispatch now and exact 21-path worker manifest later |
| invocationBoundary | local governed reads, authoring, tests, gates, git, and one operator-mediated external worker invocation |
| interceptionBoundary | no IDE/shell/provider interception or runtime enforcement claim |
| claimLanguage | controls declared progression and proof shape; does not judge semantic truth or agent reasoning |
| forbiddenExpansion | product/runtime edits; reasoning-trace inspection; provider/live/public/deployment; automatic GC-010 successor; worker commit |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation storage class | semantic convergence control standard, front door, checker, fixture, and default packet projections |
| Stable reference output | `docs/reference/semantic_convergence_control/README.md`; `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` |
| Worker return output | `docs/reviews/CVF_SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION_WORKER_RETURN_2026-08-31.md` |
| Generated aggregate impact | none; no generated aggregate path is authorized |
| Runtime impact | none; no product/runtime path is authorized |
| Index/front-door updates | `docs/reference/work_order_template/README.md`; `docs/reference/guard_orientation/README.md`; ADIF entries index |
| Layout boundary | one canonical SCEC folder owns semantics; orientation and scaffold files only route/project the contract |

## Verification Commands

At minimum, after final edits run:

```powershell
python -m unittest governance.compat.test_check_semantic_convergence_control
python governance/compat/test_build_dispatch_packet_scaffold.py
python governance/compat/test_run_worker_return_scaffold.py
python governance/compat/test_run_agent_autorun_workflow_gate.py
python governance/compat/check_semantic_convergence_control.py
python governance/compat/check_core_guard_self_protection.py
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase worker-return-fast
git diff --check
git status --short --untracked-files=all
git rev-parse HEAD
```

If a repository wrapper is the canonical current invocation, use it and record
the exact command. Repair all in-scope failures and rerun after the final edit.
Never hide a failure with selective test or catalog suppression.

## Acceptance Criteria

- [ ] All 21 authorized artifacts exist or are updated exactly as required.
- [ ] Canonical standard defines forward activation, schema, set algebra,
  escalation, proof mapping, adoption, and claim boundary.
- [ ] Checker fails closed for malformed active blocks and does not score
  semantic truth.
- [ ] Historical T1J replay rejects the unjustified narrow continuation.
- [ ] All 16 required test families pass.
- [ ] Checker is bound exactly once in common autorun and three local catalogs.
- [ ] Dispatch and worker-return scaffolds emit valid SCEC blocks.
- [ ] No existing check is removed, skipped, weakened, or conditionally hidden.
- [ ] ADIF-0055 records the learning and is indexed.
- [ ] No forbidden path, product/runtime effect, provider/live action, staging,
  or commit occurred.
- [ ] Full worker return passes worker-return-fast and `git diff --check`.

Fail conditions include: prose-only implementation; checker relying only on
keyword presence; global reopening of historical docs; automatic semantic
truth claims; an allowed post-escalation narrow token; missing negative replay;
catalog suppression; scope drift; or worker commit.

## Review Gate

The worker return is evidence, not acceptance. Reviewer closure requires source
inspection, test inspection, independent reruns, and semantic comparison to the
paired baseline. A green structural gate cannot override a failed invariant.

## Closure Checklist

- [ ] Worker changed set matches the exact 21-path manifest.
- [ ] Worker HEAD equals committed dispatch HEAD and no worker commit exists.
- [ ] Reviewer independently validates standard, checker, replay, tests, and
  catalog/scaffold changes.
- [ ] All direct, reviewer-fast, pre-commit, and pre-closure gates pass after
  final accepted edits.
- [ ] Material commit and continuity commit remain separate.
- [ ] GC-010 T1J-R4 stays parked until closure is complete.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only when the exact manifest cannot satisfy the
contract without additional authority, source contradiction, or forbidden-path
change. In-scope implementation/test defects must be repaired and gates rerun
without asking the operator.

## Operator Checkpoint

Stop after the uncommitted worker return. No foundation completion, GC-010
successor, provider call, deployment, or public export is automatic. The
reviewer and operator retain those authorities.

## Worker Autonomy / No-Question Rule

Within the exact manifest and contract, choose maintainable internal structure,
write tests, repair failures, and complete the return without seeking stylistic
approval. Stop rather than infer permission for any additional path or effect.

## Claim Boundary

This packet authorizes a local governance-control implementation only. It does
not authorize observation of private reasoning, automated semantic truth
judgment, GC-010 product changes, provider/live execution, deployment, or
public readiness. Passing gates proves the declared SCEC contract and tests,
not universal correctness of autonomous agents.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: SCEC-T1 is a private provenance foundation tranche. Public export, if
ever desired, requires a separate reviewed public-sync batch.
