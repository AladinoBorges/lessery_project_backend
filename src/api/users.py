from fastapi import APIRouter, HTTPException
from sqlalchemy import BigInteger

from src.controllers.users import (
    create_user,
    get_user,
    get_user_by_email,
    get_users,
)
from src.schemas.UserBase import UserCreateSchema, UserReadSchema
from src.utils.errors.handlers import http_exceptions

router = APIRouter()


@router.post("/users", response_model=UserReadSchema)
def create_new_user(
    user_data: UserCreateSchema,
) -> UserReadSchema | HTTPException:
    error_status_code = 400
    error_message: str = "User already registered."

    user_already_registered = get_user_by_email(user_data.email)

    if user_already_registered:
        http_exceptions(error_message, error_status_code)

    new_user = create_user(user_data)

    return new_user


@router.get("/users", response_model=UserReadSchema)
def get_all_users(
    skip: int = 0,
    limit: int = 13,
) -> UserReadSchema | HTTPException:
    error_status_code = 404
    error_message: str = "No users found."

    users = get_users(skip, limit)

    if users is None:
        http_exceptions(error_message, error_status_code)

    return users


@router.get("/users/{user_id}", response_model=UserReadSchema)
def get_user_by_id(
    user_id: BigInteger,
) -> UserReadSchema | HTTPException:
    error_status_code = 404
    error_message: str = "User not found."

    user = get_user(user_id)

    if user is None:
        http_exceptions(error_message, error_status_code)

    return user
