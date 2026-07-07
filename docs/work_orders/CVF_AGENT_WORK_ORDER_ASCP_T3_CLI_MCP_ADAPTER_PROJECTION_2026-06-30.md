# CVF Agent Work Order - ASCP-T3 CLI/MCP Adapter Projection

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: ASCP-T3

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: fe2f6205

executionBaseHead: fe2f6205

closureBaseHead: fe2f6205

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for ASSF CLI/MCP adapter
projection.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `fe2f6205`.

Mission summary: implement a bounded external projection helper that exposes
allowlisted metadata and activation policy state while denying package body
reads, output use, provider calls, and lifecycle mutation.

Do-not-misread notes: this work order does not authorize package lifecycle
mutation, package body reads, skill usage receipt emission or consumption,
provider calls, MCP server behavior, public-sync, or remaining package runtime
conversion.

## Purpose

Implement ASCP-T3 so external CLI/MCP consumers can inspect safe ASSF package
metadata and readiness state without gaining package execution authority.

## 1. Mission

Create and verify:

- CLI/MCP adapter projection standard;
- projection helper;
- focused projection tests;
- roadmap update from ASCP-T3 ready to closed and ASCP-T4 ready;
- baseline, work order, and completion evidence.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat approval on 2026-06-30 for ASCP next move | authorizes ASCP-T3 execution |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V28_2026-06-30.md` | active handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md` | scope and claim boundary |
| ASCP roadmap | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | T3 objective and T4 dependency |
| External readout boundary contract | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | allowlist and adapter boundary |
| Activation policy resolver | `governance/compat/run_assf_activation_policy_resolver.py` | policy state source |

Authority boundary: ASCP-T3 may project allowlisted metadata and policy state.
It may not read package instruction bodies, emit or consume usage receipts,
call providers, implement execution adapters, or mutate lifecycle sources.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | add projection standard, helper, tests, and roadmap update |
| Reviewer/closer | Codex | verify tests, smoke, and completion review |
| Operator approval required | operator | package execution adapter, provider/live proof, public-sync, package conversion, or lifecycle promotion |

## 4. Scope

Allowed paths:

- `docs/reference/agent_system_skills/CVF_ASSF_CLI_MCP_ADAPTER_PROJECTION_STANDARD.md`
- `governance/compat/run_assf_cli_mcp_adapter_projection.py`
- `governance/compat/test_run_assf_cli_mcp_adapter_projection.py`
- `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md`
- `docs/baselines/CVF_GC018_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md`
- `docs/reviews/CVF_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_COMPLETION_2026-06-30.md`

Forbidden paths:

- ASSF registry lifecycle sources;
- ASSF package roots;
- provider route code;
- MCP server, daemon, hook, or IDE bridge implementation;
- session state files unless a later session-sync tranche is opened;
- public-sync repository files.

Risk ceiling: R2 internal governance control.

## Scope / Target / Owner Boundary

Target: bounded external metadata and policy-state projection for ASSF package
control.

Owner boundary: Codex owns implementation and reviewer closure in this direct
tranche; operator owns future provider/live, public-sync, package conversion,
execution adapter, and lifecycle-promotion decisions.

## Allowed / Forbidden Scope

Allowed:

- `docs/reference/agent_system_skills/CVF_ASSF_CLI_MCP_ADAPTER_PROJECTION_STANDARD.md`
- `governance/compat/run_assf_cli_mcp_adapter_projection.py`
- `governance/compat/test_run_assf_cli_mcp_adapter_projection.py`
- `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md`
- `docs/baselines/CVF_GC018_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_2026-06-30.md`
- `docs/reviews/CVF_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_COMPLETION_2026-06-30.md`

Forbidden:

- package lifecycle source mutation;
- package instruction body reads;
- skill usage receipt emission or consumption;
- provider/live proof;
- MCP server runtime, daemon, hook, or IDE bridge behavior;
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
- `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md`
- `governance/compat/run_assf_external_agent_metadata_readout.py`
- `governance/compat/run_assf_activation_policy_resolver.py`
- `governance/compat/run_assf_active_resolver.py`

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASCP roadmap requires T3 CLI/MCP adapter projection after T2 closure | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | Work Plan | `ASCP-T3` | ASCP roadmap | VALUE_SET | ACCEPT |
| External metadata readout helper exposes only allowlisted metadata families | `governance/compat/run_assf_external_agent_metadata_readout.py` | `ALLOWED_SKILL_FIELDS`; `build_metadata_readout` | `ALLOWED_SKILL_FIELDS` | external metadata readout helper | RUNTIME_BEHAVIOR | ACCEPT |
| External readout contract denies adapter execution before separate evidence | `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | Adapter Admission Boundary | `EXTERNAL_AGENT_CLI_MCP` | external readout boundary contract | LITERAL_INVARIANT | ACCEPT |
| Activation policy resolver classifies readiness without body reads | `governance/compat/run_assf_activation_policy_resolver.py` | `build_activation_policy_packet` | `body_read_requested` | activation policy resolver | RUNTIME_BEHAVIOR | ACCEPT |
| CLI/MCP projection helper is new in ASCP-T3 | `governance/compat/run_assf_cli_mcp_adapter_projection.py` | ASCP-T3 new file | `build_cli_mcp_adapter_projection` | CLI/MCP adapter projection helper | DOC_ONLY_NEW | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Implement CLI/MCP adapter projection after T2 | Purpose; Mission | projection standard and helper | focused tests | PASS |
| Use external readout allowlist | Source Verification; Acceptance Criteria | allowlisted metadata families | unit tests | PASS |
| Use resolver output without body reads | Source Verification; Evidence Requirements | `activationPolicyState` | unit tests and smoke | PASS |
| Keep lifecycle activation separate | Claim Boundary | no registry or package root mutation | changed set review | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=fe2f6205`; `executionBaseHead=fe2f6205`; `closureBaseHead=fe2f6205` |
| changedSetScope(phase) | projection standard, helper, tests, roadmap update, baseline, work order, and completion review |
| traceScope(phase, actor) | work-order trace covers implementation; completion review trace covers closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit if committed |
| crossBatchIsolation | no ASSF lifecycle state, package body, provider route, execution adapter, or public-sync mutation |
| nextMoveSurfaceHandling | session-sync follows material closure |
| nextMoveSurfaces | active session state, front door, and handoff |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one bounded CLI/MCP projection helper
and focused tests under `governance/compat`.

Protected paths:

- `governance/compat/run_assf_cli_mcp_adapter_projection.py`
- `governance/compat/test_run_assf_cli_mcp_adapter_projection.py`

Operator authorization: active next move authorizes ASCP-T3 after ASCP-T2
closure.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASCP roadmap, external readout helper, activation policy resolver, external adapter boundary |
| Runtime behavior claimed | local external metadata/policy projection only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current sources support projection, not package execution |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/agent_system_skills/` and `governance/compat` |
| Storage decision | add local projection helper and reference standard, not a generated aggregate |
| Stable filename disposition | `governance/compat/run_assf_cli_mcp_adapter_projection.py` |
| Generated aggregate discipline | N/A with reason: no generated JSON aggregate is added |
| Authority boundary | projection decisions are readout evidence only; work order, package sources, and receipts remain authority |
| Forbidden expansion | no lifecycle mutation, package body read, usage receipt, provider/live proof, public export, or execution adapter |

## 7. Execution Instructions

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| projection standard | Codex | create |
| projection helper and tests | Codex | create |
| ASCP roadmap | Codex | update T3/T4 rows only |
| ASCP-T3 artifacts | Codex | create |

## Pre-Flight Checks

| Check | Status |
|---|---|
| Startup front door and active handoff read | PASS |
| Guard orientation and literal-format gotchas read | PASS |
| ADIF resolver queried | PASS |
| External readout and activation policy helpers read | PASS |

## Execution Plan

1. Add CLI/MCP adapter projection standard.
2. Add projection helper and focused tests.
3. Run focused tests and projection smoke.
4. Update roadmap T3/T4 state and file completion review.
5. Run governance gates and commit.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| Unit tests | `python -m unittest governance.compat.test_run_assf_cli_mcp_adapter_projection` PASS |
| Projection smoke | projection returns `ACTIVATION_READY` for a current ready package while external body/read output remains denied |
| Changed set review | no package roots, lifecycle registry, provider, execution adapter, or public-sync mutation |

## Review Gate

Reviewer must confirm metadata allowlist, policy state projection, no package
body read, no usage receipt emission or consumption, no provider route, no MCP
server behavior, and no lifecycle mutation.

## Closure Checklist

| Item | Status |
|---|---|
| Projection standard created | PASS |
| Projection helper created | PASS |
| Focused tests created | PASS |
| Unit tests pass | PASS |
| Projection smoke passes | PASS |
| Roadmap update filed | PASS |
| Completion review filed | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after focused tests, smoke, and governance
gates pass. Return `BLOCKED` if projection semantics require package body
reads, usage receipt mutation, provider calls, lifecycle mutation, or execution
adapter behavior.

## Operator Checkpoint

No further operator checkpoint is required for ASCP-T3 closure. Future package
execution adapter behavior, automatic invocation, lifecycle mutation,
provider/live proof, public-sync, or remaining package conversion requires
fresh authorization.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Projection emits allowlisted metadata families | unit tests PASS |
| AC2 | Projection emits activation policy state without internal receipts | unit tests PASS |
| AC3 | External package body reads and output use remain denied | unit tests and smoke PASS |
| AC4 | Projection does not emit body, loader command, truth, resolver receipt, policy receipt, or skill usage receipt fields | unit tests PASS |
| AC5 | ASCP-T4 is the next allowed implementation lane | roadmap and session-sync after closure |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: ASCP-T3 did not consume package instruction output as work evidence |
| Package root | N/A with reason: no package body was read by ASCP-T3 projection helper |
| Invocation context | ASCP-T3 projection tests and smoke |
| Receipt evidence | N/A with reason: no loader usage receipt output was consumed as evidence |
| Output consumed by CVF | local metadata/policy projection output only |
| Truth packet or source path | `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` |
| Authority boundary | projection output does not grant authority, activate packages, or bypass work-order scope |

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
| Owner surface | ASCP-T3 roadmap, baseline, work order, completion review, projection standard, helper, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | ASCP-T3 CLI/MCP adapter projection on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; projection smoke |
| Target paths | projection standard, helper, tests, roadmap, baseline, work order, completion review |
| Allowed scope source | active next move plus ASCP-T3 baseline and work order |
| Before status evidence | base commit `fe2f6205`; clean worktree before ASCP-T3 edits |
| After status evidence | pending material closure changed set |
| Diff evidence | focused tests, projection smoke, and governance gates |
| Approval boundary | active next move authorized ASCP-T3; live API keys not needed because no live behavior claim is made |
| Claim boundary | bounded external metadata and policy readout only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-ascp-t3-cli-mcp-adapter-projection-2026-06-30` |
| Expected manifest | standard, helper, tests, roadmap update, baseline, work order, completion review |
| Actual changed set | standard, helper, tests, roadmap update, baseline, work order, completion review |
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
| Completion or reviewer artifact | `docs/reviews/CVF_ASCP_T3_CLI_MCP_ADAPTER_PROJECTION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_ACTIVE_RESOLVER_AND_ADAPTER_PILOT_ROADMAP_2026-06-30.md` | `Status: ACTIVE_ROADMAP` | PASS |
| Registry JSON | N/A with reason: no registry mutation authorized or performed | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no provider route, execution adapter, or package execution changed | N/A with reason | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | projection tests | PASS | PASS |
| Runtime smoke | projection smoke | PASS | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Projection implementation | `IMPLEMENTED_BOUNDED_PROJECTION` | helper emits projection implementation token | PASS |
| External consumer | `EXTERNAL_AGENT_CLI_MCP` | helper emits external consumer token | PASS |
| Body-read disposition | `DENIED_EXTERNAL_BODY_READ_NOT_IMPLEMENTED` | unit tests and smoke observed denial | PASS |
| Output-use disposition | `DENIED_EXTERNAL_OUTPUT_USE_NOT_IMPLEMENTED` | unit tests observed denial | PASS |
| Unit test status | PASS | `python -m unittest governance.compat.test_run_assf_cli_mcp_adapter_projection` PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Claim Boundary

ASCP-T3 implements bounded external metadata and activation policy projection
only. It does not activate skills, mutate package lifecycle state, read package
instruction bodies, emit or consume skill usage receipts, implement package
execution adapters, call providers, public-sync, or grant action authority.
