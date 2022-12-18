from src.schemas.UserBase import UserCreateSchema, UserReadSchema
from src.services.utils.encoders import generate_hashed_password


class UsersService:
    def create(user_data: UserCreateSchema) -> UserReadSchema:
        hashed_password = generate_hashed_password(user_data.password)
        updated_user_data = {**user_data, "password": hashed_password}

        return updated_user_data

    def find_by_id(user_id: int) -> UserReadSchema:
        if not isinstance(user_id, int):
            raise ValueError("user id needs to be an integer")

        return user_id

    def find_by_email(email: str) -> UserReadSchema:
        if not isinstance(email, str):
            raise ValueError("user id needs to be an integer")

        return email
