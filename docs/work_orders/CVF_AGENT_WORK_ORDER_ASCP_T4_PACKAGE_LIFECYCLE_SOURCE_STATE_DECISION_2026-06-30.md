# CVF Agent Work Order - ASCP-T4 Package Lifecycle Source-State Decision

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: ASCP-T4

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: 566cde63

executionBaseHead: 566cde63

closureBaseHead: 566cde63

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for ASSF package lifecycle
source-state decision.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `566cde63`.

Mission summary: implement a read-only decision helper proving whether any
package lifecycle source should move to `ACTIVE` after ASCP-T1 through ASCP-T3.

Do-not-misread notes: this work order does not authorize package lifecycle
mutation, package body reads, skill usage receipt emission or consumption,
provider calls, MCP server behavior, public-sync, or remaining package runtime
conversion.

## Purpose

Close ASCP-T4 with a source-backed decision: current ASSF sources stay
unchanged and no package source moves to `ACTIVE` in this tranche.

## 1. Mission

Create and verify:

- lifecycle source-state decision helper;
- focused lifecycle decision tests;
- roadmap update from ASCP-T4 ready to closed bounded;
- baseline, work order, and completion evidence.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat approval on 2026-06-30 for ASCP next move | authorizes ASCP-T4 execution |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V28_2026-06-30.md` | active handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_2026-06-30.md` | scope and claim boundary |
| ASCP roadmap | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | T4 objective and T5 parked lane |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | lifecycle state semantics |
| Activation policy standard | `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md` | readiness is not lifecycle activation |

Authority boundary: ASCP-T4 may emit a read-only lifecycle decision receipt. It
may not mutate lifecycle sources, regenerate indexes, read package instruction
bodies, emit or consume usage receipts, call providers, implement execution
adapters, or reopen remaining package conversion.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | add lifecycle decision helper, tests, and roadmap update |
| Reviewer/closer | Codex | verify tests, smoke, changed set, and completion review |
| Operator approval required | operator | package execution adapter, provider/live proof, public-sync, package conversion, or lifecycle promotion |

## 4. Scope

Allowed paths:

- `governance/compat/run_assf_package_lifecycle_decision.py`
- `governance/compat/test_run_assf_package_lifecycle_decision.py`
- `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md`
- `docs/baselines/CVF_GC018_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_2026-06-30.md`
- `docs/reviews/CVF_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_COMPLETION_2026-06-30.md`

Forbidden paths:

- ASSF registry lifecycle sources;
- generated ASSF skill index;
- ASSF truth packets;
- ASSF package roots;
- provider route code;
- MCP server, daemon, hook, or IDE bridge implementation;
- session state files unless a later session-sync tranche is opened;
- public-sync repository files.

Risk ceiling: R2 internal governance control.

## Scope / Target / Owner Boundary

Target: bounded lifecycle source-state decision for ASSF package control.

Owner boundary: Codex owns implementation and reviewer closure in this direct
tranche; operator owns future provider/live, public-sync, package conversion,
execution adapter, and lifecycle-promotion decisions.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`docs/reference/agent_system_skills`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure command:

```text
python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase implementation --surface-selector docs/reference/agent_system_skills --risk-ceiling HIGH --max-results 20 --json
```

## 5. Required First Reads

Read before editing:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V28_2026-06-30.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md`
- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/run_assf_active_resolver.py`
- `governance/compat/run_assf_cli_mcp_adapter_projection.py`

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASCP roadmap requires T4 package lifecycle source decision after T3 closure | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | Work Plan | `ASCP-T4` | ASCP roadmap | VALUE_SET | ACCEPT |
| ASSF contract defines `ACTIVE` as lifecycle state selected for governed resolver/index use | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | `ACTIVE` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Activation policy standard distinguishes readiness from lifecycle activation | `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md` | State Semantics | `ACTIVATION_READY` | activation policy semantics standard | LITERAL_INVARIANT | ACCEPT |
| Runtime loader reads package bodies only on explicit eligible body request | `governance/compat/run_assf_runtime_package_loader.py` | `build_runtime_package_packet` | `include_instruction_bodies` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| CLI/MCP projection denies external body reads and output use | `governance/compat/run_assf_cli_mcp_adapter_projection.py` | constants and `build_cli_mcp_adapter_projection` | `DENIED_EXTERNAL_BODY_READ_NOT_IMPLEMENTED` | CLI/MCP projection helper | RUNTIME_BEHAVIOR | ACCEPT |
| Provider registry surfaces are out of scope and untouched by ASCP-T4 | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | runtime source files | `ProviderRegistry`; `PROVIDER_CAPABILITY_REGISTRY` | Model Gateway provider registry surfaces | BOUNDARY_REFERENCE | ACCEPT |
| Lifecycle decision helper is new in ASCP-T4 | `governance/compat/run_assf_package_lifecycle_decision.py` | ASCP-T4 new file | `build_package_lifecycle_decision` | package lifecycle decision helper | DOC_ONLY_NEW | ACCEPT |

