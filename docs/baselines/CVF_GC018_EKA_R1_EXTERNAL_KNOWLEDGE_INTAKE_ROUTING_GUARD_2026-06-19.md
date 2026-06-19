# CVF GC-018 - EKA-R1 External Knowledge Intake Routing Guard

Memory class: FULL_RECORD

Status: DISPATCH_READY

Owner: Codex Orchestrator

Worker target: Codex

Commit mode: WORKER_MAY_COMMIT

rawMemoryReleased=false

Base head: `84e9d190`

dispatchBaseHead: `84e9d190`

executionBaseHead: `84e9d190`

closureBaseHead: `84e9d190`

Material commit: `PENDING_COMMIT`

## Dispatch Prompt Envelope

Read this packet first. Implement only EKA-R1: a bounded range-aware external
knowledge intake routing guard that makes changed governed intake artifacts
cite the chain map, identify input type, and name the matching local-view guard
or bounded N/A reason. Do not implement broad external absorption, import raw
external repos, run providers, public-sync, mutate runtime behavior, or claim
universal interception.

## Purpose

Convert the external knowledge absorption chain-map checker candidate into a
small machine guard. The guard should make future external/repo/legacy/corpus
intake packets route through the Central Core chain map before they proceed to
work-order, runtime, or governance claims.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | Dispatch EKA-R1 bounded routing guard now |
| Proposed tranche | EKA-R1 External Knowledge Intake Routing Guard T1 |
| Base head | `84e9d190` |
| Worker | Codex |
| Commit route | `WORKER_MAY_COMMIT` |
| Upstream evidence | `docs/reviews/CVF_POST_DELTA_T3_NEXT_FOUNDATION_TRANCHE_SELECTION_2026-06-19.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Next sequence | Reassess next foundation candidate after EKA-R1 closes; Delta-T4 remains parked |

## Scope / Target / Owner Boundary

Allowed source paths:

- `governance/compat/check_external_knowledge_intake_routing.py`;
- `governance/compat/test_check_external_knowledge_intake_routing.py`;
- `governance/compat/run_local_governance_hook_chain.py`;
- `governance/compat/run_agent_autorun_workflow_gate.py`;
- `governance/compat/test_run_local_governance_hook_chain.py`;
- `docs/baselines/CVF_GC018_EKA_R1_EXTERNAL_KNOWLEDGE_INTAKE_ROUTING_GUARD_2026-06-19.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_EKA_R1_EXTERNAL_KNOWLEDGE_INTAKE_ROUTING_GUARD_FOR_CODEX_2026-06-19.md`;
- `docs/reviews/CVF_EKA_R1_EXTERNAL_KNOWLEDGE_INTAKE_ROUTING_GUARD_COMPLETION_2026-06-19.md`;
- `docs/reviews/evidence/eka-r1-external-knowledge-intake-routing-guard-2026-06-19.json`.

Forbidden scope:

- no external repo/folder import or broad legacy scan;
- no corpus registry content expansion;
- no provider/live call, secrets/quota use, or public-sync;
- no runtime, MCP, queue, scheduler, daemon, wrapper, shell, IDE, git, or file
  interception;
- no Delta-T4 approval-backed mutation work;
- no readiness, public, production, release, or universal governed-coding
  claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Chain map requires external knowledge intake to identify input type before routing. | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Mandatory Chain` | `Identify input type` | external knowledge chain map | ACCEPT |
