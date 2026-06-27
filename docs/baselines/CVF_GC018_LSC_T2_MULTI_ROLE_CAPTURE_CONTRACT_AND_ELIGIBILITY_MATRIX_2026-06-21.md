# CVF GC-018 - LSC-T2 Multi-Role Capture Contract And Eligibility Matrix

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-21

docType: baseline

dispatchBaseHead: b2a90d52

Batch ID: LSC-T2

## Purpose

Authorize LSC-T2 as the next bounded Learning Signal Chain foundation tranche:
a documentation/reference contract that extends capture beyond worker-return
friction to reviewer, reviewer/closer, dispatch author, session-sync steward,
operator, and external-agent returned-output signals.

LSC-T2 must define role-specific capture eligibility so CVF learns from real
friction without turning every return into a long retrospective. It must keep
capture cheap, preserve the LSC-T1 source-layout/de-dup boundary, and avoid
runtime, checker, helper, CLI/MCP, provider, public-sync, or live-proof
implementation.

## Operator Authorization

The operator approved the lane-selection audit recommendation to proceed with
the next Learning Signal Chain tranche after LSC-T1 closure. The approved lane
is LSC-T2 Multi-Role Capture Contract And Eligibility Matrix.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-21 approval: "Ok, ra work order theo roadmap" after lane audit selected LSC-T2 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| LSC-T0 roadmap | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | ACCEPT |
| LSC-T1 closed reference front door | `docs/reference/learning_signal_chain/README.md` | ACCEPT |
| LSC-T1 source-layout and de-dup contract | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | ACCEPT |
| Learning Signal Intake Bridge | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | SOURCE_AUTHORITY_FOR_EXISTING_INTAKE_FIELDS |
| AAF-T5 checker | `governance/compat/check_worker_experience_retrospective.py` | SOURCE_AUTHORITY_FOR_EXISTING_WORKER_TOKEN |
| Worker-experience standard | `docs/reference/worker_experience_retrospective/README.md` | SOURCE_AUTHORITY_FOR_EXISTING_WORKER_TOKEN |
| External knowledge absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | SOURCE_AUTHORITY_FOR_EXTERNAL_RETURN_ROUTING |

Provider-specific memory, chat memory, and private agent-local files are not
CVF source authority. External-agent outputs are input only until routed through
the external knowledge absorption chain and promoted by a governed CVF artifact.

## Scope / Owner Boundary

Allowed worker scope:

- create the LSC-T2 multi-role capture contract under
  `docs/reference/learning_signal_chain/`;
- update the Learning Signal Chain reference front door to point to LSC-T2;
- create the LSC-T2 worker-return artifact;
- define role-neutral actor categories and role-specific capture eligibility;
- define no-signal assertion guidance that prevents routine work from becoming
  mandatory retrospective prose;
- define how captured role signals map to the LSC-T1 fields
  `sourceProjection`, `rootCauseGroupId`, `captureState`, and `repeatRisk`
  without creating a new runtime schema;
- define external-agent returned-output eligibility at contract level only and
  bind it to the external knowledge absorption chain map;
- keep AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, and MLW8 parked unless separately
  authorized.

Forbidden worker scope:

- no edits to `EXTENSIONS/**`, `governance/compat/**`, tests, scripts, MCP
  packages, web UI, session state, active handoff, root startup routers,
  public-sync, `.github/**`, or dependency manifests;
- no ledger source directory, generated aggregate, generator, drift checker,
  helper readout, runtime bridge, CLI/MCP adapter, provider/live proof,
  dependency install, queue, daemon, watcher, wrapper/proxy, direct IDE/shell/
  git/filesystem interception, arbitrary command execution, or EDIT/COMMIT
  execution;
- no public catalog update, public/production/release readiness, full-hook
  equivalence, cost optimization, speed claim, or universal governed-coding
  control claim;
- no implementation of AAF-T6 read-receipt enforcement, AAF-T7 helper/index
  hardening, CGE-T3 absorption ledger, ACE-R1 evidence replay, MLW7, or MLW8.

Risk ceiling: R1 documentation/reference contract only.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts changed or created:

- `docs/reference/learning_signal_chain/README.md`
- `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md`
- `docs/reviews/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_WORKER_RETURN_2026-06-21.md`

No source, runtime, test, session, handoff, public-sync, or checker file is
authorized in worker execution.

