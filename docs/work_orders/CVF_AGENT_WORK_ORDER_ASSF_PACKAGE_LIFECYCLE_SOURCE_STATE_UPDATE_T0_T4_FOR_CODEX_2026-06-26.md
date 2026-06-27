# CVF Agent Work Order: ASSF Package Lifecycle Source-State Update T0-T4

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: work_order

Batch ID: ASSF-LIFECYCLE-SOURCE-STATE

dispatchBaseHead: 9c48f83b

executionBaseHead: 9c48f83b

closureBaseHead: 9c48f83b

Commit mode: `WORKER_MAY_COMMIT`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_FOR_CODEX_2026-06-26.md`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role executor. This packet authorizes a bounded
source-state update for `cvf-dispatch-quality-reviewer` after accepted
certification evidence.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_FOR_CODEX_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_2026-06-26.md`

## Purpose

Execute T0-T4 lifecycle source-state update, generated-index regeneration, and
metadata resolver verification.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | continue T0-T4 | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Certification decision completion | `docs/reviews/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_COMPLETION_2026-06-26.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_2026-06-26.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | scope authorization |
| Dispatcher | Codex |
| Worker | Codex single-agent multi-role |
| Reviewer | Codex |
| Closer | Codex |
| Session-sync steward | Codex in a separate commit after material closure |

## Scope / Methodology

Codex updates only the selected registry source and generated index, verifies
drift and resolver projection, and closes with a next-control decision. The
material commit must not include active session-sync paths.

## Findings / Position

The accepted certification evidence supports moving the source metadata to
`uatState: PASSED` and `certificationState: CERTIFIED`. This remains metadata
only and does not activate the package.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| T0 | Source authority and mutation protocol | T0 review |
| T1 | Registry source lifecycle update | source diff and T1 review |
| T2 | Generated index regeneration and drift proof | generator output, drift PASS, T2 review |
| T3 | Resolver projection verification | resolver output and T3 review |
| T4 | Closure and next-control decision | T4 and completion review |

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
| baseHeadFor(phase) | dispatchBaseHead=`9c48f83b`; executionBaseHead=`9c48f83b`; closureBaseHead=`9c48f83b` |
| changedSetScope(phase) | material scope only: roadmap, baseline, work order, selected registry source, generated index, T0-T4 reviews, completion review |
| traceScope(phase, actor) | Agent Operation Trace Blocks in this work order and completion review |
| commitOwner(phase) | Codex owns material commit; Codex session-sync steward owns separate sync commit after material closure |
| crossBatchIsolation | do not mix with session-sync, Web, resolver source, CLI/MCP adapter, provider/live, public-sync, or package instance work |
| nextMoveSurfaces | update only after material commit in separate session-sync |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | roadmap, baseline, work order, T0-T4 reviews, selected registry source, generated index, completion review |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | READ | active front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup facts |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | full state registry |
| `AGENT_HANDOFF_V22_2026-06-22.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | READ | guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | literal-format checklist |
| `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | SOURCE_VERIFIED | target source |
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | SOURCE_VERIFIED | lifecycle values |
| `governance/compat/generate_assf_skill_index.py` | SOURCE_VERIFIED | generator |
| `governance/compat/check_assf_skill_index_drift.py` | SOURCE_VERIFIED | drift checker |
| `governance/compat/run_assf_skill_resolver.py` | SOURCE_VERIFIED | resolver |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`assf-lifecycle-source-state-update`, role=`reviewer-closer`, lifecyclePhase=`material-closure`

Returned defects: NONE_RETURNED

- none

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| source entry carries current lifecycle fields | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 67-68 before update | `uatState` | ASSF registry entry | VALUE_SET | ACCEPT |
| T7 lifecycle guard defines `PASSED` as UAT success value | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | line 86 | `PASSED` | ASSF lifecycle guard | VALUE_SET | ACCEPT |
| T7 lifecycle guard defines `CERTIFIED` as accepted certification value | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | line 81 | `CERTIFIED` | ASSF lifecycle guard | VALUE_SET | ACCEPT |
| accepted certification decision released future source-state lane | `docs/reviews/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_COMPLETION_2026-06-26.md` | line 19 | `OPEN_ASSF_PACKAGE_LIFECYCLE_STATE_UPDATE_ROADMAP` | ASSF certification decision completion | VALUE_SET | ACCEPT |
| generator writes generated index from registry entries | `governance/compat/generate_assf_skill_index.py` | line 94 | `generate_index` | ASSF index generator | EXISTS | ACCEPT |
| drift checker verifies generated index | `governance/compat/check_assf_skill_index_drift.py` | module | `main` | ASSF drift checker | EXISTS | ACCEPT |
| resolver returns metadata packet | `governance/compat/run_assf_skill_resolver.py` | line 200 | `resolve_skill_packet` | ASSF resolver | EXISTS | ACCEPT |

## Write Ownership

| Path | Action |
|---|---|
| `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | update review artifacts and lifecycle source state |
| `docs/reference/agent_system_skills/generated/skill-index.json` | regenerate from source |
| `docs/roadmaps/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_ROADMAP_2026-06-26.md` | create and close |
| `docs/baselines/CVF_GC018_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_2026-06-26.md` | create and close |
| `docs/reviews/CVF_ASSF_LIFECYCLE_T0_SOURCE_AUTHORITY_MUTATION_PROTOCOL_2026-06-26.md` | create |
| `docs/reviews/CVF_ASSF_LIFECYCLE_T1_REGISTRY_SOURCE_UPDATE_2026-06-26.md` | create |
| `docs/reviews/CVF_ASSF_LIFECYCLE_T2_GENERATED_INDEX_REGENERATION_DRIFT_PROOF_2026-06-26.md` | create |
| `docs/reviews/CVF_ASSF_LIFECYCLE_T3_RESOLVER_PROJECTION_VERIFICATION_2026-06-26.md` | create |
| `docs/reviews/CVF_ASSF_LIFECYCLE_T4_CLOSURE_NEXT_CONTROL_DECISION_2026-06-26.md` | create |
| `docs/reviews/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_COMPLETION_2026-06-26.md` | create |

