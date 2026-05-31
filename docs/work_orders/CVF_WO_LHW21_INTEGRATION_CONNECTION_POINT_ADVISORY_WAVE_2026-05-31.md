# CVF Agent Work Order - LHW21 Integration Connection Point Advisory Wave

Memory class: FULL_RECORD

Status: READY_FOR_CLOSURE_GATE

docType: work_order

Date: 2026-05-31

## Purpose

Dispatch the operator-assigned implementer to implement LHW21 as a
documentation-only advisory connector wave using the cleaned GC-018 and
filtered intake review.

Success means three source-verified connector specs and three completion
reviews are created, all bounded to documentation-only advisory value, with no
runtime/code/public-sync changes.

## Scope / Target / Owner Boundary

Target: one bounded LHW21 doc-only wave with T1/T2/T3 specs and completion
reviews.

Owner: CVF governance/documentation surface.

Allowed scope:

- Retain `docs/reviews/CVF_LHW21_INTEGRATION_CONNECTION_POINT_FILTERED_INTAKE_REVIEW_2026-05-31.md`
  as the source-cleanup record for this batch.
- Retain `docs/baselines/CVF_GC018_LHW21_INTEGRATION_CONNECTION_POINT_ADVISORY_WAVE_2026-05-31.md`
  as the authorization baseline for this batch.
- Create `docs/reference/CVF_LHW21_T1_EVENT_TAXONOMY_SCHEMA_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`.
- Create `docs/reference/CVF_LHW21_T2_HARD_GATE_MODE_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`.
- Create `docs/reference/CVF_LHW21_T3_RECEIPT_ENRICHMENT_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`.
- Create `docs/reviews/CVF_LHW21_T1_EVENT_TAXONOMY_SCHEMA_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`.
- Create `docs/reviews/CVF_LHW21_T2_HARD_GATE_MODE_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`.
- Create `docs/reviews/CVF_LHW21_T3_RECEIPT_ENRICHMENT_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`.
- Update this work order from READY to CLOSED only after all acceptance and
  closure gates pass.
- Update `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, and
  `AGENT_HANDOFF_V15_2026-05-29.md` only at wave closure if LHW21 is actually
  closed.

Forbidden scope:

- Any `EXTENSIONS/` code file.
- Any route file or `route.ts`.
- Any runtime receipt type or `GovernanceEvidenceReceipt` modification.
- Any framework-specific adapter implementation.
- Any public-sync clone change or push.
- Any live provider/API call.
- Any retention-registry or unrelated governance-maintenance change.
- Any R0-R3 risk taxonomy change.

Risk ceiling: R0 documentation-only.

## 1. Mission

Implement the three LHW21 advisory connector specifications from the cleaned
GC-018. Preserve the operator doctrine: external frameworks connect into CVF's
connection point; CVF does not build outbound framework adapters.

## 2. Authority Chain

- Operator instruction: 2026-05-31 request to recreate a clean Opus work order.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active handoff: `AGENT_HANDOFF_V15_2026-05-29.md`
- Filtered intake review:
  `docs/reviews/CVF_LHW21_INTEGRATION_CONNECTION_POINT_FILTERED_INTAKE_REVIEW_2026-05-31.md`
- GC-018:
  `docs/baselines/CVF_GC018_LHW21_INTEGRATION_CONNECTION_POINT_ADVISORY_WAVE_2026-05-31.md`
- Parent evidence:
  `docs/baselines/CVF_GC018_LHW18_CVF_EDIT_ABSORPTION_WAVE_2026-05-30.md`,
  `docs/baselines/CVF_GC018_LHW19_CVF_RESTRUCTURE_ABSORPTION_WAVE_2026-05-30.md`,
  `docs/baselines/CVF_GC018_IS1_GENERIC_AGENT_ADAPTER_2026-05-31.md`

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and return to
  Orchestrator.

## 3. Agent Roles

- Orchestrator / dispatcher: operator
- Implementer: Codex, reassigned by operator on 2026-05-31
- Reviewer: Codex or operator-assigned reviewer
- Operator approval required for: any scope expansion, runtime change,
  public-sync change, or live proof request.

## 4. Scope

Allowed scope and forbidden scope are defined in `Scope / Target / Owner
Boundary` above and are binding.

## 5. Required First Reads

Before editing, read:

- `CVF_SESSION_MEMORY.md` - current mode and next allowed move.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` - machine-readable state.
- `AGENT_HANDOFF_V15_2026-05-29.md` - active handoff and latest closure context.
- `docs/reviews/CVF_LHW21_INTEGRATION_CONNECTION_POINT_FILTERED_INTAKE_REVIEW_2026-05-31.md` - cleaned intake and draft-defect findings.
- `docs/baselines/CVF_GC018_LHW21_INTEGRATION_CONNECTION_POINT_ADVISORY_WAVE_2026-05-31.md` - authorization and boundaries.
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` - IS1 event and control-point source.
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` - INT-1 `cvf_validate_plan` and `cvf_emit_agent_event`.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` - current `GovernanceEvidenceReceipt` baseline.
- `docs/reference/archive/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md` - absorption control standard.

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

Expected results:

- worktree contains only this authorized LHW21 batch before Opus starts;
- pre-dispatch PASS;
- pre-implementation PASS.

If a pre-flight check fails, stop and record the failed command and result.

## 6A. Source-Fidelity Pass

Existing paths verified by this packet:

- `docs/reviews/CVF_LHW21_INTEGRATION_CONNECTION_POINT_FILTERED_INTAKE_REVIEW_2026-05-31.md`
- `docs/baselines/CVF_GC018_LHW21_INTEGRATION_CONNECTION_POINT_ADVISORY_WAVE_2026-05-31.md`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `docs/reference/archive/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Source Verification Block:

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| `AgentEventType` type exists | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` | lines 16-21 | `AgentEventType` | IS1 generic agent adapter | ACCEPT |
| `ControlPoint` type exists | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` | line 25 | `ControlPoint` | IS1 generic agent adapter | ACCEPT |
| `mapAgentEventToCvf` function exists | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` | line 101 | `mapAgentEventToCvf` | IS1 generic agent adapter | ACCEPT |
| `runtimeAdapterAuthorized` literal false exists | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` | lines 57 and 116 | `runtimeAdapterAuthorized` | `AdapterMappingResult` | ACCEPT |
| `cvf_validate_plan` MCP tool exists | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | lines 776-804 | `cvf_validate_plan` | INT-1 MCP tool | ACCEPT |
| `cvf_emit_agent_event` MCP tool exists | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | lines 811-845 | `cvf_emit_agent_event` | INT-1 MCP tool | ACCEPT |
| `GovernanceEvidenceReceipt` interface exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | lines 82-105 | `GovernanceEvidenceReceipt` | `ai/types.ts` | ACCEPT |

