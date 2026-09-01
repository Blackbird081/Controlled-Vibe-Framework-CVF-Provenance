# CVF Agent Work Order - MFRP-P3-R1A-R1 Static-Only Oracle Correction

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-02

Batch ID: MFRP-P3-R1A-R1

Dispatch base head: `c94162919d3321a713c936ab8deb25fe929eab1b`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: bounded provider-free R1A-R1 static-only oracle correction worker. The worker authors a
normative JSON oracle and its evidence return; the reviewer owns ratification.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: the first R1A execution is `RETURN_TO_DESIGN` under review
SHA-256 `1f1d7126ac37dc5fd115f7663c05d0a19dfb504f55c02ae45c16710846919eea`;
its two outputs are `.rejected` evidence. The operator authorized handling the
rejection on 2026-09-02. R1B remains closed.

Do-not-misread notes: static-only forbids importing/dynamically loading P2,
calling any P2 function for any purpose, constructing a positive-control or
case receipt/payload, executing AST/code, monkeypatching or running tests. Read
source text/bytes only. Do not copy the rejected oracle or open a successor.

Required first actions: acknowledge startup authority; capture exact HEAD and
clean status; read the paired baseline, this packet, guard orientation and
literal gotchas; recompute seven historical and two P2 source hashes; inspect
all source/checker paths named below; run pre-implementation; then create only
the exact two-path worker manifest.

Return contract: leave all changes uncommitted. Return
`COMPLETE_PENDING_REVIEW` with terminal candidate
`ORACLE_RATIFICATION_CANDIDATE` only when source gaps are zero, exact coverage
reconciles and every case has static feasibility evidence. Otherwise return
`BLOCKED_WITH_REASON`. The worker never emits `ORACLE_RATIFIED_BOUNDED`.

Worker: delegated local oracle evidence worker

Reviewer/closer: CVF orchestrator/reviewer

Worker return path: `docs/reviews/CVF_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_WORKER_RETURN_2026-09-02.md`

successorTrancheOpened: NO

## Purpose

