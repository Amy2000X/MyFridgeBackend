from app.database import create_user_client


def get_all_recipes(jwt):
    supabase = create_user_client(jwt)
    print("created client")

    response = (
        supabase.table("new_recipes")
        .select("*")
        .execute()
    )
    # print("response excecuted")
    # print(response.data[0])

    return response


# def search_recipes_by_ingredients(jwt, ingredients: list[str]):
#     supabase = create_user_client(jwt)

#     query = (
#         supabase.table("recipes")
#         .select("*")
#     )
#     print(ingredients)

#     # Match ALL ingredients
#     for ingredient in ingredients:
#         query = query.contains(
#             "cleaned_ingredients",
#             [ingredient.lower()]
#         )

#     response = query.execute()

#     return response

def search_recipes_by_ingredients(jwt, ingredients):
    supabase = create_user_client(jwt)

    response = (
        supabase.table("recipes")
        .select("*")
        .execute()
    )

    recipes = response.data
    print("all recipes found:")
    print(recipes)
    matches = []

    for recipe in recipes:
        recipe_ingredients = [
            i.lower()
            for i in recipe["cleaned_ingredients"]
        ]

        if all(
            any(search in ingredient
                for ingredient in recipe_ingredients)
            for search in ingredients
        ):
            matches.append(recipe)

    return matches

def get_recipe_by_id(
    jwt,
    recipe_id
):
    supabase = create_user_client(jwt)

    response = (
        supabase
        .table("new_recipes")
        .select("*")
        .eq("id", recipe_id)
        .single()
        .execute()
    )

    return response.data