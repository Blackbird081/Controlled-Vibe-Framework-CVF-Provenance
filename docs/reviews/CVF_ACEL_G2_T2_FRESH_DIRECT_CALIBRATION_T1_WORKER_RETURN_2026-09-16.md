# CVF ACEL G2 T2 Fresh Direct Calibration T1 Worker Return

Memory class: governed-worker-return

Status: COMPLETE_PENDING_REVIEW

docType: worker_return

Date: 2026-09-16

Batch ID: ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_2026-09-16.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_2026-09-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: GRANTED_BUT_NOT_EXERCISED

executionBaseHead: `eca0182c4811a371f6db49a7b8b71d136180f056`

## Purpose

Return the ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1 attempt to the reviewer as
pending, non-authoritative evidence. This worker retargeted the existing
one-call runner to `qwen3.7-flash` and a new dated receipt path, verified all
prerequisites that source or public documentation can prove, found the
account's Free Quota Only toggle state unprovable by any tool available in
this session, and stopped at zero calls rather than risk paid exposure. The
historical 2026-07-17 receipt was left byte-identical.

## Target / Source

| Artifact | Role |
|---|---|
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_2026-09-16.md` | governing work order |
| `docs/baselines/CVF_GC018_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_2026-09-16.md` | paired dispatch baseline |
| `docs/audits/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.md` | T0 qualification audit |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts` | retargeted runner (worker-owned) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` | read-only inspection of live quota-status function |
| `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json` | read-only stale ledger snapshot |
| `docs/reviews/evidence/mao-oa-t6a-direct-candidate-calibration-2026-07-17.json` | read-only historical receipt (forbidden write target) |
| `https://www.alibabacloud.com/help/en/model-studio/model-pricing` | live-fetched public pricing documentation |
| `https://www.alibabacloud.com/help/en/model-studio/new-free-quota` | live-fetched public Free Quota Only documentation |

## Scope / Methodology

Captured `git rev-parse HEAD` and `git status --short --untracked-files=all`
before any edit; confirmed HEAD matched the dispatch `executionBaseHead`
(`eca0182c4811a371f6db49a7b8b71d136180f056`) and the worktree was clean. Ran
the pre-implementation autorun gate before editing. Confirmed an approved key
alias (`ALIBABA_API_KEY`) is present in `.env.local` without reading or
printing its value. Hashed the historical receipt
(`c5526054595a41ea990b5e125ea698d51fe3f0bb5768d80f4fdb7c1b005f6159`) before
any write and confirmed the new T1 receipt path did not already exist.
Retargeted exactly `MODEL_ID` (`qwen3.7-plus` -> `qwen3.7-flash`),
`RESULT_PATH`, and header/usage comments in the runner; left prompt, parser,
rubric, call/retry logic, key loader, and evidence shape untouched. Ran the
22 focused pure-scorer tests
(`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.harder.value.candidate.contract.test.ts`)
offline; did not run the live runner as a test. Live-fetched the two public
Alibaba documentation pages named by the baseline to refresh pricing and the
Free Quota Only mechanism description. Read
`EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` in full
and confirmed `getAlibabaFreeQuotaStatus()` only compares the static ledger's
`expirationDate` field to the current date; it contains no live account query
and no Free Quota Only toggle check. Concluded the account's actual Free
Quota Only toggle state and live remaining balance cannot be proven by any
tool or code path available to this worker session (no browser/authenticated
console access, no repo API surface for it). Per the work order's fail-closed
contract ("If any cannot be proven, stop at zero calls"), wrote a
zero-call `BLOCKED_WITH_REASON` receipt instead of attempting the live call.
Made no other source, test, runtime, package, checker, or session-state
mutation. Invoked no agent or subagent. Read no raw credential value.

## Findings / Position

**Prerequisite verification finding:** of the required pre-flight checks,
clean execution HEAD, key-alias presence, new-receipt-path absence, and
historical-receipt-hash capture were all directly proven from local state.
Current public pricing for `qwen3.7-flash` (International/Singapore tiered
rate, plus a 1M-token/90-day free-quota program) was confirmed by a live
fetch of the Alibaba Model Studio pricing page on 2026-09-16. The static
ledger snapshot (`docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json`,
captured 2026-09-10) resolves `qwen3.7-flash` as unexpired
(`expirationDate: 2026-10-22`), but this snapshot explicitly self-declares
its captured balance is not a live balance, and the runner's
`getAlibabaFreeQuotaStatus()` function performs no live query -- it is a
pure date comparison against the static ledger.

