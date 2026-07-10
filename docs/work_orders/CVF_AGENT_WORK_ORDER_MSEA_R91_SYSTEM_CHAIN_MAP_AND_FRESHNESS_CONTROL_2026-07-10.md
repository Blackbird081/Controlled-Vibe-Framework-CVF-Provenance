# CVF Agent Work Order - MSEA-R91 System Chain Map And Freshness Control

Memory class: governed-work-order

Status: DISPATCH_READY

Date: 2026-07-10

Batch ID: MSEA-R91

Commit mode: WORKER_MUST_NOT_COMMIT

Worker role: delegated worker role

Reviewer/closer: reviewer/closer role

dispatchBaseHead: `252fe1a3e`

## Dispatch Prompt Envelope

Role: delegated worker. A separate reviewer/closer owns commits and closure.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R91_SYSTEM_CHAIN_MAP_AND_FRESHNESS_CONTROL_2026-07-10.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture current `git rev-parse --short HEAD` before edits.

Current-time notes: R90 Audit A is accepted at `645df8b83`; current dispatch
base is `252fe1a3e`; no credential or live-provider action is authorized.

Do-not-misread notes: implement only the exact sixteen paths; hashes detect
drift but never authorize automatic semantic verdict rewriting; do not move the
advisory directory.

Required first actions: read the Required First Reads in order, capture status
and executionBaseHead, then run the pre-implementation gate and worker-return
scaffold command before material edits.

Return contract: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` with exact
changed paths, source hashes, test/gate evidence, final status, and unchanged
worker HEAD.

## Purpose

Produce Deliverable B as a stable reference for operators, developers, and
future agents. Preserve every partial/historical/future boundary accepted in
Audit A. Prevent the map from quietly becoming stale by checking source-file
fingerprints, source existence, Markdown/JSON agreement, and a 30-day semantic
review age. Run the same read-only check locally, in existing CI, and weekly.

## Target / Source

Target output family:

- human map: `docs/reference/system_chain/README.md`;
- machine map: `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`;
- maintenance contract:
  `docs/reference/system_chain/CVF_SYSTEM_CHAIN_FRESHNESS_STANDARD.md`;
- checker/tests/wiring and bounded evidence-path corrections.

Canonical source is MSEA-R90 Audit A and its reviewer completion at material
commit `645df8b83`, followed by current source directly read by the worker.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R91 --title "System Chain Map And Freshness Control" --date 2026-07-10 --base 252fe1a3e --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SATISFIED: MSEA-R90 Audit A reviewer acceptance at 645df8b83 and operator continuation on 2026-07-10." --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with exact implementation schema, source rows, protected path authorization, tests, CI schedule, and reviewer closure conversion. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| docOnlyNewFields | laneId, planeRange, currentPosture, sourceFingerprints, lastVerifiedDate, maxAgeDays, freshnessState, operatorReadout, nextReviewAction |
| claimBoundary | Dispatch provenance only; implementation remains pending worker execution and reviewer acceptance. |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| Audit A reviewer acceptance | `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md`; commit `645df8b83` | B may use accepted findings only. | PASS |
| Current next move | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` routes fresh B/freshness packet authoring. | Dispatch requires fresh packet and pre-dispatch pass. | PASS |
| Operator authority | Operator instructed Codex to continue from the accepted R90 completion artifact. | B plus bounded freshness implementation may proceed. | PASS |
| Worker commit boundary | paired GC-018 selects `WORKER_MUST_NOT_COMMIT`. | Worker returns uncommitted exact manifest. | PASS |

## Authority Chain

1. Root agent instructions and current session front doors for workflow scope.
2. Paired MSEA-R91 GC-018 baseline.
3. MSEA-R90 Audit A Markdown, JSON evidence, and reviewer completion.
4. Current doctrine/source files cited by Audit A.
5. Current checker, hook, autorun, workflow, and generated-registry contracts.

No temporary advisory report or provider-specific memory is CVF authority.

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | Authorizes R91 scope and any later expansion. |
| Dispatcher | Owns this source-verified packet and dispatch commit. |
| Worker | Implements exact manifest, runs tests/gates, returns without commit. |
| Reviewer/closer | Recomputes representative hashes and failures, repairs allowed defects, commits accepted material, and syncs continuity separately. |

