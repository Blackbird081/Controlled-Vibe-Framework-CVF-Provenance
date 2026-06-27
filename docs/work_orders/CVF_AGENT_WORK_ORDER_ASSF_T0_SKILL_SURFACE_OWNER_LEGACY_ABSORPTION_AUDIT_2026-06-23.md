# CVF Agent Work Order - ASSF-T0 Skill Surface Owner And Legacy Absorption Audit

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: work_order

Commit mode: `WORKER_MAY_COMMIT`

dispatchBaseHead: 87e2013a

executionBaseHead: 87e2013a

closureBaseHead: 87e2013a

## Dispatch Prompt Envelope

Role: single-agent dispatcher/worker/reviewer for a bounded ASSF-T0
documentation audit. Execute only the owner/surface/legacy absorption audit
authorized by the paired GC-018 baseline.

Canonical packet:
`docs/baselines/CVF_GC018_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md`

Do-not-misread notes: ASSF-T0 is not T1 schema work, not T2 generated-index
work, not a migration, and not an external CLI/MCP adapter. Existing skill
corpus files must remain untouched.

Return contract: commit a closed bounded documentation/audit batch if gates
pass; otherwise return `BLOCKED_WITH_REASON`.

## Purpose

Authorize and close a bounded ASSF-T0 owner/surface/legacy absorption audit for
the Agent System Skills Foundation roadmap. This work order is documentation
and governance artifact work only; it does not create a package root, runtime
resolver, generated index, CLI/MCP adapter, public export, or active skill.

## Mission

Produce the ASSF-T0 owner map, contradiction ledger, and proposed canonical
package root for the Agent System Skills Foundation roadmap.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-23 package-skills roadmap continuation | ACCEPT |
| Active state next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| ASSF roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ACCEPT |
| ASSF-T0 GC-018 | `docs/baselines/CVF_GC018_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | ACCEPT |
| Dual Agent Surface Accounting Standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | human principal selecting ASSF lane |
| Dispatcher | Codex |
| Worker | Codex |
| Reviewer/closer | Codex with explicit single-agent multi-role claim boundary |
| Session-sync steward | Codex after material commit if continuity changes |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles: Codex performs dispatch, implementation, review, closure, and commit stewardship for this small documentation tranche |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC if needed |
| baseHeadFor(phase) | `dispatchBaseHead=87e2013a`; `executionBaseHead=87e2013a`; `closureBaseHead=87e2013a` before material commit |
| changedSetScope(phase) | material scope is exactly the five ASSF-T0 artifacts named in Allowed scope and Write Ownership; session-sync is separate if needed |
| traceScope(phase, actor) | one Codex trace covers dispatch authoring, material execution, review, and closure |
| commitOwner(phase) | Codex owns material commit; session-sync commit is separate if continuity state changes |
| crossBatchIsolation | no ADIF, runtime, public-sync, skill corpus migration, or session-sync mutation in the material commit |
| nextMoveSurfaces | after material closure, update active session surfaces only in a dedicated session-sync lane if current mode or next allowed move changes |
| Closer designation | Codex is the designated closer |

## Scope

Allowed scope:

- create T0 GC-018, work order, audit, and completion review;
- update ASSF roadmap status and T0 row;
- record a proposed canonical package root only.
- `docs/baselines/CVF_GC018_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md`
- `docs/audits/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md`
- `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md`
- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`

Forbidden scope:

- no package root creation or migration;
- no schema/source JSON, generated index, resolver, loader, checker, hook, or
  CLI/MCP adapter implementation;
- no edit to existing skill library, governance registry, Toolkit runtime,
  Web templates, public-sync, provider/live, or session state in the material
  commit.

Risk ceiling: R1.

## Required First Reads

