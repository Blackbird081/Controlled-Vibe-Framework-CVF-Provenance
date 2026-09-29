# CVF Agent Work Order - KIOD-R1-R3 Knowledge Intake Deduplication Foundation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: work_order

Batch ID: KIOD-R1-R3

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: f3200159

executionBaseHead: f3200159

closureBaseHead: f3200159

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role dispatcher, implementer, reviewer, and
closer for KIOD-R1-R3.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R1_R3_KNOWLEDGE_INTAKE_DEDUPLICATION_FOUNDATION_2026-06-30.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_KIOD_R1_R3_KNOWLEDGE_INTAKE_DEDUPLICATION_FOUNDATION_2026-06-30.md`.

Commit mode: `WORKER_MAY_COMMIT`.

Base: `f3200159`.

Mission summary: create the R1 owner-surface taxonomy, R2 pre-scan packet
standard, and R3 overlap routing matrix before any next selected source pilot.

Do-not-misread notes: this work order does not authorize selected source
intake, runtime work, package activation, new checker implementation, Web/UI,
provider/live proof, public-sync, or production-readiness claims.

## Purpose

Provide the executable R1-R3 packet that turns KIOD-T0's deduplication roadmap
into reusable references and closure evidence.

## 1. Mission

Create and close three ordered references:

- KIOD-R1 owner-surface taxonomy;
- KIOD-R2 pre-scan packet standard;
- KIOD-R3 overlap routing matrix standard.

Success means future agents can classify source value against an owner surface,
complete a pre-scan packet, and choose a routing action before opening a new
lane.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-06-30 to handle KIOD-R1 -> R2 -> R3 first | authorizes this batch |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V29_2026-06-30.md` | active handoff named by state registry |
| Roadmap | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | R1-R3 planned sequence |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_KIOD_R1_R3_KNOWLEDGE_INTAKE_DEDUPLICATION_FOUNDATION_2026-06-30.md` | scope and claim boundary |

Authority boundary: this work order executes only R1-R3 reference foundation.
R4 checker decision and R5 pilot remain later moves.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author source-verified baseline and work order |
| Implementer | Codex | create R1-R3 references and roadmap update |
| Reviewer/closer | Codex | run guards, write completion review, commit material |
| Operator checkpoint owner | human operator | choose KIOD-R4 decision route or next selected source after R1-R3 |

## 4. Scope

Allowed scope:

- create KIOD-R1, KIOD-R2, and KIOD-R3 reference files;
- create paired GC-018, work order, and completion review;
- update the KIOD-T0 roadmap status and next decision;
- run focused docs/governance gates and commit material changes.

Allowed paths:

- `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md`
- `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md`
- `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md`
- `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md`
- `docs/baselines/CVF_GC018_KIOD_R1_R3_KNOWLEDGE_INTAKE_DEDUPLICATION_FOUNDATION_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R1_R3_KNOWLEDGE_INTAKE_DEDUPLICATION_FOUNDATION_2026-06-30.md`
- `docs/reviews/CVF_KIOD_R1_R3_KNOWLEDGE_INTAKE_DEDUPLICATION_FOUNDATION_COMPLETION_2026-06-30.md`

Forbidden scope:

- selected source intake or source mirror mutation;
- runtime, provider, MCP/CLI adapter, package lifecycle, generated Web data, or
  dashboard implementation;
- new checker implementation;
- public-sync, push, or public catalog claims;
- live/provider proof or production-readiness claims.

Risk ceiling: R1 documentation/governance foundation.

## Scope / Target / Owner Boundary

Target: source-verified R1-R3 reference foundation for future knowledge intake
deduplication.

Owner boundary: Codex owns this documentation closure. Future checker,
runtime, provider, public, dashboard, adapter, and selected-source pilot lanes
need separate authorization.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`knowledge-intake-deduplication`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

Disclosure command:

```text
python governance/compat/run_adif_defect_resolver.py --task-class knowledge-intake-deduplication --role dispatcher --lifecycle-phase dispatch --json
```

## 5. Required First Reads

| Path | Action | Why it matters |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | FULL_READ | front-door continuity |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | FULL_READ | compact mode and next move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | FULL_READ | canonical generated state |
| `AGENT_HANDOFF_V29_2026-06-30.md` | FULL_READ | active handoff |
| `docs/reference/guard_orientation/README.md` | FULL_READ | guard routing orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ | literal-format traps |
| `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | SOURCE_VERIFIED | R1-R3 authority |
| `governance/compat/check_external_knowledge_intake_routing.py` | SOURCE_VERIFIED | routing block shape |
| `governance/compat/check_external_absorption_overlap_discipline.py` | SOURCE_VERIFIED | overlap table shape |

