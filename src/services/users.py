from sqlalchemy import BigInteger

from src.models.user import UsersModel
from src.schemas.UserBase import UserCreateSchema, UserReadSchema
from src.services.utils.default_response import response
from src.services.utils.encoders import generate_hashed_password


class UsersService:
    def create(user_data: UserCreateSchema) -> UserReadSchema:
        hashed_password = generate_hashed_password(user_data.password)
        updated_user_data = {**user_data, "password": hashed_password}

        data = UsersModel.create(updated_user_data)

        return response(data, "error creating a new user.", 404, 200)

    def find_all(skip: int, limit: int):
        data = UsersModel.find_all(skip, limit)

        return response(data, "users not found.", 404, 200)

    def find_by_id(user_id: BigInteger) -> UserReadSchema:
        data = UsersModel.find_by_id(user_id)

        return response(data, "user not found.", 404, 200)

    def find_by_email(email: str) -> UserReadSchema:
        data = UsersModel.find_by_email(email)

        return response(data, "user not found.", 404, 200)

    """
    def update(
      user_id: BigInteger, data: UpdateUserSchema
    ) -> UserReadSchema:
        data = UsersModel.update(user_id, data)

        return response(data, "user not found.", 404, 200)


    def delete(
      user_id: BigInteger, is_active: bool
    ) -> UserDeleteSchema:
        user = UsersModel.delete(user_id, active_status)

        return response(data, "user not found.", 404, 200)
    """