# CVF GC-018 Baseline - NCR Operator Cleared Review Continuation

Memory class: governed-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-15
Batch ID: CVF-NCR-REVIEW-CONTINUATION-20261015
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
Inspection base: a786cad3c8864cbed5d80d532bea0f91778ff14b

## Purpose

Deliver the finite existing Review Cost owner/checker/scaffold amendment selected by the prior documentary ruling. Consumer is Local dispatch/review for operator-cleared same-scope rework. Preserve default machine stops, strict evidence joins and honest completion tokens; do not create another checker or change the HTML root.

## Authority / Scope

Operator2026-10-15 granted full authority after Local's explicit six-file proposal and directed no repeated micro-confirmation. That grant supersedes the prior pending maintenance-scope checkpoint at roadmap Admission Owner Ruling and docs/reviews/evidence/ncr-html-root-admission-v2-local-20261015.json ownerReconciliation; it covers this six-file amendment, tests, ordinary dependent corrections, review and local commits. Exact implementation paths below plus new return/proof are worker-owned; Local owns packet/closure/continuity. Manual delivery preference is metadata, not a model requirement or permission to invoke a worker.

Current HTML profiles remain consumed; no HTML/provider/product/native/browser/container/config/store/public/deploy execution is part of this maintenance task. Grant source parsing proves declarations only, not operator consent, actual effect control or runtime governance behavior. A future HTML proposal still needs all applicable admission/effect prerequisites without counter resets.

## Locked Continuation Contract

SPEC version NCR_REVIEW_CONTINUATION_V1. Names below are DOC_ONLY_NEW planned implementation, not current source capabilities. The current machine rejection is retained as historical evidence; implementation acceptance is pending.

