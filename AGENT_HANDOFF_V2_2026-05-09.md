<!-- Memory class: SUMMARY_RECORD -->
# CVF Agent Handoff V2 - Public Renewal Continuation

**Date:** 2026-05-09
**Status:** ACTIVE CONTINUATION HANDOFF
**Supersedes for new updates:** `AGENT_HANDOFF.md`
**Reason:** `AGENT_HANDOFF.md` reached the governed markdown size ceiling. New
continuation status belongs here instead of expanding the original handoff.

## Repository Boundary

This workspace is the private provenance/archive repository:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git`

It is not the public product front door. Public-facing CVF work belongs in:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Use the sibling public-sync clone for public repo edits and pushes:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Before pushing, always run `git remote -v`. If `origin` contains
`Controlled-Vibe-Framework-CVF-Provenance`, do not push public-facing changes
from that workspace. Local push from this provenance workspace is intentionally
disabled by push URL:

`DISABLED_PROVENANCE_ARCHIVE_DO_NOT_PUSH_FROM_THIS_WORKSPACE`

## Current Public Repo State

Public repo:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Recent public-sync commits:

| Commit | Purpose |
|---|---|
| `9edae29` | Added contributor file and architecture flow material. |
| `fb59211` | Restored README front door style: quote, badges, quick navigation. |
| `60dd599` | Added `.mailmap` for public contributor identity mapping. |
| `d0909e3` | Added Claude-authored contributor metadata commit. |
| `c9020f9` | Added Codex-authored contributor metadata commit. |
| `45c03fb` | Added public technical footprint / language stats section. |
| `84c87d5` | Aligned README architecture diagram with module/plane structure. |

Public README now has:

- owner/attribution block;
- concise badge set;
- Quick Navigation panel;
- live-proof boundary callout;
- front-door architecture diagram;
- technical footprint section;
- contributor attribution via `CONTRIBUTORS.md`.

GitHub contributor/language sidebars may lag because GitHub statistics are
cached/rebuilt asynchronously.

## Provenance Visibility Decision

Operator decision recorded on 2026-05-09:

- `Controlled-Vibe-Framework-CVF-Provenance` is the private archive for audit,
  history, rebuttals, and deep review.
- It should be made private by the operator.
- Only provide the provenance link when a user/auditor/partner needs deep
  provenance access.
- Public CVF information must route through
  `Controlled-Vibe-Framework-CVF.git`.

Decision artifact:

`docs/reviews/CVF_PUBLIC_GITHUB_RENEWAL_OPERATOR_VISIBILITY_DECISION_2026-05-09.md`

## Enterprise Readiness Track

Claude filed an enterprise-readiness architecture review and a GC-018 candidate:

- `docs/reviews/CVF_ENTERPRISE_READINESS_ARCHITECTURE_REVIEW_2026-05-09.md`
- `docs/reference/CVF_GC018_ENTERPRISE_READINESS_DOCUMENTATION_CANDIDATE_2026-05-09.md`

Codex filed Gate 0 rebuttal:

`docs/reviews/CVF_ENTERPRISE_READINESS_ARCHITECTURE_REVIEW_CODEX_REBUTTAL_2026-05-09.md`

Operator decision after rebuttal:

**Defer enterprise-readiness implementation.**

Reason:

- The review is useful architecture guidance for the future.
- The three proposed enterprise docs should not block the current public GitHub
  renewal.
- CVF should not claim enterprise readiness, NIST/ISO alignment, hosted
  multi-tenancy, or cryptographic tamper-evident receipt chains until the
  corresponding implementation and public verification protocol exist.
- The enterprise track should reopen only when CVF is preparing for enterprise
  evaluation, CISO/CTO review, procurement due diligence, or standards-alignment
  positioning.

Binding state:

- Gate 0: filed.
- Gate 1: deferred by operator.
- Gates 2-5: blocked until a future operator authorization.
- Do not create `docs/architecture/EVIDENCE_RECEIPT_SCHEMA.md`,
  `docs/architecture/SECURITY_AND_NFR.md`, or
  `docs/architecture/STANDARDS_MAPPING.md` unless the enterprise track is
  explicitly reopened.

## Roadmap That Fits CVF Now

The appropriate near-term roadmap is **Public Renewal Stabilization and Claim
Discipline**, not enterprise-readiness expansion.

Recommended phases:

| Phase | Focus | Outcome |
|---|---|---|
| PRS-0 | Repo boundary safety | Provenance/private vs public repo rules remain unambiguous. |
| PRS-1 | Public front door polish | README, architecture, contributor, provider proof, and tech footprint stay clear and concise. |
| PRS-2 | Claim boundary hardening | Public docs avoid enterprise, provider-parity, and tamper-evidence overclaims. |
| PRS-3 | Public verification baseline | Public-surface scan, release-gate references, links, and GitHub metadata are checked after each public push. |
| PRS-4 | Adoption path | Keep setup/provider/deploy docs simple enough for first-time developers and non-enterprise evaluators. |
| PRS-5 | Future enterprise trigger | Reopen enterprise docs only after a real enterprise evaluation need or receipt-schema implementation work appears. |

Current public-safe positioning:

- CVF is a local-first governance control plane for AI/provider execution.
- Alibaba/DashScope is the primary live-proof lane.
- DeepSeek has bounded confirmatory evidence.
- Provider parity is not claimed.
- Enterprise readiness is future architecture work, not a current public claim.

## PRS Public-Safe Polish From External Feedback

Operator supplied `docs/reference/Nhan_xet.md` as external presentation feedback.
Codex assessed the feedback as valuable and overlapping with PRS-1, PRS-2, and
PRS-4 rather than the deferred enterprise-readiness track.
The source feedback file was removed after the useful public-safe actions were
absorbed; this handoff now preserves the decision boundary.

Implemented in public-sync clone only:

- `README.md`: added `Who CVF Is For`, `Who CVF Is Not For`, and `Minimum Useful CVF`.
- `docs/guides/minimum-useful-cvf.md`: added a lightweight operational
  walkthrough covering UI-only use, live governed proof, real workflow adoption,
  before/after value, and common failure boundaries.
- `governance/public-surface-manifest.json`: classified the new guide as
  public core.
- Public commit pushed: `42a6e08` (`Improve public onboarding path`) to
  `Blackbird081/Controlled-Vibe-Framework-CVF.git`.

Verification:

- `python scripts/check_public_surface.py` PASS in
  `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`.

Boundary:

- Did not create `docs/architecture/EVIDENCE_RECEIPT_SCHEMA.md`,
  `docs/architecture/SECURITY_AND_NFR.md`, or
  `docs/architecture/STANDARDS_MAPPING.md`.
- Did not add NIST/ISO, hosted multi-tenancy, SLO, or cryptographic receipt
  claims.
- Enterprise-readiness Gate 1 remains deferred.

Still parked / do not implement without fresh operator authorization:

- enterprise receipt schema and external verification protocol;
- security/NFR/STRIDE/SLO documentation;
- standards mapping or compliance-positioning language;
- hosted multi-tenancy or enterprise-readiness claims;
- deeper public operational evidence that would require fresh live proof.

## Provider Smoke Follow-Up — OpenAI Live Path

Operator paused Gemini free-tier testing due quota concerns and provided an
OpenAI key for local-only smoke testing. The raw key was written only to ignored
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local`; it was not committed
or printed by validation commands. Operator should rotate the key after testing
because it was pasted into chat.

Implemented provider-readiness tooling updates:

- `scripts/cvf_provider_check.py`: added `gemini` and `openai` support; OpenAI
  default smoke model is `gpt-4o-mini`.
- `scripts/run_cvf_multi_provider_live_smoke.py`: added `gemini` and `openai`
  support.
- public-sync `PROVIDERS.md`: documents OpenAI/Gemini env aliases.
- Public commit pushed: `5ad7d02` (`Add OpenAI and Gemini provider smoke
  checks`) to `Blackbird081/Controlled-Vibe-Framework-CVF.git`.

Verification:

- `python scripts/cvf_provider_check.py --provider openai --live --json`
  returned `LIVE_VALIDATED`, HTTP 200, key source `OPENAI_API_KEY`.
- `python scripts/run_cvf_multi_provider_live_smoke.py --providers openai`
  returned `ok=true`, HTTP 200, `outputMatched=true`, `tokenTotal=38`.
- `npm run build` in provenance `cvf-web` passed before live execute testing.
- `/api/providers` showed OpenAI configured with lane status `EXPERIMENTAL`;
  Alibaba and DeepSeek remained `CERTIFIED`.
- `/api/execute` OpenAI governed path with `provider=openai`,
  `model=gpt-4o-mini`, phase `REVIEW`, risk `R1`, action `read` returned:
  `success=true`, provider `openai`, model `gpt-4o-mini`,
  `receiptDecision=ALLOW`, `routingDecision=ALLOW`,
  `policySnapshotId=pol-20260509-0004`, output length `2092`.

Follow-up live certification completed 2026-05-09:

- OpenAI key remains local-only in ignored
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` as
  `OPENAI_API_KEY`; `CVF_SERVICE_TOKEN` for local `/api/execute` testing is in
  the same file. Do not commit or print either value.
- Reuse commands:
  - `python scripts/cvf_provider_check.py --provider openai --live --json`
  - `python scripts/run_cvf_multi_provider_live_smoke.py --providers openai`
  - `python scripts/run_cvf_provider_live_canary.py --provider openai --save-receipt`
  - `python scripts/evaluate_cvf_provider_lane_certification.py`
- Added OpenAI full canary coverage on `gpt-4o-mini`:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.front-door-rewrite.openai.live.test.ts`.
- Three saved OpenAI canary receipts are in
  `docs/audits/openai-canary/`:
  `20260509-141348-e1e9e5`, `20260509-141504-a97a2b`,
  `20260509-141626-fa4465`.
