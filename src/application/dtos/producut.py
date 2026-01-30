from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from bson import ObjectId 
from typing import Dict,List
from utils.time import get_utc_now


class ProductBaseDTO(BaseModel):
    id: str
    name: str
    description: Dict
    price: int
    category: List[str]

    create_time: Optional[datetime] = None


class ProductCreateDTO(ProductBaseDTO):
    pass


class ProductUpdateDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[Dict] = {}
    price: Optional[int] = 0
    category:Optional[List] = []
    review_id: Optional[int] = 0

class ProductInDbDTO(ProductBaseDTO):
    review_id: ObjectId

