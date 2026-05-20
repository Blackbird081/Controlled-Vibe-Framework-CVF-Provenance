# Work Order — Residual G1: Role Catalog Absorption

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Worker role: Codex (Implementer)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (Candidate G1, REBUTTAL_ACCEPTED)
- `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` (Codex verdict: NON_BLOCKING)
- `docs/reviews/CVF_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_COMPLETION_2026-05-19.md` (Lane G closed)

---

## Purpose

Author a canonical role catalog reference document that formalizes the 11
CVF agent role IDs with their `allowed_outputs`, `permission_model`,
`execution_boundary`, and `receipt_ownership` fields. This is an absorption
and re-authoring exercise only — the runtime gate is unchanged.

---

## Scope / Target / Owner Boundary

In scope:

- One new canonical file: `docs/reference/CVF_AGENT_ROLE_CATALOG.md`.
- Re-authoring (not copying) the 11-role catalog from the private reference
  source at `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md`.
- Confirming that pack-policy `allowedActorRoles` in all three governed packs
  align with the catalog.

Out of scope:

- New role IDs (forbidden).
- Removal of existing role IDs (forbidden).
- Changes to `execute-role-resolver.ts` or any runtime code.
- Changes to pack policy `allowedActorRoles` unless a concrete mismatch is
  found.
- RBAC redesign.
- Auth or NextAuth.js changes.

Constraint: the private reference source is predecessor evidence only. The
canonical file must be written fresh in CVF governed document style, not
copied from the private reference.

---

## Deliverables

### Step G1.1 — GC-018 Baseline

File: `docs/baselines/CVF_GC018_G1_ROLE_CATALOG_ABSORPTION_2026-05-20.md`

Required sections: `## Status`, `## Source or Predecessor Evidence`,
`## Purpose / Decision / Baseline`, `## Scope or Proposed Tranche`,
`## Evidence / Required Evidence / Verification`, `## Claim Boundary`.

The baseline must:

- Reference Lane G closure and Codex rebuttal NON_BLOCKING verdict.
- Confirm the private reference as predecessor evidence (not canonical source).
- State that no new role IDs will be introduced.
- State that the runtime gate at `execute-role-resolver.ts` remains unchanged.

### Step G1.2 — Role Catalog File

File: `docs/reference/CVF_AGENT_ROLE_CATALOG.md`

Required frontmatter fields:

```
Memory class: FULL_RECORD
Status: AUTHORIZED
docType: reference
```

Required structural sections:

- `## Purpose` — what the catalog is and is not
- `## Scope` — absorption only, runtime gate unchanged, pack policy is the
  enforcement source
- `## Role Definitions` — one subsection per role
- `## Pack Policy Alignment` — confirm the three governed pack `allowedActorRoles`
  are consistent with the catalog
- `## Claim Boundary` — catalog is reference-only, not a runtime enforcement
  surface

Per-role subsection format (11 roles total):

```markdown
### ROLE_ID

- **allowed_outputs**: [list]
- **permission_model**: [description]
- **execution_boundary**: [description]
- **receipt_ownership**: [description]
```

Size constraint: the file must stay within the `active_markdown` governed
threshold (900 lines advisory). If the 11 roles require more than 900 lines,
open an exception in the governed exception registry before committing.

### Step G1.3 — Pack Policy Alignment Check

Verify that `allowedActorRoles` in all three governed pack policy files is
consistent with the catalog:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/execution.policy.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/documentation/execution.policy.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/strategy_analysis/execution.policy.json`

Current known value: `["OPERATOR", "BUILDER", "REVIEWER", "SERVICE_AGENT"]`.

If a role in `allowedActorRoles` is NOT in the catalog, or a catalog role
clearly should be in `allowedActorRoles` but is not, document the mismatch
in the closure review and propose a correction in a follow-up work order.
Do NOT change pack policy files in this tranche without explicit authorization.

### Step G1.4 — Closure Review

File: `docs/reviews/CVF_G1_ROLE_CATALOG_ABSORPTION_CLOSURE_REVIEW_2026-05-20.md`

Required structure: Purpose, Target, Scope/Methodology, Findings,
Decision/Disposition, Claim Boundary.

The closure review must confirm:

- GC-018 authorized before catalog file was authored.
- Catalog file exists at the specified path with all required sections.
- 11 roles present; no new roles introduced; no existing roles removed.
- Pack policy alignment check completed; any mismatches documented.
- `execute-role-resolver.ts` is unchanged.
- Pre-commit and pre-push hooks PASS.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [ ] GC-018 baseline exists and is AUTHORIZED.
- [ ] `docs/reference/CVF_AGENT_ROLE_CATALOG.md` exists with all required
      structural sections and 11 role definitions.
- [ ] No new role IDs introduced; no existing role IDs removed.
- [ ] Pack policy alignment verified and documented.
- [ ] `execute-role-resolver.ts` unchanged (verify with `git diff`).
- [ ] Pre-commit hook PASS (structural completeness, file size, taxonomy).
- [ ] Pre-push hook PASS (all 43 guards).
- [ ] Closure review filed and confirms all above.

---

## Forbidden Actions

- Do NOT copy text verbatim from `.private_reference/`. Re-author in
  canonical form.
- Do NOT introduce new role IDs.
- Do NOT change `execute-role-resolver.ts` or any other runtime file.
- Do NOT change pack policy `allowedActorRoles` without a follow-up work order.
- Do NOT redesign RBAC or the role taxonomy.
- Do NOT claim the catalog is a runtime enforcement surface.

---

## Authority Chain

- Authorized by: Codex rebuttal (G1: NON_BLOCKING) 2026-05-19
- Roadmap: `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (REBUTTAL_ACCEPTED)
- Predecessor: `docs/reviews/CVF_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_COMPLETION_2026-05-19.md` (Lane G CLOSED)
- Orchestrator: Claude; Worker: Codex; Operator approval required for GC-018

---

## Agent Roles

- Worker (Codex): GC-018, role catalog authoring, pack policy alignment check, closure review
- Orchestrator (Claude): reviews closure review

---

## Required First Reads

1. `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` — G1 scope
2. `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` — G1 verdict + downstream guards
3. `docs/reviews/CVF_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_COMPLETION_2026-05-19.md` — Lane G evidence
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts` — runtime gate (must remain unchanged)
5. All three governed pack `execution.policy.json` files — current `allowedActorRoles`
6. `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md` — predecessor evidence (read only, do not copy)

---

## Pre-Flight Checks

- [ ] Confirm `docs/reference/CVF_AGENT_ROLE_CATALOG.md` does NOT yet exist
- [ ] Read `execute-role-resolver.ts` to confirm current runtime gate implementation
- [ ] Read all three pack `execution.policy.json` to record current `allowedActorRoles`
- [ ] Read private reference catalog to understand the 11 role IDs (predecessor evidence, not source)

---

## Write Ownership

May create only:

- `docs/baselines/CVF_GC018_G1_ROLE_CATALOG_ABSORPTION_2026-05-20.md` (new)
- `docs/reference/CVF_AGENT_ROLE_CATALOG.md` (new)
- `docs/reviews/CVF_G1_ROLE_CATALOG_ABSORPTION_CLOSURE_REVIEW_2026-05-20.md` (new)

No other files may be created or modified. `execute-role-resolver.ts` must not be touched.

---

## Execution Plan

1. File GC-018 baseline (Step G1.1) — must be AUTHORIZED before catalog is authored
2. Author `docs/reference/CVF_AGENT_ROLE_CATALOG.md` (Step G1.2)
3. Perform pack policy alignment check (Step G1.3)
4. File closure review (Step G1.4)

---

## Evidence Requirements

- GC-018 AUTHORIZED confirming re-authoring (not copy) and no new role IDs
- `docs/reference/CVF_AGENT_ROLE_CATALOG.md` with 11 role definitions and all required structural sections
- Pack policy alignment documented in closure review
- `git diff` confirms `execute-role-resolver.ts` unchanged

---

## Review Gate

Stop and return to Orchestrator if:

- Private reference source has more or fewer than 11 roles
- Pack policy `allowedActorRoles` contains a role ID not in the private reference catalog
- `execute-role-resolver.ts` would need to change to be consistent with the catalog

---

## Closure Checklist

- [ ] GC-018 AUTHORIZED
- [ ] `docs/reference/CVF_AGENT_ROLE_CATALOG.md` exists with all required sections and 11 roles
- [ ] No new role IDs introduced
- [ ] Pack policy alignment verified and documented
- [ ] `execute-role-resolver.ts` unchanged (confirmed via `git diff`)
- [ ] Pre-commit and pre-push hooks PASS
- [ ] Closure review filed

---

## Return-To-Orchestrator Conditions

Return if: role count mismatch between private reference and working tree expectation; pack policy inconsistency that requires policy file changes; hook failure outside this scope.

---

## Claim Boundary

This work order covers role catalog authoring + pack policy alignment check +
GC-018 + closure review only. Runtime enforcement remains in `execute-role-resolver.ts`
and pack policy files, unchanged. Future role additions or RBAC changes require
separate work orders.
