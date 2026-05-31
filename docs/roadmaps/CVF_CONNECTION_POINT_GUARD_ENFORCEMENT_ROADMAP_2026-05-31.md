# CVF Connection Point Guard Enforcement Roadmap

Memory class: SUMMARY_RECORD

Status: CPG1_CPG2_CPG3_CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-05-31

---

## Purpose

Define the next bounded runtime roadmap after LHW21. LHW21 published the
inbound connection-point doctrine and three documentation-only advisory
connectors. This roadmap proposes a guarded runtime path:

```text
Framework -> CVF Connection Point -> Governance Engine
```

The first runtime priorities, CPG-1 event-contract extraction and CPG-2 bounded
hard-gate mode, and CPG-3 receipt enrichment are closed with bounded proof.

## Scope / Target / Owner Boundary

Target: a three-tranche runtime roadmap for inbound CVF connection points.

Owner surfaces:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/` for INT1 connection-point policy
  and MCP guard behavior.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` and
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
  for a later bounded receipt trace extension.

Boundary:

- CVF accepts inbound framework events at a CVF-owned connection point.
- CVF does not build outbound framework-specific adapters.
- No further runtime implementation is authorized without a fresh tranche
  GC-018, source-fidelity pass, work order, and autorun gates.
- No public-sync change, provider prompt change, model tuning, autonomous
  mutation, hosted-readiness claim, production-readiness claim, or universal
  bypass-prevention claim is authorized.

## Authorization / Decision

Decision: `CPG1_CPG2_CPG3_CLOSED_PASS_BOUNDED`.

Operator direction on 2026-05-31 authorized CPG-1 implementation after a fresh
runtime GC-018, source-fidelity pass, work order, and autorun gates. CPG-1 is
now `CLOSED_PASS_BOUNDED`. CPG-2 is also `CLOSED_PASS_BOUNDED` with bounded
INT1 enforce-mode proof. CPG-3 is `CLOSED_PASS_BOUNDED` with bounded web
receipt trace proof.

Parked operator checkpoint:

`SATISFIED_FOR_CPG1_CPG2_CPG3`: operator instructed Codex to proceed with
roadmap code on 2026-05-31, later to finish CPG-2, and then "CPG-3 tiep tuc".
No waiver is granted for public sync or claim expansion.

## Predecessor Evidence

- LHW21 GC-018:
  `docs/baselines/CVF_GC018_LHW21_INTEGRATION_CONNECTION_POINT_ADVISORY_WAVE_2026-05-31.md`
- LHW21 T1:
  `docs/reference/CVF_LHW21_T1_EVENT_TAXONOMY_SCHEMA_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`
- LHW21 T2:
  `docs/reference/CVF_LHW21_T2_HARD_GATE_MODE_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`
- LHW21 T3:
  `docs/reference/CVF_LHW21_T3_RECEIPT_ENRICHMENT_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Canonical IS1 event values exist | `VALUE_SET` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` | lines 16-21 | `AgentEventType` | IS1 generic agent adapter | ACCEPT: `INTENT`, `PLAN`, `TOOL_CALL`, `EXECUTION`, `RESULT` |
