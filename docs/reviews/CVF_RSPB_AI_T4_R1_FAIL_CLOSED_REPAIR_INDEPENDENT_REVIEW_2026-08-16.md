# CVF RSPB-AI-T4-R1 Fail-Closed Repair Independent Review

Memory class: governed-completion-review

Status: REVIEWER_ACCEPTED_PENDING_CLOSER

Date: 2026-08-16

## Purpose

Independent re-review of the bounded RSPB-AI-T4-R1 fail-closed repair, which
was implemented in response to the HIGH zero-threshold ambiguity bypass and
related findings recorded in
`docs/reviews/CVF_LOCAL_SYNTHESIS_FIRST_LEARNING_AND_RSPB_AI_T4_INDEPENDENT_REVIEW_2026-08-16.md`.
The reviewer authored none of the repair, made no file changes or commits,
and reproduced evidence independently rather than trusting worker-reported
results.

## Target / Source

Target is the exact five-path uncommitted RSPB-AI-T4-R1 repair at execution
base `e31fa6694f932fb727e296ed1cd8c76f9d5e9813`. Source authority is the prior
independent rejection, the repair evidence packet, the full worktree diff, and
repository-owned tests/checkers reproduced below.

## Scope / Methodology

Reviewed exactly five paths against starting committed HEAD
`e31fa6694f932fb727e296ed1cd8c76f9d5e9813`:

1. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts`
2. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.test.ts`
3. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/providers/alibaba-dashscope-provider.test.ts`
4. `docs/reviews/CVF_RSPB_AI_T4_CAPABILITY_ROUTE_AND_READINESS_EVIDENCE_KERNEL_COMPLETION_2026-08-16.md`
5. `docs/reviews/CVF_RSPB_AI_T4_R1_FAIL_CLOSED_REPAIR_EVIDENCE_2026-08-16.md`

Inspected the full kernel diff, the new test cases, the Alibaba live-test
opt-in change, and both review documents; independently reproduced every
required command; ran 14 original adversarial probes beyond the worker's own
test suite; and confirmed no provider/live call, file edit, or commit
occurred during review.

## Findings / Position

No HIGH, MEDIUM, or LOW defect was found in the repaired kernel, its tests,
the Alibaba live-test gate, or the two review documents. The repair
precisely addresses the prior HIGH defect and the MEDIUM/LOW findings with
no scope creep and no newly introduced fail-open path.

## Risk / Corrective Action

None required. The repair deliberately increases false-negative routing
posture (material authority now requires governed resolution instead of a
fast route), which is the correct direction for a fail-closed evidence
kernel.

## Decision / Disposition

`REVIEWER_ACCEPTED_PENDING_CLOSER`. Closer action remains a separate step;
this review does not commit or close RSPB-AI-T4-R1.

## Reviewer Independence

- Did not author the R1 repair, the kernel, its tests, the Alibaba test
  change, or either review document.
- Made no file changes, staging, commits, resets, or stashes. One temporary
  adversarial-probe file was written under the git-ignored
  `EXTENSIONS/CVF_GUARD_CONTRACT/node_modules/.cvf-review-probe-r1/` and
  deleted after use; it never touched tracked paths.
- Starting HEAD: `e31fa6694f932fb727e296ed1cd8c76f9d5e9813` (unchanged
  throughout; this review covers uncommitted worktree changes only).
- `git status --short`, identical before and after review:

```text
 M EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.test.ts
 M EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts
 M EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/providers/alibaba-dashscope-provider.test.ts
 M docs/reviews/CVF_RSPB_AI_T4_CAPABILITY_ROUTE_AND_READINESS_EVIDENCE_KERNEL_COMPLETION_2026-08-16.md
