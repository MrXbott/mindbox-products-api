from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError
from http import HTTPStatus

from .. import crud, schemas
from ..dependencies import get_db, limiter


router = APIRouter(
    prefix='/products',
    tags=['product'],
    responses={500: {'error': '500'}}
)

@router.get('/', response_model=list[schemas.ProductSchema])
@limiter.limit('10/minute')
async def get_products(request: Request, offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    '''
    Returns a list of all products with its details
    '''
    try:
        products = crud.get_products(db=db, offset=offset, limit=limit)
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail='db problems')
    else:
        return products    
        

@router.get('/{id}', response_model=schemas.ProductSchema)
@limiter.limit('10/minute')
async def get_product_by_id(request: Request, id: int, db: Session = Depends(get_db)):
    '''
    Returns a product with its details by the given product id
    '''
    try:
        product = crud.get_product_by_id(db=db, product_id=id)
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail='db problems')
    else:
        if not product:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='product id not found')
        return product