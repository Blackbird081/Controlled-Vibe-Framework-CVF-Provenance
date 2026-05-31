# CVF Agent Work Order - CPG-1 Inbound Event Contract Guard

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-31

## Purpose

Dispatch CPG-1 as a bounded semantic-preserving extraction: move INT1 inbound
event and advisory-plan policy out of the MCP registration file, wire the MCP
tools to the extracted module, and replace duplicated test helpers with direct
owner-module tests.

## Scope / Target / Owner Boundary

Target: `cvf.connectionPointEventContractGuard.cpg1.v1`.

Allowed scope:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts`
- `docs/work_orders/CVF_WO_CPG1_INBOUND_EVENT_CONTRACT_GUARD_2026-05-31.md`
- `docs/baselines/CVF_GC018_CPG1_INBOUND_EVENT_CONTRACT_GUARD_2026-05-31.md`
- `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- `docs/reviews/CVF_CPG1_INBOUND_EVENT_CONTRACT_GUARD_COMPLETION_2026-05-31.md`
- session continuity files only at closure

Forbidden scope:

- CPG-2 enforce-mode semantics or `connectionPointMode`
- CPG-3 receipt enrichment or `governanceTrace`
- framework-specific adapters
- public-sync changes, provider behavior changes, and production-readiness claims

Risk ceiling: R2.

## 1. Mission

Deliver a testable INT1 policy owner module while preserving the existing
advisory-only MCP behavior and dotted transport-event values.

## 2. Authority Chain

- Operator instruction: 2026-05-31 direct request to proceed with roadmap code.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Roadmap:
  `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- GC-018:
  `docs/baselines/CVF_GC018_CPG1_INBOUND_EVENT_CONTRACT_GUARD_2026-05-31.md`
- Active handoff: `AGENT_HANDOFF_V15_2026-05-29.md`

Authority boundary: CPG-2 and CPG-3 require separate closure prerequisites and
fresh dispatch packets.

## 3. Agent Roles

- Orchestrator / dispatcher: operator and Codex
- Implementer: Codex
- Reviewer: Codex self-review plus machine gates
- Operator approval required for: scope expansion, CPG-2, CPG-3, live proof,
  public-sync export, or claim expansion

## 4. Scope

Allowed and forbidden scope are binding as listed above.

## 5. Required First Reads

- `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- `docs/baselines/CVF_GC018_CPG1_INBOUND_EVENT_CONTRACT_GUARD_2026-05-31.md`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts`

## 6. Pre-Flight Checks

```powershell
git rev-parse --short HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base f032109b --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base f032109b --head HEAD
```

Expected: both autorun phases pass before runtime edits.

## 6A. Source-Fidelity Pass

Source Verification Block:

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| INT1 contract exists | `LITERAL_INVARIANT` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | line 1 | `INT1_CONTRACT` | INT1 policy module | ACCEPT: `cvf.genericMcpAdapter.int1.v1` |
| INT1 event allowlist exists | `VALUE_SET` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | lines 3-9 | `INT1_ALLOWED_EVENT_TYPES` | INT1 policy module | ACCEPT: five dotted event literals |
| Plan validator is advisory | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | lines 31-58 | `validateInt1Plan` | INT1 policy module | ACCEPT |
| Event emitter rejects unsupported types | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | lines 60-81 | `emitInt1AgentEvent` | INT1 policy module | ACCEPT |
| MCP registrations delegate to owner module | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | lines 771-805 | `cvf_validate_plan`, `cvf_emit_agent_event` | INT1 MCP tools | ACCEPT |

New Doc-Only Fields:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| `validateInt1Plan` | extracted owner helper | Yes | Delivered in CPG-1 | direct unit test PASS |
| `emitInt1AgentEvent` | extracted owner helper | Yes | Delivered in CPG-1 | direct unit test PASS |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Extract INT1 policy from `src/index.ts` | Execution Plan | `src/tools/int1-connection-point-policy.ts` | `Test-Path`; source review | PASS |
| Preserve dotted INT1 values | Acceptance Criteria | `INT1_ALLOWED_EVENT_TYPES` | direct tests | PASS |
| Preserve advisory behavior | Acceptance Criteria | `validateInt1Plan` | direct tests | PASS |
| Reject unsupported inbound event | Acceptance Criteria | `emitInt1AgentEvent` | direct tests | PASS |
| Avoid MCP index growth | Acceptance Criteria | `src/index.ts` | command-backed line count | PASS |
| Keep CPG-2 and CPG-3 held | Forbidden scope | no mode or receipt edits | `git diff --name-status` | PASS |

## 7. Write Ownership

Owned runtime files:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts`