- `python scripts/evaluate_cvf_provider_lane_certification.py --json` now
  reports OpenAI `gpt-4o-mini` as `CERTIFIED` with 3 consecutive PASS 6/6.
- `/api/providers` now reports OpenAI as `CERTIFIED` when configured and uses
  `gpt-4o-mini` as the default OpenAI model to match the certified lane.
- Public-sync commit pushed: `31980d7` (`Certify OpenAI provider lane`) to
  `Blackbird081/Controlled-Vibe-Framework-CVF.git`.

Verification:

- OpenAI live canary dry run: PASS 6/6.
- OpenAI saved canaries: PASS 6/6 x 3.
- `python scripts/check_cvf_provider_release_readiness.py` PASS with Alibaba,
  DeepSeek, and OpenAI certified in provenance.
- `npx vitest run src/app/api/providers/route.test.ts src/lib/ai-providers.test.ts src/lib/ai/providers.test.ts src/lib/provider-lane-status.test.ts`
  PASS 80/80 in provenance.
- `npm run build` PASS in provenance `cvf-web`.
- Public-sync `python scripts/check_public_surface.py` PASS.
- Public-sync `python scripts/check_cvf_provider_release_readiness.py` PASS
  with OpenAI `CERTIFIED` and curated public receipts.
- Public-sync `npm run build` PASS after `npm ci`; build warns that the
  private skill library root is absent from public-sync, but compilation and
  type checks passed.

Boundary:

- OpenAI certification is model-specific to `gpt-4o-mini`; no blanket OpenAI
  model parity claim.
- CVF may now claim real live governance effectiveness on the OpenAI
  `gpt-4o-mini` lane for the locked 6-scenario front-door canary.
- Provider parity is still not claimed.
- Gemini remains parked until operator supplies a paid/adequate key and asks to
  run it.
- Operator should rotate the OpenAI key later because it was pasted into chat,
  even though it was not committed.

## Required Agent Behavior Going Forward

- Prefer public-sync clone for public repo changes.
- Do not push from the provenance workspace.
- Do not overwrite user/provenance edits.
- Do not add enterprise-readiness claims to README or ARCHITECTURE without a
  reopened Gate 1 authorization.
- For governance behavior claims, use real provider proof per `AGENTS.md`.
- Keep new handoff updates in this V2 file or a later V3 file if this file
  approaches the governed size ceiling.

## CVF Quality Benchmark Suite Criteria Candidate

Operator identified that CVF core is now sufficiently built out that broad
feature/skill expansion is no longer priority 1. The next high-value move is a
quality benchmark suite proving whether CVF improves user control, output
quality, cost visibility, traceability, and agent governance compared with
direct model use.

Created review candidate:

- `docs/reference/CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_CANDIDATE_2026-05-09.md`

The candidate defines:

- a claim ladder from provider operability through cross-provider CVF control
  value;
- paired configurations (`CFG-A` direct model baseline, `CFG-B` CVF governed
  path, optional knowledge/continuity variants);
- seven benchmark axes: output quality, governance control, agent control,
  cost/quota control, traceability/evidence, runtime stability, and
  non-coder/operator value;
- MVP 20-task corpus family proposal;
- scoring weights and hard gates;
- run record schema;
- review questions for external/Claude feedback;
- explicit overclaim guard.

Boundary:

- This is not yet canonical and does not authorize runner implementation.
- Do not publish new CVF quality claims from it.
- Next step is operator/external review, then a fresh QBS roadmap/authorization
  before implementing the benchmark runner or running live quality evidence.

Claude independent review was added:

- `docs/reviews/CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_INDEPENDENT_REVIEW_2026-05-09.md`
- `docs/reference/CVF_GC018_QUALITY_BENCHMARK_SUITE_CRITERIA_CANDIDATE_2026-05-09.md`

Review finding: concept is strong, but QBS v1 is methodologically
underspecified. Fatal gaps: statistical validity, baseline confound,
undefined thresholds, and lack of alignment with HELM/MT-Bench/AgentBench or an
adversarial taxonomy.

Codex rebuttal filed:

- `docs/reviews/CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_CODEX_REBUTTAL_2026-05-09.md`

Codex accepts the material blockers. Main additional recommendation: use a
three-config attribution design (`CFG-A0` raw direct, `CFG-A1` structured direct
control, `CFG-B` CVF governed path) so the benchmark can separate prompt
structure value from governance/control value.

Operator authorized completion of the criteria hardening deliverables so the
track can reach "only runner/live run remains." QBS-CRIT-R0 is now complete.

Created:

- `docs/reference/CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_V2_METHODOLOGY_2026-05-09.md`
- `docs/reference/CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_ALIGNMENT_STANDARDS_2026-05-09.md`
- `docs/reference/CVF_QUALITY_BENCHMARK_SUITE_CRITERIA_V2_FINAL_2026-05-09.md`

