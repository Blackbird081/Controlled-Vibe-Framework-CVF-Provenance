# CVF Continuous Projection T4 Bounded Pilot Ledger

Memory class: governed-evidence-ledger

docType: review

Status: REVIEWER_ACCEPTED_BLOCKED_FINAL

Batch ID: CVF-CONTINUOUS-PROJECTION-T4

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: `8824cb8c7`

Date: 2026-07-21

## Purpose

Record the bounded T4 pilot evidence for `CVF-CONTINUOUS-PROJECTION-T4` R3,
the final bounded recovery attempt. R2 consumed its single authorized
real-root scan invocation when the worker's own tool-execution harness
terminated the synchronous invocation before the script's 3600-second
ceiling. R3's corrected Phase B launches exactly one hidden, detached
`powershell.exe` process via `Start-Process -PassThru`, persists its PID and
disposable output paths, and supervises that PID through short bounded
polls instead of a synchronous blocking call. This R3 run reused R1's
fixture evidence (confirmed unchanged via a scripts-diff check) and
consumed its own single fresh real-root scan invocation; that launched
process exited almost immediately with a PowerShell argument-splitting
failure before it ever reached the target script, not a scan-logic error,
not a timeout, and not a completed scan. No receipt, draft, or
measurement-contract row evidence exists for this run.

## Target / Source

Target: the four Allowed T4 outputs named in the paired work order's Required
Artifact Manifest. Source: `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_AND_CLOSURE_2026-07-20.md`,
section 6 (Pre-Flight Checks), Phase A/Phase B of section 8 (Execution
Instructions), and section 6C (Worker Autonomy / No-Question Rule);
`scripts/get_cvf_projection_drift_receipt.ps1` (the accepted T1 script);
`docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0043.md` and
`CVF_ADIF-0044.md` (the two prior-round execution-envelope defect records
this R3 contract is designed to avoid).

## Scope / Methodology

Per the R3 dispatch instruction, the worker ran every pre-flight command
before creating any output, confirmed fixture reuse eligibility via a
scripts-diff check (rather than rerunning the three fixture suites), then
attempted Phase B (the single fresh real-root scan) using the supervised
launch-and-poll contract:

1. `git rev-parse --short HEAD`
2. `git status --porcelain` (both roots)
3. `git remote get-url origin` (both roots)
4. `Test-Path EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web`
5. `Test-Path scripts\cvf_projection_policy.json`
6. `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5f5c28b85 --head HEAD`
7. `git diff --name-only 5b929dad9..HEAD -- scripts/` (fixture-reuse justification)

All seven pre-flight/reuse-justification checks passed. Phase B then:

1. created one unique disposable directory under `%TEMP%`, outside all three
   target roots, and reserved four paths inside it (stdout, stderr,
   metadata, launch sentinel);
2. confirmed neither the metadata path nor the sentinel path already
   existed (guarding against an accidental second launch);
3. resolved the script path and all four T1 input paths (`ProvenanceRoot`,
   `PublicSyncRoot`, `CvfWebRoot`, `PolicyPath`) to absolute paths;
4. launched exactly one hidden `powershell.exe` process via
   `Start-Process -WindowStyle Hidden -PassThru`, with the working directory
   set to the provenance root, redirecting stdout/stderr to the two
   reserved files, and passing `-ScanTimeoutSeconds 3600`;
5. immediately persisted the returned PID, launch time, resolved paths, and
   `scanInvocationCount=1` to the metadata file, then wrote the launch
   sentinel; the launch call itself returned immediately without
   synchronously waiting.

The worker then polled the persisted PID with one short, separately issued
tool call (well under the 60-second bound). That single poll found the
process had already exited. The worker immediately read the redirected
stdout and stderr files (a second short call) and found a PowerShell
argument-splitting failure: the spaced absolute script path was truncated
at its first space by `Start-Process -ArgumentList`, so the child process
received `-File 'D:\UNG'` and failed before ever reaching
`get_cvf_projection_drift_receipt.ps1`. This is a launch-mechanics defect in
how the worker invoked `Start-Process`, not a defect in the accepted T1
script and not a result of the script's own scan logic; the script itself
was never executed. Per the absolute prohibition on a second PID, the
worker did not relaunch. The worker then confirmed the target PID was not
running, confirmed no other `powershell.exe` process existed (no orphan),
confirmed both Git roots remained clean, and cleaned up its own disposable
temp directory before returning `BLOCKED_WITH_REASON`.

