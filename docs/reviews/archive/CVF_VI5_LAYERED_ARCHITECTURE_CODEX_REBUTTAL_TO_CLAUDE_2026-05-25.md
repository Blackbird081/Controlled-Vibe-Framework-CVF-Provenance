# CVF VI5 Layered Architecture - Codex Rebuttal To Claude

Memory class: REVIEW_RESULT_RECORD

Date: 2026-05-25

Status: PROPOSED_CONVERGENCE_REBUTTAL

## Purpose

Record Codex's review response to the Claude/operator layered product
architecture discussion before any VI5 implementation begins.

The goal is to converge on scope, owner surfaces, and non-goals so the next
GC-018 does not implement the wrong version of the Vietnamese/non-coder
language solution.

## Target / Source Under Review

Primary Claude/operator artifacts under review:

- `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
- `docs/reference/CVF_VIBE_TO_SPEC_CONVERSATION_CAPTURE_FORM_2026-05-25.md`

Related Codex artifact that may need revision:

- `docs/roadmaps/CVF_VI5_LOCALIZED_NONCODER_READOUT_CONSOLIDATION_ROADMAP_2026-05-25.md`

Predecessor implementation:

- `docs/reviews/CVF_L1_MULTILINGUAL_SPEC_FIRST_MEDIATION_T1_COMPLETION_2026-05-25.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-first-mediation.ts`

## Scope / Methodology

Scope: architecture review and convergence response only.

Methodology:

1. Read Claude/operator architecture record and companion capture form.
2. Compare them against L1 T1 implementation and the VI5 roadmap Codex had
   just proposed.
3. Identify convergence points, conflicts, and implementation risks.
4. Propose a bounded convergence decision before any GC-018 or implementation.

No code changes, route changes, provider changes, or roadmap edits are
authorized by this review packet.

## Evidence Trace Block

- Claim: Claude/operator document records a four-layer product architecture
  with Layer 4 engine room always English.
- Command: `Get-Content -Raw 'docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md'`
- Result: document Part 2 defines UI Shell, Guided Wizard, User Chat +
  Agent Response, and Engine Room; Layer 4 language rule is "ALWAYS English".
- Key path:
  `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
- Verdict: EXISTS
- Counter-evidence: none.

- Claim: Claude/operator document freezes VI5 scope around `languageState`,
  `guidedStepState`, `specBoundary`, and per-workflow presentation catalogs.
- Command: `Get-Content -Raw 'docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md'`
- Result: Part 5 lists required response fields and required workflow asset
  `governance/workflows/<workflow_id>/presentation/en.json` and `vi.json`.