**Free Quota Only unprovability finding:** a live fetch of the Alibaba Free
Quota Only documentation page on 2026-09-16 confirms this is a per-account,
per-model, authenticated console toggle, disabled by default, found on the
Model Usage page or a model's Model Gallery detail page. No tool available
in this worker session can authenticate into that console or otherwise read
this specific account's current toggle state or live remaining balance for
`qwen3.7-flash`. `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts`
lines 146-156 (`getAlibabaFreeQuotaStatus`) contain no such check. Because
the work order and baseline both require this state to be proven before any
call, and require stopping at zero calls when it cannot be, this worker
returns `BLOCKED_WITH_REASON` rather than attempting the call and risking
paid exposure.

**Terminal decision:** `BLOCKED_WITH_REASON`. Zero calls attempted, zero
retries. Runner retargeted per the manifest; new receipt written as a
zero-call blocked artifact; historical receipt confirmed byte-identical
before and after.

## Risk / Corrective Action

| Risk | Evidence | Corrective action | Disposition |
|---|---|---|---|
| attempting a live call without provable Free Quota Only state, risking real paid exposure | live fetch of Alibaba Free Quota Only doc confirms disabled-by-default authenticated toggle; `getAlibabaFreeQuotaStatus()` source has no live/account check | stopped at zero calls and returned `BLOCKED_WITH_REASON` per the work order's fail-closed contract | RESOLVED_BY_ZERO_CALL_STOP |
| mistaking the stale ledger snapshot for a live balance | ledger file's own `useBeforeLiveTestRule` and `captureDate` fields | treated ledger as expiration-only evidence, not quota-remaining or toggle evidence, in the receipt's `prerequisiteEvidence` block | RESOLVED |
| widening the runner edit beyond model/path retarget | governing work order Write Ownership and Scope sections | diff limited to `MODEL_ID`, `RESULT_PATH`, and header/usage comments; prompt, rubric, parser, call/retry logic, key loader, and evidence shape unchanged | RESOLVED |
| historical receipt mutation | Forbidden Path Manifest | hashed historical receipt before and after; both hashes identical (`c552605...6159`); no write attempted to that path | RESOLVED |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1

reviewRoundCount: 0

priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH

dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH

newIndependentCriticalEvidence: NONE

regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED

externalAgentInvocationCount: 0

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 1

usageAvailability: NOT_EXERCISED_ZERO_CALL_STOP

quotaAdmissionDisposition: NOT_PROVABLE_ACCOUNT_STATE

nextDispatchDisposition: NO_FURTHER_DISPATCH_PENDING_REVIEW

rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH

reworkGeneration: 0

consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

productionBindingEvidence: NOT_APPLICABLE_WITH_REASON: no production code path, adapter, or runtime binding created; runner retarget only

adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS

Adversarial-regression note: this return explicitly rejects treating the
stale ledger snapshot or the date-only `getAlibabaFreeQuotaStatus()` check as
proof of live Free Quota Only state, and explicitly rejects proceeding to a
call on unproven account state even though a key alias and the historical
"prior successful call" pattern were both present.

internalAgentInvocationCount: 1

providerCallCount: 0

tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: zero provider calls were made in this tranche; no quota was consumed

terminalReadinessVerdict: READY_FOR_REVIEW

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "acel-g2-t2-fresh-direct-calibration-t1-problem",
  "chainMode": "SUCCESSOR",
  "chainOrdinal": 1,
  "predecessor": {
    "path": "docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_2026-09-16.md",
    "sha256": "d6f81cb9b2eea942674b6211b539cca109ba3954d2f849e7c0b585db97907ea2"
  },
  "blockerDelta": {
    "prior": ["NO_ACCEPTED_FRESH_DIRECT_CALIBRATION", "NO_CALLABLE_T1_TO_MAO_CONSUMER"],
    "resolved": [],
    "retained": ["NO_ACCEPTED_FRESH_DIRECT_CALIBRATION", "NO_CALLABLE_T1_TO_MAO_CONSUMER"],
    "new": [],
    "reopened": [],
    "current": ["NO_ACCEPTED_FRESH_DIRECT_CALIBRATION", "NO_CALLABLE_T1_TO_MAO_CONSUMER"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 1
  },
  "claims": [
    {
      "claimId": "ACEL-G2-T2-CAL-T1-WORKER-RETURN",
      "claimClass": "DOCUMENTATION_ONLY",
      "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
      "evidenceRef": "docs/reviews/evidence/acel-g2-t2-fresh-direct-calibration-t1-2026-09-16.json"
    }
  ],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "NO_SUCCESSOR"
}
```

Both blockers are declared `retained`/`current`, not `resolved`: this return
made zero provider calls, so no fresh calibration evidence was produced that
could resolve `NO_ACCEPTED_FRESH_DIRECT_CALIBRATION`, and the callable-seam
gap was entirely out of this tranche's scope. `requiredDisposition` is
`CONTINUE_BOUNDED` because this return adds no new blocker and returns a
bounded, source-backed `BLOCKED_WITH_REASON` outcome for reviewer
disposition.

## Command Evidence

```
git rev-parse HEAD
```
Exit code 0. Result: `eca0182c4811a371f6db49a7b8b71d136180f056`, matching the
work order's `executionBaseHead` capture instruction - PASS.

```
git status --short --untracked-files=all
```
Exit code 0. Result before authoring: empty output, clean worktree - PASS.

```
sha256sum docs/reviews/evidence/mao-oa-t6a-direct-candidate-calibration-2026-07-17.json
```
Exit code 0. Result before and after all edits:
`c5526054595a41ea990b5e125ea698d51fe3f0bb5768d80f4fdb7c1b005f6159` (identical) - PASS.

```
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base eca0182c4811a371f6db49a7b8b71d136180f056 --head HEAD
```
Exit code 0. Result: `COMPLIANT: pre-implementation autorun gate passed in
10.39s.` - PASS.

```
npx vitest run --config vitest.config.ts tests/mao.harder.value.candidate.contract.test.ts
```
(run from `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`) Exit code 0. Result:
`Test Files 1 passed (1)`, `Tests 22 passed (22)` - PASS.

```
WebFetch https://www.alibabacloud.com/help/en/model-studio/model-pricing
```
Result: current `qwen3.7-flash` International/Singapore tiered pricing and a
1M-token/90-day free-quota program description retrieved -
PASS_PUBLIC_DOC_ONLY.

```
WebFetch https://www.alibabacloud.com/help/en/model-studio/new-free-quota
```
Result: Free Quota Only confirmed as a disabled-by-default, per-account,
per-model authenticated console toggle with no code-reachable state -
PASS_PUBLIC_DOC_ONLY_CONFIRMS_UNPROVABLE_ACCOUNT_STATE.

```
Direct read inspection of EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts lines 146-156
```
Result: `getAlibabaFreeQuotaStatus()` compares only the static ledger's
`expirationDate` to `now`; no live account or toggle query exists in this
function or file - PASS_CONFIRMS_UNPROVABLE_LIVE_STATE.

```
git diff --check
```
Exit code 0. Result: no whitespace-conflict errors reported - PASS.

```
python governance/compat/run_worker_return_fast_gate.py
```
Exit code 0 (see Self-Reported Gate Evidence Consistency below).

```
git status --short --untracked-files=all
```
(final, after all edits) Result: exactly three changed paths - one modified,
two untracked additions, listed in Changed Files and `git status --short`
below - PASS.

## Self-Reported Gate Evidence Consistency

`python governance/compat/run_agent_autorun_workflow_gate.py --phase
pre-implementation` was run once, before the runner edit, from
`executionBaseHead`, and exited zero with `COMPLIANT`.

`python governance/compat/run_worker_return_fast_gate.py` is required to
exit zero before this return is finalized. Any in-scope defect discovered in
the three worker-owned paths during that run was repaired directly in this
invocation, per the work order's Worker Autonomy / No-Question Rule; no gate
failure was bypassed, skipped, suppressed, or relabeled, and no repair
touched any path outside this worker's three-path manifest.

`git status --short --untracked-files=all` at return time shows exactly the
three worker-owned paths changed. This is reported as-is rather than claimed
as a clean worktree, because all three required outputs exist and are
pending by design; staging remains empty throughout.

## Changed Files

Modified (unstaged):

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts`

Created (untracked, unstaged):

- `docs/reviews/evidence/acel-g2-t2-fresh-direct-calibration-t1-2026-09-16.json`
- `docs/reviews/CVF_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_WORKER_RETURN_2026-09-16.md` (this file)

