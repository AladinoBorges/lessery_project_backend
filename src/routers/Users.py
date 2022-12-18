from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.connections.Database import Database
from src.middlewares.users import UsersMiddleware
from src.schemas.UserBase import (
    UserCreateSchema,
    UserReadSchema,
    UsersReadSchema,
)


class UsersRouter:
    connection: Session = Database.connect
    router = APIRouter(tags=["users"], prefix="/v1/users")

    @router.post("/", response_model=UserReadSchema | dict[str, int | str])
    def create(
        user_data: UserCreateSchema, database: Session = Depends(connection)
    ) -> UserReadSchema | HTTPException:
        new_user = UsersMiddleware.create(user_data, database)

        return new_user

    @router.get("/", response_model=UsersReadSchema | dict[str, int | str])
    def find_all(
        skip: int = 0, limit: int = 13, database: Session = Depends(connection)
    ) -> UserReadSchema | HTTPException:
        users = UsersMiddleware.find_all(skip, limit, database)

        return users

    @router.get(
        "/{user_id}", response_model=UserReadSchema | dict[str, int | str]
    )
    def find_by_id(
        user_id: int, database: Session = Depends(connection)
    ) -> UserReadSchema | HTTPException:

        user = UsersMiddleware.find_by_id(user_id, database)

        return user
