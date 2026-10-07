# CVF GC-018 - NCR Next-Move Alignment
Memory class: governed-dispatch-baseline
Status: DISPATCH_READY
docType: baseline
Date: 2026-10-07
Batch ID: CVF-NCR-NEXT-MOVE-ALIGNMENT-EXECUTION-20261007
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false

## Purpose

Authorize the complete bounded repair packet for NCR next-move textual consistency,
including owner headroom, legacy compatibility and existing acceptance-ledger
proof. Protected edits are limited to the named four code/test paths after committed release.

## Scope / Target / Owner Boundary

Local dispatcher owns release; Local worker owns bounded implementation;
operator-relayed Local reviewer owns independent probe. NIS-T1J stays closed.
This separately admitted maintenance packet becomes current execution authority
only through committed pins, continuity and the bound release gate.

## Decision / Baseline / Proposed Tranche

LOCAL_SCOPE_ACCEPTED_RELEASE_GATE_REQUIRED. The work order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md owns the proposed exact
six-path implementation scope. One package covers drift rejection, compatibility,
size headroom and proof; no per-case tranche or new checker/schema/hook binding.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| NCR declaration has no recognized legacy signature; helper returns no violation | governance/compat/check_active_session_state.py | next-move helpers | _check_next_allowed_move_alignment | active continuity | ACCEPT |
| Existing full-classifier fixtures cover legacy front-door/handoff drift | governance/compat/test_check_active_session_state.py | primary-token cases | ActiveSessionStateTests | checker regression | ACCEPT |
| Dispatcher/Git/proof joins already owned | docs/reference/work_order_template/CVF_WORK_ORDER_ACCEPTANCE_LEDGER_ADDENDUM.md | Oracle And Reducer Rules | N/A | return admission | ACCEPT |
| Outcome design selects reuse; parser candidate remains unimplemented | docs/reviews/learnings/CVF_OUTCOME_BOUND_CONTINUATION_LEARNING_2026-10-07.md | Existing-Owner Design Disposition | N/A | Local design | ACCEPT |

Exact source Git-byte pins at 35c7f8f1cf054f6d23f0cffd22c9a2103fe0cd1e:
- `governance/compat/check_active_session_state.py` SHA256 `5b8a085f847622d6d772e66be74e31bed4472e3d42d9f2d815c24d65e7c1eca5`.
- `governance/compat/test_check_active_session_state.py` SHA256 `cb6d2ee61a57a71b7561620be0f0f1d84d21593ff8c01648a626837c18955b6f`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006
Full query used --max-results 100: totalCandidates=27;truncated=false. All returned
IDs disclosed; no claim that this proves understanding. Applicable precautions:
source/authority fidelity, read-ahead, protected-scope admission, transitive
continuity pins, execution-base freshness, closeability, authoring-vs-release,
acceptance join, output-root anchoring and valid command signatures. No corpus
claim, provider memory authority, detached launch or live/runtime execution.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_active_session_state.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_dispatch_release_readiness.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py |
| literalTokensReviewed | DRAFT; WORKER_MUST_NOT_COMMIT; acceptance-ledger-json; requirementId; requiredProofIds; exact graph fields; Source Verification; trace labels |
| gateRunPurpose | confirm admitted packet before committed release |
| claimBoundary | admitted packet structure only; corrected behavior and independent proof not yet supplied |

## Negative Search And Collision Discipline

`rg -n 'CVF-NCR-NEXT-MOVE-ALIGNMENT|NCR_NEXT_MOVE_ALIGNMENT' docs CVF_SESSION`
returned no governed matches before authoring. Exact baseline/order/new helper,
new test and proof output paths did not exist; checker/test owners exist.
Collision decision: reuse the existing owners, two budget-driven helper paths;
no second checker, schema or registry. Scope is named paths, not a corpus inventory.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id CVF-NCR-NEXT-MOVE-ALIGNMENT --title "NCR Next-Move Alignment" --date 2026-10-07 --base 35c7f8f1cf054f6d23f0cffd22c9a2103fe0cd1e --commit-mode WORKER_MUST_NOT_COMMIT --no-evidence-readiness-applicable --stdout |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | resolve scope/spec/source/ADIF; keep DRAFT; add exact ledger and closeability graph; retain generated convergence block |
| checkerReadAheadConfirmation | governance/compat/check_active_session_state.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_dispatch_release_readiness.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py |
| docOnlyNewFields | NONE; existing contract fields reused |
| claimBoundary | packet preparation only |
## Implementation Contract

