# CVF Agent Work Order - AGSK-R4 Runtime Package Loader

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-29

docType: work_order

Batch ID: AGSK-R4

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: 4003289a

executionBaseHead: 4003289a

closureBaseHead: 4003289a

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for AGSK-R4 runtime package loader.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R4_RUNTIME_PACKAGE_LOADER_2026-06-29.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_AGSK_R4_RUNTIME_PACKAGE_LOADER_2026-06-29.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `4003289a`.

Current-time notes: current date is 2026-06-29. AGSK-R3 committed 24
CVF-owned ASSF package roots as `PROPOSED` package proposals. The operator now
requests runtime packages for CVF.

Mission summary: implement a bounded internal runtime package loader that reads
ASSF generated metadata, reports runtime eligibility, and opens package
instruction bodies only with explicit caller request and lifecycle eligibility.

Do-not-misread notes: this work order does not authorize certifying or
activating the 24 AGSK-R3 packages. The expected result for those packages is
`NOT_RUNTIME_ELIGIBLE` until separate UAT, certification, and implementation
evidence exists.

## Purpose

Create an internal ASSF runtime package loader that can be invoked by future
agents and automation as a bounded readout surface. The loader must preserve
the ASSF no-self-activation invariant and refuse body loading for packages that
are not certified, UAT-passed, implemented, and rooted at an in-scope package
`SKILL.md`.

## 1. Mission

Implement and test:

- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/test_run_assf_runtime_package_loader.py`

The helper must default to metadata-only output. If the caller passes
`--include-instruction-bodies`, it may open a package `SKILL.md` only when all
runtime eligibility checks pass.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-06-29 requesting runtime packages for CVF | authorizes AGSK-R4 opening |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current generated session state |
| Active handoff | `AGENT_HANDOFF_V27_2026-06-29.md` | current handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_AGSK_R4_RUNTIME_PACKAGE_LOADER_2026-06-29.md` | baseline and claim boundary |
| AGSK-R3 worker return | `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md` | package-root proposal evidence |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | package topology and lifecycle vocabulary |
| ASSF composition contract | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | no-self-activation invariant |
| ASSF certification lifecycle contract | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | UAT/certification gate |
| ASSF generated index | `docs/reference/agent_system_skills/generated/skill-index.json` | metadata source |
| Existing resolver | `governance/compat/run_assf_skill_resolver.py` | metadata-only selector precedent |
| External readout helper | `governance/compat/run_assf_external_agent_metadata_readout.py` | adapter-denial boundary precedent |

Authority boundary:

- AGSK-R4 may implement a loader and tests.
- AGSK-R4 may not promote package lifecycle state.
- AGSK-R4 may not implement external adapter behavior or grant action
  authority.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | implement loader and focused tests |
| Reviewer/closer | Codex | verify tests, gates, and completion review |
| Operator approval required | operator | lifecycle promotion, adapter implementation, provider/live proof, public-sync, or production claim |

## 4. Scope

Allowed scope:

- create `governance/compat/run_assf_runtime_package_loader.py`;
- create `governance/compat/test_run_assf_runtime_package_loader.py`;
- create `docs/baselines/CVF_GC018_AGSK_R4_RUNTIME_PACKAGE_LOADER_2026-06-29.md`;
- create `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R4_RUNTIME_PACKAGE_LOADER_2026-06-29.md`;
- create `docs/reviews/CVF_AGSK_R4_RUNTIME_PACKAGE_LOADER_COMPLETION_2026-06-29.md`;
- update `AGENT_HANDOFF_V27_2026-06-29.md` only with a GC-020 marker for
  existing AGSK-R3 material commit `4003289a`;
- read generated ASSF metadata and package `SKILL.md` bodies only when
  eligibility passes and caller explicitly requests body loading;
- run focused tests, smoke command, drift/anatomy checks, and governance gates.

Forbidden scope:

- editing package roots or registry entries;
- changing `skill-index.json`, generator, resolver, hook catalogs, Web runtime,
  provider/live code, public-sync files, session state, or handoff files;
- setting lifecycle values to `APPROVED`, `ACTIVE`, `PASSED`, `CERTIFIED`, or
  `IMPLEMENTED`;
- opening instruction bodies for current AGSK-R3 `PROPOSED` packages;
- claiming that package loading grants authority to perform actions.

Risk ceiling: R1 internal tooling. The helper is local and read-only except for
normal test temporary files.

## Scope / Target / Owner Boundary

Target: bounded internal runtime package loader and tests.

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
- `docs/baselines/CVF_GC018_AGSK_R4_RUNTIME_PACKAGE_LOADER_2026-06-29.md`
- this work order
- `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md`
- `governance/compat/run_assf_skill_resolver.py`
- `governance/compat/run_assf_external_agent_metadata_readout.py`

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| AGSK-R3 package roots are PROPOSED and not runtime-active | `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md` | Registry Source-State Update Evidence; Forbidden Actions Compliance | `PROPOSED`; `Resolver or runtime source mutation` | AGSK-R3 worker return | VALUE_SET | ACCEPT |
| Package lifecycle vocabulary includes CANDIDATE, PROPOSED, APPROVED, ACTIVE, RETIRED, and REJECTED | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | `ACTIVE` | ASSF package contract | VALUE_SET | ACCEPT |
| No self-activation without reviewer decision and UAT is allowed | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | No-Self-Activation Invariant | `APPROVED`; `ACTIVE`; `UAT` | ASSF composition contract | LITERAL_INVARIANT | ACCEPT |
| Certification requires UAT PASSED before CERTIFIED | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `certificationState`; `uatState` | ASSF certification contract | LITERAL_INVARIANT | ACCEPT |
| Generated index claim boundary denies runtime activation and authority expansion | `docs/reference/agent_system_skills/generated/skill-index.json` | `claimBoundary` | `claimBoundary` | ASSF generated index | LITERAL_INVARIANT | ACCEPT |
| Existing resolver reads metadata only and does not open package bodies | `governance/compat/run_assf_skill_resolver.py` | module docstring | `resolve_skill_packet` | ASSF metadata resolver | RUNTIME_BEHAVIOR | ACCEPT |
| External readout helper already denies CLI/MCP adapter behavior and package instruction body execution | `governance/compat/run_assf_external_agent_metadata_readout.py` | `CLAIM_BOUNDARY` | `CLAIM_BOUNDARY` | ASSF external readout helper | LITERAL_INVARIANT | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF contracts, generated index, resolver, external readout helper, AGSK-R3 worker return |
| Existing AGSK-R3 package state | `PROPOSED`, `AWAITING_REVIEW`, `NOT_STARTED`, not implemented |
| Runtime behavior claimed | bounded helper readout plus explicit-request eligible-body loading |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Provider registry surface | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` is not read or changed because AGSK-R4 does not claim provider routing, provider absence, or hardcoded provider capability behavior |
| Provider capability registry | `PROVIDER_CAPABILITY_REGISTRY` is not read or changed because no provider capability claim is made |

## 6A. Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| AGSK-R3 left runtime activation deferred | Scope; Forbidden scope | loader denies current PROPOSED packages | smoke command | PASS |
| ASSF no-self-activation invariant | Source Verification; Acceptance Criteria | lifecycle gate before body loading | unit tests | PASS |
| Generated index is metadata source | Mission; Source Verification | loader reads `skill-index.json` | unit tests and smoke | PASS |
| External adapter remains deferred | Forbidden scope; Dual Agent Surface Matrix | claim boundary denies CLI/MCP behavior | unit tests | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=4003289a`; `executionBaseHead=4003289a`; `closureBaseHead=4003289a` |
| changedSetScope(phase) | execution and closure changes are limited to AGSK-R4 helper, test, baseline, work order, and completion review |
| traceScope(phase, actor) | work-order trace covers direct implementation; completion review trace covers reviewer closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit |
| crossBatchIsolation | no AGSK-R3 package-root lifecycle mutation in AGSK-R4 |
| nextMoveSurfaceHandling | session-sync may be handled after material closure if required |
| nextMoveSurfaces | active session state, front door, and handoff are updated only in a session-sync step if material closure changes next move |

