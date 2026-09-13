# Umbrella Seed Reconciliation Reviewer Decision

Memory class: FULL_RECORD
docType: review
Status: REWORK_REQUIRED
Date: 2026-09-13
Review base: f5bfdffdda4041ce7277026b3ec83dae89eff43d

## Purpose

Reject COMPLETE interpretation and issue one consolidated evidence repair F1-F4.
Preserve useful membership/joins and original return. No source acceptance,
program completion or next-repository intake is granted by this review.

## Target / Source

| Evidence path | Read scope | Review use |
|---|---|---|
| docs/work_orders/CVF_AGENT_WORK_ORDER_UMBRELLA_SEED_RECONCILIATION_2026-09-13.md | Scope, execution and acceptance contract | Required dispositions, hashes, nomination |
| docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json | Parsed row sets, localEvidence, searchLedger, candidates and readDepth | Assertions under review |
| docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_WORKER_RETURN_2026-09-13.md | Findings, gates, SCEC and value tables | Assertions under review |
| docs/audits/CVF_UMBRELLA_SEED_PROVENANCE_RECEIPT_2026-09-13.json | Original decoded field comparison | Exact inherited strings |
| docs/audits/CVF_MCP_KAR_T0_DUAL_CORPUS_RECEIPT_2026-08-23.json | Corpus identity/counts | 885 upstream plus 108 external |
| docs/audits/CVF_MCP_KAR_T0_ABSORPTION_AUDIT_2026-08-23.md | Source identity line 208 | Official MCP URL and exact pin |

External historical ledger rows GEN-F-OBS-001/004 and ARCH-F-023/024 were
read directly from the receipt-bound Downloads files as targeted contradiction
samples; no new upstream scan. MCP T0 ledger header rowCount was checked.

## Scope / Methodology

Startup acknowledged: current mode=multi_repo_absorption_umbrella_reconciliation_dispatched;
active handoff=AGENT_HANDOFF_V60_2026-09-08.md; next allowed move=review evidence
and consolidate next action; parked checkpoint=stopped-chain successor,
implementation/acquisition/provider/live/public/deployment.
EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. Named contradictions:
string corruption, missing dispositions and wrong nomination mechanisms.
Information gain: determine closeability and avoid duplicate next packets.
Cost: one bounded contract/metadata review, no per-row semantic reimplementation.

## Findings / Position

Root-cause cluster: UMBRELLA-SEED-EVIDENCE-INTEGRITY. Single finding set:

```json
[
  {
    "id": "F1",
    "defect": "Receipt-bound strings are corrupted despite verbatim preservation claims",
    "evidence": "Four source labels differ from receipt: SRC-AGENT-GROUNDING-WORKSTREAM, SKILL-SRC-007, SRC-RAG-MAG-CONTEXT, MEM-SRC-003. Five sourceRow strings differ: MEM-ABS-013, SKILL-ABS-001, SKILL-ABS-006, XD-ARCH-ABS-001, XD-MCP-ABS-001. These are decoded JSON value differences, not JSON escape formatting.",
    "repair": "Restore original decoded values directly from UTF-8 receipt. Preserve stable IDs and raw historic rows; keep derived columns separate.",
    "check": "Deep equality for every receipt-owned field in all 54 source records and all 68 historical records; UTF-8 parse round-trip, exact sets and no duplicated IDs."
  },
  {
    "id": "F2",
    "defect": "Required per-row Local dispositions and evidence/search links are missing",
    "evidence": "sourceRows and historicalObligationRows are copies without any disposition field. localEvidence covers only four sources; remaining 50 have no per-source Local lookup disposition. No obligation-level disposition table exists. Three evidenceHash fields contain N/A rather than the required exact hashes.",
    "repair": "Give every source and obligation exactly one allowed metadata disposition with actual evidence/search links. Reuse scoped acceptance, never infer obligation satisfaction from repository intake. Perform the already-authorized bounded canonical lookups and group searches with explicit coverage. Unknowns require truthful searched/unsearched scope and a concrete dependency, not default NO_NEW_VALUE. Compute evidence hashes for selected local files.",
    "check": "54 source dispositions and 68 obligation dispositions; allowed enum, valid join/search/evidence foreign keys; counts partition each ID set; per-evidence path/section/hash and accepted-scope boundary."
  },
  {
    "id": "F3",
    "defect": "Next candidates are not supported by the actual source and evidence chain",
    "evidence": "MCP T0 upstream ledger has 885 rows, not 993; 993 combines 885 upstream and 108 external. Its 22 upstream groups are semantic groups, not 22 repositories. docs/audits/CVF_MCP_KAR_T0_DUAL_CORPUS_RECEIPT_2026-08-23.json names the exact mirror; docs/audits/CVF_MCP_KAR_T0_ABSORPTION_AUDIT_2026-08-23.md line 208 binds official URL and pin 5f5440bb26a62e2cf3440b92da5a667efa03b267. ARCH-F-023 is cross-harness portability, not generic application-to-agent projection; ARCH-F-024 is EXISTING/NO_CHANGE. Candidate uses SRC-EVERYTHING-CLAUDE-CODE-WORKSTREAM while its own join uses SKILL-SRC-004; corroboration must remain distinct. ECC search is claimed but absent from searchLedger; kepano scoped NO_MATCH becomes unsupported anywhere/no acceptance claims.",
    "repair": "Consume supplied MCP identity evidence inside this repair, preserve bounded T9 acceptance and assess real obligation gap. Correct ECC mechanism and primary/corroborating edges. Complete or truthfully retract unrecorded searches and global absence claims. Re-rank up to three nominations based on material remaining value; already-authorized basic lookup is not a separate next research batch.",
    "check": "Every nomination has valid primary source/obligation/finding edge, separate corroboration, concrete Local gap and current scoped evidence. No invented highest priority, global absence or deferred trivial lookup."
  },
  {
    "id": "F4",
    "defect": "Read-depth, value and chain claims overstate or misclassify evidence",
    "evidence": "Domain ledgers are called hashOnly although join columns were read. Return Remaining 47/54 and NO_NEW_VALUE classification lack a reconciled partition or semantic review. Claim that eight ZIP member values match the receipt is unsupported because receipt binds seven members only. Worker SCEC INITIAL/ordinal0 is an echo despite inherited blocker, not demonstrated chain progress.",
    "repair": "Use actual disjoint path/read-depth accounting; distinguish seven receipt-bound member hashes from manifest self-hash. Remove unsupported NO_NEW_VALUE/DOCTRINE_ADAPTED implications for unassessed input; state candidate only. Preserve the original return. New return must link to the exact governing rework work order with real hash, matching prior blockers and computed counters; never self-accept or reset the chain.",
    "check": "Read-depth totals reconcile; semantic unknowns remain unknown; claims and count partitions agree; SCEC predecessor/hash/delta valid with required escalation, no fabricated resolutionEvidence."
  }
]
```

Finding digest: 5869948b2b1c860f0675658d45a58ff90a8e30392704eeb08b39ace8cc6ec237; SHA256 of JSON array serialized with sorted keys,
compact separators and UTF-8. This digest binds all F1-F4, not separate drips.

## Decision

REWORK_REQUIRED. Membership IDs and valid join endpoints are reusable structural
results, not accepted full reconciliation. No source/obligation is independently
accepted by this review. Preserve original return; repair audit and create one
new worker return under a separate reviewed rework packet prepared from this committed finding set; the rework pair is not authority until its subsequent dispatch commit.
Do not reopen QM residual, CGE-R3 or DSH-UC01. No new intake batch yet.

## Risk / Corrective Action

Gate PASS verifies packet mechanics, not complete semantic evidence. F2 work was
already required by the initial contract, so this is evidence repair within the
same task, not expanded source research. Do not launch a separate MCP lookup
packet for the known identity now provided. Local owns review and subsequent
material-value nomination immediately on return, without operator reminder.

## Evidence / Verification

