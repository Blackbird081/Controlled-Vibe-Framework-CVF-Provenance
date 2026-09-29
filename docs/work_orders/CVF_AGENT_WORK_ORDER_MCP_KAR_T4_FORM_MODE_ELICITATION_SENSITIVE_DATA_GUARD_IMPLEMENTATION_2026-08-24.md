# CVF Agent Work Order - MCP-KAR-T4 Form-Mode Elicitation Sensitive-Data Guard Implementation

Memory class: governed-work-order

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: MCP-KAR-T4

Dispatch base head: 583c0911a8049e708bc1a75648ea6eeb907fb167

Commit mode: WORKER_MUST_NOT_COMMIT

Worker target: implementation worker subagent

Reviewer/closer: parent agent

## Dispatch Prompt Envelope

```text
Implement only committed MCP-KAR-T4. Read its baseline and this work order,
then the exact authorities and checker sources they name. Touch only the four
implementation paths plus the one worker-return path in the fulfillment
manifest. Add pure local MCP-PR-011 with a closed category vocabulary and
fail-closed form-mode sensitive-data admission. Preserve the existing composite
profile. Do not access raw secret values or open runtime/package/transport/
fixture/session/provider/live/public/deploy/production lanes. Run the required
checks, write one complete uncommitted worker return, and do not stage or commit.
```

## Purpose

Convert the reviewer-accepted T3 owner/value decision into the smallest
deterministic local MCP invariant implementation and focused regression proof.

## Authority Chain

1. Operator autonomous valuable-absorption instruction dated 2026-08-24.
2. T3 accepted closure `c62f926f27b7c98390e937fc0ca8063af9040611`.
3. T3 worker return exact four-path later manifest.
4. This baseline and work order at dispatch base
   `583c0911a8049e708bc1a75648ea6eeb907fb167`.
5. Canonical CVF standards and applicable machine guards.

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| operator | human operator | selected autonomous valuable absorption within CVF rules |
| dispatcher | parent agent | committed bounded authority packet |
| worker | separate implementation subagent | implement, verify, and return without commit |
| reviewer/closer | parent agent | independent semantic review, repair decision, commits, and continuity |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| operator selection | 2026-08-24 autonomous valuable-absorption instruction | fresh selection for valuable local tranche | RELEASED |
| T3 decision | accepted `PROCEED_ELICITATION_GUARD` at `c62f926f2`; exact four-path manifest | all five T3 gates PASS and reviewer acceptance | RELEASED |

## Worker Autonomy / No-Question Rule

