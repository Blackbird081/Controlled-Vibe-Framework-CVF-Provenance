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

What CVF could not answer at roadmap creation:
1. What % of BLOCK/CLARIFY decisions are false positives? — EVT-1 now logs data;
   rate remains traffic-dependent.
2. Does governance latency noticeably slow users down? — EVT-2 measured 20 live
   samples; median governance tax 1.57%, GREEN.
3. When NEEDS_APPROVAL fires, does the user know what to do? — EVT-3 hardened
   the existing UX with next-step copy and static safe hints.
4. Does CVF-governed output quality match ungoverned output? — EVT-4 measured
   a negative result on the frozen corpus: median normalized delta -0.28.
5. Do users recover after governance friction? — EVT-5 now instruments recovery
   and abandonment; rate remains traffic-dependent.

These are NOT blockers for CVF's current use cases (local-first, developer/operator).
They ARE the next frontier if CVF wants to demonstrate direct end-user value.

## Next Roadmap — EVT (End-User Value Track)

Roadmap file: `docs/roadmaps/CVF_EVT_END_USER_VALUE_ROADMAP_2026-05-13.md`
Codex review file: `docs/reviews/CVF_EVT_ROADMAP_CODEX_REVIEW_2026-05-14.md`

Status: EVT ROADMAP COMPLETE as of 2026-05-14. EVT-4 result is negative for
the preregistered quality-delta rule. Future EVT follow-up should be a
template/prompt-quality remediation track, not QBS reopening. If new EVT work
starts, still:
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
  Status: COMPLETE 2026-05-14. `scripts/run_evt2_live_latency_measurement.js`
  collected 20/20 live Alibaba `/api/execute` samples. `scripts/analyze_governance_tax.py`
  reported median governance tax 1.57%, fitness GREEN, low-N caveat false.
  No optimization was made because no AMBER/RED bottleneck was measured.