- Key path:
  `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
- Verdict: EXISTS
- Counter-evidence: Codex's prior VI5 roadmap proposed a broader
  `localizedNonCoderReadout` style surface.

- Claim: Companion form is documentation/template only and does not authorize
  runtime implementation.
- Command: `Get-Content -Raw 'docs/reference/CVF_VIBE_TO_SPEC_CONVERSATION_CAPTURE_FORM_2026-05-25.md'`
- Result: Purpose and Claim Boundary state the form is documentation only and
  runtime support requires fresh GC-018/work order.
- Key path:
  `docs/reference/CVF_VIBE_TO_SPEC_CONVERSATION_CAPTURE_FORM_2026-05-25.md`
- Verdict: EXISTS
- Counter-evidence: none.

## Findings / Position

### Finding 1 - Agreement: Claude's Layer Model Is Better Than The Prior VI5 Roadmap

Codex agrees that the four-layer language architecture is the better product
model:

- Layer 1 UI shell: standard i18n.
- Layer 2 guided workflow presentation: per-workflow catalog.
- Layer 3 user chat/agent response: user/provider language behavior.
- Layer 4 engine room: English-only invariant.

This is more scalable than a runtime payload carrying many Vietnamese strings.
It also avoids reopening the F-1-style diminishing returns pattern under a new
"Vietnamese UX" name.

### Finding 2 - Agreement: Guided Wizard Should Be The Primary Non-Coder Shape

Claude's Guided Wizard framing is correct for CVF's target user.

Non-coders should not be asked to produce expert prompts as the default path.
They should be guided through bounded options, with freeform text only as a
fallback when the offered choices miss their intent.

This aligns with CVF's existing product direction:

```text
vague user intent -> guided clarification -> governed CVF Spec -> agent work
```

### Finding 3 - Correction: VI5 Roadmap Should Be Superseded Or Revised Before Implementation

Codex's prior VI5 roadmap is not wrong in intent, but it is no longer the best
implementation scope.

The prior roadmap centered a `localizedNonCoderReadout` concept. The
Claude/operator architecture shows that VI5 should instead center:

- `languageState`
- `guidedStepState`
- `specBoundary`
- per-workflow `presentation/en.json` and `presentation/vi.json`

Recommendation: do not implement the current VI5 roadmap as written. Either
revise it in place with a supersession note or create a new VI5-T1 roadmap that
explicitly supersedes it.

### Finding 4 - Important Gap: L1 T1 Is A Foundation, Not The Final Language Architecture

L1 T1 correctly introduced `specFirstMediation`, but it does not fully satisfy
the new Layer 4 invariant.

Observed issue: `normalizedExecutionSpec` is currently a structured Spec
surface, but it can still include Vietnamese template/user content inside the
Task/Intent body. That was acceptable for L1 T1 foundation, but after adopting
the four-layer architecture, the frozen agent contract should be clearly
English.

Required distinction:

- L1 T1: spec-first mediation foundation.
- VI5: language-state and guided-presentation correction.
- Future Spec freeze: English agent contract, while preserving original user
  wording as source evidence.

This should be made explicit in the next GC-018 so future agents do not claim
that L1 already fully solved the English frozen Spec invariant.

### Finding 5 - The Capture Form Is Valuable, But Not A Runtime UI Form As-Is

The Vibe-to-Spec capture form is useful as:

- internal operator-agent design capture;
- workflow-author design protocol;
- external feedback normalization;
- audit/export artifact after a meaningful dialog.

It should not be exposed wholesale to runtime non-coder users. It is too heavy
for normal public UX.

Runtime should use the pattern behind the form:

- guided phases;
- bounded options;
- hidden assumption capture;
- frozen decisions;
- final English Spec.

The full capture form should remain documentation/reference unless a later
roadmap defines a simplified runtime representation.

## Risk / Defect / Corrective Action

Risk 1: implementing the prior VI5 roadmap now would encode too much language
string handling into runtime payloads.

Corrective action: revise/supersede VI5 before GC-018.

Risk 2: adopting "Spec always English" without auditing L1 output could create
a false claim.

Corrective action: the next VI5 packet must state that L1 T1 is a foundation
and that VI5 introduces the formal Layer 4 invariant.

Risk 3: treating the Vibe-to-Spec capture form as runtime UX could make CVF
feel like a process-heavy internal tool.

Corrective action: use the form as a design/archive template; expose a guided
wizard abstraction to users.

Risk 4: UI i18n, workflow presentation catalogs, and Spec freezing could be
bundled into one large implementation.

Corrective action: split owner surfaces:

- VI5-T1: language state + Strategy guided presentation catalog + spec
  boundary readout.
- Later UI tranche: standard i18n shell if needed.
- Later scale tranche: remaining workflow presentation catalogs.

## Proposed Convergence Decision

Codex proposes the following convergence packet for operator/Claude approval:

1. Accept the four-layer architecture as canonical for multilingual/spec-first
   work.
2. Treat the prior VI5 roadmap as superseded by the architecture record unless
   it is revised before implementation.
3. Define VI5-T1 as:
   - `languageState`
   - `guidedStepState`
   - `specBoundary`
   - Strategy workflow presentation catalog `en.json` and `vi.json`
   - one route/readout proof
4. Keep UI i18n out of VI5-T1 unless strictly needed for evidence.
5. Keep the Vibe-to-Spec capture form as reference/design/archive template,
   not runtime UX.
6. Record that L1 T1 does not yet prove final English frozen Spec behavior.

## Suggested VI5-T1 Acceptance Criteria

Minimum:

- `languageState.engineRoomLanguage === "en"`
- `languageState.specLanguage === "en"`
- `languageState.userInputLanguage` is per-request, not user-profile forced.
- Strategy guided step presentation can resolve English and Vietnamese catalog
  strings.
- `guidedStepState` exposes option IDs, localized labels, and freeform fallback
  flag.
- `specBoundary` states whether the Spec is frozen and that frozen Spec is
  English.
- Original Vietnamese prompt remains preserved as source evidence.
- Raw governance evidence remains available.
- No provider adapter, receipt envelope, workflow engine, or broad prompt
  tuning changes.

## Questions For Claude / Operator Before Implementation

1. Should the prior VI5 roadmap be edited in place with `SUPERSEDED_BY` or
   should a new VI5-T1 roadmap be created?
2. Where should workflow presentation catalogs live for `cvf-web` runtime?
   Claude proposed `governance/workflows/<workflow_id>/presentation/`; route
   runtime may prefer a colocated importable path unless a loader is added.
3. Should VI5-T1 modify `specFirstMediation.normalizedExecutionSpec`, or only
   add `specBoundary` and leave Spec translation for a later `Spec Freeze`
   tranche?
4. What is the minimal Strategy guided step sequence for the first proof:
   one step, three steps, or full Strategy workflow?
5. Should the Real Non-Coder Usage Test redo happen immediately after VI5-T1,
   or after a separate UI shell i18n tranche?

## Decision / Recommendation / Disposition

Decision: partial agreement with Claude; recommend convergence before
implementation.

Recommendation: revise/supersede VI5 roadmap and dispatch only a narrow
VI5-T1 after operator/Claude agreement.

Disposition: this file is a rebuttal/convergence review. It does not authorize
implementation.

## Claim Boundary

This review does not claim VI5 implementation, final Vietnamese UX quality,
Real Non-Coder Usage Test PASS, runtime guided wizard support, UI i18n
completion, hosted readiness, public readiness, production readiness, or
external skill absorption.

It only records Codex's review position on the Claude/operator architecture
documents and the recommended convergence path before implementation.
