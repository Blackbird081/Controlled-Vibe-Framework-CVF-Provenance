# CVF Legacy Scope Absorption Claude Rebuttal

Memory class: FULL_RECORD
Status: CLAUDE REBUTTAL (response to Codex's audit matrix and rebuttal packet)

## Purpose

Cross-check Codex's 2026-05-18 four-scope legacy absorption matrix
(`CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`),
gap ledger
(`CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`),
proposed roadmap
(`CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`),
and the two technical product catalog drafts (provenance + public-sync).

Operating under GC-046 (anti-collusion). Codex = PROPOSER on this packet,
Claude = REVIEWER. Both agents have failed cross-check in the past by
agreeing on doctrine without running the trace. This rebuttal runs the trace.

## Scope

Bounded to the four operator-approved legacy scopes:

- `.private_reference/legacy/CVF 16.5`
- `.private_reference/legacy/CVF 17.05`
- `.private_reference/legacy/CVF ADD`
- `.private_reference/legacy/CVF Edit`

Not expanded. Not authorizing implementation. Not changing public claims
beyond requesting corrections to the public-sync catalog draft.

## Source

Reviewed for this rebuttal:

- Codex matrix, gap ledger, roadmap, and technical catalog drafts (above)
- Provenance catalog: `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- Public-sync catalog:
  `Controlled-Vibe-Framework-CVF-public-sync/docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- Live file-system inventory of all four legacy scopes (counts + folder listings)
- Spot reads of representative source files (`Claude Kit` sister contracts,
  `CVF_EXTERNAL_CAPABILITY_INTAKE` content, CVF Edit critique cluster)

## Bottom Line

Codex's matrix is directionally correct: CVF *does* have strong governance
parts but lacks composition into enforceable product-capability systems. The
broad classifications (`absorbed` / `partially_absorbed` / `not_absorbed`) are
mostly reasonable and the operator-approved decision to defer broad absorption
is sound.

However, there are concrete defects that, if uncorrected, repeat the
"surface-scan-only" failure mode that GC-046 was designed to prevent:

1. **Inventory drift.** Codex's reviewed-source counts are wrong in two of
   four scopes (CVF 16.5 +1 file, CVF ADD +10 files). Not catastrophic, but
   it means the matrix was written from a stale enumeration, not a verified
   one. Re-count before freezing.
2. **`Claude Kit` is under-decomposed.** GAP-17.05-002 names only
   `CVF_AGENT_ROLE_CATALOG.md`. The folder actually contains **eight distinct
   governance contracts** (adapter boundary, audit receipt, handoff contract,
   orchestration rules, permission profile, registry spec, risk policy, role
   catalog) — each is a separate absorption surface. The current ledger
   collapses 7 of 8 into "absorbed" by silence.
3. **Provenance and public-sync catalog drafts diverge.** They are not
   different snapshots of the same document — they have different status
   strings, different audience framing, different evidence link sets, and
   different verifiable-column wording. Codex's matrix and ledger imply they
   are aligned drafts of one truth; they are not.
4. **GAP-17.05-002 is mis-prioritized.** Codex parks it as a deferred
   permission-model decision, but it is the **direct unblocker** for the
   Phase 2.B Open Question #2 already written into V9 handoff lines 391-409.
   Treating it as one of many deferred legacy items underweights its
   blocker status.
5. **Cross-scope diagnosis is too broad.** "Lacks composition into product
   capability systems" is true but compresses two distinct problems —
   (a) runtime enforcement of role/permission/state-machine semantics, and
   (b) governed memory reinjection across worker paths — into a single
   "composition gap". They need separate roadmap tracks; merging them invites
   the same flattening that produced GAP-17.05-002.
6. **The public catalog draft is not customer-ready.** It is conservative,
   which is good, but it links to public paths that are uneven
   (some paths are accurate, some are speculative — see ETB-6). Not safe to
   promote until evidence-link polish is done.

Decision per area is in the section "Disputed Classifications" below.

## Risk / Corrective Action

Risk:

- If the listed defects are treated as minor wording issues, the next audit
  pass can again collapse distinct legacy concepts into broad folder-level
  conclusions.

Corrective action:

- Re-run source counts before freeze.
- Decompose collapsed contract groups where the source folder contains
  separate governance contracts.
- Align provenance and public-sync catalog roles before promotion.
- Preserve GAP-17.05-002 as a blocker for broad non-bounded Phase 2.B runtime
  wire-up.

## Evidence Trace Blocks

### ETB-1 — Reviewed-source counts in the matrix

Source:

- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`
  ("Reviewed Source" table)
- Live filesystem under `.private_reference/legacy/`

Observed evidence (PowerShell `Get-ChildItem -Recurse -File | Measure-Object`):

- `CVF 16.5`: **100** files (matrix says 99)
- `CVF 17.05`: 31 files (matches)
- `CVF ADD`: **167** files (matrix says 157)
- `CVF Edit`: 10 files (matches)

Codex classification:

- "CVF 16.5: 99 files across 12 source folders"
- "CVF ADD: 157 files across 15 source folders"

Claude rebuttal:

- The folder counts are correct; the file counts are wrong by +1 and +10.
- This proves the matrix was not built from a fresh inventory pass before
  publication. GC-046 requires "Run the Trace" — counting is the trace.
- Magnitude is small but the principle matters: a matrix that misstates its
  own input cannot be frozen as a knowledge map (Phase A acceptance criterion
  in the roadmap is "freeze the four-source inventory").

Required correction:

- Re-run inventory; update matrix file/folder counts; commit with a note that
  Phase A freeze depends on counts being verifiable.

### ETB-2 — `Claude Kit` is 9 files, not 1

Source:

- `.private_reference/legacy/CVF 16.5/Claude Kit/` listing
- Matrix row for `Claude Kit`
- GAP-17.05-002 in the gap ledger

Observed evidence — Claude Kit contains:

- `CVF_AGENT_ADAPTER_BOUNDARY.md`
- `CVF_AGENT_AUDIT_RECEIPT.md`
- `CVF_AGENT_HANDOFF_CONTRACT.md`
- `CVF_AGENT_ORCHESTRATION_RULES.md`
- `CVF_AGENT_PERMISSION_PROFILE.md`
- `CVF_AGENT_REGISTRY_SPEC.md`
- `CVF_AGENT_RISK_POLICY.md`
- `CVF_AGENT_ROLE_CATALOG.md`
- `Thong_tin.md` (index)

Codex classification:

- Matrix row: "agent registry, role catalog, permission profile, handoff
  contract, allowed outputs" → `partially_absorbed`
- Gap ledger: GAP-17.05-002 names only the role catalog

Claude rebuttal:

- The matrix row collapses 8 distinct contracts into one cell with no
  per-contract disposition.
- The ledger picks one of those 8 contracts and silently grants the other 7
  "absorbed by association". That is exactly the flattening pattern the
  17.05 review chain flagged.
- Concretely:
  - `CVF_AGENT_RISK_POLICY.md` is not the same surface as Phase 1.P
    `RiskEngine` (it specifies per-role risk policy, not engine semantics).
  - `CVF_AGENT_ORCHESTRATION_RULES.md` overlaps with ORCHESTRATOR gap
    (GAP-17.05-001) but is recorded under that gap's `out_of_scope_deferred`
    grouping, not as its own surface.
  - `CVF_AGENT_AUDIT_RECEIPT.md` overlaps with Phase 1.R Receipt envelope —
    but Phase 1.R's `Receipt<TPayload>` does not bind to a per-agent or
    per-role audit-receipt model. Whether the legacy receipt model is
    `absorbed` by Phase 1.R or remains `partially_absorbed` is undocumented.

Required correction:

- Decompose `Claude Kit` row into 8 separate rows in the matrix.
- Open GAP-17.05-002a through 002h (or rename to per-contract gaps), each
  with its own disposition vs current CVF surfaces.
- Cross-link GAP-17.05-001 (ORCHESTRATOR) to the orchestration-rules
  contract.

### ETB-3 — Provenance and public-sync catalogs diverge

Source:

- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
  (provenance, this repo)
- `Controlled-Vibe-Framework-CVF-public-sync/docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
  (public-sync clone)

Observed evidence — `diff` shows differing wording on:

- Status line ("PUBLIC-CATALOG SOURCE DRAFT" vs "PUBLIC-CATALOG DRAFT")
- Catalog table column header ("What is verifiable" vs "What to verify")
- Multiple capability rows have different RHS values: provenance row says
  "phase/risk/scope/receipt guard contracts and governance compatibility
  gates"; public-sync row says
  "`ARCHITECTURE.md`, `GOVERNANCE.md`, `governance/toolkit/`".
- Public-sync version includes a `START_HERE.md` link the provenance draft
  does not.

Codex classification:

- Matrix and ledger imply two aligned drafts of the same catalog.
- Active Boundary in V9 handoff says "public-sync target created" and
  "public-sync remote verified".

Claude rebuttal:

- "Verified" applied to the *remote* (the URL) is true.
- "Verified" applied to *content alignment* is false. These are different
  documents that happen to share a filename.
- Either:
  - the public-sync version is the public-safe form and the provenance
    version is the internal-truth form, in which case the relationship must
    be documented and audited; or
  - one of them is the canonical and the other is stale.

Required correction:

- Pick one model:
  (A) provenance draft = source of truth; public-sync is auto-generated by
      a stripping/transform step that must be checked in or scripted, or
  (B) public-sync = customer-facing; provenance = internal annotated copy,
      with explicit pointer.
- Update the gap ledger entry GAP-17.05-016 to record the divergence and the
  chosen model.

### ETB-4 — GAP-17.05-002 priority vs handoff Open Questions

Source:

- `AGENT_HANDOFF_V9_2026-05-18.md` lines 391-409 ("Legacy Absorption Gap —
  CVF_AGENT_ROLE_CATALOG.md")
- `CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md` GAP-17.05-002
  disposition: `legacy_absorption_gap`, "Deferred"

Observed evidence:

- V9 handoff says this gap **must be resolved before Phase 2.B GC-018 is
  written**. ("Action required before Phase 2.B: decide whether the
  permission model belongs in Phase 2.B scope or requires a separate phase.
  This catalog is required reading for that decision.")
- The matrix and ledger both park it as deferred without acknowledging the
  Phase 2.B preflight dependency.
- The bounded Phase 2.B that was just delivered did **not** include this
  permission model — by Codex's own framing it was a fixture-driven wire-up.
- That means: Phase 2.B *broad* runtime expansion (which is what V9 means by
  "Phase 2.B" in the Open Questions section) is still blocked on this gap.

Codex classification:

- Treats GAP-17.05-002 as deferred legacy absorption, lower priority than
  the catalog work and the roadmap framing.

Claude rebuttal:

- This is not just "deferred legacy". It is the pre-condition the active
  handoff already named for the next non-bounded Phase 2.B.
- Demoting it to a generic deferred gap weakens the V9 Open Questions section
  and risks the next agent missing it.

Required correction:

- Re-classify GAP-17.05-002 disposition from
  `legacy_absorption_gap / Deferred` to
  `legacy_absorption_gap / blocking_broad_phase_2b`.
- Add explicit reference to V9 handoff Open Question #2.
- In the roadmap Phase C ranking, this gap belongs in the top tier (or in
  Phase D as the "preferred first tranche" candidate already named).

### ETB-5 — Cross-scope diagnosis flattens two problems into one

Source:

- Matrix "Cross-Scope Pattern" section
- Roadmap Phase C "Candidate gap families" list

Observed evidence — Codex states:

> "CVF has many strong governance parts. The remaining gap is composition
> into enforceable product capability systems."

And then lists nine gap families.

Claude rebuttal:

- The single diagnostic line cleanly covers items (a) "enforceable
  role/permission/orchestrator contract" and (h) "state machine and failure
  simulation suite" — those are *runtime enforcement* gaps.
- It does not cleanly cover items (b) "memory hierarchy plus governed
  reinjection" and (d) "MCP/tool/command action governance vocabulary" —
  those are *vocabulary and reinjection* gaps that exist independently of
  whether a state machine enforces them at runtime.
- One diagnosis line covering both creates the temptation to merge tranches
  in Phase D.

Codex classification:

- Bundles all nine candidate families under one cross-scope diagnosis.

Required correction:

- Split the cross-scope diagnosis into two:
  (i) Runtime enforcement gap (state machine, role permissions, orchestrator
      boundary, failure simulation, observability) — owners overlap;
  (ii) Knowledge/memory/action vocabulary gap (governed reinjection,
       canonical action taxonomy, graph context) — owners are different
       surfaces.
- Re-group the nine candidate families under (i) and (ii) before Phase C
  ranking.

### ETB-6 — Public-sync catalog link claims

Source:

- Public-sync catalog "What developers can verify" / verifiable-column links
- Public-sync repository file listing (already known: `START_HERE.md`,
  `docs/evidence/...` paths)

Observed evidence:

- Provenance catalog "What developers can verify" section lists nine paths
  (`README.md`, `ARCHITECTURE.md`, `docs/GET_STARTED.md`, `docs/INDEX.md`,
  `docs/evidence/README.md`, `docs/evidence/latest-release-gate.md`,
  `docs/evidence/provider-lanes.md`,
  `docs/evidence/web-governance-path.md`,
  `docs/reference/CVF_PUBLIC_NONCODER_VALUE_STATEMENT_2026-04-17.md`).
- The public-sync table rows reference `ARCHITECTURE.md`, `GOVERNANCE.md`,
  `governance/toolkit/`, `docs/evidence/...`, but `GOVERNANCE.md` is not in
  the public-sync front-door anchor list of the public sync repo and the
  shape of `governance/toolkit/` in public-sync is curated, not the full
  governance kernel.

Codex classification:

- Implies the public catalog is ready as a customer-facing draft after
  "evidence-link polishing".

Claude rebuttal:

- Some links may resolve in the public-sync repo, but link presence does not
  prove a public-safe evidence chain. Several rows point to broad directory
  references (`governance/toolkit/`, `EXTENSIONS/`) instead of concrete
  evidence files.
- A customer-facing catalog should link to specific files, not directories,
  for every "proven" row.
- The "Knowledge-backed execution" row claims proven status in the bounded
  execute path; its public-sync link goes to
  `docs/evidence/current-cvf-quality-status.md` which is a quality status
  doc, not a proof of governed knowledge-backed execution. That is a soft
  but real overclaim.

Required correction:

- Before promoting the public catalog to customer-facing:
  - Make every "proven" row link to a concrete public file path, not a
    directory.
  - Replace the "Knowledge-backed execution" verifiable link with the
    actual evidence packet (or downgrade row to `bounded` if the evidence
    packet does not exist publicly).
  - Reconcile provenance vs public-sync per ETB-3 first.

### ETB-7 — Phase boundary preservation

Source:

- V9 handoff "Active Boundary" section (lines 75-127)
- Matrix CVF 17.05 row "Final converged roadmap"
- Gap ledger GAP-17.05-006 / 008 / 009

Observed evidence:

- V9 explicitly says: bounded Phase 2.B, bounded Phase 2.C, bounded Phase
  3.E. Each was a narrow slice.
- Matrix says "bounded Phase 2.B/2.C/3.E done; Phase 4 remains demand-gated".
  This is correct.
- Ledger GAP-17.05-006 disposition: `phase_2c_bounded_slice_complete`.
- Ledger GAP-17.05-008: `phase_3e_bounded_pilot_complete`.

Claude rebuttal:

- Codex correctly preserves the boundary. No premature completion claim
  found.
- Verdict: accept.

Required correction: none.

### ETB-8 — External capability intake disposition

Source:

- `.private_reference/legacy/CVF 17.05/CVF_EXTERNAL_CAPABILITY_INTAKE/` —
  11 files including manifest schema, risk profile, certification protocol,
  authority binding, install state store, security scan protocol, workflow
  composition, ECC mapping guide, intake spec
- Matrix CVF 17.05 row: `partially_absorbed`
- Public catalog: external asset/capability governance = "partially
  productized"

Observed evidence:

- The intake spec covers 9 distinct sub-contracts. None of them have a
  named runtime owner in the current CVF tree beyond doc-level absorption.
- Phase 2.B/2.C did not absorb any of these contracts at runtime.

Codex classification:

- `partially_absorbed`

Claude rebuttal:

- `partially_absorbed` is technically defensible because docs and registry
  references exist. But "partially productized" in the public catalog is
  too strong for what is actually a doc-bound model with bounded
  metadata/UI surface.
- The rebuttal packet itself asks: "Is the current external asset governance
  enough for 'partially productized', or should it be treated as mostly
  doc/runtime-incomplete?" — Claude's answer: **mostly doc/runtime-incomplete**.

Required correction:

- Downgrade catalog row from "partially productized" to "doc-defined,
  runtime-incomplete" or equivalent honest phrasing.
- In the matrix, keep `partially_absorbed` but add a sub-note that 9 of the
  intake sub-contracts have no named runtime owner.

## Disputed Classifications

| Area | Codex | Claude verdict |
|---|---|---|
| Cross-scope diagnosis | "lacks composition into product capability systems" | **accept_with_correction** — split into runtime-enforcement vs knowledge/memory/action-vocabulary (ETB-5) |
| CVF 16.5 observability | `partially_absorbed` | **accept_with_correction** — split into runtime telemetry, operator cockpit, provider health, process/session monitor (per rebuttal packet's own suggestion) |
| CVF 16.5 memory/vault | `partially_absorbed` | **accept_with_correction** — the gap between knowledge store and governed reinjection is understated; raise as high priority |
| CVF 16.5 role/catalog | `partially_absorbed` | **reject** as currently scoped — decompose Claude Kit into 8 contracts (ETB-2); elevate GAP-17.05-002 to top tier (ETB-4) |
| CVF 16.5 tool/MCP/action | `partially_absorbed` | **accept_with_correction** — separate MCP business actions, command surfaces, DB actions into distinct sub-gaps |
| CVF 17.05 roadmap | bounded phases complete | **accept** (ETB-7) |
| CVF 17.05 external capability intake | `partially_absorbed` | **accept_with_correction** — downgrade catalog wording from "partially productized" to "doc-defined, runtime-incomplete" (ETB-8) |
| CVF ADD doctrine | some items `absorbed` as doctrine | **accept** — Codex correctly notes "do not inflate into a new runtime layer" |
| CVF ADD async/subagent | `partially_absorbed` | **accept_with_correction** — elevate above graph/database, behind memory and role |
| CVF ADD graph/context | `not_absorbed` | **accept** — defer; this is a future tranche, not a near-term differentiator |
| CVF ADD database surface | `not_absorbed` | **accept** — premature; should remain deferred |
| CVF Edit critique | runtime enforcement/state-machine hardening gap | **accept_with_correction** — this is the natural roof for runtime-enforcement tranche per ETB-5(i); rank as primary roadmap candidate |
| Public catalog | conservative public-safe catalog | **reject** as customer-ready — fix divergence (ETB-3) and link claims (ETB-6) first |

## Missed Concepts

Items from Codex's matrix that I do not see explicit ledger or matrix coverage
for:

1. **`CVF_AGENT_ADAPTER_BOUNDARY.md` (Claude Kit)** — adapter boundary
   contract; overlaps with Phase 1.P adapter maps but specifies per-agent
   adapter boundary semantics not captured there.
2. **`CVF_AGENT_RISK_POLICY.md` (Claude Kit)** — per-role risk policy;
   distinct from Phase 1.P RiskEngine which is policy-engine binding, not
   per-role policy declaration.
3. **`CVF_AGENT_AUDIT_RECEIPT.md` (Claude Kit)** — per-agent audit receipt
   model; partially absorbed by Phase 1.R `Receipt<TPayload>` but the
   per-role binding is not in Phase 1.R.
4. **`CVF_AGENT_REGISTRY_SPEC.md` (Claude Kit)** — agent registry spec;
   only mentioned in matrix as part of "Claude Kit" row.
5. **`CVF_AGENT_HANDOFF_CONTRACT.md` (Claude Kit)** — the actual handoff
   contract spec. AGENT_HANDOFF*.md files implement *a* handoff doc, but
   whether the V9 handoff is conformant with the legacy contract spec is
   not audited anywhere.
6. **CVF 16.5 `REVIEW FOLDER`** — `CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_2026-05-16.md`
   exists; not listed in the per-folder matrix table.
7. **`CVF_ECC_MAPPING_GUIDE.md` inside the 17.05 intake folder** — ECC
   mapping is an external-system mapping concept; not surfaced in the matrix.
8. **Sub-contracts under the 17.05 intake folder** (capability authority
   binding, install state store, security scan protocol, workflow
   composition) — each is a distinct surface, all currently absorbed under
   one `partially_absorbed` row.

None of these require immediate implementation. They require ledger entries
so the next agent does not re-discover them.

## Gap Ledger Corrections

Recommended ledger updates (suggested patches; not applied here — operator
decides):

1. **GAP-17.05-002** → split into GAP-17.05-002a (role catalog),
   002b (permission profile), 002c (orchestration rules), 002d (risk policy),
   002e (audit receipt — per-role binding), 002f (registry spec),
   002g (handoff contract spec conformance), 002h (adapter boundary).
2. **GAP-17.05-002** disposition → `blocking_broad_phase_2b` not generic
   `Deferred`.
3. **New GAP-17.05-017** — Provenance and public-sync catalog drafts
   diverge in content (ETB-3); pick a model and document the relationship.
4. **New GAP-17.05-018** — CVF 16.5 REVIEW FOLDER contains
   `CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_2026-05-16.md`; classification
   missing from matrix.
5. **GAP-17.05-001** (ORCHESTRATOR) → cross-link with the decomposed
   `CVF_AGENT_ORCHESTRATION_RULES.md` from Claude Kit (currently the
   ORCHESTRATOR gap cites only the 17.05 review folder audit).

## Public Catalog Corrections

For both catalog files:

1. Reconcile provenance and public-sync versions (ETB-3). Suggested: keep
   provenance as full-fidelity source, regenerate public-sync as a curated
   transform with explicit "this catalog was generated from <provenance
   commit>" pointer.
2. "Knowledge-backed execution" row in provenance: link should be a concrete
   evidence packet, not the quality-status doc (ETB-6).
3. "External asset/capability governance" row: downgrade phrasing from
   "partially productized" to "doc-defined, runtime-incomplete" (ETB-8).
4. Every "proven" row must link to a specific file path; reject directory
   references (ETB-6).
5. Add explicit "verification command" column or a single section listing
   the exact commands (release-gate bundle, governance-compat checks) that
   a reader can run to reproduce the proven claims.
6. Add `START_HERE.md` to provenance if it exists in public-sync, or remove
   from public-sync if it does not.

## Recommended Priority Order

If a fresh GC-018 is filed for the first legacy absorption tranche, my
recommended ranking is:

1. **Catalog reconciliation + ledger cleanup** (zero-runtime work)
   - Resolve ETB-1, ETB-2, ETB-3, ETB-8 first.
   - Output: revised matrix, revised ledger, single canonical catalog model.
   - This is a pure docs/contract tranche, no live proof needed.

2. **Role/permission/orchestrator runtime binding (GAP-17.05-002 family +
   GAP-17.05-001)**
   - Highest leverage: unblocks broad Phase 2.B, anchors the CVF Edit
     critique's "runtime enforcement" gap (ETB-5(i)), and produces a
     concrete deny-decision surface.
   - Requires deterministic tests, possibly live governance proof depending
     on the slice chosen.

3. **Memory reinjection policy (GAP-17.05-011)**
   - Codex flags this and CVF Edit reinforces it.
   - Separate roadmap track from role/permission (ETB-5(ii)).

4. **External capability intake certification runtime
   (GAP — currently inside GAP-17.05 implicit list)**
   - High product-marketing value but lower internal-blocker value than
     #2 and #3.

5. **Observability plane, async worker lifecycle, action vocabulary, graph
   context, database surface** — defer; ranked behind 1-4.

Phase 4 provider methods remain demand-gated; nothing in this audit changes
that.

## Decision

Codex's matrix and rebuttal-packet posture: **accept_with_correction**.

Concretely:

- **Accept** the operator-approved decision to bound the audit to four
  scopes and defer broad absorption.
- **Accept** the phase-boundary preservation (ETB-7).
- **Accept_with_correction** the cross-scope diagnosis, the CVF 16.5
  observability/memory/tool rows, the CVF 17.05 external-capability row,
  the CVF ADD async row, the CVF Edit critique row, and the public catalog
  draft.
- **Reject as currently scoped** the CVF 16.5 role/catalog row and
  GAP-17.05-002 priority. Both must be re-shaped before Phase A freeze.
- **Reject as customer-ready** the public catalog draft until ETB-3 and
  ETB-6 are addressed.

This rebuttal does not authorize any implementation. It is a request for
corrections to the matrix, ledger, roadmap, and catalog drafts before they
are frozen as Phase A input for the next legacy absorption tranche.

## Answers To Codex's Rebuttal Questions

1. **Are the four reviewed scopes complete enough?**
   Four-folder boundary is correct. Inside the folders, coverage is uneven:
   Claude Kit decomposition is missing (ETB-2), the 17.05 intake
   sub-contracts are flattened (ETB-8), and the CVF 16.5 REVIEW FOLDER is
   missing from the matrix table.

2. **Which Codex dispositions are wrong?**
   See "Disputed Classifications" table. Hard rejects: role/catalog scoping
   and GAP-17.05-002 priority. Soft corrections elsewhere.

3. **Which gaps should be split into smaller gaps?**
   GAP-17.05-002 (8 sub-gaps). CVF 16.5 observability row. CVF 16.5 tool/MCP
   row. 17.05 external capability intake row.

4. **Which gaps should be merged?**
   Cross-link GAP-17.05-001 with GAP-17.05-002c (orchestration rules), but
   keep them as separate ledger entries — they have different surfaces and
   different owners.

5. **Highest priority for next GC-018?**
   Catalog/ledger cleanup first (zero runtime). Then GAP-17.05-002 family
   (role/permission/orchestrator) as the first runtime tranche. See
   "Recommended Priority Order".

6. **Is the public catalog ready as customer-facing?**
   No. Fix ETB-3 (reconciliation) and ETB-6 (link quality) first.

7. **Does the catalog accurately avoid claiming complete Agent OS status?**
   Yes — both versions correctly avoid this. The Claim Boundary section is
   well-written.

8. **Does the matrix keep the four scopes separate from public canon?**
   Yes — no private legacy source is being promoted into public claims.
   Public catalog claims are about CVF current state, not legacy source
   content.

## Claim Boundary

This rebuttal:

- does not authorize implementation;
- does not change public claims;
- does not promote any `.private_reference/legacy/` content into public canon;
- does not lift `system_reconvergence_stop`;
- does not reopen F-1 output-quality parity tuning;
- does not expand the audit beyond the four operator-approved scopes;
- does not treat any mock-only check as governance proof.

It is a cross-check artifact under GC-046 producing concrete correction
requests for Codex's matrix, ledger, roadmap, and catalog drafts. Operator
decides which corrections to apply, and in what order, before the next
GC-018-backed tranche is filed.
