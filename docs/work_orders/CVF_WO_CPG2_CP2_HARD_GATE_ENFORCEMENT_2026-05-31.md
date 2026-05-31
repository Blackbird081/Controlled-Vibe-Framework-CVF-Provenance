# CVF Agent Work Order - CPG-2 CP2 Hard Gate Enforcement

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-31

## Purpose

Close the CPG-2 implementation packet after hold release. CPG-2 adds a bounded
`connectionPointMode` to CP2 plan
validation so the owned INT1 connection point can remain advisory by default
and optionally hold/block progression in enforce mode.

Fresh CPG-2 GC-018, explicit operator checkpoint, implementation, focused
tests, and release-quality governance proof are satisfied.

## Scope / Target / Owner Boundary

Target contract candidate:

`cvf.connectionPointHardGateEnforcement.cpg2.v1`

Allowed scope after hold release:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` only if exposing the mode
  through the MCP tool schema is unavoidable.
- CPG-2 GC-018 baseline, this work order, parent roadmap, completion review,
  and session continuity at closure.

Forbidden scope:

- CPG-3 receipt enrichment or `governanceTrace`.
- Web `/api/execute/route.ts`.
- Provider routing, prompts, model selection, memory behavior, or Learning
  Plane mutation.
- Framework-specific adapters or universal bypass-prevention claims.
- Public-sync changes.

Risk ceiling: R2-R3. Any expansion beyond the owned INT1 connection point
requires a new work order.

## Authority Chain

| Authority | Path / basis | Disposition |
|---|---|---|
| Operator instruction | 2026-05-31 request to stage CPG-2 while Claude executes LHW22-LHW24 | ACCEPT |
| CPG-2 roadmap | `docs/roadmaps/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_ROADMAP_2026-05-31.md` | ACCEPT |
| Parent CPG roadmap | `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md` | ACCEPT |
| CPG-1 completion | `docs/reviews/CVF_CPG1_INBOUND_EVENT_CONTRACT_GUARD_COMPLETION_2026-05-31.md` | ACCEPT |
| Fresh CPG-2 GC-018 | `docs/baselines/CVF_GC018_CPG2_CP2_HARD_GATE_ENFORCEMENT_2026-05-31.md` | ACCEPT |
| Operator checkpoint | 2026-05-31 operator authorized CPG-2 implementation from the staged packet | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
|---|---|---|
| Orchestrator | Release hold only after fresh GC-018 and operator checkpoint | No silent dispatch |
| Implementer | Add bounded mode semantics after hold release | Owned MCP connection point only |
| Reviewer | Verify default compatibility, enforce mapping, live proof, and claim boundary | No public or universal enforcement claim |

## Required First Reads

- `docs/roadmaps/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_ROADMAP_2026-05-31.md`
- `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- `docs/reviews/CVF_CPG1_INBOUND_EVENT_CONTRACT_GUARD_COMPLETION_2026-05-31.md`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- `governance/compat/check_work_order_dispatch_quality.py`

## Pre-Flight Checks

Initial hold was released for CPG-2 implementation. Closure is now backed by
release-quality governance proof.

After a fresh CPG-2 GC-018 and operator checkpoint exist, capture a non-empty
base and run:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| INT1 policy owner exists | `EXISTS` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `INT1_CONTRACT` | INT1 policy module | ACCEPT |
| CP2 validator exists | `EXISTS` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `validateInt1Plan` | INT1 policy module | ACCEPT |
| Current CP2 advisory decisions exist | `VALUE_SET` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `advisoryDecision` | `validateInt1Plan` | ACCEPT: `ALLOW_ADVISORY`, `REVIEW_RECOMMENDED`, `REJECT_ADVISORY` |
| Current CP2 result is not runtime execution authorization | `LITERAL_INVARIANT` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `runtimeExecutionAuthorized` | `validateInt1Plan` | ACCEPT: literal `false` |
| Current event allowlist exists | `VALUE_SET` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `INT1_ALLOWED_EVENT_TYPES` | INT1 policy module | ACCEPT: five dotted event values |
| Current event emitter rejects unsupported event types | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `emitInt1AgentEvent` | INT1 policy module | ACCEPT |
| MCP tool registration delegates to owner function | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | INT1 MCP registration | `cvf_validate_plan` | MCP server tool registry | ACCEPT |
| Existing tests cover advisory behavior | `EXISTS` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts` | test source file | `validateInt1Plan` | INT1 adapter test suite | ACCEPT |
| CPG-1 completion says CPG-2 remains future work | `EXISTS` | `docs/reviews/CVF_CPG1_INBOUND_EVENT_CONTRACT_GUARD_COMPLETION_2026-05-31.md` | Finding-To-Governance Learning Disposition | `CPG-2` | CPG-1 completion review | ACCEPT |

## New Doc-Only Fields

| Implemented field | Purpose | Source status | Runtime claim boundary | Validation evidence |
|---|---|---|---|---|
| `ConnectionPointMode` | `advisory` or `enforce` vocabulary | Implemented in CPG-2 owner module | Owned MCP connection point only | Focused INT1 tests |
| `connectionPointMode` | Input/config field for CP2 behavior | Implemented in CPG-2 owner module and MCP schema | Owned MCP connection point only | Default compatibility test |
| `acceptedForProgression` | Output decision for owned connection-point progression | Implemented in CPG-2 owner module | Not provider execution authorization | Enforce-mode allow/review/reject tests |

## Current Runtime Freshness Verification

Current CPG-2 source extends the INT1 owner module instead of reintroducing
inline MCP policy logic. The prior gap, a missing bounded mode-controlled
progression decision, is closed.

| Runtime surface | Current source checked | Freshness disposition |
|---|---|---|
| INT1 owner module | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | EXISTS |
| CP2 advisory validator | `validateInt1Plan` | EXISTS and remains default |
| MCP registration | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | Delegate exists; avoid regrowth |
| Focused tests | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts` | Extend in place |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence required |
|---|---|---|
| Fresh GC-018 before implementation | Require GC-018 before implementation | GC-018 path and operator checkpoint |
| Default advisory compatibility | Add tests preserving CPG-1 outputs | Focused test PASS |
| Enforce-mode deterministic mapping | Add mode/progression decision in owner module | Tests for allow/review/reject |
| No CPG-3 receipt enrichment | Forbid receipt field changes | `git diff --name-status` |
| No universal bypass claim | Claim boundary in completion review | Completion review text |
| Release-quality proof | Run release gate bundle | `python scripts/run_cvf_release_gate_bundle.py --json` PASS |

