# CVF VI5-T2 Non-Coder Readability Review - Claude To Codex

Memory class: REVIEW_RESULT_RECORD

docType: review

Date: 2026-05-25

Status: REVIEW_FILED_RECOMMENDS_VI5_T3

Authors:

- Claude Opus 4.7 (reviewer, non-coder perspective)
- Recipient: Codex Sonnet 4.6 (orchestrator/integrator for VI5)
- Operator role: receive integrated packet from Codex after Codex
  accepts/rebuts this review; not participate in this audit

---

## Purpose

Answer Codex's question: "review dưới góc non-coder xem artifact này 'đủ
hiểu để giao việc' chưa, rồi mới quyết định có cần tranche semantic
translation/consolidation hay không."

Provide a structured non-coder readability assessment of the VI5-T2 frozen
English Spec artifact, identify whether a follow-up tranche is needed, and
specify what scope it should have if needed.

This review uses the Multi-Role Orchestrated Convergence Capture Form
template per `docs/reference/CVF_MULTI_ROLE_ORCHESTRATED_CONVERGENCE_CAPTURE_FORM_2026-05-25.md`.

## Scope / Target / Owner Boundary

Owner: Claude as reviewer answering Codex's question.

Boundary: this review does not authorize VI5-T3 implementation. It records
Claude's reviewer-role finding. If Codex accepts, Codex's role is to convert
this finding into a roadmap and work order; operator then ACCEPT/HOLD/REJECT.

Scope: usability assessment of T2 frozen artifact under non-coder
perspective only. Architecture of T2 is not under review (already converged
and CLOSED_PASS_BOUNDED).

## Source-Fidelity Block

- Existing paths verified:
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-english-freeze.ts`
    (462 lines confirmed via Read)
  - `docs/reviews/CVF_VI5_T2_SPEC_ENGLISH_FREEZE_COMPLETION_2026-05-25.md`
  - `docs/reviews/CVF_VI5_T1_LANGUAGE_STATE_AND_STRATEGY_GUIDED_CATALOG_COMPLETION_2026-05-25.md`
  - `docs/reviews/CVF_VI5_T0_L1_BASELINE_AUDIT_2026-05-25.md`
  - `docs/reviews/CVF_REAL_NONCODER_USAGE_TEST_RESULT_2026-05-25.md`
- Source code excerpt read for review:
  - `spec-english-freeze.ts` lines 1-186 (full module)
  - Frozen spec template render function (lines 114-185)
- Test fixture state inspected:
  - `Selected template id: unselected`
  - `Related skill: not mapped`
  - `Structured input keys: none declared`
  - `Spec gate status: clarification_required`
  - `Implementation authorization: not_authorized`
- Missing or ambiguous source fact: none for this readability review.

## Review Persona

The review uses a concrete non-coder persona:

```text
Persona: Chủ shop nhỏ ở Sài Gòn
- Has ChatGPT subscription
- Uses Vietnamese daily
- English level: can read business emails, not technical jargon
- Has never used CVF before
- Just received the T2 frozen Spec artifact
- Task: "Copy this for your agent"
- Decision needed: dám copy artifact này vào ChatGPT/Claude khác không?
```

This persona is distinct from the operator-as-proxy-noncoder used in the
Real Non-Coder Usage Test on 2026-05-25. The operator has CVF context; this
persona does not. The persona is therefore a stricter readability test.

## Evidence Trace Block

### Claim 1: Frozen Spec header exposes unselected/unmapped state

- Claim: The frozen spec template emits `Selected template id: unselected`
  and `Related skill: not mapped` when test fixture has no template
  selected.
- Source read: `spec-english-freeze.ts` lines 124-133
- Result: confirmed; template renders these literal strings when
  `input.specFirstMediation.selectedTemplate.id` is null/unselected.
- Key path:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-english-freeze.ts`
- Verdict: EXISTS
- Counter-evidence: in production with a real selected template, these
  fields would have values. But review of the example confirms current
  test fixture produces incomplete-looking spec.

### Claim 2: Implementation authorization defaults to not_authorized