?? docs/reviews/CVF_RSPB_AI_T4_R1_FAIL_CLOSED_REPAIR_EVIDENCE_2026-08-16.md
```

- No provider or live call was made. Ambient `ALIBABA_API_KEY` was present
  in the review environment (confirmed as a boolean only; the value was
  never read or printed). This real ambient-key condition was used to
  verify the opt-in gate rather than a synthetic substitute, and the key
  was cleared only for the child-process full-suite run as instructed.
- No secret value, header, or request/response body was printed at any
  point in this review.

## Requirement-By-Requirement Confirmation

| # | Requirement | Result |
|---|---|---|
| 1 | `materialScoreDelta=0` cannot disable equal-score comparison | Confirmed. `capability-route-readiness.contract.ts:196` now uses `<=` in place of the prior `<`; `0.9 - 0.9 = 0 <= 0` is true, so the material comparison window is entered. Probe 1 reproduces the exact prior failure input and returns `AMBIGUOUS_ROUTE` with all six reasons. |
| 2 | Equal-score, six-dimension-divergent candidates escalate to `AMBIGUOUS_ROUTE` | Confirmed by probe 1 and by the worker's own new test at `capability-route-readiness.contract.test.ts:48-64`, independently reproduced. |
| 3 | Single candidate with R1-R3, credentials, network, mutation, irreversible, or public/human effects cannot `FAST_ROUTE` | Confirmed. `hasMaterialAuthorityFootprint` (lines 149-156) and the `requiresAuthorityReview` gate (lines 202, 206) force `FULL_RESOLUTION_REQUIRED`. Probes 2, 3, 4 each isolate a single dimension (R1 risk only; credentials only; mutation only) and all three independently escalate, which is stronger evidence than the worker's own test, which only exercises the all-dimensions-set case. |
| 4 | Such a candidate produces `MATERIAL_AUTHORITY_REVIEW_REQUIRED` and non-ready readiness evidence | Confirmed. Probes 2-4 show `issues: ['MATERIAL_AUTHORITY_REVIEW_REQUIRED']`; probe 2's readiness evaluates to `UNKNOWN` via the `route.stage !== 'FAST_ROUTE'` readiness check at line 328. |
| 5 | Malformed readiness arrays/identifiers fail closed as `UNKNOWN`, do not throw, sanitize evidence, and retain `executionAuthorized=false` | Confirmed. `validateReadinessInput` (lines 278-286) and `malformedReadinessResult` (lines 288-310) intercept before any array `.filter` call. Probes 8, 9, 10, 11 independently confirm: `null` `requiredDependencies` does not throw and returns `UNKNOWN`; an unsafe `readinessDecisionId` is sanitized to `'invalid'` and not echoed; unsafe `evidenceRefs` entries are filtered while valid ones are kept; an entirely `null` readiness input does not throw, returns `UNKNOWN`, and retains `executionAuthorized: false`. |
| 6 | Ordinary R0 single-candidate routing still works | Confirmed, no regression. Probe 5 (pure R0, zero footprint) returns `FAST_ROUTE`/`READY`. Probe 6 (two R0 candidates, wide score gap) returns `FAST_ROUTE`. |
| 7 | New fail-open paths, unsafe defaults, type errors, or misleading evidence | None found. The exact-threshold boundary (probe 7: score gap equals the default 0.1 threshold) and a small-but-outside-window R0-only pair (probe 12) both correctly land in `FULL_RESOLUTION_REQUIRED`, not a silent `FAST_ROUTE`. Frozen-object tamper resistance holds (probe 14). `npm run check` is clean with no type errors. |
| 8 | Alibaba live tests require both `CVF_ALIBABA_LIVE_TEST=true` and a valid key; ambient key alone must not activate live tests | Confirmed by direct reproduction. With the real ambient `ALIBABA_API_KEY` present and `CVF_ALIBABA_LIVE_TEST` unset, `npx vitest run ... alibaba-dashscope-provider.test.ts` produced 5 passed, 3 skipped, zero provider calls. Line 19 of the diff reads `LIVE = process.env.CVF_ALIBABA_LIVE_TEST === 'true' && API_KEY !== 'PLACEHOLDER_KEY'`, requiring both sides. This matches the sibling `gemini-provider.test.ts` idiom (`LIVE = process.env.CVF_GEMINI_LIVE_TEST === 'true'`), so the fix aligns with existing repository convention rather than inventing a new one. |
| 9 | Disclosed two-call incident is not used as T4 evidence or repeat-live authority | Confirmed. The R1 repair-evidence document labels it `INCIDENT_ONLY_NOT_T4_EVIDENCE` and states no repeat-live authority is granted (lines 80-81); the completion document repeats this at lines 17-22. Test-file inspection independently corroborates the call count: `alibaba-dashscope-provider.test.ts` has exactly two `it()` blocks calling `provider.execute` directly (lines 67-76 and 77-85), and a third governed E2E test (line 87) that the disclosure states returned `BLOCKED` before reaching `provider.execute`, consistent with the guard-blocking pattern shown for the same provider at lines 47-59. No secret was echoed by this disclosure. |
| 10 | Prior self-closure status was truthfully replaced by pending independent re-review | Confirmed. The completion document's line 7 reads `Status: REPAIR_IMPLEMENTED_PENDING_INDEPENDENT_REREVIEW`; line 13 states prior closure at `b571cd4b3` is not ratified; the Acceptance Receipt Assertion Matrix (lines 234-236) uses `PASS_PENDING_REREVIEW` rather than plain `PASS` for the three repaired assertions, an honest label that does not overclaim the prior rejection into a closure. |

## Independently Reproduced Commands

| Command | Result |
|---|---|
| `npx vitest run --pool forks src/contracts/capability-route-readiness.contract.test.ts` | 19/19 passed |
| `npx vitest run --pool forks <kernel> src/index.test.ts src/package.boundary.test.ts src/boundary.signals.test.ts` | 65/65 passed (4 files: 19+34+7+5) |
| `npm run check` (`tsc --noEmit`) | PASS, clean exit |
| Alibaba provider test, ambient key present, `CVF_ALIBABA_LIVE_TEST` unset | 5 passed, 3 skipped, zero provider calls |
| Full suite (`npm test`) with all four Alibaba env vars cleared in-process | 597 passed, 5 skipped, 39 test files, exit 0 |
| mixed-origin checker, working-tree-aware current-base invocation | COMPLIANT, 1 artifact checked, 0 violations |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --parallel` | 64/64 PASS |
| `git diff --check` | Clean (CRLF advisories only) |
| `git status --short` | 5 paths, matches the declared batch |
| 14 independent adversarial probes (git-ignored temp dir, removed after use) | All 14 confirm correct fail-closed behavior; no fail-open path found |

