# CVF Agent Work Order - ASCP-T1 ACTIVE Resolver Pilot

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: ASCP-T1

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: c134346e

executionBaseHead: c134346e

closureBaseHead: c134346e

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for ASSF active resolver pilot.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T1_ACTIVE_RESOLVER_PILOT_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASCP_T1_ACTIVE_RESOLVER_PILOT_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `c134346e`.

Mission summary: implement a read-only ACTIVE resolver decision layer that
combines generated ASSF metadata, truth index records, and existing runtime
loader eligibility without body reads.

Do-not-misread notes: this work order does not authorize lifecycle mutation,
automatic package invocation, package body reads, external adapters, provider
calls, public-sync, or remaining package runtime conversion.

## Purpose

Implement the first bounded ACTIVE resolver layer so CVF can tell which current
runtime packages are ready for explicit body-load invocation while preserving a
traceable distinction between selection, readiness, and actual use.

## 1. Mission

Create and verify:

- `governance/compat/run_assf_active_resolver.py`;
- `governance/compat/test_run_assf_active_resolver.py`;
- roadmap, baseline, work order, and completion evidence;
- focused tests and real repo smoke showing 6 ready packages.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat approval on 2026-06-30 for ACTIVE resolver / CLI-MCP adapter / package activation roadmap | authorizes ASCP roadmap and T1 opening |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V28_2026-06-30.md` | active handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASCP_T1_ACTIVE_RESOLVER_PILOT_2026-06-30.md` | scope and claim boundary |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | lifecycle and adapter boundary |
| Skill truth packet standard | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | truth packet authority |
| Runtime loader | `governance/compat/run_assf_runtime_package_loader.py` | eligibility behavior |

Authority boundary: ASCP-T1 may add resolver decision logic and tests. It may
not mutate lifecycle sources or read package instruction bodies.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | add resolver helper and tests |
| Reviewer/closer | Codex | verify focused tests, smoke, and completion review |
| Operator approval required | operator | future lifecycle mutation, automatic invocation, external adapter, provider/live proof, public-sync, or package conversion |

## 4. Scope

Allowed paths:

- `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md`
- `governance/compat/run_assf_active_resolver.py`
- `governance/compat/test_run_assf_active_resolver.py`
- `docs/baselines/CVF_GC018_ASCP_T1_ACTIVE_RESOLVER_PILOT_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T1_ACTIVE_RESOLVER_PILOT_2026-06-30.md`
- `docs/reviews/CVF_ASCP_T1_ACTIVE_RESOLVER_PILOT_COMPLETION_2026-06-30.md`

Forbidden paths:

- ASSF registry lifecycle sources;
- ASSF package roots;
- external adapter code;
- provider route code;
- session state files unless a later session-sync tranche is opened;
- public-sync repository files.

Risk ceiling: R2 internal governance control.

## Scope / Target / Owner Boundary

Target: bounded activation-readiness resolver for current ASSF runtime packages.

Owner boundary: Codex owns implementation and reviewer closure in this direct
tranche; operator owns future adapter, provider/live, public-sync, package
conversion, and lifecycle-promotion decisions.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`docs/reference/agent_system_skills`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the ADIF resolver was called through Python import because the
module has no CLI `main()` output path.

## 5. Required First Reads

Read before editing:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V28_2026-06-30.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md`
- `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md`
- `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md`
- `governance/compat/run_assf_runtime_package_loader.py`

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF lifecycle includes `ACTIVE` but loading must not imply activation | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields; Provider Adapter Boundary | `ACTIVE`; `adapterContract` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Runtime loader can compute eligibility without instruction bodies | `governance/compat/run_assf_runtime_package_loader.py` | `build_runtime_package_packet` | `include_instruction_bodies` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime eligibility requires certification, UAT, internal implementation, and package root existence | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons` | `certificationState`; `uatState`; `internalAgentDisposition`; `canonicalRoot` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Truth index exposes runtime eligibility and truth receipt hashes | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` | root `entries` | `runtimeEligibility`; `receiptHash` | generated skill truth index | VALUE_SET | ACCEPT |
| Usage receipts are separate from resolver decisions | `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md` | Scope Boundary; Claim Boundary | `skillUsageReceipt` | skill usage receipt standard | LITERAL_INVARIANT | ACCEPT |
| ACTIVE resolver helper is new in ASCP-T1 | `governance/compat/run_assf_active_resolver.py` | ASCP-T1 new file | `build_active_resolver_packet` | active resolver helper | DOC_ONLY_NEW | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF package contract, truth packet standard, usage receipt standard, runtime loader, external adapter boundary, six runtime-eligible package roots |
| Runtime behavior claimed | read-only resolver decision helper |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Open ACTIVE resolver before adapter and package activation | Purpose; Mission | active resolver helper | focused tests and smoke | PASS |
| Keep package body usage separate from selection | Source Verification; Claim Boundary | resolver decision receipt, no usage receipt | unit tests | PASS |
| Defer external CLI/MCP adapter | Dual Agent Surface Matrix | external consumer denied | unit tests | PASS |
| Keep remaining runtime package conversion parked | Scope; Roadmap | ASCP-T5 value-parked | roadmap review | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=c134346e`; `executionBaseHead=c134346e`; `closureBaseHead=c134346e` |
| changedSetScope(phase) | roadmap, helper, tests, baseline, work order, and completion review |
| traceScope(phase, actor) | work-order trace covers direct implementation; completion review trace covers reviewer closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit if committed |
| crossBatchIsolation | no ASSF lifecycle state, package body, adapter, or provider route mutation |
| nextMoveSurfaceHandling | session-sync follows material closure if closure changes next move |
| nextMoveSurfaces | active session state, front door, and handoff |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one read-only active resolver helper
and focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_assf_active_resolver.py`
- `governance/compat/test_run_assf_active_resolver.py`

Operator authorization: the operator approved continuing into ACTIVE resolver,
CLI/MCP adapter, and package activation sequencing.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/agent_system_skills/` and `governance/compat` |
| Storage decision | add local resolver helper; no generated aggregate |
| Stable filename disposition | `governance/compat/run_assf_active_resolver.py` |
| Generated aggregate discipline | N/A with reason: no generated JSON aggregate is added |
| Authority boundary | resolver decisions support readiness only; package sources and truth packets remain authority |
| Forbidden expansion | no lifecycle mutation, adapter, provider/live proof, public export, or package body read |

