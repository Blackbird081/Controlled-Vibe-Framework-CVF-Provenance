# CVF Agent Work Order: ASSF-T7 Certification UAT Drift Deprecation Retirement Guard

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-25

docType: work_order

Batch ID: ASSF-T7

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `eb269c4c`

executionBaseHead: capture with `git rev-parse --short HEAD` before edits

closureBaseHead: `d78630be`

## Dispatch Prompt Envelope

Role: Claude worker for ASSF-T7 Certification UAT Drift Deprecation Retirement
Guard.

Canonical packet: this work order plus
`docs/baselines/CVF_GC018_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_2026-06-25.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

dispatchBaseHead: `eb269c4c`.

executionBaseHead: worker captures with `git rev-parse --short HEAD` before
first material edit.

Current-time notes: dispatch date is 2026-06-25.

Required first actions: read this work order, the GC-018 baseline, startup
front doors, Guard Orientation, Governed Artifact Literal Format Gotchas,
Required First Reads, and ADIF disclosures; capture `git status --short` and
`git rev-parse --short HEAD`; run pre-implementation gate before material
edits.

Do-not-misread notes: T7 is documentation-only guard foundation. Do not
implement a checker, resolver change, generated-index mutation, package
instance, `SKILL.md`, `skill.source.json`, Web runtime/source change, CLI/MCP
adapter, provider call, live proof, public-sync, push, commit, or session-sync
edit.

Return contract: satisfied. Claude returned `COMPLETE_PENDING_REVIEW` to Codex
with changed files, gate evidence, exact remaining review boundary, and no
material commit identifier.

## Purpose

Dispatch Claude to execute ASSF-T7 by authoring the certification lifecycle
guard contract that ASSF needs before package promotion, Web certified
projection, external-agent adapter claims, or lifecycle retirement can be
trusted.

## Objective

Create a source-backed guard contract that defines:

- certification and UAT evidence boundaries;
- package/index/resolver consistency drift classes;
- dangling source and invalid selector drift classes;
- duplicate-ID, stale successor, deprecation, retirement, and lifecycle
  violation rules;
- dishonest enforcement or adapter-claim detection;
- machine-check candidates without implementing a checker in this tranche.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Create source-verified GC-018 baseline and work order |
| Worker | Claude | Author T7 guard contract and worker return without committing |
| Reviewer/closer | Codex | Review Claude output, repair minor allowed findings if needed, commit material closure |
| Session-sync steward | Codex | Update active session state, handoff, and front door after review |

## Operator Checkpoint

Operator selected ASSF-T7 after ASSF-T6 closure and ADIF authoring hardening.
No additional operator checkpoint is required before Claude starts, provided
Claude stays inside Allowed scope and returns `BLOCKED_WITH_REASON` for any
forbidden-scope need.

## Authority Chain

| Authority | Path |
|---|---|
| Operator instruction | chat request on 2026-06-25: create work order ASSF-T7 for Claude |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` |
| GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_2026-06-25.md` |
| ASSF roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` |
| ASSF-T1 package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` |
| ASSF-T2 generated index | `docs/reference/agent_system_skills/generated/skill-index.json` |
| ASSF-T2 generated index README | `docs/reference/agent_system_skills/generated/README.md` |
| ASSF-T2 resolver | `governance/compat/run_assf_skill_resolver.py` |
| ASSF-T5 composition contract | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` |
| ASSF-T6 Web projection contract | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` |
| ASSF-T6 migration audit | `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` |
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
| rolePattern | Codex dispatches; Claude authors guard contract and worker return; Codex reviews, closes, commits, and session-syncs |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=eb269c4c`; `executionBaseHead` confirmed by Claude; `closureBaseHead` set by Codex before closure commit |
| changedSetScope(phase) | Claude changes only the two allowed worker deliverables; Codex owns completion review, status conversion, roadmap closure, commit, and session-sync if accepted |
| traceScope(phase, actor) | one Claude worker-return trace covers guard contract and worker return; one Codex trace covers review/closure if accepted |
| commitOwner(phase) | Claude commits nothing (`WORKER_MUST_NOT_COMMIT`); Codex owns any material/closure/session-sync commit |
| crossBatchIsolation | no changes outside ASSF-T7 allowed scope |
| Before status evidence | clean worktree at dispatch base `eb269c4c` before ASSF-T7 packet authoring |
| nextMoveSurfaces | Claude must not edit active session state, active handoff, front door, generated active-session aggregate, roadmap closure rows, or session-sync surfaces |
| Closer designation | Codex is the designated reviewer and closer |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_COMPLETION_2026-06-25.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_COMPLETION_2026-06-25.md`
- `docs/baselines/CVF_GC018_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_2026-06-25.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_FOR_CLAUDE_2026-06-25.md`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
- session front-door/state/handoff paths only if Codex changes current mode or
  next allowed move after accepting the worker return.

Claude must not create the completion review and must not mark the work closed.

## Scope

Allowed scope:

- Create `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md`.
- Create `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_WORKER_RETURN_2026-06-25.md`.
- Run read-only source verification, enumeration commands, and governance
  gates.
- Update no other file unless a gate failure inside Allowed scope requires a
  narrowly scoped repair in one of the two allowed worker deliverables.
- Codex reviewer/closer may update `docs/baselines/CVF_GC018_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_2026-06-25.md`.
- Codex reviewer/closer may update `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_FOR_CLAUDE_2026-06-25.md`.
- Codex reviewer/closer may update `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`.
- Codex reviewer/closer may create `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_COMPLETION_2026-06-25.md`.

Forbidden scope:

- Commit, push, public-sync, or publication.
- Runtime CVF Web route, component, action, API, service, loader, test, UI, or
  data implementation.
- Any existing `governance/compat/` checker or resolver edit.
- Generated-index edits under `docs/reference/agent_system_skills/generated/`.
- Package instance creation, including `SKILL.md`, `skill.source.json`, and
  registry entry creation.
- External CLI/MCP adapter implementation or external-agent runtime behavior.
- Provider call, live proof, secret use, or public repository operation.
- Active session state, active handoff, session front door, generated active
  session aggregate, or agent workspace state edits.
- Roadmap closure update, baseline closure conversion, work-order closure
  conversion, or completion review creation.
- Claiming any Web example is certified unless existing governed package
  certification evidence is cited.

Risk ceiling: R1 documentation-only guard contract.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0006: Source Verification symbol cell contains a value/type
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class

Remediation applied:

- ADIF-0001: Worker must avoid exhaustive coverage claims unless command output
  proves the exact search root and count.
- ADIF-0002: Worker must cite CVF-governed docs or repository source files, not
  provider-local memory, for every source fact.
- ADIF-0006: Worker Source Verification symbol cells must contain bare symbols,
  paths, sections, or tokens only.
- ADIF-0007: Worker must keep keyword-heavy scope exclusions out of evidence
  rows unless they are direct source facts.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake source | operator-originated ASSF-T7 continuation request |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| scope classification | R1 documentation-only guard foundation |
| risk sensitivity | R1; no runtime, generated index, resolver, adapter, provider/live, public-sync, or commit authority |
| selected role route | Codex dispatcher; Claude worker; Codex reviewer/closer; Codex session-sync steward |
| Intake authority | ASSF roadmap, T7 GC-018 baseline, and this work order |
| Runtime/source modification | not authorized |
| External evidence intake | not authorized by this work order |
| Disposition | route to documentation-only guard contract worker execution |
| escalation condition | scope expansion, forbidden paths, provider/live, public-sync, secrets/quota, dependency install, destructive actions, commit request, or claim-boundary change |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | operator request to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this ASSF-T7 work order and matching GC-018 baseline |
| Disposition | Claude worker executes local documentation-only guard contract work; no external material is absorbed |
| Claim boundary | no external-agent packet, adapter behavior, public claim, or provider proof is accepted as source authority |

## Required First Reads

Before editing material artifacts, read:

1. `CVF_SESSION_MEMORY.md` - startup front door and current mode.
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json` - active handoff pointer and current mode.
3. `AGENT_HANDOFF_V22_2026-06-22.md` - current handoff and next allowed move.
4. `docs/reference/guard_orientation/README.md` - task-class guard orientation.
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` - literal-format traps.
6. `docs/baselines/CVF_GC018_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_2026-06-25.md` - lane baseline.
7. `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` - T7 roadmap source.
8. `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` - canonical package lifecycle and external-agent fields.
9. `docs/reference/agent_system_skills/generated/README.md` - generated index boundary.
10. `docs/reference/agent_system_skills/generated/skill-index.json` - metadata-only index claim boundary and current package states.
11. `governance/compat/run_assf_skill_resolver.py` - read-only resolver boundary and excluded status behavior.
12. `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` - no-automatic-promotion and package graph rules.
13. `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` - Web projection classification boundary.
14. `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` - Web migration findings escalated to T7.
15. `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` - mandatory dual-agent matrix.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Worker deliverable | Evidence required |
|---|---|---|---|
| T7 checks package/index consistency | define consistency drift classes for package contract fields, generated index metadata, and resolver behavior | T7 guard contract | Source Verification Block and drift class table |
| T7 checks dangling sources and invalid selectors | define missing source artifact and invalid selector drift classes | T7 guard contract | source-backed taxonomy |
| T7 checks dishonest enforcement or adapter claims | bind external disposition claims to adapter contract and evidence | T7 guard contract | Adapter Claim Honesty Rules and Dual Agent Surface Matrix |
| T7 checks duplicate IDs, stale successors, missing UAT, and lifecycle violations | define lifecycle violation taxonomy and hold/reject dispositions | T7 guard contract | lifecycle violation table |
| T7 integrates machine gates only after stable repeated use | list machine-check candidates without implementing them | T7 guard contract | Machine-Check Candidate Matrix |
| T7 cites T1, T2, T5, and T6 foundations | read and cite Required First Reads 8 through 14 | T7 guard contract and worker return | Source Verification Block |

## Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base eb269c4c --head HEAD
```

