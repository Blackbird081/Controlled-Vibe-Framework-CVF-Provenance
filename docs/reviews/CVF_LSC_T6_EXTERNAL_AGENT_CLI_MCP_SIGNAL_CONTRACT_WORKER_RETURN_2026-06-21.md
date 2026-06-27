# CVF LSC-T6 External Agent CLI/MCP Signal Contract - Worker Return

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: worker_return

Date: 2026-06-21

dispatchBaseHead: 5ee4b9b5

executionBaseHead: c4b2c061

Commit mode: WORKER_MUST_NOT_COMMIT

## git status --short

```
?? docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md
?? docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_WORKER_RETURN_2026-06-21.md
 M docs/reference/learning_signal_chain/README.md
```

(Recorded after all three worker artifacts were created/updated, before any commit.)

## Purpose

Return uncommitted worker artifacts for LSC-T6 External Agent CLI/MCP Signal
Contract after executing
`docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_FOR_WORKER_2026-06-21.md`
under `WORKER_MUST_NOT_COMMIT`.

The work order authorized defining a portable external-agent signal IO contract
so future CLI/MCP adapter authors know what five fields a minimal signal event
carries, what defaults normalization may synthesize, how external returned output
routes through the absorption chain, how LSC-T3 readout and LSC-T4 outcomes
appear as advisory output for external consumers, and that no adapter behavior
is implemented by this contract.

## Scope / Methodology

Task class: `WORKER_MUST_NOT_COMMIT` adapter-contract-only documentation/reference
authoring.

Allowed scope executed:

- Read all required source files named in Required First Reads.
- Created `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md`
  with all Required Contract Content sections per work order section Required Contract
  Content and GC-018 section Required Contract.
- Updated `docs/reference/learning_signal_chain/README.md` with an LSC-T6 row
  stating adapter-contract-only scope and no runtime/adapter/ledger implementation.
- Created `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_WORKER_RETURN_2026-06-21.md`
  (this file).

Forbidden scope confirmed not executed:

- No edits to `governance/compat/**`, `CVF_SESSION/**`, active handoff, root
  startup routers, public-sync, `.github/**`, dependency manifests, web UI,
  MCP packages, runtime provider routes, or Learning Plane runtime source.
- No ledger source directory, generated aggregate, generator, drift checker,
  durable store, CLI/MCP adapter, MCP tool, runtime bridge, provider/live proof,
  read-receipt enforcement, queue/daemon/watcher, wrapper/proxy, or arbitrary
  command execution implemented.
- No implementation of LSC-T5, LSC-T7, AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7,
  or MLW8.
- No commit performed.

## Source Inventory

| Source | Read status | Notes |
|---|---|---|
| `docs/reference/guard_orientation/README.md` | READ | task-first guard map; worker execution guard confirmed |
| `docs/baselines/CVF_GC018_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_2026-06-21.md` | READ | GC-018 authorization, scope/boundary, required contract |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_FOR_WORKER_2026-06-21.md` | READ | work order, packet shape, acceptance criteria, source verification block |
| `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | READ | LSC-T6 row line 257; minimal payload lines 188-195; external readiness boundary lines 215-229; design-control gate lines 231-245 |
| `docs/reference/learning_signal_chain/README.md` | READ | existing front door table before update |
| `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | READ | field ownership lines 55-70; CLI/MCP minimal payload boundary lines 202-210 |
| `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | READ | external-agent returned-output eligibility lines 85-91; absorption routing lines 170-184 |
| `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md` | READ | signalReadout shape lines 25-58; readout relationship lines 134-151; LSC-T6 routing lines 176-179 |
| `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | READ | outcome vocabulary lines 61-74; LSC-T6 future-tranche routing lines 205-223 |
| `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | READ | mandatory chain; input type router lines 55-76 |
| `governance/compat/run_agent_automation_assist.py` | READ | SignalReadoutItem lines 459-474; AssistReport.to_dict signalReadout lines 531-543; _print_human lines 801-809 |

## Scan-Depth Ledger

