# CVF Agent Work Order - EAIC-KR T1 Primary Source Intake

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED_PARKED_KNOWLEDGE_GAP

docType: work_order

Date: 2026-07-22

Batch ID: CVF-EAIC-KR-T1

dispatchBaseHead: `6ce93ecd2`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker selected by the operator

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_EAIC_KR_T1_WORKER_RETURN_2026-07-22.md`

## Dispatch Prompt Envelope

Role: primary-source intake worker for CVF-EAIC-KR-T1.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_2026-07-22.md`

Paired baseline:
`docs/baselines/CVF_GC018_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_2026-07-22.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker must capture the current clean HEAD at start and it
must match the operator-supplied execution base exactly.

Current-time notes: public sources are time-sensitive; record exact URL,
publisher, page title, page version/date when shown, and retrieval timestamp.

Do-not-misread notes: the allowlisted sources are evidence inputs, not selected
providers, CVF authority, executable requirements, or implementation approval.
Do not invoke Claude, Codex, another agent, a provider API, an MCP tool, or an
agent CLI from this worker session.

Required first actions: read the session front door, active state, active
handoff, guard orientation, literal gotchas, paired baseline, this work order,
T0 map, T0 completion review, chain map, and checker sources before writing.

Return contract: create exactly the two worker outputs, run required gates,
leave all changes unstaged and uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Retrieve and reconcile operator-approved official public sources for launch
admission, process identity, cumulative budget, and unknown usage. Produce an
evidence ledger that clearly separates host-specific, protocol, runtime, OS,
API-key, and opaque subscription semantics and recommends either a T2 decision
packet or continued parking.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id EAIC-KR-T1 --title "External Agent Invocation Control Primary Source Intake" --date 2026-07-22 --base 6ce93ecd2 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "EAIC-KR T0 accepted and operator approved bounded T1 intake" --stdout` |
| generatedProfile | source-intake plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact authority, source roots, role routing, evidence, output, and stop rules |
| checkerReadAheadConfirmation | applicable checker constants and regex-sensitive fields were inspected before authoring |
| docOnlyNewFields | sourceAuthorityClass; accessModeClass; domainReadinessDisposition; sourceVolatility |
| claimBoundary | scaffold provenance only; no source correctness, runtime, provider, or implementation claim |

## Authority Chain

