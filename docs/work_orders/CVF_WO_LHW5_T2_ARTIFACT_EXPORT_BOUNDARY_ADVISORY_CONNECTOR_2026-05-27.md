# CVF Work Order — LHW5-T2 Artifact Export Boundary Advisory Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW5-T2: a connector spec binding W6 artifact verification status →
V3 execution diagnostic class → LHW3-T1 failure trend signal into a single
export-boundary advisory packet. Closes the gap where W6 verifies artifact
shapes and V3 classifies diagnostic failures, but no connector defines the
advisory packet that tells an agent or non-coder what artifact shape is
acceptable, what V3 class was raised during export, and what the safe next
action is — without exposing technical field names.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed. The advisory packet does not block artifact export.

## Authority Chain

- LHW5 roadmap: `docs/roadmaps/CVF_LHW5_WORKFLOW_CONNECTOR_WAVE5_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW5_T2_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- LH1 ledger (`md2html` + artifact renderer trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- W6 completion: `docs/reviews/CVF_W6_NONCODER_ARTIFACT_EXPORT_HARDENING_COMPLETION_2026-05-24.md`
- V3 source: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`
- LHW3-T1 spec: `docs/reference/CVF_LHW3_OPERATIONAL_FAILURE_TREND_READOUT_CONNECTOR_SPEC_2026-05-27.md`
- LHW5-T1 spec: `docs/reference/CVF_LHW5_DATABASE_ACTION_BOUNDARY_CONNECTOR_SPEC_2026-05-27.md`

## Gate Condition — CHECK FIRST

```text
Gate 1 — T1 status: CLOSED_PASS
```

Read `docs/reviews/CVF_LHW5_T1_*_COMPLETION_2026-05-27.md`.

If T1 is not CLOSED_PASS, stop and report to Orchestrator.

## Agent Roles

Implementer writes spec (S1–S5) using W6, V3, and LHW3-T1 vocabulary verbatim.
Reviewer checks W6 field names verbatim, V3 `ExecutionDiagnosticClass` tokens
verbatim, LHW3-T1 signal labels verbatim, advisory-only (no blocking) explicit,
S5 Source Verification complete. Auditor confirms T1 gate documented,
`md2html` LH1 trigger recorded, no new renderer or export pipeline claimed.
No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW5_ARTIFACT_EXPORT_BOUNDARY_ADVISORY_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
New renderers, export pipelines, and runtime enforcement remain blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. T1 completion (understand the database boundary chain T2 builds beside)
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/deliverable-pack.ts`
   — confirm W6 fields: `PackArtifactVerification`, `PackArtifactVerificationStatus`
   values (`PASS`, `PASS_WITH_WARNINGS`, `FAIL`), `PackArtifactVerificationCheck`,
   `PackArtifactVerificationSeverity` values (`blocking`, `warning`);
   confirm `artifactVerification.status` field path
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`
   — confirm V3 `ExecutionDiagnosticClass` export-relevant values:
   `provider_empty_output`, `policy_blocked`, `routing_denied`, `unknown_error`;
   confirm `ExecutionDiagnostic.class` field name; confirm `classifyProviderError`
6. `docs/reference/CVF_LHW3_OPERATIONAL_FAILURE_TREND_READOUT_CONNECTOR_SPEC_2026-05-27.md`
   — confirm LHW3-T1 trend signal labels: `overconstraint signal`,
   `provider instability signal`, `underspecification signal`,
   `degraded-output or drift signal`, `audit gap signal`; confirm advisory-only
