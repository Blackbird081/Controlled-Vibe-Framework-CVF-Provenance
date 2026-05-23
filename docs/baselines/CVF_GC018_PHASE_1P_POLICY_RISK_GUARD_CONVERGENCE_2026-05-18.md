# GC-018 Authorization — Phase 1.P Policy / Risk / Guard Contract Convergence

Memory class: SUMMARY_RECORD

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION

Date: 2026-05-18

```text
GC-018 Continuation Candidate
- Candidate ID: CVF-17.05-PHASE-1P
- Date: 2026-05-18
- Parent roadmap / wave: .private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md
- Proposed scope: Define canonical policy decision contract, canonical risk
  assessment contract with R-scale binding, and bind GuardEngine surfaces to
  canonical guard contract. Keep domain behavior as adapters. Mark templates
  and historical modules as legacy_reference.
- Continuation class: STRUCTURAL
- Active quality assessment: docs/reviews/archive/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md
- Assessment date: 2026-05-17
- Weighted total: 7.5/10 (Phase 1.0 inventory complete; canonical contracts
  absent is the primary gap — this phase directly addresses it)
- Lowest dimension: Machine enforceability (1/2 — contracts exist at doc level
  only until Phase 1.P delivers typed interfaces)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: Phase 1.0 inventory confirmed 13
  PolicyEngine surfaces, 26 RiskEngine/Scorer surfaces, 7 GuardEngine surfaces
  with no canonical contract home. Adding new canonical contracts does not
  mutate existing runtime — it creates the missing anchor point that adapters
  can reference. Deferring further means every new implementation adds another
  orphaned surface to the inventory.
- Quality protection commitments: (1) No existing implementation deleted or
  renamed — adapter pattern only. (2) No runtime wire-up in this phase — contract
  definition and adapter plan only. (3) Conformance tests proposed per surface
  before any migration begins. (4) GuardEngine: CVF_GUARD_CONTRACT/src/engine.ts
  confirmed as canonical — no new engine created, existing canonical extended.
- Why now: Phase 1.0 gate is passed. Owner map confirmed canonical homes for
  Policy (CVF_v1.6.1_GOVERNANCE_ENGINE + CVF_GUARD_CONTRACT), Risk
  (CVF_ECO_v1.2_LLM_RISK_ENGINE + CVF_v1.7.1_SAFETY_RUNTIME), Guard
  (CVF_GUARD_CONTRACT). Contracts can be defined without kernel owner ambiguity.
- Active-path impact: LIMITED — contract definition only; no existing code path
  changed until Phase 2.B runtime wire-up.
- Risk if deferred: Each new absorption or feature continues to introduce
  PolicyEngine/RiskScorer/GuardEngine variants without a canonical target.
  Drift inventory grows. Phase 2.A contract sketch and Phase 2.B runtime
  wire-up are blocked on Phase 1.P outputs.
- Lateral alternative considered: YES
- Why not lateral shift: Moving directly to Phase 2.A contract sketch without
  canonical policy/risk/guard contracts would require Phase 2.A to define those
  contracts inline — duplicating Phase 1.P work and creating a different home.
- Real decision boundary improved: YES — canonical contracts enable Phase 1.I,
  1.R, 1.M adapter plans and Phase 2.B runtime wire-up to reference typed
  interfaces rather than prose descriptions.
- Expected enforcement class: GOVERNANCE_DECISION_GATE (contract acceptance)
  → CI_REPO_GATE (conformance tests per surface, Phase 2.B)
- Required evidence if approved:
  - Canonical policy decision contract type exists in root (TypeScript interface
    or Python abstract class depending on path)
  - Canonical RiskLevel type exists covering R0-R3 scale
  - CVF_GUARD_CONTRACT/src/engine.ts confirmed as canonical GuardEngine home;
    domain guard adapters documented
  - Each Phase 1.0 PolicyEngine surface has a proposed adapter map
  - Each Phase 1.0 RiskEngine/Scorer surface has a proposed adapter map
  - Each Phase 1.0 GuardEngine surface has a proposed adapter map
  - Conformance test stubs exist for each canonical contract

Depth Audit
- Risk reduction: 2 (directly addresses the fragmentation identified as
  CRITICAL in Problem A / freeze-blocker in owner map)
- Decision value: 2 (canonical contracts are the required input for Phase 2.B
  runtime wire-up — without them the capability chain cannot close)
- Machine enforceability: 1 (contract is a typed interface; enforcement of
  adapter conformance requires Phase 2.B tests — not machine-hard at this phase)
- Operational efficiency: 1 (reduces manual disambiguation cost per new
  implementation; adapter plan eliminates repeated "which engine?" analysis)
- Portfolio priority: 2 (Phase 1.P is explicitly listed as the first
  implementation phase in the converged roadmap after Phase 1.0)
- Total: 8/10
- Decision: CONTINUE
- Reason: Phase 1.0 gate passed, owner map confirms canonical homes, no
  existing runtime mutated, adapter pattern is safe expansion, Phase 2 is
  gated on this output.

Authorization Boundary
- Authorized now: YES
- Next batch name: CVF-17.05-PHASE-1P implementation
- Permitted implementation:
  - Canonical policy decision contract (TypeScript + Python paths)
  - Canonical RiskLevel type and R-scale binding
  - GuardEngine adapter documentation and conformance test stubs
  - Adapter map for all 46 Phase 1.0 surfaces across the three concern groups
  - legacy_reference marking for starter template and dist surfaces
- Not permitted:
  - Deleting or renaming any existing implementation
  - Runtime wire-up or execution path changes (Phase 2.B)
  - New PolicyEngine / RiskEngine / GuardEngine implementations beyond the
    canonical contract itself
  - Changes to public claims or release gates
```

## Purpose

Authorize Phase 1.P contract definition and adapter mapping for the policy
decision, risk assessment, and guard engine concern groups. This packet is
the gating authorization record that must exist before any Phase 1.P
implementation work begins.

## Decision / Baseline / Proposed Tranche

- Decision: CONTINUE
- Candidate ID: CVF-17.05-PHASE-1P
- Depth Audit total: 8/10
- Authorized scope: canonical policy decision contract (TypeScript + Python),
  canonical RiskLevel type and R-scale binding, GuardEngine adapter
  documentation and conformance test stubs, adapter map for all 46 Phase 1.0
  surfaces across the three concern groups, legacy_reference marking for
  starter template and dist surfaces
- Not authorized: deleting or renaming any existing implementation, runtime
  wire-up or execution path changes, new engine implementations beyond the
  canonical contract itself, changes to public claims or release gates

## Evidence / Required Evidence / Verification

Phase 1.0 gate evidence:
- Commit `daa97429` (2026-05-18) delivered all four required Phase 1.0
  extended scope artifacts
- Drift inventory: `docs/reviews/archive/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md`
  (13 PolicyEngine, 26 RiskEngine/RiskScorer, 7 GuardEngine surfaces)
- Owner map: `docs/reviews/archive/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md`
  (kernel surfaces #3 policy, #4 risk, #5 guard mapped)
- Alias table: `docs/reviews/archive/CVF_17_05_KERNEL_TERMINOLOGY_ALIAS_TABLE_2026-05-17.md`
  (canonical terms: PolicyEngine, RiskEngine, GuardEngine registered)

Required evidence for Phase 1.P completion:
- Canonical policy decision contract type exists in repo root
- Canonical RiskLevel type exists covering R0-R3 scale
- CVF_GUARD_CONTRACT/src/engine.ts confirmed as canonical GuardEngine home
- Each Phase 1.0 PolicyEngine surface (13) has a proposed adapter map
- Each Phase 1.0 RiskEngine/Scorer surface (26) has a proposed adapter map
- Each Phase 1.0 GuardEngine surface (7) has a proposed adapter map
- Conformance test stubs exist for each canonical contract

## Source Authorization

Parent roadmap phase definition:
```
Phase 1.P - Policy, Risk, And Guard Contract Convergence
Opens only after Phase 1.0.
Scope: Define canonical policy decision contract. Define canonical risk
assessment contract and R-scale binding. Bind GuardEngine/GuardRuntimeEngine
surfaces to canonical guard contract. Keep domain behavior as adapters where
appropriate. Mark templates and historical modules as legacy_reference.
```

Phase 1.0 gate passed: commit `daa97429` (2026-05-18) delivered all four
required Phase 1.0 extended scope artifacts.

## Claim Boundary

This packet authorizes Phase 1.P contract definition and adapter mapping only.
It does not authorize runtime changes, public claim changes, or Phase 2 work.
