from pydantic import BaseModel, ConfigDict
from typing import Optional


class ReviewDict(BaseModel):
    id: int 
    reviws: dict = []

class Review(BaseModel):
    id: int
    user_id: int
    rating: float
    text = str