from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.connections.Database import Database
from src.models.users import UsersModel
from src.schemas.UserBase import (
    UserCreateSchema,
    UserReadSchema,
    UserUpdateSchema,
)
from src.services.users import UsersService
from src.utilities.encryption.encoders import generate_hashed_password
from src.utilities.errors.handlers import Exceptions
from src.utilities.responses.handlers import Default


class UsersRouter:
    connection: Session = Database.connect
    router = APIRouter(tags=["users"], prefix="/v1")
    response_type = (
        list[UserReadSchema] | UserReadSchema | dict[str, bool | int | str]
    )

    @router.post("/user", response_model=response_type)
    def create(
        user_data: UserCreateSchema,
        database: Session = Depends(connection),
    ) -> UserCreateSchema | HTTPException:
        user_exists = UsersModel.find_by_email(user_data.email, database)

        if user_exists:
            message = (
                "user already registered. please, "
                + "use another email or try to login instead."
            )

            return Exceptions.http(message, 400)

        user_data.password = UsersService.create(user_data)

        new_user = UsersModel.create(user_data, database)

        return Default.unique(new_user, "error creating a new user.", 404)

    @router.get("/users", response_model=response_type)
    def find_all(
        skip: int = 0,
        limit: int = 13,
        database: Session = Depends(connection),
    ) -> UserReadSchema | HTTPException:
        users = UsersModel.find_all(skip, limit, database)

        return Default.multiple(users, "no users found.", 404)

    @router.get("/user", response_model=response_type)
    def find_by_email(
        email: str, database: Session = Depends(connection)
    ) -> UserReadSchema | HTTPException:
        valid_email = UsersService.find_by_email(email)

        user = UsersModel.find_by_email(valid_email, database)

        return Default.unique(user, "user not found.", 404)

    @router.get("/user/{id}", response_model=response_type)
    def find_by_id(
        id: int, database: Session = Depends(connection)
    ) -> UserReadSchema | HTTPException:
        valid_id = UsersService.find_by_id(id)

        user = UsersModel.find_by_id(valid_id, database)

        return Default.unique(user, "user not found.", 404)

    @router.patch("/user/{id}", response_model=response_type)
    def update(
        id: int,
        data: UserUpdateSchema,
        database: Session = Depends(connection),
    ) -> UserReadSchema | HTTPException:

        validated_data = UsersService.update(id, data)

        user = UsersModel.update(id, validated_data, database)

        return user
