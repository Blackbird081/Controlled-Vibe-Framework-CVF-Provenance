# CVF Agent Work Order - ADIF-CLI-T1 CLI Classification And Entrypoints

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: ADIF-CLI-T1

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: d2ce31e0

executionBaseHead: d2ce31e0

closureBaseHead: d2ce31e0

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for ADIF CLI entrypoints and CLI
surface classification.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_CLI_T1_CLI_CLASSIFICATION_AND_ENTRYPOINTS_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ADIF_CLI_T1_CLI_CLASSIFICATION_AND_ENTRYPOINTS_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `d2ce31e0`.

Mission summary: add direct CLI entrypoints for ADIF agent-facing helpers and
add centralized CLI classification for future helper surface control.

Do-not-misread notes: this work order does not authorize ASSF package
activation, MCP adapter implementation, ADIF entry mutation, provider calls,
public-sync, or blanket CLI creation for every module.

## Purpose

Provide repeatable command surfaces for ADIF resolver/readout/intake work and
establish a central rule for deciding which future helpers should expose CLI
versus remain module-only.

## 1. Mission

Create and verify:

- CLI `main()` entrypoints for three ADIF helpers;
- `docs/reference/CVF_CLI_SURFACE_CLASSIFICATION_STANDARD_2026-06-30.md`;
- `governance/compat/CVF_CLI_SURFACE_CLASSIFICATION_REGISTRY.json`;
- `governance/compat/check_cli_surface_classification.py`;
- focused tests and CLI smoke evidence;
- baseline, work order, and completion evidence.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-06-30 for CLI plus centralized classification | authorizes ADIF-CLI-T1 opening |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V28_2026-06-30.md` | active handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ADIF_CLI_T1_CLI_CLASSIFICATION_AND_ENTRYPOINTS_2026-06-30.md` | scope and claim boundary |
| ADIF resolver source | `governance/compat/run_adif_defect_resolver.py` | target CLI surface |
| ADIF preflight source | `governance/compat/run_adif_preflight_readout.py` | target CLI surface |
| ADIF finding intake source | `governance/compat/run_adif_finding_intake_bridge.py` | target CLI surface |

Authority boundary: ADIF-CLI-T1 may add local command entrypoints and CLI
classification control. It may not widen governance runtime authority.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | add CLI entrypoints, registry, checker, and tests |
| Reviewer/closer | Codex | verify focused tests, CLI smokes, checker, and completion review |
| Future boundary owner | human operator | future MCP adapter, package activation, provider/live proof, public-sync, or hook wiring expansion |

## 4. Scope

Allowed paths:

- `docs/reference/CVF_CLI_SURFACE_CLASSIFICATION_STANDARD_2026-06-30.md`
- `governance/compat/CVF_CLI_SURFACE_CLASSIFICATION_REGISTRY.json`
- `governance/compat/check_cli_surface_classification.py`
- `governance/compat/test_check_cli_surface_classification.py`
- `governance/compat/run_adif_defect_resolver.py`
- `governance/compat/run_adif_preflight_readout.py`
- `governance/compat/run_adif_finding_intake_bridge.py`
- ADIF helper tests
- ADIF-CLI-T1 baseline, work order, and completion review

Forbidden paths:

- ADIF entry files except read-only resolver loading;
- ASSF package roots and lifecycle registries;
- CLI/MCP adapter code;
- provider route code;
- session state files unless a later session-sync tranche is opened;
- public-sync repository files.

Risk ceiling: R2 internal governance control.

## Scope / Target / Owner Boundary

Target: bounded local CLI entrypoints and CLI surface classification.

