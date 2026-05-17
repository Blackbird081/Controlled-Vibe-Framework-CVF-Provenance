# CVF 17.05 Kernel Terminology Alias Table

Date: 2026-05-17

Memory class: FULL_RECORD

Status: PHASE 1.0 EXTENDED SCOPE ARTIFACT. Canonical term registry and
synonym/alias map for the 12 governance kernel surfaces.

This file does not authorize implementation, does not modify runtime code,
does not change public claims, and does not change release gates.

Authorized by:
`.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`

## Purpose

Map all known synonym and alias relationships across the 6 drift concern groups
inventoried in Phase 1.0, plus the additional kernel surfaces from the
Governance Kernel Freeze recommendation. For each alias family:

- state the canonical term;
- list all observed aliases and their locations;
- recommend a disposition (adopt / retire / remap).

This table is the interim canonical vocabulary registry for the CVF governance
kernel. No new alias may be introduced in any governance artifact, guard, or
contract without first registering it here.

## Target

Source evidence:
- `docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md` (94 surfaces)
- `docs/reviews/CVF_17_05_REVIEW_CVF_CONVERGED_VERDICT_2026-05-17.md` (drift evidence summary)
- `docs/reviews/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md` (12 kernel surfaces)
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/` (orchestrator gap audit)

## Scope / Target / Owner Boundary

In scope:

- Canonical term per alias family
- All observed aliases from drift inventory + kernel surfaces
- Location evidence (file path pattern or module)
- Recommended disposition per alias: `adopt` / `retire` / `remap`

Out of scope:

- Code changes — this is a doc-only alias registry
- Deprecating existing code — requires Phase 1.P/1.I/1.R/1.M GC-018
- New term introductions — any new term must be added here first

Owner: interim owner is this artifact. Permanent owner is `docs/reference/`
once promoted via separate GC-018.

## Active Boundary

This table records the current alias landscape. Disposition recommendations
are proposals — operator acknowledgment is required before retire or remap
decisions are acted upon in code.

## Entry Format

Each entry contains:

```
Canonical term    — the single preferred term going forward
Aliases observed  — synonyms found in the working tree
Location pattern  — where the alias appears
Disposition       — adopt | retire | remap
Rationale         — why this canonical term was chosen
```

---

## Group 1 — Policy Engine

**Canonical term:** `PolicyEngine`

| Alias | Location pattern | Disposition | Notes |
|---|---|---|---|
| `PolicyEngine` | `CVF_v1.6.1_GOVERNANCE_ENGINE/`, `CVF_STARTER_TEMPLATE_REFERENCE/` | `adopt` | Canonical term |
| `RoutingPolicyEngine` | `CVF_MODEL_GATEWAY/src/routing-policy.ts` | `remap` | Gateway-domain adapter — should reference canonical `PolicyEngine` interface; local name acceptable as adapter subtype |
| `PolicyDecisionEngine` | `CVF_v1.2.1_EXTERNAL_INTEGRATION/policies/policy.decision.engine.ts` | `retire` | External integration adapter — rename to `PolicyEngine` adapter pattern in Phase 1.P |
| `BasePolicyEngine` | `CVF_STARTER_TEMPLATE_REFERENCE/src/cvf/policy-engine.service.ts` | `retire` | Starter template only — `legacy_reference`; no production consumers |

**Rationale:** `PolicyEngine` is the most broadly used name and matches the
Python governance core (`policy_engine.py`). All domain-specific variants
should be typed as adapters (`SomeDomainPolicyEngineAdapter`) or dropped.

---

## Group 2 — Risk Engine / Risk Scorer

**Canonical term:** `RiskEngine` (for runtime engines); `RiskScorer` (for
scoring helpers that output a `RiskLevel`)

| Alias | Location pattern | Disposition | Notes |
|---|---|---|---|
| `RiskEngine` | `CVF_v1.7.1_SAFETY_RUNTIME/policy/risk.engine.ts` | `adopt` | Canonical for full engine implementations |
| `RiskScorer` | `CVF_ECO_v1.2_LLM_RISK_ENGINE/src/risk.scorer.ts` | `adopt` | Canonical for scoring-only helpers |
| `RiskPropagationEngine` | `CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/03_contamination_guard/risk_propagation_engine.ts` | `remap` | Domain-bounded propagation logic within contamination guard — acceptable as local subtype; must emit canonical `RiskLevel` |
| `RiskDetector` | `CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/03_contamination_guard/risk_detector.ts` | `remap` | Domain detection helper — acceptable local subtype |
| `RiskAggregator` | `CVF_ECO_v1.2_LLM_RISK_ENGINE/src/risk.aggregator.ts` | `remap` | ECO domain adapter — aggregates scores; should declare itself as `RiskScorer` adapter |
| `RiskLock` | `CVF_v1.8_SAFETY_HARDENING/core/risk/risk.lock.ts` | `remap` | Safety hardening locking mechanism — not a scorer; rename to `RiskLockGuard` or similar to distinguish from scoring |
| `RiskClassifierService` | `CVF_STARTER_TEMPLATE_REFERENCE/src/cvf/risk-classifier.service.ts` | `retire` | Template only; `legacy_reference` |
| `RiskEscalationService` | `CVF_STARTER_TEMPLATE_REFERENCE/src/cvf/risk-escalation.service.ts` | `retire` | Template only; `legacy_reference` |

**Rationale:** The R0–R3 risk tier system is the canonical vocabulary. All
scorers must emit a value in that tier system. `RiskEngine` and `RiskScorer`
are the two canonical class-name patterns; domain variants must subtype or
adapt them.

---

## Group 3 — Guard Engine

**Canonical term:** `GuardEngine`

| Alias | Location pattern | Disposition | Notes |
|---|---|---|---|
| `GuardEngine` | `CVF_GUARD_CONTRACT/src/engine.ts`, `CVF_ECO_v1.3_DOMAIN_GUARDS/src/guard.engine.ts` | `adopt` | Canonical — `CVF_GUARD_CONTRACT` is the root-owned canonical home |
| `GuardRuntime` | (no explicit class; referenced in drift inventory as a pattern name) | `retire` | Not a distinct canonical class — use `GuardEngine` |
| `ContaminationGuard` | `CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/03_contamination_guard/` | `remap` | Domain guard — acceptable local name as a `GuardEngine` domain subtype |
| `RiskGateGuard` | `CVF_GUARD_CONTRACT/src/guards/risk-gate.guard.ts`, `CVF_ECO_v2.5_MCP_SERVER/`, `CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/` | `adopt` | Canonical guard gate pattern — `risk-gate.guard` is valid naming within `GuardEngine` architecture |

**Rationale:** `CVF_GUARD_CONTRACT/src/engine.ts` is the confirmed canonical
guard engine. Node\_modules copies are packaging artifacts and not separate
canonical surfaces. `ContaminationGuard` is a valid domain subtype name.

---

## Group 4 — Agent Role / Actor Role

**Canonical term:** `AgentRole` (base union); `CVFRole` (legacy alias, retire)

| Alias | Location pattern | Disposition | Notes |
|---|---|---|---|
| `AgentRole` | `CVF_CONTROL_PLANE_FOUNDATION/src/agent.definition.boundary.contract.ts` | `adopt` | Canonical base role union |
| `DesignAgentRole` | `CVF_CONTROL_PLANE_FOUNDATION/src/design.contract.ts` | `remap` | Design-domain role extension — acceptable as a domain-scoped subtype of `AgentRole` |
| `CVFRole` | Multiple files (DOM typedefs in node\_modules — false positive) | `retire` | No active production use found; alias for `AgentRole` should be removed |
| `ActorRole` | (referenced in drift inventory pattern; no production file found) | `retire` | Alias not found in production code — do not introduce |
| `OperatorRole` | (referenced in drift inventory pattern; no production file found) | `remap` | If introduced, must be a subtype of `AgentRole` with value `"operator"` |
| `orchestrator` (role string) | `CVF_CONTROL_PLANE_FOUNDATION/src/agent.definition.boundary.contract.ts`, `src/design.contract.ts` | `adopt` | Canonical role string for the orchestrator agent |
| `planner` (role string) | Private source: `CVF_AGENT_ROLE_CATALOG.md` | `adopt` | Valid role value — not yet in root CPF enum |
| `worker` (role string) | Private source: `CVF_AGENT_ROLE_CATALOG.md` | `adopt` | Valid role value — not yet in root CPF enum |
| `reviewer` (role string) | Private source: `CVF_AGENT_ROLE_CATALOG.md` | `adopt` | Valid role value — not yet in root CPF enum |

**Rationale:** `AgentRole` in CPF is the canonical union. Domain-specific
extensions are valid as long as they are typed as subtypes of `AgentRole`.
The ORCHESTRATOR-as-CEO role boundary is a distinct concern — the role string
`"orchestrator"` exists; the role-boundary contract does not.

---

## Group 5 — Receipt / Evidence Envelope

**Canonical term:** `GovernanceReceipt` (proposed — does not exist yet);
interim: `ExecutionReceipt` (from CPF consumer contracts)

| Alias | Location pattern | Disposition | Notes |
|---|---|---|---|
| `ExecutionReceipt` | `CVF_CONTROL_PLANE_FOUNDATION/` (inferred from consumer contracts) | `adopt` | Interim canonical name for CPF execution receipts |
| `GatewayReceipt` | `CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | `remap` | Domain receipt — gateway-specific payload; must compose canonical base receipt |
| `SkillAuditReceipt` | `CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/` (inferred) | `remap` | Skill-domain receipt adapter |
| `GovernanceLedger` | `CVF_CONTROL_PLANE_FOUNDATION/` (inferred from `controlled.memory.gateway.contract.ts`) | `remap` | Ledger-level record — distinct from individual receipts; needs its own canonical home |
| `AuditLogEntry` | `CVF_EXECUTION_PLANE_FOUNDATION/src/execution.observer.contract.ts` | `remap` | Observation log entry — not a receipt; rename to avoid confusion |
| `W7Receipt` | Private source reference | `adopt` | Canonical name for W7-path receipts — not yet in root; must extend base receipt |

**Rationale:** A canonical `Receipt<TPayload>` envelope type does not exist
yet. Until Phase 1.P defines it, `ExecutionReceipt` is the closest existing
canonical pattern. Domain receipts (`GatewayReceipt`, `SkillAuditReceipt`)
must compose it rather than creating parallel receipt shapes.

---

## Group 6 — Memory Model

**Canonical term:** none established — `not_owned` surface

| Alias | Location pattern | Disposition | Notes |
|---|---|---|---|
| `MemoryHome` | Not found in active production code | `adopt` (when owner assigned) | Reserve for future canonical memory location concept |
| `WorkingMemory` | Not found in active production code | `adopt` (when owner assigned) | Reserve for the active-session memory tier |
| `TaskMemory` | Not found in active production code | `adopt` (when owner assigned) | Reserve for task-scoped memory tier |
| `SkillMemory` | Not found in active production code | `adopt` (when owner assigned) | Reserve for skill-output memory tier |
| `AuditMemory` | Not found in active production code | `adopt` (when owner assigned) | Reserve for audit-trail memory tier |
| `ReceiptMemory` | Not found in active production code | `adopt` (when owner assigned) | Reserve for receipt-store memory tier |
| `MemoryStore` | Not found in active production code | `remap` | Generic name; if introduced, must be scoped to a specific memory tier |

**Rationale:** All memory-tier terms are reserved pending owner assignment.
No new memory-tier class or type may be introduced until the memory model
owner is confirmed. The `express-rate-limit` `MemoryStore` in node\_modules
is an unrelated third-party false positive and must not be confused with a
CVF canonical surface.

---

## Group 7 — Orchestrator Role Boundary (new — not in drift inventory)

**Canonical term:** `OrchestratorBoundary` (proposed — does not exist yet)

| Alias | Location pattern | Disposition | Notes |
|---|---|---|---|
| `orchestrator_overreach` | Private source only (`orchestrator_overreach.guard.ts`) | `adopt` (when absorbed) | Reserve as canonical signal name for overreach detection |
| `ORCHESTRATOR_MUST_NOT` | Private source only | `adopt` (when absorbed) | Reserve as canonical policy rule prefix |
| `matchingRegisteredLane` | Private source only | `adopt` (when absorbed) | Reserve for worker-lane matching condition |
| `delegationRequired` | Private source only | `adopt` (when absorbed) | Reserve as canonical field name for delegation-required flag |
| `delegationRecorded` | Private source only | `adopt` (when absorbed) | Reserve as canonical field name for delegation evidence |
| `fallback_execute` | Private source only | `adopt` (when absorbed) | Reserve as canonical router outcome value |
| `worker_lane` | Private source only | `adopt` (when absorbed) | Reserve as canonical term for specialist execution lane |

**Rationale:** All ORCHESTRATOR role-boundary terms are currently absent from
the root working tree. They are reserved here to prevent future agents from
introducing conflicting synonyms. The ORCHESTRATOR convergence roadmap
(separate GC-018, post-Phase 1.0) is the authorized path to absorb them.

---

## Group 8 — Execution Lifecycle State

**Canonical term:** `PhaseState` (phase governance); `TaskState` (task lifecycle)

| Alias | Location pattern | Disposition | Notes |
|---|---|---|---|
| `PhaseState` | `CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/` | `adopt` | Canonical for phase-level lifecycle state |
| `TaskState` | `CVF_CONTROL_PLANE_FOUNDATION/src/continuity.checkpoint.contract.ts` (implied by `phaseBoundary`) | `adopt` | Canonical for task-level checkpoint state |
| `WorkflowState` | Not found in active production code | `adopt` (when owner assigned) | Reserve for workflow-level state — no owner yet |
| `RuntimeState` | Not found in active production code | `adopt` (when owner assigned) | Reserve for runtime execution state — no owner yet |

