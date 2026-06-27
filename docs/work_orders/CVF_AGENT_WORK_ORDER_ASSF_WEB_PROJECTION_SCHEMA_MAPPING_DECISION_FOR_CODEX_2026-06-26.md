# CVF Agent Work Order: ASSF Web Projection Schema Mapping Decision

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: work_order

Batch ID: ASSF-WEBPROJ-T0

dispatchBaseHead: 42bdf2f6

executionBaseHead: 42bdf2f6

closureBaseHead: 3d983897

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role worker/reviewer/closer for a decision-only
ASSF Web projection schema/mapping tranche.

executionBaseHead: `42bdf2f6`

Current-time notes: active handoff is `AGENT_HANDOFF_V23_2026-06-26.md`; active
front door is compacted; this packet follows material-only dispatch and keeps
session-sync separate.

Required first actions: read the paired GC-018 baseline, read all Required First
Reads, run the pre-flight checks, and stop before any forbidden Web/runtime or
package mutation.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_FOR_CODEX_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT` for execution review artifacts until the
reviewer/closer accepts them. Codex may later close and commit as reviewer only
after the required review artifacts and gates pass.

Return contract: produce decision and completion review artifacts, then close
bounded if source evidence supports it. Return `BLOCKED_WITH_REASON` if a
schema/mapping decision cannot be made without forbidden implementation scope.

Do-not-misread notes: this work order does not authorize Web runtime mutation,
registry source mutation, generated-index mutation, resolver source mutation,
package instance creation, certification decision, package activation, CLI/MCP
adapter implementation, provider/live proof, public-sync, push, or session-sync
inside the material execution commit.

## Purpose

Decide the source-backed ASSF Web projection schema and mapping plan for a
future implementation tranche. The output must answer which current Web
surfaces should carry or derive certified ASSF package metadata, and which
surfaces must remain unchanged until a later implementation work order.

## Scope / Target / Owner Boundary

Target: a decision review and completion review for ASSF Web projection
schema/mapping.

Owner boundary: Codex may create only the review artifacts named in Write
Ownership during execution. Codex must not mutate Web source, ASSF registry
source, generated index, resolver source, package roots, adapter source, active
session surfaces, or public-sync surfaces in the material execution commit.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator next move | ASSF Web projection schema/mapping decision GC-018 plus source-verified work order, decision-first | ACCEPT |
| Active front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V23_2026-06-26.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md` | ACCEPT |
| Web projection contract | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | ACCEPT |
| Lifecycle guard contract | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | approves next-move lane and later scope expansion |
| Dispatcher | Codex |
| Worker | Codex, no commit during execution artifact drafting |
| Reviewer | Codex after execution artifacts exist |
| Closer | Codex after reviewer acceptance |
| Session-sync steward | Codex in a separate commit after the material commit, if next move changes |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | active next allowed move naming ASSF Web projection schema/mapping decision GC-018 and work order |
| Scope classification | bounded source-verified decision packet and later review artifacts |
| Intake role | Codex dispatches and may execute decision artifacts without committing until reviewer closure |
| Reviewer role | Codex reviewer/closer validates artifacts, gates, boundaries, and commits accepted material |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; single-agent multi-role with reviewer closure conversion |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `SINGLE_AGENT_MULTI_ROLE` |
| selected role route | Codex dispatch author to Codex no-commit worker to Codex reviewer/closer |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if the decision requires Web runtime mutation, package mutation, adapter behavior, provider/live proof, public-sync, push, or broader scope |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | READ | active front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup facts |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | active state registry |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | READ | role and guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | literal-format pre-write checklist |
| `docs/baselines/CVF_GC018_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md` | READ | paired authorization baseline |
| `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | READ | canonical projection boundary |
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | READ | certification and bridge preconditions |
| `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | READ | certified package source entry |
| `docs/reference/agent_system_skills/generated/skill-index.json` | READ | generated metadata-only readout |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | SOURCE_VERIFIED | current Web skill payload shape |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/frontdoor-skills.ts` | SOURCE_VERIFIED | current front-door loader |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-template-map.ts` | SOURCE_VERIFIED | current template-to-skill mapping |

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/check_assf_certified_metadata_admission.py --require-certified
python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase PRE_DISPATCH --surface governance/compat --risk-ceiling R0 --max-results 5
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Web projection contract defines classification vocabulary | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 80-90 | `CERTIFIED_PACKAGE_PROJECTION` | ASSF Web projection contract | VALUE_SET | ACCEPT |
| Web projection contract separates canonical and presentation surfaces | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 93-102 | `skill-index.json` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Web projection contract forbids activation by projection | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 105-128 | `frontDoorTier` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Lifecycle guard requires certified package and Web schema work before bridge | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 176-183 | `certificationState` | ASSF lifecycle guard contract | LITERAL_INVARIANT | ACCEPT |
| Admission completion recommends this next control | `docs/reviews/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_COMPLETION_2026-06-26.md` | top metadata and Findings / Position | `OPEN_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_WORK_ORDER` | ASSF admission completion | LITERAL_INVARIANT | ACCEPT |
| Registry entry records certified candidate state | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 71-72 | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| Registry entry records certification review artifacts | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 17-21 | `reviewArtifacts` | ASSF registry entry | VALUE_SET | ACCEPT |
| Generated index claim boundary is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | line 2 | `claimBoundary` | ASSF generated index | LITERAL_INVARIANT | ACCEPT |
| Current Web Skill type has `corpusClass` and no ASSF `certificationState` field | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | lines 7-33 | `corpusClass` | CVF Web Skill type | EXISTS | ACCEPT |
| Current Web skill index metadata lacks ASSF certification counters | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | lines 42-50 | `SkillIndexMeta` | CVF Web Skill index payload | EXISTS | ACCEPT |
| Current Web front-door loader reads `/data/skills-index.json` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/frontdoor-skills.ts` | lines 25-32 | `fetchFrontDoorSkillRecords` | CVF Web front-door skill loader | EXISTS | ACCEPT |
| Current Web template mapping owns template-to-skill linkage | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-template-map.ts` | lines 26-41 | `templateToSkillMap` | CVF Web skill-template mapping | EXISTS | ACCEPT |
| ASSF resolver is metadata-only and read-only | `governance/compat/run_assf_skill_resolver.py` | lines 202-258 | `resolve_skill_packet` | ASSF metadata resolver | EXISTS | ACCEPT |
| ASSF certified metadata checker entry point exists | `governance/compat/check_assf_certified_metadata_admission.py` | lines 170-226 | `check` | ASSF certified metadata admission checker | EXISTS | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

