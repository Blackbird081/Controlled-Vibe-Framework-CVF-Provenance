# GC-018 Authorization - Legacy Role/Permission Tranche

Memory class: SUMMARY_RECORD

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION

Date: 2026-05-18

```text
GC-018 Continuation Candidate
- Candidate ID: CVF-LEGACY-PHASE-D-ROLE-PERMISSION
- Date: 2026-05-18
- Parent roadmap / wave: docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md
- Proposed scope: implement a bounded Role/Permission contract slice covering
  per-role permission profiles, allowed output classes, deny-rule vocabulary,
  and receipt owner boundary metadata for existing CVF roles.
- Continuation class: STRUCTURAL_CONTRACT
- Active quality assessment: docs/reviews/CVF_LEGACY_PHASE_C_GAP_TRIAGE_FOR_IMPLEMENTATION_2026-05-18.md
- Assessment date: 2026-05-18
- Weighted total: 8/10
- Lowest dimension: Machine enforceability (1/2 until a later runtime tranche
  consumes this contract)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: Phase C selected Role/Permission
  as the first dependency-safe Phase D tranche. ORCHESTRATOR, runtime workflow,
  and memory continuity all depend on an owner boundary for role and permission
  semantics.
- Quality protection commitments: (1) Do not rename CVFRole values. (2) Do not
  change route/provider execution. (3) Do not change public claims. (4) Keep
  live proof out of scope unless provider/governed AI execution behavior
  changes.
- Why now: GAP-17.05-002 is blocker severity and blocks broad role governance
  claims. The tranche is deterministic and contract-local.
- Active-path impact: NONE for provider execution; deterministic contract only.
- Risk if deferred: other Phase D tranches would continue depending on an
  unowned permission boundary.
- Lateral alternative considered: YES
- Why not lateral shift: implementing ORCHESTRATOR or runtime workflow first
  would require a role/permission exception and would increase ownership risk.
- Real decision boundary improved: YES, the tranche gives later runtime slices a
  typed owner boundary.
- Expected enforcement class: CI_REPO_GATE by deterministic contract tests.
- Required evidence if approved:
  - Role permission profiles exist for every current CVFRole.
  - Allowed output classes and deny-rule vocabulary are typed.
  - Receipt owner boundary metadata is present.
  - Deterministic tests prove coverage and deny/allow semantics.
  - No route/provider execution behavior is changed.

Depth Audit
- Risk reduction: 2 (addresses blocker GAP-17.05-002)
- Decision value: 2 (unblocks later Phase D dependency decisions)
- Machine enforceability: 1 (contract-local until consumed by runtime)
- Operational efficiency: 1 (removes repeated per-tranche role boundary debate)
- Portfolio priority: 2 (selected by Phase C as first Phase D tranche)
- Total: 8/10
- Decision: CONTINUE
- Reason: contract-local implementation reduces dependency risk without
  changing provider execution or public claims.

Authorization Boundary
- Authorized now: YES
- Next batch name: CVF-LEGACY-PHASE-D-ROLE-PERMISSION implementation
- Permitted implementation:
  - a canonical role-permission contract under CVF_GUARD_CONTRACT
  - deterministic tests for role coverage, deny rules, output classes, and
    receipt owner boundaries
  - barrel exports for the new contract
- Not permitted:
  - route.ts or provider execution changes
  - RBAC provider configuration changes
  - renamed role values
  - public catalog claim expansion
  - ORCHESTRATOR, runtime workflow, memory continuity, or provider method
    implementation
```

## Purpose

Authorize the first Phase D implementation tranche selected by Phase C:
Role/Permission.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_GUARD_CONTRACT` contract surface.

Owner: CVF guard contract package.

Authorized scope:

- per-role permission profile contract for existing `CVFRole` values;
- allowed output class vocabulary;
- deny-rule vocabulary;
- receipt owner boundary metadata;
- deterministic tests.

Out of scope:

- provider execution;
- route execution;
- public claims;
- NextAuth/RBAC provider configuration;
- other Phase D tranches.

## Decision / Baseline / Proposed Tranche

- Decision: CONTINUE
- Candidate ID: CVF-LEGACY-PHASE-D-ROLE-PERMISSION
- Depth Audit total: 8/10
- Proposed tranche: Legacy Role/Permission contract tranche
- Live proof: not required for this tranche because the authorized slice is a
  deterministic contract and does not control provider execution.

## Evidence / Required Evidence / Verification

Required evidence:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-permission.contract.ts`
- deterministic tests proving coverage and contract semantics
- `npm run test -- --run src/contracts/contracts.phaseD-role-permission.test.ts`
- `npm run check`

## Source Authorization

Phase C selected Role/Permission first:

- `docs/reviews/CVF_LEGACY_PHASE_C_GAP_TRIAGE_FOR_IMPLEMENTATION_2026-05-18.md`

Roadmap Phase D slot:

- `docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`

## Claim Boundary

This GC-018 authorizes deterministic Role/Permission contract work only. It
does not authorize public claim expansion, provider execution changes, route
behavior changes, or implementation of the remaining Phase D tranches.
