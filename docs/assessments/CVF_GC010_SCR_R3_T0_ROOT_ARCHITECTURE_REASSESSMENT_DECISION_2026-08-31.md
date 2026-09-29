# CVF GC010 SCR R3 T0 Root Architecture Reassessment Decision

Memory class: FULL_RECORD

docType: assessment

Status: REVIEWER_ACCEPTED_FINAL

Batch ID: GC010-SCR-R3-T0

Date: 2026-08-31

successorTrancheOpened: NO

Selected terminal: `ROOT_ARCHITECTURE_REASSESSED_NO_TRUTHFUL_PRODUCT_OWNER_RETAIN_PARKED`

## Purpose

Close the GC010 pending-agent-execution question at the architecture level after
SCEC correctly stopped the T1J-R1-through-R3 narrow decision chain. This packet
adjudicates the complete owner cluster once: route order, immutable payload
provenance, atomic execution claim, deployment topology, SQLite lifecycle,
provider terminalization, and authenticated restart recovery.

The operator authorized the orchestrator/reviewer to complete this decision
directly. No external worker dispatch is required, no implementation is implied,
and no narrower successor is opened.

## Source Authority

| Source | Accepted fact |
| --- | --- |
| `docs/reviews/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_WORKER_RETURN_2026-08-31.md` | The real approval-resume caller has a validation-to-delete TOCTOU window; early deletion is not failure recovery. |
| `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md` | SQLite CAS and crash states are real primitives, but route order, payload construction, lifecycle, and recovery ownership were unresolved. |
| `docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md` | The accepted consolidated precondition is `ACCEPTED_ROUTE_NATIVE_PRODUCTION_PENDING_EXECUTION_COMPOSITION_OWNER_CONTRACT`; the worker's two-barrier and unchanged-order claims were rejected. |
| `docs/reviews/CVF_SCEC_E1_GC010_T1J_R1_R3_EFFECTIVENESS_RECONCILIATION_WORKER_RETURN_2026-08-31.md` | Two non-decreasing blocker transitions require architecture reassessment and forbid automatic same-problem T1J-R4. |
| `docs/reviews/CVF_SCEC_E3_LOCATOR_SNAPSHOT_EFFECTIVENESS_VALIDATION_WORKER_RETURN_2026-08-31.md` | The SCEC evidence-binding foundation is effective; this architecture decision may rely on the accepted blocker history without reopening checker work. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | Approval validation occurs at lines 177-268; approved consumption/deletion occurs at 497-513; the mandatory gateway and `guardResult` occur later at 577-605; provider invocation begins at 779-810. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | `ApprovalStore` is a process-local `Map` with whole-file persistence and no transaction/CAS state machine. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | The immutable payload requires normalized intent, actor/session/runtime binding, original guard result, environment identity, and a full guard-policy snapshot; its environment currently permits only `single_process_non_production`. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` | The specialized SQLite store provides transactional CAS and durable local state, not distributed deployment ownership. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts` | The runtime requires a caller-supplied DB path and explicit `close()`; it intentionally owns no route, environment, audit, or recovery authority. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.ts` | The sole non-test owner is a bounded local harness that constructs and closes one runtime per invocation. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts` and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | The Web package can load `better-sqlite3`, but these files do not declare persistent-disk, singleton-process, serverless, multi-instance, or recovery-operator guarantees. |

## Root Architecture Question

Can current committed source truthfully name one product owner that atomically
binds an approved request to exactly one provider-execution lifecycle while
preserving the single guard/admission chain and recovering durable `CLAIMED` or
`EXECUTING` records after process loss?

Answer: no. The primitives exist, but the product topology and authority needed
to compose them do not.

## Consolidated Blocker Ledger

| Blocker | Current evidence | Decision |
| --- | --- | --- |
| Route order and consumption | Approval is consumed before the only real guard result exists. Moving consumption is a behavior change with audit/failure consequences. | RETAINED |
| Immutable payload provenance | No route-native builder owns normalized intent, session identity, production environment, or guard-policy rows/version/config digests. | RETAINED |
| Atomic claim | SQLite CAS can be authoritative, but JSON approval deletion and SQLite creation/claim cannot form one transaction. | RETAINED |
| Deployment topology and lifecycle | A local SQLite singleton is safe only with one long-lived Node process and persistent local disk; current deployment authority states neither. | RETAINED |
| Recovery authority | `abandonBeforeStart` and `resolveAmbiguousExecutingCrash` are callable primitives with zero product caller and no authenticated actor/endpoint policy. | RETAINED |
| Provider terminalization | The route has initial calls, retries, early responses, and exception paths; no current owner maps every post-begin exit to one durable terminal state. | RETAINED |

No blocker is marked resolved merely because an implementation could be
imagined. Under SCEC, an architectural choice requires accepted source or an
explicit operator-owned product constraint, not a reviewer-authored fiction.

## Candidate Comparison

| Candidate | Result | Reason |
| --- | --- | --- |
| Compose current pending runtime directly into `/api/execute` | `EXISTING_SOURCE_INCOMPATIBLE` | Required payload arrives only after the gateway, while current approval consumption occurs before it; production environment and recovery authority are absent. |
| Upgrade `ApprovalStore` into the execution owner | `EXISTING_SOURCE_INCOMPATIBLE` | Whole-file persistence is not transactional CAS and cannot own crash ambiguity around provider calls. |
| Declare process-global SQLite ownership in a new route module | `NO_CURRENT_PRODUCT_TOPOLOGY_OWNER` | Technically constructible, but unsafe to claim without persistent-disk and single-instance deployment guarantees. |
| Introduce a distributed transactional store/recovery service | `PROPOSED_NEW_SYSTEM_WITHOUT_OWNER` | No selected dependency, schema owner, deployment authority, or operational recovery role exists. |
| Retain the proven non-production core and park product composition | `ACCEPTED` | Preserves working primitives, avoids false exactly-once/production claims, and replaces tranche churn with conjunctive reopen conditions. |

## Reopen Contract

GC010 product composition may reopen only when one decision packet supplies all
of the following together:

1. an explicit deployment topology: either one long-lived Node process with
   persistent local disk, or a named external transactional store;
2. one route-native payload adapter owning normalized intent, actor/session
   binding, guard-policy version/config digests, and a truthful environment;
3. one exact order covering approval validation, gateway, durable create,
   atomic claim, audit, begin, every provider attempt, and terminalization;
4. an authenticated recovery owner and policy for durable `CLAIMED` and
   `EXECUTING` records after restart;
5. adversarial tests for concurrent resume, create conflict, pre-call failure,
   post-call ambiguity, retry, and every early-return path after begin.

These are conjunctive facts, not five future tranches. A reopen packet missing
any item terminates `NO_VIABLE_PRODUCT_OWNER_RETAIN_PARKED` without another
narrow follow-up.

## Decision

`ROOT_ARCHITECTURE_REASSESSED_NO_TRUTHFUL_PRODUCT_OWNER_RETAIN_PARKED`.

The issue is complete as an architecture decision. Existing T1A/T1C
non-production primitives remain accepted and unchanged. T1J-R4 is cancelled as
an automatic successor; T1K and T2 do not open. This is not a claim that durable
approval resume is impossible. It is a claim that current source lacks the
product/deployment authority required to implement it truthfully.

## Evidence / Verification

- Re-read the accepted independent-review corrections for T1J-R1, R2, and R3.
- Re-read the accepted SCEC-E1 stop evidence and SCEC-E3 effectiveness closure.
- Reconstructed current `/api/execute` ordering from approval validation through
  mandatory gateway and provider invocation.
- Compared `ApprovalStore`, pending core, SQLite store, composition owner, local
  harness, Web package dependencies, and Next configuration directly.
- Confirmed zero source/test/runtime mutation and zero provider/network call.

## Epistemic Process Block

### Expected Result / Prediction

If the prior tranche churn came from a root ownership gap, direct source
reconstruction would show that no single current module owns all route,
transaction, topology, and recovery facts.

### Evidence Comparison

The prediction matched. Each candidate solves only a subset, and the missing
facts are product/deployment decisions rather than additional local code search.

### Contradiction Or Gap Disposition

No contradiction. The accepted T1J blocker expansion is preserved. The SCEC
foundation did its intended job by forcing this consolidated decision.

### Claim Update

GC010 is no longer pending another narrow tranche. It is parked under one
machine-readable conjunctive reopen contract.

## Finding-To-Governance Learning Disposition

The reusable learning is already owned by SCEC: repeated non-decreasing blocker
sets force architecture reassessment and prohibit automatic successors. No new
checker or standard is required from this adjudication.

Runtime/provider/cost learning lane: N/A_WITH_REASON - no provider or live
execution occurred and no production topology was selected.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance architecture adjudication; no public-sync batch is
authorized.

## Claim Boundary

This assessment closes the GC010 architecture question as parked. It creates no
runtime, route, store, API, provider/live, deployment, production, public-sync,
T1J-R4, T1K, or T2 authority.
