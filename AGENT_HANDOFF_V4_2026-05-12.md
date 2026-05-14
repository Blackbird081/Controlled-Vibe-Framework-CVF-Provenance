<!-- Memory class: SUMMARY_RECORD -->
# CVF Agent Handoff V4 - QBS R10 Pre-Registration Continuation

**Date:** 2026-05-12
**Status:** ACTIVE CONTINUATION HANDOFF
**Supersedes for new updates:** `AGENT_HANDOFF_V3_2026-05-10.md`
**Reason:** V3 reached the governed markdown size ceiling after QBS-33 through
QBS-40 continuation updates.

## Repository Boundary

This workspace is the private provenance/archive repository:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git`

Public-facing CVF changes belong only in the sibling public-sync clone:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Before any public push, run `git remote -v` and confirm `origin` is:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Do not push public artifacts from this provenance workspace. The provenance
workspace currently has its push URL intentionally disabled:

`DISABLED_PROVENANCE_ARCHIVE_DO_NOT_PUSH_FROM_THIS_WORKSPACE`

## Current QBS State

Latest public commit:

`11c2828 Preregister QBS R10 checkpoint`

Latest public pre-registration tag:

`qbs/preregister/qbs1-powered-single-provider-20260512-alibaba-r10`

Tag SHA:

`11c2828155eb58f65ee89b68a9b02e904dcf7a5a`

Current public status:

`QBS40_R10_PREREGISTERED_NO_SCORED_RUN`

No QBS score, L4/L5 claim, family-level claim, provider-parity claim, or
human-gold claim is made.

## QBS-33 Through QBS-40 Continuation Summary

The locked QBS rerun remediation decision is recorded in:

`docs/reviews/CVF_QBS_RERUN_REMEDIATION_PROPOSAL_2026-05-11.md`

That proposal and the user decisions in it are binding for the QBS-33 onward
sequence. Do not request another Claude review before continuing QBS unless
the user explicitly reopens the decision.

Closed public commits:

- QBS-33: `b32295b Add QBS33 rework decoupling support`
- QBS-34: `bf944e0 Add QBS34 reviewer completeness retry`
- QBS-35: `1089530 Add QBS35 live run preflight`
- QBS-36: `df0c66c Publish QBS36 triangulated calibration reference`
- QBS-37: `034324a Publish QBS37 family diagnostic calibration`
- QBS-38: `791b07e Add QBS38 governance family metadata`
- QBS-39: `188e6fd Add QBS39 family allow output contracts`
- QBS-40: `11c2828 Preregister QBS R10 checkpoint`

### QBS-33

Status: `QBS33_REWORK_DECOUPLING_READY_NO_NEW_SCORE`

Calibration-only scripts support reviewer vs derived rework. Scored-run
reviewer artifacts record both `reviewer_rework` and `derived_rework`, while
the claim gate remains reviewer-rework-based for R6-R10 comparability.

### QBS-34

Status: `QBS34_REVIEWER_COMPLETENESS_RETRY_READY_NO_NEW_SCORE`

Reviewer scoring now performs bounded missing-alias retry and can emit
redacted completeness diagnostics. Raw full outputs are not dumped by default.

### QBS-35

Status: `QBS35_LIVE_RUN_PREFLIGHT_READY_NO_NEW_SCORE`

Live/reviewer/adjudicator scripts now share deterministic env/key/workspace
preflight. Preflight prints only `PRESENT`/`MISSING`, never raw key values, and
fails if an explicit env file resolves inside public-sync.

### QBS-36

Statuses:

- `QBS36_AVAILABLE_PROVIDER_TRIANGULATION_COMPLETE_NO_NEW_SCORE`
- `QBS36_R9_TRIANGULATED_CALIBRATION_REFERENCE_READY_NO_NEW_SCORE`

QBS-36 rebuilt the R9 calibration reference using model-only available-provider
triangulation across:

- Alibaba/DashScope `qwen3-max`
- OpenAI `gpt-4o`
- DeepSeek `deepseek-reasoner`

Results: 35 anchors adjudicated, 3 votes per anchor, 0 `requires_review`
exclusions, rebuilt reference count 35. Boundary: model-only adjudication, not
human gold.

### QBS-37

Status: `QBS37_R9_POST_TRIANGULATION_FAMILY_DIAGNOSTIC_COMPLETE_NO_NEW_SCORE`

Post-triangulation calibration-only reviewer check passed aggregate gates:

- weighted kappa: `0.72`
- Spearman rho: `0.7831388456799362`
- paired anchor count: `35`
- OpenAI vs reference: PASS
- DeepSeek vs reference: PASS

Per-family metrics are diagnostic-only. Lowest family diagnostics remained in
negative controls, cost/quota provider selection, and builder-handoff technical
planning.

### QBS-38

Status: `QBS38_RUNTIME_GOVERNANCE_FAMILY_MAPPER_READY_NO_NEW_SCORE`

Added bounded governance-family metadata for QBS corpus tasks and trusted
templates in the three chronic-negative families:

- `normal_productivity_app_planning`
- `builder_handoff_technical_planning`
- `cost_quota_provider_selection`

Family metadata is not a hard-gate override, reviewer label, score,
provider-routing directive, or claim-ladder shortcut.

### QBS-39

Status: `QBS39_FAMILY_CONDITIONAL_ALLOW_OUTPUT_CONTRACT_READY_NO_NEW_SCORE`

Added a `Family Output Contract` prompt section for the three chronic-negative
families. The contract applies only if CVF allows generation and does not
override BLOCK, CLARIFY, or NEEDS_APPROVAL decisions.

### QBS-40

Status: `QBS40_R10_PREREGISTERED_NO_SCORED_RUN`

Public artifacts/code changed:

- `docs/benchmark/qbs-1/qbs40-r10-checkpoint-and-preregistration.md`
- `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260512-alibaba-r10.md`
- `docs/benchmark/qbs-1/provider-model-manifest.qbs1-powered-single-provider-20260512-alibaba-r10.json`
- `docs/benchmark/qbs-1/config-prompt-manifest.qbs1-powered-single-provider-20260512-alibaba-r10.json`
- `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260512-alibaba-r10.md`
- `scripts/check_qbs_scored_run_readiness.py`
- `README.md`
- `docs/benchmark/README.md`
- `docs/benchmark/qbs-1/README.md`

R10 is now pre-registered as:

`qbs1-powered-single-provider-20260512-alibaba-r10`

Pre-registration tag:

`qbs/preregister/qbs1-powered-single-provider-20260512-alibaba-r10`

R10 remains full eight-family `POWERED_SINGLE_PROVIDER` Alibaba/DashScope
`qwen-turbo`, preserving R6-R9 comparability. Reviewer scoring is planned with
OpenAI `gpt-4o-mini` and DeepSeek `deepseek-chat` against the QBS36
triangulated calibration reference.

Validation completed for QBS-40:

- `python -m py_compile scripts/check_qbs_scored_run_readiness.py`: PASS
- `python -m json.tool` for R10 provider/config manifests: PASS
- `python scripts/check_qbs_scored_run_readiness.py --json`: PASS with expected
  no-tag warning before tag creation.
- After commit/tag:
  `python scripts/check_qbs_scored_run_readiness.py --json --require-preregistration --preregistration-tag qbs/preregister/qbs1-powered-single-provider-20260512-alibaba-r10`: PASS
- `python scripts/check_public_surface.py`: PASS
- `git diff --check`: PASS

## QBS-41 Closed Continuation

QBS-41 completed after QBS-40.

Public commit:

`a951709 Publish QBS R10 scored artifacts and post-score analysis`

Public status:

`QBS41_R10_REVIEWER_AGREEMENT_FAIL_NO_PUBLIC_QBS_CLAIM`

Public artifacts:

- `docs/benchmark/qbs-1/r10-post-score-analysis-qbs41.json`
- `docs/benchmark/qbs-1/r10-post-score-analysis-qbs41.md`
- `docs/benchmark/runs/qbs1-powered-single-provider-20260512-alibaba-r10/` (full run dir)
- `scripts/score_qbs_model_assisted_reviewers.py` (R10/QBS41 status strings added)

R10 execution result:

- 48 tasks x 3 repeats x 3 configs = 432 configuration executions.
- Hard gates: PASS (all 8 gates clean)
- Scorer completeness: 432/432 paired — QBS-34 retry holds, no missing scores.
- Reviewer agreement: FAIL
  - quadratic-weighted Cohen kappa: `0.3789`
  - Spearman rho: `0.5869`
- L4 result: FAIL
  - median normalized quality delta CFG-B vs CFG-A1: `-0.125`
  - bootstrap 95% CI: `[-0.25, 0.0]`
  - median heavy/reject improvement CFG-B vs CFG-A1: `-0.167`

QBS-41 post-score analysis key findings:

- `cost_quota_provider_selection` highest disagreement (mean abs diff `1.741`) —
  persistent across R6–R10; primarily a reviewer-level problem, not output-only.
- `negative_controls` regressed to median delta `-0.4375` (from `-0.125` in R9).
  QBS-39 family contract does not cover this family. Needs investigation.
- kappa marginally better than R9 (`0.379` vs `0.372`); rho improved (`0.587` vs
  `0.438`). QBS-39 remediation had a small positive effect but not enough to pass.
- Calibration-only kappa (`0.72`, QBS-37) does not generalise to live run scoring —
  live corpus is harder to agree on than the 35-anchor calibration set.

Boundary:

- No QBS score was claimed.
- No L4/L5, family-level, or provider-parity claim is made.
- Historical R5–R9 artifacts were not mutated.
- Raw key values were not printed or committed.

## Binding Boundary For Next Agent

The user has confirmed API keys are available in the provenance `.env.local` and
granted standing permission to use them for benchmark tests without re-asking.

Key file (do not print raw values):

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web\.env.local`

