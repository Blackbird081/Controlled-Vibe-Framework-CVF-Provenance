# CVF VI5 Surface Fidelity Codex Response

Memory class: REVIEW_RESULT_RECORD

docType: review

Date: 2026-05-26

Status: SURFACE_FIDELITY_PIVOT_RECORDED_PENDING_OPERATOR_DECISION

Authors:

- Codex (surface-fidelity audit, Part 6 response, template update)
- Operator (authority and surface correction)
- Claude Opus 4.7 (source concept synthesis)

---

## Purpose

Respond to Part 6 of
`docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
and record the corrected VI5 target after the operator clarified that the
actual HOLD verdict referred to Surface 1 web export spec, not Surface 2 T2
`englishSpecFreeze`.

This packet also records the docs-only amendment to
`docs/reference/CVF_MULTI_ROLE_ORCHESTRATED_CONVERGENCE_CAPTURE_FORM_2026-05-25.md`
adding Section 0 Surface Fidelity Gate.

## Scope / Methodology

Scope:

- Answer whether Codex's earlier English Spec reliability premise was verified
  for Surface 1, Surface 2, both, or neither.
- Verify the two app-builder exported markdown artifacts present in the repo
  root.
- Update the convergence template with a Surface Fidelity Gate so the next
  convergence loop does not evaluate the wrong artifact.

Method:

- Read the active handoff and the two 2026-05-26 concept docs.
- Search both `cvf-spec-app_builder_complete-full.md` and
  `cvf-spec-app_builder_complete-full 2.md` for Vietnamese chrome/leak
  evidence.
- Compare Surface 1 evidence with the known VI5-T2 Surface 2 proof boundary.
- Avoid re-auditing the operator's HOLD verdict via persona simulation.

## Source-Fidelity Block

Existing paths verified:

- `AGENT_HANDOFF_V13_2026-05-25.md`
- `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
- `docs/concepts/CVF_CROSS_AGENT_MEMORY_AND_AUTO_LOAD_ASSESSMENT_2026-05-26.md`
- `cvf-spec-app_builder_complete-full.md`
- `cvf-spec-app_builder_complete-full 2.md`
- `docs/reference/CVF_MULTI_ROLE_ORCHESTRATED_CONVERGENCE_CAPTURE_FORM_2026-05-25.md`
- `docs/reviews/CVF_VI5_T3_CLAUDE_ACCEPTANCE_OF_CODEX_SOLUTION_2026-05-26.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-english-freeze.ts`

Surface identities:

| Surface | Artifact | Audience | Current disposition |
|---|---|---|---|
| Surface 1 | Web export markdown spec | Non-coder and external agent | Real blocker; English-mode export leaks Vietnamese chrome |
| Surface 2 | `/api/execute` `englishSpecFreeze` JSON field | CVF-aware agent / Engine Room | T2 English-freeze integrity proven; not the operator HOLD surface |

Missing or ambiguous fact:

- Exact web-export source renderer path still needs code tracing before any
  implementation tranche. The exported markdown files are enough to identify
  the wrong-target convergence issue, but not enough to implement a fix.

## Evidence Trace Block

### Claim 1: Surface 1 English-mode export contains Vietnamese leak

- Claim: `cvf-spec-app_builder_complete-full 2.md` is not clean English.
- Source read: `cvf-spec-app_builder_complete-full 2.md`.
- Evidence: `rg` matched Vietnamese chrome and protocol lines including
  `Template: Tạo Ứng dụng Hoàn chỉnh`, Vietnamese template description,
  Vietnamese field labels, Vietnamese user values, and protocol phrases such
  as `đúng rồi`.
- Result: English-mode web export still contains unintended Vietnamese
  chrome/structure. User-entered Vietnamese values may be valid source data,
  but Vietnamese labels/headings/protocol text are surface i18n coverage gaps.
- Verdict: EXISTS.

### Claim 2: Surface 2 T2 is not the operator HOLD artifact

- Claim: VI5-T2 `englishSpecFreeze` is a server-side JSON response field for
  CVF-aware agents, not the downloadable web export reviewed by the operator.
- Source read:
  `docs/concepts/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md`
  Part 2 and related source list.
- Result: the concept doc explicitly separates Surface 1 web export spec from
  Surface 2 T2 `englishSpecFreeze`.
- Verdict: EXISTS.

### Claim 3: Previous VI5-T3 convergence targeted the wrong surface

- Claim: `docs/reviews/CVF_VI5_T3_CLAUDE_ACCEPTANCE_OF_CODEX_SOLUTION_2026-05-26.md`
  converged on server-side portable handoff readiness, not Surface 1 web export
  i18n leakage.
- Source read: target and purpose sections of that review packet.
- Result: the packet targets
  `docs/reviews/CVF_VI5_T3_CODEX_REBUTTAL_AND_SOLUTION_TO_CLAUDE_2026-05-25.md`,
  which is centered on `specHandoffReadiness`, `portableAgentPacket`, and
  `localizedHandoffGuide` for the T2/server-side handoff path.
- Verdict: EXISTS.

### Claim 4: The convergence template lacked a surface gate

- Claim: the existing multi-role convergence form started at `## 1. Trigger`
  and had no required Surface Fidelity Gate.
- Source read:
  `docs/reference/CVF_MULTI_ROLE_ORCHESTRATED_CONVERGENCE_CAPTURE_FORM_2026-05-25.md`.
