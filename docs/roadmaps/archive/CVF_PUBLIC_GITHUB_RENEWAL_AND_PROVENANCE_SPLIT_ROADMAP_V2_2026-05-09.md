# CVF Public GitHub Renewal And Provenance Split Roadmap V2 — 2026-05-09

Memory class: FULL_RECORD
Status: FINAL ROADMAP — GATES A-B OPEN / GATES C-E BLOCKED
Owner intent: renew the public GitHub surface while preserving the historical CVF development record as private provenance.
Authorization: `docs/reviews/CVF_PUBLIC_GITHUB_RENEWAL_ROADMAP_CLAUDE_AUTHORIZATION_2026-05-09.md`
GC-018: `docs/reference/CVF_GC018_PUBLIC_GITHUB_RENEWAL_CANDIDATE_2026-05-09.md`

## 0. Authorization Boundary

Claude authorization status:

`AUTHORIZED — GO_WITH_PRE_R_BASELINE_BEFORE_RENAME`

Current gate state:

| Gate | State | Meaning |
|---|---|---|
| Gate A | OPEN | Authorization file 2026-05-09 permits Pre-R.0 and Pre-R local/reversible work. |
| Gate B | OPEN | V2 reviewed, rename strategy confirmed, old repo -> private confirmed, and `HYBRID_SIGNED_MANIFEST` accepted. |
| Gate C | BLOCKED | Requires Pre-R.0 resolution and complete R1 manifest/export verification. |
| Gate D | BLOCKED | Requires GitHub cutover prerequisites and verification passes. |
| Gate E | BLOCKED | Requires renewed repo live gate evidence and closure proof. |

This roadmap does not authorize:

- GitHub repo rename
- creation of the renewed public repo
- history export
- public cutover
- deletion or rewrite of provenance history

It authorizes:

- V2 finalization
- Pre-R.0 hook-failure investigation
- Pre-R reversible impact inventory, baseline measurement, and scanner planning

## 1. Purpose

CVF has reached a point where the current public repository contains too much historical operating material for its intended external audience. GitHub should present the current developer-facing product clearly: core architecture, modules, setup, governance contracts, provider boundaries, and evidence indexes.

The full historical repository remains valuable, but primarily as provenance: commit history, internal handoffs, rebuttals, wave records, raw evidence, and partner/audit proof. That material should not be the default public reading path for devs or noncoders.

This roadmap defines a governed renewal path:

- rename the current repository into a provenance/archive role
- create a clean public repository using the original product name
- curate only current, developer-relevant CVF materials into the renewed public repo
- preserve auditability without exposing operational noise as the public front door

## 2. Decision Anchor

Target current repo:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Recommended rename:

`Controlled-Vibe-Framework-CVF-Provenance`

Renewed public repo name:

`Controlled-Vibe-Framework-CVF`

Rationale:

- The old repository has full historical value but poor public surface clarity.
- Reusing the original name for the clean repo preserves the future product URL and brand, but intentionally breaks some old deep links after the name is reused.
- Renaming the current repo first frees the namespace.
- The provenance repo should be private or archived read-only unless an explicit partner/audit sharing decision is made.

V2 decision posture:

`CONDITIONAL_RENAME_AND_REUSE`

CVF may proceed with the rename-and-reuse strategy only after a Pre-R impact inventory and communication plan are complete. This roadmap rejects a blind rename. It accepts that old deep links may break only if the breakage is enumerated, documented, and offset by renewed public evidence in the new repo.

Alternatives considered:

| Option | Decision | Reason |
|---|---|---|
| Keep current repo public and create `cvf-public` | Rejected for now | preserves old URLs but leaves product brand URL on the noisy repo |
| Keep current repo public and use GitHub Pages as clean front door | Deferred | helps first impression but does not solve clonable-noise/public-surface issue |
| Rename current repo and reuse original name for clean repo | Preferred conditionally | best long-term product URL, but requires explicit URL-breakage and evidence-reverification plan |
| Defer renewal to v5.0+ | Fallback stop rule | use if Pre-R shows unacceptable link or evidence-verification breakage |

Known URL-impact classes:

- GitHub Release URLs such as `releases/tag/v4.0.0-rc.1`
- GitHub Actions run URLs such as CI2-H hosted run `25575296660`
- old issue/discussion links if any exist
- external citations in partner messages, posts, docs, or internal references
- raw blob links to old `docs/reviews`, `docs/audits`, `docs/baselines`, and `AGENT_HANDOFF*`

Required mitigation:

- inventory public GitHub releases, Actions links, issues/discussions, and known external citations before rename
- publish a short cutover notice before rename if the old repo remains briefly public
- create renewed-repo release evidence after cutover
- include `PROVENANCE.md` with private provenance access and hash anchors
- pause if impact inventory finds more than 10 externally important links that cannot be replaced by renewed repo summaries or partner-provenance access

## 3. Non-Goals

This roadmap does not authorize:

- rewriting or deleting historical Git history
- publishing raw secrets, local runtime state, or provider keys
- claiming unsupported provider parity
- moving every historical artifact into the renewed repo
- using GitHub public docs as the primary noncoder product experience
- turning CVF into a skill/template marketplace

## 4. Audience Model

### Public renewed repo audience

Developers, technical evaluators, integration partners, and security-minded reviewers who need:

- what CVF is
- how the architecture works
- how to run it
- which modules exist
- how agents/providers/tools connect through CVF
- what governance evidence exists
- what the current claim boundaries are

### Noncoder audience

Noncoders should primarily use:

- Web UI
- short product guides
- cost and provider setup help
- visible evidence receipts
- exportable outputs

They should not need to read historical GitHub roadmaps, rebuttals, or raw evidence chains.

### Provenance audience

Maintainers, auditors, and selected partners who need:

- full development timeline
- agent handoffs
- Claude/Codex review exchanges
- raw wave evidence
- historical roadmaps and closure packets
- proof of how CVF was created

## 5. Publication Model

Adopt:

`PRIVATE_PROVENANCE_REPO + CLEAN_PUBLIC_CORE_REPO`

Optional later:

`PARTNER_PROVENANCE_PACKET`

This keeps the current GitHub name useful for public users while preserving deep proof elsewhere.

## 6. Classification Scheme

Every file or folder considered for the renewed repo must be classified before export.

| Class | Meaning | Default action |
|---|---|---|
| `KEEP_PUBLIC_CORE` | Current code or docs required to understand/run CVF | copy into renewed repo |
| `KEEP_PUBLIC_EVIDENCE_SUMMARY` | Current evidence summary, release gate result, provider matrix | copy as curated summary |
| `PRIVATE_PROVENANCE` | Operational/provenance records including handoffs, rebuttals, raw logs, wave records, old or new | keep only in provenance repo unless explicitly promoted |
| `LOCAL_ONLY_RUNTIME` | local config, runtime state, generated logs, keys, caches | do not publish |
| `PUBLIC_EXAMPLE_OPTIONAL` | examples/templates useful for onboarding but not core | copy only after size/signal review |
| `DEFER_EXPORT` | unclear ownership or stale value | keep out until reviewed |

## 6.1 Future Publication Control

The renewal must prevent the same public-surface drift from recurring.

From the first push of the renewed public repo onward, these artifact types are private/provenance by default, whether old or newly created:

- agent handoff files
- Claude/Codex rebuttal files
- raw wave roadmaps and working continuation plans
- raw logs, browser traces, hosted run dumps, and generated test artifacts
- internal assessments and counter-reviews
- uncurated baseline, audit, and review packets
- operator-local runtime state
- provider-key setup transcripts
- any evidence artifact that includes raw prompt/output material not intentionally public-reviewed

Promotion into the public repo requires an explicit public-surface decision:

1. classify the artifact as `KEEP_PUBLIC_CORE`, `KEEP_PUBLIC_EVIDENCE_SUMMARY`, or `PUBLIC_EXAMPLE_OPTIONAL`
2. write or update the public-surface manifest
3. strip raw operational chatter and keep only durable technical signal
4. run secret/runtime scan
5. run link/path scan
6. verify claim boundaries
7. merge through protected review

No artifact may be public only because an agent generated it during normal work.

## 6.2 Renewed Repo Anti-Drift Controls

The renewed repo should include machine and process controls:

```text
governance/public-surface-manifest.json
scripts/check_public_surface.py
.github/pull_request_template.md
.github/workflows/public-surface.yml
CODEOWNERS
```

