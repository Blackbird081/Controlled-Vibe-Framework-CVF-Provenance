# CVF GC-018 Baseline - CADP AI T5 R2 Transport-Neutral External Readout Adapter Foundation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: CADP-AI-T5-R2

Date: 2026-08-15

Dispatch base head: `9ed651abd5c3bc0d291ae7b1902012cc6d5f132f`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Independent reviewer/closer

Worker target: transport-neutral contract worker role

## Purpose

Authorize a bounded second T5 slice that creates a pure, transport-neutral
adapter contract over the accepted T5-R1 authority foundation and makes that
contract discoverable through the Guard Contract package root. The tranche
may prove validation ordering, fail-closed response composition, literal-false
authority, and package-root export integrity. It does not register or invoke
an MCP tool or CLI command and does not lift the external-agent invocation
moratorium.

## Authorization

The active bootstrap read model, session front door, and active handoff name a
fresh CADP-AI-T5-R2 dispatch as the only next move. The operator's explicit
continuation instruction
instruction releases dispatch authoring, while implementation remains
forbidden until this GC-018 baseline and its paired work order are independently
reviewed and committed.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind mcp-cli-adapter --batch-id CADP-AI-T5-R2 --title "CADP AI T5 R2 Transport-Neutral External Readout Adapter Foundation" --date 2026-08-15 --base 9ed651abd5c3bc0d291ae7b1902012cc6d5f132f --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CADP-AI-T5-R1 authority foundation accepted bounded at 7d96fa115" --dependency "CADP-AI-T5D adapter decision accepted deferred at ef84a1f6a" --include-worker-return-skeleton --stdout` |
| generatedProfile | mcp-cli-adapter plus `WORKER_MUST_NOT_COMMIT` no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | resolved all generated placeholders; narrowed the packet to an exact seven-path worker manifest; added source verification, ADIF disclosure, transport-neutral contract requirements, dual-surface accounting, and explicit moratorium controls |
| checkerReadAheadConfirmation | read applicable dispatch, source-verification, scaffold-provenance, ADIF, trace, handoff, Markdown, Delta-boundary, and foundation-storage checker sources before authoring |
| docOnlyNewFields | `transportFoundationDisposition`; `packageRootDisposition`; no runtime schema field is introduced by this baseline |
| claimBoundary | dispatch-authoring provenance only; no adapter runtime, provider, live, public, MCP, CLI, credential, or invocation behavior claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| T5-R1 authority foundation | `docs/reviews/CVF_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_COMPLETION_2026-08-15.md`, accepted bounded at material commit `7d96fa115eece9e76b913d4568e49e9c1c3f4dab` | rows 1-7 and 9 accepted bounded; row 8 remains deferred and may be addressed only by a fresh packet | ACCEPT |
| T5D adapter decision | `docs/reviews/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_COMPLETION_2026-08-14.md`, bounded deferred decision; material anchor `ef84a1f6a` | a later slice must remain source-verified and must not treat decision evidence as runtime authority | ACCEPT |
| Invocation moratorium remains active | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md`, Roadmap Release Rules | no MCP/CLI registration, launch, or invocation is permitted in this tranche | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json`

Returned defects: 22, not truncated.

Disclosed defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021,
ADIF-0024, ADIF-0028, ADIF-0029, ADIF-0031, ADIF-0033, ADIF-0039,
ADIF-0043, ADIF-0044, ADIF-0045, ADIF-0049, ADIF-0051, ADIF-0052.

