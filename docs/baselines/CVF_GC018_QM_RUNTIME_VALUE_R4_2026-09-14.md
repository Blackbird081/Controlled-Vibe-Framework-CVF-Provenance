# CVF GC-018 Baseline - QM Runtime Value R4

Memory class: governed-dispatch-baseline

docType: baseline

Status: APPROVED_FOR_EXECUTION

Date: 2026-09-14

Batch ID: QM-RUNTIME-VALUE-R4

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: fd231762b9cae0bc425e5fa61ac5fd9799ff5bff

## Purpose

Authorize one independent per-source lane inside the active
`DOMAIN-PILOT-THREE-REPO-2026-09` program. The lane recovers and terminally
accounts for runtime/use-case value in QM's `src/memory` tree at the indexed immutable pin.

## Decision / Baseline

Local decision: `APPROVED_FOR_EXECUTION`. Dispatch the paired work order after
the pre-dispatch gates pass. The worker may write only the two named evidence
outputs and must not commit. This is an `INITIAL` independent lane, not a
successor or reopening of the stopped aggregate residual-recovery chain.

The active three-repository program remains `LOCAL_RUNTIME_VALUE_RECOVERY`,
with `expansionAllowed=false`. Completion of this lane does not complete QM as
a whole, complete the pilot, or authorize `ARCH-ABS-009`, `SKILL-SRC-005`, or
another repository package.

## Parent Program Contract Binding

| Field | Bound value |
| --- | --- |
| programId | `DOMAIN-PILOT-THREE-REPO-2026-09` |
| parent state | `CVF_SESSION/state/entries/activeExternalAbsorptionProgram.json` |
| sourceId | `yc-software__qm` |
| source state at dispatch | `INCOMPLETE` |
| nextActionClass | `CONTINUE_ACTIVE_PROGRAM` |
| expansionAllowed | `false` |
| exitDisposition | `RETAIN_ACTIVE_PROGRAM` |
| chainBoundary | `INDEPENDENT_PER_SOURCE_LANES_ONLY` |
| controlling review | `docs/reviews/CVF_EXTERNAL_LOCAL_ABSORPTION_PROGRAM_CONTINUITY_HARDENING_2026-09-13.md` |

## Scope / Target / Owner Boundary

The worker may read the pinned ignored mirror
`.private_reference/source_mirrors/yc-software__qm/`, the paired dispatch
packet, cited CVF authority/evidence, and directly relevant QM tests found by
deterministic path or symbol searches. The worker owns only:

- `docs/audits/CVF_QM_RUNTIME_VALUE_R4_2026-09-14.json`
- `docs/reviews/CVF_QM_RUNTIME_VALUE_R4_WORKER_RETURN_2026-09-14.md`

Local owns the baseline, work order, review, commits, continuity, candidate
selection, CVF owner comparison, and final absorption decision. External-agent
research is advisory and has no execution role in this lane.

Forbidden effects: changing or fetching the mirror; executing upstream code,
tests, scripts, skills, packages, builds, or dependencies; importing source;
editing CVF runtime/product/checker/registry/session surfaces; using provider,
live, credential, network-write, public-sync, push, deploy, or production
surfaces; worker commit.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | Paired work order and two evidence outputs | Static inspection and pending return | Exact manifest and authority | Internal relay; no adapter needed | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | No external interface selected | No CLI/MCP or provider invocation | Private owner comparison requires local inspection | No external consumer requirement; adapter deferred | N/A_WITH_REASON |

## Source Verification Block

