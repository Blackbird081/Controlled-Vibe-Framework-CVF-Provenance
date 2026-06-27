# CVF Agent Work Order: Guard Binding Catalog-Aware Checker Hardening

Memory class: work-order
Status: CLOSED_PASS
dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_FOR_CODEX_2026-06-26.md`
Owner: Codex reviewer/closer multi-role
Date: 2026-06-26

## Purpose

Implement the roadmap and baseline for catalog-aware checker binding validation.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator request | current session | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_ROADMAP_2026-06-26.md` | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_2026-06-26.md` | ACCEPT |
| Guard orientation | `docs/reference/guard_orientation/README.md` | ACCEPT |

## Agent Roles

| Role | Agent | Commit mode |
|---|---|---|
| Dispatcher | Codex | WORKER_MAY_COMMIT |
| Worker | Codex | WORKER_MAY_COMMIT |
| Reviewer/closer | Codex | WORKER_MAY_COMMIT |

## Scope

Allowed scope:

- Add shared binding helper.
- Update checkers that validate runner binding markers.
- Remove marker-only constants from the two runner files.
- Add narrow governed artifacts for the batch.

Allowed paths:

- `docs/baselines/CVF_GC018_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_2026-06-26.md`
- `docs/reviews/CVF_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_COMPLETION_2026-06-26.md`
- `docs/roadmaps/CVF_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_ROADMAP_2026-06-26.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_FOR_CODEX_2026-06-26.md`
- `governance/compat/guard_binding_catalog.py`
- `governance/compat/check_active_session_state.py`
- `governance/compat/check_agent_workspace_skeleton.py`
- `governance/compat/check_agent_handoff_boundary.py`
- `governance/compat/check_agent_workspace_design.py`
- `governance/compat/check_agent_workspace_runtime_boundary.py`
- `governance/compat/check_agent_workspace_state.py`
- `governance/compat/check_corpus_completeness_report_integrity.py`
- `governance/compat/check_corpus_intelligence_classification.py`
- `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`
- `governance/compat/check_finding_to_governance_learning.py`
- `governance/compat/check_foundation_storage_layout.py`
- `governance/compat/check_index_classification.py`
- `governance/compat/check_markdown_structural_completeness.py`
- `governance/compat/check_multi_provider_execution_log.py`
- `governance/compat/check_public_export_disposition.py`
- `governance/compat/check_rescan_intelligence_hardening.py`
- `governance/compat/check_system_loop_interlock.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Forbidden scope:

- Package instance creation.
- Certification decision.
- Generated-index mutation.
- Resolver mutation.
- Web runtime change.
- CLI/MCP adapter change.
- Provider/live proof.
- Public-sync or push.

## Required First Reads

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V22_2026-06-22.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |

## Pre-Flight Checks

| Check | Disposition |
|---|---|
| Worktree inspected before material edits | PASS |
| ADIF resolver queried | PASS |
| Protected paths authorized | PASS |

## Write Ownership

| Path | Ownership |
|---|---|
| `governance/compat/guard_binding_catalog.py` | CODEX |
| `governance/compat/check_*.py` listed in baseline | CODEX |
| `governance/compat/run_agent_autorun_workflow_gate.py` | CODEX |
| `governance/compat/run_local_governance_hook_chain.py` | CODEX |
| `docs/roadmaps/CVF_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_ROADMAP_2026-06-26.md` | CODEX |
| `docs/baselines/CVF_GC018_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_2026-06-26.md` | CODEX |
| `docs/reviews/CVF_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_COMPLETION_2026-06-26.md` | CODEX |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Catalog paths are explicitly mapped by runner path | `governance/compat/guard_binding_catalog.py` | line 14 | `CATALOG_PATHS_BY_RUNNER` | guard binding catalog helper | ACCEPT |
| Effective binding text returns runner text plus catalog text | `governance/compat/guard_binding_catalog.py` | line 36 | `effective_binding_text` | guard binding catalog helper | ACCEPT |
| Marker lookup is centralized | `governance/compat/guard_binding_catalog.py` | line 50 | `has_binding_marker` | guard binding catalog helper | ACCEPT |
| Work-order marker validation reads effective binding text | `governance/compat/check_work_order_dispatch_quality.py` | line 2887 | `effective_binding_text` | `_run_check` marker validation | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Closure evidence |
|---|---|---|
| Add shared helper | Create `guard_binding_catalog.py` | PASS |
| Convert checkers | Import helper and replace direct text lookup | PASS |
| Remove marker constants | Delete `CATALOG_BINDING_MARKERS` from runners | PASS |
| Run gates | Execute targeted binding gates | PASS |

## ADIF Defect Registry Disclosure

Query:

`python governance/compat/run_adif_defect_resolver.py --task-class guard-binding-catalog-aware-checker-hardening --role codex-multi-role --phase material-implementation --surface governance/compat --risk-ceiling R1`

Resolver query: taskClass=`guard-binding-catalog-aware-checker-hardening`, role=`codex-multi-role`, lifecyclePhase=`material-implementation`

