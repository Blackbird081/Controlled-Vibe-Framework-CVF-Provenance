# CVF Agent Work Order: ASSF-T6 CVF Web Projection And Existing Example Migration

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-25

docType: work_order

Batch ID: ASSF-T6

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `15f1ea2a`

executionBaseHead: capture with `git rev-parse --short HEAD` before edits

closureBaseHead: N/A with reason: pending worker execution and Codex review

## Dispatch Prompt Envelope

Role: Claude worker for ASSF-T6 CVF Web Projection And Existing Example
Migration.

Canonical packet: this work order plus
`docs/baselines/CVF_GC018_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_2026-06-25.md`.

Commit mode: `WORKER_MAY_COMMIT` for material T6 artifacts only.

dispatchBaseHead: `15f1ea2a`.

executionBaseHead: worker captures with `git rev-parse --short HEAD` before
first material edit.

Current-time notes: dispatch date is 2026-06-25.

Required first actions: read this work order, the GC-018 baseline, startup
front doors, Guard Orientation, and Required First Reads; capture `git status
--short` and `git rev-parse --short HEAD`; run pre-implementation gate before
material edits.

Do-not-misread notes: T6 is documentation and audit only. Do not implement a
CVF Web route, component, API, runtime loader, generator, checker, resolver
change, package instance, `SKILL.md`, `skill.source.json`, generated-index
mutation, external CLI/MCP adapter, provider call, live proof, public-sync, or
session-sync edit. Current CVF Web examples are presentation or candidate
inputs until package certification proves otherwise.

Return contract: after material artifacts are complete, gates pass, and any
material commit is made, return `COMPLETE_PENDING_REVIEW` to Codex with commit
SHA, changed files, gate evidence, and explicit remaining review boundary. Do
not edit active session state, the active handoff, or `CVF_SESSION_MEMORY.md`.

## Purpose

Dispatch Claude to execute ASSF-T6. The mission is to define how future
certified CVF agent system-skill packages may be projected into CVF Web while
preserving plain-language forms, and to audit existing Web skill/template
examples for migration disposition.

## Objective

Produce a source-backed Web projection contract plus an existing-example
migration audit that lets reviewers distinguish:

- certified package projection;
- package candidate;
- legacy reference only;
- duplicate or superseded example;
- rejected example with reason.

The worker must keep Web presentation separate from canonical package truth and
must record the external-agent CLI/MCP adapter boundary explicitly.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Create source-verified GC-018 baseline and work order |
| Worker | Claude | Author T6 material artifacts, run gates, and commit material work if gates pass |
| Reviewer/closer | Codex | Review Claude output, repair minor allowed findings if needed, close or return findings |
| Session-sync steward | Codex | Update active session state, handoff, and front door after review |

## Operator Checkpoint

Operator selected ASSF-T6 after ASSF-T5 closure. No additional operator
checkpoint is required before Claude starts, provided Claude stays inside
Allowed scope and returns `BLOCKED_WITH_REASON` for any forbidden-scope need.

## Authority Chain

