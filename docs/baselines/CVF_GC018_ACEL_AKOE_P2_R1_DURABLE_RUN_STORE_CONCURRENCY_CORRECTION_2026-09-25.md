# CVF GC-018 Baseline - ACEL AKOE-P2-R1 Durable Run Store Concurrency Correction

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-AKOE-P2-R1

Dispatch base head: `fee4316f1affdcf2675c4e9832d96ebc7b917402`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local reviewer/closer

Reviewer owner: Local reviewer/closer distinct from the worker phase

Worker target: shared-workspace `INTERNAL_AGENT` runtime-correction role

## Purpose

Authorize one bounded correction of the confirmed `MaoFileRunStore.appendEvent`
lost-update race. The tranche must serialize the complete per-run
load/replay/append/write transaction, convert the P2 defect probe into a
fail-closed durable-winner regression, prove real second-process exclusion and
exception-safe lock release, and return all changes uncommitted.

## Authorization / Decision

The operator explicitly authorized AKOE-P2-R1 runtime correction and machine-
gate hardening on 2026-09-25. The machine-gate correction and truthful blocked
P2 evidence are committed at `fee4316f1`; this baseline opens only the runtime
repair needed to resolve `run_store_concurrent_write_lost_race`.

This baseline does not close P2, open P3/P4, alter another runtime owner,
authorize provider/live/public/deployment work, or permit worker commit.

## Scope

Allowed:

- modify `MaoFileRunStore.appendEvent` and its failure vocabulary only as
  needed for a per-run fail-closed transaction;
- reuse the existing `acquireLock`/`releaseLock` persistence primitive rather
  than create a second lock protocol;
- modify the durable-run-store test owner and the existing P2 launcher defect
  probe;
- create one bounded Vitest peer fixture that invokes the real production
  `MaoFileRunStore.appendEvent` path from a second OS process;
- create the exact P2-R1 worker return and detached final-hash receipt.

Forbidden:

- new runtime, queue, scheduler, store family, daemon, watcher, or adapter;
- change to delegation-ledger locking semantics, package dependencies,
  production launcher behavior, contracts, public exports, or session state;
- weakening the defect probe to accept two successes with one lost event;
- timeout-as-exclusion evidence, in-process-only concurrency proof, automatic
  stale-lock takeover, or success before durable persistence;
- provider/network/live/public/deployment/production action, staging, or
  worker commit.

## Baseline Invariants

1. One lock identity is derived from the same canonical per-run snapshot
   identity; unrelated runs remain independent.
2. Lock ownership covers the full load/replay/append/atomic-write sequence.
3. Two conflicting terminal attempts cannot both return success unless both
   are durably present and valid; for the current state machine exactly one
   attempt wins durably and the other fails closed.
4. Lock-acquisition failure, stale-lock detection, replay rejection, write
   failure, and injected post-acquire failure perform no partial mutation.
5. Every acquired lock is released through an exception-safe path; a later
   real peer can acquire after a failed transaction.
6. No automatic stale-lock stealing or deletion is introduced.
7. `createRun`, `resumeRun`, discovery, replay validation, idempotency, and
   unrelated-run concurrency retain existing behavior.
8. The worker does not convert the intentionally failing defect evidence by
   changing only the assertion; the production repair must make the durable-
   winner assertion true.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| AKOE-P2 blocked worker evidence | `docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md`, SHA-256 `a44fe1cf35db9b4b65a5b4439432665a80fa814a50b204ef82f96214bc6762d1`, committed at `fee4316f1` | names the exact outside-manifest race and no broader blocker | SATISFIED |
| Machine-gate correction | ADIF-0059, standard, checker, and tests committed with the blocked evidence at `fee4316f1` | P2-R1 must not edit or bypass those guards | SATISFIED |
| Operator scope decision | explicit confirmation on 2026-09-25 | limited to runtime fix plus already-completed machine-gate hardening | SATISFIED |
| Dispatch continuity | this packet is not yet materially committed | later handoff marker and current-authority sync must precede worker edits | REQUIRED_BEFORE_IMPLEMENTATION |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| run-store append is an unguarded read-modify-write | implementation fact | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 186-215 | `appendEvent(` | durable run store | ACCEPT |
| run-store atomic rename does not serialize writers | implementation fact | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 443-466 | local `atomicWriteJson` | durable run store persistence | ACCEPT |
| current P2 probe observes two success results and fewer than two durable terminal events | executable defect evidence | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.worker.launcher.test.ts` | test beginning line 470 | `DEFECT PROBE` cancel/completion race | launcher test owner | ACCEPT |
| canonical lock primitive uses exclusive create, retry, stale fail-closed, and token-bound release | reusable implementation | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.delegation.ledger.persistence.ts` | lines 104-174 | `acquireLock`; `releaseLock` | delegation persistence helper | ACCEPT |
| delegation store holds the lock over load/replay/mutate/write | sibling-owner precedent | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.delegation.ledger.store.ts` | `withCas` around lines 688-742 | `withCas` | delegation ledger store | ACCEPT |
| durable-run-store focused test owner exists | test owner | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts` | `describe("MaoFileRunStore")` | run-store tests | ACCEPT |

## Exact Input Evidence

