from app.database import supabase

def register_user(email: str, password: str):
    response = supabase.auth.sign_up({
        "email": email,
        "password": password
    })

    return response

