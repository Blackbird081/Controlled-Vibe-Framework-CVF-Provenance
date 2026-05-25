# CVF GC-018 Phase 2.B Runtime Coherence Baseline

Memory class: SUMMARY_RECORD

Status: GC018_ACCEPTED

docType: baseline

Date: 2026-05-21

---

## Source / Predecessor Evidence

- `docs/reference/archive/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_MEMORY_TAIL_ADAPTERS_MIGRATION_COMPLETION_2026-05-21.md`
- `docs/roadmaps/CVF_PHASE_2B_RUNTIME_COHERENCE_ROADMAP_2026-05-21.md`
- `docs/reviews/CVF_PHASE_2B_RUNTIME_COHERENCE_CODEX_REBUTTAL_2026-05-21.md`
- `docs/roadmaps/CVF_PHASE_2B_LIVE_GOVERNANCE_PROOF_ROADMAP_2026-05-21.md`

---

## Purpose

Authorize implementation of the Phase 2.B internal runtime-coherence proof
chain:

`RC-01 -> RC-02 -> RC-03 -> RC-04 -> RC-05 -> RC-06`

---

## Authorization / Decision

Decision: ACCEPTED.

The work may implement a deterministic internal coherence graph, validator,
targeted test harness, wrapper command, and completion review.

---

## Scope / Target / Owner Boundary

Owner boundary: Guard Contract runtime-coherence graph only.

In scope:

- adapter inventory checksum;
- internal evidence graph schema;
- deterministic runtime-coherence harness;
- cross-family graph validator;
- negative coherence gates;
- completion review.

---

## Target / Source Under Review

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/phase2b-runtime-coherence.contract.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phase2b-runtime-coherence.test.ts`
- `scripts/run_phase2b_runtime_coherence_harness.mjs`

---

## Scope / Methodology

Implement in a package-local way that does not introduce provider runtime,
web-route runtime, persistent memory, or kernel-owner replacement.

---

## Evidence Trace Block

| Required evidence | How it will be proven |
| --- | --- |
| 46 row inventory coverage | graph validator requires all primary row ids |
| representative adapter outputs | targeted test builds nodes from migrated adapter outputs |
| graph joins | edge validator checks shared keys |
| negative gates | tests reject missing row, trace mismatch, live-mode claim, forbidden claim |

---

## Findings / Position

The proposed scope is bounded and consistent with HN2.c because it does not
change canonical ownership or release frozen kernel behavior.

---

## Risk / Defect / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Live proof bundled too early | graph evidence mode must be `internal_fixture` |
| Adapter table coverage is mistaken for runtime coherence | completion must cite positive graph validation |
| Runtime path is widened | no provider/web/persistence code may be touched |

---

## Verification

Required:

- `npm test -- --run src/contracts/contracts.phase2b-runtime-coherence.test.ts`
  in `EXTENSIONS/CVF_GUARD_CONTRACT`;
- `npm run check` in `EXTENSIONS/CVF_GUARD_CONTRACT`;
- `node scripts/run_phase2b_runtime_coherence_harness.mjs --json`;
- docs governance and markdown structural checks.

---

## Decision / Recommendation / Disposition

Proceed to work order.

---

## Claim Boundary

This GC-018 authorizes internal runtime coherence only. It does not authorize
live provider proof, provider runtime changes, Maika changes, persistent
memory, database schema migration, public-sync updates, public catalog claims,
or global freeze release.
