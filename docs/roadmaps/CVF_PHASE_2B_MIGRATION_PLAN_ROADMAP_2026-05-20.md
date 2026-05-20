# CVF Phase 2.B Migration Plan Roadmap

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL

docType: roadmap

Date: 2026-05-20

---

## Status

READY_FOR_REBUTTAL. This is a static planning artifact. It does not authorize
implementation, GC-018 filing, runtime change, provider/memory/Maika edits, or
public-sync work. It declares the migration order, owner assignment, and done
criterion structure that Phase 2.B will need before any adapter wire-up GC-018
can be filed.

## Authorization / Decision Chain

- GAP discovery record:
  `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`
  (`GAP-17.05-004`) records that broad Phase 2.B-style runtime expansion still
  needs migration order, owner assignment, done criterion, and dependency
  graph before another GC-018.
- Phase 2.A placeholder
  (`GovernedCapability.availableFrom: 'Phase-2B'`) is documented as a
  placeholder, not an execution plan.
- HN2.b owner map roadmap (parallel):
  `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
  — Phase 2.B migration must cite the owner map for any kernel-touching
  adapter.
- HN2.c freeze-release rule roadmap (parallel):
  `docs/roadmaps/CVF_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_ROADMAP_2026-05-20.md`
  — any adapter touching a frozen kernel surface must invoke the release
  process.
- Active session state authority:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json` (`currentMode:
  operator_lane_selection_active`,
  `freezePosture: governance_kernel_freeze_recommended`).
- Blocked work classes that constrain this roadmap:
  `new_governance_semantics`, `new_role_taxonomies`,
  `new_policy_risk_guard_engines`, `new_receipt_envelopes`,
  `new_memory_tiers_beyond_lane_h_scope`,
  `new_provider_execution_semantics`,
  `public_claims_of_coherent_governed_capability_runtime`.

## Purpose

Phase 1 (Phases 1.P / 1.I / 1.R / 1.M) delivered **adapter maps** identifying
46 surfaces and assigning canonical homes. Phase 2.A introduced
`GovernedCapability` with `availableFrom: 'Phase-2B'` as a placeholder for
"runtime wire-up arrives later". A bounded fixture-driven Phase 2.B slice was
already delivered on 2026-05-18; this roadmap covers the remaining broader
Phase 2.B migration-plan problem before any additional adapter wire-up can be
authorized.

The remaining Phase 2.B migration plan currently lacks four required inputs:

1. **Migration order** — which adapter migrates first; which depends on
   which.
2. **Owner assignment per surface** — who is responsible for each migration
   (agent role, not human name).
3. **Done criterion per surface** — what test/check proves a migration is
   complete.
4. **Dependency graph** — explicit edges where adapter X cannot start until
   adapter Y is migrated.

Without these, any Phase 2.B GC-018 would file blind. This roadmap declares
the structure (schema) for those four inputs and the rebuttal/GC-018 cycle
that produces the actual Phase 2.B migration plan artifact.

This roadmap does NOT enumerate all 46 surfaces. It declares the **method**
by which the migration plan is built. The enumeration is the downstream
GC-018's job.

## Scope / Target / Owner Boundary

In scope:

- Defining the schema for each of the four required inputs (order, owner,
  done, dependency).
- Defining the rebuttal/GC-018 cycle that produces the Phase 2.B migration
  plan artifact.
- Defining how the migration plan integrates with HN2.b owner map and HN2.c
  freeze-release rule.
- Defining what kinds of migrations may proceed under Phase 2.B vs which
  require freeze release first.

Out of scope:

- Listing the 46 surfaces (downstream Phase 2.B GC-018 enumerates them).
- Implementing any adapter (downstream work orders per surface).
- New role taxonomy, engine, receipt envelope, tier, method contract,
  phase.
- Code/runtime/provider/memory/Maika changes at filing time.
- Public-sync update.
- Lifting freeze posture (HN2.c-compliant release required for kernel
  surfaces).
- Authorizing Phase 2.B start before HN2.b closure.

