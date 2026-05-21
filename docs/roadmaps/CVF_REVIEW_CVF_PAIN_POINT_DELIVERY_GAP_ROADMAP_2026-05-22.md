# CVF Review-CVF Pain Point Delivery Gap Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_DRAFT_PENDING_OPERATOR_AUTHORIZATION

docType: roadmap

Date: 2026-05-22

Author: Claude (planning role)

---

## Authorization or Decision

This roadmap is a **draft**. It does not file GC-018, does not authorize
any implementation, does not lift any freeze, and does not change
current posture (`terminal_hardening_closed`,
`governance_kernel_freeze_recommended`).

Each tranche below requires a separate, candidate-specific GC-018
authorization signed by the operator before any implementation begins.

Predecessor audit (mandatory reading before any tranche dispatch):

- `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`

Source of original deliverables this roadmap is measured against:

- `.private_reference/legacy/CVF 17.05/Review CVF.md`

---

## Purpose

Re-anchor planning of the Review CVF.md eight pain points against the
original review's deliverable list — not the candidate-closure status —
and propose five sequenced tranches that close the delivery gap recorded
in the predecessor audit.

---

## Why This Tranche / Purpose

The 17.05 Review CVF.md identified eight pain points (A–H) and named
concrete deliverables for each. Six candidate closure reviews on
2026-05-20 marked every pain point CLOSED, but the bounded closures
either rejected the deliverable, narrowed it to a contract-only artifact,
or partitioned it as "product expansion" and refused to build it.

The predecessor audit documents that the original review's diagnosis is
still load-bearing: CVF has Governance Infrastructure but does not have
Governed Productized Intelligence.

This roadmap re-anchors planning against the original review's
deliverable list rather than the candidate-closure status. It proposes
five tranches in the same strategic order the original review named,
each scoped so the work order can be measured against an unambiguous
deliverable from the source review.

---

## Scope

In scope:

- Five tranches (T1–T5) targeting the gaps recorded in the predecessor
  audit's per-pain-point table.
- Per-tranche objectives, deliverables, acceptance criteria, claim
  boundaries, and pre-conditions.
- Sequencing rules tied to the original review's four-phase strategic
  priority order.
- Anti-pattern guardrails that prevent recurrence of closure-by-rejection,
  closure-by-redefinition, and contract-only closure.

Out of scope:

- Filing any GC-018 baseline.
- Reopening A1/C1/D1/E1/G1/H1 closure reviews (their bounded contracts
  remain valid).
- Lifting any freeze, releasing any frozen surface, or changing the
  one-surface freeze-release rule.
- Any public-sync update.
- Any release claim, hosted readiness claim, or matured-kernel claim.
- Maika child-data, photo, or vision proof (separately demand-gated).
- Broader provider stability (separately demand-gated).
- D-06 kernel-owner replacement, D-07 global freeze lift.

---

## Non-Goals

- This roadmap is not a release plan.
- This roadmap is not a marketing artifact.
- This roadmap is not authorization. It is a planning record that the
  operator may accept, reject, modify, or sequence differently.
- This roadmap does not promise that tranches will be authorized at all,
  in this order, or in any particular timeframe.
- This roadmap does not invalidate the existing six closure reviews. It
  proposes additional, complementary delivery work.

---

## Work Plan

### Tranche Sequencing Rule

Tranches must execute in the order T1 → T5 unless the operator
authorizes a reordering. The order follows the 17.05 review's strategic
priority (Phase 1 Stabilization → Phase 2 Runtime Maturity → Phase 3
Productization → Phase 4 Operational Intelligence), prioritized by the
review's own statement that PROBLEM B was "priority cao nhất".

Within each tranche, the standard chain is: GC-018 baseline → work
order → Codex Orchestrator → Reviewer rebuttal → Implementer → Auditor
completion review.

### T1 — Capability Intake Pipeline (Pain B foundation, also unblocks F)

**Original review section:** "CAPABILITY INTAKE PIPELINE" and "SKILL
CERTIFICATION SYSTEM" (Review CVF.md lines 466–525).

**Why first:** The review explicitly named this as the architecture
missing from CVF. Without it, Tranche 2 (skill packs) has no
machine-readable surface, and Tranche 3 (workflow composition) has
nothing to compose.

**Concrete deliverables:**

- `governance/toolkit/05_OPERATION/CVF_CAPABILITY_INTAKE_PIPELINE_GUARD.md`
  defining the intake → normalization → risk audit → policy binding →
  certification → workflow mapping → governed runtime pipeline as a
  governed surface contract.
- A JSON schema set under `governance/schemas/skill-pack/`:
  `skill.meta.schema.json`,
  `risk.profile.schema.json`,
  `authority.scope.schema.json`,
  `execution.boundary.schema.json`,
  `receipt.schema.schema.json`,
  `workflow.binding.schema.json`.
- A validator script `scripts/validate_skill_pack_certification.py` that
  takes a candidate skill pack directory, runs all six schema validations,
  and emits a pass/fail certification result with reasons.
- One reference pack at `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/strategy_analysis/`
  that ports the existing `business_analysis/01_strategy_analysis.skill.md`
  into the certified six-artifact format, passes the validator, and
  carries a receipt schema bound to existing `GovernanceEvidenceReceipt`.

**Acceptance criteria:**

- Validator runs offline, returns deterministic JSON, no network call.
- Reference pack passes validation; a deliberate violation in each of
  the six artifacts triggers a distinct rejection reason.
- No runtime change to provider lanes, route, persistence, or memory.
- File-size guard COMPLIANT, structural completeness COMPLIANT.

**Claim boundary:**

- Closes only the intake pipeline contract and one reference pack.
- Does not claim runtime workflow execution, multi-pack production
  readiness, or noncoder UX expansion.

**Pre-conditions:**

- Operator authorization (separate GC-018).
- Decision on whether `_certified/` lives inside the existing skill
  library extension or a new extension.

### T2 — Product Skill Pack System Minimum Viable Set (Pain B delivery)

**Original review section:** "PRODUCT SKILL PACK SYSTEM" and "10
workflows cực mạnh" (Review CVF.md lines 167–192).

**Why second:** This is the priority the original review named as
"highest". T1 supplies the artifact format; T2 ships the first set of
actually-certified packs.

**Concrete deliverables:**

- Five certified skill packs at
  `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/_certified/`,
  each passing the T1 validator:
  - `product_brief/`
  - `sop_generator/`
  - `strategy_analysis/` (ported from T1)
  - `proposal_writer/`
  - `meeting_summarizer/`
- A registry file `governance/registries/cvf-certified-skill-pack-registry.json`
  listing each certified pack with version, risk profile, and authority
  scope.
- One offline regression test per pack confirming the workflow.spec
  produces deterministic JSON-mode output against a recorded provider
  fixture.

**Acceptance criteria:**

- All five packs pass the T1 certification validator.
- Registry validates against a registry schema and is loaded by an
  offline test.
- No live provider call is added to the test suite.
- File-size guard COMPLIANT, structural completeness COMPLIANT.

**Claim boundary:**

- Closes only the five named packs.
- Does not claim that all 183 existing `.skill.md` files have been
  certified.
- Does not claim production readiness, multi-tenant readiness, or
  marketplace readiness.

**Pre-conditions:**

- T1 closed with completion review.
- Operator authorization (separate GC-018).
- Operator confirms the five pack names match real noncoder demand.

### T3 — Workflow Composition Engine + Outcome-to-Workflow Registry (Pain F delivery, depends on T2)

**Original review section:** "WORKFLOW COMPOSITION LAYER" and "Noncoder
KHÔNG nên thấy 'skills'" (Review CVF.md lines 527–604).

**Why third:** The review's stated UX rule is that noncoders see
outcomes, not skills. T1+T2 produce certified packs. T3 makes those
packs reachable from outcome buttons via a declared workflow.

**Concrete deliverables:**

- A composition contract at
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflow-composition/`
  with a typed `WorkflowComposition` interface declaring `outcome →
  workflow → certified pack[] → policy[]`.
- An outcome-to-workflow registry mapping each of the original
  review's named outcomes to a workflow + pack set:
  - `Create PRD` (was Create Product Spec)
  - `Generate SOP`
  - `Review Contract`
  - `Build Landing Page`
  - `Summarize Meeting`
  - `Create Proposal`
- An expanded `OutcomeQuickActions` surface listing all six outcomes,
  each routing through the composition layer.
- A receipt extension adding `workflowComposition` to the existing
  `GovernanceEvidenceReceipt` so a single execution receipt names the
  composed workflow.

**Acceptance criteria:**

- All six outcomes are visible in the home page browse state.
- Each outcome execution produces a receipt with `workflowComposition`
  populated.
- Offline tests cover each outcome's composition resolution.
- One live `/api/execute` proof on Alibaba qwen-turbo for at least the
  `Generate SOP` outcome returns ALLOW with `workflowComposition`
  present in the receipt.
- File-size guard COMPLIANT, structural completeness COMPLIANT.

**Claim boundary:**

- Closes only the six named outcomes and the composition contract.
- Does not claim hosted SaaS readiness or public deployment.
- Does not claim broad outcome coverage beyond the six.

**Pre-conditions:**

- T2 closed with completion review.
- Operator authorization (separate GC-018).
- GC-023 pre-flight on `home/page.tsx`, `OutcomeQuickActions.tsx`, and
  `route.ts` before any line addition.

### T4 — Provider Method Coverage Expansion (Pain D delivery)

**Original review section:** "PROVIDER ABSTRACTION LAYER" (Review
CVF.md lines 221–253).

**Why fourth:** Once outcome workflows route through certified packs,
some packs will demand `stream()`, `json_mode()`, and `tool_call()`
behaviors that the current adapter set does not normalize. This tranche
brings the gateway closer to provider parity for the methods the
review named.

**Concrete deliverables:**

- A unified `ProviderMethodContract` interface in
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`
  declaring `complete`, `stream`, `tool_call`, `json_mode`,
  `vision`, `embedding`, and `receipt` as required methods (any of
  which may legally throw `UnsupportedMethodError` for a given
  provider).
- Capability declarations per provider in
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/<provider>/capability.json`.
- Two new adapter implementations for the highest-priority missing
  methods: `stream()` on Alibaba qwen-turbo and `json_mode()` on
  DeepSeek deepseek-chat. The choice of these two is bounded by the
  same operator-authorized provider lanes already certified.
- A negative gate test ensuring `UnsupportedMethodError` fires when a
  pack workflow requests a method the bound provider does not declare
  in its capability file.

**Acceptance criteria:**

- All existing tests pass.
- New tests for `stream()` on Alibaba and `json_mode()` on DeepSeek
  pass at least one live invocation each, with redacted output and no
  raw secret printed.
- Negative gate test passes.
- File-size guard COMPLIANT, structural completeness COMPLIANT.
- Release gate PASS 7/7.

**Claim boundary:**

- Closes only `stream()` on Alibaba and `json_mode()` on DeepSeek plus
  the unified contract.
- Does not claim broad provider stability.
- Does not claim parity across all named methods or all providers.
- `retry()`, `cost()`, `risk()` remain placed at their existing owners
  per D1.

**Pre-conditions:**

- T3 closed with completion review.
- Operator authorization (separate GC-018).
- Operator authorizes use of Alibaba + DeepSeek live keys for the two
  new live probes.

### T5 — Runtime Memory Hierarchy Wiring (Pain H delivery)

**Original review section:** "MEMORY GOVERNANCE MODEL" (Review CVF.md
lines 338–359).

**Why fifth:** Outcome workflows running through certified packs
generate task, skill, and audit memory events. The H1 classifier
already returns tier labels, but no flow uses the labels. This tranche
wires the classifier output into a single tier — task memory — end to
end, leaving organizational and long-term tiers as deferred future
work.

**Concrete deliverables:**

- A retention policy contract at
  `governance/toolkit/05_OPERATION/CVF_MEMORY_TIER_RETENTION_POLICY.md`
  declaring per-tier retention, injection, and retrieval policy as
  governed text.
- A runtime task-memory store at
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/task-memory/` that
  uses the existing classifier to tag each event, enforces task-tier
  retention, and refuses to persist any event whose tier classification
  is not `task`.
