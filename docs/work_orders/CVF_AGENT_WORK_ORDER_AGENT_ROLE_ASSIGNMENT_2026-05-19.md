# CVF Agent Work Order - Agent Role Assignment And Delegation

Memory class: POINTER_RECORD

Status: CLOSED - completed as docs/reference prerequisite before Lane B/C/H
implementation, with operator waiver to proceed without waiting for a separate
Claude review in this overnight execution session.

## Purpose

Define the bounded work needed to turn the current partially absorbed
agent-role, orchestrator, worker, and subagent knowledge into a practical
CVF-native role-assignment standard for agent execution.

This work order exists because Lane B/C/H implementation will rely on clear
agent role assignment. The role standard should be completed before Lane B
opens implementation, so downstream work orders can assign orchestrator,
planner, implementer, reviewer, auditor, and specialist worker roles without
scope drift.

## Source

Source inputs:

- Operator instruction on 2026-05-19: complete agent role assignment work before
  or as a prerequisite to Lane B/C/H execution.
- `AGENT_HANDOFF_V9_2026-05-18.md` - active session state, selected Lane B/C/H
  order, and legacy/source reuse instruction.
- `docs/reviews/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md` - records
  Surface 2 agent/actor role and Surface 7 delegation/handoff gaps.
- `docs/reviews/CVF_17_05_UNABSORBED_KERNEL_SOURCE_MATRIX_2026-05-17.md` -
  records ORCHESTRATOR and worker-lane source concepts as not fully absorbed.
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md` -
  records GAP-17.05-001, GAP-17.05-002, and GAP-17.05-013.
- `docs/reviews/CVF_LEGACY_PHASE_D_ORCHESTRATOR_TRANCHE_COMPLETION_2026-05-18.md`
  - confirms the ORCHESTRATOR tranche is contract-local, not runtime
  enforcement.
- `docs/reviews/CVF_LEGACY_PHASE_D_ROLE_PERMISSION_TRANCHE_COMPLETION_2026-05-18.md`
  - confirms role/permission work is contract-local.

Legacy source files to re-open before authoring:

- `.private_reference/legacy/CVF ADD/Human System Harness/CVF_ORCHESTRATOR_DELEGATION_CONTRACT.md`
- `.private_reference/legacy/CVF ADD/deepagents/CVF_WORKER_DELEGATION_CONTRACT.md`
- `.private_reference/legacy/CVF ADD/deepagents/CVF_SUBAGENT_EXECUTION_BOUNDARY.md`
- `.private_reference/legacy/CVF ADD/Agent Harnesses/CVF_WORKER_SESSION_CONTRACT.md`
- `.private_reference/legacy/CVF ADD/Agent Harnesses/CVF_EXECUTION_SESSION_PROTOCOL.md`
- `.private_reference/legacy/CVF ADD/Agent Harnesses/CVF_SESSION_VALIDATION_GATE_SPEC.md`
- `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md`
- `.private_reference/legacy/CVF_Important/ADDING_CONTEXT CONTROL/CVF_AGENT_ROLE_EXECUTION_SPEC.md`

## Owner / Source

Owner: CVF orchestration and delegation surface.

Dispatcher: operator and current coordinating agent.

Implementer: Codex or assigned implementing agent.

Reviewer: Claude or assigned reviewer. Operator waiver is required if reviewer
silence must be treated as non-blocking.

## Scope / Target / Owner Boundary

Target deliverables:

- `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md`
- `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md`
- update to `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_BCH_2026-05-19.md`
  only if the new role standard changes the Lane B/C/H dispatch prerequisite;
- update to `docs/INDEX.md` release navigation when new reference files are
  created;
- update to `AGENT_HANDOFF_V9_2026-05-18.md` for session continuity.

Owner boundary:

- This work order is docs/reference and dispatch-standard work only.
- It does not authorize runtime scheduler enforcement, live subagent execution,
  new worker spawning, provider behavior changes, public claims, or Phase 2.B
  runtime expansion.

## Protocol / Contract / Requirements

Protocol:

- Complete this role-assignment work order before filing Lane B GC-018, unless
  the operator explicitly waives the prerequisite.
- Re-open the listed legacy source files before writing new canon.
- Treat matrix and ledger rows as navigation aids, not substitutes for source
  review.
- Record source reuse decisions inside the new reference standard:
  `reuse`, `normalize`, `reject`, or `defer`.
- Keep all claims at `defined` level unless tests or live proof are added by a
  later authorized tranche.

Contract:

- The role assignment matrix must tell an orchestrator how to assign roles for
  a user request.
- The delegation/subagent standard must define when a subagent or specialist
  worker may be used, what it may receive, and what it must not do.
- Lane B/C/H remains sequential after this prerequisite closes.

## Enforcement / Verification

Verification is through:

- source-path citations in the new reference files;
- structural Markdown and docs governance checks;
- explicit statement that no runtime enforcement claim is made;
- reviewer no-blocking disposition or operator waiver before Lane B starts.

## Boundaries / Non-Goals

Non-goals:

- no runtime role-enforcement implementation;
- no scheduler, worker pool, background job, or live subagent lifecycle;
- no new provider calls;
- no public catalog promotion unless separately requested;
- no replacement of existing CPF/EPF delegation contracts;
- no broad legacy absorption outside role/delegation/subagent assignment.

## Claim Boundary

This work order may close with a `defined` claim only:

- agent role assignment matrix is defined;
- delegation and subagent boundary standard is defined;
- Lane B/C/H prerequisite order is recorded.

It must not claim runtime-enforced ORCHESTRATOR behavior, runtime worker-lane
dispatch, or live subagent governance.

## 1. Mission

Create a CVF-native role assignment and delegation standard before Lane B/C/H
implementation begins.

Success means an orchestrator can read the standard and decide:

- which role owns intake, planning, implementation, review, audit, and
  operator escalation;
- when a specialist worker or subagent is allowed;
- when delegation is mandatory, forbidden, or requires operator approval;
- which context, tools, artifacts, memory writes, and review gates apply.

## 2. Authority Chain

- Operator instruction: 2026-05-19 request to sequence agent-role work before
  Lane B/C/H implementation.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Decision pack:
  `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md`
- Lane roadmap:
  `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_B_C_H_2026-05-19.md`
- Current work-order standard:
  `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- Active handoff: `AGENT_HANDOFF_V9_2026-05-18.md`

