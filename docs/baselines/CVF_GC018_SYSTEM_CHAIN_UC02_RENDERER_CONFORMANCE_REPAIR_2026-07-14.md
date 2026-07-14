# CVF GC-018 System Chain UC-02 Renderer Conformance Repair

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018_baseline

Date: 2026-07-14

Risk classification: R1

## Purpose

Authorize one provider-free repair of the three actual Markdown template
owners exposed by the accepted UC-02 run, followed by output regeneration
without another UC-02 invocation.

## Baseline Decision

UC-02 closed `CLOSED_PASS_BOUNDED` at material commit `9173af70b`. Its 9/9
receipt remains accepted. The separate GAP
`cvf.asc.gap.phase_governance_generated_markdown_conformance.v1` releases this
repair only.

## Scope / Target / Owner Boundary

Writable source is limited to `build_log`, `build_manifest_log`, and
`build_packet` owners, one focused test, regenerated release-gate outputs, and
one worker return. The UC-02 runner, receipt, diagnostic, coverage, closed
archive-path GAP, scenario registry, checkers, session, provider, and public
surfaces are read-only.

## Design Control Gate

| Control | Decision |
|---|---|
| Template owners | three directly source-verified renderers only |
| Orchestration | existing release gate may regenerate outputs once |
| UC-02 boundary | zero proof-run invocations and zero scenario events |
| Provider boundary | zero external provider/API/MCP calls |
| Admission target | twelve Markdown outputs pass current governed checks |
| JSON boundary | paired JSON regeneration is allowed but schema semantics stay unchanged |

## Evidence And Verification

The accepted UC-02 completion, the open renderer-conformance GAP, fresh source
reads, and the exact symbol-definition lines below form the dispatch evidence.
No provider result or provider-local memory is used as authority.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| seven family logs use the shared remediation-log renderer | `scripts/runtime_evidence_manifest/baselines.py` | import and `emit_family_baseline` | `build_log`; `emit_family_baseline` | family baseline orchestration | RUNTIME_BEHAVIOR | ACCEPT |
| family-log Markdown template owner | `scripts/export_cvf_remediation_receipt_log.py` | line 26 | `build_log` | remediation receipt Markdown renderer | EXISTS | ACCEPT |
| manifest-log Markdown template owner | `scripts/runtime_evidence_manifest/manifest_builder.py` | line 77 | `build_manifest_log` | multi-runtime manifest Markdown renderer | EXISTS | ACCEPT |
| four packet Markdown template owner | `scripts/export_cvf_release_packet.py` | line 71 | `build_packet` | release/audit/onboarding packet renderer | EXISTS | ACCEPT |
| non-ASCII separator and stale range literals are emitted by packet renderer | `scripts/export_cvf_release_packet.py` | lines 55, 176, 181 | `_extract_latest_batch_title`; `build_packet` | release packet renderer | VALUE_SET | ACCEPT |
| release gate regenerates manifest before packets | `scripts/run_cvf_runtime_evidence_release_gate.py` | line 35 `main` | `main` | runtime evidence release gate | RUNTIME_BEHAVIOR | ACCEPT |
| renderer GAP names this bounded repair | `docs/reference/system_chain/gaps/entries/phase_governance_generated_markdown_conformance.json` | complete entry | `cvf.asc.gap.phase_governance_generated_markdown_conformance.v1` | system-chain GAP source | VALUE_SET | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Control | Evidence | Disposition |
|---|---|---|---|
| keep UC-02 proof | no proof runner invocation | zero-call statement | READY |
| repair actual owners | exact three-source manifest | source diff and focused tests | READY |
| regenerate current outputs | existing release gate once | 20 output paths | READY |
| close downstream GAP | reviewer-owned after clean gates | completion and GAP update | HOLD_FOR_REVIEWER |

## Cost And Retry Control

UC-02 calls: zero. Scenario events: zero. Provider calls: zero. Release-gate
regeneration calls: one planned, one result-changing retry maximum only after a
diagnosed allowed-scope source repair.

## Acceptance Criteria

- Three template owners emit checker-safe ASCII Markdown with required common
  and review sections plus Checker Source Read-Ahead blocks.
- Packet output no longer embeds empty or stale verification ranges as PASS.
- Focused tests validate all three renderer families and negative regressions.
- Existing release gate regenerates exactly 20 current outputs.
- Reviewer-fast and worker-return fast gates pass.
- No UC-02, provider, coverage, GAP, roadmap, or session mutation by worker.

## Fail Conditions

Any fourth source owner, checker weakening, semantic evidence fabrication,
UC-02 invocation, provider call, unexpected output, secret exposure, or second
retry stops the tranche.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| UC-02 proof accepted | material commit `9173af70b` | SATISFIED |
| renderer GAP open | named per-entry GAP source | SATISFIED |
| packet authoring is next move | session commit `ef38f567e` | SATISFIED |
| dispatch base clean | empty `git status --short` at `ef38f567e` | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-repair`, role=`dispatcher`, lifecyclePhase=`dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class runtime-repair --role dispatcher --lifecycle-phase dispatch --surface-selector system-chain --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Dependency Release Evidence`; `Roadmap-To-Work-Order Trace Matrix`; `Public Export Disposition` |
| gateRunPurpose | confirmation and dispatch evidence after direct renderer-owner verification; not first discovery |
| claimBoundary | renderer repair authorization only |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | GC-018 dispatch baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | source-verified manual authoring |
| checkerReadAheadConfirmation | checker sources and literal gotchas read first |
| docOnlyNewFields | N/A with reason: no new runtime/schema field |
| claimBoundary | dispatch only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal renderer repair in private provenance.

## Claim Boundary

This baseline authorizes only renderer conformance and regeneration. It does
not reopen UC-02 or claim provider, production, public, scale, certification,
or user value.

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| UC-02 retained disposition | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` at `9173af70b` | PASS |
| renderer GAP before repair | open | `cvf.asc.gap.phase_governance_generated_markdown_conformance.v1` open | PASS |
| template-owner count | exactly 3 | three source-verified renderer symbols | PASS |
| live-call authorization | 0 UC-02 and 0 provider calls | dispatch authorizes zero | PASS |
| repair execution receipt | worker return plus regenerated outputs | not executed at dispatch | N/A with reason: dispatch phase |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `Status: DISPATCH_READY` | PASS |
| Work order status | paired work order | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | declared completion review | not yet executed | BLOCKED |
| Roadmap state | system-chain roadmap | UC-02 stays proven | N/A with reason |
| Registry JSON | renderer GAP index | open until repair review | BLOCKED with reason |
| Registry Markdown | GAP README | open until repair review | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence | repository source only | N/A with reason |
| System loop interlock | regenerated outputs | not yet executed | BLOCKED |
| Session continuity | active state | separate after material closure | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | renderer repair dispatch, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, apply_patch, GAP generator, dispatch gates |
| Target paths | correction artifacts plus paired baseline/work order |
| Allowed scope source | session nextAllowedMove after `9173af70b` |
| Before status evidence | clean worktree at HEAD `ef38f567e` |
| After status evidence | source-verified dispatch packet and owner correction |
| Diff evidence | material dispatch diff before commit |
| Approval boundary | packet authoring and one no-commit worker |
| Claim boundary | no implementation, regeneration, UC-02, provider, public, or session edit |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc02-renderer-repair-baseline-2026-07-14 |
| Expected manifest | correction artifacts plus paired packet |
| Actual changed set | recomputed before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |
