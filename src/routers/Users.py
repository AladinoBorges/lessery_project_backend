from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.connections.Database import Database
from src.models.users import UsersModel
from src.schemas.UserBase import (
    UserCreateSchema,
    UserReadSchema,
    UsersReadSchema,
)
from src.services.users import UsersService
from src.utilities.responses.handlers import Default


class UsersRouter:
    connection: Session = Database.connect
    router = APIRouter(tags=["users"], prefix="/v1/users")
    response_type = (
        UsersReadSchema | UserReadSchema | dict[str, bool | int | str]
    )

    @router.post("/", response_model=response_type)
    def create(
        user_data: UserCreateSchema, database: Session = Depends(connection)
    ) -> UserReadSchema | HTTPException:
        data = UsersService.create(user_data)

        new_user = UsersModel.create(data, database)

        return Default.unique(new_user, "error creating a new user.", 404)

    @router.get("/", response_model=response_type)
    def find_all(
        skip: int = 0, limit: int = 13, database: Session = Depends(connection)
    ) -> UserReadSchema | HTTPException:
        users = UsersModel.find_all(skip, limit, database)

        return Default.multiple(users, "users not found.", 404)

    @router.get("/{user_id}", response_model=response_type)
    def find_by_id(
        user_id: int, database: Session = Depends(connection)
    ) -> UserReadSchema | HTTPException:
        data = UsersService.find_by_id(user_id)

        user = UsersModel.find_by_id(data, database)

        return Default.unique(user, "user not found.", 404)

    @router.get("/?{user_mail}", response_model=response_type)
    def find_by_email(
        user_mail: int, database: Session = Depends(connection)
    ) -> UserReadSchema | HTTPException:
        data = UsersService.find_by_email(user_mail)

        user = UsersModel.find_by_email(data, database)

        return Default.unique(user, "user not found.", 404)