- Audit-memory readout integration: extend `audit-memory-receipt.ts` so
  the receipt surfaces `taskMemoryDecision` and `taskMemoryReason` for
  events that were considered for the task store.

**Acceptance criteria:**

- Task store rejects non-task events at boundary; rejection produces
  a deterministic reason.
- Audit-memory readout exposes new fields without changing
  `canReinject=false` behavior.
- No persistence, database, or external memory store is introduced.
- File-size guard COMPLIANT, structural completeness COMPLIANT.
- Existing 2739-test cvf-web suite passes.

**Claim boundary:**

- Closes only task-tier wiring.
- Does not claim organizational memory, long-term memory, retrieval
  flow, injection flow, or persistence.
- Does not claim production memory readiness.

**Pre-conditions:**

- T4 closed with completion review.
- Operator authorization (separate GC-018).
- Operator decides whether task-tier store is in-memory only or
  file-backed in a session-scoped directory.

### Anti-Pattern Guardrails (apply to every tranche)

Each tranche's GC-018 must explicitly forbid:

- **Closure by rejection alone.** A tranche cannot close by arguing
  the deliverable duplicates existing surfaces unless the predecessor
  audit's per-pain-point table is updated with a named equivalence
  proof, and the equivalence is verified by an independent reviewer.
- **Closure by scope redefinition.** A tranche cannot close by
  re-classifying the deliverable as "product expansion outside
  scope". If the deliverable is product expansion, the tranche either
  builds it or is canceled, but it does not close with the gap intact.
- **Contract-only closure.** A tranche scoped to deliver runtime
  capability cannot close with a contract or registry artifact and a
  "no runtime wiring" claim boundary. If runtime wiring is deferred,
  the tranche stays OPEN with a named follow-on tranche.
- **Implicit scope inflation.** A tranche cannot quietly add work not
  named in its work order. Any scope expansion requires a fresh GC-018
  amendment.

---

## Acceptance Criteria

The roadmap as a whole is "delivered" when, for each of T1–T5:

1. A candidate-specific GC-018 baseline is filed and authorized.
2. A work order is dispatched naming the deliverables and acceptance
   criteria of that tranche verbatim from this roadmap.
3. A completion review records evidence against each acceptance
   criterion of the tranche.
4. The predecessor audit's per-pain-point table is updated with the
   actual delivery status, citing the completion review path.
5. No tranche closes by rejection, redefinition, or contract-only
   substitution without the explicit operator-signed amendment named
   under "Anti-Pattern Guardrails".

The roadmap is **withdrawn** if the operator declines to authorize T1
within a reasonable decision window. Withdrawal must be recorded as a
revision to this file, not silent abandonment.

---

## Verification or Evidence

Static verification of this roadmap before dispatch:

- File paths under "Work Plan" must be checked for existence or
  declared as new-creation in each tranche's GC-018.
- The predecessor audit `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
  must exist and be cited.
- Source review at `.private_reference/legacy/CVF 17.05/Review CVF.md`
  must be referenced by every tranche's GC-018.

Per-tranche verification belongs in each tranche's completion review,
not in this roadmap.

---

## Claim Boundary

This roadmap claims only that five tranches are proposed to close the
delivery gap recorded in the predecessor audit. It does not claim that
any tranche will be authorized, executed, or completed. It does not
file GC-018. It does not lift freeze. It does not change posture or
public claims. It does not modify the existing six closure reviews from
2026-05-20. It does not claim Review CVF.md's pain points are now
re-opened in CVF state; they remain CLOSED for the bounded contracts
the closure reviews executed, and OPEN for the deliverables this
roadmap names.
