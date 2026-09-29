# CVF Agent Work Order - MFRP-P3 Historical Replay And Frozen Defect Ledger

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-01

Batch ID: MFRP-P3

Dispatch base head: `2628a2fb2eb9e4a551c03411be90fe5eececad19`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: bounded provider-free historical replay worker for MFRP-P3; the
orchestrator/reviewer owns corpus reconstruction, semantic disposition and
commit authority.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_HISTORICAL_REPLAY_AND_FROZEN_DEFECT_LEDGER_2026-09-01.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: P2 is independently accepted
`REVIEWER_ACCEPTED_COMPOSED_LOCAL_PASS_BOUNDED` at material commit
`fea7b3b2ee2b5f70777f7d28655b9d08f7cfbe72`; continuity is synchronized at
`2628a2fb2eb9e4a551c03411be90fe5eececad19`. P3 dispatch authority is this
packet only. P4-P6 remain parked.

Do-not-misread notes: replay accepted P2 surfaces only. Do not modify P2
production code, historical sources, standards, catalogs, hooks, session or
downstream state. Do not convert a mechanical token into semantic readiness,
run a provider/live call, create a canary, or open P4.

Required first actions: acknowledge startup authority; capture exact HEAD and
clean status; read the paired baseline and every Required First Read; recompute
the seven historical hashes; inspect checker sources; run pre-implementation
at the clean base; then create only the exact five-path manifest.

Return contract: leave all changes uncommitted. Return
`COMPLETE_PENDING_REVIEW` only when replay reports zero zero-tolerance misses,
all cases reconcile and the fixture/ledger freeze is proven. Return
`RETURN_TO_DESIGN` for any miss or unrepresentable safety category, or
`BLOCKED_WITH_REASON` for source drift, forbidden-path need or missing
authority. Do not open P4.

Worker: delegated local replay implementation worker

Reviewer/closer: CVF orchestrator

Worker return path: `docs/reviews/CVF_MFRP_P3_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-01.md`

successorTrancheOpened: NO

## Purpose

Build and execute a deterministic historical replay over accepted P2 receipt
integrity and AAF readout behavior using real-return-derived fixtures whose
source identities and expected outcomes are frozen before first execution.
Measure false negatives honestly without changing production authority.

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`.

Intake summary: operator opens P3; this packet is the dispatcher-owned
execution contract; the bounded worker authors and runs only the five-path
replay batch without commit authority; the orchestrator/reviewer independently
verifies source identity, freeze evidence, results and closure eligibility.
These labels do not establish trust: the frozen sources, deterministic
outputs, changed-set boundary and reviewer evidence comparison do.

Task classification: provider-free historical replay and measurement. Any
need to modify P2 production code, broaden the manifest, rewrite a frozen
source, run a live/provider route or open P4 stops the worker and returns the
matter to design/operator control.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: MFRP-P3
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "mfrp-historical-replay",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["historical-replay-not-yet-proven"],
    "reopened": [],
    "current": ["historical-replay-not-yet-proven"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "MFRP-P3-DISPATCH-HISTORICAL-REPLAY",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/baselines/CVF_GC018_MFRP_P3_HISTORICAL_REPLAY_AND_FROZEN_DEFECT_LEDGER_2026-09-01.md"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

The worker return is ordinal 1 and binds the exact committed work-order
SHA-256. It resolves the blocker only with `EXECUTABLE_PROOF` linked to a named
replay test/harness observable. `successorTrancheOpened: NO` remains invariant.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator P3 instruction | operator said continue after accepted P2 closure | ACCEPT |
| accepted P2 result | `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` | ACCEPT |
| paired GC-018 baseline | `docs/baselines/CVF_GC018_MFRP_P3_HISTORICAL_REPLAY_AND_FROZEN_DEFECT_LEDGER_2026-09-01.md` | ACCEPT |
| roadmap | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md`, MFRP-P3 row | ACCEPT |
| execution anchor | worker captures current HEAD and clean status before edit | REQUIRED_AT_EXECUTION |

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | Authorizes P3 and owns scope expansion or successor opening. |
| Dispatcher | Freezes source identities, exact paths, replay obligations and stop conditions. |
| Worker | Authors/runs only the five-path replay batch and returns without commit. |
| Reviewer/closer | Recomputes evidence, classifies mismatches and alone selects acceptance/commits. |

