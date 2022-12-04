from typing import List
from pydantic import BaseModel


class ProductBase(BaseModel):
    product_id: int
    product_name: str
    brand: str

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    category_id: int
    category: str

    class Config:
        orm_mode = True

class ProductSchema(ProductBase):
    categories: List[CategoryBase]

class CategorySchema(CategoryBase):
    products: List[ProductBase]