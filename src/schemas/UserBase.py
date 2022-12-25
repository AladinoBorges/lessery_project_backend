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


class UserUpdateSchema(BaseSchema):
    name: str = None
    last_name: str = None
    email: str = None
    password: str | bytes = None
    is_active: bool = None
    verified: bool = None
