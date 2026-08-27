# CVF Public Skill Registry Atomic Reconciliation Roadmap

Memory class: governed-roadmap

Status: ROADMAP_CLOSED_BLOCKED_AGT_REGISTRY_DEBT

Date: 2026-08-27

## Purpose

Remove the final truthful blocker on public PR `#4` by making the user-skill
registry generator own exact, deterministic, non-destructive reconciliation
against the current 62-file source library. The roadmap admits one worker
return and no automatic successor.

## Authorization / Decision

The operator requested the next roadmap after PCIT-R1-BD1 bounded closure and
has standing authority for serious, high-value fixes with explicit time/quota
discipline. This roadmap selects the remaining required-CI blocker because it
directly gates merge value. It does not reopen PCIT or create PSRR-R2.

## Current Evidence

- Public exact SHA `86b1e728d8363e66c700ffdde9c2f6c02c93ed1e` passes Web,
  build, coverage, static/public checks and Python 3.9/3.10/3.11.
- Documentation & Testing run `33047367938` fails only Governance Registry
  Validation and its dependent fail-closed Status Check.
- The validator observes 335 user registry records and 62 source skill files.
- Read-only name reconciliation proves six desired filenames are already
  present, 329 current filenames are stale and 56 desired filenames are new.
- `generate_user_skills.py` is the existing canonical generator, but it only
  writes desired outputs and leaves stale files behind.
- `clean_user_registry.py` deletes every user record and the index unless run
  with dry-run, so clean-then-generate has an avoidable destructive gap.

## Scope / Target / Owner Boundary

PSRR-R1 may change only the public user-registry generator, one focused
generator test file, and the generated `user-skills` directory, plus its named
private worker return. The validator and cleaner are read-only unless the
worker proves a direct correctness blocker that cannot be solved in the
generator; that condition returns blocked rather than widening scope.

The generated directory is a large changed set by count but one owner family.
Deletion is authorized only for stale `USR-*.gov.md` files absent from the
desired manifest. No arbitrary file, agent registry, source skill, quarantine,
mapping record or external-source artifact may be deleted or rewritten.

## Design Control Gate

The generator must compute the complete desired manifest before mutation and
support:

1. a no-write dry-run that reports add/update/delete counts and exact paths;
2. a no-write check mode that exits nonzero on drift and zero on exact parity;
3. a caller-selected output directory for isolated tests;
4. deterministic content and ordering;
5. failure-before-mutation when a desired source cannot be read or rendered;
6. bounded stale deletion limited to `USR-*.gov.md` and generated `INDEX.md`;
7. an apply mode whose second run is byte-idempotent.

The worker must test failure atomicity and path boundaries in a temporary
directory before applying reconciliation to the public registry.

## Tranche Value Admission

| Factor | Decision |
| --- | --- |
| outcome consumer | public maintainers and users relying on required PR status |
| severity | P1 release blocker; all other exact-SHA required families are green |
| evidence | observed hosted run plus local 335/62 and 6/329/56 reconciliation |
| marginal value | one bounded generated-owner repair can unlock honest merge readiness |
| cost ceiling | one worker return, one generator/test owner, one generated family, zero providers |
| stop condition | stop on source-skill mutation, validator weakening, unrelated registry family, secret, deploy or second tranche |
| disposition | CONTINUE_HIGH_VALUE as PSRR-R1 only |

## Work Plan

PSRR-R1 first implements and tests safe manifest reconciliation in an isolated
output directory. Only after those tests pass may it apply the generator once
to the public user registry, rerun it to prove idempotence, run registry
validation and public-sync preflight, and return all changes uncommitted for
independent review.

## Acceptance Criteria

- Generator dry-run and check modes are mutation-free.
- A render/read failure leaves the target directory byte-equivalent.
- Apply deletes only manifest-stale user governance records and replaces the
  generated index; unrelated files survive.
- Final public registry contains exactly 62 records plus one index, all source
  links resolve, and validator exits zero.
- Second apply creates no diff and check mode exits zero.
- No CI threshold, workflow, validator rule, source skill or dependency changes.
- Worker leaves both repositories uncommitted with empty staging areas.
- Reviewer owns commit, push and exact-SHA hosted proof; PR merge is a later
  reviewer/operator action only after required checks are green.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | public generator and generated user registry | local Git-reversible generated-output reconciliation only | source, focused tests, validator | N/A with reason: no agent adapter behavior changes | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | public repository artifacts only | no CLI/MCP invocation, activation or runtime eligibility claim | generated Markdown records | external adapter remains outside this registry-maintenance lane | `DEFERRED_WITH_REASON` |

## Verification / Evidence

Evidence must include dual HEAD/status/staging, exact before/after manifests,
dry-run output, failure-atomicity tests, focused generator tests, registry
validator, idempotence diff, public-sync preflight and the full worker-return
fast gate.

## Non-Goals

No source-skill deletion, semantic skill review, risk-policy redesign, agent
registry change, package-skill lifecycle promotion, dependency upgrade,
provider/live call, secret read, workflow weakening, merge, deploy, Netlify
action, public-main mutation or automatic successor.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: these legacy user governance projections are
not ASSF package-skill lifecycle entries.

Target lifecycle state: unchanged.

Prior phase evidence: current source library and generated registry only.

Next forbidden skip: no promotion, activation, loading, projection into ASSF,
or runtime eligibility claim.

Runtime/provider proof: N/A with reason: deterministic local generation only.

Claim boundary: generated user-registry parity, not package productionization.

## Public Export Disposition

EXPORTED

Public-sync remote: `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Public commit: `d27d3db261404e8f594f130702ca7ef2c86a0ee7`

Public artifact path:
`docs/reviews/CVF_GC019_PSRR_R1_GENERATED_USER_REGISTRY_STRUCTURAL_CHANGE_REVIEW_2026-08-27.md`

Hosted run `33053902261` accepts the PSRR user-registry and GC-019 surfaces but
remains red only for the separately owned AGT registry family and dependent
Status Check.

## Next Allowed Move

PSRR-R1 is closed with its USR outcome accepted and exported. The next allowed
move is a separately governed, single-tranche AGT registry reconciliation
roadmap because exact-SHA hosted evidence proves that family is now the sole
remaining required-check blocker. Do not create PSRR-R2, merge or deploy.

## Claim Boundary

This roadmap authorizes one no-commit generated-owner reconciliation candidate.
It does not authorize merge, deployment, provider/live use, secret access,
source-skill mutation, validator weakening, arbitrary deletion or public-green
claims before exact-SHA hosted proof.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | real headings, dual-agent rows, package control fields, public disposition and dispatch status |
| gateRunPurpose | confirm one-tranche roadmap shape after source verification |
| claimBoundary | structural conformance does not prove safe deletion or hosted success |
