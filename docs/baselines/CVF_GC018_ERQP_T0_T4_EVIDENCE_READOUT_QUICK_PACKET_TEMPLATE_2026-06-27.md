# GC-018 - ERQP-T0-T4 Evidence Readout Quick Packet Template

Memory class: GC_018_BASELINE

Status: CLOSED_PASS_BOUNDED

Owner: Codex

Date: 2026-06-27

Base head: `f94f7ef6`

## Baseline Decision

Decision: authorize and close a bounded `REFERENCE_ONLY` evidence/readout
quick-packet template batch.

## Purpose

Authorize the small non-runtime template lane recommended by EFRD-T0-T4,
without opening runtime, UI, checker, provider/live, adapter, package,
public-sync, generated-state, or DICE work.

## Scope / Methodology

Scope: roadmap, GC-018, work order, stable quick-packet template reference, and
completion review.

Methodology: source-verify the EFRD quick-packet recommendation, map packet
fields to existing readout sources, record a stable template, run governance
gates, and keep session-sync separate after material commit.

## Findings / Position

ERQP reduces friction by making a one-page readout packet mechanically
repeatable by future agents without creating a new execution surface. It tells
the next agent what fields to include and where each field must be sourced.

## Proposed Tranche

| Tranche | Scope | Disposition |
|---|---|---|
| ERQP-T0 | Source-verify quick-packet authority | COMPLETE |
| ERQP-T1 | Define quick-packet field set | COMPLETE |
| ERQP-T2 | Add stable template reference | COMPLETE |
| ERQP-T3 | Record use boundary and future escalation | COMPLETE |
| ERQP-T4 | Closure and gates | COMPLETE |

## Source Inventory

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
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

| Roadmap item | Work order section | Completion evidence |
|---|---|---|
| ERQP-T0 authority | Source Verification Block | this baseline and roadmap |
| ERQP-T1 packet fields | Quick-Packet Field Matrix | template reference |
| ERQP-T2 stable template | Planned Artifact Manifest | stable template reference |
| ERQP-T3 use boundary | Next-Control Recommendation | completion review |
| ERQP-T4 closure | Machine Closure Package | completion review and gates |

## Allowed Scope

- Add this GC-018 baseline.
- Add the matching roadmap.
- Add the matching work order.
- Add `docs/reference/CVF_EVIDENCE_READOUT_QUICK_PACKET_TEMPLATE.md`.
- Add the matching completion review.
- Run governance gates and commit material after gates pass.

## Forbidden Scope

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

## Current Runtime Freshness Verification

| Runtime claim | Current evidence | Disposition |
|---|---|---|
| Runtime implementation | no runtime path is in Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |
| UI or dashboard implementation | no UI path is in Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |
| Checker implementation | no checker path is in Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |
| MCP or CLI adapter | no MCP or CLI adapter path is in Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |
| Provider/live proof | no further provider/live proof is authorized or run | NOT_IMPLEMENTED_WITH_REASON |
| Generated workspace state mutation | generated workspace state is outside Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ERQP template reference | internal agents may use the template for manual readout assembly only | source verification and completion review | N/A with reason: no adapter created | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future external-agent readout support remains deferred | no executable external-agent support or CLI/MCP ingress claim | claim boundary | deferred adapter owner; fresh GC-018 required | DEFERRED_WITH_REASON |

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
| claimScope | GC-018 authorization for ERQP template/reference work |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: source verification, completion review, and gate output |
| actionEvidence | ACTION_EVIDENCE_PRESENT: planned material manifest and completion evidence |
| invocationBoundary | local source reads and governed markdown/reference edits only |
| interceptionBoundary | no runtime interception or adapter behavior changed |
| claimLanguage | evidence/readout quick-packet template only |
| forbiddenExpansion | no runtime, UI, checker, MCP, CLI, IDE bridge, further provider/live proof, public-sync, generated workspace state mutation, resolver mutation, adapter mutation, package activation, certification decision, DICE, or push |

## Acceptance Criteria

| Criterion | Evidence |
|---|---|
| Quick-packet authority source-verified | Source Verification Block |
| Packet field set maps to existing sources | roadmap and template reference |
| Stable template reference exists | reference file |
| Runtime, checker, and adapter scope blocked | claim boundaries |
| Governance gates pass | command output |

## Evidence / Verification

Required verification before material commit:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base f94f7ef6 --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base f94f7ef6 --head HEAD --enforce`
- `git diff --check`

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

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance template/reference work. No public-sync batch is
authorized.

## Claim Boundary

This GC-018 authorizes only evidence/readout quick-packet template and
reference work. It does not authorize runtime, UI, checker, MCP, CLI, IDE
bridge, further provider/live proof, public-sync, generated workspace state
mutation, resolver mutation, adapter mutation, package activation,
certification decision, DICE, production readiness, public readiness, or push.
