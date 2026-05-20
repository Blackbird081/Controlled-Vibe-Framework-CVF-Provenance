# CVF HN2.b Governance Kernel Owner Map Roadmap

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL

docType: roadmap

Date: 2026-05-20

---

## Status

READY_FOR_REBUTTAL. This is a static planning artifact. It does not authorize
implementation, GC-018 filing, runtime change, provider/memory/Maika edits, or
public-sync work. It declares the next step after HN2.a inventory closure.

## Authorization / Decision Chain

- Claude rebuttal on post-pain-point hardening roadmap requires HN2 split into
  HN2.a (inventory, Fast-Lane), HN2.b (owner map, GC-018), HN2.c (freeze-release
  rule, GC-018):
  `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
- HN2.a inventory CLOSED 2026-05-20:
  `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
  `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_CLOSURE_REVIEW_2026-05-20.md`
- Active session state authority:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json` (`freezePosture:
  governance_kernel_freeze_recommended`)
- Blocked work classes that constrain this roadmap (from active state):
  `new_governance_semantics`, `new_role_taxonomies`,
  `new_policy_risk_guard_engines`, `new_receipt_envelopes`,
  `new_memory_tiers_beyond_lane_h_scope`,
  `new_provider_execution_semantics`.

## Purpose

Convert the HN2.a static inventory of 12 governance-kernel surfaces into a
single authoritative **owner map** artifact that:

1. Names exactly one `canonical_owner` file/symbol per surface, or an explicit
   parallel sub-surface row where HN2.a already observed split ownership
   (for example runtime guard vs repository guard).
2. Classifies every observed alias as one of:
   `canonical_owner`, `adapter_required`, `legacy_alias`, `deferred`, `rejected`.
3. Records each classification with an evidence path and a one-line
   justification.
4. Becomes the routing artifact that future work orders cite to answer
   "where does this kernel concept live?"

The owner map does not author new semantics. It writes down the truth of what
already exists and where to direct future work.

## Scope / Target / Owner Boundary

In scope:

- 12 surfaces named in HN2.a inventory (and only those):
  Authority model, Role model, Policy decision surface, Risk model, Guard model,
  Execution lifecycle, Delegation/handoff, Receipt envelope, Memory tier model,
  Capability surface, Provider execution semantics, Vocabulary aliases.
- Producing one classification per observed alias for each surface.
- Updating `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` only if the map
  changes the canonical owner declaration there, with a baseline-recorded
  change.
- Adding `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-{XX}.md` as
  the new map artifact under the GC-018 baseline path.

Out of scope:

- No new surface added to the 12.
- No new role taxonomy, role ID, policy engine, risk engine, guard engine,
  receipt format, or memory tier.
- No code/runtime/provider/memory/Maika changes.
- No public-sync update.
- No live governance proof at filing (downstream work orders may add proof if
  the map is cited as a routing input).
- No release-posture lift.

Owner boundary: Orchestrator dispatches a single GC-018 packet after this
roadmap is rebutted; Reviewer rebuts the owner map proposal before it is
authoritative; Worker is not used for filing-only work.

---

## Predecessor / Source Evidence

- `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
  (12-surface inventory with owner candidates, aliases, terms, ambiguity)
- `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_CLOSURE_REVIEW_2026-05-20.md`
- `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
  (Claude HN2 split direction)
- `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/*.contract.ts`
- `docs/reference/CVF_AGENT_ROLE_CATALOG.md`

---

## Required First Reads

Before the GC-018 packet is written (after this roadmap passes rebuttal):

1. `CVF_SESSION/ACTIVE_SESSION_STATE.json` (current freeze posture)
2. `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
   (inventory table)
3. `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_CLOSURE_REVIEW_2026-05-20.md`
4. `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
5. `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` (current owner declarations)
6. `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md` (FROZEN supreme governance)

---

## Per-Surface Sections

Each of the 12 surfaces below records: HN2.a observed owner candidate, what the
owner map must decide, the load-bearing constraint inherited from inventory, and
the GC-018 acceptance seed.

### 1. Authority Model

`hn2aOwnerCandidate`: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`

`ownerMapDecision`: Confirm `orchestrator.contract.ts` as `canonical_owner`;
classify control matrix entries and legacy ORCHESTRATOR packets as
`legacy_alias`.

`loadBearingConstraint`: Authority chain `ECOSYSTEM/doctrine/` →
`operating-model/` → `governance/` is FROZEN and must remain the spine. Owner
map cannot replace this.

`gc018AcceptanceSeed`:

- single canonical owner file/symbol named;
- each control-matrix authority row tagged as `canonical_owner` /
  `legacy_alias` / `adapter_required` / `rejected`;
- no new authority semantics introduced.

### 2. Role Model

`hn2aOwnerCandidate`: `docs/reference/CVF_AGENT_ROLE_CATALOG.md`

`ownerMapDecision`: Confirm catalog as `canonical_owner` for role taxonomy;
classify `CVFRole`, `AgentFunctionRole`, `execute-role-resolver.ts`,
`role-permission.contract.ts` as `adapter_required` (runtime expressions) vs
`legacy_alias` (older labels). Web RBAC roles tagged separately.

`loadBearingConstraint`: G1 closed role catalog as **reference-only** absorption.
Owner map cannot expand it into runtime role IDs without G2 authorization.

`gc018AcceptanceSeed`:

- catalog confirmed canonical owner for taxonomy;
- runtime role expressions classified as `adapter_required` with clear adapter
  pointer;
- web RBAC roles tagged `parallel_surface` (do not collide with execution role
  taxonomy);
- no new role IDs introduced.

### 3. Policy Decision Surface

`hn2aOwnerCandidate`: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/policy-decision.contract.ts`

`ownerMapDecision`: Confirm policy-decision contract as `canonical_owner` for
the decision shape; classify pack-local `execution.policy.json` files as
`adapter_required` (concrete policy data per governed pack).

`loadBearingConstraint`: Pack policies must remain instance-of the contract,
not parallel implementations. Owner map cannot create a new PolicyEngine.

`gc018AcceptanceSeed`:

- contract is canonical owner;
- pack policy files declared `adapter_required` with reference back to
  contract;
- no new decision verbs added beyond `allow/deny/escalate/defer`.

### 4. Risk Model

`hn2aOwnerCandidate`: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/risk-engine.contract.ts`

`ownerMapDecision`: Confirm risk-engine contract as `canonical_owner` for
R0–R3 scale; classify `R_SCALE_POLICY_BINDING` in `types.ts` as `legacy_alias`
or `canonical_alias` depending on whether the binding is part of the contract.

`loadBearingConstraint`: R0–R3 is FROZEN. Owner map cannot introduce R4, sub-
levels, or alternate scales.

`gc018AcceptanceSeed`:

- risk-engine contract is canonical owner;
- R-scale appearances in docs/code classified as canonical_alias / legacy_alias;
- no new risk level introduced.

### 5. Guard Model

`hn2aOwnerCandidate`: `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` (runtime
guard); `governance/toolkit/05_OPERATION/CVF_GUARD_AUTHORING_STANDARD_GUARD.md`
(repository guard authoring).

`ownerMapDecision`: Recognize **two parallel guard surfaces** — runtime
guard engine and repository governance guards. Classify each guard file in
`governance/toolkit/05_OPERATION/` as `repository_guard`, and runtime guards
as `runtime_guard`. Both are canonical for their respective layers.

`loadBearingConstraint`: Runtime guard and repository guard are distinct
concerns and must not be collapsed.

`gc018AcceptanceSeed`:

- two parallel owner rows named (runtime + repository), each classified with
  the dedicated `runtime_guard` / `repository_guard` classes;
- every guard file in `governance/toolkit/05_OPERATION/` classified;
- no new guard engine introduced.

### 6. Execution Lifecycle

`hn2aOwnerCandidate`: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts`

`ownerMapDecision`: Confirm runtime-workflow contract as `canonical_owner` for
INTAKE → DESIGN → BUILD → REVIEW → FREEZE; classify `LegacyCVFPhaseAlias` and
`DISCOVERY` term as `legacy_alias` with explicit alias mapping.

`loadBearingConstraint`: Phase vocabulary is FROZEN. Owner map records aliases,
does not rename phases.

`gc018AcceptanceSeed`:

- workflow contract is canonical owner;
- every legacy phase term mapped to canonical phase;
- no new phase introduced.

### 7. Delegation / Handoff

`hn2aOwnerCandidate`: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`
(delegation); `AGENT_HANDOFF_V10_2026-05-19.md` (handoff continuity instance).

`ownerMapDecision`: Recognize delegation (orchestrator → worker) and handoff
(agent → agent across sessions) as **adjacent but separate surfaces**.
Orchestrator contract owns delegation; agent handoff format/registry owns
handoff continuity. Tag each ADR as evidence of the split.

`loadBearingConstraint`: Delegation receipt (`delegationReceiptId`) and handoff
continuity must not be merged.

`gc018AcceptanceSeed`:

- two canonical owners named, one per concern;
- ADRs cited as decision provenance;
- no merger of delegation and handoff into single envelope.

### 8. Receipt Envelope

`hn2aOwnerCandidate`: `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`
(`GovernanceEvidenceReceipt`)

`ownerMapDecision`: Confirm `GovernanceEvidenceReceipt` as the shared root
envelope. Classify `GatewayReceipt`, `web-governance-envelope.ts`,
`audit-memory-receipt.ts` as **lane-specific receipts** (`adapter_required`)
each carrying the shared evidence receipt where applicable.

`loadBearingConstraint`: No new receipt envelope. Lane-specific receipts must
remain compositions of the canonical shape.

`gc018AcceptanceSeed`:

- canonical evidence receipt named;
- each lane receipt classified as `adapter_required`;
- composition relationship recorded (which lane receipt embeds the canonical
  evidence receipt);
- no new receipt envelope type introduced.

### 9. Memory Tier Model

`hn2aOwnerCandidate`: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`

`ownerMapDecision`: Confirm classifier contract as `canonical_owner` for the
7-tier model (frozen after H1). Classify `audit-memory-receipt.ts` as a
**capture-side observer** (`adapter_required`), not a tier definition.

`loadBearingConstraint`: H2/H1 closures stand. No new tier. `canReinject: false`
and capture-vs-reinjection boundary are FROZEN.

`gc018AcceptanceSeed`:

- classifier contract is canonical owner;
- audit-memory-receipt classified as capture observer;
- no new tier or reinjection semantics.

### 10. Capability Surface

`hn2aOwnerCandidate`: `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/skill-registry.ts`

`ownerMapDecision`: Confirm skill-registry as `canonical_owner` for runtime
capability surface; classify GovernedCapability intake doctrine docs as
`canonical_alias` for the intake side; classify `full-skill-registry.ts` as
`canonical_alias` of the same runtime owner if no behavioral divergence.

`loadBearingConstraint`: GovernedCapability intake doctrine is the gate for
new skills. Owner map does not allow new skills.

`gc018AcceptanceSeed`:

- runtime skill-registry is canonical owner;
- intake doctrine docs classified as canonical_alias (intake-side);
- two skill-registry files explicitly classified (same owner or one is
  legacy_alias);
- no new skill added.

### 11. Provider Execution Semantics

`hn2aOwnerCandidate`: `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`

`ownerMapDecision`: Confirm model-gateway as `canonical_owner` for provider
execution surface; classify each method contract
(`provider-output`, `stream`, `tool-call`, `json-mode`, `reasoning`, `vision`)
as `canonical_method_contract` (parallel canonical owners per method, all
re-exported by the gateway).

`loadBearingConstraint`: Method contracts are split by design. Owner map
cannot bundle them. Vision runtime, reasoning runtime remain gated by CDH-D
rebuttal.

`gc018AcceptanceSeed`:

- gateway is canonical owner of the surface;
- each method contract recorded as canonical-per-method;
- no new method contract added;
- runtime/contract separation preserved (contract-only files are not runtime
  owners).

### 12. Vocabulary Aliases

`hn2aOwnerCandidate`: `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`
(`LegacyCVFPhaseAlias`, etc.)

`ownerMapDecision`: Confirm `types.ts` as `canonical_owner` for runtime
vocabulary aliases; classify doctrine vocabulary, role catalog terms, and
control-matrix labels as `documentation_alias`.

`loadBearingConstraint`: FROZEN doctrine vocabulary is supreme. Owner map
records aliases, does not rename canonical terms.

`gc018AcceptanceSeed`:

- types.ts is canonical owner for runtime aliases;
- doctrine/catalog/matrix terms classified;
- no canonical term renamed.

---

## Owner Map Artifact Specification

The downstream GC-018 packet must produce one file:

`docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-{XX}.md`

Required structure (informative; final form locked at GC-018 review):

1. **Header** — Memory class FULL_RECORD; status `OWNER_MAP_AUTHORITATIVE`.
2. **Authority chain** — link to doctrine, post-pain-point rebuttal, HN2.a
   inventory, this roadmap, and the slice-specific GC-018 baseline.
3. **Map table** — one row per surface alias:

   `surface | aliasObservedInHN2a | classification | rationale | evidencePath`

   Classifications restricted to enumerated set:
   `canonical_owner`, `canonical_alias`, `adapter_required`, `legacy_alias`,
   `deferred`, `rejected`, `parallel_surface`, `documentation_alias`,
   `repository_guard`, `runtime_guard`, `canonical_method_contract`.

   Class precedence must be explicit: `canonical_owner` is reserved for the
   root owner of a surface or declared sub-surface; `runtime_guard` and
   `repository_guard` are guard-model sub-surface classes;
   `canonical_method_contract` is provider-method only; `documentation_alias`
   is not a `canonical_alias`; unresolved cases default to `deferred`, not
   `canonical_owner`.

4. **Coverage assertion** — every alias listed in HN2.a inventory is
   classified; no alias omitted.
5. **Forbidden expansion register** — explicit list of what the map does NOT
   authorize (no new role, no new engine, no new receipt, no new tier, no new
   method, no new phase).
6. **Citation rule** — instruction for future work orders: when a work order
   touches a kernel surface, it must cite the owner map row.
7. **Change protocol** — owner map updates require a new GC-018 with rebuttal;
   no silent reclassification.

---

## Cross-Surface Non-Goals

- Do not file one bundled HN2.b + HN2.c + Phase 2.B GC-018.
- Do not introduce any new governance semantics.
- Do not lift `freezePosture: governance_kernel_freeze_recommended`.
- Do not change public catalog (GC-024 catalog update may follow only after
  closure, separately authorized).
- Do not modify any code, test, runtime, provider, memory, or Maika file.
- Do not author HN2.c freeze-release rule inside this artifact.

## Downstream Dispatch Order

Recommended (advisory, operator decides):

1. **Reviewer rebuttal on this roadmap** (Codex or Claude in reviewer role).
2. If non-blocking — file **HN2.b GC-018 baseline** with the owner map
   artifact specification.
3. Dispatch HN2.b work order (filing-only; produces the map file plus a
   completion review).
4. HN2.b completion review locks the owner map as authoritative.
5. HN2.c roadmap (separate artifact, see HN2.c roadmap filed in parallel) may
   then proceed.

HN2.b must close before HN2.c is dispatched. Phase 2.B GC-018 may NOT cite the
owner map until HN2.b closure.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Owner map adds new role IDs or new engine | GC-018 acceptance criteria forbid net-new IDs; reviewer rejects if any new ID appears |
| Map collapses two parallel surfaces (e.g., runtime vs repository guard) | Per-surface acceptance seeds require two canonical owners where the inventory shows two |
| Map ratifies broken alias as canonical | Each row requires evidencePath; ambiguous aliases default to `deferred`, not `canonical_owner` |
| Map becomes runtime contract instead of routing | Map is reference doc only; no contract import depends on it |
| HN2.b is bundled with HN2.c or Phase 2.B | Forbidden-bundle rule in this roadmap; separate GC-018s required |
| Map silently rewrites doctrine vocabulary | Forbidden-expansion register forbids term rename; doctrine is FROZEN |

## Non-Goals

- Implementation.
- Public-sync update.
- Freeze posture lift.
- New role taxonomy, engine, receipt, tier, method, phase.
- Runtime coherence claim.
- Pain-point reopen.

## Work Plan

1. File this roadmap (filing-only, no GC-018 yet).
2. Reviewer rebuts; if non-blocking, Orchestrator files HN2.b GC-018 baseline.
3. HN2.b work order produces the owner map file.
4. HN2.b completion review locks the map.
5. Update `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` pointer to map.
6. Update `CVF_SESSION_MEMORY.md` index entry for HN2.b closure if the active
   session front door needs a pointer refresh.

## Acceptance Criteria (for this roadmap)

- All 12 inventoried surfaces appear in this roadmap with per-surface decision,
  load-bearing constraint, and GC-018 acceptance seed.
- Enumerated classification set is named (11 classes).
- Class precedence is named so parallel/specialized classes cannot collide
  with `canonical_owner`.
- Forbidden expansion register is explicit.
- No GC-018, no code change, no new semantics introduced by this artifact.
- Replacement for `governance_kernel_freeze_recommended` posture is NOT
  claimed here (that belongs to HN2.c).

## Verification

Static verification only at filing:

- Markdown structural completeness check.
- `CVF_SESSION_MEMORY.md` index updated to point at this roadmap if needed.
- Active review queue updated to add `hn2b-owner-map-roadmap` entry under
  `READY_FOR_REBUTTAL`.

## Related Artifacts

- `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
- `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
- `docs/roadmaps/CVF_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_ROADMAP_2026-05-20.md`
  (filed in parallel; depends on HN2.b closure before activation)
- `docs/roadmaps/CVF_PHASE_2B_MIGRATION_PLAN_ROADMAP_2026-05-20.md`
  (filed in parallel; depends on HN2.b owner map before slice work begins)

## Claim Boundary

This roadmap is a private planning artifact. It proves no runtime behavior,
authorizes no implementation, files no GC-018, changes no public-facing CVF
claim, lifts no freeze posture, and reopens no pain point. It commits only to
the next step: a rebuttal-then-GC-018 cycle that produces the kernel owner map.
