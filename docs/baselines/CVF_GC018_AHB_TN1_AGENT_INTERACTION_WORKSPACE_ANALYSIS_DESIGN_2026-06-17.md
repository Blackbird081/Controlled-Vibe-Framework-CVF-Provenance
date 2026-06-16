# CVF GC-018 - AHB-Tn.1 Agent Interaction Workspace Analysis Design

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-17

Batch ID: AHB-Tn.1

executionBaseHead: 05f3f795

## Purpose

Authorize and close AHB-Tn.1 as bounded analysis/design for the future
agent-interaction workspace, after AHB-T3 closed the machine-enforced handoff
contract local view.

## Scope / Target / Owner Boundary

Target: governance foundation design for future agent-interaction workspace
work.

Owner boundary: Codex-owned single-agent/multi-role analysis, design packet,
commit, and closure. No product runtime mutation, workspace build, provider or
live proof, public-sync, interlock registry edit, historical archive movement,
or production/public readiness claim is authorized.

## Source Authority

| Source | Path | Role |
|---|---|---|
| Active next move | `CVF_SESSION/state/entries/nextAllowedMove.json` | Authorizes operator decision for AHB-Tn analysis/design |
| AHB-T2 ratified contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Central Core for workspace handoff semantics |
| AHB-T3 checker closure | `docs/reviews/CVF_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_COMPLETION_2026-06-17.md` | Machine-enforced predecessor |
| AHB roadmap | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-Tn workspace candidate route |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | Stable folder/index rule |
| Operational reference index | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Cross-CVF routing front door |

## Authorization Decision

Proceed with AHB-Tn.1 after operator authorization on 2026-06-17.

Decision: Codex may create a stable `docs/reference/agent_workspace/` front
door, a workspace design standard, a bounded work order, completion evidence,
and roadmap/index/AGENTS pointers. Codex must not build the workspace or mutate
runtime/product/provider/public surfaces.

## Baseline Decision

AHB-Tn.1 is approved as a bounded governance-foundation analysis/design
tranche.

The baseline is the clean worktree at `05f3f795`, after AHB-T3 material closure
and session sync. The allowed changed set is limited to stable workspace
reference files, AGENTS and operational-index pointers, AHB roadmap update, and
matching GC-018, work order, and completion evidence.

## Authorized Scope

Authorized:

- add stable front door `docs/reference/agent_workspace/README.md`;
- add stable design standard
  `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`;
