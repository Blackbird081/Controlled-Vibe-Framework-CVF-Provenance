# CVF GC-018 Baseline - ACEL G2 T2 Real-Agent Experiment Design

Memory class: governed-dispatch-baseline

docType: baseline

Status: AUTHORIZED_READY

Batch ID: ACEL-G2-T2-REAL-AGENT-EXPERIMENT-DESIGN

Dispatch base head: `9cf7fd62e988bd760a27a2e585b5c6a543cdbbc5`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer/closer: Local

Worker target: INTERNAL_AGENT design and source-verification worker

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize a bounded design-and-qualification pass for the ACEL G2 T2
real-agent topology experiment. The worker must determine whether current CVF
owners can support a truthful fixed-versus-dynamic real-agent comparison,
qualify a non-duplicate candidate task, and freeze an execution-ready design
without running an agent, resolving a credential, or making a provider call.

## Operator Authorization

The operator explicitly approved `G2-T2` on 2026-09-16 after T1 closed at
material commit `0d31159f3e77d79253b8075daf00e8fdf9851d66` and continuity commit
`9cf7fd62e988bd760a27a2e585b5c6a543cdbbc5`.

This authorization opens design and candidate qualification only. A later
execution packet must separately declare any actual agent, provider, live,
credential, quota, network, or production authority.

## Target / Source

- T1 completion and accepted claim ceiling:
  `docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_COMPLETION_2026-09-16.md`.
