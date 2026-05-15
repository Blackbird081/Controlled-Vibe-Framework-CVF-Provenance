# CVF Agent Handoff V5 — Active Continuation

**Opened:** 2026-05-15  
**Reason:** `AGENT_HANDOFF_V4_2026-05-12.md` reached the governed markdown
advisory ceiling after the EVT-4 F-1 prompt-contract evidence tranche.

## Active Thread

Continue from commit `a1959a71`:

`Document and partially remediate EVT-4 quality gap`

## Current Priority

F-1 remains highest priority.

The prompt-contract layer improved the corrected EVT-4 gap but did not close
parity. Best retained evidence remains median `CFG-B - CFG-A = -0.16`, below
the preregistered `>= -0.05` rule.

Next authorized implementation direction from the previous handoff:

- Stop adding broad/global prompt instructions.
- Split narrow non-coder deliverable families for the remaining weak EVT-4
  shapes.
- Route the EVT-4 harness directly to those families for a new live comparison.

## F-1 Template-Family Split — 2026-05-15

User said "tiếp tục theo roadmap"; Codex started the next F-1 tranche.

Scope:

- Add bounded trusted form families:
  - `operator_plan`
  - `decision_memo`
  - `faq_outline`
  - `acceptance_criteria`
- Add narrow `TRUSTED_FORM_MAP` entries and activation coverage.
- Add exact output templates for those families.
- Update EVT-4 harness mapping so frozen tasks use the new family when the task
  shape is explicit.
- Run unit/type/lint verification and a live EVT-4 rerun.

Boundaries:

- No QBS rerun.
- No hard-gate or enforcement threshold change.
- No provider routing change.
- No output-validator change.
- No public repo push from the provenance workspace.
- Do not claim quality parity unless the live evidence meets the registered
  `>= -0.05` rule.

### Execution Update

Implemented:

- Added `operator_plan` and `decision_memo` to
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/business.ts`.
- Added `faq_outline` and `acceptance_criteria` to
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/content.ts`.
- Added narrow trusted-form routing entries for the four new families in
  `trusted-form-corpus.ts`.
- Added skill-template mappings for the four new families and also closed the
  pre-existing RULE-T4 mapping drift for `meeting_notes`, `job_description`,
  and `performance_review`.
- Updated trusted non-coder token budget / prompt-contract recognition.
- Updated EVT-4 harness mapping so explicit frozen tasks route to the new
  families.

Live evidence:

- `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TEMPLATE_FAMILY_SPLIT_EVIDENCE_2026-05-15.json`
- `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TEMPLATE_FAMILY_SPLIT_SUMMARY_2026-05-15.md`

Result:

- 20/20 live pairs completed.
- 20 CFG-B live receipts.
- 0 safety failures.
- Median `CFG-B - CFG-A = -0.16`.
- Registered decision rule `>= -0.05` was **not met**.

Verification:

- `node --check scripts/run_evt4_output_quality_ab.js` PASS.
- Focused unit set PASS (138/138).
- Template governance set PASS (169/169).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing `_request` warning in
  `src/app/api/system/jobs/route.test.ts`.

Current status:

- F-1 remains open. Do not claim parity.
- Family split alone is insufficient.
- The next bounded hypothesis should target family-specific depth/rubric
  improvements for `feature_prioritization`, `user_persona`, and
  `operator_plan`, because reviewer rationales now cite thin depth, weaker
  actionable detail, and missing verification steps rather than generic wrapper
  mismatch.

## F-1a Two-Pass Phase 0 Measurement — 2026-05-15

User approved coding the Claude-reviewed plan: measure two-pass quality
expansion before implementing any runtime feature.

Implemented in `scripts/run_evt4_output_quality_ab.js`:

- Added opt-in `EVT4_TWO_PASS_EXPANSION=true`.
- Default one-pass behavior remains unchanged.
- Experimental CFG-B path now runs:
  - Pass 1: existing governed `/api/execute`.
  - Pass 2: second governed `/api/execute` with `_previousOutput` and a
    quality-expansion intent.
- Evidence now records pass-1/pass-2 receipt presence, receipt IDs, duration,
  usage, output hashes, and excerpts.

GC / evidence:

- Review doc:
  `docs/reviews/CVF_GC018_EVT4_TWO_PASS_PHASE0_MEASUREMENT_2026-05-15.md`
- Evidence:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TWO_PASS_PHASE0_EVIDENCE_2026-05-15.json`
- Summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TWO_PASS_PHASE0_SUMMARY_2026-05-15.md`

Live result:

- 20/20 completed pairs.
- 20/20 CFG-B final receipts.
- 20/20 CFG-B expansion receipt pairs.
- 0 safety failures.
- Median `CFG-B - CFG-A = -0.16`.
- CFG-B median duration: `32217` ms.
- CFG-B median output tokens: `1966`.
- Decision rule `>= -0.05`: **false**.

Conclusion:

- Two-pass expansion is governance-feasible in the harness but does not close
  F-1.
- Do not implement runtime two-pass from this evidence.
- Next F-1 work needs a sharper task-specific evaluator/rubric or targeted
  family-contract repair for immediate actionability and specificity, not just
  more output length.

## F-1 Family Rubric Repair — 2026-05-15

User asked Codex to continue autonomously through the roadmap. Codex executed
the next bounded F-1 hypothesis:

`docs/reviews/CVF_GC018_EVT4_FAMILY_RUBRIC_REPAIR_2026-05-15.md`

Implementation:

- Repaired targeted family output contracts for:
  - `feature_prioritization`
  - `user_persona`
  - `operator_plan`
  - `competitor_review`
- Added exact sections for implementation steps, action plans, verification
  signals, operating checklists, and acceptance checks.
- No QBS, hard-gate, provider routing, output-validator, or runtime two-pass
  production change.

Verification:

- `npx vitest run src/lib/templates/governance-enforcement.test.ts src/lib/front-door-template-standard.test.ts src/lib/templates/index.test.ts src/lib/execute-prompt-contract.test.ts`
  PASS (42/42).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing `_request` warning in
  `src/app/api/system/jobs/route.test.ts`.

Live evidence:

- One-pass family-rubric repair:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_FAMILY_RUBRIC_REPAIR_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_FAMILY_RUBRIC_REPAIR_SUMMARY_2026-05-15.md`.
  Result: 20/20 receipts, 0 safety failures, median `-0.16`.
- Family-rubric repair plus two-pass expansion:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_RUBRIC_TWO_PASS_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_RUBRIC_TWO_PASS_SUMMARY_2026-05-15.md`.
  Result: 20/20 final receipts, 20/20 expansion receipt pairs, 0 safety
  failures, median `-0.16`.

Current F-1 conclusion:

- F-1 is still not closed.
- The worst outliers improved, but the median remains fixed at `-0.16`.
- Prompt, template, family split, and two-pass output shaping have hit a
  practical ceiling under the current EVT-4 scorer.
- Evidence shows CFG-B is **token-constrained**: median output tokens 1966–2048
  on a corpus that needs depth. The bottleneck is not model capability but
  system prompt size + budget allocation.

**Codex's recommended remediation path (highest probability of F-1 closure):**

1. **Lean Governed System Prompt for R0/R1 trusted noncoder**
   - Strip framework philosophy/doctrine from `CVF_SYSTEM_PROMPT`.
   - Preserve all governance constraints and safety directives.
   - Expected saving: ~200–300 tokens, freeing depth capacity.

2. **Selective Output Budget Increase**
   - Alibaba qwen-turbo: keep 2048 (stable, no regression signal).
   - DeepSeek V4 Pro: increase 2048 → 3072 or 4096.
   - Only for trusted noncoder EVT templates.
   - Update `execute-route-budget.ts` token tracking.

3. **Family-Specific Output Contracts (not just prompt wrappers)**
   - Current: prompt wrapper around generic skeleton.
   - Better: explicit per-family structure (sections, checks, depth signals).
   - Target weakest families: `feature_prioritization`, `user_persona`,
     `competitor_review`, `pricing_strategy`, `acceptance_criteria`.

