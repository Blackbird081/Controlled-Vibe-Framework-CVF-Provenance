# CVF Local-Synthesis-First Learning And RSPB-AI-T4 Independent Review

Memory class: governed-completion-review

Status: TARGET_A_REVIEWER_ACCEPTED_PENDING_CLOSER_TARGET_B_REVIEW_REJECTED_REPAIR_REQUIRED

Date: 2026-08-16

## Purpose

Independent reviewer pass, bounded to two targets: (A) the uncommitted
local-synthesis-first absorption learning batch (five paths), and (B) a
retrospective independent review of RSPB-AI-T4 (`844919a6c..b571cd4b3`),
whose completion evidence self-declared acceptance without a distinct
reviewer. The reviewer authored neither target, made no file changes or
commits, and reproduced evidence independently rather than trusting worker-
reported results.

## Scope / Methodology

Review Target A's bounded local-synthesis-first governance batch and Target B's
committed T4 range independently. Inspect full diffs, source, tests, exports,
authority boundaries, negative cases, and commit choreography; reproduce the
repository-owned focused checks without editing either target.

## Findings / Position

Target A is semantically accepted with two non-blocking drift notes. Target B
is rejected because adversarial probes expose one HIGH fail-open routing case
and related untested high-risk input behavior. Detailed evidence remains in the
two target sections below.

## Risk / Corrective Action

Target A may proceed to closer commit after structural gate hygiene. Target B
must remain unratified until a bounded repair addresses the zero-threshold
ambiguity defect, absolute single-candidate risk, tests, and truthful completion
evidence, followed by another independent review.

## Decision / Disposition

TARGET_A_REVIEWER_ACCEPTED_PENDING_CLOSER; TARGET_B_REVIEW_REJECTED_REPAIR_REQUIRED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | mixed-origin control keys; review structural headings; checker read-ahead fields; encoding boundary; exact split verdicts |
| gateRunPurpose | independently reproduce bounded target evidence and prepare a machine-readable reviewer return without converting Target B rejection into closure |
| claimBoundary | review evidence only; no repair, commit, runtime, provider/live, public sync, deploy, or production authority |

## Reviewer Independence

- Starting HEAD: `c8bbd24d706146ce9fe19ed53c2cf5eda7f97af0`.
- Observed `git status --short` identical before and after review:
  five paths (four modified, one untracked) matching the intended learning
  batch; no other drift.
- No file changes, staging, commits, resets, or stashes were performed by
  the reviewer. One temporary adversarial-probe harness was written under
  the git-ignored `EXTENSIONS/CVF_GUARD_CONTRACT/node_modules/.cvf-review-probe/`
  and deleted after use; it never touched tracked paths.
- No provider, live API, network acquisition, credential, MCP, deployment,
  or public-sync action was invoked.

## Target A - Local-Synthesis-First Priority Learning

Reviewed paths:

1. `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
2. `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md`
3. `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`
4. `governance/compat/test_check_mixed_origin_derived_synthesis_absorption.py`
5. `docs/reviews/CVF_LOCAL_SYNTHESIS_FIRST_PRIORITY_LEARNING_2026-08-16.md`

### Verdict

`REVIEWER_ACCEPTED_PENDING_CLOSER`

### Semantic requirements confirmed

| Required confirmation | Evidence |
|---|---|
| Local packs are first semantic input, justified by prior co-design | Standard lines 120-124: "already contains an informed CVF adaptation hypothesis" |
| Priority grants no authority/correctness/runtime/import right | `authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED` retained; standard Claim Boundary; learning record lines 36-39 |
| Content/examples/use-cases required; name/dir/ext/generated-appearance/pattern-count cannot alone justify REJECT/DEFER/NO_NEW_VALUE | Standard lines 138-141 |
| Cluster review reduces latency without hiding file-level value or traceability | Standard lines 142-145 |
| High-fit clusters route directly to a bounded work order | `mappingAction: DIRECT_WORK_ORDER_FOR_HIGH_FIT_CLUSTERS`; standard lines 147-149 |
| Required sequence WO -> no-commit worker -> distinct reviewer + test rerun -> closer | `deliverySequence: WORK_ORDER_THEN_WORKER_THEN_INDEPENDENT_REVIEWER`; standard lines 149-153 |
| Worker machine checks cannot substitute for independent review | Standard lines 152-154 |
| Upstream inspection targeted, not a prove-from-zero gate | `upstreamConsultation: TARGETED_FOR_PROVENANCE_OR_GAP`; standard lines 156-159 |

The learning record does not exempt itself: lines 53-54 state its own
worker-run checks "do not satisfy the independent reviewer requirement."
Status is `IMPLEMENTED_PENDING_INDEPENDENT_REVIEW`, not a self-closure.

### Checker and negative tests

Enforcement is real, not token-only. `check_mixed_origin_derived_synthesis_absorption.py`
lines 196-203 iterate every key in `EFFICIENCY_CONTROLS` and emit
`..._control_missing` when absent and `..._control_invalid` when the value
is outside the allowed set. The six new keys (lines 58-63) each have a
single-member allowed set, so any substitution fails. The five negative
tests each assert the specific `mixed_origin_efficiency_control_invalid`
type, and the guard regex is anchored so a prose mention cannot satisfy it.
No loophole, contradictory wording, or overly broad enforcement was found
in the six controls themselves.

### Findings

**Medium - latent enforcement drift on two sibling artifacts (not a
blocker for this batch; flag to closer).** Adding six required keys
retroactively invalidates existing marker-bearing artifacts. The checker
is forward-only (`run_check` inspects only changed paths), so nothing
fails today, but the violation is armed. Old-checker vs new-checker
comparison on unchanged content:

| Path | Old checker | New checker |
|---|---|---|
| `docs/reviews/CVF_RSPB_AI_T3_CONTROLLED_ACQUISITION_CONTRACT_KERNEL_COMPLETION_2026-08-16.md` | 0 violations | 6 violations |
| `docs/reviews/CVF_RSPB_AI_T4_CAPABILITY_ROUTE_AND_READINESS_EVIDENCE_KERNEL_COMPLETION_2026-08-16.md` | 0 violations | 6 violations |

These two are clean regressions caused by this batch; any future edit to
either file will fail the gate until the six controls are added. Five
further artifacts (assessments, baseline, work order, preflight contract)
report 1 violation each under both old and new checkers, so that is
pre-existing drift, not caused by this batch.

**Low - the standard's own `## Absorption Efficiency And Provenance Reuse`
section carries the six controls only inside a fenced ```text block**
(standard lines 126-133). `_section()` does no fence-stripping, so the
regex matches the fenced lines and the standard self-validates today, but
a future reformat of that fence would silently break self-compliance.

### Independently reproduced commands

| Command | Result |
|---|---|
| `python -m unittest governance.compat.test_check_mixed_origin_derived_synthesis_absorption -v` | OK, 16/16 passed, including all five new negative tests |
| mixed-origin checker, working-tree-aware current-base invocation | COMPLIANT, 1 artifact checked, 0 violations, exit 0 |
| core self-protection checker, working-tree-aware current-base invocation | COMPLIANT, exactly 2 protected files changed, authorized by the learning record, 0 violations, exit 0 |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --parallel` | All passed, 64/64, exit 0 |
| `git diff --check` | Clean, exit 0 (CRLF advisory warnings only) |
| `git status --short` | 5 paths as declared; manifest delta zero |

The worker's reported evidence matched independent reproduction in every
case.

## Target B - Retrospective Independent Review Of RSPB-AI-T4

