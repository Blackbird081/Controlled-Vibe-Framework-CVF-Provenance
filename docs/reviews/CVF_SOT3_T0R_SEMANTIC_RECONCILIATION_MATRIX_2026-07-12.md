# CVF SOT3-T0R Semantic Reconciliation Matrix

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: review_context

Date: 2026-07-12

Matrix ID: SOT3-T0R-MATRIX

## Purpose

Independent semantic re-audit of the SOT3-T0 advisory evidence. Deeply re-reads
all 61 retained documentation files, independently audits every ABSORB and
REJECT row from the committed processing ledger, and verifies the three
disputed findings (SOT3-F01/F02/F03) against fresh source citations. Prior
dispatcher and prior external-review conclusions are treated as hypotheses to
test, not authority.

## Target / Source

Primary committed evidence (read, not re-hashed):

- `docs/evidence/sot/sot3-t0-source-manifest.json`
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md`
- `docs/reviews/CVF_SOT3_T0_EXTERNAL_REVIEW_RETURN_2026-07-12.md`
- `docs/corpus-intelligence/registry/entries/sot3-t0-retained-three-layer-advisory-scan.json`

Retained source roots (read-only, targeted semantic reads):

- `.private_reference/legacy/CVF_SOT 10.07/CVF_Refinery_Patch`
- `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch`
- `.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Flow_Patch`

## Scope / Methodology

- No file hashing was repeated; the committed manifest and per-file SHA-256
  values are reused as-is per the work order's do-not-misread instruction.
- All 61 documentation files were read in full this tranche (6 had already been
  read in T0: Refinery root README/TREEVIEW, Flow root README/TREEVIEW/
  Architecture.md, Kernel package README). The remaining 55 files - all
  Refinery/Kernel/Flow doctrine, specs, guides, evidence samples, and the four
  Kernel external-knowledge-absorption maps - are new coverage in T0R.
- All 9 REJECT-disposition source files (Flow's embedded refinery: spec,
  schema, 5 TypeScript modules, 1 test) were read in full and independently
  compared against the corresponding Refinery specs.
- All 35 ABSORB-disposition files were independently re-read and checked for
  internal contradiction with the topology claim before accepting ABSORB as
  unqualified.
- Every claim below cites file path and, where applicable, line number.

## Source Inventory: 61-Document Coverage Table

Aggregate summary (detail table follows below):

| Root | Files | Coverage |
|---|---:|---|
| REFINERY | 25 | 25/25 COMPLETE |
| KERNEL | 22 | 22/22 COMPLETE |
| FLOW | 14 | 14/14 COMPLETE |
| Total | 61 | 61/61 COMPLETE |

### R2 Repair: Exact 61-Row Documentation Coverage Table

Per bounded-repair R2, this table is keyed by `rootId + sourceRelativePath`,
one row per manifest documentation record, each with a meaningful body fact or
section citation (not a filename or title-only fact), its semantic relevance,
and its disposition or relationship to the architecture decision.

Historical Kernel review paths encode `/` as `&#47;` in the key cell, matching
the committed ledger's authority-safe convention. Decode the entity before
manifest set comparison; the retained root is
`.private_reference/legacy/CVF_SOT 10.07/CVF_Truth_Kernel_Patch/`.

