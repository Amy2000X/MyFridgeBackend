from collections import defaultdict

from app.repositories import recipe_repository, fridge_repository

from app.services.ingredient_service import get_normalized_fridge_ingredients
from app.services.translate_service import translate

def get_recipes(jwt):
    response = recipe_repository.get_all_recipes(jwt)
    return response

def search_recipes(jwt):

    fridge_items = (
        fridge_repository.get_all_items(jwt)
    )

    recipes = (
        recipe_repository.get_all_recipes(jwt)
    )

    fridge_ingredients = (
        get_normalized_fridge_ingredients(
            fridge_items
        )
    )

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

    results.sort(
        key=lambda x: x["match_count"],
        reverse=True
    )

    return results[:10]

def cook_recipe(
    jwt,
    recipe_id,
    force=False
):

    recipe = (
        recipe_repository
        .get_recipe_by_id(
            jwt,
            recipe_id
        )
    )

    fridge_items = (
        fridge_repository
        .get_all_items(jwt).data
    )

    inventory = build_inventory(
        fridge_items
    )

    missing_messages = []

    deductions = []

    cleaned = recipe[
        "cleaned_ingredients"
    ]

    amounts = recipe[
        "ingredient_amount"
    ]

    units = recipe[
        "ingredient_unit"
    ]

    for index, ingredient in enumerate(
        cleaned
    ):
        required_amount = (
            amounts[index]
            if index < len(amounts)
            else None
        )

        required_unit = (
            units[index]
            if index < len(units)
            else None
        )

        if required_amount is None:
            continue

        ingredient_items = (
            inventory.get(
                ingredient,
                []
            )
        )

        available_amount = (
            get_available_amount(
                ingredient_items
            )
        )

        if (
            available_amount
            < required_amount
        ):

            missing_messages.append(
                f"{ingredient}: "
                f"need {required_amount}{required_unit}, "
                f"have {available_amount}{required_unit}"
            )

        deductions.append({
            "ingredient": ingredient,
            "required": required_amount,
            "available": available_amount,
            "items": ingredient_items
        })

    if (
        missing_messages
        and not force
    ):
        return {
            "requires_confirmation": True,
            "message": "\n".join(
                missing_messages
            )
        }

    consumed = perform_deduction(jwt, deductions)

    return {
        "success": True,
        "deducted": consumed
    }

def build_inventory(fridge_items):

    inventory = defaultdict(list)

    for item in fridge_items:

        product = item["products"]

        translated_name = translate(
            product["name"]
        )

        inventory[
            translated_name
        ].append(item)

    return inventory

def get_available_amount(fridge_items):
    return sum(
        item["quantity"]
        for item in fridge_items
    )

def perform_deduction(jwt, deductions):
    consumed = []

    for deduction in deductions:

        required = min(
            deduction["required"],
            deduction["available"]
        )

        items = sorted(
            deduction["items"],
            key=lambda x:
                x["expire_date"]
        )

        for item in items:

            if required <= 0:
                break

            current_amount = (
                item["quantity"]
            )

            if current_amount <= required:

                fridge_repository.delete_fridge_item(
                    jwt,
                    item["id"]
                )

                consumed.append({
                    "ingredient": deduction["ingredient"],
                    "item_id": item["id"],
                    "used": current_amount
                })

                required -= current_amount

            else:

                new_amount = (
                    current_amount
                    - required
                )

                fridge_repository.update_fridge_item_quantity(
                    jwt,
                    item["id"],
                    new_amount
                )

                consumed.append({
                    "ingredient": deduction["ingredient"],
                    "item_id": item["id"],
                    "used": required
                })

                required = 0
    return consumed