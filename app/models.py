from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .db import Base


products_categories = Table('products_categories', Base.metadata, 
    Column('product_id', ForeignKey('products.product_id'), primary_key=True),
    Column('category_id', ForeignKey('categories.category_id'), primary_key=True)
    )

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    brand = Column(String, index=True)
    categories = relationship('Category', secondary='products_categories', back_populates='products')


class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    products = relationship('Product', secondary='products_categories', back_populates='categories')

