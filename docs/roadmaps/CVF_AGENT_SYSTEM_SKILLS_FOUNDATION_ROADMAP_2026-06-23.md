# CVF Agent System Skills Foundation Roadmap

Memory class: FULL_RECORD

Status: ASSF_T5_CLOSED_PASS_BOUNDED

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

ADIF is closed bounded. ASSF-T0 is closed bounded as an owner/surface/legacy
absorption audit. The operator identified that the currently opened legacy
folders are only seed examples, not the complete skill-related legacy corpus.
ASSF-T0.1 legacy skill corpus rescan is closed bounded. It produced the
filesystem-backed absorption candidate ledger required before ASSF-T1 could
freeze any package schema or storage topology. ASSF-T1 through ASSF-T5 are now
closed bounded; ASSF-T6 remains parked pending fresh operator selection,
GC-018, Source Verification, roadmap trace, Dual Agent Surface Matrix, and
work order.

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
storage or schema. ASSF-T0.1 must run a filesystem-backed legacy skill rescan
and produce an absorption candidate ledger before ASSF-T1 dispatch. No later
tranche may dispatch from proposed paths or fields as if they already exist.
Every child requires fresh GC-018, Source Verification, roadmap trace, Dual
Agent Surface Matrix, and dependency-release evidence.

## Mandatory Legacy Skill Rescan Gate

ASSF-T0.1 is a required precondition for ASSF-T1. It must scan the legacy tree
for skill-related knowledge rather than relying on currently opened files,
remembered folder names, or a small seed list.

Seed paths that must be included, but are not complete corpus coverage:

- `.private_reference/legacy/CVF_Important/ADK SkillToolset/`
- `.private_reference/legacy/CVF_Important/Windows_Skill_Normalization/`
- `.private_reference/legacy/CVF_Important/ADDING_CVF_Skill Formation Layer/`
- `.private_reference/legacy/CVF 16.5/Memento-Skills/`

Required T0.1 output:

- filesystem-backed enumeration command and manifest for legacy skill-relevant
  candidate files;
- absorption candidate ledger with at least these dispositions:
  `ABSORB_AS_CONTRACT_INPUT`, `ABSORB_AS_LIFECYCLE_INPUT`,
  `ABSORB_AS_PACKAGE_PATTERN`, `ABSORB_AS_TOOL_ADAPTER_INPUT`,
  `REFERENCE_ONLY`, `DUPLICATE`, `REJECT_DIRECT`, and
  `BLOCKED_UNVERIFIED_SOURCE`;
- source-fidelity notes for any already well-formed CVF-format legacy packets;
- explicit statement that no legacy file becomes canonical authority until
  re-expressed in a CVF-owned forward artifact;
- no migration, package creation, runtime adapter, public-sync, activation, or
  generated index work.

## Negative Search And Collision Discipline

ASSF-T0.1 must record negative-search and collision evidence before declaring a
legacy skill candidate source-absent or unverified. Required future search
roots are `.private_reference/legacy/`, `governance/skill-library/`,
`docs/roadmaps/`, `docs/reference/`, and `EXTENSIONS/`. Required future query
terms include skill, package, toolset, formation, lifecycle, normalization,
memento, adapter, MCP, CLI, ADK, and governed evolution. Exact future command
examples include `rg -n --hidden --no-ignore -i "skill|package|toolset|formation|lifecycle|normalization|memento|adapter|mcp|cli|adk|governed evolution" .private_reference/legacy`
and `rg --files --hidden --no-ignore .private_reference/legacy`. Absence in
the operator's currently opened folders is not negative evidence. Collision or
duplicate findings must be recorded in the absorption ledger rather than
silently dropped.

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

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | future system-skill resolver and package loader; proposed root `docs/reference/agent_system_skills/` | governed task/role/phase/risk selection; no authority expansion from loading | T0 audit; T1/T2 contract and tests still required | N/A with reason: no adapter implemented by roadmap/T0 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP skill discovery/load adapter | adapter contract, authentication/approval/receipt and mutation boundary required | separate source-verified adapter tranche | deferred adapter owner; requires separate GC-018/work order | `DEFERRED_WITH_REASON` |

