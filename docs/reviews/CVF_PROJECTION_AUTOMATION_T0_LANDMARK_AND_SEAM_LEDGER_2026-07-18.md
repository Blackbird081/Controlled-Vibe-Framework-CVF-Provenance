# CVF Projection Automation T0 Landmark And Seam Ledger

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_BOUNDED

docType: review

Date: 2026-07-18

Batch ID: CVF-PROJECTION-AUTO-T0

Produced for work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_PROJECTION_AUTOMATION_T0_LANDMARK_AND_SEAM_AUDIT_2026-07-18.md`

executionBaseHead: `7192f1112`

## Purpose

Build a terminal landmark and seam ledger that a later T1 tranche can use to
implement a safe dry-run projection mapper across the private provenance
repository, the public-sync clone, and the `cvf-web` package, without
guessing roots, allowlists, remote rules, or `cvf-web` module owners.

## Target / Source

Target: the private provenance repository root, the public-sync clone root,
and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`.

Source read directly for this ledger:

- `scripts/cvf-public-sync.ps1` (public-sync allowlist and seam owner)
- `scripts/update_cvf_workspace_public_core.ps1` (workspace updater pattern
  owner)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts`
  (cvf-web runtime-module registry owner)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/README.md`
- `docs/reviews/CVF_SOT3_CVF_PROJ_T4_COMPLETION_REVIEW_2026-07-18.md` (paired
  baseline: private projection closure)
- `docs/reviews/CVF_WEB_INHERITANCE_T5_COMPLETION_REVIEW_2026-07-18.md`
  (paired baseline: cvf-web inheritance closure)
- `docs/reviews/CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_LEDGER_2026-07-18.md`
  (existing cvf-web registry/page seam evidence)
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_agent_handoff_boundary.py`
- `governance/compat/check_worker_return_quality_gate.py`
- `governance/compat/check_public_export_disposition.py`
- `governance/compat/check_markdown_structural_completeness.py`
- `governance/compat/check_governed_file_size.py`
- direct `git status --short`, `git rev-parse`, and `git remote -v` in the
  private provenance root and the public-sync clone root

## Scope / Methodology

1. Confirmed a clean provenance worktree at `executionBaseHead` before any
   read.
2. Read both prerequisite completion reviews named in the work order's
   Dependency Release Evidence table and reconfirmed their commit hashes and
   dispositions directly against `git log`.
3. Read `scripts/cvf-public-sync.ps1` in full to recompute the public-sync
   allowlist, denylist, mapped-file exports, dry-run/no-commit/no-push flags,
   and root/remote validation logic directly from source rather than from
   prior memory.
4. Read `scripts/update_cvf_workspace_public_core.ps1` to recompute the
   workspace updater's path-escape guard (`Assert-PathInsideWorkspace`) and
   overlay-file copy pattern as the reusable safe-copy seam.
5. Read `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts`
   in full to enumerate the fixed `MODULES` registry array, its module-health
   probe (`moduleHealth`), and its declared `boundary` string as the cvf-web
   registry seam.
6. Ran `git status --short`, `git rev-parse --short HEAD`, and
   `git remote -v` in both the private provenance root and the public-sync
   clone root to capture roots, remotes, and dirty/clean status directly.
7. Read the six named checker sources to extract literal headings, markers,
   and enum tokens this ledger and the paired worker return must satisfy.
8. Built the terminal mapping rows below with a `MECHANICAL`,
   `SEMANTIC_REVIEW`, or `NOT_APPLICABLE_WITH_REASON` disposition per row.
9. Defined proposed T1 manifest and receipt fields as explicit doc-only new
   fields, not present runtime claims.
10. Defined fail-closed negative cases for missing root, wrong remote, dirty
    target, and path escape, all cited to source-proven guard logic already
    present in `cvf-public-sync.ps1` or `update_cvf_workspace_public_core.ps1`.

## Findings / Position

### Landmark Commits/Artifacts

| Landmark | Artifact | Commit | Disposition |
|---|---|---|---|
| private SOT3 CVF projection closure | `docs/reviews/CVF_SOT3_CVF_PROJ_T4_COMPLETION_REVIEW_2026-07-18.md` | `9f7c92663` | PASS (reconfirmed: `Status: REVIEWER_ACCEPTED_BOUNDED_ROADMAP_CLOSED`, disposition `SOT3-CVF-PROJ-T4-R1 is accepted bounded... roadmap is CLOSED_PASS_BOUNDED`) |
| cvf-web inheritance closure | `docs/reviews/CVF_WEB_INHERITANCE_T5_COMPLETION_REVIEW_2026-07-18.md` | `64ec0f672` | PASS (reconfirmed: `Status: REVIEWER_ACCEPTED_WITH_MAINTENANCE`, disposition `CVF Web capability inheritance and operator projection roadmap is CLOSED_PASS_BOUNDED`) |
| T0 dispatch of this audit | `docs/work_orders/CVF_AGENT_WORK_ORDER_PROJECTION_AUTOMATION_T0_LANDMARK_AND_SEAM_AUDIT_2026-07-18.md` | `7192f1112` | PASS (matches recorded `executionBaseHead` for this worker) |
| private-to-Web capability seam evidence | `docs/reviews/CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_LEDGER_2026-07-18.md` | part of `277b979a7`..`90aa165c6` range (T0 dispatch/closure) | PASS (source for the `runtime-modules.ts` owner identity used below) |

### Provenance/Public-Sync/cvf-web Roots And Remote/Status Evidence

| Root | Path | `git rev-parse --short HEAD` | `git status --short` | `git remote -v` (origin) |
|---|---|---|---|---|
| provenance (this repository) | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` | `7192f1112` | clean (empty output) | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git` |
| public-sync clone | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync` | `141031c57` | clean (empty output) | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` |
| cvf-web package root | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` (inside provenance root; no independent git root) | N/A_WITH_REASON: shares provenance root history | N/A_WITH_REASON: shares provenance root working tree | N/A_WITH_REASON: not an independent git repository |

