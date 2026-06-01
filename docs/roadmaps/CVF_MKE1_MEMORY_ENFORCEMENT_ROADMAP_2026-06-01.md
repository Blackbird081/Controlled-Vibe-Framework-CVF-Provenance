# CVF MKE1 Memory Enforcement Roadmap

Memory class: FULL_RECORD

Status: PROPOSED

docType: roadmap

Date: 2026-06-01

## Purpose

Advance the Memory plane from advisory-only to governed enforcement. MKG7
delivered a bounded advisory surface — `memoryAdvisoryReadout` in the execute
response, a readout-eligibility policy, and a fail-closed durable store — but
none of these currently affect execution decisions. MKE1 wires the eligibility
signal into the enforcement gate, enables REVOKED/DENIED states to block
execution, and wires the durable write path into a governed route surface.

MKE1 starts from the MKG7 result (commit `7564f57b`): `memory-readout-
eligibility-policy.ts`, `buildMemoryAdvisoryReadout`, `durable-memory-store.ts`
(fail-closed write), and `route-memory-advisory.ts` (advisory attachment after
AI execution).

## Authorization / Decision

Authority:

- operator direction on 2026-06-01 to create a Memory Enforcement roadmap;
- `docs/reviews/CVF_MKG7_T7_MEMORY_LIVE_PROOF_DECISION_2026-06-01.md` — T7
  verdict: NO live proof required for advisory surface; enforcement requires
  a new GC-018;
- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` — T1
  contract: advisory-only execution boundary; enforcement requires separate
  authorization;
- `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md`
  — Non-Goal: "do not convert advisory Memory output into execution-policy
  enforcement in this roadmap unless a later GC-018 explicitly authorizes it."

This roadmap defines the authority path that enables tranche GC-018s to be
opened. The roadmap itself is not a GC-018 and does not authorize
implementation. Each tranche is blocked until its own GC-018 exists and is
marked AUTHORIZED_FOR_IMPLEMENTATION.

## Current State (Source-Verified at `7564f57b`)

### Existing surfaces

| Surface | File | Line | Current boundary |
| --- | --- | --- | --- |
| Eligibility evaluation | `memory-readout-eligibility-policy.ts:53` | `evaluateReadoutEligibility` | Returns state + reason; not wired into execution gate |
| Advisory attachment | `route.ts:822` | `buildMemoryAdvisoryReadout` | Runs **after** AI execution; cannot block |
| Enforcement gate | `route.ts:343` | `evaluateEnforcement` | Runs **before** AI execution; inputs: mode/content/budget/spec/risk/skill — **no memory signal** |
| Enforcement input | `enforcement.ts:34` | `EnforcementInput` | Extensible — optional fields; no `memoryEligibility` field yet |
| Durable store write | `durable-memory-store.ts:201` | `write` deny branch | Fail-closed; **not wired into any route** |
| Durable store read | `durable-memory-store.ts:308` | `read` deny branch | Fail-closed; **not wired into any route** |
| Route line count | `route.ts` | 860 lines | Hard limit 1000; helper extraction required before enforcement addition |

### Gap analysis

| Gap | Impact | MKE1 tranche |
| --- | --- | --- |
| REVOKED/DENIED eligibility does not block execution | Memory-revoked actors can execute governed routes | E1 |
| memoryAdvisoryReadout runs post-execution — cannot block | Advisory-only; no enforcement signal | E1 |
| EnforcementInput has no memory signal | Enforcement gate blind to memory state | E1 |
| Durable write/read not wired into any route | Memory persistence has no governed route surface | E2 |
| No live proof of enforcement behavior | Cannot claim governed Memory enforcement | E3 |

## Scope

In scope:

- add `memoryEligibility` signal to `EnforcementInput` (additive optional field);
- move eligibility evaluation **before** `evaluateEnforcement` call (line ~343);
- add `MEMORY_REVOKED` and `MEMORY_DENIED` as enforcement block reasons;
- extract a helper from `route.ts` if needed before adding enforcement logic;
- add a governed route surface for durable read/write (`POST /api/memory/write`);
- run a live governance proof once enforcement is wired;
- close MKE1 with a bounded completion review.

Out of scope:

- autonomous memory mutation without actor authorization;
- raw Memory content release;
- prompt injection or automatic reinjection;
- graph persistence mutation;
- new role taxonomy;
- public-sync or public README claims;
- production readiness or hosted readiness claims;
- enforcement of memory quality scoring (that is a Learning Plane concern).

## Non-Goals

- do not promote `memoryAdvisoryReadout` to an enforcement gate without a
  separate live proof;
- do not treat durable write as production-stable until live proof passes;
- do not add enforcement for memory tier quality or relevance score — that
  belongs in a Learning Plane enforcement roadmap;
- do not use operator silence as approval for live proof or public-sync.

## Tranche Plan

| Tranche | Name | Goal | Primary outputs | Status | Dependency |
| --- | --- | --- | --- | --- | --- |
| MKE1-E1 | Enforcement Gate Wire-In | Move eligibility evaluation before enforcement; add REVOKED/DENIED block signal to EnforcementInput | `enforcement.ts` delta, `route.ts` delta, helper extraction, focused tests | PROPOSED | none |
| MKE1-E2 | Durable Write Route | Add governed `POST /api/memory/write` route with actor authorization, provenance gate, and receipt | new route file, tests | PROPOSED | E1 non-live gates and tests PASS |
| MKE1-E3 | Live Governance Proof | Prove enforcement gate blocks REVOKED execution with live provider call | live proof receipt, completion review | PROPOSED | E1 + E2 complete |

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| M1.0 | Open GC-018 for MKE1-E1 | E1 baseline | PROPOSED |
| M1.1 | Extract route helper if route.ts growth needed | helper module, route shrinks | PROPOSED |
| M1.2 | Add `memoryEligibility` to `EnforcementInput`; move eligibility before enforcement gate | `enforcement.ts` + `route.ts` delta | PROPOSED |
| M1.3 | Add REVOKED/DENIED block path in enforcement | enforcement block reasons | PROPOSED |
| M1.4 | Focused tests: REVOKED blocks execution, ALLOWED proceeds, advisory preserved | test file | PROPOSED |
| M1.5 | Open GC-018 for MKE1-E2; add durable write route | `POST /api/memory/write` route + tests | PROPOSED |
| M1.6 | Open GC-018 for MKE1-E3; run live governance proof | live receipt, completion review | PROPOSED |

## Workstream Details

### MKE1-E1 Enforcement Gate Wire-In

**What changes:**

1. Add `memoryEligibility?: MemoryReadoutEligibilityResult` to `EnforcementInput`
   (`enforcement.ts:34`).
2. In `route.ts`, move `buildMemoryAdvisoryReadout` to run **before**
   `evaluateEnforcement` (currently line 343). Pass the eligibility result into
   `EnforcementInput`.
3. Add a block branch in `evaluateEnforcement` (or a wrapper) for states
   `REVOKED` and `READOUT_DENIED`: return `status: 'BLOCK'`, reason
   `memory_access_revoked` or `memory_readout_denied`.
4. Keep `STALE_NEEDS_REFRESH`, `NO_AUTHORITY_SOURCE`, `OUT_OF_SCOPE_FOR_ACTOR`
   as advisory-only (non-blocking) in E1 — a later tranche can harden these
   if authorized.

**File-size constraint:** `route.ts` is at 860 lines. Moving the eligibility
call earlier + adding an enforcement branch will add ~10–15 lines. If route
exceeds 870 lines, extract the memory pre-flight into a dedicated helper
(`route-memory-preflight.ts`) before adding enforcement logic.

**Safety invariants preserved:**
- `rawMemoryReleased: false` and `canReinject: false` on all memory surfaces;
- enforcement block returns `status 400` with governance receipt — same pattern
  as existing BLOCK path (lines 360–388);
- advisory readout still attached to ALLOW responses (it runs before enforcement
  now, so the advisory is available for both BLOCK and ALLOW response envelopes).

### MKE1-E2 Durable Write Route

Add `POST /api/memory/write` as a governed route:

- auth: service-token or session (same pattern as `/api/memory/readout`);
- body: actor, scope, tier, summary, provenanceScore, policyDecision,
  actorAuthorized;
- calls `DurableMemoryStore.write()` — the existing fail-closed path;
- returns `DurableMemoryReceipt` with `summaryOnly:true`,
  `rawMemoryReleased:false`, `canReinject:false`;
- no raw content intake — request body must not accept a `content` field.

Depends on E1 live proof to confirm enforcement gate is stable before adding a
write surface.

### MKE1-E3 Live Governance Proof

Run the release-quality governance bundle with a scenario where
`memoryEligibility.state === 'REVOKED'` causes execution to return BLOCK:

```powershell
python scripts/run_cvf_release_gate_bundle.py --json
```

Expected: live receipt proving the REVOKED → BLOCK path in a real governed
request. Standard: `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Pre-execution gate | eligibility evaluated before `evaluateEnforcement` call (line ~343) |
| REVOKED blocks | `state === 'REVOKED'` → `enforcement.status === 'BLOCK'`, reason `memory_access_revoked` |
| DENIED blocks | `state === 'READOUT_DENIED'` → `enforcement.status === 'BLOCK'`, reason `memory_readout_denied` |
| ALLOWED proceeds | `state === 'READOUT_ALLOWED'` → execution continues normally |
| Advisory preserved | `memoryAdvisoryReadout` still present in ALLOW response |
| Safety invariants | `rawMemoryReleased:false` and `canReinject:false` on all memory surfaces |
| Durable write route | `POST /api/memory/write` exists, authenticated, receipted, no raw content |
| Live proof | live receipt proves REVOKED → BLOCK with real provider |
| File-size | `route.ts` stays under 1000 lines; helpers extracted if needed |

