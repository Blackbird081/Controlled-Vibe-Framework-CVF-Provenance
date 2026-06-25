# CVF Agent Work Order GFS-PY-T1 Governed Python File Size Coverage

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-25

docType: work_order

Batch ID: GFS-PY-T1

Commit mode: SINGLE_AGENT_MULTI_ROLE_MAY_COMMIT

## Dispatch Prompt Envelope

Role: GFS-PY-T1 single-agent worker/reviewer/closer; governed Python size guard upgrade.

Canonical packet: this work order plus `docs/baselines/CVF_GC018_GFS_PY_T1_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_2026-06-25.md`.

Commit mode: `SINGLE_AGENT_MULTI_ROLE_MAY_COMMIT`.

Base: executionBaseHead `75af9858` (capture actual with `git rev-parse --short HEAD` at start).

Current-time notes: current dispatch date is 2026-06-25; record actual local start time in the completion review.

Do-not-misread notes: this is a guard-upgrade tranche only. Do not split any
monolith in T0; the dispatch-quality decomposition is held as roadmap T1-T4.
Do not author a duplicate guard or fold `.py` into `check_governed_file_size.py`.
Do not enforce non-governance Python (`EXTENSIONS/`, `tools/`,
`governance/skill-library/`). Do not raise any seeded exception above its
frozen line count. Do not change the flat baseline thresholds (it would trip
the guard's own baseline-protection). The guard must call no network/provider
API; it is a static line-count scan only.

Required first actions: read front door/state/handoff/guard orientation
documents, this work order, the GC-018 baseline, the existing
`check_python_automation_size.py` and its registry and policy doc; capture
`git status --short`; run the guard read-only before and after seeding; run
the pre-implementation gate.

Return contract: close `CLOSED_PASS_BOUNDED` after self-review with all
artifacts present and gates passing, or stop at `BLOCKED_WITH_REASON` if a
gate fails outside allowed scope.

You are the GFS-PY-T1 single-agent worker, reviewer, and closer in one
operator-granted pass. Upgrade the guard, seed the registry, wire the guard
into the local hook chain and autorun pre-implementation phase, update the
policy doc, write tests, self-review, and commit.

## Purpose

Upgrade the existing governed Python size guard to class-aware thresholds with
a touch rule, seed legacy exceptions for the governance Python already over its
class hard threshold, and wire the guard into the local hook chain and the
autorun pre-implementation phase, in one operator-granted single-agent pass.

## Core Guard Self-Protection Authorization

| Field | Disposition |
| --- | --- |
| Authorized guard-maintenance scope | GFS-PY-T1 upgrades `governance/compat/check_python_automation_size.py` in place (per-class classifier, touch rule, near-hard rule, seedAuthorization bypass), seeds `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`, appends one additive guard entry to `governance/compat/run_local_governance_hook_chain.py` (two list locations) and one to `governance/compat/run_agent_autorun_workflow_gate.py`, and extends `governance/compat/test_check_python_automation_size.py`; it does not weaken any existing check, hook, or autorun entry |
| Protected paths | `governance/compat/check_python_automation_size.py`; `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/test_check_python_automation_size.py` |
| Operator authorization | operator selected GFS-PY-T1 and confirmed per-class thresholds, touch rule, wiring point, and non-governance deferral on 2026-06-25 |
| Rollback boundary | revert this material commit; the change is additive guard logic, additive registry seed, additive wiring entries, and additive tests |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-implementation`

Returned defects:

- ADIF-0001 - Exhaustive directory claim omits actual children: this work order
  makes no exhaustive-directory claim; it names specific owned paths.
- ADIF-0002 - Provider-local interaction accepted as authority: the guard is a
  static line-count scan with no network or provider call.
- ADIF-0007 - Gate keyword in exclusion prose triggers wrong evidence class:
  this work order's exclusion and deferral prose avoid bare gate-trigger tokens
  where they would falsely signal a different evidence class than
  governance-checker maintenance.
- ADIF-0009 - Backtick-quoted heading name truncates real section: this work
  order does not backtick-quote any literal heading string.

Resolver query: taskClass=`Closure`, role=`closer`, lifecyclePhase=`pre-closure`

Returned defects:

- ADIF-0003 - Closed GC-018 lacks Machine Closure Package: a complete Machine
  Closure Package appears below.
- ADIF-0008 - Reusable lesson remains only in provider memory: the rule and
  split sequence are recorded in governed artifacts, not only session memory.
- ADIF-0004 - Decided roadmap retains same-tranche parked residue: T0 leaves no
  open residue for itself on closure.
- ADIF-0005 - Closed artifact retains pending-gate residue: the acceptance
  checkboxes below are reconciled before the closed claim.
- ADIF-0009 - Backtick-quoted heading name truncates real section: this work
  order does not backtick-quote any literal heading string.

## Scope / Target / Owner Boundary

Target: one bounded single-agent pass upgrading the governed Python size guard
to per-class thresholds with a touch rule, seeding legacy exceptions, and
wiring the guard into local and autorun enforcement.

Owner boundary:

- this work order names the single agent (Claude) as worker, reviewer, and
  closer for this operator-granted pass;
- the agent owns only the paths in Write Ownership below;
- the dispatch-quality monolith split is owned by the held roadmap T1-T4, not
  this work order.

## Authority Chain

| Authority | Path | Disposition |
| --- | --- | --- |
| GC-018 baseline | `docs/baselines/CVF_GC018_GFS_PY_T1_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_2026-06-25.md` | authorizes this work order |
| Roadmap | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | sequences T0 and the held T1-T4 split |
| Existing guard | `governance/compat/check_python_automation_size.py` | the checker upgraded in place |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | packet shape |

## Agent Roles

| Role | Assignment |
| --- | --- |
| Worker | Claude (single-agent multi-role pass) |
| Reviewer | Claude (same pass, self-review) |
| Closer | Claude (same pass) |
| Operator | authorizes scope and design; reviews the closed result |

Dispatch-authorship does not by itself grant execution; the operator granted
this single-agent multi-role pass explicitly on 2026-06-25.

## Required First Reads

- `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, the active handoff;
- `docs/baselines/CVF_GC018_GFS_PY_T1_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_2026-06-25.md`;
- `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md`;
- `governance/compat/check_python_automation_size.py` and its registry and policy doc.

## Pre-Flight Checks

- capture `git status --short` and `git rev-parse --short HEAD`;
- run the guard read-only before seeding to record the baseline over-hard set;
- confirm no duplicate guard exists and that `check_governed_file_size.py` still
  excludes `.py`.

## Write Ownership

The agent owns exactly:

- `governance/compat/check_python_automation_size.py`
- `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`
- `governance/compat/test_check_python_automation_size.py`
- `governance/compat/run_local_governance_hook_chain.py` (additive guard entries only)
- `governance/compat/run_agent_autorun_workflow_gate.py` (one additive guard entry)
- `governance/toolkit/05_OPERATION/CVF_PYTHON_AUTOMATION_SIZE_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` (cross-reference only)
- `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md`
- this work order, the GC-018 baseline, and the completion review
- session-state sources and handoff continuity after the material commit

## Required Artifact Manifest

| Artifact | Path | Status |
| --- | --- | --- |
| Roadmap | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | DELIVERED |
| GC-018 baseline | `docs/baselines/CVF_GC018_GFS_PY_T1_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_2026-06-25.md` | DELIVERED |
| Upgraded guard | `governance/compat/check_python_automation_size.py` | DELIVERED |
| Seeded registry | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | DELIVERED |
| Extended tests | `governance/compat/test_check_python_automation_size.py` | DELIVERED |
| Hook-chain wiring | `governance/compat/run_local_governance_hook_chain.py` | DELIVERED |
| Autorun wiring | `governance/compat/run_agent_autorun_workflow_gate.py` | DELIVERED |
| Policy doc | `governance/toolkit/05_OPERATION/CVF_PYTHON_AUTOMATION_SIZE_GUARD.md` | DELIVERED |
| Completion review | `docs/reviews/CVF_GFS_PY_T1_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_COMPLETION_2026-06-25.md` | DELIVERED |

## Forbidden Path Manifest

- any monolith split of `governance/compat/check_work_order_dispatch_quality.py`;
- any non-governance Python under `EXTENSIONS/`, `tools/`, `governance/skill-library/`;
- any raise of a seeded exception above its frozen line count;
- any change to the flat `softThresholdLines`/`hardThresholdLines` baseline fields;
- any network/provider/LLM call in the guard.

## Required Proof Manifest

| Proof | Required literal |
| --- | --- |
| Per-class classification test | `test_checker_files_classified` |
| Touch-rule growth test | `test_touched_excepted_file_that_grew_fails` |
| Seed-exemption test | `test_freshly_seeded_exception_growth_is_exempt` |
| Near-hard shrink test | `test_near_hard_touched_without_shrink_fails` |
| Seed-authorization accept test | `test_new_exception_with_valid_seed_authorization_is_accepted` |
| Guard dry-run after seeding | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` |

## Execution Plan

1. read first reads; capture `git status --short`.
2. add the per-class classifier, threshold resolver, touch rule, near-hard
   rule, and seedAuthorization bypass to the guard.
3. seed the registry with per-class thresholds and legacy exceptions for the
   files over their class hard threshold plus the two files the wiring pushes
   into the exception band.
4. wire the guard into the local hook chain (pre-commit and pre-push lists) and
   the autorun shared command list.
5. extend the test suite; run it green.
6. update the policy doc and the cross-reference.
7. run the guard read-only and the pre-implementation gate.
8. self-review, author the completion review, and commit material then
   session-sync.

## Review Gate

Self-review confirms: the guard is COMPLIANT repo-wide; the 15 focused tests
pass; the wiring runs in the local hook chain; no monolith was split; no
non-governance Python is enforced; no seeded exception exceeds its frozen line
count; the flat baseline thresholds are unchanged.

## Evidence Requirements

- read-only guard run output before and after seeding (over-hard set then COMPLIANT);
- `pytest governance/compat/test_check_python_automation_size.py` green (15 tests);
- a local hook-chain run showing `governed python automation size` PASS;
- the pre-implementation autorun receipt before commit.

## Worker Return Packet Shape Contract

N/A with reason: this is a single-agent multi-role pass; the return is the
completion review at
`docs/reviews/CVF_GFS_PY_T1_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_COMPLETION_2026-06-25.md`,
not a separate no-commit worker-return packet.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | the upgraded guard in the local hook chain and autorun pre-implementation | flags oversized or growing governed Python only; grants no authority and blocks no path beyond the size gate | guard source, registry, tests | no adapter implemented | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no CLI/MCP surface beyond the existing guard CLI | N/A with reason: no external surface created | N/A with reason: no adapter scope | `NOT_APPLICABLE_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` cited for routing-format conformance only; N/A with reason: no external or legacy source is ingested |
| Input type | operator-provided external comparison, critique, or recommendation |
| Required route | the coverage gap routes directly into this work order; no external corpus is consulted |
| Chain map route | internal guard-coverage gap -> operator-confirmed design -> GFS-PY-T1 work order -> guard upgrade -> local + autorun wiring |
| Matching local-view guard | N/A with reason: no external-knowledge-intake-scoped ingestion occurs |
| Owner surface | the GFS-PY guard upgrade |
| Disposition | guard-upgrade only; no external intake |
| Claim boundary | the gap originates from this repository's own guard surfaces |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
| --- | --- |
| Finding | governed Python automation was size-checked only in CI by a flat-threshold guard, so new Python size debt could land locally undetected and a checker could not be size-distinguished from a test or CLI orchestrator |
| Defect class | MACHINE_GATE_GAP |
| Learning lane | GOVERNANCE_CONTROL_PLANE |
| Learning disposition | RULE_ADDED |
| Runtime/provider/cost lane | N/A_WITH_REASON: authoring-time size-governance change with no runtime, provider, latency, token, or cost behavior |
| Promotion direction | the guard becomes class-aware and is wired into the local hook chain and the autorun pre-implementation phase, moving enforcement earlier than CI |
| Next control action | the held GFS-PY T1-T4 roadmap splits the dispatch-quality monolith so its exception can later be removed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: references internal guard internals and the GFS-PY split roadmap.

## Acceptance Criteria

- [x] the guard classifies every in-scope governed `.py` into one of the four classes;
- [x] per-class soft/hard thresholds are applied with a retained flat fallback;
- [x] an excepted file that grows when touched fails unless approvedMaxLines is raised in the same change;
- [x] a near-hard touched governed Python file fails without same-batch shrink or split evidence;
- [x] a seeded legacy exception is accepted only when its seedAuthorization GC-018 path exists;
- [x] the guard is wired into the local hook chain and the autorun pre-implementation phase;
- [x] the guard is COMPLIANT repo-wide after seeding;
- [x] no monolith is split and no non-governance Python is enforced;
- [x] the focused test suite passes.

## Fail Conditions

- [x] no monolith split occurred in T0 (confirms ABSENCE);
- [x] no duplicate guard was authored (confirms ABSENCE);
- [x] no seeded exception exceeds its frozen line count (confirms ABSENCE);
- [x] no flat baseline threshold was changed (confirms ABSENCE).

## Closure Checklist

- [x] guard upgraded and COMPLIANT repo-wide;
- [x] registry seeded with per-class thresholds and legacy exceptions;
- [x] wiring added to local hook chain and autorun;
- [x] 15 focused tests pass;
- [x] policy doc and cross-reference updated;
- [x] roadmap records T0 done and T1-T4 held;
- [x] GC-018 closed;
- [x] completion review authored;
- [x] pre-implementation gate passed before commit;
- [x] session continuity synced after material commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Roadmap state | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | T0 executed; T1-T4 held | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_GFS_PY_T1_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GFS_PY_T1_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | per-class thresholds plus seven seeded legacy exceptions | PASS |
| Registry Markdown | N/A with reason | the Python size guard has no companion markdown registry; the JSON registry is the single source | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported | N/A with reason |
| System loop interlock | this file | the guard upgrade is a reusable local gate; no retroactive enforcement on past commits | PASS |
| Session continuity | active session sync after material commit | separate session-sync lane | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Operator Checkpoint

N/A with reason: the operator confirmed all design decisions before
execution; no mid-pass operator checkpoint is parked.

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| Guard classification | four path-based classes | four classes | PASS |
| Per-class thresholds | checker/test/helper/cli soft+hard | applied with flat fallback | PASS |
| Touch rule | excepted file growth fails unless authorized bump | enforced and tested | PASS |
| Near-hard rule | touched near-hard file needs shrink/split | enforced and tested | PASS |
| seedAuthorization gating | accept only when GC-018 exists | enforced and tested | PASS |
| Wiring | local hook chain + autorun pre-implementation | both wired | PASS |
| Repo-wide guard | COMPLIANT | COMPLIANT exit 0 | PASS |
| Monolith split | none in T0 | none | PASS |
| Focused tests | all pass | 15/15 | PASS |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation path class | `governance/compat/` guard, its JSON registry, and its focused test |
| Storage decision | upgrade one existing guard in place, seed its existing JSON registry, extend its existing test; create no new durable foundation file beyond this tranche's governance artifacts |
| Existing aggregate impact | none: the guard report is computed live; no generated aggregate is added |
| Generated state impact | none: `CVF_SESSION/ACTIVE_SESSION_STATE.json` is regenerated through its sources during session-sync, not hand-edited |
| Durable governance boundary | the registry is the single source for Python size exceptions; no hidden state store is added |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | GFS-PY-T1 guard upgrade and registry seed only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - guard upgrade with dry-run and unit-test evidence |
| receiptEvidence | CVF_RECEIPT_PRESENT - autorun pre-implementation receipt before commit |
| actionEvidence | ACTION_EVIDENCE_PRESENT - guard source, registry, tests, policy doc |
| invocationBoundary | roadmap-sequenced, operator-authorized single-agent multi-role pass |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a class-aware, locally-enforced Python size guard upgrade |
| forbiddenExpansion | no monolith split, no duplicate guard, no exception raise above frozen line count, no flat-threshold change, no non-governance enforcement, no network/provider call |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Claude worker/reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | GFS-PY-T1 single-agent pass, 2026-06-25 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver query, guard edits, registry seed, gate runs |
| Target paths | the guard, registry, policy doc, test, hook chain, autorun gate, roadmap, and this tranche's governance artifacts |
| Allowed scope source | operator instruction to scope GFS-PY-T1 on 2026-06-25 |
| Before status evidence | clean worktree at HEAD `75af9858` |
| After status evidence | guard upgraded, registry seeded, wiring added, COMPLIANT repo-wide |
| Diff evidence | real-range name-status and gate output before commit |
| Approval boundary | guard upgrade and registry seed only |
| Claim boundary | no monolith split and no non-governance enforcement performed |
| Agent type | worker/reviewer/closer (single-agent multi-role) |
| Invocation ID | `cvf-gfs-py-t1-governed-python-file-size-coverage-2026-06-25` |
| Expected manifest | the guard, registry, policy doc, test, hook chain, autorun gate, roadmap, and this tranche's governance artifacts |
| Actual changed set | matches the expected manifest |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Return-To-Orchestrator Conditions

Because this is a single-agent multi-role pass, the return is to the operator,
not a separate orchestrator. Return `CLOSED_PASS_BOUNDED` to the operator when
all acceptance criteria are met and gates pass; return `BLOCKED_WITH_REASON` if
a gate fails outside allowed scope or if any change would require splitting the
monolith, enforcing non-governance Python, or raising a seeded exception above
its frozen line count.

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one agent, three roles: Claude is worker, reviewer, and closer in one operator-granted pass |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=75af9858`; `executionBaseHead=75af9858`; `closureBaseHead=75af9858` |
| changedSetScope(phase) | Claude owns the guard, registry, tests, wiring, policy doc, roadmap, and this tranche's governance artifacts; no other surface is touched |
| traceScope(phase, actor) | one Claude trace covers authoring, execution, and closure for this single-agent pass |
| commitOwner(phase) | Claude owns the material commit and the separate session-sync commit |
| crossBatchIsolation | do not mix GFS-PY-T1 with any monolith split, non-governance Python, provider/live, public-sync, or runtime work |
| Before status evidence | clean worktree at dispatch base `75af9858` |
| nextMoveSurfaces | Claude updates next-move surfaces after the material commit since the current mode advances to GFS-PY-T1 closed |
| Closer designation | Claude is the designated reviewer and closer for this operator-granted pass |

## Claim Boundary

This work order covers the GFS-PY-T1 guard upgrade and registry seed only. It
splits no monolith, enforces no non-governance Python, raises no seeded
exception above its frozen line count, changes no flat baseline threshold, runs
no network/provider call, and claims no runtime/provider/live or public
behavior.
