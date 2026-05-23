# CVF 17.05 Governance Kernel Owner Map

Date: 2026-05-17

Memory class: FULL_RECORD

Status: PHASE 1.0 EXTENDED SCOPE ARTIFACT. Owner map for the 12 kernel
surfaces identified in the Governance Kernel Freeze recommendation.

This file does not authorize implementation, does not modify runtime code,
does not change public claims, and does not change release gates.

Authorized by:
`.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`

## Purpose

Assign a canonical owner — or an explicit "no owner / needs decision" marker —
to each of the 12 kernel surfaces that must be resolved before the Governance
Kernel Freeze can be lifted. This map is a required companion artifact to
`docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md`.

A surface is only freeze-unblocked when it has a confirmed canonical owner and
an adapter strategy, or an explicit `freeze_blocker` decision that the operator
has acknowledged.

## Target

Source: Kernel surface list in
`.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`
(Section: "What Is The Governance Kernel?")

Drift evidence: `docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md`

Orchestrator gap: `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_AGENT_ORCHESTRATOR_ROLE_ABSORPTION_GAP_CODEX_AUDIT_2026-05-17.md`

## Scope / Target / Owner Boundary

In scope:

- All 12 kernel surfaces from the freeze recommendation
- Proposed canonical owner per surface (module path)
- Proposed adapter strategy for non-canonical surfaces
- `freeze_blocker` flag where ownership is unresolved

Out of scope:

- Implementation of any consolidation — that requires Phase 1.P/1.I/1.R/1.M GC-018
- Deprecation decisions — require separate consumer analysis
- Phase 2+ runtime wiring

Owner: CVF Phase 1.0 reconvergence surface. This map is a FULL_RECORD and
must be consulted before any new governance semantics are introduced.

## Active Boundary

All dispositions in this map are proposed assignments requiring manual operator
verification. No surface may be treated as "owner confirmed" until the operator
acknowledges the proposed owner and adapter strategy.

Surfaces marked `freeze_blocker` block all implementation work in their concern
group until resolved.

## Owner Map

### Surface 1 — Authority Hierarchy

**What it governs:** who can approve, deny, delegate, execute, finalize

**Current state:** Partially documented in `governance/toolkit/02_POLICY/CVF_MASTER_POLICY.md`
and `ECOSYSTEM/doctrine/`. No single machine-checkable canonical contract.

**Proposed canonical owner:** `ECOSYSTEM/doctrine/` (doctrine layer is the
supreme authority hierarchy — FROZEN, read-only)

**Adapter strategy:** `governance/toolkit/05_OPERATION/` guard files are the
operational adapters. All new authority concepts must trace to doctrine before
being added.

**Disposition:** `partially_owned` — doctrine exists and is frozen; the gap
is that no machine-readable authority-hierarchy contract exists in `EXTENSIONS/`
that doctrine consumers can reference.

**Freeze status:** `freeze_blocker` until a machine-readable canonical pointer
contract is created and registered (does not require new semantics — pointer
only).

---

### Surface 2 — Agent / Actor Roles

**What it governs:** orchestrator, planner, worker, reviewer, auditor, operator