| Input | SHA-256 | Use |
|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `4fd1b4ee9f3ecff0930998da14bc2d2303348375329cda14faa0ae5dca356379` | production defect owner |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts` | `19d22b89beec59c553067ca8a37c0392a4f5fc78fe45b61d5337411d328c789f` | focused regression owner |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.worker.launcher.test.ts` | `1aeaa2e4aa2a7a7a182ea501cee42831f9f4b0b22619b03cb9b49ff9201f4c2e` | P2 defect probe |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.delegation.ledger.persistence.ts` | `6364b61fdc22b37387ab431eae4b48d5dbe0a05be5406f89088be543421c7499` | read-only reusable lock owner |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned packet, return, and peer-fixture paths | `Test-Path` returned `False` before authoring for all four planned paths | CLEAR |
| packet identity | `rg -n "ACEL-AKOE-P2-R1|Durable Run Store Concurrency Correction" docs CVF_SESSION AGENT_HANDOFF_V63_2026-09-18.md` returned no match before authoring | CLEAR |
| owner collision | current run-store and reusable persistence owners exist; no new owner is required | REUSE_EXISTING_OWNERS |

## Required Correction Evidence

The worker return must prove:

- the original defective assertion fails after production repair and is
  replaced by a durable-winner/fail-closed assertion;
- a same-run real second process reaches READY and ATTEMPTING while the parent
  holds the real lock, cannot ENTER before PARENT_RELEASE, then ENTERS and
  COMPLETES after release;
- exactly one conflicting terminal attempt succeeds and durable replay contains
  exactly that winner with no fabricated success;
- post-acquire rejection/failure releases ownership so a subsequent peer
  acquires and performs a valid append;
- a stale lock fails closed without takeover or mutation;
- different run identities do not share a lock;
- focused tests and package typecheck/full suite pass.

## Acceptance Criteria

- all eight invariants have deterministic evidence;
- production code reuses the existing lock primitive and changes no sibling
  lock semantics;
- the final defect regression asserts desired behavior, not the known bug;
- real second-process and post-acquire cleanup proofs pass without using a
  timeout as positive evidence;
- exact manifest, no-staging, no-commit, worker gate, and final return-byte hash
  binding pass;
- return-time closeability is `CLOSEABLE` with no outside-authority blocker.

## Evidence / Verification

Dispatch evidence is the exact paired-packet diff from `fee4316f1`, source
hashes and symbol locators, collision search, high-risk contract admission,
author-fast gate, and full material pre-commit gate. Worker evidence is the
failing-before/passing-after desired oracle, real peer barrier transcript,
post-acquire cleanup and stale-lock tests, focused and full package results,
exact pending set, worker full gate, and detached final-return hash receipt.
This section defines required evidence and does not claim it already exists.

## Stop Conditions

Return `BLOCKED_WITH_REASON` for missing dispatch release, source/hash drift,
need to edit a forbidden path, need for a new dependency or runtime owner,
inability to prove real peer exclusion, automatic stale-lock takeover need,
or any external/provider/live/public requirement. Do not report completion
while a named blocker remains.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | paired packet and exact run-store paths | bounded local source/test correction; no commit or final acceptance | deterministic process tests and local gates | existing file-store API only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter | no ingress, mutation, provider, or public authority | zero external invocation ceiling | N/A with reason: no adapter is used or created | N/A_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Worker execution (WORKER_MUST_NOT_COMMIT)`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: 12 of 16 candidates shown by bounded resolver output.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Worker execution (WORKER_MUST_NOT_COMMIT)" --role worker --lifecycle-phase pre-implementation --max-results 12 --json` |
| Returned defect count | 16 candidates; output truncated to 12 |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0020, ADIF-0021, ADIF-0047, ADIF-0048, ADIF-0050, ADIF-0051, ADIF-0055, ADIF-0056, ADIF-0057 |
| Disclosed defectIds | same twelve returned IDs; ADIF-0059 is separately controlling direct evidence |
| Dispatch impact | exact manifest, source fidelity, checker read-ahead, honest execution base, semantic convergence, closeability, and no-commit separation are mandatory |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status; work-order convergence fields; high-risk nine-key JSON; closeability graph/recheck; full worker-return shape; final hash binding; no-commit evidence |
| gateRunPurpose | confirm the completed packet after source inspection; not discover runtime design or accept the future repair |
| claimBoundary | dispatch admission only; no repair correctness, P2 closure, or runtime readiness claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-AKOE-P2-R1 --title "ACEL AKOE-P2-R1 Durable Run Store Concurrency Correction" --date 2026-09-25 --base fee4316f1affdcf2675c4e9832d96ebc7b917402 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id run_store_concurrent_write_lost_race --prior-finding-set-digest a44fe1cf35db9b4b65a5b4439432665a80fa814a50b204ef82f96214bc6762d1 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence run_store_concurrent_write_lost_race --scec-problem-key acel-akoe-p2-durable-intent-projection --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md --scec-predecessor-sha256 a44fe1cf35db9b4b65a5b4439432665a80fa814a50b204ef82f96214bc6762d1 --scec-required-disposition READY_WITH_EXECUTABLE_PROOF --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | generic worker rework dispatch with no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact P2 blocker, source hashes, invariants, transaction proof, scope, and evidence contract |
| checkerReadAheadConfirmation | named dispatch, high-risk, closeability, convergence, review-probe, trace, and export checkers inspected |
| docOnlyNewFields | Required Correction Evidence only |
| claimBoundary | scaffold provenance only; no implementation or closure claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private-provenance correction packet; no public-sync authority or
public artifact evidence exists.

## Claim Boundary

This baseline authorizes only the exact P2-R1 durable-run-store concurrency
correction and its deterministic local evidence. It does not accept the future
worker result, close P2, open P3/P4, create a runtime owner, change external
behavior, or authorize provider/live/public/deployment/production action.
