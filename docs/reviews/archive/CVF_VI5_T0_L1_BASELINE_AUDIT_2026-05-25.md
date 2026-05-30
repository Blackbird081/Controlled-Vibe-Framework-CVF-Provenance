# CVF VI5-T0 L1 Baseline Audit

Memory class: REVIEW_RESULT_RECORD

docType: review

Date: 2026-05-25

Status: CLOSED_PASS_BASELINE_RECORDED

## Purpose

Record the empirical baseline for L1 `specFirstMediation.normalizedExecutionSpec`
before VI5-T1 implementation begins.

This audit determines whether VI5-T1 may truthfully claim the current Spec body
is English-only. It does not change runtime behavior.

## Scope / Target / Owner Boundary

Target: one live Vietnamese Strategy `/api/execute` request using the existing
L1 `cvf.specFirstMediation.l1.v1` readout.

Owner surface: VI5 convergence and baseline audit.

Out of scope:

- Spec English freeze implementation;
- route behavior changes;
- provider adapter changes;
- prompt tuning;
- presentation catalog implementation;
- Real Non-Coder Usage Test PASS;
- production, hosted, public, or freeze-release claims.

## Source-Fidelity Block

- Existing paths verified:
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-first-mediation.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  - `docs/reviews/CVF_VI5_MULTI_ROLE_CONVERGENCE_CLAUDE_ACCEPTANCE_2026-05-25.md`
  - `docs/reference/CVF_MULTI_ROLE_ORCHESTRATED_CONVERGENCE_CAPTURE_FORM_2026-05-25.md`
- Planned new paths clearly marked as NEW:
  - this audit packet
- Missing or ambiguous source fact: none.

## Evidence Trace Block

- Claim: current L1 `normalizedExecutionSpec` is not English-only for a
  Vietnamese Strategy request.
- Command:
  `npm run test:run -- src/app/api/execute/route.vi5-t0-l1-baseline.alibaba.live.test.ts`
- Result: PASS after one classified harness correction; live receipt
  `rcpt-env-mpl4ct9q-fdm2xr`; provider/model `alibaba/qwen-turbo`;
  `specFirstContract=cvf.specFirstMediation.l1.v1`;
  `sourceLanguage=vi`; `workingLanguage=en`; `outputLanguage=vi`;
  `originalPromptPreserved=true`; `observedSpecBodyLanguage=mixed`;
  `normalizedExecutionSpecLength=4309`.
- Key path:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-first-mediation.ts`
- Verdict: EXISTS.
- Counter-evidence: none.

- Claim: first T0 live attempt failed before provider execution due to
  request-harness authority wording, not provider/model failure.
- Command:
  `npm run test:run -- src/app/api/execute/route.vi5-t0-l1-baseline.alibaba.live.test.ts`
- Result: first attempt returned `http=400`, `success=false`,
  `guard=BLOCK:authority_gate`, safe error "We need to adjust your request
  for better results." The action text was changed from audit wording to an
  allowed Strategy analysis wording before rerun.
- Key path:
  temporary live test harness
- Verdict: CLASSIFIED_AND_RERUN_ALLOWED.
- Counter-evidence: none.

## Findings / Position

### Finding 1 - L1 T1 Is Foundation, Not Final English Freeze

The live baseline confirms Codex's concern: the current L1
`normalizedExecutionSpec` contains English structure and Vietnamese user/body
content.

Observed preview included:

```text
# CVF Execution Spec
- Entry mode: template_first
- Source language: vi
- Working language: en
- Output language: vi
- Template: Phân tích Chiến lược
...
## Context
Phân tích chiến lược kinh doanh, so sánh các phương án
...
Original prompt: Tôi cần phân tích chiến lược mở rộng CVF...
```

This is correctly classified as:

```text
observedSpecBodyLanguage = mixed
```

### Finding 2 - VI5-T1 Must Report, Not Enforce

VI5-T1 must not claim that the Spec body is already English-only.

The correct VI5-T1 fields are:

- `languageState.specContractLanguage = "en"`
- `specBoundary.observedSpecBodyLanguage = "mixed"` for this baseline
- `specBoundary.englishFreezeEnforced = false`

VI5-T2 should own any actual Spec English Freeze migration/enforcement.

### Finding 3 - Original Vietnamese Preservation Is Working

The live readout preserved original Vietnamese prompt and metadata:

- `sourceLanguage=vi`
- `workingLanguage=en`
- `outputLanguage=vi`
- `originalPromptPreserved=true`

This means VI5-T1 can build boundary/readout fields on top of L1 without
rewriting L1 generation.

## Risk / Corrective Action

Risk 1: future VI5 code may accidentally assert English-only Spec body.

Corrective action: VI5-T1 acceptance criteria must use the three-field
empirical split accepted by Claude:

- intent: `specContractLanguage`
- observed state: `observedSpecBodyLanguage`
- enforcement state: `englishFreezeEnforced`

Risk 2: live proof could be rerun blindly after the first `authority_gate`
failure.

Corrective action: the first failure was classified as
`test_harness_authority_wording`, retryable after payload correction, with no
evidence of provider/model failure.

Risk 3: Real Non-Coder Usage Test could be reopened too early.

Corrective action: keep Real Non-Coder Usage Test on hold until VI5-T1 adds
language state, guided step state, spec boundary, and Strategy catalog proof.

## Decision / Recommendation / Disposition

Decision: VI5-T0 CLOSED_PASS_BASELINE_RECORDED.

Recommendation: proceed to VI5-T1 GC-018 and work order with
`observedSpecBodyLanguage=mixed` as the current L1 baseline.

Disposition: baseline audit complete. VI5-T1 implementation remains
unauthorized until fresh GC-018 and work order are filed.

## Claim Boundary

This audit claims only one live L1 baseline result. It does not claim VI5-T1
implementation, English Spec freeze, Real Non-Coder Usage Test PASS, runtime
guided wizard support, UI i18n, hosted readiness, production readiness, or
freeze posture changes.
