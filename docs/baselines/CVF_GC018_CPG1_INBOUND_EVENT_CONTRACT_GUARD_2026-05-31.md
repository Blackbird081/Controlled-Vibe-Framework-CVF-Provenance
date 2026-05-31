# CVF GC-018 Continuation Candidate
## CPG-1 Inbound Event Contract Guard

Memory class: BASELINE_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-31

---

## Purpose

Authorize the first bounded runtime tranche after LHW21: extract the INT1
inbound event contract policy from the MCP registration file into a same-domain
module and test the real owner logic directly.

This tranche tightens the CVF-owned connection point without changing CP2
advisory semantics, framework adapters, provider behavior, or receipt schemas.

## Scope / Target / Owner Boundary

Target contract: `cvf.connectionPointEventContractGuard.cpg1.v1`.

Owner: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER`.

Allowed runtime change:

- create `src/tools/int1-connection-point-policy.ts`;
- import the extracted policy from `src/index.ts`;
- replace duplicated test helpers in `src/tools/int1-adapter.test.ts` with
  imports from the owner module.

Forbidden scope:

- no CPG-2 `connectionPointMode`;
- no enforce-mode refusal;
- no CPG-3 `governanceTrace`;
- no framework-specific adapter;
- no provider prompt, model, public-sync, hosted-readiness, or production claim.

## Source / Predecessor Evidence

- Roadmap:
  `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- LHW21 baseline:
  `docs/baselines/CVF_GC018_LHW21_INTEGRATION_CONNECTION_POINT_ADVISORY_WAVE_2026-05-31.md`
- LHW21 T1:
  `docs/reference/CVF_LHW21_T1_EVENT_TAXONOMY_SCHEMA_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`
- LHW21 T2:
  `docs/reference/CVF_LHW21_T2_HARD_GATE_MODE_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`
- Current runtime owner:
  `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- Current tests:
  `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts`

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| INT1 contract exists | `LITERAL_INVARIANT` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | line 770 | `INT1_CONTRACT` | INT1 MCP adapter | ACCEPT: `cvf.genericMcpAdapter.int1.v1` |
| INT1 transport event set exists | `VALUE_SET` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | lines 771-774 | `INT1_ALLOWED_EVENT_TYPES` | INT1 MCP adapter | ACCEPT: `intent.received`, `plan.created`, `tool.requested`, `execution.state`, `result.produced` |
| INT1 plan tool is advisory | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | lines 779-808 | `cvf_validate_plan` | INT1 MCP tool | ACCEPT: does not block execution |
| INT1 event emitter validates supported types | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | lines 814-851 | `cvf_emit_agent_event` | INT1 MCP tool | ACCEPT |
| Test file duplicates policy helpers | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts` | lines 8-67 | `validatePlan` | INT1 test helper | ACCEPT: replace with owner-module imports |
| Same-domain policy module is new | `DOC_ONLY_NEW` | `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md` | CPG-1 tranche | `int1-connection-point-policy.ts` | planned MCP policy module | ACCEPT: planned new file |

## New Proposed Fields And Symbols

| Proposed item | Intended owner | Purpose | Runtime status now |
| --- | --- | --- | --- |
| `INT1_CONTRACT` export | `src/tools/int1-connection-point-policy.ts` | Preserve existing INT1 contract literal in extracted owner module | DOC_ONLY_NEW |
| `INT1_ALLOWED_EVENT_TYPES` export | `src/tools/int1-connection-point-policy.ts` | Preserve existing transport event set in extracted owner module | DOC_ONLY_NEW |
| `validateInt1Plan` | `src/tools/int1-connection-point-policy.ts` | Make existing advisory plan evaluation independently testable | DOC_ONLY_NEW |
| `emitInt1AgentEvent` | `src/tools/int1-connection-point-policy.ts` | Make existing inbound event validation independently testable | DOC_ONLY_NEW |

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/archive/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  LHW21 T1/T2 specs, CPG roadmap, current INT1 inline owner block, and INT1
  test file.
