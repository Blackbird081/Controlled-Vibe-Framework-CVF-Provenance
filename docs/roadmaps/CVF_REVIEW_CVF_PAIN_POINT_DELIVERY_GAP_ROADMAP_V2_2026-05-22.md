# CVF Review-CVF Pain Point Delivery Gap Roadmap V2

Memory class: FULL_RECORD

Status: ACTIVE_ROADMAP_AUTHORIZED_FOR_T1_DISPATCH

docType: roadmap

Date: 2026-05-22

Author: Claude (planning role), corrected after Codex blocking review

Supersedes: `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_2026-05-22.md`

---

## Purpose

Final unified roadmap for closing the Review CVF.md delivery gap. V2
resolves all six findings from the Codex blocking review and is the
authoritative steering record for the five-tranche pain-point delivery
program from this point forward.

This is now the active roadmap of record. The V1 draft is superseded.

---

## Authorization or Decision

V2 is authorized as the **active roadmap** for the pain-point delivery
program. Operator authorized 2026-05-22 after Codex blocking review at
`docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_CODEX_REVIEW_2026-05-22.md`.

Authorization scope:

- T1 may be dispatched as a work order under a separate candidate-specific
  GC-018.
- T2–T5 remain pending operator authorization. Each requires its own
  GC-018 before any implementation begins.
- T3 and T4 additionally require explicit **blocked-work-override** language
  from the operator before GC-018 (see "Blocked-Work Overrides" below).

Predecessor artifacts (mandatory reading):

