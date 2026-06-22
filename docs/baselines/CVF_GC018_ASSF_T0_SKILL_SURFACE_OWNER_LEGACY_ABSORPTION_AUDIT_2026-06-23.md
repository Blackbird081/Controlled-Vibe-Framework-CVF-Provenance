# CVF GC-018 - ASSF-T0 Skill Surface Owner And Legacy Absorption Audit

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: gc018_baseline

dispatchBaseHead: 87e2013a

executionBaseHead: 87e2013a

closureBaseHead: 87e2013a

Commit mode: `WORKER_MAY_COMMIT`

Batch ID: ASSF-T0

## Purpose

Authorize ASSF-T0 as a documentation and audit-only foundation tranche for the
Agent System Skills Foundation roadmap. The tranche inventories the main
repo-local skill owner surfaces, reconciles conflicting definitions and
lifecycle vocabularies, records a contradiction ledger, and proposes one
canonical package root for future T1/T2 work.

ASSF-T0 does not create a package root, schema, generated index, resolver,
runtime loader, CLI/MCP adapter, public export, or skill activation.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-23 chat instruction to continue the package-skills roadmap | ACCEPT |
| Active state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT - next move permits ASSF-T0 or another governed lane |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT - ADIF closed; ASSF may be selected |
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ACCEPT |
| Dual Agent Surface Accounting Standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | ACCEPT |
| Guard Orientation | `docs/reference/guard_orientation/README.md` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| CVF has a canonical skill specification surface | `governance/skill-library/specs/CVF_SKILL_SPEC.md` | Required Sections; Skill Classification | `CVF Skill` | skill specification | EXISTS | ACCEPT |
| Skill rollout policy names the registry as source of truth | `governance/toolkit/05_OPERATION/CVF_SKILL_ROLLOUT_POLICY.md` | Cross-Extension Rollout | `governance/skill-library/registry/` | rollout policy | LITERAL_INVARIANT | ACCEPT |
| Governance skill library is an active owner surface with specs, registry, UAT, and examples | `governance/skill-library/README.md` | File Structure; Workflow; Quick Links | `governance/skill-library/` | skill governance library | EXISTS | ACCEPT |
| End-user skill library is a user-facing skill corpus, not the system-package authority by itself | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | Portfolio Note; Statistics; Automated Validation | `.skill.md` | end-user skill library | EXISTS | ACCEPT |
| Current concept page defines skills as form-based templates and CVF Web projection | `docs/concepts/skill-system.md` | What is a Skill; Skill Library in Web UI | `.skill.md` | product skill concept | EXISTS | ACCEPT |
| Toolkit mapping defines a different executable skill contract and lifecycle vocabulary | `EXTENSIONS/CVF_TOOLKIT_REFERENCE/01_CORE_MAPPING/skill.schema.mapping.md` | Toolkit Canonical Skill Contract; Skill Lifecycle | `skillId`; `status` | Toolkit skill schema mapping | VALUE_SET | ACCEPT |
| v3.0 lifecycle code defines another lifecycle vocabulary and activation preconditions | `EXTENSIONS/CVF_v3.0_CORE_GIT_FOR_AI/skill_lifecycle/skill.lifecycle.ts` | `SkillLifecycleState`; `activateSkill` | `PROPOSED`; `VERIFIED`; `ACTIVE`; `DEPRECATED`; `REVOKED` | v3 skill lifecycle registry | VALUE_SET | ACCEPT |
| External skill screening accepts patterns but defers direct import/runtime | `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md` | Accepted Pattern Set; Deferred Or Rejected Value | `ACCEPT_AS_PATTERN`; `DEFER_RUNTIME_GATED` | external skill screening matrix | VALUE_SET | ACCEPT |
| Prior skill evolution roadmap excludes self-modifying skills | `docs/roadmaps/archive/CVF_SKILL_EVOLUTION_LOOP_RUNTIME_ADOPTION_ROADMAP_2026-05-16.md` | Non-Goals; Claim Boundary | `autonomous production skill rewrite`; `self-modifying skills` | skill evolution roadmap | LITERAL_INVARIANT | ACCEPT |
| Generated aggregate discipline requires compact sources and generator for future large indexes | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | Rule; Closure Requirement | `generated source layout` | generated aggregate standard | RUNTIME_BEHAVIOR | ACCEPT |

## Scope / Owner Boundary

