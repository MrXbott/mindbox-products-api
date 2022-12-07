from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from http import HTTPStatus

from .. import crud, schemas
from ..dependencies import get_db, limiter


router = APIRouter(
    prefix="/categories",
    tags=["category"],
)

@router.get('/', response_model=list[schemas.CategorySchema])
@limiter.limit('10/minute')
async def get_categories(request: Request, offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    '''
    Returns a list of all categories with their products
    '''
    try:
        categories = crud.get_categories(db=db, offset=offset, limit=limit)
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail='db problems')
    else:
        return categories

@router.get('/{id}', response_model=schemas.CategorySchema)
@limiter.limit('10/minute')
async def get_category_by_id(request: Request, id: int, db: Session = Depends(get_db)):
    '''
    Returns a category with its products by the given category id
    '''
    try:
        category = crud.get_category_by_id(db=db, category_id=id)
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail='db problems')
    else:
        if not category:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
        return category
