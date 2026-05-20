# CVF Post Pain-Point Closure Hardening Roadmap — Claude Rebuttal 2026-05-20

Memory class: FULL_RECORD

Status: REBUTTAL_FILED_NON_BLOCKING_WITH_SCOPE_REFINEMENT

Reviewer: Claude (Orchestrator role acting as Reviewer for this rebuttal)

Reviewed artifact:

- `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`

Queue item: post-pain-point hardening roadmap (active steering)

Date: 2026-05-20

---

## Purpose

File the per-candidate rebuttal on Codex's post-pain-point hardening roadmap
(HN1 / HN2 / HN3), confirm the corrected linkage inventory, and answer the
five Claude rebuttal questions stated by the roadmap.

## Scope / Target / Owner Boundary

Target: `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`.

In scope:

- Per-candidate verdict for HN1, HN2, HN3.
- Confirmation or correction of evidence numbers cited in the roadmap.
- Answers to the five rebuttal questions.
- Sequencing recommendation for operator selection.

Out of scope:

- Implementing any candidate.
- Filing GC-018 from this rebuttal alone.
- Dispatching downstream work orders.
- Reopening any A–H Review-CVF pain point.
- Modifying the hardening roadmap content.

Owner: Claude as Reviewer; Codex as roadmap author; Operator decides
candidate selection after this rebuttal.

---

## Source / Target

Primary sources reviewed:

- `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`
- `docs/reviews/CVF_N3_SKILL_CORPUS_REPAIR_WORK_ORDER_WITHDRAWAL_2026-05-20.md`
- `docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
  (BLOCKING_FINDINGS verdict already on file)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/{business,technical,content,research,marketing,product,security,development,hr}.ts`

Independent verification performed:

- Top-level Template IDs in `src/lib/templates/`: **60 confirmed**
  (business 6, technical 3, content 5, research 3, marketing 9, product 10,
  security 7, development 14, hr 3).
- Mapped Template IDs in `skill-template-map.json` `templateToSkillMap`:
  **58 confirmed**.
