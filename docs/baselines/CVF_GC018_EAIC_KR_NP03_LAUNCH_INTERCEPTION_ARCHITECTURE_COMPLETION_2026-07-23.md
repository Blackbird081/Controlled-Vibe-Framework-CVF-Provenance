# CVF GC-018 EAIC-KR NP-03 Launch Interception Architecture Completion

Memory class: FULL_RECORD

Status: DISPATCH_READY_DOCUMENTATION_ONLY

docType: baseline

Date: 2026-07-23

dispatchBaseHead: `ee4fbe0a2`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one bounded documentation-only decision packet that resolves whether
NP-03 can receive a source-backed owner, covered launch surfaces, platform
boundary, smallest build slice, and deterministic proof seam without claiming
universal host control or interfering with internal agent autonomy.

This baseline does not authorize T5, implementation, process observation,
provider use, CLI/MCP invocation, live proof, public-sync, or moratorium lift.

## Authorization / Decision

The operator instructed the reviewer/dispatcher to continue completing the
parked next move after EAIC-KR-T4 closure. That instruction releases only the
documentation-only NP-03 architecture-completion packet described here.

The worker may select one bounded pattern, compose compatible patterns, or
return `NO_VIABLE_BOUNDED_PATTERN`. A decision is acceptable only when its
claim is no broader than the launch surfaces and evidence it names.

## Audit Finding

T4 closed both readiness axes as `NOT_READY`. NP-03 remained `MISSING` because
no current or planned component detects a launch that bypasses the proposed
EAIC coordinator. A coordinator admission function alone cannot observe an
out-of-band shell, IDE, script, MCP host, or other process path that never calls
it.

CVF must not solve this gap by claiming hidden universal interception,
governing provider-native helpers inside an already-authorized parent session,
or expanding into host-wide surveillance without explicit operator authority.

## Scope / Methodology

The worker must:

1. re-read the T3 threat row, T4 NP-03 row, T4 completion review, T1
   OS/process evidence, and current bounded launcher sources;
2. inspect current repository source for any newly relevant launch,
   observation, receipt-admission, quarantine, broker, wrapper, IDE, shell,
   process-tree, or result-acceptance owner;
3. compare at least these bounded pattern families:
   - mandatory governed launch path or wrapper;
   - host-controlled broker, sandbox, or process containment boundary;
   - OS observation followed by reject or quarantine;
   - surface-specific IDE, shell, or MCP integration;
   - governed-result admission that quarantines outcomes lacking a correlated
     launch receipt;
   - composed pattern, if required;
4. distinguish prevention, detection, post-launch observation, result
   quarantine, and universal interception;
5. name the accountable CVF owner and smallest build slice only if source and
   boundary evidence support them;
6. define an NP-03 fixture that can deterministically pass or fail without a
   provider call or uncontrolled host action;
7. decide whether NP-03 architecture completion is `READY_FOR_T5_AUTHORING`,
   `PARTIAL_NOT_READY`, or `NO_VIABLE_BOUNDED_PATTERN`.

## Non-Goals

- no runtime, source, test, checker, hook, package, UI, schema, registry,
  roadmap, session, or handoff implementation;
- no process launch, enumeration, monitoring, interception, termination, or
  containment;
- no agent invocation through CLI/MCP;
- no provider, API, account, credential, network, browser, or quota use;
- no provider/model selection or hard-coding;
- no universal OS, IDE, shell, filesystem, or user-process control claim;
- no per-helper governance inside the parent agent session;
- no T5 roadmap authoring or implementation release;
- no public-sync, push, deploy, or production claim.

## Required Decision Dimensions

