# CVF GC-018 Release Gate Build Timeout Maintenance

Memory class: FULL_RECORD

Status: GC018_ACCEPTED_FOR_TIMEOUT_MAINTENANCE

docType: baseline

Date: 2026-05-21

---

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_RELEASE_GATE_BUILD_TIMEOUT_MAINTENANCE_ROADMAP_2026-05-21.md`
- `docs/reviews/CVF_HOSTED_PRODUCT_READINESS_PROOF_COMPLETION_2026-05-21.md`
- `scripts/run_cvf_release_gate_bundle.py`

---

## Purpose / Decision / Baseline

Decision: ACCEPTED for a single release-gate timeout maintenance edit.

The prior direct production build passed in about 468s, while the release gate
failed because the build subcheck used a 300s timeout. The accepted baseline is
to raise only that subcheck timeout to 900s and rerun the same mandatory gate.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: release-gate web build timeout maintenance.

Accepted work:

- update `check_web_build()` timeout in `scripts/run_cvf_release_gate_bundle.py`;
- rerun `python scripts/run_cvf_release_gate_bundle.py --json`;
- file completion and continuity updates.

---

## Scope / Proposed Tranche

In scope:

- `scripts/run_cvf_release_gate_bundle.py`;
- documentation artifacts for this maintenance tranche;
- active session queue/state/handoff updates.

Out of scope:

- application source changes;
- provider/runtime changes;
- test expectation changes;
- deployment/public-sync work;
- hosted SaaS claim or freeze release.

---

## Evidence / Required Evidence / Verification

Required verification:

- release-gate runner diff shows only the web build timeout maintenance;
- full release gate returns PASS;
- governance checks return PASS;
- no raw provider key or service token is printed or committed.

---

## Claim Boundary

This GC-018 authorizes only a timeout maintenance correction in the release
gate runner. It does not authorize broader readiness claims or product/runtime
changes.
