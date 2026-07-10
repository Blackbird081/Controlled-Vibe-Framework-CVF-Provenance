# CVF System Chain Map

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-07-10

## Purpose

Provide a stable, truthful whole-picture reference for how CVF connects
frozen doctrine to contract, contract to runtime, runtime to enforcement,
enforcement to evidence, and evidence to operator-visible surfaces. This
reference is Deliverable B: it exists only because reviewer-accepted MSEA-R90
Audit A already produced five bounded, source-backed lane verdicts. This
README does not re-derive those verdicts; it presents them as a durable
front door for operators, developers, and future agents, alongside a
machine-checkable freshness contract that detects when the underlying
sources drift.

## Scope / Applies To

Applies to any operator, developer, or agent who needs a single entry point
for "how does CVF's governance chain actually connect end to end, and is
that picture still current." Does not apply to runtime/product code and
does not itself implement, modify, or supersede any `governance/compat/check_*.py`
checker, the R72F lifecycle decision, or the MSEA-R90 Audit A findings it
summarizes.

## Canonical Source

- Audit: `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md`
- Evidence: `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json`
- Reviewer acceptance: `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md`
  (`Status: REVIEWER_ACCEPTED_BOUNDED`, material commit `645df8b83`)
- Machine map: `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`
- Freshness contract: `docs/reference/system_chain/CVF_SYSTEM_CHAIN_FRESHNESS_STANDARD.md`

This README and its JSON companion carry only findings already accepted by
the MSEA-R90 reviewer closure. No claim here is stronger than that
acceptance; several rows below explicitly preserve `PARTIAL` scope rather
than presenting a partial connection as `CURRENT`.

## The Five-Lane Whole Picture

Each lane below distinguishes **current** (proven and unqualified),
**partial** (proven for a bounded sample or with a documented gap),
**historical** (a past state or trace, not a live receipt), and **future**
(explicitly deferred, not yet authorized) surfaces. Do not read a `PARTIAL`
row as `CURRENT` coverage of the full named scope.

### Lane 1 - Doctrine to Contract

laneId: `DOCTRINE_TO_CONTRACT`

**Posture: PARTIAL.** Verdict: `PARTIAL_CHAIN_WITH_DOCUMENTED_DRIFT`.

Frozen doctrine (`ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md`) declares seven
layers L0 through L6. L0 (`ECOSYSTEM/doctrine/`) and L3
(`ECOSYSTEM/operating-model/`) exist in the active tree and match the
doctrine's named contents. L1 and L2 doctrine-named content exists only
under a legacy-reference mirror, not the active `ECOSYSTEM/` tree - this is
a **historical** gap, not a current implementation. Three additional
module-map documents (`ARCHITECTURE.md`, `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md`,
`docs/CVF_CORE_KNOWLEDGE_BASE.md`) use independent layer-numbering schemes
not cross-referenced to the doctrine; this is recorded drift, not an error
in any of the four documents individually.

### Lane 2 - Contract to Runtime

laneId: `CONTRACT_TO_RUNTIME`

**Posture: PARTIAL.** Verdict: `PARTIAL_RUNTIME_CONNECTION_FOR_SAMPLED_ROWS`.

Three of the Governance Control Matrix's fifty `GC-NNN` rows were sampled
past file existence, to an actual caller/invocation route and to whether the
cited test exercises the cited source:

- **GC-011** is the one **current**, fully proven row: a real production
  caller exists at `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/sdk/cvf.sdk.ts:132`,
  and its cited test matches its cited source.
