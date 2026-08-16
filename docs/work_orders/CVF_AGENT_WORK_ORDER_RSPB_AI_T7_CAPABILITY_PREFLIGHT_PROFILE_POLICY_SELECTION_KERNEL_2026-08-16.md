# CVF Agent Work Order - RSPB-AI-T7 Capability Preflight Profile Policy Selection Kernel

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: RSPB-AI-T7

Dispatch base head: `e27474ca8ee5d57f8340e24c7e1b4896e016da9e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: external delegated worker role

Reviewer/closer: current independent reviewer/orchestrator role

Worker return path: `docs/reviews/CVF_RSPB_AI_T7_CAPABILITY_PREFLIGHT_PROFILE_POLICY_SELECTION_KERNEL_WORKER_RETURN_2026-08-16.md`

## Dispatch Prompt Envelope

Role: implementation worker for RSPB-AI-T7.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_RSPB_AI_T7_CAPABILITY_PREFLIGHT_PROFILE_POLICY_SELECTION_KERNEL_2026-08-16.md`

Paired baseline: `docs/baselines/CVF_GC018_RSPB_AI_T7_CAPABILITY_PREFLIGHT_PROFILE_POLICY_SELECTION_KERNEL_2026-08-16.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-08-16; derive repository facts from
the current execution base, not provider memory.

Do-not-misread notes: this is pure in-memory Guard Contract work. It grants no
file loading, environment observation, acquisition, network, adapter,
execution, provider/live, public, deployment, or production authority.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this packet, paired baseline, selected source files, existing T3/T4
owners, and checker sources before editing. Capture full `executionBaseHead`
and initial `git status --short`.

Return contract: implement only the exact manifest, run every required proof,
leave all changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Implement a deterministic, fail-closed profile-policy kernel that validates
an explicitly supplied profile catalog/request and produces constraints for
preflight evidence consumption while keeping every action-authority literal
false.

## Operator Checkpoint

Operator checkpoint: SATISFIED. The operator explicitly directed continuation
under the established distinct worker and reviewer/orchestrator rule. Any
authority expansion named in Forbidden Actions requires a new checkpoint.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake source | accepted mixed-origin local synthesis ledger and selected eight-file cluster |
| Scope classification | bounded five-path pure TypeScript implementation |
| Risk sensitivity | R1 local-only; environment I/O, provider/live, secrets, public-sync, and production forbidden |
| Selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Dispatcher/orchestrator | current independent reviewer/orchestrator role |
| Worker | external delegated implementation worker only |
| Reviewer/closer | independent reviewer/closer, distinct from worker |
| External evidence intake | predecessor ledger reused; selected hashes must be recomputed |
| Disposition | worker implements without commit; independent reviewer evaluates and closes |
| Escalation condition | stop and return blocked for a sixth path, authority expansion, I/O, mutation, or canonical contradiction |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| operator continuation | current instruction to continue under prior rule | ACCEPT |
| active next move | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| paired baseline | `docs/baselines/CVF_GC018_RSPB_AI_T7_CAPABILITY_PREFLIGHT_PROFILE_POLICY_SELECTION_KERNEL_2026-08-16.md` | ACCEPT |
| accepted local ledger | `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json` | ACCEPT |

## Agent Roles

| Role | Responsibility | Commit permission |
| --- | --- | --- |
| worker | exact-manifest implementation, tests, and pending return | FORBIDDEN |
| reviewer/orchestrator | independent diff review, probes, bounded repair decision | REVIEWER_ONLY |
| closer | accepted material commit and separate continuity sync | CLOSER_ONLY |

## Required First Reads

| Path | Required action |
| --- | --- |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | FULL_READ |
| `CVF_SESSION_MEMORY.md` | FULL_READ |
| `AGENT_HANDOFF_V59_2026-08-11.md` | FULL_READ |
| `docs/reference/guard_orientation/README.md` | FULL_READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ |
| this work order and paired baseline | FULL_READ |
| selected eight local files and current T3/T4 owners | SOURCE_VERIFIED |

## Pre-Flight Checks

| Check | Required result |
| --- | --- |
| `git rev-parse HEAD` | captured as executionBaseHead |
| `git status --short` | no pre-existing owned-path change |
| selected eight SHA-256 values | exact match to paired baseline |
| exact five worker paths | absent or unchanged as declared |
| provider/live opt-in | not used |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RSPB-AI-T7 --title "Capability Preflight Profile Policy Selection Kernel" --date 2026-08-16 --base e27474ca8 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit external-worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | bound exact five-path manifest, functional contract, selected source hashes, proof commands, and independent-review handoff |
| checkerReadAheadConfirmation | prior unchanged T6 checker read-ahead reused and governing orientation/template/standards refreshed |
| docOnlyNewFields | profile catalog; requested profile; observed platform; risk-scoped TTL; network posture; literal authority boundary |
| claimBoundary | worker dispatch only; no runtime I/O, action authority, provider/live, public, or production claim |

## Worker Autonomy / No-Question Rule

Repair allowed-scope defects directly. Return only for a source contradiction,
forbidden-path need, or missing authority that makes safe completion impossible.

## Reviewer Blocked-Return Disposition - R1

Disposition: `REVIEW_REJECTED_RETRY_REQUIRED`.

The first worker returned `BLOCKED_WITH_REASON` at execution base
`592368d370e8ae40ebe039ff647d7a9b9f81b114`. Independent reviewer
reproduction disproved the claimed package-wide Vitest/Vite incompatibility:

- `npx vitest run src/contracts/capability-route-readiness.contract.test.ts`
  passed 19/19 under Node v22.17.0, Vitest 1.6.1, and Vite 5.4.21;
- `npm test` passed 40/40 files, 624 tests, with 5 intentionally skipped;
- no dependency edit, install, network access, or provider call was required.

The original command incorrectly named a nonexistent local config file. This
R1 amendment removes that argument from all focused commands. A missing
optional config file is not evidence of a broken test toolchain. The retrying
worker must execute the exact corrected commands from the package directory
and may claim a dependency blocker only if the direct package script also
fails and the raw output supports that conclusion.

Reviewer documentation repair disclosure: before preserving the blocked
return, the reviewer added only its missing Mandatory Blind-Spot Control and
External Repository Absorption Entry Control sections. No worker command,
finding, status, or implementation claim was changed.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-absorption-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class external-absorption-implementation --role dispatcher --lifecycle-phase pre-dispatch --surface-selector EXTENSIONS/CVF_GUARD_CONTRACT --risk-ceiling MEDIUM --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no defect-specific addition; exact manifest and independent review remain mandatory |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | Purpose; Source Verification Block; Agent Handoff Contract Control Block; Worker Output Checker Read-Ahead Mandate; Worker Return Packet Shape Contract; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Claim Boundary; ACCEPT; REJECT |
| gateRunPurpose | confirmation of packet structure and authority boundaries before worker execution |
| claimBoundary | no claim that pending implementation is correct or accepted |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| route/readiness evidence owner exists | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts` | exported types and evaluators | `CapabilityRouteDecision`; `CapabilityReadinessDecision`; `evaluateCapabilityReadiness` | Guard Contract | ACCEPT |
| controlled acquisition owner exists | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/controlled-acquisition.contract.ts` | exported types and evaluators | `ControlledAcquisitionPlan`; `evaluateControlledAcquisitionAuthorization` | Guard Contract | ACCEPT |
| package barrels own new discoverability | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` | contract export surface | `evaluateCapabilityRoute` | contracts barrel | ACCEPT |
| root barrel owns public package surface | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | root exports | `evaluateCapabilityReadiness` | package root | ACCEPT |
| local profile contract is canonical authority | GOVERNANCE | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/docs/reference/capability_preflight_bootstrap/contracts/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROFILE.md` | full document | `cvf.capabilityPreflightBootstrap.v1` | mixed-origin candidate | REJECT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| planned artifact path existence | all five planned worker paths were absent before dispatch authoring | NEW_PATHS_CONFIRMED |
| exact token search | `rg -n "capability-preflight-profile-policy|Capability Preflight Profile Policy Selection" docs CVF_SESSION EXTENSIONS/CVF_GUARD_CONTRACT` returned no match | NO_COLLISION |
| collision decision | enrich Guard Contract; do not create a parallel root or runtime loader | ENRICH_EXISTING |

## Scope / Methodology

Implement a pure TypeScript module using the selected local files only as
design/use-case evidence. Validate caller-provided unknown input before field
access, then deterministically select an exact requested profile and return a
bounded policy result. Do not read local JSON at runtime.

Required input concepts:

- bounded dense catalog with unique `profileId` values;
- exact `requestedProfileId`, explicit `observedPlatform`, `riskLevel`, and
  caller-provided ISO `now`;
- profile platforms, network mode, install preferences, four risk TTL values,
  explicit privilege policy, bounded path-discovery strings, destinations,
  and notes;
- optional current T4 route/readiness evidence may be consumed only after
  strict validation and may never be strengthened.

Required output concepts:

- deterministic selected profile identity and risk-scoped TTL;
- normalized platform/network/install/path-discovery constraints;
- explicit validation issues and fail-closed disposition;
- literal `executionAuthorized: false`, `acquisitionAuthorized: false`,
  `networkAuthorized: false`, `taskAuthorityGranted: false`, and
  `mutationAuthorized: false` on every return path.

## Functional Requirements

1. Accept `unknown`; reject non-plain objects, proxies/accessors, sparse
   arrays, unknown keys, non-string fields, duplicates, and oversized input.
2. Support the five selected use cases without hard-coding ambient OS:
   `windows-local`, `linux-local`, `macos-local`, `offline-local`, and
   `restricted-network`.
3. Require exact requested-profile lookup and platform membership. Unknown,
   duplicate, or incompatible selections fail closed.
4. Require positive integer TTLs for R0-R3 and monotonic non-increasing TTL as
   risk increases. Bound every TTL to at most 86400 seconds.
5. `OFFLINE` requires zero destinations and installation preferences limited
   to existing or verified-local artifact classes. `RESTRICTED` must never
   infer destination authority; declared destinations remain constraints only.
6. `NORMAL` is a posture label, not network authorization. Every output keeps
   `networkAuthorized: false`.
7. Privilege policy must remain `EXPLICIT_APPROVAL`; installation preferences
   containing approval language do not constitute approval.
8. If T4 evidence is accepted as input, validate its exact current contract
   versions, freshness, issue-free state, binding, and literal false authority.
   Any malformed/stale/ambiguous input fails closed.
9. Reject secret-like field names or values, control characters, unsafe path
   fragments, non-lowercase SHA-256 digests where a digest is accepted, and
   unbounded strings/arrays.
10. Ensure stable issue ordering, stable normalized output, no input mutation,
    and identical output for identical explicit inputs.
11. Export through both current Guard Contract barrels without changing
    existing behavior.

## Allowed Paths

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-preflight-profile-policy.contract.ts` (NEW)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-preflight-profile-policy.contract.test.ts` (NEW)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts`
- `docs/reviews/CVF_RSPB_AI_T7_CAPABILITY_PREFLIGHT_PROFILE_POLICY_SELECTION_KERNEL_WORKER_RETURN_2026-08-16.md` (NEW)

