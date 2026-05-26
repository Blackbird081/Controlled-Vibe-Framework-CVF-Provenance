# CVF Phase 2.B Runtime Coherence Roadmap

Memory class: FULL_RECORD

Status: READY_FOR_REBUTTAL

docType: roadmap

Date: 2026-05-21

---

## Purpose

Move Phase 2.B from bounded adapter/table coverage to runtime-coherence
evidence without claiming live provider proof.

This roadmap is the next required bridge after all 46 primary Phase 2.B rows
have bounded adapter/receipt coverage recorded.

---

## Authority Chain

- Static Phase 2.B migration plan:
  `docs/reference/archive/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- Final table-coverage completion:
  `docs/reviews/CVF_PHASE_2B_MEMORY_TAIL_ADAPTERS_MIGRATION_COMPLETION_2026-05-21.md`
- HN2.b owner map:
  `docs/reference/archive/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- HN2.c freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`

---

## Authorization / Decision

Decision: propose the next Phase 2.B tranche as internal runtime coherence,
not live proof.

Authorization posture: READY_FOR_REBUTTAL. Implementation requires a downstream
GC-018/work order after this roadmap is accepted.

---

## Problem Statement

Phase 2.B currently has complete bounded adapter/receipt coverage, but that is
not yet proof that the adapters compose coherently through the real internal
runtime chain.

The missing proof is not another row migration. The missing proof is an
end-to-end internal coherence chain that shows receipt, policy, risk, identity,
role, audit, trace, task, and memory adapter outputs can be joined into one
stable internal evidence graph without widening provider behavior or invoking a
live model.

---

## Scope

In scope:

- Runtime-coherence harness for existing Phase 2.B adapter outputs.
- Deterministic internal fixture path that exercises existing local contracts.
- Evidence graph validator that links adapter snapshots by receipt id, trace
  id, actor/session id, policy decision, risk level, task id, and memory id
  where available.
- Negative coherence cases for missing ids, mismatched trace ids, unsupported
  adapter versions, and overclaiming boundaries.
- Completion review that separates internal runtime coherence from live
  governance proof.

---

## Non-Goals

- No live provider call.
- No Maika proof.
- No public catalog update.
- No public-sync update.
- No new provider runtime behavior.
- No new policy, risk, guard, receipt, or memory engine.
- No persistent memory store.
- No database schema migration.
- No new memory tier.
- No reinjection runtime expansion.
- No HN2.c freeze lift or kernel owner replacement.
- No claim that CVF governs a real provider until the separate live-proof
  roadmap closes.

---

## Proposed Dependency Chain

Runtime coherence should close as a single bounded chain:

```text
RC-01 adapter inventory checksum
  -> RC-02 internal evidence graph schema
  -> RC-03 deterministic runtime-coherence harness
  -> RC-04 cross-family graph validator
  -> RC-05 negative coherence gates
  -> RC-06 completion review
```

The chain is intentionally sequential. `RC-03` must not run before `RC-01` and
`RC-02` lock the adapter inventory and graph keys.

---

## Work Packages

| id | package | done criterion |
| --- | --- | --- |
| RC-01 | Adapter inventory checksum | All Phase 2.B adapter exports are discoverable and versioned; missing export fails. |
| RC-02 | Internal evidence graph schema | Graph schema defines node/edge keys and forbidden claims. |
| RC-03 | Deterministic coherence harness | Local harness generates a joined receipt/policy/risk/identity/memory evidence graph. |
| RC-04 | Cross-family graph validator | Validator proves graph joins and rejects mismatched ids. |
| RC-05 | Negative coherence gates | Tests fail for missing receipt ids, trace mismatch, unsupported adapter version, and live-proof overclaim. |
| RC-06 | Completion review | Review states exactly what internal coherence proves and does not prove. |

---

## Work Plan

1. File reviewer rebuttal for this roadmap.
2. If accepted, file a bounded GC-018/work order for `RC-01 -> RC-06`.
3. Implement the adapter inventory checksum and evidence graph schema first.
4. Build the deterministic runtime-coherence harness against existing local
   contracts.
5. Add cross-family graph validation and negative coherence gates.
6. Run package/docs verification and file completion review.

---

## Acceptance Criteria

- One command runs the internal coherence harness without live provider keys.
- The harness consumes existing Phase 2.B adapter/receipt outputs, not ad hoc
  string fixtures.
- The graph validator proves all available adapter families can be joined by
  stable evidence keys.
- Negative tests prove the validator catches broken joins.
- Completion review explicitly says this is not live governance proof.
- No provider, Maika, persistence, database, public-sync, or kernel-owner
  behavior changes are introduced.

---

## Verification / Evidence

Required verification after implementation:

- targeted runtime-coherence harness tests;
- package type/build checks for touched packages;
- docs governance compatibility check;
- markdown structural completeness check;
- completion review with Evidence Trace Block.

Suggested command name:

```bash
node scripts/run_phase2b_runtime_coherence_harness.mjs --json
```

The exact command may change during implementation if the existing repo pattern
requires a TypeScript or package-local runner.

---

## Exit Condition

Runtime coherence is closed only when a completion review records:

- graph schema version;
- adapter inventory checksum;
- positive coherence result;
- negative coherence gates;
- unchanged provider/Maika/memory/database/public boundaries.

---

## Downstream Dependency

The separate live-proof roadmap must not execute until this runtime-coherence
roadmap is closed.

---

## Claim Boundary

This roadmap may be cited only as proposed authorization for internal Phase 2.B
runtime-coherence proof.

It must not be cited as live governance proof, provider proof, Maika proof,
public capability evidence, persistent memory evidence, or global freeze
release.
