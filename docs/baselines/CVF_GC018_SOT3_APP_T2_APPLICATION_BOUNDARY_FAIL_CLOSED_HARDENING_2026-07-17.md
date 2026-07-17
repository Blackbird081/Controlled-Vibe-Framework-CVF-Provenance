# CVF GC-018 Baseline - SOT3-APP-T2 Application Boundary Fail-Closed Hardening

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: SOT3-APP-T2

Dispatch base head: `e023be9f9`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through standing roadmap-completion instruction

Reviewer owner: independent reviewer/closer

Worker target: delegated implementation worker

## Purpose

Release one bounded downstream implementation tranche that prevents blocked,
expired, review-held, or obligation-bearing contexts from reaching governed
execution and proves that rejected freeze paths create no evidence record.

## Source / Predecessor Evidence

T1 closure commit `f193bf2e9`, its completion review, contract ratification,
and direct-invocation ledger are the predecessor evidence. The accepted T0B
aggregate digest identifies the external sibling corpus.

## Decision / Baseline

Decision: dispatch the exact bounded T2 implementation below. Only `ALLOW` is
continuable to the execution fake until obligation, escalation, or review-hold
owners exist and are separately authorized.

## Proposed Tranche

The tranche owns nine exact external paths and two private review outputs. All
other application, CVF, runtime, provider, and later-roadmap scope is excluded.

## Evidence / Verification

Required evidence is the nine-path before/after SHA-256 manifest, deterministic
zero/one call counters, focused tests, typecheck/test output, exact provenance
status, unchanged HEAD, and the worker-return fast gate.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T1 contract inventory closure | `docs/reviews/CVF_SOT3_APP_T1_R3_COMPLETION_REVIEW_2026-07-17.md`; material commit `f193bf2e9`; status closed bounded with reviewer repairs | accepted caller-edge closure with zero unresolved | SATISFIED |
| roadmap authorization | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md`; T2 row and acceptance criteria | T1 closed and fresh source verification completed | SATISFIED |
| clean packet-authoring base | session-sync commit `e023be9f9` | no unresolved worker changes | SATISFIED |
| T3 release | T2 independent closure does not exist | keep later tranche parked | SATISFIED_WITH_HOLD: T3 execution remains parked |

## Source Verification Block

| Claimed item | Fact class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| context usability gate exists | RUNTIME_BEHAVIOR | `docs/reviews/CVF_SOT3_APP_T1_DOWNSTREAM_CONTRACT_RATIFICATION_AND_CONTINUATION_MATRIX_2026-07-17.md` | Source Contradiction And Blocker Ledger row 1 | `GovernedContextPackage.assertUsable` | `packages/domain/src/entities/context-package.ts` | ACCEPT |
| usability gate is unwired | RUNTIME_BEHAVIOR | `docs/reviews/CVF_SOT3_APP_T1_DOWNSTREAM_CONTRACT_RATIFICATION_AND_CONTINUATION_MATRIX_2026-07-17.md` | T2 Implementation Requirements item 1 | `GovernedOutputService.create` | `packages/application/src/services/governed-output.service.ts` | ACCEPT |
| five route decisions and continuations | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T1_DOWNSTREAM_CONTRACT_RATIFICATION_AND_CONTINUATION_MATRIX_2026-07-17.md` | Five-Value Continuation Matrix | `route_decision` | `ContextPackage` | ACCEPT |
| governed execution call boundary | RUNTIME_BEHAVIOR | `docs/reviews/CVF_SOT3_APP_T1_R3_DIRECT_INVOCATION_AND_CALLER_RESULT_TRUTH_CORRECTION_2026-07-17.md` | Direct Invocation And Caller Result Ledger row 17 | `GovernedExecutionAdapter.execute` | `GovernedOutputService.create` | ACCEPT |
| phase freeze gate precedes evidence write | RUNTIME_BEHAVIOR | `docs/reviews/CVF_SOT3_APP_T1_R3_DIRECT_INVOCATION_AND_CALLER_RESULT_TRUTH_CORRECTION_2026-07-17.md` | Direct Invocation And Caller Result Ledger rows 19-20 | `assertFreezeAllowed` | `ReviewFreezeService.freeze` | ACCEPT |
| identity middleware rejects missing actor | RUNTIME_BEHAVIOR | N/A with reason: canonical external evidence digest in this baseline | external source `apps/api/src/middleware/identity.middleware.ts`, `registerIdentityMiddleware` | `x-actor-id` | Fastify preHandler | ACCEPT |
| phase middleware lacks explicit return after reply | RUNTIME_BEHAVIOR | N/A with reason: canonical external evidence digest in this baseline | external source `apps/api/src/middleware/cvf-governance.middleware.ts`, `registerCVFGovernanceMiddleware` | `reply.send` | Fastify preHandler | ACCEPT |
| error response exposes raw message | RUNTIME_BEHAVIOR | N/A with reason: canonical external evidence digest in this baseline | external source `apps/api/src/middleware/error.middleware.ts`, `registerErrorMiddleware` | `error.message` | Fastify error handler | ACCEPT |
| output controller is a static reference implementation | RUNTIME_BEHAVIOR | N/A with reason: canonical external evidence digest in this baseline | external source `apps/api/src/controllers/output.controller.ts`, `OutputController.create` | `REFERENCE_IMPLEMENTATION` | `OutputController` | ACCEPT |
| output route constructs static controller | RUNTIME_BEHAVIOR | N/A with reason: canonical external evidence digest in this baseline | external source `apps/api/src/routes/outputs.routes.ts`, `registerRoutes` | `OutputController` | Fastify route registration | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime claim |
|---|---|---|
| `EXECUTION_CALL_COUNT` | prove rejected contexts do not invoke the execution fake | none |
| `EVIDENCE_WRITE_COUNT` | prove rejected freeze paths do not write evidence | none |
| `EXTERNAL_SOURCE_HASH_MANIFEST` | preserve before/after identity for non-Git sibling source | none |

