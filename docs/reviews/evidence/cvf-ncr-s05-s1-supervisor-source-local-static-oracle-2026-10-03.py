"""Local AST/identity oracle. Never import, compile or evaluate worker source."""
from pathlib import Path
import ast
import copy
import hashlib
import json
import subprocess
import time

started = time.monotonic()
root = Path(r'D:\UNG DUNG AI\TOOL AI 2026\CVF-NCR-S05-S1-SOURCE-20261003')
worker_path = Path('docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-worker-2026-10-03.json')
worker = json.loads(worker_path.read_text(encoding='utf-8'))
expected = {'README.md', 'WORKER_RETURN.md', 'evidence/source-manifest.json',
            'evidence/requirement-map.json', 'src/supervisor.py', 'src/envelope_contract.py',
            'src/windows_job.py', 'src/boundary_admission.py'}
expected |= {'fixtures/fx_' + name + '.py' for name in ('d1', 'm1', 't1', 'b1', 'n1', 'l1')}
actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
ledger = {r['path']: r for r in worker['sourceLedger']}
manifest = json.loads((root / 'evidence/source-manifest.json').read_text(encoding='utf-8'))
checks = []
def check(name, ok, detail=None):
    checks.append({'id': name, 'passed': bool(ok), 'detail': detail})
check('exact-file-set', actual == expected == set(ledger), sorted(actual))
rows = []
trees = {}
for rel in sorted(expected):
    raw = (root / rel).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    rows.append({'path': rel, 'bytes': len(raw), 'sha256': digest})
    check('identity:' + rel, digest == ledger[rel]['sha256'] and len(raw) == ledger[rel]['bytes'])
    text = raw.decode('utf-8')
    check('line-cap:' + rel, len(text.splitlines()) <= (1200 if rel.endswith('.py') else 600))
    if rel.endswith('.py'):
        trees[rel] = ast.parse(text, filename=rel)
        check('syntax:' + rel, True)
check('manifest-13-join', {r['path'] for r in manifest['files']} == expected - {'evidence/source-manifest.json'}
      and all(r['sha256'] == ledger[r['path']]['sha256'] and r['bytes'] == ledger[r['path']]['bytes'] for r in manifest['files']))
check('byte-cap', sum(r['bytes'] for r in rows) <= 1048576)

def shape_issues(collection):
    issues = []
    allowed_imports = {'math', 'ntpath', 're', 'envelope_contract', 'boundary_admission', 'windows_job'}
    banned_calls = {'open', 'exec', 'eval', 'compile', '__import__', 'Popen', 'run', 'system', 'socket', 'connect', 'write_text', 'write_bytes'}
    for rel, tree in collection.items():
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                if any(a.name.split('.')[0] not in allowed_imports for a in node.names):
                    issues.append(rel + ':effect-import')
            if isinstance(node, ast.ImportFrom) and node.module and node.module.split('.')[0] not in allowed_imports:
                issues.append(rel + ':effect-import')
            if isinstance(node, ast.Call):
                name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr if isinstance(node.func, ast.Attribute) else ''
                regex_compile = isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id == 're' and name == 'compile'
                if name in banned_calls and not regex_compile:
                    issues.append(rel + ':effect-call')
            if isinstance(node, ast.Dict):
                for key, val in zip(node.keys, node.values):
                    if isinstance(key, ast.Constant) and key.value == 'os_action_enabled' and not (isinstance(val, ast.Constant) and val.value is False):
                        issues.append(rel + ':os-action-enabled')
            if isinstance(node, ast.Assign) and any(isinstance(t, ast.Attribute) and t.attr == 'launch_authority' for t in node.targets):
                if not (isinstance(node.value, ast.Constant) and node.value.value == 'NO_GO'):
                    issues.append(rel + ':launch-enabled')
    for name in ('d1', 'm1', 't1', 'b1', 'n1', 'l1'):
        rel = 'fixtures/fx_' + name + '.py'
        if rel not in collection or not any(isinstance(n, ast.FunctionDef) and n.name == 'build_plan' for n in collection[rel].body):
            issues.append(rel + ':fixture-missing')
    return issues

