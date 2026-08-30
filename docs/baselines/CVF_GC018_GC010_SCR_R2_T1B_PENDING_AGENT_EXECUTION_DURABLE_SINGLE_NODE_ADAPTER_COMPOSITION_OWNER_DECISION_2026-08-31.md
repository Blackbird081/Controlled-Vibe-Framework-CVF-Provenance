# CVF GC-018 GC010 SCR-R2-T1B Pending Agent Execution Durable Single-Node Adapter And Composition Owner Decision

Memory class: governed-baseline

docType: baseline

Status: DISPATCHED_DECISION_ONLY

Batch ID: GC010-SCR-R2-T1B

Date: 2026-08-31

dispatchBaseHead: `25e3b22ed`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one documentation-only decision that selects the exact durable
single-node storage boundary and exact future composition owner for the
accepted T1A pending-execution core. The tranche distinguishes durable local
state from cross-process linearizable CAS, names a smallest future
implementation manifest, and implements nothing.

## Authority Chain

- Operator instructed continuation of the same GC010 system chain and granted
  full orchestrator/reviewer authority.
- Accepted T1A material commit: `f55b80826`.
- T1A completion:
  `docs/reviews/CVF_GC010_SCR_R2_T1A_PENDING_AGENT_EXECUTION_NON_PRODUCTION_CORE_IMPLEMENTATION_COMPLETION_2026-08-30.md`.
- Controlling T0B contract:
  `docs/assessments/CVF_GC010_SCR_R2_T0B_PENDING_AGENT_EXECUTION_SAFE_RESUME_CONTRACT_DECISION_2026-08-30.md`.
- Paired work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1B_PENDING_AGENT_EXECUTION_DURABLE_SINGLE_NODE_ADAPTER_COMPOSITION_OWNER_DECISION_2026-08-31.md`.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| Accepted pending-execution core | T1A completion and material `f55b80826` | decision may consume its public store interface as source evidence only | ACCEPT |
| Existing SQLite capability | cvf-web already depends on `better-sqlite3`; local adapters use WAL and transactions | compare as a candidate, do not infer CAS compatibility | ACCEPT |
| Production consumer | historical GC010 production-consumer tranche remains parked | no route/provider wiring in T1B | ACCEPT |

## Scope / Target / Owner Boundary

Worker creates exactly one assessment and one worker return. The assessment
must compare current file-backed, event-store, MAO, generic SQLite, route, and
new-owner candidates; select one exact adapter boundary and one exact
composition owner or retain the chain parked; define a smallest future file
manifest; and choose one terminal token.

Runtime, source, test, route, package, dependency, lockfile, configuration,
checker, workflow, continuity, provider/live, public-sync, deployment, and
production mutation are forbidden.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T1A exposes the store seam and only an in-memory implementation | runtime/schema | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 494, 590, 860, 911 | `PendingAgentExecutionStore`; `InMemoryPendingAgentExecutionStore`; claim/begin | cvf-web pending-execution core | ACCEPT |
| Approval file store is last-writer in-memory state and swallows persistence errors | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | lines 63, 85, 118 | `ApprovalStore`; `persist`; `FileBackedApprovalStore` | cvf-web approval owner | ACCEPT |
| Knowledge file store uses temp-write/rename but no versioned CAS | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | lines 134, 158 | `FileBackedKnowledgeStore`; `_persist` | cvf-web knowledge owner | ACCEPT |
| SOT3 evidence store serializes only inside one process | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | lines 278, 281, 296, 326-348 | `appendQueue`; atomic document replacement | cvf-web evidence owner | ACCEPT |
| MAO file store uses replay plus atomic rename without a cross-process lock/CAS | runtime | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 111, 130, 186, 443 | `MaoFileRunStore`; `atomicWriteJson` | Execution Plane MAO owner | ACCEPT |
| Generic SQLite adapters already use WAL and transactions but expose no conditional version/status update | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | lines 241-246, 259, 338-363 | `SQLiteEventListAdapter`; `SQLiteKeyValueAdapter` | cvf-web generic storage owner | ACCEPT |
| `/api/execute` is the current provider-call composition route and is already near its source-size ceiling | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 99, 797-859 | `POST`; `admitAndInvokeProvider` | cvf-web execute route | ACCEPT |
| Approval PATCH is decision-only and separately owns audit emission | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` | lines 57-119 | `PATCH`; `appendAuditEvent` | cvf-web approval decision route | ACCEPT |

## Candidate Families Required

1. Existing approval/knowledge file stores.
2. Existing SOT3 and MAO atomic-file patterns.
3. Existing generic SQLite adapters reused or extended.
4. Existing approval PATCH or `/api/execute` as direct composition owner.
5. A new specialized server-only SQLite pending-execution adapter plus a new
   server-only composition module.

Every family must receive exactly one classification:
`EXISTING_SOURCE_COMPATIBLE`, `EXISTING_SOURCE_INCOMPATIBLE`,
`PROPOSED_NEW_OWNER_COMPATIBLE`, or `NO_CURRENT_OWNER`.

## Required Decision Contract

The assessment must answer all of these:

1. Which exact adapter class and repo-relative source path own persistence?
2. Which exact composition function/module and path own future construction
   and orchestration without becoming a route or provider caller?
3. What single-node process model is supported, and what distributed/network
   filesystem claims remain forbidden?
4. What SQLite/file schema stores immutable payload, digest, status, version,
   claim metadata, attempt index, request correlation, and terminal reason?
5. What create transaction proves uniqueness and durable read-back?
6. What exact conditional CAS predicate produces one winner across Node
   processes on the same host?
7. What journal, synchronous, busy-timeout, transaction, and error settings
   are required, and which failures return zero grant authority?
8. How are corrupt, partially migrated, unknown-schema, and digest-mismatched
   rows handled without repair-on-read or silent fallback?
9. How do `CLAIMED`, `EXECUTING`, crash-before-start, and ambiguous-after-start
   recovery preserve T0B/T1A semantics?
10. Which T1A core symbols may the adapter import, and how is duplicate state
    validation avoided?
11. Why are the four non-selected candidate families unsafe or owner-wrong?
12. What smallest future implementation/test manifest is authorized for later
    consideration, with no route/provider/audit integration?
13. What separate evidence would be required before a production consumer,
    cross-node store, route, provider admission, or audit integration opens?

## Allowed Terminal Tokens

Select exactly one:

- `SPECIALIZED_SQLITE_SINGLE_NODE_ADAPTER_AND_COMPOSITION_OWNER_SELECTED`
- `EXISTING_OWNER_REUSE_SELECTED`
- `NO_SAFE_DURABLE_COMPOSITION_RETAIN_PARKED`

## Acceptance Criteria

- Exactly five candidate families are compared and classified.
- Adapter and composition owner paths are exact, non-colliding, and
  source-compatible, or the parked token explains the blocking fact.
- Durability, single-node cross-process CAS, and distributed safety are not
  conflated.
- The CAS winner predicate and fail-closed persistence/error semantics are
  implementation-ready but documentation-only.
- The future manifest is minimal and creates no route/provider authority.
- Exactly one terminal token appears as the selected result.
- Worker returns two uncommitted files and reports zero provider/external calls.

## Decision / Baseline / Proposed Tranche

T1B is a documentation-only selection gate between the accepted T1A core and
any later durable implementation. A selected result may name a future T1C
manifest, but this baseline opens no implementation tranche automatically.

## Evidence / Verification

Required evidence is a fresh execution base, exact source reads and negative
searches, five-family classification matrix, thirteen ordered answers, one
selected terminal token, exact two-file diff, worker-return fast gate, zero
external/provider calls and no commit.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010-SCR-R2-T1B --title "Pending Agent Execution Durable Single-Node Adapter And Composition Owner Decision" --date 2026-08-31 --base 25e3b22ed --commit-mode WORKER_MUST_NOT_COMMIT --dependency "accepted T1A core material f55b80826; decision-only durable single-node adapter and composition ownership" --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit and adapter trigger profiles |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact decision scope, five candidates, thirteen questions, terminal tokens and source evidence |
| checkerReadAheadConfirmation | dispatch, lifecycle, read-ahead, trace, delta, worker-return and public-disposition checkers read |
| docOnlyNewFields | candidateCompatibilityClass; singleNodeCasBoundary; compositionOwnerDisposition |
| claimBoundary | authoring provenance only; no adapter/runtime behavior |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | normal documentation-only decision controls remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | source-table columns and dispositions; dispatch envelope fields; worker fast-doc profile; trace and delta table labels; public disposition tokens |
| gateRunPurpose | confirmation evidence before dispatch, not first discovery or runtime proof |
| claimBoundary | artifact conformance only; worker/reviewer own semantic correctness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private decision-only system-chain dispatch; no public artifact or
release claim is authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | paired work order | dispatch status | PENDING_WORKER_RETURN |
| Completion or reviewer artifact | assessment and worker return | reviewer-owned | PENDING_REVIEW |
| Roadmap state | historical GC010 roadmap | production consumer remains parked | PASS |
| Registry JSON | active state | steward-owned | N/A with reason: dispatch precedes continuity sync |
| Registry Markdown | front door/handoff | steward-owned | N/A with reason: separate continuity commit |
| External evidence digest | N/A with reason: no external evidence | none | N/A with reason |
| System loop interlock | successor flag NO | no automatic successor | PASS |
| Session continuity | post-material dispatch sync | steward-owned | PENDING |

## Claim Boundary

This baseline authorizes exactly one documentation-only adapter/composition
decision. It does not create or modify storage, schema, source, tests, route,
package exports, provider admission/invocation, durable audit, public sync,
deployment, cross-node safety, production consumer, or production readiness.
