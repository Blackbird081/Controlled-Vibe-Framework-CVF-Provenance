# CVF Roadmap: Orchestration Command Catalog Refactor And ASSF Gate Wiring

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: roadmap

Batch ID: ORCHESTRATION-CATALOG-ASSF-WIRING

baseHead: 3384a941

## Purpose

Close a bounded maintenance tranche that refactors near-limit orchestration
command catalogs and wires the ASSF certified metadata admission checker into
the standard local and autorun gate bundles.

## Authorization / Decision

| Field | Disposition |
|---|---|
| Authorization source | operator instruction to proactively refactor the near-limit orchestration files |
| Decision scope | command catalog extraction plus ASSF admission gate wiring |
| Material base | `3384a941` |
| Closure posture | `CLOSED_PASS_BOUNDED` |

## Scope / Methodology

Codex split command catalog data out of the two orchestration runners, kept the
runners focused on execution flow, added the ASSF admission checker to the new
catalog modules, and verified that the size guard no longer forces avoidance of
the gate wiring.

## Findings / Position

The two orchestration runners were at their approved exception limits. The
correct response is to reduce the runners, not to leave a valid gate outside the
standard bundles. This tranche closes that maintenance debt while keeping
package, Web, runtime, provider, public-sync, and session-sync work outside the
material commit.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| command catalog extraction could break runner imports | py_compile and live gate commands required |
| adding the ASSF gate could re-trigger size guard failures | catalog extraction reduces runner line counts before wiring |
| protected governance paths need authorization | completion review includes Core Guard Self-Protection Authorization |
| this maintenance could broaden ASSF scope | no registry, resolver, package, Web, runtime, public, or provider paths are owned |

## Non-Goals

| Non-goal | Reason |
|---|---|
| package instance creation or activation | command catalog maintenance only |
| resolver or registry mutation | ASSF admission gate already exists and remains read-only |
| Web runtime or schema mutation | Web projection remains parked |
| CLI/MCP adapter behavior | outside this maintenance tranche |
| provider/live proof, public-sync, push, or session-sync | outside the material commit |

## Design Control Gate

| Control | Required outcome | Status |
|---|---|---|
| file-size maintainability | runners reduced below prior exception-limit pressure | PASS |
| hook-chain coverage | local hook command catalogs include ASSF admission gate | PASS |
| autorun coverage | autorun common command catalog includes ASSF admission gate | PASS |
| bounded scope | no package/Web/runtime/provider/public/session work enters material commit | PASS |

## Tranche Plan

| Tranche | Objective | Artifact | Status |
|---|---|---|---|
| T0 | confirm near-limit runner debt and source locations | this roadmap and baseline | COMPLETE |
| T1 | extract local hook command catalogs | `governance/compat/local_governance_hook_catalog.py` plus local hook chain modules | COMPLETE |
| T2 | extract autorun command catalog | `governance/compat/agent_autorun_command_catalog.py` | COMPLETE |
| T3 | wire ASSF admission checker into catalogs | catalog modules | COMPLETE |
| T4 | verify size, compile, gates, and closure | completion review | COMPLETE |

## Work Plan

| Step | Work | Output |
|---|---|---|
| 1 | identify orchestration command catalog boundaries | GC-018 baseline |
| 2 | extract local hook command chains | local catalog modules |
| 3 | extract autorun command builder catalog | autorun catalog module |
| 4 | wire ASSF admission gate | catalog source rows |
| 5 | verify and close | completion review |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order instruction | Closure evidence | Disposition |
|---|---|---|---|
| refactor near-limit orchestration files | extract command catalog modules | runner line counts below prior exception limits | PASS |
| wire ASSF admission gate | add checker command to local and autorun catalogs | catalog source and gate output | PASS |
| preserve bounded scope | forbid package/Web/runtime/public/provider/session work | changed set and completion review | PASS |
| verify governance health | run focused and bundled gates | completion review evidence table | PASS |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | `run_local_governance_hook_chain.py` line count is materially reduced | PASS |
| AC2 | `run_agent_autorun_workflow_gate.py` line count is materially reduced | PASS |
| AC3 | ASSF admission checker is present in all local hook chain catalogs | PASS |
| AC4 | ASSF admission checker is present in autorun common command catalog | PASS |
| AC5 | no package, Web, resolver, registry, provider, public-sync, push, or session-sync mutation is part of the material change | PASS |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| local runner imports extracted catalog | `governance/compat/run_local_governance_hook_chain.py` | lines 125-131 | `HOOK_CHAINS` | local hook runner | EXISTS | ACCEPT |
| local catalog aggregator defines hook chains | `governance/compat/local_governance_hook_catalog.py` | lines 19-23 | `HOOK_CHAINS` | local hook catalog aggregator | EXISTS | ACCEPT |
| reviewer-fast local chain includes ASSF gate | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | line 120 | `ASSF certified metadata admission` | reviewer-fast hook catalog | EXISTS | ACCEPT |
| pre-commit local chain includes ASSF gate | `governance/compat/local_governance_hook_catalog_pre_commit.py` | line 175 | `ASSF certified metadata admission` | pre-commit hook catalog | EXISTS | ACCEPT |
| pre-push local chain includes ASSF gate | `governance/compat/local_governance_hook_catalog_pre_push.py` | line 136 | `ASSF certified metadata admission` | pre-push hook catalog | EXISTS | ACCEPT |
| autorun runner imports extracted catalog | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 36-54 | `_common_commands` | autorun workflow runner | EXISTS | ACCEPT |
| autorun catalog includes ASSF gate | `governance/compat/agent_autorun_command_catalog.py` | lines 255-257 | `ASSF certified metadata admission` | autorun command catalog | EXISTS | ACCEPT |
| ASSF admission checker exists | `governance/compat/check_assf_certified_metadata_admission.py` | line 168 | `check` | ASSF admission checker | EXISTS | ACCEPT |