| Item | Scan depth | Disposition |
|---|---|---|
| LSC-T0 roadmap line 257 | Direct read | ACCEPT - LSC-T6 External Agent CLI/MCP Signal Contract work plan row confirmed |
| LSC-T0 roadmap lines 188-195 | Direct read | ACCEPT - five minimal fields confirmed: `signalClass`, `actorRole`, `sourceSummary`, `severity`, `lane`; normalization defaults confirmed |
| LSC-T0 roadmap lines 215-229 | Direct read | ACCEPT - external readiness boundary: no direct execution authority confirmed |
| LSC-T0 roadmap lines 231-245 | Direct read | ACCEPT - design-control gate: CLI/MCP-facing boundary, intake extension, mutation boundary, source authority, runtime boundary all required |
| LSC-T1 lines 55-70 | Direct read | ACCEPT - `LearningSignalIntakeInput`/`LearningSignalIntakeRecord` field ownership; map-to-not-parallel rule confirmed |
| LSC-T1 lines 202-210 | Direct read | ACCEPT - CLI/MCP Minimal Payload Boundary; five fields + synthesized defaults confirmed |
| LSC-T2 lines 85-91 | Direct read | ACCEPT - External reviewer/external agent capture eligibility confirmed |
| LSC-T2 lines 170-184 | Direct read | ACCEPT - External Agent Returned-Output Routing: four mandatory steps confirmed; `externalReturnEligibility` rule confirmed |
| LSC-T3 lines 25-58 | Direct read | ACCEPT - `signalReadout` advisory shape; advisory boundary confirmed |
| LSC-T3 lines 134-151 | Direct read | ACCEPT - readout item fields; JSON/human output contract confirmed |
| LSC-T3 lines 176-179 | Direct read | ACCEPT - LSC-T6 routing as candidate input to schema design confirmed |
| LSC-T4 lines 61-74 | Direct read | ACCEPT - seven LSC-T4 outcome vocabulary terms confirmed |
| LSC-T4 lines 205-223 | Direct read | ACCEPT - LSC-T6 future-tranche routing; LSC-T3 consumes T4 vocabulary confirmed |
| External absorption chain map lines 55-76 | Direct read | ACCEPT - mandatory chain; input type router confirmed |
| AAF helper lines 459-474, 531-543, 801-809 | Direct read | ACCEPT - SignalReadoutItem, signalReadout in to_dict, Learning Signal Readout section in _print_human confirmed |

## Changed-Path List

