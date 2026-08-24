# CVF GC-018 Baseline - RFR-R1 Build Authority Closure

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-24

Batch ID: RFR-R1

Dispatch base head: `e196899548d04f88ee5bc40cfce1ddf268a29d6b`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: current orchestrator/reviewer/closer

Worker target: separate external implementation agent

## Purpose

Authorize a bounded Guard Contract change that makes mutating BUILD fail closed
unless typed evidence proves an accepted SPEC and a valid, non-revoked,
non-expired, target-bounded WORK ORDER.

## Authorization

The operator's 2026-08-24 instruction to resolve the verified findings before
absorption or coding releases RFR-R1 only. R2-R6, provider/live, credentials,
deployment and public synchronization remain parked.

## Dependency Release Evidence

| Dependency | Evidence | Release rule | Disposition |
|---|---|---|---|
| findings verified | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | F1 is HIGH `RUNTIME_AUTHORITY_GAP` | ACCEPT |
| tranche ordered | `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md` | R1 is first implementation tranche | ACCEPT |
| operator authority | explicit 2026-08-24 proceed instruction following the remediation plan | bounded remediation authorized | ACCEPT |

## Scope

- add typed BUILD authority evidence to `GuardRequestContext`;
- add a mandatory `build_authority` guard using existing action-intent logic;
- register and export it in the shared factory;
- add dedicated positive and negative tests;
- add one no-commit worker-return packet.

## Non-Goals

No phase-enum expansion, SPEC/WORK ORDER storage or issuer, filesystem lookup,
signature scheme, engine/gateway/MCP/Web edit, config hardening, provider/live
call, session sync, deployment, public sync, staging, or commit by worker.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| five phases remain canonical | TYPE_MODEL | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | lines 21-27 | `CanonicalCVFPhase` | Guard Contract types | ACCEPT |
| request context lacks BUILD authority evidence | TYPE_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | lines 93-110 | `GuardRequestContext` | Guard Contract types | ACCEPT |
| mandatory core omits BUILD authority | COMPOSITION_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | line 262 | `MANDATORY_GUARD_IDS` | Guard Contract types | ACCEPT |
| shared factory is canonical composition | COMPOSITION | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | lines 380-392 | `createGuardEngine` | Guard Contract root | ACCEPT |
| mutation intent owner is reusable | OWNER_REUSE | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/action-intent.ts` | helper exports | `hasModifyIntent` | Guard Contract guards | ACCEPT |
| current BUILD tests do not require SPEC/WORK ORDER | TEST_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts` | PhaseGate and AuthorityGate suites | positive BUILD cases | Guard Contract tests | ACCEPT |

## Required Runtime Invariant

For `phase=BUILD` and `hasModifyIntent(action)=true`, the default engine must
return `BLOCK` unless all conditions hold:

- `specStatus` is exactly `ACCEPTED` and `acceptedSpecRef` is non-empty;
- `workOrderStatus` is exactly `VALID` and `workOrderRef` is non-empty;
- `revoked` is not true;
- an optional `expiresAt` parses as a valid timestamp strictly after evaluation;
- every target file is within an explicitly listed work-order scope;
- empty or missing authority evidence fails closed.

Non-BUILD, phase-transition and genuinely read-only actions remain outside this
new guard. Existing guards retain their own authority.

## Acceptance Criteria

- `build_authority` is a member of `MANDATORY_GUARD_IDS` and cannot be disabled
  or unregistered through existing APIs;
- `createGuardEngine()` registers and exports the new guard;
- missing SPEC, rejected SPEC, missing WORK ORDER, expired/revoked WORK ORDER,
  missing scope, and out-of-scope targets each block with stable reason codes;
- valid evidence and in-scope targets allow this guard but do not bypass any
  other guard;
- dedicated tests cover direct guard and shared-factory composition;
- package typecheck and focused/full Guard Contract tests pass;
- exact five-path worker manifest, unchanged HEAD and empty staging.

## Decision / Baseline

Proceed with a typed, deterministic mandatory guard inside the existing Guard
Contract. Do not convert SPEC or WORK ORDER into runtime phases and do not add a
new storage, approval, registry, or execution subsystem.

## Evidence / Verification

Worker evidence must include focused tests, full Guard Contract tests,
typecheck, file-size guard, worker-return fast gate, diff check, exact status,
empty staging and unchanged HEAD. Reviewer must independently add adversarial
scope and time-boundary cases before acceptance.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R1 --title "Runtime Finding Remediation R1 Build Authority Closure" --date 2026-08-24 --base e196899548d04f88ee5bc40cfce1ddf268a29d6b --commit-mode WORKER_MUST_NOT_COMMIT --dependency "operator remediation authorization on 2026-08-24" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker return |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified invariant, exact manifest, negative matrix, role split and claim boundaries |
| checkerReadAheadConfirmation | applicable checker sources were read before authoring |
| docOnlyNewFields | reason-code taxonomy in dispatch only; runtime fields are worker-owned implementation |
| claimBoundary | scaffold provenance does not prove implementation |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; exact manifest; worker-return headings; Public Export Disposition |
| gateRunPurpose | confirm R1 packet requirements before dispatch |
| claimBoundary | structural conformance is not runtime closure proof |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact artifact paths | `Test-Path` returned false for all proposed dispatch, guard, test and return paths | ABSENT_BEFORE_AUTHORING |
| exact symbols | repository search found no `BuildAuthority` or `build_authority` owner | NO_SAME_OWNER_COLLISION |
| owner decision | action intent and engine composition are reused; only the missing guard is new | EXISTING_OWNER_ENRICHMENT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 50 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no additional ADIF constraint; canonical guards remain binding |

## Machine Closure Package

Worker owns only the three production/test edits and pending return. Reviewer
owns repairs within that manifest, completion review, roadmap disposition,
material commit and later continuity sync. R2 stays parked.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | R1 dispatch authorization only |
| claimDisposition | CLAIM_REJECTED until worker evidence and independent review |
| receiptEvidence | N/A with reason: no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatcher made no runtime edit |
| invocationBoundary | governed local document authoring and pre-dispatch checks |
| interceptionBoundary | CLAIM_REJECTED_NO_RECEIPT |
| claimLanguage | dispatch-ready only |
| forbiddenExpansion | no later tranche, provider/live, deployment or public claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes R1 construction and local tests only. It does not prove
the invariant is implemented, deployed, live, universally adopted, or closed.
