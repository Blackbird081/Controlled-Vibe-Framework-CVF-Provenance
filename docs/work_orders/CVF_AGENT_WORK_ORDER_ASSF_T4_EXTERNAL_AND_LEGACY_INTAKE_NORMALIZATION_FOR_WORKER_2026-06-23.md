# CVF Agent Work Order ASSF-T4 External And Legacy Intake Normalization For Worker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: work_order

Batch ID: ASSF-T4

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: ASSF-T4 no-commit worker; External And Legacy Intake Normalization contract author.

Canonical packet: this work order plus `docs/baselines/CVF_GC018_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_2026-06-23.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

dispatchBaseHead: `050741bb`.

executionBaseHead: worker must capture with `git rev-parse --short HEAD` before edits.

Current-time notes: current dispatch date is 2026-06-23; worker must record actual local start time in the return packet.

Do-not-misread notes: T4 is contract-definition-only. Do not write any normalizer, promoter, resolver, generator, or test code. Do not create a real skill candidate entry. Do not run an external or legacy scan. Normalized output is always `CANDIDATE`; no path may set a skill `APPROVED` or `ACTIVE` without reviewer decision and UAT. Reuse the frozen ASSF-T1 contract, the ASSF-T3 no-self-activation invariant, the external screening disposition vocabulary, and the ASSF-T0.1 ledger disposition vocabulary; do not invent weaker rules. Any external or legacy claim that cannot be reverified against a CVF-governed source must route to a rejected/blocked outcome.

Required first actions: read front door/state/handoff/guard orientation, read this packet, the GC-018 baseline, the ASSF-T1 contract, the ASSF-T3 bridge contract, the external screening matrix, the ASSF-T0.1 ledger, and the dual-agent standard; capture `git status --short`; run the pre-implementation gate.

Return contract: return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` without committing.

You are the ASSF-T4 worker. Author only the External And Legacy Intake
Normalization contract document and the worker-return packet described here.
You must not commit. Return `COMPLETE_PENDING_REVIEW` only with the required
artifacts present and reviewer-fast evidence captured, or return
`BLOCKED_WITH_REASON` if a gate fails outside allowed scope.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Exhaustive directory claim omits actual children: this work order makes no exhaustive-directory claim; it cites named source families by path, not by claiming a complete listing.
- ADIF-0002 - Provider-local interaction accepted as authority: the normalization rejects any provider-local or legacy claim that cannot be reverified against a CVF-governed source and keeps normalized output at CANDIDATE pending reviewer decision and UAT.
- ADIF-0006 - Source Verification symbol cell contains a value/type: the Source Verification Block lists only field/path/symbol names in the verified-symbol column, never value assignments or type annotations.
- ADIF-0007 - Gate keyword in exclusion prose triggers wrong evidence class: scope-exclusion sentences avoid bare gate-trigger tokens; this is a contract-definition tranche with no new corpus scan, readiness, or provider claim.

## Core Guard Self-Protection Authorization

| Field | Disposition |
|---|---|
| Authorized guard-maintenance scope | ASSF-T4 creates one NEW governed reference document under `docs/reference/agent_system_skills/` and the worker-return packet; it does not create, modify, delete, or weaken any `governance/compat/` guard, hook chain, or autorun gate |
| Protected paths | all existing `governance/compat/*.py` guards, hook chains, and autorun gates remain unmodified by this tranche |
| Operator authorization | operator selected ASSF-T4 with contract-definition-only scope |
| Rollback boundary | worker creates only the new normalization contract document and worker-return packet; revert is deletion of those two new files |

## Purpose

Provide a no-commit worker packet for ASSF-T4 so the External And Legacy
Intake Normalization is defined, as a contract document only, against the
frozen ASSF-T1 package contract, the ASSF-T3 promotion bridge contract, the
external skill screening matrix, and the ASSF-T0.1 legacy absorption ledger,
and returned for Codex review before any later tranche implements an
executable normalizer.

## Objective