## Required First Reads

1. `CVF_SESSION_MEMORY.md`.
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
4. `AGENT_HANDOFF_V40_2026-07-10.md`.
5. `docs/reference/guard_orientation/README.md`.
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
7. Paired MSEA-R91 GC-018 baseline.
8. This work order.
9. R90 Audit A Markdown, JSON, and completion review.
10. Every source file in Source Verification Block before editing its owner.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| R90 accepted baseline | `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md` | Status line 5; Decision section lines 74-84 | `REVIEWER_ACCEPTED_BOUNDED` | MSEA-R90 completion review | ACCEPT |
| Human five-lane findings | `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md` | lane headings lines 67, 116, 194, 298, 335 | five lane verdicts | Audit A Markdown | ACCEPT |
| Machine five-lane findings | `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json` | `chainEdges`, `manifestRecords`, `pathDispositions` | `chainEdges` | Audit A evidence schema | ACCEPT |
| Doctrine authority | canonical contract: `ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md` | Layer Overview lines 18-32 | L0-L6 | frozen doctrine | ACCEPT |
| GC-019 stale path | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | line 54 | `GC-019` evidence list | Governance Control Matrix | ACCEPT |
| Operational index stale/missing paths | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | lines 22-24, 38, 41, 46-47, 58 | evidence lookup paths | Operational Reference Index | ACCEPT |
| Autorun insertion owner | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` line 54 | `_common_commands` | agent autorun command catalog | ACCEPT |
| Pre-commit insertion owner | `governance/compat/local_governance_hook_catalog_pre_commit.py` | line 6 | `PRE_COMMIT_CHECKS` | local hook catalog | ACCEPT |
| Pre-push insertion owner | `governance/compat/local_governance_hook_catalog_pre_push.py` | line 6 | `PRE_PUSH_CHECKS` | local hook catalog | ACCEPT |
| Reviewer-fast insertion owner | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | line 6 | `REVIEWER_FAST_CHECKS` | local hook catalog | ACCEPT |
| Existing CI insertion owner | `.github/workflows/documentation-testing.yml` | name line 1; trigger block line 3 | `Documentation & Testing` | GitHub Actions workflow | ACCEPT |
| Freshness checker implementation pattern | `governance/compat/check_roadmap_closure_freshness.py` | validator line 164; main line 197 | `validate_roadmap_closure_freshness` | freshness checker module | ACCEPT |
| Freshness test pattern | `governance/compat/test_check_roadmap_closure_freshness.py` | tests lines 15, 35, 58, 78 | focused fixtures | pytest module | ACCEPT |
| Generated corpus registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | top-level `corpora` | `corpora` | GC-051 generated aggregate | ACCEPT |
| GC-051 generator | `governance/compat/generate_corpus_scan_registry.py` | `generate_aggregate` and `--generate` action | `generate_aggregate` | generated aggregate owner | ACCEPT |

## New Doc-Only Fields

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| laneId | Stable Markdown/JSON key. | Yes | Yes | Exactly five unique values. |
| planeRange | Doctrine and component coverage. | Yes | Yes | Explicit L0-L6 or bounded cross-plane value. |
| currentPosture | CURRENT, PARTIAL, HISTORICAL, or FUTURE. | Yes | Yes | Matches accepted Audit A claim. |
| sourceFingerprints | Path and SHA-256 list. | Yes | Yes | Every path exists and hash matches. |
| lastVerifiedDate | Semantic review date. | Yes | Yes | ISO date. |
| maxAgeDays | Review-age ceiling. | Yes | Yes | Integer `30`. |
| freshnessState | Machine freshness result. | Yes | Yes | CURRENT, SOURCE_DRIFT, PATH_MISSING, MAP_DRIFT, AGE_EXPIRED. |
| operatorReadout | Human remediation text. | Yes | Yes | Present for each failure class. |
| nextReviewAction | Governed follow-up, never auto-verdict rewrite. | Yes | Yes | Non-empty. |

## Current Runtime Freshness Verification

This tranche changes repository governance automation, not product runtime.
The worker must re-read each insertion owner at executionBaseHead and record
exact insertion locations. If any symbol or path differs from the Source
Verification table, update only the worker return with `REJECT` and the current
symbol, or return to the orchestrator with a source-not-found blocking reason
when no safe owner exists.

## Negative Search And Collision Discipline

| Check | Command/root/query | Disposition |
|---|---|---|
| Output collision | `rg --files --hidden --no-ignore docs governance .github | rg 'MSEA[_-]R91|SYSTEM_CHAIN_MAP|system-chain-map-freshness'` | COLLISION_CHECK_REQUIRED: historical or proposed mentions are non-authoritative; an exact active target-path collision blocks creation. |
| Existing map owner | `rg -n "whole-picture|system-chain map|sourceFingerprints" docs/reference governance/compat` | Enrich an existing owner if a canonical equivalent exists; otherwise use planned owner. |
| Missing H2 artifact | `rg --files --hidden --no-ignore | rg 'CVF_H2_WORKING_MEMORY_RUNTIME_PROOF_COMPLETION_2026-05-22.md$'` | Do not create or substitute without semantic proof. |
| Stale basenames | Search every R90 `STALE_ARCHIVE_MOVE` basename under active and archive owners. | Correct only confirmed successors. |
| Checker name collision | `rg --files governance/compat | rg 'check_system_chain_map_freshness.py$'` | COLLISION_CHECK_REQUIRED: an exact current target path blocks creation; similar freshness names do not. |
| Same-token collision: `executionBaseHead` | Exact repo-wide token search | NON_AUTHORITATIVE_COLLISION: this required handoff field intentionally occurs elsewhere; the absence interpretation is rejected. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`system-chain map freshness`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "system-chain map freshness" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: exact query returned no entries. |
| Dispatch impact | Source hashing, checker read-ahead, protected authorization, generated-registry pairing, and no-commit review remain mandatory. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one read-only system-chain map
freshness checker and test; wire only that checker into current local/autorun/CI
owners; add one scheduled read-only workflow.

Protected paths:

- `governance/compat/check_system_chain_map_freshness.py`
- `governance/compat/test_check_system_chain_map_freshness.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `.github/workflows/documentation-testing.yml`
- `.github/workflows/system-chain-map-freshness.yml`

