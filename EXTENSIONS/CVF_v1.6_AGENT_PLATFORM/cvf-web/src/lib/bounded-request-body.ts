/** Application-retained request bound; not a proxy, concurrency or upload deadline. */
export async function readBoundedRequestBody(request: Request, maxBytes: number): Promise<string | null> {
    if (!Number.isSafeInteger(maxBytes) || maxBytes < 0) throw new RangeError('Invalid request byte limit');
    const declaredLength = Number(request.headers.get('content-length'));
    if (Number.isFinite(declaredLength) && declaredLength > maxBytes) return null;
    if (!request.body) return '';
    const reader = request.body.getReader();
    const decoder = new TextDecoder();
    let bytes = 0;
    let text = '';
    try {
        while (true) {
            const { done, value } = await reader.read();
            if (done) return text + decoder.decode();
            bytes += value.byteLength;
            if (bytes > maxBytes) {
                void reader.cancel().catch(() => undefined);
                return null;
            }
            text += decoder.decode(value, { stream: true });
        }
    } finally {
        reader.releaseLock();
    }
}