## 6. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| KIOD-T0 names R1 owner-surface taxonomy as the next tranche | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | Work Plan | `KIOD-R1` | KIOD-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| KIOD-T0 names R2 pre-scan packet standard | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | Work Plan | `KIOD-R2` | KIOD-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| KIOD-T0 names R3 routing matrix | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | Work Plan | `KIOD-R3` | KIOD-T0 roadmap | LITERAL_INVARIANT | ACCEPT |
| Routing block requires seven field rows | `governance/compat/check_external_knowledge_intake_routing.py` | constants | `REQUIRED_FIELDS` | external knowledge intake routing checker | RUNTIME_BEHAVIOR | ACCEPT |
| Routing block input types are canonical enum values | `governance/compat/check_external_knowledge_intake_routing.py` | constants | `ALLOWED_INPUT_TYPES` | external knowledge intake routing checker | RUNTIME_BEHAVIOR | ACCEPT |
| Overlap table requires owner-surface, disposition, delta, and action columns | `governance/compat/check_external_absorption_overlap_discipline.py` | constants | `REQUIRED_COLUMNS` | overlap discipline checker | RUNTIME_BEHAVIOR | ACCEPT |
| Overlap dispositions are a fixed token set | `governance/compat/check_external_absorption_overlap_discipline.py` | constants | `ALLOWED_DISPOSITIONS` | overlap discipline checker | RUNTIME_BEHAVIOR | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | roadmap, routing checker, overlap checker, package productionization SOP |
| Runtime behavior claimed | N/A_WITH_REASON: no runtime behavior is modified or claimed |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| KIOD-R1 owner-surface taxonomy | Execution Plan | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | `check_external_knowledge_intake_routing.py` | PASS |
| KIOD-R2 pre-scan packet | Execution Plan | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | `check_external_knowledge_intake_routing.py` | PASS |
| KIOD-R3 routing matrix | Execution Plan | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | `check_external_absorption_overlap_discipline.py` | PASS |
| Park R4/R5 | Claim Boundary | roadmap next decision | autorun pre-closure | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatcher -> Codex implementer -> Codex reviewer/closer |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=f3200159`; `executionBaseHead=f3200159`; `closureBaseHead=f3200159` |
| changedSetScope(phase) | R1-R3 reference files, GC-018, work order, completion review, and KIOD-T0 roadmap update |
| traceScope(phase, actor) | work order and completion review carry repo-local trace evidence |
| commitOwner(phase) | Codex reviewer/closer owns material commit; separate session-sync commit follows if continuity changes |
| crossBatchIsolation | clean worktree at dispatch; no unrelated material paths in this batch |
| nextMoveSurfaces | session front door, generated active session state, and active handoff if next move changes |

## Pre-Flight Checks

| Check | Status |
|---|---|
| Startup front door and active handoff read | PASS |
| Guard orientation and literal-format gotchas read | PASS |
| ADIF disclosure query run | PASS |
| Pre-implementation autorun on `f3200159..HEAD` before edits | PASS |

## Execution Plan

1. Create R1 owner-surface taxonomy with owner categories and route actions.
2. Create R2 pre-scan packet standard with required fields and stop conditions.
3. Create R3 routing matrix with overlap-disposition-to-action mapping.
4. Update KIOD-T0 roadmap to record R1-R3 pass and make R4 the next decision.
5. Create completion review and run focused guards, autorun, and commit steward.

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Existing owner-surface priority | KIOD-T0 Design Control Gate | R1 taxonomy lists owner surfaces first | PASS |
| Non-goals | KIOD-T0 Non-Goals | forbidden scope keeps runtime/public/provider parked | PASS |
| Lane split | KIOD-T0 Work Plan | executes R1-R3 only | PASS |
| Dependency/source-verification plan | KIOD-T0 Source Verification Block | source verification recorded above | PASS |
| Claim boundary | KIOD-T0 Claim Boundary | no selected source or runtime claim | PASS |
| Acceptance criteria | KIOD-T0 Acceptance Criteria | completion review records R1-R3 evidence | PASS |
| Verification/evidence | KIOD-T0 Verification / Evidence | focused guards and autorun gates required | PASS |
| Dispatch-readiness decision | KIOD-T0 Authorization / Decision | R1 was the next allowed tranche | PASS |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | `docs/reference/external_agent_review/` |
| Storage decision | create three stable reference filenames for KIOD-R1, KIOD-R2, and KIOD-R3 |
| Stable filename disposition | stable filenames omit date suffixes and rely on git history plus completion evidence |
| Generated aggregate discipline | N/A with reason: no generated JSON aggregate is added or changed |
| Authority boundary | references define intake routing only, not runtime/source behavior |
| Forbidden expansion | no selected source intake, checker implementation, package activation, provider/live proof, public-sync, dashboard, adapter, or production-readiness claim |

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | Codex | create |
| `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | Codex | create |
| `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | Codex | create |
| `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | Codex | update R1-R3 status and R4 next move |
| KIOD-R1-R3 baseline, work order, and completion review | Codex | create |

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `python governance/compat/check_external_knowledge_intake_routing.py --base f3200159 --head HEAD --enforce` | PASS |
| `python governance/compat/check_external_absorption_overlap_discipline.py --base f3200159 --head HEAD --enforce` | PASS |
| `python governance/compat/check_markdown_structural_completeness.py --base f3200159 --head HEAD --enforce` | PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base f3200159 --head HEAD` | PASS |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base f3200159 --head HEAD --enforce` | PASS |

## Review Gate

Reviewer/closer must confirm:

- R1-R3 artifacts exist and are inside allowed scope;
- R1-R3 do not claim selected source intake or runtime behavior;
- roadmap next move advances to KIOD-R4 decision;
- all focused and autorun gates pass.

## Closure Checklist

| Item | Status |
|---|---|
| R1 taxonomy created | PASS |
| R2 pre-scan packet standard created | PASS |
| R3 routing matrix standard created | PASS |
| KIOD-T0 roadmap updated | PASS |
| Completion review filed | PASS |
| Public/provenance boundary preserved | PASS |

## Return-To-Orchestrator Conditions

Return `BLOCKED` if any required source fact is missing, any reference claims
selected source intake, or any gate failure requires runtime, package, provider,
public-sync, dashboard, adapter, or checker implementation outside this scope.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | R1 owner-surface taxonomy exists | R1 reference file |
| AC2 | R2 pre-scan packet standard exists | R2 reference file |
| AC3 | R3 routing matrix exists | R3 reference file |
| AC4 | Roadmap records R1-R3 pass and R4 next | KIOD-T0 roadmap |
| AC5 | No forbidden runtime/public/package/provider claim is made | claim boundary and gates |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator decision -> KIOD-T0 roadmap -> KIOD-R1 taxonomy -> KIOD-R2 pre-scan packet -> KIOD-R3 routing matrix -> KIOD-R4 negative-search decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` |
| Disposition | ADAPT operator-approved deduplication discipline into reference artifacts |
| Claim boundary | documentation foundation only; no selected source intake, runtime, package, provider, public, dashboard, adapter, or production-readiness claim |

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: NOT_APPLICABLE_WITH_REASON - package-skill references are owner
surface labels only.

Target lifecycle state: NOT_APPLICABLE_WITH_REASON - no package skill lifecycle
state is changed.

Prior phase evidence: KIOD-R1-R3 relies on existing package-skill governance
surfaces only as possible owner surfaces.

Next forbidden skip: future package candidate intake cannot skip the ASSF
package productionization SOP, UAT, truth packet, usage receipt, resolver, or
live/provider proof requirements.

Runtime/provider proof: N/A with reason: no runtime, package, provider, model,
or live governance behavior is claimed.

Claim boundary: no package conversion, lifecycle mutation, activation, adapter
behavior, or production-readiness claim is made.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | KIOD-R1-R3 knowledge intake deduplication foundation on 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | R1-R3 reference files, KIOD-T0 roadmap, baseline, work order, completion review |
| Allowed scope source | operator instruction plus KIOD-T0 roadmap and paired baseline |
| Before status evidence | base commit `f3200159`; clean worktree before edits |
| After status evidence | material changed set pending gates |
| Diff evidence | `git diff --name-status` and pre-closure gate |
| Approval boundary | operator requested KIOD-R1 -> R2 -> R3 before later lanes |
| Claim boundary | reference foundation only |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-kiod-r1-r3-knowledge-intake-deduplication-foundation-2026-06-30` |
| Expected manifest | baseline, work order, R1-R3 references, roadmap update, completion review |
| Actual changed set | baseline, work order, R1-R3 references, roadmap update, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation. Public-safe export requires a
separate public-sync decision.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_KIOD_R1_R3_KNOWLEDGE_INTAKE_DEDUPLICATION_FOUNDATION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_KIOD_T0_KNOWLEDGE_INTAKE_OVERLAP_DEDUPLICATION_ROADMAP_2026-06-30.md` | R1-R3 `PASS_BOUNDED`; R4 next | PASS |
| Registry JSON | N/A with reason: no generated registry JSON changed | N/A with reason | PASS |
| Registry Markdown | R1-R3 reference files | `Status: ACTIVE_REFERENCE` | PASS |
| External evidence digest | N/A with reason: no selected source evidence digest created | N/A with reason | N/A with reason |
| System loop interlock | R1-R3 references | future intake routes through R1-R3 | PASS |
| Session continuity | session-sync may follow material closure | N/A with reason | PASS |
| Focused tests | governance guards and autorun gates | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| R1 taxonomy | present | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md` | PASS |
| R2 pre-scan packet standard | present | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md` | PASS |
| R3 routing matrix | present | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md` | PASS |
| Provider/live claim | none | NOT_RUN_WITH_REASON | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | KIOD-R1-R3 documentation foundation |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT - reference files, roadmap update, baseline, work order, and completion review |
| invocationBoundary | local governed Markdown authoring only |
| interceptionBoundary | no IDE, shell hook, git hook, provider, MCP, Web, public-sync, or runtime interception claim |
| claimLanguage | defines references and routing for future knowledge intake deduplication |
| forbiddenExpansion | no selected source intake, runtime, package activation, provider/live proof, public-sync, dashboard, adapter, checker implementation, or production-readiness claim |

## Claim Boundary

This work order closes only R1-R3 documentation foundation. It does not absorb
or certify a selected source, mutate runtime or package state, run providers,
publish public artifacts, implement a new checker, or prove semantic
completeness.

## Operator Checkpoint

No immediate human input is required to close R1-R3. After closure, the next
human decision is KIOD-R4 negative-search evidence decision or a later pilot
only after that decision is made.
