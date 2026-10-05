// Text Encoding Exception: Vietnamese user-facing copy and matching localization fixtures.
'use client';

import { useRef, useState } from 'react';
import {
    createSpecConfirmationCandidate, MAX_CONFIRMATION_BYTES, reviewBindingKey,
    verifySpecConfirmationReadback, type SpecConfirmationCandidate,
} from '@/lib/intent-spec-confirmation';
import { getPendingReviewDecisions, isCurrentReviewAcknowledged, type IntentSpecReviewState, type ReviewLanguage } from '@/lib/intent-spec-review';

export function IntentSpecConfirmation({ review, language }: { review: IntentSpecReviewState; language: ReviewLanguage }) {
    const vi = language === 'vi';
    const [reviewer, setReviewer] = useState('');
    const [candidate, setCandidate] = useState<SpecConfirmationCandidate | null>(null);
    const [result, setResult] = useState<{ key: string; text: string } | null>(null);
    const [busy, setBusy] = useState(false);
    const [opened, setOpened] = useState(false);
    const bindingKey = reviewBindingKey(review, language, reviewer);
    const [previousKey, setPreviousKey] = useState(bindingKey);
    const liveKey = useRef(bindingKey);
    liveKey.current = bindingKey;
    const generation = useRef(0);
    if (previousKey !== bindingKey) {
        generation.current++;
        setPreviousKey(bindingKey); setCandidate(null); setResult(null); setBusy(false);
    }
    const active = candidate?.bindingKey === bindingKey ? candidate : null;
    const ready = reviewer.trim().length > 0 && reviewer.trim().length <= 120
        && isCurrentReviewAcknowledged(review) && getPendingReviewDecisions(review).length === 0;
    const control = 'min-h-11 rounded-lg border border-gray-300 px-3 py-2 text-sm focus:ring-2 focus:ring-indigo-500 disabled:opacity-50 dark:border-gray-600';

    const create = async () => {
        const key = bindingKey;
        const operation = ++generation.current;
        setCandidate(null); setResult(null); setBusy(true);
        try {
            const next = await createSpecConfirmationCandidate(review, language, reviewer);
            if (liveKey.current === key && generation.current === operation) setCandidate(next);
        } catch {
            if (liveKey.current === key && generation.current === operation) {
                setResult({ key, text: vi ? 'Chưa tạo được gói. Hãy kiểm lại bản review và thử lại.' : 'Could not create the file. Check the review and try again.' });
            }
        } finally { if (generation.current === operation) setBusy(false); }
    };

    const download = () => {
        if (!active) return;
        let url: string | null = null;
        try {
            url = URL.createObjectURL(new Blob([active.fileContent], { type: 'application/json;charset=utf-8' }));
            const link = document.createElement('a');
            link.href = url; link.download = `cvf-spec-review-r${active.revision}.json`; link.click();
            setResult({ key: bindingKey, text: vi ? 'Đã yêu cầu tải. Chọn lại file để kiểm tra nội dung đã lưu.' : 'Download requested. Select the saved file to check its content.' });
        } catch {
            setResult({ key: bindingKey, text: vi ? 'Không tải được file. Chưa có xác nhận lưu.' : 'Download failed. No saved-file confirmation.' });
        } finally { if (url) URL.revokeObjectURL(url); }
    };

    const readback = async (file: File) => {
        if (!active) return;
        const key = bindingKey;
        const operation = ++generation.current;
        setResult(null); setBusy(true);
        try {
            if (file.size > MAX_CONFIRMATION_BYTES) throw new Error('FILE_TOO_LARGE');
            const ok = await verifySpecConfirmationReadback(active, new Uint8Array(await file.arrayBuffer()));
            if (liveKey.current === key && generation.current === operation) {
                setResult({ key, text: ok
                    ? (vi ? 'File đã chọn khớp đúng gói của bản review này.' : 'Selected file matches this exact review candidate.')
                    : (vi ? 'File không khớp. Chưa xác nhận bản này.' : 'File does not match. This revision is unconfirmed.') });
            }
        } catch {
            if (liveKey.current === key && generation.current === operation) {
                setResult({ key, text: vi ? 'Không kiểm tra được file. Chưa xác nhận bản này.' : 'Could not verify the file. This revision is unconfirmed.' });
            }
        } finally { if (generation.current === operation) setBusy(false); }
    };

    if (!opened) return <button type="button" className={`${control} mt-4`} onClick={() => setOpened(true)}>
        {vi ? 'Lưu bản review để đối chiếu' : 'Keep a review copy for comparison'}
    </button>;

    return <div className="mt-4 rounded-lg border border-gray-200 p-3 dark:border-gray-700" role="group"
        aria-label={vi ? 'Lưu bản review để đối chiếu' : 'Keep a review copy for comparison'}>
        <label className="block text-sm">
            {vi ? 'Tên người review (tự khai báo)' : 'Reviewer name (self-declared)'}
            <input value={reviewer} maxLength={120} className={`${control} mt-1 w-full bg-white dark:bg-gray-900`}
                onChange={event => setReviewer(event.target.value)} />
        </label>
        <p className="my-2 text-xs text-gray-600 dark:text-gray-400">
            {vi ? 'File chứa brief và câu trả lời của bạn. Tải rồi chọn lại file để kiểm đúng nội dung. Tên này chưa được xác thực; gói không cấp quyền build và chưa được lưu trên server.' : 'The file contains your brief and answers. Download and select it again to check the exact content. This name is unverified; the file grants no build permission and is not saved on a server.'}
        </p>
        <button type="button" className={control} disabled={!ready || busy} onClick={create}>
            {vi ? 'Tạo gói cho bản đã review' : 'Create file for reviewed revision'}
        </button>
        {active && <div className="mt-2 space-y-2">
            <button type="button" className={control} disabled={busy} onClick={download}>{vi ? 'Tải gói review' : 'Download review file'}</button>
            <label className="block text-sm">{vi ? 'Chọn file đã lưu để đối chiếu' : 'Select saved file for comparison'}
                <input type="file" accept=".json,application/json" disabled={busy}
                    onChange={event => {
                        const file = event.target.files?.[0];
                        event.target.value = '';
                        if (file) void readback(file);
                    }} className="mt-1 block w-full text-sm" />
            </label>
        </div>}
        {result?.key === bindingKey && <p role="status" className="mt-2 text-sm">{result.text}</p>}
    </div>;
}