Expected results:

- `git status --short` has no unrelated dirty files before worker edits.
- Pre-implementation gate passes or fails only on issues the worker can repair
  inside Allowed scope.

If a pre-flight check fails outside Allowed scope, stop and return
`BLOCKED_WITH_REASON` with command output.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Claude | create only |
| `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_WORKER_RETURN_2026-06-25.md` | Claude | create only |
| `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_COMPLETION_2026-06-25.md` | Codex | reviewer-owned; Claude must not create |
| `docs/baselines/CVF_GC018_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_2026-06-25.md` | Codex | closure conversion only |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_FOR_CLAUDE_2026-06-25.md` | Codex | closure conversion only |
| `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Codex | closure rows only after review |
| Any other path | Not Claude | forbidden unless Codex issues a revised work order |

## Worker Autonomy / No-Question Rule

Claude must repair and rerun gate failures inside Allowed scope. Claude must
stop and return `BLOCKED_WITH_REASON` only for scope expansion, forbidden
paths, live/provider proof, public-sync, secret/quota consumption, dependency
install, destructive actions, commit request, or claim-boundary changes.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | new ASSF reference contract plus worker-return review artifact |
| Storage decision | place durable guard contract under `docs/reference/agent_system_skills/`; place worker return under `docs/reviews/` |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | contract is documentation-only candidate guidance; no generated aggregate, runtime store, checker, resolver, package registry, or adapter state is created |

