# CVF GC-018 - INDEX-T1 Forward-Only INDEX Classification Checker

Memory class: FULL_RECORD

Status: HOLD_UNTIL_MPI_T0_CLOSURE

Date: 2026-06-21

docType: gc018_baseline

dispatchBaseHead: acb2b980

## Purpose

Authorize a small post-MPI-T0 checker tranche that promotes the INDEX
classification standard from packet-bound policy to machine-enforced
governance for future CVF classification artifacts and agent handoffs.

This baseline is dependency-held. It must not be dispatched until MPI-T0 closes
with an accepted `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md`
and reviewer evidence that the standard is ready for enforcement.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-21: after MPI-T0 standard, open a small checker tranche so INDEX becomes mandatory governance without disrupting MPI roadmap | ACCEPT |
| MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` row `INDEX-T1` | ACCEPT |
| Guard orientation index | `docs/reference/guard_orientation/README.md` row `Guard / checker maintenance` | ACCEPT |
| Work order template family | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reference/work_order_template/README.md` | ACCEPT |
| Existing hook surfaces | `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` | ACCEPT |
| Existing checker pattern | `governance/compat/check_corpus_intelligence_classification.py`; existing `governance/compat/test_*.py` naming pattern | ACCEPT |
| MPI-T0 output | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | ACCEPT - created by MPI-T0 and accepted by reviewer; INDEX-T1 remains parked for operator selection |

## Dependency Hold

| Dependency | Required release evidence | Current status |
|---|---|---|
| MPI-T0 INDEX standard | accepted `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` and MPI-T0 completion review | HOLD |
| MPI-T0 legacy recheck | accepted `docs/reviews/CVF_MPI_T0_INDEX_LEGACY_MEMORY_GRAPH_RECHECK_WORKER_RETURN_2026-06-21.md` and reviewer closure | HOLD |
| INDEX-T1 source verification refresh | work order updated after MPI-T0 closure to cite the actual standard sections | HOLD |

No worker may implement INDEX-T1 until these rows are refreshed from `HOLD` to
released evidence with artifact path, closure disposition, and base-head.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | REVIEW_AND_CLASSIFY_BEFORE_ABSORPTION |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | INDEX-T1 GC-018 baseline |
| Disposition | ADAPT as dependency-held governance checker packet |
| Claim boundary | no external input is promoted as source authority; MPI-T0 standard must be accepted first |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | INDEX-T1 dependency-held checker planning only |
| claimDisposition | N/A with reason: no Delta execution-control behavior is implemented or claimed |
| receiptEvidence | N/A with reason: no Delta receipt is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | future worker executes only after MPI-T0 dependency release |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | checker planning and future structural validation only |
| forbiddenExpansion | enforcement wrapper, proxy enforcement, interception, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, cost optimization, and universal control remain out of scope |

## Rescan Intelligence Hardening

- Original source artifact: operator INDEX checker instruction and MPI roadmap
  INDEX-T1 row.
- Predecessor intake artifact: MPI-T0 held standard/recheck packet.
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
| DO_NOW | Create dependency-held INDEX-T1 baseline/work order only. |
| SEPARATE_RUNTIME_TRANCHE | Runtime Memory, vector, graph, adapter, provider/live, and public-sync work remain out of scope. |
| STRATEGIC_OPERATOR_DECISION | Operator decides after MPI-T0 whether to release INDEX-T1 before MPI-T1. |
| OUT_OF_SCOPE | Legacy rescan, direct runtime promotion, public claim, and universal-control claims. |
| RESOLVED_BY_DESIGN | Keep INDEX standard authoring and checker enforcement as separate tranches. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| INDEX-T1-RS1 | Dependency Hold | MPI-T0 must close before checker implementation | HOLD | Could checker work bypass the missing standard? | PASS - dependency release required |
| INDEX-T1-RS2 | Scope / Owner Boundary | checker scope is governance-only | RESOLVED_BY_DESIGN | Could this become runtime Memory work? | PASS - runtime and generated paths forbidden |

## Scope / Owner Boundary

Allowed future worker scope after dependency release:

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

Risk ceiling after release: R1 governance checker/source-test tranche only.

## Core Guard Self-Protection Authorization

