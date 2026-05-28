# CVF GC-018 AIF-C - Memory Gateway Phase 2a

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

Date: 2026-05-24

## Purpose

Authorize bounded implementation of AIF-C Memory Gateway Phase 2a inside
`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/` after operator unblock. The tranche
absorbs the legacy `agentmemory` specification set into local deterministic
memory policy modules and tests.

## Scope

In scope:

- `controlled-memory-gateway.ts`
- `memory-lifecycle-policy.ts`
- `memory-retrieval-policy.ts`
- `memory-context-packager.ts`
- targeted unit tests and TypeScript verification
- registry, roadmap, session, work-order, and completion-review updates

Out of scope:

- durable memory persistence
- cross-session memory store
- live `/api/execute` memory reinjection
- provider routing or receipt semantics
- public-sync work
- `graph_search` activation before explicit integration

## Source / Predecessor Evidence

- `docs/roadmaps/archive/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`
- `docs/work_orders/archive/CVF_WO_AIF_C_MEMORY_GATEWAY_PHASE2_2026-05-23.md`
- `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `.private_reference/legacy/CVF 16.5/agentmemory/`

## Decision / Baseline / Proposed Tranche

Decision: proceed after the operator's 2026-05-24 instruction to complete the
roadmap and work orders. This is treated as the explicit
`new_memory_tiers_beyond_lane_h_scope` override required by the work order.

Baseline: H2/T5 proved bounded ephemeral memory surfaces, but the legacy
controlled-memory gateway doctrines were not fully represented in runtime-owned
Learning Plane modules.

Proposed tranche: implement Phase 2a as local policy and packaging modules with
no durable persistence and no live provider reinjection.

## Legacy Spec Scan Block

Legacy folder scanned:

- `.private_reference/legacy/CVF 16.5/agentmemory/`

| File | Status in this tranche | Reason if deferred |
| --- | --- | --- |
| `CVF_CONTROLLED_MEMORY_GATEWAY.md` | ABSORBED | Gateway operations, policy decision, audit receipt, and raw-release boundary mapped to `controlled-memory-gateway.ts`. |
| `CVF_MEMORY_ACCESS_POLICY.md` | ABSORBED | Access decisions and default-deny posture mapped to gateway and retrieval policy. |
| `CVF_MEMORY_CAPTURE_ADAPTER.md` | DEFERRED | Event capture adapter requires runtime event surfaces outside Phase 2a. |
| `CVF_MEMORY_CONTEXT_PACKAGER.md` | ABSORBED | Governed `[MEMORY_CONTEXT]` block mapped to `memory-context-packager.ts`. |
| `CVF_MEMORY_EVENT_HOOKS.md` | DEFERRED | Hook emission requires integration into runtime event lifecycle. |
| `CVF_MEMORY_GUARD_CONTRACT.md` | ABSORBED | Required checks and output boundaries mapped to gateway decisions. |
| `CVF_MEMORY_LIFECYCLE_POLICY.md` | ABSORBED | Working, episodic, semantic, procedural, disputed, expired, forgotten transitions mapped to `memory-lifecycle-policy.ts`. |
| `CVF_MEMORY_PRIVACY_FILTER_POLICY.md` | ABSORBED | Privacy filtering represented as redaction and exclusion outcomes. |
| `CVF_MEMORY_REINJECTION_PROTOCOL.md` | PARTIAL | Summary-only reinjection boundary represented; live agent-context reinjection remains deferred. |
| `CVF_MEMORY_RETRIEVAL_POLICY.md` | ABSORBED | Keyword, semantic, recency, audit-trust filtering mapped; `graph_search` remains deferred. |
| `Thong_tin.md` | METADATA_READ | Metadata file read for folder context; no runtime rule required. |

## Depth Audit

| Candidate | Type | Score | Decision | Rationale |
| --- | --- | ---: | --- | --- |
| Phase 2a local policy modules | IMPLEMENTATION_FOUNDATION | 9/10 | CONTINUE | Directly addresses the legacy absorption blindspot without widening live runtime behavior. |
| Durable memory persistence | PERSISTENCE_CHANGE | 0/10 | REJECT | Outside operator-confirmed in-memory tranche and would require separate persistence authorization. |
| Live prompt reinjection | GOVERNANCE_RUNTIME_CHANGE | 0/10 | REJECT | Would assert governed AI behavior and require live proof plus route integration. |
| `graph_search` retrieval activation | CROSS_TRANCHE_DEPENDENCY | 4/10 | DEFER | Requires AIF-B graph service integration after Phase 1 foundation. |

## Acceptance Criteria

- GC-018 filed with complete Legacy Spec Scan Block.
- All implementation-facing `agentmemory` specs read and classified.
- Phase 2a modules implemented under Learning Plane ownership.
- Targeted tests and TypeScript check pass.
- Registry, roadmap tracker, session memory, active state, handoff, and work
  order are updated.
- Completion review filed.

## Evidence / Verification

Required verification:

- focused AIF-C test coverage
- Learning Plane `npm run check`
- Learning Plane full test suite
- repository governance hook chain before commit

No live provider API call is required because this tranche does not claim live
CVF governance behavior or provider execution.

## Claim Boundary

AIF-C can claim only a local deterministic Memory Gateway Phase 2a foundation.
It cannot claim durable memory, cross-session memory, provider-routed memory,
live prompt reinjection, full Pain H closure, or public product readiness.
