# CVF GC-018 Baseline - RSPB-AI-T2 Capability Environment Snapshot Doctor Enrichment And Pre-Dispatch Consumer Implementation

Memory class: governed-dispatch-baseline

rawMemoryReleased=false

Status: REVIEWER_ACCEPTED_DISPATCH_READY

docType: baseline

Date: 2026-08-16

Batch ID: RSPB-AI-T2

Dispatch base head: `c849677d2`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Dispatcher/reviewer/closer: role-separated governed agents

Worker target: one bounded Python source-and-test implementation worker

## Purpose

Authorize the smallest accepted RSPB snapshot slice: enrich the existing
`scripts/cvf_doctor.py` owner with a secret-free, non-mutating capability
snapshot mode; add isolated tests for availability, unknown-state, redaction,
and TTL behavior; and make the existing release-gate bundle consume that
snapshot before starting expensive work. No candidate scanner import or
parallel owner is authorized.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RSPB-AI-T2 --title "Capability Environment Snapshot Doctor Enrichment And Pre-Dispatch Consumer Implementation" --date 2026-08-16 --base c849677d2 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the accepted T1 owner decision, exact three-path source/test manifest, focused test matrix, no-mutation boundary, and worker-return contract |
| checkerReadAheadConfirmation | work-order dispatch, prompt-envelope, operation-trace, epistemic-process, public-disposition, file-size, and worker-return guards reviewed; dual-agent matrix standard reviewed because its checker remains a documented candidate |
| docOnlyNewFields | none |
| claimBoundary | dispatch authoring evidence only; runtime behavior remains pending worker implementation and independent review |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Source Verification columns; no-commit profile; review headings; Agent Operation Trace fields; Dual Agent dispositions; Public Export Disposition |
| gateRunPurpose | confirm source-backed packet shape after authoring |
| claimBoundary | baseline and companion work order only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "runtime implementation" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned none |
| Dispatch impact | no additional ADIF-specific constraint; canonical guards still apply |

## Authorization / Source

| Authority | Evidence | Disposition |
|---|---|---|
| T1 owner reconciliation | `docs/reference/capability_preflight_bootstrap/CVF_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_CONTRACT.md` at material commit `d591c542a` | PASS |
| T1 independent completion | `docs/reviews/CVF_RSPB_AI_T1_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_AND_READ_ONLY_SNAPSHOT_VALUE_PROBE_COMPLETION_2026-08-16.md` at material commit `d591c542a` | PASS |
| operator implementation checkpoint | explicit `next` instruction on 2026-08-16 after the T1 closure | PASS |
| clean dispatch base | `git status --short` empty at `c849677d2` | PASS |

## Decision / Baseline

Proceed with one no-commit implementation worker. Reuse the doctor and release
bundle owners. Keep acquisition, mutation, candidate-code execution, secrets,
network/provider use, public sync, deployment, and production outside scope.

## Scope / Owner Boundary

The doctor remains the only environment-observation owner. The release bundle
is a bounded consumer, not a new authority owner. Snapshot evidence can stop a
workflow for missing, unknown, or stale prerequisites; it cannot grant
capability, execution, mutation, activation, approval, or deployment authority.

## Allowed Paths

1. `scripts/cvf_doctor.py`
2. `scripts/run_cvf_release_gate_bundle.py`
3. `scripts/test_cvf_doctor_snapshot.py`
4. `docs/reviews/CVF_RSPB_AI_T2_CAPABILITY_ENVIRONMENT_SNAPSHOT_DOCTOR_ENRICHMENT_AND_PRE_DISPATCH_CONSUMER_IMPLEMENTATION_WORKER_RETURN_2026-08-16.md`

## Forbidden Actions

- no import, copy, execution, or adaptation-by-copy of the predecessor
  candidate scanner implementation;
- no environment-variable enumeration, `.env` bootstrap in snapshot mode,
  credential/secret status, raw executable path, full PATH, socket/port probe,
  filesystem write probe, network/provider call, package install, or repair;
