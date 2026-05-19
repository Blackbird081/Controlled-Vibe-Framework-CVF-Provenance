# CVF GC-018 — EVT-4 Template Payload Diagnostic Rerun

**Date:** 2026-05-14  
**Status:** APPROVED BY USER FOR EXECUTION  
**Scope:** F-1 diagnostic correction for EVT-4 output quality evidence.

## Authorization

User asked to proceed from the active handoff findings after commit `95c95e6b`.
This GC-018 authorizes a narrow diagnostic rerun of EVT-4 after inspecting the
raw evidence and finding that the measurement harness sent all CFG-B executions
through the `documentation` template, even when the frozen task record carried
`strategy_analysis`, `feature_prioritization`, `user_persona`,
`pricing_strategy`, or `competitor_review`.

## Root-Cause Finding Before Code Change

The observed `CFG-B - CFG-A = -0.28` result is materially affected by the EVT-4
harness payload, not by QBS, hard-gate logic, provider routing, or output
validation. The harness recorded each task's intended `templateId` in evidence
metadata but `buildGovernedPayload()` hard-coded `templateId: 'documentation'`
for every governed CFG-B call. This explains why non-documentation tasks all
returned the generic "Operational Documentation Packet" wrapper.

## Allowed Work

- Update `scripts/run_evt4_output_quality_ab.js` so CFG-B uses each task's
  actual frozen `templateId`.
- Map task prompts into the required fields for the trusted form templates used
  by the frozen EVT-4 corpus.
- Preserve the original negative evidence artifact; write corrected rerun
  evidence under a new filename.
- Run the corrected live A/B harness with real DashScope-compatible provider
  calls and live `/api/execute` receipts.
- Update the active handoff with the corrected finding and any remaining
  quality gap.

## Boundaries

- No QBS rerun.
- No hard-gate or enforcement threshold change.
- No provider routing change.
- No runtime `CVF_SYSTEM_PROMPT` change.
- No output validator change.
- No template content rewrite unless a later GC-018 authorizes product runtime
  prompt-contract remediation after the corrected evidence is reviewed.
- No raw API keys printed or committed.

## Exit Criteria

- [x] Corrected harness payload uses task-specific `templateId`.
- [x] Corrected evidence file and summary file are published separately from
      the original EVT-4 artifacts:
      `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TEMPLATE_CORRECTED_EVIDENCE_2026-05-14.json`
      and
      `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TEMPLATE_CORRECTED_SUMMARY_2026-05-14.md`.
- [x] CFG-B live receipt count is recorded: 20/20.
- [x] Summary distinguishes the original documentation-wrapper artifact from
      any remaining true governed-output quality gap. Corrected rerun still
      failed the decision rule with median delta `-0.32`, proving the harness
      bug was real but not sufficient to explain the full F-1 gap.
