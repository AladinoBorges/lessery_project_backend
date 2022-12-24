from fastapi import HTTPException

from src.schemas.UserBase import UserCreateSchema
from src.services.utils.users.validations import Validate
from src.utilities.encryption.encoders import generate_hashed_password
from src.utilities.errors.handlers import Exceptions


class UsersService:
    def create(user: UserCreateSchema) -> bytes | HTTPException:
        try:
            Validate.name(user.name)
            Validate.email(user.email)
            Validate.password(user.password)
            Validate.lastname(user.last_name)

            hashed_password = generate_hashed_password(user.password)

            if not hashed_password:
                return Exceptions.http(
                    "Erro ao encriptar a sua password.", 400
                )

            return hashed_password

        except (HTTPException) as Error:
            return Error

    def find_by_id(user_id: int) -> int | HTTPException:
        return Validate.identifier(user_id)

    def find_by_email(email: str) -> str | HTTPException:
        return Validate.email(email)
