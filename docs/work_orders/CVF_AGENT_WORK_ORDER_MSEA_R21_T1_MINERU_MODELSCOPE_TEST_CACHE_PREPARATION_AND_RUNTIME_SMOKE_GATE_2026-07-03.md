# CVF Agent Work Order - MSEA-R21-T1 MinerU ModelScope Test Cache Preparation And Runtime Smoke Gate

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R21_T1

Dispatch base head: bd322a8d

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_WORKER_RETURN_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R21_T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker must capture `git rev-parse --short HEAD` before edits.

Current-time notes: artifact date is 2026-07-03; use current repository state, pinned MinerU source mirror, and the operator's test-first ModelScope route choice.

Do-not-misread notes: this packet authorizes only command-exists-gated ModelScope pipeline model-cache preparation. It does not authorize package install, parser/OCR/VLM/API/router/Gradio/Docker execution, local temporary service startup, document body read, extraction outputs, public-sync, schema/writer/adapter/checker implementation, legal advice, current-law, production, or workflow-chain claims.

Required first actions: read startup files, guard orientation, literal gotchas, this work order, the paired GC-018 baseline, source references, and checker source listed in the Checker Source Read-Ahead Block before writing worker outputs.

Return contract: create the worker return and companion readiness matrix, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute the first bounded MinerU test-prep step after operator ModelScope
selection: verify whether the local environment already exposes the
`mineru-models-download` command, then either perform one explicit ModelScope
pipeline model-cache/download attempt or return a package-install authorization
blocker. The worker must not run parser/OCR/VLM/service/Docker/API commands or
read source document bodies.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R21_T1 --title "MinerU ModelScope Test Cache Preparation And Runtime Smoke Gate" --date 2026-07-03 --base bd322a8d --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed scaffold fields, set DISPATCH_READY, added R20 dependency release, source-verified ModelScope/download/config facts, evidence-reuse plan, worker-output shape mandate, route tokens, and conditional cache-prep command boundary. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py`. |
| docOnlyNewFields | selectedRouteToken; modelSourceRoute; downloadCommandStatus; modelCachePrepDisposition; configWritebackReceipt; runtimeSmokeGateDisposition; installAuthorizationStatus |
| claimBoundary | Dispatch authoring provenance only; no parser/OCR/VLM/API/Docker/service/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, missing MinerU source
mirror, missing command that would require package install, failed network or
download diagnostic that cannot be classified safely, forbidden-scope need, or
missing authority that makes completion impossible.

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition |
| --- | --- | --- | --- |
| MSEA-R20-T1 accepted operator model-source checkpoint | `docs/reviews/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | `df5b71fa` | SATISFIED - selected route token `HOLD_PENDING_OPERATOR_MODEL_SOURCE_CHOICE` explicitly allowed operator selection among local, modelscope, huggingface, auto/config write-back, or defer |
| Session next-move freshness | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V34_2026-07-03.md` | `bd322a8d` | SATISFIED - next allowed move permits modelscope remote download permission before runtime smoke work-order authoring |
| Operator model-source choice | current operator instruction in this session | N/A | SATISFIED - operator accepted ModelScope for test-first use while deferring deeper project-specific model selection |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | Worker output checker read-ahead is mandatory; provider-local authority is excluded; package install remains blocked; ModelScope cache preparation is conditional and does not become parser runtime readiness. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; Evidence Reuse And Encoding Plan fields; ADIF resolver query exactness; Dependency Release Evidence; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields; Worker Return Packet Shape Contract fields; Source-Intake Decision Packet Fields; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; Delta block field labels; Agent Operation Trace labels. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm this work order's dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this work order and paired baseline only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R21-T1 must re-read current CVF-governed sources, accepted R20 artifacts, pinned MinerU source mirror docs/source, and local command metadata before attempting any allowed command.

unicodePathHandling: Use LiteralPath and UTF-8-safe command output for local paths; do not normalize or rewrite filenames.

extractedTextAuthority: N/A with reason

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` |
| priorVerificationAnchor | `## Route Decision Menu Selection` |
| recomputeReason | R21-T1 must re-read current CVF-governed sources, accepted R20 artifacts, pinned MinerU source mirror docs/source, and local command metadata before attempting any allowed command |
| freshRecomputeRequired | true for source facts, command existence, model-cache/config evidence, and diagnostics; no document body read and no parser extraction |
| unicodePathHandling | Use `-LiteralPath` and UTF-8-safe command output for local paths; do not normalize or rewrite filenames |
| extractedTextAuthority | N/A with reason |

