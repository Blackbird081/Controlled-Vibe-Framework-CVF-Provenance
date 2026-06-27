# CVF EA Review Finding Triage And Remediation Register - 2026-06-06

Memory class: SUMMARY_RECORD

Status: TRIAGE_RECORDED_PENDING_REMEDIATION

## Purpose

This register records the actionable parts of the external-agent review supplied
as root-local input:

`CVF_EA_REVIEW_2026-06-06.md`

The purpose is to preserve correct findings for later repair without treating
every external statement as equally current. The external review says it
reviewed public commit tree `859b1b3`; the current public-sync hardening branch
checked during this triage is `codex/p1-p5-public-doc-cleanup` at `ad3895913`.

## Scope / Target / Owner Boundary

Target:

- classify EA findings as accepted, needs verification, stale snapshot, or
  roadmap-only;
- identify the clean next remediation lanes;
- preserve public/provenance boundary before any follow-up implementation.

Owner boundary:

- this is a triage register, not a closure packet;
- no runtime/source behavior is changed by this register;
- no public readiness, hosted readiness, production readiness, provider-quality,
  cost/performance, or live-governance behavior claim is made;
- the root input file remains operator-supplied local review input unless a
  later batch explicitly promotes it into governed evidence.

## Target / Source

Target under review:

- External-agent finding set in root-local `CVF_EA_REVIEW_2026-06-06.md`.
- Current public-sync branch state sampled for drift-sensitive checks.

Source authority:

- Operator-supplied root review input is accepted as reviewer feedback, not as
  source-of-truth proof.
- Current repo files and public-sync command output are source authority for
  whether a finding is still locally reproducible.

## Scope / Methodology

Methodology:

- read the external review input;
- spot-check the highest-impact public-surface findings against public-sync;
- classify each finding into accepted, needs verification, stale snapshot, or
  roadmap-only disposition;
- avoid implementing fixes in this triage register.

Out of scope:

- full public corpus audit;
- full extension implementation-depth audit;
- live/provider proof;
- public push or runtime/source changes.

## Decision / Recommendation / Disposition

Decision: `ACCEPT_WITH_BOUNDED_REMEDIATION`.

Recommendation: open a small `EA-P0 Public Surface Hygiene` batch first, then a
separate `EA-P1 Public Evidence Discoverability` batch. Do not mix long-horizon
runtime/package refactors with the quick public-doc hygiene fixes.

Disposition:

- `EA-P0`: accepted and ready for a small source-verified remediation order.
- `EA-P1`: accepted as follow-up roadmap/work-order material.
- `EA-P2`: accepted as longer-horizon product/refactor debt.
- stale-snapshot claims: record but do not repair until rechecked against the
  target public branch/commit.

## Findings / Position

Position: several EA findings are valid remediation input. The strongest
accepted findings are public raw metadata exposure, missing public coverage
visibility, weak current-pointer discoverability, provider-dependency
visibility, CPF source-tree navigation debt, and public demo friction.

The truncation finding is not accepted as proven on current public-sync branch
because targeted tail checks did not reproduce an obvious incomplete ending.
It remains a reusable completeness-risk signal.

## Risk / Corrective Action

Primary risk:

- external evaluators may mistake internal governance metadata and dense
  date-stamped references for product instability or internal leakage;
- public evidence may be harder to trust when coverage/current pointers are not
  visible enough;
- long-horizon runtime/refactor debt may be mixed into small documentation
  hardening unless separated.

Corrective action:

- open `EA-P0 Public Surface Hygiene` for metadata and completeness guard work;
- open `EA-P1 Public Evidence Discoverability` for coverage/current-pointer and
  provider-dependency clarity;
- keep CPF tree grouping, barrel refactor, package naming, and public demo as
  separate product/refactor work.

## Source Snapshot

| Source | Evidence | Disposition |
| --- | --- | --- |
| External review input | `CVF_EA_REVIEW_2026-06-06.md` was read from root local workspace. | ACCEPT as operator-supplied review input |
| Reviewed public commit claimed by EA | EA file states `commit tree 859b1b3`. | STALE_SNAPSHOT risk |
| Current public-sync branch checked | `codex/p1-p5-public-doc-cleanup` at `ad3895913`. | ACCEPT as current branch-local check |
| Public-sync default remote baseline observed | `origin/main` at `d97f38c08`. | ACCEPT as context, not proof EA reviewed this exact state |

