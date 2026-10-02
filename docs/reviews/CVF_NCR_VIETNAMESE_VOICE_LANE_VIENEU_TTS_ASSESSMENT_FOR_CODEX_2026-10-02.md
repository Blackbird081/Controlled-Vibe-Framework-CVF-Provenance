# CVF NCR Vietnamese Voice Lane VieNeu-TTS Assessment For Codex

Memory class: FULL_RECORD

Status: LOCAL_CLASSIFIED_ADVISORY_CANDIDATE_UNKNOWN

docType: review_context

Date: 2026-10-02

From: Claude, acting as INTERNAL_AGENT worker (batch CVF-NCR-HYPERFRAMES-REUSE-AUDIT)

To: Codex / Local (owner of classification, any GC-018 and any resulting work order)

EPISTEMIC_PROCESS_NA_WITH_REASON: advisory assessment packet - it reports web-observed, unverified facts and proposes a next scope; it makes no closure claim and updates no source-of-truth state.

## Purpose

Record, at the operator's request, (1) a preliminary assessment of the VieNeu-TTS repository as a Vietnamese voice candidate for the accepted private CVF explainer video, and (2) the operator's design principle for paid or hosted options, so Local can classify both and scope the next packet.

## Operator Request And Work-Order Boundary

This file is OUTSIDE the work order. The work order `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HYPERFRAMES_REUSE_CAPABILITY_AUDIT_2026-10-02.md` allows exactly three worker paths and forbids network use. This fourth path and the read-only network observations below were done only because the operator asked for them directly in the session after the worker return was produced (operator messages: add VieNeu-TTS as a Vietnamese option; paid options must be designed in, not excluded; add an assessment of the new repository and the principle, plus one file for Codex outside the work order, stated as operator-requested and added to CVF).

Consequences, disclosed: the three returned worker documents are unchanged and still describe a three-path manifest; with this file present, the stored static cross-check of the audit evidence will report a manifest difference by design. Local should treat this file as a separate operator-requested artifact, not as part of the audit return. The worker did not edit the roadmap, source-mirror INDEX, continuity or any existing document, and did not commit.

## Target / Source

Candidate: `https://github.com/pnnbao97/VieNeu-TTS.git`. Observations on 2026-10-02 (UTC), all unpinned and web-only: `git ls-remote --symref` HEAD of main `85344322b7258b4e25479b692e8e3396baf9db34` observed at 2026-10-02T16:34:47Z; a page summary of the GitHub README produced by a summarizing tool; a summary of the Hugging Face model card `pnnbao-ump/VieNeu-TTS`; a fetch of the repository LICENSE that failed with HTTP 503. No clone, install, download, model run, script execution or provider call occurred. Related accepted context: the HyperFrames audit return (R05 local Vietnamese narration SOURCE_CONTRADICTED, R06 hosted voice UNKNOWN, case P-08).

## Scope / Methodology

Web-observed claims are classified WEB_SUMMARY_UNVERIFIED, which is weaker than source-read. They were produced by a small summarizing model, not by reading the repository blobs, so wording may be inexact. Nothing here is a source-supported or runtime-supported classification.

## Findings / Position

Reported by the README summary (all WEB_SUMMARY_UNVERIFIED):

| Topic | Reported | Needed before relying on it |
|---|---|---|
| Purpose | Vietnamese (and bilingual) TTS with voice cloning, local processing | read source at a pin |
| Current open model | v3 Turbo, 48 kHz, flow matching, MOSS-Audio-Tokenizer-Nano codec, sea-g2p phonemizer | verify names and versions in source |
| Newer model | v4 reported proprietary, API only through the vendor site | confirm terms and pricing; treat as a hosted option |
| Code license | Apache-2.0 | read LICENSE blob (the fetch failed with 503) |
| Offline use | offline after model download; optional local API server | observe network calls on install and first run |
| CPU | ONNX Runtime CPU path without PyTorch; NVIDIA GPU optional | measure on the Windows host |
| Windows | reported supported, standalone installer mentioned | observe |
| Voices | 25 presets; clone from 3-8 s reference audio | rights of presets; consent rule for cloning |
| Install | `pip install vieneu` or `uv sync` | verify package provenance and dependency set |

Discrepancy to resolve: the Hugging Face model card that was retrieved describes the older 0.5B and 0.3B variants fine-tuned from NeuTTS Air, licensed Apache-2.0, with 3-5 s cloning. It does not describe v3 Turbo. Therefore the license of the v3 Turbo weights, the MOSS codec and the sea-g2p phonemizer is UNVERIFIED, even though the repository code is reported Apache-2.0. Do not infer weight or dependency licenses from the code license.