Reason for deferral: architecture accounting is required now, but CLI/MCP
runtime implementation is not authorized by this roadmap.

## Tranche Sequence

### ASSF-T0 - Skill Surface, Owner, And Legacy Absorption Audit

Enumerate CVF Web templates, governance skill specs/registries, Toolkit and
Guard Contract registries, rollout/intake/certification surfaces, archived
skill roadmaps, external-skill analyses, and unabsorbed legacy. Produce an
owner map, contradiction ledger, and proposed canonical root. No migration.

Status: `CLOSED_PASS_BOUNDED`.

Closure artifacts:

- `docs/baselines/CVF_GC018_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md`
- `docs/audits/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md`
- `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md`

T0 proposed canonical root for future T1/T2 work:
`docs/reference/agent_system_skills/`. The path is proposed only and is not
created by T0.

### ASSF-T0.1 - Legacy Skill Corpus Rescan And Absorption Candidate Ledger

Scan `.private_reference/legacy/` for skill-related material, including but not
limited to ADK SkillToolset, Windows Skill Normalization, ADDING CVF Skill
Formation Layer, and Memento-Skills. Classify candidate files and folders into
an absorption ledger before ASSF-T1 schema work starts.

Status: `CLOSED_PASS_BOUNDED`.

Dispatch artifacts:

- `docs/baselines/CVF_GC018_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_2026-06-23.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_FOR_WORKER_2026-06-23.md`
- `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`
- `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_WORKER_RETURN_2026-06-23.md`
- `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_COMPLETION_2026-06-23.md`

Closure result: worker respected `WORKER_MUST_NOT_COMMIT`; Codex reviewer
accepted the worker return after independent count verification and gates. The
rescan enumerated 629 legacy files, found 4855 keyword hits across 422 files,
and classified the highest-signal candidates in a 24-row absorption ledger.

ASSF-T0.1 is not authorized to migrate files, create packages, create the
canonical root, generate an index, implement resolvers, activate skills, expose
CLI/MCP adapters, or claim runtime/provider/live/public behavior.

### ASSF-T1 - Canonical Package Contract And Storage Topology

Define the system `SKILL.md` profile, compact machine source schema, identity,
authority/risk/lifecycle fields, package layout, dual-agent matrix, and
provider-adapter boundary. Reconcile existing CVF Skill Spec and the ASSF-T0.1
legacy absorption ledger instead of creating a competing definition.

Status: `CLOSED_PASS_BOUNDED`.

Closure artifacts:

- `docs/reference/agent_system_skills/README.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_WORKER_RETURN_2026-06-23.md`
- `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_COMPLETION_2026-06-23.md`

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

Status: `CLOSED_PASS_BOUNDED`.

Closure artifacts:

- `docs/baselines/CVF_GC018_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_2026-06-25.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_FOR_WORKER_2026-06-25.md`
- `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md`
- `docs/reviews/CVF_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_WORKER_RETURN_2026-06-25.md`
- `docs/reviews/CVF_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_COMPLETION_2026-06-25.md`

T5 is contract-definition-only. No composition engine, loader, resolver change,
conflict checker, package instance, SKILL.md, skill.source.json, registry entry,
normalizer, promoter, CLI/MCP adapter, runtime/provider/live/public behavior,
activation, readiness, or automatic-promotion behavior is released.

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
- rewriting all existing end-user or legacy skill materials immediately;
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
skips ASSF-T0.1 before T1 schema freeze, loads the full library for every task,
auto-activates learning output, conflates provider adapters with canonical
packages, or implements CLI/MCP/runtime behavior without fresh authority.

## Work Plan

