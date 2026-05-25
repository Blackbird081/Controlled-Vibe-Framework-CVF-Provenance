# CVF CDH-M Delta Codex Rebuttal

Memory class: FULL_RECORD

Status: REBUTTAL_FILED_NON_BLOCKING_WITH_PRIVACY_GATE

docType: review

Reviewer: Codex

Date: 2026-05-20

Reviewed artifact:
`docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md#per-slice-section-m`

---

## Status

Verdict: NON_BLOCKING_WITH_PRIVACY_GATE.

CDH-M may proceed to a slice-specific GC-018 and work order, but only as
deployment verification and evidence hardening for the already implemented
Maika text-summary path.

This rebuttal does not authorize implementation, Maika photo or vision work,
direct provider fallback, child-data proof, public-sync claims, or bundled CDH
closure.

## Purpose

Record Codex's reviewer-role disposition for the CDH-M delta slice so the next
agent can distinguish a valid Maika deployment-verification path from the
blocked broader CDH roadmap. The purpose is to preserve the useful downstream
work while preventing scope inflation into child-data, health, photo, provider,
or public-claim surfaces.

## Target Or Source Under Review

Primary planning source:

- `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`

Evidence and predecessor sources checked:

- `docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- `docs/reviews/archive/CVF_M1_MAIKA_TEXT_SUMMARY_COMPLETION_2026-05-19.md`
- `../CVF-Workspace/Nha tre Maika/supabase/functions/generate-daily-summary/index.ts`
- `../CVF-Workspace/Nha tre Maika/src/pages/admin/DailyReports.jsx`

## Scope Or Methodology

The review checked whether the CDH-M slice corrects Finding 4 from the original
CDH rebuttal without reopening the blocked parts of that roadmap.

The audit was read-only. No Maika source, CVF runtime code, Supabase settings,
or public-sync files were modified.

The review focused on:

- whether Maika summary generation uses the governed CVF `/api/execute` path;
- whether direct provider calls or provider SDK imports exist in the summary
  Edge Function;
- whether the frontend payload excludes child identity, contact fields, student
  IDs, and photos from the summary request;
- whether the remaining live proof and privacy boundary are stated honestly.

## Findings Or Position

### Finding 1 - Corrected CDH-M Scope Is Directionally Valid

The meta-roadmap correctly narrows M to deployment verification and evidence
hardening for a text-only daily summary path. That correction addresses the
main overreach in the original CDH roadmap: Maika cannot be used as broad proof
that CVF governs child data, photos, health records, vision flows, or downstream
school operations.

Evidence trace:

- Claim checked: M is text-summary verification only.
- Source: `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`
- Result: the slice explicitly excludes Maika photo-description proof, direct
  provider fallback, public-sync claim, and child identity/contact payload proof.
- Disposition: SUPPORTED.

### Finding 2 - Existing Source Supports CVF-Only Summary Routing

The Maika Edge Function source is consistent with the intended M slice boundary.
It calls `CVF_EXECUTE_URL`, signs the request with CVF service-token material,
and sends a documentation-template request to CVF. It does not import a direct
LLM provider SDK and does not implement a direct provider fallback.

Evidence trace:

- Claim checked: Maika summary generation is routed through CVF rather than a
  direct provider.
- Source:
  `../CVF-Workspace/Nha tre Maika/supabase/functions/generate-daily-summary/index.ts`
- Result: the function builds a CVF `/api/execute` request, requires an
  authenticated admin or teacher sender, and returns local rule-based fallback
  text on CVF/network/auth failures.
- Disposition: SUPPORTED_WITH_DEPLOYMENT_GAP.

### Finding 3 - Deployment Proof Is Still Missing

The M1 completion review is explicit that the implementation is source-complete
and locally checked, but not yet proven by deployed Supabase invocation with a
real admin or teacher session and configured CVF secrets.

The next work order must not treat local source audit as release-quality proof.
It must prove the deployed Edge Function path end to end.

Evidence trace:

- Claim checked: live deployment verification remains pending.
- Source: `docs/reviews/archive/CVF_M1_MAIKA_TEXT_SUMMARY_COMPLETION_2026-05-19.md`
- Result: status is `CLOSED_WITH_DEPLOYMENT_VERIFICATION_PENDING`.
- Disposition: GAP CONFIRMED.

### Finding 4 - Health Data Requires Explicit Privacy Gate

The current Maika request builder excludes child names, parent names, contact
data, student IDs, and photos from the summary payload. However, it can include
a health field when health is not the normal/default value.

That is acceptable only inside a privacy-gated product proof. It must not be
described as "low-governance" or used as a casual governance demonstration. The
next GC-018 must choose one of these proof postures before implementation:

- proof corpus excludes abnormal health values and verifies the non-health
  minimized payload only; or
- proof corpus includes abnormal health text only after treating it as
  sensitive data with explicit minimization, retention, logging, and evidence
  redaction controls.

Evidence trace:

- Claim checked: summary payload is minimized but not necessarily health-free.
- Sources:
  `../CVF-Workspace/Nha tre Maika/supabase/functions/generate-daily-summary/index.ts`
  and `../CVF-Workspace/Nha tre Maika/src/pages/admin/DailyReports.jsx`
- Result: summary payload excludes identity/photo fields, but includes health
  when the value is abnormal/non-default.
- Disposition: PRIVACY GATE REQUIRED.

### Finding 5 - Photo And Vision Remain Out Of Scope

The reviewed M slice is not a bridge into photo governance. Any later Maika
photo description, vision-runtime, or child-photo evidence must be routed
through the CDH-D vision-runtime gate or a later dedicated roadmap.

Evidence trace:

- Claim checked: M does not authorize photo or vision.
- Source: CDH-M non-goals and original Finding 4.
- Result: no photo proof is authorized by this slice.
- Disposition: SUPPORTED_AND_LOAD_BEARING.

## Risk / Defect / Corrective Action

| Risk | Why It Matters | Required Correction |
| --- | --- | --- |
| Local source audit mistaken for live proof | M1 is not deployed-proof complete | Work order must require deployed Supabase Edge Function invocation with authenticated admin or teacher session |
| Health text treated as low-governance data | Abnormal health text can be sensitive child data | GC-018 must either exclude abnormal health from proof or classify it as sensitive and require redaction/minimization controls |
| UI success mistaken for CVF governance evidence | A summary string alone does not prove governed routing | Completion proof must include CVF-side receipt/audit evidence, not only Maika UI output |
| Direct provider fallback reintroduced later | Would violate the corrected CDH-M boundary | Work order must preserve CVF-only provider routing and local rule-based fallback only |
| M used to over-close CDH | One Maika proof does not close C/D/H | Closure review must state CDH-M only; no bundled CDH runtime claim |
| Secrets printed during proof | Supabase/CVF tokens are sensitive | Evidence must use env/Supabase secrets and redact all raw key material |

## Decision / Recommendation / Disposition

CDH-M is NON_BLOCKING_WITH_PRIVACY_GATE.

Allowed next move:

- Orchestrator may file a slice-specific GC-018 for CDH-M deployment
  verification and evidence hardening.
- After that GC-018 is accepted, a work order may be dispatched for the live
  deployed Maika summary proof.

Required GC-018 / work order corrections:

- name the scope as CDH-M deployment verification and evidence hardening;
- require deployed Supabase Edge Function invocation, not local-only source
  inspection;
- require authenticated admin or teacher session;
- require CVF receipt or audit evidence proving `/api/execute` governance;
- require payload evidence showing identity/photo/contact fields are absent;
- decide the abnormal-health proof posture before execution;
- preserve local rule-based fallback only;
- forbid direct provider fallback, Maika photo proof, public-sync claim, and
  bundled CDH closure.

## Claim Boundary

After this rebuttal, the only accepted CDH-M claim is:

CVF has a plausible, source-supported Maika text-summary integration candidate
that can proceed to live deployment verification through the governed CVF path,
subject to an explicit privacy gate for health/minimized child-adjacent text.

This is not proof of:

- governed child-data handling in general;
- governed photo or vision runtime behavior;
- Maika production readiness;
- public CVF product claims;
- closure of CDH-C, CDH-D, or CDH-H.
