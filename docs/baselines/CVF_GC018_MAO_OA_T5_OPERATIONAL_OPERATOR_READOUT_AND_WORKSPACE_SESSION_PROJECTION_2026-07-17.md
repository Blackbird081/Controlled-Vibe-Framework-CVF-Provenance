# CVF GC-018 Baseline - MAO-OA-T5 Operational Operator Readout And Workspace Session Projection

Memory class: FULL_RECORD

Date: 2026-07-17

Status: CLOSED_PASS_BOUNDED

GC-018 ID: MAO-OA-T5

Risk class: R2

Commit mode: WORKER_MUST_NOT_COMMIT

Dispatch base: `a61a5c24d`

Governing roadmap:
`docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`

Paired work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T5_OPERATIONAL_OPERATOR_READOUT_AND_WORKSPACE_SESSION_PROJECTION_2026-07-17.md`

## Purpose

Release one bounded execution-plane composition tranche that converts existing
MAO evidence readouts, milestone-only projections, caller-supplied workspace
lane snapshots, guard receipts, current-mode/next-move facts, and an optional
session-sync projection into one deterministic operator readout. The owner
returns a value only and performs no workspace/session/UI/queue/provider action.

## Baseline Decision

`CLOSED_PASS_BOUNDED`.

MAO-OA-T5 is independently accepted after exact-scope recomputation, source
inspection, 22/22 focused tests, TypeScript check, 69 files and 1,760 package
tests, GC-051 alignment, file-size compliance, and reviewer-fast 62/62. No
reviewer source or test repair was required. Fresh T6 packet authoring is next;
T7 remains parked.

## Scope / Target / Owner Boundary

New composition owner:
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.operator.projection.ts`.

The owner may:

- build the existing evidence readout and freshness classification;
- build the existing milestone-only workspace projection;
- summarize caller-supplied workspace items by canonical lane;
- surface blocked/parked and accepted-material items without mutation;
- expose current mode, active handoff, and next allowed move from explicit
  caller inputs;
- reject a guard PASS that lacks a non-empty receipt/evidence path; and
- carry an optional existing session-sync projection as a plan only.

It must not import active session/workspace JSON, generators, filesystem, UI,
queue, provider, network, process, git, or commit-steward owners.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-OA-T4 accepted closure | material commit `ede430587`; `docs/reviews/CVF_MAO_OA_T4_COMPLETION_REVIEW_2026-07-17.md`; final disposition `REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIR` | T4 review/closer composition must be accepted | ACCEPT |
| operator-view authority | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md`, Read Model Sections | read model may expose current mode, lanes, guard evidence, accepted material, and next move without actions | ACCEPT |
| runtime boundary | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | T5 remains READ_MODEL_ONLY | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-OA-T5 --title "MAO Operational Operator Readout And Workspace Session Projection" --date 2026-07-17 --base a61a5c24d --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MAO-OA-T4 accepted closure ede430587" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced blanks with direct source verification, workspace design controls, exact six-path manifest, behavior and negative tests |
| checkerReadAheadConfirmation | dispatch, workspace design/runtime, handoff, trace, worker-return, registry, file-size, and public-export checkers reviewed |
| docOnlyNewFields | T5 proposed composition types are separated below |
| claimBoundary | scaffold provenance only; no implementation or operator-surface proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`, surfaceSelector=`MAO`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-implementation --surface-selector MAO --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | standard no-commit, exact-scope, workspace read-model, and generated-registry controls remain binding |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| deterministic evidence readout exists | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | lines 246-307 | `buildEvidenceReadout` | MAO evidence readout contract | ACCEPT |
| freshness classification exists | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | lines 369-386 | `classifyReadoutFreshness` | MAO evidence readout contract | ACCEPT |
| milestone-only projection exists | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | lines 397-472 | `projectWorkspaceMilestones` | MAO evidence readout contract | ACCEPT |
| session projection is a non-mutating value | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/closer.interlock.contract.ts` | lines 184-205 | `buildSessionSyncProjection` | closer interlock contract | ACCEPT |
| operator view names required sections | DOC_CONTRACT | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | Read Model Sections | `Current Mode`; `Lane Summary`; `Guard Status`; `Next Move` | operator view plan | ACCEPT |
| workspace state is projection, not runtime truth | DOC_CONTRACT | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | Scope / Target / Owner Boundary | `workspace state topology` | workspace topology contract | ACCEPT |
| model-gateway provider registry exists but is excluded | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | lines 1-32 | `ProviderRegistry` | model gateway provider registry | ACCEPT |
| provider capability registry exists but is excluded | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 69 | `PROVIDER_CAPABILITY_REGISTRY` | model gateway capability registry | ACCEPT |

## Current Runtime Freshness Verification

Verified at clean dispatch base `a61a5c24d` on 2026-07-17.

| Check | Evidence | Disposition |
|---|---|---|
| planned new source/test/entry/return | all four paths absent | ACCEPT |
| accepted composition owners | direct symbol search found every cited function | ACCEPT |
| provider surfaces | both current registries above exist but are explicitly outside T5 dependency/import scope | ACCEPT |
| T4 accepted closure | `git show --stat ede430587` contains exact ten-path closure | ACCEPT |
| dispatch base | `git rev-parse --short HEAD`=`a61a5c24d`; worktree clean before packet authoring | ACCEPT |

## New Doc-Only Fields

| Proposed symbol | Intended role | Disposition |
|---|---|---|
| `MaoOperationalOperatorProjection` | bounded local composition owner | DOC_ONLY_NEW |
| `MaoOperationalOperatorProjectionInput` | ledger, terminal IDs, session facts, workspace items, guard evidence, optional session plan | DOC_ONLY_NEW |
| `MaoOperationalOperatorReadout` | deterministic read-only operator result | DOC_ONLY_NEW |
| `MaoOperationalWorkspaceItemSnapshot` | caller DTO using canonical lane vocabulary | DOC_ONLY_NEW |
| `MaoOperationalGuardSnapshot` | checker/status/evidence DTO | DOC_ONLY_NEW |

## Agent Workspace Design Control Block

| Field | Value |
|---|---|
| Workspace purpose | one bounded read-only operator projection for accepted MAO evidence and caller-supplied workspace/session facts |
| Contract source | archive-qualified contract path `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | runtime source returning an in-memory value only; no generated state or durable workspace write |
| Handoff fields | caller-supplied current mode, active handoff, next move, lane and evidence paths remain read-only projections |
| State ownership | active session/workspace registries remain owned by their generators and session-sync steward; T5 owns no state file |
| Guard owner | existing agent workspace design/runtime guards plus focused source tests |
| Build boundary | runtime source is pure composition only; provider proof, public-sync, registry edits beyond GC-051 accountability, UI, queue, and workspace mutation are forbidden |

