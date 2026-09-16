# CVF ACEL G2 T2 Candidate Qualification T0 Audit

Memory class: governed-audit

Status: COMPLETE_PENDING_REVIEW

docType: audit

Date: 2026-09-16

Batch ID: ACEL-G2-T2-CANDIDATE-QUALIFICATION-T0

executionBaseHead: `af218333f1005e7aa51ba318a172cb9b1336df7b`

Companion machine ledger: `docs/audits/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.json`

## Purpose

Audit whether the existing MAO-OA-T6A hard-task contract is reconstructable
and suitable for a separately governed fresh direct-lane calibration, while
keeping the historical T6A live result explicitly `NOT_ACCEPTED` and keeping
task qualification distinct from live-result admission. This audit performs
no test, runner, or provider execution.

## Target / Source

The exact twelve-path corpus named by the paired GC-018 baseline
(`docs/baselines/CVF_GC018_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.md`).
All twelve are read-only inputs; none were modified by this audit. Full
per-source hashes, byte counts, and extracted facts are in the companion
machine ledger's `sourceLedger` array.

## Scope / Methodology

1. Captured `git rev-parse HEAD` (`af218333f1005e7aa51ba318a172cb9b1336df7b`,
   matching the operator-stated `executionBaseHead`) and confirmed a clean
   worktree before any file was created.
2. Ran the pre-implementation autorun gate from that base before authoring.
3. Read all twelve manifest paths in full and recomputed SHA-256 and byte
   count for each from current bytes; zero drift, zero unresolved.
4. Reconstructed the T6A task contract, parser, rubric, and defect rules
   directly from current source
   (`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts`)
   and its 22 focused tests, without executing either.
5. Inspected the current runner source
   (`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts`)
   for whether it persists the sanitized-candidate field the T6A reviewer's
   R5 finding identified as missing, without running it.
6. Compared the T6A candidate against the excluded MAO-LIVE-T1 prime-number
   task across the seven dimensions this work order's Acceptance Contract
   section C requires.
7. Selected exactly one of the three allowed terminal decisions and named
   every downstream blocker between qualification and the eventual G2-T2
   experiment.

## Findings / Position

### Finding 1 - the T6A task contract is fully reconstructable from current source

The fixed task prompt, strict JSON schema (`objective`, exactly-3
`dependencies`, exactly-3 `risks` each with non-empty `mitigation`,
exactly-3 `verification`, `rollback`, `stopCondition`), a markdown-fence-
tolerant parser, a three-part deterministic 100-point rubric (40 schema/
completeness, 30 fixed-constraint correctness, 30 risk/verification
specificity), four material-defect classes, and the
`releaseCandidate = score<=80 OR materialDefectFound` rule are all present,
pure-function, and network/credential/retry-free in current source. This is
independently confirmed by 22/22 passing focused Vitest cases covering every
row of the work order's original Focused Test Matrix plus the negation-
handling (F1) and empty-input (F2) edge cases, and was independently
re-executed and re-confirmed by the T7 critique (source row 12) against the
same current source.

### Finding 2 - the runner now persists the field the reviewer found missing

The T6A completion review's R3 finding rejected the historical live score
because the persisted evidence contained only a raw-response hash, not the
parsed candidate, making independent rescoring structurally impossible. R5
recorded that the runner was repaired to persist `sanitizedCandidate` in
future authorized executions. Reading current runner source
(line 292 of the runner script) confirms this repair is present now:
`sanitizedCandidate: parsedCandidate?.ok ? parsedCandidate.raw : null` is
written into the artifact alongside the raw-response hash, usage, latency,
call count, retry count, rubric, defects, and the reviewer-owned release
boolean. This is a static source-inspection finding, not an execution or a
new receipt: no test, runner, or provider call was made to produce it.

### Finding 3 - the historical live result remains rejected and is not recomputed here

The historical evidence artifact
(`docs/reviews/evidence/mao-oa-t6a-direct-candidate-calibration-2026-07-17.json`)
still records `sanitizedCandidate: null` and
`reviewerEvidenceDisposition: "NOT_RECOMPUTABLE_MISSING_SANITIZED_CANDIDATE"`.
The T6A completion review (R3-R5), the T6A work order's own Closure
Checklist and Acceptance Receipt Assertion Matrix, and the T7 final roadmap
closure and independent critique all preserve this rejection and
`T6B_NOT_RELEASED`. This audit does not rescale, infer, average, or
otherwise resurrect the reported 100/100 score, the zero-defect claim, or
the worker's `releaseCandidateAsWorkerEvidence` value under any framing.
Missing sanitized scorer input in the historical run is not repaired by
inference; it is repaired only by a future authorized call that exercises
the already-fixed runner.

### Finding 4 - the T6A candidate is structurally distinct from and harder than the excluded task

The full seven-dimension comparison is in the companion machine ledger's
`hardnessNoveltyComparison` object. In summary: the T6A candidate carries a
six-field nested-object JSON schema with two fixed-cardinality arrays,
a three-dimension deterministic rubric, an explicit risk/rollback/stop-
condition reasoning requirement the excluded task has no analog of, four
named material-defect classes, a concrete falsifiable release-threshold
hypothesis (score at or below 80, or one material defect), and a task type
(constrained release planning) that is semantically non-equivalent to the
excluded task's single deterministic primality judgment. Complexity alone
is not treated as proof of a low score or of value gain; this finding
establishes structural hardness and novelty distinctness from the excluded
duplicate only.

### Finding 5 - successful-parse evidence is ready; parse failure remains fail-closed

Static inspection of current runner source (no execution) confirms it emits
every field named in the work order's Acceptance Contract section D when
the provider response parses successfully: sanitized parsed candidate,
raw-response hash, provider/model metadata, usage, latency, call count,
retry count, score dimensions, material defects, and the reviewer-owned
release boolean. However, on parse failure the runner writes
`sanitizedCandidate: null` and retains only a raw-response hash, not
reconstructable response bytes. An independent reviewer therefore cannot
reproduce the `INVALID_JSON` finding from that receipt alone. A future
calibration packet must mark such an outcome non-admissible and fail closed,
unless a separately authorized evidence-shape repair preserves sanitized
failure input or an equivalent reconstructable diagnostic. This finding is
bounded to source-shape inspection; it does not authorize that repair or
claim a future call will succeed or produce any particular score.

## Risk / Corrective Action

| Risk | Evidence | Corrective action | Disposition |
|---|---|---|---|
| conflating task-contract readiness with the rejected historical score | T6A completion review R3-R5; T7 closure and critique all preserve the rejection | this audit's terminal decision explicitly excludes the historical score and cites Finding 3 separately from Findings 1/2/4/5 | RESOLVED |
| treating source presence as proof of composition or future success | prior ACEL-G2-T2 design return's own adversarial-rejection discipline (source row 1) | Finding 2 and the evidence-readiness section are scoped to "current source emits field X," never "a future call will succeed" | RESOLVED |
| treating parse-failure output as independently reproducible | current runner persists `sanitizedCandidate: null` on parse failure and keeps only `rawResponseHash` | qualify packet authoring conditionally; require the future packet to reject parse-failure evidence unless separately authorized source repair makes it reconstructable | RESOLVED_BY_FAIL_CLOSED_PACKET_REQUIREMENT |
| treating schema/rubric complexity as evidence of a low score or value gain | this work order's Acceptance Contract section C closing sentence | Finding 4 and the machine ledger's `explicitDisclaimer` field state this exclusion directly | RESOLVED |
| widening qualification into an implicit calibration authorization | this work order's Operator Checkpoint and Claim Boundary sections | Terminal Decision section below states qualification returns to the operator before any provider call, consistent with the governing baseline | RESOLVED |
| the still-open callable-seam blocker being silently treated as resolved by this qualification | frozen G2-T2 design predecessor (source rows 1-2), `compositionGraph` GAP edges | Downstream Blockers section below explicitly retains `NO_CALLABLE_T1_TO_MAO_CONSUMER` as unresolved and out of this qualification's scope | RESOLVED |

## Downstream Blockers

- **Candidate qualification -> fresh direct calibration:** conditionally
  resolved for packet authoring. A separately authorized Local GC-018
  baseline and work order are required before any call is dispatched, and
  that packet must reject a parse-failure outcome as non-admissible unless a
  separately authorized evidence-shape repair first makes it independently
  reconstructable.
- **Fresh direct calibration -> callable seam:** unchanged and unresolved.
  Per the frozen G2-T2 design corpus (source rows 1-2), no callable seam
  exists between the T1 `RouteAction`/`decideRouteAction` decision contract
  and either MAO call surface
  (`operational.worker.launcher.ts` or `live.provider.value.pilot.ts`).
  This qualification does not address, narrow, or resolve that gap.
- **Callable seam -> G2-T2 A/B experiment:** unchanged and unresolved.
  Full G2-T2 execution needs both a qualified candidate (this qualification)
  and the callable seam (not addressed here), plus a fresh
  operator-authorized experiment work order.

## Decision / Terminal Disposition

`QUALIFIED_FOR_FRESH_DIRECT_CALIBRATION_PACKET`

Basis: the task, prompt, parser, deterministic rubric, material-defect
rules, and successful-parse evidence path are reconstructable from current
source without execution (Findings 1, 2, 5); the candidate is
structurally distinct from and harder than the excluded duplicate task
(Finding 4); and the historical live result remains explicitly
`NOT_ACCEPTED` and is not resurrected, rescaled, or treated as evidence by
this decision (Finding 3). This decision permits only a later Local
GC-018/work order dispatch decision. It does not itself authorize a
provider call. Any later packet must fail closed on a non-reconstructable
parse-failure receipt unless separately authorized source repair precedes
the call. This decision does not satisfy the later direct-lane admission threshold of an
accepted score at or below 80/100 or an independently accepted material
defect, resolve the callable-seam blocker, or open G2-T2 execution.

## Claim Boundary

This audit records a read-only, source-backed candidate-qualification
decision for the ACEL-G2-T2-CANDIDATE-QUALIFICATION-T0 tranche only. It does
not accept, rescale, or infer the historical T6A 100/100 score, zero-defect
claim, or release-candidate boolean; does not release T6B; does not execute
any test, runner, or provider call; does not access any credential; does
not implement the callable seam; does not authorize or dispatch G2-T2; and
does not claim runtime, production, or public-sync readiness. Local
reviewer/closer independently decides acceptance of this qualification
result.
