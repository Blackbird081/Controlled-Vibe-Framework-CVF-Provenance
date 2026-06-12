# CVF Agent Work Order: MEOR-T3 DSCP Profile Requirement Bridge

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-12

Worker: Codex

Reviewer: Codex in separated reviewer pass

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `472c474d`

executionBaseHead: `472c474d`

closureBaseHead: `472c474d`

GC-018:
`docs/baselines/CVF_GC018_MEOR_T3_DSCP_PROFILE_REQUIREMENT_BRIDGE_2026-06-12.md`

## Purpose

Implement profile-scoped metadata requirement declarations in DSCP and expose
a deterministic bridge to MEOR-T2 without adding global domain defaults.

## Authority Chain

| Authority | Path | Status |
| --- | --- | --- |
| Operator direction | 2026-06-12 execute the full foundation roadmap | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_FOUNDATION_ROADMAP_2026-06-12.md` | MEOR-T3 authorized |
| T2 completion | `docs/reviews/CVF_MEOR_T2_EXTRACTION_METADATA_FINDING_NORMALIZATION_COMPLETION_2026-06-12.md` | PASS at `69ec7574` |
| GC-018 | T3 baseline | AUTHORIZED |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement | Output | Verification |
| --- | --- | --- | --- |
| Profile-scoped declarations | optional profile field | profile contract update | focused type/runtime tests |
| No global defaults | bridge consumes one explicit profile | new bridge module | omitted-profile and isolation tests |
| T2 ownership bridge | requirement-to-profile owner map | bridge result | exact map assertion |
| Fail closed | canonical validation failures | bridge result | negative tests |
| No descriptor mutation | pure declaration processing | source and tests | deep equality assertion |

## Intake Role Routing Decision

- Intake summary: implement a bounded deterministic TypeScript bridge from the
  closed T1/T2 contract into existing DSCP profiles.
- Risk sensitivity: low-risk local control-plane code; no provider, secret,
  external workspace, legal decision, or public claim.
- routeMode: `SINGLE_AGENT_MULTI_ROLE`;
- reason: narrow source/test tranche with exact local outcomes;
- independence control: implementation, adversarial test recomputation, and
  closure review occur as separate passes.
- Escalation condition: stop if implementation requires global defaults,
  descriptor mutation, EC/Policy_Local changes, provider use, retrieval, or a
  wider claim.

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Implementer | Codex build pass | contract field, bridge, focused tests |
| Adversarial reviewer | Codex reviewer pass | invalid declarations and non-mutation |
| Closer | Codex closure pass | full tests, registries, gates, continuity |

## Single-Agent Multi-Role Control Block

- Role separation ledger: implementer, test reviewer, closer, and committer are
  recorded as separate passes.
- Evidence basis: source inspection, focused and full tests, git diff, and
  machine gates.
- Self-review boundary: no independent external review is claimed.
- Escalation conditions: scope expansion, provider/live use, external changes,
  secrets, destructive action, public-sync, or claim-boundary change.
- Gate sequence: pre-dispatch, pre-implementation, reviewer-fast, committed
  material evidence, pre-closure, and continuity sync.

## Worker Autonomy / No-Question Rule

Repair allowed-scope implementation, tests, typing, formatting, and gate
failures without asking the operator. Escalate only for a listed
Return-To-Orchestrator condition.

## Required First Reads

1. T1 contract and machine semantics.
2. T2 completion and `metadata_evidence.py`.
3. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`.
4. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts`.

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Fact class | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Profile identifier | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 7-8 | `DomainProfileId` | type alias | EXISTS | ACCEPT |
| Existing profile contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 23-54 | `DscpDomainProfile` | interface | EXISTS | ACCEPT |
| Explicit profile application | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 96-100 | `applyDomainProfileToDescriptorInput` | function | RUNTIME_BEHAVIOR | ACCEPT |
| Existing DSCP exports | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | lines 77-98 | DSCP profile export block | barrel | EXISTS | ACCEPT |
| T1 evidence values | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json` | `values.evidenceBasis` | `evidenceBasis` | machine semantics | VALUE_SET | ACCEPT |
| T1 ownership invariant | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_CONTRACT_2026-06-12.md` | `Profile Ownership And Isolation` | `ownerProfileId` | canonical contract | LITERAL_INVARIANT | ACCEPT |

## New Runtime Fields And Symbols

| New item | Intended owner | Disposition |
| --- | --- | --- |
| `MetadataEvidenceBasis` | DSCP profile contract | DOC_ONLY_NEW |
| `DscpMetadataRequirement` | DSCP profile contract | DOC_ONLY_NEW |
| `metadataRequirements` | `DscpDomainProfile` | DOC_ONLY_NEW |
| `DscpMetadataRequirementBridgeResult` | new bridge module | DOC_ONLY_NEW |
| `buildDscpMetadataRequirementBridge` | new bridge module | DOC_ONLY_NEW |

## Allowed Scope

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`;
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts`;
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts`;
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.metadata.requirement.bridge.test.ts`;
- T3 baseline, work order, completion, parent roadmap, GC-051, and continuity.

## Forbidden Scope

- changing profile application behavior or descriptor values;
- global requirement registries or implicit defaults;
- extraction-foundation, LPCI, EC, or external Policy_Local source;
- dependencies, OCR, corpus ingestion, retrieval, provider/API-key use;
- public-sync and readiness claims.

## Write Ownership

| Path | Action |
| --- | --- |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | UPDATE |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | CREATE |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | UPDATE |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.metadata.requirement.bridge.test.ts` | CREATE |
| T3 governance and GC-051 surfaces | CREATE/UPDATE |
| other runtime paths | FORBIDDEN |

## Forbidden Filesystem State At Dispatch

- both new TypeScript target paths are absent;
- no external Policy_Local path is modified;
- worktree contains only this dispatch packet, roadmap, and continuity state.

## Pre-Flight Checks

1. Confirm HEAD includes T2 closure `69ec7574` and sync `472c474d`.
2. Confirm T1 contract and T2 completion exist.
3. Confirm both new TypeScript paths are absent.
4. Run pre-dispatch autorun on the staged dispatch range.
5. Commit dispatch and replace `executionBaseHead` with that commit.

## Execution Plan

1. Add exact T1 evidence-basis literals and a requirement declaration type.
2. Add optional `metadataRequirements` to `DscpDomainProfile`.
3. Implement a pure bridge that validates one explicit profile.
4. Return a deterministic declaration list and requirement-owner map.
5. Reject empty identifiers, duplicates, owner mismatch, empty evidence lists,
   and unsupported evidence values.
6. Prove omitted requirements are valid and produce empty outputs.
7. Prove the profile and declaration arrays are not mutated.
8. Run focused, full, and type-check verification.

## Evidence Requirements

- exact evidence-basis literal coverage;
- deterministic sort/order and owner map;
- exact validation failure tokens;
- no profile bleed or global defaults;
- no descriptor mutation or gate activation;
- focused vitest, full control-plane test, and TypeScript check PASS;
- changed-path and registry evidence.

## Acceptance Criteria

1. Requirement ownership is explicit and equals the enclosing profile ID.
2. Requirement IDs are unique within a profile.
3. Acceptable evidence values are limited to the T1 set.
4. Empty declarations fail closed.
5. Omitted requirements produce an empty valid bridge.
6. Bridge outputs are deterministic and do not mutate inputs.
7. Existing profiles without the optional field remain source-compatible.
8. No domain-specific default requirement appears.
9. No descriptor, metadata value, or gate is changed.
10. Focused, full, and type-check verification pass.

## Review Gate

The reviewer must construct invalid declarations independently, compare input
objects before and after bridge execution, and reject any global registry,
implicit requirement, descriptor mutation, or domain-specific default.

## Closure Checklist

- [ ] Source and focused tests exist.
- [ ] Validation failures and deterministic outputs pass.
- [ ] Existing profile tests remain compatible.
- [ ] Full tests and type check pass.
- [ ] GC-051 JSON and Markdown are updated.
- [ ] Reviewer-fast and pre-closure pass.
- [ ] Roadmap and continuity release only MEOR-T4.

## Return-To-Orchestrator Conditions

Return if the bridge requires global defaults, descriptor mutation, changes to
T1 semantics, extraction or Policy_Local edits, a dependency, provider use,
retrieval, or a wider claim.

## Operator Checkpoint

operator.checkpoint.waiver: operator explicitly authorized execution of the
full foundation roadmap. No additional checkpoint is required inside scope.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | dispatched status | BLOCKED pending execution |
| Completion or reviewer artifact | T3 completion review | not authored at dispatch | BLOCKED pending execution |
| Roadmap state | foundation roadmap | T3 dispatched | PASS |
| Registry JSON | GC-051 JSON | T3 source/test entries | BLOCKED pending execution |
| Registry Markdown | GC-051 Markdown | T3 quick lookup rows | BLOCKED pending execution |
| External evidence digest | N/A with reason: repo-local implementation only | no external evidence | N/A with reason |
| System loop interlock | N/A with reason: no loop mutation planned | local bridge only | N/A with reason |
| Session continuity | active state/memory/handoff | T3 implementation next | PASS |

## Claim Boundary

This work order authorizes profile declaration and validation only. It does not
authorize metadata correction, domain decisions, gate activation, retrieval,
provider use, external integration, or readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation implementation; no public-sync authorized.
