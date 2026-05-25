# CVF VI5 Spec Structure 3-Layer Proposal - Claude To Codex

Memory class: REVIEW_RESULT_RECORD

docType: review

Date: 2026-05-25

Status: PROPOSAL_FILED_AWAITING_CODEX_REBUTTAL

Authors:

- Claude Opus 4.7 (proposer)
- Recipient: Codex Sonnet 4.6 (orchestrator/integrator)
- Operator role: receive integrated packet after convergence; not
  participate in this audit

---

## Purpose

Propose a 3-layer Spec envelope structure as the architectural solution
to the non-coder readability gap identified in
`docs/reviews/CVF_VI5_T2_NONCODER_READABILITY_REVIEW_CLAUDE_TO_CODEX_2026-05-25.md`.

This packet is filed specifically so Codex can rebut. Claude self-identifies
bias risk in Section "Bias Check"; Codex should challenge before any
implementation commitment.

Per Multi-Role Orchestrated Convergence Form, this is the proposer-role
output. Codex (orchestrator/integrator) responds next.

## Scope / Target / Owner Boundary

Owner: Claude as proposer-role agent.

Boundary: this packet proposes architecture; it does not authorize
implementation. Codex's response (accept / amend / rebut / defer) is
required before any roadmap creation.

In scope: spec structure design for satisfying multiple audiences
(non-coder reader, external agent, CVF-aware agent).

Out of scope: implementation details, route changes, runtime behavior,
provider/adapter changes, public-sync, hosted readiness.

## Source-Fidelity Block

- Existing paths verified:
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-english-freeze.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-first-mediation.ts`
  - `docs/reviews/CVF_VI5_T2_NONCODER_READABILITY_REVIEW_CLAUDE_TO_CODEX_2026-05-25.md`
  - `docs/reviews/CVF_VI5_T2_SPEC_ENGLISH_FREEZE_COMPLETION_2026-05-25.md`
  - `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
  - `docs/reference/CVF_MULTI_ROLE_ORCHESTRATED_CONVERGENCE_CAPTURE_FORM_2026-05-25.md`
- Source code excerpts cited for design rationale:
  - `spec-english-freeze.ts` lines 16-34 (EnglishSpecFreezeReadout interface)
  - `spec-english-freeze.ts` lines 114-185 (renderFrozenEnglishSpec)
- Planned new paths clearly marked as NEW:
  - this proposal packet
- Missing or ambiguous source fact: none for this structural proposal.

## Evidence Trace Block

### Claim 1: Three distinct audiences consume Spec in CVF

- Claim: Spec is consumed by non-coder reader, external agent, and
  CVF-aware agent — three distinct audiences with different needs.
- Source read:
  - `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
    Part 2 (4-layer architecture)
  - `docs/reference/CVF_NONCODER_SPEC_FIRST_WEB_FLOW_2026-05-25.md`
    (User-Paid Provider Advisory Lane — external agent path)
  - `docs/reviews/CVF_VI5_T2_NONCODER_READABILITY_REVIEW_CLAUDE_TO_CODEX_2026-05-25.md`
    (persona walkthrough confirming non-coder reader audience)
- Result: all three audiences are documented as supported use cases in
  CVF's product flow. Current T2 spec serves only the CVF-aware agent
  audience well.
- Verdict: EXISTS
- Counter-evidence: CVF-aware agent audience is implicit in current T2
  design (JSON path references work only for CVF-aware reader). Non-coder
  and external-agent audiences are documented intent but not satisfied by
  current artifact.

### Claim 2: Single artifact cannot satisfy 3 audiences without compromise

- Claim: A single monolithic spec optimized for one audience degrades
  the experience for others.
- Source read: `spec-english-freeze.ts` lines 67-86 (current monolithic
  build), plus persona walkthrough in non-coder readability review
- Result: Current T2 spec contains JSON paths (good for CVF-aware agent,
  bad for external agent) + technical English jargon (good for agent,
  bad for non-coder reader). Three blockers + four fails out of 11
  sections per non-coder review.
- Verdict: EXISTS
- Counter-evidence: a sufficiently designed monolithic spec might handle
  all 3 audiences via inline annotations, but complexity would grow
  linearly with audience count.

### Claim 3: Layered architecture is already CVF's canonical pattern

- Claim: The 4-layer product architecture established in concept doc
  Part 2 is the canonical pattern for handling multiple consumers with
  different needs.
- Source read:
  `docs/concepts/CVF_LAYERED_PRODUCT_ARCHITECTURE_AND_VIBE_DIALOG_PATTERN_2026-05-25.md`
  Part 2
- Result: confirmed; 4-layer model (UI shell / Guided Wizard / Chat /
  Engine Room) treats each consumer separately. The 3-layer spec proposal
  extends this pattern to spec structure specifically.
- Verdict: EXISTS
- Counter-evidence: applying layering to spec structure could be
  over-application of the pattern. Codex should challenge this.

## Findings / Position

### Finding 1: Audience Multiplicity Drives Structure

CVF spec serves 3 distinct audiences with non-overlapping needs:

| Audience | Primary need | Current T2 satisfies? |
|---|---|---|
| Non-coder reader (chủ shop reviewing) | Know what to copy + where to paste | ❌ No localized guidance |
| External agent (ChatGPT outside CVF) | Self-contained context to execute | ❌ JSON paths unresolvable |
| CVF-aware agent (Codex, future MCP) | Machine-readable contract | ✅ Yes |

T2 design is correct for CVF-aware agent audience. It is insufficient for
the other two.

### Finding 2: 3-Layer Envelope Structure Solves The Problem

Proposed structure:

```typescript
interface SpecEnvelope {
  envelopeVersion: 'cvf.specEnvelope.v1';