| Dimension | Required output |
| --- | --- |
| accountable owner | current or proposed CVF owner with source-backed responsibility boundary |
| covered launch surfaces | explicit allowlist of paths the pattern can observe or mediate |
| excluded launch surfaces | explicit paths it cannot observe or mediate |
| platform boundary | Windows, POSIX, IDE, shell, MCP host, or result-admission limitations |
| prevention capability | exact pre-launch denial capability or `NONE` |
| detection capability | exact observable bypass signal or `NONE` |
| quarantine capability | exact result/receipt admission boundary or `NONE` |
| smallest build slice | one bounded source/test slice, or `NOT_DESIGNABLE` |
| deterministic proof seam | fixture inputs, expected evidence, pass condition, fail condition |
| internal-helper non-interference | proof that parent-session helpers remain outside NP-03 |
| residual bypass | what remains possible after the proposed slice |
| final readiness | one canonical verdict with rationale |

## Decision Safety Rule

`READY_FOR_T5_AUTHORING` is allowed only if every mandatory dimension has a
source-backed value and the deterministic proof can fail when the bypass is
not detected or quarantined. A wrapper-only design that sees only cooperative
launches cannot claim out-of-band detection. A receipt quarantine design may
claim rejection of uncorrelated results, but it must not claim that it prevented
or terminated the underlying process.

If no bounded design can satisfy NP-03 without host-wide control or unsupported
assumptions, the correct result is `NO_VIABLE_BOUNDED_PATTERN`.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | parent agent session and provider-native internal helpers | helpers inherit the parent assignment and are not separately intercepted or charged | roadmap autonomy perimeter; T4 NP-09 | no per-helper adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | proposed EAIC coordinator plus the NP-03 pattern to be decided | documentation analysis only; no actual launch, adapter call, process control, or receipt admission | T3 THREAT-04; T4 NP-03; current launcher sources | future adapter remains unbuilt and must stay explicitly bounded | `DEFERRED_WITH_REASON` |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| T3 architecture direction accepted | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_DECISION_PACKET.md`; material commit `97a805b5b` | ACCEPT |
| T4 readiness review closed | `docs/reviews/CVF_EAIC_KR_T4_BUILD_READINESS_AND_NEGATIVE_PROOF_COMPLETION_REVIEW_2026-07-23.md`; material commit `5a598bef6` | ACCEPT |
| NP-03 isolated as only pre-T5 architecture reopen | same T4 completion review, Decision / Disposition | ACCEPT |
| operator releases documentation-only completion | operator instruction on 2026-07-23: continue completing the recorded next move | ACCEPT |
| T5 or implementation release | no release exists | N/A with reason: explicitly outside this packet |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 50 --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039,
ADIF-0043, ADIF-0049, ADIF-0006.

Applied controls: source-backed per-pattern findings, no provider-local
authority, no aggregate readiness beyond mandatory dimensions, create-only
ownership, no-commit reviewer conversion, verified command signatures, and
explicit external-action boundaries.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| NP-03 requires bypass detection plus rejection or quarantine | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_DECISION_PACKET.md` | Negative-Proof Plan; NP-03 | `NP-03` | T3 threat model | VALUE_SET | ACCEPT |
| current launch-bypass owner is absent | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_DECISION_PACKET.md` | Threat Model; THREAT-04 | `OWNER_SURFACE_NOT_FOUND` | T3 threat model | VALUE_SET | ACCEPT |
| T4 requires owner, surfaces, platform boundary, slice, and seam before T5 | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T4_BUILD_READINESS_AND_NEGATIVE_PROOF_DECISION_PACKET.md` | Pre-T5 Architecture Completion Requirement | `NP-03` | T4 decision packet | VALUE_SET | ACCEPT |
| both T4 readiness axes are not ready | `docs/reviews/CVF_EAIC_KR_T4_BUILD_READINESS_AND_NEGATIVE_PROOF_COMPLETION_REVIEW_2026-07-23.md` | Decision / Disposition | `t5RoadmapAuthoringReadiness` | T4 completion review | VALUE_SET | ACCEPT |
| governed command launcher starts only registered profile commands behind preflight and receipt consumption | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | `GovernedCommandProfile`; `DirectGovernedCommandRunner`; `launchGovernedCommand` | `launchGovernedCommand` | governed command launcher | RUNTIME_BEHAVIOR | ACCEPT |
| MAO operational launcher composes a local adapter and explicitly makes no real process/provider/network call | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | module boundary; `MaoOperationalWorkerLauncher` | `MaoOperationalWorkerLauncher` | execution-plane MAO launcher | LITERAL_INVARIANT | ACCEPT |
| Windows Job Objects and POSIX process groups are evidence candidates, not existing CVF bindings | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md` | Value Conversion Matrix; Cross-Source Reconciliation | `RUNTIME_CANDIDATE` | T1 intake ledger | VALUE_SET | ACCEPT |
| aggregate decision cannot exceed per-item authority evidence | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0028.md` | Purpose; Remediation | `ADIF-0028` | ADIF registry | LITERAL_INVARIANT | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; Roadmap-To-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Dual Agent Surface Matrix; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | confirm the authored packet against already-read requirements and record evidence, not discover structure for the first time |
| claimBoundary | read-ahead proves structural preparation only, not NP-03 readiness or runtime capability |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAIC-KR-NP03 --title "EAIC-KR NP-03 Launch Interception Architecture Completion" --date 2026-07-23 --base ee4fbe0a2 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic no-commit documentation and evidence decision |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | direct canonical-template authoring was used because task-specific source verification and strict two-output ownership were required; completed NP-03 authority, decision dimensions, dual-agent boundary, evidence, and acceptance controls |
| checkerReadAheadConfirmation | dispatch, handoff, structural, worker-return, epistemic, Delta-boundary, and file-size checker sources reviewed |
| docOnlyNewFields | NP-03 pattern, surface, platform, build-slice, proof-seam, residual-bypass, and readiness fields |
| claimBoundary | dispatch-authoring provenance only; no implementation or runtime proof |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a universal interception claim will remain
unsupported; a bounded mediated-launch plus result-quarantine pattern may be
designable, but must be tested against NP-03 wording.

