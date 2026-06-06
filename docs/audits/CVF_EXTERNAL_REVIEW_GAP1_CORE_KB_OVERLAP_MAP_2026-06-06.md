# CVF External Review GAP1 Core KB Overlap Map

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-06

baseHead: ae6b64b6

Work order:
`docs/work_orders/CVF_WO_EXTERNAL_REVIEW_GAP1_CORE_KB_OVERLAP_MAP_2026-06-06.md`

## Purpose

This audit resolves the first safe move for External Review GAP1:
documentation bloat and repetition around `docs/CVF_CORE_KNOWLEDGE_BASE.md`.

The conclusion is bounded: the Core KB should not be rewritten until a separate
pointer-ification order is opened. This artifact only maps overlap, corrects
false owner paths, and identifies where future edits should point.

## Target / Source

Target source: `docs/CVF_CORE_KNOWLEDGE_BASE.md`.

Review source: External Review GAP1 in
`docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md`.

## Scope / Methodology

Scope is limited to mapping overlap between the target document and verified
owner surfaces. Methodology used heading reads, command-backed line counts, and
path verification for suspected owner documents.

## Source Corpus Manifest

| ID | Source path | Source role | Processing status | Evidence pointer |
| --- | --- | --- | --- | --- |
| C01 | `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` | External review gap source | READ | `## GAP 1 - Documentation Bloat and Repetition` |
| C02 | `docs/CVF_CORE_KNOWLEDGE_BASE.md` | Target document | READ | headings I-XIX; line count 944 |
| C03 | `CLAUDE.md` | Agent guidance overlap owner | READ | `## Architecture`; `## Governance Controls to Know` |
| C04 | `ARCHITECTURE.md` | Architecture front-door owner | READ | `## 1. System Shape`; `## 7. Current Control Boundaries` |
| C05 | `docs/guides/CVF_QUICK_ORIENTATION.md` | Newcomer orientation overlap owner | READ | `### 5-Phase Controlled Loop`; `### Risk Model R0-R3` |
| C06 | `docs/reference/CVF_MODULE_INVENTORY.md` | Module inventory owner | READ | `## Inventory` |
| C07 | `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md` | Architecture diagrams owner | READ | sections 1-8 |
| C08 | `docs/reference/CVF_ARCHITECTURE_MAP.md` | Historical architecture map | READ | `Status: DRAFT` and layer sections |
| C09 | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | Governance control owner | READ | `## Control Matrix` |
| C10 | `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | Provider readiness owner | READ | `## Provider Readiness` |
| C11 | `docs/reference/CVF_REFERENCE_GOVERNED_LOOP.md` | Governed loop owner | READ | `## What It Runs` |
| C12 | `docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md` | Known limitations owner | READ | `## Limitations Register` |
| C13 | `docs/reference/CVF_PUBLIC_STRUCTURE_OVERVIEW.md` | Public structure owner | READ | `## Top-Level Root Map` |
| C14 | `CHANGELOG.md` | Release history owner | READ | `## [v4.0.0] - GA Release - 2026-05-16` |
| C15 | `docs/INDEX.md` | Documentation index owner | READ | `## Storage Taxonomy` |
| C16 | `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md` | Markdown structure owner | READ | `## Common Required Elements` |
| C17 | `docs/reference/CVF_SESSION_GOVERNANCE_BOOTSTRAP.md` | Session governance owner | READ | `## Always-On Bootstrap` |
| C18 | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | Maintainability owner | READ | `### File Classes And Thresholds` |
| C19 | `governance/toolkit/05_OPERATION/CVF_ARCHITECTURE_CHECK_GUARD.md` | Extension-rule owner | READ | `### CVF Extension Rules` |
| C20 | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | Skill Library owner | READ | statistics section |
| C21 | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/README.md` | MCP Server owner | READ | `## Tools`; `## Guard Pipeline` |
| C22 | `MODULE_INVENTORY.md` | Rejected owner path from audit prose | SKIPPED_WITH_REASON | root path not found; corrected to C06 |
| C23 | `ARCHITECTURE_DIAGRAMS.md` | Rejected owner path from audit prose | SKIPPED_WITH_REASON | root path not found; corrected to C07 |

