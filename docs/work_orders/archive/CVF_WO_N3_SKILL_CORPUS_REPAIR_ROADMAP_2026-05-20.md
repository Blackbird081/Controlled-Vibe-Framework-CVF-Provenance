# Work Order — N3: Skill Corpus Dead-Reference Repair Roadmap (Filing Only)

Memory class: FULL_RECORD

Status: WITHDRAWN — see
`docs/reviews/CVF_N3_SKILL_CORPUS_REPAIR_WORK_ORDER_WITHDRAWAL_2026-05-20.md`.
Worker (Codex) correctly triggered the work order's own Review Gate
("Zero dead references found in skill index") during pre-flight. Audit
confirmed 27 skills / 0 dead / 0 orphans. Authoring premise was incorrect.
Do not re-execute this work order.

docType: work_order

Worker role: Codex (Orchestrator-author role)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_2026-05-20.md` (REBUTTAL_FILED_NON_BLOCKING_WITH_GATE_UPDATE)
- `docs/reviews/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_CODEX_REBUTTAL_2026-05-20.md` (Codex verdict on N3: NON_BLOCKING_AS_ROADMAP_ONLY)
- `CVF_SESSION_MEMORY.md` pending list: "Skill corpus dead-reference repair — needs a fresh work order; do not start without one"
- Prior repair commit `e28c5464` (post-Lane-G skill corpus test path fix that left residual dead references uncovered)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json` (skill index)

Authority chain: Codex rebuttal accepted N3 as roadmap-only work; no
implementation may begin from this tranche. Downstream implementation
requires a second-round rebuttal of the new roadmap, then a fresh GC-018,
then a separate work order.

---

## Purpose

File a fresh planning roadmap that inventories skill corpus dead references
and stale pointer surfaces, classifies each issue, and proposes per-class
repair strategies with named owner files. The roadmap is the only artifact
this tranche produces. Implementation is explicitly out of scope.

This work order is intake/planning work. It does not modify the skill
index, skill discovery code, skill registry, or any cvf-web surface.

---

## Scope / Target / Owner Boundary

In scope:

- Inventory dead references and stale pointer surfaces in:
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json`
  - Any skill discovery / lookup code that indexes the skill index (search
    for the loader by reading the file's importers in
    `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/`).
  - Any skill-related test fixture that references missing skill IDs or
    missing skill markdown files.
- Classify each issue into exactly one of four classes:
  - `delete` — entry is dead and not referenced; safe to remove
  - `archive-pointer` — entry should remain in index but point to an
    archive path
  - `rewrite-pointer` — entry references the correct concept but the path
    has moved; rewrite to the new canonical path
  - `defer` — issue requires operator/product decision; document the
    decision question and do not propose a repair
- File the roadmap at
  `docs/roadmaps/CVF_SKILL_CORPUS_REPAIR_ROADMAP_2026-05-20.md` with
  explicit evidence anchors and proposed downstream gates.
- File the closure review at the governance repo.

Out of scope (forbidden per Codex rebuttal):

- Skill corpus repair implementation. Any edit to
  `skills-index.json`, skill markdown files, skill loader code, or skill
  fixtures is forbidden in this tranche.
- Mass delete or mass rename of skill entries.
- New skill taxonomy.
- New skill discovery semantics.
- Public claim updates.
- Auth / RBAC changes.
- Filing GC-018 from this tranche.
- Filing the downstream implementation work order from this tranche.
- Reopening any A–H Review-CVF pain point.

Owner boundary:

- This work order touches only the governance repo and only adds three
  new files (roadmap, optional inventory CSV/JSON evidence file, closure
  review) plus session-state and handoff sync edits.

---

## Issue Classes Required in Roadmap

The roadmap must produce an inventory where every dead-reference issue is
assigned exactly one class:

| Class | Meaning | Implementation cost (informational) |
| --- | --- | --- |
| `delete` | Dead entry, no callers, safe to drop | Low — single JSON edit |
| `archive-pointer` | Entry must remain but path moved to archive | Low — single JSON edit |
| `rewrite-pointer` | Entry concept is alive, path canonicalized elsewhere | Medium — JSON edit + verify new path exists |
| `defer` | Decision question, not a code problem | None until decision filed |

If any issue cannot be assigned a class with confidence, mark it `defer`
and explain the decision question in the roadmap.

---

## Deliverables

### Step N3.1 — Skill Corpus Surface Read

Read in full before drafting any roadmap content:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json`
   (full content; do not modify).
