# CVF VI5-T4/T5 Operator Web Export HOLD Review - 2026-05-26

Status: HOLD

Memory class: REVIEW_PACKET

Surface: Surface 1 web export markdown from `https://vibcode.netlify.app/home`

## Purpose

Record the operator's first hosted Surface 1 export acceptance sample after
VI5-T4/T5 implementation, classify whether it can pass the parked operator
checkpoint, and prevent later agents from marking T4 PASS from inconsistent
export evidence.

## Target / Source

Target surface:

- Hosted `vibcode.netlify.app` Surface 1 markdown export.

Reviewed artifacts:

- `cvf-spec-app_builder_complete-full new.md`
- `cvf-spec-app_builder_complete-full new(1).md`

These files are local/operator export samples and remain untracked evidence
inputs, not governed product artifacts.

Reference implementation surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-export-portable-handoff.ts`

## Scope / Target / Owner Boundary

Owner surface: VI5-T4/T5 Surface 1 operator export acceptance.

In scope:

- Check whether the hosted English Guided/Full export contains the T4/T5
  portable handoff readiness block.
- Check whether the exported packet is internally consistent enough for an
  external coding agent to act.
- Record PASS / PASS_WITH_MINOR_FIX / HOLD disposition for this sample.

Out of scope:

- Implementing a hosted fix.
- Changing provider routing, MCP, receipt envelopes, workflow execution, or
  public product claims.
- Treating local untracked export samples as committed governed artifacts.

## Scope / Methodology

Method:

- Located the two new operator export files in the provenance workspace.
- Scanned both files for Vietnamese leakage, handoff readiness text, risk gate
  language, and export section structure.
- Compared the hosted English export against local source expectations for
  `buildPortableAgentHandoffReadiness()`.
- Classified contradictions that could cause a receiving external agent to
  stop, misunderstand source values, or bypass CVF control intent.

## Evidence Trace

| Claim | Evidence |
| --- | --- |
| The Vietnamese export exists and is internally Vietnamese-localized. | `cvf-spec-app_builder_complete-full new.md` uses Vietnamese chrome, protocol text, and user values. |
| The English export is improved but not T4/T5-ready. | `cvf-spec-app_builder_complete-full new(1).md` uses English protocol chrome but lacks the T4/T5 `Portable Agent Handoff Readiness` block. |
| Local source expects the missing block. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx` calls `buildPortableAgentHandoffReadiness()` and injects the result before `Task`; `spec-export-portable-handoff.ts` emits the block for `template.id=app_builder_complete`, `lang=en`, `mode=full`. |
| Hosted export and local expected behavior diverge. | Operator exported from hosted `vibcode.netlify.app`; resulting English file has no `Portable Agent Handoff Readiness`. |
| The export has a risk gate contradiction. | UI screenshot shows `Spec Gate: PASS — Ready to execute`, while the exported packet says `Risk Level R2`, `Max Risk R1`, `Risk Valid WARNING`, and mandates stop if risk exceeds R1. |

## Findings

### Finding 1 - Missing Portable Agent Handoff Readiness Block

Severity: high

The English Guided/Full export does not include the T4/T5 block that tells a
receiving external agent how to preserve Vietnamese source values, choose hidden
technical defaults, ask only material clarification questions, and produce an
operator-reviewable response.

This means the current hosted export must not be marked T4 PASS.

### Finding 2 - Risk Gate Contradiction

Severity: high

The UI claims `Spec Gate: PASS — Ready to execute`, but the packet itself says
`Risk Level R2`, `Max Risk R1`, and `Risk Valid WARNING`. A receiving agent can
reasonably stop instead of executing, because the packet also says risk above
R1 must stop and warn.

This is not just wording. It creates conflicting control instructions inside
the handoff.

### Finding 3 - English Export Still Has Vietnamese Control Labels

Severity: medium

Some Vietnamese source values are expected and should be preserved. However,
the English export still includes Vietnamese template title/description and
field labels such as `Tên app / sản phẩm`, `Đây là loại sản phẩm gì?`, and
`Nó giải quyết vấn đề gì?`.

This is acceptable only if the packet includes an explicit source-values
handling rule. Because the T4/T5 block is missing, the receiving agent gets less
help distinguishing source evidence from untranslated control chrome.

## Risk / Corrective Action

Risk if uncorrected:

- An external coding agent may stop on the R2 > R1 warning even though the UI
  says the spec is ready.
- An external coding agent may treat Vietnamese field labels as untranslated
  control chrome rather than source evidence.
- VI5-T4/T5 could be falsely marked PASS from a hosted export that does not
  include the readiness block proven in local tests.

Corrective action:

- Confirm hosted deploy contains the VI5-T4/T5 implementation.
- Re-export the English Guided/Full packet after deployment or export-path fix.
- Make UI gate and packet risk status agree before another operator acceptance
  test.

## Verdict

`HOLD`

Do not mark VI5-T4/T5 Surface 1 export acceptance PASS from these samples.

## Decision / Recommendation / Disposition

Decision: `HOLD_HOSTED_OPERATOR_EXPORT`

Recommendation:

Before asking the operator to retest:

1. Confirm whether hosted `vibcode.netlify.app` is deployed from a commit that
   includes VI5-T4/T5.
2. Export a fresh English `CVF Guided Agent (5-Phase)` packet and verify it
   contains `Portable Agent Handoff Readiness`.
3. Resolve the risk gate contradiction by making the UI gate and packet risk
   status agree.
4. Re-run operator/external-agent acceptance only after the exported packet is
   internally consistent.

Disposition:

- Vietnamese export: acceptable as localized user-facing packet sample.
- English export: not accepted for T4/T5 operator PASS.
- Hosted Surface 1 acceptance checkpoint remains open.

## Claim Boundary

This review records one operator-hosted export acceptance result only. It does
not change provider routing, MCP behavior, receipt envelopes, workflow
execution, public product claims, or production readiness.

## Verification

- Local source inspection and static export-file audit only.
- No hosted redeploy, browser automation, provider/API call, or external-agent
  acceptance run was performed in this review.