Operator authorization: the operator required automatic updating or reminders
after the scan and continued after reviewer acceptance of Audit A.

Rollback boundary: revert only the exact R91 worker and reviewer changed set.
Do not revert R90, R72F, or unrelated hook controls.

Scope boundary: no semantic auto-edit, runtime/product source, Web UI,
provider/live proof, public-sync, session mutation, or advisory relocation.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake summary | Convert reviewer-accepted Audit A into a stable map and durable drift reminder. |
| Scope classification | Reference, checker, focused test, catalog wiring, CI schedule, and path-owner correction. |
| Risk sensitivity | Protected governance wiring and stale-claim risk; no product runtime. |
| Selected role route | MULTI_AGENT_MULTI_ROLE |
| Escalation condition | Source owner missing, semantic contradiction with R90, required scope beyond exact manifest, or need for destructive/public/live action. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

route: MULTI_AGENT_MULTI_ROLE

rolePattern: MULTI_AGENT_MULTI_ROLE

phase: dispatch, worker execution, reviewer closure, optional session sync

baseHeadFor(phase): dispatchBaseHead=`252fe1a3e`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_MUST_CAPTURE_AT_CLOSURE

changedSetScope(phase): dispatch pair; exact sixteen-path worker manifest;
reviewer-owned closure paths only

traceScope(phase, actor): exact source reads, hashes, tests, paths, diffs, and
per-role base anchors

commitOwner(phase): worker commit forbidden; reviewer/closer owns accepted
material commit

crossBatchIsolation: clean worktree required before worker execution; no Web
UI, runtime/provider/live, public-sync, session, lifecycle change, or advisory
relocation

nextMoveSurfaces: reviewer updates continuity only upon reviewer acceptance

dispatchBaseHead: `252fe1a3e`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_MUST_CAPTURE_AT_CLOSURE

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R91_SYSTEM_CHAIN_MAP_AND_FRESHNESS_CONTROL_COMPLETION_2026-07-10.md`

reviewerOwnedClosurePaths:

- every worker-owned path in Write Ownership;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R91_SYSTEM_CHAIN_MAP_AND_FRESHNESS_CONTROL_2026-07-10.md`;
- `docs/reviews/CVF_MSEA_R91_SYSTEM_CHAIN_MAP_AND_FRESHNESS_CONTROL_COMPLETION_2026-07-10.md`.

