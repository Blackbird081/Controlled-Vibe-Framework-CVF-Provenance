# NCR P09 - Release result consistency

Memory class: FULL_RECORD

docType: baseline

Status: LOCAL_IMPLEMENTED_VERIFIED_BOUNDED

Date: 2026-10-06

## Purpose

Continue the wider NCR backlog after bounded P06 ingress maintenance. Make
release runner console, JSON/file and exit agree on missing/skipped evidence.

## Source Verification Block

| Source | Disposition | Finding |
|---|---|---|
| scripts/run_cvf_release_gate_bundle.py, print_results/result_payload/main | ACCEPT | Console counts only FAIL; JSON also rejects missing/non-PASS SOT3; main has two independently chosen renderers |
| scripts/test_run_cvf_release_gate_bundle.py | ACCEPT | Existing hermetic build/scan/runtime fixtures; reuse without running live release bundle |
| scripts/test_run_cvf_sot3_a5_release_integration.py | ACCEPT | Existing SOT3 payload admission controls; preserve exact live-proof contract |
| docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md, P09/W03-C | ACCEPT | Required checks and console/JSON/file/exit must agree; dry-run is not release PASS |

## Decision / Scope

Operator next authorizes bounded Local reversible maintenance; Local implements
and decides technical disposition. Four material paths: scripts/run_cvf_release_gate_bundle.py,
scripts/test_cvf_release_result_consistency.py (new focused hermetic suite), this
baseline, scripts/test_run_cvf_sot3_a5_release_integration.py (existing fake run_cmd
signature corrected to accept the existing env argument). Replace the roadmap
selection line and add one evidence pointer; preserve prior delta. No
provider invocation, new checker/schema, state/handoff, commit/public/deploy.

Reuse result_payload as decision owner for all rendering. Any check outside
PASS/WARN, or an empty check list, cannot be PASS. Preserve existing non-release
non-SOT3 payload exception, SOT3 admission and warning semantics. CLI passes the
same computed payload to console and JSON/file rather than independently
recomputing release success. No missing-name manifest expansion is claimed.

## Evidence / Verification Plan

Hermetic tests cover FAIL, SKIP/ABSENT/unknown status, empty list, non-PASS or
missing SOT3, valid PASS/warning and existing non-release exception. Compare
console text, JSON/file and exit. Actual CLI dry-run text and JSON are permitted
read-only diagnostics; expected FAIL/exit 1, not live governance proof. No call
or mock response is used to assert AI governance. Existing SOT3/runner suites
check regressions without real subprocess/provider execution.

## Current Runtime Freshness Verification

Local 2026-10-06 at HEAD 45b1a48d4 plus disclosed dirty worktree: named runner
print_results, result_payload and both main exit branches inspected directly.
The contradiction is present in current source, not inferred from public absence
or historical audit. This is selected renderer/decision code only.

## Verification Results

Initial static preflight rejected an incidental negative-scope phrase; clarified
the named-code scope and retained preflight.log. Repaired preflight PASS 85/85,
11.32s before runner edits (preflight-repaired.log). ADIF query zero candidates,
no truncation (adif.json). Red new suite: five methods with six failures/nine
subtest errors against old decision/rendering signature; green five methods PASS.
The matrix covers sixteen scenarios across statuses, evidence and legacy callers.

Focused runner regression PASS 14/14 (runner-focused.log). SOT3 regression first
ran 66 with one error: old fake_run_cmd did not accept env already passed by the
unchanged E2E caller. Corrected only that test-double signature; 66/66 PASS
(sot3-regression-repaired.log). Total 85 hermetic test methods PASS; no real
provider, build or E2E subprocess was invoked. No new release proof is claimed.

The initial broader runner suite entered the unrelated full-tree secret scan.
That owned Python process was stopped; exact known synthetic fixture bytes/path
were verified and its one scratch file removed. No full scan PASS is claimed;
runner-regression.log is interrupted evidence. No other fixture/path cleanup.

Actual CLI dry-run, text and JSON modes, both exit 1 and gate FAIL. Console text,
stdout JSON and --output files agree; SOT3 remains SKIP. Receipts: dry-text.log,
dry-json.log, dry-text-result.json, dry-json-result.json in
.cvf/runtime/ncr-p09-results-20261006/. This is correct non-release classification,
not a failed live proof. git diff --check PASS; final static is final-static.log.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_public_export_disposition.py |
| literalTokensReviewed | Source/Decision/Evidence/Claim Boundary; read-ahead fields; complete trace labels; Resolver query; Returned defects; Public Export Disposition |
| gateRunPurpose | Confirm authored bounded scope/evidence; not first discovery of literals |
| claimBoundary | Static packet admission, not release/governance proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Worker execution`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED. Zero candidates and no truncation.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local maintainer/reviewer |
| Provider or surface | private workspace, no provider |
| Session or invocation | NCR-P09-RESULT-20261006 |
| Working directory | repository root |
| Command or tool surface | Python hermetic tests, dry-run CLI, static autorun |
| Target paths | four paths above and existing roadmap |
| Allowed scope source | operator next and existing P09 backlog |
| Before status evidence | prior worktree delta retained |
| After status evidence | 85 hermetic tests PASS; both actual dry-run modes truthfully FAIL/exit 1 |
| Diff evidence | scoped git diff |
| Approval boundary | local reversible maintenance only |
| Claim boundary | runner result truth, not release readiness |
| Agent type | Local |
| Invocation ID | NCR-P09-RESULT-20261006 |
| Expected manifest | runner/new test/SOT3 fixture signature/baseline/roadmap |
| Actual changed set | same expected set plus untouched prior delta |
| Manifest delta | MATCH intended scope |

## Claim Boundary

Result consistency is separate from real governance/release proof. No release
is run or accepted; prior pending checkpoints remain parked. Work is uncommitted.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY - bounded local runner maintenance.
