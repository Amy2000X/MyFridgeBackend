from fastapi import Header, HTTPException
from app.database import supabase


async def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Missing token"
        )

    token = authorization.replace("Bearer ", "")

    try:
        supabase.postgrest.auth(token)
        response = supabase.auth.get_user(token)

        return {
            "token": token,
            "user": response.user
        }

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )