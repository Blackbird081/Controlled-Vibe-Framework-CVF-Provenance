# CVF Agent Work Order - Public External Evaluation Package And Catalog Alignment

Memory class: FULL_RECORD
Status: DISPATCHED_TO_CLAUDE
Date: 2026-06-20
docType: work_order
Batch ID: PECA-T1
Owner: Claude worker, Codex reviewer
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: `f2330d0e`
executionBaseHead: worker must refresh with `git rev-parse --short HEAD` before editing and report the value.
closureBaseHead: N/A - pending Codex reviewer conversion once worker returns.
rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Claude worker under Codex/orchestrator review.

Canonical packet: this work order and matching PECA-T1 GC-018.

Commit mode: `WORKER_MUST_NOT_COMMIT`. Do not commit, push, tag, release, or
publish.

Execution surface: sibling public-sync clone only:
`D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`.

Current-time notes: current mode is
`delta_t11_durable_audit_evidence_bundle_closed_next_foundation_ready`;
Delta-T11 is closed at session-sync commit `f2330d0e`. The selected lane is
public/external-evaluation package and catalog alignment. Delta-T12 is not
opened by default.

Do-not-misread notes: the durable public technical product catalog is the
reader orientation surface. The 2026-06-19 public external review snapshot is a
dated evidence artifact, not the whole catalog. Do not publish private
provenance material or claim readiness, universal control, direct interception,
or new runtime behavior.

Required first actions: read `CVF_SESSION_MEMORY.md`, resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, read `AGENT_HANDOFF_V20_2026-06-19.md`,
read this work order and the matching GC-018, switch to the public-sync clone,
verify `git remote -v`, capture `executionBaseHead`, then run the
pre-implementation gate from the provenance repo before public-sync edits if
available.

Return contract: return uncommitted public-sync artifacts for Codex review with
`COMPLETE_PENDING_REVIEW`, `executionBaseHead`, exact changed paths, commands
run, path-link proof, and claim boundary; or return `BLOCKED_WITH_REASON` with
evidence. Codex owns review, public-sync commit/push decision, provenance
closure conversion, and session sync.

## Purpose

Give Claude a bounded public-sync documentation task that makes the public CVF
repository clearer for external agents and user developers. The work must
preserve the technical product catalog as the durable public orientation
surface and frame the 2026-06-19 public external review snapshot as dated
evidence only.

## Required First Reads

| Artifact | Use |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | active mode, next move, parked scope |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable continuity |
| `AGENT_HANDOFF_V20_2026-06-19.md` | current handoff and no-commit boundary |
| `docs/baselines/CVF_GC018_PUBLIC_EXTERNAL_EVALUATION_PACKAGE_CATALOG_ALIGNMENT_2026-06-20.md` | exact authorization |
| `AGENTS.md` | public/provenance repository boundary |
| `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` | catalog authority and public-sync path verification rule |
| `docs/reference/external_agent_review/README.md` | external-agent review reference front door |
| `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\README.md` | public front door |
| `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\docs\reference\CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` | public catalog |
| `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\docs\guides\external-agent-review-guide.md` | external reviewer guide |
| `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\docs\evidence\public-external-review-snapshot-2026-06-19.md` | dated evidence snapshot |

## Scope / Target / Owner Boundary

Allowed scope in the sibling public-sync clone only:

- update `README.md`;
- update `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`;
- update `docs/guides/external-agent-review-guide.md`;
- update `docs/evidence/public-external-review-snapshot-2026-06-19.md`;
- create `docs/reviews/CVF_PUBLIC_EXTERNAL_EVALUATION_PACKAGE_CATALOG_ALIGNMENT_COMPLETION_2026-06-20.md`;
- run read-only path/link/grep checks needed to prove the public front door is
  coherent.

Allowed scope in this private provenance repo:

- none for Claude. Claude must not edit this provenance repo.

Forbidden scope:

- no commits, staging for commit, push, tag, release, or GitHub publication;
- no provenance workspace edits by Claude;
- no private provenance packets, active handoffs, raw logs, secrets, or hidden
  operator material copied into public-sync;
