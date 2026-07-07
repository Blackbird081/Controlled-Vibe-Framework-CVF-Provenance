# CVF Agent Work Order AGSG-T1 Source-Verified ASSF Reconciliation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-28

docType: work_order

Batch ID: AGSG-T1

dispatchBaseHead: `940ffadd`

executionBaseHead: `940ffadd`

closureBaseHead: `940ffadd`

commitMode: `WORKER_MAY_COMMIT`

## Dispatch Prompt Envelope

Work order route: `SINGLE_AGENT_MULTI_ROLE`.

Assigned work: source-verify AGSG-T1 against ASSF owner surfaces, author the
AGSG-T2 advisory reference, author AGSG-T3 checker value decision and lane
closeout, update the AGSG-T0 roadmap closure state, run governance gates, commit
material, and perform a separate session-sync commit.

Do not implement runtime, provider/live, public-sync, plugin, command, persona,
hook, checker, resolver, generated aggregate, package instance, or CLI/MCP
adapter changes.

## Authority Chain

| Authority surface | Role in this work order | Disposition |
|---|---|---|
| `AGENTS.md` | session startup, guard, commit, and closure rules | ACCEPT |
| `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | roadmap source and tranche scope | ACCEPT |
| `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | ASSF package and claim boundary source | ACCEPT |
| `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md` | intake/reverification/no-self-activation source | ACCEPT |
| `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | composition and authority ceiling source | ACCEPT |

## Agent Roles

| Role | Assigned agent | Boundary |
|---|---|---|
| dispatcher | Codex | author source-verified work order and baseline |
| worker | Codex | author documentation-only AGSG-T2/T3 artifacts |
| reviewer | Codex | run gates and repair in-scope failures |
| closer | Codex | close roadmap only after closure evidence exists |
| session-sync steward | Codex | update session surfaces after material commit only |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- active handoff named by the state registry
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`
- ASSF package, intake, composition, registry, generated-index, and resolver surfaces cited in Source Verification

## Pre-Flight Checks

- Confirm base head `940ffadd`.
- Confirm changed set stays inside the target documentation paths.
- Run source verification before treating any upstream or local-pack claim as CVF-owned.
- Run ADIF resolver and disclose returned defect IDs.
- Keep session-sync out of the material commit.

## Write Ownership

| Path class | Owner | Disposition |
|---|---|---|
| AGSG material docs | Codex same-agent chain | WRITE_ALLOWED |
| ASSF runtime/resolver/generated aggregate | no owner in this work order | WRITE_FORBIDDEN |
| public-sync repository | no owner in this work order | WRITE_FORBIDDEN |
| session surfaces | session-sync steward after material commit | WRITE_DEFERRED |

## Purpose

Complete the AGSG roadmap after AGSG-T0 by converting valuable external skill
governance patterns into CVF-owned, ASSF-aligned documentation while rejecting
or parking all runtime and checker lanes that do not yet prove enough value.

## Scope / Target / Owner Boundary

Target paths:

- `docs/baselines/CVF_GC018_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md`;
- `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md`;
- `docs/reviews/CVF_AGSG_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`;
- `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`;
- session-sync surfaces only after material commit.

Forbidden paths:

- `governance/compat/*.py`;
- `docs/reference/agent_system_skills/generated/skill-index.json`;
- `docs/reference/agent_system_skills/registry/entries/*.json`;
- runtime/source/test files;
- public-sync repository paths;
- upstream or legacy advisory source folders.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AGSG-T0 requires T1 source-verified ASSF reconciliation | `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | `AGSG-T1: Source-Verified ASSF Reconciliation` | `AGSG-T1` | AGSG-T0 roadmap | ACCEPT |
| Work-order source verification is mandatory before dispatch | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | `Enforcement / Verification` | `Source Verification Block` | work-order template | ACCEPT |
| ASSF package contract owns package anatomy and authority fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | `SKILL.md Profile`; `Compact Machine Source Schema`; `Risk And Lifecycle Fields` | `authorityCeiling`; `useWhen`; `doNotUseWhen` | ASSF package contract | ACCEPT |
| ASSF resolver is metadata-only and not activation evidence | `governance/compat/run_assf_skill_resolver.py` | resolver output `claimBoundary`; `resolve_skill_packet` | `resolve_skill_packet` | ASSF resolver | ACCEPT |
| ASSF generated index is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | `claimBoundary` | `claimBoundary` | ASSF generated index | ACCEPT |
| ASSF composition rules prohibit authority expansion through loading/composition | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | `No-Automatic-Promotion Invariant`; `Capability Claim Controls` | `authorityCeiling`; `capabilityClaims` | ASSF composition control contract | ACCEPT |
| Dual-agent accounting is mandatory for agent-facing artifacts | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | `Mandatory Dual Agent Surface Matrix` | `EXTERNAL_AGENT_CLI_MCP` | dual-agent surface standard | ACCEPT |
| Upstream skill anatomy and validator patterns are advisory source inputs | `.private_reference/external_repos/agent-skills/docs/skill-anatomy.md`; `.private_reference/external_repos/agent-skills/scripts/validate-skills.js` | `Recommended Structure`; `REQUIRED_SECTIONS`; `SECTION_EXEMPT_SKILLS` | `REQUIRED_SECTIONS` | upstream advisory source | ACCEPT |
| Local pack is advisory-only and cannot prove runtime enforcement | `.private_reference/legacy/CVF_Agent_Skills_Governance_Absorption_Pack/docs/absorptions/agent-skills-governance/00_SCOPE_AND_CLAIM_BOUNDARY.md` | `Out of scope`; `Prohibited claims`; `Runtime upgrade path` | `ABSORPTION_SPEC_ONLY` | local advisory pack | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Query:

```text
resolve_defect_packet(task_class='Work-order authoring / dispatch', role='dispatcher', lifecycle_phase='pre-dispatch', max_results=20)
```

Returned defectIds:

- `ADIF-0001`
- `ADIF-0002`
- `ADIF-0007`
- `ADIF-0006`

Disposition: all are accounted for by explicit source verification,
dispatch-boundary wording, dual-agent matrix, and no direct runtime/checker
implementation.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher_worker_reviewer_closer_session_sync_steward_same_agent |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`940ffadd`; executionBaseHead=`940ffadd`; closureBaseHead=`940ffadd`; sessionSyncBaseHead=material commit after closure |
| changedSetScope(phase) | material docs only before material commit; protected session/handoff paths only after material commit |
| traceScope(phase, actor) | material artifacts carry Agent Operation Trace Block; session-sync surfaces carry GC-020 marker in active handoff |
| commitOwner(phase) | same local agent may commit material and then session-sync after gates pass |
| crossBatchIsolation | worktree was clean at `940ffadd` before AGSG-T1 edits |
| nextMoveSurfaces | update after material commit to AGSG lane closed and next external-absorption selection |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | AGSG-T1 work order, AGSG-T2 advisory reference, AGSG-T3 closeout | Documentation guidance only; no resolver mutation, package activation, package instruction loading, or authority expansion | source verification rows and ASSF references | N/A with reason: no internal adapter implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | deferred ASSF adapter lane | No CLI/MCP consumer support; no external mutation or package readout is implemented by this work order | ASSF external disposition fields and dual-agent standard | separate adapter work order required | `DEFERRED_WITH_REASON` |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Artifact evidence | Status |
|---|---|---|---|
| Source-verified ASSF reconciliation | Verify ASSF T1/T2/T4/T5 and external inputs | T1 baseline and T2 reference source tables | PASS |
| Advisory repair if a gap is proven | Author compact AGSG-T2 advisory | `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` | PASS |
| Checker value decision | Author T3 closeout with reopen conditions | `docs/reviews/CVF_AGSG_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | PASS |
| Runtime/adapter lane parked | Record reopen conditions | T3 closeout and roadmap closure update | PASS |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Read startup, guard orientation, gotchas, AGSG-T0, ASSF owner surfaces, upstream source, and local pack | source verification rows |
| 2 | Author T1 baseline and this work order | baseline/work-order files |
| 3 | Author T2 advisory reference | reference file |
| 4 | Author T3 value decision and closeout | review file |
| 5 | Update AGSG-T0 roadmap to closed bounded | roadmap diff |
| 6 | Run commit steward and hook gates | gate output and commit |
| 7 | Update session/front-door/handoff after material commit | dedicated session-sync commit |

