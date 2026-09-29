# CVF Agent Work Order EPSOT-T1 Provider Skill Trace Source Of Truth

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

dispatchBaseHead: `09a753ea`

executionBaseHead: `09a753ea`

closureBaseHead: `09a753ea`

routeToken: `WORKER_MAY_COMMIT`

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for EPSOT-T1 source-of-truth trace
guard.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`.

Commit mode: `WORKER_MAY_COMMIT`.

Base: `09a753ea`.

## Purpose

Implement the bounded EPSOT-T1 source-of-truth trace guard for provider-owned
external skill output consumption claims.

## 0. Surface Fidelity Gate

This work order authorizes a single-agent, local-governance implementation
tranche for provider-owned external skill traceability. It does not authorize
provider runtime control, package activation, public sync, live provider proof,
or UI work.

## 1. Authority Chain

| Authority | Evidence |
|---|---|
| Operator instruction | Build a source-of-truth mechanism so provider-owned external skill surfaces leave trace evidence in CVF. |
| Repository front door | `AGENTS.md` canonical authority for external provider memory-boundary and live proof rules |
| Guard orientation | `docs/reference/guard_orientation/README.md` read before governed artifact authoring |
| Literal gotchas | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` read before artifact authoring |
| GC-018 baseline | `docs/baselines/CVF_GC018_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md` |

## 2. Transfer Objective

Implement a bounded source-of-truth trace lane for external provider skill
consumption claims:

- create the standard;
- create the checker and regression tests;
- wire the checker into reviewer-fast, pre-commit, and autorun catalogs;
- close with focused local evidence.

## 3. Source Packet

| Source | Purpose |
|---|---|
| `governance/compat/check_memory_access_claim.py` | analogous changed-Markdown checker structure |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | reviewer-fast catalog insertion point |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | pre-commit catalog insertion point |
| `governance/compat/agent_autorun_command_catalog.py` | autorun catalog insertion point |
| `docs/reference/CVF_EXTERNAL_PROVIDER_SKILL_SOURCE_OF_TRUTH_STANDARD_2026-06-30.md` | new standard |

## 4. Role Assignment

| Role | Assignment |
|---|---|
| Implementer | Codex |
| Reviewer/closer | Codex in same governed single-agent tranche |
| Commit owner | Codex |
| Public-sync owner | N/A with reason: no public-sync authorized |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | implement checker, tests, standard, and catalog wiring |
| Reviewer/closer | Codex | run gates, close review, and commit material |
| Operator approval required | operator | any runtime adapter, ACTIVE resolver, live proof, public-sync, or provider-side audit work |

## Required First Reads

