# CVF GC-018 Baseline - CADP-AI-T4 Authority Boundary Machine Enforcement

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-14

Batch ID: CADP-AI-T4

Dispatch base head: `783f18637434aad1a611d20b89c46a676c61151e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Independent reviewer/closer

Worker target: implementation worker role

## Purpose

Authorize a hermetic, read-only drift checker for the accepted CADP T1, T3A,
and T3B authority boundaries. The checker must validate a strict fixture,
detect every named negative mutation, and prove package-root discoverability
without changing production contracts or claiming runtime enforcement.

## Authorization

The operator's 2026-08-14 `continue` direction releases the next ordered T4
tranche after bounded T3B closure. It does not release T5-T7, provider/live
execution, credentials, external adapters, deployment, public sync, or hook
wiring.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T3B accepted bounded | `docs/reviews/CVF_CADP_AI_T3B_MODEL_GATEWAY_CONSTRAINT_PROJECTION_COMPLETION_2026-08-13.md`; material commit `9a4920c92cdc5f44692c0e8b3ab213db379ae5c8` | independent acceptance plus explicit operator continuation | ACCEPT |
| T4 roadmap entry | `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md`, Work Plan T4 | repeated accepted invariant and fresh checker GC-018 | ACCEPT |

## Scope

- add one strict JSON fixture describing the accepted CADP authority-boundary
  surfaces and package-root exports;
- add one read-only Python checker that accepts `--json` and `--enforce`;
- add one Python test module with positive real-repository proof and a
  temporary negative corpus for every named violation class;
- add one worker-return packet with executed evidence;
- preserve all accepted TypeScript contract and test files byte-for-byte.

## Non-Goals

No TypeScript production edit, checker hook/autorun/CI wiring, provider call,
secret resolution, runtime interception, CLI/MCP adapter, deployment, public
sync, registry regeneration, roadmap closure, session sync, or commit.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | `Core Guard Self-Protection Authorization`; `Authorized guard-maintenance scope`; `Protected paths`; `Operator authorization`; `Rollback boundary`; `WORKER_MUST_NOT_COMMIT`; worker-return required headings and read-ahead fields |
| gateRunPurpose | confirm exact protected-path authorization and dispatch/return shape before authoring |
| claimBoundary | structural checks do not prove checker semantics or T4 completion |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1 admission and assignment cannot grant execution authority | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts` | declarations and validators around lines 26, 76, 89, 437, 472, 503 | `CADP_CONTRACT_VERSION`; `executionAuthorized` | CADP Guard Contract | ACCEPT |
| T3A emits pre-execution eligibility with literal false authority | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/cadp.capability.consumer.contract.ts` | contract/projection declarations around lines 31, 66-69, 96, 299 | `CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION`; `executionAuthorized` | Execution Plane CADP consumer | ACCEPT |
| T3A is exported through its package root | PACKAGE_BOUNDARY | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | CADP export block around lines 1420-1434 | `CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION`; `evaluateCadpCapabilityConsumer` | Execution Plane root barrel | ACCEPT |
| T3B keeps four authorization fields literal false and provider-neutral | LITERAL_INVARIANT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/cadp.constraint.projection.contract.ts` | contract version, projection, and result builders | `executionAuthorized`; `liveExecutionAuthorized`; `providerCallAuthorized`; `credentialResolutionAuthorized` | Model Gateway CADP constraint projection | ACCEPT |
| T3B is exported through its package root | PACKAGE_BOUNDARY | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | CADP export block around lines 383-403 | `CADP_CONSTRAINT_PROJECTION_CONTRACT_VERSION`; `evaluateCadpConstraintProjection` | Model Gateway root barrel | ACCEPT |
| T4 is checker-only and has no hook wiring | ROADMAP_BOUNDARY | `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md` | External Absorption Value Conversion Matrix | `negative fixtures/checker`; `no hook wiring` | CADP-AI roadmap | ACCEPT |

## Named Violation Taxonomy

| Code | Required detection |
|---|---|
| `FIXTURE_SCHEMA_INVALID` | malformed JSON, unknown/missing keys, duplicate IDs, unsafe paths, or invalid expected types |
| `SURFACE_MISSING` | a fixture-owned contract or package-root file is absent |
| `CONTRACT_VERSION_DRIFT` | required version symbol/value is absent or changed |
| `AUTHORITY_TYPE_WIDENED` | a protected authorization property is no longer declared literal `false` |
| `AUTHORITY_VALUE_WIDENED` | a protected output assignment is missing or permits a non-false value |
| `FORBIDDEN_EXECUTION_SEAM` | a fixture-listed execution, provider, network, process, or credential-resolution seam appears in an owned contract |
| `PACKAGE_EXPORT_DRIFT` | a required symbol/module is no longer exported from the package root |

## Acceptance Criteria

- the fixture schema is closed and rejects unknown keys and unsafe paths;
- the checker is deterministic, read-only, repository-root aware, and emits a
  stable JSON report plus nonzero `--enforce` exit on violations;
- each taxonomy code has at least one isolated negative-corpus test;
- real-repository validation passes against the accepted T1/T3A/T3B sources;
- package-boundary tests verify required symbols and module specifiers, not
  only local source tokens;
- checker/test code remains within the governed file-size limits;
- no protected path outside the exact manifest changes;
- worker leaves staging empty, HEAD unchanged, and returns
  `COMPLETE_PENDING_INDEPENDENT_REVIEW` or `BLOCKED_WITH_REASON`.

## Decision / Baseline

Proceed with one standalone fixture-driven checker and its focused test under
`WORKER_MUST_NOT_COMMIT`. The accepted TypeScript sources remain immutable and
hook/autorun wiring remains outside T4.

## Evidence / Verification

Worker evidence requires the focused Python suite, direct checker JSON/enforce
run against the real repository, read-only corpus proof, core-guard and
file-size checks, `git diff --check`, exact pending status, empty staging, and
unchanged HEAD. Independent reviewer evidence remains required for acceptance.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create the bounded CADP T4 checker and its
focused test only.

Protected paths:

- `governance/compat/check_cadp_authority_boundary_drift.py`
- `governance/compat/test_check_cadp_authority_boundary_drift.py`

Operator authorization: the operator's 2026-08-14 `continue` releases T4 under
this exact manifest and no broader guard-maintenance scope.

Rollback boundary: delete only the two new Python paths and the new fixture if
independent review rejects the implementation; do not modify or remove any
pre-existing guard, contract, test, hook, catalog, or session surface.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id CADP-AI-T4 --title "CADP AI T4 Consumer Boundary Machine Enforcement" --date 2026-08-14 --base 783f18637434aad1a611d20b89c46a676c61151e --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CADP-AI-T3B accepted bounded at 9a4920c92cdc5f44692c0e8b3ab213db379ae5c8" --include-worker-return-skeleton --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-verified T4 scope, taxonomy, manifest, authorization, and claim boundaries |
| checkerReadAheadConfirmation | checker sources listed above were read before governed authoring |
| docOnlyNewFields | named violation taxonomy; no runtime schema field introduced |
| claimBoundary | dispatch provenance only; no machine-enforcement completion claim |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Exact path existence | `rg --files` and `Test-Path` equivalent searches found none of the six proposed artifact names before authoring | ABSENT_BEFORE_AUTHORING |
| Token search | `rg -n --fixed-strings` across `docs`, `governance`, `CVF_SESSION`, and `EXTENSIONS` found no proposed checker, fixture, baseline, work-order, or return name | NO_SAME_TOKEN_COLLISION |
| Collision decision | generic CADP/checker terms occur elsewhere with different owners; the exact T4 paths and checker ownership are new and bounded | NON_AUTHORITATIVE_COLLISIONS_NOT_BINDING |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cadp`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cadp --risk-ceiling HIGH --max-results 10 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no additional ADIF constraint; canonical guards and source boundaries still apply |

## Machine Closure Package

Worker owns only fixture, checker, test, and pending return. Reviewer owns any
repair, completion review, roadmap/registry update, material commit, and later
session-sync commit. T5 remains parked after worker return.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | dispatch authorization for a local static checker only |
| claimDisposition | CLAIM_REJECTED until worker execution and independent review |
| receiptEvidence | N/A with reason: no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatcher performed no T4 implementation |
| invocationBoundary | governed document authoring and local pre-dispatch gates |
| interceptionBoundary | CLAIM_REJECTED_NO_RECEIPT: no runtime interception |
| claimLanguage | T4 dispatch-ready only; no checker PASS or closure claim |
| forbiddenExpansion | no TypeScript semantics, runtime/provider/live, production, adapter or public claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance checker dispatch only; no public-sync authorization.

## Claim Boundary

This baseline authorizes construction and local verification of a bounded
static drift checker. It does not claim current machine enforcement, semantic
equivalence to TypeScript compilation, runtime interception, provider safety,
live proof, production readiness, or T4 closure.
