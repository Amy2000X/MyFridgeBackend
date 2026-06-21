from app.repositories import recipe_repository, fridge_repository

from app.services.ingredient_service import get_normalized_fridge_ingredients


def get_recipes(jwt):
    print("service get recipe start")
    response = recipe_repository.get_all_recipes(jwt)

    return response.data

# This is with cleaned ingredients, but they are not clean.
# def search_recipes(jwt, ingredients: list[str]):
#     normalized = [
#         ingredient.strip().lower()
#         for ingredient in ingredients
#     ]

#     response = (
#         recipe_repository.search_recipes_by_ingredients(
#             jwt,
#             normalized
#         )
#     )

#     return response.data

def search_recipes(jwt):

    fridge_items = (
        fridge_repository.get_all_items(jwt)
    ).data

    recipes = (
        recipe_repository.get_all_recipes(jwt)
    ).data

    fridge_ingredients = (
        get_normalized_fridge_ingredients(
            fridge_items
        )
    )
    print(fridge_ingredients)

    results = []

    for recipe in recipes:

        recipe_ingredients = set(
            ingredient.lower()
            for ingredient in recipe[
                "cleaned_ingredients"
            ]
        )

        matches = (
            fridge_ingredients
            &
            recipe_ingredients
        )

        missing = (
            recipe_ingredients
            -
            fridge_ingredients
        )

        results.append({
            "recipe": recipe,
            "match_count": len(matches),
            "total_ingredients": len(
                recipe_ingredients
            ),
            "matched_ingredients": list(
                matches
            ),
            "missing_ingredients": list(
                missing
            )
        })
    print("FRIDGE INGREDIENTS:")
    print(fridge_ingredients)

    print("RECIPE INGREDIENTS:")
    print(recipe["cleaned_ingredients"])

    results.sort(
        key=lambda x: x["match_count"],
        reverse=True
    )

    return results[:10]