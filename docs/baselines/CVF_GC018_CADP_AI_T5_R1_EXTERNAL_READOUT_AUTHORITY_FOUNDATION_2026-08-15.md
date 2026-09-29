# CVF GC-018 Baseline - CADP AI T5 R1 External Readout Authority Foundation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: CADP-AI-T5-R1

Date: 2026-08-15

Dispatch base head: `576af12fba91bb6972e1e7646d63fe1d30d7b7d2`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Independent reviewer/closer

Worker target: contract/fixture/negative-proof foundation worker role (no
external entry point)

## Purpose

Authorize a documentation-and-contract-only foundation tranche that source-
verifies and bounds the nine `MISSING_AUTHORITY` prerequisite rows recorded
by the accepted CADP-AI-T5 deferral. The worker may add CVF-native, pure,
deterministic TypeScript contracts, exact read-only metadata allowlists,
caller-identity input contracts, ingress/size validators, a redaction
contract, deterministic error/receipt and freshness/replay contracts, and
focused positive/negative fixtures inside the existing Guard Contract owner.
This tranche does not create, register, or wire any external entry point,
and does not lift the external-agent invocation moratorium.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind mcp-cli-adapter --batch-id CADP-AI-T5-R1 --title "CADP AI T5 R1 External Readout Authority Foundation" --date 2026-08-15 --base 576af12fba91bb6972e1e7646d63fe1d30d7b7d2 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CADP-AI-T5 decision accepted bounded and deferred at ef84a1f6a" --dependency "CADP-AI-T6 live compatibility accepted bounded at 2599ff10e" --include-worker-return-skeleton --stdout` |
| generatedProfile | mcp-cli-adapter plus `WORKER_MUST_NOT_COMMIT` no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | resolved every generated placeholder cell with decision-scoped prose, the nine-row prerequisite foundation table, exact Guard Contract source citations, the exact allowed-path manifest, and the foundation-only claim boundary; removed the trigger-map echo section; added the Dual Agent Surface Matrix and Reviewer Closure Conversion detail required for this batch |
| checkerReadAheadConfirmation | checker sources listed in the Checker Source Read-Ahead Block below were read before this baseline was authored |
| docOnlyNewFields | `prerequisiteRow`; `foundationScopeDisposition`; no runtime schema field is introduced by this baseline |
| claimBoundary | dispatch authoring provenance only; no runtime, provider, live, public, MCP, CLI, or model-router behavior claim |

## Authorization

The active session bootstrap read model and active handoff both name this
exact next allowed move: dispatcher authoring of a fresh GC-018 baseline and
`WORKER_MUST_NOT_COMMIT` work order for CADP-AI-T5-R1, source-verifying and
bounding the nine missing T5 prerequisite rows, without creating an external
entry point and without lifting the invocation moratorium. This baseline does
not authorize MCP tool registration, CLI command addition, external-agent
invocation, credential access, provider calls, network access, state
mutation, hook/autorun/CI wiring, public sync, deployment, or production
claims.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| CADP-AI-T5 decision accepted bounded and deferred | `docs/reviews/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_COMPLETION_2026-08-14.md`, top status line records an accepted, closed, bounded, deferred-missing-authority disposition; material closure anchor `ef84a1f6a` | independent completion-review acceptance plus explicit operator selection of the R1 foundation tranche | ACCEPT |
| CADP-AI-T6 live compatibility accepted bounded | `AGENT_HANDOFF_V59_2026-08-11.md`, Current Authority row records reviewer-accepted, closed, bounded T6-R2 status at `2599ff10e`; roadmap Work Plan T6 row `ACCEPTED_LIVE_BOUNDED` | independent reviewer acceptance recorded in the active handoff and roadmap | ACCEPT |
| Foundation scope stays inside the nine-row deferral, not a T5 implementation release | `docs/assessments/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md`, Reopen / Future-Manifest Conditions items 1-9 | this baseline authorizes only foundation contract/fixture/negative-proof work satisfying items 2-8; item 1 (moratorium lift) and item 9 (final owner reconciliation sign-off) remain reviewer/operator-owned, not worker-owned | ACCEPT_FOR_FOUNDATION_SCOPE_ONLY |

## Scope