API invocation used: `resolve_defect_packet(task_class="Work-order authoring / dispatch", role="dispatcher", lifecycle_phase="pre-dispatch")`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate marker in boundary prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied: use bounded file lists, CVF-governed source files only,
source symbols without value/type assignments, and compact boundary prose.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatches, executes no-commit decision artifacts, reviews, and closes if evidence supports closure |
| phase | DISPATCH_AUTHORING; EXECUTION; REVIEWER_CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=42bdf2f6`; `executionBaseHead=42bdf2f6`; closure base recorded in completion review |
| changedSetScope(phase) | dispatch packet first; later decision/completion reviews only; session-sync separate |
| traceScope(phase, actor) | each material artifact records Agent Operation Trace Block |
| commitOwner(phase) | Codex reviewer/closer owns material commit when execution artifacts pass gates |
| crossBatchIsolation | no Web runtime, package, adapter, provider, public, resolver, generated-index, registry, or session-sync mutation in execution commit |
| Before status evidence | dispatchBaseHead `42bdf2f6`; clean worktree evidence: `git status --short` returned no paths before dispatch authoring |
| nextMoveSurfaces | updated only in a separate session-sync commit after the accepted material commit |
| Closer designation | Codex reviewer/closer |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Role separation ledger | dispatch packet, decision review, completion review, material commit, and session-sync are separate steps |
| Evidence basis | source verification, pre-flight checks, reviewer-fast/pre-closure gates, commit steward preflight |
| Self-review boundary | Codex may review its own decision artifact only against the work order and machine gates; forbidden scope remains blocked |
| Gate sequence | pre-dispatch for packet, pre-closure/reviewer-return for execution artifacts, session-sync gates only after material commit |
| Escalation conditions | any required Web runtime, package lifecycle, adapter, provider/live, public-sync, or push action |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | decision review and completion review only, unless closure finds an allowed documentation-only correction in this work order or paired baseline |
| workerReturnStatus | N/A with reason: Codex single-agent multi-role execution |
| closer | Codex |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | Web projection schema/mapping decision artifacts | internal agents may use the decision to draft a later implementation work order; no direct runtime, activation, package execution, or authority expansion is granted | source verification and decision review | no internal Web loader, route, component, generated data, or mapping mutation in this tranche | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter or external readout of projected package metadata | no external agent can certify, mutate, execute, activate, or consume packages through this decision | Dual Agent standard and Web projection contract adapter invariant | adapter remains deferred; separate source-verified adapter work order required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator next-move direction to governed GC-018/source-verified work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order instruction | Expected closure evidence | Disposition |
|---|---|---|---|
| Make schema/mapping decision before implementation | Required Outputs and Execution Plan | decision review | PASS |
| Source-verify Web fields and mapping surfaces | Source Verification Block | decision review Source Verification Block | PASS |
| Keep adapter separated | Dual Agent Surface Matrix | completion review claim boundary | PASS |
| Preserve no runtime mutation | Forbidden Changed Paths And Actions | git diff evidence | PASS |

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md` | Codex | create decision review |
| `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_COMPLETION_2026-06-26.md` | Codex | create completion review |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable governance files created by worker | two review artifacts under the reviews directory only |
| New generated aggregate | N/A with reason: no generated aggregate, generated index, registry, resolver, or Web data output is authorized |
| New source layout | N/A with reason: no source-layout split, package root, Web source, adapter source, or registry source family is authorized |
| Index or registry mutation | N/A with reason: ASSF generated index and registry entries remain read-only inputs |
| Storage owner | documentation evidence under the planned review paths |
| Closure disposition required | reviewer verifies changed paths exactly match Write Ownership before any material commit |

