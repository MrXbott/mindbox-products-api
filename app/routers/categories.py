from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from http import HTTPStatus

from .. import crud, schemas
from ..dependencies import get_db, limiter


router = APIRouter(
    prefix="/categories",
    tags=["category"],
    responses={404: {"description": "Not found"}},
)

@router.get('/', response_model=list[schemas.CategorySchema])
@limiter.limit('10/minute')
async def get_categories(request: Request, offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    '''
    Returns a list of all categories with their products
    '''
    categories = crud.get_categories(db=db, offset=offset, limit=limit)
    if not categories:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return categories

@router.get('/{id}', response_model=schemas.CategorySchema)
@limiter.limit('10/minute')
async def get_category_by_id(request: Request, id: int, db: Session = Depends(get_db)):
    '''
    Returns a category with its products by the given category id
    '''
    category = crud.get_category_by_id(db=db, category_id=id)
    if not category:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return category