This is exactly the three-path Required Artifact Manifest from the governing
work order. No other repository path was created, modified, deleted,
renamed, staged, or committed.

## git status --short

```
 M EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts
?? docs/reviews/CVF_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_WORKER_RETURN_2026-09-16.md
?? docs/reviews/evidence/acel-g2-t2-fresh-direct-calibration-t1-2026-09-16.json
```

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. No `git add`, `git commit`, `git push`, or
branch operation was executed at any point in this invocation. HEAD remains
`eca0182c4811a371f6db49a7b8b71d136180f056`, staging remains empty, and all
three artifacts remain uncommitted for reviewer disposition.

## Terminal Decision

`BLOCKED_WITH_REASON`

Reason: `account_free_quota_only_state_not_provable`. The runner was
correctly retargeted to `qwen3.7-flash` and the new receipt path, all
locally provable prerequisites passed, and public pricing/free-quota-program
documentation was refreshed live. But the account's actual Free Quota Only
toggle state for `qwen3.7-flash` -- an authenticated, per-account,
per-model console setting, disabled by default -- cannot be read by any tool
or code path available to this worker session. Proceeding to a call without
that proof would risk real paid exposure, which both the work order and
baseline explicitly forbid. Zero calls were attempted.

## Zero Provider Calls

`providerCallCount: 0`; `agentOrSubagentInvocations: 0`; `credentialValueAccess:
0`; `liveNetworkCallsToProvider: 0`; `retryCount: 0` for this entire tranche.
The two `WebFetch` calls in this return were to public, unauthenticated
Alibaba documentation pages only, not the DashScope provider API, and carried
no credential.

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE

outsideAuthorityBlockers: NONE

nextRepairRoute: NOT_APPLICABLE_CLOSEABLE

