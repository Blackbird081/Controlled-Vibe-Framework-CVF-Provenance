# CVF Agent Work Order - Continuous Projection T3 Audience And Presentation Gate

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-CONTINUOUS-PROJECTION-T3

dispatchBaseHead: `c060fc7a5`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated worker

Reviewer/closer: Codex reviewer/closer

Worker return path: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T3_WORKER_RETURN_2026-07-20.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker for `CVF-CONTINUOUS-PROJECTION-T3`.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T3_AUDIENCE_PRESENTATION_GATE_2026-07-20.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture the current committed HEAD before any edit and
require it to match the operator/reviewer dispatch note.

Current-time notes: artifact date is 2026-07-20; execution is manual
copy/paste only because external-agent CLI/MCP/provider automation remains
parked.

Do-not-misread notes: T3 is a local read-only evidence validator. It does not
authorize a real-root scan, browser session, README/Web edit, public-sync,
provider call, MCP/CLI call, commit, push, or T4 work.

Required first actions: read `CVF_SESSION_MEMORY.md`, active state, active
handoff, guard orientation, literal gotchas, `DESIGN.md`, the paired baseline,
this packet, and every source/checker named below; then capture HEAD and actual
`git status --short` before editing.

Return contract: leave exactly the two new scripts and worker-return artifact
unstaged and uncommitted; run the focused proof and worker-return fast gate;
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement the frozen T3 audience and presentation evidence gate. The worker
must validate accepted T1/T2 evidence plus an explicit reviewer-owned seven-row
audience packet without inventing semantic heuristics or touching real
projection targets.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-CONTINUOUS-PROJECTION-T3 --title "Continuous Projection T3 Audience And Presentation Gate" --date 2026-07-20 --base c060fc7a5 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T2 completion review docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_COMPLETION_REVIEW_2026-07-20.md commit f350b925a REVIEWER_ACCEPTED_WITH_REPAIRS" --stdout` |
| generatedProfile | web-ui-dashboard plus `WORKER_MUST_NOT_COMMIT` no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced scaffold fields with source-verified scope, frozen T3 schemas, manifests, negative cases, and closure ownership. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py` |
| docOnlyNewFields | fields frozen in the paired baseline under New Doc-Only Fields |
| claimBoundary | Dispatch shape and bounded implementation instructions only; no runtime/provider/live/public mutation, Web edit, MCP/CLI adapter, or production claim. |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator | direct 2026-07-20 instruction to finish T3 and T4 | ACCEPT for T3 dispatch only |
| Roadmap | `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md`, T3 section | ACCEPT |
| T2 closure | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_COMPLETION_REVIEW_2026-07-20.md`, commit `f350b925a` | ACCEPT |
| Paired baseline | `docs/baselines/CVF_GC018_CONTINUOUS_PROJECTION_T3_AUDIENCE_PRESENTATION_GATE_2026-07-20.md` | ACCEPT |

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Operator | human operator | releases T3 scope and owns later T4 checkpoint |
| Dispatcher | dispatch author | packet source fidelity, dispatch gate, and manual handoff prompt |
| Worker | delegated no-commit worker | exactly three allowed outputs and focused proof |
| Reviewer/closer | independent reviewer/closer | semantic review, bounded repair, commit, and T4 dependency decision |

## Scope / Target / Owner Boundary

Worker owns only two new scripts and the worker-return packet. Reviewer owns
semantic evidence, acceptance, repairs, completion review, commits, session
sync, and T4 release. Existing files are read-only references.

## Scope

Required work:

- add `scripts/get_cvf_projection_audience_gate.ps1`;
- add `scripts/test_cvf_projection_audience_gate.ps1`;
- consume explicit receipt, review-draft, and audience-evidence JSON paths;
- implement the paired baseline contract exactly and fail closed;
- create only disposable fixtures in the test process;
- author the worker return after reading its applicable checkers.

Forbidden work:

- any edit to existing scripts, policy, README, cvf-web, public-sync, roadmap,
  baseline, work order, session, handoff, checker, or hook file;
- root discovery, recursive real-root scan, browser automation, screenshots,
  network access, provider/API use, Claude CLI, MCP, or external service;
