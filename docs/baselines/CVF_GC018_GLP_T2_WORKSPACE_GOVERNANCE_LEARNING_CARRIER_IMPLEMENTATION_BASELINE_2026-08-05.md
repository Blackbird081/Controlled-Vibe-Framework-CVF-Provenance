# CVF GC-018 Baseline - GLP T2 Workspace Governance Learning Carrier Implementation

Memory class: FULL_RECORD

Status: HOLD_OPERATOR_IMPLEMENTATION_AUTHORITY

docType: baseline

Date: 2026-08-05

Batch ID: GLP-T2

dispatchBaseHead: `2e540b429`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: bounded governance-template and hermetic-test implementation worker

## Purpose

Define the exact R2 implementation boundary for the public-safe, same-scope
governance-continuity carrier accepted by GLP-T1. This baseline authorizes
packet review only until the operator explicitly releases implementation.

## Source / Predecessor Evidence

- accepted design audit:
  `docs/audits/CVF_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_2026-08-05.md`;
- accepted worker return and reviewer closure:
  `docs/reviews/CVF_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_WORKER_RETURN_2026-08-05.md`;
- accepted material commit: `87febcba9`;
- current packet-authoring anchor: `2e540b429`.

## Baseline Decision

Decision: `HOLD_OPERATOR_IMPLEMENTATION_AUTHORITY`.

The technical design is source-backed and bounded, but packet authoring does
not itself release the R2 implementation worker.

## Authorization / Dependency Gate

| Dependency | Evidence | Disposition |
|---|---|---|
| GLP-T1 carrier decision | `docs/reviews/CVF_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_WORKER_RETURN_2026-08-05.md`; material commit `87febcba9`; decision `CARRIER_DESIGN_ACCEPTED` | ACCEPT |
| canonical carrier | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | ACCEPT |
| focused test owner | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | ACCEPT |
| implementation authority | current next-move surfaces release packet authoring only | HOLD_OPERATOR_IMPLEMENTATION_AUTHORITY |

This baseline must not be changed to a ready or dispatched status until the
operator explicitly releases GLP-T2 implementation and the pre-dispatch gate
passes on the released packet range.

## Scope / Target / Owner Boundary

Allowed implementation paths after release:

- `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
- `scripts/test_cvf_golden_downstream_bootstrap.ps1`
- `docs/reviews/CVF_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_WORKER_RETURN_2026-08-05.md`

The template receives one compact public-safe subsection adjacent to its
existing Risk Classification section. The golden harness receives focused
assertions only. The worker owns neither closure nor commit.

Forbidden paths and actions:

- `scripts/new-cvf-workspace.ps1` and every bootstrap/runtime helper;
- catalog, profile, manifest, policy, checker, hook, session, handoff, public-
  sync clone, downstream project, provider, network, credential, deployment,
  or release surface;
- incident chronology, operator identity, session or invocation identifiers,
  exact historic quota/token/time numbers, raw dissent, or private-only paths
  in the public-safe carrier;
- widening scope when an existing byte-preservation or merge-path assertion
  fails. Such a result is `BLOCKED_WITH_REASON`, not bootstrap-edit authority.

## Risk Classification

Risk: R2.

Reason: the source edit is static and small, but the template is projected to
new and refreshed downstream projects and is listed in the public projection
surface. Independent review is mandatory; no live/provider proof is required
because this tranche asserts deterministic local projection only.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GLP-T2 --title "Workspace Governance Learning Carrier Implementation" --date 2026-08-05 --base 2e540b429 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with accepted T1 carrier, exact two-path implementation/test manifest, authority hold, public/private boundary, and hermetic proof contract |
| checkerReadAheadConfirmation | dispatch-quality, ADIF disclosure, handoff-boundary, worker-return, public-disposition, trace, dual-surface, file-size, and roadmap-freshness checkers/standards |
| docOnlyNewFields | carrierSection; publicSafeSemantics; privateEvidenceSentinels; hermeticProofMatrix |
| claimBoundary | dispatch baseline only; no template, test, bootstrap, workspace, project, public-sync, provider, network, or runtime mutation |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| accepted T2 implementation has one carrier and one test owner | VALUE_SET | `docs/audits/CVF_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_2026-08-05.md` | R1-Corrected Design Schema; T2AllowedPaths | `T2AllowedPaths` | GLP-T1 carrier design | ACCEPT |
| downstream template owns project risk guidance | EXISTS | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | Risk Classification | `Risk Classification` | downstream AGENTS template | ACCEPT |
| bootstrap consumes the downstream template | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | CP1 lines 342-388 | `agentsTemplatePath`; `downstreamAgentsPath` | CP1 downstream AGENTS generation | ACCEPT |
| CVF-generated projects refresh in place | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | lines 362-369 | `isCvfGeneratedAgents` | CP1 refresh branch | ACCEPT |
| hand-edited projects receive a merge block | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | lines 372-383 | `CVF_MERGE_BLOCK_START` | CP1 merge branch | ACCEPT |
| golden harness uses a hermetic local core clone | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | setup lines 45-58 | `New-CvfHermeticCoreClone` | golden downstream bootstrap harness | ACCEPT |
| golden harness already exercises a second bootstrap | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | AC-06 lines 117-122 | `secondBootstrap` | golden downstream bootstrap harness | ACCEPT |
| golden harness already owns legacy/mixed fixtures | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | BSL-R1 lines 292-318 | `sentinelProject` | golden downstream bootstrap harness | ACCEPT |
| both implementation paths are public projection inputs | VALUE_SET | `scripts/cvf-public-sync.ps1` | projection allowlist lines 90 and 134 | `test_cvf_golden_downstream_bootstrap.ps1`; `CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | public-sync projection allowlist | ACCEPT |
| same-scope continuity remediation has five canonical controls | VALUE_SET | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md` | Same-scope authority continuity | `Same-scope authority continuity` | ADIF-0026 remediation | ACCEPT |

No runtime field, symbol, or source path is inferred from provider memory or
chat history. Proposed carrier prose and test assertion names are doc-only new
items and are not represented as existing source facts.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | this packet specifies static template and hermetic test work; it makes no provider, live, production, or runtime-enforcement claim |
| requiredFutureAction | any future live-governance claim requires a separate source-verified packet and mandatory real-provider proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance template implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "governance template implementation" --role worker --lifecycle-phase pre-implementation --json`

