# CVF GC-018 - INDEX-T1 Forward-Only INDEX Classification Checker

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-21

docType: gc018_baseline

dispatchBaseHead: 8ce1fd86

## Purpose

Authorize a small post-MPI-T0 checker tranche that promotes the INDEX
classification standard from packet-bound policy to machine-enforced
governance for future CVF classification artifacts and agent handoffs.

This baseline is released for worker execution after MPI-T0 and MPI-T1
reviewer closure. The accepted INDEX standard exists, the operator selected
INDEX-T1 on 2026-06-21, and implementation remains bounded to the checker
tranche described below.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-21: after MPI-T0 standard, open a small checker tranche so INDEX becomes mandatory governance without disrupting MPI roadmap | ACCEPT |
| MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` row `INDEX-T1` | ACCEPT |
| Guard orientation index | `docs/reference/guard_orientation/README.md` row `Guard / checker maintenance` | ACCEPT |
| Work order template family | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reference/work_order_template/README.md` | ACCEPT |
| Existing hook surfaces | `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` | ACCEPT |
| Existing checker pattern | `governance/compat/check_corpus_intelligence_classification.py`; existing `governance/compat/test_*.py` naming pattern | ACCEPT |
| MPI-T0 output | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | ACCEPT - created by MPI-T0 and accepted by reviewer |
| MPI-T1 completion checkpoint | `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_COMPLETION_2026-06-21.md` | ACCEPT - records operator selection of INDEX-T1 |
| Operator selection | 2026-06-21 instruction: select `INDEX-T1` work order | ACCEPT - releases this checker work order for dispatch |

## Dependency Release Gate

