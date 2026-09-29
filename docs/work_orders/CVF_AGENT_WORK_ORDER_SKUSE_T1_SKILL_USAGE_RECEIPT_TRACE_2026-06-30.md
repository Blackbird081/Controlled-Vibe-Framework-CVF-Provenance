# CVF Agent Work Order - SKUSE-T1 Skill Usage Receipt Trace

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: SKUSE-T1

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: 6372ea64

executionBaseHead: 6372ea64

closureBaseHead: 6372ea64

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for skill usage receipt trace.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_SKUSE_T1_SKILL_USAGE_RECEIPT_TRACE_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_SKUSE_T1_SKILL_USAGE_RECEIPT_TRACE_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `6372ea64`.

Mission summary: add receipt evidence for explicit eligible ASSF runtime
package body reads and require changed governed artifacts that claim such use
to cite the receipt.

Do-not-misread notes: this work order does not authorize automatic activation,
ACTIVE resolver behavior, external adapters, provider calls, public-sync, or
package lifecycle mutation.

## Purpose

Implement the bounded skill usage receipt trace layer so CVF can inspect
evidence when a CVF-owned ASSF/runtime package body is opened and consumed as
work evidence.

## 1. Mission

Create and verify:

- loader `skillUsageReceipts` for eligible explicit body reads;
- optional `--receipt-out` output;
- stable receipt trace standard;
- markdown receipt trace checker and focused tests;
- governance catalog wiring;
- closure evidence.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat approval on 2026-06-30 to make skill use traceable | authorizes SKUSE-T1 opening |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V28_2026-06-30.md` | active handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_SKUSE_T1_SKILL_USAGE_RECEIPT_TRACE_2026-06-30.md` | scope and claim boundary |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | package field authority |
| SKSOT-T1 truth packet standard | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | truth packet authority |
| Runtime loader | `governance/compat/run_assf_runtime_package_loader.py` | body-read and eligibility behavior |

Authority boundary: SKUSE-T1 may add receipt evidence and a trace checker. It
may not mutate package lifecycle state or activate packages.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | update loader, standard, checker, tests, and hooks |
| Reviewer/closer | Codex | verify checks and completion review |
| Operator approval required | operator | future ACTIVE resolver, external adapter, provider/live proof, public-sync, or package promotion |

## 4. Scope

Allowed paths:

- `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md`
- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/test_run_assf_runtime_package_loader.py`
- `governance/compat/check_cvf_skill_usage_receipt_trace.py`
- `governance/compat/test_check_cvf_skill_usage_receipt_trace.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `docs/baselines/CVF_GC018_SKUSE_T1_SKILL_USAGE_RECEIPT_TRACE_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_SKUSE_T1_SKILL_USAGE_RECEIPT_TRACE_2026-06-30.md`
- `docs/reviews/CVF_SKUSE_T1_SKILL_USAGE_RECEIPT_TRACE_COMPLETION_2026-06-30.md`

Forbidden paths:

- ASSF registry entries;
- ASSF package roots;
- resolver activation code;
- external adapter code;
- session state files unless a later session-sync tranche is opened;
- public-sync repository files.

Risk ceiling: R2 internal governance control.

## Scope / Target / Owner Boundary

Target: bounded usage receipt traceability for explicit eligible ASSF runtime
package body reads.