| Authority | Path |
|---|---|
| Operator instruction | chat request on 2026-06-25: create work order for Claude |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` |
| GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_2026-06-25.md` |
| ASSF roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` |
| ASSF-T1 package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` |
| ASSF-T2 generated index | `docs/reference/agent_system_skills/generated/skill-index.json` |
| ASSF-T2 generated index README | `docs/reference/agent_system_skills/generated/README.md` |
| ASSF-T2 resolver | `governance/compat/run_assf_skill_resolver.py` |
| ASSF-T5 composition contract | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` |
| Dual Agent Surface Accounting Standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` |
| Governed artifact literal-format gotchas checklist | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` |

Authority boundary:

- If this work order conflicts with the GC-018 baseline, the baseline and
  canonical standards control.
- If source verification contradicts a planned field or claim, stop and return
  `BLOCKED_WITH_REASON`.
- Provider-local memory, chat summaries, or Claude-specific files are not CVF
  authority.

## Scope

Allowed scope:

- Create `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md`.
- Create `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md`.
- Create `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_WORKER_RETURN_2026-06-25.md`.
- Create `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_COMPLETION_2026-06-25.md`.
- Update `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` with T6 material artifact rows and closure status after worker evidence exists.
- Update this work order (`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_FOR_WORKER_2026-06-25.md`) and GC-018 baseline (`docs/baselines/CVF_GC018_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_2026-06-25.md`) from `DISPATCH_READY` to a worker-return or closure-pending status if material evidence supports it.
- Run read-only enumeration and governance gates.
- Commit material T6 artifacts after gates pass.

Forbidden scope:

- Runtime CVF Web route, component, action, API, service, loader, test, or UI
  implementation.
- Any existing `governance/compat/` checker or resolver edit.
- Generated-index edits under `docs/reference/agent_system_skills/generated/`.
- Package instance creation, including `SKILL.md`, `skill.source.json`, and
  registry entry creation.
- External CLI/MCP adapter implementation or external-agent runtime behavior.
- Provider call, live proof, secret use, public-sync, push, or publication.
- Active session state, active handoff, session front door, generated active
  session aggregate, or agent workspace state edits.
- Claiming any Web example is certified unless existing governed package
  certification evidence is cited.

Risk ceiling: R1 documentation and audit only.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:
- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0006: Source Verification symbol cell contains a value/type
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class

Remediation applied:
- ADIF-0001: The worker must record exact search roots and avoid claiming full Web or legacy coverage beyond executed commands.
- ADIF-0002: Source Verification uses CVF-governed files and repository source files only.
- ADIF-0006: Verified path or symbol cells contain bare symbols or paths, not assignments or type annotations.
- ADIF-0007: Keyword-heavy exclusion prose is kept in scope sections and not used as evidence for unrelated registries.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake class | roadmap-derived ASSF tranche selected by operator |
| Routing role | Claude worker with Codex reviewer and session-sync steward |
| Intake authority | ASSF roadmap, T6 GC-018 baseline, and this work order |
| Runtime/source modification | Not authorized |
| External evidence intake | Not authorized by this work order |
| Disposition | route to documentation and audit worker execution |

## Legacy Absorption Coverage Index Disposition

| Coverage index | Disposition | Evidence |
|---|---|---|
| ASSF-T0.1 legacy skill corpus rescan | NOT_APPLICABLE_WITH_REASON | T6 audits existing CVF Web skill/template examples; it does not reopen the legacy corpus scan or absorb new legacy material |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | operator request to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this ASSF-T6 work order and matching GC-018 baseline |
| Disposition | Claude worker executes local documentation and audit only; no external material is absorbed |
| Claim boundary | no external-agent packet, adapter behavior, public claim, or provider proof is accepted as source authority |

## Required First Reads

Before editing material artifacts, read:

1. `CVF_SESSION_MEMORY.md` - startup front door and current mode.
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json` - active handoff pointer and current mode.
3. `AGENT_HANDOFF_V22_2026-06-22.md` - current handoff and next allowed move.
4. `docs/reference/guard_orientation/README.md` - task-class guard orientation.
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` - literal-format traps.
6. `docs/baselines/CVF_GC018_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_2026-06-25.md` - lane baseline.
7. `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` - T6 roadmap source.
8. `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` - canonical package fields and adapter projection rule.
9. `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` - composition and authority boundary.
10. `docs/reference/agent_system_skills/generated/README.md` - generated index boundary.
11. `docs/reference/agent_system_skills/generated/skill-index.json` - metadata-only index claim boundary.
12. `governance/compat/run_assf_skill_resolver.py` - read-only resolver boundary.
13. `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` - mandatory dual-agent matrix.
14. `docs/concepts/skill-system.md` - current product skill concept surface.
15. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-template-map.ts` - Web template-to-skill mapping behavior.
16. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json` - mapping data source.
17. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` - Web skill type surface if relevant to audit.
18. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/index.ts` - Web template aggregation surface if relevant to audit.

## Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 15f1ea2a --head HEAD
```

Expected results:

- `git status --short` has no unrelated dirty files before worker edits.
- Pre-implementation gate passes or fails only on issues the worker can repair
  inside Allowed scope.

If a pre-flight check fails outside Allowed scope, stop and return
`BLOCKED_WITH_REASON` with command output.

## Source-Fidelity Pass

