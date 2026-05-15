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
- Next owner-level decision should not be another prompt patch. Options:
  1. Define a sharper automated quality rubric and preregister closure against
     that rubric.
  2. Change the product claim to disclose the measured `-0.16` quality tradeoff
     while preserving audit/safety.
  3. Rebaseline on a stronger provider/model lane for both CFG-A and CFG-B with
     a fresh preregistered comparison.

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
