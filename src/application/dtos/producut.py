from pydantic import BaseModel,  ConfigDict, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId 
from typing import Dict,List
from src.utils.time import get_utc_now

class PyObjectId(str):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        return handler(str)
    
    @classmethod
    def validate(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        if isinstance(v, str):
            try:
                ObjectId(v)  # Проверяем что это валидный ObjectId
                return v
            except:
                raise ValueError("Invalid ObjectId")
        raise TypeError("ObjectId or string required")


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
    product_id: str 
    name: Optional[str] = None
    description: Optional[Dict] = {}
    price: Optional[int] = 0
    category:Optional[List] = []
    reviews_id: Optional[PyObjectId] = 0

    model_config = ConfigDict(
        arbitrary_types_allowed=True  
    )


class ProductInDbDTO(ProductBaseDTO):
    review_id: PyObjectId

    model_config = ConfigDict(
        arbitrary_types_allowed=True  
    )