- Predecessor audit: `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- Codex blocking review: `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_CODEX_REVIEW_2026-05-22.md`
- Source of original deliverables: `.private_reference/legacy/CVF 17.05/Review CVF.md`

---

## Why This Tranche / Purpose

The 17.05 Review CVF.md identified eight pain points (A–H) with concrete
deliverables. Six closure reviews on 2026-05-20 marked every pain point
CLOSED, but the predecessor audit shows the bounded closures either
rejected the deliverable, narrowed it to a contract-only artifact, or
partitioned it as "product expansion".

V1 of this roadmap was directionally right but had internal
inconsistencies and blocked-work-class collisions. V2 fixes those and
re-anchors planning against the original review's deliverable list.

---

## Scope

In scope:

- Five tranches (T1–T5) targeting gaps recorded in the predecessor audit.
- Per-tranche objectives, deliverables, acceptance criteria, claim
  boundaries, pre-conditions, and (where required) blocked-work-override
  declarations.
- Sequencing rules aligned with the original review's four strategic
  phases.
- Anti-pattern guardrails preventing recurrence of closure-by-rejection,
  closure-by-redefinition, contract-only closure, and implicit scope
  inflation.

Out of scope:

- Reopening A1/C1/D1/E1/G1/H1 closure reviews. Their bounded contracts
  remain valid for what each was scoped to do.
- Lifting any freeze, releasing any frozen surface, or changing the
  one-surface freeze-release rule.
- Any public-sync update.
- Any release claim, hosted readiness claim, or matured-kernel claim.
- Maika child-data, photo, or vision proof (separately demand-gated).
- Broader provider stability (separately demand-gated).
- D-06 kernel-owner replacement, D-07 global freeze lift.

---

## Non-Goals

- V2 is not a release plan.
- V2 is not a marketing artifact.
- V2 does not promise any tranche will succeed; it only authorizes
  T1 dispatch and pre-positions T2–T5.
- V2 does not invalidate the existing six 2026-05-20 closure reviews; it
  proposes complementary delivery work.

---

## Blocked-Work Overrides

Active session state (as of HEAD `5279db51`) blocks several work classes
relevant to this roadmap:

- `new_governance_semantics`
- `new_role_taxonomies`
- `new_policy_risk_guard_engines`
- `new_receipt_envelopes`
- `new_memory_tiers_beyond_lane_h_scope`
- `new_provider_execution_semantics`

Per Codex Finding 3, ordinary GC-018 is **not sufficient** to authorize
tranches that touch these classes. Each affected tranche requires
explicit operator-signed override language in its GC-018 baseline.

Per-tranche override map:

| Tranche | Blocked classes touched | Override required |
| --- | --- | --- |
| T1 | none (contract + validator + reference pack only) | no override required |
| T2 | none (additional certified packs only) | no override required |
| T3 | `new_receipt_envelopes` (adding `workflowComposition` field to `GovernanceEvidenceReceipt`) | required |
| T4 | `new_provider_execution_semantics` (unified `ProviderMethodContract`, `stream()` + `json_mode()` adapters) | required |
| T5 | `new_memory_tiers_beyond_lane_h_scope` (task-tier runtime wiring beyond H1 classifier scope) | required |

If the operator declines any override, the corresponding tranche is
split into a separately demand-gated roadmap candidate or canceled. T1
and T2 do not depend on any override and may proceed under ordinary
GC-018.

---

## Work Plan

### Tranche Sequencing Rule

Tranches execute in order T1 → T5 unless the operator authorizes a
reordering in writing. The order follows the review's strategic priority
(Phase 1 Stabilization → Phase 2 Runtime Maturity → Phase 3
Productization → Phase 4 Operational Intelligence), prioritized by the
review's statement that PROBLEM B was "priority cao nhất".

Within each tranche, the chain is: GC-018 baseline → work order → Codex
Orchestrator → Reviewer rebuttal → Implementer → Auditor completion
review.

### T1 — Capability Intake Pipeline + Complete Pack Artifact Set

**Original review section:** "CAPABILITY INTAKE PIPELINE" and "SKILL
CERTIFICATION SYSTEM" (Review CVF.md lines 466–525).

**Why first:** The review explicitly named this as the architecture
missing from CVF. Without it, T2 (skill packs) has no machine-readable
surface and T3 (workflow composition) has nothing to compose.

**Codex Finding 1 resolution:** V1 listed 6 JSON schemas but omitted the
`workflow.spec` and `failure.recovery` artifacts that the original review
named. V2 expands T1 to certify the **complete eight-artifact set**.

**Concrete deliverables:**

- `governance/toolkit/05_OPERATION/CVF_CAPABILITY_INTAKE_PIPELINE_GUARD.md`
  defining intake → normalization → risk audit → policy binding →
  certification → workflow mapping → governed runtime as a governed surface
  contract.
- JSON schema set under `governance/schemas/skill-pack/`:
  - `skill.meta.schema.json`
  - `risk.profile.schema.json`
  - `authority.scope.schema.json`
  - `execution.boundary.schema.json`
  - `receipt.schema.schema.json`
  - `workflow.binding.schema.json`
  - `workflow.spec.schema.json` (added in V2)
  - `failure.recovery.schema.json` (added in V2)
- A validator script `scripts/validate_skill_pack_certification.py` that
  takes a candidate skill pack directory, runs **all eight** schema
  validations, and emits a deterministic pass/fail certification result
  with named rejection reasons per artifact.
- One reference pack at
  `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/strategy_analysis/`
  that ports the existing `business_analysis/01_strategy_analysis.skill.md`
  into the certified eight-artifact format, passes the validator, and
  carries a receipt schema bound to the existing `GovernanceEvidenceReceipt`
  shape (no envelope change).

**Acceptance criteria:**

- Validator runs offline, returns deterministic JSON, no network call, no
  live provider call.
- Reference pack passes validation against all eight schemas.
- A deliberate violation in each of the eight artifacts triggers a
  distinct, named rejection reason.
- `workflow.spec.schema.json` declares the contract that T2's
  deterministic JSON-mode output proofs depend on.
- No runtime change to provider lanes, route, persistence, memory, or
  receipt envelope.
- File-size guard COMPLIANT.
- Markdown structural completeness COMPLIANT.
- Local governance hook chain PASS.

**Claim boundary:**

- Closes only the intake pipeline contract, validator, eight schemas, and
  one reference pack.
- Does not claim runtime workflow execution, multi-pack production
  readiness, noncoder UX expansion, or live provider proof.

**Pre-conditions:**

- Operator authorization filed as GC-018 baseline
  `docs/baselines/CVF_GC018_T1_CAPABILITY_INTAKE_PIPELINE_2026-05-22.md`.
- Decision on whether `_certified/` lives inside the existing skill
  library extension (recommended) or a new extension.

**Blocked-work override:** none required.

### T2 — Product Skill Pack System Minimum Viable Set

**Original review section:** "PRODUCT SKILL PACK SYSTEM" and "10
workflows cực mạnh" (Review CVF.md lines 167–192).

**Why second:** This is the review's stated highest-priority work. T1
supplies the eight-artifact format; T2 ships the first set of
actually-certified packs.

**Codex Finding 2 resolution:** V1 certified 5 packs but T3 needed 6
outcomes (`Review Contract` and `Build Landing Page` had no backing pack).
V2 expands T2 to **seven certified packs** so every T3 outcome has a
pack-backed implementation.

**Concrete deliverables:**

- Seven certified skill packs at
  `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/`,
  each passing the T1 validator:
  - `product_brief/` → outcome **Create PRD**
  - `sop_generator/` → outcome **Generate SOP**
  - `strategy_analysis/` (ported from T1) → secondary backing for **Create PRD** edge cases
  - `proposal_writer/` → outcome **Create Proposal**
  - `meeting_summarizer/` → outcome **Summarize Meeting**
  - `contract_review/` → outcome **Review Contract** (added in V2)
  - `landing_page_builder/` → outcome **Build Landing Page** (added in V2)
- A registry file
  `governance/registries/cvf-certified-skill-pack-registry.json`
  listing each certified pack with version, risk profile, authority scope,
  and the outcome key it backs.
- One offline regression test per pack confirming the `workflow.spec`
  produces deterministic JSON-mode output against a recorded provider
  fixture.

**Acceptance criteria:**

- All seven packs pass the T1 certification validator.
- Registry validates against a registry schema and is loaded by an
  offline test.
- Every pack declares the outcome key it backs; registry rejects packs
  whose declared outcome key is unknown.
- No live provider call in the regression suite (fixture-only).
- File-size guard, markdown structural, hook chain: COMPLIANT.

**Claim boundary:**

- Closes only the seven named packs and the registry.
- Does not claim that all 183 existing `.skill.md` files have been
  certified.
- Does not claim production readiness, multi-tenant readiness, or
  marketplace readiness.

**Pre-conditions:**

- T1 closed with completion review.
- Operator authorization filed as a separate GC-018 baseline.
- Operator confirms the seven pack names match real noncoder demand.

**Blocked-work override:** none required.

### T3 — Workflow Composition Engine + Outcome Surface

**Original review section:** "WORKFLOW COMPOSITION LAYER" and "Noncoder
KHÔNG nên thấy 'skills'" (Review CVF.md lines 527–604).

**Why third:** The review's stated UX rule is that noncoders see
outcomes, not skills. T1+T2 produce certified packs. T3 makes those
packs reachable from outcome buttons via a declared workflow composition.

**Codex Finding 2 + 3 resolution:** V1's six outcomes are now fully
backed by T2's seven packs. T3 also touches the receipt envelope, which
requires explicit blocked-work override.

**Concrete deliverables:**

- A composition contract at
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflow-composition/`
  with a typed `WorkflowComposition` interface declaring
  `outcome → workflow → certified pack[] → policy[]`.
