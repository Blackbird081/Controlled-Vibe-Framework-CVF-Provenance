# CVF GC-018 Baseline - MFRP-P3-R1A-R2 Oracle Source-Binding Correction

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: MFRP-P3-R1A-R2

Dispatch base head: `184a290e9729b0a196db156d83375ae080bb6930`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one bounded correction of the committed R1A-R1 oracle so every
historical source locator and excerpt digest is reproducible by machine from
the cited, hash-pinned source bytes. The correction resolves the R1B reviewer
findings without changing P2 behavior, normative case meaning, family/class
coverage, or the accepted P4 design.

## Root Problem

The first R1B replay was adjudicated `RETURN_TO_DESIGN` at material checkpoint
`2b06d928d`. It proved useful runtime behavior but did not execute the source
bindings required by the R1 redesign. Independent reconstruction also found:

- C02 names an absent heading level even though its excerpt digest maps to the
  cited source;
- C06's excerpt digest is not reproducible as a contiguous LF-normalized line
  range in the cited source;
- the oracle publishes no closed extraction boundary, so even otherwise valid
  excerpt digests require search rather than deterministic reconstruction.

R1A-R2 therefore repairs the oracle evidence object first. R1B-R2 repair is
operator-authorized for later authoring, but its dispatch packet must pin the
actual committed R1A-R2 oracle bytes and cannot be finalized in advance.

## Decision / Baseline

The worker may modify exactly the existing oracle and create exactly one new
worker return. It must preserve all 19 case IDs, the exact 18-family set, the
exact seven zero-tolerance classes, mutations, predicates, feasibility
dispositions, P2 seam identity, and claim boundary unless a contradiction
requires `BLOCKED_WITH_REASON`.

Every `sourceRef` must carry a closed extraction boundary:

```json
{
  "sourceId": "...",
  "path": "repository/relative/path.md",
  "locator": "exact heading or literal anchor",
  "sourceExcerptLineRange": {
    "startLine": 1,
    "endLine": 1,
    "includeTrailingLf": false
  },
  "sourceExcerptSha256": "lowercase sha256",
  "byteRecipe": "UTF8_NO_BOM_LF_NORMALIZED_LINE_RANGE_V1"
}
```

Line numbers are one-based and inclusive. Extraction reads the source as
UTF-8 without BOM, normalizes CRLF and lone CR to LF, selects the inclusive
line range, joins selected lines with LF, and appends no LF when
`includeTrailingLf` is false. This tranche requires that exact false value.
The locator must occur inside the selected range. The SHA-256 is computed over
the resulting UTF-8 bytes.

The worker must recompute all seven `sourceManifest` hashes, both P2 seam
hashes, all 19 excerpt digests, the complete oracle raw-file hash, the
all-field JCS digest, and the three-key required-set JCS digest. No digest may
be refreshed merely to silence a mismatch: the selected excerpt must visibly
support the unchanged case derivation.

## Exact Artifact Manifest

| Artifact | Required action |
|---|---|
| `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json` | MODIFY only source-binding fields needed for deterministic reconstruction |
| `docs/reviews/CVF_MFRP_P3_R1A_R2_ORACLE_SOURCE_BINDING_CORRECTION_WORKER_RETURN_2026-09-02.md` | CREATE correction evidence and candidate disposition |

No third path, temporary repository artifact, staging, or commit is allowed.

## Acceptance Criteria

- Exact two-path changed set and clean execution base.
- All nine pinned source/P2 identities recompute and match before editing.
- Every source locator exists inside its declared line range.
- Every declared line range reproduces its excerpt digest without searching
  alternative recipes.
- C02 uses the real `## Risk / Corrective Action` heading.
- C06 uses a newly selected, semantically relevant, reproducible line range
  under its existing cited source and locator.
- All 19/18/7 coverage sets and all normative case fields are unchanged.
- Two independent validations produce byte-identical oracle and digest output.
- Provider/live/network call count is zero.
- Worker returns `ORACLE_CORRECTION_CANDIDATE` or `BLOCKED_WITH_REASON`; only
  the reviewer may ratify and commit it.

## Evidence / Verification

