# CVF Agent Work Order - MAO-T3 Provider-Neutral Delegation Adapter

Memory class: governed-work-order

Status: DISPATCH_READY

Date: 2026-07-11

Batch: MAO-T3

dispatchBaseHead: `ecb2679a6`

executionBaseHead: capture actual clean post-dispatch-sync HEAD before editing.

closureBaseHead: N/A with reason: reviewer conversion has not occurred.

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: delegated MAO-T3 worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T3_PROVIDER_NEUTRAL_DELEGATION_ADAPTER_2026-07-11.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture actual clean post-sync HEAD.

Current-time notes: artifact date is 2026-07-11.

Do-not-misread notes: fake/local adapter contract only; no provider/network,
queue, UI, public, session, root-barrel, or MAO-T4 work.

Required first actions: startup reads, capture HEAD/status, read paired baseline
and every ACCEPT source, then run pre-implementation gate.

Return contract: exactly four outputs, required tests/gates, no commit, return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement a provider-neutral delegation port with capability validation,
admission/authority binding, deterministic invocation identity, idempotency,
secret-safe diagnostics, and fake/local adapter tests.

## Authority Chain

`AGENTS.md`; MAO roadmap T3; T0 contract/schema; accepted T1/T2 source and
completion reviews; paired GC-018; this work order.

## Agent Roles

Worker implements and returns without commit. Independent reviewer/closer
recomputes evidence and owns accepted material commit. Session sync is separate.

## Scope / Target / Owner Boundary

### Allowed worker paths

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.delegation.adapter.contract.test.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`
- `docs/reviews/CVF_MAO_T3_PROVIDER_NEUTRAL_DELEGATION_ADAPTER_WORKER_RETURN_2026-07-11.md`

### Forbidden paths and behavior

No provider call/config/secret, provider-router mutation, queue, UI, workspace/
session, public-sync, root barrel, checker/hook, roadmap, MAO-T4+, commit, push,
or live proof. Fake/local adapter only. No retry orchestration beyond duplicate
idempotency response; MAO-T6 owns lifecycle retry/cancel/recovery.

## Write Ownership

Exactly four worker paths. Reviewer may add completion conversion and minimum
GC-051 source/aggregate coverage if required.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Final disposition | Refreshed base |
|---|---|---|---|---|
| MAO-T1 | T1 completion review | `01618e9dc` | `REVIEWER_ACCEPTED_BOUNDED` | `ecb2679a6` |
| MAO-T2 | T2 completion review | `854bb3a92` | `REVIEWER_ACCEPTED_BOUNDED` | `ecb2679a6` |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T3 --title "Provider-Neutral Delegation Adapter" --date 2026-07-11 --base ecb2679a6 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-backed T3 controls replaced all placeholders |
| checkerReadAheadConfirmation | applicable checker sources read |
| docOnlyNewFields | capability/diagnostic adapter-local vocabulary is new |
| claimBoundary | dispatch provenance only |

## Required First Reads

Guard orientation, literal gotchas, paired packet, roadmap T3, T0 contract/schema,
T1 graph, T2 resolver, provider router, and checker sources.

## Pre-Flight Checks

Capture clean HEAD/status, verify all source symbols, search collisions, and run
pre-implementation autorun before edits.

## Worker Autonomy / No-Question Rule

Repair allowed-scope failures. Return blocked for missing source, forbidden-path
need, provider/live action, ambiguous side effect, or authority expansion.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T3 deliverables | LITERAL_INVARIANT | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` | MAO-T3 | `MAO-T3 - Provider-Neutral Delegation Adapter` | roadmap | ACCEPT |
| port inputs/boundary | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Provider-Neutral Capability Port | capability declaration, authority envelope, idempotency key | T0 contract | ACCEPT |
| invocation receipt | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json` | definitions | `invocationReceipt` | schema | ACCEPT |
| authority verification | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | exports | `MaoTaskGraph`, `verifyAuthorityEnvelope` | MAO-T1 | ACCEPT |
| admission decision | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | exports | `MaoRoleResolutionReceipt` | MAO-T2 | ACCEPT |
| provider selection owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/provider.router.contract.ts` | class method | `route` | `ProviderRouterContract` | ACCEPT |
| provider registry surface | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | exported class | `ProviderRegistry` | model gateway | ACCEPT |
| capability registry surface | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | exported constant | `PROVIDER_CAPABILITY_REGISTRY` | model gateway | ACCEPT |