1. Add an optional operator-cleared route to the existing Review Cost checker and convergence scaffold. Default absence preserves all old diagnostics and stop behavior. Share one strict declaration validator in the existing review_convergence_scaffold.py, consumed by the checker and scaffold; no new checker/helper module, hook, global waiver or general refactor. Internal helper names/algorithm remain worker choices.
2. Work-order opt-in fields are exactly operatorContinuationEvidencePath and operatorContinuationEvidenceSha256, plus exactly one continuation-scope-json fenced object. All absent means legacy mode; any partial/duplicate/malformed declaration fails closed, even below round3 or on INITIAL. The route is only REWORK at round>=2, with honest reviewRoundCount==reworkGeneration and all other original convergence controls. Do not treat numeric zero/false/null/empty as absent. Optional new ScaffoldArgs fields default to None, preserving existing programmatic callers.
3. Grant source is one existing UTF-8 Markdown artifact directly/under docs/baselines/ or docs/reviews/, outside archive, with normalized repo-relative forward-slash path, no absolute/drive/dot/traversal/escape/symlink path, and matching lowercase raw SHA256. Repository root is supplied by the trusted checker context; the scaffold CLI uses its current working directory as repository root, allowing an absolute production script to run against an isolated fixture cwd without new flags or module copies. Final checker calls use its explicit current repository root; tests may inject that trusted root, never packet-controlled root/clock data. Bound reads are at most65536bytes; a limit violation, decode/read/JSON error rejects. Reject self-reference to the work order or its writable artifacts. No recursive grants or transitive fallback search. Scope/authorization files remain read-only to the worker being admitted.
4. Grant source contains exactly one operator-continuation-authorization-json fenced JSON object, with duplicate object members rejected at every depth. Exact top keys: schemaVersion, decisionOwner, operatorInstructionEvidence, status, expiresAtUtc, validityDisposition, binding, scope. schemaVersion=cvf.reviewDispatchContinuationAuthorization@1.0.0; decisionOwner=OPERATOR; status=ACTIVE; operatorInstructionEvidence is a concrete non-placeholder instruction reference/reason, minimum24characters. Unknown/missing keys or nested authorization/reference substitutes reject. This validates a declaration, not the authenticity of consent; Local must verify the real operator instruction before issuing the source artifact.
5. validityDisposition is UNTIL_UTC_EXPIRY with a valid timezone-aware UTC expiresAtUtc string strictly later than actual UTC now, or UNTIL_REVOKED_OR_SCOPE_CHANGE with expiresAtUtc=null. Every other combination rejects. No CLI/packet clock override. Tests may control the trusted test clock or use explicit future/expired dates. Revocation/status or source-byte changes invalidate old references. Scope continuity does not create a numerical allowance.
6. binding has exactly parentAssignmentId, rootCauseClusterId, reviewRoundCount, reworkGeneration, priorFindingSetDigest, dispatchSurface, commitMode. They must equal the actual target's single unambiguous corresponding scalar fields (Commit mode for commitMode); strict JSON int, not bool/float/string, for the two round fields, stable non-placeholder strings otherwise, lowercase64 digest. Require WORKER_MUST_NOT_COMMIT. dispatchSurface is the current INTERNAL_AGENT or EXTERNAL_AGENT_CLI_MCP value. A mismatch/duplicate target binding rejects; no title/problem-key/round reset.
7. scope has exactly objectiveId, acceptanceItems, allowedArtifacts, riskCeiling, effectCeilings, numericalCeilings, commitOwner. objectiveId is non-placeholder; acceptanceItems is a nonempty unique list of nonempty IDs; allowedArtifacts is a nonempty unique safe repo-path list; riskCeiling=SAME_AS_AUTHORIZED_PARENT; commitOwner=reviewer-closer. effectCeilings has exactly providerCalls, networkCalls, publicWrites, deployments, realDataMutations, destructiveActions, productRuntimeStarts with strict nonnegative integer values. numericalCeilings is a nonempty string-keyed map of strict nonnegative integer caps with positive workerMinutes and reviewerMinutes; externalInvocationCeiling, when present, must equal the existing target scalar and is required for EXTERNAL_AGENT_CLI_MCP. No null/unbounded cap, bool-as-int, duplicate/unsafe artifacts or mutable authorization path in the artifact list.
8. The target continuation-scope-json must be structurally/type-identical to grant.scope. Its allowedArtifacts must exactly equal the canonical work-order acceptance-ledger expected-artifact union, including return/proof; require a valid ledger through the existing acceptance-ledger validator. The machine checks declared scope/bindings, not arbitrary prose semantics or actual effects; Local verifies objective/AC/risk/effect/role/commit-owner semantics. Other admission, SCEC, protected-path, source, role and quota gates remain controlling.
9. A valid cleared route bypasses only the current round>=3 automatic-dispatch rejection and round>=2 missing-independent-critical-evidence rejection. Preserve all other checks, including exact digest/generation, dependency audit, full finding sweep, regression guard, no successor, autonomy, review routing and external usage/cumulative ceiling. NONE remains the truthful critical-evidence value for dependent repairs. A present invalid grant cannot fall back to ordinary automatic mode. No independently-critical finding is inferred from clearance or the six HTML findings.
10. Scaffold CLI adds --operator-continuation-evidence-path and --operator-continuation-evidence-sha256, threads them through kwargs/ScaffoldArgs, shares source/binding validation and emits those scalar fields plus exact grant.scope block. Record both flags in reproducible provenance. CLI validation occurs before the dispatcher fills the final acceptance ledger, so it validates source and argument bindings only; generated output stays a skeleton, never final dispatch admission. The completed final work-order checker must perform the full scope/ledger join. Invalid source/arguments exit nonzero before producing a candidate. Legacy generation and existing no-clearance rejection stay unchanged.
11. Completion review has an optional pair continuationWorkOrderPath/continuationWorkOrderSha256. Both absent preserves current completion rules. If either is supplied, require one of each, safe existing docs/work_orders Markdown, exact raw hash, no self/cycle, and a valid current referenced cleared work order. Require the completion reviewRoundCount to equal that work order's actual round. Reuse the real work-order diagnostic and strict grant validator, not a second acceptance oracle. At a valid cleared boundary, existing COMPLETE_REVIEW or CONSOLIDATE_SINGLE_REPAIR is permitted at round>=3 (and dependent-only consolidate at round2); this is a declaration disposition, not technical acceptance. No new stop token. CONTINUE_NEW_CRITICAL_EVIDENCE still always requires newRootCauseCountThisRound>0. Missing/invalid references retain the existing round/root restrictions plus an invalid-binding diagnostic.
12. Same-scope operator authority persists: Local may refresh a derived grant/bound packet for later consolidated dependent details under the original continuing instruction, after verifying unchanged objective, path/artifact classes, risk/effects and commit owner. Bind each actual round/digest honestly; do not demand a new user yes merely because those dependent details were consolidated. Scope/effect changes, revocation and exhausted explicit caps still stop the affected action. No grant may refill the retired HTML profiles or turn this maintenance acceptance into native/browser/provider permission.


