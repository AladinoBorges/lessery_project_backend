from sqlalchemy import BigInteger

from src.schemas.UserBase import UserCreateSchema, UserReadSchema
from src.services.users import UsersService


class UsersController:
    def create(user: UserCreateSchema) -> UserReadSchema:
        new_user: UserReadSchema = UsersService.create(user)

        return new_user

    def find_by_id(user_id: BigInteger) -> UserReadSchema:
        user: UserReadSchema = UsersService.find_by_id(user_id)

        return user

    def find_by_email(user_email: str) -> UserReadSchema:
        user: UserReadSchema = UsersService.find_by_email(user_email)

        return user

    def find_all(skip: int, limit: int) -> list[UserReadSchema]:
        users: UserReadSchema = UsersService.find_by_email(skip, limit)

        return users

    """
    def update_user(
      user_id: BigInteger, data: UpdateUserSchema
    ) -> UserReadSchema:
        user = UsersService.update(user_id, data)

        return user


    def delete_user(
      user_id: BigInteger, is_active: bool
    ) -> UserDeleteSchema:
        user = UsersService.delete(user_id, active_status)

        return user
    """
