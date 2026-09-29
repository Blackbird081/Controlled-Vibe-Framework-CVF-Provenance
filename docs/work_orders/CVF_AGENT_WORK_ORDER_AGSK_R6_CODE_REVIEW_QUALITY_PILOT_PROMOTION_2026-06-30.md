# CVF Agent Work Order - AGSK-R6 Code Review Quality Pilot Promotion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: AGSK-R6

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: 932001da

executionBaseHead: 932001da

closureBaseHead: 932001da

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for one-package ASSF lifecycle
promotion.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `932001da`.

Current-time notes: current date is 2026-06-30. AGSK-R5 proved all 24 package
roots were runtime-ineligible until UAT, certification, and internal-agent
disposition evidence existed.

Mission summary: promote the `cvf-engineering-code-review-quality` package root
to bounded internal runtime-loader eligibility.

Do-not-misread notes: this work order does not authorize `ACTIVE` status,
automatic resolver invocation, external adapters, provider calls, public-sync,
merge execution, or production claims.

## Purpose

Create a conservative pilot runtime package for CVF by advancing one package
root through UAT, certification, and internal-agent disposition source state.

## 1. Mission

Update and verify:

- `docs/reference/agent_system_skills/registry/entries/cvf-engineering-code-review-quality.json`
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md`
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/README.md`
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/skill.source.json`
- `docs/reference/agent_system_skills/generated/skill-index.json`

The runtime package loader must report the pilot package as eligible and load
the body only when `--include-instruction-bodies` is explicitly requested.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-06-30 to continue ASSF metadata/runtime conditions and use API keys only if needed | authorizes AGSK-R6 opening |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current generated session state |
| Active handoff | `AGENT_HANDOFF_V27_2026-06-29.md` | current handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_2026-06-30.md` | baseline and claim boundary |
| AGSK-R4 loader | `governance/compat/run_assf_runtime_package_loader.py` | source of body-read eligibility behavior |
| AGSK-R5 audit | `governance/compat/run_assf_runtime_eligibility_audit.py` | source of package-root eligibility audit |
| ASSF certification lifecycle contract | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | UAT/certification gate |
| Certified admission checker | `governance/compat/check_assf_certified_metadata_admission.py` | source-state admission guard |

Authority boundary:

- AGSK-R6 may promote only one pilot package root.
- AGSK-R6 may regenerate the generated skill index.
- AGSK-R6 may not activate resolver behavior or expose external adapters.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | update metadata and regenerate index |
| Reviewer/closer | Codex | verify tests, gates, and completion review |
| Operator approval required | operator | any later batch promotion, ACTIVE resolver, adapter, provider/live proof, public-sync, or production claim |

## 4. Scope

Allowed scope:

- update the pilot package registry entry and package root metadata;
- regenerate the generated skill index;
- create AGSK-R6 baseline, work order, and completion review;
- run local ASSF tests and governance gates.
- `docs/reference/agent_system_skills/registry/entries/cvf-engineering-code-review-quality.json`;
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md`;
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/README.md`;
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/skill.source.json`;
- `docs/reference/agent_system_skills/generated/skill-index.json`;
- `docs/baselines/CVF_GC018_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_2026-06-30.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_2026-06-30.md`;
- `docs/reviews/CVF_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_COMPLETION_2026-06-30.md`.

Forbidden scope:

- promoting any package other than `cvf-engineering-code-review-quality`;
- setting `status: ACTIVE`;
- editing resolver activation logic;
- implementing or claiming CLI/MCP adapter behavior;
- using provider keys or live APIs for this non-provider tranche;
- public-sync, merge execution, or production claim.

Risk ceiling: R1 internal package guidance.

## Scope / Target / Owner Boundary

Target: bounded package lifecycle promotion for one code-review package.

Owner boundary:

- Codex owns implementation and reviewer closure in this direct tranche;
- operator owns future package batches, ACTIVE resolver work, external adapter
  work, and public-sync decisions.

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
- `AGENT_HANDOFF_V27_2026-06-29.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_2026-06-30.md`
- this work order
- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/run_assf_runtime_eligibility_audit.py`
- `governance/compat/check_assf_certified_metadata_admission.py`
- pilot package registry and package root files

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Runtime loader body-read eligibility depends on certification, UAT, internal disposition, and package-root existence | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons` | `certificationState`; `uatState`; `internalAgentDisposition` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime loader reads bodies only when explicitly requested | `governance/compat/run_assf_runtime_package_loader.py` | `build_runtime_package_packet` | `include_instruction_bodies` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Certification requires UAT before certification | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `uatState`; `certificationState` | ASSF certification lifecycle contract | LITERAL_INVARIANT | ACCEPT |
| Certified metadata cannot imply ACTIVE status | `governance/compat/check_assf_certified_metadata_admission.py` | `_check_certified_entry` | `ACTIVE` | ASSF certified metadata admission checker | RUNTIME_BEHAVIOR | ACCEPT |
| Pilot package body exists | `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md` | top-level package metadata | `skillId` | ASSF package root | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | AGSK-R4 loader, AGSK-R5 audit helper, certified admission checker, certification lifecycle contract, pilot package root and registry entry |
| Runtime behavior claimed | one explicit package-loader body read |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |

## 6A. Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| AGSK-R5 left lifecycle promotion as next move | Purpose; Scope | one package promoted | audit smoke | PASS |
| Loader requires three lifecycle gates | Source Verification | registry values updated | loader smoke | PASS |
| Generated index is source-derived | Mission; Execution Plan | generated index regenerated | drift checker | PASS |
| External adapter remains deferred | Forbidden scope; Dual Agent Surface Matrix | adapter boundary denied | certified admission checker | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=932001da`; `executionBaseHead=932001da`; `closureBaseHead=932001da` |
| changedSetScope(phase) | execution and closure changes are limited to AGSK-R6 package metadata, generated index, baseline, work order, and completion review |
| traceScope(phase, actor) | work-order trace covers direct implementation; completion review trace covers reviewer closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit |
| crossBatchIsolation | no other package root is promoted in AGSK-R6 |
| nextMoveSurfaceHandling | session-sync follows material closure |
| nextMoveSurfaces | active session state, front door, and handoff are updated after material commit if closure changes next move |

## 7. Write Ownership

## Allowed Scope

Allowed paths:

- `docs/reference/agent_system_skills/registry/entries/cvf-engineering-code-review-quality.json`
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md`
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/README.md`
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/skill.source.json`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- `docs/baselines/CVF_GC018_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_2026-06-30.md`
- `docs/reviews/CVF_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_COMPLETION_2026-06-30.md`

Owned paths:

- `docs/reference/agent_system_skills/registry/entries/cvf-engineering-code-review-quality.json`
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md`
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/README.md`
- `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/skill.source.json`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- AGSK-R6 baseline, work order, and completion review

Forbidden paths:

- other package roots and registry entries;
- resolver activation logic;
- Web/runtime/provider/live/public-sync paths;
- session-sync paths until material closure is complete.

## Pre-Flight Checks

| Check | Command or evidence | Result |
|---|---|---|
| Base head | `git rev-parse --short HEAD` | `932001da` |
| Worktree | `git status --short` before AGSK-R6 edits | clean |
| ADIF query | `run_adif_defect_resolver.py` with ASSF implementation query | NONE_RETURNED |
| Source read | loader, audit helper, certification lifecycle, certified admission checker, pilot package root | READ |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Update pilot lifecycle metadata | registry/package diff |
| 2 | Regenerate generated skill index | drift checker PASS |
| 3 | Run loader body-read smoke and eligibility audit | smoke output PASS |
| 4 | Run focused tests and metadata admission checkers | test output PASS |
| 5 | Run governance gates and commit after commit-steward if gates pass | material commit by Codex reviewer/closer |

## Review Gate

| Gate | Required evidence | Status |
|---|---|---|
| Generated-index drift | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| Certified metadata admission | `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | PASS |
| Package anatomy | `python governance/compat/check_assf_package_candidate_anatomy.py --enforce` | PASS |
| Runtime loader smoke | `python governance/compat/run_assf_runtime_package_loader.py --skill-id cvf-engineering-code-review-quality --include-instruction-bodies --json` | PASS |
| Runtime audit smoke | `python governance/compat/run_assf_runtime_eligibility_audit.py --package-roots-only --json` | PASS |
| Reviewer-fast governance | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS after repairs |

