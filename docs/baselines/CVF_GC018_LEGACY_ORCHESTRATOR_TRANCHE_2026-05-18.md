# GC-018 Authorization - Legacy ORCHESTRATOR Tranche

Memory class: SUMMARY_RECORD

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION

Date: 2026-05-18

```text
GC-018 Continuation Candidate
- Candidate ID: CVF-LEGACY-PHASE-D-ORCHESTRATOR
- Date: 2026-05-18
- Parent roadmap / wave: docs/reviews/CVF_PHASE_D_FULL_ROADMAP_FOR_CODEX_2026-05-18.md
- Proposed scope: implement a bounded ORCHESTRATOR contract slice covering
  delegation profiles, worker-lane ticket shape, overreach deny-rule
  vocabulary, and deterministic coverage helpers for current CVF roles.
- Continuation class: STRUCTURAL_CONTRACT
- Active quality assessment: docs/reviews/CVF_LEGACY_PHASE_C_GAP_TRIAGE_FOR_IMPLEMENTATION_2026-05-18.md
- Assessment date: 2026-05-18
- Weighted total: 8/10
- Lowest dimension: Machine enforceability (1/2 until a later runtime tranche
  consumes this contract in live execution)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: Role/Permission is complete and
  ORCHESTRATOR is the next dependency boundary for async worker and runtime
  workflow contracts.
- Quality protection commitments: (1) Do not change provider or route
  execution. (2) Do not introduce scheduler runtime behavior. (3) Do not claim
  full ORCHESTRATOR absorption. (4) Keep the slice deterministic and
  contract-local.
- Why now: GAP-17.05-001 and GAP-17.05-013 block later runtime workflow
  boundaries unless delegation authority and worker-lane ticket metadata are
  typed first.
- Active-path impact: NONE for provider execution; deterministic contract only.
- Risk if deferred: runtime workflow would need to define worker tickets and
  overreach semantics without an owned ORCHESTRATOR contract.
- Lateral alternative considered: YES
- Why not lateral shift: memory continuity and runtime workflow both benefit
  from a prior delegation boundary; provider method remains demand-gated.
- Real decision boundary improved: YES, later runtime work can distinguish
  typed delegation from live scheduler enforcement.
- Expected enforcement class: CI_REPO_GATE by deterministic contract tests.
- Required evidence if approved:
  - ORCHESTRATOR-eligible roles have delegation profiles.
  - Overreach deny rules stay inside typed vocabulary.
  - WorkerLaneTicket requires delegation receipt and memory write restriction
    metadata.
  - Deterministic tests prove self-delegation and non-orchestrator ticket
    denial.
  - No route/provider execution behavior is changed.
```

## Purpose

Authorize Phase D Tranche 2: ORCHESTRATOR contract absorption.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_GUARD_CONTRACT` contract surface.

Owner: CVF guard contract package.

Authorized scope:

- `OrchestratorDelegationProfile` metadata;
- `OrchestratorOverreachDenyRule` vocabulary;
- `WorkerLaneTicket` async hand-off shape;
- coverage helper for ORCHESTRATOR-eligible roles;
- deterministic tests.

Out of scope:

- scheduler runtime;
- provider execution;
- route execution;
- public claims;
- complete Agent OS or universal multi-agent runtime claims.

## Decision / Baseline / Proposed Tranche

- Decision: CONTINUE
- Candidate ID: CVF-LEGACY-PHASE-D-ORCHESTRATOR
- Depth Audit total: 8/10
- Proposed tranche: Legacy ORCHESTRATOR contract tranche
- Live proof: not required because this tranche is contract-local and does not
  change how an ORCHESTRATOR issues provider execution calls.

## Evidence / Required Evidence / Verification

Required evidence:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`
- deterministic tests proving delegation coverage, deny vocabulary, and ticket
  authority boundaries
- `npm run test -- --run src/contracts/contracts.phaseD-orchestrator.test.ts`
- `npm run check`

## Source Authorization

Phase D full roadmap:

- `docs/reviews/CVF_PHASE_D_FULL_ROADMAP_FOR_CODEX_2026-05-18.md`

Prerequisite delivered:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-permission.contract.ts`

## Claim Boundary

This GC-018 authorizes deterministic ORCHESTRATOR contract work only. It does
not authorize scheduler behavior, route/provider execution changes, public
claim expansion, or a full ORCHESTRATOR runtime absorption claim.
