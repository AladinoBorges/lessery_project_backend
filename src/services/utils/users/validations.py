from fastapi import HTTPException

from src.helpers.emails import email_validation
from src.utilities.errors.handlers import Exceptions


class Validate:
    def identifier(user_id: int) -> int | HTTPException:
        if not isinstance(user_id, int):
            return Exceptions.http("user id needs to be an integer.", 400)

        return user_id

    def name(user_name: str) -> str | HTTPException:
        if (
            not user_name
            or not isinstance(user_name, str)
            or len(user_name) == 0
        ):
            return Exceptions.http("please, insert a valid name.", 400)

        return user_name

    def lastname(user_lastname: str) -> str | HTTPException:
        if (
            not user_lastname
            or not isinstance(user_lastname, str)
            or len(user_lastname) == 0
        ):
            return Exceptions.http("please, insert a valid last name.", 400)

        return user_lastname

    def email(user_email: str) -> str | HTTPException:
        if not email_validation(user_email):
            return Exceptions.http("please, insert a valid email.", 400)

        return user_email

    def password(user_password: str) -> str | HTTPException:
        if not user_password or len(user_password) < 8:
            message = (
                "please, insert a valid password with"
                + " a minimum of 8 characters."
            )

            return Exceptions.http(message, 400)

        return user_password