## Write Ownership / Limits

- docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md
- governance/compat/check_review_cost_control.py
- governance/compat/review_convergence_scaffold.py
- governance/compat/build_dispatch_packet_scaffold.py
- governance/compat/test_check_review_cost_control.py
- governance/compat/test_build_dispatch_packet_scaffold.py
- docs/reviews/CVF_NCR_REVIEW_CONTINUATION_WORKER_RETURN_2026-10-15.md
- docs/reviews/evidence/ncr-review-continuation-worker-20261015.json

Final limits: owner reference1100lines/100000bytes; Review Cost checker950/64000; convergence helper600/64000; packet helper850/80000; checker tests1000/100000; packet tests1160/120000; worker return450/64000; JSON proof120000bytes. Canonical stricter limits prevail. Current source counts and original per-file LF/CRLF are in ignored source-facts.json and bound source hashes; preserve each convention. No minification, threshold exception or new helper. Shared pure validation belongs in the existing convergence helper to reserve checker/packet space. Measured room makes a split unnecessary; real conflicts route to Local before an extra path.

## Acceptance / Required Evidence

| Requirement | Observable outcome |
|---|---|
| REQ-01 | Owner documents exact closed-shape cleared route, default stops, completion vocabulary and same-scope authority continuity. |
| REQ-02 | Strict grant/path/hash/schema/duplicate/type/expiry/scope validation, bounded reads and hostile source rejection. |
| REQ-03 | Actual work-order binding/ledger union and exactly two conditional dispatch exceptions, with every unrelated control preserved. |
| REQ-04 | Real CLI->kwargs->ScaffoldArgs->scope emission/provenance->final checker route; default callers unchanged. |
| REQ-05 | Completion links real cleared work order by raw hash; controlled existing stop tokens; no false independent root or invalid-link waiver. |
| REQ-06 | Focused positive/default/hostile production-route tests, actual CLI and read-only provenance regression; compile five Python files. |
| REQ-07 | Exact6 existing changes plus return/proof; size/encoding and source-history preservation; no effects, new checker or scope escape. |
| REQ-08 | Mandatory mapped reads before first edit/test, actual preparation order, full truthful return/learning/acceptance proof and pending independent Local probe. |

Required hostile classes: absent/one-sided/duplicate opt-in; INITIAL or wrong binding; source missing/hash/byte/encoding/JSON/duplicate-key/unknown-schema/status/expiry failures; path traversal/absolute/drive/symlink/self/recursive forms; bool/int/float/string substitutions; scope/ledger extra/missing/duplicate artifacts; unsafe source-writable artifact; wrong root/digest/round/generation/surface/commit mode; invalid completion work-order pin/round/cycle; reached/unknown external usage; zero-root CONTINUE_NEW_CRITICAL_EVIDENCE. Exact valid cleared round3 with NONE and matching source/scope/ledger must pass the actual completed work-order checker; linked completion must pass only its conditional vocabulary route. Tests may use synthetic declarations in owned local fixtures, never live consent or effects.

The real CLI's early source/binding check and the completed checker/ledger join are different phases; final tests must exercise both. Old no-clearance behavior and existing tests remain. Local independent probe is PENDING_REVIEWER_EXECUTION, not fulfilled by worker suites. Full return contract in paired order; blocked mandatory preparation cannot become COMPLETE_PENDING_REVIEW.

## Source / Predecessor Evidence

