from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

from utils.time import get_utc_now


class ProductBaseDTO(BaseModel):
    id: str
    name: str
    description: dict
    price: int
    category: list
    reviews_id: int

    create_time: Optional[datetime] = None


class ProductCreateDTO(ProductBaseDTO):
    pass


class ProductUpdateDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[dict] = {}
    price: Optional[int] = 0
    category:Optional[list] = []
    reviews_id: Optional[int] = 0

    

