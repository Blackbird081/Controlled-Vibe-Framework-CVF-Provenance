# CVF Legacy Scope Absorption — Claude Rebuttal: Five-Axis Non-Compliance

Memory class: FULL_RECORD
Status: CLAUDE REBUTTAL — STRUCTURAL CRITIQUE OF CODEX METHODOLOGY

## Purpose

Record the second-pass Claude rebuttal to Codex's 2026-05-18 four-scope
legacy absorption audit deliverables.

The first rebuttal
(`CVF_LEGACY_SCOPE_ABSORPTION_CLAUDE_REBUTTAL_2026-05-18.md`) challenged
specific content errors (file counts, Claude Kit decomposition, catalog
divergence, GAP-17.05-002 priority).

This second rebuttal is structural: it shows that the underlying methodology
Codex used does not match the five-axis methodology the operator approved
before the audit started. The content errors caught in the first rebuttal
are symptoms; the methodology gap is the cause.

This rebuttal is written under GC-046 anti-collusion discipline. Codex =
PROPOSER, Claude = REVIEWER. Both agents have previously failed the
"agree on doctrine without running the trace" failure mode. This packet
runs the trace at the methodology level.

## Scope

In scope:

- audit Codex's deliverables against the operator-approved five-axis
  methodology;
- identify which axes were partially or fully missed;
- name the structural risk that the missed axes create;
- propose a concrete correction path that does not re-do already-completed
  4-folder enumeration, but adds the missing structural artifacts.

Out of scope:

- expanding audit beyond the operator-approved four folders
  (`CVF 16.5`, `CVF 17.05`, `CVF ADD`, `CVF Edit`) — operator confirmed
  on 2026-05-18 that the other three legacy folders are intentionally
  excluded;
- authorizing implementation of any gap;
- changing public claims;
- promoting private legacy into public canon;
- reopening F-1 output-quality parity tuning.

## Source

Operator-approved methodology (the "five axes"), as stated by the operator
on 2026-05-18 before the audit:

1. **Inventory toàn bộ `.private_reference/legacy/`** (within approved
   scope) — liệt kê folder/file theo nguồn, chủ đề, độ liên quan; không
   implement ngay.
2. **Legacy concept extraction** — rút ra các concept axis: role,
   permission, orchestrator, runtime, memory, provider, workflow, receipt,
   benchmark, UI/noncoder, agent OS.
3. **Absorption status matrix** with six dispositions: `absorbed`,
   `partially_absorbed`, `doc_only`, `not_absorbed`,
   `rejected_or_superseded`, `needs_gc018`.
4. **Gap severity + dependency map** — cái nào đang block CVF thành
   "system thật"; cái nào chỉ optional/noise.
5. **Roadmap hóa theo tranche** — Role/Permission tranche, ORCHESTRATOR
   tranche, Runtime workflow tranche, Provider method tranche, Memory
   continuity tranche; mỗi tranche có GC-018 riêng trước khi implement.

Operator's binding constraint:

> "Cần một ledger/matrix có trace từng concept về file legacy cụ thể, rồi
> đối chiếu với code/docs hiện tại. Như vậy mới chống bỏ sót được."

Codex deliverables reviewed:

- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`
- `docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`
- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- public-sync `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_CLAUDE_REBUTTAL_PACKET_2026-05-18.md`
  (the rebuttal request Codex issued)

## Bottom Line

Codex delivered four artifacts that satisfy the **surface** of the five
axes (something exists for inventory, classification, ledger, roadmap, and
catalog) but fail the **structure** of three axes (concept extraction,
status vocabulary, severity/dependency map) and partially fail two
(inventory completeness inside scope, tranche naming).

The first-rebuttal content errors (Claude Kit collapsed, file counts off,
catalog divergence, GAP-17.05-002 demoted) are not isolated mistakes —
they are predictable consequences of the structural gaps. Fixing them
case-by-case treats symptoms. Fixing the structure prevents the next
audit pass from repeating the same failure mode.

## Risk / Corrective Action

Risk:

- Without a concept-axis matrix, six-token disposition vocabulary,
  severity/dependency fields, named tranche slots, and bidirectional source
  trace, the audit remains difficult to verify and can recreate the
  "surface-scan-only" failure mode.

Corrective action:

- Add a bidirectional concept-axis matrix.
- Upgrade the gap ledger with concept axis, current CVF files, controlled
  disposition, severity, dependency, and proposed tranche.
- Name the future tranches inside the roadmap while keeping implementation
  blocked until separate GC-018 packets exist.

## Axis-by-Axis Compliance

### Axis 1 — Inventory toàn bộ (within approved scope)

What the operator asked for:
list folder/file by source, theme, and relevance for all four approved
scopes; no implementation.

What Codex delivered:
matrix "Reviewed Source" table with file counts per scope and primary
source role per scope.

Compliance: **MOSTLY MET**.

Defects (already in first rebuttal):

- File counts wrong in 2 of 4 scopes (CVF 16.5 stated 99, actual 100;
  CVF ADD stated 157, actual 167).
- No theme/relevance column at the file level — only at the folder level.
- `CVF 16.5/REVIEW FOLDER` listed in folder tree but not in the matrix
  table.

Verdict: accept_with_correction. Re-run file count; add a folder-level
theme/relevance signal.

### Axis 2 — Legacy concept extraction

What the operator asked for:
extract concepts along eleven concept axes: role, permission,
orchestrator, runtime, memory, provider, workflow, receipt, benchmark,
UI/noncoder, agent OS.

What Codex delivered:
matrix organized by **folder axis** (each folder has one row); concept
extraction is implicit and scattered across folder rows.

Compliance: **STRUCTURALLY MISSING**.

Why this is the root cause of several first-rebuttal findings:

- Claude Kit collapse (first rebuttal ETB-2) happens because the matrix
  is folder-axis. If the matrix were concept-axis, the eight Claude Kit
  contracts would each contribute to multiple concept rows (role,
  permission, orchestrator, receipt) and could not be silently collapsed.
- Cross-scope diagnosis flattening (first rebuttal ETB-5) happens
  because there is no concept-axis view to see which concepts span
  multiple scopes and which are scope-local.
- Missed concepts (first rebuttal "Missed Concepts" section) happens
  because folder-axis extraction has no slot for "this concept appears
  in folder X but is also implied by sub-contract Y in folder Z."

Verdict: reject. A concept-axis matrix must be added; the folder matrix
can stay as a complementary view.

### Axis 3 — Absorption status matrix with six dispositions

What the operator asked for:
six dispositions — `absorbed`, `partially_absorbed`, `doc_only`,
`not_absorbed`, `rejected_or_superseded`, `needs_gc018`.

What Codex delivered:
four dispositions — `absorbed`, `partially_absorbed`, `not_absorbed`,
`rejected_or_reference_only`.

Compliance: **PARTIAL — 4 of 6 dispositions**.

Missing dispositions and why they matter:

- `doc_only`: distinguishes "CVF has the doctrine document" from
  "CVF has runtime enforcement". Without this, `absorbed` is overloaded
  with at least two different absorption strengths. Concrete cost:
  CVF ADD `AGENT ENGINEER` is marked `absorbed as doctrine` — that is
  effectively `doc_only` but recorded under the same word as
  contract-level absorption.
- `needs_gc018`: marks a concept as ready to enter a GC-018 tranche
  without committing to absorption strength yet. Without this, ledger
  dispositions like `doc_only_absorbed`, `legacy_absorption_gap`,
  `out_of_scope_deferred`, `bounded_resolved_for_phase_2b_fixture`,
  `phase_2c_bounded_slice_complete`, `phase_3e_bounded_pilot_complete`,
  `phase_4_demand_gate_blocked`, `deferred_legacy_absorption`,
  `catalog_draft_created`, `method_gap` proliferate ad-hoc.

The current ledger has at least **10 distinct disposition strings** for
16 entries. That is not a controlled vocabulary; it is freeform notes
formatted as labels.

Verdict: reject as a controlled vocabulary. Adopt the six-disposition
vocabulary or document an explicit reason to deviate.

### Axis 4 — Gap severity + dependency map

What the operator asked for:
identify which gaps block CVF from becoming "system thật"; identify
which gaps are optional or noise; map dependencies between gaps.

What Codex delivered:
16 ledger entries with "Phase impact" prose; no severity field; no
dependency graph; no signal for "block real system" vs "noise".

Compliance: **MISSING**.

Why this is the root cause of the GAP-17.05-002 demotion (first
rebuttal ETB-4):

- Without a severity column, GAP-17.05-002 looks like the other 15
  ledger entries.
- Without a dependency column, the fact that GAP-17.05-002 blocks
  broad Phase 2.B (a constraint already written into V9 handoff lines
  391-409) is invisible at ledger-scan time.
- Without an explicit "blocks CVF from becoming real system" flag,
  every gap reads as roadmap material with equal weight.

Concrete cost of the missing axis:

- The roadmap Phase C says "rank gaps by product value, governance
  risk, and implementation dependency" — but the input the roadmap
  needs (severity + dependency) does not exist in the ledger that
  feeds it. Phase C cannot execute its own acceptance criterion.

Verdict: reject. Severity and dependency must be added as ledger
fields before the ledger is frozen as Phase A input.

### Axis 5 — Roadmap hóa theo tranche

What the operator asked for:
named tranches (Role/Permission tranche, ORCHESTRATOR tranche, Runtime
workflow tranche, Provider method tranche, Memory continuity tranche);
each tranche has its own GC-018 before implementation.

What Codex delivered:
roadmap with Phase A (Knowledge Map Freeze), Phase B (Public Catalog
Baseline), Phase C (Gap Triage For Implementation), Phase D (First
Implementation Tranche).

Compliance: **PARTIAL**.

What works:

- Phase A/B/C/D sequence is sensible and respects the operator decision
  to defer broad absorption.
- Phase D names three candidate tranches at the very end: role/permission/
  orchestrator, external capability intake, memory reinjection.

What does not work:

- The tranches are listed as "preferred first tranche" alternatives, not
  as a parallel set of named tranches. The five-axis methodology expects
  five-ish named tranches, each with its own GC-018, run in priority
  order — not one tranche selected from a menu.
- Phase C does the gap triage but the gap triage cannot execute without
  Axis 4 inputs (severity + dependency).
- No tranche has a named owner surface, target outcome, or live-proof
  requirement at the tranche level.

Verdict: accept_with_correction. Keep Phase A/B/C/D as the meta-roadmap.
Inside Phase D, name the five tranches and reserve a GC-018 slot for
each.

## The Critical Operator Constraint That Was Missed

Operator's binding constraint, repeated:

> "Cần một ledger/matrix có trace từng concept về file legacy cụ thể, rồi
> đối chiếu với code/docs hiện tại."

This is a **bidirectional trace requirement**: for every concept, both
sides of the bridge must be named — the legacy source file(s) where the
concept lives, AND the current CVF file(s) (or absence) that implement
or fail to implement it.

What Codex delivered:
the matrix and ledger trace **one direction only**: from legacy source to
"CVF owner surface name" (a label like "guard contract, agent registry,
handoff guard, role taxonomy"). The CVF owner surface is not a file path
list; it is a category name.

Concrete cost:

- GAP-17.05-002 cites the legacy role catalog file but does not name a
  single current CVF file to compare it against. The claim "11 domain
  role IDs are more granular than current `AgentFunctionRole` values"
  is **a claim**, but the file
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-axis.contract.ts`
  is not referenced in the gap. The audit reader cannot verify the
  claim without rediscovering the comparison file independently.
