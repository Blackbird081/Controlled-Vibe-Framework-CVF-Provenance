# CVF Agent Work Order - SOT3-APP-T0A Corpus Freeze And Semantic Calibration

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIRS

docType: work_order

Date: 2026-07-16

Batch ID: `SOT3-APP-T0A`

dispatchBaseHead: `e7f45e120`

executionBaseHead: `120c0f90a`

closureBaseHead: `120c0f90a`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Worker ledger path:
`docs/reviews/CVF_SOT3_APP_T0A_CORPUS_METADATA_AND_SAMPLE_LEDGER_2026-07-16.md`

Worker return path:
`docs/reviews/CVF_SOT3_APP_T0A_WORKER_RETURN_2026-07-16.md`

Source intake decision packet: REQUIRED

Role: delegated source-intake worker for the bounded
`SOT3-APP-T0A` metadata freeze, declaration inventory, and semantic calibration
sample.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T0A_CORPUS_FREEZE_AND_SEMANTIC_CALIBRATION_2026-07-16.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture the clean committed dispatch HEAD before any edit,
record it in both outputs, and use it as the base for all worker gates.

Current-time notes: the dispatch-author snapshot was recomputed on 2026-07-16.
Recompute every count, byte total, file hash, aggregate, declaration occurrence,
sample hash, and hidden-clone Git metadata fact from the current physical roots.

Do-not-misread notes: metadata completion for all 336 files is not semantic
completion. Semantically disposition exactly SAM-01 through SAM-20. Leave the
remaining 316 semantic rows and all terminal declaration decisions for T0B.
Do not run or mutate either application or clone.

Required first actions: complete the startup acknowledgment; read guard
orientation, literal gotchas, roadmap, paired GC-018, this work order, accepted
scope review, source-intake standards, and output-applicable checker sources;
then prove clean HEAD, absent output paths, exact source snapshot, exact sample
hashes, 13 declaration occurrences, and hidden-clone metadata before writing.

Return contract: create exactly the two worker outputs named above, run the
required worker-return and documentation gates, leave every change uncommitted,
and return exactly `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute phase one of the full-corpus SOT Application intake without reducing
the source corpus: freeze objective metadata for all 336 physical files,
enumerate every hidden-clone declaration occurrence, and calibrate semantic
disposition on one fixed reviewer-selected 20-file sample. Preserve a
machine-reconcilable boundary showing that 316 file-level semantic decisions
and all terminal declaration decisions remain open for T0B.

## Operator Source Intent And Chronology

The operator attests that both named folders were authored after SOT3 to
respond to two distinct residual gaps.

| Source root | Operator-attested source class | Gap-response purpose | Authority boundary |
|---|---|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application` | `POST_SOT3_DOWNSTREAM_PRODUCT_GAP_RESPONSE` | exercise a complete downstream lifecycle from bounded source and authority through context, output, review, freeze, impact, and recall | external operator-authored evidence input only |
| `.private_reference/legacy/CVF_SOT 10.07/cvf_four_surface_control_boundary_patch` | `POST_SOT3_CONTROL_BOUNDARY_GAP_RESPONSE` | make object, mode, timing, maturity, evidence, bypass, and failure boundaries explicit | separate private reference evidence input only |

The physical `legacy` storage segment is not a semantic or chronology label.
This packet processes only SOT-Application. It does not reopen or modify the
separately accepted Four-Surface crosswalk. Operator source intent is not CVF
authority, runtime proof, or an exact filesystem timestamp claim.

## Authority Chain

| Order | Authority | Evidence | Boundary |
|---:|---|---|---|
| 1 | operator authorization | intake review material commit `24d50f0d7` plus current instruction | authorize careful governed absorption planning, not direct import |
| 2 | scope-split decision | `docs/reviews/CVF_SOT3_APP_T0_R1_SCOPE_BLOCKER_REVIEW_2026-07-15.md`, material commit `55007483c` | reject a 50-100-file reduced completion; select two-phase full-corpus route |
| 3 | continuity release | state at `e7f45e120` | authorize fresh T0A packet authoring only |
| 4 | SOT3-APP roadmap | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | release T0A and hold T0B/later work |
| 5 | paired GC-018 | `docs/baselines/CVF_GC018_SOT3_APP_T0A_CORPUS_FREEZE_AND_SEMANTIC_CALIBRATION_2026-07-16.md` | exact snapshot, sample, methods, outputs, and exclusions |
| 6 | this work order | current path | worker execution contract |
| 7 | current CVF governed surfaces | canonical standards and owner sources | CVF remains authority; external folders remain evidence inputs |

Provider memory, chat summaries, copied source claims, and the hidden clone are
not canonical CVF authority.

## Agent Roles

| Role | Responsibility | Commit authority |
|---|---|---|
| dispatcher | authors, verifies, and commits the T0A roadmap/baseline/work-order packet | dispatch packet only |
| delegated worker | recomputes source facts, writes exactly two outputs, runs worker gates, and returns | forbidden |
| independent reviewer/closer | recomputes evidence, audits all 20 semantic rows, repairs only reviewer-owned closure paths, and accepts or rejects T0A | accepted material closure only |
| session-sync steward | updates protected continuity only once an accepted material closure exists | separate session-sync commit |

Designated closer: independent reviewer/closer.

## Scope / Target / Owner Boundary

Allowed source root, read-only:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.