## Worker Autonomy / No-Question Rule

The assigned agent must repair in-scope gate failures and rerun the matching
gate locally. Stop only when a required source is missing, a forbidden
runtime/checker path is required, public export authorization is needed, or the
fix would exceed this work order's scope.

## Acceptance Criteria

- T1/T2/T3 artifacts exist and cite CVF-owned sources.
- The AGSG-T0 roadmap top status is closed bounded and same-file closure state
  is fresh.
- No runtime/source/test/checker/generated aggregate mutation occurs.
- Static checker work is either justified with implementation authorization or
  closed/parked with concrete reopen conditions.
- Material commit and session-sync commit are split.

## Fail Conditions

- Source Verification uses guessed fields, placeholder paths, or non-CVF
  authority as source truth.
- Direct import of upstream plugin/command/persona/hook/checker/runtime occurs.
- A claim says AGSG proves production-ready, secure, provider-backed, or
  runtime-enforced skill governance.
- Session-sync is mixed into the material commit.

## Verification / Evidence

Required:

- `git diff --check`;
- `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 940ffadd --head HEAD --enforce`;
- material commit hook chain;
- session-sync generator and session-sync commit steward after material commit.

## Current Runtime Freshness Verification

| Runtime claim | Current source checked | Evidence | Disposition |
|---|---|---|---|
| Runtime/checker/source files are outside this batch | staged changed set | `git diff --cached --name-status` shows only AGSG governed markdown/reference files | PASS |
| ASSF generated registry/index is outside this batch | staged changed set | no `docs/reference/agent_system_skills/generated/` or `registry/entries/` path in the changed set | PASS |
| Runtime behavior is not certified | claim boundary and forbidden paths | no runtime test, provider call, package activation, or checker execution is used as evidence | PASS |

## Evidence Requirements

| Evidence item | Required evidence | Disposition |
|---|---|---|
| Source verification | ACCEPT rows from CVF owner surfaces | REQUIRED |
| Closure scope | `git diff --cached --name-status` before commit | REQUIRED |
| Gate proof | commit steward preflight output | REQUIRED |
| Runtime abstention | no runtime/source/checker/generated paths in changed set | REQUIRED |
| Session split | separate session-sync commit after material commit | REQUIRED |

## Review Gate

The reviewer must run commit steward preflight in implementation mode and fix
in-scope failures before material commit. A failed source-verification,
runtime-boundary, public-boundary, or closure-packaging gate blocks closure.

## Closure Checklist

- [x] T1 baseline authored.
- [x] T2 advisory authored.
- [x] T3 closeout authored.
- [x] AGSG-T0 roadmap closure updated.
- [x] Runtime/checker/source mutation avoided.
- [x] Session-sync reserved for a separate commit.

## Return-To-Orchestrator Conditions

Return to orchestrator only when a required CVF source is missing, closure
requires runtime/checker implementation, public export is requested, or
resolution requires scope expansion outside this work order.

## Operator Checkpoint

N/A with reason: AGSG documentation-only continuation was already authorized;
no fresh checkpoint is required for in-scope documentation repair.

## Completion Evidence