Reviewer-return commit-steward preflight PASS at f5bfdffdda4041ce7277026b3ec83dae89eff43d; worker-return fast
PASS in 4.54 seconds. Unique ID/endpoint checks pass; inherited-value equality
fails for four labels and five backlog rows. A targeted state-entry alias search
for kepano/obsidian/affaan/ECC produced no matches in that scope only.
No full source rehash or corpus rescan was repeated without contradiction.
Incoming raw hashes: {"docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json": "c33b6a02c852da40bb80c9a06c5da95b20c4639175f5bb921c09a5d47a0a59b6", "docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_WORKER_RETURN_2026-09-13.md": "f3d6a549034acd2bb2d73ff609dfe4a8cf26816461a2dffe062465674ef85e1d"}.
Worker source execution/provider/live/public/deploy not authorized by review.

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE
outsideAuthorityBlockers: NONE
nextRepairRoute: ONE_CONSOLIDATED_REWORK
workerRedispatchAllowed: YES_WITH_REVIEWED_REWORK_PACKET
The new pair owns audit repair plus new return; original return is immutable.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_semantic_convergence_control.py |
| literalTokensReviewed | REWORK_REQUIRED; PARTIAL; WORKER_MUST_NOT_COMMIT; NO_SUCCESSOR |
| gateRunPurpose | Confirmation of nonterminal review packaging; no semantic PASS inference |
| claimBoundary | Consolidated evidence review only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer/dispatcher |
| Provider or surface | internal workspace |
| Session or invocation | umbrella-seed-review-20260913 |
| Working directory | private provenance root |
| Command or tool surface | targeted JSON comparisons and canonical reads, reviewer-return preflight |
| Target paths | docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json; docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_WORKER_RETURN_2026-09-13.md; docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_COMPLETION_2026-09-13.md |
| Allowed scope source | Original Reviewer Closure Conversion and standing operator mandate |
| Before status evidence | HEAD f5bfdffdda4041ce7277026b3ec83dae89eff43d; exactly two untracked worker output paths |
| After status evidence | Three review material paths; original worker evidence preserved; rework dispatch pair follows separately |
| Diff evidence | git status --short --untracked-files=all |
| Approval boundary | Consolidated internal evidence repair only |
| Claim boundary | No absorption, runtime or public acceptance |
| Agent type | reviewer/dispatcher |
| Invocation ID | umbrella-seed-review-20260913 |
| Expected manifest | docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json; docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_WORKER_RETURN_2026-09-13.md; docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_COMPLETION_2026-09-13.md |
| Actual changed set | docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json; docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_WORKER_RETURN_2026-09-13.md; docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_COMPLETION_2026-09-13.md |
| Manifest delta | MATCH |

## Epistemic Process Block

Expected Result / Prediction: restored seed metadata enables material nomination.
Evidence Comparison: stable IDs survive but literal values differ, Local states
are omitted, and MCP/ECC claims do not match cited evidence.
Contradiction Or Gap Disposition: F1-F4 consolidated repair; preserve raw return.
Claim Update: pending evidence is not ready for acceptance or next intake.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY: private review evidence; no export.

## Claim Boundary

Nonterminal review only. Original three-repo chain STOP/NO_SUCCESSOR remains.
This review neither claims complete absorption nor authorizes implementation.

## Corpus Completeness And Report Integrity

- Corpus task class: nonterminal review of disputed metadata evidence
- Corpus root: exact source and artifact paths in Target / Source
- Snapshot time: 2026-09-13 review at f5bfdffdda4041ce7277026b3ec83dae89eff43d
- Enumeration command: filesystem-backed targeted file/JSON reads; no new whole-corpus enumeration
- Manifest artifact or inline manifest: Target / Source; original audit assertions require F1 repair
- Manifest hash: UNKNOWN for disputed worker read set; incoming raw artifact hashes retained in reviewer decision
- Processing ledger artifact or inline ledger: worker audit; nonterminal and not accepted
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=0; ledger_terminal=0; exclusions=0; unresolved=0 for newly executed corpus scans; no new scan performed. Worker count claims are disputed, not certified by these zeros.
- Unresolved files: UNKNOWN; F1 requires unique path/depth reconciliation
- Declared exclusions: all upstream corpus-wide traversal and implementation recreation
- Unreadable or unsupported files: UNKNOWN for the unaccepted worker corpus
- Aggregation check: FAIL for inherited strings and per-row dispositions; F1 repair required
- Drift check: worker pin/status assertions retained; no fresh upstream query
- Output traceability: reviewer decision F1-F4 and original audit
- Adversarial verification: reject all-files-read, complete absorption and unsupported count claims
- Corpus verdict: PARTIAL


## Mandatory Blind-Spot Control Block

SKIPPED_WITH_REASON: nonterminal reviewer packaging; source recovery remains
incomplete and F1-F4 are required before acceptance. No corpus completeness inferred.


## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: Local packages a rejected metadata return
and issues evidence repair; no source conversion, import or execution occurs.


## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | external repo or copied folder |
| Chain map route | bounded initial survey then Local review then separate selected absorption |
| Matching local-view guard | governance/compat/check_task_governance_route.py |
| Owner surface | docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md |
| Disposition | Initial evidence collection only; no source acceptance |
| Claim boundary | No source execution or value conversion in this dispatch |

## Reviewer Packaging Repair Disclosure

Original worker content is retained; reviewer added only the mandatory Allowed terminal statuses line with BLOCKED_UNREADABLE vocabulary to satisfy the full corpus gate. No evidence claim or reported disposition was corrected in the original return. Raw incoming SHA256 remains recorded above; packaged return SHA256 is c73e7342ecf33439b25c1d982b39930189d2c8ec703d9817d187519d54c204d3. Rework worker must preserve this packaged original unchanged. The audit is byte-unchanged.