Owner boundary: Codex owns implementation and reviewer closure in this direct
tranche; operator owns future resolver, adapter, provider/live, public-sync, or
package promotion decisions.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`docs/reference/agent_system_skills`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the read-only ADIF resolver returned no matching defects for
this implementation query.

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
- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/check_external_provider_skill_usage_trace.py`

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF package lifecycle fields include status, UAT, certification, and internal/external dispositions | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema; Internal-Agent And External-Agent CLI/MCP Disposition Fields | `status`; `uatState`; `certificationState`; `internalAgentDisposition`; `externalCliMcpDisposition` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Runtime loader opens package body only when explicitly requested and eligible | `governance/compat/run_assf_runtime_package_loader.py` | module docstring; `build_runtime_package_packet` | `include_instruction_bodies`; `packageBodyDisposition` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime eligibility requires certified, UAT-passed, implemented internal disposition, and package root existence | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons` | `certificationState`; `uatState`; `internalAgentDisposition`; `canonicalRoot` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Skill truth packets define source records for evidence, obligations, verification results, and truth receipts | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | Source Authority Boundary | `truth/packets/*.json` | SKSOT-T1 truth packet standard | LITERAL_INVARIANT | ACCEPT |
| CVF skill usage receipt trace checker is new in this tranche | `governance/compat/check_cvf_skill_usage_receipt_trace.py` | SKUSE-T1 new file | `check_text`; `validate_trace_section` | SKUSE-T1 checker | DOC_ONLY_NEW | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF package contract, SKSOT-T1 standard, runtime loader, provider-skill trace checker pattern, six runtime-eligible package roots |
| Runtime behavior claimed | read-only receipt emission and markdown trace checking |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Operator requested traceability when agents use skills | Purpose; Mission | receipt trace standard and checker | completion review | PASS |
| SKSOT-T1 created truth packets but not invocation receipts | Source Verification | loader `skillUsageReceipts` | loader tests and smoke | PASS |
| Provider-owned skills must remain separate from CVF-owned skills | Authority Chain; Claim Boundary | separate CVF receipt trace checker | provider trace checker remains unchanged | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=6372ea64`; `executionBaseHead=6372ea64`; `closureBaseHead=6372ea64` |
| changedSetScope(phase) | standard, loader, checker, tests, catalogs, and closure artifacts |
| traceScope(phase, actor) | work-order trace covers direct implementation; completion review trace covers reviewer closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit if committed |
| crossBatchIsolation | no ASSF lifecycle state or package body mutation in SKUSE-T1 |
| nextMoveSurfaceHandling | session-sync follows material closure if closure changes next move |
| nextMoveSurfaces | active session state, front door, and handoff |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update the bounded ASSF runtime package
loader to emit read receipts for eligible body reads, add one read-only receipt
trace checker, add focused tests, and wire the checker into governed local
workflow catalogs.

Protected paths:

- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/check_cvf_skill_usage_receipt_trace.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/test_check_cvf_skill_usage_receipt_trace.py`
- `governance/compat/test_run_assf_runtime_package_loader.py`

Operator authorization: the operator agreed to make skill use leave traceable
evidence after SKSOT-T1 established skill truth packets.

Rollback boundary: if SKUSE-T1 is rejected, remove only the receipt changes,
new checker, tests, hook-catalog entries, SKUSE-T1 standard, and SKUSE-T1
artifacts. Do not revert prior SKSOT-T1, EPSOT-T1, AGSK-R7, or session-sync
commits unless a reviewer separately reopens those closures.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/agent_system_skills/` |
| Storage decision | add stable receipt trace standard; no generated aggregate |
| Stable filename disposition | `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md` |
| Generated aggregate discipline | N/A with reason: no generated JSON aggregate is added |
| Authority boundary | receipt evidence supports a use claim; it does not replace source authority |
| Forbidden expansion | no ACTIVE resolver, adapter, package promotion, provider/live proof, or public export |

## 7. Execution Instructions

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reference/agent_system_skills/CVF_SKILL_USAGE_RECEIPT_TRACE_STANDARD.md` | Codex | create |
| `governance/compat/run_assf_runtime_package_loader.py` | Codex | update |
| `governance/compat/test_run_assf_runtime_package_loader.py` | Codex | update |
| `governance/compat/check_cvf_skill_usage_receipt_trace.py` | Codex | create |
| `governance/compat/test_check_cvf_skill_usage_receipt_trace.py` | Codex | create |
| governance hook catalogs | Codex | update |
| SKUSE-T1 artifacts | Codex | create |

## Pre-Flight Checks

| Check | Status |
|---|---|
| Startup front door and active handoff read | PASS |
| Guard orientation and literal-format gotchas read | PASS |
| ADIF resolver queried | PASS |
| Runtime eligibility audit refreshed | PASS |

## Execution Plan

1. Add deterministic loader receipt construction for loaded eligible packages.
2. Add optional receipt bundle output.
3. Add the stable receipt trace standard.
4. Add `check_cvf_skill_usage_receipt_trace.py` and unit tests.
5. Wire the checker into reviewer-fast, pre-commit, and autorun catalogs.
6. Run focused verification and close with completion review.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| Unit tests | `python -m unittest governance.compat.test_run_assf_runtime_package_loader governance.compat.test_check_cvf_skill_usage_receipt_trace` PASS |
| Receipt trace checker | `python governance/compat/check_cvf_skill_usage_receipt_trace.py --base 6372ea64 --head HEAD --enforce` PASS |
| Loader smoke | real eligible package emits `CVF_ASSF_SKILL_USAGE_RECEIPT` |
| Core guard | complete authorization block and PASS |

## Review Gate

Reviewer must confirm receipt emission, denied-package non-emission, trace
checker behavior, hook wiring, and no package activation claim.

## Closure Checklist

