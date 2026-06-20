# CVF GC-018 - LSC-T3 Fast Helper Readout

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-21

docType: baseline

dispatchBaseHead: aca3ec97

Batch ID: LSC-T3

## Purpose

Authorize LSC-T3 as the next bounded Learning Signal Chain foundation tranche:
a read-only helper readout that surfaces helper-detectable unresolved learning
signals and a next suggested action without adding deep gate cost.

LSC-T3 follows closed LSC-T4, which supplied promotion outcome vocabulary and
blocking-vs-readout rules. LSC-T3 must use that vocabulary to make current
signals visible to internal and future CLI/MCP-connected external agents, while
preserving the LSC promise: fast capture, slow promotion.

## Operator Authorization

The operator selected the roadmap order on 2026-06-21:

`LSC-T2 -> LSC-T4 -> LSC-T3 -> LSC-T6 -> LSC-T5/T7`.

LSC-T4 is now closed at material commit `b568f248`, and session continuity is
synced at `aca3ec97`. The next allowed move is LSC-T3 dispatch.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-21 roadmap order selecting LSC-T3 after LSC-T4 closure | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| LSC-T0 roadmap | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | ACCEPT |
| LSC reference front door | `docs/reference/learning_signal_chain/README.md` | ACCEPT |
| LSC-T1 source-layout and de-dup contract | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | ACCEPT |
| LSC-T2 multi-role capture contract | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | ACCEPT |
| LSC-T4 promotion threshold policy | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | ACCEPT |
| AAF helper source | `governance/compat/run_agent_automation_assist.py` | SOURCE_AUTHORITY_FOR_HELPER_INTERFACE |
| AAF helper focused tests | `governance/compat/test_run_agent_automation_assist.py` | SOURCE_AUTHORITY_FOR_FOCUSED_TEST_SHAPE |
| Worker-experience checker | `governance/compat/check_worker_experience_retrospective.py` | SOURCE_AUTHORITY_FOR_WORKER_RETRO_DIAGNOSTICS |

Provider-specific memory, chat memory, and private agent-local files are not
CVF source authority. External-agent outputs are input only until routed through
the external knowledge absorption chain and promoted by governed CVF artifacts.

## Scope / Owner Boundary

Allowed worker scope:

- update `governance/compat/run_agent_automation_assist.py` to add an LSC-T3
  read-only signal readout using existing helper diagnostics and LSC-T4
  outcome vocabulary;
- update `governance/compat/test_run_agent_automation_assist.py` with focused
  tests for the readout JSON and human output;
- create `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md`
  as the bounded helper readout contract;
- update `docs/reference/learning_signal_chain/README.md` with an LSC-T3 row;
- create `docs/reviews/CVF_LSC_T3_FAST_HELPER_READOUT_WORKER_RETURN_2026-06-21.md`;
- keep the helper read-only, local, advisory, and changed-set based;
- surface only helper-detectable local signals, not a complete ledger or global
  historical signal store.

Forbidden worker scope:

- no edits to `CVF_SESSION/**`, active handoff, root startup routers,
  public-sync, `.github/**`, dependency manifests, web UI, MCP packages, or
  runtime provider/source routes outside the named helper/test paths;
- no ledger source directory, generated aggregate, generator, drift checker,
  durable store, CLI/MCP adapter, provider/live proof, dependency install,
  queue, daemon, watcher, wrapper/proxy, direct IDE/shell/git/filesystem
  interception, arbitrary command execution, or EDIT/COMMIT execution;
- no public catalog update, public/production/release readiness, full-hook
  equivalence, cost optimization, speed claim, or universal
  governed-coding-control claim;
- no implementation of LSC-T5, LSC-T6, LSC-T7, AAF-T6, AAF-T7, CGE-T3,
  ACE-R1, MLW7, or MLW8.