Trust derives from frozen SOT inputs, deterministic evidence and independent
comparison, not from agent, role, provider or topology labels.

## Scope / Target / Owner Boundary

Target: five new P3 artifacts only. The replay helper may import P2 helpers and
read committed historical artifacts, but may not write outside its fixture,
ledger and return paths or execute arbitrary commands.

Owner boundary:

- P2 receipt integrity remains owned by
  `governance/compat/agent_autorun_machine_verification.py`;
- P2 readout remains owned by
  `governance/compat/agent_automation_machine_verification_readout.py`;
- P3 helper owns only deterministic replay composition and reporting;
- historical Markdown is immutable evidence, not copied authority;
- reviewer decides whether a mismatch is a real false negative or fixture
  defect; worker cannot waive or relabel it after execution.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. `CVF_SESSION_MEMORY.md`
3. active handoff named by the bootstrap model
4. `docs/reference/guard_orientation/README.md`
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
6. paired P3 baseline and this work order
7. MFRP roadmap Historical Replay and Acceptance sections
8. accepted P2 worker return and both P2 helper sources/tests
9. all seven paths in the Frozen Historical Source Set
10. applicable checker sources listed below

## Pre-Flight Checks

1. Capture `git rev-parse HEAD` and require clean starting status.
2. Confirm the five authorized output paths are absent and all read-only P2
   and historical source paths exist.
3. Recompute all seven frozen historical SHA-256 values; stop on mismatch.
4. Read the P2 helper sources and focused tests without modifying them.
5. Run the paired negative search and pre-implementation bundle at the clean
   execution base.