EVT-4 — Output Quality A/B Baseline (requires GC-018, 3–5 days)
  20 prompts × CFG-A (bare API) vs CFG-B (CVF governed). Model-assisted reviewer.
  NOT a QBS rerun — different question entirely.
  Status: COMPLETE 2026-05-14 under
  `docs/reviews/CVF_GC018_EVT4_OUTPUT_QUALITY_AB_BASELINE_2026-05-14.md` and
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_PREREGISTRATION_2026-05-14.md`.
  Runner: `scripts/run_evt4_output_quality_ab.js`. Live evidence completed
  20/20 pairs, CFG-B receipts 20/20, safety failures 0, OpenAI `gpt-4o`
  reviewer. Median normalized delta CFG-B - CFG-A = -0.28, decision rule not met.
  Bounded conclusion: current governed documentation-template path reduced output
  usefulness/completeness/specificity on this corpus while preserving audit/safety.

EVT-5 — Task Recovery / Abandonment (no GC-018)
  Status: COMPLETE 2026-05-14. Added analytics events
  `task_recovery_prompted` and `task_recovery_started`; noncoder metrics now
  compute `taskRecoveryRate` and `governanceAbandonmentRate`; rollout readout
  includes `task_recovery` lane.

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

### EVT completion update — 2026-05-14

After EVT-1/EVT-3, user approved completing the rest in order and allowed
provider-key use without re-asking. Completed:

- EVT-2.1 live latency measurement: 20/20 live samples, GREEN fitness, no
  optimization.
- EVT-5 recovery/abandonment instrumentation and metrics.
- EVT-4 GC-018 + preregistration + live A/B evidence. Result negative:
  `CFG-B - CFG-A = -0.28` median normalized quality delta. This is an evidence
  finding, not a failed implementation. Next sensible work is template/prompt
  remediation for governed output quality, with a fresh roadmap/GC if it changes
  prompt contracts or quality claims.

Evidence artifacts:

- `docs/assessments/CVF_EVT2_LIVE_LATENCY_MEASUREMENT_2026-05-14.jsonl`
- `docs/assessments/CVF_EVT2_LIVE_LATENCY_MEASUREMENT_2026-05-14.md`
- `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_EVIDENCE_2026-05-14.json`
- `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SUMMARY_2026-05-14.md`

### EVT post-completion verification — 2026-05-14 (Claude, provenance workspace)

Reviewed Codex's two EVT completion commits (`c8a11760`, `15f54d80`) against the
review file `docs/reviews/CVF_EVT_ROADMAP_CODEX_REVIEW_2026-05-14.md`.

**Spec conformance — 5/5 Codex corrections applied:**

- EVT-1: `false-positive-report.ts` writes separate append-only JSONL events
  (`REPORTABLE_DECISION_OBSERVED` + `FALSE_POSITIVE_REPORTED`) linked by
  `receiptId`. Receipt is NOT mutated — verified via
  `git diff bb9491ae c8a11760 -- src/app/api/execute/route.ts` showing only
  a side-effect call to `recordReportableDecisionObserved`, no receipt field
  addition.
- EVT-1 UI: "Report false positive" button lives in `ProcessingScreen.tsx`
  (lines 486–515), not `ResultViewer`. Correct surface for BLOCK/CLARIFY.
- EVT-2: measure-first protocol followed. 20/20 live `/api/execute` samples
  collected; median governance tax 1.57% GREEN; no optimization performed
  because no AMBER/RED phase was measured.
- EVT-3: `resolveApprovalSafeHint` (ProcessingScreen.tsx:80–104) is a fixed
  pattern→safeHint Map, deterministic and static. No AI-generated fallback.
  Aligns with the "templated/deterministic, never AI-generated" constraint.
- EVT-4: GC-018 (`docs/reviews/CVF_GC018_EVT4_OUTPUT_QUALITY_AB_BASELINE_2026-05-14.md`)
  approved, preregistration committed before run, decision rule documented
  (`>= -0.05`). Result honestly recorded as negative.
- EVT-5 added: extends existing `noncoder-metrics.ts` (W127 contract) with
  `taskRecoveryRate` + `governanceAbandonmentRate`. No reinvention.

**Build health:**

- `npx tsc --noEmit` — PASS (exit 0).
- `npm run test:run` — 2613 PASS / 8 FAIL / 2 skipped (200 test files: 195 PASS,
  5 FAIL).
- All 8 failures are pre-existing and unrelated to EVT commits. Verified via
  `git log bb9491ae..HEAD -- <failed-test-paths>` returning empty for every
  failed file:
  - `src/app/api/admin/knowledge/w117-cp4-integration.test.ts` (3) — knowledge
    store mock/wiring drift, last touched far before EVT
  - `src/lib/hooks/useModals.test.ts` (1) — permission gates
  - `src/lib/intent-router-evidence-parity.test.ts` (2) — wizard mapping
    (last touched in W122-T1, 2026-04-27)
  - `src/lib/templates/governance-enforcement.test.ts` (1) — template registry
    drift (`meeting_notes`, `job_description`, `performance_review` missing
    from `skill-template-map.json`); last touched in commit `30ff4c66` (template
    quality work, well before EVT).

**EVT-4 finding — material and must not be ignored:**

CFG-B (CVF-governed) median normalized quality delta vs CFG-A (bare provider)
is **-0.28** on 20/20 R0/R1 non-coder prompts. Every single prompt scored lower
under governance. Per preregistration, this is **not** an architectural failure
by itself — it triggers a prompt/template remediation track. But it IS the
first concrete evidence that current CVF governance materially reduces output
usefulness for non-coder R0/R1 tasks while preserving audit/safety. Any future
"CVF improves end-user value" claim must reconcile with this evidence or
explicitly scope around it.

**Non-blocking but worth tracking:**

- `ProcessingScreen.tsx` grew 646 → 783 lines (advisory threshold 700 for
  `frontend_component`; hard threshold 1000). Still under hard cap, no
  exception entry needed yet. Next touch should consider extracting the FP
  button block and `resolveApprovalSafeHint` into sub-components.
- 8 pre-existing test failures should be tracked as a separate cleanup ticket,
  not as EVT regressions.

**Verdict for next agent / codex:** EVT roadmap implementation is structurally
correct and safe to merge. The negative EVT-4 result is the most important
output of this roadmap — treat it as evidence, not as a bug to fix in EVT-4.

### Findings to address later (NOT part of EVT scope — separate tickets)

Each item below is bounded, has a clear owner question, and must NOT be
silently bundled into another roadmap. Each requires its own scoping decision
or GC-018 candidate before work starts.

#### F-1. EVT-4 quality regression remediation (HIGHEST PRIORITY)

- Evidence: median CFG-B - CFG-A = -0.28 on 20/20 R0/R1 non-coder prompts
  (`docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SUMMARY_2026-05-14.md`).
- Problem: every governed prompt scored 0.16–0.32 lower than ungoverned on
  usefulness / completeness / specificity.
- Owner question: is the gap caused by (a) the documentation-template wrapper
  truncating/reformatting AI output, (b) `CVF_SYSTEM_PROMPT` over-constraining
  R0/R1 tasks, or (c) `output-validator` rejecting useful content?
- Required before starting: read raw evidence JSON, sample 5–10 CFG-B outputs
  vs CFG-A outputs by hand, identify which layer strips content. Decide
  scope (template vs system prompt vs validator) BEFORE writing GC-018.
- Boundary: NOT a QBS rerun. NOT a hard-gate change. NOT a provider routing
  change. Only changes to: template wrappers, system prompt, or output
  validator — and only if a fresh GC-018 authorizes that specific layer.

#### F-2. Pre-existing test failures cleanup (separate from EVT)

8 failures confirmed pre-existing (not caused by EVT commits). Bundle as one
cleanup ticket OR split per file owner — DO NOT close as part of EVT.

- `src/app/api/admin/knowledge/w117-cp4-integration.test.ts` (3 failures) —
  writable store wiring: `queryKnowledgeChunks` returns 0 chunks after
  `createCollection + addChunk`. Likely a `beforeEach` reset interacting badly
  with `knowledgeStore` singleton or a routing change in
  `queryKnowledgeChunks` that the W117-CP4 test never picked up.
- `src/lib/hooks/useModals.test.ts` (1 failure) — `respects permission gates
  for settings, ai usage, and context modals`. Permission contract drifted
  from test expectations.
- `src/lib/intent-router-evidence-parity.test.ts` (2 failures) —
  `field-set diff is empty for: "EN data analysis intent"` and
  `resolveGovernedStarterTemplate produces same id as routeIntent for each
  wizard starter key`. Intent router output shape vs evidence parity drift.
- `src/lib/templates/governance-enforcement.test.ts` (1 failure) — RULE-T4:
  `meeting_notes`, `job_description`, `performance_review` exist as form
  templates but are NOT mapped in `skill-template-map.json`. Either add the
  mappings OR remove the orphan templates.

Boundary: these are test/evidence drift, NOT runtime regressions. None of them
appeared in the EVT diff. Fixing them is a separate scope decision.

#### F-3. `ProcessingScreen.tsx` size advisory

- Current: 783 lines (was 646 before EVT).
- Threshold: advisory 700, hard 1000 for `frontend_component`. No exception
  needed yet; advisory only.
- Suggested extraction targets if/when next touched: (a) the FP-button block
  plus `falsePositiveReportState` state machine into a
  `FalsePositiveReportButton` sub-component; (b) `resolveApprovalSafeHint`
  into `src/lib/approval-hints.ts` with its own unit tests.
- Do NOT extract pre-emptively. Only if the file is touched again and adding
  more lines would push it toward the hard 1000 cap.

#### F-4. EVT analytics surface in operator UI

- EVT-1 logs FP events to JSONL; EVT-5 logs recovery/abandonment events to
  the analytics store. There is currently NO operator-facing surface that
  reads these and displays them. `scripts/analyze_false_positive_rate.py`
  exists but is CLI-only.
- Owner question: where should operators see FP rate and abandonment rate?
  Reuse the existing analytics dashboard (`AnalyticsDashboard.tsx`, already
  at advisory threshold), or build a separate "Governance Health" panel?
- Required before starting: confirm whether ops actually need a UI surface,
  or whether CLI + JSONL is sufficient for the local-first GA posture.

**Priority order if a single next track is chosen:** F-1 > F-2 > F-4 > F-3.

### F-1 diagnostic/remediation update — 2026-05-14 (Codex)

User said "doit" after commit `95c95e6b`; Codex pursued F-1 first.

What changed:

- Added GC-018 diagnostic authorization:
  `docs/reviews/CVF_GC018_EVT4_TEMPLATE_PAYLOAD_DIAGNOSTIC_RERUN_2026-05-14.md`.
- Found a concrete measurement bug in `scripts/run_evt4_output_quality_ab.js`:
  the evidence metadata recorded each frozen task's intended `templateId`, but
  CFG-B payload hard-coded `templateId: 'documentation'` for every governed
  call. This explains the original universal "Operational Documentation Packet"
  wrapper. This was a harness/template-wrapper artifact, not QBS, hard-gate,
  provider routing, or output-validator behavior.
- Fixed the EVT-4 harness so CFG-B uses task-specific trusted-form
  `templateId` and maps task prompts into the required fields.
- Corrected-template live rerun evidence:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TEMPLATE_CORRECTED_EVIDENCE_2026-05-14.json`
  and summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TEMPLATE_CORRECTED_SUMMARY_2026-05-14.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta still `-0.32`.
  So the hard-coded documentation wrapper was real but not the full gap.
