# CVF Agent Work Order: ASSF-PIC-T0 Pilot Candidate Selection And Source Inventory

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-25

docType: work_order

Batch ID: ASSF-PIC-T0

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `4bb9fd89`

executionBaseHead: capture with `git rev-parse --short HEAD` before edits

closureBaseHead: `f013e7d5`

## Dispatch Prompt Envelope

Role: Claude worker for ASSF-PIC-T0 Pilot Candidate Selection And Source
Inventory.

Canonical packet: this work order plus
`docs/baselines/CVF_GC018_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_2026-06-25.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

dispatchBaseHead: `4bb9fd89`.

executionBaseHead: worker captures with `git rev-parse --short HEAD` before
first material edit.

Current-time notes: dispatch date is 2026-06-25.

Required first actions: read this work order, the GC-018 baseline, startup
front doors, Guard Orientation, Governed Artifact Literal Format Gotchas,
Required First Reads, and ADIF disclosures; capture `git status --short` and
`git rev-parse --short HEAD`; run pre-implementation gate before material
edits.

Do-not-misread notes: PIC-T0 selects exactly one candidate or rejects/holds
selection with evidence. Do not create package instances, `SKILL.md`,
`skill.source.json`, registry entries, generated-index changes, resolver
changes, Web runtime changes, certification decisions, UAT pass claims,
CLI/MCP adapters, provider/live proof, public-sync, push, commit, or
session-sync edits.

Return contract: return `COMPLETE_PENDING_REVIEW` if the audit and worker
return are complete inside Allowed scope, or `BLOCKED_WITH_REASON` if source
evidence or scope prevents completion. Do not commit.

## Purpose

Dispatch Claude to execute ASSF-PIC-T0 by producing a source-backed
candidate-selection audit for the ASSF Package Instance Certification Pilot.
The audit must choose exactly one candidate from current ASSF registry source
entries, or reject/hold candidate selection with evidence, before any later
package-instance or certification work can begin.

## Objective

Create a bounded audit that records:

- current candidate source inventory;
- identity, selector, authority, lifecycle, and external-adapter evidence for
  each inspected candidate;
- exactly one selected pilot candidate or a rejection/hold decision;
- a fallback rule if the selected candidate later proves unsuitable;
- clear boundary that no package instance, certification, generated-index,
  resolver, Web, adapter, live, public, push, or activation behavior is
  released.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Create source-verified GC-018 baseline and work order |
| Worker | Claude | Author candidate-selection audit and worker return without committing |
| Reviewer/closer | Codex | Review Claude output, repair minor allowed findings if needed, commit material closure |
| Session-sync steward | Codex | Update active session state, handoff, and front door after review |

## Operator Checkpoint

Operator requested a Claude work order after the ASSF-PIC roadmap was created
and session-synced. No additional operator checkpoint is required before Claude
starts, provided Claude stays inside Allowed scope and returns
`BLOCKED_WITH_REASON` for any forbidden-scope need.

## Authority Chain

| Authority | Path |
|---|---|
| Operator instruction | chat request on 2026-06-25: create work order for Claude |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` |
| ASSF-PIC roadmap | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` |
| GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_2026-06-25.md` |
| ASSF-T1 package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` |
| ASSF-T2 registry source README | `docs/reference/agent_system_skills/registry/README.md` |
| ASSF-T2 generated index | `docs/reference/agent_system_skills/generated/skill-index.json` |
| ASSF-T7 certification lifecycle guard | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` |
| Dual Agent Surface Accounting Standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` |
| Governed Artifact Literal Format Gotchas | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` |

Authority boundary:

- If this work order conflicts with the GC-018 baseline, the baseline and
  canonical standards control.
- If source verification contradicts a planned field or claim, stop and return
  `BLOCKED_WITH_REASON`.
