# CVF GC-018 Baseline - PINT-R1 Full Corpus Content Rescan And MCP Value Reconciliation

Memory class: POINTER_RECORD

Status: DISPATCH_READY

docType: baseline

Batch ID: PINT-R1

Dispatch base head: 23f4e1657

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer/closer: independent reviewer/closer

Worker target: delegated documentation worker

## Purpose

Authorize one bounded, documentation-only rescan of every file under
`.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE`. The tranche must recover
useful knowledge missed by the earlier representative scan, especially from
`docs/absorptions`, without claiming that the corpus is sufficient to build an
MCP/CLI control runtime.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id PINT-R1 --title "Provider Intelligence Full Corpus Content Rescan And MCP Value Reconciliation" --date 2026-07-23 --base 23f4e1657 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all scaffold placeholders with current corpus, owner, handoff, rescan, and claim-boundary evidence |
| checkerReadAheadConfirmation | corpus, absorption, rescan, work-order, handoff, trace, prompt-envelope, and ADIF checker sources |
| docOnlyNewFields | per-file semantic locator, extracted delta, EAIC relevance, actual-usage distinction, receipt-layer disposition |
| claimBoundary | dispatch evidence only; no runtime, provider, live, public, package, or MCP/CLI behavior claim |

## Authorization / Decision

Operator instruction on 2026-07-23 authorizes a careful file-content rescan and
knowledge absorption. It explicitly accepts partial knowledge gain and does not
authorize premature MCP/CLI runtime construction.

Decision: `AUTHORIZE_PINT_R1_FULL_FILE_CONTENT_RESCAN_ONLY`.

## Scope / Methodology

The bounded source root contains 50 files: 31 Markdown, 7 JSON, 6 Python, and 6
Python bytecode files. Filesystem enumeration must include hidden and ignored
paths. Every file receives one terminal ledger row. The 44 non-bytecode files
must be opened or parsed. The six bytecode files must be inventoried and
terminally classified as generated artifacts; decompilation is not required
because matching readable Python source or test files exist.

The prior PINT-T0 through PINT-T3 artifacts remain accepted predecessor
evidence. This successor rescan does not reopen the rejected direct-import,
static-checker, or runtime lanes. It tests whether the complete current corpus
adds bounded doctrine or sharper knowledge-gap evidence.

## Corpus Accounting Target

| Field | Value |
| --- | --- |
| Corpus root | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE` |
| Filesystem count | 50 |
| Extension totals | Markdown=31; JSON=7; Python=6; Python bytecode=6 |
| Path manifest digest | `f94f8debf9f05021e7898e1e7065f534dcf7e6dfdd2ceb604fb8ff9dc9ae16f7` |
| Content manifest digest | `f76e62ab30ba48997fa8d7cb517247ce2afaa1406c51f0e4c0e97edc9369ed85` |
| Path digest recipe | corpus-relative forward-slash paths, ordinal/code-point sort, UTF-8 without BOM, LF-separated, one trailing LF, SHA-256 |
| Content digest recipe | lowercase SHA-256, two spaces, corpus-relative forward-slash path; rows ordinal/code-point sorted, UTF-8 without BOM, LF-separated, one trailing LF, SHA-256 |
| Required ledger | one row per file; no folder-level substitute |

## Digest Reconciliation Repair

Reviewer recomputation on 2026-07-23 reproduced the recorded canonical values
from the current 50-file corpus:

- path manifest digest:
  `f94f8debf9f05021e7898e1e7065f534dcf7e6dfdd2ceb604fb8ff9dc9ae16f7`;
- content manifest digest:
  `f76e62ab30ba48997fa8d7cb517247ce2afaa1406c51f0e4c0e97edc9369ed85`.

A second implementation using PowerShell `Sort-Object` without an explicit
ordinal comparer produced different path and content digests because its
default ordering is culture-sensitive. That result is non-canonical for this
packet and is not corpus-drift evidence.

The canonical executable recipe is:

```powershell
@'
import hashlib
from pathlib import Path

root = Path(".private_reference/legacy/CVF_PROVIDER_INTELLIGENCE")
files = sorted(
    (path for path in root.rglob("*") if path.is_file()),
    key=lambda path: path.relative_to(root).as_posix(),
)
relative_paths = [path.relative_to(root).as_posix() for path in files]
content_rows = [
    f"{hashlib.sha256(path.read_bytes()).hexdigest()}  "
    f"{path.relative_to(root).as_posix()}"
    for path in files
]
path_payload = ("\n".join(relative_paths) + "\n").encode("utf-8")
content_payload = ("\n".join(content_rows) + "\n").encode("utf-8")
print(f"count={len(files)}")
print(f"pathManifestSha256={hashlib.sha256(path_payload).hexdigest()}")
print(f"contentManifestSha256={hashlib.sha256(content_payload).hexdigest()}")
'@ | python -
```

The script hashes raw file bytes, uses corpus-relative forward-slash paths,
sorts by Python Unicode code-point order, writes LF separators with one
trailing LF, and hashes UTF-8 payloads without a BOM. The worker must use this
script or prove byte-for-byte equivalent ordering and serialization.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Earlier PINT absorption is bounded and closed | VALUE_SET | `docs/roadmaps/CVF_PINT_T0_PROVIDER_INTELLIGENCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | Machine Closure Package | `Status` | PINT roadmap | ACCEPT |
| Provider intelligence remains advisory | VALUE_SET | `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md` | Claim Boundary | provider intelligence advisory | PINT-T2 reference | ACCEPT |
| Static checker lane was closed with no checker now | VALUE_SET | `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | decision and closeout | `CLOSE_PINT_ABSORPTION_LANE_NO_CHECKER_NOW` | PINT-T3 review | ACCEPT |
| EAIC remains knowledge-gap parked | VALUE_SET | `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md` | Position and Inventory Summary | `PARKED_KNOWLEDGE_GAP` | EAIC source-acquisition map | ACCEPT |
| Complete local corpus count is 50 | EXISTS | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE` | recursive filesystem enumeration on 2026-07-23 | corpus root | local retained legacy source | ACCEPT |

## Mandatory Blind-Spot Control Block

ADIF-0014 and ADIF-0019 apply. The worker must not treat a gate pass as proof
that `DEFERRED`, `REJECTED`, or `NO_NEW_VALUE` files lack useful doctrine.
Every file must be content-accounted, and the independent reviewer must audit
all value-bearing dispositions after the worker gates pass.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE` retained legacy folder |
| Enumeration command | `Get-ChildItem -LiteralPath '.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE' -Recurse -File` |
| Manifest artifact or inline manifest | inline Corpus Accounting Target table |
| Processing ledger artifact or inline ledger | inline Corpus Completeness And Report Integrity block |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline Overlap And Novelty Classification table |
| Unresolved items | worker must state exact count and paths |
| Completion claim boundary | bounded documentation absorption only; no runtime/provider/public/production expansion |

## Corpus Completeness And Report Integrity

- Corpus task class: KNOWLEDGE_ABSORPTION.
- Corpus root: `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE`.
- Snapshot time: 2026-07-23 dispatch enumeration.
- Enumeration command: recursive PowerShell filesystem enumeration with
  `-LiteralPath`, `-Recurse`, and `-File`.
- Manifest artifact or inline manifest: required worker audit table.
- Manifest hash: `f94f8debf9f05021e7898e1e7065f534dcf7e6dfdd2ceb604fb8ff9dc9ae16f7`.
- Processing ledger artifact or inline ledger: required worker audit table.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=50; ledger_terminal=0; exclusions=0; unresolved=50.
- Unresolved files: all 50 remain worker-owned before execution.
- Declared exclusions: none.
- Unreadable or unsupported files: none known; bytecode remains visible as
  generated binary evidence.
- Aggregation check: dispatch inventory totals reconcile to 50.
- Drift check: worker must recompute before and after content review.
- Output traceability: one source locator and value disposition per file.
- Adversarial verification: independent reviewer samples all high-value and all
  deferred/rejected/no-new-value groups.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| full corpus content | unreviewed delta beyond predecessor intake | DOCTRINE_ADAPTED | worker audit and existing PINT/EAIC owners | identify only source-backed enrichment | documentation only |
| reusable receipt language | possible future contract vocabulary | PACKAGE_CANDIDATE | conditional reopen index if genuinely novel | retain only with measurable reopen condition | no package activation |
| invocation-control-relevant semantics | possible future runtime input | RUNTIME_CANDIDATE | EAIC knowledge-gap owner | sharpen gap, do not build | runtime moratorium retained |
| prototype checker invariants | possible static-check value | CHECKER_CANDIDATE | PINT-T3 decision owner | preserve only if concrete new invariant exists | no checker edit |
| foreign implementation and OpenRouter dependency | unsafe direct adoption | REJECT_DIRECT_IMPORT | PINT claim boundary | retain contrast value only | no direct import |
| generated or duplicate files | no additional semantic value when proven | NO_PACKAGE_OR_RUNTIME_VALUE | per-file ledger | close with exact reason | no future action |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| advisory provider intelligence | `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md` | CONFIRMED_EXISTING | predecessor doctrine already owns core boundary | verify file by file |
| receipt layers and stale/fail-closed semantics | `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | hidden samples and detailed absorption docs may sharpen boundaries | adapt exact deltas |
| external-agent session usage/control | `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md` | NEW_FINDING | retain only if source supplies a distinct bounded fact | map or park |
| external package and prototype checkers | `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | REJECT_DIRECT_IMPORT | direct adoption remains rejected | preserve CVF-native value only |
| duplicates and bytecode | `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md` | NO_NEW_VALUE | no independent authored knowledge when verified | close per file |

## Rescan Intelligence Hardening

- Original source artifact: `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE`.
- Predecessor intake artifact:
  `docs/roadmaps/CVF_PINT_T0_PROVIDER_INTELLIGENCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`.
- Delta ledger status: worker must classify predecessor overlap and newly
  visible file-level delta.
- Routing matrix status: required in worker audit.
- Semantic sampling status: independent reviewer required.
- Rescan intelligence verdict: PARTIAL

### Original-Intake Delta Ledger

| Current finding | Predecessor finding | Delta class | New disposition | Reason |
| --- | --- | --- | --- | --- |
| 50-file inventory including hidden and binary files | representative PINT-T0 manifest | NEW_FINDING | full file-level rescan | prior evidence did not prove 50-row content coverage |
| core provider-intelligence boundary | advisory owner already absorbed | UNCHANGED_FROM_INTAKE | retain owner | no runtime authority expansion |
| future value dispositions | prior parked runtime/checker lanes | CHANGED_DISPOSITION | only source-backed enrichment may be retained | operator authorized rescan, not implementation |
| direct foreign import | previously rejected | REMOVED_OR_REJECTED | retain rejection | no new authority |

### Follow-Up Routing Matrix

| Finding class | Route | Owner |
| --- | --- | --- |
| documentation delta inside existing owner | DO_NOW | worker audit with reviewer acceptance |
| runtime or checker candidate | SEPARATE_RUNTIME_TRANCHE | conditional reopen index and operator |
| provider/access-mode policy choice | STRATEGIC_OPERATOR_DECISION | operator |
| direct import or unrelated code | OUT_OF_SCOPE | worker records rejection |
| exact duplicate | RESOLVED_BY_DESIGN | existing PINT owner |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| S1 | absorption docs 03-06 | stale, TTL, health, and fail-closed semantics | possible enrichment | is the delta already owned by PINT-T2 or EAIC? | reviewer pending |
| S2 | absorption docs 08-11 and hidden receipts | model selection and receipt layers | possible enrichment | does estimated route usage get confused with actual session quota? | reviewer pending |
| S3 | Python checkers and bytecode | prototype enforcement | direct import rejection | is any concrete invariant novel despite rejecting code import? | reviewer pending |

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | retained legacy copied folder |
| Upstream or source-mirror disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: this is a bounded local knowledge rescan, not an upstream repository claim |
| Enumeration or manifest plan | hidden-aware filesystem enumeration of all 50 files |
| Per-file terminal-ledger plan | exactly one terminal row per manifest item |
| Owner or overlap route | PINT-T2, PINT-T3, EAIC map, or conditional reopen index |
| Value-disposition route | adapt, defer, reject direct import, or close with exact reason |
| Claim boundary | no implementation, provider, network, public, or external invocation |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | retained source -> manifest -> file-level content ledger -> overlap/value conversion -> current owner or conditional park -> reviewer closure |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | inline overlap table and existing PINT/EAIC owners |
| Disposition | ADAPT bounded doctrine; DEFER candidates; REJECT direct import |
| Claim boundary | no runtime/provider/public/production authority |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Knowledge absorption`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: ADIF-0014

