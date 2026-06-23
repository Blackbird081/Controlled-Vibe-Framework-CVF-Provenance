# CVF Agent Work Order ASSF-T0.1 Legacy Skill Corpus Rescan For Worker

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-23

docType: work_order

Batch ID: ASSF-T0.1

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: ab7ca99b

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: PENDING_WORKER_RETURN

## Dispatch Prompt Envelope

Role: ASSF-T0.1 no-commit worker; corpus scanner and absorption-candidate classifier.

Canonical packet: this work order plus `docs/baselines/CVF_GC018_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_2026-06-23.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker must capture with `git rev-parse --short HEAD` before edits.

Current-time notes: current dispatch date is 2026-06-23; worker must record actual local start time in the return packet.

Do-not-misread notes: seed folders are required inputs, not complete corpus coverage; legacy sources are candidate input, not canonical authority.

Required first actions: read front door/state/handoff/guard orientation, read this packet, capture `git status --short`, run pre-implementation gate.

Return contract: return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` without committing.

You are the ASSF-T0.1 worker. Execute only the bounded legacy skill corpus
rescan and absorption candidate ledger described in this work order. You must
not commit. Return `COMPLETE_PENDING_REVIEW` only with the required worker
return artifacts present and the reviewer-fast evidence captured, or return
`BLOCKED_WITH_REASON` if a gate fails outside allowed scope.

## Purpose

Provide a no-commit worker packet for the ASSF-T0.1 legacy skill corpus rescan
so the next skill-package tranche starts from filesystem-backed legacy evidence
instead of open tabs, memory, or seed-only assumptions.

## Objective

Scan `.private_reference/legacy/` for skill-related CVF knowledge, classify
candidate files and folders into an absorption ledger, and return a
source-backed packet for Codex review before ASSF-T1 can define the canonical
system-skill package contract and storage topology.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | ASSF-T1 parked pending T0.1 |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Current lane requires T0.1 or fresh authorization |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | Active handoff for governed execution context |
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T0.1 is mandatory before ASSF-T1 |
| GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_2026-06-23.md` | Continuation baseline for this work order |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Dispatch and source-verification controls |
| Dual-agent standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Internal and external CLI/MCP accounting |
| External intake chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Legacy source family routing |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Create source-verified dispatch packet and commit it after gates |
| Worker | assigned worker agent | Scan, classify, create audit and worker-return packet, do not commit |
| Reviewer/closer | Codex | Validate evidence, close T0.1, update session surfaces, and commit if accepted |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V22_2026-06-22.md`
- `docs/reference/guard_orientation/README.md`
- this work order
- `docs/baselines/CVF_GC018_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_2026-06-23.md`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`

## Pre-Flight Checks

- `git rev-parse --short HEAD`
- `git status --short`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base ab7ca99b --head HEAD`

## Write Ownership

The worker owns only the two worker-return artifacts named in Allowed Scope.
Codex owns the dispatch commit, closure review, roadmap closure update, session
sync, and any final material commit.

## Execution Plan

Execute the Required Execution Steps in order. Do not begin ASSF-T1 work. Do
not convert candidate knowledge into package files, schemas, registries,
generated indexes, resolvers, runtime adapters, or public artifacts.

## Evidence Requirements

Evidence must include command-backed corpus enumeration, keyword search
summaries, seed coverage, collision evidence, candidate ledger rows, changed-set
manifest, gate receipts, and explicit no-commit status.

## Review Gate

Codex reviewer must rerun reviewer-fast and relevant autorun gates before
accepting worker output. Worker self-approval is not closure.

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
`COMPLETE_PENDING_REVIEW` only after required artifacts and gate evidence exist.

## Operator Checkpoint