2. Skill index loader and lookup paths in
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/` (grep for
   `skills-index.json` and follow imports).
3. Any skill-related test file under
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/` that references skill
   IDs or skill markdown paths.
4. The most recent prior skill repair commit message and diff at
   `e28c5464` for context on what was already fixed.

Output of Step N3.1: an internal scratch list of every skill ID, its
referenced markdown path, and whether the path resolves. This list feeds
Steps N3.2 and N3.3.

### Step N3.2 — Inventory Authoring

For each skill index entry whose markdown path does NOT resolve, record:

- `skillId`
- `indexedPath` (the path written in `skills-index.json`)
- `pathExists` (boolean — must be false to appear in this inventory)
- `proposedClass` (one of `delete`, `archive-pointer`, `rewrite-pointer`,
  `defer`)
- `proposedNewPath` (required when class is `archive-pointer` or
  `rewrite-pointer`; omit otherwise)
- `evidenceCallers` (list of file paths that import / reference the
  `skillId`; empty list is acceptable but must be explicit)
- `notes` (one short sentence explaining the class choice)

Inventory may be stored inline in the roadmap, or as a separate JSON file
at `docs/evidence/skill_corpus_inventory_2026-05-20.json` if inline form
would push the roadmap over `active_markdown` advisory threshold.

### Step N3.3 — Roadmap Authoring

File path: `docs/roadmaps/CVF_SKILL_CORPUS_REPAIR_ROADMAP_2026-05-20.md`

Required structure (per
`docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`
roadmap type):

- Frontmatter: `Memory class: SUMMARY_RECORD`, `Status: READY_FOR_REBUTTAL`,
  `docType: roadmap`, `Date: 2026-05-20`.
- `## Purpose`
- `## Scope / Target / Owner Boundary`
- `## Predecessor Evidence`
- `## Inventory Summary` (counts per class; total dead-reference count)
- `## Per-Class Repair Strategy` (one subsection per class actually used)
- `## Proposed Execution Order` (delete → archive-pointer →
  rewrite-pointer → defer, or justify a different order)
- `## Downstream Gates` (must say: second-round rebuttal required, then
  GC-018, then separate work order; implementation is gated)
- `## Risk / Corrective Action`
- `## Non-Goals`
- `## Work Plan`
- `## Acceptance Criteria` (for the future implementation work order, not
  for this roadmap-filing tranche)
- `## Verification` (static verification only at this stage)
- `## Related Artifacts`
- `## Claim Boundary` (roadmap-only; no implementation)

The roadmap must NOT use any phrasing that implies implementation is
authorized by this tranche. The phrase "downstream implementation requires
fresh rebuttal + GC-018 + work order" must appear in the
`## Downstream Gates` section verbatim or near-verbatim.

### Step N3.4 — Queue Item Update

After the roadmap is committed, add a new item to
`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`:

```json
{
  "id": "skill-corpus-repair-roadmap",
  "artifactType": "roadmap",
  "path": "docs/roadmaps/CVF_SKILL_CORPUS_REPAIR_ROADMAP_2026-05-20.md",
  "status": "READY_FOR_REBUTTAL",
  "requestedReviewer": "Codex",
  "expectedResponsePath": "docs/reviews/CVF_SKILL_CORPUS_REPAIR_ROADMAP_CODEX_REBUTTAL_2026-05-20.md",
  "priority": 3,
  "source": "docs/work_orders/CVF_WO_N3_SKILL_CORPUS_REPAIR_ROADMAP_2026-05-20.md",
  "notes": "Roadmap-only intake from N3. Downstream implementation requires fresh rebuttal + GC-018 + separate work order."
}
```

Adjust priority if necessary so existing items keep their relative order.

### Step N3.5 — Closure Review

File path: `docs/reviews/CVF_N3_SKILL_CORPUS_REPAIR_ROADMAP_CLOSURE_REVIEW_2026-05-20.md`

Required structure: Purpose, Target, Scope/Methodology, Findings,
Decision/Disposition, Claim Boundary.

The closure review must confirm:

- Roadmap filed at
  `docs/roadmaps/CVF_SKILL_CORPUS_REPAIR_ROADMAP_2026-05-20.md`.
- Inventory present (inline or in evidence JSON) with every dead-reference
  entry classified.
- Roadmap's `## Downstream Gates` section explicitly forbids implementation
  without rebuttal + GC-018 + work order.
- No skill index, skill code, or skill fixture was modified.
- No public claim updated.
- Queue item `skill-corpus-repair-roadmap` added with status
  `READY_FOR_REBUTTAL`.
- Pre-commit and pre-push hooks PASS.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [ ] Skill corpus surface read completed for index, loader code, and test
      fixtures.
- [ ] Inventory authored (inline or JSON) with every dead-reference entry
      classified into exactly one of `delete` / `archive-pointer` /
      `rewrite-pointer` / `defer`.
- [ ] Roadmap filed at
      `docs/roadmaps/CVF_SKILL_CORPUS_REPAIR_ROADMAP_2026-05-20.md` with
      all required structural sections.
- [ ] `## Downstream Gates` section in the new roadmap explicitly forbids
      implementation without rebuttal + GC-018 + work order.
- [ ] Queue item `skill-corpus-repair-roadmap` added to
      `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` with `READY_FOR_REBUTTAL`.
- [ ] Closure review filed at
      `docs/reviews/CVF_N3_SKILL_CORPUS_REPAIR_ROADMAP_CLOSURE_REVIEW_2026-05-20.md`.
- [ ] No skill index, skill code, or skill fixture modified
      (verified with `git diff`).
- [ ] No GC-018 filed, no implementation work order filed.
- [ ] Pre-commit hook PASS (11/11).
- [ ] Pre-push hook PASS (43/43).
- [ ] Handoff GC-020 HEAD SHA synced after closure commit.

---

## Forbidden Actions

- Do NOT modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json`.
- Do NOT modify any file under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/`.
- Do NOT modify any skill markdown file.
- Do NOT modify any test fixture.
- Do NOT mass delete or rename skill entries.
- Do NOT propose a new skill taxonomy.
- Do NOT file GC-018 from this tranche.
- Do NOT file the downstream implementation work order from this tranche.
- Do NOT publish anything to the public-sync repo.
- Do NOT use `git add -A` or `git add .`.
- Do NOT bundle N2 work into this tranche.
- Do NOT reopen any A–H Review-CVF pain point.

---

## Authority Chain

- Authorized by: Codex rebuttal verdict NON_BLOCKING_AS_ROADMAP_ONLY on N3
  candidate, 2026-05-20.
- Predecessor roadmap:
  `docs/roadmaps/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_2026-05-20.md`
  (REBUTTAL_FILED_NON_BLOCKING_WITH_GATE_UPDATE).
- Pending source: `MEMORY.md` Pending item "Skill corpus dead-reference
  repair".
- Orchestrator: Claude; Worker: Codex (Orchestrator-author role); Operator
  approval not required for a roadmap-filing tranche.

---

## Agent Roles

- Worker (Codex as Orchestrator-author): reads skill corpus surfaces, builds
  inventory, files roadmap, updates queue, files closure review.
- Orchestrator (Claude): reviews closure review; dispatches second-round
  rebuttal for the new roadmap; later dispatches GC-018 + implementation
  work order after operator approval per accepted scope.

---

## Required First Reads

1. `docs/roadmaps/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_2026-05-20.md` —
   N3 scope.
2. `docs/reviews/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_CODEX_REBUTTAL_2026-05-20.md` —
   N3 boundary.
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json` —
   full skill index.
4. Skill index loader code in
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/` (grep
   `skills-index.json`).
5. `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md` —
   roadmap structural template.
6. Prior repair commit `e28c5464` — context on already-fixed paths.

---

## Pre-Flight Checks

- [ ] Governance repo working tree CLEAN before starting.
- [ ] Confirm `docs/roadmaps/CVF_SKILL_CORPUS_REPAIR_ROADMAP_2026-05-20.md`
      does NOT yet exist.
- [ ] Confirm the new queue item `skill-corpus-repair-roadmap` does NOT yet
      exist in `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`.
- [ ] Confirm at least one dead reference actually exists in
      `skills-index.json`. If none exist, return to Orchestrator — the
      roadmap is not needed.