No other path is writable.

## Write Ownership

The worker owns pending edits only to the five allowed paths. The reviewer
owns semantic disposition and any bounded repair. The closer alone owns
staging, commits, closure conversion, and continuity updates.

## Forbidden Actions

- Do not edit current T2/T3/T4/T5/T6 behavior or tests.
- Do not edit checkers, hooks, package files, registries, docs/reference,
  session state, handoff, adapters, CLI/MCP, Web, or public surfaces.
- Do not load the local profiles, inspect the ambient platform, environment,
  filesystem, credentials, or network from production or test code.
- Do not add executor, acquisition, installer, rollback, persistence, or
  mutation behavior.
- Do not stage, commit, push, public-sync, deploy, or invoke a provider.

## Selected Source Inventory

Use the exact eight paths and SHA-256 values in the paired baseline's
`Selected Cluster Evidence`. Recompute them before implementation. A mismatch
requires `BLOCKED_WITH_REASON`; do not silently use changed local evidence.

## Planned Worker Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| new contract source | implement pure validation/selection/policy result |
| new focused test | cover five positive profiles and adversarial fail-closed cases |
| contracts barrel | export all intended types/constants/functions |
| package root barrel | export the same bounded public surface |
| worker return | record exact diff, commands, counts, incidents, and pending status |