| Canonical IS1 control-point values exist | `VALUE_SET` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` | line 25 | `ControlPoint` | IS1 generic agent adapter | ACCEPT: `CP1_INTENT`, `CP2_PLAN`, `CP3_TOOL`, `CP4_RUNTIME`, `CP5_RESULT` |
| IS1 mapping function exists | `EXISTS` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` | line 101 | `mapAgentEventToCvf` | IS1 generic agent adapter | ACCEPT |
| IS1 adapter literal false invariant exists | `LITERAL_INVARIANT` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/generic-agent-adapter.ts` | lines 57 and 116 | `runtimeAdapterAuthorized` | `AdapterMappingResult` | ACCEPT: literal `false` |
| INT1 transport event set exists | `VALUE_SET` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | lines 3-9 | `INT1_ALLOWED_EVENT_TYPES` | INT1 policy module | ACCEPT: `intent.received`, `plan.created`, `tool.requested`, `execution.state`, `result.produced` |
| INT1 plan validator is currently advisory | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | lines 31-58 | `validateInt1Plan` | INT1 policy module | ACCEPT: source says it does not block execution |
| INT1 plan decision values exist | `VALUE_SET` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | lines 41-46 | `advisoryDecision` | `validateInt1Plan` | ACCEPT: `ALLOW_ADVISORY`, `REVIEW_RECOMMENDED`, `REJECT_ADVISORY` |
| INT1 event emitter exists | `EXISTS` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | lines 60-81 | `emitInt1AgentEvent` | INT1 policy module | ACCEPT |
| INT1 MCP registrations delegate to the policy module | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | lines 771-805 | `cvf_validate_plan`, `cvf_emit_agent_event` | INT1 MCP tools | ACCEPT |
| Receipt interface exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | lines 82-105 | `GovernanceEvidenceReceipt` | web AI types | ACCEPT |
| Receipt builder exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 65-132 | `buildEvidenceReceipt` | web governance envelope | ACCEPT |
| Execute route is near hard threshold | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | command-backed physical line count | `route.ts` | web execute route | ACCEPT: `999` lines |
| MCP index exceeds soft threshold | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | command-backed physical line count | `index.ts` | MCP server | ACCEPT: `873` lines after CPG-1 extraction |

## New Proposed Fields And Symbols

CPG-1, CPG-2, and CPG-3 names are implemented where noted:

| Proposed item | Intended tranche | Purpose | Runtime status now |
| --- | --- | --- | --- |
| `connectionPointMode` | CPG-2 | Bounded mode vocabulary: `advisory` or `enforce` | IMPLEMENTED |
| `ConnectionPointGuardDecision` | CPG-1 | Structured event-contract validation result | IMPLEMENTED |
| `governanceTrace` | CPG-3 | Bounded policy-evaluation summaries for receipt replay | IMPLEMENTED |
| `GovernanceTraceEntry` | CPG-3 | Trace-entry schema excluding raw prompts and secrets | IMPLEMENTED |

## Tranche Plan

### CPG-1 Inbound Event Contract Guard

Contract candidate:
`cvf.connectionPointEventContractGuard.cpg1.v1`

Risk: R2.

Goal: extract INT1 connection-point policy into a same-domain MCP module and
make event-contract validation independently testable.

Required planning constraints:

- Extract INT1 policy logic from `src/index.ts`; do not grow the 917-line MCP
  registration file.
- Reuse the current dotted INT1 event values and keep the IS1 canonical bridge
  explicit.
- Preserve current advisory behavior unless the fresh GC-018 authorizes a
  narrower change.
- Prove supported-event acceptance and unsupported-event rejection.

Claim limit: this tranche proves validation at the CVF-owned inbound
connection point only. It does not prove that every external framework route
is forced through CVF.

### CPG-2 CP2 Hard Gate Enforcement

Contract candidate:
`cvf.connectionPointHardGateEnforcement.cpg2.v1`

Risk: R2-R3.

Prerequisite: CPG-1 `CLOSED_PASS_BOUNDED`.

Goal: implement a bounded `connectionPointMode` rollout for CP2 plan
validation. This tranche is closed with default advisory compatibility and
optional enforce progression decisions.

Required planning constraints:

- Default rollout posture must remain explicit and reversible.
- `advisory` preserves current behavior.
- `enforce` must refuse progression for a blocking plan outcome at the owned
  connection point.
- The packet must define how `ALLOW_ADVISORY`, `REVIEW_RECOMMENDED`, and
  `REJECT_ADVISORY` map into bounded enforce-mode behavior.
- Tests must cover allow, review, reject, unsupported event, and default-mode
  compatibility.

Claim limit: enforcement applies only to traffic entering the owned
connection point. Universal framework bypass prevention requires a separate
integration proof.

### CPG-3 Governance Trace Receipt Enrichment

Contract candidate:
`cvf.governanceTraceReceiptEnrichment.cpg3.v1`

Risk: R2.

Prerequisite: CPG-2 `CLOSED_PASS_BOUNDED`.

Goal: add a bounded optional `governanceTrace` receipt extension for forensic
review after the guard behavior is proven.

Required planning constraints:

- Update the current `GovernanceEvidenceReceipt` owner type and
  `buildEvidenceReceipt()` owner builder together.
- Trace entries must be bounded policy summaries.
- Trace entries must exclude raw prompts, provider keys, secrets, and
  framework-private memory.
- Add schema, builder, route-consumer, and regression tests.
- Do not grow `route.ts`; use existing receipt-builder ownership.

Claim limit: trace enrichment supports evidence replay. It does not authorize
raw-memory capture, autonomous learning mutation, or public export.

## Maintainability Plan

| Surface | Current size | Constraint | Required action before implementation |
| --- | --- | --- | --- |
| MCP `src/index.ts` | 873 lines after CPG-1 extraction | Above 700-line soft threshold | CPG-1 extracted a same-domain policy module and reduced the file from 917 lines; later edits must avoid regrowth |
| Web `/api/execute/route.ts` | 999 lines | Near 1000-line hard threshold | CPG-3 must not add inline route logic; extend receipt ownership through `web-governance-envelope.ts` |

`python governance/compat/check_governed_file_size.py --enforce` must pass for
every implementation tranche.

## Required GC-018 Content Before Dispatch

The fresh runtime GC-018 must:

- verify every existing path, field, enum value, and symbol against current
  source;
- list proposed files separately from existing source facts;
- define CPG-1 write ownership before any edit;
- classify risk as R2-R3 and name the operator checkpoint;
- include a live governance proof plan;
- preserve the public/provenance boundary;
- include rollback and default-mode compatibility criteria;
- define the exact stop condition if enforcement semantics remain ambiguous.

## Required Autorun And Proof Gates

Before dispatch:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
```

Before material implementation:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