## Forbidden Changed Paths And Actions

Forbidden in the material execution commit:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/`
- `docs/reference/agent_system_skills/registry/`
- `docs/reference/agent_system_skills/generated/`
- `governance/compat/run_assf_skill_resolver.py`
- `governance/compat/generate_assf_skill_index.py`
- package roots, package instruction bodies, and package source JSON files
- `CVF_SESSION/`, `CVF_SESSION_MEMORY.md`, and `AGENT_HANDOFF*.md`
- public-sync clone paths or push operations

No provider/live proof, CLI/MCP adapter implementation, package activation,
package execution, package certification decision, or lifecycle mutation is
authorized.

## Required Outputs

| Output | Required content |
|---|---|
| Decision review | schema field decision, mapping surface decision, adapter decision, no-runtime claim boundary |
| Completion review | closure verdict, source verification, changed-path evidence, next-control recommendation |
| Next-control recommendation | one of `OPEN_WEB_PROJECTION_IMPLEMENTATION_WORK_ORDER`, `PARK_WEB_PROJECTION_WITH_REASON`, or `OPEN_ADAPTER_CONTRACT_DECISION` |

## Worker Return Packet Shape Contract

This single-agent multi-role work order does not require a separate worker
return artifact, but because the commit mode is `WORKER_MUST_NOT_COMMIT`, the
packet shape contract is recorded for gate compatibility and future external
worker reuse.

Required worker-return sections if delegated later:

- `Status`
- `dispatchWorkOrder`
- `Purpose`
- `Source Inventory`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Claim Boundary`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Machine Closure Package`
- actual `executionBaseHead`
- actual `git status --short`
- changed-path list
- command evidence
- no commit statement

If any section is not applicable, include the section with `N/A with reason`
or `NOT_APPLICABLE_WITH_REASON` and a short reason instead of omitting it.

## Execution Plan

1. Re-run pre-flight checks and verify worktree cleanliness.
2. Read the required ASSF and Web source files.
3. Decide whether future Web projection should extend `Skill`, `SkillIndexMeta`,
   `frontdoor-skills.ts`, `skill-template-map.ts`, generated public data, or a
   different surface.
4. Create the decision review with explicit accepted, rejected, and deferred
   mapping rows.
5. Create the completion review with gate evidence and next-control
   recommendation.
6. Run reviewer-fast or pre-closure gates on the material range.
7. Commit material closure only if gates pass.
8. Perform session-sync separately after the material commit.

## Evidence Requirements

| Evidence | Required disposition |
|---|---|
| `git status --short` before execution | clean or explain blocking paths |
| `check_assf_skill_index_drift.py` | PASS or BLOCKED_WITH_REASON |
| `check_assf_certified_metadata_admission.py --require-certified` | PASS or BLOCKED_WITH_REASON |
| Source Verification | all accepted source facts cite current files and symbols |
| Changed paths | limited to Write Ownership during execution |
| Runtime mutation check | no forbidden paths changed |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| AC1 | Decision review names accepted, rejected, and deferred Web projection fields or records a blocking source-not-found disposition |
| AC2 | Decision review maps ASSF certified metadata source fields to current Web Skill, front-door, or template mapping surfaces |
| AC3 | Completion review proves changed paths stayed inside Write Ownership |
| AC4 | No Web runtime, package, registry, generated-index, resolver, adapter, provider, public, push, or session-sync mutation appears in the material execution commit |
| AC5 | Next-control recommendation is one of the three required tokens |

## Closure Checklist

| Check | Required resolution |
|---|---|
| Decision review exists | PASS or BLOCKED with reason |
| Completion review exists | PASS or BLOCKED with reason |
| Source verification current | PASS or BLOCKED with reason |
| Forbidden changed paths absent | PASS or BLOCKED with reason |
| Governance gates pass | PASS or BLOCKED with reason |
| Session-sync separated from material commit | PASS or BLOCKED with reason |

## Worker Autonomy / No-Question Rule

Codex must repair allowed-scope artifact-shape and gate violations without
asking the operator. Codex must stop and return `BLOCKED_WITH_REASON` only when
the fix requires forbidden implementation scope, unavailable authority, or a
non-local operator decision.

## Review Gate

Before material closure, Codex reviewer/closer must run:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 42bdf2f6 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base 42bdf2f6 --head HEAD --enforce
git diff --check
```

