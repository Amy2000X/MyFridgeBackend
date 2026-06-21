from app.repositories import recipe_repository, fridge_repository


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

def search_recipes(jwt, ingredients):
    normalized = [
        ingredient.strip().lower()
        for ingredient in ingredients
    ]

    return recipe_repository.search_recipes_by_ingredients(
        jwt,
        normalized
    )
