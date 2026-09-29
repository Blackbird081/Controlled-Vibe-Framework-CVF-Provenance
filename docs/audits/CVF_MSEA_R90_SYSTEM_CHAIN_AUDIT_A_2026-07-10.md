# CVF MSEA-R90 System Chain Audit A

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_BOUNDED

docType: audit

Date: 2026-07-10

Batch ID: MSEA-R90

Worker: delegated worker role

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: `b6cba5924`

Machine companion: `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json`

## Purpose

Complete a truthful, source-backed audit that traces CVF from doctrine to
contract, contract to runtime, runtime to enforcement, enforcement to
evidence, and evidence to operator-visible surfaces. This closes the three
previously unresolved chain rows and revalidates the two rows that already
had findings, using only current CVF-owned source as authority.

## Target / Source

Target: the five system-chain edges named in the paired work order.

Source authority (current-source and canonical-contract precedence, per
Authority Chain in the work order):

- `ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md` (frozen doctrine)
- `ARCHITECTURE.md`, `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md`,
  `docs/CVF_CORE_KNOWLEDGE_BASE.md` (module-map narrations)
- `docs/reference/CVF_MODULE_INVENTORY.md`,
  `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`
  (prior bounded audit input; explicitly denies a complete-plane claim in its
  own Claim Boundary; reconciled, not copied)
- `docs/reference/CVF_MSEA_R72F_FIRST_RETIREMENT_OR_CONSOLIDATION_PILOT_DECISION_MATRIX_2026-07-08.md`
  (later lifecycle authority for the 9 cross-family checkers)
- `docs/reference/CVF_CONFORMANCE_SCENARIOS.json`,
  `scripts/run_cvf_cross_extension_conformance.py`,
  `scripts/run_cvf_packet_posture_gate_conformance.py`,
  `.github/workflows/documentation-testing.yml`
- Temporary correction reports under the operator advisory directory
  (`Gop y CVF/10.07/`) were read only as advisory context, per work order;
  every accepted fact below is re-derived from CVF-owned source.

## Scope / Methodology

Filesystem-backed direct reads, JSON parsing, `rg`/`grep`/`find` exact
searches, and current Git metadata (`git rev-parse`, `git status`) at
`executionBaseHead b6cba5924`. Each edge is traced through claim, source,
invocation, test/evidence, and operator-surface columns, recorded in the JSON
companion's `chainEdges` array with per-citation file/line/section evidence.
Contradictions are logged in a contradiction ledger with an authority
precedence rule and a narrowed claim, not silently resolved.

## Findings / Position

### Lane 1 - Doctrine to contract

`ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md` (Layer Overview, lines 18-32) is
frozen doctrine declaring seven layers L0 through L6: Doctrine, System
Definition, Build Protocol, Operating Model, Product Implementation,
Governance Modules, Ecosystem Layer.

The doctrine's own illustrative locations only partially match the live
repository:

- L0 (`/doctrine`) - live at `ECOSYSTEM/doctrine/`, all four named files
  present (`CVF_PRODUCT_POSITIONING.md`, `CVF_ARCHITECTURE_PRINCIPLES.md`,
  `CVF_ECOSYSTEM_MAP.md`, `CVF_LAYER_MODEL.md`), plus one additional file
  (`CVF_DOCTRINE_RULES.md`) not named by the doctrine's own inventory.
- L1 (`/system`, `CVF_PROJECT_MANIFEST.md`) - **not found in the active
  `ECOSYSTEM/` tree**. The only copy exists under the legacy-reference mirror
  path `private-reference / legacy / CVF_Restructure / CVF_ECOSYSTEM /
  system/`, not current authority.
- L2 (`/protocols`, `CVF_AGENT_BUILD_PROTOCOL.md`) - **not found in the
  active `ECOSYSTEM/` tree**. The only copy is under the same legacy
  mirror path at `private-reference / legacy / CVF_Restructure /
  CVF_ECOSYSTEM / protocols/`.
- L3 (`/operating-model`) - live at `ECOSYSTEM/operating-model/`, containing
  `CVF_AGENT_OPERATING_MODEL.md` and `CVF_BUILDER_MODEL.md`, matching the
  doctrine's named contents.
- L4-L6 (`/cvf-core`, `/agents`+`/policy`+`/audit`+`/identity`,
  `/examples`+`/docs`) - no single active folder set was confirmed to match
  these illustrative paths one-to-one; L6's `/docs` element is broadly
  satisfied by the live `docs/` tree, and L4/L5 content is distributed across
  `EXTENSIONS/` and `governance/` rather than the doctrine's named paths.