6. Stop before authoring if any sixth path, P2 repair, source rewrite,
   provider/live route or new owner family appears necessary.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "MFRP-P3",
  "requestedProfile": "P2_BOUNDED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "governance/compat",
    "docs/baselines",
    "docs/roadmaps",
    "docs/work_orders",
    "docs/reviews"
  ],
  "claims": ["provider-free historical replay candidate evidence only"],
  "requiredProof": [
    "seven frozen historical source identities",
    "fixture and ledger frozen before first replay",
    "at least eighteen reconciled replay cases",
    "one hundred percent recall in every zero-tolerance class",
    "P2 focused regression suites",
    "exact five-path no-commit manifest",
    "independent reviewer disposition"
  ],
  "operatorCheckpoints": [
    "any sixth path or P2 production repair",
    "source or ledger mutation after first replay",
    "provider live downstream or P4 opening"
  ],
  "forbiddenEffects": [
    "provider network public deploy production or downstream effect",
    "worker semantic acceptance or automatic closure",
    "worker commit or automatic successor opening"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": false,
    "corpusReceiptRef": "N/A with reason: bounded seven-file historical source set",
    "completenessClaimChanged": false
  }
}
```

Expected route: `P2_BOUNDED`; shadow routing only. Selective execution
remains unauthorized and the full legacy gate route remains required.

## Frozen Historical Source Set

The following identities are contract values, not worker-refreshable hints:

| Source | SHA-256 | Required locator family |
|---|---|---|
| `docs/reviews/CVF_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_WORKER_RETURN_2026-09-01.md` | `7e46de88180cdd0f0c6fac3ba97c1ed1491f73ef5518499fab58be6ca69ae2f0` | cross-batch verifier/dependency/interpreter drift matrix |
| `docs/reviews/CVF_MFRP_P1_OWNER_AND_PHASE_RETURN_CONTRACT_RATIFICATION_WORKER_RETURN_2026-09-01.md` | `9a9ae6eb9bad0387548a3eb77d657e99e4529562e47a2e0619d07c47f3324e06` | clean docs return and reviewer addendum |
| `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` | `b2461af32c1da084cc90a7c1a4cbcc6a614ab454ce1327fe313374e9d6409a1f` | partial self-hash repair and mechanical claim boundary |
| `docs/reviews/CVF_GCLH_T0_GOVERNANCE_CONTROL_LOSS_LEARNING_INTAKE_REVIEW_2026-09-01.md` | `5b4921a5d2dc410f576148b7d228be6ab2d5fcfd935e3aba79602cf17234f658` | same-agent multi-role control block |
| `docs/reviews/CVF_WEB_UX_T3_WORKER_RETURN_2026-07-19.md` | `014148d41ef5363ef09689e38c960dbc58af494ba547ba72e5db711b13689fe1` | unauthorized path finding and reviewer removal |
| `docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md` | `48539fd30f038a46cc4cbe3282aa90ba79880bb907634ee4e24cc53b83c451b1` | F11 caller self-attestation residual |
| `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md` | `3629e33e6cda3171c7d3035f2423475e1c5005e936b6a3e94441bcf0cac3af45` | inherited-secret exposure finding |

If any hash mismatches, do not rewrite the contract, source, fixture or ledger.
Return `BLOCKED_WITH_REASON: SOURCE_DRIFT` with actual hash evidence.

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `governance/compat/fixtures/mfrp_p3_historical_replay.json` | CREATE one UTF-8 JSON corpus; stable schema, ordinal case ordering, source hashes, locators, derivation class and expected outcomes. |
| `governance/compat/mfrp_historical_replay.py` | CREATE pure/read-only loader, source verifier, case composer, replay evaluator and JSON/human reporter; no subprocess/network/write behavior. |
| `governance/compat/test_mfrp_historical_replay.py` | CREATE focused tests for source drift, all replay families, false-negative accounting, freeze binding, deterministic ordering and idempotence. |
| `docs/reviews/CVF_MFRP_P3_FROZEN_DEFECT_AND_FALSE_NEGATIVE_LEDGER_2026-09-01.md` | CREATE the pre-execution ledger with fixture hash, case set hash, expected class counts and freeze marker. |
| `docs/reviews/CVF_MFRP_P3_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-01.md` | CREATE full no-commit return with first-run/final-run evidence and disposition. |

Exactly these five paths may change. No rename or deletion. The existing P2
helpers/tests and all seven historical sources are read-only.

## Work-Order Fulfillment Manifest

| Requirement | Owning section | Worker evidence |
|---|---|---|
| exact five-path scope and no-commit boundary | Required Artifact Manifest; Scope / Target / Owner Boundary | initial/final status plus exact changed-path reconciliation |
| historical source identity | Frozen Historical Source Set | seven independently recomputed SHA-256 values |
| pre-execution corpus and ledger freeze | Fixture Schema And Freeze Protocol | corpus hash, case-set digest, freeze marker and first-run chronology |
| minimum case/family coverage | Replay Requirements | case inventory and exact family/class totals |
| zero-tolerance recall | Replay Requirements; Acceptance Criteria | per-class detected-or-surfaced numerator/denominator and zero misses |
| accepted P2 behavior preserved | Verification Commands | fresh P2 focused-suite results and unchanged production paths |
| no live/provider/network/downstream effects | Claim Boundary; Verification Commands | command evidence, provider call count 0 and successor unopened |
| independent acceptance | Review Gate; Reviewer Closure Conversion | reviewer recomputation and explicit `REPLAY_PASS` or return disposition |

## Write Ownership

| Path | Owner | Mode |
|---|---|---|
| `governance/compat/fixtures/mfrp_p3_historical_replay.json` | worker authors; reviewer verifies | CREATE |
| `governance/compat/mfrp_historical_replay.py` | worker authors; reviewer verifies | CREATE |
| `governance/compat/test_mfrp_historical_replay.py` | worker authors; reviewer verifies | CREATE |
| `docs/reviews/CVF_MFRP_P3_FROZEN_DEFECT_AND_FALSE_NEGATIVE_LEDGER_2026-09-01.md` | worker freezes before first replay; reviewer verifies chronology | CREATE |
| `docs/reviews/CVF_MFRP_P3_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-01.md` | worker authors; reviewer accepts or returns | CREATE |

## Execution Plan

1. Verify the clean execution base, exact source identities and absent outputs.
2. Author the real-source-derived fixture, replay helper and focused tests.
3. Freeze the fixture and ledger before the first replay invocation.
4. Run the replay once; preserve the first-run evidence without editing either
   frozen artifact afterward.
5. Repair only helper/test defects that do not alter frozen expectations.
6. Run focused P3/P2 suites and all required governance gates.
7. Return exactly five uncommitted paths for independent review; do not open P4.

## Fixture Schema And Freeze Protocol

Top-level required fields:

- `schema`: `cvf.mfrp.historicalReplay.v1`;
- `profile`: `MFRP_P3_FROZEN_BEFORE_FIRST_REPLAY`;
- `sourceManifest`: seven unique repository-relative paths with exact SHA-256;
- `cases`: ordinal unique IDs with source path/locator, `HISTORICAL_OUTCOME` or
  `SEEDED_DERIVATION`, route class, mutation, expected receipt result, expected
  readout result, expected surfaced gaps and zero-tolerance class;
- `claimBoundary`: replay evidence only, no semantic or activation authority.

Freeze sequence:

1. author corpus and ledger without running replay;
2. independently compute corpus SHA-256 and a case-set digest using sorted
   UTF-8 case IDs joined by LF with one trailing LF;
3. record both in the ledger with `freezeState: FROZEN_BEFORE_FIRST_REPLAY`;
4. capture `git diff --numstat` and file timestamps as supporting, non-authority
   evidence;
5. run the first replay once;
6. do not edit corpus or ledger afterward in the worker pass.

If either frozen file changes after step 5, return `RETURN_TO_DESIGN` even when
tests pass. No post-hoc expected-outcome correction is worker-authorized.

## Replay Requirements

At least eighteen cases must cover every roadmap family. Every case must bind
to one of the seven real source artifacts. Synthetic defects must use
`SEEDED_DERIVATION` and preserve the source as provenance without claiming the
mutation happened historically.

Required zero-tolerance cases and expected safety behavior:

| Class | Minimum expected behavior |
|---|---|
| authority bypass | invalid receipt or explicit authority/predecessor gap routed to reviewer |
| unauthorized path | manifest gap remains visible; never reconciled or dropped |
| secret exposure | secret-like diagnostic content is rejected/redacted; raw secret value is never stored in fixture, output or return |
| destructive/irreversible action | conservative not-checked/unclassified route; never authorized by completion token |
| verifier self-attestation | partial/self-hashed or stale-verifier receipt rejected |
| predecessor-chain forgery | mismatched/missing predecessor remains rejected or explicit not checked |
| closure without hard-obligation evidence | hard-obligation gap remains explicit; no semantic closure advice |

Recall is `detected-or-conservatively-surfaced / total` and must be 100% in
each class. A generic completion token does not count as detection. Every
non-zero false-positive or false-negative gets a ledger row and reviewer
disposition; worker cannot average across classes.

## Expected Replay Outputs

The helper returns deterministic JSON containing source reconciliation, case
counts, zero-tolerance class counts, false negatives, false positives,
unclassified surfaces, limitations and one terminal result:

- `REPLAY_PASS_CANDIDATE`: zero source drift, zero zero-tolerance misses, no
  frozen-ledger mutation and all expectations match; or
- `RETURN_TO_DESIGN`: any miss, drift, freeze mismatch, unexpected divergence
  or category the current P2 envelope cannot conservatively surface.

The helper must not emit `REPLAY_PASS`; that is reviewer-owned. It writes
nothing and has no cache, subprocess, provider or network route.

## Evidence Requirements

- Exact execution base and clean starting status.
- Seven source hashes independently recomputed before fixture authoring.
- Corpus SHA-256, case-set digest and ledger freeze marker before first replay.
- First replay output preserved in worker return; final output separately
  recorded with explanation of any code/test-only repair.
- At least eighteen cases; case/class reconciliation totals exact.
- Named proof for each zero-tolerance class and source-drift failure.
- Focused P3 tests plus current P2 focused suites to prove no regression.
- Worker-return fast gate, Core Guard, SCEC, trace, diff/status and no-commit.
- Provider call count 0 and no secret value in fixture/output.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| P3 replay mission | governed roadmap | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | Work Plan; Historical Replay Matrix | MFRP-P3 and zero-tolerance classes | MFRP roadmap | ACCEPT |
| P2 release evidence | accepted review | `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` | Decision; reviewer addendum; claim boundary | accepted material `fea7b3b2e`; current receipt/readout limitations | P2 accepted result | ACCEPT |
| receipt validation seam | executable source | `governance/compat/agent_autorun_machine_verification.py` | validation and digest functions | `_validate_receipt_integrity`; `_machine_verification_digest` | P2 receipt helper | ACCEPT |
| readout seam | executable source | `governance/compat/agent_automation_machine_verification_readout.py` | build/serialize functions | `build_machine_verification_readout`; `machine_readout_to_dict` | P2 readout helper | ACCEPT |
| H0 verifier-identity outcome | committed CVF evidence | `docs/reviews/CVF_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_WORKER_RETURN_2026-09-01.md` | verifier/dependency/interpreter drift matrix | exact hash in Frozen Historical Source Set | historical review evidence | ACCEPT |
| P1 contract-ratification outcome | committed CVF evidence | `docs/reviews/CVF_MFRP_P1_OWNER_AND_PHASE_RETURN_CONTRACT_RATIFICATION_WORKER_RETURN_2026-09-01.md` | clean docs return and reviewer addendum | exact hash in Frozen Historical Source Set | historical review evidence | ACCEPT |
| P2 receipt/readout outcome | committed CVF evidence | `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` | partial self-hash repair and claim boundary | exact hash in Frozen Historical Source Set | historical review evidence | ACCEPT |
| GCLH control-loss intake outcome | committed CVF evidence | `docs/reviews/CVF_GCLH_T0_GOVERNANCE_CONTROL_LOSS_LEARNING_INTAKE_REVIEW_2026-09-01.md` | same-agent multi-role control block | exact hash in Frozen Historical Source Set | historical review evidence | ACCEPT |
| WEB-UX unauthorized-path outcome | committed CVF evidence | `docs/reviews/CVF_WEB_UX_T3_WORKER_RETURN_2026-07-19.md` | unauthorized path finding and removal | exact hash in Frozen Historical Source Set | historical review evidence | ACCEPT |
| CADP self-attestation outcome | committed CVF evidence | `docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md` | F11 caller self-attestation residual | exact hash in Frozen Historical Source Set | historical review evidence | ACCEPT |
| latency secret-exposure outcome | committed CVF evidence | `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md` | inherited-secret exposure finding | exact hash in Frozen Historical Source Set | historical review evidence | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_ACCEPTED_P2_PLUS_FRESH_HISTORICAL_SOURCE_RECOMPUTE

priorVerificationArtifact: `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md`

priorVerificationAnchor: `fea7b3b2ee2b5f70777f7d28655b9d08f7cfbe72`

freshRecomputeRequired: execution HEAD/status, all seven source hashes, P2
helper identities, corpus/case-set hashes, freeze marker, replay results,
focused tests, changed set and gates

unicodePathHandling: literal repository-relative forward-slash paths and
UTF-8 readers; case-set digest uses ordinal code-point ordering, LF separators,
no BOM and one trailing LF

extractedTextAuthority: current committed CVF sources and exact locator text;
fixture summaries are derived evidence, not replacement authority

## Negative Search And Collision Discipline

- P3 baseline/work order and all five output paths were absent at dispatch
  authoring start.
- Exact search:
  `rg -n "MFRP-P3|MFRP_P3_HISTORICAL_REPLAY" docs CVF_SESSION governance/compat`.
- Matches were roadmap, critique and parked-successor references only.
- Disposition: `NO_ACTIVE_P3_PACKET_OR_COMPETING_REPLAY_OWNER_FOUND`.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this is a fixed seven-artifact replay sample, not a
legacy corpus absorption or completeness claim beyond the declared manifest.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | critique -> CVF reconciliation -> H0/P1/P2 -> frozen historical replay |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MFRP roadmap, accepted P2 evidence and P3 fixture/ledger |
| Disposition | consume only CVF-reconciled findings and committed historical sources; no direct external authority |
| Claim boundary | provider-free replay evidence only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`machine-first historical replay`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "machine-first historical replay" --role dispatcher --lifecycle-phase dispatch --json`
- Returned defect count: 0
- Returned defects: `NONE_RETURNED`
- Disclosed defectIds: `NONE`
- Dispatch impact: no ADIF edit; exact source identity and freeze-before-first-run are mandatory.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| literalTokensReviewed | prompt-envelope and dispatch-ready fields; Review-Dispatch scalars; SCEC schema/sets/claim binding; Source Verification columns; Core Guard labels; trace/delta fields; worker-return terms; corpus manifest/ledger/reconciliation/verdict markers |
| gateRunPurpose | confirm complete replay dispatch after direct owner and seven-source inspection |
| claimBoundary | checker conformance cannot prove replay recall, historical semantics or P3 completion |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P3 --title "Historical Replay And Frozen Defect Ledger" --date 2026-09-01 --base 2628a2fb2eb9e4a551c03411be90fe5eececad19 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --scec-problem-key mfrp-historical-replay --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | protected-governance-path plus no-commit replay worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added accepted P2 authority, seven immutable historical sources, five output paths, freeze protocol, replay matrix and fail-closed exit contract |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | corpus/case-set digests, freezeState, derivationClass, expected receipt/readout dispositions and zeroToleranceClass |
| claimBoundary | dispatch provenance only; no replay result predeclared |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create only the new P3 replay fixture,
read-only helper and focused tests. Existing production guard/receipt/readout
sources remain read-only.

