# CVF GC-018 Baseline - Active Continuity T2B Instruction Carrier Compaction

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-08-11

Batch ID: ACRC-T2B

Risk ceiling: R2

Dispatch base head: `178c5e7e169c936e285f484de5abd8dae2e06c07`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: implementation worker role

## Purpose

Reduce the always-loaded Core and inherited instruction carriers while
preserving every binding rule, direct checker literal, provider-memory
boundary, and downstream bootstrap contract.

## Authorization

The operator selected T2B on 2026-08-11 after T2A closed and was parked. This
authorizes packet authoring and one bounded no-commit implementation only after
pre-dispatch PASS.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| T2A material acceptance | commit `fd4d61e73`; T2A completion review | SATISFIED |
| T2A continuity closure | commits `e95fc658f` and `178c5e7e1` | SATISFIED |
| T2B operator selection | operator selection message dated 2026-08-11 | SATISFIED |
| source/binding map before rewrite | `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_SOURCE_BINDING_MATRIX_2026-08-11.md` | SATISFIED |

## Scope

T2B may archive and compact root `AGENTS.md`, provider-local `CLAUDE.md`, and
the future-project downstream AGENTS template; add one canonical routing index
and one machine checker with focused tests; and wire that checker into existing
autorun, local-hook catalogs, and documentation CI.

## Non-Goals

No existing downstream project is modified. T3, the full active-state
aggregate, provider/network/live behavior, application/runtime code, public
sync, push, deployment, and production claims remain outside scope.

## Design Control Gate

The worker must preserve preimage bytes in three dated archives, satisfy the
source/binding matrix, and make the new checker fail closed on oversize,
missing literal, missing heading coverage, archive drift, malformed UTF-8,
unconditional full-read wording, and missing gate wiring.

## Baseline Decision

Authorize one exact-15, no-commit T2B implementation after this baseline,
the paired Work Order, and the accepted source/binding matrix pass the
pre-dispatch gate. T3 and existing downstream migration remain parked.

## Approved Budgets

| Active carrier | Maximum lines | Maximum bytes |
|---|---:|---:|
| `AGENTS.md` | 220 | 20,480 |
| `CLAUDE.md` (`NOT_CVF_SOURCE`) | 160 | 16,384 |
| downstream AGENTS template | 180 | 20,480 |
| canonical routing index | 300 | 32,768 |

## Exact Worker Scope

1. `AGENTS.md`
2. `CLAUDE.md`
3. `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
4. `docs/reference/archive/AGENTS_FULL_PRE_T2B_2026-08-11.md`
5. `docs/reference/archive/CLAUDE_FULL_PRE_T2B_2026-08-11.md`
6. `docs/reference/archive/CVF_DOWNSTREAM_AGENTS_TEMPLATE_FULL_PRE_T2B_2026-08-11.md`
7. `docs/reference/CVF_AGENT_INSTRUCTION_CARRIER_ROUTING_INDEX_2026-08-11.md`
8. `governance/compat/check_agent_instruction_carriers.py`
9. `governance/compat/test_check_agent_instruction_carriers.py`
10. `governance/compat/agent_autorun_command_catalog.py`
11. `governance/compat/local_governance_hook_catalog_pre_commit.py`
12. `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
13. `governance/compat/local_governance_hook_catalog_pre_push.py`
14. `.github/workflows/documentation-testing.yml`
15. `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_WORKER_RETURN_2026-08-11.md`

Every path outside this exact 15 is forbidden to the worker.

## Required Behavior

1. Copy all three preimage carriers byte-for-byte to the exact archive paths
   before rewriting active files.
2. Create a compact canonical routing index accounting for all 38 current
   AGENTS level-two headings and the machine-reader matrix.
3. Keep AGENTS canonical and concise; keep provider-local CLAUDE guidance
   explicitly `NOT_CVF_SOURCE`.
4. Preserve direct literals required by current checkers and the downstream
   doctor/golden bootstrap harness.
5. Preserve progressive startup: no default full state/history read.
6. Enforce budgets, hashes, literals, routing coverage and bindings through the
   new checker, wired into autorun, pre-commit, reviewer-fast, pre-push and CI.
