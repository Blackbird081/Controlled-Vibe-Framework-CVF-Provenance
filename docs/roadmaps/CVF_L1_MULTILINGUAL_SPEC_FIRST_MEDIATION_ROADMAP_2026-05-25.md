# CVF L1 Multilingual Spec-First Mediation Roadmap

Memory class: ROADMAP_RECORD

Date: 2026-05-25

Status: PROPOSED_NEXT_TRANCHE

## Purpose

Define the next bounded tranche after the real non-coder usage test HOLD:
support native-language non-coder input and output while preserving a stable
English/structured execution brief for LLMs and agents.

## Target / Source

Target owner surface: `/api/execute` user-facing request/result contract and
response-level evidence readout.

Source result:

`docs/reviews/CVF_REAL_NONCODER_USAGE_TEST_RESULT_2026-05-25.md`

## Scope / Methodology

Scope: language mediation and spec-first packaging only.

Methodology:

1. Detect or declare the user's source language.
2. Preserve the original user prompt.
3. Create a normalized CVF Execution Spec for agents.
4. Use English as the preferred internal working language when it improves
   agent consistency.
5. Return the user-facing output and evidence summary in the user's language.
6. Keep raw technical evidence available as an expandable/debug layer.

## Scope / Target / Owner Boundary

Owner: product UX and governed execution contract.

Boundary: this roadmap does not authorize implementation by itself. A fresh
value-screened GC-018 and work order are required before code changes.

Forbidden without fresh authorization:

- provider adapter changes;
- receipt envelope breaking changes;
- broad prompt tuning;
- hosted readiness;
- public release readiness;
- new workflow/provider scale;
- automatic tool/MCP/database/browser execution.

## Problem Statement

CVF currently has proof-backed governance evidence, but public non-coder users
may not write prompts in English. LLMs and agents often perform best with a
clear English execution brief, while Vietnamese users need input and output in
Vietnamese.

If CVF exposes raw English-heavy technical evidence as the default output, it
can be correct but still unusable.

## Product Direction

Preferred model:

```text
native user input
-> preserved original prompt
-> normalized CVF Execution Spec
-> English internal execution brief when needed
-> governed provider call
-> localized user-facing answer
-> localized evidence summary + raw receipt
```

Fallback early-phase model:

```text
user supplies English prompt
-> CVF emits standardized CVF Execution Spec first
-> agents implement from the spec, not from ad hoc chat wording
-> user-facing result may remain localized or bilingual
```

## Required Contract Fields

The next tranche should introduce a stable language mediation readout with at
least:

- `sourceLanguage`
- `workingLanguage`
- `outputLanguage`
- `originalPromptPreserved`
- `normalizedExecutionSpec`
- `translationAmbiguity`
- `clarificationRequired`
- `localizedEvidenceSummary`
- `rawTechnicalEvidenceAvailable`

## Non-Goals

This roadmap does not authorize:

- broad translation quality tuning;
- changing provider adapters;
- changing provider routing;
- changing the receipt envelope in a breaking way;
- adding new workflow/provider scale;
- hiding raw governance evidence;
- claiming hosted readiness;
- claiming public release readiness;
- executing tools, MCP, database actions, browser actions, or cost/spend
  actions.

## CVF Execution Spec Requirements

The normalized spec should be Markdown-compatible and agent-readable:

- original user request;
- normalized objective;
- assumptions;
- constraints;
- risk level;
- allowed actions;
- forbidden actions;
- expected output schema;
- evidence requirements;
- review gate;
- open clarification questions.

This spec is the shared contract for Codex, Claude, DeepSeek, CLI, MCP, and
future agents before implementation.

## Work Plan

Proposed L1 implementation sequence after fresh GC-018:

1. Define the language mediation readout contract and CVF Execution Spec
   minimum schema.
2. Add deterministic language/source/output metadata without provider calls.
3. Add localized short evidence summary generation from existing VI4 fields.
4. Wire the spec/readout into the existing Strategy `/api/execute` response
   without changing provider adapters or receipt envelopes.
5. Add unit coverage for Vietnamese, English, and ambiguous-language cases.
6. Run one live Vietnamese Strategy proof and record receipt, provider/model,
   localized output, and raw evidence availability.

## Acceptance Criteria

Minimum acceptance for L1:

- Vietnamese input remains valid; user is not forced to write English.
- The original prompt is preserved.
- The normalized CVF Execution Spec is emitted and readable by agents.
- User-facing answer is Vietnamese when `sourceLanguage=vi`.
- Evidence summary is short and Vietnamese-readable by default.
- Raw VI4/technical evidence remains accessible.
- Live Alibaba-compatible proof passes with one Vietnamese Strategy prompt.
- The receipt/readout records source, working, and output language.

## Verification Plan

Targeted tests:

- Vietnamese prompt -> normalized English/CVF spec -> Vietnamese answer.
- English prompt -> English spec -> English answer.
- Ambiguous Vietnamese prompt -> clarification required, no silent risky
  translation.
- Raw technical evidence remains present but not the default non-coder summary.

Live proof:

- one `/api/execute` Strategy workflow call with Vietnamese input;
- provider/model recorded;
- receipt id recorded;
- localized evidence summary inspected.

## Decision / Recommendation / Disposition

Decision: recommended next tranche before hosted readiness.

Recommendation: open `L1_MULTILINGUAL_SPEC_FIRST_MEDIATION` with fresh GC-018
and implement before any public non-coder readiness claim.

Disposition: roadmap ready for authorization, not yet dispatched.

## Claim Boundary

This roadmap is a product and contract direction. It does not claim
multilingual runtime behavior, translation quality, hosted readiness, public
readiness, production readiness, or broad provider stability.
