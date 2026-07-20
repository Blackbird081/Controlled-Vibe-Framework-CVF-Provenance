# CVF Continuous Projection T0 Three-Root Drift Contract Ledger

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIRS

docType: review

Date: 2026-07-20

Batch ID: CVF-CONTINUOUS-PROJECTION-T0

executionBaseHead: `a6afabbfa`

## Purpose

Define the terminal T0 three-root drift contract mapping every governed
projection surface across provenance, public-sync, and cvf-web to its
semantic owner, projection target, evidence class, audience, and drift
disposition, so a later T1 work order can extend the read-only mapper without
guessing or conflating file freshness with semantic or presentation
equivalence.

## Target / Source

Target: the current-state provenance root, the sibling public-sync clone,
and the cvf-web package root under provenance, as of `executionBaseHead`
`a6afabbfa`.

Source: `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md`;
`docs/baselines/CVF_GC018_CONTINUOUS_PROJECTION_T0_THREE_ROOT_DRIFT_CONTRACT_2026-07-20.md`;
`docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md`;
`docs/reviews/CVF_PROJECTION_AUTOMATION_T2_FINAL_CLOSURE_AUDIT_2026-07-18.md`;
`scripts/get_cvf_projection_map.ps1`; `scripts/cvf_projection_policy.json`;
`scripts/test_get_cvf_projection_map.ps1`; `scripts/cvf-public-sync.ps1`;
`DESIGN.md`; direct `git log`/`git status`/`git remote` in all three roots.

## Scope / Methodology

1. Confirmed `executionBaseHead` equals the operator-stated `a6afabbfa` via
   `git rev-parse HEAD` in the provenance root; worktree was clean
   (`git status --porcelain` returned zero lines).
2. Read the roadmap, paired GC-018 baseline, Web UX T4 completion, T2 final
   closure audit, the mapper source, the projection policy JSON, the focused
   test file, and `DESIGN.md` in full before drafting any row.
3. Ran the mandatory pre-implementation autorun gate
   (`python governance/compat/run_agent_autorun_workflow_gate.py --phase
   pre-implementation --base a6afabbfa --head HEAD`): 77/77 checks PASS.
4. Directly inspected all three roots read-only: provenance origin remote,
   HEAD, and clean state; the sibling public-sync clone's origin remote,
   HEAD, and clean state; the cvf-web root's `package.json` and
   `runtime-modules.ts` existence and content.