`cvf-web/package.json` line 3 records `"version": "1.7.0"`, matching the
version accepted by the cvf-web inheritance T5 closure cited above. This is a
direct package-metadata read, not a git-remote fact.

The provenance-root remote is a **different** GitHub repository
(`-Provenance` suffix) than the public-sync clone's remote
(`Controlled-Vibe-Framework-CVF.git`, no suffix). A T1 mapper must validate
both remotes independently before any push and must never push the
provenance root to the public-sync remote or vice versa.

### Public-Sync Allowlist, Mapped-File, Dry-Run, No-Commit, And No-Push Seams

Source: `scripts/cvf-public-sync.ps1`.

| Seam | Mechanism | Source anchor |
|---|---|---|
| root/remote validation | script aborts if `$PUBLIC_SYNC_ROOT` does not exist or if `git -C $PUBLIC_SYNC_ROOT remote get-url origin` does not equal the hardcoded `$PUBLIC_REMOTE` | lines 229-247 |
| allowlist trees | `$ALLOWED_TREES` (`EXTENSIONS`, `ECOSYSTEM`, `governance`, `v1.0`, `v1.1`, `tools`, `.github`, `App onboarding`) | lines 37-46 |
| allowlist root files | `$ALLOWED_ROOT_FILES` (13 named files, e.g. `README.md`, `PROVENANCE.md`) | lines 49-65 |
| allowlist scripts | `$ALLOWED_SCRIPT_FILES` (15 named public-safe scripts; explicitly excludes the provenance-only sync/push scripts) | lines 69-86 |
| allowlist docs sub-paths | `$ALLOWED_DOCS_PATHS`; explicitly excludes `docs/baselines`, `docs/reviews`, `docs/roadmaps` by omission | lines 131-141 |
| mapped exports | `$MAPPED_FILES` (`CVF_PUBLIC_CORE_AGENTS.md` -> `AGENTS.md`; `CVF_PUBLIC_CORE_CONTINUATION.md` -> `AGENT_HANDOFF.md`; `install_cvf_workspace_root_wrappers_public.ps1` -> `install_cvf_workspace_root_wrappers.ps1`) | lines 95-108 |
| denylist (defense-in-depth) | `$DENY_PATTERNS` regex list; explicitly matches `^AGENT_HANDOFF`, `^docs[/\\]baselines[/\\]`, `^docs[/\\]reviews[/\\]`, `^docs[/\\]roadmaps[/\\]`, both provenance-only sync scripts, `.env` variants, build/cache directories | lines 144-167 |
| dry-run flag | `-DryRun` switch prints the allowlist and mapped exports, then exits before any copy | lines 268-282 |
| no-commit flag | `-NoCommit` switch copies files into the public-sync worktree, then exits before `git add`/`git commit` | lines 334-338 |
| no-push flag | `-NoPush` switch commits locally but skips `git push origin main` | lines 365-373 |
| workspace-kit-only flag | `-WorkspaceKitOnly` narrows the allowlist to `$WORKSPACE_KIT_FILES` only | lines 262-264 |

A future T1 dry-run mapper must use a shared read-only policy source extracted
from, or mechanically verified against, `Get-AllowedFiles`/`Test-Denied`.
It must not dot-source or invoke the mutating sync script merely to obtain that
policy. Focused tests must prove parity so a second allowlist cannot drift.

### Workspace Updater Patterns Worth Reusing

Source: `scripts/update_cvf_workspace_public_core.ps1`.

| Pattern | Mechanism | Source anchor |
|---|---|---|
| path-escape guard | `Assert-PathInsideWorkspace` resolves both the candidate path and the workspace root to absolute paths and throws if the candidate does not start with the workspace root prefix (case-insensitive) | lines 59-66 |
| overlay copy pattern | `Copy-OverlayFiles` iterates a fixed `$overlayFiles` list, skips any source file that does not exist, creates the destination directory if missing, then force-copies | lines 68-82 |
| required-file manifest | `$requiredPublicCoreFiles` is a fixed, named list used to validate the public core clone before any workspace reconciliation | lines 14-29 |
| public remote pin | `$publicRemote` is hardcoded to the same public GitHub URL used by `cvf-public-sync.ps1`'s `$PUBLIC_REMOTE`, giving the workspace updater and the public-sync script one shared remote identity to validate against | line 13 (cross-referenced against `cvf-public-sync.ps1` line 34) |

`Assert-PathInsideWorkspace` is the single most reusable primitive for a T1
mapper's "path escape" negative case (see Fail-Closed Negative Cases below):
it is already a source-proven, throwing guard, not a proposed new control.

### cvf-web Package, Registry, Operator-Page, And Test Seams