Read before editing:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V28_2026-06-30.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`
- this work order
- `governance/compat/check_memory_access_claim.py`
- governance hook catalogs named in allowed scope

## 5. Execution Instructions

- Add the required external provider skill trace standard and table contract.
- Add a checker that scans changed governed Markdown and requires the trace
  table only for explicit current or past consumption claims.
- Keep policy prose and template prose out of the positive claim detector.
- Add focused unit tests for policy prose, missing trace, wrong disposition,
  complete trace, and incomplete `USED_WITH_TRACE`.
- Wire the checker into reviewer-fast, pre-commit, and autorun catalogs.
- Run focused tests and local governance gates before closure.

## 6. Role Output Schema

Completion output must include:

- changed file manifest;
- source verification;
- core guard authorization;
- ADIF disclosure;
- focused test evidence;
- public export disposition;
- claim boundary.

## 7. Dissent And Review Ledger

| Item | Disposition |
|---|---|
| Provider runtime interception | REJECTED - outside CVF authority and outside this tranche |
| Live proof | NOT_RUN_WITH_REASON - no governance behavior or provider behavior claim |
| Public export | DEFERRED_PRIVATE_ONLY |

## Write Ownership

Allowed paths:

- `docs/reference/CVF_EXTERNAL_PROVIDER_SKILL_SOURCE_OF_TRUTH_STANDARD_2026-06-30.md`
- `docs/baselines/CVF_GC018_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`
- `docs/reviews/CVF_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_COMPLETION_2026-06-30.md`
- `governance/compat/check_external_provider_skill_usage_trace.py`
- `governance/compat/test_check_external_provider_skill_usage_trace.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/agent_autorun_command_catalog.py`

Forbidden paths:

- package registry entries and package roots;
- ACTIVE resolver logic;
- provider adapters;
- public-sync clone;
- session state before material closure.

## Pre-Flight Checks

| Check | Command or evidence | Result |
|---|---|---|
| Base head | `git rev-parse --short HEAD` | `09a753ea` |
| Worktree | `git status --short` before EPSOT-T1 edits | clean |
| ADIF query | `run_adif_defect_resolver.py` with governance implementation query | NONE_RETURNED |
| Source read | memory access checker and three catalogs | READ |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Add source-of-truth standard | standard path exists |
| 2 | Add checker and tests | compile and unittest PASS |
| 3 | Wire reviewer-fast, pre-commit, and autorun catalogs | catalog entries present |
| 4 | Run focused checker and governance gates | gate evidence table |
| 5 | Commit material after commit-steward passes | material commit |

## Review Gate

| Gate | Required evidence | Status |
|---|---|---|
| Checker compile | `python -m py_compile governance/compat/check_external_provider_skill_usage_trace.py` | PASS |
| Focused unittest | `python -m unittest governance.compat.test_check_external_provider_skill_usage_trace` | PASS |
| Trace checker | `python governance/compat/check_external_provider_skill_usage_trace.py --base 09a753ea --head HEAD --enforce` | PASS after committed-range rerun |
| Reviewer-fast governance | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS after repairs |
| Commit steward | `python governance/compat/run_agent_commit_steward_preflight.py --base 09a753ea --head HEAD --mode reviewer-return` | required before material commit |

## Evidence Requirements

| Requirement | Required evidence |
|---|---|
| Trace table contract exists | standard file contains required table |
| Checker enforces missing and incomplete trace | focused unittest PASS |
| Catalogs invoke checker | three catalog diffs contain checker command |
| No live-provider claim | completion review records NOT_RUN_WITH_REASON |
| No provider runtime control claim | claim boundary and Machine Closure Package |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | Standard defines trace fields and tokens | PASS |
| AC2 | Checker detects explicit consumption claims without flagging policy prose | PASS |
| AC3 | Reviewer-fast, pre-commit, and autorun catalogs include the checker | PASS |
| AC4 | Completion evidence records no provider runtime or live proof claim | PASS |
| AC5 | Public export remains deferred | PASS |

## Return-To-Orchestrator Conditions

Return if:

- checker cannot distinguish policy prose from explicit consumption claims;
- required catalog wiring would break existing hook shape;
- any closure claim needs live provider behavior;
- scope pressure requires ACTIVE resolver, adapter, package, UI, or public-sync
  changes.

## Closure Checklist

| Item | Status |
|---|---|
| Standard added | PASS |
| Checker and tests added | PASS |
| Catalog wiring added | PASS |
| Focused tests pass | PASS |
| Completion review written | PASS |
| Public export disposition recorded | PASS |
| Live proof disposition recorded | PASS |
| Session-sync queued after material closure | PASS |

## Operator Checkpoint

No blocking operator checkpoint remains for EPSOT-T1. Future ACTIVE resolver,
adapter, live proof, public-sync, or provider-side audit work requires a fresh
operator decision and governed packet.

## 8. Integration Decision

Integrate the checker as a local governance guard only. Do not promote any
provider-owned skill runtime into CVF active runtime in this tranche.

## 9. Completion Evidence

Required commands:

- `python -m py_compile governance/compat/check_external_provider_skill_usage_trace.py`
- `python -m unittest governance.compat.test_check_external_provider_skill_usage_trace`
- `python governance/compat/check_external_provider_skill_usage_trace.py --base 09a753ea --head HEAD --enforce`
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`
- `python governance/compat/run_agent_commit_steward_preflight.py --base 09a753ea --head HEAD --mode reviewer-return`
- `git diff --check`

## 10. Claim Boundary

This work order authorizes trace enforcement in CVF governed artifacts. It does
not authorize provider-side audit access, external runtime interception,
adapter implementation, active resolver behavior, package activation, web UI,
public-sync, push, or live governance proof.

## Claim Boundary

EPSOT-T1 authorizes static trace enforcement in CVF governed artifacts only. It
does not authorize provider-side audit access, external runtime interception,
adapter implementation, active resolver behavior, package activation, web UI,
public-sync, push, or live governance proof.

## ADIF Defect Registry Disclosure

Resolver command:

`python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase implementation --surface-selector governance/compat --risk-ceiling HIGH --max-results 20`

