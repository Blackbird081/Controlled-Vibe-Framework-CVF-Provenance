# CVF CPG-3 Governance Trace Receipt Enrichment Roadmap

Memory class: SUMMARY_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: roadmap

Date: 2026-05-31

---

## Purpose

Implement the third connection-point guard tranche: a bounded optional
`governanceTrace` field on the web `GovernanceEvidenceReceipt` for forensic
review. CPG-3 follows CPG-1 event-contract extraction and CPG-2 hard-gate
enforcement, both closed with bounded proof.

## Scope / Target / Owner Boundary

Target contract: `cvf.governanceTraceReceiptEnrichment.cpg3.v1`.

Owner surfaces:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
- focused tests under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/`
  and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/`

Boundary:

- Receipt trace entries are bounded policy summaries.
- Trace entries must not carry raw prompts, raw outputs, system prompts,
  provider keys, secrets, private memory, or framework-private context.
- `/api/execute/route.ts` must not be edited or grown.
- No public-sync, hosted-readiness, production-readiness, provider-routing, or
  universal bypass-prevention claim is authorized.

## Authorization / Decision

Decision: `READY_FOR_IMPLEMENTATION`.

Authority chain:

- Parent roadmap:
  `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- Fresh CPG-3 GC-018:
  `docs/baselines/CVF_GC018_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`
- Work order:
  `docs/work_orders/CVF_WO_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`
- Human authorization: SATISFIED on 2026-05-31 by instruction
  "CPG-3 tiep tuc".

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| CPG-2 prerequisite is closed | `EXISTS` | `docs/reviews/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_COMPLETION_2026-05-31.md` | completion packet | `CLOSED_PASS_BOUNDED` | CPG-2 completion review | ACCEPT |
| LHW21 T3 proposed trace concept exists | `EXISTS` | `docs/reference/CVF_LHW21_T3_RECEIPT_ENRICHMENT_ADVISORY_CONNECTOR_SPEC_2026-05-31.md` | Purpose and S3 contract | `governanceTrace` | LHW21 T3 advisory spec | ACCEPT |
| Current receipt type exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | lines 82-105 | `GovernanceEvidenceReceipt` | web AI types | ACCEPT |
| Current receipt builder input exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 65-81 | `BuildGovernanceEvidenceReceiptInput` | web governance envelope | ACCEPT |
| Current receipt builder exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 107-132 | `buildEvidenceReceipt` | web governance envelope | ACCEPT |
| Execute route uses receipt builder on success path | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 847-863 | `buildEvidenceReceipt` | execute route | ACCEPT |
| Execute route must not grow | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | command-backed line count | `POST` | execute route | ACCEPT: 999 physical lines |
| Builder test suite exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.test.ts` | file source | `web-governance-envelope` | vitest suite | ACCEPT |

## New Proposed Fields And Symbols

| Proposed item | Intended owner | Purpose | Runtime status now |
| --- | --- | --- | --- |
| `GovernanceTraceEntry` | `ai/types.ts` | Bounded receipt trace entry schema | DOC_ONLY_NEW |
| `governanceTrace` | `GovernanceEvidenceReceipt` | Optional ordered policy summary trace | DOC_ONLY_NEW |
| `buildGovernanceTrace` | `web-governance-envelope.ts` | Builder-owned summary trace construction | DOC_ONLY_NEW |

## Work Plan

1. Add `GovernanceTraceEntry` to the web AI types.
2. Add optional `governanceTrace` to `GovernanceEvidenceReceipt`.
3. Extend `BuildGovernanceEvidenceReceiptInput` with optional explicit
   `governanceTrace`.
4. Add builder-owned trace construction from existing fields:
   decision/risk, routing, knowledge retrieval, memory gates, and approval.
5. Add tests proving trace presence, ordering, explicit trace override, and
   exclusion of raw prompt/secret/private memory fields.
6. Add a route-consumer test proving `/api/execute` responses include
   `governanceTrace` without editing `route.ts`.
7. Run focused tests, typecheck, build, file-size guard, live release bundle,
   and autorun closure/push gates.

## Acceptance Criteria

| Criterion | Required disposition |
| --- | --- |
| Fresh CPG-3 GC-018 exists | PASS before implementation |
| Human authorization exists | PASS before implementation |
| `GovernanceTraceEntry` exists in `ai/types.ts` | PASS |
| `GovernanceEvidenceReceipt.governanceTrace` is optional | PASS |
| `buildEvidenceReceipt()` emits bounded summary trace entries | PASS |
| Explicit `governanceTrace` input remains bounded/sanitized | PASS |
| Route response includes `governanceTrace` through builder ownership | PASS |
| `route.ts` line count remains 999 and unchanged | PASS |
| Trace excludes raw prompt, raw output, system prompt, provider key, secret, and private memory | PASS |
| Release-quality governance bundle passes | PASS before closure |

## Fail Conditions

Return to orchestrator if:

- `governanceTrace` captures raw prompt, raw output, system prompt, provider
  key, secret, or private memory;
- implementation requires editing `route.ts`;
- trace enrichment changes provider routing, model choice, prompt behavior, or
  Learning Plane mutation;
- receipt enrichment is claimed as public, hosted, production, or universal
  bypass-prevention proof;
- live release proof fails and the failure cannot be diagnosed or repaired
  inside allowed scope.

## Verification / Evidence Plan

```powershell
npm run test:run -- src/lib/web-governance-envelope.test.ts src/app/api/execute/route.governance-trace.test.ts
npm run check
npm run build
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD
python scripts/run_cvf_release_gate_bundle.py --json
```

## Non-Goals

- No edit to `/api/execute/route.ts`.
- No raw prompt, raw output, system prompt, provider key, secret, or
  framework-private memory capture.
- No provider routing, model selection, prompt behavior, memory behavior, or
  Learning Plane mutation.
- No public-sync export, hosted-readiness claim, production-readiness claim, or
  universal bypass-prevention claim.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| LHW21 T3 trace proposal was doc-only | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `RESOLVED_BY_CPG3_PLAN` | Add bounded runtime receipt field under owner builder |
| `route.ts` is at hard threshold | `MAINTAINABILITY_GAP` | `GOVERNANCE_CONTROL_PLANE` | `CONTROL_IN_PLACE` | Prohibit route edit; use receipt-builder ownership |
| Trace data could leak sensitive content if underspecified | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | Tests assert summary-only trace and forbidden key absence |
| Runtime/provider/cost findings | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `N/A_WITH_REASON` | Planning performs no provider call; release proof is required at closure |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap. No public-sync artifact or catalog claim is
authorized.

Next action: assess public-safe export only after a separate public-sync work
order.

## Claim Boundary

This roadmap authorizes bounded CPG-3 receipt trace enrichment only. It does
not authorize raw capture, provider changes, Learning Plane mutation,
public-sync, hosted readiness, production readiness, or universal bypass
prevention claims.
