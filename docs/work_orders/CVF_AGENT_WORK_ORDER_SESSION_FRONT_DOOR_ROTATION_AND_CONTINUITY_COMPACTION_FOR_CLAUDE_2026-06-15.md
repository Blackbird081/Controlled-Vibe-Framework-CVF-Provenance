# CVF Agent Work Order -- Session Front Door Rotation And Continuity Compaction

rawMemoryReleased: false

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-15

Worker: Claude (SINGLE_AGENT_MULTI_ROLE -- orchestrator and worker in same session)

Reviewer: Codex (owns commit, completion review, session state final push)

GC-018: `docs/baselines/CVF_GC018_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_2026-06-15.md`

Roadmap: `docs/roadmaps/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_ROADMAP_2026-06-15.md`

Base HEAD at dispatch: `c7d3d955`

WORKER_MUST_NOT_COMMIT: enforced. Worker authors artifacts; Codex commits.

---

## Authority Chain

GC-018: `docs/baselines/CVF_GC018_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_2026-06-15.md`
Roadmap: `docs/roadmaps/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_ROADMAP_2026-06-15.md`
Operator authorization: operator message 2026-06-15. SINGLE_AGENT_MULTI_ROLE.

## Agent Roles

| Role | Agent | Responsibility |
|---|---|---|
| Orchestrator | Claude | Authored roadmap, GC-018, work order |
| Worker | Claude | Authors all artifacts (IS-1 through IS-9) |
| Reviewer | Codex | Commits all artifacts, authors completion review (D13) |

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md` (active handoff at dispatch)
4. This work order

## Pre-Flight Checks

- [x] `wc -l AGENT_HANDOFF_V18_2026-06-12.md` -- confirmed 964L advisory-exceeded source before compaction
- [x] `wc -l CVF_SESSION_MEMORY.md` -- confirmed 1112L advisory-exceeded source before compaction
- [x] `python governance/compat/check_governed_file_size.py --json` -- confirmed advisory pressure before compaction

## Write Ownership

Worker (Claude) may write artifacts 1--11 in Allowed Scope.
Reviewer (Codex) may write artifact 12 (completion review) and commit all.
No other agent may write to these paths without fresh GC-018.

## Execution Plan

See IS-1 through IS-10 sections below.

## Evidence Requirements

- `wc -l AGENT_HANDOFF_V19_2026-06-15.md` < 200
- `wc -l CVF_SESSION_MEMORY.md` < 400
- `python governance/compat/generate_active_session_state.py --check` PASS
- `python governance/compat/generate_corpus_scan_registry.py --check` PASS
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` 16/16 PASS

## Review Gate

Reviewer (Codex) runs pre-closure autorun gate:
`python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base c7d3d955 --head HEAD`

Must PASS before completion review is authored and committed.

## Closure Checklist

- [x] D1 GC-018 authored
- [x] D2 Work order authored
- [x] D3 V19 handoff (IS-1)
- [x] D4 V18 archived (IS-2)
- [x] D5 CVF_SESSION_MEMORY.md compacted (IS-3)
- [x] D6 Compaction archive (IS-3)
- [x] D7 nextAllowedMove.json (IS-4)
- [x] D8 lastUpdated.json (IS-4)
- [x] D9 ACTIVE_SESSION_STATE.json regenerated (IS-5)
- [x] D10 AGENTS.md pointer update (IS-6)
- [x] D11 GC-051 entry (IS-7)
- [x] D12 Aggregate regenerated (IS-8)
- [x] D13 Completion review (reviewer Codex)

## Return-To-Orchestrator Conditions

Worker returns `COMPLETE_PENDING_REVIEW` when all IS-1 through IS-10 are done,
reviewer-fast 16/16 PASS, no uncommitted runtime mutations, and worker return
artifact is authored. Return to orchestrator (Codex) for commit and completion review.

Worker returns `BLOCKED` when any allowed-scope gate fails without a repair
path inside the work order scope. Return to orchestrator with blocking reason.

## Reviewer Closure Conversion

Reviewer (Codex) performs closure conversion after worker return:

completionReviewPath: `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:
- `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_COMPLETION_2026-06-15.md`
- All committed worker artifacts (D3 through D12)

Reviewer runs pre-closure autorun gate, inspects diff, authors completion review,
and commits all artifacts in a single governed batch.

## Operator Checkpoint

No operator checkpoint required for this compaction batch. Scope is bounded to
session continuity files only. Reviewer (Codex) may proceed directly to commit
after gate PASS.

## Intake Role Routing Decision

Orchestrator intake summary: three front-door files exceed advisory threshold;
compaction is infrastructure maintenance with high governance leverage.
Scope classification: governance-continuity, R0 (safe), no live proof, no
provider, no runtime change.
Risk sensitivity: low -- all artifacts are reversible, no runtime behavior affected.
Selected canonical route mode: SINGLE_AGENT_MULTI_ROLE with WORKER_MUST_NOT_COMMIT.
Role separation basis: Claude as orchestrator+worker; Codex as independent reviewer+committer.
Escalation condition: if any gate fails outside allowed-scope repair path, return BLOCKED to operator.

## Single-Agent Multi-Role Control Block

Role separation: Claude acts as orchestrator (authored roadmap/GC-018/work order)
and as worker (IS-1 through IS-9). Codex acts as independent reviewer and
committer. Claude must not commit, push, merge, or modify session state files
beyond the allowed scope above.
Evidence basis: GC-018 at `docs/baselines/CVF_GC018_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_2026-06-15.md`.
Self-review boundary: Claude may author worker return only; Codex reviews and
authors completion review independently.
Escalation conditions: if a session-state mutation outside allowed scope is
required, stop and return BLOCKED to operator.
Gate sequence: IS-1 through IS-9 -> reviewer-fast 16/16 -> worker return -> Codex
pre-closure gate -> Codex completion review -> Codex commit.

## Commit Mode

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: c7d3d955
executionBaseHead: c7d3d955
closureBaseHead: set by Codex at pre-closure gate

## Worker Autonomy / No-Question Rule

Worker executes IS-1 through IS-9 without confirmation or escalation.
Machine-gate failures inside allowed scope are mandatory worker repairs.
Work outside allowed scope (runtime source, live proof, public-sync, secret
consumption, forbidden path mutation, destructive actions) is BLOCKED outright
and must be reported as a scope violation in the worker return -- not escalated
as a question.

## Purpose

Open a new compact V19 handoff, archive V18, compact
`CVF_SESSION_MEMORY.md` to under 400 lines with prior tranche prose moved to a
compaction archive, update state source entries, regenerate
`ACTIVE_SESSION_STATE.json`, update `AGENTS.md` pointer only, add GC-051 entry
for V19, and regenerate the corpus scan registry.

---

## Allowed Scope

Artifacts the worker may author or modify:

1. `AGENT_HANDOFF_V19_2026-06-15.md` (new, < 200 lines)
2. `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md` (archive copy of V18)
3. `CVF_SESSION_MEMORY.md` (compact to < 400 lines)
4. `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md` (new compaction archive)
5. `CVF_SESSION/state/entries/nextAllowedMove.json` (update value)
6. `CVF_SESSION/state/entries/lastUpdated.json` (update value)
7. `CVF_SESSION/ACTIVE_SESSION_STATE.json` (regenerated by running generator)
8. `AGENTS.md` (update V18 reference to V19 -- pointer only, net-zero prose)
9. `docs/corpus-intelligence/registry/entries/session-front-door-v19.json` (new GC-051 entry, registryOrder 81)
10. `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (regenerated via generator)

Worker return (authored by Claude as worker, no commit):

11. `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_WORKER_RETURN_2026-06-15.md`

Completion review (authored by Codex as reviewer):

12. `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_COMPLETION_2026-06-15.md`

NOT allowed: any runtime source, test, EXTENSIONS, ECOSYSTEM, provider/API,
live proof, public-sync, or session-state file outside the list above.

---

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Claude (worker) may author artifacts 1--11
above. Codex (reviewer) may commit all artifacts 1--12, author artifact 12,
regenerate `ACTIVE_SESSION_STATE.json` if drift is found, and run the
pre-closure autorun gate.

Protected paths (must appear in Agent Operation Trace Expected manifest):

- `AGENT_HANDOFF_V19_2026-06-15.md`
- `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/lastUpdated.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENTS.md`
- `docs/corpus-intelligence/registry/entries/session-front-door-v19.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_WORKER_RETURN_2026-06-15.md`

Rollback boundary: if session-sync gates fail, revert only this compaction
batch. Do not revert prior closed tranches.

Operator authorization: explicit. Scope locked to continuity compaction only.

