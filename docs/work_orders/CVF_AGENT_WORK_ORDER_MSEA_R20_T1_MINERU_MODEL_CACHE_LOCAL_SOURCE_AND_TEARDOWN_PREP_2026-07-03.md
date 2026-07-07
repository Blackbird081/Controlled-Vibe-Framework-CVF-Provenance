# CVF Agent Work Order - MSEA-R20-T1 MinerU Model Cache Local Source And Teardown Prep

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R20_T1

Dispatch base head: a093405d

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_WORKER_RETURN_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R20_T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker must capture `git rev-parse --short HEAD` before edits.

Current-time notes: artifact date is 2026-07-03; use current repository state and pinned MinerU source mirror, not stale chat memory.

Do-not-misread notes: this packet opens model-cache/local-source and temporary-service teardown prep planning only; it does not authorize running MinerU, importing MinerU, installing packages, downloading models, starting a local service, running Docker, reading document body content, creating extraction outputs, public-sync, schema/writer/adapter/checker implementation, document-truth, extraction-accuracy, legal advice, current-law, production, or workflow-chain claims.

Required first actions: read startup files, guard orientation, literal gotchas, this work order, the paired GC-018 baseline, source references, and checker source listed in the Checker Source Read-Ahead Block before writing worker outputs.

Return contract: create the worker return and companion readiness matrix, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create a source-verified prep matrix for MinerU model source/cache selection,
local model path readiness, config write-back risk, output quarantine, and
temporary-service teardown receipts before any private local runtime smoke
pilot is authorized.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R20_T1 --title "MinerU Model Cache Local Source And Service Teardown Prep Planning" --date 2026-07-03 --base a093405d --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed scaffold fields, set DISPATCH_READY, added R19 dependency release, source-verified MinerU model-source/cache/service facts, evidence-reuse plan, worker-output shape mandate, route tokens, and runtime hold boundaries. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`. |
| docOnlyNewFields | selectedRouteToken; modelSourceChoiceStatus; localModelPathStatus; mineruConfigWritebackRisk; temporaryServiceTeardownReceipt; runtimeSmokePilotReadiness |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, missing source mirror,
missing Candidate Group A authority, forbidden-scope need, or missing local
permission that makes completion impossible.

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition |
| --- | --- | --- | --- |
| MSEA-R19-T1 accepted route selection | `docs/reviews/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` | `707953bc` | SATISFIED - selected route token `OPEN_MODEL_CACHE_AND_LOCAL_SOURCE_PREP_WORK_ORDER_FIRST` releases this prep work order |
| Session next-move freshness | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V34_2026-07-03.md` | `a093405d` | SATISFIED - next allowed move permits fresh GC-018/source-verified work order for model cache, local-source preparation, and temporary-service teardown receipt planning |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | Worker output checker read-ahead is mandatory; provider-local authority is excluded; runtime candidates are classified without execution; source verification symbol cells use real symbols or sections only. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; Evidence Reuse And Encoding Plan fields; ADIF resolver query exactness; Dependency Release Evidence; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields; Worker Return Packet Shape Contract fields; Source-Intake Decision Packet Fields; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; Target / Source; Scope / Applies To; Rescan Intelligence Hardening; ledger terminal marker; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; Delta block field labels; Agent Operation Trace labels. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm this work order's dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this work order and paired baseline only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R20-T1 must re-read current CVF-governed sources, accepted R19 artifacts, pinned MinerU source mirror docs, and read-only local metadata before selecting the next route.

unicodePathHandling: Use LiteralPath and UTF-8-safe command output for local paths; do not normalize or rewrite filenames.

extractedTextAuthority: N/A with reason

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` |
| priorVerificationAnchor | `## Route Decision Menu Selection` |
| recomputeReason | R20-T1 must re-read current CVF-governed sources, accepted R19 artifacts, pinned MinerU source mirror docs, and read-only local metadata before selecting the next route |
| freshRecomputeRequired | true for source facts and read-only metadata only; no document body read and no MinerU extraction |
| unicodePathHandling | Use `-LiteralPath` and UTF-8-safe command output for local paths; do not normalize or rewrite filenames |
| extractedTextAuthority | N/A with reason: R20-T1 must not read document body text or treat extracted text as authority |

## Operator Authorization And Privacy Boundary

