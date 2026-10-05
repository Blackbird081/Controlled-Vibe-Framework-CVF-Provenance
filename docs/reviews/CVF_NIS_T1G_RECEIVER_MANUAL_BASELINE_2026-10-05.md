# CVF NIS T1G Receiver Manual Baseline

Memory class: FULL_RECORD
Status: PROPOSED_PENDING_LOCAL_REVIEW
Date: 2026-10-05
docType: reference
Batch ID: CVF-NIS-T1G
Applies to: the document receiving format that follows an accepted or exported Intent-to-Spec review packet, and the frozen materials for a later manual-baseline comparison (BC-V1) on two synthetic jobs.
rawMemoryReleased=false
executionBaseHead: 61642432f7bf493701868dcf20d7d6b241fbeeb7
providerExecutionAuthority: FORBIDDEN

## Purpose

Give the downstream technical reviewer and the receiving builder one usable, source-bound document format for requirements, optional design, tasks, validations and open content, with two concrete job examples, and freeze the materials and a reproducible protocol so a later, separately admitted reviewer can run the manual arm of BC-V1 and then compare it with a helper. This slice prepares the experiment. It does not run either arm, implement a helper, score anyone, declare a job build-ready or grant build authority. It follows the T1F Local choices: document receiver first, no UI, no ad-hoc paste path, manual baseline before any helper.

## Scope / Applies To

In scope: the receiving role, the source identity and binding rules, the record layout, the review obligations, the manual review record, the two frozen job examples and their binding dispositions, the explicit adaptation of the T1F ledgers to the frozen bytes, and a pointer to the casepack and protocol. Out of scope: any helper or evaluator, any measured comparison, any product, UI, store, route or checker change, a producer run, upstream material, provider use, real data, public sync, general S2 and parked lanes. Cost is UNKNOWN; provider calls are zero.

## Target / Source

Frozen materials: `docs/reviews/evidence/cvf-nis-t1g-manual-baseline-casepack-2026-10-05.json` (eleven reviewer views, three attachments, separate answer key) and `docs/reviews/evidence/cvf-nis-t1g-manual-baseline-protocol-2026-10-05.json` (roles, clock, scoring, margin, admission steps, result templates). Controlling input: `docs/reviews/CVF_NIS_T1F_BUILD_READY_BRIDGE_CONTRACT_COMPLETION_2026-10-05.md` (Minimum Next Delta, Local choices C-1 to C-7), then the T1F contract and plan as modifiable input. Frozen job sources: the T1C replay for the periodic report and the T1E control LG3 for tool lending, cross-checked against the Local old-producer capture.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Minimum next delta is the smallest receiving format and a manual-baseline experiment contract tied to accepted packet bytes and revision; no helper implementation is admitted | CURRENT_SOURCE | docs/reviews/CVF_NIS_T1F_BUILD_READY_BRIDGE_CONTRACT_COMPLETION_2026-10-05.md | Minimum Next Delta | Minimum Next Delta | T1F Local completion | ACCEPT |
| C-3 default rejected: sticky reconfirmation must block affected readiness even when answer digests match; C-6 receiving format first, no production paste path | CURRENT_SOURCE | docs/reviews/CVF_NIS_T1F_BUILD_READY_BRIDGE_CONTRACT_COMPLETION_2026-10-05.md | Local Choices C-1 To C-7 | C-3, C-6, C-7 | T1F Local completion | ACCEPT |
| The value falsifier lists seeded defects D1 to D9, two clean controls and the falsification conditions | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1f-build-ready-acceptance-plan-2026-10-05.json | valueFalsifier | valueFalsifier | T1F plan | ACCEPT |
| Decision needs review counts a stale decision and a stale item; the stale flag is sticky across source change and cleared only by an explicit decision update | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts | L88-L104, L120-L137, L139-L144 | synchronizeIntentSpecReview, updateReviewDecision, decisionNeedsReview | review state | ACCEPT |
| Each decision records the brief fields it was answered against and the draft prints them under Source fields when this decision was recorded | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts | L11-L42, L167-L206 | INTENT_REVIEW_QUESTIONS, buildIntentReviewAppendix, buildReviewedDraftPacket | review draft | ACCEPT |
| An open item has nine ordered keys and status OPEN, RESOLVED or DELEGATED | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-open-items.ts | L10-L30 | ReviewOpenItem | open items | ACCEPT |
| A candidate embeds the review state and the draft and is hashed as bytes | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-confirmation.ts | L32-L60 | createSpecConfirmationCandidate | candidate file | ACCEPT |
| Acceptance rederives the file hash, checks exact keys and rebuilds the draft; it is the only strict decoder | CURRENT_SOURCE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-acceptance.ts | L71-L114 | prepareIntentSpecAcceptance | strict acceptance | ACCEPT |
| The frozen reporting packet is a reviewed draft at baseline revision 8 and a revised one at revision 11, produced by an older producer pin before open items existed | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1c-replay-2026-10-05.json | exportedBaselinePacket, exportedRevisedPacket, sourcePins | canonicalText, sha256 | frozen reviewed draft, not durable acceptance | ACCEPT |
| The tool lending control LG3 holds exact candidate file bytes, revision 7, with placeholder packet source and placeholder decision answers | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1e-frozen-legacy-2026-10-05.json | controls | LG3 fileContent, fileSha256 | frozen legacy control | ACCEPT |
| The Local old-producer capture for LG3 carries byte-equal values for the eight fields it shares with the frozen control | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1e-local-independent-review-2026-10-05.json | localOldProducerCapture | LG3 | Local capture | ACCEPT |
| The T1D fixtures name the plan inputs for both jobs, including structured items that the frozen bytes do not contain | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1d-acceptance-plan-2026-10-05.json | fixtures | FX-A, FX-B | plan fixtures | ACCEPT |
| The T1C scenario holds the stage inputs and values behind the reporting packet | CURRENT_SOURCE | docs/reviews/evidence/cvf-nis-t1c-scenario-2026-10-05.json | stageInputs | stageInputs | scenario | ACCEPT |

