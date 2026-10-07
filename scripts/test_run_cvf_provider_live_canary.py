"""Secret-source and subprocess-model boundary regressions; no provider calls."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import run_cvf_provider_live_canary as canary


class CanarySourceTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.web = Path(self.directory.name)
        self.cfg = dict(canary.PROVIDER_CONFIGS['alibaba'])
        self.web_patch = patch.object(canary, 'CVF_WEB', self.web)
        self.web_patch.start()
        self.addCleanup(self.web_patch.stop)
        self.env_patch = patch.dict(canary.os.environ, {}, clear=True)
        self.env_patch.start()
        self.addCleanup(self.env_patch.stop)

    def local(self, text='ALIBABA_API_KEY=fixture-local\n'):
        (self.web / '.env.local').write_text(text, encoding='utf-8')

    def test_auto_preserves_environment_precedence_and_reports_difference(self):
        self.local()
        canary.os.environ['ALIBABA_API_KEY'] = 'fixture-environment'
        key, report = canary.resolve_credentials(self.cfg)
        self.assertEqual(key, 'fixture-environment')
        self.assertEqual(report['selectedSource'], 'environment')
        self.assertTrue(report['sourcesDiffer'])

    def test_explicit_local_ignores_process_key(self):
        self.local()
        canary.os.environ['ALIBABA_API_KEY'] = 'fixture-environment'
        self.assertEqual(canary.resolve_api_key(self.cfg, 'local'), 'fixture-local')

    def test_explicit_environment_does_not_fall_back_to_local(self):
        self.local()
        self.assertIsNone(canary.resolve_api_key(self.cfg, 'environment'))

    def test_explicit_local_does_not_fall_back_to_environment(self):
        canary.os.environ['ALIBABA_API_KEY'] = 'fixture-environment'
        self.assertIsNone(canary.resolve_api_key(self.cfg, 'local'))

    def test_bom_export_quoted_key_and_blank_environment(self):
        self.local('\ufeffexport ALIBABA_API_KEY="fixture-local"\n')
        canary.os.environ['ALIBABA_API_KEY'] = '  '
        self.assertEqual(canary.resolve_api_key(self.cfg), 'fixture-local')

    def test_matching_sources_do_not_report_conflict(self):
        self.local()
        canary.os.environ['ALIBABA_API_KEY'] = 'fixture-local'
        _, report = canary.resolve_credentials(self.cfg)
        self.assertFalse(report['sourcesDiffer'])

    def test_source_report_never_contains_credential_values(self):
        self.local()
        canary.os.environ['ALIBABA_API_KEY'] = 'fixture-environment'
        _, report = canary.resolve_credentials(self.cfg)
        serialized = json.dumps(report)
        self.assertNotIn('fixture-environment', serialized)
        self.assertNotIn('fixture-local', serialized)

    def test_unknown_source_is_rejected(self):
        with self.assertRaises(ValueError):
            canary.resolve_api_key(self.cfg, 'other')

    def test_alibaba_subprocess_receives_requested_model_and_selected_key(self):
        self.cfg['model'] = 'fixture-requested-model'
        with patch.object(canary.subprocess, 'run') as run:
            run.return_value.returncode = 0
            self.assertEqual(canary.run_tests(self.cfg, 'fixture-selected', self.web / 'out.json'), 0)
            env = run.call_args.kwargs['env']
            self.assertEqual(env['ALIBABA_API_KEY'], 'fixture-selected')
            self.assertEqual(env['CVF_CANARY_ALIBABA_MODEL'], 'fixture-requested-model')

    def test_other_provider_subprocess_does_not_receive_alibaba_model_override(self):
        with patch.object(canary.subprocess, 'run') as run:
            canary.run_tests(canary.PROVIDER_CONFIGS['deepseek'], 'fixture-selected', self.web / 'out.json')
            self.assertNotIn('CVF_CANARY_ALIBABA_MODEL', run.call_args.kwargs['env'])

    def test_live_collection_opt_in_preserves_injected_execution_grant(self):
        with patch.dict(canary.os.environ, {'CVF_PROVIDER_EXECUTION_GRANT_ID': 'fixture-grant'}), patch.object(canary.subprocess, 'run') as run:
            canary.run_tests(self.cfg, 'fixture-selected', self.web / 'out.json')
            self.assertIn('--mode live', run.call_args.args[0])
            self.assertEqual(run.call_args.kwargs['env']['CVF_PROVIDER_EXECUTION_GRANT_ID'], 'fixture-grant')

    def test_failed_process_is_not_downgraded_to_skip(self):
        receipt = canary.build_receipt({}, self.cfg, process_exit_code=1)
        self.assertEqual(receipt['overall_status'], 'FAIL')
        self.assertEqual(receipt['process_exit_code'], 1)

    def test_failed_process_cannot_produce_pass_from_partial_json(self):
        results = [{'title': x['template_id'], 'status': 'passed'} for x in canary.SCENARIOS]
        receipt = canary.build_receipt({'testResults': [{'assertionResults': results}]}, self.cfg, 1)
        self.assertEqual(receipt['overall_status'], 'FAIL')

    def test_missing_required_scenarios_cannot_produce_pass_even_on_exit_zero(self):
        results = [{'title': canary.SCENARIOS[0]['template_id'], 'status': 'passed'}]
        receipt = canary.build_receipt({'testResults': [{'assertionResults': results}]}, self.cfg, 0)
        self.assertEqual(receipt['overall_status'], 'FAIL')
        self.assertEqual(receipt['skip_count'], 5)

    def test_cli_explicit_source_and_model_reach_run_and_safe_receipt(self):
        self.local()
        canary.os.environ['ALIBABA_API_KEY'] = 'fixture-environment'
        seen = {}
        def fake_run(cfg, key, path):
            seen.update(cfg=cfg, key=key)
            results = [{'title': x['template_id'], 'status': 'passed', 'duration': 1} for x in canary.SCENARIOS]
            path.write_text(json.dumps({'testResults': [{'assertionResults': results}]}), encoding='utf-8')
            return 0
        with patch.object(canary.sys, 'argv', ['canary', '--provider', 'alibaba', '--key-source', 'local', '--model', 'fixture-model']), patch.object(canary, 'run_tests', side_effect=fake_run), contextlib.redirect_stdout(io.StringIO()) as stdout, contextlib.redirect_stderr(io.StringIO()) as stderr:
            with self.assertRaises(SystemExit) as stop:
                canary.main()
        self.assertEqual(stop.exception.code, 0)
        self.assertEqual(seen['key'], 'fixture-local')
        self.assertEqual(seen['cfg']['model'], 'fixture-model')
        receipt = canary.build_receipt({}, seen['cfg'])
        self.assertEqual(receipt['credential_source']['selectedSource'], 'local')
        self.assertNotIn('fixture-local', stdout.getvalue() + stderr.getvalue() + json.dumps(receipt))
        self.assertNotIn('fixture-environment', stdout.getvalue() + stderr.getvalue() + json.dumps(receipt))


if __name__ == '__main__':
    unittest.main()
