# CVF Agent Work Order - INDEX-T1 Forward-Only INDEX Classification Checker

Memory class: FULL_RECORD

Status: HOLD_UNTIL_MPI_T0_CLOSURE

Date: 2026-06-21

docType: work_order

dispatchBaseHead: acb2b980

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker after dependency release. Reviewer/closer is a separate role after
worker return.

Canonical packet:
`docs/work_orders/CVF_WO_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md`

Current status: `HOLD_UNTIL_MPI_T0_CLOSURE`. Do not execute until the
Dependency Release Gate is refreshed by dispatcher/reviewer after MPI-T0 closes.

Commit mode after release: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: to be confirmed with `git rev-parse --short HEAD` at worker
start after dependency release.

Current-time notes: INDEX-T1 is a small checker tranche after MPI-T0. MPI-T0
creates the forward-only INDEX standard and legacy recheck. INDEX-T1 only
promotes that accepted standard into deterministic governance checking for
future classification artifacts and agent handoffs.

Do-not-misread notes: do not implement this while the work order remains HOLD.
Do not rescan legacy, mutate Memory runtime, edit generated registries, build a
vector DB, implement graph persistence, build CLI/MCP adapters, run provider or
live proof, touch public-sync, or claim universal governed-coding control.

Required first actions after release: read this work order, read the
INDEX-T1 GC-018 baseline, read the accepted MPI-T0 INDEX standard and completion
review, refresh `executionBaseHead`, inspect `git status --short`, then
implement only the Allowed scope.

Return contract after release: return `COMPLETE_PENDING_REVIEW` with only
allowed uncommitted artifacts, actual `executionBaseHead`, actual
`git status --short`, focused unittest/checker/fast-gate evidence, and no
commit. If blocked, return `BLOCKED_WITH_REASON` and name the exact dependency,
source, or gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Purpose

Create the post-MPI-T0 checker tranche that makes INDEX a forward-only,
machine-enforced classification discipline for future CVF classification
artifacts and agent handoffs that enter governed workflows.

This work order is not dispatch-ready yet. It is a dependency-held packet that
preserves the operator decision without disrupting MPI-T0 or MPI-T1 sequencing.

## Dependency Release Gate

| Dependency | Required release evidence | Current status |
|---|---|---|
| MPI-T0 INDEX standard | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` exists and is accepted by reviewer | HOLD |
| MPI-T0 worker return | `docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_WORKER_RETURN_2026-06-21.md` accepted or superseded by reviewer completion | HOLD |
| MPI-T0 completion review | `docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_COMPLETION_2026-06-21.md` records closure disposition | HOLD |
| Source verification refresh | this work order cites actual sections of the accepted INDEX standard | HOLD |

Dispatcher/reviewer must keep this work order in `HOLD_UNTIL_MPI_T0_CLOSURE`
until every dependency row has concrete artifact evidence. A worker must return
`BLOCKED_WITH_REASON` if asked to execute before release.

## Agent Roles

| Role | Owner | Commitment boundary |
|---|---|---|
| Dispatcher | Codex/orchestrator | creates dependency-held GC-018 baseline and work order; refreshes after MPI-T0 closure |
| Worker | future worker after release | edits only Allowed scope and returns uncommitted |
| Reviewer/closer | Codex/orchestrator after worker return | validates checker behavior, hook wiring, protected-path authorization, and commits accepted material |
| Operator | human operator | checkpoint for dependency release, scope expansion, runtime/provider/public work, secrets, or destructive action |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-21: create a small checker tranche after MPI-T0 so INDEX becomes mandatory governance without disrupting the MPI roadmap | ACCEPT |
| INDEX-T1 GC-018 baseline | `docs/baselines/CVF_GC018_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md` | ACCEPT |
| MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` row `INDEX-T1` | ACCEPT |
| Guard orientation index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Work order template family | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reference/work_order_template/README.md` | ACCEPT |
| Accepted INDEX standard | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | ACCEPT - created by MPI-T0 and accepted by reviewer; INDEX-T1 remains parked for operator selection |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | REVIEW_AND_CLASSIFY_BEFORE_ABSORPTION |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | INDEX-T1 work order |
| Disposition | ADAPT as dependency-held checker implementation packet |
| Claim boundary | no external input is source authority; accepted MPI-T0 standard controls future enforcement |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher creates held packet; future worker implements checker after release; reviewer/closer validates and commits if accepted |
| phase | HOLD; DISPATCH_REFRESH; EXECUTION_AFTER_RELEASE; CLOSURE; SESSION_SYNC_IF_NEEDED |
| baseHeadFor(phase) | `dispatchBaseHead=acb2b980`; `executionBaseHead` set after MPI-T0 release; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Allowed scope after release; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | future worker-return trace covers INDEX-T1 artifacts; reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing; reviewer/closer owns accepted material/closure/session-sync commit |
| crossBatchIsolation | do not mix INDEX-T1 with MPI-T0 implementation, MPI-T1/T2/T3/T4 runtime, Memory runtime, public-sync, provider/live, adapter work, legacy rescan, or session-sync unless separately authorized |
| Before status evidence | committed base `acb2b980`; current packet is uncommitted and dependency-held |
| nextMoveSurfaces | update only after closure if current mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_COMPLETION_2026-06-21.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; worker-return artifact; reviewer-owned completion review; optional roadmap status/session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` after release |
| closer | reviewer/closer role |

