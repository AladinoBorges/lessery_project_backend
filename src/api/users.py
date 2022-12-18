from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.connections.engine import LocalSession
from src.middlewares.users import UsersMiddleware
from src.schemas.UserBase import (
    UserCreateSchema,
    UserReadSchema,
    UsersReadSchema,
)
from src.utils.configurations.logging import database_connection_logger


def connect() -> None:
    """get_database starts and finishes a session per request. no session
    will be used on more than one request."""
    database: Session = LocalSession()

    database_connection_logger()

    try:
        yield database
    except Exception:
        database.rollback()
    finally:
        database.close()


users_router = APIRouter(tags=["users"], prefix="/api/v1/users")


@users_router.post("/", response_model=UserReadSchema | dict[str, int | str])
def create(
    user_data: UserCreateSchema, database: Session = Depends(connect)
) -> UserReadSchema | HTTPException:
    new_user = UsersMiddleware.create(user_data, database)

    return new_user


@users_router.get("/", response_model=UsersReadSchema | dict[str, int | str])
def find_all(
    skip: int = 0, limit: int = 13, database: Session = Depends(connect)
) -> UserReadSchema | HTTPException:
    users = UsersMiddleware.find_all(skip, limit, database)

    return users


@users_router.get(
    "/{user_id}", response_model=UserReadSchema | dict[str, int | str]
)
def find_by_id(
    user_id: int, database: Session = Depends(connect)
) -> UserReadSchema | HTTPException:

    user = UsersMiddleware.find_by_id(user_id, database)

    return user
