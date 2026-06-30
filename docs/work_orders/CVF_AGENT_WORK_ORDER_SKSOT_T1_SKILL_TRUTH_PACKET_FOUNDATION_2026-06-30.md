# CVF Agent Work Order - SKSOT-T1 Skill Truth Packet Foundation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: SKSOT-T1

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: 291788b6

executionBaseHead: 291788b6

closureBaseHead: 291788b6

## Dispatch Prompt Envelope

Role: Codex direct implementer and reviewer for the skill truth packet
foundation.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `291788b6`.

Current-time notes: current date is 2026-06-30. AGSK-R7 closed with six
runtime-eligible package roots, no ACTIVE resolver, and no external adapter.

Mission summary: create a CVF-native source-of-truth packet layer for those six
runtime-eligible package roots.

Do-not-misread notes: this work order does not authorize package activation,
external adapters, provider calls, public-sync, or package lifecycle mutation.

## Purpose

Implement the first bounded skill truth packet foundation so CVF can scale
skill packages without losing evidence, provenance, obligation, and receipt
traceability.

## 1. Mission

Create and verify:

- a skill truth packet standard;
- a packet source layout under `docs/reference/agent_system_skills/truth/`;
- one packet per current runtime-eligible package root;
- a generated truth index;
- a read-only checker and unit tests;
- hook catalog wiring.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat approval on 2026-06-30 to build the mechanism | authorizes SKSOT-T1 opening |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V28_2026-06-30.md` | active handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_2026-06-30.md` | scope and claim boundary |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | package field authority |
| ASSF registry source layout | `docs/reference/agent_system_skills/registry/README.md` | registry/index source discipline |
| Runtime loader | `governance/compat/run_assf_runtime_package_loader.py` | eligibility requirements |
| Runtime eligibility audit | `governance/compat/run_assf_runtime_eligibility_audit.py` | current six-package eligibility evidence |

Authority boundary:

- SKSOT-T1 may create truth records for the six already eligible package roots.
- SKSOT-T1 may create a checker and hook wiring.
- SKSOT-T1 may not mutate package lifecycle state or activate packages.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | create standard, packets, checker, tests, and hooks |
| Reviewer/closer | Codex | verify checks and completion review |
| Operator approval required | operator | future ACTIVE resolver, external adapter, provider/live proof, public-sync, or additional package promotion |

## 4. Scope

Allowed scope:

- `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md`;
- `docs/reference/agent_system_skills/truth/README.md`;
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-code-review-quality.json`;
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-debugging-error-recovery.json`;
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-planning-task-breakdown.json`;
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-security-hardening.json`;
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-spec-driven-development.json`;
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-test-driven-development.json`;
- `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json`;
- `governance/compat/check_skill_truth_packets.py`;
- `governance/compat/test_check_skill_truth_packets.py`;
- `governance/compat/agent_autorun_command_catalog.py`;
- `governance/compat/local_governance_hook_catalog_pre_commit.py`;
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`;
- `docs/baselines/CVF_GC018_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_2026-06-30.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_2026-06-30.md`;
- `docs/reviews/CVF_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_COMPLETION_2026-06-30.md`.

Forbidden scope:

- editing ASSF registry lifecycle state;
- editing package bodies or using them as active guidance;
- setting any package `ACTIVE`;
- changing resolver activation behavior;
- implementing adapters or provider calls;
- public-sync, production claims, or broad refactors.

Risk ceiling: R2 internal governance control.

## Scope / Target / Owner Boundary

Target: bounded skill truth packet control for six already runtime-eligible
ASSF package roots.

Owner boundary:

- Codex owns implementation and reviewer closure in this direct tranche;
- operator owns future ACTIVE resolver, external adapter, provider/live proof,
  public-sync, or additional package promotion decisions.

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
- `docs/reference/agent_system_skills/registry/README.md`
- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/run_assf_runtime_eligibility_audit.py`

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF registry entries are authoritative per-skill sources | `docs/reference/agent_system_skills/registry/README.md` | Purpose | `entries/` | ASSF registry source family | LITERAL_INVARIANT | ACCEPT |
| Generated ASSF skill index is a derived read model | `docs/reference/agent_system_skills/registry/README.md` | Purpose; Adding A New Entry | `generated/skill-index.json` | ASSF registry source family | LITERAL_INVARIANT | ACCEPT |
| ASSF package lifecycle fields include status, UAT, certification, and internal/external dispositions | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema; Internal-Agent And External-Agent CLI/MCP Disposition Fields | `status`; `uatState`; `certificationState`; `internalAgentDisposition`; `externalCliMcpDisposition` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Runtime eligibility requires certified, UAT-passed, implemented internal disposition, and package root existence | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons` | `certificationState`; `uatState`; `internalAgentDisposition`; `canonicalRoot` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime eligibility audit reports ready package roots through `ready_for_body_load` | `governance/compat/run_assf_runtime_eligibility_audit.py` | `build_runtime_eligibility_audit` | `ready_for_body_load` | AGSK-R5 audit helper | RUNTIME_BEHAVIOR | ACCEPT |
| Truth packet checker is new in this tranche | `governance/compat/check_skill_truth_packets.py` | SKSOT-T1 new file | `check` | SKSOT-T1 checker | DOC_ONLY_NEW | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF package contract, registry README, runtime loader, runtime audit helper, six registry entries, six package roots |
| Runtime behavior claimed | read-only packet validation and generated truth-index drift checking |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Operator requested clear central management before skill scale-up | Purpose; Mission | skill truth packet foundation | completion review | PASS |
| AGSK-R7 left six eligible package roots | Source Verification | six packet records | runtime audit and checker | PASS |
| Truth Kernel patterns should be absorbed only through CVF authority | Authority Chain; Claim Boundary | CVF standard and checker | source boundary review | PASS |
| Generated read models must not become authority | Source Verification | generated truth index checked against packet sources | checker | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=291788b6`; `executionBaseHead=291788b6`; `closureBaseHead=291788b6` |
| changedSetScope(phase) | standard, truth packet sources, generated truth index, checker, tests, catalogs, and closure artifacts |
| traceScope(phase, actor) | work-order trace covers direct implementation; completion review trace covers reviewer closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit if committed |
| crossBatchIsolation | no ASSF lifecycle state or package body mutation in SKSOT-T1 |
| nextMoveSurfaceHandling | session-sync follows material closure if closure changes next move |
| nextMoveSurfaces | active session state, front door, and handoff |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one read-only skill truth packet
checker, its focused test, and the minimal hook-catalog entries needed to run
that checker in governed local workflows.

