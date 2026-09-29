# CVF GC-018 Baseline - MFRP-H0 Autorun Receipt Verifier Identity Hardening

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MFRP-H0

Dispatch base head: `4def03d7aa7665cdc80ee56ab3ce702f3a2787e0`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: orchestrator/reviewer

successorTrancheOpened: NO

## Purpose

Authorize one bounded repair of the existing local autorun PASS-receipt reuse
boundary. H0 binds receipt reuse to the repository-controlled verifier input
snapshot and the executing Python identity so an unchanged argv list cannot
reuse evidence produced by different verifier bytes.

## Root Problem

`cvf.autorun.pass-receipt.v1` already provides content-addressed local PASS
receipts and optional reuse. Its `_command_manifest_hash` covers only command
names and argv, while `_worktree_fingerprint` covers the current path plan.
Changing a verifier body or a shared/configuration input outside that path
plan can therefore leave the receipt's declared command identity unchanged.
That is a verifier-evidence identity defect, not an agent-role defect.

## Accepted Authority

| Authority | Accepted fact |
|---|---|
| `governance/compat/run_agent_autorun_workflow_gate.py` | `cvf.autorun.pass-receipt.v1` ships; `_command_manifest_hash` hashes name and argv only; `_load_valid_receipt` trusts exact context-field equality. |
| `governance/compat/agent_autorun_command_catalog.py` | The phase command tuples are the executable checker catalog consumed by the runner. |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | Current tests cover argv drift, context mismatch, malformed receipt and changed-file content, but not cross-batch verifier/shared-input/interpreter drift. |
| `docs/reviews/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_EXTERNAL_FINDING_ABSORPTION_AND_CVF_RECONCILIATION_2026-09-01.md` | CVF accepted H0, rejected direct-script-only binding, and requires a conservative dependency closure plus interpreter identity or cache miss. |
| `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | H0 precedes P1 and must close with bounded hostile tests or disable reuse and stop. |

## Decision / Baseline

H0 uses a conservative repository-controlled verifier-input snapshot instead
of an incomplete declared dependency list. The snapshot is the current byte
state of every Git-tracked file plus every untracked non-ignored regular file.
Every repository-relative command file must be a member; an ignored, unsafe or
unresolved command file makes reuse unavailable. This deliberately
over-invalidates: unrelated repository changes can cause a cache miss, but no
repo-visible shared module, registry, configuration, fixture, standard or
checker input can drift without changing the snapshot digest.

The digest profile is `cvf.autorun.verifierIdentity.v1`. Its preimage is a
restricted RFC 8785 JCS object containing only strings, arrays and objects:
profile, digest algorithm, sorted `{path, sha256}` file records, and an
interpreter record. Paths are repository-relative, slash-normalized and sorted
lexicographically. The interpreter record binds implementation, cache tag,
five-part version, resolved executable path and executable byte SHA-256.

Unknown, unsafe, non-regular, unreadable, unstable-during-read or otherwise
unresolved identity input makes receipt reuse unavailable and runs the full
autorun bundle. It never turns incomplete identity into a hit. The full bundle
may still run; a reusable receipt may be written only from a complete identity.
After a fresh PASS the runner recomputes the complete snapshot and writes a
receipt only when pre-run and post-run identities are equal. This prevents a
mid-bundle mutation from laundering the earlier snapshot into new evidence.

Receipt schema migrates to `cvf.autorun.pass-receipt.v2`. A v1 receipt is a
deterministic miss, never upgraded in place and never accepted by fallback.
The receipt records the named identity profile and digest. Hash construction
has a fixed independent test vector; it must not reuse the TruthReceipt-specific
profile label `cvf.sotThreeLayer.receiptHash.v1`.

## Hostile Acceptance Matrix

| Case | Required observation |
|---|---|
| unchanged exact state | v2 receipt is reused and no command executes |
| v1 receipt | schema mismatch; full bundle executes |
| direct checker body drift with identical argv | identity digest mismatch; full bundle executes |
| prior-batch tracked verifier drift outside current path plan | identity digest mismatch; full bundle executes |
| shared imported Python module drift | identity digest mismatch; full bundle executes |
| tracked registry/configuration/fixture/standard drift | identity digest mismatch; full bundle executes |
| command-catalog or autorun-runner drift | identity digest mismatch; full bundle executes |
| Python implementation/version/cache-tag/path/executable digest drift | interpreter identity mismatch; full bundle executes |
| unreadable or unstable identity input | reuse unavailable; full bundle executes; no reusable receipt written from incomplete context |
| repository input drifts while the bundle runs | pre/post identities differ; PASS may be reported from the executed checks but no reusable receipt is written |
| path order variation | identical canonical preimage and digest |
| Unicode path/string vector | exact published JCS bytes and SHA-256 match an independent literal vector |
| reuse switch absent | full bundle executes even when a valid receipt exists |
| rollback/reuse disabled | full bundle remains functional and PASS receipt reuse grants no authority |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| PASS receipt schema is v1 | executable source | `governance/compat/run_agent_autorun_workflow_gate.py` | constants | `RECEIPT_SCHEMA` | autorun runner | ACCEPT |
| command manifest hashes name and argv only | executable source | `governance/compat/run_agent_autorun_workflow_gate.py` | `_command_manifest_hash` | `payload` | autorun receipt context | ACCEPT |
| worktree digest follows commit-steward changed paths | executable source | `governance/compat/run_agent_autorun_workflow_gate.py` | `_worktree_fingerprint` | `build_path_plan` | autorun receipt context | ACCEPT |
| reuse compares every expected context field | executable source | `governance/compat/run_agent_autorun_workflow_gate.py` | `_load_valid_receipt` | expected-field loop | autorun receipt validator | ACCEPT |
| command catalog is imported into the runner | executable source | `governance/compat/agent_autorun_command_catalog.py` | command tuple definitions | `_common_commands`; `_pre_implementation_commands`; `PRE_PUSH_COMMANDS` | autorun command catalog | ACCEPT |
| current focused tests omit verifier-input and interpreter drift | regression source | `governance/compat/test_run_agent_autorun_workflow_gate.py` | receipt and fingerprint tests | `test_valid_receipt_requires_exact_context`; `test_worktree_fingerprint_changes_with_file_content` | autorun focused suite | ACCEPT |
| H0 requires conservative closure, schema migration and hostile drift tests | governed reconciliation | `docs/reviews/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_EXTERNAL_FINDING_ABSORPTION_AND_CVF_RECONCILIATION_2026-09-01.md` | H0 Bounded Design Requirement | MFRP-H0 | GCLH/MFRP decision owner | ACCEPT |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `governance/compat/run_agent_autorun_workflow_gate.py` | MODIFY receipt identity/context/reuse/write behavior only. |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | MODIFY with fixed-vector, cache-hit and hostile drift regressions. |
| `docs/reviews/CVF_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_WORKER_RETURN_2026-09-01.md` | CREATE full no-commit implementation return and evidence ledger. |

No other path may change.

## Acceptance Strategy

Acceptance is evidence-graph review, not reimplementation. The reviewer reads
the diff, recomputes the fixed hash vector independently, reruns the focused
suite and at least the cross-batch/shared-input/interpreter hostile probes,
then runs governed gates. The reviewer does not rewrite the worker's solution
unless a bounded evidence correction within the same three paths is necessary.

Pass means only that local receipt reuse is invalidated on the declared input
and interpreter drifts. It does not prove checker semantics, artifact truth,
review sufficiency, provider behavior or phase completion.

## Evidence / Verification

Worker must run the pre-implementation autorun gate, the focused autorun
receipt suite, dispatch-author and worker-return gates, Core Guard, SCEC, diff
hygiene and exact status. Reviewer independently recomputes the published hash
vector and reruns exact-hit, prior-batch verifier drift, shared-input drift and
interpreter drift probes before accepting either terminal disposition. No
provider-backed live proof applies because H0 changes only local governance
receipt reuse.

## Rollback Boundary

Immediate safe rollback is to stop passing `--reuse-valid-receipt`, or make
reuse deterministically unavailable while retaining full autorun execution.
If H0 cannot prove the matrix, reviewer selects `DISABLE_REUSE_AND_STOP`; no P1
successor opens. Revert only the two protected Python changes and the H0 return;
do not alter prior GCLH/MFRP learning artifacts.

## Negative Search And Collision Discipline

- Exact three target paths were absent before authoring.
- Search roots: `docs/roadmaps`, `docs/reviews`, `docs/baselines`,
  `docs/work_orders`, `CVF_SESSION` and `governance/compat`.
- Search tokens: `MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING` and
  `mfrp-autorun-receipt-verifier-identity`.
- Existing H0 references are planning/continuity pointers only; no competing
  baseline, work order, worker return or implementation owner exists.
- Disposition: `ABSENT_H0_EXECUTION_PACKET_CONFIRMED`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`autorun receipt verifier identity hardening`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "autorun receipt verifier identity hardening" --role dispatcher --lifecycle-phase dispatch --json`
- Returned defects: `NONE_RETURNED`
- Disposition: current MFRP reconciliation remains the written defect owner;
  no new ADIF entry is authorized in H0.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Commit mode: WORKER_MUST_NOT_COMMIT`; Source Verification columns; prompt-envelope labels; SCEC fields; review-control fields; trace fields; protected-path authorization labels |
| gateRunPurpose | Confirm the source-derived packet after authoring, not discover its structure by failure. |
| claimBoundary | Dispatch and authorization shape only; H0 implementation remains pending. |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-H0 --title "Autorun Receipt Verifier Identity Hardening" --date 2026-09-01 --base 4def03d7a --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --scec-problem-key mfrp-autorun-receipt-verifier-identity --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | protected-governance-path, internal no-commit implementation profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with exact live defect, conservative snapshot contract, hostile matrix, exact manifest and rollback. |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | verifier identity profile, snapshot membership and hostile case identifiers |
| claimBoundary | Dispatch provenance only. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: harden only the existing autorun receipt
identity/reuse boundary and its focused tests.

Protected paths:

- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`

Operator authorization: the operator approved the machine-first CVF foundation
upgrade and requested continuation after accepting the independently critiqued
H0-first roadmap revision.

Rollback boundary: disable optional receipt reuse and keep the full autorun
bundle; no command catalog, hook, standard, session, provider or product path
may be changed to make reuse pass.

## Claim Boundary

This baseline authorizes exactly two protected Python modifications and one
worker return. It does not authorize command-set changes, semantic checker
changes, new standards/reference families, ADIF edits, hooks, session state,
P1/P2, provider/live execution, public sync, deployment or production claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF governance-foundation hardening.
