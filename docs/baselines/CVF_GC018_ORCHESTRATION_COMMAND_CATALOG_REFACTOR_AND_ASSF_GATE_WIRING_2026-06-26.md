# CVF GC-018 Baseline: Orchestration Command Catalog Refactor And ASSF Gate Wiring

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: baseline

Batch ID: ORCHESTRATION-CATALOG-ASSF-WIRING

dispatchBaseHead: 3384a941

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | refactor near-limit orchestration command catalogs and wire ASSF admission gate |
| Baseline | the two orchestration runner files were at approved exception limits before this maintenance |
| Proposed tranche | ORCHESTRATION-CATALOG-ASSF-WIRING T0-T4 |
| Worker route | Codex single-agent multi-role execution |
| Closure posture | `CLOSED_PASS_BOUNDED` |

## Purpose

Authorize bounded governance maintenance so valid gate wiring does not stay
outside the standard bundles solely because the orchestration files were at
their line-count exception limits.

## Scope / Methodology

The tranche extracts command catalog data from the local hook-chain runner and
the agent autorun workflow runner into same-domain helper modules, then adds the
ASSF certified metadata admission checker to those catalogs.

## Findings / Position

Avoiding gate wiring because orchestration files are near the exception limit
creates a maintenance debt. The better bounded action is to reduce the
orchestration files and wire the gate through a smaller catalog surface.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| extracted catalog import could fail in direct script mode | direct import and package import fallbacks are retained |
| extracted catalog could hide gate drift | catalogs stay under `governance/compat` and are covered by compile and bundled gates |
| protected path edits need authorization | completion review carries Core Guard Self-Protection Authorization |
| new gate wiring could imply wider ASSF scope | forbidden scope excludes package, Web, resolver, registry, provider, public, and session work |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-orchestration-refactor`, role=`codex-multi-role`, lifecyclePhase=`material-implementation`

Returned defects: NONE_RETURNED

- none

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| local runner imports extracted catalog | `governance/compat/run_local_governance_hook_chain.py` | lines 125-131 | `HOOK_CHAINS` | local hook runner | EXISTS | ACCEPT |
| local catalog aggregator defines hook chains | `governance/compat/local_governance_hook_catalog.py` | lines 19-23 | `HOOK_CHAINS` | local hook catalog aggregator | EXISTS | ACCEPT |
| reviewer-fast local chain includes ASSF gate | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | line 120 | `ASSF certified metadata admission` | reviewer-fast hook catalog | EXISTS | ACCEPT |
| pre-commit local chain includes ASSF gate | `governance/compat/local_governance_hook_catalog_pre_commit.py` | line 175 | `ASSF certified metadata admission` | pre-commit hook catalog | EXISTS | ACCEPT |
| pre-push local chain includes ASSF gate | `governance/compat/local_governance_hook_catalog_pre_push.py` | line 136 | `ASSF certified metadata admission` | pre-push hook catalog | EXISTS | ACCEPT |
| autorun runner imports extracted catalog | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 36-54 | `_common_commands` | autorun workflow runner | EXISTS | ACCEPT |
| autorun catalog owns common command builder | `governance/compat/agent_autorun_command_catalog.py` | line 51 | `_common_commands` | autorun command catalog | EXISTS | ACCEPT |
| autorun catalog includes ASSF gate | `governance/compat/agent_autorun_command_catalog.py` | lines 255-257 | `ASSF certified metadata admission` | autorun command catalog | EXISTS | ACCEPT |

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `governance/compat/run_local_governance_hook_chain.py` | Codex | refactor to consume catalog helper |
| `governance/compat/local_governance_hook_catalog.py` | Codex | create local hook catalog aggregator |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | Codex | create reviewer-fast local hook catalog |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | Codex | create pre-commit local hook catalog |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | Codex | create pre-push local hook catalog |
| `governance/compat/run_agent_autorun_workflow_gate.py` | Codex | refactor to consume catalog helper |
| `governance/compat/agent_autorun_command_catalog.py` | Codex | create autorun command catalog |
| `docs/roadmaps/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_ROADMAP_2026-06-26.md` | Codex | create and close |
| `docs/baselines/CVF_GC018_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_2026-06-26.md` | Codex | create and close |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_FOR_CODEX_2026-06-26.md` | Codex | create and close |
| `docs/reviews/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_COMPLETION_2026-06-26.md` | Codex | create completion review |

## Forbidden Scope

No package instance creation, certification decision, generated-index mutation,
resolver source mutation, Web runtime change, CLI/MCP adapter, provider/live
proof, public-sync, push, or session-sync is authorized in the material commit.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `python -m py_compile governance/compat/run_local_governance_hook_chain.py governance/compat/local_governance_hook_catalog.py governance/compat/local_governance_hook_catalog_reviewer_fast.py governance/compat/local_governance_hook_catalog_pre_commit.py governance/compat/local_governance_hook_catalog_pre_push.py governance/compat/run_agent_autorun_workflow_gate.py governance/compat/agent_autorun_command_catalog.py` | PASS |
| `python governance/compat/check_python_automation_size.py --enforce` | PASS |
| `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | PASS |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --serial` | PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 3384a941 --head HEAD --serial` | PASS |

## Current Runtime Freshness Verification

| Surface | Command | Result |
|---|---|---|
| provider registry boundary | `git diff --name-only 3384a941..HEAD -- EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | PASS - no provider registry file in material diff |
| provider capability registry boundary | `git diff --name-only 3384a941..HEAD -- EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | PASS - no PROVIDER_CAPABILITY_REGISTRY mutation in material diff |
| runtime source boundary | `git diff --name-only 3384a941..HEAD -- EXTENSIONS/CVF_v1.6_AGENT_PLATFORM` | PASS - no runtime source path owned |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | direct operator authorization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance maintenance; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | orchestration command catalog GC-018 baseline |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- command catalog extraction and gate wiring only |
| receiptEvidence | CVF_RECEIPT_PRESENT - compile, size, ASSF gate, local hook, autorun, steward evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- runner extraction, new catalog helper modules, governed artifacts |
| invocationBoundary | local governed source and markdown edits |
| interceptionBoundary | no provider, Web, adapter, resolver, registry, package instance, public-sync, push, or session-sync claim |
| claimLanguage | maintenance baseline closed bounded |
| forbiddenExpansion | no package instance, activation, runtime behavior, resolver source mutation, Web projection implementation, CLI/MCP adapter, provider/live proof, public-sync, push, package execution, or session-sync |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_COMPLETION_2026-06-26.md` | completion review exists | PASS |
| Roadmap state | `docs/roadmaps/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation applies | no registry path owned | N/A with reason |
| Registry Markdown | N/A with reason: no registry markdown mutation applies | no registry path owned | N/A with reason |
| External evidence digest | N/A with reason: no external artifact applies | repository-local evidence only | N/A with reason |
| System loop interlock | N/A with reason: no system loop surface changed | gate remains in bundle | N/A with reason |
| Session continuity | N/A with reason: material commit excludes session-sync | session-sync follows separately if needed | N/A with reason |

## Claim Boundary

This GC-018 baseline authorizes only the orchestration command catalog refactor
and ASSF gate wiring.