| Step | Owner role | Status |
|---|---|---|
| Record architecture roadmap and dual-agent rule | Codex roadmap author | PASS |
| Complete current ADIF continuous lane and Codex review | Claude worker; Codex reviewer/closer | IN_PROGRESS |
| Select and dispatch ASSF-T0 | operator checkpoint after ADIF or explicit isolated authorization | PASS |
| Select and dispatch ASSF-T0.1 legacy skill corpus rescan | operator checkpoint after T0 | PASS |
| Close ASSF-T0.1 worker-return rescan | Codex reviewer/closer | CLOSED_PASS_BOUNDED |
| Close ASSF-T1 canonical package contract | Codex reviewer/closer | CLOSED_PASS_BOUNDED |
| Implement ASSF-T2 generated index/resolver foundation | Codex worker; Claude reviewer/closer | CLOSED_PASS_BOUNDED |
| Define ASSF-T3 learning and ADIF promotion bridge contract | Codex worker; Claude reviewer/closer | CLOSED_PASS_BOUNDED |
| Define ASSF-T4 external and legacy intake normalization contract | Codex worker; Claude reviewer/closer | CLOSED_PASS_BOUNDED |
| Define ASSF-T5 composition/dependency/conflict/capability controls | dispatcher/worker/reviewer combined role | CLOSED_PASS_BOUNDED |

## Finding-To-Governance Learning Disposition

- Defect class: `RULE_GAP`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `DESIGN_REVIEW_REQUIRED`
- Next control action: ASSF-T5 Composition, Dependency, Conflict, And
  Capability Controls is closed. Operator may select ASSF-T6 (CVF Web
  Projection And Existing Example Migration), GFS-PY T2, or another governed
  lane through fresh source-verified dispatch. Any future normalizer
  implementation must cite the
  ASSF-T4 normalization contract
  (`docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md`)
  as authority and must resolve the two contract-introduced fields
  (`security_notes`, `sourceRevision`) against ASSF-T1 (add to T1 schema or
  remap `security_notes` onto T1 `sideEffects`) before an executable normalizer
  is built. Any future promoter implementation must still cite the ASSF-T3
  bridge contract
  (`docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md`)
  as authority. Any future ASSF-T6 packet must cite the ASSF-T1 package
  contract, the ASSF-T2 generated index/resolver foundation, and the ASSF-T5
  composition control contract rather than re-deriving schema, resolution, or
  composition logic from scratch. The ASSF-T4 completion review
  (`docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md`,
  Finding-To-Governance Learning Disposition) escalated this defect pattern
  to `MACHINE_CHECK_CANDIDATE`: two consecutive tranches (T3, T4) returned a
  worker-stated source-equivalence claim ("verbatim", "no new field") that
  was wrong and was caught only by manual reviewer re-derivation. A future
  governed lane should evaluate a worker-return/completion-review linter that
  requires a literal grep/diff command-and-result pair beside any equivalence
  claim about a named source file. The T5 tranche applied the evidence discipline
  (section-and-field verification for every reuse claim in the ASSF-T1 Schema
  Alignment Decision table) as a first practice of this pattern. The machine-check
  candidate escalation carries forward to ASSF-T7 or a future checker tranche.
  T5 also defined four new schema extension fields (`extends`, `replaces`,
  `capabilityClaims`, `compositionFailureDisposition`) as `PROPOSE_SCHEMA_EXTENSION`;
  a separate ASSF-T1 schema amendment work order is required before implementation.
- Runtime/provider/cost learning lane: `N/A_WITH_REASON` - roadmap-only.

## Verification / Evidence

Roadmap verification uses direct reads of the named skill spec, rollout policy,
current skill concept, legacy rescreen roadmap, external screening matrix,
archived evolution roadmap, generated aggregate discipline, and dual-agent
standard. ASSF-T0 replaced the bounded orientation set with a filesystem-backed
skill-surface owner inventory and reconciliation ledger. The operator
identified additional skill-relevant legacy seed folders, including ADK
SkillToolset, Windows Skill Normalization, ADDING CVF Skill Formation Layer,
and Memento-Skills. T0.1 has now scanned the broader legacy skill corpus and
produced the candidate ledger that T1 must consume.

## Corpus Completeness And Report Integrity