Allowed scope:

- create the ASSF-T0 audit artifact under `docs/audits/`;
- create this GC-018 baseline and the paired work order;
- create the ASSF-T0 completion review;
- update the ASSF roadmap status, T0 row, matrix shape, and operation trace;
- record a proposed canonical package root for future work.

Forbidden scope:

- no package root creation;
- no schema, `SKILL.md`, registry source, generated index, resolver, loader, or
  checker implementation;
- no migration or edit of existing skill corpus files;
- no runtime, provider/live, external CLI/MCP adapter, public-sync, or skill
  activation claim;
- no automatic promotion of learning, legacy, or external skills.

Risk ceiling: R1 - documentation/audit-only governance work.

## Required Deliverables

| Artifact | Path | Required |
|---|---|---|
| GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | YES |
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | YES |
| Audit output | `docs/audits/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | YES |
| Completion review | `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md` | YES |
| Roadmap update | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | YES |

## Decision / Baseline / Proposed Tranche

Decision: close ASSF-T0 as `CLOSED_PASS_BOUNDED` after a documentation-only
owner/surface audit.

Baseline: current repo-local skill ownership is distributed across governance
specification, registry/UAT, rollout policy, end-user `.skill.md` corpus,
product concept, Toolkit schema, v3 lifecycle source, external-skill screening,
and archived roadmap surfaces.

Proposed tranche outcome: ASSF-T1 may define the canonical package contract and
storage topology only after fresh dispatch. T0 proposes
`docs/reference/agent_system_skills/` as the future root, but does not create
it.

## Evidence / Verification

Evidence is limited to direct source reads, bounded filesystem inventory
commands, the T0 audit output, roadmap update, closure review, and governance
gate output. No runtime/provider/live evidence, public-sync evidence, package
activation evidence, or external CLI/MCP adapter evidence is claimed.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order/output handling | Evidence | Status |
|---|---|---|---|
| Reconcile owners before T1 freezes schema | audit owner map and contradiction ledger | `docs/audits/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | PASS |
| Inventory current, legacy, external, and Web skill surfaces | bounded filesystem-backed inventory | audit Evidence Snapshot and Surface Owner Map | PASS |
| Produce proposed canonical root | audit Proposed Canonical Root Decision | `docs/reference/agent_system_skills/` proposed only | PASS |
| No migration or runtime implementation | forbidden scope and closure review | completion Claim Boundary | PASS |
| Account for internal and external agents | six-column Dual Agent Surface Matrix | this baseline, work order, audit, completion review | PASS |

## Mandatory Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | future ASSF package contract and resolver, proposed under `docs/reference/agent_system_skills/` | T0 is audit-only; no loading, activation, action, commit, or runtime authority is granted | this baseline and T0 audit | N/A with reason: no adapter implemented in T0 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future separately authorized CLI/MCP discovery/load adapter | no ingress, authentication, approval, receipt, raw-data release, mutation, runtime, public, or readiness claim exists in T0 | dual-surface standard and T0 forbidden scope | deferred adapter owner; requires separate GC-018/work order | `DEFERRED_WITH_REASON` |

## Corpus Completeness And Report Integrity

- Corpus task class: INVENTORY and AUDIT.
- Corpus root: bounded owner-surface roots named in the audit Evidence Snapshot.
- Snapshot time: 2026-06-23.
- Enumeration command: `rg --files --hidden --no-ignore governance/skill-library`;
  `rg --files --hidden --no-ignore EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS`;
  `rg --files --hidden --no-ignore EXTENSIONS | rg -i "skill|skills|SKILL"`.
- Manifest artifact or inline manifest: audit Evidence Snapshot and Surface
  Owner Map.
- Manifest hash: N/A with reason: T0 records bounded owner-surface counts, not
  a per-file migration manifest.
- Processing ledger artifact or inline ledger: audit Owner Surface Map and
  Contradiction Ledger.
- Output traceability: every owner-family conclusion maps to an audit row and
  a source-verified authority row above.
- Adversarial verification: count and lifecycle contradictions are recorded as
  contradictions, not silently reconciled.
- Allowed terminal statuses: READ, DEFERRED, SKIPPED_WITH_REASON,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=audit Evidence Snapshot and Surface Owner Map; ledger_terminal=READ or DEFERRED for all T0 rows; exclusions=full migration, runtime/provider/public-sync, generated registry mutation; unresolved=0.
- Declared exclusions: no file-level quality scoring, no full legacy source
  migration, no public-sync clone scan, no runtime source mutation.