## Current Runtime Freshness Verification

| Runtime or source claim | Verification command or source | Dispatch result | Worker requirement |
|---|---|---|---|
| T7 worker contract path absent before dispatch | `Test-Path docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | `False` | create path |
| T7 worker return path absent before dispatch | `Test-Path docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_WORKER_RETURN_2026-06-25.md` | `False` | create path |
| T7 completion review path absent before dispatch | `Test-Path docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_COMPLETION_2026-06-25.md` | `False` | do not create; reviewer-owned |
| Generated index mutation is not authorized | source boundary in this work order | no generated-index file in allowed worker paths | preserve |
| Resolver mutation is not authorized | source boundary in this work order | no resolver file in allowed worker paths | preserve |

## Source-Fidelity Pass

Before writing contract claims, verify every named runtime/source field,
function, type, schema key, status, route, and existing path against current
repository source. Do not promote provider-local memory into authority.

## Negative Search And Collision Discipline

Search roots for dispatch-time negative checks: repository root, with concrete
source coverage across governed docs, source files, tests, JSON aggregates, and
external-evidence references only when the work order names them. Exact search
commands or structured queries must be copied into the worker return when the
worker adds a new field, enum, checker name, or path claim.

| Check | Exact search command or structured query | Same-token collision result | Disposition |
|---|---|---|---|
| Existing T7 guard contract path | `Test-Path docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | path occurrence is new in this dispatch packet; no prior governed artifact owns that exact path | absent at dispatch; worker creates it |
| Existing T7 worker return path | `Test-Path docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_WORKER_RETURN_2026-06-25.md` | path occurrence is new in this dispatch packet; no prior governed artifact owns that exact path | absent at dispatch; worker creates it |
| Existing T7 completion review path | `Test-Path docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_COMPLETION_2026-06-25.md` | path occurrence is new in this dispatch packet; Codex reviewer owns it | absent at dispatch; Claude does not create it |
| Proposed new certification-state vocabulary | `rg -n "certificationState|uatState|approvalState|candidateState" docs/reference/agent_system_skills docs/roadmaps governance/compat` | same-token occurrences exist in T1, T2, T6, and this packet; only source-declared values are binding | new enum values are doc-only proposals unless current source declares them |
| Proposed checker names | `rg -n "ASSF.*certification|lifecycle.*guard|certification.*guard" governance/compat docs/reference/agent_system_skills` | same-token occurrences in this packet are non-authoritative for implementation | future machine-check candidate only unless current source implements it |
| `SHA` commit-return wording | `rg -n "SHA|commit" docs/work_orders docs/reference governance/compat` | same-token collision occurrences exist elsewhere as commit metadata vocabulary | non-authoritative as a source-fact claim; worker omits commit identifier because commit mode controls |
| `WORKER_MUST_NOT_COMMIT` control token | `rg -n "WORKER_MUST_NOT_COMMIT" docs/reference docs/work_orders governance/compat` | same-token collision occurrences exist in AHB and dispatch-quality surfaces and are authoritative for commit-suppressed work orders | binding commit-mode token for this work order |

