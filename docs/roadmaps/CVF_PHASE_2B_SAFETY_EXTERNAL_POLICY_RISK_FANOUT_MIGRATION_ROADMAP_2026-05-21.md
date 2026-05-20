# CVF Phase 2.B Safety External Policy Risk Fanout Migration Roadmap

Memory class: FULL_RECORD

Status: CLOSED_SAFETY_EXTERNAL_POLICY_RISK_FANOUT_MIGRATION

docType: roadmap

Date: 2026-05-21

---

## Status

This roadmap authorizes and records a grouped but bounded Phase 2.B dependency
tranche:

- Safety Tail Risk Chain: `R-02 -> R-04 / R-05 / R-15 / R-16`
- External / Ecosystem Risk Fanout: `R-01 -> R-06 / R-07 / R-08 / R-09 / R-10 / R-11 / R-12`
- External policy chain: `P-01 -> P-07 / P-08`

It is not a broad Phase 2.B bulk migration.

---

## Authorization / Decision

Authority chain:

- Phase 2.B migration plan:
  `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- Prior receipt critical path closure:
  `docs/reviews/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_COMPLETION_2026-05-20.md`
- Prior audit/trace/task receipt chain closure:
  `docs/reviews/CVF_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_COMPLETION_2026-05-20.md`
- Prior policy/risk adapter closure:
  `docs/reviews/CVF_PHASE_2B_POLICY_RISK_CHAIN_ADAPTERS_MIGRATION_COMPLETION_2026-05-20.md`
- Prior identity/control-plane adapter closure:
  `docs/reviews/CVF_PHASE_2B_IDENTITY_CONTROL_PLANE_ADAPTERS_MIGRATION_COMPLETION_2026-05-21.md`
- HN2.b owner map:
  `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- HN2.c freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`

Decision: run these chains together because all are additive risk/policy
adapter or snapshot surfaces and all can close without changing provider
runtime, Maika, persistent memory-store, database schema, kernel ownership, or
live governance behavior.

---

## Purpose / Why This Tranche

Earlier Phase 2.B slices closed critical receipt, policy/risk, and
identity/control-plane anchors. This tranche finishes the requested safety-tail
and external/ecosystem fanout surfaces so risk and external policy decisions
can be cited through versioned adapter snapshots instead of implicit local
return values.

---

## Scope

In scope:

- Safety-tail adapters for risk evolution, refusal risk gate, risk lock, and
  hardening risk scorer surfaces.
- External/ecosystem risk adapters for ECO risk scorer, aggregator, agent
  guard risk module, MCP risk gate, Guard Contract risk gate, Phase Governance
  risk gate, External Integration risk hook, and Skill Governance risk scorer.
- External policy adapters for Certification State Machine and Policy Decision
  Engine.
- Focused tests and completion evidence.
- Codex-only workflow role chain.

---

## Non-Goals

- No Claude review or Claude-authored work product.
- No provider runtime call.
- No live governance proof claim.
- No Maika change.
- No persistent memory-store implementation.
- No database schema migration.
- No new policy/risk/guard engine.
- No kernel owner replacement.
- No public catalog or public-sync claim update.
- No global freeze lift.
- No rows outside the listed dependency chains.

---

## Work Plan

1. Add safety-tail risk evolution and refusal risk gate adapter snapshots.
2. Add safety-hardening risk scorer and risk lock adapter snapshots.
3. Add ECO risk scorer and aggregator adapter snapshots.
4. Add Agent Guard SDK risk module adapter snapshot.
5. Add MCP, Guard Contract, and Phase Governance risk gate adapter snapshots.
6. Add External Integration risk hook, policy decision, and certification
   adapter snapshots.
7. Add Skill Governance risk scorer adapter snapshot.
8. Add focused tests.
9. Run package tests/checks where toolchains are present.
10. File completion review and update active session pointers.

---

## Acceptance Criteria

- Existing score/evaluate/transition outputs remain unchanged.
- New adapters are additive snapshots with explicit version/source metadata.
- No adapter executes provider calls or changes policy decisions.
- No snapshot claims live governance proof.
- Completion review records no Claude participation and no provider/Maika/live
  proof/global-freeze/public-catalog claim.

---

## Verification / Evidence

Required:

- Focused tests for each touched package with available local toolchain.
- Type/build checks for packages with build/check scripts or local `tsc`.
- Documentation governance checks.
- Completion review with explicit bounded claim.

Known environment boundary:

- `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME` targeted Vitest is blocked by the
  existing package environment missing a local `vitest` binary. This does not
  create a live-governance claim.

---

## Claim Boundary

This roadmap may be cited only as authorization for the listed
safety-tail/external-risk/external-policy adapter snapshot chains. It must not
be cited as broad Phase 2.B migration, live runtime proof, provider execution
change, Maika change, persistent memory, database schema migration, Claude
review, public catalog update, kernel owner replacement, or global freeze
release.
