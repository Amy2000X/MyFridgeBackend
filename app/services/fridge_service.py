from app.database import create_user_client
from datetime import datetime, timedelta
# from services.product_service import get_or_create_product

from datetime import datetime, timedelta

from app.services.product_service import get_or_create_product
from app.database import create_user_client

from app.repositories import fridge_repository


def create_item_from_barcode(jwt, user_id, ean):

    product = get_or_create_product(jwt, ean)

    if product is None:
        raise Exception("Product not found")

    data = fridge_repository.add_fridge_item(jwt, user_id, product)

    return data

def create_item(jwt, user_id, data):
    supabase = create_user_client(jwt)

    product = get_or_create_product(jwt, data.ean)

    response = (
        supabase.table("fridge_items")
        .insert({
            "user_id": user_id,
            "product_id": product["id"],
            "quantity": data.quantity,
            "unit": data.unit.value,
            "status": data.status.value,
            "expire_date": data.expire_date.isoformat()
        })
        .execute()
    )

    return response.data

def get_items(jwt):
    supabase = create_user_client(jwt)

    response = (
    supabase.table("fridge_items")
    .select("""
        *,
        products(*)
    """)
    .execute()
)

    return response.data

def update_item(jwt, item_id, data):
    supabase = create_user_client(jwt)

    response = (
        supabase.table("fridge_items")
        .update({
            "quantity": data.quantity,
            "unit": data.unit.value,
            "status": data.status.value,
            "expire_date": data.expire_date.isoformat()
        })
        .eq("id", item_id)
        .execute()
    )

    return response.data

def delete_item(jwt, item_id):
    supabase = create_user_client(jwt)

    response = (
        supabase.table("fridge_items")
        .delete()
        .eq("id", item_id)
        .execute()
    )

    return response.data