Owner boundary: Codex owns implementation and reviewer closure in this direct
tranche. Future adapter, provider/live, public-sync, package activation, hook
wiring expansion, and lifecycle-promotion decisions remain outside this
tranche.

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
- `governance/compat/run_adif_defect_resolver.py`
- `governance/compat/run_adif_preflight_readout.py`
- `governance/compat/run_adif_finding_intake_bridge.py`
- ADIF focused tests

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ADIF resolver already exposes bounded packet data | `governance/compat/run_adif_defect_resolver.py` | `DefectPacket.to_dict`; `resolve_defect_packet` | `DefectPacket`; `resolve_defect_packet` | ADIF resolver | RUNTIME_BEHAVIOR | ACCEPT |
| ADIF preflight readout already exposes human and JSON-ready data | `governance/compat/run_adif_preflight_readout.py` | `PreflightReadout.to_human_text`; `PreflightReadout.to_dict`; `build_preflight_readout` | `PreflightReadout`; `build_preflight_readout` | ADIF preflight readout | RUNTIME_BEHAVIOR | ACCEPT |
| ADIF finding intake already returns a non-mutating classification outcome | `governance/compat/run_adif_finding_intake_bridge.py` | `FindingIntakeOutcome.to_dict`; `classify_finding` | `FindingIntakeOutcome`; `classify_finding` | ADIF finding intake bridge | RUNTIME_BEHAVIOR | ACCEPT |
| Dispatch-quality split modules are implementation details behind a parent checker | `governance/compat/check_work_order_dispatch_quality.py` | parent checker command surface | `check_work_order_dispatch_quality_*.py` | dispatch-quality checker | RUNTIME_BEHAVIOR | ACCEPT |
| CLI surface classification standard is new in ADIF-CLI-T1 | `docs/reference/CVF_CLI_SURFACE_CLASSIFICATION_STANDARD_2026-06-30.md` | ADIF-CLI-T1 new file | `CLI_REQUIRED`; `CLI_OPTIONAL`; `MODULE_ONLY` | CLI surface classification standard | DOC_ONLY_NEW | ACCEPT |
| CLI surface classification registry is new in ADIF-CLI-T1 | `governance/compat/CVF_CLI_SURFACE_CLASSIFICATION_REGISTRY.json` | ADIF-CLI-T1 new file | `entries` | CLI surface classification registry | DOC_ONLY_NEW | ACCEPT |
| CLI surface classification checker is new in ADIF-CLI-T1 | `governance/compat/check_cli_surface_classification.py` | ADIF-CLI-T1 new file | `build_report` | CLI surface classification checker | DOC_ONLY_NEW | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ADIF resolver, preflight readout, finding intake bridge, dispatch-quality parent checker, and split modules |
| Runtime behavior claimed | local CLI entrypoints and classification checker |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=d2ce31e0`; `executionBaseHead=d2ce31e0`; `closureBaseHead=d2ce31e0` |
| changedSetScope(phase) | standard, registry, checker, helper CLI entrypoints, tests, baseline, work order, and completion review |
| traceScope(phase, actor) | work-order trace covers direct implementation; completion review trace covers reviewer closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit if committed |
| crossBatchIsolation | no ADIF entry mutation, ASSF activation, adapter, provider route, or public-sync work |
| nextMoveSurfaceHandling | session-sync follows material closure if closure changes next move |
| nextMoveSurfaces | active session state, front door, and handoff |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add CLI entrypoints to ADIF helpers and add
one CLI classification checker plus focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_adif_defect_resolver.py`
- `governance/compat/run_adif_preflight_readout.py`
- `governance/compat/run_adif_finding_intake_bridge.py`
- `governance/compat/test_run_adif_defect_resolver.py`
- `governance/compat/test_run_adif_preflight_readout.py`
- `governance/compat/test_run_adif_finding_intake_bridge.py`
- `governance/compat/CVF_CLI_SURFACE_CLASSIFICATION_REGISTRY.json`
- `governance/compat/check_cli_surface_classification.py`
- `governance/compat/test_check_cli_surface_classification.py`

