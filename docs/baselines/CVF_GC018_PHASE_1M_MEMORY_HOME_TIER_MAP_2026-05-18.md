# GC-018 Authorization — Phase 1.M Memory-Home Tier Map

Memory class: SUMMARY_RECORD

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION

Date: 2026-05-18

```text
GC-018 Continuation Candidate
- Candidate ID: CVF-17.05-PHASE-1M
- Date: 2026-05-18
- Parent roadmap / wave: .private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md
- Proposed scope: Map existing memory homes to a bounded 5-tier hierarchy
  (working / task / skill / audit / receipt). Assign a tier to every
  memory-home surface from Phase 1.0. Extend existing GAP-MEM work without
  overwriting it. Defer long-term and organizational memory.
- Continuation class: STRUCTURAL
- Active quality assessment: docs/reviews/archive/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md
- Assessment date: 2026-05-17
- Weighted total: 7.5/10 (Phase 1.0 inventory complete; memory-home tier
  hierarchy absent is the primary gap addressed by this phase)
- Lowest dimension: Machine enforceability (1/2 — tier map exists at doc
  level only until a later phase enforces tier boundaries at runtime)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: Phase 1.0 inventory found only
  1 MemoryHome surface match — the lowest-count concern group and the
  highest-priority gap. The owner map
  (docs/reviews/archive/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md) records
  kernel surface #9 (memory model) as not_owned — zero canonical implementation
  in working tree. The unabsorbed kernel source matrix
  (docs/reviews/archive/CVF_17_05_UNABSORBED_KERNEL_SOURCE_MATRIX_2026-05-17.md)
  confirms all 8 ORCHESTRATOR concepts including working/task/skill memory
  distinctions are not_absorbed. Defining the 5-tier model requires reading
  existing memory references, not changing them — zero active-path impact.
- Quality protection commitments: (1) No existing memory reference renamed or
  deleted. (2) GAP-MEM work extended, not overwritten. (3) Multi-tenant and
  organizational memory remain out of scope. (4) Long-term or archival memory
  tiers are not introduced in this phase.
- Why now: Phase 1.0 gate passed. The not_owned status of kernel surface #9
  means there is no canonical home to conflict with. Defining the 5-tier model
  creates the missing anchor point with zero risk of breaking an existing
  canonical owner.
- Active-path impact: NONE — tier map is classification and specification only;
  no existing memory access path changed.
- Risk if deferred: Memory surfaces continue to be introduced ad hoc — session
  state, skill library, audit log, receipt store — without a canonical tier
  assignment. The not_owned gap widens as capabilities accumulate. Phase 2.B
  runtime wire-up then cannot close the evidence chain without an ad hoc
  memory topology decision.
- Lateral alternative considered: YES
- Why not lateral shift: Defining the memory tier model inline during Phase 2.B
  would require runtime memory integration and tier definition simultaneously —
  higher risk than separating the specification now.
- Real decision boundary improved: YES — 5-tier map enables Phase 2.B memory
  wire-up and any future capability runtime to reference canonical tiers rather
  than constructing a local topology.
- Expected enforcement class: GOVERNANCE_DECISION_GATE (tier map acceptance)
  → CI_REPO_GATE (memory tier boundary tests, Phase 2.B)
- Required evidence if approved:
  - 5-tier memory model defined: working / task / skill / audit / receipt
  - Each Phase 1.0 memory-home surface (1 explicit + any additional found in
    review) is classified to one tier
  - GAP-MEM existing work acknowledged and extended, not replaced
  - Long-term and organizational memory explicitly marked out of scope
  - Conformance test stubs exist for tier boundary contracts

Depth Audit
- Risk reduction: 2 (directly addresses kernel surface #9 which is not_owned —
  the highest-priority gap in the owner map; absence blocks any evidence chain
  that involves memory)
- Decision value: 2 (tier map is required for Phase 2.B memory wire-up to have
  a canonical target; without it each new capability introduces its own
  ad hoc memory topology)
- Machine enforceability: 1 (tier map is a specification doc; hard enforcement
  requires a later phase with runtime boundary contracts)
- Operational efficiency: 1 (eliminates per-feature "which memory home?"
  analysis; tier assignments are reusable across all Phase 2 capabilities)
- Portfolio priority: 2 (Phase 1.M is listed alongside 1.P/1.I/1.R as
  first implementation wave in the converged roadmap)
- Total: 8/10
- Decision: CONTINUE
- Reason: Phase 1.0 gate passed, memory model is the sole not_owned kernel
  surface with zero conflicting canonical home, 5-tier spec is zero active-path
  risk, Phase 2.B evidence chain is gated on this output.

Authorization Boundary
- Authorized now: YES
- Next batch name: CVF-17.05-PHASE-1M implementation
- Permitted implementation:
  - 5-tier memory model definition: working / task / skill / audit / receipt
  - Tier assignment for every Phase 1.0 memory-home surface
  - Extension of existing GAP-MEM work
  - Conformance test stubs for tier boundary contracts
  - legacy_reference marking for any memory surfaces that are starter templates
- Not permitted:
  - Renaming or deleting any existing memory reference or store
  - Long-term or organizational memory tier introduction
  - Runtime memory access path changes (Phase 2.B)
  - Changes to public claims or release gates
```