## Evidence Requirements

| Requirement | Required evidence |
|---|---|
| Pilot is runtime eligible | loader smoke returns runtime eligible and loaded body |
| Other package roots remain blocked | audit smoke reports 1 eligible and 23 ineligible package roots |
| Generated aggregate is current | drift checker PASS |
| Certification metadata is admissible | certified metadata checker PASS |
| No live-provider claim | completion review records NOT_RUN_WITH_REASON |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | Pilot registry entry records `APPROVED`, `PASSED`, `CERTIFIED`, and `IMPLEMENTED` | PASS |
| AC2 | Pilot package body and source metadata match the lifecycle boundary | PASS |
| AC3 | Generated index is regenerated from source | PASS |
| AC4 | Runtime loader opens pilot body only on explicit request | PASS |
| AC5 | No ACTIVE, provider, external adapter, public-sync, merge, or production claim is made | PASS |

## Return-To-Orchestrator Conditions

Return if:

- certified metadata checker rejects the pilot source state;
- generated index drift cannot be resolved;
- runtime audit reports more or fewer than one eligible package root;
- any required evidence would need live provider behavior;
- scope pressure requires promoting another package or changing resolver logic.

## Closure Checklist

| Item | Status |
|---|---|
| Source-state update completed | PASS |
| Generated index regenerated | PASS |
| Focused tests and smoke checks pass | PASS |
| Completion review written | PASS |
| Public export disposition recorded | PASS |
| Live proof disposition recorded | PASS |
| Session-sync queued after material closure | PASS |

## Operator Checkpoint

No blocking operator checkpoint remains for AGSK-R6. The operator already
authorized continuing runtime packages and allowed live API keys only if needed.
No live API was needed because this tranche claims no live provider behavior.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | AGSK-R6 code-review-quality pilot promotion on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; Python generator; Python checkers; unittest; runtime loader smoke |
| Target paths | pilot package root, pilot registry entry, generated skill index, AGSK-R6 baseline, work order, completion review |
| Allowed scope source | operator request plus AGSK-R6 baseline and this work order |
| Before status evidence | base commit `932001da`; AGSK-R5 audit reported zero runtime-eligible package roots |
| After status evidence | pilot package eligible for explicit internal body read; audit reports one eligible package root |
| Diff evidence | `git diff --name-status`; generated index drift check; loader smoke; audit smoke; governance gates |
| Approval boundary | operator requested runtime packages; live API keys allowed only if needed; no live API needed |
| Claim boundary | bounded internal package-loader body-read eligibility only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-agsk-r6-code-review-quality-pilot-promotion-2026-06-30` |
| Expected manifest | pilot registry entry; pilot package root files; generated skill index; AGSK-R6 baseline, work order, completion review |
| Actual changed set | pilot registry entry; pilot package root files; generated skill index; AGSK-R6 baseline, work order, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: AGSK-R6 is operator-directed follow-on promotion, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | pilot registry entry | lifecycle fields updated | PASS |
| Registry Markdown | pilot package `SKILL.md` and `README.md` | lifecycle boundary updated | PASS |
| External evidence digest | N/A with reason: no external evidence digest created; AGSK-R6 consumes governed ASSF metadata | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop runtime loop change in AGSK-R6 | N/A with reason | PASS |
| Session continuity | N/A with reason: material work order does not update session state; session-sync follows after material commit | N/A with reason | PASS |
| Focused tests | ASSF loader and audit tests | PASS |
| Runtime smoke | AGSK-R4 loader and AGSK-R5 audit | one eligible package root | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references private provenance package roots and
governed ASSF metadata. Public-safe export requires separate redaction and
public-sync authorization.

## Claim Boundary

AGSK-R6 authorizes one bounded internal runtime-loader package body read. It
does not authorize ACTIVE resolver behavior, automatic invocation, external
adapters, provider/live proof, public-sync, merge, commit, or production
readiness.
