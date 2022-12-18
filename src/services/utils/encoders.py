"""
    write an util that receives as parameter a unencrypted password and
    returns an encrypted (hashed) string.
"""

# TODO: UTILS START


def generate_hashed_password(
    password: str, encryption_algorithm: str = "SHA256"
) -> str | None:
    return password + "hash256"


# TODO: UTILS END
