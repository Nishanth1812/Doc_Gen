import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from app.utils.config import Settings


def encrypt_token(token: str):
    key = settings.AES_SECRET.encode()[:32]
    aes = AESGCM(key)

    nonce = os.urandom(12)

    encrypted = aes.encrypt(nonce, token.encode(), None)

    return {
        "ciphertext": encrypted.hex(),
        "nonce": nonce.hex()
    }


def decrypt_token(ciphertext: str, nonce: str):
    key = settings.AES_SECRET.encode()[:32]
    aes = AESGCM(key)

    decrypted = aes.decrypt(
        bytes.fromhex(nonce),
        bytes.fromhex(ciphertext),
        None
    )

    return decrypted.decode()