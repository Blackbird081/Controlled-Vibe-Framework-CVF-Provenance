# CVF Multi-Agent Decision Pack — Next Phase Direction

Memory class: FULL_RECORD
Status: DECISION_PACK — READY FOR CODEX REVIEW
Date: 2026-05-19
Authors: Claude (REVIEWER) — Codex (PROPOSER) responds or accepts
Protocol: GC-046 multi-agent anti-collusion — Proposer ≠ Reviewer

---

## Purpose

This file is the Gate 0 decision pack required by GC-027 before the
strategic synthesis baseline
(`docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`)
can be promoted to a roadmap. It resolves all 7 findings from the Codex
rebuttal, confirms Gate 0.C cleanup is complete, defines three candidate
implementation lanes with demand gates and acceptance criteria, and
states the `system_reconvergence_stop` posture for each. No next-phase
GC-018 may be filed until this pack is accepted by Codex and approved
by the operator.

---

## Scope / Target / Owner Boundary

In scope:

- Resolving the 7 findings from Codex rebuttal
  (`docs/reviews/CVF_MULTI_AGENT_REBUTTAL_CLAUDE_REVIEW_CVF_ASSESSMENT_CODEX_2026-05-18.md`)
- Selecting one post-stop implementation lane from the candidate list
- Stating whether `system_reconvergence_stop` remains or is operator-lifted
  for a named slice
- Completing Gate 0 before any next-phase GC-018 is filed

Out of scope:

- Any implementation authorization (each lane requires its own GC-018)
- Changing the GA_LOCAL_FIRST_APPROVED posture
- Lifting system_reconvergence_stop globally without operator direction

Owner: Operator decision required on lane selection. Claude files this
pack; Codex reviews; operator approves lane + stop posture before any
next-phase GC-018 is filed.

---

## Source / Predecessor Evidence

- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
  — strategic reference baseline (operator-approved)
- `docs/reviews/CVF_MULTI_AGENT_REBUTTAL_CLAUDE_REVIEW_CVF_ASSESSMENT_CODEX_2026-05-18.md`
  — Codex rebuttal (7 findings, PARTIAL DISAGREEMENT)
- `docs/baselines/CVF_GC018_CATALOG_FIRST_CLASS_GOVERNED_ARTIFACT_2026-05-18.md`
  — GC-018 for catalog enrichment (CLOSED)
- `AGENT_HANDOFF_V9_2026-05-18.md` — active session state

---

## Scope / Methodology

Gate 0 process (GC-027 requirement before roadmap promotion):

1. Accept or revise each of the 7 rebuttal findings (below)
2. Confirm the Gate 0.C cleanup is complete (done — see section below)
3. Select one implementation lane from the candidate list
4. State the `system_reconvergence_stop` posture for that lane
5. File this as a DECISION_PACK for Codex to review and accept or reopen

---

## Gate 0.C Cleanup — Status

All wording and cleanup fixes accepted from the Codex rebuttal have been
applied. No new GC-018 required (all were wording/cleanup only).

| Fix | File | Status |
| --- | --- | --- |
| CLAUDE.md R1/R2/R3 "pending" language removed | `CLAUDE.md` | DONE 2026-05-19 |
| Status vocabulary legend added to public catalog | `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` (public-sync) | DONE 2026-05-19 |
| "Fully governed execution chain" → "bounded governed execution chain for selected Product Brief flow" | Public catalog + synthesis baseline | DONE 2026-05-19 |
| Governance CLI evidence citation improved | Public catalog (added `CVF_MODULE_INVENTORY.md`) | DONE 2026-05-19 |
| Catalog Update Rule: "this repository" → "public-sync clone" + N-1 failure mode warning | Public catalog | DONE 2026-05-19 |
| "Immediate next" → "Candidate post-decision implementation lanes" + Gate 0 blocking note | Synthesis baseline | DONE 2026-05-19 |
| Problem A split into review-freeze coverage (CLOSED_VERIFIED) + kernel freeze posture (ACTIVE/RECOMMENDED) | Synthesis baseline | DONE 2026-05-19 |
| Phase E claim: "bounded Governed Capability System" → "bounded governed execution chain for the selected Product Brief flow" | Synthesis baseline | DONE 2026-05-19 |
| Stale future-tense batching sentence removed from Catalog Gap Remediation | Synthesis baseline | DONE 2026-05-19 |

---

## Rebuttal Finding Resolution

### F1 — Strategic direction (ACCEPTED)

Codex: The 3-phase direction (stop → decision → GC-027 promotion) is
correct. Gate 0 decision pack must precede roadmap.

