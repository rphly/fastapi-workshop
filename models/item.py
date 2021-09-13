from pydantic import BaseModel, validator
from typing import Optional, Literal


class Item(BaseModel):
    category: Literal["phones", "consoles", "tablets"]
    price: float
    title: str
    user: str

    @validator("title")
    def check_title_not_empty(cls, val):
        if len(val) == 0:
            raise ValueError("Title cannot be empty")
        return val

    @validator("price")
    def check_price(cls, val):
        if val < 0:
            raise ValueError("Price must be >= 0.")
        return val