Create a fresh committed-oracle candidate that corrects R1A-RV-1 through
R1A-RV-6. Convert all eighteen families into source-bound normative cases and
honest static feasibility dispositions using only source text/bytes. Preserve
unrepresentable gaps without executing or predicting R1B observations.

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`.

The operator authorizes R1A authoring, the dispatcher fixes authority and
scope, the worker produces two uncommitted artifacts, and the independent
reviewer recomputes identities/feasibility and alone ratifies or rejects. Trust
comes from source paths, hashes, locators, field routes and independent
comparison, not from role/provider labels.

Task classification: provider-free documentary and machine-data oracle
authoring. Any runtime invocation, executable helper, P2 repair, source rewrite,
third path, provider/live route or successor opening stops the worker.

Intake summary: the operator opened R1A authoring after accepted independent
critique absorption; this packet converts that authority into an exact
two-path, source-verified, no-execution worker assignment.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: MFRP-P3-R1A-R1
reviewRoundCount: 1
priorFindingSetDigest: 1f1d7126ac37dc5fd115f7663c05d0a19dfb504f55c02ae45c16710846919eea
dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR
reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS
newIndependentCriticalEvidence: R1A_EXECUTION_CONTRACT_BREACH_AND_SEMANTIC_MISMATCH
regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 1
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: ONE_CONSOLIDATED_REWORK
rootCauseClusterId: mfrp-p3-r1a-static-oracle-control
reworkGeneration: 1
consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

## Worker Autonomy / No-Question Rule

The worker must resolve routine allowed-scope JSON shape, locator, digest,
static-feasibility and worker-return gate failures directly by reading the
named source/checker. Ask no preference questions. Return only for a real
source contradiction, forbidden-path need, missing authority, replay/P2-edit
need or another stop condition that cannot be repaired inside the two paths.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "mfrp-p3-r1a-oracle",
  "chainMode": "SUCCESSOR",
  "chainOrdinal": 2,
  "predecessor": {
    "path": "docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md",
    "sha256": "1f1d7126ac37dc5fd115f7663c05d0a19dfb504f55c02ae45c16710846919eea"
  },
  "blockerDelta": {
    "prior": ["r1a-oracle-not-yet-ratified", "r1a-static-only-execution-boundary", "r1a-family-mechanism-mismatch"],
    "resolved": ["r1a-static-only-execution-boundary", "r1a-family-mechanism-mismatch"],
    "retained": ["r1a-oracle-not-yet-ratified"],
    "new": [],
    "reopened": [],
    "current": ["r1a-oracle-not-yet-ratified"]
  },
  "resolutionEvidence": {
    "r1a-static-only-execution-boundary": {
      "evidenceClass": "ACCEPTED_REVIEW",
      "evidencePath": "docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md",
      "sha256": "1f1d7126ac37dc5fd115f7663c05d0a19dfb504f55c02ae45c16710846919eea",
      "locator": "## Consolidated Correction Contract"
    },
    "r1a-family-mechanism-mismatch": {
      "evidenceClass": "ACCEPTED_REVIEW",
      "evidencePath": "docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md",
      "sha256": "1f1d7126ac37dc5fd115f7663c05d0a19dfb504f55c02ae45c16710846919eea",
      "locator": "## Consolidated Correction Contract"
    }
  },
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 1,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "MFRP-P3-R1A-R1-DISPATCH-STATIC-ORACLE",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/baselines/CVF_GC018_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

The worker return is the successor evidence packet and uses the committed work
order as its predecessor. It cannot resolve the blocker by self-assertion.
Reviewer acceptance and a committed oracle identity are required before R1B
can even be authored.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator correction instruction | current operator message dated 2026-09-02 | ACCEPT |
| accepted R1 reconciliation | `docs/reviews/CVF_MFRP_P3_R1_EXTERNAL_FINDING_ABSORPTION_AND_DESIGN_RECONCILIATION_2026-09-01.md` | ACCEPT |
| independent R1A rejection | `docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md`; SHA-256 `1f1d7126ac37dc5fd115f7663c05d0a19dfb504f55c02ae45c16710846919eea` | ACCEPT |
| paired GC-018 baseline | `docs/baselines/CVF_GC018_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md`; SHA-256 `7cc94d946754e830764c9c071786c84efca2e37cafe9c4814fe0402de8be2928` | ACCEPT |
| R1 design | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | ACCEPT |
| execution anchor | worker captures current HEAD and clean status before edits | REQUIRED_AT_EXECUTION |

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | Opened R1A authoring; owns scope expansion or successor opening. |
| Dispatcher | Pins sources, P2 seams, schema, exact paths and stop conditions. |
| Worker | Authors only the JSON oracle and evidence return without commit. |
| Reviewer/closer | Recomputes every binding and alone ratifies, repairs or rejects. |

The reviewer checks results; it does not repeat authoring of eighteen cases.

## Scope / Target / Owner Boundary

Target: exactly two fresh R1A-R1 artifacts. The worker reads the nine pinned
sources and calculates static evidence from text/bytes. It must not reuse the
rejected oracle, import/dynamically load P2, call P2 functions for any purpose,
construct any receipt/payload or run tests/executable probes.

Owner boundary:

- receipt object/digest/integrity semantics remain owned by
  `governance/compat/agent_autorun_machine_verification.py`;
- readout/serialization semantics remain owned by
  `governance/compat/agent_automation_machine_verification_readout.py`;
- the R1A JSON owns normative inputs and static feasibility only;
- historical documents provide provenance, not observed P2 behavior;
- reviewer owns ratification and future predecessor identities;
- R1B owns any later mutation/replay/result evidence under a separate order.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. `CVF_SESSION_MEMORY.md`
3. active handoff named by the bootstrap model
4. `docs/reference/guard_orientation/README.md`
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
6. paired R1A baseline and this work order
7. MFRP roadmap Historical Replay and P3-R1 sections
8. R1 design assessment and external-finding reconciliation
9. both current P2 seam files in full
10. all seven historical source paths
11. every checker source in the Checker Source Read-Ahead Block

## Pre-Flight Checks

1. Capture `git rev-parse HEAD`; require exact clean execution base.
2. Confirm both authorized outputs are absent and every read-only source exists.
3. Recompute seven historical and two P2 source hashes; stop on mismatch.
4. Inspect actual P2 fields/symbols before assigning any feasibility status.
5. Run the pre-implementation bundle at the clean execution base.
6. Stop before writing for any third-path, replay, P2-edit or source-gap need.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "MFRP-P3-R1A-R1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "DOC_CHANGE",
    "authorityImpact": "ENRICHES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["governance/compat/fixtures", "docs/baselines", "docs/work_orders", "docs/reviews"],
  "claims": ["normative static oracle candidate only"],
  "requiredProof": [
    "seven historical and two P2 source identities",
    "at least eighteen source-bound cases",
    "exact eighteen-family and seven-class coverage",
    "per-case static feasibility evidence",
    "no observed or runtime result fields",
    "exact two-path no-commit manifest",
    "independent reviewer disposition"
  ],
  "operatorCheckpoints": [
    "any third path or existing-source modification",
    "any replay or P2 seam invocation",
    "any R1B P4 or external effect"
  ],
  "forbiddenEffects": [
    "runtime provider network public deploy production or downstream effect",
    "worker oracle ratification or automatic successor opening",
    "worker commit or P2 owner mutation"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded nine-file named source set",
    "completenessClaimChanged": false
  }
}
```

