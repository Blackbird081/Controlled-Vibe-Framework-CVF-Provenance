# CVF GC-018 - LSC-T4 Promotion Threshold Policy

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-21

docType: baseline

dispatchBaseHead: cae048a3

Batch ID: LSC-T4

## Purpose

Authorize LSC-T4 as the next bounded Learning Signal Chain foundation tranche:
a documentation/reference policy that defines which captured learning signals
remain readout-only, which signals become governance proposals, and which
signals are eligible for rule, checker, or work-order promotion.

LSC-T4 must keep the LSC promise: fast capture, slow promotion. It must make
future helper/readout work faster by giving agents a deterministic threshold
map, while avoiding premature enforcement, runtime mutation, ledger store,
helper implementation, generator, checker, CLI/MCP adapter, provider/live proof,
public-sync, or universal governed-coding-control claims.

## Operator Authorization

The operator selected the next Learning Signal Chain roadmap order on
2026-06-21:

`LSC-T2 -> LSC-T4 -> LSC-T3 -> LSC-T6 -> LSC-T5/T7`.

The operator explicitly instructed: "nho ky va dung co hoi hay cho nua. tiep
di". This dispatch treats that as approval to proceed to LSC-T4 without another
operator checkpoint.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-21 roadmap order selecting LSC-T4 with LSC-T2 already closed at material commit `00214e9a` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| LSC-T0 roadmap | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | ACCEPT |
| LSC reference front door | `docs/reference/learning_signal_chain/README.md` | ACCEPT |
| LSC-T1 source-layout and de-dup contract | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | ACCEPT |
| LSC-T2 multi-role capture contract | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | ACCEPT |
| Learning Signal Intake Bridge | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | SOURCE_AUTHORITY_FOR_EXISTING_INTAKE_FIELDS |
| External knowledge absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | SOURCE_AUTHORITY_FOR_EXTERNAL_RETURN_ROUTING |

Provider-specific memory, chat memory, and private agent-local files are not
CVF source authority. External-agent outputs are input only until routed through
the external knowledge absorption chain and promoted by a governed CVF artifact.

## Scope / Owner Boundary

Allowed worker scope:

- update the Learning Signal Chain reference front door to list LSC-T4;
- create the LSC-T4 promotion threshold policy under
  `docs/reference/learning_signal_chain/`;
- create the LSC-T4 worker-return artifact;
- define readout-only, governance-proposal, rule-candidate,
  checker-candidate, work-order-candidate, and closure-blocker thresholds as
  documentation/reference policy;
- define how thresholds use existing LSC-T1 fields:
  `sourceProjection`, `rootCauseGroupId`, `captureState`, and `repeatRisk`;
- define how thresholds use existing Learning Signal Intake fields:
  `lane`, `defectClass`, `severity`, `disposition`, `nextControlAction`,
  `evidenceBasis`, and `autonomousMutationAuthorized`;
- preserve LSC-T2 role capture and no-signal guidance;
- keep LSC-T3 helper readout, LSC-T5 Learning Plane bridge, LSC-T6 external
  CLI/MCP contract, and LSC-T7 latency guard as future tranches.

Forbidden worker scope:

- no edits to `EXTENSIONS/**`, `governance/compat/**`, tests, scripts, MCP
  packages, web UI, session state, active handoff, root startup routers,
  public-sync, `.github/**`, or dependency manifests;
- no ledger source directory, generated aggregate, generator, drift checker,
  helper readout, runtime bridge, CLI/MCP adapter, provider/live proof,
  dependency install, queue, daemon, watcher, wrapper/proxy, direct
  IDE/shell/git/filesystem interception, arbitrary command execution, or
  EDIT/COMMIT execution;
- no public catalog update, public/production/release readiness, full-hook
  equivalence, cost optimization, speed claim, or universal
  governed-coding-control claim;
- no implementation of LSC-T3, LSC-T5, LSC-T6, LSC-T7, AAF-T6, AAF-T7, CGE-T3,
  ACE-R1, MLW7, or MLW8.

Risk ceiling: R1 documentation/reference policy only.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts changed or created:

- `docs/reference/learning_signal_chain/README.md`
- `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md`
- `docs/reviews/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY_WORKER_RETURN_2026-06-21.md`

No source, runtime, test, session, handoff, public-sync, or checker file is
authorized in worker execution.

## Decision / Baseline / Proposed Tranche

Baseline decision: LSC-T4 is ready for worker dispatch as a bounded reference
policy tranche.