4. **Output Validator → Quality Repair Hint (bounded scope)**
   - Current: pass/fail only on safety/format/length.
   - Addition: WARN-quality retry for trusted noncoder (missing depth signals).
   - Not full runtime rubric — scoped to EVT-like templates only.

**Recommended execution order:** 1 + 2 first (low risk, direct token fix).
Then 3 + 4 if needed.

**No new GC-018 needed** for steps 1–2 (system prompt tweak, budget config).
Steps 3–4 may need GC-018 if output shape semantics change.

**Exit criteria (same rule):** 20/20 live, 0 safety fails, median ≥ -0.05.

## F-2 Test Drift Cleanup — 2026-05-15

After F-1 bounded repair evidence showed no further prompt/template closure,
Codex moved to the next priority: close the pre-existing targeted test drift.

Implementation:

- `src/app/api/admin/knowledge/w117-cp4-integration.test.ts`
  - Updated the admin mock to a current scoped owner/break-glass-shaped session.
  - Queried writable knowledge chunks with the resolved org scope
    (`org_cvf`), matching current admin resource scoping.
- `src/lib/intent-router-evidence-parity.test.ts`
  - Removed stale data-analysis wizard parity assumption from the wizard-only
    parity fixture because trusted-form routing now intentionally wins for
    narrow `data_analysis` matches.
  - Kept parity coverage on unshadowed wizard starter keys.
- `src/lib/hooks/useModals.test.ts`
  - Updated expectation to the current single-shell-overlay modal contract:
    opening `quickStart` closes `apiKeyWizard`.

Verification:

- Targeted F-2 set:
  `npx vitest run src/app/api/admin/knowledge/w117-cp4-integration.test.ts src/lib/hooks/useModals.test.ts src/lib/intent-router-evidence-parity.test.ts src/lib/templates/governance-enforcement.test.ts`
  PASS (30/30).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing `_request` warning in
  `src/app/api/system/jobs/route.test.ts`.
- Full web test suite:
  `npm run test:run` PASS (200 test files, 2637 tests passed, 2 skipped).

Current F-2 conclusion:

- F-2 targeted drift is closed.
- No runtime governance behavior was changed for this cleanup.
- Remaining lint warning is pre-existing and outside the F-2 failure set.

## F-4 EVT Analytics Operator Surface — 2026-05-15

Codex resolved the owner question by reusing the existing Analytics
Dashboard/Governance Health surface rather than creating a separate operator
page. This keeps the surface local-first and avoids adding another navigation
destination.

Implementation:

- Added `src/lib/evt-operator-metrics.ts`.
  - Computes false-positive rate from append-only FP evidence records.
  - Computes task recovery and governance abandonment rates from local
    analytics events.
- Extended `GET /api/governance/false-positive-report`.
  - Authenticated operator sessions can now read aggregate FP stats.
  - No raw JSONL report contents are exposed in the UI response.
- Added `src/components/EvtGovernanceHealthPanel.tsx`.
  - Rendered inside Analytics Dashboard → Governance Health.
  - Shows observed reportable decisions, FP rate, task recovery rate, and
    abandonment rate with low-N/evidence-mode caveats.
- Updated Analytics Dashboard tests and false-positive API route tests.

Verification:

- `npx vitest run src/lib/evt-operator-metrics.test.ts src/app/api/governance/false-positive-report/route.test.ts src/components/AnalyticsDashboard.test.tsx`
  PASS (16/16).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing `_request` warning in
  `src/app/api/system/jobs/route.test.ts`.
- `npm run build` PASS. The first build attempt timed out at 5 minutes while
  still running; the rerun with a longer timeout completed successfully.

Current F-4 conclusion:

- F-4 is closed.
- Operators now have a UI surface for EVT false-positive and
  recovery/abandonment signals.
- The CLI analyzer remains useful for local evidence inspection, but it is no
  longer the only way to see the rates.

## F-3 ProcessingScreen Advisory Recheck — 2026-05-15

Codex rechecked the remaining advisory after F-2 and F-4 were closed.

Current status:

- `src/components/ProcessingScreen.tsx` remains at 783 lines.
- This is still above the 700-line advisory threshold for `frontend_component`
  and below the 1000-line hard threshold.
- The original boundary remains binding: do **not** extract pre-emptively.

Recommended extraction targets if the file is next touched:

- Extract the FP button block plus `falsePositiveReportState` state machine
  into `FalsePositiveReportButton`.
- Move `resolveApprovalSafeHint` to `src/lib/approval-hints.ts` with focused
  unit tests.

Current F-3 conclusion:

- F-3 remains advisory-only.
- No code change is recommended until `ProcessingScreen.tsx` is touched for a
  functional reason or approaches the hard 1000-line cap.

## F-1 Provider Model Screening — 2026-05-15

User asked to compare the three provider lanes and allowed OpenAI mini for
testing. Codex screened Alibaba, DeepSeek, and OpenAI with live keys and kept
the result bounded to EVT-4.

Implementation:

- `scripts/run_evt4_output_quality_ab.js`
  - Generalized from Alibaba-only to `EVT4_PROVIDER=alibaba|deepseek|openai`.
  - Added `EVT4_MODEL` override and provider-specific key resolution without
    printing raw keys.
  - Added OpenAI `max_completion_tokens` support for GPT-5-family models.
  - Added bounded provider timeout override for slow model rebaselines.
  - Treats direct-provider empty content as a failed pair instead of scoring it
    as valid output.
- `src/lib/ai-providers.ts` and `src/lib/ai/providers.ts`
  - OpenAI GPT-5/o-series compatible calls now use `max_completion_tokens`.
  - Alibaba/DeepSeek provider timeout remains 60s by default but can be raised
    with `CVF_AI_PROVIDER_TIMEOUT_MS` for governed rebaseline runs.
- `src/lib/ai/types.ts`
  - Canonical governed system prompt is now language-adaptive instead of
    forcing Vietnamese for English requests.
- `src/lib/execute-prompt-contract.ts`
  - Adds explicit response-language instruction derived from intent/input.
  - Adds checklist/acceptance-contract shaping and anti-fabrication guardrails.
- `src/app/api/execute/route.ts`
  - Successful-but-empty provider output now enters output validation and is
    retried/blocked instead of returning a successful empty response.

Evidence summary:

- Consolidated summary:
  `docs/assessments/CVF_EVT4_PROVIDER_MODEL_SCREENING_SUMMARY_2026-05-15.md`.
- OpenAI `gpt-5.4-mini` two-pass sample 5:
  median `-0.16`, not selected.
- Alibaba `qwen3.6-plus` latest smoke 2:
  median `-0.16`, not selected.
- DeepSeek `deepseek-v4-pro` full 20-pair rebaseline R2:
  `20/20` completed, `20/20` receipts, `0` safety failures, median `-0.08`.
  This is the best full-corpus lane but still below the preregistered F-1
  closure threshold `>= -0.05`.
- DeepSeek `deepseek-v4-pro` two-pass sample 5:
  median `-0.16`; two-pass is rejected for this lane.

Verification:

- `npx vitest run src/app/api/execute/route.test.ts src/lib/execute-prompt-contract.test.ts src/lib/ai-providers.test.ts src/lib/ai/providers.test.ts`
  PASS (103/103).
- `python scripts/run_cvf_release_gate_bundle.py --json` PASS.

Current F-1 conclusion:

- F-1 remains **not closed**.
- Recommended provider/model for the next attempt is DeepSeek
  `deepseek-v4-pro`, because it produced the strongest full-corpus result.
- Model choice alone is insufficient. The next narrow work should target the
  negative DeepSeek full-corpus lanes rather than switching to another model or
  enabling two-pass globally.

## F-1 Lean Prompt / DeepSeek Budget Remediation — 2026-05-15

User said "Xem handoff AGENT_HANDOFF_V5_2026-05-15 / Tiến hành theo roadmap".
Codex continued the F-1 remediation path from the provider/model screening
result.

