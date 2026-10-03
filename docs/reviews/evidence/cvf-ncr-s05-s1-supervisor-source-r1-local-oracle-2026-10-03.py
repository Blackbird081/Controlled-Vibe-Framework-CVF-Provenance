"""Independent returned-source AST/identity review; no worker code evaluation."""
import ast
import copy
import hashlib
import json
from pathlib import Path

worker_path=Path('docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-r1-worker-2026-10-03.json')
worker=json.loads(worker_path.read_text(encoding='utf-8'))
receipt=json.loads(Path('docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-r1-inputs-2026-10-03.json').read_text(encoding='utf-8'))
root=Path(worker['sourceRoot'])
expected=set(receipt['sourceFiles'])
checks=[]
def check(name,passed,details=None):
    checks.append({'id':name,'passed':bool(passed),'details':details})
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
ledger={r['path']:r for r in worker['sourceLedger']}
observed={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
check('exact-file-set',observed==expected==set(ledger))
trees={}
rows=[]
for rel in sorted(expected):
    raw=(root/rel).read_bytes()
    row={'path':rel,'bytes':len(raw),'rawSha256':hashlib.sha256(raw).hexdigest()}
    rows.append(row)
    check('identity:'+rel,row['rawSha256']==ledger[rel]['sha256'] and row['bytes']==ledger[rel]['bytes'])
    check('line-cap:'+rel,len(raw.decode('utf-8').splitlines())<=(1200 if rel.endswith('.py') else 600))
    if rel.endswith('.py'):trees[rel]=ast.parse(raw.decode('utf-8'),filename=rel)
check('external-byte-cap',sum(r['bytes'] for r in rows)<=1048576)
manifest=json.loads((root/'evidence/source-manifest.json').read_text(encoding='utf-8'))
check('manifest-thirteen-join',{r['path'] for r in manifest['files']}==expected-{'evidence/source-manifest.json'} and all(r['sha256']==ledger[r['path']]['sha256'] and r['bytes']==ledger[r['path']]['bytes'] for r in manifest['files']))
for p,h in receipt['frozenOriginalArtifacts'].items():check('frozen-artifact:'+p,digest(p)==h)
for r in receipt['frozenOriginalSourceLedger']:check('frozen-source:'+r['path'],digest(Path(receipt['frozenOriginalRoot'])/r['path'])==r['sha256'])
for r in receipt['inputIdentities']:check('release-input:'+r['path'],digest(r['path'])==r['rawSha256'])
proof=worker['proofIds']['PROOF-RETURN']
check('PROOF-RETURN-join',digest(proof['path'])==proof['rawSha256'] and Path(proof['path']).stat().st_size==proof['bytes'])

def functions(tree):return {n.name:n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef)}
def calls(node,name):return [n for n in ast.walk(node) if isinstance(n,ast.Call) and ((isinstance(n.func,ast.Name) and n.func.id==name) or (isinstance(n.func,ast.Attribute) and n.func.attr==name))]
def constants(node,value):return [n for n in ast.walk(node) if isinstance(n,ast.Constant) and n.value==value]
def feature_results(collection):
    ec=collection['src/envelope_contract.py'];sp=collection['src/supervisor.py'];ba=collection['src/boundary_admission.py']
    e=functions(ec);s=functions(sp);b=functions(ba)
    imports=[n for n in ast.walk(sp) if isinstance(n,(ast.Import,ast.ImportFrom))]
    result={}
    result['F01-sibling-imports-only']=len(imports)==3 and all(isinstance(n,ast.ImportFrom) and n.level==1 for n in imports) and not any(isinstance(n,ast.Try) for n in ast.walk(sp))
    elapsed=s['record_phase_elapsed']
    candidate=next((n.lineno for n in ast.walk(elapsed) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='candidate' for t in n.targets)),10**9)
    writes=[n.lineno for n in ast.walk(elapsed) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Attribute) and t.attr=='elapsed_seconds' for t in n.targets)]
    guards=calls(elapsed,'is_finite_nonnegative_number')
    result['F02-finite-before-mutation']=len(guards)>=3 and len(writes)==1 and candidate<writes[0] and all(n.lineno<writes[0] for n in guards) and bool(calls(e['is_finite_nonnegative_number'],'isfinite'))
    validator=e['validate_envelope']
    result['F03-tree-first-and-enum-type-guards']=bool(calls(validator,'scan_tree')) and calls(validator,'scan_tree')[0].lineno<min(n.lineno for n in ast.walk(validator) if isinstance(n,ast.Compare) and any(isinstance(op,(ast.In,ast.NotIn)) for op in n.ops)) and len(calls(validator,'type'))>=8 and bool(constants(e['_walk'],'CYCLE_DETECTED')) and bool(constants(e['_walk'],'NESTING_TOO_DEEP'))
    result['F04-digest-fullmatch']=bool(calls(e['is_sha256_digest'],'fullmatch')) and bool(calls(b['evaluate_boundary'],'fullmatch')) and not calls(e['is_sha256_digest'],'match')
    result['F04-output-hash-exact-join']=bool(constants(validator,'OUTPUT_WITHOUT_HASH')) and bool(constants(validator,'HASH_KEY_WITHOUT_OUTPUT')) and len(calls(validator,'_collision_reasons'))==2
    val=s['validate'];initial_guard=val.body[1]
    result['F05-state-before-assignment']=isinstance(initial_guard,ast.If) and bool(constants(initial_guard,'NEW')) is False and any(isinstance(n,ast.Raise) for n in ast.walk(initial_guard)) and initial_guard.lineno<min(n.lineno for n in ast.walk(val) if isinstance(n,ast.Assign))
    seal=s['seal_source_plan']
    result['F05-seal-rechecks-and-refuses']=bool(calls(seal,'validate_envelope')) and len(calls(seal,'_reject_at_seal'))==2 and bool(calls(seal,'decide_admission'))
    result['F06-lexical-prefix-device-policy']=bool(constants(e['_segment_reason'],'PATH_RESERVED_DEVICE_NAME')) and bool(constants(e['_segment_reason'],'PATH_TRAILING_DOT_OR_SPACE')) and bool(constants(e['_collision_reasons'],'_FILE_DESCENDANT_COLLISION')) and bool(calls(e['_collision_reasons'],'casefold'))
    result['F07-whole-value-sentinel']=all(bool(calls(fn,'strip')) and bool(calls(fn,'casefold')) and bool(constants(fn,'unknown')) and any(isinstance(n,ast.Compare) and any(isinstance(op,ast.Eq) for op in n.ops) for n in ast.walk(fn)) for fn in [e['is_unknown_sentinel'],b['_is_unknown_sentinel']])
    banned={'open','eval','exec','compile','__import__','Popen','socket','connect','write_bytes','write_text'}
    effect_nodes=[]
    for rel,tree in collection.items():
        for n in ast.walk(tree):
            if isinstance(n,ast.Import) and any(a.name not in {'math','re'} for a in n.names):effect_nodes.append(rel+':import')
            if isinstance(n,ast.Call):
                name=n.func.id if isinstance(n.func,ast.Name) else n.func.attr if isinstance(n.func,ast.Attribute) else ''
                regex=isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='re' and name=='compile'
                if name in banned and not regex:effect_nodes.append(rel+':call')
    result['no-enabled-effect-call-or-import']=not effect_nodes
    result['six-fixture-builders']=all('fixtures/fx_'+x+'.py' in collection and 'build_plan' in functions(collection['fixtures/fx_'+x+'.py']) for x in ['d1','m1','t1','b1','n1','l1'])
    launch=[n for n in ast.walk(sp) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Attribute) and t.attr=='launch_authority' for t in n.targets)]
    result['launch-no-go']=bool(launch) and all(isinstance(n.value,ast.Constant) and n.value.value=='NO_GO' for n in launch)
    backend=next(n for n in collection['src/windows_job.py'].body if isinstance(n,ast.ClassDef) and n.name=='WindowsJobBackend')
    methods=[n for n in backend.body if isinstance(n,ast.FunctionDef) and n.name!='unresolved_evidence']
    result['eight-os-methods-unavailable']=len(methods)==8 and all(any(isinstance(n,ast.Raise) and isinstance(n.exc,ast.Call) and isinstance(n.exc.func,ast.Name) and n.exc.func.id=='NotAdmitted' for n in ast.walk(m)) for m in methods)
    flags=[]
    for tree in collection.values():
        for n in ast.walk(tree):
            if isinstance(n,ast.Dict):
                flags.extend(v for k,v in zip(n.keys,n.values) if isinstance(k,ast.Constant) and k.value=='os_action_enabled')
    result['source-os-flags-false']=len(flags)>=8 and all(isinstance(v,ast.Constant) and v.value is False for v in flags)
    result['working-set-not-limit']=bool(constants(s['memory_fields'],'working_set_used_for_limit')) and any(isinstance(n,ast.Dict) and any(isinstance(k,ast.Constant) and k.value=='working_set_used_for_limit' and isinstance(v,ast.Constant) and v.value is False for k,v in zip(n.keys,n.values)) for n in ast.walk(s['memory_fields']))
    return result