Expected route: `P3_ELEVATED`; shadow routing only. The full legacy gate bundle
remains required.

## Frozen Historical Source Set

| Source ID | Source | SHA-256 |
|---|---|---|
| H0 | `docs/reviews/CVF_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_WORKER_RETURN_2026-09-01.md` | `7e46de88180cdd0f0c6fac3ba97c1ed1491f73ef5518499fab58be6ca69ae2f0` |
| P1 | `docs/reviews/CVF_MFRP_P1_OWNER_AND_PHASE_RETURN_CONTRACT_RATIFICATION_WORKER_RETURN_2026-09-01.md` | `9a9ae6eb9bad0387548a3eb77d657e99e4529562e47a2e0619d07c47f3324e06` |
| P2 | `docs/reviews/CVF_MFRP_P2_RECEIPT_AND_REVIEWER_READOUT_COMPOSITION_WORKER_RETURN_2026-09-01.md` | `b2461af32c1da084cc90a7c1a4cbcc6a614ab454ce1327fe313374e9d6409a1f` |
| GCLH | `docs/reviews/CVF_GCLH_T0_GOVERNANCE_CONTROL_LOSS_LEARNING_INTAKE_REVIEW_2026-09-01.md` | `5b4921a5d2dc410f576148b7d228be6ab2d5fcfd935e3aba79602cf17234f658` |
| WEBUX | `docs/reviews/CVF_WEB_UX_T3_WORKER_RETURN_2026-07-19.md` | `014148d41ef5363ef09689e38c960dbc58af494ba547ba72e5db711b13689fe1` |
| CADP | `docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md` | `48539fd30f038a46cc4cbe3282aa90ba79880bb907634ee4e24cc53b83c451b1` |
| LATENCY | `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md` | `3629e33e6cda3171c7d3035f2423475e1c5005e936b6a3e94441bcf0cac3af45` |

Any mismatch returns `BLOCKED_WITH_REASON: SOURCE_DRIFT`. The worker cannot
refresh a contract hash to make the oracle pass.

## P2 Seam Static Feasibility Sources

| Owner | SHA-256 | Static evidence surface |
|---|---|---|
| `governance/compat/agent_autorun_machine_verification.py` | `8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022` | receipt v3/profile constants, object fields, digest and validation branches |
| `governance/compat/agent_automation_machine_verification_readout.py` | `ff6088bf8144deec4582ce9faf62384b314346c9cbbb87f6b3349a2d23f7e7c3` | readout fields, completion-token rule, normalization and serialization |

