from pydantic import BaseModel, ConfigDict
from typing import Optional


class ReviewDictDTO(BaseModel):
    id: int 
    reviws: dict = []

class ReviewDTO(BaseModel):
    id: int
    user_id: int
    rating: float
    text = str