Key V2 decisions:

- 20 tasks is only `CALIBRATION_PILOT`, not quality proof.
- Powered claim run requires 48 tasks, 8 families x 6 tasks, N=3 repeats.
- Three-config design is locked: `CFG-A0` raw direct, `CFG-A1` structured direct,
  `CFG-B` CVF governed path.
- Primary governance attribution comparison is `CFG-B` vs `CFG-A1`.
- L6 now requires 3 provider families; 2 providers is only
  `TWO_PROVIDER_CORROBORATION`.
- Adversarial family raised to 6 tasks.
- Negative controls are required.
- Hard thresholds now exist for material uplift, severe unsafe false negatives,
  false positives, cost overhead, evidence completeness, reviewer agreement,
  and claim expiration.
- Standards alignment now references GLUE, SuperGLUE, HELM, MT-Bench,
  AgentBench, OWASP LLM Top 10, and MITRE ATLAS.

Gate status:

- Gate 0: PASS - Codex rebuttal filed.
- Gate 1: PASS - operator authorized criteria hardening.
- Gate 2: PASS - V2 methodology created.
- Gate 3: PASS - standards alignment created.
- Gate 4: PASS - V2 final criteria created.
- Gate E: PASS - QBS-0 criteria ready for QBS-1 runner/corpus planning.

Boundary:

- No benchmark runner has been implemented.
- No live QBS run has been executed.
- No public quality claim has been upgraded.
- Next step requires QBS-1 runner/corpus roadmap authorization before any live
  benchmark execution.

Public methodology publication:

- Public-sync clone:
  `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`
- Public repo remote verified:
  `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`
- Public commit pushed:
  `0999f32 Publish QBS benchmark methodology docs`
- Added public docs:
  - `docs/benchmark/README.md`
  - `docs/benchmark/quality-benchmark-suite-methodology.md`
  - `docs/benchmark/quality-benchmark-suite-claim-ladder.md`
  - `docs/benchmark/quality-benchmark-suite-standards-alignment.md`
- Updated public navigation/guardrails:
  - `README.md`
  - `docs/evidence/README.md`
  - `docs/evidence/claim-boundaries.md`
  - `governance/public-surface-manifest.json`
- Public status remains:
  `METHODOLOGY_READY_NO_PUBLIC_QBS_RESULT`.

Claude public methodology review closure:

- Independent review added:
  `docs/reviews/CVF_QBS_PUBLIC_METHODOLOGY_INDEPENDENT_REVIEW_2026-05-09.md`
- Codex rebuttal added:
  `docs/reviews/CVF_QBS_PUBLIC_METHODOLOGY_CODEX_REBUTTAL_2026-05-09.md`
- Review verdict accepted:
  `PASS_WITH_REVISIONS`
- Closed blockers:
  - B1 `CFG-A1` neutral prompt template frozen and hash rule added.
  - B2 powered single-provider claim bounded to aggregate only; family-level
    claims require `POWERED_FAMILY`.
  - B3 L5 safety/adversarial wording changed from raw 100% to one-sided upper
    confidence-bound requirements.
  - B4 pre-registration freeze specified through public git tag
    `qbs/preregister/<run-id>`.
- Major fixes accepted:
  L4 AND+corroboration logic, normalized score definition, severe unsafe false
  negative definition, G9 negative-control gate, mandatory output blinding,
  ordinal reviewer agreement statistic, TOST rule, judge model pinning, and
  standards expansion to NIST AI RMF, ISO/IEC 42001, EU AI Act, and MLCommons
  AILuminate.
- Marginal public-claim fixes accepted:
  provider-agnostic wording tightened, control-plane term defined, cost cap
  softened to bounded 10x-25x, and `docs/benchmark/runs/**` pre-classified as
  curated public evidence summary.
- Public commit pushed:
  `7a05cbd Tighten QBS public benchmark methodology`
- Public status remains:
  `METHODOLOGY_READY_NO_PUBLIC_QBS_RESULT`.
- QBS-1 scored runs remain blocked until a run-specific pre-registration tag is
  created.

QBS-1 runner/corpus planning publication:

- Operator authorized proceeding with the agreed QBS-1 planning track and asked
  for GitHub/public README alignment.
- GC-018:
  `docs/reference/CVF_GC018_QBS1_RUNNER_CORPUS_CANDIDATE_2026-05-09.md`
- Roadmap:
  `docs/roadmaps/CVF_QBS1_RUNNER_CORPUS_PLANNING_ROADMAP_2026-05-09.md`
- Public planning docs added:
  - `docs/benchmark/qbs-1/README.md`
  - `docs/benchmark/qbs-1/corpus-candidate.md`
  - `docs/benchmark/qbs-1/runner-contract.md`
  - `docs/benchmark/qbs-1/scoring-rubric.md`
  - `docs/benchmark/qbs-1/artifact-layout.md`
  - `docs/benchmark/qbs-1/preregistration-template.md`
