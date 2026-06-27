# CVF Agent Work Order - ERQP-T0-T4 Evidence Readout Quick Packet Template

Memory class: WORK_ORDER

Status: CLOSED_PASS_BOUNDED

Owner: Codex

Base head: `f94f7ef6`

## Dispatch Prompt Envelope

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_FOR_CODEX_2026-06-27.md`

dispatchBaseHead: `f94f7ef6`

executionBaseHead: `f94f7ef6`

closureBaseHead: `f94f7ef6`

workerCommitMode: `CODEX_MAY_COMMIT_AFTER_GATES`

mission: Execute and close the ERQP-T0-T4 evidence/readout quick-packet
template batch without runtime, UI, checker, provider/live, adapter, resolver,
package, public-sync, generated workspace state, DICE, or push scope.

## Purpose

Create and close the bounded template/reference packet recommended by EFRD for
reducing operator friction in existing evidence/readout surfaces.

## 1. Mission

Define the minimal one-page evidence/readout quick-packet template for future
operators and agents before any implementation lane is opened.

## 2. Authority Chain

- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V23_2026-06-26.md`.
- Handoff contract: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.
- EFRD reference: `docs/reference/CVF_EVIDENCE_READOUT_FRICTION_REDUCTION_DECISION.md`.
- EFRD closure: `docs/reviews/CVF_EFRD_T0_T4_EVIDENCE_READOUT_FRICTION_REDUCTION_DECISION_COMPLETION_2026-06-27.md`.
- Roadmap: `docs/roadmaps/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_ROADMAP_2026-06-27.md`.
- GC-018: `docs/baselines/CVF_GC018_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_2026-06-27.md`.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author authority packet |
| Worker | Codex | execute bounded markdown/reference edits |
| Reviewer | Codex | review changed set against work order |
| Closer | Codex | commit material after gates |
| Session-sync steward | Codex | update session surfaces in a separate commit |

## Required First Reads

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |

## Pre-Flight Checks

| Command | Expected result |
|---|---|
| `git status --short` | clean before material edits |
| `git rev-parse --short HEAD` | `f94f7ef6` before material edits |
| `python governance/compat/run_adif_defect_resolver.py --query "taskClass=evidence_readout_quick_packet role=dispatcher lifecyclePhase=dispatch"` | no returned defect IDs |

## Write Ownership

Allowed material paths:

- `docs/roadmaps/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_ROADMAP_2026-06-27.md`
- `docs/baselines/CVF_GC018_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_2026-06-27.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_FOR_CODEX_2026-06-27.md`
- `docs/reference/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE.md`
- `docs/reviews/CVF_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_COMPLETION_2026-06-27.md`

## Execution Plan

| Step | Action |
|---|---|
| ERQP-T0 | Source-verify quick-packet authority |
| ERQP-T1 | Map packet fields to existing surfaces |
| ERQP-T2 | Add stable quick-packet template reference |
| ERQP-T3 | Record use boundary and future escalation rule |
| ERQP-T4 | Run gates and commit material |

## Evidence Requirements

- Source Verification Block must cite existing CVF-owned source paths.
- Stable template must be read-only and reference-only.
- Runtime, UI, checker, provider/live, adapter, resolver, package,
  public-sync, generated-state, DICE, and push scope must remain blocked.
- Session-sync must be separate from material commit.

## 3. Allowed Scope

- Add the roadmap, GC-018, work order, stable template reference, and
  completion review named in this packet.
- Run source-verification and governance gates.
- Commit material after gates pass.
- Perform separate session-sync only after material commit succeeds.

## 4. Forbidden Scope

- Runtime, MCP, CLI, or IDE bridge implementation.
- UI or dashboard implementation.
- Checker implementation.
- Further provider/live proof.
- Generated workspace state mutation.
- Resolver or adapter mutation.
- Package activation or certification decision.
- Public-sync or push.
- DICE work.
- Mixing material commit with session-sync commit.