Minimum scanner behavior:

- block `AGENT_HANDOFF*.md`
- block `CLAUDE*.md` unless explicitly allowlisted
- block files matching `*REBUTTAL*`, `*TRANSFER_NOTE*`, `*RAW*`, `*HANDOFF*`
- block new files under `docs/reviews/`, `docs/roadmaps/`, `docs/audits/`, `docs/baselines/`, `docs/logs/`, and `docs/assessments/` unless explicitly allowlisted as curated public evidence
- block `.env*`, `.cvf/runtime`, `.cvf/config`, generated browser artifacts, and local job state
- warn on very large Markdown files
- warn on long wave-style names such as `W\d+`, `RC\d+`, and dated operational packets unless allowlisted

The scanner should support an allowlist so public evidence summaries can exist without reopening the floodgate.

## 6.3 Existing Guard Reuse And Renewal Profile

CVF already has effective guards for lifecycle, exposure, pre-public readiness, public-surface maintainability, handoff discipline, evidence retention, file size, and foundational guard surfaces. These guards are valuable, but they were built for the full internal/provenance monorepo.

They should not be copied wholesale into the renewed public repo.

### Keep in provenance repo

The full historical/provenance repo should keep the heavy guard chain because it still governs:

- agent handoff continuity
- historical evidence retention
- review/audit/baseline registry integrity
- active-window and archive behavior
- full extension lifecycle classification
- internal governance artifact writing
- deep structural-change discipline

Relevant existing controls:

- `GC-037` repository lifecycle classification
- `GC-038` repository exposure classification
- `GC-039` pre-public P3 readiness
- `GC-033` public surface maintainability for governed package barrels
- active-window, audit-retention, review-retention, file-size, and foundational guard checks
- `governance/compat/run_local_governance_hook_chain.py`

### Replace with a public repo guard profile

The renewed public repo should use a smaller `public-release` guard profile focused on:

- secret/runtime exclusion
- public-surface manifest enforcement
- blocked provenance artifact patterns
- curated evidence allowlist enforcement
- claim-boundary checks
- link/path sanity
- package install/test sanity
- release gate documentation truth

This keeps the public repo fast enough for normal contributors while still preventing internal/provenance material from leaking back into the public tree.

### Guard profile split

Recommended profiles:

| Profile | Repo | Purpose | Expected speed |
|---|---|---|---|
| `provenance-full` | `Controlled-Vibe-Framework-CVF-Provenance` | full internal governance and historical evidence integrity | slow but complete |
| `public-release` | renewed `Controlled-Vibe-Framework-CVF` | protect the clean public surface and current technical truth | fast |
| `release-live-proof` | renewed public repo or protected CI | run only when publishing governance behavior claims | intentionally live/cost-bearing |

The current long pre-push chain should remain useful in the provenance repo. The renewed public repo should not inherit all of it by default.

## 7. Renewed Repo Target Shape

Proposed clean public root:

```text
Controlled-Vibe-Framework-CVF/
  README.md
  LICENSE
  CONTRIBUTING.md
  SECURITY.md
  ARCHITECTURE.md
  GOVERNANCE.md
  PROVIDERS.md
  COST_AND_QUOTA.md
  PROVENANCE.md
  docs/
    architecture/
    evidence/
    guides/
    reference/
  packages-or-extensions/
    guard-contract/
    control-plane-foundation/
    execution-plane-foundation/
    governance-expansion-foundation/
    learning-plane-foundation/
    cvf-web/
  scripts/
  .github/
```

Exact package folder names may preserve current paths if changing paths would break imports. The first renewal pass may keep existing runtime paths and improve navigation before later structural package renames.

## 8. Public Front Door Content

### `README.md`

Target length: 150-250 lines.

Must cover:

- CVF one-line definition: governance control plane for AI/agent execution
- canonical flow: user/dev/noncoder -> CVF -> provider/agent/tool -> CVF validation -> governed output
- quick start
- module map
- live governance proof command
- current evidence status
- claim boundaries
- links to architecture and provider docs

Must not include:

- long wave history
- Claude/Codex transfer notes
- raw rebuttal chains
- detailed noncoder product marketing
- old release-candidate storylines

### `ARCHITECTURE.md`

Target: developer-first architecture.