The worker records both hashes under `p2SeamIdentity`. Static filesystem and
source-text inspection is allowed. Importing or dynamically loading either
module, calling any function, or constructing any receipt or payload object is
forbidden even when described as a positive control.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | non-executable JSON fixture under existing `governance/compat/fixtures/` plus reviewer-facing return under existing `docs/reviews/` |
| Storage decision | reuse the existing fixture and review directories; create no new folder, index, front door or registry |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | the oracle is normative machine data only; it creates no helper runtime, hidden store or parallel source of truth |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json` | CREATE one UTF-8 JSON normative oracle with exact sources, seam identities, sets, cases and static feasibility evidence |
| `docs/reviews/CVF_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_WORKER_RETURN_2026-09-02.md` | CREATE checker-safe no-commit evidence return with hash/set/feasibility reconciliation and terminal candidate |

Exactly these two paths may change. No rename or deletion.

## Work-Order Fulfillment Manifest

| Requirement | Owning section | Required worker evidence |
|---|---|---|
| exact two-path scope | Required Artifact Manifest; Core Guard authorization | initial/final status and exact changed-set reconciliation |
| historical identity | Frozen Historical Source Set | seven recomputed hashes, all MATCH |
| P2 identity | P2 Seam Static Feasibility Sources | two recomputed hashes and named symbol/field routes |
| oracle shape | Oracle Schema And Forbidden Fields | JSON parse, exact keys/tokens and forbidden-field scan |
| source binding | Source Locator And Excerpt Contract | per-case locator/excerpt digest resolution |
| exact coverage | Required Case/Family/Class Sets | set/count digests and zero missing/extra values |
| feasibility | Static Feasibility Contract | per-case route plus aggregate status totals |
| no execution | Forbidden Actions; Claim Boundary | no receipt/replay/helper/test/provider invocation and providerCallCount 0 |
| independent acceptance | Reviewer Closure Conversion | reviewer selects ratification or return-to-design |

## Oracle Schema And Forbidden Fields

The worker must follow the complete Oracle Contract in the paired baseline.
Required schema/profile tokens are `cvf.mfrp.actualSeamReplayOracle.v1` and
`MFRP_P3_R1_DISPATCHER_RATIFIED_ORACLE`.

Each case contains only normative input and static reachability data:

- stable `caseId` and one exact required family;
- exact `sourceRef` path/locator/excerpt digest and byte recipe;
- `HISTORICAL_INPUT` or `SEEDED_DERIVATION`;
- `MFRP_P2_CANONICAL_VALID_RECEIPT_V3` base profile;
- one typed closed mutation with exact JSON pointer;
- `AFTER_BINDING`, `ATTACKER_REBOUND`, or `NO_MUTATION`;
- one closed safety predicate, zero-tolerance class and prohibited outcome;
- one feasibility disposition and evidence object.

Closed safety predicates are `RECEIPT_REJECTED`,
`GAP_SURFACED_UNCLASSIFIED`, `NO_COMPLETION_TOKEN`,
`SECRET_SENTINEL_NOT_EMITTED`, `IDENTITY_DRIFT_REJECTED`,
`HARD_OBLIGATION_NOT_CLOSED`, and `POSITIVE_CONTROL_VALID`.

No case may contain an `observed*` or `actual*` key, validator/readout result,
runtime pass/fail, detected/recall field, result ledger field, replay terminal,
or reviewer acceptance. The return may report shape/feasibility counts but no
case execution result.

## Source Locator And Excerpt Contract

Every case binds one of the seven source IDs to the exact same path in
`sourceManifest`, one unique reviewable heading/locator and an excerpt digest.
The excerpt byte recipe is exact selected text after CRLF-to-LF normalization,
encoded UTF-8 without BOM, with no implicit leading/trailing whitespace added.
The locator/excerpt selection must be reproducible from the worker return.

Missing, duplicate or ambiguous locator, digest mismatch, or source ID/path
disagreement is `BLOCKED_SOURCE_GAP`. Do not weaken a locator to a whole file
or rewrite historical source text.

## Required Case Family And Class Sets

The JSON must contain at least eighteen unique ordered case IDs. It must cover
exactly the eighteen family tokens and seven zero-tolerance tokens listed in
the paired baseline. The worker may add a second case for a family only when a
distinct mutation/predicate is required; extra family or class tokens are
forbidden.

Cases may use `NONE` for non-zero-tolerance positive controls, while every one
of the seven required classes appears at least once. A class occurrence proves
normative coverage only, not representability or detection.

## Static Feasibility Contract

For every case, inspect current P2 source and choose exactly one:

- `STATICALLY_REACHABLE`: name the concrete owner path, symbol/field route,
  JSON-pointer mutation target and readout/validator predicate route;
- `NOT_REPRESENTABLE_BY_CURRENT_P2`: identify the missing field/route and why
  no current P2 observation can support the predicate without inventing data;
- `BLOCKED_SOURCE_GAP`: identify the unresolved source/locator/excerpt fact and
  stop ratification candidacy.

Do not infer reachability from the rejected fixture's expected strings. Do not
execute a sample to settle feasibility. When a P2 readout copies a field even
on invalid input, account for that behavior when judging secret-safe or
unclassified predicates. When P2 exposes only fixed local `NOT_CHECKED`
surfaces, do not claim it represents arbitrary seven-phase evidence.

The following first-return corrections are mandatory:

| Case/family | Required R1A-R1 disposition |
|---|---|
| C07 attacker-rebound verifier self-attestation | prove from source that a fully rebound nested digest, top-level verifier digest and receipt digest is rejected; otherwise use `NOT_REPRESENTABLE_BY_CURRENT_P2` |
| C08 earlier-batch verifier/shared-dependency drift | bind a real cross-batch source-identity comparison route; a nested/top-level envelope mismatch is insufficient; otherwise use `NOT_REPRESENTABLE_BY_CURRENT_P2` |
| C16 cache hit plus one-bound-input invalidation | represent both halves through a current P2 route; a no-mutation positive control alone is insufficient; otherwise use `NOT_REPRESENTABLE_BY_CURRENT_P2` |
| C18 high-risk/live/public/destructive conservative verification | use `NOT_REPRESENTABLE_BY_CURRENT_P2` unless an existing P2 input actually carries high-risk authority |

Run the same family-to-mechanism audit over every other case. Generic digest
tamper or ordinary structural rejection cannot stand in for a materially
different historical family.

The worker return must reconcile:

- total cases = sum of the three feasibility statuses;
- exact case/family/class sets and deterministic digests;
- zero source gaps for `ORACLE_RATIFICATION_CANDIDATE`;
- every unrepresentable case ID retained and excluded from detected/satisfied
  claims.

## Required Proof Manifest Atomic Literal Discipline

Use the exact two-path Required Artifact Manifest unchanged in initial status,
final status, Changed Files, Agent Operation Trace `Expected manifest` and
`Actual changed set`. Do not reconstruct a second list from prose. Any third
path is an unauthorized addition and forces `BLOCKED_WITH_REASON`.

## Write Ownership

| Path | Owner | Mode |
|---|---|---|
| `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json` | worker authors; reviewer verifies | CREATE |
| `docs/reviews/CVF_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_WORKER_RETURN_2026-09-02.md` | worker authors; reviewer repairs/accepts | CREATE |

## Execution Plan

1. Capture clean execution base and recompute all nine source hashes.
2. Read all seven historical sources and both P2 seam files in full.
3. Select exact source locators/excerpts and calculate their digests.
4. Author the JSON oracle without invoking P2 or producing observations.
5. Run JSON/set/hash/forbidden-key static checks only.
6. Author the checker-safe worker return with feasibility reconciliation.
7. Run required gates, reconcile exactly two paths and return uncommitted.

## Acceptance Criteria

Worker may return `COMPLETE_PENDING_REVIEW` only when:

- execution started clean at the captured base;
- exactly two new paths exist and no existing path changed;
- all nine pinned file hashes match;
- JSON parses and has exact schema/profile/top-level fields;
- at least eighteen unique cases exactly cover required family/class sets;
- every case resolves source/locator/excerpt and carries full feasibility;
- source-gap count is zero;
- no forbidden observed/runtime/result key or claim exists;
- no P2 invocation, receipt construction, replay, provider/live/network call,
  commit, stage or successor opening occurred;
- worker-return fast gate and required governance gates pass.

The terminal value is `ORACLE_RATIFICATION_CANDIDATE`. Any number of honest
`NOT_REPRESENTABLE_BY_CURRENT_P2` cases remains visible for reviewer decision;
the worker cannot convert them to PASS or remove their families.

## Evidence Requirements

The worker return must record exact command/result evidence for the clean base,
nine file hashes, every excerpt digest, JSON parsing, required/actual case,
family and class sets, all three feasibility totals, forbidden-key search,
exact changed set, required gates, no staged changes, no commit and zero
provider calls. Evidence must distinguish static reachability from observed
behavior and must list every unrepresentable case ID.

## Stop Conditions

Return `BLOCKED_WITH_REASON` immediately for source/seam hash drift, source
gap, need for a third path or existing-file edit, inability to represent the
required schema without observed-result fields, any request to run R1B early,
or any provider/live/network/credential/public/downstream requirement.

If static analysis reveals a P2 design gap, record it as
`NOT_REPRESENTABLE_BY_CURRENT_P2`; do not repair P2. If the gap prevents a
source locator/excerpt from resolving, use `BLOCKED_SOURCE_GAP` and stop.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with
`ORACLE_RATIFICATION_CANDIDATE`, zero source gaps, exact coverage, complete
static feasibility evidence and all required gates PASS. Return
`BLOCKED_WITH_REASON` for any stop condition. Never return a reviewer-owned
ratification token, replay PASS, successor-open token or semantic safety claim.

## Operator Checkpoint

No further operator input is required for routine two-path authoring. Stop and
request operator direction only if completion requires a third path, existing
source/P2 edit, altered required family/class/schema contract, replay/runtime
work, provider/live/network/public/downstream effect or automatic R1B opening.
R1B remains a separate future checkpoint even if R1A is reviewer-ratified.

## Forbidden Actions

- Do not import or dynamically load either P2 module and do not call
  `_machine_verification_object`, `_machine_verification_digest`,
  `_validate_receipt_integrity`, `build_machine_verification_readout`,
  `machine_readout_to_dict` or any other P2 function for any purpose.
- Do not build a positive-control, case receipt, payload object, mutated
  payload, replay output or result ledger, in memory or on disk.
- Do not execute AST/source code, monkeypatch, run tests or create any
  Python/helper/test/cache/temp executable artifact.
- Do not modify P2, historical sources, rejected evidence, roadmap, design,
  reconciliation, baseline, work order, standard, checker, hook or session.
- Do not stage, commit, push, call a provider, use network, read credentials,
  public-sync, deploy, mutate downstream workspace or open R1B/P4.

## Verification Commands

The worker must run local provider-free commands only, including:

```powershell
git rev-parse HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m json.tool governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
git diff --name-status
git diff --cached --name-status
git status --short
```

Additionally record read-only scripts/commands used to recompute file hashes,
excerpt digests, exact sets and forbidden-key scans. Do not use a command that
imports/invokes P2 seams or writes outside the two authorized paths.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md`