## Evidence Requirements

Evidence must include the captured base and initial status, eight hash checks,
exact changed-set output, focused and composed test counts, full package and
TypeScript results, `git diff --check`, worker-return fast-gate result, final
pending status, incident disclosure, and zero external service calls.

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read checker source for its review path and
conditional content. Derive exact structural headings, trace labels, Delta
table labels, corpus/value/rescan tokens, and no-commit evidence shape. Do not
assume this dispatch checklist substitutes for output-specific read-ahead.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_RSPB_AI_T7_CAPABILITY_PREFLIGHT_PROFILE_POLICY_SELECTION_KERNEL_WORKER_RETURN_2026-08-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections, written as real headings in the return: Purpose; Target /
Source; Scope / Methodology; Findings / Position; Risk / Corrective Action;
Decision / Disposition; Claim Boundary; Checker Source Read-Ahead Block;
Agent Operation Trace Block; Delta Execution Claim Boundary Control Block;
Public Export Disposition; Source Verification Block; External Knowledge
Intake Routing; Mixed-Origin Derived Synthesis Provenance; Absorption Decision
Vector; System-Chain Value Review; Corpus Completeness And Report Integrity;
Rescan Intelligence Hardening; Finding-To-Governance Learning Disposition;
Epistemic Process Block.