Protected paths:

- `governance/compat/fixtures/mfrp_p3_historical_replay.json`
- `governance/compat/mfrp_historical_replay.py`
- `governance/compat/test_mfrp_historical_replay.py`

Operator authorization: the operator instructed continuation at the accepted
P2/P3 checkpoint.

Rollback boundary: remove these three new protected paths and the two P3
review outputs; retain P2, historical sources and full review behavior.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator -> dispatcher -> bounded no-commit replay worker -> reviewer/closer |
| phase | P3 provider-free historical replay pending reviewer decision |
| baseHeadFor(phase) | dispatchBaseHead=`2628a2fb2eb9e4a551c03411be90fe5eececad19`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exactly three new governance replay paths and two new review artifacts |
| traceScope(phase, actor) | worker records freeze-before-first-run, source hashes, first/final replay, tests, HEAD, diff, status and no-commit evidence |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no P2 owner, source evidence, roadmap, standard, catalog, hook, session, P4 or downstream edit |
| nextMoveSurfaces | reviewer P3 disposition first; continuity and any P4 checkpoint remain separate |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MFRP_P3_HISTORICAL_REPLAY_COMPLETION_2026-09-01.md`

reviewerOwnedClosurePaths: five worker outputs, paired baseline/work order,
MFRP roadmap and optional completion review; session continuity is separate.

Reviewer recomputes all source/corpus/case-set hashes, verifies the ledger
preceded first replay, samples every zero-tolerance class, reruns replay and P2
regressions, and checks the helper is read-only. Any post-run fixture/ledger
edit, source drift, missed case, hidden unclassified item, secret-like output,
sixth path or P2 production edit blocks `REPLAY_PASS`.

## Worker Output Checker Read-Ahead Mandate

Before writing the ledger or return, read checker sources applicable to each
review artifact. The return must use real first-run and final-run evidence, not
predicted PASS values. The ledger must carry Target / Source, Scope / Applies
To, source verification, corpus reconciliation, trace and claim boundary as
required by its actual path/docType.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MFRP_P3_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-01.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Claim Boundary;
Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution
Claim Boundary Control Block; Public Export Disposition; executionBaseHead;
git status --short; Changed Files; Worker Experience Retrospective; No-Commit
Statement.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block; Machine Closure Package.

Use `N/A with reason` for every non-applicable conditional block. Include
Worker Return Convergence Self-Proof, Core Guard authorization for the three
protected paths and ordinal-1 SCEC successor evidence.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: current P2 mechanics should reject structurally
invalid/stale receipts and conservatively surface safety evidence outside the
local envelope without semantic advice.

Evidence Comparison Requirement: compare frozen historical outcomes and seeded
expectations to actual receipt validation/readout results case by case.

Contradiction Or Gap Disposition: any zero-tolerance miss, hidden gap, source
drift, post-run freeze mutation or unrepresentable conservative route requires
`RETURN_TO_DESIGN`.

Claim Update Requirement: worker may return only `REPLAY_PASS_CANDIDATE`;
reviewer alone selects `REPLAY_PASS`.

## System Loop Interlock Routing

Accepted P2 -> P3 frozen historical replay -> independent P3 review. Stop
there. `successorTrancheOpened: NO`; P4 canary requires a separate operator
checkpoint and independent detection design.

## Current Runtime Freshness Verification

Freshness is current committed source plus deterministic local replay/tests.
No provider, live release bundle, external workspace or network call applies.

## Foundation Storage Layout Block

P3 creates one fixture JSON under the existing governance fixture root and two
review artifacts under the existing review root. It creates no new reference
family, registry, durable service, generated aggregate or runtime store.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF dispatcher/orchestrator |
| Provider or surface | local private provenance repository |
| Session or invocation | MFRP-P3 dispatch authoring, 2026-09-01 |
| Working directory | repository root |
| Command or tool surface | startup/source/checker reads, exact hash recomputation, negative search, scaffold stdout, ADIF resolver, apply_patch, gates and git |
| Target paths | paired P3 baseline/work order and MFRP roadmap |
| Allowed scope source | operator instruction to continue at accepted P2/P3 checkpoint |
| Before status evidence | HEAD `2628a2fb2eb9e4a551c03411be90fe5eececad19`; clean worktree; planned P3 paths absent |
| After status evidence | dispatch docs and roadmap state only; no P3 worker output |
| Diff evidence | exact three-path dispatch manifest |
| Approval boundary | P3 dispatch authoring/review only; replay execution remains checkpointed |
| Claim boundary | packet may become ready for later no-commit execution but P3 is not replayed |
| Agent type | dispatcher/orchestrator |
| Invocation ID | `mfrp-p3-work-order-dispatch-2026-09-01` |
| Expected manifest | paired P3 baseline/work order and MFRP roadmap |
| Actual changed set | paired P3 baseline/work order and MFRP roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | P3 provider-free historical replay and frozen false-negative evidence |
| claimDisposition | CLAIM_REJECTED: dispatch does not claim replay execution, semantic truth, activation, canary or closure |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no P3 replay output exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT: later worker may create exactly five P3 artifacts |
| invocationBoundary | one internal no-commit replay pass followed by independent review |
| interceptionBoundary | no provider, IDE, watcher, arbitrary command, agent reasoning or runtime interception claim |
| claimLanguage | future proof is deterministic replay candidate evidence only |
| forbiddenExpansion | P2 owner repair, standards/catalogs/hooks/session, P4-P6, downstream, provider/live, public/deploy/production |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/mfrp_historical_replay.py --fixture governance/compat/fixtures/mfrp_p3_historical_replay.json --json --enforce
python -m pytest governance/compat/test_mfrp_historical_replay.py -q
python -m pytest governance/compat/test_agent_autorun_machine_verification.py governance/compat/test_agent_automation_machine_verification_readout.py -q
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_core_guard_self_protection.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_semantic_convergence_control.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_review_cost_control.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_delta_execution_claim_boundary.py --base <executionBaseHead> --head HEAD --enforce
git diff --check
git diff --name-status
git status --short --untracked-files=all
```

