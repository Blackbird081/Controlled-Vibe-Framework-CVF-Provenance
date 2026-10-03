"""Reviewer-only documentary identity/provenance probe; no worker code execution."""
from pathlib import Path
import copy
import hashlib
import json
import ntpath

ROOT = Path(__file__).resolve().parents[3]
RETURN = 'docs/reviews/CVF_CVF_NCR_S05_S1_R1_EVIDENCE_RELAY_WORKER_RETURN_2026-10-03.md'
WORKER = 'docs/reviews/evidence/cvf-ncr-s05-s1-r1-evidence-relay-worker-2026-10-03.json'
INPUT = 'docs/reviews/evidence/cvf-ncr-s05-s1-r1-evidence-relay-inputs-2026-10-03.json'
OUTPUT = 'docs/reviews/evidence/cvf-ncr-s05-s1-r1-evidence-relay-local-probe-2026-10-03.json'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def observations(evidence):
    """Check joins and epistemic labels, never authenticate a past event."""
    receipt = json.loads((ROOT / INPUT).read_bytes())
    ret = (ROOT / RETURN).read_bytes()
    checks = {}
    proof = evidence['proofIds']['PROOF-RETURN']
    checks['return-join'] = (proof['path'] == RETURN and proof['rawSha256'] == digest(ret)
                             and proof['bytes'] == len(ret))
    checks['blocked-preserved'] = (evidence['status'] == 'BLOCKED_WITH_REASON'
                                   and evidence['eventDisposition'] == 'INCOMPLETE_RETAINED_EVENT'
                                   and evidence['requirementResults']['REQ-2'] == 'BLOCKED')
    checks['base-binding'] = evidence['executionBaseHead'] == 'cc3114dff7b208fd7413d4a1880dd53add828f76'
    events = {event['eventId']: event for event in evidence['historicalEvents']}
    creation = events['EVT-CREATE-R1-JSON']
    gate = events['EVT-GATE-R1-RETURN']
    target = evidence['historicalTarget']['evidencePath']
    actual = (ROOT / target).read_bytes()
    checks['creation-identity'] = (creation['reportedSha256'] == digest(actual)
                                    and creation['reportedBytes'] == len(actual)
                                    and creation['reportedLines'] == actual.count(b'\n'))
    expected_path = ntpath.normpath(str(ROOT / target))
    checks['creation-target'] = ntpath.normpath(creation['target']['resolvedPath']) == expected_path
    checks['creation-command-exclusive'] = 'with open(path, "xb") as fh:' in creation['commandIdentity']['excerptFromToolCallInput']
    checks['mode-not-os-proof'] = creation['modeLabelInOutput']['class'] == 'WORKER_ASSERTION'
    checks['creation-time-qualified'] = (creation['eventUtc']['class'] == 'TOOL_OUTPUT (script clock)'
                                        and creation['eventUtc']['value'] == '2026-10-03T11:49:16.478881+00:00')
    for event in events.values():
        checks['transcription-digest:' + event['eventId']] = (
            digest(event['rawToolOutputText'].encode('utf-8')) == event['rawToolOutputSha256OfTranscribedText'])
    checks['creation-command-transcription-digest'] = (
        digest(creation['commandIdentity']['excerptFromToolCallInput'].encode('utf-8'))
        == creation['commandIdentity']['excerptSha256OfTranscribedText'])
    checks['gate-command-transcription-digest'] = (
        digest(gate['commandIdentity']['text'].encode('utf-8'))
        == gate['commandIdentity']['textSha256OfTranscribedText'])
    checks['gate-time-missing-preserved'] = gate['eventUtc'] == 'MISSING'
    checks['gate-historical-hash-missing-preserved'] = gate['rawLog']['rawHashAtEventTime'] == 'MISSING'
    checks['command-original-hashes-missing'] = all(
        event['commandIdentity']['rawCommandTextHash'] == 'MISSING' for event in [creation, gate])
    checks['gate-current-hash-not-history'] = (
        evidence['currentObservations']['class'] == 'LOCAL_OR_CURRENT_OBSERVATION'
        and gate['rawLog']['rawHashAtEventTime'] == 'MISSING')
    for row in receipt['frozenWorkerArtifacts']:
        raw = (ROOT / row['path']).read_bytes()
        checks['frozen:' + row['path']] = digest(raw) == row['rawSha256'] and len(raw) == row['bytes']
    checks['no-source-effects-declared'] = (not evidence['preservationChecks']['sourceRootsTouched']
                                            and not evidence['preservationChecks']['r1WorkerArtifactsModified'])
    checks['stop-freeze'] = evidence['successorFreezeDisposition'] == 'FEATURE_SUCCESSORS_FROZEN'
    checks['old-c1-stop'] = evidence['preservationChecks']['oldC1']['counters'] == [0, 0, 1, 2]
    checks['output-budget'] = len(ret) + (ROOT / WORKER).stat().st_size <= 262144
    checks['line-budgets'] = len(ret.splitlines()) <= 620 and len((ROOT / WORKER).read_bytes().splitlines()) <= 950
    return checks