| Item | Status |
|---|---|
| Receipt standard created | PASS |
| Loader receipt implemented | PASS |
| Optional receipt output implemented | PASS |
| Checker and tests created | PASS |
| Hook catalogs wired | PASS |
| Completion review filed | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after focused tests, receipt smoke, and
checker pass. Return `BLOCKED` if receipt evidence requires package activation
or lifecycle mutation.

## Operator Checkpoint

No further operator checkpoint is required for SKUSE-T1 closure. Future ACTIVE
resolver, automatic invocation, external adapter, provider/live proof,
public-sync, or package promotion requires fresh operator approval.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Loader emits receipt for eligible loaded package bodies | unit tests and smoke PASS |
| AC2 | Loader emits no receipt for metadata-only or denied packages | unit tests PASS |
| AC3 | Stable receipt trace standard exists | file created |
| AC4 | Checker unit tests cover missing trace, disposition, receipt evidence, and complete trace | unittest PASS |
| AC5 | Governance catalogs run the checker | catalog entries present |
| AC6 | No package lifecycle, ACTIVE resolver, provider/live, adapter, public-sync, or production claim is made | claim boundary PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | USED_WITH_RECEIPT |
| CVF skill id | cvf-engineering-code-review-quality |
| Package root | docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md |
| Invocation context | SKUSE-T1 real loader smoke for receipt emission verification |
| Receipt evidence | skillUsageReceipt receiptId sha256:1c50b864577052203b184e414b75f1ed21b8868caab05624f81291e74a2439e4 |
| Output consumed by CVF | receipt metadata only; package instructions were not used as task authority |
| Truth packet or source path | docs/reference/agent_system_skills/truth/packets/cvf-engineering-code-review-quality.json |
| Authority boundary | receipt proves body read only and does not grant authority, activate a package, or bypass work-order scope |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed as CVF evidence |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | N/A with reason: local file and checker work only |
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
| Owner surface | SKUSE-T1 baseline, work order, completion review, receipt trace standard, loader, checker, and tests |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | no external source, provider output, or provider-local memory is promoted as CVF authority in SKUSE-T1 |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | SKUSE-T1 skill usage receipt trace on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python checker; unittest; runtime loader smoke |
| Target paths | receipt trace standard, loader, checker, tests, governance catalogs, SKUSE-T1 artifacts |
| Allowed scope source | operator approval plus SKUSE-T1 baseline and work order |
| Before status evidence | base commit `6372ea64`; SKSOT-T1 had six truth packets |
| After status evidence | loader emits receipt and checker validates trace blocks |
| Diff evidence | receipt trace checker, unit tests, loader smoke, and governance gates |
| Approval boundary | operator approved skill-use evidence traceability; live API keys not needed because no live behavior claim is made |
| Claim boundary | bounded read-only skill usage receipt trace only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-skuse-t1-skill-usage-receipt-trace-2026-06-30` |
| Expected manifest | standard, loader, checker, tests, catalogs, baseline, work order, completion review |
| Actual changed set | standard, loader, checker, tests, catalogs, baseline, work order, completion review |
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
| Completion or reviewer artifact | `docs/reviews/CVF_SKUSE_T1_SKILL_USAGE_RECEIPT_TRACE_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: operator-directed skill control-plane tranche, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | N/A with reason: SKUSE-T1 does not mutate ASSF registry lifecycle sources | N/A with reason | PASS |
| Registry Markdown | receipt trace standard | created | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop runtime loop change in SKUSE-T1 | N/A with reason | PASS |
| Session continuity | N/A with reason: material closure does not update session state; session-sync may follow | N/A with reason | PASS |
| Focused tests | loader and receipt trace tests | PASS |
| Runtime smoke | real loader receipt smoke | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Receipt type | `CVF_ASSF_SKILL_USAGE_RECEIPT` | real loader smoke emitted receipt | PASS |
| Receipt ID | `sha256:` value | `sha256:1c50b864577052203b184e414b75f1ed21b8868caab05624f81291e74a2439e4` | PASS |
| Checker status | PASS | `check_cvf_skill_usage_receipt_trace.py --base 6372ea64 --head HEAD --enforce` PASS | PASS |
| Unit test status | PASS | `python -m unittest governance.compat.test_run_assf_runtime_package_loader governance.compat.test_check_cvf_skill_usage_receipt_trace` PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Claim Boundary

SKUSE-T1 is a bounded skill usage receipt trace tranche. It does not activate
skills, mutate package lifecycle state, implement adapters, call providers,
public-sync, or grant action authority.