Authorization evidence: the recorded instruction approved adding CLI and
requested centralized control for deciding which helpers should expose CLI
versus remain module-only.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/` and `governance/compat` |
| Storage decision | add one dated reference standard, one compact JSON registry, and one local checker |
| Stable filename disposition | registry and checker use stable names under `governance/compat` |
| Generated aggregate discipline | N/A with reason: no generated JSON aggregate is added |
| Authority boundary | the registry classifies helper CLI surfaces only; module source remains implementation authority |
| Forbidden expansion | no ADIF entry mutation, ASSF activation, MCP adapter, provider/live proof, public export, or universal hook claim |

## 7. Execution Instructions

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| CLI classification standard | Codex | create |
| CLI classification registry | Codex | create |
| CLI classification checker and tests | Codex | create |
| ADIF helper entrypoints and tests | Codex | update |
| ADIF-CLI-T1 artifacts | Codex | create |

## Pre-Flight Checks

| Check | Status |
|---|---|
| Startup front door and active handoff read | PASS |
| Guard orientation and literal-format gotchas read | PASS |
| ADIF resolver queried | PASS |
| ADIF helper sources read | PASS |

## Execution Plan

1. Add thin CLI wrappers around existing ADIF module APIs.
2. Add CLI classification standard, registry, checker, and tests.
3. Run focused unit tests and direct CLI smokes.
4. File completion review and run governance gates.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| Unit tests | ADIF helper and classification tests PASS |
| Resolver CLI smoke | ASSF-context disclosure command returns JSON and no defects |
| Preflight CLI smoke | returns bounded human-readable readout |
| Finding intake CLI smoke | returns JSON classification outcome |
| Classification checker | `python governance/compat/check_cli_surface_classification.py --enforce` PASS |

## Review Gate

Reviewer must confirm CLI wrappers preserve module behavior, classification
registry distinguishes command-facing and module-only surfaces, and no runtime
authority claim is introduced.

## Closure Checklist

| Item | Status |
|---|---|
| ADIF resolver CLI added | PASS |
| ADIF preflight CLI added | PASS |
| ADIF finding intake CLI added | PASS |
| CLI classification standard, registry, checker, and tests added | PASS |
| Unit tests pass | PASS |
| CLI smokes pass | PASS |
| Completion review filed | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after focused tests, CLI smokes, and
classification checker pass. Return `BLOCKED` if CLI entrypoints require
changing ADIF entry lifecycle or runtime package activation semantics.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | ADIF resolver CLI exists and preserves module API | tests and CLI smoke PASS |
| AC2 | ADIF preflight CLI exists and preserves resolver delegation | tests and CLI smoke PASS |
| AC3 | ADIF finding intake CLI exists and remains non-mutating | tests and CLI smoke PASS |
| AC4 | Central classification controls CLI-required and module-only surfaces | registry and checker PASS |
| AC5 | No provider/live, MCP adapter, ASSF activation, public-sync, or ADIF entry mutation is claimed | claim boundary PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: no CVF runtime skill package instruction body was consumed |
| Package root | N/A with reason: no package body was requested |
| Invocation context | local Python helper and governance checker work only |
| Receipt evidence | N/A with reason: no skill usage receipt is emitted for local ADIF helper CLI work |
| Output consumed by CVF | local command outputs and tests |
| Truth packet or source path | N/A with reason: no skill truth packet was consumed |
| Authority boundary | local CLI evidence does not activate skills or grant runtime package authority |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | N/A with reason: local Python and repo files only |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this work order and completion review |
| Authority boundary | provider-owned skill output is not CVF canonical authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local CVF implementation -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ADIF-CLI-T1 baseline, work order, completion review, standard, registry, checker, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | ADIF-CLI-T1 CLI classification and entrypoints on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; CLI smokes; classification checker |
| Target paths | standard, registry, checker, ADIF helpers, tests, baseline, work order, completion review |
| Allowed scope source | recorded instruction plus ADIF-CLI-T1 baseline and work order |
| Before status evidence | base commit `d2ce31e0`; clean worktree before ADIF-CLI-T1 edits |
| After status evidence | local material changed set pending closure gates |
| Diff evidence | focused tests, CLI smokes, checker, and governance gates |
| Approval boundary | recorded instruction requested CLI and centralized classification; live API keys not needed because no live behavior claim is made |
| Claim boundary | bounded local CLI and classification only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-adif-cli-t1-cli-classification-and-entrypoints-2026-06-30` |
| Expected manifest | standard, registry, checker, helper updates, tests, baseline, work order, completion review |
| Actual changed set | standard, registry, checker, helper updates, tests, baseline, work order, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references internal ADIF and governance helper
surfaces. Public-safe export requires separate public-sync authorization.

## Operator Checkpoint

No pending human decision remains for this bounded ADIF-CLI-T1 tranche. Future
MCP adapter implementation, ASSF package activation, provider/live proof,
public-sync, or hook wiring expansion remains outside this scope.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ADIF_CLI_T1_CLI_CLASSIFICATION_AND_ENTRYPOINTS_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: ADIF-CLI-T1 is a direct requested governance tranche, not a roadmap-derived tranche | N/A with reason | PASS |
| Registry JSON | `governance/compat/CVF_CLI_SURFACE_CLASSIFICATION_REGISTRY.json` | checker PASS | PASS |
| Registry Markdown | `docs/reference/CVF_CLI_SURFACE_CLASSIFICATION_STANDARD_2026-06-30.md` | `Status: ACTIVE_STANDARD` | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no provider route, adapter, or package execution changed | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | ADIF and CLI classification tests | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| ADIF resolver CLI | implemented | direct CLI smoke returned JSON | PASS |
| ADIF preflight CLI | implemented | direct CLI smoke returned bounded readout | PASS |
| ADIF finding intake CLI | implemented | direct CLI smoke returned `LINK_TO_EXISTING_ENTRY` | PASS |
| Classification checker | compliant | 9 entries, 0 violations | PASS |
| Unit test status | PASS | 44 tests PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Claim Boundary

ADIF-CLI-T1 adds local CLI entrypoints and centralized classification only. It
does not activate skills, mutate ADIF entries, implement MCP adapters, call
providers, public-sync, or grant runtime authority.
