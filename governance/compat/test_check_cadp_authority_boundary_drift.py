#!/usr/bin/env python3
"""
Focused tests for the CADP-AI-T4 authority boundary drift checker.

Covers: real-repository positive proof; strict fixture schema negatives;
one isolated negative-corpus mutation per named violation code; package-
export block-qualification (missing symbol, wrong module, same-token
collision outside the export block); deterministic ordering; --json
--enforce exit behavior; and byte-for-byte corpus preservation after a
checker run.

Standard-library only (unittest). No installed third-party package is
required; the file is also pytest-collectible.
"""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CHECKER_PATH = REPO_ROOT / "governance" / "compat" / "check_cadp_authority_boundary_drift.py"
REAL_FIXTURE_PATH = REPO_ROOT / "governance" / "compat" / "fixtures" / "cadp_authority_boundary_contract.v1.json"

sys.path.insert(0, str(CHECKER_PATH.parent))
import check_cadp_authority_boundary_drift as checker  # noqa: E402


# ---------------------------------------------------------------------------
# Known-good corpus: minimal mini-repository mirroring the real T1/T3A/T3B
# authority-boundary shape (contract version, literal-false fields, package
# export blocks) closely enough to exercise every checker code in isolation.
# ---------------------------------------------------------------------------

GOOD_FIXTURE: dict = {
    "schemaVersion": "cadp-authority-boundary-contract.v1",
    "surfaces": [
        {
            "surfaceId": "T1_GUARD_CONTRACT",
            "contractPath": "contracts/t1.contract.ts",
            "packageRootPath": None,
            "versionSymbol": "CADP_CONTRACT_VERSION",
            "versionValue": "cvf.cadp.v1",
            "falseAuthorityFields": ["executionAuthorized", "rawSecretsAllowed"],
            "requiredExportSymbols": [],
            "requiredExportModule": None,
            "forbiddenSeamTokens": ["child_process", "process.env"],
        },
        {
            "surfaceId": "T3A_CONSUMER",
            "contractPath": "contracts/t3a.contract.ts",
            "packageRootPath": "index.ts",
            "versionSymbol": "CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION",
            "versionValue": "cvf.cadp.consumer.v1",
            "falseAuthorityFields": ["executionAuthorized"],
            "requiredExportSymbols": ["CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION", "evaluateCadpCapabilityConsumer"],
            "requiredExportModule": "./t3a.contract",
            "forbiddenSeamTokens": ["child_process", "process.env"],
        },
    ],
}

T1_CONTRACT_GOOD = """
export const CADP_CONTRACT_VERSION = 'cvf.cadp.v1' as const;

export interface CapabilityAdmissionRecord {
  readonly executionAuthorized: false;
  readonly rawSecretsAllowed: false;
}

function build(): CapabilityAdmissionRecord {
  return {
    executionAuthorized: false,
    rawSecretsAllowed: false,
  };
}

function validate(record: CapabilityAdmissionRecord, issues: unknown[]): void {
  requireExactFalse(record, 'rawSecretsAllowed', '$.rawSecretsAllowed', issues, 'RAW_SECRET_INCLUDED', 'no raw secrets');
}
"""

T3A_CONTRACT_GOOD = """
export const CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION = 'cvf.cadp.consumer.v1' as const;

export interface Projection {
  readonly executionAuthorized: false;
}

function build(): Projection {
  return {
    executionAuthorized: false,
  };
}

export function evaluateCadpCapabilityConsumer() {}
"""

INDEX_TS_GOOD = """
// T3A export block
export {
  CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION,
  evaluateCadpCapabilityConsumer,
} from "./t3a.contract";
"""


def _build_good_corpus(root: Path) -> None:
    (root / "contracts").mkdir(parents=True, exist_ok=True)
    (root / "contracts" / "t1.contract.ts").write_text(T1_CONTRACT_GOOD, encoding="utf-8")
    (root / "contracts" / "t3a.contract.ts").write_text(T3A_CONTRACT_GOOD, encoding="utf-8")
    (root / "index.ts").write_text(INDEX_TS_GOOD, encoding="utf-8")
    fixtures_dir = root / "governance" / "compat" / "fixtures"
    fixtures_dir.mkdir(parents=True, exist_ok=True)
    (fixtures_dir / "cadp_authority_boundary_contract.v1.json").write_text(
        json.dumps(GOOD_FIXTURE, indent=2), encoding="utf-8",
    )


def _fixture_path(root: Path) -> Path:
    return root / "governance" / "compat" / "fixtures" / "cadp_authority_boundary_contract.v1.json"