Commit range: `844919a6c..b571cd4b3`.
Primary implementation: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts`.
Completion evidence under review: `docs/reviews/CVF_RSPB_AI_T4_CAPABILITY_ROUTE_AND_READINESS_EVIDENCE_KERNEL_COMPLETION_2026-08-16.md`.

### Verdict

`REVIEW_REJECTED_REPAIR_REQUIRED`

### Findings

**HIGH - `materialScoreDelta: 0` silently disables all material-authority
ambiguity detection, yielding FAST_ROUTE + READY for a maximally dangerous
candidate.** `capability-route-readiness.contract.ts` line 182 accepts
`threshold === 0` as valid (only `threshold < 0` is rejected). Line 187
gates ambiguity on `primary.score - second.score < threshold`; with
`threshold = 0` and two candidates of identical score, `0 < 0` is false, so
`materialAuthorityDifferences` is never invoked.

Reproduced failure scenario: two candidates both scoring 0.9, differing on
every one of the six material authority dimensions
(`a`: R0, no creds, no network, no mutation, reversible, non-public vs.
`b`: R3, `['prod-secret']`, `['evil.example']`, `['DELETE']`, irreversible,
public), evaluated with `{ now: NOW, materialScoreDelta: 0 }`:

- `stage = FAST_ROUTE` (expected `AMBIGUOUS_ROUTE`)
- `ambiguityReasons = []` (expected 6 reasons)
- `confidence = 0.9` (not clamped to 0.79)
- `issues = []` (no `MATERIAL_AUTHORITY_AMBIGUITY` issue)
- readiness = `READY`, `nextSafeAction` = "Bind the selected capability to
  SPEC and WORK ORDER before execution."

This directly contradicts the completion review's Acceptance Receipt
Assertion Matrix row "material ambiguity | authority-dimension differences
escalate | six dimensions tested | PASS" and Findings item 2 ("route
confidence can no longer silently override differences in risk,
credentials, network, mutation, irreversible effects, or public/human
effects"). Under `materialScoreDelta: 0` it silently does exactly that.

The deterministic tie-break compounds this: with `capabilityId` `'zzz'`
{R0} vs `'aaa'` {R3, irreversible}, `localeCompare` selects `'aaa'` - the
higher-risk candidate - as primary, with `FAST_ROUTE`/`READY` and no
ambiguity flag. The tie-break is deterministic as required but is not
risk-aware, and with the threshold disabled nothing else catches it. `0`
is the value a caller naturally passes to mean "no tolerance"; it should
escalate everything or be rejected, not silently pick the least-safe
result. No existing test exercises a non-default `materialScoreDelta`.

**MEDIUM - missing adversarial case: a single candidate never receives
ambiguity or risk scrutiny.** Ambiguity requires both `primary` and
`second` (line 187). A lone candidate with `riskLevel: 'R3'`,
`irreversibleEffects: true`, `publicOrHumanEffects: true`,
`mutationKinds: ['DROP_DB']`, `credentialScopeRefs: ['root']`, and no
dependencies/conflicts returns `FAST_ROUTE`, `confidence: 0.9`,
`issues: []`, then `READY`. Reproduced; no test covers a single high-risk
candidate.

**MEDIUM - completion evidence claims a delivery sequence that did not
occur.** The completion review records `Actor | reviewer/closer
implementing direct operator authorization` (line 118), `Agent type |
reviewer/closer` (line 130), self-declares `Status:
REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED` (line 7), and states under Machine
Closure Package "no standalone work order under single-pass learning"
(line 320). No `RSPB_AI_T4` work order exists in `docs/work_orders/` (only
T0, T1, T2), and `b571cd4b3` was committed by the same actor in one pass
21 minutes after the T3 sync. T4 was implemented and accepted by one agent
with no distinct independent reviewer - the exact `ORCHESTRATOR_PACKET_GAP`
Target A's learning record names as a defect. This review is T4's first
independent inspection, and it found a HIGH defect, which itself supports
Target A's new control.

**LOW - T4's completion review will now fail the Target A checker** (0 to
6 violations, see Target A findings above). Any repair edit to this file
must also add the six controls.

**LOW - unvalidated readiness inputs.** `evaluateCapabilityReadiness`
validates none of its input identifiers, unlike the route path.
`readinessDecisionId` containing an embedded NUL passes through
verbatim into the frozen result with `state: READY` (reproduced), and
`evidenceRefs` echoes script-like and embedded-NUL values unfiltered. A `null`
`requiredDependencies` throws `TypeError` at line 263 rather than failing
closed. Contained today because outputs are evidence-only, but it is an
inconsistent boundary versus `validateCandidateSet`.

### Confirmed-correct behaviors

- Two-stage selection: `FAST_ROUTE` only for clear low-impact cases;
  dependencies/conflicts force `FULL_RESOLUTION_REQUIRED` (lines 190-195).
- Fail-closed readiness precedence: the ordered `checks` array (lines
  264-278) places integrity/provenance/policy ahead of approval and
  dependency optimism. Verified: `integrityVerified:false` plus empty
  deps plus `approvalRequired:true` yields `BLOCKED_INTEGRITY`, not
  `BOOTSTRAP_REQUIRED`.
- Evidence/candidate-only: every route carries `authorityStatus:
  'CANDIDATE_ONLY'`, every readiness `'EVIDENCE_ONLY'`, both with literal
  `executionAuthorized: false` typed as `false`. Results are
  `Object.freeze`d; strict-mode assignment throws and the value stays
  `false`.
- Malformed/invalid input fails closed: `null` candidate set gives
  `NO_CANDIDATE` plus `MALFORMED_INPUT`; invalid `now` gives
  `NO_CANDIDATE` with `generatedAt` sentinel `1970-01-01T00:00:00Z`;
  `NaN`/out-of-range score gives `INVALID_FIELD`; future `generatedAt` is
  rejected.
- Rationale/rejection/fallback visibility: rejected entries carry
  ambiguity reasons for the runner-up and `LOWER_DETERMINISTIC_SCORE`
  otherwise; fallbacks carry
  `PRIMARY_UNAVAILABLE_AND_AUTHORITY_ENVELOPE_REVALIDATED`.
- No activation: the kernel imports only `node:util/types`. A
  repository-wide search found references solely in the contract, its
  test, and the two barrels; no router, transport, executor, acquisition,
  mutation, credential, provider, or deployment path is touched. Exports
  in `contracts/index.ts` and `src/index.ts` are type/function-only.

### Independently reproduced commands

Repository-owned scripts from `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`
(`test`: `vitest run --pool forks`, `check`: `tsc --noEmit`):

| Command | Result |
|---|---|
| `npx vitest run --pool forks src/contracts/capability-route-readiness.contract.test.ts` | 16/16 passed |
| `npm run check` (`tsc --noEmit`) | PASS, exit 0 |
| `npx vitest run --pool forks <kernel> src/index.test.ts src/package.boundary.test.ts src/boundary.signals.test.ts` | 62/62 passed (16+34+7+5); reproduces the "50/50 kernel-plus-export" claim as a subset |
| Adversarial probes (20 cases, git-ignored temp dir, removed after use) | Surfaced the HIGH and MEDIUM findings above |

The worker's numeric claims (16/16, 50/50, TypeScript PASS) are accurate.
The defects lie in cases the suite never exercises.

### Required repair

1. Reject `materialScoreDelta === 0`, or change the comparison to `<=`, or
   unconditionally compute `materialAuthorityDifferences` when a second
   candidate exists regardless of threshold. Add a negative test pinning
   `materialScoreDelta: 0` with identical scores and divergent authority
   dimensions.
2. Add a single-candidate high-risk test and decide whether absolute risk
   should gate `FAST_ROUTE` independently of comparison.
3. Correct the completion evidence: either route T4 through the
   now-required work-order -> worker -> independent-reviewer sequence, or
   amend the Actor/Status rows to state accurately that no distinct
   reviewer acted, and add the six efficiency controls so the file passes
   the amended checker.

The reviewer did not repair T4.

## Claim Boundary

This review authorizes nothing beyond its own findings. It does not commit,
stage, revert, or modify any file; both targets remain exactly as found at
HEAD `c8bbd24d7`. It does not close either target: Target A is accepted
pending closer action, and Target B is rejected pending repair, so its
existing self-declared `REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED` status is
not ratified. It does not authorize any router, transport, executor,
acquisition, installer, mutation, credential access, provider/live call,
network fetch, MCP/CLI activation, public sync, deployment, or production
readiness. It does not certify runtime behavior, cross-runtime determinism,
or trusted-evidence readiness; Target B evidence is hermetic local Vitest
and TypeScript only. It does not establish corpus completeness; the
latent-drift sweep covered nine marker-bearing artifacts under `docs/` and
is not a corpus-completeness claim. It does not grant authority to any
local synthesized pack, and does not convert Target A's priority rule into
correctness, import permission, or runtime readiness.
