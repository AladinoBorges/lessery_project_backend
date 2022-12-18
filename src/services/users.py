from fastapi import HTTPException

from src.helpers.emails import email_validation
from src.schemas.UserBase import UserBaseSchema, UserReadSchema
from src.services.utils.encoders import generate_hashed_password
from src.utilities.errors.handlers import Exceptions


class UsersService:
    def create(user: UserBaseSchema, password: str) -> str | HTTPException:
        if not email_validation(user.email):
            return Exceptions.http("please, insert a valid email.", 400)

        if not user.name or isinstance(user.name, int) or len(user.name) == 0:
            return Exceptions.http("please, insert a valid name.", 400)

        if (
            not user.last_name
            or isinstance(user.last_name, int)
            or len(user.last_name) == 0
        ):
            return Exceptions.http("please, insert a valid last name.", 400)

        if not password or len(password) < 8:
            message = (
                "please, insert a valid password with"
                + " a minimum of 8 characters."
            )

            return Exceptions.http(message, 400)

        hashed_password = generate_hashed_password(password)

        return hashed_password

    def find_by_id(user_id: int) -> UserReadSchema | HTTPException:
        if not isinstance(user_id, int):
            return Exceptions.http("user id needs to be an integer.", 400)

        return user_id

    def find_by_email(email: str) -> UserReadSchema | HTTPException:
        if not email_validation(email):
            return Exceptions.http("please, insert a valid email.", 400)

        return email
