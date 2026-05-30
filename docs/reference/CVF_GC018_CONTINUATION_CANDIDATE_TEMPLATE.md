# CVF GC-018 Continuation Candidate Template

Memory class: POINTER_RECORD

Status: reusable template for any future attempt to reopen a materially delivered roadmap under `GC-018`.

## Purpose

- provide one standard continuation packet for post-closure roadmap reopening
- make `GC-018` scoring comparable across waves
- reduce ambiguity about when a new batch is authorized versus merely proposed

## Scope / Applies-To

Applies to future continuation candidates that propose reopening a materially
delivered roadmap or wave under GC-018. It is a reusable authoring template,
not an authorization record by itself.

## Scope / Target / Owner Boundary

Target: GC-018 continuation candidate packets. Owner: CVF governance
documentation surface. This template must be copied into a concrete
candidate/review artifact before it can govern implementation.

## Claim Boundary

Using this template does not close, reopen, or authorize any roadmap. Closure,
reopening, and implementation authority require a filled candidate packet,
source verification where applicable, and the relevant autorun gates.

## When To Use

Use this template only when all of the following are true:

- the roadmap or wave is already marked `MATERIALLY DELIVERED`, `DEPTH-FROZEN`, or equivalent
- a proposer wants to reopen breadth expansion, semantic deepening, or proof-strengthening
- the proposer needs a reviewable `GC-018` decision before implementation begins

Do not use this template for:

- ordinary bug fixes on an already authorized active batch
- baseline-only reconciliation updates
- post-fix verification or closeout receipts

## Required Packet

Copy the following block into one reviewable artifact:

- roadmap update
- baseline delta
- reassessment addendum
- governance decision note

For absorption review packets (any packet produced by a multi-agent rebuttal chain governed by GC-046),
two additional blocks are required before a claim may be counted as convergence evidence:

```text
Evidence Trace Block (required per significant claim, per GC-046)
- Claim: <exact claim text>
- Command: <exact grep/find/read command used>
- Result: <count or representative output>
- Key path: <file:line for the key finding>
- Verdict: EXISTS | ABSENT | PARTIAL | DRIFT
- Counter-evidence (if any): <opposing agent's evidence>

Counter-Evidence Block (required when a REVIEWER challenges a PROPOSER claim)
- Claim challenged: <original claim text>
- Original evidence: <PROPOSER's command + result>
- Counter-evidence: <REVIEWER's command + result>
- Corrected verdict: <corrected claim text>
```

See `governance/toolkit/05_OPERATION/CVF_AGENT_REVIEW_ANTI_COLLUSION_GUARD.md` for the full protocol.

For any continuation candidate that touches Review-CVF pain points, memory,
graph knowledge, context building, operational intelligence, external
knowledge absorption, or legacy-source implementation, add this block before
scoping:

```text
Legacy Spec Scan Block (required for legacy-adjacent scope)
- Registry read: docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md
- Legacy folders scanned:
  - <path 1>
  - <path 2>
- Relevant source specs found:
  - <file or folder>
- Existing absorption evidence checked:
  - <review/baseline/roadmap path>
- Absorbed in this tranche:
  - <source file or concept>
- Explicitly deferred:
  - <source file or concept + reason>
- Out of scope:
  - <source file or concept + reason>
- Blindspot risk verdict: CLEAR | PARTIAL | BLOCKED
```

For any continuation candidate that absorbs, reopens, scopes, or implements
knowledge from `.private_reference/legacy/`, archived absorption packets,
external capability sources, Review-CVF pain points, memory, graph, workflow,
CLI/MCP/tool, provider, benchmark, context, or non-coder outcome surfaces, add
this block before implementation:

```text
Knowledge Absorption Blind-Spot Control Block
- Standard read: docs/reference/archive/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md
- Source inventory:
  - <root/family + file count>
- Prior absorption evidence resolved:
  - <registry/review/baseline/roadmap paths>
- Detailed source files used:
  - <file path>
- Source families skipped:
  - <family + reason>
- File-level accepted value:
  - <source path -> value>
- Owner-surface normalization:
  - <value -> existing CVF owner>
- Accept/defer/reject matrix:
  - <source/value -> disposition + reason>
- Adversarial roles completed:
  - Implementer: <finding>
  - Skeptic/Auditor: <finding>
  - Product/Operator Advocate: <finding>
  - Safety/Boundary Owner: <finding or N/A>
- Thin proof target:
  - <bounded proof>
- Blind-spot verdict: CLEAR | PARTIAL | BLOCKED
```

