from fastapi import APIRouter, HTTPException
from sqlalchemy import BigInteger

from src.middlewares.users import UsersMiddleware
from src.schemas.UserBase import UserCreateSchema, UserReadSchema

router = APIRouter()


@router.post("/users", response_model=UserReadSchema)
def create(
    user_data: UserCreateSchema,
) -> UserReadSchema | HTTPException:
    new_user = UsersMiddleware.create(user_data)

    return new_user


@router.get("/users", response_model=UserReadSchema)
def get_all_users(
    skip: int = 0,
    limit: int = 13,
) -> UserReadSchema | HTTPException:
    users = UsersMiddleware.find_all(skip, limit)

    return users


@router.get("/users/{user_id}", response_model=UserReadSchema)
def get_user_by_id(
    user_id: BigInteger,
) -> UserReadSchema | HTTPException:

    user = UsersMiddleware.find_by_id(user_id)

    return user
