from sqlalchemy.orm import Session

from src.schemas.UserBase import UserCreateSchema, UserReadSchema
from src.services.users import UsersService


class UsersController:
    def create(user: UserCreateSchema) -> UserReadSchema:
        new_user: UserReadSchema = UsersService.create(user)

        return new_user

    def find_by_id(user_id: int, database: Session) -> UserReadSchema:
        user: UserReadSchema = UsersService.find_by_id(user_id, database)

        return user

    def find_by_email(user_email: str) -> UserReadSchema:
        user: UserReadSchema = UsersService.find_by_email(user_email)

        return user

    def find_all(
        skip: int, limit: int, database: Session
    ) -> list[UserReadSchema]:
        users: UserReadSchema = UsersService.find_all(skip, limit, database)

        return users

    """
    def update_user(
      user_id: int, data: UpdateUserSchema
    ) -> UserReadSchema:
        user = UsersService.update(user_id, data)

        return user


    def delete_user(
      user_id: int, is_active: bool
    ) -> UserDeleteSchema:
        user = UsersService.delete(user_id, active_status)

        return user
    """
