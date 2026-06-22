# CVF Agent System Skills Foundation Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_PENDING_T0_SELECTION_AFTER_ADIF

Date: 2026-06-23

docType: roadmap

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This roadmap plans
a future generated skill-package index; it is not that index.

## Purpose

Define an architecture-scale CVF Agent System Skills foundation in which each
reusable agent capability is a governed package, packages are discovered
through a generated index, and agents progressively load only the skills
relevant to task, role, lifecycle phase, surface, and risk.

The current CVF Web skill examples and domain categories are presentation and
template surfaces. They are inputs to reconciliation, not proof that a
canonical system-skill package architecture already exists.

## Authorization / Decision

The operator directed CVF to build this foundation early rather than waiting
for the Learning Plane to finish. Future skills formed from learning, absorbed
from external sources, or recovered from legacy must all converge through the
same package, index, provenance, risk, UAT, and lifecycle architecture.

ADIF remains the active execution lane. This roadmap is parked until ADIF
review/closure or a separately authorized isolated tranche.

## Scope

In scope: owner reconciliation, legacy/external/current skill inventory,
canonical package design, generated discovery index, progressive resolver,
learning promotion, intake normalization, composition controls, CVF Web
projection, certification, UAT, drift, and lifecycle planning.

Out of scope: implementation in this roadmap batch, bulk migration, skill
activation, runtime tool execution, CLI/MCP adapter implementation,
provider/live proof, public-sync, or claims that current Web examples are
certified system packages.

## Design Control Gate

ASSF-T0 must reconcile existing owners and legacy absorption before T1 freezes
storage or schema. No later tranche may dispatch from proposed paths or fields
as if they already exist. Every child requires fresh GC-018, Source
Verification, roadmap trace, Dual Agent Surface Matrix, and dependency-release
evidence.

## Architecture Principles

1. One canonical package contract; multiple provider/export adapters.
2. Package identity and authority remain distinct from discovery metadata.
3. Metadata-first index resolution precedes `SKILL.md` and reference loading.
4. Learning, external intake, and legacy absorption all produce candidates,
   never immediate `ACTIVE` skills.
5. CVF Web projects packages; it does not own canonical skill truth.
6. Generated aggregates come from compact package sources.
7. Skill composition declares dependencies, conflicts, risk, authority, side
   effects, and evidence requirements.
8. Every package accounts for internal agents and external CLI/MCP consumers
   under the Dual Agent Surface Accounting Standard.

## Proposed Package Topology

The exact root is a T0 decision. The intended logical shape is:

```text
<canonical-system-skill-root>/
  README.md
  packages/
    <skill-id>/
      SKILL.md
      skill.source.json
      agents/
      references/
      scripts/
  registry/
    entries/
  generated/
    skill-index.json
```

`SKILL.md` is the progressive instruction front door. Compact machine-readable
sources own identity, selectors, provenance, lifecycle, risk, and adapter
dispositions. Generated index files must not be hand-edited.

## Candidate Package Contract

T0/T1 must reconcile, not blindly adopt, these field families:

- identity, version, owner, status, provenance, license;
- purpose, trigger, task classes, roles, phases, surface and risk selectors;
- canonical sources and authority boundary;
- prerequisites, dependencies, conflicts and composition order;
- input/output contract and acceptance evidence;
- side effects, permissions, commit/action authority and rollback;
- internal-agent disposition;
- external-agent CLI/MCP disposition;
- learning/legacy/external origin and promotion evidence;
- UAT, certification, deprecation, successor and retirement state;
- provider adapter/export mappings that never become canonical authority.

## Intake Convergence

| Intake lane | Candidate evidence | Mandatory normalization | Activation boundary |
|---|---|---|---|
| Learning/ADIF | repeated governed findings, promoted controls, accepted completion evidence | dedupe, canonical owner link, task/role/phase selectors, evidence threshold | review + UAT; no automatic promotion |
| External skills | screened source, license/provenance, security and capability analysis | adapt/reject decision, authority firewall, runtime/tool boundary | CVF-owned package only after review |
| Legacy CVF | corpus registry, archived skill analyses, prior roadmaps/work orders, partial absorption records | source refresh, owner reconciliation, stale claim rejection | forward-only package or explicit legacy-only disposition |
| Existing CVF Web examples | template/domain metadata and user-facing forms | separate presentation fields from canonical agent execution contract | projection only until package-certified |

