# CVF GC-018 Baseline: ASSF Web Projection Schema Mapping Decision

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-26

docType: baseline

Batch ID: ASSF-WEBPROJ-T0

dispatchBaseHead: 42bdf2f6

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | dispatch a decision-first Web projection schema and mapping task |
| Baseline | certification metadata exists, but Web schema and mapping mutation remain deferred |
| Proposed tranche | `ASSF-WEBPROJ-T0` |
| Worker route | Codex single-agent multi-role, material packet first |
| Closure posture | `DISPATCH_READY` |

## Purpose

Authorize a bounded ASSF Web projection schema/mapping decision work order.
The task decides which CVF Web fields and mapping surfaces should carry or
derive certified ASSF package metadata in a later implementation tranche.

This baseline does not authorize Web runtime mutation. It prepares the
source-verified decision packet required before any Web route, component,
schema, data file, or mapping code changes.

## Scope / Methodology

In scope:

- source-verified decision review for ASSF Web projection schema and mapping;
- comparison of current ASSF certified metadata against current CVF Web skill
  types, front-door read model, and template mapping surfaces;
- selection of allowed future implementation surfaces;
- explicit non-go decisions for external CLI/MCP adapter behavior and runtime
  projection.

Out of scope:

- Web route, component, API, schema, mapping, public data, or test mutation;
- package instance creation, certification decision, lifecycle mutation,
  generated-index mutation, resolver mutation, adapter implementation,
  provider/live proof, public-sync, push, activation, or package execution.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| Active next move authorizes this packet | SATISFIED | `CVF_SESSION_MEMORY.md` Next Allowed Move names ASSF Web projection schema/mapping decision GC-018 and work order |
| Admission gate and Web projection decision closed | SATISFIED | `docs/reviews/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_COMPLETION_2026-06-26.md` |
| Certified metadata is present | SATISFIED | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` lines 71-72 |
| Generated index carries metadata-only certified readout | SATISFIED | `docs/reference/agent_system_skills/generated/skill-index.json` lines 2 and 16-92 |
| Web schema/mapping requires source-verified decision first | SATISFIED | `docs/reviews/CVF_ASSF_ADMISSION_T4_CLOSURE_NEXT_CONTROL_2026-06-26.md` |

## Evidence / Verification

| Evidence | Result |
|---|---|
| `git rev-parse --short HEAD` | `42bdf2f6` before dispatch authoring |
| `git status --short` | clean worktree before dispatch authoring |
| `python governance/compat/check_assf_skill_index_drift.py` | required pre-execution evidence |
| `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | required pre-execution evidence |
| `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase PRE_DISPATCH --surface governance/compat --risk-ceiling R0 --max-results 5` | returned one metadata-only R0 dispatch-authoring skill packet during dispatch authoring |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Web projection contract defines classification vocabulary | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 80-90 | `CERTIFIED_PACKAGE_PROJECTION` | ASSF Web projection contract | VALUE_SET | ACCEPT |
| Web projection contract separates canonical and presentation surfaces | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 93-102 | `skill-index.json` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Web projection contract forbids activation by projection | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 105-128 | `frontDoorTier` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Lifecycle guard requires certified package and Web schema work before bridge | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 176-183 | `certificationState` | ASSF lifecycle guard contract | LITERAL_INVARIANT | ACCEPT |
| Admission completion parks Web projection until source-verified Web work order | `docs/reviews/CVF_ASSF_CERTIFIED_METADATA_ADMISSION_GATE_AND_WEB_PROJECTION_DECISION_T0_T4_COMPLETION_2026-06-26.md` | Findings / Position | `OPEN_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_WORK_ORDER` | ASSF admission completion | LITERAL_INVARIANT | ACCEPT |
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

