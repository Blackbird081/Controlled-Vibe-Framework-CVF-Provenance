# CVF HN2.c Governance Kernel Freeze-Release Rule Roadmap

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL

docType: roadmap

Date: 2026-05-20

---

## Status

READY_FOR_REBUTTAL. This is a static planning artifact. It does not authorize
implementation, GC-018 filing, runtime change, provider/memory/Maika edits, or
public-sync work. It declares the policy text needed to convert
`freezePosture: governance_kernel_freeze_recommended` from a state flag into
a binding governance rule.

## Authorization / Decision Chain

- Claude rebuttal on post-pain-point hardening roadmap requires HN2 split into
  HN2.a/HN2.b/HN2.c:
  `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
- HN2.a inventory CLOSED 2026-05-20 (read-only observation).
- HN2.b owner map roadmap filed in parallel:
  `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
- HN2.c depends on HN2.b closure before its GC-018 may be filed (the rule
  references the map).
- Active session state authority:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json` (`freezePosture:
  governance_kernel_freeze_recommended`,
  `currentMode: operator_lane_selection_active`)
- Blocked work classes that constrain this roadmap:
  `new_governance_semantics`, `new_role_taxonomies`,
  `new_policy_risk_guard_engines`, `new_receipt_envelopes`,
  `new_memory_tiers_beyond_lane_h_scope`,
  `new_provider_execution_semantics`,
  `public_claims_of_coherent_governed_capability_runtime`.

## Purpose

Codify the **freeze-release rule** for governance kernel surfaces. The rule
turns the existing recommendation
(`governance_kernel_freeze_recommended`) into a written, enforceable governance
control that future agents cannot drift past.

Concretely, the rule must answer four questions:

1. **What is frozen.** Which surfaces are under freeze (the 12 named in HN2.a /
   classified in HN2.b owner map).
2. **What "frozen" means.** What changes are blocked, what changes are
   conditionally permitted, what changes remain free.
3. **What lifts the freeze.** Conditions under which the freeze posture can be
   released (per surface or globally).
4. **Who can lift it.** Authority chain for release decisions; what evidence is
   required; what artifacts must be filed.

This is rule-making only. It does not produce a new engine, runtime path, or
role. It writes a policy document that other governance machinery (guards,
work orders, GC-018 baselines) will cite.

## Scope / Target / Owner Boundary

In scope:

- Producing one policy document
  (`governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`)
  that codifies the four answers above.
- Producing a small machine-readable companion (e.g., JSON or YAML block
  inside the policy doc) listing the 12 surfaces and per-surface freeze
  posture, so guards can read it.
- Updating `CVF_SESSION/ACTIVE_SESSION_STATE.json` `freezePosture` field
  semantics, with a baseline-recorded change (text only — no new schema
  field).
- Optionally updating `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` to
  cite the new policy.

Out of scope:

- No new schema field beyond what `freezePosture` already supports.
- No new role taxonomy, policy engine, risk engine, guard engine, receipt
  format, memory tier, or method contract.
- No code/runtime/provider/memory/Maika changes (though one repository guard
  may later be authored to mechanically enforce the rule — that is a separate
  follow-on GC-018, not this one).
- No public-sync update.
- No lifting of the existing freeze posture as part of HN2.c filing.
- No new authority chain.

Owner boundary: Orchestrator dispatches a single GC-018 packet only after
HN2.b owner map has been LOCKED as authoritative; Reviewer rebuts the rule
proposal; Worker is not used for filing-only policy work. Operator approves
the final rule before it becomes binding.

---

## Predecessor / Source Evidence

- `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
- `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`
- `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md` (FROZEN supreme)
- `governance/toolkit/05_OPERATION/` (where the rule will live)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` (current freeze posture)

---

## Required First Reads (for downstream GC-018)

1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
2. HN2.b owner map artifact (must be LOCKED before HN2.c GC-018 is filed)
3. `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
4. `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
5. `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`
6. `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md`

---

## Per-Question Sections

### Q1 — What Is Frozen

`scope`: The 12 governance-kernel surfaces classified in HN2.b owner map.

`ruleDraft`:

The freeze applies to:

- All 12 surfaces named in HN2.a inventory, as classified by HN2.b owner map.
- The classification set defined in HN2.b (canonical_owner, canonical_alias,
  adapter_required, legacy_alias, deferred, rejected, parallel_surface,
  documentation_alias, repository_guard, runtime_guard,
  canonical_method_contract).
- The canonical owner declaration per surface.

The freeze does NOT apply to:

- Adapter implementations that follow an `adapter_required` classification.
- Pack-local instances that follow a `canonical_owner` contract.
- Documentation refinements that don't change classification.

`gc018AcceptanceSeed`:

- rule names the 12 surfaces by reference to HN2.b map;
- rule names the closed classification set;
- rule states what is explicitly out of freeze scope.

### Q2 — What "Frozen" Means

`changeClasses`:

| Change | Posture |
| --- | --- |
| Rename canonical owner file/symbol | BLOCKED |
| Reclassify an alias (e.g., legacy_alias → canonical_owner) | BLOCKED without HN2.c-compliant release |
| Add new alias under an existing surface | PERMITTED if classified as legacy_alias / adapter_required and recorded in HN2.b map (requires HN2.b update, not freeze lift) |
| Add new surface to the 12 | BLOCKED |
| Add new engine, role, receipt envelope, tier, method contract, phase | BLOCKED (already in active_state blocked_work_classes) |
| Add new pack-local instance of an existing canonical contract | PERMITTED through normal GC-018 |
| Adapter implementation work that respects classification | PERMITTED through normal GC-018 |
| Documentation update without classification change | PERMITTED through Fast Lane / GC-024 |
| Lift freeze on a surface (release) | BLOCKED without HN2.c-compliant release packet |

`ruleDraft`: "BLOCKED" means a GC-018 baseline that proposes such a change
must be rejected at intake; the rebuttal verdict is BLOCKING with cite to
this rule. "PERMITTED" means normal governance applies.

`gc018AcceptanceSeed`:

- closed change-class table named verbatim in the rule;
- "BLOCKED" mapped to rebuttal action (intake reject + BLOCKING verdict);
- "PERMITTED" mapped to normal governance gate.

### Q3 — What Lifts The Freeze

`releaseConditions`:

A release packet may lift the freeze on **one named surface** (not globally)
when all five conditions hold:

1. Written justification: why the existing canonical owner / classification
   is insufficient for a real, currently-active CVF need (not hypothetical).
2. Replacement design: explicit alternative canonical owner and migration
   path for every alias the change reclassifies.
3. Evidence of harm: at least one concrete blocked work order, GC-018, or
   external pain-point that the current freeze actively prevents.
4. Reviewer rebuttal: non-blocking rebuttal from a different agent role
   than the proposer.
5. Operator approval: explicit operator authorization recorded in active
   session state.

Global lift (all 12 surfaces) is **prohibited by this rule**. Even after
HN2.c is binding, no global lift is authorized; each surface releases
independently.

`releaseRecordingRequirement`:

A release must be recorded in:

- `docs/baselines/CVF_GC018_*_FREEZE_RELEASE_*.md` (GC-018 baseline)
- HN2.b owner map (update map; new version filed; old map retained as
  superseded)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` `freezePosture` field with new
  per-surface value (text — no new schema field)

`ruleDraft`: A surface released from freeze remains under normal CVF
governance (rebuttal cycle, GC-018, work order). Release is not exemption.

`gc018AcceptanceSeed`:

- five release conditions named;
- global lift explicitly prohibited;
- release recording requirement named;
- release is not exemption from governance.

### Q4 — Who Can Lift It

`authorityChain`:

- **Proposer:** Any agent (Orchestrator, Reviewer, or Worker) may file a
  release proposal.
- **Reviewer:** Must be a different agent role than proposer. Files a
  rebuttal classified as BLOCKING / NON_BLOCKING / NON_BLOCKING_WITH_SCOPE_REFINEMENT.
- **Operator:** Holds final authority. Operator approval is required for
  any non-blocking release proposal to become binding. Recorded in active
  session state under `operatorLaneSelectionAuthority` (or successor field).
- **Doctrine:** `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md` remains supreme.
  No release can contradict doctrine. If doctrine and a release proposal
  conflict, the release is rejected at intake regardless of operator
  approval.

`ruleDraft`: The authority chain for freeze release is `doctrine →
operator → reviewer → proposer`. Reverse order (proposer self-approving) is
forbidden.

`gc018AcceptanceSeed`:

- four-role chain named verbatim;
- different-role-than-proposer rule for reviewer;
- doctrine supremacy clause;
- self-approval forbidden.

---

## Freeze-Release Rule Artifact Specification

The downstream GC-018 packet must produce one file:

`governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`

Required structure:

1. **Header** — Memory class FULL_RECORD; status `RULE_BINDING`; references
   doctrine, HN2.a inventory, HN2.b owner map, this roadmap, and the
   slice-specific GC-018 baseline.
2. **Scope** — what surfaces the rule covers (cite HN2.b map).
3. **Frozen states** — the change-class table from Q2.
4. **Release conditions** — the five conditions from Q3.
5. **Authority chain** — the four-role chain from Q4.
6. **Recording requirements** — what artifacts must be filed for each
   release.
7. **Enforcement hook (descriptive)** — names which intake/rebuttal
   workflows are expected to cite this rule. Mechanical enforcement (a
   repository guard or hook) is a separate downstream GC-018, not part of
   HN2.c.