- Operator instruction: approved bounded T1 intake on 2026-07-22.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V50_2026-07-22.md`.
- Parent roadmap: `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md`.
- T0 source map: `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md`.
- T0 accepted review: `docs/reviews/CVF_EAIC_KR_T0_COMPLETION_2026-07-22.md`.
- GC-018: `docs/baselines/CVF_GC018_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_2026-07-22.md`.
- Chain map: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

Authority boundary: external documents remain evidence inputs. CVF-owned
ratification, architecture, runtime, and implementation require later packets.

## Agent Roles

- Dispatcher: dispatcher/reviewer role.
- Worker: one manually dispatched worker session.
- Reviewer/closer: independent reviewer/closer.
- Fresh authority required for: any new source root, login, paid access,
  agent/provider invocation, executable test, implementation, T2 release,
  public-sync, or scope expansion.

Provider/model declaration requirement: the worker return records the actual
worker surface, provider, model ID, effort setting, and access mode when known.
Unknown values must be marked `NOT_AVAILABLE_WITH_REASON`; they must not be
guessed and do not affect source acceptance.

## Scope

Risk ceiling: R0 documentation and public-source evidence only.

Allowed scope:

- read repository sources named by this packet;
- retrieve public pages from the six allowlisted official root families in the
  paired baseline;
- use a public search query only to locate exact pages under those roots;
- capture source metadata, bounded paraphrase, and short excerpts totaling no
  more than 25 words from any one source page;
- classify every retrieved source and every CRITICAL domain;
- write only the two worker-owned paths;
- run local read-only verification and governance gates.

Reviewer/closer-only closeout paths (these do not expand worker authority):

- `docs/baselines/CVF_GC018_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_2026-07-22.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_2026-07-22.md`;
- `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md`;
- `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md`;
- `docs/reviews/CVF_EAIC_KR_T1_WORKER_RETURN_2026-07-22.md`;
- `docs/reviews/CVF_EAIC_KR_T1_COMPLETION_REVIEW_2026-07-22.md`;
- separately authorized session continuity surfaces.

Forbidden scope:

- agent CLI/MCP use, separate agent dispatch, provider/model/API request,
  authenticated account access, secret, service token, paid query, or quota;
- process execution or termination test against any agent host;
- evidence from third-party pages, search summaries, social content, generated
  answers, provider-local memory, or chat history;
- download, clone, install, execute, modify runtime/source/tests/checkers,
  update standards/roadmaps/registries/session/handoff, or public-sync;
- architecture selection, schema ratification, fail-closed policy ratification,
  implementation recommendation framed as authorization, or moratorium lift;
- stage, commit, push, merge, publish, delete, or rename.

Reviewer closure Allowed scope:

- `docs/baselines/CVF_GC018_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_2026-07-22.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_2026-07-22.md`;
- `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md`;
- `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md`;
- `docs/reviews/CVF_EAIC_KR_T1_WORKER_RETURN_2026-07-22.md`;
- `docs/reviews/CVF_EAIC_KR_T1_COMPLETION_REVIEW_2026-07-22.md`;
- separately authorized session continuity surfaces.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| accepted T0 | `docs/reviews/CVF_EAIC_KR_T0_COMPLETION_2026-07-22.md`; correction commit `77d75ef93` | T0 must close with explicit CRITICAL source gaps | SATISFIED |
| operator source approval | operator approved the recommended official-source T1 intake on 2026-07-22 | network retrieval must be limited to packet roots | SATISFIED |
| clean dispatch base | `git status --short` empty at `6ce93ecd2` | dispatch packet starts from a clean provenance worktree | SATISFIED |

## Worker Autonomy / No-Question Rule

Proceed autonomously with read-only repository inspection, allowlisted public
source retrieval, ledger authoring, local evidence checks, and allowed-scope
format repair. Return to the orchestrator only when an exact source root is
insufficient, contradictory evidence cannot be represented safely, an action
would require login or execution, or a required repair exceeds Allowed scope.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`source-intake`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class source-intake --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no resolver-returned pattern adds a control to this packet |

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | operator-authorized official public-source intake |
| Route | `MULTI_AGENT_SINGLE_ROLE` |
| risk sensitivity | R0 documentation and public-source evidence only |
| selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Worker role | one worker creates the evidence ledger and worker return only |
| Reviewer role | independent reviewer/closer verifies sources, repairs, commits, and syncs if accepted |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | satisfied for allowlisted source retrieval; fresh authority required for scope expansion |
| escalation condition | non-allowlisted root, login, paid access, executable test, agent/provider invocation, implementation, public-sync, or claim-boundary change |

## Required First Reads

| Path | Action | Reason |
| --- | --- | --- |
| `CVF_SESSION_MEMORY.md` | FULL_READ | active mode and parked boundaries |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | FULL_READ | active handoff and canonical state |
| `AGENT_HANDOFF_V50_2026-07-22.md` | FULL_READ | current closure and no-invocation boundary |
| `docs/reference/guard_orientation/README.md` | FULL_READ | role and task guard routing |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ | prevent repeated literal-shape repair loops |
| paired baseline and this work order | FULL_READ | exact authority and scope |
| parent roadmap, T0 map, and T0 completion review | FULL_READ | unresolved questions and accepted boundary |
| external knowledge chain map and external review front door | FULL_READ | authority and intake routing |
| checker sources in Checker Source Read-Ahead Block | SOURCE_VERIFIED | output-specific required shape |

## Pre-Flight Checks

The operator supplies the current execution base when manually dispatching.
Before any source retrieval or file edit, run:

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
Test-Path docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md
Test-Path docs/reviews/CVF_EAIC_KR_T1_WORKER_RETURN_2026-07-22.md
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected: HEAD matches the operator-supplied base, worktree is clean, both
planned outputs are absent, and pre-implementation passes. Any mismatch returns
`BLOCKED_WITH_REASON` before source retrieval.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md`

priorVerificationAnchor: accepted T0 correction commit `77d75ef93`

freshRecomputeRequired: retrieve current official pages and recheck every T0
CRITICAL gap against them; do not rerun unrelated T0 repository inventory.