- Added GC-018 prompt-contract remediation authorization:
  `docs/reviews/CVF_GC018_EVT4_PROMPT_CONTRACT_REMEDIATION_2026-05-14.md`.
- Updated `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`
  so template `outputTemplate` is treated as a minimum outline, not a
  compression target. Trusted non-coder templates now get a bounded depth target
  and explicit instructions to include assumptions, concrete next actions,
  rationale, and acceptance checks when applicable.
- Added prompt-contract unit coverage in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.test.ts`.
- Prompt-contract live rerun:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_PROMPT_CONTRACT_EVIDENCE_2026-05-14.json`
  and summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_PROMPT_CONTRACT_SUMMARY_2026-05-14.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta improved to
  `-0.20`, still FAIL.
- Depth-target live rerun:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DEPTH_TARGET_EVIDENCE_2026-05-14.json`
  and summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DEPTH_TARGET_SUMMARY_2026-05-14.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta improved to
  `-0.16`, still below preregistered `>= -0.05`.

Verification:

- `node --check scripts/run_evt4_output_quality_ab.js` PASS.
- `npx vitest run src/lib/execute-prompt-contract.test.ts` PASS (4/4).
- `npx tsc --noEmit` PASS.
- `git diff --check` PASS, with only the pre-existing Windows line-ending
  warning for `scripts/run_evt4_output_quality_ab.js`.

Current F-1 status:

- F-1 is **partially remediated but not closed**. Do not claim quality parity.
- Eliminated suspects: QBS, hard gate, routing, output validator. Also the
  all-documentation-wrapper measurement bug is fixed.
- Remaining strongest suspect: template-family fit and per-template output
  contracts for plan-like tasks. The weakest residual tasks are `Ops plan`,
  `Channel choice`, `FAQ plan`, `Retention plan`, and `Acceptance criteria`;
  reviewer rationales cite missing task-specific implementation steps, metrics,
  and acceptance checks.
- Next work should not keep broadening prompt text. It should inspect those
  specific plan-like failures and decide whether to add/route to more fitting
  trusted forms or refine the affected template contracts with a fresh GC-018.

### F-1 continuation update — 2026-05-15 (Codex)

User approved continuing the F-1 fix. Codex executed the bounded plan-shape
prompt remediation under
`docs/reviews/CVF_GC018_EVT4_PLAN_SHAPE_PROMPT_REMEDIATION_2026-05-15.md`.

What changed:

- `scripts/run_evt4_output_quality_ab.js` now supports output/summary stem
  overrides and sends each frozen EVT-4 task through its intended trusted-form
  `templateId` with mapped template inputs.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`
  now treats trusted form output templates as minimum outlines rather than
  compression targets, applies a bounded operator-ready depth target, and adds
  task-shape guidance for plan, comparison, FAQ, acceptance-criteria,
  prioritization, and persona requests.
