# CVF EAFR-R7 Fail-Closed Provider Egress Authority Repair Completion Review

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_CLOSED_BLOCKED

Date: 2026-08-26

docType: review

rawMemoryReleased=false

## Target / Source

| Field | Value |
| --- | --- |
| Baseline | `docs/baselines/CVF_GC018_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_2026-08-26.md` |
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_2026-08-26.md` |
| Worker return | `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_WORKER_RETURN_2026-08-26.md` |
| executionBaseHead | `b58f9b6cb5f3eeb20a1faab2d7bb735131673f6c` |
| Reviewer | independent orchestrator/reviewer/closer |

## Purpose

Independently adjudicate the R7 fail-closed repair, four R6 P1 row
dispositions, the newly admitted Upstash non-live egress defect, and whether
the repaired control should be retained while a successor repair is prepared.

## Scope / Methodology

The reviewer read the guard, focused tests, rate-limit implementation, setup
environment loader, Vitest configuration, gateway endpoint owners, adapter and
worker return. The reviewer reran the focused suite, TypeScript, full non-live
suite and worker-return fast gate. No live mode, provider call, network command,
credential action, build, public-sync, deployment or push occurred.

## Findings / Position

Position: `REVIEWER_ACCEPTED_CLOSED_BLOCKED` after bounded reviewer repair.

### R7-RF1 - fail-open direction is repaired

Unrecognised HTTP(S) destinations now deny before the wrapped fetch. Relative
paths, `data:`, `blob:`, `file:` and loopback are the only non-provider permit
classes. Known provider destinations still require the existing bounded grant.
Mainland DashScope coverage is derived from the gateway endpoint constant and
does not appear as a hostname literal in the guard.

### R7-RF2 - reviewer closed a protocol-relative bypass

The worker treated every string beginning with `/` as relative. A value such as
`//attacker.invalid/payload` is protocol-relative and can resolve to an external
host when the underlying fetch has a base URL. The reviewer narrowed the permit
branch to a single leading slash and added denial-before-fetch coverage, plus
explicit blob/file permit tests. Focused proof is 26 of 26 and TypeScript is
green.

### R7-RF3 - Upstash blocker is real and pre-existing

Fresh full non-live proof selected 313 files and 3553 tests: 297 files passed,
16 failed; 3465 tests passed and 88 failed. Twenty failures are the parked PVV
provider-authority denials, two are named BuildAuthority residuals, and the 66
additional failures all originate from the same denied Upstash destination.
The guard blocks it before network I/O.

This traffic was newly admitted to EAFR, not newly known to the repository. A
test comment committed at `cab8133ea` already states that `.env.local` loads
real Upstash credentials and that route tests otherwise mutate the remote
rate-limit state. The global non-live setup still loads those ambient values.

### R7-RF4 - allowlisting Upstash is rejected

Allowlisting a workspace-specific third-party hostname would recreate the
hardcoded drift mechanism R7 repairs and would preserve remote mutation in the
non-live suite. The accepted owner decision is to isolate ambient external
datastore configuration in non-live setup and prove Redis behavior only with an
injected fake client. That repair belongs to a successor tranche.

### R7-RF5 - four P1 dispositions remain bounded

| R6 row | Reviewer disposition |
| --- | --- |
| Mainland DashScope constant | `RESOLVED_FAIL_CLOSED` |
| Three endpoint environment overrides | `RESOLVED_FAIL_CLOSED` |
| Caller-supplied adapter endpoints | `BOUNDED_WITH_ACCEPTED_RESIDUAL` |
| Out-of-process harnesses | `CLASSIFIED_OUT_OF_REMIT` |

The adapter can still receive an unguarded injected fetch outside the cvf-web
process. That residual alone keeps RFR parked. The out-of-process classification
does not claim universal interception.

### R7-RF6 - evidence arithmetic and continuity were repaired

The worker correctly reported the pre-repair 3533 total but failed to add its
17 new focused tests to the post-repair total. The reviewer corrected the
return: worker-post is 3550; reviewer-post is 3553 after three additional
regressions. The dispatch continuity handoff mode mismatch was independently
repaired in commits `eaa35a7b7` and `6c54d0adf`; worker-return fast gate then
passed 66 of 66.

## Risk / Corrective Action

Retain the fail-closed repair because reverting it would restore silent external
egress. Open EAFR-R8 only for two named controls: non-live ambient external-store
isolation with injected fake Redis proof, and closure of the adapter's unguarded
fetch-injection residual. RFR, provider/live, build and external effects remain
parked.

## Reviewer Decision

