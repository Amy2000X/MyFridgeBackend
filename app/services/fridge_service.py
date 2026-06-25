
from app.services.product_service import get_or_create_product

from app.repositories import fridge_repository

def create_item_from_barcode(jwt, user_id, ean):

    product = get_or_create_product(jwt, ean)

    if product is None:
        raise Exception("Product not found")

    response = fridge_repository.add_fridge_item(jwt, user_id, product)

    return response

def get_items(jwt):
    return fridge_repository.get_all_items(jwt)
    
def update_item(jwt, item_id, data):
    return fridge_repository.update_item(jwt, item_id, data)


def delete_item(jwt, item_id):
    return fridge_repository.delete_item(jwt, item_id)
