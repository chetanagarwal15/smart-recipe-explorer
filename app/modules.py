from pydantic import BaseModel
from typing import List

class Recipe(BaseModel):
    id: str
    name: str
    cuisine: str
    isVegetarian: bool
    prepTimeMinutes: int
    ingredients: List[str]
    difficulty: str
    instructions: str
    tags: List[str]
