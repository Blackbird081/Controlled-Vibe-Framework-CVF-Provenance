# CVF GC-018 - T5 Runtime Memory Wiring

Memory class: SUMMARY_RECORD

Status: ACCEPTED

Date: 2026-05-22

Parent Commit: a9c63837

Roadmap: docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md

Work Order: docs/work_orders/CVF_WO_T5_RUNTIME_MEMORY_WIRING_2026-05-22.md

## Purpose

Authorize the bounded T5 runtime memory wiring tranche after T4 closure,
limited to an ephemeral in-process task-memory store and an audit-memory readout
extension.

## Scope / Target / Owner Boundary

In scope:

- `governance/toolkit/05_OPERATION/CVF_MEMORY_TIER_RETENTION_POLICY.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/task-memory/`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
- focused task-memory and audit-memory tests
- T5 completion review and active-session metadata updates

Out of scope:

- durable persistence, file-backed storage, database storage, external memory
  services, provider memory, archive tiers, retrieval flow, reinjection flow,
  route changes, receipt envelope changes, provider changes, public-sync,
  Maika proof, hosted-readiness claim, and freeze release.

## Source / Predecessor Evidence

T4 pre-condition is closed at
`docs/reviews/CVF_T4_PROVIDER_METHOD_COVERAGE_COMPLETION_2026-05-22.md` with
status `CLOSED_T4_PROVIDER_METHOD_COVERAGE`.

Prior audit-memory readout hardening closed at
`docs/reviews/CVF_CDH_H_AUDIT_MEMORY_READOUT_COMPLETION_2026-05-21.md`.

Active registry authority:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

## Evidence Trace Block

Blocked-work class: `new_memory_tiers_beyond_lane_h_scope`.

Override status: GRANTED.

Operator confirmation source: active session state records T5 as the next
allowed move and states that the operator override is granted only for an
ephemeral in-memory task store, with no durable persistence, file write,
database, provider memory, or external store.

Current user continuation request: `Làm tiếp phần dang dở`.

## Decision / Baseline / Proposed Tranche

Decision: ACCEPT T5 implementation baseline with the bounded memory-tier
override granted.

Baseline:

- task memory is process-local only;
- entries are lost on process exit by design;
- expired entries return no live read result;
- non-task events are rejected deterministically;
- audit readout may surface `taskMemoryDecision` and `taskMemoryReason`;
- `GovernanceEvidenceReceipt` must remain unchanged;
- `canReinject` must remain false.

## Verification

Required verification:

- focused task-memory store tests;
- focused audit-memory receipt tests;
- `CVF_LEARNING_PLANE_FOUNDATION` TypeScript check;
- `cvf-web` TypeScript check;
- markdown structural completeness check;
- governed file-size check;
- local governance hook chain if no unrelated blockers appear.

## Claim Boundary

This baseline authorizes only ephemeral in-process task memory and audit readout
visibility. It does not authorize durable memory, file writes, database writes,
external memory, provider memory, archive tiers, reinjection, route behavior
expansion, receipt envelope changes, public-sync, Maika proof, hosted readiness,
or freeze release.
