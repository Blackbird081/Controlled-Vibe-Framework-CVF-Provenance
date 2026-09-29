# CVF GC-018 Baseline - RFR-R7A Canonical MCP Guard Engine Adoption

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-24

Batch ID: RFR-R7A-CANONICAL-MCP-GUARD-ENGINE-ADOPTION

Dispatch base head: `fddcfedf5a41a04f71a2b3228f662c399f5e2e6e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through explicit approval of the R7A/R7B split

Reviewer owner: current independent orchestrator/reviewer/closer

Worker target: one delegated implementation worker role

## Purpose

Authorize RFR-R7A to make every MCP production composition root consume the
declared canonical `cvf-guard-contract` engine instead of the stale package-local
fork. MCP/CLI session-phase state must be separated from the engine without
creating a second guard factory or weakening the R1/R2 mandatory core.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R7A-CANONICAL-MCP-GUARD-ENGINE-ADOPTION --title "CVF RFR-R7A Canonical MCP Guard Engine Adoption" --date 2026-08-24 --base fddcfedf5a41a04f71a2b3228f662c399f5e2e6e --commit-mode WORKER_MUST_NOT_COMMIT --dependency "RFR-R6 reviewer disposition accepted at 39ba8f31f with remediation required" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker and MCP/CLI boundary profiles |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with verified R6 defect evidence, exact R7A manifest, canonical-engine constraints and bounded known-failure rule |
| checkerReadAheadConfirmation | dispatch-quality, prompt-envelope, lifecycle-hygiene, checker-read-ahead, worker-return-quality and corpus-coverage sources reviewed |
| docOnlyNewFields | none; existing governed dispatch fields are reused |
| claimBoundary | dispatch-authoring provenance only; no implementation or runtime success claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| R6 audit accepted with remediation required | `docs/reviews/CVF_RFR_R6_CROSS_OWNER_ADVERSARIAL_REAUDIT_WORKER_RETURN_2026-08-24.md`, reviewer annotation; material commit `39ba8f31f` | Defect A is reproduced and explicitly requires fresh owner-specific authority | ACCEPT |
| operator selects recommended split | operator message on 2026-08-24: agreement with R7A then R7B | R7A may dispatch first; R7B stays dependency-gated | ACCEPT |
| canonical package is already declared | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json`, dependencies | dependency exists without install or lockfile mutation | ACCEPT |

## Scope

R7A owns only the MCP production composition/type seams, directly affected MCP
tests, one new canonical-adoption regression test, and one worker return. It may
move session-phase storage into MCP/CLI-local state. It must not edit the Guard
Contract package, the R4 material-context validator, package manifests,
lockfiles, governance, roadmap, session state, or the stale local guard sources.

## Acceptance Invariants

- Every non-test production use of `createGuardEngine` or `GuardRuntimeEngine`
  imports from `cvf-guard-contract`.
- `src/index.ts`, `src/cli/cli.ts`, `src/cli/governed-exec.ts`, and `src/sdk.ts`
  cannot reach the local factory.
- MCP session-phase compatibility is local state only; it cannot register,
  unregister, disable, clone, wrap, proxy, or replace canonical guards.
- The live engine contains `ai_commit`, `authority_gate`, `phase_gate`, and
  `build_authority`; mandatory removal/disable and returned-view mutation fail.
- No BUILD mutation is made permissive merely to preserve an old fixture.
- The three already-known R7B composition failures may remain; no fourth
  package failure is accepted.

## Baseline Decision

`PROCEED_BOUNDED_IMPLEMENTATION`: R7A may repair Defect A only. R7B optional
field composition remains outside scope and dependency-gated on independent
R7A acceptance.

## Evidence / Verification

Required evidence is direct import search, canonical guard-ID and immutability
probes, focused MCP tests, strict TypeScript build, full MCP package test with
an exact 745-pass/3-known-R7B-fail ceiling or better, worker-return fast gate,
and exact manifest reconciliation.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| MCP declares canonical dependency | PACKAGE_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json` | dependencies | `cvf-guard-contract` | MCP package dependency owner | ACCEPT |
| live MCP root imports local factory | RUNTIME_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | import block and singleton engine | `createGuardEngine`; `GuardRuntimeEngine` | MCP server composition root | ACCEPT |
| both CLI roots import local factory | RUNTIME_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/cli.ts` and `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | import blocks and engine construction | `createGuardEngine` | MCP CLI composition roots | ACCEPT |
| SDK exports local fork | EXPORT_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/sdk.ts` | guard export block | `createGuardEngine`; `GuardRuntimeEngine` | MCP SDK surface | ACCEPT |
| local factory registers only six guards | RUNTIME_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/index.ts` | `createGuardEngine` | six local registrations | stale MCP guard owner | ACCEPT |
| canonical factory registers hardened stack | RUNTIME_SOURCE | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | Factory | `AiCommitGuard`; `BuildAuthorityGuard`; canonical factory | Guard Contract owner | ACCEPT |
| canonical mandatory IDs include R1/R2 | CONTRACT_SOURCE | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | mandatory guard constants | `MANDATORY_GUARD_IDS` | Guard Contract type owner | ACCEPT |
| canonical engine protects mandatory guards and snapshots views | RUNTIME_SOURCE | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | registration, unregister/disable and accessor methods | `snapshotGuard`; `freezeGuardView`; `unregisterGuard`; `disableGuard` | Guard Contract engine owner | ACCEPT |
| session phase methods exist only on local fork | COMPATIBILITY_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts` and `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | public methods | `getSessionPhase`; `setSessionPhase` absent canonically | MCP compatibility seam | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact R7A paths | `Test-Path -LiteralPath` returned false for baseline, work order and return before authoring | ACCEPT |
| token collision | `rg -n 'RFR-R7A|RFR_R7A|canonical MCP guard engine' docs CVF_SESSION` returned no prior tranche artifact | ACCEPT |
| production import inventory | `rg -n 'cvf-guard-contract|createGuardEngine|GuardRuntimeEngine|guards/index' EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json` identifies all current seams | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; Dependency Release Evidence; Worker Return Packet Shape Contract; Agent Handoff Contract Control Block |
| gateRunPurpose | confirm final dispatch shape after semantic/source verification, not first discovery |
| claimBoundary | checker conformance does not prove canonical engine adoption or test correctness |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | worker edits exact MCP manifest | local implementation/test only; no commit | this baseline and paired work order | repository-local source lane | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | MCP server, CLI and SDK production roots | canonical admission must be present before external caller exposure | verified current imports and R6 probes | R7A changes composition only; no live invocation | `IMPLEMENTATION_AUTHORIZED_BOUNDED` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance remediation; no public-sync action is authorized.

## Claim Boundary

This baseline authorizes local MCP source/test edits in the paired exact
manifest. It authorizes no Guard Contract edit, R7B repair, dependency install,
provider/live/network call, credential access, deployment, public sync, push,
or production-readiness claim.