- An outcome-to-workflow registry mapping each of the original review's
  six named outcomes to a workflow + pack set:
  - `Create PRD`           ← `product_brief` (+ `strategy_analysis` for edge cases)
  - `Generate SOP`         ← `sop_generator`
  - `Review Contract`      ← `contract_review`
  - `Build Landing Page`   ← `landing_page_builder`
  - `Summarize Meeting`    ← `meeting_summarizer`
  - `Create Proposal`      ← `proposal_writer`
- An expanded `OutcomeQuickActions` surface listing all six outcomes,
  each routing through the composition layer.
- A receipt envelope extension adding optional `workflowComposition`
  field to `GovernanceEvidenceReceipt` (gated by the operator override).

**Acceptance criteria:**

- All six outcomes are visible in the home page browse state.
- Each outcome execution produces a receipt with `workflowComposition`
  populated when the override is active.
- Offline tests cover each outcome's composition resolution.
- One live `/api/execute` proof on Alibaba qwen-turbo for at least the
  `Generate SOP` outcome returns ALLOW with `workflowComposition`
  present in the receipt.
- File-size guard, markdown structural, hook chain, full test suite,
  TypeScript check: COMPLIANT.

**Claim boundary:**

- Closes only the six named outcomes and the composition contract.
- Does not claim hosted SaaS readiness or public deployment.
- Does not claim broad outcome coverage beyond the six.

**Pre-conditions:**

