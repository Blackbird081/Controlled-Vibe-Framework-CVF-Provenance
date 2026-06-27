# CVF GC-018 - AHB-Tn.3 Agent Workspace State Topology Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-17

Batch ID: AHB-Tn.3

executionBaseHead: 3b340823

## Purpose

Authorize and close AHB-Tn.3 as bounded workspace state topology contract work
after AHB-Tn.2 machine-enforced the workspace design control block.

## Scope / Target / Owner Boundary

Target: governance-foundation state topology for future agent-interaction
workspace work.

Owner boundary: Codex-owned single-agent/multi-role contract authoring,
reference updates, commit, closure, and session sync. No workspace build,
generated state aggregate, runtime/source mutation, provider/live proof,
public-sync, interlock registry edit, broad archive movement, or
production/public readiness claim is authorized.

## Source Authority

| Source | Path | Role |
|---|---|---|
| Operator instruction | chat instruction on 2026-06-17 | Authorizes AHB-Tn.3 topology contract work |
| AHB-Tn.2 workspace checker closure | `docs/reviews/CVF_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_COMPLETION_2026-06-17.md` | Machine-enforced predecessor |
| Agent workspace front door | `docs/reference/agent_workspace/README.md` | Stable retrieval path |
| Workspace design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Pre-build boundary |
| Workspace design checker | `governance/compat/check_agent_workspace_design.py` | Machine-enforced work-order local view |
| Agent Handoff Contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Central Core for handoff semantics |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | Stable folder/index rule |

## Authorization Decision

Proceed with AHB-Tn.3 after operator authorization on 2026-06-17.

Decision: Codex may add a stable workspace state topology contract, update
workspace front doors and routing pointers, update the AHB roadmap, and close
with GC-018, work order, completion evidence, material commit, and separate
session sync. Codex must not build the workspace or create generated workspace
state in this batch.

## Baseline Decision

AHB-Tn.3 is approved as a bounded governance-foundation contract tranche.

The baseline is the clean worktree at `3b340823`, after AHB-Tn.2 closure and
session sync. The allowed changed set is limited to stable workspace reference
files, AGENTS and operational-index pointers, AHB roadmap update, and matching
GC-018, work order, and completion evidence.

## Authorized Scope

Authorized:

- add `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`;
- update `docs/reference/agent_workspace/README.md`;
- update
  `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`;
