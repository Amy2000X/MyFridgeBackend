from fastapi import APIRouter, Depends, Query

from app.dependencies.auth_dependency import (
    get_current_user
)

from app.services.recipe_service import (
    get_recipes,
    search_recipes
)

router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"]
)


@router.get("/")
def get_all_recipes(
    auth=Depends(get_current_user)
):
    print("in router")
    return get_recipes(
        auth["token"]
    )


@router.get("/search")
def search_recipe(
    ingredients: list[str] = Query(...),
    auth=Depends(get_current_user)
):
    return search_recipes(
        auth["token"],
        ingredients
    )