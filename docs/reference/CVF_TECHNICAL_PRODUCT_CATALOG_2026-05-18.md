# CVF Technical Product Catalog

Memory class: POINTER_RECORD
Status: PHASE-B PUBLIC-CATALOG SOURCE BASELINE

## Purpose

Provide a public-safe, technically accurate catalog of CVF. The baseline was
first issued on 2026-05-18 and is current through the 2026-05-22 B/C product
outcome runtime closure addendum. This file is a source draft for the public
GitHub repository. It must remain aligned with live evidence, public claim
boundaries, and the provenance/public repository split.

Phase B claim boundary:

- `docs/reference/CVF_PUBLIC_CATALOG_CLAIM_BOUNDARY_2026-05-18.md`

## Scope

Audience:

- users evaluating whether CVF is useful;
- developers checking the architecture;
- agents needing a factual front door before acting in the repository.

This catalog explains what CVF is, what is proven, what is bounded, and what is
still roadmap work. It intentionally avoids private legacy source links.

Catalog reconciliation model:

- Public-sync catalog is the customer-facing derivative.
- This provenance file is the annotated internal source copy used to preserve
  claim rationale, private review context, and public-sync publication
  boundary.
- The two files are allowed to differ in annotation density, but they must not
  disagree on product claims or claim boundaries.
- Permanent public-sync path verification rule: every path cited by the
  public-sync catalog must be `Test-Path`-verified on the public-sync
  filesystem before commit. Provenance-only verification is not sufficient for
  customer-facing catalog paths.

## Owner

Owner surface: public/product orientation and claim-boundary documentation.

Source inputs:

- public repository front door and evidence docs;
- 2026-05-18 four-scope legacy absorption matrix;
- 2026-05-19 Lane B workflow packaging baseline;
- 2026-05-22 B/C product outcome runtime and CLI distribution closure;
- active mandatory live governance proof rule;
- public/provenance repository split policy.

## Source / Predecessor Evidence

- `docs/baselines/CVF_GC018_PHASE_B_PUBLIC_CATALOG_BASELINE_2026-05-18.md`
- `docs/reviews/CVF_LEGACY_ABSORPTION_PHASE_A_FREEZE_2026-05-18.md`
- `docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`
- `docs/reference/CVF_PUBLIC_CATALOG_CLAIM_BOUNDARY_2026-05-18.md`
- `docs/baselines/CVF_GC018_LANE_B_WORKFLOW_PACKAGING_2026-05-19.md`
- `docs/baselines/CVF_GC018_BC_PRODUCT_OUTCOME_RUNTIME_AND_CLI_DISTRIBUTION_2026-05-22.md`
- `docs/reviews/CVF_BC_PRODUCT_OUTCOME_RUNTIME_AND_CLI_DISTRIBUTION_COMPLETION_2026-05-22.md`

## Decision / Baseline / Proposed Tranche

Decision: Phase B public catalog baseline accepted for the provenance source
copy of the public catalog.

Baseline: this catalog remains bounded to public-safe evidence and the
structured claim boundary. It does not claim complete Agent OS status,
universal provider parity, full legacy absorption, or release readiness beyond
published evidence.

Proposed tranche: none. Future Phase D implementation requires separate
GC-018 authorization.

## Requirements

This catalog must:

- link only to public-safe surfaces when used outside the provenance repo;
- separate proven, bounded, and roadmap capabilities;
- avoid private `.private_reference` source links;
- avoid claiming full Agent OS completeness;
- avoid claiming universal provider parity;
- preserve the mandatory live-governance-proof boundary.

## What CVF Is

CVF is a governance-first control framework for AI-assisted execution.

It puts a governed control plane between user intent, agent/runtime actions,
provider calls, policy checks, and evidence receipts. Its practical purpose is
to make AI work safer, more auditable, and more repeatable for both developers
and non-coders.

The core operating loop remains:

```text
INTAKE -> DESIGN -> BUILD -> REVIEW -> FREEZE
```

## Product Catalog