def _write_fixture(root: Path, fixture_obj: dict) -> None:
    _fixture_path(root).write_text(json.dumps(fixture_obj, indent=2), encoding="utf-8")


def _run_checker_inprocess(root: Path, fixture_path: Path | None = None) -> tuple[dict, list]:
    fp = fixture_path if fixture_path is not None else _fixture_path(root)
    return checker.run_checks(root, fp)


def _snapshot_tree(root: Path) -> dict[str, str]:
    snapshot: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if path.is_file():
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            snapshot[str(path.relative_to(root)).replace("\\", "/")] = digest
    return snapshot


class TempCorpusTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._tmpdir = tempfile.mkdtemp(prefix="cadp_t4_corpus_")
        self.root = Path(self._tmpdir)
        _build_good_corpus(self.root)

    def tearDown(self) -> None:
        shutil.rmtree(self._tmpdir, ignore_errors=True)


class TestRealRepositoryPositive(unittest.TestCase):
    def test_real_repository_passes_with_three_surfaces_and_zero_violations(self) -> None:
        report, violations = checker.run_checks(REPO_ROOT, REAL_FIXTURE_PATH)
        self.assertEqual(report["checkedSurfaceCount"], 3)
        self.assertEqual(report["violationCount"], 0)
        self.assertEqual(violations, [])

    def test_real_repository_cli_json_enforce_exits_zero(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CHECKER_PATH), "--json", "--enforce"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["violationCount"], 0)
        self.assertEqual(payload["checkedSurfaceCount"], 3)


