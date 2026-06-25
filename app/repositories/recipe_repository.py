from app.database import create_user_client


def get_all_recipes(jwt):
    supabase = create_user_client(jwt)

    response = (
        supabase.table("new_recipes")
        .select("*")
        .execute()
    )

    return response.data

def search_recipes_by_ingredients(jwt, ingredients):
    supabase = create_user_client(jwt)

    response = (
        supabase.table("new_recipes")
        .select("*")
        .execute()
    )

    recipes = response.data

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
    print(recipe_id)
    supabase = create_user_client(jwt)

    response = (
        supabase
        .table("new_recipes")
        .select("*")
        .eq("id", recipe_id)
        .single()
        .execute()
    )
    print(response.data)

    return response.data