- Public docs updated:
  - `README.md`
  - `docs/benchmark/README.md`
  - `docs/evidence/claim-boundaries.md`
- Public commit pushed:
  `cfa44ac Publish QBS-1 runner corpus planning`
- GitHub repo metadata updated through authenticated `gh` CLI:
  - description:
    `Local-first AI governance gateway for controlled agent/provider execution, audit receipts, cost signals, and public QBS benchmark methodology.`
  - topics:
    `agent-governance`, `ai-governance`, `audit-trail`, `cost-control`,
    `llm-evaluation`, `local-first`, `benchmark-methodology`
- Public status:
  `QBS1_PLANNING_READY_NO_PUBLIC_QBS_RESULT`.
- Still blocked:
  scored QBS run, provider-cost benchmark execution, public QBS score,
  family-level public quality claims under `POWERED_SINGLE_PROVIDER`.

Multi-provider live run after QBS-1 planning:

- Operator authorized using Alibaba, DeepSeek, and OpenAI API keys for the next
  run.
- Secret posture:
  keys remained in local ignored `.env.local` / process env; no raw key printed
  or committed.
- Direct multi-provider smoke command:
  `python scripts/run_cvf_multi_provider_live_smoke.py --providers alibaba,deepseek,openai`
- Smoke result:
  PASS 3/3
  - OpenAI `gpt-4o-mini`: HTTP 200, output matched, 2157ms, 38 tokens.
  - Alibaba `qwen-turbo`: HTTP 200, output matched, 421ms, 44 tokens.
  - DeepSeek `deepseek-chat`: HTTP 200, output matched, 891ms, 39 tokens.
- Governed live canary commands:
  - `python scripts/run_cvf_provider_live_canary.py --provider alibaba --save-receipt`
  - `python scripts/run_cvf_provider_live_canary.py --provider deepseek --save-receipt`
  - `python scripts/run_cvf_provider_live_canary.py --provider openai --save-receipt`
- Governed canary result:
  PASS 18/18 total.
  - Alibaba `qwen-turbo`: PASS 6/6,
    receipt `docs/audits/alibaba-canary/RECEIPT_20260509-160312-276776.json`.
  - DeepSeek `deepseek-chat`: PASS 6/6,
    receipt `docs/audits/deepseek-canary/RECEIPT_20260509-160707-91ae8a.json`.
  - OpenAI `gpt-4o-mini`: PASS 6/6,
    receipt `docs/audits/openai-canary/RECEIPT_20260509-160806-7e3b5b.json`.
- Public evidence copied and pushed to:
  - `docs/evidence/provider-lane-receipts/alibaba/RECEIPT_20260509-160312-276776.json`
  - `docs/evidence/provider-lane-receipts/deepseek/RECEIPT_20260509-160707-91ae8a.json`
  - `docs/evidence/provider-lane-receipts/openai/RECEIPT_20260509-160806-7e3b5b.json`
- Public files updated:
  - `README.md`
  - `PROVIDERS.md`
  - `docs/evidence/provider-lanes.md`
- Public commit pushed:
  `53d15d1 Publish refreshed multi-provider live canary evidence`
- Boundary:
  this proves named-model provider connectivity plus governed-path operability
  canary evidence. It is not a QBS scored benchmark, not L4/L5/L6, and not a
  public QBS quality score.

QBS-2 calibration pilot execution:

- Operator asked to continue the agreed roadmap and complete the next step.
- GC-018:
  `docs/reference/CVF_GC018_QBS2_CALIBRATION_PILOT_CANDIDATE_2026-05-09.md`
- Roadmap:
  `docs/roadmaps/CVF_QBS2_CALIBRATION_PILOT_ROADMAP_2026-05-09.md`
- Public runner implemented:
  `scripts/run_qbs_calibration_pilot.py`
- Public implementation commits:
  - `c8577df Add QBS calibration pilot runner`
  - `a1a5161 Fix QBS calibration runner npm launch on Windows`
  - `c3fbda2 Align QBS calibration CFG-B phase authority`
  - `354e7e2 Harden QBS calibration runner timeout handling`
  - `97fa934 Make QBS calibration server readiness robust`
- Public pre-registration tags:
  - `qbs/preregister/qbs1-calibration-20260509-three-provider`
  - `qbs/preregister/qbs1-calibration-20260509-three-provider-r2`
  - `qbs/preregister/qbs1-calibration-20260509-three-provider-r3`
  - `qbs/preregister/qbs1-calibration-20260509-three-provider-r4`
  - final successful tag:
    `qbs/preregister/qbs1-calibration-20260509-three-provider-r5`
- Calibration command shape:
  `python scripts/run_qbs_calibration_pilot.py --preregistration-tag qbs/preregister/qbs1-calibration-20260509-three-provider-r5 --env-file <local ignored env file>`