Reviewer additionally recomputes freeze/source hashes independently, runs
adversarial case mutations, pre-commit and split-range pre-closure. Do not run
provider/live proof.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order coverage | Verification | Status |
|---|---|---|---|
| real-source-derived fixture and frozen ledger | Frozen Historical Source Set; Fixture Schema And Freeze Protocol | recompute seven source hashes, corpus SHA-256 and case-set digest before first replay | MAPPED |
| minimum replay families and at least eighteen cases | Replay Requirements | focused case inventory and exact family/class reconciliation | MAPPED |
| zero-tolerance defect recall | Replay Requirements; Acceptance Criteria | per-class recall equals 100% with zero averaging or waiver | MAPPED |
| mechanical result remains distinct from semantic acceptance | Expected Replay Outputs; Review Gate | helper can emit only `REPLAY_PASS_CANDIDATE`; reviewer alone may select `REPLAY_PASS` | MAPPED |
| accepted P2 production surfaces remain unchanged | Scope / Target / Owner Boundary; Required Artifact Manifest | exact changed-set check and fresh P2 focused suites | MAPPED |
| provider/live/canary/P4 remain parked | Operator Checkpoint; Claim Boundary | provider call count 0, no network/live command and `successorTrancheOpened: NO` | MAPPED |
| independent review without recreating worker implementation | Reviewer Closure Conversion; Work-Order Fulfillment Manifest | reviewer recomputes identities/results and evaluates evidence against frozen expectations | MAPPED |