## Mandatory Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Disposition |
|---|---|---|---|---|
| `INTERNAL_AGENT` | future system-skill resolver and package loader | governed task/role/phase/risk selection; no authority expansion from loading | T1/T2 contract and tests required | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP skill discovery/load adapter | adapter contract, authentication/approval/receipt and mutation boundary required | separate source-verified adapter tranche | `DEFERRED_WITH_REASON` |

Reason for deferral: architecture accounting is required now, but CLI/MCP
runtime implementation is not authorized by this roadmap.

## Tranche Sequence

### ASSF-T0 - Skill Surface, Owner, And Legacy Absorption Audit

Enumerate CVF Web templates, governance skill specs/registries, Toolkit and
Guard Contract registries, rollout/intake/certification surfaces, archived
skill roadmaps, external-skill analyses, and unabsorbed legacy. Produce an
owner map, contradiction ledger, and proposed canonical root. No migration.

### ASSF-T1 - Canonical Package Contract And Storage Topology

Define the system `SKILL.md` profile, compact machine source schema, identity,
authority/risk/lifecycle fields, package layout, dual-agent matrix, and
provider-adapter boundary. Reconcile existing CVF Skill Spec instead of
creating a competing definition.

### ASSF-T2 - Generated Index And Progressive Resolver

Create compact registry sources, deterministic generator, drift check, and a
resolver that returns bounded package metadata from task/role/phase/surface/
risk selectors before loading package instructions or references.

### ASSF-T3 - Learning And ADIF Promotion Bridge

Map repeated, accepted learning evidence into skill candidates. Require
dedupe, source authority, evidence threshold, reviewer decision, UAT, and
explicit rejection/session-local outcomes. No self-activation.

### ASSF-T4 - External And Legacy Intake Normalization

Unify external skill screening and legacy absorption into the package-candidate
contract. Preserve provenance/license/security and reject provider-local or
legacy claims that cannot be reverified against CVF-governed sources.

### ASSF-T5 - Composition, Dependency, Conflict, And Capability Controls

Define deterministic composition order, incompatibility handling, authority
ceiling, side-effect budget, tool/CLI/MCP capability boundaries, rollback, and
failure reporting. Loading a skill must never grant new authority.

### ASSF-T6 - CVF Web Projection And Existing Example Migration

Project certified packages into CVF Web while preserving plain-language forms.
Classify each existing example as certified package projection, candidate,
legacy/reference-only, duplicate, or rejected. Do not use visibility as proof
of quality.

### ASSF-T7 - Certification, UAT, Drift, Deprecation, And Retirement Guard

Check package/index consistency, dangling sources, invalid selectors, dishonest
enforcement or adapter claims, duplicate IDs, stale successors, missing UAT,
and lifecycle violations. Integrate gates only after stable repeated use.

## Non-Goals

- one monolithic skill prompt loaded for every task;
- replacing standards, source, work orders, checkers, or reviewer judgment;
- converting every ADIF finding into a skill;
- treating external/provider packages as CVF authority;
- rewriting all existing end-user templates immediately;
- autonomous skill activation, self-modification, or authority escalation;
- claiming that package discovery proves reading, comprehension, or compliance.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| CVF has a canonical skill definition surface | `governance/skill-library/specs/CVF_SKILL_SPEC.md` | skill identity, structure, classification | `CVF Skill` | skill spec | EXISTS | ACCEPT |
| Skill rollout policy names the registry as source of truth | `governance/toolkit/05_OPERATION/CVF_SKILL_ROLLOUT_POLICY.md` | cross-extension rollout | `governance/skill-library/registry/` | rollout policy | LITERAL_INVARIANT | ACCEPT |
| Current concept page describes form-based `.skill.md` templates and CVF Web projection | `docs/concepts/skill-system.md` | What is a Skill; Skill Library in Web UI | `.skill.md` | current product skill concept | EXISTS | ACCEPT |
| Legacy/template corpus already requires rescreening | `docs/roadmaps/CVF_TEMPLATE_SKILL_CORPUS_RESCREEN_ROADMAP_2026-04-14.md` | context; classification protocol | `LEGACY_LOW_CONFIDENCE` | template/skill rescreen roadmap | VALUE_SET | ACCEPT |
| External skill package patterns were partially screened | `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md` | package model and runtime boundary rows | `ACCEPT_AS_PATTERN`; `DEFER_RUNTIME_GATED` | archived external skill screening | VALUE_SET | ACCEPT |
| Prior skill evolution work explicitly excluded external execution and self-modification | `docs/roadmaps/archive/CVF_SKILL_EVOLUTION_LOOP_RUNTIME_ADOPTION_ROADMAP_2026-05-16.md` | Scope Boundary | `external skill execution` | archived skill evolution roadmap | LITERAL_INVARIANT | ACCEPT |
| Generated aggregates require compact sources and generator discipline | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | generated source layout discipline | `generated source layout` | generated aggregate standard | RUNTIME_BEHAVIOR | ACCEPT |
| Dual consumer accounting is mandatory | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | `INTERNAL_AGENT`; `EXTERNAL_AGENT_CLI_MCP` | dual-agent surface standard | VALUE_SET | ACCEPT |

