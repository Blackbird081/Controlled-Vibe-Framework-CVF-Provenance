# CVF GC-018 Baseline: ASSF-T6 CVF Web Projection And Existing Example Migration

Memory class: FULL_RECORD

Status: APPROVED_FOR_EXECUTION

Date: 2026-06-25

docType: baseline

Batch ID: ASSF-T6

## Proposed Tranche

Tranche: ASSF-T6

Baseline decision: documentation and audit tranche to define the CVF Web
projection boundary for agent system-skill packages and classify existing CVF
Web skill or template examples for later migration. This tranche does not
implement a Web route, runtime adapter, package instance, generated-index
change, or activation path.

Verdicts:
- Dispatcher verdict: DISPATCH_APPROVED
- Worker verdict: PENDING_WORKER_EXECUTION
- Reviewer verdict: PENDING_CODEX_REVIEW

## Purpose

Establish the governance baseline for ASSF-T6. The worker must author a CVF
Web projection contract and a migration audit that separates current
plain-language Web templates and skill examples from future certified agent
system-skill packages.

Success means the project can later expose package information in CVF Web
without letting presentation examples become canonical execution authority and
without hiding the external-agent CLI/MCP adapter boundary.

## Evidence / Verification

Dispatch evidence is limited to source verification, dependency release
evidence, ADIF disclosure, Dual Agent Surface Matrix, and planned worker
artifact paths. Worker-created contract, audit, return, and completion packets
do not exist at dispatch time and must not be claimed as complete until the
worker return supplies command-backed evidence.

## Scope / Applies To

Applies to:

- future CVF Web package projection design;
- existing CVF Web skill/template mappings and example classification;
- future package certification review that needs to know whether an existing
  Web example is a projection, candidate, legacy reference, duplicate, or
  rejected example;
- internal and external agent surfaces that consume projected package metadata.

Does not apply to:

- runtime CVF Web implementation;
- route, component, API, loader, generator, checker, resolver, or test edits;
- package root creation;
- `SKILL.md` or `skill.source.json` creation;
- generated-index mutation;
- provider, live, MCP, CLI, public-sync, or adapter implementation.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| ASSF-T1 Canonical Package Contract | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_COMPLETION_2026-06-23.md`; roadmap Machine Closure Package row |
| ASSF-T2 Generated Index And Progressive Resolver | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_COMPLETION_2026-06-23.md`; generated index and resolver rows in roadmap Machine Closure Package |
| ASSF-T3 Learning And ADIF Promotion Bridge | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_COMPLETION_2026-06-23.md`; roadmap Machine Closure Package row |
| ASSF-T4 External And Legacy Intake Normalization | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md`; roadmap Machine Closure Package row |
| ASSF-T5 Composition, Dependency, Conflict, And Capability Controls | CLOSED_PASS_BOUNDED | `docs/reviews/CVF_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_COMPLETION_2026-06-25.md`; material commit `d0a24e90` and session-sync commit `15f1ea2a` |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | future CVF Web projection contract and migration audit under the agent system skills reference family | T6 defines a presentation and audit boundary only; internal agents may read the contract and audit but cannot treat Web examples as active package authority | this GC-018, the ASSF roadmap T6 section, T1 package contract, T2 metadata-only resolver and index, T5 composition contract, and source-verified Web skill/template mapping surfaces | no internal loader, resolver change, route, or runtime projection is implemented by this tranche | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external CLI/MCP or adapter readout that may expose package projection metadata after a separate adapter contract | T6 must name external disposition for every projection class; no external agent may mutate, certify, activate, or execute packages through this tranche | Dual Agent Surface Accounting Standard plus T1 external disposition fields and T6 worker audit rows | adapter owner is deferred; separate source-verified adapter work order required before CLI/MCP exposure | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF roadmap authorizes T6 CVF Web Projection And Existing Example Migration | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T6 section | `ASSF-T6` | ASSF roadmap | EXISTS | ACCEPT |
| Roadmap states CVF Web projects packages and does not own canonical truth | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Design Principles | `CVF Web projects packages` | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| Roadmap requires current concept page to describe form-based skill templates and Web projection | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Source Verification Block | `docs/concepts/skill-system.md` | ASSF roadmap | EXISTS | ACCEPT |
| T1 package contract defines identity fields for future packages | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `skillId` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 package contract defines lifecycle fields for future packages | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `certificationState` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 package contract defines external CLI/MCP disposition fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `externalCliMcpDisposition` | ASSF-T1 package schema | EXISTS | ACCEPT |
| T1 package contract says adapters are projections of canonical packages | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Internal-Agent And External-Agent CLI/MCP Disposition Fields | `adapterContract` | ASSF-T1 package schema | LITERAL_INVARIANT | ACCEPT |
| T2 generated index is metadata-only and not activation evidence | `docs/reference/agent_system_skills/generated/skill-index.json` | claimBoundary | `claimBoundary` | ASSF-T2 generated index | LITERAL_INVARIANT | ACCEPT |
| T2 resolver exposes deterministic read-only metadata resolution | `governance/compat/run_assf_skill_resolver.py` | module docstring and `resolve_skill_packet` | `resolve_skill_packet` | ASSF-T2 resolver | EXISTS | ACCEPT |
| T5 composition contract requires no authority expansion from loading or composing packages | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | Authority And Risk Boundary | `authorityCeiling` | ASSF-T5 composition contract | LITERAL_INVARIANT | ACCEPT |
| CVF Web has a template-to-skill mapping data source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json` | `templateToSkillMap` | `templateToSkillMap` | CVF Web skill-template mapping | EXISTS | ACCEPT |
| CVF Web skill-template map separates templates as input side and skills as knowledge side | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-template-map.ts` | file header comment | `templateToSkillMap` | CVF Web skill-template mapping | LITERAL_INVARIANT | ACCEPT |
| CVF Web exposes lookup function for a template's related skill | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-template-map.ts` | `getSkillForTemplate` | `getSkillForTemplate` | CVF Web skill-template mapping | EXISTS | ACCEPT |
| Concept page defines skills as form-based templates | `docs/concepts/skill-system.md` | What is a Skill? | `.skill.md` | current product skill concept | EXISTS | ACCEPT |
| Dual Agent standard requires both internal and external rows and adapter boundary | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Mandatory Dual Agent Surface Matrix | `EXTERNAL_AGENT_CLI_MCP` | Dual Agent Surface Accounting Standard | VALUE_SET | ACCEPT |
| Governed artifact literal-format gotchas checklist exists | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Purpose | `CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Governed Artifact Literal Format Gotchas | EXISTS | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:
- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0006: Source Verification symbol cell contains a value/type
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class

Remediation applied:
- ADIF-0001: This baseline does not claim exhaustive CVF Web coverage; it dispatches a worker audit to enumerate and classify the relevant surfaces.
- ADIF-0002: Source Verification ACCEPT rows cite CVF-governed docs or current repository source files only.
- ADIF-0006: Verified path or symbol cells contain only field, path, function, or section tokens.
- ADIF-0007: Exclusion prose avoids treating unrelated gate keywords as evidence claims.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | operator request to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline and the matching ASSF-T6 work order |
| Disposition | contract and audit dispatch only; no external material is absorbed |
| Claim boundary | no external-agent packet, adapter behavior, public claim, or provider proof is accepted as source authority |

## Required Worker Deliverables

| Path | Required at handoff | Purpose |
|---|---|---|
| `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Yes | Canonical T6 Web projection contract |
| `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | Yes | Classification audit for existing Web skill/template examples |
| `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_WORKER_RETURN_2026-06-25.md` | Yes | Worker return with evidence and gate receipts |
| `docs/reviews/CVF_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_COMPLETION_2026-06-25.md` | Yes | Completion packet for Codex review and closure |
| `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Yes | T6 closure rows after worker execution |