priorVerificationAnchor: `1f1d7126ac37dc5fd115f7663c05d0a19dfb504f55c02ae45c16710846919eea`

freshRecomputeRequired: execution HEAD/status, nine source hashes, all case
locators/excerpt hashes, JSON shape, exact case/family/class sets, feasibility
routes, forbidden-key scan, changed set and required gates

unicodePathHandling: repository-relative forward-slash paths and UTF-8-safe
readers; JSON and excerpt bytes use UTF-8 without BOM and normalized LF

extractedTextAuthority: current committed CVF source bytes and exact locators;
oracle summaries are derived normative evidence, not replacement authority

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| four proposed R1A paths | all returned `False` under `Test-Path` before authoring | ABSENT_BEFORE_AUTHORING |
| token search | `rg -n "MFRP-P3-R1A-R1|actualSeamReplayOracle|mfrp_p3_r1a_actual_seam_replay_oracle" docs CVF_SESSION governance/compat` | only design/reconciliation/rejected-history references; no active oracle owner |
| collision decision | new R1A pair follows accepted R1/R1A split and does not reuse rejected paths | NO_ACTIVE_R1A_ORACLE_OR_COMPETING_OWNER_FOUND |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R1A mission and eighteen/seven coverage | governed roadmap | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | Work Plan; Historical Replay And Hostile Test Matrix; P3-R1 Actual-Seam Correction | R1A and required families/classes | MFRP roadmap | ACCEPT |
| oracle schema and R1A/R1B boundary | governed design | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | Tranche Split; Committed Oracle; Safety Predicates; Freeze; Stops | `cvf.mfrp.actualSeamReplayOracle.v1` | R1 design | ACCEPT |
| four mandatory corrections | accepted review | `docs/reviews/CVF_MFRP_P3_R1_EXTERNAL_FINDING_ABSORPTION_AND_DESIGN_RECONCILIATION_2026-09-01.md` | Binding Design Amendment | per-case feasibility and two P2 seam hashes | R1 review authority | ACCEPT |
| failed R1A correction set | independent review | `docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md` | Findings / Position; Consolidated Correction Contract | R1A-RV-1 through R1A-RV-6 | R1A-R1 correction owner | ACCEPT |
| paired baseline | dispatch baseline | `docs/baselines/CVF_GC018_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md` | Decision, contracts, exact manifests and stops | SHA-256 `7cc94d946754e830764c9c071786c84efca2e37cafe9c4814fe0402de8be2928` | GC-018 R1A-R1 baseline | ACCEPT |
| receipt field/validator feasibility | executable source | `governance/compat/agent_autorun_machine_verification.py` | constants, object builder and validator | `_machine_verification_object`; `_validate_receipt_integrity` | P2 receipt owner | ACCEPT |
| readout field/serializer feasibility | executable source | `governance/compat/agent_automation_machine_verification_readout.py` | readout builder and serializer | `build_machine_verification_readout`; `machine_readout_to_dict` | P2 readout owner | ACCEPT |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this is a fixed nine-file source-bound oracle
authoring task, not a legacy corpus absorption or broad completeness claim.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | preserved advisory -> CVF absorption review -> binding R1A baseline/work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R1 reconciliation, paired baseline and this work order |
| Disposition | consume only the four CVF-verified amendments; raw advisory is not authority |
| Claim boundary | static local oracle authoring only; no external execution or authority transfer |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`committed oracle ratification`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "committed oracle ratification" --role dispatcher --lifecycle-phase dispatch --json`
- Returned defect count: 0
- Returned defects: `NONE_RETURNED`
- Disclosed defectIds: `NONE`
- Dispatch impact: exact source identity, static feasibility, oracle/runner
  separation, forbidden observed fields and no-commit controls are mandatory.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | prompt envelope first-section fields; Review-Dispatch scalars; SCEC predecessor/sets/claim fields; Task Governance eight dimensions; Source Verification columns; Core Guard authorization; worker-return fast-doc literals; trace and delta row labels |
| gateRunPurpose | confirm a complete static-oracle dispatch after direct owner/source inspection and real negative searches |
| claimBoundary | checker conformance cannot prove case feasibility, source semantics, oracle ratification or R1B readiness |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P3-R1A-R1 --title "Static-Only Oracle Correction" --date 2026-09-02 --base c94162919d3321a713c936ab8deb25fe929eab1b --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id mfrp-p3-r1a-static-oracle-control --prior-finding-set-digest 1f1d7126ac37dc5fd115f7663c05d0a19dfb504f55c02ae45c16710846919eea --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --new-independent-critical-evidence R1A_EXECUTION_CONTRACT_BREACH_AND_SEMANTIC_MISMATCH --scec-problem-key mfrp-p3-r1a-oracle --scec-chain-mode SUCCESSOR --scec-chain-ordinal 2 --scec-predecessor-path docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md --scec-predecessor-sha256 1f1d7126ac37dc5fd115f7663c05d0a19dfb504f55c02ae45c16710846919eea --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | protected-governance-path plus no-commit documentary/machine-data profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with accepted R1A authority, exact two-path scope, schema/feasibility contracts, nine hashes, fast-doc return shape and no-execution stops |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | feasibilityDisposition, feasibilityEvidence, sourceExcerptSha256, p2SeamIdentity, requiredSafetyPredicate, prohibitedOutcome |
| claimBoundary | dispatch provenance only; no oracle outcome, replay result or successor is predeclared |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one non-executable JSON fixture
under the governed compat fixture directory; do not change any existing guard,
checker, helper, test, catalog or hook.

Protected path:

- `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json`

Operator authorization: the operator explicitly opened R1A authoring on
2026-09-02.

Rollback boundary: remove only the new oracle and worker return if rejected;
retain P2 owners, design/reconciliation and all historical/rejected evidence.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator -> dispatcher -> bounded no-commit oracle worker -> reviewer/closer |
| phase | R1A static oracle candidate pending independent ratification |
| baseHeadFor(phase) | dispatchBaseHead=`c94162919d3321a713c936ab8deb25fe929eab1b`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exactly one new oracle JSON and one new worker return |
| traceScope(phase, actor) | worker records initial/final status, nine hashes, locators/excerpts, exact sets, feasibility totals, static checks, gates and no-commit evidence |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no R1B, P2 owner, historical source, rejected evidence, standard, checker, hook, session, downstream or P4 edit |
| nextMoveSurfaces | independent R1A review first; R1B authoring requires accepted and committed oracle identities plus a separate operator-governed work order |

## Reviewer Closure Conversion

completionReviewPath: N/A with reason: prefer reviewer addendum and closure
evidence in the worker return unless a material correction requires a separate
operator-authorized packet.

reviewerOwnedClosurePaths: the exact two worker outputs, paired baseline/work
order and continuity surfaces in a separate post-material sync.

closureOwner: CVF orchestrator/reviewer.

workerCommitPermission: FORBIDDEN.

The reviewer recomputes all hashes/digests/sets, audits every feasibility route,
challenges one locator and one P2 route, searches forbidden keys and decides
`ORACLE_RATIFIED_BOUNDED` or `RETURN_TO_DESIGN`. The reviewer must not execute
R1B or silently author missing cases for the worker.

## Worker Output Checker Read-Ahead Mandate

Before writing the JSON, derive its exact schema from the baseline/design and
validate it with read-only JSON/set/hash checks. Before writing the worker
return, read `governance/compat/check_worker_return_quality_gate.py`,
`governance/compat/check_agent_operation_trace.py`,
`governance/compat/check_delta_execution_claim_boundary.py`,
`governance/compat/check_governed_artifact_checker_read_ahead.py` and all
conditional checker sources triggered by the actual content.

Do not list heading-prefixed literals before real worker-return sections. Do
not retain scaffold placeholders. Record first-run and final-run gate evidence
after edits are complete.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_WORKER_RETURN_2026-09-02.md`

