import requests

from app.config import HEADER_EMAIL
from app.repositories import product_repository

OPENFOODFACTS_URL = "https://world.openfoodfacts.org/api/v3/product"

headers = {
    f"User-Agent": "MyFridge/0.1 ({HEADER_EMAIL})"
}

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

    try:
        url = f"{OPENFOODFACTS_URL}/{ean}.json"
        response = requests.get(url, headers=headers, timeout=10)

        response.raise_for_status()

        data = response.json()

        if data.get("status") == 0:
            return None
        print("Data retreived successfully from API")
        return parse_product(data)

    except Exception as e:
        print("OpenFoodFacts error:", e)
        raise

# Checks in the database if the product exists, if not, adds a new product
def get_or_create_product(jwt: str, ean: str):
    new_ean = normalize_barcode(ean)
    existing = product_repository.get_product(jwt, new_ean)
    print(existing.data)
    
    if existing.data:
        print("product exists in database")
        return existing.data[0]
    print("product does not exist in database")
    print(ean)
    product = fetch_product(ean)

    if product is None:
        return None

    inserted = product_repository.add_new_product(jwt, product)

    return inserted.data[0]

def normalize_barcode(barcode: str) -> str:
    if barcode.startswith("(01)"):
        return barcode[4:18].lstrip("0")

    return barcode.lstrip("0")