If a source fact search fails to produce a governed authority row, use `REJECT`
with corrected fact when known or stop with a blocking source-fidelity note.
Do not close implementation with guessed field names, placeholder source paths,
or provider-memory-only authority.

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF roadmap authorizes T7 Certification UAT Drift Deprecation Retirement Guard | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T7 section | `ASSF-T7` | ASSF roadmap | EXISTS | ACCEPT |
| Roadmap requires T7 to check package/index consistency and lifecycle violations | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T7 section | `missing UAT` | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| Roadmap requires future T7 packet to cite T1, T2, T5, and T6 foundations | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Machine Closure Package notes | `ASSF-T7 packet` | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| T1 defines certification lifecycle field | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `certificationState` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 defines UAT lifecycle field | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `uatState` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 defines lifecycle status vocabulary | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Lifecycle State Vocabulary | `ACTIVE` | ASSF-T1 package schema | VALUE_SET | ACCEPT |
| T1 defines external CLI/MCP disposition field | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Internal-Agent And External-Agent CLI/MCP Disposition Fields | `externalCliMcpDisposition` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 defines adapter evidence field | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Internal-Agent And External-Agent CLI/MCP Disposition Fields | `adapterEvidence` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T2 generated index is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | claimBoundary | `claimBoundary` | ASSF-T2 generated index | LITERAL_INVARIANT | ACCEPT |
| T2 generated index records current candidate package states | `docs/reference/agent_system_skills/generated/skill-index.json` | skill entries | `candidateState` | ASSF-T2 generated index | VALUE_SET | ACCEPT |
| T2 resolver excludes retired and rejected skills by default | `governance/compat/run_assf_skill_resolver.py` | `_EXCLUDED_STATUSES` | `_EXCLUDED_STATUSES` | ASSF-T2 resolver | VALUE_SET | ACCEPT |
| T2 resolver exposes skill packet resolution | `governance/compat/run_assf_skill_resolver.py` | `resolve_skill_packet` | `resolve_skill_packet` | ASSF-T2 resolver | EXISTS | ACCEPT |
| T5 composition contract forbids automatic promotion | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | No-Automatic-Promotion Invariant | `No-Automatic-Promotion Invariant` | ASSF-T5 composition contract | LITERAL_INVARIANT | ACCEPT |
| T5 composition contract restricts package graph lifecycle states | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | Package Graph Boundary | `Package Graph Boundary` | ASSF-T5 composition contract | LITERAL_INVARIANT | ACCEPT |
| T6 Web projection contract defines candidate and certified projection tokens | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Projection Classification Vocabulary | `PACKAGE_CANDIDATE` | ASSF-T6 Web projection contract | VALUE_SET | ACCEPT |
| T6 migration audit found zero certified Web projections | `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | Classification Summary | `CERTIFIED_PACKAGE_PROJECTION` | ASSF-T6 migration audit | VALUE_SET | ACCEPT |
| T6 migration audit escalated Web certification schema gap to T7 | `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | Next Action | `certificationState` | ASSF-T6 migration audit | LITERAL_INVARIANT | ACCEPT |
| Dual Agent standard requires external-agent disposition and adapter boundary | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Mandatory Dual Agent Surface Matrix | `EXTERNAL_AGENT_CLI_MCP` | Dual Agent Surface Accounting Standard | VALUE_SET | ACCEPT |

