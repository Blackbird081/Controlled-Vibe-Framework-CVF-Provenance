# CVF CPG-2 CP2 Hard Gate Enforcement Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-05-31

## Purpose

Close CPG-2 after operator implementation authorization. CPG-2 is the bounded
runtime follow-up to CPG-1: it defines and implements a
reversible `connectionPointMode` for CP2 plan validation at the CVF-owned INT1
connection point.

Fresh GC-018, operator checkpoint, runtime implementation, focused tests, and
release-quality governance proof are satisfied.

## Scope / Target / Owner Boundary

Target contract candidate:

`cvf.connectionPointHardGateEnforcement.cpg2.v1`

Owner surface:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` only if MCP tool schema or
  registration text must expose the new mode.

Delivered implementation scope:

- Add a typed `connectionPointMode` vocabulary with `advisory` and `enforce`.
- Preserve current advisory behavior by default.
- In enforce mode, map CP2 advisory outcomes into a bounded progression
  decision for the owned MCP connection point.
- Add tests for default compatibility, allow, review-hold, reject-block,
  unsupported event, invalid mode, and `runtimeExecutionAuthorized=false`.
- Run release-quality live governance proof before any governance-behavior
  closure claim.

Forbidden scope:

- Do not edit web `/api/execute/route.ts`.
- Do not add CPG-3 `governanceTrace` receipt enrichment.
- Do not create outbound framework adapters.
- Do not claim universal bypass prevention outside the owned connection point.
- Do not change provider routing, prompts, model selection, memory behavior, or
  public-sync.

## Authorization / Decision

Decision: `CLOSED_PASS_BOUNDED`.

CPG-1 is closed. CPG-2 implementation proceeded after fresh CPG-2 GC-018 and
operator checkpoint. Release-quality governance proof completed and the
completion review records final bounded closure evidence.

## Predecessor Evidence

| Artifact | Path / commit | Disposition |
|---|---|---|
| CPG-1 completion | `docs/reviews/CVF_CPG1_INBOUND_EVENT_CONTRACT_GUARD_COMPLETION_2026-05-31.md` | ACCEPT |
| CPG-1 implementation anchor | `1ff0354c` | ACCEPT |
| Parent CPG roadmap | `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md` | ACCEPT |
| LHW21 connection point advisory wave | `docs/baselines/CVF_GC018_LHW21_INTEGRATION_CONNECTION_POINT_ADVISORY_WAVE_2026-05-31.md` | ACCEPT |

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| INT1 policy module exists | `EXISTS` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `INT1_CONTRACT` | INT1 policy module | ACCEPT |
| INT1 event allowlist exists | `VALUE_SET` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `INT1_ALLOWED_EVENT_TYPES` | INT1 policy module | ACCEPT: five dotted event values |
| CP2 validator exists | `EXISTS` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `validateInt1Plan` | INT1 policy module | ACCEPT |
| CP2 advisory decisions exist | `VALUE_SET` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `advisoryDecision` | `validateInt1Plan` | ACCEPT: `ALLOW_ADVISORY`, `REVIEW_RECOMMENDED`, `REJECT_ADVISORY` |
| CP2 currently returns literal runtime non-authorization | `LITERAL_INVARIANT` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `runtimeExecutionAuthorized` | `validateInt1Plan` | ACCEPT: literal `false` |
| Event emitter currently rejects unsupported events | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `emitInt1AgentEvent` | INT1 policy module | ACCEPT |
| MCP plan tool delegates to owner function | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | INT1 MCP tool registration | `cvf_validate_plan` | MCP server tool registry | ACCEPT |
| Existing focused INT1 tests cover advisory behavior | `EXISTS` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts` | test source file | `cvf_validate_plan` | INT1 adapter tests | ACCEPT |
| CPG-1 explicitly left CPG-2 open | `EXISTS` | `docs/reviews/CVF_CPG1_INBOUND_EVENT_CONTRACT_GUARD_COMPLETION_2026-05-31.md` | Finding-To-Governance Learning Disposition | `CPG-2` | CPG-1 completion review | ACCEPT |

## New Proposed Fields And Symbols

These CPG-2 names are now implemented in the owned INT1 MCP surface.

| Implemented item | Purpose | Runtime status now |
|---|---|---|
| `ConnectionPointMode` | Typed mode vocabulary: `advisory` or `enforce` | IMPLEMENTED |
| `connectionPointMode` | Optional input/config field for CP2 validation mode | IMPLEMENTED |
| `ConnectionPointProgressionDecision` | Structured output for allow/review-hold/block progression | IMPLEMENTED |
| `acceptedForProgression` | Boolean indicating whether owned connection-point progression may continue | IMPLEMENTED |

## Current Runtime Freshness Verification