| Chain map defines the input type router for legacy, external repo, external-agent, public vocabulary, corpus, and runtime/MCP claims. | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Input Type Router` | `Input type` | external knowledge chain map | ACCEPT |
| Chain map records partial enforcement and the need to use the most specific existing local-view guard. | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Enforcement Gap` | `most specific existing guard` | external knowledge chain map | ACCEPT |
| Chain map explicitly names a future checker for changed external knowledge intake artifacts. | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Machine-Check Candidate` | `changed external knowledge intake artifacts cite this chain map` | external knowledge chain map | ACCEPT |
| Returned external-agent output already has a local-view Required Absorption Table guard. | `governance/compat/check_external_agent_absorption_table.py` | module constants and `check_text` | `REQUIRED_SECTION`; `check_text` | external-agent absorption table guard | ACCEPT |
| Local hook chain already wires the returned-output guard into reviewer-fast, pre-commit, and pre-push. | `governance/compat/run_local_governance_hook_chain.py` | `REVIEWER_FAST_CHECKS`; `HOOK_CHAINS` | `external-agent absorption table` | local governance hook chain | ACCEPT |
| Autorun common commands already wire the returned-output guard into phase gates. | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `external-agent absorption table` | autorun workflow gate | ACCEPT |
| Work orders that name source/runtime fields require source verification. | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | `Source Verification Block` | `Claimed item`; `Disposition` | work-order template | ACCEPT |

## External Knowledge Intake Routing

External knowledge intake routing: REQUIRED

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Operator-provided external comparison, critique, or recommendation |
| Chain map route | `Mandatory Chain` plus `Machine-Check Candidate` |
| Matching local-view guard | `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_rescan_intelligence_hardening.py` |
| Owner surface | New EKA-R1 guard under `governance/compat/` |
| Disposition | `ADAPT` into bounded routing guard |
| Claim boundary | This routing block does not prove broad external absorption, runtime enforcement, public readiness, or universal interception |

## Guard Design Control Block

| Field | Disposition |
| --- | --- |
| Guard name | `check_external_knowledge_intake_routing.py` |
| Guard style | range-aware, forward-only, changed-file scoped |
| Trigger | changed governed Markdown intake artifacts with explicit marker or external/legacy/corpus intake path markers |
| Required section | `## External Knowledge Intake Routing` |
| Required evidence | chain map citation; input type; chain map route; matching local-view guard or `N/A with reason`; owner surface; disposition; claim boundary |
| Composition rule | compose existing local-view guards; do not duplicate absorption-table, corpus, legacy, dispatch-quality, or autorun logic |
| Enforcement placement | reviewer-fast, pre-commit, pre-push, and autorun common phase gates |
| Bypass boundary | no universal filesystem/runtime/tool interception claim |

## Rescan Intelligence Hardening

- Original source artifact:
  `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.
- Predecessor intake artifact:
  `docs/reviews/CVF_POST_DELTA_T3_NEXT_FOUNDATION_TRANCHE_SELECTION_2026-06-19.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because EKA-R1 moves from
  recommended candidate into dispatch-ready machine-check work.
- Routing matrix status:
  - `DO_NOW`: implement bounded external knowledge intake routing guard.
  - `RESOLVED_BY_DESIGN`: compose the returned-output absorption table guard
    instead of duplicating it.
  - `SEPARATE_RUNTIME_TRANCHE`: any runtime/provider/MCP behavior proof,
    wrapper/proxy control, or broad interception work.
  - `STRATEGIC_OPERATOR_DECISION`: Delta-T4 mutation/interception breadth and
    future universal router scope.
  - `OUT_OF_SCOPE`: broad legacy rescan, corpus expansion, raw external
    package import, provider/live proof, public-sync, and readiness claims.
- Semantic sampling status: `PARTIAL_TARGETED`, limited to the chain-map
  machine-check candidate and existing local-view guard wiring.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE
- Machine guard: `governance/compat/check_rescan_intelligence_hardening.py`

### Original-Intake Delta Ledger

