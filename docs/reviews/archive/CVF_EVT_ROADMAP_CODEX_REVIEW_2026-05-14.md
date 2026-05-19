# CVF EVT Roadmap Codex Review - 2026-05-14

**Status:** CODEX REVIEW RECORDED - USER APPROVAL STILL REQUIRED PER TRACK
**Reviewed roadmap:** `docs/roadmaps/CVF_EVT_END_USER_VALUE_ROADMAP_2026-05-13.md`
**Reviewer:** Codex
**Scope:** Critical review of EVT-1 through EVT-4 before implementation
**Repository boundary:** Provenance workspace only. No public push from this clone.

---

## 1. Review Verdict

The EVT roadmap is directionally correct and should remain the next end-user
value frontier after EA completion. It correctly identifies that EA Tracks A-E
improved operator and infrastructure value, while CVF still lacks direct evidence
for the person submitting prompts.

However, the roadmap should **not be executed exactly as written**. It needs a
small scoping correction before implementation:

1. EVT-1 should log false-positive reports as separate events linked to a
   receipt. It should not mutate the evidence receipt itself.
2. EVT-1's UI surface should be `ProcessingScreen`, not primarily `ResultViewer`,
   because BLOCK/CLARIFY/NEEDS_APPROVAL responses do not normally reach the
   success-result viewer.
3. EVT-3 should be framed as audit + hardening of an existing approval UX, not as
   a greenfield UX. `ProcessingScreen` already displays pending approval context.
4. EVT-2 should first measure the actual current `/api/execute` pipeline. The
   roadmap's "intent classification" bottleneck hypothesis may not match the
   current route implementation.
5. The handoff wording should treat the roadmap as having 5 open questions: 4
   track questions plus 1 meta-question.

Implementation may begin only after the user explicitly approves a specific
track. EVT-2 optimization that changes execution order and EVT-4 still require
fresh GC-018.

---

## 2. Code-Reality Checks

