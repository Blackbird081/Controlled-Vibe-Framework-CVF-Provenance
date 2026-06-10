# CVF Agent Work Order: DSCP-T11 Profile-Aware Pipeline Harness

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-10

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `0f75ff6f`

executionBaseHead: `<worker captured: 0f75ff6f>`

closureBaseHead: `<reviewer-owned after material commit>`

---

## Purpose

Implement a bounded deterministic CPF harness proving that DSCP-T10
domain-profile metadata and gate keys flow through existing DSCP pipeline
surfaces without raw content release or cross-profile bleed.

## Authority Chain

Operator instruction 2026-06-10 -> GC-018:
`docs/baselines/CVF_GC018_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_2026-06-10.md`
-> roadmap:
`docs/roadmaps/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_ROADMAP_2026-06-10.md`
-> this work order.

Active session state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Agent Roles

| Role | Agent | Responsibility |
|---|---|---|
| Worker | Claude | Implement test/registry/worker return; do not commit |
| Reviewer | Codex | Review, run gates, close and commit if PASS |
| Operator | Human | Authorized DSCP-T11 proof direction on 2026-06-10 |

## Scope / Target / Owner Boundary

Allowed scope:

- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.aware.pipeline.harness.test.ts`.
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only for the
  new test path coverage.
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` only for the
  DSCP-T11 quick lookup row.
- Create
  `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_WORKER_RETURN_2026-06-10.md`.

Reviewer-owned closure scope:

- `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_COMPLETION_2026-06-10.md`
- `docs/roadmaps/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_ROADMAP_2026-06-10.md`
- this work order status conversion;
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V17_2026-06-07.md`

Forbidden scope:

- Do not modify the external `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local`
  workspace.
- Do not edit cvf-web, provider routing, existing ECO/LPF source contracts, or
  T10 source contracts.
- Do not run provider calls, load API keys, ingest corpus files, perform OCR,
  create vector retrieval, author PolicyLocal T12, public-sync, push, or claim
  hosted/production/public readiness.

Risk ceiling:

R1 local deterministic test harness only.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap section | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Acceptance: legal-policy metadata/gates flow through ECO path | Implementation Contract | legal-policy test | focused vitest | DISPATCHED |
| Acceptance: technical-project metadata/gates flow through LPF path | Implementation Contract | technical-project test | focused vitest | DISPATCHED |
| Acceptance: raw release remains false | Implementation Contract | package and receipt assertions | focused vitest | DISPATCHED |
| Acceptance: no cross-profile bleed | Implementation Contract | isolation test | focused vitest | DISPATCHED |
| Acceptance: blocked boundary short-circuits | Implementation Contract | blocked profile test | focused vitest | DISPATCHED |
| Registry coverage | Required Artifact Manifest | GC-051 JSON and Markdown | registry checker | DISPATCHED |

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within allowed
scope must be repaired and rerun by the worker without escalating to the
operator. If repair requires forbidden paths, provider/key use, corpus
ingestion, T12 authoring, public-sync, or readiness claims, stop and return a
blocked diagnostic.

## Required First Reads

| File | Purpose |
|---|---|
| `docs/baselines/CVF_GC018_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_2026-06-10.md` | Confirm authorization and boundary |
| `docs/roadmaps/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_ROADMAP_2026-06-10.md` | Confirm roadmap requirements |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | Verify T10 profile contract and helper |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | Verify descriptor builder |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts` | Verify ECO pack request helper |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts` | Verify LPF governed package helper |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts` | Verify retrieval receipt helper |

## Pre-Flight Checks

