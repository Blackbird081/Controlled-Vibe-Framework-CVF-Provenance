# CVF Agent Instructions

Root instruction carrier and canonical CVF authority. This is a compact router
carrying the startup contract, authority hierarchy, task-class routing, and
direct machine bindings. The full per-rule owner map lives in the routing index
`docs/reference/CVF_AGENT_INSTRUCTION_CARRIER_ROUTING_INDEX_2026-08-11.md`.
Compaction moved prose there and repealed no rule; if a rule is not restated
here, resolve its canonical owner through that index.

## Session Memory Front Door

The active session front door for new or resumed agents is:

`CVF_SESSION_MEMORY.md`

Read continuity surfaces progressively, not the full state/history aggregate
by default: (1) read the bootstrap read model first for compact current facts
(current mode, active handoff, next allowed move):

`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

(2) read the compact front door above and the current active handoff named by
the state registry; (3) read only the current-authority paths those two
surfaces name for the current task; (4) resolve the full machine-readable
state registry only as a targeted lookup, when a current fact is missing,
contradictory, or the task explicitly requires historical evidence:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Canonical standard for these budgets and their exact-hash migration debt:
`docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md`.
Machine guard: `governance/compat/check_active_session_state.py`. Some current
Core surfaces still exceed the canonical budgets in that standard as
exact-hash tracked migration debt in
`governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`; that
debt cannot grow and does not license reading full history by default.

The current active handoff in that registry is:

`AGENT_HANDOFF_V59_2026-08-11.md`

Historical handoffs are archived under:

`CVF_SESSION/handoffs/archive/`

Do not append new status to archived handoffs; update the active handoff named
by `CVF_SESSION/ACTIVE_SESSION_STATE.json`, or open a later versioned handoff
when the active one approaches its limit. Startup front doors and routing docs
must reference only the active handoff by bare filename; superseded handoffs
may appear only as archive-qualified paths.

## Mandatory Startup Acknowledgment

Before material governed work in any new or resumed session, read
`CVF_SESSION_MEMORY.md` and its bootstrap read model, identify the active
handoff those surfaces name, and resolve the full state registry only as a
targeted lookup when a current fact is missing or contradictory. Then state to
the operator, or record in the active handoff/session state, one concise
acknowledgment naming current mode, active handoff, next allowed move, and any
parked operator checkpoint. Suggested format:

`Startup acknowledged: current mode=<mode>; active handoff=<handoff>; next allowed move=<summary>; parked checkpoint=<none|summary>.`

This is a soft-accountability requirement, not proof of runtime auto-load,
universal tool support, MCP availability, or hidden cross-agent memory
transfer. Trivial direct answers may keep the confirmation internal, but any
roadmap, implementation, review, live run, commit, handoff, or public-sync
work must satisfy it first.

When the operator asks to create or refresh a local CVF Workspace from a fresh
provenance clone, use `Initialize-CVF-Operator-Workspace.ps1` as the autorun
entrypoint and preserve interactive profile selection unless the operator has
already selected an exact path and profile.

## Authority Hierarchy

1. `ECOSYSTEM/doctrine/` - frozen supreme governance.
2. `ECOSYSTEM/operating-model/` - operator-facing operating model.
3. `AGENTS.md`, canonical standards under `docs/reference/`, and governed
   roadmaps, baselines, work orders, reviews, registries and checkers.
4. Current session state: front door, bootstrap read model, active handoff.
5. `governance/compat/check_*.py` machine checkers verify the above.

Provider-specific files and memory stores are execution aids for the agent that
owns them, including `CLAUDE.md`, provider memory files, and IDE side-channel
summaries. They are not CVF source of truth and must not be cited as canonical
authority in Source Authority tables, Source Verification ACCEPT rows, corpus
manifests, closure proof, or roadmap/work-order evidence. Re-verify any fact
learned from them against a CVF-governed surface before using it as evidence;
if no CVF-governed source exists, mark the claim `BLOCKED_SOURCE_NOT_FOUND`,
`DOCUMENTATION_ONLY_WITH_REASON`, or `NOT_CVF_SOURCE`.

## Guard Orientation Index

Before authoring any governed CVF artifact, read
`docs/reference/guard_orientation/README.md` to identify which guard surfaces
apply to the current task class and role, what blocks or outputs are required,
and what failure patterns to avoid. This applies to dispatcher, worker,
reviewer, closer, and session-sync steward alike; it is an orientation layer,
and canonical standards, work orders and machine checkers still control. Also
read `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
to avoid known literal-format gate traps.

## Task Class Routing

Resolve the canonical owner for any rule through the routing index. Common
entry points:

| Task class | Canonical owner |
|---|---|
| Startup / resume | `CVF_SESSION_MEMORY.md`; bootstrap read model; active handoff |
| Work-order authoring / dispatch | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` |
| Worker execution | `docs/reference/guard_orientation/README.md`; governing work order |
| Reviewer / closure | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` |
| Session-sync | active handoff; `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| ADIF defect disclosure | `governance/compat/check_adif_defect_registry_disclosure.py` |
| Corpus scan / absorption / proportional routing | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`; `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` |
| File size / maintainability | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` |
| Encoding / symbol discipline | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` |
| Autorun / commit steward | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` |
| Handoff boundary | `docs/reference/agent_handoff/README.md` |
| UI / Web design | `DESIGN.md` |

Repeated agent mistakes are governance training samples. Promote a repeated
defect into a written rule, then into a machine check, then into the earliest
applicable autorun phase gate, per
`docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`.

## Mandatory Public Export Disposition Guard

Canonical standard:
`docs/reference/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md`.
Machine guard: `governance/compat/check_public_export_disposition.py`.

Any changed closed roadmap, final wave completion packet, public-sync batch, or
public catalog claim must include a `Public Export Disposition` section with
exactly one of `EXPORTED`, `DEFERRED_PRIVATE_ONLY`, or
`BLOCKED_MISSING_PUBLIC_ARTIFACTS`. `EXPORTED` requires public-sync remote,
commit, and artifact path evidence. Private provenance closure is not public
catalog export.

## Mandatory Agent Workspace State Generated Aggregate Guard

Generated aggregate: `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`.
Machine guard: `governance/compat/check_agent_workspace_state.py`.
Lane taxonomy: `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md`.
Item template: `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_ITEM_TEMPLATE.json`.
Never hand-edit the aggregate; change source items and regenerate.

## Mandatory Agent Workspace Skeleton Guard

Skeleton front door: `CVF_SESSION/agent_workspace/workspace/README.md`.
Machine guard: `governance/compat/check_agent_workspace_skeleton.py`.

## Mandatory Agent Workspace Runtime Boundary Guard

Runtime contract:
`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md`.
Queue front door: `CVF_SESSION/agent_workspace/runtime_queue/README.md`.
Operator view plan:
`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md`.
Machine guard: `governance/compat/check_agent_workspace_runtime_boundary.py`.
The workspace skeleton and queues are contract surfaces only; no runtime
daemon, watcher, or dispatcher is authorized by them.

## Mandatory Corpus Completeness And Report Integrity

Canonical standard:
`docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`.
Machine guard: `governance/compat/check_corpus_completeness_report_integrity.py`.

Before claiming a complete scan, inventory, or "all files read", include the
`Corpus Completeness And Report Integrity` block with manifest, processing
ledger, reconciliation, exclusions, unreadable files, aggregation and drift
checks, and one allowed corpus verdict. Self-reported counts are not evidence.

## Mandatory Corpus-To-Knowledge-Map Reconciliation

Canonical standards:
`docs/reference/CVF_KNOWLEDGE_SYSTEM_METHOD_STANDARD_2026-06-01.md`;
`docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`.
Machine guard: `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`.

Include `## Knowledge System Reconciliation`; reconcile mapped, deferred and
unmapped totals. Bare `rg --files` is not completeness evidence; use
`rg --files --hidden --no-ignore`.

## Mandatory Live Governance Proof

Any test, roadmap closure, release gate, demo proof, or public claim asserting
CVF governance behavior must use a real provider API call. Mock mode is allowed
only for pure UI structure checks that assert no AI governance behavior.
Required command for release-quality proof:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Before rerunning any failed, partial, timed-out, or ambiguous live proof, follow
`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` and record a
secret-safe diagnostic. Never print raw keys, signed headers, bearer tokens, or
unredacted provider request bodies.

## Critical Repository Boundary

Rotated under the Governed File Size Guard (GC-023) to
`docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md`. Read it
before any push, public-sync work, or repository-boundary decision. This
workspace is the private provenance repository; public-facing changes go
through the sibling public-sync clone. Run `git remote -v` before any push
intended for the public repository.

## Claim Boundary

This carrier routes agents to canonical owners and carries the direct machine
bindings listed above. It is not a complete restatement of CVF governance, and
it makes no runtime, provider, live, deployment, public-sync, or production
readiness claim on its own. Historical pre-compaction text is preserved as
evidence at `docs/reference/archive/AGENTS_FULL_PRE_T2B_2026-08-11.md`, which
is `NOT_ACTIVE_AUTHORITY`.