Candidate Group A source documents are authorized for local private CVF testing
only. Original documents must not be public-synced or redistributed. This
tranche may plan a future runtime smoke pilot but must not create extraction
outputs, copy source documents into the repository, read source document body
content, or include sensitive personal/legal details in committed artifacts.

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R19 accepted route opens model cache and local-source prep before runtime smoke | VALUE_SET | VALUE_SET | `docs/reviews/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_PLANNING_WORKER_RETURN_2026-07-03.md` | `## Reviewer Decision / Closure Disposition` | `OPEN_MODEL_CACHE_AND_LOCAL_SOURCE_PREP_WORK_ORDER_FIRST` | MSEA-R19-T1 worker return | ACCEPT |
| R19 readiness matrix selected the same model-cache/local-source prep route | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` | `## Route Decision Menu Selection` | `OPEN_MODEL_CACHE_AND_LOCAL_SOURCE_PREP_WORK_ORDER_FIRST` | MSEA-R19-T1 readiness matrix | ACCEPT |
| Candidate Group A remains private local CVF testing only | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | `## Claim Boundary` | Candidate Group A | MSEA-R17-T1 intake ledger | ACCEPT |
| MinerU source mirror remains the upstream authority for this lane | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `opendatalab__MinerU` | source mirror index | ACCEPT |
| MinerU can automatically start a local temporary service when no API URL is provided | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 146 | `mineru` | upstream README | ACCEPT |
| MinerU CLI supports a pipeline command envelope for local input and output paths | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | lines 332-336 | `mineru -p <input_path> -o <output_path> -b pipeline` | upstream README | ACCEPT |
| MinerU input may be local files or directories through supported surfaces | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | line 339 | local files or directories | upstream README | ACCEPT |
| MinerU model source uses accepted environment values and environment priority | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 12 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| MinerU unset model source reads `model-source` and may write back resolved source | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 26 | `model-source` | model source documentation | ACCEPT |
| MinerU model download writes model path and source to `mineru.json` | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 44 | `mineru.json` | model source documentation | ACCEPT |
| MinerU model updates can redownload to default location and update config | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 48 | `mineru-models-download` | model source documentation | ACCEPT |
| MinerU model download command must use a remote source and ignores local mode for that invocation | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | line 49 | `mineru-models-download` | model source documentation | ACCEPT |
| MinerU local model mode can be requested through the environment variable | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/usage/model_source.md` | lines 53-56 | `MINERU_MODEL_SOURCE` | model source documentation | ACCEPT |
| Docker deployment is limited to Linux and Windows with WSL2 | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/quick_start/docker_deployment.md` | line 6 | Docker deployment | Docker deployment documentation | ACCEPT |

## New Doc-Only Fields

| Field | Meaning | Disposition |
| --- | --- | --- |
| selectedRouteToken | Worker-selected next-route token for reviewer/closer consideration | DOC_ONLY_NEW |
| modelSourceChoiceStatus | Worker classification of whether operator has chosen `huggingface`, `modelscope`, `local`, or held auto mode | DOC_ONLY_NEW |
| localModelPathStatus | Worker classification of whether local model path proof exists | DOC_ONLY_NEW |
| mineruConfigWritebackRisk | Worker classification of config mutation risk for later runtime work | DOC_ONLY_NEW |
| temporaryServiceTeardownReceipt | Worker-defined future receipt fields for service detection and cleanup | DOC_ONLY_NEW |
| runtimeSmokePilotReadiness | Worker classification of whether later runtime smoke dispatch is ready | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Existing MSEA-R20 artifacts | negative search for `MSEA_R20_T1`, `MSEA-R20-T1`, `MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP`, and `Model Cache Local Source And Teardown Prep` across governed docs, session state, governance, and the source mirror index returned no matches before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Dispatch packet path check | Planned baseline, work order, worker return, and companion reference paths all returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| Collision decision | MSEA-R20-T1 is a new child tranche after accepted MSEA-R19-T1 route selection | SAFE_TO_CREATE |

## Authority Chain

- Operator instruction: continue after accepted MSEA-R19-T1 and complete this tranche in multiple roles.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V34_2026-07-03.md`.
- Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_2026-07-03.md`.
- Accepted R19 route selection and readiness matrix.
- Candidate Group A private intake: `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md`.
- MinerU source authority: `.private_reference/source_mirrors/opendatalab__MinerU/`.

Authority boundary: if any source contradicts this packet, stop and return
`BLOCKED_WITH_REASON`. The worker may not upgrade planning language into
runtime authority.

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
| Operator | operator | owns later runtime, model-download, local-source, document-body, public-sync, and production decisions |
| Dispatcher | dispatcher role | authors this GC-018/work order and runs pre-dispatch gates |
| Worker | delegated worker role | creates only the named worker return and companion readiness matrix, without commit |
| Reviewer/closer | reviewer/closer | reviews returned artifacts, repairs allowed-scope shape defects if needed, commits material if accepted |
| Session-sync steward | reviewer/closer once material is accepted | updates active session state once accepted material exists |

