# CVF Active Continuity Read-Cost T1 Amendment 1

Memory class: ACTIVE_WORK_ORDER

Status: HOLD_UNTIL_POST_AUTHORITY_S2_PASS

Date: 2026-08-10

Risk ceiling: R2

Commit mode: WORKER_MUST_NOT_COMMIT

Dispatch base HEAD: `b751bc8a3e5d231ce1968afc4d9c1129715709d6`

Repair input base HEAD: `c6bef41ccb2e2543c93480f4e97ac13ff444046e`

Worker execution HEAD: capture the dedicated post-authority session-sync
release HEAD named by the active handoff before the first worker edit.

## Dispatch Prompt Envelope

```text
Role: repair worker; an independent reviewer/closer owns acceptance.
Canonical packet: docs/work_orders/CVF_ACTIVE_CONTINUITY_READ_COST_T1_AMENDMENT_1_2026-08-10.md.
Commit mode: WORKER_MUST_NOT_COMMIT.
dispatchBaseHead: b751bc8a3e5d231ce1968afc4d9c1129715709d6
executionBaseHead: capture the current dedicated release-sync HEAD; retain
  c6bef41ccb2e2543c93480f4e97ac13ff444046e as repairInputBaseHead only.
Current-time notes: preserve the existing dirty exact-seven repair; add only
  the authorized helper as path eight; no session-sync or external effect.
Do-not-misread notes: this amendment repairs size and strict-validation
  blockers; it does not open T2, T3, current continuity compaction, or runtime.
Required first actions: verify the authority hashes, HEAD, staged zero, current
  exact-seven hashes, protected path set, and the no-ninth-path boundary.
Return contract: COMPLETE_PENDING_INDEPENDENT_REVIEW or BLOCKED with exact-eight
  manifest, tests, gates, file facts, staged zero, no commit, and zero calls.
```

## Purpose

Amend the already-authorized T1 worker scope only enough to close two
source-proven repair blockers:

1. extract the read-budget domain and validation logic into one new pure helper
   so the active-session checker satisfies its `python_checker` hard ceiling;
2. permit a bounded pointer compaction of exactly two `AGENTS.md` history-heavy
   sections so the touched root router satisfies GC-023 near-hard shrink.

All original T1 behavior remains binding except where this amendment expressly
replaces exact-seven, the original `AGENTS.md` no-compaction instruction, and
the original single-file checker implementation shape.

## Authority Chain

1. Operator token on 2026-08-10:
   `AUTHORIZE_CVF_ACTIVE_CONTINUITY_T1_AMENDMENT_1_EXACT8`.
2. Parent roadmap at commit `c6bef41ccb2e2543c93480f4e97ac13ff444046e`:
   `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md`,
   canonical LF SHA-256
   `6e5b66d50aa40012274d06df4e042bb4c728cd72d65b24e3ddd7b36faaad0fbd`.
3. Parent Work Order at the same commit:
   `docs/work_orders/CVF_ACTIVE_CONTINUITY_READ_COST_T1_WORK_ORDER_2026-08-10.md`,
   canonical LF SHA-256
   `49a9b1f50b444b9a3ca088d0f0d4218675f4602cc5f0aa89f22583416b3cf51b`.
4. Parent authorization review:
   `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T1_WORK_ORDER_AUTHORIZATION_REVIEW_2026-08-10.md`,
   canonical LF SHA-256
   `7e7873d9f3dd8499ba7cd5b75be253855542b0498272c166c49713fab1a99ace`.
5. This amendment and its independent authorization review become the latest
   worker authority after review PASS.

This Amendment remains dependency-held until the post-authority S2 session
release passes independent review. The governed S2 state entry is the separate
release artifact that changes this held authority into an executable dispatch;
the worker must not start from S1.

Canonical LF SHA-256 means SHA-256 of the Git blob bytes at the pinned commit,
not checkout bytes transformed by `core.autocrlf`.

## Agent Roles