- Task-shape guidance is emitted after the rendered template skeleton so it can
  override generic SWOT/risk/overview/documentation wrapper headings when those
  headings conflict with the user's requested deliverable.
- Unit coverage was expanded in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.test.ts`.
- Route receipts now use a single `knowledgeInjected` boolean derived from
  `hasKnowledgeContext(finalKnowledgeContext)` for consistency; this is not an
  F-1 quality lever.

Live evidence:

- Plan-shape rerun:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_PLAN_SHAPE_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_PLAN_SHAPE_SUMMARY_2026-05-15.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta `-0.16`.
- Shape-override rerun:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SHAPE_OVERRIDE_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SHAPE_OVERRIDE_SUMMARY_2026-05-15.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta `-0.16`.
- Negative experiments kept as audit artifacts but not retained in runtime:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_OPERATOR_CHECKS_SUMMARY_2026-05-15.md`
  and
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SYSTEM_APPENDIX_SUMMARY_2026-05-15.md`.
  Both made weak plan-like tasks worse, especially `Ops plan` and
  `Retention plan`.

Verification:

- `node --check scripts/run_evt4_output_quality_ab.js` PASS.
- `npx vitest run src/lib/execute-prompt-contract.test.ts src/app/api/execute/route.test.ts`
  PASS (33/33).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing `_request` warning in
  `src/app/api/system/jobs/route.test.ts`.
- `git diff --check` PASS with only Windows line-ending warnings for
  `AGENT_HANDOFF_V4_2026-05-12.md` and
  `scripts/run_evt4_output_quality_ab.js`.

Current F-1 status:

- F-1 remains **partially remediated but not closed**. Do not claim EVT-4
  quality parity.
- Best measured state: corrected-template gap improved from `-0.32` to a
  stable `-0.16`, still below the preregistered `>= -0.05` rule.
- Eliminated suspects now include QBS, hard gate, routing, output validator,
  all-documentation harness wrapper, and broad system-prompt appendix.
- Next likely scope: template-specific redesign or new trusted template
  families for plan, FAQ, acceptance-criteria, and decision/comparison
  deliverables under a fresh scope decision/GC-018. Do not keep adding global
  prompt instructions without new evidence.

### F-1 deliverable-contract continuation — 2026-05-15 (Codex)

User said "tiếp tục"; Codex continued F-1 under
`docs/reviews/CVF_GC018_EVT4_DELIVERABLE_CONTRACT_REMEDIATION_2026-05-15.md`.

What changed:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`
  now resolves bounded deliverable shapes for trusted non-coder form requests.
