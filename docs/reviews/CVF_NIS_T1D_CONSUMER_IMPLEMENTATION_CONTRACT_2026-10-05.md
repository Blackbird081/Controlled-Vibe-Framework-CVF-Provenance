# CVF NIS T1D Consumer Implementation Contract

Memory class: FULL_RECORD
Status: PROPOSED_PENDING_LOCAL_REVIEW
Date: 2026-10-05
docType: reference
Batch ID: CVF-NIS-T1D
Applies to: the existing Intent-to-Spec review consumer for the `app_builder_complete` template (non-coder spec review, save and reopen).
rawMemoryReleased=false
executionBaseHead: a27c13fa7a30fbc76b755aac539ec65e6dcae49d
providerExecutionAuthority: FORBIDDEN

## Purpose

Give Local one implementation-ready contract for a bounded change to the existing review consumer: a user-declared ledger of unknown, conflict and delegated items, with an effective-decision projection, source and revision invalidation, and a separate unresolved summary, without changing the meaning of viewed confirmation and without relaxing the strict saved-file checks. The contract is a proposal. Its write paths are a proposed envelope, not authority; Local decides and issues any implementation work order.

## Scope / Applies To

In scope: the data shape of an open item, how it is created, edited, invalidated and rendered, which schema string and key sets a saved candidate uses, how legacy candidates stay byte-identical and readable, the exact proposed write paths, the planned acceptance oracles, the rollback boundary, the alternatives rejected, and the choices left to Local with a selected default.

Out of scope: any product edit, test run, store or auth change, upstream command, script or install, a Spec Kit runtime, design, plan, tasks or consistency artifacts, an automatic parser of prose, any build-ready certificate, real data, public sync and parked lanes. Cost is UNKNOWN; provider calls are zero.

## Target / Source

Target owners (existing): `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts`, `.../src/lib/intent-spec-confirmation.ts`, `.../src/lib/intent-spec-acceptance.ts`, `.../src/components/IntentSpecReview.tsx`. Capability evidence: `docs/reviews/evidence/cvf-nis-t1d-capability-assessment-2026-10-05.json` (selected pinned Spec Kit files, per-file ledger, native, pattern and runtime dispositions). Planned oracles: `docs/reviews/evidence/cvf-nis-t1d-acceptance-plan-2026-10-05.json`. Predecessor: `docs/reviews/CVF_NIS_T1C_BUILDER_HANDOFF_VALUE_PROOF_COMPLETION_2026-10-05.md` Findings / Position and Minimum Next Delta; `docs/reviews/CVF_NIS_T1B_D_INTEGRATED_REVIEW_PERSISTENCE_COMPLETION_2026-10-05.md`.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Review state has five keys and decisions have five keys; both are checked by exact key set | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-acceptance.ts | L15-L19, L28, L34 | object, checkReview | strict candidate.v1 acceptance | ACCEPT |
| Candidate embeds the whole state and the draft built from it | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-confirmation.ts | L36-L42 | createSpecConfirmationCandidate | candidate payload | ACCEPT |
| Acceptance rebuilds the draft with the current builder and compares bytes | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-acceptance.ts | L88 | prepareIntentSpecAcceptance | exact reconstruction | ACCEPT |
| Payload has exactly seven keys; schema and scope are exact literals | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-acceptance.ts | L76-L79 | prepareIntentSpecAcceptance | candidate.v1 literals | ACCEPT |
| Confirmation requires acknowledgement and zero pending decisions | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-confirmation.ts | L32-L34 | createSpecConfirmationCandidate | confirmation gate | ACCEPT |
| Stale handling flags decisions by their mapped fields and all answered decisions for an unmapped change | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts | L81-L97 | synchronizeIntentSpecReview | revision invalidation | ACCEPT |
| A decision update resets its own reconfirmation flag and source snapshot | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts | L99-L116 | updateReviewDecision | decision update | ACCEPT |
| Reopen returns stored draft and metadata without rerunning the review validator | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review-api.ts | L106-L129 | handleReadReview | reopen route | ACCEPT |
| Readiness builder has no review input and runs inside the exporter before the review hook | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-export-portable-handoff.ts | L7-L12 and SpecExport.tsx L775, L950-L951 | buildPortableAgentHandoffReadiness | readiness section | ACCEPT |
| Unknowns inside prose do not change pending status; conflict resolution appears only in the appendix | CURRENT_SOURCE | docs/reviews/CVF_NIS_T1C_BUILDER_HANDOFF_VALUE_PROOF_COMPLETION_2026-10-05.md | L28-L39 | Findings / Position | T1C Local disposition | ACCEPT |
| Upstream represents unknowns as inline markers, capped at three, replaced on resolution | UPSTREAM_PINNED_SOURCE | .private_reference/source_mirrors/github__spec-kit/templates/commands/specify.md | L124-L129, L231 | NEEDS CLARIFICATION policy | upstream dependency read 1 | ACCEPT |
| Upstream clarify overwrites the earlier statement and caps questions at five | UPSTREAM_PINNED_SOURCE | .private_reference/source_mirrors/github__spec-kit/templates/commands/clarify.md | L129-L138, L195-L196 | integration step | upstream selected file | ACCEPT |
| Upstream marker is reviewer-owned and unversioned; a human can override the gate | UPSTREAM_PINNED_SOURCE | .private_reference/source_mirrors/github__spec-kit/templates/commands/implement.md | L56-L88 | checklist gate | upstream dependency read 2 | ACCEPT |