Returned defects: NONE_RETURNED

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| foundationWork | YES |
| reason | Governance checker helper added in `governance/compat` next to consuming checkers |
| stablePathDecision | Existing checker/helper folder retained |
| indexUpdate | N/A with reason: no docs/reference front-door index changed |
| archiveMove | N/A with reason: no material archive move in this work order |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| contractSource | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | Codex dispatcher, worker, reviewer, closer in one batch |
| phase | material-implementation |
| baseHeadFor(phase) | `f73546c5` |
| dispatchBaseHead | `f73546c5` |
| executionBaseHead | `f73546c5` |
| closureBaseHead | `f73546c5` |
| changedSetScope(phase) | paths listed in Write Ownership |
| traceScope(phase, actor) | Codex material diff and command evidence |
| commitOwner(phase) | Codex |
| crossBatchIsolation | Session compaction is separate |
| nextMoveSurfaces | No next-move change in material commit |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| runtimeMutation | N/A with reason: no runtime file changed |
| webMutation | N/A with reason: no Web file changed |
| providerProof | N/A with reason: no live provider claim made |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | N/A with reason: this work order does not design or build an agent-interaction workspace |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | N/A with reason: no workspace storage path changed |
| Handoff fields | N/A with reason: no workspace handoff field changed |
| State ownership | N/A with reason: no workspace state changed |
| Guard owner | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Build boundary | No runtime source, provider proof, public-sync, or registry edits are authorized |

## External Knowledge Intake Routing

Chain map citation: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | local governance checker source only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `governance/compat` |
| Disposition | N/A with reason: no external knowledge was used |
| Claim boundary | local repo evidence only |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | Material checker/catalog-binding hardening only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT in command outputs from targeted gates |
| actionEvidence | ACTION_EVIDENCE_PRESENT in git diff and targeted checker runs |
| invocationBoundary | Local Python commands only |
| interceptionBoundary | No live provider, Web, package, resolver, generated-index, or public-sync work |
| claimLanguage | bounded implementation and verification claim |
| forbiddenExpansion | No package instance, certification decision, Web runtime, CLI/MCP adapter, generated-index, resolver, provider proof, public-sync, or push |

## Execution Plan

| Step | Result |
|---|---|
| Add helper module | PASS |
| Convert checker imports and lookups | PASS |
| Remove runner marker constants | PASS |
| Run py_compile and targeted gates | PASS |

## Evidence Requirements

| Evidence | Required | Result |
|---|---|---|
| Python compile | YES | PASS |
| Targeted binding gates | YES | PASS |
| `git diff --check` | YES | pending final pre-commit run |
| Commit steward | YES | pending final pre-commit run |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-26 governed material batch |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, Python, git |
| Target paths | Write Ownership section |
| Allowed scope source | this work order and GC-018 baseline |
| Before status evidence | `git status --short` material edit set |
| After status evidence | final closure gates before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator authorized checker catalog-reader hardening |
| Claim boundary | material checker/catalog-binding hardening only |
| Agent type | single-agent multi-role |
| Invocation ID | local Codex session 2026-06-26 |
| Expected manifest | Write Ownership section |
| Actual changed set | completion review Actual Changed Set |
| Manifest delta | N/A with reason: no out-of-scope material paths intended |

## Acceptance Criteria

| Criterion | Status |
|---|---|
| Catalog-aware binding helper exists | PASS |
| Direct runner text checks use helper | PASS |
| Required marker checks use effective binding text | PASS |
| Marker constants are removed from runners | PASS |

## Review Gate

Reviewer must verify targeted gates and ensure no session-sync change is included in the material commit.

## Closure Checklist

| Item | Status |
|---|---|
| Material paths only | PASS |
| Protected path authorization present | PASS |
| No forbidden scope mutation | PASS |
| Session-sync split reserved for later commit | PASS |

## Return-To-Orchestrator Conditions

Return only if catalog-aware helper fails binding gates or if protected-path authorization is rejected.

## Operator Checkpoint

Operator already authorized proactive checker hardening and front-door/handoff compaction. This work order covers only the material checker hardening portion.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_COMPLETION_2026-06-26.md` | `Status: CLOSED_PASS` | PASS |
| Roadmap state | `docs/roadmaps/CVF_GUARD_BINDING_CATALOG_AWARE_CHECKER_HARDENING_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | Not a GC-051 registry update; registry surfaces are outside this material scope | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | Not a GC-051 registry update; registry surfaces are outside this material scope | BLOCKED with reason |
| External evidence digest | N/A with reason | No external evidence used | N/A with reason |
| System loop interlock | N/A with reason | No system loop runtime changed | N/A with reason |
| Session continuity | N/A with reason | Session sync is split into a later commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Receipt |
|---|---|
| Work order scope closed | Completion review |
| Binding gates pass | Completion review command evidence |
| Session compaction separated | Completion review claim boundary |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This work order closes only the checker/catalog-binding hardening material batch.
