from pydantic import BaseModel as BaseSchema


class UserBaseSchema(BaseSchema):
    name: str
    last_name: str
    email: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserReadSchema(UserBaseSchema):
    id: int
    is_active: bool

    class Config:
        orm_mode: bool = True


class UsersReadSchema(BaseSchema):
    users: list[UserReadSchema]
