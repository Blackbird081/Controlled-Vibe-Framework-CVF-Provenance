# CVF Phase D — Full Roadmap For Codex

Memory class: FULL_RECORD
Status: HAND-OFF FROM CLAUDE TO CODEX

## Purpose

Hand the complete Phase D legacy absorption implementation to Codex as a
single self-contained roadmap. Codex must execute all five tranches in the
mandatory order below, file a fresh GC-018 before each tranche, commit
atomically after each step, and sync the V9 handoff after every commit.

Operator instruction (2026-05-18): complete all of Phase D in one pass,
one tranche at a time in dependency order, without stopping between tranches
except for the mandatory GC-018 pre-step.

## Authorization

This roadmap is authorized by:

- `docs/reviews/CVF_LEGACY_PHASE_C_GAP_TRIAGE_FOR_IMPLEMENTATION_2026-05-18.md`
- `docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`
- Operator instruction on 2026-05-18: "tạo roadmap chi tiết cho toàn bộ
  phase D để Codex làm 1 lần cho xong luôn"

Role/Permission tranche is ALREADY COMPLETE at commit `69016bb2`. Codex
starts at Tranche 2.

## Scope

In scope:

- Tranche 2 (ORCHESTRATOR): GAP-17.05-001, GAP-17.05-013
- Tranche 5 (Memory continuity): GAP-17.05-011, part of GAP-17.05-013,
  part of GAP-17.05-015
- Tranche 3 (Runtime workflow): GAP-17.05-004, GAP-17.05-010,
  GAP-17.05-012, GAP-17.05-013, GAP-17.05-015
- Tranche 4 (Provider method): GAP-17.05-009
- Phase D closure: update concept-axis matrix dispositions, update gap
  ledger dispositions, update handoff

Out of scope for ALL tranches:

- Changing public claims in the public catalog without updated live evidence
- Changing route/provider execution without explicit live proof requirement
  in the tranche GC-018
- Lifting `system_reconvergence_stop` — operator decision only
- Expanding beyond the four approved legacy folders
- Reopening F-1 output-quality parity tuning
- DS N≥14 and Track M (suspended)
- Claiming complete Agent OS or universal provider parity

## Non-Goals

This roadmap does not convert Phase D completion into an Agent OS claim,
a marketplace launch, a release gate change, or a new provider hub. Each
tranche is a contract or contract-local runtime slice only. Public catalog
rows may only be updated from `partially_absorbed` to a stronger claim
after deterministic tests pass AND live proof is run where required by the
tranche GC-018.

## Execution Rules (MANDATORY for every tranche)

1. **GC-018 first**: File the GC-018 baseline document BEFORE writing any
   implementation code. Path: `docs/baselines/CVF_GC018_LEGACY_<TRANCHE>_TRANCHE_2026-05-18.md`.
2. **Atomic commit per step**: Each step below is one commit. Do not batch
   two tranches into one commit.
3. **GC-020 after every commit**: After each commit, update `Current HEAD`
   and the HEAD log block in `AGENT_HANDOFF_V9_2026-05-18.md`, then commit
   the handoff update as a separate commit immediately.
4. **Hook chain clean**: Every commit (including handoff syncs) must pass
   `governance/compat/run_local_governance_hook_chain.py` without
   `--no-verify`. If the hook chain blocks, fix the root cause.
5. **Live proof discipline**: Run a live Alibaba or DeepSeek call only when
   the tranche GC-018 explicitly requires it. Do not run live calls for
   deterministic-only tranches.
6. **Disposition updates**: After completing a tranche, update the
   corresponding rows in `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`
   and the crosswalk table in
   `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`.
   Use only the six controlled dispositions: `absorbed`, `partially_absorbed`,
   `doc_only`, `not_absorbed`, `rejected_or_superseded`, `needs_gc018`.

## Dependency Order

```
Tranche 1 (Role/Permission) — DONE ✓ commit 69016bb2
    ↓
Tranche 2 (ORCHESTRATOR) — start here
    ↓
Tranche 5 (Memory continuity) — must decide scope before Tranche 3
    ↓
Tranche 3 (Runtime workflow) — needs Tranche 1 + Tranche 5 scope
    ↓
Tranche 4 (Provider method) — needs named consuming vertical slice
    ↓
Phase D closure
```