Allowed hidden dependency target, read-only Git metadata only:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\.Controlled-Vibe-Framework-CVF`.

The worker may use `git rev-parse`, `git status --short --branch`, and
`git remote -v` against the hidden target. No fetch, pull, push, checkout,
reset, clean, submodule, maintenance, worktree, or file mutation is allowed in
either external root.

Allowed current-CVF reads are the startup/guard surfaces, committed T0A packet,
accepted intake/scope reviews, current owner standards, and checker sources.
Allowed writes are exactly the two new review artifacts in the fulfillment
manifest.

Forbidden scope includes editing any external file; editing roadmap, baseline,
work order, intake/rebuttal, session/handoff/generated state, Catalog/GAP/ADIF,
checker/hook/test, runtime/product, package, or public-sync files; dependency
resolution; install; build; typecheck; test; CI; app/server/browser/API/provider
execution; binding validation; source copy; terminal T0B classification; or a
commit by the worker.

## Write Ownership

| Path | Worker action | Owner boundary |
|---|---|---|
| `docs/reviews/CVF_SOT3_APP_T0A_CORPUS_METADATA_AND_SAMPLE_LEDGER_2026-07-16.md` | create | 336 metadata rows, aggregate receipt, 13 declaration occurrences, exact 20-row semantic sample, reconciliation, and partial claim boundary |
| `docs/reviews/CVF_SOT3_APP_T0A_WORKER_RETURN_2026-07-16.md` | create | execution/gate evidence, changed-set proof, no-commit return, and reviewer handoff |

Worker may not edit any pre-existing path.

## Commit Mode And Base-Anchor Lifecycle

| Phase | Required anchor | Changed-set boundary | Commit owner |
|---|---|---|---|
| dispatch authoring | dispatchBaseHead=`e7f45e120` | roadmap plus paired GC-018/work order | dispatcher |
| worker execution | executionBaseHead=captured clean committed T0A dispatch HEAD | exactly the two worker outputs | worker cannot commit |
| reviewer closure | closureBaseHead=captured from worker execution base and committed dispatch | worker outputs plus explicitly reviewer-owned closure paths | reviewer/closer |
| session sync | accepted material closure commit | protected continuity files only | session-sync steward |

The worker must not substitute `HEAD..HEAD`, a dirty base, or a remembered SHA
for the captured execution base.

## Dependency Release Evidence

| Dependency | Accepted artifact | Material commit | Final disposition | Release result |
|---|---|---|---|---|
| intake and operator authorization | `docs/reviews/CVF_SOT3_DOWNSTREAM_APPLICATION_AND_FOUR_SURFACE_ABSORPTION_INTAKE_REVIEW_2026-07-15.md` | `24d50f0d7` | `OPERATOR_AUTHORIZED_FOR_ROADMAP_AUTHORING` | PASS |
| two-phase scope decision | `docs/reviews/CVF_SOT3_APP_T0_R1_SCOPE_BLOCKER_REVIEW_2026-07-15.md` | `55007483c` | `ACCEPT_TWO_PHASE_FULL_CORPUS_WITH_CHANGES` | PASS for T0A only |
| continuity release | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `e7f45e120` | `sot3_app_t0_scope_split_packet_authoring_next` | PASS for packet authoring |
| roadmap T0A release | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | current dispatch batch | `T0A_DISPATCH_READY` | PASS for T0A only |
| GC-018 boundary | `docs/baselines/CVF_GC018_SOT3_APP_T0A_CORPUS_FREEZE_AND_SEMANTIC_CALIBRATION_2026-07-16.md` | current dispatch batch | `DISPATCH_READY` | PASS |

T0B has no dependency-release row and remains held. No worker may infer T0B
release from this work order, roadmap sequencing, chat, or operator silence.

## Required First Reads

| Order | Path | Required action |
|---:|---|---|
| 1 | `CVF_SESSION_MEMORY.md` | FULL_READ |
| 2 | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | FULL_READ |
| 3 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | FULL_READ |
| 4 | active handoff named by state | FULL_READ |
| 5 | `docs/reference/guard_orientation/README.md` | FULL_READ |
| 6 | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ |
| 7 | SOT3-APP roadmap, paired T0A GC-018, and this work order | FULL_READ |
| 8 | `docs/reviews/CVF_SOT3_APP_T0_R1_SCOPE_BLOCKER_REVIEW_2026-07-15.md` | FULL_READ |
| 9 | `docs/reference/external_agent_review/README.md` | FULL_READ |
| 10 | `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` | FULL_READ |
| 11 | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | FULL_READ |
| 12 | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | FULL_READ |
| 13 | checker sources named in Worker Output Checker Read-Ahead Mandate | SOURCE_VERIFIED |
| 14 | exact SAM-01 through SAM-20 source files | FULL_READ before semantic rows |

## Pre-Flight Checks

1. Run `git rev-parse --short HEAD` in the CVF provenance workspace and record
   it as `executionBaseHead`.
2. Require empty `git status --short` before the first write.
3. Confirm HEAD contains this exact committed work order and paired baseline.
4. Confirm both worker output paths are absent.
5. Enumerate the literal source root using hidden-inclusive, no-ignore physical
   file enumeration.
6. Require exactly 336 files, 238522 bytes, and aggregate SHA-256
   `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee`.
7. Recompute all 20 sample hashes and require an exact match to the sample
   table below.
8. Re-run the exact declaration search and require 13 occurrence lines.
9. Recompute hidden-target metadata and require short HEAD `a78b35c`, empty
   `git status --short`, and origin
   `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`.
10. Read checker sources before writing either output.
11. Stop on any mismatch; do not silently refresh the packet or replace a
    sample.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| operator authorized the governed SOT3-APP lane | VALUE_SET | `docs/reviews/CVF_SOT3_DOWNSTREAM_APPLICATION_AND_FOUR_SURFACE_ABSORPTION_INTAKE_REVIEW_2026-07-15.md` | Decision / Disposition | `OPERATOR_AUTHORIZED_FOR_ROADMAP_AUTHORING` | governed intake review | ACCEPT |
| reduced-corpus completion is rejected and two-phase full-corpus processing is selected | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T0_R1_SCOPE_BLOCKER_REVIEW_2026-07-15.md` | Decision / Disposition | `ACCEPT_TWO_PHASE_FULL_CORPUS_WITH_CHANGES` | governed scope-blocker review | ACCEPT |
| T0A requires 336 metadata rows and an exact 20-row semantic sample | VALUE_SET | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | Work Plan | `SOT3-APP-T0A` | SOT3-APP roadmap | ACCEPT |
| T0B remains dependency-held | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T0_R1_SCOPE_BLOCKER_REVIEW_2026-07-15.md` | Decision / Disposition | `T0B release` | governed scope-blocker review | ACCEPT |
| the dispatch snapshot is 336 files and 238522 bytes | VALUE_SET | `docs/baselines/CVF_GC018_SOT3_APP_T0A_CORPUS_FREEZE_AND_SEMANTIC_CALIBRATION_2026-07-16.md` | Current External Source Snapshot | `physical file count` | paired GC-018 evidence carrier | ACCEPT |
| the canonical ordinal aggregate has the fixed dispatch digest | VALUE_SET | `docs/baselines/CVF_GC018_SOT3_APP_T0A_CORPUS_FREEZE_AND_SEMANTIC_CALIBRATION_2026-07-16.md` | Current External Source Snapshot | `aggregate SHA-256` | paired GC-018 evidence carrier | ACCEPT |
| exact declaration search currently returns 13 occurrences | VALUE_SET | `docs/baselines/CVF_GC018_SOT3_APP_T0A_CORPUS_FREEZE_AND_SEMANTIC_CALIBRATION_2026-07-16.md` | Current External Source Snapshot | `hidden-clone declaration occurrences` | paired GC-018 evidence carrier | ACCEPT |
| exact sample paths and dispatch hashes are fixed | VALUE_SET | `docs/baselines/CVF_GC018_SOT3_APP_T0A_CORPUS_FREEZE_AND_SEMANTIC_CALIBRATION_2026-07-16.md` | Reviewer-Selected Semantic Calibration Sample | `SAM-01` through `SAM-20` | paired GC-018 sample contract | ACCEPT |
| source-intake packets require bounded scope and overlap routing | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` | Required Packet Fields | `Source Intake Decision Packet` | source-intake decision packet standard | ACCEPT |
| corpus reporting permits an explicit partial verdict with unresolved rows | LITERAL_INVARIANT | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | Corpus Verdict | `PARTIAL` | corpus completeness standard | ACCEPT |
| worker output is reviewer-converted and worker cannot commit | LITERAL_INVARIANT | archive-qualified contract source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Central Core | `WORKER_MUST_NOT_COMMIT` | agent handoff contract | ACCEPT |

## New Doc-Only Fields

| Output | New fields | Classification | Boundary |
|---|---|---|---|
| metadata row | sourceId, relativePath, bytes, sha256, metadataState | DOC_ONLY_NEW | objective file evidence; `METADATA_FROZEN` is not semantic completion |
| sample row | sampleId, sampleGroup, sourcePath, sourceSha256, processingStatus, disposition, valueClass, overlapClass, ownerRoute, nextGovernedAction, reason, adversarialChallenge | DOC_ONLY_NEW | semantic calibration only for exact 20 files |
| declaration row | declarationId, sourcePath, sourceLine, literalTarget, declarationClass, resolvedTarget, targetExists, candidateOwnerRoute, candidateDriftDisposition, candidateRuntimeUseDisposition, t0aState | DOC_ONLY_NEW | occurrence inventory and candidate routing; terminal decisions remain T0B-owned |
| aggregate receipt | fileCount, totalBytes, aggregateSha256, snapshotTime, executionBaseHead | DOC_ONLY_NEW | reproducibility evidence only |

No proposed field is represented as an existing runtime, API, binding, or CVF
contract field.

## Negative Search And Collision Discipline

| Check | Required evidence | Disposition |
|---|---|---|
| ledger output path | exact `Test-Path` before first write | collision check must return false |
| worker-return output path | exact `Test-Path` before first write | collision check must return false |
| semantic sample | compare exact sample IDs, paths, and hashes with committed baseline | no replacement or reduction |
| batch token | `rg -n "SOT3-APP-T0A|SOT3_APP_T0A" docs CVF_SESSION` | predecessor and dispatch references only before outputs |
| source declarations | exact fixed-string search for `.Controlled-Vibe-Framework-CVF` | all occurrence lines retained; no deduplication by file |
| collision response | any planned-path collision or unexpected prior artifact | `BLOCKED_WITH_REASON` |

Negative-search evidence is execution evidence and must appear in the worker
return. Do not convert an unexpected collision into an overwrite.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: docs/reviews/CVF_SOT3_APP_T0_R1_SCOPE_BLOCKER_REVIEW_2026-07-15.md

priorVerificationAnchor: 55007483c

freshRecomputeRequired: true

unicodePathHandling: preserve literal Windows paths and source filenames; normalize only aggregate relative-path separators to forward slashes and sort with ordinal comparison

extractedTextAuthority: direct source bytes and direct decoded text are authoritative for this task; summaries, rendered views, and provider memory are navigation only

Any prior count, hash, sample observation, or declaration is a dispatch
expectation to recompute, not evidence the worker may copy.

## Source Intake Decision Packet

| Field | Value |
|---|---|
| Decision packet standard | `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` |
| Input root or repository | literal SOT-Application source root in Scope / Target / Owner Boundary |
| Bounded scope | 336 metadata rows, complete declaration inventory, and exact SAM-01 through SAM-20 semantic calibration |
| Enumeration authority | physical filesystem enumeration, byte counts, SHA-256, ordinal normalized-path aggregate, and exact fixed-string declaration search |
| Owner-surface taxonomy | CONFIRMED_EXISTING, ENRICH_EXISTING, NEW_FINDING, REJECT_DIRECT_IMPORT, NO_NEW_VALUE, OWNER_SURFACE_NOT_FOUND |
| Pre-scan packet source | accepted scope review `55007483c`, roadmap, paired GC-018, and this work order |
| Overlap routing matrix | every sample row maps to a current CVF owner, pending downstream owner, or OWNER_SURFACE_NOT_FOUND with next governed action |
| Negative-search evidence | negative-search command `rg -n "SOT3-APP-T0A|SOT3_APP_T0A" docs CVF_SESSION`; exact declaration search; output collisions; sample exactness |
| Core disposition | ADAPT objective full-corpus metadata and sample-calibration evidence only |
| Value conversion requirement | every sample row receives one valueClass and one nextGovernedAction |
| Overlap classification requirement | every sample row receives overlapClass plus ownerRoute and a concrete next governed action; no owner promotion in T0A |
| Worker output path | exact ledger and worker-return paths declared at the top of this packet |
| Forbidden scope | semantic propagation to 316 un-sampled files, terminal declaration disposition, T0B release, mutation, runtime, live, or public action |
| Claim boundary | partial intake calibration only; no full absorption or product-readiness claim |

`OWNER_SURFACE_NOT_FOUND` and `NEW_FINDING` are escalation results. Each such
row must name a specific next governed action: current-owner recheck in T0B,
fresh GAP proposal after T0B, or explicit rejection. They do not authorize a
new owner surface.

## Required Metadata Freeze Method

1. Enumerate physical files under the literal source root with hidden files
   and ignored files included; do not follow or inspect paths outside the root.
2. Convert each relative path separator to `/` for the ledger and aggregate.
3. For each physical file compute byte length and SHA-256 from its bytes.
4. Sort aggregate input rows by normalized relative path using ordinal
   code-point comparison, not case-insensitive or locale-aware comparison.
5. Encode each aggregate input row exactly as
   `relativePath<TAB>bytes<TAB>sha256<LF>` using UTF-8 without BOM.
6. SHA-256 the concatenated aggregate bytes.
7. Emit exactly one metadata row for each path and assign
   `metadataState=METADATA_FROZEN` only after path, bytes, and hash are present.
8. Reconcile unique paths, metadata rows, total bytes, per-file hashes, and
   aggregate receipt. Record zero missing and zero duplicate paths.

The 336 metadata rows need no semantic disposition except for the 20 sample
rows. Do not use `METADATA_FROZEN` as a corpus semantic terminal status.

## Complete Declaration Inventory Method

Run an exact fixed-string, hidden-inclusive, no-ignore search for
`.Controlled-Vibe-Framework-CVF` from the literal source root. Preserve every
physical occurrence separately, including multiple declarations in the same
file. The dispatch expectation is 13 occurrence lines.

For each occurrence record source path, physical line, literal matched target,
declaration class, resolved target, target-existence result, and candidate
owner/drift/runtime-use routing. Set `t0aState=DECLARATION_ENUMERATED`.

Candidate routing is not terminal provenance disposition. T0A must not claim
that a declaration is safe, current, severed, governed, synchronized, used at
runtime, or unused at runtime. T0B retains terminal decisions after the T0A
sample is accepted.

## Fixed Reviewer-Selected Semantic Sample

Process exactly these paths. No replacement, convenience sample, or sample-size
change is authorized.