N/A with reason: the operator selected T0.1 dispatch. No extra checkpoint is
required before bounded worker execution; stop conditions define the return path.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-T0.1 must scan legacy skill-related knowledge before ASSF-T1 | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Mandatory Legacy Skill Rescan Gate; ASSF-T0.1 tranche | `ASSF-T0.1` | ASSF roadmap | VALUE_SET | ACCEPT |
| T0.1 required dispositions include contract, lifecycle, package pattern, tool adapter, reference, duplicate, reject, and blocked-source categories | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Required T0.1 output | absorption candidate ledger dispositions | ASSF roadmap | VALUE_SET | ACCEPT |
| T0.1 is not authorized to migrate, create packages, create root, generate index, implement resolver, activate skills, expose adapters, or claim runtime/provider/live/public behavior | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T0.1 tranche; Scope; Fail Conditions | forbidden scope | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| Work-order authors must include source verification before implementation | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Mandatory Work Order Source Verification | `Source Verification Block` | work-order template | LITERAL_INVARIANT | ACCEPT |
| GC-018 legacy-adjacent scope requires legacy scan and blind-spot controls | `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` | Legacy Spec Scan Block; Knowledge Absorption Blind-Spot Control Block | legacy absorption controls | GC-018 template | LITERAL_INVARIANT | ACCEPT |
| Dual Agent Surface Matrix must account for internal and external CLI/MCP consumers | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | `INTERNAL_AGENT`; `EXTERNAL_AGENT_CLI_MCP` | dual-agent surface standard | LITERAL_INVARIANT | ACCEPT |
| Legacy ADK SkillToolset notes identify progressive disclosure, metadata, instructions, resources, and skill loading patterns | `.private_reference/legacy/CVF_Important/ADK SkillToolset/Thong_tin.md` | ADK SkillToolset notes | L1 metadata; L2 instructions; L3 resources | legacy source family | EXISTS | ACCEPT |
| Legacy ADK assimilation log records skill normalization, trigger patterns, and governance signals | `.private_reference/legacy/CVF_Important/ADK SkillToolset/CVF_KNOWLEDGE_ASSIMILATION_LOG.md` | Absorbed Knowledge Modules | Skill Normalization Schema; Planner Trigger Patterns | legacy source family | EXISTS | ACCEPT |
| Legacy Windows normalization notes identify shell and platform assumptions as skill defects | `.private_reference/legacy/CVF_Important/Windows_Skill_Normalization/Thong_tin.md` | Refactor 86 skills for Windows environment | PowerShell conversion; OS compatibility | legacy source family | EXISTS | ACCEPT |
| Legacy skill formation notes define learn, extract, structure, save, reuse and SKILL.md folder pattern | `.private_reference/legacy/CVF_Important/ADDING_CVF_Skill Formation Layer/Thong_tin.md` | Skill Formation Layer notes | Skill as First-Class Object; SKILL.md | legacy source family | EXISTS | ACCEPT |
| Legacy Memento README rejects direct production mutation | `.private_reference/legacy/CVF 16.5/Memento-Skills/README.md` | Core Rule; Canonical Flow | skill improvement proposal; governed reinjection | legacy source family | LITERAL_INVARIANT | ACCEPT |
| Legacy Memento spec lists skill mutation types and approval classes | `.private_reference/legacy/CVF 16.5/Memento-Skills/GOVERNED_SKILL_EVOLUTION_SPEC.md` | Skill Mutation Types; Approval Classes | PATCH_EXISTING_SKILL; CREATE_NEW_SKILL; HUMAN_REVIEW_REQUIRED | legacy source family | VALUE_SET | ACCEPT |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | Codex dispatcher creates work order; worker scans and returns review artifacts; Codex reviewer/closer decides closure and commit |
| phase | DISPATCH_AUTHORING -> WORKER_EXECUTION -> REVIEWER_CLOSURE -> SESSION_SYNC if next move changes |
| baseHeadFor(phase) | dispatchBaseHead=`ab7ca99b`; executionBaseHead=worker must capture with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures from worker return |
| changedSetScope(phase) | worker may create only the audit and worker-return paths named in Allowed Scope |
| traceScope(phase, actor) | worker records commands, manifest, changed-set evidence, and gate receipts in return packet |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; Codex reviewer/closer owns any material and session-sync commit |
| crossBatchIsolation | no ASSF-T1/T2/T3/T4/T5/T6/T7 implementation; no unrelated cleanup |
| nextMoveSurfaces | worker must not edit active session state, session front door, active handoff, or generated active-session aggregate |
| closer designation | Codex reviewer/closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_COMPLETION_2026-06-23.md` |
| workerReturnPath | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_WORKER_RETURN_2026-06-23.md` |
| reviewerOwnedClosurePaths | ASSF roadmap update, T0.1 completion review, active session state/front door/handoff sync, material commit, and session-sync commit if accepted |
| workerReturnDisposition | `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` |
| reviewerCommitRule | Reviewer may commit only after validating worker evidence, rerunning gates, and resolving closure defects |

## Worker Autonomy / No-Question Rule