## Decision / Baseline / Proposed Tranche

Baseline decision: LSC-T2 is ready for worker dispatch as a bounded reference
contract tranche.

Proposed tranche: `LSC-T2 Multi-Role Capture Contract And Eligibility Matrix`.

Tranche owner split: dispatcher creates this GC-018 baseline and paired work
order; worker authors only the reference/front-door/return artifacts without
committing; reviewer/closer reviews and commits accepted material if gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| LSC-T0 includes reviewer/orchestrator/operator friction and external-agent critique in the Learning Signal Chain purpose | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 14, 53-56 | reviewer/orchestrator/operator friction; external-agent CLI/MCP readiness | LSC-T0 roadmap | ACCEPT |
| LSC-T0 defines unified signal classes for reviewer, orchestrator, operator, and external-agent signals | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 131-138 | `REVIEWER_FRICTION`; `ORCHESTRATOR_FRICTION`; `OPERATOR_CORRECTION`; `EXTERNAL_AGENT_CRITIQUE` | LSC-T0 roadmap | ACCEPT |
| LSC-T0 defines `actorRole` as role-neutral and includes reviewer, orchestrator, operator, external-agent, runtime, provider, and public-surface actors | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | line 173 | `actorRole` | LSC-T0 roadmap minimal signal event contract | ACCEPT |
| LSC-T0 explicitly identifies LSC-T2 as Multi-Role Capture Contract with separate eligibility per role to avoid false positives | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | line 253 | `LSC-T2`; Multi-Role Capture Contract | LSC-T0 work plan | ACCEPT |
| LSC-T0 requires capture-fast and promotion-slow latency behavior | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 197-213 | Latency Budget; blocking rule | LSC-T0 roadmap | ACCEPT |
| LSC-T0 requires future work orders to preserve parked lanes and support external CLI/MCP agents without chat memory | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 301-317 | Acceptance Criteria For Future Work Orders | LSC-T0 roadmap | ACCEPT |
| LSC-T1 owns allowed LSC extension fields for source projection, root cause grouping, capture state, and repeat risk | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 72-86 | `sourceProjection`; `rootCauseGroupId`; `captureState`; `repeatRisk` | LSC-T1 contract | ACCEPT |
| LSC-T1 defines `disposition` as governed source of truth and `captureState` as derived/advisory | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 117-139 | `disposition`; `captureState` | LSC-T1 contract | ACCEPT |
| LSC-T1 defines CLI/MCP minimal payload boundary including `signalClass` and `actorRole` but no adapter implementation | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 202-210 | CLI/MCP minimal payload | LSC-T1 contract | ACCEPT |
| LSC-T1 keeps AAF-T6/T7, CGE-T3, ACE-R1, and MLW7/8 parked | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 212-221 | Parking Ledger | LSC-T1 contract | ACCEPT |
| LSC reference front door exists and currently lists LSC-T1 as active contract | `docs/reference/learning_signal_chain/README.md` | lines 1, 40-45 | Current Contracts | LSC reference front door | ACCEPT |
| Existing intake bridge owns lane, defect class, severity, disposition, input, record, and the autonomous mutation false invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | lines 11-65, 123-170 | `LearningSignalIntakeInput`; `LearningSignalIntakeRecord`; `autonomousMutationAuthorized` | LPF intake bridge | ACCEPT |
| AAF-T5 checker owns existing worker-experience token names and friction levels only for eligible worker-return artifacts | `governance/compat/check_worker_experience_retrospective.py` | lines 5-10, 34-56, 165-192 | `WORKER_EXPERIENCE_RETRO`; `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON`; `FRICTION_LEVELS` | worker-experience checker | ACCEPT |
| Worker-experience standard owns existing worker token syntax and exact no-friction assertion | `docs/reference/worker_experience_retrospective/README.md` | lines 23-25, 54-68 | token block; exact NA assertion | worker-experience standard | ACCEPT |
| External-agent returned output must be classified through the external knowledge absorption chain before governed action | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | lines 25, 55-66, 73-75, 90 | External-agent returned output | external knowledge absorption chain map | ACCEPT |

## New Doc-Only Fields