- **GC-001** is invoked (a real caller exists at
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts:122`), but its cited test
  exercises a distinct, non-identical source file from the one the matrix
  row names. Disposition: `INVOKED_WITH_CITED_TEST_PAIRING_MISMATCH`.
- **GC-009** has a valid, matched source-and-test pair, but no confirmed
  production caller was found anywhere in the repository.

The remaining 47 rows were not individually re-verified in this bounded
pass; treat them as a **future** verification target, not proven runtime
connections.

### Lane 3 - Runtime to Enforcement

laneId: `RUNTIME_TO_ENFORCEMENT`

**Posture: CURRENT.** Verdict: `PROVEN_CONNECTED_VIA_DATA_DRIVEN_REGISTRY`.

The nine deep-chain cross-family checkers
(`check_cross_family_approval_artifact_external_revocation_issuer_proof_authority_*.py`,
CF-076 through CF-084) are invoked through a real, data-driven,
parameterized chain: the documentation-testing CI workflow runs
`scripts/run_cvf_cross_extension_conformance.py`, which reads
`docs/reference/CVF_CONFORMANCE_SCENARIOS.json`'s CF-076..CF-084 command
arrays and subprocess-executes
`scripts/run_cvf_packet_posture_gate_conformance.py --gate` against each of
the nine checkers over four canonical packet postures.
`governance/compat/check_conformance_artifact_consistency.py` enforces
registry/report/summary mutual consistency.

The R72F `RETIREMENT_HOLD_SOURCE_GAP` lifecycle disposition for these nine
checkers is unchanged by this map. Execution-edge existence and
retirement-safety are separate questions; this reference does not reopen
or re-decide the R72F disposition.

### Lane 4 - Enforcement to Evidence

laneId: `ENFORCEMENT_TO_EVIDENCE`

**Posture: CURRENT** (for the corrected citations). Verdict:
`TWELVE_OF_TWELVE_DISPOSITIONED`.

All twelve prior path candidates across the seven-document evidence
manifest were recomputed fresh by MSEA-R90 Audit A: eleven were
`STALE_ARCHIVE_MOVE` (each with a confirmed archive successor) and one was
confirmed `MISSING`
(`CVF_H2_WORKING_MEMORY_RUNTIME_PROOF_COMPLETION_2026-05-22.md`, verified
absent by full-repository basename search). This R91 tranche corrects the
GC-019 roadmap citation in `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
and the ten distinct stale/missing citations in
`docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` to their
confirmed archive-qualified successors, and marks the H2 citation
explicitly missing rather than substituting the distinct sibling artifact
`CVF_T5_RUNTIME_MEMORY_WIRING_COMPLETION_2026-05-22.md` as an unproven
equivalent.

### Lane 5 - Evidence to Operator Surface

laneId: `EVIDENCE_TO_OPERATOR_SURFACE`

**Posture: PARTIAL.** Verdict: `PARTIAL_OPERATOR_VISIBILITY_BY_ENFORCEMENT_CLASS`.

`RUNTIME_GUARD` class evidence (GC-001 through GC-014) has a confirmed Web
UI route at
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance`.

`CI_REPO_GATE` class evidence (the 186 `governance/compat/check_*.py`
scripts, including the nine cross-family checkers from Lane 3) has proven
**current** CLI aggregate/per-check human-readable output:
`governance/compat/run_agent_autorun_workflow_gate.py` prints a
`[PASS]`/`[FAIL] <name> (<duration>)` line per configured checker, and
`governance/compat/run_local_governance_hook_chain.py` prints a
`PASS`/`FAIL` line per hook-chain step plus an aggregate summary. Web
Operations exposes a bounded five-job-type subset
(`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts`),
of which exactly one job type (`docs_governance_check`) wires directly to
one named checker (`check_docs_governance_compat.py`). **No unified Web
inventory across all 186 checkers exists** - this remains an explicit
**future** gap, not something to infer from the presence of the
`/governance` route directory alone.

## Operator Readout

If you need to know "is CVF's governance chain actually wired together,"
read the five lane postures above before trusting any single component's
own claim. If you need to know whether this map itself is still trustworthy,
run:

```
python governance/compat/check_system_chain_map_freshness.py --as-of-date <YYYY-MM-DD> --json --enforce
```

A `CURRENT` result means every fingerprinted source still matches its
recorded hash, the Markdown and JSON lane records still agree, and the map
was reviewed within the last 30 days. Any other result names a specific
remediation action - see
`docs/reference/system_chain/CVF_SYSTEM_CHAIN_FRESHNESS_STANDARD.md`.

## No-Auto-Semantics Guarantee

Detecting source drift or review-age expiry **never** rewrites a lane's
`currentPosture` or `verdict` automatically. Only a fresh governed review
that reads the changed source and issues a new accepted finding may update
those fields. The freshness checker's role is limited to flagging that a
review is due, not deciding what the review should conclude.

## Claim Boundary

This reference presents the five lane verdicts reviewer-accepted by
MSEA-R90 Audit A at material commit `645df8b83`. It does not certify
semantic correctness of every governed artifact in the repository, does not
prove all fifty Governance Control Matrix rows are runtime-connected, does
not claim a unified Web inventory exists for all 186 `governance/compat`
checkers, does not reopen or re-decide the R72F lifecycle disposition for
the nine cross-family checkers, and does not authorize a Web dashboard,
runtime/provider/live behavior, public export, or session-state mutation.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | repo-local reference summarizing reviewer-accepted MSEA-R90 Audit A findings |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: five lane postures with source citations; no new semantic finding beyond R90 acceptance |
| receiptEvidence | N/A with reason: this reference has no runtime execution receipt of its own; its evidence is the cited R90 audit and reviewer completion artifacts |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source fingerprints recomputed and verified against current repository content at authoring time |
| invocationBoundary | manually authored governed reference plus a companion machine-checkable freshness checker |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, or Web interception claim |
| claimLanguage | source-backed summary and freshness-detection reference, not a new audit |
| forbiddenExpansion | no Web dashboard, runtime/provider/live behavior, public export, R72F lifecycle re-decision, session-state mutation, or automatic semantic-verdict rewrite |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: no public-sync authorization exists for MSEA-R91.