Implementation retained:

- Replaced the server-side `CVF_SYSTEM_PROMPT` in
  `src/lib/ai/types.ts` with a lean governed prompt.
  - Preserves governance/safety, anti-bypass, secret-protection, final
    deliverable, and language-adaptive constraints.
  - Removes long framework philosophy, platform overview, and example
    interaction material from live provider context.
- Updated `resolveExecutionMaxTokens()` in `execute-route-budget.ts` to be
  provider/model aware.
  - Trusted noncoder templates stay at `2048` by default.
  - Explicit `deepseek` + `deepseek-v4-pro` trusted noncoder calls use `3072`.
  - `4096` was tested and rejected because it caused live timeout instability.
- Moved route budget resolution until after provider routing so the selected
  provider/model controls the token cap.
- Added route/budget/provider prompt tests.

Live evidence:

- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_LEAN_PROMPT_BUDGET_RERUN_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_LEAN_PROMPT_BUDGET_RERUN_SUMMARY_2026-05-15.md`
  - 4096-token attempt.
  - Completed 15/20.
  - 0 safety failures.
  - Median `-0.16`.
  - Rejected because several CFG-B calls timed out.
- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_LEAN_PROMPT_3072_RERUN_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_LEAN_PROMPT_3072_RERUN_SUMMARY_2026-05-15.md`
  - Completed 19/20.
  - 19 CFG-B live receipts.
  - 0 safety failures.
  - Median `-0.12`.
  - One CFG-A direct-provider empty-output failure.
  - F-1 closure rule not met.

Rejected follow-up hypothesis:

- GC note:
  `docs/reviews/CVF_GC018_EVT4_FAMILY_CONTRACT_REPAIR_R2_2026-05-15.md`
- Evidence:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_FAMILY_CONTRACT_R2_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_FAMILY_CONTRACT_R2_SUMMARY_2026-05-15.md`
- Result:
  - Completed 19/20.
  - 19 CFG-B live receipts.
  - 0 safety failures.
  - Median `-0.16`.
  - One CFG-A direct-provider empty-output failure.
- Conclusion: broad family-contract reshaping worsened the retained
  lean-prompt/3072 result, so those runtime contract changes were reverted.
  Keep the evidence packet as a rejected hypothesis.

Verification:

- Targeted tests after retained changes:
  `npx vitest run src/lib/execute-prompt-contract.test.ts src/app/api/execute/route.test.ts src/lib/ai/providers.test.ts`
  PASS (82/82).
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with the pre-existing `_request` warning in
  `src/app/api/system/jobs/route.test.ts`.
- `python scripts/run_cvf_release_gate_bundle.py --json` PASS.

Current F-1 conclusion:

- F-1 remains open. Do not claim parity.
- Retain lean prompt + DeepSeek V4 Pro 3072 budget because it is stable enough
  and better than 4096, but it still does not meet the preregistered
  `>= -0.05` rule.
- Prompt length and broad contract shaping are no longer the highest-probability
  closure path.
- Next recommended path: fix the EVT-4 harness/protocol reliability first
  (bounded retry for empty direct-provider CFG-A responses, without scoring
  empty outputs), then test a narrower per-task repair only if the completed
  20/20 rebaseline still shows the same negative families.

### Protocol Reliability Follow-up

Implemented:

- `scripts/run_evt4_output_quality_ab.js`
  - Added bounded `EVT4_DIRECT_EMPTY_RETRIES` for CFG-A direct-provider empty
    output.
  - Empty output is still never scored as valid; the runner retries and records
    retry attempts for successful CFG-A records.
  - Evidence config now records `directEmptyRetries`.

Verification:

- `node --check scripts/run_evt4_output_quality_ab.js` PASS.

Live evidence:

- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_LEAN_3072_DIRECT_RETRY_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_LEAN_3072_DIRECT_RETRY_SUMMARY_2026-05-15.md`
- Result:
  - Completed 19/20.
  - 19 CFG-B live receipts.
  - 0 safety failures.
  - Median `-0.12`.
  - Direct CFG-A retry recovered transient empty outputs on EVT4-08, EVT4-19,
    and EVT4-20.
  - New blocker: EVT4-09 CFG-B returned `422` after output-validation retry
    exhaustion.

