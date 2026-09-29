# CVF Public Projection Pre-Push T1 Profile Owner And Gate Amendment 1 Source Verification

Memory class: FULL_RECORD

Status: ACCEPTED_FOR_DISPATCH

Date: 2026-08-12

docType: review

Batch ID: PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-1

## Purpose

Verify the source basis for amending PUBLIC-PROJECTION-PREPUSH-T1's
`BLOCKED_CONTRACT_CONTRADICTION` disposition: whether a disposable,
hash-verified candidate sandbox - materialized outside both the private Core
and the public-sync clone - can execute the full previously accepted
test/type/lint/build proof envelope without weakening any command and
without ever mutating the real public clone.

## Scope / Methodology

Read-only inspection of: the current T1 baseline, work order, and blocked
worker return; the accepted LPCI1-REF-T1A Amendment 2 completion evidence
that already proved an equivalent offline-junction build strategy against
the same public candidate; `package.json` and generator-script content from
the pinned public candidate; and the applicable dispatch, self-protection,
operation-trace, worker-return, and artifact-shape checker sources. No
secret access, no network action, no repository mutation.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `docType: review` structural group (Target/Source, Scope/Methodology, Findings/Position, Risk/Corrective Action, Decision); Core Guard Self-Protection required tokens; operation trace field list; bounded claim vocabulary; public disposition enum |
| gateRunPurpose | confirm source-backed amendment-dispatch shape before authoring the paired baseline and work order; not first discovery |
| claimBoundary | dispatch-authoring source verification only; no implementation, sandbox execution, or push/deploy claim |

## Authority And Base

| Item | Evidence | Disposition |
| --- | --- | --- |
| Operator | dispatcher/amendment-author role instruction and disposition source (`REVIEWER_CONFIRMED_BLOCKED_UNDER_CURRENT_CONTRACT`, amendable via disposable candidate-sandbox execution) | ACCEPT |
| Core dispatch base | `main@bbcb21acd753ec5c4f5a5c234da585e09febc562`, with the exact inherited five-path T1 dirty set present (four intent-to-added, zero staged content; one untracked), no other dirty path, and staged content zero - see the paired baseline's Preimage Authority Matrix for the pinned SHA-256 of each of the five paths | ACCEPT |
| Public candidate | `lpci1-ref-staging@021f8b852afc245a6383177dd69bf56caf488b02`, exact union 41, staged zero, `origin` = `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` | ACCEPT_READ_ONLY_EVIDENCE |
| T1 blocked worker return | `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md`; `Status: BLOCKED_WITH_REASON`; terminal disposition `BLOCKED_CONTRACT_CONTRADICTION` | ACCEPT_AS_PREDECESSOR |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T1's owner/policy/gate work is authorized and its worker-owned paths are fixed | VALUE_SET | `docs/baselines/CVF_GC018_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_2026-08-11.md` | Scope / Target / Owner Boundary | four stable owner paths | T1 GC-018 baseline | ACCEPT |
| T1 work order requires test/type/lint/build without weakening and fail-closed on read-only-vs-build conflict | VALUE_SET | `docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_2026-08-11.md` | Required Semantic Delta item 5; Acceptance Criteria AC-05 | test/type/lint/build command requirement | T1 work order | ACCEPT |
| Current T1 disposition is `BLOCKED_WITH_REASON` / `BLOCKED_CONTRACT_CONTRADICTION` because `cvf-web` `build` cannot run without mutating the tracked public-clone worktree | BEHAVIOR | `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md` | Findings / Position; Terminal Disposition | `prebuild` hook `fs.rmSync`/`fs.writeFileSync` evidence | T1 blocked worker return | ACCEPT |
| The eight-package dependency topology for the same public candidate (`lpci1-ref-staging@2103a38f..021f8b852`) is viable and a full build (121 static pages) succeeds when fully materialized; this proves topology/outcome only, not disposable-sandbox isolation, because those junctions were materialized directly inside the real public clone's worktree and restored afterward | EXECUTION_EVIDENCE | `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_2_COMPLETION_2026-08-11.md` | Findings / Position; Verification table | Production build PASS row | Amendment 2 independent reviewer closure | ACCEPT |
| The same junction methodology's full command/evidence trail confirms which local dependency store was used, that no package install occurred, and that the temporary entries were materialized in-place inside the public worktree and restored - not extracted into a disposable out-of-repository sandbox | EXECUTION_EVIDENCE | `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_2_WORKER_RETURN_2026-08-11.md` | Scope / Methodology step 10; Offline Dependency Link section | Offline Dependency Link | Amendment 2 accepted worker return | ACCEPT |
| The accepted candidate proof envelope's exact scope: Model Gateway 30 files/231 tests + TypeScript; focused cvf-web union-41 suite 15 files/218 tests; cvf-web TypeScript; scoped ESLint; production `next build --webpack` with 121 static pages | EXECUTION_EVIDENCE | `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_2_COMPLETION_2026-08-11.md` | Verification table | exact PASS rows per check | Amendment 2 accepted completion | ACCEPT |
| `cvf-web` declares exactly eight sibling package dependencies | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` (public candidate) | `dependencies` block | `cvf-model-gateway` | public candidate package manifest | ACCEPT |
| `cvf-model-gateway`'s own source resolves further siblings (`CVF_v1.7.3_RUNTIME_ADAPTER_HUB`, `CVF_v1.2.1_EXTERNAL_INTEGRATION`, `CVF_GUARD_CONTRACT`) via relative imports, which only resolve correctly when `CVF_MODEL_GATEWAY` itself sits at its real `EXTENSIONS/` sibling position rather than as a flattened copy inside `cvf-web/node_modules/` | BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (public candidate) | import statements | `CVF_v1.7.3_RUNTIME_ADAPTER_HUB` | Model Gateway package source | ACCEPT |
| The rejected T1 worker return's `cvf_web_check`/`cvf_web_lint` GATE failures were caused by this same incomplete-topology pattern (a non-junctioned, separately-installed `cvf-model-gateway` copy inside `cvf-web/node_modules/`), not a genuine public-owned source defect | BEHAVIOR | `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md` | Findings / Position, item 2 | Command Evidence table | T1 blocked worker return | ACCEPT |
| `cvf-web`'s `prebuild` lifecycle hook runs before `build` and deletes/recreates `.next` plus the two generator scripts | BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` (public candidate) | `scripts.prebuild` | `prebuild` | public candidate package manifest | ACCEPT |
| The skill-index generator also writes generated output directly into tracked source paths | BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` (public candidate) | lines 691 and 712 | `writeFileSync` | public candidate generator script | ACCEPT |
| The registered skill-index generator is bounded in size and was read in full before authoring sandbox execution instructions | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` (public candidate) | whole file | 725 lines | public candidate generator script | ACCEPT |

