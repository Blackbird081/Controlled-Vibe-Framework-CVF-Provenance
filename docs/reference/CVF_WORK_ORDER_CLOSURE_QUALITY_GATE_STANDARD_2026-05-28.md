# CVF Work Order Closure Quality Gate Standard

Memory class: POINTER_RECORD

Status: canonical mandatory closure-quality standard for agent work orders.

## Purpose

This standard prevents agents from closing work orders with incomplete
roadmap traceability, stale continuity state, inaccurate file-change claims, or
unchecked acceptance residue.

It exists because CVF relies on agents to divide roles, implement, review, and
close work without continuous operator intervention. Dispatch and closure must
therefore be explicit enough that another agent can verify the result from
files and commands rather than trust memory.

## Scope

This standard applies to every new or amended CVF work order, roadmap closure,
completion review, public-sync batch, and delegated agent execution after
2026-05-28.

It is mandatory for documentation-only work, runtime/code work, public-facing
work, live-proof work, and multi-agent transfer work. Higher-risk work may add
stricter gates, but it may not omit this standard.

## Rule

No agent may mark a work order or roadmap task `CLOSED`, `CLOSED_PASS`,
`CLOSED_PASS_BOUNDED`, or equivalent unless the closure packet records and
passes the following gates:

1. Roadmap-to-work-order trace matrix.
2. Closure diff gate.
3. Claim integrity scan.
4. Negative/fail-condition scan.
5. Checklist finalization gate.
6. Continuity sync gate.
7. Agent autorun `pre-closure` gate.

If any gate is incomplete, the worker must return to Orchestrator or file a
blocking defect. Operator silence is not a waiver.

## Requirements

### 1. Roadmap-To-Work-Order Trace Matrix

Every work order derived from a roadmap must include a table before execution:

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| <requirement> | <section> | <path/field> | <command/check> | <PASS/BLOCKED/N/A with reason> |

Rules:

- every roadmap acceptance item must map to at least one work-order
  instruction or explicit `N/A with reason`;
- every required field named by a roadmap must appear as either a sourced
  runtime/source item or a declared new doc-only field;
- a missing row blocks dispatch;
- `PASS` may be recorded only after the final artifact exists and is checked.

### 2. Closure Diff Gate

Before closure, the worker must compare:

- roadmap requirements;
- work-order requirements;
- final artifact content;
- completion review claims.

The completion packet must state whether any requirement was lost, renamed, or
weakened between roadmap, work order, implementation, and review.

### 3. Claim Integrity Scan

Every claim about changed files, untouched files, public status, runtime/code
impact, live proof, provider behavior, receipt envelope behavior, hosted
readiness, production readiness, or operator acceptance must be backed by a
command, file path, receipt, or explicit `N/A with reason`.

File-change claims must be based on `git diff --name-status`, `git status
--short`, or committed diff output. Memory-based file-change claims are not
valid closure evidence.

### 4. Negative And Fail-Condition Scan

Work orders must include explicit fail conditions when missing fields,
ambiguous thresholds, stale source facts, public/provenance boundary errors, or
forbidden runtime claims would invalidate the task.

At closure, the worker must confirm each fail condition is absent or mark the
work `BLOCKED`.

### 5. Checklist Finalization Gate

Closure checklists are evidence controls, not decoration. Any unchecked item in
a work order, roadmap, completion packet, or public-sync checklist must be one
of:

- checked after evidence exists;
- marked `N/A` with reason;
- marked `BLOCKED` with return-to-orchestrator action.

Open checkbox residue is a closure defect.

### 6. Continuity Sync Gate

If the task changes current mode, handoff status, roadmap status, public-sync
status, or next allowed move, the worker must update the active session
front door, machine-readable state registry, and active handoff as applicable.

The worker must not leave a newer registry and stale front-door or handoff
claim in conflict.

### 7. Agent Autorun Pre-Closure Gate

Before any closed-equivalent status claim, run:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure
```

The completion packet must record the command and result. If the command fails,
the artifact must remain `DRAFT`, `HOLD_*`, `BLOCKED`, or equivalent until the
blocking gate is fixed or explicitly waived by the operator.

Pre-closure cannot be satisfied by handwritten `PASS` tables when the machine
gate reports source-verification, structural-completeness, continuity,
file-size, worktree, or dispatch-quality violations.

## Exceptions

There are no exceptions for delegated work-order closure.

For trivial direct answers that do not create or modify governed artifacts,
this standard does not apply. For emergency fixes, the worker may perform the
minimal fix first only when delay would cause operational harm, but the closure
quality gates must be recorded before claiming the task closed.

## Enforcement Surface

This standard is enforced by:

- work-order authors before dispatch;
- implementers before completion;
- reviewers before PASS disposition;
- active handoff/session-state sync;
- local governance hooks where structural checks apply;
- `governance/compat/check_work_order_dispatch_quality.py`, which hard-fails
  dispatch/ready work orders, connector-wave roadmaps, and fast-lane audits
  when prerequisite GC-018 baselines, source files, source-verification truth,
  roadmap trace matrices, or prerequisite completion evidence are missing.
- `governance/compat/run_agent_autorun_workflow_gate.py`, which bundles the
  mandatory phase gates for pre-dispatch, pre-implementation, pre-closure, and
  pre-push agent workflows.

Future automation may add hard checks, but manual compliance is mandatory now.

## Related Artifacts

- `AGENTS.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_AGENT_EXECUTION_WORKFLOW_SOP_2026-05-19.md`
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`
- `docs/reference/CVF_QUALITY_ASSESSMENT_STANDARD.md`
- `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`

## Final Clause

Closure is not a status label. Closure is a verified transition from authority
to artifact to evidence to continuity state. If another agent cannot reproduce
that chain from the files and commands recorded in the packet, the work is not
closed.