## Write Ownership

After hold release, the implementer may touch only the owner/test files listed
in Allowed scope plus CPG-2 governance artifacts. Any web route, receipt,
provider, public-sync, or unrelated code change returns the order to
Orchestrator.

## Execution Plan

1. Stop unless fresh CPG-2 GC-018 and operator checkpoint exist.
2. Capture `baseHead`; run pre-dispatch and pre-implementation autorun gates.
3. Add `ConnectionPointMode` and progression-decision output to the INT1 owner
   module with default `advisory` behavior.
4. If MCP schema exposure is required, edit `src/index.ts` minimally and keep
   file-size evidence.
5. Extend focused INT1 tests for default, enforce allow, enforce review-hold,
   enforce reject-block, unsupported event, invalid mode, and literal
   `runtimeExecutionAuthorized=false`.
6. Run targeted tests, MCP build, file-size guard, pre-closure gate, and the
   release-quality live governance bundle.
7. File completion review with claim boundary and public export disposition.

## Evidence Requirements

- `git diff --name-status <baseHead> HEAD`
- `npm run test:run -- src/tools/int1-adapter.test.ts`
- `npm run build`
- command-backed `src/index.ts` line count
- `python governance/compat/check_governed_file_size.py --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD`
- `python scripts/run_cvf_release_gate_bundle.py --json`

## Acceptance Criteria

| Criterion | Required disposition |
|---|---|
| Fresh CPG-2 GC-018 exists | PASS before implementation |
| Operator checkpoint exists | PASS before implementation |
| `advisory` default preserves CPG-1 behavior | PASS |
| `enforce` + `ALLOW_ADVISORY` allows owned progression | PASS |
| `enforce` + `REVIEW_RECOMMENDED` holds owned progression for review | PASS |
| `enforce` + `REJECT_ADVISORY` blocks owned progression | PASS |
| Unsupported event rejection remains unchanged | PASS |
| `runtimeExecutionAuthorized=false` remains literal | PASS |
| No receipt, route, provider, public-sync, or adapter change appears | PASS |

## Review Gate

The reviewer must reject closure if direct MCP tests are used as the only
governance-behavior proof, if enforce mode authorizes provider execution, if
review outcomes are silently allowed, or if the completion review claims
universal framework bypass prevention.

## Closure Checklist

| Item | Resolution |
|---|---|
| Fresh GC-018 verified | PASS |
| Operator checkpoint verified | PASS |
| Source Verification Block refreshed | PASS |
| Runtime freshness table refreshed | PASS |
| Closure Diff Gate completed | PASS |
| Release-quality live governance proof completed | PASS |

## Return-To-Orchestrator Conditions

Return any follow-up work if a source path differs, enforce semantics become
ambiguous, or implementation requires web route, receipt, provider,
public-sync, or framework-adapter changes.

## Operator Checkpoint

SATISFIED. The operator authorized CPG-2 implementation from the staged roadmap
and work order on 2026-05-31.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Private provenance closure only. No public-sync artifact or public
catalog claim is authorized.

## Claim Boundary

This work order closes bounded CPG-2 implementation only. It does not add
receipt trace fields, change provider behavior, authorize public-sync, prove
hosted/production readiness, or prove universal bypass-prevention claims.
