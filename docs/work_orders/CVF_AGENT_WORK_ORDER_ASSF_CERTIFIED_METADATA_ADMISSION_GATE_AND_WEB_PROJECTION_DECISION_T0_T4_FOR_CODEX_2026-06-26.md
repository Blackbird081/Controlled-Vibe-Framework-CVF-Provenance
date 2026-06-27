# CVF Agent Work Order: ASSF Certified Metadata Admission Gate And Web Projection Decision T0-T4

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: work_order

Batch ID: ASSF-CERTIFIED-METADATA-ADMISSION

dispatchBaseHead: a790bf58

executionBaseHead: a790bf58

closureBaseHead: a790bf58

Commit mode: `WORKER_MAY_COMMIT`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_FOR_CODEX_2026-06-26.md`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role executor. This packet authorizes a bounded
ASSF certified metadata admission checker and Web projection decision, not Web
implementation.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_FOR_CODEX_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_2026-06-26.md`

## Purpose

Execute T0-T4 for the certified metadata admission gate and Web projection
decision.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | continue T0-T4 | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Paired roadmap | `docs/roadmaps/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_ROADMAP_2026-06-26.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_2026-06-26.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | scope authorization |
| Dispatcher | Codex |
| Worker | Codex single-agent multi-role |
| Reviewer | Codex |
| Closer | Codex |
| Session-sync steward | Codex in a separate commit if session state changes |

## Scope / Methodology

Codex implements a read-only checker, adds focused tests, records direct gate
proof, and parks Web projection behind a future source-verified work order.

## Findings / Position

The currently certified ASSF metadata needs a machine gate before downstream
surfaces rely on it. This work order closes that control without broadening
package authority.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| T0 | Source inventory and authority | T0 review |
| T1 | Checker implementation and tests | checker, test file, T1 review |
| T2 | Gate execution and resolver readout | command evidence and T2 review |
| T3 | Web projection decision | T3 review |
| T4 | Closure next control | T4 and completion review |

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role reviewer --phase PRE_DISPATCH --surface governance/compat --risk-ceiling R0
```

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| contractSource | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex acts as dispatcher, worker, reviewer, and closer for this local material tranche |
| phase | dispatch, execution, closure |
| baseHeadFor(phase) | dispatchBaseHead=`a790bf58`; executionBaseHead=`a790bf58`; closureBaseHead=`a790bf58` |
| changedSetScope(phase) | material scope only: checker, tests, roadmap, GC-018, work order, T0-T4 reviews, completion review |
| traceScope(phase, actor) | Agent Operation Trace Blocks in this work order and completion review |
| commitOwner(phase) | Codex owns material commit; Codex session-sync steward owns separate sync commit if needed |
| crossBatchIsolation | do not mix with session-sync, Web implementation, resolver source mutation, CLI/MCP adapter, provider/live, public-sync, or package instance work |
| nextMoveSurfaces | update only after material commit in separate session-sync if needed |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | roadmap, baseline, work order, checker, tests, T0-T4 reviews, completion review |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | READ | active front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup facts |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | full state registry |
| `AGENT_HANDOFF_V22_2026-06-22.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | READ | guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | literal-format checklist |
| `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | SOURCE_VERIFIED | certified source metadata |
| `docs/reference/agent_system_skills/generated/skill-index.json` | SOURCE_VERIFIED | generated read model |
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | SOURCE_VERIFIED | lifecycle and Web bridge rules |
| `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | SOURCE_VERIFIED | Web projection boundary |
| `governance/compat/generate_assf_skill_index.py` | SOURCE_VERIFIED | index source validation API |
| `governance/compat/run_assf_skill_resolver.py` | SOURCE_VERIFIED | metadata-only resolver |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`assf-certified-metadata-admission-gate`, role=`reviewer-closer`, lifecyclePhase=`material-closure`

Returned defects: NONE_RETURNED

- none

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| certified source metadata exists | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 71-83 | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| generated index carries certified metadata | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 16-92 | `skills[0]` | ASSF generated index | VALUE_SET | ACCEPT |
| certification requires UAT pass | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 89-91 | `uatState` | lifecycle guard contract | LITERAL_INVARIANT | ACCEPT |
| adapter implemented claim requires evidence | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 138-148 | `adapterEvidence` | adapter claim honesty rules | LITERAL_INVARIANT | ACCEPT |
| Web projection requires later source-verified work order | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 171-183 | `CERTIFIED_PACKAGE_PROJECTION` | Web bridge rule | LITERAL_INVARIANT | ACCEPT |
| generated index validation API exists | `governance/compat/generate_assf_skill_index.py` | lines 107-115 | `validate_index_matches_sources` | ASSF index generator | EXISTS | ACCEPT |
| resolver command entry point exists | `governance/compat/run_assf_skill_resolver.py` | lines 202-267 | `resolve_skill_packet` | ASSF resolver | EXISTS | ACCEPT |

## Write Ownership

| Path | Action |
|---|---|
| `governance/compat/check_assf_certified_metadata_admission.py` | create read-only checker |
| `governance/compat/test_check_assf_certified_metadata_admission.py` | create focused tests |
| `docs/roadmaps/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_ROADMAP_2026-06-26.md` | create and close |
| `docs/baselines/CVF_GC018_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_2026-06-26.md` | create and close |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_FOR_CODEX_2026-06-26.md` | create and close |
| `docs/reviews/CVF_ASSF_ADMISSION_T0_SOURCE_INVENTORY_AND_AUTHORITY_2026-06-26.md` | create |
| `docs/reviews/CVF_ASSF_ADMISSION_T1_CERTIFIED_METADATA_CHECKER_IMPLEMENTATION_2026-06-26.md` | create |
| `docs/reviews/CVF_ASSF_ADMISSION_T2_GATE_EXECUTION_AND_READ_MODEL_PROOF_2026-06-26.md` | create |
| `docs/reviews/CVF_ASSF_ADMISSION_T3_WEB_PROJECTION_DECISION_2026-06-26.md` | create |
| `docs/reviews/CVF_ASSF_ADMISSION_T4_CLOSURE_NEXT_CONTROL_2026-06-26.md` | create |
| `docs/reviews/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_COMPLETION_2026-06-26.md` | create |

