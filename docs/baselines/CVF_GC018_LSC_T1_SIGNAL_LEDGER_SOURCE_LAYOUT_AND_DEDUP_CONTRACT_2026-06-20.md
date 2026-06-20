# CVF GC-018 - LSC-T1 Signal Ledger Source Layout And De-Dup Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-20

docType: baseline

dispatchBaseHead: 90b06fa0

Batch ID: LSC-T1

## Purpose

Authorize LSC-T1 as a bounded Learning Signal Chain foundation tranche for a
source-verified signal-ledger source layout and de-dup contract.

LSC-T1 responds to the accepted LSC-T0 roadmap and two rounds of adversarial
review. The central design correction is that CVF must not create a second
learning-signal core beside the existing Learning Plane intake bridge. LSC-T1
must define how worker-experience tokens, finding-to-governance rows, and future
MLW/RT projections map into or extend `LearningSignalIntakeRecord` without
double-counting one root cause.

## Operator Authorization

The operator accepted the Learning Signal Chain roadmap direction and reported
the second-round advisory review as `APPROVE_NO_BLOCKING_FINDINGS`, with the
instruction to open LSC-T1 and fold N4/N5 into the work order.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 approval to continue from LSC-T0 into LSC-T1 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| LSC-T0 roadmap | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | ACCEPT |
| Codex classification | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CODEX_CLASSIFICATION_2026-06-20.md` | ACCEPT |
| Round-1 advisory rebuttal | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_2026-06-20.md` | ADVISORY_INPUT_CLASSIFIED |
| Round-2 advisory rebuttal | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md` | ADVISORY_INPUT_ACCEPTED |
| Learning Signal Intake Bridge | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | SOURCE_AUTHORITY |
| AAF-T5 checker | `governance/compat/check_worker_experience_retrospective.py` | SOURCE_AUTHORITY_FOR_AAF_TOKEN_ENUMS |
| Worker-experience standard | `docs/reference/worker_experience_retrospective/README.md` | SOURCE_AUTHORITY_FOR_AAF_TOKEN_SHAPE |
| JSON generated aggregate discipline | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | ACCEPT |
| External knowledge absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |

Provider-specific memory and private chat history are not CVF source authority.
External-agent rebuttals are advisory inputs only after Codex classification and
this dispatch baseline absorb their accepted findings.

## Scope / Owner Boundary

Allowed worker scope:

- create a Learning Signal Chain reference front door;
- create the LSC-T1 signal-ledger source-layout and de-dup contract;
- create a JSON signal-ledger entry template that maps to existing
  `LearningSignalIntakeInput` / `LearningSignalIntakeRecord` fields and LSC
  extension fields;
- define deterministic `rootCauseGroupId` derivation and projection de-dup;
- define exact AAF-T5 `frictionLevel` to intake `severity` or no-entry mapping;
- define `disposition` as the governed source of truth and `captureState` as a
  derived/advisory view, or define a strict allowed-pairs table with conflict
  rule;
- define the generated Markdown-readable index rule without building the
  generator or checker;
- create the LSC-T1 worker-return artifact.

Forbidden worker scope:

- no edits to `EXTENSIONS/**`, runtime source, tests, MCP packages, web UI,
  provider routing, public-sync, session state, active handoff, root startup
  routers, or closed predecessor artifacts;
- no implementation of an actual signal ledger generator, drift checker,
  helper readout, CLI/MCP adapter, runtime bridge, provider/live proof, queue,
  daemon, watcher, wrapper/proxy, direct IDE/shell/git/filesystem interception,
  arbitrary command execution, EDIT/COMMIT execution, public catalog update, or
  production/public/release readiness claim;
- no reopening of AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, or MLW8.

Risk ceiling: R1 documentation/reference and schema-template contract only.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts changed or created:

- `docs/reference/learning_signal_chain/README.md`
- `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md`
- `docs/reference/learning_signal_chain/CVF_LEARNING_SIGNAL_LEDGER_ENTRY_TEMPLATE.json`
- `docs/reviews/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_WORKER_RETURN_2026-06-20.md`

No source, runtime, test, session, or public-sync file is authorized in worker
execution.

## Decision / Baseline / Proposed Tranche

Baseline decision: LSC-T1 is ready for worker dispatch as a bounded contract
tranche.

Proposed tranche: `LSC-T1 Signal Ledger Source Layout And De-Dup Contract`.

Tranche owner split: dispatcher creates this GC-018 baseline and paired work
order; worker authors only the reference/template/return artifacts without
committing; reviewer/closer reviews and commits accepted material if gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| LSC-T0 defines LSC-T1 as signal-ledger source layout and de-dup contract | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 252, 312-315 | `LSC-T1`; `rootCauseGroupId`; `LearningSignalIntakeRecord` | LSC-T0 roadmap | ACCEPT |
| LSC-T0 requires existing intake extension instead of a parallel record | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 148-165, 240 | `LearningSignalIntakeInput`; `LearningSignalIntakeRecord`; existing intake extension | LSC-T0 roadmap | ACCEPT |
| Round-2 review approves LSC-T1 dispatch with N4/N5 folded in | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md` | lines 86, 199-204 | `APPROVE_NO_BLOCKING_FINDINGS`; N4; N5 | advisory rebuttal round 2 | ACCEPT |
| Round-2 review requires exact AAF-to-intake severity mapping | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md` | lines 129-136 | `frictionLevel`; `severity`; no-entry | advisory rebuttal round 2 | ACCEPT |
| Round-2 review requires disposition/captureState authority rule | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md` | lines 139-145 | `captureState`; `disposition` | advisory rebuttal round 2 | ACCEPT |
| Round-2 review requires AAF-T5 checker as source surface | `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md` | lines 150-152 | `check_worker_experience_retrospective.py` | advisory rebuttal round 2 | ACCEPT |
| Learning Signal Intake Bridge owns lanes, defect classes, severity, disposition, input, record, and mutation invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | lines 11-68, 123-173 | `LearningSignalLane`; `LearningSignalDefectClass`; `LearningSignalSeverity`; `LearningSignalDisposition`; `LearningSignalIntakeInput`; `LearningSignalIntakeRecord`; `autonomousMutationAuthorized` | LPF intake bridge | ACCEPT |
| AAF-T5 checker owns worker retro token names and friction levels | `governance/compat/check_worker_experience_retrospective.py` | lines 34-56, 176-200, 273-275 | `WORKER_EXPERIENCE_RETRO`; `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON`; `FRICTION_LEVELS` | worker-experience checker | ACCEPT |
| Worker-experience standard owns token syntax and exact NA assertion | `docs/reference/worker_experience_retrospective/README.md` | lines 47-68 | `WORKER_EXPERIENCE_RETRO`; `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` | worker-experience standard | ACCEPT |
| Future ledger aggregate should use generated source layout and drift check | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | lines 24-29, 31-43, 71-82 | future ledger/manifest aggregate; generator; drift checker | JSON generated aggregate discipline | ACCEPT |
| External-agent returned outputs require classification before governed action | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | lines 35-42, 44-62, 70-78 | external-agent returned output route | external knowledge absorption chain map | ACCEPT |

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `90b06fa0`.
- `git status --short` showed uncommitted LSC-T0 roadmap/review artifacts and
  this LSC-T1 dispatch batch.
- Source verification used direct file reads and `rg -n` lookups against current
  repository files.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base 90b06fa0 --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 90b06fa0 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 90b06fa0 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 90b06fa0 --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed baseline/work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | LSC-T1 signal-ledger source-layout and de-dup contract |
| Disposition | ADAPT as CVF-owned Learning Signal Chain contract |
| Claim boundary | advisory rebuttals become authority only through Codex classification, this baseline, and paired work order |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T1 signal-ledger contract dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation/reference and JSON template authoring only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | source-layout contract, de-dup rule, schema template, and generated-index decision only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| LSC must not create a parallel record beside `LearningSignalIntakeRecord` | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T1 must bind ledger layout to existing intake bridge | handled by this dispatch |
| AAF-to-intake severity mapping needs exact no-entry and blocking rules | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T1 contract must define mapping table | handled by this dispatch |
| `captureState` can drift from governed `disposition` | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T1 contract must define source-of-truth rule | handled by this dispatch |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed by this dispatch | handled |

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`.
- Predecessor intake artifact: `docs/reviews/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_CLAUDE_REBUTTAL_ROUND2_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because round-2 N4/N5 were promoted from advisory findings into LSC-T1 dispatch requirements.
- Routing matrix status: `DO_NOW` for LSC-T1 source-layout/de-dup contract; `SEPARATE_RUNTIME_TRANCHE` for generator/checker/helper/CLI/MCP/runtime work; `STRATEGIC_OPERATOR_DECISION` for later lane ordering; `OUT_OF_SCOPE` for provider/live/public-sync/direct-interception/readiness claims; `RESOLVED_BY_DESIGN` for round-1 parallel-core risk folded into intake-bridge binding.
- Semantic sampling status: sampled N4, N5, and root-cause de-dup owner rule against current source verification.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | LSC remains capture-fast, promotion-slow, and proposal-only. |
| CHANGED_DISPOSITION | N4/N5 moved from advisory refinements into LSC-T1 work-order requirements. |
| NEW_FINDING | AAF `frictionLevel=NONE` and exact NA assertion must create no signal entry. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception scope remains rejected for LSC-T1. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | LSC-T1 documentation/reference and JSON-template contract. |
| SEPARATE_RUNTIME_TRANCHE | generator, drift checker, helper readout, CLI/MCP adapter, runtime bridge. |
| STRATEGIC_OPERATOR_DECISION | ordering of AAF-T6/T7, CGE-T3, ACE-R1, MLW7/8 after LSC-T1. |
| OUT_OF_SCOPE | provider/live, public-sync, direct interception, readiness, universal control. |
| RESOLVED_BY_DESIGN | no parallel learning-signal record; extend or map to existing intake bridge. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LSC-T1-S1 | round-2 N4 | no-friction AAF returns should not create signal entries | mapped into required severity table | prevents empty no-friction returns from polluting de-dup counts | PASS |
| LSC-T1-S2 | round-2 N5 | `disposition` and `captureState` can conflict | mapped into source-of-truth rule | prevents derived state from overriding governed disposition | PASS |
| LSC-T1-S3 | LSC-T0 de-dup | projections must share one root cause | mapped into rootCauseGroupId requirement | prevents AAF/Finding/MLW projections from triple-counting | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch for Learning Signal Chain contract work. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Claim Boundary

This baseline authorizes only a documentation/reference and schema-template
contract for LSC-T1. It does not implement a ledger store, generator, checker,
helper readout, runtime Learning Plane mutation, provider/live proof, CLI/MCP
adapter behavior, public-sync, direct interception, wrapper/proxy enforcement,
queue/daemon, watcher, readiness, cost optimization, full-hook equivalence, or
universal governed-coding control.
