"""Boundary tests for the Q001 candidate/artifact secret scan."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scan_cvf_q001_candidate_secrets as scanner


class Q001SecretScanTests(unittest.TestCase):
    def test_existing_fixture_exceptions_are_exact_and_candidate_has_no_unreviewed_hits(self):
        report = scanner.scan([(path, "candidate") for path in scanner.candidate_files()])
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["fixtureLinesAllowed"], 9)
        self.assertEqual(report["filesUnreadable"], 0)
        self.assertNotIn(scanner.REPO_ROOT / scanner.CANDIDATE / ".env.local", scanner.candidate_files())

    def test_new_test_fixture_secret_is_reported_without_printing_value(self):
        with tempfile.TemporaryDirectory(dir=scanner.REPO_ROOT / ".cvf" / "runtime") as directory:
            root = Path(directory)
            path = root / "route.test.ts"
            synthetic = "sk-" + "Z" * 32
            path.write_text("const fixture = '" + synthetic + "';\n", encoding="utf-8")
            report = scanner.scan([(path, "candidate")], candidate_root=root)
            self.assertEqual(report["status"], "FAIL")
            self.assertEqual(len(report["findings"]), 1)
            self.assertNotIn(synthetic, json.dumps(report))

            pat = "github_" + "pat_" + "Z" * 24
            path.write_text("const fixture = '" + pat + "';\n", encoding="utf-8")
            changed = scanner.scan([(path, "candidate")], candidate_root=root)
            self.assertEqual(changed["status"], "FAIL")
            self.assertNotIn(pat, json.dumps(changed))

    def test_artifact_secret_and_unreadable_artifact_fail_closed(self):
        with tempfile.TemporaryDirectory(dir=scanner.REPO_ROOT / ".cvf" / "runtime") as directory:
            root = Path(directory)
            artifact = root / "packet.html"
            synthetic = "sk-" + "Q" * 32
            artifact.write_text("<p>" + synthetic + "</p>", encoding="utf-8")
            report = scanner.scan([(artifact, "artifact")])
            self.assertEqual(report["status"], "FAIL")
            self.assertNotIn(synthetic, json.dumps(report))
            missing = scanner.scan([(root / "missing.html", "artifact")])
            self.assertEqual(missing["status"], "FAIL")
            self.assertEqual(missing["filesUnreadable"], 1)

    def test_changed_secret_at_allowlisted_fixture_location_is_not_exempt(self):
        with tempfile.TemporaryDirectory(dir=scanner.REPO_ROOT / ".cvf" / "runtime") as directory:
            root = Path(directory)
            path = root / "src/app/api/artifacts/export/route.test.ts"
            path.parent.mkdir(parents=True)
            synthetic = "github_" + "pat_" + "N" * 24
            path.write_text("\n" * 117 + synthetic + "\n", encoding="utf-8")
            report = scanner.scan([(path, "candidate")], candidate_root=root)
            self.assertEqual(report["status"], "FAIL")
            self.assertEqual(report["findings"][0]["line"], 118)
            self.assertNotIn(synthetic, json.dumps(report))


if __name__ == "__main__":
    unittest.main()