## Provider Registry Boundary

ASCP-T4 makes no provider registry absence, hardcoded-provider,
provider-selection, provider-routing, model-capability, or live-governance
claim. Current provider registry surfaces are accounted for and remain
untouched: `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` exports
`ProviderRegistry`, and `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
declares `PROVIDER_CAPABILITY_REGISTRY`.

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Decide whether package lifecycle source should move to `ACTIVE` | Purpose; Mission | lifecycle decision helper and completion review | unit tests and smoke | PASS |
| Keep readiness separate from lifecycle activation | Source Verification; Claim Boundary | `HOLD_NO_ACTIVE_SOURCE_MUTATION` | lifecycle decision smoke | PASS |
| Preserve package sources and generated index | Scope; Evidence Requirements | no registry/index/package root mutation | changed set review | PASS |
| Keep ASCP-T5 value-parked | Roadmap update | T5 remains `VALUE_PARKED` | roadmap review | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=566cde63`; `executionBaseHead=566cde63`; `closureBaseHead=566cde63` |
| changedSetScope(phase) | lifecycle decision helper, tests, roadmap update, baseline, work order, and completion review |
| traceScope(phase, actor) | work-order trace covers implementation; completion review trace covers closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit if committed |
| crossBatchIsolation | no ASSF lifecycle state, package body, provider route, execution adapter, generated index, truth packet, or public-sync mutation |
| nextMoveSurfaceHandling | session-sync follows material closure |
| nextMoveSurfaces | active session state, front door, and handoff |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one bounded lifecycle decision helper
and focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_assf_package_lifecycle_decision.py`
- `governance/compat/test_run_assf_package_lifecycle_decision.py`

Operator authorization: active next move authorizes ASCP-T4 after ASCP-T3
closure.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASCP roadmap, ASSF package contract, activation policy semantics standard, runtime package loader, active resolver, CLI/MCP projection helper |
| Runtime behavior claimed | local lifecycle source-state decision only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support hold decision, not lifecycle mutation |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/agent_system_skills/` and `governance/compat` |
| Storage decision | add local decision helper, not a generated aggregate |
| Stable filename disposition | `governance/compat/run_assf_package_lifecycle_decision.py` |
| Generated aggregate discipline | N/A with reason: no generated JSON aggregate is added or edited |
| Authority boundary | decision receipt is readout evidence only; package sources, truth packets, and work orders remain authority |
| Forbidden expansion | no lifecycle mutation, package body read, usage receipt, provider/live proof, public export, execution adapter, or package conversion |

## 7. Execution Instructions

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| lifecycle decision helper and tests | Codex | create |
| ASCP roadmap | Codex | update T4/T5 rows only |
| ASCP-T4 artifacts | Codex | create |

## Pre-Flight Checks

| Check | Status |
|---|---|
| Startup front door and active handoff read | PASS |
| Guard orientation and literal-format gotchas read | PASS |
| ADIF resolver queried | PASS |
| Runtime loader, active resolver, activation policy standard, and projection helper read | PASS |

## Execution Plan

1. Add lifecycle source-state decision helper.
2. Add focused tests.
3. Run focused tests and lifecycle decision smoke.
4. Update roadmap T4/T5 state and file completion review.
5. Run governance gates and commit.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| Unit tests | `python -m unittest governance.compat.test_run_assf_package_lifecycle_decision` PASS |
| Lifecycle decision smoke | decision returns `HOLD_NO_ACTIVE_SOURCE_MUTATION` with 6 ready packages and 0 active source records |
| Changed set review | no registry entries, generated indexes, truth packets, package roots, provider code, execution adapter, or public-sync mutation |

