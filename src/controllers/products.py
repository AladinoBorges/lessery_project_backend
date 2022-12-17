from sqlalchemy import BigInteger

from src.schemas.ProductBase import ProductReadSchema
from src.services.products import ProductsService


class ProductsController:
    def create(
        external_url: str, api_name: str, user_id: BigInteger
    ) -> ProductReadSchema:
        new_product: ProductReadSchema = ProductsService.create(
            external_url, api_name, user_id
        )

        return new_product

    def find_all(skip: int, limit: int) -> list[ProductReadSchema]:
        products: list[ProductReadSchema] = ProductsService.find_all(
            skip, limit
        )

        return products

    def find_by_id(product_id: BigInteger) -> ProductReadSchema:
        product: ProductReadSchema = ProductsService.find_by_id(product_id)

        return product

    def find_by_code(product_code: str) -> ProductReadSchema:
        product: ProductReadSchema = ProductsService.find_by_code(product_code)

        return product

    def find_by_name(product_name: str) -> list[ProductReadSchema]:
        products: list[ProductReadSchema] = ProductsService.find_by_name(
            product_name
        )

        return products

    def find_by_category(product_category: str) -> list[ProductReadSchema]:
        products: list[ProductReadSchema] = ProductsService.find_by_category(
            product_category
        )

        return products

    def find_by_owner_id(owner_id: BigInteger) -> list[ProductReadSchema]:
        products: list[ProductReadSchema] = ProductsService.find_by_owner_id(
            owner_id
        )

        return products
