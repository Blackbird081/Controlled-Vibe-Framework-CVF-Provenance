# GC-018 Authorization - Legacy Memory Continuity Tranche

Memory class: SUMMARY_RECORD

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION

Date: 2026-05-18

```text
GC-018 Continuation Candidate
- Candidate ID: CVF-LEGACY-PHASE-D-MEMORY-CONTINUITY
- Date: 2026-05-18
- Parent roadmap / wave: docs/reviews/CVF_PHASE_D_FULL_ROADMAP_FOR_CODEX_2026-05-18.md
- Proposed scope: implement a bounded memory continuity contract slice covering
  memory tier ownership, reinjection policy fields, provenance threshold,
  privacy filter requirement, max age, and worker persistent/archive write
  denial without ORCHESTRATOR delegation receipt.
- Continuation class: STRUCTURAL_CONTRACT
- Active quality assessment: docs/reviews/CVF_LEGACY_PHASE_C_GAP_TRIAGE_FOR_IMPLEMENTATION_2026-05-18.md
- Assessment date: 2026-05-18
- Weighted total: 8/10
- Lowest dimension: Machine enforceability (1/2 until runtime reinjection
  consumes the policy)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: Runtime workflow depends on a
  clear memory owner boundary before it can model memory violations and
  reinjection transitions.
- Quality protection commitments: (1) Do not inject memory into live provider
  calls. (2) Do not change knowledge-store runtime. (3) Do not claim complete
  governed memory. (4) Keep the slice deterministic and contract-local.
- Why now: GAP-17.05-011 blocks memory continuity and Agent OS claims, and
  GAP-17.05-013/GAP-17.05-015 include memory-axis runtime constraints.
- Active-path impact: NONE for provider execution; deterministic contract only.
- Risk if deferred: runtime workflow would define memory violation states
  without a canonical tier owner and reinjection policy boundary.
- Lateral alternative considered: YES
- Why not lateral shift: runtime workflow would overlap memory authority if it
  starts before this tranche.
- Real decision boundary improved: YES, later runtime work can distinguish
  memory policy typing from live reinjection.
- Expected enforcement class: CI_REPO_GATE by deterministic contract tests.
- Required evidence if approved:
  - Every memory tier has an owner role.
  - Reinjection policy includes required privacy filter, provenance threshold,
    and max age fields.
  - Worker persistent/archive writes require ORCHESTRATOR delegation receipt.
  - Deterministic tests prove policy and tier coverage.
```

## Purpose

Authorize Phase D Tranche 5: Memory continuity contract absorption.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_GUARD_CONTRACT` contract surface.

Owner: CVF guard contract package.

Authorized scope:

- memory tier owner contract;
- memory reinjection policy contract;
- worker memory write restriction type;
- deterministic tests.

Out of scope:

- live memory reinjection into provider calls;
- knowledge-store runtime changes;
- dashboard or persistence changes;
- complete Agent OS memory claims.

## Decision / Baseline / Proposed Tranche

- Decision: CONTINUE
- Candidate ID: CVF-LEGACY-PHASE-D-MEMORY-CONTINUITY
- Depth Audit total: 8/10
- Proposed tranche: Legacy Memory continuity contract tranche
- Live proof: not required because this tranche is contract-local and does not
  inject memory into a live governed AI output path.

## Evidence / Required Evidence / Verification

Required evidence:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts`
- deterministic tests proving tier ownership, reinjection policy fields, and
  worker write restriction semantics
- `npm run test -- --run src/contracts/contracts.phaseD-memory-continuity.test.ts`
- `npm run check`

## Source Authorization

Phase D full roadmap:

- `docs/reviews/CVF_PHASE_D_FULL_ROADMAP_FOR_CODEX_2026-05-18.md`

Prerequisite delivered:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`

## Claim Boundary

This GC-018 authorizes deterministic memory continuity contract work only. It
does not authorize runtime reinjection, provider execution changes, public
claim expansion, or a full governed memory claim.
