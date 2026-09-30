# CVF NCR HTML B2b Synthetic Byte Boundary

Memory class: POINTER_RECORD

Status: SYNTHETIC_BOUNDARY_IMPLEMENTED_UNCONNECTED

docType: reference

Date: 2026-09-30

## Purpose

Name who owns the artifact bytes of a rendered HTML review packet at the first point where a decoded string becomes bytes, state the copy rules that keep those bytes trustworthy, and say clearly which byte boundaries are still unproven. The implemented part is an in-memory synthetic helper. Nothing here selects a store, an accepting actor or an acceptance effect.

## Scope / Applies To

Applies to the isolated helper `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts`, which reuses the B2a identity shape from `src/lib/html-artifact-acceptance-candidate.ts`. No route, page, component, store, file or network path imports or calls it. The B2a contract at `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md` holds a proposal for a future store; this document neither ratifies nor restates that proposal, and it stays an open operator decision there.

## Byte Values That Must Not Be Confused

| Value | What it is | Is it artifact identity |
|---|---|---|
| JSON envelope bytes | The transport bytes of the route response body. The HTML is one JSON string inside them, so quotes, backslashes, control characters and escapes change the bytes. | No. Tests show the envelope is longer and hashes differently. |
| Decoded HTML string | The string a consumer holds after JSON parsing. A JSON escape may decode to a lone surrogate, which has no UTF-8 form. | Not yet. It is the input of the byte owner. |
| Owned artifact bytes | The UTF-8 bytes produced from the decoded string exactly once, held privately by the handoff. | Yes. Identity is SHA-256 of these bytes plus their length, using the B2a algorithm label. |
| Carried candidate | An optional B2a candidate for the same bytes, always `DRAFT_UNACCEPTED`, with `sourceHash`, attempt and receipt kept as separate supporting fields. | No. It refers to the identity and adds no acceptance. |
| Blob bytes | The bytes of a `Blob` built from the string with type `text/html;charset=utf-8`. | Only when compared as bytes. Reading a Blob back as text is not a check. |
| Rendered DOM | What preview or print shows. | No. It is presentation, not byte custody. |
| Clipboard text | A text string passed to a paste target. | No. It is not a store. |
| `sourceHash` | The route hash of source text only. | No. |

## First Byte Owner And Custody Rules

The first byte owner is the B2b handoff created from the decoded string. Rules that the synthetic tests exercise:

1. Encode once. The string is encoded to UTF-8 at creation, with no trimming, newline conversion, BOM insertion or removal, or Unicode normalization. Empty, non-string and malformed-Unicode input is rejected, never repaired with a replacement character.
2. The owned bytes are never exposed by reference. Every read returns a fresh copy, and no property of the handoff holds the array.
3. Bytes handed in are copied before use. Later change to the caller's array, or to the larger buffer behind a view, cannot change the handoff. Only the view's own region is taken.
4. Adopted bytes must be well-formed UTF-8. A leading BOM is data and is kept.
5. Verification takes bytes as input and hashes those bytes. A string, another array type or bytes with different content are refused. It does not re-encode a string and does not trust a stored hash of something else.
6. Length is compared before hash, and a same-length change must fail on the hash.
7. The byte-array type check does not rely on `instanceof`, because bytes produced by Node internals can belong to another realm under a DOM test environment.
8. Identity is computed on the owned bytes by an independent path and then compared with the B2a identity computed from the string; a disagreement stops creation.

## Observations Made By The Synthetic Tests

- JSON stringify and parse of a synthetic packet returns the same decoded string, and its owned bytes match a hand-written UTF-8 encoder.
- Bytes from an in-memory Blob match the owned bytes for ASCII, non-ASCII, supplementary characters, CRLF, a leading BOM and a decomposed accent. The global Blob of the DOM test environment, read through a file reader, also matches.
- Text readback of a Node Blob drops a leading BOM although the bytes keep it. A text-only roundtrip therefore cannot show BOM fidelity, which is why byte comparison is required.
- Composed and decomposed forms of one accent, CRLF and LF, a BOM, and a title change that keeps the byte length each produce a different identity.

## Not Proven

These boundaries are outside what synthetic in-memory tests show, and no claim is made about them:

- The real route response bytes on the network, and what the deployed server or a proxy does to them.
- A real browser: how `response.json`, the download Blob, the saved file, print and preview behave, including the file actually written to disk and read back.
- What a clipboard destination stores after paste.
- Any store, durability, backup or recovery behavior.
- Wiring: no caller binds this handoff to the route output, the panel's displayed result or a writer. The panel still holds a string, and download makes a Blob from it.

## Next Unproven Boundary

The next boundary to prove is browser and file: build the download Blob from the handed-off bytes rather than from the string, read back the bytes of a really saved file in a real browser, and compare them to the identity. That needs its own work order, real-browser evidence and a decision about wiring; this tranche does not open it.

## Open Operator Decisions

Unchanged from B2a and not answered here: the real accepting actor and account, real data source and classification, store location and writer model, backup and key custody, retention, RPO and RTO, cost, pilot or live effect, and whether Profile B or C applies.

## Claim Boundary

This document describes an isolated, synthetic, in-memory byte handoff. It is not artifact acceptance, a durable store, an operator decision, network, saved-file, clipboard or real-browser proof, or authorization for real data, provider or live use, public sync or deployment. Q001 and Q004 remain open.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
