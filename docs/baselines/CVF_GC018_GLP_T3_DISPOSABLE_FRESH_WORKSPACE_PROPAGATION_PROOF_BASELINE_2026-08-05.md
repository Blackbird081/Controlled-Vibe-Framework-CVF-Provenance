# CVF GC-018 Baseline - GLP T3 Disposable Fresh Workspace Propagation Proof

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_DISPATCH_READY

docType: baseline

Date: 2026-08-05

Batch ID: GLP-T3

dispatchBaseHead: `34dfbdb0c`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: bounded local propagation-proof worker

## Purpose

Define a read-only-to-provenance, disposable-workspace proof of the accepted
GLP-T2R1 carrier projection. The proof must enumerate the generated manifest,
assert expected artifacts and project guidance, scan for private leakage, and
clean every disposable path without changing implementation source.

## Source / Predecessor Evidence

- roadmap: `docs/roadmaps/CVF_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_ROADMAP_2026-08-05.md`;
- accepted alignment review:
  `docs/reviews/CVF_GLP_T2R1_CP1_BYTE_PRESERVING_MERGE_REPAIR_COMPLETION_2026-08-05.md`;
- accepted material commit: `f59457b9a`;
- proof owner: `scripts/test_cvf_golden_downstream_bootstrap.ps1`.

## Baseline Decision

Decision: `RELEASE_GLP_T3_BOUNDED_PROOF`.

The source owner and proof boundary are identifiable. The operator explicitly
released this bounded execution on 2026-08-05. Dispatch still requires a
non-empty committed release range and a passing pre-dispatch gate.

## Authorization / Dependency Gate

| Dependency | Evidence | Disposition |
|---|---|---|
| GLP-T2R1 accepted | completion review above; commit `f59457b9a`; reviewer accepted bounded | ACCEPT |
| GLP-T3 roadmap scope | roadmap Work Plan row and T2R1 outcome | ACCEPT |
| local disposable proof owner | golden harness setup, assertions, and cleanup | ACCEPT |
| implementation change need | current harness already covers the required generated surfaces and carrier | N/A with reason: proof-only execution |
| execution authority | explicit operator release recorded on 2026-08-05 | ACCEPT |

## Scope / Target / Owner Boundary

Allowed worker outputs after release:

- `docs/audits/CVF_GLP_T3_DISPOSABLE_FRESH_WORKSPACE_PROPAGATION_PROOF_2026-08-05.md`
- `docs/reviews/CVF_GLP_T3_DISPOSABLE_FRESH_WORKSPACE_PROPAGATION_PROOF_WORKER_RETURN_2026-08-05.md`

Allowed execution after release:

- one local invocation of `scripts/test_cvf_golden_downstream_bootstrap.ps1`;
- read-only inspection of the named source/template owners and command output;
- disposable local Git repositories and temporary directories created by the
  existing harness, followed by its governed cleanup path.

Forbidden:

- edits to scripts, templates, tests, checkers, catalogs, profiles, runtime,
  session state, downstream repositories, or public-sync surfaces;
- persistent generated workspace or fixture retention;
- provider, network, credential, live-governance, push, deployment, or release
  action;
- inference of downstream adoption or causal latency reduction.

## Risk Classification

Risk: R1.

Reason: the worker creates only two provenance evidence artifacts and runs one
existing local hermetic harness. The harness creates and removes disposable
directories behind a path-safety guard. Any need to retain or mutate a real
workspace, change source, use the network, or rerun after an unclear failure
stops the tranche.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GLP-T3 --title "Disposable Fresh Workspace Propagation Proof" --date 2026-08-05 --base 10319c7dc --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the roadmap-derived proof-only scope, exact two-output manifest, one-run ceiling, independent review route, and explicit execution hold |
| checkerReadAheadConfirmation | dispatch-quality, ADIF disclosure, handoff boundary, operation trace, public disposition, file-size, roadmap freshness, and worker-return quality sources |
| docOnlyNewFields | generatedManifestReadout; expectedArtifactAssertionLedger; guidanceReadout; privateLeakageReadout; callLevelResult |
| claimBoundary | packet definition only; no proof execution or downstream adoption claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| GLP-T3 requires a disposable fresh-workspace proof | VALUE_SET | `docs/roadmaps/CVF_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_ROADMAP_2026-08-05.md` | Work Plan GLP-T3 row | `GLP-T3` | GLP roadmap | ACCEPT |
| GLP-T2R1 alignment is accepted bounded | VALUE_SET | `docs/reviews/CVF_GLP_T2R1_CP1_BYTE_PRESERVING_MERGE_REPAIR_COMPLETION_2026-08-05.md` | Findings / Position | `Reviewer verdict` | GLP-T2R1 completion review | ACCEPT |
| harness creates a hermetic local core and disposable project | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | setup lines 75-89 | `New-CvfHermeticCoreClone`; `projectA` | golden downstream bootstrap harness | ACCEPT |
| harness enumerates required generated surfaces | VALUE_SET | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | AC-01 lines 91-102 | `requiredSurfaces` | golden downstream bootstrap harness | ACCEPT |
| harness reads generated manifest and requiredDocs | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | BSL-R3 lines 120-124 | `manifestA`; `requiredDocs` | golden downstream bootstrap harness | ACCEPT |
| harness verifies the five-rule project guidance carrier | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | helper lines 63-70 and GLP assertions | `Test-CvfCarrierContent` | golden downstream bootstrap harness | ACCEPT |
| harness scans exact private sentinels | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | GLP private leakage block lines 352-369 | `privateSentinels`; `privateHits` | golden downstream bootstrap harness | ACCEPT |
| harness removes tracked temp roots and fails on residue | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | cleanup lines 551-578 | `Remove-CvfHermeticDirectory`; `residue` | golden downstream bootstrap harness | ACCEPT |

