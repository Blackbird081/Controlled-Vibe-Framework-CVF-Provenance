# CVF Agent Work Order: DSCP-T10 Domain Profile And Scan Adapter Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-10

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `27123c55`

executionBaseHead: `<worker must capture before edits>`

closureBaseHead: `0afa8737`

---

## Purpose

Implement a bounded deterministic DSCP domain-profile contract so CVF scan and
memory packaging can carry domain-specific language, facet, gate, and boundary
rules without hard-coding PolicyLocal/Vietnamese legal-policy behavior into the
generic DSCP foundation.

## Authority Chain

Operator instruction 2026-06-10 -> GC-018:
`docs/baselines/CVF_GC018_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_2026-06-10.md`
-> roadmap:
`docs/roadmaps/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_ROADMAP_2026-06-10.md`
-> this work order.

Active session state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

Prerequisite release evidence:

| Prerequisite | Artifact | Commit | Disposition |
|---|---|---|---|
| DSCP-T9 local pipeline harness | `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_COMPLETION_2026-06-08.md` | `5c90506a` | ACCEPT |
| DSCP-T6 scan descriptor runtime | `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md` | `13cc1505` | ACCEPT |
| DSCP-T7 ECO multi-domain pilot | `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md` | `958f8d2b` | ACCEPT |
| DSCP-T8 LPF cross-lane wire-in | `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_COMPLETION_2026-06-08.md` | `e96aacaf` | ACCEPT |

## Agent Roles

| Role | Agent | Responsibility |
|---|---|---|
| Worker | Claude | Implement contract/test/registry/worker return; do not commit |
| Reviewer | Codex | Review, run gates, close and commit if PASS |
| Operator | Human | Authorized DSCP-T10 direction on 2026-06-10 |

## Scope / Target / Owner Boundary

Allowed scope:

- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`.
- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts`.
- Update only the required CPF export barrel or `src/index.ts` so the new
  contract is importable.
- Update `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts`
  if source inspection confirms it is the minimal CPF export owner.
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only for the
  new source/test path coverage.
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` only for the
  DSCP-T10 quick lookup row/section.
- Create
  `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_WORKER_RETURN_2026-06-10.md`.

Reviewer-owned closure scope:

- `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_COMPLETION_2026-06-10.md`
- `docs/reviews/CVF_GC019_DSCP_T10_DOMAIN_PROFILE_CONTRACT_STRUCTURAL_REVIEW_2026-06-10.md`
- `docs/roadmaps/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_ROADMAP_2026-06-10.md`
- this work order status conversion;
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V17_2026-06-07.md`

Forbidden scope:

- Do not modify the external `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local`
  workspace.
- Do not edit cvf-web, ECO runtime retrieval, LPF memory runtime, or provider
  routing.
- Do not run provider calls, load API keys, ingest corpus files, perform OCR,
  create vector retrieval, author PolicyLocal T12, public-sync, push, or claim
  hosted/production/public readiness.

Risk ceiling:

R1 local deterministic source contract and tests only.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap section | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Purpose: split common scan/memory method from domain-specific rules | Purpose | new domain-profile contract | focused vitest | PASS |
| Implementation targets | Scope and Required Artifact Manifest | source/test/registry/return paths | `git diff --name-status` | PASS |
| Acceptance: profile supports multiple domains/languages | Implementation Contract | tests for legal, company docs, technical docs | focused vitest | PASS |
| Acceptance: gate keys copied only when allowed | Implementation Contract | `applyDomainProfileToDescriptorInput` or equivalent | focused vitest | PASS |
| Boundary: no external Policy_Local edits | Forbidden scope | no external changed files | repo diff plus no external writes | PASS |

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within allowed
scope must be repaired and rerun by the worker without escalating to the
operator. If repair requires external product edits, provider/key use, corpus
ingestion, T12 authoring, public-sync, or any forbidden path, stop and return a
blocked diagnostic with exact evidence.

## Required First Reads

| File | Purpose |
|---|---|
| `docs/baselines/CVF_GC018_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_2026-06-10.md` | Confirm authorization and boundary |
| `docs/roadmaps/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_ROADMAP_2026-06-10.md` | Confirm roadmap requirements |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | Verify DSCP gate and metadata owner interfaces |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | Verify descriptor builder behavior |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts` | Verify ECO adapter remains generic |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts` | Verify LPF adapter lock behavior remains separate |
| `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | Confirm common facet schema and domain extensions |
| `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | Confirm classification vocabulary is not legal-only |

## Pre-Flight Checks