Protected paths (every changed guard/control path is listed):

- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/check_skill_truth_packets.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/test_check_skill_truth_packets.py`

Operator authorization: the operator instructed Codex to proceed building the
skill source-of-truth control mechanism after reviewing the Truth Kernel
reference input and agreeing to the skill control-plane direction.

Rollback boundary: if SKSOT-T1 is rejected, remove only the new checker, test,
hook-catalog entries, skill truth packet standard, truth packet layout, packet
sources, generated truth index, and SKSOT-T1 artifacts. Do not revert prior
AGSK package promotion, ASSF registry entries, package roots, or session-sync
commits.

Scope boundary: this authorization does not extend to unrelated guard behavior,
package lifecycle state, package bodies, resolver activation, external
adapters, provider/live proof, public-sync, or production runtime.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/agent_system_skills/` |
| Storage decision | add stable skill truth packet standard plus `truth/packets/` source records and `truth/generated/` read model |
| Stable filename disposition | standard uses `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md`; dated execution evidence remains in baseline/work order/review |
| Generated aggregate discipline | generated truth index is derived from packet sources and checked by `check_skill_truth_packets.py` |
| Authority boundary | packet sources and ASSF registry entries are source records; generated index is read-only read model |
| Forbidden expansion | no competing package registry, no ACTIVE resolver, no adapter, no public export |

