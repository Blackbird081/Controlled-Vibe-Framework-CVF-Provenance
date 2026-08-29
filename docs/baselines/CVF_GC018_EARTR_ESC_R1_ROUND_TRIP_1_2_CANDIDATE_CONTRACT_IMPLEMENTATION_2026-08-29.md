# CVF GC-018 Baseline - EARTR-ESC-R1 Round-Trip 1.2 Candidate Contract Implementation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EARTR-ESC-R1

Date: 2026-08-29

Dispatch base head: `590cf8ab71805abb947a2c49b8dcc33335aadc1e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Worker: delegated Claude implementation worker

Orchestrator/reviewer/closer: Codex

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one bounded implementation tranche for the accepted enrichment of
`cvf.external-agent-round-trip` from 1.1.0 to candidate-aware 1.2.0 semantics.
The tranche modifies exactly four existing owner paths and creates one
evidence-only worker return. It does not release, publish, or distribute 1.2.0.

## Operator Authorization And Review Closure

The operator instructed the orchestrator/reviewer to proceed on 2026-08-29
after external closure confirmation returned `ACCEPT`. The reviewed design is
content-pinned at SHA-256
`ff3ca9815a52bcd2383f7da3f063fade6f53c02fc0d2da94972925c6c13c06c1`.
The exact closure handback is preserved under the archive path in Source
Verification with SHA-256
`b3b734d1ccd36a4c5dd22912bbfc0a9516a23e64b60ae1c7c8f6aca3b0dbbdda`.

The worker leaves every change unstaged and uncommitted. Codex independently
reviews, probes, repairs only within the accepted boundary, and controls any
later commit or representation refresh.

## Baseline Decision / Proposed Tranche

| Field | Decision |
| --- | --- |
| Candidate | EARTR-ESC-R1 typed two-lane absorption-candidate and receipt-binding implementation |
| Value gate | PASS: serious provenance-contamination and legacy-validator ambiguity; source-backed by current validator and externally reviewed design; non-duplicate; bounded four-owner delta exceeds local implementation cost |
| Protocol disposition | ENRICH_EXISTING `cvf.external-agent-round-trip`; target minor version 1.2.0 |
| Owner disposition | Modify the current finding workflow, representation contract, validator, and focused tests only |
| Cost boundary | Four material paths plus one worker return; local deterministic tests; zero provider/network quota |
| Release boundary | Public and portable refresh remain reviewer/operator-controlled and cannot be claimed until separately completed |

## Acceptance Criteria

1. External candidates use mutually exclusive source-value and internal-defect
   variants with conditional and forbidden fields.
2. Candidate IDs are return-local and Local reconciliation binds the exact
   manifest, PASS receipt, protocol version, and candidate-contract version.
3. Legacy 1.1 returns remain readable but legacy non-empty candidates cannot be
   silently promoted into typed reconciliation.
4. Candidate contract v1 fails closed on malformed variants, broken source
   references, source-set drift, mixed lanes, invalid enums, and authority
   widening.
5. Validation receipts bind the exact manifest and the candidate-aware
   semantics actually enforced.
6. All focused packet tests pass and the worker returns exactly the authorized
   five-path changed set with empty staging.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| existing protocol owner and same-release rule | governed contract fact | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` | Scope / Owner Boundary; Protocol Identity; Update Rule | `cvf.external-agent-round-trip`; current version `1.1.0` | protocol representation contract | ACCEPT |
| current candidate collection is untyped | current source fact | `scripts/external_agent_packet.py` | `validate_return` | `suggestedAbsorptionCandidates` is not validated | return validator | ACCEPT |
| current receipt lacks exact-manifest/candidate-contract binding | current source fact | `scripts/external_agent_packet.py` | receipt construction | `validate_return` | return validator | ACCEPT |
| current focused fixture already has stable source IDs | current test fact | `scripts/test_external_agent_packet.py` | `_make_return` | `sources[0].id` | focused test owner | ACCEPT |
| final design closure | operator-supplied external review evidence | `docs/reviews/archive/external_agent_handbacks/eartr_esc_r0_2026-08-29/CVF_EARTR_ESC_R0_RB01_CLOSURE_CONFIRMATION_2026-08-29.md.preserved` | Verdict; Remaining Blocking Findings | `ACCEPT`; `NONE` | preserved non-authoritative handback plus operator disposition | ACCEPT |

