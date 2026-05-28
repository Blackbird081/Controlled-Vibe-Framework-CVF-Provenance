# CVF GC-019 T5 Task Memory Directory Structural Review

Memory class: FULL_RECORD

Status: APPROVE_BOUNDED_COORDINATION_PACKAGE

Date: 2026-05-22

## Purpose

Classify the T5 addition of `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/task-memory/`
under the structural change audit guard and confirm it does not create a new
extension, move ownership, or widen memory persistence.

## Scope / Target / Owner Boundary

Target change:

- new Learning Plane Foundation subdirectory:
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/task-memory/`
- no new extension root;
- no route file;
- no provider adapter;
- no durable memory store;
- no ownership transfer between logical planes.

Owner remains `CVF_LEARNING_PLANE_FOUNDATION`.

## Target / Source Under Review

Source authority:

- `docs/work_orders/CVF_WO_T5_RUNTIME_MEMORY_WIRING_2026-05-22.md`
- `docs/baselines/CVF_GC018_T5_RUNTIME_MEMORY_WIRING_2026-05-22.md`
- `governance/toolkit/05_OPERATION/CVF_MEMORY_TIER_RETENTION_POLICY.md`

## Scope / Methodology

The review classifies the filesystem addition against GC-019 structural-change
classes. The change is a bounded coordination package inside an existing
extension: it groups task-memory types, store implementation, index re-export,
and focused tests without moving existing modules.

## Findings / Position

Position: APPROVE.

Findings:

- The addition is not a physical merge.
- The addition is not a replacement package.
- The addition does not change public extension lineage.
- The addition preserves rollback: the new subdirectory can be removed without
  relocating existing Learning Plane source files.
- The addition is necessary for T5 because the work order names a task-memory
  store as an implementation deliverable.

## Risk / Defect / Corrective Action

Risk: a task-memory directory could be misread as durable memory infrastructure.

Corrective action: the retention policy and GC-018 baseline bind the directory
to ephemeral in-process storage only. Any durable store requires a future
GC-018 and a fresh blocked-work override.

## Decision / Recommendation / Disposition

Decision: approve the T5 task-memory subdirectory as a bounded coordination
package within the existing Learning Plane Foundation extension.

Recommendation: do not create a new extension root or move existing memory
contracts for T5.

## Verification

Verification should confirm:

- no new `EXTENSIONS/` root is created;
- no existing module is moved;
- task-memory code remains in-process only;
- rollback remains limited to the new subdirectory and audit readout fields.

## Claim Boundary

This review approves only the T5 subdirectory addition. It does not approve
durable memory, database storage, external memory services, provider memory,
archive tiers, reinjection, public-sync, or hosted-readiness claims.