Author one governed reference document that defines how an external skill
screening disposition and a legacy absorption ledger disposition each map
into an ASSF skill candidate (always `CANDIDATE`), preserving provenance,
license, and security, with a reverification gate that routes any
provider-local or legacy claim that cannot be reverified against a
CVF-governed source to a rejected/blocked outcome, reusing the ASSF-T3
no-self-activation invariant, and return it for Codex review.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | ASSF-T4 is the operator-selected next move |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current lane points to ASSF-T4 |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | active handoff for governed execution context |
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T4 tranche definition |
| GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_2026-06-23.md` | continuation baseline for this work order |
| ASSF-T1 package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | mandatory candidate shape and lifecycle authority |
| ASSF-T3 promotion bridge contract | `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md` | sibling intake-lane contract; reuse its no-self-activation invariant and reviewer/UAT pattern |
| External skill screening matrix | `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md` | external-intake disposition vocabulary and normalization-field source |
| ASSF-T0.1 legacy absorption ledger | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | legacy-intake disposition vocabulary source |
| External knowledge absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | external-intake routing authority |
| Dual-agent standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | internal and external CLI/MCP accounting |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Claude (this turn) | Create source-verified dispatch packet; dispatcher does not execute |
| Worker | assigned worker agent | Author the normalization contract and worker-return packet; do not commit |
| Reviewer/closer | Codex | Validate provenance/license/security preservation, reverification gate, no-self-activation reuse, dual-agent accounting, close T4, update session surfaces, and commit if accepted |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V22_2026-06-22.md`
- `docs/reference/guard_orientation/README.md`
- this work order
- `docs/baselines/CVF_GC018_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_2026-06-23.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md`
- `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md`
- `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`
- `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`

## Pre-Flight Checks

