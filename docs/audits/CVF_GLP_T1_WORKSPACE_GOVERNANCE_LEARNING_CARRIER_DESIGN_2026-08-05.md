# CVF GLP-T1 Workspace Governance Learning Carrier Design

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_WITH_CORRECTIONS

docType: audit

Date: 2026-08-05

Batch ID: GLP-T1

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_2026-08-05.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_2026-08-05.md`

dispatchBaseHead: `bdc6540ca`

executionBaseHead: `107a7a6a6`

r1ExecutionBaseHead: `a2b8d8220`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Select or reject the smallest safe carrier for the governance-latency
learning (same-scope authority continuity, real escalation boundaries, one
consolidated review pass, diminishing-return stop, dispatch-authenticated
Fast Doc eligibility) confirmed absent from the workspace propagation chain
by GLP-T0, comparing four candidates against one rubric.

## Target / Source

- `docs/reference/guard_orientation/README.md` (182 lines)
- `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` (235 lines)
- `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` (175 lines)
- `docs/reference/governance_control_index/CVF_GOVERNANCE_CONTROL_INDEX.md`
- `docs/reference/review_cost_control/README.md` and paired standard (347 lines)
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md`
- `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md`
- `workspace_overlay_catalog.json`; `workspace_overlay_profiles/` (15 files)
- accepted GLP-T0 audit and reviewer return at material commit `60884f5c0`

## Scope / Methodology

Read-only comparison. Reproduced current catalog membership for all four
carrier candidates with a direct query against `workspace_overlay_catalog.json`
(34 artifacts). Read the full current text of each candidate file to extract
exact section anchors, current line count, and semantic role. Applied one
decision rubric (semantic fit, discoverability, public safety, duplication
risk, drift/maintenance cost, profile reach, consumer reach, rollback
simplicity) to all four candidates without pre-selecting a winner. No
carrier, catalog, profile, template, or any other forbidden-scope path was
created or edited.

## Findings / Position

### Current catalog membership (reproduced)

```text
python -c "query workspace_overlay_catalog.json for guard-orientation-index,
  downstream-agents-template, governance-control-matrix" ->
guard-orientation-index: 1 hit
  path: docs/reference/guard_orientation/README.md
  selectionTags: [workspace-premium, downstream-governance, operator-orientation]
downstream-agents-template: 1 hit
  path: governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md
  selectionTags: [workspace-standard, downstream-governance]
governance-control-matrix: 1 hit
  path: docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md
  selectionTags: [workspace-premium, downstream-governance]

python -c "query for CVF_GOVERNANCE_CONTROL_INDEX, review_cost_control,
  WORKER_RETURN_QUALITY_GATE, GCI-010, GCI-017" ->
CVF_GOVERNANCE_CONTROL_INDEX: 0 hits
review_cost_control: 0 hits
WORKER_RETURN_QUALITY_GATE: 0 hits
GCI-010: 0 hits
GCI-017: 0 hits
```

This exactly reproduces the GC-018 baseline's Current Source Freshness
Verification. No contradicting evidence found.

### Profile reach of the three catalog-carried candidates

Using the profile-tag resolution reproduced during GLP-T0
(`Resolve-ProfileTags` recursive extends plus `includeSelectionTags`):

| Candidate | Selection tags | Reaches `operator-local` (7 resolved tags)? | Reaches `paid-user-safe`/`public-free`? |
|---|---|---|---|
| `guard-orientation-index` | `workspace-premium`, `downstream-governance`, `operator-orientation` | YES (operator-local resolves `downstream-governance` and `operator-orientation`) | NO (neither tag is in the `paid-user-safe`/`public-free` resolved set) |
| `governance-control-matrix` | `workspace-premium`, `downstream-governance` | YES (`downstream-governance` resolved) | NO |
| `downstream-agents-template` | `workspace-standard`, `downstream-governance` | YES | YES (`workspace-standard` is resolved by every profile including `public-free`) |

The downstream template is the only candidate with public/`paid-user-safe`
reach today. This matters for the public-safety comparison below: any
semantic added there is exposed far beyond the `operator-local`/premium tier
GLP-T0 identified as the actual gap (`operator-local` was the profile GLP-T0
compared, not `public-free`).

### Candidate 1 - `guard-orientation-index` (existing owner, amendment)

- **Current role**: task-first guard router; already has a `## Common Failure
  Patterns` table (a compact, one-row-per-pattern shape already used for
  comparable machine-checker-triggered friction) and a `## Task Class Guard
  Map` whose `Reviewer-return review` row already cites both
  `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`
  and `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md` as
  required reads for the reviewer role.
- **Semantic fit**: HIGH. The missing learning (same-scope authority
  continuity, real escalation boundaries, consolidated review pass,
  diminishing-return stop) is exactly a "what should a reviewer/dispatcher do
  at this decision point" rule, which is this file's stated purpose ("what
  guard surfaces to read, what blocks or outputs are required, what failure
  patterns to avoid").
  - Design Question 1 (self-contained without non-copied private paths): YES.
    The operational rule (points 1-5 of ADIF-0026's same-scope-continuity
    remediation) can be stated as five short, provider-neutral bullets with
    no incident chronology, no session ID, no operator name, and no quota
    number - all of which are absent from those five points already.
  - Design Question 3 (would amending the downstream template overgrow a
    high-blast-radius shared surface): not applicable to this candidate;
    answered under Candidate 3.