| Item | Delta category | Original disposition | Updated disposition | Rationale |
| --- | --- | --- | --- | --- |
| EKA-R1 routing guard | `CHANGED_DISPOSITION` | recommended candidate | `DISPATCH_READY` | operator authorized this tranche |
| Guard implementation artifact | `NEW_FINDING` | no EKA-R1 checker existed | new checker required | selected machine-check candidate needs a local-view guard |
| External-agent absorption table guard | `UNCHANGED_FROM_INTAKE` | existing local-view guard | compose, do not duplicate | EKA-R1 routes to it when applicable |
| Broad external absorption router | `REMOVED_OR_REJECTED` | known future gap | parked | this tranche is bounded to changed artifacts |
| Delta-T4 mutation/interception | `UNCHANGED_FROM_INTAKE` | parked | parked | outside EKA-R1 |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
| --- | --- | --- |
| DO_NOW | EKA-R1 routing guard | this dispatch opens the checker |
| RESOLVED_BY_DESIGN | returned-output absorption-table enforcement | existing guard remains owner |
| SEPARATE_RUNTIME_TRANCHE | runtime/provider/MCP behavior proof, wrapper/proxy control, and broad interception | requires separate authorization |
| STRATEGIC_OPERATOR_DECISION | Delta-T4 mutation/interception breadth and future universal router scope | operator checkpoint required |
| OUT_OF_SCOPE | broad legacy scan, corpus expansion, raw external repo import, provider/live proof, public-sync, and readiness claims | outside scope |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| EKA-R1-01 | Chain map `Machine-Check Candidate` | changed intake artifacts cite chain map | `CHANGED_DISPOSITION` | Could this imply universal router? | PASS_BOUNDARY |
| EKA-R1-02 | Chain map `Enforcement Gap` | use most specific local-view guard | `UNCHANGED_FROM_INTAKE` | Could EKA-R1 duplicate existing guards? | PASS_COMPOSES |
| EKA-R1-03 | Chain map `Input Type Router` | input type must be identified | `CHANGED_DISPOSITION` | Could a generic external note skip routing? | PASS_CHECKER_TARGET |

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex orchestrator/worker/reviewer/closer in one bounded tranche |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE |
| baseHeadFor(phase) | dispatch=`84e9d190`; execution=`84e9d190`; closure=`84e9d190` |
| changedSetScope(phase) | checker, tests, hook wiring, GC-018, work order, completion review, evidence JSON |
| traceScope(phase, actor) | Codex owns dispatch, execution, and closure trace for this material batch |
| commitOwner(phase) | Codex |
| crossBatchIsolation | No session-sync in material commit; no public-sync; no runtime/provider/live scope |
| nextMoveSurfaces | Session-sync after material closure records EKA-R1 closure and next candidate |
| closerDesignation | Codex is the closer |

## Acceptance Criteria

| ID | Criterion | Status |
| --- | --- | --- |
| AC1 | Add range-aware checker requiring changed external knowledge intake artifacts to cite the chain map. | OPEN |
| AC2 | Checker requires `## External Knowledge Intake Routing` with input type and chain-map route. | OPEN |
| AC3 | Checker requires matching local-view guard evidence or bounded `N/A with reason`. | OPEN |
| AC4 | Checker ignores unrelated changed Markdown and archived artifacts. | OPEN |
| AC5 | Focused checker tests cover pass/fail/ignore cases. | OPEN |
| AC6 | Reviewer-fast, pre-commit, pre-push, and autorun phase gates include the checker. | OPEN |

## Evidence / Verification Requirements

| Gate | Command | Required result |
| --- | --- | --- |
| Focused test | `python -m pytest governance/compat/test_check_external_knowledge_intake_routing.py governance/compat/test_run_local_governance_hook_chain.py` | PASS |
| Checker smoke | `python governance/compat/check_external_knowledge_intake_routing.py --base 84e9d190 --head HEAD --enforce` | PASS |
| Worker fast gate | `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_external_knowledge_intake_routing.py` | PASS |
| Pre-closure autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <implementationBase> --head HEAD` | PASS after material commit |
| Pre-push autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-push --base <implementationBase> --head HEAD` | PASS after material commit |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance guard hardening. Public-sync is not authorized.

## Claim Boundary

This GC-018 authorizes only a changed-file routing guard for governed external
knowledge intake artifacts. It does not prove complete legacy absorption,
external repo absorption, runtime behavior, provider governance, MCP execution
control, durable action audit, wrapper/proxy control, public readiness, or
universal bypass prevention.