Current follow-up conclusion:

- CFG-A empty-output flake is now bounded and observable.
- F-1 is still not closed.
- The next blocker is governed output validation / quality for the MVP-scope
  feature-prioritization lane, not provider blank output.

## F-1 Diminishing Returns Stop Rule — 2026-05-15

User explicitly agreed that low-value pursuit of perfection should stop rather
than consuming time and tokens indefinitely.

Guard added:

- `docs/reviews/CVF_F1_DIMINISHING_RETURNS_STOP_RULE_2026-05-15.md`
- `AGENTS.md` now contains the same stop rule as a mandatory agent-enforced
  instruction. Future agents must obey it without waiting for a human reminder.

Binding continuation rule:

- Do **not** continue broad prompt/template/model/token-budget tuning for F-1.
- Retain the current useful posture:
  - lean governed system prompt;
  - DeepSeek `deepseek-v4-pro` trusted noncoder cap at `3072`;
  - bounded CFG-A direct-empty retry;
  - family-contract R2 treated as rejected evidence.
- Only one bounded F-1 continuation remains recommended:
  1. fix the concrete EVT4-09 governed output-validation exhaustion if it is
     still reproducible;
  2. run one clean full rebaseline;
  3. if the registered rule still fails, close F-1 as
     `not met, evidence-backed` and move to higher-value CVF work.

Future agents must not rerun EVT-4 just hoping reviewer variance closes the
gap, must not increase token budget above the retained stable cap, and must not
reopen runtime two-pass or broad template reshaping without fresh evidence and
explicit user authorization.

## F-1 Closure — Not Met, Evidence-Backed — 2026-05-15

Codex followed the mandatory stop rule.

Diagnostic step:

- Added `EVT4_TASK_IDS` to `scripts/run_evt4_output_quality_ab.js` so a single
  frozen task can be diagnosed without rerunning unrelated tasks.
- Added CFG-B failure detail capture for `outputValidation`,
  `governanceEvidenceReceipt`, provider, and model on failed records.
- Ran EVT4-09 only:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_EVT409_VALIDATION_DIAG_EVIDENCE_2026-05-15.json`
  / summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_EVT409_VALIDATION_DIAG_SUMMARY_2026-05-15.md`
  - EVT4-09 did not reproduce the 422 in isolation.
  - Completed with local delta `-0.20`.

Final clean rebaseline:

- Evidence:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_FINAL_STOP_RULE_REBASELINE_EVIDENCE_2026-05-15.json`
- Summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_FINAL_STOP_RULE_REBASELINE_SUMMARY_2026-05-15.md`
- Result:
  - Completed `20/20`.
  - CFG-B live receipts `20/20`.
  - Safety failures `0`.
  - Median normalized delta `-0.08`.
  - Registered rule `>= -0.05` was **not met**.
  - CFG-A direct-empty retry recovered transient empty outputs on EVT4-01 and
    EVT4-02.

Closure packet:

- `docs/reviews/CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md`

Final F-1 status:

- F-1 is closed as `not met, evidence-backed`.
- Do not claim output-quality parity.
- Do not continue F-1 micro-tuning.
- EVT-4 remains useful as a regression benchmark after meaningful product-level
  changes, not as an open-ended tuning loop.

## Non-Coder Output Quality Hardening Roadmap — 2026-05-15

User confirmed the post-F-1 direction:

1. carry a bounded honest claim;
2. turn the gap into a product roadmap;
3. focus on real user pain: MVP scope, pricing, SOP/handoff, persona/actionability;
4. use EVT-4 as a regression benchmark, not an infinite tuning loop.

Added:

- Bounded claim:
  `docs/reviews/CVF_EVT4_BOUNDED_VALUE_CLAIM_2026-05-15.md`