## 7. Execution Instructions

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | Codex | create |
| `docs/reference/agent_system_skills/truth/README.md` | Codex | create |
| `docs/reference/agent_system_skills/truth/packets/cvf-engineering-code-review-quality.json` | Codex | create |
| `docs/reference/agent_system_skills/truth/packets/cvf-engineering-debugging-error-recovery.json` | Codex | create |
| `docs/reference/agent_system_skills/truth/packets/cvf-engineering-planning-task-breakdown.json` | Codex | create |
| `docs/reference/agent_system_skills/truth/packets/cvf-engineering-security-hardening.json` | Codex | create |
| `docs/reference/agent_system_skills/truth/packets/cvf-engineering-spec-driven-development.json` | Codex | create |
| `docs/reference/agent_system_skills/truth/packets/cvf-engineering-test-driven-development.json` | Codex | create |
| `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` | Codex | create |
| `governance/compat/check_skill_truth_packets.py` | Codex | create |
| `governance/compat/test_check_skill_truth_packets.py` | Codex | create |
| `governance/compat/agent_autorun_command_catalog.py` | Codex | update |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | Codex | update |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | Codex | update |
| `docs/baselines/CVF_GC018_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_2026-06-30.md` | Codex | create |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_2026-06-30.md` | Codex | create |
| `docs/reviews/CVF_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_COMPLETION_2026-06-30.md` | Codex | create |

## Allowed Paths

- `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md`
- `docs/reference/agent_system_skills/truth/README.md`
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-code-review-quality.json`
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-debugging-error-recovery.json`
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-planning-task-breakdown.json`
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-security-hardening.json`
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-spec-driven-development.json`
- `docs/reference/agent_system_skills/truth/packets/cvf-engineering-test-driven-development.json`
- `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json`
- `governance/compat/check_skill_truth_packets.py`
- `governance/compat/test_check_skill_truth_packets.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `docs/baselines/CVF_GC018_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_2026-06-30.md`
- `docs/reviews/CVF_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_COMPLETION_2026-06-30.md`

## Forbidden Paths

- ASSF registry entries;
- ASSF package roots;
- resolver activation code;
- external adapter code;
- session state files unless a later session-sync tranche is opened;
- public-sync repository files.

## Pre-Flight Checks

| Check | Status |
|---|---|
| Startup front door and active handoff read | PASS |
| Guard orientation and literal-format gotchas read | PASS |
| ADIF resolver queried | PASS |
| Runtime eligibility audit refreshed | PASS |

## Execution Plan

Implement:

1. Add the skill truth packet standard and truth folder README.
2. Add six packet JSON files for current runtime-eligible package roots.
3. Add generated truth index derived from the packet sources.
4. Add `check_skill_truth_packets.py` with `--base`, `--head`, `--enforce`, and `--json`.
5. Add unit tests covering pass and failure modes.
6. Wire the checker into reviewer-fast, pre-commit, and autorun catalogs.
7. Run focused verification and close with completion review.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| Unit tests | `python -m unittest governance.compat.test_check_skill_truth_packets` PASS |
| Packet checker | `python governance/compat/check_skill_truth_packets.py --base 291788b6 --head HEAD --enforce` PASS |
| Runtime audit | six eligible package roots remain unchanged |
| Core guard | complete authorization block and PASS |

## Review Gate

Reviewer must confirm packet count, generated truth index drift, strict
obligation enforcement, hook wiring, and no package activation claim.

## Closure Checklist

| Item | Status |
|---|---|
| Standard created | PASS |
| Six packets created | PASS |
| Generated truth index created | PASS |
| Checker and tests created | PASS |
| Hook catalogs wired | PASS |
| Completion review filed | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after focused tests and checker pass. Return
`BLOCKED` if packet sources cannot be source-verified or if package lifecycle
mutation is required.

## Operator Checkpoint

No further operator checkpoint is required for SKSOT-T1 closure. Future ACTIVE
resolver, external adapter, provider/live proof, public-sync, or additional
package promotion requires fresh operator approval.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Standard and truth README exist | files created |
| AC2 | Six packets exist for the six runtime-eligible packages | packet count 6 |
| AC3 | Generated index matches packet sources | checker PASS |
| AC4 | Checker unit tests cover core failure modes | unittest PASS |
| AC5 | Governance catalogs run the checker | catalog entries present |
| AC6 | No package lifecycle, ACTIVE resolver, provider/live, adapter, public-sync, or production claim is made | claim boundary PASS |

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
| Input type | Legacy source family |
| Chain map route | external/private reference input -> CVF-governed reference standard -> packet checker and source records |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | SKSOT-T1 baseline, work order, completion review, standard, packets, generated truth index, checker, and tests |
| Disposition | absorb useful source-of-truth patterns into CVF-owned skill governance without treating private reference input as canonical authority |
| Claim boundary | no external source or provider-local memory is promoted as CVF authority in SKSOT-T1 |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | SKSOT-T1 skill truth packet foundation on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | apply_patch; PowerShell hash calculation; Python checker; unittest; runtime audit |
| Target paths | skill truth standard, truth packet layout, generated truth index, checker, tests, governance catalogs, SKSOT-T1 artifacts |
| Allowed scope source | operator approval plus SKSOT-T1 baseline and work order |
| Before status evidence | base commit `291788b6`; AGSK-R7 had six runtime-eligible package roots |
| After status evidence | six truth packets and generated truth index validate through checker |
| Diff evidence | packet checker, unit tests, runtime audit, and governance gates |
| Approval boundary | operator approved building the mechanism; live API keys not needed because no live behavior claim is made |
| Claim boundary | bounded read-only skill truth packet control only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-sksot-t1-skill-truth-packet-foundation-2026-06-30` |
| Expected manifest | standard, README, six packets, generated index, checker, tests, catalogs, baseline, work order, completion review |
| Actual changed set | standard, README, six packets, generated index, checker, tests, catalogs, baseline, work order, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

SKSOT-T1 is a bounded skill truth packet foundation. It does not activate
skills, mutate package lifecycle state, implement adapters, call providers,
public-sync, or grant action authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references private ASSF provenance and internal skill
truth records. Public-safe export requires a separate public-sync tranche.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SKSOT_T1_SKILL_TRUTH_PACKET_FOUNDATION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: operator-directed skill control-plane foundation, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | N/A with reason: SKSOT-T1 does not mutate ASSF registry lifecycle sources | N/A with reason | PASS |
| Registry Markdown | skill truth standard and README | created | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop runtime loop change in SKSOT-T1 | N/A with reason | PASS |
| Session continuity | N/A with reason: material closure does not update session state; session-sync may follow | N/A with reason | PASS |
| Focused tests | skill truth packet tests | PASS |
| Runtime smoke | skill truth packet checker and runtime eligibility audit | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Packet count | `6` | `6` | PASS |
| Runtime eligibility claim | existing six runtime-eligible package roots only | six packet records match existing eligible roots | PASS |
| Checker status | PASS | `check_skill_truth_packets.py --base 291788b6 --head HEAD --enforce` PASS | PASS |
| Unit test status | PASS | `python -m unittest governance.compat.test_check_skill_truth_packets` PASS | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |
