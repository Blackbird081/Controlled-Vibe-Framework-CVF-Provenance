# QM Service-Token Replay Dedupe T1 Local Completion Review

Memory class: FULL_RECORD
docType: completion_review
Status: ACCEPTED_PENDING_MATERIAL_COMMIT
Date: 2026-09-14
closureBaseHead: ac1dd70612228c45d19e4b4b7d2ab1785204172f

## Purpose

Record Local acceptance of bounded process-local exact-request replay deduplication after one worker rework generation and one narrow reviewer benchmark correction. Material commit, continuity synchronization and committed-range closure remain subsequent steps.

## Target / Source

Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_2026-09-14.md`.
Baseline: `docs/baselines/CVF_GC018_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_2026-09-14.md`.
Worker return: `docs/reviews/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_WORKER_RETURN_2026-09-14.md`.

## Scope / Methodology

`EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`. Local inspected the changed verifier and hostile regressions, confirmed the prior F1/F2 root causes were resolved, then made one narrow reviewer-owned benchmark correction: exact same input per pair with alternating branch order. No production route, signature input, dependency, provider, network, live, public or deployment surface changed.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Replay lifetime covers the inclusive signature-validity interval | LOCAL_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts | replay ledger insertion | verifyServiceTokenRequest | service-token verifier | ACCEPT |
| Future-dated and boundary replay regressions | LOCAL_TEST | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts | hostile regression suite | future-dated timestamp replay lifetime | focused verifier tests | ACCEPT |
| Current consumer rejects an exact replay | LOCAL_TEST | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.test.ts | QBS replay case | POST direct invocation | current QBS consumer test | ACCEPT |
| Added latency is bounded by paired control | LOCAL_BENCHMARK | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/benchmark-service-token-replay-dedupe.ts | paired measurement | ledger-disabled versus enabled | bounded synthetic benchmark | ACCEPT |

## Findings / Position

| Finding | Decision | Evidence |
|---|---|---|
| F1 future-timestamp replay bypass | ACCEPT_REPAIRED | expiry is `timestampMs + window + 1`; pruning retains the entry at the last valid millisecond; five hostile regressions pass |
| F2 absolute-only benchmark | ACCEPT_REPAIRED | same-function ledger-disabled control; exact same input per pair; alternating branch order |
| Exact replay and consumer behavior | ACCEPT | focused suite passes 22/22; QBS first request returns 200 and exact replay returns 401 |
| Data/storage boundary | ACCEPT_BOUNDED | module stores only SHA-256 replay identity and numeric expiry; no raw token/body/header storage or emission |
| Capacity and lifecycle | ACCEPT | fixed 10,000 default, deterministic lazy prune, fail closed at unexpired capacity, no timer or I/O |
| Latency | ACCEPT_BOUNDED | reviewer runs: added median 0.0031 ms in both; added p95 0.0074 ms and 0.0053 ms, below 0.10/0.25 ms ceilings |
| GC-051 coverage | ACCEPT_REPAIRED | Local added one bounded registry source entry and regenerated the aggregate |

## Decision

Local accepts the implementation as `CLOSED_PASS_BOUNDED` pending the material commit. Technical rework ends; no further worker redispatch. The accepted claim is one-process exact valid-request deduplication only. Multi-process/shared/durable replay protection and all other parked QM candidates remain unopened.

## Evidence / Verification

- Focused Vitest: 2 files, 22/22 tests PASS.
- TypeScript: `npm run check` PASS.
- Reviewer benchmark run 1: added median 0.0031 ms; p95 0.0074 ms; PASS.
- Reviewer benchmark run 2: added median 0.0031 ms; p95 0.0053 ms; PASS.
- Exact material manifest before this completion artifact: five worker paths plus GC-051 source entry and generated aggregate.
- Failed-run and rework history remain preserved in the worker return.

## Risk / Corrective Action

Protection is process-local and resets on process restart. It does not coordinate across workers or instances. Capacity exhaustion intentionally denies new valid identities until expiry pruning reclaims space. These are accepted bounded behaviors, not deployment-wide guarantees.

## Review Cost Telemetry

Review-Cost Telemetry: REQUIRED
reviewRoundCount: 2
workerRepairTurnCount: 1
newRootCauseCountThisRound: 0
dependentFindingCountThisRound: 0
providerCallCount: 0
materialCommitCount: 0
continuityCommitCount: 0
elapsedReviewMinutes: NOT_AVAILABLE_WITH_REASON: review spans the worker relay boundary without a consolidated wall-clock meter
tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: no consolidated internal-worker usage meter
valueDelta: one concrete security defect and one measurement defect were repaired; reviewer validation now supports bounded acceptance without another worker round
stopDisposition: COMPLETE_REVIEW
preRepairAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR
commitPlanDisposition: DEFAULT_ONE_MATERIAL_ONE_CONTINUITY
latencyDisposition: WITHIN_FAST_PATH_TARGET
avoidableDelayClass: NONE

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE
outsideAuthorityBlockers: NONE
nextRepairRoute: Local material commit followed by continuity and committed-range verification.
workerRedispatchAllowed: NO

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | completion status, review telemetry, closeability, source verification, exact manifest and GC-051 coverage |
| gateRunPurpose | confirm reviewer acceptance structure and material-commit readiness |
| claimBoundary | accepted bounded implementation; no committed-range closure yet |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

No public artifact, public-sync or deployment is authorized in this tranche.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - GC-051 records the one new benchmark source only; no source-wide scan or completeness claim.

## Finding-To-Governance Learning Disposition

Defect classes: `WORKER_EXECUTION_ERROR`; `UNVERIFIED_CLAIM`.
Lane: `RUNTIME_BEHAVIOR_LEARNING`.
Disposition: `N/A_WITH_REASON` - the existing work-order contract, hostile regression tests and paired benchmark directly contain the two defects; no new general governance rule is justified.
Next control action: retain future-timestamp inclusive-boundary regression coverage and same-input alternating-order measurement for later replay-ledger changes.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_2026-09-14.md` | approved exact scope plus this Local acceptance decision | PASS |
| Completion or reviewer artifact | this completion review | `Status: ACCEPTED_PENDING_MATERIAL_COMMIT` | PASS |
| Roadmap state | `docs/roadmaps/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPLICATION_ROADMAP_2026-09-14.md` | T1 terminal acceptance is recorded by this completion review | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated aggregate includes `qm-service-token-replay-dedupe-t1-benchmark` | PASS |
| Registry Markdown | this completion review | human-readable GC-051 disposition and bounded source scope are recorded above | PASS |
| External evidence digest | N/A with reason: no new external artifact or digest is used by implementation acceptance | Local source/test evidence only | N/A with reason: no external evidence digest |
| System loop interlock | N/A with reason: no system-loop owner changed | no interlock mutation | N/A with reason: outside tranche |
| Session continuity | active front door, state and handoff | dedicated continuity synchronization follows the material commit | N/A with reason: post-material step |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: no live runtime receipt is claimed | N/A_WITH_REASON |
| Provider receipt evidence | N/A with reason: provider execution is forbidden | N/A_WITH_REASON |
| Focused implementation evidence | 22/22 synthetic/direct-route tests, TypeScript PASS and two paired benchmark runs | PASS |
| Worker-return acceptance | generation 1 evaluated and accepted with one documented Local measurement correction | PASS |
| Closure claim | bounded Local acceptance pending material and continuity commits | PASS |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | QM R1 M5 -> Local current-consumer verification -> bounded CVF-native implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` |
| Disposition | ADAPT without direct source copy |
| Claim boundary | no new source acquisition or source-wide completeness claim |

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/reviews/CVF_EXTERNAL_LOCAL_ABSORPTION_PROGRAM_CONTINUITY_HARDENING_2026-09-13.md"
}
```

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | process-local exact valid-request replay deduplication |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no live/provider receipt is asserted |
| actionEvidence | ACTION_EVIDENCE_PRESENT: focused synthetic verifier and direct-route tests |
| invocationBoundary | in-process verifier and route fixture only |
| interceptionBoundary | no shared-process or deployment-wide interception |
| claimLanguage | bounded process-local replay protection |
| forbiddenExpansion | distributed storage, M4, M7, provider/live, public and deployment |

