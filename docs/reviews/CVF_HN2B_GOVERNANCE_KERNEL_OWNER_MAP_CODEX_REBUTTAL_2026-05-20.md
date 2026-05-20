# CVF HN2.b Governance Kernel Owner Map Codex Rebuttal

Memory class: FULL_RECORD

Status: REBUTTAL_FILED_NON_BLOCKING_WITH_SCOPE_REFINEMENT

docType: review

Reviewer: Codex

Date: 2026-05-20

---

## Purpose

Review the HN2.b owner-map roadmap and decide whether it may proceed later to
its own GC-018 and implementation work order.

This is a rebuttal-only packet. It authorizes no owner-map artifact, no GC-018,
no code/runtime change, no doctrine edit, no public-sync work, and no freeze
posture lift.

---

## Scope / Target / Owner Boundary

In scope:

- `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
- `docs/work_orders/CVF_WO_HN2B_OWNER_MAP_REBUTTAL_2026-05-20.md`
- `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
- `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_CLOSURE_REVIEW_2026-05-20.md`
- `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
- selected source spot-checks from the HN2.a owner candidates

Out of scope:

- producing `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_*.md`;
- filing HN2.b GC-018;
- creating new classifications beyond the declared 11;
- changing doctrine, runtime, provider, memory, Maika, or public-sync files.

---

## Target / Source Under Review

Queue item:

- `hn2b-owner-map-roadmap`

Expected response path:

- `docs/reviews/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_CODEX_REBUTTAL_2026-05-20.md`

Roadmap under review:

- `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`

---

## Scope / Methodology

Method:

1. Confirmed the active queue item is `READY_FOR_REBUTTAL`.
2. Verified HN2.a closed as an inventory-only packet and lists 12 surfaces.
3. Checked HN2.b covers all 12 surfaces with per-surface decision notes and
   GC-018 acceptance seeds.
4. Checked the 11-class classification set and patched the roadmap to add
   class precedence and parallel sub-surface handling.
5. Spot-checked owner candidates:
   `orchestrator.contract.ts`, `policy-decision.contract.ts`, `engine.ts`,
   and `types.ts`.
6. Checked doctrine/control-matrix context and the HN2 split direction.

No live governance proof was run. This review is static.

---

## Findings / Position

Position: **NON_BLOCKING_WITH_SCOPE_REFINEMENT**.

Findings:

1. HN2.b is correctly separated from HN2.a and HN2.c. HN2.a remains
   observation-only; HN2.b would classify owners; HN2.c would codify the
   freeze-release rule.
2. The roadmap covers the 12 HN2.a surfaces: authority, roles, policy
   decision, risk, guard, lifecycle, delegation/handoff, receipt, memory,
   capability, provider execution, and vocabulary aliases.
3. The 11-class set is acceptable after refinement:
   `canonical_owner`, `canonical_alias`, `adapter_required`, `legacy_alias`,
   `deferred`, `rejected`, `parallel_surface`, `documentation_alias`,
   `repository_guard`, `runtime_guard`, `canonical_method_contract`.
4. I patched the roadmap before filing this rebuttal to fix two planning
   issues: stale `MEMORY.md` references now point to `CVF_SESSION_MEMORY.md`,
   and class precedence now prevents `canonical_owner` from colliding with
   guard/provider-specific classes.
5. Source spot-checks support the roadmap direction:
   `orchestrator.contract.ts` carries delegation/ticket/receipt-required
   semantics, `policy-decision.contract.ts` defines `PolicyDecision` and the
   R0-R3 risk type used by policy evaluation, `engine.ts` owns runtime guard
   evaluation, and `types.ts` owns shared runtime vocabulary plus
   `GovernanceEvidenceReceipt`.
6. The downstream owner map must not become a doctrine rewrite. It must be a
   routing/reference artifact with evidence paths and a forbidden-expansion
   register.

---

## Risk / Defect / Corrective Action

| Risk | Corrective action |
| --- | --- |
| `canonical_owner` becomes ambiguous for split surfaces | Use explicit parallel sub-surface rows and class precedence |
| Owner map adds new governance semantics | GC-018 must forbid new role, engine, receipt, tier, method, phase, or surface |
| Guard model collapses runtime and repository guard layers | Keep `runtime_guard` and `repository_guard` as separate classes |
| Provider-method contracts are bundled into runtime provider support | Keep method contracts as `canonical_method_contract`; runtime remains separately gated |
| HN2.b is treated as HN2.c | HN2.b may not author freeze-release policy text |

---

## Decision / Recommendation / Disposition

Disposition: **NON_BLOCKING_WITH_SCOPE_REFINEMENT**.

HN2.b may proceed later to a slice-specific GC-018 only if that GC-018 includes:

- owner map artifact path under `docs/reference/`;
- the closed 11-class classification set and class-precedence rule;
- full coverage of every HN2.a alias;
- evidence path for every classification row;
- forbidden-expansion register;
- citation rule for future work orders;
- change protocol requiring fresh GC-018 and rebuttal for reclassification.

HN2.b must close and lock the owner map before HN2.c GC-018 is filed.

---

## Claim Boundary

This rebuttal may be cited as:

> HN2.b is acceptable for later GC-018-gated owner-map authoring after class
> precedence and parallel sub-surface handling were clarified.

This rebuttal must not be cited as:

> The owner map exists, the governance kernel is coherent, the freeze is
> lifted, or runtime/kernel behavior has changed.

