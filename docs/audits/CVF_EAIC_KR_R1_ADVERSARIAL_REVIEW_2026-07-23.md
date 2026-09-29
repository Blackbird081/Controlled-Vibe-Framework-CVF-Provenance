# CVF EAIC-KR R1 Adversarial Review (Independent Reviewer Pass)

Memory class: FULL_RECORD

docType: audit

Status: REVIEW_COMPLETE_APPROVE_WITH_REPAIRS

Date: 2026-07-23

Review type: independent adversarial review, read-only. No file under review
was edited, staged, or committed by this review.

## Purpose

Independently challenge the provenance, corpus integrity, owner mapping,
claim boundaries, T2 impact, and proposed next move of the EAIC-KR-R1 intake.

## Target / Source

The target is the primary intake audit named below. Sources are its manifest,
two file ledgers, corpus registry entry, pinned Brainless mirror and index,
the two copied-pack roots, and the held EAIC-KR T2 baseline.

## Scope / Methodology

Read-only local recomputation of counts, hashes, exact-content intersection,
negative searches, mirror identity, source declarations, owner-path existence,
and T2 hold state. No reviewed artifact was edited by the independent reviewer.

## Reviewer Disclosure

| Field | Value |
|---|---|
| Provider | Anthropic (Claude Code CLI session) |
| Model | claude-opus-4-8 |
| Effort | high; independent recomputation of counts, hashes, SHA-256 content-match set, and negative searches; targeted source reads |
| Execution surface | local filesystem and local Git worktree only, read-only; no clone, no fetch, no network beyond inspecting the already-pinned local mirror |
| Internal helper/subagent usage | none; no delegation, no recursive dispatch |
| Usage/quota evidence | UNKNOWN (not exposed to this review session) |

## Review Target

Primary: `docs/audits/CVF_EAIC_KR_R1_CVF_23_07_EXTERNAL_REPOSITORY_INTAKE_AUDIT_2026-07-23.md`

Supporting: the manifest, the two file ledgers, the corpus registry entry, and
`.private_reference/source_mirrors/INDEX.md`.

## Independently Recomputed Evidence

| Claim in the audit under review | Independent recomputation performed | Result |
|---|---|---|
| 18 Conversation-Resilient Governance files; 213 Interaction Projection files; 231 total | filesystem `find`/enumeration over both roots | MATCHES: 18, 213, 231 |
| Both file ledgers contain matching per-root row counts | parsed both ledger JSON files, counted rows | MATCHES: 18 and 213 rows |
| Brainless mirror pinned at commit `4c5d5ab6...`, tree `080fe561...`, 321 tracked files, clean | `git rev-parse HEAD`, `git rev-parse HEAD^{tree}`, `git ls-files \| wc -l`, `git status --porcelain` inside the mirror | MATCHES exactly; mirror is clean; no `.gitmodules` |
| Disposition aggregate: ADAPT 112, CHECKER_CANDIDATE 14, DEFER 50, NO_PACKAGE_OR_RUNTIME_VALUE 11, PACKAGE_CANDIDATE 41, RUNTIME_CANDIDATE 3 | recomputed from raw `[relativePath, disposition, overlapClass]` rows in both ledgers | MATCHES exactly, sum 231 |
| Overlap aggregate: CONFIRMED_EXISTING 65, ENRICH_EXISTING 147, NEW_FINDING 8, NO_NEW_VALUE 11 | same recomputation | MATCHES exactly, sum 231 |
| Manifest hash `688e5935...` reproducible from `sorted-paths-newline-joined-with-trailing-newline` | recomputed sha256 over both roots via full paths and via ledger-relative paths, forward-slash, Python codepoint sort | DOES NOT MATCH either variant tried. Not proven wrong -- the exact path form (root-relative vs full, separator) and collation order (PowerShell `Sort-Object` locale vs Python codepoint sort) are not pinned in the manifest, so this reviewer could not deterministically reproduce the recipe. Flagged as a reproducibility gap, not a disproven claim. |
| Zero exact-content SHA-256 matches between non-empty upstream files and non-empty Interaction Projection files | hashed all 321 upstream tracked files (297 distinct non-empty hashes) and all Interaction Projection files (209 non-empty, 209 distinct hashes); intersected hash sets | MATCHES: 0 common hashes, corroborating "separately authored pack" |
| Zero matches for `receipt`, `cumulative envelope`, `admission owner`, `governed event`, `cost boundary`, `retry diagnosis`, `process tree` in the Brainless mirror | `git grep -il` for each of the 7 terms across tracked mirror files | MATCHES: 0 hits for all 7 terms |
| Upstream `LICENSE` is MIT, copyright 2026 Ben Swerdlow; README describes shadcn components recreating Claude Code/Codex/Grok terminal UIs; `references/captures/` and `registry/` are real tracked paths | read `LICENSE` and `README.md` at pinned HEAD; listed tracked paths under `references/captures/` | MATCHES on all points |
| All 8 named owner-surface target paths exist (T2 baseline, invocation-control reassessment, three Guard Contract contracts, boundary-first doctrine, agent-workspace design standard, external-absorption core standard) | existence check on each named path | MATCHES: all 8 exist |
| T2 remains held behind four unresolved operator decisions (admission, identity, cumulative envelope, unknown usage) | read `docs/baselines/CVF_GC018_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_2026-07-23.md` | MATCHES: all four rows are `HOLD_UNSATISFIED` / `PROPOSED_NOT_RATIFIED`; baseline states no `HOLD_UNSATISFIED` row may be read as released |
| Interaction Projection foundation files self-declare no runtime/authority claim and name Brainless as reference-only | read `00_FOUNDATION/AUTHORITY_VS_PROJECTION.md` and `00_FOUNDATION/EXTERNAL_SOURCE_PROVENANCE.md` | CORROBORATES: both files state `Runtime implementation claim: NONE`, `CVF authority: None`, `Source imported: None`, and list explicit "Not adapted" items (provider authority, session-wide permission defaults, raw reasoning, third-party code) |

## Findings / Position

Position: `APPROVE_WITH_REPAIRS`.

### Material Findings

| ID | Severity | Claim challenged | Evidence inspected | Finding | Required repair |
|---|---|---|---|---|---|
| RV-01 | MEDIUM | Manifest hash `688e5935...` is reproducible from the stated `hashInput` | Recomputed sha256 with two plausible path conventions; neither matched | The hash cannot be independently reproduced by a third party without the exact path form and collation rule. Every count the hash is meant to protect reconciled exactly by direct recomputation, so this is a documentation gap, not a proven integrity failure. | Pin the exact hash recipe in the manifest: path form (root-relative, forward-slash only), sort order (ordinal/codepoint, not locale), and encoding. |
| RV-02 | LOW | Audit's "Ledger terminal statuses" line (READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE) matches the ledgers | Parsed `rowShape=[relativePath, disposition, overlapClass]` in both ledgers; actual disposition values are ADAPT/PACKAGE_CANDIDATE/CHECKER_CANDIDATE/RUNTIME_CANDIDATE/DEFER/NO_PACKAGE_OR_RUNTIME_VALUE, and NO_NEW_VALUE lives in the overlapClass column | The audit prose names a status vocabulary that does not literally match the ledger's two-column field values. Aggregate counts are correct; a reader reconciling by field name rather than by count would be misled. | Align audit prose to the ledger's actual disposition + overlapClass vocabulary, or explicitly state the prose line is a superset mapping, not a literal field list. |
| RV-03 | LOW | Corpus verdict `COMPLETE_WITH_DECLARED_EXCLUSIONS` alongside `exclusions=0` in the reconciliation line | Compared `declaredExclusions` (3 items) against the reconciliation line | Two of the three declared "exclusions" are scope caveats (no execution; no line-by-line semantic certification), not file exclusions. Only the 321-file mirror is a genuine out-of-manifest exclusion. `exclusions=0` is correct for files but reads as tension against the word "EXCLUSIONS" in the verdict. | Optional: separate "scope boundaries" from the one true corpus exclusion so the verdict and the zero-exclusions reconciliation are not read as contradictory. |

None of RV-01 through RV-03 change the terminal decision or the T2 hold. All are documentation-integrity repairs, not evidence reversals.

## Risk / Corrective Action

The material risk is evidence that is numerically correct but not independently
reproducible or vocabulary that appears to describe literal ledger fields when
it does not. Apply RV-01 through RV-03 before R1B so downstream documentation
inherits a deterministic hash recipe and unambiguous corpus terminology.

## Overclaims

