from fastapi import APIRouter, Depends, Query

from app.dependencies.auth_dependency import (
    get_current_user
)

from app.schemas.recipe_schema import CookRecipeRequest

from app.services.recipe_service import (
    get_recipes,
    search_recipes,
    cook_recipe
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
    auth=Depends(get_current_user)
):
    return search_recipes(
        auth["token"],
    )

@router.post("/cook")
def cook_recipe_endpoint(
    payload: CookRecipeRequest,
    auth=Depends(
        get_current_user
    )
):
    return cook_recipe(
        auth["token"],
        payload.recipe_id,
        payload.force
    )