## Forbidden Scope

No package instance creation, activation, readiness claim, package instruction
execution, package integration, resolver source mutation, Web projection,
CLI/MCP adapter behavior, provider/live proof, public-sync, push, or
session-sync is authorized in the material commit.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `git diff --name-status` | changed set limited to Write Ownership |
| `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| resolver command | one metadata-only result for target candidate |
| pre-closure autorun | PASS |
| commit steward material preflight | PASS |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | Target source records `uatState: PASSED` | PASS |
| AC2 | Target source records `certificationState: CERTIFIED` | PASS |
| AC3 | Generated index drift checker passes | PASS |
| AC4 | Resolver returns metadata-only target result | PASS |
| AC5 | Forbidden runtime/session/public paths are absent | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local shell and file-edit tools |
| Session or invocation | 2026-06-26 ASSF-LIFECYCLE-SOURCE-STATE material tranche |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, Python governance commands, apply_patch |
| Target paths | selected ASSF registry source, generated index, roadmap, GC-018, work order, T0-T4 reviews, completion review |
| Allowed scope source | operator instruction to continue T0-T4 plus this work order Write Ownership |
| Before status evidence | `git status --short` empty at base `9c48f83b` |
| After status evidence | material changed set listed in Actual changed set |
| Diff evidence | `git diff --name-status` over material worktree |
| Approval boundary | operator authorized T0-T4 only |
| Claim boundary | metadata source-state update only; no runtime, package instance, Web, adapter, provider/live, public-sync, push, or session-sync |
| Agent type | SINGLE_AGENT_MULTI_ROLE |
| Invocation ID | ASSF-LIFECYCLE-SOURCE-STATE-T0-T4-CODEX-2026-06-26 |
| Expected manifest | `docs/baselines/CVF_GC018_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_2026-06-26.md`; `docs/reference/agent_system_skills/generated/skill-index.json`; `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json`; `docs/reviews/CVF_ASSF_LIFECYCLE_T0_SOURCE_AUTHORITY_MUTATION_PROTOCOL_2026-06-26.md`; `docs/reviews/CVF_ASSF_LIFECYCLE_T1_REGISTRY_SOURCE_UPDATE_2026-06-26.md`; `docs/reviews/CVF_ASSF_LIFECYCLE_T2_GENERATED_INDEX_REGENERATION_DRIFT_PROOF_2026-06-26.md`; `docs/reviews/CVF_ASSF_LIFECYCLE_T3_RESOLVER_PROJECTION_VERIFICATION_2026-06-26.md`; `docs/reviews/CVF_ASSF_LIFECYCLE_T4_CLOSURE_NEXT_CONTROL_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_COMPLETION_2026-06-26.md`; `docs/roadmaps/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_ROADMAP_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_FOR_CODEX_2026-06-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_2026-06-26.md`; `docs/reference/agent_system_skills/generated/skill-index.json`; `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json`; `docs/reviews/CVF_ASSF_LIFECYCLE_T0_SOURCE_AUTHORITY_MUTATION_PROTOCOL_2026-06-26.md`; `docs/reviews/CVF_ASSF_LIFECYCLE_T1_REGISTRY_SOURCE_UPDATE_2026-06-26.md`; `docs/reviews/CVF_ASSF_LIFECYCLE_T2_GENERATED_INDEX_REGENERATION_DRIFT_PROOF_2026-06-26.md`; `docs/reviews/CVF_ASSF_LIFECYCLE_T3_RESOLVER_PROJECTION_VERIFICATION_2026-06-26.md`; `docs/reviews/CVF_ASSF_LIFECYCLE_T4_CLOSURE_NEXT_CONTROL_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_COMPLETION_2026-06-26.md`; `docs/roadmaps/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_ROADMAP_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_FOR_CODEX_2026-06-26.md` |
| Manifest delta | MATCH |

## Review Gate

| Gate | Command | Required result |
|---|---|---|
| Structural completeness | `python governance/compat/check_markdown_structural_completeness.py --base 9c48f83b --head HEAD --enforce` | PASS |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 9c48f83b --head HEAD --enforce` | PASS |
| Drift | `python governance/compat/check_assf_skill_index_drift.py` | PASS |