**Current state:** 20 distinct role definitions found across repo (see drift
inventory). `AgentRole` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.definition.boundary.contract.ts`
is the most canonical today. `DesignAgentRole` in
`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/design.contract.ts` covers design
agents. No canonical ORCHESTRATOR-as-CEO boundary contract exists.

**Proposed canonical owner:** `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.definition.boundary.contract.ts`
for the base role union. Domain-specific role extensions are adapters in their
respective modules.

**Adapter strategy:** Each domain module (skill governance, model gateway, web
platform) may define domain-local role extensions but must reference the CPF
base `AgentRole` union — not create a parallel role taxonomy.

**Disposition:** `partially_owned` — base CPF role union exists;
ORCHESTRATOR-as-CEO role boundary is `not_absorbed` (see orchestrator gap
audit).

**Freeze status:** `freeze_blocker` for any new role taxonomy additions until
CPF base role union is declared the canonical home and the ORCHESTRATOR role
boundary gap is closed.

---

### Surface 3 — Policy Decision Model

**What it governs:** allow, deny, needs approval, policy class, policy IDs

**Current state:** 13 distinct PolicyEngine implementations (see drift
inventory). Python governance engine at `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/`
is the primary runtime authority for the Python governance path.
`EXTENSIONS/CVF_GUARD_CONTRACT/` is the TypeScript guard contract surface.
No single canonical policy decision type exists that all engines reference.

**Proposed canonical owner:** `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/core/policy_engine.py`
for the Python governance path. `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`
for the TypeScript guard contract path.

**Adapter strategy:** `CVF_MODEL_GATEWAY` routing policy is an adapter over
the guard contract. `CVF_v1.2.1_EXTERNAL_INTEGRATION` policy decision engine
is a domain adapter. Starter template policy engine is `legacy_reference` only.

**Disposition:** `partially_owned` — two runtime paths (Python / TypeScript)
each have a candidate owner; they are not unified under a single
cross-language canonical contract.

**Freeze status:** `freeze_blocker` for new PolicyEngine implementations.
Existing adapters may continue. Unification strategy requires separate GC-018.

---

### Surface 4 — Risk Model

**What it governs:** R0–R3 and domain-specific risk scorers

**Current state:** 26 distinct RiskEngine/RiskScorer implementations (see
drift inventory). R0–R3 scale is defined in
`governance/toolkit/02_POLICY/CVF_MASTER_POLICY.md`. No single canonical
`RiskLevel` type that all scorers emit.

**Proposed canonical owner:** R0–R3 policy definition stays in
`governance/toolkit/02_POLICY/CVF_MASTER_POLICY.md`. Runtime risk type:
`EXTENSIONS/CVF_ECO_v1.2_LLM_RISK_ENGINE/src/risk.scorer.ts` is the primary
canonical scorer for the ECO risk path. Safety runtime path:
`EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/policy/risk.engine.ts`.

**Adapter strategy:** Domain scorers (skill governance, safety hardening,
contamination guard) are adapters that must output a canonical `RiskLevel`
value — they may not introduce new risk tiers.

**Disposition:** `partially_owned` — R0–R3 policy exists; no single canonical
`RiskLevel` TypeScript type that adapters import.

**Freeze status:** `freeze_blocker` for new risk tiers or new risk scorer
implementations. Existing adapters may continue.

---

### Surface 5 — Guard Model

**What it governs:** guard contract, runtime guard, domain guard, safety guard

**Current state:** 7 distinct GuardEngine implementations (see drift inventory).
`EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` is the TypeScript canonical guard
engine surface. `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/` provides the safety
domain canonical guard surfaces.

**Proposed canonical owner:** `EXTENSIONS/CVF_GUARD_CONTRACT/` — TypeScript
guard contract is the root-owned guard surface that other modules reference.
Domain guards are adapters that plug into the guard contract.

**Adapter strategy:** `CVF_ECO_v1.3_DOMAIN_GUARDS`, `CVF_ECO_v2.0_AGENT_GUARD_SDK`,
`CVF_ECO_v2.5_MCP_SERVER` guard engine are all domain adapters. They must
consume the guard contract engine, not implement parallel guard engines.

**Disposition:** `owned` — `CVF_GUARD_CONTRACT` is the confirmed canonical
guard contract. Node modules copies are packaging artifacts, not separate
canonical surfaces.

**Freeze status:** `watch` — owner is clear; node\_modules copies need
deprecation path in Phase 1.R.

---

### Surface 6 — Execution Lifecycle

**What it governs:** phase state, task state, workflow state, runtime state

**Current state:** Phase state is owned by `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/`.
Task and workflow state have no single canonical model. `ContinuityCheckpoint`
in CPF provides a schema standard for checkpoint records.

**Proposed canonical owner:** `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/`
for phase lifecycle. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/continuity.checkpoint.contract.ts`
for task checkpoint vocabulary. Workflow state: no owner yet.

**Adapter strategy:** Extensions that track internal task state must conform
to the CPF checkpoint vocabulary or declare an explicit adapter contract.

**Disposition:** `partially_owned` — phase lifecycle has an owner; workflow
state and runtime state have no canonical owner.

**Freeze status:** `freeze_blocker` for workflow state and runtime state —
no new state machines or workflow runtime contracts until an owner is assigned.

---

### Surface 7 — Delegation / Handoff Model

**What it governs:** worker lane, ownership, handoff, receipt, closure

**Current state:** `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts`
(ADD-C2) and `src/agent.handoff.contract.ts` (GAP-AGENT-HANDOFF) are the
canonical delegation and handoff contracts. Worker-lane concept exists in
private source material but is not yet canonicalized in root.

**Proposed canonical owner:** `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`
for delegation and handoff contracts. Worker-lane registry: `not_absorbed` —
no owner assigned.

**Adapter strategy:** `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts`
is the EPF adapter over the CPF delegation contract. All other delegation
surfaces must reference CPF as the canonical home.

**Disposition:** `partially_owned` — delegation and handoff contracts exist;
worker-lane delegation-required semantics are `not_absorbed`.

**Freeze status:** `freeze_blocker` for worker-lane and mandatory-delegation
concepts. These require the ORCHESTRATOR role boundary convergence roadmap
(separate GC-018) before canonicalization.

---

### Surface 8 — Receipt / Evidence Envelope

**What it governs:** audit receipt, gateway receipt, skill receipt, W7 receipt

**Current state:** 27 distinct Receipt/Ledger/AuditLog surfaces (see drift
inventory). No canonical `Receipt<TPayload>` envelope type that all domains
reference. CPF contains multiple consumer receipt contracts
(`agent.governed.session.contract.ts`, `consumer.contract.ts`, etc.).

**Proposed canonical owner:** `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts`
for the base governance receipt. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`
for execution-path receipts. Domain receipts (gateway, skill, W7) are adapters.

**Adapter strategy:** Domain receipt types must extend or compose the canonical
CPF base receipt, not create parallel receipt envelopes with incompatible
payloads.

**Disposition:** `partially_owned` — CPF has receipt-like types; no single
`Receipt<TPayload>` canonical type exists yet.

**Freeze status:** `freeze_blocker` for new receipt envelope formats. Existing
domain receipts may continue. Receipt unification requires Phase 1.P GC-018.

---

### Surface 9 — Memory Model

**What it governs:** working, task, skill, audit, receipt memory

**Current state:** 1 surface found matching memory-tier vocabulary (see drift
inventory — a node\_modules `express-rate-limit` false positive). No active
canonical memory-tier implementation exists in the CVF working tree.
`docs/reference/CVF_MEMORY_RECORD_CLASSIFICATION.md` (GC-022) defines
FULL\_RECORD / SUMMARY\_RECORD / POINTER\_RECORD for governance docs — this is
a doc-governance classification, not a runtime memory tier.

**Proposed canonical owner:** No owner — `not_owned`. The memory-tier model
(working\_memory / task\_memory / skill\_memory / audit\_memory / receipt\_memory)
has zero canonical implementation.

**Adapter strategy:** Cannot define adapter strategy without a canonical owner.
GC-022 doc-governance classification must not be confused with a runtime memory
tier — they are distinct concerns.

**Disposition:** `not_owned` — the memory tier model is entirely unimplemented
at the runtime level.

**Freeze status:** `freeze_blocker` — highest priority unowned surface. Any
new memory tier or memory home must wait for explicit owner assignment and
separate GC-018.

---

### Surface 10 — Capability Model

**What it governs:** skill, certified capability, product workflow, outcome

**Current state:** Skill system exists in
`EXTENSIONS/CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/`. Certified capability
concept exists in doctrine but has no runtime contract. Product workflow and
Outcome are documented in `Review CVF.md` (Problem B) as absent from the
working tree.

**Proposed canonical owner:** `EXTENSIONS/CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/`
for the skill layer. Certified capability, product workflow, and outcome: no
owner — `not_owned`.

**Adapter strategy:** Skill system is the adapter-ready layer for the capability
model — but the capability model it should adapt to does not yet exist.

**Disposition:** `partially_owned` — skill system exists; certified capability
/ product workflow / outcome chain is `not_absorbed`.

**Freeze status:** `freeze_blocker` for new capability/workflow/outcome
runtime contracts. The missing chain (`Outcome → Workflow → Certified Capability
→ Policy → Runtime → Validation → Receipt`) requires Phases 2.A–C GC-018
before any component may be wired.

---

### Surface 11 — Provider Execution Model

**What it governs:** provider output, stream, tool call, json mode, receipt

**Current state:** `EXTENSIONS/CVF_MODEL_GATEWAY/` owns the provider execution
path. Provider output contract exists at
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts`.
`parseProviderNdjsonStream` exists at line 92. Schema-only work (ADD-B
`ContextProfile`, ADD-E1 `ScopedKnowledgeProvider`) completed and bounded.

**Proposed canonical owner:** `EXTENSIONS/CVF_MODEL_GATEWAY/` for provider
execution model. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/scoped.knowledge.provider.contract.ts`
for the read-only knowledge provider contract (adapter layer).

**Adapter strategy:** All new provider integrations must go through
`CVF_MODEL_GATEWAY` as the canonical execution path. Provider receipt must
compose the CVF base receipt format (Surface 8 dependency).

**Disposition:** `owned` — model gateway is the established canonical owner
for provider execution.

**Freeze status:** `watch` — owner is clear. New provider method semantics
beyond already-authorized schema-only work require separate GC-018.

---

### Surface 12 — Kernel Vocabulary

**What it governs:** canonical terms and aliases

**Current state:** No canonical alias table exists. Multiple synonym families
identified across the drift inventory: PolicyEngine / RoutingPolicyEngine /
PolicyDecisionEngine; RiskScorer / RiskEngine / RiskPropagation;
GuardEngine / GuardRuntime; AgentRole / ActorRole / CVFRole /
DesignAgentRole; Receipt / AuditReceipt / GatewayReceipt / SkillAuditReceipt.

**Proposed canonical owner:** `docs/reviews/CVF_17_05_KERNEL_TERMINOLOGY_ALIAS_TABLE_2026-05-17.md`
(the companion artifact to this map) is the interim canonical alias registry.
A permanent canonical vocabulary home in `docs/reference/` requires a separate
GC-018 to promote it from review artifact to reference artifact.

**Adapter strategy:** All new governance documents must use the canonical term
from the alias table. Documents using deprecated synonyms must be updated when
their module is migrated in Phase 1.P/1.I/1.R/1.M.

**Disposition:** `partially_owned` — alias table exists as this session's
deliverable; no permanent `docs/reference/` home yet.

**Freeze status:** `watch` — alias table is now available. No new synonym
introductions permitted; all new contracts must use canonical terms.

---

## Owner Summary Table

| # | Kernel Surface | Proposed Owner | Disposition | Freeze Status |
|---|---|---|---|---|
| 1 | Authority hierarchy | `ECOSYSTEM/doctrine/` (frozen) | `partially_owned` | `freeze_blocker` |
| 2 | Agent / actor roles | `CVF_CONTROL_PLANE_FOUNDATION/src/agent.definition.boundary.contract.ts` | `partially_owned` | `freeze_blocker` |
| 3 | Policy decision model | `CVF_v1.6.1_GOVERNANCE_ENGINE/` (Py) + `CVF_GUARD_CONTRACT/` (TS) | `partially_owned` | `freeze_blocker` |
| 4 | Risk model | `CVF_ECO_v1.2_LLM_RISK_ENGINE/` + `CVF_v1.7.1_SAFETY_RUNTIME/` | `partially_owned` | `freeze_blocker` |
| 5 | Guard model | `CVF_GUARD_CONTRACT/src/engine.ts` | `owned` | `watch` |
| 6 | Execution lifecycle | `CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/` + CPF checkpoint | `partially_owned` | `freeze_blocker` |
| 7 | Delegation / handoff model | `CVF_CONTROL_PLANE_FOUNDATION/` (partial) | `partially_owned` | `freeze_blocker` |
| 8 | Receipt / evidence envelope | `CVF_CONTROL_PLANE_FOUNDATION/` (partial) | `partially_owned` | `freeze_blocker` |
| 9 | Memory model | none | `not_owned` | `freeze_blocker` |
| 10 | Capability model | `CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/` (partial) | `partially_owned` | `freeze_blocker` |
| 11 | Provider execution model | `CVF_MODEL_GATEWAY/` | `owned` | `watch` |
| 12 | Kernel vocabulary | alias table (interim) | `partially_owned` | `watch` |

**Freeze-blocker count:** 9 of 12 surfaces  
**Owned (clear owner):** 2 of 12 surfaces (Guard model, Provider execution model)  
**Watch (owner clear, action deferred):** 3 surfaces  
**Not owned:** 1 surface (Memory model)

## Freeze Release Criteria

The Governance Kernel Freeze may be lifted for a given surface when:

1. A canonical owner module is confirmed by the operator.
2. An adapter strategy is documented for all non-canonical implementations.
3. The alias table has a canonical term entry for the surface's key concepts.
4. A GC-018 is filed for the consolidation work in that surface.

Lifting the freeze does not mean the consolidation is complete — it means
implementation may begin under a separate GC-018.

## Findings

Of 12 kernel surfaces:

- 9 are `freeze_blocker` — no new semantics may be added in these areas
- 2 are `owned` with clear canonical owners (Guard model, Provider execution)
- 1 is `not_owned` (Memory model) — highest priority gap; no implementation
  path exists until an owner is assigned
- The ORCHESTRATOR role boundary (surfaces 2 and 7) is the most complex
  gap: partial absorption with private source material not yet canonicalized

The drift inventory's 94 surfaces map onto 12 kernel surfaces as follows:
PolicyEngine → Surface 3; RiskEngine/RiskScorer → Surface 4;
GuardEngine → Surface 5; AgentRole/CVFRole → Surface 2;
Receipt/Ledger → Surface 8; Memory/MemoryHome → Surface 9.

Surfaces 1, 6, 7, 10, 11, 12 were not directly covered by the drift inventory
script but are captured here from the freeze recommendation and orchestrator
gap audit.

## Risk

Without this owner map, agents cannot determine whether a proposed change
touches a freeze-blocked kernel surface. The drift inventory established
what exists; this map establishes who owns it. Both are required before
any consolidation work may begin.

The `not_owned` Memory model is the highest-risk gap: if a new memory tier
is introduced without an owner assignment, it will immediately add another
orphaned surface to the inventory.

## Decision

This owner map is a discovery and assignment artifact, not an implementation
authorization. The following decisions are proposed and require operator
acknowledgment:

1. `CVF_GUARD_CONTRACT/src/engine.ts` is confirmed as the canonical TypeScript
   guard engine — Phase 1.R consolidation should use it as the target.
2. `CVF_MODEL_GATEWAY/` is confirmed as the canonical provider execution
   model — new provider methods must route through it.
3. Memory model is `not_owned` — no new memory tier work may begin without
   a separate owner assignment decision.
4. ORCHESTRATOR role boundary surfaces 2 and 7 require the ORCHESTRATOR
   convergence roadmap (separate GC-018) before canonicalization.

## Claim Boundary

This owner map:

- does not authorize implementation of any Phase 1 sub-phase
- does not modify runtime code
- does not change public claims or release gates
- does not promote any private review source into CVF canon
- does not claim live governance proof
- proposed owners are heuristic assignments requiring operator confirmation
- `not_owned` classification does not prohibit reading existing surfaces —
  it prohibits adding new semantics to that concern group
