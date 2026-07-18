# CVF Web Inheritance T3P1 Worker Return - MAO Durable Run Discovery Prerequisite

Memory class: governed-worker-return

Self-declared worker-return artifact: yes

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_INHERITANCE_T3P1_MAO_DURABLE_RUN_DISCOVERY_PREREQUISITE_2026-07-18.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_INHERITANCE_T3P1_MAO_DURABLE_RUN_DISCOVERY_PREREQUISITE_2026-07-18.md`

Status: ACCEPTED_BY_REVIEWER_WITH_REPAIRS

Batch ID: CVF-WEB-INHERITANCE-T3P1

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: `233940c5b` (dispatcher-provided post-dispatch session HEAD;
verified via `git rev-parse --short HEAD` before editing and unchanged after
editing).

## Target / Source

Target artifacts:
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` (new
`listRunIds` method and `MaoDurableRunListSuccess` type),
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` (type export),
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts`
(focused discovery tests), and
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts`
(package-root discoverability test).

Source of truth: `snapshotFileNameFor`, `loadAndReplay`,
`MaoDurableRunStoreFailureReason`, and `atomicWriteJson`'s `.tmp-` suffix
convention, all in `durable.run.store.ts` at this execution head, per the
work order's Source Verification Block.

## Purpose

Implement a deterministic, read-only, fail-closed discovery seam over the
existing `MaoFileRunStore` root so a later prerequisite can enumerate valid
run identities without guessing them or weakening replay validation.

## Scope / Methodology

Read the required startup surfaces, guard orientation, literal-format
gotchas checklist, the T3P1 work order, the paired baseline, the roadmap's
T3P1 row, the accepted T3A review, and every file in the work order's Source
Verification Block before editing. Confirmed the execution HEAD and a clean
worktree, ran the pre-implementation autorun gate, and ran the existing
24-test baseline suite before any edit.

Implementation sequence:

1. Added `MaoDurableRunListSuccess` (`{ ok: true; taskGraphIds: readonly
   string[] }`) next to the existing `MaoDurableRun*Success` types.
2. Added a `CANONICAL_SNAPSHOT_FILENAME_RE` constant
   (`/^[0-9a-f]{64}\.json$/`) matching exactly `snapshotFileNameFor`'s output
   shape.
3. Added `MaoFileRunStore.listRunIds()`: on `ENOENT` from `readdir` on the
   root, return `{ ok: true, taskGraphIds: [] }` without any `mkdir` or
   write; otherwise list entries, keep only names matching the canonical
   regex, `stat` each and keep only regular files (excluding directories),
   parse each candidate only far enough to read `graph.taskGraphId` via the
   existing `isPersistedGraphShape` guard, require the filename to exactly
   equal `snapshotFileNameFor(candidateTaskGraphId)` (hash binding), then
   call the existing private `loadAndReplay(candidateTaskGraphId)` for full
   schema/authority/sequence/replay validation and propagate its failure
   without a partial result. Returns unique task-graph IDs via `Set`,
   sorted with `Array.prototype.sort()` (ordinary JavaScript lexicographic
   order).
4. Exported `MaoDurableRunListSuccess` from `mao/index.ts`'s existing
   durable-run-store export block; no other export in that file was
   touched.
5. Added seven focused `listRunIds` test cases to
   `mao.durable.run.store.test.ts`: missing root (empty success, root not
   created), deterministic sorted-unique ordering across two runs, ignored
   non-canonical entries (a `.txt` file, a `.tmp-` file, and a
   subdirectory), fail-closed on invalid JSON in a canonical-looking file,
   fail-closed on a canonical filename that does not hash-bind to its
   embedded `taskGraphId`, fail-closed on a canonical candidate that fails
   full replay validation (tampered `eventId`), and repeated-call purity
   (deep equality plus unchanged directory entries/bytes/mtime).
6. Added one package-root discoverability test to
   `mao.package.root.exports.test.ts` proving `MaoFileRunStore` and its
   `listRunIds` result shape are importable and usable through
   `../src/index`, not only the local `src/mao/` barrel.
7. Ran focused tests, the full package test suite, `npm run check`, the
   governed file-size guard, and the worker-return fast gate after the
   final edit.

## Findings / Position

- **Missing root never creates it.** `readdir` on a nonexistent root throws
  `ENOENT`; `listRunIds` catches exactly that code and returns a successful
  empty list without calling `mkdir` or any write function. The focused test
  asserts `stat` on the missing root still rejects after the call.
- **Canonical candidate filtering excludes exactly what the work order
  requires.** The regex `^[0-9a-f]{64}\.json$` matches only
  `snapshotFileNameFor`'s output shape; it does not match the atomic
  writer's own `<hash>.json.tmp-<suffix>` temporary files (the `.tmp-`
  suffix comes after `.json`, so the regex's end anchor already excludes
  them), a plain `.txt` file, or a directory name. An explicit `stat` check
  additionally excludes any directory that happens to be named with 64 hex
  characters plus `.json`.
- **No second validation implementation was added.** Every canonical
  candidate that passes filename/hash-binding still goes through the
  existing private `loadAndReplay`, which alone owns
  schema/authority/sequence/replay validation; `listRunIds` only performs
  the additional filename-to-embedded-ID binding check that `loadAndReplay`
  itself does not need (it already receives the ID as a parameter for
  `resumeRun`/`appendEvent`).
- **Fail-closed, not fail-open, on any canonical anomaly.** An invalid-JSON
  canonical file, a hash-binding mismatch, or a replay-validation failure on
  any single candidate causes the whole `listRunIds` call to return that
  typed failure; there is no partial-results field, warning list, or
  skip-and-continue behavior, matching the work order's explicit
  prohibition on silently omitting a canonical invalid snapshot.
- **Purity is proven, not assumed.** The repeated-call test captures
  directory entries, file bytes, and file `mtimeMs` before and after two
  `listRunIds` calls and asserts all three are unchanged, plus asserts the
  two call results are deeply equal.
- **Ordering is unique and deterministic.** IDs are collected in a `Set`
  before sorting, so a corrupted store that somehow produced two canonical
  files embedding the same `taskGraphId` (which cannot happen through this
  class's own `createRun`/`appendEvent`, since both derive the filename from
  the ID) would still report that ID once; the sort uses the default
  `Array.prototype.sort()` string comparison the work order specifies.

## Risk / Corrective Action

Reviewer correction: the worker implementation initially used `stat()` to
classify canonical-looking entries. Because `stat()` follows symbolic links,
a canonical-named link could have escaped the caller-supplied root and been
read as a snapshot candidate. The reviewer replaced that classification with
`readdir(..., { withFileTypes: true })` plus `Dirent.isFile()`, which does not
follow symbolic links, and expanded the ignored-entry regression case to
cover a canonical directory and a file symlink where the platform permits
creation. This repair remains within the worker-owned source/test paths.

No other corrective action was required against the work order's scope: the
existing `MaoDurableRunStoreFailureReason` union already covered every
failure this method needed (`IO_FAILURE`, `INVALID_SNAPSHOT_JSON`,
`GRAPH_ID_MISMATCH`, and whatever `loadAndReplay` itself returns), so no new
failure reason, source contradiction, or execution-head mismatch arose.
Risk is bounded to a read-only discovery method: `createRun`, `appendEvent`,
and every existing method's behavior are unchanged and their 24 pre-existing
tests still pass unmodified; no cvf-web, evidence-ledger, heartbeat,
configuration, or session path was touched.

## Changed Files

```
M  EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts
M  EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts
M  EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts
M  EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts
```

`docs/reviews/CVF_WEB_INHERITANCE_T3P1_WORKER_RETURN_2026-07-18.md` is this
new, unstaged, uncommitted worker-return file, the fifth allowed path.

## git status --short --untracked-files=all

```
 M EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts
 M EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts
 M EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts
 M EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts
?? docs/reviews/CVF_WEB_INHERITANCE_T3P1_WORKER_RETURN_2026-07-18.md
```

## Command Evidence

```
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 233940c5b --head HEAD
=> COMPLIANT: pre-implementation autorun gate passed. PASS (run before and after edits)

cd EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION
npx vitest run tests/mao.durable.run.store.test.ts tests/mao.package.root.exports.test.ts --config vitest.config.ts
=> baseline (before edit): Test Files 2 passed (2); Tests 24 passed (24).
=> final (after edit): Test Files 2 passed (2); Tests 32 passed (32). PASS

npm test
=> Test Files 70 passed (70); Tests 1790 passed (1790). PASS

npm run check
=> tsc -p tsconfig.json --noEmit completed with no output. PASS

cd ../../..
python governance/compat/check_governed_file_size.py --enforce
=> COMPLIANT - Governed file size is within the active policy. PASS

git diff --name-status
=> M  EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts
=> M  EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts
=> M  EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts
=> M  EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts

git diff --cached --name-status
=> (empty) PASS

git status --short --untracked-files=all
=> four modified paths plus this untracked worker-return file. PASS

git rev-parse --short HEAD
=> 233940c5b (unchanged from executionBaseHead). PASS
```

```
python governance/compat/run_worker_return_fast_gate.py
=> COMPLIANT: worker-return fast gate passed. PASS
```

The worker-return fast gate's bundled sub-checks (corpus scan registry
aggregate drift, epistemic process packet, worker-return quality gate,
reviewer-fast governance gate 62/62, whitespace diff check) all reported PASS
against this artifact's final content before submission.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_experience_retrospective.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| literalTokensReviewed | checker read-ahead section field names (`applicableCheckersRead`, `literalTokensReviewed`, `gateRunPurpose`, `claimBoundary`); trace-block required label set (`Actor`, `Provider or surface`, `Session or invocation`, `Working directory`, `Command or tool surface`, `Target paths`, `Allowed scope source`, `Before status evidence`, `After status evidence`, `Diff evidence`, `Approval boundary`, `Claim boundary`, `Agent type`, `Invocation ID`, `Expected manifest`, `Actual changed set`, `Manifest delta`); target/source heading group; corpus completeness `Corpus verdict` bullet-line shape; guard's own applicability word set for its rescan/non-rescan vocabulary |
| gateRunPurpose | evidence confirmation run after direct checker-source read |
| claimBoundary | structural conformance does not replace implementation review |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated implementation worker |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-WEB-INHERITANCE-T3P1 no-commit worker execution, 2026-07-18 |
| Working directory | repository root, with execution-plane sub-shell for `npx vitest`, `npm test`, and `npm run check` |
| Command or tool surface | Read, Edit, Bash, governance gate scripts |
| Target paths | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts`; `docs/reviews/CVF_WEB_INHERITANCE_T3P1_WORKER_RETURN_2026-07-18.md` |
| Allowed scope source | dispatched work order `CVF_AGENT_WORK_ORDER_CVF_WEB_INHERITANCE_T3P1_MAO_DURABLE_RUN_DISCOVERY_PREREQUISITE_2026-07-18.md` |
| Before status evidence | clean worktree at `233940c5b`; `MaoFileRunStore` had no discovery method; baseline focused suite was 24/24 |
| After status evidence | `MaoFileRunStore.listRunIds` and `MaoDurableRunListSuccess` exist and are package-root exported; focused suite is 32/32; full package suite is 1790/1790; typecheck clean |
| Diff evidence | `git diff --name-status` shows exactly the four allowed source/test paths modified |
| Approval boundary | T3P1 read-only run-discovery prerequisite dispatch only |
| Claim boundary | no cvf-web, evidence-ledger, heartbeat, configuration, provider/live, public, push, or production mutation |
| Agent type | delegated implementation worker |
| Invocation ID | `cvf-web-inheritance-t3p1-worker-2026-07-18` |
| Expected manifest | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts`; `docs/reviews/CVF_WEB_INHERITANCE_T3P1_WORKER_RETURN_2026-07-18.md` |
| Actual changed set | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts`; `docs/reviews/CVF_WEB_INHERITANCE_T3P1_WORKER_RETURN_2026-07-18.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred in this tranche |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | read-only durable run-discovery contract and focused tests |
| claimDisposition | N/A with reason: dispatch/implementation adds no execution-control or enforcement behavior beyond typed enumeration |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - discovery creates no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION - no action surface is released |
| invocationBoundary | exact five-path T3P1 worker packet |
| interceptionBoundary | no IDE, shell, provider, filesystem-action, or agent-action interception claim |
| claimLanguage | enumerate, validate, sort, and return run identities without mutation |
| forbiddenExpansion | Web, evidence/heartbeat persistence, run/event mutation, worker launch, provider/live, public, push, production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance T3P1 no-commit worker execution; no public-sync action.

## External Knowledge Intake Routing

Chain map reference: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Value |
|---|---|
| Chain map | N/A with reason: no external chain-map source is consumed in this tranche |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external route applies |
| Matching local-view guard | N/A with reason: no local-view guard match applies |
| Owner surface | existing `durable.run.store.ts` `MaoFileRunStore` owner |
| Disposition | N/A with reason: no external item is being routed in this tranche |
| Claim boundary | this section records applicability only; no external source was absorbed |

## Rescan Intelligence Hardening

NOT_APPLICABLE_WITH_REASON: this tranche is a bounded four-path source/test
implementation against directly cited existing source, not a corpus
re-examination or intake-refresh activity, so the hardening fields below do
not apply.

- Original source artifact: N/A with reason: not applicable to this tranche.
- Predecessor intake artifact: N/A with reason: not applicable to this tranche.
- Delta ledger status: N/A with reason: not applicable to this tranche.
- Routing matrix status: N/A with reason: not applicable to this tranche.
- Semantic sampling status: N/A with reason: not applicable to this tranche.
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

## Corpus Completeness And Report Integrity

NOT_APPLICABLE_WITH_REASON: this tranche verifies a small named set of
existing source files directly (the durable run store, its package-root
barrel, and its two existing test files), not a folder-, subtree-, or
archive-scale corpus enumeration, so no manifest/ledger/reconciliation block
is required.

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - a small named set of source
  files was verified directly, not a folder- or archive-scale corpus.

## Finding-To-Governance Learning Disposition

N/A_WITH_REASON: no repeated or non-obvious defect pattern was discovered
during this tranche; the implementation matched the work order's Required
Discovery Contract on the first pass with zero test failures and zero
typecheck errors. The ADIF resolver query for `taskClass=backend,
role=worker, lifecyclePhase=pre-implementation` returned zero defects.

## Epistemic Process Block

Expected Result / Prediction: canonical snapshots can be discovered safely
by filtering to the exact `snapshotFileNameFor` filename shape, binding the
recomputed hash of each candidate's embedded `graph.taskGraphId` back to its
filename, and reusing the existing `loadAndReplay` for full validation,
without adding a second validation implementation or any write path.

Evidence Comparison: all seven new discovery test cases (missing root,
valid deterministic ordering, ignored non-canonical entries, invalid-JSON
fail-closed, hash-binding-mismatch fail-closed, replay-failure fail-closed,
and repeated-call purity) passed on the first implementation pass, plus the
new package-root discoverability test; the full 1790-test package suite and
`tsc --noEmit` also passed with zero failures, directly confirming the
prediction against real filesystem behavior rather than assumption.

Contradiction Handling: no contradictory source or test evidence was found;
no `BLOCKED_WITH_REASON` condition was triggered.

Claim Update: Claim confirmed. The read-only discovery contract is
implemented exactly as specified: missing root returns empty without
creating it, every canonical candidate receives full replay validation with
no partial results, ordering is unique/sorted/deterministic, and repeated
calls are proven pure against real filesystem entries and bytes.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
frictionLevel: LOW
frictionType: GATE_SURPRISE
observedStep: the first pre-implementation run after adding this worker
  return failed the agent operation trace integrity gate because the
  `Actual changed set` cell said "same five paths listed in Expected
  manifest" (prose) instead of literal repo-local paths; rewriting the cell
  with the five real paths resolved it on the next run with no further
  repair needed.
preventiveControlCandidate: NONE

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`backend`, role=`worker`, lifecyclePhase=`pre-implementation`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class backend --role worker --lifecycle-phase pre-implementation --surface-selector execution-plane --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. This worker made no `git add`, `git commit`,
`git stash`, or session-state edit of any kind. Exactly the four allowed
source/test paths were modified and left unstaged; this worker-return file
is left untracked and uncommitted. `git status --short --untracked-files=all`
and `git diff --cached --name-status` evidence above confirm zero staged
changes and an unchanged HEAD at `233940c5b`.

## Claim Boundary

This worker return covers exactly the five allowed no-commit paths named in
the CVF-WEB-INHERITANCE-T3P1 work order. It does not authorize any cvf-web,
evidence/heartbeat persistence, configuration, session, provider/live,
public, push, release, or production mutation. Independent reviewer/closer
recomputation of purity, race-safe fail-closed behavior, canonical filename
binding, reuse of replay validation, and test coverage, plus any material
commit and closure claim, remain pending and out of scope for this return.