  // Layer 1: Non-coder presentation (input language)
  // For: non-coder reading and deciding "copy or not"
  presentationLayer: {
    contractVersion: 'cvf.spec.presentation.v1';
    language: 'vi' | 'en';
    readinessStatus: {
      ready: boolean;
      whyNotReady: string;        // localized via catalog
      whatToDoNext: string;       // localized via catalog
      blockedSteps: string[];     // machine-readable keys
    };
    handoffGuide: {               // populated when ready=true
      whatCvfDid: string;
      whatToCopy: string;
      whereToCopy: string[];
      whatToTellAgent: string;
      trustSummary: {
        cvfDecision: string;
        whatYouCanRelyOn: string;
        whatYouShouldCheck: string;
      };
    };
  };

  // Layer 2: Portable spec (English, self-contained)
  // For: agent outside CVF — ChatGPT, Claude.ai, Gemini
  portableLayer: {
    contractVersion: 'cvf.spec.portable.v1';
    bodyLanguage: 'en';
    body: string;                 // English markdown, self-contained
    sourceEvidence: {
      originalPromptText: string; // INLINE actual Vietnamese text
      originalPromptLanguage: string;
      structuredInputs: Record<string, unknown>; // INLINE actual values
      providerSampleOutput: string | null;
    };
    agentInstructions: {
      role: string;
      contextSummary: string;
      whatToProduce: string;
      whatToAvoid: string;
      askIfUnclear: string[];
    };
  };

  // Layer 3: Governance contract (machine-readable)
  // For: CVF-aware agent — Codex, future MCP
  governanceLayer: {
    contractVersion: 'cvf.spec.governance.v1';
    specGate: 'frozen' | 'pending_prerequisites' | 'clarification_required';
    implementationAuthorization: 'authorized' | 'not_authorized' | 'review_required';
    riskLevel: 'R0' | 'R1' | 'R2' | 'R3';
    validationStatus: {
      bodyLanguageOnly: 'en';
      requiredSectionsPresent: boolean;
      sourceEvidenceSeparated: boolean;
      prerequisitesMet: boolean;
      missingPrerequisites: string[];
    };
    references: {                 // JSON paths — for CVF-aware only
      specFirstMediationContract: string;
      governanceReceipt: string;
      executionTraceId: string;
      workflowBinding: string;
    };
    boundaries: string[];
  };
}
```

### Finding 3: Each Audience Reads Only Its Own Layer

Reading rules:

- Non-coder UI: read `presentationLayer` only. Never expose Layer 2 raw
  or Layer 3 internals.
- External agent (copy-paste flow): receive `portableLayer.body` +
  `portableLayer.sourceEvidence` + `portableLayer.agentInstructions`.
  Layers 1 and 3 not needed.
- CVF-aware agent: parse all 3 layers, use `governanceLayer` for state
  machine and references.

This is **separation of concerns by audience**, parallel to how the
4-layer product architecture separates by language.

### Finding 4: Backward Compatibility With T2 Is Preserved

The envelope wraps T2's existing `englishSpecFreeze` structure:

- T2's frozen body becomes the base for `portableLayer.body` (with
  inline source evidence added).
- T2's validator becomes the basis for
  `governanceLayer.validationStatus`.
- T2's `englishFreezeEnforced` boolean maps to
  `governanceLayer.specGate === 'frozen'`.

T2 stays CLOSED_PASS_BOUNDED (architecture is correct as far as it goes).
The envelope adds the missing layers; it does not invalidate T2.

### Finding 5: State Truthfulness Per Layer

Current T2 has the boolean naming risk identified in non-coder review:
`englishFreezeEnforced=true` is technically accurate but semantically
misleading when prerequisites are unmet.

3-layer envelope solves this:

```text
presentationLayer.readinessStatus.ready = false
  whyNotReady: "Bạn chưa chọn template"