The worker must repair any machine-gate failure inside Allowed Scope and rerun
the relevant gate without pausing for approval. The worker must stop and return
`BLOCKED_WITH_REASON` only when repair would exceed Allowed Scope, alter
commit mode, touch forbidden paths, require live/provider/public-sync/secrets,
release a new prerequisite, or require session/front-door/handoff ownership.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake class | legacy source family |
| Route mode | `MULTI_AGENT_SINGLE_ROLE` |
| Selected route | Codex dispatcher -> worker scanner/classifier -> Codex reviewer/closer |
| Primary worker role | corpus scanner and absorption-candidate classifier |
| Reviewer role | Codex reviewer/closer validates corpus coverage and closure |
| External intake route | external knowledge intake chain map plus legacy coverage lookup |
| Scope classification | bounded no-commit worker-return over two allowed output paths |
| Risk sensitivity | high because legacy absorption affects future package authority, external CLI/MCP disposition, public-sync boundary, provider/live claim boundary, and production-readiness language |
| Escalation condition | stop with `BLOCKED_WITH_REASON` if remediation exceeds allowed scope, touches forbidden paths, needs new human authorization, or requires session/front-door/handoff ownership |
| Dispatch status | ACCEPT |
| Reason | T0.1 is selected, source-verified, and bounded to no-commit worker-return execution |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index status | NOT_APPLICABLE_WITH_REASON |
| Reason | No canonical legacy coverage index exists for ASSF-T0.1 yet; this work order creates the scan and ledger evidence needed before a later index or guard can exist |
| Required worker evidence | full legacy-root enumeration, seed coverage, keyword searches, candidate ledger, collision evidence, and unresolved-count accounting |
| Future guard candidate | require legacy scan evidence before ASSF package schema dispatch when roadmap declares legacy absorption as a precondition |

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
|---|---|---|---|
| T0.1 audit ledger | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | worker | AWAITING_WORKER_RETURN |
| T0.1 worker return | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_WORKER_RETURN_2026-06-23.md` | worker | AWAITING_WORKER_RETURN |
| T0.1 completion review | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_COMPLETION_2026-06-23.md` | reviewer | REVIEWER_OWNED_AFTER_RETURN |
| Reviewer-fast evidence | command output in worker return | worker | AWAITING_WORKER_RETURN |
| Material commit | git commit after reviewer acceptance | reviewer | REVIEWER_OWNED_AFTER_RETURN |

## Allowed Scope

The worker may create or edit only:

- `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`
- `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_WORKER_RETURN_2026-06-23.md`

The worker may read these roots for evidence:

- `.private_reference/legacy/`
- `governance/skill-library/`
- `docs/roadmaps/`
- `docs/reference/`
- `EXTENSIONS/`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V22_2026-06-22.md`

## Forbidden Scope

The worker must not:

- commit, push, public-sync, or edit Git remotes;
- edit `.private_reference/legacy/`;
- edit active session state/front door/handoff or generated session aggregate;
- create `docs/reference/agent_system_skills/` or any canonical package root;
- create generated index files, resolvers, package schemas, adapters, runtime
  behavior, provider/live proof, CVF Web projection, or UAT/certification
  surfaces;
- change GC-051 corpus registries, roadmap status, baselines, work orders, or
  unrelated files;
- promote legacy/provider-local memory into canonical authority.

## Required Execution Steps

1. Capture startup state:
   - `git rev-parse --short HEAD`
   - `git status --short`
2. Read the active session front door, active session state, active handoff,
   guard orientation index, roadmap, GC-018 baseline, and this work order.
3. Run pre-implementation gate using the dispatch base unless the reviewer has
   provided a newer dispatch commit:
   - `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base ab7ca99b --head HEAD`
4. Enumerate the full legacy root:
   - `rg --files --hidden --no-ignore .private_reference/legacy`
5. Search legacy skill-relevant terms:
   - `rg -n --hidden --no-ignore -i "skill|skills|package|toolset|formation|lifecycle|normalization|memento|adapter|mcp|cli|adk|governed evolution" .private_reference/legacy`
6. Search collision and current-surface terms outside legacy:
   - `rg -n -i "skill|skills|package|toolset|formation|lifecycle|normalization|memento|adapter|mcp|cli|adk|governed evolution" governance/skill-library docs/roadmaps docs/reference EXTENSIONS`
7. Inspect candidate files enough to justify each disposition.
8. Create the audit ledger and worker-return packet.
9. Run:
   - `python governance/compat/run_worker_return_fast_gate.py`
   - `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`
10. Return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`,
    or `BLOCKED_WITH_REASON` without committing.

## Required Deliverables

### Audit Artifact

Path:

`docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`

Required sections:

- Purpose
- Scope And Forbidden Scope
- Source Verification Refresh
- Corpus Completeness And Report Integrity
- Legacy Manifest Summary
- Absorption Candidate Ledger
- Seed Folder Coverage
- Negative Search And Collision Evidence
- Source-Fidelity Notes For Well-Formed CVF Legacy Packets
- Dual Agent Surface Matrix
- Knowledge Absorption Blind-Spot Control Block
- External Knowledge Intake Routing
- Finding-To-Governance Learning Disposition
- Machine-Check Candidate Notes
- Public Export Disposition
- Delta Execution Claim Boundary Control Block
- Agent Operation Trace Block
- Claim Boundary

## Worker Return Packet Shape Contract

Path:

`docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_WORKER_RETURN_2026-06-23.md`

Required sections:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Worker Status
- Required Artifact Manifest
- Roadmap-To-Work-Order Trace Matrix
- Dual Agent Surface Matrix
- Corpus Completeness And Report Integrity
- Legacy Spec Scan Block
- Knowledge Absorption Blind-Spot Control Block
- Negative Search And Collision Evidence
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
and use `N/A with reason` or `NOT_APPLICABLE_WITH_REASON` for conditional
blocks that do not apply.

## Absorption Candidate Ledger Contract

Each candidate row must include:

| Required column | Meaning |
|---|---|
| Candidate path | File or folder path |
| Evidence type | file name, content hit, seed path, collision, or related current surface |
| Source excerpt or section | Short section/heading summary, not long copied text |
| Candidate domain | contract, package pattern, lifecycle/evolution, tool adapter, shell/platform, governance, evaluation, UAT/certification, runtime, web projection, other |
| Internal-agent implication | how it affects internal package loading or task execution |
| External-agent CLI/MCP implication | how it affects CLI/MCP or external agents |
| Disposition | one allowed disposition from this work order |
| Reason | source-backed classification reason |
| Next ASSF owner | T1, T2, T3, T4, T5, T6, T7, REFERENCE_ONLY, or REJECTED |

Allowed dispositions:

- `ABSORB_AS_CONTRACT_INPUT`
- `ABSORB_AS_LIFECYCLE_INPUT`
- `ABSORB_AS_PACKAGE_PATTERN`
- `ABSORB_AS_TOOL_ADAPTER_INPUT`
- `REFERENCE_ONLY`
- `DUPLICATE`
- `REJECT_DIRECT`
- `BLOCKED_UNVERIFIED_SOURCE`

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Required worker evidence | Disposition |
|---|---|---|---|
| Full legacy-root scan before T1 | run full legacy enumeration and keyword search | command output summary, manifest, ledger | READY |
| Seed folders included but not treated as complete | inspect named seed paths and compare against broader scan | seed coverage table and broader results | READY |
| Candidate absorption ledger | classify candidates into allowed dispositions | ledger table | READY |
| Legacy stays non-canonical until re-expressed | claim boundary and source-fidelity notes | no authority promotion language | READY |
| No implementation/migration | forbidden scope and changed-set evidence | `git status --short` plus manifest | READY |
| Dual-agent accounting | include internal and external CLI/MCP implications | Dual Agent Surface Matrix and ledger columns | READY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF future package loader, generated index, and resolver design | T0.1 may produce candidates only; no internal loader behavior or package authority | audit ledger and return packet | no adapter implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external CLI/MCP package discovery/load adapter | T0.1 must classify adapter-relevant legacy knowledge but must not expose or implement adapters | ledger column `External-agent CLI/MCP implication` | separate ASSF adapter work required | `DEFERRED_WITH_REASON` |

## Legacy Spec Scan Block

| Field | Worker requirement |
|---|---|
| Scan root | `.private_reference/legacy/` |
| Required seed paths | ADK SkillToolset; Windows Skill Normalization; ADDING CVF Skill Formation Layer; Memento-Skills |
| Search roots outside legacy | `governance/skill-library/`, `docs/roadmaps/`, `docs/reference/`, `EXTENSIONS/` |
| Required query terms | skill, skills, package, toolset, formation, lifecycle, normalization, memento, adapter, MCP, CLI, ADK, governed evolution |
| Negative evidence rule | absence requires exact command/query/root evidence |
| Collision evidence rule | duplicates and overlapping surfaces must be ledgered, not silently dropped |

## Knowledge Absorption Blind-Spot Control Block