Present aliases: `DASHSCOPE_API_KEY`, `OPENAI_API_KEY`, `DEEPSEEK_API_KEY`.

## QBS Live Rerun Track — SUSPENDED 2026-05-12

**Decision:** User and Claude jointly decided to suspend QBS live reruns after R10.
This is not an abandonment of QBS — it is a deliberate pause pending a structural
fix to the scoring method before any further live cost is spent.

### Reason for suspension

The reviewer-agreement kappa has failed in 5 of 6 scored runs (R6–R10) and shows
no consistent improvement trend despite six remediation tranches (QBS-22 through
QBS-39):

| Run | kappa | rho | Result |
| --- | --- | --- | --- |
| R5 | 0.714 | 0.787 | PASS |
| R6 | 0.504 | 0.599 | FAIL |
| R7 | 0.464 | 0.533 | FAIL |
| R8 | 0.500 | 0.570 | FAIL |
| R9 | 0.372 | 0.438 | FAIL |
| R10 | 0.379 | 0.587 | FAIL |

The root cause is structural, not prompt-level: `gpt-4o-mini` and `deepseek-chat`
do not agree sufficiently on live corpus outputs (432 tasks) even when they agree
well on the 35-anchor calibration set (QBS-37 kappa `0.72`). Further rubric
or output-quality remediation rounds are unlikely to escape this ceiling without
changing the reviewer models or scoring architecture.

