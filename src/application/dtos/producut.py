from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

from utils.time import get_utc_now


class ProductBase(BaseModel):
    id: str
    name: str
    description: dict
    price: int

    reviews_id: int

    create_time: datetime = get_utc_now

class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[dict] = {}
    price: Optional[int] = 0

    reviews_id: Optional[int] = 0

    create_time: datetime = get_utc_now

