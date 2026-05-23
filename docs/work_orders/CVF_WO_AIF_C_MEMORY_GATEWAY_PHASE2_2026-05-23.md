# CVF Work Order: AIF-C Memory Gateway Phase 2

Memory class: FULL_RECORD

Status: DEMAND_GATED_NOT_AUTHORIZED

docType: work_order

Date: 2026-05-23

Tranche: AIF-C

Roadmap: `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`

---

## Purpose

Implement Memory Gateway Phase 2 by absorbing the unimplemented portions of
the `agentmemory` spec set (CVF 16.5) into `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/`.

T5 delivered `canReinject=false` + 7-tier classifier + ephemeral task store.
This tranche delivers the next layer: lifecycle decay, semantic retrieval,
context packager, and privacy-filtered reinjection — all in-memory, no durable
persistence required for Phase 2a.

---

## STOP — This work order is DEMAND_GATED

**Do not begin implementation until ALL of the following are satisfied:**

1. Operator explicitly grants blocked-work override for
   `new_memory_tiers_beyond_lane_h_scope`
2. A fresh GC-018 is filed and accepted (use GC-018 template with Legacy Spec
   Scan Block)
3. Codex has read all 10 `agentmemory` spec files and filed the file-by-file
   absorption table (see below)
4. The GC-018 includes the explicit scope declaration for Phase 2a vs 2b

**When the operator authorizes this work order, update Status from
`DEMAND_GATED_NOT_AUTHORIZED` to `READY_FOR_IMPLEMENTATION` and file the
required GC-018.**

---

## Authority Chain

Operator → Claude (roadmap author) → Codex (implementer).

Authorization: DEMAND_GATED. This work order is not authorized for implementation
until the operator grants the required blocked-work overrides (see STOP section).
Parent roadmap: `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`.

---

## Agent Roles

- Operator: authorizer — must grant `new_memory_tiers_beyond_lane_h_scope` override
- Claude: GC-018 reviewer — confirms Legacy Spec Scan Block is complete
- Codex: implementer — reads all 10 agentmemory specs before implementing

---

## Required First Reads

Before filing GC-018 (mandatory):

- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- `docs/reviews/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `docs/reviews/CVF_T5_RUNTIME_MEMORY_WIRING_COMPLETION_2026-05-22.md`
- All 10 spec files under `.private_reference/legacy/CVF 16.5/agentmemory/`

---

## Pre-Flight Checks

Before any implementation:

1. Operator grants blocked-work override for `new_memory_tiers_beyond_lane_h_scope`
2. GC-018 filed and accepted with Legacy Spec Scan Block complete
3. All 10 agentmemory spec files read; file-by-file table in GC-018
4. GC-023 line count check for all target files in `CVF_LEARNING_PLANE_FOUNDATION`
5. Confirm T5 `canReinject=false` invariant is still passing before touching any memory code

---

## Write Ownership

Codex owns (Phase 2a only):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` (new)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` (new)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` (new, `graph_search` deferred)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` (new)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/` — targeted tests per module (new)
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` — agentmemory row update
- `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md` — AIF-C row update

No provider, receipt, route, live reinjection, public-sync, or durable persistence changes.

---

## Execution Plan

1. Receive operator authorization and GC-018 acceptance
2. Read all 10 agentmemory spec files
3. Complete file-by-file absorption table in GC-018
4. Implement Module 1: `controlled-memory-gateway.ts`
5. Implement Module 2: `memory-lifecycle-policy.ts`
6. Implement Module 3: `memory-retrieval-policy.ts` (with `graph_search` explicitly deferred)
7. Implement Module 4: `memory-context-packager.ts`
8. Write targeted tests for each module
9. Verify T5 `canReinject=false` invariant still passes
10. Run full `CVF_LEARNING_PLANE_FOUNDATION` test suite and TypeScript check
11. Update registry agentmemory row
12. Update roadmap Progress Tracker AIF-C row
13. File completion review

---

## Evidence Requirements

- Full `CVF_LEARNING_PLANE_FOUNDATION` test suite PASS
- TypeScript check PASS
- GC-023 line count compliant for all new/modified files
- T5 `canReinject=false` invariant preserved (test evidence)
- `graph_search` explicitly deferred in `memory-retrieval-policy.ts`
- Legacy Spec Scan Block in GC-018 verified
- Completion review filed

---

## Owner / Source

Owner: Codex (implementer), Claude (reviewer), operator (authorizer).

Predecessor evidence (mandatory reading before GC-018):

- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- `docs/reviews/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
  (agentmemory row — `partially_absorbed`)
