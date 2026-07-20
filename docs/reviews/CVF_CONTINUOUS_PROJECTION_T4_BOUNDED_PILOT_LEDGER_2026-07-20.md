# CVF Continuous Projection T4 Bounded Pilot Ledger

Memory class: governed-evidence-ledger

docType: review

Status: REVIEWER_ACCEPTED_BLOCKED_REDISPATCH_READY_R2

Batch ID: CVF-CONTINUOUS-PROJECTION-T4

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: `5b929dad9`

Date: 2026-07-21

## Purpose

Record the bounded T4 pilot evidence for `CVF-CONTINUOUS-PROJECTION-T4` R1.
R0 stopped at the pre-implementation gate before any fixture rerun or
real-root scan; that literal-format defect was repaired at material commit
`1bbd4729a`, and this R1 run consumed the single authorized real-root T1
scan invocation. The scan failed on a path-containment error before writing
any receipt, so no receipt, draft, or measurement-contract row evidence
exists for this run either.

## Target / Source

Target: the four Allowed T4 outputs named in the paired work order's Required
Artifact Manifest. Source: `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_AND_CLOSURE_2026-07-20.md`,
section 6 (Pre-Flight Checks), Phase A/Phase B of section 8 (Execution
Instructions), and section 6C (Worker Autonomy / No-Question Rule); and
`scripts/get_cvf_projection_drift_receipt.ps1` (the accepted T1 script,
`Assert-PathContainment` function).

## Scope / Methodology

Per section 6, the worker ran every listed pre-flight command before creating
any output file, then Phase A (fixture reruns), then Phase B (the single
real-root scan attempt):

1. `git rev-parse --short HEAD`
2. `git status --porcelain`
3. `git remote get-url origin`
4. `git -C ..\Controlled-Vibe-Framework-CVF-public-sync status --porcelain`
5. `git -C ..\Controlled-Vibe-Framework-CVF-public-sync remote get-url origin`
6. `Test-Path EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web`
7. `Test-Path scripts\cvf_projection_policy.json`
8. `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5f5c28b85 --head HEAD`

All eight pre-flight checks passed. Phase A then reran all three
disposable-fixture suites, all of which passed. Phase B then created a
unique temporary directory under `%TEMP%` (outside all three target roots)
and invoked `scripts/get_cvf_projection_drift_receipt.ps1` exactly once with
`-ScanTimeoutSeconds 3600` and `-ReceiptOutputPath` pointed at a file inside
that temporary directory. The invocation failed immediately (0.35 seconds
elapsed, well inside the timeout) with a structured `PATH_ESCAPE` error, not
a timeout and not a dirty-root refusal. Per the work order's Phase B
instruction ("Do not rerun") and the hard constraint against retrying the
real-root scan, the worker stopped after this single invocation and did not
attempt a second scan with a different receipt path.

## Findings / Position

### Pre-Flight Results (Commands 1-8)

| Check | Expected | Observed | Disposition |
| --- | --- | --- | --- |
| `git rev-parse --short HEAD` | matches operator-supplied executionBaseHead `5b929dad9` | `5b929dad9` | PASS |
| `git status --porcelain` (provenance root) | empty | empty | PASS |
| `git remote get-url origin` (provenance root) | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git` per policy `expectedRemotes.provenanceRemote` | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git` | PASS |
| `git -C ..\Controlled-Vibe-Framework-CVF-public-sync status --porcelain` | empty | empty | PASS |
| `git -C ..\Controlled-Vibe-Framework-CVF-public-sync remote get-url origin` | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` per policy `expectedRemotes.publicRemote` | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` | PASS |
| `Test-Path EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web` | `True` | `True` (path exists) | PASS |
| `Test-Path scripts\cvf_projection_policy.json` | `True` | `True` (path exists) | PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5f5c28b85 --head HEAD` | COMPLIANT | `COMPLIANT: pre-implementation autorun gate passed in 5.93s.` | PASS, confirming the R0 literal-format defect fix at commit `1bbd4729a` |

### Phase A - Disposable Fixture Pilot Results

| Suite | Result |
| --- | --- |
| `scripts/test_cvf_projection_drift_receipt.ps1` | `Total: 53, Pass: 53, Fail: 0` -- PASS |
| `scripts/test_cvf_projection_review_packet.ps1` | `Total: 91, Pass: 91, Fail: 0` -- PASS |
| `scripts/test_cvf_projection_audience_gate.ps1` | `Total: 144, Pass: 144, Fail: 0` -- PASS |

All three fixture suites passed with zero failures, so Phase B was
authorized to proceed.

### Phase B - Single Real-Root Receipt Attempt

Command (elapsed 0.3458898 seconds, well inside the 3600-second ceiling, so
this is not a timeout):

```text
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/get_cvf_projection_drift_receipt.ps1 `
  -ProvenanceRoot "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF" `
  -PublicSyncRoot "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" `
  -CvfWebRoot "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web" `
  -PolicyPath "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\scripts\cvf_projection_policy.json" `
  -ReceiptOutputPath "C:\Users\DELL\AppData\Local\Temp\cvf_t4_r1_realscan_d8d2837a\real_root_receipt.json" `
  -ScanTimeoutSeconds 3600
