from pydantic import BaseModel as BaseSchema


class UserBaseSchema(BaseSchema):
    name: str
    last_name: str
    email: str


class UserCreateHashedSchema(UserBaseSchema):
    password: bytes


class UserCreateSchema(UserBaseSchema):
    password: str


class UserReadSchema(UserBaseSchema):
    id: int
    is_active: bool
    verified: bool

    class Config:
        orm_mode: bool = True