---

## Write Ownership

May create only:

- `docs/roadmaps/CVF_SKILL_CORPUS_REPAIR_ROADMAP_2026-05-20.md` (new)
- `docs/reviews/CVF_N3_SKILL_CORPUS_REPAIR_ROADMAP_CLOSURE_REVIEW_2026-05-20.md` (new)
- `docs/evidence/skill_corpus_inventory_2026-05-20.json` (new, optional;
  only if inline inventory would push the roadmap past `active_markdown`
  advisory threshold)

May modify only:

- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` (add new queue item)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` (next-allowed-move update after
  closure)
- `AGENT_HANDOFF_V10_2026-05-19.md` (status line + GC-020 HEAD SHA sync)

No other files may be created or modified in either repo. Skill corpus
surfaces (index JSON, loader code, fixtures, markdown files) are strictly
read-only.

---

## Execution Plan

1. Pre-flight checks (Section: Pre-Flight Checks).
2. Read skill corpus surfaces (Step N3.1).
3. Build inventory with class assignments (Step N3.2).
4. Author roadmap with required structural sections (Step N3.3).
5. Add queue item (Step N3.4).
6. File closure review (Step N3.5).
7. Update session state nextAllowedMove + handoff.
8. Commit + GC-020 sync.

---

## Evidence Requirements

- Inventory present (inline or JSON) with every entry classified.
- Roadmap structural completeness hook PASS.
- Queue JSON parses cleanly after new item added.
- `git diff` confirms no skill surface modified.
- Closure review cites the new roadmap path and confirms no implementation
  occurred.

---

## Review Gate

Stop and return to Orchestrator if:

- No dead references exist in `skills-index.json` (the roadmap is
  unnecessary).
- Classifying any issue requires modifying a skill surface to disambiguate
  (suggests scope inflation past roadmap-only).
- The inventory grows past 100 entries (suggests broader corpus rot needing
  a different intake artifact, not a single roadmap).
- The required structural sections for the new roadmap cannot be filled
  from the inventory alone.

---

## Non-Goals

- Skill corpus repair implementation.
- New skill taxonomy or registry.
- New skill discovery semantics.
- Auth or RBAC changes.
- Public claim updates.
- N2 work (workflow-chain V2 rebuttal).
- Reopening any A–H Review-CVF pain point.

---

## Work Plan

Sequential:

1. Run pre-flight checks (Section: Pre-Flight Checks).
2. Read skill corpus surfaces (Step N3.1).
3. Build inventory + class assignments (Step N3.2).
4. Author roadmap (Step N3.3).
5. Add queue item (Step N3.4).
6. File closure review (Step N3.5).
7. Update session state + handoff.
8. Commit using HEREDOC commit message; do not amend.

If any review-gate condition fires, stop and report to Orchestrator before
proceeding.

---

## Closure Checklist

- [ ] Inventory built and classified for every dead reference.
- [ ] Roadmap filed with all required structural sections.
- [ ] Roadmap's Downstream Gates section forbids implementation.
- [ ] Queue item `skill-corpus-repair-roadmap` added with
      `READY_FOR_REBUTTAL`.
- [ ] Closure review filed.
- [ ] No skill index, code, fixture, or markdown modified.
- [ ] Session state nextAllowedMove updated.
- [ ] Handoff GC-020 HEAD SHA synced.
- [ ] Pre-commit + pre-push hooks PASS.
- [ ] No GC-018, no implementation work order.

---

## Return-To-Orchestrator Conditions

Return if:

- Zero dead references found in skill index.
- Inventory exceeds 100 entries.
- Class assignment requires modifying a skill surface to disambiguate.
- Markdown structural completeness hook blocks the roadmap and the fix
  requires roadmap content the inventory cannot supply.
- Queue JSON parse fails after the update.
- Hook failure outside this scope.

---

## Claim Boundary

This work order covers a single intake roadmap filing for skill corpus
dead-reference repair, plus an inventory artifact, queue item addition,
and closure review. It does not authorize new code, new tests, new policy,
new GC-018, downstream work orders, runtime changes, skill taxonomy
changes, or any public claim. Implementation of the proposed repairs
requires a separate rebuttal cycle, a fresh GC-018, and a new work order
dispatched after operator approval.
