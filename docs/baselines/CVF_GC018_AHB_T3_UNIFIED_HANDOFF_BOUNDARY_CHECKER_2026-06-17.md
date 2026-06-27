# CVF GC-018 - AHB-T3 Unified Handoff Boundary Checker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-17

Batch ID: AHB-T3

executionBaseHead: 230565e4

## Purpose

Authorize and close AHB-T3 as bounded machine enforcement for the ratified
Agent Handoff Contract.

## Scope / Target / Owner Boundary

Target: governance-control machine check for agent handoff-boundary contract
evidence.

Owner boundary: Codex-owned single-agent/multi-role implementation, review,
commit, and closure. No product runtime mutation, provider/live proof,
public-sync, interlock registry edit, historical archive movement, or
agent-interaction workspace build is authorized.

## Source Authority

| Source | Path | Role |
|---|---|---|
| AHB-T2 ratified contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Central Core for CF-01 through CF-09 |
| AHB roadmap | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-T3 candidate after T2/F2 |
| AHB-T2-F2 completion | `docs/reviews/CVF_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_COMPLETION_2026-06-16.md` | Predecessor enforcement closure before AHB-T3 |
| AOT checker | `governance/compat/check_agent_operation_trace.py` | Trace/manifest local view that AHB must not duplicate or weaken |
| Autorun gate | `governance/compat/run_agent_autorun_workflow_gate.py` | Mandatory phase-gate host |
| Local hook chain | `governance/compat/run_local_governance_hook_chain.py` | Local hook host |

## Authorization Decision

Proceed with AHB-T3 now that operator explicitly authorized it on 2026-06-17.

Decision: Codex may implement a unified handoff-boundary machine check derived
from the AHB-T2 contract, with focused tests, stable `docs/reference/agent_handoff/`
front door, autorun/local-hook bindings, roadmap closure, completion evidence,
and session continuity after material commit.

## Baseline Decision

AHB-T3 is approved as a bounded governance-control checker tranche.

The baseline is the clean worktree at `230565e4`, after AHB-T2-F2 material
closure and session-sync. The allowed changed set is limited to the checker,
focused tests, stable handoff reference folder, autorun/local-hook bindings,
AGENTS/operational-index pointers, AHB roadmap closure, and matching GC-018,
work order, and completion evidence.

## Authorized Scope

Authorized:

- add `governance/compat/check_agent_handoff_boundary.py`;
- add `governance/compat/test_check_agent_handoff_boundary.py`;
- add stable reference front door
  `docs/reference/agent_handoff/README.md`;
- add stable machine-check standard
  `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`;
- bind the checker into autorun and local hook chains;
- update `AGENTS.md` and the operational reference index with the mandatory
  handoff-boundary guard;
- update the AHB roadmap, this GC-018, work order, and completion review.

## Forbidden Scope

- No product runtime/source mutation under `EXTENSIONS/**`.
- No provider/API/live proof.
- No public-sync or public catalog claim.
- No interlock registry edit.
- No agent-interaction workspace build.
- No broad archive movement.
- No weakening of AOT-T3 dispatch-manifest scope enforcement.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add and bind a bounded agent handoff
boundary checker, with tests and stable reference index, so future governed
handoff work orders must cite and instantiate the ratified AHB contract.

Protected paths:

- `AGENTS.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/agent_handoff/README.md`
- `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`
- `governance/compat/check_agent_handoff_boundary.py`
- `governance/compat/test_check_agent_handoff_boundary.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Operator authorization: operator instructed Codex to proceed with AHB-T3 on
2026-06-17.

Rollback boundary: revert only AHB-T3 checker, tests, hook bindings, stable
handoff reference folder, and matching docs if this batch is rejected. Do not
revert AHB-T2-F2, AHB-T2-F1, AHB-T2, AOT-T3, or prior AHB closures.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Stable `docs/reference/agent_handoff/` front door exists. |
| AC2 | Machine-check standard names the ratified contract and checker. |
| AC3 | Checker catches changed handoff work orders missing the Agent Handoff Contract Control Block. |
| AC4 | Checker catches missing `Reviewer Closure Conversion` for `WORKER_MUST_NOT_COMMIT`. |
| AC5 | Checker catches missing C3 closer designation. |
| AC6 | Checker catches dispatch-ready handoff work orders without clean-worktree evidence. |
| AC7 | Checker is bound into autorun and local hook chains. |
| AC8 | Focused tests and governance gates pass. |

## Evidence / Verification

Required evidence:

```powershell
pytest governance/compat/test_check_agent_handoff_boundary.py -q
python governance/compat/check_agent_handoff_boundary.py --base 230565e4 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 230565e4 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 230565e4 --head HEAD --enforce
git diff --check
```

## Rescan Intelligence Hardening

- Original source artifact: AHB-T2 ratified contract.
- Predecessor intake artifact: AHB roadmap, AHB-T2 completion, AHB-T2-F2
  enforcement completion, and AOT-T3 completion.
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS.
- Routing matrix status: DO_NOW for AHB-T3 machine check only; workspace
  remains AHB-Tn.
- Semantic sampling status: focused checker tests for missing block, C4
  reviewer conversion, C3 closer, clean-worktree dispatch evidence, and
  non-handoff ignore.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | AHB-T3 disposition |
|---|---|
| `UNCHANGED_FROM_INTAKE` | CF-01 through CF-09 remain the ratified contract fields. |
| `CHANGED_DISPOSITION` | AHB-T3 moves from candidate to closed machine enforcement. |
| `NEW_FINDING` | none. |
| `REMOVED_OR_REJECTED` | workspace build, runtime/provider/public-sync, registry edit remain out of scope. |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
|---|---|---|
| RESOLVED_BY_DESIGN | AHB-T3 work-order handoff contract enforcement | checker, tests, stable standard, hook bindings |
| STRATEGIC_OPERATOR_DECISION | AHB-Tn agent-interaction workspace | later operator decision after AHB-T3 closure |
| SEPARATE_RUNTIME_TRANCHE | Agent-interaction workspace | AHB-Tn only |
| OUT_OF_SCOPE | Runtime/provider/public-sync/live proof | explicitly forbidden |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AHB-T3-S1 | Required Work Order Block | handoff work orders need a contract control block | missing block regression | Could a future work order cite base heads but skip the AHB contract? | PASS |
| AHB-T3-S2 | Commit Mode Rules | C4 requires reviewer closure conversion | `WORKER_MUST_NOT_COMMIT` regression | Could a no-commit worker return lack reviewer-owned closure paths? | PASS |
| AHB-T3-S3 | C3 Rule | N-plus-agent chains require closer designation | C3 closer regression | Could three actors leave commit ownership ambiguous? | PASS |
| AHB-T3-S4 | Cross-Batch Isolation Rule | dispatch-ready packets need clean-worktree evidence | cross-batch isolation regression | Could a second batch start with polluted worktree evidence? | PASS |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this batch changes governance checkers,
tests, and governed markdown only. It does not edit CVF product runtime routes,
provider adapters, model registries, hardcoded provider selection, or live
governance behavior. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`
and `PROVIDER_CAPABILITY_REGISTRY` are out-of-scope and untouched.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. No public-sync batch is
authorized.

## Claim Boundary

AHB-T3 closes bounded machine enforcement for handoff-boundary contract
evidence. It does not prove runtime governance behavior, provider behavior,
workspace isolation, public readiness, production readiness, or public export.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-T3 unified handoff-boundary checker |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_handoff/README.md`; `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `docs/reviews/CVF_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Allowed scope source | operator authorization for AHB-T3 on 2026-06-17 |
| Before status evidence | HEAD `230565e4`; worktree clean |
| After status evidence | AHB-T3 material closure pending commit |
| Diff evidence | `git diff --name-status 230565e4..HEAD` |
| Approval boundary | bounded governance-control checker and stable reference front door |
| Claim boundary | no runtime/provider/live/public/workspace implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-t3-unified-handoff-boundary-checker-2026-06-17` |
| Expected manifest | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_handoff/README.md`; `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `docs/reviews/CVF_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Actual changed set | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_handoff/README.md`; `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `docs/reviews/CVF_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
