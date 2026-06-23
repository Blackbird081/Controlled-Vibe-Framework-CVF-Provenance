# CVF Agent Work Order ASSF-T3 Learning And ADIF Promotion Bridge For Worker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: work_order

Batch ID: ASSF-T3

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: ASSF-T3 no-commit worker; Learning And ADIF Promotion Bridge contract author.

Canonical packet: this work order plus `docs/baselines/CVF_GC018_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_2026-06-23.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

dispatchBaseHead: `b1969159`.

executionBaseHead: worker must capture with `git rev-parse --short HEAD` before edits.

Current-time notes: current dispatch date is 2026-06-23; worker must record actual local start time in the return packet.

Do-not-misread notes: T3 is contract-definition-only. Do not write any promoter, resolver, generator, drift checker, or test code. Do not create a real skill candidate entry. Do not run a learning or legacy scan. Promoted output is always `CANDIDATE`; no path may set a skill `APPROVED` or `ACTIVE` without reviewer decision and UAT. Reuse the frozen ASSF-T1 contract, the LSC dedupe and threshold rules, and the ADIF entry shape; do not invent weaker rules.

Required first actions: read front door/state/handoff/guard orientation, read this packet, the GC-018 baseline, the ASSF-T1 contract, the LSC-T4 threshold policy, the LSC signal-ledger entry template, the ADIF entry template, and the dual-agent standard; capture `git status --short`; run the pre-implementation gate.

Return contract: return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` without committing.

You are the ASSF-T3 worker. Author only the Learning And ADIF Promotion
Bridge contract document and the worker-return packet described here. You
must not commit. Return `COMPLETE_PENDING_REVIEW` only with the required
artifacts present and reviewer-fast evidence captured, or return
`BLOCKED_WITH_REASON` if a gate fails outside allowed scope.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Exhaustive directory claim omits actual children: this work order makes no exhaustive-directory claim; it cites named source families by path, not by claiming a complete listing.
- ADIF-0002 - Provider-local interaction accepted as authority: the bridge keeps promoted skills at CANDIDATE pending reviewer decision and UAT; no provider-local or agent-memory output is authority.
- ADIF-0006 - Source Verification symbol cell contains a value/type: the Source Verification Block lists only field/path/symbol names in the verified-symbol column, never value assignments or type annotations.
- ADIF-0007 - Gate keyword in exclusion prose triggers wrong evidence class: scope-exclusion sentences avoid bare gate-trigger tokens; this is a contract-definition tranche with no corpus scan, readiness, or provider claim.

## Core Guard Self-Protection Authorization

| Field | Disposition |
|---|---|
| Authorized guard-maintenance scope | ASSF-T3 creates one NEW governed reference document under `docs/reference/agent_system_skills/` and the worker-return packet; it does not create, modify, delete, or weaken any `governance/compat/` guard, hook chain, or autorun gate |
| Protected paths | all existing `governance/compat/*.py` guards, hook chains, and autorun gates remain unmodified by this tranche |
| Operator authorization | operator selected ASSF-T3 with contract-definition-only scope |
| Rollback boundary | worker creates only the new bridge contract document and worker-return packet; revert is deletion of those two new files |

## Purpose

Provide a no-commit worker packet for ASSF-T3 so the Learning And ADIF
Promotion Bridge is defined, as a contract document only, against the frozen
ASSF-T1 package contract, the LSC promotion-threshold policy, and the ADIF
entry registry, and returned for Codex review before any later tranche
implements an executable promoter.

## Objective