features=feature_results(trees)
for name,passed in features.items():check(name,passed)
mutations=[]
variants=[('relative-import-level','src/supervisor.py','F01-sibling-imports-only'),('finite-guard-rename','src/supervisor.py','F02-finite-before-mutation'),('digest-match','src/envelope_contract.py','F04-digest-fullmatch'),('missing-hash-join','src/envelope_contract.py','F04-output-hash-exact-join'),('missing-seal-refusal','src/supervisor.py','F05-seal-rechecks-and-refuses'),('missing-device-reason','src/envelope_contract.py','F06-lexical-prefix-device-policy'),('substring-sentinel','src/envelope_contract.py','F07-whole-value-sentinel'),('native-import','src/windows_job.py','no-enabled-effect-call-or-import')]
for label,rel,target in variants:
    modified=copy.deepcopy(trees)
    tree=modified[rel]
    if label=='native-import':tree.body.extend(ast.parse('import ctypes').body)
    for n in ast.walk(tree):
        if label=='relative-import-level' and isinstance(n,ast.ImportFrom):n.level=0
        if label=='finite-guard-rename' and isinstance(n,ast.Attribute) and n.attr=='is_finite_nonnegative_number':n.attr='unguarded_number'
        if label=='digest-match' and isinstance(n,ast.Attribute) and n.attr=='fullmatch':n.attr='match'
        if label=='missing-hash-join' and isinstance(n,ast.Constant) and n.value=='OUTPUT_WITHOUT_HASH':n.value='JOIN_REMOVED'
        if label=='missing-seal-refusal' and isinstance(n,ast.Attribute) and n.attr=='_reject_at_seal':n.attr='_permit_seal'
        if label=='missing-device-reason' and isinstance(n,ast.Constant) and n.value=='PATH_RESERVED_DEVICE_NAME':n.value='DEVICE_GUARD_REMOVED'
        if label=='substring-sentinel' and isinstance(n,ast.FunctionDef) and n.name=='is_unknown_sentinel':n.body=ast.parse("return type(value) is str and 'unknown' in value.strip().casefold()").body
    mutations.append({'id':label,'detected':not feature_results(modified)[target],'kind':'AST_ONLY_NEVER_EVALUATED'})
