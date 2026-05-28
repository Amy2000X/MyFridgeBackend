from fastapi import APIRouter, HTTPException
from app.schemas import (
    RegisterRequest,
)
from app.services.auth_service import (
    register_user,
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(data: RegisterRequest):
    try:
        response = register_user(
            data.email,
            data.password
        )

        return {
            "message": "User registered",
            "user": response.user
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
