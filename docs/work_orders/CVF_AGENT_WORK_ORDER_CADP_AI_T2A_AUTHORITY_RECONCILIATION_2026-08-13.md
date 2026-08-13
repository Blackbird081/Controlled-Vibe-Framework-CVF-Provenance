# CVF Agent Work Order - CADP-AI-T2A Authority Reconciliation

Memory class: governed-work-order

Status: DISPATCH_READY

Date: 2026-08-13

Batch ID: CADP-AI-T2A-R1

## Dispatch Prompt Envelope

```text
Role: implementation worker; independent reviewer/closer follows.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T2A_AUTHORITY_RECONCILIATION_2026-08-13.md
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: executionBaseHead captured from committed dispatch HEAD.
Current-time notes: grant v2 is dispatcher-owned committed input; no secret/live use.
Do-not-misread notes: preserve v1; do not modify production source or claim T2/F11 re-closure.
Required first actions: capture HEAD/status; read baseline, packet, blocker return, source and v1/v2 grants.
Return contract: COMPLETE_PENDING_INDEPENDENT_REVIEW or BLOCKED_WITH_REASON with exact tests, hashes, status and no commit.
```

dispatchBaseHead: `27f5a9c9ce531214d439942dc9e111efd5ced160`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Prove the additive v2 grant repairs current-HEAD consumability while v1 remains
fail-closed historical evidence.

## Agent Roles

| Role | Responsibility |
|---|---|
| dispatcher | commits baseline, work order and grant v2 authority |
| worker | exact two-path test/return; no commit |
| reviewer/closer | fresh adversarial review, finality and accepted commit |

## Required First Reads

Read startup surfaces, baseline, this work order, T3A blocker, grants v1/v2,
repository owner source, owner-binding contract and existing owner tests.

## Pre-Flight Checks

Capture HEAD/status, confirm v2 is committed, staging is empty, v1 remains
unchanged, and the two-path worker manifest is exact.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: closure changed one pinned artifact and invalidated prior bind evidence.

priorVerificationArtifact: T3A blocked worker return.

priorVerificationAnchor: `c0e2a8e4b`

freshRecomputeRequired: true

unicodePathHandling: UTF-8-safe literal repository paths; new content ASCII.

extractedTextAuthority: current committed Git bytes and executed local proof.

## Worker Autonomy / No-Question Rule

Proceed inside exact two-path worker scope. Stop if production source, v1,
provider/live, secrets, or any third path is required.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator repair authorization | operator affirmative approval and continuation direction on 2026-08-13 | ACCEPT |
| blocker | `docs/reviews/CVF_CADP_AI_T3A_EXECUTION_PLANE_VERIFIED_CAPABILITY_CONSUMER_WORKER_RETURN_2026-08-13.md` | ACCEPT |
| baseline | `docs/baselines/CVF_GC018_CADP_AI_T2A_AUTHORITY_RECONCILIATION_2026-08-13.md` | ACCEPT |
| committed grant v2 | `governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v2.json` | ACCEPT |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | verify additive authority repair |
| scope classification | SECURITY_SENSITIVE_HERMETIC_AUTHORITY_REPAIR |
| risk sensitivity | high |
| selected role route | SINGLE_AGENT_SINGLE_ROLE |
| role separation basis | worker proof followed by independent reviewer acceptance |
| escalation condition | any production mutation or widened claim |

## Allowed Scope

Worker writes exactly the test and worker return paths in Required Artifact
Manifest. Grant v2, baseline and this packet are dispatcher-owned committed
inputs. Every other path is forbidden.

## Write Ownership

Worker owns only the two Required Artifact Manifest paths. Dispatcher owns v2
and dispatch inputs. Reviewer owns completion, finality and commit.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| v1 current-HEAD bind fails | executed evidence | `docs/reviews/CVF_CADP_AI_T3A_EXECUTION_PLANE_VERIFIED_CAPABILITY_CONSUMER_WORKER_RETURN_2026-08-13.md` | Findings / Position | v1 pin mismatch | T3A blocker | ACCEPT |
| production validates committed artifact pins | runtime | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/repository-capability-owner.source.ts` | grant loader | `loadCommittedRepositoryCapabilityGrant` | Guard Contract | ACCEPT |
| durable grant identity prevents rebinding | runtime | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/repository-capability-owner.source.ts` | grant registration | `GRANT_ID_REBOUND` | Guard Contract | ACCEPT |

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/repository-capability-owner.source.test.ts` | REQUIRED | v1/v2 bind, hash, reopen and replay proof |
| `docs/reviews/CVF_CADP_AI_T2A_AUTHORITY_RECONCILIATION_WORKER_RETURN_2026-08-13.md` | REQUIRED | worker evidence |

## Execution Plan

1. Recompute all v2 artifact hashes from current HEAD.
2. Add v1-fail/v2-pass and durable replay/reopen tests.
3. Run focused and full Guard Contract proof.
4. Write the worker return and stop uncommitted.

## Work-Order Fulfillment Manifest

| Deliverable | Verification | Handoff state |
|---|---|---|
| v1 negative/v2 positive proof | focused Vitest | pending worker |
| full Guard Contract regression | package test and typecheck | pending worker |
| return | worker-return fast gate | pending worker |

## Acceptance Criteria

- v1 fails current-HEAD binding for the disclosed pin mismatch;
- v2 binds only after committed visibility and all four artifact hashes match;
- v2 has a distinct grant ID/hash and cannot reset v1 durable state;
- duplicate/reopen/retry behavior remains fail-closed;
- no production code, raw secret, provider or external action changes;
- independent reviewer recomputes hashes and authors fresh probes.

## Evidence Requirements

Record exact v1/v2 hashes, commands, test counts, SQLite/replay behavior,
execution base, status, staging and residuals. Green worker tests are not
independent acceptance.

## Review Gate

Independent reviewer reads the complete two-path diff, independently hashes
all v2 artifacts, probes v1/v2 from current HEAD and across reopen/replay, and
reassesses T2/F11 consumability before resuming T3A.

## Closure Checklist

- [ ] independent review disposition exists
- [ ] v1 remains unchanged and fail-closed
- [ ] v2 current-HEAD binding and durable behavior pass
- [ ] reviewer-owned material commit and pre-closure gate pass
- [ ] T3A dependency and session continuity are refreshed

## Return-To-Orchestrator Conditions

Return blocked if repair requires production source, v1 mutation, a third
worker path, provider/live, secrets, public sync, deployment or production.

## Operator Checkpoint

No checkpoint inside exact hermetic repair. Any widened scope requires fresh
operator direction.

## Verification Commands

```powershell
pnpm --dir EXTENSIONS/CVF_GUARD_CONTRACT exec tsc --noEmit
pnpm --dir EXTENSIONS/CVF_GUARD_CONTRACT exec vitest run --pool forks src/contracts/repository-capability-owner.source.test.ts src/contracts/capability-owner-binding.contract.test.ts src/contracts/capability-admission-distribution-profile.contract.test.ts
pnpm --dir EXTENSIONS/CVF_GUARD_CONTRACT test
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
```

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CADP-AI-T2A-R1 --title "Authority Reconciliation" --date 2026-08-13 --base 27f5a9c9c --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | two-path manifest, v1/v2 proof and reviewer contract |
| checkerReadAheadConfirmation | applicable checker sources inspected |
| docOnlyNewFields | authority reconciliation decision |
| claimBoundary | scaffold provenance only |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | worker then independent reviewer/closer |
| phase | T2A authority reconciliation |
| baseHeadFor(phase) | dispatch=`27f5a9c9c`; execution=`WORKER_MUST_CAPTURE_AT_START`; closure=`NOT_EXECUTED_YET` |
| changedSetScope(phase) | exact two worker paths |
| traceScope(phase, actor) | hashes, binder, SQLite reopen/replay, tests and gates |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no T3A/provider/public/deploy/session mixing |
| Before status evidence | clean worktree verified at committed dispatch HEAD |
| nextMoveSurfaces | worker return and independent completion review |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CADP_AI_T2A_AUTHORITY_RECONCILIATION_COMPLETION_2026-08-13.md` |
| reviewerOwnedClosurePaths | repair finality, T2/F11 reassessment, T3A dependency refresh, completion and commit |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |
| acceptanceRequirement | full diff plus independent current-HEAD hash, v1/v2, reopen and replay probes |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Required Artifact Manifest; Reviewer Closure Conversion; Public Export Disposition |
| gateRunPurpose | confirmation evidence after complete packet authoring |
| claimBoundary | green gates do not repair authority or close T2/F11 |

## Machine Closure Package

N/A with reason: pending no-commit work order; reviewer owns closure package.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defect count: 0.

Returned defects: NONE_RETURNED

Dispatch impact: independent proof remains required.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local repository |
| Session or invocation | T2A-R1 dispatch 2026-08-13 |
| Working directory | repository root |
| Command or tool surface | Git blob hash, source reads, apply_patch |
| Target paths | baseline, work order, grant v2 |
| Allowed scope source | operator repair authorization |
| Before status evidence | clean worktree at HEAD `27f5a9c9c` |
| After status evidence | pending dispatch inputs |
| Diff evidence | exact three dispatcher paths |
| Approval boundary | dispatch only |
| Claim boundary | no repair success claim |
| Agent type | dispatcher |
| Invocation ID | `cadp-ai-t2a-r1-dispatch-2026-08-13` |
| Expected manifest | three dispatcher inputs |
| Actual changed set | recorded before commit |
| Manifest delta | must be zero |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private authority repair.

## Claim Boundary

This packet authorizes hermetic v2 proof only. T2/F11 remain under
reassessment and T3A remains blocked pending independent acceptance.
