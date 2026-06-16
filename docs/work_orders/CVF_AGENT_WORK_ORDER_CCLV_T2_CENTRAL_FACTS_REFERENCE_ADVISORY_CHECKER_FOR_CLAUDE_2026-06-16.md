# CVF Agent Work Order - CCLV-T2 Central Facts Reference Advisory Checker For Claude

Memory class: POINTER_RECORD

Status: DISPATCHED_TO_CLAUDE

docType: work-order

Date: 2026-06-16

Batch ID: CCLV-T2

rawMemoryReleased: false

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 28a72f45

executionBaseHead: worker must refresh with `git rev-parse --short HEAD` before
implementation and report the value.

closureBaseHead: N/A - pending Codex reviewer closure after worker return.

## Purpose

Give Claude a bounded implementation packet for CCLV-T2 so central facts packet
and local reference drift can be caught by an advisory checker before final
review.

## Scope / Target / Owner Boundary

Target: one advisory governance checker, one focused test file, one completion
review, and a CCLV roadmap status update if implementation evidence passes.

Owner boundary: Claude owns worker implementation and pending-return evidence.
Codex owns review, closure conversion, and commit. The worker must not commit.

## Dispatch Prompt Envelope

```text
Role: Claude = worker/implementer. Codex = reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CLAUDE_2026-06-16.md.
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: 28a72f45 at dispatch authoring; worker must refresh with git rev-parse --short HEAD before implementation and report it.
Current-time notes: No live key, no provider call, no public-sync, no legacy scan. This is a narrow governance checker tranche.
Do-not-misread notes: Advisory checker only. Do not hard-wire as a global hard-fail hook. Do not rewrite old artifacts. Do not move CCLV-T1 templates.
Required first actions: read this work order, the GC-018 baseline, CCLV standard, CCLV roadmap, CCLV-T1 template, JSON companion, and local reference rules; then run the focused negative search before edits.
Return contract: COMPLETE_PENDING_REVIEW with executionBaseHead, HEAD unchanged, exact changed paths, tests/gates run, and claim boundary; or BLOCKED_WITH_REASON if scope conflicts.
```

## 1. Mission

Implement CCLV-T2: a narrow advisory checker that validates central facts
packets and local reference blocks when they are present in changed or
explicitly passed files. The checker should catch missing shared fields and
broken local references early without requiring every small batch to create a
central packet.

## 2. Authority Chain

- Operator instruction: 2026-06-16 session, Codex to select the next roadmap and
  create a Claude work order.
- Codex audit/selection:
  `docs/reviews/CVF_CCLV_T1_T1A_CODEX_AUDIT_AND_CCLV_T2_SELECTION_2026-06-16.md`.
- GC-018:
  `docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md`.
- Roadmap:
  `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`.
- CCLV standard:
  `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md`.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.

Authority boundary: if any source contradicts this work order, stop and return
`BLOCKED_WITH_REASON` instead of widening scope.

## 3. Agent Roles

- Orchestrator / dispatcher: Codex.
- Implementer: Claude.
- Reviewer / closer: Codex.
- Fresh explicit authorization required for: hard global hook wiring,
  runtime/provider/live work, public-sync, legacy scan, historical rewrites, or
  credential use.

## Intake Role Routing Decision

routeMode: MULTI_AGENT_MULTI_ROLE

Intake summary: operator requested Codex to update Claude's recent CCLV work,
assess quality, choose the next roadmap, and create a Claude work order.

Scope classification: bounded governance checker implementation with protected
`governance/compat` paths explicitly authorized below.

Risk sensitivity: R1 docs/governance checker; no live, provider, credential,
public-sync, production-readiness, or runtime-routing scope.

Selected role route: Claude worker/implementer with WORKER_MUST_NOT_COMMIT;
Codex reviewer/closer.

Escalation condition: return `BLOCKED_WITH_REASON` if implementation requires
hard global hook wiring, historical rewrite, legacy scan, live/provider work,
public-sync, or any path outside Write Ownership.

## 4. Scope

Allowed scope:

- Create `governance/compat/check_central_facts_reference.py`.
- Create `governance/compat/test_check_central_facts_reference.py`.
- Create `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md`.
- Update the CCLV roadmap only for CCLV-T2 closure and CCLV-T3 release after
  implementation evidence exists.

Forbidden scope:

- No global hard-fail hook wiring in this tranche.
- No broad repo rewrite or historical artifact migration.
- No movement of the CCLV-T1 Markdown or JSON template.
- No removal or weakening of AOT, closure quality, public export, or
  finding-learning evidence.
- No runtime/provider/API/live/public-sync/legacy broad scan.
- No commit by worker.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one advisory governance checker and
one focused checker test for CCLV-T2. No hook hard-fail wiring is authorized.

Protected paths:

- governance/compat/check_central_facts_reference.py
- governance/compat/test_check_central_facts_reference.py

Operator authorization: operator requested Codex to choose the next roadmap and
dispatch a Claude work order following CCLV-T1 closed commit `89debbd6` and
CCLV-T1A closed commit `dcc114e6`; Codex selected CCLV-T2 as the bounded next
foundation move.

Rollback boundary: if rejected, revert only CCLV-T2 implementation artifacts and
the CCLV-T2 closure update. Do not revert CCLV-T1, CCLV-T1A, session sync, or
the prompt envelope standardization commits.

## 5. Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| CCLV-T2 checker purpose | `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` | Tranche Plan row `CCLV-T2` | `CCLV-T2` | CCLV roadmap | EXISTS | ACCEPT |
| Advisory / narrow guard strategy | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Guard Strategy` | `advisory or narrow` | CCLV standard | EXISTS | ACCEPT |
| Central facts field list | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Required Central Facts` | `batchId` through `claimBoundary` | CCLV standard | EXISTS | ACCEPT |
| Local reference field list | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Required Local References` | `Central Facts Reference`; `Local View Role`; `Local Disposition`; `Local Delta` | CCLV standard | EXISTS | ACCEPT |
| Markdown template shape | `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md` | `## Central Facts Packet` | `Field` table | Closure facts template | EXISTS | ACCEPT |
| JSON template shape | `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json` | `fieldOrder`; `templateInstance` | `schemaId` | Closure facts JSON template | EXISTS | ACCEPT |
| Local role/disposition rules | `docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md` | `## Field Rules` | `Local View Role`; `Local Disposition` | Local reference rules | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

N/A with reason: this work order authorizes a documentation/governance checker
for CCLV packet shape. It makes no runtime capability, provider behavior, hosted
state, or source-symbol absence claim. Negative search below is collision
discipline for the planned checker name, not a runtime freshness claim.

## 6. Negative Search And Collision Discipline

Before editing, run a focused negative search:

```powershell
rg -n "check_central_facts_reference|central facts reference checker|CENTRAL_FACTS_REFERENCE|CCLV_T2|CCLV-T2" governance/compat docs/reference docs/work_orders docs/baselines docs/roadmaps
```

Expected dispatch-time result: only roadmap/dispatch planning references should
exist. If a real checker already exists, stop and return `BLOCKED_WITH_REASON`
with the path.

## Legacy Absorption Coverage Index Disposition

Disposition: NOT_APPLICABLE_WITH_REASON.

Reason: CCLV-T2 is a forward-only governance checker for central facts/local
reference packet shape. It does not absorb, reopen, scope, or implement legacy
knowledge, memory, graph, provider, workflow, benchmark, context, or corpus
content. No legacy coverage index row is required for this tranche.

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| CCLV-T2 advisory checker | Sections 7-9 | `governance/compat/check_central_facts_reference.py` | focused pytest and checker self-run | PASS for dispatch |
| CCLV-AC2 shared vs local distinction | Sections 7-8 | checker validates central facts and local reference blocks separately | focused tests | PASS for dispatch |
| CCLV-AC3 permissive enforcement | Sections 4, 7, 8 | advisory default; `--enforce` only when called | focused tests | PASS for dispatch |
| CCLV-AC4 local role retained | Sections 7-8 | validates local fields without replacing local artifact judgment | focused tests | PASS for dispatch |
| CCLV-AC5 no runtime/provider/live/public/legacy scope | Sections 4, 11, Public Export Disposition | claim boundary and forbidden scope | reviewer inspection | PASS for dispatch |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without additional confirmation for non-destructive actions
inside Allowed scope.

