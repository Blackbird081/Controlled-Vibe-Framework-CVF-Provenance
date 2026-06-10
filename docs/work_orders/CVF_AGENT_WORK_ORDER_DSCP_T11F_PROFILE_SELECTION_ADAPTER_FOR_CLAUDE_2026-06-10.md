# CVF Agent Work Order: DSCP-T11F Profile Selection Adapter

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-10

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `8a7cd134`

executionBaseHead: worker must capture

closureBaseHead: reviewer-owned after return

---

## Purpose

Implement a bounded deterministic CPF adapter that selects a registered domain
profile and applies it to a descriptor input only when selection is unique and
profile application is not blocked.

## Authority Chain

Operator instruction 2026-06-10 -> post-T11E audit:
`docs/audits/CVF_DSCP_POST_T11E_NEXT_ROADMAP_AUDIT_2026-06-10.md`
-> GC-018:
`docs/baselines/CVF_GC018_DSCP_T11F_PROFILE_SELECTION_ADAPTER_2026-06-10.md`
-> roadmap:
`docs/roadmaps/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_ROADMAP_2026-06-10.md`
-> this work order.

Active session state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Agent Roles

| Role | Agent | Responsibility |
|---|---|---|
| Worker | Claude | Implement source/test/registry/worker return; do not commit |
| Reviewer | Codex | Review, run gates, close and commit if PASS |
| Operator | Human | Authorized DSCP-T11E closure and next work order on 2026-06-10 |

## Scope / Target / Owner Boundary

Allowed worker scope:

- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts`.
- Update `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts`
  only to export the new adapter contract.
- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.selection.adapter.test.ts`.
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only for the
  new source and test path coverage.
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` only for the
  DSCP-T11F quick lookup rows.
- Create
  `docs/reviews/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_WORKER_RETURN_2026-06-10.md`.

Reviewer-owned closure scope:

- this work order status conversion;
- `docs/reviews/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_COMPLETION_2026-06-10.md`;
- session continuity files after material commit.

## Reviewer Closure Conversion

completionReviewPath:

`docs/reviews/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_COMPLETION_2026-06-10.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_COMPLETION_2026-06-10.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T11F_PROFILE_SELECTION_ADAPTER_FOR_CLAUDE_2026-06-10.md`
- `docs/roadmaps/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_ROADMAP_2026-06-10.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V17_2026-06-07.md`

Reviewer conversion rule: Claude must not create or edit the completion review
unless a later operator instruction changes the owner. Codex owns closure
conversion, final gate reruns, commit, and continuity sync.

Forbidden scope:

- Do not modify external `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local`.
- Do not edit cvf-web, provider routing, ECO runtime, LPF runtime, corpus data,
  T12 artifacts, public-sync, or readiness artifacts.
- Do not run provider calls, load API keys, ingest corpus files, perform OCR,
  create vector retrieval, or claim hosted/production/public readiness.

Risk ceiling:

R1 local deterministic CPF source and tests only.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap section | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Acceptance: unique selection applies profile | Implementation Contract | adapter source and tests | focused vitest | ASSIGNED |
| Acceptance: no-match stop | Implementation Contract | stop result tests | focused vitest | ASSIGNED |
| Acceptance: ambiguous stop | Implementation Contract | stop result tests | focused vitest | ASSIGNED |
| Acceptance: blocked profile application stop | Implementation Contract | blocked gate tests | focused vitest | ASSIGNED |
| Acceptance: facet-key selection | Implementation Contract | `requiredFacetKey` tests | focused vitest | ASSIGNED |
| Registry coverage | Required Artifact Manifest | GC-051 JSON and Markdown | registry checker | ASSIGNED |

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within allowed
scope must be repaired and rerun by the worker without escalating to the
operator. If repair requires forbidden paths, provider/key use, corpus
ingestion, T12 authoring, public-sync, or readiness claims, stop and return a
blocked diagnostic.

## Pre-Flight Checks

| Check | Command | Required result |
|---|---|---|
| Base HEAD captured | `git rev-parse --short HEAD` | record as `executionBaseHead` |
| New adapter source absent before implementation | `Test-Path -LiteralPath EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts` | False |
| New adapter test absent before implementation | `Test-Path -LiteralPath EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.selection.adapter.test.ts` | False |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 8a7cd134 --head HEAD` | PASS before edits or reviewer-recorded if dispatched by operator return |

## Required First Reads

