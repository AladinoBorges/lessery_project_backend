from fastapi import HTTPException
from sqlalchemy import BigInteger

from src.controllers.users import UsersController
from src.schemas.UserBase import UserCreateSchema, UserReadSchema
from src.utils.errors.handlers import http_exceptions


class UsersMiddleware:
    def create(user_data: UserCreateSchema) -> UserReadSchema | HTTPException:
        error_status_code = 400
        error_message: str = "User already registered."

        user_already_registered = UsersController.find_by_email(
            user_data.email
        )

        if user_already_registered:
            http_exceptions(error_message, error_status_code)

        new_user = UsersController.create(user_data)

        return new_user

    def find_all(
        skip: int = 0, limit: int = 13
    ) -> UserReadSchema | HTTPException:
        error_status_code = 404
        error_message: str = "No users found."

        users = UsersController.find_all(skip, limit)

        if users is None or len(users) == 0:
            http_exceptions(error_message, error_status_code)

        return users

    def find_by_id(user_id: BigInteger) -> UserReadSchema | HTTPException:
        error_status_code = 404
        error_message: str = "User not found."

        user = UsersController.find_by_id(user_id)

        if user is None:
            http_exceptions(error_message, error_status_code)

        return user

    def find_by_email(user_email: str) -> UserReadSchema | HTTPException:
        error_status_code = 404
        error_message: str = "User not found."

        user = UsersController.find_by_id(user_email)

        if user is None:
            http_exceptions(error_message, error_status_code)

        return user