## Review Gate

Reviewer must confirm readiness is not lifecycle activation, the helper does
not write source files or open package bodies, and ASCP-T5 remains value-parked.

## Closure Checklist

| Item | Status |
|---|---|
| Lifecycle decision helper created | PASS |
| Focused tests created | PASS |
| Unit tests pass | PASS |
| Lifecycle decision smoke passes | PASS |
| Roadmap update filed | PASS |
| Completion review filed | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after focused tests, smoke, changed set
review, and governance gates pass. Return `BLOCKED` if decision semantics
require lifecycle mutation, registry/index edits, package body reads, usage
receipt mutation, provider calls, or execution adapter behavior.

## Operator Checkpoint

No further operator checkpoint is required for ASCP-T4 closure. Future package
execution adapter behavior, automatic invocation, lifecycle mutation,
provider/live proof, public-sync, or remaining package conversion requires
fresh authorization.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Decision helper summarizes ready and active source counts | unit tests PASS |
| AC2 | Helper emits `HOLD_NO_ACTIVE_SOURCE_MUTATION` | unit tests and smoke PASS |
| AC3 | Helper emits no source mutation recommendations | unit tests PASS |
| AC4 | Helper does not open package bodies or write files | unit tests PASS |
| AC5 | ASCP-T5 remains value-parked | roadmap update PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: ASCP-T4 did not consume package instruction output as work evidence |
| Package root | N/A with reason: no package body was read by ASCP-T4 decision helper |
| Invocation context | ASCP-T4 decision tests and smoke |
| Receipt evidence | N/A with reason: no loader usage receipt output was consumed |
| Output consumed by CVF | local lifecycle decision output only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | decision output does not grant authority, activate packages, or bypass work-order scope |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | local Python helper and repo metadata only |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this work order and paired completion review |
| Authority boundary | provider-owned skill output is not CVF canonical authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local CVF skill-control implementation -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASCP-T4 roadmap, baseline, work order, completion review, helper, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | ASCP-T4 package lifecycle source-state decision on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; lifecycle decision smoke |
| Target paths | helper, tests, roadmap, baseline, work order, completion review |
| Allowed scope source | active next move plus ASCP-T4 baseline and work order |
| Before status evidence | base commit `566cde63`; clean worktree before ASCP-T4 edits |
| After status evidence | pending material closure changed set |
| Diff evidence | focused tests, lifecycle decision smoke, changed set review, and governance gates |
| Approval boundary | active next move authorized ASCP-T4; live API keys not needed because no live behavior claim is made |
| Claim boundary | bounded lifecycle source-state decision only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-ascp-t4-package-lifecycle-source-state-decision-2026-06-30` |
| Expected manifest | helper, tests, roadmap update, baseline, work order, completion review |
| Actual changed set | helper, tests, roadmap update, baseline, work order, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references internal ASSF governance and private
provenance surfaces. Public-safe export requires separate public-sync
authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_T4_PACKAGE_LIFECYCLE_SOURCE_STATE_DECISION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | `Status: ACTIVE_ROADMAP` | PASS |
| Registry JSON | N/A with reason: no registry mutation authorized or performed | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no provider route, execution adapter, or package execution changed | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | lifecycle decision tests | PASS | PASS |
| Runtime smoke | lifecycle decision smoke | PASS | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Lifecycle decision | `HOLD_NO_ACTIVE_SOURCE_MUTATION` | helper emits decision token | PASS |
| Source mutation disposition | `NO_SOURCE_MUTATIONS_AUTHORIZED` | helper emits disposition token | PASS |
| Runtime eligible count | 6 | lifecycle decision smoke observed 6 | PASS |
| Activation ready count | 6 | lifecycle decision smoke observed 6 | PASS |
| Active source count | 0 | lifecycle decision smoke observed 0 | PASS |
| Unit test status | PASS | `python -m unittest governance.compat.test_run_assf_package_lifecycle_decision` PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Claim Boundary

ASCP-T4 implements bounded lifecycle source-state decision only. It does not
activate skills, mutate package lifecycle state, read package instruction
bodies, emit or consume skill usage receipts, implement package execution
adapters, call providers, public-sync, or grant action authority.