- inventory the current CADP T1/T3A/T3B/T4 TypeScript contract sources and
  the existing owner-binding grant pattern relevant to a future read-only
  external consumer;
- add one new CVF-native external-readout foundation contract module under
  the existing Guard Contract owner (`EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/`),
  containing pure, deterministic TypeScript types and validator functions
  only, with no HTTP/CLI/MCP transport binding;
- define an exact read-only metadata field allowlist for a future CADP
  external readout response, reusing the T1 `falseAuthorityFields` and
  secret/private-provenance rejection pattern;
- define an explicit external caller identity **input contract** (shape
  only: caller identifier, requested scope, request timestamp) that does not
  resolve, validate against, or store any credential;
- define an ingress schema and size/shape validator for a hypothetical
  external request, following the strict-record-type pattern already used by
  T1;
- define a redaction contract that rejects secret and private-provenance
  fields from the T1 rejection invariants when applied to an external-facing
  read-only payload;
- define a deterministic external error/receipt contract, extending the T1
  `DeterministicCadpReceipt` pattern with an explicit input time (no ambient
  clock/UUID);
- define a replay/freshness contract for a stateless external read/query
  call (explicit issued-at/expiry fields; no session or credential state);
- add focused positive and adversarial negative Vitest fixtures for every
  contract above, following the T4 fixture/negative-corpus pattern;
- add a standalone negative-proof plan document (prose plan only, or a small
  fixture-driven test file) that names the adversarial classes this
  foundation must resist;
- reconcile this foundation explicitly against the ASSF external-agent
  readout boundary contract, the RTAD-T5 Model Gateway MCP boundary, and the
  existing CADP T1/T2/T2A/T3A/T3B/T4 owners so no owner surface is
  duplicated;
- create exactly the two governed Markdown artifacts named by this
  dispatch pair (this baseline and its paired work order).

## Non-Goals

