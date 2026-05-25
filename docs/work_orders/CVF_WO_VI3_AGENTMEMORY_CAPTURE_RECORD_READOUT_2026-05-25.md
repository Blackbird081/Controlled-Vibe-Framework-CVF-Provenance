# CVF Work Order VI3 Agentmemory Capture Record Readout

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-25

---

## Purpose

Implement the bounded VI3 agentmemory capture-record readout authorized by
`docs/baselines/CVF_GC018_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_2026-05-25.md`.

## Scope / Target / Owner Boundary

Allowed owner files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/vertical-integration-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi1-vertical-chain.alibaba.live.test.ts`
- VI3 completion/session/handoff files

Forbidden:

- editing `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`;
- direct memory search/write outside the existing governed audit capture;
- memory reinjection, raw memory release, automatic promotion, external memory
  adapters, MCP/tool/database/browser automation, provider routing changes,
  new receipt envelope schema, public-sync, hosted readiness, production
  readiness, or freeze release.

## Agent Roles

- Implementer: add capture record fields inside existing audit memory receipt.
- Auditor: verify `/api/execute/route.ts` remains untouched and no new runtime
  authority opens.
- Product/operator advocate: make memory observation understandable to API
  consumers.
- Safety/boundary owner: preserve capture-as-observation, not permission.

## Authority Chain

- VI1 closed route vertical readout and memory hook posture.
- VI2 closed request-context/profile diagnostics.
- Agentmemory legacy sources remain valuable only as bounded evidence readout,
  not as runtime memory import or reinjection.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reviews/CVF_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_COMPLETION_2026-05-25.md`
- `docs/baselines/CVF_GC018_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_2026-05-25.md`
- `.private_reference/legacy/CVF 16.5/agentmemory/CVF_MEMORY_EVENT_HOOKS.md`
- `.private_reference/legacy/CVF 16.5/agentmemory/CVF_MEMORY_CAPTURE_ADAPTER.md`

## Pre-Flight Checks

- confirm worktree is clean after VI2 closure;
- confirm route file remains at 999 lines and is not edited;
- confirm no memory reinjection, external adapter, or promotion behavior is
  introduced;
- confirm live key loading remains secret-safe.

## Write Ownership

Writes are limited to the VI3 helper/test surfaces listed above, completion
review, and session continuity files.

## Execution Plan

1. Add capture-record type and builder inside `audit-memory-receipt.ts`.
2. Attach capture record to `AuditMemoryReceipt`.
3. Update VI memory surface summary/evidence to reference capture record.
4. Update unit/route/live tests.
5. Run focused tests, check, live proof, session guards.
6. File completion review, close work order, update session/handoff, commit.

## Acceptance Criteria

- successful route responses expose `auditMemoryReceipt.captureRecord`;
- capture record includes hook event, payload summary, policy context,
  privacy filters, disallowed behaviors, capture decision, next safe action,
  and boundaries;
- VI memory surface references the capture record;
- `/api/execute/route.ts` is unchanged;
- focused tests, TypeScript check, live proof, and session guards pass.

## Evidence Requirements

- focused audit-memory/VI/route tests PASS;
- cvf-web TypeScript check PASS;
- live VI route proof PASS with capture record present;
- active state guard PASS;
- handoff guard PASS.

## Review Gate

Before closure, verify the diff does not edit `/api/execute/route.ts`, add
memory retrieval/reinjection, add direct memory writes beyond existing governed
audit capture, change provider routing, change receipt envelopes, add external
adapters, or make hosted/production/freeze claims.

## Closure Checklist

- [x] capture record added
- [x] audit memory receipt exposes capture record
- [x] VI memory surface references capture record
- [x] route file unchanged
- [x] focused tests PASS
- [x] TypeScript check PASS
- [x] live proof PASS or diagnostic filed
- [x] completion review filed
- [x] active state/front door/handoff updated
- [x] active state guard PASS
- [x] handoff guard PASS
- [x] commit created

## Return-To-Orchestrator Conditions

Return blocked if implementation requires route edits, memory reinjection,
external memory adapters, provider routing changes, or a new receipt schema.

## Operator Checkpoint

No checkpoint is required unless live proof lacks a usable key, an unclear live
failure needs a rerun, or implementation requires scope expansion beyond the
VI3 owner files.

## Claim Boundary

VI3 closes only response-level agentmemory capture-record readout. It does not
close memory retrieval, memory reinjection, automatic promotion, external memory
adapters, hosted readiness, production readiness, or freeze release.
