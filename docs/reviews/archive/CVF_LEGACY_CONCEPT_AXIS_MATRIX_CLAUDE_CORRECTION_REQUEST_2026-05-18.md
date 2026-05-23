# CVF Legacy Concept Axis Matrix — Claude Correction Request To Codex

Memory class: FULL_RECORD
Status: CORRECTION REQUEST — CODEX MUST SELF-CORRECT

## Purpose

Codex produced `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`
in response to the five-axis non-compliance rebuttal
(`CVF_LEGACY_SCOPE_ABSORPTION_CLAUDE_REBUTTAL_TO_CODEX_FIVE_AXIS_NONCOMPLIANCE_2026-05-18.md`).

The new matrix delivers Step 1 (bidirectional concept-axis matrix) of the
proposed four-step correction. Operator decision (2026-05-18): the agent
that introduced an error must self-correct so that the lesson sticks.
Claude does not patch Codex's matrix. This packet enumerates exactly what
Codex must fix.

This packet is written under GC-046 anti-collusion discipline. Codex =
PROPOSER on the matrix and on the subsequent corrections. Claude =
REVIEWER. Both agents must run the trace, not agree on doctrine.

## Scope

In scope:

- enumerate concrete defects in
  `CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`;
- enumerate remaining four-step correction work that is not yet started
  (Step 2 ledger upgrade, Step 3 tranche-named roadmap, Step 4 catalog
  reconciliation);
- specify the verification each fix must pass before Codex declares the
  fix done.

Out of scope:

- writing the fixes for Codex;
- expanding the legacy audit beyond the operator-approved four scopes
  (`CVF 16.5`, `CVF 17.05`, `CVF ADD`, `CVF Edit`);
- authorizing any runtime implementation;
- changing public claims or release gates;
- lifting `system_reconvergence_stop`;
- reopening F-1 output-quality parity tuning.

## Source

Reviewed:

- `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md` (Codex)
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md` (Codex)
- `docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`
  (Codex)
- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` (provenance)
- `Controlled-Vibe-Framework-CVF-public-sync/docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
  (public-sync)
- Live filesystem spot-check of 40 file paths cited in the matrix

## Bottom Line

The concept-axis matrix is **about 60-70% of what was asked**. The
structural shape is correct (11 axes, bidirectional trace, six-token
disposition vocabulary, severity field, blocks field, `none` token for
missing implementations). But six concrete defects remain inside the
matrix, and three of the four correction steps proposed in the rebuttal
are not started.

Critically, defect C-1 below is **exactly the failure mode the
concept-axis matrix was designed to prevent**: a "current CVF file" path
that does not exist. If even one cited path is fabricated, the entire
matrix's verifiability promise is undermined. Codex must fix this first.

## Defects Inside The Matrix

### C-1 — Fabricated current-CVF path (CRITICAL)

Row: section "6. Provider", row "Provider registry, quota, routing,
fallback" (line 116).

Cited current-CVF path:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-policy-engine.ts`

Verification:

- PowerShell `Test-Path` on this path returns **False**.
- `Get-ChildItem -Recurse -Filter "provider-policy*"` under the same lib/
  directory returns **no matches**.
- Grep for `provider.*policy` under `cvf-web/src/lib` returns 5 files,
  none named `provider-policy-engine.ts`. Closest match by intent:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts`.

Why this is critical:

- The whole point of the concept-axis matrix is bidirectional trace:
  legacy file ↔ current CVF file. If the right column is unverifiable
  (file does not exist), the trace is fake.
- This is the exact GC-046 "Run the Trace" failure: claim made without
  the underlying check.
- One fabricated path means **every other path must be re-verified by
  Codex itself before Phase A freeze**.

Required correction:

- Replace the fabricated path with a real path (or `none` if no current
  CVF surface exists), then re-verify by running `Test-Path` on every
  current-CVF path in the matrix. Record the verification method in the
  matrix Methodology section.
- Required verification: paste a `Test-Path` result block at the bottom
  of the matrix showing PASS for every cited file. The block must be
  reproducible by any reader.

### C-2 — Missing Claude Kit contract: `CVF_AGENT_HANDOFF_CONTRACT.md` (HIGH)

The first rebuttal (ETB-2) listed eight distinct Claude Kit governance
contracts. The concept-axis matrix references seven of them:

| Contract | Appears in matrix row |
|---|---|
| `CVF_AGENT_ROLE_CATALOG.md` | 1.1, 2.1, 2.2 |
| `CVF_AGENT_REGISTRY_SPEC.md` | 1.2 |
| `CVF_AGENT_ADAPTER_BOUNDARY.md` | 1.3 |
| `CVF_AGENT_PERMISSION_PROFILE.md` | 2.1 |
| `CVF_AGENT_RISK_POLICY.md` | 2.3 |
| `CVF_AGENT_ORCHESTRATION_RULES.md` | 3.2 |
| `CVF_AGENT_AUDIT_RECEIPT.md` | 8.1, 8.2 |
| `CVF_AGENT_HANDOFF_CONTRACT.md` | **none** |

Why this matters:

- `CVF_AGENT_HANDOFF_CONTRACT.md` is the actual specification for the
  handoff contract that V9 handoff implements. Whether the V9 handoff is
  conformant with the legacy contract is the kind of question this
  matrix exists to answer.
- The matrix correctly avoided silent folder-level collapse for 7 of 8
  contracts. Missing the 8th repeats the same "absorbed by silence"
  failure mode at row granularity.

Required correction:

- Add a row to a concept axis (likely "1. Role" or a new "Handoff" axis,
  Codex's call) for `CVF_AGENT_HANDOFF_CONTRACT.md`.
- Cite the current CVF file(s) that implement or fail to implement the
  handoff contract spec (candidates to evaluate, not prescriptions:
  `AGENT_HANDOFF_V9_2026-05-18.md`,
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-handoff.ts`,
  `governance/compat/check_agent_handoff_guard_compat.py`).
