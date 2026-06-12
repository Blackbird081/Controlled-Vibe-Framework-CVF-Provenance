# CVF Agent Work Order: MEOR-T4 Cross-Domain Conformance

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-12

Worker: Codex

Reviewer: Codex in separated reviewer pass

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `7b2204dc`

executionBaseHead: `7b2204dc`

closureBaseHead: `7b2204dc`

GC-018:
`docs/baselines/CVF_GC018_MEOR_T4_CROSS_DOMAIN_CONFORMANCE_2026-06-12.md`

## Purpose

Prove that MEOR profile requirements and evidence evaluation remain
domain-scoped across legal-policy and technical-project synthetic fixtures.

## Authority Chain

| Authority | Path | Status |
| --- | --- | --- |
| Operator direction | 2026-06-12 execute the foundation roadmap | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_FOUNDATION_ROADMAP_2026-06-12.md` | T4 authorized |
| T3 completion | `docs/reviews/CVF_MEOR_T3_DSCP_PROFILE_REQUIREMENT_BRIDGE_COMPLETION_2026-06-12.md` | PASS at `5f328d11` |
| T4 GC-018 | T4 baseline | AUTHORIZED |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement | Output | Verification |
| --- | --- | --- | --- |
| Legal/technical isolation | disjoint profile requirements | shared fixture and tests | exact-set and negative assertions |
| Four resolution paths | resolved, unresolved, conflict, not-applicable cases | shared fixture | Python exact outcome assertions |
| One semantic authority | both suites consume one JSON file | shared fixture | path and parse assertions |
| No global defaults | bridge receives explicit profiles only | TypeScript test | absence and owner checks |
| No real use-case coupling | synthetic values only | fixture | forbidden-token search |

## Intake Role Routing Decision

- Intake summary: cross-language conformance proof for the closed T1-T3
  foundation.
- Risk sensitivity: low-risk local tests and synthetic data only.
- routeMode: `SINGLE_AGENT_MULTI_ROLE`;
- reason: bounded test-only tranche with exact machine semantics.
- independence control: fixture authoring, adversarial test pass, and closure
  review are separated.
- Escalation condition: stop for runtime edits, real Policy_Local data,
  provider use, external writes, or claim expansion.

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Fixture author | Codex design pass | shared synthetic authority |
| Test implementer | Codex build pass | TypeScript and Python tests |
| Adversarial reviewer | Codex review pass | cross-profile injection and drift |
| Closer | Codex closure pass | full tests, registries, gates, continuity |

## Single-Agent Multi-Role Control Block

- Role separation ledger: fixture author, implementer, adversarial reviewer,
  and closer are separate passes.
- Evidence basis: source inspection, shared fixture, focused/full tests, git
  diff, and machine gates.
- Self-review boundary: no independent external review is claimed.
- Escalation conditions: scope expansion, provider/live use, external changes,
  secrets, destructive action, public-sync, or claim-boundary change.
- Gate sequence: pre-dispatch, pre-implementation, reviewer-fast, committed
  material evidence, pre-closure, and continuity sync.

## Worker Autonomy / No-Question Rule

Repair allowed-scope fixture, test, typing, formatting, and gate failures
without asking the operator. Escalate only for a listed
Return-To-Orchestrator condition.

## Required First Reads

1. T1 contract and machine semantics.
2. T2 `metadata_evidence.py` and focused tests.
3. T3 profile contract, bridge, focused tests, and completion.
4. Parent roadmap acceptance criteria.

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Fact class | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Canonical machine values | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json` | top-level value arrays and rules R1-R6 | `observedStates`, `evidenceBases`, `resolutionStates`, `downstreamDispositions` | T1 machine semantics | VALUE_SET | ACCEPT |
| Evidence record input | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py` | `MetadataEvidenceRecord` | `MetadataEvidenceRecord` | dataclass | EXISTS | ACCEPT |
| Evidence evaluation | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py` | `evaluate_metadata_evidence` | `evaluate_metadata_evidence` | function | RUNTIME_BEHAVIOR | ACCEPT |
| Cross-profile fail token | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py` | `_validate_record` owner comparison | `CROSS_PROFILE_REQUIREMENT_BLEED` | validation path | LITERAL_INVARIANT | ACCEPT |
| Profile requirement declaration | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | `DscpMetadataRequirement` | `DscpMetadataRequirement` | interface | EXISTS | ACCEPT |
| Profile bridge | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | `buildDscpMetadataRequirementBridge` | `buildDscpMetadataRequirementBridge` | function | RUNTIME_BEHAVIOR | ACCEPT |
| Bridge owner mismatch | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | owner comparison branch | `OWNER_PROFILE_MISMATCH` | validation path | LITERAL_INVARIANT | ACCEPT |

## New Doc-Only Fields

| New item | Intended owner | Disposition |
| --- | --- | --- |
| `fixtureVersion` | T4 JSON fixture | DOC_ONLY_NEW |
| `profiles` | T4 JSON fixture | DOC_ONLY_NEW |
| `cases` | T4 JSON fixture | DOC_ONLY_NEW |
| `expectedResolutionState` | T4 JSON fixture case | DOC_ONLY_NEW |
| `expectedDownstreamDisposition` | T4 JSON fixture case | DOC_ONLY_NEW |

## Allowed Scope

- `docs/reference/CVF_MEOR_T4_CROSS_DOMAIN_CONFORMANCE_FIXTURES_2026-06-12.json`;
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.metadata.requirement.cross.domain.conformance.test.ts`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_metadata_evidence_cross_domain.py`;
- T4 baseline, work order, completion, parent roadmap, GC-051, and continuity.

## Forbidden Scope

- any runtime source modification;
- external Policy_Local paths or real candidate identifiers;
- LPCI/EC schema, gate, retrieval, OCR, or corpus changes;
- provider/API-key use, dependency changes, public-sync, or readiness claims.

## Write Ownership

| Path | Action |
| --- | --- |
| T4 shared fixture | CREATE |
| T4 TypeScript conformance test | CREATE |
| T4 Python conformance test | CREATE |
| T4 governance, GC-051, and continuity | CREATE/UPDATE |
| runtime source and external paths | FORBIDDEN |

## Forbidden Filesystem State At Dispatch

- all three T4 implementation target paths are absent;
- external Policy_Local remains outside the write set;
- no runtime source file is staged or modified.

## Pre-Flight Checks

1. Confirm HEAD descends from T3 closure `5f328d11` and sync `7b2204dc`.
2. Confirm T1-T3 artifacts exist and T3 is closed.
3. Confirm all three T4 implementation paths are absent.
4. Run reviewer-fast and pre-dispatch autorun on the real dispatch range.
5. Commit the dispatch packet before implementation.

## Execution Plan

1. Create one parseable JSON fixture with two explicit profiles.
2. Give each profile a disjoint requirement set and owner IDs.
3. Add resolved, unresolved, conflict, and not-applicable cases.
4. Consume the fixture in TypeScript and assert exact bridge outputs.
5. Consume the same fixture in Python and assert exact evaluation outputs.
6. Inject cross-profile ownership errors and assert canonical fail tokens.
7. Assert no raw content, Policy_Local candidate IDs, or global defaults.
8. Run focused, full, type-check, registry, and governance verification.

## Evidence Requirements

- one shared fixture path consumed by both suites;
- exact per-profile requirement IDs and owner maps;
- negative cross-profile bleed assertions;
- exact four-path resolution and downstream outcomes;
- fixture parse and forbidden-token checks;
- focused/full tests and TypeScript check PASS;
- changed-path and GC-051 evidence.

## Acceptance Criteria

1. Legal-policy requirements never appear in technical-project bridge output.
2. Technical-project requirements never appear in legal-policy bridge output.
3. Cross-profile requirement use fails closed in both surfaces.
4. Resolved, unresolved, conflict, and not-applicable cases match T1 semantics.
5. Both test suites consume the same fixture.
6. No runtime source is modified.
7. No real candidate ID, raw content, or Policy_Local path enters the fixture.
8. No global requirement or automatic gate release is introduced.
9. Focused/full tests, TypeScript check, registry checks, and gates pass.

## Review Gate

The reviewer must recompute requirement sets from the fixture, swap one
requirement across profiles, verify both canonical failure paths, and compare
the four expected outcomes against T1 rules rather than trusting test names.

## Closure Checklist

- [ ] Shared fixture exists and parses.
- [ ] Both focused suites consume the shared fixture.
- [ ] Cross-domain negative assertions pass.
- [ ] Four semantic paths pass.
- [ ] Full package tests and TypeScript check pass.
- [ ] GC-051 JSON and Markdown are updated.
- [ ] Reviewer-fast and pre-closure pass.
- [ ] Roadmap and continuity release only MEOR-T5.

## Return-To-Orchestrator Conditions

Return if conformance requires runtime changes, real Policy_Local data, new
semantics, global defaults, a dependency, provider use, retrieval, or a wider
claim.

## Operator Checkpoint

operator.checkpoint.waiver: operator explicitly authorized execution of the
full foundation roadmap. No additional checkpoint is required inside scope.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: DISPATCHED` | READY |
| Completion or reviewer artifact | T4 completion review | absent before execution | BLOCKED |
| Roadmap state | foundation roadmap | T4 dispatched; T5 held | READY |
| Registry JSON | GC-051 JSON | update after implementation | BLOCKED |
| Registry Markdown | GC-051 Markdown | update after implementation | BLOCKED |
| External evidence digest | N/A with reason: synthetic repo-local proof only | no external evidence | N/A with reason |
| System loop interlock | N/A with reason: no loop mutation planned | test-only tranche | N/A with reason |
| Session continuity | active state/memory/handoff | T4 execution next | READY |

## Claim Boundary

This work order authorizes synthetic cross-domain conformance only. It does not
authorize metadata correction, domain decisions, gate activation, retrieval,
provider use, external integration, or readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation test tranche; no public-sync authorized.