- `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
- `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`
- `docs/reference/guard_orientation/README.md`
- `governance/skill-library/specs/CVF_SKILL_SPEC.md`
- `governance/toolkit/05_OPERATION/CVF_SKILL_ROLLOUT_POLICY.md`
- `governance/skill-library/README.md`
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md`
- `docs/concepts/skill-system.md`
- `EXTENSIONS/CVF_TOOLKIT_REFERENCE/01_CORE_MAPPING/skill.schema.mapping.md`
- `EXTENSIONS/CVF_v3.0_CORE_GIT_FOR_AI/skill_lifecycle/skill.lifecycle.ts`
- `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md`
- `docs/roadmaps/archive/CVF_SKILL_EVOLUTION_LOOP_RUNTIME_ADOPTION_ROADMAP_2026-05-16.md`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
rg --files --hidden --no-ignore governance/skill-library
rg --files --hidden --no-ignore EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS
rg --files --hidden --no-ignore EXTENSIONS | rg -i "skill|skills|SKILL"
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 87e2013a --head HEAD
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| CVF Skill Spec exists and defines identity, capability, risk, authority, and audit fields | `governance/skill-library/specs/CVF_SKILL_SPEC.md` | Required Sections | `Skill Identity`; `Authority Mapping`; `Audit & Traceability` | skill spec | VALUE_SET | ACCEPT |
| Governance skill library owns registry, specs, UAT, and external intake scripts | `governance/skill-library/README.md` | File Structure; Scripts | `governance/skill-library/registry/` | governance skill library | EXISTS | ACCEPT |
| End-user library owns form-based `.skill.md` content and active/legacy portfolio notes | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | Statistics; Portfolio Note | `.skill.md` | end-user skill library | EXISTS | ACCEPT |
| Toolkit uses an executable schema distinct from form-based skills | `EXTENSIONS/CVF_TOOLKIT_REFERENCE/01_CORE_MAPPING/skill.schema.mapping.md` | Toolkit Canonical Skill Contract | `skillId`; `status`; `inputSchema`; `outputSchema` | Toolkit skill schema | VALUE_SET | ACCEPT |
| v3 lifecycle registry uses PROPOSED/REGISTERED/VERIFIED/ACTIVE/DEPRECATED/REVOKED states | `EXTENSIONS/CVF_v3.0_CORE_GIT_FOR_AI/skill_lifecycle/skill.lifecycle.ts` | `SkillLifecycleState` | lifecycle states | v3 lifecycle registry | VALUE_SET | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order handling | Output artifact | Status |
|---|---|---|---|
| Enumerate owner surfaces | bounded inventory commands and owner map | T0 audit | PASS |
| Record contradiction ledger | audit contradiction table | T0 audit | PASS |
| Propose canonical root | proposed-only root decision | T0 audit | PASS |
| No migration | forbidden scope and diff evidence | completion review | PASS |
| Dual consumer accounting | six-column matrix | all T0 artifacts | PASS |

## Write Ownership

