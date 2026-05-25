# Work Order — N1: Public-Sync Catalog Update (GC-024 BINDING)

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Worker role: Codex (Implementer)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_2026-05-20.md` (REBUTTAL_FILED_NON_BLOCKING_WITH_GATE_UPDATE)
- `docs/reviews/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_CODEX_REBUTTAL_2026-05-20.md` (Codex verdict on N1: NON_BLOCKING_WITH_PUBLIC_BOUNDARY)
- `CLAUDE.md` (GC-024 BINDING rule: "Every agent that delivers a new capability tranche must update the public technical catalog before closing the tranche")
- 2026-05-20 closure reviews at `docs/reviews/CVF_{A1,C1,D1,E1,G1,H1}_*_CLOSURE_REVIEW_2026-05-20.md`

Authority chain: Codex rebuttal accepted N1 as public-safe catalog
maintenance under GC-024/Fast-Lane only. No fresh GC-018 is required.

---

## Purpose

Update the public technical product catalog in the public-sync repository
to reflect the four new public-safe surfaces delivered by the 2026-05-20
residual closure tranche, so that the public-facing catalog matches the
public code subset already shipped.

This work order is documentation/catalog maintenance only. It does not
deliver new code, new tests, or new governance semantics.

---

## Scope / Target / Owner Boundary

In scope:

- Update `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` in the
  public-sync repository at
  `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`.
- Add catalog rows for the four public-safe surfaces (per Codex rebuttal N1
  accepted scope):
  1. Five read-only CLI verbs (`run`, `skill`, `receipt`, `trace`,
     `provider`) — source `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
  2. Three new offline benchmark metrics (`humanCorrectionRate`,
     `longHorizonStabilityRate`, `rollbackSuccessRate`) — source
     `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
  3. Canonical 11-role agent role catalog — source
     `docs/reference/CVF_AGENT_ROLE_CATALOG.md` only if this path exists in
     the public-sync repo. If it is missing, record a public-sync coverage gap
     in the audit packet and do not add a catalog row.
  4. Memory tier classifier contract — source
     `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`,
     limited to contract surface and offline/unit verification claim
- Update the Delivery History Summary (R3 section) with a one-paragraph
  entry citing the 2026-05-20 closure tranche.
- File a Fast-Lane audit packet under `docs/audits/` (in the public-sync
  repo) per GC-024 BINDING rule.
- Verify every new evidence path with `Test-Path` from the public-sync
  clone before any commit.

Out of scope (forbidden per Codex rebuttal):

- Copying provenance docs, review packets, GC-018 baselines, work orders,
  handoffs, private evidence records, or internal closure reviews into the
  public-sync repository.
- New code, new tests, new policy in any repository.
- Claiming fresh live governance proof, new runtime behavior, or expanded
  governance semantics.
- Reopening any A–H Review-CVF pain point.
- Modifying the public-sync `.gitignore` rules that block internal artifact
  classes.

Owner boundary:

- This work order touches only the public-sync repo (`Blackbird081/Controlled-Vibe-Framework-CVF`)
  for catalog + audit.
- The governance repo (this repo) is read-only source-of-truth for evidence
  paths during catalog updates.

---

## Deliverables

### Step N1.1 — Public-Safe Evidence Path Inventory

Before any catalog edit, produce an inventory of public-safe evidence paths.

Author the inventory at the top of the Fast-Lane audit packet (Step N1.4)
as a table:

| Surface | Public-safe evidence path | Verified by Test-Path? |
|---|---|---|
| CLI verbs | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` | yes/no |
| CLI verb tests | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/commands/cvf-*.test.ts` (5 files) | yes/no |
| Benchmark metrics | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts` | yes/no |
| Benchmark metric tests | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/governance-reliability-metrics.test.ts` | yes/no |
| Role catalog | `docs/reference/CVF_AGENT_ROLE_CATALOG.md` | yes/no |
| Memory tier classifier | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts` | yes/no |
| Memory tier classifier tests | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-tier-classifier.test.ts` | yes/no |

Run `Test-Path` from the **public-sync clone**, not the governance repo.

If any path is missing from the public-sync clone:

- The corresponding catalog row must NOT be added (per Codex rebuttal: catalog
  must reflect already-landed public code, not aspirational claims).
- Record the gap in the audit packet under "Public-sync coverage gaps".

### Step N1.2 — Public-Sync Repository Verification

Before any commit, the Worker must:

1. `cd` to the public-sync clone.
2. Run `git remote -v` and confirm the remote is
   `Blackbird081/Controlled-Vibe-Framework-CVF` (NOT the provenance
   repository).
3. Run `git status` to confirm a clean working tree before starting.
4. Record both checks in the audit packet under "Pre-flight verification".

### Step N1.3 — Catalog Row Authoring

Update `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` in the
public-sync clone:

- Add capability rows for each surface in the inventory whose Test-Path
  returned PASS.
- For each row, fill: surface name, catalog-vocabulary status, evidence path,
  one-line plain-language description.
- Do NOT force `proven` for offline/read-only/schema-only surfaces. Use the
  existing public catalog status vocabulary (`active`, `schema-defined`, etc.)
  so the catalog does not imply fresh live governance proof.
- Update the Delivery History Summary (R3 section) with a one-paragraph
  entry citing the 2026-05-20 residual closure tranche, without naming
  internal artifact classes.
- Do NOT add catalog rows for any surface whose evidence path is missing in
  the public-sync clone.

Permitted catalog text style:

- Plain-language. No internal artifact references (no "GC-018", no closure
  review paths, no work order IDs, no roadmap IDs).
- The phrase "2026-05-20 tranche" is acceptable; specific review/work-order
  paths are not.

### Step N1.4 — Fast-Lane Audit Packet

File: `docs/audits/CVF_FAST_LANE_N1_PUBLIC_CATALOG_UPDATE_2026-05-20.md`
(in the public-sync repo).

Required sections (per `docs/reference/CVF_FAST_LANE_AUDIT_TEMPLATE.md`):

- Purpose
- Source / Predecessor Evidence
- Scope (catalog rows added; surfaces excluded with reason)
- Public-Safe Evidence Path Inventory (the Step N1.1 table)
- Pre-flight Verification (the Step N1.2 results)
- Risk Classification (R0, documentation-only)
- Decision / Disposition
- Claim Boundary

The audit packet must explicitly cite GC-024 BINDING rule as the
authorization for skipping GC-018.

### Step N1.5 — Public-Sync Commit and Push

After audit packet is filed and catalog is updated:

1. `git add` only the catalog file and the audit packet. Do NOT use
   `git add -A` or `git add .`.
2. Verify `git status` shows only the two expected files staged.
3. Commit with a descriptive message citing the 2026-05-20 tranche and
   GC-024 BINDING rule.
4. Push to `origin/main` on the public-sync remote.
5. Do NOT push to the governance repo.

### Step N1.6 — Closure Review

File: `docs/reviews/CVF_N1_PUBLIC_SYNC_CATALOG_UPDATE_CLOSURE_REVIEW_2026-05-20.md`
(in the **governance repo** — closure reviews live in governance, not
public-sync, per public-sync `.gitignore`).

Required structure: Purpose, Target, Scope/Methodology, Findings,
Decision/Disposition, Claim Boundary.

The closure review must confirm:

- Public-sync remote verified as `Blackbird081/Controlled-Vibe-Framework-CVF`
  before push.
- Test-Path verification PASS for every catalog row added.
- No provenance/internal artifacts pushed to public-sync.
- Fast-Lane audit packet filed in public-sync repo.
- Public-sync commit landed on `origin/main`.
- Governance repo unchanged except for this closure review.
- Pre-commit and pre-push hooks PASS on the governance repo when filing
  this closure review.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [ ] Public-safe evidence path inventory completed; every catalog row added
      corresponds to a Test-Path PASS in the public-sync clone.
- [ ] `git remote -v` verification recorded in audit packet, showing
      `Blackbird081/Controlled-Vibe-Framework-CVF`.
- [ ] Catalog rows added for the four surfaces (or fewer if any path is
      missing in public-sync; gaps documented).
- [ ] Delivery History Summary updated with 2026-05-20 tranche entry.
- [ ] Fast-Lane audit packet filed in public-sync at
      `docs/audits/CVF_FAST_LANE_N1_PUBLIC_CATALOG_UPDATE_2026-05-20.md`.
- [ ] Public-sync commit landed on `Blackbird081/Controlled-Vibe-Framework-CVF`
      `origin/main`.
- [ ] No internal artifacts (handoffs, baselines, internal reviews,
      roadmaps, work orders, GC-018 baselines, provenance docs) committed
      to public-sync.
- [ ] Closure review filed in governance repo.
- [ ] Pre-commit and pre-push hooks PASS on governance repo for the closure
      review commit.

---

## Forbidden Actions

- Do NOT push to the governance repo as part of N1.
- Do NOT use `git add -A` or `git add .` in the public-sync repo.
- Do NOT copy any file from `docs/reviews/`, `docs/baselines/`,
  `docs/roadmaps/`, `docs/work_orders/`, or any handoff into the public-sync
  repo.
- Do NOT add catalog rows for surfaces whose evidence path is missing in
  the public-sync clone.
- Do NOT use `proven` unless the row is backed by the catalog's required live
  governance proof boundary.
- Do NOT claim fresh live governance proof, new runtime behavior, or
  expanded governance semantics in catalog text.
- Do NOT reopen any A–H Review-CVF pain point.
- Do NOT modify the public-sync `.gitignore`.
- Do NOT bundle N2 or N3 work into this tranche.

---

## Authority Chain

- Authorized by: Codex rebuttal verdict NON_BLOCKING_WITH_PUBLIC_BOUNDARY on
  N1 candidate, 2026-05-20
- Roadmap: `docs/roadmaps/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_2026-05-20.md`
  (REBUTTAL_FILED_NON_BLOCKING_WITH_GATE_UPDATE)
- Predecessor closure tranche: commit `e3536795` (6 residual work orders
  closed)
- Binding rule: GC-024 in `CLAUDE.md`
- Orchestrator: Claude; Worker: Codex; Operator approval not required for
  Fast-Lane catalog maintenance under GC-024

---

## Agent Roles

- Worker (Codex): inventory, public-sync verification, catalog edits, audit
  packet, public-sync commit/push, closure review
- Orchestrator (Claude): reviews closure review; verifies governance-repo
  hygiene after N1 closes

---

## Required First Reads

1. `docs/roadmaps/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_2026-05-20.md` —
   N1 scope and intended sequencing
2. `docs/reviews/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_CODEX_REBUTTAL_2026-05-20.md` —
   per-candidate verdict and N1 public boundary
3. `CLAUDE.md` Public-Sync Rule section + Public Catalog Update Rule (GC-024)
4. `docs/reference/CVF_FAST_LANE_AUDIT_TEMPLATE.md` — Fast-Lane audit
   packet structure
5. The 6 closure reviews at `docs/reviews/CVF_{A1,C1,D1,E1,G1,H1}_*_CLOSURE_REVIEW_2026-05-20.md`
   — plain-language summaries of what shipped (use these to draft catalog
   row descriptions)
6. The current public catalog at
   `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\docs\reference\CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
   — read before editing

