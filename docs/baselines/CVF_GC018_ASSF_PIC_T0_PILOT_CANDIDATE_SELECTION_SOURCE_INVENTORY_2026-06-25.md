# CVF GC-018 Baseline: ASSF-PIC-T0 Pilot Candidate Selection And Source Inventory

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-25

docType: baseline

Batch ID: ASSF-PIC-T0

## Proposed Tranche

Tranche: ASSF-PIC-T0

Baseline decision: documentation and audit tranche to select exactly one pilot
candidate from existing ASSF registry source entries, or reject/hold the pilot
candidate selection with evidence. This tranche creates no package instance and
does not change package lifecycle state.

Verdicts:

- Dispatcher verdict: DISPATCH_APPROVED
- Worker verdict: BLOCKED_WITH_REASON_ACCEPTED_AS_PROCESS_HALT
- Reviewer verdict: CLOSED_PASS_BOUNDED_WITH_T1_HOLD

## Purpose

ASSF-PIC-T0 opens the ASSF Package Instance Certification Pilot by choosing the
single candidate that later PIC tranches may harden, test, and review. Success
means a reviewer receives a source-backed candidate-selection audit that names
one selected candidate or records why no candidate can proceed, with source
inventory, selector inventory, authority boundary, and fallback disposition.

## Evidence / Verification

Dispatch evidence is limited to current roadmap authority, dependency release
evidence, source verification, ADIF disclosure, Dual Agent Surface Matrix, and
planned worker artifact paths. Worker-created audit and worker-return packets
do not exist at dispatch time and must not be claimed as complete until the
worker return supplies command-backed evidence.

## Scope / Applies To

Applies to:

- existing ASSF registry source entries under the registry source family;
- current generated index metadata for candidate discovery only;
- candidate source inventory and selector inventory;
- pilot candidate selection or rejection decision for ASSF-PIC.

Does not apply to:

