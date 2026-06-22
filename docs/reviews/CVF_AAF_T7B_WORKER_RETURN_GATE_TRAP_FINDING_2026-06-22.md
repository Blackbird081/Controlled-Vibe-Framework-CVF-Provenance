# CVF AAF-T7B Worker-Return Gate-Trap Finding

Memory class: FULL_RECORD

Status: FINDING_RECORDED

docType: finding_review

Date: 2026-06-22

Reviewer: Claude (worker-role observation during AAF-T7B execution, recorded under operator instruction 2026-06-22)

rawMemoryReleased: false

## Purpose

Record four repeating governance-gate authoring traps observed while producing
the AAF-T7B worker-return artifact. Each trap forced an authoring round that
reworded incidental tokens or added a required block, not a correction of real
scope. These are continuation evidence for the CGFP family (checker trigger and
structure context gaps), not a new root cause. This finding promotes the
observations from worker-session experience into a governed artifact so the
lessons survive outside provider memory, per the agent-error-to-governance
learning philosophy.

## Scope / Target / Owner Boundary

Target: the applicability and structure logic of four governance checkers as
exercised by a `docType: review` worker-return artifact that also touches
protected `governance/compat/` files. Owner boundary: this artifact records the
finding only. It modifies no checker, no standard, and no AAF-T7B deliverable.
Any checker hardening or standard-row promotion requires a separate GC-018 and
work order reviewed and closed by the reviewer/closer role.

## Target / Source

Observed while authoring
`docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_WORKER_RETURN_2026-06-22.md`
at execution base HEAD `7e52ab68`, against the AAF-T7B work order and GC-018
baseline. The pre-implementation autorun gate cycled 2 then 4 then 1 then 0
failing gates, and the worker-return fast gate cycled 1 then 0, across authoring
rounds. Most repairs were structural-block additions or token rewording.

Source checkers:

- `governance/compat/check_core_guard_self_protection.py` (`_has_core_auth`, required tokens at lines 271-277)
- `governance/compat/check_closure_packaging_preflight.py` (core-guard closure preflight on protected paths)
- `governance/compat/check_rescan_intelligence_hardening.py` (`placeholder_residue` token scan, line 335)
- `governance/compat/check_agent_packet_authority_and_encoding.py` (authority-path regex, line 27)

## Scope / Methodology

Each trap was located by running the failing checker directly with
`--base 7e52ab68 --head HEAD --enforce`, reading the violation code, and
cross-checking against the checker's constant or regex. Each repair was the
minimum change that satisfied the gate without weakening real evidence, then the
full pre-implementation autorun gate and worker-return fast gate were rerun to
confirm zero violations.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Disposition |
|---|---|---|---|---|
| Core-guard auth requires four tokens plus every protected path | `governance/compat/check_core_guard_self_protection.py` | lines 271-277 | `_has_core_auth` | ACCEPT |
| Auth doc must be a changed standard auth-doc path | `governance/compat/check_core_guard_self_protection.py` | lines 140-176 | `_authorization_docs`; `_is_standard_auth_doc_path` | ACCEPT |
| Placeholder residue scans the rescan section for the token | `governance/compat/check_rescan_intelligence_hardening.py` | line 335 | placeholder-residue token tuple | ACCEPT |
| Authority-path regex matches any docs path ending .md | `governance/compat/check_agent_packet_authority_and_encoding.py` | line 27 | review-packet authority path pattern | ACCEPT |

## Findings / Position

| ID | Finding | Evidence | Disposition |
|---|---|---|---|
| F-AAFT7B-001 | A source-only changed set touching protected `governance/compat/` files fails core-guard and closure-packaging until a changed auth-doc carries the `Core Guard Self-Protection Authorization` block listing every protected path; the committed GC-018 is not in the changed range, so the worker-return artifact must carry the block itself. | Two checkers fired on the two helper files until the worker return under `docs/reviews/` added the authorization block with both protected paths and the four required tokens. | MACHINE_GATE_DESIGN_EXPECTED |
| F-AAFT7B-002 | The rescan placeholder-residue scan fires on the bare token used as evidence inside the rescan section, even when describing the helper output legitimately. | The adversarial-review row described the scaffold body as having empty fields using the residue token, which tripped the gate; rewording to a non-token phrase cleared it. | MACHINE_GATE_GAP |
| F-AAFT7B-003 | The review-packet authority gate treats any `docs/{baselines,roadmaps,work_orders,reviews}/...md` string in the body as a cited authority artifact and requires it to exist, so demonstration or smoke-only paths in an Evidence section become missing-authority failures. | The Evidence section named two non-existent smoke paths to document write-refusal behavior; the gate read them as cited authority and failed until they were described generically. | MACHINE_GATE_GAP |
| F-AAFT7B-004 | A `docType: review` worker-return artifact must satisfy the full strict Rescan Intelligence Hardening schema (six fields, three subsections, four delta categories, six routing lanes) and the markdown common-element `Status:` line, even for a bounded helper return with no re-intake. | The freeform rescan table and a `## Status` heading without a `Status:` line failed both gates until the canonical schema and a top-level `Status:` line were added. | MACHINE_GATE_DESIGN_EXPECTED |

