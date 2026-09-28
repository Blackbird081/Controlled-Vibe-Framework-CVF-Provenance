# CVF GC-018 Baseline - RSE-T4 Tool Classifier Block Recovery Enforcement

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-09-28

Batch ID: RSE-T4-H1

Dispatch base head: `91a98b2d8`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local orchestrator/reviewer under operator instruction to park NCR and harden the CVF foundation.

Reviewer owner: Local orchestrator/reviewer.

Worker target: one shared-workspace `INTERNAL_AGENT` worker.

## Purpose

Authorize one bounded governance-hardening tranche for ADIF-0061. The tranche
adds an RSE tool/classifier-block recovery contract, projects it through the
work-order and worker-return scaffolds, and enforces it through two existing
gates with focused hostile tests.

## Scope

Documentation and local deterministic governance tooling only. No NCR package,
runtime/provider/live, external UI control, safety-classifier bypass, public
sync, deployment, queue, daemon, watcher or direct interception is authorized.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id RSE-T4-H1 --title "Tool Classifier Block Recovery Enforcement" --date 2026-09-28 --base 91a98b2d8 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --root-cause-cluster-id NOT_APPLICABLE_INITIAL_DISPATCH --prior-finding-set-digest NOT_APPLICABLE_INITIAL_DISPATCH --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence NONE --scec-problem-key RSE-TOOL-CLASSIFIER-BLOCK-RECOVERY --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition ROOT_CONTRACT_REQUIRED --scec-successor-scope NO_SUCCESSOR --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-verified RSE-T4 authority, exact twelve-path manifest, recovery contract and deterministic proof |
| checkerReadAheadConfirmation | dispatch, worker-return, core-guard, closeability and file-size sources inspected before authoring |
| docOnlyNewFields | tool/classifier recovery and event-capture fields named in paired work order |
| claimBoundary | authoring provenance only; no runtime or external classifier behavior claim |

## Baseline Decision

`GO_RSE_T4_BOUNDED_MACHINE_HARDENING`. Existing RSE-T1/T2 rules correctly keep
routine technical decisions away from the operator, but RSE-T3 observes only
return-time jurisdiction shape. ADIF-0061 records the missing tool-level
recovery contract and earlier enforcement.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| operator questions are exceptional | `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md` | Operator Question Classification | operator-question decision table | RSE-T1 | ACCEPT |
| worker returns route findings without operator escalation | `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | Operator Action Is The Exception | worker-return jurisdiction block | RSE-T2 | ACCEPT |
| current diagnostic is return-time/read-only | `governance/compat/run_agent_automation_assist.py` | `_build_jurisdiction_readout` | return-time jurisdiction readout | RSE-T3/AAF helper | ACCEPT |
| dispatch envelope has an existing gate owner | `governance/compat/check_dispatch_prompt_envelope.py` | `validate_work_order` | dispatch work-order validation | dispatch prompt gate | ACCEPT |
| worker-return quality has an existing gate owner | `governance/compat/check_worker_return_quality_gate.py` | worker-return validation | return packet validation | worker-return quality gate | ACCEPT |
| recurring classifier escalation is unhandled | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0061.md` | Remediation | ADIF-0061 | ADIF | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| target artifacts | all new addendum/baseline/work-order/return paths returned `False` before authoring | ACCEPT_NO_COLLISION |
| exact recovery tokens | `rg -n -S "toolClassifierBlockRecovery|platformForcedPrompt|classifierBlockEventCount|Instruction Poisoning" docs governance CVF_SESSION` | only ADIF-0061/S11 learning evidence existed; no active contract owner | ACCEPT_NEW_FIELDS |
| overlap | RSE-T1/T2/T3 and ADIF-0057 inspected | compose existing authority/closeability owners; do not duplicate them |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch-ready applicability; worker-return status; protected-path authorization; exact manifest; file-size no-growth discipline |
| gateRunPurpose | source-first feasibility and literal-shape confirmation |
| claimBoundary | structural feasibility only, not proof that external UI prompts can be suppressed |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned top-ten defects: ADIF-0001, 0002, 0014, 0015, 0020, 0021, 0028,
0029, 0033 and 0044. ADIF-0061 is the explicit origin defect. Dispatch impact:
source paths are exact, external UI evidence is not authority, checker sources
were read first, protected paths are explicitly authorized, and runtime/tool
timeout behavior is not claimed.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH` |
| Returned defect count | 10 (bounded resolver result; truncated=true) |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044 |
| Disclosed defectIds | returned top ten plus origin ADIF-0061 |
| Dispatch impact | exact paths, source-first checker read-ahead, protected-path authorization and external-platform claim boundary |

## Risk / Corrective Action

The main risk is overclaiming that repository prose can suppress an external
safety dialog. The contract must distinguish worker-authored escalation from a
platform-forced prompt and require recording rather than bypass. Existing
oversized governed files may not grow beyond their current tracked size; use
replacement/extraction where the file-size guard requires it.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | RSE-T4 packet authoring, 2026-09-28 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, scaffold stdout, `apply_patch`, Git |
| Target paths | paired RSE-T4 baseline and work order |
| Allowed scope source | operator instruction and ADIF-0061 |
| Before status evidence | clean worktree at HEAD `91a98b2d8`; NCR parked |
| After status evidence | paired dispatch packet pending validation/commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet authoring and bounded local governance hardening only |
| Claim boundary | no implementation or external runtime change during authoring |
| Agent type | INTERNAL_AGENT Local orchestrator/reviewer |
| Invocation ID | `rse-t4-dispatch-author-20260928` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order only at authoring |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local RSE contract, scaffold and checker enforcement |
| claimDisposition | CLAIM_REJECTED: no direct runtime enforcement or platform interception is claimed |
| receiptEvidence | N/A with reason: deterministic governance tests only |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no external action |
| invocationBoundary | cooperating agents that consume governed packets/scaffolds |
| interceptionBoundary | no IDE, tool, filesystem, shell, provider or platform interception |
| claimLanguage | packet-shape and return-evidence enforcement only |
| forbiddenExpansion | classifier bypass, automatic external prompt handling, NCR, provider/live, public/deploy |

## Evidence / Verification

The paired work order owns the exact commands, focused fixtures, independent
probe and gate graph. Baseline admission requires the paired work order,
pre-dispatch gate and committed continuity binding; this baseline is not
implementation or external-runtime proof.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance hardening; no public-sync authority.

## Claim Boundary

This baseline authorizes an exact local documentation/checker/scaffold tranche.
It does not weaken safety controls, suppress platform UI, execute a provider,
reopen NCR, or claim prevention until independent review accepts the tests.