The current-format branch applies only when the primary state declaration is
PROGRAM_ID=CVF-NCR, with optional Next allowed move: prefix. Recognize it before
searching incidental legacy-family tokens in its narrative. Require exactly one
nonempty PROGRAM_ID, NEXT_ACTION_CLASS and BATCH_ID in that order, separated
by semicolons and followed by the header-ending period. Values use uppercase
letters,digits,underscore or hyphen and start with a letter. Extra/duplicate
header assignments and missing/malformed required assignments fail closed in
this NCR branch. Spaces around assignments/delimiters are formatting only.

Compare the full NCR declaration, including guidance after the header, across
state, the front door Next Allowed Move section and the active handoff section.
Use the single physical declaration line, with optional matching outer Markdown
backticks/prefix and surrounding whitespace removed; collapse internal whitespace
runs in guidance for comparison; compare canonical header values independently
of spacing around assignments/delimiters. Preserve case and punctuation in
values/guidance. State NCR declaration must also be a single physical line. Same IDs
with changed authority/stop guidance must reject. Missing, duplicate, malformed,
wrong-program or different declaration on either Markdown surface must reject.
Do not consume adjacent historical prose/Mode lines or scan the whole document
for an incidental PROGRAM_ID. Multiple declaration lines fail even if identical.
Multiline state strings and incomplete physical-line headers must reject.
Unmarked prose on subsequent Markdown lines is outside the declaration: do not
claim to detect arbitrary prose wrapping while also ignoring historical prose. Existing generated declarations are one
physical line. This is textual consistency, not semantic authority validation.

State declarations outside this NCR format retain legacy token behavior and the
existing unknown-family disposition. Existing _next_allowed_move_signature and
_check_next_allowed_move_alignment entrypoints remain callable; current callers,
classify/report/CLI behavior, budget and authority checks remain unchanged.
No generalized new grammar, generator/state-schema change or case-insensitive
full prose matching. Changes cannot enable work or equate aligned text with an
agent understanding it.

Move the bounded next-move comparison responsibility to the new named helper
through the current entrypoint. Move the related test group to its named test
owner without dropping legacy full-classifier drift coverage. Choose ordinary
implementation details within these contracts; no duplication of a whole test
fixture class, inherited duplicate test suite or broad helper extraction.

## Required Proof Cases

NCR-01: current synchronized single-line declarations pass, also with harmless
spacing/prefix/outer-backtick differences. NCR-02: front-door-only and
handoff-only guidance drift fail, even with identical header IDs. NCR-03: missing,
duplicate, empty or wrong-program declarations fail; malformed state NCR header
fails rather than skipping. NCR-04: incidental legacy tokens and historical
prose cannot mask the primary NCR comparison. NCR-05: existing DIR-T cases and
other legacy families retain their prior primary-token behavior; old unknown
non-NCR families keep prior disposition. NCR-06: current classifier reaches the
new comparison through its real entrypoint with disposable fixtures; whole
authority/budget regression suite passes. NCR-07: file budgets and direct CLI
imports pass after extraction; no release/provider behavior is asserted.

Capture discriminating pre-repair negatives against unchanged checker code
before product edits, then green controls and named regression results. Store
commands/exits, failing assertions, old/final source hashes and exact changed
paths in the evidence JSON. Separate fixture/helper observations from the
full-classifier cases. Do not call real providers or read/modify a live ledger.

## Near-Threshold Owner Maintainability Plan

