# CVF GC-018 Baseline - MAO-T0 Source Inventory, Architecture Decisions, And Schemas

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-11

Batch ID: MAO-T0-DISPATCH

dispatchBaseHead: `636f9639f`

executionBaseHead: `TO_BE_CAPTURED_BY_WORKER_AT_START`

closureBaseHead: `TO_BE_CAPTURED_BY_REVIEWER_AT_CLOSURE`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Authorize the delegated worker to complete MAO-T0 documentation and schema foundation only:
source inventory, overlap analysis, architecture decisions, task/event/receipt
schemas, lifecycle tables, and threat/failure model. No runtime implementation
is authorized.

## Scope / Target / Owner Boundary

Worker owns exactly the four T0 reference/schema deliverables and one worker
return named in the paired work order. Codex is independent reviewer and closer.
Existing AHB, workspace, work-order, approval, provider-routing, commit-steward,
session-sync, ASC, and R91 owners remain authoritative.

## Decision / Baseline / Proposed Tranche

Release MAO-T0 as a docs/schema contract tranche. It must decide new schema
fields explicitly, reconcile all historical overlap, and stop before executable
orchestration, provider adapters, queue/scheduler work, catalog admission, or
MAO-T1.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO roadmap | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md`; commit `6a08a041e` | roadmap must be PROPOSED and critique-gated | SATISFIED |
| External critique and internal reconciliation | `docs/reviews/CVF_MAO_ROADMAP_EXTERNAL_CRITIQUE_INTERNAL_RECONCILIATION_2026-07-11.md`; commit `d61c3c92c` | internal reconciliation must accept T0 with caveats | SATISFIED |
| Reopen conditions | R94 `CLOSED_PASS_BOUNDED`; R95 `REVIEWER_ACCEPTED_BOUNDED` in generated session state | both terminal | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T0 --title "MAO Source Inventory Architecture Decisions And Schemas" --date 2026-07-11 --base a2907dbed --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SATISFIED: MAO roadmap commit 6a08a041e and internal reconciliation artifact accepted before dispatch" --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all placeholders with source-backed MAO-T0 authority, scope, evidence, and controls |
| checkerReadAheadConfirmation | dispatch-quality, ADIF disclosure, AHB, workspace-design, runtime-boundary, scaffold-provenance, and public-disposition checkers read |
| docOnlyNewFields | new MAO schema fields belong in the T0 New Doc-Only Fields table, not this baseline Source Verification table |
| claimBoundary | dispatch authorship only; no runtime/provider/public behavior claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| AHB canonical route and closer semantics | LITERAL_INVARIANT | canonical contract, not archive: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | CF-01, CF-07, C3 | `route`, `commitOwner(CLOSURE)` | Agent Handoff Contract | ACCEPT |
| Workspace generated state is projection, not runtime queue | LITERAL_INVARIANT | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | Topology Decision and Storage Topology | `ACTIVE_AGENT_WORKSPACE_STATE.json` | workspace topology | ACCEPT |
| Workspace runtime expansion needs fresh authority | LITERAL_INVARIANT | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | runtime expansion boundary | `RUNTIME_IMPLEMENTATION_REQUESTED` | workspace runtime boundary | ACCEPT |
| Historical coordination contract exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/execution.multi.agent.coordination.contract.ts` | class definition | `MultiAgentCoordinationContract` | execution-plane contract | ACCEPT |
| Historical cloud runtime exists but has no non-test caller | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/cloud/multi.agent.runtime.ts` | class and admission methods plus repo search | `MultiAgentRuntime` | phase-governance runtime | ACCEPT |
| MA1 transfer standard is archive-qualified | EXISTS | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | sections 0-10 | archived packet section set | archived MA1 template | ACCEPT |

## Current Runtime Freshness Verification

Verified at `636f9639f`: source paths and symbols above exist; repo search confirms
no non-test `MultiAgentRuntime` caller; R91 and ASC freshness remain CURRENT.
No new MAO runtime/schema source is claimed to exist.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-contract`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class architecture-contract --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs/reference --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: none returned |
| Dispatch impact | T0 must still carry the reconciliation caveat that no MAO-specific ADIF calibration baseline exists |

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/check_agent_workspace_runtime_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Agent Workspace Design Control Block`; `Source Verification Block` |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | packet structure only; no execution or runtime proof |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

The delegated worker performs execution. The independent reviewer is designated closer and commit
owner. The worker must not use subagents because T0 requires one bounded worker
context and one independent reviewer context.

## Evidence / Verification

Pre-dispatch requires source searches, JSON validation, `git diff --check`,
dispatch-quality, AHB, workspace-design, and autorun gates on the real range.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired work order | DISPATCH_READY | N/A with reason: dispatch packet, not closure |
| Completion or reviewer artifact | critique reconciliation | REVIEWER_ACCEPTED_BOUNDED | PASS |
| Roadmap state | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` | PROPOSED | PASS |
| Registry JSON | N/A with reason: no registry edit | no change | N/A with reason |
| Registry Markdown | N/A with reason: no registry edit | no change | N/A with reason |
| External evidence digest | critique reconciliation | sha256 `E7392BC13A7F56E8647E94D091B5F76BB8EA3D67ACCF4245EE0E150A5354726D` | PASS |
| System loop interlock | R91/ASC freshness | CURRENT | PASS |
| Session continuity | active front doors | dispatch authoring current | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | Evidence field | Required value | Observed value | Status |
|---|---|---|---|---|---|
| MAO-T0-Q1 | reconciliation | verdict | accepted with T0 caveats | accepted with T0 caveats | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance contract/schema dispatch; no public artifact exists.

## Claim Boundary

This baseline authorizes MAO-T0 documentation and schemas only. It does not
authorize runtime, provider calls, agent spawning, queue/scheduler, UI, package,
public-sync, session-state, ASC/R91 semantic, L4, R84, or R73F changes.