Tranche 4 dependency note: the "named consuming vertical slice" means a
concrete web UI feature or runtime call that specifically needs a new
provider method. If no such feature is selected by the time Tranches 2, 5,
and 3 are complete, Tranche 4 remains demand-gated and Codex must record
that fact in the closure packet rather than implementing a placeholder.

---

## Tranche 2 — ORCHESTRATOR

### GAPs covered

- GAP-17.05-001: ORCHESTRATOR role boundary is `doc_only`; missing
  mandatory worker-lane delegation, overreach guard, orchestrator task
  router.
- GAP-17.05-013: Async worker/subagent lifecycle is `needs_gc018`; missing
  canonical async ticket lifecycle, delegation receipts, scheduler contract.

### Matrix rows covered

3.1 ORCHESTRATOR role boundary, 3.2 Orchestration rules contract,
3.3 Reverse brief / solution bias guard, 4.3 Async worker ticket lifecycle,
5.3 Worker memory write restriction (partial — owned by this tranche's
delegation boundary, full absorption deferred to Tranche 5).

### Prerequisite check

Before filing GC-018 for this tranche, verify:
```powershell
Test-Path EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-permission.contract.ts
# must return True — confirms Tranche 1 landed
```

### Step 2.0 — File GC-018

Create `docs/baselines/CVF_GC018_LEGACY_ORCHESTRATOR_TRANCHE_2026-05-18.md`.

Required sections: Candidate ID, date, parent roadmap, proposed scope,
continuation class, quality-first decision, quality protection commitments,
why now, active-path impact, risk if deferred, live proof boundary (see
below), required evidence.

Live proof boundary for this tranche:
- Deterministic delegation and state tests are sufficient.
- Live proof is required ONLY if the tranche changes how the orchestrator
  issues a provider execution call. If the tranche is contract-local
  (delegation contract + overreach guard types), live proof is NOT required.
- Record the decision explicitly in the GC-018.

Acceptance criteria for this step: GC-018 file exists, hook chain PASS,
GC-020 handoff sync committed.

### Step 2.1 — Implement ORCHESTRATOR contract

Target package: `EXTENSIONS/CVF_GUARD_CONTRACT`

Files to create:
- `src/contracts/orchestrator.contract.ts` — defines:
  - `OrchestratorDelegationProfile`: which role IDs may delegate, to which
    worker role IDs, and under which conditions
  - `OrchestratorOverreachDenyRule`: vocabulary of forbidden orchestrator
    behaviors (recursive self-delegation, bypassing policy gate, exceeding
    worker-lane count)
  - `WorkerLaneTicket`: typed ticket shape for async worker hand-off,
    including `ticketId`, `delegatingRole`, `workerRole`, `receiptRequired`
  - `orchestratorCoversAllRoles(roles)`: coverage helper
- `src/contracts/contracts.phaseD-orchestrator.test.ts` — tests:
  - every ORCHESTRATOR-eligible role has a delegation profile
  - deny rules stay within vocabulary
  - ORCHESTRATOR may not self-delegate
  - BUILDER and AI_AGENT may not issue WorkerLaneTickets without a
    delegating ORCHESTRATOR
  - worker memory write restriction is flagged in the ticket type
- `src/contracts/index.ts` — re-export new types

GC-023 check before writing:
```powershell
(Get-Content EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts).Count
# must be under 1000 before adding exports; if close, create a
# dedicated barrel for Phase D exports
```

Acceptance criteria: tests pass, TypeScript check PASS, hook chain PASS,
concept-axis rows 3.1/3.2/4.3 disposition updated from `doc_only` /
`needs_gc018` to `absorbed` or `partially_absorbed` with delta note.

### Step 2.2 — File tranche completion packet

Create `docs/reviews/CVF_LEGACY_PHASE_D_ORCHESTRATOR_TRANCHE_COMPLETION_2026-05-18.md`.

Required sections: Purpose, Scope, Source (GC-018 path + implemented files
+ commit SHA), Findings/Position, Decision, Risk/Corrective Action,
Evidence Trace Block (4 claims minimum), Verification, Related Artifacts.

Evidence Trace Block must include:
- Fresh GC-018 existed before implementation → ACCEPTED
- Delegation profiles cover all ORCHESTRATOR-eligible roles → ACCEPTED
- Deny-rule vocabulary is typed and tested → ACCEPTED
- No live proof required (or: live proof run and PASS) → ACCEPTED