---

## Pre-Flight Checks

- [ ] Confirm public-sync clone exists at expected path and `git remote -v`
      shows `Blackbird081/Controlled-Vibe-Framework-CVF`.
- [ ] Confirm public-sync clone working tree is CLEAN before starting.
- [ ] Confirm governance repo working tree is CLEAN before starting.
- [ ] Read the current public catalog so additive edits do not break
      existing rows or section ordering.

---

## Write Ownership

Public-sync repo, may create or modify only:

- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` (modify)
- `docs/audits/CVF_FAST_LANE_N1_PUBLIC_CATALOG_UPDATE_2026-05-20.md` (new)

Governance repo, may create only:

- `docs/reviews/CVF_N1_PUBLIC_SYNC_CATALOG_UPDATE_CLOSURE_REVIEW_2026-05-20.md` (new)

No other files may be created or modified in either repo.

---

## Execution Plan

1. Pre-flight checks (Step N1.1 inventory + Step N1.2 remote verification).
2. Authoring catalog rows in public-sync (Step N1.3).
3. Filing Fast-Lane audit packet in public-sync (Step N1.4).
4. Commit and push to public-sync `origin/main` (Step N1.5).
5. Filing closure review in governance repo (Step N1.6).

---

## Evidence Requirements

- Inventory table with Test-Path PASS for every added catalog row.
- `git remote -v` output recorded in audit packet.
- Public-sync commit SHA cited in closure review.
- Closure review path: `docs/reviews/CVF_N1_PUBLIC_SYNC_CATALOG_UPDATE_CLOSURE_REVIEW_2026-05-20.md`.

---

## Review Gate

Stop and return to Orchestrator if:

- Public-sync remote is NOT `Blackbird081/Controlled-Vibe-Framework-CVF`.
- More than one evidence path is missing in public-sync (suggests broader
  sync gap that needs its own roadmap, not a catalog patch).
- Catalog edit would require a status value outside the existing public catalog
  vocabulary.
- An internal artifact (handoff, baseline, internal review, roadmap, work
  order) would need to be copied into public-sync to make the catalog row
  meaningful.

---

## Non-Goals

- Implementing N2 (workflow-chain V2 rebuttal cycle).
- Implementing N3 (skill corpus repair roadmap).
- Updating the governance repo catalog (it is convenience-only; public-sync
  catalog is authoritative).
- Adding new capabilities to the public surface.
- Modifying any source code, test, or governance file.

---

## Work Plan

Sequential:

1. Run pre-flight checks (Section: Pre-Flight Checks).
2. Build evidence path inventory (Step N1.1).
3. Verify public-sync remote (Step N1.2).
4. Author catalog rows + delivery history update (Step N1.3).
5. File Fast-Lane audit packet (Step N1.4).
6. Commit + push public-sync (Step N1.5).
7. File closure review (Step N1.6).

If any review-gate condition fires, stop and return to Orchestrator before
proceeding to the next step.

---

## Closure Checklist

- [ ] Public-safe evidence path inventory recorded in audit packet.
- [ ] `git remote -v` verification recorded.
- [ ] Catalog rows added or updated with status values from the existing public
      catalog vocabulary for every included surface with Test-Path PASS.
- [ ] Delivery History Summary updated with 2026-05-20 tranche entry.
- [ ] Fast-Lane audit packet filed in public-sync.
- [ ] Public-sync commit landed on `Blackbird081/Controlled-Vibe-Framework-CVF`
      `origin/main` with commit SHA recorded.
- [ ] No internal artifacts copied to public-sync.
- [ ] Closure review filed in governance repo.
- [ ] Pre-commit and pre-push hooks PASS on governance repo.
- [ ] No A–H pain-point reopen and no blocked work class violation.

---

## Return-To-Orchestrator Conditions

Return if:

- Public-sync remote mismatch.
- Multiple evidence paths missing in public-sync.
- Catalog edit would require a status value outside the existing public
  catalog vocabulary.
- Internal artifact would need to be copied to satisfy a catalog row.
- Hook failure outside this scope.

---

## Claim Boundary

This work order covers public catalog row additions, a delivery history
paragraph, a Fast-Lane audit packet, public-sync commit and push, and a
governance-repo closure review only. It does not authorize new code, new
tests, new governance semantics, new public claims beyond catalog-row
alignment with already-landed public code, or any change to the governance
repo other than the closure review file.

This work order does not reopen any A–H Review-CVF pain point and does not
preempt N2 or N3 in the post-residual roadmap.