Write mode: create one module and modify the two listed owner/test files.

## 8. Execution Plan

1. File baseline and this work order; run pre-dispatch and pre-implementation.
2. Extract pure policy functions and constants into the new same-domain module.
3. Wire MCP registration handlers through the module.
4. Replace duplicated test helpers with direct imports.
5. Run targeted tests, MCP build, file-size guard, and closure gates.

Stop if behavior changes beyond semantic preservation or any gate fails.

## Evidence Requirements

- `npm run test:run -- src/tools/int1-adapter.test.ts`
- `npm run build`
- `git diff --name-status`
- command-backed `src/index.ts` line count
- `python governance/compat/check_governed_file_size.py --enforce`

The command-backed evidence above is mandatory before closure. Direct
MCP tests prove only the bounded owner-module behavior; they do not prove
governed-route live enforcement.

## 10. Acceptance Criteria

- Extracted policy module exists.
- MCP handlers use the extracted owner functions.
- INT1 tests import owner functions and pass.
- All five supported events remain accepted.
- Unsupported event remains rejected.
- Plan outcomes remain `ALLOW_ADVISORY`, `REVIEW_RECOMMENDED`, or
  `REJECT_ADVISORY`.
- `runtimeExecutionAuthorized=false` remains literal in results.
- `src/index.ts` shrinks and does not grow.
- No CPG-2, CPG-3, public-sync, provider, or framework-adapter change appears.

Fail conditions:

- any enforce-mode behavior appears;
- any receipt runtime field changes;
- any framework-specific adapter appears;
- any gate fails;
- `src/index.ts` grows.

## 11. Review Gate

Implementation proceeds only after pre-dispatch and pre-implementation pass.
Closure requires targeted tests, MCP build, file-size guard, pre-closure gate,
and a bounded completion review.

## 12. Closure Checklist

| Item | Resolution |
| --- | --- |
| Acceptance criteria resolved before closed-equivalent status | SATISFIED |
| Required tests and evidence commands run | SATISFIED |
| Autorun pre-closure gate uses a non-empty committed range | SATISFIED after closure commit |
| Changed-file set stays inside allowed scope | SATISFIED |
| Roadmap-to-work-order trace matrix checked | SATISFIED |
| Public catalog update | N/A with reason: private provenance runtime hardening |
| Session front door, registry, and active handoff sync at closure | SATISFIED |

## Closure Evidence

| Evidence | Result |
| --- | --- |
| Implementation commit | `1ff0354c` |
| Targeted INT1 tests | PASS, `8/8` |
| MCP build | PASS |
| MCP full suite | PASS, `22` files and `554` tests |
| MCP index physical size | PASS, `917` to `873` lines |
| Governed file-size guard | PASS |
| Release-quality governed-route bundle | PASS, `7/7` after classified timeout isolation |
| Completion review | `docs/reviews/CVF_CPG1_INBOUND_EVENT_CONTRACT_GUARD_COMPLETION_2026-05-31.md` |

## 13. Return-To-Orchestrator Conditions

Return without continuing if any source fact, gate, ownership boundary, or
advisory-only invariant fails.

## Operator Checkpoint

SATISFIED_FOR_CPG1 on 2026-05-31: operator instructed Codex to proceed with
roadmap code. No waiver is granted for CPG-2, CPG-3, live-proof closure,
public-sync export, or claim expansion.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance CPG-1 runtime hardening. Public export requires a
separate curated public-sync work order.

## Claim Boundary

This work order authorizes semantic-preserving CPG-1 extraction and required
governed-route regression proof only. It does not authorize enforce mode,
receipt enrichment, provider-quality claims, public export, hosted readiness,
or production readiness.
