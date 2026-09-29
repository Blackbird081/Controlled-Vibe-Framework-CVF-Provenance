# CVF GC-018 AGSG-BSH-T1 Scope-Triggered Blind-Spot Presence Guard

Memory class: FULL_RECORD

Status: WORK_ORDER_READY

Date: 2026-06-28

docType: baseline

Batch ID: AGSG-BSH-T1

## Purpose

Authorize a scope-triggered machine check that closes the recurring absorption
blind-spot recorded as [ADIF-0014](../reference/agent_defect_intelligence/entries/CVF_ADIF-0014.md):
CVF's Mandatory Knowledge Absorption Blind-Spot Control and Mandatory Corpus
Completeness controls are both claim-triggered, so an absorption artifact that
touches a legacy or external source folder but stays silent about completeness
can close `PASS` without ever invoking either control. The AGSG-T1 absorption
baseline is the observed instance: it carries neither a Blind-Spot Control
Block nor a Corpus Completeness block, and no gate fired.

This baseline authorizes design and dispatch only. It does not itself
implement the checker; implementation is delegated to the paired work order
under the dispatch-author-is-not-executor rule (B13/B23).

## Scope

In scope:

- author this GC-018 baseline and its paired work order;
- record the defect as ADIF-0014 (already created in this batch);
- specify a scope-triggered presence checker
  `governance/compat/check_absorption_blindspot_control_presence.py` that, when
  a changed work order / GC-018 baseline / completion review touches a source
  path under `.private_reference/legacy/` or `.private_reference/external_repos/`,
  requires the artifact to carry the Mandatory Blind-Spot Control Block heading
  and a Corpus Completeness And Report Integrity block, independent of any
  completeness claim;
- wire the checker into the local governance hook chain at pre-dispatch and
  pre-implementation;
- add fixtures proving both a passing and a failing case.

Out of scope (parked / forbidden unless separately authorized):

- editing the existing claim-triggered checkers
  (`check_knowledge_absorption_priority_compat.py`,
  `check_corpus_completeness_report_integrity.py`);
- runtime, provider, live, public-sync, or benchmark behavior;
- importing upstream skill content (that is the separate ASSF skill-library
  enrichment lane, not this hardening lane);
