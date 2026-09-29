# CVF Agent Work Order - LPCI1-REF T1A Public-Safe Branch Deploy Binding Amendment 2

Memory class: governed-worker-dispatch

Status: APPROVED_FOR_EXECUTION

Batch ID: LPCI1-REF-T1A-PUBLIC-SAFE-BRANCH-DEPLOY-BINDING-AMENDMENT-2

Dispatch base head: `99a99ee2548f6ef76f18d014ac422abfbe7ff98c`

dispatchBaseHead: `99a99ee2548f6ef76f18d014ac422abfbe7ff98c`

executionBaseHead: captured after committed Amendment 2 authority and session sync.

closureBaseHead: same as executionBaseHead because worker must not commit.

Commit mode: WORKER_MUST_NOT_COMMIT

Worker return path: `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_2_WORKER_RETURN_2026-08-11.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker for a source-first one-test repair.

Canonical packet: this work order plus paired Amendment 2 source verification
and GC-018 baseline.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: require exact clean Core dispatch HEAD supplied by the
orchestrator; public branch HEAD stays `2103a38f...` with authorized union 41.

Current-time notes: public dirty union 41 is authorized inherited state.

Do-not-misread notes: fix test setup, not runtime policy or expected status.
No network, commit, push, deploy, secrets, provider/store, or production.

Required first actions: startup, guards, packet, ADIF, both Git states,
union-41 hashes, and pre-implementation gate.

Return contract: one private source edit, identical same-path public mirror,
exact union-41 public worktree, one private return, staging zero, unchanged
HEADs, and `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Align the stale route-governance test fixture with accepted service-role
policy while preserving runtime denial behavior.

## Scope / Target / Owner Boundary

Worker owns only the exact private/public test path and return. Reviewer owns
acceptance and both repository commits. External actions remain excluded.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator | delegated orchestrator/reviewer authority and `next` | ACCEPT |
| Source verification | `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_2_SOURCE_VERIFICATION_2026-08-11.md` | ACCEPT |
| Baseline | `docs/baselines/CVF_GC018_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_2_2026-08-11.md` | ACCEPT |
| Blocker | Amendment 1 return at commit `7c0a1982b` | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | envelope, source-first ownership, inherited worktree, no-commit return, trace and disposition |
| gateRunPurpose | confirm Amendment 2 work order |
| claimBoundary | shape does not prove execution or hosted behavior |

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Dispatcher | orchestrator | committed authority |
| Worker | delegated implementation role | one-path source/public repair; no commit |
| Reviewer/closer | independent reviewer | tests, acceptance and commits |
| Session-sync steward | orchestrator | separate continuity commit |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake summary | independent deterministic review found stale test setup |
| risk sensitivity | authorization test semantics and public candidate |
| scope classification | one-path source-first repair |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| route | MULTI_AGENT_MULTI_ROLE |
| implementation owner | delegated worker |
| review/commit owner | independent reviewer/closer |
| escalation condition | runtime edit, extra path, network need, secret, or external action |

## Worker Autonomy / No-Question Rule

Proceed inside exact scope. Use a temporary ignored offline junction to the
existing sibling Model Gateway package when needed; restore it afterward.

## Current Runtime Freshness Verification

Union-41 hash reconciliation passes. Model Gateway typecheck and 231 tests
pass; cvf-web typecheck passes offline. Focused cvf-web result is 14 passing
files / 215 passing tests and three failures in one stale test file.

## Required First Reads

Session front doors; guard orientation; literal gotchas; repository boundary;
`DESIGN.md`; Amendment 1 blocked return; all Amendment 2 authority; checker
sources; exact route, policy, auth helper and test sources.

## Pre-Flight Checks

Run worker ADIF query for task class `LPCI1-REF source-first route governance
test repair` and pre-implementation autorun from dispatch base
`99a99ee2548f6ef76f18d014ac422abfbe7ff98c` to exact execution HEAD. Require
Core clean and public exact union 41, staged zero.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI1-REF source-first route governance test repair`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Execution Instructions

1. Edit only the private test owner named in the baseline.
2. Derive the service actor from `test-service-token`, digest it for release
   policy, set the exact allowlist environment variable in setup, and delete it
   in teardown. Keep expected 400 assertions and all runtime code unchanged.
3. Run the single test in private Core if installed tooling permits.
4. Copy the repaired private source byte to the same public path.
5. Prove private/public equality and exact public union 41.
6. Materialize and restore the offline sibling junction as needed; no fetch.
7. Run focused 15-file tests, both typechecks, Model Gateway full tests,
   scoped lint, production build, and `git diff --check`.
8. Create only the Amendment 2 return and run worker-return fast gate.

## Write Ownership

- Private: exact test path plus exact Amendment 2 return.
- Public: same test path within inherited union 41.
- Every other tracked path is read-only.

## Execution Plan

Validate; repair source; mirror exact byte; run complete deterministic proof;
return without commit.

## Work-Order Fulfillment Manifest

Expected private changes: test owner and worker return. Expected public set:
exact inherited union 41, with only the test byte diverging from `e82ab11dc`
and equaling repaired private source. Staging zero.

## Evidence Requirements

Record commands, hashes, counts, offline link lifecycle, actual statuses, and
zero external actions. Mandatory checks may not be deferred on a complete return.

## Acceptance Criteria

| Requirement | Evidence | Failure condition |
| --- | --- | --- |
| Scope | exact two private paths and union-41 public set | any extra path |
| Semantics | expected 400 cases pass through allowlisted service role | runtime relaxation or assertion weakening |
| Fidelity | repaired private/public test hashes equal | mismatch |
| Determinism | all tests/types/lint/build pass offline | failure or deferral |
| No effect | HEADs unchanged, staging zero, no external action | commit/push/deploy/network/provider/store |

## Review Gate

Independent reviewer reruns semantic, hash, test, type, lint and build evidence
before committing either repository.

## Closure Checklist

- [ ] Exact private/public ownership and union 41.
- [ ] Full deterministic verification passes.
- [ ] HEADs unchanged and staging zero.
- [ ] No secrets or external action.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with every check passing; otherwise
`BLOCKED_WITH_REASON` with the first exact contradiction.

## Operator Checkpoint

No checkpoint inside exact local scope. New authority is required for runtime
changes, widening, network, secrets, push, deploy, provider/store or production.

## Agent Handoff Contract Control Block

Canonical source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | clean Core executionBaseHead; public HEAD `2103a38f...` with authorized union 41 |
| changedSetScope(phase) | exact private test + return; same public test within union 41 |
| traceScope(phase, actor) | source repair, mirror and deterministic proof only |
| commitOwner(phase) | nobody in EXECUTION; reviewer in CLOSURE |
| crossBatchIsolation | only inherited union 41 is allowed public predecessor state |
| nextMoveSurfaces | reviewer/session steward owned |
| Worker terminal status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_2_COMPLETION_2026-08-11.md`

reviewerOwnedClosurePaths: repaired private source, worker return, completion
review if necessary, and exact public union-41 commit; session sync separate.

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: this work order changes one existing test fixture
and does not create, relocate, refactor, or change ownership of any durable
foundation storage or index surface.

## External Knowledge Intake Routing

Chain map: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external epistemic input |
| Matching local-view guard | N/A with reason: local source/tests control |
| Owner surface | Amendment 2 authority and test owner |
| Disposition | N/A with reason: no external authority admitted |
| Claim boundary | no external runtime inference |

## Worker Return Packet Shape Contract

Return must contain all standard worker-return sections, including exact
manifests/hashes/tests, operation trace, delta boundary, external routing,
rescan N/A, corpus N/A, epistemic process, closure package, public disposition,
terminal status, git status, changed files, command evidence, no-commit
statement, and worker experience retrospective.

## Dual Agent Surface Matrix

| Surface | Disposition | Evidence boundary |
| --- | --- | --- |
| INTERNAL_AGENT | AUTHORIZED | local source/test repair and deterministic tooling |
| EXTERNAL_AGENT_CLI_MCP | NOT_AUTHORIZED | no external adapter required |
| Adapter boundary | NONE | local repair only |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/work-order author |
| Provider or surface | private Core and read-only public-sync |
| Session or invocation | `lpci1-ref-t1a-amendment-2-dispatch-20260811` |
| Working directory | Core plus public-sync clone |
| Command or tool surface | local Git/source/tests and authority authoring |
| Target paths | exact three Amendment 2 authority files |
| Allowed scope source | delegated authority and committed blocker |
| Before status evidence | Core clean worktree at `99a99ee2548f6ef76f18d014ac422abfbe7ff98c`; public union 41 staged zero |
| After status evidence | authority pending commit; runtime/public untouched |
| Diff evidence | `git diff --name-status` must show exact authority set |
| Approval boundary | dispatch only |
| Claim boundary | no implementation, commit, push, deploy, hosted/provider/store, production |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `lpci1-ref-t1a-amendment-2-dispatch-20260811` |
| Expected manifest | source verification, baseline, work order |
| Actual changed set | reviewer verifies before commit |
| Manifest delta | must be zero |
| Deletion or rename disposition | N/A with reason: new authority only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | one-path source-first test repair dispatch |
| claimDisposition | CLAIM_REJECTED: no repaired/hosted behavior yet |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no hosted receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local failure isolation and authority authoring |
| invocationBoundary | zero runtime/public mutation, commit, push, deploy, provider/store, production |
| interceptionBoundary | local repositories only |
| claimLanguage | approved for no-commit one-path repair |
| forbiddenExpansion | runtime relaxation, network, secrets, push, deploy, provider/store, production, `main` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: repair and independent review precede any public export.

## Claim Boundary

This packet can authorize a local repair only. It proves no implementation,
public export, hosted deployment, provider/store behavior or production state.