| Sample ID | Group | Relative path | Required SHA-256 | Calibration purpose |
|---|---|---|---|---|
| SAM-01 | doctrine | `README.md` | `5d01f41b7e9de5c7f86a42a1f36d533bcd7bf0aba7c7f2bedc8ec69a6f95be8b` | product boundary and full lifecycle claim |
| SAM-02 | doctrine | `docs/ARCHITECTURE.md` | `1cff0111b87b1849b2deae8023c62ba54fec6b71f7204eea63d930c0d76cedf9` | downstream/core ownership split |
| SAM-03 | doctrine | `docs/CLAIM_BOUNDARY.md` | `fb2b3b5faf6a2e3c313aac3d63623e21b31003a122b956cbcad9b22e11143886` | overclaim and evidence boundary |
| SAM-04 | doctrine | `docs/REVIEW_FREEZE_PROTOCOL.md` | `60da0585588db647aa7249af8516cdeae1848c6c952a2a3582265e5d6154623e` | review/freeze semantics |
| SAM-05 | no-new-value control | `TREEVIEW.md` | `208f4b0708f20f9115450cac7035cc2e47ff85010a313808fd5a370801265bce` | navigation duplication and latent-value challenge |
| SAM-06 | provenance | `.cvf/manifest.json` | `21d1ab9073f154f15d30784b4044437b650c9b645f76f1a2f4aa9fdf0e2958dc` | hidden governance root declaration |
| SAM-07 | provenance | `.cvf/bindings/truth-kernel.binding.json` | `a696ddbef39870bd8b6c633c6354c61da039b2bef94d992e0bd65505ccc39666` | Kernel binding declaration and version gap |
| SAM-08 | provenance | `.cvf/bindings/truth-flow.binding.json` | `238b416f4eeb85c656b06e85545dd737a96dd57d74095c06ce5a9e4c51505b79` | Flow binding declaration and version gap |
| SAM-09 | provenance | `.env.example` | `3a369c5ed83c1618740f371cfb9772776b86451d643e89b40b07006757059667` | environment default coupling |
| SAM-10 | provenance | `apps/api/src/config.ts` | `22ae2e2f83c600bfdcf9fffd8ad948e68bc75ccb01d717ab3013247d9dc12fba` | application default coupling |
| SAM-11 | runtime candidate | `packages/cvf-bindings/src/truth-kernel.adapter.ts` | `32fbc200bc2717fc7c7c3477334590fada1d3547ccaa067ba9809d76c38189da` | local adapter versus current T8 contract |
| SAM-12 | runtime candidate | `packages/cvf-bindings/src/truth-flow.adapter.ts` | `ca3e5720fd2adece259ebf7c6722033ba90336abddb0561c52816a3852a61222` | decision semantics and continuation risk |
| SAM-13 | runtime candidate | `packages/application/src/services/governed-output.service.ts` | `6b6e63bf914d09d65fb0fcb0a3f110c08d001e5d6b71738d1cfe2efa01e3f377` | output creation after Flow decision |
| SAM-14 | runtime candidate | `packages/application/src/services/context-builder.service.ts` | `339dd7d45bda7f2c9e35bc76b11a11cb7e6767584a750d6240798894e38c0c7b` | context construction after Flow decision |
| SAM-15 | runtime candidate | `apps/api/src/middleware/cvf-governance.middleware.ts` | `830c354ca3e2d1cf09ca6ac38b1cbbd071562067919f300bc01db5a6f1baf1b8` | phase-gate response and fall-through risk |
| SAM-16 | evidence candidate | `packages/evidence/src/freeze-package.ts` | `bb6d98ce161afff12c315a1172d14eef5d68bc48e6009d863912122ddcafbd5a` | freeze evidence completeness |
| SAM-17 | test-quality | `tests/e2e/controlled-quotation.e2e.test.ts` | `7ee0122074d813427e744ed33322db425a413826872ac61a58da706b9e65eea6` | E2E naming versus actual behavior proof |
| SAM-18 | test-quality | `tests/integration/truth-kernel-binding.test.ts` | `b1801152ceba1b254ad738e09111cd07c1867ed4f527fbb848642929e3cfe8cd` | binding test versus current contract proof |
| SAM-19 | negative-proof | `tests/failure-injection/missing-review.test.ts` | `f451414a0cdfde42f84bbb1684765aa131e6065c0c6d5a62d8d5e268d618d1d6` | missing-review fail-closed evidence |
| SAM-20 | fixture | `fixtures/controlled-quotation/expected-freeze-record.yaml` | `33a25d2d28ef7502fed8b6aaf64ef652d770f0ce59ea32de0d4ef5412f7f13f7` | fixture value versus runtime proof boundary |

## Semantic Calibration Method

For each sample row:

1. Read the complete source file directly.
2. Select exactly one processing status: READ, ADAPTED, DEFERRED, REJECTED,
   NO_NEW_VALUE, or BLOCKED_UNREADABLE. A read-only evidence row may remain
   READ; an unreadable file stops the tranche.
3. Select exactly one disposition: ABSORB, ADAPT, DEFER, REJECT, BLOCK, or
   NO_NEW_VALUE.
4. Select exactly one valueClass: DOCTRINE_ADAPTED, PACKAGE_CANDIDATE,
   RUNTIME_CANDIDATE, CHECKER_CANDIDATE, NO_PACKAGE_OR_RUNTIME_VALUE, or
   REJECT_DIRECT_IMPORT.
5. Select exactly one overlapClass: CONFIRMED_EXISTING, ENRICH_EXISTING,
   NEW_FINDING, REJECT_DIRECT_IMPORT, NO_NEW_VALUE, or
   OWNER_SURFACE_NOT_FOUND.
6. Name a current CVF owner path/symbol, pending downstream owner, or explicit
   no-owner result. Do not promote a new owner.
7. Give a file-specific reason and next governed action.
8. Add an adversarial challenge that tests whether reject/defer/no-new-value
   treatment hides doctrine, package, runtime, checker, provenance, or
   negative-proof value.
9. Separate source intent from proven behavior. Tests, fixtures, constants,
   interfaces, declarations, and filenames do not prove runtime integration.

The worker must not propagate the sample rubric to un-sampled files in T0A.

## Execution Plan

1. Complete startup and pre-flight checks without writes.
2. Create the ledger skeleton only after every pre-flight expectation passes.
3. Emit and reconcile all 336 metadata rows and the aggregate receipt.
4. Emit all 13 declaration occurrence rows with candidate-only routing.
5. Read and semantically calibrate SAM-01 through SAM-20.
6. Add source-intake, external-absorption, value, overlap, reverse-owner,
   corpus, epistemic, trace, claim-boundary, and public-disposition blocks.
7. Create the checker-safe worker return with the exact changed-set and command
   evidence.
8. Run all required gates. Repair only the two worker-owned outputs.
9. Leave changes uncommitted and return for independent review.

## Evidence Requirements

The ledger must carry the literal source root, executionBaseHead, snapshot time,
enumeration/hash algorithm, 336 atomic metadata rows, aggregate receipt, 13
atomic declaration rows, 20 atomic semantic rows, corpus reconciliation,
owner/value/overlap reasoning, and a bounded `PARTIAL` verdict. The worker
return must carry starting and final `git status --short`, exact changed files,
exact commands and exit results, gate evidence, no-commit statement, and one of
the two allowed return statuses. Prior reviews are navigation evidence only;
all acceptance facts require fresh recomputation.

## Required Artifact Manifest

| Required artifact | Required content | Worker disposition at return |
|---|---|---|
| `docs/reviews/CVF_SOT3_APP_T0A_CORPUS_METADATA_AND_SAMPLE_LEDGER_2026-07-16.md` | 336 metadata rows, aggregate receipt, 13 declaration rows, 20 semantic sample rows, reconciliation, required governed blocks | exact path; CREATED or BLOCKED |
| `docs/reviews/CVF_SOT3_APP_T0A_WORKER_RETURN_2026-07-16.md` | status, scope/method/findings/risk, execution trace, delta boundary, commands, changed files, no-commit proof, return contract | exact path; CREATED |

Exactly two worker-created files are allowed. The optional completion review is
reviewer-owned and must not be created by the worker.

## Required Proof Manifest Atomic Literal Discipline

Every manifest row, changed-file row, output-path row, and command-evidence row
must carry one atomic literal path or command. Do not join multiple paths in a
single code span, wrap one literal across lines, or substitute prose such as
"the ledger above" for the exact path. Counts and hashes must appear as single
unbroken ASCII tokens.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Planned artifact | Acceptance evidence |
|---|---|---|---|
| full-corpus identity is retained | Required Metadata Freeze Method | metadata/sample ledger | 336 unique rows, 238522 bytes, aggregate match |
| sample before semantic propagation | Fixed Sample and Semantic Calibration Method | metadata/sample ledger | exactly 20 terminal sample rows |
| complete hidden-clone occurrence visibility | Complete Declaration Inventory Method | metadata/sample ledger | exactly 13 occurrence rows |
| reviewer accepts or corrects rubric | worker leaves no-commit reviewer handoff | worker return plus reviewer-owned completion review | independent audit of all 20 rows |
| T0B remains held | scope, reconciliation, and claim boundary | both worker outputs | unresolved semantic count 316 and no T0B release language |
| no source mutation | explicit forbidden scope and Git evidence | worker return | exact changed set contains only two review files |