Update disposition in gap ledger crosswalk:
- GAP-17.05-001: change from `doc_only` to `partially_absorbed` (contract
  exists; runtime enforcement deferred to Tranche 3)
- GAP-17.05-013: change from `needs_gc018` to `partially_absorbed` (ticket
  type exists; full async lifecycle deferred to Tranche 3)

---

## Tranche 5 — Memory Continuity

### GAPs covered

- GAP-17.05-011: Governed persistent memory and reinjection are
  `needs_gc018`; missing privacy filtering, provenance scoring, controlled
  reinjection policy.
- Part of GAP-17.05-013: worker memory write restriction not absorbed.
- Part of GAP-17.05-015: memory-tier boundary missing from governance
  runtime.

### Matrix rows covered

5.1 Memory capture and retrieval policy, 5.2 Governed memory reinjection,
5.3 Worker memory write restriction.

### Why Tranche 5 before Tranche 3

Tranche 3 (Runtime workflow) depends on the memory boundary being defined
first. GAP-15 and GAP-13 both have partial memory-axis components.
Implementing runtime workflow before the memory owner boundary is set would
create overlapping contracts with unclear ownership.

### Prerequisite check

Before filing GC-018:
```powershell
Test-Path EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts
# must return True — confirms Tranche 2 landed
```

### Step 5.0 — File GC-018

Create `docs/baselines/CVF_GC018_LEGACY_MEMORY_CONTINUITY_TRANCHE_2026-05-18.md`.

Live proof boundary:
- Deterministic memory tests are sufficient for contract-local memory tier
  and reinjection policy typing.
- Live proof is required ONLY if reinjection changes governed AI output
  (i.e., if a memory record is injected into a live provider call in this
  tranche). If the tranche is contract-local types and deterministic tests
  only, live proof is NOT required.
- Record the decision explicitly.

### Step 5.1 — Implement Memory Continuity contract

Target package: `EXTENSIONS/CVF_GUARD_CONTRACT`

Files to create:
- `src/contracts/memory-continuity.contract.ts` — defines:
  - `MemoryTierOwner`: which role is authoritative for each memory tier
    (working / session / persistent / archive)
  - `MemoryReinjectionPolicy`: conditions under which a memory record may
    be reinjected into a new execution context; must include
    `privacyFilter`, `provenanceScoreThreshold`, `maxAgeSeconds`
  - `WorkerMemoryWriteRestriction`: typed deny rule — workers may not write
    to persistent or archive tiers without ORCHESTRATOR delegation receipt
  - `memoryContinuityCoversAllTiers(tiers)`: coverage helper
- `src/contracts/contracts.phaseD-memory-continuity.test.ts` — tests:
  - every memory tier has an owner role
  - reinjection policy fields are present and typed
  - worker write restriction fires for persistent/archive tiers
  - GOVERNOR role is the authoritative owner for archive tier
  - privacy filter field is required (non-optional)
- `src/contracts/index.ts` — re-export new types

Acceptance criteria: tests pass, TypeScript check PASS, hook chain PASS,
concept-axis rows 5.1/5.2/5.3 dispositions updated.

### Step 5.2 — File tranche completion packet

Create `docs/reviews/CVF_LEGACY_PHASE_D_MEMORY_CONTINUITY_TRANCHE_COMPLETION_2026-05-18.md`.

Evidence Trace Block minimum:
- Fresh GC-018 existed before implementation → ACCEPTED
- All memory tiers have owner boundaries → ACCEPTED
- Worker write restriction is typed and tested → ACCEPTED
- No live proof required (or: live proof PASS) → ACCEPTED

Update gap ledger crosswalk:
- GAP-17.05-011: change from `needs_gc018` to `partially_absorbed`
  (contract exists; runtime reinjection pipeline deferred to Tranche 3)
- Part of GAP-17.05-015 (memory axis): update delta note

---

## Tranche 3 — Runtime Workflow

### GAPs covered

- GAP-17.05-004: Phase 2.B runtime wire-up lacks owner-confirmed migration
  plan for state-machine and failure transitions.
- GAP-17.05-010: Legacy observability plane broader than current metrics.
- GAP-17.05-012: Tool, MCP, command, and database actions need canonical
  action vocabulary.
- GAP-17.05-013: Async worker/subagent scheduler and delegation lifecycle
  (partial — Tranche 2 covered contract types; this tranche covers runtime
  wiring).