Before closure:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD
python scripts/run_cvf_release_gate_bundle.py --json
```

Direct MCP unit tests are necessary but insufficient for a release-quality
governance behavior claim. Live governance proof must use a real provider API
call through the governed CVF route.

## Non-Goals

- No further runtime code edit in this parent-roadmap closure batch.
- No outbound LangChain, CrewAI, AutoGen, or provider-specific adapter.
- No universal claim that every external framework path is already forced
  through CVF.
- No raw prompt, secret, provider-key, or private-memory trace capture.
- No public-sync export, hosted-readiness claim, or production-readiness claim.

## Work Plan

| Tranche | Contract candidate | Prerequisite | Risk | Current status |
| --- | --- | --- | --- | --- |
| CPG-1 | `cvf.connectionPointEventContractGuard.cpg1.v1` | Fresh GC-018 + operator checkpoint | R2 | CLOSED_PASS_BOUNDED |
| CPG-2 | `cvf.connectionPointHardGateEnforcement.cpg2.v1` | CPG-1 `CLOSED_PASS_BOUNDED` + fresh GC-018 | R2-R3 | CLOSED_PASS_BOUNDED |
| CPG-3 | `cvf.governanceTraceReceiptEnrichment.cpg3.v1` | CPG-2 `CLOSED_PASS_BOUNDED` + fresh GC-018 | R2 | CLOSED_PASS_BOUNDED |

CPG-2 closure packet:

- `docs/roadmaps/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_ROADMAP_2026-05-31.md`
- `docs/work_orders/CVF_WO_CPG2_CP2_HARD_GATE_ENFORCEMENT_2026-05-31.md`
- `docs/reviews/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_COMPLETION_2026-05-31.md`

CPG-3 closure packet:

- `docs/baselines/CVF_GC018_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`
- `docs/roadmaps/CVF_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_ROADMAP_2026-05-31.md`
- `docs/work_orders/CVF_WO_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`
- `docs/reviews/CVF_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_COMPLETION_2026-05-31.md`

## Verification / Evidence

Roadmap-creation evidence:

| Evidence | Command or source | Result |
| --- | --- | --- |
| LHW21 closure | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base c460a8ef --head HEAD` before roadmap batch | PASS |
| MCP index physical size | PowerShell `Get-Content` line count | `917` lines |
| Execute route physical size | PowerShell `Get-Content` line count | `999` lines |
| Current source anchors | Source Verification Block above | ACCEPT |
| Runtime edit in roadmap batch | `git diff --name-status` | N/A with reason: roadmap documentation only |
| CPG-1 implementation | `1ff0354c`; `docs/reviews/CVF_CPG1_INBOUND_EVENT_CONTRACT_GUARD_COMPLETION_2026-05-31.md` | CLOSED_PASS_BOUNDED; MCP suite `554/554`, release bundle `7/7` |
| CPG-2 implementation | `docs/reviews/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_COMPLETION_2026-05-31.md` | CLOSED_PASS_BOUNDED; focused INT1 `12/12`, MCP build PASS, release bundle PASS `7/7` |
| CPG-3 implementation | `55dc22c9`; `docs/reviews/CVF_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_COMPLETION_2026-05-31.md` | CLOSED_PASS_BOUNDED; focused web tests `19/19`, typecheck/build PASS, release bundle PASS `7/7` |

## Acceptance Criteria For Roadmap Readiness

This roadmap may move from proposed to implementation-ready only when:

- LHW21 remains `CLOSED_PASS_BOUNDED`;
- a fresh runtime GC-018 exists and passes source-fidelity review;
- operator checkpoint is explicitly satisfied;
- CPG-1 work order exists with owned paths and forbidden scope;
- maintainability extraction is included in CPG-1 scope;
- live-proof plan names the governed route and secret-safe diagnostics;
- autorun `pre-dispatch` gate passes on a real changed range.

## Fail Conditions

Return to orchestrator if:

- proposed names are presented as current runtime fields;
- an outbound framework adapter is added;
- `index.ts` grows without same-domain extraction;
- `route.ts` grows beyond its hard threshold;
- `governanceTrace` captures raw prompt, secret, provider key, or
  framework-private memory;
- a runtime enforcement claim is made from direct MCP tests alone;
- public-sync or live-provider work starts without the required packet and
  operator checkpoint.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Advisory-only INT1 boundary did not refuse blocked progression | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `RESOLVED_BY_CPG2` | CPG-2 defines bounded enforce semantics |
| Event validation logic sits in an MCP index file above soft threshold | `MAINTAINABILITY_GAP` | `GOVERNANCE_CONTROL_PLANE` | `PHASE_GATE_PLACEMENT_GAP` | CPG-1 must extract a same-domain policy module before adding logic |
| Receipt trace proposal was not a runtime field | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `RESOLVED_BY_CPG3` | CPG-3 adds bounded summary-only receipt trace via the owner builder |
| Runtime/provider/cost findings | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `N/A_WITH_REASON` | Roadmap creation performs no runtime execution, provider call, or cost analysis |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap is private provenance planning. No public-sync artifact
or catalog claim is authorized.

Next action: assess public-safe export only after a separate public-sync work
order; private CPG-2 closure is not a public catalog claim.

## Claim Boundary

This roadmap records bounded CPG-1, CPG-2, and CPG-3 closure. It does not
deliver framework adapters, prove universal bypass prevention, export public
artifacts, or claim hosted or production readiness.
