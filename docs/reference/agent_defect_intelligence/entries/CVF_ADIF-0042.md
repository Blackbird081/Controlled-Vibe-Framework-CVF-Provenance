# ADIF-0042 - Screenshot Metadata Accepted Without Pixel-State Binding

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0042
title: Screenshot metadata accepted without pixel-state binding
defectCategory: CLOSURE_EVIDENCE
defectClass: EVIDENCE_INTERPRETATION_ERROR
defectRole: worker
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Worker execution (`WORKER_MUST_NOT_COMMIT`); Reviewer-return review; Closure
roles: dispatcher; worker; reviewer; closer
lifecyclePhases: pre-dispatch; pre-implementation; pre-closure
surfaceSelectors: browser-evidence packets containing PNG screenshots plus JSON capture metadata
detectionSignals: JSON and prose declare a visible terminal anchor while the retained PNG shows an onboarding overlay, blur layer, stale page, or different state
enforcementLevel: GUIDANCE_ONLY
checkerBindings: NOT_APPLICABLE_WITH_REASON: current structural gates validate packet shape but do not inspect arbitrary screenshot pixels against JSON claims
promotionState: MACHINE_CHECK_CANDIDATE
supersedes: NONE
lastVerifiedCommit: c0b38fbe1
roadmapSeedId: NONE
```

## Purpose

Prevent DOM assertions, script-authored labels, or capture metadata from being
accepted as visual evidence when the final saved screenshot does not visibly
contain the state claimed by the packet.

## Scope / Applies To

Applies to browser-acceptance work that retains screenshots with a companion
capture manifest, interaction trace, OCR text, DOM state, or visual verdict.
It is especially relevant when onboarding, dialogs, reloads, or asynchronous
effects can change the page between assertion and final screenshot write.

## Bad Example

Assert a form heading in the DOM, navigate or reload, write a screenshot that
shows onboarding over the page, and retain the earlier heading in JSON with a
PASS verdict without reopening the saved PNG.

## Good Example

Use one persistent browser context, clear or dismiss blocking overlays, assert
the exact terminal state immediately before capture, compute SHA256 after the
final write, bind that hash to the capture record, reopen the exact saved PNG,
and let an independent reviewer inspect the pixels at original resolution.

## Canonical Sources

- `docs/reviews/CVF_WEB_UX_T4_R4_BLOCKED_RETURN_REVIEW_2026-07-20.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T4_R5_SCREENSHOT_STATE_BINDING_REPAIR_2026-07-20.md`
- `docs/reviews/CVF_WEB_UX_T4_R5_WORKER_RETURN_2026-07-20.md`
- `docs/reference/guard_orientation/README.md`

## Remediation

1. Preserve one browser context through dismissal, navigation, and capture when
   state continuity matters.
2. Assert overlay absence and the route-specific terminal anchor immediately
   before each screenshot write.
3. Hash the saved bytes after the final write and record the same hash in every
   companion manifest.
4. Reopen the saved file, not merely the live page, and record visual inspection
   separately from DOM assertions.
5. Require the reviewer to recompute hashes and inspect every closure-critical
   image at original resolution.
6. Consider a future image-manifest guard only after a reusable pixel or OCR
   comparison contract is designed; do not treat structural packet PASS as
   content agreement.

## Epistemic Process Block

### Expected Result / Prediction

A screenshot whose capture record names a visible terminal anchor should show
that anchor in its final saved pixels without an obscuring overlay.

### Evidence Comparison

T4-R4 supplied mutually consistent prose and JSON for three scenarios, but all
three saved PNGs showed onboarding over the claimed terminal state. T4-R5 used
one persistent context, overlay assertions, post-write hashes, and visual
reopen inspection; the reviewer recomputed all three hashes and observed the
claimed pixels.

### Contradiction Or Gap Disposition

Metadata agreement is rejected as visual proof when final pixels contradict
it. Pixel inspection plus exact-byte binding is required for closure-critical
screenshots.

### Claim Update

Browser evidence is accepted only to the extent that the saved image bytes,
their manifest, and reviewer observation agree.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent reviewer/closer |
| Provider or surface | local provenance workspace and retained browser evidence |
| Session or invocation | CVF Web UX T4 R4-R5 closure learning, 2026-07-20 |
| Working directory | repository root |
| Command or tool surface | original-resolution image inspection, JSON parsing, SHA256 recomputation, apply_patch, ADIF integrity gate |
| Target paths | ADIF-0042 entry and entries README row |
| Allowed scope source | AGENTS.md mandatory ADIF disclosure and repeated T4 browser-evidence defect |
| Before status evidence | R3 and R4 required repeated repairs for target/result binding; R4 metadata directly contradicted all three PNGs |
| After status evidence | ADIF-0042 is resolver-discoverable and the entries front door lists it |
| Diff evidence | new entry plus README row in the T4 material closure batch |
| Approval boundary | governance learning only; no browser runtime, OCR checker, source, hosted, deploy, public, provider, or production mutation |
| Claim boundary | reusable guidance and machine-check candidate; no generic pixel-semantic checker exists |
| Agent type | reviewer/closer |
| Invocation ID | `cvf-web-ux-t4-adif-0042-2026-07-20` |
| Expected manifest | ADIF-0042 entry and entries README row within the larger T4 material closure batch |
| Actual changed set | ADIF-0042 entry and entries README row within the larger T4 material closure batch |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance defect intelligence; no public-sync work is
authorized by this entry.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | reusable browser-evidence guidance only |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or automatic visual comprehension is claimed |
| receiptEvidence | N/A with reason: this ADIF entry creates no runtime receipt |
| actionEvidence | N/A with reason: retained R4-R5 evidence supports the defect record, not a new runtime action |
| invocationBoundary | local documentation and evidence inspection only |
| interceptionBoundary | no browser, provider, hosted, production, or agent-action interception |
| claimLanguage | guidance requires saved-pixel and metadata agreement for closure-critical screenshots |
| forbiddenExpansion | no OCR checker, image model, runtime gate, provider/live call, public-sync, or production mutation |

## Claim Boundary

This entry records a recurring browser-evidence defect and bounded prevention
rule. It does not implement visual comprehension, OCR comparison, automatic
overlay detection, runtime enforcement, or public behavior.