- GAP-17.05-015: CVF Edit identifies runtime enforcement and state-machine
  hardening gaps.

### Matrix rows covered

4.1 State machine and failure transitions, 4.2 Guard runtime enforcement,
4.3 Async worker ticket lifecycle (runtime wiring), 7.1 Outcome workflow
chain, 7.2 External capability lifecycle, 9.2 Operational benchmark
extension, 9.3 Deterministic failure simulation suite, 10.2 Deliverable
pack evidence export.

### Prerequisite check

Before filing GC-018:
```powershell
Test-Path EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts
Test-Path EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts
# both must return True
```

### Step 3.0 — File GC-018

Create `docs/baselines/CVF_GC018_LEGACY_RUNTIME_WORKFLOW_TRANCHE_2026-05-18.md`.

This is the largest tranche. The GC-018 must specify which sub-items are
contract-local (deterministic tests only) versus which require live proof.

Live proof boundary (must be explicit in GC-018):
- State-machine contract extensions and failure simulation test suites:
  deterministic only, no live proof required.
- Guard runtime enforcement changes that affect how a governed AI call is
  dispatched: live proof required (Alibaba or DeepSeek call through the
  guard path, receipt emitted, gate outcome recorded).
- Tool/MCP action vocabulary additions: deterministic only unless a new
  tool call is added to the live execution path.
- Operational benchmark extension: deterministic tests for schema; live
  proof only if new metrics are emitted in a live governed call.

The GC-018 must declare whether live proof is required and which test or
call proves it. Codex may split the sub-items into a deterministic-only
portion and a live-proof portion, but must file a single GC-018 for the
tranche.

### Step 3.1 — Implement Runtime Workflow contract

Target packages: `EXTENSIONS/CVF_GUARD_CONTRACT`,
`EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL` (extend, do not
overwrite frozen surfaces).

Files to create or extend:
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts`
  — defines:
  - `RuntimeFailureState`: vocabulary of CVF runtime failure states
    (policy_denied, gate_timeout, provider_error, worker_overreach,
    memory_write_violation, receipt_missing)
  - `GuardEnforcementPoint`: where in the execution path each guard fires
    (intake / design / build / review / freeze)
  - `ToolActionClass`: canonical vocabulary for tool/MCP/command/database
    action types
  - `WorkflowTransition`: typed state machine edge (fromState, toState,
    trigger, receiptRequired)
  - `OperationalBenchmarkExtension`: schema for additional metrics beyond
    the bounded Phase 3.E pilot (defines fields; does not wire live emission)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phaseD-runtime-workflow.test.ts`
  — tests:
  - all failure states are in vocabulary
  - all guard enforcement points are named
  - tool action class vocabulary is exhaustive for current CVF surfaces
  - workflow transition receipts are required for mutation/approval
    transitions
  - failure simulation: given a `worker_overreach` event, transition to
    denied state and require receipt
  - failure simulation: given a `memory_write_violation`, transition to
    denied state
- `src/contracts/index.ts` — re-export

If live proof is required per GC-018: run one governed Alibaba or DeepSeek
call through the updated guard enforcement path, emit at least one new
OperationalBenchmarkExtension metric, record the receipt. Append the live
call result to the completion packet Evidence Trace Block.

GC-023 check before writing:
```powershell
(Get-Content EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts).Count
# if ≥ 900 lines, extract Phase D exports to a dedicated barrel file
# EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/phaseD.exports.ts
# and re-export from index.ts
```

Acceptance criteria: tests pass, TypeScript check PASS, hook chain PASS,
concept-axis rows 4.1/4.2/7.1/9.2/9.3 dispositions updated.

### Step 3.2 — File tranche completion packet

Create `docs/reviews/CVF_LEGACY_PHASE_D_RUNTIME_WORKFLOW_TRANCHE_COMPLETION_2026-05-18.md`.

Evidence Trace Block minimum:
- Fresh GC-018 existed before implementation → ACCEPTED
- Failure state vocabulary is exhaustive for current CVF paths → ACCEPTED
- Guard enforcement points are named and tested → ACCEPTED
- Tool action class vocabulary typed → ACCEPTED
- Live proof result (or: not required per GC-018 decision) → ACCEPTED

