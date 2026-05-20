# CVF Post-Residual-Closure Next Roadmap

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL — Claude (Orchestrator) proposes three candidate
tranches as the next work after all six Review-CVF residual work orders
(A1/C1/D1/E1/G1/H1) closed at commit `e3536795` on 2026-05-20.

docType: roadmap

Reviewer / Worker: Claude (Orchestrator role) authoring; Codex (Reviewer role)
expected to rebut before any candidate proceeds to GC-018 or work order
dispatch.

Date: 2026-05-20

Predecessor:

- `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`
  (AUTHORITATIVE direction: A–H all CLOSED; new work must be product expansion
  or fresh roadmap, not residual closure)
- `docs/reviews/CVF_17_05_REVIEW_CVF_RESIDUAL_PAIN_POINTS_ASSESSMENT_2026-05-19.md`
- `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md`
- `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` (3 items pending)

---

## Purpose

Pick the next governance tranche now that A–H residual closure is complete.

The 2026-05-20 closure tranche shipped concrete deliverables (5 CLI verbs, 3
benchmark metrics, an 11-role catalog, a memory tier classifier contract,
plus two explicit rejections). It did NOT do three things that are now due:

1. Update the **public technical catalog** (GC-024 BINDING rule) for the new
   capabilities now in the governance repo.
2. Process the **workflow-chain governance V2 roadmap** (priority 1 in the
   active review queue, READY_FOR_REBUTTAL since 2026-05-19).
3. File a roadmap for the **skill corpus dead-reference repair** that has
   been listed as pending since the post-Lane-G repair tranche.

This file proposes three candidate tranches — N1, N2, N3 — and submits them
for Codex rebuttal. Operator selects one or more after rebuttal returns
no-blocking.

This roadmap does NOT authorize implementation, does NOT file any GC-018,
and does NOT modify any public claim.

---

## Scope / Target / Owner Boundary

In scope:

- Three candidate tranches with explicit scope, evidence anchor, blocking
  classification, and forbidden expansion.
- A recommended execution sequence with reasoning.
- The exact GC-018 obligation per candidate (required / optional / none).

Out of scope:

- Reopening any A–H pain point (direction codex 2026-05-20 forbids this).
- New runtime semantics outside scoped candidate boundaries.
- Public claim expansion before public-sync catalog update.
- Implementation. Implementation requires a candidate-specific GC-018
  authorization and a dispatched work order.

Owner:

- Claude (Orchestrator) authors this roadmap.
- Codex (Reviewer) rebuts.
- Operator selects which candidates proceed and in which order.
- Worker (Codex-as-implementer) executes only after GC-018 + work order.

---

## Candidate Tranches

### N1 — Public-Sync Catalog Update (GC-024 BINDING)

Intent: **bounded-expansion of catalog only, no new code**.

Predecessor evidence:

- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` (governance
  repo copy; public-sync copy is the authoritative public catalog)
- Closure reviews at `docs/reviews/CVF_{A1,C1,D1,E1,G1,H1}_*_CLOSURE_REVIEW_2026-05-20.md`
- GC-024 BINDING rule in `CLAUDE.md` ("Every agent that delivers a new
  capability tranche must update the public technical catalog before closing
  the tranche")

In scope:

- Add new capability rows to the public catalog for:
  - 5 read-only CLI verbs (`run`, `skill`, `receipt`, `trace`, `provider`)
  - 3 new offline benchmark metrics (`humanCorrectionRate`,
    `longHorizonStabilityRate`, `rollbackSuccessRate`)
  - 11-role canonical agent role catalog
  - Memory tier classifier contract (7 tiers, reference-only)
- Update the Delivery History Summary (R3 section) with the 2026-05-20
  closure tranche.
- Verify every new path with `Test-Path` from the public-sync clone before
  commit (the N-1 failure mode).
- Sync catalog + necessary public-safe artifacts to the public-sync repo.

Out of scope:

- New code, new tests, new policy.
- Copying internal artifacts that are blocked by public-sync `.gitignore`
  (handoffs, baselines, reviews, roadmaps).
- Changing the verdict / scope of any 2026-05-20 closure review.

GC-018 obligation: **No.** This is catalog maintenance under an existing
binding rule (GC-024). A Fast-Lane audit is sufficient.

Forbidden expansion:

- Re-opening any A–H pain point.
- Claiming runtime memory wiring (H1 was contract-only).
- Claiming live governance proof beyond closure review wording.

Blocking classification proposal: **NON_BLOCKING** (catalog maintenance under
existing rule).

Evidence anchor after closure:

- Updated public catalog at `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
  in the public-sync repo.
- A fast-lane audit at `docs/audits/CVF_FAST_LANE_N1_PUBLIC_CATALOG_UPDATE_<date>.md`.

### N2 — Workflow-Chain Governance V2 Reviewer Rebuttal Cycle

