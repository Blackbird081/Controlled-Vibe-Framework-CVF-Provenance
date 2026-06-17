# CVF GC-018 - AHB-Tn.2 Agent Workspace Design Checker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-17

Batch ID: AHB-Tn.2

executionBaseHead: 5c79881e

## Purpose

Authorize and close AHB-Tn.2 as bounded machine hardening for the future
agent-interaction workspace design boundary after AHB-Tn.1 created the stable
workspace reference foundation.

## Scope / Target / Owner Boundary

Target: governance-control enforcement for the Agent Workspace Design Control
Block.

Owner boundary: Codex-owned single-agent/multi-role checker implementation,
tests, documentation update, commit, closure, and session sync. No workspace
build, product runtime mutation, provider/live proof, public-sync, interlock
registry edit, historical archive movement, or production/public readiness
claim is authorized.

## Source Authority

| Source | Path | Role |
|---|---|---|
| Operator instruction | chat instruction on 2026-06-17 | Authorizes continuing AHB-Tn.2 workspace foundation hardening |
| AHB-Tn.1 workspace front door | `docs/reference/agent_workspace/README.md` | Stable workspace retrieval path |
| AHB-Tn.1 design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Defines Agent Workspace Design Control Block |
| AHB-T2 ratified contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Central Core for handoff semantics |
| AHB-T3 checker | `governance/compat/check_agent_handoff_boundary.py` | Machine-enforced handoff local view |
| Foundation storage checker | `governance/compat/check_foundation_storage_layout.py` | Stable folder/index guard |
| AHB roadmap | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | Tranche route and workspace candidate state |

## Authorization Decision

Proceed with AHB-Tn.2 after operator authorization on 2026-06-17.

Decision: Codex may add a dedicated workspace design checker, focused tests,
autorun/local-hook bindings, stable reference updates, AGENTS/index pointers,
roadmap closure, work order, and completion evidence. Codex must not build the
workspace or mutate runtime/product/provider/public surfaces.

## Baseline Decision

AHB-Tn.2 is approved as a bounded governance-control machine-hardening tranche.

The baseline is the clean worktree at `5c79881e`, after AHB-Tn.1 closure and
session sync. The allowed changed set is limited to the checker, tests,
autorun/local-hook binding, stable workspace reference updates, AGENTS and
operational-index pointers, AHB roadmap update, and matching GC-018, work order,
and completion evidence.

## Authorized Scope

Authorized:

- add `governance/compat/check_agent_workspace_design.py`;
- add `governance/compat/test_check_agent_workspace_design.py`;
- bind the checker into `governance/compat/run_agent_autorun_workflow_gate.py`;
- bind the checker into `governance/compat/run_local_governance_hook_chain.py`;
- update `docs/reference/agent_workspace/README.md`;
- update
  `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`;
