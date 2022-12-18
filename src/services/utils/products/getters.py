from src.routers.external.amazon import AmazonAPI
from src.routers.external.shopee import ShopeeAPI
from src.schemas.ProductBase import ProductBaseSchema

"""
    write an util that receives as parameter a product url (ex: amazon) and
    parses the unique id (removes all information from the url and leaves only
    the unique id).

    then, write another util that connects with amazon API and retrieves all
    necessary information for product creation on LESSERY database.
"""


EXTERNAL_APIS: dict[str, callable] = {"amazon": AmazonAPI, "shopee": ShopeeAPI}


class GettersUtils:
    def extract_unique_id_from_url(url: str) -> str | None:
        return None

    def get_product_info_from_external_api(
        this, url: str, api_name: str
    ) -> ProductBaseSchema | None:
        product_id: str = this.extract_unique_id_from_url(url)

        EXTERNAL_APIS[api_name].get_product()

        return product_id
