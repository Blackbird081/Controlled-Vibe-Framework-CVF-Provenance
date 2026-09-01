# CVF MFRP-P3-R1A Independent Review - Return To Design

Memory class: governed-review

docType: review

Status: REVIEWER_REJECTED_RETURN_TO_DESIGN

Date: 2026-09-02

Batch ID: MFRP-P3-R1A-REVIEW

Review base head: `c94162919d3321a713c936ab8deb25fe929eab1b`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Record the independent disposition of the two-path R1A worker return, preserve
its exact bytes as rejected evidence and define one consolidated correction
set. This review checks returned evidence; it does not recreate the oracle,
invoke P2 or perform R1B.

## Target / Source

| Source | Identity / role |
|---|---|
| R1A baseline | `docs/baselines/CVF_GC018_MFRP_P3_R1A_COMMITTED_ORACLE_RATIFICATION_2026-09-01.md`; SHA-256 `ed0811e913cbd6229aba4fa5662fe0ebf043d79dd02e0002872a932d85066b32` |
| R1A work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_R1A_COMMITTED_ORACLE_RATIFICATION_2026-09-01.md`; SHA-256 `4f86dbb6c2a46d2f3a8797ebcb7bdc8185f70139dcfe64447f3a1000bc9feb3a` |
| rejected oracle | archive manifest `docs/reviews/rejected_evidence/MFRP_P3_R1A_2026-09-02/ARCHIVE_MANIFEST.txt`; SHA-256 `732b756b4231c9499cb1648e5798c70f4774e22962f8604d11e0a31c20439940`; `NOT_ACTIVE_AUTHORITY` |
| rejected worker return | same archive manifest; SHA-256 `093518b84047b0b0f295c157710743d1b83ba4eb779c84fdbb5a8392abbc1f6a`; `NOT_ACTIVE_AUTHORITY` |
| P2 receipt owner | `governance/compat/agent_autorun_machine_verification.py`; SHA-256 `8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022` |
| P2 readout owner | `governance/compat/agent_automation_machine_verification_readout.py`; SHA-256 `ff6088bf8144deec4582ce9faf62384b314346c9cbbb87f6b3349a2d23f7e7c3` |

## Scope / Methodology

The reviewer confirmed execution base `c94162919d3321a713c936ab8deb25fe929eab1b`,
the exact two untracked paths and no staging/commit. It recomputed all nine
pinned source hashes, parsed the JSON, reconciled 20 cases/18 families/seven
classes, read both P2 seams and compared each disputed case to its declared
mutation, attack-binding mode, predicate and static route. It did not construct
a receipt, import a P2 owner or invoke a P2 function.

Worker-return fast passed, including reviewer-fast 67/67. That proves document
shape and repository compatibility only; it does not waive the contract or
semantic findings below.

## Findings / Position

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| R1A-RV-1 | CRITICAL | the worker constructed a canonical receipt and invoked `_validate_receipt_integrity`, `build_machine_verification_readout` and `machine_readout_to_dict`; the baseline required `BLOCKED_WITH_REASON` before any P2 invocation or receipt build | BLOCKS_RATIFICATION |
| R1A-RV-2 | HIGH | the work order required a nonexistent autorun phase `pre-review`; the command returned BLOCKED while the terminal contract required every named gate PASS | DISPATCH_PACKET_CORRECTION_REQUIRED |
| R1A-RV-3 | CRITICAL | C07 declares `ATTACKER_REBOUND`, but its evidence proves only failure when dependent identity/digest values are not fully rebound; it does not establish rejection of the declared attacker model | ORACLE_CASE_CORRECTION_REQUIRED |
| R1A-RV-4 | HIGH | C08 reduces earlier-batch verifier/dependency drift to an after-binding nested/top-level envelope mismatch and therefore does not model the cross-batch identity claim | ORACLE_CASE_CORRECTION_REQUIRED |
| R1A-RV-5 | HIGH | C16 covers only an unmutated positive control and omits the required one-bound-input cache-invalidation half of its family | ORACLE_CASE_CORRECTION_REQUIRED |
| R1A-RV-6 | CRITICAL | C18 adds a synthetic high-risk field and relies on ordinary digest tamper; current P2 has no high-risk/live/public/destructive authority input, so this family is not statically represented by that route | MARK_NOT_REPRESENTABLE_OR_REDESIGN_ROUTE |

## Risk / Corrective Action

Accepting the returned oracle would convert execution-derived observations
into a document presented as static evidence and would ratify four materially
misrepresented defect families. Preserve the rejected bytes, supersede the
original dispatch, and issue only the bounded static-only R1A-R1 correction
defined below. R1B remains closed until an independent reviewer ratifies a
fresh oracle.

## Consolidated Correction Contract

One R1A-R1 rework packet may proceed with all findings delivered atomically:

1. create a fresh oracle and fresh worker return; never reuse active paths or
   content from the rejected archive;
2. static-only means filesystem/source reads, JSON parsing, hashing and text
   search only: no import, dynamic loading, AST execution, function call,
   receipt/payload construction, monkeypatch, test or temporary executable;
3. use existing `pre-implementation` and `reviewer-fast` gates only; remove
   the nonexistent `pre-review` command;
4. C07 must either prove the fully rebound attacker model from source alone or
   be `NOT_REPRESENTABLE_BY_CURRENT_P2`;
5. C08 must model cross-batch verifier/dependency identity rather than a
   same-object envelope mismatch, or be unrepresentable;
6. C16 must cover both exact-identity reuse and invalidation after one bound
   input changes, or be unrepresentable at the P2 seam;
7. C18 must be `NOT_REPRESENTABLE_BY_CURRENT_P2` unless an existing P2 field
   actually carries the high-risk authority condition;
8. every case must pass a family-to-mechanism semantic audit; generic receipt
   digest tamper is not sufficient merely because it produces rejection.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "mfrp-p3-r1a-oracle",
  "chainMode": "SUCCESSOR",
  "chainOrdinal": 1,
  "predecessor": {
    "path": "docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_R1A_COMMITTED_ORACLE_RATIFICATION_2026-09-01.md",
    "sha256": "4f86dbb6c2a46d2f3a8797ebcb7bdc8185f70139dcfe64447f3a1000bc9feb3a"
  },
  "blockerDelta": {
    "prior": ["r1a-oracle-not-yet-ratified"],
    "resolved": [],
    "retained": ["r1a-oracle-not-yet-ratified"],
    "new": ["r1a-static-only-execution-boundary", "r1a-family-mechanism-mismatch"],
    "reopened": [],
    "current": ["r1a-oracle-not-yet-ratified", "r1a-static-only-execution-boundary", "r1a-family-mechanism-mismatch"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 1,
    "nonDecreasingBlockerTransitions": 1
  },
  "claims": [{
    "claimId": "MFRP-P3-R1A-REVIEW-RETURN-TO-DESIGN",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Decision / Disposition

`RETURN_TO_DESIGN`.

The returned oracle is not ratified and cannot become R1B predecessor input.
The two returned files are preserved byte-identically under `.rejected`
suffixes. One corrective R1A-R1 dispatch may be authored; R1B and P4 remain
closed.

## Finding-To-Governance Learning Disposition

- Defect class: `WORKER_EXECUTION_ERROR`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `RULE_EXISTS`
- Next control action: bind the existing no-execution rule to explicit static-
  only allowed/forbidden operation classes and remove the invalid phase from
  the corrective work order; no new general checker is justified yet.

## Epistemic Process Block

### Expected Result / Prediction

A static-only R1A worker should stop rather than call the measured P2 seams,
and every case should represent its full declared family and attack mode.

### Evidence Comparison

The return explicitly records all three calls and a constructed receipt. Static
source comparison also contradicts C07, C08, C16 and C18 as declared.

### Contradiction Or Gap Disposition

The execution breach contaminates feasibility provenance and independently
activates the stop condition. Mechanical gate PASS cannot cure it.

### Claim Update

Evidence supports `R1A_ORACLE_NOT_RATIFIED_CORRECTIVE_REWORK_REQUIRED`, not an
oracle safety or runtime finding about P2.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_machine_closure_package.py` |
| literalTokensReviewed | governed review headings; accepted defect/lane/disposition tokens; epistemic four-part structure; trace fields; public disposition; machine closure rows |
| gateRunPurpose | preserve one evidence-backed rejection and consolidated correction set without converting machine PASS into ratification |
| claimBoundary | checker PASS validates document structure only; it cannot ratify an oracle or open R1B |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | original R1A work order plus this review | original bytes retained as historical dispatch evidence; this review rejects its return and the fresh R1A-R1 work order supersedes execution authority | PASS |
| Completion or reviewer artifact | this review | `RETURN_TO_DESIGN` and six consolidated findings | PASS |
| Roadmap state | existing MFRP roadmap | N/A with reason: R1A-R1 is a correction under the accepted two-tranche design; no roadmap claim changes | N/A with reason |
| Registry JSON | N/A with reason: no corpus/registry owner changed | no mutation | N/A with reason |
| Registry Markdown | N/A with reason: no registry owner changed | no mutation | N/A with reason |
| External evidence digest | rejected-evidence archive manifest | two exact SHA-256 identities | PASS |
| System loop interlock | N/A with reason: R1B/P4 remain closed | no interlock mutation | N/A with reason |
| Session continuity | active continuity surfaces | separate post-material sync after corrective dispatch commit | PENDING_SEPARATE_SYNC |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF independent reviewer/orchestrator |
| Provider or surface | local private provenance repository |
| Session or invocation | MFRP-P3-R1A independent review, 2026-09-02 |
| Working directory | repository root |
| Command or tool surface | governed reads, SHA-256, JSON parse, static P2 inspection, worker-return fast and git |
| Target paths | two rejected worker outputs, this review and archive manifest |
| Allowed scope source | operator returned `COMPLETE_PENDING_REVIEW` and then instructed the reviewer to handle the rejection |
| Before status evidence | HEAD `c94162919d3321a713c936ab8deb25fe929eab1b`; exact two untracked worker outputs; nothing staged |
| After status evidence | exact bytes relocated under `.rejected`; review/manifest authored; no active oracle remains |
| Diff evidence | archive hashes equal original returned hashes; final exact changed set reconciled before commit |
| Approval boundary | independent review, rejection preservation and corrective-dispatch preparation only |
| Claim boundary | no oracle ratification, P2 invocation/mutation, R1B, P4 or external effect |
| Agent type | independent reviewer/orchestrator |
| Invocation ID | `mfrp-p3-r1a-independent-review-return-to-design-2026-09-02` |
| Expected manifest | `docs/baselines/CVF_GC018_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md`; `docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md`; `docs/reviews/rejected_evidence/MFRP_P3_R1A_2026-09-02/ARCHIVE_MANIFEST.txt`; `docs/reviews/rejected_evidence/MFRP_P3_R1A_2026-09-02/governance_compat_fixtures_mfrp_p3_r1a_actual_seam_replay_oracle.json.rejected`; `docs/reviews/rejected_evidence/MFRP_P3_R1A_2026-09-02/CVF_MFRP_P3_R1A_COMMITTED_ORACLE_RATIFICATION_WORKER_RETURN_2026-09-01_md.rejected`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md`; `docs/reviews/CVF_MFRP_P3_R1A_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-02.md`; `docs/reviews/rejected_evidence/MFRP_P3_R1A_2026-09-02/ARCHIVE_MANIFEST.txt`; `docs/reviews/rejected_evidence/MFRP_P3_R1A_2026-09-02/governance_compat_fixtures_mfrp_p3_r1a_actual_seam_replay_oracle.json.rejected`; `docs/reviews/rejected_evidence/MFRP_P3_R1A_2026-09-02/CVF_MFRP_P3_R1A_COMMITTED_ORACLE_RATIFICATION_WORKER_RETURN_2026-09-01_md.rejected`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_2026-09-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | two untracked rejected outputs moved byte-identically to the content-addressed archive; original hashes preserved |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance rejection and corrective dispatch evidence.

## Claim Boundary

This review rejects one R1A execution and authorizes only preparation of a
corrective static-only R1A-R1 packet. It does not ratify an oracle, decide P2
safety, open R1B/P4-P6, modify P2, change downstream workspace or authorize
provider/live/network/public/deploy/production effects.