7. `docs/roadmaps/CVF_LHW5_WORKFLOW_CONNECTOR_WAVE5_ROADMAP_2026-05-27.md`
   — confirm T2 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| W6 `PackArtifactVerificationStatus` values | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/deliverable-pack.ts` | lines 49-52 | `PASS`, `PASS_WITH_WARNINGS`, `FAIL` | `PackArtifactVerificationStatus` | ACCEPT |
| W6 `PackArtifactVerificationSeverity` values | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/deliverable-pack.ts` | line 54 | `blocking`, `warning` | `PackArtifactVerificationSeverity` | ACCEPT |
| W6 `PackArtifactVerification.status` field | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/deliverable-pack.ts` | lines 74-78 | `status`, `checks`, `provenance` | `PackArtifactVerification` | ACCEPT |
| V3 `ExecutionDiagnosticClass` tokens | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts` | lines 16-32 | `provider_empty_output`, `policy_blocked`, `routing_denied`, `unknown_error`, `model_unavailable` | `ExecutionDiagnosticClass` | ACCEPT |
| V3 `ExecutionDiagnostic.class` field | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts` | lines 54-58 | `class: ExecutionDiagnosticClass` | `ExecutionDiagnostic` | ACCEPT |
| LHW3-T1 trend signal labels | `docs/reference/CVF_LHW3_OPERATIONAL_FAILURE_TREND_READOUT_CONNECTOR_SPEC_2026-05-27.md` | lines 46-52 (approx) | `overconstraint signal`, `provider instability signal`, `underspecification signal`, `degraded-output or drift signal`, `audit gap signal` | LHW3-T1 trend mapping | ACCEPT |

New doc-only fields proposed by this work order: `exportAdvisoryId`,
`exportAdvisoryType`, `w6VerificationStatus`, `v3DiagnosticClass`,
`exportPlainMessage`, `exportSuggestedNextStep`, and `exportAdvisoryBlocking`.
These must be labeled documentation-only in the connector spec.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW5_ARTIFACT_EXPORT_BOUNDARY_ADVISORY_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc binding W6 artifact verification
  status → V3 execution diagnostic class → LHW3-T1 failure trend signal into
  a plain-language export-boundary advisory packet.
- State what it is not: not a W6/V3 runtime extension; not a new renderer or
  export pipeline; not a workflow blocker.
- Explicit statement: "This connector does not block artifact export. The
  export-boundary advisory packet is a non-blocking governance record. An agent
  or operator may read it to understand what failed and what is safe to try
  next, but ignoring it does not prevent a workflow from running."

### S2 — W6 status + V3 class to advisory type mapping

Table columns: `W6 verification status` | `V3 diagnostic class` |
`LHW3-T1 trend signal (where applicable)` | `Advisory type` |
`Plain-language message` | `Suggested next step`

Minimum rows:

- `FAIL` + `policy_blocked` + `overconstraint signal` → **Policy Block Advisory**
  → "CVF blocked the export because the output didn't meet the current policy."
  → "Try a lower-risk request or contact your administrator."
- `FAIL` + `provider_empty_output` + `provider instability signal` → **Provider Failure Advisory**
  → "The AI provider returned no usable content for this export."
  → "Wait a moment and try again, or check provider status."
- `PASS_WITH_WARNINGS` + `unknown_error` → **Quality Warning Advisory**
  → "The export completed but CVF detected potential quality issues."
  → "Review the exported content carefully before using it."
- `FAIL` + `routing_denied` → **Routing Denied Advisory**
  → "CVF could not route this export to an available provider."
  → "Try a lower-risk workflow or contact your administrator."
- `PASS` (no diagnostic) → no advisory generated; boundary satisfied.

All W6 status and V3 class tokens must be used verbatim from source files.

### S3 — Export advisory packet minimum fields

Prose + field list (max 10 lines):

Every artifact export advisory packet must contain:

- `exportAdvisoryId`: unique token
- `exportAdvisoryType`: one of `policy_block` | `provider_failure` |
  `quality_warning` | `routing_denied` | `none`
- `w6VerificationStatus`: from W6 `PackArtifactVerificationStatus`
- `v3DiagnosticClass`: from V3 `ExecutionDiagnosticClass` when present
- `exportPlainMessage`: non-technical human-readable message
- `exportSuggestedNextStep`: one-sentence action for the operator or agent
- `exportAdvisoryBlocking`: always `false`

State explicitly: "These fields are documentation-only minimum requirements.
`exportAdvisoryBlocking=false` is invariant. The advisory packet does not
extend `GovernanceEvidenceReceipt` or any existing receipt envelope."

### S4 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| W6 artifact verification | Runtime (cvf-web DeliverablePack) | Stable |
| V3 execution diagnostic classification | Runtime (cvf-web route) | Stable |
| LHW3-T1 trend signal computation | Document-only (LHW3-T1) | Future: trend aggregator |
| W6→V3 signal-to-advisory mapping | Document-only | Future: export advisory engine |
| Advisory packet dispatch | Document-only | Future: operator-facing notification |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

### S5 — Source Verification Table (mandatory)

Required columns: `Claimed item` | `Source file` | `Verified line/section` |
`Verified path or symbol` | `Owning interface/function/schema` | `Disposition`

Cover every W6 status token, V3 diagnostic class token, and LHW3-T1 signal
label cited in S2 and S3.

## Pre-Flight

- [ ] T1 CLOSED_PASS confirmed
- [ ] Working tree clean
- [ ] All required first reads done
- [ ] W6 `PackArtifactVerificationStatus` tokens confirmed from source files
- [ ] V3 `ExecutionDiagnosticClass` tokens confirmed from source files
- [ ] LHW3-T1 trend signal labels confirmed from spec

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Confirm T1 gate.
2. Read all required first reads.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw5_t2_complete`).
7. Commit: `docs(lhw5-t2): add artifact export boundary advisory connector spec`.
8. Write completion review; include T3 gate answer.

Spec size guard: < 200 lines. Trim S3 prose if approaching 180 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 maps minimum 5 W6+V3 combinations to advisory types
- `exportAdvisoryBlocking=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw5_t2_complete`
- Completion review written with T3 gate answer

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 covers minimum 5 signal-to-advisory combinations
- [ ] `exportAdvisoryBlocking=false` invariant explicit in S1 and S3
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated

## T3 Gate Output (required in completion review)

Answer explicitly: "Was a concrete failure simulation scenario packet gap
identified during T2 work?"

- YES → describe gap in one sentence; T3 proceeds.
- NO → "No gap found. T3 proceeds per roadmap rationale."
  (T3 proceeds regardless — this output is informational.)

## Review Gate

Before committing: Reviewer perspective completed; all W6/V3 field names
verbatim; LHW3-T1 signal labels verbatim; `exportAdvisoryBlocking=false`
explicit; S5 complete with no `BLOCKED_SOURCE_NOT_FOUND` rows; no code file
in diff.

## Closure Checklist

- [ ] T1 gate confirmed documented
- [ ] Spec created with all 5 sections
- [ ] S2 advisory mapping uses W6+V3+LHW3-T1 vocabulary verbatim
- [ ] `exportAdvisoryBlocking=false` explicit
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] S4 boundary table honest; no doc-only row labeled Runtime
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T3 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- T1 gate is not CLOSED_PASS;
- any required first read file is missing;
- a W6 status token or V3 diagnostic class token cannot be confirmed from
  source files;
- writing the connector requires creating a new renderer, export pipeline, or
  blocking artifact export;
- spec exceeds 200 lines before S4 is complete.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by T1
CLOSED_PASS and source-verified W6/V3/LHW3-T1 vocabulary; no operator checkpoint
required unless a new renderer, export pipeline, or workflow-blocking requirement
is discovered during implementation.

## Claim Boundary

LHW5-T2 produces a documentation artifact. It does not claim W6/V3 runtime
extension, new artifact renderer, export pipeline, receipt envelope extension,
provider behavior, hosted readiness, production readiness, or public release
readiness.