| Path | Mode |
|---|---|
| `docs/baselines/CVF_GC018_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | create |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | create |
| `docs/audits/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | create |
| `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md` | create |
| `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | update T0/status/matrix/AOT only |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation root | Proposed only: `docs/reference/agent_system_skills/` |
| Root created in this tranche | NO |
| Storage class | future canonical reference package root; not current runtime storage |
| Generated aggregate | N/A with reason: T0 does not create `skill-index.json` |
| Compact source layout | deferred to ASSF-T1/T2 |
| Adapter storage | deferred; external CLI/MCP adapter requires separate GC-018/work order |
| Current owner sources | governance spec/registry, end-user library, Toolkit schema, v3 lifecycle, product concept, archived external-skill screening |
| Boundary | no migration, no activation, no runtime load, no public-sync |

## Execution Plan

1. Read required sources.
2. Run bounded inventory commands.
3. Write T0 audit with owner map, contradiction ledger, and proposed root.
4. Update roadmap T0 status and matrix shape.
5. File completion review.
6. Run reviewer-fast, pre-implementation, commit steward, pre-commit, and
   committed-range pre-closure.

## Mandatory Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | future ASSF package contract and resolver | T0 grants no loading, activation, mutation, commit, or runtime authority | T0 audit and completion review | N/A with reason: no adapter in T0 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future separately authorized CLI/MCP adapter | no ingress, authentication, approval, receipt, raw-data release, mutation, runtime, public, or readiness claim | paired GC-018 and dual-surface standard | deferred adapter owner; separate GC-018 required | `DEFERRED_WITH_REASON` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance audit only.

## Evidence Requirements

| Evidence requirement | Required source |
|---|---|
| Owner inventory | bounded `Test-Path` and `rg --files --hidden --no-ignore` command evidence |
| Source facts | Source Verification Block with direct repo-local sources |
| Contradiction ledger | T0 audit table |
| No migration/runtime claim | material changed set and Closure Diff Gate |
| Dual-agent accounting | six-column Dual Agent Surface Matrix in every T0 artifact |
| Closure | reviewer-fast, commit steward, pre-commit, and real-range pre-closure gates |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | screened external skill -> ASSF-T4 normalization candidate -> CVF-owned package review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | future ASSF-T4 intake normalization contract |
| Disposition | T0 may cite screened external-skill patterns, but must not import, activate, or expose them |
| Claim boundary | external-agent CLI/MCP package use remains deferred |

## Review Gate

Before claiming closure, run:

```powershell
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 87e2013a --head HEAD --enforce
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 87e2013a --head <material-commit>
```

The pre-closure gate must use a real material commit SHA, not
an empty same-head verification range.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | Audit owner map exists | T0 audit |
| AC2 | Contradiction ledger exists | T0 audit |
| AC3 | Proposed root is proposed-only and not created | T0 audit and diff |
| AC4 | Existing skill corpus/runtime files are untouched | committed diff |
| AC5 | Roadmap records ASSF-T0 closed bounded without full roadmap closure | roadmap |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T0_CLOSED_PASS_BOUNDED_PENDING_T1_SELECTION` | PASS |
| GC-018 status | paired baseline | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md` | reviewer-owned closure review | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T0 is not authorized to update GC-051 registry surfaces and no generated skill index is created | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T0 is not authorized to update GC-051 registry surfaces and no generated skill index is created | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported; external screening cited as reference input only | N/A with reason |
| System loop interlock | ASSF roadmap | T1/T2 remain future tranches; no automatic skill activation | PASS |
| Session continuity | active session sync if next move changes | separate session-sync lane after material commit | PASS |
| Public export | this work order | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Status | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| Route | `SINGLE_AGENT_MULTI_ROLE` | `SINGLE_AGENT_MULTI_ROLE` | PASS |
| Changed set | five ASSF-T0 artifacts only | baseline, work order, audit, completion review, roadmap | PASS |
| External CLI/MCP disposition | deferred with adapter boundary | `DEFERRED_WITH_REASON` | PASS |
| Runtime/provider/public claim | none | none | PASS |

## Closure Checklist

- [x] Source Verification Block uses direct source files.
- [x] Roadmap-to-work-order trace is present.
- [x] Dual Agent Surface Matrix includes `INTERNAL_AGENT` and `EXTERNAL_AGENT_CLI_MCP`.
- [x] Allowed paths include every material changed path.
- [x] External Knowledge Intake Routing is present with chain-map citation.
- [x] Public Export Disposition is `DEFERRED_PRIVATE_ONLY`.
- [x] Machine Closure Package is present.
- [x] No package root, generated index, resolver, runtime adapter, or skill activation is claimed.

## Operator Checkpoint

ASSF-T0 may close without another operator checkpoint because the operator
already selected the package-skills roadmap and T0 is bounded documentation
work. ASSF-T1 requires explicit operator selection or a fresh dispatch packet.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if a gate fails outside allowed paths, a source
fact cannot be verified, any existing skill corpus/runtime file would need
mutation, external CLI/MCP runtime behavior becomes necessary, or T1/T2 package
creation is required to complete T0.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher/worker/reviewer |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T0 work order execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, inventory commands, apply_patch, governance gates, git commit |
| Target paths | this work order; paired baseline; T0 audit; T0 completion review; ASSF roadmap |
| Allowed scope source | operator instruction, active session next move, ASSF roadmap |
| Before status evidence | clean HEAD `87e2013a` |
| After status evidence | T0 closed bounded in material commit |
| Diff evidence | committed name-status and pre-closure gate |
| Approval boundary | ASSF-T0 documentation/audit only |
| Claim boundary | no package/index/resolver/runtime/adapter/public behavior |
| Agent type | single-agent multi-role governed batch |
| Invocation ID | `assf-t0-work-order-2026-06-23` |
| Expected manifest | this work order; paired baseline; T0 audit; T0 completion review; ASSF roadmap |
| Actual changed set | this work order; paired baseline; T0 audit; T0 completion review; ASSF roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This work order closes only ASSF-T0 audit work. ASSF-T1 schema, package-root
creation, index/resolver implementation, CLI/MCP adapter, public-sync, and
skill activation remain future separately governed tranches.