Source: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts`,
cross-checked against the accepted
`CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_LEDGER_2026-07-18.md` (WEB-04 row).

| Seam | Mechanism | Source anchor |
|---|---|---|
| registry owner | fixed `MODULES: ModuleDefinition[]` array; 13 entries as of this read (`cvf-web`, `guard-contract`, `phase-governance-runtime`, `control-plane-foundation`, `execution-plane-foundation`, `governance-expansion-foundation`, `learning-plane-foundation`, `model-gateway`, `policy-engine`, `trust-sandbox`, `cvf-refinery`, `cvf-truth-kernel`, `cvf-truth-flow`) | `runtime-modules.ts` lines 60-191 |
| module-health probe | `moduleHealth()` resolves `repoRoot`/`repoPath`, checks `existsSync`, and reads `package.json` for `name`/`version`/`scripts`; returns `healthStatus` of `available`/`partial`/`missing` | lines 201-231 |
| registry report shape | `getRuntimeModuleRegistry()` maps each `ModuleDefinition` through `moduleHealth`, computes a `summarize()` roll-up, and returns a fixed `boundary` string: `"Read-only module registry. It does not trigger module actions or widen Web authority."` | lines 257-271 |
| operator page owner | `src/app/(dashboard)/governance/runtime-modules/page.tsx` (identity confirmed by the accepted WEB-04 row; not independently re-read line-by-line by this T0 audit, since the existing accepted ledger already source-cites it) | cited row: `CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_LEDGER_2026-07-18.md` row WEB-04 |
| package version anchor | `cvf-web/package.json` line 3 | `"version": "1.7.0"` (direct read, this ledger) |
| test seam | 4 dedicated SOT3 test files named in the accepted WEB-02 row (`route.sot3-activation-failure-recovery.test.ts`, `route.sot3-activation.alibaba.live.test.ts`, `sot3-activation-evidence-store.test.ts`, `sot3-knowledge-adapter.test.ts`) | cited row: `CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_LEDGER_2026-07-18.md` row WEB-02 |

The registry array has zero entries dedicated to a "projection automation"
or "mapper" module as of this read. Any T1 mapper that adds a Web-visible
status surface would need a new `ModuleDefinition` entry following the exact
existing field shape (`id`, `name`, `repoPath`, `runtimeClass`,
`webExposureState`, `exposedActions`, `evidenceOwner`, `notes`), not a
parallel registry.

### Terminal Mapping Rows

| # | Candidate mapper action | Disposition | Reason / source |
|---|---|---|---|
| M-01 | Read provenance root file inventory against the public-sync allowlist trees/files/mapped-exports | `MECHANICAL` | pure recomputation of `Get-AllowedFiles`/`Test-Denied` logic already in `cvf-public-sync.ps1` lines 179-224; no judgment required beyond string/regex matching |
| M-02 | Detect a file present in provenance but absent from public-sync that also matches the allowlist | `MECHANICAL` | set-difference of two file lists; deterministic |
| M-03 | Decide whether an allowlisted file's *content* diff (not just presence) is safe to project | `SEMANTIC_REVIEW` | content correctness (e.g., whether a doc still reads truthfully once exported) is not decidable from a file-presence diff alone; requires a human/reviewer read, consistent with the existing `DEFERRED_PRIVATE_ONLY` posture on every closed T4/T5 review cited above |
| M-04 | Detect `docs/baselines`, `docs/reviews`, `docs/roadmaps`, or `AGENT_HANDOFF*` paths present in a proposed export set | `MECHANICAL` | exact regex match against `$DENY_PATTERNS` lines 144-167; a T1 mapper must fail closed on any such match |
| M-05 | Detect cvf-web `runtime-modules.ts` entries that reference a package absent from `cvf-web/package.json` dependencies | `MECHANICAL` | deterministic cross-reference of two structured sources (registry array vs. package.json dependency keys); already performed manually in the cited WEB-01 row |
| M-06 | Decide whether a cvf-web registry gap (e.g., missing SOT3 entries) should be silently auto-repaired by a mapper | `NOT_APPLICABLE_WITH_REASON`: this T0 ledger authorizes no implementation; any repair remains a future source-verified, reviewer-accepted tranche, not an automated mapper action, per the accepted WEB-04 row's own framing ("scoped T1 registry-truth correction, not a new UI build") |
| M-07 | Validate that the public-sync clone's remote equals the hardcoded `$PUBLIC_REMOTE` before any copy | `MECHANICAL` | exact string comparison, `cvf-public-sync.ps1` lines 241-247 |
| M-08 | Validate that a target write path stays inside the intended root before any file operation | `MECHANICAL` | reuse of `Assert-PathInsideWorkspace`'s prefix-check logic, `update_cvf_workspace_public_core.ps1` lines 59-66 |
| M-09 | Decide whether a new capability family (not yet audited) should be added to a future landmark ledger | `SEMANTIC_REVIEW` | requires operator/dispatcher scoping judgment, consistent with every closed roadmap's "fresh GC-018/source-verified work order" boundary cited in the T4 and T5 completion reviews |
| M-10 | Produce a dry-run report of proposed copy/skip/deny actions without writing any file | `MECHANICAL` | direct analogue of the existing `-DryRun` switch behavior, lines 268-282 |

### Proposed T1 Manifest And Receipt Fields (Doc-Only New Fields)

These fields do not exist in any current runtime, script, or schema. They are
proposed here only as a starting contract for a future T1 dispatch packet and
must be source-verified against whatever T1 actually implements before use.

Proposed T1 manifest fields:

- `mapperRunId` - opaque identifier for one dry-run mapper invocation.
- `sourceRoot` - one of `provenance`, `public-sync`, `cvf-web`.
- `targetRoot` - one of `provenance`, `public-sync`, `cvf-web`.
- `candidateAction` - one of `COPY`, `SKIP_DENIED`, `SKIP_UNCHANGED`,
  `SKIP_NOT_ALLOWLISTED`, `FLAG_SEMANTIC_REVIEW`.
- `matchedAllowlistRule` - the specific allowlist tree, root-file, or
  mapped-export entry a candidate path matched, or `NONE`.
- `matchedDenyPattern` - the specific `$DENY_PATTERNS` regex a candidate path
  matched, or `NONE`.

Proposed T1 receipt fields:

- `receiptId` - opaque identifier for one completed dry-run report.
- `rootsValidated` - boolean-equivalent enum (`PASS`/`FAIL`) per root,
  recomputed from `git remote -v` and `git status --short` at receipt time.
- `pathEscapeChecksRun` - count of `Assert-PathInsideWorkspace`-equivalent
  checks performed.
- `deniedPathCount` - count of candidates rejected by `matchedDenyPattern`.
- `semanticReviewFlagCount` - count of candidates routed to
  `FLAG_SEMANTIC_REVIEW`.
- `noWriteConfirmation` - fixed literal confirming the dry-run receipt itself
  performed zero filesystem writes outside its own receipt output path.

`docOnlyNewFields: true` for both lists above. None of these field names
exist in `cvf-public-sync.ps1`, `update_cvf_workspace_public_core.ps1`, or
`runtime-modules.ts` as of this read.

### Fail-Closed Negative Cases

| Case | Required behavior | Source-proven basis |
|---|---|---|
| missing root | abort before any file read/write if `$PUBLIC_SYNC_ROOT` (or an equivalent T1 target root) does not exist | `cvf-public-sync.ps1` lines 234-238, `[ABORT]` and `exit 1` |
| wrong remote | abort before any file read/write if the target root's `origin` remote does not equal the expected hardcoded remote for that root | `cvf-public-sync.ps1` lines 240-247; note the provenance root and public-sync root have two *different* expected remotes (see Roots table above), so a T1 mapper must check the correct expected value per root, not one shared constant |
| dirty target | a T1 mapper must record `git status --short` for the target root before any write and must not silently overwrite untracked or modified files; the reviewed scripts do not currently auto-stash or auto-discard, so a T1 implementation must add an explicit abort-or-confirm step rather than assuming git-add-all safety | inferred requirement; no existing script in this ledger's source set performs an automated dirty-target check, so this is a gap a T1 packet must close, not an existing mechanical seam |
| path escape | abort before any filesystem write if the resolved absolute destination path does not start with the intended root's absolute path prefix | `update_cvf_workspace_public_core.ps1` lines 59-66, `Assert-PathInsideWorkspace` throws |

The "dirty target" case is the one negative case in this table without a
directly reusable existing guard; a T1 packet must design and source-verify
that check rather than assuming an existing script already covers it.

## Risk / Corrective Action

| Risk | Disposition | Control |
|---|---|---|
| a future mapper treats file presence as semantic correctness | rejected | rows M-03 and M-09 above are explicitly routed to `SEMANTIC_REVIEW`, not `MECHANICAL` |
| a future mapper invents a second allowlist that drifts from `cvf-public-sync.ps1` | flagged | T1 must extract a shared read-only policy source or prove mechanical parity under focused tests; invoking the mutating sync flow for audit is forbidden |
| a future mapper silently repairs the cvf-web registry without a fresh dispatch | rejected | row M-06 is `NOT_APPLICABLE_WITH_REASON`; this ledger authorizes no implementation |
| dirty-target overwrite during a future mapper's first write pass | flagged (gap, not yet controlled) | recorded as the one negative case without an existing reusable guard; a T1 packet must close it before any write-capable mapper ships |
| this ledger's terminal rows are mistaken for T1 authorization | rejected | Claim Boundary below states this ledger performs no implementation |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `## Target`; `## Source`; `## Scope`; `## Methodology`; `## Findings`; `## Risk`; `## Public Export Disposition`; `REQUIRED_HEADINGS`; `REQUIRED_BLOCK_FIELDS`; review docType five-group set (target/source, scope/methodology, findings/position, risk/corrective action, decision/recommendation/disposition) |
| gateRunPurpose | confirmation and evidence for this landmark/seam ledger's own structural shape, read directly from checker source before drafting |
| claimBoundary | structural read-ahead for this ledger only; the paired worker-return packet carries its own separate read-ahead block |

