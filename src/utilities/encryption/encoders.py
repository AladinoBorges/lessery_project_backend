# https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/#scrypt
import os

from cryptography.exceptions import (
    AlreadyFinalized,
    InvalidKey,
    UnsupportedAlgorithm,
)
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

Exceptions = (
    AlreadyFinalized
    | UnsupportedAlgorithm
    | InvalidKey
    | TypeError
    | ValueError
)

PASSWORD_SALT: str = os.environ.get("BACKEND_PUBLIC_PASSWORD_ENCRYPTION_SALT")


def serialize_string_to_bytes(value: str, encoding="utf-16") -> bytes:
    result = bytes(value, encoding)

    return result


def key_derivation_function(
    salt: bytes,
    length: int = 64,
    cost: int = 2**18,
    block_size: int = 8,
    parallelization: int = 1,
) -> Scrypt | Exceptions:
    return Scrypt(
        salt=salt, length=length, n=cost, r=block_size, p=parallelization
    )


def generate_hashed_password(
    password: str, password_salt: str = PASSWORD_SALT
) -> bytes | Exception:
    hashed_password: bytes = key_derivation_function(
        serialize_string_to_bytes(password_salt)
    ).derive(serialize_string_to_bytes(password, "utf-8"))

    return hashed_password


def verify_hashed_password(
    password: str,
    encrypted_password: bytes,
    password_salt: str = PASSWORD_SALT,
) -> bool | Exception:
    try:
        key_derivation_function(
            serialize_string_to_bytes(password_salt)
        ).verify(
            key_material=serialize_string_to_bytes(password, "utf-8"),
            expected_key=encrypted_password,
        )

        return True
    except (InvalidKey, AlreadyFinalized) as Error:
        raise Error
