from typing import Optional

from schemas import OID, CustomModel


class LamodaProduct(CustomModel):
    product_sku: str
    product_type: str
    product_title: str
    brand: str
    price: str
    attributes: list[dict]
    category_id: Optional[OID]
    url: str


class LamodaCategory(CustomModel):
    category_title: str
    product_links: list[str]
    url: str
    products: Optional[list[LamodaProduct]]