- Corpus task class: ROADMAP_CLOSURE_UPDATE.
- Corpus root: this roadmap; closed ASSF-T0.1 scan root `.private_reference/legacy/`.
- Snapshot time: 2026-06-23.
- Enumeration command: worker and reviewer verified `rg --files --hidden --no-ignore .private_reference/legacy` -> 629 files, plus the required keyword search -> 4855 hits across 422 files.
- Manifest artifact or inline manifest: T0.1 audit Legacy Manifest Summary and worker-return Corpus Completeness section.
- Manifest hash: N/A with reason: text inline manifest summary; no generated manifest artifact.
- Processing ledger artifact or inline ledger: `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` Absorption Candidate Ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=629; keyword_hits=4855 across 422 files; ledger_terminal=24 ledger rows; exclusions=full line-by-line direct reads of all 422 matched files, migration, package creation, runtime/provider/public/CLI/MCP adapter; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: actual legacy scan, per-file absorption ledger, source hashes, migration, package creation, generated index, resolver, runtime/provider/live/public behavior, and CLI/MCP adapter.
- Unreadable or unsupported files: 0 for this roadmap edit.
- Aggregation check: N/A with reason: no generated aggregate created by this roadmap edit.
- Drift check: N/A with reason: no generated aggregate created by this roadmap edit.
- Output traceability: ASSF-T0.1 closure is recorded in Authorization / Decision, Design Control Gate, Mandatory Legacy Skill Rescan Gate, Tranche Sequence, Work Plan, and Machine Closure Package.
- Adversarial verification: the roadmap explicitly rejects treating operator open tabs or T0 owner counts as full legacy skill corpus coverage.
- Corpus verdict: PARTIAL

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

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | this roadmap | `Status: ASSF_T5_CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T5 GC-018 status | `docs/baselines/CVF_GC018_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T5 work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_FOR_WORKER_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T5 composition control contract | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | `Status: CANDIDATE` reference contract | PASS |
| ASSF-T5 worker return | `docs/reviews/CVF_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_WORKER_RETURN_2026-06-25.md` | `Status: WORKER_RETURN_COMPLETE` | PASS |
| ASSF-T5 completion review | `docs/reviews/CVF_ASSF_T5_COMPOSITION_DEPENDENCY_CONFLICT_CAPABILITY_CONTROLS_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T4 GC-018 status | `docs/baselines/CVF_GC018_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T4 work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_FOR_WORKER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T4 normalization contract | `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md` | `Status: CANDIDATE` reference contract | PASS |
| ASSF-T4 worker return | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_WORKER_RETURN_2026-06-23.md` | `Status: COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, accepted after reviewer repair | PASS |
| ASSF-T4 completion review | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T3 GC-018 status | `docs/baselines/CVF_GC018_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T3 work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_FOR_WORKER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T3 bridge contract | `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md` | `Status: CANDIDATE` reference contract | PASS |
| ASSF-T3 worker return | `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_WORKER_RETURN_2026-06-23.md` | accepted after reviewer handoff repair | PASS |
| ASSF-T3 completion review | `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md` | reviewer-owned closure review | PASS |
| ASSF-T0.1 GC-018 status | `docs/baselines/CVF_GC018_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T0.1 work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_FOR_WORKER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T0.1 worker return | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_WORKER_RETURN_2026-06-23.md` | `Status: ACCEPTED_BY_REVIEWER` | PASS |
| ASSF-T0.1 audit ledger | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T0.1 completion review | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T1 GC-018 status | `docs/baselines/CVF_GC018_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T1 work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_FOR_WORKER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T1 package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | `Status: ACTIVE_REFERENCE` | PASS |
| ASSF-T1 reference README | `docs/reference/agent_system_skills/README.md` | `Status: ACTIVE_REFERENCE` | PASS |
| ASSF-T1 worker return | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_WORKER_RETURN_2026-06-23.md` | `Status: ACCEPTED_BY_REVIEWER` | PASS |
| ASSF-T1 completion review | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T2 GC-018 status | `docs/baselines/CVF_GC018_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T2 work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_FOR_WORKER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| ASSF-T2 registry README | `docs/reference/agent_system_skills/registry/README.md` | `Status: ACTIVE_REFERENCE` | PASS |
| ASSF-T2 generated index README | `docs/reference/agent_system_skills/generated/README.md` | `Status: ACTIVE_REFERENCE` | PASS |
| ASSF-T2 generated skill index | `docs/reference/agent_system_skills/generated/skill-index.json` | drift-checked, in sync with sources | PASS |
| ASSF-T2 worker return | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_WORKER_RETURN_2026-06-23.md` | `Status: COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, accepted after reviewer repair | PASS |
| ASSF-T2 completion review | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T0 is not authorized to update GC-051 registry surfaces and no generated skill index is created | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T0 is not authorized to update GC-051 registry surfaces and no generated skill index is created | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported; external skill screening remains reference input | N/A with reason |
| System loop interlock | this roadmap | T1->T2->T3->T4->T5 are closed in order and consumed; T5 is required before T6; no automatic package activation | PASS |
| Session continuity | active session sync if next move changes | separate session-sync lane after material commit | PASS |
| Public export | this roadmap | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Roadmap status | `ASSF_T5_CLOSED_PASS_BOUNDED` | `ASSF_T5_CLOSED_PASS_BOUNDED` | PASS |
| T0 closure artifacts | baseline, work order, audit, completion review | all named in T0 closure artifacts | PASS |
| T0.1 closure artifacts | GC-018, work order, audit, worker return, completion review | all named in ASSF-T0.1 tranche section | PASS |
| Package root | proposed only | proposed only | PASS |
| External CLI/MCP adapter | deferred | `DEFERRED_WITH_REASON` | PASS |
| Runtime/provider/live claim | none | none | PASS |
| T5 composition control contract | CLOSED_PASS_BOUNDED | all T5 artifacts present; schema alignment decision table present | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | Agent System Skills architecture roadmap through ASSF-T5 closure update |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- T5 composition control contract closed as CLOSED_PASS_BOUNDED |
| receiptEvidence | N/A with reason: no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- T5 GC-018, work order, composition control contract, worker return, completion review, and gate evidence |
| invocationBoundary | governed roadmap and dispatch authoring only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | proposed canonical package/index/progressive-loading foundation |
| forbiddenExpansion | no skill activation, runtime execution, CLI/MCP implementation, provider/live, public-sync, or readiness claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | combined ASSF-T5 dispatcher/worker/reviewer with Codex reviewer repair |
| Provider or surface | local workspace |
| Session or invocation | Agent System Skills roadmap ASSF-T5 closure update, 2026-06-25 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, governance gates, git commit |
| Target paths | this roadmap; ASSF-T5 baseline; ASSF-T5 work order; T5 composition control contract; worker return; completion review |
| Allowed scope source | operator instruction to execute ASSF-T5; active session next move |
| Before status evidence | clean HEAD `cb063785`; ASSF-T5 dispatch ready |
| After status evidence | ASSF-T5 closed bounded; ASSF-T6 pending operator selection |
| Diff evidence | real-range name-status and gate output |
| Approval boundary | ASSF-T5 documentation/reference contract only |
| Claim boundary | T5 composition control contract only; no composition engine, loader, conflict checker, resolver change, package instance, registry entry, runtime, CLI/MCP implementation, or public-sync |
| Agent type | roadmap author and T0 closer |
| Invocation ID | `cvf-agent-system-skills-foundation-t5-closure-2026-06-25` |
| Expected manifest | this roadmap; ASSF-T5 baseline; ASSF-T5 work order; T5 composition control contract; worker return; completion review |
| Actual changed set | this roadmap; ASSF-T5 baseline; ASSF-T5 work order; T5 composition control contract; worker return; completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This roadmap now records the architecture sequence, the closed bounded ASSF-T0
through ASSF-T5 tranches. ASSF-T5 is a contract-definition-only closure; it does
not create a composition engine, loader, conflict checker, resolver change,
generator change, drift checker, test code, package instance, SKILL.md,
skill.source.json, registry entry, normalizer, promoter, CLI/MCP adapter,
migration, runtime/provider/live/public behavior, activation, readiness, or
automatic-promotion behavior. ASSF-T6 (CVF Web Projection) is the next tranche
and requires fresh operator selection, GC-018, and source-verified work order.
