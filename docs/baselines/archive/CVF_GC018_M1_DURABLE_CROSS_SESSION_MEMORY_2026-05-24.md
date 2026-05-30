# CVF GC-018 - M1: Durable Cross-Session Memory

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS

docType: baseline

Date: 2026-05-24

---

## STOP — Demand Gate

This baseline is `DEMAND_GATED`. Codex must not begin M1 implementation until
M2 (`CVF_WO_M2_D06_MEMORY_TIER_FREEZE_RELEASE_2026-05-24.md`) has status
`CLOSED_PASS`.

Check M2 work order status before reading further. If M2 is not `CLOSED_PASS`,
stop and return to operator.

---

## Scope

Authorize one bounded M1 durable memory tranche after M2 CLOSED_PASS.

Scope: skill-tier and long-term-tier durable memory storage with explicit policy
authorization and receipt evidence. No tier below long-term is authorized for
durable persistence.

---

## Purpose

After M2 releases the freeze on `memory-tier-classifier.contract.ts`, M1
implements durable storage for skill-tier and long-term-tier memory using the
tier classifier as the policy gate. This enables cross-session memory reads
and writes under the AIF C2 summary-only reinjection gate.

---

## Source / Predecessor Evidence

- M2 GC-018: `docs/baselines/CVF_GC018_M2_D06_MEMORY_TIER_FREEZE_RELEASE_2026-05-24.md`
- Memory gateway: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
- Memory lifecycle policy: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts`
- Memory retrieval policy: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
- Memory context packager: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- Memory tier classifier (to be unfrozen by M2): `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`
- AIF C2 reinjection gate: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts`
- Runtime memory hierarchy: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/memory/runtime-memory-hierarchy.ts`
- Legacy spec absorption registry: `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`

---

## Legacy Spec Scan Block

Per corrective control from `docs/reviews/archive/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`:
any memory tranche must read the legacy spec absorption registry before design.

Legacy sources relevant to M1:

- `.private_reference/legacy/CVF 16.5/agentmemory/` — 10 files: Memory Gateway,
  lifecycle decay (working→episodic→semantic→procedural), semantic/graph
  retrieval, context packager, reinjection protocol. Codex must read these
  before designing the durable store interface to avoid re-implementing without
  legacy precedent.

Codex must: (a) read the registry, (b) confirm relevant legacy files have been
read, (c) note in GC-018 if any legacy design decision conflicts with the
implementation plan.

---

## Decision / Baseline / Proposed Tranche

Decision: after M2 CLOSED_PASS, execute a bounded M1 durable memory tranche
wiring skill-tier and long-term-tier storage to the unlocked tier classifier.

Baseline: currently all tiers have `canReinject=false` and
`durablePersistenceAllowed=false` in `runtime-memory-hierarchy.ts`. M1 changes
the persistence path for skill and long-term tiers only, under explicit policy
authorization, while preserving the reinjection constraint as summary-only
via the AIF C2 gate.

---

## Guardrails

- `canReinject=false` invariant must be preserved in `runtime-memory-hierarchy.ts`.
  Reinjection is only allowed through the existing AIF C2 summary-only gate.
- Only skill-tier and long-term-tier may be durably persisted. Working, task,
  audit, and receipt tiers must remain as-is.
- No raw memory may reach the provider prompt. All reinjection passes through
  `evaluateAifMemoryReinjection()` in `aif-memory-reinjection.ts`.
- Privacy filters for `containsSecret`, lifecycle state `expired`/`disputed`,
  and provenance score must be enforced at write time.
- Cross-session memory read path must emit a receipt with memory ids, scope,
  and policy decision.
- No autonomous memory write. All durable writes must be explicitly authorized
  via the policy gate.
- Durable store backend is in-scope for this tranche (file-system or SQLite).
  Hosted/cloud persistence is out of scope.

---

## Pass Conditions

- Durable store interface for skill-tier and long-term-tier implemented.
- Cross-session write: at least one governed write with receipt.
- Cross-session read: at least one governed read with receipt.
- Summary-only reinjection path proven through AIF C2 gate with live receipt.
- `canReinject=false` binding test still PASS.
- All relevant test suites PASS (CVF_LEARNING_PLANE_FOUNDATION, cvf-web
  targeted tests).
- TypeScript check PASS.
- Release gate PASS.
- Governance review filed at:
  `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`

---

## Evidence / Verification

Required evidence before this baseline is closed:

- M2 work order status `CLOSED_PASS` confirmed.
- Durable store interface implemented for skill-tier and long-term-tier.
- Cross-session write receipt and cross-session read receipt filed.
- `canReinject=false` binding test PASS.
- TypeScript check PASS (LPF + cvf-web).
- Release gate PASS.
- Completion review filed at:
  `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`

---

## Claim Boundary

M1 claims bounded durable memory for skill-tier and long-term-tier with
policy-gated cross-session read/write and receipt evidence. It does not claim
autonomous reinjection, broad memory authority, privacy bypass, hosted/cloud
persistence, or any kernel surface modification beyond what M2 already
authorized.

---

## Disposition

Closed by `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`.