| Owner | Current count | Hard threshold | Extraction/split target | New helper path | Minimum shrink target | Post-change limit |
|---|---|---|---|---|---|---|
| governance/compat/check_active_session_state.py | 951 | 1000 | next-move comparison responsibility | governance/compat/active_session_next_move_alignment.py | 50 lines | <=901 |
| governance/compat/test_check_active_session_state.py | 1172 | 1200 | related alignment tests, preserving full-classifier oracles | governance/compat/test_active_session_next_move_alignment.py | 50 lines | <=1122 |

Minimum shrink target: 50 lines per existing owner; measured from committed
source pins, not achieved by deleting oracles or bulk whitespace compaction.
New files remain below their applicable GC-023 hard limits. Entrypoints are
writable, not forbidden. Count command: Python len(Path(path).read_text().splitlines())
for the four named code/test paths. All extraction writes are worker-owned.

## Current Runtime Freshness Verification

Named helper/test source read at the pinned revision; earlier isolated NCR skip
observation retained in the shared learning. No corrected checker exists yet.
No new runtime/provider or whole-gate enforcement proof is asserted.

## Claim Boundary

Implementation contract is reviewable, not activated. Provider, pilot, actual
data, public/deploy and stopped send/B2 lanes remain outside this packet.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/reviews/learnings/CVF_OUTCOME_BOUND_CONTINUATION_LEARNING_2026-10-07.md |
| Chain map route | Local existing-owner control repair planning |
| Matching local-view guard | N/A with reason: internal sources only |
| Owner surface | governance/compat/check_active_session_state.py |
| Disposition | Local scope admitted; committed release gate required |
| Claim boundary | no external repository absorption or public absence claim |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON - internal packet preparation only.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON - no absorption corpus processed.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named checker/test and proof packet only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY - private maintenance packet.
## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher/reviewer |
| Provider or surface | private repository tools, no delegation/provider call |
| Session or invocation | ncr-next-move-alignment-packet-20261007 |
| Working directory | repository root |
| Command or tool surface | source/pin review, admitted contract revision, exact-path staging and commit helper |
| Target paths | `docs/baselines/CVF_GC018_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md` |
| Allowed scope source | operator continuation and explicit Local reviewer relay selection on 2026-10-07 |
| Before status evidence | clean worktree at e1a39623d2da54c0a5523bbec0d3574ff8d06b1e before Local disposition |
| After status evidence | exact two admitted packet paths; implementation not started |
| Diff evidence | Git diff of the two packet artifacts; unchanged source pins; active-state validators |
| Approval boundary | admitted six-path implementation; committed release required before execution; final independent review pending |
| Claim boundary | no implementation/dispatch/provider or runtime control proof |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-next-move-alignment-packet-20261007 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Evidence / Verification

Ledger validator COMPLIANT; active-state closeability graph zero violations.
Source pins and line counts reverified. No checker/test implementation or worker
execution proof supplied by this dispatch-time packet.

## Local Technical Disposition

ACCEPT_SCOPE_FOR_BOUNDED_IMPLEMENTATION. Operator continuation on 2026-10-07
admits the named repair; operator selected Claude running Local as independent
reviewer and will relay the task. No automatic Claude invocation or subagent.
Implementation actor: LOCAL_CODEX_ROOT; probe actor: LOCAL_CLAUDE_OPERATOR_RELAY.
Actual invocation IDs, distinct oracle/evidence bytes and probe result must
be recorded at review; assignment is not executed independent proof.
Source Git-byte hashes and 951/1172 line counts reverified at e1a39623d2da54c0a5523bbec0d3574ff8d06b1e;
no source diff. Existing source handles legacy primary tokens and skips NCR;
three legacy full-classifier fixtures establish the preserved oracle group.
Ledger validation COMPLIANT. Full comparison remains textual consistency.
Prose-wrap claim narrowed to observable single-line boundaries; no arbitrary
history/prose discrimination or general semantic authorization is promised.
Packet commit plus current-authority pins, EXECUTE continuity and release gate
must precede worker edits. Worker returns once; independent proof and final
closure remain pending the operator-relayed Local reviewer.

Execution batch separates the newly admitted implementation from the earlier
planning/disposition batch; scope and source pins remain those reviewed above.