## Findings / Position

### Pre-Flight And Reuse-Justification Results

| Check | Expected | Observed | Disposition |
| --- | --- | --- | --- |
| `git rev-parse --short HEAD` | matches required executionBaseHead `8824cb8c7` | `8824cb8c7` | PASS |
| `git status --porcelain` (provenance root) | empty | empty | PASS |
| `git remote get-url origin` (provenance root) | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git` per policy `expectedRemotes.provenanceRemote` | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git` | PASS |
| `git status --porcelain` (public-sync root) | empty | empty | PASS |
| `git remote get-url origin` (public-sync root) | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` per policy `expectedRemotes.publicRemote` | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` | PASS |
| `Test-Path EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web` | `True` | `True` (path exists) | PASS |
| `Test-Path scripts\cvf_projection_policy.json` | `True` | `True` (path exists) | PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5f5c28b85 --head HEAD` | COMPLIANT | `COMPLIANT: pre-implementation autorun gate passed in 4.89s.` | PASS |
| `git diff --name-only 5b929dad9..HEAD -- scripts/` | empty (no script changes since R1's executionBaseHead) | empty | PASS -- justifies reusing R1's fixture totals without rerunning |

### Phase A - Fixture Evidence Reuse (No Rerun)

Per the R3 dispatch instruction, the three disposable-fixture suites were
not rerun. The scripts-diff check above confirms `scripts/` is byte-for-byte
unchanged between R1's `executionBaseHead` (`5b929dad9`) and this run's
`HEAD` (`8824cb8c7`), so R1's accepted fixture totals are reused as R3
evidence:

| Suite | Reused result (from R1, accepted at `5b929dad9`) |
| --- | --- |
| `scripts/test_cvf_projection_drift_receipt.ps1` | `Total: 53, Pass: 53, Fail: 0` -- PASS (reused) |
| `scripts/test_cvf_projection_review_packet.ps1` | `Total: 91, Pass: 91, Fail: 0` -- PASS (reused) |
| `scripts/test_cvf_projection_audience_gate.ps1` | `Total: 144, Pass: 144, Fail: 0` -- PASS (reused) |

### Phase B - Single Supervised Real-Root Receipt Process

Launch (all four T1 input paths and the script path resolved to absolute
paths before launch; working directory set to the provenance root; stdout
and stderr redirected to two disposable files under a unique `%TEMP%`
subdirectory outside all three target roots):

```text
Start-Process -FilePath "powershell.exe" -ArgumentList @(
    '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $scriptPath,
    '-ProvenanceRoot', $provRoot, '-PublicSyncRoot', $pubRoot,
    '-CvfWebRoot', $webRoot, '-PolicyPath', $policyPath,
    '-ScanTimeoutSeconds', '3600'
) -WorkingDirectory $provRoot -WindowStyle Hidden `
  -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath -PassThru
```

Result: PID `22624` was returned immediately (launch call did not block);
metadata (PID, launch time, resolved paths, `scanInvocationCount=1`) and the
launch sentinel were persisted to the disposable directory immediately
after.

Poll 1 (first short, separately issued bounded call after launch): `Get-Process
-Id 22624` returned nothing -- `STATUS=EXITED`. The process had already
terminated by the time of this first poll.

Immediate output inspection (second short bounded call):

- stdout redirect file: 174 bytes -- contained only the standard Windows
  PowerShell banner text ("Windows PowerShell", copyright line, and the
  "Install the latest PowerShell" notice), never a receipt.
- stderr redirect file: 158 bytes -- contained exactly:
  `Processing -File 'D:\UNG' failed because the file does not have a '.ps1'
  extension. Specify a valid Windows PowerShell script file name, and then
  try again.`