Proceed autonomously inside the exact manifest. Ask only if a governed source
contradiction or forbidden dependency makes safe implementation impossible.
Routine implementation choices must be resolved from current source and tests.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`MCP form-mode elicitation sensitive-data guard implementation dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "MCP form-mode elicitation sensitive-data guard implementation dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned none |
| Dispatch impact | canonical guards remain binding |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MCP-KAR-T4 --title "Form-Mode Elicitation Sensitive-Data Guard Implementation" --date 2026-08-24 --base 583c0911a8049e708bc1a75648ea6eeb907fb167 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MCP-KAR-T3 reviewer-accepted closure c62f926f2; operator authorized autonomous valuable absorption on 2026-08-24" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker and MCP/CLI boundary stubs |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact authority, behavior contract, manifest, tests, handoff, and held boundaries |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| docOnlyNewFields | `elicitationMode`; `requestedDataCategories`; `MCP-PR-011`; `UNSAFE_ELICITATION_REQUEST` |
| claimBoundary | dispatch authoring and one expected no-commit worker return |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | Dispatch Prompt Envelope placement; source columns; manifest; worker-return declarations; trace labels; Delta enums; adapter and public boundaries |
| gateRunPurpose | confirm authored dispatch completeness and record evidence before implementation; gates are not first-discovery tools |
| claimBoundary | T4 bounded local implementation |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T3 approved exact implementation owner | GOVERNED_REVIEW | `docs/reviews/CVF_MCP_KAR_T3_FORM_MODE_ELICITATION_SENSITIVE_DATA_OWNER_VALUE_DECISION_WORKER_RETURN_2026-08-24.md` | Decision / Disposition; Reviewer Decision | `PROCEED_ELICITATION_GUARD`; four-path manifest | T3 accepted closure | ACCEPT |
| reference owns invariant vocabulary | GOVERNED_REFERENCE | `docs/reference/mcp_gateway/CVF_MCP_NORMATIVE_INVARIANT_PROFILE.md` | Protocol Contract / Normative Mapping and Requirements | `MCP-PR-001` through `MCP-PR-010`; local named codes | MCP gateway reference | ACCEPT |
| source owns pure composition | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | lines 77-111 | `MCPProtocolInvariantProfileInput`; `evaluate` | execution-plane foundation | ACCEPT |
| focused oracle exists | TEST_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mcp.protocol.invariant.profile.test.ts` | `validInput`; profile suite | accepted composite and negative rule checks | focused test owner | ACCEPT |
| barrel export exists | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | lines 40-49 | `createMCPProtocolInvariantProfile` | execution-plane barrel | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact rule | T3 fresh search found no existing form-mode category admission rule | PASS_WITH_GAP_OBSERVED |
| exact owner | existing invariant profile is selected; parallel owner forbidden | PASS |
| decision code | worker must search source/test roots for `UNSAFE_ELICITATION_REQUEST` before adding it | PASS_REQUIRES_FRESH_WORKER_CHECK |
| negative-search command/root/query | `git grep -n "UNSAFE_ELICITATION_REQUEST\|MCP-PR-011" -- docs/reference/mcp_gateway EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests` | REQUIRED_BEFORE_EDIT |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intakeRoute | REUSE_ACCEPTED_T3_EXACT_MANIFEST |
| routeMode | MULTI_AGENT_MULTI_ROLE |
| scopeClassification | BOUNDED_LOCAL_IMPLEMENTATION_NO_EXTERNAL_EFFECT |
| selectedRoleRoute | committed parent dispatch, separate no-commit worker, parent reviewer/closer |
| riskSensitivity | security-sensitive pre-collection category boundary; raw secrets and external effects forbidden |
| workerRole | pure local implementation and evidence worker |
| reviewerRole | independently inspect semantics/tests and own commits/continuity |
| authorityBoundary | T3 and current CVF sources; external material grants no authority |
| escalationRoute | return blocked only for source contradiction or forbidden dependency |

## Scope / Methodology

Allowed:

- add `MCP-PR-011` and a closed typed elicitation mode/category vocabulary;
- add a category-only input seam to the existing aggregate evaluator;
- update the normative mapping and focused tests;
- retain or confirm the current barrel export without widening it;
- write exactly one worker return and run local deterministic checks.

Required semantics:

- form mode rejects password, API-key, access-token, and payment-credential
  categories with a source-verified local code such as
  `UNSAFE_ELICITATION_REQUEST`;
- unknown or malformed categories fail closed in form mode;
- URL mode permits sensitive categories;
- ordinary contact/profile form categories are accepted;
- no raw values, example credentials, secret payloads, storage, logging, or
  returned secret content;
- existing ten rules and accepted composite behavior remain intact.

Forbidden:

- any path outside the fulfillment manifest;
- runtime bridge, package manifest, dependency, transport, adapter, fixture
  import, session/handoff, checker, registry, generated aggregate, or roadmap;
- network, credential, provider/live, public, deployment, or production action;
- worker staging or commit.

## Required First Reads

- startup bootstrap/front door and active handoff;
- guard orientation and literal-format gotchas;
- committed T4 baseline and work order;
- T3 worker return and its four-path manifest;
- all four implementation paths;
- the package manifest needed only to select existing local test/typecheck commands;
- worker-return and applicable governance checker sources.

## Pre-Flight Checks

Capture the clean committed dispatch HEAD as `executionBaseHead`; verify exact
allowed paths; run pre-implementation autorun; run the collision search. Stop
only for contradiction or forbidden dependency.

## Write Ownership

The worker owns exactly the four implementation paths and one worker-return
path listed in the fulfillment manifest. It must leave all changes unstaged and
uncommitted. Reviewer/closer owns acceptance and commits.

## Execution Plan

1. Verify base, clean status, sources, and collision results.
2. Define minimal closed types for mode and requested-data categories.
3. Add `MCP-PR-011` to the existing evaluator without changing prior ordering.
4. Add normative reference mapping and claim boundary.
5. Add focused positive, negative, malformed, URL-mode, and composite tests.
6. Verify the existing export remains sufficient; avoid unrelated export churn.
7. Run focused tests, TypeScript, pre-implementation/worker-return gates.
8. Write one complete worker return and do not stage or commit.

## Acceptance Criteria

- exact manifest only and `MCP-PR-011` pure/local/side-effect-free;
- closed category vocabulary with form-sensitive and unknown/malformed
  fail-closed behavior;
