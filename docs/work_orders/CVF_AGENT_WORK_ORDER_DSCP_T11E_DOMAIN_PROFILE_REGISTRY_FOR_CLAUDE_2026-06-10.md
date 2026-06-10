# CVF Agent Work Order: DSCP-T11E Domain Profile Registry

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-10

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `6a1cce6b`

executionBaseHead: `6a1cce6b`

closureBaseHead: `6a1cce6b`

---

## Purpose

Implement a bounded deterministic CPF domain-profile registry and selector so
scan-layer callers can select a profile before applying it to DSCP descriptors.

## Authority Chain

Operator instruction 2026-06-10 -> GC-018:
`docs/baselines/CVF_GC018_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_2026-06-10.md`
-> roadmap:
`docs/roadmaps/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_ROADMAP_2026-06-10.md`
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
| Operator | Human | Authorized T11E review/commit and next-roadmap preparation on 2026-06-10 |

## Scope / Target / Owner Boundary

Allowed worker scope:

- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts`.
- Update `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts`
  only to export the new registry contract.
- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.registry.test.ts`.
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only for the
  new source and test path coverage.
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` only for the
  DSCP-T11E quick lookup rows.
- Create
  `docs/reviews/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_WORKER_RETURN_2026-06-10.md`.

Reviewer-owned closure scope:

- `docs/baselines/CVF_GC018_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_2026-06-10.md`
- `docs/roadmaps/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_ROADMAP_2026-06-10.md`
- this work order status conversion;
- `docs/reviews/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_COMPLETION_2026-06-10.md`
- session continuity files after material commit.

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
| Acceptance: registry operations | Implementation Contract | source and tests | focused vitest | PASS |
| Acceptance: exact, ambiguous, and no-match selection | Implementation Contract | `select(criteria)` tests | focused vitest | PASS |
| Acceptance: facet-key selection | Implementation Contract | `requiredFacetKey` tests | focused vitest | PASS |
| Acceptance: select-then-apply isolation | Implementation Contract | pipeline integration tests | focused vitest | PASS |
| Registry coverage | Required Artifact Manifest | GC-051 JSON and Markdown | registry checker | PASS |

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
| New registry source absent before implementation | `Test-Path -LiteralPath EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | False |
| New registry test absent before implementation | `Test-Path -LiteralPath EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.registry.test.ts` | False |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 6a1cce6b --head HEAD` | PASS before edits or reviewer-recorded if dispatched by operator return |

## Required First Reads

| File | Purpose |
|---|---|
| `docs/baselines/CVF_GC018_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_2026-06-10.md` | Confirm authorization and boundary |
| `docs/roadmaps/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_ROADMAP_2026-06-10.md` | Confirm roadmap requirements |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | Verify existing profile contract |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | Verify export surface |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: domain profile ID type | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 8 | `DomainProfileId` | `DomainProfileId` | ACCEPT |
| EXISTS: domain family type | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 12 | `DscpDomainFamily` | `DscpDomainFamily` | ACCEPT |
| EXISTS: domain profile contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 23 | `DscpDomainProfile` | `DscpDomainProfile` | ACCEPT |
| RUNTIME_BEHAVIOR: profile application helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 92 | `applyDomainProfileToDescriptorInput` | `applyDomainProfileToDescriptorInput` | ACCEPT |
| EXISTS: existing profile helper barrel export | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | line 77 | `applyDomainProfileToDescriptorInput` | `control.plane.context.barrel.ts` | ACCEPT |

## New Runtime Symbols

The following are implementation outputs authorized by this work order and are
verified by focused tests and completion evidence, not pre-existing source
facts:

- `DscpDomainProfileRegistry`
- `createDscpDomainProfileRegistry`
- `DomainProfileSelectionCriteria`
- `DomainProfileSelectionResult`
- `DomainProfileRegistrationResult`

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | Yes | Local registry source |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | Yes | Export surface |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.registry.test.ts` | Yes | Focused deterministic tests |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Yes | GC-051 machine registry coverage |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | Yes | GC-051 human registry coverage |
| `docs/reviews/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_WORKER_RETURN_2026-06-10.md` | Yes | Worker evidence packet |

## Work-Order Fulfillment Manifest

