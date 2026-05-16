import { ArrowRight, CheckCircle2, ClipboardCheck, ShieldCheck } from 'lucide-react';

import { validateHandoff } from '@/lib/agent-handoff-validator';

const SAMPLE_HANDOFF = validateHandoff({
  workflow: {
    id: 'web-review-demo',
    name: 'New Knowledge Review',
    status: 'completed',
  },
  fromTask: {
    id: 'source-review',
    agentId: 'architect',
    status: 'completed',
    output: [
      'The new knowledge is ready for review.',
      'Keep the source note, the receipt, and the claim boundary together.',
      'Use the HTML packet as a review aid only.',
    ].join(' '),
  },
  toAgentId: 'builder',
  toAgentRole: 'builder',
});

const DECISION_STYLE = {
  ALLOW: 'border-emerald-200 bg-emerald-50 text-emerald-800 dark:border-emerald-900/60 dark:bg-emerald-950/30 dark:text-emerald-100',
  WARN: 'border-amber-200 bg-amber-50 text-amber-800 dark:border-amber-900/60 dark:bg-amber-950/30 dark:text-amber-100',
  BLOCK: 'border-red-200 bg-red-50 text-red-800 dark:border-red-900/60 dark:bg-red-950/30 dark:text-red-100',
} as const;

const HANDOFF_BENEFITS = [
  'The next person can see what was reviewed and what still needs attention.',
  'The visible receipt makes the packet easier to trust, share, and revisit.',
  'New knowledge becomes a clear handoff note instead of hidden background context.',
];

export default function AgentHandoffPage() {
  const hasIssues = SAMPLE_HANDOFF.issues.length > 0;

  return (
    <div className="mx-auto max-w-7xl space-y-6 px-4 py-6 text-gray-900 dark:text-gray-100">
      <header className="border-b border-gray-200 pb-5 dark:border-white/[0.08]">
        <div className="mb-2 flex items-center gap-2 text-xs font-bold uppercase tracking-wide text-indigo-600 dark:text-indigo-300">
          <ClipboardCheck className="h-4 w-4" aria-hidden="true" />
          Agent Handoff
        </div>
        <h1 className="text-3xl font-bold tracking-normal text-gray-950 dark:text-white">
          Pass reviewed work forward with less guesswork
        </h1>
        <p className="mt-3 max-w-3xl text-sm leading-6 text-gray-600 dark:text-gray-300">
          When CVF absorbs new knowledge, the useful outcome is not a hidden system change.
          The useful outcome is a packet another person or assistant can review, continue,
          and challenge without losing the source trail.
        </p>
      </header>

      <section className="grid gap-5 lg:grid-cols-[minmax(0,0.95fr)_minmax(0,1.05fr)]">
        <div className="rounded-lg border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-gray-900">
          <div className="flex items-center gap-2">
            <ShieldCheck className="h-5 w-5 text-indigo-500" aria-hidden="true" />
            <h2 className="text-lg font-semibold text-gray-950 dark:text-white">Sample handoff check</h2>
          </div>

          <div className="mt-5 grid gap-3 sm:grid-cols-[minmax(0,1fr)_auto_minmax(0,1fr)] sm:items-center">
            <div className="rounded-lg border border-gray-200 bg-gray-50 p-4 dark:border-gray-800 dark:bg-gray-950">
              <div className="text-xs font-bold uppercase tracking-wide text-gray-500 dark:text-gray-400">Reviewed source</div>
              <div className="mt-2 text-sm font-semibold text-gray-950 dark:text-white">New knowledge review</div>
            </div>
            <ArrowRight className="hidden h-5 w-5 text-gray-400 sm:block" aria-hidden="true" />
            <div className="rounded-lg border border-gray-200 bg-gray-50 p-4 dark:border-gray-800 dark:bg-gray-950">
              <div className="text-xs font-bold uppercase tracking-wide text-gray-500 dark:text-gray-400">Next step</div>
              <div className="mt-2 text-sm font-semibold text-gray-950 dark:text-white">Continue from packet</div>
            </div>
          </div>

          <div className={`mt-4 rounded-lg border p-4 text-sm leading-6 ${DECISION_STYLE[SAMPLE_HANDOFF.decision]}`}>
            <div className="font-semibold">Decision: {SAMPLE_HANDOFF.decision}</div>
            <div className="mt-1">
              {SAMPLE_HANDOFF.contextCarried
                ? 'The reviewed context is present and can move forward.'
                : 'The reviewed context is missing and should not move forward yet.'}
            </div>
          </div>

          <div className="mt-4 rounded-lg border border-gray-200 bg-gray-50 p-4 dark:border-gray-800 dark:bg-gray-950">
            <div className="text-xs font-bold uppercase tracking-wide text-gray-500 dark:text-gray-400">Carried summary</div>
            <p className="mt-2 text-sm leading-6 text-gray-600 dark:text-gray-300">{SAMPLE_HANDOFF.outputSummary}</p>
          </div>
        </div>

        <div className="space-y-5">
          <div className="rounded-lg border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-gray-900">
            <h2 className="text-lg font-semibold text-gray-950 dark:text-white">Why this helps non-coders</h2>
            <div className="mt-4 space-y-3">
              {HANDOFF_BENEFITS.map(item => (
                <div key={item} className="flex gap-3 text-sm leading-6 text-gray-600 dark:text-gray-300">
                  <CheckCircle2 className="mt-1 h-4 w-4 shrink-0 text-emerald-500" aria-hidden="true" />
                  <span>{item}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="rounded-lg border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-gray-900">
            <h2 className="text-lg font-semibold text-gray-950 dark:text-white">Review notes</h2>
            {hasIssues ? (
              <div className="mt-4 space-y-3">
                {SAMPLE_HANDOFF.issues.map(issue => (
                  <div key={issue.code} className="rounded-lg border border-amber-200 bg-amber-50 p-3 text-sm leading-6 text-amber-800 dark:border-amber-900/60 dark:bg-amber-950/30 dark:text-amber-100">
                    {issue.friendlyMessage}
                  </div>
                ))}
              </div>
            ) : (
              <p className="mt-3 text-sm leading-6 text-gray-600 dark:text-gray-300">
                No handoff issues were found in this sample. Real handoffs should still keep the
                source, receipt, and claim boundary visible for review.
              </p>
            )}
          </div>
        </div>
      </section>
    </div>
  );
}