No provider-local memory or downstream evidence is used as authority.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | LOCAL_SOURCE_VERIFICATION |
| reason | the packet uses current local harness and template source only |
| requiredFutureAction | any provider/live or persistent-workspace proof needs a separate packet and authority |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --surface-selector scripts/test_cvf_golden_downstream_bootstrap.ps1 --risk-ceiling MEDIUM --max-results 20 --json`

Returned defects: NONE_RETURNED

## Proof Contract

| Proof dimension | Required evidence | Fail condition |
|---|---|---|
| call-level result | one harness invocation and its final assertion denominator | non-zero exit, missing denominator, or second execution without classified reason |
| generated manifest | observed `.cvf/manifest.json` keys plus requiredDocs assertions | missing file, parse failure, or missing required catalog/script entries |
| expected artifacts | exact AC-01 required-surface list and missing count | any required surface absent |
| project guidance | exactly one carrier heading and all five semantics in generated `AGENTS.md` | missing, duplicate, or incomplete carrier |
| negative leakage | exact sentinel list, inspected carrier consumers, and zero-hit count | any hit or incomplete scan scope |
| isolation and cleanup | hermetic paths only and residue count zero | persistent residue or unsafe cleanup target |
| claim boundary | local generated-fixture propagation only | adoption, production, provider, public, or causal-effect overclaim |

## Reviewer Independence

The worker must not commit or review its own result. An independent reviewer
recomputes the manifest/artifact/guidance/leakage conclusions from the worker
record and may rerun the existing harness once only when the first run is
semantically interpretable. Review disagreement remains visible in the
completion disposition.

## Stop Conditions

Stop as `BLOCKED_WITH_REASON` for any source contradiction, unexpected dirty
worktree, need for an implementation edit, non-disposable path, cleanup
failure, private leakage, network/provider demand, unclear first-run failure,
or change to risk/external-effect/commit-owner boundaries.

## Evidence / Verification

Packet evidence consists of direct current-source verification, the accepted
T2R1 completion artifact, the exact two-output manifest, and the held
dependency row. Before release, anchors must be refreshed and pre-dispatch must
pass on a committed non-empty packet range. Worker evidence must then come from
the single local harness call and the two uncommitted outputs.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | generated disposable project `AGENTS.md` | static guidance readout only | harness and audit | local bootstrap projection | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no ingress, auth, receipt, mutation, or runtime claim | exact proof-only scope | external adapter excluded | `DEFERRED_WITH_REASON` |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | source-verification claim types and dispositions; ADIF query line; no-commit handoff route; operation-trace labels; public-export tokens; worker-return headings and no-commit evidence |
| gateRunPurpose | confirmation of packet shape and source fidelity before release |
| claimBoundary | local held baseline only; no execution evidence |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the accepted carrier appears exactly once with
all five semantics in a disposable fresh project, alongside every required
surface and a valid manifest, with zero private leakage and zero residue.

Evidence Comparison Requirement: the worker records each dimension separately
and preserves any contradiction rather than collapsing all evidence into the
harness exit code.

Contradiction Handling Requirement: any failed dimension stops the proof or
narrows the claim; gate success cannot override semantic evidence.

Claim Update Requirement: return `PROPAGATION_PROVEN_BOUNDED` or
`PROPAGATION_PROOF_FAILED`, with local-only scope.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local private provenance repository |
| Session or invocation | GLP-T3 packet authoring, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | startup reads, roadmap/source inspection, scaffold helper, ADIF resolver, apply_patch, dispatch gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | active next-move permits source-verified GLP-T3 packet authoring only |
| Before status evidence | HEAD `10319c7dc`; clean worktree |
| After status evidence | paired packet held for explicit execution authority |
| Diff evidence | `git diff --name-status` limited to paired packet paths |
| Approval boundary | packet authoring only |
| Claim boundary | no worker execution, downstream mutation, public sync, provider/network use, push, or deployment |
| Agent type | dispatcher |
| Invocation ID | `glp-t3-packet-authoring-2026-08-05` |
| Expected manifest | this baseline; paired work order |
| Actual changed set | this baseline; paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | held local disposable-workspace proof packet |
| claimDisposition | N/A with reason: no proof execution in this baseline |
| receiptEvidence | N/A with reason: no runtime/provider receipt applies |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source-verification and packet diff only |
| invocationBoundary | local documentation authoring only |
| interceptionBoundary | no shell, IDE, filesystem, provider, or agent-runtime interception claim |
| claimLanguage | future bounded proof contract, not completed propagation evidence |
| forbiddenExpansion | no source edit, persistent workspace, downstream, provider/live, public-sync, push, or deployment action |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this provenance packet neither changes public artifacts nor authorizes
public sync.

## Operator Release

The operator explicitly released GLP-T3 execution on 2026-08-05. Worker routing
is execution-layer metadata and does not alter the role-neutral evidence
contract, independent-review boundary, one-call ceiling, zero-network rule, or
no-commit requirement.

## Claim Boundary

This baseline releases a bounded GLP-T3 proof packet. It does not execute the
harness, mutate a real workspace, prove adoption, call a provider, use the
network, publish, push, or deploy.
