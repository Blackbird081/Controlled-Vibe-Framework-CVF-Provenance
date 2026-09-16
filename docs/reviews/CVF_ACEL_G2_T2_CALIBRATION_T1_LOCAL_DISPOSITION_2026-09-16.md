# CVF ACEL G2 T2 Calibration T1 Local Disposition

Memory class: governed-review

docType: review

Status: REVIEWER_ACCEPTED_BOUNDED_EVIDENCE_WITH_PROCESS_DEVIATION

Date: 2026-09-16

Batch ID: ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1

executionBaseHead: `eca0182c4811a371f6db49a7b8b71d136180f056`

## Purpose

Separate the original zero-call, fail-closed worker return from the later
operator-directed live call. Accept one direct calibration data point after
independent rescoring without treating it as a compliant completion of the
original zero-paid-exposure packet or as G2-T2 actual-agent proof.

## Target / Source

- Governed dispatch: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_2026-09-16.md` and its paired GC-018 baseline.
- Zero-call worker return: `docs/reviews/CVF_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_WORKER_RETURN_2026-09-16.md`.
- Zero-call receipt: `docs/reviews/evidence/acel-g2-t2-fresh-direct-calibration-t1-2026-09-16.json`.
- Operator-resumed live receipt: `docs/reviews/evidence/acel-g2-t2-fresh-direct-calibration-t1-live-2026-09-16.json`; SHA-256 `0221a9d5dbbe15479064a21e9d98303d31617d678a8777d0f8fccad91632aeea`.
- Existing T6A runner and deterministic scorer: `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts`.
- Historical rejected receipt: `docs/reviews/evidence/mao-oa-t6a-direct-candidate-calibration-2026-07-17.json`; SHA-256 remains `c5526054595a41ea990b5e125ea698d51fe3f0bb5768d80f4fdb7c1b005f6159`.

## Scope / Methodology

Role: Local reviewer/orchestrator. External Web research is closed; the
shared-workspace worker was INTERNAL_AGENT. Local owns final technical
disposition. Review consumed the returned evidence, inspected the exact
runner/grant seam, and recomputed the rubric from the sanitized candidate.
The focused 22-test suite and TypeScript check passed. No second provider
call or broad duplicate live run was made.

## Findings / Position

| Question | Local finding |
|---|---|
| Original packet | Worker correctly stopped `BLOCKED_WITH_REASON` at zero calls because Free Quota Only and live account quota were not proven. This is accepted as a truthful stop, not a calibration result. |
| Operator override | The operator later explicitly ordered one live call using the Alibaba keys and the recorded free-quota model, despite the disclosed inability to guarantee zero paid cost. This changed the cost-admission boundary but was not incorporated into a new pre-call governed work order. Record the process deviation; do not relabel the original packet compliant. |
| Harness compatibility | The T6A runner lacked the now-required `ProviderExecutionGrant`. Local added an exact one-call Alibaba grant and directed output to a distinct receipt. No credential value was printed or persisted. |
| Live observation | Exactly one runner invocation reached the provider path: `qwen3.7-flash`, `dashscope-intl.aliyuncs.com`, 188 input and 2,755 output tokens, `callCount=1`, `retryCount=0`, successful parsed candidate. The actual billed amount is not observed. |
| Independent score | `evaluateHarderCandidate(JSON.stringify(sanitizedCandidate))` matched every stored rubric/defect/release field: score 100/100, zero defects, `materialDefectFound=false`, `releaseCandidate=false`. |
| Re-run safety | Local added a pre-secret/pre-provider receipt-exists guard after the call so this runner cannot overwrite the live receipt or re-present `consumedCalls=0` on a later invocation. |
| Downstream authority | T6B is not released because its score/defect trigger is false. This direct candidate measurement does not prove a T1-to-MAO callable seam or real-agent benefit from topology adaptation. |

## Risk / Corrective Action

The 2026-09-10 quota ledger is dated selection evidence, not live billing
evidence. The call proceeded under a later direct operator instruction, with
paid exposure disclosed beforehand; do not assert cost US$0 without an
account bill. A future live packet must bind the current harness grant before
dispatch, include an output-collision guard before the first call, and state
its billing ceiling explicitly. The original zero-call receipt's false
`00:00` event placeholders and seven-versus-six prerequisite count were
repaired by Local in their own evidence paths.

## Decision / Recommendation / Disposition

Accept only the new direct-calibration observation as
`REVIEWER_ACCEPTED_BOUNDED_EVIDENCE_WITH_PROCESS_DEVIATION`. Do not promote
the historical T6A 100/100 result, claim T6B release, or start another live
call. The next G2 decision is whether to design a genuinely discriminating
real-agent task/quality rubric and separately authorize a comparative T2
trial; the present candidate's 100/100 cannot distinguish policies.

## Evidence / Verification

- Live receipt SHA-256: `0221a9d5dbbe15479064a21e9d98303d31617d678a8777d0f8fccad91632aeea`.
- Historical receipt SHA-256 before/after: `c5526054595a41ea990b5e125ea698d51fe3f0bb5768d80f4fdb7c1b005f6159`.
- Original zero-call receipt SHA-256 before/after live call: `58b25c1602592f0529106781e3fcf5e791d0a7c8763945e4b139a06e5f09fbd6`.
- TypeScript `npx tsc --noEmit -p tsconfig.json`: PASS. Focused scorer tests: 22/22 PASS.
- Independent sanitized-candidate rescore: exact rubric/defect/release match.
- Reviewer-fast gate: 68/68 PASS after evidence correction.
- Provider call count for this Local live resume: 1; retry count: 0. No post-call provider test or release gate was run.

## Reviewer Non-Duplication

`EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`: only the named
contradictions (missing grant, receipt collision, independent rescore and
incorrect zero-call metadata) prompted focused checks. No broad duplicate
implementation or provider rerun was performed.

## External/Local Coordination Binding

External advice remains input, not private-CVF proof. The INTERNAL_AGENT
worker produced the zero-call return; Local reviewed and later executed the
operator-resumed single live call. Local alone owns this bounded decision.

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

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer/orchestrator |
| Provider or surface | private CVF workspace; one Alibaba/DashScope live call |
| Session or invocation | ACEL-G2-T2 calibration operator resume, 2026-09-16 |
| Working directory | repository root at `eca0182c4811a371f6db49a7b8b71d136180f056` |
| Command or tool surface | source inspection, `apply_patch`, focused offline tests, one `npx tsx` runner invocation, independent scorer, reviewer-fast gate |
| Target paths | runner, zero-call worker return/receipt, distinct live receipt, this Local review |
| Allowed scope source | original T1 work order for the zero-call return; subsequent explicit operator live-call instruction for the distinct resume |
| Before status evidence | original worker's exact three uncommitted paths; zero-call and historical receipt hashes recorded |
| After status evidence | same paths plus distinct live receipt and Local review; one observed live runner invocation, no retry |
| Diff evidence | `git status --short`; runner diff; SHA-256 checks of both earlier receipts |
| Approval boundary | operator explicitly authorized API key use, selected model by Local, then instructed the call despite disclosed cost uncertainty; no second call authorized |
| Claim boundary | bounded direct calibration evidence only; no zero-bill, T6B, comparative G2 or production claim |
| Agent type | LOCAL_REVIEWER_ORCHESTRATOR |
| Invocation ID | `acel-g2-t2-calibration-t1-local-resume-2026-09-16` |
| Expected manifest | original three worker paths plus one distinct live receipt and Local review under the operator resume |
| Actual changed set | exact five paths in `git status --short` at review time |
| Manifest delta | MATCH_WITH_DISCLOSED_OPERATOR_RESUME |

## Expected Result / Prediction

One direct `qwen3.7-flash` candidate would yield a parsed, independently
rescorable T6A response; a score at or below 80 or material defect would
release the harder T6B trigger.

## Evidence Comparison

The candidate parsed and independently rescored exactly as the receipt states,
but scored 100 with no defects. The T6B trigger did not fire. Actual billing
was not observed, so the free-quota snapshot does not prove zero charge.

## Contradiction Or Gap Disposition

The old runner lacked the mandatory grant binding, which Local repaired before
the call. The original cost gate remained unproven; later operator instruction
permitted the direct call but did not retroactively make that gate pass. The
candidate is too easy for a discriminating comparative trial as currently
formulated. The callable-seam gap remains open.

## Claim Update

CVF has one new accepted, bounded direct-calibration data point. It has no
accepted T6B release or actual-agent G2 comparative result.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_review_cost_control.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | `docType: review`; `Status: REVIEWER_ACCEPTED_BOUNDED_EVIDENCE_WITH_PROCESS_DEVIATION`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirmation of already inspected bounded evidence and review shape, not discovery of findings or a claim that the original cost gate passed |
| claimBoundary | checker success cannot prove account billing, comparative value, or retroactive dispatch compliance |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private credential-referenced calibration evidence; no public-sync
authority or public catalog claim.

## Claim Boundary

This review admits one parsed, independently rescored direct response and
preserves the original zero-call block and later process deviation. It does
not prove zero billing, a production consumer, policy improvement, G2-T2
actual-agent value, T6B release, public readiness or deployment.