| File | Purpose |
|---|---|
| `docs/audits/CVF_DSCP_POST_T11E_NEXT_ROADMAP_AUDIT_2026-06-10.md` | Confirm selected lane |
| `docs/baselines/CVF_GC018_DSCP_T11F_PROFILE_SELECTION_ADAPTER_2026-06-10.md` | Confirm authorization and boundary |
| `docs/roadmaps/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_ROADMAP_2026-06-10.md` | Confirm roadmap requirements |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | Verify existing registry and selection output |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | Verify existing profile application helper |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | Verify export surface |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: selection criteria contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | line 10 | `DomainProfileSelectionCriteria` | `DomainProfileSelectionCriteria` | ACCEPT |
| EXISTS: selection result contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | line 22 | `DomainProfileSelectionResult` | `DomainProfileSelectionResult` | ACCEPT |
| EXISTS: profile registry class | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | line 46 | `DscpDomainProfileRegistry` | `DscpDomainProfileRegistry` | ACCEPT |
| RUNTIME_BEHAVIOR: registry selection | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | line 90 | `select` | `DscpDomainProfileRegistry.select` | ACCEPT |
| EXISTS: registry factory | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | line 169 | `createDscpDomainProfileRegistry` | `createDscpDomainProfileRegistry` | ACCEPT |
| EXISTS: domain profile contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 23 | `DscpDomainProfile` | `DscpDomainProfile` | ACCEPT |
| RUNTIME_BEHAVIOR: profile application helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 92 | `applyDomainProfileToDescriptorInput` | `applyDomainProfileToDescriptorInput` | ACCEPT |
| EXISTS: registry barrel export | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | line 86 | `DscpDomainProfileRegistry` | `control.plane.context.barrel.ts` | ACCEPT |

## New Runtime Symbols

The following are implementation outputs authorized by this work order and must
be verified by focused tests and completion evidence, not pre-existing source
facts:

- `DscpProfileSelectionAdapterInput`
- `DscpProfileSelectionAdapterResult`
- `DscpProfileSelectionStopReason`
- `selectAndApplyDscpDomainProfile`

Worker may choose equivalent names only if the worker return records the exact
symbols and the intent remains unchanged.

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts` | Yes | Local adapter source |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | Yes | Export surface |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.selection.adapter.test.ts` | Yes | Focused deterministic tests |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Yes | GC-051 machine registry coverage |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | Yes | GC-051 human registry coverage |
| `docs/reviews/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_WORKER_RETURN_2026-06-10.md` | Yes | Worker evidence packet |

## Work-Order Fulfillment Manifest

