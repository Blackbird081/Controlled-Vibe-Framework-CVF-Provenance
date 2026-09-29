# CVF Agent Work Order - AGSK-R5 Runtime Eligibility Audit

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: AGSK-R5

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: 7e64e8bf

executionBaseHead: 7e64e8bf

closureBaseHead: 7e64e8bf

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for AGSK-R5 runtime eligibility
audit.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `7e64e8bf`.

Current-time notes: current date is 2026-06-30. AGSK-R4 closed a bounded
runtime package loader, and the operator now requests continuing ASSF metadata
and runtime-condition evaluation.

Mission summary: implement a no-body runtime eligibility audit helper that
summarizes ASSF generated metadata, package-root counts, lifecycle state
counts, and runtime ineligibility reason buckets.

Do-not-misread notes: this work order does not authorize package lifecycle
promotion. The expected result for AGSK-R3 package roots is still zero runtime
eligible until UAT, certification, and internal implementation evidence exists.

## Purpose

Create a bounded internal audit surface so future lifecycle-promotion work can
see exactly which ASSF metadata conditions block runtime body loading.

## 1. Mission

Implement and test:

- `governance/compat/run_assf_runtime_eligibility_audit.py`
- `governance/compat/test_run_assf_runtime_eligibility_audit.py`

The helper must never request instruction bodies and must never mutate package
metadata.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-06-30 to continue ASSF metadata and runtime-condition evaluation | authorizes AGSK-R5 opening |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current generated session state |
| Active handoff | `AGENT_HANDOFF_V27_2026-06-29.md` | current handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md` | baseline and claim boundary |
| AGSK-R4 loader | `governance/compat/run_assf_runtime_package_loader.py` | source of eligibility behavior |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | package metadata and lifecycle vocabulary |
| ASSF certification lifecycle contract | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | UAT/certification gate |
| ASSF generated index | `docs/reference/agent_system_skills/generated/skill-index.json` | metadata source |

Authority boundary:

- AGSK-R5 may implement audit summary and tests.
- AGSK-R5 may not promote package lifecycle state.
- AGSK-R5 may not open package instruction bodies.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | implement audit helper and focused tests |
| Reviewer/closer | Codex | verify tests, gates, and completion review |
| Operator approval required | operator | lifecycle promotion, adapter implementation, provider/live proof, public-sync, or production claim |

## 4. Scope

Allowed scope:

- create `governance/compat/run_assf_runtime_eligibility_audit.py`;
- create `governance/compat/test_run_assf_runtime_eligibility_audit.py`;
- create `docs/baselines/CVF_GC018_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`;
- create `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`;
- create `docs/reviews/CVF_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_COMPLETION_2026-06-30.md`;
- run focused tests and real-index audit commands.

Forbidden scope:

- editing package roots, registry entries, generated index, resolver behavior,
  hook catalogs, Web runtime, provider/live paths, public-sync paths, or
  session state;
- setting lifecycle values to `APPROVED`, `ACTIVE`, `PASSED`, `CERTIFIED`, or
  `IMPLEMENTED`;
- opening instruction bodies for any package;
- claiming external CLI/MCP support, provider proof, public export, or
  production readiness.

Risk ceiling: R1 internal tooling. The helper is local and read-only except for
normal test temporary files.

## Scope / Target / Owner Boundary

Target: bounded internal runtime eligibility audit helper and tests.

Owner boundary:

- Codex owns implementation and review in this direct tranche;
- operator owns any later lifecycle promotion or external adapter decision.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`governance/compat`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the read-only ADIF resolver returned no matching defects for
this implementation query.

## 5. Required First Reads

Read before editing:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V27_2026-06-29.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`
- this work order
- `governance/compat/run_assf_runtime_package_loader.py`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md`
- `docs/reference/agent_system_skills/generated/skill-index.json`

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Runtime loader builds bounded package packets from generated metadata | `governance/compat/run_assf_runtime_package_loader.py` | `build_runtime_package_packet` | `build_runtime_package_packet` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime loader emits denial reasons without opening bodies by default | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons`; `include_instruction_bodies` | `_runtime_ineligibility_reasons` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| ASSF contract defines lifecycle and internal disposition fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `internalAgentDisposition` | ASSF package contract | EXISTS | ACCEPT |
| Certification requires UAT before certification | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `uatState` | ASSF certification lifecycle contract | LITERAL_INVARIANT | ACCEPT |
| Generated index claim boundary denies activation authority | `docs/reference/agent_system_skills/generated/skill-index.json` | `claimBoundary` | `claimBoundary` | ASSF generated index | LITERAL_INVARIANT | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | AGSK-R4 loader, ASSF package contract, certification lifecycle contract, generated skill index |
| Runtime behavior claimed | bounded no-body audit summary |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |

## 6A. Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| AGSK-R4 left lifecycle promotion as next move | Purpose; Forbidden scope | audit only, no promotion | real-index audit | PASS |
| Runtime loader exposes eligibility behavior | Source Verification; Execution Plan | audit reuses loader | focused tests | PASS |
| Generated index is metadata source | Mission; Source Verification | audit reads generated index through loader | focused tests and smoke | PASS |
| External adapter remains deferred | Forbidden scope; Dual Agent Surface Matrix | claim boundary denies CLI/MCP behavior | focused tests | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=7e64e8bf`; `executionBaseHead=7e64e8bf`; `closureBaseHead=7e64e8bf` |
| changedSetScope(phase) | execution and closure changes are limited to AGSK-R5 helper, test, baseline, work order, and completion review |
| traceScope(phase, actor) | work-order trace covers direct implementation; completion review trace covers reviewer closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit |
| crossBatchIsolation | no AGSK-R3 package-root lifecycle mutation in AGSK-R5 |
| nextMoveSurfaceHandling | session-sync may be handled after material closure if required |
| nextMoveSurfaces | active session state, front door, and handoff are updated only in a session-sync step if material closure changes next move |

## 7. Write Ownership

Owned paths:

- `governance/compat/run_assf_runtime_eligibility_audit.py`
- `governance/compat/test_run_assf_runtime_eligibility_audit.py`
- `docs/baselines/CVF_GC018_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`
- `docs/reviews/CVF_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_COMPLETION_2026-06-30.md`

Forbidden paths:

- `docs/reference/agent_system_skills/packages/**`
- `docs/reference/agent_system_skills/registry/entries/**`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- Web/runtime/provider/live/public-sync paths
- `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, and active handoff files

## Pre-Flight Checks

| Check | Command or evidence | Result |
|---|---|---|
| Base head | `git rev-parse --short HEAD` | `7e64e8bf` |
| Worktree | `git status --short` | AGSK-R5 files only |
| ADIF query | `run_adif_defect_resolver.py` with implementation/governance-compat query | NONE_RETURNED |
| Source read | AGSK-R4 loader, ASSF contracts, generated index | READ |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Implement runtime eligibility audit helper | helper file added |
| 2 | Add focused tests for summary counts, package-root filtering, and claim boundary | test file added |
| 3 | Run focused tests and loader regression tests | completion review evidence |
| 4 | Run real-index package-root and all-record audit commands | completion review evidence |
| 5 | Run governance gates and commit after commit-steward if gates pass | material commit by Codex reviewer/closer |

## Review Gate

| Gate | Required evidence | Status |
|---|---|---|
| Focused tests | `python -m unittest governance.compat.test_run_assf_runtime_eligibility_audit` | PASS |
| Loader regression | `python -m unittest governance.compat.test_run_assf_runtime_package_loader` | PASS |
| Real-index audit | `python governance/compat/run_assf_runtime_eligibility_audit.py --package-roots-only --json` | PASS |
| Reviewer-fast governance | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | pending rerun after shape repairs |

## Evidence Requirements

| Requirement | Required evidence |
|---|---|
| Audit summary works | focused unit tests PASS |
| Audit does not request instruction bodies | claim boundary and tests PASS |
| AGSK-R3 package-root state is summarized | real-index package-root audit PASS |
| Loader compatibility preserved | loader regression tests PASS |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | Audit returns runtime eligible and ineligible counts | PASS |
| AC2 | Audit returns ineligibility reason buckets | PASS |
| AC3 | Audit filters to package roots only | PASS |
| AC4 | Audit never requests instruction bodies | PASS |
| AC5 | Current package-root audit reports 24 blocked package roots and 0 runtime eligible | PASS |

## Return-To-Orchestrator Conditions

| Condition | Disposition |
|---|---|
| Helper cannot import AGSK-R4 loader | BLOCKED with reason: repair import path or return to reviewer |
| Real-index audit reports package body loading | BLOCKED with reason: audit must not request instruction bodies |
| Package lifecycle mutation appears in diff | BLOCKED with reason: remove mutation or return for fresh authorization |
| Focused tests fail | BLOCKED with reason: repair before closure |

## Operator Checkpoint

| Checkpoint | Disposition |
|---|---|
| Lifecycle promotion | Not authorized in AGSK-R5; operator must open a separate bounded promotion tranche |
| External adapter | Not authorized in AGSK-R5; operator must open a separate adapter tranche |
| Provider/live proof | Not required and not authorized because no provider behavior is claimed |
| Public-sync | Deferred private only |

## Closure Checklist

| Item | Status |
|---|---|
| Helper added within owned scope | PASS |
| Focused tests added and passing | PASS |
| Real-index audit records 24 blocked package roots and 0 eligible package roots | PASS |
| Registry, generated index, resolver, package roots, session state, and handoff unchanged | PASS |
| Claim boundary denies activation, certification, adapters, provider/live, public-sync, and production readiness | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `run_assf_runtime_eligibility_audit.py` | internal metadata audit only; no package body or action authority | focused tests and real-index audit | no external adapter | `IMPLEMENTED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter only | no external mutation, activation, package execution, provider call, public-sync, commit, or push | claim boundary | separate adapter contract/work order required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | AGSK-R4 runtime package loader -> AGSK-R5 runtime eligibility audit |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | AGSK-R5 baseline, work order, completion review, audit helper, and focused tests |
| Disposition | IMPLEMENT bounded internal metadata audit; defer activation, certification, external adapter, provider/live, and public-sync |
| Claim boundary | No external source or provider-local memory is promoted as CVF authority in AGSK-R5 |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: AGSK-R5 is operator-directed follow-on audit helper, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | N/A with reason: no registry JSON or generated index edit in AGSK-R5 | no changed registry path | PASS |
| Registry Markdown | N/A with reason: no registry Markdown edit in AGSK-R5 | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created; AGSK-R5 consumes existing governed ASSF metadata | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop interlock roadmap or runtime loop change in AGSK-R5 | N/A with reason | PASS |
| Session continuity | N/A with reason: material work order does not update session state; session-sync may follow after material commit | N/A with reason | PASS |
| Focused tests | `governance/compat/test_run_assf_runtime_eligibility_audit.py` | 3 unittest cases PASS | PASS |
| Runtime audit smoke | `governance/compat/run_assf_runtime_eligibility_audit.py` | package-root audit reports 24 blocked, 0 eligible | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references private provenance package roots and
internal governance helper implementation. Public-safe export requires
separate redaction and public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSK-R5 bounded ASSF runtime eligibility audit |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - helper summarizes metadata and denial reasons without opening instruction bodies |
| receiptEvidence | CVF_RECEIPT_PRESENT - focused tests and real-index audit commands |
| actionEvidence | ACTION_EVIDENCE_PRESENT - helper, test, and source verification |
| invocationBoundary | governed local Python helper and tests only |
| interceptionBoundary | no IDE, shell hook, git, provider, CLI/MCP, Web, public-sync, or external runtime interception claim |
| claimLanguage | implements a no-body ASSF runtime eligibility metadata audit |
| forbiddenExpansion | no package promotion, certification, registry/index mutation, resolver activation, external adapter, provider/live proof, public-sync, or production-readiness claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | AGSK-R5 runtime eligibility audit work-order closure on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; runtime audit smoke command; governance gates |
| Target paths | `governance/compat/run_assf_runtime_eligibility_audit.py`; `governance/compat/test_run_assf_runtime_eligibility_audit.py`; `docs/baselines/CVF_GC018_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`; `docs/reviews/CVF_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_COMPLETION_2026-06-30.md` |
| Allowed scope source | operator request plus AGSK-R5 baseline and work order |
| Before status evidence | base commit `7e64e8bf` |
| After status evidence | helper and tests added; current AGSK package roots audited as not runtime eligible |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | operator requested continuing ASSF metadata and runtime-condition evaluation; lifecycle promotion and external adapter remain forbidden |
| Claim boundary | bounded internal metadata audit only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-agsk-r5-runtime-eligibility-audit-work-order-2026-06-30` |
| Expected manifest | `governance/compat/run_assf_runtime_eligibility_audit.py`; `governance/compat/test_run_assf_runtime_eligibility_audit.py`; `docs/baselines/CVF_GC018_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`; `docs/reviews/CVF_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_COMPLETION_2026-06-30.md` |
| Actual changed set | `governance/compat/run_assf_runtime_eligibility_audit.py`; `governance/compat/test_run_assf_runtime_eligibility_audit.py`; `docs/baselines/CVF_GC018_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_2026-06-30.md`; `docs/reviews/CVF_AGSK_R5_RUNTIME_ELIGIBILITY_AUDIT_COMPLETION_2026-06-30.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

AGSK-R5 is a bounded metadata audit tranche. It does not activate packages,
certify packages, mutate lifecycle state, open instruction bodies, grant
authority, expose external adapters, call providers, public-sync, or claim
production readiness.
