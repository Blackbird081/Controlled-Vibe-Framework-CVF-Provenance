"""Disposable offline illustrations of selected learning; no project/runtime proof."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import uuid
import zipfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def manifest(entries):
    return {name: {'size': len(data), 'sha256': digest(data)} for name, data in entries.items()}


def run(runtime):
    runtime = runtime.resolve()
    runtime.mkdir(parents=True, exist_ok=True)
    # Retain the owned fixture for inspection; no recursive cleanup.
    repo = Path(tempfile.mkdtemp(prefix='archive-fixture-', dir=runtime)).resolve()
    assert repo.is_relative_to(runtime)
    def git(*args):
        return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.PIPE)
    git('init', '-q')
    git('config', 'core.autocrlf', 'false')
    (repo / '.gitattributes').write_bytes(b'payload.txt text eol=crlf\n')
    (repo / 'payload.txt').write_bytes(b'first\nsecond\n')
    git('add', '.gitattributes', 'payload.txt')
    git('-c', 'user.name=Offline fixture', '-c', 'user.email=fixture@example.invalid',
        'commit', '-qm', 'disposable archive input')
    archive = repo / 'input.zip'
    git('archive', '--format=zip', '-o', str(archive), 'HEAD')
    with zipfile.ZipFile(archive) as z:
        members = {n: z.read(n) for n in z.namelist() if not n.endswith('/')}
        z.extractall(repo / 'extracted')
    extracted = {p.relative_to(repo / 'extracted').as_posix(): p.read_bytes()
                 for p in (repo / 'extracted').rglob('*') if p.is_file()}
    blobs = {n: git('show', 'HEAD:' + n) for n in members}
    cases = []
    def check(name, assertion):
        assert assertion, name
        cases.append({'name': name, 'result': 'PASS'})
    check('archive-member-positive', manifest(members) == manifest(extracted))
    check('raw-blob-comparison-separate', manifest(blobs) != manifest(extracted))
    tampered = dict(extracted, **{'payload.txt': b'changed\n'})
    check('archive-tamper-negative', manifest(members) != manifest(tampered))
    missing = {n: b for n, b in extracted.items() if n != 'payload.txt'}
    check('archive-missing-member-negative', manifest(members) != manifest(missing))
    valid = str(uuid.UUID('12345678-1234-4234-8234-123456789abc'))
    def allowed(value):
        try:
            return str(uuid.UUID(value)) == value
        except ValueError:
            return False
    check('domain-positive-before-negative', allowed(valid) and not allowed('invalid-id'))
    # Synthetic state only, with deliberately different returned and durable layers.
    prior = {'summary': ['stored-prefix'], 'checkpoint': 1}
    fallback = {**prior, 'status': 'error'}
    blocked = {**prior, 'status': 'running'}
    returned = {'status': 'error', 'summary': ['stored-prefix', 'not-stored']}
    check('fallback-status-is-not-terminal-summary',
          fallback['status'] == returned['status'] and fallback['summary'] != returned['summary'])
    check('blocked-fallback-keeps-prefix', blocked['status'] != returned['status']
          and blocked['summary'] == prior['summary'] and blocked['checkpoint'] == 1)
    def valid_receipt(data):
        return set(data) == {'kind', 'events'} and data['kind'] == 'RAW_RECEIPT' and isinstance(data['events'], list)
    check('publication-shape-positive', valid_receipt({'kind': 'RAW_RECEIPT', 'events': []}))
    check('publication-summary-miswrite-negative', not valid_receipt({'summary': 'derived'}))
    return {'schemaVersion': 'ccma.parentLearningProbe@1', 'evidenceClass': 'SYNTHETIC_OFFLINE',
            'cases': cases, 'archiveSha256': digest(archive.read_bytes()),
            'archiveSourceRef': git('rev-parse', 'HEAD').decode().strip(),
            'archiveMembers': manifest(members), 'rawBlobs': manifest(blobs),
            'gitVersion': git('--version').decode().strip(),
            'configuration': {'core.autocrlf': False, 'gitattributes': 'payload.txt text eol=crlf'},
            'claimLimit': 'Actual disposable Git/archive bytes plus synthetic UUID/state/shape examples. '
                          'No Customer Care tests, database, provider, agent-adherence or general effectiveness proof.'}


if __name__ == '__main__':
    result = run(Path(sys.argv[1]))
    result['scriptSha256'] = digest(Path(__file__).read_bytes())
    Path(sys.argv[2]).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(f"PASS: {len(result['cases'])} bounded offline checks")