pendingStatusTokensAllowedBeforeReview: COMPLETE_PENDING_REVIEW,
IMPLEMENTATION_COMPLETE_PENDING_REVIEW, DRAFT, HOLD_*

forbiddenClosedEquivalentResidue: COMPLETE_PENDING_REVIEW, NOT_EXECUTED_YET,
WORKER_RETURNS_PENDING, PRE_CLOSURE_NOT_RUN, FAIL_EXPECTED_PENDING_FINALITY,
DISPATCHED as current status

predecessorClosureFactSource: stable MSEA-R90 completion review and material
commit `645df8b83`, not mutable session prose

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for source reads, deterministic hashing,
reference authoring, allowed path corrections, checker/test implementation,
catalog/workflow insertion, generated registry refresh, and gate repairs within
Write Ownership. Stop only for a semantic contradiction, missing source owner,
destructive action, public/live action, or required scope outside this packet.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | map README/JSON/standard and checker CLI output | Repo-local static governance only | fingerprints, focused tests, hook/CI wiring | no remote adapter | IMPLEMENT_AND_TEST |
| `EXTERNAL_AGENT_CLI_MCP` | N/A with reason: no external adapter is authorized | No ingress, auth, mutation, receipt, or remote execution | Forbidden Scope | remains separate | N/A_WITH_REASON |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: reviewer-accepted MSEA-R90 Audit A is the semantic
baseline; every fingerprint and current path is recomputed at execution.

priorVerificationAnchor: material commit `645df8b83` and current worker
executionBaseHead.

freshRecomputeRequired: YES

unicodePathHandling: UTF-8 readers with explicit encoding and replacement;
authored governed text defaults to ASCII.

extractedTextAuthority: SOURCE_AUTHORITY

## System Loop Interlock Routing

| Field | Value |
|---|---|
| Upstream loop | Reviewer-accepted MSEA-R90 Audit A and current source files. |
| Upstream output | Five bounded lane verdicts and source manifest. |
| Downstream loop | Human whole-picture map, machine map, and freshness checker. |
| Downstream input | Accepted findings plus recomputed fingerprints. |
| Finding route | Drift emits fail-closed remediation and returns to governed review. |
| Mutation boundary | Checker and weekly workflow are read-only; no semantic auto-update. |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | Stable system-chain reference family under `docs/reference/system_chain/`. |
| Storage decision | README is human front door; JSON is machine map; standard owns maintenance semantics. |
| Existing aggregate impact | One new GC-051 entry source plus regenerated aggregate is required. |
| Generated state impact | None; worker cannot edit session/workspace state. |
| Durable governance boundary | Checker owns drift detection; reviewer owns semantic verdict updates. |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | historical advisory scout -> R90 CVF-source audit -> reviewer-accepted R90 -> R91 canonical map |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R91 system-chain reference family |
| Disposition | ADAPT only accepted, independently verified findings |
| Claim boundary | Temporary advisory files are not evidence and are not promoted. |

## Planned Worker Fulfillment Manifest

| Artifact | Required worker action | Required at handoff |
|---|---|---|
| `docs/reference/system_chain/README.md` | Create truthful whole-picture map and operator readout. | Yes |
| `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | Create deterministic five-lane map with fingerprints and freshness metadata. | Yes |
| `docs/reference/system_chain/CVF_SYSTEM_CHAIN_FRESHNESS_STANDARD.md` | Define hash, age, drift, reminder, review, and no-auto-semantics contract. | Yes |
| `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | Correct confirmed GC-019 archive path only. | Yes |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Correct confirmed archive paths, handle missing H2 honestly, and add system-chain map lookup. | Yes |
| `governance/compat/check_system_chain_map_freshness.py` | Create read-only checker. | Yes |
| `governance/compat/test_check_system_chain_map_freshness.py` | Create focused positive/negative tests. | Yes |
| `governance/compat/agent_autorun_command_catalog.py` | Add checker to common autorun commands. | Yes |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | Add checker command. | Yes |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | Add checker command. | Yes |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | Add checker command. | Yes |
| `.github/workflows/documentation-testing.yml` | Add checker to existing documentation CI. | Yes |
| `.github/workflows/system-chain-map-freshness.yml` | Add weekly/manual read-only reminder workflow. | Yes |
| `docs/corpus-intelligence/registry/entries/msea-r91-system-chain-map-and-freshness.json` | Register bounded R91 source/output family. | Yes |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Regenerate from entry sources. | Yes |
| `docs/reviews/CVF_MSEA_R91_SYSTEM_CHAIN_MAP_AND_FRESHNESS_CONTROL_WORKER_RETURN_2026-07-10.md` | Create full no-commit worker return. | Yes |