unicodePathHandling: use literal paths and UTF-8-safe readers; worker-authored
governed prose remains ASCII.

extractedTextAuthority: page text is external evidence only; the worker's
normalized paraphrase and source metadata are review inputs, not CVF authority.

recomputeReason: external public documentation is time-sensitive and must be
retrieved fresh within the approved roots.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Intake Decision Packet; External Absorption Core; External Absorption Value Conversion Matrix; Overlap And Novelty Classification; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Worker Return Packet Shape Contract; Public Export Disposition |
| gateRunPurpose | confirm work-order and planned-output shape after checker-source read-ahead |
| claimBoundary | checker alignment is dispatch evidence only and does not prove external-source accuracy |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T1 owns primary-source reconciliation | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Work Plan T1 row | `T1` | EAIC-KR roadmap | ACCEPT |
| T1 requires recorded source/network authorization | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Roadmap Release Rules | `T1` | EAIC-KR roadmap | ACCEPT |
| launch admission is CRITICAL and missing primary knowledge | VALUE_SET | `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md` | Knowledge Gap And Source Acquisition Map row 1 | `Launch admission` | T0 knowledge map | ACCEPT |
| process identity is CRITICAL and missing primary knowledge | VALUE_SET | `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md` | Knowledge Gap And Source Acquisition Map row 2 | `Process identity` | T0 knowledge map | ACCEPT |
| cumulative budget is CRITICAL and missing primary knowledge | VALUE_SET | `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md` | Knowledge Gap And Source Acquisition Map row 5 | `Cumulative budget` | T0 knowledge map | ACCEPT |
| unknown usage is CRITICAL and missing primary knowledge | VALUE_SET | `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md` | Knowledge Gap And Source Acquisition Map row 6 | `Unknown usage` | T0 knowledge map | ACCEPT |
| external input must remain advisory until reconciled | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Central Core | `Central Core` | external knowledge chain map | ACCEPT |

The approved external roots are new intake targets, not existing CVF runtime
fields. They are therefore declared below rather than represented as current
source facts.

## New Doc-Only Fields

| Field | Purpose |
| --- | --- |
| sourceAuthorityClass | PRIMARY_OFFICIAL, SUPPORTING_OFFICIAL, DISCOVERY_ONLY, or REJECTED_NON_PRIMARY |
| accessModeClass | API_KEY, ACCOUNT_SUBSCRIPTION, LOCAL_PROCESS, PROTOCOL, OS_RUNTIME, or UNKNOWN |
| domainReadinessDisposition | READY_FOR_T2_DECISION, PARTIAL_REMAINS, OPAQUE_REQUIRES_OPERATOR_POLICY, or BLOCKED_MISSING_PRIMARY_SOURCE |
| sourceVolatility | STABLE_SPEC, VERSIONED_DOC, CURRENT_PRODUCT_DOC, or CURRENT_SUPPORT_DOC |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| planned artifact existence | dispatcher `Test-Path` returned false for both worker outputs | ACCEPT |
| exact batch search | `rg -n "EAIC.KR.T1.PRIMARY.SOURCE.INTAKE|EAIC-KR-T1" docs CVF_SESSION` returned no prior T1 artifact | ACCEPT |
| runtime-field collision | all new fields are in New Doc-Only Fields and must not be claimed as existing schemas | ACCEPT |
| external evidence collision | duplicate pages or mirrored copies must resolve to one official canonical URL row | ACCEPT |

Source intake decision packet: REQUIRED

## Source Intake Decision Packet

