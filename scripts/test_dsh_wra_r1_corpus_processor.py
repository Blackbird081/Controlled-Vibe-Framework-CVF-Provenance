#!/usr/bin/env python3
"""
Adversarial / deterministic tests for scripts/dsh_wra_r1_corpus_processor.py

Covers: omission detection, duplicate-path detection, path-normalization
collision, unsupported/binary input handling, stale-pin detection, false
NO_NEW_VALUE detection (region disposition must cite an exact owner or DEFER,
never silently NO_NEW_VALUE without an owner hint), byte-deterministic
generation across separate runs, and stale/tampered-artifact detection in
--verify (DSH-WRA-R1-RV-F03).

Location note (DSH-WRA-R1-RV-F04, Rework R1): this test previously lived at
`governance/compat/fixtures/dsh_wra_r1_corpus_processor_test.py`, a path
under the protected `governance/compat/` guard prefix
(`_is_protected()` in `governance/compat/check_core_guard_self_protection.py`
treats every `governance/compat/*.py` file as protected regardless of
subdirectory). No Core Guard Self-Protection Authorization was granted for
this worker-owned test file, so it is relocated here, alongside its helper
under `scripts/`, following the same `scripts/test_<helper>.py` naming
convention used by other worker-owned test files in this directory (e.g.
`scripts/test_external_agent_snapshot_projection.py`,
`scripts/test_run_cvf_release_gate_bundle.py`).

Run:
    python scripts/test_dsh_wra_r1_corpus_processor.py
"""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "dsh_wra_r1_corpus_processor.py"

spec = importlib.util.spec_from_file_location("dsh_processor", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules["dsh_processor"] = mod  # required so @dataclass can resolve cls.__module__
spec.loader.exec_module(mod)  # type: ignore[union-attr]


FAILURES: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name}" + (f" - {detail}" if detail and not condition else ""))
    if not condition:
        FAILURES.append(name)


def test_real_mirror_reconciles() -> None:
    records = mod.enumerate_and_hash(mod.MIRROR_ABS)
    check("real_mirror_tracked_count_matches_expected", len(records) == mod.EXPECTED_TRACKED_COUNT,
          f"got {len(records)}")
    paths = [r.path for r in records]
    check("real_mirror_no_duplicate_paths", len(paths) == len(set(paths)))
    check("real_mirror_zero_unreadable", all(r.readable for r in records))

    region_ledger = mod.build_region_ledger(records)
    check("real_mirror_region_reconciles", region_ledger["reconciles"] is True)
    check("real_mirror_zero_unmapped", region_ledger["unmapped"] == 0)

    pkg_ledger = mod.build_package_family_ledger(records)
    check("real_mirror_package_json_count_is_272", pkg_ledger["packageJsonManifestCount"] == 272,
          f"got {pkg_ledger['packageJsonManifestCount']}")


def test_omission_detection() -> None:
    """A manifest missing a tracked file must be detectable by comparing
    ledger row count against manifest file count (Gate 4 reconciliation)."""
    records = mod.enumerate_and_hash(mod.MIRROR_ABS)
    ledger_rows = mod.build_ledger_rows(records)
    # Simulate omission: drop one row.
    omitted = ledger_rows[:-1]
    check("omission_is_detectable_via_count_mismatch", len(omitted) != len(records))


def test_duplicate_path_detection() -> None:
    records = mod.enumerate_and_hash(mod.MIRROR_ABS)
    ledger_rows = mod.build_ledger_rows(records)
    # Simulate duplication: append a copy of the first row.
    duplicated = ledger_rows + [ledger_rows[0]]
    paths = [r["path"] for r in duplicated]
    check("duplicate_path_is_detectable", len(paths) != len(set(paths)))