check('oracle-eight-negative-mutations',all(r['detected'] for r in mutations),mutations)
pending=[r for r in worker['writeLedger'] if 'PLANNED' in r.get('result','')]
result={'schemaVersion':'cvf.s05.s1R1LocalIndependentStaticProbe.v1','actor':'local-s05-s1-r1-independent-reviewer','sourceExecutionCount':0,'workerEvidenceRawSha256':digest(worker_path),'oracleRawSha256':digest(__file__),'checks':checks,'sourceLedger':rows,'features':features,'mutations':mutations,'pendingWriteEvents':pending,'sourceReviewVerdict':'PASS_STATIC_REPAIR_CORRESPONDENCE' if all(c['passed'] for c in checks) else 'STATIC_FINDINGS','closureVerdict':'WITHHELD_PENDING_FINAL_WRITE_EVENT_CORROBORATION','claimBoundary':'Identity/AST correspondence and static deductions, not behaviour/OS proof; historical create mode not independently observed.'}
Path('.cvf/runtime/s05-s1-r1-local-probe-evidence.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'passed':sum(c['passed'] for c in checks),'total':len(checks),'mutationsDetected':sum(m['detected'] for m in mutations),'bytes':sum(r['bytes'] for r in rows),'sourceReviewVerdict':result['sourceReviewVerdict'],'closureVerdict':result['closureVerdict']}))
