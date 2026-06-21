from pydantic import BaseModel
from typing import List


class RecipeResponse(BaseModel):
    id: int
    title: str
    ingredients: List[str]
    instructions: str
    image_name: str
    cleaned_ingredients: List[str]
    
class CookRecipeRequest(BaseModel):
    recipe_id: int
    force: bool = False