from database import db
from fastapi import APIRouter, Request, HTTPException, Depends
from typing import Optional
from models.item import Item


def authenticated(request: Request):
    user = request.state.user
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    return user


router = APIRouter(
    prefix="/items",
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(authenticated)],
)


@router.get("")
def get_items():
    res = db.child("items").get()
    return res.val()


@router.get("/{item_id}")
def get_items(item_id: Optional[int]):
    res = db.child("items").order_by_child("id").equal_to(item_id).get()
    return res.val()


@router.post("")
async def create(request: Request, item: Item):

    item = item.dict()
    print(item)

    return item