## Checker Source Read-Ahead Block
| Field | Value |
| --- | --- |
| applicableCheckersRead | governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_external_absorption_overlap_discipline.py; governance/compat/check_epistemic_process_packet.py; governance/compat/check_equivalence_claim_evidence.py; governance/compat/check_governed_file_size.py |
| literalTokensReviewed | reference headings Purpose, Scope or Applies To and Claim Boundary; Overlap And Novelty Classification columns and allowed disposition tokens; epistemic markers Expected Result, Evidence Comparison, Contradiction, Claim Update; Source Verification Block columns |
| gateRunPurpose | confirmation and evidence that the declared shapes hold after writing; not first discovery of the shapes |
| claimBoundary | covers authoring shapes only and certifies no source fit or contract outcome |

## Contract

### Selected route

Native extension of the existing owners (route NATIVE in the assessment). Pattern value is limited to vocabulary and is rewritten in CVF wording. No upstream runtime, command, script, template text or package is used. Native does not require a prior failure of another route; each route was assessed independently in the assessment file.

### Data model

New pure helper module `intent-spec-open-items.ts` (no I/O) defines the shape and rules. Each item is stored nested under the decision it is linked to.

| Field | Rule |
|---|---|
| id | `U` or `C` followed by 1 to 99, assigned by the helper from the kind, unique across the whole review, never reused while the item exists |
| kind | `UNKNOWN` or `CONFLICT` |
| text | what is unknown or what conflicts; 1 to 2000 characters; a placeholder-only value is refused with the same placeholder list the decision check uses |
| sourceFields | 0 to 6 distinct field ids of the current brief; a `CONFLICT` needs at least two; may cite fields outside the linked decision's own mapping |
| sourceValues | snapshot of the cited fields' text at record or reconfirm time; keys equal sourceFields |
| status | `OPEN`, `RESOLVED` or `DELEGATED` |
| resolution | required and non-empty only when `RESOLVED`; otherwise the empty string |
| delegation | required and non-empty only when `DELEGATED`: the boundary the user allows the builder to decide inside; otherwise the empty string |
| needsReconfirmation | true when a cited source changed after the snapshot; stored candidates require false |

A decision carries `openItems` only when it has at least one item; the key is absent otherwise. Caps are fail-closed safety bounds, never a quota: at most 50 items per review; the 51st is refused, not dropped. There is no minimum and no maximum expected count; absence of an item is not a defect and is never demanded before the user supplies it.

