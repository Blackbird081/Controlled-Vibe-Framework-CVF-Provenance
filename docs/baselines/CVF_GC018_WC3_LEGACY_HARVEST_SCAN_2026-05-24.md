# CVF GC-018 WC-3 Legacy Harvest Scan

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

---

## Purpose

Authorize WC-3 as a documentation-only legacy harvest scan after WC-1 and
WC-2 closed. The scan converts legacy source folders into one prioritized map
for future value work, rather than opening isolated audit tranches.

## Scope / Proposed Tranche

In scope:

- `.private_reference/legacy/CVF 16.5/`
- `.private_reference/legacy/CVF ADD/`
- `.private_reference/legacy/CVF Edit/`
- cross-reference to remaining Review-CVF pain points D, E, F, G, and H

Out of scope:

- source-code changes
- route/provider/receipt/memory behavior changes
- hosted/cloud persistence
- `canReinject=true`
- public-sync changes
- implementation work orders beyond the mapping output

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- operator authorization on 2026-05-24 to proceed to WC-3 after DeepSeek rerun

## Decision / Baseline

Decision: open WC-3 as a mapping-only tranche.

Baseline: the registry already identifies high-risk legacy families, but it is
not a combined value-prioritized harvest map across CVF 16.5, CVF ADD, and CVF
Edit. WC-3 supplies that missing map.

## Required Evidence / Verification

WC-3 must produce:

- one mapping document under `docs/reference/`
- scan counts for all three requested legacy roots
- absorption status by source family
- pain-point mapping
- ranked candidate list for future work orders
- explicit claim boundary that no implementation was opened

## Claim Boundary / Approval Gate

This authorization approves mapping only. Any implementation candidate selected
from the WC-3 map requires a fresh GC-018/work order and must preserve the
existing blocked-work boundaries unless explicitly overridden.
