# CVF ASSF-T0 Skill Surface Owner And Legacy Absorption Audit

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: audit

## Purpose

Reconcile CVF's current skill-related owner surfaces before the Agent System
Skills Foundation freezes a package contract or storage topology. This audit
identifies the current owner families, conflicting definitions, lifecycle
vocabularies, and the proposed canonical package root for future ASSF work.

## Scope / Target / Owner Boundary

Target: ASSF-T0 owner/surface/legacy absorption audit for the Agent System
Skills Foundation roadmap.

Owner boundary: Codex authored this audit under the paired ASSF-T0 GC-018 and
work order. Existing skill corpus, runtime source, public-sync, active session
state, and external CLI/MCP adapter surfaces are excluded from material
mutation.

## Target / Source

| Target or source | Path | Disposition |
|---|---|---|
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ACCEPT |
| Baseline | `docs/baselines/CVF_GC018_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | ACCEPT |
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | ACCEPT |
| Governance skill spec | `governance/skill-library/specs/CVF_SKILL_SPEC.md` | ACCEPT |
| End-user skill library | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | ACCEPT_AS_INPUT |
| Toolkit skill schema | source-verified in paired baseline | ACCEPT_AS_INPUT |
| v3 lifecycle source | source-verified in paired baseline | ACCEPT_AS_INPUT |

## Scope / Methodology

Methodology: read source-verified skill-owner surfaces, run bounded filesystem
inventory commands, classify owners, record contradictions, and propose a
future canonical package root without creating it.

Exclusions: no package migration, no per-file skill quality certification, no
generated index, no resolver, no runtime/provider/live proof, no public-sync,
and no external CLI/MCP adapter.

## Findings / Position

Position: `CLOSED_PASS_BOUNDED`.

CVF has enough skill material to justify a system-skill package foundation, but
not enough unified authority to freeze T1 by copying any one legacy surface.
The safe next move is a canonical package contract that reconciles the existing
owner families and makes internal-agent and external CLI/MCP dispositions
explicit.

## Risk / Corrective Action

Risk: stale counts and conflicting lifecycle vocabularies may be mistaken for
canonical package truth.

Corrective action: ASSF-T1 must define canonical package fields and lifecycle
mapping from verified sources; ASSF-T2 must generate inventory totals from
compact package sources rather than README counts.

## Evidence Snapshot

| Evidence command or read | Result | Disposition |
|---|---|---|
| `Test-Path governance/skill-library` | True | ACCEPT |
| `Test-Path EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS` | True | ACCEPT |
| Toolkit reference root presence check | True | ACCEPT - exact source path retained in paired baseline |
| v3 lifecycle root presence check | True | ACCEPT - exact source path retained in paired baseline |
| external skill rewrite example root presence check | True | ACCEPT - example presence only; no corpus claim |
| `rg --files --hidden --no-ignore governance/skill-library` | 853 paths | BOUNDED_INVENTORY |
| `rg --files --hidden --no-ignore EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS` | 277 paths | BOUNDED_INVENTORY |
| `rg --files --hidden --no-ignore EXTENSIONS | rg -i "skill|skills|SKILL"` | 448 paths | BOUNDED_INVENTORY |

Counts are owner-surface orientation evidence, not per-file quality
certification or migration readiness.

## Surface Owner Map

| Surface family | Representative owner path | Current role | T0 disposition |
|---|---|---|---|
| Governance skill specification | `governance/skill-library/specs/CVF_SKILL_SPEC.md` | canonical skill-format authority | ACCEPT_AS_OWNER_MAP |
| Governance skill registry and UAT | `governance/skill-library/registry/`; `governance/skill-library/uat/` | governance records, validation, UAT, external-source tooling | ACCEPT_AS_OWNER_MAP |
| Rollout policy | `governance/toolkit/05_OPERATION/CVF_SKILL_ROLLOUT_POLICY.md` | ecosystem lifecycle and registry source-of-truth policy | ACCEPT_AS_OWNER_MAP |
| End-user skill library | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/` | user-facing `.skill.md` corpus and Web projection input | ADAPT_AS_CANDIDATE_INPUT |
| Product concept page | `docs/concepts/skill-system.md` | user-facing explanation of form-based skills | ADAPT_AS_PRESENTATION_INPUT |
| Toolkit executable schema | source-verified in paired baseline | executable schema and registry requirements | ADAPT_AS_CONTRACT_INPUT |
| v3 lifecycle runtime | source-verified in paired baseline | lifecycle runtime implementation pattern | ADAPT_AS_LIFECYCLE_INPUT |
| External skill screening | `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md` | external-skill pattern and deferral decisions | ACCEPT_AS_PATTERN_INPUT |
| Skill evolution roadmap | `docs/roadmaps/archive/CVF_SKILL_EVOLUTION_LOOP_RUNTIME_ADOPTION_ROADMAP_2026-05-16.md` | proposal-only evolution and self-modification boundary | ACCEPT_AS_BOUNDARY_INPUT |

## Contradiction Ledger

