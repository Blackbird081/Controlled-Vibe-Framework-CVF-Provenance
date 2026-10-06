"""Result rendering only: no subprocess or provider execution."""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_cvf_release_gate_bundle as bundle


class ReleaseResultConsistencyTests(unittest.TestCase):
    def assert_consistent(self, checks, sot3=None, expected='FAIL'):
        payload = bundle.result_payload(checks, '2026-10-06', sot3=sot3)
        self.assertEqual(payload['gate_result'], expected)
        text = io.StringIO()
        with contextlib.redirect_stdout(text):
            console_exit = bundle.print_results(checks, '2026-10-06', payload=payload)
        self.assertIn(f'GATE RESULT: {expected}', text.getvalue())
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            json_exit = bundle.json_output(payload)
        self.assertEqual(json.loads(output.getvalue()), payload)
        self.assertEqual(console_exit, json_exit)
        self.assertEqual(json_exit, 0 if expected == 'PASS' else 1)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'result.json'
            bundle.write_json_payload(payload, path)
            self.assertEqual(json.loads(path.read_text(encoding='utf-8')), payload)

    def test_status_matrix(self):
        for status in ['PASS', 'WARN', 'FAIL', 'SKIP', 'ABSENT', 'UNKNOWN']:
            with self.subTest(status=status):
                self.assert_consistent([bundle.CheckResult('Required check', status, 'synthetic')],
                                       expected='PASS' if status in ['PASS', 'WARN'] else 'FAIL')

    def test_empty_list_is_not_release_evidence(self):
        self.assert_consistent([])

    def test_sot3_payload_matrix(self):
        for evidence in [None, {}, {'overall': 'FAIL'}, {'overall': 'SKIP'}, {'overall': 'ABSENT'}, {'overall': 'PASS'}]:
            with self.subTest(evidence=evidence):
                self.assert_consistent([bundle.CheckResult('SOT3 proof', 'PASS', 'synthetic')], evidence,
                                       'PASS' if evidence == {'overall': 'PASS'} else 'FAIL')

    def test_skip_cannot_be_overridden_by_pass_payload(self):
        self.assert_consistent([bundle.CheckResult('SOT3 proof', 'SKIP', 'dry-run')], {'overall': 'PASS'})

    def test_legacy_console_call_and_non_release_exception(self):
        checks = [bundle.CheckResult('SOT3 proof', 'PASS', 'synthetic')]
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(bundle.print_results(checks, '2026-10-06'), 1)
        self.assert_consistent([bundle.CheckResult('UI structure only', 'PASS', 'synthetic')], expected='PASS')


if __name__ == '__main__':
    unittest.main()