- update `AGENTS.md`;
- update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`;
- update AHB roadmap with AHB-Tn.2 closure and next candidate;
- add this GC-018, the AHB-Tn.2 work order, and completion review.

## Forbidden Scope

- No workspace root, UI, queue, inbox, generated state aggregate, or runtime
  source.
- No product runtime/source mutation under `EXTENSIONS/**`.
- No provider/API/live proof.
- No public-sync or public catalog claim.
- No interlock registry edit.
- No broad archive movement.
- No registry edit or GC-051 entry.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add and bind the workspace design checker so
future workspace work orders must carry a governed pre-build control block.

Protected paths:

- `AGENTS.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/agent_workspace/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`
- `governance/compat/check_agent_workspace_design.py`
- `governance/compat/test_check_agent_workspace_design.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Operator authorization: operator instructed Codex to continue with AHB-Tn.2
workspace foundation hardening on 2026-06-17.

Rollback boundary: revert only AHB-Tn.2 checker, tests, bindings, reference
updates, roadmap update, and matching evidence if this batch is rejected. Do
not revert AHB-Tn.1, AHB-T3, AHB-T2-F2, AHB-T2-F1, AHB-T2, AOT-T3, or prior
AHB closures.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Workspace checker exists and enforces the Agent Workspace Design Control Block for changed workspace work orders. |
| AC2 | Focused tests cover missing block, valid block, missing field, incomplete build boundary, ignored non-workspace work order, standard markers, and hook binding. |
| AC3 | Workspace standard status is machine-enforced and names the checker. |
| AC4 | AGENTS and the operational index route future agents to the checker and front door. |
| AC5 | Autorun and local hook chains run the checker. |
| AC6 | AHB roadmap records AHB-Tn.2 closure and keeps any build as a future operator decision. |
| AC7 | Governance gates pass on `5c79881e..HEAD`. |

## Evidence / Verification

Required evidence:

```powershell
pytest governance/compat/test_check_agent_workspace_design.py -q
python governance/compat/check_agent_workspace_design.py --base 5c79881e --head HEAD --enforce
python governance/compat/check_agent_handoff_boundary.py --base 5c79881e --head HEAD --enforce
python governance/compat/check_foundation_storage_layout.py --base 5c79881e --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 5c79881e --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 5c79881e --head HEAD --enforce
python governance/compat/check_machine_closure_package.py --base 5c79881e --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 5c79881e --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 5c79881e --head HEAD --enforce
git diff --check
```

## Rescan Intelligence Hardening

- Original source artifact: AHB-Tn.1 workspace front door and design standard.
- Predecessor intake artifact: AHB-Tn.1 completion and active next-move state.
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS.
- Routing matrix status: DO_NOW for workspace design checker only; build
  remains future candidate.
- Semantic sampling status: focused source and gate review for workspace
  control block, hook binding, and claim boundary.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | AHB-Tn.2 disposition |
|---|---|
| `UNCHANGED_FROM_INTAKE` | AHB-T2 CF-01 through CF-09 remain the Central Core. |
| `CHANGED_DISPOSITION` | AHB-Tn.2 changes from generic build-or-hardening candidate to closed machine-hardening tranche. |
| `NEW_FINDING` | no new defect finding; this is planned control-plane hardening from AHB-Tn.1. |
| `REMOVED_OR_REJECTED` | workspace build, runtime/provider/public-sync, registry edit remain out of scope. |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
|---|---|---|
| DO_NOW | Workspace design checker | operator authorized bounded foundation hardening |
| RESOLVED_BY_DESIGN | Artifact-only workspace control block gap | checker enforces block presence and required fields |
| STRATEGIC_OPERATOR_DECISION | Future workspace build | requires separate authorization after machine-hardening closure |
| SEPARATE_RUNTIME_TRANCHE | Workspace build, generated state, queue, inbox, or runtime source | requires fresh GC-018 and separate work order |
| OUT_OF_SCOPE | Provider proof, public-sync, registry edit | explicitly forbidden |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AHB-TN2-S1 | AHB-Tn.1 design standard | workspace work orders need Agent Workspace Design Control Block | checker required block | Could agents still skip the block? | PASS |
| AHB-TN2-S2 | Agent workspace front door | future agents must read stable folder before workspace work | README and AGENTS pointer | Could agents rely on chat or provider memory only? | PASS |
| AHB-TN2-S3 | AHB-T2 contract | workspace coordination must preserve handoff fields | required contract source | Could workspace bypass AHB central core? | PASS |
| AHB-TN2-S4 | Foundation storage standard | stable reference families need indexed paths | stable workspace folder | Could the checker scatter into dated docs only? | PASS |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this batch changes governance checkers,
tests, and governed markdown only. It does not edit CVF product runtime routes,
provider adapters, model registries, hardcoded provider selection, or live
governance behavior. Model Gateway `provider-registry.ts` and
`PROVIDER_CAPABILITY_REGISTRY` are out-of-scope and untouched.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance enforcement. No public-sync batch is
authorized.

## Claim Boundary

AHB-Tn.2 closes bounded workspace design machine enforcement only. It does not
build the workspace, alter runtime behavior, run provider/live proof,
public-sync, edit registries, or claim production/public readiness.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.2 agent workspace design checker |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/test_check_agent_workspace_design.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Allowed scope source | operator authorization for AHB-Tn.2 workspace-foundation hardening on 2026-06-17 |
| Before status evidence | HEAD `5c79881e`; clean worktree |
| After status evidence | AHB-Tn.2 material closure pending commit |
| Diff evidence | `git diff --name-status 5c79881e..HEAD` |
| Approval boundary | bounded workspace design checker and foundation hardening only |
| Claim boundary | no workspace build, runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn2-agent-workspace-design-checker-2026-06-17` |
| Expected manifest | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/test_check_agent_workspace_design.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Actual changed set | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/test_check_agent_workspace_design.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