8. **Doctrine supremacy clause** — explicit statement that doctrine
   overrides this rule in any conflict.
9. **Change protocol** — updates to this rule itself require a fresh GC-018
   with rebuttal; this rule is self-versioned.

A small machine-readable block (JSON or YAML inside the policy doc) lists
the 12 surfaces and per-surface posture (`frozen` / `released_YYYY-MM-DD`),
so future guards can read it.

---

## Cross-Surface Non-Goals

- Do not file one bundled HN2.b + HN2.c GC-018.
- Do not author HN2.b owner map inside HN2.c.
- Do not lift the existing freeze posture in HN2.c filing itself.
- Do not introduce a new doctrine layer above
  `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md`.
- Do not modify code, runtime, provider, memory, Maika.
- Do not update public-sync.
- Do not author the mechanical enforcement guard inside HN2.c (separate
  follow-on).

## Downstream Dispatch Order

Strict order:

1. HN2.b owner map roadmap rebutted (non-blocking).
2. HN2.b GC-018 baseline filed.
3. HN2.b work order produces map.
4. HN2.b completion review **LOCKS** the map.
5. **Only then** — HN2.c roadmap rebutted (this file).
6. HN2.c GC-018 baseline filed.
7. HN2.c work order produces the rule.
8. HN2.c completion review records the rule as binding.
9. Optional follow-on: a repository guard that mechanically enforces the
   rule (separate roadmap + GC-018).

HN2.c must NOT be filed at GC-018 if the owner map is not LOCKED. This
roadmap may be reviewed in parallel with HN2.b's roadmap, but no GC-018 for
HN2.c may be filed until HN2.b closure.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Rule is written before owner map locks → references a moving target | Hard prerequisite: HN2.c GC-018 may not file until HN2.b completion review locks the map |
| Rule becomes a runtime engine | Rule is a policy document; no contract import depends on it; mechanical enforcement is a separate follow-on |
| Rule authorizes silent reclassification | Authority chain requires reviewer + operator; self-approval forbidden |
| Rule enables global lift later | Global lift is explicitly prohibited even after rule is binding |
| Rule lifts freeze on filing | Out of scope; HN2.c does not lift freeze, it codifies the lift process |
| Rule contradicts doctrine | Doctrine supremacy clause required in the rule artifact |
| Future agents drift past the rule without citing it | Rule names enforcement hook (descriptive); follow-on guard mechanically enforces |
| Rule expands to cover non-kernel surfaces | Scope explicitly limited to 12 HN2.a surfaces |

## Non-Goals

- Implementation.
- Public-sync update.
- Lifting existing freeze posture.
- Mechanical enforcement guard (separate follow-on roadmap).
- New role, engine, receipt, tier, method, phase, doctrine layer.
- Pain-point reopen.

## Work Plan

1. File this roadmap (filing-only).
2. Wait for HN2.b closure (map LOCKED).
3. Reviewer rebuts this roadmap.
4. If non-blocking, Orchestrator files HN2.c GC-018 baseline.
5. HN2.c work order produces the rule file.
6. HN2.c completion review records the rule as binding.
7. Update `CVF_SESSION/ACTIVE_SESSION_STATE.json` freeze posture semantics
   text (no new schema field).
8. Update `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` to cite the rule.
9. Update `MEMORY.md` index for HN2.c closure.

## Acceptance Criteria (for this roadmap)

- All four questions (Q1–Q4) have explicit rule drafts and GC-018 acceptance
  seeds.
- Closed change-class table is named.
- Five release conditions are named.
- Four-role authority chain is named.
- Doctrine supremacy clause is named.
- Global lift is prohibited.
- HN2.b prerequisite is explicit.
- No GC-018, no code change, no new semantics introduced.

## Verification

Static verification only at filing:

- Markdown structural completeness check.
- `MEMORY.md` index updated.
- Active review queue updated to add `hn2c-freeze-release-rule-roadmap` entry
  under `READY_FOR_REBUTTAL`.

## Related Artifacts

- `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
  (prerequisite — must close before HN2.c GC-018)
- `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
- `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
- `docs/roadmaps/CVF_PHASE_2B_MIGRATION_PLAN_ROADMAP_2026-05-20.md` (consumer
  of the freeze-release rule; cites it when migration adapters touch kernel
  surfaces)
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`

## Claim Boundary

This roadmap is a private planning artifact. It proves no runtime behavior,
authorizes no implementation, files no GC-018, changes no public-facing CVF
claim, lifts no freeze posture, modifies no doctrine, and reopens no pain
point. It commits only to the next step: a rebuttal-then-GC-018 cycle that
produces a binding freeze-release rule **after** HN2.b owner map is locked.