CVF already has sufficient evidence for its doctrine: hard gates PASS across all
6 scored runs, scorer completeness is stable at 432/432, and all artifacts are
reproducible with documented claim boundaries. The framework does not require an
L4/L5 quality claim to be useful or trustworthy.

### Conditions to reopen QBS live reruns

All three conditions must be met before pre-registering R11:

1. **Reviewer model upgrade** — replace `gpt-4o-mini` with `gpt-4o` (or stronger)
   AND replace `deepseek-chat` with `deepseek-reasoner` (or equivalent reasoning
   model). The calibration-only check (QBS-37 style) must pass kappa ≥ 0.60 with
   the new models before any live run is pre-registered.

2. **Fresh GC-018 candidate** — a new continuation candidate must be written,
   reviewed (optionally by Codex), and user-approved. It must explicitly address
   the reviewer-model change, the new calibration reference strategy, and whether
   the claim gate thresholds change.

3. **User explicit authorization** — the user must explicitly say to reopen QBS.
   Do not reopen based on inference from other instructions. Do not pre-register
   R11 or run calibration-only checks with new reviewer models without this
   explicit signal.

### What is NOT blocked

- EA Enhancement Track (Tracks A, B, C, D, E) — fully independent, start immediately.
- Any documentation, analysis, or read-only work on existing QBS artifacts.
- Calibration-only dry runs (no live cost) if user later approves a new reviewer-model
  preflight check as part of reopening.

