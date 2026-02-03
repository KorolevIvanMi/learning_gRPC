from pydantic import BaseModel,  ConfigDict, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId 
from typing import Dict,List
from src.utils.time import get_utc_now


class ProductBaseDTO(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: str
    name: str
    description: Dict[str, str] = Field(
        default_factory=dict,
        description="Плоский словарь string->string. Не использовать вложенные объекты!"
    )
    price: int
    category: List[str]



class ProductCreateDTO(ProductBaseDTO):
    pass


class ProductUpdateDTO(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: str
    name: Optional[str] = None
    description: Optional[Dict] = {}
    price: Optional[int] = 0
    category:Optional[List] = []
    reviews_id: Optional[ObjectId] = 0

class ProductInDbDTO(ProductBaseDTO):
    review_id: ObjectId

