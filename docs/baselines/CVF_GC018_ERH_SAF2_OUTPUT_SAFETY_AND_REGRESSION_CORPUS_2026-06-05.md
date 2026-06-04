# CVF GC-018 - ERH-SAF2 Output Safety And Regression Corpus

Memory class: FULL_RECORD

Status: AUTHORIZED_DISPATCH_PACKET

docType: gc018_baseline

Date: 2026-06-05

dispatchBaseHead: `faa96dbf`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize ERH-SAF2 as the bounded output-safety follow-up from ERH-SAF1.

SAF1 hardened the input screening path (DLP → SAF1 → legacy safety). SAF2
closes two remaining gaps:

1. **Output safety audit**: `output-validator.ts` already detects
   `UNSAFE_CONTENT` in AI provider responses, but fires no audit event when
   that specific issue is found — the audit only fires after retry budget
   exhaustion. SAF2 adds an `OUTPUT_SAFETY_TRIGGERED` audit event the first
   time `UNSAFE_CONTENT` is detected in an AI response, before retries.

2. **Governance-specific output patterns**: `UNSAFE_PATTERNS` in
   `output-validator.ts` cover code-injection / hacking signals. SAF2 adds
   governance-specific detection — AI output that echoes governance-bypass
   instructions (governance-disable acknowledgment, policy-override echo) to
   the caller, which would indicate a prompt-injection success.

3. **Safety regression corpus**: no bounded adversarial test file exists for
   the SAF1 input chain. SAF2 adds
   `safety-workflow-chain.regression.test.ts` — a documented corpus of
   adversarial prompt samples that must always block/strip/log correctly,
   serving as a regression guard for future pattern changes.

## Scope / Target / Owner Boundary

Target runtime surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/output-validator.ts`
  (add governance output patterns + export safety issue type)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  (add `OUTPUT_SAFETY_TRIGGERED` audit event on first UNSAFE_CONTENT detection)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety-workflow-chain.regression.test.ts`
  (new adversarial regression corpus)

Authorized outputs:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_SAF2_OUTPUT_SAFETY_AND_REGRESSION_CORPUS_FOR_CLAUDE_2026-06-05.md`
- `docs/reference/CVF_ERH_SAF2_OUTPUT_SAFETY_AND_REGRESSION_CORPUS_2026-06-05.md`
- `docs/reference/CVF_ERH_SAF2_OUTPUT_SAFETY_AND_REGRESSION_CORPUS_LEDGER_2026-06-05.md`
- `docs/reviews/CVF_ERH_SAF2_OUTPUT_SAFETY_AND_REGRESSION_CORPUS_COMPLETION_2026-06-05.md`
- bounded source/test/checker files named by the SAF2 work order.

Out of scope:

- ML classifier, embedding-based detection, provider prompt tuning;
- auth runtime, provider routing, rate limiter, durable audit storage;
- package manifest, lockfile changes;
- `policySnapshotId` persistence, Redis;
- public-sync, public push, hosted-readiness, production-readiness claims;
- SAF3 (drift checker) — separate authorization required.

Risk ceiling: R2 runtime output safety hardening. Escalate before any route
refactor, package change, provider behavior change, or claim boundary expansion.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-05: author SAF2 GC-018 and work order; scope = candidates 1+2 (output audit + regression corpus) | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |
| SAF1 completion review | `docs/reviews/CVF_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | ACCEPT — SAF2_READY verdict recorded |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |

## Decision / Baseline

Decision: authorize Claude to implement SAF2 under `WORKER_MUST_NOT_COMMIT`.

Baseline facts:

- SAF1 `CLOSED_PASS_BOUNDED` at `faa96dbf`; `SAF2_READY` recorded.
- `output-validator.ts` already has `UNSAFE_CONTENT` issue type and
  `UNSAFE_PATTERNS` (5 regex). Route already calls `validateOutput` and fires
  `OUTPUT_VALIDATION_EXHAUSTED` after retry budget exhaustion.
- Gap 1: no audit event fires at the *first* `UNSAFE_CONTENT` detection —
  only after all retries are exhausted.
- Gap 2: no governance-specific output patterns (e.g., AI echoing
  "governance disabled" to indicate injection success).
- Gap 3: no regression corpus for SAF1 input patterns.
- `output-validator.ts` is 235 lines (soft threshold 700, hard limit 1000) —
  adding bounded patterns is safe.