- no runtime/source behavior changes, provider/live calls, CVF Web behavior,
  package/dependency edits, lockfile edits, CI workflow edits, generated session
  state, queue/daemon, MCP/tool registration, or launcher/profile expansion;
- no direct IDE/shell/git/filesystem interception, wrapper/proxy enforcement,
  production, hosted, release, enterprise, route-coverage, benchmark parity, or
  universal governed-coding-control claims.

## Write Ownership

Claude may write only the public-sync paths listed in Allowed scope. Claude may
not write any private provenance path, Git metadata path, package/dependency
path, CI workflow, runtime/source path, active session path, or handoff path.

Codex owns any public-sync commit/push, provenance closure conversion, and
session-sync edits once the uncommitted worker return is reviewed.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| intake summary | operator approved continuing to a Claude work order from Delta-T11 closure `3d0b70c5` and session-sync `f2330d0e`, targeting public/external-evaluation catalog clarity |
| scope classification | bounded public documentation alignment in public-sync |
| risk sensitivity | R1 documentation-only; no runtime/provider/live behavior |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| role separation basis | Claude edits uncommitted public-sync working tree; Codex reviews, commits, pushes only if safe, closes, and syncs provenance |
| escalation condition | return `BLOCKED_WITH_REASON` if the task requires private provenance publication, runtime/provider/live work, secrets, dependency changes, CI rewrites, commits, push, or claim expansion |

## Authority Chain