- `git rev-parse --short HEAD`
- `git status --short`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 050741bb --head HEAD`

## Write Ownership

The worker owns only the artifacts named in Allowed Scope. Codex owns the
dispatch commit, closure review, roadmap closure update, session sync, and any
final material commit.

## Execution Plan

Execute the Required Execution Steps in order. Do not begin ASSF-T5 work. Do
not implement a normalizer, promoter, resolver, generator, or test code; do
not create a real skill candidate; do not activate any skill.

## Evidence Requirements

Evidence must include a conformance mapping from external screening
dispositions and legacy ledger dispositions to ASSF-T1 candidate fields and
states, a statement of the no-self-activation invariant reuse, the
provenance/license/security preservation requirement, the reverification gate
definition, the changed-set manifest, gate receipts, and explicit no-commit
status.

## Review Gate

Codex reviewer must rerun reviewer-fast and relevant autorun gates and verify
that the normalization contract preserves provenance/license/security, reuses
the ASSF-T3 no-self-activation invariant, rejects unreverifiable claims,
defines both the external side and the legacy side, and accounts for internal
and external agents before accepting worker output. Worker self-approval is
not closure.

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

N/A with reason: the operator selected ASSF-T4 with contract-definition-only
scope. No extra checkpoint is required before bounded worker execution; stop
conditions define the return path.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-T4 must unify external skill screening and legacy absorption into the package-candidate contract, preserve provenance/license/security, and reject claims that cannot be reverified against CVF-governed sources | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T4 - External And Legacy Intake Normalization | reject provider-local or legacy claims | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| The contract defines the candidate shape and lifecycle states a normalized candidate must use | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | CANDIDATE; PROPOSED; APPROVED; ACTIVE; DEPRECATED; RETIRED; REJECTED | ASSF-T1 contract | VALUE_SET | ACCEPT |
| The contract defines the provenance fields a normalized candidate must populate | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | originLane | ASSF-T1 contract | VALUE_SET | ACCEPT |
| A sibling intake-lane contract already defines the no-self-activation invariant T4 reuses | `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md` | No-Self-Activation Invariant | No-Self-Activation Invariant | ASSF-T3 bridge contract | LITERAL_INVARIANT | ACCEPT |
| The external skill screening matrix defines the external-intake disposition vocabulary | `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md` | screening disposition column | ACCEPT_AS_PATTERN; DEFER_RUNTIME_GATED; MERGE_AS_PATTERN | external skill screening matrix | VALUE_SET | ACCEPT |
| The ASSF-T0.1 legacy ledger defines the legacy-intake disposition vocabulary | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | Absorption Candidate Ledger | ABSORB_AS_CONTRACT_INPUT; REFERENCE_ONLY; BLOCKED_UNVERIFIED_SOURCE | ASSF-T0.1 audit ledger | VALUE_SET | ACCEPT |
| The external knowledge absorption chain map is the external-intake routing authority | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | chain map | CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP | external absorption chain map | EXISTS | ACCEPT |
| Dual Agent Surface Matrix must account for internal and external CLI/MCP consumers | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | INTERNAL_AGENT; EXTERNAL_AGENT_CLI_MCP | dual-agent surface standard | LITERAL_INVARIANT | ACCEPT |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | Claude dispatcher creates work order; worker authors the normalization contract and returns review artifacts; Codex reviewer/closer decides closure and commit |
| phase | DISPATCH_AUTHORING -> WORKER_EXECUTION -> REVIEWER_CLOSURE -> SESSION_SYNC if next move changes |
| baseHeadFor(phase) | dispatchBaseHead=`050741bb`; executionBaseHead=worker must capture with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures from worker return |
| changedSetScope(phase) | worker may create only the paths named in Allowed Scope |
| traceScope(phase, actor) | worker records commands, conformance mapping, changed-set evidence, and gate receipts in the return packet |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; Codex reviewer/closer owns any material and session-sync commit |
| crossBatchIsolation | no ASSF-T5/T6/T7 implementation; no unrelated cleanup |
| nextMoveSurfaces | worker must not edit active session state, session front door, active handoff, or generated active-session aggregate |
| closer designation | Codex reviewer/closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | reviewer creates a completion review under the reviews directory after accepting this return |
| workerReturnPath | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_WORKER_RETURN_2026-06-23.md` |
| reviewerOwnedClosurePaths | ASSF roadmap update, T4 completion review, active session state/front door/handoff sync, material commit, and session-sync commit if accepted |
| workerReturnDisposition | `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` |
| reviewerCommitRule | Reviewer may commit only after validating provenance/license/security preservation, the reverification gate, no-self-activation reuse, and dual-agent accounting |

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
| Intake class | external repo or copied folder |
| Route mode | `MULTI_AGENT_SINGLE_ROLE` |
| Selected route | Claude dispatcher -> worker normalization-contract author -> Codex reviewer/closer |
| Primary worker role | External And Legacy Intake Normalization contract author |
| Reviewer role | Codex reviewer/closer validates provenance/license/security, reverification gate, no-self-activation, and closure |
| External intake route | external and legacy sources remain evidence; the normalization promotes them only to CANDIDATE and rejects unreverifiable claims |
| Scope assessment | bounded no-commit worker-return authoring one contract document |
| Risk sensitivity | high because the normalization defines how external and legacy evidence becomes a candidate; a weak rule could let an unverifiable provider-local claim reach an active skill, affecting selection behavior, license/security posture, external CLI/MCP disposition, and production-readiness language |
| Escalation condition | stop with `BLOCKED_WITH_REASON` if remediation exceeds allowed scope, touches forbidden paths, needs new human authorization, requires session/front-door/handoff ownership, or requires a contract change |
| Dispatch status | ACCEPT |
| Reason | T4 is selected, source-verified, and bounded to a no-commit contract-definition worker-return |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index status | NOT_APPLICABLE_WITH_REASON |
| Canonical coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` is the canonical legacy coverage index; T4 does not run a new legacy scan and so does not update it |
| Reason | ASSF-T0.1 already enumerated and classified the legacy corpus; T4 defines a normalization mapping against the existing ledger and external screening disposition vocabularies rather than re-running any scan |
| Required worker evidence | a conformance mapping from external screening and legacy ledger dispositions to ASSF-T1 candidate fields and states |
| Future guard candidate | a future tranche may add a checker that normalized candidate entries carry valid reverifiable provenance back to a CVF-governed source |

## Required Artifact Manifest

| Required output | Path | Required at handoff | Exists |
|---|---|---|---|
| External And Legacy Intake Normalization contract | `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md` | yes | no |
| T4 worker return | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_WORKER_RETURN_2026-06-23.md` | yes | no |

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
|---|---|---|---|
| External And Legacy Intake Normalization contract | `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md` | worker | DELIVERED |
| T4 worker return | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_WORKER_RETURN_2026-06-23.md` | worker | DELIVERED |
| T4 completion review | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md` | reviewer | DELIVERED |
| Material commit | git commit after reviewer acceptance | reviewer | DONE |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| New durable foundation file | `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md` |
| Owning reference family | `docs/reference/agent_system_skills/` (existing reference family) |
| Front door | the existing `docs/reference/agent_system_skills/README.md` front door already covers this family; no new subfolder is created, so no new front door is required |
| Index/aggregate impact | none; T4 creates a single governed reference document and no generated aggregate |
| Relocation/split/refactor | none; this is a new additive document, not a relocation, split, or refactor of an existing file |
| Size discipline | the normalization contract must respect the governed markdown size threshold; if it would approach the threshold, the worker must split it into a companion document in the same family rather than overrunning |