| Evidence item | Status |
|---|---|
| T1 baseline authored | PASS |
| T2 advisory reference authored | PASS |
| T3 closeout authored | PASS |
| AGSG-T0 roadmap closed | PASS |
| Runtime/checker/source mutation avoided | PASS |
| Material/session commit split planned | PASS |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable foundation file created | `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` |
| Filename discipline | stable undated filename in `docs/reference`; history carried by git and closure artifacts |
| Index impact | N/A with reason: advisory reference is not an ASSF generated registry or skill-index entry |
| Refactor boundary | no existing stable reference file split, rename, or relocation |
| Guard owner | `governance/compat/check_foundation_storage_layout.py` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_COMPLETION_REVIEW_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason: no registry JSON changed | `git diff --cached --name-status` excludes registry JSON paths | PASS |
| Registry Markdown | `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` | top `Status: ACTIVE_REFERENCE` | PASS |
| External evidence digest | Source Verification Block | upstream/local advisory inputs are mapped to CVF owner surfaces; sha256 samples: upstream anatomy `3A5F57BDB384AEF91723BF6F4CAEC780E15A7A1E34453CEC41D73419AC187989`; local scope `8AB56812C0FA9F036003D81C0CAA3D8255E046EBA3AF15D5892E2EEA92FCF15D` | PASS |
| System loop interlock | `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | next move closes AGSG lane and parks runtime/checker lanes | PASS |
| Session continuity | session-sync commit after material commit | N/A with reason: intentionally split from material commit | PASS |
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| Baseline | `docs/baselines/CVF_GC018_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| Advisory reference | `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` | top `Status: ACTIVE_REFERENCE` | PASS |
| Closeout | `docs/reviews/CVF_AGSG_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap closure | `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| AGSG-WO-Q1 | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md` | `Status` | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| AGSG-WO-Q2 | `docs/baselines/CVF_GC018_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md` | `Status` | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| AGSG-WO-Q3 | `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | `Status` | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | AGSG-T1 work-order execution, 2026-06-28 |
| Working directory | repository root |
| Command or tool surface | PowerShell, rg, Get-Content, apply_patch, governance gates |
| Target paths | AGSG-T1 baseline; this work order; AGSG-T2 advisory; AGSG-T3 closeout; AGSG-T0 roadmap |
| Allowed scope source | request to write all AGSG roadmap artifacts and AGSG-T0 next allowed move |
| Before status evidence | baseHead `940ffadd`; worktree clean before AGSG-T1 edits |
| After status evidence | material artifacts authored and staged before material commit |
| Diff evidence | `git diff --cached --name-status` against baseHead `940ffadd` before material commit |
| Approval boundary | documentation/reference closeout only |
| Claim boundary | no runtime, provider/live, public-sync, checker implementation, plugin import, command import, persona orchestration, hook install, resolver mutation, package instance, adapter, benchmark, security certification, or production-readiness claim |
| Agent type | dispatcher/worker/reviewer/closer |
| Invocation ID | `cvf-agsg-t1-work-order-source-verified-reconciliation-2026-06-28` |
| Expected manifest | T1 baseline; T1 work order; T1 completion review; T2 advisory reference; T3 closeout; AGSG-T0 roadmap update |
| Actual changed set | `docs/baselines/CVF_GC018_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md`; `docs/reviews/CVF_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_COMPLETION_REVIEW_2026-06-28.md`; `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md`; `docs/reviews/CVF_AGSG_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`; `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no tracked deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSG-T1 work order for documentation-only ASSF reconciliation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - work-order and closure documentation only |
| receiptEvidence | N/A with reason: no runtime receipt, provider call, adapter run, checker implementation, or package activation |
| actionEvidence | ACTION_EVIDENCE_PRESENT - source verification, roadmap trace, and completion evidence rows |
| invocationBoundary | local governed artifact authoring and commit choreography |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | work order executes source-verified documentation reconciliation only |
| forbiddenExpansion | no runtime activation, plugin import, command import, persona orchestration, hook install, checker implementation, resolver mutation, package instance, CLI/MCP adapter, provider/live proof, public-sync, benchmark, security certification, or production-readiness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order cites private provenance workspace paths and
operator-supplied advisory material. Public-safe publication requires separate
redaction and public-sync authorization.

## Claim Boundary

This work order closes only the AGSG documentation reconciliation lane. It is
not runtime, provider/live, public-sync, package, checker, adapter, benchmark,
security, or production-readiness evidence.
