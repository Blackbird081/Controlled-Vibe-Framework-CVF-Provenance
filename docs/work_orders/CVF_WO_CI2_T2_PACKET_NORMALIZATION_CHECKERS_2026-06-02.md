# CVF Work Order - CI2-T2 Packet Normalization Checkers

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-02

dispatchBaseHead: `65a0620f`

executionBaseHead: 7a0e911f

closureBaseHead: 7a0e911f

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Implement structural machine checks for the three CI1-T6 checker stubs:
NR-04 per-file source hash, NR-05 normalized path, and NR-11 canonical
disposition alias.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| CI2 GC-018 | `docs/baselines/CVF_GC018_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_2026-06-02.md` | ACCEPT |
| CI2 roadmap | `docs/roadmaps/CVF_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_ROADMAP_2026-06-02.md` | ACCEPT |
| CI1-T6 checker stubs | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | ACCEPT |
| CI2-T1 source hash standard | `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` after T1 closure | REQUIRED |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch only after T1 closure | no runtime/product work |
| Worker | implement checker scripts/tests and bounded hook wiring | no unrelated guard rewrites |
| Reviewer | verify tests, hook scope, self-protection | reject scope bleed |

## Dependency Gate

CI2-T2 must not begin until CI2-T1 is closed and
`docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` exists.

## Roadmap-To-Work-Order Trace Matrix

| CI2 roadmap requirement | CI2-T2 instruction |
| --- | --- |
| Turn standards into structural enforcement | implement checker scripts and tests |
| Protect core guards from uncontrolled edits | this work order is the explicit guard-maintenance authority |
| Feed later index model | expose deterministic pass/fail behavior for T3 |

## Source Verification Block

| Claimed item | Evidence type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| NR-04 checker stub requires sourceHash or manifest proxy | DOC_ONLY_NEW | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | lines 111-119 | `check_corpus_packet_source_hash` | Checker Spec Stubs | ACCEPT |
| NR-05 checker stub requires canonical normalizedPath | DOC_ONLY_NEW | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | lines 123-132 | `check_corpus_packet_normalized_path` | Checker Spec Stubs | ACCEPT |
| NR-11 checker stub requires dispositionAlias to ACCEPT_DEFERRED | DOC_ONLY_NEW | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | lines 136-145 | `check_corpus_packet_disposition_canonical` | Checker Spec Stubs | ACCEPT |
| NR-05 canonical algorithm exists | EXISTS | `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md` | Canonical Form section | `normalizedPath` | Path Normalization Standard | ACCEPT |
| NR-11 canonical merge rule exists | EXISTS | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | lines 174-219 | `ACCEPT_DEFERRED` | Corpus Intelligence Classification Standard | ACCEPT |
| Existing corpus checker pattern is Python CLI with base/head range | EXISTS | `governance/compat/check_corpus_intelligence_classification.py` | module header and argument/range helpers | `THIS_SCRIPT_PATH` | governance/compat checker pattern | ACCEPT |
| Existing hook chain owns checker registration | EXISTS | `governance/compat/run_local_governance_hook_chain.py` | pre-commit chain checker list | `HOOK_CHAINS` | local governance hook chain | ACCEPT |
| Commit choreography standard exists | EXISTS | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | CI2-T2 Binding section | `CI2-T2 Binding` | Tranche Commit Choreography Standard | ACCEPT |

## Write Ownership

| Path | Action | Owner |
| --- | --- | --- |
| `governance/compat/check_corpus_packet_source_hash.py` | CREATE | Worker |
| `governance/compat/check_corpus_packet_normalized_path.py` | CREATE | Worker |
| `governance/compat/check_corpus_packet_disposition_canonical.py` | CREATE | Worker |
| `governance/compat/test_check_corpus_packet_source_hash.py` | CREATE | Worker |
| `governance/compat/test_check_corpus_packet_normalized_path.py` | CREATE | Worker |
| `governance/compat/test_check_corpus_packet_disposition_canonical.py` | CREATE | Worker |
| `governance/compat/run_local_governance_hook_chain.py` | UPDATE | Worker |
| `governance/compat/run_agent_autorun_workflow_gate.py` | UPDATE IF REQUIRED | Worker |
| `docs/reviews/CVF_CI2_T2_PACKET_NORMALIZATION_CHECKERS_COMPLETION_2026-06-02.md` | CREATE | Worker |

## Allowed Scope

- create `governance/compat/check_corpus_packet_source_hash.py`;
- create `governance/compat/check_corpus_packet_normalized_path.py`;
- create `governance/compat/check_corpus_packet_disposition_canonical.py`;
- create matching tests under `governance/compat/test_check_corpus_packet_source_hash.py`,
  `governance/compat/test_check_corpus_packet_normalized_path.py`, and
  `governance/compat/test_check_corpus_packet_disposition_canonical.py`;
- update `governance/compat/run_local_governance_hook_chain.py` to include the
  three checkers in pre-commit and pre-push chains;
- update `governance/compat/run_agent_autorun_workflow_gate.py` only if needed
  to include the three checkers in relevant autorun phases;
