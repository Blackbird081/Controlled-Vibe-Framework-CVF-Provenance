# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-05-19

## Purpose

This file is the single session-memory entry point for new agents, resumed
agents, future `cvf-cli`, and future `cvf-mcp-server` startup.

It does not replace durable evidence, roadmaps, handoffs, or governance guards.
It routes agents to the current session state before they choose which deeper
materials to load.

## Owner And Source

Owner: CVF governance/session-continuity surface.

Source truth:

- human operator session decision on 2026-05-17
- active state registry at `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- review packets listed in Required First Reads

## Scope Boundary

In scope:

- session-start routing
- active handoff pointer routing
- current blocked-work posture
- startup guard routing for agents and future CLI/MCP entrypoints

Out of scope:

- replacing handoffs
- replacing evidence packets
- replacing governance guards
- implementing `cvf-cli` or `cvf-mcp-server`

## Active State Registry

Machine-readable active state:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Agents and tools must resolve this registry before treating any root handoff as
current.

## Current Session Mode

- Current mode: `operator_lane_selection_active`
- Previous mode: `system_reconvergence_stop`
- Freeze posture: `governance_kernel_freeze_recommended`
- Active handoff pointer: `AGENT_HANDOFF_V10_2026-05-19.md`
- Historical handoff archive: `CVF_SESSION/handoffs/archive/`
- Operator approved lanes B+C+H on 2026-05-19. Lane-specific stop lifts
  are in `CVF_SESSION/ACTIVE_SESSION_STATE.json`. Lanes execute in order
  B→C→H, each requiring its own GC-018. Broad absorption and new
  governance semantics remain blocked outside lane scopes.

## Required First Reads

Read these first for the current 17.05 reconvergence context:

- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_AGENT_HANDOFF_AND_MEMORY_GAP_CODEX_AUDIT_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SINGLE_SESSION_MEMORY_FRONT_DOOR_PROPOSAL_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_AGENT_ORCHESTRATOR_ROLE_ABSORPTION_GAP_CODEX_AUDIT_2026-05-17.md`

## Required Startup Guards

Route through:

- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`
- `docs/reference/CVF_SESSION_GOVERNANCE_BOOTSTRAP.md`
- `governance/toolkit/05_OPERATION/CVF_SESSION_GOVERNANCE_BOOTSTRAP_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_AGENT_HANDOFF_TRANSITION_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_AGENT_HANDOFF_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_MEMORY_GOVERNANCE_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNED_ARTIFACT_AUTHORING_GUARD.md`

## Protocol Requirements

1. Load this file first.
2. Resolve `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
3. Confirm active handoff, current mode, blocked work classes, and next allowed
   move.
4. Load only the first-read packets and guards required by the active state.
5. Treat root handoff files as current only when the active state registry
   points to them.

## Blocked Work Classes

Do not start these work classes from this session state without a later explicit
roadmap or human override:

- broad external knowledge absorption
- new governance semantics
- new role taxonomies
- new policy, risk, or guard engines
- new receipt envelopes
- new memory tiers
- new capability workflow runtime contracts
- new provider execution semantics
- public claims of a coherent governed capability runtime

## Startup Acknowledgment

Before material governed work, an agent should be able to state:

- active session mode
- active handoff path
- required first-read packet set
- blocked work classes
- next allowed move

## Next Allowed Move

Proceed with corrected Lane D → Lane E → Lane F → Lane G work-order sequence.
Lane D has filed GC-018 and is implemented as contract-and-flag work only.
Lane E has filed GC-018 and is implemented as offline governance reliability
metrics plus `cvf benchmark governance`; its operational baseline is honestly
marked `baseline_deferred_no_real_audit_log` because no suitable real audit
JSONL source exists in this workspace. Lane F is the next allowed
implementation lane after Lane E commit-level closure. Do not broaden
absorption, role taxonomy, provider semantics, public claims, or live-proof
claims outside the lane boundaries recorded in
`CVF_SESSION/ACTIVE_SESSION_STATE.json`.

## Enforcement And Verification

Machine check:

- `python governance/compat/check_active_session_state.py --enforce`

Hook chain:

- `governance/compat/run_local_governance_hook_chain.py`

## Boundaries And Non-Goals

- This front door does not assert that CVF already has a unified governed
  capability runtime.
- This front door does not authorize new semantic layers.
- This front door does not make private review packets public.
- This front door does not remove historical handoffs.

