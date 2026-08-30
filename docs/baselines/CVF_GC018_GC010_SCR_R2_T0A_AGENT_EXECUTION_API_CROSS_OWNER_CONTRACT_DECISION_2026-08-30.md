# CVF GC-018 Baseline - GC010 SCR R2 T0A Agent Execution API Cross-Owner Contract Decision

Memory class: governed-dispatch-baseline

Status: DISPATCHED_DECISION_ONLY

Batch ID: GC010-SCR-R2-T0A

Dispatch base head: d98a6b2c6

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator and orchestrator/reviewer

Reviewer owner: orchestrator/reviewer

Worker target: delegated worker role

## Purpose

Resolve the smallest product-owned contract for one new Web Agent Execution
API system chain without implementing it. The decision must bind the existing
`AgentExecutionRuntime`, Web approval store/API, provider-attempt admission,
durable audit store, and response boundary without duplicating the accepted
`/api/execute` chain.

## Authority And Decision

The operator directed continued system-chain development and explicitly
authorized the orchestrator/reviewer to proceed. GC010-SCR-R1-T0 remains
closed with `NO_VIABLE_CONSUMER_RETAIN_PARKED`; this fresh T0A does not rewrite
that source finding. It supplies the missing product-owner decision and tests
whether a new isolated API chain can be specified safely before implementation.

## Decision / Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Decision | Open one decision-only cross-owner contract tranche. |
| Product trigger candidate | a new isolated `POST /api/agent-execution` route, subject to worker source verification and interface viability |
| Existing route boundary | `POST /api/execute` remains unchanged and must not be wrapped by AER |
| Proposed tranche | GC010-SCR-R2-T0A documentation-only assessment and worker return |
| Successor | no T1 opens automatically |

## Authorized Scope

- Read current Guard Contract and cvf-web source.
- Compare synchronous, asynchronous submit/resume, and parked designs.
- Name exact existing owner symbols, interface gaps, identity bindings,
  terminal states, and the smallest possible future write/test manifest.
- Create exactly one assessment and one worker return.

## Forbidden Scope

- No TypeScript, package, route, test, checker, hook, workflow, or session edit.
- No creation of `/api/agent-execution` in this tranche.
- No modification of `/api/execute` or its accepted gateway/admission chain.
- No provider/API/network/browser call, credential read, public sync, deploy,
  production claim, or worker commit.
- No automatic release of implementation, live proof, or GC010-SCR-R1 T1-T5.

## Completion Standard

The worker must identify whether one exact design can preserve single guard
evaluation, exactly-once approval settlement, exactly-once provider-attempt
admission per actual call, and durable terminal audit projection. A ready
decision requires an exact trigger, request/actor/session/approval/attempt/
receipt identity mapping, failure semantics, and complete future manifest.

## Evidence / Verification

Use current committed source at the worker execution base, direct symbol and
path searches, the pre-implementation gate, worker-return fast gate, unchanged
HEAD, empty staged diff, and an exact two-path untracked/modified status.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| AER owns guard then provider execution | runtime source | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | `ExecutionProvider`; `AgentExecutionRuntime.execute`; `runAwaitingApproval` | `AgentExecutionRuntime` | Guard Contract runtime | ACCEPT |
| AER is not package-exported | package source | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | exports/files and runtime-helper exports | no AER entry | Guard Contract package | ACCEPT |
| Web owns per-attempt admission and invocation | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-attempt-admission.ts` | `admitAndInvokeProvider` | function at current source | cvf-web | ACCEPT |
| Web owns durable audit append/read | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | `appendAuditEvent`; `readAuditEvents` | named functions | cvf-web | ACCEPT |
| Web owns approval persistence and decision API | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` | approval store; GET/PATCH handlers | current approval record/API owner | cvf-web | ACCEPT |
| Existing execute route already owns a separate accepted chain | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | gateway call, initial/retry admission, reconciliation | `POST` | cvf-web | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Four planned artifact paths | `Test-Path` returned false for baseline, work order, assessment, and worker return before authoring | ACCEPT |
| Batch collision | `rg -n "GC010-SCR-R2-T0A|AGENT_EXECUTION_API_CROSS_OWNER" docs CVF_SESSION` returned no match before authoring | ACCEPT |
| Existing route collision | the selected candidate route is currently absent; worker must recompute from its execution base | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010-SCR-R2-T0A --title "Agent Execution API System Chain Cross Owner Contract Decision" --date 2026-08-30 --base d98a6b2c6 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "operator-authorized decision-only amendment; GC010-SCR-R1-T0 retained parked; no implementation" --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-verified decision-only scope, exact outputs, terminal tokens, and no-successor boundary |
| checkerReadAheadConfirmation | work-order dispatch quality, dispatch prompt envelope, lifecycle hygiene, checker read-ahead, worker-return quality, and structural checkers read |
| docOnlyNewFields | product trigger decision; cross-owner identity map; approval lifecycle map; future manifest |
| claimBoundary | dispatch authoring provenance only; no runtime behavior is implemented |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector "system-chain decision-only" --risk-ceiling MEDIUM --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF-specific control was returned; normal dispatch controls remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | dispatch envelope fields; source table columns; no-commit handoff fields; worker-return full-gate fields; public disposition; claim boundary |
| gateRunPurpose | confirmation evidence after direct checker inspection, not first discovery |
| claimBoundary | shape readiness only; no semantic acceptance or runtime proof |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private decision-only dispatch authority with no public
artifact, runtime behavior, or release claim.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | paired work order | `Status: DISPATCHED_DECISION_ONLY` | PENDING_WORKER_RETURN |
| Completion or reviewer artifact | worker return reviewer addendum or separate completion | reviewer-owned | PENDING_REVIEW |
| Roadmap state | prior GC010 roadmap remains closed/parked | no historical rewrite | PASS |
| Registry JSON | active session state | session-sync steward only | N/A with reason: dispatch material precedes continuity sync |
| Registry Markdown | active handoff/front door | session-sync steward only | N/A with reason: separate continuity commit |
| External evidence digest | N/A with reason: no external evidence consumed | zero external calls required | N/A with reason |
| System loop interlock | no successor opens automatically | explicit in work order | PASS |
| Session continuity | separate post-commit sync | reviewer/closer owned | PENDING |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| Runtime receipt | N/A with reason: documentation-only decision | N/A_WITH_REASON |
| Worker return | exact assessment plus return | PENDING |
| Provider calls | zero | PENDING |
| Closure claim | bounded architecture decision only | PENDING |

## Claim Boundary

This baseline authorizes only a fresh system-chain product-contract decision.
It does not reopen the closed R1 T0 finding, implement a route or adapter,
settle an approval, call a provider, or establish production readiness.