## Source Verification Block (Roadmap-Level)

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `evaluateEnforcement` call position | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 343 | `evaluateEnforcement` | execute route | ACCEPT |
| `EnforcementInput` extensible | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` | lines 34–62 | `EnforcementInput` | `evaluateEnforcement` | ACCEPT |
| No memory field in EnforcementInput (field absent — new) | DOC_ONLY_NEW | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` | lines 34–62 | `EnforcementInput` | `EnforcementInput` | ACCEPT |
| `memoryAdvisoryReadout` runs post-execution | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 822 | `buildMemoryAdvisoryReadout` | execute route | ACCEPT |
| REVOKED state in eligibility policy | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts` | line 11 | `REVOKED` | `MemoryReadoutEligibilityState` | ACCEPT |
| READOUT_DENIED state | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts` | line 9 | `READOUT_DENIED` | `MemoryReadoutEligibilityState` | ACCEPT |
| Durable write not wired into execute route | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 89 | `DurableMemoryStore` | durable store | ACCEPT |
| Existing BLOCK pattern | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 360–388 | `enforcement` | `EnforcementResult` | ACCEPT |
| route.ts line count | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | physical count | 860 lines | execute route | ACCEPT |
| Live proof script | EXISTS | `scripts/run_cvf_release_gate_bundle.py` | top-level file | `run_cvf_release_gate_bundle` | release gate scripts | ACCEPT |

## Risk Register

| Risk | Control |
| --- | --- |
| Enforcement gate breaks existing ALLOW path | Focused regression tests: ALLOWED state → execution proceeds; full non-live suite must pass |
| Memory eligibility evaluated with empty candidates (no history) → wrong BLOCK | Eligibility with `authoritySourcePresent: false` → `NO_AUTHORITY_SOURCE` (non-blocking in E1); test this scenario explicitly |
| route.ts grows past maintainability threshold | Extract `route-memory-preflight.ts` helper before adding enforcement; gate on line count |
| Durable write route opens raw content intake | Request schema must not accept `content` field; test assertion required |
| Live proof reveals unexpected BLOCK cascade | Classify as `WORKER_EXECUTION_ERROR`; repair allowed-scope failure before marking live proof passed |

## Required Work Orders

Each tranche requires its own GC-018 + work order before implementation:

- `CVF_WO_MKE1_E1_MEMORY_ENFORCEMENT_GATE_WIREIN_2026-06-01.md`
- `CVF_WO_MKE1_E2_MEMORY_DURABLE_WRITE_ROUTE_2026-06-01.md`
- `CVF_WO_MKE1_E3_MEMORY_LIVE_GOVERNANCE_PROOF_2026-06-01.md`

## Verification / Evidence

Required phase gates, baseHead captured before each tranche:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/check_execute_route_step_sequence.py --enforce
python governance/compat/check_public_export_disposition.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base <baseHead> --head HEAD --enforce
```

E3 (live proof) additionally requires:

```powershell
python scripts/run_cvf_release_gate_bundle.py --json
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MKE1 is a private governance roadmap. No public-sync remote, public
repository commit, hosted proof, public artifact path, or public README claim
is included until E3 live proof passes and a separate public-sync tranche is
authorized.

## Claim Boundary

This roadmap authorizes planning for Memory enforcement only. It does not by
itself authorize live/provider proof, public-sync, raw Memory release, prompt
injection, Memory reinjection, graph mutation, autonomous durable mutation,
production readiness, hosted readiness, or public readiness. Each tranche
requires its own GC-018 before implementation begins.