## Source Inventory

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | READ |
| `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | READ |
| `docs/reference/CVF_EVIDENCE_READOUT_FRICTION_REDUCTION_DECISION.md` | SOURCE_VERIFIED |
| `docs/reviews/CVF_EFRD_T0_T4_EVIDENCE_READOUT_FRICTION_REDUCTION_DECISION_COMPLETION_2026-06-27.md` | SOURCE_VERIFIED |
| `docs/reviews/CVF_WORKFLOW_VALUE_PROOF_T0_T4_COMPLETION_2026-06-27.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | SOURCE_VERIFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Current next allowed move authorizes an optional EVIDENCE_READOUT_QUICK_PACKET non-runtime template lane | `CVF_SESSION_MEMORY.md` | Next Allowed Move | `evidence_readout_friction_decision_closed_pass_bounded_pending_quick_packet_or_foundation_selection` | active session front door | ACCEPT |
| EFRD reference recommends a reusable non-runtime quick-packet lane | `docs/reference/CVF_EVIDENCE_READOUT_FRICTION_REDUCTION_DECISION.md` | Next-Control Recommendation | `EVIDENCE_READOUT_QUICK_PACKET` | EFRD decision reference | ACCEPT |
| EFRD completion says the next lane should remain optional and small | `docs/reviews/CVF_EFRD_T0_T4_EVIDENCE_READOUT_FRICTION_REDUCTION_DECISION_COMPLETION_2026-06-27.md` | Next-Control Recommendation | `EVIDENCE_READOUT_QUICK_PACKET` | EFRD completion review | ACCEPT |
| WVP records paperwork load as confirmed friction | `docs/reviews/CVF_WORKFLOW_VALUE_PROOF_T0_T4_COMPLETION_2026-06-27.md` | Value Verdict | `Paperwork load`; `FRICTION_CONFIRMED` | WVP completion review | ACCEPT |
| Read-model decision maps required evidence and closure readiness to governed sources | `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md` | Projection Sections | `requiredEvidence`; `closureReadiness` | local workspace projection read model | ACCEPT |
| Operator view plan defines current-mode, guard-status, and next-move sections | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | Read Model Sections | `Current Mode`; `Guard Status`; `Next Move` | operator view plan | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`evidence_readout_quick_packet`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Roadmap-To-Work-Order Trace Matrix

| Roadmap item | Work order task | Evidence |
|---|---|---|
| ERQP-T0 authority | source verification | source rows |
| ERQP-T1 field set | map fields to surfaces | roadmap matrix |
| ERQP-T2 stable template | add template reference | reference file |
| ERQP-T3 next boundary | record next-control recommendation | completion review |
| ERQP-T4 closure | run gates and commit | completion review |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| routeToken | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | codex_dispatch_implementation_review_closure_session_sync |
| contractSource | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| baseHeadFor(phase) | dispatch=`f94f7ef6`; execution=`f94f7ef6`; closure=`f94f7ef6`; session-sync=material commit |
| changedSetScope(phase) | roadmap, GC-018, work order, stable template reference, completion review |
| traceScope(phase, actor) | Agent Operation Trace Block in roadmap, work order, reference, and completion review |
| commitOwner(phase) | Codex for material after gates; Codex for separate session-sync after material commit |
| crossBatchIsolation | material and session-sync commits must be separate |
| nextMoveSurfaces | update active session, front door, and active handoff only after material commit |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | reduce evidence/readout assembly friction before any workspace implementation |
| Contract source | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| Front door | `CVF_SESSION_MEMORY.md` and `docs/reference/agent_workspace/README.md` |
| Storage class | one stable template reference plus dated governed evidence artifacts |
| Handoff fields | active session and AHB fields remain source of truth |
| State ownership | no generated workspace state mutation in this batch |
| Guard owner | `governance/compat/check_agent_workspace_design.py` |
| Build boundary | template/reference only; no workspace build, UI, runtime source, provider proof, public-sync, registry edits, checker, or adapter implementation |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| stableFoundationPath | `docs/reference/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE.md` |
| datedEvidencePaths | roadmap, GC-018, work order, and completion review |
| indexOrFrontDoor | active session front door remains `CVF_SESSION_MEMORY.md` |
| storageDecision | stable template reference is not date-suffixed; evidence artifacts are date-suffixed |
| archivePolicy | future replacement requires governed archive/supersession batch |
| claimBoundary | no raw package import, runtime queue, MCP, CLI, IDE bridge, provider expansion, public-sync, generated workspace state mutation, checker, resolver, or adapter mutation |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ERQP template reference | internal agents may use it for manual quick-packet assembly only | this work order and reference | N/A with reason: no adapter created | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future external-agent readout support remains deferred | no executable external-agent support | claim boundary | deferred adapter owner; fresh GC-018 required | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator continuation is authorization context only; source facts are re-verified against CVF-governed surfaces |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | governed roadmap, baseline, work-order, reference, and review artifact surfaces |
| Disposition | ADAPT continuation into CVF-owned template/reference artifacts |
| Claim boundary | no external prompt is used as source proof for runtime fields, package facts, live results, or public claims |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ERQP-T0-T4 work order execution |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: source verification and gate output |
| actionEvidence | ACTION_EVIDENCE_PRESENT: material changed-set and completion review |
| invocationBoundary | local source reads and governed markdown/reference edits only |
| interceptionBoundary | no runtime interception or adapter behavior changed |
| claimLanguage | evidence/readout quick-packet template only |
| forbiddenExpansion | no runtime, UI, checker, MCP, CLI, IDE bridge, further provider/live proof, public-sync, generated workspace state mutation, resolver mutation, adapter mutation, package activation, certification decision, DICE, or push |

## Current Runtime Freshness Verification