## Current Runtime Freshness Verification

Re-verified read-only at dispatch time: Core `HEAD` is
`bbcb21acd753ec5c4f5a5c234da585e09febc562` with the exact inherited
five-path T1 dirty set present, zero staged content, and no other dirty
path - Core is not claimed clean. Public-sync clone is clean at
`021f8b852afc245a6383177dd69bf56caf488b02` on branch `lpci1-ref-staging`
with `origin` = `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`.
The five existing T1 worker-owned paths remain exactly as the blocked
worker return left them (four owner artifacts intent-to-added with zero
staged content, one untracked worker return), each matching its pinned
SHA-256 in the paired baseline's Preimage Authority Matrix; none were
read-modified by this source verification.

## Exact Amendment Decision

Amend the T1 profile so that mutating package commands (test/type/lint/build)
execute only inside a disposable candidate sandbox materialized outside both
repository roots from the exact `authorizedCandidateHead` commit via a
hash-verifiable read-only extraction (`git archive` or equivalent), with
dependency isolation achieved by junctioning/copying/linking only from
existing local dependency stores (no install, no network), fail-closed on
any sandbox-creation, materialization-mismatch, dependency-isolation,
missing-executable, timeout, nonzero-exit, or cleanup-failure condition, and
fail-closed - never self-repair - on any observed before/after change to the
real public clone. The verification profile must reproduce, not substitute
for, the exact Pinned Command Manifest recorded in the paired baseline
(Model Gateway full suite and TypeScript; the exact 15-file cvf-web union-41
`vitest` invocation; cvf-web TypeScript under the complete eight-package
offline dependency topology; ESLint scoped to exactly
`src/app/api/lpci/query/route.governance.test.ts`; the three-step build
sequence). Amendment worker preflight must additionally require exact
preimage matching against the paired baseline's Preimage Authority Matrix
before any implementation-authoring edit; any mismatch is
`BLOCKED_PREIMAGE_MISMATCH`.

Amendment work stays inside the same five T1 worker-owned paths unless a
checker requires otherwise:

- `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md`
- `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json`
- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/test_run_public_projection_pre_push_gate.py`
- `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md`

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`PUBLIC-PROJECTION-PREPUSH-T1 Amendment 1 sandbox verification dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Findings / Position