| Required control | Evidence |
|---|---|
| Open tabs are not corpus coverage | explicit statement in audit and return |
| T0 owner audit is not corpus completeness | explicit statement in audit and return |
| Name-only search is insufficient | at least content/section-level inspection for included candidates |
| Legacy direct adoption is forbidden | claim boundary and disposition reasons |
| External-agent disposition is mandatory | ledger column and matrix row |

## Corpus Completeness And Report Integrity

- Corpus task class: LEGACY_RESCAN_WORKER_RETURN.
- Corpus root: `.private_reference/legacy/`.
- Snapshot time: worker must record local date/time.
- Enumeration command: worker must run and record `rg --files --hidden --no-ignore .private_reference/legacy`.
- Manifest artifact or inline manifest: worker must include either a manifest
  section or a path to generated manifest evidence in the audit.
- Manifest hash: optional for text-only inline manifest; if omitted, record
  N/A with reason.
- Processing ledger artifact or inline ledger: audit ledger path/section.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=worker_to_record; ledger_terminal=worker_to_record; exclusions=worker_to_record; unresolved=0 for dispatch packet, worker must replace with actual corpus count in return.
- Unresolved files: 0
- Declared exclusions: non-skill legacy files, binary/unreadable files with
  reason, implementation/migration/public/runtime surfaces.
- Unreadable or unsupported files: list count and reason.
- Aggregation check: N/A with reason unless worker creates a generated
  aggregate, which is not expected.
- Drift check: N/A with reason unless worker creates a generated aggregate,
  which is not expected.
- Output traceability: every absorption conclusion maps to manifest and ledger.
- Adversarial verification: state how the worker avoided seed-only and
  memory-only conclusions.
- Corpus verdict: PARTIAL

## External Knowledge Intake Routing

| Field | Worker requirement |
|---|---|
| Chain map | cite `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Chain map route | legacy source family -> absorption blind-spot control -> ASSF candidate ledger -> reviewer decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T0.1 audit and future ASSF-T1/T4 normalization decisions |
| Disposition | candidate intake only; no direct canonical authority or activation |
| Route | Knowledge Absorption Blind-Spot Control Block plus legacy coverage lookup |
| Boundary | candidate input only; no direct activation or canonical authority |
| External-agent disposition | required in matrix and ledger |
| Claim boundary | legacy and external skills remain candidate inputs, not CVF authority |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
- Delta ledger status: worker must refresh in audit and return packet.
- Routing matrix status: worker must refresh in audit and return packet.
- Semantic sampling status: worker must include at least three samples in audit and return packet.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Worker instruction |
|---|---|
| `UNCHANGED_FROM_INTAKE` | preserve T0 closed bounded owner/surface findings when still valid |
| `CHANGED_DISPOSITION` | record any T0/T0.1 classification changes caused by full legacy scan |
| `NEW_FINDING` | record newly discovered skill-relevant legacy sources |
| `REMOVED_OR_REJECTED` | record duplicates, stale paths, and direct-adoption rejections |

### Follow-Up Routing Matrix

| Routing lane | Worker instruction |
|---|---|
| `DO_NOW` | scan and classify within T0.1 allowed scope |
| `SEPARATE_RUNTIME_TRANCHE` | route runtime/provider/adapter implementation out of scope |
| `STRATEGIC_OPERATOR_DECISION` | flag items needing later strategy before T1/T4/T5 |
| `OUT_OF_SCOPE` | mark migration, package creation, public-sync, root/index/resolver work out of scope |
| `RESOLVED_BY_DESIGN` | mark items handled by no-commit candidate-ledger design |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T0.1-WO-S1 | roadmap Mandatory Legacy Skill Rescan Gate | seed paths are incomplete | full scan required | Could open tabs be enough? | reject |
| ASSF-T0.1-WO-S2 | Memento hard rules | no direct production mutation | no activation | Could legacy self-write be accepted? | reject |
| ASSF-T0.1-WO-S3 | dual-agent standard | external CLI/MCP row required | external disposition | Could internal-only accounting pass? | reject |

The worker must record whether this defect class should become a future
machine-check candidate. At minimum, evaluate:

- work orders for schema/package design must require legacy scan evidence if
  the roadmap declares legacy absorption as a precondition;
- closure packets must fail if external-agent disposition is absent;
- candidate ledgers should include internal-agent and external CLI/MCP columns.

## Finding-To-Governance Learning Disposition

| Field | Required worker value |
|---|---|
| Defect class | choose one or more: `LEGACY_SCAN_GAP`, `SOURCE_FIDELITY_GAP`, `EXTERNAL_AGENT_DISPOSITION_GAP`, `PACKAGE_AUTHORITY_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `DESIGN_REVIEW_REQUIRED`, `MACHINE_CHECK_CANDIDATE`, or `REFERENCE_ONLY` |
| Next control action | state whether T1/T4/T5/T7 should absorb each control |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance scan over `.private_reference/legacy/`. Public-safe
skill architecture output requires later redaction and public-sync authority.