## Public-Safe Carrier Contract

The new subsection must express exactly these provider-neutral semantics:

1. same-scope authority continues while objective, allowed path/artifact
   class, risk ceiling, external-effect class, and commit owner remain stable;
2. escalation is required only for a real boundary change, destructive or
   public action, secrets/quota, live/provider use, changed commit authority,
   or an explicit operator-set budget;
3. reviewer findings are consolidated across the complete record/field/edge
   matrix before the first repair;
4. round three without an independent new root cause returns
   `REVIEW_COST_ESCALATION_REQUIRED` instead of continuing micro-repairs;
5. repeated confirmation without a boundary change is avoidable operator wait,
   not governance safety.

The carrier must not include the private evidentiary examples that motivated
the rule.

## Hermetic Proof Matrix

| Proof | Required evidence | Stop condition |
|---|---|---|
| fresh project delivery | first bootstrap generates `AGENTS.md` with one subsection and all five semantics | missing or duplicated carrier |
| generated-project refresh | existing AC-06 second bootstrap retains exactly one subsection and all five semantics | duplication, omission, or tracked drift |
| hand-edited project delivery | legacy fixture receives exactly one merge block containing the carrier | missing/duplicate block or carrier |
| byte preservation | bytes outside the inserted merge block equal the pre-bootstrap hand-edited fixture bytes | any unrelated byte change; do not edit bootstrap |
| private leakage negative | template and generated project files exclude exact private sentinels and private path fragments | any forbidden evidence appears |
| changed-set boundary | only the two implementation paths plus worker return are modified | any additional path needed or changed |

## Evidence / Verification

Before release, the paired packet must pass dispatch-quality, ADIF disclosure,
handoff-boundary, structural, file-size, and pre-dispatch autorun checks. After
release, the worker must run the exact hermetic proof and pending-return gates
named by the work order; the reviewer independently verifies semantics before
any commit.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | generated/refreshed downstream project `AGENTS.md` | static public-safe guidance only; no action or commit authority | CP1 source plus golden harness | internal bootstrap projection only | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP carrier is changed by GLP-T2 | no ingress, auth, receipt, raw-data, mutation, or runtime claim | exact two-path manifest | external adapter is outside scope | `DEFERRED_WITH_REASON` |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Source Verification dispositions; ADIF resolver query; no-commit contract; exact trace labels; dual-agent dispositions; public-export tokens; active Markdown and test-code thresholds |
| gateRunPurpose | confirm packet shape before dispatch review, not discover implementation requirements during worker execution |
| claimBoundary | local baseline structure and source fidelity only |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the accepted template-only carrier will project
cleanly through all three existing bootstrap branches without private leakage.

Evidence Comparison Requirement: the worker compares fresh, refreshed, and
hand-edited project results against that prediction.

Contradiction Handling Requirement: any missing delivery, duplication, private
leakage, or byte-preservation failure must be recorded and returned without
editing the bootstrap path.

Claim Update Requirement: the worker reports the prediction as confirmed,
narrowed, or blocked; gate success alone is not semantic proof.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local private provenance repository |
| Session or invocation | GLP-T2 packet authoring, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification, scaffold helper, ADIF resolver, apply_patch, dispatch gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | accepted GLP roadmap; T1 material commit `87febcba9`; next-move surfaces at `2e540b429` |
| Before status evidence | HEAD `2e540b429`; clean worktree |
| After status evidence | paired packet remains held for operator implementation authority |
| Diff evidence | `git diff --name-status` limited to paired packet paths |
| Approval boundary | packet authoring only |
| Claim boundary | no implementation, external effect, public sync, provider/network use, push, or deployment |
| Agent type | dispatcher |
| Invocation ID | `glp-t2-packet-authoring-2026-08-05` |
| Expected manifest | this baseline; paired work order |
| Actual changed set | this baseline; paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | packet definition for static template and hermetic test work |
| claimDisposition | N/A with reason: no implementation or runtime execution in this baseline |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | N/A with reason: no implementation action is executed |
| invocationBoundary | local documentation and source-verification only |
| interceptionBoundary | no shell, IDE, filesystem, provider, or agent-runtime interception claim |
| claimLanguage | bounded future implementation contract, not implemented behavior |
| forbiddenExpansion | no bootstrap, runtime, provider/live, CLI/MCP, public-sync, push, or deployment expansion |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: both designed implementation paths are public projection inputs, but
this private provenance packet neither edits them nor authorizes public sync.

## Claim Boundary

This baseline establishes a source-verified, held GLP-T2 implementation
contract. It does not release the worker, implement the carrier, mutate a
workspace/project, prove propagation, publish, call a provider, use the
network, push, or deploy.