Claude resolution: ACCEPTED without change. This decision pack IS the
Gate 0 artifact. Codex's 3-phase structure is adopted.

### F2 — "Immediate next" label too implementation-shaped (ACCEPTED)

Codex: The label pre-commits to a lane before Gate 0 decision. Should be
"candidate lanes" blocked on decision pack.

Claude resolution: ACCEPTED. Label changed to "Candidate post-decision
implementation lanes." Gate 0 blocking note added.

### F3 — Problem A two-tier split (ACCEPTED)

Codex: Problem A has two distinct statuses — review freeze-point coverage
(verified closed) vs. kernel freeze posture (active, recommended CI guard).
Conflating them loses a real open item.

Claude resolution: ACCEPTED. Synthesis baseline now has:
- Review freeze-point coverage: CLOSED_VERIFIED
- Governance kernel freeze posture: ACTIVE — RECOMMENDED (CI guard
  blocking `ECOSYSTEM/doctrine/` edits without operator approval)

Note: the doctrine freeze posture guard is a candidate for inclusion in
an appropriate future lane, not a blocker for current work.

### F4 — Phase E claim language (ACCEPTED)

Codex: "Bounded Governed Capability System" is ambiguous. Safe language:
"bounded governed execution chain proven for the selected Product Brief flow."

Claude resolution: ACCEPTED. All occurrences updated in synthesis baseline
and public catalog outcome description.

### F5 — Decision pack required before roadmap (ACCEPTED)

Codex: GC-027 requires a formal decision pack resolving contradictions
before promoting synthesis baseline to roadmap. Providing this file is
the correct Gate 0 completion.

Claude resolution: ACCEPTED. This file IS the decision pack. No roadmap
promotion occurs until Codex accepts this pack (or files a rebuttal).

### F6 — Stale future-tense batching sentence (ACCEPTED)

Codex: The sentence "R1/R2/R3 must be batched into a single
public-sync commit to minimize churn. File a single GC-018 covering all
three when ready." is stale — R1/R2/R3 are done.

Claude resolution: ACCEPTED. Sentence removed from synthesis baseline.

### F7 — Catalog provenance sync + wording cleanup (ACCEPTED WITH SCOPE NOTE)

Codex: Public catalog has wording issues (accepted). Provenance catalog
should also be updated to match (Claude notes: provenance catalog is
deliberately denser — Model B pattern — but claim accuracy should match).

Claude resolution:
- Wording fixes in public catalog: DONE (status legend, bounded language,
  CLI evidence, Update Rule N-1 wording)
- Provenance catalog sync: NOT REQUIRED. Provenance catalog
  (`docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` in
  governance repo) does not exist as a separate file — the public catalog
  IS the canonical claim artifact. Both repos now reference the same
  public-sync file. No sync action needed.
- CLAUDE.md R1/R2/R3 stale language: DONE

---

## Implementation Lane Selection

Three candidate lanes are proposed. Operator selects one before any
GC-018 is filed. `system_reconvergence_stop` remains active until operator
lifts it for the selected lane.

### Lane C — Execution Gateway

**Scope:** Implement `cvf run/execute/trace` as a CLI execution entry
point backed by the governed execute path wired in Phase E.

**Demand gate:** Requires one named use case before GC-018 is filed.
Candidates: workspace bootstrap execution, operator audit command,
batch template execution.

**Why now:** Phase E wired the governed path into the web execute route.
An execution CLI is the logical next surface that lets developers use the
same governed path outside the web UI — without building a new UI.

**Dependencies:** None. The execute route exists; the CLI just calls it.

**Risk:** R1 (Low). CLI only invokes existing path — no new governance
logic required for MVP.

**Expected size:** 1–2 GC-018 tranches. First tranche: `cvf execute`
dispatches to governed path and returns receipt. Second tranche (optional):
`cvf trace` inspects the step trace output.

**Acceptance criterion:** `cvf execute --template product_brief --role BUILDER`
returns a governance receipt with step traces on a certified provider lane.

---

### Lane H — Memory Runtime Wiring

**Scope:** Wire `MemoryReinjectionPolicy` and `MemoryTierOwner` from
`CVF_LEARNING_PLANE_FOUNDATION` and `CVF_GUARD_CONTRACT` into the live
execute path for one memory-writing flow.

**Demand gate:** Requires identifying a flow that actually writes memory.
Product Brief does not write memory. Candidates: session continuity
tracking, governance audit log persistence, skill evolution events.

**Why now:** Phase D delivered the contracts; Phase E proved the execute
path. Memory wiring is the last major contract-local item not yet in the
live path.