| Fact | Source file | Verified section | Disposition |
| --- | --- | --- | --- |
| The three-repo program is active and QM is next | `CVF_SESSION/state/entries/activeExternalAbsorptionProgram.json` | `value` | ACCEPT |
| Program exit and expansion are machine constrained | `docs/reviews/CVF_EXTERNAL_LOCAL_ABSORPTION_PROGRAM_CONTINUITY_HARDENING_2026-09-13.md` | decision and validation | ACCEPT |
| External is preliminary; Local owns private verification and final decision | `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md` | two-step agreement and program continuity | ACCEPT |
| QM mirror identity and immutable pin are registered | `.private_reference/source_mirrors/INDEX.md` | `yc-software__qm` row | ACCEPT |
| Prior aggregate recovery cannot be silently reopened | `docs/reviews/CVF_THREE_REPO_RECOVERY_EVIDENCE_REWORK_COMPLETION_2026-09-13.md` | SCEC disposition | ACCEPT |

Provider-specific memory and the external-agent return are not source authority
for QM runtime behavior. Every runtime-value finding must cite the pinned QM
source and its CVF comparison owner separately.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | `External repo or copied folder` |
| Chain map route | active Local per-source runtime-value recovery |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md` |
| Disposition | ADAPT through Local source verification and per-item terminal accounting |
| Claim boundary | Dispatch routing only; no source value or absorption is accepted here |

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/reviews/CVF_EXTERNAL_LOCAL_ABSORPTION_PROGRAM_CONTINUITY_HARDENING_2026-09-13.md"
}
```

## Acceptance Criteria

1. Exact mirror HEAD equals `361a6c0095dcd3d156aca91353f3ffba0bb8b69b`,
   checkout branch/detached state is recorded, and the mirror is clean and
   unchanged before and after the read-only audit.
2. A deterministic manifest covers every blob under the the memory tree.
3. Every manifest row has actual read depth and a terminal processing status;
   counts reconcile, with exclusions and unreadable files explicit.
4. Directly relevant tests are selected by recorded deterministic searches and
   included in a separate evidence ledger.
5. Every reported mechanism identifies producer, verifier, non-test consumer,
   integration path, test evidence, failure semantics, CVF owner comparison,
   practical benefit, and one allowed terminal value disposition.
6. The audit revisits the named residual hypotheses and records newly found
   value without equating pattern overlap with runtime absorption.