Owner boundary: Orchestrator dispatches Phase 2.B GC-018 only after HN2.b
owner map is LOCKED; Reviewer rebuts the Phase 2.B migration plan proposal;
Worker implements adapters per-surface only after each surface's slice
GC-018 and work order.

---

## Predecessor / Source Evidence

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/` (GovernedCapability placeholder
  `availableFrom: 'Phase-2B'`)
- Phase 1.P / 1.I / 1.R / 1.M adapter map artifacts (search
  `docs/reviews/` for `PHASE_1*` and `ADAPTER_MAP*`)
- HN2.a inventory: `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
- HN2.b owner map roadmap (parallel filing)
- HN2.c freeze-release rule roadmap (parallel filing)
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`
- GAP discovery evidence:
  `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`

---

## Required First Reads (for downstream GC-018)

1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
2. HN2.b owner map artifact (must be LOCKED before Phase 2.B GC-018 cites it).
3. HN2.c freeze-release rule (binding before any kernel-touching Phase 2.B
   adapter starts).
4. Phase 1.x adapter map artifacts (enumerating the 46 surfaces).
5. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/` (GovernedCapability and
   skill registry — these are where wire-up lands).
6. `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md` (FROZEN supreme).

---

## Per-Input Sections

### Input 1 — Migration Order

`purpose`: Establish a total or partial order across the 46 surfaces so that
the next adapter to migrate is always unambiguous.

`schemaRequirements`:

A migration order artifact must declare:

- **Sort key:** explicit ordering principle (e.g., "topological order over
  dependency graph", "risk-class ascending then alphabetical"). One named
  rule, not vibes.
- **Stages:** named stages (e.g., Stage A = pure data adapters; Stage B =
  contract adapters with no kernel touch; Stage C = kernel-touching
  adapters requiring freeze release).
- **Per-surface stage assignment:** every surface assigned to exactly one
  stage; no unassigned surface.
- **Stage gate:** what must close before the next stage starts.

`forbiddenPatterns`:

- Order is not "whoever feels ready first".
- Order does not pull kernel-touching adapters into Stage A.
- No surface is unassigned.

`gc018AcceptanceSeed`:

- one named sort key;
- stage table;
- per-surface stage assignment for all 46 surfaces;
- stage gate condition for each stage transition.

### Input 2 — Owner Assignment

`purpose`: Assign an agent role responsible for each surface's migration.

`schemaRequirements`:

- **Owner role:** one role from the existing CVFRole catalog (no new role
  IDs created by this assignment).
- **Reviewer role:** different from owner; named per surface.
- **Operator escalation:** explicit path for when owner and reviewer
  disagree.
- **Coverage:** every surface assigned exactly one owner role and one
  reviewer role; no unassigned surface.

`forbiddenPatterns`:

- No new role taxonomy.
- Owner cannot self-review.
- Multiple owners per surface forbidden (use stages to split work, not
  ownership).

`gc018AcceptanceSeed`:

- owner + reviewer roles named per surface;
- every surface covered;
- owner ≠ reviewer;
- no new role ID introduced;
- escalation path named.

### Input 3 — Done Criterion

`purpose`: Define what evidence proves a single surface migration is complete.

`schemaRequirements`:

Each surface's done criterion must include:

- **Test evidence:** at least one test file/case proving the adapter
  implements the canonical contract.
- **Type evidence:** type-check passes for the adapter.
- **Governance evidence:** receipt/audit-event recorded if the surface
  passes through a runtime path.
- **Boundary evidence:** explicit statement of what the migration does NOT
  claim (e.g., "contract-only; no live runtime claim").
- **Closure review:** a completion review file under `docs/reviews/`.

`tieredCriteria`:

| Surface type | Required evidence |
| --- | --- |
| Contract-only adapter | test + type + closure review |
| Pack-local data adapter | test + type + closure review |
| Runtime adapter (no kernel touch) | test + type + governance receipt + closure review |
| Kernel-touching adapter | test + type + governance receipt + HN2.c-compliant freeze release + closure review |

`forbiddenPatterns`:

- "Tests pass locally" alone is not done.
- A closure review without test evidence is rejected.
- Kernel-touching adapter without freeze release recorded is rejected.

`gc018AcceptanceSeed`:

- tiered evidence table named;
- per-surface evidence requirement assigned;
- closure review required for every migration;
- kernel-touch tier requires explicit freeze release citation.

### Input 4 — Dependency Graph

`purpose`: Declare which surfaces cannot start until other surfaces are done.

`schemaRequirements`:

- **Edges:** explicit `dependsOn` list per surface (may be empty).
- **No cycles:** dependency graph is a DAG.
- **Critical path:** identify the longest chain of dependencies (informative
  for scheduling).
- **Cross-stage dependency:** dependencies cannot violate stage gates (a
  Stage A surface cannot depend on a Stage C surface).

`forbiddenPatterns`:

- Implicit "we'll figure it out later" dependencies.
- Cycles.
- Dependencies that violate stage gates.

`gc018AcceptanceSeed`:

- explicit edges per surface;
- DAG verification (no cycles);
- critical path identified;
- stage-gate compliance verified.

---

## Phase 2.B Migration Plan Artifact Specification

The downstream Phase 2.B GC-018 packet must produce one file:

`docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-{XX}.md`

Required structure:

1. **Header** — Memory class FULL_RECORD; status `MIGRATION_PLAN_AUTHORITATIVE`.
2. **Authority chain** — link to doctrine, HN2.b owner map (LOCKED),
   HN2.c freeze-release rule (BINDING), this roadmap, the Phase 2.B GC-018
   baseline.
3. **Stage table** — Input 1 stage definitions.
4. **Per-surface table** — one row per surface:
   `surfaceName | stage | ownerRole | reviewerRole | doneCriterionTier |
   dependsOn | freezeReleaseRequired | adapterTargetPath`.
5. **Dependency graph** — DAG visualization (textual or mermaid).
6. **Critical path** — named.
7. **Stage gate conditions** — per stage transition.
8. **Freeze release callouts** — every surface marked
   `freezeReleaseRequired: true` lists its HN2.c release prerequisite.
9. **Forbidden expansion register** — no new role, no new engine, no new
   receipt, no new tier, no new method, no new phase, no kernel surface
   added beyond HN2.a's 12.
10. **Citation rule** — any per-surface migration GC-018 must cite its row
    in this table.
11. **Change protocol** — updates to the plan require a fresh Phase 2.B
    GC-018 with rebuttal.

A machine-readable companion (`docs/reference/cvf_phase_2b_migration_plan.json`
or YAML) is permitted if the GC-018 declares it; otherwise the markdown
table is authoritative.

---

## Migration Stage Examples (advisory)

(These are illustrative; the Phase 2.B GC-018 binds the actual stage
definitions.)

- **Stage A — Pure data / contract adapters.** No runtime side effect, no
  kernel touch. Migration is type-and-test work. No freeze release.
- **Stage B — Pack-local / lane-specific adapters.** Touch a single lane
  (e.g., one governed pack, one provider method). Runtime side effect
  limited to the lane. No kernel touch.
- **Stage C — Kernel-touching adapters.** Modify or replace a canonical
  owner of one of the 12 HN2.a surfaces. **Requires HN2.c-compliant freeze
  release before start.**

Operator may approve more or fewer stages at GC-018; the schema above
holds.

---

## Cross-Surface Non-Goals

- Do not file Phase 2.B GC-018 before HN2.b owner map is LOCKED.
- Do not file kernel-touching adapter work order before HN2.c rule is
  BINDING and the per-surface release packet is approved.
- Do not bundle Phase 2.B migration plan with HN2.b or HN2.c.
- Do not author any of the 46 adapter implementations inside this artifact
  or its downstream GC-018 baseline (those are per-surface slice work
  orders).
- Do not modify code, runtime, provider, memory, Maika at filing time.
- Do not update public-sync.
- Do not claim runtime coherence from the existence of the migration plan.

## Downstream Dispatch Order

Strict order:

1. HN2.b owner map roadmap rebutted → HN2.b GC-018 → HN2.b work order →
   HN2.b completion review **LOCKS** the map.
2. HN2.c freeze-release rule roadmap rebutted → HN2.c GC-018 → HN2.c work
   order → HN2.c completion review records the rule as BINDING.
3. **Only then** — this Phase 2.B migration plan roadmap rebutted.
4. Phase 2.B GC-018 baseline filed.
5. Phase 2.B work order produces the migration plan artifact.
6. Phase 2.B completion review locks the plan.
7. Per-surface slice work orders dispatch in stage order, citing both the
   plan and (for kernel-touching surfaces) the freeze-release packet.

This roadmap may be reviewed in parallel with HN2.b and HN2.c roadmaps,
but no Phase 2.B GC-018 may be filed until HN2.b and HN2.c are both closed.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Phase 2.B GC-018 cites a not-yet-locked owner map | Hard prerequisite: HN2.b must close before Phase 2.B GC-018 |
| Kernel-touching adapter migrated without freeze release | Done-criterion tier requires HN2.c release citation; reviewer rejects otherwise |
| Migration order picked by convenience | Acceptance criterion requires one named sort key |
| Owner role expands the role taxonomy | "No new role IDs" rule in Input 2 acceptance seed |
| Done criterion drifts to "tests pass locally" | Tiered evidence table with closure review requirement |
| Dependency graph has cycles | DAG verification in acceptance criterion |
| Migration plan claims runtime coherence | Forbidden expansion register; migration plan is routing only |
| Per-surface work order skips citation back to plan | Citation rule named in the plan artifact |
| 47th surface gets added to migration | Forbidden expansion register: no kernel surface added beyond HN2.a |
| Phase 2.B becomes a unified bulk migration GC-018 | Per-surface slice work orders required; bulk migration forbidden |

## Non-Goals

- Implementation.
- Per-surface adapter authoring.
- Public-sync update.
- New role, engine, receipt, tier, method, phase, doctrine layer.
- Runtime coherence claim.
- Pain-point reopen.
- Phase 2.C or later phase planning.

## Work Plan

1. File this roadmap (filing-only).
2. Wait for HN2.b closure (map LOCKED) and HN2.c closure (rule BINDING).
3. Reviewer rebuts this roadmap.
4. If non-blocking, Orchestrator files Phase 2.B GC-018 baseline.
5. Phase 2.B work order produces the migration plan artifact.
6. Phase 2.B completion review locks the plan.
7. Per-surface slice work orders dispatch in stage order.
8. Update `CVF_SESSION_MEMORY.md` index for Phase 2.B closure if needed;
   update the GAP ledger or successor gap record to mark "Phase 2.B migration
   plan owner/order/done-criterion" as RESOLVED.

## Acceptance Criteria (for this roadmap)

- All four inputs (order, owner, done, dependency) have schema requirements
  and GC-018 acceptance seeds.
- Tiered done criterion table is named.
- DAG/dependency-graph requirement is explicit.
- HN2.b and HN2.c prerequisites are explicit and strict (not advisory).
- Stage gate concept is named.
- Per-surface citation rule is named.
- Bulk migration is explicitly forbidden.
- No GC-018, no code change, no enumeration of 46 surfaces introduced by
  this artifact.

## Verification

Static verification only at filing:

- Markdown structural completeness check.
- `CVF_SESSION_MEMORY.md` index updated to point at this roadmap if needed.
- Active review queue updated to add `phase-2b-migration-plan-roadmap`
  entry under `READY_FOR_REBUTTAL`.

## Related Artifacts

- `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
  (prerequisite — must close before Phase 2.B GC-018)
- `docs/roadmaps/CVF_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_ROADMAP_2026-05-20.md`
  (prerequisite — must be BINDING before kernel-touching adapter start)
- `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
- `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/` (GovernedCapability target)
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`

## Claim Boundary

This roadmap is a private planning artifact. It proves no runtime behavior,
authorizes no implementation, files no GC-018, changes no public-facing CVF
claim, lifts no freeze posture, modifies no doctrine, enumerates no
adapter surface, and reopens no pain point. It commits only to the next
step: a rebuttal-then-GC-018 cycle that produces a Phase 2.B migration plan
**after** HN2.b owner map is LOCKED and HN2.c freeze-release rule is BINDING.