A second finding: three additional module-map documents currently coexist as
active read surfaces and use layer-numbering schemes that are not the
doctrine's L0-L6 and are not declared as restatements of it in their own
text: `ARCHITECTURE.md` (a four-role Meta/Control/Channels/Evidence stack),
`docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md` (a "5 Layers" mermaid stack
footer-dated 2026-02-25), and `docs/CVF_CORE_KNOWLEDGE_BASE.md` (a separate
"5 Layers" v1.0-v1.7.2 version stack that self-declares itself the base for
future additions in its own Rule 4). This is recorded in Contradiction Ledger
entry CL-01 with an authority-precedence resolution: the frozen doctrine
outranks the three narrations for layer-naming claims; the narrations are not
treated as wrong, only as parallel, non-doctrine-derived descriptions.

Verdict for this lane: `PARTIAL_CHAIN_WITH_DOCUMENTED_DRIFT`. The doctrine
exists and is internally coherent; two of its seven named content locations
(L1, L2) have no active-tree counterpart; the broader repository is described
by at least three other module maps that do not reference the doctrine's
layer vocabulary.

### Lane 2 - Contract to runtime

`docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` is a fifty-row control
matrix mapping each `GC-NNN` rule to a primary owner, enforcement class, and
evidence path. File existence alone does not prove a runtime connection;
each of the three sampled rows was traced past its cited file to a real
caller/invocation route and to whether its cited test actually exercises
that same source symbol. Findings:

- **GC-001** (`EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/phase-gate.guard.ts`,
  class `PhaseGateGuard`) - file present, and a real runtime caller exists:
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` line 122
  (`engine.registerGuard(new PhaseGateGuard())`). A separate SDK bridge
  registration at
  `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/sdk/cvf.sdk.ts`
  line 821 uses a **different, non-identical** `PhaseGateGuard` class defined
  in that module's own `governance/guard_runtime/guards/phase.gate.guard.ts`;
  it is not evidence for the GC-001 cited implementation. The matrix row's
  cited test,
  `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/tests/guard.runtime.test.ts`,
  imports `PhaseGateGuard` from
  `../governance/guard_runtime/guards/phase.gate.guard.js` (confirmed by a
  direct `diff` of the two same-named class files: the v1.1.1 module's
  version is a v1.1.3-hardening rewrite with a different import surface,
  different phase/role tables, and a different type source) - **not** from
  the file the matrix row cites
  (`EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/phase-gate.guard.ts`). The
  cited runtime file has a real caller; the cited test does not test that
  same file. Row disposition:
  `INVOKED_WITH_CITED_TEST_PAIRING_MISMATCH` (the runtime symbol is invoked;
  the test-to-source citation pairing in the matrix row is mismatched).
- **GC-009** (`EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts`,
  class `MandatoryGateway`, factory `createMandatoryGateway`) - file present,
  and the cited test
  (`EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts`)
  correctly imports `MandatoryGateway` from the same-directory
  `./mandatory-gateway` (confirmed same-file citation, valid test-to-source
  pairing). However, a repo-wide search
  (`grep -rn "MandatoryGateway\|createMandatoryGateway"` across all `.ts`
  files, excluding the class's own definition and its own test) found
  **zero non-test callers** anywhere in the repository - no channel entry
  wrapper, SDK bridge, or `index.ts` re-export instantiates or imports it.
  Row disposition: `IMPLEMENTED_NOT_INVOCATION_PROVEN` (source and test
  exist and match each other; no production caller route was found).
- **GC-011**
  (`EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/pipeline.orchestrator.ts`,
  class `PipelineOrchestrator`) - file present, re-exported from
  `governance/guard_runtime/index.ts` line 47, and instantiated by a real
  caller: `governance/guard_runtime/sdk/cvf.sdk.ts` line 132
  (`this.pipeline = new PipelineOrchestrator(this.engine)` inside the SDK
  bridge constructor, imported at line 38). The cited test file
  (`EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/tests/pipeline.orchestrator.test.ts`)
  is confirmed present. Row disposition: `PROVEN_CONNECTED` - this is the
  one row of the three with a matched runtime caller, source, and test all
  pointing at the same symbol.

The same matrix's GC-019 row cites
`docs/roadmaps/CVF_RESTRUCTURING_ROADMAP_2026-03-21.md` as an active-path
evidence pointer; the file exists only at
`docs/roadmaps/archive/CVF_RESTRUCTURING_ROADMAP_2026-03-21.md`. This is
carried into the Enforcement-to-evidence lane as path-disposition candidate
EPD-01, since the control matrix is itself one of the seven evidence-manifest
documents.

The remaining 47 control-matrix rows were not individually re-verified for
runtime-symbol existence in this bounded pass; this is recorded as a sampling
limit in the JSON companion, not a claim that all fifty rows are proven.

Verdict for this lane: `PARTIAL_RUNTIME_CONNECTION_FOR_SAMPLED_ROWS`.
Of the three spot-verified rows, only GC-011 reached a fully proven
source-caller-test match; GC-001's cited test exercises a different,
non-identical source file than the one the matrix row names; GC-009 has a
valid source-test pairing but no confirmed production caller anywhere in
the repository. This lane's verdict is downgraded from the prior draft's
`PROVEN_CONNECTED_FOR_SAMPLED_ROWS` because file existence alone was
insufficient evidence of a proven runtime connection for 2 of the 3 sampled
rows.

### Lane 3 - Runtime to enforcement (reverified, not copied)

This lane corrects and closes the previously open runtime-to-enforcement
question for the nine deep-chain
`check_cross_family_approval_artifact_external_revocation_issuer_proof_authority_*.py`
checkers. Every hop was re-derived from current source at this audit's
`executionBaseHead`, independent of any temporary advisory report:

1. `.github/workflows/documentation-testing.yml`, job
   `conformance-artifact-consistency` (lines 734-751): step "Rebuild
   conformance artifacts" runs `python
   scripts/run_cvf_cross_extension_conformance.py` (line 747); step "Enforce
   conformance artifact consistency" runs
   `governance/compat/check_conformance_artifact_consistency.py --enforce`.
2. `scripts/run_cvf_cross_extension_conformance.py` line 20 declares
   `SCENARIO_REGISTRY = REPO_ROOT / "docs/reference/CVF_CONFORMANCE_SCENARIOS.json"`;
   `_load_scenarios` (lines 203-218) reads every record in the registry's
   `scenarios` array; `main`/`_run` (lines 372-397) subprocess-executes each
   scenario's `command`.
3. A fresh JSON parse of `docs/reference/CVF_CONFORMANCE_SCENARIOS.json` at
   this audit's `executionBaseHead` confirms 84 total scenario records, of
   which exactly 9 (`CF-076` through `CF-084`, lines 532-611) each carry a
   `command` of the exact shape `["python",
   "scripts/run_cvf_packet_posture_gate_conformance.py", "--gate",
   "governance/compat/<checker>.py"]`, and the 9 named checkers are exactly
   the 9 deep-chain cross-family files - a verified 1:1 mapping.
4. `scripts/run_cvf_packet_posture_gate_conformance.py` `main` (lines 42-56)
   requires `--gate`, resolves it to an absolute path, and subprocess-runs
   that gate script with `--packet` against four canonical packet postures
   (`PACKETS` tuple, lines 17-22).

This confirms a real, data-driven, parameterized execution edge from CI
through a JSON registry through a generic gate runner to each of the nine
checkers. `governance/compat/check_conformance_artifact_consistency.py`
(module constants, lines 19-21) further enforces that the scenario registry
stays mutually consistent with a generated Markdown report and JSON summary
whenever the CI job runs.

Historical evidence, per checker (not only an aggregate Wave 1 PASS): each of
the 9 checkers has its own dedicated batch section in
`docs/reviews/cvf_phase_governance/CVF_CONFORMANCE_TRACE_2026-03-07.md`
recording (a) the registry line range in
`docs/reference/CVF_CONFORMANCE_SCENARIOS.json` where its `scenarioId` record
lives, (b) the trace batch heading/line where that specific checker was added
and wired into the packet-posture gate path, and (c) a `scenarioCount`-tagged
`authoritative Wave 1 overall result -> PASS` line recorded at the point in
history when that checker's scenario was included - not merely the final
`scenarioCount = 84` aggregate line reused for all nine:

| Checker (scenario ID) | Registry lines (`CVF_CONFORMANCE_SCENARIOS.json`) | Trace batch addition line | Trace per-checker historical PASS line |
|---|---|---|---|
| `check_..._authority_attestation_verification.py` (CF-076) | 532-537 | 488 | 504 (`scenarioCount = 76`) |
| `check_..._authority_provenance_verification.py` (CF-077) | 539-544 | 511 | 527 (`scenarioCount = 77`) |
| `check_..._authority_provenance_attestation_verification.py` (CF-078) | 546-551 | 534 | 550 (`scenarioCount = 78`) |
| `check_..._authority_provenance_attestation_freshness.py` (CF-079) | 553-558 | 557 | 573 (`scenarioCount = 79`) |
| `check_..._authority_provenance_attestation_provenance.py` (CF-080) | 560-565 | 580 | 596 (`scenarioCount = 80`) |
| `check_..._authority_provenance_attestation_provenance_verification.py` (CF-081) | 567-572 | 603 | 619 (`scenarioCount = 81`) |
| `check_..._authority_provenance_attestation_provenance_freshness.py` (CF-082) | 574-579 | 626 | 642 (`scenarioCount = 82`) |
| `check_..._authority_provenance_attestation_provenance_freshness_proof.py` (CF-083) | 581-586 | 649 | 665 (`scenarioCount = 83`) |
| `check_..._authority_provenance_attestation_provenance_freshness_proof_verification.py` (CF-084) | 588-594 | 672 | 688 (`scenarioCount = 84`) |

All nine checker file paths under `governance/compat/` were re-confirmed
present at this audit's `executionBaseHead` by direct filesystem check
(full names omitted from the table for width; each is
`check_cross_family_approval_artifact_external_revocation_issuer_proof_authority_...py`
with the suffix shown in the table's Checker column). Each row's Trace batch
addition line and per-checker historical PASS line is a distinct citation
into `CVF_CONFORMANCE_TRACE_2026-03-07.md`, not a single reused aggregate
line - satisfying a per-checker (not only overall-Wave) historical evidence
requirement.

The trace document's own Status line (line 5) declares it a "local-only
conformance trace for W2 remediation" - this is historical, textual evidence
of past per-checker and aggregate PASS results, not a live current-run
receipt. The generated JSON summary that the runner would produce on a fresh
run
(`docs/reviews/cvf_phase_governance/CVF_CROSS_EXTENSION_CONFORMANCE_SUMMARY_2026-03-07.json`)
is absent from the working tree at this audit's `executionBaseHead`, because
it is a build artifact regenerated at CI/local run time, not committed
source. This is recorded as a declared exclusion in the corpus completeness
block, not as a missing-evidence finding.

Lifecycle disposition (not reopened, not re-decided): the nine checkers carry
`RETIREMENT_HOLD_SOURCE_GAP` from
`docs/reference/CVF_MSEA_R72F_FIRST_RETIREMENT_OR_CONSOLIDATION_PILOT_DECISION_MATRIX_2026-07-08.md`
Decision Matrix, which is the later governed decision superseding R72B's
earlier `R72F_RETIREMENT_REVIEW_CANDIDATE` classification. Execution-edge
existence (now confirmed) and retirement-safety (already held, separately
decided) are distinct questions; this audit does not convert the hold into a
different disposition.

Contradiction note: a temporary, non-CVF advisory report (read only as
advisory input per work order, located under the operator advisory
directory) had earlier concluded these nine checkers carried no execution
edge, because its scan matched only literal `check_*.py` filename tokens in
`governance/compat/*.py`, `scripts/*.py`, and `.github/workflows/*` source
text and did not parse the JSON scenario registry's `command` arrays. This
audit's fresh, CVF-source-only recomputation corrects that prior temporary
finding per authority precedence (current source and canonical contracts
outrank temporary/provider-specific material, per work-order Authority
Chain). See Contradiction Ledger entry CL-02.

Verdict for this lane: `PROVEN_CONNECTED_VIA_DATA_DRIVEN_REGISTRY`.

### Lane 4 - Enforcement to evidence (twelve candidates)

All twelve prior path candidates were recomputed fresh at this audit's
`executionBaseHead` by direct filesystem checks and archive-sibling search,
not carried forward from any prior report. The count matches the work
order's "twelve prior path candidates" exactly: eleven `STALE_ARCHIVE_MOVE`
and one confirmed `MISSING`.

| ID | Citing document (line) | Cited path | Disposition | Successor |
|---|---|---|---|---|
| EPD-01 | Governance Control Matrix (54) | `docs/roadmaps/CVF_RESTRUCTURING_ROADMAP_2026-03-21.md` | STALE_ARCHIVE_MOVE | `docs/roadmaps/archive/...` |
| EPD-02 | Operational Reference Index (22) | `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md` | STALE_ARCHIVE_MOVE | `docs/audits/archive/...` |
| EPD-03 | Operational Reference Index (23) | `docs/reviews/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md` | STALE_ARCHIVE_MOVE | `docs/reviews/archive/...` |
| EPD-04 | Operational Reference Index (24) | `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` | STALE_ARCHIVE_MOVE | `docs/reference/archive/...` |
| EPD-05 | Operational Reference Index (25) | `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md` | STALE_ARCHIVE_MOVE | `docs/roadmaps/archive/...` |
| EPD-06 | Operational Reference Index (38) | `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` | STALE_ARCHIVE_MOVE | `docs/reference/archive/...` (duplicate of EPD-04 target) |
| EPD-07 | Operational Reference Index (38) | `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md` | STALE_ARCHIVE_MOVE | `docs/audits/archive/...` (duplicate of EPD-02 target) |
| EPD-08 | Operational Reference Index (41) | `docs/reference/CVF_QWEN3_HOSTED_PROOF_PREREQUISITES_2026-05-23.md` | STALE_ARCHIVE_MOVE | `docs/reference/archive/...` |
| EPD-09 | Operational Reference Index (41) | `docs/reviews/CVF_D10_QWEN3_R1_COMPATIBLE_HOSTED_PROOF_COMPLETION_2026-05-23.md` | STALE_ARCHIVE_MOVE | `docs/reviews/archive/...` |
| EPD-10 | Operational Reference Index (46) | `docs/work_orders/CVF_WO_AIF_C_MEMORY_GATEWAY_PHASE2_2026-05-23.md` | STALE_ARCHIVE_MOVE | `docs/work_orders/archive/...` |
| EPD-11 | Operational Reference Index (47) | `docs/work_orders/CVF_WO_AIF_B_GRAPH_KNOWLEDGE_PHASE1_2026-05-23.md` | STALE_ARCHIVE_MOVE | `docs/work_orders/archive/...` |
| EPD-12 | Operational Reference Index (58) | `docs/reviews/CVF_H2_WORKING_MEMORY_RUNTIME_PROOF_COMPLETION_2026-05-22.md` | **MISSING** | none found |

EPD-12 was confirmed genuinely missing by a full-repository basename search
(`find -iname`), not only an archive-sibling check: no file with this
basename exists anywhere in the repository, active or archived. A sibling
artifact (`CVF_T5_RUNTIME_MEMORY_WIRING_COMPLETION_2026-05-22.md`) does exist
in `docs/reviews/archive/`, but it is a distinct file cited separately by the
same lookup-table row, not a renamed copy of the H2 file.

Verdict for this lane: `TWELVE_OF_TWELVE_DISPOSITIONED`. Eleven citing
documents need a one-line path correction to their archive-qualified
location (owner action, not executed by this audit per Forbidden Scope);
`CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` should either remove its
`CVF_H2_WORKING_MEMORY_RUNTIME_PROOF_COMPLETION_2026-05-22.md` citation or
have that artifact re-created by its original owner (also an owner action).

### Lane 5 - Evidence to operator surface

Two enforcement classes (`docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
Enforcement Classes table) have materially different operator-surface
maturity. This lane was recomputed directly against
`governance/compat/run_agent_autorun_workflow_gate.py`,
`governance/compat/run_local_governance_hook_chain.py`,
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/operations/page.tsx`,
and
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts`,
distinguishing three separate claims that must not be collapsed into one:

**(a) CLI aggregate/per-check output exists.** Confirmed by direct source
read: `run_agent_autorun_workflow_gate.py` line 74 prints
`[{status}] {result.name} ({result.duration_s:.2f}s)` per configured command
(`status` is `PASS`/`FAIL` from `result.returncode`), giving one
human-readable line per checker in a phase run, plus an aggregate summary.
`run_local_governance_hook_chain.py` lines 195-196 print a
`status = "PASS" if result.returncode == 0 else "FAIL"` line per hook-chain
step (`[CVF hook] START [{index}/{total}] {label}` framing at line 144), and
line 267 prints an aggregate `All {args.hook} governance checks passed.`
line. Both CLIs give real per-checker PASS/FAIL text, not merely a final
aggregate.

**(b) Web Operations exposes a subset, not the full 186.** Direct source
read of `web-governance-jobs.ts` confirms a `GovernanceJobType` union
(lines 16-21) of
exactly 5 job kinds: `cvf_doctor`, `provider_check`, `docs_governance_check`,
`release_gate_dry_readiness`, `full_live_release_gate`. The
`docs_governance_check` job (lines 154-160) is traced to its own single
`buildArgv`: `['governance/compat/check_docs_governance_compat.py', '--base',
'HEAD~1', '--head', 'HEAD', '--json']` - **one** named checker, not a
loop over the 186 `governance/compat/check_*.py` files. `release_gate_dry_readiness`
and `full_live_release_gate` (lines 161-174) invoke
`scripts/run_cvf_release_gate_bundle.py`, a bundle script, not a
per-checker enumeration in this job definition itself - this audit did not
trace how many individual checkers that bundle script internally runs or
whether its output is surfaced per-checker in the Operations page UI; that
would require reading the bundle script and the page's rendering of its
JSON output, which is out of this bounded pass. The Operations page
(`operations/page.tsx`) itself was confirmed to reference these same job
type strings (`docs_governance_check` and related identifiers), consistent
with the job registry it calls.

**(c) A unified Web inventory/readout of all 186 checkers is NOT proven.**
No file in this manifest shows the Web UI iterating
`governance/compat/check_*.py` as a full directory listing, nor rendering a
per-checker table for all 186 scripts. The existence of a `/governance`
route directory (RUNTIME_GUARD-class UI, GC-001..GC-014, confirmed present
at
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance`)
is a separate claim from "the 186 CI_REPO_GATE-class checkers have a unified
Web surface" - this audit does not infer the latter from the former. The
data source for any given Web governance job is traced explicitly above
(job registry -> `buildArgv` -> named script/checker path); no claim in this
audit asserts GC-001 through GC-014, nor the 186 `governance/compat`
checkers as a whole, are fully surfaced in the Web UI beyond what (a)/(b)
trace.

`scripts/cvf_doctor.py` (`main`, lines 203-227) is a genuine CLI
human-readable operator readout, printing a `CVF Doctor: <status>` line, one
line per check, and remediation hints - but this audit did not confirm it
surfaces the 186 `governance/compat` checkers specifically rather than a
separate workspace-health check set; that would require reading the checks
it wires internally, which is out of this bounded pass.

`EXTENSIONS/CVF_v1.7.2_SAFETY_DASHBOARD` was confirmed present but a grep
across its `app/` and `components/` directories for `governance/compat`,
`check_cross_family`, or `autorun-receipts` returned zero matches, confirming
this dashboard is not wired to the CI_REPO_GATE checker class this audit
traces.

Verdict for this lane: `PARTIAL_OPERATOR_VISIBILITY_BY_ENFORCEMENT_CLASS`.
CLI aggregate/per-check human-readable output is proven for both the
autorun gate and the hook chain (claim a). Web Operations exposes a
5-job-type subset with exactly one named `governance/compat` checker wired
directly into a job definition (`docs_governance_check` ->
`check_docs_governance_compat.py`), with the two release-gate job types
delegating to a bundle script this audit did not trace further (claim b). A
unified Web inventory/readout across all 186 `governance/compat` checkers is
explicitly NOT established by this audit and must not be inferred from the
presence of the `/governance` route directory alone (claim c).

## Risk / Corrective Action

| Risk | Corrective action owner | Action |
|---|---|---|
| GC-019 control-matrix row cites a stale active-path roadmap link | reviewer/closer or a later fresh work order | one-line path correction to `docs/roadmaps/archive/CVF_RESTRUCTURING_ROADMAP_2026-03-21.md`; not executed by this audit (forbidden scope: no runtime/source/checker edit) |
| Ten distinct stale citations in `CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` (EPD-02 through EPD-11) | reviewer/closer or a later fresh work order | batch path correction to archive-qualified locations |
| One confirmed-missing citation (`CVF_H2_WORKING_MEMORY_RUNTIME_PROOF_COMPLETION_2026-05-22.md`, EPD-12) in the same index | operator or original artifact owner | either recreate the artifact from its recorded source, or remove the citation and replace with the still-present sibling `CVF_T5_RUNTIME_MEMORY_WIRING_COMPLETION_2026-05-22.md` if it is judged an equivalent substitute |
| Four coexisting, non-cross-referenced layer/architecture numbering schemes | operator decision (not this audit) | decide whether `ARCHITECTURE.md`, `CVF_ARCHITECTURE_DIAGRAMS.md`, and `CVF_CORE_KNOWLEDGE_BASE.md` should cite the doctrine L0-L6 model explicitly, or remain intentionally independent narrations; this audit takes no position beyond recording the drift |
| CI_REPO_GATE-class checker evidence (186 checkers, including the 9 cross-family checkers) has CLI human-formatted per-checker readout (autorun gate, hook chain) but no unified Web per-checker readout beyond the single `docs_governance_check` job | operator decision (not this audit; explicitly forbidden: no maintenance/freshness implementation in this tranche) | any future unified Web readout surface requires a separate, freshly authorized work order |
| Contract-to-runtime lane: 2 of 3 sampled Governance Control Matrix rows (GC-001, GC-009) lack a fully proven source-caller-test match (GC-001's cited test exercises a different source file; GC-009 has no confirmed production caller) | reviewer/closer or a later fresh work order | correct the GC-001 matrix row's test citation to point at the file it actually tests, or add the matching test for the cited source; trace or add a real production caller for `MandatoryGateway`/`createMandatoryGateway`, or downgrade the GC-009 row's enforcement claim; not executed by this audit (forbidden scope: no runtime/source/checker edit) |

## Decision / Recommendation / Disposition

**Audit A verdict: `COMPLETE_WITH_DOCUMENTED_DRIFT`.**

All five chain lanes received a terminal, source-backed disposition:

1. Doctrine to contract - `PARTIAL_CHAIN_WITH_DOCUMENTED_DRIFT`
2. Contract to runtime - `PARTIAL_RUNTIME_CONNECTION_FOR_SAMPLED_ROWS`
   (downgraded from an earlier draft's `PROVEN_CONNECTED_FOR_SAMPLED_ROWS`
   after tracing past file existence to actual caller/test pairing: only
   GC-011 reached a fully proven match; GC-001's cited test exercises a
   different source file, GC-009 has no confirmed production caller)
3. Runtime to enforcement - `PROVEN_CONNECTED_VIA_DATA_DRIVEN_REGISTRY`
   (reclassified from the prior temporary report's incorrect
   no-execution-edge finding)
4. Enforcement to evidence - `TWELVE_OF_TWELVE_DISPOSITIONED` (11
   stale-archive-move, 1 confirmed missing)
5. Evidence to operator surface -
   `PARTIAL_OPERATOR_VISIBILITY_BY_ENFORCEMENT_CLASS` (CLI per-checker
   readout proven for both the autorun gate and hook chain; Web exposes a
   5-job-type subset with exactly one named `governance/compat` checker
   wired directly in; a unified Web readout across all 186 checkers is not
   established)

No lane returned an unresolved or unclassifiable edge; no debt or governance
hold was converted into a "confirmed broken chain" claim. The nine
cross-family checkers keep their existing `RETIREMENT_HOLD_SOURCE_GAP`
lifecycle disposition unchanged.

This audit does not authorize Deliverable B, a maintenance/freshness
mechanism, repository cleanup, checker/runtime/hook edits, or any lifecycle
re-decision. Those corrective actions require separate, freshly authorized
work.

## Corpus Completeness And Report Integrity

- Corpus task class: BOUNDED_REPOSITORY_SYSTEM_CHAIN_AUDIT.
- Corpus root: the 31-path source manifest recorded in the JSON companion's
  `sourceManifest` array, drawn from the work order's Required First Reads
  plus the source files each chain edge cites.
- Snapshot time: 2026-07-10T12:58:41Z, `executionBaseHead b6cba5924`.
- Enumeration command: `filesystem-backed direct file reads` plus targeted
  `find`/`grep`/`python -c json.load` commands per source, recorded per-edge
  in the JSON companion.
- Manifest artifact or inline manifest: `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json`
  `sourceManifest`.
- Manifest hash: `sha256:98fc0f14315c51e717ed9dacc23e9b1dd4c14438feb42353a9ef81558926181b`,
  computed deterministically over the 31 `sourceManifest` entries in their
  declared array order, normalized as one path per line (UTF-8, LF line
  endings, no trailing whitespace per line, single trailing newline), via
  `hashlib.sha256(normalized_manifest.encode("utf-8")).hexdigest()`. Every
  `manifestRecords` entry in the JSON companion carries this same hash under
  `manifestHash` for direct reconciliation.
- Processing ledger artifact or inline ledger: the same JSON companion's
  `chainEdges`, `pathDispositions`, and `manifestRecords` arrays; each
  `manifestRecords` entry carries its own per-path terminal status.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE. Observed in this audit: READ (all 31 manifest
  sources, one `terminalStatus: READ` record per path in the JSON
  companion's `manifestRecords` array); SKIPPED_WITH_REASON, DEFERRED, and
  BLOCKED_UNREADABLE were not needed because every manifest source was
  directly readable and in scope.
- Reconciliation: manifest=31, ledger_terminal=31, exclusions=3, unresolved=0.
- Unresolved files: 0.
- Declared exclusions: the legacy-reference mirror path `private-reference /
  legacy / CVF_Restructure / CVF_ECOSYSTEM/` (searched for existence only,
  not treated as current authority); the
  CI-generated conformance summary JSON (absent from the working tree by
  design, regenerated at CI runtime); external Document Translator and
  Policy_Local source trees (out of this audit's scope, per work order
  forbidden paths).
- Unreadable or unsupported files: 0.
- Aggregation check: Markdown chain-lane verdicts and JSON `chainEdges`
  array agree on all 5 `chainLink` identifiers and their verdict fields;
  Markdown's 12-row evidence table and JSON `pathDispositions` array agree
  on all 12 `id` values and dispositions; Markdown's corpus-completeness
  manifest count (31) and JSON `sourceManifest`/`manifestRecords` array
  lengths (31 each) agree.
- Drift check: all citations re-derived fresh at `executionBaseHead
  b6cba5924`; none reused from a prior report without independent
  recomputation. This repair pass re-verified the manifest count by direct
  `len()` count of the JSON array (31, not the prior draft's miscounted 30)
  and recomputed the manifest hash fresh rather than reusing any placeholder
  text.
- Output traceability: every finding in this document maps to a
  `sourceCitations` entry or a `pathDispositions` entry in the JSON
  companion; every manifest path maps to a `manifestRecords` entry.
- Adversarial verification: three governance-control-matrix rows
  independently spot-verified past file-existence to actual caller/test
  pairing (GC-001, GC-009, GC-011; only GC-011 reached a fully proven match,
  see Lane 2 downgrade); the H2 missing candidate independently re-searched
  beyond the archive-only check the prior temporary report used; the
  runtime-to-enforcement chain independently re-derived from the JSON
  registry rather than trusted from any prior report; the manifest count
  and hash were independently recomputed from the JSON array rather than
  copied from the prior draft's incorrect count.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Contradiction Or Gap Disposition

Two contradictions were found and resolved by authority precedence; both are
recorded in the JSON companion's `contradictionLedger` (CL-01, CL-02) and
summarized in Lane 1 and Lane 3 above. Neither contradiction blocks a
terminal verdict for its lane.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| A static reference-only scan of `check_*.py` filename tokens across source files under-detects data-driven, registry-parameterized checker invocation (JSON `command` arrays passed through a generic `--gate` runner) | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON: this is a lesson about the method used by a temporary, non-CVF advisory scan, not a CVF governance rule, checker, or hook gap; no CVF-owned automation exhibited this defect | Next action: none required from this worker-scope audit; no ADIF entry or checker change is proposed. |
| `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` and `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` cite eleven archive-moved paths as active and one path that no longer exists | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Next action: a future evidence-path freshness checker could catch stale citations in these two files automatically; this audit does not implement it (forbidden scope: no maintenance/freshness mechanism in this tranche). |
| File-existence-only sampling for contract-to-runtime rows (GC-001, GC-009, GC-011) initially produced a `PROVEN_CONNECTED_FOR_SAMPLED_ROWS` verdict; tracing to actual caller/invocation route and test pairing found 2 of 3 rows unproven (GC-001's cited test exercises a non-identical source file; GC-009 has no confirmed production caller) | METHOD_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_CANDIDATE | Next action: a future Governance Control Matrix row verifier could require a confirmed caller-site citation (not only a source-file existence check and a same-named test-file existence check) before a row is marked runtime-proven; this audit does not implement it (forbidden scope: no checker/runtime edit in this tranche). |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance audit; public-sync and public claims are
forbidden by the paired work order.

## Epistemic Process Block

### Expected Result / Prediction

At least some current CVF chain edges would be structural, manual,
historical, stale, or absent rather than uniformly machine-connected; prior
scout counts might change under correct authority and data-driven invocation
resolution.

### Evidence Comparison

Confirmed. The doctrine-to-contract lane found two of seven named doctrine
locations absent from the active tree and three parallel non-doctrine module
maps. The enforcement-to-evidence lane found eleven stale citations and one
genuinely missing artifact. The runtime-to-enforcement lane's prior scout
count (an incorrect "no execution edge" finding for the nine cross-family
checkers) changed materially once the JSON scenario registry was parsed as a
data source rather than searched as literal text - confirming the prediction
that correct authority and data-driven invocation resolution would move the
prior counts.

### Claim Update

The prior temporary advisory report's runtime-to-enforcement finding for the
nine cross-family checkers is REJECTED and REPLACED by this audit's
`PROVEN_CONNECTED_VIA_DATA_DRIVEN_REGISTRY` verdict. The
`docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`
prior audit's own Claim Boundary (it does not claim every plane is a
complete workflow-chain system) is CONFIRMED and carried forward unchanged;
this audit's doctrine-to-contract and enforcement-to-evidence findings are
consistent with, and extend, that prior audit's caution rather than
contradicting it. The R72F lifecycle decision for the nine checkers is
CONFIRMED unchanged.

## Claim Boundary

This audit maps five CVF system-chain edges to source-backed dispositions at
`executionBaseHead b6cba5924`. It does not certify semantic correctness of
every governed artifact in the repository, does not prove all 50
governance-control-matrix rows are runtime-connected (only 3 were
spot-verified, and of those 3 only GC-011 reached a fully proven
source-caller-test match), does not authorize Deliverable B, a
maintenance/freshness mechanism, repository cleanup, or any
runtime/checker/hook/session-state mutation, and does not reopen, alter, or
re-decide the R72F lifecycle disposition for the nine cross-family checkers.
It does not claim a unified Web inventory/readout exists for all 186
`governance/compat` checkers - only that CLI aggregate/per-check output
exists (autorun gate, hook chain) and that Web Operations surfaces exactly
one named checker (`check_docs_governance_compat.py`) directly in a job
definition, with two other job types delegating to an untraced bundle
script. Corrective actions named in Risk / Corrective Action require
separate, freshly authorized work.