## Corpus-To-Knowledge-Map Reconciliation

| Corpus group | Metadata coverage | Semantic coverage in T0A | Knowledge/value route | Residual obligation |
|---|---:|---:|---|---|
| all source files | 336 | 20 | sample rows only | 316 semantic rows in T0B |
| declaration occurrences | N/A with reason: occurrence inventory | candidate routing for 13 | provenance owner/drift/runtime-use candidates | terminal decisions in T0B |
| doctrine sample | included | SAM-01 through SAM-05 | doctrine/no-new-value calibration | corpus propagation in T0B |
| provenance sample | included | SAM-06 through SAM-10 | clone coupling calibration | corpus propagation and terminal decisions in T0B |
| runtime/evidence/test/fixture sample | included | SAM-11 through SAM-20 | package/runtime/checker/reject calibration | corpus propagation in T0B |

## Acceptance Criteria

- `executionBaseHead` is the clean committed T0A dispatch HEAD.
- Exactly two output paths are created and no existing file is edited.
- All 336 physical paths have one unique metadata row.
- File count, bytes, every per-file hash, and ordinal aggregate reconcile.
- All metadata rows use `METADATA_FROZEN` without semantic-completion claims.
- All 13 declaration occurrences are present with physical line and candidate
  routing; none is described as terminally resolved.
- Exactly SAM-01 through SAM-20 have complete semantic rows.
- Every sample row has one processing status, disposition, valueClass,
  overlapClass, ownerRoute, nextGovernedAction, reason, and adversarialChallenge.
- Reconciliation is metadata=336, sample=20, semantic_unresolved=316,
  declaration_occurrences=13, missing_paths=0, duplicate_paths=0.
- Corpus verdict is `PARTIAL`.
- T0B remains held.
- Worker-return full gate and all applicable documentation gates pass.
- Worktree remains uncommitted; worker returns `COMPLETE_PENDING_REVIEW`.

## Review Gate

The reviewer/closer must independently recompute file count, byte total,
aggregate, declaration count, and all 20 sample hashes; audit every sample row;
challenge all DEFER, REJECT, BLOCK, NO_NEW_VALUE, and no-owner results; verify
316 unresolved semantics remain visible; run the closure diff gate; and either
accept, repair within reviewer-owned paths, or return the tranche.

T0A acceptance calibrates T0B packet authoring. It does not automatically
dispatch T0B.

## Closure Diff Gate

| Comparison | Required reviewer result |
|---|---|
| roadmap versus work order | all T0A requirements mapped; no T0B release |
| work order versus ledger | 336/13/20/316 reconciliation and exact taxonomies present |
| work order versus worker return | exact two-file changed set, commands, status, and no-commit evidence agree |
| source snapshot versus completion claim | all counts/hashes freshly recomputed; drift is blocked, not normalized |
| semantic sample versus claim boundary | only 20 sample decisions; no full-corpus semantic claim |
| external roots versus Git diff | no external or hidden-clone mutation |

Any mismatch is a closure defect and blocks `CLOSED_PASS` or equivalent.

## Closure Checklist

The worker return must resolve every row as PASS, `N/A with reason`, or BLOCKED.

| Check | Required terminal evidence |
|---|---|
| clean execution start | executionBaseHead plus empty starting `git status --short` |
| output collision | both exact output paths absent before creation |
| metadata freeze | 336 unique rows and aggregate receipt |
| declaration inventory | 13 occurrence rows |
| sample calibration | 20 exact sample rows |
| reconciliation | 336 metadata, 20 sample, 316 semantic unresolved |
| changed set | exactly two worker-owned files |
| gates | command, exit status, and concise result |
| commit boundary | explicit no-commit statement and final `git status --short` |

## Stop Conditions

Return `BLOCKED_WITH_REASON` without a completion claim if:

- source count, total bytes, aggregate, any sample hash, or declaration count
  differs from the committed packet;
- a source or sample file is unreadable;
- a planned output path exists or another path would need editing;
- the hidden clone is missing, dirty, at a different HEAD, or has a different
  remote;
- semantic evidence requires executing the application, resolving packages,
  or inferring runtime behavior;
- any sample must be replaced or the sample size changed;
- a current CVF owner fact cannot be source-verified;
- source, hidden-clone, runtime, session, checker, registry, or public mutation
  is required;
- a required gate cannot pass within the two worker-owned files.

Do not ask the operator to choose a repair that is already inside the exact
two-output allowed scope. Repair literal/schema defects autonomously and rerun.

## Return-To-Orchestrator Conditions

Return the exact failed expectation, current safe evidence, commands run,
unchanged external-source statement, worktree status, and smallest required
packet-level correction. Do not propose reduced 50-100-file completion; the
operator/reviewer already rejected that route.

## Operator Checkpoint

N/A with reason: the operator selected the two-phase full-corpus route. The
next human/reviewer checkpoint is semantic acceptance or correction of the 20
sample rows after worker return.

## Worker Autonomy / No-Question Rule

The worker may choose read-only enumeration/hashing mechanics that reproduce
the specified algorithm and may repair only the two output artifacts until
gates pass. The worker must not widen scope, replace samples, reinterpret T0A
as T0B, or seek approval for ordinary in-scope formatting repairs.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| routing mode | `MULTI_AGENT_MULTI_ROLE` |
| intake summary | operator-authorized T0A full metadata freeze plus fixed semantic sample |
| scope classification | bounded documentation/evidence task with exactly two writable review paths |
| risk sensitivity | private-path and semantic-overclaim risk; no provider, live, secret, public-sync, or production action |
| selected role route | multi-agent route with separated dispatcher, worker, reviewer/closer, and session steward |
| escalation condition | stop and return BLOCKED_WITH_REASON on drift, collision, unreadable evidence, out-of-scope repair, or gate failure outside the two outputs |
| dispatch owner | Codex dispatcher/reviewer lane |
| execution owner | delegated source-intake worker |
| closure owner | independent reviewer/closer |
| session owner | separate session-sync steward |
| cross-role restriction | worker cannot commit, close T0A, author T0B, or update continuity |

## Legacy Absorption Coverage Index Disposition

N/A with reason: T0A processes the operator-authored post-SOT3
SOT-Application source. The Four-Surface `.private_reference/legacy` path is
named only to preserve operator source-intent chronology and is covered by its
separate accepted FSCB ledger/crosswalk. This work order performs no legacy
corpus absorption or coverage-index mutation.

## Provider Memory Authority Boundary

Provider-specific files and memories may guide navigation only. They are not
CVF source authority and must not appear as accepted Source Verification,
manifest, semantic, closure, or owner evidence. Re-verify every usable fact
against the committed packet, canonical CVF surface, or literal external file.
If no governed/source fact exists, use `BLOCKED_WITH_REASON`, identify the
missing authority, and stop the affected claim.

