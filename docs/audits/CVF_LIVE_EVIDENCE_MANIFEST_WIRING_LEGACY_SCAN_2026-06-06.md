# CVF Live Evidence Manifest Wiring Legacy Scan

Memory class: AUDIT_RECORD

Status: BOUNDED_TARGETED_SCAN_COMPLETE

Date: 2026-06-06

## Purpose

Record the bounded legacy scan that informed the release-gate live evidence
manifest wiring. The implementation target is narrow: make release-gate JSON
evidence directly produce a secret-safe manifest with hash, rerun command,
optional HMAC signature, and optional external anchor metadata.

## Decision

Proceed with integrated release-gate manifest wiring and keep legacy-derived
runtime telemetry receipt expansion as a separate GC-018/work-order candidate.
The accepted implementation is evidence packaging only.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---:|---|---|---|
| Release gate has machine-readable JSON payload | `scripts/run_cvf_release_gate_bundle.py` | 323 | `result_payload` | release gate reporting | ACCEPT |
| Release gate now accepts evidence output path | `scripts/run_cvf_release_gate_bundle.py` | 392 | `--output` | CLI parser | ACCEPT |
| Release gate now accepts manifest output path | `scripts/run_cvf_release_gate_bundle.py` | 394 | `--manifest-output` | CLI parser | ACCEPT |
| Release gate requires a concrete output artifact before manifest generation | `scripts/run_cvf_release_gate_bundle.py` | 408 | `parser.error` | CLI parser | ACCEPT |
| Release gate writes the manifest after writing JSON evidence | `scripts/run_cvf_release_gate_bundle.py` | 434 | `write_live_evidence_manifest` | release gate main flow | ACCEPT |
| Manifest builder hashes evidence artifacts | `scripts/build_cvf_live_evidence_manifest.py` | 49 | `sha256` | `file_record` | ACCEPT |
| Manifest builder records repository origin, branch, commit, and dirty status | `scripts/build_cvf_live_evidence_manifest.py` | 63 | `repository` | `build_manifest` | ACCEPT |
| Manifest builder records accepted secret env names without raw key values | `scripts/build_cvf_live_evidence_manifest.py` | 71 | `acceptedSecretEnv` | `build_manifest` | ACCEPT |
| Manifest builder supports external anchor metadata | `scripts/build_cvf_live_evidence_manifest.py` | 79 | `externalAnchor` | `build_manifest` | ACCEPT |
| Manifest builder supports optional HMAC signature | `scripts/build_cvf_live_evidence_manifest.py` | 92 | `signature` | `build_manifest` | ACCEPT |
| Scheduled smoke workflow uses integrated release-gate manifest output | `.github/workflows/cvf-scheduled-live-governance-smoke.yml` | 70 | `run_cvf_release_gate_bundle.py` | GitHub Actions workflow | ACCEPT |
| Canonical standard documents integrated release-gate manifest command | `docs/reference/CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026-06-06.md` | 28 | `canonical integrated command` | live evidence manifest standard | ACCEPT |

## Legacy Scan Scope

Targeted query class: receipt, evidence, audit, replay, rerun, signature, HMAC,
anchor, provenance, manifest, immutable, verify, and verification.

The scan was intentionally bounded to evidence/rerun value for the live
manifest lane. It was not a full legacy absorption pass.

## Legacy Value Disposition

| Legacy source | Evidence pointer | Accepted value | Disposition |
|---|---:|---|---|
| `.private_reference/legacy/CVF 16.5/tolaria/CVF_KNOWLEDGE_PROVENANCE_RECEIPT.md` | 29, 55, 56, 98, 104 | Governed knowledge/evidence use should have a receipt-like artifact with source path/hash and replay independence. | ACCEPT |
| `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_AUDIT_RECEIPT.md` | 6, 12, 19, 20, 34, 101 | Agent/run evidence should carry trace identity, status, validation, and output hash concepts. | ACCEPT_BOUNDED |
| `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_LOCAL_TELEMETRY_RECEIPT_SPEC.md` | 6, 12, 21, 22, 145, 149, 157 | Telemetry should support governance, cost, latency, audit receipts, and secret redaction. | DEFER_RUNTIME_SCHEMA |
| `.private_reference/legacy/CVF ADD/cortex-hub/CVF_CORTEX_TRACE_AND_AUDIT_MODEL.md` | 17, 18, 77, 79, 80, 81, 83, 106, 109 | Audit evidence should be replay-safe and preserve request/result/packaging/final-action lineage. | ACCEPT_BOUNDED |