## Acceptance Criteria

- Required artifacts exist in allowed paths only.
- Legacy root enumeration and keyword search are command-backed.
- Seed paths are covered but not treated as full corpus.
- Ledger rows use only allowed dispositions and include internal/external
  implications.
- Well-formed CVF legacy packets are identified as candidates, not authority.
- Negative search and collisions are explicit.
- No commit is made by the worker.
- Reviewer-fast gates are run or failure is classified.

## Stop Conditions

Return `BLOCKED_WITH_REASON` if:

- pre-implementation gate fails outside allowed scope;
- `.private_reference/legacy/` is unavailable;
- worker cannot create the two required artifacts;
- any required scan command cannot run and no equivalent safe filesystem
  command is available;
- required source facts cannot be verified without exceeding allowed scope;
- a repair would require session sync, roadmap/baseline/work-order edits,
  public-sync, live/provider proof, package/root/index/resolver/adapter
  implementation, or a commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T0_1_DISPATCH_READY` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_2026-06-23.md` | `Status: DISPATCH_READY` | PASS |
| Work order status | this file | `Status: DISPATCH_READY` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_WORKER_RETURN_2026-06-23.md` | PENDING_WORKER_RETURN | PENDING |
| Audit ledger | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | PENDING_WORKER_RETURN | PENDING |
| Completion review | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_COMPLETION_2026-06-23.md` | REVIEWER_OWNED_AFTER_RETURN | PENDING |
| Registry JSON | N/A with reason | no GC-051 registry update authorized | N/A with reason |
| Registry Markdown | N/A with reason | no GC-051 registry update authorized | N/A with reason |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable files created by worker | audit ledger and worker-return packet only |
| Canonical package root | N/A with reason: forbidden until ASSF-T1/T2 source-verified closure |
| Generated index or aggregate | N/A with reason: forbidden by this work order |
| Storage migration | N/A with reason: out of scope |
| Layout risk | bounded documentation outputs only; reviewer owns closure commit |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Work order status | `DISPATCH_READY` | `DISPATCH_READY` | PASS |
| Worker commit mode | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Allowed output paths | audit and worker-return only | audit and worker-return only | PASS |
| External-agent disposition required | yes | yes | PASS |
| Package/root/index/resolver implementation | forbidden | forbidden | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | Worker-return legacy scan and absorption candidate ledger |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - no-commit worker-return dispatch only |
| receiptEvidence | CVF_RECEIPT_PRESENT - worker must provide command and gate receipts in return packet |
| actionEvidence | ACTION_EVIDENCE_PRESENT - worker must provide manifest, ledger, and changed-set evidence |
| invocationBoundary | governed local filesystem scan and documentation return |
| interceptionBoundary | no provider/runtime/API/browser interception claim |
| claimLanguage | scan and classify legacy skill candidates |
| forbiddenExpansion | no commit, package root, generated index, resolver, runtime, CLI/MCP adapter, public-sync, or active skill claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T0.1 dispatch, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, governance gates, git commit by dispatcher only |
| Target paths | this work order; T0.1 GC-018 baseline; ASSF roadmap |
| Allowed scope source | operator instruction to create work order |
| Before status evidence | clean worktree at HEAD `ab7ca99b` |
| After status evidence | ASSF-T0.1 dispatch ready |
| Diff evidence | real-range name-status and gate output before dispatcher commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | worker-return lane; no implementation |
| Agent type | dispatcher |
| Invocation ID | `cvf-assf-t0-1-legacy-skill-corpus-rescan-work-order-2026-06-23` |
| Expected manifest | this work order; T0.1 GC-018 baseline; ASSF roadmap |
| Actual changed set | this work order; T0.1 GC-018 baseline; ASSF roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This work order authorizes only a no-commit worker-return legacy scan and
absorption candidate ledger. It does not authorize ASSF-T1, package contract
freeze, storage topology creation, skill package creation, generated index,
resolver, runtime/provider/live proof, public-sync, CLI/MCP adapter
implementation, session sync, or worker commit.