## Acceptance Criteria

- canonical ownership is reconciled before schema or migration;
- packages are independently versioned and progressively loadable;
- generated index metadata cannot replace canonical package/source authority;
- all three intake lanes converge through one candidate lifecycle;
- existing Web examples receive explicit migration dispositions;
- internal and external CLI/MCP consumers are both accounted for;
- loading/composition cannot widen action authority;
- no skill becomes `ACTIVE` without review and UAT evidence.

## Fail Conditions

Stop if a tranche creates another isolated registry, treats Web examples as
certified packages, bulk-imports legacy/external skills without rescreening,
loads the full library for every task, auto-activates learning output, conflates
provider adapters with canonical packages, or implements CLI/MCP/runtime
behavior without fresh authority.

## Work Plan

| Step | Owner role | Status |
|---|---|---|
| Record architecture roadmap and dual-agent rule | Codex roadmap author | PASS |
| Complete current ADIF continuous lane and Codex review | Claude worker; Codex reviewer/closer | IN_PROGRESS |
| Select and dispatch ASSF-T0 | operator checkpoint after ADIF or explicit isolated authorization | PARKED |
| Implement ASSF-T1/T2 early foundation | future source-verified tranches | PARKED |
| Connect learning/external/legacy lanes | future T3/T4 tranches | PARKED |

## Finding-To-Governance Learning Disposition

- Defect class: `RULE_GAP`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `DESIGN_REVIEW_REQUIRED`
- Next control action: ASSF-T0 owner and legacy absorption audit after ADIF.
- Runtime/provider/cost learning lane: `N/A_WITH_REASON` - roadmap-only.

## Verification / Evidence

Roadmap verification uses direct reads of the named skill spec, rollout policy,
current skill concept, legacy rescreen roadmap, external screening matrix,
archived evolution roadmap, generated aggregate discipline, and dual-agent
standard. ASSF-T0 must replace this bounded orientation set with a complete
filesystem-backed skill-surface inventory and reconciliation ledger.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | screened external skill -> ASSF-T4 normalization candidate -> CVF-owned package review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | future ASSF-T4 intake normalization contract |
| Disposition | ADAPT architecture patterns only; no external skill activation |
| Claim boundary | external skills remain reference input until source, provenance, license, risk, UAT, and authority review pass |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance architecture roadmap. Public skill architecture or
catalog changes require a later public-safe artifact and public-sync batch.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | Agent System Skills architecture roadmap |
| claimDisposition | N/A with reason: roadmap only |
| receiptEvidence | N/A with reason: no runtime receipt |
| actionEvidence | N/A with reason: no package/index/resolver implementation |
| invocationBoundary | governed roadmap authoring only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | proposed canonical package/index/progressive-loading foundation |
| forbiddenExpansion | no skill activation, runtime execution, CLI/MCP implementation, provider/live, public-sync, or readiness claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex roadmap author |
| Provider or surface | local workspace |
| Session or invocation | Agent System Skills roadmap, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, governance gates, git commit |
| Target paths | this roadmap and Dual Agent Surface Accounting Standard |
| Allowed scope source | operator instruction to record the architecture rule and roadmap while preserving ADIF focus |
| Before status evidence | clean HEAD `7c0480bc`; Claude ADIF-T0 checkpoint committed |
| After status evidence | two documentation-only architecture artifacts |
| Diff evidence | real-range name-status and gate output |
| Approval boundary | roadmap/standard authoring only; ASSF execution parked |
| Claim boundary | no ADIF edits, skill package/index/runtime, CLI/MCP implementation, or public-sync |
| Agent type | roadmap author |
| Invocation ID | `cvf-agent-system-skills-foundation-roadmap-2026-06-23` |
| Expected manifest | this roadmap; Dual Agent Surface Accounting Standard |
| Actual changed set | this roadmap; Dual Agent Surface Accounting Standard |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This roadmap records the architecture and sequencing decision only. It does not
create a canonical package root, `SKILL.md`, source schema, registry, generated
index, resolver, Learning Plane bridge, external intake adapter, Web migration,
guard, or runtime CLI/MCP surface.