| Field | Disposition |
|---|---|
| Protected paths authorized | `governance/compat/check_index_classification.py`; `governance/compat/test_check_index_classification.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Authorization source | operator instruction to create post-MPI-T0 checker tranche; this GC-018 baseline; matching work order |
| Authorized scope | add deterministic INDEX classification checker, focused tests, and narrow hook/autorun wiring after MPI-T0 dependency release |
| Rollback boundary | revert only INDEX-T1 checker/test/wiring/template/reference edits if checker gate fails or exceeds scope |
| Not authorized | runtime Memory changes, provider/live proof, public-sync, external dependency adoption, adapter behavior, generated aggregate edits, session-sync, or retroactive rewrite |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| INDEX-T1 is a planned follow-up checker tranche | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | Tranche Plan | `INDEX-T1` | MPI roadmap | VALUE_SET | ACCEPT |
| MPI-T0 must precede checker enforcement | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | INDEX Standard; Work Plan | `MPI-T0`; `INDEX-T1` | MPI roadmap | VALUE_SET | ACCEPT |
| Guard/checker maintenance requires protected-path authorization | `docs/reference/guard_orientation/README.md` | Task Class Guard Map | `Guard / checker maintenance` | Guard orientation index | VALUE_SET | ACCEPT |
| Work order authoring requires source verification | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Enforcement / Verification | Source Verification Block | Work order template | VALUE_SET | ACCEPT |
| Work order template family README is the stable folder index | `docs/reference/work_order_template/README.md` | Canonical Template; Addenda In This Folder | `docs/reference/work_order_template/README.md` | Work order template family | EXISTS | ACCEPT |
| Autorun gate has common command wiring surface | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `GateCommand` | Autorun workflow gate | EXISTS | ACCEPT |
| Local hook chain has hook wiring surface | `governance/compat/run_local_governance_hook_chain.py` | `HOOK_CHAINS` | `reviewer-fast`; `pre-commit`; `pre-push` | Local governance hook chain | EXISTS | ACCEPT |
| INDEX standard exists and names enforced fields | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | created by MPI-T0 and accepted by reviewer | `CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | INDEX standard | EXISTS | ACCEPT |

## Negative Search And Collision Discipline

Search roots: `docs`; `governance`.

Search command / query:
`rg -n "CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21|check_index_classification|test_check_index_classification" docs governance --glob !docs/baselines/CVF_GC018_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md --glob !docs/work_orders/CVF_WO_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_2026-06-21.md`

Coverage: source, tests, docs, JSON, and external-evidence-bearing governed
artifacts under the searched roots.

| Check | Command or evidence | Result | Collision / disposition |
|---|---|---|---|
| INDEX standard present after MPI-T0 closure | `Test-Path docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | `True` | execution remains parked until operator selects INDEX-T1 |
| INDEX checker not yet present | `Test-Path governance/compat/check_index_classification.py` | `False` | new file allowed only after dependency release |
| INDEX checker tests not yet present | `Test-Path governance/compat/test_check_index_classification.py` | `False` | new file allowed only after dependency release |
| `EXISTS` same-token collision occurrence | source-verification vocabulary appears elsewhere | non-authoritative collision | not binding for the missing INDEX standard/checker files |
| `INDEX` same-token collision occurrence | planning and MPI-T0 references appear elsewhere | non-authoritative collision | not binding as existing standard/checker implementation |
| `MPI` same-token collision occurrence | roadmap and tranche vocabulary appears elsewhere | non-authoritative collision | not binding as INDEX-T1 dependency release evidence |
| Existing mentions are planning/dependency references | exact search command above | hits only in MPI-T0/roadmap planning references and existing corpus checker references | no collision with existing INDEX checker |

## Proposed Tranche

Tranche ID: `INDEX-T1`

Name: `Forward-Only INDEX Classification Checker`

Dependency status: `HOLD_UNTIL_MPI_T0_CLOSURE`

Commit mode after release: `WORKER_MUST_NOT_COMMIT`

Primary worker return:

- `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_WORKER_RETURN_2026-06-21.md`

## Required Future Checks

After dependency release and worker implementation:

```powershell
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_check_index_classification
python governance/compat/check_index_classification.py --base <releasedBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_index_classification.py
```

Reviewer/closer may add stricter pre-closure and commit steward gates after the
worker return is accepted.

## Evidence / Verification

| Evidence item | Required command or artifact | Status |
|---|---|---|
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base acb2b980 --head HEAD --enforce` | required for held packet |
| Core guard authorization | `python governance/compat/check_core_guard_self_protection.py --base acb2b980 --head HEAD --enforce` | required for protected-path authorization |
| Pre-dispatch autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base acb2b980 --head HEAD` | required before claiming packet-ready |
| Future worker checks | commands listed in Required Future Checks | HOLD until MPI-T0 closure |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance checker planning. No public-sync,
public-facing claim, or public repository mutation is authorized.

## Claim Boundary

This GC-018 baseline authorizes only a dependency-held future checker tranche.
It does not claim that INDEX is currently machine-enforced, does not dispatch
implementation before MPI-T0 closure, and does not authorize runtime Memory,
legacy rescan, provider/live, public-sync, CLI/MCP adapter, vector DB, graph
persistence, interception, queue, daemon, watcher, or universal governed-coding
control.
