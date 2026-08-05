# CVF GC-018 Baseline - GLP T2R1 CP1 Byte-Preserving Merge Repair

Memory class: FULL_RECORD

Status: HOLD_OPERATOR_IMPLEMENTATION_AUTHORITY

docType: baseline

Date: 2026-08-05

Batch ID: GLP-T2R1

dispatchBaseHead: `7cdc72393`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: bounded CP1 merge-repair implementation worker

## Purpose

Define the exact R2 repair boundary after GLP-T2 proved that CP1 rewrites the
complete hand-edited `AGENTS.md` and cannot preserve outside-block bytes. This
baseline authorizes packet review only until the operator explicitly releases
implementation.

## Source / Predecessor Evidence

- blocked GLP-T2 completion review:
  `docs/reviews/CVF_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_COMPLETION_2026-08-05.md`;
- blocked worker evidence:
  `docs/reviews/CVF_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_WORKER_RETURN_2026-08-05.md`;
- blocked material commit: `071866e7b`;
- current packet-authoring anchor: `7cdc72393`.

## Baseline Decision

Decision: `HOLD_GLP_T2R1_OPERATOR_IMPLEMENTATION_AUTHORITY`.

The repair candidate is source-backed and bounded. No implementation is
released until the operator explicitly confirms this new bootstrap scope.

## Authorization / Dependency Gate

| Dependency | Evidence | Disposition |
|---|---|---|
| GLP-T2 blocked review | `docs/reviews/CVF_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_COMPLETION_2026-08-05.md`; material commit `071866e7b`; decision `BLOCKED_IMPLEMENTATION_EVIDENCE` | ACCEPT |
| canonical carrier | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | ACCEPT |
| focused test owner | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | ACCEPT |
| CP1 repair owner | `scripts/new-cvf-workspace.ps1` lines 342-388 | ACCEPT |
| implementation authority | no operator confirmation for expanded bootstrap scope | REQUIRED |

Packet authoring is released by current continuity. Worker dispatch remains
held until the authority row becomes `ACCEPT`, the base is refreshed, and the
full pre-dispatch gate passes on that release range.

## Scope / Target / Owner Boundary

Allowed implementation paths only after explicit release:

- `scripts/new-cvf-workspace.ps1`
- `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
- `scripts/test_cvf_golden_downstream_bootstrap.ps1`
- `docs/reviews/CVF_GLP_T2R1_CP1_BYTE_PRESERVING_MERGE_REPAIR_WORKER_RETURN_2026-08-05.md`

CP1 receives one bounded byte-preserving merge helper/branch repair. The
template receives the previously accepted compact carrier, and the existing
golden harness receives the focused fresh/refresh/hand-edited assertions. The
worker owns neither closure nor commit.

Forbidden paths and actions:

- every bootstrap/helper path other than `scripts/new-cvf-workspace.ps1`;
- catalog, profile, manifest, policy, checker, hook, session, handoff, public-
  sync clone, downstream project, provider, network, credential, deployment,
  or release surface;
- incident chronology, operator identity, session or invocation identifiers,
  exact historic quota/token/time numbers, raw dissent, or private-only paths
  in the public-safe carrier;
- encoding conversion of preserved outside bytes, broad bootstrap refactor, or
  unrelated newline normalization.

## Risk Classification

Risk: R2.

Reason: CP1 mutates downstream project guidance and the affected source/test
paths are public projection inputs. The repair is local and deterministic but
must preserve arbitrary pre-existing bytes and remain independently reviewed.
No live/provider proof is required.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GLP-T2R1 --title "CP1 Byte-Preserving Merge Repair" --date 2026-08-05 --base 7cdc72393 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | adapted the accepted GLP-T2 packet to the source-proven CP1 contradiction, exact three-source implementation manifest, authority hold, byte contract, and hermetic proof contract |
| checkerReadAheadConfirmation | dispatch-quality, ADIF disclosure, handoff-boundary, worker-return, public-disposition, trace, dual-surface, file-size, and roadmap-freshness checkers/standards |
| docOnlyNewFields | bytePreservingMergeContract; carrierSection; privateEvidenceSentinels; hermeticProofMatrix |
| claimBoundary | held dispatch baseline only; no template, test, bootstrap, workspace, project, public-sync, provider, network, or runtime mutation |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| GLP-T2 is blocked by outside-block byte drift | VALUE_SET | `docs/reviews/CVF_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_COMPLETION_2026-08-05.md` | Findings / Position | `BLOCKED_IMPLEMENTATION_EVIDENCE` | GLP-T2 completion review | ACCEPT |
| downstream template owns project risk guidance | EXISTS | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | Risk Classification | `Risk Classification` | downstream AGENTS template | ACCEPT |
| bootstrap consumes the downstream template | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | CP1 lines 342-388 | `agentsTemplatePath`; `downstreamAgentsPath` | CP1 downstream AGENTS generation | ACCEPT |
| CVF-generated projects refresh in place | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | lines 362-369 | `isCvfGeneratedAgents` | CP1 refresh branch | ACCEPT |
| hand-edited projects receive a merge block | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | lines 372-383 | `CVF_MERGE_BLOCK_START` | CP1 merge branch | ACCEPT |
| current hand-edited branch reads text and rewrites the whole file | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | lines 355-382 | `existingContent`; `Set-Content` | CP1 merge branch | ACCEPT |
| golden harness uses a hermetic local core clone | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | setup lines 45-58 | `New-CvfHermeticCoreClone` | golden downstream bootstrap harness | ACCEPT |
| golden harness already exercises a second bootstrap | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | AC-06 lines 117-122 | `secondBootstrap` | golden downstream bootstrap harness | ACCEPT |
| golden harness already owns legacy/mixed fixtures | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | BSL-R1 lines 292-318 | `sentinelProject` | golden downstream bootstrap harness | ACCEPT |
| all three source/test paths are public projection inputs | VALUE_SET | `scripts/cvf-public-sync.ps1` | projection allowlist | `new-cvf-workspace.ps1`; `test_cvf_golden_downstream_bootstrap.ps1`; `CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | public-sync projection allowlist | ACCEPT |
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

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --surface-selector scripts/new-cvf-workspace.ps1 --risk-ceiling MEDIUM --max-results 20 --json`

## Byte-Preserving Merge Contract

- Existing bytes outside any prior CVF merge block remain byte-for-byte
  identical after first insertion and refresh.
- Marker discovery may inspect decoded text, but preserved prefix/suffix bytes
  must be carried from the original byte array rather than reserialized.
- Exactly one current CVF merge block is emitted at the top.
- A prior CVF merge block is replaced without accumulating blank lines or
  changing the project-owned suffix.
- Unsupported or ambiguous marker structure fails closed without rewriting the
  file.

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
| byte preservation | original outside-block bytes remain identical after first insertion and second refresh | any unrelated byte change |
| malformed markers | duplicate, reversed, or unterminated markers fail closed without file mutation | any rewrite or success claim |
| private leakage negative | template and generated project files exclude exact private sentinels and private path fragments | any forbidden evidence appears |
| changed-set boundary | only the three source/test paths plus worker return are modified | any additional path needed or changed |

## Evidence / Verification

Before release, the paired packet must pass dispatch-quality, ADIF disclosure,
handoff-boundary, structural, file-size, and pre-dispatch autorun checks. After
release, the worker must run the exact hermetic proof and pending-return gates
named by the work order; the reviewer independently verifies semantics before
any commit.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | generated/refreshed downstream project `AGENTS.md` | static public-safe guidance only; no action or commit authority | CP1 source plus golden harness | internal bootstrap projection only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP carrier is changed by GLP-T2R1 | no ingress, auth, receipt, raw-data, mutation, or runtime claim | exact three-source manifest | external adapter is outside scope | `DEFERRED_WITH_REASON` |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Source Verification dispositions; ADIF resolver query; no-commit contract; exact trace labels; dual-agent dispositions; public-export tokens; active Markdown and test-code thresholds |
| gateRunPurpose | confirm packet shape before dispatch review, not discover implementation requirements during worker execution |
| claimBoundary | local baseline structure and source fidelity only |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a byte-oriented CP1 merge repair will project the
accepted carrier through all branches while preserving project-owned bytes.

Evidence Comparison Requirement: the worker compares fresh, refreshed, and
hand-edited project results against that prediction.

Contradiction Handling Requirement: any missing delivery, duplication, private
leakage, malformed-marker mutation, or byte-preservation failure stops the
worker without widening beyond the three source/test paths.

Claim Update Requirement: the worker reports the prediction as confirmed,
narrowed, or blocked; gate success alone is not semantic proof.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local private provenance repository |
| Session or invocation | GLP-T2R1 repair packet authoring, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification, scaffold helper, ADIF resolver, apply_patch, dispatch gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | GLP roadmap plus blocked T2 review at `071866e7b`; current continuity authorizes documentation-only repair packet authoring |
| Before status evidence | HEAD `7cdc72393`; clean worktree |
| After status evidence | paired packet remains held for operator implementation authority |
| Diff evidence | `git diff --name-status` limited to paired packet paths |
| Approval boundary | packet authoring only; no GLP-T2R1 implementation dispatch |
| Claim boundary | no implementation, external effect, public sync, provider/network use, push, or deployment |
| Agent type | dispatcher |
| Invocation ID | `glp-t2r1-repair-packet-authoring-2026-08-05` |
| Expected manifest | this baseline; paired work order |
| Actual changed set | this baseline; paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | held packet definition for CP1 byte-preserving merge repair, carrier, and hermetic proof |
| claimDisposition | N/A with reason: no implementation or runtime execution in this baseline |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | N/A with reason: no implementation action is executed |
| invocationBoundary | local documentation and source-verification only |
| interceptionBoundary | no shell, IDE, filesystem, provider, or agent-runtime interception claim |
| claimLanguage | bounded future implementation contract, not implemented behavior |
| forbiddenExpansion | no other bootstrap/helper, runtime, provider/live, CLI/MCP, public-sync, push, or deployment expansion |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: all designed source/test paths are public projection inputs, but
this private provenance packet neither edits them nor authorizes public sync.

## Claim Boundary

This baseline establishes one held, source-verified GLP-T2R1 repair contract.
It does not release or implement the repair, mutate a workspace/project, prove
propagation, publish, call a provider, use the network, push, or deploy.
