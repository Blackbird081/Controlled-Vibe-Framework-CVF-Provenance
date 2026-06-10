# CVF GC-018 - MLW8 Proof Export Live

Memory class: POINTER_RECORD

Status: BASELINE_ACCEPTED

Date: 2026-06-06

## Purpose

This GC-018 baseline authorizes a bounded MLW8 proof/export/live tranche. The
goal is to add evidence handling around existing MLW8 efficiency and
overconstraint feedback without changing MLW8 into an autonomous optimizer,
policy mutator, evidence reducer, provider router, public readiness claim, or
production readiness claim.

## Scope / Target / Owner Boundary

Target:

- MLW8 proof/export/live evidence boundary for cost proof, benchmark evidence,
  live release gate evidence, and public-safe export evidence.

Owner boundary:

- Private provenance owns GC-018, work order, runtime helper, tests, evidence,
  completion review, and session sync.
- Public-sync owns only the public-safe evidence artifact and public commit.
- Existing MLW8 advisory helper remains the source authority for MLW8 feedback
  and authority-boundary invariants.

## 2. Authority Chain

- Operator instruction: 2026-06-06 chat instruction authorizing MLW8
  optimization/benchmark/cost proof, public-safe export order, live/provider
  proof order, multi-role execution, API-key live run, and no further operator
  questions for this tranche.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V15_2026-05-29.md`.
- Existing MLW8 closure:
  `docs/reviews/CVF_MLW8_EFFICIENCY_OVERCONSTRAINT_FEEDBACK_COMPLETION_2026-06-05.md`.
- Existing MLW8 runtime owner:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw8-efficiency-overconstraint-feedback.ts`.
- Public boundary authority:
  `docs/reference/archive/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md`
  and `AGENTS.md`.
- Live proof authority: `scripts/run_cvf_release_gate_bundle.py`.

## Source / Predecessor Evidence

Predecessor evidence:

- `docs/baselines/CVF_GC018_MLW8_EFFICIENCY_OVERCONSTRAINT_FEEDBACK_2026-06-05.md`
- `docs/work_orders/CVF_WO_MLW8_EFFICIENCY_OVERCONSTRAINT_FEEDBACK_2026-06-05.md`
- `docs/reviews/CVF_MLW8_EFFICIENCY_OVERCONSTRAINT_FEEDBACK_COMPLETION_2026-06-05.md`