Important correction after operator review: the existing visual module maps are a public-core asset, not provenance noise. The renewed repo should keep the diagram-first architecture style because it shows CVF's module relationships faster than prose alone.

Must cover:

- control plane
- execution plane
- guard contract
- provider adapter boundary
- web as a control surface, not all of CVF
- evidence receipt lifecycle
- cost/quota guard position
- local-first posture

Required visual treatment:

- keep a high-level module map showing meta governance, control plane, execution channels, and evidence/continuation governance
- keep a dependency-layer map showing Layer 0 through Layer 3 plus cross-cutting evidence
- keep the active reference path from user intent to provider call to receipt/freeze artifact
- keep the sequence diagram showing user, entry surface, guard contract, governance runtime, tool/model/agent, provider API, and audit/freeze/baseline
- tighten labels and notes so the diagrams explain boundaries without long paragraph text inside boxes
- add short diagram notes below each diagram for provider proof boundary, Web inheritance boundary, and what the diagram does not claim
- avoid copying stale v1.x marketing labels into the main public architecture unless the corresponding module is exported and current

### `CONTRIBUTORS.md`

Must be carried forward from the current repo as a public attribution artifact.

Purpose:

- recognize Tien / Blackbird081 as creator, product owner, governance authority, and release owner
- recognize Claude as an AI design/coding collaborator
- recognize Codex (OpenAI) as an AI engineering/repository/governance collaborator
- explain that GitHub commit metadata may not fully represent AI-assisted collaboration

Boundary:

- contributor acknowledgement does not transfer project ownership, licensing authority, or governance authority away from the human owner
- public contributor attribution should stay concise and role-based
- detailed Claude/Codex rebuttals, transfer notes, prompts, and operating history remain provenance-only unless separately curated

### `GOVERNANCE.md`

Must cover:

- phase gates
- risk classification
- approval flow
- DLP/redaction
- output validation
- audit/evidence receipts
- live-proof rule

### `PROVIDERS.md`

Must cover:

- provider-agnostic design
- current certified/bounded provider lanes
- adapter requirements
- unsupported-provider claim boundary
- key handling and redaction expectations

### `COST_AND_QUOTA.md`

Must cover:

- local-first cost guard
- provider-specific economics
- preflight quota behavior
- budget stop/warn strategy
- no raw key storage in public artifacts

### `PROVENANCE.md`

Must be short but verifiable.

Required posture:

```markdown
# CVF Provenance

CVF's full development history is preserved in a private provenance repository:

`Controlled-Vibe-Framework-CVF-Provenance`

The public repository intentionally contains the current product surface and curated evidence summaries, not the full internal operating log.

## Verification

Final provenance tag: `provenance-anchor-2026-05-XX`
Commit: `<git commit sha>`
Export manifest SHA256: `<sha256>`
Export date: `2026-05-XX`

The renewed public repository includes `docs/EXPORT_MANIFEST.md`, binding exported paths and evidence summaries to the final provenance anchor.

## Auditor Access

Partners and security auditors may request selected provenance access or a partner provenance packet.

- Request channel: `<operator-defined contact>`
- Target response time: `48 hours`
- Retention target: `minimum 7 years` unless superseded by legal or operator policy

## What Is Preserved

- full Git history before renewal
- `docs/reviews/*`, `docs/audits/*`, `docs/baselines/*`
- agent handoffs and Claude/Codex review exchanges
- release evidence and provider-lane evidence
- public-renewal decision and export manifests

## What Is Not Preserved In Public

- raw provider keys
- `.env`, `.env.local`
- `.cvf/runtime/` owner-specific local state
- temporary browser/test artifacts
- developer local caches
```

Optional stronger verification:

- OpenTimestamps proof for the export manifest hash
- DNS TXT record containing the export manifest SHA256 if an owner domain is available

## 9. Evidence Model For Renewed Repo

Public evidence should be index-first, not raw-log-first.

Target files:

```text
docs/evidence/README.md
docs/evidence/latest-release-gate.md
docs/evidence/provider-lanes.md
docs/evidence/web-governance-path.md
docs/evidence/redaction-and-key-safety.md
docs/evidence/claim-boundaries.md
docs/evidence/renewed-repo-release-gate-proof.md
docs/EXPORT_MANIFEST.md
```

Each evidence summary should include:

- date
- command or hosted run link where applicable
- provider lane
- pass/fail status
- scope boundary
- pointer to provenance archive availability, not raw internal chatter

The renewed repo must not rely only on the old CI2-H run from the provenance repo. After cutover, the protected live release gate must be configured and run on the renewed repo. The public GA evidence summary must cite the renewed repo run, while `PROVENANCE.md` may cite the original CI2-H hosted run `25575296660` as historical provenance.

Export provenance strategy:

`HYBRID_SIGNED_MANIFEST`

The first renewed public repo may use a clean initial history for clarity, but it must include `docs/EXPORT_MANIFEST.md` in the first commit. The manifest must bind:

- final provenance tag
- final provenance commit SHA
- exported path list
- export date
- SHA256 for the manifest itself or a generated export bundle
- evidence boundaries and known omitted provenance classes

This avoids pretending the renewed repo contains full commit ancestry while still giving external reviewers a verifiable anchor into the preserved provenance repository.

## 10. What Stays Out Of The Renewed Repo

Default private/provenance-only for both existing and future artifacts:

- `AGENT_HANDOFF*.md`
- `CLAUDE.md`
- Claude/Codex rebuttal and transfer notes
- detailed wave roadmaps `Wxxx` unless still current architecture reference
- raw `.json` evidence packets unless explicitly curated
- incremental logs
- internal assessments
- archived or uncurated audits and baselines
- local `.cvf/runtime`, `.cvf/config`, local provider settings
- generated browser/test artifacts

These artifact types may still be created during future development, but their default destination is the provenance repo or local/private workspace. The renewed public repo should receive only curated summaries and current technical contracts.

Default review-before-copy:

- `CVF_SKILL_LIBRARY/`
- legacy `v1.0/`, `v1.1/`
- old `EXTENSIONS/CVF_v1.x_*` folders
- case studies and tutorials
- public noncoder docs

## 11. Required Local Preparation

Before publishing the renewed repo:

1. Create a local clean export workspace outside the provenance repo.
2. Copy only classified files.
3. Run secret scan.
4. Run size/noise scan.
5. Run dependency install/test for exported runnable modules.
6. Run live governance proof only if making a release-quality governance claim.
7. Produce a public-surface manifest.
8. Produce a provenance split decision record.

## 12. GitHub Operations Plan

### G1. Freeze current repo state

- confirm current `main` is pushed
- tag final provenance snapshot, for example `provenance-pre-renewal-2026-05-09`
- write a short provenance closure note in the old repo before rename

### G2. Rename current repo

Rename:

`Blackbird081/Controlled-Vibe-Framework-CVF`

to:

`Blackbird081/Controlled-Vibe-Framework-CVF-Provenance`

Recommended settings:

- visibility: private
- archive: optional read-only after renewal is complete
- issues/discussions: disabled unless used for internal audit

### G3. Create new clean repo

Create:

`Blackbird081/Controlled-Vibe-Framework-CVF`

Recommended settings:

- public only after initial clean push passes verification
- branch protection after first stable push
- Actions enabled only for curated workflows

### G4. Push curated public repo

From the clean export workspace:

- initialize clean Git history
- commit curated public surface
- push to new `Controlled-Vibe-Framework-CVF`
- verify README, links, Actions, package install, and release gate docs

### G5. Update local remotes

For the current full local provenance clone:

```bash
git remote set-url origin https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git
```

For the new clean public workspace:

```bash
git remote add origin https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git
```

Do not point the historical working copy at the renewed clean repo.

## 13. Verification Gates

### V1. Public surface review

Pass criteria:

- README is dev-first and under target length
- no handoff/rebuttal/raw wave logs in root navigation
- architecture and module map are clear
- noncoder content is short and product-use oriented

### V2. Secret and runtime safety

Pass criteria:

- no raw provider keys
- no `.env`, `.env.local`, `.cvf/runtime`, `.cvf/config`
- no local job state
- redaction docs describe fake-key and real-key boundaries correctly

### V3. Build/test sanity

Pass criteria:

- exported modules install
- relevant unit tests pass
- web app boots if included
- release-quality proof command is documented

### V4. Evidence truth

Pass criteria:

- no unsupported provider parity claim
- evidence summaries link to current known proof
- DeepSeek and Alibaba boundaries remain explicit
- live proof claims cite live runs

### V5. Provenance preservation

Pass criteria:

- old repo renamed and preserved
- final provenance tag exists
- renewed repo has `PROVENANCE.md`
- no historical proof needed for audit is destroyed

### V6. Future anti-drift enforcement

Pass criteria:

- public-surface manifest exists
- public-surface scanner exists
- CI runs the scanner on pull requests
- PR template asks whether new files are public-core, public-evidence-summary, optional example, or provenance-only
- blocked private/provenance patterns cannot be added without an explicit allowlist entry
- allowlist entries require a short reason and owner approval

Public-surface scanner test plan:

Positive tests must block:

- `AGENT_HANDOFF_TEST.md` in repo root
- `*_REBUTTAL_*.md`
- `*_TRANSFER_NOTE_*.md`
- `docs/reviews/uncurated-raw-review.md`
- `docs/roadmaps/CVF_W999_INTERNAL_WORKING_PLAN_2026-05-09.md`
- `.env`, `.env.local`
- `.cvf/runtime/sample.jsonl`
- generated browser/test artifacts

Negative tests must allow:

- allowlisted files in `governance/public-surface-manifest.json`
- curated `docs/evidence/*.md` entries with manifest ownership
- source files under exported public modules
- public architecture docs explicitly classified as `KEEP_PUBLIC_CORE`

Override behavior:

- overrides require an allowlist entry with reason and owner
- override events should append to `docs/evidence/public-surface-allowlist-audit.jsonl` or equivalent curated audit file
- overrides should be reviewed periodically to prevent public-surface creep

Speed target:

- current `pre-commit` measurement on 2026-05-09: approximately `1.21s`
- current `pre-push` measurement on 2026-05-09: failed early at `memory governance compatibility` after approximately `3.99s`, so it is not a valid full-chain duration
- `public-release` target: under `10s` locally for the default public pre-push profile, excluding live provider proof
- `release-live-proof` is intentionally separate and may take minutes because it performs live provider work

Pre-R must re-measure the clean baseline before R0 authorization.

## 14. Risk Register

| Risk | Impact | Mitigation |
|---|---|---|
| Old links break after new repo reuses old name | Historical docs links may no longer resolve publicly | Accept intentionally; provenance repo is private and available on request |
| Accidentally publishing internal handoff material again | Public surface remains noisy | file classification manifest and public-surface scan before push |
| Removing too much technical context | Devs cannot evaluate CVF | keep architecture/module/evidence summaries strong |
| Secret leakage during export | Security incident | run secret scan before first push |
| Import paths break due folder renames | tests/build fail | first pass may preserve current runtime paths |
| Public repo overclaims CVF maturity | trust damage | evidence summaries must include scope boundaries |
| Provenance repo becomes inaccessible to maintainers | audit continuity loss | keep owner/admin access and tag final snapshot |
| Public repo slowly accumulates new handoffs/rebuttals/logs again | renewal benefit decays within weeks | enforce public-surface scanner, manifest, PR template, and allowlist review from day one |

## 15. Implementation Phases

### Phase Pre-R — Reversible Hygiene And Impact Baseline

Deliverables:

- `PRE_R.0` pre-push hook failure investigation and resolution
- PRE_R.0 hygiene report: `docs/reviews/CVF_PUBLIC_GITHUB_RENEWAL_PRE_R0_HYGIENE_REPORT_2026-05-09.md`
- URL and reference impact inventory for the current GitHub repo
- current release URL inventory, including `v4.0.0-rc.1`
- known external citation inventory if discoverable by operator
- hook-chain timing baseline
- warning-mode public-surface scanner prototype or simulated report
- README/navigation cleanup draft without repo rename
- decision: proceed to rename, switch to separate-public repo, use landing page, or defer to v5.0+

Exit:

- `PRE_R_RENEWAL_IMPACT_BASELINE_COMPLETE`

#### `PRE_R.0` — Resolve Pre-Push Hook Failure

Baseline measurement found that:

- `pre-commit` passed in approximately `1.21s`
- `pre-push` failed early at `memory governance compatibility` after approximately `3.99s`

This must be resolved before hygiene scan results are considered valid.

2026-05-09 update: PRE_R.0 is resolved in
`docs/reviews/CVF_PUBLIC_GITHUB_RENEWAL_PRE_R0_HYGIENE_REPORT_2026-05-09.md`.
The failure was a path-specific memory-class expectation mismatch for this V2
roadmap. The full provenance `pre-push` chain now passes in `309.14s`.

Required work:

1. Run the full pre-push chain and capture the exact `memory governance compatibility` failure output.
2. Determine whether the failure is caused by the new renewal planning files, existing dirty state, stale memory-governance registry data, or an actual governance violation.
3. Fix the failure without weakening the provenance/full guard profile.
4. Re-run `python governance/compat/run_local_governance_hook_chain.py --hook pre-push`.
5. Record the clean timing result in a Pre-R hygiene report.

Exit condition:

- full provenance `pre-push` chain passes, or Claude/operator explicitly reclassifies the failure as unrelated to renewal and authorizes continuing Pre-R with a named exception.

Stop rules:

- more than 10 important external links would break without replacement
- renewed public evidence cannot be recreated on the new repo
- operator decides a landing page solves enough of the problem for now
- provenance access model cannot be stated clearly

### Phase R0 — Review And Authorization

Deliverables:

- this roadmap reviewed by Claude/operator
- GC-018 public GitHub renewal candidate filed
- final decision on repo names
- final decision on old repo visibility
- final decision on initial public module scope
- final decision on commit-provenance strategy

Exit:

- `AUTHORIZED_TO_EXPORT_PUBLIC_RENEWAL`

### Phase R1 — Classification Manifest

Deliverables:

- machine-readable or table-based export manifest
- classify root files
- classify `docs/`
- classify `EXTENSIONS/`
- classify `governance/`
- classify scripts and workflows

Exit:

- every exported path has an explicit class

### Phase R2 — Clean Public Workspace

Deliverables:

- new local clean workspace
- copied curated files
- rewritten README/ARCHITECTURE/GOVERNANCE/PROVIDERS/COST docs
- curated evidence index

Exit:

- public tree can be read without internal operating context

### Phase R3 — Verification

Deliverables:

- secret scan result
- link scan result
- install/test result
- evidence truth review
- public surface review
- public anti-drift scan result
- export manifest draft
- PROVENANCE.md draft

Exit:

- `PUBLIC_EXPORT_READY`

### Phase R4 — Anti-Drift Guard Installation

Deliverables:

- `governance/public-surface-manifest.json`
- `scripts/check_public_surface.py`
- `.github/workflows/public-surface.yml`
- `.github/pull_request_template.md`
- `CODEOWNERS` or documented owner review rule
- initial allowlist for curated public evidence files
- `public-release` guard profile documented
- existing heavy provenance guard chain explicitly kept out of default public pre-push

Exit:

- future handoff/rebuttal/raw-log/wave-history artifacts are blocked from the public repo by default

### Phase R5 — GitHub Cutover

Deliverables:

- provenance repo renamed
- renewed repo created under original name
- clean public workspace pushed
- remotes updated
- branch protection and Actions reviewed
- GitHub environment `cvf-live-release-gate` created on renewed repo
- `DASHSCOPE_API_KEY` or accepted live-key alias configured in renewed repo environment secrets
- protected live release gate workflow dispatch verified as available

Exit:

- `PUBLIC_RENEWAL_ON_GITHUB`

### Phase R6 — Post-Cutover Hardening

Deliverables:

- first public issue templates
- contribution guide
- security policy
- public release tag
- optional partner provenance packet
- first anti-drift PR dry run
- renewed repo protected live release gate PASS evidence
- `AUDIT_TRAIL.md` short showcase
- partner provenance packet script or manual packet recipe

Exit:

- `CVF_PUBLIC_RENEWAL_CLOSED`

## 16. Initial Export Candidate Set

Likely keep:

- `README.md` rewritten
- `ARCHITECTURE.md` rewritten or tightened
- `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md` only if converted into a current, curated diagram appendix rather than exported as stale full-history v1.0-v1.7 material
- `LICENSE`
- `CONTRIBUTORS.md` carried forward and tightened only for public clarity, preserving owner / Claude / Codex attribution
- `ECOSYSTEM/doctrine/` as `KEEP_PUBLIC_CORE` unless Claude/operator explicitly rejects
- selected `.github/workflows`
- `EXTENSIONS/CVF_GUARD_CONTRACT/`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`
- `EXTENSIONS/CVF_GOVERNANCE_EXPANSION_FOUNDATION/`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` if Web remains part of public dev surface
- `scripts/run_cvf_release_gate_bundle.py`
- minimal governance compatibility scripts needed by release gate
- curated docs under `docs/architecture`, `docs/evidence`, `docs/guides`, `docs/reference`

Likely exclude:

- `AGENT_HANDOFF*.md`
- `docs/reviews/` except curated public evidence summaries
- `docs/roadmaps/` except current public renewal roadmap if desired
- `docs/baselines/`
- `docs/audits/`
- `docs/logs/`
- `docs/assessments/`
- `.claude/`
- `.private_reference/`
- local runtime/config/cache

Needs review:

- `CVF_SKILL_LIBRARY/`
- `governance/skill-library/`
- legacy `v1.0/`, `v1.1/`
- `CVF_ECOSYSTEM_ARCHITECTURE.md`
- `docs/CVF_ARCHITECTURE_DECISIONS.md`
- `docs/CVF_CORE_KNOWLEDGE_BASE.md`

## 17. Claude Review Questions

1. Should the old repo be private immediately after rename, or remain public read-only until the clean repo is published?
2. Should the renewed public repo preserve current folder paths for build safety, or introduce cleaner package names in the first pass?
3. Which evidence artifacts must remain public as summaries, and which should be provenance-only?
4. Should `cvf-web` ship in the first clean public repo, or wait until the core packages are clear?
5. Should the skill/template library be excluded from first public renewal to avoid product-positioning drift?
6. What is the minimum provider evidence set required in the renewed repo?
7. Should `AGENTS.md` be public in the renewed repo, or replaced with a shorter `DEVELOPMENT_RULES.md`?
8. Should `docs/CVF_ARCHITECTURE_DECISIONS.md` be split into active ADRs and provenance-only historical ADRs before export?
9. What is the public claim language for GA: `local-first approved`, `provider-hub ready`, or a narrower phrase?
10. What branch/tag naming should anchor the final provenance snapshot?
11. Should the renewed public repo block future `docs/reviews`, `docs/roadmaps`, `docs/audits`, `docs/baselines`, `docs/logs`, and `docs/assessments` files by default, allowing only curated summaries?
12. Who owns public-surface allowlist approval after renewal?
13. Which existing guards must remain provenance-only, and which should be ported into the public `public-release` guard profile?
14. Should `run_local_governance_hook_chain.py` gain named profiles before export, or should the renewed repo start with a smaller new script?
15. Does Claude accept `CONDITIONAL_RENAME_AND_REUSE` after Pre-R impact inventory, or require the safer separate-public/landing-page option?
16. Does Claude accept `HYBRID_SIGNED_MANIFEST`, or require `git filter-repo` path-preserving history?
17. Does Claude accept `ECOSYSTEM/doctrine/` as `KEEP_PUBLIC_CORE` in the first export?
18. Does Claude require OpenTimestamps/DNS anchoring for the first public renewal, or is manifest SHA256 plus provenance tag enough for R6?

## 18. Final Authorization Posture

Proceed with this posture:

`GO_WITH_PRE_R_BASELINE_BEFORE_RENAME`

Gates A and B are open for Pre-R.0 and Pre-R local/reversible work only.

Do not push the renewed repo until:

- classification manifest is complete
- GC-018 candidate is filed and authorized
- public docs are rewritten
- anti-drift guard is installed
- secret/runtime scan passes
- evidence claims are underclaimed
- provenance repo has a final tag
- renewed repo live gate environment and evidence plan are ready

Do not rename the GitHub repository until:

- Pre-R impact inventory is complete
- Pre-R hook baseline is clean
- R1 classification/export manifest is complete
- Gate C is opened by explicit operator authorization
- GitHub cutover prerequisites are satisfied

## 19. Final Boundary

The renewed public GitHub repository should show CVF as a serious developer-facing governance control plane.

It should not expose the full internal operating journal as the product surface.

Git history and the provenance repository preserve how CVF was made. The renewed public repo should show what CVF is now, how to run it, how to integrate with it, and what evidence supports its current claims.
