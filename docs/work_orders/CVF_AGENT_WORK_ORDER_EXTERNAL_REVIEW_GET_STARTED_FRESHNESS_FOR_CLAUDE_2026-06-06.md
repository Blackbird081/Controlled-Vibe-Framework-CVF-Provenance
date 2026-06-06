# CVF Agent Work Order: External Review GET_STARTED Freshness For Claude

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-06

dispatchBaseHead: `c55697ac`

closureBaseHead: `c8a13184`

executionBaseHead: `c8a13184`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Dispatch Claude to implement the first bounded documentation repair derived from
the external-review gap analysis: refresh `docs/GET_STARTED.md` stale version
and skill-count claims, add a small public-facing glossary for common CVF terms,
and add one release-readiness freshness check so this specific drift does not
quietly recur.

This work order does not authorize runtime changes, UI changes, public-sync,
public push, governance-rule removal, durable persistence work, live/provider
proof, hosted readiness, production readiness, public readiness, cost or
performance claims, or autonomous mutation.

## Authority Chain

| Authority | Evidence | Status |
| --- | --- | --- |
| Operator instruction | 2026-06-06: "Bạn fix đi, và lên work order cho claude thi công" | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; current mode records LE1 as bounded-closed continuity | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` | ACCEPT |
| External-review gap analysis | `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` | ACCEPT |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ACCEPT |
| Finding-to-governance learning standard | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD_2026-05-29.md` | ACCEPT |

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope documentation, source-fidelity, markdown, and
governance-gate defects directly, then rerun the failed gate. Claude must
escalate before changing scope,
touching runtime/source code, changing public-sync, using secrets/live quota,
changing governance semantics, adding dependencies, modifying `.git/`, or
making public/hosted/production readiness claims.

## Agent Roles

| Role | Assignment |
| --- | --- |
| Orchestrator | Codex |
| Worker | Claude |
| Reviewer / committer | Codex or operator-designated reviewer after Claude returns completion evidence |
| Operator checkpoint | Required before public-sync, GC-018 expansion, durable persistence work, governance-rule removal, live/provider proof, or runtime implementation |

## Scope

Allowed scope:

- Update `docs/GET_STARTED.md` line 244 and line 395 stale skill-count text so
  they no longer disagree.
- Prefer a non-fragile phrase that points to the Skill Library README/current
  library source instead of introducing a new hardcoded count. If Claude keeps a
  number, it must cite `62 active skills` from the Skill Library README and use
  the same value consistently.
- Update `docs/GET_STARTED.md` footer version/date from stale `March 20, 2026 ·
  Version: 1.6.0` to a source-backed v4.0.0 GA wording.
- Add a concise "10 terms to know" glossary near the top of
  `docs/GET_STARTED.md` after the intro/workspace rule area. Definitions must
  be public-facing and plain-language, without weakening internal governance
  vocabulary.
- Add one release-readiness freshness check to
  `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` requiring
  `docs/GET_STARTED.md` version/skill-library wording to be checked against
  `CHANGELOG.md` and the Skill Library README before future public-facing
  sync/claim work.
- Produce a completion review under `docs/reviews/` with changed files,
  source evidence, gates run, and public export disposition.