Update gap ledger crosswalk:
- GAP-17.05-004: `partially_absorbed` → `absorbed` if contract covers all
  current Phase 2.B wire-up paths; otherwise remain `partially_absorbed`
  with updated delta note
- GAP-17.05-010: update disposition and delta note
- GAP-17.05-012: `needs_gc018` → `partially_absorbed` (vocabulary defined;
  enforcement runtime deferred if no live path changed)
- GAP-17.05-015: `partially_absorbed` → `absorbed` if state-machine and
  guard enforcement are both covered

---

## Tranche 4 — Provider Method

### GAPs covered

- GAP-17.05-009: Phase 4.T1/T2 provider methods are demand-gated; missing
  first-class provider method coverage and CLI/job lifecycle semantics.

### Matrix rows covered

6.1 Provider output contract, 6.2 Provider registry/quota/routing/fallback,
6.3 Stream/tool/JSON/vision/embedding/reasoning methods.

### Dependency: named consuming vertical slice

This tranche cannot begin until a concrete web UI feature or runtime call
explicitly needs a new provider method. The following conditions both apply:

1. A specific provider method (stream, vision, embedding, reasoning, or a
   new model endpoint) must be selected.
2. A specific consuming vertical slice (a page, an API route, or a runtime
   job) must be named.

If no vertical slice has been selected by the time Tranches 2, 5, and 3
are complete, Codex must:

- Record that fact in the Phase D closure packet.
- Set GAP-17.05-009 disposition to remain `needs_gc018` with a note
  "demand-gated: no consuming slice selected as of 2026-05-18".
- Do NOT implement a placeholder provider method just to close the tranche.

### If a consuming slice IS available

Step 4.0 — File GC-018:
`docs/baselines/CVF_GC018_LEGACY_PROVIDER_METHOD_TRANCHE_2026-05-18.md`

The GC-018 must name:
- The specific provider method being added.
- The consuming vertical slice that needs it.
- Live proof requirement: REQUIRED — a new provider method that affects
  governed execution must be demonstrated with a live provider call
  through the governed path, with receipt emitted and gate outcome
  recorded.

Step 4.1 — Implement:
Extend `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts` to
add the new method type. Add a governed route or runtime handler for the
consuming slice. Run live proof.

Step 4.2 — File completion packet:
`docs/reviews/CVF_LEGACY_PHASE_D_PROVIDER_METHOD_TRANCHE_COMPLETION_2026-05-18.md`

Update gap ledger: GAP-17.05-009 disposition from `needs_gc018` to
`partially_absorbed` (one method added; universal parity not claimed).

---

## Phase D Closure

After all applicable tranches are complete (Tranches 2, 5, 3, and 4 if
unlocked), file a single closure packet:

### Step D.CLOSE — File Phase D closure packet

Create `docs/reviews/CVF_LEGACY_PHASE_D_CLOSURE_2026-05-18.md`.

Required sections:

**Summary table** — one row per tranche:

| Tranche | Status | Commit | Live proof | GAPs closed |
|---|---|---|---|---|
| Role/Permission | COMPLETE | 69016bb2 | not required | GAP-002 (partial) |
| ORCHESTRATOR | COMPLETE | <SHA> | <result> | GAP-001 (partial), GAP-013 (partial) |
| Memory continuity | COMPLETE | <SHA> | <result> | GAP-011 (partial), GAP-013 (partial) |
| Runtime workflow | COMPLETE | <SHA> | <result> | GAP-004, GAP-010, GAP-012, GAP-015 |
| Provider method | COMPLETE or DEMAND-GATED | <SHA or n/a> | <result or n/a> | GAP-009 |

**Concept-axis matrix final disposition pass** — verify every Phase D
matrix row is no longer `needs_gc018`. Any row still `needs_gc018` after
all tranches must be explained with a note.

**Gap ledger crosswalk final pass** — verify no Phase D GAP remains
`needs_gc018` without an explicit deferral note and reason.

**Claim boundary update** — update the Technical Product Catalog rows for:
- "Role and agent governance": `partially absorbed` → `absorbed` (if
  Tranche 2 covered all matrix rows) or update the evidence link.
- "Memory and continuity": update evidence link to include
  memory-continuity contract.
- "Operational observability": update evidence link if runtime workflow
  tranche extended the schema.
- Do NOT upgrade any row to `proven` without live proof.
- Run `Test-Path` on all catalog paths in public-sync before committing.