---

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| `activeHandoff` field in ACTIVE_SESSION_STATE.json | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | root key | `activeHandoff` | generate_active_session_state.py output | ACCEPT |
| `currentMode` field in ACTIVE_SESSION_STATE.json | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | root key | `currentMode` | generate_active_session_state.py output | ACCEPT |
| `stateKey` field in nextAllowedMove.json | `CVF_SESSION/state/entries/nextAllowedMove.json` | top-level | `stateKey` | state entry schema | ACCEPT |
| `value` field in nextAllowedMove.json | `CVF_SESSION/state/entries/nextAllowedMove.json` | top-level | `value` | state entry schema | ACCEPT |
| `stateOrder` field in lastUpdated.json | `CVF_SESSION/state/entries/lastUpdated.json` | top-level | `stateOrder` | state entry schema | ACCEPT |
| `registryOrder` in GC-051 entry | `docs/corpus-intelligence/registry/entries/model-gateway-c02-p4a-unified-gateway-skeleton-tests.json` | line 2 | `registryOrder` | GC-051 entry schema | ACCEPT |
| `supersededHandoffs` array in ACTIVE_SESSION_STATE.json | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | root array | `supersededHandoffs` | generate_active_session_state.py output | ACCEPT |
| AGENT_HANDOFF_V18 archive pointer in ACTIVE_SESSION_STATE.json | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `supersededHandoffs` array (current) | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V17_2026-06-07.md` (V17 example -- V18 will join after archive) | state array | ACCEPT |
| AGENTS.md handoff reference | `AGENTS.md` | lines 16--17 | `AGENT_HANDOFF_V18_2026-06-12.md` (current) | front-door routing | ACCEPT |
| `generate_active_session_state.py` command | `AGENTS.md` lines 458--461 and `CVF_SESSION/ACTIVE_SESSION_STATE.json` generator field | line 461 | `activeSessionStateGenerator` | generate_active_session_state.py | ACCEPT |
| `generate_corpus_scan_registry.py --generate` | `governance/compat/generate_corpus_scan_registry.py` | line 14 | `REGISTRY_PATH` | REGISTRY_PATH constant (output path) | ACCEPT |

New doc-only fields (no runtime claim):

| Field | Doc-only rationale |
|---|---|
| `session-front-door-v19` (GC-051 entry id) | New entry not yet in registry; doc-only until generator runs |
| `session_front_door_rotation_compaction_complete` (mode value) | New mode string; doc-only until state source files updated |

---

## Execution Instructions

### IS-1 Open V19 handoff (< 200 lines)

Author `AGENT_HANDOFF_V19_2026-06-15.md` at repo root.

Required sections:

- Memory class: POINTER_RECORD
- Status: ACTIVE HANDOFF
- Date opened: 2026-06-15
- Supersedes: `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`
- Purpose (1--2 sentences)
- Scope / Target / Owner Boundary (< 5 lines)
- Startup Acknowledgment (single line)
- Current Mode: `session_front_door_rotation_compaction_complete`
- Active Boundary (current handoff + archived predecessor)
- Core Guard Self-Protection Authorization (reuse from GC-018; reference protected paths)
- Latest Continuity Note (P3/P4A closed; compaction closed; next allowed move)
- Parked Lanes (pointer to parked items, not expanded list)

Hard limit: < 200 lines. Do not expand parked lane detail here.

### IS-2 Archive V18

Copy V18 content to
`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`.
Do not modify the V18 content. The root-level V18 file is deleted at commit
time by Codex (reviewer).

### IS-3 Compact CVF_SESSION_MEMORY.md

Keep:

- Front matter (Memory class, Status, Last updated, Current mode marker,
  Enforcement posture, Freeze posture)
- Purpose section
- Startup Order section (updated to reference V19)
- Current State section (updated: mode = `session_front_door_rotation_compaction_complete`,
  active handoff = `AGENT_HANDOFF_V19_2026-06-15.md`)
- Latest Continuity Note (brief: P3/P4A closed, compaction closed, next move)

Move all content below Latest Continuity Note (prior closed-tranche history)
to `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`.

Target line count: < 400 lines.

Add at the bottom of CVF_SESSION_MEMORY.md a one-line pointer:

`Prior closed-tranche history archived at: CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`

### IS-4 Update state source entries

Update `CVF_SESSION/state/entries/nextAllowedMove.json`:

```json
{
  "stateOrder": 126,
  "stateKey": "nextAllowedMove",
  "value": "Session Front Door Rotation And Continuity Compaction is CLOSED_PASS_BOUNDED. AGENT_HANDOFF_V19_2026-06-15.md is the active handoff; V18 archived. CVF_SESSION_MEMORY.md compacted under 400 lines. Next allowed move: consider Model Gateway C-02 P4B live-provider wiring only through fresh operator authorization, fresh GC-018, source-verified work order, live-run diagnostic discipline, and explicit credential boundary. P4A does not authorize provider/API use, live proof, provider/model addition, EPF wiring, strategy-layer implementation, AI Gateway absorption, public-sync, external app mutation, raw memory release, co-work product development, production readiness, or public readiness. LHW24 remains the latest closed numbered LHW wave. Strategy Layer implementation, AI Gateway family absorption, live Redis proof, next-auth, and external receipt-anchor remain parked."
}
```

Update `CVF_SESSION/state/entries/lastUpdated.json`:

```json
{
  "stateOrder": 215,
  "stateKey": "lastUpdated",
  "value": "2026-06-15"
}
```

### IS-5 Regenerate ACTIVE_SESSION_STATE.json

Run:

```bash
python governance/compat/generate_active_session_state.py --generate
```

Verify `activeHandoff` = `AGENT_HANDOFF_V19_2026-06-15.md` and
`currentMode` = `session_front_door_rotation_compaction_complete` in output.

### IS-6 Update AGENTS.md pointer

Find the two occurrences of `AGENT_HANDOFF_V18_2026-06-12.md` in `AGENTS.md`
(lines 16 and 24) and change both to `AGENT_HANDOFF_V19_2026-06-15.md`.
No other changes permitted. Net line change must be zero.

### IS-7 Add GC-051 entry for V19

Create `docs/corpus-intelligence/registry/entries/session-front-door-v19.json`:

```json
{
  "registryOrder": 81,
  "id": "session-front-door-v19",
  "corpusType": "POLICY_DOCUMENT",
  "displayName": "CVF Session Front Door Handoff V19 compact pointer record",
  "scopePaths": [
    "AGENT_HANDOFF_V19_2026-06-15.md"
  ],
  "fileCount": 1,
  "status": "SCANNED",
  "findings": [],
  "negativeSearchTerms": [
    "fetch (not in handoff - no network call)",
    "rawMemoryReleased: true (not in handoff - stays false)"
  ],
  "nextScanRecommendation": "NONE_REQUIRED",
  "scanWave": "SESSION-FRONT-DOOR-ROTATION-2026-06-15",
  "scanDate": "2026-06-15",
  "manifestHash": null,
  "manifestPath": null,
  "packetPath": "docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_WORKER_RETURN_2026-06-15.md",
  "notes": "Compact active handoff pointer record opened 2026-06-15. Supersedes V18. Contains current mode, next allowed move, parked lane pointers, and Core Guard Self-Protection Authorization. No runtime source. No live call. No provider data."
}
```

### IS-8 Regenerate GC-051 aggregate

Run:

```bash
python governance/compat/generate_corpus_scan_registry.py --generate
```

Verify corpora count increases to 81.

### IS-9 Author worker return

Create `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_WORKER_RETURN_2026-06-15.md`.

Required sections: Purpose, Target And Source, Scope And Methodology, Changed
File Set (all paths), Findings And Position, Acceptance Criteria Evidence
(AC-1 through AC-9 from roadmap), Gate Results, No-Commit Evidence, Public
Export Disposition (DEFERRED_PRIVATE_ONLY with Reason), Legacy Absorption
Coverage Index Disposition (NOT_APPLICABLE_WITH_REASON), Finding-To-Governance
Learning Disposition, Risk And Corrective Action, Negative Search And Collision
Discipline, Claim Boundary, Agent Operation Trace Block (17-label table).

### IS-10 Run reviewer-fast gate

```bash
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
```

Must reach 16/16 PASS before submitting worker return.

---

## Acceptance Criteria

See roadmap AC-1 through AC-9. Worker is responsible for AC-1 through AC-8.
Reviewer (Codex) is responsible for AC-9 (committed diff evidence).

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap deliverable | Work order instruction | Status |
|---|---|---|
| D3 V19 handoff | IS-1 | DISPATCHED |
| D4 V18 archived | IS-2 | DISPATCHED |
| D5 CVF_SESSION_MEMORY.md compacted | IS-3 | DISPATCHED |
| D6 Compaction archive | IS-3 | DISPATCHED |
| D7 nextAllowedMove.json | IS-4 | DISPATCHED |
| D8 lastUpdated.json | IS-4 | DISPATCHED |
| D9 ACTIVE_SESSION_STATE.json regenerated | IS-5 | DISPATCHED |
| D10 AGENTS.md pointer update | IS-6 | DISPATCHED |
| D11 GC-051 entry | IS-7 | DISPATCHED |
| D12 Aggregate regenerated | IS-8 | DISPATCHED |
| Worker return | IS-9, IS-10 | DISPATCHED |
| D1 GC-018 | Authored by Orchestrator | COMPLETE |
| D2 Work order | This document | COMPLETE |
| D13 Completion review | Reviewer (Codex) | COMPLETE |

---

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this work order performs session continuity
maintenance only (handoff rotation, CVF_SESSION_MEMORY.md compaction, state
source updates, GC-051 registry update). It does not add or absorb any legacy
knowledge, workflow-chain connector, or foundation-plane capability. The
coverage index at
`docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` is
unaffected by this compaction batch.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED`; checked closure checklist | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_COMPLETION_2026-06-15.md` | Codex review packet | PASS |
| Roadmap state | `docs/roadmaps/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_ROADMAP_2026-06-15.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generator drift check | PASS |
| Registry Markdown | N/A | N/A with reason: no markdown companion exists or is required by GC-051 | PASS |
| External evidence digest | N/A | N/A with reason: no live proof, provider call, or external service | N/A with reason |
| System loop interlock | N/A | N/A with reason: no autonomous mutation, loop activation, or live routing | N/A with reason |
| Session continuity | `AGENT_HANDOFF_V19_2026-06-15.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active pointers agree; root V18 removed | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Receipt acceptance primitives | N/A with reason: this batch does not create or accept runtime receipts | No receipt primitive invoked | PASS |
| Query acceptance primitives | N/A with reason: this batch does not execute retrieval/query acceptance | No query acceptance primitive invoked | PASS |
| Freshness disclosure | N/A with reason: no external or time-sensitive result is accepted | No freshness field required | PASS |

## Claim Boundary

This work order authorizes only the session continuity compaction artifacts
listed in Allowed Scope. It does not authorize runtime source changes, test
mutations, live proof, public-sync, provider/API use, or any governed work
outside those paths. Worker must not exceed this boundary.

## Agent Operation Trace Block

| Label | Value |
|---|---|
| Actor | Claude (SINGLE_AGENT_MULTI_ROLE -- orchestrator + worker) |
| Provider or surface | Claude Code VSCode extension, local filesystem |
| Session or invocation | Session 2026-06-15, continuation of P4A worker phase context |
| Working directory | d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF |
| Command or tool surface | Write, Edit, Bash (cp, python generate scripts) |
| Target paths | See Allowed Scope items 1-11 |
| Allowed scope source | GC-018: docs/baselines/CVF_GC018_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_2026-06-15.md |
| Before status evidence | AGENT_HANDOFF_V18 964L ACTIVE; CVF_SESSION_MEMORY.md 1112L; AGENTS.md 925L -- all advisory-exceeded |
| After status evidence | AGENT_HANDOFF_V19 151L ACTIVE; CVF_SESSION_MEMORY.md 167L; AGENTS.md 925L pointer-updated; ACTIVE_SESSION_STATE.json activeHandoff=AGENT_HANDOFF_V19_2026-06-15.md |
| Diff evidence | git status --short: 8 modified + 7 untracked = 15 changed paths |
| Approval boundary | Operator message 2026-06-15; GC-018 authorized; WORKER_MUST_NOT_COMMIT |
| Claim boundary | Session continuity compaction only; no runtime, no live, no provider, no public-sync |
| Agent type | Claude Sonnet 4.6 (claude-sonnet-4-6) |
| Invocation ID | Session 2026-06-15 / continuation from P4A context window |
| Expected manifest | `AGENT_HANDOFF_V18_2026-06-12.md`; `AGENT_HANDOFF_V19_2026-06-15.md`; `AGENTS.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`; `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/lastUpdated.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION_MEMORY.md`; `docs/baselines/CVF_GC018_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_2026-06-15.md`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/session-front-door-v19.json`; `docs/roadmaps/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_ROADMAP_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_FOR_CLAUDE_2026-06-15.md` |
| Actual changed set | `AGENT_HANDOFF_V18_2026-06-12.md`; `AGENT_HANDOFF_V19_2026-06-15.md`; `AGENTS.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`; `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/lastUpdated.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION_MEMORY.md`; `docs/baselines/CVF_GC018_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_2026-06-15.md`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/session-front-door-v19.json`; `docs/roadmaps/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_ROADMAP_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_FOR_CLAUDE_2026-06-15.md` |
| Manifest delta | MATCH -- expected manifest equals actual changed set (15 paths) |
