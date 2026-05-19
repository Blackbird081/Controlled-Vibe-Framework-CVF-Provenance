# CVF Next Phase Roadmap — Lane D + E + F + G

Memory class: SUMMARY_RECORD
Status: OPERATOR_APPROVED — 2026-05-19

## Authorization / Decision

Authority: `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
Decision pack: `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md`
Session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
Implementer: Codex (per lane, sequentially)
Reviewer: Claude
Protocol: GC-018 per lane before implementation

Operator instruction (2026-05-19): implement all four remaining lanes D + E
+ F + G in sequence, using the same work-order discipline established in Lane
B/C/H.

## Purpose

This roadmap defines the four remaining implementation lanes approved after
Lane B/C/H closure. Each lane extends an existing CVF foundation — none is a
blank-slate build. Codex must read the existing infrastructure before writing
anything new.

Lane execution order: D → E → F → G.

Each lane requires its own GC-018 before implementation begins. No lane may
be parallelized or skipped without operator instruction.

---

## Scope

This roadmap covers only the remaining approved Lane D, Lane E, Lane F, and
Lane G work after Lane B/C/H closure. It authorizes detailed lane-specific
work orders, per-lane GC-018 packets, implementation, review packets, and
GC-020 handoff syncs for those four lanes.

Out of scope: any new lane beyond D/E/F/G, public repository claim changes,
global stop-rule changes, and live governance claims not backed by the
required lane evidence packet.

---

## Non-Goals

- Globally lifting `system_reconvergence_stop` — lifted per-lane only
- Building stream/reasoning/vision from zero (D already has gateway foundation)
- Rebuilding benchmark from zero (E already has W72/W91/W98/QBS-1 runs)
- Rebuilding template system from zero (F already has 10+ outcome categories)
- Building a new RBAC system (G extends existing `CVFRole`/`resolveExecutionCVFRole`)
- New provider integrations beyond what the current routing policy supports
- Multi-tenant cloud enforcement
- Public claims without evidence receipts

---

## Prerequisite First Reads (before any GC-018)

Before filing the first GC-018 for Lane D, Codex must read:

1. `CVF_SESSION_MEMORY.md` — active session mode
2. `AGENT_HANDOFF_V9_2026-05-18.md` — active posture and stop-lift boundary
3. `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` —
   corrected problem map; understand what already exists
4. `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md`
   — §4 Canonical Ownership Map
5. `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_B_C_H_2026-05-19.md` —
   the B/C/H pattern; this roadmap follows the same structure
6. `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` —
   role ownership for each phase
7. `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` —
   GC-023 file-size limits before touching any governed file

Anti-duplication rule: before writing any new file or function, grep the
relevant existing source to verify it does not already exist.

---

## Work Plan

1. Lane D: complete provider method parity foundation for the stream contract
   and CLI `--stream` handoff.
2. Lane E: define offline governance reliability metrics and publish the first
   baseline from audit log data.
3. Lane F: add noncoder outcome quick-action buttons using existing governed
   packs and home-page flow.
4. Lane G: add the minimum runtime actor gate through `allowedActorRoles` and
   the existing execute role resolver.

Each lane must produce a work order, GC-018 authorization, implementation
evidence, reviewer disposition, and GC-020 handoff sync before the next lane
starts.

---

## Lane D — Provider Method Parity

### Problem (from corrected problem map)

`CVF_MODEL_GATEWAY` exists with routing policy, fallback policy, gateway
receipt, and provider registry. Gap: `stream()`, `reasoning()`, `vision()`,
`embedding()` method signatures are not standardized across providers. The
gateway knows how to route but not how to normalize method-level contracts.

### Demand gate

**Selected use case: streaming execution response** — when `cvf execute` is
called with `--stream`, the CLI should receive a streamed response rather
than a single buffered completion. This is the first concrete consuming flow
for `stream()` parity.

### Scope

- Add `StreamContract` interface to `CVF_MODEL_GATEWAY` defining the standard
  stream response envelope (chunk, role, done signal, receipt obligation)
- Add `stream()` method stub to `LLMAdapter` interface (already has `complete()`)
- Wire `cvf execute --stream` flag in `CVF_ECO_v2.2_GOVERNANCE_CLI` to pass
  `stream: true` in the POST body to `/api/execute`
- Add a `streamingEnabled` field to `execution.policy.json` in governed packs
  that support streaming
- Tests: unit tests for StreamContract, stream flag parsing in CLI
- No live streaming implementation in Next.js route — that is Lane D+1

### Forbidden scope

- Implementing `reasoning()`, `vision()`, `embedding()` — demand-gated on
  separate consuming flows
- Adding live streaming SSE handler to route.ts — beyond this lane's scope
- New provider registration — routing policy is not changed
- Public catalog row upgrade without Test-Path verification

### Risk ceiling: R1

---

## Lane E — Benchmark Reorientation

### Problem (from corrected problem map)

W72/W91/W98/QBS-1 benchmark infrastructure exists. Gap: metrics measure
output quality and provider latency; they do not measure governance
reliability (policy violation rate, receipt integrity rate, cross-session
continuity rate, hallucination recovery rate).

### Demand gate

**Selected metric set: governance receipt integrity** — measure what
percentage of governed executions produce a valid governance receipt with
non-null `receiptId`, `stepTraces`, and `decision` fields. This is directly
observable from existing audit event output.

### Scope

- Add `governance-reliability-metrics.ts` to `CVF_ECO_v2.2_GOVERNANCE_CLI`
  with 4 metric definitions: `receiptIntegrityRate`, `policyDecisionRate`,
  `stepTraceCompletionRate`, `auditEventCaptureRate`
- Add `cvf benchmark governance` CLI subcommand that reads a JSONL audit log
  and computes the 4 metrics
- Add `docs/benchmark/CVF_GOVERNANCE_RELIABILITY_BASELINE_2026-05-19.md`
  recording the first baseline run against Phase E audit log data
- Tests: unit tests for each metric computation
- No change to existing QBS-1 preregistration files

### Forbidden scope

- Rebuilding QBS-1 or W72/W91/W98 benchmark files
- Adding hallucination recovery metric (requires live multi-turn session data
  — demand-gate for Lane E+1)
- Connecting to live provider for benchmark run — offline JSONL only for Lane E
- Changing public benchmark claims

### Risk ceiling: R0 (offline computation only)

---

## Lane F — Noncoder UX

### Problem (from corrected problem map)

Templates, template marketplace, and W122–W130 noncoder work all exist. Gap:
the home page UX still requires the user to navigate the canonical
`src/lib/templates/` directory-backed categories manually. `[Create Product
Brief]`, `[Generate SOP]`, `[Analyze Strategy]` are not promoted as
first-class outcome buttons on the home surface.

### Demand gate

**Selected outcome surface: 3 outcome quick-action buttons on the home page**
— `Create Product Brief`, `Generate SOP`, `Analyze Strategy`. Each button
pre-fills the corresponding governed pack template and immediately enters the
execution flow without requiring the user to browse categories.

### Scope

- Add `OutcomeQuickActions` component to `cvf-web/src/components/` with 3
  outcome buttons (uses the 3 governed packs from Lane B)
- Wire `OutcomeQuickActions` into the home page (`(dashboard)/home/page.tsx`)
  as a prominent row above the template browser
- Each button calls `handleTryTemplate` (already exists) with the governed
  pack's templateId pre-filled
- Add bilingual labels (vi/en) following the existing `lang` prop pattern
- Tests: component render test, button click triggers correct templateId
- No new template categories — use only the 3 governed packs from Lane B

### Forbidden scope

- Adding a new `app_builder_complete`/`documentation`/`strategy_analysis`
  template — only use existing governed packs
- Redesigning the template browser or category navigation
- Adding a new page route
- Changing auth/RBAC logic

### Risk ceiling: R0 (UI component only, no runtime change)

---

## Lane G — Runtime Actor Enforcement

### Problem (from corrected problem map)

Phase D contracts define `CVFRole`, `resolveExecutionCVFRole()` is wired in
route.ts. Gap: worker/planner/reviewer/auditor roles are defined in the role
assignment matrix but not enforced as distinct runtime execution boundaries.
The execute path resolves a role but does not gate on actor type — an
`OBSERVER` runtime role could submit an execution if the permission check
passed.

### Demand gate

**Selected enforcement point: minimum actor role gate in execute route** —
before dispatching to the AI provider, check that the resolved actor role is
in the `allowedActorRoles` list from the governing workflow pack's
  `execution.policy.json`. Reject with `403` if the actor role is not allowed.
  Use the existing `CVFRole` values already emitted by
  `resolveExecutionCVFRole()` (`OPERATOR`, `BUILDER`, `REVIEWER`, `OBSERVER`,
  `SERVICE_AGENT`), not display/RBAC labels such as Owner/Admin/Viewer.

### Scope

- Add `allowedActorRoles` field to `execution.policy.json` schema in each
  governed pack (array of `CVFRole` strings)
- Add `validateActorRoleGate()` function in
  `cvf-web/src/lib/execute-role-resolver.ts` (already exists) that checks
  `resolvedExecutionRole.role` against `allowedActorRoles`
- Wire the gate into `route.ts` immediately after `resolveExecutionCVFRole()`
  — if role is not in `allowedActorRoles`, return `{ status: 403, error: 'actor_role_not_permitted' }`
- Update all 3 governed packs to include `allowedActorRoles`
- Tests: unit tests for `validateActorRoleGate()`, route integration test for
  the 403 path
- Emit `actor_role_gate_result` in audit event payload

### Forbidden scope

- Adding planner/worker/auditor as separate session or job types
- Changing the `CVFRole` enum or permission profile logic
- Implementing a background job queue or worker pool
- Enforcement beyond the `allowedActorRoles` check

### Risk ceiling: R1 (existing execute path gating only)

---

## Commit and Handoff Discipline

Same as Lane B/C/H:

- Separate commits per lane: GC-018, implementation, completion packet, GC-020 sync
- No `--no-verify`
- No public catalog edit from the governance repo
- GC-020 handoff update after every commit

---

## Acceptance Criteria

- [ ] Lane D closes with stream contract and CLI flag behavior defined and
      unit-tested.
- [ ] Lane E closes with all 4 governance reliability metrics defined,
      unit-tested, and recorded in an offline baseline.
- [ ] Lane F closes with 3 outcome quick actions rendered and tested against
      the correct governed pack template IDs.
- [ ] Lane G closes with `allowedActorRoles` checked before provider dispatch
      and unit/integration evidence for permitted and denied roles.
- [ ] Each lane has a completion review packet and GC-020 handoff sync.

## Verification / Evidence

Required evidence for closure:

- Per-lane GC-018 file before implementation starts.
- Per-lane work order in `docs/work_orders/`.
- Targeted unit or integration test output for every changed behavior.
- Reviewer disposition in `docs/reviews/`.
- Hook-chain proof without bypassing hooks.

---

## Claim Boundary

Lane D closes with: `stream()` method contract defined and CLI flag wired —
`defined`

Lane E closes with: 4 governance reliability metrics defined and baseline
computed from audit log — `defined, offline-tested`

Lane F closes with: 3 outcome quick-action buttons on home page — `defined,
unit-tested`

Lane G closes with: `allowedActorRoles` gate enforced in execute route —
`defined, unit-tested`

No lane may claim live-proven, runtime-enforced, or production-ready behavior
without a separate GC-018 with live proof evidence.