- sensitive URL mode and general contact/profile form mode accepted;
- no raw secret-value input, output, logging, storage, or test material;
- existing composite profile and prior rules pass unchanged;
- focused tests and TypeScript PASS;
- worker-return fast gate PASS; zero provider/network/live calls;
- worker leaves complete changes uncommitted for reviewer.

## Evidence Requirements

Record execution base, before/after status, exact changed paths, collision-search
results, source symbols, category-vocabulary design, rule ordering, focused test
names and counts, TypeScript result, governance gate results, zero raw-value
proof, zero external-effect count, and any bounded deviation from the expected
barrel-export action.

## Review Gate

Reviewer must inspect the complete changed set before repair, verify type and
semantic closure, confirm no raw-value seam, rerun focused tests/TypeScript and
reviewer-fast/pre-closure gates, then accept or return bounded repair.

## Closure Checklist

- all acceptance criteria source-backed;
- exact manifest and no deletion/rename drift;
- worker return reconciles commands, tests, status, and claims;
- reviewer owns material commit; session continuity is a separate commit;
- no runtime/external lane opened;
- Public Export Disposition explicit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` with a complete passing packet, or
`BLOCKED_WITH_REASON` only for a genuine authority contradiction or forbidden
dependency. Do not return routine allowed-scope questions.

## Verification Commands

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git grep -n "UNSAFE_ELICITATION_REQUEST\|MCP-PR-011" -- docs/reference/mcp_gateway EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests
npm test -- --run tests/mcp.protocol.invariant.profile.test.ts
npm run typecheck
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

Use the package's actual existing script spelling if it differs; record the
working directory and exact command rather than modifying package metadata.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_MCP_KAR_T3_FORM_MODE_ELICITATION_SENSITIVE_DATA_OWNER_VALUE_DECISION_WORKER_RETURN_2026-08-24.md`

priorVerificationAnchor: T3 accepted closure `c62f926f27b7c98390e937fc0ca8063af9040611`

freshRecomputeRequired: collision search, exact base/status, focused tests,
TypeScript, semantic inspection, exact changed set, and governance gates

unicodePathHandling: literal UTF-8 paths and direct reads

extractedTextAuthority: governed sources and current code only

