# CVF Closure Central Facts Packet Template

Memory class: REFERENCE_TEMPLATE

Status: ACTIVE_TEMPLATE

docType: reference

Text Encoding Exception: em dash and standard punctuation used in governance prose

## Scope / Target / Owner Boundary

Target: a copyable template for the central core packet defined by the CCLV
standard. One packet records the shared closure facts of a governed batch so that
roadmap, work order, worker return, completion review, and session entries
reference it instead of duplicating those facts.

Owner boundary: this template owns the shape of the central facts packet only. It
does not own runtime behavior, live proof, or public-sync scope, and it does not
reduce any evidence requirement.

## Applies To

Copy this template when a governed batch produces the same closure facts across
more than one governed artifact. For a small single-file batch where a separate
packet would add overhead, use the inline `## Central Facts Packet` section
pattern described in the CCLV standard instead.

## Purpose

Provide one source of truth for shared batch closure facts. Authors fill this
packet once per batch; local artifacts then carry a short Central Facts Reference
block (see the local reference rules) plus their own local view.

Standard authority:
`docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md`

Local reference rules:
`docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md`

Machine companion:
`docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json`

## How To Use

1. Copy this file to `docs/reviews/evidence/CVF_<BATCH>_CLOSURE_FACTS_<YYYY-MM-DD>.md`.
2. Fill every field in the Central Facts table. Use `PENDING` for the material
   commit before commit, and `N/A with reason: <reason>` where a field does not
   apply.
3. Optionally copy the JSON companion to the same basename with a `.json`
   extension for machine consumers.
4. In each local artifact, add the Central Facts Reference block pointing at this
   packet, plus the local view fields. Do not repeat all shared facts.
5. After the material commit, update `materialCommit` and `actualChangedSet` from
   command-backed evidence, not from memory.

## Central Facts Packet

Replace bracketed placeholders. Keep field names exactly as written; downstream
local references and any future advisory checker key on them.

| Field | Value |
|---|---|
| `batchId` | `<stable batch identifier, e.g. CCLV-T1>` |
| `baseHead` | `<material or dispatch base SHA, e.g. 9be27628>` |
| `materialCommit` | `<material closure commit SHA, or PENDING before commit>` |
| `sessionSyncCommit` | `<session-sync commit SHA, or N/A with reason: <reason>>` |
| `expectedChangedSet` | `<canonical expected repo-relative paths for the material batch>` |
| `actualChangedSet` | `<command-backed actual repo-relative paths for the material batch>` |
| `roadmapStatus` | `<final or current roadmap tranche status, or N/A with reason>` |
| `workOrderStatus` | `<final or current work-order status>` |
| `completionReview` | `<path to reviewer completion artifact, or N/A with reason>` |
| `publicExportDisposition` | `<EXPORTED | DEFERRED_PRIVATE_ONLY | blocked state>` |
| `findingRootCauseSummary` | `<root finding summary, or N/A with reason>` |
| `claimBoundary` | `<what this batch proves and does not prove>` |

## Field Notes

- `batchId` must match the GC-018 and work order Batch ID for traceability.
- `expectedChangedSet` and `actualChangedSet` mirror the Agent Operation Trace
  manifest. A mismatch is a closure defect, not a documentation preference.
- `sessionSyncCommit` is separate from `materialCommit` whenever the closure used
  a split material/session range.
- `publicExportDisposition` uses the same vocabulary as the Public Export
  Disposition guard.
- `claimBoundary` is shared by every local artifact; local artifacts may add a
  local delta but must not contradict it.

## Filled Example (Illustrative — CCLV-T1A)

This example is for illustration only; it documents an already-closed batch and
does not reopen it.

| Field | Value |
|---|---|
| `batchId` | `CCLV-T1A` |
| `baseHead` | `71b4f2ce` |
| `materialCommit` | `dcc114e6` |
| `sessionSyncCommit` | `9be27628` |
| `expectedChangedSet` | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md; docs/reference/work_order_template/README.md; docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md; docs/reference/work_order_template/CVF_WORK_ORDER_MACHINE_CLOSURE_PACKAGE_ADDENDUM.md; docs/baselines/CVF_GC018_CCLV_T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR_2026-06-16.md; docs/reviews/CVF_CCLV_T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR_WORKER_RETURN_2026-06-16.md` |
| `actualChangedSet` | same as expected (Manifest delta MATCH) |
| `roadmapStatus` | `CCLV-T1A application closed; CCLV roadmap unchanged by T1A` |
| `workOrderStatus` | `COMPLETE_PENDING_REVIEW then committed by reviewer` |
| `completionReview` | `docs/reviews/CVF_CCLV_T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR_WORKER_RETURN_2026-06-16.md` |
| `publicExportDisposition` | `DEFERRED_PRIVATE_ONLY` |
| `findingRootCauseSummary` | `RULE_GAP: template bloat via inline rule accumulation; resolved by addendum extraction` |
| `claimBoundary` | `Documentation/governance structure only; template reduced 1200->994 lines; no runtime, provider, live, or public scope` |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude combined worker/reviewer |
| Provider or surface | Claude Code / IDE session |
| Session or invocation | 2026-06-16 CCLV-T1 closure facts packet template authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Write tool |
| Target paths | `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md` |
| Allowed scope source | GC-018 CCLV-T1; work order CCLV-T1 |
| Before status evidence | base `9be27628`; file did not exist |
| After status evidence | template authored; pending commit |
| Diff evidence | new file; no prior content |
| Approval boundary | doc-only authoring; no runtime/provider/live/public scope |
| Claim boundary | repo-local trace only; no OS/user attribution |
| Agent type | Claude combined worker/reviewer |
| Invocation ID | cclv-t1-closure-facts-template-2026-06-16 |
| Expected manifest | `docs/baselines/CVF_GC018_CCLV_T1_CLOSURE_FACTS_PACKET_TEMPLATE_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T1_CLOSURE_FACTS_PACKET_TEMPLATE_2026-06-16.md`; `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md`; `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json`; `docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md`; `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`; `docs/reviews/CVF_CCLV_T1_CLOSURE_FACTS_PACKET_TEMPLATE_COMPLETION_2026-06-16.md` |
| Actual changed set | docs/baselines/CVF_GC018_CCLV_T1_CLOSURE_FACTS_PACKET_TEMPLATE_2026-06-16.md; docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T1_CLOSURE_FACTS_PACKET_TEMPLATE_2026-06-16.md; docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md; docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json; docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md; docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md; docs/reviews/CVF_CCLV_T1_CLOSURE_FACTS_PACKET_TEMPLATE_COMPLETION_2026-06-16.md |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This template defines the shape of a closure central facts packet. It does not
prove any runtime/provider behavior, live governance proof, public-release state,
or production state, and it does not reduce any existing evidence requirement.
