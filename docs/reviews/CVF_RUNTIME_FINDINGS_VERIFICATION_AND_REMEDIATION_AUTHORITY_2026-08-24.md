# CVF Runtime Findings Verification And Remediation Authority

Memory class: governed-review

Status: ACCEPTED_FOR_REMEDIATION

docType: review

Date: 2026-08-24

Review base head: `e196899548d04f88ee5bc40cfce1ddf268a29d6b`

## Purpose

Record the source-and-test verification of the ten external-agent findings and
authorize a CVF-native remediation sequence. This review does not import an
external architecture and does not itself change runtime behavior.

## Target / Source

Target: the external audit questions supplied by the operator on 2026-08-24.

Sources checked include the canonical Guard Contract, Mandatory Gateway, MCP
server and Model Gateway adapter, MAO/Truth/evidence contracts, capability
admission surfaces, isolation contracts, generated catalogs, and their focused
tests. Provider-specific memory was not used as authority.

## Scope / Methodology

The review followed `SCOUT -> TRACE OWNERS -> VERIFY -> CLASSIFY -> REPORT`.
Each hypothesis was challenged against production source and negative tests.
The bounded relevant suites completed with 328 passing tests and no provider,
credential, paid API, deployment, or public-sync action.

## Findings / Position

| ID | Verified classification | Severity | Existing CVF owner | Position |
|---|---|---|---|---|
| F1 | `RUNTIME_AUTHORITY_GAP` | HIGH | Guard Contract | Five runtime phases are deliberate, but generic mutating BUILD admission does not require accepted SPEC plus valid, in-scope WORK ORDER evidence. |
| F2 | `PARTIAL_MONOTONICITY` | MEDIUM | Guard Contract engine | Result aggregation is monotonic, but a registered guard remains caller-mutable through its object reference. |
| F3 | configuration-authority gap | MEDIUM | Mandatory Gateway | Current Web composition is safe by default; constructor/update configuration remains mutable authority without an immutable bootstrap boundary. |
| F4 | `AUTHORITY_WIDENING_RISK` | MEDIUM | Mandatory Gateway | `bypassActions` uses substring matching and can collide with wider action strings. |
| F5 | `MATERIAL_PROVENANCE_GAP` | HIGH | Model Gateway, context/evidence and Truth owners | Evidence exists by class, but no complete secret-safe invocation-context manifest binds all material model-visible inputs to one invocation. |
| F6 | `DISTRIBUTED_EQUIVALENT` | INFO | MAO ledgers and Truth Kernel | Append-only occurrence evidence and truth evaluation exist as distinct distributed owners; no new event subsystem is justified. |
| F7 | `NO_NEW_VALUE` / enrich existing owner | INFO | CADP, ASSF, Execution Plane | Capability definition/provider/consumer separation exists; trust must remain distinct from compatibility. |
| F8 | `BYPASS_PATH_FOUND` (conditional) | HIGH | MCP server, Model Gateway and Execution Plane | The exported MCP adapter can trust caller-supplied `policyResult`; default composition has no executor and is fail-closed, but native admission is not intrinsic to the adapter. |
| F9 | dimensional but incomplete isolation | MEDIUM | Execution/isolation contracts | Dimensions exist, but `worker_threads` are not a security boundary and inherit process environment. |
| F10 | `ALREADY_STRONG` with selective enrichment | LOW | generated indexes, schemas and compat checkers | Machine-readable generation is strong; remaining handwritten duplication should be enriched only at existing generators. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| canonical runtime has five phases | TYPE_MODEL | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | lines 21-27 | `CanonicalCVFPhase` | Guard Contract types | ACCEPT |
| generic context has no SPEC/WORK ORDER authority evidence | TYPE_MODEL | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | `GuardRequestContext`, lines 93-110 | `GuardRequestContext` | Guard Contract types | ACCEPT |
| BUILD role admission can allow without SPEC/WORK ORDER | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/phase-gate.guard.ts` | phase-role matrix and `evaluate` | `PhaseGateGuard` | Guard Contract | ACCEPT |
| BUILD action authority uses role/action/risk only | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts` | lines 109-190 | `AuthorityGateGuard.evaluate` | Guard Contract | ACCEPT |
| shared factory lacks a BUILD prerequisite guard | COMPOSITION | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | lines 380-392 | `createGuardEngine` | Guard Contract package root | ACCEPT |
| current tests positively allow AI_AGENT BUILD | TEST_EVIDENCE | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts` | PhaseGateGuard and AuthorityGateGuard suites | `allows AI_AGENT in BUILD`; `allows AI_AGENT write action in BUILD` | Guard Contract tests | ACCEPT |
| mandatory IDs omit BUILD authority | CONFIGURATION | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | line 262 | `MANDATORY_GUARD_IDS` | Guard Contract types | ACCEPT |
| action mutation classifier already exists | OWNER_REUSE | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/action-intent.ts` | exported helpers | `hasModifyIntent` | Guard Contract | ACCEPT |
| external hypotheses are not canonical authority | SOURCE_BOUNDARY | `AGENTS.md` | Authority Hierarchy and Claim Boundary | canonical authority hierarchy | repository instruction carrier | ACCEPT |