The `BLOCKED_CONTRACT_CONTRADICTION` recorded against the real public clone
is correct and is not overturned: `cvf-web`'s `build`/lifecycle hooks
genuinely cannot run read-only against that specific worktree. The
contradiction is amendable, not permanent, because the same package graph
was already proven buildable offline, without network access and without
any tracked-source delta, against a fully-materialized dependency topology
for the identical public candidate commit (Amendment 2). That prior proof
used temporary junctions created directly inside the real public clone's
own worktree, then restored - it establishes only that the dependency
topology and expected test/build outcomes are achievable, not that
disposable, out-of-repository sandbox isolation works or that zero
transient public-clone mutation is achievable by that same method. The
missing piece in the rejected T1 implementation was execution location:
mutating commands were pointed at the real public clone instead of at a
disposable, hash-verified copy of it materialized outside both repository
roots. This amendment must freshly prove that out-of-repository sandbox
isolation, not merely reuse Amendment 2's in-place-junction proof as if it
were equivalent.

## Risk / Corrective Action

Primary risk: a sandbox implementation that silently degrades into either
(a) weakening/skipping a required command category to avoid the
contradiction, or (b) achieving isolation from the real clone in the common
case while still permitting a path-escape or dependency-link-escape under
adversarial input. The paired work order requires explicit fail-closed
tests for both failure classes, an explicit before/after invariant capture
of the real public clone (HEAD, branch, full status including untracked,
staged and unstaged diff) around the entire sandboxed run, and an explicit
prohibition on the runner ever cleaning or repairing the public clone
itself. A secondary, already-realized risk is recorded as a governance
lesson rather than re-litigated: the prior worker's direct `cvf-web` test
run created and then manually removed an untracked `.cvf/runtime/`
directory in the real public clone; the paired baseline records this as an
unauthorized transient public-clone mutation, now cleaned, and the
successful cleanup is explicitly not accepted as proof the original action
was read-only.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/amendment author |
| Provider or surface | local private Core plus read-only public-sync clone |
| Session or invocation | `public-projection-prepush-t1-amendment-1-source-verification-20260812` |
| Working directory | Core plus public-sync clone |
| Command or tool surface | local file reads, Git read-only inspection (`status`, `rev-parse`, `branch`, `remote`), ADIF resolver, authority authoring |
| Target paths | exact three Amendment 1 authority paths |
| Allowed scope source | dispatcher/amendment-author role instruction naming `REVIEWER_CONFIRMED_BLOCKED_UNDER_CURRENT_CONTRACT` and the disposable-sandbox amendment decision |
| Before status evidence | Core `HEAD` at `bbcb21acd753ec5c4f5a5c234da585e09febc562` with exact inherited five-path T1 dirty set present, zero staged, no other dirty path; public clean at `021f8b852afc245a6383177dd69bf56caf488b02` on `lpci1-ref-staging` |
| After status evidence | three authority files pending; five existing T1 worker-owned paths unmodified; public clone unmodified |
| Diff evidence | Core `git status --short` partitions into exactly three sets: (1) inherited five-path T1 implementation set (four intent-to-added, one untracked, unchanged from before this dispatch) - see Preimage Authority Matrix; (2) new three-path Amendment 1 authority-authoring set (this source verification, the paired baseline, the paired work order), all untracked; (3) unexpected paths: none. Public-sync `git status --short` must remain empty |
| Approval boundary | Amendment 1 dispatch-authoring only; no implementation |
| Claim boundary | no sandbox creation, no package execution, no commit, no push, no deploy, no provider/store, no secret, no network, no public-clone mutation |
| Agent type | dispatcher/amendment author |
| Invocation ID | `public-projection-prepush-t1-amendment-1-source-verification-20260812` |
| Expected manifest | source verification, baseline, work order (this three-path set) |
| Actual changed set | this three-path set only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: three new authority files only; no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local dispatch-authoring source verification for a disposable-sandbox amendment to T1 |
| claimDisposition | CLAIM_REJECTED: no sandbox, package-command, or repaired-candidate behavior is claimed yet |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no execution receipt is produced by dispatch authoring |
| actionEvidence | ACTION_EVIDENCE_PRESENT: read-only Git state checks, ADIF resolver run, direct source/package-manifest/generator-script inspection |
| invocationBoundary | zero sandbox creation, zero package execution, zero mutation of either repository, zero commit |
| interceptionBoundary | no IDE, provider, browser, network, or remote mutation claim |
| claimLanguage | accepted for Amendment 1 dispatch; implementation remains a separate no-commit worker action |
| forbiddenExpansion | sandbox execution, package install, network fetch, push, deploy, secrets, provider/store, production, public-clone mutation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dispatch-authoring source verification.
No public artifact is created and the public clone is inspected read-only
only.

## Claim Boundary

This source verification establishes the evidentiary basis for amending
T1's disposition via disposable-sandbox execution. It proves no sandbox
was created, no package command was executed, and neither repository was
mutated. It authorizes drafting the paired baseline and work order only; it
does not authorize implementation, commit, push, deploy, provider/store
action, secret access, network installs, or any public-clone mutation.