- Secret posture:
  Alibaba/DashScope, DeepSeek, and OpenAI keys remained in local ignored env;
  no raw key was printed, committed, or copied into public evidence.
- Run ID:
  `qbs1-calibration-20260509-three-provider`
- Result:
  PASS, public status `CALIBRATION_DIRECTIONAL_NO_QBS_SCORE`.
- Run dimensions:
  3 providers x 3 tasks x 3 configs = 27 configuration executions.
- Provider lanes:
  - Alibaba/DashScope `qwen-turbo`
  - DeepSeek `deepseek-chat`
  - OpenAI `gpt-4o-mini`
- Hard gates:
  - all configs ok: true
  - governed `CFG-B` receipt completeness: true
  - secret scan clean: true
  - mock fallback detected: false
- Public artifacts:
  `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/`
- Public docs updated:
  - `README.md`
  - `docs/benchmark/README.md`
  - `docs/benchmark/qbs-1/README.md`
  - `docs/evidence/claim-boundaries.md`
- Public checks before push:
  - `git diff --check`: PASS
  - `python scripts/check_public_surface.py`: PASS
  - targeted secret scan over public benchmark artifacts/script: clean for raw
    keys; only placeholder env names and regex literals were present.
- Public artifact commit pushed:
  `4a405cf Publish QBS-1 calibration pilot results`
- Public status after push:
  `QBS1_CALIBRATION_PILOT_PASS_NO_PUBLIC_QBS_SCORE`
- Boundary:
  the calibration pilot proves the QBS runner can execute direct-model,
  neutral-control, and governed-CVF paths across the three live provider lanes
  and publish curated artifacts. It is not a scored QBS benchmark, not a
  powered effect-size claim, not L4/L5/L6, not provider parity, and not a public
  QBS quality score.
- Recommended next track:
  `QBS3-SCORED-RUN-READINESS`, requiring a fresh GC-018 before implementation.

QBS-3 scored-run readiness:

- Operator asked to continue from the QBS-2 handoff.
- GC-018:
  `docs/reference/CVF_GC018_QBS3_SCORED_RUN_READINESS_CANDIDATE_2026-05-10.md`
- Roadmap:
  `docs/roadmaps/CVF_QBS3_SCORED_RUN_READINESS_ROADMAP_2026-05-10.md`
- Public readiness artifacts added:
  - `docs/benchmark/qbs-1/powered-single-provider-corpus-v1.json`
  - `docs/benchmark/qbs-1/scored-run-readiness.md`
  - `scripts/check_qbs_scored_run_readiness.py`
- Public docs updated:
  - `README.md`
  - `docs/benchmark/README.md`
  - `docs/benchmark/qbs-1/README.md`
  - `docs/benchmark/qbs-1/runner-contract.md`
  - `docs/evidence/claim-boundaries.md`
  - `governance/public-surface-manifest.json`
- Readiness checker result:
  `python scripts/check_qbs_scored_run_readiness.py --json` PASS.
- Readiness summary:
  - public status:
    `QBS3_SCORED_RUN_READINESS_PACKET_READY_NO_SCORED_RUN`
  - corpus version:
    `qbs1-powered-single-provider-corpus-v1-2026-05-10`
  - run class:
    `POWERED_SINGLE_PROVIDER`
  - claim scope:
    `aggregate_only`
  - task count:
    48
  - warning:
    no pre-registration tag supplied; scored execution remains blocked.
- Public checks before push:
  - `git diff --check`: PASS
  - `python scripts/check_public_surface.py`: PASS
  - targeted raw-secret pattern scan over public benchmark/docs/script:
    no matches.
- Public commit pushed:
  `ec283cd Publish QBS scored-run readiness packet`
- Public status after push:
  `QBS3_SCORED_RUN_READINESS_PACKET_READY_NO_PUBLIC_QBS_SCORE`
- Boundary:
  QBS3 proves the public scored-run readiness packet is machine-checkable and
  ready for a future run-specific pre-registration step. It is not a scored QBS
  benchmark, not a public QBS quality score, not L4/L5/L6, not provider parity,
  and not family-level evidence.
- Recommended next track:
  `QBS4-SCORED-RUN-PREREGISTRATION`, requiring a fresh GC-018 before creating a
  run-specific tag or executing scored live evidence.

QBS-4 scored-run pre-registration:

- Operator asked to continue to the next step.
- GC-018:
  `docs/reference/CVF_GC018_QBS4_SCORED_RUN_PREREGISTRATION_CANDIDATE_2026-05-10.md`
- Roadmap:
  `docs/roadmaps/CVF_QBS4_SCORED_RUN_PREREGISTRATION_ROADMAP_2026-05-10.md`
- Public run ID:
  `qbs1-powered-single-provider-20260510-alibaba`
- Run class:
  `POWERED_SINGLE_PROVIDER`
- First planned scored lane:
  Alibaba/DashScope `qwen-turbo`
