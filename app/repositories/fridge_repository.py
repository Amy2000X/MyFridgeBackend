from datetime import datetime, timedelta

from app.services.product_service import get_or_create_product
from app.database import create_user_client

def add_fridge_item(jwt, user_id, product):

    supabase = create_user_client(jwt)

    response = (
        supabase.table("fridge_items")
        .insert({
            "user_id": user_id,
            "product_id": product["id"],
            "quantity": 1,
            "unit": "pieces",
            "status": "good",
            "expire_date": (
                datetime.utcnow() + timedelta(days=7)
            ).isoformat()
        })
        .execute()
    )

    return response.data

def get_all_items(jwt):
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

def update_fridge_item_quantity(jwt, fridge_item_id, quantity):
    supabase = create_user_client(jwt)

    return (
        supabase
        .table("fridge_items")
        .update({
            "quantity": quantity
        })
        .eq(
            "id",
            fridge_item_id
        )
        .execute()
    )

def delete_item(jwt, item_id):
    supabase = create_user_client(jwt)

    response = (
        supabase.table("fridge_items")
        .delete()
        .eq("id", item_id)
        .execute()
    )

    return response.data