## Verification

- `python -m py_compile scripts/run_cvf_release_gate_bundle.py scripts/build_cvf_live_evidence_manifest.py`: PASS.
- `python scripts/run_cvf_release_gate_bundle.py --dry-run --json --output <temp>/result.json --manifest-output <temp>/manifest.json | python -m json.tool`: PASS.
- Manifest content assertions for schema, evidence sha256, rerun command, and signature status: PASS.
- `python governance/compat/check_finding_to_governance_learning.py --enforce`: PASS for the new audit; broad range includes existing repository history.
- `python governance/compat/check_corpus_completeness_report_integrity.py --enforce`: PASS for the new audit after schema repair; broad range retains three pre-existing out-of-batch violations.

## Knowledge Absorption Blind-Spot Control Block

Prior absorption evidence resolved:

- Current live evidence manifest standard exists at
  `docs/reference/CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026-06-06.md`.
- Current manifest builder exists at `scripts/build_cvf_live_evidence_manifest.py`.
- Scheduled smoke workflow exists at
  `.github/workflows/cvf-scheduled-live-governance-smoke.yml`.
- External review gap remediation already identified signed receipts,
  immutable anchor, and third-party rerun as high-value auditability gaps.

Detailed source reads completed:

- READ_DEEP:
  `.private_reference/legacy/CVF 16.5/tolaria/CVF_KNOWLEDGE_PROVENANCE_RECEIPT.md`
- READ_DEEP:
  `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_AUDIT_RECEIPT.md`
- READ_DEEP:
  `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_LOCAL_TELEMETRY_RECEIPT_SPEC.md`
- READ_DEEP:
  `.private_reference/legacy/CVF ADD/cortex-hub/CVF_CORTEX_TRACE_AND_AUDIT_MODEL.md`

Normalization decision:

- Accepted now: output artifact hash, rerun command, repo commit, dirty status,
  accepted secret env names, optional HMAC signature, and optional external
  anchor metadata.
- Deferred: runtime receipt schema expansion, trace IDs, provider latency/cost
  telemetry, and learning-plane telemetry routing.
- Rejected for this batch: any claim that HMAC alone proves third-party
  immutable anchoring.

Adversarial role review:

- Reviewer: integrated wiring must not alter governance behavior or turn a mock
  run into release-quality proof. Verdict: satisfied by retaining existing
  live-gate semantics and by documenting claim boundaries.
- Security: manifest must not print or persist raw provider keys. Verdict:
  satisfied by storing accepted env names only and using `CVF_AUDIT_SIGNING_KEY`
  only from process environment.
- Evidence reviewer: if manifest output is requested, the evidence file must
  exist. Verdict: satisfied by requiring `--output` before
  `--manifest-output`.

Blind-spot delta:

- Reduced: release-gate result artifacts can now be paired with reproducible
  hash/rerun evidence without a separate manual command.
- Remaining: richer runtime telemetry receipts need a separate GC-018 work
  order because current release-gate checks do not expose cost/latency/trace
  schema fields.

## Corpus Completeness And Report Integrity

