# CVF GC-018 - AAF-T3 Guard Orientation Index

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: baseline

dispatchBaseHead: ab3854d9

Batch ID: AAF-T3

## Purpose

Authorize AAF-T3 as a bounded governance-orientation follow-up to AAF-T2. AAF-T2
reduced late gate surprises by adding helper diagnostics, but the operator
identified a higher-leverage prevention layer: future agents should be able to
read a task-first guard map before writing governed artifacts, so common guard
failures are avoided rather than repaired after the fact.

AAF-T3 creates a stable, role-neutral Guard Orientation Index that tells a new
or resumed agent what role is active, what task class is being attempted, which
guard surfaces to read first, what blocks are required, what failure pattern to
avoid, and which fast command applies. The index is documentation and routing
only; it does not change checker semantics, runtime behavior, provider behavior,
or public-sync state.

## Operator Authorization

The operator authorized AAF-T3 on 2026-06-20 and added a binding
role-neutrality constraint: orientation and work-order text should describe
roles and required work, not name a specific agent/provider/model. This avoids
fragile text that becomes stale when a single-agent or multi-agent route changes.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 AAF-T3 selection and role-neutrality constraint | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T2 closure | `docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_COMPLETION_2026-06-20.md` | ACCEPT |
| Operational reference index | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | ACCEPT |
| Startup guard router | `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md` | ACCEPT |
| Root agent instructions | `AGENTS.md` | ACCEPT |
| Guard registry guard | `governance/toolkit/05_OPERATION/CVF_GUARD_REGISTRY_GUARD.md` | ACCEPT |
| Agent handoff contract | `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md` | ACCEPT |
| Commit steward protocol | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | ACCEPT |

## Scope / Owner Boundary

Allowed scope:

- create one stable guard-orientation front door under `docs/reference/guard_orientation/`;
- update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` to route guard-orientation questions to the new front door;
- update `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md` to list the new orientation index as a startup orientation surface;
- update `AGENTS.md` with a short role-neutral instruction that future agents should read the Guard Orientation Index before material governed work;
- create one AAF-T3 worker-return review artifact;
- use role names such as operator, dispatcher, worker, reviewer, closer, and session-sync steward instead of naming a specific provider/model/agent in normative instructions.

Forbidden scope:

- no checker implementation, hook wiring, autorun phase changes, CI changes, runtime source, product UI, MCP wiring, provider/live proof, dependency install, public-sync, CodeGraph install/init, queue, watcher, daemon, or background service;
- no changes to `CVF_SESSION/ACTIVE_SESSION_STATE.json`, generated session state source files, active handoff, or session memory during worker execution;
- no automatic mutation by the index or helper;
- no direct IDE/shell/git/filesystem interception claim;
- no readiness, public release, production, universal speed, full-hook equivalence, or universal governed-coding-control claim.

Risk ceiling: R1 governance documentation and orientation.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with exactly these
owned artifacts changed or created:

- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`
- `AGENTS.md`
- `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_WORKER_RETURN_2026-06-20.md`

No other files are authorized for the worker.

## Decision / Baseline / Proposed Tranche

Baseline decision: AAF-T3 is ready for role-neutral worker dispatch as a bounded
orientation-index tranche.

Proposed tranche: `AAF-T3 Guard Orientation Index`.

Tranche owner split: the dispatch author creates the GC-018 and work order; the
worker creates the orientation index and updates allowed routing surfaces
without committing; the reviewer/closer reviews, repairs only within allowed
scope if needed, commits accepted material, and session-syncs only after
material closure.

Baseline evidence:

- Current HEAD is `ab3854d9`.
- AAF-T2 closed at material commit `904eb09a` and closure continuity commit
  `ab3854d9`.
- Existing `CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` routes work classes
  to source surfaces, but it is not a task-first guard orientation map.
- Existing `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md` lists startup guard surfaces,
  but it does not summarize what each role/task class should do first.
- Existing guard registry rules keep guard files discoverable, but they do not
  provide the compact orientation needed by a new external agent before
  authoring governed artifacts.

## Source / Predecessor Evidence

| Source | Evidence | Disposition |
|---|---|---|
| AAF-T2 closure | `docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_COMPLETION_2026-06-20.md` lines 82, 168-204 | ACCEPT |
| Operational reference index purpose and lookup rows | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` lines 9, 34, 48, 50, 54, 58, 65 | ACCEPT |
| Startup guard router surfaces | `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md` lines 7, 36, 40-41, 50-51, 54, 99 | ACCEPT |
| Guard registry discoverability rule | `governance/toolkit/05_OPERATION/CVF_GUARD_REGISTRY_GUARD.md` lines 8, 14, 18-26, 32, 47 | ACCEPT |
| Root startup and source verification requirements | `AGENTS.md` lines 30, 236, 533, 542, 567, 585 | ACCEPT |
| Handoff boundary required block | `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md` lines 35-69 | ACCEPT |

## Evidence / Verification

Dispatch author verification before this packet:

- `git status --short` was clean except the recurring Windows global git-ignore
  permission warning.
- Source verification used direct file reads and `rg -n` lookups against current
  repository files.

Required pre-dispatch verification before commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base ab3854d9 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base ab3854d9 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base ab3854d9 --head HEAD --enforce
```