| Proposed field or term | Owner in LSC-T2 | Runtime status | Reason |
|---|---|---|---|
| `captureEligibility` | LSC-T2 reference contract | DOC_ONLY_NEW | names role-specific conditions for when a signal should be captured |
| `noSignalAssertion` | LSC-T2 reference contract | DOC_ONLY_NEW | prevents routine work from becoming retrospective latency |
| `roleSignalSurface` | LSC-T2 reference contract | DOC_ONLY_NEW | describes the role-owned artifact surface where a signal may be declared |
| `externalReturnEligibility` | LSC-T2 reference contract | DOC_ONLY_NEW | binds external-agent returned outputs to chain-map classification before CVF promotion |

These fields are documentation/reference vocabulary only. They must not be
presented as existing runtime fields, checker fields, or active ledger schema.

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `b2a90d52`.
- `git status --short` was clean before LSC-T2 dispatch authoring.
- Source verification used direct file reads and `rg -n` lookups against
  current repository files.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base b2a90d52 --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base b2a90d52 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base b2a90d52 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base b2a90d52 --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed baseline/work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | LSC-T2 multi-role capture contract and eligibility matrix |
| Disposition | ADAPT as CVF-owned Learning Signal Chain role-capture contract |
| Claim boundary | external-agent returns remain input only until classified and promoted through governed CVF artifacts |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T2 multi-role capture contract dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation/reference contract authoring only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | multi-role capture eligibility, no-signal assertion, and external-return routing contract only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Worker-only capture leaves reviewer/orchestrator/operator friction chat-only | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | LSC-T2 must define role-specific capture eligibility and no-signal rules | handled by this dispatch |
| Multi-role capture can create latency if every role must write long retrospectives | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T2 must keep capture cheap and define no-signal assertions | handled by this dispatch |
| External-agent returned output needs classification before becoming CVF authority | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T2 must bind external returns to the chain map | handled by this dispatch |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed by this dispatch | handled |

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`.
- Predecessor intake artifact: `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because LSC-T2 moves multi-role
  capture from deferred roadmap item to dispatch-ready contract work.
- Routing matrix status: `DO_NOW` for LSC-T2 documentation/reference contract;
  `SEPARATE_RUNTIME_TRANCHE` for any checker/helper/generator/CLI/MCP/runtime
  implementation; `STRATEGIC_OPERATOR_DECISION` for AAF-T6/T7, CGE-T3, ACE-R1,
  MLW7/8; `OUT_OF_SCOPE` for provider/live/public-sync/direct-interception/
  readiness claims.
- Semantic sampling status: sampled LSC-T0 LSC-T2 row, LSC-T1 extension fields,
  AAF-T5 token source, and external returned-output routing.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | LSC remains capture-fast, promotion-slow, and proposal-only. |
| CHANGED_DISPOSITION | LSC-T2 multi-role capture moved from roadmap row into dispatch requirements. |
| NEW_FINDING | Multi-role capture requires no-signal assertions to avoid creating new latency. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception scope remains rejected for LSC-T2. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | LSC-T2 documentation/reference multi-role capture contract. |
| SEPARATE_RUNTIME_TRANCHE | checker, helper readout, generator, drift checker, CLI/MCP adapter, runtime bridge. |
| STRATEGIC_OPERATOR_DECISION | AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, MLW8 ordering after LSC-T2. |
| OUT_OF_SCOPE | provider/live, public-sync, direct interception, readiness, universal control. |
| RESOLVED_BY_DESIGN | extend LSC-T1 field/de-dup contract instead of creating a parallel signal core. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LSC-T2-S1 | LSC-T0 work plan | LSC-T2 extends capture beyond workers | mapped into Required Deliverables | prevents worker-only learning blind spot | PASS |
| LSC-T2-S2 | LSC-T1 extension fields | LSC owns `sourceProjection`, `rootCauseGroupId`, `captureState`, `repeatRisk` | reused by T2 contract | avoids new runtime schema | PASS |
| LSC-T2-S3 | External chain map | external-agent returned output needs classification | routed through External Knowledge Intake | prevents external output becoming authority by shortcut | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch for Learning Signal Chain contract work. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Claim Boundary

This baseline authorizes only LSC-T2 documentation/reference contract work for
multi-role capture eligibility. It does not implement a ledger store, generator,
drift checker, helper readout, runtime Learning Plane mutation, provider/live
proof, CLI/MCP adapter behavior, public-sync, direct interception, wrapper/proxy
enforcement, queue/daemon, watcher, readiness, cost optimization,
full-hook equivalence, or universal governed-coding control.