Evidence Comparison Requirement: compare every candidate against current
source, excluded surfaces, and the deterministic proof requirement.

Contradiction Handling Requirement: contradictory evidence requires a
Contradiction Or Gap Disposition and narrowed final verdict.

Claim Update Requirement: record whether NP-03 became architecture-complete,
remained partial, or has no viable bounded pattern.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private architecture decision with no implementation, public artifact,
or public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | documentation-only NP-03 architecture comparison |
| claimDisposition | N/A with reason: no execution behavior is implemented |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | N/A with reason: no external action is performed |
| invocationBoundary | local repository reads and two create-only documentation outputs |
| interceptionBoundary | no IDE, shell, Git, filesystem, provider, process, or user activity interception |
| claimLanguage | architecture decision and proof design only |
| forbiddenExpansion | no T5, runtime, live proof, CLI/MCP invocation, provider use, public-sync, or moratorium lift |

## Acceptance Criteria

- one owner/surface/platform/slice/seam decision for NP-03;
- at least five bounded pattern families compared;
- prevention, detection, and quarantine claims separated;
- excluded surfaces and residual bypass stated;
- internal helpers explicitly preserved outside the governed perimeter;
- final verdict is one canonical value;
- exactly two worker-owned outputs, unstaged and uncommitted;
- worker-return fast gate passes.

## Evidence / Verification

Required evidence includes executionBaseHead, initial and final Git status,
exact current-source citations, bounded negative-search results, the complete
pattern/surface/platform matrices, the deterministic NP-03 proof-seam design,
an empty staged diff, the exact two-path pending manifest, worker-return
fast-gate PASS, and governed-file-size PASS.

The worker must not substitute live execution, process observation, provider
use, or an external call for repository-local architecture evidence.

## Claim Boundary

This baseline authorizes a repository-local architecture decision only. It does
not establish that CVF can observe arbitrary launches, control a host, prevent
processes, intercept an IDE or shell, or safely invoke another agent. Any future
build or proof requires a new operator-approved roadmap and work order.