## Findings / Position

Position: proceed with pointer-ification only after this source-verified map;
do not rewrite the target document in the same tranche.

## Section-To-Owner Overlap Map

| Core KB section | Current content class | Recommended owner surface | Disposition | Reason |
| --- | --- | --- | --- | --- |
| I. Dinh danh & dinh vi CVF | Product identity and positioning | `README.md`, `docs/GET_STARTED.md`, `docs/guides/CVF_QUICK_ORIENTATION.md` | MAPPED_RETAIN_SUMMARY | Core KB may keep a short internal anchor, but public/newcomer identity belongs in front-door docs. |
| II. Kien truc 5 layers | Architecture model | `ARCHITECTURE.md`, `CLAUDE.md`, `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md`, `docs/reference/CVF_MODULE_INVENTORY.md` | MAPPED_POINTER_CANDIDATE | Strong overlap with current architecture owners; future edit should pointer-ify after owner decision. |
| III. Lich su cac version | Release history | `CHANGELOG.md` | MAPPED_POINTER_CANDIDATE | Changelog is the canonical release-history owner. |
| IV. 4-phase process | Governed workflow | `docs/reference/CVF_REFERENCE_GOVERNED_LOOP.md`, `CLAUDE.md` | MAPPED_POINTER_CANDIDATE | The governed loop has a dedicated reference owner. |
| V. Risk model CVF goc | Risk taxonomy | `CLAUDE.md`, `docs/guides/CVF_QUICK_ORIENTATION.md`, governance standards as needed | MAPPED_RETAIN_SUMMARY | Risk is cross-cutting; keep a compact KB summary until a dedicated current risk contract is selected. |
| VI. 5-layer safety kernel | Safety architecture | `ARCHITECTURE.md`, `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md`, `docs/reference/CVF_MODULE_INVENTORY.md` | MAPPED_POINTER_CANDIDATE | Architecture owners already cover control boundaries and diagrams. |
| VII. Governance system | Governance controls and gates | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`, `docs/reference/CVF_SESSION_GOVERNANCE_BOOTSTRAP.md` | MAPPED_POINTER_CANDIDATE | Dedicated governance owners exist and should carry detailed gate lists. |
| VIII. Skill Library | Extension/product module summary | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | MAPPED_POINTER_CANDIDATE | The module README is the correct detail owner. |
| IX. Cau truc file he thong | Repository/file structure | `docs/reference/CVF_PUBLIC_STRUCTURE_OVERVIEW.md`, `docs/reference/CVF_MODULE_INVENTORY.md`, `docs/INDEX.md` | MAPPED_POINTER_CANDIDATE | Structure information overlaps with public structure, inventory, and docs index. |
| X. Quality metrics | Evidence snapshot | Reviews, assessments, benchmark receipts, and limitations register | DEFERRED_OWNER_DECISION | Requires a separate evidence-owner decision to avoid moving stale quality claims. |
| XI. Nguyen tac bat bien | Invariants and mandatory rules | `AGENTS.md`, `CLAUDE.md`, `governance/toolkit/05_OPERATION/CVF_ARCHITECTURE_CHECK_GUARD.md` | DEFERRED_OWNER_DECISION | High-authority rules should not be collapsed without explicit authority-chain review. |
| XII. Checklist dinh vi extension moi | Extension placement checklist | `governance/toolkit/05_OPERATION/CVF_ARCHITECTURE_CHECK_GUARD.md`, `docs/reference/CVF_MODULE_INVENTORY.md` | MAPPED_POINTER_CANDIDATE | Checklist details belong with guard and inventory owners. |
| XIII. CVF MCP Server | MCP module description | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/README.md` | MAPPED_POINTER_CANDIDATE | MCP README is the module owner. |
| XIV. Key docs de doc them | Navigation/read-next list | `docs/INDEX.md`, `docs/GET_STARTED.md`, `README.md` | MAPPED_POINTER_CANDIDATE | Navigation should be owned by front-door and index files. |
| XIV. CVF Extension Rules | Extension architecture rules | `governance/toolkit/05_OPERATION/CVF_ARCHITECTURE_CHECK_GUARD.md`, `docs/reference/CVF_MODULE_INVENTORY.md` | MAPPED_POINTER_CANDIDATE | Rooted in architecture-check governance. |
| XV. Quality Assessment Canon | Quality review doctrine | Review standards and assessment packets | DEFERRED_OWNER_DECISION | Needs a separate source-verification packet for current assessment canon. |
| XVI. Pre-public P3 Execution Isolation | Public/provenance boundary | `AGENTS.md`, `docs/reference/CVF_PUBLIC_STRUCTURE_OVERVIEW.md`, public export standard | DEFERRED_OWNER_DECISION | Public boundary edits are high-risk and require their own work order. |
| XVII. Markdown Structural Completeness | Markdown artifact structure | `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md` | MAPPED_POINTER_CANDIDATE | Dedicated standard exists. |
| XVIII. Session Memory Front Door | Session startup and handoff routing | `docs/reference/CVF_SESSION_GOVERNANCE_BOOTSTRAP.md`, `CVF_SESSION_MEMORY.md`, active handoff registry | MAPPED_RETAIN_SUMMARY | Core KB can point to session bootstrap but should not replace active state. |
| XIX. Governed File Maintainability Planning | File-size guard and rotation | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | MAPPED_POINTER_CANDIDATE | Dedicated guard owns thresholds and workflow. |

## Findings

Finding 1: GAP1 is real, but the immediate problem is semantic repetition, not
an urgent line-count breach. `docs/CVF_CORE_KNOWLEDGE_BASE.md` is 944 lines in
this snapshot.

Finding 2: The audit's root-level owner examples `MODULE_INVENTORY.md` and
`ARCHITECTURE_DIAGRAMS.md` are not valid workspace paths. The verified owner
paths are `docs/reference/CVF_MODULE_INVENTORY.md` and
`docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md`.

Finding 3: `docs/guides/CVF_QUICK_ORIENTATION.md` contained stale "131 active
skills" wording while the current source of truth used by the prior GET_STARTED
freshness repair is 62 active skills. The same-batch side freshness repair
replaced both Quick Orientation occurrences with `62 active skills`.

Finding 4: Five Core KB sections need explicit owner decisions before rewrite:
quality metrics, invariants, quality assessment canon, public boundary, and
current risk-contract authority.

## Risk / Corrective Action

Primary risk: a direct rewrite could collapse high-authority rule text or point
to stale owner paths.

Corrective action: split low-risk pointer candidates from high-authority owner
decisions in the next work order.

## Recommended Next Work Order

Open a separate source-verified GAP1 pointer-ification work order only after
the operator accepts this map. That future order should:

- edit only selected Core KB sections;
- preserve a compact KB map rather than deleting context wholesale;
- move details to verified owners through links and short summaries;
- avoid changing high-authority rule text without explicit authority-chain
  review;
- treat the Quick Orientation skill-count freshness issue as closed by the
  same-batch side repair; broader count-drift hardening remains separate.

## Corpus Completeness And Report Integrity

- Corpus task class: AUDIT.
- Corpus root: `docs/CVF_CORE_KNOWLEDGE_BASE.md`; root front-door docs;
  selected `docs/reference` owner files; selected `governance/toolkit`
  guard files; selected extension README owners.
- Snapshot time: 2026-06-06T00:00:00+07:00.
- Enumeration command: `rg --files --hidden --no-ignore` plus
  `rg -n "^#|^##|^###" docs/CVF_CORE_KNOWLEDGE_BASE.md`;
  `Get-Content docs/CVF_CORE_KNOWLEDGE_BASE.md | Measure-Object -Line`; path existence checks for
  rejected root owner paths.
- Manifest artifact or inline manifest: see `## Source Corpus Manifest`.
- Manifest hash: N/A with reason: inline manifest only; no detached hash
  artifact generated for this bounded documentation map.
- Processing ledger artifact or inline ledger: every manifest row has terminal status `READ` or
  `SKIPPED_WITH_REASON`.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`,
  `DEFERRED`, `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=23; ledger_terminal=23; exclusions=4; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: full semantic review of every `docs/reference` file;
  runtime/source behavior; public-sync clone; live/provider proof; Core KB
  rewrite.
