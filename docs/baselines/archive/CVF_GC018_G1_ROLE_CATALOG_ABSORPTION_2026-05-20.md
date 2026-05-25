# CVF GC-018 G1 Role Catalog Absorption

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-20

---

## Purpose

Authorize reference-only absorption of the 11 CVF agent role templates.

---

## Source or Predecessor Evidence

- `docs/work_orders/CVF_WO_RESIDUAL_G1_ROLE_CATALOG_ABSORPTION_2026-05-20.md`
- `docs/reviews/archive/CVF_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_COMPLETION_2026-05-19.md`
- `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_ROLE_CATALOG.md`

---

## Decision / Baseline

Decision: CONTRACT_CLOSURE by canonical reference absorption.

The private reference is predecessor evidence only. The canonical catalog must
be re-authored and must not change runtime role enforcement.

---

## Scope or Proposed Tranche

Authorized:

- Create `docs/reference/CVF_AGENT_ROLE_CATALOG.md`.
- Preserve the 11 existing role IDs.
- Check pack policy alignment.

Forbidden:

- New role IDs.
- Runtime gate changes.
- Pack policy mutation in this tranche.
- RBAC redesign.

---

## Evidence / Required Evidence / Verification

Required evidence:

- 11 role definitions present.
- `execute-role-resolver.ts` unchanged.
- Pack policy `allowedActorRoles` reviewed for the three governed packs.

---

## Claim Boundary

This baseline authorizes a reference catalog only. Runtime enforcement remains
owned by existing role resolver and pack policy files.