| Runtime claim | Current evidence | Disposition |
|---|---|---|
| Runtime implementation | no runtime path is in Write Ownership | NOT_IMPLEMENTED_WITH_REASON |
| UI or dashboard implementation | no UI path is in Write Ownership | NOT_IMPLEMENTED_WITH_REASON |
| Checker implementation | no checker path is in Write Ownership | NOT_IMPLEMENTED_WITH_REASON |
| MCP or CLI adapter | no MCP or CLI adapter path is in Write Ownership | NOT_IMPLEMENTED_WITH_REASON |
| Provider/live proof | no provider/live command is authorized or run | NOT_IMPLEMENTED_WITH_REASON |
| Generated workspace state mutation | generated workspace state is outside Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |

## Planned Artifact Manifest

| Path | Purpose |
|---|---|
| `docs/roadmaps/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_ROADMAP_2026-06-27.md` | roadmap |
| `docs/baselines/CVF_GC018_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_2026-06-27.md` | baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_FOR_CODEX_2026-06-27.md` | work order |
| `docs/reference/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE.md` | stable template reference |
| `docs/reviews/CVF_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_COMPLETION_2026-06-27.md` | completion review |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Quick-packet authority source-verified | Source Verification Block |
| Packet fields mapped to existing sources | Quick-Packet Field Matrix |
| Stable template reference added | reference file |
| Runtime, checker, and adapter scope blocked | control blocks and claim boundary |
| Governance gates pass | command output |
| Material commit separate from session-sync | commit history |

## Review Gate

Required gates before material commit:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base f94f7ef6 --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base f94f7ef6 --head HEAD --enforce`
- `git diff --check`

## Closure Checklist

- [x] Roadmap authored.
- [x] GC-018 authored.
- [x] Work order authored.
- [x] Stable template reference authored.
- [x] Completion review authored.
- [x] Forbidden runtime/provider/public/adapter/generated-state/checker scope remains blocked.

## Operator Checkpoint

No operator checkpoint is required unless a gate demands scope outside this
work order.

## Return-To-Orchestrator Conditions

- Source verification fails for a required field.
- A gate requires runtime, UI, checker, provider/live, public, adapter,
  resolver, generated workspace state, package activation, certification, DICE,
  or push scope.
- Worktree contains unrelated changes outside allowed scope.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_FOR_CODEX_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_ROADMAP_2026-06-27.md` | `Status: ROADMAP_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | no corpus registry source edit required | N/A | BLOCKED with reason: no corpus registry source edit authorized |
| Registry Markdown | no registry Markdown edit authorized | N/A | BLOCKED with reason: no registry Markdown edit authorized |
| External evidence digest | no external evidence file is promoted as CVF source authority | all claims reverified against CVF-governed source rows | BLOCKED with reason: no external evidence artifact is promoted |
| System loop interlock | no system-loop registry mutation in scope | `governance/compat/check_system_loop_interlock.py` via autorun | PASS |
| Session continuity | session-sync required after material commit | active session state and handoff after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Runtime mode | REFERENCE_ONLY | REFERENCE_ONLY | PASS |
| Stable template path | `docs/reference/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE.md` | present in Planned Artifact Manifest | PASS |
| Runtime mutation | none | no runtime path in Write Ownership | PASS |
| Checker mutation | none | no checker path in Write Ownership | PASS |
| Session-sync split | separate commit after material | required by this work order | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-27 ERQP-T0-T4 evidence readout quick packet template |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, python governance gates, git |
| Target paths | roadmap, GC-018, work order, stable template reference, completion review |
| Allowed scope source | active session next allowed move after EFRD-T0-T4 |
| Before status evidence | HEAD `f94f7ef6`; clean worktree |
| After status evidence | material closure pending commit |
| Diff evidence | `git diff --name-status f94f7ef6..HEAD` |
| Approval boundary | evidence/readout quick-packet template only |
| Claim boundary | no runtime, UI, checker, MCP, CLI, IDE bridge, further provider/live proof, public-sync, generated workspace state mutation, resolver mutation, adapter mutation, package activation, certification decision, DICE, or push |
| Agent type | Codex dispatcher/implementer/reviewer/closer |
| Invocation ID | `erqp-t0-t4-evidence-readout-quick-packet-template-2026-06-27` |
| Expected manifest | `docs/roadmaps/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_ROADMAP_2026-06-27.md`; `docs/baselines/CVF_GC018_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_FOR_CODEX_2026-06-27.md`; `docs/reference/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE.md`; `docs/reviews/CVF_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_COMPLETION_2026-06-27.md` |
| Actual changed set | `docs/roadmaps/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_ROADMAP_2026-06-27.md`; `docs/baselines/CVF_GC018_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_FOR_CODEX_2026-06-27.md`; `docs/reference/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE.md`; `docs/reviews/CVF_ERQP_T0_T4_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE_COMPLETION_2026-06-27.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance template/reference work. No public-sync batch is
authorized.

## Claim Boundary

This work order is closed bounded for an evidence/readout quick-packet template
only. It does not authorize runtime, UI, checker, MCP, CLI, IDE bridge, further
provider/live proof, public-sync, generated workspace state mutation, resolver
mutation, adapter mutation, package activation, certification decision, DICE,
production readiness, public readiness, or push.