| Path | Action | Authorization |
|---|---|---|
| `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | Created: full external-agent CLI/MCP signal IO reference contract | Work order Write Ownership table |
| `docs/reference/learning_signal_chain/README.md` | Updated: added LSC-T6 row to Current Contracts table | Work order Write Ownership table |
| `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_WORKER_RETURN_2026-06-21.md` | Created: this worker return artifact | Work order Write Ownership table |

No other paths changed.

## Findings / Position

### F1 - Contract is adapter-contract-only and documentation/reference-only

The LSC-T6 reference contract defines `externalAgentSignalEvent` (five required
fields: `signalClass`, `actorRole`, `sourceSummary`, `severity`, `lane`) and
`externalAgentNoSignalAssertion` (`"noSignal": true` with required `reason`).
Both shapes are documentation-only. No endpoint, schema validator, runtime
parser, or MCP tool exists for them.

### F2 - Five-field minimal event preserves LSC-T1 intake ownership

The contract's section External-Agent Signal Event Shape now distinguishes
direct intake fields from external payload tokens. `sourceSummary`, `severity`,
and `lane` map directly to existing intake fields. `signalClass` and
`actorRole` are LSC-T0/T1 minimal CLI/MCP payload tokens that must be classified
or normalized by the absorbing role before projection into existing owner
surfaces such as `defectClass`, `sourceArtifact`, `evidenceBasis`, `lane`, or
LSC extension `sourceProjection`. The contract creates no parallel runtime
field definitions.

### F3 - Normalization defaults are future behavior, clearly labeled

Seven normalization defaults (`sourceId`, `recordId`, `observedAt`, `repeatRisk=POSSIBLE`,
`captureState=CAPTURED`, `autonomousMutationAuthorized=false`, `rootCauseGroupId=PENDING`)
are documented as future helper/ledger normalization behavior. Each default cites
its LSC-T1 authority. The contract explicitly states no normalization helper
exists yet.

### F4 - Absorption routing four-step chain documented

The section External Returned-Output Absorption Routing section documents the four
mandatory steps from LSC-T2 section External Agent Returned-Output Routing: identify,
route through absorption workflow, record disposition, map to signal using
absorption packet as `sourceArtifact`. The no-bypass rule is stated explicitly.

### F5 - Readout relationship and promotion vocabulary marked advisory

The section Readout Relationship section states `signalReadout` is advisory only and
`recommendedOutcome` values do not authorize dispatch, mutation, or work-order
creation. The section Promotion Recommendation Boundary table defines allowed vs.
forbidden use of each LSC-T4 outcome for external consumers.

### F6 - `autonomousMutationAuthorized=false` invariant preserved

The section Mutation Boundary section documents this invariant explicitly for external
actors. The contract states no promotion outcome authorizes autonomous mutation.

### F7 - README row states no adapter/runtime behavior

The updated LSC README row for LSC-T6 states: "adapter-contract-only and
documentation/reference-only; no CLI/MCP adapter behavior, ledger store,
generator, drift checker, runtime mutation, provider/live proof, or public-sync
implemented."

## Risk / Corrective Action

| Risk | Severity | Mitigation |
|---|---|---|
| Future adapter authors may mistake documentation-only shapes for active schemas | low | Contract states "documentation-only" and "no current runtime" at multiple points; the contract's own claim boundary section reiterates this |
| `externalAgentSignalEvent` field list may diverge from LSC-T1 updates | low | Contract maps each field to a specific LSC-T1 authority; any LSC-T1 change requires a separate work order that should also update LSC-T6 |
| External agents may assert `OBSERVED_REPEATED` without ledger evidence | low | The section Promotion Recommendation Invariants section explicitly forbids this; LSC-T4 blocking boundary rule is reiterated |
| No residual uncorrected risk identified | - | - |

## Pre-Flight Gate Evidence

### Gate 1: `git rev-parse --short HEAD` at worker start

```
c4b2c061
```

### Gate 2: `git status --short` at worker start

```
(clean worktree)
```

### Gate 3: `python -m unittest governance.compat.test_run_agent_automation_assist`

```
Ran 45 tests in 0.033s
OK
```

Result: 45/45 PASS.

### Gate 4: `python governance/compat/run_agent_automation_assist.py --base 5ee4b9b5 --head HEAD --json --enforce`

```json
{
  "defects": [],
  "signalReadout": []
}
```

Result: `defects=[]` PASS; `signalReadout` list present PASS; exit 0 PASS.

### Gate 5: `python governance/compat/run_worker_return_fast_gate.py`

```
corpus scan registry aggregate drift: PASS
reviewer-fast governance gate: 32/32 checks PASS (all checks pass including
  agent packet authority and encoding, core guard self-protection, worker
  experience retrospective, work-order dispatch quality, corpus completeness,
  finding-to-governance learning quality, rescan intelligence hardening,
  Delta execution claim boundary, public export disposition quality,
  machine closure package, epistemic process packet)
git diff whitespace check: PASS
COMPLIANT: worker-return fast gate passed in 2.59s.
```

Result: COMPLIANT PASS.

Note: first fast-gate run caught section-sign non-ASCII characters in both
deliverables. Repaired per Worker Autonomy rule by replacing all section-sign
characters with ASCII `section ` in
`CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` and this worker-return
file before rerunning the gate successfully.

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - LSC-T6 is a bounded
  adapter-contract-only documentation/reference tranche, not a corpus
  enumeration or legacy scan.
- Corpus root: NOT_APPLICABLE_WITH_REASON - no corpus root assigned.
- Snapshot time: NOT_APPLICABLE_WITH_REASON - no corpus snapshot taken.
- Enumeration command: filesystem-backed direct file reads per Source Inventory
  and Scan-Depth Ledger above; no corpus enumeration command authorized.
- Manifest artifact or inline manifest: inline Source Inventory and Scan-Depth
  Ledger above.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash created.
- Processing ledger artifact or inline ledger: inline Scan-Depth Ledger above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Source Inventory; ledger_terminal=READ for all named source rows; exclusions=corpus scan, legacy source-family enumeration, public-sync, runtime/provider/live proof, CLI/MCP adapter, and parked lanes; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: corpus scan, legacy source-family enumeration, public-sync,
  runtime/provider/live proof, CLI/MCP adapter, ledger/generator/drift checker
  implementation, and parked lanes (LSC-T5/T7, AAF-T6/T7, CGE-T3, ACE-R1,
  MLW7/8).
- Unreadable or unsupported files: 0.
- Aggregation check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate created.
- Drift check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate or generated
  corpus registry changed.
- Output traceability: Changed-Path List and Source Inventory define all worker
  output traceability.
- Adversarial verification: reviewer/closer must run reviewer-fast or stricter
  gate before acceptance.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed baseline/work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | LSC-T6 External Agent CLI/MCP Signal Contract |
| Disposition | ADAPT as CVF-owned external-agent signal IO contract tranche |
| Claim boundary | external-agent returns remain input only until classified; LSC-T6 does not implement external-agent CLI/MCP adapter IO behavior |

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`.
- Predecessor intake artifact: `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md`.
- Predecessor capture artifact: `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md`.
- Predecessor readout artifact: `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md`.
- Predecessor promotion artifact: `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md`.
- Delta ledger status: `CHANGED_DISPOSITION` - LSC-T6 moves external-agent
  CLI/MCP signal IO from roadmap row into deployed reference contract.