## Core Guard Self-Protection Authorization

| Field | Disposition |
|---|---|
| Protected paths authorized | `governance/compat/check_index_classification.py`; `governance/compat/test_check_index_classification.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Authorization source | operator instruction; INDEX-T1 GC-018 baseline; this work order |
| Authorized scope | add deterministic INDEX classification checker, focused tests, and narrow hook/autorun wiring after MPI-T0 dependency release |
| Rollback boundary | revert only INDEX-T1 checker/test/wiring/template/reference edits if checker gate fails or exceeds scope |
| Not authorized | runtime Memory changes, provider/live proof, public-sync, external dependency adoption, adapter behavior, generated aggregate edits, session-sync, or retroactive rewrite |

## Required First Reads After Release

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | guard/checker maintenance routing and protected-path authorization rule |
| `docs/baselines/CVF_GC018_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md` | GC-018 authorization and claim boundary |
| `docs/work_orders/CVF_WO_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md` | current work order and dependency-release state |
| `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | accepted standard to enforce |
| `docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_COMPLETION_2026-06-21.md` | MPI-T0 release evidence and any reviewer limitations |
| `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | INDEX-T1 row and MPI sequencing |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | work-order source verification and claim-language rules |
| `docs/reference/work_order_template/README.md` | template family index for updating references |
| `governance/compat/run_agent_autorun_workflow_gate.py` | autorun common command wiring surface |
| `governance/compat/run_local_governance_hook_chain.py` | local hook chain wiring surface |
| `governance/compat/check_corpus_intelligence_classification.py` | nearby range-aware classification checker pattern |

## Allowed Scope After Release

The future worker may change only:

- `governance/compat/check_index_classification.py`
- `governance/compat/test_check_index_classification.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/work_order_template/README.md`
- `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_WORKER_RETURN_2026-06-21.md`

## Write Ownership

| Path | Owner during worker execution after release | Disposition |
|---|---|---|
| `governance/compat/check_index_classification.py` | worker | create |
| `governance/compat/test_check_index_classification.py` | worker | create |
| `governance/compat/run_agent_autorun_workflow_gate.py` | worker | update narrowly |
| `governance/compat/run_local_governance_hook_chain.py` | worker | update narrowly |
| `docs/reference/guard_orientation/README.md` | worker | update narrowly |
| `docs/reference/work_order_template/README.md` | worker | update narrowly |
| `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_WORKER_RETURN_2026-06-21.md` | worker | create |
| `docs/baselines/CVF_GC018_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md` | reviewer/closer | no worker edit unless explicitly released by reviewer |
| this work order | reviewer/closer | no worker edit unless explicitly released by reviewer |
| Memory runtime, generated aggregates, session state, active handoff, public-sync, MCP, `.github/**` | out of worker scope | forbidden |

## Forbidden Scope

The worker must not:

- edit Memory runtime, runtime extension paths, generated JSON aggregates, scan registry
  entries or aggregate, active session state, active handoff, public-sync, MCP
  packages, dependency manifests, `.github/**`, or public repository files;
- implement vector DB, embedding store, graph persistence, CLI/MCP adapter
  behavior, provider/live proof, wrapper/proxy enforcement, direct IDE/shell/git
  interception, arbitrary command execution, EDIT/COMMIT execution, queue,
  daemon, watcher, readiness, or universal governed-coding control;
- rescan legacy, expand KGR, implement MPI-T1/T2/T3/T4, mutate runtime Learning
  Plane, create durable store, implement LSC ledger, or rewrite historical CVF
  artifacts.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| INDEX-T1 is a planned checker tranche | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | Tranche Plan | `INDEX-T1` | MPI roadmap | VALUE_SET | ACCEPT |
| INDEX-T1 is held after MPI-T0 | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | Work Plan | `HOLD_AFTER_MPI_T0` | MPI roadmap | VALUE_SET | ACCEPT |
| Protected checker work needs guard authorization | `docs/reference/guard_orientation/README.md` | Task Class Guard Map | `Guard / checker maintenance` | Guard orientation index | VALUE_SET | ACCEPT |
| Work orders require source verification | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Enforcement / Verification | Source Verification Block | Work order template | VALUE_SET | ACCEPT |
| Template family README is the stable index for template references | `docs/reference/work_order_template/README.md` | Scope / Target / Owner Boundary; Canonical Template | `docs/reference/work_order_template/README.md` | Work order template family | EXISTS | ACCEPT |
| Autorun gate wiring surface exists | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `GateCommand` | Autorun workflow gate | EXISTS | ACCEPT |
| Local hook chain wiring surface exists | `governance/compat/run_local_governance_hook_chain.py` | `HOOK_CHAINS` | `reviewer-fast`; `pre-commit`; `pre-push` | Local governance hook chain | EXISTS | ACCEPT |
| Range-aware classification checker pattern exists | `governance/compat/check_corpus_intelligence_classification.py` | script constants and range helpers | `THIS_SCRIPT_PATH` | Corpus intelligence classification checker | EXISTS | ACCEPT |
| INDEX standard exists and defines enforceable blocks | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | created by MPI-T0 and accepted by reviewer | `CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | INDEX standard | EXISTS | ACCEPT |

## Pre-Flight Checks

Before this work order can move out of HOLD, dispatcher/reviewer must run:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base acb2b980 --head HEAD --enforce
python governance/compat/check_core_guard_self_protection.py --base acb2b980 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base acb2b980 --head HEAD
```

After dependency release, worker must also run the Required Checks After
Release section.

## Negative Search And Collision Discipline

Search roots: `docs`; `governance`.

Search command / query:
`rg -n "CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21|check_index_classification|test_check_index_classification" docs governance --glob !docs/baselines/CVF_GC018_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md --glob !docs/work_orders/CVF_WO_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md`

Coverage: source, tests, docs, JSON, and external-evidence-bearing governed
artifacts under the searched roots.

| Check | Command or evidence | Result | Collision / disposition |
|---|---|---|---|
| INDEX standard present after MPI-T0 closure | `Test-Path docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | `True` | keep work order parked until operator selects INDEX-T1 |
| INDEX checker not yet present | `Test-Path governance/compat/check_index_classification.py` | `False` | create only after dependency release |
| INDEX checker tests not yet present | `Test-Path governance/compat/test_check_index_classification.py` | `False` | create only after dependency release |
| `CVF_AGENT_WORK_ORDER_TEMPLATE_2026` same-token collision occurrence | template references appear elsewhere | non-authoritative collision | not binding as INDEX standard/checker evidence |
| `CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026` same-token collision occurrence | handoff contract references appear elsewhere | non-authoritative collision | not binding as INDEX standard/checker evidence |
| `EXISTS` same-token collision occurrence | source-verification vocabulary appears elsewhere | non-authoritative collision | not binding for the missing INDEX standard/checker files |
| `INDEX` same-token collision occurrence | planning and MPI-T0 references appear elsewhere | non-authoritative collision | not binding as existing standard/checker implementation |
| `MPI` same-token collision occurrence | roadmap and tranche vocabulary appears elsewhere | non-authoritative collision | not binding as INDEX-T1 dependency release evidence |
| `MULTI_AGE` same-token collision occurrence | derived from multi-agent route vocabulary and appears elsewhere | non-authoritative collision | not binding as INDEX standard/checker evidence |
| `README` same-token collision occurrence | README references appear elsewhere | non-authoritative collision | not binding as INDEX standard/checker evidence |
| `CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP` same-token collision occurrence | external-intake chain map references appear elsewhere | non-authoritative collision | not binding as INDEX standard/checker evidence |
| `HEAD` same-token collision occurrence | git command vocabulary appears elsewhere | non-authoritative collision | not binding as dependency release evidence |
| Existing mentions are planning/dependency references | exact search command above | hits only in MPI-T0/roadmap planning references and existing corpus checker references | no collision with existing INDEX checker |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order requirement | Disposition |
|---|---|---|
| MPI-T0 authors the INDEX standard | Dependency Release Gate blocks execution until accepted standard exists | ACCEPT |
| INDEX-T1 promotes policy to machine enforcement | Allowed scope includes checker, tests, hook/autorun wiring, and references | ACCEPT |
| Do not merge checker into MPI-T0 | Status remains HOLD until MPI-T0 closure; worker cannot execute early | ACCEPT |
| Avoid runtime/readout/vector/graph expansion | Forbidden Scope excludes runtime, Memory, vector, graph, provider/live, public-sync, and adapter work | ACCEPT |

## Execution Plan

Held packet phase:

1. Keep this work order in `HOLD_UNTIL_MPI_T0_CLOSURE`.
2. Wait for MPI-T0 worker return and reviewer completion.
3. Refresh Source Verification rows against the accepted INDEX standard.
4. Rerun pre-dispatch gate before any worker execution.

After dependency release:

1. Capture `executionBaseHead`.
2. Capture `git status --short`.
3. Read Required First Reads.
4. Implement `check_index_classification.py`.
5. Implement focused tests.
6. Wire checker into the narrowest hook/autorun surfaces.
7. Update guard orientation and work-order template family references.
8. Run required checks.
9. Create worker-return artifact.
10. Return `COMPLETE_PENDING_REVIEW` uncommitted or `BLOCKED_WITH_REASON`.

## Future Checker Contract

After dependency release, the checker should enforce only forward-looking INDEX
discipline. It should fail future applicable artifacts when:

- an artifact claims INDEX-governed classification but omits the required INDEX
  block or required classification fields from the accepted standard;
- a classification artifact uses ambiguous or non-terminal dispositions where
  the standard requires terminal disposition;
- an artifact claims retroactive rewrite of historical CVF artifacts;
- an artifact treats provider/private memory as CVF source authority;
- an artifact claims runtime, public, provider/live, adapter, vector, graph, or
  direct-interception enforcement outside its allowed scope;
- a worker-return or work-order packet routes INDEX-governed work without the
  required dependency/source-verification evidence.

The checker must avoid semantic overreach. It may validate structure, required
blocks, allowed tokens, path scope, and claim-boundary language. It must not
judge the truth of legacy findings, execute external agents, read provider
memory, run live proof, or mutate artifacts.

## Required Checks After Release

The future worker must run:

```powershell
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_check_index_classification
python governance/compat/check_index_classification.py --base <releasedBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_index_classification.py
```

If hook/autorun wiring is changed, reviewer may additionally require:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <releasedBaseHead> --head HEAD
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
```

## Evidence Requirements

The worker-return packet must record:

- actual `executionBaseHead`;
- actual before/after `git status --short`;
- exact changed-file manifest;
- focused unittest output;
- checker command output;
- worker-return fast-gate output;
- hook/autorun evidence when wiring changed;
- explicit no-runtime/no-generated/no-session/no-public/no-provider/no-MCP
  boundary;
- exact Claim Boundary and Public Export Disposition.

## Review Gate

Reviewer/closer must reject or return the worker output if:

- MPI-T0 dependency release is not refreshed in this work order;
- any path outside Allowed Scope is changed;
- checker behavior exceeds structural validation into semantic truth judgment;
- checker claims runtime/provider/live/public/adapter/vector/graph enforcement;
- hook/autorun wiring is broad, duplicated, or untested;
- focused tests do not cover missing INDEX block, retroactive rewrite,
  provider/private authority misuse, and forbidden expansion claims;
- protected-path authorization is missing or stale.

## Worker Autonomy / No-Question Rule

After dependency release, the worker must repair allowed-scope checker, test,
template-reference, guard-orientation, packet-shape, source-fidelity, or gate
failures and rerun relevant gates without asking the operator.

The worker must stop and return `BLOCKED_WITH_REASON` only when the repair would
exceed Allowed scope, change the claim boundary, require runtime/provider/live/
public-sync/MCP/generated/session/handoff edits, release a new dependency,
consume secrets or quota, alter parked-lane ordering, touch forbidden paths, or
perform destructive or irreversible actions.

## Acceptance Criteria After Release

| Criterion | Required evidence |
|---|---|
| INDEX standard dependency released | accepted MPI-T0 completion review and actual standard sections cited |
| Checker exists | `governance/compat/check_index_classification.py` |
| Focused tests exist | `governance/compat/test_check_index_classification.py` |
| Checker catches missing INDEX block | focused test evidence |
| Checker catches forbidden retroactive rewrite claim | focused test evidence |
| Checker catches provider/private memory authority misuse | focused test evidence |
| Checker catches forbidden runtime/public/provider/live/adapter/vector/graph claim expansion | focused test evidence |
| Hook/autorun wiring is narrow and tested | changed command lists plus reviewer-fast or autorun evidence |
| Guard orientation/template references updated | changed reference paths and no file-size guard failure |
| Forbidden scope untouched | `git diff --name-status` and `git status --short` evidence |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only after dependency release, allowed
artifacts exist, focused tests pass, checker command passes, worker-return gate
passes or records allowed `N/A with reason`, and all changes remain uncommitted.

Return `BLOCKED_WITH_REASON` when MPI-T0 dependency is not released, the accepted
standard lacks enforceable fields, source verification fails, a gate fails
outside worker-owned scope, or a necessary action would exceed Allowed scope.

## Operator Checkpoint

Operator checkpoint is required before releasing this HOLD packet for worker
execution, broadening checker scope, touching runtime/provider/live/public/MCP/
generated/session/handoff surfaces, adopting dependencies, changing MPI
sequence, or claiming INDEX is fully enforced outside governed CVF artifact
flows.

No operator checkpoint is needed for keeping this packet held or for
allowed-scope remediation after dependency release.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation storage class | governance checker/source-test and reference pointer updates |
| New durable storage | none |
| Generated aggregate impact | none |
| Source layout | `governance/compat/check_index_classification.py`; `governance/compat/test_check_index_classification.py` |
| Index/front-door updates | `docs/reference/guard_orientation/README.md`; `docs/reference/work_order_template/README.md` |
| Layout boundary | no Memory runtime, vector DB, graph persistence, generated registry, session state, or public-sync changes |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | INDEX-T1 dependency-held checker packet and future structural checker only |
| claimDisposition | N/A with reason: no Delta execution-control behavior is implemented or claimed |
| receiptEvidence | N/A with reason: no Delta receipt is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | future worker execution only after MPI-T0 dependency release |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | checker planning and future structural validation only |
| forbiddenExpansion | enforcement wrapper, proxy enforcement, interception, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, cost optimization, and universal control remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher role |
| Provider or surface | local workspace |
| Session or invocation | INDEX-T1 work order authoring, 2026-06-21 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Codex apply_patch |
| Target paths | `docs/baselines/CVF_GC018_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md`; `docs/work_orders/CVF_WO_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md`; `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` |
| Allowed scope source | operator instruction to create post-MPI-T0 checker work order |
| Before status evidence | HEAD `acb2b980`; existing MPI packet files uncommitted |
| After status evidence | INDEX-T1 GC-018/work order created; roadmap work-order list updated; uncommitted |
| Diff evidence | new held baseline and work order; roadmap trace update |
| Approval boundary | dependency-held checker packet only; no implementation before MPI-T0 release |
| Claim boundary | planning/dispatch artifact only; no current machine enforcement claim |
| Agent type | dispatcher |
| Invocation ID | index-t1-work-order-authoring-2026-06-21 |
| Expected manifest | INDEX-T1 GC-018 baseline; INDEX-T1 work order; MPI roadmap trace update |
| Actual changed set | pending git status |
| Manifest delta | MATCH |

## Closure Checklist

Reviewer/closer closure evidence must resolve these items after release:

- MPI-T0 dependency release is refreshed.
- Accepted INDEX standard sections are source-verified.
- Checker and focused tests exist.
- Hook/autorun wiring is narrow and tested.
- Guard orientation/template references are updated.
- No forbidden paths changed.
- Required checks pass.
- Worker-return packet includes required sections and worker-experience token.
- Session-sync is performed only if mode or next-move surfaces change.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Dependency release | MPI-T0 completion review and accepted INDEX standard | dispatcher/reviewer refresh | HOLD |
| GC-018 status | `docs/baselines/CVF_GC018_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md` | reviewer updates after accepted worker return | HOLD |
| Work order status | this work order | reviewer updates after dependency release and closure | HOLD |
| Checker | `governance/compat/check_index_classification.py` | exists after worker return | HOLD |
| Tests | `governance/compat/test_check_index_classification.py` | unittest pass after worker return | HOLD |
| Worker return | `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_WORKER_RETURN_2026-06-21.md` | status row | HOLD |
| Completion review | `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_COMPLETION_2026-06-21.md` | reviewer-owned final disposition | HOLD |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance checker planning. No public-sync,
public-facing claim, or public repository mutation is authorized.

## Claim Boundary

This work order is a dependency-held future checker packet. It does not claim
INDEX is currently machine-enforced, does not dispatch implementation before
MPI-T0 closure, and does not authorize Memory runtime changes, legacy rescan,
provider/live proof, public-sync, vector DB, graph persistence, CLI/MCP adapter
behavior, wrapper/proxy enforcement, direct IDE/shell/git/filesystem
interception, arbitrary command execution, EDIT/COMMIT execution, queue,
daemon, watcher, readiness, full-hook equivalence, cost optimization, or
universal governed-coding control.