Risk ceiling: R1 local read-only helper diagnostic and reference contract.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts changed or created:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`
- `docs/reference/learning_signal_chain/README.md`
- `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md`
- `docs/reviews/CVF_LSC_T3_FAST_HELPER_READOUT_WORKER_RETURN_2026-06-21.md`

No session, handoff, public-sync, provider/live, MCP, dependency, queue/daemon,
or runtime mutation path is authorized in worker execution.

## Decision / Baseline / Proposed Tranche

Baseline decision: LSC-T3 is ready for worker dispatch as a bounded helper
readout tranche after LSC-T4 closure.

Proposed tranche: `LSC-T3 Fast Helper Readout`.

Tranche owner split: dispatcher creates this GC-018 baseline and paired work
order; worker implements only the read-only helper/readout contract, focused
tests, reference/front-door update, and worker-return artifact without
committing; reviewer/closer reviews and commits accepted material if gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| LSC-T0 defines LSC-T3 as Fast Helper Readout | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | line 254 | `LSC-T3`; Fast Helper Readout | LSC-T0 roadmap | ACCEPT |
| LSC-T0 requires future work orders to keep capture fast and promotion governed | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 301-316 | Acceptance Criteria For Future Work Orders | LSC-T0 roadmap | ACCEPT |
| LSC-T2 defines multi-role signal eligibility and no-signal boundaries | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 85-90, 106-126 | Capture Eligibility Matrix; no-signal guidance | LSC-T2 contract | ACCEPT |
| LSC-T2 maps role signals to existing intake fields without adding runtime fields | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 141-149, 161-164 | `sourceSummary`; `lane`; `severity` | LSC-T2 contract | ACCEPT |
| LSC-T2 preserves closure blocking only for critical or observed repeated signals | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | line 202 | closure blocking rule | LSC-T2 contract | ACCEPT |
| LSC-T4 defines outcome vocabulary consumed by LSC-T3 | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | lines 61-79 | `READOUT_ONLY`; `WATCH_FOR_REPEAT`; `GOVERNANCE_PROPOSAL_CANDIDATE`; `RULE_CANDIDATE`; `CHECKER_CANDIDATE`; `WORK_ORDER_CANDIDATE`; `CLOSURE_BLOCKER` | LSC-T4 policy | ACCEPT |
| LSC-T4 defines threshold matrix and blocking-vs-readout behavior | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | lines 83-130 | Threshold Decision Matrix; Blocking-Vs-Readout Policy | LSC-T4 policy | ACCEPT |
| LSC-T4 states LSC-T3 helper should consume outcome vocabulary | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | lines 205-219 | LSC-T3 Future-Tranche Routing; Latency Budget | LSC-T4 policy | ACCEPT |
| AAF helper is read-only and changed-set based | `governance/compat/run_agent_automation_assist.py` | lines 1-18 | module docstring | AAF helper | ACCEPT |
| AAF helper report owns JSON fields and defects list | `governance/compat/run_agent_automation_assist.py` | lines 459-510 | `AssistReport`; `to_dict` | AAF helper | ACCEPT |
| AAF helper builds report from changed paths and diagnostics | `governance/compat/run_agent_automation_assist.py` | lines 514-620 | `build_report` | AAF helper | ACCEPT |
| AAF helper owns human output rendering | `governance/compat/run_agent_automation_assist.py` | lines 624-669 | `_print_human` | AAF helper | ACCEPT |
| AAF helper CLI owns `--json` and `--enforce` behavior | `governance/compat/run_agent_automation_assist.py` | lines 672-710 | `main` | AAF helper CLI | ACCEPT |
| Existing focused tests cover BuildReport and CLI output shape | `governance/compat/test_run_agent_automation_assist.py` | lines 258-365 | `BuildReportTests`; `CliOutputTests` | AAF helper focused tests | ACCEPT |
| Existing focused tests cover corpus diagnostics JSON | `governance/compat/test_run_agent_automation_assist.py` | lines 365-499 | `CorpusDiagnosticTests`; `BuildReportCorpusTests` | AAF helper focused tests | ACCEPT |
| Existing focused tests cover worker-experience helper diagnostics | `governance/compat/test_run_agent_automation_assist.py` | lines 597-623 | `WorkerExperienceHelperDiagnosticTests` | AAF helper focused tests | ACCEPT |
| Worker-experience checker exposes `diagnose` and eligible retro semantics | `governance/compat/check_worker_experience_retrospective.py` | lines 34-61, 153-201 | `RETRO_TOKEN`; `RETRO_NA_TOKEN`; `diagnose` | worker-experience checker | ACCEPT |

## New Doc-Only Terms

| Proposed term | Owner in LSC-T3 | Runtime status | Reason |
|---|---|---|---|
| `signalReadout` | AAF helper JSON report and LSC-T3 reference contract | DOC_ONLY_NEW until implemented by worker in helper output | advisory list of helper-detectable current signals |
| `SignalReadoutItem` | AAF helper internal dataclass if worker chooses dataclass implementation | DOC_ONLY_NEW / helper-local | stable internal shape for one advisory readout row |
| `nextSuggestedAction` | AAF helper readout item | DOC_ONLY_NEW / helper-local | human-readable next action, not an executable command |
| `blocking` | AAF helper readout item | DOC_ONLY_NEW / helper-local | advisory boolean derived from LSC-T4 blocker rules; no gate authority |

These terms are helper/report vocabulary only. They must not be presented as
existing runtime fields, ledger schema fields, or CLI/MCP adapter fields.

## Required Helper Contract

The worker must implement an LSC-T3 helper readout with these properties:

- read-only: no writes, no staging, no commits, no pushes, no deletes, no
  provider/live calls, no arbitrary command execution;
- fast: reuse already-computed helper diagnostics from `build_report`; do not
  run full gates from inside the helper;
- advisory: readout items recommend next actions, but do not block closure or
  execute promotion;
- local: surface only changed-set helper-detectable signals, not a complete
  historical ledger;
- LSC-T4 vocabulary: each item must use one of the LSC-T4 outcomes, with
  routine low/medium issues defaulting away from `CLOSURE_BLOCKER`;
- JSON-visible: `--json` output must include a stable `signalReadout` list;
- human-visible: non-JSON output must print a concise Learning Signal Readout
  section;
- no-signal cheap path: if no helper-detectable signal exists, output a short
  no-signal line and keep `defects=[]`.

Minimum item fields:

| Field | Required behavior |
|---|---|
| `sourcePath` | changed path or `N/A_WITH_REASON` when not path-specific |
| `sourceSurface` | helper diagnostic surface such as work-order, corpus, worker-experience, steward-lane |
| `severity` | `low`, `medium`, `high`, or `critical`; default to `low` unless existing diagnostic severity is source-backed |
| `repeatRisk` | default `POSSIBLE`; do not claim `OBSERVED_REPEATED` without ledger/de-dup proof |
| `recommendedOutcome` | one LSC-T4 outcome vocabulary value |
| `nextSuggestedAction` | concise advisory text for the operator/reviewer/worker |
| `blocking` | `true` only if LSC-T4 blocker rules are satisfied; otherwise `false` |
| `reason` | concise source-backed reason |

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `aca3ec97`.
- `git status --short` was clean before LSC-T3 dispatch authoring.
- Source verification used direct file reads and `rg -n` lookups against
  current repository files.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base aca3ec97 --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base aca3ec97 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base aca3ec97 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base aca3ec97 --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed baseline/work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | LSC-T3 fast helper readout |
| Disposition | ADAPT as CVF-owned helper/readout tranche |
| Claim boundary | external-agent returns remain input only until classified and promoted through governed CVF artifacts; LSC-T3 does not implement external-agent CLI/MCP IO |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T3 fast helper readout dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | read-only local helper diagnostics only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | helper readout, unresolved local signal visibility, and next suggested action only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Agents need fast visibility into unresolved helper-detectable signals | HELPER_GAP | GOVERNANCE_CONTROL_PLANE | WORK_ORDER_CANDIDATE | LSC-T3 must add read-only signal readout to AAF helper | handled by this dispatch |
| Readout must not make routine signals closure blockers | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T3 must consume LSC-T4 blocking-vs-readout policy | handled by this dispatch |
| External CLI/MCP agents will later need portable signal IO | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | keep LSC-T6 parked for schema/adapter contract | deferred |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed by this dispatch | handled |

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`.
- Predecessor intake artifact: `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md`.
- Predecessor capture artifact: `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md`.
- Predecessor promotion artifact: `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because LSC-T3 moves helper readout from roadmap row into dispatch-ready helper work.
- Routing matrix status: `DO_NOW` for read-only helper diagnostic and focused tests; `SEPARATE_RUNTIME_TRANCHE` for ledger store, generator, drift checker, CLI/MCP adapter, runtime bridge, or latency guard enforcement; `STRATEGIC_OPERATOR_DECISION` for LSC-T6 and LSC-T5/T7 after LSC-T3; `OUT_OF_SCOPE` for provider/live/public-sync/direct-interception/readiness claims.
- Semantic sampling status: sampled LSC-T0 LSC-T3 row, LSC-T0 future-work acceptance criteria, LSC-T2 role signal rules, LSC-T4 outcome/blocking rules, AAF helper report functions, AAF helper tests, and worker-experience checker.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | LSC remains capture-fast, promotion-slow, and proposal-only. |
| CHANGED_DISPOSITION | LSC-T3 helper readout moved from roadmap row into dispatch requirements. |
| NEW_FINDING | The helper needs an explicit signal readout surface so agents see unresolved local diagnostics without running deep gates. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception/CLI-MCP adapter scope remains rejected for LSC-T3. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | LSC-T3 read-only helper readout and focused tests. |
| SEPARATE_RUNTIME_TRANCHE | ledger store, source directory, generator, drift checker, CLI/MCP adapter, runtime bridge, latency guard. |
| STRATEGIC_OPERATOR_DECISION | LSC-T6, then LSC-T5/T7 per active roadmap order. |
| OUT_OF_SCOPE | provider/live, public-sync, direct interception, readiness, universal control. |
| RESOLVED_BY_DESIGN | surface current helper-detectable signals instead of creating a global signal store. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LSC-T3-S1 | LSC-T0 work plan | LSC-T3 exits with read-only helper diagnostic and focused tests | mapped into Required Deliverables | prevents docs-only closure for helper tranche | PASS |
| LSC-T3-S2 | LSC-T4 outcome vocabulary | readout must use T4 outcomes | mapped into Required Helper Contract | prevents invented outcome names | PASS |
| LSC-T3-S3 | AAF helper source | helper is read-only and changed-set based | allowed scope limited to helper/test | prevents runtime or gate execution expansion | PASS |
| LSC-T3-S4 | LSC-T4 blocking policy | routine readout does not block closure | Required Helper Contract sets `blocking=false` unless blocker conditions are met | prevents latency regression | PASS |

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - LSC-T3 dispatch is a bounded
  helper/readout work order, not a corpus enumeration or legacy scan.
- Corpus root: NOT_APPLICABLE_WITH_REASON - no corpus root is assigned.
- Snapshot time: NOT_APPLICABLE_WITH_REASON - no corpus snapshot is taken.
- Enumeration command: filesystem-backed direct file reads listed in Source
  Verification Block and Required First Reads; no corpus enumeration command is
  authorized.
- Manifest artifact or inline manifest: inline Source Verification Block above.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is
  created.
- Processing ledger artifact or inline ledger: inline Source Verification Block
  and semantic sampling tables above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=corpus enumeration and legacy scan surfaces out of scope; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: corpus scan, legacy source-family enumeration,
  public-sync copy, runtime/provider/live proof, CLI/MCP adapter, and parked lanes.
- Unreadable or unsupported files: 0.
- Aggregation check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate is
  created.
- Drift check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate or generated
  corpus registry is changed.
- Output traceability: Required Deliverables and Source Verification Block
  define all worker output traceability.
- Adversarial verification: reviewer/closer must run reviewer-fast or stricter
  applicable gate before acceptance.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch for Learning Signal Chain helper work. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Claim Boundary

This baseline authorizes only LSC-T3 read-only local helper readout work and
focused tests for current helper-detectable signals. It does not implement a
ledger store, generator, drift checker, durable store, runtime Learning Plane
mutation, provider/live proof, CLI/MCP adapter behavior, public-sync, direct
interception, wrapper/proxy enforcement, queue/daemon, watcher, readiness, cost
optimization, full-hook equivalence, or universal governed-coding control.