Remediation applied: this baseline avoids exhaustive directory claims, cites
CVF-governed sources and current repository source files only, keeps boundary
trigger prose inside scope sections, and uses bare field/function/token symbols
in Source Verification rows.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| No unsupported source field is accepted | all Source Verification rows use `ACCEPT` with existing files and symbols | PASS |
| No negative-search field is promoted to source fact | missing-field decisions are deferred to the future decision review | PASS |
| Collision handling | no same-name baseline or work order existed before this add-only dispatch packet | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF Web projection schema/mapping decision artifacts | internal agents may use the decision to author a later Web implementation work order; this packet does not grant runtime, activation, package execution, or session-sync authority | Web projection contract, lifecycle guard, registry entry, generated index, Web source files | no internal Web loader, API route, component, or data mutation is implemented by this tranche | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external agent or CLI/MCP adapter reading projected package metadata | external agents cannot infer adapter availability, certification authority, mutation authority, or package execution rights from this packet | Dual Agent standard and ASSF Web projection adapter-separation invariant | adapter remains deferred; separate source-verified adapter work order required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator next-move direction to governed GC-018/source-verified work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order coverage | Planned closure evidence | Disposition |
|---|---|---|---|
| Source-verified Web projection schema/mapping decision | Work order Required Outputs and Source Verification Block | decision review | PASS |
| Decision-first before implementation | Forbidden scope and claim boundary | completion review | PASS |
| External adapter remains separated | Dual Agent Surface Matrix | decision review and completion review | PASS |
| Existing certified metadata consumed read-only | Source Verification Block | registry/index read evidence | PASS |

## Planned Artifact Manifest

| Artifact | Purpose | Status |
|---|---|---|
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_FOR_CODEX_2026-06-26.md` | paired source-verified work order | PRESENT |
| `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md` | future decision review | PLANNED |
| `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_COMPLETION_2026-06-26.md` | future completion review | PLANNED |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| AC1 | Decision review names the exact Web schema fields or rejects field addition with reason |
| AC2 | Decision review maps ASSF certified metadata fields to current Web surfaces or records a blocking source-not-found disposition in the review |
| AC3 | No Web runtime, registry source, generated index, resolver, adapter, provider, public, or session paths change in the material decision commit |
| AC4 | The completion review records whether a later implementation work order is valuable and names its exact allowed surfaces |

## Fail Conditions

Return `BLOCKED_WITH_REASON` if:

- a needed Web field or mapping source cannot be found and no doc-only decision
  is safe;
- certification metadata cannot be source-verified from registry/index sources;
- the decision would require immediate Web runtime mutation, adapter behavior,
  provider/live proof, public-sync, or package execution;
- governance gates fail outside the allowed packet scope.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF Web projection schema/mapping dispatch baseline |
| claimDisposition | N/A with reason: dispatch authorization only; no implementation or runtime claim |
| receiptEvidence | N/A with reason: no runtime receipt is created by this baseline |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- source verification and dependency release evidence |
| invocationBoundary | governed local dispatch packet authoring only |
| interceptionBoundary | no provider, Web runtime, CLI, MCP, adapter, package execution, or filesystem interception claim |
| claimLanguage | decision-first dispatch for later schema/mapping review |
| forbiddenExpansion | no package instance, certification decision, lifecycle mutation, registry mutation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, package instruction execution, or session-sync in material packet |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | local repository tools |
| Session or invocation | ASSF-WEBPROJ-T0 dispatch packet, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, Python resolver, source reads, apply_patch |
| Target paths | this baseline; paired work order |
| Allowed scope source | active session next allowed move after front-door compaction |
| Before status evidence | HEAD `42bdf2f6`; `git status --short` returned no paths |
| After status evidence | pending dispatch packet changed set |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | GC-018 and source-verified work order only |
| Claim boundary | dispatch packet only; no Web runtime, package, adapter, provider, public, generated-index, resolver, registry, or session mutation |
| Agent type | dispatch author |
| Invocation ID | ASSF-WEBPROJ-T0-DISPATCH-2026-06-26 |
| Expected manifest | this baseline; paired work order |
| Actual changed set | this baseline; paired work order |
| Manifest delta | MATCH |

## Claim Boundary

This baseline authorizes only a decision-first work order. It does not
implement, expose, certify, activate, execute, export, or adapt any package or
Web projection surface.
