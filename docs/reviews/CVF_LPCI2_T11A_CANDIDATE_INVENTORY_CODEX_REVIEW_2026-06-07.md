# CVF LPCI2-T11A Candidate Inventory Codex Review

Memory class: FULL_RECORD

Status: REVIEWED_RETURN_TO_WORKER

docType: codex_review

Date: 2026-06-07

reviewBaseHead: `db43e449`

workerReturn: `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_WORKER_RETURN_2026-06-07.md`

workerInventory: `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md`

workOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_T11A_POLICYLOCAL_CANDIDATE_INVENTORY_FOR_CLAUDE_2026-06-07.md`

## Purpose

Review the Claude T11A Candidate Inventory worker return and decide whether it
can close T11A or must return for supplementary evidence.

## Scope / Target / Owner Boundary

Target/source:

- `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_WORKER_RETURN_2026-06-07.md`
- `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md`
- external `Law use case_Codex` bundle existence observed by filesystem
  enumeration.

Owner boundary: Codex owns this review and supplement dispatch decision. Claude
owns only the worker-return artifacts it produced under
`WORKER_MUST_NOT_COMMIT`.

## Target / Source

Primary source: `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_WORKER_RETURN_2026-06-07.md`.

Supporting source: `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md`.

External source signal: filesystem enumeration of the private
`Law use case_Codex` bundle.

## Scope / Methodology

Method:

- compare worker return against the original T11A work order;
- compare original scope against operator clarification that the six files are
  part of a real Codex use-case bundle;
- classify any gap as worker execution failure or orchestration scope gap;
- preserve the no-extraction/no-ingestion/no-provider boundary.

## Review Verdict

`PASS_FOR_ORIGINAL_SCOPE__SUPPLEMENT_REQUIRED`

Claude satisfied the original dispatched work order for the six files directly
under `Policy_Local/data_input`. The return is not sufficient to close T11A
after operator clarification that the same six files are part of a deeper real
use-case bundle under:

`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex`

That bundle includes the input files, an agent request, Codex-generated
extracted text, and Codex-rendered output variants. It is therefore material
T11A provenance for later CVF-governed context-layer comparison.

## Acceptance Review

| Review item | Evidence | Disposition |
|---|---|---|
| Original six direct input candidates enumerated | Worker return and inventory list six candidate IDs `T11A-CAND-001` through `T11A-CAND-006` | PASS |
| Pilot law files excluded | Worker return records two pilot exclusions and excludes them from candidates | PASS |
| Manifest exists externally | `policylocal-t11-candidate-manifest.json`; SHA256 `e06dc12c54c3a3ecab7d468c8de996feae9f1f79b9cce568642932e2ea0cf43e` | PASS |
| Worker respected no extraction boundary | Worker return states no body extraction, OCR, ingestion, runtime query, provider call, or public-sync | PASS |
| Real use-case bundle inventoried | `Law use case_Codex` folder contains source inputs plus request, extracted text, and rendered output variants | FAIL_SUPPLEMENT_REQUIRED |

## Finding

Finding ID: `T11A-F1-REAL-USE-CASE-BUNDLE-OMITTED`

Defect class: `OPERATOR_SCOPE_CLARITY_GAP`

The original T11A work order scoped only the six direct files under
`Policy_Local/data_input`. Operator clarification after dispatch established
that the six files are also duplicated inside a real use-case bundle with
additional lineage artifacts:

- `Request for agent.docx`
- `_extracted_text/`
- `_rendered_don_kien_nghi/`

The missing bundle inventory is not a worker execution failure. It is an
orchestration scope gap caused by incomplete initial dispatch context.

## Findings / Position

Position: accept the worker return for the original direct-input inventory
scope, but do not close T11A. The real use-case bundle is now in scope for
provenance because it contains the prior unguided Codex request, extracted
text, and rendered outputs that later CVF-governed context work must compare
against.

## Risk / Corrective Action

Risk: closing T11A now would make downstream T11B/T11C work treat six direct
input files as the whole case, losing the actual request-to-output lineage.

Corrective action: dispatch a supplement work order for real use-case bundle
inventory and lineage mapping before any T11A closure decision.

## Required Remediation

Create and dispatch a T11A supplement work order that inventories the full real
use-case bundle with artifact roles and lineage.

The supplement must classify artifacts as:

- `source_input`
- `agent_request`
- `ungoverned_extracted_text`
- `ungoverned_generated_output`
- `rendered_output_variant`

The supplement must not read or summarize document body content, rerun Codex,
modify extracted output, ingest into the corpus, run provider calls, or claim
legal quality. It must create only a provenance inventory and machine-readable
manifest for later CVF-governed context-layer work.

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| Defect class | `OPERATOR_SCOPE_CLARITY_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `TEMPLATE_OR_DISPATCH_SCOPE_CANDIDATE` |
| Worker blame | `NO` |
| CVF control-plane lesson | Work orders for real operator use cases must distinguish raw input files from full execution bundles when the operator supplies prior unguided agent outputs. |
| Disposition | `N/A_WITH_REASON` |
| Reason | A supplement work order fixes the current scope gap. A reusable template/rule update is a later candidate after one more real use-case bundle demonstrates repeatability. |
| Next control action | `WORK_ORDER_SUPPLEMENT_ADDED` |

## Claim Boundary

This review does not close T11A, T11, T11B, T11C, T11D, or T12. It accepts the
worker return only for its original direct-input inventory scope and requires a
supplement before T11A closure.

No source authenticity, current-law status, legal advice quality, extraction
quality, context-readiness, runtime behavior, provider behavior, public-sync,
hosted readiness, production readiness, or public readiness is claimed.

## Next Allowed Move

Dispatch the T11A supplement work order for the `Law use case_Codex` bundle.
After the supplement returns, Codex may review both the original worker return
and supplement return together before deciding whether T11A can close.