| Field | Value |
| --- | --- |
| Decision packet standard | `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` |
| Input root or repository | six official public root families listed in the paired baseline |
| Bounded scope | four CRITICAL T0 domains only |
| Enumeration authority | worker records every retrieved official page in the ledger Source Manifest |
| Owner-surface taxonomy | existing EAIC reference family; new implementation owner is forbidden |
| Pre-scan packet source | T0 knowledge gap and source acquisition map |
| Overlap routing matrix | compare every source claim against T0 evidence and existing CVF owners |
| Negative-search evidence | exact URLs, redirects, duplicate canonical pages, and missing official answers recorded per query |
| Core disposition | ADAPT official-source evidence into the bounded T1 ledger |
| Value conversion requirement | classify doctrine, later runtime candidate, later checker candidate, or no runtime value without implementation |
| Overlap classification requirement | use confirmed, enriched, new-gap, rejected-direct-import, no-new-value, or owner-missing disposition |
| Worker output path | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md` |
| Forbidden scope | login, paid access, agent/provider execution, source import, runtime/checker build, policy ratification, or public release |
| Claim boundary | knowledge intake and readiness recommendation only |

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | allowlisted official public documentation roots in paired baseline |
| Enumeration command | browser/source retrieval log plus ledger Source Manifest; no filesystem clone |
| Manifest artifact or inline manifest | T1 ledger Source Manifest |
| Processing ledger artifact or inline ledger | T1 ledger Per-Source Processing Ledger |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | EAIC T0 map and T1 ledger; architecture owner remains undecided |
| Unresolved items | explicit per-domain list required at return |
| Completion claim boundary | bounded public-source evidence only; no runtime, provider, public, or production expansion |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| official host documentation | host-specific launch, identity, and usage semantics | DOCTRINE_ADAPTED or RUNTIME_CANDIDATE | T1 ledger and later T2 decision packet | reviewer decides whether evidence is sufficient for T2 | no adapter or process implementation |
| protocol and OS/runtime specifications | portable and platform-specific primitives | DOCTRINE_ADAPTED or RUNTIME_CANDIDATE | T1 ledger | preserve non-equivalent semantics | no conformance inference or executable test |
| absent or opaque official evidence | explicit unresolved gap | NO_PACKAGE_OR_RUNTIME_VALUE | T1 ledger unresolved rows | remain parked or request operator policy | no implementation from absence |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| host launch and session docs | T0 launch-admission and process-identity rows | ENRICH_EXISTING | exact host-visible identifiers or hooks, if documented | adapt evidence; do not select an owner |
| usage and subscription docs | T0 usage, cumulative-budget, and unknown-usage rows | ENRICH_EXISTING or NO_NEW_VALUE | access-mode visibility boundary | preserve opacity and operator-policy need |
| MCP and process specifications | current command launcher and MCP contract evidence | CONFIRMED_EXISTING or NEW_FINDING | protocol/OS primitive not yet mapped | map to T1 evidence; later architecture decision only |

For any `NEW_FINDING`, record the negative search command and result in the T1
ledger, then route the item to a concrete next governed action in the later T2
decision packet or keep it parked with reason.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | official source retrieval -> authority classification -> T0 overlap comparison -> four-domain readiness ledger -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | `docs/reference/external_agent_invocation_control/` family |
| Disposition | ADAPT primary-source knowledge; reject direct implementation import |
| Claim boundary | accepted sources inform a later decision packet but do not authorize architecture or runtime |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | manually dispatched parent worker session | provider-native reasoning and internal helpers remain autonomous inside scope | worker trace and output manifest | no per-helper CVF adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no invocation interface released | no separate session or perimeter-crossing invocation is authorized | zero invocation counters required | future adapter remains parked | `DEFERRED_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> one worker -> independent reviewer/closer |
| phase | pre-implementation worker dispatch |
| baseHeadFor(phase) | dispatchBaseHead=`6ce93ecd2`; executionBaseHead must match operator-supplied current HEAD; closureBaseHead is reviewer-captured |
| changedSetScope(phase) | exactly two worker-owned output paths |
| traceScope(phase, actor) | worker records repository commands, public-source URLs, retrieval surface, provider/model declaration, internal-helper count when observable, and zero forbidden invocation counts |
| commitOwner(phase) | reviewer/closer; worker commit permission is forbidden |
| crossBatchIsolation | ignore and do not touch every path outside the two worker outputs |
| nextMoveSurfaces | worker does not update roadmap or continuity; reviewer decides T2 readiness and sync |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAIC_KR_T1_COMPLETION_REVIEW_2026-07-22.md` |
| reviewerOwnedClosurePaths | paired baseline; this work order; parent roadmap; T1 ledger; worker return; completion review; separately authorized continuity surfaces |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Required Artifact Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md` | create reconciled manifest, per-source ledger, domain matrix, gaps, and recommendation |
| `docs/reviews/CVF_EAIC_KR_T1_WORKER_RETURN_2026-07-22.md` | create no-commit evidence and gate return packet |

Every other path is read-only or forbidden for writes.

