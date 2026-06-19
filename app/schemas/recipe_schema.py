from typing import List, Optional
from pydantic import BaseModel


class RecipeIngredient(BaseModel):
    name: str
    available: bool


class RecipeSummary(BaseModel):
    id: str
    name: str
    image: str
    match_percentage: int
    missing_ingredients: List[str]


class RecipeDetail(BaseModel):
    id: str
    name: str
    image: str
    category: str
    cuisine: str
    instructions: str
    ingredients: List[RecipeIngredient]

class SearchRecipesRequest(BaseModel):
    cuisine: Optional[str] = None