- Product roadmap:
  `docs/roadmaps/CVF_NONCODER_OUTPUT_QUALITY_HARDENING_ROADMAP_2026-05-15.md`
- `AGENTS.md` now points future agents to both artifacts and says future
  output-quality work must proceed as product-level non-coder deliverable
  hardening, not F-1 parity tuning.

Roadmap tracks:

- QH-1: MVP Scope And Backlog Actionability.
- QH-2: Pricing Recommendation Actionability.
- QH-3: SOP And Handoff Procedural Depth.
- QH-4: Persona-To-Action Bridge.
- QH-5: Decision Memo Activation Steps.

Recommended next tranche:

- Start with QH-1 and QH-2 only after a fresh GC/review note.
- Do not run EVT-4 until there is a meaningful product-level change to regress.

## QH-1/QH-2 Non-Coder Output Hardening — Implemented, Mixed Regression — 2026-05-15

Codex executed the first bounded product-quality tranche after F-1 closure.

Pre-implementation review:

- `docs/reviews/CVF_GC018_QH1_QH2_NONCODER_OUTPUT_HARDENING_2026-05-15.md`

Implementation:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`
  now adds a `pricing` deliverable shape and makes `pricing` and
  `prioritization` shape-specific contracts primary when detected.
- QH-1 `feature_prioritization` now leads with:
  - `Do now / MVP`;
  - `Do next`;
  - `Defer`;
  - explicit non-goals;
  - first validation/build step;
  - owner/role;
  - acceptance check.
- QH-1 scoring matrix is now supporting evidence after the scope decision.
- QH-2 `pricing_strategy` now leads with concrete pricing recommendation:
  tiers/options, target user, included limits/features, price anchors or
  relative bands, first experiment, and risk/validation checks.
- Product and marketing template metadata were aligned so the catalogue no
  longer says scoring-first or broad theoretical pricing.

Static verification:

- `npx vitest run src/lib/execute-prompt-contract.test.ts src/lib/templates/index.test.ts src/lib/front-door-template-standard.test.ts src/lib/trusted-form-corpus.test.ts`
  PASS: `124/124`.
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing warning:
  `src/app/api/system/jobs/route.test.ts` unused `_request`.

Focused live evidence:

- Evidence:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH1_QH2_FOCUSED_EVIDENCE_2026-05-15.json`
- Summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH1_QH2_FOCUSED_SUMMARY_2026-05-15.md`
- Result:
  - Completed `2/2`.
  - CFG-B receipts `2/2`.
  - Safety failures `0`.
  - Median delta `-0.12`; parity decision rule not met.
  - EVT4-05 pricing tiers improved vs baseline delta `-0.20 -> -0.12`,
    CFG-B `0.72 -> 0.76`.
  - EVT4-09 MVP scope improved vs baseline delta `-0.20 -> -0.12`,
    CFG-B `0.72 -> 0.84`.

Full EVT-4 regression:

- Evidence:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH1_QH2_REGRESSION_EVIDENCE_2026-05-15.json`
- Summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH1_QH2_REGRESSION_SUMMARY_2026-05-15.md`
- Result:
  - Completed `20/20`.
  - CFG-B receipts `20/20`.
  - Safety failures `0`.
  - Median delta `-0.12` vs final stop-rule baseline `-0.08`.
  - Registered parity/no-degrade threshold not met.
  - EVT4-05 pricing tiers improved strongly: delta `-0.20 -> 0.20`,
    CFG-B `0.72 -> 1.00`.
  - EVT4-09 MVP scope improved modestly: delta `-0.20 -> -0.16`,
    CFG-B `0.72 -> 0.76`.
  - EVT4-14 backlog triage improved: delta `-0.28 -> -0.20`,
    CFG-B `0.72 -> 0.80`.
  - EVT4-11 pilot pricing stayed stable on CFG-B score: `0.76 -> 0.76`.
  - EVT4-18 freemium decision retained CFG-B `1.00`.

Result packet:

- `docs/reviews/CVF_QH1_QH2_NONCODER_OUTPUT_HARDENING_RESULT_2026-05-15.md`

Current claim:

- QH-1/QH-2 are implemented as bounded product deliverable hardening.
- Governance receipts and safety remain stable on EVT-4.
- Target lanes improved/stayed bounded, but full regression is mixed.
- Do **not** claim output-quality parity.
- Do **not** claim full no-degrade from this tranche.
- Do **not** rerun EVT-4 merely to chase reviewer/provider variance.

Recommended continuation:

- Commit this tranche.
- Next useful product work is QH-3 SOP/handoff, QH-4 persona-to-action, or
  QH-5 decision activation, each with fresh GC/review scope before code.

## QH-3 SOP/Handoff Procedural Depth — Implemented, Focused Mixed Improvement — 2026-05-16

Codex executed QH-3 as bounded product-quality hardening, not F-1 reopening.

Pre-implementation review:

- `docs/reviews/CVF_GC018_QH3_SOP_HANDOFF_PROCEDURAL_DEPTH_2026-05-16.md`

Implementation:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`
  now makes checklist/documentation outputs procedural runbooks with:
  - required inputs, artifacts, and fields;
  - step-by-step procedure;
  - decision branches;
  - QA checks;
  - common failure modes and recovery;
  - escalation rules;
  - final handoff acceptance checklist.
