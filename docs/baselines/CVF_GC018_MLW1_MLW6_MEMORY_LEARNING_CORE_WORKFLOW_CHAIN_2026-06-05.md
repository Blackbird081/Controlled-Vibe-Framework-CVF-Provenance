# CVF GC-018 - MLW1-MLW6 Memory Learning Core Workflow Chain

Memory class: FULL_RECORD

Status: AUTHORIZED_DISPATCH_PACKET

docType: gc018_baseline

Date: 2026-06-05

dispatchBaseHead: `9c523807`

## Purpose

Authorize a bounded MLW1-MLW6 contract wave after MLW0 closed the current
source verification prerequisite.

This baseline authorizes source-verified contract and workflow-chain artifacts
for the six core Memory/Learning Workflow tranches. It does not authorize
runtime mutation, backend selection, public-sync, live provider proof, hosted
readiness, production readiness, public readiness, or autonomous learning.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-05 operator authorized Codex to self-audit, close roles, and proceed through MLW1-MLW6 | ACCEPT |
| MLW0 source map | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` status `CLOSED_PASS_BOUNDED` | ACCEPT |
| MLW0 completion | `docs/reviews/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_COMPLETION_2026-06-05.md` | ACCEPT |
| CI1-T11 roadmap | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | ACCEPT |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` current mode `mlw0_current_source_verification_map_closed_pass_bounded` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` records MLW0 closure head | ACCEPT |

## Source / Predecessor Evidence

| Predecessor | Evidence | MLW1-MLW6 dependency |
| --- | --- | --- |
| MLW0 source map | Current owner surface and legacy concept verification tables | provides source-backed symbols and blocked legacy names |
| T11A packet | `docs/audits/CVF_CI1_T11A_LEARNING_PLANE_DEEP_SCAN_PACKET_2026-06-05.md` | truth, evaluation, reputation, adaptation, simulation |
| T11B packet | `docs/audits/CVF_CI1_T11B_MEMORY_KNOWLEDGE_STORE_DEEP_SCAN_PACKET_2026-06-05.md` | memory gateway, lifecycle, privacy, provenance |
| T11C packet | `docs/audits/CVF_CI1_T11C_RAG_CONTEXT_CONTROL_DEEP_SCAN_PACKET_2026-06-05.md` | context bundle, router, fusion, budget, cache boundary |
| T11D packet | `docs/audits/CVF_CI1_T11D_EXECUTION_AUDIT_LEARNING_DEEP_SCAN_PACKET_2026-06-05.md` | continuity, handoff, audit feedback, planner trace |
| T10 packet | `docs/audits/CVF_CI1_T10_CORTEX_HUB_MEMORY_LEARNING_DEEP_SCAN_PACKET_2026-06-05.md` | external memory/MCP/provider boundary input only |

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZE_MLW1_MLW6_CONTRACT_WAVE_ONLY

Risk ceiling: R1.

The wave may create source-verified contract documents, workflow-chain models,
failure cases, checker/test plans, closure review, registry entry, and session
continuity. It may not modify runtime TypeScript/Python source, routes, tests,
package files, public-sync, or provider/live proof surfaces.

## Scope

Allowed:

- author one work order for MLW1-MLW6 core contract closure;
- author one reference artifact per tranche MLW1 through MLW6;
- update the CI1-T11 roadmap from roadmap-ready to bounded core-chain closed;
- update GC-051 registry with a project-source planning/contract entry;
- author one completion review;
- update active session state, session memory, and active handoff;
- run local governance and autorun gates.

Forbidden:

- runtime memory writes or durable backend implementation;
- choosing SQLite, Postgres, Redis, vector store, or any production backend;
- route changes, package/lockfile changes, test file changes, or checker code;
- live provider calls or mandatory release gate claims;
- public-sync or public README/catalog claims;
- autonomous policy, prompt, provider, memory, or learning mutation;
- MLW7/MLW8 scope.

## Worker Autonomy / No-Question Rule

Codex must repair allowed-scope governance gate failures without escalating to
the operator. Escalate only for runtime implementation, public-sync, live proof,
secrets/quota, destructive actions, MLW7/MLW8 expansion, or claim-boundary
changes beyond contract closure.

## Exit Criteria

MLW1-MLW6 core wave is closed when:

1. Six tranche reference artifacts exist and cite MLW0 source facts.
2. Each artifact contains new doc-only fields separated from current source
   verification.
3. The work order and completion review include Machine Closure Package,
   Finding-To-Governance Learning Disposition, and Public Export Disposition.
4. The CI1-T11 roadmap records MLW1-MLW6 as bounded contract-closed.
5. Session continuity is updated.
6. Pre-closure and pre-push autorun gates pass on the full changed range.

## Evidence / Verification

Required verification:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 9c523807 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 9c523807 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 9c523807 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-push --base 9c523807 --head HEAD
```

## Corpus Completeness And Report Integrity

- Corpus task class: GC-018_DISPATCH_BASELINE_CONTRACT_WAVE.
- Corpus root: `docs/reference/` plus `docs/roadmaps/` source packets named in this baseline.
- Snapshot time: 2026-06-05.
- Enumeration command: `rg --files --hidden --no-ignore docs/reference docs/roadmaps docs/audits`.
- Manifest artifact or inline manifest: inline scope paths in this baseline and registry entry `mlw1-mlw6-core-workflow-chain`.
- Manifest hash: `5305c7a18f61607d211b02c324c31f1140051e320073f12e5ef701977d125b4a`.
- Processing ledger artifact or inline ledger: work order execution plan plus completion review Roadmap-To-Work-Order Trace Matrix.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=7; ledger_terminal=7; exclusions=4; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: runtime source mutation, public-sync, live proof, MLW7/MLW8.
- Unreadable or unsupported files: none.
- Aggregation check: PASS - six MLW1-MLW6 tranches plus MLW0 source map accounted for.
- Drift check: PASS at dispatchBaseHead `9c523807`.
- Output traceability: `docs/work_orders/CVF_WO_MLW1_MLW6_MEMORY_LEARNING_CORE_WORKFLOW_CHAIN_2026-06-05.md`.
- Adversarial verification: reviewer must sample each tranche against MLW0 blocked/renamed rows and reject legacy runtime field claims.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Claim Boundary

This baseline authorizes bounded contract and workflow-chain closure only. It
does not prove runtime behavior, live governance behavior, durable distributed
storage, production readiness, hosted readiness, public readiness, or autonomous
learning safety.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the wave derives from private legacy scan packets and private
provenance source verification. Public-facing memory/learning claims require a
separate public-safe summary and public-sync authorization.