Author one governed reference document that defines how a repeated, accepted
LSC learning signal and a recorded ADIF finding each map into an ASSF skill
candidate (always `CANDIDATE`), with dedupe by root-cause group, an evidence
threshold reusing the LSC-T4 policy, a reviewer-decision gate, a UAT
requirement, explicit rejection and session-local outcomes, and a strict
no-self-activation invariant, and return it for Codex review.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | ASSF-T3 is the operator-selected next move |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current lane points to ASSF-T3 |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | active handoff for governed execution context |
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T3 tranche definition |
| GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_2026-06-23.md` | continuation baseline for this work order |
| ASSF-T1 package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | mandatory candidate shape and lifecycle authority |
| ASSF-T2 resolver foundation | `governance/compat/run_assf_skill_resolver.py` | the data plane promoted candidates feed |
| LSC promotion threshold policy | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | threshold and dedupe authority to reuse |
| LSC signal ledger entry template | `docs/reference/learning_signal_chain/CVF_LEARNING_SIGNAL_LEDGER_ENTRY_TEMPLATE.json` | learning-evidence source shape |
| ADIF entry template | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | defect-finding source shape |
| Dual-agent standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | internal and external CLI/MCP accounting |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Claude (this turn) | Create source-verified dispatch packet; dispatcher does not execute |
| Worker | assigned worker agent | Author the bridge contract and worker-return packet; do not commit |
| Reviewer/closer | Codex | Validate dedupe, threshold reuse, reviewer/UAT gate, no-self-activation, dual-agent accounting, close T3, update session surfaces, and commit if accepted |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V22_2026-06-22.md`
- `docs/reference/guard_orientation/README.md`
- this work order
- `docs/baselines/CVF_GC018_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_2026-06-23.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md`
- `docs/reference/learning_signal_chain/CVF_LEARNING_SIGNAL_LEDGER_ENTRY_TEMPLATE.json`
- `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`
- `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`

## Pre-Flight Checks

