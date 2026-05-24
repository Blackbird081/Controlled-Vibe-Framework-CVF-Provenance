# CVF Work Order: R2 - Execute Route Durable Memory Wiring

Memory class: FULL_RECORD

Status: DEMAND_GATED

docType: work_order

Date: 2026-05-24

Tranche: R2

Roadmap: `docs/roadmaps/CVF_R1_R2_P2_POST_M1_GAP_CLOSURE_ROADMAP_2026-05-24.md`

---

## STOP - Demand Gate

Do not implement R2 until a fresh GC-018 explicitly authorizes changes to
`/api/execute` durable-memory behavior.

This route is the governed AI execution path. Any claim that memory affects
execution must be proven with a real provider API call under the mandatory live
governance proof rule.

---

## Purpose

Close the gap between M1's durable-memory store and real user value in the web
execution path. A non-coder using the web UI should benefit from bounded
cross-session memory only through explicit policy gates and receipt evidence.

---

## Authority Chain

- Required future GC-018 baseline: not yet issued.
- Roadmap: `docs/roadmaps/CVF_R1_R2_P2_POST_M1_GAP_CLOSURE_ROADMAP_2026-05-24.md`
- M1 completion review:
  `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
- Mandatory live governance proof rule in root `AGENTS.md`.

---

## Scope / Target / Owner Boundary

Target:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Existing AIF C2 memory reinjection route helpers.
- A route-local durable-memory adapter or bridge, if needed.
- Route unit tests and one live proof spec/script.

Owner: CVF web governed execution route.

Boundary:

- No raw memory in provider prompt.
- No `canReinject=true`.
- No autonomous write.
- No tier beyond `skill` and `long-term`.
- No hosted/cloud persistence claim.

---

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Draft GC-018 and define route memory policy. |
| Implementer | Wire durable read path without raw-memory prompt release. |
| QA | Add route unit tests and live proof coverage. |
| Governance Reviewer | Verify receipt evidence and `canReinject=false` invariants. |
| Release Manager | Run release gate, file completion review, and commit. |

---

## Required First Reads

- `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`

---

## Write Ownership

Allowed after GC-018 only:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Route-local durable memory adapter/helper files, if needed.
- Route tests under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/`.
- Completion review and roadmap status updates.

---

## Pre-Flight Checks

- Fresh GC-018 exists and authorizes `/api/execute` durable-memory changes.
- Live provider key is available through approved environment variables.
- R1 resilience fix is present.
- `canReinject=false` invariant remains unchanged.

---

## Required Design Questions

- Which actor and scope decide whether a durable read is allowed?
- Which request field or server-side policy selects durable memory retrieval?
- How is the durable-memory receipt embedded in `governanceEvidenceReceipt`
  without leaking raw memory?
- How does the route degrade if the durable store file is unavailable or
  corrupt?
- What exact claim is supported by the live proof?

---

## Execution Plan

1. File and approve fresh GC-018 for route behavior.
2. Define durable-memory request/actor/scope policy.
3. Add route adapter that reads only policy-authorized summaries.
4. Embed durable-memory receipt evidence in `governanceEvidenceReceipt`.
5. Add corrupt-store and denied-policy route tests.
6. Run targeted route tests and live provider proof.
7. Run release gate.
8. File completion review and update roadmap.

---

## Evidence Requirements

- Route unit tests showing durable-memory retrieval is gated, receipt-bearing,
  and summary-only.
- Unit or integration test showing corrupt durable store does not break
  `/api/execute`.
- Live provider proof through `/api/execute`.
- Release gate PASS if governance behavior is claimed.
- Completion review filed.

---

## Acceptance Criteria

- [ ] Fresh GC-018 baseline exists and authorizes R2.
- [ ] Route reads durable memory only when policy allows it.
- [ ] Receipt evidence includes durable-memory read decision and memory ids.
- [ ] Provider prompt contains only authorized summary context.
- [ ] `canReinject=false` remains binding.
- [ ] Live proof PASS with approved provider key and no raw secret printed.
- [ ] Completion review filed and roadmap updated.

---

## Review Gate

The completion review must confirm GC-018 authority, policy-gated route read,
summary-only prompt context, receipt evidence, live proof, release gate, and no
raw secret or raw memory release.

---

## Operator Checkpoint

R2 is registered from the Claude audit but not authorized for implementation
in this fast-lane R1 commit.

---

## Closure Checklist

- [ ] GC-018 filed.
- [ ] Route durable-memory policy implemented.
- [ ] Route tests PASS.
- [ ] Live proof PASS.
- [ ] Release gate PASS.
- [ ] Completion review filed.

---

## Return-To-Orchestrator Conditions

Return blocked if GC-018 is absent, route tests fail, live proof cannot run, or
any implementation would require `canReinject=true` or raw-memory prompt
release.

---

## Claim Boundary

R2, once complete, may support a bounded claim that the governed web execution
route can use durable skill/long-term memory under policy gate and receipt
evidence. It must not claim broad memory authority, autonomous reinjection, or
production-grade hosted durable memory.
