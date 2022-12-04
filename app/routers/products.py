from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from http import HTTPStatus

from .. import crud, schemas
from ..dependencies import get_db


router = APIRouter(
    prefix="/products",
    tags=["product"],
    responses={404: {"description": "Not found"}},
)

@router.get('/', response_model=list[schemas.ProductSchema])
async def get_products(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    '''
    Returns a list of all products with its details
    '''
    products = crud.get_products(db=db, offset=offset, limit=limit)
    if not products:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return products

@router.get('/{id}', response_model=schemas.ProductSchema)
async def get_product_by_id(id: int, db: Session = Depends(get_db)):
    '''
    Returns a product with its details by the given product id
    '''
    product = crud.get_product_by_id(db=db, product_id=id)
    if not product:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return product