Dispatch impact: use exact source symbols and paths; preserve role/commit
boundaries; require output-specific checker read-ahead; prohibit provider-local
authority; keep the writable manifest atomic; record CWD, final status, and
command signatures; do not mix session/protected paths into worker scope.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_cadp_authority_boundary_drift.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; canonical Source Verification columns and ACCEPT disposition; Scaffold Provenance fields; full ADIF query/disclosure; eight Delta fields; seventeen trace fields; no-commit handoff/conversion fields; work-order structural headings; Foundation Storage Layout Block |
| gateRunPurpose | confirm packet structure and authority evidence before pre-dispatch; not discover requirements after dispatch |
| claimBoundary | checker conformity proves packet shape only; it does not prove future adapter semantics or external availability |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T5-R1 exposes strict ingress validation | source fact | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.ts` | function beginning at line 372 | `validateCadpExternalReadoutIngress` | T5-R1 external-readout foundation | ACCEPT |
| T5-R1 exposes exact metadata allowlist validation | source fact | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.ts` | function beginning at line 462 | `validateCadpExternalReadoutAllowlistedMetadata` | T5-R1 external-readout foundation | ACCEPT |
| T5-R1 exposes secret/private-provenance rejection | source fact | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.ts` | function beginning at line 429 | `redactCadpExternalReadoutPayload` | T5-R1 external-readout foundation | ACCEPT |
| T5-R1 exposes freshness evaluation | source fact | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.ts` | function beginning at line 537 | `evaluateCadpExternalReadoutFreshness` | T5-R1 external-readout foundation | ACCEPT |
| Guard Contract package root is explicit | source fact | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` | `main`, `types`, and exports `.` | `src/index.ts` | npm package export map | ACCEPT |
| Guard Contract root does not yet export T5-R1 symbols | bounded source fact | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | current barrel export surface | `createGuardEngine` | Guard Contract package root | ACCEPT |
| T4 fixture permits package-root export proof | source fact | `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json` | `T5R1_EXTERNAL_READOUT_FOUNDATION` surface | `packageRootPath` | CADP authority-boundary fixture | ACCEPT |
| T4 checker verifies package export block and symbols | source fact | `governance/compat/check_cadp_authority_boundary_drift.py` | `check_surface` package-root branch | `requiredExportSymbols` | CADP authority-boundary checker | ACCEPT |
| External CLI/MCP invocation remains deferred | governance fact | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Roadmap Release Rules | `T5` | external-agent invocation-control owner | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Exact T5-R2 artifact paths | `Test-Path` returned `False` for the planned baseline, work order, and worker-return paths before authoring | UNIQUE_PATHS |
| Same-batch token search | `rg -n "CADP-AI-T5-R2\|T5 R2 Transport-Neutral" docs CVF_SESSION` returned only current next-move references and no prior T5-R2 packet | NO_PACKET_COLLISION |
| Coverage | search covered governed docs and current session surfaces; production ownership was checked directly in Guard Contract source, tests, package metadata, fixture JSON, and checker source | BOUNDED_SOURCE_VERIFIED |
| Collision decision | current session mentions authorize the packet name but are not competing artifacts; create one baseline/work-order pair only | CREATE_UNIQUE_PAIR |

## Scope

- add one pure TypeScript adapter-contract module under
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/`;
- compose T5-R1 ingress, freshness, allowlist, redaction, and deterministic
  receipt helpers in a fixed fail-closed order without duplicating their
  logic;
- define exact transport-neutral request/response envelopes with literal
  `false` for external invocation, mutation, activation, execution, provider
  call, credential resolution, and transport registration authority;
- expose the adapter contract from the internal contracts barrel and the
  Guard Contract package root through explicit named exports;
- update only the T5-R1 fixture row for package-root discoverability and add
  exactly one T5-R2 adapter surface row;
- add focused positive and adversarial tests, including proof that rejected
  ingress never reaches later composition stages;
- create one reference negative-proof/transport-foundation plan and one
  worker-return packet.

## Non-Goals

No MCP server file, CLI command, HTTP endpoint, tool registration, external
process launch, authentication implementation, credential/token handling,
provider API call, network access, live test, mutable store, filesystem read,
hook/autorun/CI wiring, public sync, deployment, production claim, session
state edit, moratorium lift, or worker commit.

## Transport Foundation Decision