## Write Ownership

Worker-owned paths are exactly the sixteen paths in Planned Worker Fulfillment
Manifest.

Write mode: create new planned files; bounded modifications to existing planned
owners; generated aggregate only through its generator.

Forbidden paths: every other repository path, including paired dispatch
baseline, active session/handoff files, R90 artifacts, cross-family checkers,
scenario registry, runtime/product source, public-sync, and advisory directory.

## Freshness Contract Requirements

The machine JSON must include:

- schemaVersion and stable mapId;
- sourceAudit and reviewerCompletion paths;
- exactly five ordered lane records with laneId, planeRange, currentPosture,
  verdict, implementedBy/invokedBy/testedBy/evidenceOwner/operatorSurface,
  knownGaps, and nextReviewAction;
- sourceFingerprints array with repo-relative path, SHA-256, and evidence role;
- lastVerifiedDate=`2026-07-10` and maxAgeDays=`30`;
- reminder policy stating semantic verdicts are never auto-rewritten.

The checker must:

1. parse JSON with UTF-8;
2. validate required keys, enums, five unique ordered lane IDs, and SHA format;
3. recompute every source SHA-256 and fail missing/mismatch;
4. compare README lane IDs and verdicts against JSON;
5. fail when `asOfDate - lastVerifiedDate > maxAgeDays`;
6. validate checker presence in all four local/autorun catalogs and both CI
   workflow surfaces;
7. emit one actionable human message per failure plus secret-free JSON output;
8. accept `--as-of-date YYYY-MM-DD`, `--json`, and `--enforce`;
9. never write the map, hashes, verdicts, session state, or source files.

The weekly workflow must use read-only repository permissions, no secret, a
weekly cron, manual dispatch, and the checker command with `--enforce`.

## Evidence Path Correction Rules

- Replace the GC-019 active path with its confirmed archive-qualified path.
- Replace each of R90's ten distinct archive-moved Operational Index paths
  with its confirmed archive-qualified successor.
- Remove the missing H2 path token or label the historical claim missing while
  retaining the distinct T5 artifact. Do not claim equivalence.
- Re-run exact basename and path existence checks after edits.
- The new freshness checker must cover both corrected owner documents.

## Focused Test Matrix

| Test | Expected result |
|---|---|
| current fixture with valid hashes and age <=30 | PASS |
| one source path missing | PATH_MISSING failure |
| one source content changed | SOURCE_DRIFT failure |
| README lane verdict differs from JSON | MAP_DRIFT failure |
| duplicate/missing lane ID | schema failure |
| as-of date at day 30 | PASS |
| as-of date at day 31 | AGE_EXPIRED failure |
| missing one hook/catalog/workflow binding | wiring failure |
| `--json` output | valid secret-free JSON with status and violations |
| checker run in real repo after all edits | PASS |

## Worker Output Checker Read-Ahead Mandate

Before authoring each new reference, checker, workflow, or worker return, read
the checkers applicable to that path family and content triggers. The dispatch
checklist is not a substitute. Record applicable checker paths and literal
tokens in the worker return.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R91_SYSTEM_CHAIN_MAP_AND_FRESHNESS_CONTROL_WORKER_RETURN_2026-07-10.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required worker-return sections include Purpose, Target / Source, Scope /
Methodology, Findings / Position, Risk / Corrective Action, Decision /
Disposition, Checker Source Read-Ahead Block, External Knowledge Intake
Routing, Epistemic Process Block, Agent Operation Trace Block, Delta Execution
Claim Boundary Control Block, Public Export Disposition, Corpus Completeness
And Report Integrity, Finding-To-Governance Learning Disposition, Claim
Boundary, Changed Files, Command Evidence, Machine Closure Package, and
No-Commit Statement.