Position: F-AAFT7B-001 and F-AAFT7B-004 are correct, by-design gate behavior
and are recorded so the next author front-loads the blocks. F-AAFT7B-002 and
F-AAFT7B-003 are checker-context gaps in the CGFP family: the gate matches a
token or path string without distinguishing evidence-quoting prose, demonstration
paths, or smoke examples from real citations. All four are worker-blameless.

## Risk / Corrective Action

Risk: authors spend rounds adding boilerplate or rewording legitimate evidence,
and may learn to strip honest evidence reflexively to dodge a token or path
match, which could hide a real future violation.

Corrective action: no change is made by this finding. Recommended follow-ups,
each requiring its own GC-018 and work order:

- promote F-AAFT7B-001 and F-AAFT7B-004 as authoring-front-load rows in the
  work-order authoring hardening addendum so worker-return packets carry the
  core-guard block and full rescan schema from the first draft;
- extend the CGFP checker-context hardening to F-AAFT7B-002 and F-AAFT7B-003 so
  the placeholder-residue scan ignores tokens inside quoted evidence cells, and
  the authority-path gate ignores paths inside code fences, inline code, or a
  recognized demonstration or smoke-example context.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `MACHINE_GATE_GAP` for F-AAFT7B-002 and F-AAFT7B-003; `MACHINE_GATE_DESIGN_EXPECTED` for F-AAFT7B-001 and F-AAFT7B-004 |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_CANDIDATE` for the two gap findings; `AUTHORING_ADDENDUM_CANDIDATE` for the two design-expected findings |
| Root cause grouping | `PROPAGATED_SYMPTOM` of the CGFP keyword and structure context root cause; cite `docs/reviews/CVF_CGFP_T1_CHECKER_TRIGGER_FALSE_POSITIVE_FINDING_2026-06-17.md` as upstream cause |
| Next control action | reviewer/closer routes to a CGFP follow-up tranche or authoring-addendum tranche through a fresh GC-018 |
| Worker blame | `N/A_WITH_REASON`: applicability and structure context gaps are checker and authoring-template design matters, not a worker error |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude (finding author, worker-role observation) |
| Provider or surface | Claude Code VSCode extension |
| Session or invocation | 2026-06-22 AAF-T7B worker execution and finding authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Grep, Bash (git, python checkers) |
| Target paths | this finding record |
| Allowed scope source | operator instruction 2026-06-22 to record the gate-trap finding per the rules |
| Before status evidence | clean worktree at `7e52ab68` after stashing the AAF-T7B batch (git status --short empty) |
| After status evidence | finding recorded; no commit by this authoring |
| Diff evidence | `git diff --name-status` |
| Approval boundary | finding record only; no checker, standard, or AAF-T7B deliverable modified |
| Claim boundary | repo-local trace only; no runtime, provider, or public behavior |
| Agent type | Claude |
| Invocation ID | `aaf-t7b-gate-trap-finding-2026-06-22` |
| Expected manifest | this finding record |
| Actual changed set | this finding record |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Self-Demonstration Note

This finding must quote the trigger token and the path-shaped strings as
evidence, so it would itself trip the rescan placeholder-residue scan and the
authority-path gate if those tokens were placed outside guarded contexts. The
rescan schema below is authored to satisfy the current gates; that an honest
finding cannot pass without dodging its own documented traps corroborates
F-AAFT7B-002 and F-AAFT7B-003.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance finding. No public-sync batch is
authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T7B worker-return gate-trap finding record |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | finding record authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, or provider interception claim |
| claimLanguage | finding record only |
| forbiddenExpansion | checker modification, standard-row edits, AAF-T7B deliverable edits, runtime, provider, public-sync, and any apply behavior remain out of scope |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | local governed control-plane finding route, not external authority |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | AAF-T7B worker-return gate-trap finding |
| Disposition | ADAPT as a CVF-owned finding record with bounded follow-up routing |
| Claim boundary | observations remain a finding record until a separate governed tranche acts on them |

## Corpus Completeness And Report Integrity

- Corpus task class: control-plane finding record for four observed gate traps.
- Corpus root: the four source checkers and the AAF-T7B worker-return artifact.
- Snapshot time: 2026-06-22 finding authoring.
- Enumeration command: filesystem-backed direct file reads plus `rg --files --hidden --no-ignore` for targeted confirmation.
- Manifest artifact or inline manifest: Source Verification Block in this finding.
- Manifest hash: N/A with reason: bounded direct-read finding, no generated manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows in this finding.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=Source Verification Block; ledger_terminal=READ for cited checker rows; exclusions=full-repo sweep and checker code edits; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: full-repo sweep, checker code edits, standard-row edits, runtime, provider, web, MCP, and public-sync surfaces.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated by this finding.
- Drift check: N/A with reason: no generated aggregate edited by this finding.
- Output traceability: each finding ID maps to a checker constant or regex in the Source Verification Block.
- Adversarial verification: the Semantic Sampling table distinguishes design-expected gate behavior from checker-context gaps.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Finding-To-Governance Learning Disposition Table

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Protected-guard auth block must be in the changed worker return | MACHINE_GATE_DESIGN_EXPECTED | GOVERNANCE_CONTROL_PLANE | AUTHORING_ADDENDUM_CANDIDATE | front-load the core-guard block in worker-return authoring | deferred to a separate tranche |
| Placeholder-residue scan fires on quoted evidence token | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | extend CGFP context-stripping to evidence cells | deferred to a separate tranche |
| Authority-path gate fires on demonstration or smoke paths | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | extend CGFP context-stripping to fenced and demonstration paths | deferred to a separate tranche |
| Strict rescan schema and Status line required for review docType | MACHINE_GATE_DESIGN_EXPECTED | GOVERNANCE_CONTROL_PLANE | AUTHORING_ADDENDUM_CANDIDATE | front-load the full rescan schema in worker-return authoring | deferred to a separate tranche |

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: this is a deterministic record of observed
checker behavior with direct command evidence, not an estimation, forecast, or
probabilistic judgment task; no epistemic confidence calibration applies.

## Machine Closure Package

| Closure item | Required artifact or path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: this is a finding record, not a work order | no work order in this artifact | N/A with reason: finding record |
| Completion or reviewer artifact | this file | finding recorded | FINDING_RECORDED |
| Roadmap state | N/A with reason: standalone finding, no roadmap | no roadmap row | N/A with reason: no roadmap |
| Runtime, provider, or live evidence | N/A with reason: no runtime, provider, or live behavior | no runtime calls | N/A with reason: no runtime |
| Public-sync evidence | N/A with reason: no public-sync authorized | no public-sync | N/A with reason: no public-sync |
| System loop interlock | N/A with reason: no system-loop surface in scope | no loop scope | N/A with reason: no loop |
| Session continuity | N/A with reason: no session mutation by this finding | no session change | N/A with reason: no session mutation |

## Rescan Intelligence Hardening

- Original source artifact: N/A with reason: not a re-intake; a checker-behavior finding from AAF-T7B worker execution.
- Predecessor intake artifact: `docs/reviews/CVF_CGFP_T1_CHECKER_TRIGGER_FALSE_POSITIVE_FINDING_2026-06-17.md` as the upstream CGFP root cause.
- Delta ledger status: `NEW_FINDING` because two new checker-context traps and two design-expected authoring requirements are recorded.
- Routing matrix status: `STRATEGIC_OPERATOR_DECISION` for whether to open a CGFP follow-up or authoring-addendum tranche.
- Semantic sampling status: sampled the four checker constants and the AAF-T7B worker-return artifact sections that triggered them.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | The CGFP root cause (keyword and structure context gaps) is unchanged. |
| CHANGED_DISPOSITION | The CGFP family now has two additional checker-context instances and two authoring-front-load instances. |
| NEW_FINDING | Placeholder-residue scan on quoted evidence and authority-path gate on demonstration paths are newly recorded. |
| REMOVED_OR_REJECTED | No prior finding is removed or rejected by this record. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | None; this is a record-only finding with no in-scope change. |
| RESOLVED_BY_DESIGN | The core-guard block and rescan schema requirements are intended gate behavior; document them as authoring front-load. |
| DEFER | CGFP context-stripping extension and authoring-addendum rows to a separate governed tranche. |
| STRATEGIC_OPERATOR_DECISION | Operator decides whether to open the CGFP follow-up or addendum tranche. |
| SEPARATE_RUNTIME_TRANCHE | None; no runtime, provider, or public behavior is involved. |
| OUT_OF_SCOPE | Editing checker code, editing standards, and editing AAF-T7B deliverables in this finding. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T7B-GT-RS1 | core-guard checker tokens | protected guard files need a changed auth block | RESOLVED_BY_DESIGN | Is this a checker bug or intended protection? | PASS - intended protection; record as authoring front-load |
| AAF-T7B-GT-RS2 | rescan placeholder scan | residue token scan ignores context | MACHINE_CHECK_CANDIDATE | Could the token be legitimate quoted evidence? | PASS - yes; gap confirmed, defer to CGFP follow-up |
| AAF-T7B-GT-RS3 | authority-path regex | any docs md string is a citation | MACHINE_CHECK_CANDIDATE | Could the path be a demonstration or smoke example? | PASS - yes; gap confirmed, defer to CGFP follow-up |
| AAF-T7B-GT-RS4 | rescan schema requirement | review docType needs the full schema | RESOLVED_BY_DESIGN | Should a bounded helper return be exempt? | PASS - no exemption exists; record as authoring front-load |

## Claim Boundary

This finding records four observed governance-gate authoring traps from AAF-T7B
worker execution and routes recommended follow-ups. It modifies no checker, no
standard, and no AAF-T7B deliverable, changes no runtime behavior, and does not
claim the gaps are fixed. Any fix requires a separate GC-018, work order, and
reviewer or closer closure.
