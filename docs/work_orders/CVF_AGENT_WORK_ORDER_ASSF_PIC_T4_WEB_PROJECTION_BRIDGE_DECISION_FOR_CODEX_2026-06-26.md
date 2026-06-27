# CVF Agent Work Order: ASSF-PIC-T4 Web Projection Bridge Decision

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: work_order

Batch ID: ASSF-PIC-T4

dispatchBaseHead: ecfc911b

executionBaseHead: ecfc911b

closureBaseHead: ecfc911b

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Codex multi-role executor. This packet authorizes a local decision-only
T4 closure after operator approval to proceed through ASSF-PIC-T4 and T5.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_FOR_CODEX_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_2026-06-26.md`

Do-not-misread notes: this work order does not authorize Web runtime mutation,
registry mutation, generated-index mutation, resolver mutation, package
creation, certification, activation, CLI/MCP adapter implementation,
provider/live proof, public-sync, push, or session-sync in the material commit.

## Purpose

Decide whether the selected ASSF candidate can receive a certified Web
projection bridge. The required decision is bounded to current source evidence.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-26 approval for Codex to process T4 and T5 | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active session bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| ASSF-PIC roadmap | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | ACCEPT |
| Paired baseline | `docs/baselines/CVF_GC018_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_2026-06-26.md` | ACCEPT |

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
| `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | READ | T4 requirements |
| `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | READ | selected candidate lifecycle state |
| `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | READ | Web projection boundary |
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | READ | bridge and adapter rules |
| `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | READ | current Web schema gap evidence |

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0
```

## Scope / Methodology

Codex read the current roadmap, T2/T3 closure evidence, selected registry
entry, ASSF Web projection contract, ASSF certification lifecycle guard, and
T6 Web migration audit. Codex ran read-only generated-index drift and resolver
commands to ensure the selected candidate state was not stale.

## Findings / Position

The Web projection bridge is deferred. The selected candidate is not certified,
UAT has not started, the Web schema bridge has not been implemented, and the
external adapter remains deferred.

## Required Outputs

| Roadmap output | Closure evidence |
|---|---|
| Web projection decision | `WEB_PROJECTION_DEFERRED_CERTIFICATION_HELD` |
| schema bridge disposition | `SCHEMA_BRIDGE_DEFERRED_CERTIFICATION_HELD` |
| no self-certification claim from Web display | decision review and completion review deny Web display as package truth |
| external-agent adapter disposition | `EXTERNAL_ADAPTER_DEFERRED_NO_EVIDENCE` |

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/baselines/CVF_GC018_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_2026-06-26.md` | Codex | create and close baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_FOR_CODEX_2026-06-26.md` | Codex | create and close work order |
| `docs/reviews/CVF_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_2026-06-26.md` | Codex | create decision review |
| `docs/reviews/CVF_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_COMPLETION_2026-06-26.md` | Codex | create completion review |
| `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | Codex | update T4/T5 status rows only |

## Forbidden Changed Paths And Actions

No package roots, registry source, generated index, resolver source, Web
runtime, adapter source, provider/live proof, public-sync, push, package
activation, lifecycle mutation, certification decision, or session-sync path is
inside this material work order.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-PIC-T4 is the Web projection bridge decision | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | `ASSF-PIC-T4 - Web Projection Bridge Decision` | `ASSF-PIC-T4` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |
| Candidate UAT remains not started | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `uatState` | ASSF registry entry | VALUE_SET | ACCEPT |
| Candidate certification remains not started | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| Candidate external adapter remains deferred | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `externalCliMcpDisposition` | ASSF registry entry | VALUE_SET | ACCEPT |
| Certified Web projection requires package certification | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Classification Vocabulary | `CERTIFIED_PACKAGE_PROJECTION` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Bridge requires UAT passed and certification state certified | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Web Projection Certification Bridge | `certificationState` | ASSF lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| Existing Web skill surface lacks certification state | `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | Findings / Position | `corpusClass` | ASSF-T6 Web audit | LITERAL_INVARIANT | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| Selected registry entry | read current source entry | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lifecycle fields remain not started; external adapter remains deferred |
| Generated index drift | ran current drift check before T4 closure | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| Resolver readout | ran current resolver query before T4 closure | `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0` | one metadata-only candidate readout |
| Web projection surface | read contract and T6 audit | Web projection contract and T6 Web audit | bridge deferred; no Web runtime mutation |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatches, executes, reviews, and closes this decision-only tranche |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=ecfc911b`; closure base recorded in completion review |
| changedSetScope(phase) | material closure paths only; session-sync follows separately if next move changes |
| traceScope(phase, actor) | Codex trace covers T4 material artifacts only; later session-sync trace covers continuity only |
| commitOwner(phase) | Codex owns material commit and separate session-sync commit |
| crossBatchIsolation | T4 material closure is separate from T5 and session-sync |
| nextMoveSurfaces | updated only after material commit succeeds |
| Closer designation | Codex is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | T4 baseline; this work order; T4 decision review; T4 completion review; ASSF-PIC roadmap T4/T5 status rows |
| workerReturnStatus | N/A with reason: Codex is executing single-agent multi-role closure |
| closer | Codex |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator direction to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this T4 work order |
| Disposition | local decision only |
| Claim boundary | no external material absorbed |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order coverage | Output artifact | Status |
|---|---|---|---|
| Web projection decision | Required Outputs | T4 decision review | PASS |
| schema bridge disposition | Required Outputs | T4 decision review | PASS |
| no Web self-certification | Forbidden actions and Claim Boundary | T4 completion review | PASS |
| external-agent adapter disposition | Required Outputs | T4 decision review | PASS |

## Execution Plan

1. Verify current lifecycle, Web, adapter, generated-index, and resolver source
   facts.
2. Record the T4 decision review with one Web projection disposition.
3. Record the completion review and roadmap T4/T5 status update.
4. Run governance gates and diff hygiene.
5. Commit material T4 closure only.
6. Perform session-sync separately after the material commit succeeds.

## Evidence Requirements

| Evidence | Required disposition |
|---|---|
| Source verification | all source facts cite CVF-governed files |
| Drift check | PASS or blocking reason |
| Resolver readout | metadata-only candidate readout or blocking reason |
| Changed paths | stay inside Write Ownership |
| Forbidden actions | no runtime, Web, adapter, registry, generated-index, resolver, provider, public, or session-sync mutation |

## Review Gate

Codex reviewer/closer must verify the decision review, completion review,
roadmap update, exact changed paths, and gate evidence before material commit.

## Closure Checklist

| Check | Required resolution |
|---|---|
| T4 decision review exists | PASS |
| Completion review exists | PASS |
| Web projection disposition present | PASS |
| Schema bridge disposition present | PASS |
| External adapter disposition present | PASS |
| Forbidden mutation absent | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` if T4 produces the required dispositions without
forbidden mutation. Return `BLOCKED_WITH_REASON` if certification evidence,
Web bridge authority, adapter evidence, or gate compliance cannot be established
inside scope.

