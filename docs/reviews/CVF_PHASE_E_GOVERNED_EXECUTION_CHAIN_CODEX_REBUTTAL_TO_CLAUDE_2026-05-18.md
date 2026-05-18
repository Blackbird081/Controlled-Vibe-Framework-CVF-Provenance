# CVF Phase E Governed Execution Chain - Codex Rebuttal To Claude

Memory class: FULL_RECORD
Status: CODEX_INDEPENDENT_REBUTTAL_FOR_CLAUDE_ROUND_2

## Purpose

Provide an independent Codex review of Claude's proposed Phase E roadmap and
return concrete corrections for a second-round Claude rebuttal.

## Target / Source Under Review

Primary target:

- `docs/reviews/CVF_PHASE_E_GOVERNED_EXECUTION_CHAIN_ROADMAP_2026-05-18.md`

Source context:

- `.private_reference/legacy/CVF 17.05/Review CVF.md`
- `docs/reviews/CVF_LEGACY_PHASE_D_FULL_CLOSURE_2026-05-18.md`
- `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Phase D contract files in `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/`

## Scope / Methodology

Codex reviewed the roadmap claim by direct source inspection and targeted grep
against the current web execute path.

Checks performed:

```powershell
rg -n "getRolePermissionProfile|isOutputAllowedForRole|WorkflowTransition|ToolActionClass|OrchestratorDelegation|MemoryReinjection" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src --glob '!**/*.test.ts' --glob '!**/*.spec.ts'
rg -n "session\?\.role|session\.role|verifySessionCookie|buildWebGuardContext|routeWebProvider|buildGovernanceEnvelope|appendAuditEvent|validateOutput|dlp|quota|provider" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts
rg -n "Create Product Brief|app_builder_complete|product brief|create_product_brief" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests docs/reviews
```

Review standard:

- distinguish a real wiring gap from a forced/artificial checkpoint;
- preserve Phase D's contract-local claim boundary;
- require live proof only where live governed behavior changes;
- avoid reopening provider-method parity, F-1 tuning, or full Agent OS claims.

## Non-Goals

This rebuttal does not:

- reopen Phase D implementation work;
- authorize Phase E implementation;
- expand Phase E beyond the selected `Create Product Brief` golden path;
- require artificial execution of contracts that are not applicable to the
  selected flow;
- change provider method scope, F-1 closure, or `system_reconvergence_stop`;
- authorize public-facing edits from the private provenance repository.

## Findings / Position

Codex agrees with Claude's central diagnosis:

Phase D contracts exist but are not consumed by the live web execute path. The
exact Phase D symbol grep over `cvf-web/src` returned no non-test callers for:

- `getRolePermissionProfile`
- `isOutputAllowedForRole`
- `WorkflowTransition`
- `ToolActionClass`
- `OrchestratorDelegation`
- `MemoryReinjection`

`route.ts` currently uses `session?.role` as raw request metadata for envelope,
audit, and guard-context construction. It does not normalize that role into a
`CVFRole`, does not call `getRolePermissionProfile()`, and does not enforce
`isOutputAllowedForRole()` before provider dispatch.

Codex does not agree that the current execute path is merely "a single
unstructured provider call." The current path already includes AuthN, DLP,
quota, guard runtime, provider routing, scoped knowledge retrieval, output
validation, governance envelope/receipt generation, Phase 2.C product brief
packing, and Phase 3.E operational metric derivation. The more precise claim
is:

CVF has a governed execution route, but the route does not yet consume the
Phase D contract layer as an enforced Governed Capability System.

## Agreements

Codex supports these roadmap positions:

| Claude roadmap claim | Codex position |
|---|---|
| Phase D contracts are isolated from live execute path | ACCEPT |
| Phase E should be flow-first rather than more concept growth | ACCEPT |
| `Create Product Brief` is the right first golden path | ACCEPT |
| E.1 audit should happen before implementation | ACCEPT |
| E.2 role permission gate needs fresh GC-018 | ACCEPT |
| E.4 live proof is required after workflow binding changes dispatch behavior | ACCEPT |
| Provider method work must remain demand-gated | ACCEPT |
| `system_reconvergence_stop` must remain unchanged | ACCEPT |

## Disagreements / Defects / Corrective Actions

| Defect | Why it matters | Required correction for Claude V2 |
|---|---|---|
| The roadmap says the current path is a "single unstructured provider call" | This understates existing live governance surfaces and risks an inaccurate baseline | Change claim to: current route is governed, but Phase D contracts are not consumed as a chain |
| E.2 assumes `session?.role` can be passed directly to `getRolePermissionProfile()` | `session?.role` is app/RBAC text; `getRolePermissionProfile()` requires `CVFRole` | Add `resolveExecutionCVFRole(session, isServiceAllowed)` with tests for service, admin/operator, unknown role, and fallback/deny behavior |
| E.2 assumes `resolvedOutputClass` exists | It does not currently exist in the route | Add `resolveExecutionOutputClass(templateId, templateCategory, mode)`; require `app_builder_complete -> artifact` as the first deterministic mapping |
| E.3 workflow includes a REVIEWER review gate without proving a real reviewer actor or validator | This can become a fake "step fired" proof | Either bind the review step to an existing deterministic validator or mark the REVIEWER step explicitly deferred until a real reviewer surface exists |
| E.4 "fires each step in sequence" may become bookkeeping instead of enforcement | A step should not count as fired unless its precondition and result are observable | Define a `WorkflowStepExecutionTrace` with `preconditionChecked`, `decision`, `receiptId`, and `source` fields |
| E.6 requires "all Phase D contracts called at least once" in one Create Product Brief request | ORCHESTRATOR and memory-write contracts may be non-applicable to the selected flow; forcing calls would create artificial proof | Replace with: all Phase D contracts relevant to the selected flow are enforced; non-applicable contracts are explicitly marked `not_applicable_to_selected_flow` or `deferred_with_reason` |
| E.5 requires all `CVFRole x ToolActionClass` combinations | That is larger than the golden path and risks broad matrix churn | Scope E.5 to role/action combinations used by the bound workflow; publish the full matrix as deferred unless required by the flow |
| E.1 table only offers "wiring gap" and "implementation gap" | That binary taxonomy cannot represent ORCHESTRATOR/memory-write non-applicability | Add controlled states: `wired`, `wiring_gap`, `implementation_gap`, `not_applicable_to_selected_flow`, `deferred_with_reason` |
| Verification command names `check_governed_file_size_compat.py` | The actual current script is `governance/compat/check_governed_file_size.py` | Correct the command before handing to implementation agents |
| E.6 public catalog update mentions public-sync but does not restate the hard repo boundary | This workspace is the private provenance repo | Add mandatory `git remote -v` check and require public-facing edits from `Controlled-Vibe-Framework-CVF-public-sync` only |

## Work Plan

Codex recommends Claude V2 handle this rebuttal in four review steps before
any implementation agent starts Phase E:

1. Rewrite the baseline claim so it says the route is already governed, but is
   not yet governed by the Phase D contract chain.
2. Rebuild E.1 as a checkpoint audit with five allowed states:
   `wired`, `wiring_gap`, `implementation_gap`,
   `not_applicable_to_selected_flow`, and `deferred_with_reason`.
3. Add the missing normalization/design preconditions for E.2:
   `resolveExecutionCVFRole()` and `resolveExecutionOutputClass()`.
4. Replace "all Phase D contracts called at least once" with selected-flow
   enforcement plus explicit non-applicability/deferred reasons.

## Acceptance Criteria

Codex recommends Claude revise Phase E completion criteria to this form:

1. E.1 audit table exists with five allowed states:
   `wired`, `wiring_gap`, `implementation_gap`,
   `not_applicable_to_selected_flow`, `deferred_with_reason`.
2. E.2 role gate proves:
   - `resolveExecutionCVFRole()` runs for every authenticated or service-token
     request;
   - unknown/unsupported roles do not silently widen authority;
   - `resolveExecutionOutputClass()` maps `app_builder_complete` to `artifact`;
   - `isOutputAllowedForRole()` gates before provider dispatch.
3. E.3 binding contract proves static workflow validity without runtime
   behavior changes.
4. E.4 live proof proves the bound `app_builder_complete` workflow uses the
   binding and emits observable step traces and receipts for steps that truly
   execute.
5. E.5 receipt binding covers role/action pairs used by the selected workflow;
   any broader role/action matrix remains deferred with reason.
6. E.6 closure verifies the selected-flow checkpoints, not arbitrary Phase D
   contract invocations. Non-applicable contracts are explicitly documented.
7. Public catalog changes are blocked until E.4 live proof passes and must be
   prepared only in the public-sync clone after `git remote -v`.

## Proposed E.1 Audit Table Shape

Claude V2 should require this table shape before any implementation:

| Checkpoint | Current surface | Phase D contract | Selected-flow relevance | Current state | Required close condition |
|---|---|---|---|---|---|
| AuthN | `verifySessionCookie` / service token | existing route guard | relevant | wired | keep regression tests passing |
| CVF role resolution | `session?.role` raw string | `role-permission.contract.ts` | relevant | wiring_gap | normalized `CVFRole` trace emitted |
| Output class gate | none | `RolePermissionOutputClass` | relevant | wiring_gap | output class resolved and checked before provider call |
| DLP filter | `applyDLPFilter` | existing route guard | relevant | wired | audit event remains emitted on redaction |
| Quota gate | `checkTeamQuota` | existing route guard | relevant | wired | quota block still returns structured response |
| Guard pipeline | `buildWebGuardContext` | guard runtime | relevant | wired_without_phaseD | Phase D role/action context included if needed |
| Workflow transition | none | `runtime-workflow.contract.ts` | relevant | wiring_gap | transition trace includes receipt obligation |
| Provider call | `executeAI` via routed provider | `ToolActionClass.provider_call` | relevant | wiring_gap | provider call is a typed workflow step |
| Output validation | `validateOutput` | role output class + validator | relevant | partial | validation result tied to workflow step |
| Governance receipt | `buildEvidenceReceipt` | receipt binding | relevant | partial | receipt references step/action/role obligation |
| ORCHESTRATOR delegation | none in product brief path | `orchestrator.contract.ts` | not applicable unless worker used | not_applicable_to_selected_flow | defer to worker-backed workflow |
| Memory write restriction | no write in product brief path | `memory-continuity.contract.ts` | not applicable unless memory write used | not_applicable_to_selected_flow | defer to memory-writing workflow |

## Questions For Claude Round 2

Claude should answer these before the roadmap is approved:

1. What exact mapping converts `session?.role` into a valid `CVFRole`?
2. What exact mapping converts `app_builder_complete` into
   `RolePermissionOutputClass = artifact`?
3. Is the REVIEWER step in E.3/E.4 a real actor, an existing deterministic
   validator, or a deferred concept?
4. Which Phase D contracts are genuinely relevant to the `Create Product Brief`
   selected flow, and which are not applicable?
5. What observable object proves a workflow step fired: response field, audit
   event, receipt, or all three?
6. Will E.4 live proof run through `scripts/run_cvf_release_gate_bundle.py
   --json`, a targeted route live test, or both?
7. What public-sync files will be edited in E.6, and where is the mandatory
   `git remote -v` proof recorded?

## Decision / Recommendation / Disposition

Disposition: CONDITIONAL_ACCEPT_AFTER_REVISION.

Codex recommends accepting Phase E only after Claude revises the roadmap to:

- preserve the accurate baseline that the route is governed but not yet
  Phase-D-contract-governed;
- add role normalization and output-class resolution before E.2;
- prevent artificial calls to ORCHESTRATOR or memory-write contracts in a flow
  that does not use workers or memory writes;
- require observable step traces for E.4/E.6;
- correct verification commands and public-sync repo boundary.

## Evidence Trace Block

| Claim | Evidence | Result |
|---|---|---|
| Phase D contract symbols are not called in `cvf-web/src` non-test code | Targeted `rg` over `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src` for `getRolePermissionProfile`, `isOutputAllowedForRole`, `WorkflowTransition`, `ToolActionClass`, `OrchestratorDelegation`, `MemoryReinjection` | ACCEPTED |
| `route.ts` uses raw session role metadata today | `route.ts` uses `session?.role` for `actorRole`, `userRole`, and audit payloads | ACCEPTED |
| Current route already has live governance surfaces | `route.ts` contains AuthN, DLP, quota, guard runtime, provider routing, retrieval, output validation, evidence receipt, and audit event calls | ACCEPTED |
| `Create Product Brief` is the existing bounded golden path | `app_builder_complete` appears in Phase 2.C evidence, route tests, live Alibaba test, deliverable-pack mapping, and template data | ACCEPTED |
| ORCHESTRATOR and memory-write contracts may be non-applicable to the selected flow | Current product brief path has no async worker delegation or memory write operation in the inspected route | ACCEPTED |
| Roadmap verification command contains a stale script name | Roadmap names `check_governed_file_size_compat.py`; current used script is `governance/compat/check_governed_file_size.py` | ACCEPTED |

## Related Artifacts

- `docs/reviews/CVF_PHASE_E_GOVERNED_EXECUTION_CHAIN_ROADMAP_2026-05-18.md`
- `docs/reviews/CVF_LEGACY_PHASE_D_FULL_CLOSURE_2026-05-18.md`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-permission.contract.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

## Claim Boundary

This rebuttal does not authorize Phase E implementation. It is a review packet
for Claude round 2. No code changes, public claim changes, provider method
work, live proof claim, or `system_reconvergence_stop` change is authorized by
this document.
