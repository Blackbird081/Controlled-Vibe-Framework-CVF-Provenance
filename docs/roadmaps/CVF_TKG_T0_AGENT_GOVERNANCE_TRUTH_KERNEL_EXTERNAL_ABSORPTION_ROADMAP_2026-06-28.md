# CVF TKG-T0 Agent Governance And Truth Kernel External Absorption Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-28

Batch ID: TKG-T0

External knowledge intake routing: REQUIRED

## Purpose

Audit the upstream `microsoft/agent-governance-toolkit` repository and the
operator-provided `CVF_Truth_Kernel_Patch/` folder, then decide what CVF should
absorb, adapt, defer, or reject before any implementation tranche.

Decision:
`ACCEPT_TRUTH_KERNEL_AS_SOURCE_PROVENANCE_DOCTRINE_SEED_WITH_RUNTIME_DEFERRED`

Recommended next:
`AUTHOR_TKG_T1_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT`

## Target / Source

Reviewed sources:

- upstream repository clone:
  `.external_intake/agent-governance-toolkit` at commit `e5693cb`
- operator-provided external-agent folder:
  `CVF_Truth_Kernel_Patch/`
- local CVF evidence/truth owner surfaces:
  `docs/reference/CVF_ENTERPRISE_EVIDENCE_PACK.md`
- local CVF evidence-to-truth learning surface:
  `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md`
- local CVF release truth packet:
  `docs/reference/CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md`
- local CVF TruthScore doctrine:
  `docs/reviews/CVF_WD1_TRUTHSCORE_WEIGHTING_DOCTRINE_COMPLETION_2026-05-31.md`

Closure base head: `f928d6f0`.

## Scope / Methodology

1. Read CVF startup, active state, active handoff, guard orientation, and
   literal-format guidance.
2. Clone and inspect the upstream Microsoft Agent Governance Toolkit source at
   a fixed commit.
3. Read the operator-provided Truth Kernel patch folder beyond filenames,
   including docs, maps, specs, TypeScript package entrypoints, gates,
   provenance detector, receipt code, and tests.
4. Compare external concepts against current CVF evidence, truth, learning,
   release, and governance boundaries.
5. Select a documentation-only next tranche that adapts the useful doctrine
   without importing runtime package code or claiming live governance behavior.

No runtime source, generated aggregate, checker, provider/live proof,
public-sync, adapter, package activation, certification, vector store,
database, MCP server, CLI bridge, or Truth Kernel extension package import is
authorized by TKG-T0.

## Authorization / Decision

Operator authorization: continue the existing external-absorption rule for
`microsoft/agent-governance-toolkit` and the operator-provided
`CVF_Truth_Kernel_Patch/` folder.

Roadmap decision:
`ACCEPT_TRUTH_KERNEL_AS_SOURCE_PROVENANCE_DOCTRINE_SEED_WITH_RUNTIME_DEFERRED`

This authorizes only a documentation-owned external-intake roadmap and next
tranche selection. It does not authorize implementation.

## Non-Goals

- No direct import of AGT code, Truth Kernel package code, or patch checkers.
- No runtime/provider/live proof.
- No public-sync export.
- No MCP gateway, CLI bridge, adapter, hypervisor, kill switch, circuit
  breaker, runtime monitor, package activation, certification, generated
  aggregate, vector store, database, or hosted/production readiness claim.
- No replacement of existing CVF evidence, truth, receipt, learning, release,
  or approval surfaces.

## Design Control Gate

| Control | Required disposition |
|---|---|
| CVF authority | CVF-owned TKG-T1 contract must become the first reusable authority surface |
| Existing owner surfaces | TKG-T1/T2 must reconcile with Enterprise Evidence Pack, MLW3, release truth packet, and WD1 before any build |
| External-source handling | upstream AGT and `CVF_Truth_Kernel_Patch/` stay source inputs only |
| Runtime boundary | implementation-shaped items remain parked until fresh GC-018 and source verification |
| Claim boundary | integrity, hash, receipt, approval, and LLM judgment must not be overclaimed as truth |

## Work Plan