contractProfile: WORKER_RETURN_FAST_DOC_V1

scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT

Commit mode: WORKER_MUST_NOT_COMMIT

publicSyncDisposition: FORBIDDEN

liveRuntimeDisposition: FORBIDDEN

checkerMutationDisposition: FORBIDDEN

workerSelfSelection: FORBIDDEN

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Self-declared worker-return artifact: yes; Responds to work
order; dispatchWorkOrder; Purpose; Scope / Methodology; Findings / Position;
Risk / Corrective Action; Checker Source Read-Ahead Block; Agent Operation
Trace Block; Delta Execution Claim Boundary Control Block; Finding-To-
Governance Learning Disposition; Epistemic Process Block; Conditional Controls
Disposition; Claim Boundary; git status --short; Changed Files; Command
Evidence; No-Commit Statement; executionBaseHead.

Conditional Controls Disposition must state:
`conditionalControlsDisposition: EKI_NA; RIH_NA; CCRI_NA` with concise reasons:
external critique was already CVF-reconciled, no rescan occurred, and this is
a bounded named-file task rather than a corpus-completeness claim.

## Review Gate

The worker return is evidence, not acceptance. Reviewer must verify:

1. exact two-path diff and no staged files;
2. exact nine file hashes and reproducible excerpt digests;
3. JSON schema/profile/forbidden-key discipline;
4. exact case/family/class sets and count reconciliation;
5. every `STATICALLY_REACHABLE` route exists in current P2 source;
6. every `NOT_REPRESENTABLE_BY_CURRENT_P2` rationale is honest and retained;
7. zero `BLOCKED_SOURCE_GAP` for ratification eligibility;
8. no receipt/replay/P2 invocation or successor effect;
9. current required gates pass independently.