## Allowed Scope

External downstream root:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.

Exactly these external source/test paths may be modified or created:

- `packages/application/src/services/governed-output.service.ts`
- `packages/application/src/services/review-freeze.service.ts`
- `apps/api/src/app.ts`
- `apps/api/src/controllers/output.controller.ts`
- `apps/api/src/routes/outputs.routes.ts`
- `apps/api/src/middleware/cvf-governance.middleware.ts`
- `apps/api/src/middleware/error.middleware.ts`
- `tests/integration/application-boundary-negative.test.ts`
- `apps/api/src/middleware/application-boundary.middleware.test.ts`

Exactly two private-provenance worker outputs are allowed:

- `docs/reviews/CVF_SOT3_APP_T2_EXTERNAL_SOURCE_PATCH_AND_TEST_EVIDENCE_2026-07-17.md`
- `docs/reviews/CVF_SOT3_APP_T2_WORKER_RETURN_2026-07-17.md`

## Forbidden Scope

- no other external source, configuration, lockfile, fixture, or test path;
- no CVF Core, registry, checker, hook, session, roadmap, baseline, or work-order mutation;
- no provider, network, live API, browser, UI, public-sync, push, or production action;
- no T3 or later-tranche work;
- no Git initialization or commit inside the non-Git sibling source;
- no worker commit or staging in the private provenance repository.

## Acceptance Criteria

1. `GovernedOutputService.create` invokes the existing domain usability gate
   before any execution call.
2. Only `ALLOW` may reach `GovernedExecutionAdapter.execute` in this tranche.
   `BLOCK`, expired contexts, `WARN`, `ESCALATE`, and `REVIEW_REQUIRED` fail
   closed with stable `SOT_*` errors and `EXECUTION_CALL_COUNT=0`.
3. `WARN` and `ESCALATE` are not silently treated as plain `ALLOW`; absent an
   obligation/escalation owner they stop before execution.
4. A failed review or failed phase-freeze decision yields
   `EVIDENCE_WRITE_COUNT=0` and no freeze record.
5. Missing phase headers return once with 428; missing identity remains 401.
6. API errors expose stable safe tokens and request identity, not arbitrary raw
   internal error text.
7. Output controller/route use an injected application boundary in tests; no
   static reference payload may claim successful output creation.
8. Focused tests and full available typecheck/test commands pass without a
   provider, network, browser, or live service.
9. The evidence artifact records SHA-256 before/after hashes for every allowed
   external path, exact test counts, call counters, and a full changed-path
   manifest.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Closure evidence |
|---|---|---|
| identity and phase/guard decisions | middleware return/redaction tests | focused API middleware test |
| all decision consumers | five-value output-service matrix | execution-call counter |
| controller-service wiring | injected output application boundary | controller/route focused test |
| redaction | safe error serialization | no raw sentinel in response |
| freeze | phase/review rejection before evidence | evidence-write counter |
| no blocked output/provider lane | no execution call on all negative cases | negative integration test |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`downstream application boundary implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "downstream application boundary implementation" --role worker --lifecycle-phase pre-implementation --json`

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | delegated implementation worker followed by independent reviewer/closer |
| phase | implementation worker return |
| baseHeadFor(phase) | dispatchBaseHead=`e023be9f9`; executionBaseHead=worker captures committed dispatch HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | nine exact external paths plus two exact provenance review outputs |
| traceScope(phase, actor) | worker records external hashes, commands, counters, provenance Git boundary, and no-commit evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns private-provenance material commit |
| crossBatchIsolation | no unrelated external or provenance path may coexist |
| nextMoveSurfaces | reviewer/session steward only following an accepted T2 completion review |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_APP_T2_COMPLETION_REVIEW_2026-07-17.md` |
| reviewerOwnedClosurePaths | paired baseline; paired work order; roadmap; two worker outputs; completion review; protected continuity in a later sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-APP-T2 --title "Application Boundary Fail-Closed Hardening" --date 2026-07-17 --base e023be9f9 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T1 closure f193bf2e9" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic worker dispatch plus no-commit worker-return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact external-source boundary, T1-derived semantics, counters, hash evidence, and two-output return |
| checkerReadAheadConfirmation | dispatch, handoff, closure, worker-return, external absorption, encoding, public disposition, and file-size checkers reviewed |
| docOnlyNewFields | `EXECUTION_CALL_COUNT`; `EVIDENCE_WRITE_COUNT`; `EXTERNAL_SOURCE_HASH_MANIFEST` |
| claimBoundary | scaffold use does not prove implementation or runtime behavior |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Roadmap-To-Work-Order Trace Matrix; ADIF Defect Registry Disclosure; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm evidence supporting a source-verified T2 dispatch packet |
| claimBoundary | structural confirmation only; no implementation, test, or runtime proof |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this artifact | `Status: DISPATCH_READY` | PASS |
| Work order status | paired T2 work order | `Status: DISPATCH_READY` | PASS |
| Roadmap state | SOT3-APP roadmap | `Status: SOT3_APP_T2_DISPATCHED_WORKER_NEXT` | PASS |
| Registry JSON | existing GC-051 aggregate | no new provenance source path until worker outputs exist | PASS |
| Registry Markdown | existing registry documentation | unchanged at dispatch | PASS |
| Completion or reviewer artifact | future T2 completion review | reviewer-owned following worker return | N/A with reason |
| External evidence digest | accepted T0B external corpus digest | 336-file aggregate sha256 `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee`; worker must refresh allowed-path hashes | PASS |
| System loop interlock | T1 closure -> T2 worker -> independent review | T3 and later parked | PASS |
| Session continuity | protected sync after material dispatch commit | separate commit | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private downstream implementation packet; no public-safe artifact set or
public-sync authorization exists.

## Claim Boundary

This baseline authorizes only the exact T2 external-source/test changes and two
private review outputs. It does not prove implementation success, authorize
provider/live/public work, release T3, or permit a worker commit.
