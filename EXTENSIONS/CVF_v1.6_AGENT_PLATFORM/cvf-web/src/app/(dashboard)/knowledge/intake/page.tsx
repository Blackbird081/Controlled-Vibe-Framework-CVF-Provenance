import { BookOpenCheck, CircleCheck, FileText, ShieldCheck } from 'lucide-react';

const REVIEW_STEPS = [
  {
    title: 'What changed?',
    body: 'Capture the new fact, policy, customer note, or product rule in plain words before it is used.',
  },
  {
    title: 'Who should trust it?',
    body: 'Name the audience and the situation where this knowledge should help, so CVF does not reuse it everywhere.',
  },
  {
    title: 'What should it become?',
    body: 'Turn raw notes into clearer choices, review packets, receipts, and handoff notes people can check.',
  },
];

const BENEFITS = [
  'A non-coder can see why a new piece of knowledge matters before it shapes an answer.',
  'The review packet keeps the original source and the visible receipt together.',
  'Future work starts with fewer hidden assumptions and clearer next steps.',
];

export default function KnowledgeIntakePage() {
  return (
    <div className="mx-auto max-w-7xl space-y-6 px-4 py-6 text-gray-900 dark:text-gray-100">
      <header className="border-b border-gray-200 pb-5 dark:border-white/[0.08]">
        <div className="mb-2 flex items-center gap-2 text-xs font-bold uppercase tracking-wide text-emerald-600 dark:text-emerald-300">
          <BookOpenCheck className="h-4 w-4" aria-hidden="true" />
          Knowledge Intake
        </div>
        <h1 className="text-3xl font-bold tracking-normal text-gray-950 dark:text-white">
          Bring new knowledge into CVF without hiding the trail
        </h1>
        <p className="mt-3 max-w-3xl text-sm leading-6 text-gray-600 dark:text-gray-300">
          This page frames how new material becomes useful to people who do not write code:
          a clear source, a visible reason to trust it, and a review packet that can be shared.
        </p>
      </header>

      <section className="grid gap-4 md:grid-cols-3">
        {REVIEW_STEPS.map(step => (
          <article
            key={step.title}
            className="rounded-lg border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-gray-900"
          >
            <div className="mb-3 flex h-9 w-9 items-center justify-center rounded-lg bg-emerald-50 text-emerald-600 dark:bg-emerald-950/40 dark:text-emerald-200">
              <CircleCheck className="h-5 w-5" aria-hidden="true" />
            </div>
            <h2 className="text-base font-semibold text-gray-950 dark:text-white">{step.title}</h2>
            <p className="mt-2 text-sm leading-6 text-gray-600 dark:text-gray-300">{step.body}</p>
          </article>
        ))}
      </section>

      <section className="grid gap-5 lg:grid-cols-[minmax(0,0.9fr)_minmax(0,1.1fr)]">
        <div className="rounded-lg border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-gray-900">
          <div className="flex items-center gap-2">
            <ShieldCheck className="h-5 w-5 text-indigo-500" aria-hidden="true" />
            <h2 className="text-lg font-semibold text-gray-950 dark:text-white">What the user gets</h2>
          </div>
          <div className="mt-4 space-y-3">
            {BENEFITS.map(item => (
              <div key={item} className="flex gap-3 text-sm leading-6 text-gray-600 dark:text-gray-300">
                <CircleCheck className="mt-1 h-4 w-4 shrink-0 text-emerald-500" aria-hidden="true" />
                <span>{item}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="rounded-lg border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-gray-900">
          <div className="flex items-center gap-2">
            <FileText className="h-5 w-5 text-indigo-500" aria-hidden="true" />
            <h2 className="text-lg font-semibold text-gray-950 dark:text-white">Ready for a review packet</h2>
          </div>
          <p className="mt-3 text-sm leading-6 text-gray-600 dark:text-gray-300">
            The next step is to send approved source text to Artifact Export. The result is an
            HTML presentation candidate for review, not a claim that CVF proved new behavior by itself.
          </p>
          <div className="mt-4 rounded-lg border border-amber-200 bg-amber-50 p-4 text-sm leading-6 text-amber-800 dark:border-amber-900/60 dark:bg-amber-950/30 dark:text-amber-100">
            Keep the source, the receipt, and the claim boundary visible so the next person can
            review the work without guessing what changed.
          </div>
        </div>
      </section>
    </div>
  );
}