## Pre-Flight Checks

Required before worker execution:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path 'docs\reviews\CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_WORKER_RETURN_2026-07-03.md'
Test-Path 'docs\reference\CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected result: clean worktree at execution start, planned worker outputs
absent before writing, and pre-implementation gate passing after worker output
authoring and allowed-scope repairs.

## Write Ownership

| Path family | Worker permission |
| --- | --- |
| `docs/reviews/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_WORKER_RETURN_2026-07-03.md` | CREATE_ONLY_UNCOMMITTED |
| `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | CREATE_ONLY_UNCOMMITTED |
| session-state, front-door, and active-handoff surfaces | FORBIDDEN |
| `.private_reference/source_mirrors/**` | READ_ONLY |
| runtime, package, source, public-sync, Web, MCP, model-router, checker, adapter paths | FORBIDDEN |

## Execution Plan

1. Capture `executionBaseHead` and current worktree status.
2. Complete Required First Reads and checker-source read-ahead.
3. Recompute source facts from R19/R17 and the pinned MinerU mirror.
4. Run only allowed read-only metadata commands.
5. Author the worker return and companion readiness matrix.
6. Run worker-return fast gate and pre-implementation autorun.
7. Leave changes uncommitted and return the status token.

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| Base and worktree status | `executionBaseHead`, `git status --short`, and actual changed file list |
| Source verification | Source Inventory plus Source Verification Block in worker outputs |
| Local metadata | Command/result table, with no secrets or document content printed |
| Runtime non-execution | Explicit statement that no MinerU import, command, install, model download, service startup, Docker run, or extraction output occurred |
| Route decision | exactly one `selectedRouteToken` in both worker return and companion matrix |
| Gates | worker-return fast gate and pre-implementation autorun output |

## Allowed Read-Only Local Metadata

The worker may run only metadata/read-only commands needed to classify the
current host for a later runtime pilot. Allowed examples:

- `git rev-parse --short HEAD`
- `git status --short`
- `python --version`
- `where python`
- `Get-Command docker -ErrorAction SilentlyContinue`
- `Get-Command wsl -ErrorAction SilentlyContinue`
- `Get-ChildItem Env:MINERU_MODEL_SOURCE -ErrorAction SilentlyContinue`
- `Test-Path` for proposed private output roots or existing local document paths
- `Get-ChildItem Env:USERPROFILE -ErrorAction SilentlyContinue` without printing secrets

Forbidden even for metadata:

- importing MinerU modules;
- invoking `mineru`, `mineru-api`, `mineru-router`, `mineru-gradio`, or `mineru-models-download`;
- running `pip`, `uv`, `conda`, Docker containers, WSL commands, API calls, model downloads, parser/OCR/VLM/hybrid execution, or any command that creates extraction outputs or starts local services;
- printing secret values or document body content.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intakeRole | dispatcher-authored private runtime-precondition planning work order |
| scope classification | bounded private planning and read-only metadata; changed paths limited to the two worker outputs |
| workerRole | no-commit source verifier, model-cache/local-source readiness matrix author, and route selector |
| reviewerRole | reviewer/closer validates worker return and companion readiness matrix |
| operatorRole | owns any later runtime, installation, model-download, fuller-content, public-sync, provider, or production decision |
| route mode | MULTI_AGENT_SINGLE_ROLE |
| routeDecision | proceed with model/cache/local-source/teardown prep; hold all runtime execution |
| escalationCondition | source contradiction, need to run MinerU, need to install/download/start services, need to read document body content, need to quote fuller content, or need to edit forbidden paths |
| claimBoundary | role routing only; no automatic execution, provider routing, public export, or production claim |

## Route Decision Menu

Worker must select exactly one `selectedRouteToken`:

| Token | Meaning |
| --- | --- |
| OPEN_MSEA_R21_LOCAL_RUNTIME_SMOKE_PILOT_WORK_ORDER | A future local runtime smoke pilot work order can be authored, still requiring fresh runtime authorization before execution |
| HOLD_PENDING_OPERATOR_MODEL_SOURCE_CHOICE | Operator must choose remote source, local source path, or auto/config write-back risk before runtime can proceed |
| HOLD_PENDING_LOCAL_MODEL_PATH_OR_CACHE_PROOF | Local-source path or model-cache evidence remains missing |
| HOLD_RUNTIME_PENDING_SERVICE_TEARDOWN_RECEIPT | Temporary service detection and teardown receipt remains insufficiently specified |
| HOLD_ALL_RUNTIME_LANES | No source-backed runtime-adjacent lane is ready |

## Required Worker Analysis

1. Re-read R19 worker return and matrix; summarize why model-cache/local-source prep was selected.
2. Re-read R17 privacy boundary and R12/R18 runtime gating policy as needed.
3. Re-read pinned MinerU source mirror docs for model source, config write-back,
   model-download behavior, local-model mode, pipeline command envelope, input
   surfaces, Docker/WSL2 boundary, and local temporary service behavior.
4. Perform read-only local metadata only from the allowed command list.
5. Produce a companion readiness matrix with:
   - model source choice posture;
   - local model path or cache posture;
   - MinerU config write-back risk posture;
   - temporary service detection and teardown receipt fields;
   - output quarantine posture;
   - privacy/redaction posture;
   - forbidden runtime action checklist;
   - selected route token and rationale.
6. Do not include document body content, raw secrets, or source file copies.

## Runtime Candidate Parking Checks

| Candidate | Required disposition for this tranche | Reason |
| --- | --- | --- |
| MinerU install or package activation | REMOVED_OR_REJECTED | package lifecycle mutation is outside this planning tranche |
| model download | REMOVED_OR_REJECTED | model lifecycle may be planned, but download is forbidden |
| `mineru` local parser run | REMOVED_OR_REJECTED | execution requires a later GC-018/work order |
| local temporary service startup | RUNTIME_CANDIDATE | source-visible behavior must be planned for detection and teardown before any later run |
| `mineru-api`, `mineru-router`, `mineru-gradio` | REMOVED_OR_REJECTED | API/router/Gradio lanes remain out of scope |
| Docker deployment | REMOVED_OR_REJECTED | Docker/WSL2 may be classified, but container execution is forbidden |
| output quarantine root | CHECKER_CANDIDATE | future receipts must prove outputs stay private and outside public-sync paths |
| service teardown receipt | CHECKER_CANDIDATE | future runtime smoke pilot should have machine-checkable stop/cleanup evidence |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; delegated worker executes under no-commit; reviewer/closer accepts or rejects |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=a093405d; executionBaseHead=worker captures at start; closureBaseHead=reviewer/closer sets before material commit |
| changedSetScope(phase) | dispatch may add only this work order and paired GC-018 baseline; worker may add only the named worker return and companion readiness matrix |
| traceScope(phase, actor) | dispatcher trace in this work order; worker trace in worker return and companion reference; reviewer trace in commit/steward evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns any material commit after review |
| crossBatchIsolation | clean worktree required before worker execution; worker must not touch session, handoff, runtime, public, source-mirror, package, or checker paths |
| nextMoveSurfaces | reviewer/closer updates active session state only once accepted material exists; worker must not edit session state |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_COMPLETION_2026-07-03.md` (optional; prefer reviewer repair inside the worker return unless a separate completion artifact is necessary) |
| reviewerOwnedClosurePaths | worker return and companion reference named in Work-Order Fulfillment Manifest; session-sync surfaces only after material acceptance |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under the reviews directory | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| companion reference under the reference directory | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

Literal-shape reminders: do not list required headings as backticked heading
strings before the real section; write source-not-found disposition spelling in
prose instead of the exact blocked enum in literalTokensReviewed; avoid stale
dependency wording unless a dependency-release row cites the accepted artifact
path and commit.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_WORKER_RETURN_2026-07-03.md` | create uncommitted worker return with `Status: COMPLETE_PENDING_REVIEW` or `Status: BLOCKED_WITH_REASON` |
| `docs/reference/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_READINESS_MATRIX_2026-07-03.md` | create uncommitted companion readiness matrix with selected route token and claim boundary |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_WORKER_RETURN_2026-07-03.md`

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
two worker-owned outputs. Any runtime, install, model download, local service,
document body, public-sync, schema/writer/checker/adapter, package, Web, MCP,
model-router, or action-authority need returns to orchestrator.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Worker mode honored | PASS or BLOCKED with reason |
| Output manifest matches work order | PASS or BLOCKED with reason |
| Source verification recomputed | PASS or BLOCKED with reason |
| Read-only metadata stayed bounded | PASS or BLOCKED with reason |
| Route token is one of the menu tokens | PASS or BLOCKED with reason |
| Claim boundary excludes runtime execution | PASS or BLOCKED with reason |
| Reviewer-return steward preflight | PASS or BLOCKED with reason |
| Session-sync update after material acceptance | reviewer/closer-owned only |

## Operator Checkpoint

Operator checkpoint is required before any later tranche authorizes MinerU
installation, model download, local service startup, parser/OCR/VLM/hybrid/API/
router/Gradio/Docker execution, source document body read, derived-output
inclusion beyond metadata, public-sync, production claim, or workflow-chain
completion claim.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Source-Intake Decision Packet Fields

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | source-mirror absorption follow-on planning |
| Negative search performed | Yes - see Negative Search And Collision Discipline |
| Disposition | ADAPT |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R19 model/cache/local-source route | `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` | ENRICH_EXISTING | converts route selection into a worker-owned prep matrix | execute planning only |
| MinerU model-source and config write-back facts | `docs/reference/CVF_MSEA_R19_T1_MINERU_LOCAL_EXTRACTION_ENVIRONMENT_MODEL_LIFECYCLE_AND_SERVICE_TEARDOWN_READINESS_MATRIX_2026-07-03.md` | ENRICH_EXISTING | sharpens model-cache and local-source readiness before runtime | source-verify and classify |
| MinerU runtime execution | `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | REJECT_DIRECT_IMPORT | runtime remains unauthorized in this tranche | forbid execution |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA_R20_T1 MinerU Model Cache Local Source And Teardown Prep dispatch, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, `Get-Content`, `python governance/compat/build_dispatch_packet_scaffold.py`, `apply_patch` |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R20_T1_MINERU_MODEL_CACHE_LOCAL_SOURCE_AND_TEARDOWN_PREP_2026-07-03.md` |
| Allowed scope source | active next allowed move after session-sync commit `a093405d` and accepted MSEA-R19-T1 route token |
| Before status evidence | `git rev-parse --short HEAD` returned `a093405d`; clean worktree confirmed because `git status --short` was empty |
| After status evidence | two new dispatch artifacts pending gate confirmation |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator said to close the tranche in multiple roles after R19 acceptance; active next allowed move authorizes fresh GC-018/source-verified work order for model-cache/local-source/teardown prep |
| Claim boundary | dispatch authoring and planning-only worker assignment |
| Agent type | dispatcher |
| Invocation ID | `msea-r20-t1-dispatch-2026-07-03` |
| Expected manifest | the two dispatch artifacts named in Target paths |
| Actual changed set | pending pre-dispatch gate confirmation |
| Manifest delta | pending pre-dispatch gate confirmation |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | MSEA-R20-T1 dispatch authoring for MinerU model-cache/local-source and teardown prep planning |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | delegated worker may perform source verification and read-only local metadata only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | planning, readiness matrix, and route selection only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without a fresh source-verified authorization |

## Acceptance Criteria

| Criterion | Required evidence |
| --- | --- |
| Worker obeys no-commit mode | worker return includes `WORKER_MUST_NOT_COMMIT honored`, changed files, and actual `git status --short` |
| Worker creates only authorized outputs | worker return and companion matrix paths match Work-Order Fulfillment Manifest |
| Source facts are re-read | worker output Source Inventory lists R19/R17 and MinerU source mirror docs used |
| Read-only metadata stays bounded | worker output names commands used and confirms no install, import, model download, service start, Docker run, parser/OCR run, or extraction output |
| Route decision is explicit | companion matrix includes exactly one `selectedRouteToken` from Route Decision Menu |
| Privacy boundary is preserved | no document body content, raw secrets, original document copy/import, public-sync, or sensitive legal details in committed artifacts |
| Gates pass | worker-return fast gate and pre-implementation autorun pass before handoff or report the blocker |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if:

- Candidate Group A authority is missing or contradicted;
- pinned MinerU source mirror is missing or drifted beyond citation repair;
- a useful answer requires MinerU execution, install, model download, service
  startup, Docker/WSL execution, API/router/Gradio use, or document body read;
- required output artifacts cannot pass worker-return fast gate after
  allowed-scope repairs;
- local metadata would require printing secrets or sensitive document content.

## Claim Boundary

This work order authorizes only source-verified planning and read-only local
metadata for a future private MinerU runtime smoke pilot. It does not authorize
MinerU install, import, model download, parser/OCR/VLM/hybrid/API/router/
Gradio/Docker execution, local temporary service startup, provider/live proof,
S3/RAG, source document copy/import, fuller content quotation, schema/writer/
adapter/checker implementation, package activation, public-sync, benchmark,
document-truth, extraction-accuracy, legal advice quality, current-law
correctness, production readiness, action authority, or workflow-chain
completion claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Candidate Group A source documents and this internal runtime-precondition
planning lane are authorized only for local private CVF testing. No public-sync
export is authorized.
