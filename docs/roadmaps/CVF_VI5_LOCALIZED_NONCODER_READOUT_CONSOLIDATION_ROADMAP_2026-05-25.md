# CVF VI5 Localized Non-Coder Readout Consolidation Roadmap

Memory class: ROADMAP_RECORD

Date: 2026-05-25

Status: PROPOSED_FOR_OPERATOR_REVIEW

## Purpose

Define a bounded roadmap for improving Vietnamese non-coder usability after
`cvf.specFirstMediation.l1.v1` proved that CVF can preserve the original
Vietnamese prompt, produce a standard agent-readable Spec, and return a short
localized evidence summary.

This roadmap is intentionally narrow. It targets CVF-controlled action/readout
clarity, not broad translation quality tuning.

## Authorization Or Decision

Decision state: proposed only.

Implementation is not authorized by this document. If the operator accepts the
value boundary, the next step is a fresh GC-018 and work order for VI5.

## Target / Source

Primary source:

`docs/reviews/CVF_L1_MULTILINGUAL_SPEC_FIRST_MEDIATION_T1_COMPLETION_2026-05-25.md`

Parent roadmap:

`docs/roadmaps/CVF_L1_MULTILINGUAL_SPEC_FIRST_MEDIATION_ROADMAP_2026-05-25.md`

Product direction:

`docs/reference/CVF_NONCODER_SPEC_FIRST_WEB_FLOW_2026-05-25.md`

Live sample observed on 2026-05-25:

- provider/model: `alibaba/qwen-turbo`
- receipt: `rcpt-env-mpkz9wg4-2izzf8`
- decision: `ALLOW`
- result: `specFirstMediation` contract passed, but model output still used
  some English headings such as `MVP Scope And Prioritization Decision`.

## Scope / Target / Owner Boundary

Owner surface: `cvf-web` response-level and UI-ready non-coder readout.

Target user: Vietnamese non-coder reviewing a CVF result and deciding what to
copy, what to trust, and what to do next.

Boundary: this roadmap is about the CVF-controlled readout layer. It does not
try to control every heading or sentence emitted by the provider model.

## Problem Statement

L1 T1 already proves the core control point:

```text
Vietnamese input -> preserved prompt -> English/structured working Spec
-> localized evidence summary -> raw technical evidence available
```

The remaining issue is public-facing clarity. A Vietnamese non-coder may still
see mixed-language provider output or internal terms and miss the most
important action:

```text
This is the part to read.
This is the part to copy to an agent.
This is the evidence summary.
This is what CVF did not authorize.
```

If CVF tries to solve this by tuning the provider output until all text is
perfect Vietnamese, the tranche can become expensive and low-yield. The better
target is a small CVF-owned localized action/readout layer.

## Value Screen

High-value if scoped to:

- Vietnamese labels for CVF-owned readout fields;
- an explicit "copy this Spec for the agent" cue;
- a short action summary in the user's language;
- clear separation between user-facing summary and raw technical evidence;
- explicit advisory/source-only boundaries.

Low-value if scoped to:

- broad translation quality benchmarking;
- forcing every provider output heading into Vietnamese;
- repeated live reruns for wording variance;
- multilingual expansion beyond Vietnamese and English;
- prompt tuning that reopens F-1-style diminishing returns.

## Product Principle

CVF should not become a translation product.

CVF should become a reliable control product that lets Vietnamese non-coders
work in Vietnamese while agents receive a precise, structured Spec.

The readout should answer four practical questions:

1. What did CVF understand?
2. What should I copy to the agent?
3. What did governance allow or not allow?
4. What should I do next?

## Proposed Scope

VI5 should add a deterministic `localizedNonCoderReadout` surface derived from
existing `specFirstMediation`, governance receipt, and route response data.

Minimum fields:

- `contractVersion`
- `language`
- `primaryActionLabel`
- `primaryActionText`
- `copyReadySpecLabel`
- `copyReadySpec`
- `whatCvfUnderstood`
- `whatCvfDid`
- `whatToDoNext`
- `evidenceSummary`
- `rawEvidenceLabel`
- `rawEvidenceAvailable`
- `advisoryBoundaryText`
- `implementationBoundaryText`
- `reviewQuestions`