workerRedispatchAllowed: NO

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | `Self-declared worker-return artifact: yes`, `Responds to work order:`, `dispatchWorkOrder:`, the full worker-return heading set, exact-match convergence-control literal fields, `WORKER_MUST_NOT_COMMIT honored` without backticks, ASCII-only body text, SCEC required top fields with `prior` a subset of `resolved` union `retained`, corpus verdict bullet-line shape |
| gateRunPurpose | confirmation of this return's shape against known checker constants after authoring, not discovery |
| claimBoundary | checker success cannot accept a blocked outcome as a successful calibration, prove live account state, or authorize a retry |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | INTERNAL_AGENT live-calibration worker |
| Provider or surface | local private CVF workspace, Claude Code CLI; two public-documentation WebFetch reads only |
| Session or invocation | ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1, 2026-09-16 |
| Working directory | repository root at `eca0182c4811a371f6db49a7b8b71d136180f056` |
| Command or tool surface | governed file reads, `git rev-parse`, `git status`, `sha256sum`, `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation`, `npx vitest run`, `WebFetch` (public docs only), `python governance/compat/run_worker_return_fast_gate.py`, file edit/creation |
| Target paths | the exact three paths in Changed Files above |
| Allowed scope source | governing work order Required Artifact Manifest |
| Before status evidence | HEAD `eca0182c4811a371f6db49a7b8b71d136180f056`; `git status --short --untracked-files=all` empty; staging empty; new receipt path absent; historical receipt hash `c552605...6159` |
| After status evidence | HEAD unchanged; staging still empty; exactly the three target paths changed; historical receipt hash unchanged |
| Diff evidence | `git status --short --untracked-files=all` before and after; `git diff --name-status` shows exactly the three worker-owned paths; `git diff --check` clean |
| Approval boundary | one INTERNAL_AGENT worker invocation under this work order's `SINGLE_AGENT_MULTI_ROLE` route; provider call authority was granted (max 1 call) but not exercised; no commit, staging, agent/subagent invocation, credential-value access, public sync, or deploy |
| Claim boundary | no worker self-acceptance of any outcome, no historical-result mutation, no callable-seam resolution, no source/test/runtime/checker/session-state mutation outside the three-path manifest |
| Agent type | INTERNAL_AGENT worker |
| Invocation ID | `acel-g2-t2-fresh-direct-calibration-t1-worker-2026-09-16` |
| Expected manifest | the exact three paths in the work order's Required Artifact Manifest |
| Actual changed set | the exact three paths in Changed Files above |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this invocation |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | bounded runner retarget and zero-call blocked receipt only |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or live behavior is claimed |
| receiptEvidence | CVF_RECEIPT_PRESENT: the new receipt at `docs/reviews/evidence/acel-g2-t2-fresh-direct-calibration-t1-2026-09-16.json` records a blocked, zero-call outcome, not a live-call result |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no provider call, agent, or subagent action is executed |
| invocationBoundary | local file reads/edits, governance gates, focused offline tests, and two public-documentation fetches only |
| interceptionBoundary | no agent/provider/IDE/shell/git/filesystem interception claim |
| claimLanguage | blocked-with-reason outcome only, never a successful calibration or accepted score |
| forbiddenExpansion | provider call, credential-value access, retry, historical-receipt mutation, production, public, and deployment - none exercised |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | public vendor documentation -> Local worker prerequisite check -> blocked packet -> this worker return -> Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and three private evidence outputs |
| Disposition | public documentation is treated as input evidence only, not private CVF proof; no external agent is invoked in this tranche |
| Claim boundary | public documentation cannot substitute for authenticated account-state proof; this return does not claim it does |

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
  "parentArtifact": "docs/baselines/CVF_GC018_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_2026-09-16.md"
}
```

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: this is the first and only worker attempt on this dispatch; there is
no prior worker-return pass of this same parent to compare a delta ledger,
routing matrix, or adversarial sample against. No redispatch is permitted
per the work order's one-call, zero-retry contract.

## Corpus Completeness And Report Integrity

- Corpus task class: LIVE_PROOF
- Corpus root: exact bounded three-path Required Artifact Manifest in the paired GC-018 baseline, plus named read-only sources
- Snapshot time: 2026-09-16, worker executionBaseHead
- Enumeration command: filesystem-backed direct reads of the named paths; two public-documentation live fetches
- Manifest artifact or inline manifest: `docs/reviews/evidence/acel-g2-t2-fresh-direct-calibration-t1-2026-09-16.json`
- Manifest hash: worker records the historical receipt's SHA-256 directly in the new receipt's `prerequisiteEvidence.historicalReceiptHashBefore` field
- Processing ledger artifact or inline ledger: `prerequisiteEvidence` object in the same receipt
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE. The receipt separately uses prerequisite-proof statuses PROVEN, PROVEN_PUBLIC_DOC_ONLY, PROVEN_STALE_SNAPSHOT_ONLY and NOT_PROVABLE; these must not be conflated with corpus read status.
- Reconciliation: manifest=7; ledger_terminal=7; exclusions=0; unresolved=0. The seven prerequisite records are four locally proven, one public-documentation-only, one stale-snapshot-only, and one (`accountFreeQuotaOnlyToggle`, including live balance) explicitly `NOT_PROVABLE`. The zero-call receipt uses null timestamps because no live run occurred; the worker's original `00:00` placeholders were not observed event times and Local removed them during review.
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: PASS; all six prerequisite records reconcile to the receipt's `prerequisiteEvidence` object
- Drift check: PASS; `sha256sum docs/reviews/evidence/mao-oa-t6a-direct-candidate-calibration-2026-07-17.json` recomputed before and after edits, result MATCH (both `c5526054595a41ea990b5e125ea698d51fe3f0bb5768d80f4fdb7c1b005f6159`)
- Output traceability: prerequisite evidence -> unprovable Free Quota Only finding -> zero-call stop -> this worker return
- Adversarial verification: "prior successful call implies current authorization" and "stale ledger snapshot implies live balance" were both explicitly challenged and rejected
- Corpus verdict: COMPLETE_VERIFIED

## Knowledge System Reconciliation

- Knowledge task class: LIVE_PROOF
- Source manifest: `docs/reviews/evidence/acel-g2-t2-fresh-direct-calibration-t1-2026-09-16.json`
- Source manifest hash: historical receipt hash recorded in the same manifest's `prerequisiteEvidence` object
- Enumeration safety: filesystem-backed exact-path reads plus two public-documentation fetches, reconciled to the named source list above
- Intake registry or ledger: receipt `prerequisiteEvidence` object with six terminal status records
- Authority assets: governing work order, paired GC-018 baseline, T0 qualification audit, runner source, quota-ledger source, quota-ledger JSON, historical receipt, two public vendor docs
- Derived views: prerequisite evidence, unprovable-toggle finding, blocked receipt, this worker return
- Semantic region ledger: runner retarget, prerequisite proof scope, Free Quota Only mechanism, historical receipt integrity
- Region reconciliation: assets=9; mapped=9; deferred=0; unmapped=0
- Orphan or unmapped assets: none
- Cross-region links: each finding in this return cites one or more named sources above
- Drift check: PASS
- Rebuildability check: PASS; the receipt contains exact evidence status, scope limits, and code line citations for the unprovable finding
- Retrieval boundary: prerequisite-check and blocked-outcome evidence only; no live score or callable-seam evidence
- Adversarial verification: the stale ledger and the date-only status function were both explicitly rejected as live-account proof
- Knowledge-map verdict: RECONCILED_WITH_DECLARED_GAPS
- Claim boundary: this result is a zero-call blocked outcome, not execution-readiness or production evidence

## Finding-To-Governance Learning Disposition

No new governance rule is created from this tranche. The gap this worker
surfaced -- that no code path in
`EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` can
verify live account Free Quota Only state or live remaining balance -- is
recorded as a finding for Local's disposition, not repaired here, because
the work order's Forbidden Path Manifest and Write Ownership sections do not
authorize gateway or ledger source changes in this tranche.

## Epistemic Process Block

### Expected Result / Prediction

A fresh direct calibration call to `qwen3.7-flash` could produce one
independently reviewable, successfully-parsed evidence point, provided all
prerequisites -- including live account Free Quota Only state -- could be
proven immediately before the call.

### Evidence Comparison

The runner retarget, key-alias presence, receipt-path availability, and
historical-receipt-hash preservation were all directly proven. Public
pricing and Free Quota Only mechanism documentation were refreshed live.
However, the prediction's live-account-state precondition could not be
confirmed: the account's actual Free Quota Only toggle for `qwen3.7-flash`
is an authenticated console setting with no code-reachable state, and the
static ledger snapshot explicitly disclaims itself as non-live evidence. The
call was therefore never attempted.

### Contradiction Or Gap Disposition

No source contradiction was found. A structural gap was confirmed: the
codebase has no mechanism to verify live Alibaba account quota-toggle state,
so this class of prerequisite can only ever be proven by direct operator
console inspection or a future credentialed status-check tool, neither of
which exists in this tranche's authorized scope. This gap is reported, not
repaired. The callable-seam blocker
(`NO_CALLABLE_T1_TO_MAO_CONSUMER`) remains untouched and out of scope.

### Claim Update

This return does not establish a fresh calibration data point, does not
consume any quota, and does not resolve the account-state verification gap.
It returns a bounded, evidence-backed `BLOCKED_WITH_REASON` outcome for
Local disposition, which may re-authorize a future attempt only after
account-state proof becomes available by some means outside this worker's
tool access.

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: this is pending worker evidence, not accepted
closure material. A later reviewer owns any completion review or closure
projection named by the governing work order's Reviewer Closure Conversion
block; that completion review does not yet exist and is not cited here as a
present authority artifact.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
frictionLevel: MEDIUM
frictionType: HELPER_GAP
observedStep: the work order requires immediate-pre-call proof of an
authenticated, per-account provider console toggle (Free Quota Only) that no
tool available to this worker session can read; distinguishing "public
documentation confirms the mechanism exists and is disabled by default" from
"this account's current state is proven" was the key judgment that produced
the zero-call stop
preventiveControlCandidate: HELPER_DIAGNOSTIC

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private G2-T2 calibration worker return; no public-sync authority is
claimed or exercised.

## N/A With Reason Instruction

Every packet-shape section in this return that could be conditionally
inapplicable is marked `N/A_WITH_REASON` or `NOT_APPLICABLE_WITH_REASON`
with an explicit reason rather than omitted: see Rescan Intelligence
Hardening and Machine Closure Package above.

## Claim Boundary

This worker return records command evidence with actual exit codes,
executionBaseHead invariance, a literal machine-parseable three-path changed
set, and a no-commit statement for the
ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1 tranche only. It does not accept its
own blocked disposition as final, does not attempt or claim any provider
call, does not mutate the historical receipt, does not resolve the
callable-seam blocker, does not mutate any source/test/runtime/checker/
session-state path outside the three-path manifest, does not access any raw
credential value, does not publish, push, deploy, or claim runtime or
production readiness. Overall worker status: `COMPLETE_PENDING_REVIEW`.