7. No complete-QM or complete-pilot claim is made. Unread QM regions remain
   explicitly `INCOMPLETE` for later bounded accounting.

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | external repository pinned in a local ignored source mirror |
| Upstream or source-mirror disposition | read-only exact pin; no fetch or mutation |
| Enumeration or manifest plan | exact-pin `git ls-tree` for the memory tree plus linked-test ledger |
| Per-file terminal-ledger plan | every target blob receives `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, or `BLOCKED_UNREADABLE` |
| Owner or overlap route | bounded private-CVF owner search per mechanism |
| Value-disposition route | worker proposes evidence; Local makes final dispositions |
| Claim boundary | no source copy, execution, implementation, or self-acceptance |

## Overlap And Novelty Classification

Per-item comparison must test existing CVF owner, real consumer, integration,
test oracle, and failure behavior. External pattern overlap is advisory only.
Use distinct terminal dispositions rather than a repository-wide novelty claim.

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| Each discovered QM mechanism | `OWNER_SURFACE_NOT_FOUND` until exact search is recorded | `OWNER_SURFACE_NOT_FOUND` | Compare consumer, integration, tests, failures, and operational recipe | Worker replaces with an allowed evidence-backed classification |
| Program coordination contract | `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md` | `CONFIRMED_EXISTING` | No new coordination owner is needed | Reuse owner and keep source-value decision local |

## Mandatory Blind-Spot Control Block

Require complete target-tree membership, directly linked tests, non-test
consumers, failure/adverse paths, lifecycle/cleanup, and all prior hypotheses.
Keep every out-of-scope QM region explicit; do not infer source-wide completion.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded pinned-source semantic audit.
- Corpus root: `src/memory` at the required QM pin.
- Snapshot time: worker captures UTC start/end at the immutable pin.
- Enumeration command: filesystem-backed `rg --files --hidden --no-ignore` reconciled to exact-pin `git ls-tree -r --full-tree` for blob identity.
- Manifest artifact or inline manifest: planned worker audit JSON.
- Manifest hash: worker computes from normalized path/blob rows.
- Processing ledger artifact or inline ledger: planned worker audit JSON.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: dispatch state `manifest=19; ledger_terminal=0; exclusions=0; unresolved=19`; accepted return must reach `manifest=19; ledger_terminal=19; exclusions=0; unresolved=0`.
- Declared exclusions: other QM regions; linked tests use a separate ledger.
- Unresolved files: 19 at dispatch; worker must account for every row and reach unresolved=0.
- Unreadable or unsupported files: worker records individually.
- Aggregation check: unique path/blob rows and item IDs reconcile without cross-unit addition.
- Drift check: mirror pin and clean status before/after.
- Output traceability: worker audit to return and Local completion review.
- Adversarial verification: enumeration is not semantic absorption.
- Corpus verdict: PARTIAL - this baseline is tree-bounded.

## Evidence / Verification

Use static source inspection only. Hash and count evidence must be reproducible
from `git -C <mirror> ls-tree -r --full-tree <pin> -- <path>` and source reads
must address immutable blobs or the clean exact-pin checkout. Self-reported
totals, filenames alone, README descriptions, and test names alone are not
sufficient evidence.

Reviewer verification is M5/M10/safety/M20 and evidence-consuming. Local must
not recreate the worker's full read merely because review is due. A rerun needs
a named contradiction, expected information gain, and cost reason.

## Stop Conditions

Return `BLOCKED_WITH_REASON` for pin mismatch, dirty mirror, missing governed
authority, unowned write need, ambiguous corpus reconciliation, or any need to
execute upstream/runtime/provider code. Preserve partial evidence. Do not
substitute another repo and do not choose a next program action.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`EXTERNAL_ABSORPTION`, role=`ORCHESTRATOR`, lifecyclePhase=`DISPATCH`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class EXTERNAL_ABSORPTION --role ORCHESTRATOR --lifecycle-phase DISPATCH --json`.

Returned defects: NONE_RETURNED
Result on 2026-09-14: zero returned defects; `truncated=false`.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | `APPROVED_FOR_EXECUTION`; `WORKER_MUST_NOT_COMMIT`; program continuity markers; write ownership; return status |
| gateRunPurpose | Confirm release structure and machine continuity before dispatch |
| claimBoundary | Documentation dispatch validation only; no runtime behavior proof |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local orchestrator/reviewer |
| Surface | Codex local workspace |
| Working directory | repository root |
| Operation | Read governed authority, build bounded baseline/work order, run deterministic gates |
| Target paths | This baseline and paired work order |
| Allowed scope | Operator instruction to continue Claude work until all three repos are actually handled |
| Commit boundary | Local commits dispatch; worker must not commit |
| Claim boundary | No QM source execution, implementation, or absorption acceptance |

## Claim Boundary

This baseline authorizes a static, evidence-producing audit of QM memory source
tree. It does not authorize implementation, accept a candidate into CVF,
close QM, close the three-repo pilot, or exit/expand the active program.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch with no public artifact or public-sync scope.

## R1/R2/R3 Dependency And R4 Boundary

Accepted R3 completion: `docs/reviews/CVF_QM_RUNTIME_VALUE_R3_COMPLETION_2026-09-14.md`
at `bc914729c149ddc1f5d3d22c62eaab9b1d2769aa`; R1/R2 acceptance unchanged.
R4 is INITIAL and has 19 memory target blobs, disjoint from prior target paths.
Reuse requires exact blob and full-read provenance. Manifest digest: `5fb76f1a20a702dfcf25ad38ace8f6f68491cff8f2791919b5a8c820de20bcfc`.
Git bytes=86253; selected pin `361a6c0095dcd3d156aca91353f3ffba0bb8b69b`; fresh receipt in paired work order.
No whole-QM or implementation claim.