| Capability | Current status | What is verifiable |
|---|---|---|
| Governance control plane | proven and active | `ARCHITECTURE.md`; `governance/toolkit/05_OPERATION/CVF_AUDIT_PROTOCOL.md` |
| Governance CLI execution gateway | implemented as canonical CLI runtime gateway | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/bin/cvf.ts`; `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`; `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`; package binary exposes `cvf` and `cvf-guard`; calls existing `/api/execute`, not a replacement provider/runtime |
| Live governance proof | proven and mandatory for release claims | `scripts/run_cvf_release_gate_bundle.py`; `docs/CVF_INCREMENTAL_TEST_LOG.md` |
| Non-coder governed path | proven on bounded provider lanes | `docs/reference/archive/CVF_PUBLIC_NONCODER_VALUE_STATEMENT_2026-04-17.md`; `docs/assessments/CVF_W119_T1_NONCODER_ADOPTION_EVIDENCE_PACK_2026-04-23.md` |
| Provider lanes | certified only where evidence exists | `docs/audits/alibaba-canary/INDEX.md`; `docs/audits/deepseek-canary/INDEX.md` |
| Knowledge-backed execution | proven in bounded execute path | `docs/audits/CVF_W101_T1_CP1_KNOWLEDGE_NATIVE_EXECUTE_PATH_INTEGRATION_AUDIT_2026-04-17.md`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` |
| Deliverable packs | implemented in web product path | `README.md`; `docs/reviews/CVF_W130_EXPORT_ACTIVATION_CONTRACT_2026-04-28.md` |
| Workflow capability packs | runtime-bound for certified product outcomes | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts`; `governance/registries/cvf-certified-skill-pack-registry.json`; `cvf skill list --certified`; `cvf skill plan <pack-or-outcome>`; `cvf run <certified-pack>` resolves to existing execute templates with product outcome metadata |
| External asset/capability governance | partially productized | `docs/reference/CVF_PUBLIC_STRUCTURE_OVERVIEW.md`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts` |
| Role and agent governance | partially absorbed | role vocabulary and handoff governance exist; full enforceable role permission runtime is still roadmap work |
| Memory and continuity | partially runtime-wired | knowledge store, audit, session continuity, handoff rules, and execute-route audit memory receipt exist; governed reinjection across all worker paths is not complete |
| Provider method breadth | demand-gated | current slices use existing provider calls; streaming/tool-call/vision/embedding/reasoning methods need named consumer slices |
| Operational observability | partially absorbed | `docs/CVF_INCREMENTAL_TEST_LOG.md`; `docs/reviews/archive/CVF_W130_EVIDENCE_PACK_EXPORT_EVIDENCE_2026-04-28.md` |
| Tool/MCP/database action governance | roadmap | tool registry and guards exist; full canonical action taxonomy is still future work |
| Async workers/subagents | roadmap | sandbox and worker concepts exist; canonical async work-ticket and delegation lifecycle remain future work |
| Graph/code-intelligence context | roadmap | valuable legacy pattern; no full graph context resolver is claimed yet |

## B/C Closure Note For Agents

The original Review-CVF B/C pain point said CVF had skill governance concepts
but lacked practical skill packs, packaged workflows, an outcome-oriented
runtime, and a unified canonical CLI gateway.

As of the 2026-05-22 closure packet, that structural pain point is closed for
the current private implementation baseline:

- certified practical skill packs are registry-backed;
- packaged workflows have executable product outcome runtime plans;
- `cvf skill list --certified` and `cvf skill plan <pack-or-outcome>` expose
  the pack/runtime contract;
- `cvf run <certified-pack>` routes a certified pack into the existing governed
  execute path;
- package-level `cvf` and `cvf-guard` binaries exist with build and smoke
  proof.

Future usage may reveal bugs, ergonomics gaps, or release-packaging work. Those
items should be filed as usage-driven hardening or a new GC-018 tranche. Do not
reopen B/C merely because additional polish is possible. Reopen B/C only if a
new review proves the core pack/workflow/outcome-runtime contract above is
absent or materially nonfunctional.

## What Users Can Expect

Users can expect a governed AI path that records decisions and evidence instead
of treating AI output as an untracked chat transcript.

For non-coders, CVF is strongest where the request enters a trusted form or
bounded governed workflow. For developers, CVF is strongest where phase,
guard, policy, and evidence contracts are respected by the repository workflow.

## What Developers Can Verify

Developers should start from the public repository front door:

- `README.md`
- `ARCHITECTURE.md`
- `docs/GET_STARTED.md`
- `docs/CVF_INCREMENTAL_TEST_LOG.md`
- `docs/audits/alibaba-canary/INDEX.md`
- `docs/audits/deepseek-canary/INDEX.md`
- `docs/audits/CVF_W101_T1_CP1_KNOWLEDGE_NATIVE_EXECUTE_PATH_INTEGRATION_AUDIT_2026-04-17.md`
- `docs/assessments/CVF_W119_T1_NONCODER_ADOPTION_EVIDENCE_PACK_2026-04-23.md`
- `docs/reference/archive/CVF_PUBLIC_NONCODER_VALUE_STATEMENT_2026-04-17.md`

Release-quality governance proof uses:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Mock-only UI checks are not sufficient for claims that CVF controls AI or
provider behavior.

## Verification

This source draft is verified by local governance document checks in the
provenance repository. Public repository publication still requires the
public-sync boundary check and normal public release review before push.

Verification commands run after catalog reconciliation:

```bash
python governance/compat/check_docs_governance_compat.py
python governance/compat/check_memory_governance_compat.py
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_agent_handoff_guard_compat.py
```

Result: all four checks passed in the provenance repository.

2026-05-22 B/C catalog addendum path check:

```powershell
PASS EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/bin/cvf.ts
PASS EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts
PASS EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts
PASS EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/product-outcome.runtime.ts
PASS governance/registries/cvf-certified-skill-pack-registry.json
PASS docs/baselines/CVF_GC018_BC_PRODUCT_OUTCOME_RUNTIME_AND_CLI_DISTRIBUTION_2026-05-22.md
PASS docs/reviews/CVF_BC_PRODUCT_OUTCOME_RUNTIME_AND_CLI_DISTRIBUTION_COMPLETION_2026-05-22.md
```

This addendum updates the provenance source catalog only. Public-sync
publication remains a separate step and must re-run public-sync `Test-Path`
checks from the public-sync clone before any public repository commit.

Public-sync path check:

- The customer-facing public-sync derivative intentionally omits links to
  `START_HERE.md` and `docs/INDEX.md` because those paths were not present in
  the public-sync clone during reconciliation.
- Model B discipline is now binding for this catalog: every public-sync
  catalog path must be verified with `Test-Path` from the public-sync clone
  before commit. Current check result is recorded in the public-sync copy.
- Step 1 re-check (2026-05-18): extracted 15 `Test-Path` lines from the
  public-sync catalog and verified them in
  `Controlled-Vibe-Framework-CVF-public-sync`: 15/15 PASS.
- Step 4 provenance claim-link re-check (2026-05-18): every file-level path
  cited by the provenance source catalog was verified from the provenance
  workspace before commit:

```powershell
PASS README.md
PASS ARCHITECTURE.md
PASS docs/GET_STARTED.md
PASS docs/CVF_INCREMENTAL_TEST_LOG.md
PASS docs/audits/alibaba-canary/INDEX.md
PASS docs/audits/deepseek-canary/INDEX.md
PASS docs/audits/CVF_W101_T1_CP1_KNOWLEDGE_NATIVE_EXECUTE_PATH_INTEGRATION_AUDIT_2026-04-17.md
PASS docs/assessments/CVF_W119_T1_NONCODER_ADOPTION_EVIDENCE_PACK_2026-04-23.md
PASS docs/reference/archive/CVF_PUBLIC_NONCODER_VALUE_STATEMENT_2026-04-17.md
PASS governance/toolkit/05_OPERATION/CVF_AUDIT_PROTOCOL.md
PASS scripts/run_cvf_release_gate_bundle.py
PASS docs/reference/CVF_PUBLIC_STRUCTURE_OVERVIEW.md
PASS docs/reference/CVF_PUBLIC_CATALOG_CLAIM_BOUNDARY_2026-05-18.md
PASS docs/reviews/CVF_W130_EXPORT_ACTIVATION_CONTRACT_2026-04-28.md
PASS docs/reviews/archive/CVF_W130_EVIDENCE_PACK_EXPORT_EVIDENCE_2026-04-28.md
PASS EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts
PASS EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/external-asset-governance.ts
PASS docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md
PASS docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md
PASS docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md
```

Knowledge-backed execution check:
`docs/audits/CVF_W101_T1_CP1_KNOWLEDGE_NATIVE_EXECUTE_PATH_INTEGRATION_AUDIT_2026-04-17.md`
materially backs the bounded claim because it records route wiring for
`knowledgeContext`, governance-precedence prompt injection, response
`knowledgeInjection`, and unchanged enforcement/guard/provider routing. The row
remains `proven in bounded execute path`, not a universal runtime or UI claim.

## What Agents Must Respect

Agents using CVF should treat the repository as a governed workspace, not a
free-form coding sandbox.

Required posture:

- read the front-door instructions before changing files;
- preserve provenance/public repository boundaries;
- do not print or commit API keys;
- do not claim governance behavior without live proof;
- record gaps instead of silently absorbing broad legacy concepts;
- use roadmap and GC-018 gates for substantial continuation.

## Public Claim Boundary

The structured Phase B public claim boundary is:

- `docs/reference/CVF_PUBLIC_CATALOG_CLAIM_BOUNDARY_2026-05-18.md`

CVF may claim:

- governance-first AI control framework;
- bounded live non-coder value;
- evidence-backed provider lanes where receipts exist;
- governed knowledge-backed execution in the proven path;
- certified practical skill packs and an outcome-oriented CLI runtime gateway,
  bounded to the Governance CLI package and the current certified pack
  registry;
- public auditability through docs, evidence packets, guards, and release gates.

CVF must not claim yet:

- complete Agent OS status;
- full universal provider parity;
- full external capability marketplace readiness;
- public npm release, hosted CLI distribution readiness, or marketplace-level
  skill economy;
- full legacy repository absorption;
- unrestricted autonomous self-improvement;
- complete role-permission, memory-reinjection, async-worker, graph-context,
  database-action, or provider-method coverage.

## Related Artifacts

Private/provenance source draft:

- `docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md`
- `docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`

Public repository target:

- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- `docs/reference/CVF_PUBLIC_CATALOG_CLAIM_BOUNDARY_2026-05-18.md`

## Final Clause

This catalog is deliberately conservative. It is useful for customer
evaluation because it separates proven product behavior from roadmap ambition.