- retroactively re-opening or re-closing the AGSG absorption lane.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Baseline decision | Promote ADIF-0014 from rule to a scope-triggered machine check at the earliest applicable autorun phase |
| Proposed tranche | AGSG-BSH-T1 checker design + work order dispatch; implementation by executor |
| Runtime disposition | NOT_APPLICABLE_WITH_REASON: offline governance checker only |
| Checker disposition | IMPLEMENT_SCOPE_TRIGGERED_PRESENCE_CHECK |
| Public disposition | DEFERRED_PRIVATE_ONLY |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Blind-Spot Control standard mandates a control block with seven gates and a CLEAR/PARTIAL/BLOCKED verdict | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | `## Mandatory Blind-Spot Control Block` | `Blind-Spot Control Block` | blind-spot prevention standard | ACCEPT |
| Corpus completeness control is triggered by a completeness claim or the required section, not by source scope | `governance/compat/check_corpus_completeness_report_integrity.py` | `REQUIRED_SECTION`; completeness-claim regex list | `REQUIRED_SECTION` | corpus completeness checker | ACCEPT |
| Knowledge absorption priority checker exists and runs in the hook chain | `governance/compat/check_knowledge_absorption_priority_compat.py` | top module docstring | `check_knowledge_absorption_priority_compat` | knowledge absorption checker | ACCEPT |
| Both checkers are listed in the local governance hook chain | `governance/compat/run_local_governance_hook_chain.py` | `check_knowledge_absorption_priority_compat.py`; `check_corpus_completeness_report_integrity.py` | hook chain checker list | local governance hook chain | ACCEPT |
| Observed instance: AGSG-T1 baseline carries neither control block | `docs/baselines/CVF_GC018_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md` | full file; no `Blind-Spot Control Block` and no `Corpus Completeness` heading present | absence of both headings | AGSG-T1 baseline | ACCEPT |
| Learning philosophy mandates rule-to-machine-check-to-earliest-gate escalation | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | escalation-ladder section | escalation ladder | learning philosophy | ACCEPT |
| Defect is recorded as ADIF-0014 with GUIDANCE_ONLY pending this checker | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0014.md` | `defectId: ADIF-0014`; `enforcementLevel` | `ADIF-0014` | ADIF registry | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Running `governance/compat/run_adif_defect_resolver.py` for the work-order
authoring / dispatch task class at pre-dispatch returns: ADIF-0001 (exhaustive
directory claim), ADIF-0002 (provider-local interaction accepted as authority),
ADIF-0006 (Source Verification symbol cell contains a value/type), ADIF-0007
(gate marker in boundary prose triggers wrong evidence class), ADIF-0008
(memory-only lesson anti-pattern), and the new ADIF-0014 (scope-triggered
absorption control evaded by completeness silence) authored in this batch.
Each is honored: this baseline carries a Source Verification Block whose
`Verified path or symbol` cells contain only symbols (ADIF-0006), keeps gate
verdict tokens out of boundary prose (ADIF-0007), cites governed sources rather
than provider-local memory (ADIF-0002), enumerates a manifest in its work
order (ADIF-0001), and records the lesson in the ADIF registry rather than
session memory only (ADIF-0008, ADIF-0014).

## Mandatory Blind-Spot Control Block

Knowledge Absorption Blind-Spot Control Block

- Gate 1 (source enumeration): the source-of-record for this lane's claims is
  the AGSG-T1 baseline and the two existing absorption checkers; the upstream
  `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack`
  and `.private_reference/external_repos/agent-skills` are cited only as the
  observed-instance evidence, not re-absorbed here.
- Gate 2 (prior-scan reuse): inherits the AGSG absorption scan; this lane adds
  no new corpus claim.
- Gate 3 (capability-surface coverage): scope is one offline checker plus hook
  wiring and fixtures; no provider/memory/graph/workflow/CLI/MCP surface.
- Gate 4 (non-coder outcome): not applicable; offline governance guard.
- Gate 5 (pain-point linkage): directly closes the Review-CVF documentation-gap
  pain point (capability present but unsurfaced) at its absorption-time root.
- Gate 6 (claim boundary): this lane authorizes a presence checker only; it
  does not import skill content or re-open the AGSG absorption verdict.
- Gate 7 (completeness): the manifest in the paired work order enumerates every
  file the executor may create or modify; no source folder is claimed as
  exhaustively re-read because no re-absorption occurs here.
- Blind-spot verdict: CLEAR

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - this is a GC-018 dispatch baseline, not a
  corpus inventory, folder-tree scan, or extraction report.
- Corpus root: N/A with reason - no corpus root was authorized or enumerated;
  the legacy/external source folders are cited as observed-instance evidence,
  not re-scanned here.
- Snapshot time: 2026-06-28 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads and `rg -n` source
  lookups over the named AGSG-BSH-T1 authority files.
- Manifest artifact or inline manifest: Source Verification Block and the paired
  work order Execution Plan manifest.
- Manifest hash: N/A with reason - no generated corpus manifest artifact was
  produced.
- Processing ledger artifact or inline ledger: inline in the Source
  Verification Block.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline; ledger_terminal=inline; exclusions=no-corpus-inventory-scope; unresolved=0.
- Unresolved files: 0
- Declared exclusions: full corpus inventory, folder-tree scan, extraction
  report, upstream skill-content absorption, runtime/provider proof, public-sync.
- Unreadable or unsupported files: none.
- Aggregation check: N/A with reason - no corpus aggregate was produced.
- Drift check: N/A with reason - no corpus aggregate was produced.
- Output traceability: baseline source evidence cites current repo authority
  files and the paired work order carries the executor manifest.
- Adversarial verification: claim rejects any full-corpus, complete-inventory,
  runtime, or public readiness assertion.
- Corpus verdict: PARTIAL

## Rescan Intelligence Hardening

- Original source artifact: the observed AGSG-T1 absorption instance and the
  two existing claim-triggered absorption checkers.
- Predecessor intake artifact:
  `docs/baselines/CVF_GC018_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because this lane promotes the
  blind-spot control from rule-only to a planned scope-triggered machine check
  (ADIF-0014), without re-scanning any corpus.
