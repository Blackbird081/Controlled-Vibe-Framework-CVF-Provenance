# CVF GC-018 Baseline - WOAS-R5 Scaffold-First Dispatch Quality Gate

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: WOAS-R5

Dispatch base head: `048816a0`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: reviewer/closer role

Worker target: delegated worker role, not a provider-specific role

## Purpose

Authorize one bounded guard-hardening tranche that makes scaffold-first dispatch
authoring machine-checkable. The worker must add a scaffold provenance standard,
extend the dispatch scaffold helper to emit a `Scaffold Provenance Block`, add a
dedicated provenance checker with focused tests, and wire that checker into the
local gate chain so future dispatch packets fail before worker execution when
they look hand-written or retain unresolved scaffold placeholders.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id WOAS-R5 --title "Scaffold-First Dispatch Quality Gate" --date 2026-07-01 --base 048816a0 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled authority chain, source verification, allowed scope, acceptance criteria, fail conditions, verification commands, and claim boundaries; removed all unresolved placeholder fields. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| docOnlyNewFields | `Scaffold Provenance Block`; `scaffoldHelperCommand`; `generatedProfile`; `generatedSkeletonStatus`; `manualEditsAfterScaffold`; `checkerReadAheadConfirmation`; `docOnlyNewFields` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring-scaffold`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order-authoring-scaffold" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF entries were returned for this exact query; worker must still record any new repeated non-obvious defect pattern in ADIF before closure if one is found. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py` |
| literalTokensReviewed | `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `Status: DISPATCH_READY`; `## Dispatch Prompt Envelope`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Core Guard Self-Protection Authorization`; `## Delta Execution Claim Boundary Control Block`; `CLAIM_REJECTED`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `## Public Export Disposition`; `DEFERRED_PRIVATE_ONLY`; `Agent Operation Trace Block`; `Scaffold Provenance Block`; `scaffoldHelperCommand`; `generatedProfile`; `manualEditsAfterScaffold` |
| gateRunPurpose | Confirmation evidence, not first discovery; checker source and literal tokens were read before this baseline was authored. |
| claimBoundary | Read-ahead evidence for this WOAS-R5 dispatch baseline only; worker must repeat source read-ahead for its own changed artifacts. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session permits another bounded work-order-authoring scaffold hardening lane following WOAS-R4 material commit `e6a56718`. | EXISTS | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| Dispatch scaffold helper owns trigger-family and scaffold argument generation. | EXISTS | `governance/compat/build_dispatch_packet_scaffold.py` | line 49 and line 134 | `TRIGGER_FAMILIES`; `ScaffoldArgs` | dispatch scaffold helper | ACCEPT |
| Dispatch scaffold helper owns baseline and work-order text generation. | EXISTS | `governance/compat/build_dispatch_packet_scaffold.py` | line 519 and line 591 | `build_gc018_baseline`; `build_work_order` | dispatch scaffold helper | ACCEPT |
| Worker-return skeleton helper already emits self-declaration and work-order response markers. | EXISTS | `governance/compat/build_worker_return_skeleton_scaffold.py` | line 9 and lines 21-22 | `build_worker_return_skeleton`; `work_order_path` | worker-return skeleton helper | ACCEPT |
| Worker-return fast gate already runs the WOAS-R4 worker-return quality checker before reviewer-fast. | EXISTS | `governance/compat/run_worker_return_fast_gate.py` | line 30 and lines 50-51 | `build_commands`; `worker-return quality gate` | worker-return fast gate | ACCEPT |
| Dispatch prompt envelope checker requires the envelope as the first top-level work-order section near the top. | EXISTS | `governance/compat/check_dispatch_prompt_envelope.py` | lines 38 and 59 | `ENVELOPE_SECTION_MARKER`; `REQUIRED_FIELDS` | dispatch prompt envelope checker | ACCEPT |
| Checker read-ahead guard requires a machine-shaped block in changed governed execution artifacts. | EXISTS | `governance/compat/check_governed_artifact_checker_read_ahead.py` | lines 22-23 | `REQUIRED_HEADING`; `REQUIRED_FIELDS` | checker read-ahead guard | ACCEPT |
| Existing repository has no scaffold provenance block or checker. | LITERAL_INVARIANT | `governance/compat/`; `docs/reference/work_order_authoring/`; `docs/baselines/`; `docs/work_orders/`; `docs/reviews/` | negative search before authoring returned no matches | `Scaffold Provenance Block`; `scaffold provenance`; `SCAFFOLD_PROVENANCE` | pre-dispatch negative search | ACCEPT |

