# CVF GC-018 Baseline - RFR-R6 Cross-Owner Adversarial Re-Audit

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-24

Batch ID: RFR-R6-CROSS-OWNER-ADVERSARIAL-REAUDIT

Dispatch base head: `ad5edc2b4`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through standing dependency-ordered roadmap authority

Reviewer owner: current independent orchestrator/reviewer/closer

Worker target: one delegated audit worker role

## Purpose

Authorize the terminal RFR-R6 read-only adversarial re-audit of findings F1-F10
and the R1-R5 owner boundaries. The worker produces one pending evidence packet;
it does not repair source, close the roadmap, commit, or open external effects.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R6-CROSS-OWNER-ADVERSARIAL-REAUDIT --title "CVF RFR-R6 Cross-Owner Adversarial Re-Audit" --date 2026-08-24 --base ad5edc2b4 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "RFR-R5 independently closed bounded at 82a0073b2fca002fd7999ed70905166295946515" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with verified R6 authority, exact read/write scope, proof matrix and claim boundaries |
| checkerReadAheadConfirmation | dispatch-quality, prompt-envelope, lifecycle-hygiene, checker-read-ahead, worker-return-quality and corpus-coverage sources reviewed |
| docOnlyNewFields | none; this packet reuses existing governed dispatch fields |
| claimBoundary | provenance for dispatch authoring only; no runtime, provider, live, public, deployment or closure claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| RFR-R1 through RFR-R5 independently accepted | R1 `a67034370`; R2 `84d44889f`; R3 `a18ba512f`; R4 `8ec399aa5`; R5 `82a0073b2fca002fd7999ed70905166295946515` and continuity `ad5edc2b4` | every implementation tranche closed bounded and continuity explicitly releases fresh R6 dispatch authoring | ACCEPT |
| R6 roadmap authority | `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md`, Tranche Matrix and Closure Gates | R6 is adversarial cross-owner re-audit and bounded closure decision | ACCEPT |

## Scope

Worker write scope is exactly one path:

- `docs/reviews/CVF_RFR_R6_CROSS_OWNER_ADVERSARIAL_REAUDIT_WORKER_RETURN_2026-08-24.md`

Read scope is the runtime-finding authority, roadmap, R1-R5 baselines/work
orders/completion reviews, and the source/test/package paths those accepted
packets cite. Local deterministic tests and typechecks may execute without
editing tracked files. Generated caches, coverage, snapshots and lockfile drift
must not be retained.

## Required Finding Matrix

| Finding | R6 audit question | Required terminal disposition |
| --- | --- | --- |
| F1 | Can any BUILD mutation reach execution without accepted SPEC, valid WORK ORDER and bounded target authority? | `CLOSED`, `RETAINED_WITH_REASON`, or `BLOCKED_WITH_REASON` |
| F2-F4 | Can mandatory guards/configuration be removed, reordered, bypassed or canonically mismatched? | same terminal vocabulary |
| F5 | Can material context be omitted, forged, reordered, or leak raw secret-bearing content while receipt binding still passes? | same terminal vocabulary |
| F6-F7 | Do routing/registry and runtime policy seams create a currently proven exploitable gap, or only bounded enrichment candidates? | same terminal vocabulary |
| F8 | Can caller policy data authorize native MCP execution without canonical CVF admission? | same terminal vocabulary |
| F9 | Can declared platform/isolation evidence exceed actual executor guarantees, inherit host environment, or be forged? | same terminal vocabulary |
| F10 | Does any current cross-owner seam leave an unowned execution/receipt/authority transition? | same terminal vocabulary |

Every row must cite current source/test/review evidence. Worker assertion or
prior PASS counts alone are insufficient.

## Baseline Decision

`PROCEED_BOUNDED_AUDIT`: dependency evidence is complete and R6 may perform
the exact read/test/evidence-return scope. Any implementation repair or second
write path is outside this decision.

## Evidence / Verification

Dispatch evidence consists of the committed R1-R5 material identities, current
continuity release, source verification, collision search, ADIF resolver,
pre-dispatch autorun gate and exact three-path dispatcher manifest. Worker
closure evidence remains pending and cannot be inferred from this baseline.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R6 is terminal cross-owner re-audit | ROADMAP_AUTHORITY | `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md` | Tranche Matrix; Closure Gates; Acceptance Criteria | `R6`; F1-F10 terminal dispositions | roadmap owner | ACCEPT |
| originating findings and corrective routes are fixed | REVIEW_AUTHORITY | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | findings F1-F10; remediation sequence | F1-F10 | governed findings authority | ACCEPT |
| R1-R5 have independent bounded completion evidence | REVIEW_EVIDENCE | `docs/reviews/CVF_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_COMPLETION_2026-08-24.md` | Dependency Receipt; Test And Gate Evidence; Decision | R1-R5 chain and R5 result | latest completion owner | ACCEPT |
| current continuity releases R6 dispatch authoring only | SESSION_AUTHORITY | `CVF_SESSION/state/entries/nextAllowedMove.json` | `value` | R6 fresh source verification and dispatch | active continuity owner | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact R6 baseline/work-order/return paths | `Test-Path -LiteralPath` returned false for all three before authoring | ACCEPT |
| token collision | `rg -n "RFR-R6|RFR_R6|cross-owner adversarial|cross-owner re-audit" docs CVF_SESSION` found only roadmap, findings authority and current continuity references | ACCEPT |
| collision decision | no pre-existing R6 dispatch or worker-return artifact | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_changed_corpus_registry_coverage.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; dependency release; Worker Return Packet Shape Contract; Agent Handoff Contract Control Block |
| gateRunPurpose | confirm final dispatch shape after source verification, not discover semantic requirements |
| claimBoundary | checker conformance does not prove the R6 finding dispositions or roadmap closure |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | one delegated audit worker consuming committed repo paths | read/test plus exact-one worker-return write; no source repair or commit | this baseline and paired work order | repository-local audit only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | operator copies the committed packet | transport does not grant mutation, MCP invocation, provider or runtime authority | explicit no-commit return contract | no automatic CLI/MCP adapter or enforcement claim | `CONTRACT_ONLY` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`review`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class review --role worker --lifecycle-phase pre-execution --json`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private terminal audit dispatch; no public-sync action is authorized.

## Claim Boundary

This baseline authorizes a local read/test/review pass and one uncommitted
worker-return artifact. It authorizes no source repair, implementation, package
installation, provider/live/network call, credential access, deployment,
public sync, push, production claim, or roadmap closure by the worker.