**Evidence Trace Block minimum (6 claims):**
1. All Phase D tranches have GC-018 before implementation → ACCEPTED
2. No public claim was changed without live proof → ACCEPTED
3. system_reconvergence_stop posture unchanged → ACCEPTED
4. Concept-axis matrix has no `needs_gc018` rows without deferral note → ACCEPTED
5. Gap ledger crosswalk is consistent with matrix dispositions → ACCEPTED
6. Public catalog Test-Path verification passes in public-sync → ACCEPTED

**GC-020 handoff sync**: after the closure commit, update V9 Current HEAD
and HEAD log block, commit the handoff sync as a separate commit, verify
`python governance/compat/check_active_session_state.py --enforce` shows
COMPLIANT.

---

## Forbidden Moves (apply to the entire Phase D roadmap)

- Do NOT promote any private legacy source file into the public repository.
- Do NOT implement a tranche without a pre-existing GC-018 for that tranche.
- Do NOT use `--no-verify` on any commit. If the hook chain blocks, fix the
  root cause.
- Do NOT bump or extend the `route.ts` RESOLVED exception entry. It is a
  tombstone.
- Do NOT change the GA_LOCAL_FIRST_APPROVED posture.
- Do NOT reopen F-1 output-quality parity tuning.
- Do NOT change public claims in the catalog without live or deterministic
  proof for the specific claim row.
- Do NOT claim ORCHESTRATOR or memory continuity as "fully absorbed" after
  the contract-local tranches — use `partially_absorbed` until a runtime
  path enforces the contract.
- Do NOT start Tranche 4 unless a named consuming vertical slice exists.
  Record demand-gated status in the closure packet instead.

## Verification Commands (run after each tranche)

```bash
# TypeScript check (run from guard contract dir)
cd EXTENSIONS/CVF_GUARD_CONTRACT && npm run check

# Unit tests (run from guard contract dir)
npm run test -- --run src/contracts/contracts.phaseD-<tranche>.test.ts

# Governance compat
python governance/compat/check_active_session_state.py --enforce
python governance/compat/check_docs_governance_compat.py --base HEAD --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce

# File size guard
python governance/compat/check_governed_file_size_compat.py --base HEAD --head HEAD --enforce

# Handoff guard (after GC-020 sync)
python governance/compat/check_agent_handoff_guard_compat.py --base HEAD~1 --head HEAD --enforce
```

For tranches requiring live proof:
```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

## Work Plan

See the five tranche sections above: Tranche 2 (ORCHESTRATOR), Tranche 5
(Memory continuity), Tranche 3 (Runtime workflow), Tranche 4 (Provider
method), and Phase D closure. Each tranche follows the same pattern:
file GC-018 → implement contract → file completion packet → update matrix
and ledger dispositions → GC-020 handoff sync.

## Acceptance Criteria

Phase D is complete when all of the following hold:

- Tranche 2 (ORCHESTRATOR) completion packet exists and tests pass.
- Tranche 5 (Memory continuity) completion packet exists and tests pass.
- Tranche 3 (Runtime workflow) completion packet exists and tests pass.
- Tranche 4 (Provider method) completion packet exists, or the closure
  packet records it as demand-gated with explicit reason.
- Concept-axis matrix has no `needs_gc018` row without a deferral note.
- Gap ledger crosswalk dispositions are consistent with the matrix.
- Public catalog claim rows are updated only where evidence supports the
  change; Test-Path verification passes 100% in public-sync.
- `system_reconvergence_stop` posture is unchanged.
- No public claim changed without live or deterministic proof.
- Phase D closure packet exists with a 6-claim Evidence Trace Block.
- `python governance/compat/check_active_session_state.py --enforce` shows
  COMPLIANT at the final handoff sync commit.

## Related Artifacts

- `docs/reviews/CVF_LEGACY_PHASE_C_GAP_TRIAGE_FOR_IMPLEMENTATION_2026-05-18.md`
- `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`
- `docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`
- `docs/baselines/CVF_GC018_LEGACY_ROLE_PERMISSION_TRANCHE_2026-05-18.md`
- `docs/reviews/CVF_LEGACY_PHASE_D_ROLE_PERMISSION_TRANCHE_COMPLETION_2026-05-18.md`
- `AGENT_HANDOFF_V9_2026-05-18.md`
