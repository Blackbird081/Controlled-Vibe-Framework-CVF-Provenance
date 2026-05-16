import { ArrowRight, FileCheck2, ShieldCheck, Sparkles } from 'lucide-react';

import ArtifactExportPanel, { type ArtifactExportRequest } from '@/components/ArtifactExportPanel';

const starterRequest: ArtifactExportRequest = {
  title: 'Customer Onboarding Review Packet',
  sourcePath: 'workspace/reviews/customer-onboarding.md',
  sourceContent: [
    '# Customer Onboarding Review Packet',
    '',
    'Memory class: FULL_RECORD',
    '',
    'Status: READY_FOR_REVIEW',
    '',
    '## Summary',
    '',
    'This packet captures the current onboarding plan, the checks already made, and the open decisions that still need a human review.',
    '',
    '## Claim Boundary',
    '',
    'This is an HTML presentation candidate. It helps review and handoff. It is not a live governance proof by itself.',
  ].join('\n'),
  memoryClass: 'FULL_RECORD',
  status: 'READY_FOR_REVIEW',
  claimBoundary: 'HTML presentation candidate only. It helps review and handoff, but it is not governed artifact generation proof.',
  receiptAnchor: 'receipt-customer-onboarding-demo',
};

const valueCards = [
  {
    title: 'Bring knowledge into the review',
    body: 'Approved source text can become a clean review page without changing the meaning of the original material.',
    icon: Sparkles,
  },
  {
    title: 'Keep the receipt visible',
    body: 'The output keeps the receipt anchor and review boundary close to the work, so a non-coder can see what is safe to rely on.',
    icon: ShieldCheck,
  },
  {
    title: 'Hand off with less guessing',
    body: 'The HTML candidate is meant for review, sharing, and handoff. It does not replace human judgment or live proof.',
    icon: FileCheck2,
  },
];

export default function ArtifactsPage() {
  return (
    <div className="mx-auto max-w-7xl space-y-6 px-4 py-6">
      <header className="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm dark:border-gray-800 dark:bg-gray-900">
        <div className="flex flex-col gap-5 lg:flex-row lg:items-start lg:justify-between">
          <div className="max-w-3xl">
            <div className="mb-2 flex items-center gap-2 text-xs font-bold uppercase tracking-wide text-indigo-600 dark:text-indigo-300">
              <FileCheck2 className="h-4 w-4" aria-hidden="true" />
              Artifact Export
            </div>
            <h1 className="text-2xl font-bold text-gray-950 dark:text-white">
              Turn approved work into an HTML review packet
            </h1>
            <p className="mt-3 text-sm leading-6 text-gray-600 dark:text-gray-300">
              This page is for people who need a clean, reviewable version of AI-assisted work.
              It keeps the source, receipt anchor, status, and claim boundary visible so the
              next reviewer does not have to guess what happened.
            </p>
          </div>
          <div className="rounded-xl border border-amber-200 bg-amber-50 px-4 py-3 text-xs leading-5 text-amber-800 dark:border-amber-900/70 dark:bg-amber-950/30 dark:text-amber-200">
            HTML presentation candidate only. PDF, image export, and governed-artifact
            generation claims are out of scope for this tranche.
          </div>
        </div>
      </header>

      <section className="grid gap-4 md:grid-cols-3" aria-label="Artifact export value">
        {valueCards.map(({ title, body, icon: Icon }) => (
          <article
            key={title}
            className="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm dark:border-gray-800 dark:bg-gray-900"
          >
            <div className="mb-4 inline-flex h-9 w-9 items-center justify-center rounded-lg bg-indigo-50 text-indigo-600 dark:bg-indigo-950/40 dark:text-indigo-300">
              <Icon className="h-4 w-4" aria-hidden="true" />
            </div>
            <h2 className="text-sm font-semibold text-gray-950 dark:text-white">{title}</h2>
            <p className="mt-2 text-sm leading-6 text-gray-600 dark:text-gray-300">{body}</p>
          </article>
        ))}
      </section>

      <section className="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm dark:border-gray-800 dark:bg-gray-900">
        <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <h2 className="text-sm font-semibold text-gray-950 dark:text-white">
              What new knowledge should become
            </h2>
            <p className="mt-2 max-w-3xl text-sm leading-6 text-gray-600 dark:text-gray-300">
              When CVF absorbs useful knowledge, the web surface should turn it into clearer
              choices, review packets, receipts, and handoff notes. The user benefit is better
              review and safer reuse, not more hidden complexity.
            </p>
          </div>
          <div className="flex items-center gap-2 rounded-lg border border-gray-200 px-3 py-2 text-xs font-semibold text-gray-600 dark:border-gray-800 dark:text-gray-300">
            Source
            <ArrowRight className="h-3.5 w-3.5" aria-hidden="true" />
            Review
            <ArrowRight className="h-3.5 w-3.5" aria-hidden="true" />
            Handoff
          </div>
        </div>
      </section>

      <ArtifactExportPanel initialRequest={starterRequest} />
    </div>
  );
}
