import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

# Fixed version of crypto.py
# Change 1: Set minimum password length to 12, this is a security best practice to prevent weak passwords. We changed it so it would not allow empty or short passwords that attackers could guess with relative ease.
# Change 2: Raised the scrypt cost from 2**14 to 2**17, this is a security best practice to make it more difficult for attackers to brute force the password. We raised it so it would take longer for attackers to guess the password.

MIN_PASSWORD_LEN = 12  # minimum password length


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = Scrypt(
        salt=salt,
        length=32, 
        n=2**17,         # raised from 2**14
        r=8,
        p=1,
    )
    return kdf.derive(password.encode("utf-8"))


def encrypt_file(input_path: str, output_path: str, password: str) -> None:
    """Encrypt a file using AES-256-GCM with a password."""
    if len(password) < MIN_PASSWORD_LEN:
        raise ValueError(f"Password must be at least {MIN_PASSWORD_LEN} characters.")

    salt = os.urandom(16)
    nonce = os.urandom(12)
    key = derive_key(password, salt)

    with open(input_path, "rb") as f:
        plaintext = f.read()

    ciphertext = AESGCM(key).encrypt(nonce, plaintext, None)

    with open(output_path, "wb") as f:
        f.write(salt)
        f.write(nonce)
        f.write(ciphertext)

#for round -trip
def decrypt_file(input_path: str, output_path: str, password: str) -> None:
    with open(input_path, "rb") as f:
        data = f.read()

    salt, nonce, ciphertext = data[:16], data[16:28], data[28:]
    key = derive_key(password, salt)
    plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)

    with open(output_path, "wb") as f:
        f.write(plaintext)


if __name__ == "__main__":
    encrypt_file("message.txt", "message.enc", "correcthorsebattery")
    decrypt_file("message.enc", "roundtrip.txt", "correcthorsebattery")
    print("Round-trip complete")