- semantic keyword scoring, automatic quality decisions, or inferred evidence;
- output-file, apply, copy, approve, commit, push, deploy, or mutation mode;
- T4 implementation or a T4 receipt.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| T2 accepted implementation | completion review at `docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_COMPLETION_REVIEW_2026-07-20.md`, commit `f350b925a` | must be accepted before T3 dispatch | ACCEPT |
| UX evidence vocabulary | completion at `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md`, commit `d757fe5ac` | reuse bounded evidence; do not expand claim | ACCEPT |
| Clean dispatch boundary | dispatcher observed HEAD `c060fc7a5` and clean worktree before packet authoring | worker must start from committed dispatch/session-sync HEAD and a clean worktree | ACCEPT |

## Worker Autonomy / No-Question Rule

Repair allowed-scope test or literal defects directly. Return to the reviewer
only for a source contradiction, a need to modify a forbidden path, a dirty
worktree not caused by this batch, or a requirement that would add real-root,
browser, provider, network, or mutation authority.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`continuous projection T3 audience presentation gate`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "continuous projection T3 audience presentation gate" --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defect count: `0`. Disclosed defectIds: NONE. Dispatch impact: no
registry-specific additions beyond the canonical packet rules.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V49_2026-07-20.md`
4. `docs/reference/guard_orientation/README.md`
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
6. `DESIGN.md`
7. paired baseline and this work order
8. source files in the Source Verification Block
9. `governance/compat/check_worker_return_quality_gate.py`
10. `governance/compat/check_markdown_structural_completeness.py`

## Pre-Flight Checks

Before editing, record:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path scripts/get_cvf_projection_audience_gate.ps1
Test-Path scripts/test_cvf_projection_audience_gate.ps1
Test-Path docs/reviews/CVF_CONTINUOUS_PROJECTION_T3_WORKER_RETURN_2026-07-20.md
```

All three target paths must be absent and the worktree must be clean. If the
committed execution HEAD differs from the reviewer dispatch note, stop and
return `BLOCKED_WITH_REASON`.

## Source-Fidelity Pass

### Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T3 requires audience checks after freshness | VALUE_SET | `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md` | Work Plan, T3 | `T3 - Audience And Presentation Gate` | roadmap | ACCEPT |
| receipt carries rows, reconciliation, errors, and no-write evidence | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly | `rows`; `reconciliationMatch`; `errors`; `noTargetWriteConfirmation` | T1 receipt schema | ACCEPT |
| draft is review-required and non-authorizing | VALUE_SET | `scripts/get_cvf_projection_review_packet.ps1` | final draft assembly | `draftStatus`; `authorizesDecision`; `claimBoundary` | T2 draft schema | ACCEPT |
| draft contains source receipt identity | EXISTS | `scripts/get_cvf_projection_review_packet.ps1` | source facts assembly | `sourceFacts` | T2 draft schema | ACCEPT |
| automatic semantic approval is forbidden | VALUE_SET | `scripts/cvf_projection_policy.json` | `semanticReviewBoundary` | `autoApproveForbidden` | projection policy | ACCEPT |
| Web/UI work must read the root design contract | LITERAL_INVARIANT | `AGENTS.md` | UI / Web Design Contract | `DESIGN.md` | CVF agent instructions | ACCEPT |
| UX evidence is bounded to localhost current source | LITERAL_INVARIANT | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md` | Claim Boundary | `current-source localhost` | UX completion review | ACCEPT |

## New Doc-Only Fields

The audience evidence and gate output fields are new T3 contract fields listed
in the paired baseline. They must not be represented as pre-existing runtime
fields or inserted into existing T1/T2 source.

## Current Runtime Freshness Verification

No T3 runtime behavior exists at dispatch. T1 and T2 have fixture-proven local
scripts only. T4 owns the later reviewer-authorized real-root read-only run.

## Evidence Reuse And Encoding Plan

| Evidence | verificationMode | owner | Rule |
| --- | --- | --- | --- |
| T1/T2 schema literals | `RECOMPUTE_REQUIRED` | worker | read current source directly; do not copy from chat or provider memory |
| UX completion vocabulary | `REUSE_PRIOR_VERIFICATION` | worker | preserve its localhost/hosted claim boundary |
| Worker test counts | `RECOMPUTE_REQUIRED` | worker | report actual assertions from the final run |
| Closure evidence | `REVIEWER_RECOMPUTE_ONLY` | reviewer | worker must not claim closure or commit-range PASS |

ASCII is required for both scripts and the worker return. Do not normalize
unrelated files.

## Negative Search And Collision Discipline

The dispatcher confirmed all three worker output paths were absent before
authoring. The worker must repeat the `Test-Path` checks and search existing
source for the frozen new schema identifiers. Any existing collision stops the
batch; do not overwrite or rename around it.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order implementation | Proof | Disposition |
| --- | --- | --- | --- |
| progressive disclosure | ordered README and Web assessment rows | focused positive and negative fixtures | ACCEPT |
| language | README language-clarity assessment | required row and terminal-status tests | ACCEPT |
| navigation | cvf-web navigation-clarity assessment | required row and terminal-status tests | ACCEPT |
| external-agent context | evidence-route assessment | required row and locator validation | ACCEPT |
| source freshness plus presentation | T1 receipt and T2 draft validation before audience result | identity and fail-closed tests | ACCEPT |
| reuse UX evidence | evidence packet uses reviewer locators; no new visual doctrine | schema and claim boundary tests | ACCEPT |

## Frozen Interface And Schema

Implement the exact input, ordered seven-row assessment schema, terminal
status logic, output fields, and frozen claim boundary in the paired baseline.
Do not add optional fields or fallback aliases. JSON booleans must be validated
by type, not truthy string conversion. Enum matching is ordinal and
case-sensitive.

Malformed input must exit nonzero with one stable diagnostic code:
`UNSUPPORTED_OR_INVALID_AUDIENCE_EVIDENCE`. A valid FAIL or REVIEW_REQUIRED
assessment is not malformed; it emits a success object with the corresponding
terminal `gateStatus`.

## Pending Artifact Evidence Finality

The worker return must describe the actual three pending paths and actual
unstaged status. It must not say the worktree is clean, closure passed, or a
commit exists. The reviewer recomputes semantic and closure evidence.

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Artifact | Required worker action |
| --- | --- |
| `scripts/get_cvf_projection_audience_gate.ps1` | create the read-only validator and deterministic stdout JSON gate |
| `scripts/test_cvf_projection_audience_gate.ps1` | create disposable-fixture positive, negative, type, order, identity, and no-mutation proof |
| `docs/reviews/CVF_CONTINUOUS_PROJECTION_T3_WORKER_RETURN_2026-07-20.md` | create checker-safe no-commit return evidence |

## Forbidden Path Manifest

Every path not listed in the Required Artifact Manifest is forbidden. In
particular, existing `scripts/`, `README.md`, `DESIGN.md`, `EXTENSIONS/`,
`docs/roadmaps/`, `docs/baselines/`, `docs/work_orders/`, `CVF_SESSION/`,
`AGENT_HANDOFF_V49_2026-07-20.md`, and all public-sync content are read-only.

## Required Proof Manifest

Required Proof Manifest Atomic Literal Discipline: each row below is one
atomic assertion and must be reported independently.

| Proof | Required result |
| --- | --- |
| PowerShell parse | both scripts parse without error |
| deterministic positive fixture | repeated runs emit byte-equivalent JSON |
| seven-row positive fixture | `gateStatus=PASS`; row count 7; Boolean `authorizesMutation=false` |
| valid FAIL fixture | `gateStatus=FAIL` |
| valid review fixture | `gateStatus=REVIEW_REQUIRED` |
| identity mismatch | nonzero with stable diagnostic |
| malformed schemas | missing, extra, duplicate, reordered, renamed, wrong-case, wrong-type, and empty-evidence cases fail closed |
| no mutation surface | no root, output, apply, copy, commit, push, browser, provider, or network parameter/path |
| worker-return fast gate | PASS for the pending worker return and owned scripts |

## Write Ownership

Allowed paths are exactly the three Required Artifact Manifest paths. Worker
must not stage or commit. Reviewer may repair only those paths during review.

## Execution Plan

1. Read all required sources and checker files.
2. Capture `executionBaseHead` and clean status.
3. Implement the gate without reading real roots.
4. Implement the disposable-fixture proof suite before broad gate execution.
5. Run syntax and focused proof once; repair within allowed paths.
6. Author the worker return from actual final evidence.
7. Run worker-return fast gate once and return pending output.

Do not run the full 83-check pre-commit chain repeatedly. The reviewer owns the
full closure gate after semantic inspection.

## Design Control Carry-Forward

`DESIGN.md` is the visual authority, but T3 changes no UI. The gate validates
reviewer evidence locators and required audience dimensions; it does not turn
design guidance into autonomous semantic scoring.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | local PowerShell gate over explicit files | validation only; no semantic, commit, browser, provider, or public authority | frozen schema and fixture proof | internal local script only | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | no adapter in this tranche | no ingress, auth, raw-data release, mutation, or public authority | explicit moratorium and forbidden scope | separate future source-verified adapter work order required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | `NOT_APPLICABLE_WITH_REASON`: no external repository, critique, or provider output is absorbed |
| Matching local-view guard | N/A with reason: source verification and focused local proof remain authority |
| Owner surface | paired T3 baseline and this work order |
| Disposition | `NOT_APPLICABLE_WITH_REASON` |
| Claim boundary | worker output is implementation evidence, not external knowledge authority |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatch author; delegated worker after handoff |
| Provider or surface | local private provenance workspace; manual copy/paste handoff |
| Session or invocation | Continuous Projection T3 dispatch, 2026-07-20 |
| Working directory | repository root resolved by the worker |
| Command or tool surface | local shell and filesystem only |
| Target paths | exactly the three Required Artifact Manifest paths |
| Allowed scope source | operator instruction plus paired baseline/work order |
| Before status evidence | dispatcher HEAD `c060fc7a5`, clean worktree before packet authoring; worker must capture fresh committed HEAD and clean status |
| After status evidence | worker must report three unstaged pending paths |
| Diff evidence | `git diff --name-status`; `git status --short` including untracked files |
| Approval boundary | bounded T3 implementation only |
| Claim boundary | no T4, real-root, browser, provider, network, mutation, public-sync, commit, push, or production claim |
| Agent type | dispatcher; delegated no-commit implementation worker; independent reviewer/closer |
| Invocation ID | `continuous-projection-t3-manual-dispatch-2026-07-20` |
| Expected manifest | exactly the three Required Artifact Manifest paths |
| Actual changed set | worker must recompute at return |
| Manifest delta | worker must report MATCH or block |
| Deletion or rename disposition | N/A with reason: no deletion or rename is authorized |

## Epistemic Process Block

### Expected Result / Prediction

A schema-driven reviewer-evidence gate should prevent freshness-only PASS from
being misread as audience-quality PASS without inventing semantic automation.

### Evidence Comparison

T1 proves a receipt contract and T2 proves a review-draft contract, while the
roadmap and UX closure require a separate audience/presentation dimension.

### Contradiction Or Gap Disposition

The gate validates evidence completeness and terminal decisions; it does not
claim to observe or understand UX by itself.

### Claim Update

T3 may claim deterministic evidence gating after focused proof, not real-root
freshness, hosted presentation quality, or automated semantic review.

## Evidence Requirements

Report exact assertion totals and commands. Preserve stderr/stdout separation
for malformed cases. Record token/quota usage as `0 provider calls` because the
worker is forbidden to use any provider or external-agent CLI/MCP surface.

## Acceptance Criteria

- [ ] Exactly three allowed paths are pending and nothing is staged.
- [ ] Both scripts parse.
- [ ] The exact input/output contracts and seven ordered rows are implemented.
- [ ] Positive, FAIL, REVIEW_REQUIRED, identity, cardinality, order, enum,
  Boolean, empty-evidence, and no-mutation cases are proven.
- [ ] No existing source or real root was modified or scanned.
- [ ] Worker-return fast gate passes.
- [ ] Worker returns `COMPLETE_PENDING_REVIEW` without committing.

## Review Gate

Reviewer must inspect source before running tests, recompute the full
contract/schema/path/authority/test matrix, and repair allowed-scope defects in
one consolidated round where possible. T4 stays held until T3 is committed and
independently accepted.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | repository-local read-only T3 evidence-gate implementation over accepted T1/T2 contracts |
| scope classification | two new local scripts plus one no-commit worker return; disposable fixtures only |
| risk sensitivity | R1 bounded local validation; fail closed; no real-root, browser, network, mutation, or provider action |
| escalation condition | source contradiction, dirty start, forbidden-path need, or need for real-root/browser/network/mutation authority |
| selected role route | no-commit implementation worker -> independent reviewer/closer |
| mode | `MULTI_AGENT_MULTI_ROLE` |
| implementation owner | delegated worker through manual copy/paste |
| review owner | Codex reviewer |
| closure owner | Codex reviewer/closer |
| execution-lane authority | operator-owned; this packet authorizes local manual handoff only |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> no-commit implementation worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`c060fc7a5`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | dispatch packet paths; exactly three worker paths; reviewer-owned closure paths; protected continuity paths separately |
| traceScope(phase, actor) | each actor records only commands, changed set, and evidence from its own phase |
| commitOwner(phase) | worker=`WORKER_MUST_NOT_COMMIT`; reviewer/closer owns material commit; session-sync steward owns continuity commit |
| crossBatchIsolation | one clean worktree and one T3 batch; unrelated changes block worker start |
| nextMoveSurfaces | reviewer/session-sync steward updates roadmap, state fragments, generated state, memory front door, and active handoff when T3 is accepted |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T3_COMPLETION_REVIEW_2026-07-20.md` |
| reviewerOwnedClosurePaths | paired baseline; this work order; roadmap; completion review; accepted worker outputs; separate continuity surfaces as applicable |
| closureOwner | Codex reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T3_WORKER_RETURN_2026-07-20.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_cvf_projection_audience_gate.ps1`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker must include Purpose, Target / Source, Scope / Methodology, Findings
/ Position, Risk / Corrective Action, Claim Boundary, Checker Source Read-Ahead
Block, Agent Operation Trace Block, Delta Execution Claim Boundary Control
Block, Public Export Disposition, actual base/status/diff evidence, and
conditional N/A-with-reason sections required by the worker-return checker.

## Verification Commands

```powershell
$null = [System.Management.Automation.Language.Parser]::ParseFile((Resolve-Path 'scripts/get_cvf_projection_audience_gate.ps1'), [ref]$null, [ref]$null)
$null = [System.Management.Automation.Language.Parser]::ParseFile((Resolve-Path 'scripts/test_cvf_projection_audience_gate.ps1'), [ref]$null, [ref]$null)
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_cvf_projection_audience_gate.ps1
python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_cvf_projection_audience_gate.ps1
git status --short
git diff --name-status
```

If the fast-gate wrapper does not accept a PowerShell target, run the focused
PowerShell suite directly and run `run_worker_return_fast_gate.py` without
inventing an unsupported substitution; record the exact outcome.

## Closure Checklist

- [ ] Reviewer verifies actual changed set and no staged files.
- [ ] Reviewer reads both scripts before test execution.
- [ ] Reviewer recomputes focused proof and fast gate.
- [ ] Every finding is repaired, rejected with evidence, or blocks closure.
- [ ] Material commit remains reviewer-owned.
- [ ] T4 is released only from committed T3 completion evidence.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for a dirty starting tree, source contradiction,
existing-path collision, forbidden-path need, inability to implement exact
fail-closed behavior, need for real-root/browser/provider/network access, or a
required schema change beyond the paired baseline.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | dispatch envelope fields; `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; source columns; `ACCEPT`; handoff fields; worker-return profile; manifest and proof markers |
| gateRunPurpose | confirm packet completeness before manual worker handoff, not discover requirements during execution |
| claimBoundary | structural checks do not prove T3 implementation or semantic correctness |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local T3 evidence validation only |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | `CLAIM_REJECTED_NO_RECEIPT`: T3 implementation is pending and no execution-control receipt is claimed |
| actionEvidence | `CLAIM_REJECTED_NO_ACTION`: no action path; Boolean `authorizesMutation=false` |
| invocationBoundary | manual local script invocation over explicit fixture files |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, browser, provider, or agent coding control |
| claimLanguage | PASS validates contract-complete reviewer evidence; it does not independently decide semantic quality |
| forbiddenExpansion | no T4, real-root, provider, live, public, package, Web edit, MCP/CLI adapter, or model-router behavior |

## Operator Checkpoint

The operator authorized T3/T4 continuation. This packet consumes that authority
only for T3 implementation through manual copy/paste. T4 requires T3 closure.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch only. No public-sync artifact or mutation
is authorized.

## Claim Boundary

This work order authorizes exactly two new read-only PowerShell scripts and one
no-commit worker-return packet for T3. It does not authorize T4, real-root
scanning, semantic decisions, README/Web edits, public-sync, browser activity,
provider/API/Claude CLI/MCP use, commit, push, deployment, or production claims.
