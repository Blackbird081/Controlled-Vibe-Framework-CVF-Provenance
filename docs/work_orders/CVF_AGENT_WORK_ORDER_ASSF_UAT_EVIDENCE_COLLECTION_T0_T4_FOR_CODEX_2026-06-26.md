# CVF Agent Work Order: ASSF-UAT Evidence Collection T0-T4

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: work_order

Batch ID: ASSF-UAT

dispatchBaseHead: 110b64bf

executionBaseHead: 110b64bf

closureBaseHead: 110b64bf

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role executor. This packet authorizes local
documentation-only ASSF-UAT T0-T4 closure.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_FOR_CODEX_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_2026-06-26.md`

Do-not-misread notes: this work order does not authorize package instance
creation, certification decision, lifecycle mutation, registry mutation,
generated-index mutation, resolver mutation, Web runtime change, CLI/MCP
adapter behavior, provider/live proof, public-sync, push, activation,
readiness claim, package instruction execution, or session-sync in the
material commit.

## Purpose

Complete ASSF-UAT T0-T4 for `cvf-dispatch-quality-reviewer`: protocol,
static evidence, manual UAT script, certification-readiness decision, and
checker-reopen decision.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | approve Codex multi-role completion of T0-T4 | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Prior ASSF-PIC roadmap closure | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | ACCEPT |
| Paired baseline | `docs/baselines/CVF_GC018_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_2026-06-26.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | scope approval |
| Dispatcher | Codex |
| Worker | Codex single-agent multi-role |
| Reviewer | Codex |
| Closer | Codex |
| Session-sync steward | Codex in a separate commit after material closure |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | READ | active front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup facts |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | active state registry |
| `AGENT_HANDOFF_V22_2026-06-22.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | READ | guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | literal-format checklist |
| `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | READ | selected candidate source |
| `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | READ | package schema |
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | READ | UAT/certification rules |

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0
```

## Scope / Methodology

Codex reads source artifacts, authors the roadmap, baseline, work order, T0-T4
reviews, and completion review, then runs gates and commits material before any
session-sync.

## Findings / Position

The candidate is ready for a future manual UAT run, not for certification in
this batch.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/roadmaps/CVF_ASSF_PACKAGE_CANDIDATE_UAT_EVIDENCE_COLLECTION_ROADMAP_2026-06-26.md` | Codex | create and close roadmap |
| `docs/baselines/CVF_GC018_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_2026-06-26.md` | Codex | create and close baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_FOR_CODEX_2026-06-26.md` | Codex | create and close work order |
| `docs/reviews/CVF_ASSF_UAT_T0_EVIDENCE_PROTOCOL_AND_WORK_ORDER_COMPLETION_2026-06-26.md` | Codex | create T0 closure |
| `docs/reviews/CVF_ASSF_UAT_T1_STATIC_PACKAGE_CANDIDATE_EVIDENCE_2026-06-26.md` | Codex | create T1 review |
| `docs/reviews/CVF_ASSF_UAT_T2_MANUAL_OPERATOR_UAT_SCRIPT_2026-06-26.md` | Codex | create T2 script |
| `docs/reviews/CVF_ASSF_UAT_T3_EVIDENCE_REVIEW_CERTIFICATION_READINESS_DECISION_2026-06-26.md` | Codex | create T3 decision |
| `docs/reviews/CVF_ASSF_UAT_T4_CHECKER_IMPLEMENTATION_REOPEN_DECISION_2026-06-26.md` | Codex | create T4 decision |
| `docs/reviews/CVF_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_COMPLETION_2026-06-26.md` | Codex | create completion review |

## Forbidden Changed Paths And Actions

No package source entry, generated index, resolver source, Web runtime, adapter
source, provider/live proof, public-sync, push, package activation, lifecycle
mutation, certification decision, or session-sync path is inside this material
work order.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| candidate identity is source-backed | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `skillId` | ASSF registry entry | VALUE_SET | ACCEPT |
| candidate UAT state is not started | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `uatState` | ASSF registry entry | VALUE_SET | ACCEPT |
| candidate certification state is not started | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| lifecycle guard requires passed UAT before certification | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `uatState` | ASSF-T7 lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| package contract defines external adapter disposition fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Internal-Agent And External-Agent CLI/MCP Disposition Fields | `externalCliMcpDisposition` | ASSF package contract | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| Selected registry entry | read current source entry | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lifecycle fields remain not started; external adapter remains deferred |
| Generated index drift | ran current drift check | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| Resolver readout | ran current resolver query | `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0` | metadata-only candidate readout |