## Risk / Corrective Action

Remediation order is fail-closed and severity-led:

1. R1 closes F1 at the generic Guard Contract BUILD boundary.
2. R2 closes F2-F4 without weakening existing defaults.
3. R3 removes caller-supplied policy trust from MCP execution admission.
4. R4 binds material model-visible context to a secret-safe invocation manifest.
5. R5 makes isolation guarantees explicit and rejects unsupported claims.
6. R6 reruns the cross-owner adversarial audit and closes only proven findings.

Absorption and unrelated feature coding remain parked until the three HIGH
findings are independently accepted.

## Decision / Disposition

The external agent's questions were materially valid audit prompts. F1, F5 and
F8 are confirmed HIGH defects or gaps; F2-F4 and F9 are bounded hardening work;
F6, F7 and F10 do not justify new subsystems. Proceed through the governed
roadmap and one fresh GC-018/work order per implementation tranche.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|---|
| F1 | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `PHASE_GATE_PLACEMENT_GAP` | add mandatory typed BUILD prerequisite and negative tests in R1 | dispatched by R1 packet |
| F2-F4 | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | harden immutability and exact action matching in R2 | deferred to dependency-gated R2 |
| F5 | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `RUNTIME_LEARNING_CANDIDATE` | compose existing evidence owners in R4 | deferred to dependency-gated R4 |
| F8 | `MACHINE_GATE_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `MACHINE_CHECK_CANDIDATE` | require native admission result at MCP invocation in R3 | deferred to dependency-gated R3 |
| F9 | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `DESIGN_REVIEW_REQUIRED` | bind isolation claims to actual adapter guarantees in R5 | deferred to dependency-gated R5 |
| F6/F7/F10 | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `RULE_EXISTS` | retain existing-owner discipline; no subsystem creation | handled by roadmap non-goals |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | external findings -> local owner trace -> verified governed review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Guard Contract, Model Gateway, Execution Plane, MCP, Truth/evidence and isolation owners |
| Disposition | ADAPT verified deltas into existing owners; reject subsystem overlap |
| Claim boundary | external questions are inputs, never CVF authority or completion evidence |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| literalTokensReviewed | review heading families; `Source Verification Block`; `Finding-To-Governance Learning Disposition`; `Public Export Disposition`; canonical dispositions |
| gateRunPurpose | confirm governed review and downstream dispatch shape before authoring |
| claimBoundary | structure checks do not prove runtime remediation or closure |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance review evidence; no public-sync action is
authorized by this artifact.

## Claim Boundary

Confirmed claims are limited to the inspected local source and executed bounded
tests at the review base. This review does not claim live-provider proof,
production deployment, public export, runtime remediation, or closure of any
finding.
