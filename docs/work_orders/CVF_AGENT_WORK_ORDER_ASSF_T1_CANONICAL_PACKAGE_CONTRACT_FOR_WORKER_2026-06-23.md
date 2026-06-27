# CVF Agent Work Order ASSF-T1 Canonical Package Contract And Storage Topology For Worker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: work_order

Batch ID: ASSF-T1

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: ASSF-T1 no-commit worker; canonical package contract author.

Canonical packet: this work order plus `docs/baselines/CVF_GC018_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_2026-06-23.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

dispatchBaseHead: `ed7d0580`.

executionBaseHead: worker must capture with `git rev-parse --short HEAD` before edits.

Current-time notes: current dispatch date is 2026-06-23; worker must record actual local start time in the return packet.

Do-not-misread notes: T1 is contract-definition-only; reconcile the existing CVF Skill Spec and the ASSF-T0.1 ledger, do not create a competing definition, and do not create any package root, `SKILL.md`, `skill.source.json`, generated index, resolver, or example package.

Required first actions: read front door/state/handoff/guard orientation, read this packet and the GC-018 baseline, read the ASSF-T0.1 audit ledger and the CVF Skill Spec, capture `git status --short`, run pre-implementation gate.

Return contract: return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` without committing.

You are the ASSF-T1 worker. Author only the single canonical package contract
reference document and the paired worker-return packet described here. You must
not commit. Return `COMPLETE_PENDING_REVIEW` only with the required worker
return artifacts present and reviewer-fast evidence captured, or return
`BLOCKED_WITH_REASON` if a gate fails outside allowed scope.

## Core Guard Self-Protection Authorization

| Field | Disposition |
|---|---|
| Authorized guard-maintenance scope | N/A with reason: ASSF-T1 authors only documentation under `docs/reference/agent_system_skills/` and `docs/reviews/`; it does not modify any protected `governance/compat/*.py` guard, hook chain, or autorun gate |
| Protected paths | none modified by this tranche |
| Operator authorization | operator selected ASSF-T1 and directed the dispatcher to author this work order |
| Rollback boundary | worker creates only two new documentation files; revert is deletion of those two files |

## Purpose

Provide a no-commit worker packet for ASSF-T1 so the canonical system-skill
package contract and storage topology are frozen as a single governed
reference document that reconciles the existing CVF Skill Spec and the accepted
ASSF-T0.1 absorption candidate ledger.

## Objective

Author one canonical package contract reference document defining the system
`SKILL.md` profile, the compact machine-readable source schema, identity,
authority, risk and lifecycle field families, the package layout/storage
topology, the dual-agent surface matrix, and the provider-adapter boundary,
reconciled against `governance/skill-library/specs/CVF_SKILL_SPEC.md` and the
ASSF-T0.1 ledger, and return it for Codex review before ASSF-T2 builds the
generated index and resolver.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | ASSF-T1 is the operator-selected next move |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current lane points to ASSF-T1 |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | active handoff for governed execution context |
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T1 tranche definition; T1 must consume the T0.1 ledger |
| GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_2026-06-23.md` | continuation baseline for this work order |
| ASSF-T0.1 audit ledger | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | mandatory legacy-absorption input |
| Existing skill spec | `governance/skill-library/specs/CVF_SKILL_SPEC.md` | current skill definition surface to reconcile |
| Dual-agent standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | internal and external CLI/MCP accounting |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Claude (this turn) | Create source-verified dispatch packet; dispatcher does not execute |
| Worker | assigned worker agent | Author the contract reference doc and worker-return packet; do not commit |
| Reviewer/closer | Codex | Validate reconciliation fidelity, close T1, update session surfaces, and commit if accepted |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V22_2026-06-22.md`
- `docs/reference/guard_orientation/README.md`
- this work order
- `docs/baselines/CVF_GC018_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_2026-06-23.md`
- `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`
- `governance/skill-library/specs/CVF_SKILL_SPEC.md`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`

## Pre-Flight Checks

- `git rev-parse --short HEAD`
- `git status --short`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base ed7d0580 --head HEAD`