Additional closure-semantic query returned: ADIF-0019.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | corpus verdict, terminal status, conversion lane, overlap disposition, rescan delta and routing vocabularies |
| gateRunPurpose | confirm dispatch shape and evidence after source review |
| claimBoundary | structural read-ahead only; semantic completeness remains reviewer-owned |

## Acceptance Criteria

- all 50 files are present in one file-level processing ledger;
- all 44 non-bytecode files are opened or parsed;
- all 16 files under `docs/absorptions/openrouter-provider-intelligence` are
  read individually and cite semantic regions;
- all seven hidden JSON samples are parsed individually;
- all six Python source/test files are read individually;
- all six bytecode files remain visible and receive generated-artifact reasons;
- new value is compared against PINT-T2, PINT-T3, and EAIC owners;
- estimated request-level usage is not promoted into actual session/quota
  measurement evidence;
- no runtime, checker, provider, public, package, CLI/MCP, network, or process
  action occurs;
- worker leaves exactly the allowed outputs unstaged and uncommitted.

## Verification / Evidence

Dispatch evidence is the filesystem-backed 50-file enumeration, two
deterministic manifest digests, source-verification table, ADIF disclosure,
checker read-ahead block, and the pre-dispatch gates. Worker completion
evidence must be command-backed in the audit and worker return; it is not
preclaimed by this baseline.

## Baseline Decision

`DISPATCH_READY_FOR_BOUNDED_DOCUMENTATION_RESCAN`.

This decision does not state that CVF now has enough knowledge to build the
MCP/CLI control runtime. The EAIC parked status and invocation moratorium remain
unchanged unless a later operator-authorized tranche supplies the missing
primary evidence.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | delegated worker reads local corpus and authors governed documents | no commit; no runtime/external action | work order and worker return | parent session only | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | future EAIC owner | no invocation or adapter execution | EAIC knowledge-gap map | explicitly deferred pending primary sources and operator authorization | DEFERRED_WITH_REASON |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance knowledge-absorption dispatch; no public-sync is
authorized.

## Claim Boundary

This baseline authorizes only a full local content rescan and documentation
value reconciliation. It does not authorize runtime construction, CLI/MCP
invocation, provider/API/account use, network access, process control, checker
implementation, package activation, public sync, or a claim that the knowledge
gap is closed.