## Pre-Flight Checks

At worker start:

```powershell
$executionBaseHead = git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R91_SYSTEM_CHAIN_MAP_AND_FRESHNESS_CONTROL_WORKER_RETURN_2026-07-10.md --title "MSEA R91 System Chain Map And Freshness Control Worker Return"
```

Stop before edits on unexpected tracked/untracked state outside the dispatch
pair. An allowed-scope packet-shape failure may be repaired only inside worker
ownership; otherwise return blocked.

## Execution Plan

1. Capture executionBaseHead, status, source inventory, and negative searches.
2. Re-read R90 five lanes and current source; build deterministic map JSON.
3. Write the human README and maintenance standard without overclaiming.
4. Correct the confirmed stale/missing citations under the evidence rules.
5. Implement checker and focused tests; keep file sizes below governed limits.
6. Wire checker into exact catalogs/workflows and add weekly reminder.
7. Add GC-051 entry source and run its generator.
8. Recompute all source fingerprints after final allowed-source edits.
9. Run focused tests, checker real-repo pass, worker-return fast gate, all
   applicable governance gates, JSON/YAML parse checks, and diff hygiene.
10. Return exactly sixteen uncommitted paths with HEAD unchanged.

## Evidence Requirements

Worker return must record:

- executionBaseHead and final HEAD;
- exact sixteen-path status and name-status evidence;
- five lane IDs/verdicts in both formats;
- fingerprint count, normalization, and representative recomputation;
- all stale/missing path before/after checks;
- focused test counts;
- real-repo freshness checker result;
- local catalog and workflow wiring checks;
- weekly workflow permission/secret scan;
- GC-051 generator and checker results;
- worker-return fast gate and final diff hygiene;
- explicit no-commit statement.

## Review Gate

Reviewer must recompute at least five representative fingerprints, one path
correction from each owner document, day-30/day-31 age behavior, one missing
path fixture, one README/JSON mismatch fixture, every catalog/workflow binding,
and the exact worker changed set. Reviewer-fast must pass before acceptance.

## Acceptance Criteria

- [ ] Exactly five lane rows reconcile between README and JSON.
- [ ] B distinguishes CURRENT, PARTIAL, HISTORICAL, and FUTURE surfaces.
- [ ] No claim is stronger than reviewer-accepted R90.
- [ ] All source fingerprints exist and match after final worker edits.
- [ ] Checker passes every focused positive/negative test.
- [ ] Real repository checker result is CURRENT.
- [ ] 30-day boundary passes at day 30 and fails at day 31.
- [ ] All catalog/workflow bindings are present once, with no duplicate label.
- [ ] Weekly workflow is read-only and secret-free.
- [ ] Eleven stale citations are corrected and H2 missing status is honest.
- [ ] GC-051 source/aggregate match and cover changed map/review citations.
- [ ] Worker return passes full fast gate.
- [ ] Worker performs no commit and HEAD is unchanged.

Fail conditions:

- [ ] Any map row cites temporary material as authority.
- [ ] Any semantic verdict is auto-generated from hash/file existence alone.
- [ ] Any source drift is silently accepted or hash-updated without review.
- [ ] Any missing artifact is replaced by an unproven equivalent.
- [ ] Any protected, runtime, public, session, lifecycle, or cleanup path
      outside the exact manifest changes.
- [ ] Any workflow requests write permission or secret.

Closure is blocked if any fail condition is present.

## Closure Checklist

- [ ] Worker manifest matches exactly sixteen paths.
- [ ] All acceptance criteria resolve PASS or a blocking return.
- [ ] Reviewer recomputation matches worker evidence.
- [ ] Focused tests and real-repository freshness check pass.
- [ ] GC-051 source and generated aggregate match.
- [ ] No pending or unchecked residue remains at closure conversion.
- [ ] Material and session-sync commits remain separate.

## Return-To-Orchestrator Conditions

Return to orchestrator with `BLOCKED_WITH_REASON` if current source contradicts
an accepted R90 lane, a required insertion owner is missing, H2 equivalence is
needed to preserve a claim, a destructive/public/live action becomes necessary,
or implementation requires any path outside Write Ownership.

