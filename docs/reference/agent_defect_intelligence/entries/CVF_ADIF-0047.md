# ADIF-0047 - Provider-Backed Surface Misreported As Zero Invocation Consumption

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0047
title: Provider-backed surface misreported as zero invocation consumption
defectCategory: CLOSURE_EVIDENCE
defectClass: EVIDENCE_INTERPRETATION_ERROR
defectRole: worker
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Worker execution (WORKER_MUST_NOT_COMMIT); Reviewer-return review; Runtime / provider / live proof; Closure
roles: worker; reviewer; closer
lifecyclePhases: pre-implementation; pre-closure
surfaceSelectors: provider-backed CLI sessions, manual copy/paste worker returns, invocation receipts, usage and quota disclosures
detectionSignals: execution surface names a provider-backed CLI while the same return reports unqualified zero CLI or provider calls; usage is unknown but zero-consumption language remains
enforcementLevel: GUIDANCE_ONLY
checkerBindings: NOT_APPLICABLE_WITH_REASON: current gates validate field presence but do not distinguish host-session consumption from worker-initiated outbound calls
promotionState: MACHINE_CHECK_CANDIDATE
supersedes: NONE
lastVerifiedCommit: 551832fe0
roadmapSeedId: NONE
```

## Purpose

Prevent a worker return from undercounting provider or quota consumption by
equating "no recursive/outbound call initiated by the worker" with "the
provider-backed host session consumed nothing."

## Scope / Applies To

Applies whenever an agent works inside Claude Code, Codex, another
provider-backed CLI/IDE surface, or a similar authenticated host while
reporting invocation, provider-call, usage, quota, or cost evidence.

## Bad Example

Declare `Execution surface: provider CLI`, `Provider API calls: 0`, and `no
CLI action` without qualifying that zero covers only direct outbound calls
and that the host session itself may consume provider quota.

## Good Example

Record the provider-backed execution surface separately. Report zero only for
worker-initiated outbound or recursive calls. Record host-session
usage/quota from an exposed receipt, or use `UNKNOWN_NOT_EXPOSED`. Do not infer
zero consumption from missing telemetry.

## Canonical Sources

- `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`,
  Core Rule and Mandatory Dual Agent Surface Matrix.
- `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`, diagnostic
  and provider/model/receipt boundary.
- `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md`,
  host usage observability and unknown-usage distinctions.
- `docs/reviews/CVF_EAIC_KR_R1B_WORKER_RETURN_2026-07-23.md`, Provider /
  Model / Execution Disclosure and Reviewer-Owned Repairs.

## Remediation

Separate at least three facts in every applicable return:

1. the host execution surface;
2. worker-initiated outbound/recursive invocations; and
3. measured host-session usage/quota.

Zero is valid only for the bounded event class actually observed. Unknown
host usage stays unknown. A future checker may flag unqualified zero-call
claims when the same artifact names a provider-backed execution surface.

## Epistemic Process Block

### Expected Result / Prediction

A no-recursion worker should be able to prove zero outbound calls without
claiming that its provider-backed host session consumed zero quota.

### Evidence Comparison

The R1B return named `Claude Code CLI session` as its execution surface, then
reported zero CLI/provider calls and said no provider or CLI action occurred,
while also reporting usage as `UNKNOWN_NOT_EXPOSED`.

### Contradiction Or Gap Disposition

The zero claim and unknown-usage claim used different implicit denominators.
Reviewer repair made the denominator explicit: zero outbound/recursive calls,
unknown host-session consumption.

### Claim Update

Invocation evidence must distinguish surface, outbound calls, and metered
usage. This is guidance and a checker candidate; no automated detection or
cost measurement is claimed.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/closer |
| Provider or surface | local private provenance workspace |
| Session or invocation | EAIC-KR-R1B reviewer closure, 2026-07-23 |
| Working directory | repository root |
| Command or tool surface | local file reads, rg, apply_patch, governance gates, and Git evidence |
| Target paths | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0047.md`; entries README row; R1B worker return |
| Allowed scope source | operator instruction to repair reviewer findings and record necessary tranche learning |
| Before status evidence | R1B return named a provider-backed CLI surface but used unqualified zero provider/CLI-call language |
| After status evidence | return distinguishes host surface, outbound calls, and unknown usage; defect is resolver-discoverable |
| Diff evidence | material closure changed set and reviewer gate output |
| Approval boundary | governance learning and evidence repair only; no checker, runtime, provider, CLI/MCP, public, or policy implementation |
| Claim boundary | defect record and guidance only; no automated prevention or usage measurement claim |
| Agent type | reviewer/closer |
| Invocation ID | `eaic-kr-r1b-adif-0047-2026-07-23` |
| Expected manifest | ADIF-0047; entries README row; R1B worker return repair |
| Actual changed set | ADIF-0047; entries README row; R1B worker return repair within the R1B closure batch |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance learning. No public-sync action is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | provider-backed surface accounting guidance |
| claimDisposition | CLAIM_REJECTED: no runtime usage meter or invocation interceptor is implemented |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: R1B exposed no host usage receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: reviewer repaired contradictory disclosure language in the R1B return |
| invocationBoundary | local reviewer inspection and documentation repair only |
| interceptionBoundary | no provider, CLI/MCP adapter, process, wrapper, proxy, or runtime interception |
| claimLanguage | distinguish surface, outbound call count, and measured usage |
| forbiddenExpansion | no automatic cost control, quota measurement, provider integration, runtime enforcement, public-sync, or production claim |

## Claim Boundary

This entry records one recurring evidence-accounting defect and a bounded
checker candidate. It does not measure Claude/Codex usage, prove the host
made a particular number of backend requests, or authorize provider, CLI/MCP,
runtime, checker, public, or production implementation.
