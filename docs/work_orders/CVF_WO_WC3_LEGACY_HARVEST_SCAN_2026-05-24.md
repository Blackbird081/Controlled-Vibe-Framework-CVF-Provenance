# CVF Work Order WC-3 Legacy Harvest Scan

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-05-24

---

## Purpose

Execute the WC-3 legacy harvest scan authorized by GC-018 and publish one
combined map that future agents can use to pick high-value implementation work.

## Scope / Owner Surface

Owner: Codex documentation/mapping role.

In scope:

- scan CVF 16.5, CVF ADD, and CVF Edit source folders;
- map source families to current absorption status;
- cross-reference remaining Review-CVF pain points;
- rank future absorption candidates.

Out of scope:

- code changes;
- public-sync changes;
- new runtime behavior;
- new provider behavior;
- new memory tier or reinjection semantics;
- new claims beyond the map.

## Authority Chain

- Operator instruction on 2026-05-24: proceed to WC-3 after DeepSeek rerun.
- Roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- GC-018:
  `docs/baselines/CVF_GC018_WC3_LEGACY_HARVEST_SCAN_2026-05-24.md`

## Agent Roles

- Codex as implementer/mapping author.
- Codex as reviewer for structural completeness and claim boundary.
- Operator as authorization source for opening WC-3.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- `docs/reviews/archive/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`

## Pre-Flight Checks

- Verify the working tree before editing.
- Count files under the three requested legacy roots.
- Confirm WC-3 remains documentation-only.
- Confirm no public-sync update is required because no public capability is
  added.

## Write Ownership

Allowed writes:

- `docs/baselines/CVF_GC018_WC3_LEGACY_HARVEST_SCAN_2026-05-24.md`
- `docs/work_orders/CVF_WO_WC3_LEGACY_HARVEST_SCAN_2026-05-24.md`
- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- `docs/reviews/CVF_WC3_LEGACY_HARVEST_SCAN_COMPLETION_2026-05-24.md`
- roadmap/session/handoff metadata needed to record closure

Forbidden writes:

- source code
- provider adapters
- execute route
- receipt envelopes
- memory runtime
- public-sync

## Protocol / Contract / Requirements

The scan must:

1. Count the files under each requested legacy root.
2. Use existing registry and blindspot audit as predecessor evidence.
3. Classify source families as implemented, partial, deferred, or rejected.
4. Rank candidates by user value, pain-point relevance, and implementation risk.
5. Close WC-3 only when the mapping document exists.

## Execution Plan

1. File GC-018 and this work order.
2. Scan and count the legacy source roots.
3. Produce the mapping document.
4. File completion review.
5. Update the roadmap acceptance status.

## Evidence Requirements

- scan counts for CVF 16.5, CVF ADD, and CVF Edit;
- mapping document path;
- ranked candidate list;
- explicit no-source-code-change statement.

## Acceptance Criteria

- [x] Mapping document created.
- [x] CVF 16.5, CVF ADD, and CVF Edit coverage recorded.
- [x] Review-CVF pain points D/E/F/G/H mapped.
- [x] Ranked candidates recorded.
- [x] No source code changed.

## Review Gate

The tranche may close only after markdown structural completeness, docs
governance, and `git diff --check` pass.

## Closure Checklist

- [x] GC-018 filed.
- [x] Work order filed.
- [x] Mapping document filed.
- [x] Completion review filed.
- [x] Roadmap updated.

## Return-To-Orchestrator Conditions

Return blocked if:

- legacy roots cannot be read;
- file counts are unavailable;
- the scan would require source-code changes;
- the operator asks to implement a candidate before the map closes.

## Operator Checkpoint

After WC-3, the operator should select whether the next implementation tranche
starts with workflow state-machine proof, memory event/context packaging, or
tool/action governance.

## Enforcement / Verification

Verification commands:

- `rg --files ".private_reference/legacy/CVF 16.5" ".private_reference/legacy/CVF ADD" ".private_reference/legacy/CVF Edit"`
- `python governance/compat/check_markdown_structural_completeness.py`
- `python governance/compat/check_docs_governance_compat.py`
- `git diff --check`

## Related Artifacts

- `docs/baselines/CVF_GC018_WC3_LEGACY_HARVEST_SCAN_2026-05-24.md`
- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- `docs/reviews/CVF_WC3_LEGACY_HARVEST_SCAN_COMPLETION_2026-05-24.md`

## Claim Boundary / Final Clause

WC-3 is a map. It does not implement the candidates it ranks and does not
authorize future work without a fresh work order.