## Write Ownership

The worker owns only the two artifacts named in Allowed Scope. Codex owns the
dispatch commit, closure review, roadmap closure update, session sync, and any
final material commit.

## Execution Plan

Execute the Required Execution Steps in order. Do not begin ASSF-T2 work. Do
not create the package root directory, any `SKILL.md`, any `skill.source.json`,
any generated index, any resolver, or any example package. Do not migrate any
existing CVF Web example.

## Evidence Requirements

Evidence must include a CVF-Skill-Spec reconciliation table, a T0.1 ledger
consumption table, the field-family schema definitions, the storage-topology
description, the dual-agent matrix, the provider-adapter boundary, the
changed-set manifest, gate receipts, and explicit no-commit status.

## Review Gate

Codex reviewer must rerun reviewer-fast and relevant autorun gates and verify
that the contract reconciles every CVF Skill Spec required section and maps
every T0.1 `ABSORB_AS_*` ledger row before accepting worker output. Worker
self-approval is not closure.

## Closure Checklist

- [x] Work order status is dispatch-ready.
- [x] Commit mode is `WORKER_MUST_NOT_COMMIT`.
- [x] Allowed output paths are named.
- [x] Dual Agent Surface Matrix is present.
- [x] External knowledge intake routing is present.
- [x] Worker return packet shape is present.
- [x] Public Export Disposition is private-only.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for Stop Conditions. Return
`COMPLETE_PENDING_REVIEW` only after the required artifacts and gate evidence
exist.

## Operator Checkpoint