## Acceptance Criteria

- Web projection contract defines canonical-vs-presentation boundary.
- Web projection contract includes the Dual Agent Surface Matrix.
- Existing Web skill/template examples are classified with one of:
  `CERTIFIED_PACKAGE_PROJECTION`, `PACKAGE_CANDIDATE`,
  `LEGACY_REFERENCE_ONLY`, `DUPLICATE_OR_SUPERSEDED`, or
  `REJECTED_WITH_REASON`.
- Audit explains why no existing Web example may become certified solely by
  being listed in Web surfaces.
- External-agent CLI/MCP disposition is explicit for every projection class.
- Worker return includes source-backed enumeration commands and no exhaustive
  coverage claim beyond the executed search roots.
- Completion review remains pending Codex review until Codex validates closure.
- No runtime/source code, generated index, package instance, adapter, provider,
  live, public-sync, or session state surface is changed by the worker.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T6 Web projection contract and existing example migration audit dispatch |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch baseline only |
| receiptEvidence | N/A with reason: no runtime execution, provider call, or adapter receipt exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block and dispatch artifact manifest |
| invocationBoundary | governed local documentation dispatch only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, or Web runtime interception claim |
| claimLanguage | authorizes a bounded documentation and audit tranche for Claude worker execution |
| forbiddenExpansion | no runtime Web implementation, route, component, API, resolver, generator, checker, package instance, SKILL.md, skill.source.json, generated-index mutation, CLI/MCP adapter, provider/live proof, public-sync, or session-sync edit by worker |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this dispatch references private provenance architecture and repository
source surfaces. Public-safe export requires a separate redaction and
public-sync authorization.

## Dispatch Readiness Package

| Readiness item | Required artifact/path | Evidence | Status |
|---|---|---|---|
| Roadmap status | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T5_CLOSED_PASS_BOUNDED`; T6 parked pending operator selection | PASS |
| GC-018 status | this file | `Status: APPROVED_FOR_EXECUTION` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_FOR_WORKER_2026-06-25.md` | `Status: APPROVED_FOR_EXECUTION` | PASS |
| Worker output paths | this file | Required Worker Deliverables table | PASS |
| External adapter boundary | this file | Dual Agent Surface Matrix | PASS |
| Runtime implementation | N/A with reason | runtime implementation is forbidden in this tranche | N/A with reason |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T5_CLOSED_PASS_BOUNDED`; T6 selected by operator after T5 | PASS |
| GC-018 status | this file | `Status: APPROVED_FOR_EXECUTION` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T6_CVF_WEB_PROJECTION_EXISTING_EXAMPLE_MIGRATION_FOR_WORKER_2026-06-25.md` | `Status: APPROVED_FOR_EXECUTION` | PASS |
| Worker material artifacts | N/A with reason | pending Claude worker execution | N/A with reason |
| Completion or reviewer artifact | N/A with reason | pending Claude worker execution and Codex review | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: T6 dispatch is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: T6 dispatch is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported; external-agent boundary is contract-only | N/A with reason |
| System loop interlock | this file | ASSF-T6 routes from T1-T5 architecture into future T7 certification without activation | PASS |
| Session continuity | N/A with reason | Codex session-sync will occur after dispatch commit; worker must not edit session surfaces | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Dispatch status | APPROVED_FOR_EXECUTION | APPROVED_FOR_EXECUTION | PASS |
| Worker material artifacts | pending worker execution | pending worker execution | PASS |
| Runtime/provider receipt | N/A with reason | no runtime/provider action authorized | PASS |
| External adapter receipt | N/A with reason | no CLI/MCP adapter authorized | PASS |

## Claim Boundary

This baseline is dispatch authority only. It does not prove the Web projection
contract exists, does not classify any Web example yet, does not create or
activate any package, and does not authorize public-sync or external adapter
implementation. Closure requires worker artifacts, gate evidence, and Codex
review.
