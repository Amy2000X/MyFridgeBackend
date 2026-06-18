from app.database import create_user_client
from datetime import datetime, timedelta
# from services.product_service import get_or_create_product

from datetime import datetime, timedelta

from app.services.product_service import get_or_create_product
from app.database import create_user_client

def add_fridge_item(jwt, user_id, product):

    supabase = create_user_client(jwt)

    # product = get_or_create_product(jwt, ean)

    # if product is None:
    #     raise Exception("Product not found")

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