N/A with reason: the operator selected ASSF-T1 and directed contract-
definition-only scope. No extra checkpoint is required before bounded worker
execution; stop conditions define the return path.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-T1 must reconcile the CVF Skill Spec and the T0.1 ledger, not create a competing definition | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T1 - Canonical Package Contract And Storage Topology | reconcile existing CVF Skill Spec and the ASSF-T0.1 legacy absorption ledger | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| ASSF-T1 must consume the T0.1 candidate ledger before schema work | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Next control action | ASSF-T1 must consume the T0.1 candidate ledger before schema | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| The candidate package contract field families are enumerated in the roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Candidate Package Contract | identity, version, owner, status, provenance, license | ASSF roadmap | VALUE_SET | ACCEPT |
| The existing CVF Skill Spec defines seven required sections | `governance/skill-library/specs/CVF_SKILL_SPEC.md` | Required Sections | Skill Identity; Intent Layer; Capability Layer; Risk Profile; Authority Mapping | skill spec | VALUE_SET | ACCEPT |
| The existing CVF Skill Spec defines four classification classes mapped to R0-R3 | `governance/skill-library/specs/CVF_SKILL_SPEC.md` | Skill Classification | Assistive; Advisory; Executable; Analytical | skill spec | VALUE_SET | ACCEPT |
| The T0.1 ledger provides legacy schema and lifecycle candidates to reconcile | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | Absorption Candidate Ledger | Absorption Candidate Ledger | ASSF-T0.1 audit | EXISTS | ACCEPT |
| Generated aggregates require compact sources and generator discipline | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | generated source layout discipline | generated source layout | generated aggregate standard | LITERAL_INVARIANT | ACCEPT |
| Dual Agent Surface Matrix must account for internal and external CLI/MCP consumers | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | INTERNAL_AGENT; EXTERNAL_AGENT_CLI_MCP | dual-agent surface standard | LITERAL_INVARIANT | ACCEPT |
| The proposed canonical root path is named by ASSF-T0 | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T0 proposed canonical root | docs/reference/agent_system_skills/ | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | Claude dispatcher creates work order; worker authors the contract and returns review artifacts; Codex reviewer/closer decides closure and commit |
| phase | DISPATCH_AUTHORING -> WORKER_EXECUTION -> REVIEWER_CLOSURE -> SESSION_SYNC if next move changes |
| baseHeadFor(phase) | dispatchBaseHead=`ed7d0580`; executionBaseHead=worker must capture with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures from worker return |
| changedSetScope(phase) | worker may create only the contract reference doc and the worker-return path named in Allowed Scope |
| traceScope(phase, actor) | worker records commands, reconciliation tables, changed-set evidence, and gate receipts in the return packet |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; Codex reviewer/closer owns any material and session-sync commit |
| crossBatchIsolation | no ASSF-T2/T3/T4/T5/T6/T7 implementation; no unrelated cleanup |
| nextMoveSurfaces | worker must not edit active session state, session front door, active handoff, or generated active-session aggregate |
| closer designation | Codex reviewer/closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | reviewer creates a completion review under the reviews directory after accepting this return |
| workerReturnPath | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_WORKER_RETURN_2026-06-23.md` |
| reviewerOwnedClosurePaths | ASSF roadmap update, T1 completion review, active session state/front door/handoff sync, material commit, and session-sync commit if accepted |
| workerReturnDisposition | `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` |
| reviewerCommitRule | Reviewer may commit only after validating reconciliation fidelity, rerunning gates, and resolving closure defects |

## Worker Autonomy / No-Question Rule

The worker must repair any machine-gate failure inside Allowed Scope and rerun
the relevant gate without pausing for approval. The worker must stop and return
`BLOCKED_WITH_REASON` only when repair would exceed Allowed Scope, alter commit
mode, touch forbidden paths, require live/provider/public-sync/secrets, release
a new prerequisite, or require session/front-door/handoff ownership.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake class | legacy source family |
| Route mode | `MULTI_AGENT_SINGLE_ROLE` |
| Selected route | Claude dispatcher -> worker contract author -> Codex reviewer/closer |
| Primary worker role | canonical package contract author and reconciler |
| Reviewer role | Codex reviewer/closer validates reconciliation fidelity and closure |
| External intake route | consume the accepted ASSF-T0.1 absorption ledger plus the CVF Skill Spec |
| Scope classification | bounded no-commit worker-return over two allowed output paths |
| Risk sensitivity | high because the package contract becomes the authority every later ASSF tranche depends on, affecting schema, generated index, resolver, external CLI/MCP disposition, public-sync boundary, and production-readiness language |
| Escalation condition | stop with `BLOCKED_WITH_REASON` if remediation exceeds allowed scope, touches forbidden paths, needs new human authorization, or requires session/front-door/handoff ownership |
| Dispatch status | ACCEPT |
| Reason | T1 is selected, source-verified, and bounded to contract-definition-only no-commit worker-return execution |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index status | NOT_APPLICABLE_WITH_REASON |
| Canonical coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` is the canonical legacy coverage index; T1 does not run a new legacy scan and so does not update it |
| Reason | ASSF-T0.1 already enumerated and classified the legacy corpus into an accepted absorption ledger; T1 consumes that ledger rather than re-running the scan or updating the canonical coverage index |
| Required worker evidence | a T0.1 ledger-consumption table mapping each `ABSORB_AS_*` row to a contract field or explicit deferral |
| Future guard candidate | require contract/index consistency evidence before ASSF-T2 generated-index dispatch |

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
|---|---|---|---|
| T1 contract reference doc | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | worker | ACCEPTED_BY_REVIEWER |
| T1 worker return | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_WORKER_RETURN_2026-06-23.md` | worker | ACCEPTED_BY_REVIEWER |
| T1 completion review | a reviewer-created completion review under the reviews directory | reviewer | REVIEWER_OWNED_AFTER_RETURN |
| Reviewer-fast evidence | command output in worker return | worker | PASS |
| Material commit | git commit after reviewer acceptance | reviewer | REVIEWER_OWNED_AFTER_RETURN |

## Allowed Scope

The worker may create or edit only:

- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_WORKER_RETURN_2026-06-23.md`