- no changes to Guard Contract, Execution Plane, setup workflow, route,
  registry, CLI/MCP adapter, public catalog, continuity, hook, or checker;
- no live release run, public sync, push, deployment, or production action;
- no worker staging or commit.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| doctor already owns bounded command discovery/version checks | RUNTIME_BEHAVIOR | `scripts/cvf_doctor.py` | lines 32-48 and 71-110 | `command_version`; `build_checks` | CVF doctor | ACCEPT |
| current doctor full mode performs env bootstrap and mutating/network-adjacent checks | RISK_FACT | `scripts/cvf_doctor.py` | lines 51-68 and 203-217 | `is_port_listening`; `path_writable`; `bootstrap_repo_env` | CVF doctor full mode | ACCEPT |
| release bundle starts expensive checks eagerly | RUNTIME_BEHAVIOR | `scripts/run_cvf_release_gate_bundle.py` | lines 628-647 | `main`; `check_web_build`; `check_e2e`; `check_sot3` | release-gate bundle | ACCEPT |
| selected minimal contract requires AVAILABLE/MISSING/UNKNOWN, short TTL, redaction, and evidence/authority separation | GOVERNED_DECISION | `docs/reference/capability_preflight_bootstrap/CVF_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_CONTRACT.md` | lines 160-208 | Minimal CVF-Native Snapshot Contract | capability preflight reconciliation | ACCEPT |
| current owner decision is enrich doctor and use a pre-dispatch consumer | GOVERNED_DECISION | `docs/reviews/CVF_RSPB_AI_T1_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_AND_READ_ONLY_SNAPSHOT_VALUE_PROBE_COMPLETION_2026-08-16.md` | lines 79-89 | `PROCEED_TO_IMPLEMENTATION_WORK_ORDER` | T1 independent completion | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| dispatch paths | both proposed packet paths were absent before authoring | PASS |
| new test and worker-return paths | both paths were absent before authoring | PASS |
| owner collision | repo source inspection found the existing doctor and release-bundle owner; no new scanner owner is permitted | PASS |
| clean base | HEAD `c849677d2`; status empty before authoring | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | `scripts/cvf_doctor.py` and release-bundle preflight consumer | local read-only evidence may fail closed; never grants authority | focused unit tests and independent review | repository-native Python only | IMPLEMENTED |
| EXTERNAL_AGENT_CLI_MCP | doctor command-line JSON output | read-only local CLI invocation only; no MCP, authentication, mutation, or remote support | CLI schema tests | CLI output is in scope; MCP adapter is explicitly deferred | CONTRACT_ONLY |

## Evidence / Verification

Required proof is hermetic Python unit testing, syntax compilation, doctor
snapshot CLI smoke output, release-bundle dry-run compatibility, file-size and
worker-return gates, and independent reviewer recomputation. No live/provider
proof is authorized, so this tranche cannot claim production readiness.

## Risk / Corrective Action

Primary risks are secret/path leakage, mutation hidden inside a diagnostic,
incorrectly classifying a failed version probe as available, stale evidence,
and running expensive release checks despite preflight failure. Controls are
an exact allow-list, no env bootstrap in snapshot mode, redacted path classes,
injected time, fail-closed UNKNOWN/expiry, short-circuit consumer tests, and a
four-path manifest.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: T1 already normalized the evidence into repo-local authority |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T1 contract and independent completion |
| Disposition | NOT_APPLICABLE_WITH_REASON: no new intake in T2 |
| Claim boundary | implementation consumes accepted CVF artifacts only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime implementation dispatch; public sync is not
authorized in this tranche.

## Claim Boundary

This baseline authorizes a later no-commit source/test implementation worker
for the four listed outputs only. It does not prove runtime correctness before
review, grant capability authority, activate candidate code, or authorize
live/provider/public/deployment/production behavior.
