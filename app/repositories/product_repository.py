from supabase import Client

import requests

# from config.supabase import supabase

from app.database import create_user_client
from app.config import HEADER_EMAIL

OPENFOODFACTS_URL = "https://world.openfoodfacts.org/api/v3/product"

def get_product(jwt: str, ean: str):

    supabase = create_user_client(jwt)

    response = (
        supabase.table("products")
        .select("*")
        .eq("ean", ean)
        .limit(1)
        .execute()
    )
    return response
    
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

def add_new_product(jwt, product):
    supabase = create_user_client(jwt)

    inserted = (
        supabase.table("products")
        .insert(product)
        .execute()
    )

    return inserted
