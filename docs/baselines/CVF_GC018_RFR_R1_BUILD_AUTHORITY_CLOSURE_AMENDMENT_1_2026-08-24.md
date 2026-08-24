# CVF GC-018 Baseline - RFR-R1 Build Authority Closure Amendment 1

Memory class: governed-dispatch-baseline

Status: APPROVED_FOR_EXECUTION

Date: 2026-08-24

Batch ID: RFR-R1-AMENDMENT-1

Parent dispatch HEAD: `9df990f8b56d6fbc0e314aa3a84959104586f7de`

Commit mode: REVIEWER_CLOSER_OWNS_COMMIT

## Purpose

Resolve the source-backed manifest contradiction in the RFR-R1 worker return
without weakening the mandatory shared-factory BUILD authority invariant.

## Scope / Target / Owner Boundary

The current orchestrator/reviewer may repair the original five-path pending
implementation and exactly five dependent paths:

1. `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts`
2. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts`
3. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.test.ts`
4. `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`
5. `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_WORKER_RETURN_2026-08-24.md`

The completion review and R1 roadmap transition remain reviewer-owned closure
paths. Session continuity remains a separate post-material-commit batch.

## Amendment Decision

`PROCEED_WITH_EXACT_SCOPE_EXPANSION`.

The shared factory must remain mandatory. An opt-in compatibility flag,
conditional registration, silent evidence synthesis, or assertion weakening is
forbidden. Existing BUILD execution fixtures must either carry explicit valid
authority and bounded targets or assert the new fail-closed result.

## Decision / Baseline / Proposed Tranche

Decision: `PROCEED_WITH_EXACT_SCOPE_EXPANSION`.

Baseline: the parent RFR-R1 implementation is locally valid in isolation but
cannot close while runtime propagation, dependent tests, evidence shape, and
the reviewed system-chain fingerprint remain unresolved.

Proposed tranche: one consolidated Amendment 1 reviewer repair followed by one
material commit and, only after acceptance, one separate continuity commit.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| exact factory assertions require eight guards | TEST_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts` | lines 39-63 | `createGuardEngine` tests | Guard Contract tests | ACCEPT |
| runtime config cannot carry BUILD authority evidence | INTERFACE_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | `RuntimeConfig`, lines 89-111 | `RuntimeConfig` | Agent Execution Runtime | ACCEPT |
| runtime pre-check omits BUILD authority evidence | COMPOSITION_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | `preCheck`, lines 192-207 | `GuardRequestContext` construction | Agent Execution Runtime | ACCEPT |
| runtime BUILD fixtures omit evidence and bounded targets | TEST_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.test.ts` | helper and BUILD suites, lines 29-46 and 111-338 | `defaultConfig`; `createRuntime` | Agent Execution Runtime tests | ACCEPT |
| system-chain map fingerprints the changed factory | FRESHNESS_DEPENDENCY | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | `CONTRACT_TO_RUNTIME`, lines 59-116 | `sourceFingerprints` | system-chain map | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_worker_experience_retrospective.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_system_chain_map_freshness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | exact source paths; current symbol lines; retrospective enums; `git diff --name-status`; system-chain semantic review requirement |
| gateRunPurpose | confirm the exact amendment evidence before dependent repairs; not first discovery |
| claimBoundary | dispatch authority only; no implementation or closure claim |

## Required Semantic Repair

- malformed runtime evidence must return `BLOCK`, never throw;
- accepted SPEC and WORK ORDER references must be non-empty after trimming;
- the runtime must carry typed BUILD authority evidence into guard context;
- positive BUILD fixtures must declare both valid evidence and bounded targets;
- exact factory count/ID assertions must include `build_authority`;
- the `CONTRACT_TO_RUNTIME` lane must be semantically re-read before its source
  fingerprint is refreshed; its broader posture must not be auto-promoted.

## Verification Contract

Run focused guard and runtime tests, full package tests, TypeScript no-emit,
worker-return fast gate, reviewer-fast, system-chain freshness, governed file
size, diff checks, and material pre-commit. No provider/live proof applies.

## Acceptance Criteria

1. Mandatory shared composition remains unconditional.
2. Malformed values fail closed without exceptions.
3. Runtime propagation is explicit and typed.
4. Full package and TypeScript checks pass.
5. Worker-return and system-chain gates pass.
6. No R2-R6, provider/live, public, deployment, or push authority opens.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason: no `governance/compat/`
checker or `AGENTS.md` source is changed.

Protected paths: N/A with reason: the system-chain map is a reviewer-owned
reference freshness surface, not a governance checker source.

Operator authorization: operator message `next` on 2026-08-24 after the
reviewer proposed RFR-R1 Amendment 1.

Rollback boundary: revert this amendment and its exact RFR-R1 repair batch as
one bounded tranche; continuity remains separately reversible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 50 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no added control beyond the amendment contract |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair; public sync remains unauthorized.

## Claim Boundary

This baseline authorizes exact local repairs only. It does not accept the
worker return, close R1, release R2-R6, or authorize runtime/provider/live,
deployment, public sync, push, or production.
