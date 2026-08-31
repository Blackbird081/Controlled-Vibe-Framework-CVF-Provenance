# CVF GC-018 SCEC-T1-R3 Locator-To-Content Evidence Binding Hardening Baseline

Memory class: governed-baseline

- Status: `READY_FOR_DISPATCH`
- Date: `2026-08-31`
- Execution base: `4a8719deda9f31a2c389760f2de0bddf43cdeb30`
- Task ID: `SCEC-T1-R3`
- Problem key: `scec-locator-content-binding`
- Governing work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_T1_R3_LOCATOR_TO_CONTENT_EVIDENCE_BINDING_HARDENING_2026-08-31.md`
- Commit authority: orchestrator/reviewer only
- Worker commit authority: none

## Purpose

Close the one SCEC foundation gap exposed by SCEC-E2: a non-empty locator that
does not occur in its hash-bound evidence file currently passes. This tranche
hardens the existing evidence-binding contract and exactly replays the failed
E2 probe. GC010 and every product/runtime successor remain parked.

## Root Problem

The checker binds a resolved blocker to a safe file path and SHA-256, but it
validates `locator` only as a non-empty string. Consequently the binding proves
which file was cited without proving that the declared location exists in that
file. E2 independently demonstrated this bypass with the real work-order path,
its correct digest, and locator
`THIS_LOCATOR_DOES_NOT_EXIST_ANYWHERE_IN_THE_FILE`; validation returned no
violation.

## Accepted Authority

| Authority | Accepted fact |
|---|---|
| `docs/assessments/CVF_SCEC_E2_EVIDENCE_BINDING_EFFECTIVENESS_VALIDATION_2026-08-31.md` | Reviewer-corrected E2 matrix records the absent non-empty locator as unexpectedly valid. |
| `docs/reviews/CVF_SCEC_E2_EVIDENCE_BINDING_EFFECTIVENESS_VALIDATION_WORKER_RETURN_2026-08-31.md` | Accepted verdict is `INEFFECTIVE_REOPEN_FOUNDATION`; only locator-to-content hardening opens. |
| `governance/compat/check_semantic_convergence_control.py` | `_validate_resolution_evidence` checks locator non-emptiness but never resolves it against evidence bytes. |
| `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | Invariant 13 claims a precise locator and fail-closed validation while preserving the semantic-truth boundary. |

## Decision / Baseline