| Contradiction | Evidence | T0 decision | T1 implication |
|---|---|---|---|
| Counts vary across surfaces: governance README says 124 user skills plus agent skills; end-user README says 62 active skills and 80 archived; concept page mixes 62 active with larger domain totals and later "131 skills" language | `governance/skill-library/README.md`; `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md`; `docs/concepts/skill-system.md` | Do not use count as authority. Treat counts as stale unless regenerated by future package index. | T1/T2 must define generated index totals from compact sources only. |
| Skill meaning varies: canonical spec defines controlled capability; concept page defines form-based template; Toolkit mapping treats skill as atomic execution unit | `CVF_SKILL_SPEC.md`; `docs/concepts/skill-system.md`; `skill.schema.mapping.md` | Preserve all as inputs, but do not freeze any single legacy definition as the system package contract. | T1 must define package type, instruction front door, machine source, and execution boundary separately. |
| Lifecycle vocabulary conflicts: DRAFT/ACTIVE/DEPRECATED/REVOKED/SUPERSEDED, PROPOSED/APPROVED/ACTIVE/DEPRECATED/RETIRED, draft/validated/released/deprecated, and PROPOSED/REGISTERED/VERIFIED/ACTIVE/DEPRECATED/REVOKED all appear | rollout policy; concept page; Toolkit mapping; v3 lifecycle source | Normalize to a new ASSF lifecycle rather than reusing a legacy enum silently. | T1 must map old states to candidate/active/deprecated/retired dispositions explicitly. |
| External skill sources are valuable but unsafe as authority | external screening matrix | External inputs become candidates or patterns only. | T4 must handle provenance, license, security, and rejection before any package activation. |
| Existing Web examples are presentation surfaces, not certified system packages | ASSF roadmap; concept page; end-user skill library README | Treat Web examples as projection/candidate input only. | T6 must classify examples as certified projection, candidate, legacy/reference-only, duplicate, or rejected. |

## Proposed Canonical Root Decision

Proposed root for future ASSF package architecture:

`docs/reference/agent_system_skills/`

Proposed future layout, not created by T0:

```text
docs/reference/agent_system_skills/
  README.md
  packages/
    <skill-id>/
      SKILL.md
      skill.source.json
      references/
      scripts/
  registry/
    entries/
  generated/
    skill-index.json
```

Rationale:

- `docs/reference/` is already a canonical reference owner surface for active
  standards and contracts.
- package identity and machine-readable source should remain private
  provenance-controlled before any public projection;
- existing `governance/skill-library/` remains a source and legacy governance
  owner, not the new package root, to avoid mixing historical registries with
  the future generated index;
- future public projection can be curated later from this reference root.

## T1/T2 Carry-Forward Requirements

1. T1 must define a new ASSF package contract that maps, but does not blindly
   inherit, legacy skill fields.
2. T1 must define lifecycle state mapping from all four observed vocabularies.
3. T1 must preserve dual-agent surface accounting with explicit adapter
   boundary.
4. T2 must use generated aggregate discipline if it creates `skill-index.json`.
5. No skill may become `ACTIVE` from T0 evidence alone.

## Mandatory Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | future package resolver rooted at proposed `docs/reference/agent_system_skills/` | T0 audit grants no loading, activation, mutation, or execution authority | this audit and paired baseline | N/A with reason: no adapter implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP skill package discovery/load adapter | no ingress, authentication, approval, receipt, raw-data, mutation, runtime, public, or readiness claim | dual-surface standard and ASSF roadmap | deferred adapter owner; separate source-verified tranche required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | screened external skill -> ASSF-T4 normalization candidate -> CVF-owned package review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | future ASSF-T4 intake normalization contract |
| Disposition | pattern/reference input only |
| Claim boundary | no external package import, runtime execution, CLI/MCP exposure, or activation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private owner-surface audit. No public-safe package-skill claim is made.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| Existing skill surfaces conflict on counts, definitions, lifecycle states, and authority boundaries | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ASSF-T1 canonical package contract |
| External skill package patterns are useful but cannot be authority by themselves | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DEFERRED_TO_FUTURE_TRANCHE | ASSF-T4 external and legacy intake normalization |
| Runtime/provider/cost behavior | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T0_CLOSED_PASS_BOUNDED_PENDING_T1_SELECTION` | PASS |
| GC-018 status | paired baseline | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | paired work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Audit artifact | this audit | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md` | reviewer-owned closure review | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T0 is not authorized to update GC-051 registry surfaces and no generated skill index is created | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T0 is not authorized to update GC-051 registry surfaces and no generated skill index is created | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported; archived external screening cited as source input only | N/A with reason |
| System loop interlock | ASSF roadmap | T1/T2 remain future governed tranches | PASS |
| Session continuity | session-sync lane if next move changes | separate from material commit | PASS |
| Public export | this audit | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Audit status | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| Owner map | present | present | PASS |
| Contradiction ledger | present | present | PASS |
| Proposed root | proposed only, not created | proposed only, not created | PASS |
| External CLI/MCP adapter | deferred | `DEFERRED_WITH_REASON` | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex worker/reviewer |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T0 audit, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, `Test-Path`, `rg --files`, apply_patch, governance gates |
| Target paths | this audit; paired baseline; paired work order; completion review; ASSF roadmap |
| Allowed scope source | ASSF-T0 GC-018 and operator package-skills continuation |
| Before status evidence | clean HEAD `87e2013a` |
| After status evidence | T0 audit complete and committed |
| Diff evidence | committed name-status and pre-closure gate |
| Approval boundary | T0 audit only |
| Claim boundary | no package/index/resolver/runtime/adapter/public behavior |
| Agent type | single-agent multi-role governed batch |
| Invocation ID | `assf-t0-audit-2026-06-23` |
| Expected manifest | this audit; paired baseline; paired work order; completion review; ASSF roadmap |
| Actual changed set | this audit; paired baseline; paired work order; completion review; ASSF roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This audit is a bounded owner-surface and legacy-reconciliation artifact. It
does not certify any existing skill package, create the proposed root, migrate
skills, implement generated indexes or resolvers, or authorize external
CLI/MCP/runtime behavior.