class TestGoodCorpusBaseline(TempCorpusTestCase):
    def test_good_corpus_passes_with_zero_violations(self) -> None:
        report, violations = _run_checker_inprocess(self.root)
        self.assertEqual(report["checkedSurfaceCount"], 2)
        self.assertEqual(violations, [])

    def test_checker_execution_leaves_corpus_byte_for_byte_unchanged(self) -> None:
        before = _snapshot_tree(self.root)
        _run_checker_inprocess(self.root)
        # Also exercise the CLI entry point, which performs its own file reads.
        subprocess.run(
            [sys.executable, str(CHECKER_PATH), "--json", "--enforce",
             "--repo-root", str(self.root), "--fixture", str(_fixture_path(self.root))],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        after = _snapshot_tree(self.root)
        self.assertEqual(before, after)

    def test_deterministic_ordering_across_repeated_runs(self) -> None:
        # Introduce multiple simultaneous violations so ordering is meaningful.
        t1_path = self.root / "contracts" / "t1.contract.ts"
        t1_path.write_text(T1_CONTRACT_GOOD.replace("cvf.cadp.v1", "cvf.cadp.v2"), encoding="utf-8")
        index_path = self.root / "index.ts"
        index_path.write_text("// no export block here\n", encoding="utf-8")

        _, violations_first = _run_checker_inprocess(self.root)
        _, violations_second = _run_checker_inprocess(self.root)
        self.assertGreaterEqual(len(violations_first), 2)
        self.assertEqual(
            [v.to_dict() for v in violations_first],
            [v.to_dict() for v in violations_second],
        )
        codes = [v.code for v in violations_first]
        self.assertEqual(codes, sorted(codes))


class TestFixtureSchemaNegatives(TempCorpusTestCase):
    def _assert_schema_invalid(self, mutated_fixture) -> None:
        _write_fixture(self.root, mutated_fixture)
        report, violations = _run_checker_inprocess(self.root)
        self.assertTrue(any(v.code == "FIXTURE_SCHEMA_INVALID" for v in violations), msg=report)

    def test_malformed_json_is_schema_invalid(self) -> None:
        _fixture_path(self.root).write_text("{ not valid json", encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        self.assertTrue(any(v.code == "FIXTURE_SCHEMA_INVALID" for v in violations), msg=report)

    def test_unknown_top_level_key_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        mutated["unexpectedTopKey"] = True
        self._assert_schema_invalid(mutated)

    def test_unknown_surface_key_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        mutated["surfaces"][0]["extraKey"] = "nope"
        self._assert_schema_invalid(mutated)

    def test_missing_surface_key_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        del mutated["surfaces"][0]["forbiddenSeamTokens"]
        self._assert_schema_invalid(mutated)

    def test_duplicate_surface_id_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        mutated["surfaces"][1]["surfaceId"] = mutated["surfaces"][0]["surfaceId"]
        self._assert_schema_invalid(mutated)

    def test_duplicate_contract_path_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        mutated["surfaces"][1]["contractPath"] = mutated["surfaces"][0]["contractPath"]
        self._assert_schema_invalid(mutated)

    def test_absolute_path_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        mutated["surfaces"][0]["contractPath"] = "/etc/passwd"
        self._assert_schema_invalid(mutated)

    def test_parent_traversal_path_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        mutated["surfaces"][0]["contractPath"] = "../../etc/passwd"
        self._assert_schema_invalid(mutated)

    def test_wrong_scalar_type_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        mutated["surfaces"][0]["versionSymbol"] = 12345
        self._assert_schema_invalid(mutated)

    def test_empty_required_collection_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        mutated["surfaces"][0]["falseAuthorityFields"] = []
        self._assert_schema_invalid(mutated)

    def test_empty_forbidden_seam_collection_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        mutated["surfaces"][0]["forbiddenSeamTokens"] = []
        self._assert_schema_invalid(mutated)

    def test_duplicate_package_root_path_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        extra = copy.deepcopy(mutated["surfaces"][1])
        extra["surfaceId"] = "T3B_DUPLICATE_ROOT"
        extra["contractPath"] = "contracts/t3b.contract.ts"
        extra["versionSymbol"] = "T3B_VERSION"
        extra["versionValue"] = "v1"
        mutated["surfaces"].append(extra)
        self._assert_schema_invalid(mutated)

    def test_wrong_schema_version_is_schema_invalid(self) -> None:
        mutated = copy.deepcopy(GOOD_FIXTURE)
        mutated["schemaVersion"] = "cadp-authority-boundary-contract.v0"
        self._assert_schema_invalid(mutated)


class TestSurfaceMissing(TempCorpusTestCase):
    def test_missing_contract_path_is_surface_missing(self) -> None:
        (self.root / "contracts" / "t1.contract.ts").unlink()
        report, violations = _run_checker_inprocess(self.root)
        self.assertTrue(any(v.code == "SURFACE_MISSING" and v.surface_id == "T1_GUARD_CONTRACT" for v in violations), msg=report)
        # Focused: no unrelated code should be required to detect this.
        t1_codes = {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"}
        self.assertEqual(t1_codes, {"SURFACE_MISSING"})

    def test_missing_package_root_path_is_surface_missing(self) -> None:
        (self.root / "index.ts").unlink()
        report, violations = _run_checker_inprocess(self.root)
        self.assertTrue(any(v.code == "SURFACE_MISSING" and v.surface_id == "T3A_CONSUMER" for v in violations), msg=report)


class TestContractVersionDrift(TempCorpusTestCase):
    def test_version_value_drift_is_detected(self) -> None:
        path = self.root / "contracts" / "t1.contract.ts"
        path.write_text(T1_CONTRACT_GOOD.replace("cvf.cadp.v1", "cvf.cadp.v1-drifted"), encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t1_codes = {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"}
        self.assertIn("CONTRACT_VERSION_DRIFT", t1_codes)

    def test_version_symbol_removed_is_detected(self) -> None:
        path = self.root / "contracts" / "t1.contract.ts"
        path.write_text(T1_CONTRACT_GOOD.replace("CADP_CONTRACT_VERSION", "RENAMED_VERSION_SYMBOL"), encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t1_codes = {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"}
        self.assertIn("CONTRACT_VERSION_DRIFT", t1_codes)

    def test_version_declaration_decoy_inside_string_does_not_pass(self) -> None:
        path = self.root / "contracts" / "t1.contract.ts"
        mutated = T1_CONTRACT_GOOD.replace(
            "export const CADP_CONTRACT_VERSION = 'cvf.cadp.v1' as const;",
            "const decoy = \"CADP_CONTRACT_VERSION = 'cvf.cadp.v1'\";",
        )
        path.write_text(mutated, encoding="utf-8")
        _, violations = _run_checker_inprocess(self.root)
        self.assertIn("CONTRACT_VERSION_DRIFT", {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"})


class TestAuthorityWidening(TempCorpusTestCase):
    def test_field_widened_to_boolean_type_is_detected(self) -> None:
        path = self.root / "contracts" / "t1.contract.ts"
        mutated = T1_CONTRACT_GOOD.replace(
            "readonly executionAuthorized: false;",
            "readonly executionAuthorized: boolean;",
        )
        path.write_text(mutated, encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t1_codes = {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"}
        self.assertIn("AUTHORITY_TYPE_WIDENED", t1_codes)

    def test_field_widened_to_true_value_is_detected(self) -> None:
        """Widening only the value-position assignment (interface type position
        left untouched) must be detected as AUTHORITY_VALUE_WIDENED without
        requiring the unrelated AUTHORITY_TYPE_WIDENED code -- the two checks
        are independent."""
        path = self.root / "contracts" / "t1.contract.ts"
        mutated = T1_CONTRACT_GOOD.replace(
            "    executionAuthorized: false,\n    rawSecretsAllowed: false,",
            "    executionAuthorized: true,\n    rawSecretsAllowed: false,",
        )
        path.write_text(mutated, encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t1_codes = {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"}
        self.assertIn("AUTHORITY_VALUE_WIDENED", t1_codes)
        self.assertNotIn("AUTHORITY_TYPE_WIDENED", t1_codes)

    def test_output_assignment_removed_is_value_widened(self) -> None:
        path = self.root / "contracts" / "t1.contract.ts"
        mutated = T1_CONTRACT_GOOD.replace(
            "    executionAuthorized: false,\n",
            "",
        )
        path.write_text(mutated, encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t1_codes = {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"}
        self.assertIn("AUTHORITY_VALUE_WIDENED", t1_codes)

    def test_requireexactfalse_validator_call_alone_satisfies_value_position(self) -> None:
        """rawSecretsAllowed has no object-literal value assignment in the good
        corpus's validate() function shape by itself -- only the
        requireExactFalse(...) runtime-validator call. This must independently
        satisfy the value-position check, matching the real T1 source idiom for
        caller-input fields that are never re-emitted as an output literal."""
        path = self.root / "contracts" / "t1.contract.ts"
        # Remove the object-literal assignment but keep the requireExactFalse call.
        mutated = T1_CONTRACT_GOOD.replace("    rawSecretsAllowed: false,\n", "")
        path.write_text(mutated, encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t1_codes = {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"}
        self.assertNotIn("AUTHORITY_VALUE_WIDENED", t1_codes)

    def test_requireexactfalse_call_removed_is_value_widened(self) -> None:
        """Removing both the object-literal assignment and the
        requireExactFalse(...) call must be detected."""
        path = self.root / "contracts" / "t1.contract.ts"
        mutated = T1_CONTRACT_GOOD.replace("    rawSecretsAllowed: false,\n", "")
        mutated = mutated.replace(
            "  requireExactFalse(record, 'rawSecretsAllowed', '$.rawSecretsAllowed', issues, 'RAW_SECRET_INCLUDED', 'no raw secrets');\n",
            "",
        )
        path.write_text(mutated, encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t1_codes = {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"}
        self.assertIn("AUTHORITY_VALUE_WIDENED", t1_codes)

    def test_nonliteral_value_cannot_be_masked_by_unrelated_false_decoy(self) -> None:
        path = self.root / "contracts" / "t1.contract.ts"
        mutated = T1_CONTRACT_GOOD.replace(
            "    executionAuthorized: false,",
            "    executionAuthorized: computeAuthority(),",
        )
        mutated += "\nconst unrelated = { executionAuthorized: false };\n"
        path.write_text(mutated, encoding="utf-8")
        _, violations = _run_checker_inprocess(self.root)
        self.assertIn("AUTHORITY_VALUE_WIDENED", {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"})

    def _assert_computed_key_is_widened(self, computed_assignment: str) -> None:
        path = self.root / "contracts" / "t1.contract.ts"
        mutated = T1_CONTRACT_GOOD.replace(
            "    executionAuthorized: false,",
            computed_assignment,
        )
        mutated += "\nconst unrelated = { executionAuthorized: false };\n"
        path.write_text(mutated, encoding="utf-8")
        _, violations = _run_checker_inprocess(self.root)
        self.assertIn("AUTHORITY_VALUE_WIDENED", {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"})

    def test_computed_quoted_authority_key_is_widened(self) -> None:
        self._assert_computed_key_is_widened('    ["executionAuthorized"]: true,')

    def test_computed_template_authority_key_is_widened(self) -> None:
        self._assert_computed_key_is_widened("    [`executionAuthorized`]: true,")

    def test_computed_dynamic_key_is_fail_closed(self) -> None:
        self._assert_computed_key_is_widened("    [authorityFieldName]: true,")


class TestForbiddenExecutionSeam(TempCorpusTestCase):
    def test_child_process_token_family_is_detected(self) -> None:
        path = self.root / "contracts" / "t1.contract.ts"
        path.write_text(T1_CONTRACT_GOOD + "\nimport { exec } from 'child_process';\n", encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t1_codes = {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"}
        self.assertIn("FORBIDDEN_EXECUTION_SEAM", t1_codes)

    def test_process_env_token_family_is_detected_independently(self) -> None:
        path = self.root / "contracts" / "t3a.contract.ts"
        path.write_text(T3A_CONTRACT_GOOD + "\nconst key = process.env.SECRET;\n", encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t3a_codes = {v.code for v in violations if v.surface_id == "T3A_CONSUMER"}
        self.assertIn("FORBIDDEN_EXECUTION_SEAM", t3a_codes)
        # Isolated: unrelated surface (T1) must remain clean.
        t1_codes = {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"}
        self.assertEqual(t1_codes, set())

    def test_forbidden_token_inside_string_is_not_a_seam(self) -> None:
        path = self.root / "contracts" / "t1.contract.ts"
        path.write_text(T1_CONTRACT_GOOD + "\nconst prose = 'child_process';\n", encoding="utf-8")
        _, violations = _run_checker_inprocess(self.root)
        self.assertNotIn("FORBIDDEN_EXECUTION_SEAM", {v.code for v in violations if v.surface_id == "T1_GUARD_CONTRACT"})


class TestPackageExportDrift(TempCorpusTestCase):
    def test_missing_root_symbol_is_detected(self) -> None:
        mutated_index = INDEX_TS_GOOD.replace(
            "  evaluateCadpCapabilityConsumer,\n", "",
        )
        (self.root / "index.ts").write_text(mutated_index, encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t3a_codes = {v.code for v in violations if v.surface_id == "T3A_CONSUMER"}
        self.assertIn("PACKAGE_EXPORT_DRIFT", t3a_codes)

    def test_wrong_module_specifier_is_detected(self) -> None:
        mutated_index = INDEX_TS_GOOD.replace("./t3a.contract", "./t3a.contract.renamed")
        (self.root / "index.ts").write_text(mutated_index, encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t3a_codes = {v.code for v in violations if v.surface_id == "T3A_CONSUMER"}
        self.assertIn("PACKAGE_EXPORT_DRIFT", t3a_codes)

    def test_same_token_outside_export_block_does_not_satisfy_requirement(self) -> None:
        """A required symbol appearing elsewhere in index.ts (not inside the
        module-qualified export block) must NOT satisfy package discoverability
        -- this is the export-block-qualification collision case."""
        mutated_index = (
            "// decoy: symbol mentioned in a comment, not exported\n"
            "// evaluateCadpCapabilityConsumer is referenced here only as prose\n"
            "export { someOtherThing } from './unrelated.module';\n"
        )
        (self.root / "index.ts").write_text(mutated_index, encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t3a_codes = {v.code for v in violations if v.surface_id == "T3A_CONSUMER"}
        self.assertIn("PACKAGE_EXPORT_DRIFT", t3a_codes)

    def test_symbol_present_in_unrelated_export_block_does_not_satisfy_requirement(self) -> None:
        """Required symbols exported from a different module specifier must not
        satisfy the requirement for this surface's own module."""
        mutated_index = (
            "export {\n"
            "  CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION,\n"
            "  evaluateCadpCapabilityConsumer,\n"
            "} from \"./some/other/wrong/module\";\n"
        )
        (self.root / "index.ts").write_text(mutated_index, encoding="utf-8")
        report, violations = _run_checker_inprocess(self.root)
        t3a_codes = {v.code for v in violations if v.surface_id == "T3A_CONSUMER"}
        self.assertIn("PACKAGE_EXPORT_DRIFT", t3a_codes)


class TestCliJsonEnforceOnCorpus(TempCorpusTestCase):
    def test_enforce_exit_nonzero_on_violation(self) -> None:
        (self.root / "contracts" / "t1.contract.ts").unlink()
        proc = subprocess.run(
            [sys.executable, str(CHECKER_PATH), "--json", "--enforce",
             "--repo-root", str(self.root), "--fixture", str(_fixture_path(self.root))],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        self.assertNotEqual(proc.returncode, 0)
        payload = json.loads(proc.stdout)
        self.assertGreater(payload["violationCount"], 0)

    def test_advisory_mode_without_enforce_exits_zero_but_reports_violations(self) -> None:
        (self.root / "contracts" / "t1.contract.ts").unlink()
        proc = subprocess.run(
            [sys.executable, str(CHECKER_PATH), "--json",
             "--repo-root", str(self.root), "--fixture", str(_fixture_path(self.root))],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        self.assertEqual(proc.returncode, 0)
        payload = json.loads(proc.stdout)
        self.assertGreater(payload["violationCount"], 0)


if __name__ == "__main__":
    unittest.main()