- Dispatcher authors the amendment and prepares dispatch evidence.
- Independent amendment reviewer authorizes or rejects dispatch.
- Separate repair worker edits the exact-eight set without committing.
- Independent build reviewer/closer accepts, returns, or closes the repair.
- Session-sync steward owns any later V57 continuity repair separately.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake source | operator exact-eight authority after worker `BLOCKED_SIZE_SCOPE` |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| scope classification | R2 protected governance-maintenance repair |
| risk sensitivity | protected Core router and compatibility checker; fail closed at R2 |
| selected role route | dispatcher, independent authorization reviewer, separate no-commit worker, independent build reviewer/closer |
| Runtime/source modification | exact eight paths only |
| External evidence intake | not authorized |
| Disposition | exact-eight repair after authorization review PASS |
| escalation condition | ninth path, exception-registry edit, session-sync, external effect, deletion, or claim expansion |

## Scope

Allowed scope is exactly the eight paths in `## Exact Changed Set`. Existing
dirty T1 work is repair input and must not be reset, stashed, discarded, or
recreated from the base commit. Every other path is read-only.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. the parent Work Order
3. the parent authorization review
4. this amendment
5. this amendment's authorization review
6. the eight authorized paths
7. the checker sources in `## Checker Source Read-Ahead Block`

Full historical continuity is not a startup prerequisite. Targeted lookup is
allowed only when one of these current authority surfaces lacks a needed fact.

## Preflight Checks

Before editing, verify:

- current HEAD is the dedicated post-authority session-sync release commit
  named by the active handoff;
- `c6bef41ccb2e2543c93480f4e97ac13ff444046e` is an ancestor and remains the
  repair-input comparison base, not the current execution HEAD;
- staged path count is zero;
- the existing dirty set is exactly the original seven paths;
- the seven working-file hashes match `## Repair Input Manifest`;
- the authority artifacts match their canonical Git-blob hashes;
- no session, handoff, downstream, exception-registry, hook, or public path is
  dirty.

A mismatch returns `BLOCKED` without cleanup or destructive recovery.

## Write Ownership

The worker owns only exact-eight implementation edits and must not commit. The
reviewer/closer owns acceptance and any material commit. The session-sync
steward owns later generated state, V57, and next-move synchronization.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Amendment coverage | Evidence | Status |
|---|---|---|---|
| T1 canonical read-budget standard | retained from parent Work Order | standard diff and tests | MAPPED |
| T1 machine enforcement | helper extraction plus checker integration | focused tests and source review | MAPPED |
| Core progressive startup | retained plus bounded router pointer compaction | `AGENTS.md` diff and guard pass | MAPPED |
| future downstream startup | retained from original exact-seven | template diff and tests | MAPPED |
| current debt cannot grow | strict equality repair | registry tests and current-byte validation | MAPPED |
| maintainable governed files | checker/helper/test ceilings and router shrink | size gates | MAPPED |
| no T2/T3 execution | exact-eight and claim boundary | name-status evidence | MAPPED |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: parent T1 Work Order, parent authorization review,
and repair-round source findings.

priorVerificationAnchor: `c6bef41ccb2e2543c93480f4e97ac13ff444046e`.

freshRecomputeRequired: true

unicodePathHandling: use literal repository-relative paths and UTF-8-safe
readers; newly authored content remains ASCII.

extractedTextAuthority: current repository bytes, Git blob bytes, source
symbols, and local checker output only.

## Worker Autonomy / No-Question Rule

Inside exact-eight scope, repair source, tests, semantics, line count, encoding,
and local gate failures and rerun focused checks without asking the operator.
Return `BLOCKED` only when closure requires a ninth path, a file-size exception,
session-sync authority, destructive action, secrets/quota, an external effect,
or a contradiction in this authority packet.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must contain Status, Purpose, Scope / Methodology, Findings /
Position, Risk / Corrective Action, Claim Boundary, Checker Source Read-Ahead
Block, Agent Operation Trace Block, Delta Execution Claim Boundary Control
Block, Public Export Disposition, executionBaseHead, git status, exact changed
files, tests, gates, file sizes, no-commit evidence, and zero-call accounting.
Conditional sections use `N/A with reason` when they do not apply.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Verification class | Disposition |
|---|---|---|---|---|---|---|
| Root agent router is 1171 lines at repair-input base | `AGENTS.md` | complete base file at `c6bef41...` | `AGENTS.md` | Core startup router | VALUE_SET | ACCEPT |
| GC-023 requires at least 50 lines of shrink for a touched active markdown file within 25 lines of hard 1200 | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | Rule and File Classes And Thresholds | `active_markdown` | governed file-size guard | LITERAL_INVARIANT | ACCEPT |
| F-1 details already have canonical review and roadmap owners | `AGENTS.md` | Mandatory F-1 Diminishing Returns Stop Rule | `Mandatory F-1 Diminishing Returns Stop Rule` | Core startup router | EXISTS | ACCEPT |
| legacy continuation detail already points to versioned roadmap owners | `AGENTS.md` | Latest Closed Continuation Roadmap | `Latest Closed Continuation Roadmap` | Core startup router | EXISTS | ACCEPT |
| active-session checker is a `python_checker` with hard 1000 lines | `governance/compat/check_python_automation_size.py` | `CLASS_THRESHOLDS` | `python_checker` | Python automation size gate | LITERAL_INVARIANT | ACCEPT |
| non-check/test helper in compat is `python_library_helper` with hard 900 lines | `governance/compat/check_python_automation_size.py` | `_classify` and `CLASS_THRESHOLDS` | `python_library_helper` | Python automation size gate | LITERAL_INVARIANT | ACCEPT |
| active-session tests are `python_test` with hard 1200 lines | `governance/compat/check_python_automation_size.py` | `_classify` and `CLASS_THRESHOLDS` | `python_test` | Python automation size gate | LITERAL_INVARIANT | ACCEPT |
| migration validation currently accepts approved maxima above current facts | `governance/compat/check_active_session_state.py` | `_validate_migration_entry` | `approvedMaxLines`; `approvedMaxBytes` | read-budget migration validator | RUNTIME_BEHAVIOR | ACCEPT |
| surface waiver check currently uses greater-than-or-equal maxima | `governance/compat/check_active_session_state.py` | `_check_surface_read_budget` | `approvedMaxLines`; `approvedMaxBytes` | read-budget surface checker | RUNTIME_BEHAVIOR | ACCEPT |
| active session and handoff continuity remain session-sync-owned | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `activeHandoff` and current-mode fields | `AGENT_HANDOFF_V57_2026-08-10.md` | generated active state | VALUE_SET | ACCEPT |

No source item is blocked. The helper below is new and is not represented as
an existing runtime symbol.

## New Doc-Only Fields And Files

| New item | Classification | Owner | Purpose |
|---|---|---|---|
| `governance/compat/active_continuity_read_budget.py` | DOC_ONLY_NEW | active-session checker | pure constants, parsing, validation, budget, and wording functions extracted from the existing checker |

The helper is repository-local governance automation. It is not a provider,
API, state-schema, route, product runtime, or external-agent adapter.

## Repair Input Manifest

These are the expected raw working-file SHA-256 values before exact-eight work:

| Path | SHA-256 | Lines | Bytes |
|---|---|---:|---:|
| `AGENTS.md` | `d8a1618ce4d34354213b5c2d99c51cf804c1b203227ebe4981cdb4620dce5834` | 1185 | 65810 |
| `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md` | `b2117b33c105d4ce92f3647968c90a567a0a7a890ae1412c1dee40e1845137d0` | 133 | 6115 |
| `governance/toolkit/05_OPERATION/CVF_SESSION_GOVERNANCE_BOOTSTRAP_GUARD.md` | `b8aaf74b625385936ae7863f2ac8fa4692fa17b8fce51e5ef7621be9de4522c6` | 130 | 5654 |
| `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | `7f545fa243754cd3066f3b4264959f4b7f9bd3fa2f348bd1b99cc21483e34a74` | 262 | 12374 |
| `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json` | `a062afc4c2ce586dd9cd871a827c8d60ac75c6d7e78847a047c4e716fc4cffd1` | 30 | 882 |
| `governance/compat/check_active_session_state.py` | `874c7355843d8db0d1eb6ea608b67c93f455928df9431881beda971a632f58e7` | 1150 | 49325 |
| `governance/compat/test_check_active_session_state.py` | `73b76481eb8f573cda8e3fdf635237f6e7ed7e0f5a94bc396d96dd801eb4bd83` | 1138 | 53366 |

Line and byte counts use current raw checkout bytes. A line-ending-only change
that invalidates a listed hash is authority drift and returns `BLOCKED`.

## Exact Changed Set

The worker may edit exactly these eight paths:

1. `AGENTS.md`
2. `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md`
3. `governance/toolkit/05_OPERATION/CVF_SESSION_GOVERNANCE_BOOTSTRAP_GUARD.md`
4. `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
5. `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`
6. `governance/compat/active_continuity_read_budget.py`
7. `governance/compat/check_active_session_state.py`
8. `governance/compat/test_check_active_session_state.py`

The list contains eight paths. No ninth implementation path is authorized.

This amendment and its authorization review are dispatcher/reviewer authority
artifacts already committed before worker re-entry and are not worker changes.

## Required Repair Behavior

### Exact helper extraction

- Move cohesive read-budget constants and pure parsing/validation/wording logic
  from `check_active_session_state.py` into
  `active_continuity_read_budget.py`.
- Keep repository traversal, report assembly, existing checker CLI, exit codes,
  and integration ownership in `check_active_session_state.py`.
- Use an explicit import; do not load the helper dynamically.
- Do not create a second checker, hook, registry, CLI, package, or test file.
- Preserve all pre-existing active-session checks and report fields.

### Strict migration equality

- `approvedMaxLines` must be a strict integer equal to `lineCount` and current
  raw line count.
- `approvedMaxBytes` must be a strict integer equal to `byteCount` and current
  raw byte count.
- Greater, smaller, boolean, string, null, missing, duplicate, unknown, or
  malformed values fail closed.
- Both registry validation and surface-waiver consumption enforce equality.
- Replace permissive test expectations with exact-equality positive and N+1
  negative proofs.

### Bounded `AGENTS.md` shrink

Relative to execution-base `AGENTS.md` at 1171 lines, final `AGENTS.md` must be
at most 1121 lines. This is a minimum 50-line shrink, not wording compression
merely to stay below 1200.

The worker may compact exactly these two sections:

1. `Mandatory F-1 Diminishing Returns Stop Rule - 2026-05-15`
2. `Latest Closed Continuation Roadmap`

For the F-1 section, retain in `AGENTS.md`:

- final status `closed: not met, evidence-backed`;
- no broad F-1 tuning, token-cap increase, two-pass reintroduction, or
  hope-based EVT-4 rerun;
- pointers to the canonical stop-rule, closure, bounded-value, and successor
  roadmap artifacts already named in the base section;
- fresh human authority requirement for reopening broad F-1 work.

For the continuation-roadmap section, retain in `AGENTS.md`:

- pointers to the W132 and W131 roadmaps already named in the base section;
- W133 requires fresh GC-018 and roadmap authority before implementation;
- no claim expansion beyond the canonical versioned roadmap/review owners;
- current high-level boundary that Web governance inheritance is bounded and
  future work must not overstate it.

Do not copy the removed history into a new ninth file. The existing versioned
reviews and roadmaps remain the detail owners. Do not compact any other
`AGENTS.md` section in this repair.

### Retained semantic and adversarial proof

Retain and pass all previously repaired T1 behaviors, including:

- strict top-level JSON object and exact field-set validation;
- exact `schemaVersion`, status, removal action, and valid ISO date;
- raw `requiredFirstReads` cardinality/type checking before string filtering;
- correct imperative full-read detection and correct negation handling;
- exact line and byte N+1 tests for bootstrap, front door, and handoff;
- no mutation of real continuity fixtures;
- progressive targeted-read positive wording;
- unchanged downstream non-blocking bootstrap fallback.

### File ceilings

- `AGENTS.md`: at most 1121 lines.
- `governance/compat/check_active_session_state.py`: at most 1000 lines.
- `governance/compat/active_continuity_read_budget.py`: at most 900 lines.
- `governance/compat/test_check_active_session_state.py`: at most 1200 lines.
- All other exact-eight files must pass their applicable governed size guard.
- No file-size exception or exception-registry edit is authorized.
- Do not make tests unreadable merely to reduce line count.

## Parent-Owned Continuity Release Dependency

Before worker entry, the parent orchestrator must complete both dedicated
session-sync commits: one before the Amendment authority commit and one after
it. The final active handoff must name the Amendment authority parent and route
only to this exact-eight repair. The worker captures that final session-sync
HEAD as `executionBaseHead`.

The worker must not edit state sources, generated state, session memory,
bootstrap, V57, or any successor handoff. A missing or stale final release sync
returns `BLOCKED_PARENT_SESSION_SYNC`; do not weaken or suppress the checker.

## Execution Plan

1. Verify preflight facts without altering the dirty repair input.
2. Add the pure helper and extract only cohesive read-budget logic.
3. Repair strict migration equality in helper/checker integration and tests.
4. Compact only the two authorized `AGENTS.md` sections to canonical pointers.
5. Run focused semantic and size checks, then the single sanitized broad suite.
6. Return exact-eight evidence without staging, committing, or synchronizing
   continuity.

## Evidence Requirements

Return command-backed evidence for execution HEAD, exact-eight name-status and
hashes, all final line/byte counts, strict-equality probes, focused and broad
tests, applicable gates, `git diff --check`, staged zero, no commit, no ninth
path, and zero external calls. Record the parent-owned V57 failure separately
from in-scope implementation results.

## Verification Commands

Run in this order with provider/live key variables removed from the test
process environment:

1. focused `test_check_active_session_state.py` suite;
2. `python governance/compat/check_python_automation_size.py --enforce`;
3. `python governance/compat/check_governed_file_size.py --enforce`;
4. active-session checker enforcement, recording the parent-owned V57 result;
5. text encoding, guard self-protection, exact-scope checks, and
   `python governance/compat/run_worker_return_fast_gate.py` against the return
   packet and focused test target;
6. full sanitized non-live Python suite once, serially, after focused PASS;
7. `git diff --check`, exact-eight name-status/hash manifest, secret scan,
   staged-zero audit, and no-ninth-path proof.

No doctor, fetch, provider, network, browser, live, Docker, PostgreSQL,
deployment, public-sync, push, downstream mutation, deletion, or commit is
authorized.

## Acceptance Criteria

- AC-01: exact helper extraction leaves checker CLI/report behavior intact.
- AC-02: checker is at most 1000 lines and helper is at most 900 lines.
- AC-03: test owner is at most 1200 lines without meaning-obscuring compaction.
- AC-04: final `AGENTS.md` is at most 1121 lines and only the two named history
  sections receive pointer compaction beyond retained T1 startup edits.
- AC-05: approved maxima equal current facts exactly; all non-equal values fail.
- AC-06: all retained semantic and boundary tests pass.
- AC-07: exact-eight paths are dirty and no ninth implementation path changes.
- AC-08: no exception registry, session-sync, downstream, runtime, provider,
  public, deployment, or external-effect path changes.
- AC-09: HEAD remains the worker execution base, staged count is zero, and the
  worker made no commit.

## Review Gate

An independent reviewer must inspect extraction boundaries, strict-equality
semantics, exact `AGENTS.md` pointer content, adversarial proof, file sizes, and
exact-eight/no-ninth containment. Green tests alone are not acceptance.

## Closure Checklist

- [x] Operator exact-eight authority is recorded.
- [x] Parent roadmap and Work Order trace is retained.
- [x] Source Verification Block separates existing facts from the new helper.
- [x] Exact-eight and no-ninth boundaries are explicit.
- [x] Both size blockers have deterministic acceptance thresholds.
- [x] Strict migration equality and retained proof are explicit.
- [x] Parent-owned session-sync remains outside worker scope.
- [x] Worker no-commit and reviewer closure ownership remain explicit.

This checklist covers dispatch completeness. Implementation remains pending
independent build review.

## Worker Return

Return exactly `COMPLETE_PENDING_INDEPENDENT_REVIEW` or `BLOCKED`.

Include execution HEAD, exact-eight name-status and hashes, AC-01 through AC-09
matrix, focused/full tests, gate results, strict-equality probes, final file
lines/bytes, `AGENTS.md` section diff, parent-owned session result, staged zero,
no commit, zero-call accounting, and claim boundary.

Stop after return. Do not stage, commit, push, sync continuity, or begin T2/T3.

## Return-To-Orchestrator Conditions

Return `BLOCKED` for authority/hash drift, a required ninth path, a needed
exception-registry edit, a non-parent in-scope failure that cannot be repaired
inside exact eight, secrets/quota need, destructive action, external effect, or
contradiction in this packet.

## Execution Authority Waiver

operator.checkpoint.waiver: exact-eight repair is authorized by the operator
token in this amendment. Fresh operator authority is mandatory for a ninth
path, exception registry, T2/T3, session-sync, provider/live, deployment,
public-sync, push, deletion, or commit-mode change.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Binding |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher, independent amendment reviewer, separate no-commit repair worker, independent build reviewer/closer, later session-sync steward |
| phase | `T1_AMENDMENT`, `T1_REPAIR`, `T1_REVIEW`, `T1_CLOSURE_OR_BLOCK` |
| baseHeadFor(phase) | `dispatchBaseHead=b751bc8a3e5d231ce1968afc4d9c1129715709d6`; `repairInputBaseHead=c6bef41ccb2e2543c93480f4e97ac13ff444046e`; worker captures the dedicated post-authority session-sync `executionBaseHead`; reviewer records `closureBaseHead` |
| changedSetScope(phase) | worker exact eight only; authority artifacts are pre-committed dispatcher/reviewer paths |
| traceScope(phase, actor) | dispatcher traces authority; worker traces exact-eight repair; reviewer traces acceptance; steward separately traces session-sync |
| commitOwner(phase) | reviewer/closer after semantic acceptance; worker must not commit |
| crossBatchIsolation | T2, T3, downstream migration, session-sync, provider/live, and public-sync remain separate |
| nextMoveSurfaces | unchanged during repair worker execution |

Designated closer: `INDEPENDENT_BUILD_REVIEWER_CLOSER`.

## Reviewer Closure Conversion

- completionReviewPath:
  `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T1_COMPLETION_REVIEW_2026-08-10.md`
- reviewerOwnedClosurePaths: completion review and accepted material commit only
- worker commit disposition: `WORKER_MUST_NOT_COMMIT`
- session-sync disposition: separate parent-owned batch after material review

## Commit Prompt Readiness

Commit owner: independent reviewer/closer only after semantic PASS.

Commit scope: accepted exact-eight material paths plus a reviewer-owned
completion review when required by the closure gate. Session-sync paths must be
a later separate commit.

Worker commit: FORBIDDEN.

Push: FORBIDDEN.

## Core Guard Self-Protection Authorization

Protected paths authorized for the worker:

- `AGENTS.md`
- `governance/toolkit/05_OPERATION/CVF_SESSION_GOVERNANCE_BOOTSTRAP_GUARD.md`
- `governance/compat/active_continuity_read_budget.py`
- `governance/compat/check_active_session_state.py`
- `governance/compat/test_check_active_session_state.py`

Operator authorization: exact token
`AUTHORIZE_CVF_ACTIVE_CONTINUITY_T1_AMENDMENT_1_EXACT8` on 2026-08-10.

Authorized guard-maintenance scope: progressive-read T1 semantic repair,
strict migration equality, pure-helper extraction, and bounded compaction of
the two named `AGENTS.md` historical sections.

Rollback boundary: revert only exact-eight implementation edits if rejected.
Do not delete history, mutate exception registries, rewrite session state,
modify archived handoffs, or change public/downstream/runtime/provider state.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_active_session_state.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | `## Dispatch Prompt Envelope`, `## Source Verification Block`, `## Core Guard Self-Protection Authorization`, `## Agent Handoff Contract Control Block`, `## Reviewer Closure Conversion`, `## Commit Prompt Readiness`, `## Checker Source Read-Ahead Block`, `## Delta Execution Claim Boundary Control Block`, `## Foundation Storage Layout Block`, `## Scaffold Provenance Block` |
| gateRunPurpose | confirm source-verified amendment shape and exact-eight authority before dispatch |
| claimBoundary | read-ahead covers this amendment and its no-commit repair contract only |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | `WORK_ORDER` |
| generatedSkeletonStatus | `NOT_USED_WITH_REASON` |
| manualEditsAfterScaffold | amendment was authored from the accepted parent packet and current checker literals |
| checkerReadAheadConfirmation | checker sources were inspected before authoring; gates are confirmation evidence |
| docOnlyNewFields | one new helper path is listed separately as `DOC_ONLY_NEW` |
| claimBoundary | no claim that the helper generated this amendment |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing `governance/compat/` pure-helper ownership beside its checker |
| Storage decision | add one same-domain helper; no new directory, package, hook, registry, or parallel checker |
| Existing aggregate impact | none |
| Generated state impact | none during worker repair |
| Durable governance boundary | helper owns pure read-budget logic; checker retains CLI/report/integration ownership |

## Legacy Absorption Coverage Index Disposition

`NOT_APPLICABLE_WITH_REASON`

Reason: this amendment extracts current first-party checker logic into a
same-owner helper. It does not intake, enumerate, absorb, or claim coverage of
a legacy or external repository corpus.

## External Knowledge Intake Routing

| Field | Decision |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Operator-provided external comparison, critique, or recommendation |
| Chain map route | operator input -> CVF-governed source re-verification -> bounded first-party Work Order amendment |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | this amendment and the parent T1 roadmap/Work Order |
| Disposition | `N/A_WITH_REASON`: the operator supplied scope authority, not an external corpus or factual source |
| Claim boundary | no external repository, copied corpus, provider memory, or third-party authority is consumed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | repository-local startup instructions and compatibility checking |
| claimDisposition | N/A with reason: no universal execution-control claim is made |
| receiptEvidence | N/A with reason: T1 creates no runtime receipt |
| actionEvidence | N/A with reason: evidence is local source, test, and gate output |
| invocationBoundary | local worker shell and Python test/checker invocation |
| interceptionBoundary | no IDE, shell, git, provider, network, or runtime interception claim |
| claimLanguage | bounded progressive-read routing and repository-local fail-closed checks |
| forbiddenExpansion | runtime/provider control, universal agent control, deployment, public-sync, push, or production-readiness claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds:

- `ADIF-0001`
- `ADIF-0002`
- `ADIF-0014`
- `ADIF-0015`
- `ADIF-0020`
- `ADIF-0021`
- `ADIF-0028`
- `ADIF-0029`
- `ADIF-0033`
- `ADIF-0044`

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | Core/downstream startup instructions and local checker/helper | repository-local R2 governance maintenance only | source, tests, and local gates | filesystem continuity reads only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | generated downstream AGENTS instructions | no CLI/MCP runtime or external invocation added | template and checker evidence only | no runtime adapter | `N/A_WITH_REASON` |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher / amendment author role |
| Provider or surface | isolated local CVF Core authority worktree |
| Session or invocation | active-continuity T1 Amendment 1, 2026-08-10 |
| Working directory | isolated authority worktree at execution-base commit |
| Command or tool surface | governed reads, source search, hash/size probes, patch authoring, projected gates, independent review |
| Target paths | this amendment and its authorization review only |
| Allowed scope source | operator exact token `AUTHORIZE_CVF_ACTIVE_CONTINUITY_T1_AMENDMENT_1_EXACT8` |
| Before status evidence | clean worktree in the isolated authority checkout at `c6bef41ccb2e2543c93480f4e97ac13ff444046e` |
| After status evidence | amendment authority artifacts only; staged zero before projected gate preparation |
| Diff evidence | name-status, SHA-256, line/byte facts, and projected commit range |
| Approval boundary | exact-eight worker repair only after review PASS |
| Claim boundary | no implementation edit, session-sync, provider/network/live/public/deploy action, push, or downstream mutation |
| Agent type | dispatcher |
| Invocation ID | `active-continuity-read-cost-t1-amendment-1-2026-08-10` |
| Expected manifest | amendment plus authorization review |
| Actual changed set | amendment plus authorization review after review completion |
| Manifest delta | MATCH required before authority commit |
| Deletion or rename disposition | N/A with reason: authority authoring deletes or renames nothing |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this is a private-provenance Core repair authority packet. No public
artifact, public-sync batch, or push is authorized.

Next action: complete independent worker repair and review locally; any later
public export requires a separate public-sync decision.

## Claim Boundary

This amendment authorizes only the exact-eight, no-commit T1 repair. It does
not authorize current Core session/handoff compaction, T2, T3, downstream
mutation, LPCI1 development, provider/live behavior, deployment, public-sync,
push, deletion, exception-registry modification, or production-readiness
claims.