- `git rev-parse --short HEAD`
- `git status --short`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b1969159 --head HEAD`

## Write Ownership

The worker owns only the artifacts named in Allowed Scope. Codex owns the
dispatch commit, closure review, roadmap closure update, session sync, and any
final material commit.

## Execution Plan

Execute the Required Execution Steps in order. Do not begin ASSF-T4 work. Do
not implement a promoter, resolver, generator, drift checker, or test code; do
not create a real skill candidate; do not activate any skill.

## Evidence Requirements

Evidence must include a conformance mapping from LSC signal fields and ADIF
entry fields to ASSF-T1 candidate fields, a statement of the no-self-activation
invariant, citations of the reused LSC dedupe and LSC-T4 threshold rules, the
changed-set manifest, gate receipts, and explicit no-commit status.

## Review Gate

Codex reviewer must rerun reviewer-fast and relevant autorun gates and verify
that the bridge contract reuses the existing dedupe and threshold rules,
forbids self-activation, defines both the learning side and the ADIF side, and
accounts for internal and external agents before accepting worker output.
Worker self-approval is not closure.

## Closure Checklist

- [x] Work order status is dispatch-ready.
- [x] Commit mode is `WORKER_MUST_NOT_COMMIT`.
- [x] Allowed output paths are named.
- [x] Dual Agent Surface Matrix is present.
- [x] External knowledge intake routing is present.
- [x] Worker return packet shape is present.
- [x] Public Export Disposition is private-only.
- [x] ADIF Defect Registry Disclosure is present.
- [x] Core Guard Self-Protection Authorization is present.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for Stop Conditions. Return
`COMPLETE_PENDING_REVIEW` only after the required artifacts and gate evidence
exist.

## Operator Checkpoint

N/A with reason: the operator selected ASSF-T3 with contract-definition-only
scope. No extra checkpoint is required before bounded worker execution; stop
conditions define the return path.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-T3 must map repeated accepted learning evidence into skill candidates with dedupe, source authority, evidence threshold, reviewer decision, UAT, and explicit rejection/session-local outcomes, with no self-activation | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T3 - Learning And ADIF Promotion Bridge | No self-activation | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| The contract defines the candidate shape and lifecycle states a promoted candidate must use | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | CANDIDATE; PROPOSED; APPROVED; ACTIVE; DEPRECATED; RETIRED; REJECTED | ASSF-T1 contract | VALUE_SET | ACCEPT |
| The contract defines the provenance fields a promoted candidate must populate | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | originLane | ASSF-T1 contract | VALUE_SET | ACCEPT |
| A read-only ASSF resolver foundation already exists that promoted candidates feed | `governance/compat/run_assf_skill_resolver.py` | resolve | resolve | ASSF resolver | EXISTS | ACCEPT |
| Learning-evidence promotion already has a governed dedupe-by-root-cause and threshold policy to reuse | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | De-dup before promotion | rootCauseGroupId | LSC-T4 promotion threshold policy | LITERAL_INVARIANT | ACCEPT |
| Learning-evidence promotion recommendation is not promotion execution | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | Promotion recommendation is not promotion execution | Promotion recommendation is not promotion execution | LSC-T4 promotion threshold policy | LITERAL_INVARIANT | ACCEPT |
| The ADIF entry template defines the defect-finding source shape and a promotion ladder | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | Required Fields | promotionState | ADIF entry template | VALUE_SET | ACCEPT |
| A read-only ADIF defect resolver already exists to query findings | `governance/compat/run_adif_defect_resolver.py` | resolve_defect_packet | resolve_defect_packet | ADIF resolver | RUNTIME_BEHAVIOR | ACCEPT |
| Dual Agent Surface Matrix must account for internal and external CLI/MCP consumers | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | INTERNAL_AGENT; EXTERNAL_AGENT_CLI_MCP | dual-agent surface standard | LITERAL_INVARIANT | ACCEPT |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | Claude dispatcher creates work order; worker authors the bridge contract and returns review artifacts; Codex reviewer/closer decides closure and commit |
| phase | DISPATCH_AUTHORING -> WORKER_EXECUTION -> REVIEWER_CLOSURE -> SESSION_SYNC if next move changes |
| baseHeadFor(phase) | dispatchBaseHead=`b1969159`; executionBaseHead=worker must capture with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures from worker return |
| changedSetScope(phase) | worker may create only the paths named in Allowed Scope |
| traceScope(phase, actor) | worker records commands, conformance mapping, changed-set evidence, and gate receipts in the return packet |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; Codex reviewer/closer owns any material and session-sync commit |
| crossBatchIsolation | no ASSF-T4/T5/T6/T7 implementation; no unrelated cleanup |
| nextMoveSurfaces | worker must not edit active session state, session front door, active handoff, or generated active-session aggregate |
| closer designation | Codex reviewer/closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | reviewer creates a completion review under the reviews directory after accepting this return |
| workerReturnPath | `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_WORKER_RETURN_2026-06-23.md` |
| reviewerOwnedClosurePaths | ASSF roadmap update, T3 completion review, active session state/front door/handoff sync, material commit, and session-sync commit if accepted |
| workerReturnDisposition | `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` |
| reviewerCommitRule | Reviewer may commit only after validating dedupe reuse, threshold reuse, reviewer/UAT gate, no-self-activation, and dual-agent accounting |

## Worker Autonomy / No-Question Rule

The worker must repair any machine-gate failure inside Allowed Scope and rerun
the relevant gate without pausing for approval. The worker must stop and return
`BLOCKED_WITH_REASON` only when repair would exceed Allowed Scope, alter commit
mode, touch forbidden paths, require live/provider/public-sync/secrets, release
a new prerequisite, require session/front-door/handoff ownership, or require a
change to the frozen ASSF-T1 contract (a contract gap must be reported, not
silently worked around).

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake class | external-agent returned output |
| Route mode | `MULTI_AGENT_SINGLE_ROLE` |
| Selected route | Claude dispatcher -> worker bridge-contract author -> Codex reviewer/closer |
| Primary worker role | Learning And ADIF Promotion Bridge contract author |
| Reviewer role | Codex reviewer/closer validates dedupe, threshold, reviewer/UAT gate, no-self-activation, and closure |
| External intake route | learning signals and ADIF findings remain evidence; the bridge promotes them only to CANDIDATE |
| Scope assessment | bounded no-commit worker-return authoring one contract document |
| Risk sensitivity | high because the bridge defines how evidence becomes a candidate; a weak rule could let unreviewed evidence reach an active skill, affecting selection behavior, external CLI/MCP disposition, and production-readiness language |
| Escalation condition | stop with `BLOCKED_WITH_REASON` if remediation exceeds allowed scope, touches forbidden paths, needs new human authorization, requires session/front-door/handoff ownership, or requires a contract change |
| Dispatch status | ACCEPT |
| Reason | T3 is selected, source-verified, and bounded to a no-commit contract-definition worker-return |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index status | NOT_APPLICABLE_WITH_REASON |
| Canonical coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` is the canonical legacy coverage index; T3 does not run a new legacy scan and so does not update it |
| Reason | ASSF-T0.1 already enumerated and classified the legacy corpus and ASSF-T1 reconciled it into the package contract; T3 defines a promotion bridge against existing source shapes rather than re-running any scan |
| Required worker evidence | a conformance mapping from LSC signal fields and ADIF entry fields to ASSF-T1 candidate fields |
| Future guard candidate | a future tranche may add a checker that promoted candidate entries carry valid provenance back to an LSC signal or ADIF finding |