New Doc-Only Fields:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| `eventTaxonomySchemaAdvisoryType` | Names T1 advisory connector type. | Yes | Yes | Defined only in T1 spec. |
| `publishedEventSchema` | Describes IS1 event contract for framework authors. | Yes | Yes | Defined only in T1 spec. |
| `hardGateModeAdvisoryType` | Names T2 advisory connector type. | Yes | Yes | Defined only in T2 spec. |
| `connectionPointMode` | Describes `advisory` and `enforce` connection-entry modes. | Yes | Yes | Defined only in T2 spec. |
| `receiptEnrichmentAdvisoryType` | Names T3 advisory connector type. | Yes | Yes | Defined only in T3 spec. |
| `governanceTrace` | Proposed receipt-trace field for future forensic replay. | Yes | Yes | Defined only in T3 spec; runtime receipt type must remain unchanged. |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T1 Event Taxonomy Schema advisory | Execution Plan steps 1-3 | `docs/reference/CVF_LHW21_T1_EVENT_TAXONOMY_SCHEMA_ADVISORY_CONNECTOR_SPEC_2026-05-31.md` | `Test-Path`; line count; reviewer check | PENDING |
| T2 Hard Gate Mode advisory | Execution Plan steps 4-6 | `docs/reference/CVF_LHW21_T2_HARD_GATE_MODE_ADVISORY_CONNECTOR_SPEC_2026-05-31.md` | `Test-Path`; line count; reviewer check | PENDING |
| T3 Receipt Enrichment advisory | Execution Plan steps 7-9 | `docs/reference/CVF_LHW21_T3_RECEIPT_ENRICHMENT_ADVISORY_CONNECTOR_SPEC_2026-05-31.md` | `Test-Path`; line count; reviewer check | PENDING |
| Documentation-only boundary | Acceptance Criteria | `runtimeExecutionAuthorized=false`; no code files | `rg`; `git diff --name-status` | PENDING |
| Draft-defect cleanup retained | Completion reviews | no stale source path, no ready/authorized drift | reviewer check | PENDING |

## 7. Write Ownership

Owned files:

- `docs/reviews/CVF_LHW21_INTEGRATION_CONNECTION_POINT_FILTERED_INTAKE_REVIEW_2026-05-31.md`
- `docs/baselines/CVF_GC018_LHW21_INTEGRATION_CONNECTION_POINT_ADVISORY_WAVE_2026-05-31.md`
- `docs/reference/CVF_LHW21_T1_EVENT_TAXONOMY_SCHEMA_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`
- `docs/reference/CVF_LHW21_T2_HARD_GATE_MODE_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`
- `docs/reference/CVF_LHW21_T3_RECEIPT_ENRICHMENT_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`
- `docs/reviews/CVF_LHW21_T1_EVENT_TAXONOMY_SCHEMA_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`
- `docs/reviews/CVF_LHW21_T2_HARD_GATE_MODE_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`
- `docs/reviews/CVF_LHW21_T3_RECEIPT_ENRICHMENT_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`
- `docs/work_orders/CVF_WO_LHW21_INTEGRATION_CONNECTION_POINT_ADVISORY_WAVE_2026-05-31.md`
- session continuity files only at final closure

Write mode:

- create-only for specs and completion reviews;
- modify-listed for this work order and session continuity at closure.

## 8. Execution Plan

1. Run pre-flight gates and stop on any failure.
2. Create T1 spec with five sections: Purpose, Design, Contract, Integration
   Guidance, Verification Matrix.
