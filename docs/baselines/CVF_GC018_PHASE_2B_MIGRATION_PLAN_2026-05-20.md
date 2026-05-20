# CVF GC-018 Phase 2.B Migration Plan

Memory class: FULL_RECORD

Status: GC018_ACCEPTED_FOR_STATIC_MIGRATION_PLAN

docType: baseline

Date: 2026-05-20

Owner lane: Private provenance / governance planning

---

## Purpose

Authorize the static Phase 2.B migration-plan artifact after the HN2.b owner
map has been locked and the HN2.c freeze-release rule has become binding.

This GC-018 authorizes only one planning output:

`docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`

It does not authorize adapter implementation, runtime wiring, provider changes,
Maika changes, memory changes, public-sync work, or any public claim that CVF
has broad coherent runtime execution.

---

## Authority Chain

- Doctrine: `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md`
- HN2.a inventory:
  `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
- HN2.b owner map:
  `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- HN2.c freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- Phase 2.B roadmap:
  `docs/roadmaps/CVF_PHASE_2B_MIGRATION_PLAN_ROADMAP_2026-05-20.md`
- Phase 2.B rebuttal:
  `docs/reviews/CVF_PHASE_2B_MIGRATION_PLAN_CODEX_REBUTTAL_2026-05-20.md`
- Gap record:
  `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`

---

## Source / Predecessor Evidence

Predecessor evidence:

- Phase 1 adapter maps under
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/`
- Prior bounded Phase 2.B completion:
  `docs/reviews/CVF_17_05_PHASE_2B_BOUNDED_WIREUP_COMPLETION_2026-05-18.md`
- Phase 2.B preflight blocker:
  `docs/reviews/CVF_17_05_PHASE_2B_PREFLIGHT_OWNER_MIGRATION_PLAN_2026-05-18.md`
- Gap ledger entry `GAP-17.05-004` requiring order, owner, done criterion, and
  dependency graph.

---

## Purpose / Decision / Baseline

Decision: accept a static planning baseline only. The baseline closes the
missing migration-plan inputs but does not approve implementation.

Baseline output: one authoritative reference file with exactly 46 primary
targets and a citation rule for later per-surface GC-018 packets.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: static Phase 2.B migration planning.

Accepted decision: produce the migration-plan reference artifact and close the
planning gap. Reject adapter implementation inside this tranche.

---

## Scope

In scope:

- Enumerate 46 primary Phase 2.B migration targets from existing Phase 1
  adapter maps.
- Assign stage, owner role, reviewer role, done criterion tier, dependencies,
  freeze-release posture, and adapter target path for every target.
- Define stage gates and DAG verification rules.
- Lock a citation rule for future per-surface work orders.

Out of scope:

- Editing source code.
- Implementing any adapter.
- Creating new role taxonomy, policy engine, risk engine, guard engine,
  receipt envelope, memory tier, provider method, execution phase, or kernel
  surface.
- Lifting the governance-kernel freeze globally.
- Claiming live governance proof or runtime coherence.
- Updating the public-sync repository.

---

## Target Selection Rule

The plan must use a bounded 46-target set:

- Policy: 8 non-legacy production targets from the Phase 1.P policy map.
- Risk: 16 non-legacy, non-node_modules production targets from the Phase 1.P
  risk map.
- Role: 7 non-legacy, non-false-positive production targets from the Phase
  1.I role-axis map.
- Receipt: 7 Phase 1.R receipt/ledger targets that are direct migration
  anchors or runtime-lane consumers.
- Memory: 8 non-false-positive Phase 1.M memory-tier targets.

Legacy fixtures, test-only references, generated `node_modules` copies, and
false positives may be cited as source evidence but must not become Phase 2.B
primary migration targets.

---

## Acceptance Criteria

- The plan artifact has status `MIGRATION_PLAN_AUTHORITATIVE`.
- Exactly 46 primary migration targets are listed.
- Every target has one stage, one owner role, one reviewer role, one done tier,
  a `dependsOn` value, a `freezeReleaseRequired` value, and a source path.
- Owner role and reviewer role are different.
- Dependency edges form a DAG.
- Stage gates prevent later-stage runtime work from starting before earlier
  dependencies close.
- Any future per-surface work order must cite the matching row in the plan.
- Kernel-touching work remains blocked until an HN2.c release packet exists.

---

## Evidence / Required Evidence / Verification

Required verification for this baseline:

- target row count equals 46;
- owner/reviewer roles differ on every row;
- dependency graph is acyclic by inspection;
- HN2.b and HN2.c artifacts exist before Phase 2.B plan closure;
- completion review records the no-runtime-claim boundary.

---

## Claim Boundary

This GC-018 closes the planning gap recorded as needing migration order, owner
assignment, done criterion, and dependency graph. It does not close or execute
any adapter migration itself.
