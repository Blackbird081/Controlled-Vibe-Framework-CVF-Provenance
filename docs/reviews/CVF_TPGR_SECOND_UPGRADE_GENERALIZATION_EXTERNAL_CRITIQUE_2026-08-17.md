# CVF TPGR Second Upgrade Generalization External Critique

Memory class: governed-planning-review

Status: ADVISORY_INPUT_PENDING_RECONCILIATION

docType: external_critique

Date: 2026-08-17

External return SHA-256:
`f27d420ccc1c56a7d62fa35c4fd4c8684b7ab0d99e7ff316bfe7185dbd9122db`

Reviewer normalization: the external return is preserved semantically. The
CVF reviewer added the governed-review evidence wrapper, corrected the
working-tree statement to distinguish pre-save state from the returned file,
and replaced four checker-triggering prose labels with equivalent
"outside-source" wording. The hash above identifies the exact pre-review
external return; the normalized artifact has a different hash.

## Purpose

Preserve the second independent external critique of the TPGR second-upgrade
revised plan as advisory evidence pending CVF reconciliation. This critique
answers the operator's generalization question: whether the revised plan
establishes a reusable CVF absorption operating model for future repositories,
or mainly optimizes gate execution for the current 205-file use case.

## Target / Source

| Input | Identity | Authority disposition |
| --- | --- | --- |
| primary revised plan | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_CRITIQUE_RECONCILIATION_AND_REVISED_PLAN_2026-08-17.md`; HEAD `532e4bd81bc4e927cbaa46b2f9a44bee18551a93`; SHA-256 `3f4f922f083d499a6c8c908e6c30b564cb808e2dceeeebe14d885e129a513582` | CVF-governed planning source |
| prior external critique | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_EXTERNAL_CRITIQUE_2026-08-17.md`; SHA-256 `e77bc771796b387be4d270c40ee87ad0c7174e1d236eb66f232496d332a0e820` | advisory input; facts re-verified against CVF sources |
| TPGR standard | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | canonical current T0 authority |
| absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | canonical routing order; records the unresolved universal-router gap |
| outside-source core standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | canonical general absorption lifecycle |
| mixed-origin standard | `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md` | canonical evidence-reuse and system-chain rules |
| blind-spot prevention standard | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | canonical seven-gate absorption discipline |
| corpus scan registry standard | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` (GC-051) | canonical source registration and scan-state inheritance |

## Scope / Methodology

External reviewer verified HEAD and both artifact hashes exactly, read all
eight mandatory sources in full (2,370 lines), and additionally inspected the
route registry, router, autorun catalog, and the generated corpus scan
registry (`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`, 170
registered corpora) as machine evidence for the generalization question. The
reviewer accepted both corrections the prior reconciliation made to the first
critique (catalog-unwired vs orphan; hash-binds-bytes vs proves-reading). No
repository path other than this returned critique was created or modified; no
path was staged or committed. No T15, checker, catalog, or selective-execution
action was taken.

## Findings / Position

External scope verdict: `SPLIT_TPGR_AND_ABSORPTION_ARCHITECTURE`.

Central finding: CVF already operates a general, machine-checked absorption
lifecycle (outside-source core standard, mixed-origin standard,
blind-spot prevention standard, GC-051 corpus registry) proven in production
at 170 registered corpora across six source-type categories. The revised TPGR
plan's routing mechanisms are generic, but its evidence base, cost model, and
R2 feasibility gate are drawn entirely from the single 205-file local corpus.
The plan should route the existing absorption lifecycle rather than restate or
absorb it, and its R2 gate must be rescoped across multiple source archetypes
before it can support a general activation decision.

Final recommendation: `REVISE_R2_SCOPE_BEFORE_APPROVAL`.

## Risk / Corrective Action

Risk: approving R2 in its current single-archetype scope would validate cost
savings only for the cheapest possible case (an already-accepted corpus with
maximal evidence inheritance), producing activation evidence biased toward
approval and unrepresentative of first-time repository intake, upstream delta
re-intake, or owner-gap cases.

Corrective action: rescope R2 to five source archetypes (new upstream
repository, local synthesis pack, cluster-from-accepted-corpus regression,
upstream delta, minimal named-file intake) with an explicit stop condition on
the no-inheritance case, before any operator activation decision.

Secondary risk: without reserved claim vocabulary, a bounded capability-cluster
review could be reported as full corpus absorption, silently accumulating
unread-file blind spots behind valid-looking receipts.

Corrective action: adopt the eight-token claim vocabulary in this critique,
reserve the word "absorbed" for machine-checked tokens only, and require
explicit unread-file reconciliation before any corpus-level absorption claim.

---

# Independent External Critique

## Artifact Verification

| Item | Expected | Computed | Status |
| --- | --- | --- | --- |
| HEAD | `532e4bd81bc4e927cbaa46b2f9a44bee18551a93` | `532e4bd81bc4e927cbaa46b2f9a44bee18551a93` | VERIFIED |
| Working tree before saving the returned critique | -- | clean | VERIFIED |
| Revised plan SHA-256 | `3f4f922f083d...13582` | `3f4f922f083d499a6c8c908e6c30b564cb808e2dceeeebe14d885e129a513582` | VERIFIED |
| Prior critique SHA-256 | `e77bc771796b...a0e820` | `e77bc771796b387be4d270c40ee87ad0c7174e1d236eb66f232496d332a0e820` | VERIFIED |

All eight mandatory sources read in full. Additionally inspected as machine
evidence: the route registry, `route_task_governance.py`,
`agent_autorun_command_catalog.py`, and the generated corpus scan registry. No
file created, edited, staged, or committed. No T15, checker, catalog, or
selective-execution action taken.

Both corrections the reconciliation made to the prior critique are accepted:
"catalog-unwired" is the correct term for the 114 checkers absent from the
autorun catalog, not "orphan," since absence from one catalog does not prove
absence from all usage; and a content hash binds a receipt to bytes, not to
semantic understanding, so `clusterSemanticReceipt` is a genuine improvement
over a hash-only proposal.

## Executive Position

The revised plan is a sound governance-routing design answering a question it
was not asked to answer. It optimizes which controls execute (task-proportional
routing). It does not define how knowledge enters CVF (the absorption
lifecycle) -- and it does not need to, because that lifecycle already exists
and is already general. Verification found: `CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`
defines a generic manifest/ledger/disposition/owner-map/value-conversion/
overlap process explicitly stated to apply uniformly across repositories;
`CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` (GC-051) already registers
170 corpora across six source-type categories (`CVF_EXTENSION` 87,
`PROJECT_SOURCE` 37, `POLICY_DOCUMENT` 18, `LEGACY_FOLDER` 17, `TEST_CORPUS` 6,
`EXTERNAL_SOURCE` 5) with scan-state inheritance and drift checking; and the
chain map explicitly records its own remaining gap -- no universal
trigger/router yet machine-enforces every external repo, review, corpus, or
legacy intake through the full chain. That is precisely the role TPGR should
fill: router, not owner. The revised plan's R2 feasibility gate benchmarks
only the seven-file cluster and one medium local tranche, both drawn from the
same already-accepted 205-file corpus at the same intake stage with maximal
evidence inheritance -- the cheapest possible case, and therefore structurally
biased toward an approval decision that would not generalize to first-time
repository intake, upstream delta re-intake, or owner-gap resolution. The
205-file corpus is itself one component (205 local files) of an already
GC-051-registered 764-file `EXTERNAL_SOURCE` corpus with three distinct
completeness verdicts already tracked separately (`gc047: COMPLETE_VERIFIED`,
`gc048: RECONCILED_VERIFIED`, `gc050: NOT_RUN`) -- proof that CVF already needs,
and partially has, the non-confusable completeness vocabulary this critique
formalizes. Scope verdict: `SPLIT_TPGR_AND_ABSORPTION_ARCHITECTURE`. Final
recommendation: `REVISE_R2_SCOPE_BEFORE_APPROVAL`.

## Requirement-To-Design Gap Matrix

| # | Operator requirement | Current revised plan | Gap | Severity |
| --- | --- | --- | --- | --- |
| G1 | Reusable across future repositories | Mechanisms generic; evidence, cost model, R2 all 205-only | Scope statement and multi-archetype evidence absent | High |
| G2 | Layer A lifecycle defined | Not addressed; `intakeStage` I0-I3 is a 4-value label with no stage contract | I0-I3 unbound to the 11 absorption-lifecycle activities and existing standards | High |
| G3 | Layer A / Layer B authority separation | Undeclared; P6 implies eventual TPGR ownership of absorption | Duplicate-mega-standard risk | High |
| G4 | No copy/paste of external structure | Stated as prose prohibition in the 205 route only | Not bound to the existing machine-checked overlap/value-conversion guards | Medium |
| G5 | Later delta intake after upstream change | Invalidation triggers cover evidence, not source updates | No upstream-delta stage; scenario unserviced | High |
| G6 | 205 corpus not the implicit universal case | 205 route is the only worked example; R2 benchmarks only it | Overfitting risk in the activation evidence | High |
| G7 | Non-confusable completeness claims | Not addressed | Cluster review could be reported as full absorption | High |
| G8 | Small named-file intake without repo ceremony | `sourceScale: NAMED_FILES` exists in the registry | Not connected to any absorption-lifecycle minimum; ceremony floor undefined | Medium |
| G9 | Downstream project use without authority contamination | P6 deferred entirely | GC-051 Rule 5 already covers registration; routing side unstated | Medium |
| G10 | Prefer enrichment of existing owners | `ownerFit` covers CVF-side owner fit | Silent on which governance owner holds each new rule | Medium |

## Smallest Reusable Architecture

Four components; three already exist; one new owner is genuinely necessary.

**A. Source Registration -- existing owner: GC-051 corpus scan registry.**
Every source archetype registers here first. Already proven at 170 corpora.
Requires only one enum extension: add `DERIVED_SYNTHESIS_PACK` and
`NAMED_FILE_SET` to `corpusType`.

**B. Absorption Lifecycle -- existing owners: outside-source core,
mixed-origin, and blind-spot prevention standards.** Own manifest, ledger,
disposition, owner-map, value-conversion, overlap, and semantic-review
discipline. TPGR must not restate any of this.

**C. Routing -- existing owner: TPGR standard.** Owns profile, dimensions,
evidence inheritance, control selection, escalation, and fallback, extended
per the revised plan's Designs 1-8 with the corrections below.

**D. Stage Contract -- NEW, and the only genuinely new owner needed.** A thin
binding table naming, per intake stage, the entry-required evidence,
exit-produced evidence, receipt type, invalidation triggers, and licensed
claim. This is the interface between Layer A and Layer B: TPGR routes stages;
the existing standards define what each stage means. It should live inside the
TPGR owner as a "Layer A Interface" section -- one page, not a new standard.

Explicitly rejected: a new unified absorption mega-standard; a second
governance control plane; TPGR restating ledger/manifest/disposition
semantics; per-repository bespoke routing.

## Stage Model

| Stage | Entry evidence | Exit evidence | Receipt | Invalidation | Allowed claim |
| --- | --- | --- | --- | --- | --- |
| S0 REGISTERED | source identity: URL+pinned commit, local root, or explicit file list | GC-051 entry with `status: NOT_STARTED` | `sourceRegistrationRef` | scope paths change; upstream commit moves | "source is known to CVF"; not "read" |
| S1 ACCOUNTED | S0 | filesystem-backed manifest + hash; blind-spot Gate 1 | `corpusReceipt` | root/manifest hash drift; file count drift vs registry | "corpus structurally enumerated"; not "understood" |
| S2 DISPOSITIONED | S1 | every manifest item at a terminal status; reconciliation totals | `corpusReceipt` (extended) | ledger hash drift; scope expansion | "every file reached a terminal disposition"; not "every file read substantively" |
| S3 TRIAGED | S2 | overlap/novelty classification; candidate clusters ranked | `triageReceipt` | owner-surface set changes; new completeness claim | "candidates identified"; not "value confirmed" |
| S4 CLUSTER_UNDERSTOOD | S3 + selected hashes | `clusterSemanticReceipt`: content summary, use cases, value disposition, target owner, claim boundary, reviewer identity | `clusterSemanticReceipt` | selected-file/owner/dependency hash drift; checker-closure drift; new claim class | "this named cluster is substantively understood"; never repo-level |
| S5 OWNER_MAPPED | S4 | owner-fit result; direct dependencies; `ADAPT_CANDIDATE` vs `ADAPTED` | `ownerMapReceipt` | owner moves/changes semantics; conflict appears | "value has a named CVF target"; not "materialized" |
| S6 CVF_NATIVE_CONVERTED | S5 (valid, unexpired) | CVF-native diff under the named owner; focused proof; routed closure | `checkerClosureReceipt` | actual paths/effects exceed manifest | "value materialized in a CVF owner" |
| S7 PROMOTED | S6 + independent review | authority/runtime/public decision under P3/P4 | closure evidence | any fail-closed trigger | scope-exact promotion claim only |
| S8 DELTA_REINTAKE | prior S1-S7 receipts + new upstream identity | delta manifest: added/changed/removed vs pinned commit | `deltaReceipt` | upstream commit change always invalidates S1/S2 | "delta accounted"; prior cluster claims survive only where hashes match |

Two rules make this general rather than 205-shaped: (1) stage monotonicity
with evidence gating -- S(n) requires a valid, unexpired S(n-1) receipt, and a
missing/invalidated predecessor forces re-entry only at the earliest
invalidated stage, not a full restart; (2) claim confinement -- each stage
licenses exactly one claim class, and no stage may license a claim from a
later stage. S8 closes the gap in scenario 4 (upstream delta), which the
current plan does not serve at all.

## Task/Risk Routing Matrix

| Ceremony component | Disposition | Rationale |
| --- | --- | --- |
| GC-051 registration | KEEP (all sources) | Cheapest control in the system; already at 170 corpora |
| Filesystem-backed manifest (S1) | KEEP | Blind-spot Gate 1 exists because self-reported counts failed twice (230 vs 97 files) |
| Terminal ledger (S2) | CONDITIONAL, scaled to source | Full ledger for repo/corpus intake; for a named-file set the file list is the ledger |
| Blind-spot 7 gates | CONDITIONAL | Full set at S1-S3 for new sources; Gates 4-7 only at S4-S6 when S1-S3 receipts are valid |
| Value-conversion matrix | KEEP | The anti-copy/paste control; also captures package/runtime/checker opportunity |
| Overlap/novelty classification | KEEP | Prevents duplicate owners and silently-dropped deltas |
| Mixed-origin provenance block | CONDITIONAL | Required when more than one origin class; N/A for single-origin upstream |
| System-chain value review | CONDITIONAL | Required at S3/S5 for composed capabilities; not for a doc-only named-file intake |
| Conditional reopen index | KEEP | Cheap; prevents candidate loss in closeout prose |
| Corpus completeness re-proof per task | REMOVE | Replaced by S1/S2 receipt inheritance plus named invalidation |
| Per-file semantic re-adjudication | REMOVE | Already forbidden by the mixed-origin standard's `semanticReviewUnit: CAPABILITY_CLUSTER` |
| Fresh intake ceremony for accepted corpus | REMOVE | The defect that motivated this program |
| Full legacy bundle on every task | CONDITIONAL | Retained for authority/safety/runtime/public/destructive/irreversible and all unresolved states |
| Reviewer semantic audit | KEEP | Machine gates never prove value conversion |
| Independent review before closure | KEEP | Non-negotiable at S6/S7 |

## Authority Placement

| Rule | Owner | Action |
| --- | --- | --- |
| Source registration, typed corpora, scan-state inheritance | GC-051 corpus scan registry | ENRICH: add `DERIVED_SYNTHESIS_PACK` and `NAMED_FILE_SET` to `corpusType` |
| Manifest/ledger/disposition/owner-map/value-conversion/overlap | Outside-source core | UNCHANGED -- TPGR must not restate |
| Origin classes, claim-specific evidence, decision vector, system-chain, evidence reuse | Mixed-origin standard | UNCHANGED |
| Seven blind-spot gates | Blind-spot prevention standard | ENRICH: state which gates bind to which stage (S1-S3 vs S4-S6) |
| Chain-map routing order and the named universal-router gap | Chain map | ENRICH: name TPGR as the router that closes the recorded gap |
| Profile/dimensions/escalation/fallback/inheritance/control selection | TPGR standard | ENRICH per Designs 1-8 |
| Stage contract (S0-S8): entry/exit/receipt/invalidation/claim | NEW -- TPGR "Layer A Interface" section | The only new surface; a table, not a standard |
| Claim vocabulary | Corpus completeness standard + TPGR | ENRICH both; single token set, referenced not duplicated |
| Downstream project routing | GC-051 Rule 5 + TPGR | ENRICH: state that project registration does not equal authority promotion |

Eight enrichments, one new table, zero new standards.

## R2 Feasibility Scope Assessment

**R2 as scoped cannot validate the general objective.** It benchmarks the
seven-file cluster and one medium local tranche, both drawn from the same
already-accepted local corpus, same intake stage (I2), same origin class
(`ACCEPTED_DERIVED`), same evidence state (`INHERITED_FRESH`), same owner-fit
posture. Two samples from one cell of the routing matrix cannot establish
behavior across the matrix. R2 as written exercises none of: S0/S1 for an
unregistered source; S8 delta re-intake; `EXTERNAL_UNACCEPTED` origin;
`OWNER_GAP`/`OWNER_CONFLICT`; the P3/P4 fallback path; or the named-file
minimum-ceremony floor -- yet all six are load-bearing for the operator's
stated objective, and four are where fail-closed behavior lives. The
seven-file cluster is also the cheapest possible case: cost savings measured
there will be the most favorable number the design can produce, because
inherited evidence covers nearly everything. Generalizing that ratio to a
first-time large intake -- where S1-S3 dominate and inheritance saves nothing
-- would materially overstate the program's value.

R2 must become archetype-based, minimum five archetypes:

| Archetype | Cell exercised | Why required |
| --- | --- | --- |
| A1 New upstream repository (S0-S3) | `EXTERNAL_UNACCEPTED`, `NEW` | The dominant future case; no inheritance available |
| A2 Local synthesis pack (S0-S5) | `ACCEPTED_DERIVED`, mixed-origin | The RSPB pattern generalized |
| A3 Cluster from accepted corpus (S4-S6) | `INHERITED_FRESH` | The seven-file fixture -- regression only |
| A4 Upstream delta (S8) | `DELTA_REFRESHED` | Currently unserviced; highest design risk |
| A5 Named-file intake (S1-S6, minimal) | `NAMED_FILES` | Proves the ceremony floor works |

Per archetype: one-time authoring cost, recurring maintenance, selected-vs-full
command count, wall time, and ceremony-artifact count. Stop condition: if
savings on A1 (the no-inheritance case) are negative, the program is
optimizing only for reuse of already-accepted corpora and must be re-scoped
before any activation decision. R2's current scope cannot ask this question.

## Semantic Completeness Vocabulary

CVF already tracks three distinct completeness states separately in the
generated corpus registry (`verdicts: {gc047, gc048, gc050}`) but lacks prose
vocabulary that prevents collapsing them into "absorbed." Proposed token set,
each mapped to exactly one stage:

| Token | Exact meaning | Stage | Must never be read as |
| --- | --- | --- | --- |
| `SOURCE_REGISTERED` | Identity and scope known | S0 | any reading occurred |
| `STRUCTURALLY_ENUMERATED` | Filesystem-backed manifest + hash; count reconciled | S1 | any file was read |
| `LEDGER_DISPOSITIONED` | Every manifest item at a terminal status | S2 | every file was read substantively |
| `TRIAGE_CLASSIFIED` | Shallow/automated overlap-novelty pass | S3 | value confirmed |
| `CLUSTER_SEMANTICALLY_READ` | Named cluster substantively read; scope = the listed files | S4 | repository-level understanding |
| `CAPABILITY_ABSORBED` | One bounded capability materialized in a named CVF owner | S6 | repository absorbed |
| `CORPUS_SEMANTICALLY_ABSORBED` | Every substantive file read and dispositioned into owners | S4xN + S6xN | -- |
| `DELTA_ACCOUNTED` | Upstream change enumerated against pinned prior | S8 | delta absorbed |

Binding rules: (1) `CLUSTER_SEMANTICALLY_READ` and `CAPABILITY_ABSORBED` are
invalid without an explicit file/cluster list; (2) N cluster claims never sum
to `CORPUS_SEMANTICALLY_ABSORBED` -- that token requires explicit
reconciliation proving no substantive file remains unread, mechanically the
blind-spot Gate 7 cross-check generalized to files; (3) the bare word
"absorbed" is forbidden in governed artifacts outside these tokens, and this
is machine-checkable exactly like the existing maturity-as-value phrase
rejection in the mixed-origin guard; (4) `LEDGER_DISPOSITIONED` never implies
`CLUSTER_SEMANTICALLY_READ` -- the TPGR standard already states a terminal
ledger row is not full-read proof, and this elevates that statement to
enforced vocabulary.

The RSPB registry entry is the live worked example of why this matters: it is
`STRUCTURALLY_ENUMERATED` and `LEDGER_DISPOSITIONED` at 764 files,
`CLUSTER_SEMANTICALLY_READ` for selected clusters only, and explicitly not
`CORPUS_SEMANTICALLY_ABSORBED` -- its `gc050: NOT_RUN` proves the
classification layer never ran. Current prose cannot express that distinction;
this vocabulary can.

## Three Strongest Future-Repository Failure Modes

**1. Stage-claim laundering at scale.** Highest severity. A future large
repository is registered, manifested, and ledger-dispositioned; one small
cluster is read; the closeout says "repository absorbed." Every downstream
tranche inherits a receipt implying semantic coverage that never existed, and
because inheritance is designed to prevent re-reading, nothing ever revisits
it. This is the LHW20 failure (claimed 13/97 subfolders, actual 24/230)
reappearing at receipt level, harder to detect because the receipt looks
structurally valid. Controls: reserved-word claim vocabulary with machine
checking; scope-bound cluster claims; no promotion by aggregation;
`CORPUS_SEMANTICALLY_ABSORBED` requires explicit unread-file reconciliation.

**2. Upstream drift with live inherited receipts.** High severity. Scenario 4
is unserviced today. An upstream repo advances after intake; CVF holds cluster
receipts pinned to the old commit. Selected-file hashes still match (those
specific files did not change), so no current invalidation trigger fires --
but the surrounding code changed, and the cluster's meaning with it. CVF
converts against a stale understanding while every receipt reports fresh.
Controls: S8 as a first-class stage; pinned-commit binding in
`sourceRegistrationRef`; upstream commit change always invalidates S1/S2
regardless of selected-file hash stability.

**3. Architecture dilution through owner-gap accumulation.** High severity.
Successive intakes each hit `OWNER_GAP`, each creates a "small, justified" new
owner, and after many absorptions CVF's structure mirrors the union of
absorbed repositories -- copy/paste at the architectural level, which no
file-diff check detects. Controls: `OWNER_GAP` routes to an explicit authority
decision, never auto-creation; the existing overlap/novelty guard defaults to
`ENRICH_EXISTING`; the value-conversion matrix's `REJECT_DIRECT_IMPORT` lane;
periodic owner-count-versus-absorption-count review as a leading indicator.

## Scope Verdict

`SPLIT_TPGR_AND_ABSORPTION_ARCHITECTURE`

Not a redesign verdict: the routing mechanisms in Designs 1-8 are sound and
generic. The defect is that the plan never states the boundary between what it
routes (task/risk/evidence controls) and what already exists and handles
absorption (manifest, ledger, disposition, owner-map, value-conversion,
overlap, provenance -- all machine-checked and running at 170 registered
corpora). The chain map itself names the exact gap TPGR should fill: no
universal trigger/router yet machine-enforces every external repo, review,
corpus, or legacy intake through the existing chain. TPGR should close that
gap by routing into the existing lifecycle stages, not by restating or
absorbing them.

## Final Recommendation

`REVISE_R2_SCOPE_BEFORE_APPROVAL`

Not `REPLACE_WITH_GENERAL_ABSORPTION_ARCHITECTURE_PLAN`: a replacement would
likely re-derive the absorption lifecycle, which already exists, is already
general, and is already running at 170 corpora; rebuilding it would create the
duplicate mega-standard the operator explicitly warned against.

Not `KEEP_CURRENT_R2`: two same-cell samples cannot validate the general
objective, and the sampled cell is the cheapest possible case, biasing the
evidence toward approval at the exact moment the operator decides whether to
fund the program.

Not `STOP_THE_UPGRADE`: the diagnosis is sound, the fail-closed posture is
right, the prior reconciliation demonstrated genuine independent judgment by
correcting two overclaims in the first critique, and the chain map's recorded
universal-router gap is real work worth doing.

Required revisions before approval, in priority order:

1. Declare the Layer A / Layer B split in the TPGR owner; delete P6 rather
   than defer it.
2. Author the S0-S8 stage contract binding `intakeStage` to existing standards
   by reference.
3. Adopt the claim vocabulary; reserve the word "absorbed" for machine-checked
   tokens only.
4. Rescope R2 to five archetypes (A1-A5) with the A1 stop condition.
5. Add S8 upstream-delta handling with pinned-commit invalidation.
6. Demote the 205-file cluster from primary evidence to regression fixture A3.

Items 1-3 and 6 are documentation-only and low cost. Item 4 is the decision
gate. Item 5 closes the one genuinely unserviced scenario. None requires
abandoning the revised plan's Designs 1-8, which remain endorsed as corrected
by the prior reconciliation.

## Process Notes

The finding most worth weighing first: the 170-corpus registry. It reframes
the whole program -- the absorption lifecycle is not missing, it is mature and
general, and TPGR's real job is to become the router the chain map already
names as its own gap. That reframing makes the required work smaller, not
larger.

The finding worth acting on fastest: the claim vocabulary. It is
documentation-only, costs almost nothing, and is the sole control against
stage-claim laundering -- the failure mode whose damage compounds silently
behind every inherited receipt.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| literalTokensReviewed | review headings; checker-read-ahead table fields; external-intake routing rows; epistemic fields; operation-trace labels; public disposition; exact claim boundary heading |
| gateRunPurpose | confirm the normalized advisory return satisfies governed-review evidence shape before CVF reconciliation |
| claimBoundary | checker conformance and advisory preservation only; no implementation or intake completion proof |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | returned architectural critique -> CVF source verification -> reviewer reconciliation -> operator decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing TPGR and absorption owner surfaces named in the reconciliation |
| Disposition | ADVISORY_INPUT_PENDING_RECONCILIATION |
| Claim boundary | external reasoning remains advisory until independently verified and dispositioned by CVF |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: this critique performs targeted source verification and
  registry aggregation only; it opens no scan, intake refresh, or new corpus
  completeness claim.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - the 170-entry count is a
  targeted aggregation of the current generated registry, not a new complete
  scan or semantic-completeness claim over those source corpora.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE_PLANNING.

Expected Result / Prediction: separating the existing absorption lifecycle
from TPGR routing should reduce duplicate governance design while exposing
whether the proposed R2 evidence set generalizes beyond the RSPB fixture.

Evidence Comparison: the critique compares the revised plan with canonical
absorption owners, the generated registry, and the recorded universal-router
gap; external conclusions remain subject to the CVF reconciliation.

Contradiction Or Gap Disposition: claims about lifecycle maturity, universal
registration, delta invalidation, claim-token enforcement, and R2 stop logic
require independent modification where the governed evidence is narrower.

Claim Update: the advisory disposition is
`SPLIT_TPGR_AND_ABSORPTION_ARCHITECTURE` with
`REVISE_R2_SCOPE_BEFORE_APPROVAL`; active TPGR authority remains unchanged.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | external reviewer return normalized by CVF reviewer/orchestrator |
| Provider or surface | operator-transferred advisory file in the local private provenance repository |
| Session or invocation | TPGR second-upgrade generalization critique, 2026-08-17 |
| Working directory | repository root |
| Command or tool surface | governed source reads, registry aggregation, SHA-256 verification, reviewer normalization |
| Target paths | this external critique only |
| Allowed scope source | operator requested a second external critique of the generalized absorption objective |
| Before status evidence | HEAD `532e4bd81bc4e927cbaa46b2f9a44bee18551a93`; returned critique untracked |
| After status evidence | advisory content preserved with governed-review wrapper; reconciliation still required |
| Diff evidence | exact changed-path review before material commit |
| Approval boundary | critique preservation and independent CVF reconciliation only |
| Claim boundary | no rule, checker, registry, catalog, selective execution, T15, runtime, provider/live, public, deployment, or production authorization |
| Agent type | external reviewer plus reviewer/orchestrator normalization |
| Invocation ID | `tpgr-second-upgrade-generalization-critique-20260817` |
| Expected manifest | this external critique only before separate reconciliation authoring |
| Actual changed set | this external critique only at normalization time |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private advisory review; public-sync is not authorized.

## Decision / Disposition

External advisory disposition:
`SPLIT_TPGR_AND_ABSORPTION_ARCHITECTURE` and
`REVISE_R2_SCOPE_BEFORE_APPROVAL`.

## Claim Boundary

This critique is advisory input only. It is not CVF authority and must not be
cited as canonical authority in Source Authority tables, Source Verification
ACCEPT rows, corpus manifests, closure proof, or roadmap/work-order evidence.
Every fact reported here must be re-verified against a CVF-governed surface
before use as evidence. It authorizes no implementation at any stage. It does
not enable selective execution; `selectiveExecutionAuthorized` remains false.
It does not open RSPB-AI-T15, change any standard/checker/registry/catalog/
hook, or promote the 205-file corpus (or the 764-file RSPB-AI-T0 corpus it is
part of) to authority. Measurements reported here (170 corpora, type/status
distributions, the RSPB registry entry, the 193/79 checker counts) are
discovery evidence from a read-only session, not verified CVF claims requiring
no further check. The prior reconciliation's `catalog-unwired` framing is
accepted and reused here without modification. Operator and the CVF
reviewer/orchestrator must reconcile this critique in a governed artifact
before any further decision. No file was created, modified, staged, or
committed in producing this critique beyond this review artifact itself; no
work order was created; no provider/live, network, public-sync, deployment,
destructive, or production action was taken. Repository state unchanged at
HEAD `532e4bd81bc4e927cbaa46b2f9a44bee18551a93`.