- Result: Section 0 was absent before this packet's docs-only amendment.
- Verdict: EXISTS.

## Findings / Position

### Finding 1: Part 6 Answer

Codex's earlier English Spec reliability premise was **not verified for Surface
1 web export**.

Strict answer:

```text
Surface 1: not verified; counter-evidence now exists in the English-mode web export.
Surface 2: English-only freeze integrity was verified for T2.
Both surfaces: not verified.
External-agent reliability: not proven for either surface by a copy-paste external-agent test.
```

Therefore the statement "agents read English Spec more reliably" should be
treated as a general product intuition, not a surface-specific evidence claim.
The only hard proof in T2 is English-freeze integrity for Surface 2, not
external-agent execution reliability and not web-export cleanliness.

### Finding 2: VI5-T3 Must Not Be Dispatched As Previously Converged

The 2026-05-25/26 VI5-T3 convergence is now marked wrong-target for the
operator HOLD blocker. Its proposed server-side readiness fields may still be
useful later, but they do not fix the actual artifact the operator reviewed.

Disposition: HOLD previous VI5-T3 implementation.

### Finding 3: The Immediate Product Blocker Is Surface 1 Web Export I18n

The actual next product tranche, if operator chooses to fix the HOLD blocker,
should be a Surface 1 web export i18n coverage tranche, not T2 portable
handoff readiness.

Candidate scope, pending operator decision:

- identify the web export markdown renderer;
- separate user-entered values from chrome/labels/protocol text;
- add English coverage for template metadata, field labels, headings, and
  guided-agent protocol text;
- add a leak detector that marks `chrome_language_leak=true` when declared
  output language is English but Vietnamese chrome remains;
- prove with the app-builder complete export in English mode.

### Finding 4: Cross-Agent Memory Options Remain Pending

`docs/concepts/CVF_CROSS_AGENT_MEMORY_AND_AUTO_LOAD_ASSESSMENT_2026-05-26.md`
is proposed and awaiting operator decision. No Alpha/Beta/Gamma/Delta
implementation is dispatched by this packet.

## Risk / Corrective Action

Risk 1: Agents continue VI5-T3 implementation from the previous convergence
packet.

Corrective action: active state and handoff should mark previous VI5-T3 as
HOLD_WRONG_TARGET and require operator decision before any implementation.

Risk 2: Agents overcorrect by deleting Surface 2 work.

Corrective action: preserve T2 as `CLOSED_PASS_BOUNDED` for Surface 2 English
freeze integrity. The defect is target selection, not T2's internal claim.

Risk 3: Web-export i18n implementation might translate user-entered data.

Corrective action: future tranche must classify leaks as chrome/labels/protocol
text only. User data is source evidence and must be preserved unless the user
explicitly asks for translation.

Risk 4: Section 0 Surface Fidelity Gate becomes ceremony without verification.

Corrective action: every future convergence packet must list source path, output
surface, audience, language layer, generation trigger, and operator verdict path
before role outputs.

## Decision / Recommendation / Disposition

Decision:

- Previous VI5-T3 convergence targeted Surface 2 and is therefore not valid as
  the fix for the operator's Surface 1 HOLD blocker.
- Codex's English Spec reliability claim was not verified for Surface 1.
- Surface 2 T2 remains valid only as a bounded internal English-freeze proof.
- The convergence form now includes Section 0 Surface Fidelity Gate.

Recommendation:

- Do not dispatch VI5-T3 implementation.
- Ask operator to decide whether to pivot the next tranche to Surface 1 web
  export i18n coverage.
- Keep cross-agent memory options pending until operator selects Alpha/Beta/
  Gamma/Delta or defers.

Disposition: pending operator decision.

## Operator Delivery Packet

Operator decision needed:

- `ACCEPT_WEB_EXPORT_I18N_PIVOT`: open a fresh Surface 1 web export i18n
  coverage roadmap/GC-018.
- `HOLD`: request more evidence about the web export renderer before roadmap.
- `DEFER`: do not fix Surface 1 now; keep HOLD unresolved.
- `RETURN_TO_T2_VI5_T3`: explicitly choose to continue server-side T2 portable
  handoff readiness despite it not fixing the current web export blocker.

Cross-agent memory decision remains separate:

- Alpha / Beta / Gamma / Delta / Defer per
  `docs/concepts/CVF_CROSS_AGENT_MEMORY_AND_AUTO_LOAD_ASSESSMENT_2026-05-26.md`.

## Downstream Dispatch Rules

No implementation is authorized by this packet.

If operator accepts web export i18n pivot:

- Create fresh roadmap and GC-018.
- First task must identify the source renderer for Surface 1.
- Tests must distinguish user data from chrome leakage.
- Live/browser export proof is required only if the tranche claims user-facing
  web-export behavior. Static artifact tests may be used for renderer
  deterministic coverage.

If operator accepts memory Option Alpha/Beta/Gamma:

- Create separate GC-018 scoped to the selected option.
- Do not combine memory auto-load work with Surface 1 i18n work.

## Claim Boundary

This packet does not claim:

- web export renderer fix;
- VI5-T3 implementation;
- cross-agent memory option implementation;
- external-agent reliability proof;
- hosted/public/production readiness;
- provider/model/prompt/receipt changes;
- semantic translation quality;
- operator HOLD resolution.

It only records the corrected surface-fidelity answer and updates the
convergence template to prevent repeat wrong-target convergence.
