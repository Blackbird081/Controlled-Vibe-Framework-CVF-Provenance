# CVF GC-018 — LHW10 Workflow Connector Wave 10

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-05-28

---

## Purpose

Authorize LHW10 Workflow Connector Wave 10: three documentation-only connector
specs binding existing proven runtime surfaces into coherent chains. Each
tranche closes a gap where two or more already-closed surfaces exist but no
standard connector maps their combined output into a named advisory type.

---

## Scope

Three documentation-only connector specs:

- T1 — Workflow Transition Enforcement Advisory Connector
- T2 — Runtime Maturity Evidence Chain Connector
- T3 — Provider Health Degradation Advisory Connector

No `.ts` / `.tsx` / `.js` / `.py` file change. No `EXTENSIONS/` source file
change. No receipt envelope schema change. No public-sync repo change. No MCP
transport, tool execution, CLI invocation, memory reinjection, new role
taxonomy, or RBAC change.

---

## Source / Predecessor Evidence

- LHW9 GC-018:
  `docs/baselines/CVF_GC018_LHW9_WORKFLOW_CONNECTOR_WAVE9_2026-05-28.md`
  — Status: ACTIVE; LHW9 CLOSED_PASS_BOUNDED
- LHW9 roadmap:
  `docs/roadmaps/CVF_LHW9_WORKFLOW_CONNECTOR_WAVE9_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- LH1 ledger:
  `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — Remaining triggers for `Agent Harnesses`, `Review CVF_3.md`,
    `Review CVF_4.md`, `cortex-hub`, `free Claude Code`, `freellmapi`,
    `CVF_EDIT_ANALYSIS.md`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  — `nextAllowedMove` names LHW9 as latest CLOSED_PASS_BOUNDED; authorizes
    follow-on wave with fresh GC-018

Existing runtime sources confirmed present at HEAD `118b8d48`:

| Source surface | File | Key verified symbol |
| --- | --- | --- |
| W1 `WorkflowStateMachineProjection` | `cvf-web/src/lib/workflows/workflow-resolver.ts` line 39 | `finalState` |
| WR1 `WorkflowRecoveryReadout.currentState` | `cvf-web/src/lib/workflows/workflow-resolver.ts` line 88 | `currentState` |
| WR1 `WorkflowRecoveryAction` (4 values) | `cvf-web/src/lib/workflows/workflow-resolver.ts` line 50 | `resume_from_checkpoint`, `hold_for_reviewer_gate`, `escalate_to_governance`, `request_human_review` |
| WR1 `WorkflowRequestedTransitionDisposition` (4 values) | `cvf-web/src/lib/workflows/workflow-resolver.ts` line 56 | `valid_from_current_state`, `invalid_from_current_state`, `configured_deferred_gate`, `no_requested_transition` |
| VI1 `integratedSurfaceCount` | `cvf-web/src/lib/vertical-integration-readout.ts` line 115 | `integratedSurfaceCount` |
| VI1 `requiredSurfaceCount` | `cvf-web/src/lib/vertical-integration-readout.ts` line 114 | `requiredSurfaceCount` |
| G1 `ExecutionIdentityDecision.authority.canExecute` | `cvf-web/src/lib/execution-identity.ts` line 25–55 | `canExecute` |
| W5 `ProviderMethodFallbackStatus` (5+ values) | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` line 46 | `ready`, `missing_provider_model` |
| W5 `ProviderMethodFallbackEvaluation.status` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-fallback-normalization.ts` line 87 | `status` |
| W4 `clarityStatus` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts` line 75 | `clarityStatus` |
| LHW8-T2 `authorityChainAdvisoryType` | `docs/reference/CVF_LHW8_T2_EXECUTION_IDENTITY_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-28.md` | S2 mapping |
| LHW9-T1 `mcpApprovalAdvisoryType` | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S2 mapping |

---

## Decision / Baseline

LHW10 is authorized. Each tranche is documentation-only, binds surfaces already
CLOSED_PASS_BOUNDED in HEAD, adds no runtime authority, and extends no receipt
envelope schema.

T2 is gated on T1 CLOSED_PASS. T3 is gated on T1 + T2 CLOSED_PASS.

The blocked-work-class list in `ACTIVE_SESSION_STATE.json` remains in force.
No tranche may claim: broad external knowledge absorption, new governance
semantics, new role taxonomies, new policy risk guard engines, new receipt
envelopes, new memory tiers beyond Lane H scope, new provider execution
semantics, or public claims of coherent governed capability runtime.

---

## Required Evidence

Per tranche before CLOSED_PASS_BOUNDED:

1. Connector spec with 5 sections (S1–S5) where:
   - S2 mapping table uses field names verbatim from verified source files
   - S3 minimum fields list names each doc-only field explicitly
   - S4 boundary table labels Runtime-proven / Doc-proven / Doc-only / Not
     authorized rows accurately
   - S5 Source Verification Table has individual rows per enum value; no
     aggregate rows for multi-value types; all rows ACCEPT
2. Fast Lane audit per `docs/reference/CVF_FAST_LANE_AUDIT_TEMPLATE.md`
3. Work order per `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
   with Source Verification Table
4. Completion review with: Roadmap-To-Work-Order Trace Matrix, Closure Diff
   Gate, Claim Integrity Scan, Fail-Condition Scan, Closure Checklist, Risk /
   Corrective Action, Decision / Recommendation / Disposition
5. Governance gates PASS:
   - `check_work_order_dispatch_quality.py`
   - `check_markdown_structural_completeness.py`
   - `check_docs_governance_compat.py`
6. No code file in diff; spec line count < 250 per GC-023
7. Session continuity updated after each tranche

---

## Verification

Pre-closure governance gate:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 118b8d48 --head <lhw10-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base 118b8d48 --head <lhw10-commit> --enforce
python governance/compat/check_docs_governance_compat.py --base 118b8d48 --head <lhw10-commit> --enforce
```

---

## LHW Rejection Language Rule (operator direction 2026-05-28)

When writing a rejection log entry in any LHW roadmap, always state that the
rejection is scope-specific, not permanent:

- BAD: "rejected: requires live route"
- GOOD: "rejected *from this LHW wave* (doc-only scope) — eligible for
  live-proof roadmap after LHW waves are exhausted"

`abtop` and `gridex` are NOT permanently blocked. They are rejected from
documentation-only LHW waves because they require live route execution to prove
value. API keys are available. They become eligible once LHW waves have
exhausted all PARTIALLY_ABSORBED LH1 families.

Scope sequencing: complete all LHW connector waves first, then open live-proof
roadmap scope.

## Claim Boundary

LHW10 is a connector-normalization wave. It does not claim MCP transport, tool
execution, CLI invocation, workflow re-execution, memory reinjection, raw memory
release, new execution authority, new role taxonomy, RBAC changes, receipt
envelope extensions, external skill ingestion, provider behavior changes, hosted
readiness, production readiness, or public release readiness.