The readout should be short enough for a non-coder to scan before opening raw
technical evidence.

## Non-Goals

This roadmap does not authorize:

- broad Vietnamese translation tuning;
- multi-language expansion beyond Vietnamese and English;
- provider prompt rewrites;
- provider adapter changes;
- provider routing changes;
- receipt envelope breaking changes;
- changing model output validation;
- new workflows or workflow scale;
- new external skill imports;
- certified skill pack publication;
- hiding raw technical evidence;
- hosted readiness;
- public release readiness;
- production readiness;
- tool, MCP, browser, database, CLI, or spend execution.

## Work Plan

Proposed sequence after operator approval and fresh GC-018:

1. Define `localizedNonCoderReadout.vi5.v1` as a deterministic contract.
2. Build readout from existing `specFirstMediation`, receipt, selected
   template, related skill, and provider/model metadata.
3. Add Vietnamese text for CVF-controlled labels when `outputLanguage=vi`.
4. Add English fallback when `outputLanguage=en` or language is unknown.
5. Add a `copyReadySpecLabel` and a clear boundary that the Spec is the agent
   handoff, not loose chat.
6. Add short `whatToDoNext` guidance:
   - review the summary;
   - copy the Spec;
   - approve or edit before implementation;
   - open raw evidence only for audit/debug.
7. Add unit tests for Vietnamese, English, advisory lane, and missing/clarify
   cases.
8. Add one route-level test proving the field is emitted.
9. Optionally run one live Vietnamese Strategy request for operator review,
   only after deterministic tests pass.

## Acceptance Criteria

Minimum acceptance:

- Vietnamese user can identify the copy-ready Spec without reading raw JSON.
- The readout says what CVF understood in Vietnamese.
- The readout says what CVF did in Vietnamese.
- The readout says what to do next in Vietnamese.
- The readout states advisory LLM output is source-only.
- The readout states implementation still requires governed route or explicit
  approval.
- Raw technical evidence remains available and is not removed.
- No provider adapter, provider routing, or receipt envelope change.
- Existing L1 `specFirstMediation` tests still pass.

Operator acceptance for moving the usability gate:

- A Vietnamese non-coder can read the readout without Codex explaining it.
- The user can point to the exact Spec block to copy to an agent.
- Mixed-language provider output no longer blocks understanding because the
  CVF-owned readout explains the action path.

## Verification Or Evidence

Required deterministic verification:

```text
npm run test:run -- src/lib/localized-noncoder-readout.test.ts src/lib/spec-first-mediation.test.ts src/app/api/execute/route.test.ts
npm run check
```

Optional live proof after deterministic pass:

- one Vietnamese `/api/execute` Strategy request;
- provider/model recorded;
- receipt recorded;
- `localizedNonCoderReadout.language=vi`;
- operator reviews `output`, `specFirstMediation.normalizedExecutionSpec`, and
  `localizedNonCoderReadout`.

Live failures must follow:

`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

## Operator Review Rubric

The operator should answer before implementation:

1. Is this problem worth fixing now, or is L1 good enough?
2. Should CVF optimize only the readout/action layer, not the full provider
   output?
3. What labels should the Vietnamese user see for:
   - copy-ready Spec;
   - evidence summary;
   - raw technical evidence;
   - advisory source-only note;
   - implementation boundary?
4. What would make the sample PASS from a non-coder viewpoint?
5. What should remain English because agents/auditors need exact terms?

## Decision / Recommendation / Disposition

Decision: proposed for operator review.

Recommendation: proceed only if the operator agrees that the remaining
Vietnamese issue is an action/readout clarity problem, not a broad translation
problem.

Disposition: do not implement until fresh GC-018 and work order are opened.

## Claim Boundary

This roadmap does not claim that VI5 is implemented, that Vietnamese UX is
fixed, that the Real Non-Coder Usage Test has passed, or that CVF is public,
hosted, production, or multilingual-release ready.

It only defines a bounded candidate tranche for localized non-coder readout
consolidation.