rawMemoryReleased=false

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | post-SOT3 operator-authored downstream copied-folder gap response |
| Upstream or source-mirror disposition | `LOCAL_OPERATOR_AUTHORED_INPUT_WITHOUT_UPSTREAM`; hidden clone is a declared dependency target, not source authority |
| Enumeration or manifest plan | T0A full physical 336-row metadata freeze using path, bytes, SHA-256, and ordinal aggregate |
| Per-file terminal-ledger plan | T0A metadata for 336 and semantic terminal decisions for exact 20; T0B retains remaining 316 |
| Owner or overlap route | sample rows route to current CVF owner, pending downstream owner, or explicit no-owner escalation |
| Value-disposition route | ABSORB, ADAPT, DEFER, REJECT, BLOCK, or NO_NEW_VALUE plus valueClass and adversarial review |
| Claim boundary | T0A partial evidence only; no source mutation, full absorption, runtime, or product claim |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | operator-named 336-file downstream copied folder |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | full 336 metadata freeze plus exact reviewer-stratified 20-file semantic sample |
| Blind-spot prevention action | preserve all file identities, enumerate all declarations, retain T0B obligation, and adversarially audit low-value/reject/defer rows |
| Residual gap | 316 semantic rows and all terminal declaration decisions |
| Blind-spot verdict | PARTIAL_T0A_ACCEPTED_T0B_REQUIRED |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | literal SOT-Application root in Scope / Target / Owner Boundary |
| Enumeration command | hidden-inclusive, no-ignore physical filesystem enumeration and exact declaration fixed-string search |
| Manifest artifact or inline manifest | `docs/reviews/CVF_SOT3_APP_T0A_CORPUS_METADATA_AND_SAMPLE_LEDGER_2026-07-16.md`, 336-row metadata table and aggregate receipt |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_SOT3_APP_T0A_CORPUS_METADATA_AND_SAMPLE_LEDGER_2026-07-16.md`, exact 20-row semantic table plus 13 declaration rows |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE; metadataState is separate |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline Overlap And Novelty Classification table plus `docs/reference/sot_three_layer/README.md` |
| Unresolved items | 316 un-sampled semantic decisions and terminal declaration dispositions |
| Completion claim boundary | T0A partial calibration; no full external absorption completion |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| 336-file metadata | reproducible corpus identity | `DOCTRINE_ADAPTED` | T0A ledger | freeze and reviewer-verify | no runtime/package claim |
| doctrine sample | downstream lifecycle and boundary claims | `DOCTRINE_ADAPTED` | future downstream owner | calibrate before T0B | no CVF Core promotion |
| domain/application sample | scoped downstream product lifecycle | `PACKAGE_CANDIDATE` | future downstream owner | calibrate package boundary before T0B | no package activation |
| binding/config sample | provenance and contract-coupling evidence | `RUNTIME_CANDIDATE` | current owner or future GAP | candidate route only | no binding validation |
| runtime-shaped source sample | behavior and continuation risks | `RUNTIME_CANDIDATE` | later T1/T2 owner map | source-verify later | no behavior proof |
| test/fixture sample | proof-quality boundaries | `CHECKER_CANDIDATE` or `REJECT_DIRECT_IMPORT` | later T3 evidence lane | distinguish fixture from production path | no test execution |
| TREEVIEW sample | navigation or latent doctrine | `NO_PACKAGE_OR_RUNTIME_VALUE` candidate | retained evidence | adversarially challenge in T0A | no package/runtime value claim |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| SOT3 doctrine references | `docs/reference/sot_three_layer/README.md` | `CONFIRMED_EXISTING` candidate | application should consume, not own | calibrate sample; ratify in T1 |
| T8/binding-shaped files | `EXTENSIONS/CVF_REFINERY/src/packet-hash/packet-hash.ts` | `REJECT_DIRECT_IMPORT` candidate | local bindings may be stale or incomplete | record evidence; no import |
| downstream application lifecycle | OWNER_SURFACE_NOT_FOUND | `OWNER_SURFACE_NOT_FOUND` candidate | possible sibling product owner | record next governed action; no promotion |
| copied tests/fixtures/navigation | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | `NO_NEW_VALUE` or `ENRICH_EXISTING` candidate | latent negative-proof or doctrine value possible | adversarial sample audit |

`OWNER_SURFACE_NOT_FOUND` is not permission to create an owner. T0A records the
candidate and routes a T0B/T1 decision.

## Reverse Architecture Projection Matrix

| Accepted value group | Catalog/GAP owner check | Disposition before T0A closure | Target source | Claim class | Evidence |
|---|---|---|---|---|---|
| downstream product doctrine | current catalog/GAP registry | `DEFER_PENDING_ACCEPTANCE` | future downstream owner or GAP | doctrine candidate | T0A sample only |
| application integration risk | current runtime and evidence owners | `DEFER_PENDING_ACCEPTANCE` | later owner update or GAP | runtime candidate | source text only |
| hidden-clone coupling | current provenance/adapter owner | `DEFER_PENDING_ACCEPTANCE` | T0B terminal route | provenance candidate | 13 occurrence rows |
| no-new-value group | current docs/package/checker owners | `NOT_APPLICABLE_WITH_REASON` until adversarial review completes | retained evidence only | negative result candidate | file-specific challenge required |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | intake authorization -> scope split -> committed T0A packet -> no-commit metadata/sample ledger -> reviewer checkpoint -> fresh T0B decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | SOT3-APP roadmap until T0A calibration and T0B corpus completion |
| Disposition | ADAPT evidence only; reject direct import |
| Claim boundary | T0A partial-evidence lane only |

## Corpus Completeness And Report Integrity

- Corpus task class: downstream SOT application intake calibration.
- Corpus root: literal SOT-Application root in Scope / Target / Owner Boundary.
- Snapshot time: worker execution start on 2026-07-16 or later.
- Enumeration command: `rg --files --hidden --no-ignore` plus filesystem-backed per-file byte/hash reads, ordinal normalized-path aggregate, and fixed-string declaration search.
- Manifest artifact or inline manifest: 336-row metadata table and aggregate receipt in the worker ledger.
- Manifest hash: `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee`.
- Processing ledger artifact or inline ledger: exact 20-row semantic table and 13-row declaration inventory in the worker ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=336; ledger_terminal=20; metadata_frozen=336; semantic_sample_terminal=20; unresolved=316; declaration_occurrences=13; exclusions=0.
- Unresolved files: 316 semantic dispositions remain T0B-owned.
- Declared exclusions: none from metadata; 316 files are intentionally outside T0A semantic sampling and remain enumerated.
- Unreadable or unsupported files: zero required; any occurrence blocks T0A.
- Aggregation check: file_count=336; total_bytes=238522; aggregate matches; missing_paths=0; duplicate_paths=0.
- Drift check: worker recomputes every file hash, aggregate, sample hash, declaration count, and hidden-target metadata.
- Output traceability: every physical file maps to metadata; each sample/declaration maps to path, hash or line, decision, and evidence.
- Adversarial verification: independent reviewer audits all 20 sample rows and every reject/defer/block/no-new-value/no-owner result.
- Corpus verdict: PARTIAL

## Epistemic Process Block

Expected Result / Prediction: the source preserves useful downstream lifecycle
intent but mixes doctrine, copied contracts, runtime-shaped code, fixtures,
tests, and hidden-clone coupling that require owner-aware semantic calibration.

Evidence Comparison: T0A compares that prediction against all 336 objective
file identities, all 13 current declaration occurrences, and the exact
reviewer-selected 20-file cross-family sample.

Contradiction Or Gap Disposition: record file-specific evidence and use
DEFER, REJECT, BLOCK, NO_NEW_VALUE, OWNER_SURFACE_NOT_FOUND, or
BLOCKED_WITH_REASON honestly. Do not infer runtime behavior.

Claim Update: T0A may calibrate a rubric and identify candidate owner routes.
Only independent review may accept it for fresh T0B packet authoring.

## Finding-To-Governance Learning Disposition

If execution exposes a repeated, non-obvious dispatch or gate defect, the
worker must report it in the return but cannot edit ADIF. The reviewer decides
whether a separate ADIF entry is required before closure. Source-specific
semantic disagreements are evidence findings, not automatic ADIF defects.

## Source Snapshot Carry-Forward Boundary

The ledger must retain exact enumeration/hash algorithm, executionBaseHead,
source snapshot time, aggregate receipt, sample IDs/hashes, and declaration
search token so T0B can detect drift without reusing semantic conclusions as
fresh evidence. Any T0B dispatch must recompute the corpus before propagation.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| applicability | NOT_APPLICABLE_WITH_REASON |
| reason | T0A creates two governed markdown evidence files only and does not create or alter application storage, cache, database, source mirror, index, or generated aggregate layout |
| owner boundary | existing `docs/reviews/` governed artifact family |
| future trigger | later durable source-mirror or application-storage work requires fresh GC-018 and source verification |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | committed T0A packet and two uncommitted worker outputs | read external roots; write only exact review outputs; no commit | metadata, hashes, declarations, sample rows, gates | local filesystem and read-only Git metadata | ACTIVE_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | no downstream adapter ratified | no CLI/MCP ingress, execution, dependency resolution, or external-agent product claim | explicit absence of adapter proof | separate source-verified adapter roadmap | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`External knowledge absorption`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "External knowledge absorption" --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defects: ADIF-0016; ADIF-0020; ADIF-0021; ADIF-0027

| DefectId | Dispatch application |
|---|---|
| ADIF-0016 | reusable metadata/sample/declaration schemas and the T0B residual obligation are explicit |
| ADIF-0020 | worker reads output-applicable checker sources before writing and records the result |
| ADIF-0021 | source-intake applicability uses the exact marker, section, and required fields |
| ADIF-0027 | reverse owner/GAP routing is explicit and no candidate is prematurely promoted |

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read checker source for its path, docType, and
conditional evidence class.

| Output artifact | Required checker-source read-ahead result |
|---|---|
| metadata/sample ledger under `docs/reviews/` | derive exact review headings, source-intake fields, absorption/value/overlap/reverse-routing blocks, corpus fields/statuses, epistemic fields, trace labels, public disposition, and partial claim terms |
| worker return under `docs/reviews/` | derive worker-return status/self-declaration/work-order markers, required headings, trace/delta labels, changed-files/commands/no-commit evidence, conditional controls, and full-gate shape |

Do not pre-list fake `##` headings before the real section and do not write PASS
before the matching command executes.