| Check | Command | Required result |
|---|---|---|
| Base HEAD captured | `git rev-parse --short HEAD` | record as `executionBaseHead` |
| New test absent before implementation | `Test-Path -LiteralPath EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.aware.pipeline.harness.test.ts` | False |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 0f75ff6f --head HEAD` | PASS before edits or reviewer-recorded if dispatched by operator return |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: domain-profile contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 23-46 | `DscpDomainProfile` | `DscpDomainProfile` | ACCEPT |
| RUNTIME_BEHAVIOR: profile application helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 92-173 | `applyDomainProfileToDescriptorInput` | `ApplyDomainProfileResult` | ACCEPT |
| EXISTS: descriptor metadata owner | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 48-50 | `metadata` | `GovernedArtifactDescriptor` | ACCEPT |
| EXISTS: custom gate owner | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 11-25 | `customGates` | `GovernanceGateSet` | ACCEPT |
| RUNTIME_BEHAVIOR: descriptor builder preserves metadata | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | lines 31-56 | `buildGovernedArtifactDescriptor` | `GovernedArtifactDescriptorResult` | ACCEPT |
| EXISTS: ECO pack request helper | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts` | line 19 | `buildECOGovernedPackRequest` | `GovernedContextPackRequest` | ACCEPT |
| RUNTIME_BEHAVIOR: LPF package blocks raw content release | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts` | lines 42-52 | `buildLPFGovernedPackage` | `GovernedContextPackage` | ACCEPT |
| RUNTIME_BEHAVIOR: retrieval receipt blocks raw source release | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts` | lines 30-52 | `buildGovernedRetrievalReceipt` | `GovernedRetrievalReceipt` | ACCEPT |

## New Doc-Only Fields

