# CVF GC-018 Baseline - RSPB-AI-T7 Capability Preflight Profile Policy Selection Kernel

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: RSPB-AI-T7

Dispatch base head: `e27474ca8ee5d57f8340e24c7e1b4896e016da9e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Orchestrator/reviewer: current independent reviewer/orchestrator role

Worker target: external delegated worker role

Mixed-origin derived synthesis: REQUIRED

rawMemoryReleased=false

## Purpose

Authorize one bounded local-first tranche that converts the detailed local
platform/profile family into a CVF-native, pure Guard Contract kernel. The
kernel selects and validates an explicitly requested preflight profile and
derives bounded freshness/network/acquisition constraints without observing
the environment or granting execution, acquisition, network, or task authority.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RSPB-AI-T7 --title "Capability Preflight Profile Policy Selection Kernel" --date 2026-08-16 --base e27474ca8 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit external-worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | selected eight local profile/policy files, reconciled T2/T3/T4 owners, fixed a five-path worker manifest, and added fail-closed pure-kernel criteria |
| checkerReadAheadConfirmation | prior unchanged T6 checker read-ahead reused; guard orientation, literal gotchas, work-order template, dual-agent standard, and commit choreography refreshed |
| docOnlyNewFields | explicit profile request; platform compatibility; risk-scoped TTL; network posture; policy-only authority literals |
| claimBoundary | dispatch evidence only; no environment scan, acquisition, network call, execution, provider/live, public, or production claim |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | Purpose; Source Verification Block; Negative Search And Collision Discipline; Mixed-Origin Derived Synthesis Provenance; Absorption Decision Vector; System-Chain Value Review; Dual Agent Surface Matrix; Public Export Disposition; Claim Boundary; ACCEPT; REJECT; CONTRACT_ONLY |
| gateRunPurpose | confirmation and dispatch evidence after bounded source inspection |
| claimBoundary | structural readiness does not prove worker implementation correctness |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-absorption-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class external-absorption-implementation --role dispatcher --lifecycle-phase pre-dispatch --surface-selector EXTENSIONS/CVF_GUARD_CONTRACT --risk-ceiling MEDIUM --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional defect-specific constraint; local-first and independent-review rules remain binding |

## Authorization / Source

- Operator instruction: continue under the prior rule with this agent as
  dispatcher/reviewer/orchestrator and a separate external worker.
- Active continuity: `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
- Accepted ledger: `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json`.
- Existing snapshot owner: `scripts/cvf_doctor.py`.
- Existing acquisition owner: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/controlled-acquisition.contract.ts`.
- Existing route/readiness owner: `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts`.
- Local profile files are high-value design evidence, not CVF authority or
  copy authority.

## Decision / Baseline

Decision: `PROCEED_BOUNDED_HIGH_VALUE`.

T2 supplies environment evidence, T4 supplies route/readiness evidence, and
T3 supplies approval-bound acquisition decisions. The remaining high-fit gap
is an explicit profile policy that deterministically constrains how those
surfaces are interpreted for Windows, Linux, macOS, offline, and restricted
network contexts while retaining literal no-authority outputs.

## Scope / Owner Boundary

Owner: `EXTENSIONS/CVF_GUARD_CONTRACT/`.

Risk ceiling: `R1`. Pure TypeScript validation and transformation only. All
time and observations are caller inputs. No filesystem, environment read,
database, subprocess, network, provider, credentials, random source, storage,
or mutation.

## Allowed Paths

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-preflight-profile-policy.contract.ts` (NEW)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-preflight-profile-policy.contract.test.ts` (NEW)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts`
- `docs/reviews/CVF_RSPB_AI_T7_CAPABILITY_PREFLIGHT_PROFILE_POLICY_SELECTION_KERNEL_WORKER_RETURN_2026-08-16.md` (NEW)

## Forbidden Actions

- No direct import, execution, or file loading of local candidate code/data.
- No modification of T2, T3, T4, T5, T6, existing guards, hooks, checkers,
  package metadata, session state, handoff, registries, Web, CLI/MCP, adapters,
  executor, acquisition, rollback, or public surfaces.
- No environment/filesystem/database/network/provider/live/credential access.
- No default profile inferred from ambient OS; the profile ID and observed
  platform must be explicit inputs.
- No execution, acquisition, network, install, package activation, task
  authorization, or mutation grant.
- Worker must not stage, commit, push, or public-sync.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| route/readiness evidence owner exists | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts` | exported types and evaluators | `CapabilityRouteDecision`; `CapabilityReadinessDecision`; `evaluateCapabilityReadiness` | Guard Contract | ACCEPT |
| controlled acquisition owner exists | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/controlled-acquisition.contract.ts` | exported contract and evaluators | `ControlledAcquisitionPlan`; `evaluateControlledAcquisitionAuthorization` | Guard Contract | ACCEPT |
| read-only snapshot owner exists | EXISTS | `scripts/cvf_doctor.py` | capability snapshot functions and JSON output | `build_capability_snapshot` | CVF doctor | ACCEPT |
| local profile contract is canonical CVF authority | GOVERNANCE | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/docs/reference/capability_preflight_bootstrap/contracts/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROFILE.md` | full document | `cvf.capabilityPreflightBootstrap.v1` | mixed-origin candidate | REJECT |
| local profile JSON is safe for direct runtime loading | RUNTIME_BEHAVIOR | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/docs/reference/capability_preflight_bootstrap/profiles/windows-local.profile.json` | full file | `windows-local` | mixed-origin candidate | REJECT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| planned artifact path existence | all five planned worker paths returned `False` before authoring | NEW_PATHS_CONFIRMED |
| exact token search | `rg -n "capability-preflight-profile-policy|Capability Preflight Profile Policy Selection" docs CVF_SESSION EXTENSIONS/CVF_GUARD_CONTRACT` returned no match | NO_COLLISION |
| current owner comparison | T2/T3/T4 owners exist; no profile-policy selection owner exists | ENRICH_EXISTING_GUARD_CONTRACT |

## Selected Cluster Evidence

All paths below are relative to the accepted local folder root.

| File | Bytes | SHA-256 | Disposition |
| --- | ---: | --- | --- |
| `docs/reference/capability_preflight_bootstrap/contracts/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROFILE.md` | 3124 | `7f405e163eac1d3a93a928e919c483e6fb3a4e0a638ff96a35bb2d61f0e1d2bf` | ADAPT |
| `docs/reference/capability_preflight_bootstrap/profiles/linux-local.profile.json` | 498 | `dc99aba8ce347a5aa1db92ed2b3cf40817a7afa2d48f84769335ff6e1e119173` | ADAPT |
| `docs/reference/capability_preflight_bootstrap/profiles/macos-local.profile.json` | 548 | `83933c1d85a68cc208288b51bbac020418d3b980fd1ff918cf01b43ca46960a3` | ADAPT |
| `docs/reference/capability_preflight_bootstrap/profiles/offline-local.profile.json` | 457 | `fa27a6ff87a68539060cdefaf3899f0c9f6b73442c08cfb1f6de091a7039e1cc` | ADAPT |
| `docs/reference/capability_preflight_bootstrap/profiles/restricted-network.profile.json` | 511 | `788ac3e38a8a7b07791900855d99b24b5cf642d4106188c7edbfdf2f092a571a` | ADAPT |
| `docs/reference/capability_preflight_bootstrap/profiles/windows-local.profile.json` | 628 | `eef14e3e69049b58f3797497c98861b7a7dadf4e751003aea404d1e9939b63b4` | ADAPT |
| `docs/reference/capability_preflight_bootstrap/policies/CVF_CAPABILITY_PREFLIGHT_AUTHORITY_POLICY.md` | 1043 | `ee4a4ccb55355a41a5f27554b8665cee0ccbfbd7d659cce44dedc99229f717ea` | ADAPT |
| `docs/reference/capability_preflight_bootstrap/policies/CVF_CAPABILITY_ROUTE_AMBIGUITY_POLICY.md` | 987 | `5bcc80f054a15bd87dfed6d75eb0454703a1a3284661b33a5691cd87b835348b` | ADAPT |

## Mixed-Origin Derived Synthesis Provenance

artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE

authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED

| Input or concept | Origin class | Evidence basis | Claim type | Validation method | Current CVF owner | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| platform/network/profile constraints | OPERATOR_AGENT_CO_DESIGNED | eight selected local files | derived design | content/use-case inspection and CVF-native tests | Guard Contract | ADAPT |
| evidence is not authority | CVF_PUBLIC_DERIVED | local policy plus current T3/T4 literals | invariant | literal false assertions | Guard Contract | ENRICH_EXISTING |
| local files as runtime configuration | MIXED_ORIGIN | candidate JSON/docs | candidate data | direct-load risk review | none | REJECT_DIRECT_IMPORT |

## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
| --- | --- | --- | --- |
| Knowledge absorption | PROCEED_BOUNDED | eight-file profile cluster | one cluster |
| Direct import | REJECT_DIRECT_IMPORT | noncanonical candidate JSON/docs | CVF-native rewrite only |
| Runtime activation | CONTRACT_ONLY | pure deterministic kernel | no I/O or executor |
| Authority promotion | NOT_AUTHORIZED | output literals remain false | independent review required |

## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
| --- | --- | --- | --- | --- | --- |
| environment snapshot | T2 doctor | accepted evidence owner | HIGH_VALUE | READY_TO_CONSUME | bind only as caller evidence |
| route/readiness | T4 Guard Contract | accepted evidence owner | HIGH_VALUE | READY_TO_CONSUME | validate and preserve authority false |
| controlled acquisition | T3 Guard Contract | accepted decision owner | HIGH_VALUE | CONTRACT_ONLY | constrain but never execute |
| profile/policy selection | selected local cluster | missing owner seam | HIGH_VALUE | IMPLEMENT_NOW | add pure kernel |
| ambient detection/adapters/executor | local runtime candidates | separately governed | DEFER | NOT_AUTHORIZED | no action |

## Absorption Efficiency And Provenance Reuse

manifestLedgerReuse: REUSE_IF_FRESH

semanticReviewUnit: CAPABILITY_CLUSTER

defaultValuePosture: PRESERVE_UNTIL_CONTRADICTED

additionalValueProbe: SKIP_UNLESS_NAMED_GAP

latencyBudget: SINGLE_PASS_BOUNDED

intakePriority: LOCAL_SYNTHESIZED_PACK_FIRST

localSemanticInspection: FILE_AND_USE_CASE_CONTENT_REQUIRED

mappingAction: DIRECT_WORK_ORDER_FOR_HIGH_FIT_CLUSTERS

deliverySequence: WORK_ORDER_THEN_WORKER_THEN_INDEPENDENT_REVIEWER

namePatternInference: FORBIDDEN_AS_VALUE_DISPOSITION

upstreamConsultation: TARGETED_FOR_PROVENANCE_OR_GAP

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | accepted local Capability Preflight Bootstrap folder |
| Enumeration command | predecessor `rg --files --hidden --no-ignore`; named eight-file selection |
| Manifest artifact or inline manifest | `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_MANIFEST_2026-08-15.json` |
| Processing ledger artifact or inline ledger | `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | Guard Contract T3/T4 plus T2 doctor snapshot owner |
| Unresolved items | 0 processing rows; implementation pending worker/reviewer |
| Completion claim boundary | selected-cluster dispatch only; no full scan or authority activation |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| profile contract | lifecycle/state separation | PACKAGE_CANDIDATE | Guard Contract | adapt bounded fields | pure contract |
| five platform profiles | platform, TTL, network, privilege use cases | RUNTIME_CANDIDATE | focused tests and constants | rewrite and validate | no file loading |
| authority/ambiguity policies | no-strengthening invariants | DOCTRINE_ADAPTED | contract assertions | encode | no new doctrine owner |
| local JSON direct loading | ambient/config authority risk | REJECT_DIRECT_IMPORT | none | reject | no filesystem |
| invalid profile/authority fixtures | negative validation vocabulary | CHECKER_CANDIDATE | focused test | adapt into tests | no hook wiring |
| adapters and executor | no selected T7 value | NO_PACKAGE_OR_RUNTIME_VALUE | existing candidate ledger | retain prior disposition | out of tranche |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| route/readiness | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts` | CONFIRMED_EXISTING | accepted evidence | consume only |
| acquisition approval | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/controlled-acquisition.contract.ts` | CONFIRMED_EXISTING | accepted authority boundary | preserve |
| environment observation | `scripts/cvf_doctor.py` | CONFIRMED_EXISTING | accepted runtime evidence | no scanner work |
| explicit profile policy | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/` | NEW_FINDING | no deterministic profile-policy owner | implement bounded kernel |

## Mandatory Blind-Spot Control Block

The local folder is provenance-backed derived synthesis. All eight selected
files were inspected at content and use-case level. Their high-fit value is
preserved while direct loading and ambient authority inference are rejected.

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | selected mixed-origin copied-folder cluster |
| Upstream or source-mirror disposition | accepted predecessor evidence reused; no fetch |
| Enumeration or manifest plan | accepted 205-file ledger; named eight-file cluster |
| Per-file terminal-ledger plan | eight hashes above |
| Owner or overlap route | existing T2/T3/T4 owners and Guard Contract |
| Value-disposition route | profile kernel DO_NOW; I/O and adapters deferred |
| Claim boundary | no full scan, direct import, persistence, or authority activation |