Preliminary fit against the accepted job (assessment, not proof): a local Vietnamese engine would address the audit's R05 gap. HyperFrames source shows audio clips with a `src` and timing attributes (README composition example uses a WAV file), so a per-scene WAV from any engine is a plausible input; compatibility of a 48 kHz file and of the mixing path is UNKNOWN until observed. Measured speech duration would replace the estimated scene timings. Vietnamese naturalness and diacritic pronunciation are UNKNOWN and need a Vietnamese-speaking listener; static checks cannot judge them.

## Operator Principle: Paid And Hosted Options Are Designed In

Local correction under D100 / canonical section 2.2: preserve applicable local, self-hosted and hosted/paid options for explicit user choice. No production or proof lane is selected here. Local VieNeu is a possible proof candidate because the source addresses Vietnamese WAV generation and offers CPU/ONNX, while actual suitability and compute/download costs remain UNKNOWN; those reasons do not establish a default.

| Lane | Readiness / selection | Reconsideration or selection condition | Required controls |
|---|---|---|---|
| Local VieNeu v3 Turbo | UNKNOWN_RUNTIME; possible proof candidate, not selected | user selects after hardware, rights, implicit downloads and measured cost/quality requirements are scoped | separate code/model/codec/preset pins and rights, consent, rate/channels/duration/hash |
| Self-hosted VieNeu or another voice endpoint | DESIGNED_OPT_IN_NOT_ADMITTED | user identifies endpoint/operator and chooses credential, data, availability and cost envelope | endpoint/runtime identity, transport, retention, secret custody, joined artifact evidence |
| VieNeu v4 or vendor API | DESIGNED_OPT_IN_NOT_ADMITTED; availability/terms/cost UNKNOWN | explicit user selection after current provider terms and egress/budget envelope | budget ceiling, per-call receipt, explicit credential grant, data-egress consent |
| HeyGen voice via HyperFrames | DESIGNED_OPT_IN_NOT_ADMITTED; Vietnamese availability/cost UNKNOWN | user selection after source/provider language, rights and budget evidence | same credential/egress/artifact controls |
| No voice (silent text-only) | alternative reduced artifact, not automatic narrated-job success | explicit user agreement to reduced scope | preserve claim boundary; no narrated-video acceptance |

Controls proposed for any paid or hosted lane: (1) the user or operator selects the lane, the agent applies the selected policy; any fallback must already fit its authorized envelope, otherwise it stops and requests the changed lane/budget/egress authority; (2) sending narration text to a provider is a data-egress effect separate from cost approval; (3) record call count, characters and real cost where available, never an estimate presented as a measurement; (4) credentials come from an explicit grant, not from an ambient `.env` file (the HyperFrames CLI auto-loads `.env` from the working directory); (5) every lane must produce the same contract: one WAV per scene, measured duration, SHA-256, so rendering does not depend on the voice source. Voice cloning of a real person requires that person's written consent; the proof should use preset or synthetic voices only.

This principle is an operator direction stated in the session and recorded here as an advisory boundary only. The lasting rule is now recorded independently in roadmap D100 and canonical section 2.2; this note supplies advisory input and grants no execution permission.

## Proposed Amendments For Local To Consider

1. In the HyperFrames audit disposition, classify P-08 as designed options with readiness, reasons and reconsideration conditions; do not select a proof default. Add the lane table above as the voice-lane contract. Do this by Local review wording or a same-target correction; the worker did not edit the returned documents.
2. Reclassify audit rows R05 and R06 as lane-specific: R05 stays contradicted only for the Kokoro engine; a separate row for the VieNeu local lane stays UNKNOWN pending source and license evidence.
3. Open one source-only packet for VieNeu-TTS in the same shape as the HyperFrames audit: freshness preflight with a fresh `ls-remote` observation and an immutable pin, isolated mirror, root and weight license evidence, selected Git-blob reads (README, LICENSE, package metadata, install and inference entry points, model download code, telemetry or network paths, preset and cloning terms), PARTIAL ledger, requirement fit for R04-R06 and the lane contract, and a smallest-proof plan (one scene voice, CPU, Windows, offline after staging, measured duration, listener review) marked NOT_EXECUTED_PLANNED.
4. Combine the VieNeu proof with the HyperFrames proof in one planned case set (S05 only): VieNeu WAV plus a silent HyperFrames composition, with operator checkpoints before any download or install.

## Risk / Corrective Action

