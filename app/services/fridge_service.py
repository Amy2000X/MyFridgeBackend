from app.database import (
    create_user_client
)

def create_item(jwt, user_id, data):
    supabase = create_user_client(jwt)

    response = (
        supabase.table("fridge_items")
        .insert({
            "user_id": user_id,
            "name": data.name,
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
        .select("*")
        .execute()
    )

    return response.data

