# CVF Continuous Projection T4 Worker Return - Bounded Pilot And Closure

Memory class: governed-worker-return

docType: review

Status: REVIEWER_ACCEPTED_BLOCKED_FINAL

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_AND_CLOSURE_2026-07-20.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_AND_CLOSURE_2026-07-20.md`

Paired baseline: `docs/baselines/CVF_GC018_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_AND_CLOSURE_2026-07-20.md`

Batch ID: CVF-CONTINUOUS-PROJECTION-T4

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: `8824cb8c7`

Date: 2026-07-21

## Purpose

Execute the frozen T4 bounded pilot sequence R3 (fixture-evidence reuse, one
fresh supervised real-root T1 scan process, T2 draft persistence, and a
measurement ledger), the final bounded recovery attempt per the paired
GC-018 baseline and work order. R3's Phase B correction launches exactly
one hidden, detached `powershell.exe` process and supervises it through
short polls of its persisted PID, instead of the synchronous invocation
that R2 proved incompatible with the worker's own tool-execution time
window. This return reports that the pre-implementation gate passed and
fixture evidence was validly reused, but that the single R3-authorized
process launch failed almost immediately due to an argument-quoting defect
before the target script ever executed.

## Target / Source

Target: the four Allowed outputs named in the work order's Required
Artifact Manifest. Source: `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_AND_CLOSURE_2026-07-20.md`,
sections 6 (Pre-Flight Checks) and 8 (Execution Instructions, Phase A/Phase
B, the supervised-process contract); `scripts/get_cvf_projection_drift_receipt.ps1`
(the accepted T1 script, never executed this run);
`docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0043.md` and
`CVF_ADIF-0044.md` (the two prior-round defect records); and
`docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_LEDGER_2026-07-20.md`
(full pre-flight, reuse-justification, and launch-attempt evidence).

## Scope / Methodology

The worker confirmed `executionBaseHead` `8824cb8c7` and a clean worktree in
both roots, then ran the pre-flight checks and the required
`git diff --name-only 5b929dad9..HEAD -- scripts/` reuse-justification check
(empty output, confirming `scripts/` is unchanged since R1). The bundled
pre-implementation autorun gate passed (`COMPLIANT`). Per the R3 dispatch
instruction, the three disposable-fixture suites were not rerun; R1's
accepted totals (`53/53`, `91/91`, `144/144`) were reused, justified by the
empty scripts-diff.

Phase B then followed the supervised launch-and-poll contract: created one
unique disposable directory under `%TEMP%`, reserved four paths (stdout,
stderr, metadata, launch sentinel), confirmed neither the metadata nor
sentinel path already existed, resolved the script path and all four T1
input paths to absolute paths, and launched exactly one hidden
`powershell.exe` process via `Start-Process -WindowStyle Hidden -PassThru`
with the working directory set to the provenance root. The launch call
returned immediately with PID `22624`; the worker persisted that PID,
launch time, and resolved paths to the metadata file and wrote the launch
sentinel, all without waiting synchronously for the scan. The worker then
issued one short, separately bounded poll (well under the 60-second limit)
and found the process had already exited. A second short call read the
redirected stdout and stderr: stdout contained only the standard Windows
PowerShell startup banner, and stderr contained a native PowerShell
argument-parsing error -- `Start-Process -ArgumentList` had not correctly
preserved the spaced absolute script path, so the child process received a
truncated `-File` argument and failed before ever reaching
`get_cvf_projection_drift_receipt.ps1`'s own logic. Per the absolute
prohibition on a second PID or relaunch, the worker did not attempt another
launch. The worker confirmed the target PID was gone, confirmed no orphaned
`powershell.exe` process remained, confirmed both Git roots stayed clean,
removed its own disposable temp directory, and returned
`BLOCKED_WITH_REASON`. Per the work order's explicit framing, R3 is the
final bounded recovery attempt and this worker does not propose or execute
an R4.

## Findings / Position

1. All pre-flight and reuse-justification checks passed, including the
   bundled pre-implementation autorun gate (`COMPLIANT: pre-implementation
   autorun gate passed in 4.89s.`) and the required
   `git diff --name-only 5b929dad9..HEAD -- scripts/` check (empty output),
   justifying reuse of R1's fixture totals without rerunning.
2. Fixture evidence was validly reused, not rerun: `53/53`, `91/91`,
   `144/144`, matching R1's accepted totals exactly.
3. The single R3-authorized supervised process launch (PID `22624`)
   returned immediately as designed and its metadata/sentinel were
   persisted correctly, satisfying the launch contract's own shape. The
   process itself, however, failed almost instantly -- not the target
   script, but the Windows PowerShell interpreter parsing its own launch
   arguments -- because `Start-Process -ArgumentList` did not correctly
   quote the absolute script path
   (`D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\scripts\get_cvf_projection_drift_receipt.ps1`),
   which contains spaces. The child process received a truncated `-File`
   argument (`D:\UNG`) and exited with a native argument-parsing error
   before `get_cvf_projection_drift_receipt.ps1` was ever invoked.
4. This is distinct from both prior rounds: R1 failed on a script-reported
   `PATH_ESCAPE` containment refusal after the script started; R2's script
   was actually running when the worker's own harness killed the parent
   call; here, in R3, the target script never started at all -- the
   failure occurred one layer earlier, in how the worker constructed the
   process-launch command. The supervised launch-and-poll contract itself
   (detached process, persisted PID, short polls, no synchronous wait)
   functioned exactly as designed; the defect is specific to this
   invocation's argument marshaling.
5. Both roots were confirmed clean immediately after the failed launch, no
   orphaned process remained, and the worker's own disposable temp
   directory was removed. The single real-root scan invocation permitted
   by this R3 dispatch is now consumed. Per the work order's explicit
   framing of R3 as the final bounded recovery attempt with no
   worker-proposed R4, this worker does not draft or recommend a further
   redispatch; that decision belongs to the reviewer.

## Risk / Corrective Action

Risk: none. The target script was never executed, so it never reached any
read or write logic against `ProvenanceRoot`, `PublicSyncRoot`, or
`CvfWebRoot`; `git status --porcelain` was confirmed empty in both roots
immediately after the failed launch. No fixture suite was rerun or failed
(evidence was validly reused), no second process was launched, no orphaned
process remained (confirmed by direct enumeration), and no forbidden action
of any kind (agent CLI, MCP, provider/API, browser, network, apply, copy,
commit, push, retry, or mutation) was taken.

Corrective action: none available to the worker inside Allowed scope for
this invocation -- the single authorized PID launch is already consumed and
a second launch is absolutely forbidden. The reviewer owns deciding how a
future dispatch (if one is separately authorized beyond this R0-R3
recovery sequence) should construct the process-launch argument list so a
spaced absolute path is not truncated -- for example, letting PowerShell's
own array-to-command-line conversion handle quoting through a differently
structured argument array, using `cmd.exe /c` with an explicitly
pre-quoted string, or shortening the vulnerable path segment by setting the
process working directory to the script's own folder and passing a
relative script name.

## Decision / Recommendation / Disposition

`BLOCKED_WITH_REASON`. Pre-flight checks passed, fixture evidence was
validly reused, and the single R3-authorized supervised process launch
failed almost instantly due to an argument-quoting defect in how the
worker invoked `Start-Process`, before the target script ever executed --
not a script-reported error, not a timeout, and not a completed scan. No
relaunch was attempted, honoring the absolute no-second-PID constraint.
Per the work order's explicit statement that R3 is the final bounded
recovery attempt, this worker does not recommend or execute an R4; the
reviewer owns deciding the next governed step for this pilot lane.

## Claim Boundary

This return proves that the pre-implementation gate passed, that fixture
evidence was validly reused (justified by an empty scripts-diff), and that
the single R3-authorized supervised process launch failed due to a
worker-side argument-quoting defect before the target script executed. It
does not claim a completed real-root scan, receipt/draft evidence,
row-level drift measurement, T2/T3 execution, or any mutation. It does not
claim a defect in the accepted T1 script, the work order text, or the
supervised launch-and-poll contract itself.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_finding_to_governance_learning.py`; `scripts/get_cvf_projection_drift_receipt.ps1` (confirmed never invoked; defect traced to the launch call instead) |
| literalTokensReviewed | required review-doc heading list (section names, not heading-prefixed: Purpose, Scope / Methodology, Findings / Position, Risk / Corrective Action, Checker Source Read-Ahead Block, Agent Operation Trace section, Delta Execution Claim Boundary section, Public Export Disposition, External Knowledge Intake Routing, rescan-hardening section, Corpus Completeness And Report Integrity, Finding-To-Governance Learning Disposition, Epistemic Process section, Claim Boundary, git status --short, Changed Files, Command Evidence, No-Commit Statement); `SELF_DECLARE_MARKER`; `RESPONDS_MARKER`; `AOT_FIELDS`; `DELTA_FIELDS`; `PUBLIC_EXPORT_TOKENS`; Finding-To-Governance defect class/learning lane/disposition/next-action vocabulary; `review` docType structural groups (target/source, scope/methodology, findings/position, risk/corrective action, decision/recommendation/disposition) |
| gateRunPurpose | confirm this worker-return packet's shape against the checker constants before reviewer handoff, used as confirmation evidence rather than as the means of discovering the required sections |
| claimBoundary | checker compliance proves packet structure only; the pre-flight, fixture-reuse, and supervised-launch-attempt results are proven by the ledger and the command evidence below |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated no-commit evidence worker |
| Provider or surface | local private provenance workspace; manual copy/paste handoff |
| Session or invocation | Continuous Projection T4 R3 worker execution, 2026-07-21 |
| Working directory | repository root |
| Command or tool surface | Git status/remote/rev-parse; PowerShell `Test-Path`; `python governance/compat/run_agent_autorun_workflow_gate.py`; `git diff --name-only` (fixture-reuse justification); one `Start-Process -PassThru` launch (failed at argument parse, before script execution); one `Get-Process` poll; direct file reads of the redirected stdout/stderr; process/root verification after the failed launch; temp-directory cleanup |
| Target paths | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_LEDGER_2026-07-20.md`; `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md` |
| Allowed scope source | paired GC-018 baseline and this work order, Required Artifact Manifest |
| Before status evidence | `git rev-parse --short HEAD` = `8824cb8c7` (matches required executionBaseHead); `git status --porcelain` empty in both the provenance root and the sibling public-sync root before any edit or launch attempt |
| After status evidence | `git status --short` (provenance root) shows exactly two modified paths (this file and the ledger, both already tracked from the R2 accepted return); `git status --porcelain` remains empty in the public-sync root; the two JSON evidence paths were never created because the target script never executed |
| Diff evidence | `git diff --name-status` shows only the two already-tracked review paths as modified; no other path changed |
| Approval boundary | bounded T4 pre-flight, fixture-reuse, and single-supervised-process-attempt evidence only, per Scope / Target / Owner Boundary in the work order |
| Claim boundary | no completed real-root scan, receipt/draft, T2/T3 execution, mutation, public-sync, commit, push, or production claim |
| Agent type | delegated no-commit evidence worker |
| Invocation ID | `continuous-projection-t4-bounded-pilot-r3-2026-07-21` |
| Expected manifest | up to four Allowed paths depending on run outcome; a blocked-launch-attempt run yields exactly two modified paths (ledger and worker return) plus zero new JSON evidence paths |
| Actual changed set | exactly two modified paths: the ledger and this worker return |
| Manifest delta | MATCH for the blocked-launch-attempt case |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred in this batch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | local T4 pre-flight, fixture-reuse justification, and single supervised real-root scan launch attempt only |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no T1 receipt, T2 draft, or CVF execution-control receipt was produced; the target script never executed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no action path exists; zero filesystem writes occurred inside the provenance or public-sync root, confirmed by direct post-attempt status checks |
| invocationBoundary | manual local Git/PowerShell/Python governance-check invocation only, per section 4's Allowed actions, plus exactly one supervised process launch (which failed at argument parse) and one short poll |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, browser, provider, or agent coding control exists in this batch |
| claimLanguage | this return proves a fail-closed, failed supervised-launch attempt only; it does not independently decide how a future dispatch should correct the argument-quoting defect |
| forbiddenExpansion | no second process launch, real-root scan, T2/T3 execution, provider, live, public, package, Web edit, MCP/CLI adapter, or model-router behavior is implemented or claimed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance no-commit worker return only. No public-sync
artifact or mutation is authorized or performed by this batch.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside repository, critique, or provider output was absorbed to produce this return |
| Matching local-view guard | N/A with reason: source verification against the paired baseline/work order and direct checker-source reading remain authority |
| Owner surface | paired T4 baseline and work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no outside input is promoted or absorbed by this worker return |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: this worker return is a bounded pilot evidence packet, not a
  rescan output, re-audit output, or intake-refresh output of any existing
  corpus, folder tree, or prior scan output, so no delta ledger, routing
  matrix, or semantic sampling record applies.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded T4 execution-evidence return, not a source corpus scan
- Corpus root: N/A with reason: the target script never executed
- Snapshot time: 2026-07-21 worker return
- Enumeration command: `rg --files --hidden --no-ignore docs/reviews docs/reviews/evidence`
- Manifest artifact or inline manifest: ledger and worker return present; receipt and draft absent
- Manifest hash: N/A with reason: no corpus manifest was produced
- Processing ledger artifact or inline ledger: paired T4 pilot ledger
- Allowed terminal statuses: READ; SKIPPED_WITH_REASON; DEFERRED; BLOCKED_UNREADABLE
- Reconciliation: manifest=4; ledger_terminal=2; exclusions=2; unresolved=0
- Unresolved files: 0
- Declared exclusions: real-root receipt and draft were not produced because the target script never executed
- Unreadable or unsupported files: 0
- Aggregation check: N/A with reason: no receipt rows exist
- Drift check: both Git roots remained clean; no corpus result exists
- Output traceability: executionBaseHead `8824cb8c7`, PID 22624, captured stderr, and this return
- Adversarial verification: reviewer must independently confirm no orphan and absent JSON paths
- Corpus verdict: BLOCKED

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
| --- | --- | --- | --- | --- |
| `Start-Process -ArgumentList` does not reliably preserve an absolute path element containing spaces when launching a detached PowerShell child process, causing the child to receive a truncated `-File` argument and fail before the target script executes, distinct from both the prior round's script-reported `PATH_ESCAPE` (R1) and the harness-timeout interruption of a running script (R2) | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | next action: reviewer decides how a future supervised-launch dispatch (if separately authorized beyond this R0-R3 recovery sequence) should construct the process-launch command so a spaced absolute path survives argument marshaling, for example via explicit re-quoting, `cmd.exe /c` with a pre-quoted string, or a shortened relative path from a working directory set to the script's own folder |

This batch discusses local process-launch mechanics and governance-gate
behavior only; it involves no runtime execution of the target script, no
provider call, and no cost/latency measurement beyond the sub-second
launch-to-exit interval, so the runtime/provider/cost learning-lane
requirement is N/A_WITH_REASON here.

## Epistemic Process Block

### Expected Result / Prediction

A clean committed HEAD matching the required executionBaseHead, two clean
Git roots, a passing pre-implementation gate, confirmed unchanged
`scripts/` content (justifying fixture reuse), and a detached
launch-and-poll process (avoiding R2's synchronous-call timeout) should let
the single real-root scan complete successfully and produce one accepted
receipt.

### Evidence Comparison

The pre-implementation gate passed and the scripts-diff check confirmed
zero script changes since R1, validating fixture-evidence reuse. The single
supervised process launch attempt diverged from expectation for a third,
distinct reason compared to R1 and R2: rather than a script-reported
`PATH_ESCAPE` (R1) or a harness-timeout interruption of a running script
(R2), the launched process itself failed almost instantly because
`Start-Process -ArgumentList` did not preserve the spaced absolute script
path, so the target script never executed at all.

### Contradiction Or Gap Disposition

There is no contradiction inside the accepted T1 script, the work order
text, or the supervised launch-and-poll contract as designed; all three
behaved as documented. The gap is in how this worker constructed the
`Start-Process -ArgumentList` array for a path containing spaces. This
cannot be closed inside worker scope because the single authorized PID
launch is already consumed and the absolute prohibition on a second PID
applies regardless of the failure's cause. It is not converted to a PASS,
and per the explicit R3 final-bounded-recovery framing, no fourth attempt
(R4) is proposed by this worker.

### Claim Update

This run may claim a passing pre-implementation gate, validly reused
fixture evidence (justified by an empty scripts-diff), and one supervised
process launch that failed due to an argument-quoting defect before the
target script executed. It may not claim a completed real-root scan,
receipt/draft evidence, or any measurement-contract row that depends on
Phase B having produced a receipt. It may not claim the accepted T1 script,
work order, or supervised-process contract itself is defective.

## git status --short

Before edit (recorded before Phase B's launch attempt):

```text
(clean; no output in either the provenance root or the sibling public-sync root)
```

After edit (current, at time of this return):

```text
 M docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_LEDGER_2026-07-20.md
 M docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md