- **Discoverability**: HIGH. Already read by dispatcher, worker, and
  reviewer roles before governed artifact authoring per `## Read This First`
  step 1, and specifically named in the `Reviewer-return review` guard-map
  row, which is the exact role/task class where the missing learning applies.
- **Public safety**: the file's own `## Public Export Disposition` is not
  present as a top-level field (it is a `POINTER_RECORD`/`ACTIVE_REFERENCE`
  reference file, not itself flagged private), and its content is already
  operational guidance with no incident-specific detail - consistent with
  the pattern of the existing `## Common Failure Patterns` rows, none of
  which cite session dates, operator names, or quota numbers.
- **Duplication risk**: LOW. This does not create a new owner; ADIF-0026
  remains canonical source, this is a routing/summary row exactly like the
  file's other 24 `Common Failure Patterns` rows and Task Class Guard Map
  rows, none of which duplicate their source standard's full text.
- **Drift/maintenance cost**: LOW-MEDIUM. One additional guard-map row plus
  one additional failure-pattern row to keep aligned if ADIF-0026's
  same-scope-continuity list changes; comparable to the existing 12+
  guard-map rows' maintenance burden, not a new cost class.
- **Profile reach**: `operator-local` and all `downstream-governance` +
  `operator-orientation` premium profiles; correctly excludes `public-free`
  and `paid-user-safe`, matching GLP-T0's finding that the gap was observed
  in `operator-local`.
- **Rollback**: trivial - revert two added rows (one guard-map row, one
  failure-pattern row) in a single file; no catalog/profile change needed
  since the artifact is already catalog-registered.

### Candidate 2 - `governance-control-matrix` (existing owner, amendment)

- **Current role**: per its own `docs/reference/governance_control_index/CVF_GOVERNANCE_CONTROL_INDEX.md`
  relationship table, the control matrix is "owner and enforcement map" -
  "GCI consumes it as ownership evidence; the matrix remains the canonical
  owner/evidence map." It answers *which control owns what*, not *what should
  I do right now*.
- **Semantic fit**: LOW-MEDIUM (Design Question 2). Adding an operational
  same-scope-continuity rule here would make it discoverable only *after* an
  agent already knows to look up "who owns this control," not at the actual
  reviewer decision point during a live review. This directly answers Design
  Question 2 ("would the governance control matrix make the rule discoverable
  at the action point, or only classify ownership after the fact?"): the
  latter.
- **Discoverability at point of action**: LOW. Not named in the guard
  orientation Task Class Guard Map's `Reviewer-return review` row; a reviewer
  mid-review has no existing prompt to consult the control matrix for
  latency/authority guidance.
- **Duplication risk**: MEDIUM. Would create a second location (alongside
  guard orientation's existing ADIF-0026 citation) referencing the same
  underlying rule with a different framing, risking drift between an
  ownership-style entry here and an operational-style entry elsewhere.
- **Verdict**: not selected; weaker fit than Candidate 1 on the exact
  question the roadmap asked (a carrier that reaches the actual decision
  point, not merely an ownership index).

### Candidate 3 - `downstream-agents-template` (existing owner, amendment)

- **Current role**: generated directly into every new downstream project's
  agent instructions (`## Workspace Isolation Rule`, `## Risk Classification`
  at lines 158-171, `## Handoff and Tranche Closure Protocol`). This is the
  file GLP-T0 already confirmed has R0-R3 risk classification and independent
  review requirements but zero same-scope/avoidable-wait/review-cost
  vocabulary.
- **Semantic fit**: MEDIUM-HIGH for a downstream *project* agent, but the
  learning GLP-T0 found missing is a CVF-internal reviewer/dispatcher
  discipline (same-scope authority continuity across *this* provenance
  repository's own review rounds), not necessarily a rule a downstream
  project's own agent needs to enact on its own commits. The rule is about
  how a CVF *reviewer* should treat repeated confirmation requests during
  provenance-side review, which downstream projects do not perform.
- **Design Question 3 (blast radius)**: this is the highest-blast-radius
  candidate. `selectionTags: [workspace-standard, downstream-governance]`
  reaches `public-free` and `paid-user-safe`, i.e. every generated
  downstream project regardless of tier, per the profile-reach table above.
  Any addition here is public-facing content by default, requiring a stricter
  public-safety review than the other three catalog-carried candidates.
- **Duplication risk**: LOW if scoped correctly, but the content would
  overlap with guard orientation's Task Class Guard Map without downstream
  projects having their own reviewer role that consumes it identically.
- **Verdict**: not selected as primary carrier; correctly excluded from the
  minimal-change design because the confirmed gap (GLP-T0) is a provenance
  reviewer-side latency defect, not a downstream-project execution defect,
  and adding it here would expose internal reviewer-cost operational detail
  to every public/paid-user-safe profile without evidence that downstream
  project agents need it to execute their own tasks correctly.

### Candidate 4 - new compact public-safe carrier

- **Semantic fit**: would require inventing a new file and a new catalog
  entry purely to hold five bullets that already fit inside an existing,
  already-catalog-registered, already-role-appropriate file.
- **Discoverability**: would need a brand-new guard-map row pointing to it
  anyway (to be discoverable at the point of action), which duplicates most
  of the work of Candidate 1 while adding a new artifact class to maintain.
- **Duplication risk**: HIGH. Creates a second small governance-carrier
  family (alongside `review_cost_control/`) purely for workspace propagation,
  when guard orientation already exists as the single discoverable
  entrypoint for this exact class of guidance.
- **Drift/maintenance cost**: HIGHER than Candidate 1 - a new file needs its
  own catalog entry, its own front-door registration overhead, and its own
  future staleness tracking, none of which guard orientation needs since it
  is already catalog-registered and already maintained.
- **Verdict**: rejected per the roadmap's own governance-cost principle
  ("prefer modifying one existing distributed owner over adding a new owner
  only when semantic fit and discoverability are at least equivalent") -
  Candidate 1 has equal-or-better semantic fit and discoverability at lower
  cost, so a new carrier is not justified.

### Decision rubric summary

| Criterion | Guard orientation (C1) | Control matrix (C2) | Downstream template (C3) | New compact carrier (C4) |
|---|---|---|---|---|
| Semantic fit | HIGH | LOW-MEDIUM | MEDIUM-HIGH (wrong audience) | HIGH but unnecessary |
| Discoverability at action point | HIGH | LOW | MEDIUM (public download, not review time) | requires new row anyway |
| Public safety (default reach) | operator-local + premium only | operator-local + premium only | public-free + paid-user-safe (broadest) | depends on new tags chosen |
| Duplication risk | LOW | MEDIUM | LOW-MEDIUM (wrong owner) | HIGH (new family) |
| Drift/maintenance cost | LOW-MEDIUM | LOW-MEDIUM | MEDIUM (broad blast radius) | HIGH (new artifact class) |
| Rollback simplicity | trivial (revert 2 rows) | trivial | trivial but affects public reach | requires catalog entry removal too |

## R1 Consumer-Chain Repair

Independent review returned `REVIEW_CHANGES_REQUIRED_R1` on the original
first-pass analysis above. Per the redispatch instruction to preserve the
original recommendation and every reviewer disagreement rather than rewrite
history, the Findings / Position sections above (including the "Decision
rubric summary" table, "Answers To The Eight Design Questions", and the
original `exitRecommendation`) are retained unedited as the first-pass
record. This section is the R1 correction; the corrected final decision
appears in the repaired `carrierOwnerPath` through `exitRecommendation`
fields below, which now supersede the first-pass fields of the same name.

### R1-1: Corrected generated rule-pack path

The first-pass audit's projectConsumer field cited a false generated path
`<workspace>/.cvf-rule-pack/<profile>/source/...`. The actual default is
source-verified at `scripts/sync_cvf_workspace_rule_pack.ps1`:

```text
param(...)
    [string]$OutputDirName = "CVF_RULE_PACKS",
...
$outputRoot = Join-Path $workspaceRootResolved $OutputDirName
$profileRoot = Join-Path $outputRoot $ProfileName
$sourceRoot = Join-Path $profileRoot "source"
```

The correct generated path is
`<workspace>/CVF_RULE_PACKS/<profile>/source/<relativeSource>`, confirmed
against the script's own generated documentation at lines ~425-427
(`- $OutputDirName\$ProfileName\source\`). `docs/reference/CVF_WORKSPACE_RULES.md`
lines 179 and 214-216 independently confirm the same `CVF_RULE_PACKS/`
directory name and `CVF_RULE_PACKS/ACTIVE_RULE_PACK.json` active-manifest
path. `.cvf-rule-pack` does not appear anywhere in either source file; it was
an unverified first-pass error.

### R1-2: Copied-to-rule-pack is not mandatory project consumption

`docs/reference/CVF_WORKSPACE_RULES.md` lines 189-191 states directly:
"Rule packs are selected guidance, not full repository export. They do not
turn the workspace into the private full CVF repository and do not replace
project-level `AGENTS.md`, manifests, policies, or handoffs." This is a
source-backed statement that the rule-pack mechanism (which carries guard
orientation, control matrix, and any new compact carrier) is explicitly
**not** a project-mandatory consumption path - it is workspace-root
guidance a project agent may or may not read.

Separately, `scripts/new-cvf-workspace.ps1` lines 242-254 define the
generated project manifest's `requiredDocs` array. It contains
`.cvf/manifest.json`, `.cvf/policy.json`, `scripts/initialize_cvf_clone.ps1`,
`../WORKSPACE_RULES.md`, the bootstrap log, session-memory/state files,
`docs/INDEX.md`, and catalog-kit files. **None of the four T1 candidates
appear in `requiredDocs`.** `requiredDocs` is therefore not itself proof of
mandatory consumption for any candidate; it only proves guard orientation,
control matrix, and a new compact carrier are absent from it exactly as much
as the downstream template is.

The decisive distinguishing evidence is a separate, unconditional code path:
`scripts/new-cvf-workspace.ps1` lines 342-396 (`# CP1: Generate downstream
AGENTS.md from template`) directly reads
`governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
(line 343: `$agentsTemplatePath = Join-Path $cvfCorePath
"governance\toolkit\05_OPERATION\CVF_DOWNSTREAM_AGENTS_TEMPLATE.md"`) and
writes its substituted content directly into every new project's `AGENTS.md`
(line 344: `$downstreamAgentsPath = Join-Path $projectPath "AGENTS.md"`),
with placeholder substitution for `{{CVF_CORE_PATH}}`, `{{CVF_CORE_COMMIT}}`,
`{{BOOTSTRAP_DATE}}`, and `{{PROJECT_NAME}}` (lines 350-353). This happens
unconditionally on every project bootstrap - not gated by catalog tags,
profile selection, or `-AllowProvenanceContinuity`. On refresh, if the
existing `AGENTS.md` is CVF-generated (detected via the `Generated by CVF
workspace bootstrap` and `CVF Agent Instructions` markers, lines 362-365),
it is fully regenerated in place (line 368); if hand-edited, a merge block is
inserted at the top (lines 372-383) so the current template content is still
delivered to the project even when the project has diverged.

`CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` is additionally listed in
`$requiredPublicCoreFiles` at `scripts/new-cvf-workspace.ps1` line 83 - a
hard dependency the bootstrap script checks for before it will run at all,
unlike guard orientation, the control matrix, or any compact carrier, none
of which appear in that required-file list and none of which are read
anywhere in `new-cvf-workspace.ps1`.

This is the exact terminal link (`project bootstrap/adoption`) the roadmap's
authority chain names
(`provenance owner -> curated rule-pack catalog -> selected workspace
profile -> workspace guidance -> project bootstrap/adoption`) that the
first-pass audit did not verify. The rule-pack mechanism (Candidates 1-2 and
any new compact carrier under Candidate 4) terminates at "workspace
guidance"; only the downstream template continues unconditionally to
"project bootstrap/adoption."

### R1-3 and R1-4: Re-scored candidates against the full terminal chain

| Candidate | Reaches workspace guidance? | Reaches project bootstrap/adoption (mandatory, unconditional)? | Public-safety classification |
|---|---|---|---|
| `guard-orientation-index` | YES (`operator-local` + premium profiles via rule-pack sync) | NO - `CVF_WORKSPACE_RULES.md` lines 189-191 explicitly excludes rule packs from replacing/reaching project `AGENTS.md` | reach is bounded to `operator-local`/premium; not evaluated further because it fails the mandatory-consumer requirement |
| `governance-control-matrix` | YES (same premium-tier rule-pack reach) | NO - same rule-pack boundary as guard orientation | not evaluated further; same reason |
| `downstream-agents-template` | N/A (not rule-pack distributed; delivered by a separate unconditional bootstrap path) | YES - `new-cvf-workspace.ps1` lines 342-396, unconditional, every project, both fresh-install and refresh | reach is every generated project's `AGENTS.md` regardless of tier; this is a genuine public-safety question to classify (R1-4), not an automatic disqualifier per redispatch instruction 4 |
| new compact carrier | depends on chosen tags; if rule-pack distributed, same NO as C1/C2 | NO unless a new unconditional bootstrap code path were also added, which is out of T1/T2 scope (forbidden implementation) | not applicable; fails the mandatory-consumer requirement by construction unless bootstrap script itself is changed, which no T1/T2 scope authorizes |

Per redispatch instruction 4, broad project reach is a safety question to
classify, not automatic disqualification. Re-applying the same
`includedSemantics`/`excludedEvidence` boundary from the first-pass analysis
to the downstream template:

- The five compact rule bullets (same-scope authority continuity, real
  escalation-boundary list, consolidated review pass, round-three
  escalation, avoidable-wait framing) contain no incident chronology,
  operator identity, quota numbers, or raw dissent text - the same
  public-safe content already judged safe for guard orientation in the
  first-pass analysis. Public-safety content classification does not change
  when the carrier changes; only reach changes.
- The downstream template already carries comparably sensitive-looking
  operational content today (Mandatory Governance Proof, R0-R3 Risk
  Classification, Handoff and Tranche Closure Protocol) without an incident
  in its own history of exposing private evidence, because its authors
  already write operational rules, not private examples, into it - the same
  discipline this audit's `excludedEvidence` list enforces.
- Absence of a `## Public Export Disposition` field on the downstream
  template file itself is not evidence of unsafety (redispatch instruction
  4); the template's actual current content is the safety evidence, and it
  contains no such field one way or the other while still being
  operationally safe to generate into every project today.

Conclusion: the downstream template's broader reach is classified
`PUBLIC_SAFE_WITH_BOUNDARY`, not `DISQUALIFIED`, because the same exclusion
boundary that made guard orientation's amendment safe applies identically
here.

### R1-5: Corrected Markdown maintainability threshold

The first-pass Epistemic Process Block cited "182-line size (well under the
700-line markdown advisory threshold)" - the wrong threshold class. Per
`governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`
`#### active_markdown` section, the correct thresholds for non-archived
markdown intended for active reading or governed execution reference are
advisory `> 900` lines and hard `> 1200` lines, not the `general_source`/
`frontend_component` classes' 700/1000 numbers. The downstream template is
currently 235 lines; adding a compact Risk Classification companion section
of roughly 15-20 lines keeps it at approximately 250-255 lines, far below
even the corrected 900-line advisory threshold.

## Risk / Corrective Action

No corrective action was taken or is authorized by this audit; it is a
design comparison only, and no carrier, catalog, profile, or template path
was created or edited. The residual risk identified by the R1 correction is
different from the first-pass risk: if a future T2 implementation exposes
any `excludedEvidence` item in the downstream template's every-project reach
(broader than guard orientation's `operator-local`/premium reach), the
leakage blast radius is every generated project rather than a bounded
premium tier. The `negativeProof` plan in the R1-corrected schema below is
the corrective control for that specific risk and must run before any T2
closure, not merely be proposed. The original guard-orientation-only risk
note (incident-chronology leakage into a `workspace-premium` file) remains
accurate as a description of the first-pass candidate's own risk profile,
preserved below for the record.

## First-Pass Design Schema (superseded by R1 correction below)

The following `carrierOwnerPath` through `exitRecommendation` fields are the
original first-pass worker recommendation, preserved unedited per redispatch
instruction 7. They are superseded by the `## R1-Corrected Design Schema`
section further below, which is now the audit's operative recommendation.

### carrierOwnerPath (first-pass)

`docs/reference/guard_orientation/README.md`

### carrierForm (first-pass)

existing-owner amendment

### semanticFit (first-pass)

Guard orientation is the file every dispatcher/worker/reviewer role already
reads before governed artifact authoring (`## Read This First` step 1), and
its `Reviewer-return review` guard-map row already names ADIF-0026 and the
review-cost standard as required reads for exactly the role and task class
where GLP-T0 found the missing vocabulary. Amending it adds the missing
operational rule to the same row/table shape the file already uses, at the
exact point of action, without creating a new artifact class or exposing the
rule beyond the `operator-local`/premium tier GLP-T0 actually tested.

### includedSemantics (first-pass, unchanged content also used in R1)

Exactly five short, provider-neutral operational rules (restated compactly,
not copied verbatim from ADIF-0026's prose):

1. Same-scope authority persists across dependent repairs while objective,
   path/artifact class, risk ceiling, external-effect class, and commit
   owner stay unchanged; do not infer a one-repair-turn cap from a bare
   "continue" instruction.
2. Escalate for a real boundary change only: new objective or artifact
   class, new protected/out-of-scope path, increased risk, live/provider
   use, destructive/public/external action, secrets/quota, changed commit
   authority, or an explicit operator-set budget reached.
3. Complete one consolidated record/edge review matrix before the first
   repair; do not discover dependent findings one round at a time.
4. At round three with no independent new root cause, escalate
   (`REVIEW_COST_ESCALATION_REQUIRED`) instead of continuing micro-repair.
5. Repeated confirmation requests with none of the above boundary changes
   are avoidable operator wait, not governance safety.

### excludedEvidence (first-pass, unchanged content also used in R1)

- incident chronology and specific tranche names (e.g. SOT3-T2, WS2-T1)
  used as ADIF-0026's evidentiary examples;
- operator identity, session timestamps, or invocation IDs;
- exact quota/token/elapsed-minute numbers from any specific past review;
- raw reviewer dissent text or specific past finding content;
- any private provenance file path not already itself catalog-registered.

### catalogDisposition (first-pass)

Reuse existing entry. `guard-orientation-index` is already
catalog-registered with `selectionTags: [workspace-premium,
downstream-governance, operator-orientation]`; no new catalog entry, no tag
change, and no profile-file change is proposed. T2 would only edit the
already-registered file's content.

### profileExposure (first-pass)

No change to `workspace_overlay_catalog.json` or any profile file. The
existing tag set already yields the correct reach identified above:
`operator-local` and other `downstream-governance` + `operator-orientation`
profiles receive the amendment on their next rule-pack sync;
`public-free`/`paid-user-safe` do not.

### projectConsumer (first-pass - path corrected by R1-1, disagreement preserved)

The first-pass claim was: "the already-existing rule-pack sync path,
`scripts/sync_cvf_workspace_rule_pack.ps1` copies the catalog-registered file
into `<workspace>/.cvf-rule-pack/<profile>/source/docs/reference/guard_orientation/README.md`."
R1-1 above corrects the generated path to
`<workspace>/CVF_RULE_PACKS/<profile>/source/...` and, more importantly per
R1-2, this consumer path is workspace-root guidance, not a project-mandatory
read - `CVF_WORKSPACE_RULES.md` lines 189-191 state rule packs do not
replace project `AGENTS.md`. This field's original conclusion ("no new
consumer path is needed") is superseded by the R1-corrected schema below.

### driftOwner (first-pass)

Provenance maintainer of `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md`
remains the canonical source. Trigger for carrier refresh: any material
change to ADIF-0026's "Same-scope authority continuity" remediation list
(points 1-5 under "Same-scope authority continuity added after Governance
Latency WS2-T1") must be reflected in the guard-orientation amendment in the
same governed batch, per the existing pattern where guard orientation's
`Reviewer-return review` row already tracks ADIF-0026 and the review-cost
standard as required reads.

### T2AllowedPaths (first-pass implementationProofPlan)

Proposed bounded manifest for a future GLP-T2 (not authorized by this T1):

- `docs/reference/guard_orientation/README.md` (add one guard-map cross-
  reference note and one `## Common Failure Patterns` row, or a short new
  subsection near `## Task Class Guard Map`)

No other path. No catalog, profile, template, bootstrap, or checker file is
in the T2 proposed manifest.

### positiveProof (first-pass)

- exact-string assertion that the five compact rule bullets are present in
  `docs/reference/guard_orientation/README.md` after T2;
- catalog query confirms `guard-orientation-index` selection tags are
  unchanged (`workspace-premium`, `downstream-governance`,
  `operator-orientation`);
- reproduction of the GLP-T0 profile-tag/catalog-selection script confirms
  `operator-local`'s resolved 28-artifact set still includes
  `guard-orientation-index` and that the artifact's copied content in a
  disposable test workspace contains the five new bullets (deferred to T3
  per the roadmap's Work Plan, not executed by T1 or T2).

### negativeProof (first-pass)

- exact-string assertion that none of the excluded-evidence items (incident
  tranche names, operator identity, quota numbers, raw dissent text) appear
  in the amended guard-orientation file;
- catalog query confirms `public-free` and `paid-user-safe` resolved tag
  sets still do not intersect `guard-orientation-index`'s selection tags,
  i.e. the amendment does not newly reach public/paid-user-safe profiles;
- diff-based assertion that no other catalog artifact, profile file, or
  template file changed in the same T2 batch.

### rollback (first-pass)

Revert the single amended file
(`docs/reference/guard_orientation/README.md`) to its pre-T2 content in one
commit. No catalog, profile, or generated-workspace state requires separate
rollback because no such state is proposed to change.

## R1-Corrected Design Schema (operative recommendation)

The R1 consumer-chain evidence above changes the required schema answers.
This section is the audit's final, operative recommendation, superseding
every first-pass field above per the R1-1 through R1-5 corrections.

### carrierOwnerPath (R1-corrected)

`governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`

### carrierForm (R1-corrected)

existing-owner amendment

### semanticFit (R1-corrected)

The downstream template is the only candidate with a source-verified,
unconditional, mandatory project-adoption path (R1-2). The originating
operator finding was a downstream project repeating governance-latency
behavior (redispatch instruction 3); a downstream project's own agent can
only receive the same-scope-continuity rule through a file it is actually
guaranteed to have, and only the downstream template meets that bar. Adding
the rule to the existing `## Risk Classification` section (lines 158-171)
places it immediately adjacent to the R0-R3 risk table GLP-T0 already
identified as present but incomplete - the exact same section, not a new
one, keeping the amendment minimal and semantically co-located with the
related existing content.

### includedSemantics (R1-corrected)

Unchanged from the first-pass five bullets (see `### includedSemantics
(first-pass, unchanged content also used in R1)` above); public-safety
content does not change when the carrier changes, only reach does, per
R1-3/R1-4.

### excludedEvidence (R1-corrected)

Unchanged from the first-pass list (see `### excludedEvidence (first-pass,
unchanged content also used in R1)` above); the same five exclusions apply
regardless of carrier, and are now the binding boundary for a
broader-reaching file, making their enforcement in `negativeProof` below
more consequential than in the first-pass guard-orientation-only design.

### catalogDisposition (R1-corrected)

No change. The downstream template's project-adoption path
(`new-cvf-workspace.ps1` CP1) is independent of `workspace_overlay_catalog.json`
entirely - it is not rule-pack distributed, so there is no catalog entry to
reuse, add, or modify. `downstream-agents-template`'s existing catalog entry
(`selectionTags: [workspace-standard, downstream-governance]`) governs a
separate, secondary rule-pack-copy path into `operator-local`/premium/
`paid-user-safe`/`public-free` workspace roots; that catalog entry is
unaffected and requires no change.

### profileExposure (R1-corrected)

No catalog or profile-file change. The mandatory project-adoption reach is
not profile-gated: `new-cvf-workspace.ps1`'s CP1 step (lines 342-396) runs
for every generated project regardless of which `-Profile` the workspace
bootstrap used. The rule-pack copy of the same template file (existing
`downstream-agents-template` catalog entry) additionally reaches
`public-free`, `paid-user-safe`, and every `downstream-governance` profile
at the workspace-root level, unchanged from today.

### projectConsumer (R1-corrected)

`scripts/new-cvf-workspace.ps1` lines 342-396 (`# CP1: Generate downstream
AGENTS.md from template`): reads
`governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` and
writes its substituted content to `<project>/AGENTS.md` on every fresh
bootstrap; on refresh, fully regenerates in place if the existing file is
CVF-generated (lines 362-369), or inserts a merge block at the top if
hand-edited (lines 372-383) so the current template content still reaches
the project. This is the exact `project bootstrap/adoption` terminal link
the roadmap's authority chain names and the first-pass design did not reach.

### driftOwner (R1-corrected)

Same source owner as the first-pass design:
`docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md`
maintainer. Trigger for carrier refresh is identical: any material change to
ADIF-0026's "Same-scope authority continuity" remediation list (points 1-5)
must be reflected in the downstream-template amendment in the same governed
batch. The refresh mechanism differs from the first-pass design: existing
projects receive the update automatically on their next
`Update-CVF-Workspace.ps1`/bootstrap-refresh run (via the CP1 regeneration or
merge-block path), not only on next rule-pack sync.

### T2AllowedPaths (R1-corrected implementationProofPlan)

Proposed bounded manifest for a future GLP-T2 (not authorized by this T1):

- `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
  (add a compact companion subsection immediately after the existing
  `## Risk Classification` section, lines 158-171, containing the five
  `includedSemantics` bullets; no other section edited)
- `scripts/test_cvf_golden_downstream_bootstrap.ps1`
  (extend the existing hermetic fresh-bootstrap, second-bootstrap, and
  legacy/mixed-project fixtures with exact carrier-delivery, refresh,
  private-leakage, merge-block, and byte-preservation assertions)

No other path. No catalog, profile, bootstrap script, or checker file is in
the T2 proposed manifest - the bootstrap script's CP1 logic already performs
the required substitution and delivery. The existing golden harness is the
focused test owner; T2 changes only the template's static content and its
hermetic regression assertions, not the delivery mechanism.

### positiveProof (R1-corrected)

- exact-string assertion that the five compact rule bullets are present in
  `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
  immediately after `## Risk Classification` following T2;
- run `powershell -ExecutionPolicy Bypass -File
  scripts/test_cvf_golden_downstream_bootstrap.ps1`; extend its existing
  hermetic local-core fixture so the first generated `<project>/AGENTS.md`
  must contain all five bullets, proving actual CP1 project adoption without
  network use;
- after the harness's existing second-bootstrap refresh, assert that the same
  CVF-generated `AGENTS.md` still contains exactly one carrier subsection and
  all five bullets, proving refresh delivery and idempotency.

### negativeProof (R1-corrected)

- harness assertions that the amended template and each generated
  `AGENTS.md` contain none of the exact private-evidence sentinels selected
  from `excludedEvidence`, including `SOT3-T2`, `WS2-T1`, private source
  paths, raw dissent text, operator/session identifiers, or incident-specific
  quota values;
- extend the harness's legacy/mixed-project fixture with a hand-edited
  `AGENTS.md`; assert that bootstrap inserts exactly one CVF merge block,
  delivers all five bullets inside it, and preserves the pre-existing bytes
  outside that block;
- diff-based assertion that no catalog, profile, or bootstrap-script path
  changed in the same T2 batch - only the template's static content changed.

### rollback (R1-corrected)

Revert the template and its matching golden-harness assertions to their
pre-T2 content in one commit. Because CP1 reads the template fresh on every
bootstrap/refresh invocation rather than caching it, a reverted template is
immediately reflected in any subsequent project generation or refresh with
no additional generated-state cleanup required. Projects that already
received the T2 content in their `AGENTS.md` before rollback are not
automatically reverted - the same asymmetry that applies to any change to
this already-existing, already-mandatory template today - and is out of T1/
T2 scope to solve.

## Governance Cost Budget Evidence

- Candidates compared: 4 (all against one shared rubric, first-pass and R1).
- Catalog queries run: 2 (three-candidate membership; three-name negative
  search for uncataloged surfaces); unchanged by R1 because the decisive R1
  evidence is bootstrap-script source, not a catalog query.
- Source files fully read: 7 first-pass (guard orientation, downstream
  template, control matrix, control index, review-cost README, ADIF-0026,
  worker-return quality standard) plus 3 more read for R1
  (`scripts/new-cvf-workspace.ps1`, `docs/reference/CVF_WORKSPACE_RULES.md`
  in full, `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`
  threshold section) = 10 total.
- First-pass gate count: pre-implementation autorun gate run once at
  `107a7a6a6..HEAD` (zero-diff baseline confirmation) before first-pass
  writing; PASS. R1 gate count: pre-implementation autorun gate run once at
  `a2b8d8220..HEAD` (zero-diff baseline confirmation) before R1 edits; PASS.
- Repair round count: 1 (this R1 consumer-chain repair, in response to
  independent reviewer `REVIEW_CHANGES_REQUIRED_R1`).
- Operator wait classification: none; no operator checkpoint needed for R1
  per the redispatch's own statement that R1 needs no operator checkpoint.
- Recurring-cost judgment (R1-corrected): amending the downstream template is
  not the lowest-recurring-cost candidate in isolation (its every-project
  reach means broader review scrutiny per future amendment), but it is the
  only candidate that satisfies the mandatory-consumer requirement at all;
  recurring cost is evaluated against candidates that actually solve the
  problem, not against candidates that fail the requirement cheaply.

## Answers To The Eight Design Questions (R1-corrected)

1. **Can the selected carrier hold a self-contained rule without depending on
   non-copied private paths?** YES - the five compact bullets under
   `includedSemantics` contain no reference to a private-only path in either
   the first-pass or R1-corrected carrier; the content itself did not change,
   only the carrier file did (R1-3/R1-4).
2. **Would the control matrix make the rule discoverable at the action point,
   or only classify ownership after the fact?** Only after the fact - this
   first-pass finding is unchanged by R1 and remains a reason the control
   matrix is not selected.
3. **Would modifying the downstream template overgrow a high-blast-radius
   shared control surface?** R1-CORRECTED ANSWER: broad reach is a safety
   question to classify, not automatic disqualification (redispatch
   instruction 4); the content is classified `PUBLIC_SAFE_WITH_BOUNDARY`
   (R1-4), so overgrowing is not the deciding factor - mandatory consumption
   is (R1-2).
4. **Does a new compact carrier reduce recurring drift cost enough to justify
   a new catalog artifact?** NO, and R1 adds a second, decisive reason: a new
   compact carrier has no unconditional project-adoption path unless the
   bootstrap script itself is also changed, which is out of T1/T2 scope
   (R1-3 table, "new compact carrier" row).
5. **Which exact semantics are public-safe?** Unchanged: the five bullets
   under `includedSemantics`.
6. **Which evidence must remain private?** Unchanged: the five items under
   `excludedEvidence`.
7. **Which profile tags and project consumers should receive the carrier?**
   R1-CORRECTED ANSWER: no catalog/profile-tag change; the consumer is
   `scripts/new-cvf-workspace.ps1`'s CP1 step, which is unconditional and not
   profile-gated (R1-corrected `projectConsumer`/`profileExposure`).
8. **What deterministic T2 proof demonstrates inclusion, private leakage
   exclusion, idempotent refresh, and rollback?** See the R1-corrected
   `positiveProof`, `negativeProof`, and `rollback` fields above, which now
   include a disposable bootstrap-script invocation proving actual project
   adoption - the concrete gap R1 found in the first-pass proof plan.

## exitRecommendation

R1-corrected: `CARRIER_DESIGN_ACCEPTED`

Selected carrier: `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
(supersedes the first-pass `docs/reference/guard_orientation/README.md`
selection). The consumer chain to this carrier is mandatory and
source-verified per R1-2 (`scripts/new-cvf-workspace.ps1` lines 342-396,
unconditional on every project bootstrap and refresh), so
`STOP_NO_SAFE_CARRIER` is not warranted - a safe carrier with a proven
mandatory consumer exists.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`design specification`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "design specification" --role worker --lifecycle-phase pre-implementation --json`

## Negative Search And Collision Discipline

| Search | Root | Result | Disposition |
|---|---|---|---|
| GLP-T1 output path collision | `docs/audits/` and `docs/reviews/` | no pre-existing `*GLP_T1*` files before this worker session | ACCEPT |
| exact catalog paths for control index, review-cost family, worker-return quality standard | `workspace_overlay_catalog.json` | 0 hits for all three (reproduces GC-018 freshness verification) | ACCEPT |
| `.cvf-rule-pack` literal string (first-pass false path) | `scripts/sync_cvf_workspace_rule_pack.ps1`; `docs/reference/CVF_WORKSPACE_RULES.md` | 0 hits in either file; `CVF_RULE_PACKS` is the only generated-directory name present | ACCEPT_AS_R1_CORRECTION |
| `requiredDocs` array membership for all four T1 candidates | `scripts/new-cvf-workspace.ps1` lines 242-254 | 0 hits for guard orientation, control matrix, downstream template, or any compact-carrier path | ACCEPT_AS_R1_EVIDENCE |
| CP1 downstream `AGENTS.md` generation code path | `scripts/new-cvf-workspace.ps1` lines 342-396 | confirmed unconditional read of `CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` and write to project `AGENTS.md` on every fresh install and refresh | ACCEPT_AS_R1_DECISIVE_EVIDENCE |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_worker_experience_retrospective.py` |
| literalTokensReviewed | `SECTION_GROUPS["review"]` five heading groups; `FAST_DOC_REQUIRED_HEADINGS`; `SELF_DECLARE_MARKER`; `RESPONDS_MARKER`; `DISPATCH_WORK_ORDER_MARKER`; `PUBLIC_EXPORT_TOKENS`; `DELTA_FIELDS`; `AOT_FIELDS`; `DEFECT_CLASSES`; `LANES`; `RETRO_TOKEN`/`RETRO_NA_TOKEN`; external-knowledge intake trigger phrases (avoided verbatim in this file) |
| gateRunPurpose | confirm output-artifact shape after source-verified findings, not first discovery |
| claimBoundary | GLP-T1 documentation design audit only; no implementation or external-effect claim |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction (first-pass, preserved): guard orientation may
be the lowest-cost existing owner because it is already distributed and
already routes review-cost work, but a compact carrier may be safer if
self-contained semantics would overload the orientation index.

Evidence Comparison (first-pass, preserved): guard orientation's existing
`Reviewer-return review` row already cites ADIF-0026 and the review-cost
standard, and its existing `## Common Failure Patterns` table already holds
comparable compact rows for 25 other patterns without apparent overload;
adding one more row of similar size is consistent with the file's current
shape. The first-pass comparison cited the wrong Markdown threshold class
(700-line `general_source`/`frontend_component` advisory instead of the
900-line `active_markdown` advisory that actually governs this file) -
corrected in R1-5; the corrected threshold does not change the no-overload
conclusion for guard orientation's own size, but the citation itself was
wrong and is flagged here rather than silently fixed.

Contradiction Or Gap Disposition (R1-CORRECTED): the first-pass audit
treated "no evidence favored the downstream template" as support for
excluding it. R1 review found this backward: the first-pass audit never
checked whether guard orientation's rule-pack distribution reaches the
generated project at all, and source verification (R1-2) shows it does not
- `CVF_WORKSPACE_RULES.md` lines 189-191 explicitly state rule packs do not
replace project `AGENTS.md`. The gap was not a missing consideration
favoring guard orientation; it was an unverified assumption that any
catalog-distributed candidate reaches the same audience as the downstream
template. That assumption is now falsified by source evidence.

Claim Update (R1-CORRECTED): the first-pass prediction is INVALIDATED, not
confirmed. Guard orientation and the control matrix are lowest-cost only
among candidates that already fail the roadmap's own mandatory
`project bootstrap/adoption` requirement; they were never valid
alternatives to a candidate that actually reaches downstream project agents,
because the originating operator finding (a downstream project repeating
governance-latency behavior) can only be addressed by a carrier the
downstream project's own agent is guaranteed to read. The updated claim is:
the downstream template (Candidate 3) is selected because it is the only
candidate with a source-verified mandatory consumer, and its broader reach
is a classified, bounded safety question (`PUBLIC_SAFE_WITH_BOUNDARY`), not
a disqualifying cost.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this audit analyzes private provenance carrier-selection reasoning
and cites internal reviewer-cost/ADIF learning; it does not authorize
public-sync mutation. The R1-selected downstream template carrier itself
remains private provenance content at this time; a future public-safe
classification would need its own review before crossing the public-sync
boundary.

## Claim Boundary

This audit compares and recommends only. It does not implement, create, or
edit any carrier, catalog entry, profile, template, bootstrap, workspace, or
downstream artifact - including the disposable test-workspace invocations
described in the R1-corrected `positiveProof`/`negativeProof`, which are
proposed T2/T3 evidence steps, not actions this audit performs. It does not
authorize GLP-T2 implementation, provider/network use, push, deployment, or
production readiness. The R1-corrected `CARRIER_DESIGN_ACCEPTED`
recommendation (selecting the downstream template) is a worker recommendation
only; the independent reviewer/closer owns the accepted T1 exit decision.
This R1 repair makes no commit and creates no artifact beyond editing the two
already-existing worker-owned paths, per the redispatch's forbidden-scope
instruction.
