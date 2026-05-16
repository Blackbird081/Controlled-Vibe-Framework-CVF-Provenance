Memory class: SUMMARY_RECORD

# CVF Knowledge Vault Intake Source Adoption Matrix - 2026-05-16

Status: ACTIVE SOURCE MATRIX.

## Purpose

Map the `tolaria` source files to the CVF runtime behavior adopted in this
tranche.

## Scope

Owner surface:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`

Implemented files:

- `src/knowledge.vault.intake.contract.ts`
- `src/knowledge.vault.intake.types.ts`
- `tests/knowledge.vault.intake.contract.test.ts`

## Source

Source folder:

- `.private_reference/legacy/CVF 16.5/tolaria/`

## Decision

Adopt the governed markdown intake, graph, snapshot, receipt, drift, reinjection,
and tool-gate pattern. Defer live vault file I/O and live MCP execution.

## Adoption Matrix

| Source file | Adopted pattern | CVF owner behavior | Status |
|---|---|---|---|
| `CVF_KNOWLEDGE_VAULT_INTAKE.md` | raw vault file is input only | markdown intake, frontmatter normalization, registry candidate, receipt | adopted |
| `CVF_KNOWLEDGE_PROVENANCE_RECEIPT.md` | no receipt, no governed knowledge use | deterministic receipts for intake, graph, snapshot, tool, reinjection | adopted |
| `CVF_VAULT_SOURCE_OF_TRUTH_POLICY.md` | CVF registry plus receipt is authority | source input versus governed source-of-truth boundary | adopted |
| `CVF_MARKDOWN_KNOWLEDGE_GRAPH.md` | nodes, edges, wikilinks, eligibility | graph view with explicit and derived edges | adopted |
| `CVF_CONTEXT_SNAPSHOT_PACKAGER.md` | governed temporary context snapshots | snapshot packaging with filters, exclusions, token budget, receipt | adopted |
| `CVF_KNOWLEDGE_DRIFT_SIGNAL.md` | detect and recommend, no mutation | drift signal with `autoApplyAllowed: false` | adopted |
| `CVF_GOVERNED_REINJECTION_PROTOCOL.md` | learning may propose, governance approves | reinjection proposal and forbidden mutation block | adopted |
| `CVF_MCP_KNOWLEDGE_TOOL_GUARD.md` | read/write tool gate before execution | MCP-style knowledge tool decision and receipt | adopted |
| `Thong_tin.md` | source origin | source context only | classified |

## Evidence

Runtime evidence target:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.vault.intake.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.vault.intake.types.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/knowledge.vault.intake.contract.test.ts`

## Verification

The matrix is valid only when:

- raw files cannot become agent context without registry and receipt;
- context snapshot excludes blocked, review-required, superseded, conflicted,
  and over-budget assets;
- reinjection remains proposal-only;
- MCP-style write tools require receipt and block direct raw writes.

## Claim Boundary

This matrix records deterministic local Control Plane adoption. It does not
claim live vault file I/O or live MCP tool execution.