## 7. Write Ownership

Owned paths:

- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/test_run_assf_runtime_package_loader.py`
- `docs/baselines/CVF_GC018_AGSK_R4_RUNTIME_PACKAGE_LOADER_2026-06-29.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R4_RUNTIME_PACKAGE_LOADER_2026-06-29.md`
- `docs/reviews/CVF_AGSK_R4_RUNTIME_PACKAGE_LOADER_COMPLETION_2026-06-29.md`
- `AGENT_HANDOFF_V27_2026-06-29.md` for GC-020 marker only

Forbidden paths:

- `docs/reference/agent_system_skills/packages/**`
- `docs/reference/agent_system_skills/registry/entries/**`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- Web/runtime/provider/live/public-sync paths
- `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, and handoff edits beyond the
  single AGSK-R3 GC-020 marker named above

## Pre-Flight Checks

| Check | Command or evidence | Result |
|---|---|---|
| Base head | `git rev-parse --short HEAD` | `4003289a` |
| Worktree | `git status --short` | AGSK-R4 files only |
| Existing ASSF drift | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| Existing ASSF anatomy | `python governance/compat/check_assf_package_candidate_anatomy.py --enforce` | PASS |
| Source read | ASSF contracts, resolver, external readout, AGSK-R3 worker return | READ |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Implement runtime package loader | helper file added |
| 2 | Add focused tests for default no-body behavior, eligible body load, ineligible denial, out-of-scope roots, selectors, and claim boundary | test file added |
| 3 | Run focused tests and smoke command | completion review evidence |
| 4 | Run ASSF drift/anatomy checks and reviewer-fast gate | gate receipts |
| 5 | Commit after commit-steward if gates pass | material commit by Codex reviewer/closer |

## Evidence Requirements

| Requirement | Required evidence |
|---|---|
| Metadata packet exists | unit test and CLI smoke output |
| Default instruction body denial | unit test with patched `open` |
| Eligible body load only after lifecycle gates | synthetic package unit test |
| Current AGSK package body denial | real-index smoke command |
| No lifecycle/index/registry mutation | `git diff --name-status` and ASSF drift check |

## Review Gate

| Gate | Required result |
|---|---|
| Focused unittest | PASS |
| ASSF drift check | PASS |
| ASSF package anatomy check | PASS |
| Reviewer-fast governance hook | PASS before commit claim |
| Commit steward preflight | PASS before material commit |

## Closure Checklist

| Item | Disposition |
|---|---|
| Helper added | checked |
| Tests added | checked |
| Current PROPOSED package denied body loading | checked |
| No registry or generated-index edit | checked |
| No provider/live/public-sync claim | checked |
| Public Export Disposition present | checked |

## Return-To-Orchestrator Conditions

| Condition | Return status |
|---|---|
| Helper and tests pass with current AGSK package denied | `CLOSED_PASS_BOUNDED` |
| Lifecycle gate cannot be implemented without package promotion | `BLOCKED_WITH_REASON` |
| Any registry/index/provider/public-sync mutation becomes necessary | stop and return to operator |

## Operator Checkpoint

No additional operator checkpoint is required for AGSK-R4 bounded loader
implementation. Fresh operator authorization is required before any lifecycle
promotion, UAT/certification, external adapter, provider/live proof,
public-sync, or production-readiness claim.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | AGSK-R4 runtime package loader implementation on 2026-06-29 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python unittest; ASSF drift/anatomy checks; reviewer-fast gate |
| Target paths | AGSK-R4 helper, test, baseline, work order, and completion review |
| Allowed scope source | this work order and paired AGSK-R4 baseline |
| Before status evidence | `dispatchBaseHead=4003289a`; `executionBaseHead=4003289a`; `closureBaseHead=4003289a` |
| After status evidence | runtime loader and focused tests added; no registry or generated-index mutation |
| Diff evidence | `git diff --name-status` over AGSK-R4 changed set |
| Approval boundary | operator requested runtime packages; promotion and external adapter remain forbidden |
| Claim boundary | bounded internal runtime package loader only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-agsk-r4-runtime-package-loader-2026-06-29` |
| Expected manifest | helper, test, baseline, work order, completion review |
| Actual changed set | AGSK-R4 helper, test, baseline, work order, completion review |
| Manifest delta | none observed |
| Deletion or rename disposition | N/A with reason: none |

## 8. Acceptance Criteria

| ID | Criterion | Required evidence | Status |
|---|---|---|---|
| AC1 | Loader builds bounded runtime package packets from generated metadata | focused unit tests | PASS |
| AC2 | Loader does not open instruction bodies by default | unit test with patched `open` | PASS |
| AC3 | Loader opens instruction bodies only when explicit request and eligibility pass | synthetic eligible package test | PASS |
| AC4 | Current AGSK-R3 PROPOSED package is denied body loading | real-index smoke command | PASS |
| AC5 | Claim boundary denies activation, authority grant, provider calls, CLI/MCP adapter behavior, public-sync, and commit/push | unit test and output inspection | PASS |

## 9. Completion Evidence

| Evidence | Result |
|---|---|
| Focused tests | `python -m unittest governance.compat.test_run_assf_runtime_package_loader` PASS, 7 tests |
| Real-index smoke | `python governance/compat/run_assf_runtime_package_loader.py --skill-id cvf-engineering-code-review-quality --include-instruction-bodies --json` returns `NOT_RUNTIME_ELIGIBLE` |
| Completion review | `docs/reviews/CVF_AGSK_R4_RUNTIME_PACKAGE_LOADER_COMPLETION_2026-06-29.md` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AGSK_R4_RUNTIME_PACKAGE_LOADER_COMPLETION_2026-06-29.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: AGSK-R4 is operator-directed follow-on runtime helper, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | N/A with reason: no registry JSON or generated index edit in AGSK-R4 | `check_assf_skill_index_drift.py` PASS | PASS |
| Registry Markdown | N/A with reason: no registry Markdown edit in AGSK-R4 | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created; AGSK-R4 consumes existing governed AGSK-R3 package roots | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop interlock roadmap or runtime loop change in AGSK-R4 | N/A with reason | PASS |
| Session continuity | `AGENT_HANDOFF_V27_2026-06-29.md` | GC-020 marker for `4003289a` present | PASS |
| Focused tests | `governance/compat/test_run_assf_runtime_package_loader.py` | 7 unittest cases PASS | PASS |
| Runtime smoke | `run_assf_runtime_package_loader.py` | `NOT_RUNTIME_ELIGIBLE` for current AGSK package | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references private provenance package roots and
governance helper implementation. Public-safe export requires separate
redaction and public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSK-R4 work order for bounded internal runtime package loader |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - internal helper implemented and tested |
| receiptEvidence | CVF_RECEIPT_PRESENT - tests and smoke command |
| actionEvidence | ACTION_EVIDENCE_PRESENT - helper and test files |
| invocationBoundary | local Python helper only |
| interceptionBoundary | no IDE, shell hook, git, provider, CLI/MCP, Web, public-sync, or external runtime interception claim |
| claimLanguage | creates runtime package loader with lifecycle-gated body loading |
| forbiddenExpansion | no package promotion, no certification, no registry/index mutation, no external adapter, no provider/live proof, no public-sync, no production-readiness claim |

## Claim Boundary

This work order is closed bounded. AGSK-R4 creates a runtime package loader
surface, but it does not activate, certify, publish, externally expose, or
authorize execution of any ASSF package.
