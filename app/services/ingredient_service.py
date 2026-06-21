from ingredient_parser import parse_ingredient


# def split_recipe_ingredients(ingredients: list[str]):
def split_recipe_ingredients():
    ingredients = [
        "1 cup evaporated milk",
        "1 cup whole milk",
        "1 tsp. garlic powder",
        "1 tsp. onion powder",
        "1 tsp. smoked paprika",
        "½ tsp. freshly ground black pepper",
        "1 tsp. kosher salt, plus more",
        "2 lb. extra-sharp cheddar, coarsely grated",
        "4 oz. full-fat cream cheese",
        "1 lb. elbow macaroni"
        ]
    clean_ingredients = []

    for one in ingredients:

        result = parse_ingredient(one)
        clean_ingredients.append(result)
        print(result)



    