## Required Contract Shape

Create `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` with these sections:

| Required section | Minimum content |
|---|---|
| Status and claim boundary | mark contract `Status: CANDIDATE`; state documentation-only boundary |
| Purpose | explain why certification, UAT, drift, deprecation, retirement, and adapter honesty are controlled together |
| Source Authority | cite T1, T2, T5, T6, and this work order |
| Certification and UAT State Model | define allowed documentation-level state vocabulary and explicitly mark new enum proposals as doc-only unless already source-backed |
| Lifecycle Violation Taxonomy | include missing UAT, invalid selector, dangling source, duplicate ID, stale successor, illegal retirement, and graph-state violation |
| Drift Detection Classes | separate package contract drift, generated index drift, resolver selection drift, Web projection drift, and adapter claim drift |
| Deprecation Successor Retirement Rules | define hold/reject dispositions for stale successors and retirement without evidence |
| Adapter Claim Honesty Rules | bind `externalCliMcpDisposition`, `adapterContract`, `adapterEvidence`, and `externalMutationBoundary` to evidence before any `IMPLEMENTED` claim |
| Web Projection Certification Bridge | preserve T6 rule that current Web entries remain candidates until package certification evidence exists |
| Dual Agent Surface Matrix | include `INTERNAL_AGENT` and `EXTERNAL_AGENT_CLI_MCP` rows with interface, authority/risk boundary, evidence, and adapter boundary |
| Machine-Check Candidate Matrix | list future checker candidates without implementing them |
| Source Verification Block | cite source facts used by the contract |
| Public Export Disposition | use `DEFERRED_PRIVATE_ONLY` unless separate export authority exists |

## Worker Return Requirements

Create `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_WORKER_RETURN_2026-06-25.md` with:

| Required section | Minimum content |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Execution base | `git rev-parse --short HEAD` result captured before edits |
| Changed files | exact `git diff --name-status` output or equivalent command-backed list |
| Gate receipts | pre-implementation and pre-closure/pre-review gate outputs, or blocked diagnostic |
| Source verification | sources used for every lifecycle, index, resolver, Web, and adapter claim |
| ADIF reflection | whether any repeated non-obvious defect pattern was observed and whether a new ADIF entry is needed |
| Claim boundary | no commit, no closure, no runtime, no adapter, no session-sync |

## Worker Return Packet Shape Contract

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
3. Source-verify every lifecycle, generated index, resolver, Web projection,
   and adapter claim before writing the contract.
4. Create the T7 guard contract inside the required contract shape.
5. Create the worker return with command-backed evidence.
6. Run the required gates and repair allowed-scope failures.
7. Return `COMPLETE_PENDING_REVIEW` with no commit.

## Evidence Requirements

| Evidence item | Required proof |
|---|---|
| Changed files | `git diff --name-status` output |
| Worktree state | `git status --short` output |
| Source facts | Source Verification Block rows with ACCEPT, REJECT, or BLOCKED_SOURCE_NOT_FOUND |
| Gate receipts | pre-implementation gate plus pre-closure or worker-return fast gate where applicable |
| No commit | worker return states `WORKER_MUST_NOT_COMMIT` and no commit SHA |
| No runtime/adapter/session-sync | claim boundary and changed-file evidence |

## Review Gate

Codex will review the worker return before commit. Review must verify changed
files, source-fidelity rows, Dual Agent Surface Matrix, machine-check candidate
boundary, no generated index drift, no resolver mutation, and no forbidden
session or public-sync edits.

## Closure Checklist

| Closure item | Required disposition before Codex closure |
|---|---|
| Worker deliverables exist | required |
| Worker return status is `COMPLETE_PENDING_REVIEW` or explains `BLOCKED_WITH_REASON` | required |
| Changed set matches Write Ownership | required |
| Gates pass or blocked diagnostic is accepted | required |
| Completion review created by Codex only | required |
| Roadmap and session sync updated only after acceptance | required if accepted |