## Required Orientation Index Shape

The new index must be concise and task-first. It must include at minimum:

- purpose and claim boundary;
- role-neutral role glossary;
- "read first" startup row;
- task-class map for startup/resume, work-order authoring, worker execution,
  reviewer-return review, closure, session-sync, external knowledge absorption,
  public-sync, runtime/provider/live proof, and guard/checker maintenance;
- per-row fields: task class, active role, read first, required blocks, common
  failure to avoid, fast command or gate, claim boundary;
- explicit "do not name a provider/model/agent in normative role instructions"
  rule;
- pointer back to operational reference index and startup guard router.

## Claim Boundary

AAF-T3 may claim only improved guard discoverability and earlier human/agent
orientation for governed work. It must not claim checker enforcement, automatic
governance decisioning, runtime control, provider/live behavior, public-sync
readiness, MCP execution, direct interception, production readiness, or universal
latency elimination.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py`; startup guard router |
| Owner surface | `docs/reference/guard_orientation/README.md` |
| Disposition | ADAPT as CVF-owned orientation reference |
| Claim boundary | existing CVF helpers, standards, and checkers remain source authority; the index is a navigation layer |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T3 guard-orientation documentation dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | cooperating local user/agent reads the index manually |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | orientation index, not execution-control enforcement |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain parked |

## Rescan Intelligence Hardening

- Original source artifact: operator AAF-T3 selection and AAF-T2 closure
  follow-up candidate.
- Predecessor intake artifact:
  `docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_COMPLETION_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because AAF-T3 promotes guard
  orientation from recommendation into a governed reference-index tranche.
- Routing matrix status:
  - `DO_NOW`: create role-neutral task-first guard orientation index.
  - `RESOLVED_BY_DESIGN`: keep index as documentation/routing only.
  - `SEPARATE_RUNTIME_TRANCHE`: checker implementation, CLI/MCP integration,
    watcher/daemon, provider/live, direct interception.
  - `OUT_OF_SCOPE`: public-sync, production readiness, universal control.
- Semantic sampling status: `PARTIAL_TARGETED`, limited to AAF-T2 follow-up and
  operator role-neutrality constraint.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | AAF helper remains read-only, local, and advisory. |
| CHANGED_DISPOSITION | Guard orientation moves from operator recommendation to dispatch-ready documentation tranche. |
| NEW_FINDING | Normative role instructions should avoid naming a specific agent/provider/model. |
| REMOVED_OR_REJECTED | Checker implementation, runtime, MCP, watcher, provider/live, public-sync, direct-interception scope remains rejected. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | Create orientation index and route it from startup/reference surfaces. |
| RESOLVED_BY_DESIGN | Keep orientation role-neutral and task-first. |
| SEPARATE_RUNTIME_TRANCHE | Checker implementation, helper integration, CLI/MCP integration, watcher/daemon, provider/live, direct interception. |
| STRATEGIC_OPERATOR_DECISION | Broad CGE-T3 absorption after AAF-T3 is declined or closed. |
| DEFER | Public-sync summary or public-facing guard orientation page. |
| OUT_OF_SCOPE | Production readiness, universal governed-coding-control claim. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T3-RS1 | Role-neutrality constraint | use role names, not provider/model names | DO_NOW | Could future single-agent or multi-agent routes stale the wording? | PASS_ROLE_NEUTRAL_REQUIRED |
| AAF-T3-RS2 | Required Orientation Index Shape | task-first guard map | DO_NOW | Could this become another long reference that agents skip? | PASS_CONCISE_TABLE_REQUIRED |
| AAF-T3-RS3 | Scope / Owner Boundary | documentation only | OUT_OF_SCOPE runtime | Could the index imply checker enforcement or runtime control? | PASS_BOUNDARY_EXPLICIT |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T3 is private provenance governance orientation work. Public export
requires separate public-sync authorization and a bounded public-facing summary
if the operator requests it later.

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - this is a GC-018 dispatch baseline, not a corpus inventory, folder-tree scan, or extraction report.
- Corpus root: N/A with reason - no corpus root was authorized or enumerated.
- Snapshot time: 2026-06-20 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads and `rg -n` source lookups over named AAF-T3 authority files.
- Manifest artifact or inline manifest: Authority Chain, Source / Predecessor Evidence, and Source Verification Block in the paired work order.
- Manifest hash: N/A with reason - no generated corpus manifest artifact was produced.
- Processing ledger artifact or inline ledger: inline in Evidence / Verification.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=inline; ledger_terminal=inline; exclusions=no-corpus-inventory-scope; unresolved=0
- Unresolved files: 0
- Declared exclusions: full corpus inventory, folder-tree scan, extraction report, runtime/provider proof, public-sync.
- Unreadable or unsupported files: none.
- Aggregation check: N/A with reason - no corpus aggregate was produced.
- Drift check: N/A with reason - no corpus aggregate was produced.
- Output traceability: baseline source evidence cites current repo authority files and the AAF-T3 work order carries detailed line anchors.
- Adversarial verification: claim rejects any full-corpus, complete-inventory, checker-enforcement, runtime, or public readiness assertion.
- Corpus verdict: PARTIAL
