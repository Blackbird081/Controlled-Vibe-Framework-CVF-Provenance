# CVF GC-018 Baseline - ACEL G2 T2 Fresh Direct Calibration T1

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-09-16

Batch ID: ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1

dispatchBaseHead: `44464b449033d5e2d51ca9baa4a32d5e66198445`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Prepare one fresh direct-lane measurement of the qualified T6A harder task,
with a new immutable receipt and independent Local rescoring. This is a
calibration point, not a G2-T2 A/B experiment or evidence of MAO improvement.

## Authority Chain

Operator: explicit G2-T2 calibration approval (2026-09-16); Local conditional candidate
qualification at material `36784f6c6efa2fdca6b497a6d341ece7bcd3a2c8`;
this GC-018 and its paired work order. The historical T6A live result remains
`NOT_ACCEPTED`; it is never a baseline score for this tranche.

## Source / Predecessor Evidence

- `docs/audits/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.md`:
  qualification is only for packet authoring and parse failure must fail closed.
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts`:
  current runner hardcodes the old receipt path and `qwen3.7-plus`.
- `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json`:
  `qwen3.7-plus` free quota expired 2026-08-31; `qwen3.7-flash` snapshot is
  dated to 2026-10-22, but the captured balance is not a live balance.
- [Alibaba Model Studio pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing)
  lists `qwen3.7-flash` International/Singapore tier; pricing and quota must
  be checked again immediately before execution.
- [Alibaba free quota rules](https://www.alibabacloud.com/help/en/model-studio/new-free-quota)
  describe the Free Quota Only switch; its actual account state is not proven
  by this document.

## Decision / Baseline / Proposed Tranche

The candidate task and scorer remain fixed. Permit only a minimal source edit
to direct the existing one-call runner to a new T1 receipt and the currently
ledger-eligible `qwen3.7-flash` model. The worker must prove the model is
available at the current account/endpoint and Free Quota Only is enabled
without printing credentials. If any prerequisite is unverified, return
`BLOCKED_WITH_REASON` with zero calls. Maximum one attempted call, zero retries,
and expected paid cost US$0; do not proceed if a paid charge is possible.

## Scope / Target / Owner Boundary

Allowed worker paths are exactly the runner above, a new dated T1 receipt at
`docs/reviews/evidence/acel-g2-t2-fresh-direct-calibration-t1-2026-09-16.json`,
and a worker return at
`docs/reviews/CVF_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_WORKER_RETURN_2026-09-16.md`.
The historical T6A receipt is a forbidden write target. The worker must not
change task prompt, parser, rubric, defect classes, gateway harness, ledger,
credential files, callable seam, T1 routing, MAO lane, public repository,
deployment or production state.

## Acceptance / Fail-Closed Contract

Before the call: clean exact execution base; fresh model/pricing/quota evidence;
Free Quota Only confirmed on the actual account; approved key alias presence
only; new receipt absent; historical receipt hash recorded; runner diff limited
to model, target receipt and authority comments. If any check fails, no call.

After the call: exactly one attempted call and zero retries, even on timeout or
error. Store a secret-safe receipt with provider/model, usage, latency, call
count, raw-response hash, parsed sanitized candidate when parse succeeds,
rubric dimensions and defect classes. A reviewer independently recomputes
score/defects from the sanitized candidate. If parse fails, the current
receipt is non-reconstructable: `INVALID_JSON`, any score, any material defect
and the release boolean are `NOT_ACCEPTED`; no retry and no T6B release.
No result in this tranche alone proves a callable T1-to-MAO seam or G2-T2 value.

## Operator Checkpoint

The operator authorized this bounded calibration. Any model substitution,
paid exposure, second call, retry, credential expansion, runner evidence-shape
change, or additional file returns to the operator. The worker cannot infer
approval from a previously successful call.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | existing T6A runner and Local reviewer | one direct call, no commit, independent review | qualification audit and this baseline | local runner only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none in this tranche | no external ingress, credential or mutation | Local-only work order | deferred adapter owner; no CLI/MCP call | `DEFERRED_WITH_REASON` |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts` | Yes | bounded model and output retarget |
| `docs/reviews/evidence/acel-g2-t2-fresh-direct-calibration-t1-2026-09-16.json` | Yes | new secret-safe one-call or zero-call blocked receipt |
| `docs/reviews/CVF_ACEL_G2_T2_FRESH_DIRECT_CALIBRATION_T1_WORKER_RETURN_2026-09-16.md` | Yes | pending review evidence |

## Evidence Requirements / Verification

The worker returns the exact invocation, zero-or-one-call ledger, secret-safe
quota and model checks, receipt, unchanged historical SHA-256 and final worktree
status. Local recomputes any successfully parsed score and defect from the
persisted candidate. Pre-dispatch, pre-implementation, worker-return and
committed-range closure gates remain separate evidence.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033 and ADIF-0044; truncated 10/24.
Impact: source identity, exact ownership, role boundary, credential and receipt
admission remain explicit.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | dispatch status, provider grant, SCEC, exact path ownership, live-effect boundary |
| gateRunPurpose | confirm the packet against current gates, then repair all in-scope failures |
| claimBoundary | source read-ahead is not runtime or provider proof |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id ACEL-G2-T2-FRESH-DIRECT-CALIBRATION-T1 --title "G2 T2 Fresh Direct Candidate Calibration" --date 2026-09-16 --base 44464b449033d5e2d51ca9baa4a32d5e66198445 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "ACEL G2 T2 candidate qualification material 36784f6c6" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact source and receipt ownership, quota gate, fail-closed acceptance |
| checkerReadAheadConfirmation | dispatch, grant, routing, handoff and closeability sources read |
| docOnlyNewFields | fresh receipt; parse-failure non-admission |
| claimBoundary | no live result or public claim |

## Claim Boundary

This authorizes only bounded Local execution after work-order preflight. It
does not claim an accepted score, material defect, T6B release, MAO advantage,
G2-T2 experiment, runtime seam, production readiness, or public export.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private calibration authority and evidence; no public sync requested.