Prior ruling docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md Admission Owner Ruling and docs/reviews/evidence/ncr-html-root-admission-v2-local-20261015.json ownerReconciliation at3064e1d8030c4942d7bd8db7212907a9e0fbd9e6; continuity a786cad3c8864cbed5d80d532bea0f91778ff14b. The held HTML baseline/snapshot are historical read-only inputs, not authority for this code change. Raw source rows in companion docs/reviews/evidence/ncr-review-continuation-dispatch-20261015.json bind all six actual existing files and current locked baseline. No new clearance grant is issued for HTML by this dispatch; only future isolated test fixtures exercise the schema.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: the six existing Review Cost owner/checker/scaffold/test paths specified by this packet, plus worker return/proof. Local owns packet/review/closure and exact6 continuity. No new checker or hook.
Protected paths:
- governance/compat/check_review_cost_control.py
- governance/compat/review_convergence_scaffold.py
- governance/compat/build_dispatch_packet_scaffold.py
- governance/compat/test_check_review_cost_control.py
- governance/compat/test_build_dispatch_packet_scaffold.py
Operator authorization: on2026-10-15, following the explicit six-file scope proposal, the operator granted full authority to proceed and directed Local not to wait for repeated confirmations. This supersedes the pending maintenance-scope checkpoint, and authorizes the named existing-owner implementation, tests, same-scope corrections, Local review and local commits. Manual worker transfer remains the operator's chosen delivery method. Routine in-scope implementation and packet repair must not reopen approval questions.
Rollback boundary: only this six-file amendment and new pending return/proof; preserve original HTML root identity/counters/freeze, failed evidence, spent profiles, four P4 blocked rows/C15 exclusions and unrelated work. Worker copies this exact five-protected-path authorization into its pending return so the changed set carries authorization. Local may fix dependent packet defects under this same grant; a worker cannot self-expand the manifest or create a successor.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id CVF-NCR-REVIEW-CONTINUATION-20261015 --title "NCR Operator Cleared Review Continuation" --date 2026-10-15 --base a786cad3c8864cbed5d80d532bea0f91778ff14b --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key ncr-review-dispatch-operator-cleared-continuation --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path; INTERNAL_AGENT INITIAL; WORKER_MUST_NOT_COMMIT |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: actual generated convergence/SCEC retained; existing full-packet control shape adapted; locked continuation SPEC, exact8 manifest/ledger, source mapping and budgets authored by Local |
| checkerReadAheadConfirmation | targeted operative ownership/round/parser/size/format/dispatch predicates read before tracked edits |
| docOnlyNewFields | continuationSpecVersion; operatorContinuationEvidencePath; operatorContinuationEvidenceSha256; continuationWorkOrderPath; continuationWorkOrderSha256 |
| claimBoundary | actual helper exit0/raw SHA retained in ignored custody; no implementation or execution-admission result inferred |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, maxResults=`40`
Resolver command: `python -B governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 40 --json`
Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006
Actual result:27 candidates/27 returned, not truncated. Resolver metadata and applicable ownership/source/size/format controls read; no every-entry-body claim. ADIF-0026 operative same-scope owner and mandatory-stop sections also read directly. Apply existing worker-preparation reminder; no new reminder checker. Worker resolves its own role/phase before first edit.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_core.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_artifacts.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_independent_review_probe_admission.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_review_cost_control.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_governed_file_size.py; governance/compat/check_python_automation_size.py; governance/compat/check_external_knowledge_intake_routing.py |
| literalTokensReviewed | exact source columns and DOC_ONLY_NEW; INITIAL sentinel for this distinct amendment; eight-row acceptance ledger and exact8 union; five-path Core authorization;12-gate graph; optional clearance and completion source join; full return profile; line/byte and near-hard budgets; Internal source intake row |
| gateRunPurpose | confirmation/evidence after targeted operative owner/parser/source/graph/trace/size predicate reads; not first discovery or runtime proof |
| claimBoundary | targeted current predicates; no every-checker-body/read-comprehension or historical preparation correction claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition | Source fact type |
|---|---|---|---|---|---|---|---|
| Current work-order round predicates | EXISTS | governance/compat/check_review_cost_control.py | diagnose_work_order definition | diagnose_work_order | current Review Cost dispatch | ACCEPT | EXISTS |
| Current completion stop predicates | EXISTS | governance/compat/check_review_cost_control.py | diagnose definition | diagnose | current Review Cost completion | ACCEPT | EXISTS |
| CLI convergence stop | EXISTS | governance/compat/review_convergence_scaffold.py | validate definition | validate | current convergence helper | ACCEPT | EXISTS |
| Argument and output plumbing | EXISTS | governance/compat/build_dispatch_packet_scaffold.py | ScaffoldArgs definition | ScaffoldArgs | current packet data model | ACCEPT | EXISTS |
| Current default rejection tests | EXISTS | governance/compat/test_check_review_cost_control.py | test_round_three_is_not_automatic_dispatch_eligible definition | test_round_three_is_not_automatic_dispatch_eligible | current tests | ACCEPT | EXISTS |
| Current rework generator fixture | EXISTS | governance/compat/test_build_dispatch_packet_scaffold.py | _base_args definition | _base_args | current tests | ACCEPT | EXISTS |
| Same-scope authority owner | EXISTS | docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md | Same-Scope Authority Continuity And Micro-Checkpoint Prevention | docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md | current canonical owner | ACCEPT | EXISTS |

