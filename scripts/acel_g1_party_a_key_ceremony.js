#!/usr/bin/env node
/**
 * ACEL G1 T3A-C1 - Ed25519 key generator helper for the Party A ceremony tool.
 *
 * Boundary: this helper only generates one ephemeral in-memory Ed25519 key pair
 * and emits it as a single JSON object on stdout for the calling wrapper to
 * capture. It has no standalone logging path, writes no file, reads no existing
 * key, performs no ceremony decision, and must never be invoked as a durable
 * key-production step on its own. The caller owns identity checks, protection,
 * persistence and cleanup.
 *
 * Emitted JSON (single line, stdout, captured by the caller):
 *   {
 *     "helperContract": "cvf.acel.g1.keyCeremonyHelper@1",
 *     "algorithm": "Ed25519",
 *     "privateKeyPkcs8DerBase64": "<PKCS8 DER, 48 bytes, base64>",
 *     "publicKeyRawBase64Url": "<raw 32-byte public key, base64url>",
 *     "publicKeySha256Hex": "<SHA-256 of the raw 32 public bytes, hex>",
 *     "selfTestSignatureVerified": true
 *   }
 *
 * The private field is secret. The caller must protect it immediately and must
 * never echo, log, or persist it in plaintext.
 */

'use strict';

const crypto = require('crypto');

const HELPER_CONTRACT = 'cvf.acel.g1.keyCeremonyHelper@1';
// Node's key-generation type name is lowercase; the JWK curve name and the
// governed registry algorithm label are capitalized. They are deliberately
// separate constants so neither vocabulary is used in the other's position.
const NODE_KEY_TYPE = 'ed25519';
const JWK_CURVE = 'Ed25519';
const ALGORITHM = 'Ed25519';
const PKCS8_DER_LENGTH = 48;
const RAW_PUBLIC_KEY_LENGTH = 32;
const SIGNATURE_LENGTH = 64;

/**
 * Generate one Ed25519 key pair and prove it signs and verifies before return.
 * Throws on any shape or self-test deviation so the caller fails closed rather
 * than persisting an unproven key.
 */
function generateVerifiedKeyMaterial() {
  const { publicKey, privateKey } = crypto.generateKeyPairSync(NODE_KEY_TYPE);

  const privateKeyPkcs8Der = privateKey.export({ type: 'pkcs8', format: 'der' });
  if (privateKeyPkcs8Der.length !== PKCS8_DER_LENGTH) {
    throw new Error(
      `unexpected PKCS8 DER length ${privateKeyPkcs8Der.length}, expected ${PKCS8_DER_LENGTH}`
    );
  }

  const publicKeySpkiDer = publicKey.export({ type: 'spki', format: 'der' });
  const publicKeyRaw = publicKeySpkiDer.subarray(publicKeySpkiDer.length - RAW_PUBLIC_KEY_LENGTH);
  if (publicKeyRaw.length !== RAW_PUBLIC_KEY_LENGTH) {
    throw new Error(
      `unexpected raw public key length ${publicKeyRaw.length}, expected ${RAW_PUBLIC_KEY_LENGTH}`
    );
  }

  // Independent cross-check: the raw bytes taken from the SPKI tail must equal
  // the JWK public coordinate, so a future SPKI prefix change cannot silently
  // publish wrong public-key bytes.
  const jwk = publicKey.export({ format: 'jwk' });
  if (jwk.crv !== JWK_CURVE) {
    throw new Error(`unexpected JWK curve ${jwk.crv}, expected ${JWK_CURVE}`);
  }
  const jwkPublicRaw = Buffer.from(jwk.x, 'base64url');
  if (Buffer.compare(publicKeyRaw, jwkPublicRaw) !== 0) {
    throw new Error('raw public key mismatch between SPKI tail and JWK coordinate');
  }

  // Round-trip the private material the caller will actually persist, so the
  // protected blob is proven usable before it is written anywhere.
  const reimportedPrivateKey = crypto.createPrivateKey({
    key: privateKeyPkcs8Der,
    format: 'der',
    type: 'pkcs8',
  });
  const reimportedPublicSpkiDer = crypto
    .createPublicKey(reimportedPrivateKey)
    .export({ type: 'spki', format: 'der' });
  if (Buffer.compare(publicKeySpkiDer, reimportedPublicSpkiDer) !== 0) {
    throw new Error('re-imported private key does not derive the same public key');
  }

  const challenge = crypto.randomBytes(32);
  const signature = crypto.sign(null, challenge, reimportedPrivateKey);
  if (signature.length !== SIGNATURE_LENGTH) {
    throw new Error(
      `unexpected signature length ${signature.length}, expected ${SIGNATURE_LENGTH}`
    );
  }
  const selfTestSignatureVerified = crypto.verify(null, challenge, publicKey, signature);
  if (selfTestSignatureVerified !== true) {
    throw new Error('generated key failed its own sign/verify self-test');
  }

  const publicKeySha256Hex = crypto.createHash('sha256').update(publicKeyRaw).digest('hex');

  return {
    helperContract: HELPER_CONTRACT,
    algorithm: ALGORITHM,
    privateKeyPkcs8DerBase64: privateKeyPkcs8Der.toString('base64'),
    publicKeyRawBase64Url: publicKeyRaw.toString('base64url'),
    publicKeySha256Hex,
    selfTestSignatureVerified,
  };
}

function main() {
  // Refuse extra arguments: this helper has exactly one behavior and must not
  // grow an alternate mode that could write or disclose key material.
  const extraArgs = process.argv.slice(2);
  if (extraArgs.length > 0) {
    process.stderr.write(
      `${HELPER_CONTRACT}: no arguments are accepted; received ${extraArgs.length}\n`
    );
    process.exit(2);
  }

  let payload;
  try {
    payload = generateVerifiedKeyMaterial();
  } catch (error) {
    // Error text only; never the generated material.
    process.stderr.write(`${HELPER_CONTRACT}: generation failed: ${error.message}\n`);
    process.exit(1);
  }

  // Single captured stdout emission. The caller consumes this; the helper keeps
  // no copy and emits nothing else.
  process.stdout.write(`${JSON.stringify(payload)}\n`);
}

main();
