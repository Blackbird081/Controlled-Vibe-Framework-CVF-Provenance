# CVF GC-018 Baseline: ASSF Web Projection Implementation

Memory class: FULL_RECORD
Status: DISPATCH_READY
Date: 2026-06-26
docType: baseline
Batch ID: ASSF-WEBPROJ-T1
dispatchBaseHead: cf50a81f

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | dispatch a source-verified Web projection implementation work order |
| Baseline | ASSF-WEBPROJ-T0 selected `OPEN_WEB_PROJECTION_IMPLEMENTATION_WORK_ORDER` |
| Proposed tranche | `ASSF-WEBPROJ-T1` |
| Worker route | Codex single-agent multi-role, material packet first |
| Closure posture | `DISPATCH_READY` |

## Purpose

Authorize a bounded implementation work order that projects certified ASSF
package metadata into the CVF Web skill index as read-only presentation data.
This baseline authorizes a Web implementation tranche only after the
decision-first packet closed and source verification identified the Web
public skill-index production path.

## Scope / Methodology

In scope:

- add optional ASSF projection fields to the Web `Skill` read model;
- extend the Web skill-index generator to read the ASSF generated skill index;
- project certified ASSF package entries into Web presentation records without
  granting activation, adapter, package execution, or certification authority;
- update the generated Web public skill-index artifact by running the generator;
- add focused Web tests for type, generator, and display behavior.

Out of scope:

- creating or changing ASSF registry entries;
- changing ASSF generated-index source or resolver behavior;
- creating package instances;
- making a certification decision;
- mutating package lifecycle state;
- implementing CLI/MCP adapter behavior;
- provider/live proof;
- public-sync or push.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| Active next move authorizes this packet | SATISFIED | `CVF_SESSION_MEMORY.md` Next Allowed Move names fresh GC-018 and source-verified work order for Web projection implementation |
| Decision-first prerequisite is complete | SATISFIED | `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_COMPLETION_2026-06-26.md` recommends `OPEN_WEB_PROJECTION_IMPLEMENTATION_WORK_ORDER` |
| Web data production path is source-verified | SATISFIED | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` lines 7-8 and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` lines 412-437 |
| Certified ASSF metadata exists | SATISFIED | `docs/reference/agent_system_skills/generated/skill-index.json` lines 14-16, 55-70, and 92-94 |
| Adapter remains deferred | SATISFIED | `docs/reference/agent_system_skills/generated/skill-index.json` lines 8-25 |

## Evidence / Verification

| Evidence | Result |
|---|---|
| `git rev-parse --short HEAD` | `cf50a81f` before dispatch authoring |
| `git status --short` | clean worktree before dispatch authoring |
| `python governance/compat/check_assf_skill_index_drift.py` | required pre-dispatch evidence |
| `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | required pre-dispatch evidence |
| ADIF resolver API call for work-order authoring/dispatcher/pre-dispatch | returned ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006 |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Web predev/prebuild scripts generate the skill index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | lines 7-8 | `build-skill-index.js` | Web package scripts | RUNTIME_BEHAVIOR | ACCEPT |
| Web generator currently reads legacy skill roots and corpus governance | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` | lines 8-12 and 277-280 | `buildSkillIndex` | Web skill-index generator | EXISTS | ACCEPT |
| Web generator currently creates skill records | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` | lines 337-364 | `skillRecord` | Web skill-index generator | EXISTS | ACCEPT |
| Web generator writes public skills-index JSON | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` | lines 412-437 | `writeIndex` | Web skill-index generator | RUNTIME_BEHAVIOR | ACCEPT |
| Web `Skill` type is the read-model target | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | lines 7-34 | `Skill` | CVF Web Skill type | EXISTS | ACCEPT |
| Web `SkillIndexMeta` is the meta target | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | lines 42-50 | `SkillIndexMeta` | CVF Web Skill index payload | EXISTS | ACCEPT |
| Web library loads public skill index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillLibrary.tsx` | lines 23-44 | `SkillLibrary` | Web skill library component | EXISTS | ACCEPT |
| Web detail view renders one skill record | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillDetailView.tsx` | lines 11-92 | `SkillDetailView` | Web skill detail component | EXISTS | ACCEPT |
| Web front-door search reads public skill index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/frontdoor-skills.ts` | lines 28-36 | `fetchFrontDoorSkillRecords` | Web front-door reader | EXISTS | ACCEPT |
| Web projection contract defines projection vocabulary | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 80-91 | `CERTIFIED_PACKAGE_PROJECTION` | ASSF Web projection contract | VALUE_SET | ACCEPT |
| Web projection contract forbids activation by projection | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 113-128 | `frontDoorTier` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Lifecycle contract requires separate Web schema bridge | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 176-184 | `certificationState` | ASSF lifecycle guard contract | LITERAL_INVARIANT | ACCEPT |
| ASSF generated index is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 1-5 | `claimBoundary` | ASSF generated skill index | LITERAL_INVARIANT | ACCEPT |
| ASSF generated index carries certified package fields | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 14-16 and 55-70 | `certificationState` | ASSF generated skill index | VALUE_SET | ACCEPT |
| ASSF generated index carries UAT pass state | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 92-94 | `uatState` | ASSF generated skill index | VALUE_SET | ACCEPT |
| Current Web tests load public skill index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-corpus-governance.test.ts` | lines 10-24 and 72-83 | `loadSkillIndex` | Web corpus governance tests | EXISTS | ACCEPT |

## New Doc-Only Fields