## Finding Triage Ledger

| ID | EA finding | Local check / evidence | Triage disposition | Remediation lane |
| --- | --- | --- | --- | --- |
| EA-P0-01 | Public docs expose internal `Memory class: ...` metadata. | `rg -n "Memory class:" README.md GET_STARTED.md ARCHITECTURE.md GOVERNANCE.md docs -g "*.md"` in public-sync returns many public docs, including `GOVERNANCE.md`, `docs/guides/external-agent-review-guide.md`, and multiple `docs/reference/*` files. | ACCEPT | Public-surface metadata hygiene guard and conversion plan |
| EA-P0-02 | `GOVERNANCE.md` and `ARCHITECTURE.md` may be truncated. | Tail check on current public-sync branch shows `ARCHITECTURE.md` ends with `## 8. Read Next`; `GOVERNANCE.md` ends with an external review boundary block and evidence bullets. No obvious current truncation was confirmed from the tail check. | NEEDS_VERIFICATION / possible stale snapshot | Add public-doc completeness scanner for canonical public docs |
| EA-P1-01 | Coverage report is not publicly visible; test pass count is not coverage proof. | No public coverage percentage was verified during this triage; EA critique is consistent with prior claim-boundary posture. | ACCEPT | Public evidence discoverability and CI coverage artifact plan |
| EA-P1-02 | Dated docs proliferation lacks a clear current-version pointer. | Public docs include many date-stamped reference artifacts; existing indexes exist but EA still failed to identify current canonical pointers. | ACCEPT_WITH_CLARIFICATION | Add/refresh canonical public reference index and README pointer |
| EA-P1-03 | Public readiness expectation mismatch remains because many surfaces are internal/private/non-export-ready. | This matches current bounded public claim boundaries and prior external review guidance. | ACCEPT as known limitation, not defect by itself | Improve public expectation-setting |
| EA-P1-04 | Provider concentration risk around DashScope/Alibaba live proof. | This is already bounded in live-proof standards but should be more visible to public evaluators. | ACCEPT_WITH_CLARIFICATION | Add provider-dependency boundary to external-agent guide/claim boundary |
| EA-P2-01 | CPF source tree is flat and hard to navigate. | Targeted public-sync count returns `169` files directly under the CPF source root. | ACCEPT | Separate CPF source tree refactor roadmap |
| EA-P2-02 | CPF consumer pipeline bridge barrel is unusually large and may contain more than re-export logic. | Targeted public-sync file existence check confirms the named barrel surface exists. Size/logic split was not inspected in this triage. | ACCEPT_FOR_REVIEW | Separate barrel ownership/refactor audit |
| EA-P2-03 | ALL_CAPS extension folder names may create npm publishing friction. | Public tree uses ALL_CAPS extension folder names by design. Package aliasing/publish strategy was not checked in this triage. | ACCEPT_AS_PRODUCT_PACKAGING_DEBT | Separate package-publication strategy task |
| EA-P2-04 | Time-to-first-working-demo remains harder than mainstream agent frameworks. | Public getting-started material exists, but EA still reports friction. | ACCEPT_AS_PRODUCT_EXPERIENCE_DEBT | Separate five-minute live demo/public onboarding lane |
| EA-NR-01 | Governance-first architecture is a major strength. | Positive assessment, not a defect. | RECORD_ONLY | N/A |
| EA-NR-02 | Runtime maturity lags conceptual/governance design. | Broad strategic assessment consistent with current bounded claim posture. | RECORD_AS_BOUNDARY_SIGNAL | Feed into roadmap prioritization, not a quick fix |

## Remediation Backlog

### EA-P0 Public Surface Hygiene

Scope:

- hide or remove raw `Memory class: ...` lines from public-facing docs, or
  convert only machine-needed cases to comments that do not read as public
  product copy;
- add a public-doc metadata leak guard to local/CI public hook chain;
- add a canonical-doc completeness check for root public docs such as
  `README.md`, `ARCHITECTURE.md`, `GOVERNANCE.md`, `docs/GET_STARTED.md`, and
  `SECURITY.md`.

Boundary:

- documentation and guard hardening only;
- no runtime/source behavior change;
- no public readiness expansion beyond cleaner public surface hygiene.

### EA-P1 Public Evidence Discoverability

Scope:

- publish or explicitly bound coverage visibility;
- add/refresh a public canonical-reference pointer index;
- make provider-key/quota dependency more visible to external reviewers;
- strengthen public expectation-setting around internal/private/export-candidate
  surfaces.

Boundary:

- evidence/discoverability only unless a later work order authorizes CI changes;
- no new coverage threshold claim without command-backed evidence.

### EA-P2 Product And Refactor Debt

Scope:

- CPF `src` domain grouping;
- large barrel audit/refactor;
- package publication naming/alias strategy;
- five-minute real-provider public demo path.

Boundary:

- separate roadmaps/work orders required;
- do not fold these into quick public-doc hygiene.

## Corpus Completeness And Report Integrity

- Corpus task class: targeted external-review finding triage.
- Corpus root: `CVF_EA_REVIEW_2026-06-06.md` plus targeted current public-sync
  checks.
- Snapshot time: 2026-06-06 local session.
- Enumeration command: `Get-ChildItem` targeted path checks plus direct file
  reads and targeted ripgrep searches; no complete public corpus enumeration
  claimed.
- Manifest artifact or inline manifest: inline manifest in this section.
- Manifest hash: N/A_WITH_REASON targeted triage does not claim complete
  corpus manifest stability.
- Processing ledger artifact or inline ledger: inline ledger below.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`,
  `BLOCKED_UNREADABLE`.

| Path | Processing status | Notes |
| --- | --- | --- |
| `CVF_EA_REVIEW_2026-06-06.md` | READ_FULL | Operator-supplied external-agent review input. |
| public-sync `GOVERNANCE.md` | READ_TAIL | Used only to test the truncation claim at current branch head. |
| public-sync `ARCHITECTURE.md` | READ_TAIL | Used only to test the truncation claim at current branch head. |
| public-sync public docs via `rg "Memory class:"` | SEARCHED_TARGETED | Used to verify metadata leak class. |
| public-sync CPF source tree | ENUMERATED_TARGETED | Used to verify flat source tree count. |

- Reconciliation: manifest=inline-targeted; ledger_terminal=READ plus targeted SEARCHED/ENUMERATED statuses mapped as READ; exclusions=full public corpus and full extension audit; unresolved=3.
- Unresolved files: 3.
- Declared exclusions: full public corpus, full extension implementation-depth
  audit, hosted deployment inspection.
- Unreadable or unsupported files: none.
- Aggregation check: EA findings are aggregated into remediation lanes; this
  packet does not claim fixes are complete.
- Drift check: EA reviewed a claimed `859b1b3` public tree; this triage checked
  current public-sync branch `ad3895913`, so drift-sensitive findings require
  recheck before implementation.
- Output traceability: accepted findings map to the Finding Triage Ledger.
- Adversarial verification: truncation was not accepted blindly; metadata leak
  and flat source-tree claims were command-supported.
- Corpus verdict: PARTIAL

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP`, `MACHINE_GATE_GAP`, `RUNTIME_SIGNAL_GAP`.

Learning lane: `GOVERNANCE_CONTROL_PLANE`,
`DOCUMENTATION_ONLY_LEARNING`, `RUNTIME_BEHAVIOR_LEARNING`.

| Finding class | Defect / signal | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Public metadata leak | Raw `Memory class` labels appear on public-facing docs and confuse external evaluators. | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Add public-surface metadata leak guard. |
| Public doc completeness uncertainty | EA reports possible truncated root docs; current tail check does not confirm but risk is reusable. | DOCUMENTATION_ONLY_LEARNING | MACHINE_CHECK_CANDIDATE | Add bounded root public-doc completeness scanner. |
| Evidence discoverability gap | Coverage/current-pointer/provider-dependency boundaries are not obvious enough to public reviewers. | DOCUMENTATION_ONLY_LEARNING | TEMPLATE_UPDATED | Update public external-agent guide, claim boundary, and reference index. |
| Runtime/product refactor debt | CPF flat tree, large barrel, packaging aliases, and demo friction are product maturity issues. | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | Open separate source-verified work orders before implementation. |
| Broad positive assessment | Governance-first design is strong but not a defect. | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | Record as context only; no control action required. |

## Claim Boundary

This register records what CVF accepts from the EA review as remediation input.
It does not claim:

- the EA review is fully correct;
- all public docs were re-audited;
- all accepted findings are fixed;
- runtime implementation maturity changed;
- coverage improved;
- package publication readiness changed;
- hosted/public/production readiness changed;
- live governance behavior was re-proven.
