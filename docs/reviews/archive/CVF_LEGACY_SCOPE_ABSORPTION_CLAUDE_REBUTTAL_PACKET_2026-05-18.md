# CVF Legacy Scope Absorption Claude Rebuttal Packet

Memory class: FULL_RECORD
Status: READY FOR CLAUDE REBUTTAL

## Purpose

Transfer the 2026-05-18 four-scope legacy absorption audit to Claude for
independent rebuttal.

Claude's task is not to agree with the matrix. Claude's task is to challenge
whether Codex classified the legacy knowledge correctly, whether any important
source concepts were missed, whether any public catalog claim is too strong,
and whether any deferred gap should be split, merged, escalated, or rejected.

## Scope

Claude must review only the operator-approved legacy scopes:

- `.private_reference/legacy/CVF 16.5`
- `.private_reference/legacy/CVF 17.05`
- `.private_reference/legacy/CVF ADD`
- `.private_reference/legacy/CVF Edit`

Claude must not expand the audit to other legacy folders unless the operator
explicitly authorizes it.

## Source

Primary packets to review:

- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`
- `docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`
- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- Public-sync draft:
  `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\docs\reference\CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`

Relevant source folders:

- `.private_reference/legacy/CVF 16.5/`
- `.private_reference/legacy/CVF 17.05/`
- `.private_reference/legacy/CVF ADD/`
- `.private_reference/legacy/CVF Edit/`

## Findings To Challenge

Claude should specifically challenge these Codex findings:

| Area | Codex classification | Required challenge |
|---|---|---|
| Cross-scope diagnosis | CVF has strong parts, but lacks composition into product capability systems | Is this too broad, too weak, or missing a deeper kernel/runtime diagnosis? |
| CVF 16.5 observability | `partially_absorbed` | Should observability be split into runtime telemetry, operator cockpit, provider health, and process/session monitor gaps? |
| CVF 16.5 memory/vault | `partially_absorbed` | Did Codex understate the gap between knowledge store and governed memory reinjection? |
| CVF 16.5 role/catalog | `partially_absorbed` | Are `allowed_outputs`, permission denials, and agent identity runtime important enough to be a top-priority tranche? |
| CVF 16.5 tool/MCP/action | `partially_absorbed` | Should MCP business actions, command surfaces, and DB actions be one gap or separate owner surfaces? |
| CVF 17.05 roadmap | bounded phases complete, Phase 4 demand-gated | Did Codex correctly preserve the phase boundary, or did it prematurely mark any item complete? |
| CVF 17.05 external capability intake | `partially_absorbed` | Is the current external asset governance enough for "partially productized", or should it be treated as mostly doc/runtime-incomplete? |
| CVF ADD doctrine | some items `absorbed` as doctrine | Did Codex overclassify any ADD source as absorbed when runtime activation is still bounded? |
| CVF ADD async/subagent | `partially_absorbed` | Should this be elevated above memory and role work, or remain behind them? |
| CVF ADD graph/context | `not_absorbed` | Should code-intelligence context be a near-term product differentiator or deferred lower? |
| CVF ADD database surface | `not_absorbed` | Is DB execution surface a real CVF product path or a tempting but premature side branch? |
| CVF Edit critique | runtime enforcement/state-machine hardening gap | Did Codex capture the severity correctly, or should this become the next primary roadmap? |
| Public catalog | conservative public-safe catalog | Are any claims too strong, too weak, missing evidence links, or unsuitable for customer-facing GitHub? |

## Risk

The main risk is false convergence: Codex may have grouped gaps too broadly,
classified doc-level absorption as stronger than it is, or made the public
catalog too customer-facing before evidence links are polished.

Corrective action required from Claude:

- identify any wrong classification;
- provide Evidence Trace Blocks for each correction;
- propose exact ledger/catalog wording changes;
- preserve the four-folder audit boundary unless the operator expands it.

## Requirements

Claude's rebuttal must include:

- Evidence Trace Blocks for every disputed claim.
- A verdict for each major area:
  `accept`, `accept_with_correction`, `reject`, or `needs_more_source_review`.
- A corrected gap list if Claude thinks GAP-010 through GAP-016 are incomplete
  or wrongly grouped.
- A corrected public catalog claim boundary if any catalog line is too strong
  or too weak.
- A recommended next roadmap priority order.

Claude must not:

- claim that private legacy source has become public canon;
- authorize runtime implementation;
- change public claims without evidence;
- reopen F-1 output-quality parity tuning;
- recommend copying external repos or raw external skill packs into CVF;
- treat mock-only checks as governance proof.

## Rebuttal Questions

Claude should answer these questions directly:

1. Are the four reviewed scopes complete enough for an initial absorption
   matrix, or did Codex skip important source folders/files inside those
   scopes?
2. Which Codex dispositions are wrong?
3. Which gaps should be split into smaller gaps?
4. Which gaps should be merged because they share one owner surface?
5. Which gap is the highest priority for the next GC-018 implementation tranche?
6. Is the public technical catalog ready as a customer-facing draft after
   evidence-link polishing, or should it remain internal-only?
7. Does the catalog accurately avoid claiming complete Agent OS status?
8. Does the matrix correctly keep `CVF 16.5`, `CVF 17.05`, `CVF ADD`, and
   `CVF Edit` separate from public canon?

## Expected Output Format

Claude should write a new review packet, preferably:

`docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_CLAUDE_REBUTTAL_2026-05-18.md`

Suggested structure:

```markdown
# CVF Legacy Scope Absorption Claude Rebuttal

Memory class: FULL_RECORD
Status: CLAUDE REBUTTAL

## Purpose
## Scope
## Source
## Bottom Line
## Evidence Trace Blocks
## Disputed Classifications
## Missed Concepts
## Gap Ledger Corrections
## Public Catalog Corrections
## Recommended Priority Order
## Decision
## Claim Boundary
```

## Evidence Trace Block Template

Claude should use this template for each major challenge:

```markdown
### ETB-N - <claim being challenged>

Source:

- `<source path>`
- `<source path>`

Observed evidence:

- <what the source actually says>

Codex classification:

- <absorbed / partially_absorbed / not_absorbed / roadmap / claim wording>

Claude rebuttal:

- <why the classification is right or wrong>

Required correction:

- <exact correction or "none">
```

## Claim Boundary

This packet is a request for rebuttal only. It does not authorize
implementation, does not change public claims, does not complete legacy
absorption, and does not expand the reviewed folder scope.
