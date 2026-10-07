"""Synthetic scanner boundaries in disposable roots; never read local credentials."""
import json
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_cvf_release_gate_bundle as bundle


class ReleaseSecretScanBoundaryTests(unittest.TestCase):
    def test_pinned_fixture_requires_path_file_line_and_number(self):
        synthetic = 'sk-' + 'Z' * 32
        content = synthetic + '\nclean\n'
        rel = '.private_reference/mirror/test.yaml'
        pin = (rel, hashlib.sha256(content.encode()).hexdigest(), 1,
               hashlib.sha256(synthetic.encode()).hexdigest())
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / rel
            path.parent.mkdir(parents=True)
            path.write_bytes(content.encode())
            with mock.patch.object(bundle, 'REPO_ROOT', root), mock.patch.object(
                bundle, 'RELEASE_SECRET_FIXTURE_FINGERPRINTS', {pin}
            ):
                self.assertEqual(bundle.check_secrets(False).status, 'PASS')
                self.assertFalse(bundle.is_allowed_secret_line(path, synthetic, 2))
                self.assertFalse(bundle.is_allowed_secret_line(path, synthetic + 'x', 1))
                self.assertFalse(bundle.is_allowed_secret_line(path, synthetic))
                # PEM bodies and every other byte are bound, not just the header.
                path.write_bytes((content + 'changed body\n').encode())
                self.assertEqual(bundle.check_secrets(False).status, 'FAIL')
                path.write_bytes(content.encode())
                moved = path.with_name('moved.yaml')
                path.rename(moved)
                self.assertEqual(bundle.check_secrets(False).status, 'FAIL')

    def scan(self, root):
        with mock.patch.object(bundle, 'REPO_ROOT', root):
            return bundle.check_secrets(False)

    def test_test_paths_and_placeholder_substrings_do_not_hide_secrets(self):
        synthetic = 'sk-' + 'Z' * 32
        for name in ['tests/fixture.py', 'src/route.test.ts', 'src/route.spec.ts', 'packet.html']:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(synthetic + ' # placeholder dummy ...\n', encoding='utf-8')
                result = self.scan(root)
                self.assertEqual(result.status, 'FAIL')
                self.assertNotIn(synthetic, json.dumps(result.__dict__))

    def test_unreadable_target_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'invalid.py').write_bytes(b'\xffinvalid-utf8')
            result = self.scan(root)
            self.assertEqual(result.status, 'FAIL')
            self.assertIn('invalid.py', '\n'.join(result.detail))

    def test_skipped_directories_are_pruned_and_counts_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skip = root / 'node_modules'
            skip.mkdir()
            (skip / 'hidden.py').write_text('sk-' + 'Z' * 32, encoding='utf-8')
            (root / 'clean.py').write_text('print(1)\n', encoding='utf-8')
            result = self.scan(root)
            self.assertEqual(result.status, 'PASS')
            self.assertEqual(result.name, 'Secrets scan')
            self.assertIn('filesScanned=1', '\n'.join(result.detail))
            self.assertIn('skippedDirectories=1', '\n'.join(result.detail))

    def test_exact_private_exception_does_not_expand_to_changed_line_or_path(self):
        rel, line = sorted(bundle.PRIVATE_REFERENCE_SECRET_ALLOWLIST)[0]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with mock.patch.object(bundle, 'REPO_ROOT', root):
                self.assertTrue(bundle.is_allowed_secret_line(root / rel, line))
                self.assertFalse(bundle.is_allowed_secret_line(root / rel, line + ' changed'))
                self.assertFalse(bundle.is_allowed_secret_line(root / 'tests/moved.py', line))

    def test_root_runtime_archive_is_pruned_without_exempting_other_cvf_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            archived = root / '.cvf/runtime/archive/fixture.ts'
            archived.parent.mkdir(parents=True)
            archived.write_text('sk-' + 'Z' * 32, encoding='utf-8')
            (root / 'clean.py').write_text('print(1)\n', encoding='utf-8')
            result = self.scan(root)
            self.assertEqual(result.status, 'PASS')
            self.assertIn('filesScanned=1', '\n'.join(result.detail))
            for rel in ['.cvf/authority.ts', 'src/runtime/fixture.ts', 'src/.cvf/runtime/fixture.ts']:
                with self.subTest(rel=rel):
                    path = root / rel
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text('sk-' + 'Z' * 32, encoding='utf-8')
                    result = self.scan(root)
                    self.assertEqual(result.status, 'FAIL')
                    self.assertNotIn('sk-' + 'Z' * 32, json.dumps(result.__dict__))
                    path.unlink()


if __name__ == '__main__':
    unittest.main()