### Behavior rules

1. Source invalidation. `synchronizeIntentSpecReview` compares each item's snapshot with the current text of its own cited fields and sets `needsReconfirmation` (sticky) when they differ. Existing decision rules, including the all-decisions rule for an unmapped change (T1C accepted it), are unchanged. An item without cited fields never becomes stale from a source change.
2. Updates. `updateReviewDecision` accepts an optional `openItems` change. An items-only change keeps the decision's answer, disposition, reconfirmation flag and source snapshot untouched, bumps the revision and clears the acknowledgement. It stores only a valid item set; an invalid set leaves the state unchanged, and the component pre-validates with the helper to show the reason. Without the items-only rule, an item edit would silently clear a decision's stale flag (the existing update resets it).
3. Pending. A decision with any stale item counts as needing review. Item status `OPEN`, `RESOLVED` or `DELEGATED` never counts as pending. The decision-level `CONFLICT` and `OPEN` dispositions keep blocking confirmation exactly as before; an explicit item is the structured way to carry a known conflict or unknown forward while keeping draft confirmation usable.
4. Viewed confirmation. Unchanged: acknowledgement is bound to the revision. It is independent of item counts and means only that this revision was viewed.
5. Delegation. Delegation records the user's stated boundary. The projection adds a fixed sentence that delegation does not cover privacy, retention, payment, authentication, deployment or scope changes, mirroring the existing decision policy in the portable readiness text (L51-L55). The consumer never picks a default on the user's behalf.
6. Effective decision. For a `RESOLVED` item the appendix shows the user-entered resolution and the cited source snapshot. The original source fields stay unchanged in the source packet. The appendix states that the effective decision applies only to the listed fields and that the source text is retained.
7. Readiness. The readiness section of the exporter is not changed (see CF-7 in the assessment). The review-owned header and appendix carry the counts and state that the readiness lines in the source packet route to review only. The appendix ends with `Build readiness: NOT_ASSESSED`.
8. No inference. Items come only from user entry. There is no prose parser, no model call and no claim that the list is complete.

### Draft projection

When no decision has an item, `buildReviewedDraftPacket` and `buildIntentReviewAppendix` produce exactly today's bytes. When any item exists: the header gains one count line before the source packet, and the appendix gains one trailing section with counts by status, one block per item in decision order then array order (kind, status, linked decision, statement, cited source snapshot, effective decision or delegation boundary), the claim sentences above, and the `NOT_ASSESSED` line. Per-decision rows keep today's exact layout. Labels are provided for `vi` and `en`.

### Schema and compatibility policy

| Case | Schema string | Rule |
|---|---|---|
| State with no items | `cvf.intentSpecReviewCandidate.v1` | Byte-identical to today: same key order, same draft, same hashes, same binding key |
| State with at least one item | `cvf.intentSpecReviewCandidate.v2` | Same seven payload keys and scope literal; review has the same five keys; each decision has the five keys, plus `openItems` when non-empty |
| Stored legacy file reopened | none | Unchanged route; no revalidation is added |
| Stored v2 file reopened | none | Same route; the draft carries the items as text |

Acceptance validates exactly two shapes. The v1 path keeps today's code and exact key sets, so a v1 file with an `openItems` key is rejected as before. The v2 path has its own exact key sets, requires at least one item (one canonical encoding per state), requires every item valid and non-stale (each snapshot equals the stored brief text for its cited fields, the same test decisions already pass), requires no pending decision, and rebuilds the draft with the same builder. Both use the same failure code and the same wrapper record schema. No existing check is relaxed. The producer emits v2 only when an item exists; removing the last item returns the state to the v1 encoding.

Version and serialization policy: new field absent rather than empty; fixed field order per item; the draft is never embedded in the item set; the old reader rejects v2 for save (fail closed) and still reopens a stored v2 record by its draft text.

### Candidate write paths (proposed, not authorized)