## Current Runtime Freshness Verification

Verified at `ecb2679a6`. New adapter symbols are outputs, not existing facts.

## Negative Search And Collision Discipline

Search delegation adapter, capability, invocation receipt, diagnostic, and
idempotency tokens. Record reuse/collision; do not duplicate provider policy.
`ProviderRegistry` and `PROVIDER_CAPABILITY_REGISTRY` remain existing downstream
provider/configuration owners; the fake/local T3 port neither replaces nor
claims absence of those surfaces.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`adapter contract implementation`, role=`worker`, lifecyclePhase=`implementation`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "adapter contract implementation" --role worker --lifecycle-phase implementation --surface-selector "multi-agent orchestration provider-neutral delegation adapter" --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

Disclosed defectIds: N/A with reason: NONE_RETURNED.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch envelope; AHB fields; full worker-return contract; trace manifest; public disposition |
| gateRunPurpose | confirmation/evidence after source-backed authoring; not first discovery |
| claimBoundary | dispatch compatibility only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

Intake summary: fake/local adapter contract with independent review.

Scope classification: `RUNTIME_FOUNDATION_FAKE_LOCAL_NO_LIVE_PROVIDER`

Risk sensitivity: HIGH.

Escalation condition: authority mismatch, idempotency conflict ambiguity,
provider/live requirement, forbidden path, or source contradiction.

## Dual Agent Surface Matrix

| Surface | Intended use | Interface | Authority/risk boundary | Required evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | fake/local invocation contract | direct local port | admitted role and immutable authority only | focused tests | no network/provider |
| EXTERNAL_AGENT_CLI_MCP | not implemented | none | cannot become authority | N/A with reason: excluded | fresh future packet required |

## Agent Handoff Contract Control Block

Contract source, active and not archive:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | actual execution base captured at start |
| changedSetScope(phase) | exactly four worker paths |
| traceScope(phase, actor) | worker execution trace only |
| commitOwner(phase) | reviewer/closer; worker cannot commit |
| crossBatchIsolation | clean worktree; one MAO-T3 batch only |
| Before status evidence | clean worktree; `git status --short` empty at dispatch start |
| nextMoveSurfaces | separate session sync after accepted material |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MAO_T3_PROVIDER_NEUTRAL_DELEGATION_ADAPTER_COMPLETION_2026-07-11.md`

reviewerOwnedClosurePaths: baseline, work order, completion review, and minimum GC-051 coverage.

## Roadmap-to-Work-Order Trace Matrix

| Requirement | Handling | Status |
|---|---|---|
| capability contract | provider-neutral typed input | PASS |
| invocation identity | deterministic task/attempt/adapter receipt | PASS |
| authority enforcement | hash and admitted-role negatives | PASS |
| idempotency | duplicate replay and conflict tests | PASS |
| diagnostics | secret-safe classified envelope | PASS |
| fake/local tests | no network/provider execution | PASS |

## Work-Order Fulfillment Manifest

Exactly four worker paths.

## Required Artifact Manifest

| Artifact | Owner | Required evidence | Status |
|---|---|---|---|
| adapter source | worker | focused tests/typecheck | REQUIRED |
| focused test | worker | positive/negative/idempotency cases | REQUIRED |
| local MAO barrel | worker | bounded export only | REQUIRED |
| worker return | worker | complete pending review | REQUIRED |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Return includes all generic review headings, conditional N/A sections, Source
Inventory, trace, Delta boundary, public disposition, and actual status.

## Execution Plan

1. Verify sources/base and run pre-implementation gate.
2. Define capability/request/result/diagnostic/idempotency contracts.
3. Implement fake/local port that validates admission and authority before action.
4. Test success, missing capability, rejected/approval-pending admission, stale
   authority, duplicate replay, conflicting key, invalid output, and secret-safe diagnostics.
5. Update local barrel, create return, run all commands, stop uncommitted.

## Verification Commands

- From execution-plane package: `npx vitest run --config vitest.config.ts tests/mao.delegation.adapter.contract.test.ts`
- `npx tsc -p tsconfig.json --noEmit`
- Repo root: `python governance/compat/check_governed_file_size.py --enforce`
- Repo root: `python governance/compat/run_worker_return_fast_gate.py`
- Repo root: `git diff --check`

## Acceptance Criteria

- [ ] Capability and authority are validated before fake/local action.
- [ ] Only admitted roles may invoke; approval-required/rejected plans fail closed.
- [ ] Idempotency replay returns existing receipt and conflicts are classified.
- [ ] Receipt matches T0 invocation fields and diagnostics are secret-safe.
- [ ] No provider/network/commit/queue/public action occurs.
- [ ] Focused tests, typecheck, fast gate, and self-audit pass.

## Evidence Requirements

Exact commands/results, negative cases, actual final status, evidence trace, and
separate material/session-sync ranges.

## Negative And Fail-Condition Scan

Block closure for authority widening, provider hardcoding/call, duplicate side
effect, ambiguous diagnostic, missing receipt field, forbidden path, or open checklist.

## Review Gate

Worker returns `COMPLETE_PENDING_REVIEW`; reviewer independently reruns tests and
reviewer-return steward preflight before acceptance.

## Closure Checklist

- [ ] Requirements and commands pass after final edit.
- [ ] Closure Diff Gate and exact changed-set evidence complete.
- [ ] No runtime/provider/public expansion occurred.
- [ ] Continuity sync remains separate after material commit.

## Return-To-Orchestrator Conditions

Missing source, provider/live need, forbidden-path necessity, ambiguous side
effect, authority expansion, or irreparable out-of-scope gate failure.

## Operator Checkpoint

No checkpoint for fake/local tests. Real provider/network/quota requires fresh authorization.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | MAO-T3 dispatch, 2026-07-11 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver, patch, gates, git |
| Target paths | paired MAO-T3 baseline/work order |
| Allowed scope source | operator request and roadmap T3 |
| Before status evidence | clean worktree at `ecb2679a6` |
| After status evidence | two new packet artifacts pending commit |
| Diff evidence | exact pending two-path diff |
| Approval boundary | packet dispatch only; no implementation |
| Claim boundary | repo-local trace; no provider/production attribution |
| Agent type | dispatcher |
| Invocation ID | mao-t3-dispatch-2026-07-11 |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | fake/local MAO-T3 adapter contract and tests |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: dispatch proves no invocation receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT at worker return through focused tests |
| invocationBoundary | local fake function only |
| interceptionBoundary | no provider/network/IDE/shell/git interception claim |
| claimLanguage | tested contract, not provider support |
| forbiddenExpansion | live provider, queue, UI, commit, public, MAO-T4+ |

## Foundation Storage Layout Block

| Question | Disposition |
|---|---|
| Generated aggregate | N/A with reason: none introduced. |
| Storage | local execution-plane source/test |
| Persistence | in-memory fake idempotency store only; no durable runtime claim |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired MAO-T3 packet |
| Disposition | NOT_APPLICABLE_WITH_REASON: internal sources only |
| Claim boundary | no external intake claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Next action: retain in provenance through MAO closure.

## Machine Closure Package

| Field | Value |
|---|---|
| Work-order state | `DISPATCH_READY` |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Dependencies | T1/T2 accepted |
| Worker terminal status | `COMPLETE_PENDING_REVIEW` only |
| Next action | delegated fake/local execution from clean post-sync HEAD |

## Acceptance Receipt Assertion Matrix

| Assertion | Evidence |
|---|---|
| authority/admission binding | negative tests |
| idempotency | replay/conflict tests |
| diagnostics | classified secret-safe receipt |
| provider neutrality | import/network/changed-set scan |

## Claim Boundary

This dispatch authorizes fake/local adapter contract implementation only. It
does not establish real provider support, live governance, retry lifecycle,
queueing, reviewer effectiveness, public readiness, or production orchestration.
