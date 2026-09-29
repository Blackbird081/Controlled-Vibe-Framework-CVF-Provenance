# CVF GC-018 Baseline - ACEL G2 Runtime Topology Experiment T1

Memory class: governed-dispatch-baseline

Status: READY_TO_DISPATCH

Batch ID: ACEL-G2-TOPOLOGY-EXPERIMENT-T1

Dispatch base head: `c71176f0af24b804de5cc8e6870c93a493a9f6df`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator selected G2 on 2026-09-16; Local owns technical disposition.

Reviewer owner: Local reviewer/closer.

Worker target: INTERNAL_AGENT shared-workspace implementation worker.

## Purpose

Authorize one experimental, non-production runtime seam that can execute a
hermetic 32-run G2 topology-policy oracle. T1 measures decision-contract
correctness and receipt integrity only; it does not claim that dynamic agent
topology improves real task outcomes.

## Decision / Baseline / Proposed Tranche

Decision: authorize G2 T1 as the smallest reversible experiment under the
existing Control Plane Foundation owner. Baseline: current delegation is
static and current benchmark evidence is proposal-only. Proposed tranche:
implement an isolated contract, fixtures, tests and runner, then emit one
deterministic 32-run receipt for Local review. T2 and production adoption are
not authorized.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G2-TOPOLOGY-EXPERIMENT-T1 --title "ACEL G2 Runtime Topology Experiment Harness And Hermetic 32-Run Oracle" --date 2026-09-16 --base c71176f0af24b804de5cc8e6870c93a493a9f6df --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with exact experimental boundary, eight-path manifest, 32-run matrix and T2 admission rule. |
| checkerReadAheadConfirmation | Work-order, worker-return, trace, Delta, external-intake, corpus, public-disposition and closeability checker owners reviewed. |
| docOnlyNewFields | taskClass; policy; repetition; runtimeEvidence; routeAction; admitted; qualityOracle; orchestrationMetrics |
| claimBoundary | Dispatch provenance only; no production topology or agent-quality claim. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Delegation authority is static | FACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | delegation contract and validators | `DelegationContract` | Control Plane Foundation delegation contract | ACCEPT |
| G2 is Local-accepted ADAPT | FACT | `docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md` | Findings / Position | `G2` | Local completion review | ACCEPT |
| Smallest experiment is 8 x 2 x 2 | ADVISORY_INPUT | `.private_reference/external_reviews/agent_capability_engineering_lab_2026-09-15/AGENT_CAPABILITY_ENGINEERING_LAB_CVF_LOCAL_AUDIT_HANDOFF_v2.md` | experiment gate after audit | `G2` experiment design | external advisory input only | ACCEPT_WITH_LOCAL_BOUNDARY |
| Existing benchmark evidence is proposal-only | FACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/performance.benchmark.harness.contract.ts` | evidence classification | `EvidenceClass` | Control Plane Foundation benchmark contract | ACCEPT |

## Negative Search And Collision Discipline

| Check | Exact search root or command | Result | Disposition |
|---|---|---|---|
| Dispatch path collisions | `Test-Path -LiteralPath docs/baselines/CVF_GC018_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_2026-09-16.md; Test-Path -LiteralPath docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_2026-09-16.md` | both false before authoring | CLEAR |
| Source/test token collision | `rg -n "ACEL-G2-TOPOLOGY-EXPERIMENT-T1|runtime.topology.experiment" EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests` | none before authoring | CLEAR |
| Docs/JSON token collision | `rg -n "ACEL-G2-TOPOLOGY-EXPERIMENT-T1|runtime.topology.experiment" docs --glob "*.md" --glob "*.json"` | none before authoring | CLEAR |
| External evidence collision | `rg -n "32|8 x 2 x 2|topology" .private_reference/external_reviews/agent_capability_engineering_lab_2026-09-15` | advisory experiment shape only | ACCEPT_WITH_LOCAL_BOUNDARY |
| Production topology controller | accepted T0 owner audit across source, tests and docs | no accepted runtime controller found | DO_NOT_INVENT_PRODUCTION_OWNER |

## Experiment Boundary

T1 contains four task classes with two fixtures each, two policies and two
repetitions: exactly 32 hermetic executions. Policy A is fixed preselected
topology. Policy B may choose `NO_DELEGATE`, `DELEGATE`, `PARALLELIZE`,
`RECLAIM` or `ESCALATE` from declared runtime evidence. A correct
`NO_DELEGATE` decision is success.

Every run must first satisfy its deterministic quality oracle and governance
constraints. Only admitted runs may enter comparative summaries. Metrics are
decision correctness, first-pass admission, retry count, simulated context
transfer units, orchestration steps and deterministic integration effort.
Wall-clock values may be recorded but cannot be treated as stable performance
evidence in this hermetic tranche.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES_BOUNDED_EXPERIMENTAL |
| runtimeMutationAuthorized | YES_EXPERIMENTAL_NON_PRODUCTION_ONLY |
| freshnessVerificationMode | SOURCE_TEST_AND_32_RUN_MACHINE_RECEIPT |
| reason | T1 introduces executable experiment code and runs it locally without provider/network effects. |
| requiredFutureAction | A separate T2 work order is required for real agent executions. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Worker execution`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: NONE_RETURNED (`totalCandidates=0`).

## Evidence / Verification

- Exact two-file dispatch diff and clean pre-authoring worktree evidence.
- Focused TypeScript tests, full typecheck and two byte-identical runner runs.
- Exactly 32 unique receipt records reconciled to the closed matrix.
- Local review of quality admission, authority preservation and claim ceiling.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch status, no-commit contract, exact paths, 32-run matrix, coordination binding, trace labels, closeability graph and private export disposition |
| gateRunPurpose | confirm packet shape and machine bindings as evidence before dispatch; not first discovery |
| claimBoundary | checker conformance does not prove experiment correctness or real-agent value |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher |
| Provider or surface | local private CVF workspace |
| Session or invocation | ACEL-G2-TOPOLOGY-EXPERIMENT-T1 baseline authoring, 2026-09-16 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification, collision searches, scaffold helper, ADIF resolver, apply_patch and dispatch gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator message selecting G2 on 2026-09-16 |
| Before status evidence | clean worktree at HEAD `c71176f0af24b804de5cc8e6870c93a493a9f6df` |
| After status evidence | exact two dispatch artifacts pending commit |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | bounded internal hermetic experiment dispatch only |
| Claim boundary | no actual agents, provider/live execution, production routing or public effect |
| Agent type | dispatcher |
| Invocation ID | `acel-g2-topology-experiment-t1-baseline-20260916` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | same two paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes an isolated experimental contract, fixtures, tests,
runner and proposal-only receipt. It does not authorize production export,
existing delegation-contract mutation, live providers, actual subagent
invocations, T2 real-agent trials, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private experimental dispatch with no public artifact authority.