New Doc-Only Fields:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| continuationSpecVersion | locked contract identity | Yes | Yes | NCR_REVIEW_CONTINUATION_V1 |
| operatorContinuationEvidencePath | proposed work-order opt-in | Yes | Yes | strict source/binding/ledger checks |
| operatorContinuationEvidenceSha256 | proposed raw source pin | Yes | Yes | lowercase exact SHA256 |
| continuationWorkOrderPath | proposed completion reference | Yes | Yes | valid cleared current work order |
| continuationWorkOrderSha256 | proposed completion raw pin | Yes | Yes | exact current bytes |

## Evidence / Verification

The first commit hook additionally required explicit non-intake blocks because the negative scope sentence contained its intake trigger phrase. Those predicates were read after that failure; the failure remains in material-commit.log and preparation stays PARTIAL_WITH_REASON.

Current declared-state CLI, source-pin and shape receipts are in ignored invocation custody. No implementation suite or worker probe was run. Initial declared-state preflight rejected a companion key, baseline verification heading, intake risk wording and a multi-path Internal source cell. These defects were consolidated after reading their exact predicates; preparation is PARTIAL_WITH_REASON, not retroactive full read-ahead. Original invalid CLI receipt and reviewer-preflight.log remain in ignored custody. The optional roadmap edit also triggered committed-target dirty-frontier protection, so it is deferred to accepted implementation review; the original roadmap bytes remain unchanged. New operator authority is carried by this baseline and current continuity, not by altering old ruling history.

## Decision / Evidence

Local locks this admitted scope/design for worker implementation after material/continuity/bound pre-dispatch PASS. This is a newly authorized Review Cost owner problem, INITIAL only for that independent maintenance scope, not a relabeled HTML repair. Implementation, full gate and distinct Local probe remain pending. Actual entry/scaffold/ADIF/source and declared-state receipts live in ignored invocation custody; no historical failure is rewritten.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md |
| Chain map route | operator instruction -> Local locked packet -> internal worker -> Local technical disposition |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | existing Review Cost owner and NCR roadmap |
| Disposition | no external repository absorption or remote research; manual transfer is delivery only |
| Claim boundary | shared-workspace worker is INTERNAL_AGENT regardless of provider/model |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON - named internal Review Cost owner maintenance only; no source acquisition or absorption work.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - six named internal source files and bounded predicate verification; no file-enumeration coverage claim.

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON - existing internal owner/checker/scaffold/test amendment; no new external source intake.

The next hook rejected the bare N/A corpus disposition because it lacked the literal Corpus verdict label; corrected after reading that operative predicate, preserving material-commit-terminal.log and PARTIAL preparation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private existing-owner maintenance; no public artifact/catalog/export claim.

## Claim Boundary

Maintenance dispatch only; implementation and distinct Local probe pending. No new checker/hook, runtime governance efficacy, tool interception or HTML/native/provider/effect release. HTML root ordinal2/counters2,0,2,0/two blockers/freeze, historical PARTIAL/failed bytes and four P4 rows/C15 exclusions stay unchanged. R1/R2partial,R3/R4open,R5/R6deferred; data/custody/business/send/B2/P11/public/deploy parked, LHW24 retained.
