# CVF GC-018 VI5-T4/T5 Hosted Export Acceptance Retest

Memory class: BASELINE_RECORD

Status: APPROVED

docType: baseline

Date: 2026-06-04

dispatchBaseHead: `7c082836`

## Purpose

Authorize a bounded Claude work order to retest the hosted Surface 1 web export
acceptance path for VI5-T4/T5 after ERH cleanup. The goal is to determine
whether the hosted Netlify web UI now exposes a fresh `app_builder_complete`
English full export that contains the portable external-agent handoff block and
is understandable enough for an external agent to proceed.

## Source / Predecessor Evidence

| Source | Evidence | Disposition |
| --- | --- | --- |
| VI5-T4/T5 original baseline | `docs/baselines/archive/CVF_GC018_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_2026-05-26.md` | ACCEPT |
| VI5-T4/T5 work order | `docs/work_orders/archive/CVF_WO_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_2026-05-26.md` | ACCEPT |
| VI5-T4/T5 completion | `docs/reviews/archive/CVF_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_COMPLETION_2026-05-26.md` | ACCEPT |
| Surface fidelity source | `docs/concepts/archive/CVF_OPERATOR_AGENT_AUTHORITY_AND_SURFACE_FIDELITY_2026-05-26.md` | ACCEPT |
| ERH initial closure | `docs/reviews/CVF_ERH_INITIAL_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md` | ACCEPT |

## Decision / Baseline / Proposed Tranche

Decision: open `VI5-HR1` as a hosted export acceptance retest and external-agent
readiness review.

Baseline:

- VI5-T5 deterministic source readiness was completed on 2026-05-26.
- VI5-T4 remained `READY_FOR_OPERATOR_ACCEPTANCE` pending a fresh web export and
  external-agent review.
- The active parked checkpoint still names VI5-T4/T5 hosted Netlify freshness
  and operator external-agent retest.

Proposed tranche:

- Claude verifies the hosted target freshness and export packet shape.
- Claude evaluates the fresh export as an external receiving agent.
- Claude returns a bounded review packet with `PASS`, `PASS_WITH_MINOR_FIX`, or
  `HOLD` style verdict and safe evidence.

## Scope / Target / Owner Boundary

Target:

- hosted Surface 1 web UI at `https://vibcode.netlify.app/home`;
- `app_builder_complete` template;
- English language;
- Full / CVF Guided Agent export mode;
- portable handoff section expected from VI5-T5.

Allowed actions:

- use browser/network access to inspect the hosted web UI;
- export or copy the generated markdown packet;
- evaluate the packet as an external agent;
- create a private review artifact in this provenance repository.

Blocked actions:

- runtime source edits;
- public-sync edits or push;
- dependency or auth migration;
- provider/API proof;
- consuming secrets or service tokens;
- hosted `/api/execute` governance proof;
- production or public-readiness certification.

## Surface Fidelity Control Block

| Control | Result |
| --- | --- |
| Surface verified before dispatch | Surface 1 hosted web export target is sourced from archived Surface Fidelity evidence |
| Previous wrong target avoided | Surface 2 `englishSpecFreeze` is not the test target |
| Audience verified | non-coder operator plus external build/evaluation agent |
| Language invariant | English packet chrome, original user-entered values preserved |
| Operator test dependency | Claude may perform external-agent evaluator role, but final operator acceptance remains reviewer/committer controlled |

## Required Proof

Claude must produce a review packet that records:

- hosted URL visited;
- template/language/mode selected;
- whether `Portable Agent Handoff Readiness` appears in the fresh hosted export;
- whether known Vietnamese chrome leakage is absent from packet chrome;
- external-agent readiness verdict;
- any live browser/hosted diagnostic if the retest fails, times out, or cannot
  obtain the export.

## Evidence / Verification

Authoring verification for this baseline:

```powershell
git rev-parse --short HEAD
Test-Path docs/reviews/archive/CVF_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_COMPLETION_2026-05-26.md
Test-Path docs/work_orders/archive/CVF_WO_VI5_T4_T5_SURFACE1_EXPORT_ACCEPTANCE_AND_PORTABLE_HANDOFF_2026-05-26.md
rg -n "vibcode.netlify.app/home|Portable Agent Handoff Readiness|PASS_WITH_MINOR_FIX" docs
```

Expected worker verification:

- hosted retest evidence is recorded in
  `docs/reviews/CVF_VI5_HR1_HOSTED_EXPORT_ACCEPTANCE_RETEST_CLAUDE_REVIEW_2026-06-04.md`;
- failures include live browser/hosted diagnostics before rerun;
- worker returns pending review under `WORKER_MUST_NOT_COMMIT`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline only authorizes a private hosted retest work order. It
does not update the public repository or make a public readiness claim.

## Claim Boundary

This baseline authorizes a bounded hosted export freshness and external-agent
readiness retest only. It does not prove live governance behavior, provider
behavior, hosted SaaS readiness, production readiness, public readiness,
dependency security clearance, or broad template portability.