## Checker Source Read-Ahead Block
| Field | Value |
| --- | --- |
| applicableCheckersRead | governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_external_absorption_overlap_discipline.py; governance/compat/check_absorption_blindspot_control_presence.py; governance/compat/check_equivalence_claim_evidence.py; governance/compat/check_package_skill_productionization_pipeline.py; governance/compat/check_epistemic_process_packet.py |
| literalTokensReviewed | reference headings Purpose, Scope or Applies To and Claim Boundary; Overlap And Novelty Classification columns and the five allowed disposition tokens; epistemic markers Expected Result, Evidence Comparison, Contradiction, Claim Update; Source Verification Block columns; blind-spot and entry-control blocks; the closed equivalence phrase list and the package-intent phrase list |
| gateRunPurpose | confirmation and evidence that the declared shapes hold after writing; not first discovery of the shapes |
| claimBoundary | covers authoring shapes only and certifies no source fit, experiment value or readiness |

## Receiving Role And Consumption

The receiving role is the one the exported packet already names: an external builder agent that reads the packet, plans and proposes tasks (Portable Agent Handoff Readiness, Receiving Agent Mission and External Agent Acceptance Checklist), and an operator review gate that accepts or holds the agent's answer. Today the builder's plan and task output is unstructured and cannot be checked against the packet. This format is returned by that builder, or written by Local for review, and is read by the existing downstream technical reviewer (Local) before any build discussion. The reviewer reads the record next to the bound source bytes and writes a manual review record for named scopes. No production consumer integration is proven: there is no store, UI, route or paste path in this slice, and the receiving builder's ability to produce a valid record is UNPROVEN.

## Source Identity And Binding

| Binding kind | What it is | Status in the frozen jobs |
|---|---|---|
| EXPORTED_REVIEWED_DRAFT | the printed review draft: exported packet, review appendix, printed revision and viewed line | job A revisions 8 and 11 (attachments A and B) |
| ACCEPTED_FILE_CANDIDATE_BYTES | the exact candidate file bytes with their SHA-256 and the revision inside the file | job C revision 7 (attachment C), synthetic |
| HISTORICAL_SYNTHETIC_RECORD | an acceptance record minted by a test producer | exists for LG3 only as a hash, not used as a source |
| CURRENT_VERIFIED_ACCEPTANCE | an acceptance event verified now by the existing strict path | never claimed by this slice |