Authority boundary:

- This work order authorizes authoring the role/delegation reference standard
  only.
- If the work requires runtime enforcement, stop and propose a fresh GC-018.

## 3. Agent Roles

- Orchestrator / dispatcher: current coordinating agent.
- Implementer: Codex or assigned implementing agent.
- Reviewer: Claude or assigned reviewer.
- Auditor / governance: Markdown, docs taxonomy, and active-session gates.
- Operator approval required for: runtime scope, public claim changes, reviewer
  waiver, or making Lane B proceed before this work closes.

## 4. Scope

Allowed scope:

- Create the two target reference files listed above.
- Normalize relevant legacy concepts into CVF-native language.
- Cite source paths and current CVF owner/gap records.
- Update Lane B/C/H work order only for sequencing and first-read linkage.
- Update docs index and handoff pointers.

Forbidden scope:

- Do not modify runtime code.
- Do not add or change live provider behavior.
- Do not claim full ORCHESTRATOR absorption.
- Do not claim runtime subagent enforcement.
- Do not expand Lane B/C/H scope.

Risk ceiling:

- R0 for docs/reference authoring.
- Escalate to R1 and return to orchestrator if any implementation or runtime
  semantics are proposed.

## 5. Required First Reads

Before authoring files, read:

- `AGENT_HANDOFF_V9_2026-05-18.md` - active posture and source reuse
  instruction.
- `docs/reviews/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md` -
  current owner map and freeze blockers.