## New Doc-Only Fields

| Field | Intended owner | Dispatch disposition |
| --- | --- | --- |
| `Scaffold Provenance Block` | new standard and checker to be created by worker | DOC_ONLY_NEW until worker implementation creates source and tests |
| `scaffoldHelperCommand` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |
| `generatedProfile` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |
| `generatedSkeletonStatus` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |
| `manualEditsAfterScaffold` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |
| `checkerReadAheadConfirmation` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |
| `docOnlyNewFields` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for baseline | `Test-Path docs/baselines/CVF_GC018_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_2026-07-01.md` returned `False` before authoring | PASS |
| Path existence for work order | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_2026-07-01.md` returned `False` before authoring | PASS |
| Path existence for planned worker return | `Test-Path docs/reviews/CVF_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_WORKER_RETURN_2026-07-01.md` returned `False` before authoring | PASS |
| Token collision search | `rg -n "WOAS_R5_SCAFFOLD_FIRST|WOAS-R5 Scaffold-First|woas_r5_scaffold_first|CVF_WOAS_R5" docs/baselines docs/work_orders docs/reviews docs/reference/work_order_authoring governance/compat CVF_SESSION_MEMORY.md AGENT_HANDOFF_V30_2026-07-01.md` returned no matches before authoring | PASS |
| Scaffold provenance negative search | `rg -n "Scaffold Provenance Block|scaffold provenance|SCAFFOLD_PROVENANCE" governance/compat docs/reference/work_order_authoring docs/baselines docs/work_orders docs/reviews` returned no matches before authoring | PASS |
| Collision decision | No existing WOAS-R5 packet, worker return, scaffold provenance standard, or scaffold provenance checker was found. | PASS |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| WOAS-R1 dispatch scaffold foundation | Material commit `fb6a0ae9`; helper and standard exist. | R5 may extend scaffold authoring because the helper foundation is closed and current. | SATISFIED |
| WOAS-R3 worker-return skeleton scaffold | Material commit `38765baf`; generated worker-return skeleton exists. | R5 may rely on worker-return skeleton fields and must preserve them. | SATISFIED |
| WOAS-R4 worker-return quality gate | Material commit `e6a56718`; worker-return quality gate is wired into worker-return fast gate and local hooks. | R5 may add the analogous dispatch-input quality gate following material commit `e6a56718`. | SATISFIED |
| Current active mode | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` records lane selection after material commit `e6a56718`. | Dispatch may proceed only as bounded scaffold/checker hardening with no runtime/provider/public expansion. | SATISFIED |

## Baseline Decision

Decision: DISPATCH_READY

Proposed tranche: WOAS-R5 Scaffold-First Dispatch Quality Gate.

Baseline boundary: standard/helper/checker/test/catalog wiring only, with
`WORKER_MUST_NOT_COMMIT` and reviewer-owned closure.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: WOAS-R5 does not ingest or classify outside source material. |
| Matching local-view guard | N/A with reason: no outside-source local-view guard is needed for scaffold/checker work. |
| Owner surface | `docs/reference/work_order_authoring/`; `governance/compat/` |
| Disposition | NOT_APPLICABLE_WITH_REASON: local scaffold provenance and checker-hardening tranche only. |
| Claim boundary | No outside-source intake, absorption, source import, source-mirror mutation, or external-agent output conversion is authorized. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: WOAS-R5 may add a scaffold provenance
checker, focused tests, helper-generated block, and gate wiring for dispatch
artifact quality only.

Protected paths:

- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/check_dispatch_scaffold_provenance.py`
- `governance/compat/test_check_dispatch_scaffold_provenance.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/agent_autorun_command_catalog.py`

Operator authorization: current operator instruction selected the R5 tranche to
reduce latency and improve worker output quality after material commit
`e6a56718`.

Rollback boundary: reviewer/closer may reject the uncommitted worker return; no
protected-path change is committed unless the reviewer accepts the WOAS-R5
material batch.

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | Add a reference standard under `docs/reference/work_order_authoring/` defining the required `Scaffold Provenance Block` fields and claim boundary. |
| AC2 | Extend `build_dispatch_packet_scaffold.py` so generated GC-018 and work-order output includes a filled scaffold provenance stub with no `FILL_ME` values for the fields it can know at generation time. |
| AC3 | Add a dedicated range-aware checker, preferably `governance/compat/check_dispatch_scaffold_provenance.py`, that fails changed dispatch-ready baselines/work orders missing the block, missing required fields, retaining placeholder values, or claiming provenance without a helper command or manual-edit disposition. |
| AC4 | Wire the checker into pre-dispatch/autorun common checks and local reviewer-fast/pre-commit/pre-push catalogs. |
| AC5 | Add focused tests covering a valid scaffold-provenance block, missing block failure, unresolved placeholder failure, quoted-marker non-applicability where relevant, helper output inclusion, and catalog wiring. |
| AC6 | Worker return passes WOAS-R4 `run_worker_return_fast_gate.py` with focused pytest targets for the new checker/helper/catalog tests. |

## Fail Conditions

| Condition | Required response |
| --- | --- |
| Worker needs runtime/provider/live proof, public-sync, Web/UI/dashboard, MCP/CLI adapter behavior, package lifecycle mutation, model-router work, action authority, automatic invocation, or production-readiness work. | Return `BLOCKED_WITH_REASON`; new GC-018/source-verified work order is required. |
| Worker finds that adding the checker would require broad rewrite of `check_work_order_dispatch_quality.py` or large near-threshold file expansion. | Prefer a new same-domain checker; if still blocked, return `BLOCKED_WITH_REASON` with source evidence. |
| Helper output changes unrelated default scaffold content beyond the new provenance block. | Repair before return or document the exact intentional delta and add focused tests. |
| New checker false-flags archived docs, completion reviews, or quoted examples that are not changed dispatch-ready baselines/work orders. | Repair eligibility logic and add regression tests before return. |
| Worker return cannot satisfy the WOAS-R4 worker-return quality gate. | Repair in allowed scope before return or return `BLOCKED_WITH_REASON` with exact failing checker evidence. |

## Verification Commands

Worker must run at minimum:

```text
python -m unittest governance.compat.test_check_dispatch_scaffold_provenance governance.compat.test_build_dispatch_packet_scaffold governance.compat.test_run_local_governance_hook_chain -v
python governance/compat/check_dispatch_scaffold_provenance.py --base 048816a0 --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_dispatch_scaffold_provenance.py --pytest-target governance/compat/test_build_dispatch_packet_scaffold.py --pytest-target governance/compat/test_run_local_governance_hook_chain.py
python governance/compat/run_agent_automation_assist.py --base 048816a0 --head HEAD --json --enforce
```

Worker should add or adjust direct commands if source changes require a
different focused test path. Gate runs are confirmation evidence, not first
discovery.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | WOAS-R5 authorizes dispatch scaffold/checker/test/catalog wiring only. |
| requiredFutureAction | If a later packet adds runtime or provider behavior, create a fresh source-verified work order and live-proof plan. |
| providerRegistryBoundary | N/A with reason: no provider registry mutation or provider routing claim. |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | WOAS-R5 scaffold-first dispatch quality gate baseline |
| claimDisposition | CLAIM_REJECTED: this packet makes no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, or universal governed-coding-control claim. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this dispatch. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this dispatch. |
| invocationBoundary | Manual local helper/checker/test invocation only after worker implementation. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | Dispatch artifact shape, helper scaffolding, and local checker coverage only. |
| forbiddenExpansion | Runtime/provider/live/public/package/Web/MCP/model-router behavior requires fresh source-verified authorization. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | WOAS-R5 scaffold-first dispatch quality gate, 2026-07-01 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | shell, scaffold helper stdout, apply_patch, pre-dispatch gates |
| Target paths | this baseline; paired WOAS-R5 work order |
| Allowed scope source | current operator instruction to create R5 work order after material commit `e6a56718` |
| Before status evidence | HEAD `048816a0`; worktree clean before dispatch authoring |
| After status evidence | pending pre-dispatch verification before material dispatch commit |
| Diff evidence | `git diff --name-status` before dispatch commit |
| Approval boundary | dispatch packet authoring only |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router claim |
| Agent type | dispatcher |
| Invocation ID | `woas-r5-dispatch-2026-07-01` |
| Expected manifest | this baseline; paired WOAS-R5 work order |
| Actual changed set | to be verified before dispatch commit |
| Manifest delta | TO_VERIFY_BEFORE_COMMIT |
| Deletion or rename disposition | N/A with reason: no deletion or rename planned |

## Claim Boundary

This baseline authorizes local scaffold provenance standard/helper/checker/test
and gate-catalog wiring only. It does not authorize real outside-source intake,
source import, source-mirror mutation, runtime/provider/live proof,
public-sync, Web/UI/dashboard, MCP/CLI adapter behavior, package lifecycle
mutation, model-router work, action authority, automatic invocation, or
production-readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: WOAS-R5 is private provenance governance-helper work. No public-sync
export is authorized by this baseline.
