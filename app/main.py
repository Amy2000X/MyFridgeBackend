# from fastapi import FastAPI
# from .schemas import User


# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/register")
# async def register_user():
#     test = User(email="test@gmail.com", password="Testing123!")

#     response = supabase.auth
#     print(test.email)
#     return {"email:": test.email, "test_password": test.password}

from fastapi import FastAPI
from app.routers.auth_router import router as auth_router
from app.routers.fridge_router import router as fridge_router
from app.routers.recipe_router import router as recipe_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)

app.include_router(auth_router)
app.include_router(fridge_router)
app.include_router(recipe_router)