## 7. Execution Instructions

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | Codex | create |
| `governance/compat/run_assf_active_resolver.py` | Codex | create |
| `governance/compat/test_run_assf_active_resolver.py` | Codex | create |
| ASCP-T1 artifacts | Codex | create |

## Pre-Flight Checks

| Check | Status |
|---|---|
| Startup front door and active handoff read | PASS |
| Guard orientation and literal-format gotchas read | PASS |
| ADIF resolver queried | PASS |
| Runtime package count refreshed | PASS |

## Execution Plan

1. Add active resolver helper using loader eligibility and truth index.
2. Add focused unit tests.
3. Run focused tests and real repo resolver smoke.
4. File completion review and run governance gates.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| Unit tests | `python -m unittest governance.compat.test_run_assf_active_resolver` PASS |
| Resolver smoke | `python governance/compat/run_assf_active_resolver.py --json --max-results 100` reports 32 total and 6 ready |
| Core guard | complete authorization block and PASS |

## Review Gate

Reviewer must confirm resolver decisions, denied external consumer behavior,
no body read, no usage receipt emission, and no adapter or lifecycle claim.

## Closure Checklist

| Item | Status |
|---|---|
| Active resolver helper created | PASS |
| Focused tests created | PASS |
| Unit tests pass | PASS |
| Real repo smoke observes 6 ready packages | PASS |
| Completion review filed | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after focused tests, smoke, and governance
gates pass. Return `BLOCKED` if resolver readiness requires lifecycle mutation
or package body use.

## Operator Checkpoint

No further operator checkpoint is required for ASCP-T1 closure. Future
external adapter implementation, automatic invocation, lifecycle mutation,
provider/live proof, public-sync, or remaining package conversion requires
fresh authorization.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Resolver returns ready only when loader and truth checks pass | unit tests PASS |
| AC2 | Resolver produces decision receipts but no skill usage receipts | unit tests PASS |
| AC3 | External CLI/MCP consumer is denied | unit tests PASS |
| AC4 | Real repo smoke sees 6 ready packages | smoke PASS |
| AC5 | No package lifecycle, provider/live, adapter, public-sync, or production claim is made | claim boundary PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: ASCP-T1 did not consume package instruction output as work evidence |
| Package root | N/A with reason: no package body was requested |
| Invocation context | ASCP-T1 resolver smoke used metadata and truth index only |
| Receipt evidence | N/A with reason: no `skillUsageReceipt` is emitted until the runtime loader explicitly reads an eligible body |
| Output consumed by CVF | resolver decision receipt metadata only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | resolver decision receipt does not grant authority, activate a package, or bypass work-order scope |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | N/A with reason: local Python helper and repo metadata only |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this work order and completion review |
| Authority boundary | provider-owned skill output is not CVF canonical authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | local CVF skill-control implementation -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASCP-T1 roadmap, baseline, work order, completion review, helper, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | ASCP-T1 active resolver pilot on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; resolver smoke |
| Target paths | roadmap, helper, tests, baseline, work order, completion review |
| Allowed scope source | operator approval plus ASCP-T1 baseline and work order |
| Before status evidence | base commit `c134346e`; SKUSE-T1 closed and session-synced |
| After status evidence | active resolver emits readiness decisions for 6 packages |
| Diff evidence | focused tests, resolver smoke, and governance gates |
| Approval boundary | operator approved roadmap sequencing; live API keys not needed because no live behavior claim is made |
| Claim boundary | bounded read-only active resolver only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-ascp-t1-active-resolver-pilot-2026-06-30` |
| Expected manifest | roadmap, helper, tests, baseline, work order, completion review |
| Actual changed set | roadmap, helper, tests, baseline, work order, completion review |
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
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_T1_ACTIVE_RESOLVER_PILOT_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | `Status: ACTIVE_ROADMAP` | PASS |
| Registry JSON | N/A with reason: ASCP-T1 does not mutate registry lifecycle sources | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop runtime loop change in ASCP-T1 | N/A with reason | PASS |
| Session continuity | N/A with reason: material closure does not update session state; session-sync may follow | N/A with reason | PASS |
| Focused tests | active resolver tests | PASS |
| Runtime smoke | active resolver smoke | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Resolver receipt type | `CVF_ASSF_ACTIVE_RESOLVER_DECISION_RECEIPT` | unit test verified receipt type | PASS |
| Ready package count | 6 | smoke observed 6 `ACTIVATION_READY` items | PASS |
| Total generated candidates | 32 | smoke observed 32 total candidates | PASS |
| Unit test status | PASS | `python -m unittest governance.compat.test_run_assf_active_resolver` PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Claim Boundary

ASCP-T1 is a bounded active resolver pilot. It does not activate skills, mutate
package lifecycle state, read package instruction bodies, implement adapters,
call providers, public-sync, or grant action authority.