All worker-reported numbers (19/19, 65/65, 597/597 with 5 skipped,
TypeScript PASS, reviewer-fast 64/64) matched independent reproduction
exactly.

## Additional Verification Beyond The Worker's Own Evidence

- Re-checked the two artifacts flagged in the prior review round as newly
  non-compliant under the amended mixed-origin checker (the T3 and T4
  completion documents going from 0 to 6 violations). The T4 completion
  document now carries all six efficiency controls
  (`docs/reviews/CVF_RSPB_AI_T4_CAPABILITY_ROUTE_AND_READINESS_EVIDENCE_KERNEL_COMPLETION_2026-08-16.md:105-115`)
  and passes with 0 violations; that regression is resolved for this file.
- Isolated each of the six material-authority dimensions individually
  (credentials-only, mutation-only, R1-only) rather than relying on the
  worker's single all-dimensions-set test case, to rule out a narrower
  implementation that only catches the combined case.

## Adversarial Probe Log

| Probe | Scenario | Observed result |
|---|---|---|
| 1 | Original HIGH repro: `materialScoreDelta: 0`, identical score, R0 vs R3 all six dimensions differ | `AMBIGUOUS_ROUTE`, all six reasons, `MATERIAL_AUTHORITY_AMBIGUITY` issue |
| 2 | Single R1-risk candidate, no other footprint | `FULL_RESOLUTION_REQUIRED`, `MATERIAL_AUTHORITY_REVIEW_REQUIRED`, readiness `UNKNOWN` |
| 3 | Single candidate, credentials-only footprint | `FULL_RESOLUTION_REQUIRED`, `MATERIAL_AUTHORITY_REVIEW_REQUIRED` |
| 4 | Single candidate, mutation-only footprint | `FULL_RESOLUTION_REQUIRED`, `MATERIAL_AUTHORITY_REVIEW_REQUIRED` |
| 5 | Pure R0 single candidate, zero footprint | `FAST_ROUTE`, `READY` (no regression) |
| 6 | Two R0 candidates, wide score gap, no footprint | `FAST_ROUTE` (no regression) |
| 7 | Score gap exactly equal to default threshold (0.1) | `FULL_RESOLUTION_REQUIRED`, not ambiguous, not a silent fast route |
| 8 | Malformed readiness: `requiredDependencies: null` | No throw, `UNKNOWN` |
| 9 | Unsafe `readinessDecisionId` with path traversal and NUL byte | Sanitized to `'invalid'`, not echoed, `UNKNOWN`, `executionAuthorized: false` |
| 10 | Unsafe `evidenceRefs` entries mixed with a valid one | Unsafe entries filtered, valid entry retained |
| 11 | Entirely `null` readiness input | No throw, `UNKNOWN`, `executionAuthorized: false` |
| 12 | Two R0 candidates within the material score window, zero footprint | `FULL_RESOLUTION_REQUIRED`, no ambiguity reasons (correct: window entered but no authority divergence) |
| 13 | Single high-risk candidate, high score | Confidence correctly clamped to 0.79 under `FULL_RESOLUTION_REQUIRED` |
| 14 | Attempted mutation of a frozen route decision | Throws under strict mode; object remains frozen and unchanged |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/run_local_governance_hook_chain.py` (`reviewer-fast` hook set) |
| literalTokensReviewed | mixed-origin efficiency control keys; six material-authority dimension reason codes; readiness state literals; `executionAuthorized: false` |
| gateRunPurpose | independently reproduce repair evidence and confirm no drift reintroduced against the mixed-origin checker |
| claimBoundary | review evidence only; no repair, commit, runtime, provider/live, public sync, deploy, or production authority |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| none found in this re-review | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | N/A_WITH_REASON | repair verified correct; no new control action required |

runtimeProviderCostLearningLane: N/A_WITH_REASON - no provider or live call
occurred during this review; the ambient key present in the environment was
never used to make a request.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the repair should eliminate both reproduced
optimistic-routing defects (zero-threshold bypass and single-candidate
absolute-risk fast routing) without introducing a new fail-open path.

Evidence Comparison: prediction held. All 14 independently authored
adversarial probes, including three that isolate individual authority
dimensions the worker's own test suite did not test separately, confirm
correct fail-closed behavior with no regression to ordinary R0 routing.

Contradiction Or Gap Disposition: none found.

Claim Update: RSPB-AI-T4-R1 repair is independently verified correct and
accepted pending closer action; prior closure at `b571cd4b3` remains
unratified until a closer acts on this acceptance.

## Verdict

`REVIEWER_ACCEPTED_PENDING_CLOSER`

## Claim Boundary

This review authorizes nothing beyond its own findings. It does not commit,
stage, revert, or modify any file; the worktree remains exactly as found at
HEAD `e31fa6694f9`. It does not close RSPB-AI-T4-R1; that is a closer
action. It does not authorize any router, transport, executor, acquisition,
mutation, credential access, provider/live call, network fetch, MCP/CLI
activation, public sync, deployment, or production readiness. It does not
certify runtime behavior beyond the hermetic Vitest/TypeScript evidence
reproduced above. It does not grant repeat-live authority for the disclosed
two-call incident, which remains incident-only evidence and not T4 proof.
