# CVF Agent Work Order - PKGSOP-T2 Package Skill Pipeline Guard

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: PKGSOP-T2

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: 046ba66d

executionBaseHead: 046ba66d

closureBaseHead: 046ba66d

## Dispatch Prompt Envelope

Role: Codex direct dispatcher, implementer, reviewer, and closer for the
package skill productionization pipeline checker.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_PKGSOP_T2_PACKAGE_SKILL_PIPELINE_GUARD_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_PKGSOP_T2_PACKAGE_SKILL_PIPELINE_GUARD_2026-06-30.md`.

Commit mode: `REVIEWER_MAY_COMMIT`.

Base: `046ba66d`.

Mission summary: implement a read-only checker and hook wiring that enforce the
PKGSOP-T1 package skill productionization pipeline.

Do-not-misread notes: this work order does not authorize package conversion,
lifecycle mutation, package root mutation, truth packet mutation, provider
calls, Model Gateway/model router work, provider registry mutation, public-sync,
or production-readiness expansion.

## Purpose

Make the package skill productionization SOP enforceable by machine gates.

## 1. Mission

Add:

- package skill productionization pipeline checker;
- focused tests;
- autorun/reviewer-fast/pre-commit/pre-push wiring;
- governed baseline and completion review.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | current session request to make the checker immediately | authorizes PKGSOP-T2 checker/wiring |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V28_2026-06-30.md` | active handoff named by state registry |
| Paired baseline | `docs/baselines/CVF_GC018_PKGSOP_T2_PACKAGE_SKILL_PIPELINE_GUARD_2026-06-30.md` | scope and claim boundary |
| Package SOP | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` | pipeline source |

Authority boundary: this work order authorizes checker implementation and
wiring only.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author baseline and work order |
| Implementer | Codex | add checker, tests, and catalog wiring |
| Reviewer/closer | Codex | verify tests, gates, and closure review |
| Operator approval required | operator | any future package conversion, runtime work, public-sync, or model-router work |

## 4. Scope

Allowed paths:

- `governance/compat/check_package_skill_productionization_pipeline.py`
- `governance/compat/test_check_package_skill_productionization_pipeline.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `docs/baselines/CVF_GC018_PKGSOP_T2_PACKAGE_SKILL_PIPELINE_GUARD_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_PKGSOP_T2_PACKAGE_SKILL_PIPELINE_GUARD_2026-06-30.md`
- `docs/reviews/CVF_PKGSOP_T2_PACKAGE_SKILL_PIPELINE_GUARD_COMPLETION_2026-06-30.md`

Forbidden paths:

- ASSF registry entries;
- package roots;
- truth packets;
- generated ASSF indexes;
- runtime package executor behavior;
- provider registry;
- public-sync repository;
- session state until material closure requires a separate session-sync.

Risk ceiling: R1 checker and governance wiring.

## Scope / Target / Owner Boundary

Target: machine enforcement for package skill productionization pipeline
discipline.

Owner boundary: Codex owns direct checker closure in this tranche. Operator
owns any future package runtime expansion, remaining-package conversion, Model
Gateway/model router, provider registry mutation, or public-sync decision.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`guard`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`governance/compat`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure command:

```text
python governance/compat/run_adif_defect_resolver.py --task-class guard --role worker --lifecycle-phase implementation --surface-selector governance/compat --risk-ceiling HIGH --max-results 20 --json
```

## Package Skill Productionization Control Block

- SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
- Current phase: P11 scale-up operation guard systemization
- Target lifecycle state: N/A with reason: checker implementation only
- Prior phase evidence: PKGSOP-T1 material commit `693608cb`; ASCP-P1-P3 six-package baseline `43e4092f`
- Next forbidden skip: no package source, package root, truth packet, ACTIVE state, provider call, or production claim may bypass the SOP phase ladder
- Runtime/provider proof: N/A with reason: this tranche adds a read-only checker and makes no new runtime behavior claim
- Claim boundary: machine enforcement for package-skill pipeline evidence only

## 5. Required First Reads