- Unreadable or unsupported files: none.
- Aggregation check: PASS - 20 Core KB level-two sections were mapped to owner
  recommendations.
- Drift check: PASS.
  Source reads were taken from commit `ae6b64b6` before this
  audit batch.
- Output traceability: `## 3. Section-To-Owner Overlap Map`.
- Adversarial verification: the two root owner paths named in audit prose were
  challenged, rejected, and corrected to verified `docs/reference` paths.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Knowledge System Reconciliation

- Knowledge task class: SEMANTIC_REGION_MAP.
- Source manifest: inline `## Source Corpus Manifest`.
- Source manifest hash: N/A with reason: inline manifest only; no detached hash
  artifact generated for this bounded documentation map.
- Enumeration safety: `rg --files --hidden --no-ignore` plus targeted heading
  reads and file existence checks.
- Intake registry or ledger: inline `## Section-To-Owner Overlap Map`.
- Source authority order: current workspace source files and canonical
  standards first; external audit prose second; memory/handoff summaries last.
- Authority assets: 20 Core KB level-two sections.
- Derived views: this overlap map only.
- Rebuildability check: PASS - rebuildable from heading inventory and
  owner-file heading reads recorded in the work order.
- Semantic region ledger: see `## 3. Section-To-Owner Overlap Map`.
- Region reconciliation: assets=20; mapped=15; deferred=5; unmapped=0.
- Deferred regions: current risk-contract authority, quality metrics, high
  authority invariants, quality assessment canon, and public boundary edits.
- Orphan or unmapped assets: none.
- Cross-region links: recorded through recommended owner surfaces in the
  overlap map.
- Drift check: PASS
  No runtime/source or public-sync claim is made.
- Retrieval boundary: this is not a retrieval index, chatbot answer surface,
  production knowledge graph, or runtime memory integration.
- Adversarial verification: stale/suspect paths were separated from accepted
  owner mappings; the stale Quick Orientation count was repaired in the same
  batch.
- Knowledge-map verdict: RECONCILED_WITH_DECLARED_GAPS

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| GAP1 needs overlap mapping before rewrite | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Use source-verified work order before pointer-ification. |
| Audit prose named false root owner paths | RULE_GAP | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | Source Verification Block corrected the paths before dispatch. |
| Quick Orientation had stale skill count | MACHINE_GATE_GAP | DOCUMENTATION_ONLY_LEARNING | MACHINE_CHECK_CANDIDATE | Same-batch side repair closed both Quick Orientation occurrences; broader count-drift guard remains a candidate. |
| High-authority Core KB sections need owner decision | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | Future pointer-ification order must split low-risk and high-authority edits. |

Runtime/provider/cost learning lane: N/A_WITH_REASON - this audit makes no
runtime, provider, cost, token, or latency finding.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_WO_EXTERNAL_REVIEW_GAP1_CORE_KB_OVERLAP_MAP_2026-06-06.md` | source verification block and bounded status | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EXTERNAL_REVIEW_GAP1_CORE_KB_OVERLAP_MAP_COMPLETION_2026-06-06.md` | completion review with closure diff gate and claim boundary | PASS |
| Roadmap state | `N/A with reason` | audit-derived, not roadmap-derived | N/A with reason: not roadmap-derived |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | updated with ER-GAP1 extension README owner-surface corpus entry | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | updated quick lookup, finding index, and next recommendation rows | PASS |
| External evidence digest | this audit artifact | 23-row bounded corpus manifest and 20-row overlap map | PASS |
| System loop interlock | `N/A with reason` | no system-loop interlock changed | N/A with reason: no interlock change |
| Session continuity | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, active handoff | final sync is included in allowed scope | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance audit. It does not include a public-sync
remote, commit, or artifact path.

## Claim Boundary

This artifact proves only a bounded source-verified overlap map for GAP1. It
does not prove a cleaned Core KB, public documentation readiness, source-code
quality, runtime governance behavior, live provider behavior, or complete
semantic correctness of every owner surface.
