# CVF GC-018 Baseline - EAFR-R2 Durable Memory HTTP Write Authority Fail Closed

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EAFR-R2-DURABLE-WRITE

Dispatch base head: `8036abf5609e3e87d6de98153cbad3c724f97475`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the explicit EAFR roadmap authority and R1 waiver

Reviewer owner: current independent orchestrator/reviewer

Worker target: implementation worker role

## Purpose

Close the reachable durable-memory HTTP write defect by requiring complete
provenance, binding actor identity and role to authenticated server evidence,
and proving every rejected request causes no storage mutation.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R2 --title "Durable Memory HTTP Write Authority Fail Closed" --date 2026-08-25 --base ee268fa5b --commit-mode WORKER_MUST_NOT_COMMIT --dependency "EAFR-R1 bounded operator-waiver closure at ee268fa5b" --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-verified R2 scope, exact manifest, acceptance and rollback boundaries |
| checkerReadAheadConfirmation | dispatch, packet-authority, trace, claim-boundary and worker-return checker sources |
| docOnlyNewFields | none |
| claimBoundary | authoring provenance only; no runtime behavior claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| EAFR-R1 bounded closure | material commit `ee268fa5b` records the explicit operator waiver and named R1C debt | R1 must close without relaxing R2 | RELEASED |
| EAFR-R1A | accepted at `ef142bfb2` | non-live runner boundary must be closed | RELEASED |
| EAFR-R1B | fail-closed adjudication accepted at `fc10c8e65` | authority question must be decided | RELEASED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime implementation`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "runtime implementation" --role worker --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | no additional ADIF-specific control; all ordinary CVF controls remain mandatory |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Source Verification Block; Current Runtime Freshness Verification; exact manifest; commit mode; Public Export Disposition |
| gateRunPurpose | confirm as evidence that the already source-verified dispatch matches checker shape |
| claimBoundary | structural compliance is not implementation proof |

## Current Runtime Freshness Verification

Verified against HEAD `ee268fa5b` on 2026-08-25:

- the HTTP route accepts optional `provenanceScore` and passes omission through;
- the durable store substitutes omitted provenance with `1`;
- request-body actor and policy fields can currently self-assert write authority;
- server-owned session and signed-token identity helpers already exist and can
  be reused without modifying their owner files.

This is source freshness only; route deployment or external exposure is not claimed.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| provenance is optional and forwarded | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.ts` | request type, validation and store call | `provenanceScore?`; `validateBody`; `store.write` | memory write route | ACCEPT |
| omission becomes maximum trust | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | write admission | `input.provenanceScore ?? 1` | durable store | ACCEPT |
| caller supplies actor and policy claims | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.ts` | validation and policy gate | `actorId`; `actorRole`; `actorAuthorized`; `policyDecision` | memory write route | ACCEPT |
| authenticated role resolver exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts` | role mapping | `resolveExecutionCVFRole` | server-owned role resolver | ACCEPT |
| stable signed-token identity exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | identity helper | `deriveServiceTokenIdentity` | service-token authentication | ACCEPT |
| route tests lack omission and identity-mismatch probes | TEST_GAP | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.test.ts` | existing six cases | `/api/memory/write` suite | route test owner | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact R2 packet paths | absent before authoring | PASS |
| current EAFR-R2 token search | only roadmap/session planning references existed | PASS |
| collision decision | extend the existing route, test, authentication identity and role owners; create no duplicate runtime authority owner | PASS |

## Required Invariants

1. Missing, undefined-equivalent, non-finite, negative, or above-one provenance
   cannot reach `store.write` and cannot mutate the store.
2. Empty required strings and malformed optional security fields fail closed.
3. Session writes bind actor identity to `session.userId` and actor role to the
   server-owned role resolver; caller mismatch is rejected.
4. Signed service-token writes bind actor identity to the stable derived token
   identity and role `SERVICE_AGENT`; caller mismatch is rejected.
5. Caller `actorAuthorized` or `policyDecision` fields cannot independently
   grant authority. Store inputs are derived only after authentication and role
   binding succeeds.
6. Existing valid summary-only writes remain possible for a bound, authorized
   actor and preserve raw-content rejection and receipt invariants.

rawMemoryReleased=false

## Baseline Decision / Proposed Tranche

Dispatch one exact three-path no-commit implementation tranche. Any owner-file
expansion returns blocked to the orchestrator.

## Verification Evidence

Pinned source hashes, focused adversarial tests, typecheck, safe non-live suite,
worker-return fast gate, independent reviewer proof, and exact manifest.

## Exact Worker Manifest

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.test.ts`
- `docs/reviews/CVF_EAFR_R2_DURABLE_MEMORY_HTTP_WRITE_AUTHORITY_FAIL_CLOSED_WORKER_RETURN_2026-08-25.md`

## Risk / Rollback

Risk is R2 because an authenticated durable write boundary changes. Rollback is
the exact three-path worker diff. Any need to edit auth helpers, role resolver,
durable store, package scripts, other tests, documentation, registries, session
state, or environment configuration returns `BLOCKED_WITH_REASON`.

## Claim Boundary

This baseline authorizes only the exact three-path hermetic R2 repair. It does
not authorize live/provider/network calls, credential or environment-file
access, deployment, public sync, push, production claims, or R3 work.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance remediation; no public-sync authority.