```

Result: exit code `1`. Structured error envelope on stdout:

```json
{
    "receiptId": null,
    "schemaVersion": "1.0.0",
    "sourceRoot": "PROVENANCE_ROOT",
    "targetRoot": "PUBLIC_SYNC_ROOT",
    "cvfWebRoot": "CVF_WEB_ROOT",
    "errors": [
        {
            "code": "PATH_ESCAPE",
            "message": "PATH_ESCAPE: 'C:\\Users\\DELL\\AppData\\Local\\Temp\\cvf_t4_r1_realscan_d8d2837a\\real_root_receipt.json' is not contained within 'D:\\UNG DUNG AI\\TOOL AI 2026\\Controlled-Vibe-Framework-CVF\\'"
        }
    ],
    "noTargetWriteConfirmation": "CONFIRMED_NO_TARGET_WRITE: this run performed zero filesystem writes inside ProvenanceRoot, PublicSyncRoot, or CvfWebRoot."
}
```

Diagnostic classification:

| Field | Value |
| --- | --- |
| stage | Phase B, single real-root receipt attempt |
| class | structured path-containment refusal (`PATH_ESCAPE`) |
| retryability | NOT_RETRYABLE by this worker: the work order's Phase B instruction says "Do not rerun," and the hard constraint forbids retrying the real-root scan regardless of diagnostic class |
| user action | reviewer must decide either to widen the accepted T1 script's containment rule to permit a receipt path outside the current working directory, or to redispatch a future tranche whose Phase B instruction supplies a `-ReceiptOutputPath` value that is itself inside the provenance root's working directory (while still outside `ProvenanceRoot`/`PublicSyncRoot`/`CvfWebRoot` proper) |
| elapsed time | 0.3458898 seconds |
| exit code | 1 |
| diagnostic code | `PATH_ESCAPE` |
| safe message | receipt output path was not contained within the current working directory, which is the accepted T1 script's actual containment boundary, not "outside all three target roots" as paraphrased in the work order's Phase B instruction |

Root cause, traced directly in `scripts/get_cvf_projection_drift_receipt.ps1`:
the `-ReceiptOutputPath` branch resolves `$cwdContainer = (Get-Location).ProviderPath`
and calls `Assert-PathContainment -CandidatePath $ReceiptOutputPath
-ContainerPath $cwdContainer` before checking containment against
`ProvenanceRoot`/`PublicSyncRoot`/`CvfWebRoot`. Because the worker's current
working directory is the provenance repository root itself, any
`-ReceiptOutputPath` located under `%TEMP%` (outside the repository
entirely) fails this first containment check with `PATH_ESCAPE`, before the
script ever reaches its own read-only three-root scan logic. The work
order's Phase B instruction to place the temporary receipt path "outside all
three target roots" is accurate for `ProvenanceRoot`/`PublicSyncRoot`/`CvfWebRoot`
individually, but is incompatible with the accepted script's additional,
stricter requirement that the receipt path also be contained within the
current working directory.

This defect sits in the accepted T1 script's existing containment logic (a
path the worker is forbidden to modify) and in the work order's own Phase B
instruction (also forbidden to modify). The worker has no Allowed path
through which to repair either side of this contradiction, and the single
real-root scan invocation permitted by this batch is now consumed.

## Risk / Corrective Action

Risk: none from the worker's own action. The scan attempt wrote zero bytes
to any location: the script's own `noTargetWriteConfirmation` field
confirms zero filesystem writes inside `ProvenanceRoot`, `PublicSyncRoot`,
or `CvfWebRoot`, and the temporary directory outside all three roots
(created and owned solely by this worker for the disposable receipt
attempt) contained zero files after the failed invocation, confirmed by
direct enumeration before cleanup. No fixture suite failed, no forbidden
action of any kind was taken, and both Git roots remain clean after the
attempt.

Corrective action: none available to the worker inside Allowed scope. This
is a genuine contradiction between the work order's Phase B temp-path
instruction and the accepted T1 script's working-directory containment
rule; repairing either side requires editing a forbidden path (the script or
the work order). The reviewer owns deciding which side to repair, and owns
deciding whether a repaired future dispatch needs to supply a
`-ReceiptOutputPath` value nested under the current working directory
(while remaining outside the three named target roots) instead of a bare
`%TEMP%` path.

## Measurement Contract Evidence

Per the paired GC-018's Measurement Contract, the following rows are
reported as `NOT_APPLICABLE_WITH_REASON` because Phase B never produced a
receipt:

| Metric | Worker evidence |
| --- | --- |
| fixture stability | CONFIRMED: `53/53`, `91/91`, `144/144` -- all three suites passed with zero failures |
| false positives | NOT_APPLICABLE_WITH_REASON: the real-root scan failed before producing a receipt; no rows exist to inspect |
| missed drift | NOT_APPLICABLE_WITH_REASON: the real-root scan failed before producing a receipt; no rows exist to inspect |
| reviewer effort | preparationMinutes: pre-flight, fixture rerun, one real-root scan attempt, and stop-condition diagnosis; no receipt or draft preparation occurred because none was produced |
| packet usefulness | NOT_APPLICABLE_WITH_REASON: no receipt or draft was produced |
| no mutation | CONFIRMED: `git status --short` was empty in both roots immediately before and immediately after the scan attempt; the script's own `noTargetWriteConfirmation` field confirms zero filesystem writes inside any of the three named target roots; the worker's own disposable temp directory contained zero files and was removed by the worker after enumeration |

## Decision / Recommendation / Disposition

`BLOCKED_WITH_REASON`. The worker consumed the single authorized real-root
scan invocation; it failed on a structured `PATH_ESCAPE` containment error,
not a timeout, dirty-root refusal, or scan-logic failure. No retry was
attempted. The reviewer owns resolving the contradiction between the work
order's Phase B temp-path instruction and the accepted T1 script's
working-directory containment rule, and owns deciding whether and how to
release a further R2 redispatch with a corrected Phase B receipt-path
instruction.

Reviewer disposition on 2026-07-21: `ACCEPTED_BLOCKED_RETURN`. The R1 stop is
correct, fixture results are accepted for bounded reuse, and the single R1
invocation is consumed. R2 omits `-ReceiptOutputPath`, captures the script's
documented stdout-only receipt in memory, and receives one fresh no-retry scan
ceiling. This does not accept a completed real-root scan or pilot result.

## Claim Boundary

This ledger proves that the pre-implementation gate passed (confirming the
R0 defect repair), that all three fixture suites passed with zero failures,
and that the single authorized real-root scan attempt failed on a
structured path-containment error before writing any receipt. It does not
claim a completed real-root scan, receipt/draft evidence, row-level drift
measurement, or any mutation. It does not claim the underlying
containment/instruction contradiction is fixed; that repair is
reviewer-owned because both sides of the contradiction live in forbidden
paths.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_finding_to_governance_learning.py`; `scripts/get_cvf_projection_drift_receipt.ps1` (root-caused directly for the stop condition itself) |
| literalTokensReviewed | Agent Operation Trace section label set; Epistemic Process section required subsections (Expected Result / Prediction, Evidence Comparison, Contradiction Or Gap Disposition, Claim Update); Delta Execution Claim Boundary section field set; Overlap And Novelty Classification section; Finding-To-Governance defect class, learning lane, disposition, and next-action vocabulary |
| gateRunPurpose | confirm this ledger's shape against the checker constants before reviewer handoff, used as confirmation evidence rather than as the means of discovering the required sections |
| claimBoundary | checker compliance proves packet structure only; the pre-flight, fixture, and real-root-scan results are proven by the Findings / Position section above |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated no-commit evidence worker |
| Provider or surface | local private provenance workspace; manual copy/paste handoff |
| Session or invocation | Continuous Projection T4 R1 worker execution, 2026-07-21 |
| Working directory | repository root |
| Command or tool surface | Git status/remote/rev-parse; PowerShell `Test-Path`; `python governance/compat/run_agent_autorun_workflow_gate.py`; the three fixture-suite scripts; one `scripts/get_cvf_projection_drift_receipt.ps1` invocation; direct file reads and enumeration of the disposable temp directory |
| Target paths | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_LEDGER_2026-07-20.md`; `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md` |
| Allowed scope source | paired GC-018 baseline and this work order, Required Artifact Manifest |
| Before status evidence | `git rev-parse --short HEAD` = `5b929dad9` (matches required executionBaseHead); `git status --porcelain` empty in both roots before any edit or scan attempt |
| After status evidence | `git status --short` (provenance root) shows exactly two modified paths (this ledger and the worker return, both already tracked from the R0 accepted return); `git status --porcelain` remains empty in the public-sync root; the two JSON evidence paths were never created because the scan attempt failed before writing a receipt |
| Diff evidence | `git diff --name-status` shows only the two already-tracked review paths as modified; no other path changed |
| Approval boundary | bounded T4 pre-flight, fixture, and single-real-root-scan-attempt evidence only |
| Claim boundary | no completed real-root scan, receipt/draft, T2/T3 execution, mutation, public-sync, commit, push, or production claim |
| Agent type | delegated no-commit evidence worker |
| Invocation ID | `continuous-projection-t4-bounded-pilot-r1-2026-07-21` |
| Expected manifest | up to four Allowed paths depending on run outcome; a blocked scan-attempt run yields exactly two modified paths (ledger and worker return) plus zero new JSON evidence paths |
| Actual changed set | exactly two modified paths: this ledger and the worker return |
| Manifest delta | MATCH for the blocked-scan-attempt case |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred in this batch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | local T4 pre-flight, fixture-rerun, and single real-root scan attempt only |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no T1 receipt, T2 draft, or CVF execution-control receipt was produced; the scan attempt failed before any receipt was written |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no action path exists; zero filesystem writes occurred inside the provenance or public-sync root, confirmed by the script's own no-write confirmation field |
| invocationBoundary | manual local Git/PowerShell/Python governance-check invocation only, plus exactly one T1 script invocation |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, browser, provider, or agent coding control exists in this batch |
| claimLanguage | this ledger proves a fail-closed real-root scan attempt only; it does not independently decide how the containment/instruction contradiction should be resolved |
| forbiddenExpansion | no fixture-failure retry, second real-root scan, T2/T3 execution, provider, live, public, package, Web edit, MCP/CLI adapter, or model-router behavior is implemented or claimed |

## Overlap And Novelty Classification

NOT_APPLICABLE_WITH_REASON: this ledger absorbs no outside repository,
critique, or provider output. Its only cited material is this repository's
own source (`scripts/get_cvf_projection_drift_receipt.ps1` and the paired
dispatch work order), which is CVF-owned source, not outside absorbed
knowledge, so no overlap-versus-novelty classification against an existing
CVF owner surface applies.

## Epistemic Process Block

### Expected Result / Prediction

A clean committed HEAD matching the required executionBaseHead, two clean
Git roots, a passing pre-implementation gate, and three passing fixture
suites should let the single real-root scan complete successfully and
produce one accepted receipt.

### Evidence Comparison

The pre-implementation gate passed and all three fixture suites passed with
zero failures, confirming the R0 repair and the fixture mechanisms remain
stable. The single real-root scan attempt diverged from expectation: it
failed in 0.35 seconds (not a timeout) with a structured `PATH_ESCAPE`
error, traced directly to `Assert-PathContainment` inside the accepted T1
script requiring the receipt output path to be nested under the current
working directory, a stricter rule than the work order's Phase B
instruction ("outside all three target roots") anticipated.

### Contradiction Or Gap Disposition

The work order's Phase B instruction and the accepted T1 script's own
containment logic are in direct contradiction for any `-ReceiptOutputPath`
located outside the repository working directory. This gap cannot be closed
inside worker scope because both sides (the script and the work order) are
forbidden paths for this worker. It is not converted to a PASS, and per the
hard constraint against retrying the real-root scan, no second invocation
with a corrected path was attempted.

### Claim Update

This run may claim a passing pre-implementation gate, three passing fixture
suites, and one fully diagnosed failed real-root scan attempt. It may not
claim a completed real-root scan, receipt/draft evidence, or any
measurement-contract row that depends on Phase B having produced a receipt.
