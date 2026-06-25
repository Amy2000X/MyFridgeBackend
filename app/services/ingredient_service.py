from app.services.translate_service import translate


def get_normalized_fridge_ingredients(fridge_items):
    ingredients = set()

    for item in fridge_items:

        product_name = (
            item["products"]["name"]
        )

        translated = translate(
            product_name
        )

        ingredients.add(
            translated.lower()
        )

    return ingredients