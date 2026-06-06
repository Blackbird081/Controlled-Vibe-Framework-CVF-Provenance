# CVF ERH-SAF2 Output Safety And Regression Corpus Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-05

Worker: Claude

executionBaseHead: `9f3f0882`

dispatchPacketCommit: `bb4cbaa9`

closureBaseHead: `9f3f0882`

GC-018: `docs/baselines/CVF_GC018_ERH_SAF2_OUTPUT_SAFETY_AND_REGRESSION_CORPUS_2026-06-05.md`

Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_SAF2_OUTPUT_SAFETY_AND_REGRESSION_CORPUS_FOR_CLAUDE_2026-06-05.md`

## Purpose

Record the completion of ERH-SAF2: governance-specific output pattern
detection, `OUTPUT_SAFETY_TRIGGERED` audit event wiring before retry
exhaustion, and bounded adversarial regression corpus for the SAF1 input chain.

## Scope / Target / Owner Boundary

Target: `cvf-web` output-validator and `/api/execute` route module.

Implemented:

- `GOVERNANCE_OUTPUT_PATTERNS` (8 regex patterns) + `ERH_SAF2_MARKER` in
  `output-validator.ts`
- `isGovernanceOutputUnsafe` exported helper in `output-validator.ts`
- Governance check (section 4b) in `validateOutput` — fires `UNSAFE_CONTENT`
  for governance echo patterns
- `OUTPUT_SAFETY_TRIGGERED` first-detection helper in `route.ts`, called after
  initial validation and retry-loop validation
- `safety-workflow-chain.regression.test.ts` — 10 SAF1 input entries
  (CRITICAL × 5, HIGH × 3, MEDIUM × 2) + 4 SAF2 output governance entries
- `check_erh_output_safety_workflow_chain.py` — 9-check machine verifier
- `test_check_erh_output_safety_workflow_chain.py` — pattern unit tests +
  live integration test
- Hook chain and autorun gate updated with SAF2 checker
- GC-052 interlock registry updated
- Workflow-chain reference doc and ledger created
- ERH roadmap SAF2 row updated to `CLOSED_PASS_BOUNDED`

Not implemented:

- SAF3 (drift checker) — deferred; decision recorded below
- ML classifier, embedding-based detection
- Provider routing changes, auth edits, package manifest changes
- Public-sync, production security certification

## Decision / Baseline

Decision: `ACCEPT_BOUNDED`

Baseline: SAF1 completion records `SAF2_READY`. SAF2 candidates 1 and 2
(output safety audit event and regression corpus) are implemented within
Allowed scope. Machine checker enforces SAF2 wiring markers in source.

## Source / Predecessor Evidence

| Source | Purpose | Disposition |
| --- | --- | --- |
| `docs/reviews/CVF_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | SAF2_READY basis | ACCEPTED |
| `cvf-web/output-validator.ts` | governance pattern target | MODIFIED (patterns + marker) |
| `cvf-web/src/app/api/execute/route.ts` | audit event wiring target | MODIFIED (OUTPUT_SAFETY_TRIGGERED block) |
| `cvf-web/src/lib/safety-workflow-chain.ts` | regression corpus target | READ_ONLY |

## Findings / Position

| Item | Finding | Disposition |
| --- | --- | --- |
| `ERH_SAF2_MARKER` in output-validator.ts | present — `GOVERNANCE_OUTPUT_SAFETY_ACTIVE` | PASS |
| `GOVERNANCE_OUTPUT_PATTERNS` exported | 8 patterns added | PASS |
| `isGovernanceOutputUnsafe` exported | helper function added | PASS |
| Governance check in `validateOutput` (4b) | fires `UNSAFE_CONTENT` for governance patterns if not already flagged | PASS |
| `OUTPUT_SAFETY_TRIGGERED` in route.ts | added before retry exhaustion | PASS |
| Audit payload has no raw AI output | payload uses issues list + counts + provider/model | PASS |
| Timing: triggered before exhausted | `OUTPUT_SAFETY_TRIGGERED` position < `OUTPUT_VALIDATION_EXHAUSTED` in source | PASS |
| First-detection retry coverage | helper emits once and is called after initial and retry validations | PASS — reviewer correction |
| Regression corpus SAF1 entries | 10 entries (C-01..C-05, H-01..H-03, M-01..M-02) | PASS |
| Regression corpus SAF2 entries | 4 entries (OG-01..OG-04) | PASS |
| Machine checker | `check_erh_output_safety_workflow_chain.py` — 9 checks | PASS |
| Hook chain wiring | SAF2 checker added after SAF1 entry | PASS |
| Autorun gate wiring | SAF2 GateCommand added after SAF1 entry | PASS |
| GC-052 connection | `erh-saf2-output-safety-workflow-chain` added | PASS |
| Route line count | 850 -> 874 (hard limit 1000) | PASS |
| Output-validator line count | 235 → ~304 (advisory 700) | PASS |

## Evidence / Verification

| Check | Result |
| --- | --- |
| `git rev-parse --short HEAD` at start | `9f3f0882` |
| Worktree at start | clean |
| Pre-implementation autorun gate `--base faa96dbf --head HEAD` | PASS |
| Route line count before edit | 850 |
| output-validator.ts line count before edit | 235 |
| `ERH_SAF2_MARKER` present in source | VERIFIED |
| `OUTPUT_SAFETY_TRIGGERED` added before retry exhaustion | VERIFIED |
| Regression corpus ≥10 SAF1 entries | 10 entries VERIFIED |
| `npm run check` | PASS |
| `npx vitest run src/lib/safety-workflow-chain.regression.test.ts` | 18/18 PASS |
| `npx vitest run src/lib/output-validator.test.ts` | 32/32 PASS |
| `npm run build` | PASS |
| `check_erh_output_safety_workflow_chain.py --enforce` | PASS — 0 violations |
| `pytest test_check_erh_output_safety_workflow_chain.py -q` | 17/17 PASS |
| `check_markdown_structural_completeness.py --base 9f3f0882 --head HEAD --enforce` | PASS — 3 files checked, 0 violations |
| `check_system_loop_interlock.py --base 9f3f0882 --head HEAD --enforce` | PASS |
| `check_finding_to_governance_learning.py --base 9f3f0882 --head HEAD --enforce` | PASS |
| `check_public_export_disposition.py --base 9f3f0882 --head HEAD --enforce` | PASS |
| Route line count final | 874 (hard limit 1000) |
| output-validator.ts line count final | 262 (advisory 700) |
| `git diff --name-status 9f3f0882` shows only Allowed paths | VERIFIED — 6 modified, 6 new, all within Allowed scope |
| Pre-closure autorun gate | BLOCKED — uncommitted worktree (expected: WORKER_MUST_NOT_COMMIT) |

## Risk / Corrective Action

| Risk | Corrective action | Status |
| --- | --- | --- |
| Governance output patterns may produce false positives on legitimate content | by design — patterns are conservative and narrow (exact governance-bypass phrases); false-positive rate expected low; claim boundary explicit | ACCEPTED |
| Initial worker diff emitted `OUTPUT_SAFETY_TRIGGERED` only after the first validation call | reviewer correction added an emit-once helper and retry-loop call so first-detection semantics cover retry output too | REMEDIATED |
| `OUTPUT_SAFETY_TRIGGERED` may fire before a later retry clears UNSAFE_CONTENT | by design — first-detection semantics are intentional; the audit trail records detection independently of final retry outcome | ACCEPTED |
| Regex-only output screen does not detect novel obfuscated governance bypasses | by design — SAF2 is deterministic pattern-only; claim boundary states no comprehensive coverage or ML claim | ACCEPTED |
| Route line count increased from 850 to 874 (headroom to limit: 126) | within limit; no corrective action needed | ACCEPTED |
| Pre-closure autorun gate blocked by uncommitted worktree | expected under WORKER_MUST_NOT_COMMIT; Codex reviewer must commit and re-run pre-closure gate | DEFERRED_TO_REVIEWER |

## SAF3 Decision

**Verdict: `SAF3_NOT_NEEDED`**

Rationale:

- SAF2 closes both actionable output-safety gaps identified in the SAF1
  completion: output audit event and regression corpus.
- The third SAF1 candidate (safety coverage drift checker) is a speculative
  future improvement, not a currently source-visible gap with concrete evidence.
- Route size is 874 lines (limit 1000), leaving headroom, but a drift checker
  would require a new route coverage scanning approach that warrants a separate
  roadmap item rather than SAF3 continuation.
- SAF2 passes all required machine-checker gates.
- No new source-visible output-safety gaps were uncovered during SAF2
  implementation that would require immediate SAF3 remediation.
- SAF3 was always a decision checkpoint, not a pre-authorized tranche.

SAF3 may be opened in a future work order if a concrete source-visible coverage
gap is identified. This decision does not close the possibility permanently;
it records that no current evidence justifies SAF3 at this time.

## Reviewer Checklist

