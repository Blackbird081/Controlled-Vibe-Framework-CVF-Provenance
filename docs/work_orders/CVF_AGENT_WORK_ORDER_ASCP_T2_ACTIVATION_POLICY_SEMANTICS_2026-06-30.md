# CVF Agent Work Order - ASCP-T2 Activation Policy Semantics

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: ASCP-T2

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: 76f632ff

executionBaseHead: 76f632ff

closureBaseHead: 76f632ff

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for ASSF activation policy
semantics.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `76f632ff`.

Mission summary: define and implement policy semantics for selected, ready,
body-read requested, and used-with-receipt before ASCP-T3 adapter work.

Do-not-misread notes: this work order does not authorize package lifecycle
mutation, automatic invocation, package body reads by the policy helper,
external adapters, provider calls, public-sync, or remaining package runtime
conversion.

## Purpose

Implement the ASCP-T2 policy layer so future adapter and activation work can
inspect the difference between selection, activation readiness, body-read
request, and receipt-backed output use.

## 1. Mission

Create and verify:

- activation policy semantics standard;
- activation policy resolver helper;
- focused policy tests;
- roadmap update from ASCP-T2 ready to closed and ASCP-T3 ready;
- baseline, work order, and completion evidence.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat approval on 2026-06-30 for next move after ASCP-T1 and ADIF-CLI-T1 | authorizes ASCP-T2 execution |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V28_2026-06-30.md` | active handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md` | scope and claim boundary |
| ASCP roadmap | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | T2 objective and T3 dependency |
| Active resolver | `governance/compat/run_assf_active_resolver.py` | readiness behavior |
| Runtime loader | `governance/compat/run_assf_runtime_package_loader.py` | body read and usage receipt behavior |

Authority boundary: ASCP-T2 may classify activation policy states. It may not
read package instruction bodies, emit usage receipts, implement adapters, or
mutate lifecycle sources.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | add policy standard, helper, tests, and roadmap update |
| Reviewer/closer | Codex | verify tests, smokes, and completion review |
| Operator approval required | operator | future adapter behavior, lifecycle mutation, provider/live proof, public-sync, or package conversion |

## 4. Scope

Allowed paths:

- `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md`
- `governance/compat/run_assf_activation_policy_resolver.py`
- `governance/compat/test_run_assf_activation_policy_resolver.py`
- `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md`
- `docs/baselines/CVF_GC018_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md`
- `docs/reviews/CVF_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_COMPLETION_2026-06-30.md`

Forbidden paths:

- ASSF registry lifecycle sources;
- ASSF package roots;
- external adapter code;
- provider route code;
- session state files unless a later session-sync tranche is opened;
- public-sync repository files.

Risk ceiling: R2 internal governance control.

## Scope / Target / Owner Boundary

Target: bounded activation policy semantics for ASSF runtime package control.

Owner boundary: Codex owns implementation and reviewer closure in this direct
tranche; operator owns future adapter, provider/live, public-sync, package
conversion, and lifecycle-promotion decisions.

## Allowed / Forbidden Scope

Allowed:

- `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md`
- `governance/compat/run_assf_activation_policy_resolver.py`
- `governance/compat/test_run_assf_activation_policy_resolver.py`
- `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md`
- `docs/baselines/CVF_GC018_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_2026-06-30.md`
- `docs/reviews/CVF_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_COMPLETION_2026-06-30.md`

Forbidden:

- package lifecycle source mutation;
- package instruction body reads by the policy helper;
- skill usage receipt emission by the policy helper;
- external CLI/MCP adapter implementation;
- provider/live proof;
- public-sync;
- remaining package conversion.

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
- `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md`
- `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md`
- `governance/compat/run_assf_active_resolver.py`
- `governance/compat/run_assf_runtime_package_loader.py`

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASCP roadmap requires T2 activation policy semantics before adapter work | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | Work Plan | `ASCP-T2`; `ASCP-T3` | ASCP roadmap | VALUE_SET | ACCEPT |
| Active resolver returns readiness decisions and loader command hints | `governance/compat/run_assf_active_resolver.py` | `ActiveResolverItem.to_dict`; `_loader_command` | `activationDecision`; `loaderCommand` | active resolver helper | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime loader owns body reads and usage receipts | `governance/compat/run_assf_runtime_package_loader.py` | `build_runtime_package_packet`; `_build_skill_usage_receipt` | `include_instruction_bodies`; `skillUsageReceipts` | runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Usage receipt standard defines consumed package-output trace | `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md` | Governed Artifact Trace Requirement | `USED_WITH_RECEIPT` | skill usage receipt trace standard | LITERAL_INVARIANT | ACCEPT |
| External adapter remains deferred | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | Adapter Admission Boundary | `EXTERNAL_AGENT_CLI_MCP` | external readout boundary contract | LITERAL_INVARIANT | ACCEPT |
| Activation policy resolver helper is new in ASCP-T2 | `governance/compat/run_assf_activation_policy_resolver.py` | ASCP-T2 new file | `build_activation_policy_packet` | activation policy resolver | DOC_ONLY_NEW | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Define selected, ready, body-read requested, and used-with-receipt | Purpose; Mission | policy standard and helper states | focused tests | PASS |
| Preserve receipt-backed use requirement | Source Verification; Acceptance Criteria | `USED_WITHOUT_RECEIPT_DENIED` and `USED_WITH_RECEIPT` | unit tests | PASS |
| Defer external CLI/MCP adapter until after T2 | Scope; Dual Agent Surface Matrix | ASCP-T3 ready after T2 | roadmap update | PASS |
| Keep lifecycle activation separate | Claim Boundary | no registry or package root mutation | changed set review | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=76f632ff`; `executionBaseHead=76f632ff`; `closureBaseHead=76f632ff` |
| changedSetScope(phase) | policy standard, helper, tests, roadmap update, baseline, work order, and completion review |
| traceScope(phase, actor) | work-order trace covers implementation; completion review trace covers closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit if committed |
| crossBatchIsolation | no ASSF lifecycle state, package body, adapter, or provider route mutation |
| nextMoveSurfaceHandling | session-sync follows material closure |
| nextMoveSurfaces | active session state, front door, and handoff |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one bounded activation policy helper
and focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_assf_activation_policy_resolver.py`
- `governance/compat/test_run_assf_activation_policy_resolver.py`