## Forbidden Scope

No package instance creation, certification decision, generated-index mutation,
resolver source mutation, Web runtime change, CLI/MCP adapter, provider/live
proof, public-sync, push, or session-sync is authorized in the material commit.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `python -m unittest governance.compat.test_check_assf_certified_metadata_admission` | PASS |
| `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | PASS |
| `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| resolver command | PASS, one metadata-only candidate |
| pre-closure autorun | PASS |
| commit steward material preflight | PASS |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | Checker blocks certified metadata without UAT pass | PASS |
| AC2 | Checker blocks missing review artifacts | PASS |
| AC3 | Checker blocks generated index drift | PASS |
| AC4 | Checker blocks unsupported adapter implemented claims | PASS |
| AC5 | Web projection implementation remains out of scope | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local shell and file-edit tools |
| Session or invocation | 2026-06-26 ASSF-CERTIFIED-METADATA-ADMISSION material tranche |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, Python governance commands, apply_patch |
| Target paths | checker, tests, roadmap, GC-018, work order, T0-T4 reviews, completion review |
| Allowed scope source | operator instruction to continue T0-T4 plus this work order Write Ownership |
| Before status evidence | `git status --short` empty at base `a790bf58` |
| After status evidence | material changed set listed in Actual changed set |
| Diff evidence | `git diff --name-status` over material worktree |
| Approval boundary | operator authorized T0-T4 only |
| Claim boundary | admission checker and decision artifacts only; no runtime, package instance, Web implementation, adapter, provider/live, public-sync, push, or session-sync |
| Agent type | SINGLE_AGENT_MULTI_ROLE |
| Invocation ID | ASSF-CERTIFIED-METADATA-ADMISSION-T0-T4-CODEX-2026-06-26 |
| Expected manifest | `governance/compat/check_assf_certified_metadata_admission.py`; `governance/compat/test_check_assf_certified_metadata_admission.py`; `docs/roadmaps/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_ROADMAP_2026-06-26.md`; `docs/baselines/CVF_GC018_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_FOR_CODEX_2026-06-26.md`; `docs/reviews/CVF_ASSF_ADMISSION_T0_SOURCE_INVENTORY_AND_AUTHORITY_2026-06-26.md`; `docs/reviews/CVF_ASSF_ADMISSION_T1_CERTIFIED_METADATA_CHECKER_IMPLEMENTATION_2026-06-26.md`; `docs/reviews/CVF_ASSF_ADMISSION_T2_GATE_EXECUTION_AND_READ_MODEL_PROOF_2026-06-26.md`; `docs/reviews/CVF_ASSF_ADMISSION_T3_WEB_PROJECTION_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_ADMISSION_T4_CLOSURE_NEXT_CONTROL_2026-06-26.md`; `docs/reviews/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_COMPLETION_2026-06-26.md` |
| Actual changed set | `governance/compat/check_assf_certified_metadata_admission.py`; `governance/compat/test_check_assf_certified_metadata_admission.py`; `docs/roadmaps/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_ROADMAP_2026-06-26.md`; `docs/baselines/CVF_GC018_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_FOR_CODEX_2026-06-26.md`; `docs/reviews/CVF_ASSF_ADMISSION_T0_SOURCE_INVENTORY_AND_AUTHORITY_2026-06-26.md`; `docs/reviews/CVF_ASSF_ADMISSION_T1_CERTIFIED_METADATA_CHECKER_IMPLEMENTATION_2026-06-26.md`; `docs/reviews/CVF_ASSF_ADMISSION_T2_GATE_EXECUTION_AND_READ_MODEL_PROOF_2026-06-26.md`; `docs/reviews/CVF_ASSF_ADMISSION_T3_WEB_PROJECTION_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_ADMISSION_T4_CLOSURE_NEXT_CONTROL_2026-06-26.md`; `docs/reviews/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_COMPLETION_2026-06-26.md` |
| Manifest delta | MATCH |