## Closure Checklist

| Item | Status |
|---|---|
| Registry source updated | PASS |
| Generated index regenerated | PASS |
| Resolver verified | PASS |
| Completion review authored | PASS |
| Session-sync excluded from material commit | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` if source update, index regeneration, drift proof,
resolver proof, and closure gates pass. Return `BLOCKED_WITH_REASON` if source
authority contradicts the update or any forbidden surface is required.

## Operator Checkpoint

Operator already authorized T0-T4. A new operator checkpoint is required before
package instance creation, activation, Web projection, CLI/MCP adapter work,
provider/live proof, public-sync, push, or session-sync beyond this material
closure.

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

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | generated index and resolver metadata | metadata may be read; package cannot be activated or executed | drift and resolver proof | no loader or execution bridge | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter | no external mutation or execution authority | adapter fields remain deferred | separate adapter work order required | `DEFERRED_WITH_REASON` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance metadata update; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF lifecycle source-state work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- selected metadata source and generated index only |
| receiptEvidence | CVF_RECEIPT_PRESENT - drift and resolver proof |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- source diff and generated diff |
| invocationBoundary | governed local material update |
| interceptionBoundary | no provider, Web, adapter, runtime, or external mutation claim |
| claimLanguage | lifecycle metadata update only |
| forbiddenExpansion | no package instance, activation, runtime behavior, resolver source mutation, Web projection, CLI/MCP adapter, provider/live proof, public-sync, push, package execution, or package integration |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_T0_T4_COMPLETION_2026-06-26.md` | closure review exists | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_LIFECYCLE_SOURCE_STATE_UPDATE_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lifecycle fields updated | PASS |
| Registry Markdown | N/A with reason: no markdown registry companion applies | JSON source only | BLOCKED with reason: no markdown registry companion exists for this JSON-only ASSF entry |
| External evidence digest | N/A with reason: no external artifact applies | repository-local evidence only | N/A with reason |
| System loop interlock | N/A with reason: no system loop surface changed | no system loop mutation | N/A with reason |
| Session continuity | N/A with reason: material commit excludes session-sync | session-sync follows in separate commit | N/A with reason |

## Claim Boundary

This work order closes a metadata update. It does not authorize runtime,
adapter, Web, provider/live, public-sync, activation, package execution, or
session-sync behavior.