Risks: acting on web summaries as if they were source; assuming v3 Turbo weights share the code license; letting a paid lane become an agent-side fallback; ambient credentials; cloning voices without consent; running install without a checkpoint. Corrective action: Local classifies this packet, then dispatches the source-only packet before any install. No corrective edit was made to returned documents.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input source | operator-named repository URL `https://github.com/pnnbao97/VieNeu-TTS.git`, web observation only |
| Chain map route | operator request -> advisory note -> Local classification -> fresh source-only packet |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | private video design and HyperFrames audit lane |
| Disposition | SOURCE_COMPARISON_RUNTIME_PENDING |
| Claim boundary | web summaries are not CVF proof; no source, runtime or license verification |

## Claim Boundary

Advisory only. Not an audit, not a source-supported or runtime-supported finding, not a license opinion, not an admission of VieNeu-TTS or any paid lane, not a production, voice, render or publication decision, not ratification of the operator principle as CVF policy. The repository was not cloned or run; HEAD was only observed. Worker-session usage and cost are UNKNOWN, not zero.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## External/Local Coordination Binding

Role: shared-workspace `INTERNAL_AGENT`. Phase: operator-requested advisory note outside the work-order manifest. Decision owner: Local.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py` (manifest and trace rules); `governance/compat/check_external_knowledge_intake_routing.py` (input types, binding section); `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Input type`; `External/Local Coordination Binding`; `Agent Operation Trace Block` labels; `Checker Source Read-Ahead Block` fields |
| gateRunPurpose | Confirm the advisory note shape; the exact-manifest check against the work order is expected to flag this file as an operator-authorized addition |
| claimBoundary | Structural gates cannot verify web-observed claims, licenses or runtime behavior. |

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| Defect class | OPERATOR_SCOPE_CLARITY_GAP |
| Learning lane | DOCUMENTATION_ONLY_LEARNING |
| Finding | the audit treated the paid voice lane as excluded; the operator wants paid lanes designed in as opt-in |
| Disposition | N/A_WITH_REASON: wording amendment for Local; no canonical rule or checker change proposed here |
| Next control action | Local decides whether to ratify the opt-in design principle in the roadmap and amend the audit wording |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Internal worker |
| Provider or surface | Shared private CVF workspace; read-only web fetches and `git ls-remote` by operator request |
| Session or invocation | operator-requested VieNeu-TTS assessment note, 2026-10-02 |
| Working directory | Repository root |
| Approval boundary | Operator request in session; advisory only; Local owns classification and commit |
| Invocation ID | cvf-ncr-vieneu-tts-assessment-note-20261002 |
| Expected manifest | this file only (outside the three-path work-order manifest, operator-authorized) |
| Actual changed set | `docs/reviews/CVF_NCR_VIETNAMESE_VOICE_LANE_VIENEU_TTS_ASSESSMENT_FOR_CODEX_2026-10-02.md` |
| Command or tool surface | WebFetch (GitHub page summary, Hugging Face card, LICENSE attempt), `git ls-remote --symref`, file write |
| Target paths | this file only |
| Allowed scope source | operator messages in this session; outside the work-order manifest |
| Before status evidence | three untracked audit paths, HEAD `4870a4c45`, nothing staged |
| After status evidence | four untracked paths, no commit |
| Diff evidence | `git diff --name-status` is empty; `git status --short --untracked-files=all` lists four untracked paths |
| Claim boundary | web observation and assessment only |
| Agent type | INTERNAL_AGENT worker |
| Manifest delta | one path beyond the three-path work-order manifest, operator-authorized, disclosed above |

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. This file is uncommitted; Local owns classification, registration in the roadmap or source-mirror INDEX, and any commit.

## Local Disposition - 2026-10-03

The original web-summary observations above remain historical and unverified. The earlier license discrepancy is not a current finding that v3 has no license declaration: a later Local observation of the v3 Turbo publisher card declares Apache-2.0 for weights/ONNX/presets and states consent; it is unpinned publisher evidence, not independent rights-chain or pinned production clearance. Pinned source observations at 85344322b7258b4e25479b692e8e3396baf9db34 are PARTIAL (3 READ, 142 DEFERRED / 145 paths), preserved in `docs/reviews/evidence/cvf-ncr-hyperframes-vieneu-local-review-2026-10-03.json`. They identify unpinned model/codec retrieval, possible preset override, denoiser retrieval, incomplete public codec_dir forwarding and GPU remote-code loading. No runtime was executed.

Root selector is operator; downstream selector is project owner within granted authority. Local classifies VieNeu as a candidate UNKNOWN_RUNTIME, records the existing mirror without refreshing or executing it, and accepts this note only as historical advisory plus explicitly marked Local corrections. No worker redispatch, voice clone, model download, paid call or production default follows. Closure authority: `docs/reviews/CVF_CVF_NCR_HYPERFRAMES_REUSE_CAPABILITY_AUDIT_COMPLETION_2026-10-03.md`.
