# CVF Agent Work Order - LPCI2-T10 PolicyLocal Foundation Readiness For Claude

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-07

dispatchBaseHead: 1729683b
executionBaseHead: 1729683b
closureBaseHead: N/A - worker must return uncommitted packet for Codex review

Commit mode: WORKER_MUST_NOT_COMMIT

Risk class: R1_LOCAL_SCRIPT_AND_EVIDENCE_ONLY

Worker: Claude

Reviewer / closer: Codex or operator-designated reviewer

## Purpose

Create a source-verified T10 PolicyLocal foundation readiness packet before
any corpus expansion or deployment work. The worker must add a deterministic
local verifier and a machine-readable readiness report that re-check the T9
foundation artifacts without rerunning provider calls, chat runtime, vector
retrieval, corpus expansion, or production deployment.

This work order is a foundation hardening step. It prepares PolicyLocal for
later corpus expansion or deployment work orders by making the existing T9
external artifacts reproducible, hash-bound, schema-checked, and assertion-
checked from a single local command.

## Startup Acknowledgment

Startup acknowledged: current mode=lpci2_t9_correction_clean_closed; active
handoff=AGENT_HANDOFF_V16_2026-06-06.md; next allowed move=author a fresh
source-verified PolicyLocal foundation, corpus expansion, or deployment work
order; parked checkpoint=DEP2/Redis/receipt-anchor lanes remain parked.

## Authority Chain

