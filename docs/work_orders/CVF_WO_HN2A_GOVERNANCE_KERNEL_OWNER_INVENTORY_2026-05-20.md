# Work Order — HN2.a: Governance Kernel Owner Inventory (Fast-Lane)

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Worker role: Codex (Orchestrator-author role)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md` (HN2 framing)
- `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md` (Claude verdict on HN2: NON_BLOCKING_WITH_SPLIT — split into HN2.a inventory / HN2.b owner map / HN2.c freeze-release rule)
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` (`freezePosture: governance_kernel_freeze_recommended`)

Authority chain: Claude rebuttal on HN2 required a 3-way split. HN2.a is
the first sub-tranche — observation only, no classification, no policy
making. No GC-018 is required for HN2.a; downstream HN2.b and HN2.c each
require their own GC-018.

---

## Purpose

Produce a precise inventory of the CVF governance kernel surfaces and
their current ownership claim, as a static observation artifact, so that
the downstream HN2.b owner map and HN2.c freeze-release rule can be
classified and policy-codified without label-shifting between
observation, classification, and rule-making.

This work order produces a single inventory artifact. It does NOT assign
classifications, does NOT propose policy, and does NOT change any
runtime, guard, or doctrine file.

---

## Scope / Target / Owner Boundary

In scope:

- For each kernel surface listed below, identify and record the current
  canonical-owner candidate file path (if any), every legacy alias file
  path observed, and any ambiguity note.
- Kernel surfaces to inventory (exhaustive list, do not add):
  1. Authority model (who decides what)
  2. Role model (role IDs + allowed_outputs)
  3. Policy decision surface
  4. Risk model
  5. Guard model
  6. Execution lifecycle
  7. Delegation / handoff
  8. Receipt envelope
  9. Memory tier model
  10. Capability surface
  11. Provider execution semantics
  12. Vocabulary aliases (term-drift surface)
- Output: one inventory artifact at
  `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`.

Out of scope (forbidden):

- Assigning any class (`canonical_owner`, `adapter_required`,
  `legacy_alias`, `deferred`, `rejected`) to any surface. That is HN2.b.
- Codifying any policy text (e.g., freeze-release rule). That is HN2.c.
- Renaming any file or term.
- Modifying any guard, doctrine, registry, runtime, or policy file.
- Filing GC-018.
- Public claim updates.
- Reopening any A–H Review-CVF pain point.
- Touching the public-sync repo.

Owner boundary:

- This work order touches the governance repo only and creates exactly
  one new file (the inventory artifact) plus the standard
  session-state/handoff sync edits.

---

## Per-Surface Required Fields (must appear for each of the 12 surfaces)

| Field | Meaning |
| --- | --- |
| `surfaceName` | The kernel surface name (from the 12-item list above) |
| `currentCanonicalOwnerCandidate` | Single best-current-owner file path, or `owner_gap` if none clearly exists |
| `legacyAliasesObserved` | List of additional file paths that currently carry overlapping authority claims (may be empty) |
| `termsObserved` | List of terms used across docs/code that refer to this surface (may be empty) |
| `ambiguityNote` | One short sentence describing any ambiguity, OR `none observed` |
| `evidencePaths` | At least one concrete file path that grounds the entry |

The inventory must NOT include:

- A class column (`canonical_owner` / `adapter_required` / etc.).
- A policy verdict.
- A "should be" claim.

Observation only.

---

## Deliverables

### Step HN2a.1 — Source Read

Read in this order before authoring:

1. `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`
2. `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`
3. `governance/toolkit/05_OPERATION/` directory listing (read filenames; do
   not modify any file).
4. `ECOSYSTEM/doctrine/` directory listing (read filenames; FROZEN, do
   not modify).
5. `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` (if present).
6. `docs/CVF_ARCHITECTURE_DECISIONS.md`.
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts` (role model evidence).
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/*/execution.policy.json` (policy decision evidence).
9. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts` (memory tier evidence; H1 closed).
10. `EXTENSIONS/CVF_MODEL_GATEWAY/src/` directory listing (provider semantics evidence).
11. `docs/reference/CVF_AGENT_ROLE_CATALOG.md` (G1 absorbed role catalog).

### Step HN2a.2 — Inventory Authoring

File path: `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`

Required structure:

- Frontmatter: `Memory class: FULL_RECORD`, `Status: INVENTORY_FILED`,
  `docType: review`, `Reviewer: Codex (Orchestrator-author)`,
  `Date: 2026-05-20`.
- `## Purpose`
- `## Scope / Target / Owner Boundary`
- `## Source / Target` (predecessor list)
- `## Scope / Methodology`
- `## Findings / Position` — observation only; no class, no policy.
- `## Per-Surface Inventory Table` (the 12-row table; every row has every
  required field filled or explicitly `owner_gap` / `none observed`).
- `## Risk / Corrective Action` — risks that downstream HN2.b/HN2.c will
  inherit if not corrected (e.g., term drift, owner_gap entries).
- `## Decision / Disposition` — INVENTORY_ONLY; no implementation
  authority claimed.
- `## Claim Boundary`.

The Per-Surface Inventory Table must use exactly this column order:

| surfaceName | currentCanonicalOwnerCandidate | legacyAliasesObserved | termsObserved | ambiguityNote | evidencePaths |
| --- | --- | --- | --- | --- | --- |

Each cell value must be a literal string (or comma-separated list);
do not embed JSON, links, or markdown headings inside cells.

If a surface has no clear canonical owner: set
`currentCanonicalOwnerCandidate` to `owner_gap` and note in
`ambiguityNote`.

### Step HN2a.3 — Closure Review

File path: `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_CLOSURE_REVIEW_2026-05-20.md`

Required structure: Purpose, Target, Scope/Methodology, Findings,
Decision/Disposition, Claim Boundary.

The closure review must confirm:

- All 12 surfaces present in inventory.
- Every row has all required fields filled.
- No row contains a class assignment or policy verdict.
- No code/guard/policy/registry/runtime file modified.
- No GC-018 filed.
- No public-sync push.
- Pre-commit and pre-push hooks PASS.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [ ] Inventory artifact filed at
      `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
      with all required structural sections.
- [ ] Per-Surface Inventory Table has exactly 12 rows (one per surface
      from the fixed list).
- [ ] Every row has all six required fields filled.
- [ ] No row contains a class assignment, policy verdict, or "should be"
      claim.
- [ ] No guard / runtime / doctrine / registry / policy file modified.
- [ ] No GC-018 filed.
- [ ] No public-sync push.
- [ ] No A–H pain-point reopen.
- [ ] Closure review filed at
      `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_CLOSURE_REVIEW_2026-05-20.md`.
- [ ] Pre-commit hook PASS (11/11).
- [ ] Pre-push hook PASS (43/43).
- [ ] Handoff GC-020 HEAD SHA synced after closure commit.

---

## Forbidden Actions

- Do NOT assign any class to any surface.
- Do NOT propose any freeze-release rule.
- Do NOT modify any guard / runtime / doctrine / registry / policy file.
- Do NOT add or remove any role ID.
- Do NOT touch any memory tier file (H1 closed; out of scope).
- Do NOT touch any provider execution file.
- Do NOT touch the public-sync repo.
- Do NOT file GC-018.
- Do NOT bundle HN1 or HN3 work into this tranche.
- Do NOT use `git add -A` or `git add .`.
- Do NOT reopen any A–H Review-CVF pain point.

---

## Authority Chain

- Authorized by: Claude rebuttal verdict NON_BLOCKING_WITH_SPLIT on HN2,
  with HN2.a explicitly framed as inventory-only and Fast-Lane gated.
- Predecessor roadmap:
  `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`.
- Orchestrator: Claude; Worker: Codex (Orchestrator-author role).
- Operator approval not required for inventory-only filing.

---

## Agent Roles

- Worker (Codex Orchestrator-author): source reading, inventory authoring,
  closure review.
- Orchestrator (Claude): reviews closure review; if inventory is sound,
  dispatches HN2.b (owner map) as a separate GC-018-gated tranche.

---

## Required First Reads

1. `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md` —
   HN2 split rationale.
2. `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md` —
   HN2 framing.
3. The two private 17.05 freeze documents listed in Step HN2a.1.
4. `governance/toolkit/05_OPERATION/` directory listing.
5. `ECOSYSTEM/doctrine/` directory listing (FROZEN; read-only).
6. `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md` —
   review structural template.

---

## Pre-Flight Checks

- [ ] Governance repo working tree CLEAN before starting.
- [ ] Confirm inventory artifact path does NOT yet exist.
- [ ] Confirm closure review path does NOT yet exist.
- [ ] Read the 12-surface list once before drafting any row.

---

## Write Ownership

May create only:

- `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md` (new)
- `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_CLOSURE_REVIEW_2026-05-20.md` (new)

May modify only:

- `docs/work_orders/CVF_WO_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
  (status/checklist closure sync only)
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` (queue item update after closure)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` (nextAllowedMove update after
  closure)