| Level | Artifact | Status |
| --- | --- | --- |
| Operator | current instruction, 2026-06-20 | ACCEPTED |
| Session | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION_MEMORY.md` | next move selects public/external-evaluation package/catalog alignment |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | active |
| Public/provenance boundary | `AGENTS.md` | binding |
| Catalog authority | `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` | active provenance source catalog |
| External review reference | `docs/reference/external_agent_review/README.md` | active index |
| GC-018 | `docs/baselines/CVF_GC018_PUBLIC_EXTERNAL_EVALUATION_PACKAGE_CATALOG_ALIGNMENT_2026-06-20.md` | DISPATCHED_TO_CLAUDE |

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Dispatcher | Codex | source-verified packet and dispatch |
| Implementer | Claude | uncommitted public-sync documentation edits and completion review |
| Reviewer/committer | Codex | inspect worker return, run gates/checks, commit/push or reject |
| Session-sync actor | Codex | update provenance continuity only once public-sync outcome is accepted |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason: Claude is not authorized to
edit protected provenance guards, active state, active handoff, front door, or
session source. Public-sync documentation edits are allowed only in the sibling
public-sync clone.

Protected paths:

- N/A with reason: no protected provenance path is worker-owned.

Human authorization: the operator approved continuing to a Claude work order for
the post-T11 public/external-evaluation package and catalog alignment lane.

Rollback boundary: Codex may reject or revert only PECA-T1 public-sync working
tree changes if returned work is unsafe. Do not alter Delta-T11 closure commit
`3d0b70c5`, session-sync commit `f2330d0e`, or earlier provenance history.

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | worker-no-commit split: Claude worker returns uncommitted public-sync artifacts; Codex reviewer owns commit/push decision and closure |
| phase | DISPATCH_AUTHORING, WORKER_EXECUTION, REVIEWER_CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatch=`f2330d0e`; execution=worker refreshed public-sync/provenance heads; closure=N/A pending |
| changedSetScope(phase) | dispatch packet; public-sync docs and completion review; reviewer closure conversion; separate sync |
| traceScope(phase, actor) | exact manifests and commands per phase |
| commitOwner(phase) | Codex only |
| crossBatchIsolation | worker must start from clean public-sync worktree or return BLOCKED; Before status evidence: public-sync `git status --short` clean at `94bb69dc8`, provenance dispatch base clean at `f2330d0e` |
| nextMoveSurfaces | Claude must not edit; Codex handles during reviewer closure |
| closerOwner | Codex is designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
| --- | --- |
| completionReviewPath | public-sync `docs/reviews/CVF_PUBLIC_EXTERNAL_EVALUATION_PACKAGE_CATALOG_ALIGNMENT_COMPLETION_2026-06-20.md` |
| reviewerOwnedClosurePaths | matching GC-018, this work order, public-sync completion review, public-sync changed docs, and active session state/front door/handoff only if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| reviewerAction | Codex must review uncommitted public-sync diff before any public commit or push |

## Public Catalog Alignment Control Block

| Field | Disposition |
| --- | --- |
| catalog role | durable public orientation for CVF capabilities, boundaries, and user-developer understanding |
| snapshot role | dated evidence artifact for 2026-06-19 public external review context |
| README role | route readers to catalog for understanding and snapshot for evidence |
| external-agent guide role | paste-ready review instructions requiring source-backed findings |
| public/private boundary | public-safe summaries only; no private provenance disclosure |
| export boundary | Claude may edit public-sync working tree but must not commit or push |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | N/A with reason: PECA-T1 is public documentation alignment, not Delta execution evidence |
| claimDisposition | N/A with reason: documentation-only public catalog alignment |
| receiptEvidence | N/A with reason: no new receipt or execution evidence is created |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | Claude edits public documentation only after remote/worktree verification |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | public reader orientation and dated evidence clarification only |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, EDIT/COMMIT execution, provider/live proof, readiness, and universal control remain parked |

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active next move recommends public/external-evaluation package and catalog alignment from public-sync only. | VALUE_SET | `CVF_SESSION_MEMORY.md` | lines 134-137 | `nextAllowedMove` | active session front door | ACCEPT |
| Active next move does not open Delta-T12 by default. | LITERAL_INVARIANT | `CVF_SESSION_MEMORY.md` | line 137 | `deltaT12Default` | active session front door | ACCEPT |
| Parked scope keeps runtime/provider/public-sync execution and universal claims bounded. | LITERAL_INVARIANT | `CVF_SESSION_MEMORY.md` | lines 140-145 | `parkedScope` | active session front door | ACCEPT |
| Public repository URL is the public CVF target. | VALUE_SET | `AGENTS.md` | line 167 | `publicRepositoryUrl` | public/provenance boundary | ACCEPT |
| Public-facing changes must use sibling public-sync clone. | VALUE_SET | `AGENTS.md` | lines 171-178 | `publicSyncClonePath` | public/provenance boundary | ACCEPT |
| Public-sync catalog is the customer-facing derivative. | LITERAL_INVARIANT | `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` | line 32 | `publicSyncCatalog` | technical product catalog | ACCEPT |
| Public-sync catalog paths must be verified from the public-sync clone. | LITERAL_INVARIANT | `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` | lines 39-41 and 251-255 | `testPathVerificationRule` | technical product catalog | ACCEPT |
| External-agent review front door prepares public-context summaries but does not authorize public-sync by itself. | LITERAL_INVARIANT | `docs/reference/external_agent_review/README.md` | lines 20-24 and 89 | `externalReviewFrontDoor` | external agent review reference | ACCEPT |
| External-agent packet template is used when public catalog wording or public/private context boundaries need review. | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md` | lines 27-29 | `externalReviewPacketTemplate` | external agent review reference | ACCEPT |

## Current Public-Sync Freshness Verification