- package instance creation;
- certification decision;
- generated-index mutation;
- resolver mutation;
- CVF Web runtime mutation;
- CLI/MCP adapter implementation;
- provider call, live proof, public-sync, push, package activation, or package
  instruction execution.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| ASSF Package Instance Certification Pilot roadmap | ROADMAP_READY | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md`; material commit `916c6908` |
| ASSF-T1 package contract foundation | SATISFIED | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`; material commit `2752d04e` |
| ASSF-T2 generated index and resolver foundation | SATISFIED | `docs/reference/agent_system_skills/registry/README.md`; `docs/reference/agent_system_skills/generated/skill-index.json`; material commit `3746bd48` |
| ASSF-T5 no-automatic-promotion foundation | SATISFIED | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md`; material commit `afeb2673`; reviewer repair commit `d0a24e90` |
| ASSF-T7 certification lifecycle guard | SATISFIED | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md`; material commit `e76e4d09` |
| Current session selection | SATISFIED | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V22_2026-06-22.md`; session-sync commit `4bb9fd89` |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF-PIC-T0 candidate-selection audit and worker-return packet | internal agents may inspect current registry source entries and select exactly one candidate or reject/hold selection; no package state, generated index, resolver, Web, commit, activation, or certification authority is granted | ASSF-PIC roadmap, T1 package contract, registry README, generated index, T7 guard contract, this baseline | no internal loader, resolver, generator, package root, or Web bridge is implemented by this tranche | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external package readout or adapter claim | external agents cannot certify, mutate, activate, execute, or consume package instructions through this tranche | Dual Agent Surface Accounting Standard and T1/T7 adapter boundary rules | adapter implementation is deferred; a later source-verified adapter work order is required before `IMPLEMENTED` external disposition is allowed | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-PIC roadmap requires PIC-T0 as first tranche | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | Design Control Gate | `PIC-T0` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |
| ASSF-PIC-T0 required outputs include GC-018 baseline, source-verified work order, candidate-selection audit, completion review, and explicit decision | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | ASSF-PIC-T0 section | `PILOT_CANDIDATE_SELECTED` | ASSF-PIC roadmap | VALUE_SET | ACCEPT |
| ASSF-PIC fail conditions forbid generated-index mutation without a dedicated tranche | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | Fail Conditions | `generated index` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |
| T1 defines package identity fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `skillId` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 defines selector fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `roles` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 defines lifecycle and certification fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `certificationState` | ASSF-T1 package schema | EXISTS | ACCEPT |
| Registry source README names entry sources as authoritative for candidates | `docs/reference/agent_system_skills/registry/README.md` | Purpose | `entries/` | ASSF-T2 registry source family | LITERAL_INVARIANT | ACCEPT |
| Registry source README forbids hand-editing generated index | `docs/reference/agent_system_skills/registry/README.md` | Purpose | `skill-index.json` | ASSF-T2 registry source family | LITERAL_INVARIANT | ACCEPT |
| Current generated index is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | `claimBoundary` | `claimBoundary` | ASSF-T2 generated index | LITERAL_INVARIANT | ACCEPT |
| Existing candidate entry `cvf-dispatch-quality-reviewer` exists | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `skillId` | ASSF-T2 registry source entry | EXISTS | ACCEPT |
| Existing candidate entry `cvf-worker-return-author` exists | `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json` | root object | `skillId` | ASSF-T2 registry source entry | EXISTS | ACCEPT |
| T7 certification lifecycle guard blocks certification without UAT evidence | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `uatState` | ASSF-T7 certification lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| Dual Agent standard requires external-agent row and adapter boundary | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Mandatory Dual Agent Surface Matrix | `EXTERNAL_AGENT_CLI_MCP` | Dual Agent Surface Accounting Standard | VALUE_SET | ACCEPT |
| Governed artifact literal-format gotchas checklist exists | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Purpose | `CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Governed Artifact Literal Format Gotchas | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Runtime or source claim | Verification command or source | Dispatch result | Worker requirement |
|---|---|---|---|
| Candidate audit path absent before dispatch | `Test-Path docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | `False` | create path |
| Worker return path absent before dispatch | `Test-Path docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_WORKER_RETURN_2026-06-25.md` | `False` | create path |
| Completion review path absent before dispatch | `Test-Path docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` | `False` | do not create; reviewer-owned |
| Current registry source entries are discoverable | `Get-ChildItem docs/reference/agent_system_skills/registry/entries` | two JSON source entries observed | worker must re-run and record exact command output |
| Generated index mutation is not authorized | this baseline and matching work order | generated index is not in worker-owned paths | preserve |
| Resolver mutation is not authorized | this baseline and matching work order | resolver source is not in worker-owned paths | preserve |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied:

- ADIF-0001: This baseline names only the observed registry source family and
  requires the worker to record exact enumeration commands before any candidate
  count or coverage claim.
- ADIF-0002: ACCEPT rows cite CVF-governed repository files only.
- ADIF-0007: Evidence rows use concrete source facts instead of keyword-heavy
  exclusion prose.
- ADIF-0006: Verified path or symbol cells contain only field, path, section,
  function, or token names.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator request to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline and the matching ASSF-PIC-T0 work order |
| Disposition | local candidate-selection dispatch only; no external material is absorbed |
| Claim boundary | operator direction selects the next ASSF lane; package facts must still be source-verified before any later package-instance tranche |

## Required Worker Deliverables

| Path | Required at worker return | Purpose |
|---|---|---|
| `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | Yes | Candidate-selection audit with source inventory, selector inventory, authority boundary, and decision |
| `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_WORKER_RETURN_2026-06-25.md` | Yes | Worker return with evidence, changed files, gate receipts, and review boundary |

## Reviewer-Owned Closure Deliverables

| Path | Owner | Purpose |
|---|---|---|
| `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` | Codex reviewer/closer | Completion review after worker return |
| this baseline | Codex reviewer/closer | Final status conversion after review |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_FOR_CLAUDE_2026-06-25.md` | Codex reviewer/closer | Final status conversion after review |
| `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | Codex reviewer/closer | PIC-T0 status row update after review |
| active session front door and active handoff | Codex session-sync steward | Session continuity after material review commit |

## Planned Output Filesystem State At Dispatch