## Operator Authorization And Privacy Boundary

The operator selected ModelScope for test-first MinerU preparation while
deferring deeper use-case or project-specific model choice. Candidate Group A
source documents remain authorized for local private CVF testing only. Original
documents must not be public-synced or redistributed. This tranche may create
metadata/redacted evidence about model-cache preparation but must not copy
source documents into the repository, read source document body content, create
parser outputs, or include sensitive personal/legal details in committed
artifacts.

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MinerU source mirror remains the current upstream authority for this lane. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | line 35 | `opendatalab__MinerU` | source mirror index | ACCEPT |
| R20 selected a hold pending operator model-source choice before runtime smoke. | VALUE_SET | VALUE_SET | `docs/reviews/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_WORKER_RETURN_2026-07-03.md` | `## Reviewer Decision / Closure Disposition` | `HOLD_PENDING_OPERATOR_MODEL_SOURCE_CHOICE` | MSEA-R20-T1 worker return | ACCEPT |
| R20 matrix names modelscope download permission as a release option. | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | lines 62-67 | `modelscope` | MSEA-R20-T1 readiness matrix | ACCEPT |
| MinerU supports `MINERU_MODEL_SOURCE=modelscope`. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | lines 12-14 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| MinerU quick usage says users can switch from huggingface to modelscope through the environment variable. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md` | lines 4-6 | `MINERU_MODEL_SOURCE` | quick usage documentation | ACCEPT |
| MinerU built-in model download generates `mineru.json` and may update config. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/quick_usage.md` | line 122 | `mineru-models-download` | quick usage documentation | ACCEPT |
| MinerU model download writes path and actual source to `mineru.json`. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 44 | `mineru.json` | model source documentation | ACCEPT |
| MinerU download command supports remote source and model type choices. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 91-105 | `--source`; `--model_type` | `download_models` | ACCEPT |
| MinerU download command supports pipeline or VLM models from ModelScope or HuggingFace. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/models_download.py` | lines 114-117 | `download_models` | `download_models` | ACCEPT |
| MinerU project exposes `mineru-models-download` as a console script. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | line 133 | `mineru-models-download` | project scripts | ACCEPT |
| MinerU config path can be set with `MINERU_TOOLS_CONFIG_JSON` or defaults to `mineru.json` in the user home directory. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/models_download_utils.py` | lines 23-28 | `get_tools_config_file_path` | config path helper | ACCEPT |
| Pipeline backend is the lower-risk first smoke target because it can run CPU or GPU. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 74 | `pipeline` | upstream README backend comparison | ACCEPT |
| MinerU CLI parser runtime can automatically start a local temporary service without API URL. | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 146 | `mineru` | upstream README | ACCEPT |
| VLM MinerU2.5 model exists on HuggingFace and ModelScope but is not selected for this first test gate. | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/changelog.md` | line 112 | `opendatalab/MinerU2.5-2509-1.2B` | changelog | ACCEPT |

## New Doc-Only Fields

| Field | Meaning | Disposition |
| --- | --- | --- |
| selectedRouteToken | Worker-selected next route for reviewer/closer consideration | DOC_ONLY_NEW |
| modelSourceRoute | Records that the operator selected ModelScope for test-first preparation | DOC_ONLY_NEW |
| downloadCommandStatus | Worker classification of whether `mineru-models-download` exists locally | DOC_ONLY_NEW |
| modelCachePrepDisposition | Worker classification of command result, cache/config evidence, or blocker | DOC_ONLY_NEW |
| configWritebackReceipt | Secret-safe before/after `mineru.json` metadata and diff summary | DOC_ONLY_NEW |
| runtimeSmokeGateDisposition | Whether a later parser smoke work order can be authored | DOC_ONLY_NEW |
| installAuthorizationStatus | Records that package install remains unauthorized in this tranche | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R21 artifact path check | `Test-Path` for planned baseline, work order, worker return, and companion reference returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| R21 token search | `rg -n "MSEA_R21_T1|MSEA-R21-T1|MODELSCOPE_TEST_CACHE_PREPARATION|ModelScope Test Cache Preparation" docs CVF_SESSION AGENT_HANDOFF_V34_2026-07-03.md .private_reference/source_mirrors/INDEX.md` returned no matches before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Collision decision | MSEA-R21-T1 is a new child tranche released by accepted MSEA-R20-T1 and operator ModelScope test choice | SAFE_TO_CREATE |

## Authority Chain

- Operator instruction: select ModelScope for test-first MinerU preparation, while deferring deeper project-specific model choice.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V34_2026-07-03.md`.
- Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_2026-07-03.md`.
- Accepted R20 route selection and readiness matrix.
- Candidate Group A private intake: `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md`.
- MinerU source authority: `.private_reference/source_mirrors/opendatalab__MinerU/`.

Authority boundary: if any source contradicts this packet, stop and return
`BLOCKED_WITH_REASON`. The worker may not upgrade cache-prep language into
parser runtime, package install, service startup, or production authority.

## Required First Reads

| Source | Required action |
| --- | --- |
| active session front door named by root agent instructions | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V34_2026-07-03.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| paired GC-018 baseline | READ |
| this work order | READ |
| source files listed in Source Verification Block | READ |
| checker source listed in Checker Source Read-Ahead Block | READ |

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Operator | operator | owns model-source, package-install, parser-runtime, document-body, public-sync, and production decisions |
| Dispatcher | dispatcher role | authors this GC-018/work order and runs pre-dispatch gates |
| Worker | delegated worker role | creates only the named worker return and companion readiness matrix, without commit |
| Reviewer/closer | reviewer/closer | reviews returned artifacts, repairs allowed-scope shape defects if needed, commits material if accepted |
| Session-sync steward | reviewer/closer once material is accepted | updates active session state once accepted material exists |

## Pre-Flight Checks

Required before worker execution:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path 'docs\reviews\CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_WORKER_RETURN_2026-07-03.md'
Test-Path 'docs\reference\CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_READINESS_MATRIX_2026-07-03.md'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected result: clean worktree at execution start, planned worker outputs
absent before writing, and pre-implementation gate passing after worker output
authoring and allowed-scope repairs.

## Write Ownership

| Path family | Worker permission |
| --- | --- |
| `docs/reviews/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_WORKER_RETURN_2026-07-03.md` | CREATE_ONLY_UNCOMMITTED |
| `docs/reference/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_READINESS_MATRIX_2026-07-03.md` | CREATE_ONLY_UNCOMMITTED |
| user-home `mineru.json` and model cache created or updated by `mineru-models-download` | CONDITIONAL_LOCAL_SIDE_EFFECT_ALLOWED only if the command already exists and the worker runs the explicit allowed command |
| session-state, front-door, and active-handoff surfaces | FORBIDDEN |
| `.private_reference/source_mirrors/**` | READ_ONLY |
| runtime source, package lifecycle, public-sync, Web, MCP, model-router, checker, adapter paths | FORBIDDEN |

## Execution Plan

1. Capture `executionBaseHead` and current worktree status.
2. Complete Required First Reads and checker-source read-ahead.
3. Recompute source facts from R20/R17 and the pinned MinerU mirror.
4. Run read-only local metadata commands to identify Python, the download command, `MINERU_MODEL_SOURCE`, `MINERU_TOOLS_CONFIG_JSON`, and existing user config presence.
5. If `mineru-models-download` is absent, do not install anything; write a blocker route.
6. If `mineru-models-download` is present, set only the process-local model source to `modelscope` and run one explicit pipeline cache-prep command.
7. Record secret-safe before/after config/cache metadata, command exit status, and diagnostic classification.
8. Author the worker return and companion readiness matrix.
9. Run worker-return fast gate and pre-implementation autorun.
10. Leave changes uncommitted and return the status token.

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| Base and worktree status | `executionBaseHead`, `git status --short`, and actual changed file list |
| Source verification | Source Inventory plus Source Verification Block in worker outputs |
| ModelSource route | `modelSourceRoute: modelscope` and explicit non-auto statement |
| Command availability | `Get-Command mineru-models-download -ErrorAction SilentlyContinue` result |
| Allowed command if present | exact command `mineru-models-download --source modelscope --model_type pipeline` |
| Config write-back | secret-safe before/after metadata for resolved config path; no raw secrets printed |
| Cache evidence | model path/cache root evidence only if created or reported by the command; no model files committed |
| Runtime non-execution | explicit statement that no parser/OCR/VLM/API/router/Gradio/Docker/service/document-body action occurred |
| Route decision | exactly one `selectedRouteToken` in both worker return and companion matrix |
| Gates | worker-return fast gate and pre-implementation autorun output |

## Allowed Commands

The worker may run these commands or direct equivalents:

```powershell
git rev-parse --short HEAD
git status --short
python --version
Get-Command python -ErrorAction SilentlyContinue
Get-Command mineru-models-download -ErrorAction SilentlyContinue
Get-ChildItem Env:MINERU_MODEL_SOURCE -ErrorAction SilentlyContinue
Get-ChildItem Env:MINERU_TOOLS_CONFIG_JSON -ErrorAction SilentlyContinue
Test-Path (Join-Path $HOME 'mineru.json')
```

If `mineru-models-download` exists, the worker may run exactly one download
command:

```powershell
$env:MINERU_MODEL_SOURCE='modelscope'; mineru-models-download --source modelscope --model_type pipeline
```

The worker must not print raw secret values or document body content. If the
command fails, classify the failure by stage, class, retryability, user action,
safe message, and whether a rerun is allowed. Do not repeatedly consume network
or storage after an unclear failure.

## Forbidden Commands And Actions

- Do not run `pip`, `uv`, `conda`, package install, package upgrade, or source import.
- Do not import MinerU modules manually.
- Do not invoke `mineru`, `mineru-api`, `mineru-router`, or `mineru-gradio`.
- Do not run parser/OCR/VLM/hybrid/API/router/Gradio/Docker/WSL/service commands.
- Do not read document body content.
- Do not create parser extraction outputs.
- Do not edit `.private_reference/source_mirrors/**`, runtime source, public-sync, schema/writer/adapter/checker, Web, MCP, model-router, or session-sync paths.
- Do not claim extraction accuracy, document truth, legal advice quality, current-law correctness, production readiness, or workflow-chain completion.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intakeRole | dispatcher-authored private runtime-precondition work order |
| scope classification | bounded local model-cache preparation and gate decision; changed repo paths limited to the two worker outputs |
| workerRole | no-commit source verifier, command-exists gate runner, ModelScope pipeline cache-prep executor if allowed, and route selector |
| reviewerRole | reviewer/closer validates worker return and companion readiness matrix |
| operatorRole | owns any later package install, parser runtime, document-body, fuller-content, public-sync, provider, or production decision |
| route mode | MULTI_AGENT_SINGLE_ROLE |
| routeDecision | proceed with ModelScope test cache preparation only; hold parser runtime |
| escalationCondition | missing download command, package install need, source contradiction, network/cache failure that cannot be classified safely, need to run parser/service/Docker/API, need to read document body content, or need to edit forbidden paths |
| claimBoundary | role routing only; no automatic execution, provider routing, public export, parser proof, or production claim |

## Route Decision Menu

Worker must select exactly one `selectedRouteToken`:

| Token | Meaning |
| --- | --- |
| OPEN_MSEA_R22_LOCAL_PIPELINE_RUNTIME_SMOKE_WORK_ORDER | ModelScope pipeline cache preparation succeeded enough to author a fresh parser smoke work order |
| HOLD_PENDING_MINERU_PACKAGE_INSTALL_AUTHORIZATION | `mineru-models-download` is missing or unusable because MinerU is not installed; package lifecycle mutation needs a fresh work order |
| HOLD_PENDING_MODELSCOPE_DOWNLOAD_DIAGNOSTIC | ModelScope cache preparation failed with a classified network/storage/source diagnostic that needs operator action |
| HOLD_PENDING_CONFIG_WRITEBACK_REVIEW | cache command touched or would touch config in a way requiring reviewer/operator decision before runtime |
| HOLD_ALL_MINERU_RUNTIME_LANES | no source-backed next step is ready |

## Required Worker Analysis

1. Re-read R20 worker return and matrix; summarize why operator model-source choice was the blocker.
2. Record `modelSourceRoute: modelscope` and state that this is a test-first route, not final project model selection.
3. Re-read pinned MinerU docs/source for model source, config write-back, download command entry point, command options, pipeline backend, and temporary service runtime boundary.
4. Verify command availability before any download attempt.
5. If available, run exactly one ModelScope pipeline command and capture secret-safe command/result/config/cache evidence.
6. If unavailable or failed, classify the blocker and do not install anything.
7. Produce a companion readiness matrix with:
   - command availability;
   - ModelScope source route;
   - pipeline model type choice;
   - config write-back receipt;
   - cache/root evidence or blocker;
   - privacy/redaction posture;
   - forbidden runtime action checklist;
   - selected route token and rationale.
8. Do not include document body content, raw secrets, original source file copies, model files, or large command logs.

## Runtime Candidate Parking Checks

| Candidate | Required disposition for this tranche | Reason |
| --- | --- | --- |
| MinerU package install or package activation | REMOVED_OR_REJECTED | package lifecycle mutation is outside this tranche |
| ModelScope pipeline model cache/download | RUNTIME_CANDIDATE | authorized only through existing `mineru-models-download` command and one explicit pipeline command |
| VLM or MinerU2.5 model download | REMOVED_OR_REJECTED | VLM is heavier and deferred until pipeline test proves environment value |
| `mineru` local parser run | REMOVED_OR_REJECTED | parser execution requires a later GC-018/work order |
| local temporary service startup | REMOVED_OR_REJECTED | source-visible behavior must remain held for runtime smoke teardown receipt |
| `mineru-api`, `mineru-router`, `mineru-gradio` | REMOVED_OR_REJECTED | API/router/Gradio lanes remain out of scope |
| Docker or WSL execution | REMOVED_OR_REJECTED | container/WSL execution is forbidden |
| config write-back receipt | CHECKER_CANDIDATE | future receipts must prove `mineru.json` changes are understood before runtime |
| output quarantine root | CHECKER_CANDIDATE | future parser outputs must stay private and outside public-sync paths |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; delegated worker executes under no-commit; reviewer/closer accepts or rejects |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=bd322a8d; executionBaseHead=worker captures at start; closureBaseHead=reviewer/closer sets before material commit |
| changedSetScope(phase) | dispatch may add only this work order and paired GC-018 baseline; worker may add only the named worker return and companion readiness matrix |
| traceScope(phase, actor) | dispatcher trace in this work order; worker trace in worker return and companion reference; reviewer trace in commit/steward evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns any material commit after review |
| crossBatchIsolation | clean worktree required before worker execution; worker must not touch session, handoff, runtime source, public, source-mirror, package install, checker, adapter, Web, MCP, or model-router paths |
| nextMoveSurfaces | reviewer/closer updates active session state only once accepted material exists; worker must not edit session state |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_COMPLETION_2026-07-03.md` (optional; prefer reviewer repair inside the worker return unless a separate completion artifact is necessary) |
| reviewerOwnedClosurePaths | worker return and companion reference named in Work-Order Fulfillment Manifest; session-sync surfaces only after material acceptance |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under the reviews directory | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, command evidence shape, and no-commit evidence shape before writing |
| companion reference under the reference directory | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

Literal-shape reminders: do not list required headings as heading-prefixed
strings before the real section; write source-not-found disposition spelling in
prose instead of the exact enum in literalTokensReviewed; avoid stale dependency
wording unless a dependency-release row cites the accepted artifact path and
commit.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_WORKER_RETURN_2026-07-03.md` | create uncommitted worker return with `Status: COMPLETE_PENDING_REVIEW` or `Status: BLOCKED_WITH_REASON` |
| `docs/reference/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_READINESS_MATRIX_2026-07-03.md` | create uncommitted companion readiness matrix with selected route token and claim boundary |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_WORKER_RETURN_2026-07-03.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

## Review Gate

Reviewer/closer must run reviewer-return steward preflight before accepting the
worker return. Reviewer may repair only allowed-scope shape defects inside the
two worker-owned outputs. Any package install, parser runtime, service startup,
document body read, public-sync, schema/writer/checker/adapter, package
mutation, Web, MCP, model-router, or action-authority need returns to
orchestrator.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Worker mode honored | PASS or BLOCKED with reason |
| Output manifest matches work order | PASS or BLOCKED with reason |
| Source verification recomputed | PASS or BLOCKED with reason |
| ModelScope route honored | PASS or BLOCKED with reason |
| Package install avoided | PASS or BLOCKED with reason |
| Parser/runtime execution avoided | PASS or BLOCKED with reason |
| Route token is one of the menu tokens | PASS or BLOCKED with reason |
| Claim boundary excludes runtime execution | PASS or BLOCKED with reason |
| Reviewer-return steward preflight | PASS or BLOCKED with reason |
| Session-sync update after material acceptance | reviewer/closer-owned only |

## Operator Checkpoint

Operator checkpoint is required before any later tranche authorizes package
installation, parser/OCR/VLM/hybrid/API/router/Gradio/Docker execution, local
temporary service startup, source document body read, derived-output inclusion
beyond metadata, public-sync, production claim, or workflow-chain completion
claim.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| modelDownloadAuthorized | CONDITIONAL_YES_MODELSCOPE_PIPELINE_ONLY |
| packageInstallAuthorized | NO |
| freshnessVerificationMode | SOURCE_VERIFIED_CONDITIONAL_DOWNLOAD_ONLY |
| reason | This work order authorizes only a command-exists-gated ModelScope pipeline model cache/download attempt; it does not authorize parser runtime, service startup, OCR, VLM, Docker, provider/live proof, or package install. |
| requiredFutureAction | If command exists and cache preparation succeeds, author a separate parser smoke work order; if command is missing, return a package-install authorization blocker. |

## Source-Intake Decision Packet Fields

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | source-mirror absorption follow-on planning |
| Negative search performed | Yes - see Negative Search And Collision Discipline |
| Disposition | RUNTIME_CANDIDATE |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R20 operator model-source hold route | `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | ENRICH_EXISTING | converts operator ModelScope choice into a bounded command-exists cache-prep gate | execute R21 worker |
| MinerU model-source and config write-back facts | `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | ENRICH_EXISTING | sharpens ModelScope test route and config receipt requirements | source-verify and classify |
| MinerU package install | `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | REJECT_DIRECT_IMPORT | package lifecycle remains unauthorized in this tranche | forbid install |
| MinerU parser runtime | `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | REJECT_DIRECT_IMPORT | parser runtime remains unauthorized until a later work order | forbid execution |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA_R21_T1 MinerU ModelScope Test Cache Preparation And Runtime Smoke Gate dispatch, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, `Get-Content`, `python governance/compat/build_dispatch_packet_scaffold.py`, `apply_patch` |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_2026-07-03.md` |
| Allowed scope source | active next allowed move after session-sync commit `bd322a8d`, accepted MSEA-R20-T1 route token, and operator ModelScope test-first choice |
| Before status evidence | `git rev-parse --short HEAD` returned `bd322a8d`; clean worktree confirmed because `git status --short` was empty |
| After status evidence | two new dispatch artifacts passed pre-dispatch autorun gate |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator chose ModelScope for test-first MinerU preparation after R20 held on model-source choice |
| Claim boundary | dispatch authoring and conditional model-cache preparation only |
| Agent type | dispatcher |
| Invocation ID | `msea-r21-t1-dispatch-2026-07-03` |
| Expected manifest | the two dispatch artifacts named in Target paths |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R21_T1_MINERU_MODELSCOPE_TEST_CACHE_PREPARATION_AND_RUNTIME_SMOKE_GATE_2026-07-03.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | MSEA-R21-T1 dispatch authoring for MinerU ModelScope pipeline model-cache preparation gate |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, parser runtime, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - only future worker command/cache/config evidence may exist |
| actionEvidence | CLAIM_REJECTED_NO_ACTION - dispatch itself performs no model download or parser/service action |
| invocationBoundary | delegated worker may perform source verification, read-only metadata, and the single conditional ModelScope pipeline cache-prep command only if the command already exists |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | cache-prep gate, conditional command evidence, route selection, and hold/open decision only |
| forbiddenExpansion | Do not expand into package install, parser/OCR/VLM/API/Docker/service/provider/live/public/package/Web/MCP/model-router behavior without fresh source-verified authorization |

## Acceptance Criteria

| Criterion | Required evidence |
| --- | --- |
| Worker obeys no-commit mode | worker return includes `WORKER_MUST_NOT_COMMIT honored`, changed files, and actual `git status --short` |
| Worker creates only authorized outputs | worker return and companion matrix paths match Work-Order Fulfillment Manifest |
| Source facts are re-read | worker output Source Inventory lists R20/R17 and MinerU source mirror docs/source used |
| ModelSource route is explicit | output records `modelSourceRoute: modelscope` and no auto mode |
| Download command is gated | command is run only if `mineru-models-download` exists; otherwise no install occurs |
| Pipeline-only scope is honored | no VLM/MinerU2.5 download in this tranche |
| Runtime actions stay blocked | no parser/OCR/VLM/API/router/Gradio/Docker/WSL/service/document-body action occurs |
| Privacy boundary is preserved | no document body content, raw secrets, original document copy/import, public-sync, or sensitive legal details in committed artifacts |
| Gates pass | worker-return fast gate and pre-implementation autorun pass before handoff or report the blocker |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if:

- Candidate Group A authority is missing or contradicted;
- pinned MinerU source mirror is missing or drifted beyond citation repair;
- `mineru-models-download` is missing or requires package install;
- the ModelScope command fails and cannot be classified safely within one attempt;
- useful completion requires parser/OCR/VLM/API/router/Gradio/Docker/WSL/service execution;
- useful completion requires document body read, fuller content inclusion, source import, or forbidden path edits;
- required output artifacts cannot pass worker-return fast gate after allowed-scope repairs.

## Claim Boundary

This work order authorizes only source-verified ModelScope pipeline model-cache
preparation and route selection for a future private MinerU parser smoke pilot.
It does not authorize MinerU package install, parser/OCR/VLM/hybrid/API/router/
Gradio/Docker execution, local temporary service startup, provider/live proof,
S3/RAG, source document copy/import, fuller content quotation, schema/writer/
adapter/checker implementation, package activation, public-sync, benchmark,
document-truth, extraction-accuracy, legal advice quality, current-law
correctness, production readiness, action authority, or workflow-chain
completion claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Candidate Group A source documents and this internal runtime-precondition
lane are authorized only for local private CVF testing. No public-sync export is
authorized.