## Agent Handoff Contract Control Block

archive exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

Stable front door: `docs/reference/agent_handoff/README.md`, section
`Central Core`.

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher authors committed packet; delegated worker executes and returns without commit; independent reviewer/closer audits and commits accepted material; session-sync steward updates continuity separately |
| phase | `DISPATCH_AUTHORING`; `EXECUTION`; `CLOSURE`; `SESSION_SYNC` |
| baseHeadFor(phase) | dispatchBaseHead=`e7f45e120`; executionBaseHead=worker captures clean committed dispatch HEAD; closureBaseHead=reviewer captures worker execution base |
| changedSetScope(phase) | dispatch=roadmap plus paired GC-018/work order; execution=exact two worker outputs; closure=accepted worker outputs plus reviewer-owned closure paths; session-sync=protected continuity paths only |
| traceScope(phase, actor) | each actor records only phase-local paths, commands, hashes, HEAD, diff, status, and gate evidence |
| commitOwner(phase) | dispatcher commits dispatch; worker forbidden; reviewer/closer commits accepted material; session-sync steward commits continuity separately |
| crossBatchIsolation | prior FSCB and T0 blocker decisions are committed; T0A begins from a clean dispatch HEAD and excludes T0B/later work |
| nextMoveSurfaces | worker cannot edit; reviewer may release only fresh T0B packet authoring once T0A is accepted; session steward updates state once material closure is accepted |
| closerOwner | independent reviewer/closer designated above |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_APP_T0A_COMPLETION_2026-07-16.md` |
| reviewerOwnedClosurePaths | accepted worker ledger; accepted worker return; SOT3-APP roadmap; this work-order status/closure evidence; T0A completion review |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_SOT3_APP_T0A_WORKER_RETURN_2026-07-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Worker return must include these always-required section names and evidence
terms:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Checker Source Read-Ahead Block
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- Claim Boundary
- git status --short
- Changed Files
- Command Evidence
- No-Commit Statement
- executionBaseHead

Worker return must include or explicitly resolve these conditional controls:

- Source Intake Decision Packet
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Work-Order Fulfillment Manifest
- Machine Closure Package

Return vocabulary:

- success: `COMPLETE_PENDING_REVIEW`
- blocked: `BLOCKED_WITH_REASON`
- no commit: `WORKER_MUST_NOT_COMMIT`

## Verification Commands

Replace `<executionBaseHead>` with the captured committed dispatch HEAD.

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_source_intake_decision_packet_preflight.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_core.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_value_conversion.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_overlap_discipline.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_knowledge_intake_routing.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_governed_artifact_checker_read_ahead.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git status --short
```

No runtime, build, typecheck, test, CI, server, browser, provider, or live-proof
command is authorized.

## Near-Threshold Owner Maintainability Plan

The worker ledger may be large because 336 atomic metadata rows are required.
Keep narrative compact and tables mechanically regular. If the governed file
size guard reports a threshold defect, stop and return to the reviewer; do not
split the required atomic ledger across unplanned paths or compress evidence
by deleting rows.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIRS; Dispatch Prompt Envelope; Role:; Canonical packet:; Commit mode:; executionBaseHead; Current-time notes:; Do-not-misread notes:; Required first actions:; Return contract:; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Negative Search And Collision Discipline; Evidence Reuse And Encoding Plan; Source Intake Decision Packet; Work-Order Fulfillment Manifest; Required Proof Manifest Atomic Literal Discipline; Roadmap-To-Work-Order Trace Matrix; Acceptance Criteria; Review Gate; Closure Diff Gate; Worker Autonomy / No-Question Rule; Legacy Absorption Coverage Index Disposition; Provider Memory Authority Boundary; External Repository Absorption Entry Control; Mandatory Blind-Spot Control Block; External Absorption Core; External Absorption Value Conversion Matrix; Overlap And Novelty Classification; Reverse Architecture Projection Matrix; External Knowledge Intake Routing; Corpus Completeness And Report Integrity; Dual Agent Surface Matrix; ADIF Defect Registry Disclosure; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; COMPLETE_PENDING_REVIEW; BLOCKED_WITH_REASON; WORKER_MUST_NOT_COMMIT; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm exact dispatch and worker-output shape after checker-source review; gates are proof, not first discovery |
| claimBoundary | checker conformance does not prove corpus semantics, provenance safety, runtime behavior, or product quality |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id SOT3-APP-T0A --title "SOT3 Application Corpus Freeze And Semantic Calibration" --date 2026-07-16 --base e7f45e120 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SOT3-APP-T0 R1 scope-blocker review material commit 55007483c" --stdout --include-worker-return-skeleton` |
| generatedProfile | source-intake plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact dependencies, operator source intent, 336-file snapshot, 13-declaration baseline, fixed 20-path sample, two-output manifest, partial-corpus reconciliation, and T0B hold |
| checkerReadAheadConfirmation | dispatch, handoff, worker-return, ADIF, source-intake, absorption, corpus, trace, encoding, and read-ahead checker sources reviewed |
| docOnlyNewFields | metadata, sample, declaration, and aggregate fields listed above |
| claimBoundary | dispatch-authoring provenance only |