Closure is invalid if any required artifact is missing or if any forbidden path
is modified.

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\**` | External product edits are out of DSCP-T11F scope |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/**` | No web/runtime/provider route edit authorized |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/**` | Existing ECO source is out of scope |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/**` | Existing LPF source is out of scope |
| `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | Do not reopen T11D/T12 readiness in this tranche |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\**` | EXTERNAL_WORKSPACE_NOT_MODIFIED | EXTERNAL_WORKSPACE_NOT_MODIFIED | Stop if modification is required; external product edits are forbidden |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Existing web files are out of scope; worker must not edit, stage, or claim them |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Existing ECO source is out of scope; worker must not edit it |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Existing LPF source is out of scope; worker must not edit it |
| `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Existing T11/T12 readiness roadmap is out of scope; worker must not edit it |

## Write Ownership

Owned files or modules:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.selection.adapter.test.ts`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`
- `docs/reviews/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_WORKER_RETURN_2026-06-10.md`

Write mode:

modify-listed only.

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Read all Required First Reads.
3. Implement the local selection adapter.
4. Export the adapter through the CPF barrel.
5. Add focused tests.
6. Register the new source and test paths in GC-051 JSON and Markdown.
7. Run CPF `npm run check`.
8. Run focused DSCP-T11F vitest.
9. Run reviewer-fast gate.
10. Author the worker return packet.
11. Stage allowed worker artifacts and return without committing.

## Implementation Contract

Required behavior:

1. Adapter input must include a `DscpDomainProfileRegistry`, a
   `DomainProfileSelectionCriteria`, and the descriptor input accepted by
   `applyDomainProfileToDescriptorInput`.
2. Adapter result must include status, selected profile ID or null, match count,
   matched IDs, diagnostics, and the applied descriptor input only on success.
3. If registry selection returns zero matches, the result must stop before
   profile application.
4. If registry selection returns multiple matches, the result must stop before
   profile application.
5. If profile application returns a blocked `BLOCKED_UNTIL_*` style result, the
   adapter must return a blocked stop result and must not build any package or
   receipt.
6. Success is allowed only when exactly one profile matches and profile
   application succeeds.
7. Tests must prove legal-policy and technical-project profile isolation and
   no gate bleed.

Recommended status tokens:

- `PROFILE_APPLIED`
- `PROFILE_SELECTION_NO_MATCH`
- `PROFILE_SELECTION_AMBIGUOUS`
- `PROFILE_APPLICATION_BLOCKED`

Equivalent ASCII tokens are allowed if documented in the worker return.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| `npm run test -- tests/dscp.profile.selection.adapter.test.ts` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| `git diff --name-status` | only allowed worker paths plus reviewer-owned closure shell |
| Worker return packet | includes command output summaries, changed-file list, and claim boundary |

Base-anchor evidence:

- `dispatchBaseHead`: `8a7cd134`
- `executionBaseHead`: worker must capture before edits
- `closureBaseHead`: reviewer-owned post-return value
- Commit mode: `WORKER_MUST_NOT_COMMIT`

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| Unique profile selection applies metadata/gates through existing helper | PASS |
| No-match and ambiguous selection stop before profile application | PASS |
| Blocked profile application stop is explicit and tested | PASS |
| `requiredFacetKey` path is covered | PASS |
| Legal-policy and technical-project profiles do not bleed gates or metadata | PASS |
| GC-051 JSON and Markdown cover new source/test paths | PASS |
| No forbidden path is modified | PASS |

## Fail Conditions

| Condition | Action |
|---|---|
| Any external `Policy_Local` file needs modification | STOP and return blocked diagnostic |
| Any provider call or API key use appears necessary | STOP and return to reviewer |
| Any corpus ingestion, OCR, vector search, T12, current-law, legal-quality, public-readiness, or production-readiness claim is introduced | STOP and remove claim |
| Existing external runtime surfaces must be changed | STOP and return to reviewer unless a separate roadmap authorizes source changes |
| GC-051 cannot cover the new path cleanly | STOP and return exact registry error |

## Return Packet Requirements

Claude must return uncommitted artifacts with:

- `executionBaseHead`;
- `git status --short`;
- `git diff --name-status`;
- package check command and result;
- focused test command and result;
- reviewer-fast result;
- GC-051 JSON and Markdown update summary;
- exact exported symbols and status tokens;
- exact claim boundary.

## Return-To-Orchestrator Conditions

Worker returns when:

- all allowed worker artifacts are staged and uncommitted;
- required commands have PASS evidence or a bounded blocker diagnostic;
- no forbidden path is modified;
- worker return packet is complete.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: DISPATCHED` before worker execution | READY |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_COMPLETION_2026-06-10.md` | reviewer-authored on worker-return review | NOT_STARTED_BY_DESIGN |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_ROADMAP_2026-06-10.md` | `Status: DISPATCHED` before worker execution | READY |
| Adapter source | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts` | source file required from worker | WORKER_ASSIGNED |
| Focused tests | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.selection.adapter.test.ts` | focused test evidence required from worker | WORKER_ASSIGNED |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | DSCP-T11F source/test entries required | WORKER_ASSIGNED |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | DSCP-T11F quick lookup rows required | WORKER_ASSIGNED |
| External evidence digest | N/A | N/A with reason: no external product, corpus, provider, or public-sync artifact consumed or produced | N/A with reason |
| System loop interlock | no system-loop mutation | local CPF adapter only | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V17_2026-06-07.md` | reviewer-owned sync in DSCP-T11F closure batch | NOT_STARTED_BY_DESIGN |

## Review Gate

Reviewer must confirm:

1. `git diff --name-status` contains only allowed worker paths plus reviewer
   closure shell.
2. CPF `npm run check` PASS.
3. Focused DSCP-T11F vitest PASS.
4. Reviewer-fast PASS.
5. GC-051 JSON and Markdown registry surfaces cover the new source/test paths.
6. Worker return contains all required evidence.

## Closure Checklist

- [ ] Worker return reviewed and accepted
- [ ] CPF `npm run check` PASS confirmed
- [ ] Focused DSCP-T11F vitest PASS confirmed
- [ ] GC-051 registry PASS confirmed
- [ ] Reviewer-fast PASS confirmed
- [ ] Completion review authored by reviewer
- [ ] Reviewer commits material artifacts
- [ ] Session continuity synced by reviewer

## Operator Checkpoint

operator.checkpoint.waiver: operator authorized DSCP-T11F dispatch on
2026-06-10. Operator approval remains required for external `Policy_Local`
edits, provider/key use, corpus ingestion, T12 authoring, public-sync, or any
readiness claim.

## Claim Boundary

This work order authorizes only a local deterministic CPF profile selection
adapter and focused tests. It does not claim provider behavior, live governance
proof, retrieval quality, semantic correctness, corpus ingestion, OCR, vector
search, PolicyLocal T12 readiness, legal advice quality, current-law status,
public readiness, hosted readiness, production readiness, public-sync, memory
reinjection, high-risk promotion, Learning Orchestrator runtime behavior, or
autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; not public-synced.