Accept R7 as `CLOSED_BLOCKED`. The safety repair and first two P1 resolutions
are accepted, but the full non-live suite is intentionally red on a disclosed
external dependency and the adapter residual remains. RFR must not resume.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_roadmap_closure_freshness.py` |
| literalTokensReviewed | review structure, blocked disposition, reviewer repair, Public Export Disposition, Machine Closure Package |
| gateRunPurpose | confirm direct source inspection and recomputed evidence, not discover required packet shape |
| claimBoundary | checker conformance does not clear Upstash or adapter residuals |

## Review Cost Telemetry And Stop Disposition

- `reviewRoundCount`: 1
- `workerRepairTurnCount`: 0
- `newRootCauseCountThisRound`: 2 reviewer findings: protocol-relative bypass and evidence arithmetic
- `dependentFindingCountThisRound`: 2
- `elapsedReviewMinutes`: NOT_AVAILABLE_WITH_REASON: exact governed wall-clock telemetry unavailable
- `providerCallCount`: 0
- `tokenOrQuotaUsage`: NOT_AVAILABLE_WITH_REASON: zero provider calls
- `valueDelta`: retained fail-closed repair, closed one bypass, corrected evidence, selected safe successor direction
- `stopDisposition`: COMPLETE_REVIEW_BLOCKED
- `preRepairAuditDisposition`: REPAIR_REQUIRED_BEFORE_ACCEPTANCE
- `materialCommitCount`: 1
- `continuityCommitCount`: 1
- `commitPlanDisposition`: DEFAULT_ONE_MATERIAL_ONE_CONTINUITY
- `latencyDisposition`: EXTENDED_WITH_REASON: full 313-file suite recomputed
- `avoidableDelayClass`: NONE

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| non-live setup loads ambient external-store credentials | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | R8 isolates the environment and proves Redis through an injected fake |
| protocol-relative strings passed the relative-path permit branch | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | reviewer regression retained in R7 source |
| worker post-test total omitted newly added tests | WORKER_EXECUTION_ERROR | EVIDENCE_INTEGRITY | RULE_EXISTS | reviewer corrected arithmetic before acceptance |

runtimeProviderCostLearningLane: INCIDENT_RECORDED - zero R7 worker and reviewer
provider calls; historical DashScope traffic remains permanently unquantified.

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE_REVIEW
- Expected Result / Prediction: default deny would close the provider-host bypasses while preserving legitimate non-live traffic.
- Evidence Comparison: provider-host bypasses closed, but ambient Upstash credentials exposed pre-existing real datastore egress; reviewer also found a protocol-relative permit bug.
- Contradiction Or Gap Disposition: keep the safer default, repair the local bypass, close R7 blocked and route datastore isolation plus adapter narrowing to R8.
- Claim Update: R7 is materially valuable but not green; RFR remains parked.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | independent orchestrator/reviewer/closer |
| Provider or surface | private local repository; zero provider calls |
| Session or invocation | EAFR-R7 independent review, 2026-08-26 |
| Working directory | repository root and cvf-web package |
| Command or tool surface | source inspection, bounded searches, focused/full non-live Vitest, TypeScript and governance gates |
| Target paths | R7 guard/test, repaired worker return, this completion review and EAFR roadmap |
| Allowed scope source | committed R7 packet and standing reviewer/closer authority |
| Before status evidence | HEAD `b58f9b6cb`; three worker paths dirty; staging empty |
| After status evidence | reviewer-repaired R7 material closure pending commit; staging empty |
| Diff evidence | exact diff, direct source review, 26/26 focused and 3553-test full suite |
| Approval boundary | R7 review and blocked closure only |
| Claim boundary | no Upstash allowlist, provider/live, build, RFR resume or external effect |
| Agent type | reviewer/closer |
| Invocation ID | `eafr-r7-review-2026-08-26` |
| Expected manifest | R7 guard/test, worker return, completion review and EAFR roadmap |
| Actual changed set | MATCH_WITH_DISCLOSED_REVIEWER_REPAIR |
| Manifest delta | completion review and roadmap are reviewer-owned closure paths |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | process-local R7 egress repair and blocked closure |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: 26/26 focused, TypeScript PASS, 3465 pass/88 named fail, reviewer-fast 66/66 |
| actionEvidence | ACTION_EVIDENCE_PRESENT: fail-closed inversion, gateway derivation, protocol-relative repair and owner decision against allowlisting |
| invocationBoundary | local non-live tests and governance only; zero provider calls |
| interceptionBoundary | one Vitest process global fetch only; no OS, proxy, subprocess or production interception claim |
| forbiddenExpansion | RFR resume, provider/live, build, credential use, public sync, deployment and push |
| claimLanguage | R7 closes blocked and retains a safer local control while named residuals move forward |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair and blocked closure; no public-sync authority.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | committed R7 packet | `WORKER_MUST_NOT_COMMIT` honored | PASS |
| Completion or reviewer artifact | this review | `REVIEWER_ACCEPTED_CLOSED_BLOCKED` | PASS |
| Worker return | R7 return | accepted after disclosed reviewer repairs | PASS |
| Test evidence | focused/typecheck/full non-live | 26/26; zero diagnostics; 3465 pass/88 named fail | PASS_BOUNDED |
| Reviewer governance | worker-return fast gate | 66/66 PASS | PASS |
| Roadmap state | EAFR roadmap | R7 blocked; R8 planning next; RFR parked | PASS |
| Registry JSON | N/A with reason: no registry classification change | none | PASS |
| Registry Markdown | N/A with reason: no projection change | none | BLOCKED with reason: not applicable |
| External evidence digest | N/A with reason: none consumed | none | N/A with reason |
| System loop interlock | R6 blocked -> R7 blocked -> R8 planning | explicit successor boundary | PASS |
| Session continuity | separate post-material sync | material commit required first | BLOCKED with reason: material commit pending |

## Claim Boundary

This review accepts a process-local fail-closed repair and closes R7 only as a
blocked tranche. It does not authorize real Upstash egress, clear the adapter
residual, resume RFR, call a provider, build, publish, deploy, push, or make a
universal security or production-readiness claim.