| Step | Output | Status |
|---|---|---|
| TKG-T0.1 | inventory AGT and Truth Kernel patch | COMPLETE |
| TKG-T0.2 | classify source/provenance/verification doctrine | COMPLETE |
| TKG-T0.3 | reject direct runtime/package import for this tranche | COMPLETE |
| TKG-T0.4 | select TKG-T1 CVF-owned contract as next move | COMPLETE |

## Acceptance Criteria

| Criterion | Evidence | Status |
|---|---|---|
| Upstream AGT reviewed at fixed commit | External Artifact Hash Manifest | PASS |
| Local patch reviewed beyond filenames | External Artifact Hash Manifest and Absorption Classification | PASS |
| Existing CVF owner surfaces considered | Source Verification Block | PASS |
| Runtime/package work not authorized | Non-Goals and Claim Boundary | PASS |
| Next tranche selected | Proposed Roadmap | PASS |

## Verification / Evidence

| Evidence item | Result |
|---|---|
| `git rev-parse --short HEAD` before material edit | `f928d6f0` |
| upstream AGT clone commit | `e5693cb` |
| external hash capture | recorded in External Artifact Hash Manifest |
| local patch structural non-promotion | `CVF_Truth_Kernel_Patch/` is not committed in TKG-T0 |
| expected changed set | this roadmap only |

## External Artifact Hash Manifest

| Artifact | Source class | Commit or local source | SHA256 |
|---|---|---|---|
| `README.md` | upstream AGT | `microsoft/agent-governance-toolkit@e5693cb` | `E99E836204772A0AD7A79768E83BD6DF998C0AB4194166491FBBC0AF9B7F3473` |
| `docs/specs/AGENT-OS-POLICY-ENGINE-1.0.md` | upstream AGT | `microsoft/agent-governance-toolkit@e5693cb` | `4CDC9F39019A3A470342EEE0CCFEAC8B1CAC0D3C6B0996441777A4494D420854` |
| `docs/specs/MCP-SECURITY-GATEWAY-1.0.md` | upstream AGT | `microsoft/agent-governance-toolkit@e5693cb` | `65D12E7CA9FCFD3B2F6B2839DA2497AD4737884FF6361C914CD549CD49560CFF` |
| `docs/specs/AGENT-HYPERVISOR-EXECUTION-CONTROL-1.0.md` | upstream AGT | `microsoft/agent-governance-toolkit@e5693cb` | `DC2E5B4BAAADC9D37F6001D467C236F19AAC6E9798C3A3F42FCD79967575FE2B` |
| `docs/INDEPENDENCE.md` | upstream AGT | `microsoft/agent-governance-toolkit@e5693cb` | `D321C3B42905371A6E7E19F70B4B6965A3CA97C7E2F4BCBBFAD82795F0702454` |
| `CVF_Truth_Kernel_Patch/docs/reference/truth/CVF_TRUTH_KERNEL_DOCTRINE.md` | operator-provided patch | local external folder | `C82BCDF012038E080FC184C180DD5653CC39275220F513BDB30813BF08E991E4` |
| `CVF_Truth_Kernel_Patch/docs/reference/truth/EVIDENCE_REGISTRY_SPEC.md` | operator-provided patch | local external folder | `7E7D96D7ED22D8CD51E6AE90444BBBAE05D42B30F065232C32C64D11DF8AD9D7` |
| `CVF_Truth_Kernel_Patch/docs/reference/truth/OBLIGATION_REGISTRY_SPEC.md` | operator-provided patch | local external folder | `746FEC8DE46AA91A81D87E33D292009CE736B176EDC30EA092816EBE9478CB0E` |
| `CVF_Truth_Kernel_Patch/docs/reference/truth/PROVENANCE_LABEL_SPEC.md` | operator-provided patch | local external folder | `BC86A39662518B65DFE0D951B5EE46BDD23238641B65182BA7920A7447233922` |
| `CVF_Truth_Kernel_Patch/EXTENSIONS/CVF_TRUTH_KERNEL/src/gates/strict-mode.ts` | operator-provided patch | local external folder | `449DA40EDB0324DEAD7D0440D9467373602C9DB5EB51650A244F893A389F08A5` |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Current CVF already has enterprise evidence-pack discipline | `docs/reference/CVF_ENTERPRISE_EVIDENCE_PACK.md` | Evidence Pack Principles; Minimum Evidence Set | CVF Enterprise Evidence Pack | CVF owner surface | EXISTS | ACCEPT |
| Current CVF already has evidence-to-truth learning signal routing | `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md` | Purpose; Workflow; Failure Modes | cvf.mlw3.evidenceToTruthLearningSignalPipeline.v1 | CVF owner surface | EXISTS | ACCEPT |
| Current CVF already has release truth packet boundary language | `docs/reference/CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md` | Purpose; Claim Boundary; What Is Proven | CVF Release Candidate Truth Packet | CVF owner surface | EXISTS | ACCEPT |
| Current CVF already has TruthScore weighting doctrine | `docs/reviews/CVF_WD1_TRUTHSCORE_WEIGHTING_DOCTRINE_COMPLETION_2026-05-31.md` | Purpose; Doctrine Summary | cvf.truthScoreWeightingDoctrine.wd1.v1 | CVF owner surface | EXISTS | ACCEPT |