## Evidence Reuse And Encoding Plan

verificationMode: `RECOMPUTE_REQUIRED`

recomputeReason: T4 authors a fresh normalization contract and does not reuse any prior verification receipt or manifest hash. The external screening matrix and ASSF-T0.1 ledger are read as disposition-vocabulary sources; the worker must re-read them directly and map their dispositions into the ASSF-T1 candidate shape rather than relying on any earlier verification artifact.

priorVerificationArtifact: N/A with reason: no prior verification receipt is reused; this is a contract-definition tranche

priorVerificationAnchor: N/A with reason: no prior verification receipt is reused

freshRecomputeRequired: YES - the worker re-reads each named source directly and records a fresh conformance mapping

## Allowed Scope

The worker may create or edit only:

- `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md`
- `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_WORKER_RETURN_2026-06-23.md`

The worker may read these for evidence:

- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md`
- `docs/reference/agent_system_skills/README.md`
- `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json`
- `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md`
- `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`
- `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
- `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V22_2026-06-22.md`

The normalization contract is added inside the existing
`docs/reference/agent_system_skills/` reference family, which already carries
a `README.md` front door; no new subfolder is created, so no new front door is
required.

## Forbidden Scope

The worker must not:

- commit, push, public-sync, or edit Git remotes;
- write any normalizer, promoter, resolver, generator, or test code;
- create, modify, delete, or weaken any `governance/compat/*.py` guard, hook
  chain, autorun gate, or any file outside Allowed Scope;
- create a real skill candidate entry under `registry/entries/` or anywhere;
- run an external scan, a legacy scan, or any corpus enumeration beyond reading
  the named source files;
- define any normalization path that sets a skill `APPROVED` or `ACTIVE`
  without reviewer decision and UAT;
- accept any provider-local or legacy claim that cannot be reverified against a
  CVF-governed source;
- drop or weaken the provenance, license, or security fields on a normalized
  candidate;
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
2. Read the required first reads, including the ASSF-T1 contract, the ASSF-T3
   bridge contract, the external screening matrix, and the ASSF-T0.1 ledger.
3. Run the pre-implementation gate using the dispatch base unless the reviewer
   has provided a newer dispatch commit:
   - `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 050741bb --head HEAD`
4. Author the External And Legacy Intake Normalization contract document at
   `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md`,
   defining: the external-screening-disposition-to-candidate mapping; the
   legacy-ledger-disposition-to-candidate mapping; the provenance/license/
   security preservation requirement; the reverification gate that routes any
   claim not reverifiable against a CVF-governed source (including
   `BLOCKED_UNVERIFIED_SOURCE` and unverifiable external claims) to a
   rejected/blocked outcome; reuse of the ASSF-T3 no-self-activation invariant;
   and explicit REJECTED and session-local outcomes. Normalized output is
   always `CANDIDATE`.
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

### Normalization Contract Document

The normalization contract must reuse the ASSF-T1 lifecycle states and
provenance fields and the ASSF-T3 no-self-activation invariant. It must define
both the external side and the legacy side, the provenance/license/security
preservation requirement, the reverification gate, and the REJECTED and
session-local outcomes. It must carry an external-agent CLI/MCP disposition
field.

### Worker Return Packet

The worker-return packet must conform to the Worker Return Packet Shape
Contract below.

## Worker Return Packet Shape Contract

Path:

`docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_WORKER_RETURN_2026-06-23.md`

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
Rescan Intelligence Hardening section. The Corpus Completeness And Report
Integrity section must use the full field list (Corpus task class, Corpus root,
Snapshot time, Enumeration command, Manifest artifact or inline manifest,
Manifest hash, Processing ledger artifact or inline ledger, Allowed terminal
statuses including READ/SKIPPED_WITH_REASON/DEFERRED/BLOCKED_UNREADABLE,
Reconciliation, Unresolved files, Declared exclusions, Unreadable or
unsupported files, Aggregation check, Drift check, Output traceability,
Adversarial verification, Corpus verdict), not a condensed
`NOT_APPLICABLE_WITH_REASON` block.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | the normalization contract that future internal intake tooling will consume | T4 defines the mapping and gates only; it implements no normalizer and grants no authority to set a candidate APPROVED or ACTIVE | the normalization contract document and its conformance to the ASSF-T1 lifecycle states | no normalizer implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP external-intake or candidate-review adapter | T4 records the external-agent disposition in the normalization contract; it does not implement, expose, or authorize any adapter | dual-agent standard and the ASSF-T1 external-agent disposition field | separate ASSF adapter work required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Worker requirement |
|---|---|
| Chain map | cite `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external screening or legacy ledger disposition -> ASSF-T4 normalization mapping -> ASSF CANDIDATE or REJECTED -> reviewer decision -> UAT -> APPROVED/ACTIVE or REJECTED |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T4 normalization contract and future ASSF-T5 work |
| Disposition | candidate intake only; normalization never activates a skill |
| Route | consume the accepted ASSF-T1 contract, the ASSF-T3 bridge contract, and the existing external screening and legacy ledger disposition vocabularies |
| Boundary | candidate proposal only; unreverifiable claims rejected; no instruction loading or activation |
| External-agent disposition | required in the matrix and in the normalization contract |
| Claim boundary | external and legacy skills remain candidate inputs, not CVF authority |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md`
- Delta ledger status: worker must refresh in the worker-return packet.
- Routing matrix status: worker must refresh in the worker-return packet.
- Semantic sampling status: worker must include at least three samples in the worker-return packet.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Worker instruction |
|---|---|
| `UNCHANGED_FROM_INTAKE` | preserve the ASSF-T1 contract lifecycle states and the ASSF-T3 no-self-activation invariant as authority |
| `CHANGED_DISPOSITION` | record the contract adding the external/legacy intake lane alongside the T3 learning/ADIF lane |
| `NEW_FINDING` | record any field a normalized candidate needs that the ASSF-T1 contract does not define, as a contract gap |
| `REMOVED_OR_REJECTED` | record any self-activation path, any dropped provenance/license/security field, or any accepted unreverifiable claim as rejected |

### Follow-Up Routing Matrix

| Routing lane | Worker instruction |
|---|---|
| `DO_NOW` | author the normalization contract and the worker-return packet |
| `SEPARATE_RUNTIME_TRANCHE` | route any executable normalizer, resolver wiring, and runtime activation to a later tranche |
| `STRATEGIC_OPERATOR_DECISION` | flag whether a future tranche should implement an executable normalizer or add a normalization-conformance checker |
| `OUT_OF_SCOPE` | mark migration of existing CVF Web examples, public-sync, and runtime/provider/live out of scope |
| `RESOLVED_BY_DESIGN` | mark items handled by the contract-only scope, the no-self-activation invariant, and the reverification gate |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T4-WO-S1 | roadmap ASSF-T4 tranche | unverifiable provider-local or legacy claims must be rejected | reverification gate required | could an external claim with no CVF-governed source be accepted as CANDIDATE? | reject |
| ASSF-T4-WO-S2 | roadmap ASSF-T4 tranche | provenance/license/security must be preserved | provenance/license/security fields required | could a normalized candidate drop its source license? | reject |
| ASSF-T4-WO-S3 | dual-agent standard | external CLI/MCP disposition required | normalization contract must carry the field | could the contract omit the external-agent disposition? | reject |

The worker must record whether this defect class should become a future
machine-check candidate. At minimum, evaluate:

- whether a future tranche should add a checker that normalized candidate
  entries carry valid reverifiable provenance back to a CVF-governed source;
- whether the reverification gate should have a standing regression test when a
  normalizer is later implemented;
- whether this normalization contract should be cited as a required read in any
  future normalizer work order.

## Finding-To-Governance Learning Disposition