## Epistemic Process Block

### Expected Result / Prediction

Given that both prerequisite roadmaps (private SOT3 CVF projection and cvf-web
inheritance) closed bounded on 2026-07-18 with an explicit "next lane is a
read-only-first automation roadmap" pointer in the T4 completion review, this
audit expected to find: (a) a working, source-proven public-sync allowlist
script with dry-run/no-commit/no-push flags already present; (b) a reusable
path-escape guard already present in the workspace updater; and (c) a cvf-web
runtime-module registry with a known, source-cited gap (missing SOT3 entries)
rather than a clean registry.

### Evidence Comparison

Direct reads confirmed all three predictions. `cvf-public-sync.ps1` already
implements `-DryRun`, `-NoCommit`, and `-NoPush` flags plus a root/remote
abort check. `update_cvf_workspace_public_core.ps1` already implements
`Assert-PathInsideWorkspace` as a throwing prefix-check guard.
`runtime-modules.ts`'s `MODULES` array has zero entries for `cvf-refinery`,
`cvf-truth-kernel`, or `cvf-truth-flow`, matching the accepted WEB-04 row's
prior finding exactly. One prediction gap was found during this audit: no
reviewed script currently implements an automated "dirty target" abort check,
which is recorded as an open negative case above rather than a false
prediction.