Before writing contract claims, verify every named runtime/source field,
function, type, schema key, template ID, file path, and status against current
repository source. Do not promote provider-local memory into authority.

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF roadmap authorizes T6 CVF Web Projection And Existing Example Migration | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T6 section | `ASSF-T6` | ASSF roadmap | EXISTS | ACCEPT |
| Roadmap states CVF Web projects packages and does not own canonical truth | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Design Principles | `CVF Web projects packages` | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| T1 defines package identity field | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `skillId` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 defines package certification lifecycle field | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `certificationState` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 defines external disposition field | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `externalCliMcpDisposition` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 separates adapter projection from canonical package authority | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Internal-Agent And External-Agent CLI/MCP Disposition Fields | `adapterContract` | ASSF-T1 package schema | LITERAL_INVARIANT | ACCEPT |
| T2 generated index is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | claimBoundary | `claimBoundary` | ASSF-T2 generated index | LITERAL_INVARIANT | ACCEPT |
| T2 resolver exposes read-only skill metadata resolution | `governance/compat/run_assf_skill_resolver.py` | `resolve_skill_packet` | `resolve_skill_packet` | ASSF-T2 resolver | EXISTS | ACCEPT |
| T5 composition contract preserves authority ceiling | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | Authority And Risk Boundary | `authorityCeiling` | ASSF-T5 composition contract | LITERAL_INVARIANT | ACCEPT |
| Web mapping data source exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json` | `templateToSkillMap` | `templateToSkillMap` | CVF Web skill-template mapping | EXISTS | ACCEPT |
| Web map separates template input and skill knowledge sides | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-template-map.ts` | file header comment | `templateToSkillMap` | CVF Web skill-template mapping | LITERAL_INVARIANT | ACCEPT |
| Web map exposes lookup function | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-template-map.ts` | `getSkillForTemplate` | `getSkillForTemplate` | CVF Web skill-template mapping | EXISTS | ACCEPT |
| Concept page defines current skills as form-based templates | `docs/concepts/skill-system.md` | What is a Skill? | `.skill.md` | current product skill concept | EXISTS | ACCEPT |
| Dual Agent standard requires external row and adapter boundary | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Mandatory Dual Agent Surface Matrix | `EXTERNAL_AGENT_CLI_MCP` | Dual Agent Surface Accounting Standard | VALUE_SET | ACCEPT |

### Current Runtime Freshness Verification

Worker must record fresh command-backed evidence in the migration audit:

```powershell
rg --files EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src | rg "(skill|template|spec-first|recommender|templates|types)"
rg -n "templateToSkillMap|categoryToDomainMap|getSkillForTemplate|SkillRef" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-template-map.ts EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json
rg -n "skill|Skill|template|Template|domain|Domain" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/index.ts docs/concepts/skill-system.md
```

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Project certified packages into CVF Web while preserving forms | Objective; Required Deliverables | `CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | reviewer checks projection boundary section | PASS |
| Classify each existing example | Required Deliverables; Acceptance Criteria | migration audit classification ledger | worker records enumeration commands and classifications | PASS |
| CVF Web does not own canonical package truth | Scope; Fail Conditions | projection contract claim boundary | source verification against roadmap and T1 | PASS |
| Dual Agent Surface Matrix mandatory | Dual Agent Surface Matrix | contract, audit, worker return, completion review | reviewer checks both consumer rows and adapter boundary | PASS |
| No runtime, adapter, generated-index, or package activation | Forbidden scope; Fail Conditions | changed-file manifest | `git diff --name-status` and gate results | PASS |

## Worker Autonomy / No-Question Rule

Claude proceeds without operator confirmation for non-destructive actions inside
Allowed scope, including format remediation and rerunning failed gates after an
allowed-scope fix.

Escalate only if remediation would require runtime code, generated-index edit,
session/front-door/handoff edit, external adapter work, public-sync, live
provider proof, secret use, destructive action, risk increase, or a claim
boundary change.

## System Loop Interlock Routing

Upstream loop: ASSF-T1 through ASSF-T5 package architecture and composition
contracts.

Downstream loop: future ASSF-T7 certification, UAT, drift, and lifecycle
planning.

Routing rule: every deferred, rejected, duplicate, or candidate Web example in
the migration audit must name a next action and must not mutate package state.

Claim boundary: the audit is an intake and migration-classification artifact,
not an autonomous package promotion or activation mechanism.

## Planned Worker Fulfillment Manifest