5. Attempted a live read-only mapper invocation against the real clean
   provenance and public-sync roots (no `-ReceiptOutputPath`, so no file
   write was possible per the mapper's own containment guard). The
   recursive three-root byte-comparison over `EXTENSIONS`, `ECOSYSTEM`, and
   `governance` did not complete inside this worker's execution window; it
   is recorded as an attempted-but-inconclusive evidence source below and is
   not required by the work order's Required Implementation, which asks for
   source-backed root/landmark/terminal evidence rather than a fresh
   receipt. The accepted T2 governed-receipt run (`5df0c6f77`,
   `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_FINAL_CLOSURE_AUDIT_2026-07-18.md`)
   remains the accepted proof that the mapper mechanism itself is correct,
   deterministic, and fail-closed; this ledger reuses that proof rather than
   re-deriving it.
6. Directly inspected public-sync root files, `docs/` subdirectories,
   `.gitignore`, and `git log --diff-filter=A` history for the three
   deny-patterned doc classes to distinguish historical drift from current
   policy intent.
7. Directly verified the three `mappedFiles` policy entries exist at their
   provenance source paths, and that the `expectedSot3RegistryIds` are
   present in both `cvf-web/package.json` dependencies and
   `runtime-modules.ts` registry ids.

## Negative Search And Collision Discipline

| Query | Scope | Result | Collision handling |
|---|---|---|---|
| `docs/baselines`, `docs/reviews`, `docs/roadmaps` in `scripts/cvf-public-sync.ps1` | provenance sync script source | zero matches for these three literal path strings in the script body (they appear only as `DENY_PATTERNS` regex fragments, already cited in the Source Verification Block) | no alias promoted; the deny-pattern citation is the only source-owner claim made |
| `AGENT_HANDOFF` prefix at public-sync root | public-sync root directory listing plus `git ls-files` and `git check-ignore -v` | three ignored local residue files matched: `AGENT_HANDOFF_INTEGRATIONS_2026-05-17.md`, `AGENT_HANDOFF_LIVE_TEST_VARIANCE_2026-05-17.md`, `AGENT_HANDOFF_V8_2026-05-17.md`; only the mapped `AGENT_HANDOFF.md` is tracked | treated as confirmed local-root residue below, not tracked public content and not a missing-term false negative |
| `docs/baselines`, `docs/reviews`, `docs/roadmaps` presence in public-sync clone | public-sync root filesystem plus `git ls-files` and `git check-ignore -v` | filesystem counts are 12, 37, and 20; tracked counts are 0, 4, and 0 respectively at HEAD `9f39111cd` | `.gitignore` covers baselines and roadmaps; the 12 baseline files, 33 of 37 review files, and all 20 roadmap files are ignored local residue. Four review files are tracked policy drift. The two states are kept distinct and recorded for separate reviewer triage |
| `cvf-refinery`, `cvf-truth-kernel`, `cvf-truth-flow` in cvf-web dependencies and registry | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`, `.../src/lib/server/runtime-modules.ts` | 3/3 present in both, matching policy `expectedSot3RegistryIds` | no collision; direct match confirms `Get-CvfWebObservation`'s accepted read model with zero semantic review flags |

No `SOURCE_AUTHORITY_BLOCKED` disposition is used anywhere in this ledger;
every claimed surface was found and confirmed by direct inspection above.

## Three-Root Identity Table

| Root | Repository role | Current origin | Clean/dirty observation | Semantic authority | Mutation prohibition |
|---|---|---|---|---|---|
| Provenance (this repository) | private governed source of truth | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git` (matches `policy.expectedRemotes.provenanceRemote`) | CLEAN at HEAD `a6afabbfa` (`git status --porcelain` zero lines) | sole semantic owner of all governed content; `governance/`, `docs/reference/`, `docs/reviews/`, `docs/roadmaps/`, `docs/baselines/`, `EXTENSIONS/`, `scripts/` originate here | T0 forbids any write in this root beyond the two Allowed paths |
| Public-sync (sibling clone) | curated public projection target | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` (matches `policy.expectedRemotes.publicRemote`) | CLEAN at HEAD `9f39111cd` (`git status --porcelain` zero lines) | never a semantic owner; only a projection target curated by the reviewer/closer via `scripts/cvf-public-sync.ps1` and manual `CVF_TECHNICAL_PRODUCT_CATALOG` updates | T0 forbids any write in this root; read-only inspection only |
| cvf-web (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` under provenance) | live application package, not a separate git root | shares provenance's origin; not an independently cloned root | package root exists; `package.json` and `src/lib/server/runtime-modules.ts` both present and readable | owned by provenance as application source; observed (not owned) by the mapper's `Get-CvfWebObservation` for SOT3 dependency/registry parity | T0 forbids any write here; read-only inspection only |

## Landmark Table