## 3. Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS - MLW8 advisory runtime owner exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw8-efficiency-overconstraint-feedback.ts` | Lines 4-5 | `MLW8_EFFICIENCY_OVERCONSTRAINT_FEEDBACK_VERSION` | MLW8 feedback module | ACCEPT |
| EXISTS - MLW8 efficiency classes exist | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw8-efficiency-overconstraint-feedback.ts` | Lines 7-14 | `EfficiencyFeedbackClass` | MLW8 feedback module | ACCEPT |
| EXISTS - MLW8 overconstraint classes exist | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw8-efficiency-overconstraint-feedback.ts` | Lines 16-20 | `OverconstraintFeedbackClass` | MLW8 feedback module | ACCEPT |
| LITERAL_INVARIANT - MLW8 does not authorize automatic optimization | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw8-efficiency-overconstraint-feedback.ts` | Lines 61-64 | `automaticOptimizationAuthorized` | `EfficiencyOverconstraintFeedbackReadout.authorityBoundary` | ACCEPT |
| LITERAL_INVARIANT - MLW8 does not authorize policy relaxation | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw8-efficiency-overconstraint-feedback.ts` | Lines 61-64 | `policyRelaxationAuthorized` | `EfficiencyOverconstraintFeedbackReadout.authorityBoundary` | ACCEPT |
| LITERAL_INVARIANT - MLW8 does not authorize evidence reduction | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw8-efficiency-overconstraint-feedback.ts` | Lines 61-64 | `evidenceReductionAuthorized` | `EfficiencyOverconstraintFeedbackReadout.authorityBoundary` | ACCEPT |
| LITERAL_INVARIANT - MLW8 does not authorize autonomous mutation | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw8-efficiency-overconstraint-feedback.ts` | Lines 61-64 | `autonomousMutationAuthorized` | `EfficiencyOverconstraintFeedbackReadout.authorityBoundary` | ACCEPT |
| RUNTIME_BEHAVIOR - MLW8 builder emits public/cost/performance claim boundary | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw8-efficiency-overconstraint-feedback.ts` | Lines 143-152 | `boundaries` | `buildEfficiencyOverconstraintFeedbackReadout` | ACCEPT |
| EXISTS - cost quota estimate type exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-cost-quota.ts` | Lines 33-40 | `LiveCallEstimate` | Cost quota module | ACCEPT |
| RUNTIME_BEHAVIOR - cost quota preflight exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-cost-quota.ts` | Lines 355-444 | `evaluateCostQuotaPreflight` | Cost quota module | ACCEPT |
| RUNTIME_BEHAVIOR - cost quota summary exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-cost-quota.ts` | Lines 447-470 | `summarizeCostQuota` | Cost quota module | ACCEPT |
| EXISTS - release gate command is live-governance proof owner | `scripts/run_cvf_release_gate_bundle.py` | Lines 336-378 | `main` | Release gate bundle | ACCEPT |
| RUNTIME_BEHAVIOR - release gate bootstraps DashScope key aliases | `scripts/run_cvf_release_gate_bundle.py` | Lines 72-80 | `bootstrap_live_provider_env` | Release gate bundle | ACCEPT |
| RUNTIME_BEHAVIOR - release gate includes live Playwright governance E2E | `scripts/run_cvf_release_gate_bundle.py` | Lines 230-271 | `check_e2e` | Release gate bundle | ACCEPT |
| RUNTIME_BEHAVIOR - release gate JSON output exists | `scripts/run_cvf_release_gate_bundle.py` | Lines 318-328 | `json_output` | Release gate bundle | ACCEPT |
| EXISTS - Alibaba key aliases exist | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/alibaba-env.ts` | Lines 1-18 | `resolveAlibabaApiKey` | Alibaba env resolver | ACCEPT |
| EXISTS - public export dispositions are canonical | `docs/reference/archive/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md` | Lines 29-36 | `Public Export Disposition` | Public export standard | ACCEPT |
| RUNTIME_BEHAVIOR - exported public work requires remote, commit, path evidence | `docs/reference/archive/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md` | Lines 53-63 | `EXPORTED` | Public export standard | ACCEPT |
| EXISTS - public-facing changes must use public-sync clone | `AGENTS.md` | Lines 127-150 | `Controlled-Vibe-Framework-CVF-public-sync` | Repository boundary instructions | ACCEPT |
| EXISTS - public-safe MLW8 summary blocks cost/performance/live readiness claims | `docs/reference/CVF_PUBLIC_SAFE_MEMORY_LEARNING_SUMMARY_2026-06-05.md` | Lines 34-39, 92-122 | `Blocked public wording` | Public-safe summary | ACCEPT |

## 4. Current Runtime Freshness Verification

Searches completed before this baseline:

```powershell
rg -n "MLW8|efficiency|overconstraint|cost|release_gate|public export|live" docs EXTENSIONS scripts governance
rg -n "LearningOrchestrator|LearningSignalIntakeBridge|buildEfficiencyOverconstraintFeedbackReadout" .
git -C "d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" remote -v
git -C "d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" status --short
git -C "d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" rev-parse --short HEAD
```

Freshness result:

- Existing MLW8 runtime surface is advisory-only and source-backed.
- Existing cost quota and release gate surfaces can support a bounded proof
  readout.
- Public-safe summary already blocks public claims that MLW8 optimizes cost,
  output quality, or runtime behavior automatically.
- Public-sync clone remote is the public repository and was clean at HEAD
  `970374bbe` before this tranche.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.

Baseline:

- MLW8 remains advisory-only.
- PEL1 may prove and export bounded evidence around MLW8, cost quota, and live
  release gate status.
- Public export must follow public-sync remote/commit/path evidence.

Proposed tranche:

- `MLW8-PEL1` proof/export/live readout and evidence closure.

## 5. New Runtime Surface Authorized

This baseline authorizes a new bounded readout helper:

`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw8-proof-export-live-readout.ts`

The helper may:

- combine existing MLW8 advisory readout state with cost quota disposition,
  live release gate status, and public export disposition;
- emit proof/export eligibility, diagnostics requirements, and claim boundary
  fields;
- preserve false authority flags for automatic optimization, policy relaxation,
  evidence reduction, and autonomous mutation.

The helper must not:

- optimize prompts, context, providers, costs, latency, or output quality;
- relax policy, DLP, approval, or evidence requirements;
- claim production readiness, hosted readiness, public readiness, cost
  reduction, or performance improvement without explicit evidence and public
  export disposition;
- call provider APIs directly.

## 6. Public-Safe Export Authority

Public-safe export is authorized only from:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

The public artifact must be bounded evidence wording. It may say MLW8 has a
proof/export/live boundary and cite public-safe evidence. It must not include
private provenance paths, raw receipts, secrets, internal handoff content, hidden
IDE history, or unsupported cost/performance/readiness claims.

## Evidence / Verification

Required verification:

- pre-dispatch and pre-implementation autorun gates before runtime edits;
- focused MLW8 PEL1 unit tests;
- release-quality live proof command;
- public-sync remote, commit, and artifact path evidence;
- pre-closure and pre-push autorun gates before closure claim.

## 7. Live Provider Proof Authority

Operator authorization permits using available API keys for this tranche.
Release-quality live proof must run:

```powershell
python scripts/run_cvf_release_gate_bundle.py --json
```

Any failed, partial, timed-out, or rerun-triggering live run must be classified
with a secret-safe diagnostic before rerun.

## 8. Risk Ceiling

Risk ceiling: R2 bounded governed proof/export/live evidence.

Escalation is not required for live key use, public-sync work, or routine
allowed-scope gate remediation because the operator explicitly authorized this
tranche. Escalation is still required for destructive actions, secret exposure,
unbounded public claims, production deployment, provider routing changes,
policy relaxation, or runtime mutation.

## Claim Boundary

This baseline authorizes proof handling only. It does not claim cost
optimization, benchmark superiority, output quality improvement, provider
quality superiority, production readiness, hosted readiness, or public readiness.

## 9. Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private GC-018 authorization baseline. Public-safe export is
authorized as downstream work in the matching work order and must be closed with
public-sync remote, commit, and artifact path evidence before any public catalog
claim.