Root cause: `Start-Process -ArgumentList` with an array element containing
spaces (the absolute script path `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\scripts\get_cvf_projection_drift_receipt.ps1`)
was not correctly re-quoted by the launcher, so the child `powershell.exe`
process received a truncated `-File` argument (`D:\UNG`, split at the first
space) and refused to execute before ever reaching
`get_cvf_projection_drift_receipt.ps1`'s own logic. The accepted T1 script
was never invoked; this is a defect in the worker's own process-launch
mechanics for this dispatch, not in the script, not in the work order text,
and not a result the script's own timeout or scan logic ever produced.

Post-exit verification (performed immediately, before any further action):

| Check | Result |
| --- | --- |
| target PID (`22624`) still running | `False` |
| any `powershell.exe` process running (orphan check) | none found |
| `git status --porcelain` (provenance root) | empty |
| `git status --porcelain` (public-sync root) | empty |
| `git rev-parse --short HEAD` | `8824cb8c7` (unchanged) |

Diagnostic classification:

| Field | Value |
| --- | --- |
| stage | Phase B, single supervised real-root scan process |
| class | worker launch-mechanics failure (argument-splitting on an absolute path containing spaces, occurring before the target script executed) |
| retryability | NOT_RETRYABLE: this was the single R3-authorized invocation; the absolute prohibition on a second PID, relaunch, or replacement process applies regardless of the failure's cause, and R3 is the final bounded recovery attempt with no self-authorized R4 |
| user action | reviewer must decide how a future dispatch (if any) should launch the process so the spaced absolute path survives `Start-Process -ArgumentList` marshaling -- for example, wrapping the argument list construction so PowerShell's own array-to-command-line conversion quotes each element correctly, or invoking through `cmd.exe /c` with an explicitly pre-quoted command string, or changing working directory to the script's own folder and passing a relative script name to shorten the vulnerable path segment |
| elapsed time | sub-second; the process exited almost immediately upon failing to parse its own `-File` argument, well before either the 60-second poll bound or the script's 3600-second internal ceiling could matter |
| exit code | not captured (the process was gone by the first poll; per the accepted R3 contract, a detached process's exit code is not guaranteed durable across separate worker shell calls, and receipt/stderr content remains authoritative) |
| diagnostic code | none from the target script (it never ran); the captured diagnostic is Windows PowerShell's own native `-File` argument-parsing error |
| safe message | the supervised process was launched successfully (one real PID, immediately persisted) but failed before reaching the target script because its own argument list was not correctly quoted for a path containing spaces; no receipt, partial output, or target-root write resulted |

This is a genuine worker-side launch-mechanics defect distinct from both R1
(`PATH_ESCAPE`, a script-reported containment refusal) and R2 (a
harness-timeout interruption of a script that was actually running). Here,
the process launched and exited almost instantly without the target script
ever executing. The worker has no Allowed action that both respects the
absolute no-second-PID/no-relaunch constraint and corrects the launch
argument construction within this invocation; the single real-root scan
invocation permitted by this R3 dispatch is now consumed, and per the work
order's explicit instruction, R3 is the final bounded recovery attempt with
no worker-proposed R4.

## Risk / Corrective Action

Risk: none from the worker's own action. Zero filesystem writes occurred
inside `ProvenanceRoot`, `PublicSyncRoot`, or `CvfWebRoot` -- the target
script was never executed, so it never reached any read or write logic at
all, and `git status --porcelain` was confirmed empty in both roots
immediately after the failed launch. No fixture suite was rerun or failed
(evidence was validly reused per the R3 instruction), no second process was
launched, no orphaned process remained (confirmed by direct enumeration),
and no forbidden action of any kind (agent CLI, MCP, provider/API, browser,
network, apply, copy, commit, push, retry, or mutation) was taken.

Corrective action: none available to the worker inside Allowed scope for
this invocation, because the single authorized PID launch is already
consumed and a second launch is absolutely forbidden. The reviewer owns
deciding how any future dispatch should construct the `Start-Process`
argument list (or use an alternative launch mechanism) so that an absolute
path containing spaces is not truncated by argument marshaling, and owns
deciding whether the R3 outcome (final bounded recovery attempt, per the
work order) closes this pilot lane or requires a separately authorized new
tranche outside the R0-R3 recovery sequence.

## Measurement Contract Evidence

Per the paired GC-018's Measurement Contract, the following rows are
reported as `NOT_APPLICABLE_WITH_REASON` because Phase B never produced a
receipt:

| Metric | Worker evidence |
| --- | --- |
| fixture stability | CONFIRMED (reused from R1, script-diff-justified): `53/53`, `91/91`, `144/144` -- all three suites passed with zero failures at the last point `scripts/` changed |
| false positives | NOT_APPLICABLE_WITH_REASON: the target script never executed; no receipt rows exist to inspect |
| missed drift | NOT_APPLICABLE_WITH_REASON: the target script never executed; no receipt rows exist to inspect |
| reviewer effort | preparationMinutes: pre-flight, fixture-reuse justification, one supervised process launch-and-poll cycle (sub-second to detection), and stop-condition diagnosis; no receipt or draft preparation occurred because none was produced |
| packet usefulness | NOT_APPLICABLE_WITH_REASON: no receipt or draft was produced |
| no mutation | CONFIRMED: `git status --short` was empty in both roots immediately before and immediately after the launch attempt; the target script never executed and therefore never reached any file-write logic; no orphaned `powershell.exe` process remained after the single launched PID exited |

## Decision / Recommendation / Disposition

`BLOCKED_WITH_REASON`. The worker launched exactly one supervised hidden
process for the single R3-authorized real-root scan invocation; that
process exited almost immediately due to a `Start-Process` argument-quoting
failure on a spaced absolute path, before the target script ever executed
-- not a script-reported error, not a timeout, and not a completed scan. No
relaunch or second PID was attempted, honoring the absolute constraint for
this final bounded recovery attempt. Per the work order's explicit
instruction that R3 is the final bounded recovery attempt with no
worker-proposed R4, this worker does not recommend or draft a further
redispatch; the reviewer owns deciding the next governed step for this
pilot lane.

## Claim Boundary

This ledger proves that the pre-implementation gate passed, that R1's
fixture evidence was validly reused (justified by an empty `scripts/`
diff), and that the single R3-authorized supervised process launch failed
due to a worker-side argument-quoting defect before the target script
executed. It does not claim a completed real-root scan, receipt/draft
evidence, row-level drift measurement, or any mutation. It does not claim a
defect in the accepted T1 script, the work order text, or the supervised
launch-and-poll contract itself; the failure traces to how the worker
constructed the `Start-Process` argument list for a path containing spaces.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_finding_to_governance_learning.py`; `scripts/get_cvf_projection_drift_receipt.ps1` (confirmed never invoked, defect traced to the launch call instead) |
| literalTokensReviewed | Agent Operation Trace section label set; Epistemic Process section required subsections (Expected Result / Prediction, Evidence Comparison, Contradiction Or Gap Disposition, Claim Update); Delta Execution Claim Boundary section field set; Overlap And Novelty Classification section; Finding-To-Governance defect class, learning lane, disposition, and next-action vocabulary |
| gateRunPurpose | confirm this ledger's shape against the checker constants before reviewer handoff, used as confirmation evidence rather than as the means of discovering the required sections |
| claimBoundary | checker compliance proves packet structure only; the pre-flight, fixture-reuse, and supervised-launch-attempt results are proven by the Findings / Position section above |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated no-commit evidence worker |
| Provider or surface | local private provenance workspace; manual copy/paste handoff |
| Session or invocation | Continuous Projection T4 R3 worker execution, 2026-07-21 |
| Working directory | repository root |
| Command or tool surface | Git status/remote/rev-parse; PowerShell `Test-Path`; `python governance/compat/run_agent_autorun_workflow_gate.py`; `git diff --name-only` (fixture-reuse justification); one `Start-Process -PassThru` launch of `scripts/get_cvf_projection_drift_receipt.ps1` (failed at argument parse, before script execution); one `Get-Process` poll; direct file reads of the redirected stdout/stderr; process/root verification after the failed launch; temp-directory cleanup |
| Target paths | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_LEDGER_2026-07-20.md`; `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md` |
| Allowed scope source | paired GC-018 baseline and this work order, Required Artifact Manifest |
| Before status evidence | `git rev-parse --short HEAD` = `8824cb8c7` (matches required executionBaseHead); `git status --porcelain` empty in both the provenance root and the sibling public-sync root before any edit or launch attempt |
| After status evidence | `git status --short` (provenance root) shows exactly two modified paths (this ledger and the worker return, both already tracked from the R2 accepted return); `git status --porcelain` remains empty in the public-sync root; the two JSON evidence paths were never created because the target script never executed |
| Diff evidence | `git diff --name-status` shows only the two already-tracked review paths as modified; no other path changed |
| Approval boundary | bounded T4 pre-flight, fixture-reuse, and single-supervised-process-attempt evidence only |
| Claim boundary | no completed real-root scan, receipt/draft, T2/T3 execution, mutation, public-sync, commit, push, or production claim |
| Agent type | delegated no-commit evidence worker |
| Invocation ID | `continuous-projection-t4-bounded-pilot-r3-2026-07-21` |
| Expected manifest | up to four Allowed paths depending on run outcome; a blocked-launch-attempt run yields exactly two modified paths (ledger and worker return) plus zero new JSON evidence paths |
| Actual changed set | exactly two modified paths: this ledger and the worker return |
| Manifest delta | MATCH for the blocked-launch-attempt case |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred in this batch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | local T4 pre-flight, fixture-reuse justification, and single supervised real-root scan launch attempt only |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no T1 receipt, T2 draft, or CVF execution-control receipt was produced; the target script never executed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no action path exists; zero filesystem writes occurred inside the provenance or public-sync root, confirmed by direct post-attempt status checks |
| invocationBoundary | manual local Git/PowerShell/Python governance-check invocation only, plus exactly one supervised process launch (which failed at argument parse) and one short poll |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, browser, provider, or agent coding control exists in this batch |
| claimLanguage | this ledger proves a fail-closed, failed supervised-launch attempt only; it does not independently decide how a future dispatch should correct the argument-quoting defect |
| forbiddenExpansion | no second process launch, real-root scan, T2/T3 execution, provider, live, public, package, Web edit, MCP/CLI adapter, or model-router behavior is implemented or claimed |

## Overlap And Novelty Classification

NOT_APPLICABLE_WITH_REASON: this ledger absorbs no outside repository,
critique, or provider output. Its only cited material is this repository's
own source (`scripts/get_cvf_projection_drift_receipt.ps1`, the paired
dispatch work order, and ADIF-0043/ADIF-0044), which is CVF-owned source and
prior governed defect records, not outside absorbed knowledge, so no
overlap-versus-novelty classification against an existing CVF owner surface
applies.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside repository, critique, or provider output was absorbed |
| Matching local-view guard | N/A with reason: repository source and direct execution evidence remain authority |
| Owner surface | paired T4 baseline and work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no outside input is promoted or absorbed by this ledger |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded T4 execution-evidence review, not a source corpus scan
- Corpus root: N/A with reason: the target script never executed
- Snapshot time: 2026-07-21 reviewer closure
- Enumeration command: `rg --files --hidden --no-ignore docs/reviews docs/reviews/evidence`
- Manifest artifact or inline manifest: ledger and worker return present; receipt and draft absent
- Manifest hash: N/A with reason: no corpus manifest was produced
- Processing ledger artifact or inline ledger: this evidence ledger
- Allowed terminal statuses: READ; SKIPPED_WITH_REASON; DEFERRED; BLOCKED_UNREADABLE
- Reconciliation: manifest=4; ledger_terminal=2; exclusions=2; unresolved=0
- Unresolved files: 0
- Declared exclusions: real-root receipt and draft were not produced because the target script never executed
- Unreadable or unsupported files: 0
- Aggregation check: N/A with reason: no receipt rows exist
- Drift check: both Git roots remained clean; no corpus result exists
- Output traceability: executionBaseHead `8824cb8c7`, PID 22624, captured stderr, and worker return
- Adversarial verification: reviewer confirmed no `powershell.exe` orphan and both JSON paths absent
- Corpus verdict: BLOCKED

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