## Provenance Path Normalization

The accepted design, three external handbacks, and two completed review prompts were moved
byte-for-byte as `.md.preserved` provenance blobs under
`docs/reviews/archive/external_agent_handbacks/eartr_esc_r0_2026-08-29/` before
dispatch. This avoids rewriting externally produced evidence merely to satisfy
active Markdown structural/encoding rules. Recorded SHA-256 values remain unchanged.
The archive holds the exact reviewed bytes and externally accepted hashes; the
paired baseline and Work Order are the active operator-authorized dispatch
surfaces.

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EARTR_ESC_R1 --title "EARTR-ESC-R1 Round-Trip 1.2 Candidate Contract Implementation" --date 2026-08-29 --base 590cf8ab71805abb947a2c49b8dcc33335aadc1e --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added exact accepted design pins, four-owner contract, dual-reader/receipt-binding cases, archive provenance normalization, and five-path worker fulfillment manifest. |
| checkerReadAheadConfirmation | Work-order template, dispatch envelope, tranche choreography, guard orientation, and literal-format gotchas were read. |
| docOnlyNewFields | N/A with reason: this baseline introduces no runtime field. |
| claimBoundary | Dispatch-authoring provenance only. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "work-order-authoring" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector docs --risk-ceiling MEDIUM --json`.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `providerExecutionAuthority: FORBIDDEN`; `Dispatch Prompt Envelope`; `Required Artifact Manifest`; trace table field labels |
| gateRunPurpose | Confirm dispatch shape and source pins before worker execution. |
| claimBoundary | Read-ahead is preparation evidence, not implementation proof. |

## Verification Evidence

Pre-change focused tests passed `58 passed` on 2026-08-29. The work order must
also pass its dispatch and capsule gates before delivery. Worker and reviewer
proof must be recomputed after implementation and cannot be substituted by
this baseline evidence.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | externally proposed collaboration model -> Local owner/design reconciliation -> adversarial review/closure -> operator-authorized existing-owner implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` |
| Disposition | ADAPT existing external-agent round-trip owners |
| Claim boundary | dispatch routing only; no source absorption, public release, runtime, provider, or production claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex orchestrator/dispatcher/reviewer |
| Provider or surface | local private-provenance repository |
| Session or invocation | EARTR-ESC-R1 dispatch authoring, 2026-08-29 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | governed reads, `rg`, Git, ADIF resolver, scaffold inspection, focused pytest, `apply_patch` |
| Target paths | this baseline, paired work order, paired task capsule, accepted design/review evidence |
| Allowed scope source | operator instruction to proceed after final external `ACCEPT` closure |
| Before status evidence | accepted design and external handbacks were untracked at base `590cf8ab71805abb947a2c49b8dcc33335aadc1e` |
| After status evidence | dispatch-authority packet plus provenance-preserved design/review evidence; implementation absent |
| Diff evidence | exact dispatch-author manifest before commit |
| Approval boundary | EARTR-ESC-R1 dispatch only; worker implementation remains no-commit and public/portable release remains closed |
| Claim boundary | no implementation, provider, public, push, deployment, or production claim |
| Agent type | orchestrator/dispatcher/reviewer |
| Invocation ID | `eartr-esc-r1-dispatch-2026-08-29` |
| Expected manifest | accepted design; five archived review/prompt artifacts; this baseline; paired work order; paired capsule |
| Actual changed set | accepted design; five archived review/prompt artifacts; this baseline; paired work order; paired capsule |
| Manifest delta | MATCH |
| Deletion or rename disposition | external handbacks/prompts moved byte-for-byte into archive; no content deletion |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This baseline authorizes only one private, local, no-commit implementation
tranche. It does not release protocol 1.2.0, refresh `EXTERNAL_AGENT_READ`,
sync or push the public repository, call providers, deploy, or claim runtime,
security, production, or universal workflow behavior.
