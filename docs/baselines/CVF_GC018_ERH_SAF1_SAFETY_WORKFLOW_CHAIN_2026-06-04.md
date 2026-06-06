# CVF GC-018 - ERH-SAF1 Safety Workflow Chain

Memory class: FULL_RECORD

Status: AUTHORIZED_DISPATCH_PACKET

docType: gc018_baseline

Date: 2026-06-04

dispatchBaseHead: `16c1fb68`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize ERH-SAF1 as the bounded runtime follow-up from ERH-RS1. The goal is
to turn the confirmed safety-layer gap into a deterministic safety workflow
chain in the web execute route.

Success means `/api/execute` has source-visible severity-classified safety
screening after DLP and before provider execution, with audit/readout evidence,
focused tests, and a machine-checkable workflow-chain boundary.

## Scope / Target / Owner Boundary

Target runtime surface:

`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

Target safety owner surface:

`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts`

Authorized outputs:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_FOR_CLAUDE_2026-06-04.md`
- `docs/reference/CVF_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_2026-06-04.md`
- `docs/reference/CVF_ERH_SAF1_SAFETY_WORKFLOW_LEDGER_2026-06-04.md`
- `docs/reviews/CVF_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md`
- bounded source/test/checker files named by the SAF1 work order.

Out of scope:

- ML DLP, model-based classifier, or "advanced AI jailbreak detection" claims;
- provider routing behavior changes;
- provider risk ceiling configuration;
- durable audit storage migration;
- `policySnapshotId` persistence;
- Redis or distributed rate limiting;
- auth, dependency, package, lockfile, public-sync, hosted-readiness,
  production-readiness, public-readiness, or public push work.

Risk ceiling: R2 runtime route safety hardening. Escalate before any route
refactor, package change, provider behavior change, public-sync work, or claim
that exceeds deterministic pattern coverage.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-04: open ERH-SAF1 Safety Workflow Chain and evaluate SAF2 after SAF1 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |
| ERH-RS1 assessment | `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | ACCEPT |
| ERH-RS1 completion | `docs/reviews/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_COMPLETION_2026-06-04.md` | ACCEPT |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |

## Decision / Baseline

Decision: authorize Claude to implement SAF1 under `WORKER_MUST_NOT_COMMIT`.

Baseline facts:

- ERH-RS1 concluded `ERH-SAF1_READY`.
- `/api/execute` already runs DLP before legacy safety screening.
- The current route safety call uses `applySafetyFilters` from `safety.ts`,
  which is a small regex/pattern helper.
- `safety-status.ts` contains richer severity-classified deterministic patterns
  but is marked `'use client'` and is not the execute-route safety chain.
- SAF1 must extract or re-own the deterministic pattern set in a server-safe
  helper rather than importing a client-only helper into route code.

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Execute route imports legacy safety filter | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 6 | `applySafetyFilters` | `/api/execute` POST route | ACCEPT |
| Execute route can append audit events | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 18 | `appendAuditEvent` | `/api/execute` POST route | ACCEPT |
| Execute route runs DLP before safety | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 240-261 | `applyDLPFilter` | `/api/execute` POST route | ACCEPT |
| DLP redaction emits audit event with payload | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 243-257 | `DLP_REDACTION_APPLIED` | `/api/execute` audit event | ACCEPT |
| Safety block currently returns 400 before provider execution | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 260-271 | `blocked` | `/api/execute` safety branch | ACCEPT |
| Current safety filter is deterministic regex/pattern based | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts` | lines 1-35 | `applySafetyFilters` | web safety filter | ACCEPT |
| Current DLP entry point reads active DLP policy | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/dlp-filter.ts` | lines 6-8 | `applyDLPFilter` | web DLP filter | ACCEPT |
| DLP preset pattern engine exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/dlp-filter-core.ts` | lines 24-74 and 149-190 | `applyDLPPatterns` | DLP pattern engine | ACCEPT |
| `safety-status.ts` is client-scoped | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety-status.ts` | line 15 | `'use client'` | web UI safety helper | ACCEPT |
| Richer severity-classified patterns exist in UI helper | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety-status.ts` | lines 115-135 | `INJECTION_PATTERNS` | web UI safety helper | ACCEPT |
| UI helper exports sanitizer and dangerous-input check | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety-status.ts` | lines 137-167 | `sanitizePrompt` | web UI safety helper | ACCEPT |
| cvf-web has type, build, and test scripts | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | lines 10-16 | `scripts` | cvf-web package manifest | ACCEPT |

## SAF2 Evaluation Checkpoint

SAF1 must not implement SAF2. The SAF1 completion review must include a short
SAF2 decision section with exactly one verdict:

- `SAF2_READY`
- `SAF2_HOLD`
- `SAF2_NOT_NEEDED`

SAF2 should be considered only after SAF1 evidence exists. Candidate SAF2 scope
may include adversarial safety regression corpus, output safety/readout
coverage, or safety coverage drift checking. SAF2 must remain separate if it
requires ML classifiers, provider prompt changes, output-quality tuning,
package changes, live quota expansion, or public claims.

## Evidence / Verification

Dispatch verification:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base 16c1fb68 --head HEAD --all-changed --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 16c1fb68 --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base 16c1fb68 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 16c1fb68 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 16c1fb68 --head HEAD
```

Closure verification must use Claude's captured execution base. If SAF1 claims
release-quality governance behavior, run the mandatory live governance proof
bundle with secret-safe environment loading.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| External review found safety layer too thin for documented claim posture | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | WORKFLOW_CHAIN_REQUIRED | ERH-SAF1 runtime safety workflow chain |
| Richer deterministic safety patterns existed only in a UI helper | ROUTE_COVERAGE_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_CANDIDATE | SAF1 checker must verify route wiring and boundary |
| Future safety uplift needs a separate decision after SAF1 evidence | SCOPE_BOUNDARY_GAP | GOVERNANCE_CONTROL_PLANE | ROADMAP_CANDIDATE | SAF2 decision section required in SAF1 completion |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ERH-SAF1 is private provenance runtime hardening and dispatch planning.

Next action: public-facing summary requires a later public-sync work order from
the public-sync clone after SAF1 is reviewed and claim boundaries are accepted.

## Claim Boundary

This GC-018 authorizes deterministic safety workflow-chain hardening only. It
does not claim ML DLP, comprehensive jailbreak protection, production security
readiness, hosted readiness, public readiness, provider behavior change, or
complete remediation of every external review architecture weakness.