## Return-To-Orchestrator Conditions

| Condition | Worker return |
|---|---|
| Allowed-scope work complete and gates pass | `COMPLETE_PENDING_REVIEW` |
| Source fact missing or contradicted | `BLOCKED_WITH_REASON` |
| Required change touches forbidden path | `BLOCKED_WITH_REASON` |
| Gate fails outside Allowed scope | `BLOCKED_WITH_REASON` |
| Operator authorization needed for scope expansion | `BLOCKED_WITH_REASON` |

## Acceptance Criteria

| Criterion | Required disposition |
|---|---|
| Contract covers certification, UAT, drift, deprecation, successor, retirement, duplicate-ID, and adapter-claim honesty | REQUIRED |
| Contract includes Dual Agent Surface Matrix with external-agent CLI/MCP disposition | REQUIRED |
| Contract keeps all new checker ideas as machine-check candidates, not implemented checks | REQUIRED |
| Contract does not claim current Web examples are certified | REQUIRED |
| Worker return includes exact changed files and gate receipts | REQUIRED |
| Worker does not commit | REQUIRED |
| Worker does not edit forbidden session, runtime, generated index, resolver, adapter, public-sync, or roadmap closure surfaces | REQUIRED |

## Agent Operation Trace Block

| Field | Value |
|---|---|
| Session or invocation | ASSF-T7 dispatch, 2026-06-25 |
| Invocation ID | ASSF-T7-dispatch-codex-2026-06-25 |
| Actor | Codex dispatcher |
| Agent type | Codex |
| Role | dispatcher |
| Provider or surface | local filesystem and governance gates |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `apply_patch`; `python governance/compat/run_agent_autorun_workflow_gate.py`; `git` |
| Base HEAD | `eb269c4c` |
| Target paths | this work order; matching GC-018 baseline |
| Allowed scope source | operator request to create ASSF-T7 work order for Claude |
| Before status evidence | clean worktree at `eb269c4c` |
| After status evidence | dispatch packet authored, pending pre-dispatch gate |
| Approval boundary | documentation-only guard contract dispatch |
| Diff evidence | to be generated by dispatch commit |
| Expected manifest | this work order; matching GC-018 baseline |
| Actual changed set | pending dispatch commit |
| Manifest delta | two new dispatch artifacts |
| Claim boundary | dispatch packet authoring only; no worker completion, runtime, adapter, public-sync, or session-sync claim |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T7 certification lifecycle guard contract worker execution |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- work order only |
| receiptEvidence | N/A with reason: no runtime execution, provider call, or adapter receipt exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block and artifact manifest |
| invocationBoundary | governed local documentation worker execution only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes Claude to create two uncommitted worker deliverables inside Allowed scope |
| forbiddenExpansion | no checker implementation, generated-index mutation, resolver mutation, package activation, Web runtime change, CLI/MCP adapter, provider call, live proof, public-sync, push, commit, or session-sync edit |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this dispatch references private provenance architecture and repository
source surfaces. Public-safe export requires a separate redaction and
public-sync authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T7_CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker material artifacts | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md`; `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_WORKER_RETURN_2026-06-25.md` | created by Claude worker and accepted by Codex review | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T7_CERTIFICATION_UAT_DRIFT_DEPRECATION_RETIREMENT_GUARD_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | T7 closure is not authorized to update GC-051 corpus registry or generated ASSF index surfaces | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | T7 closure is not authorized to update GC-051 corpus registry Markdown surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported; external-agent boundary is contract-only | N/A with reason |
| System loop interlock | this work order | T7 closes after T1/T2/T5/T6 prerequisites and releases no package activation | PASS |
| Session continuity | N/A with reason | separate session-sync lane follows material closure if next move changes | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Work order status | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| Worker commit mode | `WORKER_MUST_NOT_COMMIT` | worker left deliverables uncommitted for Codex review | PASS |
| Worker return | `COMPLETE_PENDING_REVIEW` | accepted by Codex completion review | PASS |
| Runtime/provider/live claim | none | none | PASS |
| External CLI/MCP adapter | deferred | `DEFERRED_WITH_REASON` | PASS |

## Claim Boundary

This work order is closed bounded after Codex review. It authorized Claude to
create the bounded T7 guard contract and worker return only. Codex owns the
material closure commit and separate session sync after acceptance.