def main():
    raw = (ROOT / WORKER).read_bytes()
    evidence = json.loads(raw)
    checks = observations(evidence)
    mutations = []
    for name, edit in [
        ('wrong-return-digest', lambda e: e['proofIds']['PROOF-RETURN'].update(rawSha256='0' * 64)),
        ('wrong-historical-target-hash', lambda e: e['historicalEvents'][1].update(reportedSha256='0' * 64)),
        ('fresh-time-relabeled-historical', lambda e: e['historicalEvents'][2].update(eventUtc='2026-10-03T00:00:00Z')),
        ('fresh-hash-relabeled-historical', lambda e: e['historicalEvents'][2]['rawLog'].update(rawHashAtEventTime='0' * 64)),
        ('script-mode-relabeled-os-proof', lambda e: e['historicalEvents'][1]['modeLabelInOutput'].update(**{'class': 'OS_PROOF'})),
        ('blocked-relabeled-ready', lambda e: e.update(status='COMPLETE_PENDING_REVIEW')),
    ]:
        mutant = copy.deepcopy(evidence)
        edit(mutant)
        mutations.append({'id': name, 'detected': not all(observations(mutant).values())})
    result = {
        'schemaVersion': 'cvf.s05.r1EvidenceRelayLocalProbe@1',
        'actor': 'local-s05-r1-relay-reviewer',
        'workerEvidenceRawSha256': digest(raw),
        'workerReturnRawSha256': digest((ROOT / RETURN).read_bytes()),
        'oracleRawSha256': digest(Path(__file__).read_bytes()),
        'checks': [{'id': name, 'passed': passed} for name, passed in checks.items()],
        'mutations': mutations,
        'sourceExecutionCount': 0,
        'historicalWriterOrGateReruns': 0,
        'historicalAuthentication': 'NOT_ESTABLISHED_BY_TRANSCRIPTION_HASH',
        'result': 'PASS_DOCUMENTARY_JOIN_BLOCKED_HISTORY' if all(checks.values()) else 'FAIL_DOCUMENTARY_JOIN',
        'appendixCurrentIdentities': [{'path': path, 'bytes': (ROOT / path).stat().st_size,
                                      'rawSha256': digest((ROOT / path).read_bytes())} for path in [RETURN, WORKER]],
    }
    with (ROOT / OUTPUT).open('xb') as stream:
        stream.write((json.dumps(result, indent=2) + '\n').encode('utf-8'))
    print(json.dumps({'result': result['result'], 'checks': len(checks),
                      'passed': sum(checks.values()), 'mutationsDetected': sum(m['detected'] for m in mutations)}))
    return 0 if all(checks.values()) and all(m['detected'] for m in mutations) else 1


if __name__ == '__main__':
    raise SystemExit(main())
