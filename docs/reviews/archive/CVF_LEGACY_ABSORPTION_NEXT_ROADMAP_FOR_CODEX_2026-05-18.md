# CVF Legacy Absorption — Next Roadmap For Codex

Memory class: FULL_RECORD
Status: HAND-OFF FROM CLAUDE TO CODEX

> **BLOCKING NOTICE (2026-05-18, operator-issued):** Step 0 below
> ("Remove the route.ts GC-023 exception") is **blocking** for every other
> step. The one-shot `--no-verify` bypass that landed the legacy-audit
> commit `e15f4206` was approved for that single commit only. Codex must
> split `route.ts` back under 900 lines and convert the registry
> exception entry to a `RESOLVED` tombstone BEFORE starting Steps 1-6.
> The exception entry carries a `lockBoundary` that forbids bumping,
> cloning, or relabeling. Future commits on this path must NOT use
> `--no-verify`.

## Purpose

Hand the legacy absorption audit back to Codex with:

- a precise record of which corrections were already applied in-place by
  Claude (N-1..N-4),
- a complete, ordered list of what Codex must do next,
- the acceptance criteria for each step,
- the verification commands each step must pass before Codex declares it done.

This packet exists because the operator chose the rule "ai sai người đó
phải tự sửa mới nhớ" — the agent that introduced the error must fix it so
the lesson sticks. Claude already applied four in-place fixes (N-1..N-4)
that could not wait without breaking Phase A acceptance. Everything below
is for Codex.

## Scope

In scope for this hand-off:

- closure of the legacy absorption matrix, ledger, roadmap, and catalog
  pair so they form a single coherent Phase A input;
- preparation of Phase A freeze conditions;
- preparation of Phase B catalog-promotion conditions;
- recording verification evidence inside the four artifacts themselves.

Out of scope:

- expansion beyond the four operator-approved legacy folders
  (`CVF 16.5`, `CVF 17.05`, `CVF ADD`, `CVF Edit`);
- authorization of any runtime implementation tranche;
- public catalog promotion before Phase B acceptance is met;
- changing public claims or release gates;
- lifting `system_reconvergence_stop`;
- reopening F-1 output-quality parity tuning.

## Non-Goals

This roadmap does not authorize a runtime tranche, a public GA claim, a
release-gate change, a public-canon migration of private legacy material, a
new audit scope beyond the four approved folders, or any F-1 output-quality
parity tuning. These exclusions remain binding even after Phase A freezes.

## Source

