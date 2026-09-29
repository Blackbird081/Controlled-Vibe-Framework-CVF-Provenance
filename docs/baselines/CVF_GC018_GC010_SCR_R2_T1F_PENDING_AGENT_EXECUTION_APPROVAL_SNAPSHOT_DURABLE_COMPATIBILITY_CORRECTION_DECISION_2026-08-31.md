# CVF GC-018 GC010 SCR-R2-T1F Pending Agent Execution Approval Snapshot Durable Compatibility Correction Decision

Memory class: governed-baseline

docType: baseline

Status: DISPATCHED_DECISION_BOUNDED

Batch ID: GC010-SCR-R2-T1F

Date: 2026-08-31

dispatchBaseHead: `061f92cf9`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one documentation-only cross-owner decision over the exact blocker
accepted by T1E: approval-request snapshot hashes are computed from
order-sensitive JSON bytes while the accepted durable store persists the
containing payload with canonical key ordering. This tranche selects one
bounded correction contract; it authorizes no source repair.

## Authority Chain

- The operator instructed continuation of the same GC010 system chain and
  authorized internal sub-agents under orchestrator/reviewer control.
- Accepted T1E blocked material: `d367ea1c7`.
- T1E terminal:
  `APPROVAL_SNAPSHOT_HASH_PERSISTENCE_COMPATIBILITY_BLOCKED`.
- T1E completion:
  `docs/reviews/CVF_GC010_SCR_R2_T1E_PENDING_AGENT_EXECUTION_LOCAL_HARNESS_NON_PRODUCTION_IMPLEMENTATION_COMPLETION_2026-08-31.md`.
- Paired work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1F_PENDING_AGENT_EXECUTION_APPROVAL_SNAPSHOT_DURABLE_COMPATIBILITY_CORRECTION_DECISION_2026-08-31.md`.

Historical GC010-SCR-R1 production-consumer work remains parked and supplies
no authority for this decision.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| T1E blocker | independently reproduced and closed at `d367ea1c7` | decide only the named cross-owner contradiction | ACCEPT |
| Approval snapshot/hash owner | current source in `approval-binding.ts` | inspect read-only; identify correction owner | ACCEPT_READ_ONLY |
| T1A pending core | accepted lifecycle source | inspect read-only; preserve fail-closed semantics | ACCEPT_READ_ONLY |
| T1C SQLite store | accepted JCS persistence source | inspect read-only; compare, do not modify | ACCEPT_READ_ONLY |
| Route/provider/audit/production | parked by T1E closure | no implementation or invocation | ACCEPT_PARKED |

## Scope / Target / Owner Boundary

The worker may write exactly one assessment and one worker return. The target
is the contract boundary among approval snapshot construction, approval hash
preimage, durable payload serialization and pending claim validation. All
source, tests, packages, routes, providers, audit, configuration, continuity,
public and production surfaces remain read-only.

## Source Verification Block

| Source | Required verification | Disposition |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts` | builder shape and hash preimage | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | approval record/version compatibility context | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/route.ts` | direct approval issuance caller | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | existing fail-closed hash comparison | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | claim drift/hash behavior | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` | canonical persistence bytes | ACCEPT_READ_ONLY |
| Current approval/store/execute/T1A/T1C/T1E focused tests | present compatibility and blocker regressions | ACCEPT_READ_ONLY |
| T1E blocked return and completion | exact observed receipt and reviewer finding | ACCEPT_READ_ONLY |

Provider memory and historical prose are not canonical source evidence.

## Candidate Families Required

The assessment must compare all four families against ownership, semantic
stability, fail-closed safety, backward compatibility, migration burden,
proof cost and manifest width:

1. Canonicalize the approval-request snapshot/hash boundary and fail closed
   on legacy unversioned hashes, requiring reissue.
2. Preserve insertion-order bytes in the SQLite persistence boundary.
3. Add semantic snapshot equivalence inside pending execution claim logic.
4. Introduce a versioned hash/preimage contract with an explicit migration or
   dual-read policy.

Every family must be scored with the same axes and source burden. No family may
be selected merely because it makes the T1E positive test pass.

## Required Decision Contract

The selected result must freeze:

- the canonical owner of snapshot normalization and hash preimage bytes;
- whether optional `undefined` fields are emitted, omitted or rejected;
- deterministic key and input-key ordering rules;
- separate treatment of missing pre-binding hashes, present order-sensitive
  hashes in memory, the same approval after file reload, and old pending SQLite
  version-1 rows, with no silent rewrite;
- whether dual acceptance is forbidden, required or explicitly deferred;
- exact future implementation and regression manifest;
- route-visible fail-closed/reissue behavior;
- direct raw-builder lifecycle proof through durable versions `0/1/2/3`
  without a JSON stringify/parse masking round trip;
- bidirectional deploy/rollback behavior for records issued under either hash
  contract, plus a stop-to-versioned-migration rule when safe rollback cannot
  be bounded.

The worker must derive the smallest exact future manifest for the selected
family from current ownership evidence. No candidate receives a preselected
manifest in this dispatch.

## Allowed Terminal Tokens

Exactly one terminal token is required:

- `CANONICAL_APPROVAL_REQUEST_HASH_FAIL_CLOSED_REISSUE_READY_FOR_BOUNDED_IMPLEMENTATION`
- `PRESERVE_SQLITE_SNAPSHOT_BYTE_ORDER_READY_FOR_BOUNDED_IMPLEMENTATION`
- `PENDING_CORE_SEMANTIC_SNAPSHOT_EQUIVALENCE_READY_FOR_BOUNDED_IMPLEMENTATION`
- `VERSIONED_HASH_PREIMAGE_MIGRATION_REQUIRED_BEFORE_IMPLEMENTATION`
- `BLOCKED_OWNER_OR_COMPATIBILITY_NOT_RESOLVED`

## Acceptance Criteria

- Exactly two worker-authored documentation outputs and zero source edits.
- Fresh source verification and negative collision search are recorded.
- All four candidate families receive explicit dispositions and evidence.
- One owner, compatibility contract and terminal token are unambiguous.
- A selected bounded implementation manifest contains no speculative files.
- Legacy behavior is explicit; silence is not compatibility evidence.
- T1E remains blocked until a later authorized repair and full rerun pass.
- Zero provider, browser, network, credential, package, route or production
  actions occur.

## Decision / Baseline / Proposed Tranche

T1F is a decision prerequisite only. A successful worker return remains
pending independent review and does not open implementation automatically.

successorTrancheOpened: NO

## Evidence / Verification

Required evidence includes initial/final HEAD and status, exact two-path
manifest, source symbol receipts, four-family matrix, compatibility decision,
governance gates, zero external invocations and no commit.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010-SCR-R2-T1F --title "Pending Agent Execution Approval Snapshot Durable Compatibility Correction Decision" --date 2026-08-31 --base 061f92cf9 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T1E blocked closure d367ea1c7; approval snapshot hash versus canonical persistence contradiction" --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --include-worker-return-skeleton --stdout` |
| generatedProfile | generic internal-worker documentation decision dispatch plus no-commit return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | four-family comparison, compatibility decision, exact two-output manifest, candidate implementation freeze and T1E reopen proof |
| checkerReadAheadConfirmation | dispatch, lifecycle, read-ahead, review-cost, worker-return, trace, delta, public, handoff, external-intake and storage checkers read |
| implementationFields | N/A with reason: decision-only tranche authorizes no source mutation |
| docOnlyNewFields | candidateFamilies; legacyCompatibilityContract; futureImplementationManifest |
| claimBoundary | authoring provenance only; no compatibility repair exists from this baseline |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | normal bounded documentation decision controls remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | dispatch envelope, source dispositions, decision-only route, no-commit return, trace/delta labels, handoff rows, public/external/storage boundaries |
| gateRunPurpose | confirmation/evidence after source and checker inspection; not first discovery |
| claimBoundary | artifact conformance only; worker/reviewer own decision correctness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private cross-owner correction decision; no public artifact or runtime
repair is authorized.

## Claim Boundary

This baseline authorizes exactly one documentation decision and worker return.
It does not change approval hashing, persistence or pending execution source;
accept the harness; issue or migrate approvals; register a route; call a
provider; synchronize public artifacts; deploy; open production; or authorize
an automatic successor.