## Required Artifact Manifest

| Required output | Path | Required at handoff | Exists |
|---|---|---|---|
| Learning And ADIF Promotion Bridge contract | `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md` | yes | no |
| T3 worker return | `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_WORKER_RETURN_2026-06-23.md` | yes | no |

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
|---|---|---|---|
| Learning And ADIF Promotion Bridge contract | `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md` | worker | WORKER_RETURNED |
| T3 worker return | `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_WORKER_RETURN_2026-06-23.md` | worker | WORKER_RETURNED |
| T3 completion review | `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_COMPLETION_2026-06-23.md` | reviewer | CLOSED_PASS_BOUNDED |
| Material commit | git commit after reviewer acceptance | reviewer | CLOSURE_READY |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| New durable foundation file | `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md` |
| Owning reference family | `docs/reference/agent_system_skills/` (existing reference family) |
| Front door | the existing `docs/reference/agent_system_skills/README.md` front door already covers this family; no new subfolder is created, so no new front door is required |
| Index/aggregate impact | none; T3 creates a single governed reference document and no generated aggregate |
| Relocation/split/refactor | none; this is a new additive document, not a relocation, split, or refactor of an existing file |
| Size discipline | the bridge contract must respect the governed markdown size threshold; if it would approach the threshold, the worker must split it into a companion document in the same family rather than overrunning |

## Allowed Scope

The worker may create or edit only:

- `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md`
- `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_WORKER_RETURN_2026-06-23.md`

The worker may read these for evidence:

- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/README.md`
- `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json`
- `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md`
- `docs/reference/learning_signal_chain/CVF_LEARNING_SIGNAL_LEDGER_ENTRY_TEMPLATE.json`
- `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`
- `governance/compat/run_adif_defect_resolver.py`
- `governance/compat/run_assf_skill_resolver.py`
- `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V22_2026-06-22.md`

The bridge contract is added inside the existing
`docs/reference/agent_system_skills/` reference family, which already carries a
`README.md` front door; no new subfolder is created, so no new front door is
required.

## Forbidden Scope

The worker must not:

- commit, push, public-sync, or edit Git remotes;
- write any promoter, resolver, generator, drift checker, or test code;
- create, modify, delete, or weaken any `governance/compat/*.py` guard, hook
  chain, autorun gate, or any file outside Allowed Scope;
- create a real skill candidate entry under `registry/entries/` or anywhere;
- run a learning scan, a legacy scan, or any corpus enumeration beyond reading
  the named source files;
- define any promotion path that sets a skill `APPROVED` or `ACTIVE` without
  reviewer decision and UAT;
- weaken the LSC root-cause dedupe rule or the LSC-T4 threshold policy;
- implement a CLI/MCP adapter, runtime activation, loader-executor, or any
  runtime/provider/live behavior;
- migrate or reclassify any existing CVF Web example or `governance/skill-library` entry;
- edit `.private_reference/legacy/` or re-run any scan;
- edit active session state/front door/handoff or generated session aggregate;
- change GC-051 corpus registries, roadmap status, baselines, work orders, or unrelated files;
- change the frozen ASSF-T1 contract (report a contract gap instead);
- promote legacy/provider-local content into canonical authority.

## Required Execution Steps

1. Capture startup state:
   - `git rev-parse --short HEAD`
   - `git status --short`
2. Read the required first reads, including the ASSF-T1 contract, the LSC-T4
   threshold policy, the LSC signal-ledger entry template, and the ADIF entry
   template.
3. Run the pre-implementation gate using the dispatch base unless the reviewer
   has provided a newer dispatch commit:
   - `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b1969159 --head HEAD`
4. Author the Learning And ADIF Promotion Bridge contract document at
   `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md`,
   defining: the learning-signal-to-candidate mapping; the ADIF-finding-to-candidate
   mapping; the dedupe-by-root-cause rule reusing `rootCauseGroupId`; the
   evidence threshold reusing the LSC-T4 policy; the reviewer-decision gate; the
   UAT requirement; explicit REJECTED and session-local outcomes; and the
   no-self-activation invariant. Promoted output is always `CANDIDATE`.
5. Include in the contract the mandatory reference-doc sections: `## Scope / Applies To`,
   `## Delta Execution Claim Boundary Control Block`, `## Epistemic Process Block`
   (or the `EPISTEMIC_PROCESS_NA_WITH_REASON:` token if it defines a fixed
   schema rather than testing a hypothesis), `## Claim Boundary`, and
   `## Public Export Disposition`.
6. Author the worker-return packet.
7. Run:
   - `python governance/compat/run_worker_return_fast_gate.py`
   - `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`
8. Return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`,
   or `BLOCKED_WITH_REASON` without committing.

## Required Deliverables

### Bridge Contract Document

The bridge contract must reuse the ASSF-T1 lifecycle states and provenance
fields, the LSC root-cause dedupe rule, and the LSC-T4 threshold policy. It
must define both the learning side and the ADIF side, the reviewer-decision and
UAT gates, the REJECTED and session-local outcomes, and a stated
no-self-activation invariant. It must carry an external-agent CLI/MCP
disposition field.

### Worker Return Packet

The worker-return packet must conform to the Worker Return Packet Shape
Contract below.

## Worker Return Packet Shape Contract

Path:

`docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_WORKER_RETURN_2026-06-23.md`

Required sections:

- Purpose
- Target / Source
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Worker Status
- Required Artifact Manifest
- Roadmap-To-Work-Order Trace Matrix
- Dual Agent Surface Matrix
- Corpus Completeness And Report Integrity
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- Machine Closure Package
- Acceptance Receipt Assertion Matrix
- Agent Operation Trace Block
- Claim Boundary

The worker return must also record `executionBaseHead`, `git status --short`,
a `dispatchWorkOrder:` line citing this work order, a top-level `Status:` line,
and use `N/A with reason` or `NOT_APPLICABLE_WITH_REASON` for conditional
blocks that do not apply. This changeset touches no `governance/compat/*.py`
file, so the worker return does not require a Core Guard Self-Protection
Authorization block; do not write the literal token `todo` anywhere in the
Rescan Intelligence Hardening section.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | the bridge contract that internal promotion tooling will later consume | T3 defines the mapping and gates only; it implements no promoter and grants no authority to set a candidate APPROVED or ACTIVE | the bridge contract document and its conformance to the ASSF-T1 lifecycle states | no promoter implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP promotion or candidate-review adapter | T3 records the external-agent disposition in the bridge contract; it does not implement, expose, or authorize any adapter | dual-agent standard and the ASSF-T1 external-agent disposition field | separate ASSF adapter work required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Worker requirement |
|---|---|
| Chain map | cite `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | learning signal or defect finding -> ASSF-T3 bridge mapping -> ASSF CANDIDATE -> reviewer decision -> UAT -> APPROVED/ACTIVE or REJECTED |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T3 bridge contract and future ASSF-T4 work |
| Disposition | candidate intake only; promotion never activates a skill |
| Route | consume the accepted ASSF-T1 contract and the existing LSC and ADIF source shapes |
| Boundary | candidate proposal only; no instruction loading or activation |
| External-agent disposition | required in the matrix and in the bridge contract |
| Claim boundary | learning and defect evidence remain candidate inputs, not CVF authority |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- Delta ledger status: worker must refresh in the worker-return packet.
- Routing matrix status: worker must refresh in the worker-return packet.
- Semantic sampling status: worker must include at least three samples in the worker-return packet.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Worker instruction |
|---|---|
| `UNCHANGED_FROM_INTAKE` | preserve the ASSF-T1 contract lifecycle states and the LSC-T4 threshold and dedupe rules as authority |
| `CHANGED_DISPOSITION` | record the contract connecting existing LSC and ADIF evidence shapes to the ASSF candidate shape |
| `NEW_FINDING` | record any field a promoted candidate needs that the ASSF-T1 contract does not define, as a contract gap |
| `REMOVED_OR_REJECTED` | record any self-activation path or weakened dedupe/threshold rule as rejected |

### Follow-Up Routing Matrix

| Routing lane | Worker instruction |
|---|---|
| `DO_NOW` | author the bridge contract and the worker-return packet |
| `SEPARATE_RUNTIME_TRANCHE` | route any executable promoter, resolver wiring, and runtime activation to a later tranche |
| `STRATEGIC_OPERATOR_DECISION` | flag whether a future tranche should implement an executable promoter or add a bridge-conformance checker |
| `OUT_OF_SCOPE` | mark migration of existing CVF Web examples, public-sync, and runtime/provider/live out of scope |
| `RESOLVED_BY_DESIGN` | mark items handled by the contract-only scope and the no-self-activation invariant |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T3-WO-S1 | roadmap ASSF-T3 tranche | promoted evidence becomes a candidate, never self-activated | no-self-activation invariant required | could a high-threshold signal auto-promote to ACTIVE? | reject |
| ASSF-T3-WO-S2 | LSC-T4 threshold policy | one root cause yields one promotion count | dedupe-by-root-cause required | could two projections of one root cause inflate the count? | reject |
| ASSF-T3-WO-S3 | dual-agent standard | external CLI/MCP disposition required | bridge contract must carry the field | could the bridge omit the external-agent disposition? | reject |

The worker must record whether this defect class should become a future
machine-check candidate. At minimum, evaluate:

- whether a future tranche should add a checker that promoted candidate entries
  carry valid provenance back to an LSC signal or ADIF finding;
- whether the no-self-activation invariant should have a standing regression
  test when a promoter is later implemented;
- whether the bridge contract should be cited as a required read in any future
  promoter work order.

## Finding-To-Governance Learning Disposition

| Field | Required worker value |
|---|---|
| Defect class | choose one or more: `RULE_GAP`, `MACHINE_GATE_GAP`, `PHASE_GATE_PLACEMENT_GAP`, `OPERATOR_SCOPE_CLARITY_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `DESIGN_REVIEW_REQUIRED`, `MACHINE_CHECK_CANDIDATE`, or `REFERENCE_ONLY` |
| Runtime/provider/cost lane | `N/A_WITH_REASON` unless a runtime/provider/cost finding arises |
| Next control action | state whether ASSF-T4/T7 should absorb each control (e.g. a bridge-conformance checker) |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the bridge contract references private learning-signal and defect
provenance. Public-safe promotion documentation requires later redaction and
public-sync authority.

## Acceptance Criteria

- Required artifacts exist in allowed paths only.
- The bridge contract defines both the learning side and the ADIF side and maps
  each into the ASSF-T1 candidate shape, proven by a conformance mapping.
- The bridge contract reuses the LSC root-cause dedupe rule and the LSC-T4
  threshold policy rather than inventing weaker ones.
- The bridge contract defines a reviewer-decision gate and a UAT requirement
  before any candidate advances past CANDIDATE.
- The bridge contract states a no-self-activation invariant and explicit
  REJECTED and session-local outcomes.
- The Dual Agent Surface Matrix accounts for internal and external CLI/MCP
  consumers.
- No promoter code, resolver, generator, drift checker, real candidate entry,
  skill activation, or migration is created.
- The worker return carries a top-level `Status:` line and the required
  sections.
- No commit is made by the worker.
- Reviewer-fast gates are run or failure is classified.

## Stop Conditions

Return `BLOCKED_WITH_REASON` if:

- the pre-implementation gate fails outside allowed scope;
- the ASSF-T1 contract, the LSC-T4 policy, or the ADIF entry template is unavailable;
- the worker cannot create the required artifacts;
- a promoted candidate needs a field the ASSF-T1 contract does not define (report
  the contract gap rather than changing the contract);
- a repair would require session sync, roadmap/baseline/work-order edits,
  public-sync, live/provider proof, promoter code, a CLI/MCP adapter or runtime
  activation, modification of an existing protected guard, or a commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T3_CLOSED_PASS_BOUNDED_PENDING_T4_SELECTION` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_WORKER_RETURN_2026-06-23.md` | `Status: COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, accepted after reviewer handoff repair | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T3 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T3 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported in this tranche | N/A with reason |
| System loop interlock | this work order | T2 data plane was required before T3 and is now closed; T3 is required before T4 | PASS |
| Session continuity | active session sync after material commit | separate session-sync lane after material commit | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Work order status | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| Commit mode | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Build scope | bridge contract document plus worker return only | as specified | PASS |
| T1 contract consumption | required | required | PASS |
| Self-activation path | forbidden | forbidden | PASS |
| Dedupe and threshold reuse | required | required | PASS |
| External CLI/MCP disposition | present | matrix row present | PASS |
| ADIF defect registry disclosure | present | section present | PASS |
| Runtime/provider/live claim | none | none | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T3 dispatch work order only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - dispatch-ready contract-definition worker-return lane only |
| receiptEvidence | N/A with reason: worker has not authored the bridge contract yet |
| actionEvidence | ACTION_EVIDENCE_PRESENT - Source Verification rows and governed dispatch artifact |
| invocationBoundary | roadmap-derived work-order authoring |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a bounded learning-and-defect promotion bridge contract document |
| forbiddenExpansion | no promoter code, resolver, generator, drift checker, real candidate entry, skill activation, CLI/MCP adapter, migration, runtime/provider/live, or public-sync |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude dispatch author |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T3 work-order dispatch, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver query, file authoring, governance gates |
| Target paths | this work order; matching GC-018 baseline; ASSF roadmap and source context reads |
| Allowed scope source | operator instruction to author the ASSF-T3 work order; operator selected contract-definition-only scope |
| Before status evidence | clean worktree at HEAD `b1969159` (`git status --short` empty before this dispatch pair) |
| After status evidence | ASSF-T3 dispatch ready; worker-return lane required |
| Diff evidence | real-range name-status and gate output before commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution and no bridge contract authoring |
| Agent type | dispatcher |
| Invocation ID | `cvf-assf-t3-learning-and-adif-promotion-bridge-workorder-2026-06-23` |
| Expected manifest | this work order; matching GC-018 baseline |
| Actual changed set | this work order; matching GC-018 baseline |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This work order authorizes ASSF-T3 worker-return execution only. It does not
author the bridge contract, close ASSF-T3, implement a promoter or any code,
create a real skill candidate, activate any skill, run a learning scan,
implement a CLI/MCP adapter, run provider/live proof, public-sync, or
authorize ASSF-T4.

## Related Artifacts

- `docs/baselines/CVF_GC018_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_2026-06-23.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md`
- `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
