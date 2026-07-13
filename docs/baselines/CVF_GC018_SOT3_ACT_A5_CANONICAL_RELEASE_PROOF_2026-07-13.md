# CVF GC-018 Baseline - SOT3 Activation A5 Canonical Release Proof

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: SOT3-ACT-A5

Date: 2026-07-13

Dispatch base head: `6a8f52b26`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Codex reviewer/closer

Worker target: delegated release-integration and live-proof worker

## Purpose

Authorize one bounded A5 tranche that makes SOT3 proof mandatory in the
canonical release gate, emits correlated SOT3 JSON and manifest evidence, and
runs the required real-provider release command once.

## Authority / Decision

The operator authorized A0-A5 toward `LIVE_GOVERNANCE_PROVEN_BOUNDED`. A4
closed at material commit `cab8133ea`; the activation roadmap now records
`A4_CLOSED_PASS_BOUNDED_A5_PACKET_NEXT`. This baseline releases A5 packet
execution only. It does not pre-approve the final claim.

## Source / Predecessor Evidence

The accepted A4 completion, material commit `cab8133ea`, activation roadmap
A5 Detailed Design, current canonical release runner, accepted A4 runner, and
live evidence manifest builder are the source/predecessor packet. Runtime
source overrides summaries.

## Decision / Baseline / Proposed Tranche

Decision: release one no-commit A5 implementation and canonical live-proof
tranche. Baseline: A4 is accepted but SOT3 is not yet a mandatory canonical
release check. Proposed tranche: add strict SOT3 release admission, structured
JSON/manifest evidence, no-blind-retry discipline, focused tests, and one
planned canonical run.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| A4 failure/recovery closure | `docs/reviews/CVF_SOT3_ACT_A4_FAILURE_AND_RECOVERY_BOUNDARY_PROOF_COMPLETION_2026-07-13.md`; commit `cab8133ea`; `Status: CLOSED_PASS_BOUNDED` | accepted A4 closure must precede A5 | ACCEPT |
| A5 roadmap release | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; `Status: A4_CLOSED_PASS_BOUNDED_A5_PACKET_NEXT` | fresh A5 packet required | ACCEPT |

## Scope / Target / Owner Boundary

Allowed:

- add a bounded SOT3 A5 proof adapter around the accepted A4 runner;
- wire that adapter into `scripts/run_cvf_release_gate_bundle.py` as a
  mandatory live check in the default release-quality path;
- add isolated Python tests for SOT3 admission, JSON projection, manifest
  inclusion, and no-blind-retry behavior;
- execute the canonical bundle with real Alibaba credentials and persist A5
  result, diagnostic, manifest, and worker return.

Forbidden:

- changing Truth Refinery, Truth Kernel, Truth Flow, CVF Web runtime, A1-A4
  source, historical A1-A4 evidence, provider prompts, models, or token caps;
- mock substitution for SOT3 or live governance proof;
- automatic provider retry before a secret-safe diagnostic and explicit
  result-changing action;
- public-sync, production deployment, universal-control, scale, certification,
  or real-user-value claims;
- worker commit or session-state mutation.

## Live Proof Boundary

Alibaba calls are operator-unmetered for this tranche, but the first canonical
release invocation is the only planned run. A failed, partial, empty, timed-out,
or unclear live stage must persist a diagnostic and stop. A later rerun needs a
specific result-changing repair; quota availability is not a reason to retry.

The final claim remains reviewer-owned. Worker success supports only
`COMPLETE_PENDING_REVIEW`.

## Acceptance Criteria

- A5 SOT3 check is mandatory in the default canonical release bundle.
- SOT3 check fails when proof is absent, skipped, mocked, malformed, not
  provider-backed, not context-correlated, or lacks durable owner IDs.
- release JSON contains a top-level SOT3 evidence object.
- release manifest hashes both the release result and A5 diagnostic when the
  diagnostic path is supplied.
- the release runner no longer performs an immediate blind Playwright retry.
- canonical command uses a real key and passes with no skipped mandatory live
  check.
- final evidence remains secret-safe and A5-bounded.

## Verification / Evidence

- focused Python unit tests;
- Python compile checks;
- dry-run structural JSON proof with zero provider calls;
- exactly one planned canonical live bundle invocation;
- A5 release JSON, diagnostic, and manifest hash recomputation;
- reviewer-fast, pre-implementation, worker-return, and commit-steward gates;
- `git diff --name-status`, `git status --short`, and unchanged worker HEAD.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id SOT3-ACT-A5 --title "SOT3 Activation A5 Canonical Release Proof" --date 2026-07-13 --base 6a8f52b26 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "A4 closure cab8133ea PREDECESSOR_SATISFIED" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with verified A4 dependency, current release-runner design, exact scope, diagnostics, and claim boundary |
| checkerReadAheadConfirmation | dispatch quality, handoff, live diagnostics, closure package, finding-learning, file-size, and autorun controls read |
| docOnlyNewFields | declared in paired work order |
| claimBoundary | dispatch authorization only; no A5 execution or final claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`SOT3 canonical live release bundle dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "SOT3 canonical live release bundle dispatch" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector "release runner live provider evidence manifest" --risk-ceiling HIGH --max-results 30 --json`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Returned defect count | 0 |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | worker must still read ADIF-0030 and ADIF-0031 because A5 reuses the runner-only live boundary and exact-manifest discipline |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; Source Verification Block; Required Artifact Manifest; Agent Handoff Contract Control Block; Public Export Disposition |
| gateRunPurpose | dispatch authoring confirmation after source verification |
| claimBoundary | checker compliance does not prove A5 runtime or live behavior |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: A5 uses operator-local credentials and private provenance evidence. No
public-sync authority exists.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this artifact | `Status: DISPATCH_READY` | N/A with reason: dispatch only |
| Work order status | paired A5 work order | `Status: DISPATCH_READY` | N/A with reason: execution pending |
| Completion or reviewer artifact | future A5 completion review | future reviewer evidence | N/A with reason: execution pending |
| Roadmap state | activation roadmap | `Status: A4_CLOSED_PASS_BOUNDED_A5_PACKET_NEXT` | PASS |
| Registry JSON | corpus registry | BLOCKED with reason: A5 has no corpus ownership | BLOCKED with reason |
| Registry Markdown | corpus front door | BLOCKED with reason: A5 has no catalog ownership | BLOCKED with reason |
| External evidence digest | future A5 manifest | future SHA-256 entries | N/A with reason: worker-owned future evidence |
| System loop interlock | N/A with reason: no automated loop edge at dispatch | N/A | N/A with reason |
| Session continuity | separate post-dispatch sync | pending after packet commit | N/A with reason |

## Claim Boundary

This baseline authorizes A5 implementation and one planned canonical live
release run. It does not assert `LIVE_GOVERNANCE_PROVEN_BOUNDED`, release to
users, production readiness, public availability, scale, or user validation.