- GAP-17.05-011 (memory) says "CVF has knowledge store, file-backed
  persistence, audit trail, continuity metadata, and memory governance
  docs". Five categories, zero file paths. Unverifiable.
- The pattern repeats for GAP-17.05-010, 012, 013, 014, 015.

This is precisely the **"đọc rồi báo DONE theo cảm tính"** failure mode
the operator flagged before the audit. Codex's deliverables read as
careful and bounded, but the structural trace they need to make that
care verifiable is absent.

## Why The Two Problems Are One Problem

The five-axis methodology and the bidirectional-trace constraint are
two angles on the same structural commitment:

```
The audit output must be machine-checkable.
```

- Concept-axis extraction (Axis 2) makes the rows checkable.
- Six-disposition vocabulary (Axis 3) makes the cells checkable.
- Severity + dependency map (Axis 4) makes the priority claim
  checkable.
- Named tranches with GC-018 slots (Axis 5) make the next-step claim
  checkable.
- Bidirectional trace makes each individual absorption claim checkable.

Without these structural commitments, the audit deliverable becomes a
collection of careful-sounding paragraphs that cannot be verified
without redoing the audit. That is exactly the failure mode GC-046 was
written to block at the multi-agent review level — and it has now
appeared at the audit-product level instead.

## Solution — Proposal For Operator Decision

This rebuttal proposes a two-step correction that does not throw away
Codex's existing four artifacts, but adds the structural artifacts that
make them machine-checkable.

### Step 1 — Bidirectional Concept-Axis Matrix (zero runtime)

Create a new artifact:
`docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`.

Structure: one section per concept axis (eleven total). Inside each
concept, a table:

| Concept sub-item | Legacy source files (provenance paths) | Current CVF files (or `none`) | Disposition (6-level) | Severity | Blocks |
|---|---|---|---|---|---|

Concept axes:

1. role
2. permission
3. orchestrator
4. runtime (state machine, lifecycle)
5. memory (capture, retrieval, reinjection)
6. provider (lane, method, gateway)
7. workflow (outcome, deliverable, step)
8. receipt (envelope, integrity, audit binding)
9. benchmark (live proof, DLP, deterministic consistency)
10. UI / noncoder (trusted form, deliverable pack, execute path)
11. agent OS (composition claim, end-to-end loop, hardening posture)

Acceptance criteria for this matrix:

- every cell in the "Current CVF files" column is either a concrete
  file path or the literal token `none`;
- every disposition value is one of the six approved tokens;
- every row with severity ≥ high has a `blocks` value (which CVF
  capability or roadmap phase it blocks);
- every concept sub-item appears in exactly one row (no silent
  collapse).

This is pure docs/contract work. No runtime, no live proof, no
implementation. It can be done before any GC-018 tranche is filed.

### Step 2 — Ledger Field Upgrade

Update `CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md` so each
entry has:

- `concept_axis`: which of the 11 concept axes it belongs to;
- `legacy_sources`: list of absolute legacy file paths (already
  present);
- `current_cvf_files`: list of absolute current CVF file paths or
  `none`;
- `disposition`: one of the six approved tokens;
- `severity`: `blocker | high | medium | low | noise`;
- `blocks`: list of phase IDs or capability names that this gap
  blocks (or `none`);
- `depends_on`: list of other GAP IDs this gap depends on (or `none`);
- `proposed_tranche`: which named tranche (Role/Permission, ORCHESTRATOR,
  Runtime workflow, Provider method, Memory continuity, or `none`) this
  gap belongs to.

Acceptance criterion: the ledger must round-trip with the concept-axis
matrix. Every GAP entry must reference a row in the matrix; every
high-severity matrix row must have a GAP entry.

### Step 3 — Tranche-Named Roadmap Phase D

Update the roadmap so Phase D lists five named tranches:

- Role/Permission tranche
- ORCHESTRATOR tranche
- Runtime workflow tranche
- Provider method tranche
- Memory continuity tranche

Each tranche entry has:

- which GAP IDs it covers;
- which legacy concept axes it touches;
- whether it needs live governance proof or is pure docs/contract;
- a placeholder GC-018 filename slot;
- a "do not start before" condition (dependency on Step 1 + Step 2).

This does not authorize any tranche to start; it only names them so
operator and agents share the same vocabulary going forward.

### Step 4 — Catalog Reconciliation (carried over from first rebuttal)

Resolve provenance vs public-sync divergence (first rebuttal ETB-3) and
link-quality issues (first rebuttal ETB-6) before promoting the catalog
to customer-facing. This is independent of Steps 1-3 and can run in
parallel.

## What This Rebuttal Does Not Ask

- Does not ask Codex to redo the four-folder enumeration. The
  enumeration is mostly correct; only file counts need a quick re-run.
- Does not ask for any tranche to start runtime work.
- Does not ask for the public catalog to be promoted to customer-facing.
- Does not ask for expansion beyond the four approved legacy folders.
- Does not ask for any external repository to be absorbed.
- Does not lift `system_reconvergence_stop`.

## Decision

Codex's deliverables, against the operator-approved five-axis
methodology:

- Axis 1 (Inventory): **accept_with_correction** (file counts).
- Axis 2 (Concept extraction): **reject** as structurally absent;
  must be replaced with a concept-axis matrix.
- Axis 3 (Six-disposition vocabulary): **reject** as a controlled
  vocabulary; adopt six tokens.
- Axis 4 (Severity + dependency): **reject** as absent; add fields.
- Axis 5 (Named tranches): **accept_with_correction**; name the five
  tranches inside Phase D.

Bidirectional trace constraint: **reject** as absent in the current
matrix and ledger; required correction is the concept-axis matrix
(Step 1) plus the ledger field upgrade (Step 2).

This rebuttal therefore recommends:

- pause Phase A freeze of the legacy knowledge map until Steps 1-3 are
  complete;
- treat Codex's existing four artifacts as the starting baseline, not
  the freeze input;
- when Steps 1-3 are complete, re-run Phase A acceptance with both the
  folder matrix and the concept-axis matrix as inputs.

## Claim Boundary

This rebuttal:

- does not authorize any implementation;
- does not promote `.private_reference/legacy/` content into public canon;
- does not change public claims or release gates;
- does not lift `system_reconvergence_stop`;
- does not expand the audit beyond the operator-approved four scopes;
- does not reopen F-1 output-quality parity tuning;
- does not treat any mock-only check as governance proof;
- is a structural cross-check artifact under GC-046, producing concrete
  correction requests addressed to the operator and to the next Codex
  pass.
