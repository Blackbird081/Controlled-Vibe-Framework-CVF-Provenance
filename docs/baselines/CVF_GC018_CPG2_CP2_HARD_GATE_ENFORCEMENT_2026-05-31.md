# CVF GC-018 Continuation Candidate

## CPG-2 CP2 Hard Gate Enforcement

Memory class: BASELINE_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-31

---

## Purpose

Authorize the bounded CPG-2 follow-up to CPG-1: add a typed `connectionPointMode` vocabulary and enforce-mode progression decision for CP2 plan validation at the CVF-owned INT1 connection point. Default behavior stays advisory; enforce mode must hold or block only the owned connection-point progression and must not authorize provider execution.

## Scope / Target / Owner Boundary

Target contract: `cvf.connectionPointHardGateEnforcement.cpg2.v1`.

Owner: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` (INT1 owner module + focused tests; MCP index only if schema exposure is unavoidable).

Allowed runtime change:

- add `ConnectionPointMode` vocabulary (`advisory`, `enforce`) with default advisory;
- add `connectionPointMode` input and bounded progression decision output to `validateInt1Plan` return type;
- preserve current advisory readout structure and `runtimeExecutionAuthorized=false` literal;
- map enforce mode outcomes: allow progression, review hold, block progression;
- extend `src/tools/int1-adapter.test.ts` for default, enforce-allow, enforce-review-hold, enforce-reject, unsupported event, invalid mode, and literal runtimeExecutionAuthorized=false;
- adjust `src/index.ts` only if MCP schema must surface the new mode, with same-domain size discipline.

Forbidden scope:

- no CPG-3 `governanceTrace` receipt enrichment;
- no web `/api/execute/route.ts` changes;
- no provider routing, prompt, model, memory, or Learning Plane mutation;
- no framework-specific adapters or universal bypass-prevention claims;
- no public-sync changes or production/hosted readiness claims.

## Source / Predecessor Evidence

- CPG-2 roadmap: `docs/roadmaps/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_ROADMAP_2026-05-31.md`
- CPG-2 work order: `docs/work_orders/CVF_WO_CPG2_CP2_HARD_GATE_ENFORCEMENT_2026-05-31.md`
- Parent CPG roadmap: `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- CPG-1 completion: `docs/reviews/CVF_CPG1_INBOUND_EVENT_CONTRACT_GUARD_COMPLETION_2026-05-31.md`
- Current owner module: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts`
- MCP registration: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- Focused tests: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts`

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| INT1 policy owner exists | `EXISTS` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `INT1_CONTRACT` | INT1 policy module | ACCEPT |
| CP2 advisory decisions exist | `VALUE_SET` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `advisoryDecision` | `validateInt1Plan` | ACCEPT: `ALLOW_ADVISORY`, `REVIEW_RECOMMENDED`, `REJECT_ADVISORY` |
| CP2 currently returns literal runtime non-authorization | `LITERAL_INVARIANT` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `runtimeExecutionAuthorized` | `validateInt1Plan` | ACCEPT: literal `false` |
| Event emitter rejects unsupported events | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-connection-point-policy.ts` | runtime source file | `emitInt1AgentEvent` | INT1 policy module | ACCEPT |
| MCP plan tool delegates to owner function | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | INT1 MCP tool registration | `cvf_validate_plan` | MCP server tool registry | ACCEPT |
| Existing focused INT1 tests cover advisory behavior | `EXISTS` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts` | test source file | `validateInt1Plan` | INT1 adapter tests | ACCEPT |
| CPG-1 completion leaves CPG-2 open | `EXISTS` | `docs/reviews/CVF_CPG1_INBOUND_EVENT_CONTRACT_GUARD_COMPLETION_2026-05-31.md` | Finding-To-Governance Learning Disposition | `CPG-2` | CPG-1 completion review | ACCEPT |

## New Proposed Fields And Symbols

| Proposed item | Intended owner | Purpose | Runtime status now |
| --- | --- | --- | --- |
| `ConnectionPointMode` | `src/tools/int1-connection-point-policy.ts` | Mode vocabulary: `advisory` (default) or `enforce` | DOC_ONLY_NEW |
| `connectionPointMode` | `src/tools/int1-connection-point-policy.ts` (input/return) | Optional mode selector for CP2 validation | DOC_ONLY_NEW |
| `ConnectionPointProgressionDecision` | `src/tools/int1-connection-point-policy.ts` | Structured progression decision for enforce mode | DOC_ONLY_NEW |
| `acceptedForProgression` | `src/tools/int1-connection-point-policy.ts` | Boolean indicating owned connection-point progression allowance | DOC_ONLY_NEW |

## Knowledge Absorption Blind-Spot Control Block

