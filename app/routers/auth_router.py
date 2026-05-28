from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import (
    RegisterRequest,
    LoginRequest
)
from app.services.auth_service import (
    register_user,
    login_user,
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
    
@router.post("/login")
def login(data: LoginRequest):
    try: 
        response = login_user(
            data.email,
            data.password
        )

        return {
            "message": "Login successful",
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token,
            "user": response.user
        }
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