### Contradiction Or Gap Disposition

No contradiction against the two paired baseline closures. The one gap (no
existing dirty-target guard) is recorded in the Fail-Closed Negative Cases
table as a control a future T1 packet must add, not as a defect in the
current closed roadmaps.

### Claim Update

The projection landmark and seam surface is now terminal and source-cited for
T1 planning: roots, remotes, status, the public-sync allowlist/denylist/
mapped-export/dry-run/no-commit/no-push seams, the workspace updater's
path-escape and overlay-copy patterns, and the cvf-web registry/page/test
seams are all recorded above with exact source anchors. Whether any of this
becomes an actual T1 implementation remains a separate, future, dispatcher-
and reviewer-owned decision.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this ledger is a private provenance T0 audit output. No public-safe
export or public-sync action is authorized or performed by this artifact.

## Claim Boundary

This ledger is a read-only source audit and terminal seam map. It does not
implement, run, or dry-run the mapper described in its proposed T1 fields; it
does not mutate `scripts/cvf-public-sync.ps1`,
`scripts/update_cvf_workspace_public_core.ps1`,
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`, the public-sync clone, or any
other source path; it performs no commit, push, or provider call. All
`MECHANICAL` dispositions above describe what a future T1 implementation
could deterministically automate, not work already performed. All proposed
T1 manifest and receipt fields are explicitly doc-only and require fresh
source verification at T1 dispatch time.

Reviewer clarification: the absolute root paths recorded above are evidence
from this operator workstation, not portable configuration. T1 must accept or
discover roots as validated parameters, verify each root's distinct expected
remote, and remain dry-run-only. Any write/apply mode remains reserved to T2
or a later separately authorized tranche.
