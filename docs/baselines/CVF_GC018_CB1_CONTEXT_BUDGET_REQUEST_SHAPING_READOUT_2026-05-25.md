# CVF GC-018 CB1 Context Budget Request Shaping Readout

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT

docType: baseline

Date: 2026-05-25

---

## Purpose

Authorize CB1 as a bounded implementation tranche that absorbs the next
high-value legacy knowledge identified by LH1: context budgeting, relevance
filtering, brief normalization, reverse-brief recovery, and context packaging.

The goal is to make `cvf skill select <request> [--json]` report not only which
certified pack fits, but whether the user request has enough useful context to
proceed, needs clarification, should be compacted, or is contaminated by
implementation-heavy pseudo-brief material.

## Scope / Target / Owner Boundary

Owner surface:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/commands/cvf-skill.test.ts`

Allowed:

- deterministic request-context readout for product skill pack selection;
- context budget tier classification;
- relevance/noise/contamination signals;
- missing-context and recommended-next-action readout;
- tests proving ready, clarification, compaction, and contamination behavior.

Forbidden:

- LLM scoring;
- runtime execution;
- provider/API calls;
- `/api/execute` changes;
- receipt-envelope changes;
- memory, MCP, database, or tool execution;
- public-sync, hosted readiness, production readiness, or freeze release.

## Source / Predecessor Evidence

- `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- `.private_reference/legacy/CVF ADD/caveman/CVF_CONTEXT_BUDGETING_PROTOCOL.md`
- `.private_reference/legacy/CVF ADD/caveman/CVF_RELEVANCE_FILTERING_SPEC.md`
- `.private_reference/legacy/CVF ADD/caveman/CVF_CONTEXT_COMPACTION_PROTOCOL.md`
- `.private_reference/legacy/CVF ADD/Human System Harness/CVF_REVERSE_BRIEF_PROTOCOL.md`
- `.private_reference/legacy/CVF ADD/Human System Harness/CVF_BRIEF_NORMALIZATION_SPEC.md`
- `.private_reference/legacy/CVF ADD/Workflow GoClaw/CVF_CONTEXT_PROFILE_MODEL.md`
- `.private_reference/legacy/CVF ADD/Workflow GoClaw/CVF_CONTEXT_PACKAGING_POLICY.md`
- `.private_reference/legacy/CVF ADD/Workflow GoClaw/CVF_CONTEXT_GUARDRAIL_RULEBOOK.md`
- `docs/reviews/CVF_C8_PRODUCT_SKILL_PACK_SELECTION_READOUT_COMPLETION_2026-05-25.md`

## Decision / Baseline / Proposed Tranche

Decision: proceed with CB1 as deterministic readout only.

Baseline: C8 can select a certified pack, but it does not yet report whether
the request itself has adequate problem, constraint, artifact, acceptance, and
risk context.

Proposed output:

- `cvf.productSkillPackRequestContext.v1` nested in the existing selection
  readout;
- budget tier: `minimal`, `standard`, or `expanded`;
- readiness: `ready`, `needs_clarification`, `needs_context_compaction`, or
  `blocked_contaminated_brief`;
- detected signals, missing signals, contamination flags, noise flags, and
  deterministic next action.

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - `caveman` - 11 files
  - Human System Harness - 11 files
  - Workflow GoClaw - 11 files
- Prior absorption evidence resolved:
  - LH1 closeout ledger
  - C8 completion
  - WC-3 scan map
- Detailed source files used:
  - `CVF_CONTEXT_BUDGETING_PROTOCOL.md`
  - `CVF_RELEVANCE_FILTERING_SPEC.md`
  - `CVF_CONTEXT_COMPACTION_PROTOCOL.md`
  - `CVF_REVERSE_BRIEF_PROTOCOL.md`
  - `CVF_BRIEF_NORMALIZATION_SPEC.md`
  - `CVF_CONTEXT_PROFILE_MODEL.md`
  - `CVF_CONTEXT_PACKAGING_POLICY.md`
  - `CVF_CONTEXT_GUARDRAIL_RULEBOOK.md`
- Source families skipped:
  - none from the CB1 scope
- File-level accepted value:
  - context tiers and prioritization from caveman;
  - relevance/noise filtering from caveman;
  - compaction failure rules from caveman;
  - brief contamination and missing-field recovery from Human System Harness;
  - profile/packaging/guardrail invariants from Workflow GoClaw.
- Owner-surface normalization:
  - all accepted value maps into Governance CLI product-skill-pack selection
    readout; no new runtime packager is created.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: deterministic context readout fields and tests.
  - DEFER_DEMAND_GATED: runtime context builder, memory injection, tool/skill
    affordance packaging, profile escalation execution.
  - REJECT_DIRECT: prompt/runtime profile replacement or hidden context
    mutation.
- Adversarial roles completed:
  - Implementer: add the smallest nested readout to existing C8 selection.
  - Skeptic/Auditor: do not claim real context packaging or reverse-brief
    execution.
  - Product/Operator Advocate: users/agents need to know why a request is not
    ready before wasting provider calls.
  - Safety/Boundary Owner: no memory/tool/MCP/provider execution opens.
- Thin proof target:
  - deterministic readout plus focused CLI tests.
- Blind-spot verdict: CLEAR.

## Evidence / Required Evidence / Verification

Required:

- focused `cvf skill` tests PASS;
- Governance CLI TypeScript check PASS;
- active state and handoff guard PASS.

Live proof is not required. CB1 does not assert provider, route, memory, tool,
or live governance behavior.

## Claim Boundary / Approval Gate

CB1 may claim only deterministic request-context readout inside Governance CLI
skill selection. It does not claim runtime context packaging, reverse-brief
execution, provider behavior, live governance behavior, memory injection, hosted
readiness, production readiness, public release readiness, or freeze release.
