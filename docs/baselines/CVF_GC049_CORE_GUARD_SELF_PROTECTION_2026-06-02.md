# GC-049 Baseline — Core Guard Self-Protection

Memory class: SUMMARY_RECORD

Status: ACTIVE

Date: 2026-06-02

## Purpose

Authorize a bounded guard-hardening patch after an agent modified unrelated
archive files and broke a core governance checker while attempting to fix KGR.

## Decision / Baseline

Decision: `APPROVED_GUARD_MAINTENANCE`.

Baseline: core guard files are frozen by default and may be changed only when a
same-batch authorization artifact explicitly names the protected paths and
rollback boundary.

## Proposed Tranche

GC-049-T1 adds a machine checker and hook/autorun integration. It does not
authorize archive cleanup, MKE route changes, public-sync, or production/live
release claims. Same-batch KGR-T5 bounded proof, GC-050 structural guard work,
the CVF corpus search/filter readiness standard, and the LPCI product roadmap
are explicitly listed in the scope firewall below.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add a new self-protection checker and wire
it into local hooks and autorun gates; extend Fix A/B/C forbidden-path
enforcement across scope firewall, pre-implementation gate, and dispatch-quality
checker.

Protected paths:

- `AGENTS.md`
- `governance/compat/check_core_guard_self_protection.py`
- `governance/compat/check_corpus_intelligence_classification.py`
- `governance/compat/check_forbidden_filesystem_state.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/toolkit/05_OPERATION/CVF_CORE_GUARD_SELF_PROTECTION_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_GUARD.md`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `docs/CVF_CORE_KNOWLEDGE_BASE.md`
- `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `governance/toolkit/02_POLICY/CVF_MASTER_POLICY.md`

Operator authorization: user requested immediate guard upgrade and a hard
technical freeze around core guards on 2026-06-02.

Rollback boundary: revert only GC-049 files and hook/autorun wiring if this
checker blocks legitimate guard-maintenance work unexpectedly. Do not revert KGR
or MKE changes under this rollback boundary.

## Scope Firewall Authorization

Allowed paths:

- `AGENTS.md`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge-graph-builder.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge-graph-store.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/knowledge-graph-builder.test.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/knowledge-graph-live.alibaba.test.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/knowledge-graph-store.test.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-retrieval-policy.kgr.test.ts`
- `docs/CVF_CORE_KNOWLEDGE_BASE.md`
- `docs/baselines/CVF_GC018_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_WAVE1_2026-06-01.md`
- `docs/baselines/CVF_GC049_CORE_GUARD_SELF_PROTECTION_2026-06-02.md`
- `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`
- `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
- `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
- `docs/reviews/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_LOCAL_REVIEW_2026-06-02.md`
- `docs/reviews/CVF_KGR1_T5_LIVE_PROVIDER_PROOF_COMPLETION_2026-06-02.md`
- `docs/roadmaps/CVF_LPCI_LEGAL_POLICY_CORPUS_INTELLIGENCE_CHATBOT_USE_CASE_ROADMAP_2026-06-01.md`
- `docs/roadmaps/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_ROADMAP_2026-06-01.md`
- `governance/compat/check_core_guard_self_protection.py`
- `governance/compat/check_corpus_intelligence_classification.py`
- `governance/compat/check_forbidden_filesystem_state.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `governance/toolkit/02_POLICY/CVF_MASTER_POLICY.md`
- `governance/toolkit/05_OPERATION/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_CORE_GUARD_SELF_PROTECTION_GUARD.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route-constants.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/mke1-memory-governance-live.spec.ts`
- `docs/baselines/CVF_GC018_MKE1_E3_MEMORY_LIVE_GOVERNANCE_PROOF_2026-06-01.md`
- `docs/reviews/CVF_MKE1_E3_MEMORY_LIVE_GOVERNANCE_PROOF_COMPLETION_2026-06-01.md`
- `docs/work_orders/CVF_WO_MKE1_E3_MEMORY_LIVE_GOVERNANCE_PROOF_2026-06-01.md`
- `scripts/run_cvf_release_gate_bundle.py`

Forbidden paths:

- `docs/reference/archive/`
- `docs/reviews/archive/`
- `docs/roadmaps/archive/`
- `docs/work_orders/archive/`
- `d:/UNG DUNG AI/TOOL AI 2026/Controlled-Vibe-Framework-CVF-public-sync/`

Large-Scope Change Authorization: operator authorized a single governed commit
covering KGR1 + MKE1-E3 proof seam + GC-049/050 as one batch after confirming
all artifacts were gate-clean. The high file count (>40) reflects the combined
delivery wave, not runaway scope. Archive files and MKE1-E2 route files are
explicitly excluded from this commit.

Changed-file ceiling: 50 files authorized for this delivery batch.
Rename/delete ceiling: 0 renames or deletes authorized.

Operator authorization: user requested immediate guard hardening after KGR
worker runaway and asked that core guards become technically hard to modify
outside explicit guard-maintenance scope.

Rollback boundary: if scope firewall blocks legitimate split commits, adjust
only the GC-049 scope-firewall implementation and authorization artifact. Do
not revert KGR local artifacts, MKE1-E3 artifacts, or unrelated operator work.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Local hook chain exists | `governance/compat/run_local_governance_hook_chain.py` | `HOOK_CHAINS` | `HOOK_CHAINS` | Local governance hook runner | ACCEPT |
| Autorun gate exists | `governance/compat/run_agent_autorun_workflow_gate.py` | `GateCommand` and `_common_commands` | `_common_commands` | Autorun workflow gate | ACCEPT |
| Guard registry requires KB registration | `governance/compat/check_guard_registry.py` | guard discovery and KB check | `docs/CVF_CORE_KNOWLEDGE_BASE.md` | Guard registry checker | ACCEPT |

## Claim Boundary

GC-049 protects core guard/control files and blocks runaway large-scope batches.
It does not prove runtime/provider behavior.

## Final Boundary

This is a guard-hardening baseline only. It is not a KGR, MKE, archive-cleanup,
or public-sync closure.

## Verification Boundary

Verification is local Python compile plus checker self-test against the current
working tree.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: GC-049 is private provenance governance hardening and has not been
exported to the public repository.