Dispatch one integrated implementation tranche, not another decision tranche.
The canonical enforcement path must read each evidence file as one immutable
byte snapshot, compute the declared SHA-256 from that snapshot, decode the same
snapshot as strict UTF-8 for locator resolution, and require the canonical
locator literal to occur exactly once. Missing, ambiguous, non-canonical, or
non-UTF-8 locator evidence fails closed with stable codes. The checker still
does not decide whether the located statement is true.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Locator validation is non-empty-only | `governance/compat/check_semantic_convergence_control.py` | `_validate_resolution_evidence` locator branch | `locator` | SCEC checker | `ACCEPT` |
| Repository enforcement supplies only a hash resolver | `governance/compat/check_semantic_convergence_control.py` | repository resolver and `main` validation loop | `_repo_predecessor_hash_resolver`; `validate_block` | SCEC checker | `ACCEPT` |
| Exact absent-locator probe passes | `docs/assessments/CVF_SCEC_E2_EVIDENCE_BINDING_EFFECTIVENESS_VALIDATION_2026-08-31.md` | questions 7 and 10; case matrix; reviewer evidence | unresolved-locator reviewer probe | accepted E2 assessment | `ACCEPT_AS_REGRESSION_EVIDENCE` |
| E2 reopens only this foundation gap | `docs/reviews/CVF_SCEC_E2_EVIDENCE_BINDING_EFFECTIVENESS_VALIDATION_WORKER_RETURN_2026-08-31.md` | Independent Reviewer Correction; Decision / Disposition | `INEFFECTIVE_REOPEN_FOUNDATION` | accepted E2 review | `ACCEPT` |
| Existing valid bindings use source symbols suitable for exact resolution | `docs/reviews/CVF_SCEC_T1_R2_BLOCKER_RESOLUTION_EVIDENCE_BINDING_AND_HISTORICAL_REPLAY_CORRECTION_WORKER_RETURN_2026-08-31.md` | active SCEC block | `ResolutionEvidenceBindingTests`; `HistoricalT1JReplayRejectionTests` | accepted R2 return | `ACCEPT_AS_COMPATIBILITY_EVIDENCE` |

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "scec-locator-content-binding",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["SCEC_LOCATOR_NOT_BOUND_TO_EVIDENCE_CONTENT"],
    "reopened": [],
    "current": ["SCEC_LOCATOR_NOT_BOUND_TO_EVIDENCE_CONTENT"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "SCEC-T1-R3-FOUNDATION-GAP",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/reviews/CVF_SCEC_E2_EVIDENCE_BINDING_EFFECTIVENESS_VALIDATION_WORKER_RETURN_2026-08-31.md"
  }],
  "requiredDisposition": "ROOT_CONTRACT_REQUIRED",
  "successorScope": "INTEGRATED_ROOT_CONTRACT"
}
```

## Required Control Semantics

1. The repository enforcement path resolves evidence as bytes once per path;
   hash comparison and locator lookup use that same byte snapshot.
2. Locator-bearing content must decode with strict UTF-8. Decode failure is a
   stable fail-closed violation, not an ignored or replacement-decoded pass.
3. A locator is canonical only when it is a non-empty string equal to its own
   trimmed form. The exact code-point sequence must occur exactly once in the
   decoded evidence content.
4. Zero occurrences yield `RESOLUTION_EVIDENCE_LOCATOR_NOT_FOUND`; multiple
   occurrences yield `RESOLUTION_EVIDENCE_LOCATOR_AMBIGUOUS`. Non-canonical
   whitespace and non-UTF-8 content receive separate stable codes.
5. Path safety, file-only readability, hash equality, exact blocker coverage,
   claim-link rules, predecessor evidence revalidation, and mixed-fence parser
   behavior remain enforced.
6. Shape-only unit validation may use explicit injected evidence snapshots,
   but no release-quality or CLI enforcement claim may rely on a hash-only
   resolver that cannot validate locator content.
7. Locator existence proves only that the declared text exists in the cited,
   hash-bound file. Reviewer authority still decides semantic relevance and
   truth.

## Acceptance Strategy

- exact negative replay: correct E2 work-order path and digest plus
  `THIS_LOCATOR_DOES_NOT_EXIST_ANYWHERE_IN_THE_FILE` fails with the named
  not-found code;
- negative tests: duplicate locator, surrounding whitespace, invalid UTF-8,
  directory, missing file, and hash mismatch fail with stable codes;
- positive tests: both accepted R2 executable locator symbols resolve exactly
  once and existing accepted-review/executable-proof cases remain valid;
- predecessor consumption revalidates locator content from the same bytes;
- focused SCEC suite, direct checker, ADIF integrity, worker-return fast gate,
  size guard, and diff hygiene pass.

## Evidence / Verification

Dispatch evidence is the reviewer-corrected E2 result and direct source read.
Implementation proof is deferred to the no-commit worker return and must show
the pre-fix acceptance, post-fix rejection, exact positive controls, and final
gate outputs after the last edit.

## Dual Agent Surface Matrix

| Surface | Contract state | Implemented state | Evidence | Disposition | Owner |
|---|---|---|---|---|---|
| Internal dispatcher/reviewer | Integrated root contract defined | Pending worker implementation | this baseline and work order | `CONTRACT_ONLY` | orchestrator/reviewer |
| External worker surface | Exact five-path local manifest defined | Pending operator-mediated execution | governing work order | `CONTRACT_ONLY` | worker |

## ADIF Defect Registry Disclosure

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json`
- Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
- Applied entries: `ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`, `ADIF-0020`, `ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`, `ADIF-0044`, `ADIF-0055`
- Disposition: `APPLIED`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | `READY_FOR_DISPATCH`; `WORKER_MUST_NOT_COMMIT`; `Source Verification Block`; `Semantic Convergence Outcome`; active schema field; protected-path authorization labels |
| gateRunPurpose | Confirm source-derived packet structure after authoring; not discover requirements by failure. |
| claimBoundary | Structural preparation only; no implementation or semantic-truth proof. |

## Scaffold Provenance Block

- scaffoldHelperCommand: `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id SCEC-T1-R3 --title "Locator-To-Content Evidence Binding Hardening" --date 2026-08-31 --base 4a8719deda9f31a2c389760f2de0bddf43cdeb30 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --include-worker-return-skeleton --stdout`
- generatedProfile: `protected-governance-path`
- generatedSkeletonStatus: `PATTERN_REUSED_FROM_ACCEPTED_SCEC_T1_R2_PACKET`
- manualEditsAfterScaffold: `YES - exact E2-derived locator root contract replaces generic placeholders`
- checkerReadAheadConfirmation: `COMPLETE`
- docOnlyNewFields: `locator-content semantics remain pending implementation`
- claimBoundary: `dispatch authority only`

## Claim Boundary

This baseline authorizes only local SCEC locator-to-content hardening. It does
not authorize GC010, T1J-R4, T1K/T2, product/runtime edits, semantic-truth
scoring, provider/live activity, public sync, deployment, or production.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: private provenance foundation authority, not public release material.