```text
GC-018 Continuation Candidate
- Candidate ID: <stable id>
- Date: <YYYY-MM-DD>
- Parent roadmap / wave: <path>
- Proposed scope: <short description>
- Continuation class: VALIDATION_TEST | PACKAGING_ONLY | TRUTH_CLAIM | REALIZATION | STRUCTURAL | MIXED | OTHER
- Active quality assessment: <path>
- Assessment date: <YYYY-MM-DD>
- Weighted total: <0.0..10.0/10>
- Lowest dimension: <dimension name> (<0.0..10.0/10>)
- Quality-first decision: REMEDIATE_FIRST | EXPAND_NOW
- Why expansion is still the better move now: <required if EXPAND_NOW>
- Quality protection commitments: <required if EXPAND_NOW>
- Remediation target if not expanding: <required if REMEDIATE_FIRST>
- Why now: <short justification>
- Active-path impact: NONE | LIMITED | MATERIAL
- Risk if deferred: <short description>
- Lateral alternative considered: YES | NO
- Why not lateral shift: <short justification>
- Real decision boundary improved: YES | NO
- Expected enforcement class:
  - RUNTIME_GUARD | GATEWAY_PRECONDITION | APPROVAL_CHECKPOINT | CI_REPO_GATE | GOVERNANCE_DECISION_GATE
- Required evidence if approved:
  - <artifact or test 1>
  - <artifact or test 2>

Depth Audit
- Risk reduction: <0|1|2>
- Decision value: <0|1|2>
- Machine enforceability: <0|1|2>
- Operational efficiency: <0|1|2>
- Portfolio priority: <0|1|2>
- Total: <0..10>
- Decision: CONTINUE | REVIEW REQUIRED | DEFER
- Reason: <short justification>

Authorization Boundary
- Authorized now: YES | NO
- If YES, next batch name: <planned batch>
- If NO, reopen trigger: <fresh reassessment or new candidate condition>
```

## Tranche Closure Checklist (mandatory before filing closure packet)

Every tranche closure packet must include this checklist. Each item must
be explicitly ticked or marked N/A with a one-line reason.

```text
Tranche Closure Checklist
- [ ] Public catalog updated OR explicitly N/A: <reason>
      If new proven capability added → add row to catalog capability table
      If new/extended extension → add/update extension inventory row
      If row status upgraded → update status + evidence link
      Catalog path (public-sync): docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md
- [ ] All new catalog paths Test-Path verified in public-sync clone
- [ ] GC-020 handoff Current HEAD updated to this tranche's commit SHA
- [ ] Evidence Trace Block present for all significant claims (GC-046)
- [ ] Legacy Spec Scan Block present OR explicitly N/A: <reason>
- [ ] Knowledge Absorption Blind-Spot Control Block present OR explicitly N/A:
      <reason>
```

Omitting the catalog item without an explicit N/A is a closure defect.
The pre-commit advisory (GC-024) will remind the agent at commit time,
but the checklist is the authoritative closure gate.

## Reading Rules

- every fresh `GC-018` packet must read and cite the active quality assessment before claiming expansion is the right next move
- if the current quality posture triggers the standard's remediation-first conditions, the packet should default to `Quality-first decision: REMEDIATE_FIRST`
- `Quality-first decision: EXPAND_NOW` requires a higher-value justification plus explicit quality protection commitments
- `Authorized now: YES` should only appear if the score satisfies the current `GC-018` threshold and no hard-stop override is triggered.
- any `0` in `Risk reduction`, `Decision value`, or `Machine enforceability` should force `Decision: DEFER`
- if the proposed step changes active-path implementation, the resulting packet must remain reviewable by the repository continuation gate
- low-yield continuation classes (`VALIDATION_TEST`, `PACKAGING_ONLY`, `TRUTH_CLAIM`) must record a lateral alternative and may continue only if they improve a real decision boundary in a reviewable way
- legacy-adjacent packets must not scope from active reviews alone; they must
  reconcile the active review with `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
  and any relevant `.private_reference/legacy/` source folders before the
  candidate can be treated as complete
- knowledge-absorption packets must follow
  `docs/reference/archive/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
  and must include the Knowledge Absorption Blind-Spot Control Block before any
  implementation begins

## Preferred Placement

For system-level continuation, prefer one of:

- `docs/roadmaps/...`
- `docs/baselines/...`
- `docs/reviews/...`

The same packet may be summarized in multiple places, but there should be one obvious canonical source.

## Related Controls

- `governance/toolkit/05_OPERATION/CVF_DEPTH_AUDIT_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_AGENT_REVIEW_ANTI_COLLUSION_GUARD.md` (GC-046: Evidence Trace Block requirement for absorption review chains)
- `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md#GC-018`
- `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `docs/reference/archive/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- `governance/compat/check_depth_audit_continuation_compat.py`
- `docs/roadmaps/CVF_SYSTEM_UNIFICATION_REMEDIATION_ROADMAP_2026-03-19.md`