## Planned Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Yes | T6 projection contract |
| `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | Yes | Existing Web skill/example migration audit |
| `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_WORKER_RETURN_2026-06-25.md` | Yes | Claude worker return |
| `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_COMPLETION_2026-06-25.md` | Yes | Completion packet pending Codex review |
| `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Yes | T6 closure status and artifact rows |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Codex owns session-sync |
| `CVF_SESSION/state/` | Codex owns generated active session source |
| `CVF_SESSION_MEMORY.md` | Codex owns session front door |
| `AGENT_HANDOFF_V22_2026-06-22.md` | Codex owns active handoff sync |
| `docs/reference/agent_system_skills/generated/skill-index.json` | T6 does not mutate generated index |
| `docs/reference/agent_system_skills/registry/` | T6 does not create package registry entries |
| `governance/compat/` | T6 does not edit checkers, generators, or resolvers |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/` | T6 audits Web source but does not edit runtime/source files |

## Planned Output Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | ABSENT | ABSENT | N/A with reason |
| `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | ABSENT | ABSENT | N/A with reason |
| `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_WORKER_RETURN_2026-06-25.md` | ABSENT | ABSENT | N/A with reason |
| `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_COMPLETION_2026-06-25.md` | ABSENT | ABSENT | N/A with reason |

## Planned Proof Requirements

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| Projection contract status | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | `Status: CANDIDATE` | Yes |
| Projection class vocabulary | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | `CERTIFIED_PACKAGE_PROJECTION` | Yes |
| Migration audit status | `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | `Status: COMPLETE_PENDING_REVIEW` | Yes |
| External disposition | worker-created contract and audit | `EXTERNAL_AGENT_CLI_MCP` | Yes |
| Worker return | `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_WORKER_RETURN_2026-06-25.md` | `COMPLETE_PENDING_REVIEW` | Yes |
| No activation claim | worker-created contract and audit | `no package activation` | Yes |

## Write Ownership

Owned files:

- `docs/baselines/CVF_GC018_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_2026-06-25.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_FOR_WORKER_2026-06-25.md`
- `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md`
- `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md`
- `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_WORKER_RETURN_2026-06-25.md`
- `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_COMPLETION_2026-06-25.md`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`

Write mode:

- Create-only for new T6 contract, audit, worker return, and completion packet.
- Modify-listed for GC-018, work order, and roadmap.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatcher -> Claude worker -> Codex reviewer/closer -> Codex session-sync steward |
| phase | DISPATCH_AUTHORING by Codex; EXECUTION by Claude; CLOSURE by Codex after review; SESSION_SYNC by Codex |
| baseHeadFor(phase) | `dispatchBaseHead=15f1ea2a`; `executionBaseHead` captured by Claude before edits; `closureBaseHead` captured by Codex before closure |
| changedSetScope(phase) | Claude changes only Allowed scope material paths; Codex owns review closure and session surfaces |
| traceScope(phase, actor) | Codex records dispatch trace; Claude records worker trace; Codex records review and session-sync trace |
| commitOwner(phase) | Claude may commit material T6 artifacts; Codex owns final review and session-sync commits |
| crossBatchIsolation | no GFS-PY, EQC, public-sync, runtime, adapter, or unrelated cleanup work is authorized |
| nextMoveSurfaces | Claude must not edit active next-move surfaces; return commit SHA and review boundary to Codex |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation family | ASSF agent system skills reference family |
| Durable root | `docs/reference/agent_system_skills/` |
| New durable file | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` |
| Audit root | `docs/audits/` |
| Review root | `docs/reviews/` |
| Index or front-door update | N/A with reason: no generated index or README update is required by this tranche |
| Storage boundary | contract and audit files are documentation surfaces, not package roots or generated aggregates |
| Future migration boundary | any package root, generated-index, or Web runtime storage change requires a later work order |

## Execution Plan

1. Read Required First Reads and capture `executionBaseHead`.
2. Run pre-implementation gate.
3. Enumerate relevant CVF Web skill/template/type surfaces using commands in
   Current Runtime Freshness Verification.
4. Author the Web projection contract.
5. Author the migration audit with command-backed classification ledger.
6. Author worker return and completion packet with actual changed-file and gate
   evidence.
7. Update roadmap, GC-018, and work order status only as far as evidence
   supports.
8. Run required gates.
9. Commit material T6 work if gates pass.
10. Return `COMPLETE_PENDING_REVIEW` to Codex; do not perform session sync.

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | ASSF roadmap In Scope and Out of Scope | documentation and audit only | PASS |
| Non-goals | ASSF roadmap Failure Patterns To Avoid | runtime, adapter, activation, and bulk migration blocked | PASS |
| Lane split | ASSF-T6 section | executes only Web projection and example migration lane | PASS |
| Dependency/source-verification plan | roadmap Source Verification Block | current work order carries Source Verification Block | PASS |
| Claim boundary | roadmap Claim Boundary and Public Export Disposition | no activation or public claim | PASS |
| Acceptance criteria | ASSF-T6 section and closure gate | concrete contract, audit, return, and completion packets | PASS |
| Verification/evidence | roadmap Machine Closure Package | gate and changed-file evidence required | PASS |
| Dispatch-readiness decision | operator selection of T6 | T5 closed and T6 selected by operator | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T6 projection contract and migration audit | may read projected metadata and classifications; cannot infer activation, certification, or new authority from Web examples | GC-018 Source Verification Block and worker-created contract/audit | no internal runtime projection or loader is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP projection readout or adapter contract | no mutation, activation, certification, package execution, or public claim is authorized | Dual Agent standard, T1 external fields, and T6 audit rows | deferred adapter owner; separate work order required | `DEFERRED_WITH_REASON` |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Agent type | dispatcher and delegated worker |
| Actor | Codex dispatcher, Claude worker, Codex reviewer |
| Provider or surface | Codex local repo dispatch; Claude local repo worker execution |
| Invocation ID | `cvf-assf-t6-web-projection-dispatch-2026-06-25` |
| Session or invocation | dispatchBaseHead `15f1ea2a`; worker records executionBaseHead |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git, governance Python gates |
| Target paths | T6 baseline, work order, projection contract, audit, review packets, roadmap |
| Allowed scope source | operator instruction, ASSF roadmap, GC-018 baseline, this work order |
| Before status evidence | dispatcher: `git status --short --branch` showed clean worktree at `15f1ea2a`; worker must refresh |
| After status evidence | pending worker execution |
| Diff evidence | pending worker execution |
| Expected manifest | T6 baseline, work order, projection contract, migration audit, worker return, completion review, roadmap |
| Actual changed set | pending worker execution |
| Manifest delta | pending worker execution |
| Approval boundary | material T6 documentation and audit only |
| Claim boundary | repo-local trace only; no OS/user identity proof |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: existing CVF Web skill/template surfaces will be
presentation mappings or candidates, not certified ASSF package projections.

Evidence Comparison Requirement: worker return compares actual enumeration and
classification evidence against the prediction.

Contradiction Handling Requirement: any discovered certified package projection
must cite package certification evidence; otherwise classify as candidate,
legacy reference, duplicate, or rejected with reason.

Claim Update Requirement: worker return records whether the claim was
confirmed, narrowed, or invalidated.

## Evidence Requirements

Required evidence:

- command-backed enumeration of relevant CVF Web skill/template surfaces;
- projection contract with canonical-vs-presentation boundary;
- migration audit classification ledger;
- Source Verification Block in worker-created artifacts;
- Dual Agent Surface Matrix in contract, audit, worker return, and completion
  packet;
- changed-file manifest from `git diff --name-status`;
- gate receipts;
- explicit no-runtime/no-adapter/no-activation/no-public-sync claim boundary.

Base-anchor evidence:

- `dispatchBaseHead`: `15f1ea2a`
- `executionBaseHead`: worker captures before edits
- `closureBaseHead`: Codex captures before review closure
- Commit mode: `WORKER_MAY_COMMIT`
- Pending-artifact component gates: worker records actual commands and results
- Committed-range `pre-closure`: Codex reviewer or Claude worker records only
  after material commit exists

## Acceptance Criteria

- [x] Projection contract exists and is marked `Status: CANDIDATE`.
- [x] Projection contract includes canonical truth, display, certification,
  adapter, and external-agent boundaries.
- [x] Migration audit enumerates current relevant Web skill/template surfaces
  and records exact commands.
- [x] Every audited Web example receives one allowed classification token.
- [x] No audited example is called certified without package certification
  evidence.
- [x] Dual Agent Surface Matrix appears with both consumer classes and adapter
  boundary.
- [x] Worker return includes gate evidence, changed files, and claim boundary.
- [x] Completion packet is present for Codex review.
- [x] No forbidden paths are changed.

Fail conditions:

- [x] A Web example is promoted to certified package projection without
  certification evidence. -- ABSENT: no entry promoted to CERTIFIED_PACKAGE_PROJECTION.
- [x] External-agent CLI/MCP disposition is omitted or implicit. -- ABSENT: DEFERRED_WITH_REASON recorded in all artifacts.
- [x] Runtime/source Web code, generated index, resolver, checker, package
  instance, adapter, provider/live, public-sync, or session state is changed. -- ABSENT: changed-file manifest shows documentation paths only.
- [x] Source Verification uses provider-local memory as authority. -- ABSENT: all source facts cite repository files.
- [x] A required gate fails outside Allowed scope. -- ABSENT: pre-implementation 49/49 PASS.

Closure is blocked if any fail condition is present.

## Review Gate

Implementation may proceed only after:

- this work order and its GC-018 baseline exist;
- pre-dispatch gate passed for dispatcher artifacts;
- worker pre-implementation gate passes before material edits.

Closure may proceed only after:

- worker returns `COMPLETE_PENDING_REVIEW`;
- material commit exists if Claude uses `WORKER_MAY_COMMIT`;
- Codex review finds no blocking source-fidelity, authority, external-agent,
  runtime, generated-index, package-activation, or session-sync defect;
- pre-closure gate passes on the material range.

## Closure Checklist

- [x] All acceptance criteria satisfied or marked `N/A with reason`.
- [x] Fail conditions checked and absent or returned `BLOCKED_WITH_REASON`.
- [x] Required artifacts exist.
- [x] Worker changed-file set is inside Allowed scope.
- [x] Gate evidence is current and command-backed.
- [x] Roadmap-to-work-order trace is resolved.
- [x] Dual Agent Surface Matrix remains present in closure artifacts.
- [x] Public Export Disposition is recorded.
- [x] No open checklist residue remains in closed-equivalent artifacts.
- [x] Codex session-sync happens only after review closure.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without continuing if:

- pre-implementation gate fails outside Allowed scope;
- source verification finds a missing required source path or invented field;
- a needed action would touch forbidden paths;
- a real Web implementation becomes necessary to satisfy the task;
- external adapter behavior is required;
- public/provenance boundary becomes unclear;
- provider/live proof or secret use becomes necessary;
- session-sync is required before material work can continue.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T6 Web projection contract, migration audit, worker return, completion packet, and roadmap closure rows |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- worker documentation/audit tranche only |
| receiptEvidence | N/A with reason: no runtime/provider/adapter receipt is authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- worker must provide enumeration commands, gate evidence, and changed-file manifest |
| invocationBoundary | governed local repository documentation and audit execution only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, or Web runtime interception claim |
| claimLanguage | worker may define and audit Web projection boundaries; worker may not implement or activate them |
| forbiddenExpansion | no runtime Web implementation, route, component, API, resolver, generator, checker, package instance, SKILL.md, skill.source.json, generated-index mutation, CLI/MCP adapter, provider/live proof, public-sync, push, active handoff, front door, or session state edit |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch and architecture work. Public-safe export
requires later redaction and public-sync authorization.

## Acceptance Receipt Assertion Matrix

| Item | Required value | Observed value | Status |
|---|---|---|---|
| Work order status | `Status: CLOSED_PASS_BOUNDED` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Pre-implementation gate | 49/49 PASS before material edits | 49/49 PASS at HEAD `ffa421f2` | PASS |
| No forbidden-scope change | zero forbidden-scope files in changed set | changed-file manifest shows documentation paths only | PASS |
| Worker return present | `COMPLETE_PENDING_REVIEW` at named path | present -- `Status: COMPLETE_PENDING_REVIEW` | PASS |
| Completion review present | `CLOSED_PASS_BOUNDED` at named path | present -- `Status: CLOSED_PASS_BOUNDED` | PASS |
| External-agent disposition recorded | `DEFERRED_WITH_REASON` for all audited entries | confirmed in migration audit and projection contract | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T6_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: T6 dispatch is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: T6 dispatch is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported; external-agent boundary is contract-only | N/A with reason |
| System loop interlock | this work order | T1->T2->T3->T4->T5->T6 closed in order; no automatic package activation | PASS |
| Session continuity | N/A with reason | Codex session-sync will occur after review closure; worker does not edit session surfaces | N/A with reason |

## Claim Boundary

This work order authorizes Claude to produce T6 documentation and audit
artifacts only. It does not certify any package, activate any skill, change CVF
Web runtime, expose CLI/MCP behavior, update public artifacts, or perform
session sync.
