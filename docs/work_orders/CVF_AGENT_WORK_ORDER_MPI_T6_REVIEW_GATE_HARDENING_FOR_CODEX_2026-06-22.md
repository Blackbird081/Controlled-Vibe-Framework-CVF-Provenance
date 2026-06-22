# CVF Agent Work Order - MPI-T6 Review Gate Hardening

Memory class: FULL_RECORD

Status: DISPATCHED

Date: 2026-06-22

dispatchBaseHead: 603390b7

executionBaseHead: 603390b7

closureBaseHead: 603390b7

Commit mode: WORKER_MAY_COMMIT

## Dispatch Prompt Envelope

Role: Codex single-agent implementer, reviewer, closer, and commit steward.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MPI_T6_REVIEW_GATE_HARDENING_FOR_CODEX_2026-06-22.md`

Commit mode: `WORKER_MAY_COMMIT`

executionBaseHead: `603390b7`

Current-time notes: Claude's uncommitted MPI-T6 artifacts remain isolated in
the operator worktree and are regression input only.

Do-not-misread notes: do not edit, stage, commit, or treat those artifacts as
canonical authority in this hardening worktree.

Required first actions: read the required sources, confirm the isolated clean
worktree, and run the real-range pre-dispatch gate.

Return contract: close only after focused tests, regression proof, reviewer-
fast, and committed-range closure evidence pass.

Implement the bounded hardening authorized by
`docs/baselines/CVF_GC018_MPI_T6_REVIEW_GATE_HARDENING_2026-06-22.md`.
Do not edit Claude's MPI-T6 artifacts. Return committed implementation and
focused regression evidence to Codex reviewer/closer.

## Purpose

Move four MPI-T6 review defects from manual reviewer findings into the earliest
applicable deterministic gates, without attempting general natural-language
fact checking.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator instruction on 2026-06-22 to harden CVF before MPI-T6 repair |
| Intake role | Codex implements and closes one bounded checker/test tranche |
| Reviewer role | Codex reviewer/closer with separate completion evidence |
| Routing decision | `SINGLE_AGENT_MULTI_ROLE` |
| canonical route mode | `SINGLE_AGENT_MULTI_ROLE` |
| selected role route | one-agent-many-roles |
| Public route | `DEFERRED_PRIVATE_ONLY` |
| escalation condition | forbidden path, runtime/provider/live work, public-sync, or claim-boundary expansion |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task and role guard map |
| `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | closure and residue rules |
| `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | ASCII discipline |
| `governance/compat/check_closure_packaging_preflight.py` | closure-residue and corpus owner |
| `governance/compat/check_machine_closure_package.py` | closed-artifact package owner |
| `governance/compat/check_agent_packet_authority_and_encoding.py` | provider-authority owner |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| closure checker scopes active docs by prefixes | `governance/compat/check_closure_packaging_preflight.py` | constants and active-doc predicate | `ACTIVE_DOC_PREFIXES` | closure packaging preflight | EXISTS | ACCEPT |
| closed residue is pattern-driven | `governance/compat/check_closure_packaging_preflight.py` | stale-language validation | `STALE_CLOSED_PATTERNS` | closure packaging preflight | EXISTS | ACCEPT |
| machine closure filters governed docs before validating | `governance/compat/check_machine_closure_package.py` | active-doc predicate | `_is_active_governed_doc` | machine closure package checker | EXISTS | ACCEPT |
| machine closure has a closed-equivalent predicate | `governance/compat/check_machine_closure_package.py` | status detection | `_is_closed_equivalent` | machine closure package checker | EXISTS | ACCEPT |
| provider authority validation already exists | `governance/compat/check_agent_packet_authority_and_encoding.py` | provider authority validation | `find_provider_specific_authority_violations` | packet authority checker | EXISTS | ACCEPT |
| all three checkers are already reviewer-fast wired | `governance/compat/run_local_governance_hook_chain.py` | reviewer-fast command list | `reviewer-fast` | local governance hook chain | RUNTIME_BEHAVIOR | ACCEPT |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles with separate implementation and closure evidence |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC if needed |
| baseHeadFor(phase) | `dispatchBaseHead=603390b7`; `executionBaseHead=603390b7`; `closureBaseHead=603390b7` before material commit |
| changedSetScope(phase) | dispatch docs, three checker/test pairs, worker return/completion; session sync separate |
| traceScope(phase, actor) | one Codex trace covers the bounded material tranche |
| commitOwner(phase) | Codex owns material and any separate session-sync commit |
| crossBatchIsolation | Claude's uncommitted MPI-T6 worktree remains separate and untouched |
| Before status evidence | isolated hardening worktree was clean at HEAD `603390b7` before dispatch artifacts |
| nextMoveSurfaces | session/front-door sync only following material completion |
| Closer designation | Codex is the designated closer |

## Authority Chain

| Authority | Role | Disposition |
|---|---|---|
| Operator instruction 2026-06-22 | prioritize hardening before MPI-T6 repair | ACCEPT |
| Matching GC-018 | protected-path and claim-boundary authorization | ACCEPT |
| Closure quality standard | closure and residue requirements | ACCEPT |
| AHB-T2 contract | single-agent route and commit ownership | ACCEPT |

## Agent Roles

| Role | Owner | Disposition |
|---|---|---|
| Dispatcher | Codex | assigned |
| Implementer | Codex | assigned |
| Reviewer/closer | Codex | assigned with separate completion evidence |
| Commit steward | Codex | assigned |

## Pre-Flight Checks

| Check | Result |
|---|---|
| Startup front door and active state | read and acknowledged |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` |
| Worktree isolation | clean worktree at `603390b7`; Claude changed set excluded |