Proposed tranche: `LSC-T4 Promotion Threshold Policy`.

Tranche owner split: dispatcher creates this GC-018 baseline and paired work
order; worker authors only the reference/front-door/return artifacts without
committing; reviewer/closer reviews and commits accepted material if gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| LSC-T0 names the governing principle "Fast capture, slow promotion" | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 33-39 | Fast capture, slow promotion | LSC-T0 roadmap | ACCEPT |
| LSC-T0 states promotion remains governed, reviewed, and non-blocking for routine capture | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 36-57 | promotion boundaries | LSC-T0 roadmap | ACCEPT |
| LSC-T0 defines promotion as fresh GC-018, work order, or checker only when justified | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 197-204 | Promotion | LSC-T0 latency budget | ACCEPT |
| LSC-T0 states lower-severity unresolved signals should appear in helper/readout output and not block routine closure | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 212-213 | lower-severity unresolved signals | LSC-T0 blocking rule | ACCEPT |
| LSC-T0 defines LSC-T4 as Promotion Threshold Policy with repeated-signal thresholds and blocking-vs-readout behavior | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | line 255 | `LSC-T4`; Promotion Threshold Policy | LSC-T0 work plan | ACCEPT |
| LSC-T0 requires future work orders to keep capture fast and promotion governed | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 301-316 | Acceptance Criteria For Future Work Orders | LSC-T0 roadmap | ACCEPT |
| LSC-T1 owns allowed LSC extension fields for projection, root-cause grouping, capture state, and repeat risk | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 72-86 | `sourceProjection`; `rootCauseGroupId`; `captureState`; `repeatRisk` | LSC-T1 contract | ACCEPT |
| LSC-T1 says `rootCauseGroupId` is ledger-minted and projection de-dup must not inflate counts | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 143-173 | `rootCauseGroupId`; Projection De-Dup Rule | LSC-T1 contract | ACCEPT |
| LSC-T1 leaves generator and drift checker implementation to future work | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 185-199 | generator; drift checker | LSC-T1 contract | ACCEPT |
| LSC-T2 defines role-specific capture eligibility and preserves no-signal guidance | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 77-112 | Capture Eligibility Matrix; No-Signal Assertion Guidance | LSC-T2 contract | ACCEPT |
| LSC-T2 maps role signals to existing LSC-T1 fields without adding runtime fields | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 141-149 | Mapping To LSC-T1 Fields | LSC-T2 contract | ACCEPT |
| LSC-T2 preserves closure blocking only for critical severity or observed repeated repeat risk | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 194-202 | Latency Budget; Closure | LSC-T2 contract | ACCEPT |
| Existing intake bridge owns severity, disposition, nextControlAction, evidenceBasis, and autonomous mutation false invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | lines 39-65, 163-170 | `LearningSignalIntakeInput`; `LearningSignalIntakeRecord`; `autonomousMutationAuthorized` | LPF intake bridge | ACCEPT |
| External-agent returned output must be classified through the external knowledge absorption chain before governed action | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | lines 44-66, 73-75, 90-91 | External-agent returned output | external knowledge absorption chain map | ACCEPT |

## New Doc-Only Terms

| Proposed term | Owner in LSC-T4 | Runtime status | Reason |
|---|---|---|---|
| `READOUT_ONLY` | LSC-T4 reference policy | DOC_ONLY_NEW | signal remains visible to helper/readout but does not trigger governance action |
| `WATCH_FOR_REPEAT` | LSC-T4 reference policy | DOC_ONLY_NEW | signal is weak alone but should be grouped by `rootCauseGroupId` if observed again |
| `GOVERNANCE_PROPOSAL_CANDIDATE` | LSC-T4 reference policy | DOC_ONLY_NEW | signal may become a written proposal or finding after review |
| `RULE_CANDIDATE` | LSC-T4 reference policy | DOC_ONLY_NEW | repeated or high-impact prose-rule gap may justify a rule update |
| `CHECKER_CANDIDATE` | LSC-T4 reference policy | DOC_ONLY_NEW | repeated or closure-costly machine-verifiable gap may justify checker work |
| `WORK_ORDER_CANDIDATE` | LSC-T4 reference policy | DOC_ONLY_NEW | bounded implementation or documentation work may be dispatched through GC-018 |
| `CLOSURE_BLOCKER` | LSC-T4 reference policy | DOC_ONLY_NEW | closure should pause only under critical or observed-repeated conditions already allowed by LSC-T0/T2 |