## Operator Checkpoint

operator.checkpoint.waiver: operator continuation already authorizes this exact
bounded implementation. A fresh checkpoint is still required for semantic
auto-repair, Web UI, public export, runtime/provider/live behavior, R72F change,
or advisory-directory relocation.

## Verification Commands

Required minimum:

```powershell
python -m json.tool docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json
python -m json.tool docs/corpus-intelligence/registry/entries/msea-r91-system-chain-map-and-freshness.json
python -m pytest governance/compat/test_check_system_chain_map_freshness.py -q
python governance/compat/check_system_chain_map_freshness.py --as-of-date 2026-07-10 --json --enforce
python governance/compat/generate_corpus_scan_registry.py --check
python governance/compat/check_corpus_scan_registry.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
git rev-parse --short HEAD
```

Worker may add targeted parser/YAML/catalog checks. Live provider proof is N/A
with reason: this tranche makes no provider or AI-governance behavior claim.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Dispatch Prompt Envelope`; `Source Verification Block`; `ADIF Defect Registry Disclosure`; `Core Guard Self-Protection Authorization`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Worker Return Packet Shape Contract`; `Agent Operation Trace Block`; `Delta Execution Claim Boundary Control Block`; `Public Export Disposition` |
| gateRunPurpose | Confirm source-backed dispatch shape after checker-source read-ahead. |
| claimBoundary | Dispatch and planned output shape only; no implementation result claimed. |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: accepted Audit A can support a useful whole
picture without erasing partial links, while source hashes and review age can
detect staleness without auto-editing meaning.

Evidence Comparison Requirement: worker compares real output, negative tests,
and wiring evidence with this prediction.

Contradiction Handling Requirement: a current-source contradiction produces a
ledger and narrowed/blocked lane, never silent override.

Claim Update Requirement: worker states whether B and freshness control are
confirmed, revised, narrowed, or blocked.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local provenance repository |
| Session or invocation | MSEA-R91 work-order dispatch, 2026-07-10 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source reads, rg, scaffold helper, ADIF resolver, apply_patch, governance gates, git |
| Target paths | paired MSEA-R91 baseline and work order |
| Allowed scope source | operator continuation and R90 next move |
| Before status evidence | clean worktree at `252fe1a3e`; `git status --short` was empty before dispatch authoring |
| After status evidence | dispatch pair pending reviewer-owned dispatch commit |
| Diff evidence | `git status --short`; `git diff --name-status` |
| Approval boundary | exact sixteen-path worker implementation after dispatch commit |
| Claim boundary | no worker implementation exists at dispatch |
| Agent type | dispatcher |
| Invocation ID | `msea-r91-work-order-dispatch-2026-07-10` |
| Expected manifest | MSEA-R91 baseline and work order |
| Actual changed set | MSEA-R91 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | planned repo-local reference and freshness control |
| claimDisposition | CLAIM_REJECTED_NO_EXECUTION: implementation pending |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no implementation receipt exists |
| actionEvidence | ACTION_EVIDENCE_PRESENT: dispatch source verification and gates |
| invocationBoundary | manual dispatch authoring |
| interceptionBoundary | no IDE, shell, filesystem, provider, CLI, MCP, or Web interception claim |
| claimLanguage | planned checker, tests, local/CI wiring, weekly reminder |
| forbiddenExpansion | semantic auto-edit, Web UI, runtime/provider/live, public, session, lifecycle, cleanup |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: no public-sync authorization exists for R91.

## Commit Prompt Readiness

Worker must not run a commit prompt or commit command. Reviewer/closer captures
closureBaseHead, compares the exact sixteen-path worker set, runs reviewer-fast
and pre-closure gates, and owns any accepted commit plus separate session sync.

## Claim Boundary

This work order authorizes a human/machine whole-picture map, deterministic
source-drift and age detection, corrected evidence paths, focused tests,
local/CI wiring, a weekly read-only reminder, and required GC-051 metadata. It
does not authorize semantic auto-repair, Web/dashboard implementation,
runtime/provider/live behavior, public export, R72F change, session mutation,
or advisory-directory relocation.
