# CVF Legacy Absorption And Public Catalog Roadmap

Memory class: SUMMARY_RECORD
Status: PROPOSED NEXT ROADMAP AFTER BOUNDED 17.05 COMPLETION

## Authorization

Operator direction on 2026-05-18:

- audit only `CVF 16.5`, `CVF 17.05`, `CVF ADD`, and `CVF Edit`;
- record newly discovered gaps instead of stopping the active roadmap;
- after standardization and completion, produce a technically accurate
  public-ready CVF catalog for users, developers, and agents to verify from
  GitHub links.

This roadmap is the proposed next continuation. It does not itself authorize
runtime implementation.

## Purpose

Turn the four approved legacy scopes into a controlled absorption backlog and
a truthful product catalog.

The catalog goal is commercial and technical:

- explain what CVF is;
- show what is already proven;
- name what is intentionally bounded;
- route users, developers, and agents to verifiable GitHub evidence;
- avoid overclaiming CVF as a complete Agent OS before runtime enforcement,
  role permissions, memory reinjection, async workers, and tool surfaces are
  actually complete.

## Scope

In scope:

- maintain the full absorption matrix and gap ledger;
- produce a public-safe technical product catalog;
- rank deferred gaps by product value and enforcement risk;
- convert selected gaps into future GC-018-ready tranches;
- keep private source folders private.

Out of scope:

- copying private legacy source into the public repository;
- running raw external repo tools;
- exposing raw external skill libraries to non-coders;
- changing public claims without live or deterministic evidence;
- reopening F-1 output-quality parity tuning.

## Non-Goals

This roadmap is not a rewrite of CVF into an external framework. It is not a
marketplace launch, not a new provider hub implementation, not an Agent OS
claim expansion, and not a broad feature implementation bundle.

## Work Plan

### Phase A - Legacy Knowledge Map Freeze

Inputs:

- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`
- `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`

Tasks:

- freeze the four-source inventory;
- assign every source concept to one owner surface;
- mark each concept with one of the six controlled dispositions defined in
  `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`: `absorbed`,
  `partially_absorbed`, `doc_only`, `not_absorbed`, `rejected_or_superseded`,
  `needs_gc018` (Claude N-4 rewrite: the prior list used the legacy 4-level
  vocabulary including `rejected_or_reference_only` and was not aligned with
  the matrix; the six-token vocabulary is the controlling set);
- prevent any additional folder from entering this audit without operator
  approval.

Acceptance Criteria:

- every reviewed source folder has an owner mapping;
- every non-absorbed concept has a ledger entry or is explicitly linked to an
  existing gap;
- every high-severity concept-axis row has either a GAP ID or an explicit
  rejection;
- every current CVF comparison cell is a concrete path or the literal `none`;
- no public-facing claim is derived directly from private source text.

### Phase B - Public Catalog Baseline

Inputs:

- public-sync repository front door;
- public claim boundaries and live evidence packets;
- latest release-gate evidence;
- Phase A owner map.

Tasks:

- publish a public-safe technical catalog draft in the public-sync clone;
- categorize capabilities as `proven`, `bounded`, or `roadmap`;
- link only to public repository paths;
- avoid private `.private_reference` links;
- align with mandatory live governance proof language.

Acceptance Criteria:

- catalog can be read independently by user, developer, or agent;
- every strong product claim has a public evidence or architecture link;
- every incomplete capability is named as roadmap or boundary, not as done.

### Phase C - Gap Triage For Implementation

Candidate gap families:

- enforceable role/permission/orchestrator contract;
- memory hierarchy plus governed reinjection;
- external capability intake certification runtime;
- MCP/tool/command action governance vocabulary;
- observability plane and operational intelligence;
- async worker and delegation lifecycle;
- graph/code intelligence context resolver;
- database execution surface;
- state machine and failure simulation suite.

Tasks:

- rank gaps by product value, governance risk, and implementation dependency;
- split each selected family into GC-018-sized slices;
- identify which slices require live provider proof;
- identify which slices are pure docs/contract.

Acceptance Criteria:

- no selected implementation slice depends on an unowned contract;
- live-proof requirements are listed before implementation starts;
- public catalog boundaries are updated before any claim expansion.

### Phase D - First Implementation Tranche

This phase must wait for a fresh GC-018.

Named future tranches:

| Tranche | Covers GAP IDs | Concept-axis rows | Proof need | GC-018 slot | Do not start before |
|---|---|---|---|---|---|
| Role/Permission tranche | GAP-17.05-002, part of GAP-17.05-005, part of GAP-17.05-012 | 1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 8.2 | deterministic contract tests; live proof only if route controls provider execution | `docs/baselines/CVF_GC018_LEGACY_ROLE_PERMISSION_TRANCHE_<date>.md` | concept-axis matrix and structured ledger crosswalk pass |
| ORCHESTRATOR tranche | GAP-17.05-001, GAP-17.05-013 | 3.1, 3.2, 3.3, 4.3, 5.3 | deterministic delegation/state tests; live proof if orchestrator changes provider execution | `docs/baselines/CVF_GC018_LEGACY_ORCHESTRATOR_TRANCHE_<date>.md` | Role/Permission tranche decision or explicit exception |
| Runtime workflow tranche | GAP-17.05-004, GAP-17.05-010, GAP-17.05-012, GAP-17.05-013, GAP-17.05-015 | 4.1, 4.2, 4.3, 7.1, 7.2, 9.2, 9.3, 10.2 | deterministic state-machine/failure simulation; live proof for governed AI behavior claims | `docs/baselines/CVF_GC018_LEGACY_RUNTIME_WORKFLOW_TRANCHE_<date>.md` | Role/Permission tranche and memory boundary decision |
| Provider method tranche | GAP-17.05-009 | 6.1, 6.2, 6.3 | live provider proof required if new provider method affects governed execution | `docs/baselines/CVF_GC018_LEGACY_PROVIDER_METHOD_TRANCHE_<date>.md` | named consuming vertical slice |
| Memory continuity tranche | GAP-17.05-011, part of GAP-17.05-013, part of GAP-17.05-015 | 5.1, 5.2, 5.3 | deterministic memory tests; live proof if reinjection affects governed AI output | `docs/baselines/CVF_GC018_LEGACY_MEMORY_CONTINUITY_TRANCHE_<date>.md` | Role/Permission tranche owner boundary |

Reason:

These tranches are the named continuation lanes required by the five-axis
methodology. None is authorized to start until its own GC-018 exists.

Acceptance Criteria:

- deterministic tests prove the contract;
- live governance proof is run if behavior claims CVF controls AI/provider
  execution;
- catalog is updated only after proof.

## Acceptance Criteria

This roadmap is ready to become the next implementation roadmap only when:

- the four-scope audit matrix is complete enough to prevent accidental folder
  expansion;
- every high-value unabsorbed concept is either in the gap ledger or explicitly
  rejected as reference-only;
- the public technical catalog exists in public-sync and links only to public
  surfaces;
- no catalog claim exceeds the latest public evidence boundary;
- a fresh GC-018 names the first implementation tranche before runtime work
  starts.

## Verification

Minimum verification for Phase A/B:

```bash
python governance/compat/check_docs_governance_compat.py
python governance/compat/check_memory_governance_compat.py
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_agent_handoff_guard_compat.py
```

Release or product behavior claims require:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

## Evidence

Current evidence anchors:

- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`
- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- public-sync `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`

## Claim Boundary

This roadmap can support public catalog drafting and future tranche planning.
It does not complete the deferred gaps and does not authorize CVF to claim full
Agent OS completeness, universal provider parity, unrestricted capability
marketplace readiness, or full legacy absorption.

## Verification Run

Commands run after Phase D tranche naming:

```bash
python governance/compat/check_docs_governance_compat.py
python governance/compat/check_memory_governance_compat.py
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_agent_handoff_guard_compat.py
```

Result: all four checks passed after named tranche rows were added.