Section 1 of every record states the bound attachment, its kind, SHA-256, byte count, the revision printed in the source, the viewed revision, the accepted-file pairing and the current source attachment, hash and revision. Fail-closed rules: a missing binding block, a bound hash or revision that differs from the current source, or any cited decision whose recorded source fields differ from the current source makes the affected scopes REBIND_REQUIRED or STALE_SOURCE, never ready. A pairing of SOURCE_BINDING_NOT_ESTABLISHED means only review-only bytes exist: the record may be reviewed but every readiness wording carries that limit and experiment admission is on HOLD. Rebinding, rehashing or re-rendering a record is not technical review and grants nothing.

## Record Layout

Eight numbered sections in this order. Section 1 source binding table. Section 2 open content located in the source: each marker with where it appears, its exact quote and the requirements that cite it; a marker cited by no requirement stays listed and is a visible limitation. Section 3 requirements, each with one to five statements quoted exactly from the cited source, one to twelve sources of the form `BRIEF_FIELD:key` or `DECISION:key`, and any user resolution quoted exactly. Section 4 design elements (optional, kinds DATA, INTERFACE or FLOW, each serving a requirement). Section 5 tasks with the requirements and design they serve, dependencies, validations and advisory categories. Section 6 validations, each serving a requirement. Section 7 out-of-scope claims and author limitations. Section 8 the fixed authority statement followed by the record digest line, which is the SHA-256 of all bytes above it. Designs, tasks and validations are author proposals; only quoted statements and quoted resolutions are user words, and no sentence the user did not enter may appear as a user statement.

## Review Obligations

- RO-1 Ids are safe and distinct: R, DE, T or V followed by a number from 1 to 999, unique within the record.
- RO-2 Finite resource limits, not completeness quotas: at most 100 requirements, 100 design elements, 300 tasks, 300 validations, 12 sources per requirement, 5 statements per requirement and 2000 characters per text. A record over a limit is refused whole, never truncated.
- RO-3 Every quoted statement and quoted resolution is an exact substring of the cited source section of the bound attachment.
- RO-4 Cross-links are coherent, not merely present: each task serves an existing requirement whose subject fits the task, each validation serves the requirement it checks, each design serves a requirement, every dependency names an existing task and the dependency relation has no loop.
- RO-5 Every requirement is served by at least one task and one validation. A requirement with no open content is complete for these checks and is not forced to cite any marker; no open content means no declared blocker, not complete semantics.
- RO-6 A requirement is affected by a marker when it cites the section where the marker appears; an affected requirement is blocked by open content until the user decides. Markers cited by no requirement are reported, not hidden.
- RO-7 Every user resolution that applies to a requirement is quoted by it; none is invented.
- RO-8 Sticky reconfirmation: the existing review state keeps a decision flagged for reconfirmation after a source change until an explicit decision update, and it also treats a stale item as needing review. A decision whose answer text is unchanged but whose recorded source fields changed is still stale. A requirement that cites it is stale until reconfirmed.
- RO-9 The authority statement is the fixed one. No wording, digest or rehash can grant build authority; a record carrying a grant is rejected as a record defect.
- RO-10 Texts are not placeholder words. Anything not verifiable from the supplied bytes is reported as a limitation.
- RO-11 Overlapping user rules are shown as the user entered them; the format has no field that names a winner.
- RO-12 Categories are advisory task metadata, never permission. An empty or OTHER category does not authorize sensitive work, and a supplied delegation excludes privacy, retention, payment, authentication, deployment and scope decisions. The frozen bytes contain no delegation.

## Manual Review Record

For each named scope (a requirement and the tasks, designs and validations that depend on it) the reviewer writes: scope id, verdict, reasons and the bound and current source evidence. Verdict vocabulary: READY_FOR_TECHNICAL_REVIEW (the structural obligations hold for this scope and a technical reviewer may read it; nothing more), BLOCKED_BY_OPEN_CONTENT, BLOCKED_BY_RECORD_DEFECT, STALE_SOURCE, REBIND_REQUIRED and NOT_ASSESSED. A verdict is a scope statement, never a count, score or acknowledgement, and it never grants execution. The blank answer form in the protocol is the experiment's version of this record.