- create `docs/reviews/CVF_CI2_T2_PACKET_NORMALIZATION_CHECKERS_COMPLETION_2026-06-02.md`;
- repair allowed-scope tests/checker defects.

Forbidden scope:

- LPCI runtime/product implementation;
- changing unrelated governance checkers;
- broad hook-chain rewrites;
- new corpus scans;
- public-sync.

## Required First Reads

1. CI2-T1 closure review and source-hash standard.
2. `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md`
3. `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md`
4. `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`
5. `governance/compat/check_corpus_intelligence_classification.py`
6. `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`

## Pre-Flight Checks

| Check | Command | Requirement |
| --- | --- | --- |
| Capture fresh execution base | `git rev-parse --short HEAD` | record as `executionBaseHead` in worker handoff |
| T1 standard exists | `Test-Path docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` | true |
| Existing checker import sanity | `python governance/compat/check_corpus_intelligence_classification.py --base <executionBaseHead> --head HEAD` | exit 0 |

## Execution Plan

1. Verify T1 closure.
2. Implement three checker scripts.
3. Add focused tests.
4. Wire hook/autorun chains only as required.
5. Run tests and closure gates.

## Execution Instructions

1. Implement each checker as a structural file-content checker over changed
   corpus readiness packets and relevant docs/audits or docs/reviews packet
   paths.
2. NR-04: require per-ledger-row `sourceHash`, or packet-level
   `manifestHashProxy: true` plus `manifestProxyException`.
3. NR-05: validate `normalizedPath` against the canonical transformation when
   both `sourcePath` and `normalizedPath` are present.
4. NR-11: validate rows using `DEFER` for bounded deferred implementation carry
   `dispositionAlias: ACCEPT_DEFERRED`; preserve `rawDisposition` when a
   canonical value is emitted.
5. Add focused unit tests for pass/fail cases and worktree-aware range handling.
6. Register the checkers in hook/autorun chain only after tests pass.
7. Follow the tranche commit choreography standard: do not perform archive
   cleanup, session-state sync, public-sync, or unrelated governance cleanup in
   the CI2-T2 implementation batch.

## Commit Choreography / Reviewer Closure

CI2-T2 inherits
`docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`.

Worker obligations:

- capture a fresh `executionBaseHead` before editing;
- use `<executionBaseHead>` for pending checks and component tests;
- keep implementation to CI2-T2 allowed scope;
- do not commit because commit mode is `WORKER_MUST_NOT_COMMIT`;
- do not claim `pre-closure` PASS for pending artifacts;
- return any archive hygiene, stale session state, or unrelated governance drift
  to orchestrator instead of folding it into CI2-T2.

Reviewer / committer obligations:

- capture a fresh `closureBaseHead` immediately before committing;
- commit implementation artifacts separately from closure/session sync;
- stage any required core-guard authorization in the same commit as protected
  governance changes;
- run committed-range pre-closure gates with `--base <closureBaseHead> --head HEAD`;
- perform session-state sync separately if mode or next allowed move changes;
- expect a dedicated handoff-sync-only commit after closure/session commits.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| Checkers implemented | three scripts exist and run with `--base`, `--head`, `--enforce` |
| Tests added | focused positive/negative tests pass |
| Hook integration | local hook chain includes the checkers |
| Autorun integration | added where relevant or explicitly `N/A with reason` |
| Guard self-protection | core guard self-protection gate PASS |
| No runtime bleed | no LPCI/UI/API/provider code touched |

## Evidence Requirements

- Unit test output for all three checkers.
- Hook/autorun diff evidence.
- Core guard self-protection PASS because protected governance paths are edited.

## Review Gate

Reviewer must verify checker scope, tests, hook integration, and absence of
runtime/product changes.

## Closure Checklist

| Item | Required final state |
| --- | --- |
| Three checker scripts | implemented |
| Three test files | implemented and PASS |
| Hook/autorun integration | implemented or justified |
| Core self-protection | PASS |

## Return Conditions

Return to orchestrator when checker implementation is complete or when T1 is
not closed. Stop on forbidden-scope requests.

## Operator Checkpoint

No additional operator checkpoint is required for allowed checker work. Operator
input is required only for runtime/product/public-sync expansion.

## Required Gates

```powershell
python -m pytest governance/compat/test_check_corpus_packet_source_hash.py governance/compat/test_check_corpus_packet_normalized_path.py governance/compat/test_check_corpus_packet_disposition_canonical.py
python governance/compat/check_core_guard_self_protection.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
# Reviewer/committer only, after pending artifacts are approved and committed:
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <closureBaseHead> --head HEAD
python governance/compat/run_local_governance_hook_chain.py --mode pre-commit
git diff --check
git status --short
```

## Worker Autonomy / No-Question Rule

Worker must fix allowed-scope checker/test/hook failures and rerun gates.
Worker must stop for any request to touch LPCI runtime, unrelated core guards,
public-sync, secrets, provider calls, destructive commands, or additional
corpus scans.

## Claim Boundary

CI2-T2 implements structural packet checks only. It does not prove semantic
correctness, legal correctness, runtime retrieval behavior, LPCI readiness, or
production/public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