Proceed autonomously with reading named files, implementing the listed checker
and tests, repairing allowed-scope gate failures, and rerunning the required
commands. Stop and return `BLOCKED_WITH_REASON` only if the fix would exceed
Allowed scope, hard-wire a global gate, use credentials, run live/provider
proof, public-sync, scan legacy, touch forbidden paths, or change the risk/claim
boundary.

## Reviewer Closure Conversion Block

completionReviewPath: `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CLAUDE_2026-06-16.md`
- `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md`
- `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V19_2026-06-15.md`

pendingStatusTokensAllowedBeforeReview: COMPLETE_PENDING_REVIEW,
IMPLEMENTATION_COMPLETE_PENDING_REVIEW, DRAFT, HOLD_*

forbiddenClosedEquivalentResidue: COMPLETE_PENDING_REVIEW, NOT_EXECUTED_YET,
WORKER_RETURNS_PENDING, PRE_CLOSURE_NOT_RUN, FAIL_EXPECTED_PENDING_FINALITY,
DISPATCHED as current status

predecessorClosureFactSource:
`docs/reviews/CVF_CCLV_T1_CLOSURE_FACTS_PACKET_TEMPLATE_COMPLETION_2026-06-16.md`
and
`docs/reviews/CVF_CCLV_T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR_WORKER_RETURN_2026-06-16.md`

## Required First Reads

1. This work order.
2. `docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md`.
3. `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md`.
4. `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`.
5. `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md`.
6. `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json`.
7. `docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md`.

## Pre-Flight Checks

Before editing, worker must run:

```powershell
git status --short
git rev-parse --short HEAD
rg -n "check_central_facts_reference|central facts reference checker|CENTRAL_FACTS_REFERENCE|CCLV_T2|CCLV-T2" governance/compat docs/reference docs/work_orders docs/baselines docs/roadmaps
```

If the checker already exists as real implementation, stop and return
`BLOCKED_WITH_REASON`.

## 7. Write Ownership

Create/modify only:

- `governance/compat/check_central_facts_reference.py`
- `governance/compat/test_check_central_facts_reference.py`
- `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md`
- `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`

Write mode: create listed checker/test/review paths; modify only the CCLV
roadmap row/record needed for CCLV-T2 completion.

## 8. Execution Plan

1. Complete pre-flight checks and capture executionBaseHead.
2. Implement the advisory checker.
3. Add focused tests.
4. Run the required verification commands.
5. Author the completion review and update CCLV-T2 roadmap status only if the
   implementation evidence passes.
6. Return uncommitted artifacts to Codex.

## 8A. Implementation Instructions

1. Implement `check_central_facts_reference.py` with these modes:
   - default advisory mode prints violations and exits 0;
   - `--enforce` exits non-zero when violations exist;
   - `--base <sha> --head <ref>` discovers changed files;
   - `--paths <path...>` validates explicit paths.
2. Validate Markdown central facts packets when a file contains
   `## Central Facts Packet` or the required central field table.
3. Validate JSON central facts packets when a JSON file contains
   `schemaId: cvf.closureCentralFacts.v1`, `fieldOrder`, or the closure facts
   template keys.
4. Validate local reference blocks when a file contains `Central Facts
   Reference:`.
5. Do not require a central packet for files that do not opt in to the CCLV
   pattern.
6. Accept both semicolon-separated Markdown changed-set strings and JSON arrays.
7. For `Central Facts Reference`, validate the repo-relative target path exists.
   Section or anchor validation may be best-effort; missing path is the required
   violation in this tranche.
8. Keep implementation small and dependency-free, following existing
   `governance/compat/check_*.py` style.