- Routing matrix status:
  - `DO_NOW`: author this baseline, the work order, and ADIF-0014.
  - `SEPARATE_RUNTIME_TRANCHE`: checker implementation is delegated to the
    paired work order's executor.
  - `OUT_OF_SCOPE`: corpus rescan, intake refresh, runtime, provider/live,
    public-sync, skill-content import.
- Semantic sampling status: `PARTIAL_TARGETED`, limited to confirming the
  AGSG-T1 baseline carries neither control block.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Current finding | Predecessor finding | Delta category | Current disposition | Reason |
| --- | --- | --- | --- | --- |
| Blind-spot control is rule-only and claim-triggered | AGSG-T1 absorption | CHANGED_DISPOSITION | Promote to a planned scope-triggered machine check (ADIF-0014) | AGSG-T1 closed PASS without either control block; the gap is real and recurring. |
| The two existing absorption checkers stay claim-triggered | AGSG-T1 absorption | UNCHANGED_FROM_INTAKE | Leave unmodified | This lane adds a presence checker; it does not change the existing claim-triggered checkers. |
| Upstream skill content remains unabsorbed | AGSG-T1 absorption | OUT_OF_SCOPE | Separate ASSF skill-library lane | Skill-content import is a different lane needing its own GC-018. |
| Scope-triggered presence-check requirement | N/A | NEW_FINDING | Authorize the checker under this GC-018 | The claim-triggered evasion path is a newly named defect (ADIF-0014). |
| Broad "absorption is audited" assumption | AGSG-T1 absorption | REMOVED_OR_REJECTED | Rejected | "Already audited" does not prove either control block ran; the assumption is rejected. |

### Follow-Up Routing Matrix

| Finding or issue | Routing lane | Action boundary |
| --- | --- | --- |
| Implement the scope-triggered presence checker | SEPARATE_RUNTIME_TRANCHE | Delegated to the paired work order's executor (Codex). |
| Record the defect pattern | DO_NOW | ADIF-0014 authored in this batch. |
| Import the 23 upstream skills | STRATEGIC_OPERATOR_DECISION | Operator opens the ASSF skill-library enrichment lane separately. |
| Existing claim-triggered checkers | RESOLVED_BY_DESIGN | Left unmodified by design; the new checker is additive, not a replacement. |
| Corpus rescan / intake refresh | OUT_OF_SCOPE | No corpus is rescanned; this lane authorizes a presence checker only. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| BSH-SAMPLE-01 | AGSG-T1 baseline | The baseline carries neither a Blind-Spot Control Block nor a Corpus Completeness block | grep over the AGSG-T1 baseline | Could either control block be present under a different heading? | PASS - direct grep confirms neither heading is present anywhere in the file. |

## Evidence / Verification

- ADIF-0014 created and `check_adif_entry_integrity.py --enforce` returns
  COMPLIANT (14 entries, 0 violations).
- `check_adif_defect_registry_disclosure.py` returns COMPLIANT for this
  baseline and its work order.
- `check_corpus_completeness_report_integrity.py` returns COMPLIANT for the
  changed range.
- The observed instance (AGSG-T1 baseline missing both control blocks) is
  verified by direct grep showing neither heading present.

## Continuation / Next Allowed Move

Dispatch the paired work order
`docs/work_orders/CVF_AGENT_WORK_ORDER_AGSG_BSH_T1_SCOPE_TRIGGERED_BLINDSPOT_PRESENCE_GUARD_2026-06-28.md`
to an executor (Codex) under WORKER_MUST_NOT_COMMIT until review. Dispatch
authorship here does not grant execution authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal governance baseline. No public-sync claim.

## Claim Boundary

This baseline authorizes design and dispatch of a scope-triggered presence
checker and records ADIF-0014. It does not implement the checker, modify
existing checkers, import external content, or alter the AGSG absorption lane
verdict.
