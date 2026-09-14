# CVF GC-018 Baseline - Known-Value Launcher Output Redaction
Memory class: governed-dispatch-baseline
docType: baseline
Status: APPROVED_FOR_EXECUTION
Date: 2026-09-14
Batch ID: OUTPUT-REDACTION-T1
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: bdd8329aa7d9d61d7fb8cc98de6def13e6697647

## Purpose

Add known-value output masking at the existing governed-command launcher response boundary, complementing existing credential-shape redaction. Reuse R3 M9 as a pattern reference; implement CVF-native code without copying upstream source. The opt-in dependency is usable by trusted in-process callers. The default CLI does not yet supply known secrets: do not claim automatic protection for its inherited environment, deployment or universal secret safety.

## Decision / Baseline

Execution requires pre-dispatch PASS and matching continuity. Paired work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_OUTPUT-REDACTION-T1_2026-09-14.md`; exact six-path scope and trust/input/latency boundaries are binding.

## Scope / Target / Owner Boundary

Six paths in paired work order; all other pending Local work remains read-only. Local owns review and closure. No upstream execution or ambient secrets.

## Source Verification Block

| Fact | Source file | Verified section | Disposition |
| --- | --- | --- | --- |
| Reference pattern | docs/audits/CVF_QM_RUNTIME_VALUE_R3_2026-09-14.json | M9, source pin 59cf6554faadcd06494782190c3ecae1829dd381; digest da72f5c9879d24e9977e34b08da141c838de431c86e3b6d5b8057e376490765d | ACCEPT |
| Selected consumer | EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts | dependencies 175-184; runner and output 484-562 | ACCEPT |
| CLI caller | EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts | runGovernedExecCli 61-90 | ACCEPT |
| Existing shape matcher | EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts | SECRET_TEXT_PATTERNS 45-57; redactText 169-176 | ACCEPT |
| Existing consumer test | EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts | 446-464 shape-redaction case | ACCEPT |
| Local selection | docs/reviews/CVF_QM_RUNTIME_VALUE_R4_COMPLETION_2026-09-14.md | Proportional Method Trial | ACCEPT |

## Acceptance Criteria

All acceptance rows pass with measured latency within ceilings. No self-acceptance; return pending Local review. Package/runtime activation remains separate.

## Evidence / Verification

Source references, actual test names and results, exact six-path delta, benchmark recipe/results, no secret output, disclosed historical failures. Source evidence reuse does not certify new runtime behavior.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | governance/compat/check_worker_return_quality_gate.py; governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_gate_to_role_closeability.py |
| literalTokensReviewed | diagnose, run, REQUIRED_HEADINGS, changed-path collection, protected path ownership and INITIAL convergence |
| gateRunPurpose | Confirm dispatch structure and closeability |
| claimBoundary | No implementation or semantic evidence acceptance yet |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class runtime-hardening --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json`. Returned defects: NONE_RETURNED; items=[], totalCandidates=0, truncated=false.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local dispatcher |
| Provider or surface | internal workspace |
| Session or invocation | OUTPUT-REDACTION-T1-dispatch |
| Working directory | repository root |
| Command or tool surface | bounded source reads, packet authoring, existing pre-dispatch gate |
| Target paths | docs/work_orders/CVF_AGENT_WORK_ORDER_OUTPUT-REDACTION-T1_2026-09-14.md; docs/baselines/CVF_GC018_OUTPUT-REDACTION-T1_2026-09-14.md; CVF_SESSION_MEMORY.md; AGENT_HANDOFF_V60_2026-09-08.md; CVF_SESSION/state/entries/nextAllowedMove.json; CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json; CVF_SESSION/ACTIVE_SESSION_STATE.json; CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json; docs/reviews/CVF_QM_RUNTIME_VALUE_R4_COMPLETION_2026-09-14.md |
| Allowed scope source | operator approved bounded M9 packet |
| Before status evidence | HEAD bdd8329aa; NOT a clean worktree: fourteen prior Local/startup/R4 paths retained under EXPLICIT_LANE_HANDOFF; worker delta is isolated by exact ownership, not by a clean checkout |
| After status evidence | two new dispatch documents plus authorized continuity projection; worker code not edited |
| Diff evidence | git status --short; git diff --name-status |
| Approval boundary | exact six worker paths after pre-dispatch PASS; no ambient credentials |
| Claim boundary | dispatch only, no implementation result |
| Agent type | dispatcher |
| Invocation ID | OUTPUT-REDACTION-T1-dispatch |
| Expected manifest | docs/work_orders/CVF_AGENT_WORK_ORDER_OUTPUT-REDACTION-T1_2026-09-14.md; docs/baselines/CVF_GC018_OUTPUT-REDACTION-T1_2026-09-14.md; CVF_SESSION_MEMORY.md; AGENT_HANDOFF_V60_2026-09-08.md; CVF_SESSION/state/entries/nextAllowedMove.json; CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json; CVF_SESSION/ACTIVE_SESSION_STATE.json; CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json; docs/reviews/CVF_QM_RUNTIME_VALUE_R4_COMPLETION_2026-09-14.md |
| Actual changed set | docs/work_orders/CVF_AGENT_WORK_ORDER_OUTPUT-REDACTION-T1_2026-09-14.md; docs/baselines/CVF_GC018_OUTPUT-REDACTION-T1_2026-09-14.md; CVF_SESSION_MEMORY.md; AGENT_HANDOFF_V60_2026-09-08.md; CVF_SESSION/state/entries/nextAllowedMove.json; CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json; CVF_SESSION/ACTIVE_SESSION_STATE.json; CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json; docs/reviews/CVF_QM_RUNTIME_VALUE_R4_COMPLETION_2026-09-14.md |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

Optional trusted-caller known-value masking support at the existing launcher response seam only. No automatic CLI coverage, arbitrary encodings/fragments, live/provider guarantee, upstream source execution, new credential source, publication or three-repo closure.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order with no public artifact or sync scope.

## Dispatch Validation History

First pre-dispatch run rejected incomplete shared-worktree path accounting, missing ADIF query label, ambiguous clean-worktree wording and a closed-review reference to the future packet. Local repaired these declarations; no worker or implementation has run. Prior source decisions unchanged.

Second pre-dispatch run passed 81/82 checks; the remaining failure required the exact ADIF label Returned defects rather than Actual result. The recorded empty resolver result was unchanged; the label is now corrected.