## Job Examples And Source Adaptation

| Job | Frozen source | Bytes and hash | Binding disposition | Role in the casepack |
|---|---|---|---|---|
| A periodic equipment report | reviewed draft revision 8 (attachment A) and revision 11 (attachment B) from the T1C replay, full reporting rules | 23823 bytes, SHA-256 393ecee7594febaf53da2728b3d640ad493f8a1bbfe8b2c77b191392d233b56b; 24158 bytes, 02b8d1f51a77a8233d6eab0492344e2781bbb2aa2b1bf460d1e30a73e0308ad1 | SOURCE_BINDING_NOT_ESTABLISHED, experiment admission HOLD | one clean record and six seeded records |
| C tool lending | candidate file bytes of control LG3, revision 7 (attachment C) | 6253 bytes, SHA-256 0d4a3dd870fd6f9e85541c8f338cbde2df444db44731c42ed203aeff41b3ac52 | file bytes and revision established, synthetic; placeholder packet source and placeholder answers | one clean record and three seeded records |

Job A has no accepted-file bytes, file hash or actor-bound record: the replay printed draft hashes only and used an older producer pin, and a producer may not be run here. The smallest owner route is for Local to mint, through the existing producer capture used by T1E, a candidate file for the revision 8 and revision 11 reviewed states and freeze its hash and state. LG1 and LG2 hold only the value Synthetic reporting and serve as compatibility controls, not as the reporting source.

Explicit adaptation of the T1F ledgers to the frozen bytes: structured item citations (`ITEM:` references and item ids) are removed because neither frozen source contains structured items; open content is the prose markers in the answers and in the constraints field, quoted exactly. The conflict resolution is quoted from the boundaries answer in the case it has there (the answer begins Resolution of C1 with a lower-case corrections), not in the T1F capitalized form, which is not a substring of the source. The retention requirement R6 was added so that a requirement cites the data decision. The design id D1 was renamed DE1 so that it cannot be confused with a seeded case label. The tool lending delegated item, open unknown and declared conflict of the T1D plan are unsupported content; the record instead declares as an author limitation that the lead-views-all-loans and no-accounts statements may conflict, without deciding it. The constraints-text drift of the T1F plan is unsupported in the frozen bytes; the real frozen drift is the access rule change in the target users field between revisions 8 and 11, which also gives the equal-answer case: the data decision answer is byte-equal in both revisions while its recorded target users snapshot changed. Source text, decisions and resolutions survive in the quoted sections; nothing synthetic is presented as a user requirement.

## Experiment Preparation

The casepack holds eleven neutral cases RB-01 to RB-11 in a fixed order derived by an announced SHA-256 sort rule: two clean records (one per job) and nine seeded or limitation cases D1 to D9 (D2, D3 and D8 on job C, the rest on job A). Each case has its exact Markdown reviewer view and view hash; the answer key and mutation locators sit in a separate section. Both sections are in one file, so the separation is a role protocol, not access isolation. The protocol freezes the reviewer package, the generic checklist, the blank answer form, contamination recording with taxonomy familiarity kept apart from placement knowledge, the clock (20 minutes preparation, 12 minutes per case, 180 total, one primary attempt, no practice replacement), scoring of D1 to D8 and the two controls, D9 as disclosure only, a numeric comparable-effort margin of 1.25 over a pilot of 12 reviews with sensitivity at 4 and 52, the route selection rule, admission steps and blank result templates. The worker who authored the seeds knows every placement and cannot report a blinded manual result. A helper arm needs a separately bounded order, a named consumer and an independent comparable build; none exists. All results are NOT_EXECUTED or UNKNOWN.

## Planned Acceptance (not executed)

