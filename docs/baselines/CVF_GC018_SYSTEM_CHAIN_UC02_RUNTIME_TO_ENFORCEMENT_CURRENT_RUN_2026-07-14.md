# CVF GC-018 System Chain UC-02 Runtime-To-Enforcement Current Run

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018_baseline

Date: 2026-07-14

Risk classification: R1

## Purpose

Authorize one bounded, provider-free current invocation of the canonical
registry-driven CF-076 through CF-084 runtime-to-enforcement chain. The tranche
closes only the stale current-run evidence gap recorded by UC-02.

## Authorization / Decision

The operator instructed continuation from the accepted system-chain live-proof
T0 process. Material commit `e4a585b8c` establishes UC-02 as the next use case;
session commit `a9507c1b0` releases packet authoring only. This baseline and its
paired work order authorize a no-commit worker after pre-dispatch acceptance.

## Scope / Target / Owner Boundary

Target: the nine canonical registry rows CF-076 through CF-084, their shared
packet-posture bootstrap, their real command arrays, the packet-posture gate
runner, and the nine named governance checkers.

The scenario registry owns scenario identity and command routing. The existing
packet-posture runner owns four-packet checker invocation. A new proof runner
may select the exact nine registry rows and emit a secret-free current receipt;
it may not redefine any scenario, checker, packet, semantic verdict, or policy.

## Design Control Gate

| Control | Decision |
|---|---|
| Proof class | `CURRENT_RUNTIME_INVOCATION` |
| Provider boundary | not applicable: this chain is local registry-to-subprocess enforcement and contains no AI/provider edge |
| Selection | exactly CF-076 through CF-084 from the canonical registry |
| Invocation | one planned proof-runner invocation; one diagnosed retry maximum |
| Mutation | one bounded proof runner, focused test, receipt, and worker return |
| Semantic boundary | no change to `PROVEN_CONNECTED_VIA_DATA_DRIVEN_REGISTRY` |
| Failure boundary | any missing/duplicate scenario, command drift, bootstrap failure, checker failure, or incomplete denominator fails closed |

## Current Runtime Freshness Verification

Fresh source review at `a9507c1b0` confirms:

- `scripts/run_cvf_cross_extension_conformance.py` reads
  `docs/reference/CVF_CONFORMANCE_SCENARIOS.json` and subprocess-executes its
  command arrays;
- CF-076 through CF-084 share `PACKET_POSTURE_STATE_GROUP`;
- the generic packet runner invokes each selected checker against four
  canonical packets;
- the current aggregate runner has no bounded scenario-selection CLI;
- the retained R90 PASS rows are historical, not this tranche's current-run
  receipt.

The worker must re-check these facts at `executionBaseHead` before mutation.

## Source / Predecessor Evidence

| Predecessor | Evidence | Disposition |
|---|---|---|
| live-proof T0 process | material commit `e4a585b8c` | SATISFIED |
| UC-02 packet-authoring release | session commit `a9507c1b0` and active nextAllowedMove | SATISFIED |
| semantic chain owner | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` lane `RUNTIME_TO_ENFORCEMENT` | SATISFIED |
| operational gap owner | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_COVERAGE.json` UC-02 | SATISFIED |

## Proposed Tranche

Create one dedicated UC-02 proof runner that reads the canonical scenario
registry, requires exactly nine unique rows CF-076 through CF-084, runs the
existing packet-posture bootstrap once, executes the nine unmodified registry
commands with the bootstrap-skip environment already used by the aggregate
runner, and writes one atomic JSON receipt. Add focused tests for exact
selection, missing/duplicate rows, command preservation, failure propagation,
denominator integrity, and secret-safe output.

## Work Plan

1. Re-verify all source rows and exact symbols.
2. Implement the bounded proof runner without modifying existing registry,
   checker, packet, aggregate runner, or CI behavior.
3. Run focused tests and negative fixtures.
4. Invoke the proof runner once and retain its receipt.
5. Diagnose before any retry; permit at most one result-changing retry.
6. Return without commit for reviewer reconciliation.

## Acceptance Criteria

- exactly nine unique scenario IDs are loaded from the canonical registry;
- every executed command equals its registry command array;
- shared bootstrap runs once and failures propagate non-zero;
- every scenario runs against all four canonical packets through the existing
  packet-posture gate runner;
- the receipt records call-level run status and a 9-scenario denominator;
- `9/9 PASS` is required for UC-02 acceptance;
- no provider/API key, mock, direct checker shortcut, or semantic-map mutation;
- worker leaves HEAD unchanged.

## Verification / Evidence

Required evidence: focused tests, one current-run JSON receipt, per-scenario
status/duration/command digest, aggregate 9/9 denominator, bootstrap result,
diagnostic if needed, exact diff, clean secret scan, and no-commit worker return.

## Stop Conditions

- any canonical row or symbol cannot be source-verified;
- registry contains missing or duplicate target IDs;
- proof requires modifying an existing checker, packet, scenario command, or
  semantic verdict;
- unclear failure lacks a diagnostic;
- a second retry would be needed;
- output contains secrets or uncontrolled raw subprocess content.

## Non-Goals

- no provider call or release-quality governance claim;
- no full CF-001 through CF-084 run;
- no checker/policy repair;
- no CI, Web, public-sync, session-state, or Catalog/GAP mutation;
- no production, universal, or real-user claim.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`live-proof`, role=`dispatcher`, lifecyclePhase=`dispatch`

Query:
`python governance/compat/run_adif_defect_resolver.py --task-class live-proof --role dispatcher --lifecycle-phase dispatch --surface-selector system-chain --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | GC-018 baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | all content manually source-verified |
| checkerReadAheadConfirmation | applicable checker sources read before first bundled gate |
| docOnlyNewFields | N/A with reason: baseline defines no runtime or receipt fields |
| claimBoundary | dispatch baseline only; no UC-02 execution |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gc018_stop_boundary_semantics.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Current Runtime Freshness Verification`; `Source Verification Block`; `Roadmap-To-Work-Order Trace Matrix`; `Agent Handoff Contract Control Block`; `Public Export Disposition` |
| gateRunPurpose | confirmation and dispatch evidence after source verification; not first discovery |
| claimBoundary | UC-02 packet and one provider-free current-run proof only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime-chain evidence; no public-sync authority.

## Claim Boundary

This baseline authorizes one bounded current invocation of CF-076 through
CF-084. It does not prove provider governance, all CVF enforcement, production,
public readiness, or real-user value.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | UC-02 packet authoring, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, apply_patch, dispatch gates |
| Target paths | paired GC-018 baseline and work order |
| Allowed scope source | operator continuation under UC-02 nextAllowedMove |
| Before status evidence | UC-02 planned but undispatched |
| After status evidence | source-verified UC-02 dispatch packet |
| Diff evidence | dispatch changed set captured before commit |
| Approval boundary | packet authoring and later bounded no-commit worker execution |
| Claim boundary | no UC-02 execution during packet authoring |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc02-dispatch-2026-07-14 |
| Expected manifest | this baseline and paired work order |
| Actual changed set | this baseline and paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
