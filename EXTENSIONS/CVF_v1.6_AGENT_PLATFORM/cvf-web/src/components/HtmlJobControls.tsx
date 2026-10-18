'use client';
import { useCallback, useEffect, useRef, useState } from 'react';
import { useSession } from 'next-auth/react';
import type { DraftSnapshot } from '@/lib/html-draft-recovery-contract';
import type { HtmlJob, HtmlJobDecision, HtmlJobVersion, JobCriterion } from '@/lib/html-job-contract';
import { ArtifactExportPanel, type ArtifactExportRequest, type DisplayedResult } from './ArtifactExportPanel';
import { HtmlDraftRecovery } from './HtmlDraftRecovery';
import { clearPendingJobJournal, readPendingJobJournal, writePendingJobJournal, type PendingJobJournal } from './useHtmlBuildAttempts';

type Props = { sourceRecordId: string; initialRequest: Partial<ArtifactExportRequest> };
type VersionState = 'current' | 'stale' | 'unknown' | null;
const endpoint = '/api/artifacts/jobs';
const effects = ['LOCAL_HTML_BUILD', 'LOCAL_DRAFT_SAVE', 'LOCAL_SYNTHETIC_REVIEW'] as const;
const url = (values: Record<string, string>) => `${endpoint}?${new URLSearchParams(values)}`;
async function data<T>(response: Response): Promise<T> {
  const payload = await response.json() as { success?: boolean; data?: T; error?: string };
  if (!response.ok || !payload.success || !payload.data) throw new Error(payload.error ?? `HTTP ${response.status}`);
  return payload.data;
}
function VersionStateObserver({ value, update }: { value: VersionState; update: (value: VersionState) => void }) {
  useEffect(() => update(value), [value, update]);
  return null;
}
const sameOwner = (a: HtmlJob['owner'], b: HtmlJob['owner']) => a.userId === b.userId && a.orgId === b.orgId && a.teamId === b.teamId;
const joined = (job: HtmlJob, saved: DraftSnapshot, link: HtmlJobVersion) =>
  job.jobId === link.jobId && job.sourceRecordId === saved.sourceRecordId && saved.sourceRecordId === link.sourceRecordId
  && saved.versionId === link.versionId && job.requestSha256 === saved.requestSha256
  && link.requestSha256 === saved.requestSha256 && link.htmlSha256 === saved.htmlSha256;