## Rescan Intelligence Hardening

- Original source artifact: operator-provided mixed-origin local folder.
- Predecessor intake artifact: accepted RSPB-AI-T0 205-file ledger.
- Delta ledger status: reused; eight selected hashes recomputed.
- Routing matrix status: profile cluster routed to Guard Contract.
- Semantic sampling status: all eight selected contents inspected.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Treatment |
| --- | --- |
| UNCHANGED_FROM_INTAKE | 197 files retain prior disposition |
| CHANGED_DISPOSITION | eight selected for bounded adaptation |
| NEW_FINDING | explicit profile-policy seam missing |
| REMOVED_OR_REJECTED | direct data loading rejected |

### Follow-Up Routing Matrix

| Routing lane | Handling |
| --- | --- |
| DO_NOW | pure module, tests, two barrel exports, worker return |
| SEPARATE_RUNTIME_TRANCHE | filesystem profile loading or environment discovery |
| STRATEGIC_OPERATOR_DECISION | acquisition/network/execution authority |
| OUT_OF_SCOPE | provider/live/public/deploy/production |
| RESOLVED_BY_DESIGN | explicit input and literal false authority outputs |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| RSPB-T7-S1 | platform profiles | profile selects bounded posture | ADAPT | platform mismatch and duplicate ID | REQUIRE_FAIL_CLOSED |
| RSPB-T7-S2 | offline/restricted profiles | network mode constrains behavior | ADAPT | inject destinations or infer network grant | REQUIRE_FAIL_CLOSED |
| RSPB-T7-S3 | authority policy | evidence cannot strengthen authority | ADAPT | inject authorized outputs | REQUIRE_LITERAL_FALSE |

## Corpus Completeness And Report Integrity

- Corpus task class: selected capability-cluster absorption.
- Corpus root: eight selected local files.
- Snapshot time: 2026-08-16 dispatcher selection.
- Enumeration command: predecessor `rg --files --hidden --no-ignore` plus named selection.
- Manifest artifact or inline manifest: Selected Cluster Evidence above.
- Manifest hash: eight per-file SHA-256 values above.
- Processing ledger artifact or inline ledger: accepted 205-row ledger plus conversion matrix.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=8; ledger_terminal=8; exclusions=197; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: 197 files outside this cluster.
- Unreadable or unsupported files: none selected.
- Aggregation check: 8 + 197 = 205.
- Drift check: selected hashes recomputed; no excluded-file freshness claim.
- Output traceability: cluster maps to five worker paths.
- Adversarial verification: platform, TTL, network, secrets, authority, hostile inputs, and determinism.
- Corpus verdict: PARTIAL

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Guard Contract barrel export | profile-policy evidence only; all action grants false | focused tests required | in-process import only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | none | no adapter, authentication, profile loading, or action authority | forbidden scope | separate future adapter | DEFERRED_WITH_REASON |

## Risk / Corrective Action

Fail closed on malformed/proxy/accessor/sparse/unbounded input, duplicate or
unknown profile IDs, platform mismatch, invalid TTL ordering, secret-like
content, ambiguous network posture, stale or malformed T4 evidence, or any
attempt to set an authority output true. Stop if safe behavior requires a
sixth worker path or I/O.

## Evidence / Verification

Required evidence: exact five-path diff, focused adversarial tests, current
T3/T4 regression tests, full Guard Contract tests, TypeScript no-emit,
worker-return fast gate, and zero external service calls.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted local ledger -> eight-file inspection -> owner reconciliation -> pure Guard Contract kernel |
| Matching local-view guard | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py` |
| Owner surface | Guard Contract |
| Disposition | PROCEED_BOUNDED_HIGH_VALUE |
| Claim boundary | profile evidence cannot authorize execution, acquisition, network access, or mutation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private implementation dispatch; worker may not push or public-sync.

## Claim Boundary

This baseline authorizes only a pure profile-policy selection contract, its
tests, two barrel exports, and a worker return. It does not authorize profile
file loading, environment observation, acquisition, installation, network
access, task authority, execution, mutation, credentials, adapters, provider
calls, public sync, deployment, production, or worker commit.
