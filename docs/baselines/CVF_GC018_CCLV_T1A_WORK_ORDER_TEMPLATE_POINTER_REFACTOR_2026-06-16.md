# CVF GC-018 Authorization Baseline — CCLV-T1A Work Order Template Pointer Refactor

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-06-16

Batch ID: CCLV-T1A

rawMemoryReleased: false
Text Encoding Exception: em dash and standard punctuation used in governance prose

## Purpose

Authorize the bounded CCLV-T1A work order template pointer refactor under the
Central Core Local View governance refactor program. This tranche reduces the
canonical work order template from its hard-threshold saturation point (1200
lines) to a compact skeleton with stable pointer addenda, without weakening any
requirement.

## Authority Chain

- Operator dispatch prompt: `CCLV-T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR`
  (2026-06-16 session)
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  (`currentMode: central_core_local_view_prompt_header_closed_next_cclv_t1_gc018`)
- CCLV standard:
  `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md`
- CCLV roadmap:
  `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`
  (CCLV-T1 row: `READY_FOR_GC018`)
- GC-023 file-size policy:
  `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`
- Commit mode: `WORKER_MUST_NOT_COMMIT`

## Source / Predecessor Evidence

| Source | Path | Role |
|---|---|---|
| CCLV standard | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | Governing standard for this refactor pattern |
| CCLV roadmap | `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` | Roadmap authorizing CCLV-T1 pointer refactor |
| Operator dispatch prompt | CCLV-T1A session dispatch 2026-06-16 | Original work order mission |
| GC-023 policy | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | File-size enforcement that triggered this refactor |
| Existing finality addendum | `docs/reference/CVF_AGENT_WORK_ORDER_FINALITY_AND_REVIEW_CONVERSION_ADDENDUM_2026-06-12.md` | Precedent for extraction pattern |
| Existing epistemic addendum | `docs/reference/CVF_AGENT_WORK_ORDER_EPISTEMIC_PROCESS_BLOCK_ADDENDUM_2026-06-13.md` | Precedent for extraction pattern |

## Decision / Baseline / Proposed Tranche

Decision: execute CCLV-T1A as a bounded documentation-only pointer refactor.

Proposed tranche: `CCLV-T1A` — work order template pointer refactor.

Baseline state at dispatch:
- Template line count: 1200 (at hard threshold; advisory-level at 900).
- Two extraction addenda already existed (finality: 180 lines; epistemic: 101 lines).
- No stable indexed folder existed for the template family.

Target state after tranche:
- Template line count: materially below 1200 (target 700–1000 after extraction).
- Two new stable addenda in `docs/reference/work_order_template/`.
- README front door indexes the full family with section-to-addendum mapping.
- All checker-required markers remain in the template.
- All governance gates PASS.

Tranche boundary: documentation and governance structure only. No runtime code,
provider proof, public-sync, or legacy absorption is authorized.

## Problem Statement

`docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` reached exactly
1200 lines — the hard threshold for `active_markdown`. The last batch had to
compress prose to pass the guard. Compression to pass a threshold is a
governance design smell: it signals the file needs structural extraction, not
squeezing.

The file accumulated detail from every new CVF rule addition. The CCLV standard
provides the right solution: move shared long-lived detail to central addenda;
keep the template as a compact skeleton with named section pointers.

## Scope Authorization

### Authorized (CCLV-T1A)

- Reduce `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` by
  extracting long detail sections into stable addenda under a new indexed folder.
- Create `docs/reference/work_order_template/` as a stable folder for the work
  order template family.
- Create `docs/reference/work_order_template/README.md` as the folder front door
  with purpose, addendum list, section-to-addendum mapping, mandatory vs
  conditional reads, naming rules, and archive policy.
- Create `docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md`
  (stable path) — carries §6A detail: source-fidelity rules, negative search
  discipline, intake role routing, single-agent multi-role block, source
  verification table rules, MA1 section lock.
- Create `docs/reference/work_order_template/CVF_WORK_ORDER_MACHINE_CLOSURE_PACKAGE_ADDENDUM.md`
  (stable path) — carries §6E.1 detail: machine closure package table, rules,
  Acceptance Receipt Assertion Matrix template, External Artifact Hash Manifest
  template.
- Update the template to pointer/skeleton form: preserve all required section
  headings and checker-compatible marker strings; replace long rule bodies with
  compact summaries and addendum references.
- Author this GC-018 baseline and a worker return.

### Forbidden (CCLV-T1A)

- Do not rewrite historical closed work orders.
- Do not weaken or remove closure, AOT, source verification, protected-path,
  prompt-envelope, or dispatch-quality requirements.
- Do not remove a requirement unless it remains available through a referenced
  standard or addendum at the pointer location.
- Do not create many tiny files just to reduce line count; split only sections
  that are long-lived, reusable, and independently readable.
- No runtime/provider/API/live/public-sync/legacy broad scan.
- No commit (WORKER_MUST_NOT_COMMIT).

## Operator Foundation Rule Addition

This tranche also adopts the operator-directed foundation file naming rule:

- Long-lived CVF foundation/reference addenda use **stable filenames without
  date suffixes** under the indexed folder.