| Field | Required worker value |
|---|---|
| Defect class | choose one or more: `RULE_GAP`, `MACHINE_GATE_GAP`, `PHASE_GATE_PLACEMENT_GAP`, `OPERATOR_SCOPE_CLARITY_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `DESIGN_REVIEW_REQUIRED`, `MACHINE_CHECK_CANDIDATE`, or `REFERENCE_ONLY` |
| Runtime/provider/cost lane | `N/A_WITH_REASON` unless a runtime/provider/cost finding arises |
| Next control action | state whether ASSF-T5/T7 should absorb each control (e.g. a normalization-conformance checker) |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the normalization contract references private legacy provenance and
external screening evidence. Public-safe intake documentation requires later
redaction and public-sync authority.

## Acceptance Criteria

- Required artifacts exist in allowed paths only.
- The normalization contract defines both the external side and the legacy
  side and maps each into the ASSF-T1 candidate shape, proven by a conformance
  mapping.
- The normalization contract reuses the ASSF-T1 lifecycle states and the
  ASSF-T3 no-self-activation invariant rather than inventing weaker ones.
- The normalization contract requires provenance, license, and security on
  every normalized candidate.
- The normalization contract defines a reverification gate that routes any
  claim not reverifiable against a CVF-governed source to a rejected/blocked
  outcome.
- The Dual Agent Surface Matrix accounts for internal and external CLI/MCP
  consumers.
- No normalizer code, promoter, resolver, generator, real candidate entry,
  skill activation, or migration is created.
- The worker return carries a top-level `Status:` line and the required
  sections.
- No commit is made by the worker.
- Reviewer-fast gates are run or failure is classified.

## Stop Conditions

Return `BLOCKED_WITH_REASON` if:

- the pre-implementation gate fails outside allowed scope;
- the ASSF-T1 contract, the ASSF-T3 bridge contract, the external screening
  matrix, or the ASSF-T0.1 ledger is unavailable;
- the worker cannot create the required artifacts;
- a normalized candidate needs a field the ASSF-T1 contract does not define
  (report the contract gap rather than changing the contract);
- a repair would require session sync, roadmap/baseline/work-order edits,
  public-sync, live/provider proof, normalizer code, a CLI/MCP adapter or
  runtime activation, modification of an existing protected guard, or a commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T4_CLOSED_PASS_BOUNDED_PENDING_T5_SELECTION` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_WORKER_RETURN_2026-06-23.md` | `Status: COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, accepted after reviewer repairs | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T4 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T4 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no new external evidence imported; T4 reuses existing screening and ledger dispositions | N/A with reason |
| System loop interlock | this work order | T3 bridge contract was required before T4 and is now closed; T4 is required before T5 | PASS |
| Session continuity | active session sync after material commit | separate session-sync lane after material commit | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Work order status | dispatched then closed | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Commit mode | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Build scope | normalization contract document plus worker return only | as specified | PASS |
| T1 contract consumption | required | required | PASS |
| Self-activation path | forbidden | forbidden | PASS |
| Provenance/license/security preservation | required | required | PASS |
| Reverification gate for unverifiable claims | required | required | PASS |
| External CLI/MCP disposition | present | matrix row present | PASS |
| ADIF defect registry disclosure | present | section present | PASS |
| Runtime/provider/live claim | none | none | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T4 dispatch work order only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - dispatch-ready contract-definition worker-return lane only |
| receiptEvidence | N/A with reason: worker has not authored the normalization contract yet |
| actionEvidence | ACTION_EVIDENCE_PRESENT - Source Verification rows and governed dispatch artifact |
| invocationBoundary | roadmap-derived work-order authoring |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a bounded external-and-legacy intake normalization contract document |
| forbiddenExpansion | no normalizer code, promoter, resolver, generator, real candidate entry, skill activation, CLI/MCP adapter, migration, runtime/provider/live, or public-sync |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude dispatch author |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T4 work-order dispatch, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver query, file authoring, governance gates |
| Target paths | this work order; matching GC-018 baseline; ASSF roadmap and source context reads |
| Allowed scope source | operator instruction to author the ASSF-T4 work order; operator selected contract-definition-only scope |
| Before status evidence | clean worktree at HEAD `050741bb` (`git status --short` empty before this dispatch pair) |
| After status evidence | ASSF-T4 dispatch ready; worker-return lane required |
| Diff evidence | real-range name-status and gate output before commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution and no normalization contract authoring |
| Agent type | dispatcher |
| Invocation ID | `cvf-assf-t4-external-and-legacy-intake-normalization-workorder-2026-06-23` |
| Expected manifest | this work order; matching GC-018 baseline |
| Actual changed set | this work order; matching GC-018 baseline |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This work order authorizes ASSF-T4 worker-return execution only. It does not
author the normalization contract, close ASSF-T4, implement a normalizer or
any code, create a real skill candidate, activate any skill, run an external
or legacy scan, implement a CLI/MCP adapter, run provider/live proof,
public-sync, or authorize ASSF-T5.

## Related Artifacts

- `docs/baselines/CVF_GC018_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_2026-06-23.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md`
- `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md`
- `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