Read before editing:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V28_2026-06-30.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `governance/compat/check_assf_package_candidate_anatomy.py`
- `governance/compat/check_assf_certified_metadata_admission.py`
- `governance/compat/check_skill_truth_packets.py`

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Package-skill SOP defines the phase ladder and production admission evidence | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` | End-To-End Phase Ladder; Runtime Package Production Admission | `P10 production package runtime` | package skill productionization SOP | LITERAL_INVARIANT | ACCEPT |
| Package lifecycle states include `CANDIDATE`, `PROPOSED`, `APPROVED`, and `ACTIVE` | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | `ACTIVE` | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| Checker requires package-skill control block on changed package-skill artifacts | `governance/compat/check_package_skill_productionization_pipeline.py` | checker source | `CONTROL_BLOCK` | package-skill pipeline checker | RUNTIME_BEHAVIOR | ACCEPT |
| Checker enforces required control fields | `governance/compat/check_package_skill_productionization_pipeline.py` | checker source | `CONTROL_REQUIRED_FIELDS` | package-skill pipeline checker | RUNTIME_BEHAVIOR | ACCEPT |
| Autorun catalog invokes checker | `governance/compat/agent_autorun_command_catalog.py` | command catalog | `package skill productionization pipeline` | agent autorun command catalog | RUNTIME_BEHAVIOR | ACCEPT |
| Reviewer-fast hook catalog invokes checker | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | hook catalog | `package skill productionization pipeline` | reviewer-fast hook catalog | RUNTIME_BEHAVIOR | ACCEPT |
| Pre-commit hook catalog invokes checker | `governance/compat/local_governance_hook_catalog_pre_commit.py` | hook catalog | `package skill productionization pipeline` | pre-commit hook catalog | RUNTIME_BEHAVIOR | ACCEPT |
| Pre-push hook catalog invokes checker | `governance/compat/local_governance_hook_catalog_pre_push.py` | hook catalog | `package skill productionization pipeline` | pre-push hook catalog | RUNTIME_BEHAVIOR | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Bind agents to package SOP | Mission | checker source | focused unit tests and checker smoke | PASS |
| Enforce control block | Package Skill Productionization Control Block | `CONTROL_BLOCK` | focused unit tests | PASS |
| Enforce lifecycle ladder | Source-Fidelity Pass | registry/package/truth snapshot checks | checker smoke | PASS |
| Wire into gates | Execution Instructions | hook and autorun catalogs | pre-implementation gate | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer, all Codex in same governed turn |
| baseHeadFor(phase) | `dispatchBaseHead=046ba66d`; `executionBaseHead=046ba66d`; `closureBaseHead=046ba66d` |
| changedSetScope(phase) | checker, test, hook catalogs, baseline, work order, completion review |
| traceScope(phase, actor) | work-order trace covers implementation; completion review trace covers closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit if committed |
| crossBatchIsolation | no package lifecycle mutation, runtime helper behavior mutation, generated index, truth packet, provider registry, public-sync, or session-sync mutation |
| nextMoveSurfaceHandling | session-sync follows material closure if mode or next allowed move changes |
| nextMoveSurfaces | active session state, front door, and handoff |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `governance/compat/` and `docs/reference/agent_system_skills/` |
| Storage decision | add one checker and one focused test |
| Stable filename disposition | `governance/compat/check_package_skill_productionization_pipeline.py` |
| Generated aggregate discipline | N/A with reason: no generated JSON aggregate is added or edited |
| Authority boundary | checker only; package sources and runtime helpers remain separate governed surfaces |
| Forbidden expansion | no package conversion, lifecycle mutation, runtime helper behavior change, provider call, model router, public export, or action authority |
| Model Gateway boundary | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are accounted-for, out-of-scope, and untouched |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add the package skill productionization
pipeline checker and wire it into existing governance gate catalogs.

Protected paths:

- `governance/compat/check_package_skill_productionization_pipeline.py`
- `governance/compat/test_check_package_skill_productionization_pipeline.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`

Operator authorization: the operator explicitly requested immediate checker
enforcement after confirming the SOP alone was not enough.

Rollback boundary: revert the PKGSOP-T2 material commit only; do not revert
PKGSOP-T1 SOP commit `693608cb`, ASCP-P1-P3 material commit `43e4092f`, package
roots, truth packets, generated ASSF indexes, or prior ASCP helper commits.

## 7. Execution Instructions

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| checker and focused test | Codex | create |
| autorun and hook catalogs | Codex | update |
| baseline, work order, completion review | Codex | create |

## Pre-Flight Checks

| Check | Status |
|---|---|
| Startup front door and active handoff read | PASS |
| Guard orientation and literal-format gotchas read | PASS |
| ADIF resolver queried | PASS |
| SOP and ASSF package contract source-checked | PASS |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Add checker | `governance/compat/check_package_skill_productionization_pipeline.py` |
| 2 | Add tests | `governance/compat/test_check_package_skill_productionization_pipeline.py` |
| 3 | Wire catalogs | autorun, reviewer-fast, pre-commit, pre-push |
| 4 | Run focused checks | unit test, checker smoke, py_compile |
| 5 | Run governance gates | autorun and commit steward |
| 6 | Commit material | reviewer/closer commit |
| 7 | Session sync | active state/handoff/front door if required |

## Evidence Requirements

| Evidence | Required result |
|---|---|
| ADIF disclosure | NONE_RETURNED for exact query |
| Source verification | all checker/wiring source facts ACCEPT |
| Focused unit test | PASS |
| Checker smoke | PASS |
| Governance gates | PASS |
| Changed set review | no registry, package root, truth packet, generated index, provider, public-sync, or package lifecycle mutation |

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| Checker exists | `governance/compat/check_package_skill_productionization_pipeline.py` |
| Control block enforcement exists | missing control block test fails |
| ACTIVE lifecycle evidence enforcement exists | missing truth packet test fails |
| Hook wiring exists | autorun, reviewer-fast, pre-commit, and pre-push catalogs call checker |
| Runtime boundary | no package runtime behavior changed |

## Operator Checkpoint

No additional operator checkpoint is required for this checker-only tranche.
Any future package conversion, lifecycle mutation, runtime helper behavior,
provider live proof, Model Gateway/model router work, or public-sync requires a
fresh operator-approved GC-018 or work order.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | SOP, ASSF package contract, new checker, autorun catalog, local hook catalogs |
| Runtime behavior claimed | N/A_WITH_REASON: checker behavior only; no package runtime behavior changed |
| Live/provider proof claimed | N/A_WITH_REASON: no new live proof; no provider/API behavior claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync authorized |
| Freshness disposition | PASS - current sources support checker implementation and wiring only |

## Review Gate

Reviewer must confirm the checker is read-only, catches missing package-skill
pipeline control blocks, validates lifecycle evidence for package states, and
does not mutate ASSF registry, package roots, truth packets, generated indexes,
runtime helpers, provider registry, or public-sync. The current Model Gateway
provider registry surface `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`
and capability surface `PROVIDER_CAPABILITY_REGISTRY` are accounted-for,
out-of-scope, and untouched.

## Closure Checklist

| Item | Status |
|---|---|
| Checker created | PASS |
| Focused tests created | PASS |
| Autorun wired | PASS |
| Reviewer-fast wired | PASS |
| Pre-commit wired | PASS |
| Pre-push wired | PASS |
| No runtime mutation | PASS |
| Public export deferred | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after checker, tests, hook wiring, changed-set
review, and governance gates pass. Return `BLOCKED` if checker implementation
requires package lifecycle mutation, package root mutation, provider registry
mutation, public-sync, or live provider proof.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local CVF skill-control checker -> source verification -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | PKGSOP-T2 baseline, work order, completion review, and checker |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local source verification only |
| Claim boundary | external repositories and provider skills remain input sources, not CVF authority |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: this work order implements a checker and does not consume package output |
| Package root | N/A with reason: no package body loaded |
| Invocation context | PKGSOP-T2 checker implementation |
| Receipt evidence | N/A with reason: no new skillUsageReceipt consumed |
| Output consumed by CVF | N/A with reason: none |
| Truth packet or source path | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` |
| Authority boundary | this work order does not grant authority; future receipts do not grant authority |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | PKGSOP-T2 checker implementation |
| Output consumed by CVF | N/A with reason: none |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this work order and paired completion review |
| Authority boundary | provider-owned skill output is not CVF canonical authority without governed promotion |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | PKGSOP-T2 package skill pipeline guard on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, unittest, governance gates |
| Target paths | checker, test, hook catalogs, baseline, work order, completion review |
| Allowed scope source | operator instruction plus paired baseline and work order |
| Before status evidence | base commit `046ba66d`; PKGSOP-T1 SOP closed |
| After status evidence | pipeline checker and gate wiring added |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | checker and governance wiring only |
| Claim boundary | no runtime, provider, package lifecycle, public-sync, or production-readiness expansion |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `pkgsop-t2-package-skill-pipeline-guard-2026-06-30` |
| Expected manifest | checker, test, four hook/catalog files, baseline, work order, completion review |
| Actual changed set | checker, test, four hook/catalog files, baseline, work order, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references private ASSF runtime and internal governance
gates. Public-safe export requires separate public-sync authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 baseline | `docs/baselines/CVF_GC018_PKGSOP_T2_PACKAGE_SKILL_PIPELINE_GUARD_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_PKGSOP_T2_PACKAGE_SKILL_PIPELINE_GUARD_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: no roadmap file changed | no roadmap closure state mutation | PASS |
| Registry JSON | N/A with reason: no ASSF registry mutation | no package lifecycle change | PASS |
| Registry Markdown | N/A with reason: no registry markdown mutation | no package README change | PASS |
| External evidence digest | N/A with reason: no new external evidence artifact | no new external evidence digest | N/A with reason |
| System loop interlock | no runtime mutation | checker-only implementation | PASS |
| Session continuity | session-sync may follow material commit | N/A with reason | PASS |
| Focused tests | checker unit tests and smoke | PASS | PASS |
| Runtime smoke | N/A with reason: no runtime behavior changed | N/A with reason | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Pipeline checker exists | present | `governance/compat/check_package_skill_productionization_pipeline.py` | PASS |
| Focused tests exist | present | `governance/compat/test_check_package_skill_productionization_pipeline.py` | PASS |
| Hook wiring exists | reviewer-fast, pre-commit, pre-push, autorun | changed catalogs include checker command | PASS |
| Package lifecycle mutation | none | none | PASS |
| Runtime/provider call | none | none | PASS |

## Claim Boundary

PKGSOP-T2 creates a read-only checker and gate wiring only. It does not convert
packages, mutate lifecycle sources, implement package runtime behavior, call
providers, public-sync, or grant action authority.