- Provider-local memory, chat summaries, or Claude-specific files are not CVF
  authority.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatches; Claude authors candidate-selection audit and worker return; Codex reviews, closes, commits, and session-syncs |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=4bb9fd89`; `executionBaseHead` confirmed by Claude; `closureBaseHead` set by Codex before closure commit |
| changedSetScope(phase) | Claude changes only the two allowed worker deliverables; Codex owns completion review, status conversion, roadmap update, commit, and session-sync if accepted |
| traceScope(phase, actor) | one Claude worker-return trace covers candidate audit and worker return; one Codex trace covers review/closure if accepted |
| commitOwner(phase) | Claude commits nothing (`WORKER_MUST_NOT_COMMIT`); Codex owns any material/closure/session-sync commit |
| crossBatchIsolation | no package instance, generated-index, resolver, Web, adapter, public-sync, or unrelated cleanup work is authorized |
| Before status evidence | clean worktree at dispatch base `4bb9fd89` before PIC-T0 packet authoring |
| nextMoveSurfaces | Claude must not edit active session state, active handoff, front door, generated active-session aggregate, roadmap closure rows, or session-sync surfaces |
| Closer designation | Codex is the designated reviewer and closer |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md`
- `docs/baselines/CVF_GC018_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_2026-06-25.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_FOR_CLAUDE_2026-06-25.md`
- `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md`
- session front-door/state/handoff paths only if Codex changes current mode or
  next allowed move after accepting the worker return.

Claude must not create the completion review and must not mark the work closed.

## Scope

Allowed scope:

- Create `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md`.
- Create `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_WORKER_RETURN_2026-06-25.md`.
- Codex reviewer/closer may create `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md`.
- Codex reviewer/closer may update `docs/baselines/CVF_GC018_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_2026-06-25.md`.
- Codex reviewer/closer may update `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_FOR_CLAUDE_2026-06-25.md`.
- Codex reviewer/closer may update `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md`.
- Run read-only source verification, registry enumeration, generated-index
  inspection, and governance gates.
- Update no other file unless a gate failure inside Allowed scope requires a
  narrowly scoped repair in one of the two allowed worker deliverables.
- Codex reviewer/closer may update this work order, matching GC-018 baseline,
  roadmap, completion review, and session-sync surfaces after review.

Forbidden scope:

- Commit, push, public-sync, or publication.
- Package instance creation, including `SKILL.md`, `skill.source.json`,
  package folders, registry entry creation, or lifecycle-state mutation.
- Generated-index edits under `docs/reference/agent_system_skills/generated/`.
- Registry source entry edits under `docs/reference/agent_system_skills/registry/entries/`.
- Any existing `governance/compat/` checker, generator, or resolver edit.
- Runtime CVF Web route, component, action, API, service, loader, test, UI, or
  data implementation.
- Certification decision, UAT pass claim, package activation, or package
  instruction execution.
- External CLI/MCP adapter implementation or external-agent runtime behavior.
- Provider call, live proof, secret use, or public repository operation.
- Active session state, active handoff, session front door, generated active
  session aggregate, or agent workspace state edits.
- Roadmap closure update, baseline closure conversion, work-order closure
  conversion, or completion review creation.

Risk ceiling: R1 documentation and audit only.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied:

- ADIF-0001: Worker must record exact enumeration commands and avoid claiming
  more registry or candidate coverage than the commands prove.
- ADIF-0002: Worker must cite CVF-governed docs or repository source files,
  not provider-local memory, for every source fact.
- ADIF-0007: Worker must keep keyword-heavy exclusions out of evidence rows
  unless they are direct source facts.
- ADIF-0006: Worker Source Verification symbol cells must contain bare
  symbols, paths, sections, or tokens only.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake source | operator-originated ASSF-PIC-T0 work-order request |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| scope classification | R1 documentation and audit only |
| risk sensitivity | R1; no package instance, certification, generated-index, resolver, Web, adapter, provider/live, public-sync, push, or commit authority |
| selected role route | Codex dispatcher; Claude worker; Codex reviewer/closer; Codex session-sync steward |
| Intake authority | ASSF-PIC roadmap, PIC-T0 GC-018 baseline, and this work order |
| Runtime/source modification | not authorized |
| External evidence intake | not authorized by this work order |
| Disposition | route to no-commit candidate-selection audit worker execution |
| escalation condition | scope expansion, forbidden paths, provider/live, public-sync, secrets/quota, dependency install, destructive actions, commit request, or claim-boundary change |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator request to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this ASSF-PIC-T0 work order and matching GC-018 baseline |
| Disposition | Claude worker executes local candidate-selection audit only; no external material is absorbed |
| Claim boundary | no external-agent packet, adapter behavior, public claim, or provider proof is accepted as source authority |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: worker must re-read current CVF-governed sources before citing source facts.

unicodePathHandling: literal path or UTF-8 reader required.

extractedTextAuthority: N/A with reason

priorVerificationUse: prior closure commits are dependency-release evidence
only; worker must re-read current CVF-governed sources before citing source
facts.

encodingBoundary: agent-authored artifacts default to ASCII; repository paths
may contain existing Unicode outside artifact prose.

## Required First Reads

Before editing material artifacts, read:

1. `CVF_SESSION_MEMORY.md` - startup front door and current mode.
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json` - active handoff pointer and current mode.
3. `AGENT_HANDOFF_V22_2026-06-22.md` - current handoff and next allowed move.
4. `docs/reference/guard_orientation/README.md` - task-class guard orientation.
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` - literal-format traps.
6. `docs/baselines/CVF_GC018_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_2026-06-25.md` - lane baseline.
7. `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` - PIC roadmap source.
8. `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` - canonical package fields and lifecycle.
9. `docs/reference/agent_system_skills/registry/README.md` - registry source-family rules.
10. `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` - candidate source entry.
11. `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json` - candidate source entry.
12. `docs/reference/agent_system_skills/generated/skill-index.json` - metadata-only generated index.
13. `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` - certification and UAT boundary.
14. `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` - mandatory dual-agent matrix.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Worker deliverable | Evidence required |
|---|---|---|---|
| PIC-T0 selects exactly one pilot candidate or rejects/holds selection | Objective; Required Audit Shape | candidate-selection audit | audit decision token and source-backed rationale |
| Source-verify package identity, authority, selectors, evidence, and lifecycle fields | Source-Fidelity Pass; Required First Reads | candidate-selection audit Source Verification Block | rows citing current registry source entries and T1/T7 fields |
| Do not change generated index, resolver, Web runtime, package lifecycle state, or external adapter | Scope; Forbidden Path Manifest; Claim Boundary | worker return and changed-file manifest | `git diff --name-status` evidence |
| Produce candidate-selection audit, completion review, and explicit decision | Required Worker Deliverables; Reviewer Closure Conversion | audit, worker return, reviewer-owned completion review | worker return plus Codex completion review |
| Preserve Dual Agent Surface Matrix | Dual Agent Surface Matrix | audit and worker return | both consumer rows with adapter boundary |
| Keep later tranches dependency-held | Return-To-Orchestrator Conditions; Claim Boundary | worker return | no PIC-T1 release claim by worker |

## Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 4bb9fd89 --head HEAD
```

Expected results:

- `git status --short` has no unrelated dirty files before worker edits.
- Pre-implementation gate passes or fails only on issues the worker can repair
  inside Allowed scope.

If a pre-flight check fails outside Allowed scope, stop and return
`BLOCKED_WITH_REASON` with command output.

## Source-Fidelity Pass

Before writing audit claims, verify every named field, function, schema key,
status, candidate file, and path against current repository source. Do not
promote provider-local memory into authority.

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-PIC roadmap requires PIC-T0 as first tranche | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | Design Control Gate | `PIC-T0` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |
| ASSF-PIC-T0 required outputs include candidate-selection audit and explicit decision | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | ASSF-PIC-T0 section | `PILOT_CANDIDATE_SELECTED` | ASSF-PIC roadmap | VALUE_SET | ACCEPT |
| T1 defines package identity field | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `skillId` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 defines selector fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `roles` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 defines lifecycle field | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `candidateState` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 defines external disposition field | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Internal-Agent And External-Agent CLI/MCP Disposition Fields | `externalCliMcpDisposition` | ASSF-T1 package schema | EXISTS | ACCEPT |
| Registry source README names entry sources as authoritative for candidates | `docs/reference/agent_system_skills/registry/README.md` | Purpose | `entries/` | ASSF-T2 registry source family | LITERAL_INVARIANT | ACCEPT |
| Registry source README forbids hand-editing generated index | `docs/reference/agent_system_skills/registry/README.md` | Purpose | `skill-index.json` | ASSF-T2 registry source family | LITERAL_INVARIANT | ACCEPT |
| Current generated index is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | `claimBoundary` | `claimBoundary` | ASSF-T2 generated index | LITERAL_INVARIANT | ACCEPT |
| Candidate source entry `cvf-dispatch-quality-reviewer` exists | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `skillId` | ASSF-T2 registry source entry | EXISTS | ACCEPT |
| Candidate source entry `cvf-worker-return-author` exists | `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json` | root object | `skillId` | ASSF-T2 registry source entry | EXISTS | ACCEPT |
| T7 certification lifecycle guard blocks certification without UAT evidence | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `uatState` | ASSF-T7 certification lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| Dual Agent standard requires external row and adapter boundary | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Mandatory Dual Agent Surface Matrix | `EXTERNAL_AGENT_CLI_MCP` | Dual Agent Surface Accounting Standard | VALUE_SET | ACCEPT |

### Current Runtime Freshness Verification

Worker must record fresh command-backed evidence in the candidate-selection
audit:

```powershell
Get-ChildItem -LiteralPath docs/reference/agent_system_skills/registry/entries -Filter *.json | Select-Object -ExpandProperty Name | Sort-Object
Get-Content -Raw -LiteralPath docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json
Get-Content -Raw -LiteralPath docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json
python governance/compat/check_assf_skill_index_drift.py
```

## Worker Autonomy / No-Question Rule

Claude proceeds without operator confirmation for non-destructive actions inside
Allowed scope, including format remediation and rerunning failed gates after an
allowed-scope fix.

Escalate only if remediation would require package instance creation,
generated-index edit, resolver edit, registry source mutation, Web runtime
change, external adapter work, public-sync, live provider proof, secret use,
destructive action, risk increase, commit, or a claim-boundary change.

## System Loop Interlock Routing

Upstream loop: ASSF-T1 through ASSF-T7 architecture, generated metadata,
composition, Web projection, and certification lifecycle foundation.

Downstream loop: ASSF-PIC-T1 package instance evidence and skeleton hardening.

Routing rule: PIC-T1 remains held until Codex accepts a PIC-T0 completion
review that records `PILOT_CANDIDATE_SELECTED`. If PIC-T0 returns
`PILOT_CANDIDATE_REJECTED`, downstream work returns to operator or a new
PIC-T0 replacement-selection work order.

Claim boundary: the audit is a candidate-selection handoff artifact, not an
autonomous package promotion, package instance, certification, or activation
mechanism.

## Planned Worker Fulfillment Manifest

## Planned Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | Yes | Candidate-selection audit |
| `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_WORKER_RETURN_2026-06-25.md` | Yes | Claude worker return |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Codex owns session-sync |
| `CVF_SESSION/state/` | Codex owns generated active session source |
| `CVF_SESSION_MEMORY.md` | Codex owns session front door |
| `AGENT_HANDOFF_V22_2026-06-22.md` | Codex owns active handoff sync |
| `docs/reference/agent_system_skills/generated/skill-index.json` | PIC-T0 does not mutate generated index |
| `docs/reference/agent_system_skills/registry/entries/` | PIC-T0 reads existing entries but does not edit registry sources |
| `governance/compat/` | PIC-T0 does not edit checkers, generators, or resolvers |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/` | PIC-T0 does not edit Web runtime/source files |

## Planned Output Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | ABSENT | ABSENT | N/A with reason |
| `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_WORKER_RETURN_2026-06-25.md` | ABSENT | ABSENT | N/A with reason |
| `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` | ABSENT | ABSENT | N/A with reason |

## Planned Proof Requirements

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| Candidate audit status | `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | `Status: COMPLETE_PENDING_REVIEW` | Yes |
| Candidate decision | candidate-selection audit | `PILOT_CANDIDATE_SELECTED` or `PILOT_CANDIDATE_REJECTED` | Yes |
| Single-candidate boundary | candidate-selection audit | `exactly one` | Yes |
| External disposition | candidate-selection audit and worker return | `EXTERNAL_AGENT_CLI_MCP` | Yes |
| Worker return | `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_WORKER_RETURN_2026-06-25.md` | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` | Yes |
| No activation claim | worker-created artifacts | `no package activation` | Yes |

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | Claude | create only |
| `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_WORKER_RETURN_2026-06-25.md` | Claude | create only |
| `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` | Codex | reviewer-owned; Claude must not create |
| `docs/baselines/CVF_GC018_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_2026-06-25.md` | Codex | closure conversion only |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_FOR_CLAUDE_2026-06-25.md` | Codex | closure conversion only |
| `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | Codex | PIC-T0 status rows only after review |
| Any other path | Not Claude | forbidden unless Codex issues a revised work order |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation family | ASSF Package Instance Certification Pilot |
| Durable roadmap | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` |
| Audit root | `docs/audits/` |
| Review root | `docs/reviews/` |
| Index or front-door update | N/A with reason: no generated index or README update is required by this tranche |
| Storage boundary | audit and review files are documentation surfaces, not package roots or generated aggregates |
| Future migration boundary | any package root, generated-index, resolver, or Web runtime storage change requires a later work order |

## Required Audit Shape

Create `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` with these sections:

| Required section | Minimum content |
|---|---|
| Status and decision | `Status: COMPLETE_PENDING_REVIEW`; decision token `PILOT_CANDIDATE_SELECTED` or `PILOT_CANDIDATE_REJECTED` |
| Purpose | explain why PIC-T0 selects or rejects a single pilot candidate |
| Candidate source inventory | command-backed list of current registry source entries |
| Candidate comparison matrix | one row per inspected candidate with identity, selectors, lifecycle fields, evidence, authority ceiling, side effects, adapter disposition, and pilot fit |
| Selected candidate or rejection rationale | exactly one selected `skillId`, or rejection/hold reason |
| Source inventory for selected candidate | source artifacts, canonical root, review artifacts, and missing-evidence notes |
| Selector inventory | roles, phases, surfaces, risk ceiling, context profile, and forbidden contexts if present |
| Authority boundary | what later PIC-T1 may and may not use from the selected candidate |
| Rejection fallback | what happens if the candidate proves unsuitable later |
| Dual Agent Surface Matrix | internal and external rows with adapter boundary |
| Source Verification Block | source-backed rows for every candidate/source fact |
| Public Export Disposition | `DEFERRED_PRIVATE_ONLY` unless separate export authority exists |
| Claim Boundary | no package instance, certification, generated-index mutation, resolver mutation, Web runtime, adapter, provider/live, public-sync, push, activation, or package instruction execution |

## Worker Return Packet Shape Contract

Create `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_WORKER_RETURN_2026-06-25.md` with:

| Required section | Minimum content |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| executionBaseHead | `git rev-parse --short HEAD` result captured before edits |
| Changed files | exact `git diff --name-status` output or equivalent command-backed list |
| Gate receipts | pre-implementation gate and worker-return fast gate outputs, or blocked diagnostic |
| Source verification | sources used for every identity, selector, lifecycle, evidence, and adapter claim |
| ADIF reflection | whether any repeated non-obvious defect pattern was observed and whether a new ADIF entry is needed |
| Claim boundary | no commit, no closure, no runtime, no adapter, no session-sync |

Claude's worker return must include these always-required sections:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Claim Boundary
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- executionBaseHead
- git status --short

Claude's worker return must include or explicitly mark `N/A with reason` for
these conditional gate sections:

- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

Return vocabulary:

- success: `COMPLETE_PENDING_REVIEW`
- blocked: `BLOCKED_WITH_REASON`
- no commit: `WORKER_MUST_NOT_COMMIT`

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Read all Required First Reads and preserve unrelated dirty paths.
3. Run pre-implementation gate from `dispatchBaseHead`.
4. Enumerate current registry source entries and generated-index metadata.
5. Compare each current candidate source entry against T1, T7, and PIC-T0
   requirements.
6. Create the candidate-selection audit with one selected candidate or
   rejection/hold decision.
7. Create the worker return with command-backed evidence.
8. Run the required gates and repair allowed-scope failures.
9. Return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` with no commit.

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | ASSF-PIC Scope and Design Control Gate | candidate-selection audit only | PASS |
| Non-goals | ASSF-PIC Non-Goals | bulk migration, activation, adapter, runtime, public, and certification claims blocked | PASS |
| Lane split | ASSF-PIC-T0 section | executes only candidate selection and source inventory | PASS |
| Dependency/source-verification plan | roadmap Dependency Release Evidence and Source Verification Block | this work order carries current source verification and re-read requirement | PASS |
| Claim boundary | roadmap Claim Boundary | no package instance, certification, generated-index, resolver, Web, adapter, live, public, push, or activation claim | PASS |
| Acceptance criteria | roadmap Acceptance Criteria | concrete audit and worker-return outputs required | PASS |
| Verification/evidence | roadmap Verification / Evidence | pre-dispatch, pre-implementation, and worker-return evidence required | PASS |
| Dispatch-readiness decision | roadmap says PIC-T0 is the only next work-order candidate | T0 is dispatched as the first child work order | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | PIC-T0 candidate-selection audit and worker return | may read source inventory and candidate decision; cannot infer package activation, certification, generated-index update, resolver behavior, Web projection, commit authority, or next-tranche release | ASSF-PIC roadmap, T1 package contract, registry source entries, generated index metadata, T7 lifecycle guard | no internal loader, resolver, generator, package root, or Web bridge is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external package readout or adapter claim | no external agent may mutate, certify, activate, execute, or consume package instructions through PIC-T0 | Dual Agent standard and T1/T7 external-adapter boundary rules | deferred adapter owner; separate work order required before any CLI/MCP exposure | `DEFERRED_WITH_REASON` |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Agent type | dispatcher and delegated worker |
| Actor | Codex dispatcher; Claude worker; Codex reviewer |
| Provider or surface | Codex local repo dispatch; Claude local repo worker execution |
| Invocation ID | `cvf-assf-pic-t0-candidate-selection-dispatch-2026-06-25` |
| Session or invocation | dispatchBaseHead `4bb9fd89`; worker records executionBaseHead |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git, governance Python gates |
| Target paths | PIC-T0 baseline, work order, candidate-selection audit, worker return |
| Allowed scope source | operator instruction, ASSF-PIC roadmap, GC-018 baseline, this work order |
| Before status evidence | dispatcher: clean worktree at `4bb9fd89`; worker must refresh |
| After status evidence | pending worker execution |
| Diff evidence | pending worker execution |
| Expected manifest | PIC-T0 baseline, work order, candidate-selection audit, worker return, completion review after Codex review |
| Actual changed set | pending worker execution |
| Manifest delta | pending worker execution |
| Approval boundary | material PIC-T0 documentation and audit only |
| Claim boundary | repo-local trace only; no OS/user identity proof |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one of the two current ASSF registry candidates
will be more suitable for the first pilot because it has clearer source
artifacts, lower side effects, and better review evidence than the other
candidate.

Evidence Comparison Requirement: worker return compares actual candidate
source inventory against the prediction.

Contradiction Handling Requirement: if neither candidate is suitable, the audit
must use `PILOT_CANDIDATE_REJECTED` and explain the blocking evidence rather
than selecting a weak candidate.

Claim Update Requirement: worker return records whether the candidate-selection
claim was confirmed, narrowed, or rejected.

## Evidence Requirements

Required evidence:

- command-backed enumeration of current registry source entries;
- candidate comparison matrix;
- source inventory and selector inventory for every inspected candidate;
- Source Verification Block in the audit;
- Dual Agent Surface Matrix in the audit and worker return;
- changed-file manifest from `git diff --name-status`;
- gate receipts;
- explicit no-package-instance/no-certification/no-generated-index/no-resolver
  no-Web/no-adapter/no-live/no-public/no-push claim boundary.

Base-anchor evidence:

- `dispatchBaseHead`: `4bb9fd89`
- `executionBaseHead`: worker captures before edits
- `closureBaseHead`: Codex captures before review closure
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Pending-artifact component gates: worker records actual commands and results
- Committed-range `pre-closure`: Codex reviewer records only after material
  commit exists

## Acceptance Criteria

| Criterion | Closure disposition |
|---|---|
| Candidate-selection audit exists and is marked `Status: COMPLETE_PENDING_REVIEW` | PASS |
| Candidate source inventory is command-backed and names current registry source entries | PASS |
| Candidate comparison matrix covers identity, selectors, lifecycle fields, evidence, authority, side effects, and adapter disposition | PASS |
| Audit selects exactly one candidate with `PILOT_CANDIDATE_SELECTED` or rejects selection with `PILOT_CANDIDATE_REJECTED` | PASS - selected `cvf-dispatch-quality-reviewer` |
| Selected candidate, if any, has a source-backed `skillId`, `canonicalRoot`, `sourceArtifacts`, `roles`, `phases`, `surfaces`, `riskCeiling`, `uatState`, and `certificationState` | PASS |
| Audit includes rejection fallback and downstream PIC-T1 hold boundary | PASS - PIC-T1 held pending Active Session State Bootstrap Read Model And Aggregate Size Refactor |
| Dual Agent Surface Matrix appears with both consumer classes and adapter boundary | PASS |
| Worker return includes gate evidence, changed files, execution base, and claim boundary | PASS - worker returned `BLOCKED_WITH_REASON`, accepted as correct process halt |
| No forbidden paths are changed | PASS |
| Worker does not commit | PASS |

Fail condition dispositions:

| Fail condition | Closure disposition |
|---|---|
| More than one pilot candidate is selected | ABSENT |
| Candidate is selected without source-backed identity or selector evidence | ABSENT |
| Any artifact claims certification, package activation, package instance creation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter behavior, provider/live proof, public-sync, push, or package instruction execution | ABSENT |
| Source Verification uses provider-local memory as authority | ABSENT |
| A required gate fails outside Allowed scope | PRESENT_FOR_WORKER_PREFLIGHT_AND_RESOLVED_BY_REVIEWER_OWNED_COMPLETION_AFTER_OPERATOR_INSTRUCTION |

Closure is blocked if any fail condition is present.

## Review Gate

Implementation may proceed only after:

- this work order and its GC-018 baseline exist;
- pre-dispatch gate passed for dispatcher artifacts;
- worker pre-implementation gate passes before material edits.

Closure may proceed only after:

- worker returns `COMPLETE_PENDING_REVIEW` or explains `BLOCKED_WITH_REASON`;
- Codex review finds no blocking source-fidelity, authority, external-agent,
  generated-index, resolver, Web, certification, activation, or session-sync
  defect;
- Codex material commit exists if the worker output is accepted;
- pre-closure gate passes on the material range.

## Closure Checklist

| Checklist item | Closure disposition |
|---|---|
| All acceptance criteria satisfied or marked `N/A with reason` | PASS |
| Fail conditions checked and absent or returned `BLOCKED_WITH_REASON` | PASS |
| Required artifacts exist | PASS |
| Worker changed-file set is inside Allowed scope | PASS |
| Gate evidence is current and command-backed | PASS |
| Roadmap-to-work-order trace is resolved | PASS |
| Dual Agent Surface Matrix remains present in closure artifacts | PASS |
| Public Export Disposition is recorded | PASS |
| No open checklist residue remains after closure conversion | PASS |
| Codex session-sync happens only after review closure | N/A with reason: session-sync is split into a separate follow-up commit by commit split rule |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without continuing if:

- pre-implementation gate fails outside Allowed scope;
- source verification finds a missing required source path or invented field;
- neither current candidate can be selected and no source-backed replacement is
  authorized;
- a needed action would touch forbidden paths;
- package instance creation or certification becomes necessary to satisfy the
  task;
- external adapter behavior is required;
- public/provenance boundary becomes unclear;
- provider/live proof or secret use becomes necessary;
- session-sync is required before material work can continue.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-PIC-T0 candidate-selection audit and worker return |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- worker documentation/audit tranche only |
| receiptEvidence | N/A with reason: no runtime/provider/adapter receipt is authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- worker must provide enumeration commands, gate evidence, and changed-file manifest |
| invocationBoundary | governed local repository documentation and audit execution only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, or Web runtime interception claim |
| claimLanguage | worker may select or reject one pilot candidate with source inventory; worker may not implement, certify, activate, or expose it |
| forbiddenExpansion | no package instance, certification decision, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, commit, active handoff, front door, or session state edit |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch and architecture work. Public-safe export
requires later redaction and public-sync authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | PIC-T0 `CLOSED_PASS_BOUNDED`; PIC-T1 `HOLD_UNTIL_STATE_BOOTSTRAP_REFACTOR` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | PIC-T0 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | PIC-T0 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported; external-agent boundary is deferred | N/A with reason |
| System loop interlock | this work order | PIC-T0 routes roadmap selection to candidate-selection evidence; PIC-T1 remains held until the state-bootstrap/read-model refactor is handled | PASS |
| Session continuity | N/A with reason | session-sync is split into a separate follow-up commit by commit split rule | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence absent for T0 | `receiptEvidence` is `N/A with reason` | PASS |
| Worker-return status accepted | `BLOCKED_WITH_REASON` accepted as process halt | PASS |
| Candidate-selection audit created by reviewer | audit path exists and records `PILOT_CANDIDATE_SELECTED` | PASS |
| PIC-T1 release blocked | state-bootstrap/read-model refactor required before PIC-T1 | PASS |

## Claim Boundary

This work order authorizes Claude to produce ASSF-PIC-T0 candidate-selection
audit artifacts only. It does not create or certify any package, activate any
skill, mutate the generated index, modify the resolver, change CVF Web runtime,
expose CLI/MCP behavior, update public artifacts, push to any remote, or
perform session sync.
