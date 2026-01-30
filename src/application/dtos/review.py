from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict,List
from bson import ObjectId 

class ReviewDictDTO(BaseModel):
    id: ObjectId
    reviews: Dict[ReviewDTO] = []

class ReviewDTO(BaseModel):
    id: int
    user_id: int
    rating: float
    text = str