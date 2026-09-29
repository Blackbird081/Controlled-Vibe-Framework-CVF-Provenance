# CVF GC-018 Baseline - GC010 SCR-R2 T1J-R3 Pending Runtime Route Integration Interface Decision

Memory class: governed-dispatch-baseline

Status: READY_FOR_DISPATCH

Batch ID: GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION

Dispatch base head: `f6364b9f50c316b6a226e2be082a37524a05ccf7`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer/closer: orchestrator/reviewer

Worker target: one delegated decision worker

## Purpose

Resolve the complete integration-interface cluster left by the independently corrected T1J-R2 closure in one
bounded decision pass. Select an exact source-compatible composition for pending execution inside the existing
approval-resume product flow, or keep the chain parked. This baseline authorizes documentation and source inspection
only.

## Accepted Input

- Corrected T1J-R2 assessment and terminal at material commit `df5571b9106f086b22491103a37a5690e9c9ddc6`.
- Existing `/api/execute` route remains the only current guard and provider-attempt pipeline.
- Existing pending core and SQLite store provide reusable CAS and lifecycle primitives but no accepted product-route
  composition.
- T1K, formal T1/T2, source edits, runtime invocation, provider/live, public sync, deployment, and production remain
  parked.

## Required Comparison

The worker must compare all four complete interface candidates, not isolated sub-decisions:

| Candidate | Required complete interface |
| --- | --- |
| A | Move the mandatory gateway before approval creation, build the complete immutable pending payload there, create one pending record with the approval, and define resume/claim/begin/terminal/recovery plus SQLite ownership. |
| B | Preserve current approval-return ordering, create exactly one pending record at approved-resume time after the gateway, and prove deterministic identity/CAS prevents concurrent duplicate creation while defining the same full lifecycle. |
| C | Create the pending record in the approval `PATCH` transition and prove that boundary possesses every immutable payload and policy-snapshot input without inventing or weakening evidence. |
| D | Retain the chain parked because no bounded source-compatible interface can own all required inputs and recovery transitions safely. |

Each candidate must name exact creation, claim, begin, provider-attempt, terminal, audit, SQLite lifetime, cleanup,
and crash-recovery owners. Partial combinations are not ready terminals.

## Allowed Terminals

- `ROUTE_PRE_GATEWAY_PENDING_CREATION_INTERFACE_READY_FOR_T1K_DECISION`
- `RESUME_TIME_DETERMINISTIC_PENDING_CREATION_INTERFACE_READY_FOR_T1K_DECISION`
- `APPROVAL_PATCH_PENDING_CREATION_INTERFACE_READY_FOR_T1K_DECISION`
- `PARTIAL_READY_REQUIRES_ONE_NAMED_IMPLEMENTATION_PRECONDITION`
- `NO_SAFE_INTEGRATION_INTERFACE_RETAIN_FORMAL_T1_PARKED`
- `BLOCKED_SOURCE_CONTRADICTION`

`successorTrancheOpened` must be `NO`. A ready terminal names the smallest future T1K manifest but does not open or
implement it.

## Required Worker Outputs

1. `docs/assessments/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_2026-08-31.md`
2. `docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md`

No other path may be created or edited. Worker must not stage or commit.

## Decision / Baseline

T1J-R2 established that Candidate 2's CAS and lifecycle primitives are valuable but did not establish a complete
route composition. T1J-R3 succeeds only if it resolves route ordering, immutable payload/policy-snapshot construction,
SQLite runtime lifecycle, and authorized restart recovery together. A worker answer that resolves only one or two of
these members must select a partial or parked terminal.

## Evidence / Verification

- Read current source at the worker's captured `executionBaseHead`.
- Record an exact current call-order table and an exact proposed call-order table.
- Record a required-field provenance table for every member of `PendingAgentExecutionImmutablePayload` and current
  claim inputs.
- Record a crash-window recovery matrix for `CREATED`, `CLAIMED`, `EXECUTING`, and terminal states.
- Run the pre-implementation gate and worker-return fast gate; make zero provider/live calls.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Current route validates approval near handler entry, creates/returns `NEEDS_APPROVAL`, then invokes the mandatory gateway later | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 184-267; 497-576; 594 onward | `approvedRequestRecord`; `NEEDS_APPROVAL`; `runExecuteRouteMandatoryGateway` | `POST` | ACCEPT |
| Pending immutable payload requires approval binding, normalized intent, binding, original guard result, environment, and policy snapshot | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 238-328; 367-375 | `GuardPolicySnapshot`; `PendingAgentExecutionImmutablePayload` | pending core | ACCEPT |
| Claim and begin use a CAS lifecycle and process-local single-use grant | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 775-925; 939-970 | `ResumeAuthorityGrant`; `claimPendingExecution`; `beginPendingExecution` | pending core | ACCEPT |
| Explicit pre-start and ambiguous-executing recovery transitions exist | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 987-994 | `abandonBeforeStart`; `resolveAmbiguousExecutingCrash` | pending core | ACCEPT |
| Composition requires caller-supplied absolute SQLite path and exposes explicit close | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts` | lines 137-148; 220-221 | `buildPendingAgentExecutionRuntime`; `close` | pending composition | ACCEPT |
| Store declares a single-node local-file boundary and explicit close | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` | lines 433-509 | `deploymentBoundary`; constructor; `close` | SQLite store | ACCEPT |
| Only current harness pattern supplies path and closes explicitly | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.ts` | lines 11; 44-46; 124 | `dbPath`; `runtime.close` | local harness | ACCEPT |
| T1J-R2 reviewer correction names the four-member interface cluster and keeps T1K parked | accepted assessment | `docs/assessments/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md` | Independent Reviewer Correction | `ACCEPT_WITH_MATERIAL_CORRECTION` | T1J-R2 | ACCEPT |

## Dual Agent Surface Matrix

| Surface | Role | Authority | Boundary |
| --- | --- | --- | --- |
| `INTERNAL_AGENT` | orchestrator/reviewer | dispatch, independent review, repair, commit, continuity | no worker substitution claim |
| `EXTERNAL_AGENT_CLI_MCP` | one delegated worker | exact two-file evidence-only decision return | no commit, source edit, provider/live, or successor authority |
| adapter boundary | operator-mediated copy/return | transports packet and returned file paths | not a runtime adapter or proof of provider identity |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring" --role dispatcher --lifecycle-phase dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE |
| Disclosed defectIds | NONE |
| Dispatch impact | Preserve the common guard-orientation, checker-read-ahead, convergence, and literal-format controls. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | source-verification columns and dispositions; dispatch-ready status; scaffold provenance fields; convergence fields; prompt-envelope fields; no-commit worker-return profile |
| gateRunPurpose | Confirm authored packet shape after requirements were read, not discover requirements by failure. |
| claimBoundary | Read-ahead proves awareness of forward checker shape only; semantic source correctness remains reviewer-owned. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION --title "GC010 SCR-R2 T1J-R3 Pending Runtime Route Integration Interface Decision" --date 2026-08-31 --base f6364b9f50c316b6a226e2be082a37524a05ccf7 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/assessments/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md --include-worker-return-skeleton --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Replaced placeholders with the exact T1J-R3 decision contract, verified sources, candidates, terminals, and boundaries. |
| checkerReadAheadConfirmation | Applicable dispatch, prompt-envelope, scaffold-provenance, and review-cost checker sources were read before authoring. |
| docOnlyNewFields | Candidate interface rows, payload provenance table, current/proposed call-order table, recovery authority matrix. |
| claimBoundary | Scaffold provenance only; no runtime, provider, live, public, or production behavior claim. |

## Claim Boundary

This baseline opens one documentation-only integration-interface decision. It does not authorize implementation,
route reordering, schema/store edits, runtime construction, provider/live work, T1K, T2, public sync, deployment, or
production claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision dispatch with no public artifact or export authority.