## Write Ownership

Worker-owned create-only paths:

- `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md`;
- `docs/reviews/CVF_EAIC_KR_T1_WORKER_RETURN_2026-07-22.md`.

Write mode: create-only, unstaged, uncommitted.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| durable owner family | `docs/reference/external_agent_invocation_control/` |
| new durable artifact | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md` |
| owner front door | `docs/reference/external_agent_invocation_control/README.md` remains the stable family front door and is read-only in this worker tranche |
| storage class | governed evidence ledger, not runtime state, raw web archive, cache, queue, or provider memory |
| index/update disposition | reviewer decides whether the existing front door needs a later closure update; worker must not modify it |
| generated aggregate disposition | N/A with reason: this Markdown ledger has no generated aggregate owner |
| claim boundary | durable private evidence only; no runtime, public, provider, or production authority |

## Worker Output Checker Read-Ahead Mandate

Before writing the ledger, derive its exact reference headings, source-intake
sections, corpus/value/overlap fields, trace applicability, and claim boundary
from the listed checker sources. Before writing the return, derive review
structural groups, worker-return terms, trace fields, epistemic fields, Delta
boundary fields, public disposition, and no-commit evidence shape.

Required worker-return section names include: Purpose; Target / Source; Scope /
Methodology; Findings / Position; Decision / Disposition; Risk / Corrective
Action; Source Inventory; Checker Source Read-Ahead Block; External Knowledge
Intake Routing; Epistemic Process Block; Finding-To-Governance Learning
Disposition; Agent Operation Trace Block; Delta Execution Claim Boundary
Control Block; Public Export Disposition; Claim Boundary; git status --short;
Changed Files; No-Commit Statement.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAIC_KR_T1_WORKER_RETURN_2026-07-22.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Execution Plan

| Step | Action | Output/evidence | Stop condition |
| --- | --- | --- | --- |
| 1 | capture base, clean status, and pre-implementation gate | command transcript | mismatch, dirty path, or failed gate |
| 2 | create short worker-return scaffold and read output-specific checkers | checker-safe skeleton | required output shape unresolved |
| 3 | retrieve exact official pages within allowlist | Source Manifest with URL and timestamp | login, paid access, redirect outside allowlist, or unavailable page |
| 4 | classify every source and compare with T0 | Per-Source Processing Ledger and overlap matrix | source authority ambiguous |
| 5 | resolve all four domains without inference | Domain Readiness Matrix | any domain lacks a terminal disposition |
| 6 | write bounded recommendation and worker return | two output paths | architecture or policy ratification would be required |
| 7 | run final gates and status evidence | gate output and pending manifest | failure outside Allowed scope |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| absorb operator-approved primary sources | Source Intake Decision Packet | ledger Source Manifest | reviewer checks every URL root | PASS |
| reconcile knowledge rather than import implementation | External Absorption Core | per-source and overlap ledgers | semantic reviewer audit | PASS |
| preserve provider neutrality | source roots and Dual Agent Surface Matrix | host-specific rows remain separate | domain matrix inspection | PASS |
| keep invocation moratorium | Scope and Delta boundary | zero forbidden invocation counters | worker trace and return | PASS |
| stop when knowledge remains insufficient | Epistemic block and terminal recommendation | overall T1 disposition | reviewer comparison with four T0 gaps | PASS |
| no automatic T2 release | Reviewer Closure Conversion | reviewer-owned decision | completion review | PASS |

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
| --- | --- | --- | --- |
| knowledge before architecture | Design Control Gate | T1 writes evidence only | PASS |
| architecture before implementation | Design Control Gate | no schema or runtime owner selected | PASS |
| provider neutrality | Design Control Gate | representative hosts remain separate evidence classes | PASS |
| fail-closed unknown usage | Design Control Gate | T1 gathers evidence but does not ratify policy | PASS |
| external-service authority | Roadmap Release Rules plus recorded 2026-07-22 authorization | only public-source retrieval is released | PASS |
| acceptance and stop rule | Knowledge Sufficiency Stop Rule | continued park is an accepted outcome | PASS |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: official protocol and process documents will
clarify primitives, while agent-host subscription telemetry and cumulative
budget ownership may remain incomplete or opaque.

Evidence Comparison Requirement: compare actual source findings against each
T0 question and the prediction.

Contradiction Handling Requirement: use a Contradiction Or Gap Disposition;
do not merge differing host, access-mode, OS, runtime, or protocol semantics.

Claim Update Requirement: classify each domain as
`READY_FOR_T2_DECISION`, `PARTIAL_REMAINS`,
`OPAQUE_REQUIRES_OPERATOR_POLICY`, or
`BLOCKED_MISSING_PRIMARY_SOURCE`, then recommend exactly one of
`READY_FOR_T2_DECISION_PACKET` or `PARKED_KNOWLEDGE_GAP`.

## Evidence Requirements

The ledger must include:

- Source Manifest: source ID, exact URL, official publisher, title,
  version/date, retrieved-at timestamp, source class, access-mode class,
  volatility, and terminal processing status;
- Query Ledger: query/domain, approved root, exact query or navigation route,
  result URL or no-result disposition;
- Per-Source Processing Ledger: supported claim, prohibited inference, T0
  overlap, disposition, and owner surface;
- four-row Domain Readiness Matrix with source IDs, remaining gap, terminal
  disposition, operator policy need, and blocked next decision;
- External Absorption Value Conversion Matrix;
- Overlap And Novelty Classification;
- contradiction/gap ledger;
- evidence-quality and copyright boundary: paraphrase by default and no more
  than 25 quoted words from one source page;
- one bounded overall recommendation.

The worker return must report:

- executionBaseHead and actual pending `git status --short`;
- provider/model/surface/effort/access-mode declaration when known;
- `internalSubagentInvocationCount` when observable;
- `agentCliCallCount=0`, `mcpCallCount=0`, `providerCallCount=0`,
  `apiCallCount=0`, and `authenticatedAccountAccessCount=0`;
- public retrieval count and accepted-source count;
- every final command exactly as run.

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_external_knowledge_intake_routing.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_source_intake_decision_packet_preflight.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git status --short --untracked-files=all
```

## Acceptance Criteria

- [x] exactly two worker-owned output paths existed at worker return; reviewer closure repairs are separately accounted;
- [x] every accepted source is official, public, allowlisted, and metadata-complete;
- [x] every retrieval query has a terminal result, including reviewer-refreshed rows;
- [x] all four CRITICAL domains have exactly one terminal readiness disposition;
- [x] provider, access-mode, protocol, OS, and runtime semantics remain distinct;
- [x] no implementation, policy ratification, or provider preference is inferred;
- [x] overall recommendation is exactly one allowed token;
- [x] worker-return fast gate and listed checks pass after reviewer final edits;
- [x] worker changes remained unstaged and uncommitted at return.

Fail conditions:

- a source needs login, secret, payment, executable test, or non-allowlisted root;
- third-party or generated content is used as accepted evidence;
- a missing source is replaced by inference;
- a host-specific fact is promoted to a provider-neutral guarantee;
- output claims T2 release, runtime control, cost savings, or moratorium lift;
- changed set exceeds the two worker-owned paths;
- a required gate cannot pass inside Allowed scope.

## Review Gate

Worker handoff is `COMPLETE_PENDING_REVIEW`, not closure. The independent
reviewer recomputes source counts, opens every accepted URL when feasible,
checks high-risk paraphrases, verifies all four domain dispositions, and may
return `PARKED_KNOWLEDGE_GAP` even when machine gates pass. Only the operator
may release T2 through a later source-verified decision packet.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher/reviewer role |
| Provider or surface | local provenance repository; no external agent invocation |
| Session or invocation | EAIC-KR-T1 packet authoring, 2026-07-22 |
| Working directory | repository root |
| Command or tool surface | local PowerShell, rg, Git reads, scaffold helper, ADIF resolver, apply_patch, governance gates |
| Target paths | parent roadmap; paired baseline; this work order |
| Allowed scope source | recorded 2026-07-22 authorization for bounded T1 official-source intake |
| Before status evidence | clean worktree at HEAD `6ce93ecd2` |
| After status evidence | three-path dispatch packet pending gate validation |
| Diff evidence | `git status --short`; `git diff --name-status` |
| Approval boundary | packet authoring and future manual worker dispatch only |
| Claim boundary | repo-local dispatch trace; no provider, process, or source-content correctness proof |
| Agent type | dispatcher/reviewer |
| Invocation ID | `eaic-kr-t1-dispatch-2026-07-22` |
| Expected manifest | parent roadmap; paired baseline; this work order |
| Actual changed set | parent roadmap; paired baseline; this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | public-source evidence intake for four EAIC knowledge gaps |
| claimDisposition | CLAIM_REJECTED: no execution-control or runtime-enforcement behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no agent/provider/runtime receipt is created |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local packet authoring and later public-page retrieval only |
| invocationBoundary | manual parent worker session; no external agent CLI/MCP/provider/API invocation |
| interceptionBoundary | no IDE, shell, Git, filesystem, provider, process, or internal-reasoning interception claim |
| claimLanguage | bounded source reconciliation and readiness recommendation only |
| forbiddenExpansion | no implementation, process test, provider selection, policy ratification, T2 release, public-sync, or moratorium lift |