| Surface | Evidence |
| --- | --- |
| public-sync clone path | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync` exists |
| remote verification | `git -c safe.directory=... -C <public-sync> remote -v` returned `origin https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` for fetch and push |
| public-sync HEAD at dispatch authoring | `94bb69dc8` |
| public-sync worktree at dispatch authoring | `git -c safe.directory=... -c core.optionalLocks=false -C <public-sync> status --short` returned no changed paths |
| README public start-here table | lines 21-28 contain Architecture, Technical Product Catalog, External Agent Review Guide, and 2026-06-19 Public External Review Snapshot rows |
| path existence | public-sync `README.md`, `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`, `docs/guides/external-agent-review-guide.md`, and `docs/evidence/public-external-review-snapshot-2026-06-19.md` exist |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | public-context package and catalog alignment |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; public export disposition guard |
| Owner surface | PECA-T1 work order |
| Disposition | `DO_NOW` public documentation alignment only |
| Claim boundary | no runtime/provider/live/interception/readiness/universal-control claim |

## Rescan Intelligence Hardening

Original source artifact: public-sync `README.md` and public external review
surfaces.

Predecessor intake artifact: Delta-T11 closure session state `f2330d0e`.

Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS - this dispatch converts the
operator's catalog/snapshot ambiguity finding into a bounded public-sync work
order.

Routing matrix status: COMPLETE_WITH_DECLARED_LIMITS - public documentation
alignment is routed now; runtime/provider/public release claims remain out of
scope.

Semantic sampling status: COMPLETE_WITH_DECLARED_LIMITS - representative public
reader mistakes are checked below.

- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | PECA-T1 disposition |
| --- | --- |
| UNCHANGED_FROM_INTAKE | Public-sync is the only public GitHub surface. |
| CHANGED_DISPOSITION | Catalog vs dated snapshot ambiguity becomes a bounded work order. |
| NEW_FINDING | Public front door must not make the 2026-06-19 snapshot look like the whole catalog. |
| REMOVED_OR_REJECTED | Runtime, provider/live, readiness, direct interception, and universal-control claims remain rejected. |

### Follow-Up Routing Matrix

| Routing lane | PECA-T1 route |
| --- | --- |
| DO_NOW | Public README/catalog/snapshot/guide wording alignment plus public completion review. |
| SEPARATE_RUNTIME_TRANCHE | Runtime/public release proof, live provider proof, route coverage, enforcement implementation. |
| STRATEGIC_OPERATOR_DECISION | Later public release/tag or broader marketing/product repositioning. |
| OUT_OF_SCOPE | Private provenance disclosure, dependency updates, CI rewrites, provider execution. |
| RESOLVED_BY_DESIGN | Distinguish durable catalog from dated evidence snapshot in public front door. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| PECA-RIH-001 | public README Start Here | catalog and snapshot both appear in routing table | DO_NOW | Could readers treat snapshot as the catalog replacement? | PASS - work order requires explicit role distinction. |
| PECA-RIH-002 | technical product catalog | catalog is customer-facing derivative | DO_NOW | Could catalog disappear from external-agent route? | PASS - work order requires catalog remain front-door orientation. |
| PECA-RIH-003 | external review snapshot | snapshot has 2026-06-19 date | DO_NOW | Could dated evidence imply current full system state? | PASS - work order requires point-in-time language. |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order owner | Evidence |
| --- | --- | --- |
| Delta-T11 closure selected public/external-evaluation package/catalog alignment | Codex dispatch | `CVF_SESSION_MEMORY.md` next allowed move and matching GC-018 |
| Public-sync only | Claude worker and Codex reviewer | AGENTS.md boundary plus remote verification |
| Catalog is durable orientation | Claude worker | README/catalog/guide wording and path checks |
| Snapshot is dated evidence | Claude worker | snapshot claim-boundary update and README wording |
| No public readiness or universal-control claim | Claude worker and Codex reviewer | claim boundary and public export disposition |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| stable source | public-sync documentation surfaces listed in Allowed scope |
| durable store target | N/A with reason: no runtime durable store is added |
| dated execution artifacts | this GC-018, this work order, and the public-sync completion review |
| generated aggregate | N/A with reason: no generated aggregate is added |
| index | public README start-here table and technical product catalog only |

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| public-sync `README.md` | Yes | public front-door start-here routing |
| public-sync `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` | Yes | durable catalog orientation |
| public-sync `docs/guides/external-agent-review-guide.md` | Yes | external-agent reading order and prompt |
| public-sync `docs/evidence/public-external-review-snapshot-2026-06-19.md` | Yes | dated evidence snapshot |
| public-sync `docs/reviews/CVF_PUBLIC_EXTERNAL_EVALUATION_PACKAGE_CATALOG_ALIGNMENT_COMPLETION_2026-06-20.md` | Yes | worker-return completion packet |

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| private provenance repo files | Claude has no provenance edit authority in this work order |
| public-sync `.git/**` | no direct Git metadata edits |
| public-sync `.github/**` | no CI workflow changes |
| public-sync `package.json`; `package-lock.json` | no package/dependency changes |
| public-sync runtime/source files under `EXTENSIONS/**` | documentation-only public alignment |
| private/session files `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md` | Codex-only session sync after review |

## Pre-Flight Checks

Claude must run these before editing:

- from private provenance: confirm this work order and matching GC-018 are the
  active packet;
- from public-sync: `git remote -v`;
- from public-sync: `git rev-parse --short HEAD`;
- from public-sync: `git status --short`;
- from public-sync: path existence checks for README, catalog, guide, and
  snapshot.

The public-sync worktree must be clean before edits. Dispatch authoring
evidence found the public-sync worktree clean at public-sync HEAD `94bb69dc8`.

## Execution Plan

1. Start in the private provenance repo only long enough to read this work
   order, the matching GC-018, active state, and active handoff.
2. Switch to the sibling public-sync clone.
3. Run `git remote -v`; stop unless `origin` fetch and push point to
   `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`.
4. Run `git status --short`; stop unless the public-sync worktree is clean or
   record pre-existing changes and return `BLOCKED_WITH_REASON`.
5. Capture public-sync `executionBaseHead` with `git rev-parse --short HEAD`.
6. Inspect README, catalog, external-agent review guide, and 2026-06-19
   snapshot for duplicate or ambiguous catalog/snapshot routing.
7. Apply the smallest wording edits that satisfy acceptance criteria.
8. Add a public-sync completion review with changed files, command evidence,
   path checks, public export disposition, and claim boundary.
9. Run path existence checks for every touched link and a grep scan for
   duplicate "latest public front-door/catalog sync" or equivalent stale row.
10. Return uncommitted changes to Codex with `COMPLETE_PENDING_REVIEW`.

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | Public README sends user developers/external agents to the technical product catalog for system shape, capabilities, and boundaries. |
| AC2 | Public README and external-agent guide describe the 2026-06-19 snapshot as dated evidence, not as the whole catalog. |
| AC3 | The public technical product catalog remains discoverable and clearly framed as the durable external/user-developer orientation surface. |
| AC4 | The public snapshot records its point-in-time boundary and preserves no-readiness/no-universal-control limits. |
| AC5 | Public-sync path checks prove every linked public path exists after edits. |
| AC6 | Claude returns uncommitted changes and command evidence; Codex owns public commit/push after review. |

## Evidence Requirements

Claude must report:

- `git remote -v` from public-sync;
- `git rev-parse --short HEAD` from public-sync;
- `git status --short` before and after edits from public-sync;
- path existence proof for every touched public link;
- grep scan for stale duplicate rows or ambiguous phrases:
  `catalog`, `snapshot`, `latest public`, `front-door`;
- any public-sync markdown/link validation command available without network;
- exact changed-file manifest.

Provider/live proof is not applicable because this tranche is public
documentation alignment only.

## Review Gate

Codex must not accept the worker return unless:

- public-sync remote evidence still points to
  `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`;
- the changed paths stay inside Allowed scope;
- every touched README/guide/catalog/snapshot link resolves in public-sync;
- the completion review records public export disposition and claim boundary;
- no private provenance, runtime/provider/live, readiness, or universal-control
  claim was added.

## Closure Checklist

- [ ] Claude returned `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.
- [ ] Codex reviewed public-sync diff against this work order.
- [ ] Codex ran public-sync path/link checks.
- [ ] Codex committed/pushed public-sync only if remote verification passed.
- [ ] Codex converted this GC-018/work order to closure status or recorded
  blocked disposition.
- [ ] Codex updated active session continuity only once the outcome is accepted.

## Operator Checkpoint

Operator checkpoint is required before any public push if the public-sync remote
does not match `Controlled-Vibe-Framework-CVF.git`, if the changed set expands
outside public documentation, or if the worker proposes public readiness,
runtime/provider/live, private provenance publication, or universal-control
claims.

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope markdown, link, wording, and completion-review
defects without asking the operator. Claude must stop and return
`BLOCKED_WITH_REASON` if repair requires commits, push, private provenance
publication, runtime/source edits, secrets/quota, dependency changes, CI
workflow changes, risk escalation, or claim-boundary expansion.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if:

- public-sync remote is not `Controlled-Vibe-Framework-CVF.git`;
- public-sync worktree is dirty before Claude edits;
- the task requires private provenance disclosure;
- the task requires runtime/source/provider/live/dependency/CI changes;
- README/catalog/snapshot consistency cannot be achieved without removing a
  required public evidence path;
- any public readiness or universal-control claim would be needed to satisfy
  the request.

## Worker Return Schema

Claude must return:

```text
COMPLETE_PENDING_REVIEW
executionBaseHead: <public-sync short head before edits>
dispatchBaseHead: f2330d0e
publicSyncRemoteVerified: <yes/no plus remote URL>
changedPaths:
- <path>
commands:
- <command> => <PASS/FAIL summary>
claimBoundary: public documentation alignment only; no runtime/provider/live/direct-interception/readiness/universal-control claim
```

or:

```text
BLOCKED_WITH_REASON
executionBaseHead: <public-sync short head or N/A>
dispatchBaseHead: f2330d0e
reason: <source-backed blocker>
```

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Codex / local provenance workspace plus read-only public-sync verification |
| Session or invocation | PECA-T1 dispatch, 2026-06-20 |
| Working directory | private provenance repository root |
| Command or tool surface | startup reads, source verification, apply_patch, pre-dispatch gates |
| Target paths | this work order and matching PECA-T1 GC-018 |
| Allowed scope source | current instruction, active next move, this work order, matching GC-018 |
| Before status evidence | worktree clean at provenance dispatch base `f2330d0e`; public-sync worktree clean at `94bb69dc8` |
| After status evidence | dispatch `git status --short` |
| Diff evidence | dispatch `git diff --name-status` |
| Approval boundary | Codex may create dispatch artifacts only; Claude edits public-sync no-commit |
| Claim boundary | public documentation alignment only; no runtime/provider/live/readiness/universal-control claim |
| Agent type | dispatcher under `MULTI_AGENT_MULTI_ROLE` |
| Invocation ID | `peca-t1-public-external-evaluation-package-catalog-alignment-dispatch-2026-06-20` |
| Expected manifest | `docs/baselines/CVF_GC018_PUBLIC_EXTERNAL_EVALUATION_PACKAGE_CATALOG_ALIGNMENT_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_EXTERNAL_EVALUATION_PACKAGE_CATALOG_ALIGNMENT_FOR_CLAUDE_2026-06-20.md` |
| Actual changed set | `docs/baselines/CVF_GC018_PUBLIC_EXTERNAL_EVALUATION_PACKAGE_CATALOG_ALIGNMENT_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_EXTERNAL_EVALUATION_PACKAGE_CATALOG_ALIGNMENT_FOR_CLAUDE_2026-06-20.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: deletion/rename forbidden |

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: this work order dispatches the public-sync update, but no reviewed
public-sync commit or push exists yet for PECA-T1. Next action is Claude
uncommitted worker return, then Codex review, public-sync commit, and public
push only if the remote remains `Controlled-Vibe-Framework-CVF.git`.

## Machine Closure Package

| Closure item | Artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| GC-018 baseline | `docs/baselines/CVF_GC018_PUBLIC_EXTERNAL_EVALUATION_PACKAGE_CATALOG_ALIGNMENT_2026-06-20.md` | `Status: DISPATCHED_TO_CLAUDE` | DISPATCHED_TO_CLAUDE |
| Work order | this file | `Status: DISPATCHED_TO_CLAUDE` | DISPATCHED_TO_CLAUDE |
| Public-sync completion review | public-sync `docs/reviews/CVF_PUBLIC_EXTERNAL_EVALUATION_PACKAGE_CATALOG_ALIGNMENT_COMPLETION_2026-06-20.md` | pending worker return | BLOCKED |
| Public-sync commit/push | public-sync repo | pending Codex review | BLOCKED |
| Provider/live proof | N/A documentation-only | not applicable | N/A with reason |

## Claim Boundary

PECA-T1 may improve public reader orientation for external agents and user
developers. It does not prove new runtime behavior, live governance behavior,
provider behavior, direct interception, public release readiness, production
readiness, complete route coverage, or universal governed-coding control.