Operator authorization: active next move authorizes ASCP-T2 before CLI/MCP
adapter implementation.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASCP roadmap, active resolver, runtime loader, usage receipt standard, external adapter boundary |
| Runtime behavior claimed | local activation policy classification only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support policy classification, not activation or adapter behavior |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/agent_system_skills/` and `governance/compat` |
| Storage decision | add local policy helper and reference standard, not a generated aggregate |
| Stable filename disposition | `governance/compat/run_assf_activation_policy_resolver.py` |
| Generated aggregate discipline | N/A with reason: no generated JSON aggregate is added |
| Authority boundary | policy decisions classify evidence only; work order, package sources, and receipts remain authority |
| Forbidden expansion | no lifecycle mutation, adapter, provider/live proof, public export, package body read, or usage receipt emission |

## 7. Execution Instructions

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| policy standard | Codex | create |
| policy helper and tests | Codex | create |
| ASCP roadmap | Codex | update T2/T3 rows only |
| ASCP-T2 artifacts | Codex | create |

## Pre-Flight Checks

| Check | Status |
|---|---|
| Startup front door and active handoff read | PASS |
| Guard orientation and literal-format gotchas read | PASS |
| ADIF resolver queried | PASS |
| ASCP-T1 active resolver and runtime loader read | PASS |

## Execution Plan

1. Add activation policy semantics standard.
2. Add activation policy resolver helper and focused tests.
3. Run focused tests and policy smokes.
4. Update roadmap T2/T3 state and file completion review.
5. Run governance gates and commit.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| Unit tests | `python -m unittest governance.compat.test_run_assf_activation_policy_resolver` PASS |
| Ready smoke | policy resolver returns `ACTIVATION_READY` for a current ready package |
| Body-read request smoke | policy resolver returns `BODY_READ_REQUESTED` without opening a body |
| Changed set review | no package roots, lifecycle registry, adapter, provider, or public-sync mutation |

## Review Gate

Reviewer must confirm policy states, no package body read in policy helper, no
usage receipt emission by policy helper, no external adapter, and no lifecycle
mutation.

## Closure Checklist

| Item | Status |
|---|---|
| Policy standard created | PASS |
| Policy helper created | PASS |
| Focused tests created | PASS |
| Unit tests pass | PASS |
| Policy smokes pass | PASS |
| Roadmap update filed | PASS |
| Completion review filed | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after focused tests, smokes, and governance
gates pass. Return `BLOCKED` if policy semantics require lifecycle mutation,
package body reads by the policy helper, or adapter implementation.

## Operator Checkpoint

No further operator checkpoint is required for ASCP-T2 closure. Future external
adapter implementation, automatic invocation, lifecycle mutation, provider/live
proof, public-sync, or remaining package conversion requires fresh
authorization.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Policy states distinguish selected, ready, body-read requested, and used-with-receipt | unit tests PASS |
| AC2 | Consumed output without matching receipt is denied | unit tests PASS |
| AC3 | Policy helper does not open package bodies or emit usage receipts | source and tests PASS |
| AC4 | External consumer remains not activation-ready until adapter work | unit tests PASS |
| AC5 | ASCP-T3 is the next allowed implementation lane | roadmap and session-sync after closure |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: ASCP-T2 did not consume package instruction output as work evidence |
| Package root | N/A with reason: no package body was read by ASCP-T2 policy helper |
| Invocation context | ASCP-T2 local tests and smokes |
| Receipt evidence | N/A with reason: no loader usage receipt output was consumed as evidence |
| Output consumed by CVF | local policy resolver output only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | policy receipts do not grant authority, activate packages, or bypass work-order scope |

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

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | ASCP-T2 activation policy semantics on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; policy resolver smokes; governance gates |
| Target paths | policy standard, helper, tests, roadmap, baseline, work order, completion review |
| Allowed scope source | active next move plus this work order and paired baseline |
| Before status evidence | base commit `76f632ff`; clean worktree before ASCP-T2 edits |
| After status evidence | policy helper and closure artifacts prepared for material commit |
| Diff evidence | focused tests, policy smokes, and governance gates |
| Approval boundary | active next move authorized ASCP-T2; live API keys not needed because no live behavior claim is made |
| Claim boundary | bounded local policy classification only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-ascp-t2-activation-policy-semantics-2026-06-30` |
| Expected manifest | standard, helper, tests, roadmap update, baseline, work order, completion review |
| Actual changed set | standard, helper, tests, roadmap update, baseline, work order, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local CVF skill-control implementation -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASCP-T2 roadmap, baseline, work order, completion review, policy standard, helper, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references internal ASSF governance and private
provenance surfaces. Public-safe export requires separate public-sync
authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_T2_ACTIVATION_POLICY_SEMANTICS_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | `Status: ACTIVE_ROADMAP` | PASS |
| Registry JSON | N/A with reason: no registry mutation authorized or performed | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no provider route, adapter, or package execution changed | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | activation policy tests | PASS | PASS |
| Runtime smoke | activation policy resolver smokes | PASS | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Policy receipt type | `CVF_ASSF_ACTIVATION_POLICY_DECISION_RECEIPT` | helper emits policy decision receipts | PASS |
| Ready smoke state | `ACTIVATION_READY` | smoke returned `ACTIVATION_READY` | PASS |
| Body-read request state | `BODY_READ_REQUESTED` | smoke returned `BODY_READ_REQUESTED` | PASS |
| Unit test status | PASS | `python -m unittest governance.compat.test_run_assf_activation_policy_resolver` PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Claim Boundary

ASCP-T2 is a bounded activation policy semantics tranche. It does not activate
skills, mutate package lifecycle state, read package instruction bodies,
implement adapters, call providers, public-sync, or grant action authority.