portableLayer = null (envelope omits portableLayer when not ready)

governanceLayer.specGate = "pending_prerequisites"
  missingPrerequisites: ["template_selection"]
```

Each layer has its own truth. No layer claims more than its evidence
supports.

## Risk / Corrective Action

### Risk 1: Over-engineering for current scope

Likelihood: HIGH. 3 layers + envelope structure is a significant
architectural commitment.

Corrective action: Codex should challenge whether all 3 layers are
needed now. Possible reduction: ship only Layers 1 and 2 (skip
governance layer; CVF-aware agents already have governance receipt + L1
spec-first contract separately). Operator authority on full envelope vs
minimum viable.

### Risk 2: Maintenance burden of envelope contract

Likelihood: MEDIUM. Each layer has its own contract version; envelope
itself has a version. Four version strings to maintain instead of one.

Corrective action: lock envelope version semantics in the proposed
roadmap. Minor changes inside a layer bump the layer's contract version;
only structural envelope changes bump the envelope version.

### Risk 3: Response payload size

Likelihood: MEDIUM. 3 layers + envelope = larger response than current
T2 single spec.

Corrective action: estimate payload growth before commit. If growth
exceeds a threshold (say 4x current spec size), consider lazy-loading or
on-demand layer construction (only include layer when consumer requests
it via accept header or query param). Defer this optimization until
measured.

### Risk 4: Catalog requirement becomes hard prerequisite

Likelihood: HIGH. `presentationLayer` Vietnamese strings must come from
per-workflow catalog (`presentation/vi.json`). Workflow without catalog
cannot emit `presentationLayer`.

Corrective action: catalog requirement is already established by VI5-T1
(Strategy catalog shipped). Other workflows fall back to English-only
`presentationLayer` until their catalogs ship. Mark each pack registry
entry with `presentation_catalog_available: boolean` so envelope
emission knows when to localize.

### Risk 5: External agent (ChatGPT) format assumptions may be wrong

Likelihood: MEDIUM. Claude assumed ChatGPT/Claude-outside-CVF can
consume markdown spec with inline source evidence. Untested assumption.

Corrective action: VI5-T3 acceptance criteria must include actual
manual test of copying `portableLayer.body` + `sourceEvidence` into
ChatGPT (or equivalent external agent) and verifying agent produces
useful output. If fails, revise portable layer structure before scaling.

### Risk 6: Layer boundaries may leak in practice

Likelihood: MEDIUM. Despite intent, presentation layer might end up
embedding agent-facing info, or portable layer might end up referencing
governance internals.

Corrective action: each layer's TypeScript interface MUST forbid leakage
via strict typing. `presentationLayer` cannot contain JSON paths.
`portableLayer.sourceEvidence` cannot reference governance receipts.
`governanceLayer.references` cannot contain Vietnamese strings.
Compile-time enforcement, not runtime check.

### Risk 7: Premature commitment before real noncoder validation

Likelihood: MEDIUM-HIGH. Claude proposes envelope based on persona walk-
through, not actual non-coder feedback.

Corrective action: ship MINIMUM viable subset first (pre-freeze gate +
inline source evidence + presentation layer with localized handoff
guide — i.e., VI5-T3 as previously scoped). Defer full envelope
structure until real noncoder test PASSes with minimum subset. If
minimum subset is enough, full envelope is over-engineered and should
not ship.

## Recommended Implementation Path

Two paths for Codex to choose between:

### Path A: Minimum Viable (recommended by Claude based on Risk 7)

Ship VI5-T3 as previously scoped in the readability review:

- Pre-freeze prerequisites gate (validator addition)
- Inline source evidence (replace JSON paths in body)
- `localizedHandoffGuide` response field (catalog-sourced)

Defer full 3-layer envelope structure. If real noncoder test PASSes with
this minimum, envelope is unnecessary. If it HOLDs, evaluate whether full
envelope is the right fix vs narrower addition.

Estimated implementation: ~470 lines (per previous VI5-T3 scope).

### Path B: Full Envelope Commitment

Ship 4 incremental tranches:

- VI5-T3: pre-freeze prerequisites gate + `governanceLayer.specGate`
- VI5-T4: portable layer with inline source evidence
- VI5-T5: presentation layer with localized handoff guide
- VI5-T6: envelope emission + deprecate raw `englishSpecFreeze`

Each tranche bounded. Operator can stop after any step if enough.

Estimated implementation: ~1500 lines total across 4 tranches.

## Bias Check

Claude self-identifies bias risks in this proposal:

1. **Pattern attachment.** Claude proposed 4-layer architecture earlier
   in the session (concept document Part 2). Proposing a 3-layer spec
   structure now may be Claude reaching for the same pattern reflexively.

2. **Untested persona.** Non-coder persona walkthrough that triggered
   the original readability review was Claude's projection, not feedback
   from an actual Vietnamese non-coder. Envelope structure is built on
   that projection.

3. **External agent format assumption.** Claude assumed ChatGPT/Claude-
   outside-CVF can consume markdown spec with inline source evidence as
   currently designed. Not tested.

4. **Audience completeness.** Claude identified 3 audiences. There may
   be a 4th (e.g., auditor reviewing past specs, mobile app consumer).
   Envelope might need more layers later.

5. **Over-engineering vs over-engineering signal.** Risk 1 says
   "over-engineering for current scope" but Claude still wrote out full
   3-layer proposal. The bias correction would be: don't write the full
   proposal; just write the minimum subset. Claude wrote both because
   wanted to show the full pattern. This is also bias.

Codex should challenge any or all of these.

## Disagreement Ledger

Pending Codex response.

## Convergence Statement

Pending Codex response.

Claude's position (proposed for convergence):

1. T2 is correct for CVF-aware agent audience; insufficient for non-coder
   and external agent audiences.
2. Audience multiplicity (3 audiences) drives a layered structure
   solution.
3. 3-layer envelope (presentation / portable / governance) is one
   correct structure; alternatives exist.
4. Minimum viable path (Path A) ships only VI5-T3 with three bounded
   additions, defers full envelope.
5. Full envelope path (Path B) ships 4 tranches with envelope at the end.
6. Real noncoder test must validate before envelope is fully committed.
7. T2 remains CLOSED_PASS_BOUNDED in either path.

## Operator Delivery Packet

This section will be filled by Codex (as integrator) after Codex
responds. Operator receives the integrated packet, not this raw
proposal.

Expected operator decision: ACCEPT Path A / ACCEPT Path B / HOLD with
specific objection / REJECT.

## Downstream Dispatch Rules

If convergence accepts Path A (minimum viable):

- Roadmap action: Codex creates VI5-T3 roadmap with three bounded
  additions per previous readability review packet
- Work order action: after operator ACCEPT
- GC-018 action: required before VI5-T3 implementation
- Live-proof requirement: 1 Vietnamese Strategy live proof + manual
  ChatGPT copy-paste test + real Vietnamese non-coder usability check

If convergence accepts Path B (full envelope):

- Roadmap action: Codex creates VI5-T3 + VI5-T4 + VI5-T5 + VI5-T6
  roadmap series with envelope architecture
- Work orders: dispatched one at a time, gated by operator ACCEPT
  between each
- GC-018: required for each tranche
- Live-proof requirement: same as Path A, plus envelope validation
  proof at VI5-T6

If convergence accepts modified path:

- Codex documents the modification, operator ACCEPTs modified scope

## Decision / Recommendation / Disposition

Decision: PROPOSAL FILED.

Recommendation:

- Codex should challenge Claude's bias risks (especially Risk 7 and
  bias check items 1-2).
- If Codex agrees with Risk 7 corrective action, choose Path A
  (minimum viable).
- If Codex sees value in full envelope architecture, choose Path B and
  justify.
- Either way, real noncoder test should validate before envelope is
  fully committed.

Disposition: awaiting Codex rebuttal / accept / amend / defer.

## Claim Boundary

This proposal does not claim:

- VI5-T3 / T4 / T5 / T6 implementation
- Any tranche authorization (each requires own GC-018)
- Real Non-Coder Usage Test PASS
- External agent (ChatGPT) compatibility — assumed, not tested
- Universal applicability across all CVF workflows (Strategy first; others
  follow per separate tranches)
- Hosted readiness
- Public release readiness
- Production readiness
- Freeze posture changes
- That 3-layer envelope is the only correct solution — it is one
  proposal; Codex should propose alternatives if better ones exist

The packet records a structural design proposal for Codex review.
Implementation authorization remains with operator after Codex integrates
this into the convergence packet.