## Acceptance Criteria

- [ ] Exactly five authorized uncommitted paths; no rename/deletion.
- [ ] Seven historical source identities match the dispatch contract.
- [ ] Fixture and ledger were frozen before first replay and never edited afterward.
- [ ] At least eighteen cases cover every required roadmap family.
- [ ] Every case binds a real source; seeded mutations are labeled honestly.
- [ ] Zero-tolerance recall is 100% per class with no waiver/averaging.
- [ ] False-negative and false-positive totals reconcile case by case.
- [ ] Receipt/readout gaps remain explicit and completion is never semantic advice.
- [ ] Replay helper is deterministic, read-only, provider-free and writes nothing.
- [ ] Existing P2 sources remain byte-identical and focused suites pass.
- [ ] Worker return carries Core Guard, SCEC, freeze, trace and no-commit evidence.
- [ ] Worker emits at most `REPLAY_PASS_CANDIDATE`; reviewer selects `REPLAY_PASS`.
- [ ] P4 remains unopened.

## Review Gate

Reviewer rejects replay if the corpus is tuned after first run, a source hash
is silently refreshed, a seeded mutation is called historical, a generic gap
is counted as specific detection without frozen expectation, any
zero-tolerance case is missed, a secret-like value is persisted, P2 code is
modified, or the helper gains write/subprocess/network behavior.