The worker may read these for evidence:

- `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`
- `governance/skill-library/specs/`
- `governance/skill-library/README.md`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
- `docs/concepts/skill-system.md`
- `docs/reference/`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V22_2026-06-22.md`

Creating `docs/reference/agent_system_skills/` as the parent directory of the
single contract reference doc is permitted only as the container for that one
file. The worker must not create `packages/`, `registry/`, `generated/`, any
`SKILL.md`, any `skill.source.json`, or any example package inside it.

## Forbidden Scope

The worker must not:

- commit, push, public-sync, or edit Git remotes;
- create any package root content beyond the single contract reference doc:
  no `packages/<skill-id>/`, no `SKILL.md`, no `skill.source.json`, no
  `registry/entries/`, no `generated/skill-index.json`, no example package;
- implement a resolver, generator, loader, adapter, or any runtime behavior;
- migrate or reclassify any existing CVF Web example or `governance/skill-library` entry;
- edit `.private_reference/legacy/` or re-run the full legacy scan;
- edit active session state/front door/handoff or generated session aggregate;
- modify any `governance/compat/*.py` guard, hook chain, or autorun gate;
- change GC-051 corpus registries, roadmap status, baselines, work orders, or unrelated files;
- promote legacy/provider-local content into canonical authority.

## Required Execution Steps

1. Capture startup state:
   - `git rev-parse --short HEAD`
   - `git status --short`
2. Read the required first reads, including the full ASSF-T0.1 audit ledger and
   the CVF Skill Spec.
3. Run the pre-implementation gate using the dispatch base unless the reviewer
   has provided a newer dispatch commit:
   - `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base ed7d0580 --head HEAD`
4. Build the CVF Skill Spec reconciliation table: map each of the seven CVF
   Skill Spec required sections and the four classification classes to a
   contract field or field family.
5. Build the T0.1 ledger consumption table: map each `ABSORB_AS_*` row in the
   ASSF-T0.1 absorption ledger to a contract field or an explicit deferral
   disposition with reason.
6. Author the canonical package contract reference document with all Required
   Deliverable sections.
7. Author the worker-return packet.
8. Run:
   - `python governance/compat/run_worker_return_fast_gate.py`
   - `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`
9. Return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`,
   or `BLOCKED_WITH_REASON` without committing.

## Required Deliverables

### Contract Reference Document

Path:

`docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`

Required sections:

- Purpose
- Scope / Applies To
- SKILL.md Profile
- Compact Machine Source Schema
- Identity And Authority Fields
- Risk And Lifecycle Fields
- Composition And Dependency Fields
- Internal-Agent And External-Agent CLI/MCP Disposition Fields
- Provider Adapter Boundary
- Storage Topology
- CVF Skill Spec Reconciliation Table
- ASSF-T0.1 Ledger Consumption Table
- Dual Agent Surface Matrix
- Delta Execution Claim Boundary Control Block
- Claim Boundary
- Public Export Disposition

## Worker Return Packet Shape Contract

Path:

`docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_WORKER_RETURN_2026-06-23.md`

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
a `dispatchWorkOrder:` line citing this work order, and use `N/A with reason`
or `NOT_APPLICABLE_WITH_REASON` for conditional blocks that do not apply.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | the canonical package contract this tranche defines | T1 defines the contract only; no loader, resolver, or package authority is implemented; loading must never widen authority | contract reconciliation tables and the T0.1 ledger | no adapter implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP skill discovery or load adapter | T1 defines the external-agent disposition field only; it does not implement, expose, or authorize any adapter | contract external-agent disposition field | separate ASSF adapter work required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Worker requirement |
|---|---|
| Chain map | cite `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Chain map route | legacy source family -> ASSF-T0.1 candidate ledger -> ASSF-T1 contract reconciliation -> reviewer decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T1 canonical package contract and future ASSF-T2/T4 work |
| Disposition | candidate intake only; no direct canonical authority or activation |
| Route | consume the accepted T0.1 ledger plus the CVF Skill Spec |
| Boundary | candidate input only; no direct activation or canonical authority |
| External-agent disposition | required in matrix and in the contract field |
| Claim boundary | legacy and external skills remain candidate inputs, not CVF authority |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`
- Delta ledger status: worker must refresh in the worker-return packet.
- Routing matrix status: worker must refresh in the worker-return packet.
- Semantic sampling status: worker must include at least three samples in the worker-return packet.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Worker instruction |
|---|---|
| `UNCHANGED_FROM_INTAKE` | preserve the T0.1 ledger and CVF Skill Spec as contract inputs |
| `CHANGED_DISPOSITION` | record absorption candidates moving from classified-input status to reconciled contract fields or deferrals |
| `NEW_FINDING` | record any contract field not derivable from the CVF Skill Spec or the T0.1 ledger and justify it |
| `REMOVED_OR_REJECTED` | record provider-local or unverifiable legacy claims rejected from the contract |

### Follow-Up Routing Matrix

| Routing lane | Worker instruction |
|---|---|
| `DO_NOW` | author the contract reference doc and worker-return packet |
| `SEPARATE_RUNTIME_TRANCHE` | route generated index, resolver, and CLI/MCP adapter to ASSF-T2/T5/T7 |
| `STRATEGIC_OPERATOR_DECISION` | flag package-root creation and example-package scaffolding for a later operator-selected tranche |
| `OUT_OF_SCOPE` | mark migration of existing CVF Web examples, public-sync, and runtime/provider/live out of scope |
| `RESOLVED_BY_DESIGN` | mark items handled by the contract-definition-only design |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T1-WO-S1 | roadmap ASSF-T1 tranche | reconcile, do not replace, the CVF Skill Spec | reconciliation table required | could T1 author a competing definition? | reject |
| ASSF-T1-WO-S2 | roadmap Next control action | T1 must consume the T0.1 ledger | ledger-consumption table required | could T1 skip the ledger and use the Skill Spec alone? | reject |
| ASSF-T1-WO-S3 | dual-agent standard | external CLI/MCP disposition required | matrix and contract field required | could an internal-only contract pass? | reject |

The worker must record whether this defect class should become a future
machine-check candidate. At minimum, evaluate:

- a future guard could require contract/index consistency before ASSF-T2;
- closure packets could fail if a contract omits the external-agent disposition;
- the contract should map every CVF Skill Spec required section.

## Finding-To-Governance Learning Disposition

| Field | Required worker value |
|---|---|
| Defect class | choose one or more: `RULE_GAP`, `MACHINE_GATE_GAP`, `PHASE_GATE_PLACEMENT_GAP`, `OPERATOR_SCOPE_CLARITY_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `DESIGN_REVIEW_REQUIRED`, `MACHINE_CHECK_CANDIDATE`, or `REFERENCE_ONLY` |
| Runtime/provider/cost lane | `N/A_WITH_REASON` unless a runtime/provider/cost finding arises |
| Next control action | state whether ASSF-T2/T4/T7 should absorb each control |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the contract consumes a private legacy absorption ledger. Public-safe
skill architecture output requires later redaction and public-sync authority.

## Acceptance Criteria

- Required artifacts exist in allowed paths only.
- The contract reconciles every CVF Skill Spec required section and the four
  classification classes.
- The contract maps every T0.1 `ABSORB_AS_*` ledger row to a contract field or
  an explicit deferral.
- Field families use the roadmap's candidate package contract families as the
  baseline, reconciled rather than blindly adopted.
- The Dual Agent Surface Matrix accounts for internal and external CLI/MCP
  consumers.
- No package root, `SKILL.md`, `skill.source.json`, generated index, resolver,
  example package, or migration is created.
- No commit is made by the worker.
- Reviewer-fast gates are run or failure is classified.

## Stop Conditions

Return `BLOCKED_WITH_REASON` if:

- the pre-implementation gate fails outside allowed scope;
- the ASSF-T0.1 ledger or the CVF Skill Spec is unavailable;
- the worker cannot create the two required artifacts;
- required source facts cannot be verified without exceeding allowed scope;
- a repair would require session sync, roadmap/baseline/work-order edits,
  public-sync, live/provider proof, package/root/index/resolver/adapter
  implementation, or a commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T1_CLOSED_PASS_BOUNDED_PENDING_T2_SELECTION` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_WORKER_RETURN_2026-06-23.md` | `Status: ACCEPTED_BY_REVIEWER` | PASS |
| Contract reference doc | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | no GC-051 registry or generated skill-index update authorized by T1 | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no GC-051 registry Markdown or generated skill-index update authorized by T1 | BLOCKED with reason |
| External evidence digest | N/A with reason | no external artifact digest; evidence is local governed documentation | N/A with reason |
| System loop interlock | this file | no loop, queue, daemon, runtime, or automatic activation created | PASS |
| Session continuity | active session sync after material commit if next move changes | separate session-sync lane after material commit | N/A with reason |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable files created by worker | the contract reference doc and the worker-return packet only |
| Canonical package root | DESCRIBED_NOT_CREATED: the contract describes the topology; no directory tree beyond the single contract doc's parent is created |
| Generated index or aggregate | N/A with reason: forbidden by this work order; ASSF-T2 scope |
| Storage migration | N/A with reason: out of scope; ASSF-T6 scope |
| Layout risk | bounded documentation output only; reviewer owns closure commit |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Work order status | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| Worker commit mode | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Allowed output paths | contract doc, worker-return, and reviewer-added folder README front door | contract doc, worker-return, and guard README only | PASS |
| T0.1 ledger consumption required | yes | yes | PASS |
| Package/root/index/resolver implementation | forbidden | forbidden | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | Worker-return canonical package contract definition only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - no-commit contract-definition-only worker-return dispatch |
| receiptEvidence | CVF_RECEIPT_PRESENT - worker must provide command and gate receipts in the return packet |
| actionEvidence | ACTION_EVIDENCE_PRESENT - worker must provide reconciliation tables, ledger-consumption table, and changed-set evidence |
| invocationBoundary | governed local documentation authoring |
| interceptionBoundary | no provider/runtime/API/browser interception claim |
| claimLanguage | define the canonical package contract and storage topology |
| forbiddenExpansion | no commit, package root, `SKILL.md`, `skill.source.json`, generated index, resolver, example package, migration, runtime, CLI/MCP adapter, public-sync, or active skill claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude dispatcher |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T1 dispatch, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, file authoring, governance gates, git commit by reviewer only |
| Target paths | this work order; T1 GC-018 baseline |
| Allowed scope source | operator instruction to change role and author the ASSF-T1 work order |
| Before status evidence | clean worktree at HEAD `ed7d0580` |
| After status evidence | ASSF-T1 dispatch ready |
| Diff evidence | real-range name-status and gate output before reviewer commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | worker-return lane; no contract authoring or implementation |
| Agent type | dispatcher |
| Invocation ID | `cvf-assf-t1-canonical-package-contract-work-order-2026-06-23` |
| Expected manifest | this work order; T1 GC-018 baseline |
| Actual changed set | this work order; T1 GC-018 baseline |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This work order authorizes only a no-commit, contract-definition-only
worker-return lane that defines the canonical system-skill package contract and
storage topology as a single governed reference document. It does not authorize
ASSF-T2, package root creation, `SKILL.md` or `skill.source.json` creation,
generated index, resolver, example package, migration, runtime/provider/live
proof, public-sync, CLI/MCP adapter implementation, session sync, or worker
commit.