## Purpose

Authorize Phase 1.M memory-home tier map definition for the memory-home
surfaces identified in Phase 1.0, addressing kernel surface #9 which is the
sole not_owned kernel surface with zero conflicting canonical home. This packet
is the gating authorization record that must exist before any Phase 1.M
implementation work begins.

## Decision / Baseline / Proposed Tranche

- Decision: CONTINUE
- Candidate ID: CVF-17.05-PHASE-1M
- Depth Audit total: 8/10
- Authorized scope: 5-tier memory model definition (working / task / skill /
  audit / receipt), tier assignment for every Phase 1.0 memory-home surface,
  extension of existing GAP-MEM work, conformance test stubs for tier boundary
  contracts, legacy_reference marking for starter template memory surfaces
- Not authorized: renaming or deleting any existing memory reference or store,
  long-term or organizational memory tier introduction, runtime memory access
  path changes, changes to public claims or release gates

## Evidence / Required Evidence / Verification

Phase 1.0 gate evidence:
- Commit `daa97429` (2026-05-18) delivered all four required Phase 1.0
  extended scope artifacts
- Drift inventory: `docs/reviews/archive/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md`
  (1 explicit MemoryHome surface — lowest count, confirming not_owned gap)
- Owner map: `docs/reviews/archive/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md`
  (kernel surface #9 memory model: not_owned, freeze_blocker — highest priority gap)
- Source matrix: `docs/reviews/archive/CVF_17_05_UNABSORBED_KERNEL_SOURCE_MATRIX_2026-05-17.md`
  (all 8 ORCHESTRATOR concepts including working/task/skill memory: not_absorbed)

Required evidence for Phase 1.M completion:
- 5-tier memory model defined: working / task / skill / audit / receipt
- Each Phase 1.0 memory-home surface assigned to one tier
- GAP-MEM existing work acknowledged and extended, not replaced
- Long-term and organizational memory explicitly marked out of scope
- Conformance test stubs exist for tier boundary contracts

## Source Authorization

Parent roadmap phase definition:
```
Phase 1.M - Memory-Home Tier Map
Opens only after Phase 1.0.
Scope: Map existing memory homes to a bounded hierarchy.
Recommended 5-tier model: working / task / skill / audit / receipt.
Defer long-term and organizational memory unless a later roadmap explicitly
opens them.
```

Phase 1.0 gate passed: commit `daa97429` (2026-05-18) delivered all four
required Phase 1.0 extended scope artifacts.

## Claim Boundary

This packet authorizes Phase 1.M memory tier map definition and GAP-MEM
extension only. It does not authorize runtime memory path changes, long-term
memory tiers, public claim changes, or Phase 2 work.
