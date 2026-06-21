from rapidfuzz import fuzz

def is_match(
    fridge_ingredient: str,
    recipe_ingredient: str,
    threshold: int = 80
    ):

    score = fuzz.token_set_ratio(
        fridge_ingredient.lower(),
        recipe_ingredient.lower()
    )

    return score >= threshold


def calculate_match(
    fridge_ingredients,
    recipe_ingredients
    ):

    found = []
    missing = []

    for ingredient in recipe_ingredients:
        matched = False

        for fridge in fridge_ingredients:
            if is_match(fridge, ingredient):
                matched = True
                break

        if matched:
            found.append(ingredient)

        else:
            missing.append(ingredient)

    percentage = 0
    
    if len(recipe_ingredients) > 0:

        percentage = int(
            len(found)
            / len(recipe_ingredients)
            * 100
        )

    return percentage, missing