- T1 executable decision contract:
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/runtime.topology.experiment.contract.ts`.
- Existing MAO live comparison and its reopen conditions:
  `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md`.
- Existing live comparison bridge:
  `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts`.
- Existing operational launcher:
  `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts`.
- Existing Model Gateway live harness:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`.
- Existing provider grant owner:
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts`.

## Scope / Methodology

The worker performs a source-backed architecture and experiment-design pass.
It must distinguish four different facts that must not be collapsed:

1. T1 can decide a topology action hermetically.
2. MAO has a live provider comparison bridge, but its prior easy-task result
   was `VALUE_NOT_PROVEN`.
3. The operational launcher has durable local lifecycle behavior, but source
   existence alone does not prove it is composed with the T1 decision contract
   or the MAO live bridge.
4. Model Gateway can make governed live calls only under a later bounded
   orchestrator grant; this design pass has no such grant.

The worker must produce a design packet plus machine manifest. The design must
either qualify one candidate and define an executable next tranche, or stop
truthfully with a named blocker and exact reopen evidence.

## Proposed Tranche

One INTERNAL_AGENT performs the bounded nine-source audit and authors exactly
the three declared design/evidence outputs. Local remains reviewer and decision
owner. Actual agent execution, provider access, runtime mutation and any later
implementation remain outside this tranche.

## Required Evidence

The return must contain a terminal nine-source ledger, source hashes, candidate
admission evidence, exact policy-to-runtime owner mapping, independent-grader
design, order control, cost and stop rules, and either an exact successor
manifest or a named parked blocker with reopen proof.

## Non-Goals

- no actual agent, subagent, provider, network or live execution;
- no credential or `.env.local` access;
- no source, test, package, runtime, runner, hook or checker mutation;
- no new adapter, CLI, MCP, production route or public export;
- no reopening of the closed easy MAO-LIVE-T1 task;
- no claim that dynamic topology improves quality, cost or latency.

## Required Design Decisions

The returned design must decide all of the following:

| Decision | Required evidence |
|---|---|
| Real execution owner | exact current source symbol or explicit missing-owner disposition |
| Control policy | fixed topology with identical authority, task, provider lane, rubric and budget |
| Treatment policy | dynamic topology action driven by declared runtime evidence without authority expansion |
| Candidate task | materially harder than the closed prime-number task and backed by accepted evidence |
| Independent grading | deterministic or otherwise independent from the worker under test; no self-grading |
| Randomization/order control | predeclared order/seed and no adaptive prompt tuning after seeing results |
| Cost accounting | calls, input/output tokens, wall latency and orchestration overhead; unknown is never zero |
| Stop rules | hard ceilings, safety stop, quality admission and no-repeat conditions |
| Composition gap | exact seam needed between T1 policy, MAO launcher/live bridge and evidence receipt |
| Next manifest | exact implementation/execution paths or a parked blocker with reopen proof |

## Candidate Admission Rule

A task is qualified only when accepted local evidence shows that the direct
single-agent/control lane scores at most 80/100 or contains one predeclared
rubric-defined material defect. The task must name the defect class that an
independent reviewer can detect and one bounded treatment revision can repair.

If no accepted candidate satisfies that rule, the correct result is
`BLOCKED_NO_QUALIFIED_CANDIDATE`. The worker must not manufacture a weak
candidate, reinterpret the prior 100/100 task, or spend a live call to create
baseline evidence.

## Experiment Ceiling For The Future Execution Packet

- one provider lane;
- at most four live calls for the whole accepted run;
- at most one treatment revision;
- zero adaptive prompt tuning after first observation;
- success requires at least a 10-point independently recomputed quality gain
  or correction of the predeclared material defect;
- latency overhead must not exceed 50 percent unless the quality condition is
  met and the operator explicitly accepts the tradeoff;
- no secret, policy, authority-envelope, receipt-completeness or safety
  regression;
- one failed or ambiguous safety/authority check stops execution without retry.

These are design constraints, not current execution authority.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T1 experiment contract, MAO owners and this design packet | read-only source audit plus three worker-owned docs; no calls or runtime mutation | named local sources and worker manifest | later execution adapter must be source-verified separately | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no T2 CLI/MCP owner is authorized | no external ingress, credential, mutation or public claim | no current T2 adapter evidence | explicit separate future adapter owner required if selected | `DEFERRED_WITH_REASON` - this design is internal and does not create external runtime support |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1 is executable proposal-only proof, not real-agent value proof | CLAIM_BOUNDARY | `docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_COMPLETION_2026-09-16.md` | Risk / Corrective Action; Decision / Recommendation / Disposition | T2 design requirement | Local T1 completion | ACCEPT |
| T2 must define tasks, grader, order control, cost and stop rules | VALUE_SET | `docs/reviews/CVF_ACEL_G2_TOPOLOGY_EXPERIMENT_T1_COMPLETION_2026-09-16.md` | Risk / Corrective Action | five required controls | Local T1 completion | ACCEPT |
| prior easy live task proved no added value | RISK_FACT | `docs/reviews/CVF_MAO_LIVE_T1_PROVIDER_ADAPTER_VALUE_PILOT_COMPLETION_2026-07-12.md` | Findings / Position | 100/100 tie; added latency | MAO-LIVE completion | ACCEPT |
| harder-task reopen conditions are already canonical | VALUE_SET | `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md` | Next Allowed Move | five concrete reopen conditions | MAO-LIVE roadmap | ACCEPT |
| T1 has no provider authority | LITERAL_INVARIANT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/runtime.topology.experiment.contract.ts` | AuthorityEnvelope | `AuthorityEnvelope.providerExecutionAuthority` | T1 experiment contract | ACCEPT |
| MAO live bridge has a direct lane and governed lane | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts` | direct lane; MAO lane | `runDirectLane`; `runMaoLane` | MAO live pilot bridge | ACCEPT |
| operational launcher is a separate durable composition owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | launcher class | `MaoOperationalWorkerLauncher` | MAO operational launcher | ACCEPT |
| provider execution requires an orchestrator grant | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | provider grant evaluator | `evaluateProviderExecutionAuthority` | delegation contract | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| dispatch paths | five proposed baseline/work-order/output paths returned `False` before authoring | NO_COLLISION |
| exact G2-T2 token search | `rg -n "ACEL-G2-T2|G2 T2 Real-Agent|G2 real-agent" docs CVF_SESSION` returned no prior artifact | NO_COLLISION |
| prior related owner search | MAO-LIVE and MAO operational owners exist and must be reused or explicitly separated | REUSE_EXISTING_OWNERS |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G2-T2-DESIGN --title "ACEL G2 Real-Agent Topology Experiment Design" --date 2026-09-16 --base 9cf7fd62e988bd760a27a2e585b5c6a543cdbbc5 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic no-commit worker dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | operator authority, dependency gates, exact source corpus, design decisions, candidate admission and claim ceiling |
| checkerReadAheadConfirmation | dispatch, prompt-envelope, convergence, routing, handoff, closeability, trace, provider-authority and Delta checkers |
| docOnlyNewFields | candidateAdmission; policyMapping; graderIndependence; orderControl; costCeiling; stopRules; compositionGap; nextManifest |
| claimBoundary | authoring provenance only; no experiment result or runtime readiness claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033 and ADIF-0044; resolver result was
truncated at 10 of 24 candidates.

Dispatch impact: prohibit exhaustive-corpus overclaim, provider-local
authority, hidden checker discovery, unsupported aggregation, projection drift,
protected-path widening and timeout/ceiling mismatch. No protected path is
worker-owned in this design tranche.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | ready status, first dispatch section, source columns, initial convergence sentinels, routing enums, no-commit return contract, trace labels, gate graph and forbidden provider authority |
| gateRunPurpose | confirm the packet shape before the pre-dispatch bundle |
| claimBoundary | structural conformance does not prove experiment feasibility or candidate qualification |

## Claim Boundary

This baseline authorizes only internal, read-only G2-T2 design and candidate
qualification with three uncommitted documentation outputs. It does not
authorize an actual agent, provider/live call, credential access, runtime or
production mutation, implementation, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private experiment-design authority with no public artifact scope.