| Check | Command | Required result |
|---|---|---|
| Clean working tree | `git status --short` | no unexpected modified files |
| Base HEAD captured | `git rev-parse --short HEAD` | record as `executionBaseHead` |
| New source absent before implementation | `Test-Path -LiteralPath EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | False |
| New test absent before implementation | `Test-Path -LiteralPath EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts` | False |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 27123c55 --head HEAD` | PASS before edits |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: DSCP governance gate set has `customGates` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 13-25 | `customGates` | `GovernanceGateSet` | ACCEPT |
| EXISTS: DSCP artifact descriptor has open `metadata` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 31-50 | `metadata` | `GovernedArtifactDescriptor` | ACCEPT |
| EXISTS: artifact descriptor builder accepts `metadata` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | lines 11-18 | `metadata` | `GovernedArtifactDescriptorInput` | ACCEPT |
| RUNTIME_BEHAVIOR: descriptor builder preserves supplied metadata | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | lines 50-57 | `buildGovernedArtifactDescriptor` | `GovernedArtifactDescriptorResult` | ACCEPT |
| EXISTS: ECO adapter builds governed pack request from RAG result | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts` | lines 19-35 | `buildECOGovernedPackRequest` | `GovernedContextPackRequest` | ACCEPT |
| EXISTS: LPF adapter builds governed package from memory block | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts` | lines 42-61 | `buildLPFGovernedPackage` | `GovernedContextPackage` | ACCEPT |
| CANONICAL_CONTRACT: common search/filter facets permit project domain extensions | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | lines 73-115 | common facet schema and domain extension examples | corpus search/filter readiness standard | ACCEPT |
| CANONICAL_CONTRACT: classification vocabulary is not legal-only | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | lines 69-108 | knowledge regions, owner surfaces, answer classes | corpus intelligence classification standard | ACCEPT |

## Current Runtime Freshness Verification

Repo search on 2026-06-10 found no existing DSCP `domainProfile`,
`DomainProfile`, `ScanDomainProfile`, or `domainProfileId` source contract in
active DSCP source. Existing `profileId` hits are unrelated governed-session or
release-grade profile fields, not scan-domain profiles.

## New Doc-Only Fields

None. This work order authorizes new source contract fields, not doc-only
fields.

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | Yes | DSCP-T10 domain-profile contract and helper |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts` | Yes | Focused deterministic test coverage |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Yes | GC-051 machine registry coverage |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | Yes | GC-051 human registry coverage |
| `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_WORKER_RETURN_2026-06-10.md` | Yes | Worker evidence packet |

## Work-Order Fulfillment Manifest

This work order's fulfillment manifest is the `Required Artifact Manifest`,
`Forbidden Path Manifest`, and `Evidence Requirements` set in this packet.
Closure is invalid if any required artifact is missing or if any forbidden path
is modified.

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\**` | External product edits are out of DSCP-T10 scope |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/**` | No web/runtime/provider route edit authorized |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/**` except existing read-only imports | No ECO runtime retrieval change authorized |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/**` | No LPF memory runtime change authorized |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\**` | EXTERNAL_WORKSPACE_NOT_MODIFIED | EXTERNAL_WORKSPACE_NOT_MODIFIED | Stop if modification is required; external product edits are forbidden |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Existing web files are out of scope; worker must not edit, stage, or claim them |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Existing ECO source is read-only evidence; worker must not edit it |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Existing LPF source is out of scope; worker must not edit it |

## Write Ownership

Owned files or modules:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts`
- one existing CPF export barrel or `src/index.ts`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`;
- `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_WORKER_RETURN_2026-06-10.md`.

Write mode:

modify-listed only.

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Verify the working tree contains only expected dispatch files before
   implementation.
3. Read all Required First Reads.
4. Create the DSCP domain-profile source contract.
5. Create focused CPF tests for legal-policy, company-docs, and
   technical-project profiles.
6. Add the minimal CPF export needed for imports.
7. Register new source/test paths in GC-051 JSON and Markdown.
8. Run CPF `npm run check`.
9. Run focused DSCP-T10 vitest.
10. Run reviewer-fast gate.
11. Author the worker return packet.
12. Stage allowed worker artifacts and return without committing.

## Implementation Contract

Create a deterministic source contract with names equivalent to the following.
Exact names may vary only if the worker records the source-fidelity reason in
the worker return:

- `DomainProfileId` type alias or string field;
- `DscpDomainFamily` union covering at least:
  - `legal_policy`;
  - `company_docs`;
  - `technical_project`;
  - `governance_docs`;
  - `mixed_corpus`;
- `DscpDomainProfile` interface with:
  - `domainProfileId`;
  - `domainFamily`;
  - `languageCodes`;
  - `commonFacetFields`;
  - `domainFacetFields`;
  - `domainGateKeys`;
  - `boundaryRules`;
  - `defaultMetadata`;
- deterministic helper to apply a profile to descriptor input, for example:
  `applyDomainProfileToDescriptorInput(profile, input, options)`.

Required behavior:

1. Preserve existing `GovernedArtifactDescriptorInput` fields.
2. Add profile metadata without overwriting explicit caller metadata unless the
   caller opts in through an explicit option.
3. Copy only gate keys listed in `domainGateKeys` into `customGates`.
4. Surface unknown gate keys as diagnostics, blocked result, or rejected keys in
   a deterministic result object.
5. Keep all logic local and deterministic with no file I/O, provider call, raw
   content release, or product workspace dependency.

Required profile fixtures in tests:

- PolicyLocal/Vietnamese legal-policy profile:
  - language code includes `vi`;
  - legal/policy fields are profile-owned, not global.
- Company docs profile:
  - fields include business-unit or policy-owner style metadata.
- Technical/project docs profile:
  - fields include module/runtime/interface style metadata.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| `npm run test -- tests/dscp.domain.profile.contract.test.ts` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS or pending-review acceptable only if finality is the only failure |
| `git diff --name-status` | only allowed worker paths |
| Worker return packet | includes command output summaries, changed-file list, and claim boundary |

Base-anchor evidence:

- `dispatchBaseHead`: `27123c55`
- `executionBaseHead`: worker must capture before edits
- `closureBaseHead`: reviewer-owned post-return value
- Commit mode: `WORKER_MUST_NOT_COMMIT`

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| DSCP domain-profile contract compiles | PASS |
| Focused tests cover legal-policy, company-docs, and technical-project profiles | PASS |
| PolicyLocal profile fields do not become global DSCP defaults | PASS |
| Unknown domain gate key behavior is deterministic and tested | PASS |
| Existing DSCP descriptor metadata and `customGates` remain compatible | PASS |
| GC-051 JSON and Markdown cover new source/test paths | PASS |
| No external product workspace files are modified | PASS |

## Fail Conditions

| Condition | Action |
|---|---|
| Any external `Policy_Local` file needs modification | STOP and return blocked diagnostic |
| Any provider call or API key use appears necessary | STOP and return to reviewer |
| Any corpus ingestion, OCR, vector search, T12, current-law, legal-quality, public-readiness, or production-readiness claim is introduced | STOP and remove claim |
| New profile fields are claimed as existing source facts | STOP and correct Source Verification |
| GC-051 cannot cover the new paths cleanly | STOP and return exact registry error |

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
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_COMPLETION_2026-06-10.md` | reviewer-authored post-return | PASS |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_ROADMAP_2026-06-10.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | entry covers new DSCP-T10 source/export/test paths | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | quick lookup covers new DSCP-T10 source/export/test paths | PASS |
| External evidence digest | GC-018 baseline section | sha256:c1699f4bcb36eb4523605fb0e2f2baacfb83a5838f910100f9f3ca53ddecbbb8; sha256:ab2d0045f2e6e271a9060a86c3895e08ee5ff9a1361533bff3814f0279383100; sha256:77fd13ba3397b6fdaca32e4246a85598117891fa754f05f243884fd5a2699602; sha256:7b1ec0f74f8578a46dd4a7419fe1478cb5c490d38b60853d2e137728a5c11b78 | PASS |
| System loop interlock | no system-loop mutation | domain-profile helper only | N/A with reason: no runtime loop changed |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V17_2026-06-07.md` | reviewer-owned final sync | PASS |

## Review Gate

Reviewer must confirm:

1. `git diff --name-status` contains only allowed worker paths.
2. CPF `npm run check` PASS.
3. Focused DSCP-T10 vitest PASS.
4. Reviewer-fast PASS or finality-only pending state is resolved before commit.
5. GC-051 JSON and Markdown registry surfaces cover new source/test paths.
6. Worker return contains all required evidence.

## Closure Checklist

- [x] Worker return reviewed and accepted
- [x] CPF `npm run check` PASS confirmed
- [x] Focused DSCP-T10 vitest PASS confirmed
- [x] GC-051 registry PASS confirmed
- [x] Governance gates PASS confirmed
- [x] Reviewer commits material artifacts
- [x] Completion review authored by reviewer
- [x] Session continuity synced by reviewer

## Operator Checkpoint

operator.checkpoint.waiver: operator authorized Codex on 2026-06-10 to raise the
CVF foundation beyond the current PolicyLocal/Vietnamese policy scan use case.
No additional operator decision is required for Claude to execute this local
deterministic contract tranche. Operator approval remains required for external
Policy_Local edits, provider/key use, corpus ingestion, T12 authoring,
public-sync, or any readiness claim.

## Return-To-Orchestrator Conditions

Worker returns when:

- all allowed worker artifacts are staged and uncommitted;
- required commands have PASS evidence or a bounded blocker diagnostic;
- no forbidden path is modified;
- worker return packet is complete.

## Reviewer Closure Conversion

```yaml
completionReviewPath: docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_COMPLETION_2026-06-10.md
reviewerOwnedClosurePaths:
  - CVF_SESSION/ACTIVE_SESSION_STATE.json
  - CVF_SESSION_MEMORY.md
  - AGENT_HANDOFF_V17_2026-06-07.md
  - docs/roadmaps/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_ROADMAP_2026-06-10.md
  - docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_FOR_CLAUDE_2026-06-10.md
closedStatusTokens:
  - CLOSED_PASS_BOUNDED
reviewerClosureCompleted: true
forbiddenClosedEquivalentResidue: []
```

## Claim Boundary

This work order authorizes a local deterministic source contract and focused
tests. It does not claim provider behavior, live governance proof, retrieval
quality, semantic correctness, corpus ingestion, OCR, vector search,
PolicyLocal T12 readiness, legal advice quality, current-law status, public
readiness, hosted readiness, production readiness, public-sync, memory
reinjection, high-risk promotion, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; not public-synced.