Local reviews fixture fidelity and the protocol before any execution: recompute attachment, view and casepack hashes, run the leak scan, verify clean-record quotes against the attachments, independently re-derive one placement per seed class, confirm the job A HOLD, and confirm every result field is unfilled. Nothing here runs a reviewer, a helper or a scorer.

## Residual Risks

- One worker authored the receiver, the records, the seeds and the protocol; independent authorship stays with the Local probe.
- All seeds are mine, so even a different manual reviewer sees a seed set shaped by my idea of defects; one pilot of two synthetic jobs does not test generalization or noncoder UX.
- Job A pairing is not established; until it is, admission is on HOLD or limited to review-only inputs.
- The generic checklist covers the seeded classes by design, so taxonomy familiarity of any reviewer is expected and must be disclosed.
- The numeric margin, horizon and timeboxes are predeclared assumptions, not measurements; helper costs are UNKNOWN.
- Frozen drafts and candidates are historical synthetic evidence, not a current acceptance event or actor verification.

## Minimum Next Delta

Local decides whether to admit the materials. If admitted, lift the job A HOLD with a minted candidate or label the run review-only, assemble the reviewer package without the answer key, and admit a distinct reviewer to run the manual arm once. A helper arm stays unadmitted. No successor is released here.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| Accepted packet identity, revision and sticky reconfirmation | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts | CONFIRMED_EXISTING | The receiving obligations restate existing boundaries and add none | Reuse by reference without source change |
| Receiver format, concrete job records and comparison protocol | docs/reviews/CVF_NIS_T1F_BUILD_READY_BRIDGE_CONTRACT_2026-10-05.md | ENRICH_EXISTING | Concrete frozen records, fixed cases and a predeclared protocol replace the T1F planned cases for the manual arm | Documentary preparation only |

## Epistemic Process Block

Expected Result / Prediction: a compact document format tied to exact source bytes, with two concrete job records and a fixed protocol, lets a later distinct reviewer run the manual arm without access to the seed placements and lets Local decide document versus helper from a predeclared total-effort rule.
Evidence Comparison: the frozen replay and control bytes verify by SHA-256, every clean-record quote is an exact substring of its source section, the data decision answer is byte-equal across revisions 8 and 11 while its recorded target users snapshot differs, and the Local old-producer capture shares byte-equal fields with the frozen control; the reporting source has no accepted-file bytes and no structured items.
Contradiction Or Gap Disposition: the T1F ledgers do not match the frozen bytes in item citations, the resolution quote case and the drift field, so they were adapted explicitly; job A pairing is SOURCE_BINDING_NOT_ESTABLISHED and its admission is HOLD; seeds are author-known and one job carries six of nine.
Claim Update: the receiver and experiment materials are ready for Local review; no arm was run, nothing is selected and no job is build-ready.

## Claim Boundary

This document authorizes no helper, scorer, evaluator, product edit, store, UI, producer run, provider call, real data, BUILD, public sync, general S2 or parked-lane work. A passing structural gate proves shape only. It does not prove the format is usable by a real builder, that manual review is cheaper or worse than a helper, UX value or build readiness. Frozen materials are historical synthetic evidence. BC-V1 stays NOT_EXECUTED and the 35 T1F planned cases stay NOT_EXECUTED. Cost is UNKNOWN.

## Mandatory Blind-Spot Control Block

Blind-spot verdict: NOT_APPLICABLE_WITH_REASON - named internal documentary preparation; no corpus-wide novelty, external absorption or value closure claim. Used locators and exclusions are listed in the worker return.

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON - internal governed T1F disposition and existing native and frozen fixture inputs only; upstream reassessment and acquisition are excluded.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named source and fixture pins, not a completed corpus scan; no all-repository-read claim.

## External Knowledge Intake Routing
| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | docs/reviews/CVF_NIS_T1F_BUILD_READY_BRIDGE_CONTRACT_COMPLETION_2026-10-05.md |
| Chain map route | accepted Local contract disposition -> documentary receiver and baseline preparation |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | existing NIS packet receiver and Local technical reviewer |
| Disposition | ADAPT_EXISTING; helper and experiment execution deferred |
| Claim boundary | the historic upstream-derived proposal is input only; no new acquisition or runtime grant |

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": null
}
```