No MCP tool registration, no CLI command, no `CVF_ECO_v2.5_MCP_SERVER`
registration change, no external-agent invocation or launch, no credential
access or resolution, no provider API call, no network or live test, no
state mutation, no hook/autorun/CI wiring, no public sync, no deployment, no
production claim, no lifting of the external-agent invocation moratorium, no
edit to `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, or `AGENT_HANDOFF*.md`, and
no commit by the worker.

## Nine-Row Prerequisite Foundation Disposition

Source: `docs/assessments/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md`,
Required Decision Analysis table (independently reviewed and repaired to 12
rows with 9 `MISSING_AUTHORITY` rows per
`docs/reviews/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_COMPLETION_2026-08-14.md`,
Independent Review Findings item 1).

| # | Prerequisite row | Prior disposition | This tranche's allowed foundation action | Resulting disposition |
| --- | --- | --- | --- | --- |
| 1 | owner/package export boundary | MISSING_AUTHORITY | add one new contract module under the existing Guard Contract owner; no separate package, no export from a public barrel that implies external readiness | SATISFIED_BOUNDED (contract exists; export remains internal-only until a future adapter packet) |
| 2 | external caller authentication and identity binding | MISSING_AUTHORITY | define an identity **input contract** (shape only); explicitly do not resolve or validate a credential | SATISFIED_BOUNDED (shape only; authentication mechanism remains MISSING_AUTHORITY) |
| 3 | ingress schema and request-size validation | MISSING_AUTHORITY | define a strict ingress schema and size/shape validator, fail-closed on unknown fields and oversize input | SATISFIED_BOUNDED |
| 4 | exact metadata field allowlist | MISSING_AUTHORITY | define an explicit allowlist type reusing the T1 false-authority-field pattern | SATISFIED_BOUNDED |
| 5 | secret/private-provenance redaction | MISSING_AUTHORITY | define a redaction contract that rejects T1 secret/private-provenance fields from any allowlisted payload | SATISFIED_BOUNDED |
| 6 | deterministic external error/receipt shape | MISSING_AUTHORITY | define a deterministic receipt/error contract extending the T1 `DeterministicCadpReceipt` explicit-time pattern | SATISFIED_BOUNDED |
| 7 | replay/freshness behavior | MISSING_AUTHORITY | define an issued-at/expiry freshness contract for a stateless call; no session state | SATISFIED_BOUNDED |
| 8 | package-root/transport discoverability | MISSING_AUTHORITY | explicitly keep the new module unregistered on any transport; record discoverability as still deferred | REMAINS_DEFERRED_WITH_REASON (no transport registration is in scope) |
| 9 | focused external-surface negative-proof plan | MISSING_AUTHORITY | add adversarial fixtures/tests for authority widening, unknown fields, oversize input, secret/private leakage, replay, stale request, and identity mismatch | SATISFIED_BOUNDED |

Rows 1-7 and 9 may move from `MISSING_AUTHORITY` to `SATISFIED_BOUNDED` only
after the worker produces the corresponding contract/fixture evidence and an
independent reviewer confirms it; this baseline does not itself convert any
row. Row 8 (transport discoverability) and the moratorium-lift condition from
the T5 assessment's Reopen condition 1 remain outside this tranche's Allowed
scope and stay `MISSING_AUTHORITY`/`DEFERRED_WITH_REASON` regardless of
worker output. Converting a row's disposition in the worker return without
independent review is not accepted; only an independent reviewer may record
`SATISFIED_BOUNDED` as the tranche's closing disposition per the Reviewer
Closure Conversion section below.

## Reconciliation With Adjacent Owner Surfaces

| Adjacent surface | Path | Reconciliation |
| --- | --- | --- |
| ASSF external-agent readout boundary | `docs/roadmaps/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_ROADMAP_2026-06-26.md`; `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` | ASSF governs skill/package external readout; CADP T5-R1 governs capability-admission/distribution external readout. Distinct owner domains; this tranche does not edit ASSF's contract, generated index, or resolver, and reuses ASSF's `DEFERRED_WITH_REASON` adapter posture as a pattern, not as shared authority. |
| RTAD-T5 Model Gateway MCP boundary | `docs/baselines/CVF_GC018_RTAD_T5_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY_2026-06-18.md` | RTAD-T5's Forbidden Scope prohibits new MCP runtime tools or provider live calls; this tranche adds no MCP tool and stays inside RTAD-T5's boundary rather than routing through it. |
| external-agent invocation moratorium | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md`, Roadmap Release Rules | the moratorium requires a fresh roadmap, GC-018, source-verified work order, and explicit operator decision before any T5-class implementation opens; this baseline is that fresh GC-018 for foundation-only contract work, and it does not itself constitute the operator decision lifting the moratorium for a live external entry point |
| existing CADP T1/T2/T2A/T3A/T3B/T4 owners | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts`; `governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v2.json`; `governance/compat/check_cadp_authority_boundary_drift.py`; `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json` | the new foundation module is additive inside the same Guard Contract owner and must not modify T1/T3A/T3B contract files, the T2A grant, or the T4 checker/fixture; if the worker adds a new drift-checker surface entry it must be a new fixture entry, not an edit to an existing surface's `falseAuthorityFields` or `requiredExportSymbols` |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T5 deferral records exactly nine `MISSING_AUTHORITY` prerequisite rows | CLOSURE_EVIDENCE | `docs/reviews/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_COMPLETION_2026-08-14.md` | Independent Review Findings item 1; Acceptance Receipt Assertion Matrix | `9 MISSING_AUTHORITY rows` | T5D completion review | ACCEPT |
| T5 assessment names the exact nine reopen conditions | CLOSURE_EVIDENCE | `docs/assessments/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md` | Reopen / Manifest Conditions section | items 1-9 | T5D assessment | ACCEPT |
| CADP T1 contract owns admission/assignment/distribution/evidence/receipt records with `false` authority fields | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts` | lines 26, 60-108 | `CADP_CONTRACT_VERSION`; `CapabilityAdmissionRecord`; `CapabilityDistributionManifest` | Guard Contract CADP contract | ACCEPT |
| T1 barrel export re-exports the CADP contract module symbols | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` | lines 257-280 | `CADP_CONTRACT_VERSION`; `createDeterministicCadpReceipt` | Guard Contract barrel index | ACCEPT |
| T4 drift-checker fixture defines per-surface `falseAuthorityFields`, `requiredExportSymbols`, and `forbiddenSeamTokens` schema | EXISTS | `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json` | `surfaces[0]` through `surfaces[2]` | `surfaceId`; `falseAuthorityFields`; `forbiddenSeamTokens` | CADP authority boundary contract fixture | ACCEPT |
| T4 checker is a hermetic, standalone, unwired static lexical checker with no HTTP/CLI/MCP surface | RUNTIME_BEHAVIOR | `governance/compat/check_cadp_authority_boundary_drift.py` | lines 10-18 | `CADP-AI-T4 authority boundary drift checker` | CADP authority boundary drift checker | ACCEPT |
| T2A owner-binding grant binds an internal repository-local caller identity via a committed grant JSON, not a caller-supplied credential | EXISTS | `governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v2.json` | `grantId`; `credentialReference`; `boundReceiptIds` | `cadp-ai-t2a-owner-binding-grant-v2`; `credentialReference` | T2A owner-binding grant | ACCEPT |
| RTAD-T5 forbids new MCP runtime tools or provider live calls | LITERAL_INVARIANT | `docs/baselines/CVF_GC018_RTAD_T5_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY_2026-06-18.md` | Forbidden Scope section | `Forbidden Scope` | RTAD-T5 boundary baseline | ACCEPT |
| ASSF adapter posture uses `DEFERRED_WITH_REASON` pending a future source-verified GC-018/work order | LITERAL_INVARIANT | `docs/roadmaps/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_ROADMAP_2026-06-26.md` | Dual Agent Surface Matrix | `DEFERRED_WITH_REASON` | ASSF external-agent boundary roadmap | ACCEPT |
| the invocation moratorium requires a fresh roadmap, GC-018, source-verified work order, and explicit operator decision before T5-class implementation opens | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Roadmap Release Rules | `T5 requires a new roadmap, fresh GC-018, source-verified work order, and an explicit operator decision lifting the invocation moratorium` | invocation-control roadmap | ACCEPT |
| generic MCP guide keeps `runtimeExecutionAuthorized=false` across all existing tools | LITERAL_INVARIANT | `docs/guides/CVF_GENERIC_MCP_ADAPTER_INTEGRATION_GUIDE_2026-05-31.md` | lines 175, 196 | `runtimeExecutionAuthorized` | generic MCP adapter integration guide | ACCEPT |
| the active session bootstrap read model names this exact next allowed move | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `nextAllowedMove` | active session bootstrap read model | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_cadp_authority_boundary_drift.py` |
| literalTokensReviewed | `baseline` structural class requires one heading each from source/predecessor evidence, decision/baseline/proposed tranche, and evidence/verification groups; dispatch-quality lifecycle rejects an unresolved boolean-style prerequisite disposition and stale after-closure placeholder prose; Source Verification uses the three-way accept/reject/source-not-found disposition spelling; Delta block guard requires a real Field/Disposition table for its eight fields; Dual Agent Surface Matrix requires both internal-agent and external-CLI/MCP rows with one allowed disposition token per row |
| gateRunPurpose | confirm this baseline satisfies its own structural, dispatch-quality, and Delta-block shape before the pre-dispatch autorun gate runs |
| claimBoundary | checker source read-ahead proves structural shape only; it does not itself prove the nine-row foundation disposition is correct, which rests on the Nine-Row Prerequisite Foundation Disposition table above |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact path existence for both target artifacts | `Test-Path` equivalent (`ls`) run before authoring: `docs/baselines/CVF_GC018_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_2026-08-15.md` = ABSENT; `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_2026-08-15.md` = ABSENT | ABSENT_BEFORE_AUTHORING |
| exact title token search | `rg -n --fixed-strings "T5-R1" docs CVF_SESSION` and `rg -n --fixed-strings "EXTERNAL_READOUT_AUTHORITY_FOUNDATION" docs CVF_SESSION` returned only session-state prose (`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION/state/entries/cadpAiT5R1AuthorityFoundationSelection20260815.json`, `CVF_SESSION/state/entries/nextAllowedMove.json`) naming this exact selected next move, plus one unrelated `docs/corpus-intelligence` JSON sample ID; no `docs/baselines/` or `docs/work_orders/` path collision | NO_EXACT_COLLISION |
| collision decision | session-state prose confirms this tranche is the currently selected next move, not a duplicate artifact; ADIF resolver query (taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cadp`) returned zero items | REUSE_AS_SELECTION_EVIDENCE_NOT_DUPLICATE_ARTIFACT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cadp`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cadp --risk-ceiling HIGH --max-results 10 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no added ADIF constraint; canonical source, no-runtime, and moratorium boundaries remain mandatory |

## MCP/CLI Adapter Boundary

| Field | Value |
| --- | --- |
| Adapter scope | contract/fixture/negative-proof foundation only; no transport, tool, or command is registered or invoked |
| No-runtime-overclaim | this packet does not claim any new module executes, intercepts, wraps, launches, or serves an external caller; every new symbol is a pure TypeScript type or deterministic function with no filesystem, network, process, or provider side effect |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | new CADP external-readout foundation contract module under `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/`, consumed only by internal tests and future internal review | internal agents may read the new pure contract types/validators for planning and review only; no commit, activation, or mutation authority is granted by this baseline | Source Verification rows above; worker-produced tests once returned | N/A with reason: internal contract module only, no adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | candidate future CADP external read/query surface; not implemented, registered, or invoked in this tranche | no external caller may authenticate, request, mutate, activate, or execute anything through this tranche; the identity/ingress/redaction/receipt/freshness contracts are shape-only foundations, not a live boundary | nine-row prerequisite table above; T5D assessment and completion review | deferred adapter owner; transport registration and moratorium lift both remain out of this tranche's Allowed scope | `DEFERRED_WITH_REASON` |

## Decision / Baseline

Proceed with one documentation-and-contract foundation tranche inside the
existing Guard Contract owner. This baseline authorizes the exact Allowed
scope above and no more: it does not release a T5 adapter, does not lift the
invocation moratorium, and does not itself convert any prerequisite row to a
closed-equivalent disposition. The worker executes; only an independent
reviewer may accept row conversions.

## Current Runtime Freshness Verification

| Runtime claim | Verification command or source | Observed value | Disposition |
| --- | --- | --- | --- |
| no external CADP-named HTTP/CLI/MCP entry point exists today | `docs/assessments/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md`, Existing CADP Interface Inventory; independently re-confirmed by bounded `EXTENSIONS`, `governance`, `scripts` inspection at this dispatch's base head | no external CADP entry point found in either bounded search | PASS |
| a six-column Dual Agent Surface Matrix machine checker is only a documented candidate, not a wired gate today | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`, Machine Check Candidate section; direct path check for `governance/compat/check_dual_agent_surface_matrix.py` | path absent on disk at this dispatch's base head | PASS |
| the T4 authority boundary drift checker remains standalone and unwired to any hook/autorun/CI trigger | `governance/compat/check_cadp_authority_boundary_drift.py`, module docstring | checker source confirms hermetic, dependency-free, unwired status | PASS |

## Evidence / Verification

Dispatch evidence consists of exact current-source citations for all nine
prerequisite rows, the T5D completion review's independently reviewed
arithmetic, the T4 fixture/checker schema pattern the new foundation must
extend without modification, real ADIF resolver and collision-search output,
scaffold provenance, and exact pending two-path manifest with clean staging
and unchanged HEAD. These prove dispatch shape and source fidelity only; the
worker's contract/fixture/test evidence and the independent reviewer's
acceptance still govern whether any prerequisite row may close.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: operator selected a repo-local governed foundation lane and supplied no external artifact |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline and paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | CVF-governed repository sources remain the only authority for this dispatch |

## Claim Boundary

This baseline authorizes evidence-backed foundation contract, fixture, and
negative-proof work only. It does not authorize or prove an MCP tool, a CLI
command, external-agent invocation, authentication, live redaction
effectiveness, transport registration, provider behavior, credential
resolution, network access, state mutation, public-sync readiness,
deployment, production use, or a lifted invocation moratorium. Converting any
of the nine prerequisite rows from `MISSING_AUTHORITY` to a closed-equivalent
disposition is reserved for the independent reviewer after worker evidence
exists; this baseline records the allowed scope of that evidence, not the
outcome.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-contract dispatch packet; no public
artifact or sync action is authorized.