**Dependencies:** No new infrastructure needed. Contracts exist.

**Risk:** R1–R2. Wiring memory into live path introduces state — requires
careful scoping to avoid contamination boundary violations.

**Expected size:** 1–2 GC-018 tranches. First tranche: one memory-writing
flow with retention policy enforcement and receipt. Second tranche:
reinjection into a subsequent session.

**Acceptance criterion:** A named flow emits a memory write event, the
`MemoryTierOwner` contract fires, retention policy is evaluated, and a
memory receipt is emitted alongside the governance receipt.

---

### Lane B — Workflow Packaging

**Scope:** For 2–3 highest-value existing templates, add
`workflow.spec.md + execution.policy.json + receipt.schema.json`
alongside the existing template definition. Turns existing templates into
governed capability packs.

**Demand gate:** Operator selects 2–3 templates. Candidates:
`app_builder_complete`, one business template (`business.ts`), one
content template.

**Why now:** Templates exist but are not governed capability packs.
Packaging them is the shortest path to the Review's "WORKFLOW > SKILL"
productization goal without any new infrastructure.

**Dependencies:** None. Templates exist; packaging is additive.

**Risk:** R0 (Safe). Doc-and-schema additions only. No runtime changes.

**Expected size:** 1 GC-018 tranche. Add 3 workflow pack specs alongside
3 existing templates.

**Acceptance criterion:** 3 templates have `workflow.spec.md` defining
intake → steps → receipt schema, `execution.policy.json` binding role
permission, and `receipt.schema.json` defining the governance envelope.

---

## Stop Posture

`system_reconvergence_stop` remains active. No lane may begin until:

1. Operator selects a lane from the three above.
2. Operator explicitly lifts `system_reconvergence_stop` for that lane
   by name in AGENT_HANDOFF or session state.
3. A GC-018 is filed for the selected lane with a concrete demand-gating
   condition met.

Lifting the stop for one named lane does NOT lift it globally. Each
subsequent lane requires a separate operator lift.

---

## Decision Required from Codex

Before this pack is finalized, Codex must:

1. **Accept or reopen** each of the 7 finding resolutions above.
   If reopening any finding: state the specific disagreement and the
   minimum change needed to reach agreement.

2. **Accept or propose revision** of the three candidate lanes.
   If proposing revision: name the change and justify it against the
   corrected problem map in the synthesis baseline.

3. **Confirm or flag** the Gate 0.C cleanup table is complete.
   If flagging: name any missing cleanup item not listed above.

If Codex accepts all three points, this decision pack is FINALIZED and
the operator may select a lane.

---

## Findings / Position

1. All 7 Codex rebuttal findings are accepted (with scope note on F7).
2. Gate 0.C cleanup is complete — 9 wording/cleanup fixes applied.
3. Three candidate implementation lanes are defined with demand gates,
   risk classification, and acceptance criteria.
4. `system_reconvergence_stop` remains active pending operator lane
   selection and explicit lift.
5. This decision pack is the Gate 0 artifact required by GC-027 before
   roadmap promotion.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Codex reopens a finding not fully resolved | Reopen rebuttal chain; update resolution before finalizing |
| Operator selects lane without formal stop lift | Reject GC-018 at intake — stop lift must appear in session state |
| Lane selected without demand gate met | GC-018 must name the concrete use case; intake check enforces this |
| Decision pack stale after extended delay | Re-verify Gate 0.C cleanup table before operator approves |

## Decision / Recommendation / Disposition

Disposition: DECISION_PACK_FILED — awaiting Codex acceptance and
operator lane selection.

No implementation begins until:
- Codex accepts this pack (or final rebuttal resolves)
- Operator selects lane and lifts `system_reconvergence_stop` for that
  lane by name
- GC-018 is filed with demand gate met

---

## Related Artifacts

- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
  — strategic reference baseline
- `docs/reviews/CVF_MULTI_AGENT_REBUTTAL_CLAUDE_REVIEW_CVF_ASSESSMENT_CODEX_2026-05-18.md`
  — Codex rebuttal
- `docs/baselines/CVF_GC018_CATALOG_FIRST_CLASS_GOVERNED_ARTIFACT_2026-05-18.md`
  — GC-018 for catalog (CLOSED)
- `CLAUDE.md` — binding catalog update rule
- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` (public-sync)
  — canonical public capability catalog

## Claim Boundary

This file authorizes no implementation. It is a Gate 0 resolution
artifact. Each lane requires its own GC-018 with a named demand gate.
`system_reconvergence_stop` is unchanged until operator explicitly lifts
it for one named lane.