| # | rootId | sourceRelativePath | Body fact / section citation | Semantic relevance | Disposition / architecture relationship |
|---:|---|---|---|---|---|
| 1 | FLOW | `Architecture.md` | Line 41-52 CVF Truth Stack: `CVF_TRUTH_FLOW -> CVF_TRUTH_KERNEL -> Governance Runtime`; omits Refinery entirely. | Primary source for the Flow-before-Kernel topology claim (Axis 5). | ABSORB_WITH_EXCLUSION - lifecycle stages absorbed, pre-Kernel position excluded |
| 2 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/README.md` | Line 10 `Acquire -> Refine -> Verify through Truth Kernel -> Register...`; line 32 responsibility table. | Package-level README repeats the pre-Kernel Refine-ownership claim found in the root README. | ABSORB_WITH_EXCLUSION - post-Kernel table absorbed, pre-Kernel Refine claim excluded |
| 3 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/CLAIM_BOUNDARY.md` | Line 3 lists "refinery structure" as an allowed Flow claim; line 7-13 evidence ladder. | Formal claim-boundary document that legitimizes Flow's refinery claim, strengthening the topology dispute. | ABSORB_WITH_EXCLUSION - evidence-ladder pattern absorbed, refinery-structure claim excluded |
| 4 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/CONTEXT_DISTRIBUTION.md` | Line 3 requires a distribution package to include a Truth Kernel receipt field. | Directly narrows finding F03: doctrine already requires receipt-binding; code under-implements it. | ADAPT - fix publish-gate.ts to honor this already-correct doctrine requirement |
| 5 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/FEEDBACK_LOOP.md` | Line 5 feedback may propose source-confidence changes; line 7 "A proposal becomes active only through CVF review." | Doctrine requires proposal-gating for score changes; source-score.ts mutates directly with no gate. | ADAPT - bind source-score mutation to an approved proposal per this spec |
| 6 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/FLOW_PIPELINE.md` | Line 6-7 canonical pipeline table: `Refine` stage takes intake record to refinery packet, then feeds `Verify` (Kernel). | Single strongest textual proof that Flow's own canonical pipeline places Refine before Kernel invocation. | ABSORB_WITH_EXCLUSION - stage table absorbed for post-Kernel stages, Refine-before-Kernel ownership excluded |
| 7 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/FLOW_ROUTING.md` | Line 9 "No matching route is never an implicit allow. It returns ESCALATE or BLOCKED." | Uncontested fail-closed routing invariant; post-Kernel capability with no topology conflict. | ABSORB - clean post-Kernel routing doctrine |
| 8 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/INFORMATION_DOSE.md` | Line 5-10 four dose profiles (EXECUTIVE_SUMMARY, OPERATOR_ACTION, ENGINEERING_FULL, AGENT_TASK). | Post-Kernel distribution-control capability, uncontested and useful. | ABSORB - clean post-Kernel dose-control doctrine |
| 9 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/LIFECYCLE_SPEC.md` | Line 5 states include REFINING; line 11 READY_FOR_VERIFICATION->VERIFIED listed with no receipt-binding condition. | Confirms F03 at spec level: the doctrine itself does not condition the VERIFIED transition on a Kernel receipt. | ABSORB_WITH_EXCLUSION - lifecycle vocabulary absorbed, unconditioned VERIFIED transition excluded pending receipt-binding |
| 10 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/MULTI_LEVEL_SOT.md` | Line 5-8 four SOT scopes (Internal, Project, Environment, Derived); line 10 differing-scope records may both be valid. | Clean, uncontested scoping doctrine relevant to cross-layer scope handling. | ABSORB - clean scoping doctrine |
| 11 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/REFINERY_SPEC.md` | Line 5-11 full 5-stage refinery spec (normalize, attach source, cross-reference, structural checks, enrich) with own invariants. | The single strongest document proving F02: a complete, doctrinally-serious competing Refinery spec inside Flow's own package. | REJECT - competing spec for Refinery-owned responsibility; retire in favor of dedicated Refinery |
| 12 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/TRUTH_FLOW_DOCTRINE.md` | Line 10 "Refinement improves usability but not authority"; line 14 fail-closed principle. | Doctrine-level use of "refinement" as a Flow-owned term, reinforcing F02; also states a valid fail-closed rule. | ABSORB_WITH_EXCLUSION - fail-closed and trust-boundary rules absorbed, refinement-ownership framing excluded |
| 13 | FLOW | `README.md` | Line 5 "built on top of Kernel" (post-Kernel) contradicted by line 11-20 lifecycle diagram and line 16-27 position diagram (Flow before Kernel). | Root README itself is internally self-contradictory on topology - the clearest single-file evidence of the dispute. | ABSORB_WITH_EXCLUSION - lifecycle vocabulary and post-Kernel self-claim absorbed, contradicting position diagram excluded |
| 14 | FLOW | `TREEVIEW.md` | Full package tree: src intake/refinery/lifecycle/routing/distribution/feedback/monitor plus tests. | Confirms Flow's package structure includes a dedicated refinery/ source directory, structurally embedding the F02 dispute. | ABSORB - structural map, no independent claim beyond confirming REFINERY_SPEC.md's implementation exists |
| 15 | KERNEL | `EXTENSIONS/CVF_TRUTH_KERNEL/README.md` | Line 24-32 `Canonical Sources -> Truth Kernel -> Evidence/Obligation/Provenance/Verification -> Governance Runtime`; line 180 four provenance labels. | Kernel's own canonical chain omits Refinery/Flow from any pre-Kernel role, supporting the 2-vs-1 topology tie-break. | ABSORB - internally consistent, no contradiction |
| 16 | KERNEL | `docs/evidence/truth_kernel/README.md` | Line 5-7 sample artifacts do not prove production readiness; line 9-17 seven required evidence classes. | The exact ledger-flagged missing ABSORB row (R1 repair); disciplined claim-boundary framing. | ABSORB - consistent evidence-ladder pattern |
| 17 | KERNEL | `docs/evidence/truth_kernel/SAMPLE_RELEASE_TRUTH_RECEIPT.md` | Line 18-24 verification_results has 3 non-empty entries, all status pass. | The documented 'good' receipt example always has non-empty content, never demonstrating the empty-array fail-open edge case - circumstantial support for F01 being a structural blind spot, not an accepted risk. | ADAPT - useful template, but should be paired with a documented empty-results negative example |
| 18 | KERNEL | `docs/evidence/truth_kernel/SAMPLE_TRUTH_PACKET.md` | Line 9-34 non-empty evidence, computed_claims, obligations, llm_inferred_claims, human_approval, receipt fields all populated. | Confirms the truth-packet schema's computed/llm_inferred split found in T0; sample is a fully-populated happy path. | ABSORB - confirmatory sample, consistent with schema |
| 19 | KERNEL | `docs/guides/truth/NON_CODER_TRUTH_INTAKE_GUIDE.md` | Line 5-13 seven business-language intake questions (What source, who owns it, is it still valid, sign-off). | Non-coder-first UX pattern, no architectural dispute. | DEFER - supporting guide, re-author after contract ratification |
| 20 | KERNEL | `docs/guides/truth/PROJECT_TRUTH_REFERENCES_GUIDE.md` | Line 5 principle: projects reference truth IDs, do not copy canonical truth locally unless snapshot-marked and receipt-bound. | Reference-not-copy pattern matching SOT_INDEX_SPEC.md; no conflict. | ABSORB - consistent reference discipline |
| 21 | KERNEL | `docs/guides/truth/TRUTH_KERNEL_QUICKSTART.md` | Line 18-33 quick example includes non-empty evidence and obligations arrays, unlike Refinery's quickstart. | Kernel's own quickstart does not itself trigger the empty-collection bug, a useful contrast to Refinery's quickstart which does. | ABSORB - good-practice example, worth preserving in the rewrite |
| 22 | KERNEL | `docs/reference/truth/CVF_TRUTH_KERNEL_DOCTRINE.md` | Line 27-29 "fail-stop beats fail-silent"; line 31-42 trusted-core boundary. | The doctrine that the empty-evidence receipt/gate code directly violates (Axis 6). | ABSORB - sound doctrine; implementation gap is separate |
| 23 | KERNEL | `docs/reference/truth/EVIDENCE_REGISTRY_SPEC.md` | Line 51 only approved-status evidence may be used in STRICT verification. | New gap found in T0R: no examined gate code checks evidence approval status, only verification-result status. | ABSORB - exposes an additional hardening item for SOT3-T4 |
| 24 | KERNEL | `docs/reference/truth/HUMAN_RESPONSIBILITY_SPEC.md` | Line 17-21 human decision rules require reason, risk acceptance, and cannot bypass hard obligations without exception handling. | Sound accountability doctrine, no conflict. | ABSORB - clean doctrine |
| 25 | KERNEL | `docs/reference/truth/INDEPENDENT_VERIFIER_SPEC.md` | Line 30 method enum (schema, formula, source, obligation, rule, test); line 22 LLM boundary for hard/numerical/contractual/legal claims. | Sharpens F03/F01: explains and partially indicts the RELAXED-mode obligation-only block condition as too narrow. | ABSORB - promoted to sharpening evidence for Axis 4 hardening |
| 26 | KERNEL | `docs/reference/truth/OBLIGATION_REGISTRY_SPEC.md` | Line 30-31 HARD/SOFT obligation types; HARD blocks execution or freeze. | Explains the relaxed-mode.ts method==='obligation' special case in code. | ABSORB - sound obligation model |
| 27 | KERNEL | `docs/reference/truth/PROVENANCE_LABEL_SPEC.md` | Line 14-17 four labels (MEASURED, COMPUTED, LLM_INFERRED, HUMAN_APPROVED); line 33-35 provenance-collapse definition. | Matches the truth-packet schema's computed/llm_inferred split; high-value doctrine. | ABSORB - high-value, uncontested doctrine |
| 28 | KERNEL | `docs/reference/truth/README.md` | Line 18-23 Canonical Sources -> Kernel -> Governance Runtime, matching the package README's chain exactly. | Third independent Kernel document confirming the same topology, no Refinery/Flow pre-Kernel role. | ABSORB - internally consistent |
| 29 | KERNEL | `docs/reference/truth/RUNTIME_MONITOR_SPEC.md` | Line 11-19 monitored signals (stale evidence, expired obligation, source drift) and 5 actions. | Sound decay-detection doctrine, no conflict. | ABSORB - clean doctrine |
| 30 | KERNEL | `docs/reference/truth/SOT_INDEX_SPEC.md` | Line 36-38 projects reference truth IDs, do not copy canonical truth without snapshot marking. | Reference-not-copy pattern, no conflict. | ABSORB - clean doctrine |
| 31 | KERNEL | `docs/reference/truth/VERIFICATION_GATE_SPEC.md` | Line 33 STRICT mode "Missing required evidence blocks". | The single most direct spec-vs-code contradiction found in the entire corpus (Axis 6 decisive evidence). | ABSORB - promoted to decisive F01/Axis-6 evidence |
| 32 | KERNEL | `docs&#47;reviews&#47;external_knowledge_absorption&#47;AGENT_HARNESS_FAIL_STOP_MAP.md` | Line 10-11 "the dangerous failure mode is fail-silent. Fail-stop is safer than polished wrong output." | Reveals the Kernel fail-stop doctrine's own external source; the code's empty-evidence pass is a direct violation of the very principle the doctrine says it was built from. | NO_NEW_VALUE for SOT3 architecture scope - provenance context for CVF's own knowledge-absorption learning lane |
| 33 | KERNEL | `docs&#47;reviews&#47;external_knowledge_absorption&#47;MICROSOFT_AGENT_GOVERNANCE_TOOLKIT_MAP.md` | Line 14 "deny by default / fail closed" mapped to Verification Gate / Guard Contract. | Third independent source naming fail-closed-by-default as intended Kernel behavior. | NO_NEW_VALUE for SOT3 architecture scope - provenance/context only |
| 34 | KERNEL | `docs&#47;reviews&#47;external_knowledge_absorption&#47;SANTANDER_MECHANICAL_GOVERNANCE_MAP.md` | Line 13-23 guardrail/hard-gate/evaluation vocabulary mapped onto CVF Verification Gate STRICT/BLOCKED. | General governance-pattern provenance, not specific to the three-layer topology dispute. | NO_NEW_VALUE for SOT3 architecture scope - provenance/context only |
| 35 | KERNEL | `docs&#47;reviews&#47;external_knowledge_absorption&#47;SOT_KERNEL_MAP.md` | Line 15-25 maps SOT Kernel concept onto Evidence/Obligation Registry, SOT Index, verification gates, Truth Receipt. | Shows the Kernel doctrine itself originated from a prior external-absorption exercise; explains its relative maturity vs. Refinery/Flow. | NO_NEW_VALUE for SOT3 architecture scope - provenance/context only |
| 36 | KERNEL | `tools/truth/README.md` | Line 5 templates are not production evidence by themselves. | Consistent claim-boundary discipline for operator templates. | ABSORB - template-only framing, no runtime claim |
| 37 | REFINERY | `EXTENSIONS/CVF_REFINERY/README.md` | Line 9-25 canonical chain Raw -> INTAKE gates -> Refinery -> Packet -> Kernel -> verified/reject/escalate -> Flow -> business app. | One of three Refinery canonical-chain documents that independently state the same topology in their own words; strong topology anchor. | ABSORB - unambiguous, internally consistent |
| 38 | REFINERY | `README.md` | Same canonical chain diagram (line 9-25 equivalent) as EXTENSIONS README and docs/reference README. | Distinct file from the other two Refinery READMEs (root vs package vs reference); its own file even though it states the same topology. | ABSORB - distinct file, same confirmed topology |
| 39 | REFINERY | `TREEVIEW.md` | Full package tree: types, intake, pipeline, normalize, dedupe, conflicts, quality, integrity, lineage, packet, receipts, adapters, monitor, schemas, rules, examples, tests, governance checkers, scripts, tools. | Confirms a complete, well-organized reference implementation structure exists for every doctrine concept. | ABSORB - structural map, corroborates doctrine completeness |
| 40 | REFINERY | `docs/evidence/refinery/README.md` | Line 5 samples demonstrate expected shapes only; line 7 lists required evidence for stronger claims. | Disciplined evidence-ladder framing, parallel to Kernel's evidence README. | ABSORB - consistent claim-boundary discipline |
| 41 | REFINERY | `docs/evidence/refinery/SAMPLE_FAILURE_INJECTION_REPORT.md` | Line 3-12 8-row failure-injection matrix (FI-01 to FI-08); none test the zero-stages-executed case. | Confirms by omission that the empty-pipeline scenario was never conceived of as a failure mode to test - structural blind spot, not accepted risk. | ADAPT - useful template; must add a zero-stage negative test case before SOT3-T3 contract tests |
| 42 | REFINERY | `docs/evidence/refinery/SAMPLE_REFINERY_PACKET.md` | Line 3-30 sample packet with non-empty conflict_sets, quality_findings, transformation_lineage; status REVIEW_REQUIRED. | Confirmatory sample matching REFINERY_PACKET_SPEC.md exactly; happy-path example only. | ABSORB - confirmatory sample |
| 43 | REFINERY | `docs/evidence/refinery/SAMPLE_REFINERY_RECEIPT.md` | Line 3-25 sample receipt with normalization_steps, conflict_set_ids, quality_finding_ids populated. | Confirmatory sample matching the receipt spec; happy-path example only. | ABSORB - confirmatory sample |
| 44 | REFINERY | `docs/guides/refinery/NON_CODER_SOURCE_INTAKE_GUIDE.md` | Line 5-16 ten business-language intake questions (what, where, owner, scope, purpose, expiry, sensitivity, conflicts). | Non-coder-first UX pattern, no architectural dispute. | DEFER - supporting guide, re-author after contract ratification |
| 45 | REFINERY | `docs/guides/refinery/REFINERY_QUICKSTART.md` | Line 49-53 official example calls RefineryEngine().run() with sourceEnvelopes/rawRecords/ruleManifest but NO stages argument. | The single strongest piece of evidence for F01: the documented minimal usage itself triggers the empty-pipeline fail-open. | ADAPT - must be rewritten to require or default to the mandatory stage list once Axis 6 is ratified |
| 46 | REFINERY | `docs/guides/refinery/RULE_AUTHORING_GUIDE.md` | Line 5-13 rule principles (deterministic, versioned, scoped, testable, non-destructive); line 30-38 review checklist. | Solid rule-engine design pattern matching the rules/default/*.yaml runtime files found in T0. | ABSORB - sound rule-authoring discipline |
| 47 | REFINERY | `docs/guides/refinery/SOT_VERTICAL_SLICE_GUIDE.md` | Line 22-31 eight acceptance scenarios (exact duplicate, conflict, stale source, modified hash, missing lineage, attempted CANONICAL_TRUTH). | Concrete acceptance-test scenario set; useful for scoping a future contract-test suite, but does not include a zero-stage scenario either. | ADAPT - reusable acceptance scenarios; must add a zero-stage/empty-evidence scenario |
| 48 | REFINERY | `docs/reference/refinery/CLAIM_BOUNDARY.md` | Line 3-8 allowed claims; line 10-18 not-allowed claims; line 20-27 five-rung evidence ladder. | Disciplined evidence-ladder pattern, reusable CVF-wide, parallel to Flow's own CLAIM_BOUNDARY.md. | ABSORB - reusable governance pattern |
| 49 | REFINERY | `docs/reference/refinery/CONFLICT_SET_SPEC.md` | Line 21-30 conflict preconditions: same subject/field, overlapping scope, overlapping time window, differing normalized values. | Materially stronger than Flow's embedded cross-reference.ts, which lacks scope/time-overlap checks. | ABSORB - settles Axis 3 ordering, exposes a REJECT-row algorithmic weakness |
| 50 | REFINERY | `docs/reference/refinery/CVF_REFINERY_BINDING_SPEC.md` | Line 30-35 four-way Kernel adapter response contract (ACCEPT_EVIDENCE_CANDIDATE, REJECT, ESCALATE, REQUIRE_ADDITIONAL_EVIDENCE). | New precise producer/consumer contract detail not previously cited in T0. | ABSORB - adds new contract detail for the producer/consumer mapping |
| 51 | REFINERY | `docs/reference/refinery/CVF_REFINERY_DOCTRINE.md` | Line 35-37 fail-closed principle; line 41-52 canonical 10-step pipeline order. | Internally consistent doctrine; settles Axis 3 (dedupe before conflict) at the doctrine level. | ABSORB - foundational doctrine, settles Axis 1 and Axis 3 |
| 52 | REFINERY | `docs/reference/refinery/DUPLICATE_GROUP_SPEC.md` | Line 22-24 grouping never auto-deletes/merges; merge/discard requires explicit decision and receipt. | Sound non-destructive dedupe doctrine, no conflict. | ABSORB - clean doctrine |
| 53 | REFINERY | `docs/reference/refinery/FAILURE_TOKENS.md` | Line 5-24 exhaustive 16-token table; no token exists for zero-stages-executed. | Direct proof of the structural taxonomy gap underlying F01: the token vocabulary itself has no name for the empty-pipeline case. | ADAPT - must add a new REFINERY_NO_STAGES_EXECUTED-class token before SOT3-T3 |
| 54 | REFINERY | `docs/reference/refinery/NORMALIZED_RECORD_SPEC.md` | Line 23 canonicalization must be deterministic for the same input and rule version. | Spec requirement violated by the code's randomUUID()/new Date() non-determinism in the packet builder. | ABSORB - doctrine correct; reinforces the determinism gap found in T0 |
| 55 | REFINERY | `docs/reference/refinery/QUALITY_FINDING_SPEC.md` | Line 19-24 four severity levels; line 29 scores must never hide individual blocking findings. | Sound quality-signal doctrine, no conflict. | ABSORB - clean doctrine |
| 56 | REFINERY | `docs/reference/refinery/README.md` | Line 12-24 canonical chain diagram; line 29-43 explicit reading order for all seven object-contract specs. | Titled the canonical public-safe specification surface; distinct file from root and EXTENSIONS READMEs. | ABSORB - canonical authority document for Refinery |
| 57 | REFINERY | `docs/reference/refinery/REFINERY_BOUNDARY_SPEC.md` | Line 5-11 module boundary table: Flow explicitly denied raw normalization and truth declaration. | The single most authoritative cross-package boundary document; primary tie-breaker for Axis 5. | ABSORB - decisive Axis 5 tie-breaker evidence |
| 58 | REFINERY | `docs/reference/refinery/REFINERY_PACKET_SPEC.md` | Line 26-44 status calculation logic; READY_FOR_KERNEL has no condition for zero-stages-executed. | Matches the actual code exactly; the precise textual source of the empty-pipeline spec gap (Axis 6). | ADAPT - status calculation must add a stages-executed >= 1 condition |
| 59 | REFINERY | `docs/reference/refinery/SOURCE_ENVELOPE_SPEC.md` | Line 3 identity established before refinement; line 28-37 mandatory validation fields. | The authoritative source-position contract; settles Axis 2. | ABSORB - settles Axis 2 (source position) |
| 60 | REFINERY | `docs/reference/refinery/TRANSFORMATION_LINEAGE_SPEC.md` | Line 9 canonical 8-stage enum (INTAKE, NORMALIZE, DEDUPE, CONFLICT, QUALITY, INTEGRITY, PACKET, RECEIPT); line 26 lineage-completeness gate. | Settles Axis 3 ordering; also the precise mechanism for the empty-pipeline vacuous-lineage gap (Axis 6 root cause). | ADAPT - the required-lineage completeness check must be redefined relative to a mandatory stage list, not executed-stage outputs |
| 61 | REFINERY | `tools/refinery/README.md` | Line 5 templates only, filling a template does not establish authority or readiness. | Consistent claim-boundary discipline for operator templates. | ABSORB - template-only framing, no runtime claim |

### R2 Set-Equality Proof

The 61 `(rootId, sourceRelativePath)` keys in the table above were compared
programmatically against the 61 `.md`-extension records in the committed
`docs/evidence/sot/sot3-t0-source-manifest.json`. Result: the two sets are
equal (MATCH) - zero paths present in the manifest and missing from the
table; zero paths present in the table and absent from the manifest.

```text
manifest doc count: 61
coverage table row count: 61
equal: True
manifest - table: set()
table - manifest: set()
```

## Corpus Manifest Reconciliation

- Manifest fileCount: 305 (unchanged; no rescan performed per work order).
- Documentation subset: 61 files (`.md` extension), confirmed by direct
  manifest query against the committed `sot3-t0-source-manifest.json`.
- No drift detected in retained source during this tranche; git status was
  clean at `executionBaseHead` and remained clean throughout the read-only
  audit.

## Findings / Position

T0R verdict on the T0 dispatcher position
(`THREE_LAYER_MODEL_CONFIRMED_WITH_ROLE_SPLIT_AND_CONTRACT_REWRITE`) and the T0
external-review verdict (`CONFIRMED_WITH_NARROWING`):

**`CONFIRMED_WITH_NARROWING_AND_SHARPER_ROOT_CAUSE`.** Both prior verdicts
correctly identify the three-layer separation as valuable and the prototype as
unsafe. Deeper documentation reading strengthens, rather than weakens, the two
headline findings (empty-evidence fail-open; Flow topology contradiction) and
locates a precise root cause for each that neither prior pass cited. One T0
sub-claim is narrowed: Flow's own distribution doctrine already requires a
Kernel receipt field; the gap is implementation-versus-doctrine, not a doctrine
gap. Full detail is in the companion decision recommendation.

## Independent Audit: All 35 ABSORB Rows

### R1 Repair: Exact 35-Row ABSORB Audit Table

Per bounded-repair R1, this table is keyed by `rootId + sourceRelativePath`,
one row per T0 ledger `ABSORB` record. It replaces the prior grouped/numbered
audit, which under-represented two ledger rows
(`KERNEL | docs/evidence/truth_kernel/README.md` and `FLOW | README.md`) and
duplicated Refinery root `README.md` against a different file
(`docs/reference/refinery/README.md`). Each row has an independent fact/
citation and a terminal audit verdict.

| # | rootId | sourceRelativePath | Independent fact / citation | Audit verdict |
|---:|---|---|---|---|
| 1 | FLOW | `Architecture.md` | Line 41-52: CVF Truth Stack diagram `CVF_TRUTH_FLOW -> CVF_TRUTH_KERNEL -> Governance Runtime`, asserting Flow before Kernel and omitting Refinery entirely. | ABSORB_WITH_EXCLUSION - absorb lifecycle-stage vocabulary; exclude the pre-Kernel position claim (contradicts Refinery/Kernel canonical diagrams). |
| 2 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/README.md` | Line 10 `Acquire -> Refine -> Verify through Truth Kernel -> Register...`; line 16-21 position diagram places Flow before Kernel. | ABSORB_WITH_EXCLUSION - absorb post-Kernel responsibilities (line 32 table); exclude the pre-Kernel Refine ownership claim. |
| 3 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/CLAIM_BOUNDARY.md` | Line 3 explicitly lists "refinery structure" as an allowed Flow claim, alongside lifecycle/routing/distribution claims. | ABSORB_WITH_EXCLUSION - absorb the evidence-ladder claim-discipline pattern; exclude the "refinery structure" claim line. |
| 4 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/LIFECYCLE_SPEC.md` | Line 5 states enum includes `REFINING`; line 11 lists `READY_FOR_VERIFICATION -> VERIFIED` as a required transition with no receipt-binding condition specified. | ABSORB_WITH_EXCLUSION - absorb lifecycle state vocabulary; exclude the unconditioned VERIFIED transition until receipt-bound. |
| 5 | FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/TRUTH_FLOW_DOCTRINE.md` | Line 10 "Refinement improves usability but not authority" - doctrine-level use of "refinement" as a Flow-owned term; line 14 fail-closed principle. | ABSORB_WITH_EXCLUSION - absorb fail-closed doctrine and trust-boundary rules (line 14-20); exclude "refinement" ownership framing. |
| 6 | FLOW | `README.md` | Line 5 "It is built on top of CVF Truth Kernel" (post-Kernel claim) directly contradicted by line 11-20 lifecycle diagram (`Acquire -> Refine -> Verify...`) and the Position Inside CVF diagram placing Flow before Kernel. | ABSORB_WITH_EXCLUSION - absorb lifecycle vocabulary and the post-Kernel self-claim (line 5); exclude the contradicting pre-Kernel position diagram in the same file. |
| 7 | KERNEL | `EXTENSIONS/CVF_TRUTH_KERNEL/README.md` | Line 24-32 position diagram `Canonical Sources -> Truth Kernel -> Evidence/Obligation/Provenance/Verification -> Governance Runtime`; line 180 provenance labels; line 137-141 fail-stop doctrine. | ABSORB - internally consistent with Refinery's canonical chain; no contradiction found. |
| 8 | KERNEL | `docs/evidence/truth_kernel/README.md` | Line 5-7 claim boundary: sample artifacts are examples only, do not prove production readiness; line 9-17 lists 7 required evidence classes before production claims. | ABSORB - disciplined evidence-ladder framing, consistent with Refinery's parallel evidence README. |
| 9 | KERNEL | `docs/reference/truth/CVF_TRUTH_KERNEL_DOCTRINE.md` | Line 27-29 "fail-stop beats fail-silent" - the doctrine the empty-evidence receipt/gate code violates; line 31-42 trusted-core boundary. | ABSORB - sound doctrine; the violation is in the implementation, not this text. |
| 10 | KERNEL | `docs/reference/truth/EVIDENCE_REGISTRY_SPEC.md` | Line 51 "Only approved evidence may be used in STRICT verification unless an explicit exception exists" - a requirement no examined gate code checks. | ABSORB - exposes an additional implementation gap (evidence-approval status not checked at the gate) beyond the empty-results fail-open. |
| 11 | KERNEL | `docs/reference/truth/HUMAN_RESPONSIBILITY_SPEC.md` | Line 17-21 human decision rules: overrides require reason and risk acceptance; approval must not bypass hard obligations without explicit exception handling. | ABSORB - sound accountability doctrine, no conflict found. |
| 12 | KERNEL | `docs/reference/truth/INDEPENDENT_VERIFIER_SPEC.md` | Line 30 method enum (schema, formula, source, obligation, rule, test); line 22 LLM output must not be sole verifier for hard obligations, numerical, contractual, or legal claims. | ABSORB - directly explains and partially indicts the RELAXED-mode method-obligation-only block condition in code as narrower than this spec's intent. |
| 13 | KERNEL | `docs/reference/truth/OBLIGATION_REGISTRY_SPEC.md` | Line 30-31 HARD/SOFT obligation types (HARD = violation blocks execution or freeze) - explains the code's obligation-method special case. | ABSORB - sound obligation model. |
| 14 | KERNEL | `docs/reference/truth/PROVENANCE_LABEL_SPEC.md` | Line 14-17 four provenance labels (MEASURED, COMPUTED, LLM_INFERRED, HUMAN_APPROVED); line 33-35 provenance-collapse definition. | ABSORB - matches the truth-packet schema's computed_claims/llm_inferred_claims split found in T0; high-value doctrine. |
| 15 | KERNEL | `docs/reference/truth/README.md` | Line 18-23 Canonical Sources -> Truth Kernel -> Evidence/Obligation/Provenance/Verification -> Governance Runtime - matches package README's own chain, no Refinery/Flow mentioned. | ABSORB - internally consistent; omission of Refinery/Flow noted as a documentation gap, not a contradiction. |
| 16 | KERNEL | `docs/reference/truth/RUNTIME_MONITOR_SPEC.md` | Line 11-19 monitored signals (stale evidence, expired obligation, source drift, policy change) and actions (warn/escalate/block/mark_expired). | ABSORB - sound decay-detection doctrine, no conflict. |
| 17 | KERNEL | `docs/reference/truth/SOT_INDEX_SPEC.md` | Line 36-38 rule: projects reference truth IDs, do not copy canonical truth into local files unless explicitly marked as a bound snapshot. | ABSORB - reference-not-copy pattern, no conflict. |
| 18 | KERNEL | `docs/reference/truth/VERIFICATION_GATE_SPEC.md` | Line 33 STRICT mode "Missing required evidence blocks" - the single most direct spec-vs-code contradiction in the corpus (code passes on empty results array). | ABSORB - promoted to decisive F01 evidence; the doctrine text itself is correct, the gate code under-implements it. |
| 19 | KERNEL | `tools/truth/README.md` | Line 5 "These templates are not production evidence by themselves" - correct claim-boundary framing for operator templates. | ABSORB - template-only framing, no runtime claim. |
| 20 | REFINERY | `EXTENSIONS/CVF_REFINERY/README.md` | Line 9-25 canonical chain Raw source -> CVF INTAKE gates -> CVF Refinery -> Refinery Packet -> CVF Truth Kernel -> Verified/reject/escalate -> CVF Truth Flow -> business application. | ABSORB - unambiguous, internally consistent; matches root README and docs/reference/refinery/README.md exactly. |
| 21 | REFINERY | `README.md` | Same canonical chain diagram as EXTENSIONS/CVF_REFINERY/README.md and docs/reference/refinery/README.md (three independent files agree word-for-word on topology). | ABSORB - independently distinct file from docs/reference/refinery/README.md (different path); not a duplicate of the docs/reference row. |
| 22 | REFINERY | `docs/evidence/refinery/README.md` | Line 5 "They demonstrate expected artifact shapes only"; line 7 lists required evidence classes before stronger claims (unit tests, failure injection, Guard/Phase/Kernel receipts). | ABSORB - disciplined evidence-ladder framing, parallel to Kernel's evidence README. |
| 23 | REFINERY | `docs/reference/refinery/CLAIM_BOUNDARY.md` | Line 3-8 allowed claims (defines contracts, produces packets, stable tokens); line 10-18 not-allowed claims (canonical truth, production-ready without evidence). | ABSORB - disciplined evidence-ladder pattern, reusable CVF-wide, parallel to Flow's own CLAIM_BOUNDARY.md. |
| 24 | REFINERY | `docs/reference/refinery/CONFLICT_SET_SPEC.md` | Line 21-30 conflict-detection preconditions: same subject/field, overlapping scope, overlapping time window, differing normalized values - different scopes must not be treated as conflicts automatically. | ABSORB - materially stronger than Flow's embedded cross-reference.ts, which lacks scope/time-overlap checks (REJECT-row finding). |
| 25 | REFINERY | `docs/reference/refinery/CVF_REFINERY_BINDING_SPEC.md` | Line 30-35 four-way Kernel adapter response contract (ACCEPT_EVIDENCE_CANDIDATE, REJECT, ESCALATE, REQUIRE_ADDITIONAL_EVIDENCE) - new precise producer/consumer detail. | ABSORB - adds contract detail not previously cited in T0. |
| 26 | REFINERY | `docs/reference/refinery/CVF_REFINERY_DOCTRINE.md` | Line 35-37 fail-closed principle; line 17-21 deterministic-first; line 41-52 canonical pipeline order (source envelope -> validation -> normalize -> fingerprint -> dedupe -> conflict -> quality -> integrity -> lineage -> packet -> receipt). | ABSORB - internally consistent; settles the dedupe-before-conflict axis. |
| 27 | REFINERY | `docs/reference/refinery/DUPLICATE_GROUP_SPEC.md` | Line 22-24 grouping does not delete/merge records automatically; merge/discard requires explicit downstream decision and receipt; probable matches must not be silently promoted to exact. | ABSORB - sound non-destructive dedupe doctrine. |
| 28 | REFINERY | `docs/reference/refinery/NORMALIZED_RECORD_SPEC.md` | Line 23 "Canonicalization must be deterministic for the same input and rule version" - a spec requirement the code's randomUUID/new Date non-determinism violates. | ABSORB - doctrine correct; reinforces the determinism gap found in the packet builder. |
| 29 | REFINERY | `docs/reference/refinery/QUALITY_FINDING_SPEC.md` | Line 19-24 severity levels (INFO/WARN/REVIEW/BLOCK); line 29 "Scores must never hide individual blocking findings." | ABSORB - sound quality-signal doctrine. |
| 30 | REFINERY | `docs/reference/refinery/README.md` | Line 12-24 canonical chain diagram matching root and EXTENSIONS README; line 29-43 explicit reading order for the object-contract specs. | ABSORB - the canonical, titled "public-safe specification surface" for Refinery; distinct file from root README.md and EXTENSIONS/CVF_REFINERY/README.md (three files, not duplicates). |
| 31 | REFINERY | `docs/reference/refinery/REFINERY_BOUNDARY_SPEC.md` | Line 5-11 module boundary table: Flow owns "scoped routing, distribution, lifecycle, feedback, retirement" and explicitly must not own "raw normalization" or "truth declaration". | ABSORB - elevated to primary tie-breaker evidence against Flow's competing pre-Kernel claim. |
| 32 | REFINERY | `docs/reference/refinery/REFINERY_PACKET_SPEC.md` | Line 26-44 status calculation: READY_FOR_KERNEL only when neither BLOCKED nor REVIEW_REQUIRED conditions apply; no condition for "zero stages executed". | ABSORB - matches code exactly; also the precise textual source of the empty-pipeline spec gap. |
| 33 | REFINERY | `docs/reference/refinery/SOURCE_ENVELOPE_SPEC.md` | Line 3 "gives every input a stable identity ... before refinement"; line 28-37 mandatory validation fields (identity, owner, purpose, scope, hash, reference, capture time). | ABSORB - the authoritative source-position contract (settles Axis 2). |
| 34 | REFINERY | `docs/reference/refinery/TRANSFORMATION_LINEAGE_SPEC.md` | Line 9 canonical 8-stage enum (INTAKE, NORMALIZE, DEDUPE, CONFLICT, QUALITY, INTEGRITY, PACKET, RECEIPT); line 26 "cannot be READY_FOR_KERNEL when required lineage is incomplete". | ABSORB - settles dedupe-before-conflict ordering (Axis 3); also the precise mechanism for the empty-pipeline vacuous-lineage gap. |
| 35 | REFINERY | `tools/refinery/README.md` | Line 5 "They are templates only. Filling a template does not establish source authority, truth, CVF runtime activation, or production readiness." | ABSORB - template-only framing, no runtime claim. |

### R1 Set-Equality Proof

The 35 `(rootId, sourceRelativePath)` keys in the table above were compared
programmatically against the 35 `ABSORB`-disposition rows in the committed
`docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md`.
Result: the two sets are equal (MATCH).

```text
ledger ABSORB set size: 35
matrix audit table size: 35
equal: True
ledger - matrix: set()
matrix - ledger: set()
```

### Audit verdict: 5 rows require qualification, not reversal

Rows 1-6 (`Architecture.md`, Flow package `README.md`, `CLAIM_BOUNDARY.md`,
`LIFECYCLE_SPEC.md`, `TRUTH_FLOW_DOCTRINE.md`, Flow root `README.md` - all
FLOW-root documents) each assert or support the pre-Kernel/Flow-owns-refine
topology alongside genuinely valuable post-Kernel lifecycle vocabulary in the
same document. Marking these files unconditionally ABSORB (as T0 did) risks
silently importing the rejected topology claim along with the valid lifecycle
vocabulary. T0R revises the disposition for these rows to
`ABSORB_WITH_EXCLUSION`: absorb the post-Kernel lifecycle states, routing, and
claim-boundary discipline; explicitly exclude the pre-Kernel position diagram
and the "refinery structure" claim line. This is a narrowing of scope, not a
reversal of value. Row counts: 29 `ABSORB`, 6 `ABSORB_WITH_EXCLUSION`, 0
reversed to a non-absorb disposition; 35 total.

## New Absorb Candidates (Not Ledgered, Not Counted In The 35)

The following post-Kernel capability documents were independently found
high-value and uncontested during this tranche's full-text reads, but were
not disposed `ABSORB` in the T0 ledger (their ledger disposition is
`DEFER`). Per bounded-repair R1, they are kept in this separate table and are
**not** counted toward the 35-row ABSORB reconciliation above and **not**
labeled `NEW_ABSORB_CANDIDATE` as a ledger-row substitute.

| rootId | sourceRelativePath | T0 ledger disposition | Independent finding |
|---|---|---|---|
| FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/FLOW_ROUTING.md` | DEFER | Line 9 fail-closed routing invariant ("no matching route is never an implicit allow"); uncontested post-Kernel capability |
| FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/INFORMATION_DOSE.md` | DEFER | Line 5-10 four dose profiles; uncontested post-Kernel capability |
| FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/CONTEXT_DISTRIBUTION.md` | DEFER | Line 3 requires a bound Truth Kernel receipt field; narrows F03 |
| FLOW | `EXTENSIONS/CVF_TRUTH_FLOW/docs/MULTI_LEVEL_SOT.md` | DEFER | Line 5-10 four SOT scopes; uncontested scoping doctrine |

These four rows remain the CVF reviewer's decision to reclassify, if any; this
matrix only records that they were independently found valuable and does not
substitute for or inflate the 35-row ledger reconciliation.

## Independent Audit: All 9 REJECT Rows

| # | Path | Independent verification | Audit verdict |
|---|---|---|---|
| 1 | `EXTENSIONS/CVF_TRUTH_FLOW/docs/REFINERY_SPEC.md` | full 5-stage spec (normalize, attach source, cross-reference, structural checks, enrich) with its own invariants (line 13-20); this is a complete, doctrinally-serious competing spec, not a stray note | REJECT CONFIRMED, evidence strengthened - this is the strongest single document proving F02 |
| 2 | `EXTENSIONS/CVF_TRUTH_FLOW/schemas/refinery.packet.schema.json` | `additionalProperties: false` (line 5), required fields `packetId/intakeId/normalizedPayload/transformations/conflicts/status` (line 6-13) - structurally incompatible with the dedicated Refinery packet schema field-for-field | REJECT CONFIRMED; noted the schema is well-formed and strict on its own terms |
| 3 | `EXTENSIONS/CVF_TRUTH_FLOW/src/refinery/attach-source.ts` | defines a parallel `SourceAttachment`/`IntakeRecord` concept distinct from Refinery's `SourceEnvelope` | REJECT CONFIRMED |
| 4 | `EXTENSIONS/CVF_TRUTH_FLOW/src/refinery/cross-reference.ts` | groups purely by `normalizedKey` + `JSON.stringify` value equality (line 6-17) with no scope or effective-time overlap check; this is materially weaker than Refinery's own `CONFLICT_SET_SPEC.md` (lines 26-27: scope and time-window must overlap before treating values as conflicting) | REJECT CONFIRMED; new evidence that direct import would also import a less-correct algorithm, not just a naming clash |
| 5 | `EXTENSIONS/CVF_TRUTH_FLOW/src/refinery/enrichment.ts` | includes a `claimBoundary: "DERIVED_ENRICHMENT"` tag (line 2, 6) with no equivalent in dedicated Refinery source | REJECT CONFIRMED for direct import; flagged as an ADAPT-worthy primitive to backport |
| 6 | `EXTENSIONS/CVF_TRUTH_FLOW/src/refinery/normalize.ts` | thinner than Refinery's normalize suite (single rule-list vs. separate unit/date/text normalizers per TREEVIEW) | REJECT CONFIRMED |
| 7 | `EXTENSIONS/CVF_TRUTH_FLOW/src/refinery/refinery-engine.ts` | declares a second, incompatible `RefineryPacket` (line 9-15): `packetId` (`TFR-` prefix), camelCase, `READY_FOR_VERIFICATION` status - none matching the dedicated Refinery packet | REJECT CONFIRMED (T0 finding independently reproduced) |
| 8 | `EXTENSIONS/CVF_TRUTH_FLOW/src/refinery/verification.ts` | includes a `claimBoundary: "STRUCTURAL_ONLY_NOT_TRUTH_APPROVAL"` tag (line 4, 10) with no equivalent elsewhere in the corpus | REJECT CONFIRMED for direct import; flagged as an ADAPT-worthy primitive to backport |
| 9 | `EXTENSIONS/CVF_TRUTH_FLOW/tests/refinery.test.ts` | the committed test (line 11-15) calls `refine()` with only `normalizationRules` supplied - no structural rules, no comparison candidates, no enrichment steps - and asserts `status === "READY_FOR_VERIFICATION"` as the expected, passing result | REJECT CONFIRMED; this is the single strongest piece of evidence for F01 in the entire corpus - the fail-open is a tested, asserted-correct behavior, not merely an unguarded default |

### Audit verdict: all 9 REJECT dispositions independently confirmed

No REJECT row is reversed. Two files (`enrichment.ts`, `verification.ts`)
contain primitives (`DERIVED_ENRICHMENT`, `STRUCTURAL_ONLY_NOT_TRUTH_APPROVAL`
claim-boundary tags) worth extracting into the canonical rewrite even though
direct import of the surrounding module remains rejected.

## Verification Of Disputed Findings SOT3-F01/F02/F03

### SOT3-F01 - empty-collection fail-open

Disposition: `CONFIRMED_AND_ROOT_CAUSE_SHARPENED`.

New evidence beyond T0:

- `docs/reference/refinery/TRANSFORMATION_LINEAGE_SPEC.md` line 26: "A packet
  cannot be `READY_FOR_KERNEL` when required lineage is incomplete" - the
  enforcement hook exists in the spec, but "required lineage" is defined
  relative to executed-stage outputs (line 18-20 of the code path examined in
  T0), so zero executed stages yields zero required outputs and the check
  passes vacuously. This is the precise mechanism, not just the symptom.
- `docs/reference/refinery/FAILURE_TOKENS.md`: the exhaustive 16-token list has
  no token for "no stages executed" - a structural blind spot in the token
  taxonomy itself, not only in the code.
- `docs/guides/refinery/REFINERY_QUICKSTART.md` lines 49-53: the official
  quickstart example calls `RefineryEngine().run({sourceEnvelopes, rawRecords,
  ruleManifest})` with no `stages` argument - the documented minimal usage
  itself triggers the defect.
- `docs/reference/truth/VERIFICATION_GATE_SPEC.md` line 33: STRICT mode
  "Missing required evidence blocks" - a direct textual requirement that the
  Kernel `strict-mode.ts` code (empty results array passes) does not satisfy.
- `EXTENSIONS/CVF_TRUTH_FLOW/tests/refinery.test.ts` lines 11-15: a committed
  Flow test asserts the zero-structural-rule case as the expected passing
  result, for the analogous Flow-side fail-open.
- retained-root `AGENT_HARNESS_FAIL_STOP_MAP.md` (path:
  `CVF_Truth_Kernel_Patch` then `external_knowledge_absorption` folder) lines
  10-11: the doctrine's own absorbed source material states "the dangerous
  failure mode is fail-silent" - the bug is a violation of the very principle
  the Kernel doctrine says it was built from.

### SOT3-F02 - Flow topology and packet contradiction

Disposition: `CONFIRMED_AND_EVIDENCE_MULTIPLIED`.

T0 cited three Flow sources (root README, Architecture.md, embedded refinery
type). T0R adds three more, all independently asserting the same Flow-owns-
refine, Flow-before-Kernel position: `EXTENSIONS/CVF_TRUTH_FLOW/README.md` line
10; `EXTENSIONS/CVF_TRUTH_FLOW/docs/FLOW_PIPELINE.md` line 6-7 (canonical
pipeline table: `Refine` stage takes `intake record -> refinery packet`, then
`Verify` invokes Kernel); `EXTENSIONS/CVF_TRUTH_FLOW/docs/CLAIM_BOUNDARY.md`
line 3 ("refinery structure" is an allowed Flow claim). This is six independent
Flow-authored documents, not an isolated ambiguous diagram. Against this,
Refinery's `REFINERY_BOUNDARY_SPEC.md` line 9 and Kernel's own `Canonical
Sources -> Kernel -> ...` diagram both omit Flow from any pre-Kernel role. The
conflict is a genuine cross-package contradiction between two internally
self-consistent packages, not a single stray ambiguity.

### SOT3-F03 - assertion-based trust transitions

Disposition: `CONFIRMED_WITH_NARROWING`.

New evidence narrows the claim: `EXTENSIONS/CVF_TRUTH_FLOW/docs/
CONTEXT_DISTRIBUTION.md` line 3 explicitly requires a distribution package to
contain a "Truth Kernel receipt" field. The doctrine already specifies
receipt-binding. The gap identified in T0 (`publish-gate.ts` trusting a
`truthKernelAccepted: boolean`) is therefore an implementation gap against an
existing, correct doctrine requirement, not a doctrine gap that needs to be
invented. This narrows the required fix from "add a new doctrine rule" to
"make the implementation honor the rule that already exists."

## Additional Findings Not In T0

- `EXTENSIONS/CVF_TRUTH_FLOW/schemas/refinery.packet.schema.json` uses
  `additionalProperties: false` while the Kernel's `truth.packet.schema.json`
  uses `additionalProperties: true` - an inconsistent strictness posture across
  the corpus's two packet schemas, worth normalizing in the canonical rewrite.
- `docs/reference/truth/EVIDENCE_REGISTRY_SPEC.md` line 51 requires only
  `approved` evidence for STRICT verification; no code path examined in T0 or
  T0R checks evidence approval status at the gate, only verification-result
  status. This is a new gap, adjacent to but distinct from F01.
- The four Kernel `external_knowledge_absorption` maps
  (`SOT_KERNEL_MAP.md`, `AGENT_HARNESS_FAIL_STOP_MAP.md`,
  `MICROSOFT_AGENT_GOVERNANCE_TOOLKIT_MAP.md`,
  `SANTANDER_MECHANICAL_GOVERNANCE_MAP.md`) reveal that the Kernel doctrine was
  itself built by absorbing external governance concepts. This is useful
  provenance context for CVF's own knowledge-absorption learning lane; it is
  not an architecture dispute.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| general truth doctrine | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | ENRICH_EXISTING | retained corpus doctrine (evidence/obligation/provenance/verification/receipt split) is materially more detailed than the current bounded doctrine | map exact delta before SOT3-T1 |
| skill truth packet | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | ENRICH_EXISTING | vertical slice only, not general stack proof | preserve compatibility |
| independent Refinery Core | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | confirmed again this tranche; no owner created | recommend, do not create |
| post-Kernel Flow lifecycle | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | confirmed again this tranche; no owner created | recommend, do not create |
| prototype receipt/publish paths | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | REJECT_DIRECT_IMPORT | workflow-step obligation contract remains semantically unrelated to Kernel TruthReceipt | adaptation only |
| Flow `DERIVED_ENRICHMENT` / `STRUCTURAL_ONLY_NOT_TRUTH_APPROVAL` claim tags | OWNER_SURFACE_NOT_FOUND | NEW_FINDING | inline claim-boundary typing pattern found nowhere else in corpus or current CVF | recommend as a cross-cutting pattern, not tied to any one layer |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy three-folder source family plus committed advisory evidence |
| Upstream or source-mirror disposition | `LEGACY_REFERENCE_ONLY_WITH_REASON`: operator-authored retained patch without verified upstream repository identity |
| Enumeration or manifest plan | reuse committed 305-record manifest; no hash rescan performed this tranche |
| Per-file terminal-ledger plan | 61 documentation files and 44 ABSORB/REJECT rows independently audited this tranche; remaining rows retained pending from T0 |
| Owner or overlap route | this matrix recommends; CVF reviewer decides |
| Value-disposition route | absorb, adapt, defer, reject, block, no-new-value, or absorb-with-exclusion |
| Claim boundary | `COMPARISON_ONLY_NO_ABSORPTION`: independent semantic audit and citation evidence only; no direct import or implementation |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | committed partial T0 scan and retained roots |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | 61 documentation files plus every ABSORB/REJECT and disputed contract source |
| Blind-spot prevention action | independent re-reading of every ABSORB/REJECT row and disputed finding; five rows revised, zero silently accepted |
| Residual gap | final CVF reviewer acceptance of the eight decision axes remains open |
| Blind-spot verdict | COMPLETE_PENDING_REVIEW |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| three-layer doctrine, topology-revised | prepare/evaluate/distribute separation with Flow confined post-Kernel | DOCTRINE_ADAPTED | SOT3-T2 candidate | CVF reviewer ratifies axis 5 before contract work | no implementation |
| Refinery primitives | deterministic preparation, hardened | PACKAGE_CANDIDATE | SOT3-T3 candidate | rewrite with mandatory-stage enforcement | no direct import |
| Kernel primitives | evidence/obligation/provenance/verification/receipt, hardened | RUNTIME_CANDIDATE | SOT3-T4 candidate | fail-closed and content-binding rewrite | no runtime mutation |
| Flow post-Kernel primitives | routing/dose/distribution/lifecycle/feedback | RUNTIME_CANDIDATE | SOT3-T5 candidate | remove embedded refinery ownership first | no runtime mutation |
| Flow embedded refinery (spec, schema, 5 source, 1 test) | integration-risk evidence; two extractable claim-tag primitives | REJECT_DIRECT_IMPORT | SOT3-T2 negative evidence; claim-tag pattern candidate | retire module; extract `DERIVED_ENRICHMENT`/`STRUCTURAL_ONLY_NOT_TRUTH_APPROVAL` pattern separately | no package activation |
| prototype guards and negative-case tests | enforcement use cases | CHECKER_CANDIDATE | future owner decision | record advisory value only | no checker wiring |
| Kernel external-knowledge-absorption maps (4 files) | provenance/context for CVF governance-learning lane | NO_PACKAGE_OR_RUNTIME_VALUE | separate knowledge-absorption review, outside SOT3 scope | defer to a non-SOT tranche | no runtime or package action |

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| ABSORB rows silently import the rejected Flow topology alongside valid lifecycle vocabulary | apply `ABSORB_WITH_EXCLUSION` to the five identified rows; exclude named lines explicitly |
| REJECT rows treated as zero-value | extract `DERIVED_ENRICHMENT` and `STRUCTURAL_ONLY_NOT_TRUTH_APPROVAL` claim-tag patterns before discarding the surrounding modules |
| F01 treated as a simple missing check | root-cause is a taxonomy gap (no failure token for zero-stage execution) plus a vacuous-truth definition of "required lineage"; fix must address both, not just add one guard |
| F03 treated as requiring new doctrine | doctrine already exists (`CONTEXT_DISTRIBUTION.md`); fix is implementation conformance, not design |
| new EVIDENCE_REGISTRY_SPEC gap (approved-only evidence) folded silently into F01 | track as an adjacent, separately named gap in any future contract-test lane |

## Decision / Disposition

Matrix disposition: `COMPLETE_PENDING_REVIEW`. Full 61-document semantic
coverage is delivered; every ABSORB and REJECT row from the T0 ledger is
independently re-verified; all three disputed findings are confirmed with
sharper, newly-cited root causes; five ABSORB rows are narrowed to
`ABSORB_WITH_EXCLUSION`. No row in this matrix is treated as CVF-accepted; all
dispositions remain `PENDING_CVF_REVIEWER`. The companion architecture decision
recommendation resolves the eight required decision axes.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | committed SOT3-T0 evidence plus retained three-layer roots |
| Enumeration command | filesystem-backed direct file reads from the committed manifest; no rescan |
| Manifest artifact or inline manifest | `docs/evidence/sot/sot3-t0-source-manifest.json` (reused, unmodified) |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_SOT3_T0_EXTERNAL_SOURCE_PROCESSING_LEDGER_2026-07-12.md` (reused; audited, not modified) |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE, ABSORB_WITH_EXCLUSION (T0R refinement) |
| Owner-surface map | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` and `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` (ENRICH_EXISTING); `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` (REJECT_DIRECT_IMPORT); general Refinery/Flow modules remain OWNER_SURFACE_NOT_FOUND; full table in Overlap And Novelty Classification above |
| Unresolved items | eight decision axes; resolved in companion recommendation |
| Completion claim boundary | semantic audit and citation evidence only; no absorption, runtime, or readiness proof |

## Corpus Completeness And Report Integrity

- Corpus task class: SOT3-T0R targeted semantic reconciliation of committed
  evidence and retained roots.
- Corpus root: committed T0 evidence plus the three retained roots.
- Snapshot time: 2026-07-12, T0R execution.
- Enumeration command: filesystem-backed direct file reads from the committed
  manifest; no re-enumeration or rehash performed.
- Manifest artifact or inline manifest: `docs/evidence/sot/sot3-t0-source-manifest.json` (unmodified).
- Manifest hash: unchanged from T0; per-file SHA-256 values reused as-is.
- Processing ledger artifact or inline ledger: committed T0 ledger (unmodified; independently audited in this matrix).
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=305; ledger_terminal=305; exclusions=0; unresolved=0
- Unresolved files: 0 identities unresolved; semantic acceptance remains reviewer-pending. 61/61 documentation files read; 44/44 ABSORB+REJECT rows independently audited.
- Declared exclusions: none; ADAPT/DEFER rows outside the 61-doc and ABSORB/REJECT scope remain reviewer-pending per work order scope, not excluded from future review.
- Unreadable or unsupported files: none encountered.
- Aggregation check: 61 = 25 (Refinery) + 22 (Kernel) + 14 (Flow); 44 = 35 ABSORB + 9 REJECT.
- Drift check: retained source and committed evidence unchanged throughout; `git status` clean at start and end.
- Output traceability: every finding above cites a file path and, where applicable, a line number.
- Adversarial verification: T0 and T0R conclusions were independently re-derived from source text, not copied; five ABSORB rows were revised as a result.
- Corpus verdict: PARTIAL - 61/61 documentation files and 44/44 ABSORB/REJECT rows are COMPLETE_VERIFIED for this tranche's targeted scope; the full 305-file semantic scope remains reviewer-pending per work order boundary.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: T0's advisory findings (empty-collection
fail-open, Flow topology contradiction, assertion-based trust) will hold up
under deeper reading, and every ABSORB/REJECT row will independently
reconfirm without reversal.

Evidence Comparison Requirement: all 61 documentation files and 44 ABSORB/
REJECT rows were compared against this prediction. The prediction held for all
9 REJECT rows (zero reversals) and for 29 of 35 ABSORB rows; 6 ABSORB rows
required narrowing to `ABSORB_WITH_EXCLUSION` because deeper reading found the
same documents also assert the disputed pre-Kernel Flow topology.

Contradiction Or Gap Disposition: the six narrowed ABSORB rows are the
concrete contradiction the deeper read surfaced; they are named explicitly
above, not folded silently into a broader ABSORB count.

Claim Update Requirement: T0's per-finding verdicts (F01/F02/F03) are marked
CONFIRMED with a sharper cited root cause in each case; see Verification Of
Disputed Findings above for the per-finding claim update.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | External Absorption Core; Corpus Completeness And Report Integrity; Overlap And Novelty Classification; External Absorption Value Conversion Matrix; COMPLETE_PENDING_REVIEW; COMPLETE_VERIFIED; PARTIAL; ABSORB_WITH_EXCLUSION |
| gateRunPurpose | confirm exact matrix shape after checker source review, informed by the GC-051 corpus-path detection lesson from the T0 process-findings note |
| claimBoundary | checker-shape conformance does not prove semantic correctness or absorption value |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | committed advisory evidence -> T0R independent semantic re-audit -> CVF reviewer decision -> later fresh tranche if authorized |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py` |
| Owner surface | this matrix for evidence; companion recommendation for architecture decision; CVF reviewer for acceptance |
| Disposition | ADAPT through independently re-verified source-backed reconciliation |
| Claim boundary | no external recommendation becomes CVF authority directly |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private retained source and pre-implementation architecture review.

## Claim Boundary

This matrix is an independent semantic audit and citation evidence artifact
only. It does not ratify architecture, authorize implementation, create an
owner, or accept any disposition on CVF's behalf. All dispositions remain
`PENDING_CVF_REVIEWER`.