Any false reachability, missing family/class, source drift, hidden
unrepresentable case or third path is `RETURN_TO_DESIGN`.

## Closure Checklist

- [ ] execution base and initial clean status recorded;
- [ ] exact two-path manifest equals final changed set;
- [ ] nine file hashes and every source excerpt digest recomputed;
- [ ] JSON schema/profile and exact sets reconcile;
- [ ] each case has one allowed feasibility disposition and evidence object;
- [ ] all unrepresentable case IDs remain visible and uncounted as detected;
- [ ] forbidden observed/runtime/result key scan passes;
- [ ] no replay, P2 invocation/edit, provider call, stage or commit occurred;
- [ ] worker-return fast gate and reviewer-fast bundle pass;
- [ ] independent reviewer disposition remains pending;
- [ ] `successorTrancheOpened: NO` remains exact.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF dispatcher/author |
| Provider or surface | local private provenance repository |
| Session or invocation | MFRP-P3-R1A-R1 dispatch authoring, 2026-09-02 |
| Working directory | repository root |
| Command or tool surface | source reads, hashes, negative search, ADIF resolver, scaffold helper, apply_patch and governance gates |
| Target paths | paired R1A baseline and work order only |
| Allowed scope source | operator instruction to open R1A authoring under accepted two-tranche reconciliation |
| Before status evidence | HEAD `c94162919d3321a713c936ab8deb25fe929eab1b`; clean worktree confirmed; all four proposed paths absent |
| After status evidence | one baseline and one work order authored; worker output paths remain absent |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | R1A dispatch authoring only; no worker execution |
| Claim boundary | no oracle artifact, ratification, replay, P2 mutation, R1B/P4 or external effect |
| Agent type | dispatcher/author |
| Invocation ID | `mfrp-p3-r1a-dispatch-authoring-2026-09-02` |
| Expected manifest | `docs/baselines/CVF_GC018_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch authoring |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | R1A baseline/work-order authoring and later static oracle candidate only |
| claimDisposition | CLAIM_REJECTED: no runtime execution-control, replay, interception, receipt validation result or semantic closure is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: R1A must not construct, consume or validate a replay receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: authoring creates local evidence artifacts only and performs no external/runtime action |
| invocationBoundary | static source/hash/JSON checks only; P2 seam and replay invocation are forbidden |
| interceptionBoundary | no wrapper, proxy, lifecycle hook, autorun activation or agent coding control is authorized |
| claimLanguage | normative oracle candidate and static feasibility evidence only |
| forbiddenExpansion | no R1B, P2 modification, runtime/provider/live/public/package/Web/MCP/downstream/deploy/production behavior without fresh authority |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap/design control | Work-order owner | Mapping |
|---|---|---|
| committed oracle precedes runner | exact two-path manifest and forbidden actions | MAPPED |
| at least eighteen cases/every family | Required Case Family And Class Sets | MAPPED |
| seven zero-tolerance classes | paired baseline and set reconciliation | MAPPED |
| source/locator/excerpt binding | Source Locator And Excerpt Contract | MAPPED |
| closed typed mutations/predicates | Oracle Schema And Forbidden Fields | MAPPED |
| per-case static feasibility | Static Feasibility Contract | MAPPED |
| both P2 seam hashes pinned | P2 Seam Static Feasibility Sources | MAPPED |
| no worker ratification/successor | Return contract, Review Gate and Claim Boundary | MAPPED |
| R1B byte-change/same-payload proof | explicitly deferred to separate R1B work order | PARKED_NOT_R1A |

## Claim Boundary

This work order authorizes only an exact two-path provider-free R1A worker pass
that produces a normative JSON oracle candidate and static feasibility return.
It does not authorize oracle ratification by the worker, receipt construction,
P2 seam invocation, replay, runner/test/result ledger, P2 repair, review-cost
uplift claim, R1B/P4-P6, lifecycle activation, downstream workspace edits,
provider/live/network/credential access, public sync, deployment or production.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF governance-foundation R1A dispatch.