- Unreadable or unsupported files: 0 for the bounded source files directly read.
- Unresolved files: 0.
- Aggregation check: N/A with reason: no generated aggregate created.
- Drift check: N/A with reason: no generated aggregate created.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | screened external skill -> ASSF-T4 normalization candidate -> CVF-owned package review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | future ASSF-T4 intake normalization contract |
| Disposition | T0 records pattern input only; no activation or direct import |
| Claim boundary | external skills remain candidate/reference input until provenance, license, risk, UAT, and authority review pass |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| Skill surfaces use incompatible definitions, counts, lifecycle states, and authority boundaries | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ASSF-T1 must define the canonical package contract without copying one legacy owner wholesale |
| Dual Agent Surface Matrix needs one forward batch to stabilize the six-column shape | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | T0 uses the six-column matrix in all new artifacts |
| Runtime/provider/cost behavior | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance audit. Public package-skill architecture requires a
later public-safe summary and public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T0 owner/legacy audit only |
| claimDisposition | N/A with reason: no runtime execution-control claim |
| receiptEvidence | N/A with reason: no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: documentation artifacts, inventory command evidence, committed diff, and gates only |
| invocationBoundary | local repository audit and governance authoring |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | audit and proposed root only |
| forbiddenExpansion | package creation, generated index, resolver, runtime/provider/live, CLI/MCP adapter, public-sync, readiness, and skill activation remain out of scope |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Owner map covers the main current, legacy, external, Web, Toolkit, and lifecycle skill surfaces | audit Owner Surface Map |
| AC2 | Contradiction ledger records incompatible definitions and lifecycle states | audit Contradiction Ledger |
| AC3 | Proposed canonical root is documented as proposed-only | audit Proposed Canonical Root Decision |
| AC4 | No existing skill corpus files are migrated or modified | committed diff |
| AC5 | Dual Agent Surface Matrix uses the six-column shape | all T0 artifacts |
| AC6 | Roadmap state records T0 closed bounded without closing the full roadmap | roadmap update |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T0_CLOSED_PASS_BOUNDED_PENDING_T1_SELECTION` | PASS |
| GC-018 status | this baseline | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md` | reviewer-owned closure review | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T0 is not authorized to update GC-051 registry surfaces and no generated skill index is created | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T0 is not authorized to update GC-051 registry surfaces and no generated skill index is created | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported; archived screening cited as source input only | N/A with reason |
| System loop interlock | ASSF roadmap | T1 remains parked; no automatic activation | PASS |
| Session continuity | session-sync commit after material closure if current mode/next move changes | session sync owned separately from material commit | PASS |
| Public export | this baseline | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim or changed path | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Baseline status | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| T0 scope | owner/surface audit only | owner/surface audit only | PASS |
| Proposed root | proposed only, not created | `docs/reference/agent_system_skills/` proposed only | PASS |
| External CLI/MCP adapter | deferred | `DEFERRED_WITH_REASON` | PASS |
| Runtime/provider/live claim | none | none | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher/worker/reviewer |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T0 governed audit, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, filesystem inventory commands, apply_patch, governance gates, git commit |
| Target paths | this baseline; paired work order; T0 audit; T0 completion review; ASSF roadmap |
| Allowed scope source | operator instruction to continue package-skills roadmap; ASSF roadmap; active session next move |
| Before status evidence | clean HEAD `87e2013a` |
| After status evidence | ASSF-T0 closed bounded in material commit |
| Diff evidence | committed name-status and pre-closure gate |
| Approval boundary | ASSF-T0 documentation/audit-only tranche |
| Claim boundary | no package/index/resolver/runtime/adapter/public behavior |
| Agent type | single-agent multi-role governed batch |
| Invocation ID | `assf-t0-skill-surface-owner-audit-2026-06-23` |
| Expected manifest | this baseline; paired work order; T0 audit; T0 completion review; ASSF roadmap |
| Actual changed set | this baseline; paired work order; T0 audit; T0 completion review; ASSF roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes and records only ASSF-T0 audit work. It does not
authorize ASSF-T1 schema freezing, package-root creation, generated index,
resolver, runtime loading, CLI/MCP adapter, public-sync, or skill activation.