- Prior absorption evidence resolved:
  LHW21 GC-018 and T1/T2 connector specs.
- Detailed source files used:
  `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`;
  `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/int1-adapter.test.ts`.
- Source families skipped:
  framework-specific adapters, receipt enrichment, and CP2 enforce mode;
  reason: held for separate roadmap tranches.
- File-level accepted value:
  existing event allowlist and advisory plan evaluation can become a thin,
  importable owner policy without semantic expansion.
- Owner-surface normalization:
  INT1 inline logic -> MCP same-domain tools module.
- Accept/defer/reject matrix:
  policy extraction ACCEPT_NOW; test-helper replacement ACCEPT_NOW;
  hard-gate mode DEFER_DEMAND_GATED; receipt enrichment DEFER_DEMAND_GATED;
  outbound adapters REJECT_DIRECT.
- Adversarial roles completed:
  Implementer: smallest proof is policy extraction plus direct unit tests.
  Skeptic/Auditor: preserve dotted event literals and advisory-only behavior.
  Product/Operator Advocate: make inbound guard behavior explicit before
  adding enforcement.
  Safety/Boundary Owner: no blocking mode or runtime authority is added.
- Thin proof target:
  extracted policy module, import wiring, direct unit tests, TypeScript build.
- Blind-spot verdict: CLEAR.

## GC-018 Continuation Candidate

- Candidate ID: `gc018-cpg1-inbound-event-contract-guard-2026-05-31`
- Parent roadmap / wave:
  `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- Proposed scope: extract and directly test INT1 inbound event policy
- Continuation class: REALIZATION
- Active quality assessment: LHW21 T1/T2 connector specs and roadmap source pass
- Assessment date: 2026-05-31
- Weighted total: 9/10
- Lowest dimension: portfolio priority (1/2)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now:
  this is the smallest runtime guard tightening step and removes duplicated
  test logic before any enforce-mode design.
- Quality protection commitments:
  semantic preservation, same-domain extraction, direct tests, and no CPG-2.
- Why now:
  operator authorized roadmap coding after LHW21 closure.
- Active-path impact: LIMITED
- Risk if deferred:
  connection-point behavior remains inline and tests may drift from runtime.
- Lateral alternative considered: YES
- Why not lateral shift:
  receipt enrichment and enforcement both depend on a testable owner policy.
- Real decision boundary improved: YES
- Expected enforcement class: RUNTIME_GUARD
- Required evidence if approved:
  direct tests, MCP TypeScript build, changed-file evidence.

### Depth Audit

- Risk reduction: 2
- Decision value: 2
- Machine enforceability: 2
- Operational efficiency: 2
- Portfolio priority: 1
- Total: 9
- Decision: CONTINUE
- Reason: thin extraction makes the owned connection-point policy testable.

### Authorization Boundary

- Authorized now: YES
- Next batch name: `CPG-1 Inbound Event Contract Guard`
- Operator checkpoint:
  SATISFIED on 2026-05-31 by direct instruction to proceed with roadmap code.
- Hard invariants:
  preserve advisory behavior; no `connectionPointMode`; no `governanceTrace`;
  no outbound adapter; no public or production claim.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.

Baseline: CPG-1 Inbound Event Contract Guard.

Proposed tranche: extract the current INT1 inline connection-point policy into
one same-domain MCP module, wire the existing tools through that module, and
replace duplicated test helpers with direct owner-module tests.

## Evidence / Verification

Required before closure:

```powershell
npm run test:run -- src/tools/int1-adapter.test.ts
npm run build
python governance/compat/check_governed_file_size.py --enforce
```

Live governance proof is not required for this semantic-preserving extraction.
Any later claim that CP2 blocks execution requires the mandatory governed-route
live proof.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CPG-1 is private provenance runtime hardening. Public export needs a
separate public-sync work order after bounded closure evidence exists.

## Claim Boundary

This packet authorizes CPG-1 extraction and direct tests only. It does not
authorize hard-gate enforcement, receipt enrichment, live framework proof,
public export, hosted readiness, or production readiness.