**Rationale:** `PhaseState` and `TaskState` have partial implementations.
`WorkflowState` and `RuntimeState` are reserved terms for future Phase 2
work.

---

## Group 9 — Capability / Workflow / Outcome

**Canonical term:** `Skill` (current implementation); `CertifiedCapability`,
`ProductWorkflow`, `Outcome` (reserved — not yet implemented)

| Alias | Location pattern | Disposition | Notes |
|---|---|---|---|
| `Skill` | `CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/` | `adopt` | Canonical for the current skill-layer implementation |
| `CertifiedCapability` | Doctrine only (not in working tree) | `adopt` (when owner assigned) | Reserve — the capability that graduates from skill validation |
| `ProductWorkflow` | Doctrine only (not in working tree) | `adopt` (when owner assigned) | Reserve — the governed multi-step outcome chain |
| `Outcome` | Doctrine only (not in working tree) | `adopt` (when owner assigned) | Reserve — the end-user deliverable concept |
| `OutcomeWorkflow` | Mentioned in converged verdict drift evidence | `adopt` (when owner assigned) | Reserve — the `Outcome → Workflow` linkage concept |

**Rationale:** The skill system is the only implemented layer. `CertifiedCapability`,
`ProductWorkflow`, and `Outcome` are doctrine-level concepts that have zero
active working-tree implementation. They are reserved to prevent premature
introduction of conflicting names.

---

## Consolidated Canonical Term List

| Canonical term | Group | Status |
|---|---|---|
| `PolicyEngine` | Policy decision | active |
| `RiskEngine` | Risk (runtime engine) | active |
| `RiskScorer` | Risk (scoring helper) | active |
| `RiskLevel` | Risk tier value | active (R0–R3 policy) |
| `GuardEngine` | Guard | active |
| `RiskGateGuard` | Guard gate | active |
| `AgentRole` | Agent role union | active |
| `ExecutionReceipt` | Receipt (interim) | active |
| `GovernanceReceipt` | Receipt (canonical) | reserved |
| `PhaseState` | Execution lifecycle | active |
| `TaskState` | Execution lifecycle | active |
| `WorkflowState` | Execution lifecycle | reserved |
| `RuntimeState` | Execution lifecycle | reserved |
| `Skill` | Capability | active |
| `CertifiedCapability` | Capability | reserved |
| `ProductWorkflow` | Capability | reserved |
| `Outcome` | Capability | reserved |
| `MemoryHome` | Memory | reserved |
| `WorkingMemory` | Memory | reserved |
| `TaskMemory` | Memory | reserved |
| `OrchestratorBoundary` | Orchestrator | reserved |
| `orchestrator_overreach` | Orchestrator | reserved |
| `delegationRequired` | Delegation | reserved |
| `worker_lane` | Delegation | reserved |

**Active** = term is used in the working tree and is the canonical choice.  
**Reserved** = term is not yet in the working tree; locked against conflicting
introduction.

## Findings

The alias landscape has 5 distinct structural patterns:

1. **Clean canonical** (Guard model, Provider execution): one owner, one
   term, aliases are packaging artifacts or obvious domain subtypes.
2. **Two-path split** (Policy, Risk): Python and TypeScript paths each have
   a candidate canonical term; they are not yet unified.
3. **Partially introduced** (Agent roles, Receipts): canonical term exists
   in CPF; domain aliases have multiplied without referencing the canonical.
4. **Reserved only** (Memory, Orchestrator boundary): no active implementation;
   terms reserved to prevent premature synonyms.
5. **Doctrine-only** (Capability workflow, Outcome): canonical names exist in
   doctrine but have zero working-tree implementation.

## Risk

Without this alias table, future agents will introduce new synonyms that
create additional drift surfaces. Every synonym added without registering here
is a new entry for the next drift inventory run.

The highest risk is the Orchestrator group: private source material uses 7+
distinct terms that have no working-tree counterpart. If absorbed piecemeal
without this registry, synonym families will re-fragment.

## Decision

This alias table is adopted as the interim canonical vocabulary registry for
the CVF governance kernel. Rules:

1. No new canonical term may be introduced in any governance doc, guard, or
   contract without adding it to this table first.
2. No `retire` or `remap` action may be executed in code without a separate
   Phase 1.P/1.I/1.R/1.M GC-018.
3. Reserved terms are locked — no conflicting introduction permitted.
4. This table must be consulted in the Evidence Trace Block of any absorption
   review that touches kernel vocabulary (GC-046 rule).

## Claim Boundary

This alias table:

- does not authorize renaming or retiring any existing code term
- does not modify runtime code
- does not change public claims or release gates
- does not promote any private review source into CVF canon
- does not claim live governance proof
- reserve entries do not authorize implementation — they prevent conflicting
  synonyms only