- Routing matrix status: `DO_NOW` for adapter-contract-only reference,
  README row, and worker-return packet (this tranche); `SEPARATE_RUNTIME_TRANCHE`
  for actual CLI/MCP adapter, ledger store, generator, drift checker, runtime
  bridge, latency guard; `STRATEGIC_OPERATOR_DECISION` for LSC-T5/T7 after
  LSC-T6; `OUT_OF_SCOPE` for provider/live/direct-interception/readiness claims.
- Semantic sampling status: sampled LSC-T0 minimal payload lines 188-195,
  LSC-T0 external readiness boundary lines 215-229, LSC-T1 intake ownership
  lines 55-70 and 202-210, LSC-T2 external return routing lines 170-184,
  LSC-T3 readout shape lines 25-58 and 134-151, LSC-T4 outcome vocabulary
  lines 61-74, external absorption chain map lines 55-76, AAF helper lines
  459-474 and 531-543 and 801-809.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | LSC remains capture-fast, promotion-slow, and proposal-only. `autonomousMutationAuthorized=false` invariant preserved. |
| CHANGED_DISPOSITION | LSC-T6 external-agent CLI/MCP signal IO moved from roadmap row into deployed reference contract with five-field event shape and exact no-signal assertion. |
| NEW_FINDING | `externalAgentSignalEvent` and `externalAgentNoSignalAssertion` are documentation-only shapes; they must not be presented as existing runtime schemas, parsed API payloads, or MCP tool parameters. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/CLI-MCP adapter implementation/direct-interception scope remains rejected for LSC-T6. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | LSC-T6 adapter-contract-only reference contract, README row, and worker-return packet (this tranche). |
| SEPARATE_RUNTIME_TRANCHE | actual CLI/MCP adapter, ledger store, generator, drift checker, runtime bridge, latency guard. |
| STRATEGIC_OPERATOR_DECISION | LSC-T5/T7 per active roadmap order after LSC-T6. |
| OUT_OF_SCOPE | provider/live, public-sync, direct interception, readiness, universal control. |
| RESOLVED_BY_DESIGN | define portable IO contract while preserving no execution authority and no runtime implementation. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LSC-T6-W1 | LSC-T0 line 257 | LSC-T6 exits with CLI/MCP schema and boundary contract only | mapped into Changed-Path List: three doc-only paths | prevents adapter implementation under contract work | PASS |
| LSC-T6-W2 | LSC-T1 CLI/MCP minimal payload lines 202-210 | five fields plus synthesized defaults | mapped into section External-Agent Signal Event Shape; section Normalization Defaults | prevents parallel field definition | PASS |
| LSC-T6-W3 | LSC-T2 absorption routing lines 170-184 | external output not directly eligible; four-step chain required | mapped into section External Returned-Output Absorption Routing | prevents raw external agent output becoming CVF signal | PASS |
| LSC-T6-W4 | LSC-T4 blocking-vs-readout | promotion vocabulary is advisory only | section Promotion Recommendation Boundary table; section Promotion Recommendation Invariants | prevents closure/dispatch overclaim by external consumers | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| External CLI/MCP agents needed portable signal IO contract before adapter implementation | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | WORK_ORDER_CANDIDATE | LSC-T6 defines the adapter-contract-only external-agent signal IO reference | handled by this tranche |
| Absorption routing must be documented before external signal capture eligibility is claimed | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | section External Returned-Output Absorption Routing documents four mandatory steps | handled by this tranche |
| Promotion vocabulary must be bounded for external consumers to prevent overclaim | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | section Promotion Recommendation Boundary defines allowed vs. forbidden per outcome | handled by this tranche |
| Actual CLI/MCP adapter behavior remains out of scope | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | adapter requires separate GC-018 and work order after LSC-T6 closure | deferred |
| LSC-T5 Learning Plane Bridge and LSC-T7 Latency Guard remain parked | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | N/A_WITH_REASON | operator-selected roadmap order: LSC-T5/T7 after LSC-T6 | deferred |
| Runtime/provider/cost applicability for this tranche | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: worker-return adapter-contract-only authoring
artifact - all source claims are grounded in direct file reads recorded in the
Source Inventory and Scan-Depth Ledger. Gate evidence is direct command output.
No contradictory evidence comparison or prior-belief update is required; this
is a bounded documentation/reference contract derivation.

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: worker must not mark closure. This section is
present with N/A disposition as required by the Worker Return Packet Shape
Contract. Closure is reviewer/closer-owned.

