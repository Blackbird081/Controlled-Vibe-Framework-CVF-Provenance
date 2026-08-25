# CVF GC-018 Baseline - EAFR-R1 AIF Reinjection Provenance Fail Closed

Memory class: SUMMARY_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-25

Batch ID: EAFR-R1-AIF-REINJECTION-PROVENANCE-FAIL-CLOSED

Dispatch base head: `80bf3e850`

Commit mode: `WORKER_MUST_NOT_COMMIT`

rawMemoryReleased=false

Decision owner: operator through explicit 2026-08-25 orchestrator authority

Reviewer owner: current independent orchestrator/reviewer

Worker target: one delegated implementation-and-test worker role

## Purpose

Close the AIF reinjection provenance omission gap without widening caller
authority or changing route composition. Missing, explicit-undefined, and
non-finite item provenance must be excluded before selection and prompt build.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R1-AIF-REINJECTION-PROVENANCE-FAIL-CLOSED --title "CVF EAFR-R1 AIF Reinjection Provenance Fail Closed" --date 2026-08-25 --base 0fcc1dc20 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "archive hygiene closed at 0fcc1dc20" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact source/test manifest, fail-closed semantics, adversarial cases and live-proof prohibition |
| checkerReadAheadConfirmation | dispatch, prompt-envelope, read-ahead, structural, trace, worker-return and lifecycle checkers routed before authoring |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no runtime remediation claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| EAFR roadmap | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | R1 must be the first executable tranche | ACCEPT |
| archive hygiene | commit `0fcc1dc20` | advisory history preserved and active tree clean | ACCEPT |
| source gap | source line 99 defaults omitted provenance to `1` | omission must fail closed | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| provenance is optional at request boundary | RUNTIME_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts` | line 7 | `provenanceScore` | `AifMemoryReinjectionItem` | ACCEPT |
| omission defaults to trusted score | RUNTIME_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts` | line 99 | `item.provenanceScore ?? 1` | `evaluateAifMemoryReinjection` | ACCEPT |
| selected items enter prompt block | RUNTIME_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts` | lines 103-136 | `eligible`, `selected`, `promptBlock` | `evaluateAifMemoryReinjection` | ACCEPT |
| prompt block reaches execute composition | RUNTIME_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 746-790 | `evaluateAifMemoryReinjection`; `executeAI` | execute route | ACCEPT |
| existing tests lack omission/non-finite cases | TEST_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.test.ts` | four tests at lines 10-75 | AIF memory reinjection gate suite | Vitest | ACCEPT |

## Scope

Worker may modify exactly the AIF helper and its existing test, then create the
named worker return. The execute route is read/hash-only because it already
consumes the helper result. No schema, policy-owner, provider or documentation
change is authorized.

## Acceptance Invariants

- Keep `provenanceScore` optional at the boundary so malformed inputs produce a
  governed exclusion receipt rather than a compile-only rejection.
- Missing and explicit-undefined scores are excluded with stable reason
  `missing_provenance_score`.
- `NaN`, positive infinity, and negative infinity are excluded with stable
  reason `invalid_provenance_score`.
- Finite values below the existing threshold retain
  `low_provenance_score`; the default boundary value `0.7` remains eligible.
- Excluded items never enter `selected`, `memoryIds`, or `promptBlock`.
- Existing actor, policy, kind, secret, dispute, expiry and max-item behavior
  remains unchanged.

## Baseline Decision

`PROCEED_FAIL_CLOSED_IMPLEMENTATION`: add an explicit provenance validation
step before the existing threshold comparison and prove it adversarially.

## Evidence Verification

Required closure evidence is focused adversarial Vitest, package typecheck,
full non-live suite, production build, unchanged execute-route hash, exact
three-path worker manifest, worker-return fast gate and independent review.

## Source Hash Manifest

| Path | SHA-256 at dispatch | Authority |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts` | `08811dff6dcef5acf078951bb93d6d7b84e2184b4a91c4e63a6fea051ea93d5e` | edit |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.test.ts` | `8880ded282d365a7de95ec56d530d8525e282d76a613f1e6d1da681d5a09e5f4` | edit |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | worker records dispatch hash and MATCH at return | read/hash only |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| planned paths | all four planned roadmap/baseline/work-order/return paths absent before authoring | ACCEPT |
| batch token | `rg` over `docs CVF_SESSION` returned no collision | ACCEPT |
| production owner | helper and test are the only required edit surfaces | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_repository_lifecycle_classification.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; source verification columns; dependency release evidence |
| gateRunPurpose | confirm and record evidence for the already source-verified dispatch; not first discovery |
| claimBoundary | checker PASS cannot substitute for tests or reviewer closure |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private runtime safety repair; no public-sync action is authorized.

## Claim Boundary

This baseline authorizes two source/test edits and one worker return. It does
not authorize live/provider calls, credentials, policy threshold redesign,
execute-route edits, deployment, public sync, push, commit, or readiness claims.