- `AGENT_HANDOFF_V10_2026-05-19.md` (status line + GC-020 HEAD SHA sync)

No other files may be created or modified.

---

## Execution Plan

1. Pre-flight checks.
2. Source read (Step HN2a.1).
3. Inventory authoring (Step HN2a.2).
4. Closure review (Step HN2a.3).
5. Session state + handoff sync.
6. Commit + GC-020 sync.

---

## Evidence Requirements

- All 12 surface rows complete, each with at least one concrete
  `evidencePaths` entry.
- Closure review cites inventory artifact path + commit SHA.
- `git diff` confirms only the two new docs + session-state + handoff +
  queue changed.

---

## Review Gate

Stop and return to Orchestrator if:

- More than 12 distinct kernel surfaces are observed (suggests the list
  is incomplete; Operator must approve list expansion before continuing).
- Any surface requires classification to be observable (suggests HN2.b
  scope leak into HN2.a).
- Inventory cannot be filed without modifying a guard/policy/runtime
  file (suggests Operator's intent is HN2.b or HN2.c, not HN2.a).
- A surface's `currentCanonicalOwnerCandidate` would need to be
  invented; mark `owner_gap` and continue, unless multiple owner gaps
  appear in the same surface, in which case stop and report.

---

## Non-Goals

- HN2.b owner map authoring.
- HN2.c freeze-release rule codification.
- HN1 template-linkage work.
- HN3 runtime maturity work.
- Filing GC-018.
- Public claim updates.
- Reopening any A–H Review-CVF pain point.

---

## Work Plan

Sequential:

1. Pre-flight checks.
2. Source read.
3. Author inventory.
4. File closure review.
5. Session-state + handoff sync.
6. Commit using HEREDOC commit message; do not amend.

If any review-gate condition fires, stop and report to Orchestrator
before proceeding.

---

## Closure Checklist

- [ ] 12-surface inventory present and complete.
- [ ] No class / policy / "should be" content in any row.
- [ ] Closure review filed.
- [ ] No `.ts` / `.py` / `.json` modified outside session-state/queue.
- [ ] No GC-018.
- [ ] No public-sync push.
- [ ] Session-state + handoff + queue updated.
- [ ] Pre-commit + pre-push hooks PASS.

---

## Return-To-Orchestrator Conditions

Return if:

- More than 12 kernel surfaces observed.
- Surface cannot be inventoried without classification.
- Inventory requires modifying guard/policy/runtime file.
- Markdown structural completeness hook blocks the inventory and fix
  requires content not derivable from source.
- Hook failure outside this scope.

---

## Claim Boundary

This work order produces a single inventory artifact for governance kernel
surfaces. It does not authorize new code, new tests, new policy, new
GC-018, downstream work orders, runtime changes, ownership classification,
freeze-release rule codification, or any public claim. The downstream
HN2.b owner map and HN2.c freeze-release rule each require their own
GC-018 and separate work order. This work order does not reopen any A–H
Review-CVF pain point.