| Dependency | Release evidence | Current status |
|---|---|---|
| MPI-T0 INDEX standard | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md`; status `ACTIVE_FORWARD_ONLY`; material commit `24f3b958` | RELEASED |
| MPI-T0 legacy recheck | `docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_COMPLETION_2026-06-21.md`; status `CLOSED_PASS_BOUNDED`; material commit `24f3b958` | RELEASED |
| MPI-T1 operator selection evidence | `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_COMPLETION_2026-06-21.md`; status `CLOSED_PASS_BOUNDED`; next action permits INDEX-T1 selection | RELEASED |
| INDEX-T1 source verification refresh | this baseline and matching work order cite the accepted INDEX standard sections after release | RELEASED |

Worker execution is now authorized in `WORKER_MUST_NOT_COMMIT` mode. The
worker must still keep all changes within the allowed scope and return
uncommitted artifacts for reviewer closure.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | REVIEW_AND_CLASSIFY_BEFORE_ABSORPTION |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | INDEX-T1 GC-018 baseline |
| Disposition | ADAPT as released governance checker packet |
| Claim boundary | no external input is promoted as source authority; accepted MPI-T0 standard controls enforcement |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | INDEX-T1 released checker dispatch and future structural checker only |
| claimDisposition | N/A with reason: no Delta execution-control behavior is implemented or claimed |
| receiptEvidence | N/A with reason: no Delta receipt is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | worker executes after dependency release from base `8ce1fd86` or later dispatch commit |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | checker planning and future structural validation only |
| forbiddenExpansion | enforcement wrapper, proxy enforcement, interception, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, cost optimization, and universal control remain out of scope |

## Rescan Intelligence Hardening

- Original source artifact: operator INDEX checker instruction and MPI roadmap
  INDEX-T1 row.
- Predecessor intake artifact: MPI-T0 standard/recheck packet.
- Delta ledger status: NOT_APPLICABLE_WITH_REASON - INDEX-T1 does not rescan
  legacy or corpus inputs; MPI-T0 owns the bounded legacy recheck.
- Routing matrix status: COMPLETE_WITH_DECLARED_LIMITS - checker work is routed
  to a separate post-MPI-T0 governance tranche.
- Semantic sampling status: NOT_APPLICABLE_WITH_REASON - future checker tests
  sample structural failures only; no corpus semantic sampling is authorized.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | MPI-T0 remains the legacy recheck and INDEX standard authoring tranche. |
| CHANGED_DISPOSITION | INDEX machine enforcement moved to separate INDEX-T1 checker tranche. |
| NEW_FINDING | No new rescan finding; this is a governance enforcement staging packet. |
| REMOVED_OR_REJECTED | Direct checker implementation inside MPI-T0 is rejected. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | Dispatch the released INDEX-T1 baseline/work order to a worker. |
| SEPARATE_RUNTIME_TRANCHE | Runtime Memory, vector, graph, adapter, provider/live, and public-sync work remain out of scope. |
| STRATEGIC_OPERATOR_DECISION | SATISFIED - operator selected INDEX-T1 from the MPI-T1 completion checkpoint. |
| OUT_OF_SCOPE | Legacy rescan, direct runtime promotion, public claim, and universal-control claims. |
| RESOLVED_BY_DESIGN | Keep INDEX standard authoring and checker enforcement as separate tranches. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| INDEX-T1-RS1 | Dependency Release Gate | MPI-T0 must close before checker implementation | RELEASED | Could checker work bypass the missing standard? | PASS - release evidence recorded |
| INDEX-T1-RS2 | Scope / Owner Boundary | checker scope is governance-only | RESOLVED_BY_DESIGN | Could this become runtime Memory work? | PASS - runtime and generated paths forbidden |

## Scope / Owner Boundary

Allowed worker scope:

- create `governance/compat/check_index_classification.py`;
- create `governance/compat/test_check_index_classification.py`;
- update `governance/compat/run_agent_autorun_workflow_gate.py`;
- update `governance/compat/run_local_governance_hook_chain.py`;
- update `docs/reference/guard_orientation/README.md`;
- update `docs/reference/work_order_template/README.md`;
- create `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_WORKER_RETURN_2026-06-21.md`.

Forbidden worker scope:

- no edits to Memory runtime, runtime extension paths, generated JSON aggregates, scan
  registry entries or aggregate, active session state, active handoff,
  public-sync, MCP packages, dependency manifests, `.github/**`, provider/live
  proof, vector DB, embedding store, graph persistence, CLI/MCP adapter
  behavior, queue, daemon, watcher, wrapper/proxy enforcement, direct IDE/shell
  interception, arbitrary command execution, or EDIT/COMMIT execution;
- no legacy rescan, KGR expansion, MPI-T1/T2/T3/T4 implementation, LSC ledger,
  durable store, runtime Learning Plane mutation, public claim, or historical
  CVF rewrite.

Risk ceiling: R1 governance checker/source-test tranche only.

## Core Guard Self-Protection Authorization

| Field | Disposition |
|---|---|
| Protected paths authorized | `governance/compat/check_index_classification.py`; `governance/compat/test_check_index_classification.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Authorization source | operator instruction to create post-MPI-T0 checker tranche; this GC-018 baseline; matching work order |
| Authorized scope | add deterministic INDEX classification checker, focused tests, and narrow hook/autorun wiring after dependency release |
| Rollback boundary | revert only INDEX-T1 checker/test/wiring/template/reference edits if checker gate fails or exceeds scope |
| Not authorized | runtime Memory changes, provider/live proof, public-sync, external dependency adoption, adapter behavior, generated aggregate edits, session-sync, or retroactive rewrite |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| INDEX-T1 is a planned follow-up checker tranche | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | Tranche Plan | `INDEX-T1` | MPI roadmap | VALUE_SET | ACCEPT |
| INDEX standard is active and forward-only | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | Status; Purpose; Forward-Only Application Rules | `ACTIVE_FORWARD_ONLY`; `INDEX-T1` | INDEX standard | VALUE_SET | ACCEPT |
| MPI-T1 closure permits operator selection of INDEX-T1 | `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_COMPLETION_2026-06-21.md` | Current Position; Next Move Handoff | `INDEX-T1` | MPI-T1 completion review | VALUE_SET | ACCEPT |
| Guard/checker maintenance requires protected-path authorization | `docs/reference/guard_orientation/README.md` | Task Class Guard Map | `Guard / checker maintenance` | Guard orientation index | VALUE_SET | ACCEPT |
| Work order authoring requires source verification | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Enforcement / Verification | Source Verification Block | Work order template | VALUE_SET | ACCEPT |
| Work order template family README is the stable folder index | `docs/reference/work_order_template/README.md` | Canonical Template; Addenda In This Folder | `docs/reference/work_order_template/README.md` | Work order template family | EXISTS | ACCEPT |
| Autorun gate has common command wiring surface | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `GateCommand` | Autorun workflow gate | EXISTS | ACCEPT |
| Local hook chain has hook wiring surface | `governance/compat/run_local_governance_hook_chain.py` | `HOOK_CHAINS` | `reviewer-fast`; `pre-commit`; `pre-push` | Local governance hook chain | EXISTS | ACCEPT |
| INDEX standard exists and names required metadata | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | Required Metadata Per INDEX Artifact | `INDEX type`; `Source authority`; `Status`; `Date`; `Human-reviewable`; `Claim boundary`; `Public Export Disposition` | INDEX standard | VALUE_SET | ACCEPT |

## Negative Search And Collision Discipline

Search roots: `docs`; `governance`.

Search command / query:
`rg -n "CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21|check_index_classification|test_check_index_classification" docs governance --glob !docs/baselines/CVF_GC018_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md --glob !docs/work_orders/CVF_WO_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md`

Coverage: source, tests, docs, JSON, and external-evidence-bearing governed
artifacts under the searched roots.

| Check | Command or evidence | Result | Collision / disposition |
|---|---|---|---|
| INDEX standard present | `Test-Path docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | `True` | released for INDEX-T1 worker dispatch |
| INDEX checker not yet present | `Test-Path governance/compat/check_index_classification.py` | `False` | new file is in allowed worker scope |
| INDEX checker tests not yet present | `Test-Path governance/compat/test_check_index_classification.py` | `False` | new file is in allowed worker scope |
| `EXISTS` same-token collision occurrence | source-verification vocabulary appears elsewhere | non-authoritative collision | not binding for the missing INDEX standard/checker files |
| `INDEX` same-token collision occurrence | planning and MPI-T0 references appear elsewhere | non-authoritative collision | not binding as existing standard/checker implementation |
| `MPI` same-token collision occurrence | roadmap and tranche vocabulary appears elsewhere | non-authoritative collision | not binding as INDEX-T1 dependency release evidence |
| Existing mentions are planning/dependency references | exact search command above | hits only in MPI-T0/roadmap planning references and existing corpus checker references | no collision with existing INDEX checker |

## Proposed Tranche

Tranche ID: `INDEX-T1`

Name: `Forward-Only INDEX Classification Checker`

Dependency status: `RELEASED_FOR_WORKER`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Primary worker return:

- `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_WORKER_RETURN_2026-06-21.md`

## Required Future Checks

Worker must run:

```powershell
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_check_index_classification
python governance/compat/check_index_classification.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_index_classification.py
```

Reviewer/closer may add stricter pre-closure and commit steward gates after the
worker return is accepted.

## Evidence / Verification

| Evidence item | Required command or artifact | Status |
|---|---|---|
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 8ce1fd86 --head HEAD --enforce` | required for dispatch packet |
| Core guard authorization | `python governance/compat/check_core_guard_self_protection.py --base 8ce1fd86 --head HEAD --enforce` | required for protected-path authorization |
| Pre-dispatch autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 8ce1fd86 --head HEAD` | required before claiming packet-ready |
| Worker checks | commands listed in Required Future Checks | required after worker implementation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance checker planning. No public-sync,
public-facing claim, or public repository mutation is authorized.

## Claim Boundary

This GC-018 baseline authorizes only the released INDEX-T1 checker tranche. It
does not claim that INDEX is already machine-enforced, and does not authorize
runtime Memory, legacy rescan, provider/live, public-sync, CLI/MCP adapter,
vector DB, graph persistence, interception, queue, daemon, watcher, or
universal governed-coding control.