## Worker Pending-Return Gate

| Check | Required worker result |
| --- | --- |
| output manifest | exactly two untracked worker paths |
| staging state | nothing staged |
| base state | executionBaseHead matches operator value |
| worker-return gate | PASS after final edit |
| source-intake checks | PASS after final edit |
| return status | COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON |

## Operator Checkpoint

The source-root checkpoint is satisfied only for public retrieval within the
paired baseline allowlist. A fresh operator checkpoint is required before any
new root, authenticated source, executable test, T2 packet release,
implementation, provider use, or public action.

## Closure Checklist

- [x] worker outputs were exactly the two owned paths at handoff;
- [x] all accepted sources and no-result queries have terminal rows;
- [x] all four CRITICAL domains have terminal readiness dispositions;
- [x] reviewer checked semantic accuracy and provider-neutral boundaries;
- [x] worker-return and source-intake gates pass after final edits;
- [x] reviewer converted every item to checked, N/A with reason, or BLOCKED;
- [x] material and continuity commits are assigned to separate lanes;
- [x] committed-range pre-closure gate is required before the final closure report.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` when base/worktree preflight fails, either output
already exists, required official evidence needs login or execution, the
allowlist is insufficient, an exact domain cannot receive an honest terminal
disposition, or completion requires any forbidden action.

## Claim Boundary

This work order authorizes one no-commit official-source intake and two worker
outputs. It neither selects nor invokes a provider or agent host, and it does
not ratify architecture, budget, telemetry, fail-closed behavior, runtime,
security, public, cost, or production claims.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Baseline status | paired T1 baseline | `Status: CLOSED_PASS_BOUNDED_PARKED_KNOWLEDGE_GAP` | PASS |
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED_PARKED_KNOWLEDGE_GAP` | PASS |
| Completion or reviewer artifact | T1 completion review | `Status: REVIEWER_ACCEPTED_PARKED_KNOWLEDGE_GAP` | PASS |
| Roadmap state | EAIC-KR roadmap | `Status: T1_PASS_BOUNDED_PARKED_KNOWLEDGE_GAP` | PASS |
| Registry JSON | existing generated corpus registry | GC-051 aggregate drift PASS; public web pages are not local corpus candidates | PASS |
| Registry Markdown | existing corpus registry source layout | changed-corpus coverage PASS; no new local corpus root exists | PASS |
| External evidence digest | N/A with reason: official pages are represented by the repo-local source manifest, not a detached external artifact | none | N/A with reason |
| System loop interlock | N/A with reason: no runtime loop changed | none | N/A with reason |
| Session continuity | active state and V51 handoff | separate continuity commit | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
| --- | --- | --- | --- | --- | --- |
| T1-SOURCE-COUNT | stable T1 source-intake ledger | N/A with reason: Markdown ledger | 15 reconciled source IDs | 15 | PASS |
| T1-DOMAIN-COUNT | stable T1 source-intake ledger | N/A with reason: Markdown ledger | four terminal CRITICAL domains | four | PASS |

## Current Runtime Freshness Verification

At closure base `d000aa35b`, `git diff --name-status` shows documentation-only
T1 changes. No runtime, source, test, checker, hook, package, or generated
runtime state path changed. The completion review independently refreshed the
official source claims; no runtime-effectiveness claim is made.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private knowledge-readiness evidence with no public implementation or
release authority.
