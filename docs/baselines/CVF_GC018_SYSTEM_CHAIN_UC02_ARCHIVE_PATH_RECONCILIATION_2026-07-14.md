# CVF GC-018 System Chain UC-02 Archive Path Reconciliation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-07-14

Risk classification: R1

## Purpose

Authorize one bounded local repair of the phase-governance archive-to-consumer
contract that blocked UC-02 before scenario execution.

## Authorization / Decision

UC-02 closed `CLOSED_BLOCKED_BOUNDED` at material commit `7619d807a` with a
secret-safe receipt proving bootstrap failure and zero of nine scenario
executions. Session commit `10e92b885` makes this repair packet the only next
allowed implementation lane.

The repair decision is explicit:

- accepted dated historical inputs remain under the existing `archive/` owner;
- current generated manifests, logs, packets, and posture cache remain at their
  live output paths;
- the shared packet-posture bootstrap generates current runtime evidence once
  before downstream packet runners reuse it;
- no archived file is copied or restored to its former live path.

## Decision

Authorize one no-commit repair worker against the paired work order. The
reviewer retains repair acceptance, material commit, UC-02 rerun release, and
all GAP or coverage state changes.

## Scope / Target / Owner Boundary

The worker may update only the paired work order's Planned Worker Fulfillment
Manifest. The archive index and archived evidence files are read-only. Existing
scenario registry rows, nine UC-02 checkers, coverage ledger, system-chain map,
GAP ledger, roadmap, session state, public repository, provider surfaces, and
the retained UC-02 receipt are read-only.

## Design Control Gate

| Control | Decision |
|---|---|
| Authority ownership | archive remains the sole owner of accepted historical inputs |
| Output ownership | current generated evidence remains under the live phase-governance root |
| Bootstrap order | release-evidence generation once, then local and secondary packet reuse |
| Negative boundary | no live-path restoration, fallback ambiguity, or duplicate authority |
| Proof boundary | focused deterministic tests only; UC-02 rerun remains reviewer-held |
| Provider boundary | no provider/API call or key required |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| shared bootstrap currently skips release generation for both child families | `scripts/run_cvf_packet_posture_state_bootstrap.py` | lines 14-15 and 46-50 | `LOCAL_PACKET`; `SECONDARY_PACKETS` | packet-posture bootstrap | RUNTIME_BEHAVIOR | ACCEPT |
| release gate owns current runtime manifest generation before packet export | `scripts/run_cvf_runtime_evidence_release_gate.py` | constants and `main` | `MANIFEST_SCRIPT`; `PACKET_SCRIPT` | runtime evidence release gate | RUNTIME_BEHAVIOR | ACCEPT |
| v1.9 is a required pre-existing evidence input rather than an emitted fixture | `scripts/runtime_evidence_manifest/fixtures.py` | v1.9 family entry | `receipts` | runtime family configuration | LITERAL_INVARIANT | ACCEPT |
| release packet historical inputs still use former live paths | `scripts/export_cvf_release_packet.py` | lines 22-31 | `DEFAULT_TRACE`; `DEFAULT_BASELINE`; `DEFAULT_EXECUTIVE`; `DEFAULT_REMEDIATION_JSON`; `DEFAULT_REMEDIATION_LOG` | release packet exporter | VALUE_SET | ACCEPT |
| current runtime manifest and log are live generated outputs | `scripts/runtime_evidence_manifest/fixtures.py` | lines 180-181 | `DEFAULT_MANIFEST_JSON`; `DEFAULT_MANIFEST_MD` | runtime evidence manifest exporter | VALUE_SET | ACCEPT |
| all five required historical inputs exist in archive | `docs/reviews/cvf_phase_governance/archive/CVF_ARCHIVE_INDEX.md` | archive table | dated trace, baseline, executive, remediation JSON and log | archive index | EXISTS | ACCEPT |
| current UC-02 blocker is reviewer accepted | `docs/reviews/CVF_SYSTEM_CHAIN_UC02_RUNTIME_TO_ENFORCEMENT_CURRENT_RUN_COMPLETION_2026-07-14.md` | Findings / Position | `CLOSED_BLOCKED_BOUNDED` | UC-02 reviewer closure | VALUE_SET | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Repair control | Evidence requirement | Disposition |
|---|---|---|---|
| diagnose before rerun | retain current diagnostic; no rerun in repair tranche | zero UC-02 invocation | PASS |
| reverse-project accepted finding | preserve GAP and coverage `STALE` | no Catalog/GAP downgrade | PASS |
| distinct failure permits repaired retry | repair must be reviewer accepted first | separate later rerun tranche | PASS |
| stop duplicate low-value branches | full transitive input/output inventory before edits | focused inventory test | PASS |