## Operator Checkpoint

No additional operator checkpoint is required for decision-only T4 closure.
Operator checkpoint is required before any Web runtime change, package
certification, registry mutation, adapter implementation, provider/live proof,
public-sync, push, or scope expansion.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T4 decision artifacts | internal agents may use the decision as candidate-only routing evidence; no Web certified projection is authorized | source verification and completion review | no bridge or loader implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter readout | external agents cannot consume, certify, activate, mutate, or execute packages through this decision | registry external disposition | adapter remains deferred | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | T4 records one Web projection disposition | PASS |
| AC2 | T4 records one schema bridge disposition | PASS |
| AC3 | T4 denies Web display as certification evidence | PASS |
| AC4 | T4 records external adapter disposition | PASS |
| AC5 | No forbidden source or runtime mutation occurs | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_COMPLETION_2026-06-26.md` | `Reviewer verdict: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | T4 closed; T5 released for GC-018 after T4 closure | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation authorized | no registry JSON in changed set | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no registry Markdown mutation authorized | no registry Markdown mutation | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external artifact exists | no digest applies | N/A with reason |
| System loop interlock | this work order and T4 completion review | no package activation, runtime loop, provider call, public-sync, or worker commit occurred | PASS |
| Session continuity | N/A with reason: session-sync is separate after material closure | active session paths excluded from material changed set | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-PIC-T4 work order and decision closure |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- decision-only closure |
| receiptEvidence | CVF_RECEIPT_PRESENT - source reads and gate evidence are recorded in completion review |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, Required Outputs, and closure package |
| invocationBoundary | governed local documentation only |
| interceptionBoundary | no provider, CLI, MCP, Web runtime, adapter, or package execution claim |
| claimLanguage | defers Web bridge until certification and schema prerequisites exist |
| forbiddenExpansion | no runtime/source mutation, package certification, activation, adapter, provider/live proof, public-sync, push, or material session-sync |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Agent type | single-agent multi-role |
| Provider or surface | local workspace |
| Session or invocation | ASSF-PIC-T4, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, rg, drift check, resolver readout, apply_patch, governance gates, git |
| Before status evidence | HEAD `ecfc911b`; clean worktree before authoring |
| After status evidence | T4 material closure artifacts pending commit |
| Diff evidence | `git diff --name-status`; `git diff --check` |
| Allowed scope source | operator approved Codex to process T4 and T5 after WODS-T4 closure |
| Target paths | T4 baseline, work order, decision review, completion review, and ASSF-PIC roadmap |
| Approval boundary | T4 material decision closure only |
| Claim boundary | decision-only closure |
| Invocation ID | `assf-pic-t4-web-projection-bridge-decision-2026-06-26` |
| Expected manifest | `docs/baselines/CVF_GC018_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_FOR_CODEX_2026-06-26.md`; `docs/reviews/CVF_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_COMPLETION_2026-06-26.md`; `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` |
| Actual changed set | `docs/baselines/CVF_GC018_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_FOR_CODEX_2026-06-26.md`; `docs/reviews/CVF_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_2026-06-26.md`; `docs/reviews/CVF_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_COMPLETION_2026-06-26.md`; `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` |
| Manifest delta | MATCH |

## Claim Boundary

This work order closes only the T4 decision. It does not authorize Web runtime,
schema, registry, generated-index, resolver, adapter, provider, public, package,
certification, activation, or session-sync mutation.