- `route.ts` is 850 lines (hard limit 1000) — adding one bounded audit event
  block is safe with care.

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `output-validator.ts` has UNSAFE_CONTENT issue type | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/output-validator.ts` | lines 21-28 | `ValidationIssue` union | output validator types | ACCEPT |
| `output-validator.ts` has UNSAFE_PATTERNS array | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/output-validator.ts` | lines 56-62 | `UNSAFE_PATTERNS` | output validator constants | ACCEPT |
| Route calls validateOutput after AI execution | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 742-776 | `validateOutput` | `/api/execute` POST route | ACCEPT |
| Route fires OUTPUT_VALIDATION_EXHAUSTED only after retry budget exhaustion | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 779-800 | `OUTPUT_VALIDATION_EXHAUSTED` | `/api/execute` audit event | ACCEPT |
| No OUTPUT_SAFETY_TRIGGERED audit event exists yet | EXISTS_NOT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | full file scan | `OUTPUT_SAFETY_TRIGGERED` absent | `/api/execute` audit events | ACCEPT |
| SAF1 helper exists and is server-safe | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety-workflow-chain.ts` | file source | `ERH_SAF1_MARKER` | SAF1 safety chain | ACCEPT |
| No regression corpus test file exists yet | EXISTS_NOT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/` | directory scan | `safety-workflow-chain.regression.test.ts` absent | SAF1 regression | ACCEPT |
| route.ts is 850 lines | LINE_COUNT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | full file | 850 lines; hard limit 1000 | GC-023 file size guard | ACCEPT |
| output-validator.ts is 235 lines | LINE_COUNT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/output-validator.ts` | full file | 235 lines; soft threshold 700 | GC-023 file size guard | ACCEPT |

## SAF2 Behavior Requirements

| Requirement | Required behavior |
| --- | --- |
| Deterministic only | regex/rule logic only; no ML/classifier/provider dependency |
| Output safety audit | `OUTPUT_SAFETY_TRIGGERED` audit event fires on first `UNSAFE_CONTENT` detection, before retries; payload includes issue list, no raw AI output text |
| Governance output patterns | detect AI output that echoes governance-disable/policy-override patterns (i.e., AI confirming it bypassed governance) |
| Regression corpus | bounded `.regression.test.ts`; each entry has documented adversarial prompt + expected SAF1 outcome; corpus is versioned and extensible |
| Claim boundary | SAF2 must not claim comprehensive output safety, ML DLP, or production security readiness |

## SAF3 Decision Rules

The SAF2 completion review must include a SAF3 decision with one of:

- `SAF3_READY`: clear source-visible drift/coverage gap remains after SAF2
- `SAF3_HOLD`: SAF2 evidence insufficient or scope unclear
- `SAF3_NOT_NEEDED`: SAF2 closes remaining actionable safety gaps within ERH scope

SAF3 implementation is forbidden in this work order.

## Evidence / Verification

Dispatch verification:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base faa96dbf --head HEAD --all-changed --enforce
python governance/compat/check_work_order_dispatch_quality.py --base faa96dbf --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base faa96dbf --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base faa96dbf --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base faa96dbf --head HEAD
```

Worker verification must use the Claude-captured execution base.

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason — this is a GC-018 dispatch baseline, not a corpus scan or inventory task
- Corpus root: N/A with reason
- Snapshot time: N/A with reason
- Enumeration command: `rg --files --hidden --no-ignore docs/baselines/CVF_GC018_ERH_SAF2_OUTPUT_SAFETY_AND_REGRESSION_CORPUS_2026-06-05.md` (single-file dispatch baseline; enumeration is the file itself)
- Manifest artifact or inline manifest: N/A with reason
- Manifest hash: N/A with reason
- Processing ledger artifact or inline ledger: N/A with reason
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=0; ledger_terminal=0; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: N/A with reason
- Drift check: N/A with reason
- Output traceability: N/A with reason
- Adversarial verification: N/A with reason
- Corpus verdict: COMPLETE_VERIFIED

This GC-018 authorizes a runtime safety tranche, not a corpus scan. No corpus
enumeration or completeness claim is made.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| UNSAFE_CONTENT in output fires no dedicated audit event | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | WORKFLOW_CHAIN_REQUIRED | SAF2 output safety audit event |
| Governance-specific patterns absent from output safety screen | ROUTE_COVERAGE_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_CANDIDATE | SAF2 governance output patterns |
| No adversarial regression corpus for SAF1 input chain | CORPUS_COMPLETENESS_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | SAF2 regression corpus |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ERH-SAF2 is private provenance runtime hardening and dispatch planning.

Next action: public-facing safety claim update requires a later public-sync work
order after SAF2 is reviewed and claim boundaries accepted.

## Claim Boundary

This GC-018 authorizes bounded output safety audit event, governance-specific
output pattern extension, and adversarial regression corpus only. It does not
claim ML DLP, comprehensive output safety coverage, production security
readiness, hosted readiness, public readiness, or complete remediation of the
external review safety weakness.
