import re


def email_validation(email: str) -> bool:
    REGEX: str = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    is_valid_email: bool = re.fullmatch(REGEX, email) and isinstance(
        email, str
    )

    return is_valid_email