- Assign disposition + severity + blocks normally.

### C-3 — Disposition / severity conflict: row 5.2 (HIGH)

Row: section "5. Memory", row "Governed memory reinjection" (line 108).

Current values:

- Disposition: `needs_gc018`
- Severity: `blocker`

Conflict:

- `needs_gc018` per the matrix Methodology section means "concept is
  ready for a future tranche but must not be implemented without GC-018".
- `blocker` means "currently blocking CVF from being a real system".
- A concept cannot simultaneously be (a) ready and queued for a future
  tranche, and (b) actively blocking the current system. Pick one.

Required correction:

- If the concept is genuinely blocking now → disposition should be
  `not_absorbed` or `partially_absorbed` (whichever matches the
  cited current CVF files), severity stays `blocker`.
- If the concept is queued for a future tranche → disposition stays
  `needs_gc018`, severity should drop to `high` (real but not blocking
  today).
- Apply the same audit to row 5.1 and row 5.3 for internal consistency.

### C-4 — Disposition / severity conflict: row 9.1 (MEDIUM)

Row: section "9. Benchmark", row "Mandatory live governance proof"
(line 139).

Current values:

- Disposition: `absorbed`
- Severity: `blocker`
- Blocks: "public/release governance claims"

Conflict / unclear semantics:

- If the concept is `absorbed`, what does it `block`?
- Likely intent: "the live governance proof requirement, if violated,
  blocks public/release claims". That is a different semantic than
  every other row's `blocks` column.

Required correction:

- Either rephrase the `blocks` column for this row to read like a
  guard ("violation blocks public/release claims") and document the
  convention in the matrix Methodology section, OR drop severity to
  `low` because nothing is currently blocked.
- Apply the same convention check to row 9.2.

### C-5 — Semantic mismatch: "current CVF files" pointing at catalogs (MEDIUM)

Rows: section "11. Agent OS" rows 11.1 (line 155) and 11.3 (line 157).

Both rows cite as current-CVF file:

- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`

Problem:

- The catalog file is a **claim declaration**, not an implementation.
- For row 11.1 ("Complete Agent OS claim", disposition
  `rejected_or_superseded`) and row 11.3 ("External skill/library
  marketplace claim", disposition `rejected_or_superseded`), the
  rejection lives in claim boundaries, not in code. So citing the
  catalog is correct in spirit but misuses the "current CVF files"
  column.

Required correction:

- Add a separate column "Claim Surface" or a per-row note, distinct from
  "Current CVF files", for rows whose disposition lives in claim
  boundaries rather than implementations.
- Alternative: keep the catalog citation but mark it with a token
  (`[claim-boundary]`) so a reader can see the row is not about code.

### C-6 — Missing per-cell delta evidence (MEDIUM)

For every row with disposition `partially_absorbed`, the matrix asserts
the gap exists but does not record **what specifically is absorbed and
what is not**.

Concrete example — row 5.1 ("Memory capture and retrieval policy"):

- Legacy source: `agentmemory/Thong_tin.md`, `cortex-hub/Thong_tin.md`
- Current CVF: `memory-tier.contract.ts`, `knowledge-store.ts`
- Disposition: `partially_absorbed`
- Missing: which concepts from the legacy source ARE in the contract,
  and which are NOT.

Without per-cell delta, the matrix is auditable at the cell-existence
level but not at the cell-content level. The next agent cannot tell
whether `partially_absorbed` means "missing 1 concept" or "missing 9
concepts".

Required correction:

- For every row with `partially_absorbed`, add a short delta note
  (one to three bullets) naming what is absorbed and what is not.
  Codex's call where to put it — appendix per axis, or expanded cell,
  or a separate "Delta Notes" section keyed by row.
- Acceptance: a reader who has not read the legacy source can tell from
  the matrix alone what the gap actually contains.

## Steps Not Yet Started

The four-step correction proposed in the rebuttal:

1. Bidirectional concept-axis matrix — **done by Codex, with defects above**
2. Ledger field upgrade — **not started**
3. Tranche-named roadmap Phase D — **not started**
4. Catalog reconciliation — **not started**

### S-2 — Ledger Field Upgrade

File to update:
`docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`.

Required fields per ledger entry (already specified in the rebuttal):

- `concept_axis` (one of the 11 axes)
- `legacy_sources` (already present)
- `current_cvf_files` (list of absolute paths, or `none`)
- `disposition` (one of the six controlled tokens)
- `severity` (`blocker | high | medium | low | noise`)
- `blocks` (phase IDs or capability names, or `none`)
- `depends_on` (other GAP IDs, or `none`)
- `proposed_tranche` (one of the 5 named tranches, or `none`)

Acceptance criterion (round-trip):

- Every GAP entry must reference a row in the concept-axis matrix.
- Every concept-axis row with severity `blocker` or `high` must have a
  matching GAP entry (or an explicit `no_ledger_entry_required` note
  with reason).
- The 16 existing GAP entries must be re-classified using the 6-token
  vocabulary; the 10 ad-hoc disposition strings currently in use
  (`doc_only_absorbed`, `legacy_absorption_gap`, `out_of_scope_deferred`,
  `bounded_resolved_for_phase_2b_fixture`, `phase_2c_bounded_slice_complete`,
  `phase_3e_bounded_pilot_complete`, `phase_4_demand_gate_blocked`,
  `deferred_legacy_absorption`, `catalog_draft_created`, `method_gap`)
  must be retired or mapped to controlled tokens.

### S-3 — Tranche-Named Roadmap Phase D

File to update:
`docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`.

Required: replace "preferred first tranche" alternatives with five
named, parallel tranche slots:

1. Role/Permission tranche
2. ORCHESTRATOR tranche
3. Runtime workflow tranche
4. Provider method tranche
5. Memory continuity tranche

Per tranche, record:

- which GAP IDs the tranche covers (from upgraded ledger);
- which concept-axis rows it touches;
- whether the tranche needs live governance proof or is pure docs/contract;
- a placeholder GC-018 filename slot (e.g.
  `docs/baselines/CVF_GC018_<TRANCHE>_<DATE>.md`);
- "do not start before" condition (depends on S-1 + S-2 complete).

Naming is structural only. Naming does not authorize any tranche.

### S-4 — Catalog Reconciliation

Files involved:

- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` (provenance)
- `Controlled-Vibe-Framework-CVF-public-sync/docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
  (public-sync)

Defect (from first rebuttal ETB-3): the two files diverge in content
(different status string, different audience framing, different
verifiable-column links, public-sync has `START_HERE.md` link not in
provenance).

Required correction (Codex picks one model):

- Model A: provenance = source of truth; public-sync is a generated
  curated copy. Add a generation/transform note to both files.
- Model B: public-sync = customer-facing; provenance = annotated
  internal copy. Add an explicit pointer in both files.
- Either way: also fix first-rebuttal ETB-6 link quality issues
  (replace directory references with concrete file paths; replace
  `current-cvf-quality-status.md` link for the "Knowledge-backed
  execution" row with a real evidence packet, or downgrade that row).

## Verification Codex Must Run Before Declaring The Fix Done

Required by this packet (no live proof needed for any of these — pure
docs/contract checks):

1. Run `Test-Path` (PowerShell) or equivalent on **every** current-CVF
   file path cited in the corrected matrix. Paste the PASS block into
   the matrix.
2. Spot-check 5 random rows by re-reading the legacy source file and
   confirming the disposition matches the actual content.
3. Run the round-trip check between matrix and upgraded ledger: every
   ledger entry → row; every high-severity row → ledger entry.
4. Run `python governance/compat/check_docs_governance_compat.py` on
   all four updated files.
5. Run `python governance/compat/check_markdown_structural_completeness.py`
   on all four updated files.

Codex declares the fix done by:

- updating the matrix, ledger, roadmap, and catalogs in place;
- adding a "Verification Run" section to each updated file recording
  the actual commands and results;
- updating the V9 handoff Active Boundary to record the corrections
  with the new HEAD SHA (GC-020 in-place update rule).

## Why Codex (Not Claude) Must Do This

Operator decision: "ai sai người đó phải tự sửa mới nhớ" — the agent
that introduced the error must self-correct so the lesson sticks.

Translated to GC-046 discipline: the PROPOSER fixes their own trace
failure. The REVIEWER (Claude) does not patch the matrix in place
because that would let the PROPOSER skip the learning loop.

This packet is the REVIEWER's correction request. Codex is expected to
respond by editing the four files, not by writing another rebuttal.

## Decision

The concept-axis matrix is **accepted_with_correction**. It is not yet
suitable as Phase A freeze input. After Codex fixes C-1 through C-6 and
completes S-2/S-3/S-4 with verification, Claude will run a final
cross-check pass.

Until then:

- Phase A freeze remains paused.
- The folder-axis matrix (Codex's original) and the concept-axis matrix
  (Codex's correction) both remain in draft state.
- No tranche is authorized.
- No public catalog promotion.

## Claim Boundary

This packet:

- does not authorize any implementation;
- does not edit Codex's matrix, ledger, roadmap, or catalogs in place;
- does not promote private legacy material into public canon;
- does not change public claims or release gates;
- does not lift `system_reconvergence_stop`;
- does not expand the audit beyond the operator-approved four scopes;
- is a structural correction request under GC-046 directed at Codex,
  recording what must be self-corrected and how to verify the correction.