```

Both paths were already tracked from the R2 accepted return and are
modified in place with R3's evidence; neither is staged. Neither JSON
evidence path exists, because the target script never executed.

## Changed Files

| Path | Change type | Notes |
| --- | --- | --- |
| `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_LEDGER_2026-07-20.md` | modified (unstaged) | updated with R3 pre-flight, fixture-reuse, and launch-attempt evidence |
| `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md` | modified (unstaged) | this worker-return packet, updated with R3 evidence |

No other existing tracked file was modified, renamed, or deleted. The two
JSON evidence paths (`docs/reviews/evidence/CVF_CONTINUOUS_PROJECTION_T4_REAL_ROOT_RECEIPT_2026-07-20.json`
and `docs/reviews/evidence/CVF_CONTINUOUS_PROJECTION_T4_REAL_ROOT_REVIEW_DRAFT_2026-07-20.json`)
were never created because the target script never executed.

## Command Evidence

| Command | Result |
| --- | --- |
| `git rev-parse --short HEAD` (before edit) | `8824cb8c7` -- PASS, matches required executionBaseHead |
| `git status --porcelain` (provenance root, before edit) | empty -- PASS, clean worktree |
| `git remote get-url origin` (provenance root) | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git` -- PASS, matches policy `provenanceRemote` |
| `git status --porcelain` (public-sync root, before edit) | empty -- PASS, clean sibling root |
| `git remote get-url origin` (public-sync root) | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` -- PASS, matches policy `publicRemote` |
| `Test-Path EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web` | path exists -- PASS |
| `Test-Path scripts\cvf_projection_policy.json` | path exists -- PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5f5c28b85 --head HEAD` | `COMPLIANT: pre-implementation autorun gate passed in 4.89s.` -- PASS |
| `git diff --name-only 5b929dad9..HEAD -- scripts/` | empty output -- PASS, justifies fixture-evidence reuse without rerunning |
| Phase A fixture suites | REUSED (not rerun): `53/53`, `91/91`, `144/144`, per R3's fixture-reuse instruction |
| `Start-Process -FilePath powershell.exe -ArgumentList (...) -WindowStyle Hidden -PassThru` (single Phase B launch, PID `22624`) | launch call returned immediately with a valid PID; metadata and sentinel persisted -- PASS as a launch mechanism |
| Poll 1 (`Get-Process -Id 22624`, short bounded call) | `STATUS=EXITED` -- process already gone by the first poll |
| stdout redirect file inspection | 174 bytes, standard PowerShell startup banner only, no receipt -- BLOCKED |
| stderr redirect file inspection | 158 bytes: `Processing -File 'D:\UNG' failed because the file does not have a '.ps1' extension...` -- BLOCKED, argument-quoting failure before script execution |
| target PID (`22624`) still-running check (post-exit) | `False` -- confirmed not running |
| `powershell.exe` orphan process check (post-exit) | none found -- PASS, no orphan |
| `git status --porcelain` (both roots, immediately after the failed launch) | empty in both roots -- PASS, confirms no mutation |
| Phase C (persist receipt/draft) | NOT_RUN: Phase B did not produce a receipt to persist |
| Phase D (16-row measurement ledger) | NOT_RUN: no receipt exists to cross-check; the ledger instead records the pre-flight, reuse-justification, and launch-attempt evidence per the Measurement Contract's `NOT_APPLICABLE_WITH_REASON` rows |
| `python governance/compat/run_worker_return_fast_gate.py` | ran after this file and the ledger were authored; result recorded below |

## No-Commit Statement

Reviewer disposition on 2026-07-21: `ACCEPTED_BLOCKED_RETURN_FINAL`. R3
honored the one-PID and no-relaunch ceiling, captured the space-bearing-path
argument failure, left no orphan, and kept both roots clean. The T1 script did
not execute, so no receipt or pilot result is accepted. R3 is final; T4 closes
`CLOSED_BLOCKED_BOUNDED` without R4.

`WORKER_MUST_NOT_COMMIT honored`. This worker performed zero `git add`,
`git commit`, `git push`, `git stage`, or any other staging/commit
operation. Both modified files remain unstaged at the time of this return.

WORKER_EXPERIENCE_RETRO:
frictionLevel: MEDIUM
frictionType: GATE_SURPRISE
observedStep: Phase B, the single supervised process launch, where
  Start-Process -ArgumentList truncated the spaced absolute script path
  before the target script could execute
preventiveControlCandidate: HELPER_DIAGNOSTIC