| Path | Dispatch-time state | Required worker action |
|---|---|---|
| `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | ABSENT | create |
| `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_WORKER_RETURN_2026-06-25.md` | ABSENT | create |
| `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` | ABSENT | do not create; reviewer-owned |

## Acceptance Criteria

| Criterion | Required disposition |
|---|---|
| Candidate-selection audit enumerates current registry source entries with command-backed evidence | PASS |
| Audit selects exactly one pilot candidate or records `PILOT_CANDIDATE_REJECTED` with reason | PASS - selected `cvf-dispatch-quality-reviewer` |
| Audit records source inventory, selector inventory, authority boundary, and rejection fallback | PASS |
| Audit preserves T1 package schema, T2 metadata-only boundary, and T7 certification lifecycle boundary | PASS |
| Audit includes Dual Agent Surface Matrix with internal and external rows | PASS |
| Worker return includes changed files, gate evidence, execution base, and claim boundary | PASS - `BLOCKED_WITH_REASON` return accepted as process evidence |
| Worker does not edit generated index, resolver, registry source entries, package instance files, Web runtime, session state, public-sync, or adapter source | PASS |
| Worker does not commit | PASS |

## Fail Conditions

Return `BLOCKED_WITH_REASON` if any condition is true:

- more than one pilot candidate is selected;
- a selected candidate lacks source-backed identity or selector evidence;
- package instance creation becomes necessary;
- certification, UAT pass, generated-index update, resolver update, Web runtime
  change, CLI/MCP adapter behavior, provider/live proof, public-sync, push, or
  package activation becomes necessary;
- source verification uses provider-local memory as authority;
- a gate failure cannot be repaired inside worker-owned audit or worker-return
  paths.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-PIC-T0 pilot candidate selection and source inventory dispatch |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch baseline only |
| receiptEvidence | N/A with reason: no runtime execution, provider call, or adapter receipt exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and artifact manifest |
| invocationBoundary | governed local documentation and audit dispatch only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes a bounded no-commit candidate-selection audit for Claude worker execution |
| forbiddenExpansion | no package instance, certification decision, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, or package instruction execution |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this dispatch references private provenance architecture and repository
source surfaces. Public-safe export requires a separate redaction and
public-sync authorization.

## Closure Package

| Closure item | Required artifact/path | Evidence | Status |
|---|---|---|---|
| Roadmap source | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | PIC-T0 `CLOSED_PASS_BOUNDED`; PIC-T1 `HOLD_UNTIL_STATE_BOOTSTRAP_REFACTOR` | PASS |
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_FOR_CLAUDE_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker output paths | worker return and reviewer-owned audit/completion | worker return `BLOCKED_WITH_REASON`; audit `COMPLETE_PENDING_REVIEW`; completion `CLOSED_PASS_BOUNDED` | PASS |
| External adapter boundary | this file | Dual Agent Surface Matrix | PASS |
| Runtime implementation | N/A with reason | runtime implementation is forbidden in this tranche | N/A with reason |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_FOR_CLAUDE_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | PIC-T0 `CLOSED_PASS_BOUNDED`; PIC-T1 held for Active Session State Bootstrap Read Model And Aggregate Size Refactor | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | not authorized for PIC-T0 closure; no GC-051 corpus registry mutation in scope | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | not authorized for PIC-T0 closure; no GC-051 corpus registry mutation in scope | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported | N/A with reason |
| System loop interlock | this baseline | PIC-T0 selected one candidate; PIC-T1 held for state-bootstrap/read-model refactor | PASS |
| Session continuity | N/A with reason | session-sync is split into a separate follow-up commit by commit split rule | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence absent for T0 | `receiptEvidence` is `N/A with reason` | PASS |
| Candidate decision recorded | `PILOT_CANDIDATE_SELECTED` | PASS |
| Selected candidate recorded | `cvf-dispatch-quality-reviewer` | PASS |
| PIC-T1 release blocked | state-bootstrap/read-model refactor required before PIC-T1 | PASS |

## Claim Boundary

This baseline authorizes only ASSF-PIC-T0 candidate-selection audit work. It
does not create or certify a package, mutate the generated index, modify the
resolver, change CVF Web runtime source, implement a CLI/MCP adapter, activate
or execute any skill, run provider/live proof, export public artifacts, push to
any remote, or update session continuity by worker action.
