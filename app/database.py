from supabase import create_client, Client
from app.config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_user_client(jwt: str):
    client = create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )

    client.postgrest.auth(jwt)

    return client