These fields are authorized as new Web presentation/read-model fields for the
implementation worker to add. They must not be cited as existing source facts
until the worker creates them.

| Field | Target surface | Purpose | Boundary |
|---|---|---|---|
| `assfProjectionClass` | Web `Skill` | presentation classification from ASSF Web projection vocabulary | read-only display; no authority grant |
| `certificationState` | Web `Skill` | projected ASSF certification state | display only; ASSF registry remains canonical |
| `uatState` | Web `Skill` | projected ASSF UAT state | display only |
| `reviewArtifacts` | Web `Skill` | projected evidence paths | links or text only; no proof expansion |
| `canonicalRoot` | Web `Skill` | trace back to ASSF registry source | display trace only |
| `externalCliMcpDisposition` | Web `Skill` | adapter availability disposition | must remain deferred unless separate adapter work order exists |
| `adapterContract` | Web `Skill` | adapter contract text/path when applicable | display only; no adapter implementation |
| `projectionClaimBoundary` | Web `Skill` | explicit no-activation/no-authority text | display only |
| `assfProjectedSkills` | Web `SkillIndexMeta` | count of projected ASSF records | informational counter |
| `certifiedPackageProjections` | Web `SkillIndexMeta` | count of `CERTIFIED_PACKAGE_PROJECTION` records | informational counter |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

API invocation used: `resolve_defect_packet(task_class="Work-order authoring / dispatch", role="dispatcher", lifecycle_phase="pre-dispatch")`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate marker in boundary prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied: this baseline uses bounded path manifests, cites
CVF-governed and runtime source only, keeps source-symbol cells free of
value/type syntax, and keeps trigger-prone boundary prose in explicit control
blocks.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | Web projection implementation artifacts | internal agents may display/read projected metadata but cannot mutate package state, certify packages, or execute package instruction bodies | ASSF Web projection contract and T0 decision review | no internal route activates a package | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external adapter or programmatic readout | external agents cannot use Web projection as an adapter, certification source, package executor, or mutation channel | adapter-separation invariant and generated index adapter fields | adapter remains deferred; separate source-verified adapter work order required | `DEFERRED_WITH_REASON` |

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
| Implement T0 Web projection decision | Required Outputs and Execution Plan | completion review | PASS |
| Source-verify data production path | Source Verification Block | worker return Source Verification Block | PASS |
| Keep certification state separate from corpus class | Implementation Requirements and tests | generated index diff and tests | PASS |
| Preserve adapter boundary | Dual Agent Surface Matrix and Claim Boundary | completion review | PASS |

## Planned Artifact Manifest

| Artifact | Purpose | Status |
|---|---|---|
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_WEB_PROJECTION_IMPLEMENTATION_FOR_CODEX_2026-06-26.md` | paired implementation work order | PRESENT |
| `docs/reviews/CVF_ASSF_WEB_PROJECTION_IMPLEMENTATION_WORKER_RETURN_2026-06-26.md` | future worker return | PLANNED |
| `docs/reviews/CVF_ASSF_WEB_PROJECTION_IMPLEMENTATION_COMPLETION_2026-06-26.md` | future reviewer/closure review | PLANNED |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| AC1 | Web `Skill` and `SkillIndexMeta` include optional ASSF projection fields without removing existing fields |
| AC2 | Web skill-index generator reads ASSF generated metadata and emits read-only projection records or bounded zero-match evidence |
| AC3 | Generated Web public skill-index is updated only through the generator |
| AC4 | UI displays projected certification metadata only when present and keeps adapter/deferred boundary visible |
| AC5 | Focused Web tests and governance gates pass |

## Fail Conditions

Return `BLOCKED_WITH_REASON` if:

- ASSF generated index cannot be read safely by the Web generator;
- Web projection would require mutating ASSF registry, generated ASSF index,
  resolver, package lifecycle state, or certification state;
- implementation would imply package activation or CLI/MCP adapter support;
- focused tests cannot be made deterministic without provider/live proof;
- governance gates fail outside the allowed packet scope.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF Web projection implementation dispatch baseline |
| claimDisposition | N/A with reason: dispatch authorization only; no implementation claim |
| receiptEvidence | N/A with reason: no runtime receipt is created by this baseline |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source verification and dependency release evidence |
| invocationBoundary | governed local dispatch packet authoring only |
| interceptionBoundary | no provider, CLI, MCP, adapter, package execution, or interception claim |
| claimLanguage | implementation work order authoring only |
| forbiddenExpansion | package instance, certification decision, lifecycle mutation, ASSF registry mutation, ASSF generated-index mutation, resolver mutation, CLI/MCP adapter, provider/live proof, public-sync, push, activation, and package instruction execution remain out of scope |

## Current Runtime Freshness Verification

| Runtime claim | Verification command or source | Observed value | Disposition |
|---|---|---|---|
| Web public skill-index has a generator path | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` | `predev`/`prebuild` call `build-skill-index.js`; script writes the public skills-index artifact | PASS |
| ASSF metadata source is generated and metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | `claimBoundary` states metadata-only | PASS |
| Adapter is not implemented by this dispatch | ASSF generated index adapter fields and this claim boundary | adapter disposition remains deferred | PASS |

## Claim Boundary

This baseline authorizes only dispatch of the paired implementation work order.
It does not perform implementation, certify packages, create package instances,
run providers, implement adapters, public-sync, push, mutate ASSF registry
source, mutate ASSF generated-index source, mutate resolver source, activate
packages, or execute package instruction bodies.
