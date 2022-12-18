from pydantic import BaseModel as BaseSchema


class ProductBaseSchema(BaseSchema):
    code: str
    name: str
    description: str
    price: float
    shop_name: str
    affiliate_url: str


class ProductCreateSchema(ProductBaseSchema):
    pass


class Product(ProductBaseSchema):
    id: int
    owner_id: int
    price_history: list[float]

    class Config:
        orm_mode: bool = True
        arbitrary_types_allowed = True


class ProductReadSchema(BaseSchema):
    success: bool
    status_code: int
    data: Product


class ProductsReadSchema(BaseSchema):
    success: bool
    status_code: int
    data: list[Product]