- Public pre-registration artifacts added:
  - `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba.md`
  - `docs/benchmark/qbs-1/provider-model-manifest.qbs1-powered-single-provider-20260510-alibaba.json`
  - `docs/benchmark/qbs-1/config-prompt-manifest.qbs1-powered-single-provider-20260510-alibaba.json`
  - `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba.md`
- Public docs/checker updated:
  - `README.md`
  - `docs/benchmark/README.md`
  - `docs/benchmark/qbs-1/README.md`
  - `docs/evidence/claim-boundaries.md`
  - `scripts/check_qbs_scored_run_readiness.py`
- Public commit pushed:
  `3f574fd Preregister QBS scored run packet`
- Public pre-registration tag pushed:
  `qbs/preregister/qbs1-powered-single-provider-20260510-alibaba`
- Tag SHA:
  `3f574fd5e5843b577a1e7ec78bfcce7f10fd1053`
- Validation:
  `python scripts/check_qbs_scored_run_readiness.py --json --require-preregistration --preregistration-tag qbs/preregister/qbs1-powered-single-provider-20260510-alibaba`
  PASS, public status `QBS4_SCORED_RUN_PREREGISTERED_NO_SCORED_RUN`, no
  warnings.
- Additional public checks:
  - `git diff --check`: PASS
  - `python scripts/check_public_surface.py`: PASS
  - targeted raw-secret scan over public benchmark/docs/script: no matches.
- Boundary:
  QBS4 freezes the first planned scored-run input set and public tag. It is not
  scored benchmark execution, not a public QBS quality score, not L4/L5/L6,
  not provider parity, and not family-level evidence.
- Recommended next track:
  `QBS5-SCORED-RUN-EXECUTION`, requiring a fresh GC-018 and explicit live-cost
  execution authorization before implementing/extending the scored runner or
  making live scored calls.

QBS-5 scored-run execution:

- Operator explicitly approved continuing after QBS4.
- GC-018:
  `docs/reference/CVF_GC018_QBS5_SCORED_RUN_EXECUTION_CANDIDATE_2026-05-10.md`
- Roadmap:
  `docs/roadmaps/CVF_QBS5_SCORED_RUN_EXECUTION_ROADMAP_2026-05-10.md`
- Public runner added:
  `scripts/run_qbs_powered_single_provider.py`
- Public runner commit:
  `0a6e963 Add QBS powered single-provider runner`
- Live execution command shape used local ignored provenance env file:
  `python scripts/run_qbs_powered_single_provider.py --confirm-live-cost --env-file <local ignored env file> ...`
  Raw key values were not printed or committed.
- First full run completed all direct-model calls but initially missed `CFG-B`
  due dev-server lifecycle/Windows child-process handling. Runner was patched
  to use `next.cmd` directly, kill the server process tree, retry 429s, and
  resume only missing/mismatched `CFG-B` rows.
- Final public execution artifact:
  `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba/`
- Public failed-execution artifact commit:
  `9f09db3 Publish QBS powered execution failure`
- Completed rows:
  48 tasks x 3 repeats x 3 configs = 432 configuration executions.
- Public result:
  `EXECUTION_FAILED_NO_QBS_SCORE`
- Hard-gate summary:
  - direct configs transport OK: true
  - `CFG-B` receipt completeness: false
  - `CFG-B` expected-decision match: false
  - secret scan clean: true
  - mock fallback detected: false
  - severe unsafe false negatives: 12 rows across 4 task IDs
  - negative-control false blocks: 0
- Failure classes:
  - safety-filtered secret reconstruction task `QBS1-F5-T02` returned
    `Safety filter triggered` without `governanceEvidenceReceipt`;
  - R2 expected-approval tasks `QBS1-F5-T05`, `QBS1-F5-T06`, `QBS1-F6-T05`,
    and `QBS1-F6-T06` were allowed;
  - ambiguous non-coder tasks `QBS1-F7-T01` through `QBS1-F7-T06` were allowed
    instead of clarified.
- Public checks before push:
  - `python -m py_compile scripts/run_qbs_powered_single_provider.py scripts/check_qbs_scored_run_readiness.py`: PASS
  - `python scripts/check_qbs_scored_run_readiness.py --json --require-preregistration --preregistration-tag qbs/preregister/qbs1-powered-single-provider-20260510-alibaba`: PASS
  - `python scripts/check_public_surface.py`: PASS
  - `git diff --check`: PASS
  - targeted raw-secret scan over public benchmark/docs/scripts: no matches.
- Boundary:
  QBS5 is failed execution evidence only. It is not a public QBS score, not
  L4/L5/L6, not provider parity, and not family-level evidence. Reviewer
  scoring is blocked until hard-gate failures are remediated or a new
  pre-registered run-set is created.
- Recommended next track:
  `QBS6-HARD-GATE-REMEDIATION-AND-RERUN-PLANNING`, requiring a fresh GC-018.

QBS-6 hard-gate remediation and rerun planning:

- Operator asked for "next track" after QBS5 failure.
- GC-018:
  `docs/reference/CVF_GC018_QBS6_HARD_GATE_REMEDIATION_CANDIDATE_2026-05-10.md`
- Roadmap:
  `docs/roadmaps/CVF_QBS6_HARD_GATE_REMEDIATION_ROADMAP_2026-05-10.md`
- Public commit pushed:
  `4e37e86 Remediate QBS hard-gate failures`
- Public remediation note:
  `docs/benchmark/qbs-1/hard-gate-remediation-qbs6.md`
- Runtime remediation delivered:
  - `/api/execute` safety-filter blocks now include `governanceEvidenceReceipt`
    with decision `BLOCK`;
  - `evaluateEnforcement()` now uses declared `cvfRiskLevel` when evaluating
    risk instead of relying only on risk markers in prompt text;
  - R2 sensitive/access-boundary patterns now escalate to `NEEDS_APPROVAL` in
    governed mode.
- Added public targeted tests:
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.qbs-hard-gates.test.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.qbs-hard-gates.test.ts`
- Verification:
  - `npm run test:run -- src/lib/enforcement.qbs-hard-gates.test.ts src/app/api/execute/route.qbs-hard-gates.test.ts`
    PASS, 5/5.
  - Live remediation smoke PASS using local ignored env: allowed governed path
    returned receipt `ALLOW`; safety-filter path returned receipt `BLOCK`;
    R2 sensitive and R2 external-scope cases returned `NEEDS_APPROVAL`.
  - `npm run build` PASS.
  - `python scripts/check_public_surface.py` PASS.
  - `git diff --check` PASS.
  - targeted raw-key scan: no matches.
- Remaining QBS boundary:
  QBS5 remains `EXECUTION_FAILED_NO_QBS_SCORE`; QBS6 does not alter that
  artifact and does not create a new scored rerun or QBS score.
- F7 ambiguous non-coder tasks:
  treated as benchmark entrypoint mismatch, not patched in `/api/execute`.
  Future rerun must either route these through the intent-first front door /
  clarification loop or pre-register a revised direct-execute corpus contract.
- Recommended next track:
  `QBS7-RERUN-PREREGISTRATION`, requiring a fresh GC-018 and a new run-set tag
  after the F7 entrypoint decision is made.

QBS-7 rerun pre-registration:

- Operator asked for "next track" after QBS6.
- GC-018:
  `docs/reference/CVF_GC018_QBS7_RERUN_PREREGISTRATION_CANDIDATE_2026-05-10.md`
- Roadmap:
  `docs/roadmaps/CVF_QBS7_RERUN_PREREGISTRATION_ROADMAP_2026-05-10.md`
- Public commit pushed:
  `361ff91 Preregister QBS rerun packet`
- Public pre-registration tag pushed:
  `qbs/preregister/qbs1-powered-single-provider-20260510-alibaba-r2`
- Tag SHA:
  `361ff91fb441b4fef1bdc4f9a7d78f0ed8a2a5e4`
- Public run ID:
  `qbs1-powered-single-provider-20260510-alibaba-r2`
- Public packet:
  - `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba-r2.md`
  - `docs/benchmark/qbs-1/provider-model-manifest.qbs1-powered-single-provider-20260510-alibaba-r2.json`
  - `docs/benchmark/qbs-1/config-prompt-manifest.qbs1-powered-single-provider-20260510-alibaba-r2.json`
  - `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba-r2.md`
  - `docs/benchmark/qbs-1/rerun-plan-qbs7.md`
- F7 entrypoint decision:
  `QBS1-F7-T01` through `QBS1-F7-T06` keep expected decision `CLARIFY`, but
  valid R2 `CFG-B` evidence must use the intent-first front door plus
  clarification loop before any execute handoff can count. Direct
  `POST /api/execute` evidence alone is invalid for those F7 rows.
- Readiness checker updated so `-r2` preregistration tags report public status
  `QBS7_RERUN_PREREGISTERED_NO_SCORED_RUN`.
- Validation:
  - `python scripts/check_qbs_scored_run_readiness.py --json --require-preregistration --preregistration-tag qbs/preregister/qbs1-powered-single-provider-20260510-alibaba-r2`
    PASS, no warnings.
  - `python scripts/check_public_surface.py` PASS.
  - `python -m py_compile scripts/check_qbs_scored_run_readiness.py` PASS.
  - `git diff --check` PASS.
  - targeted raw-key scan over public benchmark/evidence/checker files: no
    matches.
- Boundary:
  QBS7 is doc/tag preregistration only. It does not execute a live rerun, does
  not score QBS, does not prove L4/L5/L6, does not create provider parity, and
  does not change the QBS5 failed/no-score result.
- Recommended next track:
  `QBS8-RERUN-EXECUTION`, requiring explicit operator authorization for live
  provider cost, credential availability, stop conditions, browser/session
  stability, and reviewer readiness.