Record `Status: COMPLETE_PENDING_REVIEW`, full `executionBaseHead`, exact
changed paths, commands/results/counts, incidents, zero external service calls,
and truthful pending `git status --short`. Do not claim closure.

## Verification Commands

Run separately from `EXTENSIONS/CVF_GUARD_CONTRACT`:

```powershell
npx vitest run src/contracts/capability-preflight-profile-policy.contract.test.ts
npx vitest run src/contracts/controlled-acquisition.contract.test.ts src/contracts/capability-route-readiness.contract.test.ts
npm test
npm run check
```

Run from repository root:

```powershell
git diff --check
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

No provider/live opt-in may be set or used. No external service invocation is
authorized.

## Acceptance Criteria

- Exact five-path manifest and no deletions/renames.
- Selected eight local hashes match the baseline.
- Five intended profile use cases pass without ambient detection.
- Negative tests cover malformed/proxy/accessor/sparse/unbounded data,
  duplicates, unknown profile, platform mismatch, invalid TTL ordering,
  offline/restricted network escalation, secrets, stale T4 evidence, and all
  authority literals.
- Focused, T3/T4 regression, full package, TypeScript, diff, and worker-return
  gates pass.
- Worker returns uncommitted `COMPLETE_PENDING_REVIEW`.

## Fail Conditions

Return `BLOCKED_WITH_REASON` if selected hashes drift, a canonical owner
contradicts the contract, any safe solution needs I/O or a sixth path, a
required test cannot run, or any authority output cannot remain literal false.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | external worker -> independent reviewer/orchestrator -> closer |
| phase | worker implementation then independent review |
| baseHeadFor(phase) | dispatchBaseHead=`e27474ca8ee5d57f8340e24c7e1b4896e016da9e`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | worker exact five-path manifest; reviewer bounded repair only after full diff/test matrix |
| traceScope(phase, actor) | worker records pending diff and proof; reviewer independently reproduces and probes |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer only |
| crossBatchIsolation | no unrelated edits or accumulated tranche changes |
| nextMoveSurfaces | completion review and continuity are reviewer/closer-owned |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Existing owner root | `EXTENSIONS/CVF_GUARD_CONTRACT/` |
| New source | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-preflight-profile-policy.contract.ts` |
| New test | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-preflight-profile-policy.contract.test.ts` |
| Existing barrels | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` |
| New roots or generated state | FORBIDDEN |
| Claim boundary | source/test placement only; no loader, store, executor, or runtime service |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_RSPB_AI_T7_CAPABILITY_PREFLIGHT_PROFILE_POLICY_SELECTION_KERNEL_COMPLETION_2026-08-16.md` |
| reviewerOwnedClosurePaths | completion review, work-order closure conversion, material commit, then separate session sync |
| closureOwner | current independent reviewer/orchestrator role |
| workerCommitPermission | FORBIDDEN |

## Review Gate

The reviewer remains distinct from the worker and must inspect the complete
diff before repair. Reviewer independently challenges hostile structures,
profile collisions, TTL/network/privilege escalation, T4 evidence binding,
secret safety, determinism, input mutation, and both barrel exports. Only the
reviewer/closer may accept, repair within manifest, stage, or commit.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatching reviewer/orchestrator; external worker pending |
| Provider or surface | local private provenance repository |
| Session or invocation | RSPB-AI-T7 dispatch, 2026-08-16 |
| Working directory | repository root and Guard Contract package |
| Command or tool surface | governed reads, local hashes, negative search, scaffold, dispatch gates |
| Target paths | paired baseline and work order at dispatch; exact five worker paths at execution |
| Allowed scope source | operator continuation under prior independent worker/reviewer rule |
| Before status evidence | clean worktree at dispatch base before authoring |
| After status evidence | dispatch artifacts pending orchestrator validation and commit |
| Diff evidence | exact two-file dispatch set before continuity sync |
| Approval boundary | worker may edit only five paths and may not commit |
| Claim boundary | no I/O, action authority, provider/live, public, or production claim |
| Agent type | reviewer/orchestrator dispatching external worker |
| Invocation ID | `rspb-ai-t7-profile-policy-dispatch-2026-08-16` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | pure profile-policy contract dispatch |
| claimDisposition | CLAIM_REJECTED: no execution control, runtime enforcement, direct interception, or mandatory wrapper is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: dispatch creates no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no worker implementation has executed |
| invocationBoundary | future explicit TypeScript function call with caller-supplied data only |
| interceptionBoundary | no shell, IDE, filesystem, environment, network, adapter, proxy, or provider interception |
| claimLanguage | deterministic contract candidate pending worker and independent review |
| forbiddenExpansion | profile loading, scanning, acquisition, executor, network, credentials, provider/live, public, deploy, production |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted local ledger -> eight-file cluster -> T2/T3/T4 owner comparison -> pure Guard Contract kernel |
| Matching local-view guard | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py` |
| Owner surface | Guard Contract |
| Disposition | PROCEED_BOUNDED_HIGH_VALUE |
| Claim boundary | no direct import, runtime I/O, adapter, or authority activation |

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
| Owner-surface map | Guard Contract T3/T4 and T2 doctor owner |
| Unresolved items | 0 processing rows; implementation pending review |
| Completion claim boundary | selected-cluster worker dispatch only |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| profile contract | state separation and binding | PACKAGE_CANDIDATE | Guard Contract | adapt | pure contract |
| five profiles | platform/TTL/network use cases | RUNTIME_CANDIDATE | focused implementation/tests | rewrite | no file loading |
| authority policies | no strengthening | DOCTRINE_ADAPTED | contract invariants | encode | no new doctrine owner |
| negative profile cases | fail-closed vocabulary | CHECKER_CANDIDATE | focused tests | adapt | no hook wiring |
| local JSON and policy files as runtime configuration | unsafe parallel configuration authority | REJECT_DIRECT_IMPORT | none | rewrite selected behavior only | no filesystem loading |
| adapters/executor | no selected tranche value | NO_PACKAGE_OR_RUNTIME_VALUE | prior ledger | retain | out of scope |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| route/readiness | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts` | CONFIRMED_EXISTING | accepted evidence | consume only |
| acquisition | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/controlled-acquisition.contract.ts` | CONFIRMED_EXISTING | accepted boundary | preserve |
| snapshot | `scripts/cvf_doctor.py` | CONFIRMED_EXISTING | accepted observation | no scanner work |
| profile policy | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/` | NEW_FINDING | missing deterministic owner | implement |

## Mandatory Blind-Spot Control Block

All eight local files were inspected by content and use case. Their value is
not inferred from names or maturity; direct loading is rejected separately
from knowledge adaptation.

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | selected mixed-origin copied-folder cluster |
| Upstream or source-mirror disposition | accepted predecessor evidence reused; no fetch |
| Enumeration or manifest plan | accepted 205-file ledger and named eight-file cluster |
| Per-file terminal-ledger plan | exact hashes in paired baseline |
| Owner or overlap route | T2/T3/T4 owners and Guard Contract |
| Value-disposition route | pure profile kernel DO_NOW; I/O/adapters deferred |
| Claim boundary | no full scan, direct import, or authority activation |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`
does not own the RSPB corpus. The accepted RSPB 205-row ledger is reused and
this tranche selects eight rows without reopening the legacy index.