## Worker Return Packet Shape Contract

This single-agent multi-role work order does not require a separate worker
return artifact, but because the commit mode is `WORKER_MUST_NOT_COMMIT`, the
packet shape contract is recorded for gate compatibility and future external
worker reuse.

Required worker-return sections if this work is delegated later:

- `Status`
- `dispatchWorkOrder`
- `Purpose`
- `Source Inventory`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Claim Boundary`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Worker Return Scaffold Effectiveness Measurement`
- `Machine Closure Package`
- actual `executionBaseHead`
- actual `git status --short`
- changed-path list
- command evidence
- no commit statement

If any section is not applicable, include the section with `N/A with reason`
or `NOT_APPLICABLE_WITH_REASON` and a short reason instead of omitting it.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate marker in boundary prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatches, executes, reviews, and closes this documentation batch |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=110b64bf`; `executionBaseHead=110b64bf`; `closureBaseHead=110b64bf` |
| changedSetScope(phase) | material closure paths only; session-sync follows separately |
| traceScope(phase, actor) | Codex trace covers material artifacts only |
| commitOwner(phase) | Codex owns material commit and later session-sync commit |
| crossBatchIsolation | material closure is separate from session-sync |
| nextMoveSurfaces | updated only after material commit succeeds |
| Closer designation | Codex is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | roadmap, baseline, this work order, T0-T4 reviews, completion review |
| workerReturnStatus | N/A with reason: Codex is executing single-agent multi-role closure |
| closer | Codex |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator direction to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | local documentation decision only |
| Claim boundary | no external material absorbed |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order coverage | Output artifact | Status |
|---|---|---|---|
| T0 evidence protocol | Required T0 review | T0 completion | PASS |
| T1 static candidate evidence | Required T1 review | T1 review | PASS |
| T2 manual UAT script | Required T2 review | T2 script | PASS |
| T3 certification-readiness decision | Required T3 decision | T3 decision | PASS |
| T4 checker reopen decision | Required T4 decision | T4 decision | PASS |

## Execution Plan

1. Verify source candidate and ASSF contracts.
2. Record T0 evidence protocol and closure.
3. Record T1 static evidence.
4. Record T2 manual UAT script.
5. Record T3 certification-readiness decision.
6. Record T4 checker-reopen decision.
7. Close roadmap and completion review.
8. Gate and commit material only.
9. Perform session-sync separately.

## Evidence Requirements

| Evidence | Required disposition |
|---|---|
| Source verification | all source facts cite CVF-governed files |
| Drift check | PASS |
| Resolver readout | metadata-only candidate readout |
| UAT script | future operator-run script only |
| Forbidden actions | no runtime/source/session mutation |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF-UAT work order and reviews | internal agents may use the packet as future evidence-prep context only | T0-T4 reviews | no checker, loader, or runtime implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter readout | external agents cannot consume, certify, activate, mutate, or execute packages through this work order | candidate external disposition is deferred | adapter remains deferred | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | T0 protocol completed | PASS |
| AC2 | T1 static evidence completed | PASS |
| AC3 | T2 manual UAT script completed | PASS |
| AC4 | T3 certification-readiness decision completed | PASS |
| AC5 | T4 checker-reopen decision completed | PASS |
| AC6 | No forbidden mutation occurs | PASS |

## Review Gate

Codex reviewer/closer must verify all T0-T4 artifacts, exact changed paths, and
gate evidence before material commit.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex single-agent multi-role |
| Agent type | dispatcher/worker/reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | ASSF-UAT T0-T4 work order, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, drift check, resolver readout, apply_patch, governance gates, git |
| Target paths | `docs/roadmaps/CVF_ASSF_PACKAGE_CANDIDATE_UAT_EVIDENCE_COLLECTION_ROADMAP_2026-06-26.md`; `docs/baselines/CVF_GC018_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_FOR_CODEX_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T0_EVIDENCE_PROTOCOL_AND_WORK_ORDER_COMPLETION_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T1_STATIC_PACKAGE_CANDIDATE_EVIDENCE_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T2_MANUAL_OPERATOR_UAT_SCRIPT_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T3_EVIDENCE_REVIEW_CERTIFICATION_READINESS_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T4_CHECKER_IMPLEMENTATION_REOPEN_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_COMPLETION_2026-06-26.md` |
| Allowed scope source | operator approved Codex to complete ASSF-UAT T0-T4 |
| Before status evidence | HEAD `110b64bf`; `git status --short` returned no paths before authoring |
| After status evidence | material closure artifacts pending commit |
| Diff evidence | `git diff --name-status`; `git diff --check` |
| Approval boundary | documentation-only evidence collection and readiness decisions |
| Claim boundary | no runtime/source/session mutation |
| Invocation ID | `assf-uat-evidence-collection-t0-t4-work-order-2026-06-26` |
| Expected manifest | `docs/roadmaps/CVF_ASSF_PACKAGE_CANDIDATE_UAT_EVIDENCE_COLLECTION_ROADMAP_2026-06-26.md`; `docs/baselines/CVF_GC018_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_FOR_CODEX_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T0_EVIDENCE_PROTOCOL_AND_WORK_ORDER_COMPLETION_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T1_STATIC_PACKAGE_CANDIDATE_EVIDENCE_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T2_MANUAL_OPERATOR_UAT_SCRIPT_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T3_EVIDENCE_REVIEW_CERTIFICATION_READINESS_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T4_CHECKER_IMPLEMENTATION_REOPEN_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_COMPLETION_2026-06-26.md` |
| Actual changed set | `docs/roadmaps/CVF_ASSF_PACKAGE_CANDIDATE_UAT_EVIDENCE_COLLECTION_ROADMAP_2026-06-26.md`; `docs/baselines/CVF_GC018_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_FOR_CODEX_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T0_EVIDENCE_PROTOCOL_AND_WORK_ORDER_COMPLETION_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T1_STATIC_PACKAGE_CANDIDATE_EVIDENCE_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T2_MANUAL_OPERATOR_UAT_SCRIPT_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T3_EVIDENCE_REVIEW_CERTIFICATION_READINESS_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_T4_CHECKER_IMPLEMENTATION_REOPEN_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_COMPLETION_2026-06-26.md` |
| Manifest delta | MATCH |

## Closure Checklist

| Check | Required resolution |
|---|---|
| T0 review exists | PASS |
| T1 review exists | PASS |
| T2 script exists | PASS |
| T3 decision exists | PASS |
| T4 decision exists | PASS |
| Completion review exists | PASS |
| Forbidden mutation absent | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` if all evidence artifacts exist and gates pass.
Return `BLOCKED_WITH_REASON` if source evidence or gate compliance cannot be
established inside scope.