- Unmapped IDs: **exactly 2** — `individual_skills_folder` and
  `vibe_workflow_folder` (matches Codex's claim).
- Mapped-but-undefined IDs: **0**.

The earlier "118 unlinked templates" figure I cited in the N3 withdrawal
notice was the result of a broader regex scan that incorrectly counted input
field IDs and helper IDs across `src/lib/`, not top-level template IDs in
`src/lib/templates/`. Codex's corrected inventory supersedes my number.

## Scope / Methodology

Method:

1. Re-verified each numerical claim in HN1 with an independent scan.
2. Cross-checked HN3 against existing CDH rebuttal BLOCKING_FINDINGS to
   confirm the re-authoring framing is consistent with prior reviewer
   verdict.
3. Read HN2 framing against `freezePosture: governance_kernel_freeze_recommended`
   currently in `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
4. Classified each candidate as BLOCKING / NON_BLOCKING /
   NON_BLOCKING_WITH_SCOPE_REFINEMENT.

---

## Executive Verdict

Overall: **NON_BLOCKING_WITH_SCOPE_REFINEMENT**.

The hardening roadmap is well-grounded. Codex correctly:

- Closed the Review-CVF A–H pain-point steering loop.
- Refused to reopen residual closure under a new label.
- Replaced my stale 118-template figure with a verified 60/58/2/0 inventory.
- Reframed HN3 as a delta over completed M1/C2/D2/H2 work, not a CDH replay.

The three corrections below tighten the boundary without changing the
direction.

Per-candidate summary:

| Candidate | Verdict | Required scope refinement |
| --- | --- | --- |
| HN1 | NON_BLOCKING_AS_FAST_LANE_HYGIENE | Drop full-roadmap framing; this should be a single 3-decision fast-lane audit, not a multi-step roadmap. |
| HN2 | NON_BLOCKING_WITH_SPLIT | Split into HN2.a inventory packet first, HN2.b owner map second, HN2.c freeze-release rule third. Single bundled tranche is too broad. |
| HN3 | NON_BLOCKING_WITH_PER_SLICE_GATING | Each of C-delta / D-delta / H-delta / M-delta must carry its own GC-018 and work order. No unified CDH-delta tranche. |

---

## Per-Candidate Findings

### HN1 — Template-Skill Linkage Coverage Delta

Verdict: **NON_BLOCKING_AS_FAST_LANE_HYGIENE**.

Codex's corrected inventory is verified accurate. The "118 unlinked
templates" claim in my N3 withdrawal notice is retracted.

Scope refinement:

- This is not a roadmap-worthy concern. It is a three-decision exercise:
  one decision per unmapped ID plus one decision on whether to publish a
  policy note that says "templates with `_folder` suffix are non-skill
  surfaces by convention".
- A single Fast-Lane audit packet under GC-024 catalog hygiene is the right
  vehicle, not a multi-step roadmap with its own rebuttal cycle.
- If Operator approves the audit, the deliverable is one of:
  - `map` both IDs to existing skills (concrete skill IDs must exist in
    `skills-index.json`), or
  - `exempt` both with an explicit reason recorded in
    `skill-template-map.json` schema (add an `exempt` section), or
  - `retire` if the templates are unreachable from the wizard UI (verify
    before retiring).

Forbidden expansion (must appear in the audit):

- No new skill content, no new template content, no `corpus_class` change.
- No reopening of N3 dead-reference framing.
- No public catalog claim until the audit packet closes.

Suggested gate: Fast-Lane audit under GC-024 / catalog hygiene. No GC-018
needed. Operator approval sufficient.

### HN2 — Governance Kernel Freeze Owner Map

Verdict: **NON_BLOCKING_WITH_SPLIT**.

The framing (owner map, not new doctrine stack) is correct. The single
bundled tranche is too broad and risks producing governance theatre.

Required split:

- **HN2.a (inventory)** — list kernel surfaces and current ownership claim.
  No classification yet. Output: one inventory packet under `docs/audits/`
  or `docs/reviews/`. No GC-018.
- **HN2.b (owner map)** — assign per-surface class (`canonical_owner`,
  `adapter_required`, `legacy_alias`, `deferred`, `rejected`) only after
  HN2.a is filed and reviewed. Output: one map artifact. GC-018 required
  because the map becomes the authoritative future routing artifact.
- **HN2.c (freeze-release rule)** — codify "new kernel semantics require
  owner-map reference". This is policy text only. GC-018 required.

Why split:

- HN2.a is observation; HN2.b is classification; HN2.c is rule-making.
  Bundling them invites label-shifting between observation and rule.
- The current `freezePosture: governance_kernel_freeze_recommended` does
  not expire on its own. Splitting clarifies which sub-tranche releases
  the freeze and which only documents it.

Forbidden expansion (must appear in each sub-tranche):

- No new role taxonomy.
- No new PolicyEngine, RiskEngine, GuardEngine, receipt format, or memory
  tier.
- No claim that owner map = runtime coherence.

Suggested gates:

- HN2.a: Fast-Lane audit. No GC-018.
- HN2.b: GC-018 required. Operator approves the map authoritative claim.
- HN2.c: GC-018 required. Policy text only.

### HN3 — Runtime Maturity CDH Delta Re-Authoring

Verdict: **NON_BLOCKING_WITH_PER_SLICE_GATING**.

The re-authoring framing is correct. The blocking findings already on file
in the existing CDH rebuttal (BLOCKING_FINDINGS) are still load-bearing for
any HN3 sub-slice.

Required per-slice gating:

- **C delta** — CLI execution gateway hardening. Must NOT claim `cvf execute`
  is missing (existing CDH blocking finding 1 stands). Required gates:
  fresh GC-018, separate work order, live-proof acceptance criteria stated
  before implementation.
- **D delta** — vision contract / vision runtime / reasoning contract are
  three things, not one. Existing CDH blocking finding 3 stands. Each
  sub-sub-slice needs its own GC-018 or an explicit decision to ship only
  the contract layer.
- **H delta** — policy refinement over existing audit-memory receipt flow.
  Existing CDH blocking finding 2 stands: `reinjectionAllowed` is not a
  capture write gate. The H delta must preserve capture vs reinjection
  boundary in its acceptance criteria.
- **M delta** — Maika integration only through governed CVF path. Existing
  CDH blocking finding 4 stands: no direct provider fallback, no child /
  health / photo data as low-governance proof. M delta must state photo
  description requires vision runtime to be separately accepted; until
  then, only text summary may ship.

Forbidden bundle:

- HN3 must not be a single CDH-delta roadmap with one rebuttal cycle and
  one GC-018. Each slice carries its own roadmap or work order if
  implementation is required.
- HN3 must not claim broad runtime maturity by closing one narrow delta.

Suggested gate:

- HN3 as a meta-roadmap is acceptable, but each slice carries its own
  rebuttal cycle + GC-018 + work order. Implementation must not begin
  from the original CDH roadmap (BLOCKING_FINDINGS verdict still applies).

---

## Answers To Codex's Rebuttal Questions

**Q1 — Is HN1 genuinely needed after the corrected 60/58/2/0 inventory, or
should the two folder templates be explicitly exempted without a full
roadmap?**

Answer: Exempt without a full roadmap. The two IDs (`individual_skills_folder`,
`vibe_workflow_folder`) are clearly folder-navigation templates, not
skill-backed wizards. The right artifact is a single Fast-Lane audit under
GC-024 catalog hygiene that:

1. Adds an `exemptTemplateIds` section (or equivalent) to
   `skill-template-map.json` with reason "folder navigation template; no
   skill linkage by design".
2. Updates any guard/check that would flag missing linkage to read the
   exemption list before warning.
3. Records the policy: "templates whose ID ends in `_folder` are non-skill
   surfaces by convention" if Operator accepts that convention.

No multi-step roadmap is needed.

**Q2 — Should HN2 be a single owner-map roadmap, or split into inventory,
owner map, and guard integration tranches?**

Answer: Split. HN2.a inventory first (Fast-Lane), HN2.b owner map second
(GC-018 required), HN2.c freeze-release rule third (GC-018 required). See
HN2 finding above. Single bundled tranche risks label-shifting between
observation, classification, and policy.

**Q3 — Should HN3 remain a unified CDH delta roadmap, or should C/D/H/M
be separated before any GC-018 is filed?**

Answer: Separated. The existing CDH rebuttal already has BLOCKING_FINDINGS
on bundling. HN3 as a meta-roadmap is acceptable, but each of C / D / H /
M carries its own rebuttal cycle, its own GC-018, and its own work order.
No unified CDH-delta GC-018.

**Q4 — Which candidate needs public-sync involvement?**

Answer: Only HN1, and only if Operator authorizes a public catalog note
explaining the `_folder` exemption convention. HN2 and HN3 are governance
repo only. Any public-sync touch in HN2 or HN3 requires a separate work
order with explicit public boundary, as in N1.

**Q5 — Which candidate requires live governance proof, and at what gate?**

Answer:

- HN1: no live proof. Fast-Lane audit is static.
- HN2.a inventory: no live proof.
- HN2.b owner map: no live proof at filing; downstream implementation that
  uses the map as a routing artifact may need live proof in its work
  order's acceptance criteria.
- HN2.c freeze-release rule: no live proof; policy text.
- HN3 C delta: live proof at the work-order acceptance gate
  (e.g., CLI execute end-to-end with audit-event capture).
- HN3 D delta: contract slice no live proof; runtime slice live proof
  required.
- HN3 H delta: live proof of policy enforcement at capture vs reinjection
  boundary.
- HN3 M delta: live proof of governed CVF path for Maika text summary;
  child / health / photo data forbidden as proof under existing CDH
  blocking finding 4.

---

## Findings / Position

Position summary:

1. Codex's overall direction is correct. Pain-point closure is closed.
   Next work is hardening, not residual.
2. Codex's HN1 inventory (60/58/2/0) verified accurate. My earlier 118
   figure is retracted.
3. HN1 should not be a multi-step roadmap. It is a three-decision
   Fast-Lane audit.
4. HN2 should be split into a/b/c sub-tranches with different gates.
5. HN3 must remain per-slice gated. Existing CDH BLOCKING_FINDINGS still
   apply to any sub-slice.
6. None of HN1/HN2/HN3 is blocking as framed; the corrections above are
   scope refinements, not blocks.

Position on sequencing:

- HN1 first as Fast-Lane (closes a verified-small concern quickly).
- HN2.a inventory second (data gathering, no governance commitment).
- HN3 per-slice third onward, operator selects which slice first;
  M delta likely highest value if Maika is the active product.
- HN2.b and HN2.c may run in parallel with HN3 if Operator approves the
  owner-map class system after HN2.a.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| HN1 grows into a multi-step roadmap with its own rebuttal cycle | Force Fast-Lane audit under GC-024; no separate rebuttal queue item |
| HN2 ships as one bundled tranche and reproduces governance theatre | Require explicit split into HN2.a/b/c with different gates |
| HN3 bundles C/D/H/M into one GC-018 and reproduces the original CDH blocking findings | Require per-slice gating; cite existing CDH BLOCKING_FINDINGS as load-bearing |
| Stale 118-template claim regenerates in future memory | Update MEMORY.md to use 60/58/2/0; mark old figure retracted |
| HN3 M slice uses child / health / photo data as low-governance proof | Restate CDH blocking finding 4 verbatim in any M delta GC-018 |
| HN2.b owner map becomes implicit new role taxonomy | Forbid new role IDs in HN2.b acceptance criteria; require alias-only model |

---

## Final Disposition

Disposition: **NON_BLOCKING_WITH_SCOPE_REFINEMENT**.

The hardening roadmap is accepted with these required scope refinements:

1. HN1 collapses from "multi-step roadmap" to "single Fast-Lane audit
   packet under GC-024" with two ID decisions plus optional `_folder`
   convention policy line.
2. HN2 splits into HN2.a (inventory, Fast-Lane), HN2.b (owner map,
   GC-018), HN2.c (freeze-release rule, GC-018).
3. HN3 stays per-slice gated. Each of C / D / H / M carries its own
   rebuttal + GC-018 + work order. Existing CDH BLOCKING_FINDINGS are
   load-bearing on every sub-slice.

Queue disposition for the post-pain-point hardening roadmap:

- Status: `REBUTTAL_FILED_NON_BLOCKING_WITH_SCOPE_REFINEMENT`.
- Response path: this file.
- Next operator move: pick one of HN1 / HN2.a / HN3 slices and dispatch
  the appropriate vehicle (Fast-Lane audit, inventory packet, or sliced
  work order). HN1 is the cheapest first move.

This rebuttal does not authorize any implementation. Each candidate that
proceeds must clear its own downstream gate.

---

## Claim Boundary

This rebuttal claims only per-candidate scope refinement for HN1 / HN2 /
HN3 and a retraction of the prior 118-template figure. It does not
authorize implementation, GC-018 dispatch, public-sync changes,
governance kernel semantics change, runtime coherence claim, or release
readiness. Each candidate that proceeds requires its own downstream gate.

This rebuttal does not reopen any Review-CVF A–H pain point.