## Expected Result / Prediction

The timestamp-pinned bounded ledger should reject an exact valid replay throughout the complete inclusive signature-validity interval without changing existing verifier call shape or exceeding the fixed added-latency ceilings.

## Evidence Comparison

Source inspection, 22/22 focused tests, TypeScript and two corrected paired benchmark runs match the expected result. Generation 0 contradicted expiry and benchmark requirements; generation 1 plus the narrow reviewer measurement correction resolves both.

## Contradiction Or Gap Disposition

No remaining technical contradiction was found. GC-051 was a reviewer-owned packaging gap and is now covered. Material/continuity commits remain pending rather than being treated as completed evidence.

## Claim Update

Local accepts only the process-local result. No cross-process guarantee, provider/live behavior, deployment readiness, whole-QM closure or three-repository completion follows.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer/closer |
| Provider or surface | internal workspace |
| Session or invocation | QM-SERVICE-TOKEN-REPLAY-DEDUPE-T1-review |
| Working directory | repository root and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` |
| Command or tool surface | source/diff inspection, focused tests, TypeScript, paired benchmark, GC-051 generator and reviewer gates |
| Target paths | eight-path material manifest |
| Allowed scope source | work-order Reviewer Closure Conversion and Local reviewer authority |
| Before status evidence | HEAD `ac1dd70612228c45d19e4b4b7d2ab1785204172f`; exact five worker paths pending |
| After status evidence | same HEAD; eight material paths pending including this completion review and GC-051 coverage |
| Diff evidence | `git status --short`; `git diff --name-status`; generated-registry check |
| Approval boundary | reviewer validation, narrow benchmark correction, GC-051 packaging and acceptance |
| Claim boundary | material acceptance only; continuity and committed-range closure remain pending |
| Agent type | Local reviewer |
| Invocation ID | QM-SERVICE-TOKEN-REPLAY-DEDUPE-T1-review-generation-1 |
| Expected manifest | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.test.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/benchmark-service-token-replay-dedupe.ts`; `docs/reviews/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_WORKER_RETURN_2026-09-14.md`; `docs/corpus-intelligence/registry/entries/qm-service-token-replay-dedupe-t1-benchmark.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; this completion review |
| Actual changed set | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.test.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/benchmark-service-token-replay-dedupe.ts`; `docs/reviews/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_WORKER_RETURN_2026-09-14.md`; `docs/corpus-intelligence/registry/entries/qm-service-token-replay-dedupe-t1-benchmark.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; this completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## P4 Automatic Evidence Observation Block

p4ObservationEligibility: NO
p4ObservationPhase: N/A with reason: not a natural P4 observation candidate
p4HardObligationLocator: N/A with reason: not a natural P4 observation candidate
p4HardObligationPattern: N/A with reason: not a natural P4 observation candidate
p4SourceAuthorityLocator: N/A with reason: not a natural P4 observation candidate

## Claim Boundary

Reviewer acceptance of bounded process-local service-token replay deduplication only. No shared/durable replay protection, credentials, provider/live proof, public export, deployment, production readiness, whole-QM closure or active-program completion.