check('effect-interface-shape', not shape_issues(trees), shape_issues(trees))
backend = next(n for n in trees['src/windows_job.py'].body if isinstance(n, ast.ClassDef) and n.name == 'WindowsJobBackend')
methods = [n for n in backend.body if isinstance(n, ast.FunctionDef) and n.name != 'unresolved_evidence']
check('eight-backend-methods-refuse', len(methods) == 8 and all(any(isinstance(n, ast.Raise) and isinstance(n.exc, ast.Call) and isinstance(n.exc.func, ast.Name) and n.exc.func.id == 'NotAdmitted' for n in ast.walk(m)) for m in methods))
mutations = []
for label, rel, snippet in [('native-import', 'src/windows_job.py', 'import ctypes'),
                            ('import-time-effect', 'src/supervisor.py', "open('probe.txt', 'w')"),
                            ('fake-capability-launch', 'src/supervisor.py', "self.launch_authority = 'ALLOW'"),
                            ('fixture-os-enable', 'fixtures/fx_n1.py', "{'os_action_enabled': True}")]:
    modified = copy.deepcopy(trees)
    modified[rel].body.extend(ast.parse(snippet).body)
    mutations.append({'id': label, 'detected': bool(shape_issues(modified)), 'kind': 'AST_ONLY_NEVER_EXECUTED'})
modified = dict(trees)
del modified['fixtures/fx_l1.py']
mutations.append({'id': 'missing-FX-L1', 'detected': bool(shape_issues(modified)), 'kind': 'AST_ONLY_NEVER_EXECUTED'})
check('oracle-negative-sensitivity', all(m['detected'] for m in mutations), mutations)
counterexamples = [
 {'id': 'deadline-nonfinite', 'inputs': ['seconds=NaN', 'seconds=+Infinity', 'two finite phases whose sum overflows'], 'expected': 'reject before mutation', 'staticObservation': 'record_phase_elapsed checks type and seconds<0 only; no finite guard on input or sum', 'executed': False},
 {'id': 'unhashable-enum', 'inputs': ['envelope_version=[]', 'stage={}', 'effects=[[]]'], 'expected': 'structured rejection, no unhandled exception', 'staticObservation': 'set membership occurs without string/type guard', 'executed': False},
 {'id': 'hash-binding', 'inputs': ['outputs=[a.txt], artifact_hashes={}', 'case-colliding artifact hash keys', '64 hex characters plus terminal newline'], 'expected': 'explicit nonempty one-to-one output/hash binding and strict digest', 'staticObservation': 'hash mapping may be empty; no output/hash reconciliation, no hash-key collision check; regex uses $ with match rather than fullmatch', 'executed': False},
 {'id': 'path-name-policy', 'inputs': ['CON', 'NUL.txt', 'file plus descendant file/x', 'root with trailing dot or space'], 'expected': 'explicit admitted Windows lexical policy or rejection', 'staticObservation': 'reserved device names and file/directory prefix collisions unhandled; root lacks trailing-dot/space guard', 'executed': False},
 {'id': 'unknown-substring', 'inputs': ['custody_owner=KnownUnknownsTeam'], 'expected': 'document whether sentinel-only or substring policy', 'staticObservation': 'unknown regex search scans all strings including dict keys', 'executed': False},
 {'id': 'import-custody', 'inputs': ['ImportError inside package dependency', 'ambient sys.path sibling name'], 'expected': 'sibling-only import or fail closed', 'staticObservation': 'broad ImportError catch switches all dependencies to absolute imports', 'executed': False},
]
result = {'schemaVersion': 'cvf.s05.s1LocalStaticAudit.v1', 'head': subprocess.check_output(['git','rev-parse','HEAD'], text=True).strip(),
          'role': 'LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER', 'sourceRoot': str(root),
          'workerEvidenceSha256': hashlib.sha256(worker_path.read_bytes()).hexdigest(),
          'oracleSha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'checks': checks, 'sourceLedger': rows, 'mutations': mutations,
          'counterexamplePlans': counterexamples, 'sourceExecutionCount': 0,
          'probeDisposition': 'EXECUTED_STATIC_ONLY_FINDINGS', 'sourceAcceptance': 'WITHHELD_CONSOLIDATED_FINDINGS',
          'elapsedSeconds': round(time.monotonic() - started, 3),
          'claimBoundary': 'Identity/AST checks and static deductions only. No worker source import/evaluation/compilation or runtime behavior proof.'}
Path('.cvf/runtime/s05-s1-local-static-audit-evidence.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({'checksPassed': sum(c['passed'] for c in checks), 'checksTotal': len(checks), 'negativeAstMutationsDetected': sum(m['detected'] for m in mutations), 'sourceBytes': sum(r['bytes'] for r in rows), 'disposition': result['sourceAcceptance'], 'sourceExecutionCount': 0}))