## Mixed-Origin Derived Synthesis Provenance

artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE

authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED

The eight selected files provide detailed platform and policy use cases. The
worker must rewrite the behavior within current Guard Contract conventions;
the local documents and JSON remain evidence inputs only.

## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
| --- | --- | --- | --- |
| Knowledge absorption | PROCEED_BOUNDED | eight selected files | one cluster |
| Direct import | REJECT_DIRECT_IMPORT | noncanonical local data | rewrite only |
| Runtime activation | CONTRACT_ONLY | pure function | no I/O |
| Authority promotion | NOT_AUTHORIZED | literal false outputs | reviewer required |

## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
| --- | --- | --- | --- | --- | --- |
| snapshot | T2 doctor | existing | HIGH_VALUE | READY_TO_CONSUME | caller evidence only |
| route/readiness | T4 contract | existing | HIGH_VALUE | READY_TO_CONSUME | validate only |
| acquisition | T3 contract | existing | HIGH_VALUE | CONTRACT_ONLY | constrain only |
| profile policy | selected cluster | missing | HIGH_VALUE | IMPLEMENT_NOW | build pure kernel |

## Corpus Completeness And Report Integrity

- Corpus task class: selected capability-cluster absorption.
- Corpus root: eight selected local files.
- Snapshot time: 2026-08-16.
- Enumeration command: predecessor `rg --files --hidden --no-ignore` plus named selection.
- Manifest artifact or inline manifest: paired baseline Selected Cluster Evidence.
- Manifest hash: eight per-file SHA-256 values in paired baseline.
- Processing ledger artifact or inline ledger: accepted 205-row ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=8; ledger_terminal=8; exclusions=197; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: 197.
- Unreadable or unsupported files: none selected.
- Aggregation check: 8 + 197 = 205.
- Drift check: worker must recompute all selected hashes.
- Output traceability: five worker paths.
- Adversarial verification: required by Functional Requirements.
- Corpus verdict: PARTIAL