- Dated filenames remain appropriate for roadmaps, GC-018 packets, reviews,
  worker returns, completion evidence, and execution-only artifacts.
- When a stable addendum is materially revised, update in place; do not
  date-sprawl alongside the existing file.
- The folder README identifies the current canonical file for each addendum.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Template line count is materially below 1200 hard threshold (target 700–1000). |
| AC2 | All checker-required marker strings remain in the template (dispatch-quality PASS). |
| AC3 | Required section headings remain present for checker compatibility (markdown structural PASS). |
| AC4 | Extracted addenda are independently readable with their own Scope, Applies To, and Claim Boundary. |
| AC5 | `docs/reference/work_order_template/README.md` exists and contains folder purpose, addendum list, section-to-addendum mapping, mandatory vs conditional reads, naming rule, and archive policy. |
| AC6 | `check_governed_file_size.py --enforce` passes with zero violations. |
| AC7 | `check_markdown_structural_completeness.py --enforce` passes on changed range. |
| AC8 | `check_work_order_dispatch_quality.py --enforce` passes with zero marker violations. |
| AC9 | `check_agent_operation_trace.py --enforce` passes on changed range. |
| AC10 | `run_agent_autorun_workflow_gate.py --phase pre-implementation` COMPLIANT. |
| AC11 | Retrieval ergonomics satisfied: agent can start from template → README → read only relevant addenda. |
| AC12 | No requirement is removed without being reachable through a pointer or addendum reference. |

## Planned Changed Set

| Path | Action | Reason |
|---|---|---|
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | MODIFY | Reduce to compact skeleton with addendum pointers |
| `docs/reference/work_order_template/README.md` | CREATE | Folder front door per operator instruction |
| `docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md` | CREATE | Stable addendum for §6A source-verification detail |
| `docs/reference/work_order_template/CVF_WORK_ORDER_MACHINE_CLOSURE_PACKAGE_ADDENDUM.md` | CREATE | Stable addendum for §6E.1 machine closure package detail |
| `docs/baselines/CVF_GC018_CCLV_T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR_2026-06-16.md` | CREATE | This GC-018 baseline |

## Evidence / Verification

Pre-implementation gate commands (run before commit):

```powershell
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/check_markdown_structural_completeness.py --base 71b4f2ce --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 71b4f2ce --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 71b4f2ce --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 71b4f2ce --head HEAD
```

Expected results:

- `check_governed_file_size.py --enforce`: Violations 0; template no longer in top advisory list.
- `check_markdown_structural_completeness.py --enforce`: Violations 0; COMPLIANT.
- `check_work_order_dispatch_quality.py --enforce`: Violations 0; Marker violations 0; COMPLIANT.
- `check_agent_operation_trace.py --enforce`: Violations 0; COMPLIANT.
- `run_agent_autorun_workflow_gate.py --phase pre-implementation`: COMPLIANT.

Line count evidence:

| File | Before | After | Delta |
|---|---|---|---|
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | 1200 | 994 | -206 |
| `docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md` | n/a (new) | 212 | +212 |
| `docs/reference/work_order_template/CVF_WORK_ORDER_MACHINE_CLOSURE_PACKAGE_ADDENDUM.md` | n/a (new) | 142 | +142 |
| `docs/reference/work_order_template/README.md` | n/a (new) | 136 | +136 |

## Risk Assessment

Risk ceiling: R0 (documentation-only; no runtime, provider, or production scope).

No runtime behavior is changed. No live proof required. No public-sync authorized.
The refactor is additive for the addenda and reductive for the template body; all
extracted requirements remain reachable through pointer references.

## Dispatch Prompt Envelope

N/A with reason: operator executes directly via Claude worker session; no
separate agent handoff is expected for this batch. The work order is the operator
dispatch prompt itself.

## Claim Boundary

This baseline authorizes the CCLV-T1A pointer refactor batch only. It does not
authorize runtime behavior, provider calls, live proof, public-sync, legacy
absorption, co-work product development, or production/hosted readiness.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance baseline. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude worker |
| Provider or surface | Claude Code / IDE session |
| Session or invocation | 2026-06-16 CCLV-T1A GC-018 authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Write tool |
| Target paths | `docs/baselines/CVF_GC018_CCLV_T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR_2026-06-16.md` |
| Allowed scope source | Operator dispatch prompt CCLV-T1A; CCLV roadmap T1 row |
| Before status evidence | base `71b4f2ce`; file did not exist |
| After status evidence | GC-018 authored; WORKER_MUST_NOT_COMMIT pending Codex review |
| Diff evidence | new file; no prior content |
| Approval boundary | GC-018 authorization only; no implementation by this artifact |
| Claim boundary | repo-local trace only; no OS/user attribution |
| Agent type | Claude worker |
| Invocation ID | cclv-t1a-gc018-2026-06-16 |
| Expected manifest | `docs/baselines/CVF_GC018_CCLV_T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR_2026-06-16.md`; `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reference/work_order_template/README.md`; `docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md`; `docs/reference/work_order_template/CVF_WORK_ORDER_MACHINE_CLOSURE_PACKAGE_ADDENDUM.md` |
| Actual changed set | pending Codex review and commit |
| Manifest delta | PENDING_REVIEW |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