3. Create T1 completion review.
4. Create T2 spec with five sections: Purpose, Design, Contract, Integration
   Guidance, Verification Matrix.
5. Create T2 completion review.
6. Create T3 spec with five sections: Purpose, Design, Contract, Integration
   Guidance, Verification Matrix.
7. Create T3 completion review with a T1/T2/T3 wave summary table.
8. Run evidence commands:
   `git diff --name-status`, `git status --short`, line counts for specs, and
   `rg "runtimeExecutionAuthorized=false"` across the three specs.
9. Run pre-closure autorun gate over the full LHW21 changed range.
10. Only if all gates pass, update this work order to closed-equivalent status
    and sync active session continuity.

## 9. Evidence Requirements

Required evidence:

- three spec files exist and are under 250 lines each;
- three completion reviews exist;
- all three specs state `runtimeExecutionAuthorized=false`;
- no code/runtime/public-sync/retention-registry file appears in
  `git diff --name-status`;
- pre-dispatch, pre-implementation, and pre-closure gates pass.

Evidence Trace Block requirements:

- Claim: spec and review existence.
- Command: `Test-Path` on all six planned output paths.
- Result: true for all six paths.
- Key path: each planned output path.
- Verdict: PASS or BLOCKED.

## 10. Acceptance Criteria

- T1 spec exists with S1-S5 and cites `AgentEventType`, `ControlPoint`, and
  `mapAgentEventToCvf`.
- T2 spec exists with S1-S5 and cites `cvf_validate_plan` advisory boundary.
- T3 spec exists with S1-S5 and cites current `GovernanceEvidenceReceipt`
  baseline while keeping `governanceTrace` doc-only.
- All three specs include `runtimeExecutionAuthorized=false`.
- Completion reviews exist for T1/T2/T3.
- No `EXTENSIONS/`, route, runtime receipt type, public-sync, or retention
  registry file is changed.
- Session continuity is updated only after actual LHW21 closure.

Fail conditions:

- Any runtime code change appears.
- Any route or receipt runtime type is modified.
- Any framework-specific adapter is created.
- Any source path is stale or missing.
- Any spec exceeds 250 lines.
- Any completion review claims public, hosted, production, live-provider, or
  runtime enforcement readiness.
- Any autorun phase gate fails.

Closure is blocked if any fail condition is present.

## 11. Review Gate

Implementation may proceed only after:

- this work order and its GC-018 exist in the workspace;
- `pre-dispatch` autorun gate passes;
- `pre-implementation` autorun gate passes.

Closure may proceed only after:

- all acceptance criteria pass;
- reviewer finds no blocking defects;
- `pre-closure` autorun gate passes.

Reviewer silence is not approval.

## 12. Closure Checklist

- All acceptance criteria satisfied or explicitly marked N/A with reason.
- Required evidence commands run.
- Autorun pre-closure gate passed with the captured `baseHead`.
- Changed-file set is inside allowed scope.
- Full T1/T2/T3 wave range included in closure evidence.
- Line-count claims are current and command-backed.
- Roadmap-to-work-order trace matrix final statuses are PASS or N/A with reason.
- Closure Diff Gate completed across GC-018, work order, specs, and reviews.
- Claim Integrity Scan completed with `git diff --name-status` and
  `git status --short`.
- Fail conditions checked and absent, or work returned BLOCKED.
- No open checkbox residue remains in closed-equivalent artifacts.
- Public catalog update N/A with reason: private provenance doc-only intake, no
  public export authorized.
- Public/provenance boundary checked.
- Active session front door, state registry, and active handoff updated only if
  LHW21 closes.
- Completion packet filed.
- Changed files listed for reviewer.
- No closed-equivalent claim remains if any autorun phase gate failed.

## 13. Return-To-Orchestrator Conditions

Return without continuing if:

- any pre-flight or autorun gate fails;
- any source path is missing;
- any required source symbol differs from this work order;
- scope conflict is discovered;
- implementation would touch runtime/code/public-sync/retention-registry files;
- any spec would exceed 250 lines;
- public/provenance boundary is unclear.

## Operator Checkpoint

operator.checkpoint.waiver: none. Operator authorized creation of this clean
work order, then reassigned implementation to Codex on 2026-05-31. No runtime
or public-sync waiver is granted.

## Resolved External Worktree Condition

The concurrent out-of-scope change in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts` was resolved as a
separate build-fix batch and committed at `e7015b9c`. It is not owned or
claimed by LHW21.

Because that separate batch sits between the original captured base and the
LHW21 artifact commit, LHW21 closure uses the clean full-wave range
`c460a8ef..HEAD`. This range contains all LHW21 T1/T2/T3 artifacts and excludes
the unrelated build-fix commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY - this is private provenance documentation-only work. No
public-sync export is authorized by this work order.

## Claim Boundary

This work order authorizes only documentation-only LHW21 advisory specs and
completion reviews. It does not authorize runtime event schema enforcement,
hard-gate implementation, receipt runtime extension, adapter code, framework
integration, live provider behavior, public export, hosted readiness,
production readiness, or release readiness.