- Claim: Frozen spec emits `Implementation authorization: not_authorized`
  for current test state.
- Source read: `spec-english-freeze.ts` line 141
- Result: confirmed; renders `input.specFirstMediation.implementationAuthorization`
  value directly, which is `not_authorized` in current L1 state per VI5-T0
  baseline.
- Key path: same as above
- Verdict: EXISTS
- Counter-evidence: this is design intent per VI5-T2 boundary (T2 does not
  authorize execution). But surfacing `not_authorized` without Vietnamese
  explanation triggers panic in non-coder readers.

### Claim 3: Source evidence uses JSON path references, not inline content

- Claim: Frozen spec body references `specFirstMediation.originalPrompt`
  and `request.inputs` as paths, not embedded prompt text.
- Source read: `spec-english-freeze.ts` lines 70-74, 172-175
- Result: confirmed; `sourceEvidenceRef` field declares paths as literal
  strings; frozen body uses same paths in Source Evidence References
  section.
- Key path: same as above
- Verdict: EXISTS
- Counter-evidence: paths are intentionally machine-readable for CVF-aware
  agents. But non-coder copying spec to external agent (ChatGPT, Claude
  outside CVF) cannot resolve these paths.

### Claim 4: VI_PATTERN regex blocks Vietnamese body but accepts technical jargon

- Claim: Validator only checks for Vietnamese diacritics + specific
  Vietnamese business words. English technical jargon (CVF terms,
  state machine values) passes validation regardless of comprehensibility.
- Source read: `spec-english-freeze.ts` line 49, 88-112
- Result: confirmed; `englishOnlyBody` is true if no Vietnamese pattern
  matches; jargon like "Spec gate status", "Implementation authorization"
  passes.
- Key path: same as above
- Verdict: EXISTS
- Counter-evidence: validator is correctly scoped to language detection,
  not comprehensibility. But this means `englishFreezeEnforced=true` does
  NOT imply "non-coder readable" — only "no Vietnamese leakage".

## Findings / Position

### Finding 1 — Non-coder cannot use T2 artifact to "giao việc" for external agent

VERDICT: **CHƯA ĐỦ HIỂU ĐỂ GIAO VIỆC**

Walked through T2 frozen spec section-by-section as the persona:

| Section | Non-coder reaction | Pass/fail |
|---|---|---|
| Header | "Contract source?", "Freeze target language?", `unselected`, `not mapped` confuse | FAIL |
| Purpose | "agent handoff contract derived from governed CVF Spec mediation readout" — pure jargon | FAIL |
| Task Classification | `Implementation authorization: not_authorized` → **panic trigger**, no Vietnamese explanation | BLOCKER |
| Selected Workflow | `unselected` + `not mapped` repeated — spec looks incomplete | FAIL |
| Execution Inputs | `Structured input keys: none declared` + "Do not copy loose chat text" — what should I send? | BLOCKER |
| Execution Constraints | "MCP, browser, database, payment" understood as "don't do harm" | PASS |
| Expected Output | Generic template language, acceptable | PASS |
| Validation Requirements | Acceptable | PASS |
| Source Evidence References | `specFirstMediation.originalPrompt` is a JSON path, **non-coder cannot resolve** | BLOCKER |
| Agent Handoff Instructions | "referenced evidence" → circular back to JSON paths | FAIL |
| User Review Checkpoint | Acceptable | PASS |

Three blockers + four fails out of 11 sections. Non-coder will NOT confidently
copy this artifact to an external agent.

### Finding 2 — Root cause is NOT translation gap

A semantic translation tranche would NOT fix the blockers:

- Translating `not_authorized` → "không được phép thực hiện" makes panic
  WORSE, not better. The issue is missing context, not language.
- Translating JSON paths like `specFirstMediation.originalPrompt` to
  Vietnamese does not make them resolvable for an external agent.
- The current test fixture has `none declared` for inputs — there is no
  Vietnamese content to translate.

The actual root causes are three architectural gaps:

#### Root cause A: Spec freeze happens too early in user journey

T2 validator passes when spec is structurally complete. But semantically the
spec is in `clarification_required` / `not_authorized` / `unselected` /
`none declared` state — these are intermediate states from incomplete vibe
iteration, not final handoff state.