CPG-2 built on the CPG-1 INT1 owner module and added a mode-controlled
progression decision without moving policy logic back into the MCP registry.

| Runtime fact | Current source checked | Freshness disposition |
|---|---|---|
| INT1 policy owner exists | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | EXISTS |
| Default behavior is advisory | `validateInt1Plan` in the policy module | Preserve default compatibility |
| MCP registration delegates to owner module | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | Exists; avoid regrowth if edited |
| Receipt enrichment is absent from CPG-2 scope | `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md` | CPG-3 only |

## Enforcement Semantics Draft

| Mode | Advisory outcome | CPG-2 progression decision | Runtime claim boundary |
|---|---|---|---|
| `advisory` | `ALLOW_ADVISORY` | allow advisory readout only | no behavior change |
| `advisory` | `REVIEW_RECOMMENDED` | recommend review only | no behavior change |
| `advisory` | `REJECT_ADVISORY` | reject advisory only | no behavior change |
| `enforce` | `ALLOW_ADVISORY` | allow owned connection-point progression | not provider execution authorization |
| `enforce` | `REVIEW_RECOMMENDED` | hold owned connection-point progression for review | no universal bypass claim |
| `enforce` | `REJECT_ADVISORY` | block owned connection-point progression | no universal bypass claim |

`runtimeExecutionAuthorized=false` must remain literal in CPG-2 outputs unless a
separate future roadmap changes that invariant.

## Tranche Plan

| Tranche | Status | Scope |
|---|---|---|
| CPG-2.A | PASS | Fresh GC-018, source verification, operator checkpoint |
| CPG-2.B | PASS | Typed mode and progression decision in INT1 owner module |
| CPG-2.C | PASS | MCP registration compatibility and focused tests |
| CPG-2.D | PASS | Release-quality live governance proof and completion review |

## Non-Goals

- No public-sync export.
- No web `/api/execute/route.ts` edit.
- No CPG-3 receipt enrichment.
- No provider routing, prompt, model, memory, or Learning Plane mutation.
- No framework-specific adapter.
- No public-sync export.
- No production, hosted, provider-quality, or universal bypass-prevention
  claim.

## Work Plan

| Step | Status | Output |
|---|---|---|
| 1. Stage roadmap and work order | PASS | This roadmap and the paired CPG-2 work order |
| 2. File fresh CPG-2 GC-018 | PASS | New GC-018 with current source verification |
| 3. Release operator checkpoint | PASS | Explicit operator approval for runtime implementation |
| 4. Implement bounded mode semantics | PASS | INT1 owner module and focused tests |
| 5. Close with live proof | PASS | Completion review plus release-quality governance bundle |

## Acceptance Criteria

| Criterion | Required disposition |
|---|---|
| Fresh CPG-2 GC-018 exists before implementation | PASS |
| Operator checkpoint is explicit | PASS |
| Default `advisory` mode preserves CPG-1 behavior | PASS |
| `enforce` mode maps allow/review/reject deterministically | PASS |
| Unsupported event rejection remains unchanged | PASS |
| `runtimeExecutionAuthorized=false` remains literal | PASS |
| MCP index does not grow without same-domain extraction/shrink evidence | PASS |
| Release-quality live governance bundle passes before closure claim | PASS |

## Verification / Evidence

Implementation evidence:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
npm run test:run -- src/tools/int1-adapter.test.ts
npm run build
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD
python scripts/run_cvf_release_gate_bundle.py --json
```

Final release bundle result: PASS, 7/7 checks passed.

## Fail Conditions

- `connectionPointMode` is described as an existing runtime field before
  implementation.
- `enforce` is allowed to authorize provider/runtime execution.
- `REVIEW_RECOMMENDED` is silently allowed in enforce mode without review hold.
- CPG-3 receipt fields appear in CPG-2 implementation.
- `index.ts` grows without maintainability evidence.
- Any direct MCP test is used as a substitute for release-quality live
  governance proof.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
|---|---|---|---|---|
| CP2 remains advisory after CPG-1 extraction | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `DESIGN_REVIEW_REQUIRED` | CPG-2 GC-018 must authorize bounded enforce semantics |
| Universal bypass prevention is not proven by MCP enforcement | `CLAIM_BOUNDARY_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `RULE_EXISTS` | Keep claim limited to owned connection point |
| MCP index is above soft threshold | `MAINTAINABILITY_GAP` | `GOVERNANCE_CONTROL_PLANE` | `PHASE_GATE_PLACEMENT_GAP` | Avoid regrowth; require file-size guard |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Private provenance closure only. Public-sync is not authorized.

## Claim Boundary

This roadmap closes bounded CPG-2 code and proof only. It does not prove
universal framework bypass prevention, modify receipts, change providers,
implement CPG-3, or publish public artifacts.