None. This work order creates a test harness only.

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.aware.pipeline.harness.test.ts` | Yes | Focused deterministic pipeline harness |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Yes | GC-051 machine registry coverage |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | Yes | GC-051 human registry coverage |
| `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_WORKER_RETURN_2026-06-10.md` | Yes | Worker evidence packet |

## Work-Order Fulfillment Manifest

Closure is invalid if any required artifact is missing or if any forbidden path
is modified.

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\**` | External product edits are out of DSCP-T11 scope |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/**` | No web/runtime/provider route edit authorized |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/**` | Existing ECO source is read-only evidence; worker must not edit it |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/**` | Existing LPF source is read-only evidence; worker must not edit it |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/**` | Existing CPF source contracts are read-only evidence; worker must not edit them |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\**` | EXTERNAL_WORKSPACE_NOT_MODIFIED | EXTERNAL_WORKSPACE_NOT_MODIFIED | Stop if modification is required; external product edits are forbidden |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Existing web files are out of scope; worker must not edit, stage, or claim them |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Existing ECO source is read-only evidence; worker must not edit it |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Existing LPF source is read-only evidence; worker must not edit it |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Existing CPF source contracts are read-only evidence; worker must not edit them |

## Write Ownership

Owned files or modules:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.aware.pipeline.harness.test.ts`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`
- `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_WORKER_RETURN_2026-06-10.md`

Write mode:

modify-listed only.

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Read all Required First Reads.
3. Create the focused profile-aware pipeline harness test.
4. Register the new test path in GC-051 JSON and Markdown.
5. Run CPF `npm run check`.
6. Run focused DSCP-T11 vitest.
7. Run reviewer-fast gate.
8. Author the worker return packet.
9. Stage allowed worker artifacts and return without committing.

## Implementation Contract

Required profile fixtures in tests:

- `legal_policy` profile with `jurisdiction=VN` and `ec02Gate`.
- `technical_project` profile with `moduleId=cvf-control-plane` and
  `stabilityGate`.
- blocked legal-policy profile with `ec02Gate=BLOCKED_UNTIL_2026-07-01`.

Required behavior:

1. Preserve profile metadata through descriptor and package evidence.
2. Preserve profile gate keys in descriptor `customGates` and receipt gate
   results.
3. Prove raw source/content/memory release remains false where evidence fields
   exist.
4. Prove legal-policy gate keys and technical-project gate keys do not bleed
   across descriptors or receipts.
5. Prove blocked profile application returns `blocked=true` and no descriptor
   input is produced.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| `npm run test -- tests/dscp.profile.aware.pipeline.harness.test.ts` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| `git diff --name-status` | only allowed worker paths |
| Worker return packet | includes command output summaries, changed-file list, and claim boundary |

Base-anchor evidence:

- `dispatchBaseHead`: `0f75ff6f`
- `executionBaseHead`: worker captured `0f75ff6f`
- `closureBaseHead`: reviewer-owned post-return value
- Commit mode: `WORKER_MUST_NOT_COMMIT`

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| Legal-policy ECO path proves `domainFamily`, `jurisdiction`, and `ec02Gate` propagation | PASS |
| Technical-project LPF path proves `domainFamily`, `moduleId`, and `stabilityGate` propagation | PASS |
| Raw release evidence remains false | PASS |
| Cross-profile gate and metadata isolation is proven | PASS |
| `BLOCKED_UNTIL_*` stops before descriptor/package/receipt creation | PASS |
| GC-051 JSON and Markdown cover new test path | PASS |
| No forbidden path is modified | PASS |

## Fail Conditions

| Condition | Action |
|---|---|
| Any external `Policy_Local` file needs modification | STOP and return blocked diagnostic |
| Any provider call or API key use appears necessary | STOP and return to reviewer |
| Any corpus ingestion, OCR, vector search, T12, current-law, legal-quality, public-readiness, or production-readiness claim is introduced | STOP and remove claim |
| Existing source contracts must be changed | STOP and return to reviewer unless a separate roadmap authorizes source changes |
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

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: DISPATCHED` | READY |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_COMPLETION_2026-06-10.md` | reviewer-authored post-return | PENDING |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_ROADMAP_2026-06-10.md` | `Status: DISPATCHED` | READY |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | entry covers DSCP-T11 test path | PENDING |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | quick lookup covers DSCP-T11 test path | PENDING |
| System loop interlock | no system-loop mutation | test harness only | N/A with reason: no runtime loop changed |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V17_2026-06-07.md` | reviewer-owned final sync | PENDING |

## Review Gate

Reviewer must confirm:

1. `git diff --name-status` contains only allowed worker paths.
2. CPF `npm run check` PASS.
3. Focused DSCP-T11 vitest PASS.
4. Reviewer-fast PASS.
5. GC-051 JSON and Markdown registry surfaces cover the new test path.
6. Worker return contains all required evidence.

## Closure Checklist

- [ ] Worker return reviewed and accepted
- [ ] CPF `npm run check` PASS confirmed
- [ ] Focused DSCP-T11 vitest PASS confirmed
- [ ] GC-051 registry PASS confirmed
- [ ] Governance gates PASS confirmed
- [ ] Reviewer commits material artifacts
- [ ] Completion review authored by reviewer
- [ ] Session continuity synced by reviewer

## Operator Checkpoint

operator.checkpoint.waiver: operator authorized DSCP-T11 direction on
2026-06-10. Operator approval remains required for external `Policy_Local`
edits, provider/key use, corpus ingestion, T12 authoring, public-sync, or any
readiness claim.

## Return-To-Orchestrator Conditions

Worker returns when:

- all allowed worker artifacts are staged and uncommitted;
- required commands have PASS evidence or a bounded blocker diagnostic;
- no forbidden path is modified;
- worker return packet is complete.

## Reviewer Closure Conversion

```yaml
completionReviewPath: docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_COMPLETION_2026-06-10.md
reviewerOwnedClosurePaths:
  - CVF_SESSION/ACTIVE_SESSION_STATE.json
  - CVF_SESSION_MEMORY.md
  - AGENT_HANDOFF_V17_2026-06-07.md
  - docs/roadmaps/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_ROADMAP_2026-06-10.md
  - docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_FOR_CLAUDE_2026-06-10.md
closedStatusTokens:
  - CLOSED_PASS_BOUNDED
reviewerClosureCompleted: false
forbiddenClosedEquivalentResidue: []
```

## Claim Boundary

This work order authorizes only a local deterministic test harness. It does not
claim provider behavior, live governance proof, retrieval quality, semantic
correctness, corpus ingestion, OCR, vector search, PolicyLocal T12 readiness,
legal advice quality, current-law status, public readiness, hosted readiness,
production readiness, public-sync, memory reinjection, high-risk promotion,
Learning Orchestrator runtime behavior, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; not public-synced.