The current governed execution path is under:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ResultViewer.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`

Observed implementation facts:

- `GovernanceEvidenceReceipt` is a point-in-time evidence object with fields such
  as `receiptId`, `decision`, `riskLevel`, `provider`, `model`, `approvalId`, and
  `generatedAt`.
- `/api/execute` already returns receipts for BLOCK, CLARIFY, NEEDS_APPROVAL,
  router denial, output validation failure, and successful execution.
- `ProcessingScreen` receives failed execution responses and handles
  CLARIFY/BLOCK/NEEDS_APPROVAL UI states.
- `ResultViewer` is mostly a success-output surface, with export and evidence
  display for completed outputs.
- NEEDS_APPROVAL already auto-creates an approval record and shows a pending
  review panel with request id and admin-review language.

Implication: EVT-1 and EVT-3 are feasible, but the roadmap should target the
actual error-state surface and existing approval flow.

---

## 3. Track-Specific Review

### EVT-1 - False Positive Audit

Recommendation: **approve after scope correction**.

Do not add `falsePositiveReported: boolean` directly to
`GovernanceEvidenceReceipt`. That would blur evidence semantics: a receipt should
record what CVF decided at execution time, while a false-positive report is a
later user claim about that decision.

Preferred event shape:

```json
{
  "eventType": "FALSE_POSITIVE_REPORTED",
  "reportedAt": "ISO8601",
  "receiptId": "rcpt-...",
  "envelopeId": "env-...",
  "decision": "BLOCK|CLARIFY",
  "riskLevel": "R0|R1|R2|R3|R4",
  "reason": "safe compact reason or reason code",
  "templateId": "optional",
  "actorId": "optional hashed/session-bound id",
  "userComment": "optional bounded text"
}
```

UI placement:

- Show the button after BLOCK and CLARIFY in `ProcessingScreen`.
- Do not show it for ALLOW.
- Do not show it for NEEDS_APPROVAL in EVT-1 unless the product decision is to
  classify approval-gating complaints as a separate metric. NEEDS_APPROVAL is a
  different user pain than a false positive block/clarification.

Admin notification:

- Use passive log only for EVT-1.
- Add admin notification/review queue only after there is enough report volume to
  justify operational noise.
- If a review queue is later added, it must not auto-unblock, auto-approve, or
  bypass governance.

Exit criteria additions:

- Test that receipt content remains immutable.
- Test that duplicate clicks either de-duplicate by `receiptId` or record a
  bounded duplicate-safe event.
- Analyzer should report numerator, denominator, and low-N caveat.

### EVT-2 - Governance Latency Optimization

Recommendation: **measure first; do not optimize before real data**.

The proposed parallelization question is valid, but the roadmap's suspected
bottleneck may not match the current implementation. The route currently builds
the execution prompt, runs DLP, then evaluates enforcement and guards. It accepts
`intent` from the request rather than obviously doing a heavy model-based intent
classification inside `/api/execute`.

Answer to the DLP + intent parallelization question:

- Parallelizing pure local computations is not automatically a governance
  violation.
- It becomes risky if either branch emits audit events, persists decisions, calls
  a provider, or exposes unredacted content before DLP completes.
- The final audit trail must preserve a deterministic logical order even if
  internal measurement/compute is concurrent.
- If DLP detects sensitive data, any downstream result that used unredacted
  content must be discarded and must not be externally visible.
- Any execution-order change that changes evidence semantics requires GC-018.

Recommended EVT-2 split:

1. EVT-2.1: collect real tax logs from current route with no ordering changes.
2. EVT-2.2: only optimize AMBER/RED phases.
3. EVT-2.3: if optimization changes ordering, write GC-018 before implementation.

### EVT-3 - NEEDS_APPROVAL UX Improvement

Recommendation: **approve as audit + hardening, not greenfield UX**.

Current UX already includes:

- auto-created approval id,
- pending review status,
- admin-review explanation,
- retry-after-approval guidance.

The roadmap should therefore audit what is already present and improve only the
gaps. Likely useful hardening:

- Make the 24-hour expiry visible if it is product-approved.
- Clarify whether the user should wait, contact an admin, or check the approvals
  page.
- Preserve the approval id and receipt id in copyable form.
- Add a safe "what happened" explanation that does not expose rule patterns.

Rewrite suggestion risk:

- High risk if the hint tells users which pattern triggered governance or how to
  reword around it.
- Acceptable if the hint only suggests safe product behavior: narrow scope, add
  context, remove unrelated high-risk actions, or submit for review.
- If the system cannot generate a safe hint deterministically, omit the hint and
  show only context.

Safe examples:

- "You can submit this for review, or narrow the request to a lower-risk planning
  step."
- "Add the business context and intended reviewer so an admin can evaluate it."

Unsafe examples:

- "Remove the phrase that triggered R3."
- "Avoid mentioning approval, bypass, or production deployment."
- "Reword the request so the detector does not classify it as high risk."

### EVT-4 - Output Quality A/B Baseline

Recommendation: **keep, but preregister protocol before running**.

EVT-4 is not a QBS rerun and should stay separate while QBS is temporarily
closed. It answers a different product question: whether CVF-governed output is
meaningfully worse than a bare provider call for end-user tasks.

Protocol requirements before execution:

- Fresh GC-018.
- User-approved prompt set.
- Predefined acceptable delta threshold.
- Predefined task families.
- Reviewer rubric committed before any scored run.
- Clear statement that R0/R1 baseline does not prove behavior for R2/R3/R4.

If CFG-B < CFG-A:

- Small, localized deltas should trigger prompt/template/output-contract tuning.
- Repeated deltas across task families should trigger a bounded redesign cycle.
- It is an architecture problem only if the governance layer systematically
  degrades usefulness even when no high-risk intervention is needed.

Sample size:

- 20 prompts is acceptable only as a pilot baseline.
- For a stronger claim, use more prompts per task family and report confidence
  intervals.

Reviewer model:

- A single strong reviewer can be used for a pilot, but do not overclaim.
- For public/business claims, use at least two reviewers or one reviewer plus
  calibration/adjudication evidence.

---

## 4. Missing End-User Value Track

Add or defer a fifth candidate track:

**EVT-5 - Task Recovery / Abandonment Baseline**

Question: after CLARIFY, BLOCK, or NEEDS_APPROVAL, does the user eventually
complete the task?

Why it matters:

- False-positive rate measures whether users think CVF was wrong.
- Latency measures waiting.
- Output quality measures answer usefulness.
- Recovery/abandonment measures whether the product actually helps users finish
  work despite governance friction.

Candidate metrics:

- CLARIFY recovery rate.
- BLOCK safe-path follow-through rate.
- NEEDS_APPROVAL resumed-execution rate.
- Time from governance stop to successful completion.

This track can be deferred, but it is the most important missing end-user value
gap in the current roadmap.

---

## 5. Priority Recommendation

For a 5-10 person team deploying CVF:

1. EVT-1 and EVT-3 are highest priority because they address immediate user
   friction and trust.
2. EVT-2 should start as measurement only, then optimize if real live traffic is
   AMBER/RED.
3. EVT-4 is strategically important but should wait for GC-018 and preregistered
   scoring protocol.
4. EVT-5 should be added as a candidate follow-up or merged into EVT-1/EVT-3
   analytics if implementation bandwidth is tight.

---

## 6. Binding Notes For Next Agent

- Do not implement EVT until the user approves the specific track.
- Do not reopen QBS from EVT-4. QBS remains temporarily closed unless the user
  explicitly reopens it under the existing handoff conditions.
- Do not add false-positive state directly into immutable governance evidence
  receipts.
- Do not expose R2/R3/R4 trigger patterns in user-facing rewrite hints.
- Do not parallelize or reorder governance phases without first documenting
  whether audit semantics change.
- If a public-facing change is needed, switch to the public-sync clone and verify
  `git remote -v` before any public push.
