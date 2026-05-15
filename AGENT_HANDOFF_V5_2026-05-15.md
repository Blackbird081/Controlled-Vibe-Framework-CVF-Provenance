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
