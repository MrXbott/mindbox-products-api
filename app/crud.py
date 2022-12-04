from sqlalchemy.orm import Session
from . import models, schemas


def get_products(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.Product).offset(offset).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.product_id == product_id).first()

def get_categories(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.Category).offset(offset).limit(limit).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.category_id == category_id).first()