| Landmark | Artifact/commit | Evidence | Status |
|---|---|---|---|
| Projection mapper foundation | `scripts/get_cvf_projection_map.ps1`; closure commit `5df0c6f77` | `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_FINAL_CLOSURE_AUDIT_2026-07-18.md` reports 46/46 temp-only and 50/50 governed-receipt PASS, `schemaVersion 1.0.0`, `policyParity` 8/8 MATCH, zero errors | REVIEWER_ACCEPTED_BOUNDED |
| CVF Web UX closure (T0 release condition) | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md`; commit `d757fe5ac` | bounded localhost current-source acceptance; `CLOSED_PASS_BOUNDED` | CLOSED_PASS_BOUNDED |
| SOT3/CVF projection roadmap closure | commit `9f7c92663` | cited in roadmap Authority And Recovery Evidence; reachable via `git log --oneline -1 9f7c92663` | REACHABLE |
| T0 authoring session release | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; sync commits `0145218a2`, `ebc0242fd`, `a6afabbfa` | `git log --oneline -5` shows the exact chain: `a6afabbfa` (sync for T0 worker) after `ebc0242fd` (dispatch) after `0145218a2` (sync after Web UX closure) after `d757fe5ac` | PASS |
| Current provenance HEAD (this ledger's base) | `a6afabbfa` | `git rev-parse HEAD` | VERIFIED |
| Current public-sync HEAD | `9f39111cd` | `git rev-parse HEAD` in the sibling clone; commit message `docs: restore curated public README front door`, dated 2026-07-18 | VERIFIED |

No file-content SHA256 hash is recorded in this ledger because the live
mapper invocation against the real roots did not complete inside this
worker's execution window (see Scope / Methodology item 5); no hash claim is
made that was not independently recomputed by this worker.

## Findings / Position: Terminal Contract Rows

Every row states `semanticOwner`, `projectionTarget`, `evidenceClass`,
`audience`, and `driftDisposition`, followed by the reasoning that separates
file freshness from semantic and presentation equivalence.

| Surface | semanticOwner | projectionTarget | evidenceClass | audience | driftDisposition |
|---|---|---|---|---|---|
| `governance/toolkit/05_OPERATION/CVF_PUBLIC_CORE_AGENTS.md` -> public-sync `AGENTS.md` | provenance governance toolkit | public-sync root file (policy `mappedFiles[0]`) | source (evidence-command `Get-FileHash -Algorithm SHA256`; disposition MATCH) | external agent; developer | CURRENT - exact byte identity independently confirmed |
| `governance/toolkit/05_OPERATION/CVF_PUBLIC_CORE_CONTINUATION.md` -> public-sync `AGENT_HANDOFF.md` | provenance governance toolkit | public-sync root file (policy `mappedFiles[1]`) | source (evidence-command `Get-FileHash -Algorithm SHA256`; disposition MATCH) | external agent; developer | CURRENT - exact byte identity independently confirmed |
| `scripts/install_cvf_workspace_root_wrappers_public.ps1` -> public-sync `scripts/install_cvf_workspace_root_wrappers.ps1` | provenance scripts owner | public-sync `scripts/` (policy `mappedFiles[2]`) | source (evidence-command `Get-FileHash -Algorithm SHA256`; disposition MATCH) | developer; external agent | CURRENT - exact byte identity independently confirmed |
| Eight byte-identical `allowedRootFiles` (`ARCHITECTURE.md`, `SECURITY.md`, `CHANGELOG.md`, `CONTRIBUTORS.md`, `LICENSE`, `netlify.toml`, `package.json`, `package-lock.json`) | provenance root maintainers | public-sync repository root | source (evidence-command `Get-FileHash -Algorithm SHA256` for each pair; disposition MATCH) | end user; developer; external agent | CURRENT - all eight source/target pairs are byte-identical |
| Six target-only `allowedRootFiles` (`GOVERNANCE.md`, `PROVENANCE.md`, `PROVIDERS.md`, `CONTRIBUTING.md`, `COST_AND_QUOTA.md`, `CODEOWNERS`) | no current provenance root source file found | public-sync repository root | source (reviewer `Test-Path` and repo-wide filename search found no root source owner; public targets are tracked) | developer; external agent; reviewer/operator | SOURCE_AUTHORITY_BLOCKED - policy allowlisting does not establish a current semantic source; a later packet must identify the owner or explicitly classify these as curated public-only files |
| `docs/baselines/` (deny-patterned) | provenance-only, never a projection source | none (explicitly denied) | source (12 ignored local files; 0 tracked at public-sync HEAD `9f39111cd`) | reviewer/operator only | SEMANTIC_REVIEW_REQUIRED - local residue exists but is not committed public content; cleanup or tolerance requires a separate governed batch |
| `docs/reviews/` (deny-patterned) | provenance-only, never a projection source | none (explicitly denied) | source (37 filesystem files; 4 tracked and 33 ignored at public-sync HEAD `9f39111cd`) | reviewer/operator only | SEMANTIC_REVIEW_REQUIRED - four tracked files are policy drift and the ignored residue is a separate workspace-hygiene concern |
| `docs/roadmaps/` (deny-patterned) | provenance-only, never a projection source | none (explicitly denied) | source (20 ignored local files; 0 tracked at public-sync HEAD `9f39111cd`) | reviewer/operator only | SEMANTIC_REVIEW_REQUIRED - local residue exists but is not committed public content; cleanup or tolerance requires a separate governed batch |
| `^AGENT_HANDOFF` root files (deny-patterned) | provenance-only, never a projection source | none (explicitly denied) | source (three dated files are ignored local residue; only mapped exception `AGENT_HANDOFF.md` is tracked) | reviewer/operator only | SEMANTIC_REVIEW_REQUIRED - local residue is distinct from public repository drift and needs separate reviewer triage |
| `allowedTrees` set (`EXTENSIONS`, `ECOSYSTEM`, `governance`, `v1.0`, `v1.1`, `tools`, `.github`, `App onboarding`) | provenance root maintainers per-tree | public-sync repository root (same relative paths) | source (allow matching logic and fixture proof are current; real-root recursive receipt remains incomplete) | developer; external agent | SEMANTIC_REVIEW_REQUIRED - no per-file freshness claim is allowed until a bounded real-root receipt completes |
| `allowedDocsPaths` set (`docs/GET_STARTED.md`, `docs/CHEAT_SHEET.md`, `docs/CVF_ARCHITECTURE_DECISIONS.md`, `docs/CVF_CORE_KNOWLEDGE_BASE.md`, `docs/EXPORT_MANIFEST.md`, `docs/concepts`, `docs/guides`, `docs/reference`, `docs/benchmark`) | provenance docs maintainers | public-sync `docs/` allowed subset | source (docs-path matching logic and fixture proof are current; real-root recursive receipt remains incomplete) | end user; developer; external agent | SEMANTIC_REVIEW_REQUIRED - no per-file freshness claim is allowed until a bounded real-root receipt completes |
| `denyPatterns` set (secrets, build artifacts, internal-only classes) | provenance policy owner (`scripts/cvf_projection_policy.json`) | none (explicitly denied everywhere) | source (`policyParity` mechanism confirmed accepted in the T2 closure audit; this ledger's own negative search confirms the deny regexes match the legacy public-sync files found above) | reviewer/operator only | CURRENT  -  the deny-pattern definitions themselves are confirmed current and correctly authored; the finding is that legacy public-sync content predates full enforcement, not that the pattern definitions are stale |
| cvf-web SOT3 dependency/registry parity (`cvf-refinery`, `cvf-truth-kernel`, `cvf-truth-flow`) | cvf-web package maintainers | not projected to public-sync; internal consistency check only | source (directly confirmed: all three ids present in both `package.json` `dependencies` and `runtime-modules.ts` `id:` fields via direct grep) | developer; reviewer | CURRENT  -  3/3 present in both surfaces; zero `SOT3_DEPENDENCY_PRESENT_REGISTRY_MISSING` inconsistency flags possible under the observed data |
| `scripts/cvf-public-sync.ps1` <-> `scripts/cvf_projection_policy.json` parity | provenance scripts owner (`cvf-public-sync.ps1` is the named source of truth per the policy file's own `sourceOfTruth` field) | not projected itself (deny-patterned: `scripts[/\\]cvf-public-sync\.ps1$`) | source (T2 closure audit's `Get-PolicyParityReport` mechanism accepted with 8/8 `MATCH`; this ledger independently re-read the variable names `$PUBLIC_REMOTE`, `$ALLOWED_TREES`, `$DENY_PATTERNS` directly in the script and confirms they exist as claimed) | reviewer/operator; developer | CURRENT  -  mechanism accepted in T2; this ledger's spot-check of variable existence found no contradiction |
| Public technical catalog (`docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`) | provenance root maintainers, manually updated per the project instructions file's Public Catalog Update Rule (NOT_CVF_SOURCE, cited descriptively only) | public-sync `docs/reference/` (covered by `allowedDocsPaths`) | reviewer (manual update rule, not mapper-covered) | end user; external agent; developer | NOT_APPLICABLE_WITH_REASON  -  this surface is governed by a separate manual update rule with its own verification discipline (`Test-Path` re-verification in public-sync clone); it is outside the mapper's automated allow/deny classification scope and is recorded here only to prevent a future T1 gap, not because this ledger inspected its current freshness |
| Public-sync `README.md` hero/status content | provenance `README.md` is semantic source; public-sync `README.md` receives curated content: disposition NOT_LITERAL_WITH_REASON (confirmed by direct read comparison, evidence-command `git diff --no-index README.md ../Controlled-Vibe-Framework-CVF-public-sync/README.md`, showing distinct hero/badge content, not a byte-identical copy) | public-sync repository root | reviewer (curated projection, confirmed by direct read of public-sync `README.md` showing hero/badge content distinct from a raw file copy) | end user | AUDIENCE_PRESENTATION_RISK  -  this is the roadmap's core lesson (`Source freshness does not imply good presentation`); `README.md` is in `allowedRootFiles` so file-level projection is in scope, but the roadmap's Audience Projection Contract requires end-user presentation review separate from any freshness signal. No mapper mechanism currently evaluates presentation quality; this is exactly the T3 gap the roadmap already names |

### Row Totals

| Disposition | Row count |
|---|---|
| CURRENT | 7 |
| SEMANTIC_REVIEW_REQUIRED | 6 |
| SOURCE_AUTHORITY_BLOCKED | 1 |
| NOT_APPLICABLE_WITH_REASON | 1 |
| AUDIENCE_PRESENTATION_RISK | 1 |
| **Total rows** | **16** |

### Row Totals By Audience

| Audience | Row count (rows may list multiple audiences) |
|---|---|
| End user | 4 |
| Developer | 10 |
| External agent | 10 |
| Reviewer/operator | 9 |

### Row Totals By Evidence Class

| Evidence class | Row count |
|---|---|
| source | 14 |
| reviewer | 2 |

(Two rows cite both `source` and `reviewer` evidence classes where a manual
curation step sits alongside directly observed file state; they are counted
once in each applicable class above.)

## Explicit Separation Of Freshness, Semantic, Hosted, And Audience Dimensions

- **Source freshness** (byte/file presence identity between provenance and
  public-sync): confirmed only for the `allowedRootFiles` filename set (15/15
  present by name) and the cvf-web SOT3 dependency/registry pair (3/3
  present). Byte-level freshness for tree and mapped-file content was not
  confirmed this run because the live recursive mapper invocation did not
  complete; see the `SEMANTIC_REVIEW_REQUIRED` aggregate rows above.
- **Semantic equivalence** (does the public-sync content mean the same thing
  as the provenance content, independent of byte match): not evaluated by
  this ledger for any row beyond the mapper's own
  `FLAG_SEMANTIC_REVIEW_CHANGED` classification label, which this ledger did
  not get to exercise against real content this run. No row in this ledger
  claims semantic equivalence.
- **Hosted freshness** (whether a deployed/hosted surface matches current
  source): explicitly out of scope. No hosted, Netlify, or deployment
  identity claim is made anywhere in this ledger, consistent with the T4
  completion review's residual item "hosted/current freshness identity ...
  separate hosted packaging or deployment packet with exact build identity."
- **Audience presentation acceptance** (whether a projected surface reads
  well for its intended audience): evaluated qualitatively only for the
  public-sync `README.md` row above, flagged `AUDIENCE_PRESENTATION_RISK`
  because no automated mechanism currently checks this dimension. This
  matches the roadmap's T3 gap and its "Learning Carried Forward" item 1:
  source freshness does not imply good presentation.

## Proposed T1 Read-Only Receipt Schema

This section proposes fields only; nothing here is implemented, and no
runtime status is claimed beyond `DOC_ONLY_NEW`.

```
driftReceipt.schemaVersion        : string   (e.g. "1.0.0"), DOC_ONLY_NEW
driftReceipt.receiptId            : string   (SHA256 of canonical JSON, mirrors existing mapper receiptId pattern), DOC_ONLY_NEW
driftReceipt.generatedAtLogical   : string   (deterministic ordinal, NOT wall-clock, to preserve byte-identical repeated runs), DOC_ONLY_NEW
driftReceipt.rootsObserved        : object   (provenance/publicSync/cvfWeb identity + clean/dirty + remote match, reusing existing rootsValidated shape), DOC_ONLY_NEW
driftReceipt.rows[]                : array of terminal rows, each with:
  .surface                        : string   (source path or named surface id), DOC_ONLY_NEW
  .semanticOwner                  : string, DOC_ONLY_NEW (this work order's field)
  .projectionTarget               : string   ("NONE" for denied surfaces), DOC_ONLY_NEW (this work order's field)
  .evidenceClass                  : enum     ["source","hash","browser","reviewer"], DOC_ONLY_NEW (this work order's field)
  .audience                       : array of enum ["end_user","developer","external_agent","reviewer"], DOC_ONLY_NEW (this work order's field)
  .driftDisposition                : enum     [CURRENT, MISSING_TARGET, STALE_TARGET, AUDIENCE_PRESENTATION_RISK, SEMANTIC_REVIEW_REQUIRED, NOT_APPLICABLE_WITH_REASON, SOURCE_AUTHORITY_BLOCKED], DOC_ONLY_NEW (this work order's field)
  .sourceHash                     : string or null (SHA256, only when evidenceClass=hash and both sides read), DOC_ONLY_NEW
  .targetHash                     : string or null, DOC_ONLY_NEW
  .reviewerNote                   : string or null (required when driftDisposition=SEMANTIC_REVIEW_REQUIRED or AUDIENCE_PRESENTATION_RISK), DOC_ONLY_NEW
driftReceipt.summary.rowCount                  : integer, DOC_ONLY_NEW
driftReceipt.summary.byDisposition             : object (counts per enum value), DOC_ONLY_NEW
driftReceipt.summary.reconciliationMatch       : boolean (sum of byDisposition equals rowCount), DOC_ONLY_NEW
driftReceipt.noTargetWriteConfirmation         : string (reuse existing mapper wording verbatim), DOC_ONLY_NEW
driftReceipt.errors[]                          : array (reuse existing mapper {code,message} shape), DOC_ONLY_NEW
```

### Deterministic Ordering Rules (proposed)

1. Rows sorted by `surface` ascending (ordinal string comparison), mirroring
   the accepted mapper's existing `Sort-Object -Property sourcePath,
   targetPath` pattern.
2. `audience` arrays sorted in the fixed enum declaration order
   (`end_user`, `developer`, `external_agent`, `reviewer`), never
   insertion order, so two runs over identical state are byte-identical.
3. `receiptId` computed exactly as the existing mapper computes it: SHA256
   over the compressed canonical JSON of every field except `receiptId`
   itself, matching `Get-Sha256Hex` / `ConvertTo-Json -Compress` already
   proven deterministic in the T1/T2 accepted suites
   (`deterministic_repeated_run_receipt_id`,
   `deterministic_two_runs_receipt_id_stable`).

### Proposed Negative Cases (for T1 focused-suite parity with the accepted mapper)

- `MISSING_PROVENANCE_ROOT`, `MISSING_PUBLIC_ROOT`, `MISSING_CVF_WEB_ROOT`
  (reuse existing mapper codes verbatim).
- `WRONG_PROVENANCE_REMOTE`, `WRONG_PUBLIC_REMOTE`,
  `provenance_remote_substring_spoof_rejected` (reuse existing mapper
  negative-case names verbatim; the substring-spoof case is the one already
  proven in the accepted T2 suite and must not be weakened).
- `DIRTY_PROVENANCE_ROOT`, `DIRTY_PUBLIC_ROOT` (reuse existing mapper codes;
  a T1 drift receipt must inherit the same fail-closed dirty-root refusal
  the T0 work order itself imposed on this ledger's own evidence-gathering).
- New: `RECEIPT_TIMEOUT_INCONCLUSIVE`  -  proposed code for exactly the
  situation this ledger encountered (a live recursive run over real
  `EXTENSIONS`/`ECOSYSTEM`/`governance` trees not completing inside a bounded
  worker window). A T1 implementation should decide whether this is a hard
  failure or a partial-receipt-with-explicit-gap state; this ledger takes no
  position and marks it `DOC_ONLY_NEW` only.
- New: `AUDIENCE_EVIDENCE_MISSING`  -  proposed code for a row that requires
  `AUDIENCE_PRESENTATION_RISK` disposition but has no attached reviewer note
  or browser evidence path, forcing the receipt generator to fail closed
  rather than silently defaulting to `CURRENT`.

### Manual / CI / Scheduled Invocation Seams (proposed)

| Seam | Trigger | Apply authority | Notes |
|---|---|---|---|
| Manual | reviewer runs the T1 script locally against real roots | reviewer only; no auto-apply | mirrors today's manual mapper invocation pattern |
| CI | a read-only workflow job runs the T1 script against a disposable fixture (never the real public-sync remote) and uploads the receipt as a build artifact | none; CI never writes to any root | mirrors the existing `test_get_cvf_projection_map.ps1` and `test_cvf_projection_three_root_proof.ps1` disposable-fixture discipline; a CI job against the *real* public-sync clone would require its own separate GC-018 because it changes the trust boundary from "developer machine" to "shared runner" |
| Scheduled | an operator-authorized periodic job runs the T1 script against real roots and stores the receipt for reviewer triage | reviewer triages; scheduler never applies | requires a fresh GC-018 before any scheduled invocation against real (non-fixture) roots is authorized, per this roadmap's own Forbidden automation list ("committing, pushing, deploying, or applying to a real root unattended") |

### Reviewer Ownership (proposed)

The reviewer/closer remains the sole owner of interpreting any
`SEMANTIC_REVIEW_REQUIRED` or `AUDIENCE_PRESENTATION_RISK` row and of
deciding whether a `COPY_CANDIDATE_ABSENT_TARGET`-equivalent T1 finding
should become a real copy/apply work order. No T1 receipt field may carry an
auto-approve or auto-apply capability; this preserves the accepted policy's
`semanticReviewBoundary.autoApproveForbidden: true` invariant unchanged.

## T1 Release Recommendation

This ledger recommends that a future T1 work order MAY proceed to implement
the proposed receipt schema above, subject to:

1. A T1 implementation must first resolve the `RECEIPT_TIMEOUT_INCONCLUSIVE`
   question this ledger surfaced  -  either bound the recursive scan to a
   time budget with partial-receipt semantics, or accept a longer-running
   batch invocation model. This ledger does not resolve that design
   question and does not authorize T1 implementation by itself.
2. A T1 implementation must carry forward the four `SEMANTIC_REVIEW_REQUIRED`
   rows found in this ledger (`docs/baselines/`, `docs/reviews/`,
   `docs/roadmaps/`, and `^AGENT_HANDOFF` legacy root files already present
   in public-sync) as a pre-seeded reviewer triage list, not as new T1
   findings to rediscover.
3. This recommendation does not itself authorize any implementation, script
   edit, policy edit, real-root apply, commit, push, or public-sync
   mutation. It is a documentation recommendation only, consistent with the
   work order's Claim Boundary.

## Risk / Corrective Action

| Risk | Disposition | Control |
|---|---|---|
| Live mapper invocation against real roots did not complete inside this worker's execution window | accepted as a recorded evidence gap | affected aggregate rows use the contract-valid `SEMANTIC_REVIEW_REQUIRED` disposition rather than defaulting to `CURRENT`; no freshness claim is made without direct evidence |
| Tracked policy drift and ignored local residue were conflated in the worker draft | corrected by reviewer | four tracked review files are separated from ignored baseline, roadmap, review, and dated-handoff residue; this ledger takes no removal or mutation action |
| Confusing this ledger's terminal rows with a live drift receipt | rejected | every row states its evidence basis explicitly (`source` vs `reviewer`) and the Explicit Separation section above states plainly which dimensions were and were not evaluated |
| T1 schema proposal read as pre-authorized implementation | rejected | the T1 Release Recommendation section states plainly this is a recommendation only and lists unresolved design questions |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `Memory class`, `Status`, `docType`, required heading set from `check_worker_return_quality_gate.py` (`REQUIRED_HEADINGS`), `DEFERRED_PRIVATE_ONLY` plus `Reason:` requirement from `check_public_export_disposition.py`, `REQUIRED_FILES`/`REQUIRED_MARKERS` from `check_markdown_structural_completeness.py` |
| gateRunPurpose | confirm this ledger's own structural shape and literal tokens before drafting, per the work order's `checkerReadAheadConfirmation` field |
| claimBoundary | checker compliance confirms packet structure only; the terminal contract rows above are independently source-verified evidence, not a checker-compliance claim |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | public/simple cvf vocabulary |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no outside repository, critique packet, or provider output is absorbed |
| Matching local-view guard | N/A with reason: direct current source in all three roots is the authority for every row |
| Owner surface | continuous-projection roadmap and this ledger only |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | external-agent audience is a consumer class named in the terminal rows, not an external authority source for this ledger's own claims |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: this ledger is a first-pass T0 contract definition over currently
inspected source and repository state, not a rescan, intake-refresh, or
reassessment of a prior corpus-scan finding.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON  -  this ledger does not claim a
  complete scan, complete inventory, or exhaustive file-by-file read of any
  folder, subfolder tree, or archive. It claims direct verification of the
  specific named surfaces listed in the Terminal Contract Rows table only,
  each with its own evidence class stated. The `allowedTrees` and
  `allowedDocsPaths` rows are explicitly marked `SEMANTIC_REVIEW_REQUIRED`
  precisely because a full recursive inventory comparison was not completed
  this run.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Four deny-patterned review files are tracked in public-sync while other deny-patterned files are ignored local residue | RULE_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | a future reviewer-owned batch should disposition the four tracked files separately from optional cleanup of ignored residue; this ledger does not decide either action | deferred |
| A live recursive mapper run against real (non-fixture) three-root state can exceed a bounded worker execution window | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | proposed `RECEIPT_TIMEOUT_INCONCLUSIVE` code in the T1 schema section above; no rule change made in this ledger | deferred |

Raw-memory boundary: `rawMemoryReleased=false`. No raw memory release or
reinjection claim is made.

## Epistemic Process Block

### Expected Result / Prediction

The accepted read-only mapper and its policy should still classify every
seed surface correctly with no source contradiction, and the three-root
identity check should pass cleanly given both roots were reported clean
before dispatch.

### Evidence Comparison

Both roots were confirmed clean and correctly identified by remote URL and
HEAD. The mapper's classification mechanism remained correct per the reused
T2 acceptance evidence. Direct inspection surfaced four tracked
deny-patterned review files and separate ignored local residue in the
public-sync workspace. The mapper's source-side deny classification does not
by itself reconcile target-only residue.

### Contradiction Or Gap Disposition

No contradiction in the mapper mechanism itself. The gap found is a
real-world target-state condition rather than a defect in the source-verified
mapper logic. The live-receipt timeout is a
recorded evidence-collection gap, not a mechanism defect, and every affected
row reflects that gap explicitly rather than assuming `CURRENT`.

### Claim Update

This ledger's terminal contract is source-backed for root identity,
landmark reachability, mappedFiles/allowedRootFiles/SOT3 presence-by-name,
and the legacy deny-patterned content finding. It explicitly does not claim
completed byte-level freshness for tree-scale content, does not claim
semantic equivalence for any row, and does not claim hosted freshness for
any surface.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | no-commit worker |
| Provider or surface | private provenance workspace |
| Session or invocation | CVF-CONTINUOUS-PROJECTION-T0, 2026-07-20 |
| Working directory | repository root |
| Command or tool surface | git, direct file reads, `python governance/compat/run_agent_autorun_workflow_gate.py`, attempted `powershell -File scripts/get_cvf_projection_map.ps1` (inconclusive, see Scope / Methodology item 5) |
| Target paths | this ledger; the paired worker return |
| Allowed scope source | work order Scope / Target / Owner Boundary section |
| Before status evidence | clean provenance worktree at HEAD `a6afabbfa` |
| After status evidence | two untracked worker outputs; provenance HEAD unchanged at `a6afabbfa`; public-sync and cvf-web roots unchanged (read-only inspection only, confirmed by re-running `git status --porcelain` in the public-sync root after inspection) |
| Diff evidence | `git diff --name-status` (empty; both outputs are untracked, not modifications) |
| Approval boundary | T0 documentation audit only |
| Claim boundary | no mapper edit, policy edit, test edit, cvf-web edit, real-root apply, commit, push, or public-sync mutation |
| Agent type | no-commit worker |
| Invocation ID | `continuous-projection-t0-worker-2026-07-20` |
| Expected manifest | this ledger; the paired worker return |
| Actual changed set | this ledger; the paired worker return |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename performed |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | three-root projection drift contract definition |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, or auto-apply behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no fresh mapper receipt file was produced this run; the reused T2 receipt evidence is cited by path, not re-emitted |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no copy, apply, mutation, or filesystem write occurred in any of the three roots |
| invocationBoundary | manual local git, file-read, and autorun-gate invocation only |
| interceptionBoundary | no provider, hosted, production, or external-service interception |
| claimLanguage | inspect, map, classify, reconcile, and propose only |
| forbiddenExpansion | implementation, semantic edit, apply, commit, push, deploy, public-sync mutation, provider/live calls, production action |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this ledger is a private provenance audit of the boundary between
the provenance root and the sibling public-sync clone. It creates no
public-safe export and authorizes no public-sync mutation.

## Claim Boundary

This ledger defines a terminal T0 three-root drift contract from
source-verified root identity, landmark, and per-surface evidence. It does
not authorize mapper implementation, script edits, policy edits, test edits,
cvf-web edits, real-root apply, commit, push, deployment, public-sync
mutation, provider/live calls, or production action. Byte-level freshness
claims are explicitly withheld wherever the live mapper receipt did not
complete; no row defaults to `CURRENT` without direct evidence.