All under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/`:

| Path | Change |
|---|---|
| `lib/intent-spec-open-items.ts` | new: types, caps, id assignment, validation, snapshot, summary, labels |
| `lib/intent-spec-review.ts` | decision type, sync staleness, update, pending, header and appendix gating |
| `lib/intent-spec-confirmation.ts` | schema string chosen from the state |
| `lib/intent-spec-acceptance.ts` | dual validator for v1 and v2 |
| `components/IntentSpecReview.tsx` | per-decision open-point entry, counts, stale notice and reconfirm, vi and en copy |
| `lib/intent-spec-open-items.test.ts` | new: helper and rule tests |
| `lib/intent-spec-legacy-golden.test.ts` | new: frozen legacy byte and readback controls |
| `lib/intent-spec-review.test.ts`, `lib/intent-spec-confirmation.test.ts`, `lib/intent-spec-acceptance.test.ts`, `components/IntentSpecReview.test.tsx` | extended with the planned cases |
| `lib/intent-spec-review-api.test.ts` | optional: one v2 save and reopen case if the existing fixture permits |

Read-only and not touched: `lib/intent-spec-review-api.ts`, `lib/intent-spec-review-client.ts`, `lib/intent-spec-file-store.ts`, `lib/intent-spec-actor.ts`, `lib/intent-spec-private-profile.ts`, the review routes, `components/SpecExport.tsx`, `lib/spec-export-portable-handoff.ts`, the auth owners and every store profile. The hook and its `canContinue` need no change because pending status is computed by the extended decision check. Vietnamese copy needs the text-encoding exception header already used by the review owners.

Proposed implementation order for a later work order: capture frozen legacy digests from the base commit before any edit; add the helper and its tests; integrate the review state; add the dual acceptance validator; add the component; run the planned suites, type check and lint; rerun the legacy controls.

### Rollback boundary

Revert the single candidate commit set limited to the paths above. No store, auth, ACL, lock or data change exists to undo. Stored v2 records stay readable by the reopen route; reverted code refuses to prepare them (fail closed). Legacy records are unaffected by construction.

## Planned Acceptance (not executed)

The plan is in `docs/reviews/evidence/cvf-nis-t1d-acceptance-plan-2026-10-05.json`. Every case is NOT_EXECUTED here. It has two synthetic fixtures with inputs listed before expectations. The first is a periodic report with the fourth unknown, a conflict and its resolution, and a mid-run source change, supplied at the stages in which the user would have them. The second is a different job, built to falsify the design: a conflict that cites fields from two different questions, a delegated item, fewer than four unknowns, an item with no cited field, Vietnamese labels, and the zero-item path. Frozen legacy controls compare digests captured from the base commit. The independent Local probe is PENDING_REVIEWER_EXECUTION and must use its own assertions.

## Alternatives Considered

| Alternative | Disposition | Reason |
|---|---|---|
| Items at the top level of the state | Rejected | Needs a mount change in the exporter and gains nothing, since an item can cite any field from a nested home |
| Nested under decisions | Selected | Reuses the existing update, revision and stale flow; no exporter edit |
| Encode items inside answer prose and parse | Rejected | Prose parsing is not admitted; collides with user text; no structure to validate |
| Inline upstream-style markers in the packet text | Rejected | Capped at three upstream, overwritten on resolution (provenance lost), unstructured |
| Separate sidecar file or store record | Rejected | Store and auth edits forbidden; not bound to the confirmed bytes |
| Ignore unknown keys in acceptance | Rejected | Relaxes the fail-closed check |
| Always emit v2 | Rejected | Changes legacy bytes and hashes |
| Change the readiness builder as T1C suggested | Not selected | It has no review input and is called before the review exists (CF-7); the review header and appendix carry the summary instead; residual risk is that the source packet still prints its readiness line, mitigated by the header count line and the precedence sentence |
| Run Spec Kit commands or scripts | Rejected for this slice | Repository-layout preconditions, file writes, subprocess use, agent-enforced output, no stable API |

## Choices For Local With Selected Default

| Id | Choice | Selected default |
|---|---|---|
| LC-1 | A stale item blocks confirmation until reconfirmed | Yes, consistent with decisions |
| LC-2 | Caps | 50 items, 2000 characters, 6 cited fields, fail closed |
| LC-3 | Id format | U or C plus number, assigned by the helper |
| LC-4 | Readiness builder | Left unchanged (CF-7) |
| LC-5 | Delegation in the first slice | Included, because the order requires it |
| LC-6 | Wording of labels | Implementer drafts, Local reviews |
| LC-7 | Upstream attribution | None needed; nothing is copied; the MIT notice duty is recorded for any future copy |

## Residual Risks

No human UX evidence exists for non-coder entry of open points. Removing an item is allowed and bumps the revision, so a deleted unknown vanishes from the draft; the cleared acknowledgement is the only guard. The stored v2 shape adds validator surface that Local should probe independently. Item caps could suit real jobs poorly; they are safety bounds only.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| clarify, checklist, spec and checklist templates, and the specify dependency | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts and intent-spec-acceptance.ts | ENRICH_EXISTING | The consumer lacks structured ids, status, per-item provenance and an effective-decision projection; upstream offers vocabulary only, with unknowns held as capped inline markers that are overwritten on resolution | Native extension of the existing owners; vocabulary rewritten in CVF wording; no upstream runtime or copied text |
| plan, tasks and analyze commands and templates, and the implement dependency | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx | ENRICH_EXISTING | No structured design, plan, tasks or consistency input exists yet to consume; the structures are candidates for later builder-owned artifacts | Defer as pattern candidates to a later slice chosen by Local; no automatic successor |
| PowerShell setup scripts and common helpers | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts | REJECT_DIRECT_IMPORT | They write files into a repository layout and run subprocesses with no stable API and no CVF consumer | Keep as data; not invoked and not adopted for this slice |
| LICENSE | .private_reference/source_mirrors/INDEX.md | CONFIRMED_EXISTING | The notice duty is recorded; nothing is copied | Record only; carry the notice if a later order copies a substantial portion |

## Epistemic Process Block

Expected Result / Prediction: a nested, versioned, additive item ledger can add explicit unknown, conflict and delegation state and an effective-decision projection while every legacy candidate keeps its bytes and every existing strict check stays unchanged.
Evidence Comparison: the pinned sources show the exact key-set, literal and reconstruction checks that force a new schema string, and show that reopen and the store do not need change; the upstream files show unstructured, capped, overwriting unknown handling and an unversioned marker.
Contradiction Or Gap Disposition: the T1C suggestion to change the readiness builder is not selected because of the circular call order; no human UX evidence exists and none is claimed; golden digests cannot be produced without running code and are planned for the base commit.
Claim Update: the contract is complete as a proposal for Local; nothing is implemented or executed.

## Claim Boundary

This contract authorizes no product edit, test run, store or auth change, upstream execution, provider call, real data, BUILD, public sync or parked-lane work. A passing structural gate on this document proves its shape only. It does not prove source fit, absorption, UX value, live governance behavior or build readiness. The write paths are a proposed envelope for Local to admit or change. Cost is UNKNOWN.


## Local Reviewer Envelope Repair

Appended by Local after full commit-hook findings; original worker bytes retained in the isolated worktree and hash-bound in Local evidence. Worker-declared contract digest refers to the original worker version. No semantic worker claim or product source was rewritten.

## Mandatory Blind-Spot Control Block

Blind-spot verdict: NOT_APPLICABLE_WITH_REASON - selected source comparison only; no absorption completion. Per-file ledger in the capability assessment; excluded paths deferred, not no-value.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION - the existing dispatch baseline and work order declared selected-source entry before acquisition. This artifact compares the frozen selected source with current owners; it does not activate or absorb source.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - selected contract comparison, no whole-repository scan or completeness assertion; worker selected-file ledger remains separate evidence.
