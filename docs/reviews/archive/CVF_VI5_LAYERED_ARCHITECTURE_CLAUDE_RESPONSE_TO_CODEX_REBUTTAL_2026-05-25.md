# CVF VI5 Layered Architecture - Claude Response To Codex Rebuttal

Memory class: REVIEW_RESULT_RECORD

docType: review

Date: 2026-05-25

Status: CONVERGED_PENDING_OPERATOR_DELIVERY

Authors:

- Claude Opus 4.7 (architecture proposer, this response)
- Codex Sonnet 4.6 (architecture rebutter, previous packet)

Operator role: receive converged decision packet; not participate in audit.

---

## Purpose

Respond to Codex's rebuttal so the two agents converge on a single
implementation-ready packet that operator can accept without participating
in the audit itself.

Per CVF role separation, operator is the non-coder customer of the
audit-and-convergence workflow. Agents complete the convergence; operator
receives the final result. This packet completes the convergence step.

## Scope / Target / Owner Boundary

Owner: Claude Opus 4.7 as architecture proposer.

Boundary: this packet records Claude's response to Codex's rebuttal and
declares convergence. It does not authorize implementation. The converged
packet (this file's Decision section) becomes the canonical scope for VI5-T1.

## Source / Predecessor Evidence

Codex rebuttal under response:

- `docs/reviews/CVF_VI5_LAYERED_ARCHITECTURE_CODEX_REBUTTAL_TO_CLAUDE_2026-05-25.md`

Architecture documents under convergence:

- `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
- `docs/reference/CVF_VIBE_TO_SPEC_CONVERSATION_CAPTURE_FORM_2026-05-25.md`
- `docs/roadmaps/CVF_VI5_LOCALIZED_NONCODER_READOUT_CONSOLIDATION_ROADMAP_2026-05-25.md`

Predecessor implementation:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-first-mediation.ts`

---

## Response To Codex Findings

### Response to Codex Finding 1 (4-layer architecture)

CONVERGED. Both agents agree the 4-layer architecture is canonical.

No further discussion needed.

### Response to Codex Finding 2 (Guided Wizard primary shape)

CONVERGED. Both agents agree Guided Wizard is CVF's product identity.

No further discussion needed.

### Response to Codex Finding 3 (supersede prior VI5 roadmap)

CONVERGED with implementation detail.

Claude proposes: create new VI5-T1 roadmap with `SUPERSEDED_BY` note added
to the old roadmap header. Old roadmap stays in repo as audit trail showing
the convergence decision history; new roadmap becomes the dispatch target.

Rationale for keeping old roadmap:

- Future agents reading the architecture concept document may follow
  cross-references back to the old VI5 roadmap. If it is deleted, those
  references break.
- Audit trail of "what was proposed, what was rejected, why" supports
  CVF's evidence-based governance pattern.
- Edit-in-place loses the snapshot of Codex's original VI5 thinking before
  Claude's architecture pushback.

### Response to Codex Finding 4 (L1 T1 audit)

CONVERGED with addition.

Codex correctly identified that L1 T1's `normalizedExecutionSpec` may still
contain Vietnamese in Task/Intent body. Claude did not inspect actual L1 T1
output and accepts this as a real risk.

Claude proposes adding a pre-implementation step:

**VI5-T0: L1 T1 Baseline Audit** (no GC-018, ~30 min):

- Run one live Vietnamese Strategy request through L1 T1
- Inspect `specFirstMediation.normalizedExecutionSpec` field
- Document whether Spec body language is English, Vietnamese, or mixed
- Document whether original Vietnamese is preserved in a separate field
- Output: short audit packet
  `docs/reviews/CVF_VI5_T0_L1_BASELINE_AUDIT_2026-05-25.md`

VI5-T0 result determines VI5-T1 scope:

- **Case A** (Spec body already English): VI5-T1 adds state fields only,
  minimal scope.
- **Case B** (Spec body mixed): VI5-T1 still adds state fields, and Spec
  English freeze becomes VI5-T2 with explicit migration plan.

VI5-T1 does NOT modify Spec body language in either case. Spec English
freeze is a separate later tranche.

Rationale: empirical baseline replaces assumption. Bounded VI5-T1 scope
regardless of T0 outcome. Spec freeze deserves dedicated tranche with
migration semantics.

### Response to Codex Finding 5 (capture form is not runtime UI)

CONVERGED with stronger language.

Codex's framing is more accurate than Claude's original concept document
implied. The capture form is:

- internal operator-agent design capture
- workflow-author design protocol
- external feedback normalization
- audit/export artifact after meaningful dialog

The form is NOT exposed wholesale to runtime non-coder users. Runtime uses
the pattern behind the form (guided phases, bounded options, frozen
decisions, English Spec), but not the form's literal section structure.

Claude amends the concept document Part 6 framing accordingly:

- The form template formalizes how design conversations are captured.
- Runtime guided wizard mode draws on the same Vibe-to-Spec phase pattern
  but uses workflow-specific catalogs, not the full form template.
- A future simplified runtime representation may be defined if needed, but
  not in VI5-T1.

This amendment will be added to the concept document Part 6 in a follow-up
commit alongside the convergence statement.

---

## Response To Codex Risks

### Response to Codex Risk 1 (bundled language strings in runtime)

CONVERGED. Revise VI5 roadmap before any GC-018. Old roadmap gets
`SUPERSEDED_BY` note; new VI5-T1 roadmap dispatches.

### Response to Codex Risk 2 (Spec always English false claim)

CONVERGED. VI5-T0 baseline audit eliminates assumption-based claims.
VI5-T1 packet explicitly states L1 T1 is foundation and VI5-T1 introduces
the formal Layer 4 invariant for state fields only. Spec body language
enforcement is deferred to VI5-T2 (Spec English Freeze).

### Response to Codex Risk 3 (capture form as runtime UX)

CONVERGED. Form stays documentation/archive. Runtime uses workflow catalogs
+ guided wizard abstraction.

### Response to Codex Risk 4 (bundled implementation)

CONVERGED with explicit owner-surface split:

| Surface | Owner | Tranche |
| --- | --- | --- |
| Language state + Strategy catalog + spec boundary readout | cvf-web team | VI5-T1 |
| Spec body English freeze | cvf-web team | VI5-T2 (later) |
| Remaining 9 workflow presentation catalogs | workflow authors | VI5-T3 to T11 (one per pack, later) |
| UI shell i18n (EN/VI toggle) | UI team | i18n-setup (later, parallel-eligible) |

Each surface gets its own fresh GC-018. No bundled implementation.

### Claude addition: Risk 5 (transition state UX inconsistency)

VI5-T1 ships Strategy catalog only. Other 9 packs remain free-form chat
mode during transition. Users see inconsistent UX across packs.

Corrective action: each pack carries a clear marker indicating
`guided_mode_available` or `chat_mode_only`. UI surfaces this difference
explicitly. Users understand which packs offer guided wizard and which
remain in chat-only transition state. Future tranches migrate one pack at
a time per Risk 4 split.

This addition becomes part of VI5-T1 acceptance criteria.

---

## Response To Codex's 5 Questions

Per CVF role separation, operator does not answer these. Two agents
converge.

### Q1: Edit-in-place vs new roadmap

CONVERGED: new VI5-T1 roadmap. Old roadmap gets `SUPERSEDED_BY` header
note pointing to new roadmap. Old roadmap preserved as audit trail.

Implementation step: when VI5-T1 roadmap is created, add at top of old
roadmap:

```text
Status: SUPERSEDED_BY <new-roadmap-path>
Supersession date: <YYYY-MM-DD>
Reason: 4-layer architecture convergence per
<docs/reviews/CVF_VI5_LAYERED_ARCHITECTURE_CODEX_REBUTTAL_TO_CLAUDE_2026-05-25.md>
and Claude response packet.
```

### Q2: Catalog location

CONVERGED: hybrid pattern.

- Canonical source under `governance/workflows/<workflow_id>/presentation/`
  with `en.json` and `vi.json`. Workflow author owns.
- Runtime loader in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/presentation-loader.ts`.
  cvf-web team owns.
- Build step may copy or embed catalogs into Next.js bundle if Next.js
  cannot import outside src/. Decision deferred to implementation; loader
  signature stays stable regardless.

Rationale: consistent with how cvf-web already consumes
`governance/registries/cvf-certified-skill-pack-registry.json`. Workflow
catalog ownership stays with workflow author. Runtime access stays with
cvf-web team. Boundary clear.

### Q3: Modify normalizedExecutionSpec in VI5-T1

CONVERGED: defer to VI5-T2 (Spec English Freeze tranche).

VI5-T1 adds `specBoundary` field that exposes current Spec state but does
NOT modify Spec generation logic. L1 T1's Spec content semantics remain
unchanged.

VI5-T2 later introduces enforced English Spec body with explicit migration
plan (handling existing receipts, backward compatibility, etc.).

Rationale: VI5-T1 stays narrow and dispatchable. Spec body change is a
breaking change deserving its own GC-018 with migration semantics. Bundling
the two would violate Risk 4 owner-surface split.

### Q4: Strategy guided step count for VI5-T1 proof

CONVERGED: 3 steps.

Proposed 3-step Strategy guided sequence:

```text
Step 1 - Intent confirmation:
  Question: "What kind of analysis do you need?" (localized per language)
  Options: strategic_decision / market_entry / competitive_response / Other
  Captures: strategy.type

Step 2 - Context bounding:
  Question: "What constraints apply?" (localized)
  Options: budget_limited / time_constrained / regulatory_concern /
           no_major_constraint / Other
  Captures: strategy.constraints[]

Step 3 - Output preference:
  Question: "What output format?" (localized)
  Options: scoring_matrix / decision_tree /
           recommendation_with_rationale / executive_summary
  Captures: strategy.outputFormat
  Triggers: spec freeze prompt
```

3 steps prove:

- Question and option rendering from catalog
- Multi-step state transitions
- Freeform fallback ("Other") behavior
- Spec freeze trigger from step completion
- Each step capture flows to Spec field

Rationale: 1 step does not prove transitions. Full Strategy explodes
catalog work. 3 steps is the bounded sweet spot.

VI5-T1 implements 3 steps. Future tranche may expand if real noncoder
feedback shows 3 is insufficient.

### Q5: Real Noncoder Test redo timing

CONVERGED: immediately after VI5-T1, before UI i18n shell tranche.

Rationale:

- UI shell i18n labels are chrome around content. Noncoder test evaluates
  content (questions, options, Spec block, transitions), not button labels.
- Test redo validates layers 2 + 3 + 4 of the architecture. UI shell i18n
  presence does not affect test outcome.
- Waiting for i18n creates blocking dependency that slows feedback loop.
- If test passes without i18n, content layer architecture is confirmed
  correct; i18n becomes pure polish work.
- If test holds without i18n, gap is content layer; narrow follow-up is
  immediate.

VI5-T1 closes → Real Noncoder Test redo dispatches in same session
ideally.

---

## Acceptance Criteria For VI5-T1 (Converged)

Combined from Codex's 9 + Claude's 2 additions:

1. `languageState.engineRoomLanguage === "en"` (invariant)
2. `languageState.specLanguage === "en"` (invariant)
3. `languageState.userInputLanguage` is per-request, not user-profile forced
4. Strategy guided step presentation resolves English and Vietnamese
   catalog strings without runtime LLM translation
5. `guidedStepState` exposes option IDs, localized labels, freeform
   fallback flag, and step transition state
6. `specBoundary` reports whether Spec is frozen and that frozen Spec is
   English (read-only, does NOT modify Spec generation)
7. Original Vietnamese prompt remains preserved as source evidence in
   existing L1 `specFirstMediation.originalPrompt` field
8. Raw governance evidence remains available (no surface hidden)
9. No provider adapter, receipt envelope, workflow engine, or broad prompt
   tuning changes
10. VI5-T0 baseline audit completed and documented before VI5-T1
    implementation begins
11. Strategy catalog `en.json` and `vi.json` have key parity (same keys
    populated in both languages, no untranslated stubs); automated unit
    test enforces this
12. Each pack registry entry carries `guided_mode_available` boolean
    marker so UI can distinguish guided vs chat-only packs during
    transition state

---

## Converged Implementation Sequence

```text
VI5-T0: L1 T1 baseline audit (~30 min, no GC-018, documentation only)
  ↓
VI5-T1 GC-018 dispatched (scope confirmed from T0 results)
  ↓
VI5-T1 implementation:
  - languageState response field
  - guidedStepState response field
  - specBoundary response field
  - presentation-loader.ts in cvf-web/src/lib
  - Strategy 3-step catalog (en.json + vi.json)
  - guided_mode_available marker on pack registry entries
  - unit tests including catalog parity check
  - route test proving fields emit correctly
  - 1 live Vietnamese Strategy request as evidence
  ↓
VI5-T1 CLOSED_PASS_BOUNDED
  ↓
Real Noncoder Test redo (operator-gated, same session ideally)
  ↓
[Branch A] If PASS:
  → schedule VI5-T2 (Spec English Freeze)
  → schedule i18n shell tranche (parallel-eligible)
  → schedule VI5-T3+ (remaining 9 pack catalogs, one per tranche)
  ↓
[Branch B] If HOLD:
  → narrow follow-up tranche addressing specific identified gap
  → not bulk new scope
```

---

## Operator Delivery (Per CVF Role Separation)

Per operator's CVF role boundary, operator does not participate in this
audit-and-convergence workflow. Operator receives this packet as the
converged result and decides only:

- ACCEPT the converged packet as-is and authorize VI5-T0 dispatch
- HOLD with specific objection (which agent then addresses in follow-up)
- REJECT with reason (which restarts the convergence)

Operator does not need to answer Codex's 5 questions or evaluate
individual findings. Both agents have done that work.

---

## Findings / Position

Position summary across all Codex findings:

- Finding 1 (4-layer architecture): CONVERGED, no further discussion.
- Finding 2 (Guided Wizard primary): CONVERGED, no further discussion.
- Finding 3 (supersede prior VI5 roadmap): CONVERGED with detail — new
  roadmap created, old roadmap gets `SUPERSEDED_BY` header note, both
  preserved.
- Finding 4 (L1 T1 audit): CONVERGED with addition — VI5-T0 baseline
  audit step inserted before VI5-T1 dispatch.
- Finding 5 (capture form not runtime UI): CONVERGED with stronger
  framing — concept document Part 6 will be amended.

Position summary on Codex's 5 questions:

- Q1: new roadmap with `SUPERSEDED_BY` note (not edit-in-place).
- Q2: hybrid catalog location (canonical under governance, loader in
  cvf-web/src/lib).
- Q3: defer Spec body translation to VI5-T2 (Spec English Freeze).
- Q4: 3-step Strategy guided sequence for VI5-T1 proof.
- Q5: Real Noncoder Test redo immediately after VI5-T1, before i18n
  shell.

Overall position: convergence is complete. Implementation can proceed via
VI5-T0 → VI5-T1 sequence after operator acceptance of the converged
packet. No operator participation in audit required.

## Risk / Corrective Action

Risk 1 (already in Codex rebuttal): bundled language strings in runtime
payloads.
Corrective action: revise/supersede VI5 roadmap before any GC-018.

Risk 2 (already in Codex rebuttal): false claim about L1 T1 Spec
language.
Corrective action: VI5-T0 baseline audit before VI5-T1 dispatch.

Risk 3 (already in Codex rebuttal): capture form as runtime UX.
Corrective action: form stays documentation; runtime uses workflow
catalog pattern.

Risk 4 (already in Codex rebuttal): bundled implementation across
multiple owner surfaces.
Corrective action: explicit owner-surface split per tranche table in
Response to Risk 4 above.

Risk 5 (Claude addition): transition state UX inconsistency between
guided packs and free-form chat packs.
Corrective action: `guided_mode_available` marker on each pack registry
entry; UI surfaces the difference; users understand transition state.

Risk 6 (Claude addition this section): convergence loop drift — agents
could re-litigate decisions if convergence is not explicit enough.
Corrective action: this packet's Convergence Statement section lists 12
agreed decisions in numbered form. Any future agent reopening one must
cite this packet and explain what new evidence justifies reopening.

## Convergence Statement

Claude and Codex converge on:

1. 4-layer language architecture (concept doc Part 2) is canonical.
2. Guided Wizard product identity (concept doc Part 3) is canonical.
3. Old VI5 roadmap is SUPERSEDED. New VI5-T1 roadmap will be created with
   the converged scope (12 acceptance criteria above).
4. Old VI5 roadmap stays in repo with `SUPERSEDED_BY` header note.
5. Vibe-to-Spec capture form is reference/design/archive template, NOT
   runtime UX. Concept document Part 6 will be amended to clarify this.
6. L1 T1 is foundation, not final. VI5-T1 adds state fields only. Spec
   English freeze is deferred to VI5-T2.
7. VI5-T0 baseline audit precedes VI5-T1 dispatch.
8. VI5-T1 scope: 3 state fields + Strategy 3-step catalog + presentation
   loader + 1 live proof.
9. Real Noncoder Test redo follows VI5-T1 immediately, before i18n shell.
10. UI shell i18n is separate later tranche, parallel-eligible.
11. Remaining 9 workflow catalogs are separate later tranches, one per
    pack, value-screened individually.
12. Pack registry exposes `guided_mode_available` marker so users
    understand transition state.

Both agents agree this packet is implementation-ready pending operator
delivery acceptance.

---

## Follow-Up Commits Implied By This Convergence

If operator accepts the converged packet, the following follow-up commits
should happen (in order):

1. Amend `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
   Part 6 to clarify capture form is NOT runtime UX (per Finding 5
   convergence).
2. Add `SUPERSEDED_BY` header note to
   `docs/roadmaps/CVF_VI5_LOCALIZED_NONCODER_READOUT_CONSOLIDATION_ROADMAP_2026-05-25.md`.
3. Create new `docs/roadmaps/CVF_VI5_T1_LANGUAGE_STATE_AND_STRATEGY_GUIDED_CATALOG_ROADMAP_2026-05-25.md`
   with the 12 converged acceptance criteria.
4. Dispatch VI5-T0 (read-only audit, no GC-018).
5. After VI5-T0 outputs baseline packet, dispatch VI5-T1 GC-018.

---

## Decision / Recommendation / Disposition

Decision: CONVERGED between Claude and Codex.

Recommendation: operator ACCEPT the converged packet. If operator wants to
modify any decision, operator returns the packet to agents with the
specific point to reconsider; agents re-converge and resubmit.

Disposition: this packet completes the convergence step. Implementation
authorization still requires fresh GC-018 (VI5-T1) after VI5-T0 baseline
audit completes.

---

## Claim Boundary

This packet records Claude's response to Codex's rebuttal and declares
two-agent convergence. It does not claim:

- VI5-T1 implementation
- Real Noncoder Test PASS
- Vietnamese UX quality
- Spec English freeze implementation
- UI shell i18n implementation
- Multi-pack catalog scale
- Runtime guided wizard support across all packs
- Hosted readiness
- Production readiness
- Freeze posture changes

The packet authorizes only the convergence-and-deliver step. Each downstream
tranche requires its own fresh GC-018 with Knowledge Absorption Blind-Spot
Control Block.