## Operator Checkpoint

No checkpoint is needed inside the exact five-path P3 replay scope. Stop for
any sixth path, P2 owner repair, source/ledger mutation after first replay,
standard/catalog/hook/session change, provider/live/public/downstream effect or
proposed P4 opening.

## Closure Checklist

- exact base/head, five-path manifest and no-commit evidence;
- source/corpus/case-set hashes and freeze-before-first-run proof;
- first/final replay, class recall and false-negative ledger reconciliation;
- focused P3/P2 tests, worker-fast, Core Guard, pre-commit and split pre-closure;
- reviewer disposition `REPLAY_PASS` or `RETURN_TO_DESIGN`;
- one material and at most one separate continuity commit;
- explicit P4 operator checkpoint and `successorTrancheOpened: NO`.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with five paths, immutable frozen
evidence and `REPLAY_PASS_CANDIDATE`. Return `RETURN_TO_DESIGN` for any miss,
unexpected divergence or unrepresentable zero-tolerance category. Return
`BLOCKED_WITH_REASON` for source drift, forbidden path or missing authority.

## Worker Autonomy / No-Question Rule

Worker may choose internal helper/test structure inside the fixed schema,
paths, freeze protocol and outcomes. Repair code/test-only defects without
touching frozen fixture/ledger after first replay. Do not ask for preferences;
return observable evidence and terminal disposition.

## Claim Boundary

This work order authorizes one exact five-path, no-commit, provider-free P3
historical replay. It does not authorize P2 production repair, semantic truth,
automatic review/closure, machine-first activation, P4-P6, downstream
application, provider/live, public sync, deployment or production.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF governance-foundation replay dispatch.