## Review Gate

| Gate | Command | Required result |
|---|---|---|
| Unit tests | `python -m unittest governance.compat.test_check_assf_certified_metadata_admission` | PASS |
| Admission gate | `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | PASS |
| Drift | `python governance/compat/check_assf_skill_index_drift.py` | PASS |

## Closure Checklist

| Item | Status |
|---|---|
| Source inventory completed | PASS |
| Admission checker implemented | PASS |
| Focused tests passed | PASS |
| Web projection parked | PASS |
| Session-sync excluded from material commit | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` if the checker, tests, direct gate, drift proof,
resolver proof, and closure gates pass. Return `BLOCKED_WITH_REASON` if any
forbidden runtime/Web/resolver/adapter/session surface is required.

## Operator Checkpoint

Operator authorized this T0-T4 lane. A new operator checkpoint is required
before Web projection implementation, package instance creation, activation,
CLI/MCP adapter work, provider/live proof, public-sync, push, or session-sync
beyond closure continuity.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | direct operator authorization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance control; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF certified metadata admission work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- checker and decision artifacts only |
| receiptEvidence | CVF_RECEIPT_PRESENT - tests and gate proof |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- checker, tests, artifacts |
| invocationBoundary | governed local material update |
| interceptionBoundary | no provider, Web, adapter, runtime, resolver mutation, or external mutation claim |
| claimLanguage | admission gate closed bounded |
| forbiddenExpansion | no package instance, activation, runtime behavior, resolver source mutation, Web projection implementation, CLI/MCP adapter, provider/live proof, public-sync, push, package execution, or session-sync |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_COMPLETION_2026-06-26.md` | completion review exists | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | read-only source consumed by checker | PASS |
| Registry Markdown | N/A with reason: no markdown registry companion applies | JSON source only | BLOCKED with reason: no markdown registry companion exists for this JSON-only ASSF entry |
| External evidence digest | N/A with reason: no external artifact applies | repository-local evidence only | N/A with reason |
| System loop interlock | N/A with reason: no system loop surface changed | no system loop mutation | N/A with reason |
| Session continuity | N/A with reason: material commit excludes session-sync | session-sync follows separately if needed | N/A with reason |

## Claim Boundary

This work order closes admission checker and decision work only.
