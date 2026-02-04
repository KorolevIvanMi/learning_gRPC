from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict,List
from bson import ObjectId 

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


class ReviewDTO(BaseModel):
    id: int
    user_id: int
    rating: float
    text : str
    model_config = ConfigDict(from_attributes=True)

class ReviewDictDTO(BaseModel):
    id: PyObjectId 
    reviews: List = []
    model_config = ConfigDict(
        arbitrary_types_allowed=True  
    )