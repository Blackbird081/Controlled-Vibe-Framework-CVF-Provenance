# CVF GC-018 Lane B Workflow Packaging

Memory class: SUMMARY_RECORD
Status: AUTHORIZED

## Purpose

Authorize Lane B to package selected existing CVF templates into governed
workflow capability packs without claiming runtime enforcement or live
governance proof.

This baseline prevents Lane B from becoming another catalog-only milestone.
The deliverable is concrete pack artifacts with explicit schema, execution
policy, source template traceability, and a bounded claim surface.

## Scope

In scope:

- define three workflow capability packs;
- use only existing template sources in the current web product tree;
- publish pack files under the web product path;
- update the public-safe technical catalog with the correct bounded status;
- keep runtime behavior unchanged unless a later lane explicitly wires it.

Out of scope:

- runtime route selection changes;
- provider behavior changes;
- live governance claims;
- user-facing UI changes;
- full template-corpus packaging.

## Source / Predecessor Evidence

- `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_BCH_2026-05-19.md`
- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_B_C_H_2026-05-19.md`
- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/index.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/development.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/business.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/content.ts`

Path correction:

- The work order referenced `src/lib/templates.ts`.
- That file does not exist in the current tree.
- The current template source is split by category under
  `src/lib/templates/`, with `index.ts` as the aggregator.

## Decision / Baseline / Proposed Tranche

Decision: Lane B is authorized as a schema-defined workflow packaging tranche.

Selected templates:

| Lane | Template ID | Source path | Reason |
|---|---|---|---|
| Development | `app_builder_complete` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/development.ts` | Highest-value build-ready non-coder app packet; already carries protected constraints and acceptance criteria. |
| Business | `strategy_analysis` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/business.ts` | Broad strategic decision workflow; bounded form template with clear output sections and risk analysis. |
| Content | `documentation` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/content.ts` | Directly supports SOP, handoff, QA, and failure-recovery documentation required by the current CVF system upgrade. |

Required pack location:

```text
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/<template-id>/
```

Each selected template must have:

- `workflow.spec.md`;
- `execution.policy.json`;
- `receipt.schema.json`.

## Rule

Lane B may claim only that selected workflow capability packs are
schema-defined and cataloged.

Lane B must not claim:

- runtime route enforcement;
- provider enforcement;
- live governance pass;
- all-template coverage;
- full Agent OS workflow execution.

## Claim Boundary

This baseline authorizes only schema-defined workflow pack artifacts for the
three selected templates. It does not authorize runtime or live governance
claims.

## Allowed And Forbidden Requirements

Allowed:

- create documentation and JSON schema/policy files;
- mirror public-safe pack artifacts into the public-sync repository;
- update catalog rows with bounded wording;
- verify file existence and JSON parseability.

Forbidden:

- modifying execute-route runtime behavior in Lane B;
- changing provider routing;
- claiming live governance proof without running the mandatory live gate;
- citing private `.private_reference` source paths in public-sync catalog rows.

## Exceptions

None for this tranche. Any runtime wiring must move to Lane C or a later
authorized tranche.

## Enforcement Surface

Agents executing Lane B must verify:

- exactly three selected template IDs were packaged;
- each selected template has three pack files;
- pack JSON files parse successfully;
- public-sync catalog changes cite only paths that exist in public-sync or use
  path-free bounded language;
- completion packet states the claim boundary.

## Evidence / Verification

Expected verification:

```powershell
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/workflow.spec.md"
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/strategy_analysis/workflow.spec.md"
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/documentation/workflow.spec.md"
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_docs_governance_compat.py
```

Live release gate is not required for Lane B because no runtime governance
claim is made.

## Claim / Final / Verification Boundary

Final boundary: Lane B is documentation/schema packaging only. Verification is
limited to file existence, JSON parseability, catalog path checks, and document
governance gates. Runtime governance proof is explicitly outside this baseline.