Returned defects: NONE_RETURNED

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | single-agent local implementation and closure |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=09a753ea`; `executionBaseHead=09a753ea`; `closureBaseHead=09a753ea` |
| changedSetScope(phase) | execution and closure changes are limited to the EPSOT-T1 manifest |
| traceScope(phase, actor) | work-order trace covers direct implementation; completion review trace covers reviewer closure |
| commitOwner(phase) | Codex owns material commit; Codex owns later session-sync commit if closure changes next move |
| closer | Codex reviewer/closer |
| crossBatchIsolation | do not mutate AGSK-R7 material except by reference |
| nextMoveSurfaces | session sync only after material commit |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: EPSOT-T1 checker, tests, catalog wiring,
standard, work order, baseline, and completion review only.

Protected paths:

- `governance/compat/check_external_provider_skill_usage_trace.py`
- `governance/compat/test_check_external_provider_skill_usage_trace.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/agent_autorun_command_catalog.py`

Operator authorization: the operator approved building a source-of-truth
mechanism so provider-owned external skill surfaces leave trace evidence when
their output is consumed in CVF.

Rollback boundary: revert only EPSOT-T1 material and later session-sync records;
do not revert AGSK-R7 package-promotion material or unrelated runtime package
state.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Reviewer-fast catalog is a list of named local checks | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | `REVIEWER_FAST_CHECKS` declaration | `REVIEWER_FAST_CHECKS` | local governance hook catalog | EXISTS | ACCEPT |
| Pre-commit catalog is a list of named local checks | `governance/compat/local_governance_hook_catalog_pre_commit.py` | `PRE_COMMIT_CHECKS` declaration | `PRE_COMMIT_CHECKS` | local governance hook catalog | EXISTS | ACCEPT |
| Autorun catalog supports ranged checker commands | `governance/compat/agent_autorun_command_catalog.py` | `_range_command` and `_common_commands` | `_range_command` | agent autorun command catalog | EXISTS | ACCEPT |
| Existing changed-Markdown checker pattern uses applicable prefixes | `governance/compat/check_memory_access_claim.py` | `APPLICABLE_PREFIXES` | `APPLICABLE_PREFIXES` | memory access claim checker | EXISTS | ACCEPT |
| Existing changed-Markdown checker pattern supports ranged CLI flags | `governance/compat/check_memory_access_claim.py` | argument parser flags | `--base`, `--head`, `--enforce` | memory access claim checker CLI | EXISTS | ACCEPT |
| Provider skill trace table is new policy vocabulary | `docs/reference/CVF_EXTERNAL_PROVIDER_SKILL_SOURCE_OF_TRUTH_STANDARD_2026-06-30.md` | Required External Provider Skill Usage Trace | `External Provider Skill Usage Trace` | EPSOT-T1 standard | DOC_ONLY_NEW | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | governance hook catalogs and analogous changed-Markdown checker |
| Runtime behavior claimed | N/A_WITH_REASON: no runtime behavior is claimed |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - source supports static trace guard wiring only |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no provider-owned skill surface was consumed for this work order |
| Provider owner | N/A with reason: no provider-owned skill surface was consumed for this work order |
| Invocation context | N/A with reason: local repository authoring only |
| Output consumed by CVF | N/A with reason: no provider-owned skill output was consumed |
| CVF source-of-truth promotion path | N/A with reason: this work order is governed source evidence |
| Evidence artifact | `docs/work_orders/CVF_AGENT_WORK_ORDER_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md` |
| Authority boundary | no provider output; provider output would be not CVF canonical authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | EPSOT-T1 work order authoring, 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | repository reads, apply_patch, local checker/test authoring |
| Target paths | EPSOT-T1 material manifest |
| Allowed scope source | operator request and EPSOT-T1 GC-018 |
| Before status evidence | base `09a753ea` |
| After status evidence | EPSOT-T1 material staged for closure gates |
| Diff evidence | `git diff --name-status` before closure |
| Approval boundary | bounded trace guard only |
| Claim boundary | no provider runtime, adapter, live, public, activation, or package-promotion claim |
| Agent type | Codex |
| Invocation ID | `epsot-t1-work-order-2026-06-30` |
| Expected manifest | `docs/reference/CVF_EXTERNAL_PROVIDER_SKILL_SOURCE_OF_TRUTH_STANDARD_2026-06-30.md`; `docs/baselines/CVF_GC018_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`; `docs/reviews/CVF_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_COMPLETION_2026-06-30.md`; `governance/compat/check_external_provider_skill_usage_trace.py`; `governance/compat/test_check_external_provider_skill_usage_trace.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/agent_autorun_command_catalog.py` |
| Actual changed set | `docs/reference/CVF_EXTERNAL_PROVIDER_SKILL_SOURCE_OF_TRUTH_STANDARD_2026-06-30.md`; `docs/baselines/CVF_GC018_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_2026-06-30.md`; `docs/reviews/CVF_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_COMPLETION_2026-06-30.md`; `governance/compat/check_external_provider_skill_usage_trace.py`; `governance/compat/test_check_external_provider_skill_usage_trace.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/agent_autorun_command_catalog.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable governance foundation file created | `docs/reference/CVF_EXTERNAL_PROVIDER_SKILL_SOURCE_OF_TRUTH_STANDARD_2026-06-30.md` |
| Storage class | governed reference standard |
| Index or discovery posture | direct dated standard; no generated index mutation in this tranche |
| Rotation or split need | N/A with reason: new compact standard is below guard thresholds |
| Runtime state impact | N/A with reason: no runtime state file or generated aggregate mutation |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EPSOT_T1_PROVIDER_SKILL_TRACE_SOURCE_OF_TRUTH_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: operator-directed governance guard tranche, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation | N/A with reason | PASS |
| Registry Markdown | N/A with reason: no registry Markdown mutation | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no runtime loop or system-loop mutation | N/A with reason | PASS |
| Session continuity | N/A with reason: material work order does not update session state; session-sync follows material commit | N/A with reason | PASS |
| Focused tests | checker compile and unittest | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening; no public-sync authorization.