If a gate requires a narrower base after dispatch commit, record the adjusted
base in the completion review.

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` if the decision and completion reviews are created,
source verification is current, gates pass, and no forbidden paths are changed.

Return `BLOCKED_WITH_REASON` if the schema/mapping decision would require
immediate Web implementation, adapter work, package lifecycle mutation,
provider/live proof, public-sync, or unresolved source authority.

## Operator Checkpoint

Operator checkpoint is required before:

- implementing Web source changes;
- exposing certified metadata through a runtime route or public data artifact;
- implementing CLI/MCP adapter behavior;
- changing registry source, generated index, or resolver behavior;
- public-sync or push.

## Current Runtime Freshness Verification

| Runtime claim | Verification command or source | Observed value | Disposition |
|---|---|---|---|
| Web runtime/source mutation is outside this work order | `git diff --name-status` for ASSF-WEBPROJ-T0 material range | No cvf-web runtime path is in the expected material manifest | PASS |
| CLI/MCP adapter implementation is outside this work order | Work order forbidden scope and claim boundary | Adapter work remains deferred to a separate contract decision | PASS |
| Provider/live proof is outside this work order | Work order forbidden scope and claim boundary | No provider or live proof command is authorized | PASS |
| Package instance/certification mutation is outside this work order | Work order forbidden scope and claim boundary | No package instance or certification decision is authorized | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_COMPLETION_2026-06-26.md` | `closureDisposition: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason | No roadmap status changed by this decision-only execution. | N/A with reason |
| Registry JSON | N/A with reason | ASSF registry and GC-051 registry mutation are outside this decision-only work order. | BLOCKED with reason |
| Registry Markdown | N/A with reason | No registry markdown mutation is authorized by this decision-only work order. | BLOCKED with reason |
| External evidence digest | N/A with reason | No external evidence or live provider proof used. | N/A with reason |
| System loop interlock | `governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 3d983897 --head HEAD` | Required before commit. | PASS |
| Session continuity | Session-sync separate from material closure | Session surfaces intentionally unchanged in material commit. | PASS |

## Acceptance Receipt Assertion Matrix

| Receipt ID | Required value | Observed value | Status |
|---|---|---|---|
| ARAM-WEBPROJ-WO-001 | Decision artifact exists | `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md` | PASS |
| ARAM-WEBPROJ-WO-002 | Completion artifact exists | `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_COMPLETION_2026-06-26.md` | PASS |
| ARAM-WEBPROJ-WO-003 | Next recommendation is allowed | `OPEN_WEB_PROJECTION_IMPLEMENTATION_WORK_ORDER` | PASS |
| ARAM-WEBPROJ-WO-004 | Runtime mutation remains forbidden | No cvf-web runtime path in material manifest | PASS |
| ARAM-WEBPROJ-WO-005 | Session-sync remains separate | No session path in material manifest | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF Web projection schema/mapping decision work order |
| claimDisposition | N/A with reason: dispatch and decision artifacts only; no runtime execution claim |
| receiptEvidence | N/A with reason: no runtime receipt is produced by this work order |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- source verification, pre-flight checks, and future closure gate evidence |
| invocationBoundary | governed local repository artifact authoring only |
| interceptionBoundary | no provider, Web runtime, CLI, MCP, adapter, package execution, or filesystem interception claim |
| claimLanguage | decision-first source mapping for later implementation |
| forbiddenExpansion | no package instance, certification decision, lifecycle mutation, registry mutation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, package instruction execution, or session-sync in material execution commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | local repository tools |
| Session or invocation | ASSF-WEBPROJ-T0 work order dispatch, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, Python resolver, source reads, apply_patch |
| Target paths | this work order; paired GC-018 baseline |
| Allowed scope source | active session next allowed move after front-door compaction |
| Before status evidence | HEAD `42bdf2f6`; clean worktree evidence: `git status --short` returned no paths |
| After status evidence | pending dispatch packet changed set |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | GC-018 and source-verified work order only |
| Claim boundary | dispatch packet only; no Web runtime, package, adapter, provider, public, generated-index, resolver, registry, or session mutation |
| Agent type | dispatch author |
| Invocation ID | ASSF-WEBPROJ-T0-WORK-ORDER-DISPATCH-2026-06-26 |
| Expected manifest | this work order; paired GC-018 baseline |
| Actual changed set | this work order; paired GC-018 baseline |
| Manifest delta | MATCH |

## Claim Boundary

This work order authorizes a decision review and completion review only. It
does not implement, expose, certify, activate, execute, export, or adapt any
package or Web projection surface.