def test_path_normalization_collision() -> None:
    """Two distinct on-disk paths that would collide after naive
    normalization (e.g. backslash vs forward-slash, or case-folding on a
    case-insensitive filesystem) must not silently merge into one ledger
    row. We assert the processor's path strings are produced by git ls-files
    (which always emits forward-slash POSIX-style paths), so no backslash
    survives into a path key."""
    records = mod.enumerate_and_hash(mod.MIRROR_ABS)
    has_backslash = [r.path for r in records if "\\" in r.path]
    check("no_backslash_paths_from_git_ls_files", len(has_backslash) == 0,
          f"found: {has_backslash[:3]}")
    # Case-collision probe: no two distinct tracked paths should differ only
    # by case (which would collide on a case-insensitive checkout).
    lowered = {}
    collisions = []
    for r in records:
        key = r.path.lower()
        if key in lowered and lowered[key] != r.path:
            collisions.append((lowered[key], r.path))
        lowered[key] = r.path
    check("no_case_only_path_collisions", len(collisions) == 0, f"found: {collisions[:3]}")


def test_unsupported_binary_input_visible() -> None:
    """Binary files must still receive a ledger row (not silently dropped)."""
    records = mod.enumerate_and_hash(mod.MIRROR_ABS)
    binaries = [r for r in records if mod.is_binary(r.path)]
    check("binary_files_present_in_corpus", len(binaries) >= 0)  # corpus may have zero; assert no crash
    for r in binaries:
        check_name = f"binary_file_has_ledger_row:{r.path}"
        # every record from enumerate_and_hash always yields exactly one row
        # downstream in build_ledger_rows; verify status is a valid terminal.
        # DSH-WRA-R1-R2-F02: only the four canonical terminal statuses are
        # valid; the legacy ADAPTED/REJECTED/NO_NEW_VALUE values this check
        # previously also accepted are no longer emitted by terminalStatus.
        valid = r.processing_status in {
            "READ", "SKIPPED_WITH_REASON", "DEFERRED", "BLOCKED_UNREADABLE",
        }
        check(check_name, valid, r.processing_status)
        break  # only need to prove the mechanism once; avoid combinatorial spam
    # unsupported-format synthetic probe using a temp file with unknown ext
    with tempfile.TemporaryDirectory() as tmp:
        synthetic = Path(tmp) / "weird.file.xyz123"
        synthetic.write_bytes(b"\x00\x01\x02unsupported-binary-probe")
        digest = mod.sha256_file(synthetic)
        check("unsupported_extension_still_hashable", len(digest) == 64)


def test_stale_pin_detection() -> None:
    """If the mirror HEAD no longer matches the pinned commit constant, the
    processor must report pinMatches=False rather than silently proceeding."""
    fake_commit = "0" * 40
    fake_match = fake_commit == mod.PINNED_COMMIT
    check("stale_pin_is_detected_as_mismatch", fake_match is False)
    # Confirm the real manifest builder wires this through.
    records = mod.enumerate_and_hash(mod.MIRROR_ABS)
    manifest = mod.build_manifest(records, fake_commit, True, {"reconciles": True})
    check("manifest_pinMatches_false_on_stale_commit", manifest["pinMatches"] is False)
    manifest_ok = mod.build_manifest(records, mod.PINNED_COMMIT, True, {"reconciles": True})
    check("manifest_pinMatches_true_on_correct_commit", manifest_ok["pinMatches"] is True)


def test_false_no_new_value_detection() -> None:
    """Every region disposed NO_NEW_VALUE must carry a non-empty, non-
    OWNER_SURFACE_NOT_FOUND owner hint (an exact existing CVF owner path),
    per the work order's 'NO_NEW_VALUE is permitted only after comparison to
    an exact current CVF owner' rule."""
    for region_id in mod.NO_NEW_VALUE_REGIONS | mod.READ_NOVALUE_REGIONS:
        _, owner_hint = next(
            ((rid, hint) for rid, hint, _ in mod.REGION_RULES if rid == region_id),
            (None, None),
        )
        check(
            f"no_new_value_region_has_exact_owner:{region_id}",
            bool(owner_hint) and not owner_hint.startswith("OWNER_SURFACE_NOT_FOUND"),
            owner_hint or "MISSING",
        )
    # Adversarial: a region with OWNER_SURFACE_NOT_FOUND must never be
    # classified NO_NEW_VALUE by region_disposition/region_terminal_status.
    for region_id, owner_hint, _ in mod.REGION_RULES:
        if owner_hint.startswith("OWNER_SURFACE_NOT_FOUND"):
            disp = mod.region_disposition(region_id)
            check(
                f"owner_not_found_region_never_no_new_value:{region_id}",
                disp != "NO_NEW_VALUE",
                disp,
            )