- T2 closed with completion review.
- **Blocked-work override required.** Operator must sign explicit lift
  language for `new_receipt_envelopes` in the T3 GC-018 baseline. The
  lift applies to the single optional `workflowComposition` field only.
  If the lift is not granted, T3 is split: the composition contract +
  outcome surface ship in T3; the receipt field ships in a separate
  demand-gated candidate.
- GC-023 pre-flight on `home/page.tsx`, `OutcomeQuickActions.tsx`, and
  `route.ts` before any line addition.

### T4 — Provider Method Coverage Expansion

**Original review section:** "PROVIDER ABSTRACTION LAYER" (Review
CVF.md lines 221–253).

**Why fourth:** Once outcome workflows route through certified packs,
some packs will demand `stream()`, `json_mode()`, and `tool_call()`
behaviors that the current adapter set does not normalize.

**Codex Finding 3 resolution:** T4 introduces new provider execution
semantics and requires explicit blocked-work override.

**Concrete deliverables:**

- A unified `ProviderMethodContract` interface at
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`
  declaring `complete`, `stream`, `tool_call`, `json_mode`, `vision`,
  `embedding`, and `receipt` as required interface members. Any member
  may legally throw `UnsupportedMethodError` for a given provider.
- Capability declarations per provider in
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/<provider>/capability.json`.
- Two new adapter implementations: `stream()` on Alibaba qwen-turbo
  and `json_mode()` on DeepSeek deepseek-chat. The choice is bounded by
  existing operator-authorized provider lanes.
- A negative gate test ensuring `UnsupportedMethodError` fires when a
  pack workflow requests a method the bound provider does not declare in
  its capability file.

**Acceptance criteria:**

- All existing tests pass (Model Gateway 69+ tests, cvf-web 2739 tests).
- New tests for `stream()` on Alibaba and `json_mode()` on DeepSeek pass
  at least one live invocation each, with redacted output and no raw
  secret printed.
- Negative gate test passes.
- File-size guard, markdown structural, hook chain: COMPLIANT.
- Release gate PASS 7/7.

**Claim boundary:**

- Closes only `stream()` on Alibaba and `json_mode()` on DeepSeek plus
  the unified contract.
- Does not claim broad provider stability.
- Does not claim parity across all named methods or all providers.
- `retry()`, `cost()`, `risk()` remain placed at existing owners per D1.

**Pre-conditions:**

- T3 closed with completion review.
- **Blocked-work override required.** Operator must sign explicit lift
  language for `new_provider_execution_semantics` in the T4 GC-018
  baseline. The lift applies to the two named adapter methods and the
  unified contract interface only.
- Operator authorizes use of Alibaba + DeepSeek live keys for the two
  new live probes.

### T5 — Runtime Memory Hierarchy Wiring (Task Tier, In-Memory Only)

**Original review section:** "MEMORY GOVERNANCE MODEL" (Review CVF.md
lines 338–359).

**Why fifth:** Outcome workflows running through certified packs generate
task, skill, and audit memory events. H1 classifier returns tier labels;
no flow uses them. T5 wires the classifier output into a single tier —
task memory — end to end.

**Codex Finding 4 resolution:** V1 said "in-memory or file-backed" while
also claiming "no persistence". V2 narrows the boundary explicitly to
**ephemeral in-memory only**. If the operator later wants file-backed
storage, that is a separate tranche with its own persistence boundary
and retention proof.

**Concrete deliverables:**

- A retention policy contract at
  `governance/toolkit/05_OPERATION/CVF_MEMORY_TIER_RETENTION_POLICY.md`
  declaring per-tier retention, injection, and retrieval policy as
  governed text.
