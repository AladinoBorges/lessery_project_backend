from pydantic import BaseModel as BaseSchema
from sqlalchemy import BigInteger


class ProductBaseSchema(BaseSchema):
    code: str
    name: str
    description: str
    price: float
    shop_name: str
    affiliate_url: str


class ProductCreateSchema(ProductBaseSchema):
    pass


class ProductReadSchema(ProductBaseSchema):
    id: BigInteger
    owner_id: BigInteger
    price_history: list[float]

    class Config:
        orm_mode: bool = True