| Authority item | Path / evidence | Disposition |
|---|---|---|
| Operator instruction | 2026-06-07 request: proceed and prepare Claude work | ACCEPT |
| Session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Machine state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` | ACCEPT |
| T9 roadmap | `docs/roadmaps/CVF_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_ROADMAP_2026-06-07.md` | ACCEPT |
| T9 work order | `docs/work_orders/CVF_WO_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_2026-06-07.md` | ACCEPT |
| T9 completion | `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` | ACCEPT |
| Query receipt model | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | ACCEPT |
| Retrieval trace design | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | ACCEPT |
| Boundary contract | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | ACCEPT |
| Corpus scan registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | ACCEPT |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ACCEPT |

Authority boundary:

- This work order authorizes only T10 local foundation readiness evidence.
- If any source artifact conflicts with this work order, stop and return to
  Codex with the conflict.
- This work order does not authorize corpus expansion, deployment, public-sync,
  legal advice quality claims, current-law claims, provider calls, LLM/chat
  runtime, vector/embedding retrieval, package installation, or production
  readiness.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Orchestrator / dispatcher | Codex | Source-verify and dispatch this work order |
| Worker / implementer | Claude | Create verifier, readiness report, and worker return packet; do not commit |
| Reviewer / closer | Codex or operator-designated reviewer | Review worker diff, run closure gates, commit if accepted |
| Operator checkpoint | Operator | Required only for scope expansion, live/provider proof, public-sync, corpus expansion, deployment, or claim-boundary change |

## Worker Autonomy / No-Question Rule

Claude must proceed autonomously inside Allowed scope. In-scope schema
assertion failures, hash mismatches, missing `N/A with reason`, stale evidence
wording, and gate failures must be repaired and rerun by Claude before return.

Claude must stop only when the required repair would exceed Allowed scope,
touch a forbidden path, consume secrets or live quota, run provider calls, open
public-sync, change risk class, add dependencies, expand corpus input, or alter
the claim boundary.

## Scope

Allowed scope:

- Create
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-foundation-readiness.py`.
- Generate
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-foundation-readiness-report.json`.
- Create worker return packet:
  `docs/reviews/CVF_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_WORKER_RETURN_2026-06-07.md`.
- Optionally update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
  and `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` only if the
  readiness report records a new T10 finding or next-action state.
- Run local deterministic verification commands and governance gates.

Forbidden scope:

- Provider calls, live keys, API quota, browser live proof, or release gate.
- Chat runtime, LLM answer generation, vector or embedding retrieval.
- Corpus expansion beyond the existing two PolicyLocal DOCX-derived records.
- Current-law transition or EC-02 freshness update before 2026-07-01.
- Production, hosted, public, release, legal-advice, provider-quality,
  cost/performance, or current-law readiness claims.
- Changes under `EXTENSIONS/*`, `.github/*`, `governance/compat/*`,
  `scripts/*`, package manifests, lockfiles, public-sync clone, or deployment
  configuration.
- Changes to active session front door, state registry, or active handoff by
  Claude. Reviewer handles session sync if the worker packet is accepted.

Risk ceiling:

- R1 local deterministic script/report only.

## Required First Reads

Before edits, Claude must read:

- `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` -
  corrected T9 evidence, assertion matrix, and external artifact hashes.
- `docs/work_orders/CVF_WO_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_2026-06-07.md` -
  T9 claim boundary and acceptance query obligations.
- `docs/roadmaps/CVF_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_ROADMAP_2026-06-07.md` -
  closed roadmap and next-authorized PolicyLocal move.
- `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` - receipt
  schema and enforcement rules.
- `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` - chunk schema
  and no-vector retrieval boundary.
- `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` -
  EC-01 through EC-04 and 2026-07-01 freshness review condition.
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` - GC-051 current
  PolicyLocal registry state.

## Pre-Flight Checks

Run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-foundation-readiness.py'
Test-Path 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-foundation-readiness-report.json'
Get-FileHash 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-search-runtime.py'
Get-FileHash 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-chunk-generator.py'
Get-FileHash 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json'
Get-FileHash 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-chunks.json'
Get-FileHash 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-query-receipts-acceptance.json'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 1729683b --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 1729683b --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 1729683b --head HEAD --enforce
```

Expected pre-flight:

- HEAD is `1729683b` or a later reviewer-approved work-order dispatch commit.
- `git status --short` shows only this work-order dispatch file before Claude
  begins worker edits, or is clean after Codex commits the dispatch packet.
- The two T10 output paths do not already exist at dispatch.
- The five T9 artifact hashes match the T9 External Artifact Hash Manifest.
- Pre-dispatch and pre-implementation autorun gates pass before worker edits.

If a pre-flight check fails, Claude must record the failed command and stop
unless the failure is inside Allowed scope and repairable without changing the
claim boundary.

## Dispatch Gate Evidence

Codex dispatch checks on base `1729683b`:

| Gate | Command | Result |
|---|---|---|
| Diff whitespace | `git diff --check` | PASS |
| Work-order dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 1729683b --head HEAD --enforce` | PASS |
| Pre-dispatch autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 1729683b --head HEAD` | PASS |

## Source-Fidelity Pass

Existing paths verified by Codex before dispatch:

- `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md`
- `docs/work_orders/CVF_WO_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_2026-06-07.md`
- `docs/roadmaps/CVF_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_ROADMAP_2026-06-07.md`
- `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md`
- `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md`
- `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

Planned new paths clearly marked as NEW:

- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-foundation-readiness.py`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-foundation-readiness-report.json`
- `docs/reviews/CVF_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_WORKER_RETURN_2026-06-07.md`

Current Runtime Freshness Verification:

| Current artifact | Dispatch evidence | Result |
|---|---|---|
| `policylocal-foundation-readiness.py` | `Test-Path` at dispatch | ABSENT |
| `policylocal-foundation-readiness-report.json` | `Test-Path` at dispatch | ABSENT |
| `policylocal-search-runtime.py` | T9 hash manifest and dispatch `Get-FileHash` | PRESENT |
| `policylocal-chunk-generator.py` | T9 hash manifest and dispatch `Get-FileHash` | PRESENT |
| `policylocal-corpus-records.json` | schema parse at dispatch | PRESENT, schema `policylocal.corpusRecords.t8.v1`, records=2 |
| `policylocal-chunks.json` | schema parse at dispatch | PRESENT, schema `policylocal.chunk.t8.v1`, chunks=76 |
| `policylocal-query-receipts-acceptance.json` | schema parse at dispatch | PRESENT, schema `policylocal.queryReceipt.t8.v1`, receipts=5 |

Source Verification Block:

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: T9 closure is bounded and local deterministic | `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` | lines 5, 81 | `CLOSED_PASS_BOUNDED` | T9 completion review | ACCEPT |
| EXISTS: T9 external artifact hash manifest is present | `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` | lines 340-348 | `External Artifact Hash Manifest` | T9 completion review | ACCEPT |
| EXISTS: T9 acceptance assertion matrix is present | `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` | lines 319-338 | `Acceptance Receipt Assertion Matrix` | T9 completion review | ACCEPT |
| VALUE_SET: corrected receipt hash for acceptance receipts | `docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md` | line 347 | `policylocal-query-receipts-acceptance.json` | T9 external artifact hash manifest | ACCEPT |
| EXISTS: receipt schema version | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | lines 11, 57 | `schemaVersion` | `policylocal.queryReceipt.t8.v1` | ACCEPT |
| RUNTIME_BEHAVIOR: every query must emit a receipt | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | line 96 | `receipt` | LPCI query receipt model enforcement rules | ACCEPT |
| RUNTIME_BEHAVIOR: escalate receipts require empty selected candidates | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | lines 97, 105-106 | `selectedCandidateIds` | LPCI query receipt model enforcement rules | ACCEPT |
| RUNTIME_BEHAVIOR: freshness disclosure must be true for not-yet-in-force selected candidates | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | lines 98-99 | `freshnessDisclosureApplied` | LPCI query receipt model enforcement rules | ACCEPT |
| EXISTS: chunk schema version | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | line 72 | `schemaVersion` | `policylocal.chunk.t8.v1` | ACCEPT |
| EXISTS: chunk integrity field | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | lines 66, 106 | `chunkHash` | LPCI retrieval trace design | ACCEPT |
| RUNTIME_BEHAVIOR: no vector retrieval in current design scope | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | lines 33-35, 122-124 | `vector` | LPCI retrieval trace design | ACCEPT |
| EXISTS: boundary contract version | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | lines 11, 49 | `contractVersion` | `policylocal.boundaryContract.t7.v1` | ACCEPT |
| VALUE_SET: EC-01 through EC-04 exist | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | lines 63, 72, 82, 91 | `escalateConditions` | LPCI boundary contract | ACCEPT |
| RUNTIME_BEHAVIOR: effectiveDate transition review after 2026-07-01 | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | lines 130, 170, 183 | `reviewRequired` | LPCI boundary contract lifecycle | ACCEPT |
| EXISTS: T9 roadmap authorizes a fresh PolicyLocal foundation work order | `docs/roadmaps/CVF_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_ROADMAP_2026-06-07.md` | lines 87-88 | `fresh operator-authorized work order` | T9 roadmap closure addendum | ACCEPT |
| EXISTS: GC-051 PolicyLocal T9 state records chunk and receipt evidence | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | lines 847-851, 862, 913 | `policylocal` | GC-051 corpus scan registry | ACCEPT |

New T10 artifact fields:

| New field | Purpose | Not sourced from current runtime? | Runtime claim blocked until implementation? | Validation expectation |
|---|---|---|---|---|
| `schemaVersion` = `policylocal.foundationReadiness.t10.v1` | Version T10 readiness report | Yes | Yes | verifier writes and worker return packet cites |
| `artifactHashes` | Bind each T9 external artifact to sha256 | Yes | Yes | compare against T9 hash manifest |
| `schemaChecks` | Record corpus/chunk/receipt schema checks | Yes | Yes | all required schema checks PASS |
| `receiptAssertions` | Record AQ-01 through AQ-05 required-vs-observed values | Yes | Yes | all assertion rows PASS |
| `boundaryChecks` | Record no-provider/no-LLM/no-vector/static boundary checks | Yes | Yes | all boundary checks PASS or blocked with reason |
| `freshnessReviewRequiredOnOrAfter` | Preserve EC-02 review date | Yes | Yes | exact value `2026-07-01` |
| `claimBoundary` | Preserve bounded claim text | Yes | Yes | no production/current-law/legal-advice claim |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or closure requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| T9 closed only local deterministic mechanics | Scope; Claim Boundary | worker return packet | claim-boundary scan | READY_FOR_WORKER |
| PolicyLocal foundation requires fresh work order | Authority Chain | this work order | source verification row for T9 roadmap lines 87-88 | READY_FOR_WORKER |
| T9 external artifacts are not git-tracked | Evidence Requirements | `artifactHashes` in readiness report | `Get-FileHash` on five T9 artifacts | READY_FOR_WORKER |
| T9 acceptance evidence must not drift | Execution Plan | `receiptAssertions` in readiness report | parse existing acceptance receipts without rerun | READY_FOR_WORKER |
| EC-02 freshness review required on or after 2026-07-01 | Scope; Acceptance Criteria | `freshnessReviewRequiredOnOrAfter` | verify boundary contract lifecycle | READY_FOR_WORKER |
| No deployment or corpus expansion in T10 | Forbidden scope | worker return packet | changed-file and claim scan | READY_FOR_WORKER |

## Work-Order Fulfillment Manifest

### Required Artifact Manifest

| Path | Output stage | Purpose |
|---|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-foundation-readiness.py` | worker return | deterministic verifier for T9 foundation artifacts |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-foundation-readiness-report.json` | worker return | machine-readable T10 readiness report |
| `docs/reviews/CVF_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_WORKER_RETURN_2026-06-07.md` | worker return | worker packet for Codex review and possible closure |

### Forbidden Path Manifest

| Path | Reason |
|---|---|
| `EXTENSIONS/*` | no app/runtime integration authorized |
| `.github/*` | no CI or workflow change authorized |
| `governance/compat/*` | no checker change authorized |
| `scripts/*` | no repo root script change authorized |
| `CVF_SESSION/*` | reviewer owns session sync |
| `CVF_SESSION_MEMORY.md*` | reviewer owns front-door sync |
| `AGENT_HANDOFF*.md*` | reviewer owns handoff sync |
| `docs/roadmaps/*` | no roadmap mutation in worker scope |
| `package*.json` | no dependency or package change authorized |

### Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `EXTENSIONS/*` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Worker must not edit, stage, or claim |
| `.github/*` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Worker must not edit, stage, or claim |
| `governance/compat/*` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Worker must not edit, stage, or claim |
| `CVF_SESSION/*` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Reviewer-only session sync |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-foundation-readiness.py` | ABSENT | ABSENT | N/A |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-foundation-readiness-report.json` | ABSENT | ABSENT | N/A |

### Pre-Existing Dirty Path Exemptions

| Path | Status at dispatch | Exemption boundary |
|---|---|---|
| N/A | clean before dispatch | no dirty-path exemption granted |

### Required Proof Manifest

| Proof | Path | Required literal | Output stage |
|---|---|---|---|
| Readiness schema | `policylocal-foundation-readiness-report.json` | `policylocal.foundationReadiness.t10.v1` | worker return |
| Acceptance receipt assertions | `policylocal-foundation-readiness-report.json` | `receiptAssertions` | worker return |
| External artifact hashes | `policylocal-foundation-readiness-report.json` | `artifactHashes` | worker return |
| Freshness review boundary | `policylocal-foundation-readiness-report.json` | `2026-07-01` | worker return |
| Claim boundary | worker return packet | `no provider calls, no LLM, no vector retrieval, no current-law claim, no production readiness` | worker return |

## Write Ownership

Owned files or modules:

- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-foundation-readiness.py`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-foundation-readiness-report.json`
- `docs/reviews/CVF_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_WORKER_RETURN_2026-06-07.md`
- Optional GC-051 registry JSON/MD only if T10 records a new finding or next
  action state.

Forbidden paths:

- all paths in the Forbidden Path Manifest.

Write mode:

- create-only for the verifier, readiness report, and worker return packet;
- modify-listed only for optional GC-051 registry updates;
- no commit.

## Execution Plan

1. Pre-flight and drift check:
   - input: T9 completion, external T9 artifacts, this work order;
   - output: pre-flight evidence in worker return packet;
   - validation: hashes match T9 manifest;
   - stop condition: any T9 hash drift that cannot be explained inside
     Allowed scope.
2. Build `policylocal-foundation-readiness.py`:
   - input: existing corpus records, chunks, acceptance receipts;
   - output: deterministic verifier script;
   - validation: script reads existing JSON only and does not rerun acceptance
     unless explicitly passed a local dry-run flag that does not overwrite T9
     receipts.
3. Generate readiness report:
   - input: existing T9 artifacts;
   - output: `policylocal-foundation-readiness-report.json`;
   - validation: schema checks, count checks, hash checks, receipt assertion
     checks, boundary checks.
4. Create worker return packet:
   - input: verifier output, gate results, changed file list;
   - output: worker return packet under `docs/reviews/`;
   - validation: no closed-equivalent status, no completion-review claim.
5. Run gates:
   - input: uncommitted worker diff;
   - output: gate evidence in worker return packet;
   - validation: component gates pass or failures are repaired inside Allowed
     scope.

## Evidence Requirements

Claude must record:

- `git rev-parse --short HEAD`
- `git status --short`
- hashes for all five existing T9 artifacts;
- output of the T10 verifier command;
- JSON summary from `policylocal-foundation-readiness-report.json`;
- changed files from `git diff --name-status` and untracked files from
  `git status --short`;
- pre-dispatch/pre-implementation gate results if run after Codex dispatch
  commit;
- explicit statement that no provider calls, no LLM, no vector retrieval, no
  corpus expansion, no deployment, no public-sync, and no current-law claim
  occurred.

Suggested verifier command:

```powershell
python 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-foundation-readiness.py' --json
```

The verifier must not overwrite T9 acceptance receipts. It may write only the
T10 readiness report.

## Acceptance Criteria

Worker return is acceptable only if:

- T10 verifier script exists and is deterministic.
- T10 readiness report exists with schema
  `policylocal.foundationReadiness.t10.v1`.
- Report records all five T9 artifact hashes and they match the T9 completion
  hash manifest.
- Report confirms corpus records schema `policylocal.corpusRecords.t8.v1`,
  record count 2, chunk schema `policylocal.chunk.t8.v1`, chunk count 76,
  receipt schema `policylocal.queryReceipt.t8.v1`, and receipt count 5.
- Report contains assertion rows for AQ-01 through AQ-05, including AQ-05
  `escalateConditionTriggered=EC-02`, `freshnessDisclosureApplied=true`, and
  `selectedCandidateIds=[]`.
- Report preserves `freshnessReviewRequiredOnOrAfter=2026-07-01`.
- Worker return packet is not marked `CLOSED`, `CLOSED_PASS`, or equivalent.
- `git status --short` is reported accurately, including untracked files.
- No forbidden path was modified or staged.

Fail conditions:

- Any T9 external artifact hash drift is unrecorded or unexplained.
- Any required schema/count/assertion differs from T9 evidence.
- AQ-05 freshness assertion is missing or false.
- Verifier reruns T9 acceptance and overwrites the T9 receipt artifact.
- Worker claims legal advice quality, current-law status, provider behavior,
  vector retrieval, corpus expansion, deployment, hosted readiness, production
  readiness, public readiness, or public-sync.
- Worker commits despite `WORKER_MUST_NOT_COMMIT`.

## Review Gate

Implementation may proceed only after:

- this work order is committed or explicitly handed to Claude by the operator;
- `pre-dispatch` gate passes for the work-order dispatch range;
- `pre-implementation` gate passes for the work-order dispatch range.

Closure may proceed only after:

- Codex or operator-designated reviewer inspects the worker return packet;
- reviewer commits accepted worker artifacts;
- committed-range `pre-closure` gate passes;
- session front door, active state registry, and active handoff are updated by
  reviewer if next allowed move changes.

For this work order, Claude must not create a completion review. Claude creates
only the worker return packet; reviewer owns any closed completion artifact.

## Machine Closure Package

This work order defines the expected closure package for the reviewer:

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `DISPATCHED_TO_WORKER` before worker; reviewer may close later | N/A with reason: dispatch packet only |
| Worker return packet | `docs/reviews/CVF_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_WORKER_RETURN_2026-06-07.md` | worker evidence, changed files, claim boundary | BLOCKED until worker returns |
| Completion review | reviewer-created completion artifact or N/A with reason | final disposition and committed-range gates | BLOCKED until reviewer closure |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_ROADMAP_2026-06-07.md` | predecessor roadmap status `CLOSED_PASS_BOUNDED`; T10 is follow-on foundation readiness | PASS for dispatch |
| Corpus scan registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` or N/A with reason | T10 finding/next action if updated | BLOCKED until worker return |
| Corpus scan registry MD | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` or N/A with reason | operator lookup if updated | BLOCKED until worker return |
| External evidence digest | T10 readiness report and worker return packet | external path, schema, counts, hashes, generated time, privacy boundary | BLOCKED until worker return |
| System loop interlock | N/A with reason | local verifier/report only; no downstream runtime loop opened | N/A with reason |
| Session continuity | reviewer-owned session sync | mode/next move/handoff HEAD recorded by reviewer if the T10 worker packet is accepted | BLOCKED until reviewer-owned closure |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| T9 external artifacts live outside provenance git and need reproducible readiness verification before later PolicyLocal work | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | T10 verifier/report must hash-bind T9 artifacts and assert receipt values before corpus expansion or deployment |
| T9 AQ-05 assertion gap was fixed, but future PolicyLocal work needs a single report that rechecks required receipt assertions | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | T10 report format can become a future machine checker if repeated |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this work order references private PolicyLocal corpus artifacts and
local CVF-Workspace paths. No public-facing artifact, public-sync, public push,
or public readiness claim is authorized.

## Claim Boundary

This work order may claim only:

> T10 prepares a deterministic local foundation-readiness verifier and report
> for existing T9 PolicyLocal artifacts, so later PolicyLocal corpus expansion
> or deployment work can start from hash-bound schema and receipt evidence.

This work order does not claim:

- legal answer quality or accuracy;
- current-law status as of any date;
- legal advice, compliance, or interpretation guidance;
- provider behavior, LLM behavior, or chat runtime behavior;
- vector or semantic retrieval;
- corpus coverage beyond the existing two DOCX-derived records;
- hosted, production, public, release, or public-sync readiness;
- Learning Orchestrator runtime behavior, memory reinjection, high-risk
  promotion, or autonomous mutation.

## Closure Checklist

Reviewer closure is blocked until each item is resolved in the reviewer-owned
completion artifact:

| Item | Required close state |
|---|---|
| Worker return packet | PRESENT or BLOCKED with return reason |
| T10 verifier script | PRESENT and hash-recorded |
| T10 readiness report | PRESENT with schema `policylocal.foundationReadiness.t10.v1` |
| Artifact hash checks | PASS for all five T9 artifacts or BLOCKED with drift detail |
| Receipt assertion checks | PASS for AQ-01 through AQ-05, including AQ-05 freshness |
| Forbidden path scan | PASS: no forbidden path modified or staged |
| Claim boundary scan | PASS: no legal/current-law/provider/vector/deployment/public claim |
| Commit mode | PASS: Claude did not commit |
| Reviewer gate | PASS: committed-range pre-closure run by reviewer |
| Session sync | PASS or N/A with reason if next allowed move does not change |

## Return-To-Orchestrator Conditions

Claude must return to Codex without continuing if:

- any T9 external artifact hash differs from the T9 hash manifest and the drift
  cannot be explained as an allowed T10 report-only observation;
- the existing acceptance receipt artifact is missing, malformed, or overwritten;
- AQ-05 does not show `escalateConditionTriggered=EC-02`,
  `freshnessDisclosureApplied=true`, and `selectedCandidateIds=[]`;
- the verifier cannot satisfy the T10 readiness schema without changing T9
  runtime behavior;
- any needed repair would touch `EXTENSIONS/*`, `.github/*`,
  `governance/compat/*`, package files, public-sync, session files, handoff
  files, or deployment configuration;
- the task requires live/provider proof, secrets, quota, corpus expansion,
  current-law transition, vector retrieval, or chat runtime.

## Operator Checkpoint

No operator checkpoint is required for Claude to execute this R1 local
deterministic verifier/report work.

Operator approval is required before any of these moves:

- corpus expansion;
- EC-02 current-law transition on or after 2026-07-01;
- public-sync or public-facing artifact;
- provider/live/API-key proof;
- chat runtime, vector retrieval, or app/runtime integration;
- dependency/package change;
- production, hosted, release, legal-advice, current-law, or public-readiness
  claim.