- `docs/reviews/CVF_17_05_UNABSORBED_KERNEL_SOURCE_MATRIX_2026-05-17.md` -
  source concept status.
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md` -
  active gap state.
- `.private_reference/legacy/CVF ADD/Human System Harness/CVF_ORCHESTRATOR_DELEGATION_CONTRACT.md`
  - orchestrator coordination boundary.
- `.private_reference/legacy/CVF ADD/deepagents/CVF_WORKER_DELEGATION_CONTRACT.md`
  - bounded worker delegation contract.
- `.private_reference/legacy/CVF ADD/deepagents/CVF_SUBAGENT_EXECUTION_BOUNDARY.md`
  - subagent execution boundary.
- `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md`
  - role templates and deny rules.

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
python governance/compat/check_active_session_state.py --enforce
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_docs_governance_compat.py
rg -n "ORCHESTRATOR|worker lane|subagent|role catalog|delegationRequired" docs/reviews docs/reference AGENT_HANDOFF_V9_2026-05-18.md
git status --short
```

Expected results:

- active session state is compliant;
- Markdown and docs governance checks pass before new edits;
- current role/delegation references are visible;
- unrelated working-tree changes are not overwritten.

If a pre-flight check fails, stop and record the failed command and result.

## 7. Write Ownership

Owned files or modules:

- `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md`
- `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_BCH_2026-05-19.md`
- `docs/INDEX.md`
- `AGENT_HANDOFF_V9_2026-05-18.md`

Forbidden paths:

- `EXTENSIONS/**`
- `governance/**` except running checks
- public-sync repository files
- `.private_reference/**` source files

Write mode:

- create target reference files;
- modify-listed for work order, index, and handoff only.

## 8. Execution Plan

Steps must be sequential unless explicitly marked parallel-safe.

1. Re-read the required source and current CVF evidence.
2. Create the role assignment matrix.
3. Create the delegation and subagent boundary standard.
4. Update Lane B/C/H work order to point at the completed prerequisite.
5. Update docs index and handoff.
6. Run governance checks.
7. Prepare reviewer handoff with source reuse decisions and claim boundary.

Each step must state:

- input artifact;
- output artifact;
- validation command or evidence;
- stop condition.

## 9. Evidence Requirements

Required evidence:

- source reuse table in the role/delegation standard;
- path existence for both new reference files;
- `python governance/compat/check_markdown_structural_completeness.py`;
- `python governance/compat/check_docs_governance_compat.py`;
- `python governance/compat/check_active_session_state.py --enforce`.

Evidence Trace Block requirements:

- Claim:
- Command:
- Result:
- Key path:
- Verdict:

## 10. Acceptance Criteria

- [ ] Role assignment matrix exists and covers operator, orchestrator,
      planner, implementer, reviewer, auditor, and specialist worker/subagent.
- [ ] Delegation/subagent boundary standard exists and covers allowed
      delegation, forbidden delegation, context boundary, tool boundary,
      artifact boundary, memory boundary, escalation, and review gate.
- [ ] Source reuse decisions cite the relevant legacy source paths.
- [ ] Lane B/C/H work order records that Lane B waits for this prerequisite or
      an operator waiver.
- [ ] No runtime code is changed.
- [ ] Governance checks pass.

## 11. Review Gate

Implementation may proceed only after:

- this work order exists and is available for reviewer/operator inspection.

Closure may proceed only after:

- reviewer no-blocking disposition; or
- explicit operator waiver.

Lane B GC-018 may be filed only after this work closes, unless the operator
explicitly waives the role-standard prerequisite.

Reviewer silence is not approval unless the operator explicitly records a
waiver for this work order.

## 12. Closure Checklist

- [ ] All acceptance criteria satisfied or explicitly marked N/A with reason
- [ ] Required governance checks run
- [ ] Runtime/public claims explicitly bounded
- [ ] Lane B/C/H prerequisite status updated
- [ ] GC-020 handoff updated with current HEAD after commit
- [ ] Changed files listed for reviewer

## 13. Return-To-Orchestrator Conditions

Return to orchestrator without continuing if:

- source files contradict current gap ledger in a material way;
- runtime enforcement is required to make the role standard truthful;
- target reference files need a new taxonomy or guard;
- reviewer objects to treating this as a docs/reference prerequisite;
- implementation would exceed R0 docs-only scope;
- public/provenance boundary becomes relevant.
