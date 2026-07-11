# CVF Agent Work Order - MAO-T4 Reviewer Isolation, Dissent, And Revision Loop

Memory class: governed-work-order

Status: DISPATCH_READY

Date: 2026-07-11

Batch: MAO-T4

dispatchBaseHead: `300c9dfa3`

executionBaseHead: capture actual clean post-dispatch-sync HEAD before editing.

closureBaseHead: N/A with reason: reviewer conversion has not occurred.

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: delegated MAO-T4 worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T4_REVIEWER_ISOLATION_DISSENT_AND_REVISION_LOOP_2026-07-11.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture actual clean post-sync HEAD.

Current-time notes: artifact date is 2026-07-11.

Do-not-misread notes: local review-policy mechanics only; no provider, queue,
commit/closer interlock, UI, public, session, root-barrel, or MAO-T5 work.

Required first actions: startup reads, capture HEAD/status, read paired baseline
and every ACCEPT source, run pre-implementation gate.

Return contract: exactly five outputs, required tests/gates, no commit, return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement deterministic reviewer isolation, recomputation, self-approval guard,
dissent/defect/repair records, and bounded revision/escalation controls.

## Authority Chain

`AGENTS.md`; roadmap MAO-T4; T0 contract/schema; accepted T1-T3 source and
completion; paired GC-018; this work order.

## Agent Roles

Worker implements/tests and returns uncommitted. Independent reviewer/closer
recomputes evidence and owns accepted material commit. Session sync is separate.

## Scope / Target / Owner Boundary

### Allowed worker paths

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/reviewer.isolation.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/dissent.revision.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.reviewer.isolation.revision.contract.test.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`
- `docs/reviews/CVF_MAO_T4_REVIEWER_ISOLATION_DISSENT_AND_REVISION_LOOP_WORKER_RETURN_2026-07-11.md`

### Forbidden paths and behavior

No provider/network/secret, queue, durable store, UI, workspace/session,
public-sync, root barrel, checker/hook, roadmap, closer/commit interlock,
MAO-T5+, commit, push, or live proof. No worker conclusion may enter the
isolated source packet as reviewer authority.

## Write Ownership

Exactly five worker paths. Reviewer may add completion conversion and minimum
GC-051 source/aggregate coverage if required.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Final disposition | Refreshed base |
|---|---|---|---|---|
| MAO-T1 | T1 completion | `01618e9dc` | `REVIEWER_ACCEPTED_BOUNDED` | `300c9dfa3` |
| MAO-T2 | T2 completion | `854bb3a92` | `REVIEWER_ACCEPTED_BOUNDED` | `300c9dfa3` |
| MAO-T3 | T3 completion | `052845fa1` | `REVIEWER_ACCEPTED_BOUNDED` | `300c9dfa3` |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T4 --title "Reviewer Isolation Dissent And Revision Loop" --date 2026-07-11 --base 300c9dfa3 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-backed T4 controls replaced all placeholders |
| checkerReadAheadConfirmation | applicable checker sources read |
| docOnlyNewFields | isolation/dissent local vocabulary is new |
| claimBoundary | dispatch provenance only |

## Required First Reads

Guard orientation, literal gotchas, paired packet, roadmap T4, T0 contract/schema,
T1 graph/read model, T3 receipt, and checker sources.

## Pre-Flight Checks

Capture clean HEAD/status, verify sources, search collisions, and run
pre-implementation autorun before edits.

## Worker Autonomy / No-Question Rule

Repair allowed-scope failures. Return blocked for missing source, impossible
isolation, forbidden path, provider/live action, or authority expansion.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T4 deliverables | LITERAL_INVARIANT | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` | MAO-T4 | `MAO-T4 - Reviewer Isolation, Dissent, And Revision Loop` | roadmap | ACCEPT |
| reviewer/revision lifecycle | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | lifecycle steps 7-8 | isolated packet and bounded repair | T0 contract | ACCEPT |
| review receipt | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json` | definitions | `reviewReceipt` | schema | ACCEPT |
| authority revision ceiling | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | authority budget | `maxRevisionDepth` | MAO-T1 | ACCEPT |
| task/actor evidence inputs | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | exports | `MaoTaskGraph`, `MaoTaskDefinition` | MAO-T1 | ACCEPT |
| invocation identity | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | exports | `MaoInvocationReceipt` | MAO-T3 | ACCEPT |
| dissent readout | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts` | interface | `openDissent` | MAO-T1 | ACCEPT |

## Current Runtime Freshness Verification

Verified at `300c9dfa3`; proposed T4 symbols are new outputs, not source facts.

## Negative Search And Collision Discipline

Search reviewer packet, excluded context, review receipt, dissent, repair owner,
revision and escalation tokens. Reuse T0 vocabulary; record collisions.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`reviewer isolation implementation`, role=`worker`, lifecyclePhase=`implementation`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "reviewer isolation implementation" --role worker --lifecycle-phase implementation --surface-selector "multi-agent orchestration dissent revision" --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

Disclosed defectIds: N/A with reason: NONE_RETURNED.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch envelope; AHB fields; worker-return contract; trace manifest; public disposition |
| gateRunPurpose | confirmation after source-backed authoring; not first discovery |
| claimBoundary | dispatch compatibility only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

Intake summary: reviewer-isolation and bounded-revision foundation.

Scope classification: `RUNTIME_FOUNDATION_LOCAL_NO_PROVIDER`

Risk sensitivity: HIGH.

Escalation condition: isolation breach, self-approval, revision overflow,
authority mismatch, forbidden path, or provider/live need.

## Dual Agent Surface Matrix

| Surface | Intended use | Interface | Authority/risk boundary | Required evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | local isolation/review policy | pure local functions | reviewer evidence excludes worker conclusions | focused tests | no provider |
| EXTERNAL_AGENT_CLI_MCP | not implemented | none | cannot become authority | N/A with reason: excluded | fresh packet required |

## Agent Handoff Contract Control Block

Contract source, active and not archive:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | actual execution base captured at start |
| changedSetScope(phase) | exactly five worker paths |
| traceScope(phase, actor) | worker execution trace only |
| commitOwner(phase) | reviewer/closer; worker cannot commit |
| crossBatchIsolation | clean worktree; one MAO-T4 batch only |
| Before status evidence | clean worktree; `git status --short` empty at dispatch start |
| nextMoveSurfaces | separate session sync after accepted material |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MAO_T4_REVIEWER_ISOLATION_DISSENT_AND_REVISION_LOOP_COMPLETION_2026-07-11.md`

reviewerOwnedClosurePaths: baseline, work order, completion review, minimum GC-051 coverage.

## Roadmap-to-Work-Order Trace Matrix

| Requirement | Handling | Status |
|---|---|---|
| isolated packet | canonicalized source hash and exclusions | PASS |
| recomputation | reviewer-produced evidence only | PASS |
| self approval guard | worker/reviewer identity negatives | PASS |
| dissent/defects/repair | deterministic typed ledger | PASS |
| bounded revision | ceiling and escalation tests | PASS |
| stop/escalation | terminal decision matrix | PASS |

## Work-Order Fulfillment Manifest

Exactly five worker paths.

## Required Artifact Manifest

| Artifact | Owner | Required evidence | Status |
|---|---|---|---|
| isolation source | worker | focused tests/typecheck | REQUIRED |
| dissent/revision source | worker | bounded loop tests | REQUIRED |
| focused test | worker | positive/negative matrix | REQUIRED |
| local barrel | worker | bounded exports only | REQUIRED |
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
2. Build isolated source packet with deterministic hash and excluded-context manifest.
3. Implement review receipt, recomputation requirement, self-approval guard.
4. Implement dissent/defect/repair record and revision decision bounded by authority.
5. Test accept, repair, dissent, escalation, rejection, identity collision,
   contaminated packet, missing recomputation, and revision ceiling.
6. Update local barrel, create return, run commands, stop uncommitted.

## Verification Commands

- Execution-plane package: `npx vitest run --config vitest.config.ts tests/mao.reviewer.isolation.revision.contract.test.ts`
- `npx tsc -p tsconfig.json --noEmit`
- Repo root: `python governance/compat/check_governed_file_size.py --enforce`
- Repo root: `python governance/compat/run_worker_return_fast_gate.py`
- Repo root: `git diff --check`

## Acceptance Criteria

- [ ] Isolated packet hash/exclusions are deterministic and worker conclusions are excluded.
- [ ] Reviewer identity cannot equal worker/output author identity.
- [ ] Review receipt requires recomputed evidence and a valid decision.
- [ ] Dissent/defect class/repair owner are preserved deterministically.
- [ ] Revision depth cannot exceed authority; overflow escalates/stops.
- [ ] No provider/commit/queue/public action occurs; tests/typecheck/gates pass.

## Evidence Requirements

Exact commands/results, negative cases, final status, evidence trace, and separate
material/session-sync ranges.

## Negative And Fail-Condition Scan

Block closure for contaminated isolation, self approval, missing recomputation,
lost dissent, unowned repair, unbounded revision, forbidden path, or provider claim.

## Review Gate

Worker returns `COMPLETE_PENDING_REVIEW`; independent reviewer reruns tests and
reviewer-return steward preflight before acceptance.

## Closure Checklist

- [ ] Requirements/commands pass after final edit.
- [ ] Closure Diff Gate and exact changed set complete.
- [ ] No provider/commit/public expansion occurred.
- [ ] Continuity sync remains separate.

## Return-To-Orchestrator Conditions

Missing source, impossible isolation, forbidden path, authority expansion,
provider/live need, or irreparable out-of-scope gate failure.

## Operator Checkpoint

No checkpoint for local tests. Provider/live/public or revision-ceiling expansion requires fresh authorization.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | MAO-T4 dispatch 2026-07-11 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver, patch, gates, git |
| Target paths | paired MAO-T4 baseline/work order |
| Allowed scope source | operator request and roadmap T4 |
| Before status evidence | clean worktree at `300c9dfa3` |
| After status evidence | two new packet artifacts pending commit |
| Diff evidence | exact pending two-path diff |
| Approval boundary | packet dispatch only; no implementation |
| Claim boundary | repo-local trace; no provider/production attribution |
| Agent type | dispatcher |
| Invocation ID | mao-t4-dispatch-2026-07-11 |
| Expected manifest | paired baseline/work order |
| Actual changed set | paired baseline/work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | local MAO-T4 reviewer isolation/revision contract and tests |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: dispatch proves no review receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT at worker return through tests |
| invocationBoundary | local pure functions only |
| interceptionBoundary | no provider/network/IDE/shell/git interception claim |
| claimLanguage | tested policy mechanics, not review quality proof |
| forbiddenExpansion | provider, queue, commit, UI, public, MAO-T5+ |

## Foundation Storage Layout Block

| Question | Disposition |
|---|---|
| Generated aggregate | N/A with reason: none introduced. |
| Storage | local execution-plane source/test |
| Persistence | immutable in-memory records only; no durable runtime claim |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired MAO-T4 packet |
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
| Dependencies | T1-T3 accepted |
| Worker terminal status | `COMPLETE_PENDING_REVIEW` only |
| Next action | delegated local execution from clean post-sync HEAD |

## Acceptance Receipt Assertion Matrix

| Assertion | Evidence |
|---|---|
| source isolation | hash/exclusion tests |
| no self approval | actor identity negatives |
| dissent preservation | ledger replay tests |
| bounded revision | ceiling/escalation tests |

## Claim Boundary

This dispatch authorizes local reviewer-isolation and bounded-revision mechanics
only. It does not prove independent-review effectiveness, provider runtime,
closer/commit behavior, public readiness, or production orchestration.