Intent: **process the priority-1 review queue item before any other roadmap
work**.

Predecessor evidence:

- `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md`
  (READY_FOR_REBUTTAL since 2026-05-19)
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` — priority 1 item
  `workflow-chain-governance-v2`
- `docs/reviews/CVF_WORKFLOW_CHAIN_GOVERNANCE_PROPOSAL_REVIEWER_REBUTTAL_2026-05-19.md`
  (rebuttal on the V1 proposal that triggered V2)

In scope:

- Dispatch Codex as Reviewer to file the second-round rebuttal on V2 at
  `docs/reviews/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_CODEX_REBUTTAL_2026-05-19.md`.
- After rebuttal returns, update the queue item's `status` and
  `responsePath`.
- If no-blocking verdict: dispatch GC-018 + work order per accepted candidate
  in the V2 roadmap.
- If blocking verdict: file V3 or close V2 as superseded.

Out of scope:

- Implementing V2 candidates before rebuttal returns.
- Changing the V2 roadmap content (V2 is itself the artifact under review).

GC-018 obligation: **Per-candidate inside V2** (this tranche only processes
the rebuttal cycle; downstream GC-018s come after rebuttal).

Forbidden expansion:

- Reopening V1 proposal.
- Adding new workflow-chain candidates outside V2.

Blocking classification proposal: **NON_BLOCKING for the rebuttal step**;
downstream candidates may have their own blocking findings inside V2.

Evidence anchor after closure:

- Filed rebuttal at the expected response path.
- Updated queue item status.

### N3 — Skill Corpus Dead-Reference Repair Roadmap

Intent: **file a fresh roadmap, NOT skip straight to a work order**.

Predecessor evidence:

- `CVF_SESSION_MEMORY.md` pending list (`Skill corpus dead-reference repair —
  needs a fresh work order; do not start without one`)
- Skill corpus paths under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json`
  and the skill discovery code that indexes it
- Prior repair commit `e28c5464` noted skill corpus test paths were already
  fixed once; this candidate addresses residual dead references not covered
  there

In scope (for the roadmap, NOT the implementation):

- Inventory dead references in the skill index and skill discovery surfaces.
- Distinguish between (a) genuinely dead pointers, (b) renamed targets, (c)
  intentionally missing entries.
- Propose a per-class repair strategy with named owner files.
- Cite which guards currently fail (or only advise) on each class.

Out of scope:

- Skill corpus repair implementation in this tranche. Implementation requires
  a separate Codex rebuttal of THIS roadmap, then GC-018, then a work order.
- New skill discovery semantics.
- Auth / RBAC changes.

GC-018 obligation: **No for the roadmap; Yes for the downstream
implementation work order** (skill corpus repair will touch governed data
under cvf-web public data).

Forbidden expansion:

- Mass renaming or migration outside the dead-reference inventory.
- New skill categories.
- Public-sync sync of skill changes before catalog update.

Blocking classification proposal: **NON_BLOCKING for the roadmap itself**;
implementation downstream is gated by rebuttal + GC-018.

Evidence anchor after closure:

- Filed inventory and repair-strategy roadmap at
  `docs/roadmaps/CVF_SKILL_CORPUS_REPAIR_ROADMAP_<date>.md`.

---

## Non-Goals

- Reopening any A–H Review-CVF pain point. Direction codex 2026-05-20 marks
  them all CLOSED.
- Implementing any candidate in this tranche. This roadmap is a planning
  artifact only; downstream gates (rebuttal, GC-018, work order) apply.
- Bundling N1, N2, and N3 into one work order or commit.
- Public claim changes beyond what the public catalog update (N1) and the
  closure reviews already permit.
- Touching `llm.adapter.interface.ts` or any other file in the blocked work
  classes recorded in `CVF_SESSION/ACTIVE_SESSION_STATE.json`.

---

## Work Plan

Each candidate is its own tranche. The work plan below lists per-candidate
steps from rebuttal through closure.

### N1 work plan

1. Codex Reviewer files rebuttal at the expected response path.
2. If no-blocking: file fast-lane audit under `docs/audits/` citing GC-024
   BINDING rule.
3. Update public catalog rows in the public-sync clone (governance-repo copy
   is convenience only).
4. Run `Test-Path` on every new evidence path from the public-sync clone.
5. Commit catalog update to public-sync; do not touch governance-repo runtime
   files in this tranche.
6. File closure review.

### N2 work plan

1. Codex Reviewer files V2 rebuttal at the expected response path.
2. Update queue item `status` and `responsePath`.
3. If no-blocking per candidate inside V2: file GC-018 per candidate, then
   dispatch the candidate's work order.
4. If blocking: either file V3 or close V2 as superseded.
5. Closure review for the rebuttal step itself (not for downstream V2
   candidates — each has its own closure).

