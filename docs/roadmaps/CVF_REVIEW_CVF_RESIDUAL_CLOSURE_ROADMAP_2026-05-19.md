# CVF Review-CVF Residual Closure Roadmap — A / C / D / E / G / H

Memory class: SUMMARY_RECORD

Status: REBUTTAL_ACCEPTED — Codex rebuttal 2026-05-19 returned MIXED_NON_BLOCKING.
Corrections applied per rebuttal: C1 GC-018 required; D1/H1 prerequisites
updated to cite completed delta evidence. Ready for GC-018 dispatch (Tier 1).

docType: roadmap

Reviewer / Worker: Claude (Orchestrator role)

Date: 2026-05-19

Predecessor:

- `docs/reviews/CVF_17_05_REVIEW_CVF_RESIDUAL_PAIN_POINTS_ASSESSMENT_2026-05-19.md`

---

## Purpose

Sequence the closure of the residual pain points in the 17.05 Review CVF
audit that remain PARTIAL after the closure of Phase 3 W1 / W2 / W3,
Lane D / E / F / G, and Runtime Maturity M1 / C2 / D2 / H2 on 2026-05-19.

This roadmap is the single planning artifact for the residual A / C / D / E /
G / H candidates. It does NOT authorize implementation, does NOT file any
GC-018, and does NOT modify any public claim. It exists to be rebutted by
Codex (Reviewer role).

Problems B and F are not in this roadmap because the residual assessment
verdicts them CLOSED. Any further work on B (10 packs target) or F (6
outcomes target) is bounded productization, not pain-point closure, and is
filed separately if needed.

---

## Scope / Target / Owner Boundary

In scope:

- Six candidates labelled A1, C1, D1, E1, G1, H1 covering the six residual
  items from the assessment.
- One non-negotiable rule per candidate: each must be intent-labelled as
  contract-closure, bounded-expansion, or explicit-rejection.
- Sequence, dependencies, and Codex rebuttal target per candidate.

Out of scope:

- Phase 4 learning loops and organizational memory.
- New skill packs beyond the existing three (Problem B expansion).
- New outcome buttons beyond the existing three (Problem F expansion).
- RBAC redesign (Problem G residual is absorption only).
- Any rewriting of the 17.05 converged verdict.
- New L0–L5 layer creation.
- Any change to `llm.adapter.interface.ts` (still inside the
  `new_provider_execution_semantics` blocked work class).

Owner:

- Claude (Orchestrator role) drafts and defends this roadmap.
- Codex (Reviewer role) returns rebuttal with BLOCKING_FINDINGS or
  NON_BLOCKING_VERDICT per candidate.
- Operator approves the GC-018 baselines that follow.

Active boundary: this roadmap belongs to the Review-CVF closure track. It is
sequenced after the CDH roadmap finishes its rebuttal cycle, because three of
this roadmap's candidates (C1, D1, H1) consume CDH artifacts when CDH ships.

---

## Authorization / Decision

Authorization at filing time: NONE. This is a proposal in READY_FOR_REBUTTAL
status. The operator has authorized neither the candidates nor their
sequencing.

Decision required from Codex per candidate:

- NON_BLOCKING — candidate may proceed to GC-018 filing as drafted.
- BLOCKING_FINDINGS — candidate is held; named blocking findings must be
  fixed before the candidate re-enters the cycle.

Decision required from operator after Codex returns:

- For each NON_BLOCKING candidate: approve the GC-018 file, then dispatch
  the work order, then close on completion review.
- For each BLOCKING candidate: instruct Orchestrator to revise per the
  findings and re-file the candidate, OR formally reject the candidate.

---

## Why This Tranche

This tranche exists because the assessment in
`docs/reviews/CVF_17_05_REVIEW_CVF_RESIDUAL_PAIN_POINTS_ASSESSMENT_2026-05-19.md`
identified six concrete residual surfaces. Each is named in the 17.05
audit, each has a known partial-delivery state today, and each has a
bounded scope that does not require new architectural layers.