Closure is invalid if any required artifact is missing or if any forbidden path
is modified.

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\**` | External product edits are out of DSCP-T11E scope |
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

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.registry.test.ts`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`
- `docs/reviews/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_WORKER_RETURN_2026-06-10.md`

Write mode:

modify-listed only.

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Read all Required First Reads.
3. Implement the local registry and selector.
4. Export the registry through the CPF barrel.
5. Add focused tests.
6. Register the new source and test paths in GC-051 JSON and Markdown.
7. Run CPF `npm run check`.
8. Run focused DSCP-T11E vitest.
9. Run reviewer-fast gate.
10. Author the worker return packet.
11. Stage allowed worker artifacts and return without committing.

## Implementation Contract

Required behavior:

1. `register` accepts new profiles and rejects duplicate IDs unless
   `replaceExisting=true`.
2. `unregister`, `getById`, and `listAll` are deterministic local operations.
3. `select(criteria)` uses AND semantics for supplied criteria.
4. `select(criteria)` returns `matched=true` and a profile only when exactly one
   profile matches.
5. Ambiguous or no-match selection returns `matched=false`, `profile=null`, and
   diagnostics.
6. `requiredFacetKey` checks both `commonFacetFields` and `domainFacetFields`.
7. Select-then-apply tests prove legal-policy and technical-project profile
   isolation before descriptor build.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| `npm run test -- tests/dscp.domain.profile.registry.test.ts` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| `git diff --name-status` | only allowed worker paths plus reviewer-owned closure shell |
| Worker return packet | includes command output summaries, changed-file list, and claim boundary |

Base-anchor evidence:

- `dispatchBaseHead`: `6a1cce6b`
- `executionBaseHead`: worker captured `6a1cce6b`
- `closureBaseHead`: reviewer-owned post-return value
- Commit mode: `WORKER_MUST_NOT_COMMIT`

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| Registry operations are deterministic and locally tested | PASS |
| Selection semantics cover exact match, ambiguity, no-match, and facet keys | PASS |
| Select-then-apply integration preserves profile isolation | PASS |
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
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_COMPLETION_2026-06-10.md` | reviewer-authored post-return | PASS |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_ROADMAP_2026-06-10.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry source | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | source file present | PASS |
| Focused tests | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.registry.test.ts` | 18/18 PASS | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | DSCP-T11E source/test entries | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | DSCP-T11E quick lookup rows | PASS |
| External evidence digest | N/A | N/A with reason: no external product, corpus, provider, or public-sync artifact consumed or produced | N/A with reason |
| System loop interlock | no system-loop mutation | local CPF registry only | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V17_2026-06-07.md` | reviewer-owned final sync | PASS |

## Review Gate

Reviewer must confirm:

1. `git diff --name-status` contains only allowed worker paths plus reviewer
   closure shell.
2. CPF `npm run check` PASS.
3. Focused DSCP-T11E vitest PASS.
4. Reviewer-fast PASS.
5. GC-051 JSON and Markdown registry surfaces cover the new source/test paths.
6. Worker return contains all required evidence.

## Closure Checklist

- [x] Worker return reviewed and accepted
- [x] CPF `npm run check` PASS confirmed
- [x] Focused DSCP-T11E vitest PASS confirmed
- [x] GC-051 registry PASS confirmed
- [x] Reviewer-fast PASS confirmed
- [x] Completion review authored by reviewer
- [x] Reviewer commits material artifacts
- [x] Session continuity synced by reviewer

## Operator Checkpoint

operator.checkpoint.waiver: operator authorized DSCP-T11E review/commit on
2026-06-10. Operator approval remains required for external `Policy_Local`
edits, provider/key use, corpus ingestion, T12 authoring, public-sync, or any
readiness claim.

## Claim Boundary

This work order authorizes only a local deterministic CPF registry and selector.
It does not claim provider behavior, live governance proof, retrieval quality,
semantic correctness, corpus ingestion, OCR, vector search, PolicyLocal T12
readiness, legal advice quality, current-law status, public readiness, hosted
readiness, production readiness, public-sync, memory reinjection, high-risk
promotion, Learning Orchestrator runtime behavior, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; not public-synced.