### N3 work plan

1. Codex Reviewer files rebuttal on this roadmap (N3 section).
2. If no-blocking: author the skill corpus repair roadmap (filed under
   `docs/roadmaps/CVF_SKILL_CORPUS_REPAIR_ROADMAP_<date>.md`).
3. Hold for second rebuttal on the new roadmap.
4. After second no-blocking, file GC-018 for the implementation tranche.
5. Implementation runs only after GC-018 + work order dispatch.

---

## Acceptance Criteria

For this roadmap to be considered CLOSED:

- [ ] Codex Reviewer rebuttal filed at the expected response path with a
      per-candidate verdict (N1, N2, N3) of BLOCKING / NON_BLOCKING /
      NON_BLOCKING_WITH_GATE_UPDATE.
- [ ] Active review queue item `post-residual-closure-next-roadmap` updated
      to reflect the rebuttal disposition.
- [ ] Operator selects which candidates proceed.
- [ ] Each selected candidate carries its own downstream artifacts (fast-lane
      audit, GC-018, work order, closure review) as required by its work
      plan.
- [ ] No A–H pain-point reopen and no blocked work class violation appears
      in any downstream artifact.

For each candidate to be considered CLOSED (after this roadmap clears):

- N1 CLOSED when: public catalog reflects the new capabilities; fast-lane
  audit filed; `Test-Path` verification recorded.
- N2 CLOSED when: V2 rebuttal filed; queue item updated; if no-blocking,
  downstream GC-018 chain begins.
- N3 CLOSED when: the new skill corpus repair roadmap is filed under
  `docs/roadmaps/`; no implementation has begun.

---

## Execution Sequence (Recommended)

Proposed order:

1. **N1 first** — catalog update is overdue under GC-024 BINDING and closes
   the 2026-05-20 tranche cleanly. Catalog maintenance does not block on
   rebuttal.
2. **N2 second** — process priority-1 review queue item. The queue item has
   been pending since 2026-05-19; the closure tranche introduced no conflict
   with V2.
3. **N3 third** — file fresh skill corpus repair roadmap. This is the least
   urgent of the three because dead references are advisory-only in current
   guard chain.

Rationale:

- N1 has the strongest existing obligation (BINDING rule, catalog already
  out of date).
- N2 has the strongest queue precedent (priority 1, READY_FOR_REBUTTAL flag
  set ten days ago).
- N3 is genuinely new and should not jump the queue over an existing pending
  item.

Operator may select any subset and any order; the rebuttal flow does not
constrain which candidate runs first as long as each clears its own gate.

---

## Forbidden Maintenance Pattern

When this roadmap is rebutted:

- Do not silently accept all three. Force per-candidate verdict.
- Do not promote any candidate to GC-018 without a no-blocking verdict on
  that specific candidate.
- Do not bundle N1 + N2 + N3 into a single work order. Each is a separate
  tranche.
- Do not reopen A–H pain-point work under cover of N1/N2/N3. Direction codex
  forbids this.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Catalog update is treated as cosmetic and skipped | N1 cites GC-024 BINDING; rebuttal must confirm rule applies |
| V2 rebuttal is delayed indefinitely | N2 is explicitly scoped to the rebuttal step only |
| Skill corpus repair jumps to implementation without roadmap | N3 is roadmap-only by design; implementation needs a downstream tranche |
| Operator picks all three at once | Each candidate has its own gate; concurrent execution is allowed but each closes independently |
| Catalog update overclaims new capability | N1 forbidden expansion list rules out runtime memory wiring, live governance proof, and pain-point reopen |

---

## Decision / Recommendation / Disposition

Disposition: READY_FOR_REBUTTAL.

Recommended operator move after rebuttal:

- Treat N1 as the default first tranche (catalog hygiene under existing
  BINDING rule, no GC-018).
- Schedule N2 immediately after N1 to clear priority-1 queue item.
- Hold N3 until N1 and N2 settle, then file the inventory roadmap.

If Codex returns blocking findings on any candidate, do not dispatch that
candidate's downstream work until corrected.

---

## Verification

Static verification only (this is a planning artifact):

- The three candidates do not overlap with the closed 2026-05-20 tranche.
- The three candidates do not reopen any A–H pain point.
- The three candidates respect blocked work classes from
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Each candidate has a named predecessor, evidence anchor, and blocking
  classification proposal.

No tests, live provider calls, or release gates are required to file this
roadmap.

---

## Related Artifacts

- `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`
- `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md`
- `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md`
- `docs/roadmaps/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## Claim Boundary

This roadmap claims only a proposed next-tranche selection ready for Codex
rebuttal. It does not claim implementation authorization, GC-018
authorization, release readiness, live governance proof, or public catalog
update completion. Each candidate must clear its own rebuttal and gate
before any downstream work begins.
