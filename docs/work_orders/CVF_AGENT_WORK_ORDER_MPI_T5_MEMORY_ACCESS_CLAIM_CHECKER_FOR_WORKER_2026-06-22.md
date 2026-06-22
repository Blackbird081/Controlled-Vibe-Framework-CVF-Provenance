# CVF Agent Work Order - MPI-T5 Memory Access Claim Checker

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-22

docType: work_order

dispatchBaseHead: b761d1bd

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MPI_T5_MEMORY_ACCESS_CLAIM_CHECKER_FOR_WORKER_2026-06-22.md`

Current status: `DISPATCHED_TO_WORKER`. MPI-T4 dependency is released by
`docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_WORKER_RETURN_2026-06-22.md`
(`Status: ACCEPTED_BY_REVIEWER`) and material commit `28373d14`. Operator
selected MPI-T5 on 2026-06-22. This packet releases MPI-T5 only.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture with `git rev-parse --short HEAD` at worker start.

Current-time notes: MPI-T5 is a bounded governance-hardening checker/test/wiring
tranche dispatched on 2026-06-22 with MPI-T4 release evidenced by material
commit `28373d14`.

Do-not-misread notes: Do not edit routes, schemas, auth, existing helpers,
foundation files, registry sources or aggregates, durable stores, generated
state, session/handoff files, provider configuration, public-sync, adapters,
or any `governance/compat/*.py` file other than the two named protected paths
and only the two narrow wiring lines authorized below.

Required first actions: read this work order, paired GC-018, Required First
Reads, and current source symbols before editing; capture `executionBaseHead`
and initial `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only allowed
uncommitted artifacts and exact gate evidence, or `BLOCKED_WITH_REASON` when
the required action exceeds Allowed Scope.

Build one local static checker that flags Memory Plane overclaims in changed
governed Markdown, plus its focused tests, plus exactly two narrow wiring
lines registering it in the existing reviewer-fast hook chain and autorun
common command bundle. Do not build or edit a route, read provider memory,
execute anything, mutate any scanned file, or touch any other
`governance/compat/*.py` file.

Return `COMPLETE_PENDING_REVIEW` with only allowed uncommitted artifacts,
actual `executionBaseHead`, actual `git status --short`, focused test and
worker-return gate evidence. If blocked, return `BLOCKED_WITH_REASON`.

The worker return must include `WORKER_EXPERIENCE_RETRO` or the exact
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` assertion.

## Purpose

Implement the MPI-T5 governance-hardening checker named by the Phase 2
roadmap: a static, forward-only gate over changed governed Markdown that
rejects the five named classes of Memory Plane overclaim unless the changed
file also carries a valid source-verified citation for the claim. The checker
does not judge truth beyond citation presence; it does not execute, read
provider memory, or mutate any scanned file.

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Dispatch author | Claude | authors and gates GC-018/work order |
| Worker | assigned worker | edits only Allowed Scope and returns uncommitted |
| Reviewer/closer | Codex | validates, repairs reviewer-owned closure artifacts, commits accepted work |
| Operator | human operator | authorizes scope, risk, live/provider/public/adapter/generated expansion |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22: continue with MPI-T5 after MPI-T4 closure | ACCEPT |
| MPI-T5 GC-018 | `docs/baselines/CVF_GC018_MPI_T5_MEMORY_ACCESS_CLAIM_CHECKER_2026-06-22.md` | ACCEPT |
| Phase 2 roadmap | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | ACCEPT |
| Parent MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | ACCEPT |
| MPI-T4 worker return | `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_WORKER_RETURN_2026-06-22.md` | DEPENDENCY_RELEASE_AUTHORITY |
| MPI-T3 contract | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | SUMMARY_ONLY_CONTRACT_AUTHORITY |
| MPI-T2 contract | `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` | REGISTRY_PROJECTION_BOUNDARY_AUTHORITY |
| Sibling checker pattern | `governance/compat/check_index_classification.py` | STRUCTURAL_PATTERN_AUTHORITY |
| Hook-chain wiring point | `governance/compat/run_local_governance_hook_chain.py` | WIRING_TARGET_AUTHORITY |
| Autorun wiring point | `governance/compat/run_agent_autorun_workflow_gate.py` | WIRING_TARGET_AUTHORITY |

## Dependency Release Gate

| Dependency | Release evidence | Current status |
|---|---|---|
| MPI-T4 closure | worker return `Status: ACCEPTED_BY_REVIEWER`; material commit `28373d14`; session sync `9b620116` | RELEASED |
| Operator selection | explicit selection on 2026-06-22 | RELEASED |
| Fresh GC-018 | paired baseline in Authority Chain | RELEASED |
| Protected-path authorization | Core Guard Self-Protection Authorization block in paired GC-018 | RELEASED |
| Source refresh | current source rows below; targets confirmed absent | RELEASED |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher releases packet; worker creates checker/test/wiring/worker-return; reviewer/closer validates and commits |
| phase | DISPATCH_COMPLETE; EXECUTION; CLOSURE; SESSION_SYNC_IF_NEEDED |
| baseHeadFor(phase) | `dispatchBaseHead=b761d1bd`; worker captures `executionBaseHead`; reviewer records `closureBaseHead` |
| changedSetScope(phase) | worker changes only Allowed Scope; reviewer owns closure and continuity surfaces |
| traceScope(phase, actor) | worker trace covers four worker-owned artifacts; reviewer trace covers closure |
| commitOwner(phase) | worker commits nothing; reviewer/closer owns accepted material and later session-sync commits |
| crossBatchIsolation | do not mix MPI-T6, route/schema, existing helper, registry/durable write, provider/live, public-sync, or session work |
| Before status evidence | clean worktree at dispatch start (`git status --short` empty except this dispatch's two new files); committed base `b761d1bd`; MPI-T4 closure at `28373d14` |
| nextMoveSurfaces | reviewer updates when the MPI-T5 material completion review records an accepted closure commit |
| Closer designation | reviewer/closer is designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MPI_T5_MEMORY_ACCESS_CLAIM_CHECKER_COMPLETION_2026-06-22.md` (reviewer creates this file after accepting the worker return; it does not exist at dispatch time) |
| reviewerOwnedClosurePaths | this work order; paired GC-018; Phase 2 roadmap; worker return; completion review; continuity surfaces only if state changes |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Selected route | `MULTI_AGENT_MULTI_ROLE` |
| Intake summary | operator selected MPI-T5; MPI-T4 release evidence is the accepted worker return and material commit `28373d14` |
| Scope assessment | R2 bounded static checker plus focused tests plus two narrow wiring lines |
| Risk sensitivity | no route, filesystem mutation, registry write, durable write, provider/live, or public behavior; checker reads changed Markdown text only |
| Intake owner | dispatch author |
| Execution owner | worker |
| Review owner | reviewer/closer |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Escalation condition | `BLOCKED_WITH_REASON` for any necessary action outside Allowed Scope |
| Rationale | enforce the Memory Plane claim boundary going forward in changed governed Markdown without touching runtime behavior |

## Single-Agent Multi-Role Control Block

N/A with reason: this packet selects `MULTI_AGENT_MULTI_ROLE`; worker and
reviewer/closer are separate roles and commit ownership is explicit.

- Role separation ledger: dispatcher authors; worker implements and returns
  uncommitted; reviewer/closer independently owns acceptance and commit.
- Evidence basis: source reads, git diff, focused tests, and machine gates;
  provider memory or chat memory is not evidence.
- Self-review boundary: worker checks are not claimed as independent review.
- Escalation conditions: stop and route to reviewer/closer or operator under the
  Worker Autonomy rule when the required action exceeds Allowed Scope.
- Gate sequence: pre-dispatch; worker pre-implementation/assist and fast return;
  reviewer-fast; pre-closure; pre-push only if separately authorized.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator selection to CVF-owned work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this MPI-T5 work order |
| Disposition | ADAPT as bounded local checker implementation |
| Claim boundary | external/provider memory is not authority; current CVF source controls |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: MPI-T5 enforces the existing MPI-T2/T3/T4
boundary in changed governed Markdown and does not rescan or absorb a legacy
source family. MPI-T0 through T4 predecessor coverage remains unchanged.

## Required First Reads

| Required source | Reason |
|---|---|
| this work order and paired GC-018 | exact scope and source facts |
| `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | MPI-T5 candidate checker targets, exact section |
| `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | overall Memory Plane integration boundary |
| `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | summary-only external read boundary; `rawMemoryReleased`/`canReinject` invariants |
| `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` | registry-projection derived-view boundary |
| `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | INDEX-vs-canonical-source boundary |
| `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_WORKER_RETURN_2026-06-22.md` | current accepted Memory Plane helper boundary, accepted form |
| `governance/compat/check_index_classification.py` | sibling static checker CLI/structure pattern to mirror |
| `governance/compat/run_local_governance_hook_chain.py` lines 125-128 | exact reviewer-fast wiring tuple pattern and insertion point |
| `governance/compat/run_agent_autorun_workflow_gate.py` lines 238-243 | exact autorun wiring call pattern and insertion point |
| RSE-T1 and RSE-T2 addenda | finding and worker-return routing |

## Allowed Scope

The worker may create only:

- `governance/compat/check_memory_access_claim.py`
- `governance/compat/test_check_memory_access_claim.py`
- `docs/reviews/CVF_MPI_T5_MEMORY_ACCESS_CLAIM_CHECKER_WORKER_RETURN_2026-06-22.md`

The worker may edit only:

- `governance/compat/run_local_governance_hook_chain.py` - insert exactly one
  new `(label, command)` tuple adjacent to the existing `"index
  classification"` entry (around line 125-128); no reordering or edit of any
  other entry;
- `governance/compat/run_agent_autorun_workflow_gate.py` - insert exactly one
  new `_range_command(label, path, base, head)` call adjacent to the existing
  `"index classification"` call (around line 238-243); no reordering or edit
  of any other call.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| new checker and focused test above | worker | create |
| worker-return path above | worker | create |
| two named wiring files above | worker | edit, two narrow lines only |
| GC-018, this work order, roadmap, completion review, continuity files | reviewer/closer | no worker edit |
| every other path, incl. every other `governance/compat/*.py` file | out of worker scope | forbidden |

## Forbidden Scope

The worker must not edit existing route/helper/foundation source, registry
source or aggregate, generator, durable store, session state, active handoff,
root routers, public-sync, provider configuration, dependencies, `.github/**`,
or any `governance/compat/*.py` file other than the two named protected paths
and only the two narrow wiring lines authorized above.

The worker must not add automatic file loading, registry/durable writes,
route/schema/auth behavior, CLI/MCP adapters, provider/network calls, external
commands, vector/graph storage, queue/daemon/watcher, direct IDE/shell/git
interception, EDIT/COMMIT automation, readiness, or universal control claims.
The checker itself must not execute any scanned content, read provider
memory, or write to any file it scans.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| MPI-T5 is a governance-hardening checker, not a helper implementation | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | `## MPI-T5 Memory Access Claim Checker` | `MPI-T5` | MPI Phase 2 roadmap | VALUE_SET | ACCEPT |
| MPI-T5 candidate checker targets are the five named overclaim classes | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | `## MPI-T5 Memory Access Claim Checker`, candidate checker targets list | `MPI-T5` | MPI Phase 2 roadmap | VALUE_SET | ACCEPT |
| MPI-T5 requires its own GC-018, protected-path authorization, focused tests, hook/autorun wiring proof | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | `## MPI-T5 Memory Access Claim Checker`, final paragraph | `MPI-T5` | MPI Phase 2 roadmap | VALUE_SET | ACCEPT |
| MPI-T3 contract requires summary-only, false safety flags | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | Inherited Invariants | `rawMemoryReleased`; `canReinject` | MPI-T3 contract | LITERAL_INVARIANT | ACCEPT |
| MPI-T2 projection is caller-supplied, derived-view only | `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` | derived-view boundary section | `MPI-T2` | MPI-T2 contract | VALUE_SET | ACCEPT |
| MPI-T4 accepted helper performs no route wiring, write, or adapter behavior | `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_WORKER_RETURN_2026-06-22.md` | `## Claim Boundary` | `buildFederatedMemoryRead` | MPI-T4 worker return | VALUE_SET | ACCEPT |
| Existing reviewer-fast hook chain registers checkers as `(label, command-list)` tuples in one ordered list | `governance/compat/run_local_governance_hook_chain.py` | lines 125-128 | `"index classification"` checker tuple | reviewer-fast hook command registry | RUNTIME_BEHAVIOR | ACCEPT |
| Existing autorun common command bundle registers checkers via `_range_command(label, path, base, head)` | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 238-243 | `_range_command` | autorun common command bundle | RUNTIME_BEHAVIOR | ACCEPT |
| Existing static checker CLI contract: `--base`, `--head`, `--enforce` | `governance/compat/check_index_classification.py` | line 376 | `main` | forward-only INDEX structural checker | RUNTIME_BEHAVIOR | ACCEPT |
| Sibling checker has a paired focused-test module | `governance/compat/test_check_index_classification.py` | line 49 | `TestApplicableDetection` | checker test surface | EXISTS | ACCEPT |

## New Implementation Symbols

| Proposed symbol | Target | Status | Required semantic |
|---|---|---|---|
| `check_memory_access_claim.py` (module) | new checker | NEW_SOURCE_SYMBOL | static lexical/structural scan of changed governed Markdown only |
| main entry function (worker may name it `main`, mirroring the sibling checker's own entry-point name) | new checker | NEW_SOURCE_SYMBOL | accepts `--base`, `--head`, `--enforce`, optional `--json`; returns violations list; exits non-zero only under `--enforce` with violations |
| `test_check_memory_access_claim.py` (module) | new test | NEW_SOURCE_SYMBOL | true-positive, true-negative, and CLI-contract focused tests |

Do not place these rows in Source Verification as existing facts. Renaming is
allowed only when exact replacements are recorded in worker-return evidence,
provided the public CLI surface (`--base`, `--head`, `--enforce`, optional
`--json`) is preserved exactly so hook-chain and autorun wiring need no
special-casing.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: checker behavior and wiring line numbers must be verified by
worker against current source at execution time, since other agents may have
committed unrelated changes between dispatch and execution.

freshRecomputeRequired: YES

unicodePathHandling: literal repo-relative paths with UTF-8-safe readers

extractedTextAuthority: N/A with reason: source is read directly

Prior MPI-T4 closure evidence is reused only for dependency release. Checker
behavior must be recomputed against current source and focused tests.

## Negative Search And Collision Discipline

Search roots: `governance/compat`; `docs`.

Search command:
`rg -n -i "memory access claim|check_memory_access_claim|MemoryAccessClaim" governance/compat docs`

At dispatch, target checker/test paths do not exist and no source symbol
named `check_memory_access_claim` exists. Roadmap references are planning
authority, not implementation collisions.

## Current Runtime Freshness Verification

| Claim | Evidence | Disposition |
|---|---|---|
| Reviewer-fast hook chain registers checkers via ordered `(label, command)` tuples | current `run_local_governance_hook_chain.py` lines 125-128 | ACCEPT |
| Autorun common command bundle registers checkers via `_range_command` calls | current `run_agent_autorun_workflow_gate.py` lines 238-243 | ACCEPT |
| MPI-T2/T3/T4 boundaries remain the live source of truth for what claims are currently true | current contract/helper files cited in Source Verification Block | ACCEPT |
| Target files absent | dispatcher `Test-Path` results are `False` | ACCEPT |
| Route/provider/public behavior | N/A with reason: forbidden and not claimed | N/A_WITH_REASON |

## Helper Contract

The worker must implement a static checker module that, over changed files in
the given `--base`..`--head` range restricted to governed Markdown under
`docs/baselines/`, `docs/work_orders/`, `docs/reviews/`, and
`docs/reference/`:

1. flags claim language asserting external agents can read CVF memory through
   a live runtime/MCP/CLI route when the changed file does not also cite a
   route file, MCP tool file, or CLI adapter file as a verified source;
2. flags claim language asserting scan-registry projection is "auto-wired",
   "automatically loaded", or "wired into the route" without an explicit
   route-file citation in the same Source Verification Block;
3. flags claim language asserting KGR, graph memory, vector DB, or durable
   store is "production memory access" or "live memory access" without an
   explicit durable-store or vector-store source-file citation;
4. flags claim language asserting raw memory, raw `content` exposure, or
   reinjection (`canReinject=true`, "raw memory release", "reinjection is
   allowed") is permitted;
5. flags claim language asserting an INDEX artifact "replaces", "supersedes",
   or "is" canonical source authority, instead of being routed as INDEX input
   per the INDEX classification standard;
6. exits non-zero only under `--enforce` when any violation is found;
   supports a non-enforcing report mode that prints violations without a
   non-zero exit;
7. performs no filesystem write, no network call, no provider call, and no
   mutation of any scanned file;
8. emits a violation message naming the file, the matched claim pattern, and
   the missing required citation, mirroring `check_index_classification.py`'s
   existing violation-message style.

## Focused Test Requirements

Tests must prove:

- a true-positive case for at least one claim pattern per requirement 1-5
  above, each flagged as a violation;
- a true-negative case where the same claim language appears but the file
  also carries a valid source-verified citation for the claim (no false
  positive);
- a true-negative case for ordinary unrelated governed Markdown prose (no
  over-triggering on unrelated content, e.g. plain GC-018/work-order/review
  boilerplate with no Memory Plane claim language);
- a CLI-contract test proving `--base`/`--head`/`--enforce`/optional `--json`
  behave consistently with the sibling checker's own contract (non-zero exit
  only under `--enforce` with violations present; zero exit otherwise);
- no filesystem write, network call, or mutation of any scanned fixture
  occurs during the test run.

## Execution Plan

1. Capture `executionBaseHead` and `git status --short`.
2. Read all Required First Reads and refresh named symbols and exact line
   numbers in the two wiring targets, since other agents may have committed
   unrelated changes since dispatch.
3. Create checker and focused test only.
4. Insert exactly one wiring line into each of the two named protected files,
   following the existing adjacent entry's exact pattern.
5. Run focused pytest, the new checker against itself/sibling fixtures,
   automation assist, and worker-return fast gate.
6. Create the worker-return packet with exact evidence.
7. Return `COMPLETE_PENDING_REVIEW` uncommitted or `BLOCKED_WITH_REASON`.

## Pre-Flight Checks

Dispatcher/reviewer runs:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base b761d1bd --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base b761d1bd --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base b761d1bd --head HEAD --enforce
```

## Required Checks

Worker runs from repository root:

```powershell
git rev-parse --short HEAD
git status --short
python -m pytest governance/compat/test_check_memory_access_claim.py -q
python governance/compat/check_memory_access_claim.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_local_governance_hook_chain.py --mode reviewer-fast --base <executionBaseHead> --head HEAD
python governance/compat/run_agent_automation_assist.py --base <executionBaseHead> --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_memory_access_claim.py
```

If `reviewer-fast` does not accept the new checker cleanly because of an
unrelated checker already failing for reasons outside this tranche, record
the exact failing checker name and output verbatim and do not silently
suppress it; classify it as a `BLOCKED_WITH_REASON` candidate unless the
failure is clearly pre-existing and unrelated to MPI-T5's own changed files,
in which case record it as a noted pre-existing condition and continue.

## Evidence Requirements

Worker-return evidence must include actual base/status, exact changed
manifest, focused pytest output, the new checker's own self-test results
against true-positive/true-negative fixtures, automation-assist JSON result,
worker-return fast-gate result, exact diff of the two wiring lines, and
explicit no-mutation/no-execution/no-network/no-provider boundaries for the
checker itself.

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker, test, wiring-line, packet-shape, source-fidelity,
and gate failures and rerun gates without asking the operator. Classify these
as `SELF_HANDLE_WITHIN_SCOPE`.

Stop with `BLOCKED_WITH_REASON` only if repair requires a forbidden path,
claim/risk expansion, dependency release, route/schema/auth change, existing
helper/foundation edit, generated/session/handoff/public/provider/live/adapter/
durable work, secrets/quota, or destructive action, or if it requires editing
any `governance/compat/*.py` file other than the two named protected paths.
Route ordinary promotion candidates to reviewer/closer through the Worker
Return Jurisdiction Block.

## Mandatory Gate-Failure Remediation Protocol

Any failed gate caused by an Allowed Scope artifact is mandatory worker
remediation. A failing gate outside Allowed Scope is recorded verbatim and
returned as `BLOCKED_WITH_REASON`; it is not bypassed or hand-labeled PASS.

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Exact allowed artifacts | `git diff --name-status` contains only the three new worker-owned paths plus the two named wiring edits |
| Wiring is narrow | diff of each wiring file shows exactly one new line/entry; no other line changed |
| True positives | five focused tests, one per overclaim class, each flagged |
| True negatives | cited-claim and unrelated-prose tests produce no violation |
| CLI contract matches sibling checker | `--base`/`--head`/`--enforce`/optional `--json` behave consistently |
| No mutation/execution | checker performs no write, network, or provider call; test asserts this |
| Checks pass | focused pytest, checker self-run, reviewer-fast, automation-assist, worker-return gates |
| Commit boundary | worker changes remain uncommitted |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all criteria pass. Return
`BLOCKED_WITH_REASON` for missing/stale source, ambiguous claim-pattern
semantics, out-of-scope gate remediation, or any necessary forbidden action.

## Operator Checkpoint

Human authorization is required before any route/schema/auth change, existing
helper or foundation edit, registry/durable write, generated/session/handoff
edit by worker, provider/live proof, public-sync, adapter behavior, MPI-T6
work, edit to any `governance/compat/*.py` file beyond the two named
protected paths, risk/claim expansion, secrets/quota use, or destructive
action.

No human authorization is required for allowed-scope checker/test/wiring/
worker-return remediation or gate reruns.

## Review Gate

Reviewer rejects or repairs within reviewer-owned closure scope if changed
paths exceed Allowed Scope; either wiring file has more than the one
authorized new line/entry changed; any other `governance/compat/*.py` file is
touched; the checker produces false positives on ordinary governed Markdown
or false negatives on any of the five required claim classes; the checker
performs I/O, network, provider, or mutation behavior; tests/gates fail; or
worker-return evidence is incomplete.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order control | Disposition |
|---|---|---|
| Runtime/MCP/CLI read-access overclaim detection | Helper Contract requirement 1 plus matching focused test | ACCEPT |
| Registry auto-wiring overclaim detection | Helper Contract requirement 2 plus matching focused test | ACCEPT |
| KGR/graph/vector/durable-store production-access overclaim detection | Helper Contract requirement 3 plus matching focused test | ACCEPT |
| Raw memory/reinjection overclaim detection | Helper Contract requirement 4 plus matching focused test | ACCEPT |
| INDEX-replaces-canonical-authority overclaim detection | Helper Contract requirement 5 plus matching focused test | ACCEPT |
| Own GC-018 | paired MPI-T5 GC-018 baseline | ACCEPT |
| Protected-path authorization | Core Guard Self-Protection Authorization block in paired GC-018 | ACCEPT |
| Focused tests | Focused Test Requirements and Required Checks | ACCEPT |
| Hook/autorun wiring proof | Allowed Scope edit list plus Required Checks reviewer-fast invocation | ACCEPT |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation storage class | no storage; static checker plus narrow registry wiring |
| New durable storage | none |
| Generated aggregate impact | none |
| Source layout | one new checker module beside existing sibling checkers; one colocated test; two single-line wiring edits |
| Index/front-door updates | none during worker execution |
| Layout boundary | no existing checker edit beyond the two named narrow wiring lines; no route, store, registry source, or generator edit |

## Governed File Maintainability Plan

The two new target files must remain focused modules comparable in size to
the sibling checker pair (`check_index_classification.py` at 414 lines,
`test_check_index_classification.py` at 360 lines). The two wiring files are
not edited beyond one line/entry each and are not near-threshold targets for
this tranche. If a target would approach a governed hard threshold, return
`BLOCKED_WITH_REASON` instead of growing or splitting outside Allowed Scope.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T5 local static checker execution in focused tests |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: checker behavior must be proven by focused tests only |
| receiptEvidence | N/A with reason: no Delta receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT in worker focused tests; dispatch has N/A with reason while worker return is absent |
| claimLanguage | MPI-T5 local static checker dispatch only |
| forbiddenExpansion | route/schema/auth changes, automatic source loading, registry/durable writes, CLI/MCP adapter, provider/live, public-sync, wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |
| invocationBoundary | direct CLI invocation by reviewer-fast hook chain, autorun bundle, or a human operator running the script directly |
| interceptionBoundary | no IDE/shell/git/filesystem/provider/route interception beyond reading changed Markdown text for static analysis |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded source implementation.
- Corpus root: Required First Reads plus three new source/test targets plus
  two named wiring files.
- Snapshot time: 2026-06-22T00:00:00+07:00
- Enumeration command: `rg --files --hidden --no-ignore docs governance/compat`
- Manifest artifact or inline manifest: inline Source Verification Block above
  plus exact worker changed manifest.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is
  created.
- Processing ledger artifact or inline ledger: inline Source Verification Block.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=declared below; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: broad corpus scan, registry source/aggregate, route,
  durable store, provider/live, public-sync, adapter, MPI-T6, every other
  `governance/compat/*.py` file.
- Unreadable or unsupported files: 0.
- Aggregation check: NOT_APPLICABLE_WITH_REASON - no aggregate changed.
- Drift check: NOT_APPLICABLE_WITH_REASON - no generated aggregate changed.
- Output traceability: Allowed Scope, Source Verification Block, and focused
  tests.
- Adversarial verification: reviewer/closer must run reviewer-fast or stricter
  gate before acceptance.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Worker Return Packet Shape Contract

The worker-return must contain:

| Required item | Required value |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| executionBaseHead | actual start HEAD |
| git status --short | actual post-edit output |
| Purpose | purpose section |
| Scope / Methodology | exact execution method |
| Findings / Position | result and disposition |
| Risk / Corrective Action | residual risk and remediation |
| Changed Files | exact manifest, incl. exact diff line count for each wiring file |
| Gate Evidence | exact required check results |
| Worker Return Jurisdiction Block | present for findings, or exact RSE N/A line |
| Claim Boundary | no forbidden expansion |
| Agent Operation Trace Block | worker trace |
| Delta Execution Claim Boundary Control Block | local checker-only boundaries |
| Public Export Disposition | `DEFERRED_PRIVATE_ONLY` |
| WORKER_EXPERIENCE_RETRO | structured block or exact N/A assertion |

| Conditional gate term | Required disposition |
|---|---|
| External Knowledge Intake Routing | section or `N/A with reason` |
| Rescan Intelligence Hardening | section or `N/A with reason` |
| Corpus Completeness And Report Integrity | section or `N/A with reason` |
| Finding-To-Governance Learning Disposition | section or `N/A with reason` |
| Epistemic Process Block | section or `N/A with reason` |
| Machine Closure Package | section or `N/A with reason` |

## Open Artifact Evidence Finality

Worker evidence remains open while the uncommitted return is unreviewed. The
worker must not describe absent completion review, closure commit, or session
sync as complete. Reviewer/closer supplies committed closure evidence.

## Work-Order Fulfillment Manifest

The worker fulfills the proof manifest only with the exact three new Allowed
Scope paths, the two narrow wiring-line edits, actual command outputs, and
actual git evidence. No inferred or chat-memory evidence substitutes for a
source file or command result.

## Required Artifact Manifest

| Required artifact | Required path | Final evidence | Status |
|---|---|---|---|
| Memory access claim checker | `governance/compat/check_memory_access_claim.py` | created; focused pytest PASS | OPEN |
| Focused test | `governance/compat/test_check_memory_access_claim.py` | created; focused pytest PASS | OPEN |
| Hook-chain wiring | `governance/compat/run_local_governance_hook_chain.py` | one new tuple entry only | OPEN |
| Autorun wiring | `governance/compat/run_agent_autorun_workflow_gate.py` | one new `_range_command` call only | OPEN |
| Worker return | `docs/reviews/CVF_MPI_T5_MEMORY_ACCESS_CLAIM_CHECKER_WORKER_RETURN_2026-06-22.md` | `Status: COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` | OPEN |

## Self-Reported Gate Evidence Consistency

Any claimed PASS must match the recorded command exit/result. A skipped or
unavailable check is `N/A with reason` only when this packet allows it;
otherwise return `BLOCKED_WITH_REASON`.

## Dispatch Packet Learning Disposition

The prior reviewer finding that evidence packets can pass syntax while
lacking source fidelity is absorbed here: all existing source facts cite
current files and bare symbols; proposed checker symbols are separated from
Source Verification. Repeated drift must be routed as a governance-learning
finding.

## ACCEPT_AS_OWNER_MAP coverage

N/A with reason: this is not a corpus owner-map or connector-spec intake. The
Authority Chain explicitly names every current owner surface consumed.

## Closure Checklist

Reviewer/closer must resolve: exact deliverables; exact scope diff incl. the
two narrow wiring-line edits; focused tests/gates; true-positive/true-negative
proof for all five overclaim classes; no I/O/write/route/adapter/provider/
public scope in the checker; worker-return shape; commit ownership; closure
diff gate; and continuity sync if current mode changes. Each item must be
PASS, `N/A with reason`, or BLOCKED.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: DISPATCHED_TO_WORKER` | PASS |
| Completion or reviewer artifact | a completion review the reviewer creates after accepting this return | N/A with reason: not yet created | N/A with reason |
| Roadmap state | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | MPI-T5 row remains `PARKED_AFTER_T3_T4_DECISION`; reviewer updates this row only when accepting the material closure commit | N/A with reason: worker return not yet accepted |
| Registry JSON | N/A | no registry JSON changes authorized; verify unchanged with `git diff --name-status` before closure | N/A with reason |
| Registry Markdown | N/A | no registry Markdown changes authorized; verify unchanged with `git diff --name-status` before closure | N/A with reason |
| External evidence digest | this work order and paired GC-018 | External Knowledge Intake Routing present | PASS |
| System loop interlock | this work order | no system loop, wrapper, proxy, queue, daemon, watcher, or universal-control expansion | PASS |
| GC-018 | paired baseline | `Status: DISPATCHED_TO_WORKER` | PASS |
| Worker return | a target inside the reviews directory the worker creates | not yet created at dispatch time | N/A with reason: worker has not executed yet |
| Runtime checker/tests | three new worker source paths | not yet created at dispatch time | N/A with reason: worker has not executed yet |
| Session continuity | reviewer-owned later phase | dedicated session-sync follows material closure | N/A with reason: closure not yet reached |

## Acceptance Receipt Assertion Matrix

| Receipt/query item | Required value | Observed value | Status |
|---|---|---|---|
| Receipt behavior | no receipt/query acceptance behavior in MPI-T5 dispatch | no receipt/query behavior is authorized or claimed | N/A with reason: checker dispatch has no receipt/query surface |
| Query handling | checker reads changed Markdown text only via `--base`/`--head` range | no query parameter beyond the range arguments | PASS |
| Closure acceptance | reviewer-owned worker-return acceptance | worker must return `COMPLETE_PENDING_REVIEW`; reviewer supplies completion review | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance MPI-T5 dispatch; no public repository artifact or
claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | MPI-T5 work-order authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup/source reads, drafting, dispatch gates |
| Target paths | paired GC-018, this work order |
| Allowed scope source | operator instruction selecting MPI-T5 |
| Before status evidence | clean worktree (`git status --short` empty except this dispatch's two new files); committed HEAD `b761d1bd` |
| After status evidence | dispatch artifacts only; worker implementation absent |
| Diff evidence | pre-dispatch and steward gates before commit |
| Approval boundary | dispatch only; no worker commit |
| Claim boundary | local checker packet only |
| Agent type | dispatcher |
| Invocation ID | `mpi-t5-memory-access-claim-checker-dispatch-2026-06-22` |
| Expected manifest | GC-018, work order |
| Actual changed set | verified before dispatch commit |
| Manifest delta | MATCH required |
| Deletion or rename disposition | N/A with reason: none planned |

## Claim Boundary

This work order authorizes only one new local static checker, one focused
test file, two narrow single-line wiring edits in two named existing checker
registries, and one uncommitted worker return. It does not authorize any
route, schema, auth, existing helper/foundation edit, automatic source
loading, registry/durable write, generator, CLI/MCP adapter, external
command, vector/graph store, provider/live proof, public sync, session edit
by worker, readiness, universal governance-control claim, or any edit to any
`governance/compat/*.py` file beyond the two named protected paths and the
two narrow wiring lines.