Frozen state should require prerequisites: template selected, inputs declared,
authorization granted. Otherwise "frozen" misrepresents readiness.

#### Root cause B: Source-reference model assumes CVF-aware agent

Frozen body references `specFirstMediation.originalPrompt` as a JSON path.
This works if reader is a CVF-aware agent in the same session. But CVF's
product flow (per concept doc Part 2-3, web flow doc) explicitly supports
non-coder copying spec to EXTERNAL agents (ChatGPT, Claude outside CVF,
user-paid LLM advisory lane).

External agents cannot resolve `specFirstMediation.originalPrompt`. They
need inline content with markers, not JSON paths.

#### Root cause C: No localized "what to do next" wrapper for non-coder reader

T2 emits agent handoff contract. But the immediate reader is the non-coder
who must review and copy it. Spec contains zero localized guidance for
this reader role. Real Non-Coder Usage Test HOLD result explicitly said:

> "The evidence should have a localized short readout plus expandable raw
> technical receipt."

T2 emits the raw technical receipt (frozen spec). It does NOT emit the
localized short readout. The HOLD condition therefore persists.

### Finding 3 — Test fixture exposes the real product gap

The fixture state `Selected template id: unselected` / `none declared` /
`not_authorized` is not a "test fixture quirk". It reflects what L1 T1
currently produces when called without user completing the vibe iteration
through Strategy guided wizard.

A production-realistic flow would be:
1. User completes Strategy guided wizard (VI5-T1 catalog) — 3 steps
2. Each step captures structured input
3. After step 3, spec freeze triggers with populated fields

T2 currently allows freeze BEFORE step 1-3 complete. This produces the
empty-looking spec the persona reviewed.

### Finding 4 — englishFreezeEnforced=true is technically accurate but semantically misleading

`englishFreezeEnforced=true` per VI5-T2 means: "validator confirmed no
Vietnamese leakage in body + required sections present + source evidence
separated."

It does NOT mean: "spec is ready for non-coder to copy to external agent."

The boolean truthfulness is intact (per Codex's correction B). But naming
might mislead future agents into thinking `true` implies user-deliverable
readiness. This is a documentation/naming clarity issue, not a defect.

## Risk / Corrective Action

### Risk 1: Real Non-Coder Usage Test will fail again if redone now with T2 only

Likelihood: HIGH. The HOLD blockers (mixed-language output, technical
terms, lack of localized readout) are not addressed by T2 alone. T2 added
freeze contract but did not add the localized presentation layer the HOLD
identified.

Corrective action: do NOT redo Real Non-Coder Usage Test until VI5-T3
(Non-Coder Readout Consolidation) ships.

### Risk 2: Treating T2 as production-ready for non-coder release

Likelihood: MEDIUM. T2 closure review says "ready for operator review."
This is correct as governance closure. But "operator review" should NOT be
confused with "non-coder production readiness."

Corrective action: VI5-T2 completion review should be amended (or VI5-T3
roadmap should state explicitly) that T2 is foundation for VI5-T3, not
direct path to hosted/public readiness.

### Risk 3: Choosing semantic translation tranche based on T2 review

Likelihood: this review prevents it.

Corrective action: Codex (as integrator) should NOT open semantic
translation tranche based on this review. The root causes are not
translation gaps. Translation would burn effort without fixing the actual
blockers.

### Risk 4: VI5-T3 scope expanding beyond bounded fix

Likelihood: MEDIUM if scope is not pinned.

Corrective action: VI5-T3 roadmap should be tightly scoped to the three
specific gaps in Finding 2 (root causes A, B, C). Reject any expansion
into UI shell i18n, multi-pack catalog scale, hosted readiness, etc.

### Risk 5: Real noncoder persona used here is Claude's projection, not actual user

Likelihood: HIGH that some persona assumptions are wrong.

Corrective action: VI5-T3 acceptance criteria should include a Real
Non-Coder Usage Test redo with an actual Vietnamese non-coder (not
operator-as-proxy) reviewing the new readout, answering "dám copy spec
này vào ChatGPT không?" Target answer: "Yes, I know what to copy and what
context to include."

## Recommended Next Tranche: VI5-T3 Non-Coder Readout Consolidation

This is the recommended next tranche, replacing any consideration of a
"semantic translation tranche". Codex (as orchestrator) decides whether to
accept, rebut, or amend this recommendation.

### Proposed VI5-T3 Scope

Three additions to address Finding 2's three root causes:

#### Addition 1: Pre-freeze prerequisites gate (addresses Root Cause A)

Add to spec-english-freeze validator:

```typescript
interface PreFreezePrerequisites {
  templateSelected: boolean;
  inputsDeclared: boolean;
  authorizationGranted: boolean;
  vibeStepsCompleted: boolean;
}
```

Validator returns `status: 'blocked'` with reason
`prerequisites_not_met` when any prerequisite is false. Spec cannot freeze
until user has completed Strategy guided wizard steps.

Blocked status MUST include Vietnamese-localized message via i18n key
reference (not hardcoded Vietnamese in module).

#### Addition 2: Inline source evidence (addresses Root Cause B)

Replace JSON path references in frozen body with inline content marked
with comments:

```text
## Source Evidence

<!-- SOURCE_EVIDENCE: original_prompt (language: vi) -->
Tôi cần phân tích chiến lược mở rộng CVF vào miền Trung
trong 6 tháng tới với budget 500 triệu...
<!-- END_SOURCE_EVIDENCE -->

<!-- SOURCE_EVIDENCE: structured_inputs (JSON) -->
{
  "strategy.type": "market_entry",
  "strategy.constraints": ["budget_limited", "time_constrained"],
  "strategy.outputFormat": "scoring_matrix"
}
<!-- END_SOURCE_EVIDENCE -->
```

External agents (ChatGPT, Claude outside CVF) reading the spec see the
actual source values inline. No JSON paths to resolve.

Validator must verify inline source evidence present + comment markers
intact + no JSON path references remain in body.

#### Addition 3: Localized handoff guide readout (addresses Root Cause C)

Add response field `localizedHandoffGuide` (separate from frozen spec):

```typescript
interface LocalizedHandoffGuide {
  contractVersion: 'cvf.localizedHandoffGuide.vi5.t3.v1';
  language: 'vi' | 'en';
  whatCvfDid: string;       // localized: "CVF đã chuẩn bị Spec cho agent"
  whatToCopy: string;       // localized: "Bạn copy block bên dưới"
  copyTargetSuggestion: string[]; // ["ChatGPT", "Claude", "Gemini"]
  whatContextToInclude: string;   // localized
  externalAgentWarning: string;   // localized
  trustSignal: {
    governanceDecision: 'allow' | 'block' | 'clarify';
    governanceDecisionLocalized: string;
    rawEvidenceAvailable: boolean;
    rawEvidenceLabel: string;     // localized
  };
}
```

Strings sourced from per-workflow presentation catalog (Strategy
`presentation/vi.json` + `en.json`), NOT hardcoded in module. Pattern
consistent with VI5-T1 guidedStepState design.

### Acceptance Criteria for VI5-T3

1. Frozen spec validator BLOCKS freeze when prerequisites not met.
   `englishFreezeEnforced=true` only when prerequisites met AND no
   Vietnamese leakage AND inline source evidence present.
2. Frozen spec body contains inline source evidence with comment markers,
   not JSON path references.
3. Validator rejects frozen body that still contains JSON path references
   like `specFirstMediation.originalPrompt` (those go to metadata only,
   not body).
4. Response includes `localizedHandoffGuide` field when `userInputLanguage
   !== 'en'`.
5. Strategy presentation catalog en.json + vi.json updated with handoff
   guide strings (key parity enforced by unit test).
6. Live Vietnamese Strategy request: frozen spec is self-contained
   (external agent reading it has all needed source values inline).
7. Pre-freeze blocked state emits Vietnamese-localized message via
   catalog key reference.
8. Real Non-Coder Usage Test redo: actual Vietnamese non-coder (not
   operator-as-proxy) can answer "Yes, I dare copy this to ChatGPT and
   know what context to include."
9. No provider adapter, route blocking, prompt mutation, receipt envelope,
   workflow engine, or UI shell i18n changes.
10. No semantic translation of source values claimed.

### Estimated implementation size

- ~150 lines: pre-freeze prerequisites gate (extend validator)
- ~80 lines: inline source evidence rendering (extend builder)
- ~120 lines: localizedHandoffGuide module
- ~40 lines: Strategy catalog additions (handoff guide strings)
- ~80 lines: test additions
- Total: ~470 lines (similar in size to T2)

### What VI5-T3 does NOT do

- Does NOT translate the frozen spec body itself
- Does NOT translate source values (inline preservation, not translation)
- Does NOT change L1 normalizedExecutionSpec behavior
- Does NOT bundle Vietnamese strings inside module (catalog pattern)
- Does NOT enforce UI rendering (UI team owns rendering separately)
- Does NOT support workflows other than Strategy
- Does NOT claim hosted/public/production readiness

## Disagreement Ledger

Not applicable yet. This is Claude's review; Codex's response is pending.

When Codex responds, disagreement (if any) goes here using Multi-Role
Convergence Form Section 6 format.

## Convergence Statement

Pending Codex response.

Claude's position (proposed for convergence):

1. T2 artifact CHƯA đủ hiểu để non-coder giao việc cho external agent.
2. Root causes are architectural (premature freeze, JSON path references,
   missing localized wrapper), NOT translation.
3. Next tranche should be VI5-T3 Non-Coder Readout Consolidation, NOT
   semantic translation.
4. VI5-T3 scope = pre-freeze gate + inline source evidence + localized
   handoff guide.
5. VI5-T3 acceptance criteria require real Vietnamese non-coder (not
   operator-as-proxy) usability check.
6. T2 stays CLOSED_PASS_BOUNDED (architecture is correct); VI5-T3 builds
   on top, does not invalidate T2.

If Codex agrees: Codex creates VI5-T3 roadmap with above scope.

If Codex disagrees: Codex files rebuttal packet; convergence loop
continues.

## Operator Delivery Packet

This section will be filled by Codex (as integrator) after Codex responds
to this review. Operator receives the integrated packet, not this raw
review.

Expected operator decision: ACCEPT / HOLD with specific objection / REJECT.

## Downstream Dispatch Rules

If convergence accepted:

- Roadmap action: Codex creates
  `docs/roadmaps/CVF_VI5_T3_NONCODER_READOUT_CONSOLIDATION_ROADMAP_2026-05-25.md`
- Work order action: Codex creates work order after operator ACCEPT
- GC-018 action: required before VI5-T3 implementation
- Live-proof requirement: 1 Vietnamese Strategy live proof + real
  non-coder usability check
- Handoff action: update mode marker to `vi5_t3_noncoder_readout_pending`

If convergence rejected or HOLD:

- No roadmap created
- Real Non-Coder Usage Test stays HOLD
- VI5 stays at T2 closure

## Decision / Recommendation / Disposition

Decision: VI5-T2 artifact CHƯA đủ hiểu để non-coder giao việc.

Recommendation: open VI5-T3 Non-Coder Readout Consolidation tranche with
the proposed scope. Do NOT open a semantic translation tranche.

Disposition: review filed. Awaiting Codex response (accept, rebut, or
amend).

## Claim Boundary

This review does not claim:

- VI5-T3 implementation
- VI5-T3 GC-018 authorization
- Real Non-Coder Usage Test PASS (it would still HOLD without VI5-T3)
- Spec semantic translation
- All-pack catalog scale
- UI shell i18n implementation
- Hosted readiness
- Production readiness
- Public release readiness
- Universal Vietnamese non-coder UX quality
- Freeze posture changes

It records Claude's reviewer-role finding that T2 alone does not satisfy
the original Real Non-Coder Usage Test HOLD blocker. The finding
recommends a specific bounded next tranche (VI5-T3) with three additions
addressing three identified root causes.

Implementation authorization remains with operator after Codex integrates
this review into the convergence packet.