NONE that are blocking. The `_CANDIDATE` disposition suffixes
(`PACKAGE_CANDIDATE`, `RUNTIME_CANDIDATE`, `CHECKER_CANDIDATE`) could be
misread as semantic certification, but the audit repeatedly and explicitly
bounds them as planning/routing labels, not certification (manifest
`declaredExclusions`, the Corpus Completeness block, and the Checker
Source Read-Ahead claim boundary all state "no line-by-line semantic
certification"). The suffix itself signals non-terminal semantic commitment.
This defuses the concern that terminal classifications overstate semantic
coverage.

## Underclaims Or Missed Value

- The audit does not cite that the Interaction Projection pack's own
  foundation files (`AUTHORITY_VS_PROJECTION.md`,
  `EXTERNAL_SOURCE_PROVENANCE.md`) self-declare `Runtime implementation
  claim: NONE`, `CVF authority: None`, `Source imported: None`, and
  explicitly list what was "Not adapted" from Brainless (provider authority
  semantics, session-wide permission defaults, raw reasoning display,
  third-party code/dependencies). This is stronger corroboration of the
  operator attestation and the authority/projection separation than the
  audit currently uses. Citing it in a future revision would harden
  R1-F02/R1-F06 and the provenance verdict. This strengthens rather than
  weakens the audit's existing position; it is not a defect.

## Provenance Verdict

- Brainless: SOUND. Mirror integrity, license, README, tracked-path claims,
  the zero-exact-content-match result, and the seven zero-hit negative
  searches were all independently reproduced.
- CVF_INTERACTION_PROJECTION: correctly positioned as operator-authored
  secondary interpretation; its own provenance file corroborates the
  operator attestation.
- Conversation-Resilient Governance: correctly blocked from direct import;
  no upstream URL, authorship declaration, or license found locally.

## Owner-Surface Verdict

- Duplicate-plane risk: low; the audit opens no new plane and routes all
  accepted value into eight existing, verified-to-exist owner surfaces.
- Existing-owner mapping quality: high; every named target path exists.
- Unresolved owner decisions: correctly disclosed (Conversation-Resilient
  Governance provenance; final schema owner for trajectory/decision-record
  fields; operator decisions EAIC-T2-D1 through D4).

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Brainless UI and capture evidence | `docs/audits/CVF_EAIC_KR_R1_CVF_23_07_EXTERNAL_REPOSITORY_INTAKE_AUDIT_2026-07-23.md` | CONFIRMED_EXISTING | independently confirms the audit's bounded upstream interaction-pattern claims | retain as pinned source evidence |
| Interaction Projection governance semantics | `docs/baselines/CVF_GC018_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_2026-07-23.md` | ENRICH_EXISTING | supplies secondary vocabulary but no enforcement or operator policy | retain for R1B without releasing T2 |
| Conversation-Resilient Governance provenance | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | upstream, authorship, and license evidence remain absent | block direct import and keep visible |

## T2 Impact

Independently confirmed against
`docs/baselines/CVF_GC018_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_2026-07-23.md`:
all four operator decisions (admission, identity binding, cumulative
envelope, unknown usage) remain `HOLD_UNSATISFIED` / `PROPOSED_NOT_RATIFIED`.
That baseline states no `HOLD_UNSATISFIED` row may be interpreted as
released. This corpus supplies vocabulary and secondary evidence only; it
contains no admission owner, no process binding, no cumulative-aggregate
enforcement, and no runtime proof. T2 must remain held. This review changes
none of EAIC-T2-D1 through D4 and does not release the hold.

## Decision / Recommendation

`REPAIR_R1_AUDIT_THEN_R1B`

R1B (documentation-only EAIC-KR T2 evidence supplement) is the correct
highest-value bounded next move; no higher-value bounded alternative was
found. The RV-01 through RV-03 repairs are documentation-integrity fixes,
not blockers to the underlying decision, and should land in the R1 audit
before or alongside R1B so the supplement inherits a name-consistent
evidence base.

## Claim Boundary

This review is read-only and independent. It does not authorize
implementation, dispatch of any tranche, CLI/MCP invocation,
provider/API/account/subscription use, source or capture-harness execution,
dependency install, build, network or browser action, public-sync, commit,
or push. It does not release EAIC-KR T2 and does not lift the global
CLI/MCP invocation moratorium. It authorizes only: recording these findings,
and the operator's own decision to accept the underlying scan and optionally
author R1B under the existing hold. Machine-gate compliance is not semantic
approval. Where a claim could not be deterministically reproduced locally
(RV-01), it is marked as a reproducibility gap, not inferred as pass or
fail.