- Corpus task class: targeted legacy evidence/rerun value scan.
- Corpus root: `.private_reference`
- Snapshot time: 2026-06-06 local workspace snapshot.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference | rg -i "(receipt|evidence|audit|replay|rerun|signature|hmac|anchor|provenance|manifest|immutable|verify|verification)"`
- Manifest artifact or inline manifest: inline query-bounded source list in the Processing ledger below.
- Manifest hash: N/A with reason; query output was used inline and no separate manifest file was produced for this bounded scan.
- Processing ledger artifact or inline ledger: inline ledger below.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline query-bounded list; ledger_terminal=READ/DEFERRED; exclusions=declared; unresolved=1.
- Unresolved files: 1
- Declared exclusions: other query hits outside the four evidence/rerun owner files, non-evidence legacy material, binaries, unrelated UI/provider sources, and full legacy corpus semantics.
- Unreadable or unsupported files: none encountered in the four READ_DEEP files.
- Aggregation check: PASS for the four accepted/deferred files listed in the ledger.
- Drift check: PASS for local snapshot on 2026-06-06; future agents must rerun enumeration before expanding the scan.
- Output traceability: accepted values are mapped in the Legacy Value Disposition table.
- Adversarial verification: implementation avoided new runtime schema claims and records telemetry schema expansion as a separate work-order candidate.
- Corpus verdict: PARTIAL

| File | Processing status | Disposition |
|---|---|---|
| `.private_reference/legacy/CVF 16.5/tolaria/CVF_KNOWLEDGE_PROVENANCE_RECEIPT.md` | READ | Accepted for manifest evidence principles |
| `.private_reference/legacy/CVF 16.5/Claude Kit/CVF_AGENT_AUDIT_RECEIPT.md` | READ | Accepted bounded for run receipt principles |
| `.private_reference/legacy/CVF 16.5/OpenAgentd/CVF_LOCAL_TELEMETRY_RECEIPT_SPEC.md` | READ | Deferred for runtime telemetry schema work |
| `.private_reference/legacy/CVF ADD/cortex-hub/CVF_CORTEX_TRACE_AND_AUDIT_MODEL.md` | READ | Accepted bounded for replay-safe lineage |
| Other query hits | DEFERRED | Outside evidence-manifest lane |

## Rescan Intelligence Hardening

- Original source artifact: `.private_reference` targeted query results for evidence/rerun terms.
- Predecessor intake artifact: `docs/audits/CVF_P1_P5_SMALL_DEBT_REMEDIATION_AUDIT_2026-06-06.md` and `docs/reference/CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026-06-06.md`.
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS.
- Routing matrix status: COMPLETE_WITH_DECLARED_LIMITS.
- Semantic sampling status: COMPLETE_WITH_DECLARED_LIMITS.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Source | Delta | Disposition |
|---|---|---|---|
| UNCHANGED_FROM_INTAKE | Existing manifest standard | Hash/rerun/HMAC/anchor boundary already existed. | RESOLVED_BY_DESIGN |
| CHANGED_DISPOSITION | Release-gate bundle | Manifest builder moved from separate workflow step to integrated CLI option. | DO_NOW |
| NEW_FINDING | Legacy receipt files | "No receipt/no governed use" strengthens canonical release-gate manifest usage. | DO_NOW |
| REMOVED_OR_REJECTED | Runtime telemetry fields | Cost/latency/trace receipt schema is valuable but outside this batch. | SEPARATE_RUNTIME_TRANCHE |

### Follow-Up Routing Matrix

| Lane | Routed item | Disposition |
|---|---|---|
| DO_NOW | Integrated release-gate result and manifest command. | Implemented in this batch |
| SEPARATE_RUNTIME_TRANCHE | Runtime telemetry receipt expansion for cost/latency/trace fields. | Future GC-018/work order |
| STRATEGIC_OPERATOR_DECISION | External immutable anchor provider selection. | Operator/product decision |
| OUT_OF_SCOPE | Public-sync publication of private legacy audit details. | Excluded |
| RESOLVED_BY_DESIGN | HMAC remains optional and secret-safe. | Covered by existing builder |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LESM-001 | Knowledge provenance receipt | Evidence should carry source path/hash and remain replay-independent. | ACCEPT_BOUNDED | Does this require new runtime receipt fields now? | PASS: no, release-gate manifest covers file hash/rerun only. |
| LESM-002 | Local telemetry receipt spec | Cost/latency should be visible for review. | DEFER_RUNTIME_SCHEMA | Does this batch falsely claim cost telemetry? | PASS: no, deferred to separate GC-018. |
| LESM-003 | Cortex trace/audit model | Audit replay should preserve lineage. | ACCEPT_BOUNDED | Does the manifest claim full trace replay? | PASS: no, command/hash replay only. |

## Finding-To-Governance Learning Disposition

- Defect class: auditability gap in live evidence packaging.
- Learning lane: governance/control-plane learning.
- Escalation state: STANDARD_UPDATED and MACHINE_CHECK_CANDIDATE.
- Next control action: keep integrated `--output` plus `--manifest-output` in
  release-gate usage; consider a future guard that warns when live release
  artifacts are committed or published without a matching manifest.
- Worker-blame disposition: N/A with reason; the gap was structural because the
  manifest builder existed but was not wired into the canonical release-gate
  command.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this audit cites private legacy paths under `.private_reference/`.
Public export may cite only the public-safe standard, workflow behavior, and
manifest schema, not private provenance file contents.

## Claim Boundary

This audit supports a bounded release-gate evidence packaging improvement. It
does not close runtime telemetry receipt expansion, independent third-party
anchoring, production readiness, public certification, or full legacy
absorption.