| Decision row | R1 state | R2 authorized result | Boundary |
| --- | --- | --- | --- |
| Guard Contract package-root discoverability | deferred, `packageRootPath: null` | explicit named export from `src/index.ts`, fixture-backed | package contract only; not an external transport |
| transport-neutral adapter contract | absent | pure deterministic composition contract | no server/tool/command registration |
| authentication | shape only | remains shape only; adapter must fail closed with `AUTHENTICATION_REQUIRED` and must expose no success route based on caller self-attestation | future owner required |
| response envelope | absent | deterministic accepted/rejected envelope with no raw input echo and all authority fields false | local contract/test evidence only |
| external runtime | deferred | remains deferred | moratorium unchanged |

## Adversarial Proof Matrix

| Class | Required proof |
| --- | --- |
| unknown/oversize/accessor/proxy ingress | rejected before any adapter stage advances |
| caller self-attested authentication | cannot produce an accepted readout |
| stale, expired, or invalid timestamps | deterministic rejection |
| unallowlisted or secret/private-provenance metadata | no payload returned and no raw rejected value echoed |
| mutation/activation/execution/provider/credential fields | literal false in every response branch |
| stage callback or ambient dependency | no callback/port/process/environment/network input exists in the public adapter API |
| receipt key-order or caller mutation | inherited T5-R1 canonical receipt remains stable and snapshot-isolated |
| package export drift | T4 checker detects missing symbol/module export |

## MCP/CLI Adapter Boundary

| Field | Value |
| --- | --- |
| Adapter scope | transport-neutral contract and package-root discoverability only |
| No-runtime-overclaim | this packet does not claim the adapter executes, intercepts, wraps, registers, or serves any runtime command or external caller |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Guard Contract package-root adapter contract | may import and test pure validation/response composition; no action authority | source, focused tests, typecheck, T4 fixture/checker | internal transport-neutral contract | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no registered surface | cannot invoke, authenticate, mutate, execute, resolve credentials, or call providers | moratorium source and negative changed-set proof | MCP/CLI/HTTP adapter remains deferred to a fresh operator release | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

- exact seven-path worker manifest only;
- package-root exports are explicit, named, and fixture-checked;
- adapter API has no function/callback/port parameter capable of data access or
  side effects;
- every response carries literal-false authority fields;
- without a future authentication owner, no input can yield an accepted
  external readout;
- focused T5-R2 and T5-R1 regressions, TypeScript no-emit, T4 drift checker,
  worker-return fast gate, and pre-implementation gate pass;
- HEAD remains unchanged and staging empty at worker return.

## Evidence / Verification

- pre-dispatch autorun gate over the staged two-file packet;
- worker-captured pre-implementation gate from the committed dispatch anchor;
- Guard Contract TypeScript no-emit;
- serialized focused T5-R1/T5-R2 Vitest suite;
- CADP authority-boundary drift checker reporting five surfaces and zero
  violations;
- worker-return fast gate, Git diff check, unchanged worker HEAD, empty staging,
  and exact seven-path final status.

These are future worker/reviewer evidence requirements. This baseline records
no implementation or runtime proof.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: the operator selected a repository-local governed tranche and supplied no external artifact |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline and paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | only CVF-governed repository sources support this packet |

## Decision / Baseline

`DISPATCH_READY_BOUNDED_CONTRACT_ONLY`

T5-R2 may establish package-root and transport-neutral adapter-contract
foundations. It may not create an external transport or positive authenticated
execution path. A reviewer may accept only contract/package-root evidence and
must preserve external CLI/MCP as deferred.

## Claim Boundary

This baseline authorizes future local TypeScript contract, test, fixture,
reference-plan, and worker-return work under the paired work order. It does not
authorize or prove authentication, an external adapter runtime, MCP/CLI/HTTP
registration or invocation, credentials, provider/live/network behavior,
mutation, public sync, deployment, production, or a moratorium lift.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet; public and external runtime work is
outside scope.