- A runtime task-memory store at
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/task-memory/` that:
  - Is **ephemeral in-memory only** (no file write, no database, no
    external store, no persistence across process restart).
  - Uses the existing H1 classifier to tag each event.
  - Enforces task-tier retention.
  - Refuses to persist any event whose tier classification is not `task`.
- Audit-memory readout integration: extend `audit-memory-receipt.ts` so
  the receipt surfaces `taskMemoryDecision` and `taskMemoryReason` for
  events considered for the task store.

**Acceptance criteria:**

- Task store rejects non-task events at boundary; rejection produces a
  deterministic, machine-readable reason.
- Audit-memory readout exposes new fields without changing
  `canReinject=false` behavior.
- No file write, no database, no external store, no persistence across
  process restart. Store contents are lost on process exit by design.
- Existing 2739-test cvf-web suite passes.
- Existing CDH-H audit-memory tests still pass.
- File-size guard, markdown structural, hook chain: COMPLIANT.

**Claim boundary:**

- Closes only ephemeral in-memory task-tier wiring.
- Does not claim organizational memory, long-term memory, retrieval
  flow, injection flow, file-backed storage, database, or any form of
  durable persistence.
- Does not claim production memory readiness.

**Pre-conditions:**

- T4 closed with completion review.
- **Blocked-work override required.** Operator must sign explicit lift
  language for `new_memory_tiers_beyond_lane_h_scope` in the T5 GC-018
  baseline. The lift applies to ephemeral in-memory task-tier wiring
  only. File-backed storage and durable persistence remain blocked.

### Anti-Pattern Guardrails (apply to every tranche)

Each tranche's GC-018 must explicitly forbid:

- **Closure by rejection alone.** A tranche cannot close by arguing the
  deliverable duplicates existing surfaces unless the predecessor audit's
  per-pain-point table is updated with a named equivalence proof and the
  equivalence is verified by an independent reviewer.
- **Closure by scope redefinition.** A tranche cannot close by
  re-classifying the deliverable as "product expansion outside scope". If
  the deliverable is product expansion, the tranche either builds it or
  is canceled, but it does not close with the gap intact.
- **Contract-only closure for runtime tranches.** A tranche scoped to
  deliver runtime capability cannot close with a contract or registry
  artifact and a "no runtime wiring" claim boundary. If runtime wiring
  is deferred, the tranche stays OPEN with a named follow-on tranche.
  (T1 is exempt because it is explicitly scoped as contract-only.)
- **Implicit scope inflation.** A tranche cannot quietly add work not
  named in its work order. Any scope expansion requires a fresh GC-018
  amendment.

---

## Acceptance Criteria

The roadmap as a whole is "delivered" when, for each of T1–T5:

1. A candidate-specific GC-018 baseline is filed and authorized.
2. For T3/T4/T5, the GC-018 baseline carries explicit operator-signed
   blocked-work override language for the applicable class.
3. A work order is dispatched naming the tranche's deliverables and
   acceptance criteria verbatim from this roadmap.
4. A completion review records evidence against each acceptance
   criterion of the tranche.
5. The predecessor audit's per-pain-point table is updated with the
   actual delivery status, citing the completion review path.
6. No tranche closes by rejection, redefinition, or contract-only
   substitution (T1 exempt) without an explicit operator-signed
   amendment.

---

## Withdrawal Rule

Per Codex Finding 6, V2 replaces vague withdrawal language with a
concrete rule:

- V2 remains the active roadmap of record until either:
  - All five tranches close with completion reviews and the predecessor
    audit's per-pain-point table is fully updated, **or**
  - The operator files an explicit written withdrawal in a follow-up
    review at `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_WITHDRAWAL_<date>.md`
    citing the specific tranches abandoned and the reason.

Silent abandonment is not a valid termination state. If the operator
declines an override or a tranche, the corresponding row of the audit
table must be updated with the decision and the reason.

---

## Verification or Evidence

Static verification of V2 before T1 dispatch:

- File paths under "Work Plan" are checked for existence or declared as
  new-creation in each tranche's GC-018.
- Predecessor audit `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
  exists and is cited.
- Codex blocking review
  `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_CODEX_REVIEW_2026-05-22.md`
  exists and is cited.
- Source review at `.private_reference/legacy/CVF 17.05/Review CVF.md`
  is referenced by every tranche's GC-018.
- V2 was authored after Codex review at commit `5279db51` and filed in
  the subsequent commit that contains this file.

Per-tranche verification belongs in each tranche's completion review,
not in this roadmap.

---

## Claim Boundary

V2 claims only that five tranches are authorized as the active program
structure for closing the Review CVF.md delivery gap. T1 is dispatchable
under ordinary GC-018; T2–T5 remain pending operator authorization and
T3/T4/T5 additionally require blocked-work overrides. V2 does not claim
any tranche will be executed or completed, does not file any GC-018,
does not lift any freeze, does not change posture beyond declaring this
roadmap active, does not modify the existing six 2026-05-20 closure
reviews, does not produce a release claim, and does not modify
runtime/provider/memory behavior. Pain points A–H remain CLOSED for the
bounded contracts the 2026-05-20 closure reviews executed and OPEN for
the deliverables this roadmap names.