- update `AGENTS.md`;
- update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`;
- update AHB roadmap with AHB-Tn.3 closure and future candidate;
- add this GC-018, the AHB-Tn.3 work order, and completion review.

## Forbidden Scope

- No workspace root, UI, queue, inbox, generated state aggregate, or runtime
  source.
- No product runtime/source mutation.
- No provider/API/live proof.
- No public-sync or public catalog claim.
- No interlock registry edit.
- No registry edit or GC-051 entry.
- No checker implementation in this batch.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update governed front doors and reference
pointers so future workspace state work routes through a stable topology
contract before implementation.

Protected paths:

- `AGENTS.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/agent_workspace/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`
- `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`

Operator authorization: operator instructed Codex to proceed with AHB-Tn.3
workspace state topology contract on 2026-06-17.

Rollback boundary: revert only AHB-Tn.3 topology contract, pointers, roadmap
update, and matching evidence if this batch is rejected. Do not revert AHB-Tn.2
or prior AHB closures.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Stable workspace state topology contract exists under `docs/reference/agent_workspace/`. |
| AC2 | Contract defines state units, required fields, lanes, storage topology, generated-state candidate layout, and archive policy. |
| AC3 | README, design standard, AGENTS, operational index, and AHB roadmap point to the contract. |
| AC4 | Work order includes Agent Workspace Design Control Block and Agent Handoff Contract Control Block. |
| AC5 | Workspace build, generated state creation, runtime/provider/public/registry work remain forbidden. |
| AC6 | Governance gates pass on `3b340823..HEAD`. |

## Evidence / Verification

Required evidence:

```powershell
python governance/compat/check_agent_workspace_design.py --base 3b340823 --head HEAD --enforce
python governance/compat/check_agent_handoff_boundary.py --base 3b340823 --head HEAD --enforce
python governance/compat/check_foundation_storage_layout.py --base 3b340823 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 3b340823 --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 3b340823 --head HEAD --enforce
python governance/compat/check_machine_closure_package.py --base 3b340823 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 3b340823 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 3b340823 --head HEAD --enforce
git diff --check
```

## Rescan Intelligence Hardening

- Original source artifact: AHB-Tn.2 workspace design checker completion and
  workspace design standard.
- Predecessor intake artifact: AHB-Tn.2 session-sync next-move state.
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS.
- Routing matrix status: DO_NOW for workspace state topology contract only;
  build and generated state remain future candidates.
- Semantic sampling status: focused source and gate review for state topology,
  storage layout, and claim boundary.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | AHB-Tn.3 disposition |
|---|---|
| `UNCHANGED_FROM_INTAKE` | AHB-T2 CF-01 through CF-09 remain the Central Core. |
| `CHANGED_DISPOSITION` | AHB-Tn.3 changes from generic future build/state candidate to closed topology-contract tranche. |
| `NEW_FINDING` | no new defect finding; this is planned control-plane hardening. |
| `REMOVED_OR_REJECTED` | workspace build, generated state creation, runtime/provider/public-sync, and registry edit remain out of scope. |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
|---|---|---|
| DO_NOW | Workspace state topology contract | operator authorized bounded foundation hardening |
| RESOLVED_BY_DESIGN | Ambiguous workspace state vocabulary | contract defines state units, lanes, and required fields |
| STRATEGIC_OPERATOR_DECISION | Future workspace build or generated-state work | requires separate authorization after topology contract closure |
| SEPARATE_RUNTIME_TRANCHE | Workspace runtime, queue, inbox, dashboard, generated aggregate, or checker | requires fresh GC-018 and separate work order |
| OUT_OF_SCOPE | Provider proof, public-sync, registry edit | explicitly forbidden |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AHB-TN3-S1 | AHB-Tn.2 completion | workspace work orders need machine-enforced design control | Tn.3 work order block | Could Tn.3 bypass the checker it relies on? | PASS |
| AHB-TN3-S2 | Workspace design standard | workspace state must decide generated JSON/runtime/deferred posture | topology contract | Could future agents invent state fields later? | PASS |
| AHB-TN3-S3 | JSON aggregate discipline | generated aggregate requires source layout and drift check | candidate only | Could this batch create generated state accidentally? | PASS |
| AHB-TN3-S4 | Foundation storage standard | stable reference folders need README front doors | existing `agent_workspace` folder | Could topology scatter into dated evidence only? | PASS |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this batch changes governed markdown and
reference routing only. It does not edit CVF product runtime routes, provider
adapters, model registries, hardcoded provider selection, or live governance
behavior. Model Gateway `provider-registry.ts` and
`PROVIDER_CAPABILITY_REGISTRY` are out-of-scope and untouched.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation. No public-sync batch is
authorized.

## Claim Boundary

AHB-Tn.3 closes bounded workspace state topology contract work only. It does
not build the workspace, create generated workspace state, alter runtime
behavior, run provider/live proof, public-sync, edit registries, or claim
production/public readiness.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.3 workspace state topology contract |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_FOR_CODEX_2026-06-17.md` |
| Allowed scope source | operator authorization for AHB-Tn.3 workspace state topology contract on 2026-06-17 |
| Before status evidence | HEAD `3b340823`; clean worktree |
| After status evidence | AHB-Tn.3 material closure pending commit |
| Diff evidence | `git diff --name-status 3b340823..HEAD` |
| Approval boundary | bounded workspace state topology contract only |
| Claim boundary | no workspace build, generated state/runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn3-agent-workspace-state-topology-contract-2026-06-17` |
| Expected manifest | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_FOR_CODEX_2026-06-17.md` |
| Actual changed set | AHB-Tn.3 material changed set, verified in completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