| Item | Expected result |
| --- | --- |
| `ERH_SAF2_MARKER` present in output-validator.ts | VERIFY |
| `GOVERNANCE_OUTPUT_PATTERNS` exported (8 entries) | VERIFY |
| `isGovernanceOutputUnsafe` exported | VERIFY |
| Section 4b governance check in `validateOutput` | VERIFY — no duplicate UNSAFE_CONTENT push |
| `OUTPUT_SAFETY_TRIGGERED` fires before retry exhaustion | VERIFY — position before `OUTPUT_VALIDATION_EXHAUSTED` |
| First-detection helper covers initial and retry validations | VERIFY |
| Audit payload contains no raw AI output text | VERIFY |
| Regression corpus ≥10 SAF1 entries, ≥2 SAF2 entries | VERIFY |
| No package.json or lockfile changes | VERIFY |
| No auth runtime, provider router, rate-limiter changes | VERIFY |
| `npm run check` PASS | VERIFY |
| Build PASS | VERIFY |
| Checker and checker tests PASS | VERIFY |
| SAF3 decision is exactly one verdict (`SAF3_NOT_NEEDED`) | VERIFY |
| Completion does not claim ML DLP or production security | VERIFY |

## Core Guard Self-Protection Authorization

Operator authorization: 2026-06-05 operator authorized SAF2 dispatch after
SAF1 completion and pre-dispatch PASS.

Authorized guard-maintenance scope: added one ERH-SAF2 output safety
workflow-chain checker, focused tests, hook/autorun wiring, GC-052 interlock
connection. Output-validator.ts and route.ts updated within Allowed scope only.

Protected paths updated:
- `governance/compat/check_erh_output_safety_workflow_chain.py`
- `governance/compat/test_check_erh_output_safety_workflow_chain.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Session-continuity files (`CVF_SESSION/ACTIVE_SESSION_STATE.json`,
`CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V15_2026-05-29.md`) are updated
by Codex reviewer only after review acceptance.

Rollback boundary: if a protected continuity edit is wrong, restore only the
SAF2/SAF3 continuity text. Runtime/source, guard semantics, public-sync,
auth runtime, and package changes are outside this dispatch sync.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_SAF2_OUTPUT_SAFETY_AND_REGRESSION_CORPUS_FOR_CLAUDE_2026-06-05.md` | SAF2 completion closes the dispatched work order with `CLOSED_PASS_BOUNDED` in this reviewer artifact | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_SAF2_OUTPUT_SAFETY_AND_REGRESSION_CORPUS_COMPLETION_2026-06-05.md` | `CLOSED_PASS_BOUNDED`; SAF3 verdict `SAF3_NOT_NEEDED`; reviewer remediation recorded | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | SAF2 row moved to `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `erh-saf2-output-safety-workflow-chain` connection added; GC-051 corpus registry not applicable to SAF2 regression-test corpus | BLOCKED with reason |
| Registry Markdown | `docs/reference/CVF_ERH_SAF2_OUTPUT_SAFETY_AND_REGRESSION_CORPUS_2026-06-05.md` | SAF2 workflow-chain reference and regression-corpus boundary recorded; no GC-051 markdown registry change required | BLOCKED with reason |
| External evidence digest | `N/A with reason` | no external corpus/source digest consumed; SAF2 uses repo-local source and tests only | N/A with reason |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `erh-saf2-output-safety-workflow-chain` route added and checker-backed | PASS |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | follow-up session sync commit required after reviewer commit | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| UNSAFE_CONTENT detection emitted no dedicated audit event until SAF2 | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_ADDED | SAF2 checker enforces OUTPUT_SAFETY_TRIGGERED presence and timing |
| Governance-bypass patterns absent from output safety screen until SAF2 | ROUTE_COVERAGE_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_ADDED | SAF2 checker enforces GOVERNANCE_OUTPUT_PATTERNS marker |
| No adversarial regression corpus for SAF1 input chain until SAF2 | CORPUS_COMPLETENESS_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | SAF2 checker enforces regression corpus file existence |
| SAF3 drift checker identified as speculative future improvement | SCOPE_BOUNDARY | GOVERNANCE_CONTROL_PLANE | SAF3_NOT_NEEDED_DEFERRED | open SAF3 only if concrete source-visible coverage gap found |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: SAF2 is private provenance runtime hardening. No public-sync work
is authorized in this work order.

## Claim Boundary

This completion records bounded governance-specific output pattern detection,
`OUTPUT_SAFETY_TRIGGERED` audit event wiring with first-detection timing
guarantee, and adversarial regression corpus with local test evidence.

It does not prove ML DLP, comprehensive output safety coverage, comprehensive
jailbreak protection, production security readiness, hosted readiness, public
readiness, complete external-review remediation, or release-quality/live-proven
governance behavior.