## Operator Checkpoint

No additional checkpoint is required for this documentation-only T0-T4 closure.
Operator checkpoint is required before real UAT execution, package
certification, lifecycle mutation, registry mutation, generated-index mutation,
resolver mutation, checker implementation, adapter implementation, provider/live
proof, public-sync, push, or scope expansion.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-UAT T0-T4 work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- documentation-only closure |
| receiptEvidence | CVF_RECEIPT_PRESENT - local checks and gates |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- T0-T4 artifacts and completion review |
| invocationBoundary | governed local documentation and read-only checks |
| interceptionBoundary | no provider, CLI, MCP, Web runtime, adapter, package execution, or certification action |
| claimLanguage | closes evidence preparation without lifecycle mutation |
| forbiddenExpansion | no package instance creation, certification decision, lifecycle mutation, registry mutation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, readiness claim, package instruction execution, or session-sync in material commit |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_UAT_EVIDENCE_COLLECTION_T0_T4_COMPLETION_2026-06-26.md` | final disposition and gate evidence | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_CANDIDATE_UAT_EVIDENCE_COLLECTION_ROADMAP_2026-06-26.md` | roadmap closed bounded | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized | no corpus registry JSON in changed set | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no registry Markdown mutation is authorized | no corpus registry Markdown mutation | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external artifact is created | no external digest applies | N/A with reason |
| System loop interlock | this work order and completion review | no runtime loop or provider call | PASS |
| Session continuity | N/A with reason: session-sync is separate after material closure | active session paths excluded | N/A with reason |

## Claim Boundary

This work order closes documentation evidence preparation only.