## Rescan Intelligence Hardening

- Original source artifact: operator-provided local synthesis folder.
- Predecessor intake artifact: accepted 205-row ledger.
- Delta ledger status: reuse with eight hashes rechecked.
- Routing matrix status: profile cluster to Guard Contract.
- Semantic sampling status: all eight selected files.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Treatment |
| --- | --- |
| UNCHANGED_FROM_INTAKE | 197 excluded files |
| CHANGED_DISPOSITION | eight selected files |
| NEW_FINDING | missing profile-policy seam |
| REMOVED_OR_REJECTED | direct data loading rejected |

### Follow-Up Routing Matrix

| Routing lane | Handling |
| --- | --- |
| DO_NOW | exact five-path implementation |
| SEPARATE_RUNTIME_TRANCHE | file loading/environment observation |
| STRATEGIC_OPERATOR_DECISION | action authority |
| OUT_OF_SCOPE | external services/public/production |
| RESOLVED_BY_DESIGN | explicit inputs and false grants |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| T7-W1 | five profiles | deterministic constraints | ADAPT | collision/platform mismatch | REQUIRE_FAIL_CLOSED |
| T7-W2 | network modes | restrict behavior | ADAPT | network escalation | REQUIRE_LITERAL_FALSE |
| T7-W3 | authority policy | no strengthening | ADAPT | action grant injection | REQUIRE_REJECTION |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Guard Contract root | policy evidence only | focused proof | in-process only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | none | no adapter, auth, loading, or action authority | forbidden | future work order | DEFERRED_WITH_REASON |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| local detailed profiles retain high owner fit | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | continue direct cluster work orders with independent review |

runtimeProviderCostLearningLane: N/A_WITH_REASON - no provider or billed action is authorized.

## Epistemic Process Block

Expected Result / Prediction: detailed profile use cases should yield one
small Guard Contract delta rather than require adapters or a new runtime root.

Evidence Comparison: T2/T3/T4 own the surrounding chain, while exact profile
selection and policy constraints have no current owner.

Contradiction Or Gap Disposition: direct JSON loading and ambient detection
are rejected; only pure validation and constraint projection proceed.

Claim Update: implementation is dispatch-ready and remains unaccepted until
independent review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private worker dispatch; no push or public-sync authority.

## Closure Checklist

- [ ] Worker captured execution base and clean owned paths.
- [ ] Eight selected hashes match.
- [ ] Exact five-path manifest matches.
- [ ] Focused, T3/T4 regression, package, TypeScript, diff, and fast gates pass.
- [ ] Worker returns uncommitted `COMPLETE_PENDING_REVIEW`.
- [ ] Independent reviewer reproduces evidence and decides acceptance/repair.

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | capture base/status and verify eight hashes | worker return inventory |
| 2 | implement source and exact exports | five-path diff |
| 3 | implement adversarial tests | focused test receipt |
| 4 | run focused, regression, full-package, TypeScript, diff, and fast gates | command results and counts |
| 5 | return pending uncommitted handoff | `COMPLETE_PENDING_REVIEW` |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` on any fail condition. Otherwise return
`COMPLETE_PENDING_REVIEW` with all five paths uncommitted for independent
review.

## Claim Boundary

This work order authorizes only the pure profile-policy source, focused test,
two barrel exports, and worker return. It does not authorize profile loading,
environment scanning, acquisition, installation, network access, task or
execution authority, mutation, credentials, adapters, provider/live calls,
public sync, deployment, production, or worker commit.