- update `AGENTS.md` with the mandatory workspace design boundary;
- update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`;
- update AHB roadmap with AHB-Tn.1 closure and future build candidate;
- add this GC-018, the AHB-Tn.1 work order, and completion review.

## Forbidden Scope

- No workspace root, UI, queue, generated state aggregate, or runtime source.
- No product runtime/source mutation under `EXTENSIONS/**`.
- No provider/API/live proof.
- No public-sync or public catalog claim.
- No interlock registry edit.
- No broad archive movement.
- No dedicated new checker implementation in this batch.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add the stable agent-workspace design
front door and pointers so future workspace work has a governed retrieval path
before any build or runtime mutation is proposed.

Protected paths:

- `AGENTS.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/agent_workspace/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`

Operator authorization: operator instructed Codex to proceed with AHB-Tn
analysis/design on 2026-06-17.

Rollback boundary: revert only AHB-Tn.1 workspace design files, pointers,
roadmap update, and matching evidence if this batch is rejected. Do not revert
AHB-T3, AHB-T2-F2, AHB-T2-F1, AHB-T2, AOT-T3, or prior AHB closures.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Stable `docs/reference/agent_workspace/` front door exists. |
| AC2 | Workspace design standard cites AHB-T2, AHB-T3, and foundation storage. |
| AC3 | Future workspace build remains blocked behind fresh GC-018/work order. |
| AC4 | Operational index and AGENTS point agents to the workspace front door. |
| AC5 | AHB roadmap records AHB-Tn.1 closure and keeps build as a future candidate. |
| AC6 | Governance gates pass on `05f3f795..HEAD`. |

## Evidence / Verification

Required evidence:

```powershell
python governance/compat/check_agent_handoff_boundary.py --base 05f3f795 --head HEAD --enforce
python governance/compat/check_foundation_storage_layout.py --base 05f3f795 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 05f3f795 --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 05f3f795 --head HEAD --enforce
python governance/compat/check_machine_closure_package.py --base 05f3f795 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 05f3f795 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 05f3f795 --head HEAD --enforce
git diff --check
```

## Rescan Intelligence Hardening

- Original source artifact: AHB-T2 ratified contract and AHB roadmap.
- Predecessor intake artifact: AHB-T3 completion and active next-move state.
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS.
- Routing matrix status: DO_NOW for workspace design foundation only; build
  remains future candidate.
- Semantic sampling status: focused source and gate review for front door,
  storage layout, and claim boundary.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | AHB-Tn.1 disposition |
|---|---|
| `UNCHANGED_FROM_INTAKE` | AHB-T2 CF-01 through CF-09 remain the Central Core. |
| `CHANGED_DISPOSITION` | AHB-Tn moves from generic candidate to AHB-Tn.1 design closure plus later build candidate. |
| `NEW_FINDING` | no new defect finding; this is a planned foundation tranche. |
| `REMOVED_OR_REJECTED` | workspace build, runtime/provider/public-sync, registry edit remain out of scope. |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
|---|---|---|
| RESOLVED_BY_DESIGN | Workspace retrieval/front-door ambiguity | stable `agent_workspace` folder and standard |
| STRATEGIC_OPERATOR_DECISION | Future workspace build | requires separate authorization after design closure |
| SEPARATE_RUNTIME_TRANCHE | Workspace build or runtime state | requires fresh GC-018 and separate work order |
| MACHINE_CHECK_CANDIDATE | Dedicated workspace design control block | defer until a build or checker tranche is authorized |
| OUT_OF_SCOPE | Runtime/provider/public-sync/live proof | explicitly forbidden |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AHB-TN1-S1 | Active next move | AHB-Tn analysis/design is allowed after AHB-T3 | design-only scope | Could this be read as workspace build authorization? | PASS |
| AHB-TN1-S2 | Foundation storage standard | stable reference folders need README front doors | `agent_workspace` folder | Could future agents miss the folder/index rule again? | PASS |
| AHB-TN1-S3 | AHB-T2 contract | workspace design must preserve handoff contract fields | CF-01 through CF-09 | Could workspace coordination bypass AHB fields? | PASS |
| AHB-TN1-S4 | AHB-T3 checker | changed handoff work orders need contract blocks | AHB-Tn.1 work order | Could this batch skip machine-enforced handoff evidence? | PASS |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this batch changes governed markdown
and reference indexes only. It does not edit CVF product runtime routes,
provider adapters, model registries, hardcoded provider selection, or live
governance behavior. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`
and `PROVIDER_CAPABILITY_REGISTRY` are out-of-scope and untouched.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance design. No public-sync batch is
authorized.

## Claim Boundary

AHB-Tn.1 closes bounded workspace analysis/design foundation only. It does not
build the workspace, alter runtime behavior, run provider/live proof,
public-sync, edit registries, or claim production/public readiness.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.1 agent-interaction workspace analysis/design |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_FOR_CODEX_2026-06-17.md` |
| Allowed scope source | operator authorization for AHB-Tn analysis/design on 2026-06-17 |
| Before status evidence | HEAD `05f3f795`; clean worktree |
| After status evidence | AHB-Tn.1 material closure pending commit |
| Diff evidence | `git diff --name-status 05f3f795..HEAD` |
| Approval boundary | bounded workspace analysis/design foundation only |
| Claim boundary | no workspace build, runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn1-agent-interaction-workspace-analysis-design-2026-06-17` |
| Expected manifest | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_FOR_CODEX_2026-06-17.md` |
| Actual changed set | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_FOR_CODEX_2026-06-17.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