- Standard read: `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory: CPG-2 roadmap, CPG-2 work order, CPG-1 completion, INT1 owner module, MCP registration, INT1 focused tests, LHW21 T2 hard-gate advisory spec.
- Prior absorption evidence resolved: LHW21 GC-018 and connector specs already absorbed via CPG-1.
- Detailed source files used: `src/tools/int1-connection-point-policy.ts`, `src/index.ts`, `src/tools/int1-adapter.test.ts`.
- Source families skipped: CPG-3 receipt enrichment, web route, provider routing, and framework adapters — deferred per roadmap/work order non-goals.
- File-level accepted value: CP2 advisory outputs are preserved; enforcement adds only bounded progression decisions and keeps `runtimeExecutionAuthorized=false` literal.
- Owner-surface normalization: enforce mode stays in the INT1 owner module; MCP index touched only if schema exposure is unavoidable with same-domain shrink evidence.
- Accept/defer/reject matrix: enforce-mode progression mapping ACCEPT_NOW; schema exposure DEFER_MAINTAINABILITY_BOUNDARY; receipt enrichment REJECT_FOR_SCOPE (CPG-3); provider/public claims REJECT_FOR_SCOPE.
- Adversarial roles completed: Implementer (bounded enforcement in owner), Skeptic/Auditor (no provider authorization, default compatibility preserved), Product/Operator Advocate (progression decision explicit), Safety/Boundary Owner (runtimeExecutionAuthorized remains false; owned connection point only).
- Thin proof target: updated owner module + focused tests + MCP build + release governance bundle.
- Blind-spot verdict: CLEAR for bounded CP2 enforcement; live/provider claims remain out-of-scope and guarded by release proof requirement.

## GC-018 Continuation Candidate

- Candidate ID: `gc018-cpg2-cp2-hard-gate-enforcement-2026-05-31`
- Parent roadmap / wave: `docs/roadmaps/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_ROADMAP_2026-05-31.md`
- Proposed scope: add typed `connectionPointMode` with enforce-mode progression decision in the INT1 owner module; preserve advisory default; extend focused tests; adjust MCP schema only if required.
- Continuation class: REALIZATION
- Active quality assessment: LHW21 T2 hard-gate advisory + CPG-1 runtime extraction already pass.
- Assessment date: 2026-05-31
- Weighted total: 9/10
- Lowest dimension: portfolio priority (1/2)
- Quality-first decision: EXPAND_NOW (bounded enforcement within owned INT1 connection point)
- Why expansion is the better move now: enables enforce-mode progression control without changing provider routing or receipts; leverages existing owner module and tests.
- Quality protection commitments: preserve advisory behavior, keep `runtimeExecutionAuthorized=false`, avoid MCP index regrowth unless schema exposure is unavoidable, forbid CPG-3 fields.
- Active-path impact: LIMITED
- Risk if deferred: connection-point progression remains advisory-only; enforce-mode guard remains undefined; roadmap/work-order hold blocks CP2 hard gate.
- Lateral alternative considered: YES
- Why not lateral shift: receipt enrichment and public claims belong to CPG-3; current need is bounded CP2 enforce semantics.
- Expected enforcement class: RUNTIME_GUARD (owned connection-point progression only)
- Required evidence if approved: focused tests, MCP TypeScript build, file-size guard, release governance bundle, autorun gates, git diff scope proof.

### Depth Audit

- Risk reduction: 2
- Decision value: 2
- Machine enforceability: 2
- Operational efficiency: 2
- Portfolio priority: 1
- Total: 9
- Decision: CONTINUE
- Reason: bounded enforce-mode mapping tightens CP2 without expanding surface.

### Authorization Boundary

- Authorized now: YES
- Next batch name: `CPG-2 CP2 Hard Gate Enforcement`
- Operator checkpoint: SATISFIED on 2026-05-31 via staging request authorizing CPG-2 after fresh GC-018.
- Hard invariants: default advisory compatibility; `runtimeExecutionAuthorized=false`; no CPG-3 receipt enrichment; no provider/public/production claims; MCP index size discipline if touched.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.

Baseline: CPG-2 CP2 Hard Gate Enforcement.

Proposed tranche: add typed mode + progression decision in INT1 owner module, preserve advisory default, extend focused tests, and keep enforce outputs bounded to owned connection-point progression.

## Evidence / Verification

Required before closure:

```powershell
npm run test:run -- src/tools/int1-adapter.test.ts
npm run build
python governance/compat/check_governed_file_size.py --enforce
python scripts/run_cvf_release_gate_bundle.py --json
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; public-sync requires separate authorized batch.

## Claim Boundary

This GC-018 authorizes bounded CP2 enforce-mode semantics at the owned INT1 connection point. It does not authorize CPG-3 receipt enrichment, provider routing changes, public/production claims, or universal bypass prevention beyond the owned connection point.