The tranche is intentionally NOT "absorb all of the 17.05 audit." Five of
eight pain points are already CLOSED. This tranche covers only the residual
gap, with explicit intent labels per candidate to prevent scope inflation.

The Codex rebuttal target is on three failure modes:

1. Hidden scope inflation — a candidate that grows beyond its named surface.
2. Compute-without-data — a metric or contract that depends on upstream
   schema work the candidate does not include.
3. Governance theatre — a freeze document that duplicates what guards
   already enforce.

These three failure modes are the same ones that produced the BLOCKING
verdict on the original CDH roadmap V1.

---

## What Already Exists (Anchored to assessment evidence)

Provider contracts (Problem D anchor):

- 8 of 11 audit-named contract surfaces are defined under
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/`.
- The missing 3 (retry, cost, risk) may not belong at the method-contract
  layer at all.

Governance reliability metrics (Problem E anchor):

- 9 metric functions in
  `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`.
- 4 of 10 audit-named metrics have no compute path and need upstream
  audit-event schema additions first.

CLI registry (Problem C anchor):

- 9 verbs registered in
  `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`.
- 5 audit-named verbs missing: `run`, `skill`, `receipt`, `trace`,
  `provider`.

Audit memory (Problem H anchor):

- One tier-gate-equivalent exists at
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`.
- Five audit-named tiers (working, task, skill, organizational, long-term)
  have no explicit tier gate.

Role catalog (Problem G anchor):

- Runtime allowlist gate active in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts`
  and `cvf-web/src/app/api/execute/route.ts`.
- Canonical 11-role catalog still in the private reference at
  `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md`.

Coherence anchor (Problem A):

- Review chain: three 17.05 review docs in `docs/reviews/`.
- Guard chain: 43 pre-push guards, 11 pre-commit guards.
- No freeze documents named in the audit exist with those names.

---

## Non-Goals

The following are explicitly NOT goals of this tranche:

- Build 10 product skill packs (audit Problem B expansion is closed as
  bounded at 3).
- Build 6 outcome buttons (audit Problem F expansion is closed as bounded
  at 3).
- Build hallucination-recovery measurement using LLM judging (out of
  scope; this roadmap covers schema work only, not judging logic).
- Build learning loops or adaptive execution (Phase 4 charter required).
- Build organizational memory tier (separate Phase 4 charter required).
- Rewrite or replace any existing pre-push guard.
- Touch `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`
  (blocked work class).
- Add a new L0–L5 layer.

---

## Candidates

Six candidates A1, C1, D1, E1, G1, H1, each with intent label, scope,
prerequisites, acceptance, Codex rebuttal target, GC-018 requirement.

---

### Candidate A1 — Coherence Freeze Decision

Intent label: contract-closure OR explicit-rejection. The candidate MUST
choose one of these at GC-018 time, not "build all four files."

Audit ask: four files named `CVF_KERNEL_LAW.md`,
`CVF_RUNTIME_AUTHORITY_MODEL.md`, `CVF_EXECUTION_STATE_MODEL.md`,
`CVF_CORE_ONTOLOGY.md`.

Scope of decision artifact: a single GC-018 baseline that includes a
"Coherence Freeze Necessity Audit" section comparing:

- What the 43-guard pre-push chain already enforces about authority,
  execution state, ontology, and kernel law.
- What the existing review chain already documents about the same surfaces.
- The marginal coherence value of the four named files on top of those
  guarantees.

Two acceptable closure outcomes:

- Contract-closure outcome — the audit concludes the four files DO add
  marginal coherence value. A second work order is then filed to author
  the four files, sized at 200–400 lines each, frozen on completion.
- Explicit-rejection outcome — the audit concludes the four files DUPLICATE
  what the guard chain enforces, and the candidate is rejected with a
  written justification recorded in the closure review. The 17.05 audit
  ask is then marked as "answered by guard chain, not by named files."

Prerequisites: none. May start immediately.

Codex rebuttal target on A1:

1. Verify the Coherence Freeze Necessity Audit cites specific guards by name
   and specific behaviors they enforce, not generic claims.
2. Verify the audit does not preemptively pick contract-closure without
   justifying why the guard chain is insufficient.
3. Verify the audit does not preemptively pick explicit-rejection without
   showing the guard chain coverage explicitly.

GC-018 required: Yes (one baseline that authorizes either path).

---

### Candidate C1 — CLI Verb Completion

Intent label: contract-closure.

Audit ask: register `cvf run`, `cvf skill`, `cvf receipt`, `cvf trace`,
`cvf provider`.

Scope: extend `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
to register five new command handlers. Each handler is a thin wrapper over
existing infrastructure, not a new runtime.

Per-verb mapping:

- `cvf run <template>` — alias to `cvf execute --template <template>` with
  no behavioural change beyond argument shape.
- `cvf skill list|show` — read-only listing over the existing skill
  registry, no skill mutation.
- `cvf receipt show <id>` — read-only inspection of an existing receipt
  artifact under `audit-memory-receipt.ts` output.
- `cvf trace dump [--session <id>]` — read-only dump of the existing audit
  log, filtered by session if provided.
- `cvf provider list` — read-only listing of registered provider lanes from
  the existing provider registry.

All five verbs are read-only wrappers. No mutation, no new I/O surface, no
new auth path.

Prerequisites:

- CDH Candidate C rebuttal MUST return NON_BLOCKING first, because CDH C
  expands the CLI gateway and this candidate must not race CDH C.

Acceptance:

- Five new entries in `command.registry.ts` with `name`, `description`,
  `usage`, `execute` (or `executeAsync`) properties.
- One Vitest test file per verb (5 files, 4–6 tests each), all wrapping the
  shared `CommandRegistry` instance and using mock backends only.
- Existing CLI tests must continue to pass; total CLI test count grows by
  approximately 25 tests.

Codex rebuttal target on C1:

1. Verify each verb is a read-only wrapper. Reject any verb that exposes
   mutation, network I/O, or a new auth path.
2. Verify CDH Candidate C has actually returned NON_BLOCKING before C1
   starts.
3. Verify no verb shadows or overrides an existing command.

GC-018 required: Yes — Codex rebuttal finding 2026-05-19: adding five
canonical CLI verbs changes the public command surface; each verb must name
its backing source, input shape, and forbidden behaviors in the GC-018
baseline. `cvf run` may be an execute alias but must not imply a new runtime
path.

---

### Candidate D1 — Provider Method Contract Residual Decision

Intent label: contract-closure OR explicit-rejection per residual method.

Audit ask: standardize `retry()`, `cost()`, `risk()`.

Scope: a single GC-018 baseline that decides, per residual method, whether
it belongs at the method-contract layer (alongside reasoning, json-mode,
tool-call, embedding) OR at the policy / routing layer (alongside the
existing `quickRiskScore` and routing-policy surfaces).

Per-method analysis required in the baseline:

- `retry()` — is retry a per-method-call surface (provider-level) or a
  routing-policy surface (gateway-level)? If provider-level, build
  `retry-contract.ts`. If policy-level, record the existing policy surface
  and reject the contract file.
- `cost()` — same analysis. The existing CLI `evaluate` has a `quickRiskScore`
  that includes amount thresholds; this may already be the cost-equivalent
  surface for risk policy.
- `risk()` — same analysis. Risk classification already exists in the
  `evaluate` command and in the audit event taxonomy.

Acceptable closure outcomes per method:

- Contract-closure — a small contract file under
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/` parallel to the other 8 contracts,
  sized 30–60 lines, with a Vitest test file 4–5 tests, ≤60 lines.
- Explicit-rejection — a written justification in the baseline pointing to
  the existing policy / routing surface that already covers the named
  semantics, recorded so future agents do not re-open the ask.

Prerequisites:

- W1 closure review must remain CLOSED
  (`docs/reviews/CVF_PHASE3_W1_PROVIDER_METHOD_CONTRACTS_COMPLETION_2026-05-19.md`).
- D2 closure review must remain CLOSED
  (`docs/reviews/CVF_LANE_D_PROVIDER_METHOD_PARITY_COMPLETION_2026-05-19.md`).
- Note (Codex rebuttal 2026-05-19): original prerequisite cited CDH Candidate D
  rebuttal. That requirement is superseded — W1/D2 delta evidence is already
  closed. D1 no longer waits for CDH D; it cites the completed delta evidence
  directly.

Acceptance:

- One GC-018 baseline.
- Zero to three new contract files (depending on per-method outcome).
- Zero to three new test files.
- One closure review explicitly recording the rejected methods.

Codex rebuttal target on D1:

1. Verify the per-method analysis is explicit, not narrative.
2. Verify rejection outcomes name the existing surface that covers the
   semantics.
3. Verify contract-closure outcomes ship contract + test + closure review
   in a single tranche.

GC-018 required: Yes.

---

### Candidate E1 — Operational Benchmark Metric Expansion

Intent label: contract-closure (paired schema + metric work).

Audit ask: add the four missing metrics — hallucination recovery, human
correction count, long-horizon stability, rollback success.

Per-metric scope analysis:

- Hallucination recovery — DROP from this candidate. LLM-judged event
  classification is out of scope for the offline benchmark and is not in
  this roadmap's authorization. Record as explicit-rejection in the closure
  review.
- Human correction count — requires an upstream `operator_correction`
  audit-event type. Candidate E1 ships the event-type addition first, then
  the metric.
- Long-horizon stability — requires a time-windowed scan over
  `executionId`. The data already exists; the metric is computable today
  without upstream schema work.
- Rollback success — requires an upstream `rollback` audit-event type
  with `success: boolean` field. Candidate E1 ships the event-type addition
  first, then the metric.

Scope of work:

- Add `operator_correction` and `rollback` event types to the audit-event
  schema in
  `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
  (or, if the schema lives upstream, extend the upstream type and re-export).
- Add three new metric functions: `humanCorrectionRate`,
  `longHorizonStabilityRate`, `rollbackSuccessRate`.
- Extend `GovernanceReliabilityReport` from 9 fields to 12.
- Extend the benchmark output (table and JSON formatters) to include the
  three new metrics.

Prerequisites:

- W3 closure review must remain CLOSED.
- E1 must NOT promote the offline benchmark to "live measurement" — it
  remains offline only. The audit's "long-horizon stability" is computed
  over event windows in the supplied JSONL fixture, not over a live
  multi-day run.

Acceptance:

- One GC-018 baseline.
- Schema extension (2 new event types).
- 3 new metric functions.
- Test file expansion: existing
  `tests/governance-reliability-metrics.test.ts` grows from 68 tests to
  approximately 80 tests; if file size exceeds the governed test_code
  threshold, a dedicated test file is created instead.
- Closure review explicitly recording hallucination recovery as rejected.

Codex rebuttal target on E1:

1. Verify hallucination recovery is rejected, not silently dropped.
2. Verify the candidate ships the upstream event-type changes BEFORE the
   metric functions, not after.
3. Verify the benchmark remains offline — reject any live-run claim.

GC-018 required: Yes.

---

### Candidate G1 — Role Catalog Absorption

Intent label: contract-closure (absorption only, no RBAC redesign).

Audit ask: canonical role catalog with `allowed_outputs` and a permission
model.

Scope: absorb the 11-role catalog from the private reference
(`.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md`)
into a single canonical governed file:

- Proposed path: `docs/reference/CVF_AGENT_ROLE_CATALOG.md`.
- Frontmatter: `Memory class: FULL_RECORD`, `Status: AUTHORIZED`,
  `docType: reference`.
- Content: the 11 role IDs with `allowed_outputs`, `permission_model`,
  `execution_boundary`, `receipt_ownership`.

Coupling to runtime:

- The runtime gate at
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts`
  must continue to read `allowedActorRoles` from pack policy files. The
  catalog is reference-only; it does NOT replace pack policy.
- Pack policy files are updated only if the catalog absorption identifies
  a role mismatch.
- No new role IDs are introduced. No existing role IDs are removed.

Prerequisites:

- Lane G closure review must remain CLOSED.
- The absorption must not promote private reference content directly. It
  is a re-authoring exercise that cites the private reference as predecessor
  evidence but writes fresh content in canonical-doc form.

Acceptance:

- One GC-018 baseline (absorption authorization).
- One new file: `docs/reference/CVF_AGENT_ROLE_CATALOG.md`.
- Closure review confirming pack-policy `allowedActorRoles` aligns with the
  catalog.
- No runtime code change unless a role mismatch is found.

Codex rebuttal target on G1:

1. Verify the absorption re-authors, not copies.
2. Verify no new role IDs are introduced.
3. Verify the runtime gate is unchanged.

GC-018 required: Yes.

---

### Candidate H1 — Memory Tier Gate Decision

Intent label: contract-closure.

Audit ask: explicit tier gate for working, task, skill, organizational,
long-term memory (audit and receipt already done by H2).

Scope: a single GC-018 baseline that picks one of two architectural paths
and ships the chosen path. Both paths produce a contract layer, neither
ships runtime data flow.

Path option A — typed-per-tier:

- Five new contract files under
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/`:
  `working-memory-tier.contract.ts`, `task-memory-tier.contract.ts`,
  `skill-memory-tier.contract.ts`, `organizational-memory-tier.contract.ts`,
  `long-term-memory-tier.contract.ts`.
- Each contract names the tier identity, retention semantic, injection
  permit, retrieval permit, privacy scope, and contamination boundary.
- No runtime wiring claimed.

Path option B — single-classifier:

- One new contract file:
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`.
- Defines a single `MemoryTier` discriminated union with five tier values
  plus the existing audit and receipt tiers, and a single classifier
  contract `classifyMemoryTier(input): MemoryTier`.
- No runtime wiring claimed.

The baseline MUST choose one path explicitly. It MUST NOT ship both.

Prerequisites:

- H2 closure review must remain CLOSED
  (`docs/reviews/CVF_RUNTIME_MATURITY_H2_AUDIT_MEMORY_COMPLETION_2026-05-19.md`).
- Note (Codex rebuttal 2026-05-19): original prerequisite cited CDH Candidate H
  rebuttal. That requirement is superseded — H2 delta evidence is already
  closed and covers audit memory policy refinement. H1 no longer waits for
  CDH H; it cites the completed H2 delta evidence directly.

Acceptance:

- One GC-018 baseline naming the chosen path.
- Five new files (Path A) OR one new file (Path B).
- Test file(s) verifying tier-identity discrimination, sized inside
  governed test_code limits.
- Closure review confirming the chosen path and recording the
  rejected-path rationale.

Codex rebuttal target on H1:

1. Verify exactly one path is chosen.
2. Verify the chosen path does not silently promote into runtime wiring.
3. Verify the rejected path is named and the reason is recorded.

GC-018 required: Yes.

---

## Candidate Execution Sequence

The candidates fall into three sequencing tiers based on prerequisites.

Tier 1 — startable immediately (Codex rebuttal accepted):

- A1 (no prerequisite chain).
- G1 (Lane G already closed).
- E1 (W3 already closed).

Tier 2 — startable after GC-018 authorized (no CDH gate remaining):

- D1 (W1/D2 evidence closed; CDH D gate superseded per Codex rebuttal).
- H1 (H2 evidence closed; CDH H gate superseded per Codex rebuttal).
- C1 (GC-018 required per Codex rebuttal; verbs must be individually
  scoped in baseline; may parallel D1/H1 once GC-018 is authorized).

Tier 3 — sequenced after Tier 1 closure:

- C1, D1, H1 may be paused if Tier 1 surfaces a coherence finding that
  invalidates their scope.

No candidate proceeds to GC-018 filing until its Codex rebuttal returns
NON_BLOCKING. No candidate proceeds to implementation until its GC-018 is
AUTHORIZED.

---

## Work Plan

The work plan operationalizes the candidate execution sequence above into
ordered phases. Each phase has an explicit gate; no phase may begin until
the prior phase's gate is closed.

Phase R0 — Rebuttal (this filing onward):

- Step R0.1: Codex (Reviewer role) reads the predecessor assessment and
  this roadmap.
- Step R0.2: Codex returns a per-candidate verdict
  (NON_BLOCKING | BLOCKING_FINDINGS) recorded in a single review file
  `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`.
- Gate R0: at least one candidate marked NON_BLOCKING. If all six are
  BLOCKING, the roadmap status flips to BLOCKED and the Orchestrator
  re-files after revision.

Phase R1 — Tier 1 candidate cycles (parallel, independent):

- Step R1.A1: GC-018 file for Candidate A1 (Coherence Freeze Decision).
- Step R1.G1: GC-018 file for Candidate G1 (Role Catalog Absorption).
- Step R1.E1: GC-018 file for Candidate E1 (Operational Benchmark Metric
  Expansion).
- For each Tier 1 candidate: work order dispatch → implementation →
  closure review → continuation chain guard passes Rule A and Rule B.
- Gate R1: each Tier 1 candidate is either CLOSED with completion review
  or REJECTED with explicit rejection review.

Phase R2 — Tier 2 candidate cycles (gated on CDH NON_BLOCKING):

- Pre-step R2.0: CDH Candidate C, D, H rebuttal verdicts must all be
  NON_BLOCKING. If any is BLOCKING, the corresponding Tier 2 candidate
  here is held.
- Step R2.C1: GC-018 file for Candidate C1 (CLI Verb Completion) — only
  if CDH C NON_BLOCKING.
- Step R2.D1: GC-018 file for Candidate D1 (Provider Method Contract
  Residual Decision) — only if CDH D NON_BLOCKING.
- Step R2.H1: GC-018 file for Candidate H1 (Memory Tier Gate Decision) —
  only if CDH H NON_BLOCKING.
- For each Tier 2 candidate: work order dispatch → implementation →
  closure review → continuation chain guard passes.
- Gate R2: each Tier 2 candidate is either CLOSED with completion review
  or REJECTED with explicit rejection review.

Phase R3 — Final closure:

- Step R3.1: file a single tranche closure review at
  `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_TRANCHE_REVIEW_<date>.md`
  summarizing every candidate's disposition.
- Step R3.2: update MEMORY.md `Current Status Snapshot` to record the
  residual closure outcome.
- Gate R3: pre-push guard chain runs clean on the final closure commit.

Sequencing notes:

- Tier 1 candidates do NOT block each other. They may run in any order.
- Tier 2 candidates wait on CDH NON_BLOCKING for the matching candidate
  ONLY. They do not wait on each other.
- Tier 1 and Tier 2 may run in parallel once Tier 2 prerequisites clear.

Owner per step:

- R0: Codex (Reviewer role) holds; Orchestrator drafts revisions if
  BLOCKING.
- R1, R2 GC-018 filing: Orchestrator.
- R1, R2 implementation: Codex (Worker role).
- R1, R2 closure review: Codex (Worker role) or Reviewer role per the
  multi-agent review doc guard.
- R3: Orchestrator.

Forbidden during the work plan:

- Skipping the GC-018 step for any candidate.
- Implementing a Tier 2 candidate before its CDH gate clears.
- Adding a seventh candidate without a separate residual-assessment update
  and a fresh rebuttal cycle.
- Touching `llm.adapter.interface.ts` (blocked work class remains active).

## Acceptance Criteria

This roadmap is accepted (status flips from READY_FOR_REBUTTAL to
REBUTTED_NON_BLOCKING) only when Codex returns a per-candidate verdict for
all six candidates and at least one candidate is marked NON_BLOCKING.

The roadmap is rejected in full only when Codex finds the tranche scope
itself is wrong (for example, the residual assessment misidentifies the
remaining gap, or a hidden new layer is being introduced under the
"residual" label).

Per-candidate acceptance is defined inside each candidate section above.

---

## Verification / Evidence

For this roadmap itself, no runtime verification is required at filing
time. Verification is purely structural:

- HEAD at filing time must be `71829253` or a descendant.
- Predecessor assessment file
  `docs/reviews/CVF_17_05_REVIEW_CVF_RESIDUAL_PAIN_POINTS_ASSESSMENT_2026-05-19.md`
  must exist and be referenced by this roadmap.
- CDH roadmap
  `docs/roadmaps/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md` must exist
  (for Tier 2 prerequisite linkage).
- Each cited working-tree path inside each candidate section must currently
  exist.

For each candidate downstream, verification is defined inside that
candidate's Acceptance section above and again in its eventual GC-018
baseline.

---

## Risk / Corrective Action

Risk: Codex rebuttal returns BLOCKING on every candidate due to insufficient
intent justification. Corrective action: Orchestrator returns to the
predecessor assessment, sharpens the residual evidence, and re-files the
candidate; this does NOT trigger a roadmap rewrite.

Risk: a candidate is approved and implementation reveals the residual was
narrower than scoped. Corrective action: the closure review records the
narrower-than-scoped finding and the candidate is closed at partial-scope
with explicit "remaining sub-gap is OUT_OF_SCOPE_FOR_RESIDUAL_CLOSURE."

Risk: scope inflation creeps in during implementation despite intent
labels. Corrective action: the GC-018 baseline for the candidate names
specific files and functions and forbids adding others; any addition
requires a fresh GC-018.

Risk: Tier 2 candidates start before CDH rebuttal closes and create a
race. Corrective action: the Continuation Chain Guard's Rule A already
blocks work order closure without GC-018; Rule B blocks closure without a
completion review; this roadmap adds a soft sequencing rule on top — Tier 2
GC-018 files MUST cite the corresponding CDH NON_BLOCKING verdict in their
Source / Predecessor Evidence section.

---

## Claim Boundary

This roadmap claims only that:

- Six residual candidates have been scoped against the assessment.
- Each candidate has an intent label, a prerequisite chain, an acceptance
  definition, and a Codex rebuttal target.
- No candidate authorizes implementation. No candidate files GC-018 by
  itself.

This roadmap does not claim:

- That any candidate will be approved.
- That any candidate will close on any timeline.
- That the four named freeze documents under Candidate A1 will be authored.
  Candidate A1 may resolve as explicit-rejection.
- That the four missing metrics under Candidate E1 will all be built.
  Hallucination recovery is preemptively rejected inside the candidate.
- Any public-catalog update or release claim.

---

## Related Artifacts

Predecessor assessment:

- `docs/reviews/CVF_17_05_REVIEW_CVF_RESIDUAL_PAIN_POINTS_ASSESSMENT_2026-05-19.md`

Source audit (private reference):

- `.private_reference/legacy/CVF 17.05/Review CVF.md`

Sequencing dependency (still in rebuttal):

- `docs/roadmaps/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md`
- `docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`

Closed predecessor closures cited per candidate:

- W1: `docs/reviews/CVF_W1_PROVIDER_CONTRACT_COMPLETION_2026-05-19.md`
- W2: `docs/reviews/CVF_W2_GOVERNED_PACK_COMPLETION_2026-05-19.md`
- W3: `docs/reviews/CVF_W3_OFFLINE_BENCHMARK_EXTENSION_COMPLETION_2026-05-19.md`
- Lane G: `docs/reviews/CVF_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_COMPLETION_2026-05-19.md`
- H2: `docs/reviews/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`

Governance anchors:

- Continuation Chain Guard:
  `governance/toolkit/05_OPERATION/CVF_CONTINUATION_CHAIN_GUARD.md`
- Governed Pack Contract Guard:
  `governance/toolkit/05_OPERATION/CVF_GOVERNED_PACK_CONTRACT_GUARD.md`
- Governed File Size Guard:
  `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`