- The checklist guidance now keeps overview/assumptions short and prioritizes
  executable tables/checks to avoid spending the retained `3072` output cap on
  background prose.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/content.ts`
  documentation template was aligned to SOP/handoff runbook structure.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/business.ts`
  operator-plan template was aligned to first-72-hour procedure, operating
  cadence, QA checkpoints, failure modes, and escalation.

Static verification:

- `npx vitest run src/lib/execute-prompt-contract.test.ts src/lib/templates/index.test.ts src/lib/front-door-template-standard.test.ts src/lib/trusted-form-corpus.test.ts`
  PASS: `124/124`.
- `npx tsc --noEmit` PASS.
- `npm run lint` PASS with one pre-existing warning:
  `src/app/api/system/jobs/route.test.ts` unused `_request`.

Focused live evidence:

- Initial evidence:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH3_FOCUSED_EVIDENCE_2026-05-16.json`
- Initial summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH3_FOCUSED_SUMMARY_2026-05-16.md`
- Initial result:
  - Completed `3/3`.
  - CFG-B receipts `3/3`.
  - Safety failures `0`.
  - Median delta `-0.16`.
  - EVT4-08 ops plan improved strongly, but EVT4-12 SOP regressed because the
    first run spent too much space on overview/assumptions and hit output cap.

Bounded refinement:

- Kept QH-3 structure, shortened front matter, and emphasized executable
  procedure/QA/recovery tables.

Focused R2 evidence:

- Evidence:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH3_FOCUSED_R2_EVIDENCE_2026-05-16.json`
- Summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_QH3_FOCUSED_R2_SUMMARY_2026-05-16.md`
- Result:
  - Completed `3/3`.
  - CFG-B receipts `3/3`.
  - Safety failures `0`.
  - Median delta `-0.12`.
  - Registered parity decision rule not met.
  - EVT4-07 builder handoff improved vs QH-1/QH-2 CFG-B `0.68 -> 0.84`.
  - EVT4-08 ops plan improved vs QH-1/QH-2 CFG-B `0.68 -> 0.80`.
  - EVT4-12 SOP draft stayed stable vs QH-1/QH-2 CFG-B `0.84 -> 0.84`.

Result packet:

- `docs/reviews/CVF_QH3_SOP_HANDOFF_PROCEDURAL_DEPTH_RESULT_2026-05-16.md`

Current claim:

- QH-3 is implemented as bounded procedural-depth product hardening.
- Governance receipts and safety remain stable on focused QH-3 evidence.
- Do **not** claim F-1 parity.
- Do **not** claim full EVT-4 no-degrade.
- Do **not** rerun full EVT-4 until another meaningful product tranche is
  implemented.

Recommended continuation:

- Commit this tranche.
- Next highest-value tranche: QH-5 decision memo activation.