## Runtime Expansion Control Block

| Field | Value |
|---|---|
| runtimeExpansionMode | READ_MODEL_ONLY |
| queueBoundary | no executable queue, scheduler, inbox, dequeue, lease, or retry behavior |
| operatorViewBoundary | typed read model only; no UI, dashboard, action, or approval control |
| providerBoundary | no provider call or live proof |
| stateBoundary | caller inputs only; no session/workspace generator import or mutation |
| publicBoundary | private provenance only; no public-sync |

## Allowed Scope

Worker may change exactly six paths named by the work order: one new source,
the existing MAO barrel, one focused test, one narrow GC-051 source entry, the
generated aggregate, and one worker return.

## Forbidden Scope

- existing MAO evidence, closer, read-model, workspace, session, or generator owners;
- active session/workspace state sources or generated aggregates;
- filesystem, UI/dashboard, queue/runtime action, CLI/MCP, provider/network/process, git/commit;
- package manifests, dependencies, lockfiles, canonical workspace standards;
- completion review, roadmap/baseline/work-order mutation by worker; and
- T6-T7 implementation, live proof, public-sync, or push.

## Evidence / Verification

- source inspection and negative import test;
- focused deterministic tests, package typecheck, and full package tests;
- GC-051 generator, drift, and changed-path coverage;
- worker-return fast gate, file-size guard, and diff hygiene;
- exact six-path set, nothing staged, and unchanged worker HEAD; and
- N/A with reason for UI, queue, provider/live, git/session action, and public evidence.

## Dual Agent Surface Matrix

| Consumer class | Owner surface | Boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | proposed `MaoOperationalOperatorProjection` | deterministic read-only composition | source and focused tests required | explicit caller DTOs only | `BOUNDED_INTERNAL_RUNTIME_COMPONENT` |
| `EXTERNAL_AGENT_CLI_MCP` | no adapter owner | no ingress, auth, mutation, or public behavior | none authorized | remains parked | `N/A_WITH_REASON` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired T5 work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | T5 completion review | `Status: REVIEWER_ACCEPTED_BOUNDED` | PASS |
| Roadmap state | governing roadmap | T5 accepted; T6 packet authoring next; T7 held | PASS |
| Registry JSON | T5 entry and aggregate | generator check and zero coverage violations | PASS |
| Registry Markdown | T5 completion review | registry disposition and GC-051 evidence recorded | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | none | N/A with reason |
| System loop interlock | N/A with reason: no repository loop or external runtime mutation | none | N/A with reason |
| Session continuity | protected sync follows material closure | separate steward-owned commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Required evidence | Dispatch state |
|---|---|---|
| operator projection behavior | 22/22 focused tests and 1,760-test package regression | PASS |
| UI/provider/action acceptance | N/A with reason: forbidden | N/A_WITH_REASON |
| reviewer acceptance | independent completion review | PASS |
| public acceptance | N/A with reason: no public action | N/A_WITH_REASON |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/check_agent_workspace_runtime_boundary.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; Source Verification Block; Agent Workspace Design Control Block; Runtime Expansion Control Block; Machine Closure Package; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm source-backed T5 packet shape before dispatch |
| claimBoundary | checker conformance does not prove implementation, operator usability, runtime action, or user value |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch. No public artifact or
public-sync action is authorized.

## Claim Boundary

This baseline releases one bounded typed operator projection composition. It
does not authorize or prove workspace/session mutation, UI/dashboard behavior,
queue execution, actual agents, provider/live work, public readiness,
production readiness, shipment, or user value.
