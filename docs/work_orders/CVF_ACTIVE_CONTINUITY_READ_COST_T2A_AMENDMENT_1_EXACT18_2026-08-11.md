# CVF Active Continuity Read-Cost T2A Amendment 1 - Exact-18 Test Fixture

Memory class: WORK_ORDER_AMENDMENT

Status: AUTHORIZED_FOR_EXISTING_EXACT18_REVIEW_ONLY

Date: 2026-08-11

Batch ID: ACRC-T2A-A1

Risk ceiling: R2

Commit mode: WORKER_MUST_NOT_COMMIT

Execution base HEAD: `7b9316620ffb0099194fdbef3f0d777d6932351c`

## Authorization

The operator issued the exact token
`AUTHORIZE_T2A_AMENDMENT_EXACT18_TEST_FIXTURE_ONLY` on 2026-08-11 after the
independent reviewer found that fail-closed `currentAuthority` validation made
seven legacy active-session tests fail because their shared fixture lacked the
new required authority object.

This amendment ratifies only the already-present bounded repair for independent
review. It is not authority for any nineteenth worker implementation path.

## Purpose

Add one test-only path to the original exact-17 worker manifest so the shared
legacy fixture carries real temporary authority files/hashes and deterministic
negative proof covers unreadable and symlink authority paths. The production
checker remains fail closed; no invariant is weakened.

## Parent Authority

- Paired GC-018:
  `docs/baselines/CVF_GC018_ACTIVE_CONTINUITY_READ_COST_T2A_CORE_SURFACE_COMPACTION_2026-08-11.md`
- Parent Work Order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_CONTINUITY_READ_COST_T2A_CORE_SURFACE_COMPACTION_2026-08-11.md`
- Parent Work Order SHA-256:
  `3786355ea00f3ebd6b4d8d08c42ffb19ca5283a55880728b4ee34689ee94c630`
- GC-018 SHA-256:
  `bfe630379886f3a7f4abfd7f9f79caa6749a70d44fe46bd7c4d0064ec4296cf1`
- Worker return:
  `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2A_WORKER_RETURN_2026-08-11.md`

## Authority Chain

1. Original operator T2A authority produced the paired GC-018 and parent Work
   Order.
2. Independent review found one test-fixture scope insufficiency.
3. The operator issued the exact amendment token recorded above.
4. This amendment binds that token to one added test-only path.
5. The independent reviewer/closer owns acceptance and commit.

## Agent Roles

- Operator: owns the exact-18 amendment decision.
- Existing worker: supplied the uncommitted bounded repair and evidence.
- Independent reviewer/closer: recomputes evidence, accepts or rejects, commits,
  and parks T2A.

## Allowed / Forbidden Scope

Allowed: the one added path in `## Amendment Scope` and the original exact-17
only for review of the already-present implementation.

Forbidden: every nineteenth worker path, further implementation, T2B/T3,
provider/network/live/downstream/public/deploy/push effects, and worker commit.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. this amendment
3. the parent Work Order and paired GC-018
4. the worker return
5. the production checker and two active-session test modules

## Pre-Flight Checks

Verify HEAD `7b9316620`, staged zero, exact-18/no-nineteenth status, authority
hashes, the operator token, and current file-size facts before review closure.

## Write Ownership

The worker remains no-commit. The reviewer owns this amendment, authority-wording
correction, completion review, accepted material commit, and continuity parking.

## Amendment Scope

The eighteenth and only added worker path is:

`governance/compat/test_check_active_session_state.py`

The original 17 paths remain unchanged. Final worker manifest size is exactly
18 paths. No nineteenth worker path is authorized.

Allowed changes in the added path:

1. create temporary baseline and Work Order fixture files;
2. add valid `currentAuthority` paths and SHA-256 values to the shared state
   fixture;
3. add deterministic read-failure and symlink negative tests; and
4. keep the file below its existing hard 1,200-line test ceiling.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Verification class | Disposition |
|---|---|---|---|---|---|---|
| legacy active-session tests share one temporary repository fixture | `governance/compat/test_check_active_session_state.py` | `ActiveSessionStateTests.setUp` | `setUp` | active-session checker test owner | RUNTIME_BEHAVIOR | ACCEPT |
| the parent exact-17 excludes the legacy test file | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_CONTINUITY_READ_COST_T2A_CORE_SURFACE_COMPACTION_2026-08-11.md` | `Exact Changed Set`; `Near-Threshold Owner Maintainability Plan` | `governance/compat/test_check_active_session_state.py` | parent Work Order | LITERAL_INVARIANT | ACCEPT |
| currentAuthority absence must fail closed | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_CONTINUITY_READ_COST_T2A_CORE_SURFACE_COMPACTION_2026-08-11.md` | Required Behavior 4 | `currentAuthority` | active-session checker contract | LITERAL_INVARIANT | ACCEPT |
| current test file remains under its 1,200-line hard ceiling | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | active exception entry for the test path | `governance/compat/test_check_active_session_state.py` | governed file-size registry | VALUE_SET | ACCEPT |

No runtime/source symbol is blocked. The amendment changes fixture/proof only.

## Execution Plan

1. Ratify the exact token in this canonical amendment.
2. Recompute legacy/focused tests and fail-closed source behavior.
3. Verify exact-18, archives, budgets, generated state, and local gates.
4. Issue independent PASS or CHANGES_REQUIRED.
5. On PASS only, reviewer commits material then parks T2A separately.

## Evidence Requirements

- the legacy active-session test module passes with zero failures;
- focused generator and authority tests pass;
- unreadable-authority validation emits a typed violation;
- deterministic symlink validation emits a typed violation without requiring
  elevated filesystem privileges;
- active-session and generated-state checks pass;
- governed Python/file-size gates pass;
- final changed set is exact-18 with no nineteenth worker path;
- HEAD remains unchanged and staged paths remain zero before reviewer commit;
  and
- all external-call and worker-commit counts remain zero.

## Acceptance Criteria

- A1-AC-01: the shared fixture supplies valid authority files and hashes.
- A1-AC-02: all legacy tests pass without weakening absence validation.
- A1-AC-03: read failure and symlink cases are deterministic and fail closed.
- A1-AC-04: the added test path remains below 1,200 lines.
- A1-AC-05: exact-18/no-nineteenth containment is proven.
- A1-AC-06: independent review, not worker self-claim, owns final acceptance.

## Review Gate

Independent review must prove all amendment acceptance criteria and the parent
AC-01 through AC-12. Green focused tests alone are insufficient.

## Closure Checklist

- [x] Exact operator token is recorded.
- [x] Added path and no-nineteenth boundary are explicit.
- [x] Source Verification Block is complete.
- [x] Fail-closed and legacy-regression evidence is required.
- [x] Reviewer commit ownership and parked next move are explicit.

## Return-To-Orchestrator Conditions

Return CHANGES_REQUIRED if any legacy/focused test fails, fail-closed proof is
missing, exact-18 expands, authority hashes drift, or a local governance gate
fails. Otherwise proceed to independent completion review.

## Operator Checkpoint

The exact amendment checkpoint is satisfied by
`AUTHORIZE_T2A_AMENDMENT_EXACT18_TEST_FIXTURE_ONLY`. Any further path or scope
requires a new operator checkpoint.

## Core Guard Self-Protection Authorization

Protected paths:

- `governance/compat/test_check_active_session_state.py`
- `governance/compat/check_active_session_state.py`
- `governance/compat/test_active_continuity_t2a_authority.py`

Operator authorization: exact token
`AUTHORIZE_T2A_AMENDMENT_EXACT18_TEST_FIXTURE_ONLY`.

Authorized guard-maintenance scope: one additive legacy test-fixture/proof path
plus the already-authorized exact-17 implementation; no production weakening.

Rollback boundary: revert the exact-18 T2A material set together if rejected;
preserve both byte-identical archives and do not touch a nineteenth worker path.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Binding |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | operator authorization, existing no-commit worker repair, independent reviewer/closer |
| phase | `T2A_AMENDMENT_RATIFICATION`, `T2A_REVIEW`, `T2A_CLOSURE_OR_BLOCK` |
| baseHeadFor(phase) | `dispatchBaseHead=7b9316620ffb0099194fdbef3f0d777d6932351c`; existing worker `executionBaseHead` is unchanged; reviewer records `closureBaseHead` |
| changedSetScope(phase) | original exact-17 plus one test-fixture path equals exact-18 |
| traceScope(phase, actor) | operator token authorizes; reviewer verifies source/tests and owns closure |
| commitOwner(phase) | independent reviewer/closer after PASS |
| crossBatchIsolation | T2B/T3 and every other lane remain parked |
| nextMoveSurfaces | reviewer parks T2A only after accepted material commit |

Designated closer: `INDEPENDENT_BUILD_REVIEWER_CLOSER`.

## Reviewer Closure Conversion

- completionReviewPath:
  `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2A_COMPLETION_REVIEW_2026-08-11.md`
- reviewerOwnedClosurePaths: this amendment, completion review, accepted
  exact-18 material commit, and bounded continuity parking
- worker commit disposition: `WORKER_MUST_NOT_COMMIT`
- further implementation disposition: forbidden without fresh authority

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_active_session_state.py`; `governance/compat/check_python_automation_size.py` |
| literalTokensReviewed | `WORKER_MUST_NOT_COMMIT`; `Core Guard Self-Protection Authorization`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Agent Operation Trace Block`; `Public Export Disposition` |
| gateRunPurpose | confirmation after source review and exact operator authorization |
| claimBoundary | exact-18 test-fixture amendment and independent closure only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent reviewer/closer acting as amendment author |
| Provider or surface | local private CVF Core workspace |
| Session or invocation | ACRC-T2A-A1 exact-18 ratification, 2026-08-11 |
| Working directory | repository root |
| Command or tool surface | repository reads, patch authoring, tests, governance gates, Git read-only checks |
| Target paths | exact-18 worker material, this amendment, worker return, and completion review |
| Allowed scope source | operator token `AUTHORIZE_T2A_AMENDMENT_EXACT18_TEST_FIXTURE_ONLY` |
| Before status evidence | HEAD `7b9316620`; staged zero; exact-18 worker result |
| After status evidence | 20 changed paths: exact-18 plus two reviewer-owned artifacts |
| Diff evidence | status/name-status, source diff, tests, file-size and governance gates |
| Approval boundary | one test-only added worker path; reviewer closure/commit ownership |
| Claim boundary | no nineteenth worker path or external effect |
| Agent type | independent reviewer/closer |
| Invocation ID | `active-continuity-t2a-a1-ratification-2026-08-11` |
| Expected manifest | exact-18 worker material plus Amendment 1 and completion review |
| Actual changed set | same 20 paths before reviewer commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | V57 root removal is paired with its byte-identical archive |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance test-fixture and continuity maintenance only.

## Claim Boundary

This amendment ratifies exactly one additional test path for the existing T2A
review. It does not authorize T2B/T3, a nineteenth worker path, runtime/provider
behavior, downstream mutation, live proof, public sync, push, deployment, or
production readiness.
