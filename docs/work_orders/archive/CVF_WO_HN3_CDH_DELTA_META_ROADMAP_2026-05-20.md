# Work Order — HN3: CDH Delta Meta-Roadmap (Per-Slice Gating, Filing Only)

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Worker role: Codex (Orchestrator-author role)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md` (HN3 framing)
- `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md` (Claude verdict on HN3: NON_BLOCKING_WITH_PER_SLICE_GATING)
- `docs/roadmaps/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md` (BLOCKING; replaced by this meta-roadmap)
- `docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` (BLOCKING_FINDINGS — still load-bearing for each slice)
- Completion evidence already on file:
  - `docs/reviews/archive/CVF_M1_MAIKA_TEXT_SUMMARY_COMPLETION_2026-05-19.md`
  - `docs/reviews/archive/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`
  - `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
  - `docs/reviews/archive/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`

Authority chain: Claude rebuttal on HN3 required per-slice gating —
each of C / D / H / M slices carries its own rebuttal cycle, its own
GC-018, and its own work order. No unified CDH-delta GC-018 is allowed.
This work order produces only the meta-roadmap that organizes the four
slices; it does NOT authorize implementation of any slice.

---

## Purpose

File a single meta-roadmap that replaces the BLOCKING original CDH roadmap
by re-framing C / D / H / M as four independently gated delta slices,
each carrying its own evidence anchor, scope refinement against existing
BLOCKING_FINDINGS, downstream-gate requirements, and explicit non-goals.

The meta-roadmap is a planning artifact. It does NOT file any GC-018, does
NOT dispatch any slice work order, and does NOT modify any runtime,
guard, provider, memory, or Maika surface.

---

## Scope / Target / Owner Boundary

In scope:

- Author one new meta-roadmap at
  `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`.
- The meta-roadmap contains four independent slice sections:
  - **C delta** — existing CLI execute hardening; live-proof and JSONL
    persistence framing.
  - **D delta** — split vision contract vs vision runtime vs reasoning
    contract.
  - **H delta** — policy refinement over existing audit-memory receipt
    flow; preserve capture vs reinjection boundary.
  - **M delta** — Maika text-summary integration through governed CVF
    path only; child / health / photo data forbidden as proof.
