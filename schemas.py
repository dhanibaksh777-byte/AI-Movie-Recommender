from pydantic import BaseModel,Field
from typing import List


class Recommendation(BaseModel):
    title : str
    year : int
    director : str
    genres : List[str]
    reason : str
    summary : str


class MovieResponse(BaseModel):
    user_request : str = Field(min_length=10,max_length=150)
    response : List[Recommendation]