These terms are documentation/reference vocabulary only. They must not be
presented as existing runtime fields, checker fields, or active ledger schema.

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `cae048a3`.
- `git status --short` was clean before LSC-T4 dispatch authoring.
- Source verification used direct file reads and `rg -n` lookups against
  current repository files.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base cae048a3 --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base cae048a3 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base cae048a3 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base cae048a3 --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed baseline/work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | LSC-T4 promotion threshold policy |
| Disposition | ADAPT as CVF-owned Learning Signal Chain promotion-threshold policy |
| Claim boundary | external-agent returns remain input only until classified and promoted through governed CVF artifacts |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T4 promotion threshold policy dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation/reference policy authoring only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | promotion threshold, readout-vs-promotion, and closure-blocking policy only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Captured signals need deterministic promotion thresholds before helper/readout work | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T4 must define readout-only, watch, proposal, rule/checker/work-order, and blocker thresholds | handled by this dispatch |
| Promotion can create latency if every signal becomes a governance action | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | LSC-T4 must keep lower-severity signals in readout unless thresholds are met | handled by this dispatch |
| Critical or observed-repeated signals need explicit closure-blocking policy | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | RULE_CANDIDATE | LSC-T4 must bind blocker thresholds to LSC-T0/T2 rules | handled by this dispatch |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed by this dispatch | handled |

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`.
- Predecessor intake artifact: `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md`.
- Predecessor capture artifact: `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because LSC-T4 moves promotion thresholds from the roadmap row into dispatch-ready policy work.
- Routing matrix status: `DO_NOW` for LSC-T4 documentation/reference policy; `SEPARATE_RUNTIME_TRANCHE` for any checker/helper/generator/CLI/MCP/runtime implementation; `STRATEGIC_OPERATOR_DECISION` for LSC-T3/T5/T6/T7 as future operator-selected tranches; `OUT_OF_SCOPE` for provider/live/public-sync/direct-interception/readiness claims.
- Semantic sampling status: sampled LSC-T0 LSC-T4 row, LSC-T0 latency budget, LSC-T1 de-dup fields, LSC-T2 latency budget, and LPF intake fields.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | LSC remains capture-fast, promotion-slow, and proposal-only. |
| CHANGED_DISPOSITION | LSC-T4 promotion thresholds moved from roadmap row into dispatch requirements. |
| NEW_FINDING | Promotion policy must distinguish readout-only signals from rule/checker/work-order candidates before a fast helper is useful. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception scope remains rejected for LSC-T4. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | LSC-T4 documentation/reference promotion threshold policy. |
| SEPARATE_RUNTIME_TRANCHE | checker, helper readout, generator, drift checker, CLI/MCP adapter, runtime bridge. |
| STRATEGIC_OPERATOR_DECISION | LSC-T3, LSC-T5, LSC-T6, LSC-T7 remain future operator-selected tranches; current dispatch does not authorize them. |
| OUT_OF_SCOPE | provider/live, public-sync, direct interception, readiness, universal control. |
| RESOLVED_BY_DESIGN | extend LSC-T1/T2 field and capture contracts instead of creating a parallel signal core. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LSC-T4-S1 | LSC-T0 latency budget | capture is fast; promotion is slower and governed | mapped into Required Deliverables | prevents automatic promotion of routine notes | PASS |
| LSC-T4-S2 | LSC-T0 work plan | LSC-T4 defines repeated thresholds and blocking-vs-readout behavior | mapped into Required Deliverables | prevents helper readout before promotion semantics exist | PASS |
| LSC-T4-S3 | LSC-T1 de-dup fields | repeat risk and root-cause grouping belong to LSC field layer | reused by T4 policy | avoids duplicate count inflation | PASS |
| LSC-T4-S4 | LSC-T2 closure rule | closure blocking remains critical or observed repeated only | reused by T4 blocker policy | avoids new low-severity blockers | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch for Learning Signal Chain policy work. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Claim Boundary

This baseline authorizes only LSC-T4 documentation/reference policy work for
promotion thresholds and blocking-vs-readout behavior. It does not implement a
ledger store, generator, drift checker, helper readout, runtime Learning Plane
mutation, provider/live proof, CLI/MCP adapter behavior, public-sync, direct
interception, wrapper/proxy enforcement, queue/daemon, watcher, readiness, cost
optimization, full-hook equivalence, or universal governed-coding control.
