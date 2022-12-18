from src.models.product import ProductsModel
from src.schemas.ProductBase import ProductCreateSchema, ProductReadSchema
from src.services.utils.products.getters import GettersUtils


class ProductsService:
    def create(
        external_url: str, api_name: str, user_id: int
    ) -> ProductReadSchema:
        product_data = GettersUtils.get_product_info_from_external_api(
            external_url, api_name
        )

        product: ProductCreateSchema = ProductsModel.create(
            **product_data.dict(), owner_id=user_id
        )

        return product

    def find_all() -> list[ProductReadSchema]:
        products: list[ProductReadSchema] = ProductsModel.find_all()

        return products

    def find_by_id(product_id: int) -> ProductReadSchema:
        product: ProductReadSchema = ProductsModel.find_by_id(product_id)

        return product

    def find_by_code(product_code: str) -> ProductReadSchema:
        product: ProductReadSchema = ProductsModel.find_by_code(product_code)

        return product

    def find_by_name(product_name: str) -> list[ProductReadSchema]:
        products: list[ProductReadSchema] = ProductsModel.find_by_name(
            product_name
        )

        return products

    def find_by_category(product_category: str) -> list[ProductReadSchema]:
        products: list[ProductReadSchema] = ProductsModel.find_by_category(
            product_category
        )

        return products

    def find_by_owner_id(owner_id: int) -> list[ProductReadSchema]:
        products: list[ProductReadSchema] = ProductsModel.find_by_owner_id(
            owner_id
        )

        return products
