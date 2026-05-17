# GC-018 Authorization — Phase 0.C Anti-Collusion Hard-Fail Enforcement

Memory class: FULL_RECORD

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION

Date: 2026-05-18

```text
GC-018 Continuation Candidate
- Candidate ID: CVF-17.05-PHASE-0C
- Date: 2026-05-18
- Parent roadmap / wave: .private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md
- Proposed scope: Promote the Phase 0.B advisory checker to pre-commit
  hard-fail. New review/rebuttal/response/verdict packets that are missing an
  Evidence Trace Block will block commit. Legacy packets (written before GC-046
  existed) are grandfathered by filename date or directory scope.
- Continuation class: ENFORCEMENT
- Active quality assessment: docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md
- Assessment date: 2026-05-17
- Weighted total: 8/10 (Phase 0.B threshold met on first checker run —
  4 compliant packets detected, threshold was 3)
- Lowest dimension: Operational efficiency (1/2 — hard-fail adds friction to
  review authoring; mitigated by clear error message and grandfathering rule)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: Phase 0.B threshold is met.
  Checker exists and runs clean. The only remaining gap is exit code: advisory
  (exit 0) → hard-fail (exit non-zero on new violations). Grandfathering legacy
  packets ensures no retroactive breakage. The 17.05 chain is the worked example
  that satisfies the evidence requirement.
- Quality protection commitments: (1) Legacy review packets written before
  GC-046 (2026-05-17) are grandfathered — not checked for hard-fail.
  (2) Hard-fail applies only to new packets added in the current commit diff.
  (3) Existing compliant packets are not re-validated. (4) Advisory output
  retained alongside the hard-fail signal.
- Why now: Phase 0.B threshold evidence exists in commit edbc6980. Checker
  already runs at pre-commit. Promoting to hard-fail is a 1-line change in
  exit behavior scoped to new files only.
- Active-path impact: LOW — only new review/rebuttal/response/verdict/
  absorption packets added in a commit are checked. No existing file touched.
- Risk if deferred: Each new absorption review added without Evidence Trace
  Block silently bypasses the anti-collusion requirement. The advisory warning
  is easy to ignore. Hard-fail closes the loop.
- Lateral alternative considered: YES
- Why not lateral shift: A CI-only advisory (no pre-commit block) would still
  allow commits that miss Evidence Trace Blocks, requiring a fixup commit.
  Pre-commit hard-fail for new files is the lowest-friction point to catch the
  issue before it enters history.
- Real decision boundary improved: YES — hard-fail on new packets makes
  GC-046 Rule 1 machine-enforced at the commit boundary, not just advisory.
- Expected enforcement class: CI_REPO_GATE (pre-commit hard-fail for new
  review packets missing Evidence Trace Block)
- Required evidence if approved:
  - Phase 0.B checker exists: governance/compat/check_anti_collusion_evidence_trace.py
  - Phase 0.B threshold met: 4 compliant packets >= threshold 3 (commit edbc6980)
  - Grandfathering rule defined: only files added in current diff are checked
  - Hard-fail exits non-zero when a new review packet in the diff is missing
    an Evidence Trace Block
  - Advisory output still printed for all missing packets (including legacy)
  - Pre-commit hook chain updated to pass --enforce flag

Depth Audit
- Risk reduction: 2 (closes the GC-046 Rule 1 enforcement gap; advisory-only
  enforcement is trivially bypassed)
- Decision value: 2 (hard-fail is the only enforcement class that guarantees
  new absorption reviews carry Evidence Trace Blocks)
- Machine enforceability: 2 (pre-commit exit non-zero is the strongest local
  enforcement class available without CI)
- Operational efficiency: 1 (adds one authoring step per new review packet;
  mitigated by clear error message with remediation instruction)
- Portfolio priority: 1 (Phase 0.C is explicitly listed in the roadmap but
  was deprioritized relative to Phase 1 tracks; Phase 0.B threshold now met
  removes the only blocker)
- Total: 8/10
- Decision: CONTINUE
- Reason: Phase 0.B threshold met, checker exists, grandfathering rule
  prevents retroactive breakage, hard-fail closes the advisory gap.

Authorization Boundary
- Authorized now: YES
- Next batch name: CVF-17.05-PHASE-0C implementation
- Permitted implementation:
  - Add --enforce logic to check_anti_collusion_evidence_trace.py: exit non-zero
    when a file added in the current commit diff is a review packet missing an
    Evidence Trace Block
  - Grandfathering rule: only diff-added files are hard-checked; legacy files
    remain advisory-only
  - Update pre-commit hook chain entry to pass --enforce flag
  - Update GC-046 guard to reflect hard enforcement is now active
- Not permitted:
  - Retroactive hard-fail on existing legacy review packets
  - Blocking commits that only modify (not add) review packets
  - Changes to public claims or release gates
```

## Purpose

Authorize Phase 0.C promotion of the GC-046 Evidence Trace advisory checker
to pre-commit hard-fail for newly added review packets. This is the terminal
enforcement phase of the anti-collusion protocol.

## Decision / Baseline / Proposed Tranche

- Decision: CONTINUE
- Candidate ID: CVF-17.05-PHASE-0C
- Depth Audit total: 8/10
- Authorized scope: --enforce logic in checker (exit non-zero on new diff-added
  review packets missing Evidence Trace Block), grandfathering rule for legacy
  packets, hook chain update to pass --enforce, GC-046 status update
- Not authorized: retroactive hard-fail on legacy packets, blocking modify-only
  commits, public claim changes

## Evidence / Required Evidence / Verification

Phase 0.B gate evidence:
- Commit `edbc6980` (2026-05-18): Phase 0.B checker delivered and registered
  in pre-commit hook chain
- First run output: 4 compliant packets detected (threshold was 3) — threshold met
- Compliant packets: CVF_17_05_REVIEW_CVF_CONVERGED_VERDICT, CLAUDE_PROPOSER_RESPONSE,
  CONSENSUS_REMEDIATION_ROADMAP_DRAFT, FINAL_CONVERGED_REMEDIATION_ROADMAP

Required evidence for Phase 0.C completion:
- check_anti_collusion_evidence_trace.py exits non-zero when --enforce is
  passed and a diff-added review packet is missing an Evidence Trace Block
- Pre-commit hook chain passes --enforce to the checker
- Legacy packets continue to appear as advisory-only warnings
- GC-046 guard updated: "Hard enforcement: active (Phase 0.C)"

## Source Authorization

Parent roadmap phase definition:
```
Phase 0.C - Deferred Hard Enforcement
Scope: Pre-commit or CI hard-fail for missing Evidence Trace Blocks.
Gate: Requires separate GC-018. Requires evidence from Phase 0.B.
```

Phase 0.B evidence: commit `edbc6980` (2026-05-18). Phase 0.B threshold
(3 compliant packets) met on first checker run (4 detected).

## Claim Boundary

This packet authorizes Phase 0.C hard-fail enforcement for new review packets
only. It does not authorize retroactive enforcement on legacy packets, public
claim changes, or any Phase 1+ work.