| Closure item | Worker disposition |
|---|---|
| Commit ownership | reviewer/closer only |
| Status update (GC-018, work order) | reviewer/closer only |
| Completion review creation | reviewer/closer only |
| Session-sync surfaces | reviewer/closer only if mode or next-move changes |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker return for Learning Signal Chain external-agent
CLI/MCP signal IO contract work. No public-sync remote, public commit, public
artifact path, or public claim is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T6 worker execution: adapter-contract-only reference contract, README row, and worker return authoring only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation/reference contract authoring only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | external-agent portable signal IO shape, no-signal assertion, normalization defaults, readout relationship, absorption routing, and mutation boundary only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, CLI/MCP adapter behavior, MCP tool implementation, and universal control remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker role |
| Provider or surface | local workspace |
| Session or invocation | LSC-T6 worker execution, 2026-06-21 |
| Working directory | repository root (`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF`) |
| Command or tool surface | direct file read/write/edit tools; git status; git rev-parse; unittest; AAF helper smoke; fast gate |
| Target paths | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md`; `docs/reference/learning_signal_chain/README.md`; `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_WORKER_RETURN_2026-06-21.md` |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_FOR_WORKER_2026-06-21.md`; `docs/baselines/CVF_GC018_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_2026-06-21.md` |
| Before status evidence | HEAD `c4b2c061`; `git status --short` clean before worker execution |
| After status evidence | `?? docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md`; `?? docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_WORKER_RETURN_2026-06-21.md`; ` M docs/reference/learning_signal_chain/README.md` |
| Diff evidence | reference contract created; README LSC-T6 row added; worker-return created |
| Approval boundary | worker role: update/create only the three required paths; no commit |
| Claim boundary | adapter-contract-only reference contract, README row, and worker return only; no runtime, ledger, adapter behavior, or public-sync claim |
| Agent type | worker role |
| Invocation ID | `lsc-t6-worker-2026-06-21` |
| Expected manifest | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` (create); `docs/reference/learning_signal_chain/README.md` (update); `docs/reviews/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT_WORKER_RETURN_2026-06-21.md` (create) |
| Actual changed set | same as expected manifest |
| Manifest delta | MATCH |

## Claim Boundary

This worker return covers LSC-T6 External Agent CLI/MCP Signal Contract
adapter-contract-only documentation/reference authoring only. It does not
implement a CLI/MCP adapter, MCP tool, shell bridge, ledger store, generator,
drift checker, durable store, runtime Learning Plane mutation, provider/live
proof, public-sync, direct interception, wrapper/proxy enforcement, queue/daemon,
watcher, readiness proof, cost optimization, full-hook equivalence, or universal
governed-coding control.

No session, handoff, public-sync, provider/live, MCP, dependency, queue/daemon,
`governance/compat/**`, or runtime mutation path was edited. No commit was made.
`autonomousMutationAuthorized=false` remains invariant.

## WORKER_EXPERIENCE_RETRO

```
WORKER_EXPERIENCE_RETRO
frictionLevel: LOW
frictionType: NONE_OBSERVED
preventiveControlCandidate: NONE
notes: Execution was smooth. All required source files were directly readable.
  The LSC-T1 CLI/MCP minimal payload section (lines 202-210) and LSC-T2
  external absorption routing (lines 170-184) provided clear, source-backed
  authority for the five-field event shape and the four-step absorption chain.
  The reference contract sections map cleanly from existing LSC-T1/T2/T3/T4
  authority. Gate results are recorded in the Pre-Flight Gate Evidence section
  below after the gates have been run.
```