- Session continuity sync after reviewer closure may update only
  `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and
  `AGENT_HANDOFF_V16_2026-06-06.md` to record the closed mode and next allowed
  move.

Forbidden scope:

- Runtime code, tests, UI implementation, API routes, storage adapters, durable
  persistence, `liveEmissionWired`, provider routing, live/provider proof,
  dependency files, lockfiles, public-sync clone, public push, marketplace
  claims, hosted readiness, production readiness, public readiness, cost or
  performance claims, governance-rule retirement, GC-018 expansion, or
  autonomous mutation.
- Editing internal governance vocabulary in CLAUDE.md, work orders, handoffs,
  standards, or runtime contracts.
- Rewriting `docs/CVF_CORE_KNOWLEDGE_BASE.md`; GAP 1 pointer-ification is a
  separate packet.

Risk ceiling: R1 documentation freshness/readability only.

## Required First Reads

| Required read | Reason | Status |
| --- | --- | --- |
| `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` | source gap packet and bounded priority order | READ |
| `docs/GET_STARTED.md` | target public-facing onboarding document | SOURCE_VERIFIED |
| `CHANGELOG.md` | current GA version source | SOURCE_VERIFIED |
| `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | current skill library count/domain source | SOURCE_VERIFIED |
| `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` | release-readiness checkpoint target | SOURCE_VERIFIED |
| `docs/reference/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md` | public-export disposition required for completion | READ |
| `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | completion-quality expectations | READ |

## Pre-Flight Checks

| Check | Evidence | Status |
| --- | --- | --- |
| Base head captured | `c55697ac` | PASS |
| Source Verification Block prepared | Source Verification Block below | PASS |
| Runtime/public-sync scope blocked | Forbidden scope and Claim Boundary | PASS |
| Completion review required | Scope and Evidence Requirements | PASS |

## Write Ownership

| Role | Owned paths |
| --- | --- |
| Claude worker | `docs/GET_STARTED.md`; `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md`; one completion review under `docs/reviews/` |
| Reviewer / committer | Final review, commit, session sync if required by reviewer gate |
| Forbidden | Runtime/source code, tests, dependency files, lockfiles, `.git/`, public-sync clone, session front doors unless reviewer explicitly owns closure sync |

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| External review packet identifies GET_STARTED version drift as GAP 3 | EXISTS | `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` | `## GAP 3 — Version Drift (GET_STARTED.md vs Repo State)` | `GAP 3` | external-review gap analysis packet | ACCEPT |
| External review packet recommends GAP 3 as first Claude work order candidate | EXISTS | `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` | `## Priority Order (by effort and risk)` | `GAP 3` | external-review gap analysis packet | ACCEPT |
| GET_STARTED contains stale skill text `141 reusable skills` | VALUE_SET | `docs/GET_STARTED.md` | line 244 | `Skill Library` | public onboarding document | ACCEPT |
| GET_STARTED contains inconsistent skill text `124 skills` | VALUE_SET | `docs/GET_STARTED.md` | line 395 | `Skill Library` | public onboarding document | ACCEPT |
| GET_STARTED contains stale footer date/version | VALUE_SET | `docs/GET_STARTED.md` | line 479 | `Last updated` | public onboarding document | ACCEPT |
| Current GA version is v4.0.0 | VALUE_SET | canonical-contract: `CHANGELOG.md` | lines 5-7 | `v4.0.0`; `GA_LOCAL_FIRST_APPROVED` | changelog | ACCEPT |
| Core KB also records v4.0.0 Runtime | VALUE_SET | `docs/CVF_CORE_KNOWLEDGE_BASE.md` | lines 10 and 27 | `v4.0.0 Runtime` | core knowledge base | ACCEPT |
| Skill Library README records active skill count and domain count | VALUE_SET | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | lines 16-17 | `Tổng Skills`; `Domains` | skill library README | ACCEPT |
| Skill Library README says active skills should stay few, strong, and non-coder friendly | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | line 8 | `Portfolio Note` | skill library README | ACCEPT |
| Release-readiness checkpoint exists and currently covers documentation truthfulness | EXISTS | `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` | lines 13-24 | `Documentation truthfulness` | release-readiness checkpoint | ACCEPT |
| Release-readiness checkpoint is not a runtime implementation surface | EXISTS | `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` | lines 101-124 | `Verdict`; `Issued` | release-readiness checkpoint | ACCEPT |

## New Doc-Only Content

| New content | Purpose | Runtime claim boundary |
| --- | --- | --- |
| GET_STARTED glossary for guard, tranche, wave, closure, receipt, GC-xxx, packet, lane, handoff, phase gate | public-facing onboarding readability | documentation only |
| Release-readiness freshness check | prevent recurrence of version/skill-library drift | documentation checklist only |
| Completion review for this work order | reviewer evidence and closure boundary | documentation only |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work-order instruction | Evidence expected |
| --- | --- | --- |
| GAP 3: repair GET_STARTED version drift | update stale date/version and skill-library wording | `git diff -- docs/GET_STARTED.md` plus source citations |
| GAP 2 Track A: public glossary candidate | add concise public-facing glossary only in GET_STARTED | reviewer checks wording does not weaken internal governance vocabulary |
| Prevent recurrence | add release-readiness freshness check | `git diff -- docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` |
| Keep scope bounded | forbid runtime/public-sync/GC-rule changes | completion review claim boundary |

## Execution Instructions For Claude

1. Capture `executionBaseHead` before editing.
2. Read every Required First Read and refresh line numbers if the file changed
   since this work order was authored.
3. Edit only Allowed Scope paths.
4. Keep the glossary concise; do not introduce marketing claims.
5. Do not hardcode a skill count unless using the Skill Library README value
   and explaining why a stable pointer is not better.
6. Run the relevant markdown/governance gates listed below.
7. Return a completion review with evidence, changed files, gates, residual
   risks, and `Public Export Disposition: DEFERRED_PRIVATE_ONLY` unless a
   separate public-sync batch is authorized.

## Execution Plan

| Step | Action | Owner | Evidence |
| --- | --- | --- | --- |
| 1 | Refresh first-read line references against current HEAD | Claude | source citations in completion review |
| 2 | Patch `docs/GET_STARTED.md` stale skill-library and version text | Claude | git diff and rg negative checks |
| 3 | Add concise public-facing glossary to `docs/GET_STARTED.md` | Claude | reviewer-visible added section |
| 4 | Add release-readiness freshness check | Claude | git diff for `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` |
| 5 | Write completion review with public export disposition and claim boundary | Claude | new `docs/reviews/` artifact |
| 6 | Return to reviewer without committing | Claude | `WORKER_MUST_NOT_COMMIT` respected |

## Evidence Requirements

Minimum commands before Claude returns completion:

```powershell
git diff --name-status <executionBaseHead> HEAD
python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD
```

If Claude only returns a patch without committing, replace `HEAD` with the
reviewer's staged/committed range during Codex review.

## Review Gate

Reviewer must confirm:

- changed files stay inside Write Ownership;
- source facts in the completion review match current files;
- no stale `141 reusable skills`, `124 skills`, `Version: 1.6.0`, or
  `March 20, 2026` claim remains in `docs/GET_STARTED.md` unless explicitly
  retained with source evidence;
- glossary is plain-language and public-facing, without changing internal
  governance semantics;
- required gates pass on the reviewer-owned range;
- public export disposition is `DEFERRED_PRIVATE_ONLY` unless separately
  authorized.

## Acceptance Criteria

| Criterion | Evidence |
| --- | --- |
| `docs/GET_STARTED.md` no longer contains conflicting `141` and `124` skill-library claims | `rg -n "141 reusable skills|124 skills" docs/GET_STARTED.md` returns no matches or an explicit retained-source explanation |
| `docs/GET_STARTED.md` no longer says `Version: 1.6.0` in the footer | `rg -n "Version: 1.6.0|March 20, 2026" docs/GET_STARTED.md` returns no matches or an explicit retained-source explanation |
| Glossary is public-facing and concise | reviewer read of added glossary |
| Release-readiness checkpoint includes freshness check | diff evidence |
| No runtime/public-sync claims are made | completion review claim boundary and git diff |

## Fail Conditions

Return to reviewer if any of the following occurs:

- Claude needs to touch runtime/source code, tests, dependencies, lockfiles,
  `.git/`, public-sync, or session front doors.
- The skill-count source changes or becomes ambiguous enough that a stable
  wording cannot be chosen.
- Any gate fails outside Allowed Scope.
- The completion review claims public, hosted, production, runtime, live-proof,
  cost, performance, or provider-readiness evidence.
- Claude cannot produce source-backed line references for changed claims.

## Closure Checklist

| Item | Required closure evidence |
| --- | --- |
| Changed files listed | `git diff --name-status <executionBaseHead> HEAD` or reviewer equivalent |
| Source facts refreshed | completion review source evidence table |
| Required gates run | command output or explicit reviewer rerun evidence |
| Worktree/commit boundary clear | Claude returns without committing; reviewer records final commit if accepted |
| Session sync disposition recorded | reviewer decides whether active session state/handoff sync is required |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_EXTERNAL_REVIEW_GET_STARTED_FRESHNESS_FOR_CLAUDE_2026-06-06.md` | `Status: CLOSED_PASS_BOUNDED`; `executionBaseHead: c8a13184`; reviewer-owned closure commit required | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EXTERNAL_REVIEW_GET_STARTED_FRESHNESS_COMPLETION_2026-06-06.md` | completion review records changed files, source evidence, gate evidence, public export disposition, and claim boundary | PASS |
| Roadmap state | `N/A with reason` | Audit-derived GAP 3 work order; no roadmap row was opened or changed | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no corpus scan, classification, readiness, or search/filter registry state changed in this documentation-only packet | BLOCKED with reason: out of scope for this documentation freshness repair |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no corpus scan, classification, readiness, or search/filter registry state changed in this documentation-only packet | BLOCKED with reason: out of scope for this documentation freshness repair |
| External evidence digest | `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` | repo-local audit packet is tracked; no external/local filesystem evidence is used as canonical source | PASS |
| System loop interlock | `N/A with reason` | Documentation freshness repair only; no runtime route, loop, learning, or mutation interlock changed | N/A with reason |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V16_2026-06-06.md` | reviewer-owned session sync required after material closure commit if next allowed move changes | PASS |

## Return-To-Orchestrator Conditions

| Return condition | Meaning |
| --- | --- |
| `IMPLEMENTATION_COMPLETE_PENDING_REVIEW` | Claude completed allowed scope and supplied evidence without committing |
| `BLOCKED_SCOPE_EXPANSION_REQUIRED` | Claude needs changes outside Allowed Scope |
| `BLOCKED_SOURCE_DRIFT` | cited source facts changed enough to invalidate this work order |
| `BLOCKED_GATE_SCOPE_EXPANSION_REQUIRED` | a required gate failed and remediation would exceed Allowed Scope |

## Operator Checkpoint

No operator checkpoint is needed for routine documentation edits inside this
work order. Operator checkpoint is required before public-sync, GC-018 expansion,
durable-persistence work, runtime/source changes, live/provider proof,
dependency changes, governance-rule removal, or public/hosted/production
readiness claims.

## Public Export Disposition

Disposition: `DEFERRED_PRIVATE_ONLY`

Reason: this is a private provenance work order for internal documentation
freshness repair. It does not authorize public-sync or a public catalog claim.

## Claim Boundary

This work order authorizes only bounded documentation repair by Claude under
reviewer control. It does not prove release-quality governance behavior, public
readiness, hosted readiness, production readiness, runtime behavior, provider
behavior, durable audit persistence, or governance-rule quality.
