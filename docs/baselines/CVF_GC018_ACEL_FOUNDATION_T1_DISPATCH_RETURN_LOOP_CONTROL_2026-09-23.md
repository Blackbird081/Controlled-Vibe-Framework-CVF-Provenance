# CVF GC-018 Baseline - ACEL Foundation T1 Dispatch Return Loop Control

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-09-23

Batch ID: ACEL-FOUNDATION-T1-DISPATCH-RETURN-LOOP-CONTROL

Dispatch base HEAD: `dc935676838b08754a6b26d0a13813128df24785`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local orchestrator/reviewer

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Authorize one bounded governance-control implementation that prevents two
repeated agent-loop causes: a dispatch packet whose artifact manifest and
worker-return binding are not validated until runtime files change, and a
worker-return gate that can report compliance after selecting zero returns.

## Target / Source

| Source | Verified owner fact | Disposition |
|---|---|---|
| `docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_LOCAL_REVIEW_2026-09-23.md` | RV01 records the conditional manifest/binding admission defect; RV05 records zero-eligible and negative-path evidence gaps | ACCEPT |
| `docs/reviews/evidence/cvf-multi-agent-control-value-retrospective-2026-09-23.json` | CONTROL-VALUE-01 through 05 bind planning cost, incomplete measurement and non-causal model claims | ACCEPT |
| `docs/reviews/CVF_MULTI_AGENT_CONTROL_VALUE_RETROSPECTIVE_LOCAL_REBUTTAL_2026-09-23.md` | Local adjudicates the cross-provider proposals and preserves owner/control boundaries | ACCEPT |
| `docs/reviews/CVF_MULTI_AGENT_CONTROL_VALUE_RETROSPECTIVE_CROSS_PROVIDER_REJOINDER_2026-09-23.md` | responder accepts the Local dispositions and corrects stale-HEAD/fail-open claims | ACCEPT_AS_CORROBORATING_INPUT |
| `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | owns fulfillment-manifest, pending-return and learning-promotion rules | ACCEPT_AS_OWNER |
| `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md` | owns eligible return structure and checker-facing authoring requirements | ACCEPT_AS_OWNER |
| `governance/compat/check_work_order_dispatch_quality_range.py` | fulfillment-manifest validation is currently gated by observed runtime/source activity | ACCEPT_AS_IMPLEMENTATION_TARGET |
| `governance/compat/check_worker_return_quality_gate.py` | zero diagnostics currently yields a compliant result | ACCEPT_AS_IMPLEMENTATION_TARGET |
| `governance/compat/run_worker_return_fast_gate.py` | active work order is forwarded to probe admission but not worker-return quality | ACCEPT_AS_IMPLEMENTATION_TARGET |

## Source / Predecessor Evidence

The accepted C1-R2 Local review is the immediate defect source. The committed
retrospective, Local rebuttal and cross-provider rejoinder are corroborating
learning evidence only. The two current standards and three checker entrypoints
remain the binding implementation owners named in the table above.

## Scope / Methodology

Role: Local dispatch author; phase: foundation control dispatch; final decision
owner: Local. The worker may modify only the declared standards, three checker
entrypoints, focused tests and worker return. The implementation must preserve
working-tree-aware pending-return checks while making active-work-order
admission fail closed.

## Findings / Position

The C1-R2 loop was not solely a worker defect. The dispatch gate had enough
information to validate the packet but deferred the relevant manifest check
until a runtime path appeared. Later, a quality command could select no return
and still say compliant. Both defects belong at the earliest phase that owns
the information: manifest/binding admission at pre-dispatch and exact returned
artifact admission at the worker-return fast gate.

This tranche does not attempt model ranking, token pricing, micro-packet
design, P4 receipt repair or delegation automation. Existing review-cost and
semantic-convergence controls already own round-three stops and terminal
readiness. The new implementation must compose with them rather than create a
second loop budget.

## Required Acceptance Matrix

| ID | Required behavior | Rejection probe |
|---|---|---|
| DRC-01 | every ready no-commit work order has one parseable Required Artifact Manifest before runtime edits exist | ready packet with heading/prose but no table fails |
| DRC-02 | exact `Worker return path:` and `workerReturnPath:` bindings agree and name one required manifest row | missing, duplicate or mismatched binding fails pre-dispatch |
| DRC-03 | fast gate passes the active work order to worker-return quality admission | command-construction test rejects omission |
| DRC-04 | active-work-order quality admission resolves and diagnoses the exact return even when Git changed-path discovery would select zero | absent or ineligible exact return fails |
| DRC-05 | unrelated parked returns cannot satisfy the active work order | only the exact bound return is admitted |
| DRC-06 | existing terminal-readiness and round-three stop controls remain authoritative | focused existing tests and new regression tests pass |
| DRC-07 | standards explain earliest-phase placement and unknown cost remains unknown, not zero | source diff and worker-return evidence |

## Risk / Corrective Action

This changes protected governance checkers. Fail closed only for changed or
explicitly active dispatch/return packets; do not scan all historical returns,
rewrite legacy artifacts or infer semantic correctness from structural
admission. If exact active-work-order binding cannot be added without broad
historical breakage, return `BLOCKED_WITH_REASON` with the failing fixture.

## Decision / Disposition

`DISPATCH_READY` for one distinct shared-workspace internal worker. Local owns
review, independent negative probes, commits and continuity. No subagent,
external CLI/MCP dispatch or provider call is authorized.

## Evidence / Verification

Required evidence is focused unit coverage for DRC-01 through DRC-05, the
worker-return fast gate on the exact worker packet, reviewer-fast, and a final
changed-path manifest. Gate count is structural evidence only.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACEL-FOUNDATION-T1-DISPATCH-RETURN-LOOP-CONTROL --title "ACEL Foundation T1 Dispatch Return Loop Control" --date 2026-09-23 --base dc935676838b08754a6b26d0a13813128df24785 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-verified owner facts, exact scope, tests and claim boundary |
| checkerReadAheadConfirmation | dispatch-quality, core-self-protection, review-cost, SCEC, worker-return quality and file-size owners read before authoring |
| docOnlyNewFields | none |
| claimBoundary | authoring provenance only; no runtime/provider/public claim |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Work-Order Fulfillment Manifest`; `Required Artifact Manifest`; `Worker return path:`; `workerReturnPath:`; `terminalReadinessVerdict`; `Core Guard Self-Protection Authorization` |
| gateRunPurpose | confirm pre-read packet requirements, not discover them after drafting |
| claimBoundary | static structure admission only; no semantic worker correctness claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`GUARD_MAINTENANCE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class GUARD_MAINTENANCE --role dispatcher --lifecycle-phase dispatch --json`

Returned defects: NONE_RETURNED; `totalCandidates: 0`; `truncated: false`.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | ACEL foundation T1 packet authoring, 2026-09-23 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, apply_patch, governance gates and Git |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator direction to turn the long multi-agent case and recurring orchestrator gaps into CVF foundation learning |
| Before status evidence | clean HEAD `dc935676838b08754a6b26d0a13813128df24785` |
| After status evidence | two dispatch artifacts only before dispatch commit |
| Diff evidence | `git diff --name-status` on exact two-path packet |
| Approval boundary | packet authoring and dispatch only |
| Claim boundary | no worker implementation, subagent, live provider or public action |
| Agent type | Local orchestrator/dispatcher |
| Invocation ID | `acel-foundation-t1-dispatch-return-loop-control-authoring-20260923` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This baseline authorizes bounded structural governance hardening only. It does
not prove model quality, cost superiority, independent review, runtime agent
control, provider behavior, public readiness or automatic MCP/CLI enforcement.