7. Stop uncommitted at pending independent review.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| T2B follows accepted T2A | `docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md` | lines 171-218 | `T2A`; `T2B` | roadmap tranche sequence | ACCEPT |
| every AGENTS heading is mapped | `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T2B_SOURCE_BINDING_MATRIX_2026-08-11.md` | AGENTS Heading Binding Matrix | 38 heading rows | T2B source map | ACCEPT |
| active checker reads root carriers | `governance/compat/check_active_session_state.py` | lines 59-60, 656-704 | `AGENTS_PATH`; `CLAUDE_PATH`; `AGENT_ROUTER_MARKERS` | active-session checker | ACCEPT |
| workspace state checker requires direct AGENTS literals | `governance/compat/check_agent_workspace_state.py` | marker map | `AGENTS_PATH` marker tuple | workspace state checker | ACCEPT |
| workspace skeleton checker requires direct AGENTS literals | `governance/compat/check_agent_workspace_skeleton.py` | marker map | `AGENTS_PATH` marker tuple | workspace skeleton checker | ACCEPT |
| workspace runtime checker requires direct AGENTS literals | `governance/compat/check_agent_workspace_runtime_boundary.py` | marker map | `AGENTS_PATH` marker tuple | workspace runtime-boundary checker | ACCEPT |
| public checker requires direct AGENTS binding | `governance/compat/check_public_export_disposition.py` | binding validator | `AGENTS_PATH` | public-export checker | ACCEPT |
| completeness checker requires direct carrier bindings | `governance/compat/check_corpus_completeness_report_integrity.py` | binding validator | `AGENTS_PATH`; `CLAUDE_PATH` | corpus completeness checker | ACCEPT |
| reconciliation checker requires direct carrier bindings | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | binding validator | `AGENTS_PATH`; `CLAUDE_PATH` | corpus reconciliation checker | ACCEPT |
| downstream template is copied into generated AGENTS | `scripts/new-cvf-workspace.ps1` | lines 343-413 | `$agentsTemplatePath` | downstream bootstrap writer | ACCEPT |
| downstream doctor requires role/rehydration tokens | `scripts/check_cvf_workspace_agent_enforcement.ps1` | lines 407-440 | `requiredRoleTokens`; `rehydrationTokens` | downstream workspace doctor | ACCEPT |
| golden harness requires latency carrier phrases | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | lines 63-69 | `Test-CvfCarrierContent` | golden downstream harness | ACCEPT |
| hook commands live in catalogs | `governance/compat/local_governance_hook_catalog.py` | `HOOK_CHAINS` | phase catalog imports | local hook chain | ACCEPT |
| autorun commands live in catalog | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` | `_common_commands` | autorun workflow | ACCEPT |

## Stop Conditions

Return `BLOCKED` if a current binding lacks a canonical owner, exact-15 is
insufficient, any archive differs from its preimage, a required literal cannot
fit the approved budget without semantic loss, or an existing downstream
project/public/external path would need mutation.

## Acceptance Criteria

- AC-01: all three archives match the pinned preimage SHA-256 and raw bytes.
- AC-02: all four active/index budgets pass at N and fail at N+1.
- AC-03: routing index covers every mapped AGENTS heading exactly once.
- AC-04: AGENTS retains all direct checker literals and canonical startup.
- AC-05: CLAUDE is provider-local, compact, and retains required markers.
- AC-06: downstream template retains substitution tokens, seven roles, phase chain,
  rehydration tokens, and golden latency phrases exactly as required.
- AC-07: new checker fails closed on malformed/missing/unreadable inputs and
  archive/hash drift without raw exception leakage.
- AC-08: new checker is wired into autorun, all three local hook catalogs and
  documentation CI.
- AC-09: active-session, corpus, workspace, public-export, golden downstream,
  encoding, size and diff gates pass.
- AC-10: worker changes exact 15 paths, leaves HEAD unchanged/staged zero, and
  makes zero provider/network/live/downstream/public/push/commit calls.

## Review Gate

Independent review must compare the source/binding matrix to current source,
recompute archives and budgets, inspect semantic preservation, run adversarial
checker tests and the downstream golden harness, and reject green tests that
omit a binding class.

## Required Evidence

The return must contain exact-15 status evidence, archive hashes and raw-byte
equality, before/after line and byte counts, all 38 heading routes, literal
binding results, N/N+1 cases, focused and golden-harness results, HEAD/staged
state, and zero external-effect accounting.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACRC-T2B --title "Active Continuity Instruction Carrier Compaction" --date 2026-08-11 --base 178c5e7e169c936e285f484de5abd8dae2e06c07 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | dependency, source-map, exact-scope, budget, archive, binding and downstream boundaries |
| checkerReadAheadConfirmation | active-session, protected-path, dispatch, structure, binding, file-size and worker-return checkers read |
| docOnlyNewFields | approved carrier budget table and T2B archive names |
| claimBoundary | dispatch authoring only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds: NONE_RETURNED

Returned defects: NONE_RETURNED

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_closure_packaging_preflight.py`; `governance/compat/check_active_session_state.py`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/check_agent_workspace_skeleton.py`; `governance/compat/check_agent_workspace_runtime_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Core Guard Self-Protection Authorization`; `Agent Handoff Contract Control Block`; `Expected manifest`; `Actual changed set`; `Manifest delta`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | source-backed confirmation before dispatch |
| claimBoundary | packet and exact-scope form only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private CVF Core workspace |
| Session or invocation | ACRC-T2B baseline authoring, 2026-08-11 |
| Working directory | repository root at `178c5e7e1` |
| Command or tool surface | targeted reads, hashes/sizes, source mapping, scaffold, patch authoring |
| Target paths | roadmap, source map, baseline and Work Order |
| Allowed scope source | operator T2B selection and accepted roadmap |
| Before status evidence | clean worktree at HEAD `178c5e7e1`; staged zero |
| After status evidence | exact four dispatch artifacts before commit |
| Diff evidence | status/name-status and local dispatch gates |
| Approval boundary | packet authoring and exact-15 dispatch only |
| Claim boundary | no implementation, external effect, commit, or push |
| Agent type | dispatcher |
| Invocation ID | `active-continuity-read-cost-t2b-baseline-2026-08-11` |
| Expected manifest | roadmap, source map, baseline, Work Order |
| Actual changed set | same four dispatcher paths before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: dispatcher deletes or renames nothing |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T2B is private provenance instruction maintenance. Public projection
requires a later separately authorized public-sync batch.

## Claim Boundary

This baseline authorizes only bounded structural instruction-carrier
compaction and machine enforcement. It makes no runtime, provider, live,
downstream migration, public availability, deployment, or production claim.
