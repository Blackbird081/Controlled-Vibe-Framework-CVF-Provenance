# CVF GC-018 Baseline - GC010 SCR R2 T1G Pending Agent Execution Canonical Approval Hash Fail-Closed Reissue Non-Production Implementation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION

Dispatch base head: 6801859bd

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator continuation on 2026-08-31

Reviewer owner: orchestrator/reviewer

Worker target: one internal delegated implementation worker

## Purpose

Implement the T1F-selected canonical approval-request hashing contract and its
fail-closed legacy reissue proof inside the exact four-file source/test
manifest. Remove the T1E JSON stringify/parse mask, prove durable lifecycle
versions 0/1/2/3 after SQLite reopen, and leave all package, route-source,
provider, audit, distributed and production integration parked.

## Authority Chain

- T1E blocked closure: `d367ea1c7`.
- T1F decision dispatch: `648063886`.
- T1F accepted material: `52a84fecf`; terminal
  `CANONICAL_APPROVAL_REQUEST_HASH_FAIL_CLOSED_REISSUE_READY_FOR_BOUNDED_IMPLEMENTATION`.
- T1F closure continuity: `6801859bd`.
- Operator continuation on 2026-08-31 authorizes this separate T1G dispatch only.

## Exact Implementation Manifest

The worker changed set is exactly five paths: four implementation/test paths
plus one worker return.

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.test.ts`
5. `docs/reviews/CVF_GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION_WORKER_RETURN_2026-08-31.md`

## Required Contract

- `approval-binding.ts` remains the sole approval-request identity/hash owner.
- Builder output is an exact recognized schema projection.
- Root keys and nested `inputs` keys use ordinal ordering; locale-sensitive
  comparison is forbidden.
- Normalized optional `undefined` properties are omitted by the builder.
- The hash boundary rejects unknown own keys, own `undefined`, unsupported
  values and malformed shapes; explicit schema-defined `null` is preserved.
- The preimage is UTF-8 compact `JSON.stringify` of the already ordered exact
  projection; SHA-256 remains the digest.
- Legacy or missing hashes are not accepted or rewritten. They retain route
  409/reissue behavior; old CREATED pending rows become stale on revalidation,
  and non-CREATED rows receive no new grant.
- Any requirement for dual-read, silent migration, bidirectional mixed-version
  availability or uninterrupted rollback stops T1G and reopens Family D.

## Required Focused Proof

- New approval-binding tests cover optional omission, explicit null,
  ordinal root/input ordering, equivalent-key-order hash equality, unknown or
  malformed own-shape rejection, and legacy old-order hash inequality.
- Execute-route tests cover current exact-match resume and manually seeded
  legacy same-semantics hash 409/reissue with zero provider invocation.
- Harness test removes the JSON stringify/parse mask and proves raw builder
  create/claim/begin/terminal versions 0/1/2/3, durable reopen, and legacy
  CREATED stale mismatch without grant or execution.
- Existing approval, pending-core and SQLite regressions plus TypeScript pass.

## Acceptance Criteria

- Exact five-path worker manifest; no other file changes.
- All selected hashing, legacy and reopen rules are observable in focused tests.
- T1E blocker is removed without weakening T1A/T1C fail-closed behavior.
- No route source, approval store, pending core, SQLite store, package/barrel,
  script, workflow, provider, audit or production source is changed.
- External/provider/network/browser/credential/live calls are zero.
- Worker stops uncommitted at `COMPLETE_PENDING_REVIEW` or returns
  `BLOCKED_WITH_REASON` for a source/scope contradiction.

## Decision / Baseline / Proposed Tranche

Decision: dispatch one bounded internal T1G implementation worker under the
T1F-selected Family A contract. Baseline: current source at `6801859bd` with
T1E blocked and T1F closed pass. Proposed tranche: exact four implementation/
test paths plus one worker return; no successor is self-opened.

## Evidence / Verification

Required evidence is a clean captured execution base, pre-implementation pass,
exact five-path diff, focused approval/route/harness plus unchanged regression
tests, TypeScript, worker-return fast/quality gates, zero external calls and a
no-commit return for independent review.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION --title "GC010 SCR R2 T1G Pending Agent Execution Canonical Approval Hash Fail-Closed Reissue Non-Production Implementation" --date 2026-08-31 --base 6801859bd --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with the T1F-selected owner, exact five-path worker manifest, fail-closed contract, proof matrix and boundaries. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| docOnlyNewFields | No new machine contract fields; descriptive hashing and legacy proof rows only. |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |


## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| T1F accepted decision material `52a84fecf` | Completion review selects exact owner, contract, legacy policy and four-file future manifest | Preserve exact contract and stop on any dual-read/migration requirement | ACCEPT |

Author reminder: do not move this packet to DISPATCH_READY/DISPATCHED until every dependency row carries source-backed evidence.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`bounded implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "bounded implementation" --role worker --lifecycle-phase pre-implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE |
| Dispatch impact | No ADIF-specific amendment; canonical work-order and no-commit controls remain mandatory. |

Author reminder: run the resolver command above for real before dispatch; list every defectId it actually returns.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch status; full repo-root Source Verification paths; Agent Operation Trace labels; exact worker-return profile; claim/evidence boundary rows; public disposition token |
| gateRunPurpose | Confirm known literal contract before the pre-dispatch evidence run. |
| claimBoundary | Read-ahead covers packet shape only; it is not implementation or runtime evidence. |

Author reminder: read every applicable checker source before writing the first governed line, then fill this block as confirmation evidence.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Selected owner and canonical preimage | source contract | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts` | `buildApprovalRequestSnapshot` and `computeApprovalRequestHash`, lines 71-98 | builder and hash | approval-binding | ACCEPT |
| Selected implementation and legacy contract | accepted decision | `docs/reviews/CVF_GC010_SCR_R2_T1F_PENDING_AGENT_EXECUTION_APPROVAL_SNAPSHOT_DURABLE_COMPATIBILITY_CORRECTION_DECISION_COMPLETION_2026-08-31.md` | Findings / Position; Risk / Corrective Action | exact schema projection, legacy reissue, exact future manifest | T1F reviewer closure | ACCEPT |
| Durable mismatch/stale evidence | test/source evidence | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.test.ts` | raw builder blocker test, lines 266-286 | hash mismatch and STALE transition | T1E harness proof | ACCEPT |

Author reminder: every claimed item needs a real source file and line/section; do not leave placeholder rows in the dispatched artifact.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for worker-owned new test and return | `Test-Path` returned `False` for both before dispatch | ABSENT_CONFIRMED |
| Token search for T1G before packet authoring | `rg -n "GC010-SCR-R2-T1G|CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION" docs CVF_SESSION -g '*.md' -g '*.json'`; only continuity next-move authority existed before these packet paths | EXPECTED_AUTHORITY_ONLY |
| Collision decision | Packet paths and new test do not collide; three existing test/source paths are intentional owner edits. | PROCEED_BOUNDED |

Author reminder: run the searches for real before dispatch; do not leave placeholder rows.

## Claim Boundary

This baseline authorizes only the exact four-file non-production source/test
implementation plus one worker return. It does not accept T1E before
independent review, export a package surface, alter route source/store/pending
core/SQLite source, invoke a provider, or authorize distributed, public,
deployment or production behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch and non-production implementation only;
no public artifact or export authority is in scope.