## Dispatch Packet Authoring Learning Promotion

The prior single-pass packet failed at execution sizing, not source value. This
packet promotes the reusable correction into the governed shape: retain
full-corpus objective metadata, fix a reviewer-selected semantic sample, keep
the un-sampled semantic denominator explicit, and require a reviewer checkpoint
before full-corpus propagation. No ADIF mutation is needed because the existing
ADIF disclosure already covers reusable schema and dispatch-shape discipline.

## Next-Tranche Audit Mini-Package

T0B may be authored only after a reviewer-owned T0A completion review records:

- independently recomputed 336-file/238522-byte aggregate parity;
- independently recomputed 13 declaration occurrences;
- exact 20-row semantic audit with corrections resolved;
- accepted disposition/value/overlap/owner rubric;
- explicit semantic_unresolved=316 handoff;
- fresh source snapshot and dependency-release evidence;
- a new GC-018/work order and clean dispatch base.

This mini-package is an authoring prerequisite, not T0B release.

## Export Surface Decision

No export surface is authorized. Both worker outputs remain private provenance
review artifacts. Any later public-safe projection requires a separate
public-sync packet and must not expose private paths or operator-only evidence.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | SOT3-APP-T0A packet authoring, 2026-07-16 |
| Working directory | repository root |
| Command or tool surface | governed reads, direct filesystem enumeration/hashing, read-only hidden-target Git metadata, ADIF resolver, scaffold preview, apply_patch, and governance gates |
| Target paths | SOT3-APP roadmap, paired T0A GC-018, and this work order |
| Allowed scope source | operator instruction, scope decision `55007483c`, and clean continuity release `e7f45e120` |
| Before status evidence | clean worktree at dispatchBaseHead `e7f45e120`; all planned new artifact paths absent |
| After status evidence | exact three-path dispatch packet pending pre-dispatch verification and material commit |
| Diff evidence | `git diff --name-status`; `git diff --check`; range gates from `e7f45e120` |
| Approval boundary | T0A packet authoring and dispatch only |
| Claim boundary | no worker execution, semantic acceptance, T0B release, source/runtime/public mutation, or product proof |
| Agent type | dispatcher |
| Invocation ID | `sot3-app-t0a-dispatch-2026-07-16` |
| Expected manifest | SOT3-APP roadmap; paired T0A GC-018; paired T0A work order |
| Actual changed set | must match the exact three-path manifest before material commit |
| Manifest delta | MATCH required |
| Deletion or rename disposition | N/A with reason: none planned |

## Reviewer Closure Evidence

| Check | Reviewer result |
|---|---|
| execution base | `120c0f90a`; clean before worker writes |
| worker changed set | exact two planned untracked review artifacts |
| metadata | 336 physical files, 238522 bytes, exact per-file equality, aggregate `bbf4a91d7fb50134c711ffef8af2a6107105fc0aae9b341a0ca3896ce58534ee` |
| declarations | 13 exact source path/line rows; DEC-05/06/08 repaired to `targetExists=false` |
| semantic sample | exact SAM-01 through SAM-20 independently audited; SAM-06/07/08/12/15 wording repaired |
| reconciliation | metadata=336; sample=20; semantic_unresolved=316; declarations=13; missing declared extension targets=3 |
| claim boundary | T0B packet authoring only; no T0B execution or source/runtime/public mutation |
| completion review | `docs/reviews/CVF_SOT3_APP_T0A_COMPLETION_2026-07-16.md` |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | SOT3-APP-T0A documentation-only metadata/declaration/sample dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no application/runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no application/runtime action is executed or observed |
| invocationBoundary | manual filesystem reads, hashing, parsing, read-only Git metadata, and governance checks only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, binding resolution, or agent coding control |
| claimLanguage | objective source identity and bounded semantic-calibration evidence only |
| forbiddenExpansion | runtime/provider/live/public/package/Web/MCP/checker behavior requires fresh source-verified authorization |

## Current Runtime Freshness Verification

The closure's non-use statement is scoped to this T0A execution. Current Git
evidence shows only the five reviewer-owned governed documentation paths, and
the worker/reviewer operation traces contain enumeration, hashing, source
reads, read-only Git metadata, documentation lookup, and governance gates.
No application, runtime, test, server, browser, or live-provider command was
run. This is not a claim that such code is absent from SOT-Application.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIRS` | PASS |
| Worker ledger | `docs/reviews/CVF_SOT3_APP_T0A_CORPUS_METADATA_AND_SAMPLE_LEDGER_2026-07-16.md` | `Status: ACCEPTED_BY_REVIEWER_WITH_REPAIRS`; 336 metadata; 20 samples; 316 unresolved; 13 declarations; 3 missing targets | PASS_WITH_REPAIR |
| Worker return | `docs/reviews/CVF_SOT3_APP_T0A_WORKER_RETURN_2026-07-16.md` | `Status: ACCEPTED_BY_REVIEWER_WITH_REPAIRS` | PASS_WITH_REPAIR |
| Completion or reviewer artifact | `docs/reviews/CVF_SOT3_APP_T0A_COMPLETION_2026-07-16.md` | `Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIRS` | PASS |
| Roadmap state | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | `Status: T0A_CLOSED_PASS_BOUNDED_T0B_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | N/A with reason: no registry JSON is required or changed | no generated registry mutation | PASS |
| Registry Markdown | N/A with reason: no registry Markdown is required or changed | no registry mutation | PASS |
| External evidence digest | N/A with reason: no external benchmark or live digest is authorized | no digest created | N/A with reason |
| System loop interlock | N/A with reason: no runtime or system-loop source changed | documentation-only closure | N/A with reason |
| Session continuity | active session front door, state, and handoff | separate sync after material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| T0A evidence acceptance | 336 metadata rows, 20 semantic rows, 316 unresolved semantics, 13 declarations, and 3 missing declared targets | PASS |
| Runtime receipt evidence | N/A with reason: no runtime receipt was authorized | no runtime action occurred | N/A_WITH_REASON |
| Query acceptance evidence | N/A with reason: T0A performs no acceptance query | no query receipt exists or is claimed | N/A_WITH_REASON |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private external-source intake dispatch and private worker outputs; no
public-sync authorization or public-safe artifact set exists.

## Claim Boundary

This work order authorizes exactly one no-commit T0A worker execution producing
two review artifacts: metadata for all 336 files, inventory for every current
hidden-clone declaration occurrence, and semantic calibration for the exact 20
sample files. It does not authorize semantic disposition for the other 316
files, terminal declaration decisions, T0B, source or hidden-clone mutation,
dependency install/sync, binding validation, build, typecheck, test, CI,
runtime, API, server, browser, provider/live proof, Catalog/GAP/ADIF/session or
checker mutation, package activation, CVF Core promotion, public-sync, worker
commit, full absorption, production readiness, or user-value claims.