- `docs/baselines/archive/CVF_CONTROLLED_MEMORY_SOURCE_ADOPTION_MATRIX_2026-05-16.md`
- `docs/reviews/archive/CVF_CONTROLLED_MEMORY_RUNTIME_ADOPTION_CLOSURE_2026-05-16.md`
- `.private_reference/legacy/CVF 16.5/agentmemory/` — all 10 spec files:
  - `CVF_CONTROLLED_MEMORY_GATEWAY.md`
  - `CVF_MEMORY_ACCESS_POLICY.md`
  - `CVF_MEMORY_CAPTURE_ADAPTER.md`
  - `CVF_MEMORY_CONTEXT_PACKAGER.md`
  - `CVF_MEMORY_EVENT_HOOKS.md`
  - `CVF_MEMORY_GUARD_CONTRACT.md`
  - `CVF_MEMORY_LIFECYCLE_POLICY.md`
  - `CVF_MEMORY_PRIVACY_FILTER_POLICY.md`
  - `CVF_MEMORY_REINJECTION_PROTOCOL.md`
  - `CVF_MEMORY_RETRIEVAL_POLICY.md`
- T5 completion review:
  `docs/reviews/CVF_T5_RUNTIME_MEMORY_WIRING_COMPLETION_2026-05-22.md`

---

## Scope / Target / Owner Boundary

Target surfaces:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/` — new Phase 2a modules
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/` — targeted tests

Out of scope:

- No durable persistence, no SQLite, no external memory store
- No live reinjection on the `/api/execute` route (contract only)
- No public memory-readiness claim
- No provider, receipt, route, or public-sync change
- Phase 2b (`graph_search` retrieval) deferred until AIF-B completes

---

## Legacy Spec Scan Block (required in GC-018)

When filing the GC-018 for this tranche, Codex must complete and include:

```text
Legacy Spec Scan Block
- Registry read: docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md
- Legacy folders scanned:
  - .private_reference/legacy/CVF 16.5/agentmemory/ (all 10 files)
- Existing absorption evidence checked:
  - docs/baselines/archive/CVF_CONTROLLED_MEMORY_SOURCE_ADOPTION_MATRIX_2026-05-16.md
  - docs/reviews/archive/CVF_CONTROLLED_MEMORY_RUNTIME_ADOPTION_CLOSURE_2026-05-16.md
  - T5 completion review
- File-by-file absorption table:
  | File | Status in this tranche | Reason if deferred |
  | CVF_CONTROLLED_MEMORY_GATEWAY.md | absorbed / partial / deferred | ... |
  | CVF_MEMORY_ACCESS_POLICY.md | ... | ... |
  | CVF_MEMORY_CAPTURE_ADAPTER.md | ... | ... |
  | CVF_MEMORY_CONTEXT_PACKAGER.md | ... | ... |
  | CVF_MEMORY_EVENT_HOOKS.md | ... | ... |
  | CVF_MEMORY_GUARD_CONTRACT.md | ... | ... |
  | CVF_MEMORY_LIFECYCLE_POLICY.md | ... | ... |
  | CVF_MEMORY_PRIVACY_FILTER_POLICY.md | ... | ... |
  | CVF_MEMORY_REINJECTION_PROTOCOL.md | ... | ... |
  | CVF_MEMORY_RETRIEVAL_POLICY.md | ... | ... |
- Blindspot risk verdict: CLEAR (all 10 files explicitly covered)
```

---

## Phase 2a Deliverables (in-memory, no persistence)

### Module 1: `controlled-memory-gateway.ts`

Implements the gateway interface from `CVF_CONTROLLED_MEMORY_GATEWAY.md`:

- `MemoryGatewayRequest` — typed entry contract
- `MemoryGatewayDecision` — typed exit contract
- `evaluateMemoryGatewayRequest(req)` — dispatch to capture/retrieve/reinject

Boundary: no persistent store; delegates to in-memory working tier only.

### Module 2: `memory-lifecycle-policy.ts`

Implements lifecycle decay from `CVF_MEMORY_LIFECYCLE_POLICY.md`:

- `MemoryLifecycleState` — working | episodic | semantic | procedural
- `evaluateLifecycleTransition(tier, age, accessCount)` → new state
- Policy: working → episodic after session boundary; episodic → semantic after
  N accesses; semantic → procedural after M retrievals

Boundary: in-process only; no cross-session persistence.

### Module 3: `memory-retrieval-policy.ts`

Implements retrieval policy from `CVF_MEMORY_RETRIEVAL_POLICY.md`:

- `MemoryRetrievalMethod` — keyword | semantic | recency | audit_trust
- `graph_search` deferred (requires AIF-B)
- `evaluateRetrievalRequest(method, query, scope)` → `MemoryRetrievalResult`

Boundary: `graph_search` must be left as a stub or `DEFERRED` enum value
until AIF-B delivers the graph layer.

### Module 4: `memory-context-packager.ts`

Implements context packager from `CVF_MEMORY_CONTEXT_PACKAGER.md`:

- `MemoryContextBlock` — typed `[MEMORY_CONTEXT]` output format
- `packageMemoryContext(approved, excluded, policy)` → `MemoryContextBlock`
- Output includes: `purpose`, `scope`, `risk_level`, `approved_memory`,
  `constraints`, `excluded_memory`, `source_memory_ids`, `policy_decision`

Boundary: output format only; no actual reinjection into live route.

### Required tests per module

Each module must have a dedicated test file with at minimum:

- happy-path coverage
- `canReinject=false` invariant preserved (must not regress T5)
- boundary / edge case coverage

---

## GC-023 Pre-flight (required before implementation)

Before adding any module to `CVF_LEARNING_PLANE_FOUNDATION`:

1. Check current line count: `wc -l EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`
2. Check exception registry for `CVF_LEARNING_PLANE_FOUNDATION` entries
3. If adding to `index.ts` would exceed threshold, create dedicated module files
   instead (do not add inline)
4. New module files are separate files — GC-023 threshold applies per file

---

## Acceptance Criteria

- [ ] Blocked-work override for `new_memory_tiers_beyond_lane_h_scope` granted
      by operator (document which session/commit grants this)
- [ ] GC-018 filed and accepted with Legacy Spec Scan Block complete
- [ ] All 10 agentmemory spec files read; file-by-file table in GC-018
- [ ] `controlled-memory-gateway.ts` implemented and tested
- [ ] `memory-lifecycle-policy.ts` implemented and tested
- [ ] `memory-retrieval-policy.ts` implemented with `graph_search` explicitly
      deferred
- [ ] `memory-context-packager.ts` implemented and tested
- [ ] T5 `canReinject=false` invariant still passes
- [ ] `CVF_LEARNING_PLANE_FOUNDATION` full test suite PASS
- [ ] TypeScript check PASS
- [ ] GC-023 line count compliant for all modified/new files
- [ ] `CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` agentmemory row
      updated to reflect new absorption status
- [ ] Roadmap Progress Tracker AIF-C row updated to `CLOSED_PASS`
- [ ] `CVF_SESSION_MEMORY.md` pointer added
- [ ] Handoff Latest Work section updated with HEAD SHA

---

## Review Gate

Claude reviews the completion package for:

- All 4 Phase 2a modules implemented with targeted tests
- T5 `canReinject=false` invariant still passes
- `graph_search` explicitly deferred in `memory-retrieval-policy.ts`
- `CVF_LEARNING_PLANE_FOUNDATION` full test suite PASS
- TypeScript check PASS
- GC-023 compliant for all new files
- Legacy Spec Scan Block in GC-018 verified complete

---

## Closure Checklist

- [ ] Operator granted `new_memory_tiers_beyond_lane_h_scope` override
- [ ] GC-018 filed and accepted with Legacy Spec Scan Block
- [ ] All 10 agentmemory spec files read; file-by-file table complete
- [ ] `controlled-memory-gateway.ts` implemented and tested
- [ ] `memory-lifecycle-policy.ts` implemented and tested
- [ ] `memory-retrieval-policy.ts` implemented with `graph_search` deferred
- [ ] `memory-context-packager.ts` implemented and tested
- [ ] T5 `canReinject=false` invariant still passes
- [ ] `CVF_LEARNING_PLANE_FOUNDATION` full test suite PASS
- [ ] TypeScript check PASS
- [ ] GC-023 compliant for all new files
- [ ] Registry agentmemory row updated
- [ ] Roadmap Progress Tracker AIF-C row → `CLOSED_PASS`
- [ ] `CVF_SESSION_MEMORY.md` pointer added
- [ ] Handoff Latest Work updated with HEAD SHA
- [ ] Completion review filed

---

## Return-To-Orchestrator Conditions

Return to Claude (reviewer) when:

- All closure checklist items above are complete
- OR: a blocker is encountered (e.g., `canReinject=false` invariant broken, GC-023 threshold exceeded)

Do not return partial work. File the completion review before returning.

---

## Operator Checkpoint

Checkpoint required: operator must explicitly grant blocked-work override for `new_memory_tiers_beyond_lane_h_scope` — specifying which session or commit grants this — before implementation proceeds.

---

## Completion Review

After implementation, file at:
`docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-23.md`

Minimum sections: Purpose, Legacy Spec Scan Block (verified), Deliverables
Verified (per module), Acceptance Criteria (checklist), Claim Boundary.

---

## Claim Boundary

This work order does not authorize: durable persistence, SQLite graph storage,
live reinjection on production route, cross-session memory, public memory
readiness claim, provider change, receipt schema change, freeze release, or
`graph_search` retrieval (deferred to AIF-B). Phase 2b (graph retrieval)
requires AIF-B to complete first.
