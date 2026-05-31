# CVF Agent Work Order - CPG-3 Governance Trace Receipt Enrichment

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-31

## Purpose

Execute the bounded CPG-3 receipt enrichment tranche after fresh GC-018 and
recorded human authorization. This work order turns the LHW21 T3 `governanceTrace`
proposal into an optional runtime receipt field under the web receipt owner
without changing provider execution, route ownership, public status, or raw
data capture policy.

## 1. Mission

Implement bounded CPG-3 receipt enrichment by adding optional
`governanceTrace` summaries to `GovernanceEvidenceReceipt` through the web
receipt owner type and builder. Success means route responses can replay
summary-level governance checkpoints without exposing raw prompts, raw outputs,
system prompts, provider keys, secrets, or framework-private memory.

## Scope / Target / Owner Boundary

Target contract: `cvf.governanceTraceReceiptEnrichment.cpg3.v1`.

Owner boundary: web receipt schema and builder only. The route consumes the
field through existing `buildEvidenceReceipt()` calls; `route.ts` is explicitly
forbidden.

Allowed implementation surfaces are listed in Section 4 and Section 7.
Forbidden route/provider/public/raw-capture surfaces are binding fail
conditions.

## 2. Authority Chain

- Operator instruction: 2026-05-31 "CPG-3 tiep tuc"
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Parent roadmap:
  `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- CPG-3 roadmap:
  `docs/roadmaps/CVF_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_ROADMAP_2026-05-31.md`
- Fresh CPG-3 GC-018:
  `docs/baselines/CVF_GC018_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`
- Active handoff: `AGENT_HANDOFF_V15_2026-05-29.md`

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and reconcile
  before implementation.

## 3. Agent Roles

- Orchestrator / dispatcher: Codex under operator instruction.
- Implementer: Codex.
- Reviewer: Codex closure review plus machine gates.
- External authorization required for: scope expansion, route edit, public-sync,
  live/provider proof outside the required release bundle, secrets/quota beyond
  existing release proof, risk-level increase, or claim-boundary change.

## 4. Scope

Allowed scope:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.governance-trace.test.ts`
- `docs/baselines/CVF_GC018_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`
- `docs/roadmaps/CVF_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_ROADMAP_2026-05-31.md`
- `docs/work_orders/CVF_WO_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`
- `docs/reviews/CVF_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_COMPLETION_2026-05-31.md`
- `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- Session continuity updates are allowed for closure sync.

Forbidden scope:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- provider routing, provider prompt, model selection, memory mutation, Learning
  Plane mutation, public-sync, hosted deployment, production-readiness claim,
  universal bypass-prevention claim, raw prompt/output capture, secrets, or
  framework-private memory capture.

Risk ceiling: R2.

## 5. Required First Reads

Before editing implementation files, read:

- `docs/baselines/CVF_GC018_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`
- `docs/roadmaps/CVF_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_ROADMAP_2026-05-31.md`
- `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- `docs/reference/CVF_LHW21_T3_RECEIPT_ENRICHMENT_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.test.ts`

## 6. Pre-Flight Checks

Capture base before implementation:

```powershell
git rev-parse --short HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

Expected results:

- CPG-3 GC-018, roadmap, and work order are dispatchable.
- Active session allows CPG-3 after fresh GC-018 and recorded human authorization.

Mandatory Gate-Failure Remediation Protocol:

- If a failure is inside Allowed scope, repair it and rerun the failed gate.
- Routine guard failures inside Allowed scope, including missing `N/A with
  reason`, stale closure residue, source-verification corrections, and allowed
  continuity sync, must be repaired and rerun by the worker.
- Escalate only if remediation would exceed Allowed scope, change the claim
  boundary, release an additional hold, change risk level, open public-sync,
  consume new secrets/quota beyond required release proof, touch forbidden
  paths, or perform destructive/irreversible actions.

## 6A. Source-Fidelity Pass

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| CPG-2 prerequisite is closed | `EXISTS` | `docs/reviews/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_COMPLETION_2026-05-31.md` | completion packet | `CLOSED_PASS_BOUNDED` | CPG-2 completion review | ACCEPT |
| LHW21 T3 proposed trace concept exists | `EXISTS` | `docs/reference/CVF_LHW21_T3_RECEIPT_ENRICHMENT_ADVISORY_CONNECTOR_SPEC_2026-05-31.md` | Purpose and S3 contract | `governanceTrace` | LHW21 T3 advisory spec | ACCEPT |
| Current receipt type exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | line 99 | `GovernanceEvidenceReceipt` | web AI types | ACCEPT |
| Current receipt builder input exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 65-81 | `BuildGovernanceEvidenceReceiptInput` | web governance envelope | ACCEPT |
| Current receipt builder exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | line 245 | `buildEvidenceReceipt` | web governance envelope | ACCEPT |
| Execute route uses receipt builder on success path | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 848 | `buildEvidenceReceipt` | execute route | ACCEPT |
| Execute route is at hard threshold | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | command-backed line count | `POST` | execute route | ACCEPT: 999 physical lines |
| Builder test suite exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.test.ts` | file source | `web-governance-envelope` | vitest suite | ACCEPT |

## 6B. New Proposed Fields And Symbols

| Proposed item | Intended owner | Purpose | Runtime status before implementation |
| --- | --- | --- | --- |
| `GovernanceTraceEntry` | `ai/types.ts` | Bounded receipt trace entry schema | IMPLEMENTED |
| `governanceTrace` | `GovernanceEvidenceReceipt` | Optional ordered policy summary trace | IMPLEMENTED |
| `buildGovernanceTrace` | `web-governance-envelope.ts` | Builder-owned summary trace construction | IMPLEMENTED |

## 6C. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Fresh CPG-3 GC-018 exists | Section 2 | GC-018 path | `Test-Path` and dispatch gate | PASS |
| Human authorization exists | Section 2 | Authority chain | operator instruction 2026-05-31 | PASS |
| Add `GovernanceTraceEntry` | Section 8 | `ai/types.ts` | focused tests + typecheck | PASS |
| Add optional `governanceTrace` | Section 8 | `GovernanceEvidenceReceipt` | focused tests + typecheck | PASS |
| Builder emits bounded trace | Section 8 | `buildEvidenceReceipt()` | builder tests | PASS |
| Route consumes trace without route growth | Sections 4 and 8 | route response test | route-consumer test + route line count | PASS |
| No sensitive raw capture | Sections 4 and 10 | trace test assertions | builder and route tests | PASS |
| Release-quality proof | Section 9 | release bundle output | `python scripts/run_cvf_release_gate_bundle.py --json` | PASS |

## 7. Write Ownership

Owned files or modules:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.governance-trace.test.ts`
- `docs/baselines/CVF_GC018_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`
- `docs/roadmaps/CVF_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_ROADMAP_2026-05-31.md`
- `docs/work_orders/CVF_WO_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`
- `docs/reviews/CVF_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_COMPLETION_2026-05-31.md`
- `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Forbidden paths:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- public-sync clone
- provider adapter implementation files
- MCP INT1 files unless a separate CPG-3 defect proves they are required

Write mode: modify-listed plus create completion/test file.

## 8. Execution Plan

1. Commit or validate the CPG-3 dispatch packet and run pre-dispatch gates.
2. Run pre-implementation gates before code edits.
3. Add `GovernanceTraceEntry` and optional `governanceTrace` to the receipt
   type.
4. Add builder-owned `buildGovernanceTrace` logic using only summary fields:
   decision, risk level, routing decision, knowledge summary, approval marker,
   durable-memory receipt presence, and AIF-memory receipt presence.
5. Sanitize explicit trace input so disallowed keys are not carried into the
   receipt.
6. Extend `web-governance-envelope.test.ts`.
7. Add `route.governance-trace.test.ts` to prove existing route builder calls
   return `governanceTrace`.
8. Run focused tests, typecheck, build, file-size guard, release bundle, and
   autorun closure gates.
9. File completion review, update parent roadmap and session continuity, commit,
   run pre-push, and push.

## 9. Evidence Requirements

