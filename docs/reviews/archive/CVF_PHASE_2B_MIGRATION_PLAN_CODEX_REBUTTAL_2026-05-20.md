# CVF Phase 2.B Migration Plan Codex Rebuttal

Memory class: FULL_RECORD

Status: REBUTTAL_FILED_NON_BLOCKING_WITH_BOUNDARY_REFINEMENT

docType: review

Reviewer: Codex

Date: 2026-05-20

---

## Purpose

Review the Phase 2.B migration plan roadmap and decide whether it may proceed
later to its own GC-018 and implementation work order after HN2.b and HN2.c
close.

This is a rebuttal-only packet. It authorizes no migration plan artifact, no
GC-018, no adapter implementation, no 46-surface enumeration, no freeze lift,
no public-sync work, and no runtime coherence claim.

---

## Scope / Target / Owner Boundary

In scope:

- `docs/roadmaps/CVF_PHASE_2B_MIGRATION_PLAN_ROADMAP_2026-05-20.md`
- `docs/work_orders/CVF_WO_PHASE_2B_MIGRATION_PLAN_REBUTTAL_2026-05-20.md`
- HN2.b and HN2.c roadmap prerequisite framing
- HN2.a inventory
- selected Phase 2.B/Phase 1.x evidence files
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/skill-registry.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/full-skill-registry.ts`

Out of scope:

- producing `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_*.md`;
- listing the 46 surfaces;
- implementing any adapter;
- filing Phase 2.B GC-018;
- planning Phase 2.C or later.

---

## Target / Source Under Review

Queue item:

- `phase-2b-migration-plan-roadmap`

Expected response path:

- `docs/reviews/CVF_PHASE_2B_MIGRATION_PLAN_CODEX_REBUTTAL_2026-05-20.md`

Roadmap under review:

- `docs/roadmaps/CVF_PHASE_2B_MIGRATION_PLAN_ROADMAP_2026-05-20.md`

---

## Scope / Methodology

Method:

1. Confirmed the active queue item is `READY_FOR_REBUTTAL`.
2. Verified the roadmap requires HN2.b LOCKED before Phase 2.B GC-018.
3. Verified the roadmap requires HN2.c BINDING before kernel-touching adapter
   work can start.
4. Checked the four-input schema: order, owner, done, dependency.
5. Checked tiered done criteria, DAG/no-cycle requirement, per-surface work
   order model, and bulk-migration prohibition.
6. Reviewed Phase 2.B prior evidence:
   `CVF_17_05_PHASE_2B_PREFLIGHT_OWNER_MIGRATION_PLAN_2026-05-18.md`,
   `CVF_17_05_PHASE_2B_LEGACY_ABSORPTION_AUDIT_2026-05-18.md`, and
   `CVF_17_05_PHASE_2B_BOUNDED_WIREUP_COMPLETION_2026-05-18.md`.
7. Patched the roadmap/work order to clarify that bounded fixture-driven Phase
   2.B already delivered and this roadmap covers remaining broader migration
   planning only.

No live governance proof was run. This review is static.

---

## Findings / Position

Position: **NON_BLOCKING_WITH_BOUNDARY_REFINEMENT**.

Findings:

1. The roadmap is acceptable only as a remaining Phase 2.B migration-plan
   schema. It must not be read as reopening or negating the already delivered
   bounded fixture-driven Phase 2.B slice.
2. The four inputs are appropriate and separable: migration order, owner
   assignment, done criterion, and dependency graph.
3. The tiered done criteria are appropriately stricter for runtime and
   kernel-touching adapters. Kernel-touching work must cite an HN2.c-compliant
   freeze release.
4. The roadmap correctly forbids bulk migration and requires per-surface slice
   work orders after the migration plan is locked.
5. The roadmap correctly does not enumerate all 46 surfaces. Enumeration
   belongs to the later Phase 2.B GC-018 and plan artifact.
6. Prior evidence supports the boundary: the 2026-05-18 bounded Phase 2.B
   completion proved a fixture-driven contract chain only; the gap ledger still
   blocks broader Phase 2.B-style runtime expansion without a new GC-018.

---

## Risk / Defect / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Roadmap appears to reopen already delivered bounded Phase 2.B | Patched wording: this is remaining broader migration planning |
| Phase 2.B starts before HN2.b/HN2.c settle | HN2.b LOCKED and HN2.c BINDING remain hard prerequisites |
| Migration plan becomes bulk implementation | Plan only defines order/owner/done/dependency; per-surface work orders come later |
| 46-surface enumeration happens in rebuttal | Rebuttal and roadmap do not enumerate; later GC-018 owns enumeration |
| Kernel-touching work bypasses freeze release | Done criterion requires HN2.c-compliant release citation |

---

## Decision / Recommendation / Disposition

Disposition: **NON_BLOCKING_WITH_BOUNDARY_REFINEMENT**.

Phase 2.B may proceed later only after:

1. HN2.b owner map is locked.
2. HN2.c freeze-release rule is binding.
3. A Phase 2.B-specific GC-018 is filed for the migration plan artifact.
4. That GC-018 requires a four-input schema, per-surface table, tiered done
   criteria, stage gates, DAG verification, freeze-release callouts, citation
   rule, and bulk-migration prohibition.

Per-surface adapter implementation remains downstream of the locked migration
plan and each surface's own work order.

---

## Claim Boundary

This rebuttal may be cited as:

> The remaining Phase 2.B migration-plan roadmap is acceptable for later
> GC-018-gated planning after HN2.b and HN2.c close, with bulk migration
> forbidden.

This rebuttal must not be cited as:

> Phase 2.B runtime work is authorized, the 46 surfaces are enumerated, adapter
> implementation may begin, or CVF has a broad runtime coherence proof.