## EA Track B — CLOSED 2026-05-12

Public commit: `92858eb Add EA Track B — QBS Benchmark Dashboard tab in /governance`

New tab `📈 Benchmark` added to `/governance` page (6th tab, display-only).

Artifacts:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/QBSBenchmarkPanel.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/QBSBenchmarkPanel.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/benchmark/qbs-summary/route.ts`

Shows: R5–R10 run history (kappa, hard gates, delta, L4), per-family delta chart
(R10), suspension badge with reason and resumption conditions.

Validation: 5 tests PASS, lint PASS (max-warnings=0), build PASS.

## Next Allowed Steps — EA Enhancement Track

The user has authorized the EA Enhancement Track to begin immediately.
Execution order per `docs/roadmaps/CVF_EA_ENHANCEMENT_ROADMAP_2026-05-12.md`:

1. **Track B** — DONE (commit `92858eb`).
   QBS Benchmark Dashboard tab live in `/governance`.

2. **Track A** — DONE (commit `158309f`).
   Status: `EA_TRACK_A_INSTRUMENTATION_DEPLOYED`
   Artifacts:
   - `src/lib/governance-tax-logger.ts` — GovernanceTaxPhases/Log types,
     evaluateFitness (GREEN<10%/AMBER<20%/RED≥20%), JSONL sink via `_taxLogSink`
   - `src/lib/governance-tax-logger.test.ts` — 12 tests PASS
   - `src/app/api/execute/route.ts` — 4 timing markers + logGovernanceTax
     at final success return (pre/policy/provider/post phases)
   - `docs/benchmark/governance-tax/governance-tax-fitness-function.md`
   - `scripts/analyze_governance_tax.py` — aggregate JSONL analysis script
   - `cvf-web/.gitignore` — `/logs/` excluded
   Validation: lint PASS, tsc PASS, 53 tests PASS, build PASS

3. **Track C** — DONE (commit `b93f246`).
   Status: `EA_TRACK_C_INTEGRITY_MODEL_DEPLOYED`
   Artifacts:
   - `docs/reference/CVF_AUDIT_RECEIPT_INTEGRITY_MODEL.md` — Git-as-hash-chain
     model, receipt chain spec, known limitations (no GPG), operator checklist
   - `scripts/generate_evidence_manifest.py` — SHA-256 manifest generator
     (243 files, docs/benchmark/ + docs/evidence/)
   - `scripts/verify_evidence_manifest.py` — manifest verifier, TAMPERED
     detection confirmed working
   - `docs/evidence/MANIFEST_SHA256.json` — initial snapshot at commit 158309f
   Validation: generate+verify PASS (243/243), tamper detection PASS,
   public_surface PASS

4. **Track D** — DONE (commit `7a48cd0`).
   Status: `EA_TRACK_D_PHASE1_PROVIDER_POLICY_ENGINE_DEPLOYED`
   Artifacts:
   - `src/lib/provider-policy-engine.ts` — resolveProviderPolicy (R0/R1/R2/R3
     risk-tier routing), executeWithFailover (R0/R1 only), ProviderPreference type
   - `src/lib/provider-policy-engine.test.ts` — 11 tests PASS (R0/R1 preference,
     R2/R3 governance override, edge cases, failover scenarios)
   - `src/app/api/execute/route.ts` — wired after enforcement ALLOW; preference
     from `body.providerPreference`; failoverExec replaces direct executeAI call;
     `finalProvider`/`failoverUsed`/`policyRiskTierOverride` in receipt
   - `src/components/ProviderPreferenceSelector.tsx` — bilingual 3-option tile
     selector (Auto/Fast/Accurate); added to Settings.tsx Preferences tab
   - `src/components/Settings.tsx` — `providerPreference` added to UserPreferences
   - `docs/benchmark/qbs-1/provider-routing-policy.md` — governance policy doc
   - `docs/reviews/CVF_GC018_TRACK_D_PROVIDER_POLICY_ENGINE_2026-05-13.md` — GC-018
     continuation candidate (Depth Audit 9/10, authorized Phase D.1)
   - `governance/public-surface-manifest.json` — GC-018 review file allowlisted
   Validation: lint PASS, tsc PASS, 66 tests PASS, build PASS,
   check_public_surface.py PASS

5. **Track E** — DONE (commit `8aa7e97`).
   Status: `EA_TRACK_E_PHASE1_DLP_QUALITY_BENCHMARK_DEPLOYED`
   Artifacts:
   - `src/lib/dlp-benchmark.ts` — runDLPBenchmark: loads corpus, runs
     applyDLPPatterns per case, computes TP/FN/TN/FP/precision/recall/F1
   - `src/lib/dlp-benchmark.test.ts` — 10 tests PASS (true PII detection,
     false PII precision, F1/grade, adversarial isolation, corpus smoke test)
   - `docs/benchmark/dlp/dlp-corpus-v1.json` — 24 synthetic cases (12 true PII,
     8 false PII, 4 adversarial); no real PII; all values clearly fabricated
   - `docs/benchmark/dlp/dlp-benchmark-v1.json` — baseline: F1=0.96, Recall=1.0,
     Precision=0.9231, grade=PASS
   - `docs/benchmark/dlp/dlp-quality-baseline.md` — baseline doc with known
     limitations (CCCD false positive on 12-digit numbers; adversarial obfuscation)
   - `docs/reviews/CVF_GC018_TRACK_E_DLP_QUALITY_BENCHMARK_2026-05-13.md` — GC-018
     continuation candidate (Depth Audit 8/10, authorized Phase E.1)
   - `scripts/run_dlp_benchmark.py` — CLI runner; --save writes baseline JSON
   - `governance/public-surface-manifest.json` — GC-018 review file allowlisted
   Validation: lint PASS, tsc PASS, 76 tests PASS, build PASS,
   check_public_surface.py PASS

## EA Enhancement Track — COMPLETE

All 5 tracks delivered:
- Track B: commit `92858eb` — QBS Benchmark Dashboard
- Track A: commit `158309f` — Governance Tax Measurement
- Track C: commit `b93f246` — Audit Receipt Integrity
- Track D: commit `7a48cd0` — Provider Policy Engine (Phase D.1)
- Track E: commit `8aa7e97` — DLP Quality Benchmark (Phase E.1)

Total tests: 76 PASS. All hard gates clean across all tracks.
No open EA tracks. Next work requires a fresh GC-018.

## CVF Value Position Assessment (2026-05-13)

User and Claude jointly assessed CVF value after EA Track completion.
This assessment is BINDING context for next agent — do not dismiss.

Key finding:

> EA Tracks A–E are operator/infrastructure value, not end-user value.
> CVF measures itself well but has not yet proven it improves the experience
> of the person actually sending prompts.

What CVF CANNOT yet answer:
1. What % of BLOCK/CLARIFY decisions are false positives? — No data.
2. Does governance latency noticeably slow users down? — Baseline exists (Track A),
   but no live traffic measured yet, and no optimization done.
3. When NEEDS_APPROVAL fires, does the user know what to do? — UX unknown.
4. Does CVF-governed output quality match ungoverned output? — No A/B data.

These are NOT blockers for CVF's current use cases (local-first, developer/operator).
They ARE the next frontier if CVF wants to demonstrate direct end-user value.

## Next Roadmap — EVT (End-User Value Track)

Roadmap file: `docs/roadmaps/CVF_EVT_END_USER_VALUE_ROADMAP_2026-05-13.md`
Codex review file: `docs/reviews/CVF_EVT_ROADMAP_CODEX_REVIEW_2026-05-14.md`

Status: EVT-1 + EVT-3 CODEX-CORRECTED IMPLEMENTATION COMPLETE; EVT-2/EVT-4
NOT STARTED. Do not implement remaining EVT tracks without:
1. Reading the Codex review file above
2. User explicit approval per track
3. GC-018 for EVT-2 if execution order changes and GC-018 for EVT-4

### EVT tracks summary

EVT-1 — False Positive Audit (no GC-018, 1–2 days)
  Add "Report false positive" button after BLOCK/CLARIFY responses.
  Log to JSONL. Script to analyze FP rate. No enforcement logic changes.
  Status: IMPLEMENTED 2026-05-14 using Codex correction — separate
  append-only events linked by `receiptId`, no receipt mutation, button in
  `ProcessingScreen`, report-only passive flow.

EVT-3 — NEEDS_APPROVAL UX Improvement (no GC-018, 2–3 days)
  Audit NEEDS_APPROVAL journey. Add context message + optional rewrite hint.
  Hard constraint: hint must not expose R2/R3 patterns or teach bypass.
  Status: IMPLEMENTED 2026-05-14 using Codex correction — hardened existing
  `ProcessingScreen` approval panel, expiry/retry guidance, deterministic
  static safe hints only, no AI-generated fallback.

EVT-2 — Governance Latency Optimization (GC-018 if execution order changes, 1–5 days)
  Depends on live traffic data from EVT-1. Run analyze_governance_tax.py first.
  Only optimize if AMBER/RED. Do not touch if GREEN.
  Start: after N≥20 live requests collected.

EVT-4 — Output Quality A/B Baseline (requires GC-018, 3–5 days)
  20 prompts × CFG-A (bare API) vs CFG-B (CVF governed). Model-assisted reviewer.
  NOT a QBS rerun — different question entirely.
  Start: only after separate GC-018 + user approves prompt set.

### Codex questions (answered in review — next agent must not skip)

The roadmap contains 5 open questions for Codex (4 track questions + 1 meta):
1. EVT-1: Should FP report trigger async Admin notification or passive log only?
2. EVT-2: Does parallelizing DLP + intent classification violate governance contract?
3. EVT-3: Where is the line between "helpful UX hint" and "governance bypass guide"?
4. EVT-4: If CFG-B < CFG-A, is it an architectural problem or a prompt-engineering fix?
5. Meta: Is there a more important end-user value gap not covered?

Codex answer summary: EVT direction is correct, but do not execute exactly as
written. EVT-1 should log false-positive reports as separate events linked to
receipts, not mutate receipts. EVT-3 should be audit + hardening of the existing
approval UX. EVT-2 must measure actual live route phases before optimization.
EVT-4 remains separate from QBS and requires GC-018 plus preregistered protocol.
Codex also recommends adding/deferring EVT-5: task recovery / abandonment rate.

### EVT implementation update — 2026-05-14

User approved Codex's 5/5 corrections and authorized implementation without
per-step waiting. Implemented EVT-1 and EVT-3 in the provenance workspace:

- `src/lib/false-positive-report.ts` adds append-only JSONL event logging for
  `REPORTABLE_DECISION_OBSERVED` and `FALSE_POSITIVE_REPORTED`.
- `src/app/api/governance/false-positive-report/route.ts` records authenticated
  false-positive reports and appends audit events; unauthenticated/invalid
  reports are rejected.
- `src/app/api/execute/route.ts` passively records BLOCK/CLARIFY denominator
  events after immutable receipts are created.
- `src/components/ProcessingScreen.tsx` shows the report control for
  BLOCK/CLARIFY only, keeps NEEDS_APPROVAL out of FP reporting, and adds safer
  approval copy plus static deterministic hint templates.
- `scripts/analyze_false_positive_rate.py` computes observed reportable
  decisions, FP reports, FP rate, and low-N caveat.
- `eslint.config.mjs` now ignores `.next-cvf-release-gate/**` so full lint does
  not scan generated release-gate build artifacts.

Verification:

- Targeted Vitest PASS: false-positive lib, false-positive API route,
  `ProcessingScreen`, and execute route tests (52 tests).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing warning in
  `src/app/api/system/jobs/route.test.ts`.
- `git diff --check` PASS.

EVT-2 remains measure-first; do not optimize execution order before real phase
data. EVT-4 still requires GC-018 and a preregistered A/B protocol.

## Repository and Keys

All public work goes in the public-sync clone:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Confirm public remote before any push:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

API keys (standing permission granted by user — no need to re-ask):

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web\.env.local`

Present aliases: `DASHSCOPE_API_KEY`, `OPENAI_API_KEY`, `DEEPSEEK_API_KEY`.