## 9. Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Valid CCLV-T1 Markdown template passes. |
| AC2 | Valid CCLV-T1 JSON template passes. |
| AC3 | Missing any of the twelve central fields is reported. |
| AC4 | Valid local reference block with existing target path passes. |
| AC5 | Local reference block with missing repo-local path is reported. |
| AC6 | Non-applicable files pass without forcing central packet creation. |
| AC7 | Default advisory mode exits 0 with printed violations; `--enforce` exits non-zero on violations. |
| AC8 | Focused tests pass. |
| AC9 | No global hard-fail hook wiring is introduced. |

## Evidence Requirements

Worker must run:

```powershell
pytest governance/compat/test_check_central_facts_reference.py
python governance/compat/check_central_facts_reference.py --paths docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_central_facts_reference.py
git diff --check
```

Worker may also run:

```powershell
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce
```

Do not run live provider/API tests. They are out of scope.

## Review Gate

Codex review requires:

- worker return with `COMPLETE_PENDING_REVIEW`;
- exact uncommitted changed set inside Write Ownership;
- focused tests and checker self-run PASS;
- reviewer-fast PASS;
- `git diff --check` PASS;
- committed-range pre-closure PASS after Codex accepts and commits.

## Closure Checklist

- [ ] Worker reported executionBaseHead and HEAD unchanged.
- [ ] Checker implemented inside Allowed scope.
- [ ] Focused tests implemented inside Allowed scope.
- [ ] Completion review authored.
- [ ] CCLV roadmap updated only for CCLV-T2 completion/release state.
- [ ] Focused tests PASS.
- [ ] Checker self-run PASS on CCLV-T1 template/rules paths.
- [ ] Reviewer-fast PASS.
- [ ] `git diff --check` PASS.
- [ ] Codex committed accepted material range.
- [ ] Pre-closure gate PASS on committed material range.

## Return-To-Orchestrator Conditions

Return to orchestrator if any required action would exceed Allowed scope or if the
checker path already exists as a real implementation.

## 10. Return Contract

Return exactly one of:

- `COMPLETE_PENDING_REVIEW` with executionBaseHead, HEAD unchanged, exact
  changed paths, verification commands run, and claim boundary.
- `BLOCKED_WITH_REASON` with the blocking source, attempted command, and whether
  the required change would exceed Write Ownership.

Do not commit. Codex will inspect, run reviewer commands, author or amend closure
review if needed, and commit.

## Operator Checkpoint

No parked operator checkpoint for advisory CCLV-T2 implementation. Fresh
explicit authorization is required before hard global hook wiring, live/provider
work, public-sync, legacy scan, or historical rewrite.

## Claim Boundary

Final verification belongs to Codex after worker return and material commit.
Worker gate output is pending-return evidence, not closure evidence.

## 11. Detailed Claim Boundary

This work order authorizes only an advisory CCLV governance checker and focused
tests. It does not authorize runtime behavior, provider routing, live proof,
public-sync, production readiness, public readiness, or full CCLV adoption.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance work order. No public-sync batch is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator/reviewer |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 CCLV-T2 work order authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CLAUDE_2026-06-16.md` |
| Allowed scope source | operator requested next roadmap and Claude work order following CCLV-T1 closed commit `89debbd6` |
| Before status evidence | base `28a72f45` |
| After status evidence | work order authored; pending dispatch commit |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | dispatch packet only; worker must not commit |
| Claim boundary | repo-local trace only; no OS/user attribution |
| Agent type | Codex orchestrator/reviewer |
| Invocation ID | `cclv-t2-work-order-2026-06-16` |
| Expected manifest | `docs/reviews/CVF_CCLV_T1_T1A_CODEX_AUDIT_AND_CCLV_T2_SELECTION_2026-06-16.md`; `docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CLAUDE_2026-06-16.md`; `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` |
| Actual changed set | docs/reviews/CVF_CCLV_T1_T1A_CODEX_AUDIT_AND_CCLV_T2_SELECTION_2026-06-16.md; docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md; docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CLAUDE_2026-06-16.md; docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