No fresh corpus scan or completeness claim is authorized.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | normative profile plus pure invariant evaluator | category admission only; no raw values | focused local tests | N/A with reason: direct local contract | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | possible future form-mode caller | no transport, input collection, receipt, or mutation authority | future work order required | deferred adapter/runtime | `DEFERRED_WITH_REASON` |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| form-mode sensitive-category rejection | `docs/reference/mcp_gateway/CVF_MCP_NORMATIVE_INVARIANT_PROFILE.md`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | `ENRICH_EXISTING` | existing profile lacks pre-collection elicitation admission | add MCP-PR-011 in existing owner |
| generic secret handling | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.ts` | `CONFIRMED_EXISTING` | post-input evidence detection is a different phase | leave unchanged |
| external negative fixture | `docs/audits/CVF_MCP_KAR_T0_EXTERNAL_REDESIGN_FILE_LEDGER_2026-08-23.json` | `REJECT_DIRECT_IMPORT` | semantics already adapted by T3 | use CVF-native inline category-only tests |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/mcp_gateway/CVF_MCP_NORMATIVE_INVARIANT_PROFILE.md` | add MCP-PR-011 normative mapping and bounded verification language |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | add pure typed category admission to existing evaluator |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mcp.protocol.invariant.profile.test.ts` | add positive/negative/malformed/composite regressions without raw secret values |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | preserve or minimally update the existing export only if required |
| `docs/reviews/CVF_MCP_KAR_T4_FORM_MODE_ELICITATION_SENSITIVE_DATA_GUARD_IMPLEMENTATION_WORKER_RETURN_2026-08-24.md` | create complete uncommitted worker evidence packet |

Every other path is forbidden for worker writes.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MCP_KAR_T4_FORM_MODE_ELICITATION_SENSITIVE_DATA_GUARD_IMPLEMENTATION_WORKER_RETURN_2026-08-24.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must include Purpose, Target / Source, Scope / Methodology,
Findings / Position, Risk / Corrective Action, Decision / Disposition, checker
read-ahead, source verification, test evidence, operation trace, Delta claim
boundary, dual-agent/adaptor boundary, corpus/rescan N/A-with-reason, epistemic
process, public disposition, status, changed files, command evidence,
retrospective, and no-commit statement.

## Agent Handoff Contract Control Block

Contract source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | committed parent dispatch, separate no-commit worker, parent reviewer/closer; no independent-review claim |
| phase | dispatch, local implementation, reviewer closure, continuity sync |
| baseHeadFor(phase) | dispatchBaseHead=`583c0911a8049e708bc1a75648ea6eeb907fb167`; executionBaseHead=worker captures committed dispatch HEAD; closureBaseHead=reviewer captures before material commit |
| changedSetScope(phase) | paired dispatch; four implementation paths plus one return; separate continuity-only paths |
| traceScope(phase, actor) | commands, sources, tests, status, diff, gates, and claim boundaries |
| commitOwner(phase) | worker forbidden; parent reviewer/closer after acceptance |
| crossBatchIsolation | schema repair, TPGR, T15, runtime/package/provider/public and all held lanes untouched |
| nextMoveSurfaces | worker return, reviewer decision, material commit, continuity-only sync |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MCP_KAR_T4_FORM_MODE_ELICITATION_SENSITIVE_DATA_GUARD_IMPLEMENTATION_COMPLETION_2026-08-24.md`

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MCP_KAR_T4_FORM_MODE_ELICITATION_SENSITIVE_DATA_GUARD_IMPLEMENTATION_COMPLETION_2026-08-24.md` (create only if closure conversion requires it) |
| reviewerOwnedClosurePaths | implementation paths, worker return, optional completion review, material commit, and separate continuity sync |
| closureOwner | parent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## MCP/CLI Adapter Boundary

| Field | Value |
| --- | --- |
| Adapter scope | none; pure category-only invariant composition |
| No-runtime-overclaim | No MCP runtime, CLI, bridge, package, transport, form collector, network path, or interoperability claim is authorized. |

## Foundation Storage Layout Block

N/A with reason: this tranche adds no storage layout, durable runtime state,
registry owner, package, service, or relocation.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | CVF-native implementation in exact existing owner |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | exact four-path invariant manifest |
| Disposition | bounded native adaptation; no new intake or direct import |
| Claim boundary | protocol fact does not grant runtime or external authority |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: exact T3 decision reuse; no new corpus or source
family is opened.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - targeted implementation makes no
  completeness, inventory, or all-files-read claim.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: no new enumeration, manifest, ledger, source
import, package, or runtime work.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/parent reviewer-closer |
| Provider or surface | local private provenance repository |
| Session or invocation | MCP-KAR-T4 dispatch, 2026-08-24 |
| Working directory | repository root |
| Command or tool surface | governed reads, scaffold helper, ADIF resolver, git status, apply_patch, and autorun gate |
| Target paths | paired T4 baseline and work order |
| Allowed scope source | operator autonomous absorption instruction; T3 accepted closure and exact manifest |
| Before status evidence | clean base `583c0911a8049e708bc1a75648ea6eeb907fb167`; proposed paths absent |
| After status evidence | paired dispatch artifacts only; implementation remains unchanged |
| Diff evidence | exact two-path status/diff and clean whitespace before parent commit |
| Approval boundary | one pure local T4 implementation dispatch |
| Claim boundary | no implementation, runtime, provider/live, public, or deploy action by dispatcher |
| Agent type | dispatch author subagent; later parent reviewer/closer |
| Invocation ID | `mcp-kar-t4-dispatch-2026-08-24` |
| Expected manifest | paired T4 baseline and work order |
| Actual changed set | paired T4 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | dispatch authority for a pure local form-mode category invariant |
| claimDisposition | CLAIM_REJECTED: dispatch does not prove implementation or execution |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: governance gates are not MCP/runtime receipts |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatcher performed reads, authoring, and local gates only |
| invocationBoundary | repository-local provider-free tools |
| interceptionBoundary | no wrapper, proxy, MCP client/server, CLI, transport, collector, or bridge |
| claimLanguage | bounded implementation authority only |
| forbiddenExpansion | runtime/package/transport/fixture/session/provider/live/public/deploy/production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation work order; public sync forbidden.

## Claim Boundary

This work order authorizes only the exact pure local implementation manifest
and one no-commit worker return. It does not authorize raw secret values,
runtime interception, package or transport work, external fixture import,
session changes, provider/live calls, public sync, deployment, production, or
MCP interoperability claims.

## Operator Checkpoint

Operator authorization is satisfied by the 2026-08-24 autonomous valuable
absorption instruction. Any external effect or out-of-manifest expansion
requires a new explicit checkpoint.