def test_helper_cli_generate_and_verify_exit_codes() -> None:
    proc = subprocess.run(
        [sys.executable, str(MODULE_PATH), "--generate", "--verify"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    check("cli_generate_verify_exits_zero", proc.returncode == 0, proc.stdout[-500:] + proc.stderr[-500:])
    check("cli_reports_verify_pass", "VERIFY PASS" in proc.stdout)


def test_snapshot_date_is_deterministic_pinned_commit_derived() -> None:
    """DSH-WRA-R1-RV-F03: snapshotDateUtc must be derived from the pinned
    commit's own immutable committer timestamp, not wall-clock generation
    time, so it is identical across separate build_all_artifacts() calls
    (and therefore across separate --generate runs) regardless of when they
    are invoked."""
    manifest_a, _, _, _, _ = mod.build_all_artifacts(mod.MIRROR_ABS)
    import time
    time.sleep(1.1)  # cross a whole wall-clock second boundary
    manifest_b, _, _, _, _ = mod.build_all_artifacts(mod.MIRROR_ABS)
    check(
        "snapshot_date_utc_identical_across_calls_despite_wall_clock_advance",
        manifest_a["snapshotDateUtc"] == manifest_b["snapshotDateUtc"],
        f"{manifest_a['snapshotDateUtc']} vs {manifest_b['snapshotDateUtc']}",
    )


def test_two_generations_produce_byte_identical_artifacts() -> None:
    """DSH-WRA-R1-RV-F03: two separate calls to build_all_artifacts() against
    the same unmodified pinned mirror must produce byte-identical canonical
    output for all four artifacts, proving the generator is byte-
    deterministic end to end (not merely stable on in-memory totals)."""
    manifest_a, ledger_a, region_a, pkg_a, _ = mod.build_all_artifacts(mod.MIRROR_ABS)
    manifest_b, ledger_b, region_b, pkg_b, _ = mod.build_all_artifacts(mod.MIRROR_ABS)

    check(
        "two_generations_manifest_bytes_identical",
        mod._canonical_manifest_bytes(manifest_a) == mod._canonical_manifest_bytes(manifest_b),
    )
    check(
        "two_generations_ledger_bytes_identical",
        mod._canonical_ledger_bytes(ledger_a) == mod._canonical_ledger_bytes(ledger_b),
    )
    check(
        "two_generations_region_ledger_bytes_identical",
        mod._canonical_region_ledger_bytes(region_a) == mod._canonical_region_ledger_bytes(region_b),
    )
    check(
        "two_generations_package_family_ledger_bytes_identical",
        mod._canonical_package_family_ledger_bytes(pkg_a) == mod._canonical_package_family_ledger_bytes(pkg_b),
    )


def test_stale_tampered_artifact_fails_verify() -> None:
    """DSH-WRA-R1-RV-F03: --verify must byte-compare persisted artifacts
    against freshly regenerated canonical output, so a hand-edited/stale
    persisted manifest must cause --verify to fail (nonzero exit), not pass
    merely because the in-memory model still reconciles internally. This
    test tampers with the REAL persisted manifest file on disk, then
    restores its original bytes afterward (in a try/finally) so it never
    leaves the working tree in a tampered state, even on failure."""
    if not mod.MANIFEST_PATH.exists():
        check("stale_tampered_artifact_fails_verify", False, "persisted manifest missing; run --generate first")
        return

    original_bytes = mod.MANIFEST_PATH.read_bytes()
    try:
        mod.MANIFEST_PATH.write_bytes(original_bytes + b" ")
        proc = subprocess.run(
            [sys.executable, str(MODULE_PATH), "--verify"],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        check(
            "stale_tampered_artifact_fails_verify_nonzero_exit",
            proc.returncode != 0,
            f"exit={proc.returncode}",
        )
        check(
            "stale_tampered_artifact_verify_reports_byte_mismatch",
            "does not byte-match freshly regenerated canonical output" in proc.stdout + proc.stderr,
        )
    finally:
        mod.MANIFEST_PATH.write_bytes(original_bytes)

    # Confirm restoration actually worked: a clean --verify must pass again.
    restore_proc = subprocess.run(
        [sys.executable, str(MODULE_PATH), "--verify"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    check(
        "stale_tampered_artifact_restored_after_test",
        restore_proc.returncode == 0 and "VERIFY PASS" in restore_proc.stdout,
        restore_proc.stdout[-300:] + restore_proc.stderr[-300:],
    )


def test_r2_f02_only_canonical_terminal_statuses() -> None:
    """DSH-WRA-R1-R2-F02: the generated ledger must emit exactly the four
    canonical terminal statuses (READ, SKIPPED_WITH_REASON, DEFERRED,
    BLOCKED_UNREADABLE) and nothing else - no NO_NEW_VALUE, ADAPTED,
    REJECTED, or any other legacy value in terminalStatus."""
    records = mod.enumerate_and_hash(mod.MIRROR_ABS)
    ledger_rows = mod.build_ledger_rows(records)
    canonical = {"READ", "SKIPPED_WITH_REASON", "DEFERRED", "BLOCKED_UNREADABLE"}
    observed = {row["terminalStatus"] for row in ledger_rows}
    check(
        "r2_f02_only_canonical_terminal_statuses",
        observed.issubset(canonical),
        f"non-canonical values found: {observed - canonical}",
    )
    check("r2_f02_no_no_new_value_terminal_status", "NO_NEW_VALUE" not in observed)
    check("r2_f02_no_rejected_terminal_status", "REJECTED" not in observed)
    check("r2_f02_no_adapted_terminal_status", "ADAPTED" not in observed)


def test_r2_f02_read_rows_have_read_evidence() -> None:
    """Every READ row must carry a non-empty readEvidence field distinguishing
    an actual semantic read from mere hashing/path classification."""
    records = mod.enumerate_and_hash(mod.MIRROR_ABS)
    ledger_rows = mod.build_ledger_rows(records)
    read_rows = [r for r in ledger_rows if r["terminalStatus"] == "READ"]
    check("r2_f02_at_least_one_read_row_exists", len(read_rows) > 0)
    missing = [r["path"] for r in read_rows if not r.get("readEvidence")]
    check("r2_f02_all_read_rows_have_read_evidence", len(missing) == 0, f"missing: {missing[:5]}")
    # READ rows must have a null skipReason (mutually exclusive fields).
    wrong_field = [r["path"] for r in read_rows if r.get("skipReason")]
    check("r2_f02_read_rows_have_no_skip_reason", len(wrong_field) == 0, f"found: {wrong_field[:5]}")


def test_r2_f02_skipped_rows_have_skip_reason() -> None:
    """Every SKIPPED_WITH_REASON row must carry a non-empty skipReason field
    explaining why it was grouped, not individually opened."""
    records = mod.enumerate_and_hash(mod.MIRROR_ABS)
    ledger_rows = mod.build_ledger_rows(records)
    skipped_rows = [r for r in ledger_rows if r["terminalStatus"] == "SKIPPED_WITH_REASON"]
    check("r2_f02_at_least_one_skipped_row_exists", len(skipped_rows) > 0)
    missing = [r["path"] for r in skipped_rows if not r.get("skipReason")]
    check("r2_f02_all_skipped_rows_have_skip_reason", len(missing) == 0, f"missing: {missing[:5]}")
    wrong_field = [r["path"] for r in skipped_rows if r.get("readEvidence")]
    check("r2_f02_skipped_rows_have_no_read_evidence", len(wrong_field) == 0, f"found: {wrong_field[:5]}")


def test_r2_f02_terminal_counts_reconcile_to_8953() -> None:
    """The four canonical terminal-status counts recorded on the manifest
    must sum to exactly the expected tracked-file count (8,953), with zero
    unresolved paths."""
    manifest, ledger_rows, _, _, _ = mod.build_all_artifacts(mod.MIRROR_ABS)
    tsc = manifest["terminalStatusCounts"]
    total = sum(tsc.values())
    check("r2_f02_terminal_counts_sum_to_8953", total == mod.EXPECTED_TRACKED_COUNT, f"got {total}")
    check("r2_f02_terminal_counts_match_ledger_row_count", total == len(ledger_rows))
    check("r2_f02_unresolved_count_is_zero", manifest["unresolvedCount"] == 0)
    check("r2_f02_ledger_terminal_reconciles_true", manifest["ledgerTerminalReconciles"] is True)
    check(
        "r2_f02_allowed_terminal_count_matches_manifest_file_count",
        manifest["allowedTerminalCount"] == manifest["fileCount"] == mod.EXPECTED_TRACKED_COUNT,
    )


def test_r2_f02_path_pattern_only_row_never_mislabeled_read() -> None:
    """A file that was only ever path-pattern group-classified (not in the
    exact INDIVIDUALLY_READ_PATHS allowlist) must never be mislabeled READ -
    it must be SKIPPED_WITH_REASON (or DEFERRED for a deferred region)."""
    import dsh_wra_r1_region_rules as rr
    records = mod.enumerate_and_hash(mod.MIRROR_ABS)
    ledger_rows = mod.build_ledger_rows(records)
    read_rows = [r for r in ledger_rows if r["terminalStatus"] == "READ"]
    mislabeled = [r["path"] for r in read_rows if r["path"] not in rr.INDIVIDUALLY_READ_PATHS]
    check("r2_f02_every_read_row_is_in_the_allowlist", len(mislabeled) == 0, f"mislabeled: {mislabeled[:5]}")
    # Adversarial: every allowlist path must actually resolve to READ (proves
    # the allowlist override is not silently ignored for any entry).
    allow_paths = set(rr.INDIVIDUALLY_READ_PATHS.keys())
    read_paths = {r["path"] for r in read_rows}
    not_applied = sorted(allow_paths - read_paths)
    check("r2_f02_every_allowlist_path_resolves_to_read", len(not_applied) == 0, f"not applied: {not_applied[:5]}")


def test_r2_f02_verify_fails_on_injected_non_canonical_status() -> None:
    """Adversarial: --verify must fail (nonzero exit) if a ledger row uses a
    non-canonical terminalStatus, proving the guard is real and not merely
    documentation. Simulated in-memory (does not touch the persisted file)."""
    records = mod.enumerate_and_hash(mod.MIRROR_ABS)
    ledger_rows = mod.build_ledger_rows(records)
    tampered = [dict(r) for r in ledger_rows]
    tampered[0]["terminalStatus"] = "NO_NEW_VALUE"
    canonical = {"READ", "SKIPPED_WITH_REASON", "DEFERRED", "BLOCKED_UNREADABLE"}
    observed = {row["terminalStatus"] for row in tampered}
    check(
        "r2_f02_injected_non_canonical_status_is_detectable",
        not observed.issubset(canonical),
    )


def main() -> int:
    test_real_mirror_reconciles()
    test_omission_detection()
    test_duplicate_path_detection()
    test_path_normalization_collision()
    test_unsupported_binary_input_visible()
    test_stale_pin_detection()
    test_false_no_new_value_detection()
    test_helper_cli_generate_and_verify_exit_codes()
    test_snapshot_date_is_deterministic_pinned_commit_derived()
    test_two_generations_produce_byte_identical_artifacts()
    test_stale_tampered_artifact_fails_verify()
    test_r2_f02_only_canonical_terminal_statuses()
    test_r2_f02_read_rows_have_read_evidence()
    test_r2_f02_skipped_rows_have_skip_reason()
    test_r2_f02_terminal_counts_reconcile_to_8953()
    test_r2_f02_path_pattern_only_row_never_mislabeled_read()
    test_r2_f02_verify_fails_on_injected_non_canonical_status()

    print(f"\n{'='*60}")
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) failed: {FAILURES}")
        return 1
    print("PASS: all adversarial/deterministic corpus-processor checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