Required evidence:

- `git diff --name-status <baseHead> HEAD`
- `npm run test:run -- src/lib/web-governance-envelope.test.ts src/app/api/execute/route.governance-trace.test.ts`
- `npm run check`
- `npm run build`
- command-backed `route.ts` line count remains 999
- `python governance/compat/check_governed_file_size.py --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD`
- `python scripts/run_cvf_release_gate_bundle.py --json`

Evidence Trace Block requirements:

- Claim: CPG-3 trace field is bounded and summary-only.
- Command: focused tests + typecheck/build + release bundle.
- Result: PASS before closure.
- Key path: `ai/types.ts`, `web-governance-envelope.ts`, route consumer test.
- Verdict: close only when machine gates pass.

## 10. Acceptance Criteria

| Criterion | Required disposition |
| --- | --- |
| `GovernanceTraceEntry` exists in `ai/types.ts` | PASS |
| `GovernanceEvidenceReceipt.governanceTrace` is optional | PASS |
| `buildEvidenceReceipt()` emits trace entries from existing summary metadata | PASS |
| Explicit `governanceTrace` input is sanitized and bounded | PASS |
| Route response includes `governanceTrace` without editing `route.ts` | PASS |
| Trace excludes raw prompt, raw output, system prompt, provider key, secret, and private memory | PASS |
| `route.ts` remains 999 lines | PASS |
| Release-quality governance proof passes | PASS |

Fail conditions:

| Fail condition | Closure disposition |
| --- | --- |
| `route.ts` is modified or grows | BLOCKED |
| Trace includes raw prompt/output/system prompt/provider key/secret/private memory | BLOCKED |
| Provider routing, model, prompt, memory, or Learning Plane behavior changes | BLOCKED |
| Public/hosted/production/universal-bypass claim appears | BLOCKED |
| Release bundle fails without diagnosed allowed-scope remediation | BLOCKED |

## 11. Review Gate

Implementation may proceed only after:

- fresh CPG-3 GC-018 exists;
- recorded human authorization exists;
- `pre-dispatch` autorun gate passes;
- `pre-implementation` autorun gate passes.

Closure may proceed only after:

- focused tests, typecheck, build, file-size guard, and release bundle pass;
- `pre-closure` autorun gate passes;
- completion review records public export disposition and claim boundary.

Mandatory remediation rule:

- A gate failure inside this work order's Allowed scope is authorization to
  repair and rerun, not a preference checkpoint.

## 12. Closure Checklist

| Item | Resolution |
| --- | --- |
| Acceptance criteria satisfied | PASS |
| Required tests and evidence commands run | PASS |
| Autorun pre-closure gate passed | PASS after closure gate run |
| Closure gate uses non-empty committed range | PASS: `186040d8..HEAD` |
| Changed-file set stays inside Allowed scope | PASS |
| `route.ts` line-count claim command-backed | PASS: 999 lines |
| Roadmap-to-work-order trace matrix final statuses resolved | PASS |
| Closure Diff Gate completed | PASS |
| Claim Integrity Scan completed | PASS |
| Fail conditions absent | PASS |
| Public export disposition recorded | PASS |
| Completion packet filed | PASS |
| Session front door, state registry, and handoff synced | PASS after closure sync |

## 13. Return-To-Orchestrator Conditions

Return to orchestrator without continuing if:

- source-fidelity pass finds a missing owner path;
- implementation requires editing `route.ts`;
- trace safety requires storing raw request/output material;
- release proof requires new secrets beyond existing release-gate environment;
- public/provenance boundary becomes unclear;
- risk exceeds R2.

## Operator Checkpoint

SATISFIED. The operator authorized CPG-3 continuation on 2026-05-31 with
"CPG-3 tiep tuc" after CPG-2 was closed and synced.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order. No public-sync artifact or public
catalog claim is authorized.

## Claim Boundary

This work order authorizes bounded optional receipt trace enrichment only. It
does not authorize raw capture, provider changes, Learning Plane mutation,
public-sync, hosted readiness, production readiness, or universal bypass
prevention claims.