export function HtmlJobControls({ sourceRecordId, initialRequest }: Props) {
  const { data: session, status } = useSession();
  const user = session?.user as { userId?: string; orgId?: string; teamId?: string; realUserId?: string; realRole?: string; impersonation?: unknown } | undefined;
  const owner = { userId: user?.userId ?? '', orgId: user?.orgId ?? '', teamId: user?.teamId ?? '' };
  const expires = session?.expires ? Date.parse(session.expires) : NaN;
  const [now, setNow] = useState(() => Date.now());
  const active = status === 'authenticated' && [owner.userId, owner.orgId, owner.teamId].every(x => /^[A-Za-z0-9_-]{1,150}$/.test(x))
    && !user?.realUserId && !user?.realRole && !user?.impersonation && Number.isFinite(expires) && expires > now;
  const scope = JSON.stringify([sourceRecordId, owner, session?.expires, active]);
  const scopeRef = useRef(scope); scopeRef.current = scope;
  const [stateScope, setStateScope] = useState(scope);
  const epoch = useRef(0);
  const busy = useRef(false);
  const [capability, setCapability] = useState<'loading' | 'enabled' | 'disabled'>('loading');
  const enabled = capability === 'enabled';
  const [goal, setGoal] = useState('');
  const [criteria, setCriteria] = useState<JobCriterion[]>([{ criterionId: 'c1', text: '' }]);
  const [notes, setNotes] = useState<Record<string, string>>({});
  const [confirmed, setConfirmed] = useState(false);
  const [job, setJob] = useState<HtmlJob | null>(null);
  const [jobSignature, setJobSignature] = useState('');
  const [snapshot, setSnapshot] = useState<DraftSnapshot | null>(null);
  const [link, setLink] = useState<HtmlJobVersion | null>(null);
  const [decision, setDecision] = useState<HtmlJobDecision | null>(null);
  const [versionState, setVersionState] = useState<VersionState>(null);
  const [reopened, setReopened] = useState(false);
  const [linkAbsent, setLinkAbsent] = useState(false);
  const [pending, setPending] = useState<PendingJobJournal | null>(null);
  const [notice, setNotice] = useState('');
  const signature = JSON.stringify([goal, criteria]);
  const still = (token: number, key: string) => epoch.current === token && scopeRef.current === key && active && Date.now() < expires;

  useEffect(() => {
    epoch.current += 1; busy.current = false;
    setStateScope(scope); setGoal(''); setCriteria([{ criterionId: 'c1', text: '' }]);
    setNotes({}); setConfirmed(false); setJobSignature('');
    setCapability('loading'); setJob(null); setSnapshot(null); setLink(null); setDecision(null);
    setPending(null); setNotice(''); setVersionState(null); setReopened(false); setLinkAbsent(false);
    const token = epoch.current; const key = scope;
    if (!active || !sourceRecordId.startsWith('ncr-synthetic-')) { setCapability('disabled'); return; }
    setPending(readPendingJobJournal({ owner, sourceRecordId }));
    void fetch(url({ kind: 'capabilities' }), { cache: 'no-store' }).then(data<{ jobDecisions: true }>)
      .then(value => { if (still(token, key)) setCapability(value.jobDecisions === true ? 'enabled' : 'disabled'); })
      .catch(() => { if (still(token, key)) setCapability('disabled'); });
    return () => { epoch.current += 1; };
  }, [scope]);
  useEffect(() => {
    if (!Number.isFinite(expires) || expires <= Date.now()) return;
    const timer = window.setTimeout(() => setNow(Date.now()), Math.min(expires - Date.now(), 2 ** 31 - 1));
    return () => window.clearTimeout(timer);
  }, [expires, now]);

  const prepareJob = useCallback(async (request: ArtifactExportRequest) => {
    if (!active || Date.now() >= expires || busy.current || !enabled || goal.length < 1 || goal.length > 2000
      || criteria.some(c => !c.text.trim())) throw new Error('Complete the goal and criteria first.');
    const token = epoch.current; const key = scope;
    const jobId = crypto.randomUUID();
    const journal: PendingJobJournal = { schema: 'cvf.htmlJobPending.v1', owner, sourceRecordId, jobId, operation: 'CREATE_JOB' };
    if (!writePendingJobJournal(journal)) throw new Error('Resolve the pending operation before another write.');
    busy.current = true; setPending(journal);
    try {
      const created = await data<HtmlJob>(await fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action: 'CREATE_JOB', jobId, sourceRecordId, goal, criteria, expectedOutput: 'HTML', allowedEffects: effects, request }) }));
      if (!still(token, key)) throw new Error('Owner or session changed.');
      if (created.jobId !== jobId || created.sourceRecordId !== sourceRecordId || !sameOwner(created.owner, owner)) throw new Error('Job readback mismatch.');
      clearPendingJobJournal(journal); setPending(null); setJob(created); setJobSignature(JSON.stringify([created.goal, created.criteria]));
      setSnapshot(null); setLink(null); setDecision(null); setNotes({}); setConfirmed(false); setReopened(false); setLinkAbsent(false);
      return { jobId, sourceRecordId };
    } catch (error) { if (still(token, key)) setNotice('Job outcome unknown. Reconcile this exact ID before another Build.'); throw error; }
    finally { if (still(token, key)) busy.current = false; }
  }, [active, expires, enabled, goal, criteria, owner.userId, owner.orgId, owner.teamId, sourceRecordId, scope]);

  const loadJob = async (jobId: string) => data<HtmlJob>(await fetch(url({ kind: 'job', jobId, sourceRecordId }), { cache: 'no-store' }));
  const loadSnapshot = async (versionId: string) => data<DraftSnapshot>(await fetch(`/api/artifacts/drafts?${new URLSearchParams({ sourceRecordId, id: versionId })}`, { cache: 'no-store' }));
  const loadLink = async (jobId: string, versionId: string) => fetch(url({ kind: 'version', jobId, sourceRecordId, versionId }), { cache: 'no-store' });

  const reconcile = async () => {
    if (!active || Date.now() >= expires || !pending) return;
    const token = epoch.current; const key = scope; const target = pending;
    try {
      const foundJob = await loadJob(target.jobId);
      if (!still(token, key) || foundJob.jobId !== target.jobId || foundJob.sourceRecordId !== sourceRecordId || !sameOwner(foundJob.owner, owner)) return;
      if (target.operation === 'CREATE_JOB') {
        setGoal(foundJob.goal); setCriteria(foundJob.criteria); setJob(foundJob);
        setNotes({}); setConfirmed(false);
        setJobSignature(JSON.stringify([foundJob.goal, foundJob.criteria])); setReopened(true);
        clearPendingJobJournal(target); setPending(null); setNotice('Original job recovered. No Build was started.'); return;
      }
      const versionId = target.versionId!;
      const foundSnapshot = await loadSnapshot(versionId);
      if (!still(token, key) || foundSnapshot.versionId !== versionId || foundSnapshot.sourceRecordId !== sourceRecordId
        || foundSnapshot.requestSha256 !== foundJob.requestSha256 || foundSnapshot.state !== 'CLIENT_SUBMITTED_UNVERIFIED'
        || foundSnapshot.acceptance !== 'DRAFT_UNACCEPTED') return;
      const linkResponse = await loadLink(target.jobId, versionId);
      if (!still(token, key)) return;
      let foundLink: HtmlJobVersion | null = null;
      if (linkResponse.ok) foundLink = await data<HtmlJobVersion>(linkResponse);
      else if (linkResponse.status !== 404) throw new Error('LINK_UNCONFIRMED');
      if (!still(token, key) || (foundLink && !joined(foundJob, foundSnapshot, foundLink))) return;
      if (target.operation === 'ACCEPT_VERSION') {
        if (!foundLink || !target.decisionId) throw new Error('JOIN_UNCONFIRMED');
        const foundDecision = await data<HtmlJobDecision>(await fetch(url({ kind: 'decision', jobId: target.jobId,
          sourceRecordId, versionId, decisionId: target.decisionId }), { cache: 'no-store' }));
        if (!still(token, key) || foundDecision.decisionId !== target.decisionId || foundDecision.jobId !== foundJob.jobId
          || foundDecision.versionId !== versionId || foundDecision.requestSha256 !== foundLink.requestSha256
          || foundDecision.htmlSha256 !== foundLink.htmlSha256) return;
        setDecision(foundDecision);
      }
      setGoal(foundJob.goal); setCriteria(foundJob.criteria); setJob(foundJob); setJobSignature(JSON.stringify([foundJob.goal, foundJob.criteria]));
      setNotes({}); setConfirmed(false);
      setSnapshot(foundSnapshot); setLink(foundLink); setReopened(true); setLinkAbsent(!foundLink);
      clearPendingJobJournal(target); setPending(null);
      setNotice(foundLink ? 'Exact saved version and original job recovered by read-only lookup.'
        : 'Saved version confirmed; no link exists. Link this same pair explicitly.');
    } catch { if (still(token, key)) setNotice('Exact read-only reconciliation did not confirm this operation. Its ID remains pending.'); }
  };

  const linkSnapshot = async (saved: DraftSnapshot, targetJobId?: string) => {
    if (!active || Date.now() >= expires || !job || targetJobId !== job.jobId || saved.sourceRecordId !== sourceRecordId
      || saved.requestSha256 !== job.requestSha256 || saved.state !== 'CLIENT_SUBMITTED_UNVERIFIED'
      || saved.acceptance !== 'DRAFT_UNACCEPTED' || pending) return;
    const token = epoch.current; const key = scope;
    const journal: PendingJobJournal = { schema: 'cvf.htmlJobPending.v1', owner, sourceRecordId,
      jobId: job.jobId, versionId: saved.versionId, operation: 'LINK_VERSION' };
    if (!writePendingJobJournal(journal)) { setNotice('Resolve the pending operation before linking.'); return; }
    setPending(journal); setSnapshot(saved); setLink(null); setDecision(null); setNotes({}); setConfirmed(false); setLinkAbsent(false);
    try {
      const created = await data<HtmlJobVersion>(await fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action: 'LINK_VERSION', jobId: job.jobId, sourceRecordId, versionId: saved.versionId }) }));
      if (!still(token, key)) return;
      if (!joined(job, saved, created)) throw new Error('Link readback mismatch.');
      clearPendingJobJournal(journal); setPending(null); setLink(created); setNotice('Exact saved version linked.');
    } catch { if (still(token, key)) setNotice('Link outcome unknown. Reconcile this exact version ID.'); }
  };

  const accept = async () => {
    if (!active || Date.now() >= expires || !job || !link || !snapshot || !confirmed || pending || decision
      || jobSignature !== signature || (!reopened && versionState !== 'current') || !joined(job, snapshot, link)) return;
    const reviews = job.criteria.map(c => ({ criterionId: c.criterionId, passed: true as const, reviewNote: notes[c.criterionId] ?? '' }));
    if (reviews.some(r => !r.reviewNote.trim() || r.reviewNote.length > 1000)) { setNotice('Add an inspectable note for every criterion.'); return; }
    const token = epoch.current; const key = scope; const decisionId = crypto.randomUUID();
    const journal: PendingJobJournal = { schema: 'cvf.htmlJobPending.v1', owner, sourceRecordId, jobId: job.jobId,
      versionId: link.versionId, decisionId, operation: 'ACCEPT_VERSION' };
    if (!writePendingJobJournal(journal)) { setNotice('Resolve the pending operation first.'); return; }
    setPending(journal);
    try {
      const created = await data<HtmlJobDecision>(await fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action: 'ACCEPT_VERSION', decisionId, jobId: job.jobId, sourceRecordId, versionId: link.versionId,
          requestSha256: link.requestSha256, htmlSha256: link.htmlSha256, criteriaReview: reviews, reviewedVersionConfirmed: true }) }));
      if (!still(token, key)) return;
      if (created.decisionId !== decisionId || created.jobId !== job.jobId || created.versionId !== link.versionId
        || created.requestSha256 !== link.requestSha256 || created.htmlSha256 !== link.htmlSha256) throw new Error('Decision readback mismatch.');
      clearPendingJobJournal(journal); setPending(null); setDecision(created);
    } catch { if (still(token, key)) setNotice('Review outcome unknown. Reconcile the exact decision ID.'); }
  };

  const canReview = !!job && !!link && !!snapshot && joined(job, snapshot, link) && jobSignature === signature
    && (reopened || versionState === 'current');
  const recovery = (displayed: DisplayedResult | null, current: VersionState) => <>
    <VersionStateObserver value={current} update={setVersionState} />
    <HtmlDraftRecovery key={scope} sourceRecordId={sourceRecordId} displayed={displayed} versionState={current}
      jobMode={enabled} onConfirmedSnapshot={(saved, targetJobId) => { void linkSnapshot(saved, targetJobId); }} />
  </>;
  if (stateScope !== scope) return <p role="status">Checking local synthetic job scope...</p>;
  if (!active) return <p role="status">Normal session required for the local synthetic job.</p>;
  if (capability === 'loading') return <p role="status">Checking local synthetic job capability...</p>;
  if (!enabled) return <ArtifactExportPanel key={scope} initialRequest={initialRequest} renderRecovery={recovery} />;
  return <div data-testid="html-job-controls" className="space-y-4">
    <section className="rounded-lg border p-3" aria-label="Local synthetic HTML job">
      <p className="text-sm font-semibold">Local synthetic HTML job</p>
      <p className="text-xs">Build stays local to this selected profile. Stop is local; remote completion and cost can remain unknown.</p>
      <label className="mt-2 block text-xs">Goal<textarea aria-label="Goal" value={goal} maxLength={2000}
        onChange={e => setGoal(e.target.value)} className="mt-1 w-full rounded border p-2" /></label>
      {criteria.map((criterion, index) => <label key={criterion.criterionId} className="mt-2 block text-xs">Criterion {index + 1}
        <input aria-label={`Criterion ${index + 1}`} value={criterion.text} maxLength={500} className="ml-2 rounded border p-2"
          onChange={e => setCriteria(xs => xs.map((x, i) => i === index ? { ...x, text: e.target.value } : x))} /></label>)}
      <button type="button" disabled={criteria.length >= 8} onClick={() => setCriteria(xs => [...xs, { criterionId: `c${xs.length + 1}`, text: '' }])}>Add criterion</button>
      {job && <p data-testid="current-job-id" className="text-xs">Job {job.jobId}</p>}
    </section>
    <ArtifactExportPanel key={scope} initialRequest={initialRequest} prepareJob={prepareJob} renderRecovery={recovery} />
    {pending && <button type="button" onClick={() => void reconcile()} data-testid="reconcile-job-operation">
      Reconcile {pending.operation} {pending.jobId} {pending.versionId ?? ''} {pending.decisionId ?? ''}</button>}
    {linkAbsent && job && snapshot && !pending && <button type="button" data-testid="link-confirmed-version"
      onClick={() => void linkSnapshot(snapshot, job.jobId)}>Link this confirmed saved version to its original job</button>}
    {notice && <p role="status">{notice}</p>}
    {job && snapshot && <section className="rounded-lg border p-3" aria-label="Review saved HTML version">
      <p>Saved draft {snapshot.versionId}: client submitted, unverified, unaccepted.</p>
      <p>{reopened ? 'Reopened original job and saved version.' : 'Current displayed job and saved version.'}</p>
      {!canReview && <p data-testid="review-target-stale">Review target is stale or unconfirmed; this does not accept current work.</p>}
      {link && canReview && <>
        {job.criteria.map(c => <label key={c.criterionId} className="mt-2 block text-xs">{c.text}
          <textarea aria-label={`Review note ${c.criterionId}`} maxLength={1000} value={notes[c.criterionId] ?? ''}
            onChange={e => setNotes(xs => ({ ...xs, [c.criterionId]: e.target.value }))} className="mt-1 w-full rounded border p-2" /></label>)}
        <label className="block text-xs"><input type="checkbox" checked={confirmed} onChange={e => setConfirmed(e.target.checked)} /> I reviewed this exact saved version</label>
        <button type="button" disabled={!active || !!pending || !!decision} onClick={() => void accept()} data-testid="accept-synthetic-version">Record local synthetic review</button>
      </>}
      {decision && canReview && decision.jobId === job.jobId && decision.versionId === snapshot.versionId
        && decision.requestSha256 === snapshot.requestSha256 && decision.htmlSha256 === snapshot.htmlSha256
        && <p data-testid="synthetic-review-decision">Local synthetic person review recorded for this original version: {decision.decisionId}. Draft provenance remains unverified.</p>}
    </section>}
  </div>;
}