## Related Artifacts

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/READ_FIRST.md`
- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`
- `CVF_SESSION/handoffs/archive/`
- `AGENTS.md`
- `CLAUDE.md`
- `AGENT_HANDOFF_V9_2026-05-18.md`

## Public-Sync Workflow Orchestration Update — 2026-05-19

Public repository workflow hardening was completed from the sibling public-sync
clone:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Remote verified before push:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Final public-sync commit pushed:

`6842ffcf fix: align public web coverage gate`

New guard added in the public-sync clone:

- `governance/compat/check_workflow_orchestration_guard.py`
- `governance/toolkit/05_OPERATION/CVF_WORKFLOW_ORCHESTRATION_GUARD.md`

Purpose: make CVF workflow routing a first-class guard surface, not only a
GitHub-push fix. The guard is wired into the public static CI gate, local
governance hook chain, GitHub CI front door, and documentation/registry
surface.

Latest public GitHub checks observed green on commit `6842ffcf`:

- CVF Public Surface
- CVF Static CI Gate
- CVF CI
- CVF CI Pipeline
- CVF v1.6 Web CI

Boundary: no live release gate was run in this public-sync pass, so do not
claim new live governance behavior from this update. Documentation & Testing
legacy/provenance-era incompatibilities were not re-triggered by the final
web-only commit and remain a separate public-sync cleanup lane if needed.

Follow-up live proof on 2026-05-19: operator requested the release-quality live
gate after the public-sync CI push. The command
`python scripts/run_cvf_release_gate_bundle.py --json` was run from the
public-sync clone with process-scoped keys loaded from the provenance
`.env.local` file without printing key values. Result: PASS. Log path:
`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\artifacts\live-release-gate\release-gate-20260519-115957.out.log`.

## Lane D Provider Method Parity Update — 2026-05-19

Lane D source-fidelity found the Runtime Adapter Hub already has an optional
`LLMAdapter.stream()` callback-style method. Because that file is outside Lane D
write ownership and the method already exists, this lane did not rewrite the
Runtime Adapter Hub or invent a second broad adapter taxonomy.

Lane D implementation instead added the minimal gateway normalization surface:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/stream-contract.test.ts`
- CLI `--stream` boolean parsing and execute payload `stream: true`
- `streamingEnabled: false` in all three governed pack policies

Evidence: model gateway tests passed (`12 files`, `34 tests`), model gateway
typecheck passed, governance CLI tests passed (`4 files`, `50 tests`), and CLI
typecheck passed. Route streaming remains explicitly out of scope.

## Lane E Benchmark Reorientation Update — 2026-05-19

Lane E added offline governance reliability metrics and the CLI command:

```powershell
cvf benchmark governance --input <audit.jsonl> [--format json|table]
```

New implementation paths:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/governance-reliability-metrics.test.ts`
- `docs/baselines/CVF_GOVERNANCE_RELIABILITY_BASELINE_2026-05-19.md`

Baseline status: `baseline_deferred_no_real_audit_log`. Existing JSONL files in
the workspace were checked but are latency/PVV evidence, not governance audit
JSONL with the required metric fields. Synthetic data remains test-only. The
work-order requested `docs/benchmark/`, but docs governance rejected that
non-taxonomy folder, so the baseline lives in `docs/baselines/`.

Evidence: governance CLI tests passed (`5 files`, `59 tests`) and CLI
typecheck passed.

## Lane F Noncoder UX Update — 2026-05-19

Lane F added the bounded outcome-first home UI shortcut for three existing
governed packs:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/OutcomeQuickActions.test.tsx`
- home render/handler wiring in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx`

GC-018 and closure packet:

- `docs/baselines/CVF_GC018_LANE_F_NONCODER_UX_2026-05-19.md`
- `docs/reviews/CVF_LANE_F_NONCODER_UX_COMPLETION_2026-05-19.md`

Source-fidelity note for future agents/Claude: the buttons use only existing
template IDs `app_builder_complete`, `documentation`, and `strategy_analysis`.
They call the existing `handleSelectTemplate()` path. A new analytics event was
intentionally not retained because the typed analytics registry rejected it and
Lane F had no authority to expand analytics contracts.

Evidence: `npm run build` passed, `npm run lint` passed, and
`npm run test:run -- src/components/OutcomeQuickActions.test.tsx` passed
(`3/3`). Full web `npm run test:run` still fails inherited/background tests:
role-count expectation still assumes 8 roles while `SERVICE_AGENT` makes 9,
and skill corpus/template mapping tests still report dead references. These
are not Lane F regressions.

Active handoff advanced from `AGENT_HANDOFF_V9_2026-05-18.md` to
`AGENT_HANDOFF_V10_2026-05-19.md` because V9 approached the governed
active-markdown file-size cap.

## Lane G Runtime Actor Enforcement Update — 2026-05-19

Lane G added the bounded `allowedActorRoles` execute-route gate for the three
governed pack policies.

New/modified implementation paths:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/*/execution.policy.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.test.ts`

GC-018 and closure packet:

- `docs/baselines/CVF_GC018_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_2026-05-19.md`
- `docs/reviews/CVF_LANE_G_RUNTIME_ACTOR_ENFORCEMENT_COMPLETION_2026-05-19.md`

Source-fidelity note: route.ts was already exactly 1001 lines, so helper logic
was placed in `execute-role-resolver.ts` and route line count remains 1001.
Raw JSON role arrays are filtered against known `CVFRole` values before use.

Evidence: focused route/resolver tests passed (`41/41`), adjacent
guard-runtime role tests passed (`116/116` across 4 focused files), build
passed, lint passed, and isolated live retrieval tests passed (`4/4`). Full web
suite still fails on skill corpus/template mapping dead references; the old
`SERVICE_AGENT` 8-role expectation is fixed.

## Reviewer Closure — Lane D/E/F/G + Workflow Chain Proposal (2026-05-19)

Reviewer role (Orchestrator): Verified and closed.

Lane D quality: PASS. `StreamContract` interface correctly defines the
streaming governance surface. `receiptObligation` field carries CVF receipt
semantics into chunked output. `streamingEnabled: false` in pack policies is
correct scope discipline.

Lane E quality: PASS with honest baseline. `cvf benchmark governance` CLI
command wired. Baseline is `baseline_deferred_no_real_audit_log` — Worker
correctly declined to fabricate evidence from latency data.

Lane F quality: PASS. `OutcomeQuickActions.tsx` (113 lines) is bilingual,
delegates to existing `handleSelectTemplate()`. Analytics event correctly
dropped when typed registry rejected it.

Lane G quality: PASS. `allowedActorRoles` gate on `/api/execute`. `KNOWN_CVF_ROLES`
runtime filter prevents JSON injection. `OBSERVER` and `HUMAN` correctly
excluded. Route stays at 1001 lines. Adjacent SERVICE_AGENT role-count fix
is accurate scope restoration.

Workflow chain proposal: AWAITING_REBUTTAL. Worker (Codex) did not touch
the proposal file — correct behavior. Proposal remains at `ae492d7d` for
Reviewer/Operator rebuttal.

Open blockers carried forward:

1. `skill-corpus-governance.test.ts` dead references — needs dedicated work order.
2. `check_template_skill_standard_guard_compat.py` NameError — tech debt.
3. GC-024 advisory — public catalog needs D/E/F/G capabilities before next sync.
4. `system_reconvergence_stop` posture still active — Operator must lift.

Active handoff for next agent: `AGENT_HANDOFF_V10_2026-05-19.md`
Latest HEAD at closure: `d7d844b5`

## Runtime Maturity Delta M1/C2/D2/H2 Update — 2026-05-19

Codex completed the requested execution sequence from
`docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md`:
M1 + C2 first, then D2 + H2.

Status:

- M1 Maika text summary:
  `CLOSED_WITH_DEPLOYMENT_VERIFICATION_PENDING`. Code/build/lint/check passed,
  but live deployed Supabase invocation with an authenticated admin/teacher
  session is not claimed.
- C2 CLI execute hardening: `CLOSED`. `npm test` passed (`62/62`), and
  `npm run check` passed in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`.
- D2 vision contract: `CLOSED`. `npm test` passed (`39/39`) and
  `npm run check` passed in `EXTENSIONS/CVF_MODEL_GATEWAY`.
- H2 audit memory policy refinement: `CLOSED`. Targeted audit-memory tests
  passed (`3/3`) and `npm run build` passed in `cvf-web`.

Completion reviews:

- `docs/reviews/CVF_M1_MAIKA_TEXT_SUMMARY_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`

Final docs checks passed:

- `python governance/compat/check_docs_governance_compat.py`
- `python governance/compat/check_markdown_structural_completeness.py`

## Claim Boundary

This artifact establishes a governed session-memory front door and machine
checkable active-state pointer. It does not complete the broader Governance
Kernel Freeze or system reconvergence work.