## Write Ownership

| Path group | Owner | Disposition |
|---|---|---|
| hardening dispatch/checker/test/review artifacts | Codex | owned by this tranche |
| Claude MPI-T6 baseline and roadmap | operator/Claude worktree | excluded; do not touch |
| session-sync surfaces | Codex only following material completion | separate commit |

## Execution Plan

| Step | Required result |
|---|---|
| Dispatch validation | pre-dispatch autorun passes on real changed range |
| Checker implementation | four deterministic defect classes covered |
| Regression proof | MPI-T6-shaped fixture fails for new reasons |
| Closure | focused tests and reviewer/closure gates pass |

## Evidence Requirements

| Requirement | Evidence |
|---|---|
| Focused tests | exact pytest command and counts |
| Regression sample | MPI-T6-shaped fixture violation list |
| Changed set | `git diff --name-status` and committed diff |
| Closure | reviewer-fast, steward, and pre-closure outputs |

## Review Gate

Reject closure if any new rule relies on provider memory, scans outside a
quoted repo-local path, overfires on safe counterexamples, or fails to reject
the MPI-T6-shaped regression fixture.

## Closure Checklist

- [x] GC-018 and work order authored for dispatch.
- [ ] Focused tests pass.
- [ ] MPI-T6-shaped regression proof passes.
- [ ] Reviewer-fast passes on the hardening worktree.
- [ ] Material changed set is committed and clean.
- [ ] Pre-closure gate passes on the committed range.

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only with completion evidence and resolved
checklist. Return `BLOCKED_WITH_REASON` only for an out-of-scope blocker.

## Operator Checkpoint

N/A with reason: the operator already selected this bounded hardening tranche;
MPI-T6 correction remains parked until the new controls are closed.

## Allowed Scope

- the two dispatch artifacts;
- `governance/compat/check_closure_packaging_preflight.py` and focused test;
- `governance/compat/check_machine_closure_package.py` and focused test;
- `governance/compat/check_agent_packet_authority_and_encoding.py` and focused test;
- one worker return and one completion review;
- later generated session-sync sources and active handoff.

## Forbidden Scope

- Claude's MPI-T6 baseline and roadmap edits;
- hook wiring changes, because all owner checkers are already wired;
- runtime/product source or tests;
- live/provider/API proof;
- public-sync or public claims;
- broad prose linting or universal semantic correctness claims.

## Implementation Requirements

1. Treat `docs/baselines/` as active governed docs for closed-equivalent
   packaging validation.
2. Require closed GC-018 baselines to carry a Machine Closure Package.
3. Reject explicit closed-roadmap residue including `COMPLETE_PENDING_GATES`
   and statements that the just-closed child remains parked.
4. Reject an exhaustive `contains only` directory claim when the referenced
   repo directory has additional direct child files. Limit the grammar so safe
   descriptive prose is not treated as exhaustive evidence.
5. Reject provider-local interaction tokens such as `AskUserQuestion` when an
   authority/source table marks them `ACCEPT`, unless the row explicitly says
   `NOT_CVF_SOURCE` or equivalent.
6. Add safe counterexample tests for every rule.

## Evidence Reuse And Encoding Plan

Use ASCII in all authored source, tests, and markdown. Reuse existing checker
parsers and hook wiring. Do not add dependencies or a new checker process.

## Required Checks

```powershell
python -m pytest governance/compat/test_check_closure_packaging_preflight.py governance/compat/test_check_machine_closure_package.py governance/compat/test_check_agent_packet_authority_and_encoding.py -q
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD
```

## Acceptance Criteria

- all focused tests pass;
- MPI-T6-shaped regression fixture reports all four new defect classes;
- safe counterexamples pass;
- no unrelated checker or hook file changes;
- final changed set is clean and committed before closure.

## Fail Conditions

- a new rule depends on provider memory or chat history;
- the rule performs broad filesystem traversal without a path quoted in the
  checked artifact;
- valid historical closed artifacts are reopened outside the changed range;
- the checker claims universal semantic validation;
- any forbidden path is modified.

## Worker Autonomy / No-Question Rule

Repair allowed-scope test or gate failures and rerun autonomously. Stop only if
repair requires a forbidden path, runtime/provider/live
work, public-sync, destructive action, or a changed claim boundary.

## Single-Agent Multi-Role Control Block

Role separation ledger: Codex records dispatch, implementation, reviewer, and
closer evidence in separate artifact sections and commits.

Evidence basis: review uses repository source, focused tests, diff output, and
machine gates rather than agent memory.

Self-review boundary: independent review is not claimed; the bounded result is
single-agent evidence-backed closure only.

Escalation conditions: stop for forbidden scope, runtime/provider/live work,
public-sync, destructive action, or an operator decision outside this packet.

Gate sequence: pre-dispatch, pre-implementation, focused tests, reviewer-fast,
pre-closure, and pre-push when applicable.

## Foundation Storage Layout Block

N/A with reason: this tranche edits existing checker/test files and creates
ordinary dated baseline/work-order/review evidence. It creates no durable
foundation folder, stable reference family, storage layout, or front door.

## Worker Return Packet Shape Contract

Return status, execution base, exact changed files, focused test output,
MPI-T6-shaped regression output, gate evidence, git status, public disposition,
finding-to-governance disposition, and claim boundary.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Disposition |
|---|---|---|
| N/A with reason: this tranche is operator-authorized review-friction hardening, not roadmap-derived. | Preserve MPI-T6 as an untouched regression input. | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex CLI in isolated local worktree |
| Session or invocation | `mpi-t6-review-gate-hardening-2026-06-22` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-mpi-t6-hardening` |
| Command or tool surface | PowerShell, apply_patch, pytest, governance gates |
| Target paths | dispatch docs, three checker/test pairs, return/completion |
| Allowed scope source | operator instruction, matching GC-018, and this work order |
| Before status evidence | isolated worktree clean at HEAD `603390b7` |
| After status evidence | completion review and final `git status --short` |
| Diff evidence | real-range `git diff --name-status` and committed diff |
| Approval boundary | bounded private governance hardening only |
| Claim boundary | explicit deterministic review patterns only |
| Agent type | Codex single-agent multi-role |
| Invocation ID | `mpi-t6-review-gate-hardening-2026-06-22` |
| Expected manifest | two dispatch docs, three checker/test pairs, return/completion |
| Actual changed set | recorded in completion review |
| Manifest delta | must be MATCH before closure |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | deterministic markdown/repository review checks only |
| claimDisposition | N/A with reason: no Delta runtime behavior is changed |
| receiptEvidence | N/A with reason: no Delta receipt |
| actionEvidence | `N/A with reason`: no Delta action claim; focused tests and local checker output are governance evidence only |
| claimLanguage | review-gate hardening, not runtime enforcement |
| forbiddenExpansion | runtime, provider/live, public-sync, interception, arbitrary command execution, readiness, and universal control claims |
| invocationBoundary | local governance checker invocation only |
| interceptionBoundary | no IDE, shell, provider, route, or filesystem interception claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance hardening only.

## Claim Boundary

The tranche detects explicit machine-verifiable review patterns. It does not
repair MPI-T6 or establish general semantic truth.