## Cost And Retry Control

Provider calls: zero. UC-02 proof-run calls: zero. The worker must not execute
the real packet-posture bootstrap or the retained UC-02 runner. This avoids
creating live generated evidence before the repair is independently reviewed.

## Acceptance Criteria

- Historical input constants resolve only to existing archive owners.
- Current generated manifest/log/packet/cache outputs remain live.
- Bootstrap invokes the existing release gate once before both child runners.
- Both child runners still receive the existing skip environment flag.
- Focused tests cover call order, fail-closed release failure, archive inputs,
  live outputs, and absence of restored duplicate files.
- Worker returns without commit and without UC-02/provider invocation.

## Evidence / Verification

Dispatch evidence is the source-verified archive/live ownership matrix, the
clean dispatch base, and the passing pre-dispatch gate. Worker evidence is
limited to source diffs, focused fake-subprocess tests, syntax checks, and a
no-commit return. A later real 9/9 UC-02 receipt is required for operational
proof and is outside this baseline.

## Fail Conditions

- Any archived file is copied, moved, rewritten, or restored.
- A live generated output is incorrectly redirected into archive.
- A fallback silently prefers live over archive for historical authority.
- Existing scenario/checker semantics or retained receipt are changed.
- UC-02, provider, public-sync, or production proof is attempted.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| UC-02 blocked review accepted | material commit `7619d807a` and named completion review | SATISFIED |
| repair packet is next allowed move | session commit `10e92b885` | SATISFIED |
| worktree clean at dispatch authoring | `git status --short` at `10e92b885` | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-repair`, role=`dispatcher`, lifecyclePhase=`dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class runtime-repair --role dispatcher --lifecycle-phase dispatch --surface-selector system-chain --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Roadmap-To-Work-Order Trace Matrix`; `Dependency Release Evidence`; `ADIF Defect Registry Disclosure`; `Public Export Disposition` |
| gateRunPurpose | pre-dispatch confirmation after full transitive source and ownership review |
| claimBoundary | repair authorization only; no implementation or rerun evidence |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | GC-018 dispatch baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | manually authored from the current governed baseline pattern after source verification |
| checkerReadAheadConfirmation | applicable checker sources and literal-format gotchas were read before the bundled gate |
| docOnlyNewFields | N/A with reason: no new runtime or schema fields |
| claimBoundary | dispatch authorization only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime-chain repair packet; no public-sync scope.

## Claim Boundary

This baseline authorizes only the archive/live ownership repair and focused
tests. It does not prove UC-02, change the semantic system-chain verdict, or
claim provider, public, production, scale, certification, or user value.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | paired SCLP-UC02-R1 work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | SCLP-UC02-R1 completion review | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | system-chain live-proof roadmap | unchanged; UC-02 remains rerun-required | N/A with reason |
| Registry JSON | system-chain GAP index | unchanged; repair does not close the runtime GAP | BLOCKED with reason |
| Registry Markdown | system-chain GAP README | unchanged; 9/9 receipt is still absent | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence consumed | repository source only | N/A with reason |
| System loop interlock | focused source/test evidence | structural repair accepted; runtime proof remains `STALE` | PASS |
| Session continuity | active session state | separate synchronization after material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| R1-B-01 | focused pytest output | N/A with reason: command output | 15 passing tests | 15 passed | PASS |
| R1-B-02 | source and focused tests | N/A with reason: source constants | five archive inputs and live outputs preserved | exact ownership assertions pass | PASS |
| R1-B-03 | N/A with reason: no runtime receipt permitted | N/A with reason: no current invocation | no UC-02 success claim | coverage remains `STALE` | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | UC-02 repair packet authoring, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, git, apply_patch, dispatch gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | active nextAllowedMove after material commit `7619d807a` |
| Before status evidence | clean HEAD `10e92b885` |
| After status evidence | source-verified repair dispatch packet |
| Diff evidence | two-file dispatch diff before commit |
| Approval boundary | packet authoring and one later no-commit repair worker |
| Claim boundary | no implementation, bootstrap run, UC-02 rerun, or provider call |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc02-archive-path-repair-dispatch-2026-07-14 |
| Expected manifest | paired GC-018 baseline and work order |
| Actual changed set | paired GC-018 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