- Each slice section must declare: scope, evidence anchor, downstream
  gate (rebuttal + GC-018 + work order), forbidden expansion, and
  acceptance-criteria seed (not full acceptance criteria; that is the
  downstream slice work order's job).
- Mark the original CDH roadmap as REPLACED_BY_META; do NOT delete it.
- Add one new queue item per slice with status `READY_FOR_REBUTTAL`
  and `requestedReviewer: Codex`, so Operator can dispatch slice
  rebuttals independently.

Out of scope (forbidden):

- Implementing C / D / H / M slice work.
- Filing GC-018 for any slice.
- Dispatching any slice work order.
- Modifying any runtime file (route, resolver, guard, provider, memory).
- Modifying any test or fixture.
- Modifying any Maika file or surface.
- Modifying the original CDH roadmap content (only a status note may be
  added at the top).
- Bundling slices into a single GC-018.
- Public-sync push.
- Reopening any A–H Review-CVF pain point.

Owner boundary:

- This work order touches the governance repo only and creates exactly
  one new meta-roadmap + one closure review + queue/session/handoff
  edits, plus a small status note prepended to the BLOCKED original CDH
  roadmap.

---

## Load-Bearing Constraints from Existing CDH BLOCKING_FINDINGS

The four findings from
`docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
remain load-bearing. Every slice section in the meta-roadmap must restate
the relevant finding as a slice-level constraint:

| Slice | Load-bearing constraint |
| --- | --- |
| C delta | Must NOT claim `cvf execute` is missing (Finding 1). Existing CLI execute surface remains the baseline. |
| D delta | Must NOT bundle contract-only with provider runtime claims (Finding 3). Three sub-surfaces (vision contract / vision runtime / reasoning contract) gate independently. |
| H delta | Must NOT treat `reinjectionAllowed` as a memory-capture write gate (Finding 2). Capture vs reinjection boundary is preserved. |
| M delta | Must NOT use Maika child / health / photo data as low-governance proof (Finding 4). Text-summary only through governed CVF path until vision runtime is separately accepted. |

Any slice section that fails to restate its constraint is a structural
defect; the work order returns to Orchestrator.

---

## Per-Slice Required Fields (must appear in meta-roadmap per slice)

| Field | Meaning |
| --- | --- |
| `sliceId` | One of `CDH-C`, `CDH-D`, `CDH-H`, `CDH-M`. |
| `corrected scope` | One-paragraph scope statement after CDH BLOCKING fix. |
| `loadBearingConstraint` | Verbatim restatement of the CDH BLOCKING finding the slice must respect. |
| `evidenceAnchor` | At least one concrete completion-review path under `docs/reviews/`. |
| `downstreamGate` | Required next steps: rebuttal cycle, GC-018, work order. Live-proof requirements named explicitly. |
| `nonGoals` | At least three explicit non-goals (no bundled CDH closure, no broad runtime maturity claim, etc.). |
| `acceptanceCriteriaSeed` | 3–6 bullet points naming the kind of evidence the downstream work order must produce. Not the full acceptance criteria. |

D delta must additionally state its three sub-surfaces explicitly:

- Vision contract (typed shape only; no provider call).
- Vision runtime (provider call + audit-event capture).
- Reasoning contract (typed shape only; reasoning runtime is OUT OF SCOPE
  for this meta-roadmap and would need its own roadmap later).

---

## Deliverables

### Step HN3.1 — Source Read

Read in this order before authoring:

1. `docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` —
   the four BLOCKING findings.
2. `docs/reviews/archive/CVF_M1_MAIKA_TEXT_SUMMARY_COMPLETION_2026-05-19.md`
3. `docs/reviews/archive/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`
4. `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
5. `docs/reviews/archive/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`
6. `docs/roadmaps/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md` — the
   original BLOCKED roadmap (read for context; do not edit content).

### Step HN3.2 — Meta-Roadmap Authoring

File path: `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`

Required structure (per
`docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`
roadmap type):

- Frontmatter: `Memory class: SUMMARY_RECORD`,
  `Status: READY_FOR_REBUTTAL`, `docType: roadmap`, `Date: 2026-05-20`.
- `## Purpose`
- `## Scope / Target / Owner Boundary`
- `## Predecessor Evidence`
- `## Replacement Notice` — explicitly state the meta-roadmap replaces
  the BLOCKED CDH roadmap and that the four BLOCKING_FINDINGS remain
  load-bearing per slice.
- `## Per-Slice Sections` (four subsections, one per slice, each
  containing every required field listed above).
- `## Cross-Slice Non-Goals` — explicit forbidden bundles.
- `## Downstream Dispatch Order` — recommended slice order (e.g., M
  first if Maika is active product; H second; C third; D last because
  vision runtime is heaviest).
- `## Risk / Corrective Action`
- `## Non-Goals`
- `## Work Plan`
- `## Acceptance Criteria` (for the META-ROADMAP filing itself, not the
  slices).
- `## Verification` — static only.
- `## Related Artifacts`
- `## Claim Boundary`.

The meta-roadmap must NOT use language that implies any slice is
authorized for implementation by this filing.

### Step HN3.3 — Mark Original CDH Roadmap REPLACED_BY_META

Prepend a single status note to the top of
`docs/roadmaps/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md` (immediately
after the existing frontmatter, BEFORE any other content):

```markdown
> Status update 2026-05-20: REPLACED_BY_META. This roadmap is superseded by
> docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md per Claude rebuttal
> NON_BLOCKING_WITH_PER_SLICE_GATING. BLOCKING_FINDINGS from
> docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md
> remain load-bearing on each slice. Do not file GC-018 against this
> roadmap; use the meta-roadmap's per-slice gates instead.
```

Do NOT modify any other content in the original roadmap. Do NOT remove
or rewrite the original BLOCKED framing.

### Step HN3.4 — Add Four Slice Queue Items

Add four new items to `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`:

For each slice, use:

```json
{
  "id": "cdh-<slice>-delta",
  "artifactType": "roadmap_slice",
  "path": "docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md",
  "anchor": "#per-slice-section-<slice>",
  "status": "READY_FOR_REBUTTAL",
  "requestedReviewer": "Codex",
  "expectedResponsePath": "docs/reviews/CVF_CDH_<SLICE>_DELTA_CODEX_REBUTTAL_2026-05-20.md",
  "priority": <next available>,
  "source": "docs/work_orders/CVF_WO_HN3_CDH_DELTA_META_ROADMAP_2026-05-20.md",
  "notes": "<one short sentence summarizing scope + load-bearing constraint>"
}
```

Slice IDs are: `m`, `h`, `c`, `d` (so item ids are `cdh-m-delta`,
`cdh-h-delta`, `cdh-c-delta`, `cdh-d-delta`).

Adjust priorities so existing items keep relative order. The four new
items follow `runtime-maturity-cdh` in the queue.

### Step HN3.5 — Closure Review

File path: `docs/reviews/CVF_HN3_CDH_DELTA_META_ROADMAP_CLOSURE_REVIEW_2026-05-20.md`

Required structure: Purpose, Target, Scope/Methodology, Findings,
Decision/Disposition, Claim Boundary.

The closure review must confirm:

- Meta-roadmap filed with all four slice sections.
- Each slice section restates its load-bearing CDH BLOCKING constraint.
- Each slice section has all 7 required fields.
- D delta explicitly states its three sub-surfaces and excludes
  reasoning runtime.
- Original CDH roadmap has the REPLACED_BY_META status note prepended
  and nothing else changed in that file.
- Four new queue items added; existing items still parse cleanly.
- No code/runtime/guard/provider/memory/Maika file modified.
- No GC-018 filed; no slice implementation began.
- Pre-commit and pre-push hooks PASS.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [x] Meta-roadmap filed at
      `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md` with all
      required structural sections.
- [x] Four per-slice sections (M / H / C / D) present, each with all 7
      required fields.
- [x] D delta explicitly names its three sub-surfaces and excludes
      reasoning runtime.
- [x] Each slice section restates its load-bearing CDH BLOCKING
      constraint verbatim.
- [x] Original CDH roadmap has REPLACED_BY_META status note prepended;
      no other content changed.
- [x] Four new queue items added (`cdh-m-delta`, `cdh-h-delta`,
      `cdh-c-delta`, `cdh-d-delta`); queue JSON parses cleanly.
- [x] Closure review filed.
- [x] No code / runtime / guard / provider / memory / Maika file
      modified.
- [x] No GC-018 filed.
- [x] No public-sync push.
- [x] No A–H pain-point reopen.
- [x] Session state + handoff updated.
- [x] Pre-commit hook PASS (11/11).
- [x] Pre-push hook PASS (43/43).

---

## Forbidden Actions

- Do NOT implement any C / D / H / M slice.
- Do NOT file GC-018 from this work order.
- Do NOT dispatch any slice work order from this tranche.
- Do NOT modify any `.ts`, `.tsx`, `.py`, or `.json` runtime file.
- Do NOT modify any Maika surface or any provider integration file.
- Do NOT modify any test or fixture.
- Do NOT delete or rewrite the original CDH roadmap content beyond
  prepending the status note.
- Do NOT bundle slices under a single rebuttal or single GC-018.
- Do NOT claim broad runtime maturity from this meta-roadmap.
- Do NOT use `git add -A` or `git add .`.
- Do NOT touch the public-sync repo.
- Do NOT reopen any A–H Review-CVF pain point.

---

## Authority Chain

- Authorized by: Claude rebuttal verdict NON_BLOCKING_WITH_PER_SLICE_GATING
  on HN3 candidate, 2026-05-20.
- Predecessor roadmap:
  `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`.
- Predecessor BLOCKING source:
  `docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`.
- Orchestrator: Claude; Worker: Codex (Orchestrator-author role); Operator
  approval not required for meta-roadmap filing.

---

## Agent Roles

- Worker (Codex Orchestrator-author): source reading, meta-roadmap
  authoring, REPLACED_BY_META note insertion, queue updates, closure
  review.
- Orchestrator (Claude): reviews closure review; dispatches slice
  rebuttals and downstream GC-018 / work orders only after Operator
  selects a slice.

---

## Required First Reads

1. `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md` —
   HN3 per-slice gating + slice constraints.
2. `docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` —
   the four BLOCKING_FINDINGS (still load-bearing).
3. The four completion reviews (M1 / C2 / D2 / H2) listed in Predecessor.
4. `docs/roadmaps/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md` —
   original BLOCKED roadmap (read-only).
5. `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md` —
   roadmap structural template.

---

## Pre-Flight Checks

- [ ] Governance repo working tree CLEAN before starting.
- [ ] Confirm meta-roadmap path does NOT yet exist.
- [ ] Confirm closure review path does NOT yet exist.
- [ ] Confirm the original CDH roadmap currently has no
      REPLACED_BY_META note (so insertion is the first modification).
- [ ] Confirm the four slice queue items do NOT yet exist in
      `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`.

---

## Write Ownership

May create only:

- `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md` (new)
- `docs/reviews/CVF_HN3_CDH_DELTA_META_ROADMAP_CLOSURE_REVIEW_2026-05-20.md` (new)

May modify only:

- `docs/work_orders/CVF_WO_HN3_CDH_DELTA_META_ROADMAP_2026-05-20.md`
  (status/checklist closure sync only)
- `docs/roadmaps/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md`
  (prepend status note ONLY; no other changes)
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` (add four slice items)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` (nextAllowedMove update after
  closure)
- `AGENT_HANDOFF_V10_2026-05-19.md` (status line + GC-020 HEAD SHA sync)

No other files may be created or modified.

---

## Execution Plan

1. Pre-flight checks.
2. Source read (Step HN3.1).
3. Author meta-roadmap with all four slice sections (Step HN3.2).
4. Prepend REPLACED_BY_META note to original CDH roadmap (Step HN3.3).
5. Add four queue items (Step HN3.4).
6. File closure review (Step HN3.5).
7. Update session state + handoff.
8. Commit + GC-020 sync.

---

## Evidence Requirements

- Meta-roadmap structural completeness hook PASS.
- Each slice section has all 7 required fields verifiable by grep.
- Original CDH roadmap diff shows only the prepended status note.
- Queue JSON parses cleanly after the four new items are added.
- Closure review cites meta-roadmap path + commit SHA.

---

## Review Gate

Stop and return to Orchestrator if:

- Any slice's load-bearing CDH BLOCKING constraint cannot be restated
  verbatim without scope inflation.
- D delta cannot be authored without crossing reasoning-runtime scope.
- M delta cannot be authored without referencing child / health / photo
  data; in that case stop immediately.
- Prepending the REPLACED_BY_META note would require modifying the
  original roadmap's frontmatter or body content beyond the prepended
  block.
- Adding four queue items would conflict with existing items'
  `id`/`expectedResponsePath` fields.

---

## Non-Goals

- Implementing any C / D / H / M slice.
- Filing GC-018 for any slice.
- Dispatching any slice's downstream work order.
- Broadening to reasoning runtime, multi-modal full stack, or new
  provider semantics.
- Claiming any release / live governance proof / public catalog change.
- Reopening N1 / N2 / N3 disposition.
- Reopening any A–H Review-CVF pain point.

---

## Work Plan

Sequential:

1. Pre-flight checks.
2. Source read.
3. Author meta-roadmap.
4. Prepend REPLACED_BY_META note (single block insertion only).
5. Add queue items.
6. File closure review.
7. Session-state + handoff update.
8. Commit using HEREDOC commit message; do not amend.

If any review-gate condition fires, stop and report to Orchestrator
before proceeding.

---

## Closure Checklist

- [ ] Meta-roadmap filed with all four slice sections, all 7 fields per
      slice.
- [ ] Each slice restates its load-bearing CDH BLOCKING constraint.
- [ ] D delta explicitly excludes reasoning runtime.
- [ ] M delta explicitly forbids child / health / photo data as proof.
- [ ] Original CDH roadmap carries REPLACED_BY_META status note only.
- [ ] Four queue items added; JSON parses cleanly.
- [ ] Closure review filed.
- [ ] No runtime / guard / provider / memory / Maika file modified.
- [ ] No GC-018 filed; no slice implementation began.
- [ ] Session state + handoff + queue updated.
- [ ] Pre-commit + pre-push hooks PASS.

---

## Return-To-Orchestrator Conditions

Return if:

- Any slice constraint cannot be honored without scope inflation.
- D delta cannot be written without reasoning-runtime claims.
- M delta cannot be written without child / health / photo data
  references.
- Prepending the status note requires editing the original CDH roadmap
  body.
- Queue JSON conflict on the four new items.
- Markdown structural completeness hook blocks meta-roadmap and the fix
  is not derivable from completion-review evidence.
- Hook failure outside this scope.

---

## Claim Boundary

This work order produces a single meta-roadmap that re-frames C / D / H
/ M as four independently gated delta slices, plus a closure review,
plus queue/session-state/handoff edits, plus a single status-note
prepend to the BLOCKED original CDH roadmap. It does NOT authorize new
code, new tests, new policy, new GC-018, new provider execution, new
memory tier wiring, Maika feature expansion, runtime maturity claim, or
any public claim. Each slice's implementation requires a separate
rebuttal cycle, a fresh GC-018, and a separate work order dispatched
after Operator approval.

This work order does not reopen any A–H Review-CVF pain point and does
not preempt HN1 or HN2.a.
