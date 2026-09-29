# CVF Agent Work Order - Active Continuity Read-Cost T2A Core Surface Compaction

Memory class: ACTIVE_WORK_ORDER

Status: DISPATCH_READY

Date: 2026-08-11

Batch ID: ACRC-T2A

Risk ceiling: R2

Commit mode: WORKER_MUST_NOT_COMMIT

Dispatch base HEAD: `9c7d9cc637195e081f6f36a95cd2f6e4d2059c7d`

## Dispatch Prompt Envelope

```text
Role: worker/implementer; the independent reviewer/closer owns acceptance.
Canonical packet:
  docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_CONTINUITY_READ_COST_T2A_CORE_SURFACE_COMPACTION_2026-08-11.md
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: capture current git rev-parse HEAD before the first edit.
Current-time notes: T1 is closed and parked. T2A alone is authorized. T2B
  instruction-carrier compaction and T3 downstream migration remain parked.
Do-not-misread notes: AGENTS.md receives only the active-handoff pointer
  replacement. Do not broadly compact AGENTS.md, CLAUDE.md, or the downstream
  template. Preserve history in byte-identical archives before compaction.
Required first actions: read the bootstrap, this Work Order, the paired GC-018,
  current Core state sources, generator/checker sources, and current active
  surfaces; then verify hashes, execution HEAD, staged zero, and exact scope.
Return contract: COMPLETE_PENDING_INDEPENDENT_REVIEW or BLOCKED with exact-17,
  archive equality, state/hash binding, tests/gates, HEAD/staged state,
  no-commit, and zero-external-call evidence.
```

## Purpose

Implement T2A of the active-continuity read-cost roadmap. Preserve the current
oversized active surfaces as governed archives, replace them with compact
current-only surfaces, rotate the active handoff from V57 to V58, refresh the
generated state/bootstrap chain, bind current authority paths and hashes, and
remove the two exact migration-debt rows only after the new active surfaces
meet canonical budgets.

This Work Order does not authorize T2B instruction-carrier compaction or T3
downstream application work.

## Authority Chain

1. The operator selected `next` on 2026-08-11 following the accepted T1
   review and parked anchor `9c7d9cc63`.
2. The amended roadmap splits Core active-surface compaction into T2A and
   instruction-carrier compaction into T2B.
3. The paired GC-018 fixes the T2A risk, exact scope, and evidence boundary.
4. This Work Order is the only worker implementation authority for T2A.
5. The worker returns uncommitted evidence to an independent reviewer/closer.

Canonical sources:

- `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md`
- `docs/baselines/CVF_GC018_ACTIVE_CONTINUITY_READ_COST_T2A_CORE_SURFACE_COMPACTION_2026-08-11.md`
- `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md`
- archive-qualified contract-source exception:
  `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

## Agent Roles

- Dispatcher/Orchestrator: owns packet source fidelity and dispatch release.
- Worker/Implementer: owns only exact-17 implementation and evidence return.
- Independent reviewer/closer: owns semantic review, closure conversion,
  commit, continuity parking, and any later release.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake source | operator-selected tranche following accepted T1 review and parked anchor `9c7d9cc63` |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| scope classification | R2 protected governance-maintenance implementation |
| selected role route | dispatcher authors; separate worker implements; independent reviewer/closer accepts |
| Runtime/source modification | exact 17 repository paths only |
| External evidence intake | not authorized |
| Disposition | bounded no-commit T2A implementation |
| escalation condition | exact-17 expansion, archive mismatch, authority conflict, secret/provider/network/public/deploy effect, destructive history loss, or T2B/T3 entry |

## Scope

Allowed scope is exactly the 17 paths in `## Exact Changed Set`. Every other
path and all external effects are forbidden.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. this Work Order
3. the paired GC-018 baseline
4. `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md`
5. current `CVF_SESSION_MEMORY.md` and active V57 handoff
6. the exact source/checker files named in Source Verification

Read historical state only for a missing or contradictory current fact. The
archive copy operation requires raw bytes, not a narrative reread.

## Preflight Checks

Before any edit:

1. record `executionBaseHead` from `git rev-parse HEAD`;
2. verify staged paths are zero;
3. verify the roadmap, GC-018, and Work Order exist at the current HEAD;
4. recompute current SHA-256, line, and byte facts for the front door and V57;
5. verify all planned new paths are absent and no conflicting V58 exists;
6. verify the migration rows still match current active-surface bytes; and
7. verify the exact-17 scope can be maintained.

A failure returns `BLOCKED`; it is not authority to refresh a conflicting
source fact or add an eighteenth path.

## Write Ownership

The worker owns exact-17 edits and must not stage, commit, push, or alter any
other path. The reviewer/closer owns completion review, closure commit, and
post-acceptance session parking.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order coverage | Required evidence | Status |
|---|---|---|---|
| T2A compact Core front door | Required Behavior 1 | budget and archive equality | MAPPED |
| T2A rotate active handoff | Required Behavior 2 | root/archive/V58 name-status and pointers | MAPPED |
| refresh generated routing | Required Behavior 3 | generator/checker and drift evidence | MAPPED |
| bind current authority | Required Behavior 4 | positive and tamper tests | MAPPED |
| remove exact migration debt | Required Behavior 5 | registry state and zero read-budget violations | MAPPED |
| preserve governed history | Required Behavior 1-2 | byte-identical archive hashes | MAPPED |
| keep T2B separate | Scope Firewall Authorization | exact-17/no-eighteenth proof | MAPPED |
| keep T3 parked | Claim Boundary | state next move and no downstream diff | MAPPED |
| independent review before closure | Review Gate | completion review owned by closer | MAPPED |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: T1 closure proves the rule/checker foundation only.

priorVerificationAnchor: `9c7d9cc637195e081f6f36a95cd2f6e4d2059c7d`

freshRecomputeRequired: true

unicodePathHandling: use literal paths and UTF-8-safe readers; new authored
content remains ASCII.

extractedTextAuthority: repository bytes, generator output, and checker output.

## Worker Autonomy / No-Question Rule

Within exact-17, repair implementation, tests, packet shape, line/byte limits,
encoding, generated drift, and local gate failures without asking the operator.
Return to the Orchestrator only when a required fix needs an eighteenth path,
changes risk or external effect, loses history, consumes a secret/quota,
changes commit ownership, or enters T2B/T3.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must contain Status, Purpose, Scope / Methodology, Findings /
Position, Risk / Corrective Action, Claim Boundary, Checker Source Read-Ahead
Block, Agent Operation Trace Block, Delta Execution Claim Boundary Control
Block, Public Export Disposition, executionBaseHead, git status, exact changed
files, archive facts, tests, gates, file sizes, no-commit and zero-call
accounting. Conditional sections use `N/A with reason` when not applicable.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Verification class | Disposition |
|---|---|---|---|---|---|---|
| T2 owns Core front-door and active-handoff compaction | `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md` | section 9 | `T2` | active-continuity read-budget standard | VALUE_SET | ACCEPT |
| front-door budget is 120 lines and 20,480 bytes | `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md` | section 6 | `active front door` | active-continuity read-budget standard | LITERAL_INVARIANT | ACCEPT |
| active-handoff budget is 220 lines and 32,768 bytes | `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md` | section 6 | `active handoff` | active-continuity read-budget standard | LITERAL_INVARIANT | ACCEPT |
| current oversized surfaces are exact migration debt | `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json` | `entries` | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V57_2026-08-10.md` | migration registry schema | VALUE_SET | ACCEPT |
| active handoff and archive pointers are generated-state source fields | `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | lines 4, 35, 39-98 | `activeHandoff`; `supersededHandoffs` | active-session core source | EXISTS | ACCEPT |
| mode is a generated-state source field | `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | lines 100-101 | `currentMode` | active-session core source | EXISTS | ACCEPT |
| next move is an entry source | `CVF_SESSION/state/entries/nextAllowedMove.json` | complete object | `nextAllowedMove` | active-session entry source | EXISTS | ACCEPT |
| generator reads source layout and emits aggregate/bootstrap | `governance/compat/generate_active_session_state.py` | lines 16-37, 145-194 | `SOURCE_DIR`; `BOOTSTRAP_FIELDS`; `generate_bootstrap_read_model` | active-session generator | RUNTIME_BEHAVIOR | ACCEPT |
| generator validates aggregate against source fragments | `governance/compat/generate_active_session_state.py` | lines 196-216 | `validate_aggregate_matches_sources` | active-session generator | RUNTIME_BEHAVIOR | ACCEPT |
| active-session checker resolves handoff, required reads, and read budgets | `governance/compat/check_active_session_state.py` | lines 359-379, 470-560 | `_classify` | active-session compatibility gate | RUNTIME_BEHAVIOR | ACCEPT |
| root startup router names V57 | `AGENTS.md` | Session Memory Front Door | `AGENT_HANDOFF_V57_2026-08-10.md` | Core startup router | VALUE_SET | ACCEPT |
| current generator tests use isolated source fixtures | `governance/compat/test_generate_active_session_state.py` | test module | `generate_bootstrap_read_model` | generator proof owner | RUNTIME_BEHAVIOR | ACCEPT |

No source item is blocked. Newly introduced state fields and artifacts are
listed below rather than represented as existing source.

## New Output Fields And Files

| New item | Owner | Purpose |
|---|---|---|
| `currentAuthority` | active-session core schema and bootstrap generator | bind current baseline and Work Order paths plus SHA-256 |
| `active_continuity_read_cost_t2a_complete_pending_review` | active-session mode | prevent premature T2B/T3 entry |
| archive-rotation successor `AGENT_HANDOFF_V58_2026-08-11.md` | active continuity | compact current-only handoff |
| `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V57_2026-08-10.md` | archive | preserve V57 raw bytes |
| `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-08-11.md` | archive | preserve pre-compaction front-door raw bytes |
| `CVF_SESSION/state/entries/activeContinuityReadCostT2AImplementation20260811.json` | generated state source | record bounded T2A implementation transition |
| `governance/compat/test_active_continuity_t2a_authority.py` | test owner | isolate current-authority validation proof |
| `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2A_WORKER_RETURN_2026-08-11.md` | worker evidence | no-commit implementation return |

`currentAuthority` is an object with exactly `baselinePath`, `baselineSha256`,
`workOrderPath`, and `workOrderSha256`. Paths are repository-relative regular
files; hashes are lowercase 64-character SHA-256 values matching current raw
bytes. The generator must include the object in the bootstrap read model.

## Exact Changed Set

The worker may change exactly these 17 paths:

1. `AGENTS.md`
2. `AGENT_HANDOFF_V57_2026-08-10.md`
3. `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V57_2026-08-10.md`
4. archive-rotation successor `AGENT_HANDOFF_V58_2026-08-11.md`
5. `CVF_SESSION_MEMORY.md`
6. `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-08-11.md`
7. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
8. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
9. `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
10. `CVF_SESSION/state/entries/nextAllowedMove.json`
11. `CVF_SESSION/state/entries/activeContinuityReadCostT2AImplementation20260811.json`
12. `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`
13. `governance/compat/generate_active_session_state.py`
14. `governance/compat/test_generate_active_session_state.py`
15. `governance/compat/check_active_session_state.py`
16. `governance/compat/test_active_continuity_t2a_authority.py`
17. `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2A_WORKER_RETURN_2026-08-11.md`

The root V57 path is removed only through a move to its archive destination.
Both source and destination count in exact-17. No eighteenth path is
authorized.

## Required Behavior

### 1. Preserve and compact the front door

Before editing `CVF_SESSION_MEMORY.md`, copy its raw bytes to the named archive
path. The archive SHA-256 and byte count must equal the pre-edit source.

Replace the root front door with a current-only pointer record no larger than
120 lines and 20,480 bytes. It must identify current mode, active V58 handoff,
next allowed move, parked checkpoint, current authority paths, and targeted
archive/state lookup rules. Do not copy closed tranche narrative into it.

### 2. Rotate V57 to V58

Move root V57 to the named archive path without altering bytes. Create V58 as
the only active root handoff, no larger than 220 lines and 32,768 bytes. V58
contains current T2A facts, exact worker/reviewer boundary, current authority,
exact-17, and at most one archive-qualified predecessor pointer. It must not
carry the accumulated V57 history.

Update `AGENTS.md` only by replacing the active bare V57 filename with the
active bare V58 filename. No other `AGENTS.md` rewrite is authorized.

### 3. Refresh generated state and bootstrap

Edit state source fragments first. Set:

- current mode to `active_continuity_read_cost_t2a_complete_pending_review`;
- archive-rotation successor active handoff to `AGENT_HANDOFF_V58_2026-08-11.md`;
- session-memory archive to the new 2026-08-11 archive;
- V57 archive in `supersededHandoffs`;
- next move to independent T2A review/closure only; and
- T2B/T3 as parked checkpoints.

Add `currentAuthority` to the Core source and `BOOTSTRAP_FIELDS`. Generate both
aggregate and bootstrap with `generate_active_session_state.py`; do not hand
edit generated outputs independently. Aggregate/source/bootstrap drift is a
failure.

### 4. Enforce current authority freshness

Extend the existing active-session checker, not a parallel production checker.
It must fail closed when `currentAuthority`:

- is absent or not an object;
- has missing, extra, non-string, or empty fields;
- uses an absolute path, directory, escaping path, missing path, or symlink;
- has a malformed SHA-256; or
- does not match the raw bytes of either authority file.

Validation errors must remain safe typed checker violations; malformed values
must not escape as raw exceptions. Focused tests must cover one valid case and
each negative class above, including baseline and Work Order tampering.

### 5. Retire migration debt only after compliance

Remove both migration entries only after the new active front door and V58
pass their canonical line and byte limits. Keep the registry schema valid and
make the checker report zero read-budget violations. Do not retain a waiver for
a compliant surface and do not create a new debt row.

### 6. Worker return and stop

Create the worker-return artifact only after exact-17 source/tests/gates pass.
Return `COMPLETE_PENDING_INDEPENDENT_REVIEW`. If exact-17 cannot satisfy the
contract, return `BLOCKED` with source-backed reason and stop.

## Execution Plan

1. Run preflight and record immutable entry facts.
2. Create byte-identical archives before modifying active surfaces.
3. Rotate V57, author compact V58/front door, and update the single AGENTS
   pointer.
4. Update state fragments, generator, checker, and focused tests.
5. Generate aggregate/bootstrap and retire both exact debt rows.
6. Run focused and local governance gates.
7. Author the worker-return evidence, run its fast gate, and stop uncommitted.

## Evidence Requirements

Return command-backed evidence for:

- executionBaseHead and unchanged end HEAD;
- staged zero at entry and return;
- exact-17 name-status and no eighteenth path;
- before/source/archive/after SHA-256, lines, and bytes;
- archive raw-byte equality for V57 and the former front door;
- currentAuthority path/hash equality;
- generated-state and bootstrap equality with sources;
- migration registry disposition and zero read-budget violations;
- focused tests, file-size, encoding, archive, session, diff, and worker-return
  gates; and
- provider/network/live/browser/server/database/API/deployment/public-sync/
  push/commit counts all zero.

## Required Proof Manifest Atomic Literal Discipline

The return must contain one literal exact-17 manifest used unchanged for scope
comparison, evidence tables, and gate invocation. Do not reconstruct separate
lists from prose. Report `Expected manifest`, `Actual changed set`, and
`Manifest delta` as machine-comparable values.

## Core Guard Self-Protection Authorization

Protected paths:

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/activeContinuityReadCostT2AImplementation20260811.json`
- `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`
- `governance/compat/generate_active_session_state.py`
- `governance/compat/test_generate_active_session_state.py`
- `governance/compat/check_active_session_state.py`
- `governance/compat/test_active_continuity_t2a_authority.py`

Operator authorization: the operator authorized the next roadmap tranche on
2026-08-11 following accepted T1 review and requested that long active continuity/history
surfaces be reduced while irrelevant history stays out of current surfaces.

Authorized guard-maintenance scope: exact-17 Core active-continuity archive,
compaction, rotation, authority binding, generated routing, debt removal, and
focused proof only.

Rollback boundary: revert exact-17 only. Preserve both archives. Do not rewrite
other guard/runtime/history/provider/public/downstream paths.

## Scope Firewall Authorization

Allowed paths:

Dispatcher packet-authoring paths, excluded from worker exact-17 execution:

- `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md`
- `docs/baselines/CVF_GC018_ACTIVE_CONTINUITY_READ_COST_T2A_CORE_SURFACE_COMPACTION_2026-08-11.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_CONTINUITY_READ_COST_T2A_CORE_SURFACE_COMPACTION_2026-08-11.md`

Worker exact-17 paths:

- `AGENTS.md`
- `AGENT_HANDOFF_V57_2026-08-10.md`
- `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V57_2026-08-10.md`
- archive-rotation successor `AGENT_HANDOFF_V58_2026-08-11.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-08-11.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/activeContinuityReadCostT2AImplementation20260811.json`
- `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`
- `governance/compat/generate_active_session_state.py`
- `governance/compat/test_generate_active_session_state.py`
- `governance/compat/check_active_session_state.py`
- `governance/compat/test_active_continuity_t2a_authority.py`
- `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2A_WORKER_RETURN_2026-08-11.md`

Forbidden paths:

- `CLAUDE.md`
- `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
- dispatcher-owned roadmap and baseline artifacts
- all downstream repositories and public-sync clones
- every repository path outside exact-17

Operator authorization: exact-17 only; T2B and T3 remain parked.

Rollback boundary: revert only exact-17 if the implementation is rejected;
retain the original active-surface bytes through the two governed archives and
do not alter any forbidden path.

## Near-Threshold Owner Maintainability Plan

`governance/compat/check_active_session_state.py` must remain at or below its
hard Python-checker ceiling. If the bounded authority validator would approach
that ceiling, extract only the new same-domain helper into the already
authorized new focused test/implementation arrangement without adding a path;
otherwise return `BLOCKED`. Do not modify the near-threshold existing
`governance/compat/test_check_active_session_state.py`; put new proof in
`governance/compat/test_active_continuity_t2a_authority.py`.

The worker must report line counts for every touched Python and active Markdown
file and run governed Python/file-size enforcement.

## Verification Commands

Run at minimum:

1. focused generator and new authority tests;
2. `python governance/compat/generate_active_session_state.py --check`;
3. `python governance/compat/check_active_session_state.py --enforce --json`;
4. active archive hygiene and handoff-boundary checks;
5. governed file-size, Python-size, text-encoding, and Project Knowledge gates;
6. `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` before implementation evidence;
7. `python governance/compat/run_worker_return_fast_gate.py` for the exact test
   targets and worker return;
8. `git diff --check`, exact-17 scope, secret scan, HEAD, and staged-zero audit.

Run broader sanitized local tests only if the focused/local gate contract calls
for them. Do not run a live release bundle. No provider, network, live, browser,
Docker, PostgreSQL, deployment, public-sync, push, or downstream command is
authorized.

## Acceptance Criteria

- AC-01: pre-compaction V57 and front-door raw bytes are preserved in the
  exact archive paths.
- AC-02: active V58 and the compact front door meet both canonical budgets.
- AC-03: V58 is the only active root handoff and all current pointers agree.
- AC-04: currentAuthority is generated into bootstrap and binds both authority
  files by exact SHA-256.
- AC-05: malformed, missing, escaping, symlinked, absent, or tampered authority
  values fail closed without raw exception leakage.
- AC-06: both migration-debt rows are removed and zero budget violations remain.
- AC-07: generated source, aggregate, and bootstrap state are byte-consistent.
- AC-08: AGENTS has only the V57-to-V58 pointer replacement.
- AC-09: current mode stops at pending independent review; T2B/T3 remain parked.
- AC-10: exactly 17 paths change, HEAD is unchanged, and staged paths are zero.
- AC-11: all required focused/local gates pass and touched files meet size and
  encoding rules.
- AC-12: all external-effect and commit counts remain zero.

## Review Gate

An independent reviewer must inspect archive equivalence, compact-surface
semantics, authority validation, adversarial coverage, generated-state truth,
migration retirement, exact-17 containment, and boundaries. Green tests alone
are not acceptance.

## Closure Checklist

- [x] Roadmap trace is complete.
- [x] Source Verification Block is complete.
- [x] Exact changed set and forbidden scope are explicit.
- [x] Archive-preservation and budget semantics are explicit.
- [x] Worker return shape and no-commit rule are explicit.
- [x] Reviewer closure conversion is explicit.
- [x] Maintainability and external-effect boundaries are explicit.

Implementation and acceptance remain unresolved until independent review.

## Worker Return

Return exactly `COMPLETE_PENDING_INDEPENDENT_REVIEW` or `BLOCKED`.

Include executionBaseHead, exact-17 name-status/hashes, AC-01 through AC-12,
archive equivalence, currentAuthority evidence, before/after sizes, migration
state, focused/local gates, HEAD/staged state, no-commit and zero-call counts.
Stop after return.

## Return-To-Orchestrator Conditions

Return `BLOCKED` for authority/hash drift, archive mismatch, exact-17
insufficiency, unresolved in-scope gate failure, history-loss risk, secret or
quota need, destructive action, T2B/T3 dependency, or claim-boundary conflict.

## Execution Authority Waiver

operator.checkpoint.waiver: exact-17 T2A execution is authorized after this
dispatch packet passes pre-dispatch. Fresh operator authority is required for
scope expansion, T2B/T3, provider/live work, deployment, public sync, push,
deletion, or commit-mode change.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Binding |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher/orchestrator, separate no-commit worker, independent build reviewer/closer |
| phase | `T2A_DISPATCH`, `T2A_BUILD`, `T2A_REVIEW`, `T2A_CLOSURE_OR_BLOCK` |
| baseHeadFor(phase) | `dispatchBaseHead=9c7d9cc637195e081f6f36a95cd2f6e4d2059c7d`; worker records `executionBaseHead`; reviewer records `closureBaseHead` |
| changedSetScope(phase) | exact 17 T2A worker paths only |
| traceScope(phase, actor) | dispatcher covers packet; worker covers exact-17; reviewer covers semantic review and closure only |
| commitOwner(phase) | independent reviewer/closer after PASS |
| crossBatchIsolation | T2B instruction carriers, T3 downstream, and all other batches remain parked |
| nextMoveSurfaces | worker updates exact authorized current surfaces to pending independent review only |

Designated closer: `INDEPENDENT_BUILD_REVIEWER_CLOSER`.

## Reviewer Closure Conversion

- completionReviewPath:
  `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2A_COMPLETION_REVIEW_2026-08-11.md`
- reviewerOwnedClosurePaths: completion review, accepted exact-17 commit, and
  later bounded continuity parking only
- worker commit disposition: `WORKER_MUST_NOT_COMMIT`
- session-sync disposition: worker stops at pending review; closer owns closure

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_active_session_state.py`; `governance/compat/generate_active_session_state.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_active_archive_hygiene.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `MULTI_AGENT_MULTI_ROLE`; `WORKER_RETURN_FULL_GATE_V1`; `Core Guard Self-Protection Authorization`; `Expected manifest`; `Actual changed set`; `Manifest delta`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirmation and evidence after direct source verification |
| claimBoundary | packet form and exact-17 output contract only |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACRC-T2A --title "Active Continuity Core Surface Compaction And V58 Rotation" --date 2026-08-11 --base 9c7d9cc637195e081f6f36a95cd2f6e4d2059c7d --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact archive/rotation, authority binding, generated-state, debt-removal, maintainability, and tranche-isolation requirements |
| checkerReadAheadConfirmation | applicable checker constants and sections were read before authoring |
| docOnlyNewFields | `currentAuthority`; `active_continuity_read_cost_t2a_complete_pending_review` |
| claimBoundary | dispatch provenance only |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing root active surfaces, governed session source/archive roots, and governance compatibility root |
| Storage decision | reuse existing layout; add one V58, two archives, one state entry, one test, and one worker return |
| Existing aggregate impact | active-session aggregate and bootstrap are generator-owned outputs |
| Generated state impact | source-first edit followed by generator/check drift proof |
| Durable governance boundary | archives retain history; active surfaces retain current routing only |

## Commit Mode And Base-Anchor Lifecycle

| Field | Binding |
|---|---|
| commitMode | `WORKER_MUST_NOT_COMMIT` |
| dispatchBaseHead | `9c7d9cc637195e081f6f36a95cd2f6e4d2059c7d` |
| executionBaseHead | worker captures current HEAD immediately before edits |
| closureBaseHead | reviewer captures after worker return before acceptance |
| commitOwner | independent reviewer/closer only after PASS |
| stale-anchor action | return `BLOCKED`; do not rewrite authority from chat history |

## Negative Search And Collision Discipline

Exact path existence checks before packet authoring confirmed that V58, both
archive destinations, the new state entry, new focused test, worker return,
GC-018, and this Work Order had no conflicting pre-existing T2A artifact. The
worker must repeat collision checks from executionBaseHead before writing.

## Provider Memory Authority Boundary

`CLAUDE.md`, Codex memory, Claude memory, IDE summaries, and chat history are
NOT_CVF_SOURCE. They may guide the owning agent only. Every execution fact must
be reverified against this Work Order, the paired GC-018, canonical standards,
state sources, active surfaces, runtime source, or command evidence.

## Legacy Absorption Coverage Index Disposition

N/A with reason: T2A compacts active continuity carriers and changes no legacy
absorption, foundation-plane, provider, memory-runtime, scan, corpus, or
workflow-chain feature contract.

rawMemoryReleased=false

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | N/A with reason: no knowledge is ingested; the section is present because the legacy-coverage disposition is explicitly recorded |
| Matching local-view guard | N/A with reason: T2A changes continuity routing only |
| Owner surface | active-continuity T2A Work Order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no external source, returned output, corpus, provider, or public artifact is consumed |

## Export Surface Decision

No export surface changes. Private provenance continuity maintenance only.

## Next-Tranche Audit Mini-Package

T2B remains a separate future GC-018/Work Order for `AGENTS.md`, `CLAUDE.md`,
and the downstream instruction template. It may start only after T2A closure
and fresh operator selection. T3 remains parked until its own release.

## Dispatch Packet Authoring Learning Promotion

No new repeated machine-gate defect pattern was found during packet authoring.
The T2A/T2B split records the scope lesson directly in the roadmap: compact
active continuity first, then separately compact instruction carriers with a
checker-binding matrix.

## Work-Order Fulfillment Manifest

| Requirement | Owning section | Worker evidence |
|---|---|---|
| exact scope | Exact Changed Set | exact-17 name-status and delta |
| history preservation | Required Behavior 1-2 | archive equality hashes |
| budgets | Required Behavior 1-2 | line/byte facts and active checker |
| authority freshness | Required Behavior 3-4 | source/bootstrap/hash tests |
| debt removal | Required Behavior 5 | registry and zero violations |
| generated-state truth | Required Behavior 3 | generator check |
| maintainability | Near-Threshold Owner Maintainability Plan | size gates |
| no external effect | Claim Boundary | zero-call accounting |
| independent acceptance | Review Gate | reviewer completion packet |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds: NONE_RETURNED

Returned defects: NONE_RETURNED

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | compact Core bootstrap/front door/V58 | repository-local R2 continuity routing only | archives, state, source, focused/local gates | local filesystem reads | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no CLI/MCP runtime or external invocation | zero-call accounting | no adapter | `N/A_WITH_REASON` |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher / work-order author |
| Provider or surface | local CVF Core workspace |
| Session or invocation | active-continuity T2A dispatch authoring, 2026-08-11 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | repository reads, source search, hashes/sizes, patch authoring, local gates |
| Target paths | roadmap, paired GC-018, and this Work Order |
| Allowed scope source | operator `next` selection following accepted T1 review and parked anchor `9c7d9cc63` |
| Before status evidence | clean worktree and staged zero at base HEAD `9c7d9cc637195e081f6f36a95cd2f6e4d2059c7d` |
| After status evidence | roadmap, GC-018, and Work Order only; staged zero |
| Diff evidence | `git status --short`, `git diff --name-status`, hashes, and authoring gates |
| Approval boundary | packet authoring and exact-17 dispatch only |
| Claim boundary | no implementation, provider/network/live/public/deploy action, commit, or push |
| Agent type | dispatcher |
| Invocation ID | `active-continuity-read-cost-t2a-dispatch-2026-08-11` |
| Expected manifest | roadmap, GC-018, and this Work Order |
| Actual changed set | roadmap, GC-018, and this Work Order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: dispatch authoring deletes or renames nothing |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | repository-local active-continuity archive, compaction, generated routing, and compatibility validation |
| claimDisposition | N/A with reason: no universal execution-control claim |
| receiptEvidence | N/A with reason: no runtime governance receipt claim |
| actionEvidence | N/A with reason: local archive/source/test changes are not runtime action proof |
| invocationBoundary | local worker shell and Python invocation |
| interceptionBoundary | no IDE, shell, git, provider, network, or external-service interception claim |
| claimLanguage | bounded Core startup read-cost and authority-freshness maintenance |
| forbiddenExpansion | T2B/T3, runtime/provider control, downstream mutation, deployment, public sync, push, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T2A is private provenance continuity maintenance. Public sync is
outside worker and reviewer authority for this tranche.

## Claim Boundary

T2A may produce a compact, current-only Core bootstrap/front door/V58 chain,
preserved archives, exact current-authority hash validation, and retired
read-budget migration debt. It does not compact broad instruction carriers,
change provider/runtime behavior, modify a downstream project, call a service,
deploy, publish, push, or complete LPCI1/shift-operations development.