The return must expose exact before/after identities, all 19 line ranges and
recomputed excerpt digests, a machine-produced semantic-preservation diff,
two byte-identical reconstruction runs, exact changed-set evidence, required
gate results, and zero provider calls. Reviewer sampling supplements the full
machine reconciliation; it does not replace or repeat the worker's selection.

## Stop Conditions

Stop without guessing if any source/P2 identity drifts, a locator cannot be
placed inside a supporting exact range, a case meaning must change, any path
outside the two-path manifest is needed, or provider/live/network access would
be required. Do not edit P2, the rejected R1B evidence, the R1 redesign, P4,
checkers, standards, catalogs, registries, session state, or downstream work.

## R1B-R2 Conditional Opening Rule

The operator has authorized R1B repair authoring after R1A-R2 acceptance. That
later packet must pin the corrected oracle's committed raw SHA-256, JCS digest,
required-set digest, and containing commit; it must also pin both current P2
owners. R1B-R2 must implement the three adjudicated corrections: source
manifest/locator/excerpt execution, genuine cited-source drift rejection, and
per-case base/mutated receipt digests plus false-negative/false-positive
classification. Until those identities exist, R1B-R2 execution and P4 remain
closed.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R1 source binding | governed design | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | Source And Locator Binding; Result Ledger Contract | committed oracle and replay ledger | R1 redesign | ACCEPT |
| accepted two-tranche constraints | governed reconciliation | `docs/reviews/CVF_MFRP_P3_R1_EXTERNAL_FINDING_ABSORPTION_AND_DESIGN_RECONCILIATION_2026-09-01.md` | Binding Design Amendment | R1A/R1B division | R1 reconciliation | ACCEPT |
| current oracle identity | committed machine data | `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json` | complete JSON object | `cvf.mfrp.actualSeamReplayOracle.v1` | R1A oracle | ACCEPT |
| correction findings | reviewer-adjudicated evidence | `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md` | Independent Reviewer Adjudication | R1B-RV-1 through R1B-RV-3 | reviewer disposition | ACCEPT |
| P4 remains conditional | accepted design | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` | Dependency And Opening Rule | accepted R1B prerequisite | P4 design | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | dispatch/no-commit markers; Source Verification columns; Core Guard labels; review-admission fields; worker-return full-gate fields |
| gateRunPurpose | validate bounded correction authority and evidence shape before dispatch |
| claimBoundary | checker PASS cannot prove excerpt semantics, ratify the oracle, accept R1B, or open P4 |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`oracle source binding correction`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "oracle source binding correction" --role dispatcher --lifecycle-phase dispatch --json`
- Returned defect count: 0
- Returned defects: `NONE_RETURNED`
- Disclosed defectIds: `NONE`
- Dispatch impact: preserve exact source identity, closed extraction and
  no-commit reviewer boundary.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P3-R1A-R2 --title "Oracle Source-Binding Correction" --date 2026-09-02 --base 184a290e9729b0a196db156d83375ae080bb6930 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 2 --root-cause-cluster-id mfrp-p3-r1-oracle-source-binding-and-replay-evidence --prior-finding-set-digest a042f80260042b7f71675edc57a8fb4e33ad5a1c70963c87a471d2123d85df5c --stdout` |
| generatedProfile | protected-governance-path internal no-commit rework |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-binding recipe, two-path manifest, acceptance and conditional R1B-R2 rule |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | sourceExcerptLineRange and line extraction recipe |
| claimBoundary | scaffold provenance only; no result or successor acceptance |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify only the named committed oracle
fixture to repair deterministic source binding. No executable checker/helper,
P2 owner, hook, registry, standard, or catalog may change.

Protected path:

- `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json`

Operator authorization: explicit on 2026-09-02 for R1A-R2 oracle correction
and later R1B repair toward P4 eligibility.

Rollback boundary: restore only the oracle from its committed pre-worker bytes
and remove only the new uncommitted return.

## Claim Boundary

This baseline authorizes one local static evidence correction. It does not
ratify the corrected oracle, repair or accept R1B, run P4, change review-route
authority, alter P2, or claim safety, latency, quota, provider/live, public,
deployment, or production improvement.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance correction authority; no public sync is authorized.