## Findings / Position

| Finding | Evidence | Disposition |
|---|---|---|
| Upstream AGT is high-signal for governance doctrine | AGT README, policy engine spec, MCP gateway spec, hypervisor spec, SRE spec | ADAPT |
| Direct AGT runtime adoption would reopen runtime/provider/MCP/adapter lanes | AGT package structure and CVF parked-lane rules | DEFER_WITH_REOPEN_CONDITION |
| Local Truth Kernel patch captures the strongest CVF-fit doctrine | Truth Kernel doctrine, provenance, evidence, obligation, SOT, verifier specs | ABSORB_AS_DOCTRINE_SEED |
| Local Truth Kernel runtime package is not ready for direct promotion | strict-mode implementation only blocks fail results, while docs require missing evidence/obligation/unlabeled claim behavior | REJECT_DIRECT_IMPORT |
| CVF already owns several evidence/truth surfaces | Enterprise Evidence Pack, MLW3, release truth packet, WD1 | RECONCILE_BEFORE_BUILD |
| Best next move is a CVF-owned source/provenance/verification contract | external material plus local owner surfaces | TKG-T1_READY |

Decision: `CLOSED_PASS_BOUNDED`

## Absorption Classification

| External item | Source | CVF disposition | Reason / next condition |
|---|---|---|---|
| Deterministic interception before wire | AGT policy/MCP specs | ADAPT_AS_DOCTRINE | Map to CVF guard/runtime boundary language; no runtime gateway import |
| Deny/block/fail-closed semantics | AGT policy, MCP, hypervisor, SRE specs | ADAPT_AS_DOCTRINE | Useful for stricter claim language and future guard candidates |
| Structured decision/audit record | AGT policy and MCP specs | ADAPT_TO_EXISTING_RECEIPT_LANGUAGE | Reconcile with CVF receipts, evidence pack, and release packet boundaries |
| Core-vs-adapter independence | AGT independence policy | ABSORB_AS_ARCHITECTURE_RULE | Aligns with CVF public/provenance and adapter/package boundary discipline |
| Execution rings, kill switch, quarantine, circuit breaker | AGT hypervisor/SRE specs | DEFER_WITH_REOPEN_CONDITION | Reopen only with fresh runtime/operator requirement and GC-018 |
| MCP gateway, message signing, response scanner | AGT MCP spec | DEFER_WITH_REOPEN_CONDITION | Reopen only under MCP/adapter runtime lane with source verification |
| Truth Kernel root authority doctrine | Truth Kernel patch | ABSORB_AS_TKG_T1_SOURCE | Strong CVF fit; convert to CVF-owned contract |
| Integrity is not truth | Truth Kernel patch | ABSORB_AS_TKG_T1_SOURCE | Valuable claim-boundary doctrine for evidence and receipts |
| LLM output is not self-trusting | Truth Kernel patch | ABSORB_AS_TKG_T1_SOURCE | Valuable for independent verifier and freeze boundary |
| Evidence Registry fields | Truth Kernel patch | ADAPT_TO_EXISTING_EVIDENCE_SURFACES | Reconcile with Enterprise Evidence Pack and current evidence artifacts |
| Obligation Registry fields | Truth Kernel patch | ADAPT_AS_CONTRACT_ONLY | Valuable but no runtime obligation registry authorized yet |
| Provenance labels and provenance collapse | Truth Kernel patch | ABSORB_AS_TKG_T1_SOURCE | High value for source/provenance claim control |
| SOT Index | Truth Kernel patch | ADAPT_AS_REFERENCE_MAP_ONLY | Must not become a parallel source of truth |
| Independent Verifier | Truth Kernel patch | ABSORB_AS_DOCTRINE_SEED | Use deterministic verification methods; no runtime implementation yet |
| Human Responsibility | Truth Kernel patch | ABSORB_AS_DOCTRINE_SEED | Fits CVF accountable-approval boundary |
| Runtime Monitor | Truth Kernel patch | DEFER_WITH_REOPEN_CONDITION | Reopen only when a runtime evidence/obligation decay signal exists |
| `EXTENSIONS/CVF_TRUTH_KERNEL` package | Truth Kernel patch code | REJECT_DIRECT_IMPORT | New package needs source verification, code review, tests, build graph, and claim repair |
| Guard/checker scripts under patch | Truth Kernel patch code | DEFER_WITH_REOPEN_CONDITION | Reopen only after TKG-T1 defines exact CVF-owned fields and failure semantics |
| Non-coder Truth intake templates | Truth Kernel patch tools/docs | ADAPT_LATER | Useful after doctrine contract; not first tranche |

## Proposed Roadmap

| Tranche | Status | Objective | Boundary |
|---|---|---|---|
| TKG-T0 | CLOSED_PASS_BOUNDED | Audit AGT plus Truth Kernel patch and select next move | documentation-only |
| TKG-T1 | RECOMMENDED_NEXT | Author `Truth Foundation Source Provenance And Verification Contract` under CVF-owned reference paths | no runtime/checker/import |
| TKG-T2 | PARKED | Reconcile evidence/obligation/provenance fields against existing CVF evidence pack, MLW3, release truth packet, and WD1 | requires TKG-T1 closure |
| TKG-T3 | PARKED | Decide whether a static provenance-collapse or unlabeled-claim checker is worth implementing | requires TKG-T2 and fresh GC-018 |
| TKG-RUNTIME | PARKED | Runtime monitor, package import, MCP gateway, kill switch, or circuit breaker | fresh operator authorization, fresh GC-018, source verification, and live proof if governance behavior is claimed |

## Risk / Corrective Action

| Risk | Corrective action | Status |
|---|---|---|
| External repo replaces CVF authority | Treat AGT and Truth Kernel patch as inputs only; TKG-T1 must be CVF-owned | PASS |
| Truth Kernel creates a parallel evidence/truth subsystem | TKG-T1 must reconcile with current CVF evidence/truth surfaces before any build | PASS |
| Runtime code is imported before contract matches behavior | Reject direct import of `EXTENSIONS/CVF_TRUTH_KERNEL` in TKG-T0 | PASS |
| AGT runtime/MCP concepts reopen parked lanes | Record runtime/MCP/package/public/provider work as parked | PASS |
| Integrity/hash receipts are overclaimed as truth | Absorb "integrity is not truth" as a required claim boundary | PASS |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> Root/folder lifecycle classification plus absorption map when retained -> CVF-owned reference contract -> ABSORB, ADAPT, DEFER, REJECT, or BLOCK |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/roadmaps/CVF_TKG_T0_AGENT_GOVERNANCE_TRUTH_KERNEL_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` |
| Disposition | ADAPT upstream AGT and Truth Kernel patch into a CVF-owned source/provenance/verification doctrine roadmap |
| Claim boundary | external repo and patch are source inputs only; TKG-T0 creates no runtime, package, public, provider, adapter, MCP, or checker support |

## Rescan Intelligence Hardening

- Original source artifact: upstream `microsoft/agent-governance-toolkit` at
  `e5693cb` plus operator-provided `CVF_Truth_Kernel_Patch/`.
- Predecessor intake artifact: N/A with reason: first CVF-owned intake artifact
  for this combined AGT/Truth Kernel source set.
- Delta ledger status: first-pass classification against current CVF
  evidence/truth owner surfaces.
- Routing matrix status: items classified as absorb, adapt, defer, reject, or
  parked runtime.
- Semantic sampling status: sampled policy enforcement, MCP gateway,
  hypervisor audit, truth doctrine, provenance labels, strict-mode code, and
  existing CVF evidence/truth surfaces.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | AGT and Truth Kernel patch remain external inputs, not CVF authority |
| CHANGED_DISPOSITION | Truth Kernel runtime package is downgraded from possible direct import to candidate-only because code/spec behavior is not fully aligned |
| NEW_FINDING | TKG-T1 should reconcile Truth Kernel doctrine with existing CVF evidence/truth surfaces before any implementation |
| REMOVED_OR_REJECTED | direct AGT runtime import, MCP gateway implementation, hypervisor, package activation, and Truth Kernel runtime package import are rejected for TKG-T0 |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | close TKG-T0 and recommend TKG-T1 CVF-owned doctrine contract |
| SEPARATE_RUNTIME_TRANCHE | AGT hypervisor, MCP gateway, runtime monitor, kill switch, circuit breaker, and package import require fresh authorization |
| STRATEGIC_OPERATOR_DECISION | choose whether TKG-T1 should proceed before another external repository |
| OUT_OF_SCOPE | provider/live proof, public-sync, hosted readiness, production readiness, package activation, MCP/CLI bridge, generated aggregates |
| RESOLVED_BY_DESIGN | external-source authority boundary and direct-import rejection are recorded in this roadmap |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| TKG-T0-S1 | AGT policy engine spec | policy engine is a single enforcement point | ADAPT_AS_DOCTRINE | Could this justify importing AGT runtime into CVF now? | PASS: TKG-T0 adapts doctrine only and parks runtime |
| TKG-T0-S2 | Truth Kernel doctrine | integrity is not truth and LLM output is not self-trusting | ABSORB_AS_TKG_T1_SOURCE | Could the patch overclaim absolute truth? | PASS: roadmap preserves bounded truth-support claim |
| TKG-T0-S3 | Truth Kernel strict-mode code | strictAllows blocks fail results only | REJECT_DIRECT_IMPORT | Could direct import under-enforce the spec docs? | PASS: package import is rejected until contract/code alignment exists |
| TKG-T0-S4 | CVF existing owner surfaces | evidence pack, MLW3, release truth packet, WD1 already exist | RECONCILE_BEFORE_BUILD | Could TKG duplicate current CVF truth/evidence lanes? | PASS: TKG-T1 must reconcile instead of creating a parallel system |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | this roadmap | may use as next-lane selection and source-boundary record | Source Verification Block and Absorption Classification | N/A with reason: documentation-only roadmap | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter or public-safe readout | no external CLI, MCP, plugin, public API, or adapter behavior is created | Claim Boundary | separate GC-018/source-verified work order required | `DEFERRED_WITH_REASON` |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
|---|---|---|---|---|
| External governance runtimes are high-signal but implementation-shaped | SCOPE_EXPANSION_RISK | GOVERNANCE_CONTROL_PLANE | CLOSED_WITH_BOUNDARY | absorb doctrine first; defer runtime/import |
| Truth Kernel code/spec mismatch exists in strict-mode behavior | SOURCE_BEHAVIOR_MISMATCH | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | TKG-T1 must define contract before checker/runtime work |
| CVF already owns evidence/truth surfaces | DUPLICATE_OWNER_RISK | GOVERNANCE_CONTROL_PLANE | ROUTE_TO_RECONCILIATION | TKG-T2 may reconcile fields after TKG-T1 |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Completion or reviewer artifact | `docs/roadmaps/CVF_TKG_T0_AGENT_GOVERNANCE_TRUTH_KERNEL_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | this closed roadmap acts as the single-agent T0 closure artifact | PASS |
| Roadmap artifact | `docs/roadmaps/CVF_TKG_T0_AGENT_GOVERNANCE_TRUTH_KERNEL_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | this roadmap | PASS |
| Work order status | no worker-dispatch work order in TKG-T0 | single-agent external absorption roadmap | N/A with reason |
| Roadmap state | this roadmap | Status: CLOSED_PASS_BOUNDED | PASS |
| Registry JSON | no GC-051 registry JSON mutation authorized | changed set excludes GC-051 registry JSON | BLOCKED with reason: TKG-T0 is documentation-only |
| Registry Markdown | no GC-051 registry Markdown mutation authorized | changed set excludes GC-051 registry Markdown | BLOCKED with reason: TKG-T0 is documentation-only |
| External evidence digest | upstream commit `e5693cb`; local folder `CVF_Truth_Kernel_Patch/` | External Artifact Hash Manifest includes representative sha256 values | PASS |
| System loop interlock | N/A with reason: no loop/interlock surface changed | Claim Boundary | N/A with reason |
| Session continuity | active handoff marker planned after material commit | separate handoff-sync commit required | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| TKG-T0-Q1 | this roadmap | N/A with reason: Markdown artifact | decision selects doctrine seed with runtime deferred | `ACCEPT_TRUTH_KERNEL_AS_SOURCE_PROVENANCE_DOCTRINE_SEED_WITH_RUNTIME_DEFERRED` | PASS |
| TKG-T0-Q2 | External Artifact Hash Manifest | N/A with reason: Markdown table | upstream AGT and local patch representative hashes present | present | PASS |
| TKG-T0-Q3 | Absorption Classification | N/A with reason: Markdown table | each major external item has disposition | present | PASS |
| TKG-T0-Q4 | Proposed Roadmap | N/A with reason: Markdown table | TKG-T1 selected and runtime lane parked | present | PASS |
| TKG-T0-Q5 | Claim Boundary | N/A with reason: Markdown section | no runtime/provider/public/adapter/package implementation authorized | present | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance external-knowledge absorption roadmap. Public
summary or public-safe export requires a separate public-sync decision.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | `tkg-t0-agent-governance-truth-kernel-external-absorption-2026-06-28` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git clone/fetch, rg, Get-Content, apply_patch, governance gates |
| Target paths | `docs/roadmaps/CVF_TKG_T0_AGENT_GOVERNANCE_TRUTH_KERNEL_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` |
| Allowed scope source | operator requested continuing the old external-absorption rule for `microsoft/agent-governance-toolkit` and `CVF_Truth_Kernel_Patch` |
| Before status evidence | baseHead `f928d6f0`; worktree had operator-provided untracked `CVF_Truth_Kernel_Patch/` before patch |
| After status evidence | TKG-T0 roadmap created with no source/runtime mutation |
| Diff evidence | `git diff --name-status f928d6f0..HEAD` |
| Approval boundary | external absorption roadmap and next-tranche selection only |
| Claim boundary | no runtime, provider/live, public-sync, checker, generated aggregate, adapter, package activation, certification, vector store, database, MCP server, CLI bridge, hypervisor, kill switch, circuit breaker, or Truth Kernel package import |
| Agent type | single-agent reviewer/closer |
| Invocation ID | `tkg-t0-agent-governance-truth-kernel-absorption-2026-06-28` |
| Expected manifest | this roadmap only |
| Actual changed set | this roadmap only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this tranche |

## Claim Boundary

TKG-T0 is an external-knowledge absorption roadmap only. It does not claim CVF
has implemented AGT runtime governance, MCP gateway interception, hypervisor
execution rings, SRE circuit breakers, Truth Kernel runtime, obligation
registry runtime, evidence database, SOT index runtime, provider/live proof,
public-sync export, CLI/MCP adapter, package activation, certification,
generated aggregate, or production/hosted readiness.