Artifacts already in working tree (Codex's previous round + Claude N-1..N-4):

- `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`
- `docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`
- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` (provenance)
- `Controlled-Vibe-Framework-CVF-public-sync/docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
  (public-sync)

Correction-trace packets:

- `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_CLAUDE_CORRECTION_REQUEST_2026-05-18.md`
- This file.

## What Claude Already Fixed (N-1..N-4)

The following corrections were applied in-place by Claude after spot-checking
Codex's first correction round. Each is recorded with an inline
`Claude N-N rewrite:` note so Codex can see the failure mode without an
external packet.

### N-1 — Two fabricated paths in public-sync catalog

Location:
`Controlled-Vibe-Framework-CVF-public-sync/docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`,
Provider lanes row.

The first reconciliation round added:

- `docs/audits/alibaba-canary/INDEX.md`
- `docs/audits/deepseek-canary/INDEX.md`

Both paths exist in the provenance repository but `docs/audits/` is **empty
in the public-sync clone**. Claude removed both and left only
`docs/evidence/provider-lanes.md`. A new `Claude N-1 correction (2026-05-18)`
block was added in the Verification section recording the failure mode:
copying provenance paths into public-sync without re-verifying on the
public-sync filesystem reproduces the C-1 failure mode the matrix correction
was meant to retire.

### N-2 — Ten ad-hoc disposition strings rewritten

Location:
`docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`,
the Initial Entries section.

Codex's first round added a Controlled Vocabulary section and a Structured
Gap Crosswalk table at the top of the ledger, but the original 16 GAP
entries below kept their ad-hoc disposition strings. The strings
`doc_only_absorbed`, `method_gap`, `bounded_resolved_for_phase_2b_fixture`,
`out_of_scope_deferred`, `phase_2c_bounded_slice_complete`,
`phase_2c_3e_live_bundle_executed_phase_4_deferred`,
`phase_3e_bounded_pilot_complete`, `phase_4_demand_gate_blocked`,
`deferred_legacy_absorption`, and `catalog_draft_created` have all been
rewritten to one of the six controlled tokens. Each rewrite carries an
inline note `(Claude N-2 rewrite: replaces ad-hoc <token>; <reason>)`
so the failure mode is preserved in the audit trail.

### N-3 — Disposition conflicts between body and crosswalk

GAP-17.05-007 (consolidated live proof) body said
`phase_2c_3e_live_bundle_executed_phase_4_deferred` while the crosswalk
said `absorbed` + low severity. Body rewritten to `absorbed`. The Phase 4
deferral was duplicated across two GAPs; the body now points at
GAP-17.05-009 (provider method demand gate) for the deferral.

GAP-17.05-014 (graph/code-intelligence context) body said
`deferred_legacy_absorption` while the crosswalk said `not_absorbed`. The
crosswalk is correct (no current CVF owner surface exists for graph
context). Body rewritten to `not_absorbed` with an explanatory note that
`needs_gc018` was premature for this row because Phase D ranking has not
yet decided whether graph context enters any tranche.

### N-4 — Roadmap Phase A acceptance vocabulary mismatch

Location:
`docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`,
Phase A Tasks list.

The task list still used the legacy 4-level vocabulary
(`absorbed`, `partially_absorbed`, `not_absorbed`,
`rejected_or_reference_only`). Rewritten to reference the six-token
controlled vocabulary defined in the concept-axis matrix
(`absorbed`, `partially_absorbed`, `doc_only`, `not_absorbed`,
`rejected_or_superseded`, `needs_gc018`). Inline rewrite note records the
discrepancy.

## Work Plan

The work plan is the ordered Step 0 through Step 6 sequence below. Step 0 is
blocking and must be complete before Steps 1-6; Phase B and Phase D remain
future work and require fresh GC-018 authorization.

## What Codex Must Do Next — Ordered Steps

These are the only outstanding items between current working tree state and
Phase A freeze acceptance. Each step has acceptance criteria and a
verification command Codex must run before declaring the step done.

### Step 0 — Remove the route.ts GC-023 exception (BLOCKING — must be first)

Why: Operator's standing instruction (2026-05-18):

> "việc bypass dùng exception chỉ cho lần này thôi, phải khóa lại, và
> quan trọng là bắt Codex phải split lại cho về đúng guard"

The GC-023 exception entry for
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
was granted as a one-shot bypass during the legacy-audit commit
(`e15f4206`). It is locked in the registry with `lockBoundary` fields that
forbid bumping `approvedMaxLines`, cloning the entry to other files, or
relabeling the status. The exception is operator-temporary, not a
permanent cap.

This step is **blocking**. Steps 1-6 below are not authorized until Step 0
is complete.

Tasks:

1. Extract Phase 2.C `Create Product Brief` slice handling out of
   `route.ts` into the existing
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase2c-product-brief-slice.ts`
   module. `route.ts` should call into the slice module, not embed the
   slice logic.
2. Extract Phase 3.E emission code path out of `route.ts` into the existing
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/phase3e-operational-emission.ts`
   module on the same pattern. `route.ts` should call the emission helper,
   not contain it.
3. Run unit tests + the live Alibaba route test (already in repo) to
   confirm the bounded Phase 2.C / 3.E behavior is unchanged after split.
4. Update
   `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json`:
   change the route.ts exception entry's `status` from `ACTIVE_EXCEPTION`
   to `RESOLVED`; set `approvedMaxLines` to `1001` (i.e.
   `hardThresholdLines + 1`) so the entry becomes a tombstone for the
   audit trail without providing a usable cap. Do **not** delete the entry
   outright.
5. Run `python governance/compat/check_governed_file_size.py` and
   `python governance/compat/check_governed_exception_registry.py
   --enforce` to confirm route.ts no longer needs an exception and the
   registry is integrity-clean.
6. Commit as a single tranche. The commit MUST NOT use `--no-verify` —
   the hook chain must pass cleanly after split.

Acceptance criteria:

- `route.ts` is **below 900 lines** (the soft advisory threshold is 700;
  900 leaves headroom but stays well under the 1000-line hard threshold);
- Phase 2.C product-brief tests pass;
- Phase 3.E emission tests pass;
- the live Alibaba route test passes;
- the exception entry has `status: "RESOLVED"` and `approvedMaxLines: 1001`;
- `check_governed_file_size.py` and `check_governed_exception_registry.py
  --enforce` both PASS without `--no-verify`;
- the commit lands without skipping any hook.

Verification:

```bash
# 1. line count
wc -l EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts
# expected: < 900

# 2. governance checks
python governance/compat/check_governed_file_size.py
python governance/compat/check_governed_exception_registry.py --enforce

# 3. tests
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run test:run -- src/lib/phase2c-product-brief-slice.test.ts
npm run test:run -- src/lib/phase3e-operational-emission.test.ts
npm run test:run -- src/app/api/execute/route.test.ts
# live test requires Alibaba API key:
npm run test:run -- src/app/api/execute/route.phase2c-product-brief.alibaba.live.test.ts
```

Forbidden moves (each is a guard failure mode Codex must not take):

- **Do NOT** bump `approvedMaxLines` above 1100 — `lockBoundary.noBumpAllowed`
  is in effect and the guard will catch a `suspicious_bump` or
  `approved_max_changed_from_head` violation.
- **Do NOT** clone the same exception entry to a different path as
  precedent — `lockBoundary.noExtensionAllowed` is in effect; each new
  GC-023 violation requires its own operator approval.
- **Do NOT** delete the exception entry outright — the audit trail must
  show the bypass happened, the requirement that caused it, and the
  resolution.
- **Do NOT** use `git commit --no-verify` to land the split — the whole
  point of the lock is that the next commit on this path must pass guards
  cleanly.
- **Do NOT** mark Step 0 done until route.ts is below 900 lines AND the
  registry entry is in `RESOLVED` state.

### Step 1 — Public-sync verification discipline (CRITICAL)

Why: N-1 proved that "verify on provenance only" is not enough when Model B
is the chosen reconciliation model (public-sync = customer-facing
derivative).

Tasks:

1. Add a permanent rule to
   `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
   (provenance copy) stating: every public-sync catalog path must be
   `Test-Path`-verified on the public-sync filesystem before commit. Mirror
   the rule into the public-sync copy.
2. Add the rule to
   `governance/toolkit/05_OPERATION/CVF_AUDIT_PROTOCOL.md` (or the closest
   existing operation guard) so that future catalog reconciliations cannot
   re-introduce the same failure.
3. Choose: keep the rule advisory in docs only, OR add it as a compat check
   (`governance/compat/check_public_sync_catalog_paths.py` or extension of an
   existing compat script). Recommend: advisory first, automate later under
   a separate GC-018.

Acceptance criterion: a reader of the catalog can find the rule from the
catalog itself, not only from this hand-off packet.

Verification:

```powershell
# From provenance repo root, verify every public-sync path in the
# customer-facing catalog actually exists in the public-sync clone.
$publicSyncRoot = "d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync"
$catalog = Get-Content (Join-Path $publicSyncRoot "docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md") -Raw
# Extract the `Test-Path X` lines, verify each one.
```

Recommended: paste the resulting PASS list back into the catalog as evidence.

### Step 2 — Single source of truth for each GAP disposition

Why: Ledger now has two views — the Structured Gap Crosswalk table and the
Initial Entries body. N-3 found one conflict; spot-check found a second
(GAP-17.05-014). There may be more drift over time.

Tasks:

1. Add a one-paragraph note at the top of the Initial Entries section of
   `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`
   stating that the crosswalk table is the canonical disposition source and
   the body is supplementary narrative. Any future disagreement is resolved
   by editing the body to match the crosswalk.
2. Add a "Last reconciled with crosswalk" date stamp.
3. Re-read every body entry once more and confirm the disposition listed in
   the body matches the disposition in the crosswalk. If any mismatch
   remains, fix the body, not the crosswalk.

Acceptance criterion: a `grep`/`Grep` of every disposition token in the
body against the crosswalk produces zero mismatches.

Verification:

```bash
# For each GAP-17.05-NNN, compare disposition in body vs crosswalk row.
# Implementation note: do this by hand or with a small script; the result
# must be a 16/16 match.
```

### Step 3 — Matrix and ledger round-trip check

Why: the rebuttal required that every GAP entry must reference a row in the
concept-axis matrix, and every concept-axis row with severity `blocker` or
`high` must have a matching GAP entry. The crosswalk has `Matrix rows`
column but the matrix does not have a `Linked GAP IDs` column for the
reverse direction.

Tasks:

1. Add a `Linked GAPs` column to each concept-axis matrix table (11 tables)
   in `CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`. For each row, list the
   GAP-17.05-NNN IDs that cover it, or `none`.
2. Run the round-trip:
   - every GAP `Matrix rows` value → those rows in the matrix must list this
     GAP in their `Linked GAPs` column;
   - every matrix row with severity `blocker` or `high` → must either have a
     `Linked GAPs` value or carry an explicit `no_ledger_entry_required`
     note with reason.
3. Record the round-trip check result in the matrix's `Verification Run`
   section.

Acceptance criterion: the matrix is bidirectional (forward via
`Linked GAPs`, backward via the crosswalk's `Matrix rows`).

### Step 4 — Phase B catalog claim-link upgrade

Why: the first rebuttal ETB-6 flagged that some "proven" rows in the catalog
linked to directory references or to docs that did not back the claim.
Codex's reconciliation round partially fixed this for the public-sync copy
but not consistently for both copies.

Tasks:

1. For every catalog row with status `proven and active` or `proven and
   mandatory for release claims` or similar strong-claim wording, ensure the
   `What is verifiable` / `What to verify` cell links to **at least one
   concrete file** that materially backs the claim. Directory references
   alone are not acceptable.
2. Re-verify each link on both provenance and public-sync sides. Paste a
   per-side Test-Path PASS block into both catalogs.
3. The "Knowledge-backed execution" row: confirm
   `docs/evidence/cvf-16-5-runtime-absorption.md` (now used) actually
   demonstrates governed knowledge-backed execution; if it does not,
   downgrade the row from `proven` to `bounded`.

Acceptance criterion: every "proven" row has at least one file-level link
that, when opened by a reader, demonstrates the claim. No directory-only
links remain for "proven" rows.

### Step 5 — Phase A freeze packet

Why: only after Steps 1-4 are done does the legacy absorption knowledge map
become freezable as Phase A input. The roadmap explicitly says: "Do not
freeze Phase A legacy knowledge mapping until this matrix and the ledger
crosswalk agree."

Tasks:

1. Write a single closure packet:
   `docs/reviews/CVF_LEGACY_ABSORPTION_PHASE_A_FREEZE_<date>.md`.
2. The packet must declare:
   - which artifacts are now frozen (matrix, ledger, roadmap, both catalogs);
   - the HEAD SHA at which the freeze applies;
   - the list of corrections applied since first publication (C-1..C-6,
     S-2..S-4, N-1..N-4);
   - that no tranche is authorized by this freeze;
   - the GC-020 in-place update to V9 handoff Active Boundary.
3. Update V9 handoff Active Boundary with a new line:
   `Phase A legacy knowledge map freeze: ACCEPTED — commit <SHA>`.

Acceptance criterion: V9 handoff, freeze packet, and matrix/ledger/roadmap
all point at the same HEAD SHA. The GC-020 HEAD SHA machine check passes.

### Step 6 — Governance compat run + commit

Tasks:

1. Run the four compat checks against the updated files:

   ```bash
   python governance/compat/check_docs_governance_compat.py
   python governance/compat/check_memory_governance_compat.py
   python governance/compat/check_markdown_structural_completeness.py
   python governance/compat/check_agent_handoff_guard_compat.py
   ```

2. If any check fails, fix the cause (not the check). Common pitfalls:
   markdown structural completeness on the long ledger; agent-handoff guard
   if V9 HEAD SHA block is not aligned.
3. Commit using the GC-020 in-place update rule. Suggested message:

   ```text
   chore(legacy-audit): close N-1..N-4 corrections and prepare Phase A freeze

   Applied by Codex on Claude's hand-off:
   - Step 1: public-sync verification discipline rule documented in catalog
     and audit protocol
   - Step 2: ledger crosswalk declared canonical disposition source
   - Step 3: matrix Linked GAPs column added; round-trip checked
   - Step 4: catalog "proven" rows link only to verified file paths on both
     sides
   - Step 5: Phase A freeze packet recorded
   - Step 6: governance compat checks PASS
   ```

Acceptance criterion: clean commit on `main`, no skipped hooks, GC-020 HEAD
SHA check passes.

## Acceptance Criteria

This roadmap is complete only when Step 0 is resolved without an active
GC-023 file-size exception, Steps 1-5 are recorded in the active V9 handoff,
the Phase A freeze packet exists, and Step 6 records clean governance compat
results. A mock-only check cannot satisfy any governance-proof requirement.

## Verification / Evidence

Verification evidence for this roadmap is the per-step command output recorded
in commit messages and the V9 Active Boundary. The final Step 6 verification
set is:

```bash
python governance/compat/check_docs_governance_compat.py
python governance/compat/check_memory_governance_compat.py
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_agent_handoff_guard_compat.py
```

## Phase B Preview (Not For This Round)

After Steps 1-6 close, the next legitimate continuation is Phase B (public
catalog baseline). That phase needs a fresh GC-018. Do not start it inside
this round. Do not start any Phase D tranche inside this round.

The five named tranches inside Phase D (Role/Permission, ORCHESTRATOR,
Runtime workflow, Provider method, Memory continuity) each need their own
GC-018 and consuming-slice decision before any code change.

## Operator Posture Constraints — Unchanged

Codex must continue to respect:

- `system_reconvergence_stop` is in effect;
- bounded 17.05 phases delivered remain bounded;
- broad Phase 2.B runtime expansion remains blocked;
- Phase 4 provider methods remain demand-gated;
- public claims and release gates do not change;
- private legacy material does not migrate into public canon;
- F-1 output-quality parity tuning does not reopen;
- mock-only checks do not count as governance proof.

## Decision

After Steps 1-6 are done and verified:

- Phase A legacy knowledge map is frozen;
- legacy absorption audit (4-folder scope) is closed for the bounded
  five-axis methodology;
- Phase B public catalog baseline becomes the next legitimate continuation
  (separate GC-018);
- no tranche under Phase D is authorized until its own GC-018 is filed.

Until Steps 1-6 are done, Phase A remains unfrozen and no follow-up phase
may start.

Phase A freeze pointer: accepted at HEAD `ffae9346` by
`docs/reviews/CVF_LEGACY_ABSORPTION_PHASE_A_FREEZE_2026-05-18.md`.

## Claim Boundary

This packet:

- does not authorize any implementation;
- does not change public claims;
- does not promote private legacy material into public canon;
- does not lift `system_reconvergence_stop`;
- does not expand the audit beyond the operator-approved four scopes;
- does not reopen F-1 output-quality parity tuning;
- records what Claude already corrected (N-1..N-4) and what Codex must do
  next, with explicit acceptance criteria and verification steps for each
  remaining step.