- Primary replacement contracts are retained only for clear FAQ,
  decision/comparison, and true plan requests.
- Acceptance-criteria, prioritization, and persona requests keep their original
  template skeletons plus shape guidance only, because live evidence showed
  primary replacement contracts hurt those lanes.
- The trusted-form depth target remains `700-1100` output tokens. A deeper
  `1100-1600` target was tested and rejected.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.test.ts`
  now covers the retained primary-contract and fallback boundaries.

Live evidence:

- Broad deliverable-contract run:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DELIVERABLE_CONTRACT_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DELIVERABLE_CONTRACT_SUMMARY_2026-05-15.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta `-0.16`.
  Not retained broadly because checklist/SOP/persona/prioritization worsened.
- Scoped deliverable-contract run:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SCOPED_DELIVERABLE_CONTRACT_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SCOPED_DELIVERABLE_CONTRACT_SUMMARY_2026-05-15.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta `-0.16`.
  This is the retained code posture.
- Deep scoped-contract run:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DEEP_SCOPED_CONTRACT_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_DEEP_SCOPED_CONTRACT_SUMMARY_2026-05-15.md`.
  Result: 20/20 live receipts, 0 safety failures, median delta `-0.16`.
  Not retained because it worsened plan/persona/checklist lanes.

Verification:

- `node --check scripts/run_evt4_output_quality_ab.js` PASS.
- `npx vitest run src/lib/execute-prompt-contract.test.ts src/app/api/execute/route.test.ts`
  PASS (34/34).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing `_request` warning in
  `src/app/api/system/jobs/route.test.ts`.
- `git diff --check` PASS with only Windows line-ending warnings for
  `AGENT_HANDOFF_V4_2026-05-12.md` and
  `scripts/run_evt4_output_quality_ab.js`.

Current F-1 status:

- F-1 is still **not closed**. The best live result remains median `-0.16`,
  not the preregistered `>= -0.05` parity rule.
- The prompt-contract layer has likely reached diminishing returns. Further
  global prompt/depth changes are unsupported by the negative experiments.
- Next F-1 scope should be a real template-family split, e.g.
  `operator_plan`, `decision_memo`, `faq_outline`, and
  `acceptance_criteria`, with the EVT-4 harness routing frozen tasks directly
  to those families and a new preregistered live comparison.

## Repository and Keys

All public work goes in the public-sync clone:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Confirm public remote before any push:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

API keys (standing permission granted by user — no need to re-ask):

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web\.env.local`

Present aliases: `DASHSCOPE_API_KEY`, `OPENAI_API_KEY`, `DEEPSEEK_API_KEY`.