## Verification / Evidence

| Evidence | Result |
|---|---|
| `python -m py_compile governance/compat/run_local_governance_hook_chain.py governance/compat/local_governance_hook_catalog.py governance/compat/local_governance_hook_catalog_reviewer_fast.py governance/compat/local_governance_hook_catalog_pre_commit.py governance/compat/local_governance_hook_catalog_pre_push.py governance/compat/run_agent_autorun_workflow_gate.py governance/compat/agent_autorun_command_catalog.py` | PASS |
| line count measurement | PASS - runners reduced to 280 and 451 lines before final closure gates |
| `python governance/compat/check_python_automation_size.py --enforce` | required in completion |
| `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | required in completion |
| bundled local and autorun gates | required in completion |

## Current Runtime Freshness Verification

| Surface | Command | Result |
|---|---|---|
| provider registry boundary | `git diff --name-only 3384a941..HEAD -- EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | PASS - no provider registry file in material diff |
| provider capability registry boundary | `git diff --name-only 3384a941..HEAD -- EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | PASS - no PROVIDER_CAPABILITY_REGISTRY mutation in material diff |
| runtime source boundary | `git diff --name-only 3384a941..HEAD -- EXTENSIONS/CVF_v1.6_AGENT_PLATFORM` | PASS - no runtime source path owned |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance maintenance; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | orchestration command catalog refactor and ASSF gate wiring roadmap |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- command catalog extraction and gate wiring only |
| receiptEvidence | CVF_RECEIPT_PRESENT - compile, size, ASSF gate, local hook, autorun, steward evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- runner extraction, new catalog helper modules, governed artifacts |
| invocationBoundary | local governed source and markdown edits |
| interceptionBoundary | no provider, Web, adapter, resolver, registry, package instance, public-sync, push, or session-sync claim |
| claimLanguage | maintenance roadmap closed bounded |
| forbiddenExpansion | no package instance, activation, runtime behavior, resolver source mutation, Web projection implementation, CLI/MCP adapter, provider/live proof, public-sync, push, package execution, or session-sync |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_COMPLETION_2026-06-26.md` | completion review exists | PASS |
| Roadmap state | this roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation applies | no registry path owned | N/A with reason |
| Registry Markdown | N/A with reason: no registry markdown mutation applies | no registry path owned | N/A with reason |
| External evidence digest | N/A with reason: no external artifact applies | repository-local evidence only | N/A with reason |
| System loop interlock | N/A with reason: no system loop surface changed | gate remains in bundle | N/A with reason |
| Session continuity | N/A with reason: material commit excludes session-sync | session-sync follows separately if needed | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| ARAM-ORCH-R01 | line count measurement | runner line count | below prior exception limit | 280 and 451 | PASS |
| ARAM-ORCH-R02 | local hook chain catalogs | command label | `ASSF certified metadata admission` | present in reviewer-fast, pre-commit, and pre-push | PASS |
| ARAM-ORCH-R03 | `governance/compat/agent_autorun_command_catalog.py` | command label | `ASSF certified metadata admission` | present | PASS |

## Claim Boundary

This roadmap closes only the orchestration command catalog refactor and ASSF
gate wiring. Session-sync, Web projection, package instance work, resolver or
registry mutation, provider/live proof, public-sync, and push remain outside
this material closure.
