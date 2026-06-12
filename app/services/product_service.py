from supabase import Client

import requests

# from config.supabase import supabase

from app.database import (
    create_user_client
)

OPENFOODFACTS_URL = "https://world.openfoodfacts.org/api/v2/product"

# Gebruikt Externe API Open Food Facts
def parse_product(product_json: dict):

    product = product_json["product"]
    nutriments = product.get("nutriments", {})

    return {
        "ean": product.get("code"),
        "name": product.get("product_name"),
        "brand": product.get("brands"),
        "quantity": product.get("product_quantity"),
        "unit": product.get("product_quantity_unit"),

        "energy_kcal_100g": nutriments.get("energy-kcal_100g"),
        "fat_100g": nutriments.get("fat_100g"),
        "carbs_100g": nutriments.get("carbohydrates_100g"),
        "protein_100g": nutriments.get("proteins_100g"),
    }

def fetch_product(ean: str):
    print(f"Searching OpenFoodFacts for {ean}")

    response = requests.get(
        f"{OPENFOODFACTS_URL}/{ean}.json"
    )

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("status") == 0:
        return None

    return parse_product(data)

# Checks in the database if the product exists, if not, adds a new product
def get_or_create_product(jwt: str, ean: str):

    supabase = create_user_client(jwt)

    existing = (
        supabase.table("products")
        .select("*")
        .eq("ean", ean)
        .limit(1)
        .execute()
    )

    if existing.data:
        return existing.data[0]

    product = fetch_product(ean)

    if product is None:
        return None

    inserted = (
        supabase.table("products")
        .insert(product)
        .execute()
    )

    return inserted.data[0]

    return insert.data[0]