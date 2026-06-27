# CVF GC-018: DSCP-T3 Runtime Pilot (CPF Internal)

Memory class: FULL_RECORD

Status: ACTIVE_BASELINE

docType: gc018_baseline

Date: 2026-06-07

GC-018 control: `docs/reference/CVF_GC018_GOVERNANCE_CONTROL_STANDARD.md`

dispatchBaseHead: `fda6eff4`

---

## Proposed Tranche

DSCP-T3: Runtime Pilot (CPF Internal domain).

Predecessor: DSCP-T2 Standard Contract Authoring (`CLOSED_PASS_BOUNDED` at
`932a40aa`). DSCP-T3 wires the T2 type contracts into a deterministic
runtime function inside `CVF_CONTROL_PLANE_FOUNDATION`, using the existing
`ContextPackagerContract.pack()` as the inner engine. No provider call,
no corpus ingestion, no public/production readiness claim.

## Purpose

GC-018 authorization for DSCP-T3: implement a `GovernedContextPackerContract`
runtime class in `CVF_CONTROL_PLANE_FOUNDATION` that:

1. Accepts a `GovernedContextPackRequest` (T2 contract).
2. Validates governance envelope gates before packing.
3. Calls `ContextPackagerContract.pack()` with the inner `packRequest`.
4. Returns a `GovernedContextPackage` (T2 contract) with governance evidence.

Proof is deterministic vitest - fixed fixture in, assert output shape and
governance lock fields. No live provider, DashScope, or Alibaba API call.

---

## Authorization

Operator authorized DSCP-T3 CPF internal runtime pilot on 2026-06-07.

Predecessor evidence:
- DSCP-T1: `CLOSED_PASS_BOUNDED` at `62fa6943`
- DSCP-T2: `CLOSED_PASS_BOUNDED` at `932a40aa`
- Session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json` (key `dscpT2StandardContractAuthoring`)

Active handoff: `AGENT_HANDOFF_V17_2026-06-07.md`

## Scope

### In Scope

- New file: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts`
  - `GovernedContextPackerContract` class with `pack()` method
  - `createGovernedContextPackerContract()` factory function
  - Gate enforcement: `classificationGate` and `freshnessGate` must be `PASS`
    before calling inner `ContextPackagerContract.pack()`
  - On gate failure: return blocked result with `governanceOutcome: "BLOCKED"`
    instead of calling the inner packager

- New file: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.packer.test.ts`
  - Deterministic vitest: fixed `GovernedContextPackRequest` fixture
  - Assert `GovernedContextPackage.innerPackage` shape
  - Assert `GovernedContextPackage.governanceEvidence` block:
    - `rawContentReleased: false`
    - `canBypassGovernance: false`
    - `classificationGate: "PASS"`
    - `freshnessGate: "PASS"` 
  - Assert gate-blocked path: BLOCKED envelope -> returns blocked result without calling inner packager

### Non-Goals

- No provider API call (DashScope, Alibaba, OpenAI, DeepSeek).
- No corpus ingestion or body extraction.
- No modification of existing `.ts` files (CPF or any other module).
- No export added to any `index.ts` barrel.
- No DSCP-T3 receipt runtime (GovernedRetrievalReceipt instantiation at
  runtime is NOT in scope; contracts only covered by T2 tests).
- No public-sync, no production readiness, no public readiness claim.
- No LPCI2 T12 promotion.
- No session continuity mutation by worker.

## Acceptance Criteria

1. `dscp.governed.context.packer.ts` created: `GovernedContextPackerContract.pack()` compiles and all acceptance paths covered.
2. `pack()` returns `GovernedContextPackage` with `governanceEvidence.rawContentReleased === false` and `governanceEvidence.canBypassGovernance === false`.
3. Gate-blocked path tested: when `classificationGate !== "PASS"` OR `freshnessGate !== "PASS"`, `pack()` must NOT call `ContextPackagerContract.pack()` and must return a blocked-equivalent result.
4. `tsc --noEmit` PASS in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/` with zero errors.
5. All vitest tests PASS (target: 10 or more deterministic tests).
6. No existing `.ts` file modified.
7. All four governance component gates PASS on committed range.
8. Worker return packet present with all required evidence.

## Predecessor Evidence

| Predecessor | Path | Status |
|---|---|---|
| DSCP-T1 schema proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | CLOSED_PASS_BOUNDED |
| DSCP-T2 contracts | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | CLOSED_PASS_BOUNDED at 932a40aa |
| DSCP-T2 tests | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.contract.test.ts` | CLOSED_PASS_BOUNDED at 932a40aa |
| CPF ContextPackagerContract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | ACTIVE (existing CPF) |
| DSCP roadmap | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | DSCP-T3 row NOT_YET_AUTHORIZED; this GC-018 authorizes T3 |

## Evidence

- Source verification: work order Section 6A table
- TypeScript compilation: `tsc --noEmit` in CPF directory
- Deterministic vitest: pass count / total count in worker return
- Governance gates: Worker Pending-Return Gate table in worker return
- No existing file modified: `git status --short` output in worker return

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_FOR_CLAUDE_2026-06-07.md` | DISPATCHED at baseline publication; reviewer updates to CLOSED_PASS_BOUNDED | BLOCKED with reason: not yet dispatched |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_COMPLETION_2026-06-07.md` | reviewer-owned; pending after worker return | BLOCKED with reason: not yet dispatched |
| Roadmap state | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | DSCP-T3 row updated to CLOSED_PASS_BOUNDED after reviewer commit | BLOCKED with reason: not yet dispatched |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | session sync by reviewer/committer | BLOCKED with reason: not yet dispatched |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | session markdown by reviewer/committer | BLOCKED with reason: not yet dispatched |
| External evidence digest | TypeScript compilation + vitest results | tsc + vitest PASS in worker return | BLOCKED with reason: not yet dispatched |
| System loop interlock | no system-loop mutation authorized | DSCP-T3 is governed runtime call wrapper only | N/A with reason: no system-loop mutation authorized |
| Session continuity | `CVF_SESSION_MEMORY.md` and active handoff | reviewer-owned | BLOCKED with reason: not yet dispatched |

## Claim Boundary

This GC-018 baseline claims: authorization for DSCP-T3 governed runtime
wrapper authoring bounded to two new files in
`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`. It does not claim: provider
API quality, corpus ingestion, retrieval receipt runtime, public-sync,
production readiness, or public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; no public-sync, public catalog update,
or public artifact export authorized at this stage.
